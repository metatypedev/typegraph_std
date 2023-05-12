from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_datalabeling() -> Import:
    datalabeling = HTTPRuntime("https://datalabeling.googleapis.com/")

    renames = {
        "ErrorResponse": "_datalabeling_1_ErrorResponse",
        "GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataIn": "_datalabeling_2_GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataOut": "_datalabeling_3_GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1ObjectTrackingFrameIn": "_datalabeling_4_GoogleCloudDatalabelingV1beta1ObjectTrackingFrameIn",
        "GoogleCloudDatalabelingV1beta1ObjectTrackingFrameOut": "_datalabeling_5_GoogleCloudDatalabelingV1beta1ObjectTrackingFrameOut",
        "GoogleCloudDatalabelingV1alpha1GcsDestinationIn": "_datalabeling_6_GoogleCloudDatalabelingV1alpha1GcsDestinationIn",
        "GoogleCloudDatalabelingV1alpha1GcsDestinationOut": "_datalabeling_7_GoogleCloudDatalabelingV1alpha1GcsDestinationOut",
        "GoogleCloudDatalabelingV1beta1VideoThumbnailIn": "_datalabeling_8_GoogleCloudDatalabelingV1beta1VideoThumbnailIn",
        "GoogleCloudDatalabelingV1beta1VideoThumbnailOut": "_datalabeling_9_GoogleCloudDatalabelingV1beta1VideoThumbnailOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataIn": "_datalabeling_10_GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataOut": "_datalabeling_11_GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1GcsDestinationIn": "_datalabeling_12_GoogleCloudDatalabelingV1p2alpha1GcsDestinationIn",
        "GoogleCloudDatalabelingV1p2alpha1GcsDestinationOut": "_datalabeling_13_GoogleCloudDatalabelingV1p2alpha1GcsDestinationOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataIn": "_datalabeling_14_GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataOut": "_datalabeling_15_GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataIn": "_datalabeling_16_GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataOut": "_datalabeling_17_GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1TextPayloadIn": "_datalabeling_18_GoogleCloudDatalabelingV1beta1TextPayloadIn",
        "GoogleCloudDatalabelingV1beta1TextPayloadOut": "_datalabeling_19_GoogleCloudDatalabelingV1beta1TextPayloadOut",
        "GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataIn": "_datalabeling_20_GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataOut": "_datalabeling_21_GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataIn": "_datalabeling_22_GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataOut": "_datalabeling_23_GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1SequentialSegmentIn": "_datalabeling_24_GoogleCloudDatalabelingV1beta1SequentialSegmentIn",
        "GoogleCloudDatalabelingV1beta1SequentialSegmentOut": "_datalabeling_25_GoogleCloudDatalabelingV1beta1SequentialSegmentOut",
        "GoogleCloudDatalabelingV1beta1PdfInstructionIn": "_datalabeling_26_GoogleCloudDatalabelingV1beta1PdfInstructionIn",
        "GoogleCloudDatalabelingV1beta1PdfInstructionOut": "_datalabeling_27_GoogleCloudDatalabelingV1beta1PdfInstructionOut",
        "GoogleCloudDatalabelingV1beta1LabelImageRequestIn": "_datalabeling_28_GoogleCloudDatalabelingV1beta1LabelImageRequestIn",
        "GoogleCloudDatalabelingV1beta1LabelImageRequestOut": "_datalabeling_29_GoogleCloudDatalabelingV1beta1LabelImageRequestOut",
        "GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryIn": "_datalabeling_30_GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryIn",
        "GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryOut": "_datalabeling_31_GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataIn": "_datalabeling_32_GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataOut": "_datalabeling_33_GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataOut",
        "GoogleCloudDatalabelingV1alpha1LabelStatsIn": "_datalabeling_34_GoogleCloudDatalabelingV1alpha1LabelStatsIn",
        "GoogleCloudDatalabelingV1alpha1LabelStatsOut": "_datalabeling_35_GoogleCloudDatalabelingV1alpha1LabelStatsOut",
        "GoogleLongrunningOperationIn": "_datalabeling_36_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_datalabeling_37_GoogleLongrunningOperationOut",
        "GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataIn": "_datalabeling_38_GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataOut": "_datalabeling_39_GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1TextMetadataIn": "_datalabeling_40_GoogleCloudDatalabelingV1beta1TextMetadataIn",
        "GoogleCloudDatalabelingV1beta1TextMetadataOut": "_datalabeling_41_GoogleCloudDatalabelingV1beta1TextMetadataOut",
        "GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequestIn": "_datalabeling_42_GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequestIn",
        "GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequestOut": "_datalabeling_43_GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequestOut",
        "GoogleCloudDatalabelingV1alpha1CreateInstructionMetadataIn": "_datalabeling_44_GoogleCloudDatalabelingV1alpha1CreateInstructionMetadataIn",
        "GoogleCloudDatalabelingV1alpha1CreateInstructionMetadataOut": "_datalabeling_45_GoogleCloudDatalabelingV1alpha1CreateInstructionMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataIn": "_datalabeling_46_GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataOut": "_datalabeling_47_GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn": "_datalabeling_48_GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn",
        "GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut": "_datalabeling_49_GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut",
        "GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataIn": "_datalabeling_50_GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataOut": "_datalabeling_51_GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataOut",
        "GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataIn": "_datalabeling_52_GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataOut": "_datalabeling_53_GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadataIn": "_datalabeling_54_GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadataOut": "_datalabeling_55_GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadataOut",
        "GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponseIn": "_datalabeling_56_GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponseIn",
        "GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponseOut": "_datalabeling_57_GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponseOut",
        "GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataIn": "_datalabeling_58_GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataIn",
        "GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataOut": "_datalabeling_59_GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataIn": "_datalabeling_60_GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataOut": "_datalabeling_61_GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1CreateInstructionRequestIn": "_datalabeling_62_GoogleCloudDatalabelingV1beta1CreateInstructionRequestIn",
        "GoogleCloudDatalabelingV1beta1CreateInstructionRequestOut": "_datalabeling_63_GoogleCloudDatalabelingV1beta1CreateInstructionRequestOut",
        "GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataIn": "_datalabeling_64_GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataOut": "_datalabeling_65_GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelStatsIn": "_datalabeling_66_GoogleCloudDatalabelingV1p1alpha1LabelStatsIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelStatsOut": "_datalabeling_67_GoogleCloudDatalabelingV1p1alpha1LabelStatsOut",
        "GoogleCloudDatalabelingV1beta1ImageClassificationConfigIn": "_datalabeling_68_GoogleCloudDatalabelingV1beta1ImageClassificationConfigIn",
        "GoogleCloudDatalabelingV1beta1ImageClassificationConfigOut": "_datalabeling_69_GoogleCloudDatalabelingV1beta1ImageClassificationConfigOut",
        "GoogleCloudDatalabelingV1beta1PolylineIn": "_datalabeling_70_GoogleCloudDatalabelingV1beta1PolylineIn",
        "GoogleCloudDatalabelingV1beta1PolylineOut": "_datalabeling_71_GoogleCloudDatalabelingV1beta1PolylineOut",
        "GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadataIn": "_datalabeling_72_GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadataOut": "_datalabeling_73_GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1TimeSegmentIn": "_datalabeling_74_GoogleCloudDatalabelingV1beta1TimeSegmentIn",
        "GoogleCloudDatalabelingV1beta1TimeSegmentOut": "_datalabeling_75_GoogleCloudDatalabelingV1beta1TimeSegmentOut",
        "GoogleCloudDatalabelingV1beta1ListDatasetsResponseIn": "_datalabeling_76_GoogleCloudDatalabelingV1beta1ListDatasetsResponseIn",
        "GoogleCloudDatalabelingV1beta1ListDatasetsResponseOut": "_datalabeling_77_GoogleCloudDatalabelingV1beta1ListDatasetsResponseOut",
        "GoogleCloudDatalabelingV1beta1EvaluationJobConfigIn": "_datalabeling_78_GoogleCloudDatalabelingV1beta1EvaluationJobConfigIn",
        "GoogleCloudDatalabelingV1beta1EvaluationJobConfigOut": "_datalabeling_79_GoogleCloudDatalabelingV1beta1EvaluationJobConfigOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataIn": "_datalabeling_80_GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataOut": "_datalabeling_81_GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1PolylineConfigIn": "_datalabeling_82_GoogleCloudDatalabelingV1beta1PolylineConfigIn",
        "GoogleCloudDatalabelingV1beta1PolylineConfigOut": "_datalabeling_83_GoogleCloudDatalabelingV1beta1PolylineConfigOut",
        "GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryIn": "_datalabeling_84_GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryIn",
        "GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryOut": "_datalabeling_85_GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryOut",
        "GoogleCloudDatalabelingV1beta1ExportDataOperationResponseIn": "_datalabeling_86_GoogleCloudDatalabelingV1beta1ExportDataOperationResponseIn",
        "GoogleCloudDatalabelingV1beta1ExportDataOperationResponseOut": "_datalabeling_87_GoogleCloudDatalabelingV1beta1ExportDataOperationResponseOut",
        "GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationIn": "_datalabeling_88_GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationIn",
        "GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationOut": "_datalabeling_89_GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationOut",
        "GoogleCloudDatalabelingV1beta1TextClassificationConfigIn": "_datalabeling_90_GoogleCloudDatalabelingV1beta1TextClassificationConfigIn",
        "GoogleCloudDatalabelingV1beta1TextClassificationConfigOut": "_datalabeling_91_GoogleCloudDatalabelingV1beta1TextClassificationConfigOut",
        "GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadataIn": "_datalabeling_92_GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadataOut": "_datalabeling_93_GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadataOut",
        "GoogleCloudDatalabelingV1beta1NormalizedPolylineIn": "_datalabeling_94_GoogleCloudDatalabelingV1beta1NormalizedPolylineIn",
        "GoogleCloudDatalabelingV1beta1NormalizedPolylineOut": "_datalabeling_95_GoogleCloudDatalabelingV1beta1NormalizedPolylineOut",
        "GoogleCloudDatalabelingV1p1alpha1GcsDestinationIn": "_datalabeling_96_GoogleCloudDatalabelingV1p1alpha1GcsDestinationIn",
        "GoogleCloudDatalabelingV1p1alpha1GcsDestinationOut": "_datalabeling_97_GoogleCloudDatalabelingV1p1alpha1GcsDestinationOut",
        "GoogleCloudDatalabelingV1p1alpha1OutputConfigIn": "_datalabeling_98_GoogleCloudDatalabelingV1p1alpha1OutputConfigIn",
        "GoogleCloudDatalabelingV1p1alpha1OutputConfigOut": "_datalabeling_99_GoogleCloudDatalabelingV1p1alpha1OutputConfigOut",
        "GoogleCloudDatalabelingV1beta1ClassificationMetadataIn": "_datalabeling_100_GoogleCloudDatalabelingV1beta1ClassificationMetadataIn",
        "GoogleCloudDatalabelingV1beta1ClassificationMetadataOut": "_datalabeling_101_GoogleCloudDatalabelingV1beta1ClassificationMetadataOut",
        "GoogleCloudDatalabelingV1beta1LabelStatsIn": "_datalabeling_102_GoogleCloudDatalabelingV1beta1LabelStatsIn",
        "GoogleCloudDatalabelingV1beta1LabelStatsOut": "_datalabeling_103_GoogleCloudDatalabelingV1beta1LabelStatsOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataIn": "_datalabeling_104_GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataOut": "_datalabeling_105_GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1RowIn": "_datalabeling_106_GoogleCloudDatalabelingV1beta1RowIn",
        "GoogleCloudDatalabelingV1beta1RowOut": "_datalabeling_107_GoogleCloudDatalabelingV1beta1RowOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataIn": "_datalabeling_108_GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataOut": "_datalabeling_109_GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadataIn": "_datalabeling_110_GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadataOut": "_datalabeling_111_GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1LabelVideoRequestIn": "_datalabeling_112_GoogleCloudDatalabelingV1beta1LabelVideoRequestIn",
        "GoogleCloudDatalabelingV1beta1LabelVideoRequestOut": "_datalabeling_113_GoogleCloudDatalabelingV1beta1LabelVideoRequestOut",
        "GoogleCloudDatalabelingV1beta1ImportDataOperationResponseIn": "_datalabeling_114_GoogleCloudDatalabelingV1beta1ImportDataOperationResponseIn",
        "GoogleCloudDatalabelingV1beta1ImportDataOperationResponseOut": "_datalabeling_115_GoogleCloudDatalabelingV1beta1ImportDataOperationResponseOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataIn": "_datalabeling_116_GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataOut": "_datalabeling_117_GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1EvaluationMetricsIn": "_datalabeling_118_GoogleCloudDatalabelingV1beta1EvaluationMetricsIn",
        "GoogleCloudDatalabelingV1beta1EvaluationMetricsOut": "_datalabeling_119_GoogleCloudDatalabelingV1beta1EvaluationMetricsOut",
        "GoogleCloudDatalabelingV1beta1AnnotationMetadataIn": "_datalabeling_120_GoogleCloudDatalabelingV1beta1AnnotationMetadataIn",
        "GoogleCloudDatalabelingV1beta1AnnotationMetadataOut": "_datalabeling_121_GoogleCloudDatalabelingV1beta1AnnotationMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataIn": "_datalabeling_122_GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataOut": "_datalabeling_123_GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1ImportDataOperationMetadataIn": "_datalabeling_124_GoogleCloudDatalabelingV1beta1ImportDataOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1ImportDataOperationMetadataOut": "_datalabeling_125_GoogleCloudDatalabelingV1beta1ImportDataOperationMetadataOut",
        "GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataIn": "_datalabeling_126_GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataOut": "_datalabeling_127_GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1VideoClassificationConfigIn": "_datalabeling_128_GoogleCloudDatalabelingV1beta1VideoClassificationConfigIn",
        "GoogleCloudDatalabelingV1beta1VideoClassificationConfigOut": "_datalabeling_129_GoogleCloudDatalabelingV1beta1VideoClassificationConfigOut",
        "GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseIn": "_datalabeling_130_GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseIn",
        "GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseOut": "_datalabeling_131_GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataIn": "_datalabeling_132_GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataOut": "_datalabeling_133_GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationIn": "_datalabeling_134_GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationIn",
        "GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationOut": "_datalabeling_135_GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationOut",
        "GoogleCloudDatalabelingV1beta1EvaluationConfigIn": "_datalabeling_136_GoogleCloudDatalabelingV1beta1EvaluationConfigIn",
        "GoogleCloudDatalabelingV1beta1EvaluationConfigOut": "_datalabeling_137_GoogleCloudDatalabelingV1beta1EvaluationConfigOut",
        "GoogleCloudDatalabelingV1beta1LabelTextRequestIn": "_datalabeling_138_GoogleCloudDatalabelingV1beta1LabelTextRequestIn",
        "GoogleCloudDatalabelingV1beta1LabelTextRequestOut": "_datalabeling_139_GoogleCloudDatalabelingV1beta1LabelTextRequestOut",
        "GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseIn": "_datalabeling_140_GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseIn",
        "GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseOut": "_datalabeling_141_GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseOut",
        "GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponseIn": "_datalabeling_142_GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponseIn",
        "GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponseOut": "_datalabeling_143_GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponseOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadataIn": "_datalabeling_144_GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadataOut": "_datalabeling_145_GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1EvaluationJobIn": "_datalabeling_146_GoogleCloudDatalabelingV1beta1EvaluationJobIn",
        "GoogleCloudDatalabelingV1beta1EvaluationJobOut": "_datalabeling_147_GoogleCloudDatalabelingV1beta1EvaluationJobOut",
        "GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn": "_datalabeling_148_GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn",
        "GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut": "_datalabeling_149_GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut",
        "GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataIn": "_datalabeling_150_GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataOut": "_datalabeling_151_GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponseIn": "_datalabeling_152_GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponseIn",
        "GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponseOut": "_datalabeling_153_GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponseOut",
        "GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataIn": "_datalabeling_154_GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataOut": "_datalabeling_155_GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1AnnotationIn": "_datalabeling_156_GoogleCloudDatalabelingV1beta1AnnotationIn",
        "GoogleCloudDatalabelingV1beta1AnnotationOut": "_datalabeling_157_GoogleCloudDatalabelingV1beta1AnnotationOut",
        "GoogleCloudDatalabelingV1beta1VideoEventAnnotationIn": "_datalabeling_158_GoogleCloudDatalabelingV1beta1VideoEventAnnotationIn",
        "GoogleCloudDatalabelingV1beta1VideoEventAnnotationOut": "_datalabeling_159_GoogleCloudDatalabelingV1beta1VideoEventAnnotationOut",
        "GoogleCloudDatalabelingV1alpha1LabelOperationMetadataIn": "_datalabeling_160_GoogleCloudDatalabelingV1alpha1LabelOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelOperationMetadataOut": "_datalabeling_161_GoogleCloudDatalabelingV1alpha1LabelOperationMetadataOut",
        "GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataIn": "_datalabeling_162_GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataOut": "_datalabeling_163_GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataIn": "_datalabeling_164_GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataOut": "_datalabeling_165_GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1InputConfigIn": "_datalabeling_166_GoogleCloudDatalabelingV1beta1InputConfigIn",
        "GoogleCloudDatalabelingV1beta1InputConfigOut": "_datalabeling_167_GoogleCloudDatalabelingV1beta1InputConfigOut",
        "GoogleCloudDatalabelingV1beta1GcsSourceIn": "_datalabeling_168_GoogleCloudDatalabelingV1beta1GcsSourceIn",
        "GoogleCloudDatalabelingV1beta1GcsSourceOut": "_datalabeling_169_GoogleCloudDatalabelingV1beta1GcsSourceOut",
        "GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataIn": "_datalabeling_170_GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataOut": "_datalabeling_171_GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseIn": "_datalabeling_172_GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseIn",
        "GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseOut": "_datalabeling_173_GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseOut",
        "GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsIn": "_datalabeling_174_GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsIn",
        "GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsOut": "_datalabeling_175_GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsOut",
        "GoogleCloudDatalabelingV1beta1AnnotationValueIn": "_datalabeling_176_GoogleCloudDatalabelingV1beta1AnnotationValueIn",
        "GoogleCloudDatalabelingV1beta1AnnotationValueOut": "_datalabeling_177_GoogleCloudDatalabelingV1beta1AnnotationValueOut",
        "GoogleCloudDatalabelingV1beta1VideoPayloadIn": "_datalabeling_178_GoogleCloudDatalabelingV1beta1VideoPayloadIn",
        "GoogleCloudDatalabelingV1beta1VideoPayloadOut": "_datalabeling_179_GoogleCloudDatalabelingV1beta1VideoPayloadOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataIn": "_datalabeling_180_GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataOut": "_datalabeling_181_GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationIn": "_datalabeling_182_GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationIn",
        "GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationOut": "_datalabeling_183_GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationOut",
        "GoogleCloudDatalabelingV1beta1NormalizedVertexIn": "_datalabeling_184_GoogleCloudDatalabelingV1beta1NormalizedVertexIn",
        "GoogleCloudDatalabelingV1beta1NormalizedVertexOut": "_datalabeling_185_GoogleCloudDatalabelingV1beta1NormalizedVertexOut",
        "GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationIn": "_datalabeling_186_GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationIn",
        "GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationOut": "_datalabeling_187_GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationOut",
        "GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn": "_datalabeling_188_GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn",
        "GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataOut": "_datalabeling_189_GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataOut",
        "GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataIn": "_datalabeling_190_GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataOut": "_datalabeling_191_GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1DatasetIn": "_datalabeling_192_GoogleCloudDatalabelingV1beta1DatasetIn",
        "GoogleCloudDatalabelingV1beta1DatasetOut": "_datalabeling_193_GoogleCloudDatalabelingV1beta1DatasetOut",
        "GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationIn": "_datalabeling_194_GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationIn",
        "GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationOut": "_datalabeling_195_GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationOut",
        "GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataIn": "_datalabeling_196_GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataOut": "_datalabeling_197_GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataOut",
        "GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadataIn": "_datalabeling_198_GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadataOut": "_datalabeling_199_GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1EvaluationIn": "_datalabeling_200_GoogleCloudDatalabelingV1beta1EvaluationIn",
        "GoogleCloudDatalabelingV1beta1EvaluationOut": "_datalabeling_201_GoogleCloudDatalabelingV1beta1EvaluationOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataIn": "_datalabeling_202_GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataOut": "_datalabeling_203_GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataOut",
        "GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn": "_datalabeling_204_GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut": "_datalabeling_205_GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1TextClassificationAnnotationIn": "_datalabeling_206_GoogleCloudDatalabelingV1beta1TextClassificationAnnotationIn",
        "GoogleCloudDatalabelingV1beta1TextClassificationAnnotationOut": "_datalabeling_207_GoogleCloudDatalabelingV1beta1TextClassificationAnnotationOut",
        "GoogleCloudDatalabelingV1beta1SentimentConfigIn": "_datalabeling_208_GoogleCloudDatalabelingV1beta1SentimentConfigIn",
        "GoogleCloudDatalabelingV1beta1SentimentConfigOut": "_datalabeling_209_GoogleCloudDatalabelingV1beta1SentimentConfigOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataIn": "_datalabeling_210_GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataOut": "_datalabeling_211_GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataIn": "_datalabeling_212_GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataOut": "_datalabeling_213_GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1EventConfigIn": "_datalabeling_214_GoogleCloudDatalabelingV1beta1EventConfigIn",
        "GoogleCloudDatalabelingV1beta1EventConfigOut": "_datalabeling_215_GoogleCloudDatalabelingV1beta1EventConfigOut",
        "GoogleCloudDatalabelingV1beta1ListInstructionsResponseIn": "_datalabeling_216_GoogleCloudDatalabelingV1beta1ListInstructionsResponseIn",
        "GoogleCloudDatalabelingV1beta1ListInstructionsResponseOut": "_datalabeling_217_GoogleCloudDatalabelingV1beta1ListInstructionsResponseOut",
        "GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataIn": "_datalabeling_218_GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataOut": "_datalabeling_219_GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequestIn": "_datalabeling_220_GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequestIn",
        "GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequestOut": "_datalabeling_221_GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequestOut",
        "GoogleCloudDatalabelingV1beta1ObjectDetectionConfigIn": "_datalabeling_222_GoogleCloudDatalabelingV1beta1ObjectDetectionConfigIn",
        "GoogleCloudDatalabelingV1beta1ObjectDetectionConfigOut": "_datalabeling_223_GoogleCloudDatalabelingV1beta1ObjectDetectionConfigOut",
        "GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigIn": "_datalabeling_224_GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigIn",
        "GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigOut": "_datalabeling_225_GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigOut",
        "GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataIn": "_datalabeling_226_GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataOut": "_datalabeling_227_GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1ListDataItemsResponseIn": "_datalabeling_228_GoogleCloudDatalabelingV1beta1ListDataItemsResponseIn",
        "GoogleCloudDatalabelingV1beta1ListDataItemsResponseOut": "_datalabeling_229_GoogleCloudDatalabelingV1beta1ListDataItemsResponseOut",
        "GoogleCloudDatalabelingV1beta1OperatorMetadataIn": "_datalabeling_230_GoogleCloudDatalabelingV1beta1OperatorMetadataIn",
        "GoogleCloudDatalabelingV1beta1OperatorMetadataOut": "_datalabeling_231_GoogleCloudDatalabelingV1beta1OperatorMetadataOut",
        "GoogleCloudDatalabelingV1beta1PrCurveIn": "_datalabeling_232_GoogleCloudDatalabelingV1beta1PrCurveIn",
        "GoogleCloudDatalabelingV1beta1PrCurveOut": "_datalabeling_233_GoogleCloudDatalabelingV1beta1PrCurveOut",
        "GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequestIn": "_datalabeling_234_GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequestIn",
        "GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequestOut": "_datalabeling_235_GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequestOut",
        "GoogleProtobufEmptyIn": "_datalabeling_236_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_datalabeling_237_GoogleProtobufEmptyOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataIn": "_datalabeling_238_GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataOut": "_datalabeling_239_GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelStatsIn": "_datalabeling_240_GoogleCloudDatalabelingV1p2alpha1LabelStatsIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelStatsOut": "_datalabeling_241_GoogleCloudDatalabelingV1p2alpha1LabelStatsOut",
        "GoogleCloudDatalabelingV1beta1AnnotationSpecSetIn": "_datalabeling_242_GoogleCloudDatalabelingV1beta1AnnotationSpecSetIn",
        "GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut": "_datalabeling_243_GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut",
        "GoogleCloudDatalabelingV1beta1ObjectTrackingConfigIn": "_datalabeling_244_GoogleCloudDatalabelingV1beta1ObjectTrackingConfigIn",
        "GoogleCloudDatalabelingV1beta1ObjectTrackingConfigOut": "_datalabeling_245_GoogleCloudDatalabelingV1beta1ObjectTrackingConfigOut",
        "GoogleCloudDatalabelingV1p2alpha1OutputConfigIn": "_datalabeling_246_GoogleCloudDatalabelingV1p2alpha1OutputConfigIn",
        "GoogleCloudDatalabelingV1p2alpha1OutputConfigOut": "_datalabeling_247_GoogleCloudDatalabelingV1p2alpha1OutputConfigOut",
        "GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn": "_datalabeling_248_GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn",
        "GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut": "_datalabeling_249_GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut",
        "GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataIn": "_datalabeling_250_GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataOut": "_datalabeling_251_GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsIn": "_datalabeling_252_GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsIn",
        "GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsOut": "_datalabeling_253_GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsOut",
        "GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataIn": "_datalabeling_254_GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataOut": "_datalabeling_255_GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1GcsFolderDestinationIn": "_datalabeling_256_GoogleCloudDatalabelingV1beta1GcsFolderDestinationIn",
        "GoogleCloudDatalabelingV1beta1GcsFolderDestinationOut": "_datalabeling_257_GoogleCloudDatalabelingV1beta1GcsFolderDestinationOut",
        "GoogleCloudDatalabelingV1alpha1GcsFolderDestinationIn": "_datalabeling_258_GoogleCloudDatalabelingV1alpha1GcsFolderDestinationIn",
        "GoogleCloudDatalabelingV1alpha1GcsFolderDestinationOut": "_datalabeling_259_GoogleCloudDatalabelingV1alpha1GcsFolderDestinationOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn": "_datalabeling_260_GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut": "_datalabeling_261_GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut",
        "GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataIn": "_datalabeling_262_GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataOut": "_datalabeling_263_GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn": "_datalabeling_264_GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn",
        "GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataOut": "_datalabeling_265_GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataOut",
        "GoogleCloudDatalabelingV1beta1ConfusionMatrixIn": "_datalabeling_266_GoogleCloudDatalabelingV1beta1ConfusionMatrixIn",
        "GoogleCloudDatalabelingV1beta1ConfusionMatrixOut": "_datalabeling_267_GoogleCloudDatalabelingV1beta1ConfusionMatrixOut",
        "GoogleCloudDatalabelingV1beta1ImagePayloadIn": "_datalabeling_268_GoogleCloudDatalabelingV1beta1ImagePayloadIn",
        "GoogleCloudDatalabelingV1beta1ImagePayloadOut": "_datalabeling_269_GoogleCloudDatalabelingV1beta1ImagePayloadOut",
        "GoogleRpcStatusIn": "_datalabeling_270_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_datalabeling_271_GoogleRpcStatusOut",
        "GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseIn": "_datalabeling_272_GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseIn",
        "GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseOut": "_datalabeling_273_GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataIn": "_datalabeling_274_GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataOut": "_datalabeling_275_GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadataIn": "_datalabeling_276_GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadataOut": "_datalabeling_277_GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1CreateInstructionMetadataIn": "_datalabeling_278_GoogleCloudDatalabelingV1beta1CreateInstructionMetadataIn",
        "GoogleCloudDatalabelingV1beta1CreateInstructionMetadataOut": "_datalabeling_279_GoogleCloudDatalabelingV1beta1CreateInstructionMetadataOut",
        "GoogleCloudDatalabelingV1beta1ExampleComparisonIn": "_datalabeling_280_GoogleCloudDatalabelingV1beta1ExampleComparisonIn",
        "GoogleCloudDatalabelingV1beta1ExampleComparisonOut": "_datalabeling_281_GoogleCloudDatalabelingV1beta1ExampleComparisonOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataIn": "_datalabeling_282_GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataOut": "_datalabeling_283_GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1FeedbackMessageIn": "_datalabeling_284_GoogleCloudDatalabelingV1beta1FeedbackMessageIn",
        "GoogleCloudDatalabelingV1beta1FeedbackMessageOut": "_datalabeling_285_GoogleCloudDatalabelingV1beta1FeedbackMessageOut",
        "GoogleCloudDatalabelingV1beta1CreateDatasetRequestIn": "_datalabeling_286_GoogleCloudDatalabelingV1beta1CreateDatasetRequestIn",
        "GoogleCloudDatalabelingV1beta1CreateDatasetRequestOut": "_datalabeling_287_GoogleCloudDatalabelingV1beta1CreateDatasetRequestOut",
        "GoogleCloudDatalabelingV1beta1ExportDataRequestIn": "_datalabeling_288_GoogleCloudDatalabelingV1beta1ExportDataRequestIn",
        "GoogleCloudDatalabelingV1beta1ExportDataRequestOut": "_datalabeling_289_GoogleCloudDatalabelingV1beta1ExportDataRequestOut",
        "GoogleCloudDatalabelingV1alpha1OutputConfigIn": "_datalabeling_290_GoogleCloudDatalabelingV1alpha1OutputConfigIn",
        "GoogleCloudDatalabelingV1alpha1OutputConfigOut": "_datalabeling_291_GoogleCloudDatalabelingV1alpha1OutputConfigOut",
        "GoogleLongrunningListOperationsResponseIn": "_datalabeling_292_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_datalabeling_293_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataIn": "_datalabeling_294_GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataOut": "_datalabeling_295_GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1BigQuerySourceIn": "_datalabeling_296_GoogleCloudDatalabelingV1beta1BigQuerySourceIn",
        "GoogleCloudDatalabelingV1beta1BigQuerySourceOut": "_datalabeling_297_GoogleCloudDatalabelingV1beta1BigQuerySourceOut",
        "GoogleCloudDatalabelingV1beta1ExampleIn": "_datalabeling_298_GoogleCloudDatalabelingV1beta1ExampleIn",
        "GoogleCloudDatalabelingV1beta1ExampleOut": "_datalabeling_299_GoogleCloudDatalabelingV1beta1ExampleOut",
        "GoogleCloudDatalabelingV1beta1BoundingPolyIn": "_datalabeling_300_GoogleCloudDatalabelingV1beta1BoundingPolyIn",
        "GoogleCloudDatalabelingV1beta1BoundingPolyOut": "_datalabeling_301_GoogleCloudDatalabelingV1beta1BoundingPolyOut",
        "GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseIn": "_datalabeling_302_GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseIn",
        "GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseOut": "_datalabeling_303_GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseOut",
        "GoogleCloudDatalabelingV1alpha1ImportDataOperationResponseIn": "_datalabeling_304_GoogleCloudDatalabelingV1alpha1ImportDataOperationResponseIn",
        "GoogleCloudDatalabelingV1alpha1ImportDataOperationResponseOut": "_datalabeling_305_GoogleCloudDatalabelingV1alpha1ImportDataOperationResponseOut",
        "GoogleCloudDatalabelingV1beta1FeedbackThreadIn": "_datalabeling_306_GoogleCloudDatalabelingV1beta1FeedbackThreadIn",
        "GoogleCloudDatalabelingV1beta1FeedbackThreadOut": "_datalabeling_307_GoogleCloudDatalabelingV1beta1FeedbackThreadOut",
        "GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigIn": "_datalabeling_308_GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigIn",
        "GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigOut": "_datalabeling_309_GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigOut",
        "GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationIn": "_datalabeling_310_GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationIn",
        "GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationOut": "_datalabeling_311_GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationOut",
        "GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationIn": "_datalabeling_312_GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationIn",
        "GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationOut": "_datalabeling_313_GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationOut",
        "GoogleCloudDatalabelingV1alpha1ExportDataOperationResponseIn": "_datalabeling_314_GoogleCloudDatalabelingV1alpha1ExportDataOperationResponseIn",
        "GoogleCloudDatalabelingV1alpha1ExportDataOperationResponseOut": "_datalabeling_315_GoogleCloudDatalabelingV1alpha1ExportDataOperationResponseOut",
        "GoogleCloudDatalabelingV1beta1AnnotationSpecIn": "_datalabeling_316_GoogleCloudDatalabelingV1beta1AnnotationSpecIn",
        "GoogleCloudDatalabelingV1beta1AnnotationSpecOut": "_datalabeling_317_GoogleCloudDatalabelingV1beta1AnnotationSpecOut",
        "GoogleCloudDatalabelingV1beta1VertexIn": "_datalabeling_318_GoogleCloudDatalabelingV1beta1VertexIn",
        "GoogleCloudDatalabelingV1beta1VertexOut": "_datalabeling_319_GoogleCloudDatalabelingV1beta1VertexOut",
        "GoogleCloudDatalabelingV1beta1CsvInstructionIn": "_datalabeling_320_GoogleCloudDatalabelingV1beta1CsvInstructionIn",
        "GoogleCloudDatalabelingV1beta1CsvInstructionOut": "_datalabeling_321_GoogleCloudDatalabelingV1beta1CsvInstructionOut",
        "GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataIn": "_datalabeling_322_GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataOut": "_datalabeling_323_GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1SegmentationConfigIn": "_datalabeling_324_GoogleCloudDatalabelingV1beta1SegmentationConfigIn",
        "GoogleCloudDatalabelingV1beta1SegmentationConfigOut": "_datalabeling_325_GoogleCloudDatalabelingV1beta1SegmentationConfigOut",
        "GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyIn": "_datalabeling_326_GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyIn",
        "GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyOut": "_datalabeling_327_GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyOut",
        "GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationIn": "_datalabeling_328_GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationIn",
        "GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationOut": "_datalabeling_329_GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataIn": "_datalabeling_330_GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataOut": "_datalabeling_331_GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseIn": "_datalabeling_332_GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseIn",
        "GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseOut": "_datalabeling_333_GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseOut",
        "GoogleCloudDatalabelingV1beta1ListExamplesResponseIn": "_datalabeling_334_GoogleCloudDatalabelingV1beta1ListExamplesResponseIn",
        "GoogleCloudDatalabelingV1beta1ListExamplesResponseOut": "_datalabeling_335_GoogleCloudDatalabelingV1beta1ListExamplesResponseOut",
        "GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadataIn": "_datalabeling_336_GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadataOut": "_datalabeling_337_GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataIn": "_datalabeling_338_GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataIn",
        "GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataOut": "_datalabeling_339_GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataOut",
        "GoogleCloudDatalabelingV1beta1GcsDestinationIn": "_datalabeling_340_GoogleCloudDatalabelingV1beta1GcsDestinationIn",
        "GoogleCloudDatalabelingV1beta1GcsDestinationOut": "_datalabeling_341_GoogleCloudDatalabelingV1beta1GcsDestinationOut",
        "GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponseIn": "_datalabeling_342_GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponseIn",
        "GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponseOut": "_datalabeling_343_GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponseOut",
        "GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadataIn": "_datalabeling_344_GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadataOut": "_datalabeling_345_GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataIn": "_datalabeling_346_GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataOut": "_datalabeling_347_GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataOut",
        "GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadataIn": "_datalabeling_348_GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadataIn",
        "GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadataOut": "_datalabeling_349_GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1AttemptIn": "_datalabeling_350_GoogleCloudDatalabelingV1beta1AttemptIn",
        "GoogleCloudDatalabelingV1beta1AttemptOut": "_datalabeling_351_GoogleCloudDatalabelingV1beta1AttemptOut",
        "GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn": "_datalabeling_352_GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn",
        "GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut": "_datalabeling_353_GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut",
        "GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationIn": "_datalabeling_354_GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationIn",
        "GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationOut": "_datalabeling_355_GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationOut",
        "GoogleCloudDatalabelingV1beta1ImportDataRequestIn": "_datalabeling_356_GoogleCloudDatalabelingV1beta1ImportDataRequestIn",
        "GoogleCloudDatalabelingV1beta1ImportDataRequestOut": "_datalabeling_357_GoogleCloudDatalabelingV1beta1ImportDataRequestOut",
        "GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigIn": "_datalabeling_358_GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigIn",
        "GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigOut": "_datalabeling_359_GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigOut",
        "GoogleCloudDatalabelingV1beta1BoundingPolyConfigIn": "_datalabeling_360_GoogleCloudDatalabelingV1beta1BoundingPolyConfigIn",
        "GoogleCloudDatalabelingV1beta1BoundingPolyConfigOut": "_datalabeling_361_GoogleCloudDatalabelingV1beta1BoundingPolyConfigOut",
        "GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequestIn": "_datalabeling_362_GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequestIn",
        "GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequestOut": "_datalabeling_363_GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequestOut",
        "GoogleCloudDatalabelingV1beta1AnnotatedDatasetIn": "_datalabeling_364_GoogleCloudDatalabelingV1beta1AnnotatedDatasetIn",
        "GoogleCloudDatalabelingV1beta1AnnotatedDatasetOut": "_datalabeling_365_GoogleCloudDatalabelingV1beta1AnnotatedDatasetOut",
        "GoogleCloudDatalabelingV1beta1ExportDataOperationMetadataIn": "_datalabeling_366_GoogleCloudDatalabelingV1beta1ExportDataOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1ExportDataOperationMetadataOut": "_datalabeling_367_GoogleCloudDatalabelingV1beta1ExportDataOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseIn": "_datalabeling_368_GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseIn",
        "GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseOut": "_datalabeling_369_GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseOut",
        "GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataIn": "_datalabeling_370_GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataOut": "_datalabeling_371_GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1OutputConfigIn": "_datalabeling_372_GoogleCloudDatalabelingV1beta1OutputConfigIn",
        "GoogleCloudDatalabelingV1beta1OutputConfigOut": "_datalabeling_373_GoogleCloudDatalabelingV1beta1OutputConfigOut",
        "GoogleCloudDatalabelingV1beta1DataItemIn": "_datalabeling_374_GoogleCloudDatalabelingV1beta1DataItemIn",
        "GoogleCloudDatalabelingV1beta1DataItemOut": "_datalabeling_375_GoogleCloudDatalabelingV1beta1DataItemOut",
        "GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataIn": "_datalabeling_376_GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataOut": "_datalabeling_377_GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataOut",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataIn": "_datalabeling_378_GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataOut": "_datalabeling_379_GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1ClassificationMetricsIn": "_datalabeling_380_GoogleCloudDatalabelingV1beta1ClassificationMetricsIn",
        "GoogleCloudDatalabelingV1beta1ClassificationMetricsOut": "_datalabeling_381_GoogleCloudDatalabelingV1beta1ClassificationMetricsOut",
        "GoogleCloudDatalabelingV1beta1LabelOperationMetadataIn": "_datalabeling_382_GoogleCloudDatalabelingV1beta1LabelOperationMetadataIn",
        "GoogleCloudDatalabelingV1beta1LabelOperationMetadataOut": "_datalabeling_383_GoogleCloudDatalabelingV1beta1LabelOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequestIn": "_datalabeling_384_GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequestIn",
        "GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequestOut": "_datalabeling_385_GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequestOut",
        "GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadataIn": "_datalabeling_386_GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadataIn",
        "GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadataOut": "_datalabeling_387_GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadataOut",
        "GoogleCloudDatalabelingV1beta1InstructionIn": "_datalabeling_388_GoogleCloudDatalabelingV1beta1InstructionIn",
        "GoogleCloudDatalabelingV1beta1InstructionOut": "_datalabeling_389_GoogleCloudDatalabelingV1beta1InstructionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1ObjectTrackingFrameIn"] = t.struct(
        {
            "normalizedBoundingPoly": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyIn"]
            ),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyIn"]
            ),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ObjectTrackingFrameIn"])
    types["GoogleCloudDatalabelingV1beta1ObjectTrackingFrameOut"] = t.struct(
        {
            "normalizedBoundingPoly": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyOut"]
            ),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyOut"]
            ),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ObjectTrackingFrameOut"])
    types["GoogleCloudDatalabelingV1alpha1GcsDestinationIn"] = t.struct(
        {"outputUri": t.string(), "mimeType": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1alpha1GcsDestinationIn"])
    types["GoogleCloudDatalabelingV1alpha1GcsDestinationOut"] = t.struct(
        {
            "outputUri": t.string(),
            "mimeType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1GcsDestinationOut"])
    types["GoogleCloudDatalabelingV1beta1VideoThumbnailIn"] = t.struct(
        {"timeOffset": t.string().optional(), "thumbnail": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoThumbnailIn"])
    types["GoogleCloudDatalabelingV1beta1VideoThumbnailOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "thumbnail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoThumbnailOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1p2alpha1GcsDestinationIn"] = t.struct(
        {"mimeType": t.string(), "outputUri": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1GcsDestinationIn"])
    types["GoogleCloudDatalabelingV1p2alpha1GcsDestinationOut"] = t.struct(
        {
            "mimeType": t.string(),
            "outputUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1GcsDestinationOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1TextPayloadIn"] = t.struct(
        {"textContent": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1TextPayloadIn"])
    types["GoogleCloudDatalabelingV1beta1TextPayloadOut"] = t.struct(
        {
            "textContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextPayloadOut"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1SequentialSegmentIn"] = t.struct(
        {"end": t.integer().optional(), "start": t.integer().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1SequentialSegmentIn"])
    types["GoogleCloudDatalabelingV1beta1SequentialSegmentOut"] = t.struct(
        {
            "end": t.integer().optional(),
            "start": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1SequentialSegmentOut"])
    types["GoogleCloudDatalabelingV1beta1PdfInstructionIn"] = t.struct(
        {"gcsFileUri": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1PdfInstructionIn"])
    types["GoogleCloudDatalabelingV1beta1PdfInstructionOut"] = t.struct(
        {
            "gcsFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1PdfInstructionOut"])
    types["GoogleCloudDatalabelingV1beta1LabelImageRequestIn"] = t.struct(
        {
            "imageClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigIn"]
            ).optional(),
            "segmentationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1SegmentationConfigIn"]
            ).optional(),
            "boundingPolyConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigIn"]
            ).optional(),
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ),
            "feature": t.string(),
            "polylineConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PolylineConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelImageRequestIn"])
    types["GoogleCloudDatalabelingV1beta1LabelImageRequestOut"] = t.struct(
        {
            "imageClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigOut"]
            ).optional(),
            "segmentationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1SegmentationConfigOut"]
            ).optional(),
            "boundingPolyConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigOut"]
            ).optional(),
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ),
            "feature": t.string(),
            "polylineConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PolylineConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelImageRequestOut"])
    types["GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryIn"] = t.struct(
        {
            "itemCount": t.integer().optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryIn"])
    types["GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryOut"] = t.struct(
        {
            "itemCount": t.integer().optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1alpha1LabelStatsIn"] = t.struct(
        {"exampleCount": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDatalabelingV1alpha1LabelStatsIn"])
    types["GoogleCloudDatalabelingV1alpha1LabelStatsOut"] = t.struct(
        {
            "exampleCount": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1LabelStatsOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1TextMetadataIn"] = t.struct(
        {"languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1TextMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1TextMetadataOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequestIn"] = t.struct(
        {"job": t.proxy(renames["GoogleCloudDatalabelingV1beta1EvaluationJobIn"])}
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequestIn"])
    types["GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequestOut"] = t.struct(
        {
            "job": t.proxy(renames["GoogleCloudDatalabelingV1beta1EvaluationJobOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequestOut"])
    types["GoogleCloudDatalabelingV1alpha1CreateInstructionMetadataIn"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "createTime": t.string().optional(),
            "instruction": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1CreateInstructionMetadataIn"])
    types["GoogleCloudDatalabelingV1alpha1CreateInstructionMetadataOut"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "instruction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1CreateInstructionMetadataOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataIn"]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataOut"]
    )
    types["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"] = t.struct(
        {
            "annotatedDatasetDescription": t.string().optional(),
            "replicaCount": t.integer().optional(),
            "languageCode": t.string().optional(),
            "annotatedDatasetDisplayName": t.string(),
            "questionDuration": t.string().optional(),
            "userEmailAddress": t.string().optional(),
            "contributorEmails": t.array(t.string()).optional(),
            "instruction": t.string(),
            "labelGroup": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"])
    types["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"] = t.struct(
        {
            "annotatedDatasetDescription": t.string().optional(),
            "replicaCount": t.integer().optional(),
            "languageCode": t.string().optional(),
            "annotatedDatasetDisplayName": t.string(),
            "questionDuration": t.string().optional(),
            "userEmailAddress": t.string().optional(),
            "contributorEmails": t.array(t.string()).optional(),
            "instruction": t.string(),
            "labelGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataIn"]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataOut"]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadataIn"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadataOut"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponseIn"] = t.struct(
        {
            "dataset": t.string().optional(),
            "totalCount": t.integer().optional(),
            "annotatedDataset": t.string().optional(),
            "exportCount": t.integer().optional(),
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1LabelStatsIn"]
            ).optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1OutputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponseIn"])
    types["GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponseOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "totalCount": t.integer().optional(),
            "annotatedDataset": t.string().optional(),
            "exportCount": t.integer().optional(),
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1LabelStatsOut"]
            ).optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1OutputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponseOut"])
    types["GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "status": t.string(),
            "thumbnail": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "status": t.string(),
            "thumbnail": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1CreateInstructionRequestIn"] = t.struct(
        {"instruction": t.proxy(renames["GoogleCloudDatalabelingV1beta1InstructionIn"])}
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateInstructionRequestIn"])
    types["GoogleCloudDatalabelingV1beta1CreateInstructionRequestOut"] = t.struct(
        {
            "instruction": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1InstructionOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateInstructionRequestOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1p1alpha1LabelStatsIn"] = t.struct(
        {"exampleCount": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1LabelStatsIn"])
    types["GoogleCloudDatalabelingV1p1alpha1LabelStatsOut"] = t.struct(
        {
            "exampleCount": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1LabelStatsOut"])
    types["GoogleCloudDatalabelingV1beta1ImageClassificationConfigIn"] = t.struct(
        {
            "annotationSpecSet": t.string(),
            "allowMultiLabel": t.boolean().optional(),
            "answerAggregationType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigIn"])
    types["GoogleCloudDatalabelingV1beta1ImageClassificationConfigOut"] = t.struct(
        {
            "annotationSpecSet": t.string(),
            "allowMultiLabel": t.boolean().optional(),
            "answerAggregationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigOut"])
    types["GoogleCloudDatalabelingV1beta1PolylineIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1VertexIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1PolylineIn"])
    types["GoogleCloudDatalabelingV1beta1PolylineOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1VertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1PolylineOut"])
    types["GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadataIn"] = t.struct(
        {
            "dataset": t.string().optional(),
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "annotatedDataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadataOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1TimeSegmentIn"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TimeSegmentIn"])
    types["GoogleCloudDatalabelingV1beta1TimeSegmentOut"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TimeSegmentOut"])
    types["GoogleCloudDatalabelingV1beta1ListDatasetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "datasets": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListDatasetsResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListDatasetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "datasets": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListDatasetsResponseOut"])
    types["GoogleCloudDatalabelingV1beta1EvaluationJobConfigIn"] = t.struct(
        {
            "evaluationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationConfigIn"]
            ),
            "bigqueryImportKeys": t.struct({"_": t.string().optional()}),
            "boundingPolyConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigIn"]
            ).optional(),
            "textClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigIn"]
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1InputConfigIn"]
            ).optional(),
            "exampleCount": t.integer(),
            "exampleSamplePercentage": t.number(),
            "imageClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigIn"]
            ).optional(),
            "evaluationJobAlertConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigIn"]
            ).optional(),
            "humanAnnotationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationJobConfigIn"])
    types["GoogleCloudDatalabelingV1beta1EvaluationJobConfigOut"] = t.struct(
        {
            "evaluationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationConfigOut"]
            ),
            "bigqueryImportKeys": t.struct({"_": t.string().optional()}),
            "boundingPolyConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigOut"]
            ).optional(),
            "textClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigOut"]
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1InputConfigOut"]
            ).optional(),
            "exampleCount": t.integer(),
            "exampleSamplePercentage": t.number(),
            "imageClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigOut"]
            ).optional(),
            "evaluationJobAlertConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigOut"]
            ).optional(),
            "humanAnnotationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationJobConfigOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1PolylineConfigIn"] = t.struct(
        {"instructionMessage": t.string().optional(), "annotationSpecSet": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1PolylineConfigIn"])
    types["GoogleCloudDatalabelingV1beta1PolylineConfigOut"] = t.struct(
        {
            "instructionMessage": t.string().optional(),
            "annotationSpecSet": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1PolylineConfigOut"])
    types["GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryIn"] = t.struct(
        {
            "f1ScoreAt1": t.number().optional(),
            "f1Score": t.number().optional(),
            "precisionAt5": t.number().optional(),
            "precisionAt1": t.number().optional(),
            "recallAt5": t.number().optional(),
            "confidenceThreshold": t.number().optional(),
            "precision": t.number().optional(),
            "recallAt1": t.number().optional(),
            "recall": t.number().optional(),
            "f1ScoreAt5": t.number().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryIn"])
    types["GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryOut"] = t.struct(
        {
            "f1ScoreAt1": t.number().optional(),
            "f1Score": t.number().optional(),
            "precisionAt5": t.number().optional(),
            "precisionAt1": t.number().optional(),
            "recallAt5": t.number().optional(),
            "confidenceThreshold": t.number().optional(),
            "precision": t.number().optional(),
            "recallAt1": t.number().optional(),
            "recall": t.number().optional(),
            "f1ScoreAt5": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryOut"])
    types["GoogleCloudDatalabelingV1beta1ExportDataOperationResponseIn"] = t.struct(
        {
            "dataset": t.string().optional(),
            "totalCount": t.integer().optional(),
            "annotatedDataset": t.string().optional(),
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1LabelStatsIn"]
            ).optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1OutputConfigIn"]
            ).optional(),
            "exportCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExportDataOperationResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ExportDataOperationResponseOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "totalCount": t.integer().optional(),
            "annotatedDataset": t.string().optional(),
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1LabelStatsOut"]
            ).optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1OutputConfigOut"]
            ).optional(),
            "exportCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExportDataOperationResponseOut"])
    types["GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationIn"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationOut"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationOut"])
    types["GoogleCloudDatalabelingV1beta1TextClassificationConfigIn"] = t.struct(
        {
            "allowMultiLabel": t.boolean().optional(),
            "annotationSpecSet": t.string(),
            "sentimentConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1SentimentConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigIn"])
    types["GoogleCloudDatalabelingV1beta1TextClassificationConfigOut"] = t.struct(
        {
            "allowMultiLabel": t.boolean().optional(),
            "annotationSpecSet": t.string(),
            "sentimentConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1SentimentConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigOut"])
    types["GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadataIn"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "instruction": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadataIn"])
    types["GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadataOut"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "instruction": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1NormalizedPolylineIn"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1NormalizedVertexIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1NormalizedPolylineIn"])
    types["GoogleCloudDatalabelingV1beta1NormalizedPolylineOut"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1NormalizedPolylineOut"])
    types["GoogleCloudDatalabelingV1p1alpha1GcsDestinationIn"] = t.struct(
        {"outputUri": t.string(), "mimeType": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1GcsDestinationIn"])
    types["GoogleCloudDatalabelingV1p1alpha1GcsDestinationOut"] = t.struct(
        {
            "outputUri": t.string(),
            "mimeType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1GcsDestinationOut"])
    types["GoogleCloudDatalabelingV1p1alpha1OutputConfigIn"] = t.struct(
        {
            "gcsFolderDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationIn"]
            ).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1OutputConfigIn"])
    types["GoogleCloudDatalabelingV1p1alpha1OutputConfigOut"] = t.struct(
        {
            "gcsFolderDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationOut"]
            ).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1OutputConfigOut"])
    types["GoogleCloudDatalabelingV1beta1ClassificationMetadataIn"] = t.struct(
        {"isMultiLabel": t.boolean().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1ClassificationMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1ClassificationMetadataOut"] = t.struct(
        {
            "isMultiLabel": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ClassificationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1LabelStatsIn"] = t.struct(
        {"exampleCount": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelStatsIn"])
    types["GoogleCloudDatalabelingV1beta1LabelStatsOut"] = t.struct(
        {
            "exampleCount": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelStatsOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1RowIn"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
            "entries": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1RowIn"])
    types["GoogleCloudDatalabelingV1beta1RowOut"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "entries": t.array(
                t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1ConfusionMatrixEntryOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1RowOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadataIn"] = t.struct(
        {
            "dataset": t.string().optional(),
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadataOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1LabelVideoRequestIn"] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ),
            "eventConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EventConfigIn"]
            ).optional(),
            "feature": t.string(),
            "videoClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoClassificationConfigIn"]
            ).optional(),
            "objectTrackingConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigIn"]
            ).optional(),
            "objectDetectionConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelVideoRequestIn"])
    types["GoogleCloudDatalabelingV1beta1LabelVideoRequestOut"] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ),
            "eventConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EventConfigOut"]
            ).optional(),
            "feature": t.string(),
            "videoClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoClassificationConfigOut"]
            ).optional(),
            "objectTrackingConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigOut"]
            ).optional(),
            "objectDetectionConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelVideoRequestOut"])
    types["GoogleCloudDatalabelingV1beta1ImportDataOperationResponseIn"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "importCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImportDataOperationResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ImportDataOperationResponseOut"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "importCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImportDataOperationResponseOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1EvaluationMetricsIn"] = t.struct(
        {
            "objectDetectionMetrics": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsIn"]
            ),
            "classificationMetrics": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ClassificationMetricsIn"]
            ),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationMetricsIn"])
    types["GoogleCloudDatalabelingV1beta1EvaluationMetricsOut"] = t.struct(
        {
            "objectDetectionMetrics": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsOut"]
            ),
            "classificationMetrics": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ClassificationMetricsOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationMetricsOut"])
    types["GoogleCloudDatalabelingV1beta1AnnotationMetadataIn"] = t.struct(
        {
            "operatorMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1OperatorMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1AnnotationMetadataOut"] = t.struct(
        {
            "operatorMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1OperatorMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationMetadataOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1ImportDataOperationMetadataIn"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImportDataOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1ImportDataOperationMetadataOut"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImportDataOperationMetadataOut"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1VideoClassificationConfigIn"] = t.struct(
        {
            "applyShotDetection": t.boolean().optional(),
            "annotationSpecSetConfigs": t.array(
                t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigIn"]
                )
            ),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoClassificationConfigIn"])
    types["GoogleCloudDatalabelingV1beta1VideoClassificationConfigOut"] = t.struct(
        {
            "applyShotDetection": t.boolean().optional(),
            "annotationSpecSetConfigs": t.array(
                t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoClassificationConfigOut"])
    types["GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "feedbackMessages": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1FeedbackMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "feedbackMessages": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1FeedbackMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationIn"] = t.struct(
        {
            "timeSegment": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TimeSegmentIn"]
            ).optional(),
            "objectTrackingFrames": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ObjectTrackingFrameIn"])
            ).optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationOut"] = t.struct(
        {
            "timeSegment": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TimeSegmentOut"]
            ).optional(),
            "objectTrackingFrames": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ObjectTrackingFrameOut"])
            ).optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationOut"])
    types["GoogleCloudDatalabelingV1beta1EvaluationConfigIn"] = t.struct(
        {
            "boundingBoxEvaluationOptions": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationConfigIn"])
    types["GoogleCloudDatalabelingV1beta1EvaluationConfigOut"] = t.struct(
        {
            "boundingBoxEvaluationOptions": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationConfigOut"])
    types["GoogleCloudDatalabelingV1beta1LabelTextRequestIn"] = t.struct(
        {
            "textClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigIn"]
            ).optional(),
            "feature": t.string(),
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ),
            "textEntityExtractionConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelTextRequestIn"])
    types["GoogleCloudDatalabelingV1beta1LabelTextRequestOut"] = t.struct(
        {
            "textClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigOut"]
            ).optional(),
            "feature": t.string(),
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ),
            "textEntityExtractionConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelTextRequestOut"])
    types["GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "evaluationJobs": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1EvaluationJobIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "evaluationJobs": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1EvaluationJobOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseOut"])
    types["GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponseIn"] = t.struct(
        {
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1LabelStatsIn"]
            ).optional(),
            "exportCount": t.integer().optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1OutputConfigIn"]
            ).optional(),
            "totalCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "annotatedDataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponseIn"])
    types["GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponseOut"] = t.struct(
        {
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1LabelStatsOut"]
            ).optional(),
            "exportCount": t.integer().optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1OutputConfigOut"]
            ).optional(),
            "totalCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "annotatedDataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponseOut"])
    types["GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadataIn"] = t.struct(
        {
            "imageSegmentationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataIn"
                ]
            ).optional(),
            "imageBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataIn"
                ]
            ).optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "progressPercent": t.integer().optional(),
            "videoClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataIn"
                ]
            ).optional(),
            "textClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataIn"
                ]
            ).optional(),
            "videoEventDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataIn"
                ]
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "imageClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataIn"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "videoObjectDetectionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataIn"
                ]
            ).optional(),
            "imagePolylineDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataIn"
                ]
            ).optional(),
            "imageBoundingPolyDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataIn"
                ]
            ).optional(),
            "imageOrientedBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
                ]
            ).optional(),
            "textEntityExtractionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataIn"
                ]
            ).optional(),
            "videoObjectTrackingDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataIn"
                ]
            ).optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadataOut"] = t.struct(
        {
            "imageSegmentationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataOut"
                ]
            ).optional(),
            "imageBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadataOut"
                ]
            ).optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "progressPercent": t.integer().optional(),
            "videoClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataOut"
                ]
            ).optional(),
            "textClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadataOut"
                ]
            ).optional(),
            "videoEventDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataOut"
                ]
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "imageClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadataOut"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "videoObjectDetectionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadataOut"
                ]
            ).optional(),
            "imagePolylineDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataOut"
                ]
            ).optional(),
            "imageBoundingPolyDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadataOut"
                ]
            ).optional(),
            "imageOrientedBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
                ]
            ).optional(),
            "textEntityExtractionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataOut"
                ]
            ).optional(),
            "videoObjectTrackingDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataOut"
                ]
            ).optional(),
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1EvaluationJobIn"] = t.struct(
        {
            "modelVersion": t.string(),
            "schedule": t.string(),
            "createTime": t.string().optional(),
            "labelMissingGroundTruth": t.boolean(),
            "name": t.string().optional(),
            "annotationSpecSet": t.string(),
            "description": t.string(),
            "evaluationJobConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationJobConfigIn"]
            ),
            "attempts": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AttemptIn"])
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationJobIn"])
    types["GoogleCloudDatalabelingV1beta1EvaluationJobOut"] = t.struct(
        {
            "modelVersion": t.string(),
            "schedule": t.string(),
            "createTime": t.string().optional(),
            "labelMissingGroundTruth": t.boolean(),
            "name": t.string().optional(),
            "annotationSpecSet": t.string(),
            "description": t.string(),
            "evaluationJobConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationJobConfigOut"]
            ),
            "attempts": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AttemptOut"])
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationJobOut"])
    types["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"] = t.struct(
        {
            "annotatedDatasetDescription": t.string().optional(),
            "contributorEmails": t.array(t.string()).optional(),
            "replicaCount": t.integer().optional(),
            "annotatedDatasetDisplayName": t.string(),
            "questionDuration": t.string().optional(),
            "languageCode": t.string().optional(),
            "userEmailAddress": t.string().optional(),
            "labelGroup": t.string().optional(),
            "instruction": t.string(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"])
    types["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"] = t.struct(
        {
            "annotatedDatasetDescription": t.string().optional(),
            "contributorEmails": t.array(t.string()).optional(),
            "replicaCount": t.integer().optional(),
            "annotatedDatasetDisplayName": t.string(),
            "questionDuration": t.string().optional(),
            "languageCode": t.string().optional(),
            "userEmailAddress": t.string().optional(),
            "labelGroup": t.string().optional(),
            "instruction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponseIn"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "importCount": t.integer().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponseIn"])
    types["GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponseOut"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "importCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponseOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1AnnotationIn"] = t.struct(
        {
            "annotationValue": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationValueIn"]
            ).optional(),
            "annotationSentiment": t.string().optional(),
            "annotationMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationMetadataIn"]
            ).optional(),
            "name": t.string().optional(),
            "annotationSource": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1AnnotationOut"] = t.struct(
        {
            "annotationValue": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationValueOut"]
            ).optional(),
            "annotationSentiment": t.string().optional(),
            "annotationMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationMetadataOut"]
            ).optional(),
            "name": t.string().optional(),
            "annotationSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationOut"])
    types["GoogleCloudDatalabelingV1beta1VideoEventAnnotationIn"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
            "timeSegment": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TimeSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoEventAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1VideoEventAnnotationOut"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "timeSegment": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TimeSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoEventAnnotationOut"])
    types["GoogleCloudDatalabelingV1alpha1LabelOperationMetadataIn"] = t.struct(
        {
            "videoClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataIn"
                ]
            ).optional(),
            "videoEventDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataIn"
                ]
            ).optional(),
            "imagePolylineDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataIn"
                ]
            ).optional(),
            "textClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataIn"
                ]
            ).optional(),
            "textEntityExtractionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataIn"
                ]
            ).optional(),
            "imageBoundingPolyDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataIn"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "imageClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataIn"
                ]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "imageSegmentationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataIn"
                ]
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "videoObjectDetectionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataIn"
                ]
            ).optional(),
            "imageOrientedBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
                ]
            ).optional(),
            "imageBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataIn"
                ]
            ).optional(),
            "dataset": t.string().optional(),
            "videoObjectTrackingDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1LabelOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1alpha1LabelOperationMetadataOut"] = t.struct(
        {
            "videoClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadataOut"
                ]
            ).optional(),
            "videoEventDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataOut"
                ]
            ).optional(),
            "imagePolylineDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadataOut"
                ]
            ).optional(),
            "textClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataOut"
                ]
            ).optional(),
            "textEntityExtractionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadataOut"
                ]
            ).optional(),
            "imageBoundingPolyDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadataOut"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "imageClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadataOut"
                ]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "imageSegmentationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataOut"
                ]
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "videoObjectDetectionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataOut"
                ]
            ).optional(),
            "imageOrientedBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
                ]
            ).optional(),
            "imageBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadataOut"
                ]
            ).optional(),
            "dataset": t.string().optional(),
            "videoObjectTrackingDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1LabelOperationMetadataOut"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1InputConfigIn"] = t.struct(
        {
            "classificationMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ClassificationMetadataIn"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1GcsSourceIn"]
            ).optional(),
            "dataType": t.string(),
            "textMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextMetadataIn"]
            ),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BigQuerySourceIn"]
            ).optional(),
            "annotationType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1InputConfigIn"])
    types["GoogleCloudDatalabelingV1beta1InputConfigOut"] = t.struct(
        {
            "classificationMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ClassificationMetadataOut"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1GcsSourceOut"]
            ).optional(),
            "dataType": t.string(),
            "textMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextMetadataOut"]
            ),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BigQuerySourceOut"]
            ).optional(),
            "annotationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1InputConfigOut"])
    types["GoogleCloudDatalabelingV1beta1GcsSourceIn"] = t.struct(
        {"inputUri": t.string(), "mimeType": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1GcsSourceIn"])
    types["GoogleCloudDatalabelingV1beta1GcsSourceOut"] = t.struct(
        {
            "inputUri": t.string(),
            "mimeType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1GcsSourceOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "annotatedDatasets": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "annotatedDatasets": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseOut"])
    types["GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsIn"] = t.struct(
        {"iouThreshold": t.number().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsIn"])
    types["GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsOut"] = t.struct(
        {
            "iouThreshold": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptionsOut"])
    types["GoogleCloudDatalabelingV1beta1AnnotationValueIn"] = t.struct(
        {
            "textClassificationAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextClassificationAnnotationIn"]
            ).optional(),
            "imageBoundingPolyAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationIn"]
            ).optional(),
            "videoEventAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoEventAnnotationIn"]
            ).optional(),
            "imageSegmentationAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationIn"]
            ).optional(),
            "videoObjectTrackingAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationIn"]
            ).optional(),
            "textEntityExtractionAnnotation": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationIn"
                ]
            ).optional(),
            "imageClassificationAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationIn"]
            ).optional(),
            "videoClassificationAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationIn"]
            ).optional(),
            "imagePolylineAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationValueIn"])
    types["GoogleCloudDatalabelingV1beta1AnnotationValueOut"] = t.struct(
        {
            "textClassificationAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextClassificationAnnotationOut"]
            ).optional(),
            "imageBoundingPolyAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationOut"]
            ).optional(),
            "videoEventAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoEventAnnotationOut"]
            ).optional(),
            "imageSegmentationAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationOut"]
            ).optional(),
            "videoObjectTrackingAnnotation": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotationOut"
                ]
            ).optional(),
            "textEntityExtractionAnnotation": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationOut"
                ]
            ).optional(),
            "imageClassificationAnnotation": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1ImageClassificationAnnotationOut"
                ]
            ).optional(),
            "videoClassificationAnnotation": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationOut"
                ]
            ).optional(),
            "imagePolylineAnnotation": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationValueOut"])
    types["GoogleCloudDatalabelingV1beta1VideoPayloadIn"] = t.struct(
        {
            "signedUri": t.string().optional(),
            "frameRate": t.number().optional(),
            "videoThumbnails": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1VideoThumbnailIn"])
            ).optional(),
            "mimeType": t.string().optional(),
            "videoUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoPayloadIn"])
    types["GoogleCloudDatalabelingV1beta1VideoPayloadOut"] = t.struct(
        {
            "signedUri": t.string().optional(),
            "frameRate": t.number().optional(),
            "videoThumbnails": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1VideoThumbnailOut"])
            ).optional(),
            "mimeType": t.string().optional(),
            "videoUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoPayloadOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationIn"] = t.struct(
        {
            "timeSegment": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TimeSegmentIn"]
            ).optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationOut"] = t.struct(
        {
            "timeSegment": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TimeSegmentOut"]
            ).optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VideoClassificationAnnotationOut"])
    types["GoogleCloudDatalabelingV1beta1NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1NormalizedVertexIn"])
    types["GoogleCloudDatalabelingV1beta1NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1NormalizedVertexOut"])
    types["GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationIn"] = t.struct(
        {"outputFolderUri": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationIn"])
    types["GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationOut"] = t.struct(
        {
            "outputFolderUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1GcsFolderDestinationOut"])
    types["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataOut"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1DatasetIn"] = t.struct(
        {
            "inputConfigs": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1InputConfigIn"])
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "lastMigrateTime": t.string().optional(),
            "dataItemCount": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "blockingResources": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1DatasetIn"])
    types["GoogleCloudDatalabelingV1beta1DatasetOut"] = t.struct(
        {
            "inputConfigs": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1InputConfigOut"])
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "lastMigrateTime": t.string().optional(),
            "dataItemCount": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "blockingResources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1DatasetOut"])
    types["GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationIn"] = t.struct(
        {"outputFolderUri": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationIn"])
    types["GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationOut"] = t.struct(
        {
            "outputFolderUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationOut"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadataIn"
    ] = t.struct(
        {"dataset": t.string().optional(), "createTime": t.string().optional()}
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadataOut"
    ] = t.struct(
        {
            "dataset": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1EvaluationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "config": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationConfigIn"]
            ).optional(),
            "evaluationMetrics": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationMetricsIn"]
            ).optional(),
            "annotationType": t.string().optional(),
            "createTime": t.string().optional(),
            "evaluatedItemCount": t.string().optional(),
            "evaluationJobRunTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationIn"])
    types["GoogleCloudDatalabelingV1beta1EvaluationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "config": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationConfigOut"]
            ).optional(),
            "evaluationMetrics": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EvaluationMetricsOut"]
            ).optional(),
            "annotationType": t.string().optional(),
            "createTime": t.string().optional(),
            "evaluatedItemCount": t.string().optional(),
            "evaluationJobRunTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1TextClassificationAnnotationIn"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextClassificationAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1TextClassificationAnnotationOut"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextClassificationAnnotationOut"])
    types["GoogleCloudDatalabelingV1beta1SentimentConfigIn"] = t.struct(
        {"enableLabelSentimentSelection": t.boolean().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1SentimentConfigIn"])
    types["GoogleCloudDatalabelingV1beta1SentimentConfigOut"] = t.struct(
        {
            "enableLabelSentimentSelection": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1SentimentConfigOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataIn"]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadataOut"]
    )
    types["GoogleCloudDatalabelingV1beta1EventConfigIn"] = t.struct(
        {
            "clipLength": t.integer().optional(),
            "annotationSpecSets": t.array(t.string()),
            "overlapLength": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EventConfigIn"])
    types["GoogleCloudDatalabelingV1beta1EventConfigOut"] = t.struct(
        {
            "clipLength": t.integer().optional(),
            "annotationSpecSets": t.array(t.string()),
            "overlapLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EventConfigOut"])
    types["GoogleCloudDatalabelingV1beta1ListInstructionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1InstructionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListInstructionsResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListInstructionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1InstructionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListInstructionsResponseOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataIn"]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataOut"]
    )
    types["GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequestIn"] = t.struct(
        {"pageSize": t.integer().optional(), "pageToken": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequestIn"])
    types[
        "GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequestOut"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequestOut"]
    )
    types["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigIn"] = t.struct(
        {"annotationSpecSet": t.string(), "extractionFrameRate": t.number()}
    ).named(renames["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigIn"])
    types["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigOut"] = t.struct(
        {
            "annotationSpecSet": t.string(),
            "extractionFrameRate": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigOut"])
    types["GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigIn"] = t.struct(
        {"annotationSpecSet": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigIn"])
    types["GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigOut"] = t.struct(
        {
            "annotationSpecSet": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1ListDataItemsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataItems": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1DataItemIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListDataItemsResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListDataItemsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataItems": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1DataItemOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListDataItemsResponseOut"])
    types["GoogleCloudDatalabelingV1beta1OperatorMetadataIn"] = t.struct(
        {
            "score": t.number().optional(),
            "comments": t.array(t.string()).optional(),
            "labelVotes": t.integer().optional(),
            "totalVotes": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1OperatorMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1OperatorMetadataOut"] = t.struct(
        {
            "score": t.number().optional(),
            "comments": t.array(t.string()).optional(),
            "labelVotes": t.integer().optional(),
            "totalVotes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1OperatorMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1PrCurveIn"] = t.struct(
        {
            "areaUnderCurve": t.number().optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
            "confidenceMetricsEntries": t.array(
                t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryIn"]
                )
            ).optional(),
            "meanAveragePrecision": t.number().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1PrCurveIn"])
    types["GoogleCloudDatalabelingV1beta1PrCurveOut"] = t.struct(
        {
            "areaUnderCurve": t.number().optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "confidenceMetricsEntries": t.array(
                t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntryOut"]
                )
            ).optional(),
            "meanAveragePrecision": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1PrCurveOut"])
    types["GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequestIn"])
    types["GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequestOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1p2alpha1LabelStatsIn"] = t.struct(
        {"exampleCount": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1LabelStatsIn"])
    types["GoogleCloudDatalabelingV1p2alpha1LabelStatsOut"] = t.struct(
        {
            "exampleCount": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1LabelStatsOut"])
    types["GoogleCloudDatalabelingV1beta1AnnotationSpecSetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "blockingResources": t.array(t.string()).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "annotationSpecs": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"])
            ),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetIn"])
    types["GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "blockingResources": t.array(t.string()).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "annotationSpecs": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut"])
    types["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigIn"] = t.struct(
        {
            "overlapLength": t.integer().optional(),
            "annotationSpecSet": t.string(),
            "clipLength": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigIn"])
    types["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigOut"] = t.struct(
        {
            "overlapLength": t.integer().optional(),
            "annotationSpecSet": t.string(),
            "clipLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigOut"])
    types["GoogleCloudDatalabelingV1p2alpha1OutputConfigIn"] = t.struct(
        {
            "gcsFolderDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationIn"]
            ).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1OutputConfigIn"])
    types["GoogleCloudDatalabelingV1p2alpha1OutputConfigOut"] = t.struct(
        {
            "gcsFolderDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1GcsFolderDestinationOut"]
            ).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1OutputConfigOut"])
    types["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"] = t.struct(
        {
            "questionDuration": t.string().optional(),
            "userEmailAddress": t.string().optional(),
            "annotatedDatasetDisplayName": t.string(),
            "instruction": t.string(),
            "labelGroup": t.string().optional(),
            "contributorEmails": t.array(t.string()).optional(),
            "replicaCount": t.integer().optional(),
            "annotatedDatasetDescription": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"])
    types["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"] = t.struct(
        {
            "questionDuration": t.string().optional(),
            "userEmailAddress": t.string().optional(),
            "annotatedDatasetDisplayName": t.string(),
            "instruction": t.string(),
            "labelGroup": t.string().optional(),
            "contributorEmails": t.array(t.string()).optional(),
            "replicaCount": t.integer().optional(),
            "annotatedDatasetDescription": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"])
    types[
        "GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataIn"]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadataOut"]
    )
    types["GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsIn"] = t.struct(
        {
            "prCurve": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PrCurveIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsIn"])
    types["GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsOut"] = t.struct(
        {
            "prCurve": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PrCurveOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ObjectDetectionMetricsOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1GcsFolderDestinationIn"] = t.struct(
        {"outputFolderUri": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1GcsFolderDestinationIn"])
    types["GoogleCloudDatalabelingV1beta1GcsFolderDestinationOut"] = t.struct(
        {
            "outputFolderUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1GcsFolderDestinationOut"])
    types["GoogleCloudDatalabelingV1alpha1GcsFolderDestinationIn"] = t.struct(
        {"outputFolderUri": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1alpha1GcsFolderDestinationIn"])
    types["GoogleCloudDatalabelingV1alpha1GcsFolderDestinationOut"] = t.struct(
        {
            "outputFolderUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1GcsFolderDestinationOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1ConfusionMatrixIn"] = t.struct(
        {"row": t.array(t.proxy(renames["GoogleCloudDatalabelingV1beta1RowIn"]))}
    ).named(renames["GoogleCloudDatalabelingV1beta1ConfusionMatrixIn"])
    types["GoogleCloudDatalabelingV1beta1ConfusionMatrixOut"] = t.struct(
        {
            "row": t.array(t.proxy(renames["GoogleCloudDatalabelingV1beta1RowOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ConfusionMatrixOut"])
    types["GoogleCloudDatalabelingV1beta1ImagePayloadIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "imageThumbnail": t.string().optional(),
            "imageUri": t.string().optional(),
            "signedUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImagePayloadIn"])
    types["GoogleCloudDatalabelingV1beta1ImagePayloadOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "imageThumbnail": t.string().optional(),
            "imageUri": t.string().optional(),
            "signedUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImagePayloadOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseIn"] = t.struct(
        {
            "evaluations": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1EvaluationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseIn"])
    types["GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseOut"] = t.struct(
        {
            "evaluations": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1EvaluationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadataIn"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "dataset": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadataOut"] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "dataset": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1CreateInstructionMetadataIn"] = t.struct(
        {
            "instruction": t.string().optional(),
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateInstructionMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1CreateInstructionMetadataOut"] = t.struct(
        {
            "instruction": t.string().optional(),
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateInstructionMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1ExampleComparisonIn"] = t.struct(
        {
            "modelCreatedExamples": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ExampleIn"])
            ).optional(),
            "groundTruthExample": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ExampleIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExampleComparisonIn"])
    types["GoogleCloudDatalabelingV1beta1ExampleComparisonOut"] = t.struct(
        {
            "modelCreatedExamples": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ExampleOut"])
            ).optional(),
            "groundTruthExample": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ExampleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExampleComparisonOut"])
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1FeedbackMessageIn"] = t.struct(
        {
            "body": t.string().optional(),
            "createTime": t.string().optional(),
            "requesterFeedbackMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn"]
            ),
            "operatorFeedbackMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn"]
            ),
            "name": t.string().optional(),
            "image": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1FeedbackMessageIn"])
    types["GoogleCloudDatalabelingV1beta1FeedbackMessageOut"] = t.struct(
        {
            "body": t.string().optional(),
            "createTime": t.string().optional(),
            "requesterFeedbackMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataOut"]
            ),
            "operatorFeedbackMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataOut"]
            ),
            "name": t.string().optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1FeedbackMessageOut"])
    types["GoogleCloudDatalabelingV1beta1CreateDatasetRequestIn"] = t.struct(
        {"dataset": t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetIn"])}
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateDatasetRequestIn"])
    types["GoogleCloudDatalabelingV1beta1CreateDatasetRequestOut"] = t.struct(
        {
            "dataset": t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateDatasetRequestOut"])
    types["GoogleCloudDatalabelingV1beta1ExportDataRequestIn"] = t.struct(
        {
            "userEmailAddress": t.string().optional(),
            "filter": t.string().optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1OutputConfigIn"]
            ),
            "annotatedDataset": t.string(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExportDataRequestIn"])
    types["GoogleCloudDatalabelingV1beta1ExportDataRequestOut"] = t.struct(
        {
            "userEmailAddress": t.string().optional(),
            "filter": t.string().optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1OutputConfigOut"]
            ),
            "annotatedDataset": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExportDataRequestOut"])
    types["GoogleCloudDatalabelingV1alpha1OutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1GcsDestinationIn"]
            ).optional(),
            "gcsFolderDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1GcsFolderDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1OutputConfigIn"])
    types["GoogleCloudDatalabelingV1alpha1OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1GcsDestinationOut"]
            ).optional(),
            "gcsFolderDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1GcsFolderDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1OutputConfigOut"])
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
        "GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1BigQuerySourceIn"] = t.struct(
        {"inputUri": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1BigQuerySourceIn"])
    types["GoogleCloudDatalabelingV1beta1BigQuerySourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1BigQuerySourceOut"])
    types["GoogleCloudDatalabelingV1beta1ExampleIn"] = t.struct(
        {
            "imagePayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImagePayloadIn"]
            ).optional(),
            "textPayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextPayloadIn"]
            ).optional(),
            "annotations": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationIn"])
            ).optional(),
            "name": t.string().optional(),
            "videoPayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoPayloadIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExampleIn"])
    types["GoogleCloudDatalabelingV1beta1ExampleOut"] = t.struct(
        {
            "imagePayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImagePayloadOut"]
            ).optional(),
            "textPayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextPayloadOut"]
            ).optional(),
            "annotations": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationOut"])
            ).optional(),
            "name": t.string().optional(),
            "videoPayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoPayloadOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExampleOut"])
    types["GoogleCloudDatalabelingV1beta1BoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1VertexIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1BoundingPolyIn"])
    types["GoogleCloudDatalabelingV1beta1BoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1VertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1BoundingPolyOut"])
    types[
        "GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseIn"
    ] = t.struct(
        {
            "exampleComparisons": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ExampleComparisonIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseIn"]
    )
    types[
        "GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseOut"
    ] = t.struct(
        {
            "exampleComparisons": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ExampleComparisonOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseOut"]
    )
    types["GoogleCloudDatalabelingV1alpha1ImportDataOperationResponseIn"] = t.struct(
        {
            "importCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "totalCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1ImportDataOperationResponseIn"])
    types["GoogleCloudDatalabelingV1alpha1ImportDataOperationResponseOut"] = t.struct(
        {
            "importCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "totalCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1ImportDataOperationResponseOut"])
    types["GoogleCloudDatalabelingV1beta1FeedbackThreadIn"] = t.struct(
        {
            "feedbackThreadMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1FeedbackThreadIn"])
    types["GoogleCloudDatalabelingV1beta1FeedbackThreadOut"] = t.struct(
        {
            "feedbackThreadMetadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1FeedbackThreadMetadataOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1FeedbackThreadOut"])
    types["GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigIn"] = t.struct(
        {"minAcceptableMeanAveragePrecision": t.number(), "email": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigIn"])
    types["GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigOut"] = t.struct(
        {
            "minAcceptableMeanAveragePrecision": t.number(),
            "email": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfigOut"])
    types["GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationIn"] = t.struct(
        {
            "normalizedBoundingPoly": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyIn"]
            ),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyIn"]
            ),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationOut"] = t.struct(
        {
            "normalizedBoundingPoly": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyOut"]
            ),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotationOut"])
    types["GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationIn"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
            "polyline": t.proxy(renames["GoogleCloudDatalabelingV1beta1PolylineIn"]),
            "normalizedPolyline": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1NormalizedPolylineIn"]
            ),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationOut"] = t.struct(
        {
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "polyline": t.proxy(renames["GoogleCloudDatalabelingV1beta1PolylineOut"]),
            "normalizedPolyline": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1NormalizedPolylineOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImagePolylineAnnotationOut"])
    types["GoogleCloudDatalabelingV1alpha1ExportDataOperationResponseIn"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "exportCount": t.integer().optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1OutputConfigIn"]
            ).optional(),
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1LabelStatsIn"]
            ).optional(),
            "dataset": t.string().optional(),
            "annotatedDataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1ExportDataOperationResponseIn"])
    types["GoogleCloudDatalabelingV1alpha1ExportDataOperationResponseOut"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "exportCount": t.integer().optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1OutputConfigOut"]
            ).optional(),
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1alpha1LabelStatsOut"]
            ).optional(),
            "dataset": t.string().optional(),
            "annotatedDataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1alpha1ExportDataOperationResponseOut"])
    types["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"])
    types["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"])
    types["GoogleCloudDatalabelingV1beta1VertexIn"] = t.struct(
        {"y": t.integer().optional(), "x": t.integer().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1VertexIn"])
    types["GoogleCloudDatalabelingV1beta1VertexOut"] = t.struct(
        {
            "y": t.integer().optional(),
            "x": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1VertexOut"])
    types["GoogleCloudDatalabelingV1beta1CsvInstructionIn"] = t.struct(
        {"gcsFileUri": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1CsvInstructionIn"])
    types["GoogleCloudDatalabelingV1beta1CsvInstructionOut"] = t.struct(
        {
            "gcsFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1CsvInstructionOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1SegmentationConfigIn"] = t.struct(
        {"instructionMessage": t.string().optional(), "annotationSpecSet": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1SegmentationConfigIn"])
    types["GoogleCloudDatalabelingV1beta1SegmentationConfigOut"] = t.struct(
        {
            "instructionMessage": t.string().optional(),
            "annotationSpecSet": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1SegmentationConfigOut"])
    types["GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyIn"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1NormalizedVertexIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyIn"])
    types["GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyOut"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1NormalizedBoundingPolyOut"])
    types["GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationIn"] = t.struct(
        {
            "sequentialSegment": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1SequentialSegmentIn"]
            ).optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationOut"] = t.struct(
        {
            "sequentialSegment": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1SequentialSegmentOut"]
            ).optional(),
            "annotationSpec": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotationOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "feedbackThreads": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1FeedbackThreadIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "feedbackThreads": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1FeedbackThreadOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseOut"])
    types["GoogleCloudDatalabelingV1beta1ListExamplesResponseIn"] = t.struct(
        {
            "examples": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ExampleIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListExamplesResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListExamplesResponseOut"] = t.struct(
        {
            "examples": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1ExampleOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListExamplesResponseOut"])
    types["GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "annotatedDataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataIn"] = t.struct(
        {
            "boundingPolyConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigIn"]
            ).optional(),
            "eventConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EventConfigIn"]
            ).optional(),
            "videoClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoClassificationConfigIn"]
            ).optional(),
            "textClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigIn"]
            ).optional(),
            "imageClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigIn"]
            ).optional(),
            "segmentationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1SegmentationConfigIn"]
            ).optional(),
            "humanAnnotationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional(),
            "objectTrackingConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigIn"]
            ).optional(),
            "textEntityExtractionConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigIn"]
            ).optional(),
            "polylineConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PolylineConfigIn"]
            ).optional(),
            "objectDetectionConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataOut"] = t.struct(
        {
            "boundingPolyConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigOut"]
            ).optional(),
            "eventConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1EventConfigOut"]
            ).optional(),
            "videoClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoClassificationConfigOut"]
            ).optional(),
            "textClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigOut"]
            ).optional(),
            "imageClassificationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigOut"]
            ).optional(),
            "segmentationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1SegmentationConfigOut"]
            ).optional(),
            "humanAnnotationConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "objectTrackingConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigOut"]
            ).optional(),
            "textEntityExtractionConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigOut"]
            ).optional(),
            "polylineConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PolylineConfigOut"]
            ).optional(),
            "objectDetectionConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1GcsDestinationIn"] = t.struct(
        {"outputUri": t.string(), "mimeType": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1GcsDestinationIn"])
    types["GoogleCloudDatalabelingV1beta1GcsDestinationOut"] = t.struct(
        {
            "outputUri": t.string(),
            "mimeType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1GcsDestinationOut"])
    types["GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponseIn"] = t.struct(
        {
            "importCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "totalCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponseIn"])
    types["GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponseOut"] = t.struct(
        {
            "importCount": t.integer().optional(),
            "dataset": t.string().optional(),
            "totalCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponseOut"])
    types["GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadataIn"] = t.struct(
        {
            "instruction": t.string().optional(),
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadataIn"])
    types["GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadataOut"] = t.struct(
        {
            "instruction": t.string().optional(),
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadataOut"])
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadataIn"] = t.struct(
        {
            "videoObjectDetectionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataIn"
                ]
            ).optional(),
            "videoClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataIn"
                ]
            ).optional(),
            "imageOrientedBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataIn"
                ]
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "dataset": t.string().optional(),
            "videoEventDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataIn"
                ]
            ).optional(),
            "imagePolylineDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataIn"
                ]
            ).optional(),
            "imageSegmentationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataIn"
                ]
            ).optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "imageBoundingPolyDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataIn"
                ]
            ).optional(),
            "videoObjectTrackingDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataIn"
                ]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "imageBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataIn"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "textEntityExtractionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataIn"
                ]
            ).optional(),
            "imageClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataIn"
                ]
            ).optional(),
            "textClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadataOut"] = t.struct(
        {
            "videoObjectDetectionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadataOut"
                ]
            ).optional(),
            "videoClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadataOut"
                ]
            ).optional(),
            "imageOrientedBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadataOut"
                ]
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "dataset": t.string().optional(),
            "videoEventDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadataOut"
                ]
            ).optional(),
            "imagePolylineDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadataOut"
                ]
            ).optional(),
            "imageSegmentationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadataOut"
                ]
            ).optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "imageBoundingPolyDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadataOut"
                ]
            ).optional(),
            "videoObjectTrackingDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadataOut"
                ]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "imageBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadataOut"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "textEntityExtractionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadataOut"
                ]
            ).optional(),
            "imageClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadataOut"
                ]
            ).optional(),
            "textClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1AttemptIn"] = t.struct(
        {
            "attemptTime": t.string(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AttemptIn"])
    types["GoogleCloudDatalabelingV1beta1AttemptOut"] = t.struct(
        {
            "attemptTime": t.string(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AttemptOut"])
    types["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"] = t.struct(
        {
            "contributorEmails": t.array(t.string()).optional(),
            "annotatedDatasetDescription": t.string().optional(),
            "annotatedDatasetDisplayName": t.string(),
            "labelGroup": t.string().optional(),
            "userEmailAddress": t.string().optional(),
            "instruction": t.string(),
            "replicaCount": t.integer().optional(),
            "questionDuration": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigIn"])
    types["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"] = t.struct(
        {
            "contributorEmails": t.array(t.string()).optional(),
            "annotatedDatasetDescription": t.string().optional(),
            "annotatedDatasetDisplayName": t.string(),
            "labelGroup": t.string().optional(),
            "userEmailAddress": t.string().optional(),
            "instruction": t.string(),
            "replicaCount": t.integer().optional(),
            "questionDuration": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfigOut"])
    types["GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "imageBytes": t.string().optional(),
            "annotationColors": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationIn"])
    types["GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "imageBytes": t.string().optional(),
            "annotationColors": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotationOut"])
    types["GoogleCloudDatalabelingV1beta1ImportDataRequestIn"] = t.struct(
        {
            "userEmailAddress": t.string().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1InputConfigIn"]
            ),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImportDataRequestIn"])
    types["GoogleCloudDatalabelingV1beta1ImportDataRequestOut"] = t.struct(
        {
            "userEmailAddress": t.string().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1InputConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ImportDataRequestOut"])
    types["GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigIn"] = t.struct(
        {"annotationSpecSet": t.string(), "allowMultiLabel": t.boolean().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigIn"])
    types["GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigOut"] = t.struct(
        {
            "annotationSpecSet": t.string(),
            "allowMultiLabel": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfigOut"])
    types["GoogleCloudDatalabelingV1beta1BoundingPolyConfigIn"] = t.struct(
        {"instructionMessage": t.string().optional(), "annotationSpecSet": t.string()}
    ).named(renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigIn"])
    types["GoogleCloudDatalabelingV1beta1BoundingPolyConfigOut"] = t.struct(
        {
            "instructionMessage": t.string().optional(),
            "annotationSpecSet": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigOut"])
    types["GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequestIn"] = t.struct(
        {
            "annotationSpecSet": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetIn"]
            )
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequestIn"])
    types["GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequestOut"] = t.struct(
        {
            "annotationSpecSet": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequestOut"])
    types["GoogleCloudDatalabelingV1beta1AnnotatedDatasetIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "completedExampleCount": t.string().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataIn"]
            ).optional(),
            "annotationType": t.string().optional(),
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1LabelStatsIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "exampleCount": t.string().optional(),
            "blockingResources": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "annotationSource": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetIn"])
    types["GoogleCloudDatalabelingV1beta1AnnotatedDatasetOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "completedExampleCount": t.string().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadataOut"]
            ).optional(),
            "annotationType": t.string().optional(),
            "labelStats": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1LabelStatsOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "exampleCount": t.string().optional(),
            "blockingResources": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "annotationSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetOut"])
    types["GoogleCloudDatalabelingV1beta1ExportDataOperationMetadataIn"] = t.struct(
        {
            "annotatedDataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExportDataOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1ExportDataOperationMetadataOut"] = t.struct(
        {
            "annotatedDataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ExportDataOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseIn"] = t.struct(
        {
            "annotationSpecSets": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseIn"])
    types["GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseOut"] = t.struct(
        {
            "annotationSpecSets": t.array(
                t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1OutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1GcsDestinationIn"]
            ).optional(),
            "gcsFolderDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1GcsFolderDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1OutputConfigIn"])
    types["GoogleCloudDatalabelingV1beta1OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1GcsDestinationOut"]
            ).optional(),
            "gcsFolderDestination": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1GcsFolderDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1OutputConfigOut"])
    types["GoogleCloudDatalabelingV1beta1DataItemIn"] = t.struct(
        {
            "name": t.string().optional(),
            "textPayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextPayloadIn"]
            ).optional(),
            "videoPayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoPayloadIn"]
            ).optional(),
            "imagePayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImagePayloadIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1DataItemIn"])
    types["GoogleCloudDatalabelingV1beta1DataItemOut"] = t.struct(
        {
            "name": t.string().optional(),
            "textPayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1TextPayloadOut"]
            ).optional(),
            "videoPayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1VideoPayloadOut"]
            ).optional(),
            "imagePayload": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ImagePayloadOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1DataItemOut"])
    types[
        "GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataIn"]
    )
    types[
        "GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataOut"]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataIn"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataOut"
    ] = t.struct(
        {
            "basicConfig": t.proxy(
                renames["GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDatalabelingV1beta1ClassificationMetricsIn"] = t.struct(
        {
            "confusionMatrix": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ConfusionMatrixIn"]
            ).optional(),
            "prCurve": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PrCurveIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ClassificationMetricsIn"])
    types["GoogleCloudDatalabelingV1beta1ClassificationMetricsOut"] = t.struct(
        {
            "confusionMatrix": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1ConfusionMatrixOut"]
            ).optional(),
            "prCurve": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PrCurveOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1ClassificationMetricsOut"])
    types["GoogleCloudDatalabelingV1beta1LabelOperationMetadataIn"] = t.struct(
        {
            "imageOrientedBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataIn"
                ]
            ).optional(),
            "imageBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataIn"
                ]
            ).optional(),
            "videoClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataIn"
                ]
            ).optional(),
            "imageBoundingPolyDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataIn"
                ]
            ).optional(),
            "videoEventDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataIn"
                ]
            ).optional(),
            "imagePolylineDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataIn"
                ]
            ).optional(),
            "videoObjectDetectionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataIn"
                ]
            ).optional(),
            "videoObjectTrackingDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataIn"
                ]
            ).optional(),
            "imageClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataIn"
                ]
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "imageSegmentationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataIn"
                ]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "dataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "textEntityExtractionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataIn"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "textClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1beta1LabelOperationMetadataOut"] = t.struct(
        {
            "imageOrientedBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadataOut"
                ]
            ).optional(),
            "imageBoundingBoxDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadataOut"
                ]
            ).optional(),
            "videoClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadataOut"
                ]
            ).optional(),
            "imageBoundingPolyDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadataOut"
                ]
            ).optional(),
            "videoEventDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadataOut"
                ]
            ).optional(),
            "imagePolylineDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadataOut"
                ]
            ).optional(),
            "videoObjectDetectionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadataOut"
                ]
            ).optional(),
            "videoObjectTrackingDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadataOut"
                ]
            ).optional(),
            "imageClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadataOut"
                ]
            ).optional(),
            "annotatedDataset": t.string().optional(),
            "imageSegmentationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadataOut"
                ]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "dataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "textEntityExtractionDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadataOut"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "textClassificationDetails": t.proxy(
                renames[
                    "GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1LabelOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequestIn"])
    types["GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequestOut"])
    types["GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadataIn"])
    types["GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadataOut"])
    types["GoogleCloudDatalabelingV1beta1InstructionIn"] = t.struct(
        {
            "blockingResources": t.array(t.string()).optional(),
            "csvInstruction": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1CsvInstructionIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "dataType": t.string(),
            "createTime": t.string().optional(),
            "pdfInstruction": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PdfInstructionIn"]
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1InstructionIn"])
    types["GoogleCloudDatalabelingV1beta1InstructionOut"] = t.struct(
        {
            "blockingResources": t.array(t.string()).optional(),
            "csvInstruction": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1CsvInstructionOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "dataType": t.string(),
            "createTime": t.string().optional(),
            "pdfInstruction": t.proxy(
                renames["GoogleCloudDatalabelingV1beta1PdfInstructionOut"]
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatalabelingV1beta1InstructionOut"])

    functions = {}
    functions["projectsEvaluationsSearch"] = datalabeling.get(
        "v1beta1/{parent}/evaluations:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAnnotationSpecSetsCreate"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAnnotationSpecSetsDelete"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAnnotationSpecSetsList"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAnnotationSpecSetsGet"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotationSpecSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstructionsCreate"] = datalabeling.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstructionsGet"] = datalabeling.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstructionsList"] = datalabeling.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstructionsDelete"] = datalabeling.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEvaluationJobsGet"] = datalabeling.post(
        "v1beta1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEvaluationJobsCreate"] = datalabeling.post(
        "v1beta1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEvaluationJobsPause"] = datalabeling.post(
        "v1beta1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEvaluationJobsPatch"] = datalabeling.post(
        "v1beta1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEvaluationJobsDelete"] = datalabeling.post(
        "v1beta1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEvaluationJobsList"] = datalabeling.post(
        "v1beta1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEvaluationJobsResume"] = datalabeling.post(
        "v1beta1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = datalabeling.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = datalabeling.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsCancel"] = datalabeling.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsDelete"] = datalabeling.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsDelete"] = datalabeling.post(
        "v1beta1/{parent}/datasets",
        t.struct(
            {
                "parent": t.string(),
                "dataset": t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsGet"] = datalabeling.post(
        "v1beta1/{parent}/datasets",
        t.struct(
            {
                "parent": t.string(),
                "dataset": t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsList"] = datalabeling.post(
        "v1beta1/{parent}/datasets",
        t.struct(
            {
                "parent": t.string(),
                "dataset": t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsImportData"] = datalabeling.post(
        "v1beta1/{parent}/datasets",
        t.struct(
            {
                "parent": t.string(),
                "dataset": t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsExportData"] = datalabeling.post(
        "v1beta1/{parent}/datasets",
        t.struct(
            {
                "parent": t.string(),
                "dataset": t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsCreate"] = datalabeling.post(
        "v1beta1/{parent}/datasets",
        t.struct(
            {
                "parent": t.string(),
                "dataset": t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsImageLabel"] = datalabeling.post(
        "v1beta1/{parent}/image:label",
        t.struct(
            {
                "parent": t.string(),
                "imageClassificationConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1ImageClassificationConfigIn"]
                ).optional(),
                "segmentationConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1SegmentationConfigIn"]
                ).optional(),
                "boundingPolyConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1BoundingPolyConfigIn"]
                ).optional(),
                "basicConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
                ),
                "feature": t.string(),
                "polylineConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1PolylineConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsTextLabel"] = datalabeling.post(
        "v1beta1/{parent}/text:label",
        t.struct(
            {
                "parent": t.string(),
                "textClassificationConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1TextClassificationConfigIn"]
                ).optional(),
                "feature": t.string(),
                "basicConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
                ),
                "textEntityExtractionConfig": t.proxy(
                    renames[
                        "GoogleCloudDatalabelingV1beta1TextEntityExtractionConfigIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsEvaluationsGet"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1EvaluationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsDatasetsEvaluationsExampleComparisonsSearch"
    ] = datalabeling.post(
        "v1beta1/{parent}/exampleComparisons:search",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsVideoLabel"] = datalabeling.post(
        "v1beta1/{parent}/video:label",
        t.struct(
            {
                "parent": t.string(),
                "basicConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1HumanAnnotationConfigIn"]
                ),
                "eventConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1EventConfigIn"]
                ).optional(),
                "feature": t.string(),
                "videoClassificationConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1VideoClassificationConfigIn"]
                ).optional(),
                "objectTrackingConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1ObjectTrackingConfigIn"]
                ).optional(),
                "objectDetectionConfig": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1ObjectDetectionConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsDataItemsGet"] = datalabeling.get(
        "v1beta1/{parent}/dataItems",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1ListDataItemsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsDataItemsList"] = datalabeling.get(
        "v1beta1/{parent}/dataItems",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1ListDataItemsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsAnnotatedDatasetsDelete"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsAnnotatedDatasetsList"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsAnnotatedDatasetsGet"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1AnnotatedDatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsDatasetsAnnotatedDatasetsFeedbackThreadsDelete"
    ] = datalabeling.get(
        "v1beta1/{parent}/feedbackThreads",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsAnnotatedDatasetsFeedbackThreadsGet"] = datalabeling.get(
        "v1beta1/{parent}/feedbackThreads",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsDatasetsAnnotatedDatasetsFeedbackThreadsList"
    ] = datalabeling.get(
        "v1beta1/{parent}/feedbackThreads",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsDatasetsAnnotatedDatasetsFeedbackThreadsFeedbackMessagesDelete"
    ] = datalabeling.post(
        "v1beta1/{parent}/feedbackMessages",
        t.struct(
            {
                "parent": t.string(),
                "body": t.string().optional(),
                "createTime": t.string().optional(),
                "requesterFeedbackMetadata": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn"]
                ),
                "operatorFeedbackMetadata": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn"]
                ),
                "name": t.string().optional(),
                "image": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsDatasetsAnnotatedDatasetsFeedbackThreadsFeedbackMessagesList"
    ] = datalabeling.post(
        "v1beta1/{parent}/feedbackMessages",
        t.struct(
            {
                "parent": t.string(),
                "body": t.string().optional(),
                "createTime": t.string().optional(),
                "requesterFeedbackMetadata": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn"]
                ),
                "operatorFeedbackMetadata": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn"]
                ),
                "name": t.string().optional(),
                "image": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsDatasetsAnnotatedDatasetsFeedbackThreadsFeedbackMessagesGet"
    ] = datalabeling.post(
        "v1beta1/{parent}/feedbackMessages",
        t.struct(
            {
                "parent": t.string(),
                "body": t.string().optional(),
                "createTime": t.string().optional(),
                "requesterFeedbackMetadata": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn"]
                ),
                "operatorFeedbackMetadata": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn"]
                ),
                "name": t.string().optional(),
                "image": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsDatasetsAnnotatedDatasetsFeedbackThreadsFeedbackMessagesCreate"
    ] = datalabeling.post(
        "v1beta1/{parent}/feedbackMessages",
        t.struct(
            {
                "parent": t.string(),
                "body": t.string().optional(),
                "createTime": t.string().optional(),
                "requesterFeedbackMetadata": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadataIn"]
                ),
                "operatorFeedbackMetadata": t.proxy(
                    renames["GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadataIn"]
                ),
                "name": t.string().optional(),
                "image": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsAnnotatedDatasetsDataItemsGet"] = datalabeling.get(
        "v1beta1/{parent}/dataItems",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1ListDataItemsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsAnnotatedDatasetsDataItemsList"] = datalabeling.get(
        "v1beta1/{parent}/dataItems",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1ListDataItemsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsAnnotatedDatasetsExamplesList"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1ExampleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatasetsAnnotatedDatasetsExamplesGet"] = datalabeling.get(
        "v1beta1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatalabelingV1beta1ExampleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datalabeling",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
