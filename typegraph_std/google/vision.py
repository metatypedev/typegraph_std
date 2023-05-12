from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_vision() -> Import:
    vision = HTTPRuntime("https://vision.googleapis.com/")

    renames = {
        "ErrorResponse": "_vision_1_ErrorResponse",
        "GoogleCloudVisionV1p3beta1BoundingPolyIn": "_vision_2_GoogleCloudVisionV1p3beta1BoundingPolyIn",
        "GoogleCloudVisionV1p3beta1BoundingPolyOut": "_vision_3_GoogleCloudVisionV1p3beta1BoundingPolyOut",
        "GoogleCloudVisionV1p3beta1PageIn": "_vision_4_GoogleCloudVisionV1p3beta1PageIn",
        "GoogleCloudVisionV1p3beta1PageOut": "_vision_5_GoogleCloudVisionV1p3beta1PageOut",
        "GoogleCloudVisionV1p3beta1LocationInfoIn": "_vision_6_GoogleCloudVisionV1p3beta1LocationInfoIn",
        "GoogleCloudVisionV1p3beta1LocationInfoOut": "_vision_7_GoogleCloudVisionV1p3beta1LocationInfoOut",
        "AnnotateImageResponseIn": "_vision_8_AnnotateImageResponseIn",
        "AnnotateImageResponseOut": "_vision_9_AnnotateImageResponseOut",
        "GoogleCloudVisionV1p2beta1InputConfigIn": "_vision_10_GoogleCloudVisionV1p2beta1InputConfigIn",
        "GoogleCloudVisionV1p2beta1InputConfigOut": "_vision_11_GoogleCloudVisionV1p2beta1InputConfigOut",
        "BatchAnnotateImagesResponseIn": "_vision_12_BatchAnnotateImagesResponseIn",
        "BatchAnnotateImagesResponseOut": "_vision_13_BatchAnnotateImagesResponseOut",
        "GoogleCloudVisionV1p2beta1OutputConfigIn": "_vision_14_GoogleCloudVisionV1p2beta1OutputConfigIn",
        "GoogleCloudVisionV1p2beta1OutputConfigOut": "_vision_15_GoogleCloudVisionV1p2beta1OutputConfigOut",
        "GoogleCloudVisionV1p1beta1ProductKeyValueIn": "_vision_16_GoogleCloudVisionV1p1beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p1beta1ProductKeyValueOut": "_vision_17_GoogleCloudVisionV1p1beta1ProductKeyValueOut",
        "ImageSourceIn": "_vision_18_ImageSourceIn",
        "ImageSourceOut": "_vision_19_ImageSourceOut",
        "GoogleCloudVisionV1p1beta1OutputConfigIn": "_vision_20_GoogleCloudVisionV1p1beta1OutputConfigIn",
        "GoogleCloudVisionV1p1beta1OutputConfigOut": "_vision_21_GoogleCloudVisionV1p1beta1OutputConfigOut",
        "ProductSearchParamsIn": "_vision_22_ProductSearchParamsIn",
        "ProductSearchParamsOut": "_vision_23_ProductSearchParamsOut",
        "GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn": "_vision_24_GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut": "_vision_25_GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn": "_vision_26_GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut": "_vision_27_GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p3beta1WebDetectionIn": "_vision_28_GoogleCloudVisionV1p3beta1WebDetectionIn",
        "GoogleCloudVisionV1p3beta1WebDetectionOut": "_vision_29_GoogleCloudVisionV1p3beta1WebDetectionOut",
        "GoogleCloudVisionV1p3beta1AnnotateFileResponseIn": "_vision_30_GoogleCloudVisionV1p3beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p3beta1AnnotateFileResponseOut": "_vision_31_GoogleCloudVisionV1p3beta1AnnotateFileResponseOut",
        "GoogleCloudVisionV1p3beta1CropHintsAnnotationIn": "_vision_32_GoogleCloudVisionV1p3beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p3beta1CropHintsAnnotationOut": "_vision_33_GoogleCloudVisionV1p3beta1CropHintsAnnotationOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsIn": "_vision_34_GoogleCloudVisionV1p3beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsOut": "_vision_35_GoogleCloudVisionV1p3beta1ProductSearchResultsOut",
        "WebEntityIn": "_vision_36_WebEntityIn",
        "WebEntityOut": "_vision_37_WebEntityOut",
        "GoogleCloudVisionV1p4beta1ParagraphIn": "_vision_38_GoogleCloudVisionV1p4beta1ParagraphIn",
        "GoogleCloudVisionV1p4beta1ParagraphOut": "_vision_39_GoogleCloudVisionV1p4beta1ParagraphOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsIn": "_vision_40_GoogleCloudVisionV1p4beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsOut": "_vision_41_GoogleCloudVisionV1p4beta1ProductSearchResultsOut",
        "CropHintIn": "_vision_42_CropHintIn",
        "CropHintOut": "_vision_43_CropHintOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn": "_vision_44_GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut": "_vision_45_GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p3beta1OperationMetadataIn": "_vision_46_GoogleCloudVisionV1p3beta1OperationMetadataIn",
        "GoogleCloudVisionV1p3beta1OperationMetadataOut": "_vision_47_GoogleCloudVisionV1p3beta1OperationMetadataOut",
        "GoogleCloudVisionV1p3beta1ImageAnnotationContextIn": "_vision_48_GoogleCloudVisionV1p3beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p3beta1ImageAnnotationContextOut": "_vision_49_GoogleCloudVisionV1p3beta1ImageAnnotationContextOut",
        "OutputConfigIn": "_vision_50_OutputConfigIn",
        "OutputConfigOut": "_vision_51_OutputConfigOut",
        "GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn": "_vision_52_GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut": "_vision_53_GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p4beta1FaceRecognitionResultIn": "_vision_54_GoogleCloudVisionV1p4beta1FaceRecognitionResultIn",
        "GoogleCloudVisionV1p4beta1FaceRecognitionResultOut": "_vision_55_GoogleCloudVisionV1p4beta1FaceRecognitionResultOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn": "_vision_56_GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut": "_vision_57_GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p1beta1GcsSourceIn": "_vision_58_GoogleCloudVisionV1p1beta1GcsSourceIn",
        "GoogleCloudVisionV1p1beta1GcsSourceOut": "_vision_59_GoogleCloudVisionV1p1beta1GcsSourceOut",
        "OperationMetadataIn": "_vision_60_OperationMetadataIn",
        "OperationMetadataOut": "_vision_61_OperationMetadataOut",
        "AnnotateFileRequestIn": "_vision_62_AnnotateFileRequestIn",
        "AnnotateFileRequestOut": "_vision_63_AnnotateFileRequestOut",
        "GoogleCloudVisionV1p4beta1NormalizedVertexIn": "_vision_64_GoogleCloudVisionV1p4beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p4beta1NormalizedVertexOut": "_vision_65_GoogleCloudVisionV1p4beta1NormalizedVertexOut",
        "GoogleCloudVisionV1p2beta1LocationInfoIn": "_vision_66_GoogleCloudVisionV1p2beta1LocationInfoIn",
        "GoogleCloudVisionV1p2beta1LocationInfoOut": "_vision_67_GoogleCloudVisionV1p2beta1LocationInfoOut",
        "GoogleCloudVisionV1p2beta1ProductKeyValueIn": "_vision_68_GoogleCloudVisionV1p2beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p2beta1ProductKeyValueOut": "_vision_69_GoogleCloudVisionV1p2beta1ProductKeyValueOut",
        "GoogleCloudVisionV1p1beta1ImagePropertiesIn": "_vision_70_GoogleCloudVisionV1p1beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p1beta1ImagePropertiesOut": "_vision_71_GoogleCloudVisionV1p1beta1ImagePropertiesOut",
        "GoogleCloudVisionV1p2beta1FaceAnnotationIn": "_vision_72_GoogleCloudVisionV1p2beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p2beta1FaceAnnotationOut": "_vision_73_GoogleCloudVisionV1p2beta1FaceAnnotationOut",
        "LocalizedObjectAnnotationIn": "_vision_74_LocalizedObjectAnnotationIn",
        "LocalizedObjectAnnotationOut": "_vision_75_LocalizedObjectAnnotationOut",
        "ImagePropertiesIn": "_vision_76_ImagePropertiesIn",
        "ImagePropertiesOut": "_vision_77_ImagePropertiesOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebImageIn": "_vision_78_GoogleCloudVisionV1p4beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebImageOut": "_vision_79_GoogleCloudVisionV1p4beta1WebDetectionWebImageOut",
        "GoogleCloudVisionV1p1beta1EntityAnnotationIn": "_vision_80_GoogleCloudVisionV1p1beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p1beta1EntityAnnotationOut": "_vision_81_GoogleCloudVisionV1p1beta1EntityAnnotationOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebImageIn": "_vision_82_GoogleCloudVisionV1p3beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebImageOut": "_vision_83_GoogleCloudVisionV1p3beta1WebDetectionWebImageOut",
        "WebDetectionIn": "_vision_84_WebDetectionIn",
        "WebDetectionOut": "_vision_85_WebDetectionOut",
        "GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseIn": "_vision_86_GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseOut": "_vision_87_GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseOut",
        "ColorIn": "_vision_88_ColorIn",
        "ColorOut": "_vision_89_ColorOut",
        "GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn": "_vision_90_GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut": "_vision_91_GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p4beta1ColorInfoIn": "_vision_92_GoogleCloudVisionV1p4beta1ColorInfoIn",
        "GoogleCloudVisionV1p4beta1ColorInfoOut": "_vision_93_GoogleCloudVisionV1p4beta1ColorInfoOut",
        "GoogleCloudVisionV1p3beta1BlockIn": "_vision_94_GoogleCloudVisionV1p3beta1BlockIn",
        "GoogleCloudVisionV1p3beta1BlockOut": "_vision_95_GoogleCloudVisionV1p3beta1BlockOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn": "_vision_96_GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut": "_vision_97_GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p3beta1CropHintIn": "_vision_98_GoogleCloudVisionV1p3beta1CropHintIn",
        "GoogleCloudVisionV1p3beta1CropHintOut": "_vision_99_GoogleCloudVisionV1p3beta1CropHintOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn": "_vision_100_GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut": "_vision_101_GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p3beta1AnnotateImageResponseIn": "_vision_102_GoogleCloudVisionV1p3beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p3beta1AnnotateImageResponseOut": "_vision_103_GoogleCloudVisionV1p3beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn": "_vision_104_GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut": "_vision_105_GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn": "_vision_106_GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut": "_vision_107_GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn": "_vision_108_GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut": "_vision_109_GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn": "_vision_110_GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut": "_vision_111_GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut",
        "GoogleCloudVisionV1p2beta1SymbolIn": "_vision_112_GoogleCloudVisionV1p2beta1SymbolIn",
        "GoogleCloudVisionV1p2beta1SymbolOut": "_vision_113_GoogleCloudVisionV1p2beta1SymbolOut",
        "BatchAnnotateFilesRequestIn": "_vision_114_BatchAnnotateFilesRequestIn",
        "BatchAnnotateFilesRequestOut": "_vision_115_BatchAnnotateFilesRequestOut",
        "GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn": "_vision_116_GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut": "_vision_117_GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn": "_vision_118_GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut": "_vision_119_GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p1beta1ParagraphIn": "_vision_120_GoogleCloudVisionV1p1beta1ParagraphIn",
        "GoogleCloudVisionV1p1beta1ParagraphOut": "_vision_121_GoogleCloudVisionV1p1beta1ParagraphOut",
        "GoogleCloudVisionV1p4beta1WebDetectionIn": "_vision_122_GoogleCloudVisionV1p4beta1WebDetectionIn",
        "GoogleCloudVisionV1p4beta1WebDetectionOut": "_vision_123_GoogleCloudVisionV1p4beta1WebDetectionOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn": "_vision_124_GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut": "_vision_125_GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p1beta1BlockIn": "_vision_126_GoogleCloudVisionV1p1beta1BlockIn",
        "GoogleCloudVisionV1p1beta1BlockOut": "_vision_127_GoogleCloudVisionV1p1beta1BlockOut",
        "GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn": "_vision_128_GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut": "_vision_129_GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p4beta1EntityAnnotationIn": "_vision_130_GoogleCloudVisionV1p4beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p4beta1EntityAnnotationOut": "_vision_131_GoogleCloudVisionV1p4beta1EntityAnnotationOut",
        "GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseIn": "_vision_132_GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseOut": "_vision_133_GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn": "_vision_134_GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut": "_vision_135_GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut",
        "ListProductsInProductSetResponseIn": "_vision_136_ListProductsInProductSetResponseIn",
        "ListProductsInProductSetResponseOut": "_vision_137_ListProductsInProductSetResponseOut",
        "GoogleCloudVisionV1p2beta1PropertyIn": "_vision_138_GoogleCloudVisionV1p2beta1PropertyIn",
        "GoogleCloudVisionV1p2beta1PropertyOut": "_vision_139_GoogleCloudVisionV1p2beta1PropertyOut",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseIn": "_vision_140_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseOut": "_vision_141_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseOut",
        "PropertyIn": "_vision_142_PropertyIn",
        "PropertyOut": "_vision_143_PropertyOut",
        "AsyncBatchAnnotateImagesRequestIn": "_vision_144_AsyncBatchAnnotateImagesRequestIn",
        "AsyncBatchAnnotateImagesRequestOut": "_vision_145_AsyncBatchAnnotateImagesRequestOut",
        "GoogleCloudVisionV1p1beta1WordIn": "_vision_146_GoogleCloudVisionV1p1beta1WordIn",
        "GoogleCloudVisionV1p1beta1WordOut": "_vision_147_GoogleCloudVisionV1p1beta1WordOut",
        "GoogleCloudVisionV1p2beta1ImageAnnotationContextIn": "_vision_148_GoogleCloudVisionV1p2beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p2beta1ImageAnnotationContextOut": "_vision_149_GoogleCloudVisionV1p2beta1ImageAnnotationContextOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn": "_vision_150_GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut": "_vision_151_GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebPageIn": "_vision_152_GoogleCloudVisionV1p4beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebPageOut": "_vision_153_GoogleCloudVisionV1p4beta1WebDetectionWebPageOut",
        "GoogleCloudVisionV1p2beta1WordIn": "_vision_154_GoogleCloudVisionV1p2beta1WordIn",
        "GoogleCloudVisionV1p2beta1WordOut": "_vision_155_GoogleCloudVisionV1p2beta1WordOut",
        "GoogleCloudVisionV1p1beta1GcsDestinationIn": "_vision_156_GoogleCloudVisionV1p1beta1GcsDestinationIn",
        "GoogleCloudVisionV1p1beta1GcsDestinationOut": "_vision_157_GoogleCloudVisionV1p1beta1GcsDestinationOut",
        "TextPropertyIn": "_vision_158_TextPropertyIn",
        "TextPropertyOut": "_vision_159_TextPropertyOut",
        "GoogleCloudVisionV1p2beta1BlockIn": "_vision_160_GoogleCloudVisionV1p2beta1BlockIn",
        "GoogleCloudVisionV1p2beta1BlockOut": "_vision_161_GoogleCloudVisionV1p2beta1BlockOut",
        "GoogleCloudVisionV1p1beta1AnnotateImageResponseIn": "_vision_162_GoogleCloudVisionV1p1beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p1beta1AnnotateImageResponseOut": "_vision_163_GoogleCloudVisionV1p1beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn": "_vision_164_GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut": "_vision_165_GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut",
        "ResultIn": "_vision_166_ResultIn",
        "ResultOut": "_vision_167_ResultOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn": "_vision_168_GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut": "_vision_169_GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p4beta1VertexIn": "_vision_170_GoogleCloudVisionV1p4beta1VertexIn",
        "GoogleCloudVisionV1p4beta1VertexOut": "_vision_171_GoogleCloudVisionV1p4beta1VertexOut",
        "WebLabelIn": "_vision_172_WebLabelIn",
        "WebLabelOut": "_vision_173_WebLabelOut",
        "InputConfigIn": "_vision_174_InputConfigIn",
        "InputConfigOut": "_vision_175_InputConfigOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn": "_vision_176_GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut": "_vision_177_GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p2beta1PositionIn": "_vision_178_GoogleCloudVisionV1p2beta1PositionIn",
        "GoogleCloudVisionV1p2beta1PositionOut": "_vision_179_GoogleCloudVisionV1p2beta1PositionOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn": "_vision_180_GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut": "_vision_181_GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut",
        "ImageIn": "_vision_182_ImageIn",
        "ImageOut": "_vision_183_ImageOut",
        "GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn": "_vision_184_GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut": "_vision_185_GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut",
        "ImageContextIn": "_vision_186_ImageContextIn",
        "ImageContextOut": "_vision_187_ImageContextOut",
        "AsyncBatchAnnotateFilesRequestIn": "_vision_188_AsyncBatchAnnotateFilesRequestIn",
        "AsyncBatchAnnotateFilesRequestOut": "_vision_189_AsyncBatchAnnotateFilesRequestOut",
        "GoogleCloudVisionV1p3beta1VertexIn": "_vision_190_GoogleCloudVisionV1p3beta1VertexIn",
        "GoogleCloudVisionV1p3beta1VertexOut": "_vision_191_GoogleCloudVisionV1p3beta1VertexOut",
        "GoogleCloudVisionV1p3beta1ColorInfoIn": "_vision_192_GoogleCloudVisionV1p3beta1ColorInfoIn",
        "GoogleCloudVisionV1p3beta1ColorInfoOut": "_vision_193_GoogleCloudVisionV1p3beta1ColorInfoOut",
        "ImportProductSetsRequestIn": "_vision_194_ImportProductSetsRequestIn",
        "ImportProductSetsRequestOut": "_vision_195_ImportProductSetsRequestOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn": "_vision_196_GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut": "_vision_197_GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn": "_vision_198_GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut": "_vision_199_GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p1beta1CropHintsAnnotationIn": "_vision_200_GoogleCloudVisionV1p1beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p1beta1CropHintsAnnotationOut": "_vision_201_GoogleCloudVisionV1p1beta1CropHintsAnnotationOut",
        "TextDetectionParamsIn": "_vision_202_TextDetectionParamsIn",
        "TextDetectionParamsOut": "_vision_203_TextDetectionParamsOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsIn": "_vision_204_GoogleCloudVisionV1p1beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsOut": "_vision_205_GoogleCloudVisionV1p1beta1ProductSearchResultsOut",
        "ListOperationsResponseIn": "_vision_206_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vision_207_ListOperationsResponseOut",
        "GoogleCloudVisionV1p2beta1WebDetectionIn": "_vision_208_GoogleCloudVisionV1p2beta1WebDetectionIn",
        "GoogleCloudVisionV1p2beta1WebDetectionOut": "_vision_209_GoogleCloudVisionV1p2beta1WebDetectionOut",
        "NormalizedVertexIn": "_vision_210_NormalizedVertexIn",
        "NormalizedVertexOut": "_vision_211_NormalizedVertexOut",
        "GoogleCloudVisionV1p4beta1FaceAnnotationIn": "_vision_212_GoogleCloudVisionV1p4beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p4beta1FaceAnnotationOut": "_vision_213_GoogleCloudVisionV1p4beta1FaceAnnotationOut",
        "AsyncBatchAnnotateFilesResponseIn": "_vision_214_AsyncBatchAnnotateFilesResponseIn",
        "AsyncBatchAnnotateFilesResponseOut": "_vision_215_AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p4beta1LocationInfoIn": "_vision_216_GoogleCloudVisionV1p4beta1LocationInfoIn",
        "GoogleCloudVisionV1p4beta1LocationInfoOut": "_vision_217_GoogleCloudVisionV1p4beta1LocationInfoOut",
        "EmptyIn": "_vision_218_EmptyIn",
        "EmptyOut": "_vision_219_EmptyOut",
        "FaceAnnotationIn": "_vision_220_FaceAnnotationIn",
        "FaceAnnotationOut": "_vision_221_FaceAnnotationOut",
        "GoogleCloudVisionV1p4beta1ImagePropertiesIn": "_vision_222_GoogleCloudVisionV1p4beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p4beta1ImagePropertiesOut": "_vision_223_GoogleCloudVisionV1p4beta1ImagePropertiesOut",
        "GoogleCloudVisionV1p2beta1BoundingPolyIn": "_vision_224_GoogleCloudVisionV1p2beta1BoundingPolyIn",
        "GoogleCloudVisionV1p2beta1BoundingPolyOut": "_vision_225_GoogleCloudVisionV1p2beta1BoundingPolyOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn": "_vision_226_GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut": "_vision_227_GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut",
        "GoogleCloudVisionV1p2beta1EntityAnnotationIn": "_vision_228_GoogleCloudVisionV1p2beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p2beta1EntityAnnotationOut": "_vision_229_GoogleCloudVisionV1p2beta1EntityAnnotationOut",
        "GcsSourceIn": "_vision_230_GcsSourceIn",
        "GcsSourceOut": "_vision_231_GcsSourceOut",
        "GoogleCloudVisionV1p3beta1ImagePropertiesIn": "_vision_232_GoogleCloudVisionV1p3beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p3beta1ImagePropertiesOut": "_vision_233_GoogleCloudVisionV1p3beta1ImagePropertiesOut",
        "GoogleCloudVisionV1p4beta1PropertyIn": "_vision_234_GoogleCloudVisionV1p4beta1PropertyIn",
        "GoogleCloudVisionV1p4beta1PropertyOut": "_vision_235_GoogleCloudVisionV1p4beta1PropertyOut",
        "GoogleCloudVisionV1p4beta1OperationMetadataIn": "_vision_236_GoogleCloudVisionV1p4beta1OperationMetadataIn",
        "GoogleCloudVisionV1p4beta1OperationMetadataOut": "_vision_237_GoogleCloudVisionV1p4beta1OperationMetadataOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn": "_vision_238_GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut": "_vision_239_GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut",
        "LandmarkIn": "_vision_240_LandmarkIn",
        "LandmarkOut": "_vision_241_LandmarkOut",
        "ListProductSetsResponseIn": "_vision_242_ListProductSetsResponseIn",
        "ListProductSetsResponseOut": "_vision_243_ListProductSetsResponseOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn": "_vision_244_GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut": "_vision_245_GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn": "_vision_246_GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut": "_vision_247_GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p2beta1NormalizedVertexIn": "_vision_248_GoogleCloudVisionV1p2beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p2beta1NormalizedVertexOut": "_vision_249_GoogleCloudVisionV1p2beta1NormalizedVertexOut",
        "BatchAnnotateFilesResponseIn": "_vision_250_BatchAnnotateFilesResponseIn",
        "BatchAnnotateFilesResponseOut": "_vision_251_BatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebImageIn": "_vision_252_GoogleCloudVisionV1p1beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebImageOut": "_vision_253_GoogleCloudVisionV1p1beta1WebDetectionWebImageOut",
        "ReferenceImageIn": "_vision_254_ReferenceImageIn",
        "ReferenceImageOut": "_vision_255_ReferenceImageOut",
        "EntityAnnotationIn": "_vision_256_EntityAnnotationIn",
        "EntityAnnotationOut": "_vision_257_EntityAnnotationOut",
        "AnnotateImageRequestIn": "_vision_258_AnnotateImageRequestIn",
        "AnnotateImageRequestOut": "_vision_259_AnnotateImageRequestOut",
        "GoogleCloudVisionV1p4beta1PositionIn": "_vision_260_GoogleCloudVisionV1p4beta1PositionIn",
        "GoogleCloudVisionV1p4beta1PositionOut": "_vision_261_GoogleCloudVisionV1p4beta1PositionOut",
        "LatLongRectIn": "_vision_262_LatLongRectIn",
        "LatLongRectOut": "_vision_263_LatLongRectOut",
        "ProductIn": "_vision_264_ProductIn",
        "ProductOut": "_vision_265_ProductOut",
        "GoogleCloudVisionV1p3beta1PositionIn": "_vision_266_GoogleCloudVisionV1p3beta1PositionIn",
        "GoogleCloudVisionV1p3beta1PositionOut": "_vision_267_GoogleCloudVisionV1p3beta1PositionOut",
        "GoogleCloudVisionV1p1beta1BoundingPolyIn": "_vision_268_GoogleCloudVisionV1p1beta1BoundingPolyIn",
        "GoogleCloudVisionV1p1beta1BoundingPolyOut": "_vision_269_GoogleCloudVisionV1p1beta1BoundingPolyOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationIn": "_vision_270_GoogleCloudVisionV1p4beta1TextAnnotationIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationOut": "_vision_271_GoogleCloudVisionV1p4beta1TextAnnotationOut",
        "ProductSearchResultsIn": "_vision_272_ProductSearchResultsIn",
        "ProductSearchResultsOut": "_vision_273_ProductSearchResultsOut",
        "GcsDestinationIn": "_vision_274_GcsDestinationIn",
        "GcsDestinationOut": "_vision_275_GcsDestinationOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsIn": "_vision_276_GoogleCloudVisionV1p2beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsOut": "_vision_277_GoogleCloudVisionV1p2beta1ProductSearchResultsOut",
        "GoogleCloudVisionV1p1beta1SymbolIn": "_vision_278_GoogleCloudVisionV1p1beta1SymbolIn",
        "GoogleCloudVisionV1p1beta1SymbolOut": "_vision_279_GoogleCloudVisionV1p1beta1SymbolOut",
        "CancelOperationRequestIn": "_vision_280_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vision_281_CancelOperationRequestOut",
        "GoogleCloudVisionV1p1beta1LocationInfoIn": "_vision_282_GoogleCloudVisionV1p1beta1LocationInfoIn",
        "GoogleCloudVisionV1p1beta1LocationInfoOut": "_vision_283_GoogleCloudVisionV1p1beta1LocationInfoOut",
        "AsyncAnnotateFileResponseIn": "_vision_284_AsyncAnnotateFileResponseIn",
        "AsyncAnnotateFileResponseOut": "_vision_285_AsyncAnnotateFileResponseOut",
        "WebImageIn": "_vision_286_WebImageIn",
        "WebImageOut": "_vision_287_WebImageOut",
        "ImportProductSetsInputConfigIn": "_vision_288_ImportProductSetsInputConfigIn",
        "ImportProductSetsInputConfigOut": "_vision_289_ImportProductSetsInputConfigOut",
        "GoogleCloudVisionV1p3beta1ProductKeyValueIn": "_vision_290_GoogleCloudVisionV1p3beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p3beta1ProductKeyValueOut": "_vision_291_GoogleCloudVisionV1p3beta1ProductKeyValueOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn": "_vision_292_GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut": "_vision_293_GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut",
        "PositionIn": "_vision_294_PositionIn",
        "PositionOut": "_vision_295_PositionOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn": "_vision_296_GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut": "_vision_297_GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut",
        "CropHintsAnnotationIn": "_vision_298_CropHintsAnnotationIn",
        "CropHintsAnnotationOut": "_vision_299_CropHintsAnnotationOut",
        "GoogleCloudVisionV1p2beta1AnnotateImageResponseIn": "_vision_300_GoogleCloudVisionV1p2beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p2beta1AnnotateImageResponseOut": "_vision_301_GoogleCloudVisionV1p2beta1AnnotateImageResponseOut",
        "RemoveProductFromProductSetRequestIn": "_vision_302_RemoveProductFromProductSetRequestIn",
        "RemoveProductFromProductSetRequestOut": "_vision_303_RemoveProductFromProductSetRequestOut",
        "GoogleCloudVisionV1p1beta1FaceAnnotationIn": "_vision_304_GoogleCloudVisionV1p1beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p1beta1FaceAnnotationOut": "_vision_305_GoogleCloudVisionV1p1beta1FaceAnnotationOut",
        "GoogleCloudVisionV1p4beta1GcsSourceIn": "_vision_306_GoogleCloudVisionV1p4beta1GcsSourceIn",
        "GoogleCloudVisionV1p4beta1GcsSourceOut": "_vision_307_GoogleCloudVisionV1p4beta1GcsSourceOut",
        "GoogleCloudVisionV1p3beta1ReferenceImageIn": "_vision_308_GoogleCloudVisionV1p3beta1ReferenceImageIn",
        "GoogleCloudVisionV1p3beta1ReferenceImageOut": "_vision_309_GoogleCloudVisionV1p3beta1ReferenceImageOut",
        "GoogleCloudVisionV1p4beta1CropHintsAnnotationIn": "_vision_310_GoogleCloudVisionV1p4beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p4beta1CropHintsAnnotationOut": "_vision_311_GoogleCloudVisionV1p4beta1CropHintsAnnotationOut",
        "FeatureIn": "_vision_312_FeatureIn",
        "FeatureOut": "_vision_313_FeatureOut",
        "GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn": "_vision_314_GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn",
        "GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut": "_vision_315_GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut",
        "PageIn": "_vision_316_PageIn",
        "PageOut": "_vision_317_PageOut",
        "StatusIn": "_vision_318_StatusIn",
        "StatusOut": "_vision_319_StatusOut",
        "GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn": "_vision_320_GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn",
        "GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut": "_vision_321_GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut",
        "GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn": "_vision_322_GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut": "_vision_323_GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut",
        "DominantColorsAnnotationIn": "_vision_324_DominantColorsAnnotationIn",
        "DominantColorsAnnotationOut": "_vision_325_DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p2beta1VertexIn": "_vision_326_GoogleCloudVisionV1p2beta1VertexIn",
        "GoogleCloudVisionV1p2beta1VertexOut": "_vision_327_GoogleCloudVisionV1p2beta1VertexOut",
        "GoogleCloudVisionV1p1beta1OperationMetadataIn": "_vision_328_GoogleCloudVisionV1p1beta1OperationMetadataIn",
        "GoogleCloudVisionV1p1beta1OperationMetadataOut": "_vision_329_GoogleCloudVisionV1p1beta1OperationMetadataOut",
        "GoogleCloudVisionV1p4beta1ImageAnnotationContextIn": "_vision_330_GoogleCloudVisionV1p4beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p4beta1ImageAnnotationContextOut": "_vision_331_GoogleCloudVisionV1p4beta1ImageAnnotationContextOut",
        "ObjectAnnotationIn": "_vision_332_ObjectAnnotationIn",
        "ObjectAnnotationOut": "_vision_333_ObjectAnnotationOut",
        "GoogleCloudVisionV1p4beta1InputConfigIn": "_vision_334_GoogleCloudVisionV1p4beta1InputConfigIn",
        "GoogleCloudVisionV1p4beta1InputConfigOut": "_vision_335_GoogleCloudVisionV1p4beta1InputConfigOut",
        "GoogleCloudVisionV1p4beta1ProductKeyValueIn": "_vision_336_GoogleCloudVisionV1p4beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p4beta1ProductKeyValueOut": "_vision_337_GoogleCloudVisionV1p4beta1ProductKeyValueOut",
        "GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn": "_vision_338_GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut": "_vision_339_GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut",
        "ColorInfoIn": "_vision_340_ColorInfoIn",
        "ColorInfoOut": "_vision_341_ColorInfoOut",
        "BatchOperationMetadataIn": "_vision_342_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_vision_343_BatchOperationMetadataOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn": "_vision_344_GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut": "_vision_345_GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut",
        "BlockIn": "_vision_346_BlockIn",
        "BlockOut": "_vision_347_BlockOut",
        "GoogleCloudVisionV1p1beta1PageIn": "_vision_348_GoogleCloudVisionV1p1beta1PageIn",
        "GoogleCloudVisionV1p1beta1PageOut": "_vision_349_GoogleCloudVisionV1p1beta1PageOut",
        "VertexIn": "_vision_350_VertexIn",
        "VertexOut": "_vision_351_VertexOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebPageIn": "_vision_352_GoogleCloudVisionV1p3beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebPageOut": "_vision_353_GoogleCloudVisionV1p3beta1WebDetectionWebPageOut",
        "GoogleCloudVisionV1p1beta1VertexIn": "_vision_354_GoogleCloudVisionV1p1beta1VertexIn",
        "GoogleCloudVisionV1p1beta1VertexOut": "_vision_355_GoogleCloudVisionV1p1beta1VertexOut",
        "GoogleCloudVisionV1p1beta1ImageAnnotationContextIn": "_vision_356_GoogleCloudVisionV1p1beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p1beta1ImageAnnotationContextOut": "_vision_357_GoogleCloudVisionV1p1beta1ImageAnnotationContextOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationIn": "_vision_358_GoogleCloudVisionV1p1beta1TextAnnotationIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationOut": "_vision_359_GoogleCloudVisionV1p1beta1TextAnnotationOut",
        "GoogleCloudVisionV1p4beta1GcsDestinationIn": "_vision_360_GoogleCloudVisionV1p4beta1GcsDestinationIn",
        "GoogleCloudVisionV1p4beta1GcsDestinationOut": "_vision_361_GoogleCloudVisionV1p4beta1GcsDestinationOut",
        "TextAnnotationIn": "_vision_362_TextAnnotationIn",
        "TextAnnotationOut": "_vision_363_TextAnnotationOut",
        "GoogleCloudVisionV1p1beta1ProductIn": "_vision_364_GoogleCloudVisionV1p1beta1ProductIn",
        "GoogleCloudVisionV1p1beta1ProductOut": "_vision_365_GoogleCloudVisionV1p1beta1ProductOut",
        "GoogleCloudVisionV1p1beta1PropertyIn": "_vision_366_GoogleCloudVisionV1p1beta1PropertyIn",
        "GoogleCloudVisionV1p1beta1PropertyOut": "_vision_367_GoogleCloudVisionV1p1beta1PropertyOut",
        "ImageAnnotationContextIn": "_vision_368_ImageAnnotationContextIn",
        "ImageAnnotationContextOut": "_vision_369_ImageAnnotationContextOut",
        "GoogleCloudVisionV1p3beta1ParagraphIn": "_vision_370_GoogleCloudVisionV1p3beta1ParagraphIn",
        "GoogleCloudVisionV1p3beta1ParagraphOut": "_vision_371_GoogleCloudVisionV1p3beta1ParagraphOut",
        "GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn": "_vision_372_GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut": "_vision_373_GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn": "_vision_374_GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut": "_vision_375_GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut",
        "GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn": "_vision_376_GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut": "_vision_377_GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut",
        "BoundingPolyIn": "_vision_378_BoundingPolyIn",
        "BoundingPolyOut": "_vision_379_BoundingPolyOut",
        "GoogleCloudVisionV1p1beta1WebDetectionIn": "_vision_380_GoogleCloudVisionV1p1beta1WebDetectionIn",
        "GoogleCloudVisionV1p1beta1WebDetectionOut": "_vision_381_GoogleCloudVisionV1p1beta1WebDetectionOut",
        "GoogleCloudVisionV1p3beta1GcsDestinationIn": "_vision_382_GoogleCloudVisionV1p3beta1GcsDestinationIn",
        "GoogleCloudVisionV1p3beta1GcsDestinationOut": "_vision_383_GoogleCloudVisionV1p3beta1GcsDestinationOut",
        "LocationInfoIn": "_vision_384_LocationInfoIn",
        "LocationInfoOut": "_vision_385_LocationInfoOut",
        "KeyValueIn": "_vision_386_KeyValueIn",
        "KeyValueOut": "_vision_387_KeyValueOut",
        "AnnotateFileResponseIn": "_vision_388_AnnotateFileResponseIn",
        "AnnotateFileResponseOut": "_vision_389_AnnotateFileResponseOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn": "_vision_390_GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut": "_vision_391_GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p4beta1BlockIn": "_vision_392_GoogleCloudVisionV1p4beta1BlockIn",
        "GoogleCloudVisionV1p4beta1BlockOut": "_vision_393_GoogleCloudVisionV1p4beta1BlockOut",
        "GoogleCloudVisionV1p3beta1FaceAnnotationIn": "_vision_394_GoogleCloudVisionV1p3beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p3beta1FaceAnnotationOut": "_vision_395_GoogleCloudVisionV1p3beta1FaceAnnotationOut",
        "WordIn": "_vision_396_WordIn",
        "WordOut": "_vision_397_WordOut",
        "GoogleCloudVisionV1p4beta1AnnotateFileResponseIn": "_vision_398_GoogleCloudVisionV1p4beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p4beta1AnnotateFileResponseOut": "_vision_399_GoogleCloudVisionV1p4beta1AnnotateFileResponseOut",
        "GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseIn": "_vision_400_GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseOut": "_vision_401_GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p4beta1ReferenceImageIn": "_vision_402_GoogleCloudVisionV1p4beta1ReferenceImageIn",
        "GoogleCloudVisionV1p4beta1ReferenceImageOut": "_vision_403_GoogleCloudVisionV1p4beta1ReferenceImageOut",
        "GoogleCloudVisionV1p2beta1CropHintIn": "_vision_404_GoogleCloudVisionV1p2beta1CropHintIn",
        "GoogleCloudVisionV1p2beta1CropHintOut": "_vision_405_GoogleCloudVisionV1p2beta1CropHintOut",
        "DetectedBreakIn": "_vision_406_DetectedBreakIn",
        "DetectedBreakOut": "_vision_407_DetectedBreakOut",
        "GoogleCloudVisionV1p4beta1CelebrityIn": "_vision_408_GoogleCloudVisionV1p4beta1CelebrityIn",
        "GoogleCloudVisionV1p4beta1CelebrityOut": "_vision_409_GoogleCloudVisionV1p4beta1CelebrityOut",
        "GoogleCloudVisionV1p3beta1WordIn": "_vision_410_GoogleCloudVisionV1p3beta1WordIn",
        "GoogleCloudVisionV1p3beta1WordOut": "_vision_411_GoogleCloudVisionV1p3beta1WordOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn": "_vision_412_GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut": "_vision_413_GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut",
        "GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn": "_vision_414_GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut": "_vision_415_GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn": "_vision_416_GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut": "_vision_417_GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn": "_vision_418_GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut": "_vision_419_GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p2beta1PageIn": "_vision_420_GoogleCloudVisionV1p2beta1PageIn",
        "GoogleCloudVisionV1p2beta1PageOut": "_vision_421_GoogleCloudVisionV1p2beta1PageOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebPageIn": "_vision_422_GoogleCloudVisionV1p2beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebPageOut": "_vision_423_GoogleCloudVisionV1p2beta1WebDetectionWebPageOut",
        "GoogleCloudVisionV1p2beta1ParagraphIn": "_vision_424_GoogleCloudVisionV1p2beta1ParagraphIn",
        "GoogleCloudVisionV1p2beta1ParagraphOut": "_vision_425_GoogleCloudVisionV1p2beta1ParagraphOut",
        "SafeSearchAnnotationIn": "_vision_426_SafeSearchAnnotationIn",
        "SafeSearchAnnotationOut": "_vision_427_SafeSearchAnnotationOut",
        "ImportProductSetsResponseIn": "_vision_428_ImportProductSetsResponseIn",
        "ImportProductSetsResponseOut": "_vision_429_ImportProductSetsResponseOut",
        "GoogleCloudVisionV1p4beta1WordIn": "_vision_430_GoogleCloudVisionV1p4beta1WordIn",
        "GoogleCloudVisionV1p4beta1WordOut": "_vision_431_GoogleCloudVisionV1p4beta1WordOut",
        "GoogleCloudVisionV1p3beta1OutputConfigIn": "_vision_432_GoogleCloudVisionV1p3beta1OutputConfigIn",
        "GoogleCloudVisionV1p3beta1OutputConfigOut": "_vision_433_GoogleCloudVisionV1p3beta1OutputConfigOut",
        "GoogleCloudVisionV1p4beta1AnnotateImageResponseIn": "_vision_434_GoogleCloudVisionV1p4beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p4beta1AnnotateImageResponseOut": "_vision_435_GoogleCloudVisionV1p4beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p1beta1CropHintIn": "_vision_436_GoogleCloudVisionV1p1beta1CropHintIn",
        "GoogleCloudVisionV1p1beta1CropHintOut": "_vision_437_GoogleCloudVisionV1p1beta1CropHintOut",
        "GoogleCloudVisionV1p3beta1NormalizedVertexIn": "_vision_438_GoogleCloudVisionV1p3beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p3beta1NormalizedVertexOut": "_vision_439_GoogleCloudVisionV1p3beta1NormalizedVertexOut",
        "GoogleCloudVisionV1p1beta1NormalizedVertexIn": "_vision_440_GoogleCloudVisionV1p1beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p1beta1NormalizedVertexOut": "_vision_441_GoogleCloudVisionV1p1beta1NormalizedVertexOut",
        "AsyncBatchAnnotateImagesResponseIn": "_vision_442_AsyncBatchAnnotateImagesResponseIn",
        "AsyncBatchAnnotateImagesResponseOut": "_vision_443_AsyncBatchAnnotateImagesResponseOut",
        "GoogleCloudVisionV1p3beta1PropertyIn": "_vision_444_GoogleCloudVisionV1p3beta1PropertyIn",
        "GoogleCloudVisionV1p3beta1PropertyOut": "_vision_445_GoogleCloudVisionV1p3beta1PropertyOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn": "_vision_446_GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut": "_vision_447_GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebPageIn": "_vision_448_GoogleCloudVisionV1p1beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebPageOut": "_vision_449_GoogleCloudVisionV1p1beta1WebDetectionWebPageOut",
        "GoogleCloudVisionV1p4beta1SymbolIn": "_vision_450_GoogleCloudVisionV1p4beta1SymbolIn",
        "GoogleCloudVisionV1p4beta1SymbolOut": "_vision_451_GoogleCloudVisionV1p4beta1SymbolOut",
        "ImportProductSetsGcsSourceIn": "_vision_452_ImportProductSetsGcsSourceIn",
        "ImportProductSetsGcsSourceOut": "_vision_453_ImportProductSetsGcsSourceOut",
        "PurgeProductsRequestIn": "_vision_454_PurgeProductsRequestIn",
        "PurgeProductsRequestOut": "_vision_455_PurgeProductsRequestOut",
        "WebPageIn": "_vision_456_WebPageIn",
        "WebPageOut": "_vision_457_WebPageOut",
        "SymbolIn": "_vision_458_SymbolIn",
        "SymbolOut": "_vision_459_SymbolOut",
        "GoogleCloudVisionV1p2beta1AnnotateFileResponseIn": "_vision_460_GoogleCloudVisionV1p2beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p2beta1AnnotateFileResponseOut": "_vision_461_GoogleCloudVisionV1p2beta1AnnotateFileResponseOut",
        "ListReferenceImagesResponseIn": "_vision_462_ListReferenceImagesResponseIn",
        "ListReferenceImagesResponseOut": "_vision_463_ListReferenceImagesResponseOut",
        "CropHintsParamsIn": "_vision_464_CropHintsParamsIn",
        "CropHintsParamsOut": "_vision_465_CropHintsParamsOut",
        "GoogleCloudVisionV1p2beta1GcsSourceIn": "_vision_466_GoogleCloudVisionV1p2beta1GcsSourceIn",
        "GoogleCloudVisionV1p2beta1GcsSourceOut": "_vision_467_GoogleCloudVisionV1p2beta1GcsSourceOut",
        "GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn": "_vision_468_GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut": "_vision_469_GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p2beta1ProductIn": "_vision_470_GoogleCloudVisionV1p2beta1ProductIn",
        "GoogleCloudVisionV1p2beta1ProductOut": "_vision_471_GoogleCloudVisionV1p2beta1ProductOut",
        "ProductSetIn": "_vision_472_ProductSetIn",
        "ProductSetOut": "_vision_473_ProductSetOut",
        "GoogleCloudVisionV1p2beta1ColorInfoIn": "_vision_474_GoogleCloudVisionV1p2beta1ColorInfoIn",
        "GoogleCloudVisionV1p2beta1ColorInfoOut": "_vision_475_GoogleCloudVisionV1p2beta1ColorInfoOut",
        "GoogleCloudVisionV1p1beta1InputConfigIn": "_vision_476_GoogleCloudVisionV1p1beta1InputConfigIn",
        "GoogleCloudVisionV1p1beta1InputConfigOut": "_vision_477_GoogleCloudVisionV1p1beta1InputConfigOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn": "_vision_478_GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut": "_vision_479_GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p4beta1OutputConfigIn": "_vision_480_GoogleCloudVisionV1p4beta1OutputConfigIn",
        "GoogleCloudVisionV1p4beta1OutputConfigOut": "_vision_481_GoogleCloudVisionV1p4beta1OutputConfigOut",
        "ParagraphIn": "_vision_482_ParagraphIn",
        "ParagraphOut": "_vision_483_ParagraphOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn": "_vision_484_GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut": "_vision_485_GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut",
        "ProductSetPurgeConfigIn": "_vision_486_ProductSetPurgeConfigIn",
        "ProductSetPurgeConfigOut": "_vision_487_ProductSetPurgeConfigOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationIn": "_vision_488_GoogleCloudVisionV1p2beta1TextAnnotationIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationOut": "_vision_489_GoogleCloudVisionV1p2beta1TextAnnotationOut",
        "GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseIn": "_vision_490_GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseOut": "_vision_491_GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p2beta1CropHintsAnnotationIn": "_vision_492_GoogleCloudVisionV1p2beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p2beta1CropHintsAnnotationOut": "_vision_493_GoogleCloudVisionV1p2beta1CropHintsAnnotationOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn": "_vision_494_GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut": "_vision_495_GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p2beta1OperationMetadataIn": "_vision_496_GoogleCloudVisionV1p2beta1OperationMetadataIn",
        "GoogleCloudVisionV1p2beta1OperationMetadataOut": "_vision_497_GoogleCloudVisionV1p2beta1OperationMetadataOut",
        "GoogleCloudVisionV1p4beta1CropHintIn": "_vision_498_GoogleCloudVisionV1p4beta1CropHintIn",
        "GoogleCloudVisionV1p4beta1CropHintOut": "_vision_499_GoogleCloudVisionV1p4beta1CropHintOut",
        "GoogleCloudVisionV1p3beta1InputConfigIn": "_vision_500_GoogleCloudVisionV1p3beta1InputConfigIn",
        "GoogleCloudVisionV1p3beta1InputConfigOut": "_vision_501_GoogleCloudVisionV1p3beta1InputConfigOut",
        "DetectedLanguageIn": "_vision_502_DetectedLanguageIn",
        "DetectedLanguageOut": "_vision_503_DetectedLanguageOut",
        "AsyncAnnotateFileRequestIn": "_vision_504_AsyncAnnotateFileRequestIn",
        "AsyncAnnotateFileRequestOut": "_vision_505_AsyncAnnotateFileRequestOut",
        "GoogleCloudVisionV1p4beta1PageIn": "_vision_506_GoogleCloudVisionV1p4beta1PageIn",
        "GoogleCloudVisionV1p4beta1PageOut": "_vision_507_GoogleCloudVisionV1p4beta1PageOut",
        "GroupedResultIn": "_vision_508_GroupedResultIn",
        "GroupedResultOut": "_vision_509_GroupedResultOut",
        "GoogleCloudVisionV1p3beta1BatchOperationMetadataIn": "_vision_510_GoogleCloudVisionV1p3beta1BatchOperationMetadataIn",
        "GoogleCloudVisionV1p3beta1BatchOperationMetadataOut": "_vision_511_GoogleCloudVisionV1p3beta1BatchOperationMetadataOut",
        "GoogleCloudVisionV1p3beta1ProductIn": "_vision_512_GoogleCloudVisionV1p3beta1ProductIn",
        "GoogleCloudVisionV1p3beta1ProductOut": "_vision_513_GoogleCloudVisionV1p3beta1ProductOut",
        "GoogleCloudVisionV1p2beta1GcsDestinationIn": "_vision_514_GoogleCloudVisionV1p2beta1GcsDestinationIn",
        "GoogleCloudVisionV1p2beta1GcsDestinationOut": "_vision_515_GoogleCloudVisionV1p2beta1GcsDestinationOut",
        "GoogleCloudVisionV1p3beta1SymbolIn": "_vision_516_GoogleCloudVisionV1p3beta1SymbolIn",
        "GoogleCloudVisionV1p3beta1SymbolOut": "_vision_517_GoogleCloudVisionV1p3beta1SymbolOut",
        "GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn": "_vision_518_GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut": "_vision_519_GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p1beta1AnnotateFileResponseIn": "_vision_520_GoogleCloudVisionV1p1beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p1beta1AnnotateFileResponseOut": "_vision_521_GoogleCloudVisionV1p1beta1AnnotateFileResponseOut",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseIn": "_vision_522_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseOut": "_vision_523_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn": "_vision_524_GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut": "_vision_525_GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut",
        "GoogleCloudVisionV1p4beta1BoundingPolyIn": "_vision_526_GoogleCloudVisionV1p4beta1BoundingPolyIn",
        "GoogleCloudVisionV1p4beta1BoundingPolyOut": "_vision_527_GoogleCloudVisionV1p4beta1BoundingPolyOut",
        "GoogleCloudVisionV1p4beta1BatchOperationMetadataIn": "_vision_528_GoogleCloudVisionV1p4beta1BatchOperationMetadataIn",
        "GoogleCloudVisionV1p4beta1BatchOperationMetadataOut": "_vision_529_GoogleCloudVisionV1p4beta1BatchOperationMetadataOut",
        "OperationIn": "_vision_530_OperationIn",
        "OperationOut": "_vision_531_OperationOut",
        "GoogleCloudVisionV1p1beta1ColorInfoIn": "_vision_532_GoogleCloudVisionV1p1beta1ColorInfoIn",
        "GoogleCloudVisionV1p1beta1ColorInfoOut": "_vision_533_GoogleCloudVisionV1p1beta1ColorInfoOut",
        "GoogleCloudVisionV1p2beta1ImagePropertiesIn": "_vision_534_GoogleCloudVisionV1p2beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p2beta1ImagePropertiesOut": "_vision_535_GoogleCloudVisionV1p2beta1ImagePropertiesOut",
        "GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn": "_vision_536_GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut": "_vision_537_GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut",
        "BatchAnnotateImagesRequestIn": "_vision_538_BatchAnnotateImagesRequestIn",
        "BatchAnnotateImagesRequestOut": "_vision_539_BatchAnnotateImagesRequestOut",
        "WebDetectionParamsIn": "_vision_540_WebDetectionParamsIn",
        "WebDetectionParamsOut": "_vision_541_WebDetectionParamsOut",
        "GoogleCloudVisionV1p4beta1ProductIn": "_vision_542_GoogleCloudVisionV1p4beta1ProductIn",
        "GoogleCloudVisionV1p4beta1ProductOut": "_vision_543_GoogleCloudVisionV1p4beta1ProductOut",
        "AddProductToProductSetRequestIn": "_vision_544_AddProductToProductSetRequestIn",
        "AddProductToProductSetRequestOut": "_vision_545_AddProductToProductSetRequestOut",
        "GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn": "_vision_546_GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut": "_vision_547_GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p1beta1PositionIn": "_vision_548_GoogleCloudVisionV1p1beta1PositionIn",
        "GoogleCloudVisionV1p1beta1PositionOut": "_vision_549_GoogleCloudVisionV1p1beta1PositionOut",
        "LatLngIn": "_vision_550_LatLngIn",
        "LatLngOut": "_vision_551_LatLngOut",
        "ListProductsResponseIn": "_vision_552_ListProductsResponseIn",
        "ListProductsResponseOut": "_vision_553_ListProductsResponseOut",
        "GoogleCloudVisionV1p3beta1EntityAnnotationIn": "_vision_554_GoogleCloudVisionV1p3beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p3beta1EntityAnnotationOut": "_vision_555_GoogleCloudVisionV1p3beta1EntityAnnotationOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebImageIn": "_vision_556_GoogleCloudVisionV1p2beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebImageOut": "_vision_557_GoogleCloudVisionV1p2beta1WebDetectionWebImageOut",
        "GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn": "_vision_558_GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut": "_vision_559_GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationIn": "_vision_560_GoogleCloudVisionV1p3beta1TextAnnotationIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationOut": "_vision_561_GoogleCloudVisionV1p3beta1TextAnnotationOut",
        "GoogleCloudVisionV1p3beta1GcsSourceIn": "_vision_562_GoogleCloudVisionV1p3beta1GcsSourceIn",
        "GoogleCloudVisionV1p3beta1GcsSourceOut": "_vision_563_GoogleCloudVisionV1p3beta1GcsSourceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudVisionV1p3beta1BoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1VertexIn"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1NormalizedVertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"])
    types["GoogleCloudVisionV1p3beta1BoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1VertexOut"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"])
    types["GoogleCloudVisionV1p3beta1PageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BlockIn"])
            ).optional(),
            "width": t.integer().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PageIn"])
    types["GoogleCloudVisionV1p3beta1PageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BlockOut"])
            ).optional(),
            "width": t.integer().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PageOut"])
    types["GoogleCloudVisionV1p3beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p3beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocationInfoOut"])
    types["AnnotateImageResponseIn"] = t.struct(
        {
            "context": t.proxy(renames["ImageAnnotationContextIn"]).optional(),
            "cropHintsAnnotation": t.proxy(renames["CropHintsAnnotationIn"]).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["SafeSearchAnnotationIn"]
            ).optional(),
            "webDetection": t.proxy(renames["WebDetectionIn"]).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["ImagePropertiesIn"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(renames["LocalizedObjectAnnotationIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "productSearchResults": t.proxy(
                renames["ProductSearchResultsIn"]
            ).optional(),
            "faceAnnotations": t.array(t.proxy(renames["FaceAnnotationIn"])).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "fullTextAnnotation": t.proxy(renames["TextAnnotationIn"]).optional(),
        }
    ).named(renames["AnnotateImageResponseIn"])
    types["AnnotateImageResponseOut"] = t.struct(
        {
            "context": t.proxy(renames["ImageAnnotationContextOut"]).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["CropHintsAnnotationOut"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["SafeSearchAnnotationOut"]
            ).optional(),
            "webDetection": t.proxy(renames["WebDetectionOut"]).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["ImagePropertiesOut"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(renames["LocalizedObjectAnnotationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "productSearchResults": t.proxy(
                renames["ProductSearchResultsOut"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["FaceAnnotationOut"])
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "fullTextAnnotation": t.proxy(renames["TextAnnotationOut"]).optional(),
        }
    ).named(renames["AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p2beta1InputConfigIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsSourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1InputConfigIn"])
    types["GoogleCloudVisionV1p2beta1InputConfigOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1InputConfigOut"])
    types["BatchAnnotateImagesResponseIn"] = t.struct(
        {"responses": t.array(t.proxy(renames["AnnotateImageResponseIn"])).optional()}
    ).named(renames["BatchAnnotateImagesResponseIn"])
    types["BatchAnnotateImagesResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["AnnotateImageResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchAnnotateImagesResponseOut"])
    types["GoogleCloudVisionV1p2beta1OutputConfigIn"] = t.struct(
        {
            "batchSize": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1OutputConfigIn"])
    types["GoogleCloudVisionV1p2beta1OutputConfigOut"] = t.struct(
        {
            "batchSize": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1OutputConfigOut"])
    types["GoogleCloudVisionV1p1beta1ProductKeyValueIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1ProductKeyValueIn"])
    types["GoogleCloudVisionV1p1beta1ProductKeyValueOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductKeyValueOut"])
    types["ImageSourceIn"] = t.struct(
        {"imageUri": t.string().optional(), "gcsImageUri": t.string().optional()}
    ).named(renames["ImageSourceIn"])
    types["ImageSourceOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "gcsImageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageSourceOut"])
    types["GoogleCloudVisionV1p1beta1OutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p1beta1GcsDestinationIn"]
            ).optional(),
            "batchSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1OutputConfigIn"])
    types["GoogleCloudVisionV1p1beta1OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p1beta1GcsDestinationOut"]
            ).optional(),
            "batchSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1OutputConfigOut"])
    types["ProductSearchParamsIn"] = t.struct(
        {
            "productCategories": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "productSet": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
        }
    ).named(renames["ProductSearchParamsIn"])
    types["ProductSearchParamsOut"] = t.struct(
        {
            "productCategories": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "productSet": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSearchParamsOut"])
    types["GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn"] = t.struct(
        {
            "colors": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ColorInfoIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut"] = t.struct(
        {
            "colors": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ColorInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut"])
    types[
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut"]
    )
    types["GoogleCloudVisionV1p3beta1WebDetectionIn"] = t.struct(
        {
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionOut"] = t.struct(
        {
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionOut"])
    types["GoogleCloudVisionV1p3beta1AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "totalPages": t.integer().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p3beta1InputConfigIn"]
            ).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p3beta1AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "totalPages": t.integer().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p3beta1InputConfigOut"]
            ).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p3beta1CropHintsAnnotationIn"] = t.struct(
        {
            "cropHints": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1CropHintIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p3beta1CropHintsAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1CropHintsAnnotationOut"] = t.struct(
        {
            "cropHints": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1CropHintOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1CropHintsAnnotationOut"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsIn"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "indexTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsOut"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsOut"])
    types["WebEntityIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "description": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["WebEntityIn"])
    types["WebEntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "description": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebEntityOut"])
    types["GoogleCloudVisionV1p4beta1ParagraphIn"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WordIn"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ParagraphIn"])
    types["GoogleCloudVisionV1p4beta1ParagraphOut"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WordOut"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ParagraphOut"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsOut"])
    types["CropHintIn"] = t.struct(
        {
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
        }
    ).named(renames["CropHintIn"])
    types["CropHintOut"] = t.struct(
        {
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropHintOut"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn"
                    ]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut"
                    ]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut"])
    types["GoogleCloudVisionV1p3beta1OperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p3beta1OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1OperationMetadataOut"])
    types["GoogleCloudVisionV1p3beta1ImageAnnotationContextIn"] = t.struct(
        {"pageNumber": t.integer().optional(), "uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextIn"])
    types["GoogleCloudVisionV1p3beta1ImageAnnotationContextOut"] = t.struct(
        {
            "pageNumber": t.integer().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextOut"])
    types["OutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
            "batchSize": t.integer().optional(),
        }
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "batchSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1FaceRecognitionResultIn"] = t.struct(
        {
            "celebrity": t.proxy(
                renames["GoogleCloudVisionV1p4beta1CelebrityIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceRecognitionResultIn"])
    types["GoogleCloudVisionV1p4beta1FaceRecognitionResultOut"] = t.struct(
        {
            "celebrity": t.proxy(
                renames["GoogleCloudVisionV1p4beta1CelebrityOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceRecognitionResultOut"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"
                    ]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"
                    ]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut"])
    types["GoogleCloudVisionV1p1beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p1beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1GcsSourceOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["AnnotateFileRequestIn"] = t.struct(
        {
            "features": t.array(t.proxy(renames["FeatureIn"])),
            "pages": t.array(t.integer()).optional(),
            "inputConfig": t.proxy(renames["InputConfigIn"]),
            "imageContext": t.proxy(renames["ImageContextIn"]).optional(),
        }
    ).named(renames["AnnotateFileRequestIn"])
    types["AnnotateFileRequestOut"] = t.struct(
        {
            "features": t.array(t.proxy(renames["FeatureOut"])),
            "pages": t.array(t.integer()).optional(),
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "imageContext": t.proxy(renames["ImageContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateFileRequestOut"])
    types["GoogleCloudVisionV1p4beta1NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1NormalizedVertexIn"])
    types["GoogleCloudVisionV1p4beta1NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1NormalizedVertexOut"])
    types["GoogleCloudVisionV1p2beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p2beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocationInfoOut"])
    types["GoogleCloudVisionV1p2beta1ProductKeyValueIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1ProductKeyValueIn"])
    types["GoogleCloudVisionV1p2beta1ProductKeyValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductKeyValueOut"])
    types["GoogleCloudVisionV1p1beta1ImagePropertiesIn"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ImagePropertiesIn"])
    types["GoogleCloudVisionV1p1beta1ImagePropertiesOut"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ImagePropertiesOut"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationIn"] = t.struct(
        {
            "detectionConfidence": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "panAngle": t.number().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "angerLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "rollAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationOut"] = t.struct(
        {
            "detectionConfidence": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "panAngle": t.number().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "angerLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "rollAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationOut"])
    types["LocalizedObjectAnnotationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
        }
    ).named(renames["LocalizedObjectAnnotationIn"])
    types["LocalizedObjectAnnotationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedObjectAnnotationOut"])
    types["ImagePropertiesIn"] = t.struct(
        {"dominantColors": t.proxy(renames["DominantColorsAnnotationIn"]).optional()}
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["DominantColorsAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"] = t.struct(
        {"score": t.number().optional(), "url": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"] = t.struct(
        {
            "score": t.number().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
    types["GoogleCloudVisionV1p1beta1EntityAnnotationIn"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PropertyIn"])
            ).optional(),
            "score": t.number().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "description": t.string().optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1LocationInfoIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1EntityAnnotationOut"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PropertyOut"])
            ).optional(),
            "score": t.number().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "description": t.string().optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1LocationInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"] = t.struct(
        {"url": t.string().optional(), "score": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
    types["WebDetectionIn"] = t.struct(
        {
            "visuallySimilarImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "bestGuessLabels": t.array(t.proxy(renames["WebLabelIn"])).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["WebPageIn"])
            ).optional(),
            "webEntities": t.array(t.proxy(renames["WebEntityIn"])).optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "partialMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
        }
    ).named(renames["WebDetectionIn"])
    types["WebDetectionOut"] = t.struct(
        {
            "visuallySimilarImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "bestGuessLabels": t.array(t.proxy(renames["WebLabelOut"])).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["WebPageOut"])
            ).optional(),
            "webEntities": t.array(t.proxy(renames["WebEntityOut"])).optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageOut"])).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebDetectionOut"])
    types["GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseIn"])
    types["GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseOut"])
    types["ColorIn"] = t.struct(
        {
            "green": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "green": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn"] = t.struct(
        {
            "colors": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ColorInfoIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut"] = t.struct(
        {
            "colors": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ColorInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1ColorInfoIn"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p4beta1ColorInfoOut"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ColorInfoOut"])
    types["GoogleCloudVisionV1p3beta1BlockIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ParagraphIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "blockType": t.string().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BlockIn"])
    types["GoogleCloudVisionV1p3beta1BlockOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ParagraphOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "blockType": t.string().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BlockOut"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn"] = t.struct(
        {"type": t.string().optional(), "isPrefix": t.boolean().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "isPrefix": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut"])
    types["GoogleCloudVisionV1p3beta1CropHintIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1CropHintIn"])
    types["GoogleCloudVisionV1p3beta1CropHintOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1CropHintOut"])
    types[
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"]
    )
    types["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"] = t.struct(
        {
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductSearchResultsIn"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImagePropertiesIn"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1CropHintsAnnotationIn"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextIn"]
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p3beta1WebDetectionIn"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"] = t.struct(
        {
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductSearchResultsOut"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImagePropertiesOut"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1CropHintsAnnotationOut"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextOut"]
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p3beta1WebDetectionOut"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn"] = t.struct(
        {
            "position": t.proxy(
                renames["GoogleCloudVisionV1p2beta1PositionIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut"] = t.struct(
        {
            "position": t.proxy(
                renames["GoogleCloudVisionV1p2beta1PositionOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn"] = t.struct(
        {"languageCode": t.string().optional(), "label": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut"])
    types["GoogleCloudVisionV1p2beta1SymbolIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "text": t.string().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SymbolIn"])
    types["GoogleCloudVisionV1p2beta1SymbolOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "text": t.string().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SymbolOut"])
    types["BatchAnnotateFilesRequestIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "requests": t.array(t.proxy(renames["AnnotateFileRequestIn"])),
        }
    ).named(renames["BatchAnnotateFilesRequestIn"])
    types["BatchAnnotateFilesRequestOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "requests": t.array(t.proxy(renames["AnnotateFileRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchAnnotateFilesRequestOut"])
    types["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudVisionV1p3beta1PositionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn"])
    types["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudVisionV1p3beta1PositionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn"] = t.struct(
        {"confidence": t.number().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut"])
    types["GoogleCloudVisionV1p1beta1ParagraphIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WordIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ParagraphIn"])
    types["GoogleCloudVisionV1p1beta1ParagraphOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ParagraphOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionIn"] = t.struct(
        {
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionOut"] = t.struct(
        {
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionOut"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn"] = t.struct(
        {"isPrefix": t.boolean().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut"] = t.struct(
        {
            "isPrefix": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut"])
    types["GoogleCloudVisionV1p1beta1BlockIn"] = t.struct(
        {
            "blockType": t.string().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ParagraphIn"])
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1BlockIn"])
    types["GoogleCloudVisionV1p1beta1BlockOut"] = t.struct(
        {
            "blockType": t.string().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ParagraphOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1BlockOut"])
    types["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "medical": t.string().optional(),
            "violence": t.string().optional(),
            "adult": t.string().optional(),
            "spoof": t.string().optional(),
            "racy": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "medical": t.string().optional(),
            "violence": t.string().optional(),
            "adult": t.string().optional(),
            "spoof": t.string().optional(),
            "racy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1EntityAnnotationIn"] = t.struct(
        {
            "description": t.string().optional(),
            "topicality": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1LocationInfoIn"])
            ).optional(),
            "mid": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PropertyIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "locale": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1EntityAnnotationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "topicality": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1LocationInfoOut"])
            ).optional(),
            "mid": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PropertyOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "locale": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseIn"])
    types["GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseOut"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"] = t.struct(
        {
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"] = t.struct(
        {
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"])
    types["ListProductsInProductSetResponseIn"] = t.struct(
        {
            "products": t.array(t.proxy(renames["ProductIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProductsInProductSetResponseIn"])
    types["ListProductsInProductSetResponseOut"] = t.struct(
        {
            "products": t.array(t.proxy(renames["ProductOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductsInProductSetResponseOut"])
    types["GoogleCloudVisionV1p2beta1PropertyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PropertyIn"])
    types["GoogleCloudVisionV1p2beta1PropertyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PropertyOut"])
    types["GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1OutputConfigIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseIn"])
    types["GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1OutputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseOut"])
    types["PropertyIn"] = t.struct(
        {
            "uint64Value": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PropertyIn"])
    types["PropertyOut"] = t.struct(
        {
            "uint64Value": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyOut"])
    types["AsyncBatchAnnotateImagesRequestIn"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
            "parent": t.string().optional(),
        }
    ).named(renames["AsyncBatchAnnotateImagesRequestIn"])
    types["AsyncBatchAnnotateImagesRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "requests": t.array(t.proxy(renames["AnnotateImageRequestOut"])),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateImagesRequestOut"])
    types["GoogleCloudVisionV1p1beta1WordIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1SymbolIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WordIn"])
    types["GoogleCloudVisionV1p1beta1WordOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1SymbolOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WordOut"])
    types["GoogleCloudVisionV1p2beta1ImageAnnotationContextIn"] = t.struct(
        {"pageNumber": t.integer().optional(), "uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextIn"])
    types["GoogleCloudVisionV1p2beta1ImageAnnotationContextOut"] = t.struct(
        {
            "pageNumber": t.integer().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextOut"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn"] = t.struct(
        {"languageCode": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebPageIn"] = t.struct(
        {
            "score": t.number().optional(),
            "url": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"] = t.struct(
        {
            "score": t.number().optional(),
            "url": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"])
    types["GoogleCloudVisionV1p2beta1WordIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1SymbolIn"])
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WordIn"])
    types["GoogleCloudVisionV1p2beta1WordOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1SymbolOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WordOut"])
    types["GoogleCloudVisionV1p1beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p1beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1GcsDestinationOut"])
    types["TextPropertyIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(renames["DetectedLanguageIn"])
            ).optional(),
            "detectedBreak": t.proxy(renames["DetectedBreakIn"]).optional(),
        }
    ).named(renames["TextPropertyIn"])
    types["TextPropertyOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(renames["DetectedLanguageOut"])
            ).optional(),
            "detectedBreak": t.proxy(renames["DetectedBreakOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPropertyOut"])
    types["GoogleCloudVisionV1p2beta1BlockIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "blockType": t.string().optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ParagraphIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BlockIn"])
    types["GoogleCloudVisionV1p2beta1BlockOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "blockType": t.string().optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ParagraphOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BlockOut"])
    types["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"] = t.struct(
        {
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p1beta1WebDetectionIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"]
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationIn"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImagePropertiesIn"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationIn"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextIn"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1CropHintsAnnotationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"] = t.struct(
        {
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p1beta1WebDetectionOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationOut"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImagePropertiesOut"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationOut"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextOut"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1CropHintsAnnotationOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn"] = t.struct(
        {"languageCode": t.string().optional(), "label": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut"])
    types["ResultIn"] = t.struct(
        {
            "product": t.proxy(renames["ProductIn"]).optional(),
            "image": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "product": t.proxy(renames["ProductOut"]).optional(),
            "image": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types[
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "mid": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut"]
    )
    types["GoogleCloudVisionV1p4beta1VertexIn"] = t.struct(
        {"x": t.integer().optional(), "y": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1VertexIn"])
    types["GoogleCloudVisionV1p4beta1VertexOut"] = t.struct(
        {
            "x": t.integer().optional(),
            "y": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1VertexOut"])
    types["WebLabelIn"] = t.struct(
        {"languageCode": t.string().optional(), "label": t.string().optional()}
    ).named(renames["WebLabelIn"])
    types["WebLabelOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebLabelOut"])
    types["InputConfigIn"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceIn"]).optional(),
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["InputConfigIn"])
    types["InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputConfigOut"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"] = t.struct(
        {
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"] = t.struct(
        {
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"])
    types["GoogleCloudVisionV1p2beta1PositionIn"] = t.struct(
        {
            "z": t.number().optional(),
            "y": t.number().optional(),
            "x": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PositionIn"])
    types["GoogleCloudVisionV1p2beta1PositionOut"] = t.struct(
        {
            "z": t.number().optional(),
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PositionOut"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn"] = t.struct(
        {"confidence": t.number().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut"])
    types["ImageIn"] = t.struct(
        {
            "content": t.string().optional(),
            "source": t.proxy(renames["ImageSourceIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "content": t.string().optional(),
            "source": t.proxy(renames["ImageSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"])
    types["ImageContextIn"] = t.struct(
        {
            "languageHints": t.array(t.string()).optional(),
            "webDetectionParams": t.proxy(renames["WebDetectionParamsIn"]).optional(),
            "productSearchParams": t.proxy(renames["ProductSearchParamsIn"]).optional(),
            "cropHintsParams": t.proxy(renames["CropHintsParamsIn"]).optional(),
            "textDetectionParams": t.proxy(renames["TextDetectionParamsIn"]).optional(),
            "latLongRect": t.proxy(renames["LatLongRectIn"]).optional(),
        }
    ).named(renames["ImageContextIn"])
    types["ImageContextOut"] = t.struct(
        {
            "languageHints": t.array(t.string()).optional(),
            "webDetectionParams": t.proxy(renames["WebDetectionParamsOut"]).optional(),
            "productSearchParams": t.proxy(
                renames["ProductSearchParamsOut"]
            ).optional(),
            "cropHintsParams": t.proxy(renames["CropHintsParamsOut"]).optional(),
            "textDetectionParams": t.proxy(
                renames["TextDetectionParamsOut"]
            ).optional(),
            "latLongRect": t.proxy(renames["LatLongRectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageContextOut"])
    types["AsyncBatchAnnotateFilesRequestIn"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["AsyncAnnotateFileRequestIn"])),
            "parent": t.string().optional(),
        }
    ).named(renames["AsyncBatchAnnotateFilesRequestIn"])
    types["AsyncBatchAnnotateFilesRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["AsyncAnnotateFileRequestOut"])),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateFilesRequestOut"])
    types["GoogleCloudVisionV1p3beta1VertexIn"] = t.struct(
        {"y": t.integer().optional(), "x": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1VertexIn"])
    types["GoogleCloudVisionV1p3beta1VertexOut"] = t.struct(
        {
            "y": t.integer().optional(),
            "x": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1VertexOut"])
    types["GoogleCloudVisionV1p3beta1ColorInfoIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "score": t.number().optional(),
            "pixelFraction": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p3beta1ColorInfoOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "score": t.number().optional(),
            "pixelFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ColorInfoOut"])
    types["ImportProductSetsRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["ImportProductSetsInputConfigIn"])}
    ).named(renames["ImportProductSetsRequestIn"])
    types["ImportProductSetsRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["ImportProductSetsInputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsRequestOut"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"] = t.struct(
        {
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"] = t.struct(
        {
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"])
    types["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1CropHintsAnnotationIn"] = t.struct(
        {
            "cropHints": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1CropHintIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p1beta1CropHintsAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1CropHintsAnnotationOut"] = t.struct(
        {
            "cropHints": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1CropHintOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1CropHintsAnnotationOut"])
    types["TextDetectionParamsIn"] = t.struct(
        {
            "enableTextDetectionConfidenceScore": t.boolean().optional(),
            "advancedOcrOptions": t.array(t.string()).optional(),
        }
    ).named(renames["TextDetectionParamsIn"])
    types["TextDetectionParamsOut"] = t.struct(
        {
            "enableTextDetectionConfidenceScore": t.boolean().optional(),
            "advancedOcrOptions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextDetectionParamsOut"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
            "indexTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"])
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
    types["GoogleCloudVisionV1p2beta1WebDetectionIn"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionOut"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionOut"])
    types["NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["NormalizedVertexIn"])
    types["NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NormalizedVertexOut"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationIn"] = t.struct(
        {
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "panAngle": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "detectionConfidence": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "joyLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "recognitionResult": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceRecognitionResultIn"])
            ).optional(),
            "surpriseLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationOut"] = t.struct(
        {
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "panAngle": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "detectionConfidence": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "joyLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "recognitionResult": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceRecognitionResultOut"])
            ).optional(),
            "surpriseLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationOut"])
    types["AsyncBatchAnnotateFilesResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["AsyncAnnotateFileResponseIn"])
            ).optional()
        }
    ).named(renames["AsyncBatchAnnotateFilesResponseIn"])
    types["AsyncBatchAnnotateFilesResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["AsyncAnnotateFileResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateFilesResponseOut"])
    types["GoogleCloudVisionV1p4beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p4beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocationInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["FaceAnnotationIn"] = t.struct(
        {
            "underExposedLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "fdBoundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "joyLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "blurredLikelihood": t.string().optional(),
            "landmarks": t.array(t.proxy(renames["LandmarkIn"])).optional(),
            "surpriseLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "panAngle": t.number().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
        }
    ).named(renames["FaceAnnotationIn"])
    types["FaceAnnotationOut"] = t.struct(
        {
            "underExposedLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "fdBoundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "joyLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "blurredLikelihood": t.string().optional(),
            "landmarks": t.array(t.proxy(renames["LandmarkOut"])).optional(),
            "surpriseLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "panAngle": t.number().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FaceAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1ImagePropertiesIn"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ImagePropertiesIn"])
    types["GoogleCloudVisionV1p4beta1ImagePropertiesOut"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ImagePropertiesOut"])
    types["GoogleCloudVisionV1p2beta1BoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1VertexIn"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1NormalizedVertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"])
    types["GoogleCloudVisionV1p2beta1BoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1VertexOut"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "image": t.string().optional(),
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "image": t.string().optional(),
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut"])
    types["GoogleCloudVisionV1p2beta1EntityAnnotationIn"] = t.struct(
        {
            "description": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1LocationInfoIn"])
            ).optional(),
            "mid": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PropertyIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "score": t.number().optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1EntityAnnotationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1LocationInfoOut"])
            ).optional(),
            "mid": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PropertyOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "score": t.number().optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsSourceOut"])
    types["GoogleCloudVisionV1p3beta1ImagePropertiesIn"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ImagePropertiesIn"])
    types["GoogleCloudVisionV1p3beta1ImagePropertiesOut"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ImagePropertiesOut"])
    types["GoogleCloudVisionV1p4beta1PropertyIn"] = t.struct(
        {
            "uint64Value": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PropertyIn"])
    types["GoogleCloudVisionV1p4beta1PropertyOut"] = t.struct(
        {
            "uint64Value": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PropertyOut"])
    types["GoogleCloudVisionV1p4beta1OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p4beta1OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OperationMetadataOut"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn"
                    ]
                )
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut"
                    ]
                )
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut"])
    types["LandmarkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
        }
    ).named(renames["LandmarkIn"])
    types["LandmarkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LandmarkOut"])
    types["ListProductSetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "productSets": t.array(t.proxy(renames["ProductSetIn"])).optional(),
        }
    ).named(renames["ListProductSetsResponseIn"])
    types["ListProductSetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "productSets": t.array(t.proxy(renames["ProductSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductSetsResponseOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut"])
    types["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudVisionV1p1beta1PositionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn"])
    types["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudVisionV1p1beta1PositionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut"])
    types["GoogleCloudVisionV1p2beta1NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1NormalizedVertexIn"])
    types["GoogleCloudVisionV1p2beta1NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1NormalizedVertexOut"])
    types["BatchAnnotateFilesResponseIn"] = t.struct(
        {"responses": t.array(t.proxy(renames["AnnotateFileResponseIn"])).optional()}
    ).named(renames["BatchAnnotateFilesResponseIn"])
    types["BatchAnnotateFilesResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["AnnotateFileResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchAnnotateFilesResponseOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"] = t.struct(
        {"url": t.string().optional(), "score": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
    types["ReferenceImageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "boundingPolys": t.array(t.proxy(renames["BoundingPolyIn"])).optional(),
            "uri": t.string(),
        }
    ).named(renames["ReferenceImageIn"])
    types["ReferenceImageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "boundingPolys": t.array(t.proxy(renames["BoundingPolyOut"])).optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceImageOut"])
    types["EntityAnnotationIn"] = t.struct(
        {
            "mid": t.string().optional(),
            "properties": t.array(t.proxy(renames["PropertyIn"])).optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "locations": t.array(t.proxy(renames["LocationInfoIn"])).optional(),
            "score": t.number().optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "confidence": t.number().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["EntityAnnotationIn"])
    types["EntityAnnotationOut"] = t.struct(
        {
            "mid": t.string().optional(),
            "properties": t.array(t.proxy(renames["PropertyOut"])).optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "locations": t.array(t.proxy(renames["LocationInfoOut"])).optional(),
            "score": t.number().optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "confidence": t.number().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityAnnotationOut"])
    types["AnnotateImageRequestIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]).optional(),
            "features": t.array(t.proxy(renames["FeatureIn"])).optional(),
            "imageContext": t.proxy(renames["ImageContextIn"]).optional(),
        }
    ).named(renames["AnnotateImageRequestIn"])
    types["AnnotateImageRequestOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "features": t.array(t.proxy(renames["FeatureOut"])).optional(),
            "imageContext": t.proxy(renames["ImageContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateImageRequestOut"])
    types["GoogleCloudVisionV1p4beta1PositionIn"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "z": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PositionIn"])
    types["GoogleCloudVisionV1p4beta1PositionOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "z": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PositionOut"])
    types["LatLongRectIn"] = t.struct(
        {
            "minLatLng": t.proxy(renames["LatLngIn"]).optional(),
            "maxLatLng": t.proxy(renames["LatLngIn"]).optional(),
        }
    ).named(renames["LatLongRectIn"])
    types["LatLongRectOut"] = t.struct(
        {
            "minLatLng": t.proxy(renames["LatLngOut"]).optional(),
            "maxLatLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLongRectOut"])
    types["ProductIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
            "productCategory": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "productLabels": t.array(t.proxy(renames["KeyValueOut"])).optional(),
            "productCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["GoogleCloudVisionV1p3beta1PositionIn"] = t.struct(
        {
            "z": t.number().optional(),
            "x": t.number().optional(),
            "y": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PositionIn"])
    types["GoogleCloudVisionV1p3beta1PositionOut"] = t.struct(
        {
            "z": t.number().optional(),
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PositionOut"])
    types["GoogleCloudVisionV1p1beta1BoundingPolyIn"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1NormalizedVertexIn"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1VertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"])
    types["GoogleCloudVisionV1p1beta1BoundingPolyOut"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1NormalizedVertexOut"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1VertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationIn"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PageIn"])
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationOut"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PageOut"])
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationOut"])
    types["ProductSearchResultsIn"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(renames["GroupedResultIn"])
            ).optional(),
            "results": t.array(t.proxy(renames["ResultIn"])).optional(),
            "indexTime": t.string().optional(),
        }
    ).named(renames["ProductSearchResultsIn"])
    types["ProductSearchResultsOut"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(renames["GroupedResultOut"])
            ).optional(),
            "results": t.array(t.proxy(renames["ResultOut"])).optional(),
            "indexTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSearchResultsOut"])
    types["GcsDestinationIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsIn"] = t.struct(
        {
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsOut"] = t.struct(
        {
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsOut"])
    types["GoogleCloudVisionV1p1beta1SymbolIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SymbolIn"])
    types["GoogleCloudVisionV1p1beta1SymbolOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SymbolOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["GoogleCloudVisionV1p1beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p1beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocationInfoOut"])
    types["AsyncAnnotateFileResponseIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"]).optional()}
    ).named(renames["AsyncAnnotateFileResponseIn"])
    types["AsyncAnnotateFileResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncAnnotateFileResponseOut"])
    types["WebImageIn"] = t.struct(
        {"url": t.string().optional(), "score": t.number().optional()}
    ).named(renames["WebImageIn"])
    types["WebImageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebImageOut"])
    types["ImportProductSetsInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportProductSetsGcsSourceIn"]).optional()}
    ).named(renames["ImportProductSetsInputConfigIn"])
    types["ImportProductSetsInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportProductSetsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsInputConfigOut"])
    types["GoogleCloudVisionV1p3beta1ProductKeyValueIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1ProductKeyValueIn"])
    types["GoogleCloudVisionV1p3beta1ProductKeyValueOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductKeyValueOut"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductIn"]
            ).optional(),
            "image": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductOut"]
            ).optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"])
    types["PositionIn"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "z": t.number().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "z": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn"] = t.struct(
        {"type": t.string().optional(), "isPrefix": t.boolean().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "isPrefix": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut"])
    types["CropHintsAnnotationIn"] = t.struct(
        {"cropHints": t.array(t.proxy(renames["CropHintIn"])).optional()}
    ).named(renames["CropHintsAnnotationIn"])
    types["CropHintsAnnotationOut"] = t.struct(
        {
            "cropHints": t.array(t.proxy(renames["CropHintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropHintsAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationIn"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextIn"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImagePropertiesIn"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationIn"]
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductSearchResultsIn"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p2beta1WebDetectionIn"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1CropHintsAnnotationIn"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationOut"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextOut"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImagePropertiesOut"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationOut"]
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductSearchResultsOut"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p2beta1WebDetectionOut"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1CropHintsAnnotationOut"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"])
    types["RemoveProductFromProductSetRequestIn"] = t.struct(
        {"product": t.string()}
    ).named(renames["RemoveProductFromProductSetRequestIn"])
    types["RemoveProductFromProductSetRequestOut"] = t.struct(
        {"product": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveProductFromProductSetRequestOut"])
    types["GoogleCloudVisionV1p1beta1FaceAnnotationIn"] = t.struct(
        {
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "joyLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "landmarkingConfidence": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "rollAngle": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "angerLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1FaceAnnotationOut"] = t.struct(
        {
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "joyLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "landmarkingConfidence": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "rollAngle": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "angerLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p4beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1GcsSourceOut"])
    types["GoogleCloudVisionV1p3beta1ReferenceImageIn"] = t.struct(
        {
            "uri": t.string(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ReferenceImageIn"])
    types["GoogleCloudVisionV1p3beta1ReferenceImageOut"] = t.struct(
        {
            "uri": t.string(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ReferenceImageOut"])
    types["GoogleCloudVisionV1p4beta1CropHintsAnnotationIn"] = t.struct(
        {
            "cropHints": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1CropHintIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CropHintsAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1CropHintsAnnotationOut"] = t.struct(
        {
            "cropHints": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1CropHintOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CropHintsAnnotationOut"])
    types["FeatureIn"] = t.struct(
        {
            "model": t.string().optional(),
            "maxResults": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["FeatureIn"])
    types["FeatureOut"] = t.struct(
        {
            "model": t.string().optional(),
            "maxResults": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureOut"])
    types["GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn"] = t.struct(
        {
            "referenceImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ReferenceImageIn"])
            ).optional(),
            "statuses": t.array(t.proxy(renames["StatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn"])
    types["GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut"] = t.struct(
        {
            "referenceImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ReferenceImageOut"])
            ).optional(),
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut"])
    types["PageIn"] = t.struct(
        {
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "confidence": t.number().optional(),
            "blocks": t.array(t.proxy(renames["BlockIn"])).optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "confidence": t.number().optional(),
            "blocks": t.array(t.proxy(renames["BlockOut"])).optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn"] = t.struct(
        {
            "referenceImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ReferenceImageIn"])
            ).optional(),
            "statuses": t.array(t.proxy(renames["StatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn"])
    types["GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut"] = t.struct(
        {
            "referenceImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ReferenceImageOut"])
            ).optional(),
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut"])
    types["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "medical": t.string().optional(),
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
            "racy": t.string().optional(),
            "violence": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "medical": t.string().optional(),
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
            "racy": t.string().optional(),
            "violence": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"])
    types["DominantColorsAnnotationIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ColorInfoIn"])).optional()}
    ).named(renames["DominantColorsAnnotationIn"])
    types["DominantColorsAnnotationOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ColorInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DominantColorsAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1VertexIn"] = t.struct(
        {"x": t.integer().optional(), "y": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1VertexIn"])
    types["GoogleCloudVisionV1p2beta1VertexOut"] = t.struct(
        {
            "x": t.integer().optional(),
            "y": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1VertexOut"])
    types["GoogleCloudVisionV1p1beta1OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p1beta1OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1OperationMetadataOut"])
    types["GoogleCloudVisionV1p4beta1ImageAnnotationContextIn"] = t.struct(
        {"pageNumber": t.integer().optional(), "uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextIn"])
    types["GoogleCloudVisionV1p4beta1ImageAnnotationContextOut"] = t.struct(
        {
            "pageNumber": t.integer().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextOut"])
    types["ObjectAnnotationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
        }
    ).named(renames["ObjectAnnotationIn"])
    types["ObjectAnnotationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1InputConfigIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p4beta1GcsSourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1InputConfigIn"])
    types["GoogleCloudVisionV1p4beta1InputConfigOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p4beta1GcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1InputConfigOut"])
    types["GoogleCloudVisionV1p4beta1ProductKeyValueIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1ProductKeyValueIn"])
    types["GoogleCloudVisionV1p4beta1ProductKeyValueOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductKeyValueOut"])
    types["GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p2beta1OutputConfigIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p2beta1OutputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut"])
    types["ColorInfoIn"] = t.struct(
        {
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "pixelFraction": t.number().optional(),
        }
    ).named(renames["ColorInfoIn"])
    types["ColorInfoOut"] = t.struct(
        {
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "pixelFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorInfoOut"])
    types["BatchOperationMetadataIn"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["BatchOperationMetadataIn"])
    types["BatchOperationMetadataOut"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOperationMetadataOut"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductIn"]
            ).optional(),
            "image": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductOut"]
            ).optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"])
    types["BlockIn"] = t.struct(
        {
            "paragraphs": t.array(t.proxy(renames["ParagraphIn"])).optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "blockType": t.string().optional(),
        }
    ).named(renames["BlockIn"])
    types["BlockOut"] = t.struct(
        {
            "paragraphs": t.array(t.proxy(renames["ParagraphOut"])).optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "blockType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlockOut"])
    types["GoogleCloudVisionV1p1beta1PageIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1BlockIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PageIn"])
    types["GoogleCloudVisionV1p1beta1PageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1BlockOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PageOut"])
    types["VertexIn"] = t.struct(
        {"y": t.integer().optional(), "x": t.integer().optional()}
    ).named(renames["VertexIn"])
    types["VertexOut"] = t.struct(
        {
            "y": t.integer().optional(),
            "x": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VertexOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebPageIn"] = t.struct(
        {
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "score": t.number().optional(),
            "pageTitle": t.string().optional(),
            "url": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebPageOut"] = t.struct(
        {
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "score": t.number().optional(),
            "pageTitle": t.string().optional(),
            "url": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageOut"])
    types["GoogleCloudVisionV1p1beta1VertexIn"] = t.struct(
        {"y": t.integer().optional(), "x": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1VertexIn"])
    types["GoogleCloudVisionV1p1beta1VertexOut"] = t.struct(
        {
            "y": t.integer().optional(),
            "x": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1VertexOut"])
    types["GoogleCloudVisionV1p1beta1ImageAnnotationContextIn"] = t.struct(
        {"uri": t.string().optional(), "pageNumber": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextIn"])
    types["GoogleCloudVisionV1p1beta1ImageAnnotationContextOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "pageNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextOut"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationIn"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PageIn"])
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationOut"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PageOut"])
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p4beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1GcsDestinationOut"])
    types["TextAnnotationIn"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["TextAnnotationIn"])
    types["TextAnnotationOut"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1ProductIn"] = t.struct(
        {
            "name": t.string().optional(),
            "productCategory": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ProductKeyValueIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductIn"])
    types["GoogleCloudVisionV1p1beta1ProductOut"] = t.struct(
        {
            "name": t.string().optional(),
            "productCategory": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ProductKeyValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductOut"])
    types["GoogleCloudVisionV1p1beta1PropertyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "uint64Value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PropertyIn"])
    types["GoogleCloudVisionV1p1beta1PropertyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "uint64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PropertyOut"])
    types["ImageAnnotationContextIn"] = t.struct(
        {"pageNumber": t.integer().optional(), "uri": t.string().optional()}
    ).named(renames["ImageAnnotationContextIn"])
    types["ImageAnnotationContextOut"] = t.struct(
        {
            "pageNumber": t.integer().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageAnnotationContextOut"])
    types["GoogleCloudVisionV1p3beta1ParagraphIn"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WordIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ParagraphIn"])
    types["GoogleCloudVisionV1p3beta1ParagraphOut"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WordOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ParagraphOut"])
    types["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn"] = t.struct(
        {"label": t.string().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut"])
    types["GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p1beta1OutputConfigIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p1beta1OutputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut"])
    types["BoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(t.proxy(renames["VertexIn"])).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["NormalizedVertexIn"])
            ).optional(),
        }
    ).named(renames["BoundingPolyIn"])
    types["BoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(t.proxy(renames["VertexOut"])).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BoundingPolyOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionIn"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionOut"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionOut"])
    types["GoogleCloudVisionV1p3beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p3beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1GcsDestinationOut"])
    types["LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["LocationInfoIn"])
    types["LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationInfoOut"])
    types["KeyValueIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
    types["AnnotateFileResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["AnnotateImageResponseIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "totalPages": t.integer().optional(),
            "inputConfig": t.proxy(renames["InputConfigIn"]).optional(),
        }
    ).named(renames["AnnotateFileResponseIn"])
    types["AnnotateFileResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["AnnotateImageResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "totalPages": t.integer().optional(),
            "inputConfig": t.proxy(renames["InputConfigOut"]).optional(),
        }
    ).named(renames["AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn"] = t.struct(
        {"languageCode": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut"])
    types["GoogleCloudVisionV1p4beta1BlockIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ParagraphIn"])
            ).optional(),
            "blockType": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BlockIn"])
    types["GoogleCloudVisionV1p4beta1BlockOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ParagraphOut"])
            ).optional(),
            "blockType": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BlockOut"])
    types["GoogleCloudVisionV1p3beta1FaceAnnotationIn"] = t.struct(
        {
            "detectionConfidence": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "landmarkingConfidence": t.number().optional(),
            "panAngle": t.number().optional(),
            "rollAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "blurredLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1FaceAnnotationOut"] = t.struct(
        {
            "detectionConfidence": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "landmarkingConfidence": t.number().optional(),
            "panAngle": t.number().optional(),
            "rollAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "blurredLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationOut"])
    types["WordIn"] = t.struct(
        {
            "symbols": t.array(t.proxy(renames["SymbolIn"])).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["WordIn"])
    types["WordOut"] = t.struct(
        {
            "symbols": t.array(t.proxy(renames["SymbolOut"])).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordOut"])
    types["GoogleCloudVisionV1p4beta1AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"])
            ).optional(),
            "totalPages": t.integer().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1InputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p4beta1AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"])
            ).optional(),
            "totalPages": t.integer().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1InputConfigOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1AnnotateFileResponseIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseIn"])
    types["GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1AnnotateFileResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseOut"])
    types["GoogleCloudVisionV1p4beta1ReferenceImageIn"] = t.struct(
        {
            "uri": t.string(),
            "name": t.string().optional(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ReferenceImageIn"])
    types["GoogleCloudVisionV1p4beta1ReferenceImageOut"] = t.struct(
        {
            "uri": t.string(),
            "name": t.string().optional(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ReferenceImageOut"])
    types["GoogleCloudVisionV1p2beta1CropHintIn"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1CropHintIn"])
    types["GoogleCloudVisionV1p2beta1CropHintOut"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1CropHintOut"])
    types["DetectedBreakIn"] = t.struct(
        {"isPrefix": t.boolean().optional(), "type": t.string().optional()}
    ).named(renames["DetectedBreakIn"])
    types["DetectedBreakOut"] = t.struct(
        {
            "isPrefix": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectedBreakOut"])
    types["GoogleCloudVisionV1p4beta1CelebrityIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CelebrityIn"])
    types["GoogleCloudVisionV1p4beta1CelebrityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CelebrityOut"])
    types["GoogleCloudVisionV1p3beta1WordIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1SymbolIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WordIn"])
    types["GoogleCloudVisionV1p3beta1WordOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1SymbolOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WordOut"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductIn"]
            ).optional(),
            "image": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductOut"]
            ).optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn"] = t.struct(
        {
            "position": t.proxy(
                renames["GoogleCloudVisionV1p4beta1PositionIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut"] = t.struct(
        {
            "position": t.proxy(
                renames["GoogleCloudVisionV1p4beta1PositionOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn"] = t.struct(
        {"isPrefix": t.boolean().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut"] = t.struct(
        {
            "isPrefix": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut"])
    types["GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn"] = t.struct(
        {
            "colors": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ColorInfoIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut"] = t.struct(
        {
            "colors": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ColorInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1PageIn"] = t.struct(
        {
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1BlockIn"])
            ).optional(),
            "width": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "height": t.integer().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PageIn"])
    types["GoogleCloudVisionV1p2beta1PageOut"] = t.struct(
        {
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1BlockOut"])
            ).optional(),
            "width": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "height": t.integer().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PageOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "score": t.number().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "score": t.number().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"])
    types["GoogleCloudVisionV1p2beta1ParagraphIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WordIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ParagraphIn"])
    types["GoogleCloudVisionV1p2beta1ParagraphOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ParagraphOut"])
    types["SafeSearchAnnotationIn"] = t.struct(
        {
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "violence": t.string().optional(),
        }
    ).named(renames["SafeSearchAnnotationIn"])
    types["SafeSearchAnnotationOut"] = t.struct(
        {
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "violence": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeSearchAnnotationOut"])
    types["ImportProductSetsResponseIn"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusIn"])).optional(),
            "referenceImages": t.array(t.proxy(renames["ReferenceImageIn"])).optional(),
        }
    ).named(renames["ImportProductSetsResponseIn"])
    types["ImportProductSetsResponseOut"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "referenceImages": t.array(
                t.proxy(renames["ReferenceImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsResponseOut"])
    types["GoogleCloudVisionV1p4beta1WordIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1SymbolIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WordIn"])
    types["GoogleCloudVisionV1p4beta1WordOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1SymbolOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WordOut"])
    types["GoogleCloudVisionV1p3beta1OutputConfigIn"] = t.struct(
        {
            "batchSize": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p3beta1GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1OutputConfigIn"])
    types["GoogleCloudVisionV1p3beta1OutputConfigOut"] = t.struct(
        {
            "batchSize": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p3beta1GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1OutputConfigOut"])
    types["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p4beta1WebDetectionIn"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextIn"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImagePropertiesIn"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductSearchResultsIn"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1CropHintsAnnotationIn"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationIn"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationIn"]
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p4beta1WebDetectionOut"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextOut"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImagePropertiesOut"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductSearchResultsOut"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1CropHintsAnnotationOut"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationOut"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationOut"]
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p1beta1CropHintIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1CropHintIn"])
    types["GoogleCloudVisionV1p1beta1CropHintOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1CropHintOut"])
    types["GoogleCloudVisionV1p3beta1NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1NormalizedVertexIn"])
    types["GoogleCloudVisionV1p3beta1NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1NormalizedVertexOut"])
    types["GoogleCloudVisionV1p1beta1NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1NormalizedVertexIn"])
    types["GoogleCloudVisionV1p1beta1NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1NormalizedVertexOut"])
    types["AsyncBatchAnnotateImagesResponseIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"]).optional()}
    ).named(renames["AsyncBatchAnnotateImagesResponseIn"])
    types["AsyncBatchAnnotateImagesResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateImagesResponseOut"])
    types["GoogleCloudVisionV1p3beta1PropertyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PropertyIn"])
    types["GoogleCloudVisionV1p3beta1PropertyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PropertyOut"])
    types[
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut"]
    )
    types["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "score": t.number().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "score": t.number().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"])
    types["GoogleCloudVisionV1p4beta1SymbolIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "text": t.string().optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SymbolIn"])
    types["GoogleCloudVisionV1p4beta1SymbolOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "text": t.string().optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SymbolOut"])
    types["ImportProductSetsGcsSourceIn"] = t.struct(
        {"csvFileUri": t.string().optional()}
    ).named(renames["ImportProductSetsGcsSourceIn"])
    types["ImportProductSetsGcsSourceOut"] = t.struct(
        {
            "csvFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsGcsSourceOut"])
    types["PurgeProductsRequestIn"] = t.struct(
        {
            "deleteOrphanProducts": t.boolean().optional(),
            "productSetPurgeConfig": t.proxy(
                renames["ProductSetPurgeConfigIn"]
            ).optional(),
            "force": t.boolean().optional(),
        }
    ).named(renames["PurgeProductsRequestIn"])
    types["PurgeProductsRequestOut"] = t.struct(
        {
            "deleteOrphanProducts": t.boolean().optional(),
            "productSetPurgeConfig": t.proxy(
                renames["ProductSetPurgeConfigOut"]
            ).optional(),
            "force": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PurgeProductsRequestOut"])
    types["WebPageIn"] = t.struct(
        {
            "score": t.number().optional(),
            "url": t.string().optional(),
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "partialMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
        }
    ).named(renames["WebPageIn"])
    types["WebPageOut"] = t.struct(
        {
            "score": t.number().optional(),
            "url": t.string().optional(),
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageOut"])).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebPageOut"])
    types["SymbolIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
        }
    ).named(renames["SymbolIn"])
    types["SymbolOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SymbolOut"])
    types["GoogleCloudVisionV1p2beta1AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"])
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p2beta1InputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p2beta1AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"])
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p2beta1InputConfigOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateFileResponseOut"])
    types["ListReferenceImagesResponseIn"] = t.struct(
        {
            "referenceImages": t.array(t.proxy(renames["ReferenceImageIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["ListReferenceImagesResponseIn"])
    types["ListReferenceImagesResponseOut"] = t.struct(
        {
            "referenceImages": t.array(
                t.proxy(renames["ReferenceImageOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReferenceImagesResponseOut"])
    types["CropHintsParamsIn"] = t.struct(
        {"aspectRatios": t.array(t.number()).optional()}
    ).named(renames["CropHintsParamsIn"])
    types["CropHintsParamsOut"] = t.struct(
        {
            "aspectRatios": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropHintsParamsOut"])
    types["GoogleCloudVisionV1p2beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p2beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1GcsSourceOut"])
    types["GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn"] = t.struct(
        {
            "colors": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ColorInfoIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut"] = t.struct(
        {
            "colors": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ColorInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1ProductIn"] = t.struct(
        {
            "productCategory": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ProductKeyValueIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductIn"])
    types["GoogleCloudVisionV1p2beta1ProductOut"] = t.struct(
        {
            "productCategory": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ProductKeyValueOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductOut"])
    types["ProductSetIn"] = t.struct(
        {"displayName": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ProductSetIn"])
    types["ProductSetOut"] = t.struct(
        {
            "indexTime": t.string().optional(),
            "indexError": t.proxy(renames["StatusOut"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSetOut"])
    types["GoogleCloudVisionV1p2beta1ColorInfoIn"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p2beta1ColorInfoOut"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ColorInfoOut"])
    types["GoogleCloudVisionV1p1beta1InputConfigIn"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p1beta1GcsSourceIn"]
            ).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1InputConfigIn"])
    types["GoogleCloudVisionV1p1beta1InputConfigOut"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p1beta1GcsSourceOut"]
            ).optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1InputConfigOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"])
    types["GoogleCloudVisionV1p4beta1OutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p4beta1GcsDestinationIn"]
            ).optional(),
            "batchSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OutputConfigIn"])
    types["GoogleCloudVisionV1p4beta1OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p4beta1GcsDestinationOut"]
            ).optional(),
            "batchSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OutputConfigOut"])
    types["ParagraphIn"] = t.struct(
        {
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "confidence": t.number().optional(),
            "words": t.array(t.proxy(renames["WordIn"])).optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
        }
    ).named(renames["ParagraphIn"])
    types["ParagraphOut"] = t.struct(
        {
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "confidence": t.number().optional(),
            "words": t.array(t.proxy(renames["WordOut"])).optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "score": t.number().optional(),
            "entityId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "score": t.number().optional(),
            "entityId": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"])
    types["ProductSetPurgeConfigIn"] = t.struct(
        {"productSetId": t.string().optional()}
    ).named(renames["ProductSetPurgeConfigIn"])
    types["ProductSetPurgeConfigOut"] = t.struct(
        {
            "productSetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSetPurgeConfigOut"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationIn"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PageIn"])
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationOut"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PageOut"])
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseIn"])
    types["GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseOut"])
    types["GoogleCloudVisionV1p2beta1CropHintsAnnotationIn"] = t.struct(
        {
            "cropHints": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1CropHintIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p2beta1CropHintsAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1CropHintsAnnotationOut"] = t.struct(
        {
            "cropHints": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1CropHintOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1CropHintsAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn"
                    ]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut"
                    ]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut"])
    types["GoogleCloudVisionV1p2beta1OperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p2beta1OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1OperationMetadataOut"])
    types["GoogleCloudVisionV1p4beta1CropHintIn"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CropHintIn"])
    types["GoogleCloudVisionV1p4beta1CropHintOut"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CropHintOut"])
    types["GoogleCloudVisionV1p3beta1InputConfigIn"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p3beta1GcsSourceIn"]
            ).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1InputConfigIn"])
    types["GoogleCloudVisionV1p3beta1InputConfigOut"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p3beta1GcsSourceOut"]
            ).optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1InputConfigOut"])
    types["DetectedLanguageIn"] = t.struct(
        {"confidence": t.number().optional(), "languageCode": t.string().optional()}
    ).named(renames["DetectedLanguageIn"])
    types["DetectedLanguageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectedLanguageOut"])
    types["AsyncAnnotateFileRequestIn"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigIn"]),
            "features": t.array(t.proxy(renames["FeatureIn"])),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "imageContext": t.proxy(renames["ImageContextIn"]).optional(),
        }
    ).named(renames["AsyncAnnotateFileRequestIn"])
    types["AsyncAnnotateFileRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "features": t.array(t.proxy(renames["FeatureOut"])),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "imageContext": t.proxy(renames["ImageContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncAnnotateFileRequestOut"])
    types["GoogleCloudVisionV1p4beta1PageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "width": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BlockIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PageIn"])
    types["GoogleCloudVisionV1p4beta1PageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "width": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BlockOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PageOut"])
    types["GroupedResultIn"] = t.struct(
        {
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "results": t.array(t.proxy(renames["ResultIn"])).optional(),
            "objectAnnotations": t.array(
                t.proxy(renames["ObjectAnnotationIn"])
            ).optional(),
        }
    ).named(renames["GroupedResultIn"])
    types["GroupedResultOut"] = t.struct(
        {
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "results": t.array(t.proxy(renames["ResultOut"])).optional(),
            "objectAnnotations": t.array(
                t.proxy(renames["ObjectAnnotationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupedResultOut"])
    types["GoogleCloudVisionV1p3beta1BatchOperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "submitTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BatchOperationMetadataIn"])
    types["GoogleCloudVisionV1p3beta1BatchOperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "submitTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BatchOperationMetadataOut"])
    types["GoogleCloudVisionV1p3beta1ProductIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ProductKeyValueIn"])
            ).optional(),
            "productCategory": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductIn"])
    types["GoogleCloudVisionV1p3beta1ProductOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ProductKeyValueOut"])
            ).optional(),
            "productCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductOut"])
    types["GoogleCloudVisionV1p2beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p2beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1GcsDestinationOut"])
    types["GoogleCloudVisionV1p3beta1SymbolIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "text": t.string().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SymbolIn"])
    types["GoogleCloudVisionV1p3beta1SymbolOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "text": t.string().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SymbolOut"])
    types["GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p3beta1OutputConfigIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p3beta1OutputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p1beta1AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"])
            ).optional(),
            "totalPages": t.integer().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p1beta1InputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p1beta1AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"])
            ).optional(),
            "totalPages": t.integer().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p1beta1InputConfigOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseIn"])
    types["GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn"] = t.struct(
        {"languageCode": t.string().optional(), "label": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut"])
    types["GoogleCloudVisionV1p4beta1BoundingPolyIn"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1NormalizedVertexIn"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1VertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"])
    types["GoogleCloudVisionV1p4beta1BoundingPolyOut"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1NormalizedVertexOut"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1VertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"])
    types["GoogleCloudVisionV1p4beta1BatchOperationMetadataIn"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BatchOperationMetadataIn"])
    types["GoogleCloudVisionV1p4beta1BatchOperationMetadataOut"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BatchOperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleCloudVisionV1p1beta1ColorInfoIn"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p1beta1ColorInfoOut"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ColorInfoOut"])
    types["GoogleCloudVisionV1p2beta1ImagePropertiesIn"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ImagePropertiesIn"])
    types["GoogleCloudVisionV1p2beta1ImagePropertiesOut"] = t.struct(
        {
            "dominantColors": t.proxy(
                renames["GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ImagePropertiesOut"])
    types["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "violence": t.string().optional(),
            "racy": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "spoof": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "violence": t.string().optional(),
            "racy": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "spoof": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"])
    types["BatchAnnotateImagesRequestIn"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
            "parent": t.string().optional(),
        }
    ).named(renames["BatchAnnotateImagesRequestIn"])
    types["BatchAnnotateImagesRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["AnnotateImageRequestOut"])),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchAnnotateImagesRequestOut"])
    types["WebDetectionParamsIn"] = t.struct(
        {"includeGeoResults": t.boolean().optional()}
    ).named(renames["WebDetectionParamsIn"])
    types["WebDetectionParamsOut"] = t.struct(
        {
            "includeGeoResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebDetectionParamsOut"])
    types["GoogleCloudVisionV1p4beta1ProductIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ProductKeyValueIn"])
            ).optional(),
            "productCategory": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductIn"])
    types["GoogleCloudVisionV1p4beta1ProductOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ProductKeyValueOut"])
            ).optional(),
            "productCategory": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductOut"])
    types["AddProductToProductSetRequestIn"] = t.struct({"product": t.string()}).named(
        renames["AddProductToProductSetRequestIn"]
    )
    types["AddProductToProductSetRequestOut"] = t.struct(
        {"product": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddProductToProductSetRequestOut"])
    types["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "racy": t.string().optional(),
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "violence": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "racy": t.string().optional(),
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "violence": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1PositionIn"] = t.struct(
        {
            "z": t.number().optional(),
            "y": t.number().optional(),
            "x": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PositionIn"])
    types["GoogleCloudVisionV1p1beta1PositionOut"] = t.struct(
        {
            "z": t.number().optional(),
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PositionOut"])
    types["LatLngIn"] = t.struct(
        {"latitude": t.number().optional(), "longitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["ListProductsResponseIn"] = t.struct(
        {
            "products": t.array(t.proxy(renames["ProductIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProductsResponseIn"])
    types["ListProductsResponseOut"] = t.struct(
        {
            "products": t.array(t.proxy(renames["ProductOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductsResponseOut"])
    types["GoogleCloudVisionV1p3beta1EntityAnnotationIn"] = t.struct(
        {
            "score": t.number().optional(),
            "locale": t.string().optional(),
            "topicality": t.number().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1LocationInfoIn"])
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "mid": t.string().optional(),
            "confidence": t.number().optional(),
            "description": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PropertyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1EntityAnnotationOut"] = t.struct(
        {
            "score": t.number().optional(),
            "locale": t.string().optional(),
            "topicality": t.number().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1LocationInfoOut"])
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "mid": t.string().optional(),
            "confidence": t.number().optional(),
            "description": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"] = t.struct(
        {"score": t.number().optional(), "url": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"] = t.struct(
        {
            "score": t.number().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
    types["GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1OutputConfigIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1OutputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationIn"] = t.struct(
        {
            "text": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationOut"] = t.struct(
        {
            "text": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationOut"])
    types["GoogleCloudVisionV1p3beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p3beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1GcsSourceOut"])

    functions = {}
    functions["projectsImagesAnnotate"] = vision.post(
        "v1/{parent}/images:asyncBatchAnnotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "outputConfig": t.proxy(renames["OutputConfigIn"]),
                "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsImagesAsyncBatchAnnotate"] = vision.post(
        "v1/{parent}/images:asyncBatchAnnotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "outputConfig": t.proxy(renames["OutputConfigIn"]),
                "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFilesAsyncBatchAnnotate"] = vision.post(
        "v1/{parent}/files:annotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AnnotateFileRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFilesAnnotate"] = vision.post(
        "v1/{parent}/files:annotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AnnotateFileRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImagesAsyncBatchAnnotate"] = vision.post(
        "v1/{parent}/images:annotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateImagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImagesAnnotate"] = vision.post(
        "v1/{parent}/images:annotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateImagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsGet"] = vision.post(
        "v1/{parent}/productSets",
        t.struct(
            {
                "parent": t.string(),
                "productSetId": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsList"] = vision.post(
        "v1/{parent}/productSets",
        t.struct(
            {
                "parent": t.string(),
                "productSetId": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsPatch"] = vision.post(
        "v1/{parent}/productSets",
        t.struct(
            {
                "parent": t.string(),
                "productSetId": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsImport"] = vision.post(
        "v1/{parent}/productSets",
        t.struct(
            {
                "parent": t.string(),
                "productSetId": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsRemoveProduct"] = vision.post(
        "v1/{parent}/productSets",
        t.struct(
            {
                "parent": t.string(),
                "productSetId": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsDelete"] = vision.post(
        "v1/{parent}/productSets",
        t.struct(
            {
                "parent": t.string(),
                "productSetId": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsAddProduct"] = vision.post(
        "v1/{parent}/productSets",
        t.struct(
            {
                "parent": t.string(),
                "productSetId": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsCreate"] = vision.post(
        "v1/{parent}/productSets",
        t.struct(
            {
                "parent": t.string(),
                "productSetId": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsProductsList"] = vision.get(
        "v1/{name}/products",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsInProductSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFilesAnnotate"] = vision.post(
        "v1/{parent}/files:asyncBatchAnnotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AsyncAnnotateFileRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFilesAsyncBatchAnnotate"] = vision.post(
        "v1/{parent}/files:asyncBatchAnnotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AsyncAnnotateFileRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsGet"] = vision.post(
        "v1/{parent}/products:purge",
        t.struct(
            {
                "parent": t.string(),
                "deleteOrphanProducts": t.boolean().optional(),
                "productSetPurgeConfig": t.proxy(
                    renames["ProductSetPurgeConfigIn"]
                ).optional(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsDelete"] = vision.post(
        "v1/{parent}/products:purge",
        t.struct(
            {
                "parent": t.string(),
                "deleteOrphanProducts": t.boolean().optional(),
                "productSetPurgeConfig": t.proxy(
                    renames["ProductSetPurgeConfigIn"]
                ).optional(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsPatch"] = vision.post(
        "v1/{parent}/products:purge",
        t.struct(
            {
                "parent": t.string(),
                "deleteOrphanProducts": t.boolean().optional(),
                "productSetPurgeConfig": t.proxy(
                    renames["ProductSetPurgeConfigIn"]
                ).optional(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCreate"] = vision.post(
        "v1/{parent}/products:purge",
        t.struct(
            {
                "parent": t.string(),
                "deleteOrphanProducts": t.boolean().optional(),
                "productSetPurgeConfig": t.proxy(
                    renames["ProductSetPurgeConfigIn"]
                ).optional(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsList"] = vision.post(
        "v1/{parent}/products:purge",
        t.struct(
            {
                "parent": t.string(),
                "deleteOrphanProducts": t.boolean().optional(),
                "productSetPurgeConfig": t.proxy(
                    renames["ProductSetPurgeConfigIn"]
                ).optional(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsPurge"] = vision.post(
        "v1/{parent}/products:purge",
        t.struct(
            {
                "parent": t.string(),
                "deleteOrphanProducts": t.boolean().optional(),
                "productSetPurgeConfig": t.proxy(
                    renames["ProductSetPurgeConfigIn"]
                ).optional(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesList"] = vision.post(
        "v1/{parent}/referenceImages",
        t.struct(
            {
                "parent": t.string(),
                "referenceImageId": t.string().optional(),
                "name": t.string().optional(),
                "boundingPolys": t.array(t.proxy(renames["BoundingPolyIn"])).optional(),
                "uri": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReferenceImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesGet"] = vision.post(
        "v1/{parent}/referenceImages",
        t.struct(
            {
                "parent": t.string(),
                "referenceImageId": t.string().optional(),
                "name": t.string().optional(),
                "boundingPolys": t.array(t.proxy(renames["BoundingPolyIn"])).optional(),
                "uri": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReferenceImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesDelete"] = vision.post(
        "v1/{parent}/referenceImages",
        t.struct(
            {
                "parent": t.string(),
                "referenceImageId": t.string().optional(),
                "name": t.string().optional(),
                "boundingPolys": t.array(t.proxy(renames["BoundingPolyIn"])).optional(),
                "uri": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReferenceImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesCreate"] = vision.post(
        "v1/{parent}/referenceImages",
        t.struct(
            {
                "parent": t.string(),
                "referenceImageId": t.string().optional(),
                "name": t.string().optional(),
                "boundingPolys": t.array(t.proxy(renames["BoundingPolyIn"])).optional(),
                "uri": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReferenceImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesAsyncBatchAnnotate"] = vision.post(
        "v1/files:annotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AnnotateFileRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesAnnotate"] = vision.post(
        "v1/files:annotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AnnotateFileRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["imagesAsyncBatchAnnotate"] = vision.post(
        "v1/images:annotate",
        t.struct(
            {
                "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateImagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["imagesAnnotate"] = vision.post(
        "v1/images:annotate",
        t.struct(
            {
                "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateImagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsOperationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = vision.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = vision.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = vision.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = vision.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vision", renames=renames, types=Box(types), functions=Box(functions)
    )
