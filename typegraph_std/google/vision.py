from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_vision():
    vision = HTTPRuntime("https://vision.googleapis.com/")

    renames = {
        "ErrorResponse": "_vision_1_ErrorResponse",
        "GoogleCloudVisionV1p2beta1CropHintIn": "_vision_2_GoogleCloudVisionV1p2beta1CropHintIn",
        "GoogleCloudVisionV1p2beta1CropHintOut": "_vision_3_GoogleCloudVisionV1p2beta1CropHintOut",
        "GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn": "_vision_4_GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn",
        "GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut": "_vision_5_GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut",
        "GoogleCloudVisionV1p3beta1ParagraphIn": "_vision_6_GoogleCloudVisionV1p3beta1ParagraphIn",
        "GoogleCloudVisionV1p3beta1ParagraphOut": "_vision_7_GoogleCloudVisionV1p3beta1ParagraphOut",
        "GoogleCloudVisionV1p3beta1GcsDestinationIn": "_vision_8_GoogleCloudVisionV1p3beta1GcsDestinationIn",
        "GoogleCloudVisionV1p3beta1GcsDestinationOut": "_vision_9_GoogleCloudVisionV1p3beta1GcsDestinationOut",
        "GoogleCloudVisionV1p2beta1NormalizedVertexIn": "_vision_10_GoogleCloudVisionV1p2beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p2beta1NormalizedVertexOut": "_vision_11_GoogleCloudVisionV1p2beta1NormalizedVertexOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn": "_vision_12_GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut": "_vision_13_GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut",
        "LocationInfoIn": "_vision_14_LocationInfoIn",
        "LocationInfoOut": "_vision_15_LocationInfoOut",
        "EmptyIn": "_vision_16_EmptyIn",
        "EmptyOut": "_vision_17_EmptyOut",
        "GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn": "_vision_18_GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut": "_vision_19_GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p1beta1ProductIn": "_vision_20_GoogleCloudVisionV1p1beta1ProductIn",
        "GoogleCloudVisionV1p1beta1ProductOut": "_vision_21_GoogleCloudVisionV1p1beta1ProductOut",
        "GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn": "_vision_22_GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut": "_vision_23_GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p4beta1BoundingPolyIn": "_vision_24_GoogleCloudVisionV1p4beta1BoundingPolyIn",
        "GoogleCloudVisionV1p4beta1BoundingPolyOut": "_vision_25_GoogleCloudVisionV1p4beta1BoundingPolyOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn": "_vision_26_GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut": "_vision_27_GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebImageIn": "_vision_28_GoogleCloudVisionV1p3beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebImageOut": "_vision_29_GoogleCloudVisionV1p3beta1WebDetectionWebImageOut",
        "BatchAnnotateImagesResponseIn": "_vision_30_BatchAnnotateImagesResponseIn",
        "BatchAnnotateImagesResponseOut": "_vision_31_BatchAnnotateImagesResponseOut",
        "WordIn": "_vision_32_WordIn",
        "WordOut": "_vision_33_WordOut",
        "GoogleCloudVisionV1p2beta1BlockIn": "_vision_34_GoogleCloudVisionV1p2beta1BlockIn",
        "GoogleCloudVisionV1p2beta1BlockOut": "_vision_35_GoogleCloudVisionV1p2beta1BlockOut",
        "GoogleCloudVisionV1p3beta1ImagePropertiesIn": "_vision_36_GoogleCloudVisionV1p3beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p3beta1ImagePropertiesOut": "_vision_37_GoogleCloudVisionV1p3beta1ImagePropertiesOut",
        "TextAnnotationIn": "_vision_38_TextAnnotationIn",
        "TextAnnotationOut": "_vision_39_TextAnnotationOut",
        "GoogleCloudVisionV1p3beta1OperationMetadataIn": "_vision_40_GoogleCloudVisionV1p3beta1OperationMetadataIn",
        "GoogleCloudVisionV1p3beta1OperationMetadataOut": "_vision_41_GoogleCloudVisionV1p3beta1OperationMetadataOut",
        "ImportProductSetsResponseIn": "_vision_42_ImportProductSetsResponseIn",
        "ImportProductSetsResponseOut": "_vision_43_ImportProductSetsResponseOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebPageIn": "_vision_44_GoogleCloudVisionV1p3beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebPageOut": "_vision_45_GoogleCloudVisionV1p3beta1WebDetectionWebPageOut",
        "AsyncAnnotateFileRequestIn": "_vision_46_AsyncAnnotateFileRequestIn",
        "AsyncAnnotateFileRequestOut": "_vision_47_AsyncAnnotateFileRequestOut",
        "GoogleCloudVisionV1p1beta1ImagePropertiesIn": "_vision_48_GoogleCloudVisionV1p1beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p1beta1ImagePropertiesOut": "_vision_49_GoogleCloudVisionV1p1beta1ImagePropertiesOut",
        "GoogleCloudVisionV1p4beta1SymbolIn": "_vision_50_GoogleCloudVisionV1p4beta1SymbolIn",
        "GoogleCloudVisionV1p4beta1SymbolOut": "_vision_51_GoogleCloudVisionV1p4beta1SymbolOut",
        "GoogleCloudVisionV1p4beta1ProductIn": "_vision_52_GoogleCloudVisionV1p4beta1ProductIn",
        "GoogleCloudVisionV1p4beta1ProductOut": "_vision_53_GoogleCloudVisionV1p4beta1ProductOut",
        "TextDetectionParamsIn": "_vision_54_TextDetectionParamsIn",
        "TextDetectionParamsOut": "_vision_55_TextDetectionParamsOut",
        "GoogleCloudVisionV1p3beta1BlockIn": "_vision_56_GoogleCloudVisionV1p3beta1BlockIn",
        "GoogleCloudVisionV1p3beta1BlockOut": "_vision_57_GoogleCloudVisionV1p3beta1BlockOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn": "_vision_58_GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut": "_vision_59_GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebPageIn": "_vision_60_GoogleCloudVisionV1p2beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebPageOut": "_vision_61_GoogleCloudVisionV1p2beta1WebDetectionWebPageOut",
        "ColorInfoIn": "_vision_62_ColorInfoIn",
        "ColorInfoOut": "_vision_63_ColorInfoOut",
        "GoogleCloudVisionV1p1beta1PageIn": "_vision_64_GoogleCloudVisionV1p1beta1PageIn",
        "GoogleCloudVisionV1p1beta1PageOut": "_vision_65_GoogleCloudVisionV1p1beta1PageOut",
        "GoogleCloudVisionV1p3beta1CropHintIn": "_vision_66_GoogleCloudVisionV1p3beta1CropHintIn",
        "GoogleCloudVisionV1p3beta1CropHintOut": "_vision_67_GoogleCloudVisionV1p3beta1CropHintOut",
        "GoogleCloudVisionV1p4beta1AnnotateImageResponseIn": "_vision_68_GoogleCloudVisionV1p4beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p4beta1AnnotateImageResponseOut": "_vision_69_GoogleCloudVisionV1p4beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p1beta1WordIn": "_vision_70_GoogleCloudVisionV1p1beta1WordIn",
        "GoogleCloudVisionV1p1beta1WordOut": "_vision_71_GoogleCloudVisionV1p1beta1WordOut",
        "GoogleCloudVisionV1p2beta1PageIn": "_vision_72_GoogleCloudVisionV1p2beta1PageIn",
        "GoogleCloudVisionV1p2beta1PageOut": "_vision_73_GoogleCloudVisionV1p2beta1PageOut",
        "NormalizedVertexIn": "_vision_74_NormalizedVertexIn",
        "NormalizedVertexOut": "_vision_75_NormalizedVertexOut",
        "GoogleCloudVisionV1p4beta1BlockIn": "_vision_76_GoogleCloudVisionV1p4beta1BlockIn",
        "GoogleCloudVisionV1p4beta1BlockOut": "_vision_77_GoogleCloudVisionV1p4beta1BlockOut",
        "GoogleCloudVisionV1p1beta1EntityAnnotationIn": "_vision_78_GoogleCloudVisionV1p1beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p1beta1EntityAnnotationOut": "_vision_79_GoogleCloudVisionV1p1beta1EntityAnnotationOut",
        "GoogleCloudVisionV1p3beta1ReferenceImageIn": "_vision_80_GoogleCloudVisionV1p3beta1ReferenceImageIn",
        "GoogleCloudVisionV1p3beta1ReferenceImageOut": "_vision_81_GoogleCloudVisionV1p3beta1ReferenceImageOut",
        "GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn": "_vision_82_GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut": "_vision_83_GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut",
        "ProductSetPurgeConfigIn": "_vision_84_ProductSetPurgeConfigIn",
        "ProductSetPurgeConfigOut": "_vision_85_ProductSetPurgeConfigOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn": "_vision_86_GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut": "_vision_87_GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut",
        "GoogleCloudVisionV1p2beta1ParagraphIn": "_vision_88_GoogleCloudVisionV1p2beta1ParagraphIn",
        "GoogleCloudVisionV1p2beta1ParagraphOut": "_vision_89_GoogleCloudVisionV1p2beta1ParagraphOut",
        "GoogleCloudVisionV1p2beta1FaceAnnotationIn": "_vision_90_GoogleCloudVisionV1p2beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p2beta1FaceAnnotationOut": "_vision_91_GoogleCloudVisionV1p2beta1FaceAnnotationOut",
        "GoogleCloudVisionV1p2beta1ColorInfoIn": "_vision_92_GoogleCloudVisionV1p2beta1ColorInfoIn",
        "GoogleCloudVisionV1p2beta1ColorInfoOut": "_vision_93_GoogleCloudVisionV1p2beta1ColorInfoOut",
        "GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn": "_vision_94_GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut": "_vision_95_GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut",
        "OutputConfigIn": "_vision_96_OutputConfigIn",
        "OutputConfigOut": "_vision_97_OutputConfigOut",
        "PageIn": "_vision_98_PageIn",
        "PageOut": "_vision_99_PageOut",
        "GoogleCloudVisionV1p3beta1ProductKeyValueIn": "_vision_100_GoogleCloudVisionV1p3beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p3beta1ProductKeyValueOut": "_vision_101_GoogleCloudVisionV1p3beta1ProductKeyValueOut",
        "ImageContextIn": "_vision_102_ImageContextIn",
        "ImageContextOut": "_vision_103_ImageContextOut",
        "AnnotateFileResponseIn": "_vision_104_AnnotateFileResponseIn",
        "AnnotateFileResponseOut": "_vision_105_AnnotateFileResponseOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn": "_vision_106_GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut": "_vision_107_GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn": "_vision_108_GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut": "_vision_109_GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn": "_vision_110_GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut": "_vision_111_GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut",
        "GoogleCloudVisionV1p2beta1ProductIn": "_vision_112_GoogleCloudVisionV1p2beta1ProductIn",
        "GoogleCloudVisionV1p2beta1ProductOut": "_vision_113_GoogleCloudVisionV1p2beta1ProductOut",
        "GoogleCloudVisionV1p4beta1CelebrityIn": "_vision_114_GoogleCloudVisionV1p4beta1CelebrityIn",
        "GoogleCloudVisionV1p4beta1CelebrityOut": "_vision_115_GoogleCloudVisionV1p4beta1CelebrityOut",
        "GoogleCloudVisionV1p4beta1GcsDestinationIn": "_vision_116_GoogleCloudVisionV1p4beta1GcsDestinationIn",
        "GoogleCloudVisionV1p4beta1GcsDestinationOut": "_vision_117_GoogleCloudVisionV1p4beta1GcsDestinationOut",
        "GoogleCloudVisionV1p3beta1CropHintsAnnotationIn": "_vision_118_GoogleCloudVisionV1p3beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p3beta1CropHintsAnnotationOut": "_vision_119_GoogleCloudVisionV1p3beta1CropHintsAnnotationOut",
        "GoogleCloudVisionV1p4beta1EntityAnnotationIn": "_vision_120_GoogleCloudVisionV1p4beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p4beta1EntityAnnotationOut": "_vision_121_GoogleCloudVisionV1p4beta1EntityAnnotationOut",
        "AnnotateImageResponseIn": "_vision_122_AnnotateImageResponseIn",
        "AnnotateImageResponseOut": "_vision_123_AnnotateImageResponseOut",
        "ListReferenceImagesResponseIn": "_vision_124_ListReferenceImagesResponseIn",
        "ListReferenceImagesResponseOut": "_vision_125_ListReferenceImagesResponseOut",
        "GoogleCloudVisionV1p3beta1EntityAnnotationIn": "_vision_126_GoogleCloudVisionV1p3beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p3beta1EntityAnnotationOut": "_vision_127_GoogleCloudVisionV1p3beta1EntityAnnotationOut",
        "AsyncBatchAnnotateImagesRequestIn": "_vision_128_AsyncBatchAnnotateImagesRequestIn",
        "AsyncBatchAnnotateImagesRequestOut": "_vision_129_AsyncBatchAnnotateImagesRequestOut",
        "GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn": "_vision_130_GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut": "_vision_131_GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p1beta1GcsSourceIn": "_vision_132_GoogleCloudVisionV1p1beta1GcsSourceIn",
        "GoogleCloudVisionV1p1beta1GcsSourceOut": "_vision_133_GoogleCloudVisionV1p1beta1GcsSourceOut",
        "GoogleCloudVisionV1p3beta1ColorInfoIn": "_vision_134_GoogleCloudVisionV1p3beta1ColorInfoIn",
        "GoogleCloudVisionV1p3beta1ColorInfoOut": "_vision_135_GoogleCloudVisionV1p3beta1ColorInfoOut",
        "AsyncBatchAnnotateFilesResponseIn": "_vision_136_AsyncBatchAnnotateFilesResponseIn",
        "AsyncBatchAnnotateFilesResponseOut": "_vision_137_AsyncBatchAnnotateFilesResponseOut",
        "BoundingPolyIn": "_vision_138_BoundingPolyIn",
        "BoundingPolyOut": "_vision_139_BoundingPolyOut",
        "OperationIn": "_vision_140_OperationIn",
        "OperationOut": "_vision_141_OperationOut",
        "GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn": "_vision_142_GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut": "_vision_143_GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut",
        "GcsSourceIn": "_vision_144_GcsSourceIn",
        "GcsSourceOut": "_vision_145_GcsSourceOut",
        "ProductSearchResultsIn": "_vision_146_ProductSearchResultsIn",
        "ProductSearchResultsOut": "_vision_147_ProductSearchResultsOut",
        "GroupedResultIn": "_vision_148_GroupedResultIn",
        "GroupedResultOut": "_vision_149_GroupedResultOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn": "_vision_150_GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut": "_vision_151_GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseIn": "_vision_152_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseOut": "_vision_153_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseOut",
        "GoogleCloudVisionV1p3beta1AnnotateImageResponseIn": "_vision_154_GoogleCloudVisionV1p3beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p3beta1AnnotateImageResponseOut": "_vision_155_GoogleCloudVisionV1p3beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p3beta1GcsSourceIn": "_vision_156_GoogleCloudVisionV1p3beta1GcsSourceIn",
        "GoogleCloudVisionV1p3beta1GcsSourceOut": "_vision_157_GoogleCloudVisionV1p3beta1GcsSourceOut",
        "GoogleCloudVisionV1p4beta1ProductKeyValueIn": "_vision_158_GoogleCloudVisionV1p4beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p4beta1ProductKeyValueOut": "_vision_159_GoogleCloudVisionV1p4beta1ProductKeyValueOut",
        "ImagePropertiesIn": "_vision_160_ImagePropertiesIn",
        "ImagePropertiesOut": "_vision_161_ImagePropertiesOut",
        "GoogleCloudVisionV1p1beta1OutputConfigIn": "_vision_162_GoogleCloudVisionV1p1beta1OutputConfigIn",
        "GoogleCloudVisionV1p1beta1OutputConfigOut": "_vision_163_GoogleCloudVisionV1p1beta1OutputConfigOut",
        "GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn": "_vision_164_GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn",
        "GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut": "_vision_165_GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut",
        "ObjectAnnotationIn": "_vision_166_ObjectAnnotationIn",
        "ObjectAnnotationOut": "_vision_167_ObjectAnnotationOut",
        "GoogleCloudVisionV1p3beta1PageIn": "_vision_168_GoogleCloudVisionV1p3beta1PageIn",
        "GoogleCloudVisionV1p3beta1PageOut": "_vision_169_GoogleCloudVisionV1p3beta1PageOut",
        "GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn": "_vision_170_GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut": "_vision_171_GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationIn": "_vision_172_GoogleCloudVisionV1p3beta1TextAnnotationIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationOut": "_vision_173_GoogleCloudVisionV1p3beta1TextAnnotationOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn": "_vision_174_GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut": "_vision_175_GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut",
        "GoogleCloudVisionV1p1beta1OperationMetadataIn": "_vision_176_GoogleCloudVisionV1p1beta1OperationMetadataIn",
        "GoogleCloudVisionV1p1beta1OperationMetadataOut": "_vision_177_GoogleCloudVisionV1p1beta1OperationMetadataOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn": "_vision_178_GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut": "_vision_179_GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p2beta1CropHintsAnnotationIn": "_vision_180_GoogleCloudVisionV1p2beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p2beta1CropHintsAnnotationOut": "_vision_181_GoogleCloudVisionV1p2beta1CropHintsAnnotationOut",
        "ImageSourceIn": "_vision_182_ImageSourceIn",
        "ImageSourceOut": "_vision_183_ImageSourceOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn": "_vision_184_GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut": "_vision_185_GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p1beta1SymbolIn": "_vision_186_GoogleCloudVisionV1p1beta1SymbolIn",
        "GoogleCloudVisionV1p1beta1SymbolOut": "_vision_187_GoogleCloudVisionV1p1beta1SymbolOut",
        "StatusIn": "_vision_188_StatusIn",
        "StatusOut": "_vision_189_StatusOut",
        "GoogleCloudVisionV1p1beta1BoundingPolyIn": "_vision_190_GoogleCloudVisionV1p1beta1BoundingPolyIn",
        "GoogleCloudVisionV1p1beta1BoundingPolyOut": "_vision_191_GoogleCloudVisionV1p1beta1BoundingPolyOut",
        "CropHintIn": "_vision_192_CropHintIn",
        "CropHintOut": "_vision_193_CropHintOut",
        "GoogleCloudVisionV1p2beta1InputConfigIn": "_vision_194_GoogleCloudVisionV1p2beta1InputConfigIn",
        "GoogleCloudVisionV1p2beta1InputConfigOut": "_vision_195_GoogleCloudVisionV1p2beta1InputConfigOut",
        "InputConfigIn": "_vision_196_InputConfigIn",
        "InputConfigOut": "_vision_197_InputConfigOut",
        "GoogleCloudVisionV1p4beta1FaceAnnotationIn": "_vision_198_GoogleCloudVisionV1p4beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p4beta1FaceAnnotationOut": "_vision_199_GoogleCloudVisionV1p4beta1FaceAnnotationOut",
        "GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn": "_vision_200_GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut": "_vision_201_GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p3beta1NormalizedVertexIn": "_vision_202_GoogleCloudVisionV1p3beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p3beta1NormalizedVertexOut": "_vision_203_GoogleCloudVisionV1p3beta1NormalizedVertexOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn": "_vision_204_GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut": "_vision_205_GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p4beta1PropertyIn": "_vision_206_GoogleCloudVisionV1p4beta1PropertyIn",
        "GoogleCloudVisionV1p4beta1PropertyOut": "_vision_207_GoogleCloudVisionV1p4beta1PropertyOut",
        "GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn": "_vision_208_GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut": "_vision_209_GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn": "_vision_210_GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut": "_vision_211_GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsIn": "_vision_212_GoogleCloudVisionV1p1beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsOut": "_vision_213_GoogleCloudVisionV1p1beta1ProductSearchResultsOut",
        "GoogleCloudVisionV1p4beta1PositionIn": "_vision_214_GoogleCloudVisionV1p4beta1PositionIn",
        "GoogleCloudVisionV1p4beta1PositionOut": "_vision_215_GoogleCloudVisionV1p4beta1PositionOut",
        "GoogleCloudVisionV1p4beta1AnnotateFileResponseIn": "_vision_216_GoogleCloudVisionV1p4beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p4beta1AnnotateFileResponseOut": "_vision_217_GoogleCloudVisionV1p4beta1AnnotateFileResponseOut",
        "GoogleCloudVisionV1p4beta1ImagePropertiesIn": "_vision_218_GoogleCloudVisionV1p4beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p4beta1ImagePropertiesOut": "_vision_219_GoogleCloudVisionV1p4beta1ImagePropertiesOut",
        "PurgeProductsRequestIn": "_vision_220_PurgeProductsRequestIn",
        "PurgeProductsRequestOut": "_vision_221_PurgeProductsRequestOut",
        "GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn": "_vision_222_GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut": "_vision_223_GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p1beta1ColorInfoIn": "_vision_224_GoogleCloudVisionV1p1beta1ColorInfoIn",
        "GoogleCloudVisionV1p1beta1ColorInfoOut": "_vision_225_GoogleCloudVisionV1p1beta1ColorInfoOut",
        "GoogleCloudVisionV1p4beta1CropHintsAnnotationIn": "_vision_226_GoogleCloudVisionV1p4beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p4beta1CropHintsAnnotationOut": "_vision_227_GoogleCloudVisionV1p4beta1CropHintsAnnotationOut",
        "DominantColorsAnnotationIn": "_vision_228_DominantColorsAnnotationIn",
        "DominantColorsAnnotationOut": "_vision_229_DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn": "_vision_230_GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut": "_vision_231_GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p4beta1InputConfigIn": "_vision_232_GoogleCloudVisionV1p4beta1InputConfigIn",
        "GoogleCloudVisionV1p4beta1InputConfigOut": "_vision_233_GoogleCloudVisionV1p4beta1InputConfigOut",
        "CropHintsParamsIn": "_vision_234_CropHintsParamsIn",
        "CropHintsParamsOut": "_vision_235_CropHintsParamsOut",
        "GoogleCloudVisionV1p4beta1CropHintIn": "_vision_236_GoogleCloudVisionV1p4beta1CropHintIn",
        "GoogleCloudVisionV1p4beta1CropHintOut": "_vision_237_GoogleCloudVisionV1p4beta1CropHintOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn": "_vision_238_GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut": "_vision_239_GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn": "_vision_240_GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut": "_vision_241_GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn": "_vision_242_GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut": "_vision_243_GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut",
        "AsyncAnnotateFileResponseIn": "_vision_244_AsyncAnnotateFileResponseIn",
        "AsyncAnnotateFileResponseOut": "_vision_245_AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p3beta1BatchOperationMetadataIn": "_vision_246_GoogleCloudVisionV1p3beta1BatchOperationMetadataIn",
        "GoogleCloudVisionV1p3beta1BatchOperationMetadataOut": "_vision_247_GoogleCloudVisionV1p3beta1BatchOperationMetadataOut",
        "ImageIn": "_vision_248_ImageIn",
        "ImageOut": "_vision_249_ImageOut",
        "FaceAnnotationIn": "_vision_250_FaceAnnotationIn",
        "FaceAnnotationOut": "_vision_251_FaceAnnotationOut",
        "GoogleCloudVisionV1p1beta1InputConfigIn": "_vision_252_GoogleCloudVisionV1p1beta1InputConfigIn",
        "GoogleCloudVisionV1p1beta1InputConfigOut": "_vision_253_GoogleCloudVisionV1p1beta1InputConfigOut",
        "ImportProductSetsGcsSourceIn": "_vision_254_ImportProductSetsGcsSourceIn",
        "ImportProductSetsGcsSourceOut": "_vision_255_ImportProductSetsGcsSourceOut",
        "GoogleCloudVisionV1p2beta1BoundingPolyIn": "_vision_256_GoogleCloudVisionV1p2beta1BoundingPolyIn",
        "GoogleCloudVisionV1p2beta1BoundingPolyOut": "_vision_257_GoogleCloudVisionV1p2beta1BoundingPolyOut",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseIn": "_vision_258_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseOut": "_vision_259_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsIn": "_vision_260_GoogleCloudVisionV1p4beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsOut": "_vision_261_GoogleCloudVisionV1p4beta1ProductSearchResultsOut",
        "GoogleCloudVisionV1p2beta1PropertyIn": "_vision_262_GoogleCloudVisionV1p2beta1PropertyIn",
        "GoogleCloudVisionV1p2beta1PropertyOut": "_vision_263_GoogleCloudVisionV1p2beta1PropertyOut",
        "GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseIn": "_vision_264_GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseOut": "_vision_265_GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p2beta1GcsDestinationIn": "_vision_266_GoogleCloudVisionV1p2beta1GcsDestinationIn",
        "GoogleCloudVisionV1p2beta1GcsDestinationOut": "_vision_267_GoogleCloudVisionV1p2beta1GcsDestinationOut",
        "GoogleCloudVisionV1p4beta1GcsSourceIn": "_vision_268_GoogleCloudVisionV1p4beta1GcsSourceIn",
        "GoogleCloudVisionV1p4beta1GcsSourceOut": "_vision_269_GoogleCloudVisionV1p4beta1GcsSourceOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn": "_vision_270_GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut": "_vision_271_GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p2beta1OutputConfigIn": "_vision_272_GoogleCloudVisionV1p2beta1OutputConfigIn",
        "GoogleCloudVisionV1p2beta1OutputConfigOut": "_vision_273_GoogleCloudVisionV1p2beta1OutputConfigOut",
        "GoogleCloudVisionV1p3beta1FaceAnnotationIn": "_vision_274_GoogleCloudVisionV1p3beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p3beta1FaceAnnotationOut": "_vision_275_GoogleCloudVisionV1p3beta1FaceAnnotationOut",
        "WebEntityIn": "_vision_276_WebEntityIn",
        "WebEntityOut": "_vision_277_WebEntityOut",
        "GoogleCloudVisionV1p4beta1WordIn": "_vision_278_GoogleCloudVisionV1p4beta1WordIn",
        "GoogleCloudVisionV1p4beta1WordOut": "_vision_279_GoogleCloudVisionV1p4beta1WordOut",
        "KeyValueIn": "_vision_280_KeyValueIn",
        "KeyValueOut": "_vision_281_KeyValueOut",
        "GoogleCloudVisionV1p2beta1WordIn": "_vision_282_GoogleCloudVisionV1p2beta1WordIn",
        "GoogleCloudVisionV1p2beta1WordOut": "_vision_283_GoogleCloudVisionV1p2beta1WordOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn": "_vision_284_GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut": "_vision_285_GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn": "_vision_286_GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut": "_vision_287_GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p3beta1BoundingPolyIn": "_vision_288_GoogleCloudVisionV1p3beta1BoundingPolyIn",
        "GoogleCloudVisionV1p3beta1BoundingPolyOut": "_vision_289_GoogleCloudVisionV1p3beta1BoundingPolyOut",
        "LatLngIn": "_vision_290_LatLngIn",
        "LatLngOut": "_vision_291_LatLngOut",
        "GoogleCloudVisionV1p4beta1ReferenceImageIn": "_vision_292_GoogleCloudVisionV1p4beta1ReferenceImageIn",
        "GoogleCloudVisionV1p4beta1ReferenceImageOut": "_vision_293_GoogleCloudVisionV1p4beta1ReferenceImageOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebImageIn": "_vision_294_GoogleCloudVisionV1p1beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebImageOut": "_vision_295_GoogleCloudVisionV1p1beta1WebDetectionWebImageOut",
        "GoogleCloudVisionV1p1beta1WebDetectionIn": "_vision_296_GoogleCloudVisionV1p1beta1WebDetectionIn",
        "GoogleCloudVisionV1p1beta1WebDetectionOut": "_vision_297_GoogleCloudVisionV1p1beta1WebDetectionOut",
        "DetectedBreakIn": "_vision_298_DetectedBreakIn",
        "DetectedBreakOut": "_vision_299_DetectedBreakOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn": "_vision_300_GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut": "_vision_301_GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p1beta1AnnotateImageResponseIn": "_vision_302_GoogleCloudVisionV1p1beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p1beta1AnnotateImageResponseOut": "_vision_303_GoogleCloudVisionV1p1beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationIn": "_vision_304_GoogleCloudVisionV1p2beta1TextAnnotationIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationOut": "_vision_305_GoogleCloudVisionV1p2beta1TextAnnotationOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn": "_vision_306_GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut": "_vision_307_GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut",
        "RemoveProductFromProductSetRequestIn": "_vision_308_RemoveProductFromProductSetRequestIn",
        "RemoveProductFromProductSetRequestOut": "_vision_309_RemoveProductFromProductSetRequestOut",
        "GcsDestinationIn": "_vision_310_GcsDestinationIn",
        "GcsDestinationOut": "_vision_311_GcsDestinationOut",
        "GoogleCloudVisionV1p2beta1ImageAnnotationContextIn": "_vision_312_GoogleCloudVisionV1p2beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p2beta1ImageAnnotationContextOut": "_vision_313_GoogleCloudVisionV1p2beta1ImageAnnotationContextOut",
        "VertexIn": "_vision_314_VertexIn",
        "VertexOut": "_vision_315_VertexOut",
        "BatchAnnotateFilesResponseIn": "_vision_316_BatchAnnotateFilesResponseIn",
        "BatchAnnotateFilesResponseOut": "_vision_317_BatchAnnotateFilesResponseOut",
        "EntityAnnotationIn": "_vision_318_EntityAnnotationIn",
        "EntityAnnotationOut": "_vision_319_EntityAnnotationOut",
        "GoogleCloudVisionV1p1beta1NormalizedVertexIn": "_vision_320_GoogleCloudVisionV1p1beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p1beta1NormalizedVertexOut": "_vision_321_GoogleCloudVisionV1p1beta1NormalizedVertexOut",
        "GoogleCloudVisionV1p2beta1OperationMetadataIn": "_vision_322_GoogleCloudVisionV1p2beta1OperationMetadataIn",
        "GoogleCloudVisionV1p2beta1OperationMetadataOut": "_vision_323_GoogleCloudVisionV1p2beta1OperationMetadataOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn": "_vision_324_GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut": "_vision_325_GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p4beta1VertexIn": "_vision_326_GoogleCloudVisionV1p4beta1VertexIn",
        "GoogleCloudVisionV1p4beta1VertexOut": "_vision_327_GoogleCloudVisionV1p4beta1VertexOut",
        "ListOperationsResponseIn": "_vision_328_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vision_329_ListOperationsResponseOut",
        "ImageAnnotationContextIn": "_vision_330_ImageAnnotationContextIn",
        "ImageAnnotationContextOut": "_vision_331_ImageAnnotationContextOut",
        "GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn": "_vision_332_GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut": "_vision_333_GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p1beta1VertexIn": "_vision_334_GoogleCloudVisionV1p1beta1VertexIn",
        "GoogleCloudVisionV1p1beta1VertexOut": "_vision_335_GoogleCloudVisionV1p1beta1VertexOut",
        "LocalizedObjectAnnotationIn": "_vision_336_LocalizedObjectAnnotationIn",
        "LocalizedObjectAnnotationOut": "_vision_337_LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn": "_vision_338_GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut": "_vision_339_GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p1beta1GcsDestinationIn": "_vision_340_GoogleCloudVisionV1p1beta1GcsDestinationIn",
        "GoogleCloudVisionV1p1beta1GcsDestinationOut": "_vision_341_GoogleCloudVisionV1p1beta1GcsDestinationOut",
        "OperationMetadataIn": "_vision_342_OperationMetadataIn",
        "OperationMetadataOut": "_vision_343_OperationMetadataOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebImageIn": "_vision_344_GoogleCloudVisionV1p2beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebImageOut": "_vision_345_GoogleCloudVisionV1p2beta1WebDetectionWebImageOut",
        "ColorIn": "_vision_346_ColorIn",
        "ColorOut": "_vision_347_ColorOut",
        "GoogleCloudVisionV1p4beta1ColorInfoIn": "_vision_348_GoogleCloudVisionV1p4beta1ColorInfoIn",
        "GoogleCloudVisionV1p4beta1ColorInfoOut": "_vision_349_GoogleCloudVisionV1p4beta1ColorInfoOut",
        "ImportProductSetsInputConfigIn": "_vision_350_ImportProductSetsInputConfigIn",
        "ImportProductSetsInputConfigOut": "_vision_351_ImportProductSetsInputConfigOut",
        "GoogleCloudVisionV1p4beta1ParagraphIn": "_vision_352_GoogleCloudVisionV1p4beta1ParagraphIn",
        "GoogleCloudVisionV1p4beta1ParagraphOut": "_vision_353_GoogleCloudVisionV1p4beta1ParagraphOut",
        "AsyncBatchAnnotateFilesRequestIn": "_vision_354_AsyncBatchAnnotateFilesRequestIn",
        "AsyncBatchAnnotateFilesRequestOut": "_vision_355_AsyncBatchAnnotateFilesRequestOut",
        "WebLabelIn": "_vision_356_WebLabelIn",
        "WebLabelOut": "_vision_357_WebLabelOut",
        "SafeSearchAnnotationIn": "_vision_358_SafeSearchAnnotationIn",
        "SafeSearchAnnotationOut": "_vision_359_SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p1beta1BlockIn": "_vision_360_GoogleCloudVisionV1p1beta1BlockIn",
        "GoogleCloudVisionV1p1beta1BlockOut": "_vision_361_GoogleCloudVisionV1p1beta1BlockOut",
        "GoogleCloudVisionV1p4beta1ImageAnnotationContextIn": "_vision_362_GoogleCloudVisionV1p4beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p4beta1ImageAnnotationContextOut": "_vision_363_GoogleCloudVisionV1p4beta1ImageAnnotationContextOut",
        "GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseIn": "_vision_364_GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseOut": "_vision_365_GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn": "_vision_366_GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut": "_vision_367_GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn": "_vision_368_GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut": "_vision_369_GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut",
        "AnnotateImageRequestIn": "_vision_370_AnnotateImageRequestIn",
        "AnnotateImageRequestOut": "_vision_371_AnnotateImageRequestOut",
        "BlockIn": "_vision_372_BlockIn",
        "BlockOut": "_vision_373_BlockOut",
        "WebImageIn": "_vision_374_WebImageIn",
        "WebImageOut": "_vision_375_WebImageOut",
        "GoogleCloudVisionV1p4beta1OutputConfigIn": "_vision_376_GoogleCloudVisionV1p4beta1OutputConfigIn",
        "GoogleCloudVisionV1p4beta1OutputConfigOut": "_vision_377_GoogleCloudVisionV1p4beta1OutputConfigOut",
        "GoogleCloudVisionV1p3beta1ImageAnnotationContextIn": "_vision_378_GoogleCloudVisionV1p3beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p3beta1ImageAnnotationContextOut": "_vision_379_GoogleCloudVisionV1p3beta1ImageAnnotationContextOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn": "_vision_380_GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut": "_vision_381_GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut",
        "GoogleCloudVisionV1p4beta1WebDetectionIn": "_vision_382_GoogleCloudVisionV1p4beta1WebDetectionIn",
        "GoogleCloudVisionV1p4beta1WebDetectionOut": "_vision_383_GoogleCloudVisionV1p4beta1WebDetectionOut",
        "ParagraphIn": "_vision_384_ParagraphIn",
        "ParagraphOut": "_vision_385_ParagraphOut",
        "GoogleCloudVisionV1p4beta1LocationInfoIn": "_vision_386_GoogleCloudVisionV1p4beta1LocationInfoIn",
        "GoogleCloudVisionV1p4beta1LocationInfoOut": "_vision_387_GoogleCloudVisionV1p4beta1LocationInfoOut",
        "GoogleCloudVisionV1p4beta1NormalizedVertexIn": "_vision_388_GoogleCloudVisionV1p4beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p4beta1NormalizedVertexOut": "_vision_389_GoogleCloudVisionV1p4beta1NormalizedVertexOut",
        "ProductSetIn": "_vision_390_ProductSetIn",
        "ProductSetOut": "_vision_391_ProductSetOut",
        "GoogleCloudVisionV1p4beta1BatchOperationMetadataIn": "_vision_392_GoogleCloudVisionV1p4beta1BatchOperationMetadataIn",
        "GoogleCloudVisionV1p4beta1BatchOperationMetadataOut": "_vision_393_GoogleCloudVisionV1p4beta1BatchOperationMetadataOut",
        "BatchAnnotateImagesRequestIn": "_vision_394_BatchAnnotateImagesRequestIn",
        "BatchAnnotateImagesRequestOut": "_vision_395_BatchAnnotateImagesRequestOut",
        "WebDetectionIn": "_vision_396_WebDetectionIn",
        "WebDetectionOut": "_vision_397_WebDetectionOut",
        "GoogleCloudVisionV1p1beta1ImageAnnotationContextIn": "_vision_398_GoogleCloudVisionV1p1beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p1beta1ImageAnnotationContextOut": "_vision_399_GoogleCloudVisionV1p1beta1ImageAnnotationContextOut",
        "GoogleCloudVisionV1p3beta1InputConfigIn": "_vision_400_GoogleCloudVisionV1p3beta1InputConfigIn",
        "GoogleCloudVisionV1p3beta1InputConfigOut": "_vision_401_GoogleCloudVisionV1p3beta1InputConfigOut",
        "GoogleCloudVisionV1p1beta1PositionIn": "_vision_402_GoogleCloudVisionV1p1beta1PositionIn",
        "GoogleCloudVisionV1p1beta1PositionOut": "_vision_403_GoogleCloudVisionV1p1beta1PositionOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationIn": "_vision_404_GoogleCloudVisionV1p4beta1TextAnnotationIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationOut": "_vision_405_GoogleCloudVisionV1p4beta1TextAnnotationOut",
        "GoogleCloudVisionV1p1beta1CropHintIn": "_vision_406_GoogleCloudVisionV1p1beta1CropHintIn",
        "GoogleCloudVisionV1p1beta1CropHintOut": "_vision_407_GoogleCloudVisionV1p1beta1CropHintOut",
        "GoogleCloudVisionV1p2beta1LocationInfoIn": "_vision_408_GoogleCloudVisionV1p2beta1LocationInfoIn",
        "GoogleCloudVisionV1p2beta1LocationInfoOut": "_vision_409_GoogleCloudVisionV1p2beta1LocationInfoOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebPageIn": "_vision_410_GoogleCloudVisionV1p1beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebPageOut": "_vision_411_GoogleCloudVisionV1p1beta1WebDetectionWebPageOut",
        "TextPropertyIn": "_vision_412_TextPropertyIn",
        "TextPropertyOut": "_vision_413_TextPropertyOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn": "_vision_414_GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut": "_vision_415_GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut",
        "PositionIn": "_vision_416_PositionIn",
        "PositionOut": "_vision_417_PositionOut",
        "BatchOperationMetadataIn": "_vision_418_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_vision_419_BatchOperationMetadataOut",
        "AddProductToProductSetRequestIn": "_vision_420_AddProductToProductSetRequestIn",
        "AddProductToProductSetRequestOut": "_vision_421_AddProductToProductSetRequestOut",
        "GoogleCloudVisionV1p2beta1WebDetectionIn": "_vision_422_GoogleCloudVisionV1p2beta1WebDetectionIn",
        "GoogleCloudVisionV1p2beta1WebDetectionOut": "_vision_423_GoogleCloudVisionV1p2beta1WebDetectionOut",
        "GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn": "_vision_424_GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut": "_vision_425_GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p2beta1SymbolIn": "_vision_426_GoogleCloudVisionV1p2beta1SymbolIn",
        "GoogleCloudVisionV1p2beta1SymbolOut": "_vision_427_GoogleCloudVisionV1p2beta1SymbolOut",
        "GoogleCloudVisionV1p1beta1ProductKeyValueIn": "_vision_428_GoogleCloudVisionV1p1beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p1beta1ProductKeyValueOut": "_vision_429_GoogleCloudVisionV1p1beta1ProductKeyValueOut",
        "GoogleCloudVisionV1p3beta1PositionIn": "_vision_430_GoogleCloudVisionV1p3beta1PositionIn",
        "GoogleCloudVisionV1p3beta1PositionOut": "_vision_431_GoogleCloudVisionV1p3beta1PositionOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn": "_vision_432_GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut": "_vision_433_GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebPageIn": "_vision_434_GoogleCloudVisionV1p4beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebPageOut": "_vision_435_GoogleCloudVisionV1p4beta1WebDetectionWebPageOut",
        "FeatureIn": "_vision_436_FeatureIn",
        "FeatureOut": "_vision_437_FeatureOut",
        "CancelOperationRequestIn": "_vision_438_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vision_439_CancelOperationRequestOut",
        "ListProductsInProductSetResponseIn": "_vision_440_ListProductsInProductSetResponseIn",
        "ListProductsInProductSetResponseOut": "_vision_441_ListProductsInProductSetResponseOut",
        "GoogleCloudVisionV1p1beta1LocationInfoIn": "_vision_442_GoogleCloudVisionV1p1beta1LocationInfoIn",
        "GoogleCloudVisionV1p1beta1LocationInfoOut": "_vision_443_GoogleCloudVisionV1p1beta1LocationInfoOut",
        "GoogleCloudVisionV1p3beta1VertexIn": "_vision_444_GoogleCloudVisionV1p3beta1VertexIn",
        "GoogleCloudVisionV1p3beta1VertexOut": "_vision_445_GoogleCloudVisionV1p3beta1VertexOut",
        "GoogleCloudVisionV1p3beta1WebDetectionIn": "_vision_446_GoogleCloudVisionV1p3beta1WebDetectionIn",
        "GoogleCloudVisionV1p3beta1WebDetectionOut": "_vision_447_GoogleCloudVisionV1p3beta1WebDetectionOut",
        "ProductIn": "_vision_448_ProductIn",
        "ProductOut": "_vision_449_ProductOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn": "_vision_450_GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut": "_vision_451_GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut",
        "GoogleCloudVisionV1p4beta1PageIn": "_vision_452_GoogleCloudVisionV1p4beta1PageIn",
        "GoogleCloudVisionV1p4beta1PageOut": "_vision_453_GoogleCloudVisionV1p4beta1PageOut",
        "AnnotateFileRequestIn": "_vision_454_AnnotateFileRequestIn",
        "AnnotateFileRequestOut": "_vision_455_AnnotateFileRequestOut",
        "GoogleCloudVisionV1p3beta1WordIn": "_vision_456_GoogleCloudVisionV1p3beta1WordIn",
        "GoogleCloudVisionV1p3beta1WordOut": "_vision_457_GoogleCloudVisionV1p3beta1WordOut",
        "GoogleCloudVisionV1p2beta1AnnotateFileResponseIn": "_vision_458_GoogleCloudVisionV1p2beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p2beta1AnnotateFileResponseOut": "_vision_459_GoogleCloudVisionV1p2beta1AnnotateFileResponseOut",
        "GoogleCloudVisionV1p2beta1EntityAnnotationIn": "_vision_460_GoogleCloudVisionV1p2beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p2beta1EntityAnnotationOut": "_vision_461_GoogleCloudVisionV1p2beta1EntityAnnotationOut",
        "DetectedLanguageIn": "_vision_462_DetectedLanguageIn",
        "DetectedLanguageOut": "_vision_463_DetectedLanguageOut",
        "ListProductSetsResponseIn": "_vision_464_ListProductSetsResponseIn",
        "ListProductSetsResponseOut": "_vision_465_ListProductSetsResponseOut",
        "GoogleCloudVisionV1p2beta1ProductKeyValueIn": "_vision_466_GoogleCloudVisionV1p2beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p2beta1ProductKeyValueOut": "_vision_467_GoogleCloudVisionV1p2beta1ProductKeyValueOut",
        "ImportProductSetsRequestIn": "_vision_468_ImportProductSetsRequestIn",
        "ImportProductSetsRequestOut": "_vision_469_ImportProductSetsRequestOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebImageIn": "_vision_470_GoogleCloudVisionV1p4beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebImageOut": "_vision_471_GoogleCloudVisionV1p4beta1WebDetectionWebImageOut",
        "GoogleCloudVisionV1p3beta1OutputConfigIn": "_vision_472_GoogleCloudVisionV1p3beta1OutputConfigIn",
        "GoogleCloudVisionV1p3beta1OutputConfigOut": "_vision_473_GoogleCloudVisionV1p3beta1OutputConfigOut",
        "LatLongRectIn": "_vision_474_LatLongRectIn",
        "LatLongRectOut": "_vision_475_LatLongRectOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn": "_vision_476_GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut": "_vision_477_GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p3beta1LocationInfoIn": "_vision_478_GoogleCloudVisionV1p3beta1LocationInfoIn",
        "GoogleCloudVisionV1p3beta1LocationInfoOut": "_vision_479_GoogleCloudVisionV1p3beta1LocationInfoOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn": "_vision_480_GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut": "_vision_481_GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut",
        "GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseIn": "_vision_482_GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseOut": "_vision_483_GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p2beta1AnnotateImageResponseIn": "_vision_484_GoogleCloudVisionV1p2beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p2beta1AnnotateImageResponseOut": "_vision_485_GoogleCloudVisionV1p2beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn": "_vision_486_GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut": "_vision_487_GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn": "_vision_488_GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut": "_vision_489_GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p1beta1FaceAnnotationIn": "_vision_490_GoogleCloudVisionV1p1beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p1beta1FaceAnnotationOut": "_vision_491_GoogleCloudVisionV1p1beta1FaceAnnotationOut",
        "LandmarkIn": "_vision_492_LandmarkIn",
        "LandmarkOut": "_vision_493_LandmarkOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn": "_vision_494_GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut": "_vision_495_GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p1beta1PropertyIn": "_vision_496_GoogleCloudVisionV1p1beta1PropertyIn",
        "GoogleCloudVisionV1p1beta1PropertyOut": "_vision_497_GoogleCloudVisionV1p1beta1PropertyOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn": "_vision_498_GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut": "_vision_499_GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsIn": "_vision_500_GoogleCloudVisionV1p3beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsOut": "_vision_501_GoogleCloudVisionV1p3beta1ProductSearchResultsOut",
        "ReferenceImageIn": "_vision_502_ReferenceImageIn",
        "ReferenceImageOut": "_vision_503_ReferenceImageOut",
        "GoogleCloudVisionV1p4beta1OperationMetadataIn": "_vision_504_GoogleCloudVisionV1p4beta1OperationMetadataIn",
        "GoogleCloudVisionV1p4beta1OperationMetadataOut": "_vision_505_GoogleCloudVisionV1p4beta1OperationMetadataOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationIn": "_vision_506_GoogleCloudVisionV1p1beta1TextAnnotationIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationOut": "_vision_507_GoogleCloudVisionV1p1beta1TextAnnotationOut",
        "GoogleCloudVisionV1p2beta1GcsSourceIn": "_vision_508_GoogleCloudVisionV1p2beta1GcsSourceIn",
        "GoogleCloudVisionV1p2beta1GcsSourceOut": "_vision_509_GoogleCloudVisionV1p2beta1GcsSourceOut",
        "GoogleCloudVisionV1p3beta1PropertyIn": "_vision_510_GoogleCloudVisionV1p3beta1PropertyIn",
        "GoogleCloudVisionV1p3beta1PropertyOut": "_vision_511_GoogleCloudVisionV1p3beta1PropertyOut",
        "WebDetectionParamsIn": "_vision_512_WebDetectionParamsIn",
        "WebDetectionParamsOut": "_vision_513_WebDetectionParamsOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsIn": "_vision_514_GoogleCloudVisionV1p2beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsOut": "_vision_515_GoogleCloudVisionV1p2beta1ProductSearchResultsOut",
        "CropHintsAnnotationIn": "_vision_516_CropHintsAnnotationIn",
        "CropHintsAnnotationOut": "_vision_517_CropHintsAnnotationOut",
        "PropertyIn": "_vision_518_PropertyIn",
        "PropertyOut": "_vision_519_PropertyOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn": "_vision_520_GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut": "_vision_521_GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn": "_vision_522_GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut": "_vision_523_GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut",
        "SymbolIn": "_vision_524_SymbolIn",
        "SymbolOut": "_vision_525_SymbolOut",
        "GoogleCloudVisionV1p1beta1ParagraphIn": "_vision_526_GoogleCloudVisionV1p1beta1ParagraphIn",
        "GoogleCloudVisionV1p1beta1ParagraphOut": "_vision_527_GoogleCloudVisionV1p1beta1ParagraphOut",
        "AsyncBatchAnnotateImagesResponseIn": "_vision_528_AsyncBatchAnnotateImagesResponseIn",
        "AsyncBatchAnnotateImagesResponseOut": "_vision_529_AsyncBatchAnnotateImagesResponseOut",
        "GoogleCloudVisionV1p4beta1FaceRecognitionResultIn": "_vision_530_GoogleCloudVisionV1p4beta1FaceRecognitionResultIn",
        "GoogleCloudVisionV1p4beta1FaceRecognitionResultOut": "_vision_531_GoogleCloudVisionV1p4beta1FaceRecognitionResultOut",
        "GoogleCloudVisionV1p3beta1ProductIn": "_vision_532_GoogleCloudVisionV1p3beta1ProductIn",
        "GoogleCloudVisionV1p3beta1ProductOut": "_vision_533_GoogleCloudVisionV1p3beta1ProductOut",
        "GoogleCloudVisionV1p3beta1SymbolIn": "_vision_534_GoogleCloudVisionV1p3beta1SymbolIn",
        "GoogleCloudVisionV1p3beta1SymbolOut": "_vision_535_GoogleCloudVisionV1p3beta1SymbolOut",
        "ProductSearchParamsIn": "_vision_536_ProductSearchParamsIn",
        "ProductSearchParamsOut": "_vision_537_ProductSearchParamsOut",
        "GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseIn": "_vision_538_GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseOut": "_vision_539_GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p1beta1CropHintsAnnotationIn": "_vision_540_GoogleCloudVisionV1p1beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p1beta1CropHintsAnnotationOut": "_vision_541_GoogleCloudVisionV1p1beta1CropHintsAnnotationOut",
        "GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn": "_vision_542_GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut": "_vision_543_GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p2beta1PositionIn": "_vision_544_GoogleCloudVisionV1p2beta1PositionIn",
        "GoogleCloudVisionV1p2beta1PositionOut": "_vision_545_GoogleCloudVisionV1p2beta1PositionOut",
        "GoogleCloudVisionV1p2beta1VertexIn": "_vision_546_GoogleCloudVisionV1p2beta1VertexIn",
        "GoogleCloudVisionV1p2beta1VertexOut": "_vision_547_GoogleCloudVisionV1p2beta1VertexOut",
        "ResultIn": "_vision_548_ResultIn",
        "ResultOut": "_vision_549_ResultOut",
        "BatchAnnotateFilesRequestIn": "_vision_550_BatchAnnotateFilesRequestIn",
        "BatchAnnotateFilesRequestOut": "_vision_551_BatchAnnotateFilesRequestOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn": "_vision_552_GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut": "_vision_553_GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut",
        "ListProductsResponseIn": "_vision_554_ListProductsResponseIn",
        "ListProductsResponseOut": "_vision_555_ListProductsResponseOut",
        "GoogleCloudVisionV1p3beta1AnnotateFileResponseIn": "_vision_556_GoogleCloudVisionV1p3beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p3beta1AnnotateFileResponseOut": "_vision_557_GoogleCloudVisionV1p3beta1AnnotateFileResponseOut",
        "WebPageIn": "_vision_558_WebPageIn",
        "WebPageOut": "_vision_559_WebPageOut",
        "GoogleCloudVisionV1p2beta1ImagePropertiesIn": "_vision_560_GoogleCloudVisionV1p2beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p2beta1ImagePropertiesOut": "_vision_561_GoogleCloudVisionV1p2beta1ImagePropertiesOut",
        "GoogleCloudVisionV1p1beta1AnnotateFileResponseIn": "_vision_562_GoogleCloudVisionV1p1beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p1beta1AnnotateFileResponseOut": "_vision_563_GoogleCloudVisionV1p1beta1AnnotateFileResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusIn"])).optional(),
            "referenceImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ReferenceImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn"])
    types["GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "referenceImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ReferenceImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut"])
    types["GoogleCloudVisionV1p3beta1ParagraphIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WordIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ParagraphIn"])
    types["GoogleCloudVisionV1p3beta1ParagraphOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WordOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ParagraphOut"])
    types["GoogleCloudVisionV1p3beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p3beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1GcsDestinationOut"])
    types["GoogleCloudVisionV1p2beta1NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1NormalizedVertexIn"])
    types["GoogleCloudVisionV1p2beta1NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1NormalizedVertexOut"])
    types[
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut"]
    )
    types["LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["LocationInfoIn"])
    types["LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["GoogleCloudVisionV1p1beta1ProductIn"] = t.struct(
        {
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ProductKeyValueIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "productCategory": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductIn"])
    types["GoogleCloudVisionV1p1beta1ProductOut"] = t.struct(
        {
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ProductKeyValueOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "productCategory": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductOut"])
    types["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "violence": t.string().optional(),
            "adult": t.string().optional(),
            "spoof": t.string().optional(),
            "racy": t.string().optional(),
            "medical": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "violence": t.string().optional(),
            "adult": t.string().optional(),
            "spoof": t.string().optional(),
            "racy": t.string().optional(),
            "medical": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"])
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
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn"
                    ]
                )
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"]
                )
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
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"] = t.struct(
        {"score": t.number().optional(), "url": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"] = t.struct(
        {
            "score": t.number().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
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
    types["WordIn"] = t.struct(
        {
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "confidence": t.number().optional(),
            "symbols": t.array(t.proxy(renames["SymbolIn"])).optional(),
        }
    ).named(renames["WordIn"])
    types["WordOut"] = t.struct(
        {
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "confidence": t.number().optional(),
            "symbols": t.array(t.proxy(renames["SymbolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordOut"])
    types["GoogleCloudVisionV1p2beta1BlockIn"] = t.struct(
        {
            "blockType": t.string().optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ParagraphIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BlockIn"])
    types["GoogleCloudVisionV1p2beta1BlockOut"] = t.struct(
        {
            "blockType": t.string().optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ParagraphOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BlockOut"])
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
    types["ImportProductSetsResponseIn"] = t.struct(
        {
            "referenceImages": t.array(t.proxy(renames["ReferenceImageIn"])).optional(),
            "statuses": t.array(t.proxy(renames["StatusIn"])).optional(),
        }
    ).named(renames["ImportProductSetsResponseIn"])
    types["ImportProductSetsResponseOut"] = t.struct(
        {
            "referenceImages": t.array(
                t.proxy(renames["ReferenceImageOut"])
            ).optional(),
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsResponseOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebPageIn"] = t.struct(
        {
            "pageTitle": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "score": t.number().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebPageOut"] = t.struct(
        {
            "pageTitle": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "score": t.number().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageOut"])
    types["AsyncAnnotateFileRequestIn"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigIn"]),
            "imageContext": t.proxy(renames["ImageContextIn"]).optional(),
            "features": t.array(t.proxy(renames["FeatureIn"])),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
        }
    ).named(renames["AsyncAnnotateFileRequestIn"])
    types["AsyncAnnotateFileRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "imageContext": t.proxy(renames["ImageContextOut"]).optional(),
            "features": t.array(t.proxy(renames["FeatureOut"])),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncAnnotateFileRequestOut"])
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
    types["GoogleCloudVisionV1p4beta1SymbolIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SymbolIn"])
    types["GoogleCloudVisionV1p4beta1SymbolOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SymbolOut"])
    types["GoogleCloudVisionV1p4beta1ProductIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "productCategory": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ProductKeyValueIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductIn"])
    types["GoogleCloudVisionV1p4beta1ProductOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "productCategory": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ProductKeyValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductOut"])
    types["TextDetectionParamsIn"] = t.struct(
        {
            "advancedOcrOptions": t.array(t.string()).optional(),
            "enableTextDetectionConfidenceScore": t.boolean().optional(),
        }
    ).named(renames["TextDetectionParamsIn"])
    types["TextDetectionParamsOut"] = t.struct(
        {
            "advancedOcrOptions": t.array(t.string()).optional(),
            "enableTextDetectionConfidenceScore": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextDetectionParamsOut"])
    types["GoogleCloudVisionV1p3beta1BlockIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "blockType": t.string().optional(),
            "confidence": t.number().optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ParagraphIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BlockIn"])
    types["GoogleCloudVisionV1p3beta1BlockOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "blockType": t.string().optional(),
            "confidence": t.number().optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ParagraphOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BlockOut"])
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
    types["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"] = t.struct(
        {
            "url": t.string().optional(),
            "pageTitle": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "score": t.number().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "pageTitle": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "score": t.number().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"])
    types["ColorInfoIn"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["ColorInfoIn"])
    types["ColorInfoOut"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorInfoOut"])
    types["GoogleCloudVisionV1p1beta1PageIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1BlockIn"])
            ).optional(),
            "height": t.integer().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PageIn"])
    types["GoogleCloudVisionV1p1beta1PageOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1BlockOut"])
            ).optional(),
            "height": t.integer().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PageOut"])
    types["GoogleCloudVisionV1p3beta1CropHintIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "importanceFraction": t.number().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1CropHintIn"])
    types["GoogleCloudVisionV1p3beta1CropHintOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "importanceFraction": t.number().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1CropHintOut"])
    types["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"] = t.struct(
        {
            "context": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductSearchResultsIn"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationIn"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImagePropertiesIn"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1CropHintsAnnotationIn"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p4beta1WebDetectionIn"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationIn"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"] = t.struct(
        {
            "context": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductSearchResultsOut"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationOut"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImagePropertiesOut"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1CropHintsAnnotationOut"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p4beta1WebDetectionOut"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationOut"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"])
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
    types["GoogleCloudVisionV1p2beta1PageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1BlockIn"])
            ).optional(),
            "width": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PageIn"])
    types["GoogleCloudVisionV1p2beta1PageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1BlockOut"])
            ).optional(),
            "width": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PageOut"])
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
    types["GoogleCloudVisionV1p4beta1BlockIn"] = t.struct(
        {
            "blockType": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ParagraphIn"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BlockIn"])
    types["GoogleCloudVisionV1p4beta1BlockOut"] = t.struct(
        {
            "blockType": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ParagraphOut"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BlockOut"])
    types["GoogleCloudVisionV1p1beta1EntityAnnotationIn"] = t.struct(
        {
            "description": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "topicality": t.number().optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1LocationInfoIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "locale": t.string().optional(),
            "score": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PropertyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1EntityAnnotationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "topicality": t.number().optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1LocationInfoOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "locale": t.string().optional(),
            "score": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
    types["GoogleCloudVisionV1p3beta1ReferenceImageIn"] = t.struct(
        {
            "uri": t.string(),
            "name": t.string().optional(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ReferenceImageIn"])
    types["GoogleCloudVisionV1p3beta1ReferenceImageOut"] = t.struct(
        {
            "uri": t.string(),
            "name": t.string().optional(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ReferenceImageOut"])
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
    types["ProductSetPurgeConfigIn"] = t.struct(
        {"productSetId": t.string().optional()}
    ).named(renames["ProductSetPurgeConfigIn"])
    types["ProductSetPurgeConfigOut"] = t.struct(
        {
            "productSetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSetPurgeConfigOut"])
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
    types["GoogleCloudVisionV1p2beta1ParagraphIn"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WordIn"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ParagraphIn"])
    types["GoogleCloudVisionV1p2beta1ParagraphOut"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WordOut"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ParagraphOut"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationIn"] = t.struct(
        {
            "angerLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "tiltAngle": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "headwearLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationOut"] = t.struct(
        {
            "angerLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "tiltAngle": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "headwearLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1ColorInfoIn"] = t.struct(
        {
            "score": t.number().optional(),
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p2beta1ColorInfoOut"] = t.struct(
        {
            "score": t.number().optional(),
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ColorInfoOut"])
    types["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"])
    types["OutputConfigIn"] = t.struct(
        {
            "batchSize": t.integer().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
        }
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "batchSize": t.integer().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["PageIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "width": t.integer().optional(),
            "blocks": t.array(t.proxy(renames["BlockIn"])).optional(),
            "height": t.integer().optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "width": t.integer().optional(),
            "blocks": t.array(t.proxy(renames["BlockOut"])).optional(),
            "height": t.integer().optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["GoogleCloudVisionV1p3beta1ProductKeyValueIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1ProductKeyValueIn"])
    types["GoogleCloudVisionV1p3beta1ProductKeyValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductKeyValueOut"])
    types["ImageContextIn"] = t.struct(
        {
            "textDetectionParams": t.proxy(renames["TextDetectionParamsIn"]).optional(),
            "languageHints": t.array(t.string()).optional(),
            "latLongRect": t.proxy(renames["LatLongRectIn"]).optional(),
            "webDetectionParams": t.proxy(renames["WebDetectionParamsIn"]).optional(),
            "productSearchParams": t.proxy(renames["ProductSearchParamsIn"]).optional(),
            "cropHintsParams": t.proxy(renames["CropHintsParamsIn"]).optional(),
        }
    ).named(renames["ImageContextIn"])
    types["ImageContextOut"] = t.struct(
        {
            "textDetectionParams": t.proxy(
                renames["TextDetectionParamsOut"]
            ).optional(),
            "languageHints": t.array(t.string()).optional(),
            "latLongRect": t.proxy(renames["LatLongRectOut"]).optional(),
            "webDetectionParams": t.proxy(renames["WebDetectionParamsOut"]).optional(),
            "productSearchParams": t.proxy(
                renames["ProductSearchParamsOut"]
            ).optional(),
            "cropHintsParams": t.proxy(renames["CropHintsParamsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageContextOut"])
    types["AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "responses": t.array(
                t.proxy(renames["AnnotateImageResponseIn"])
            ).optional(),
            "inputConfig": t.proxy(renames["InputConfigIn"]).optional(),
            "totalPages": t.integer().optional(),
        }
    ).named(renames["AnnotateFileResponseIn"])
    types["AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "responses": t.array(
                t.proxy(renames["AnnotateImageResponseOut"])
            ).optional(),
            "inputConfig": t.proxy(renames["InputConfigOut"]).optional(),
            "totalPages": t.integer().optional(),
        }
    ).named(renames["AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
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
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut"] = t.struct(
        {
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
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "product": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductIn"]
            ).optional(),
            "image": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "product": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductOut"]
            ).optional(),
            "image": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"])
    types["GoogleCloudVisionV1p2beta1ProductIn"] = t.struct(
        {
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ProductKeyValueIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductIn"])
    types["GoogleCloudVisionV1p2beta1ProductOut"] = t.struct(
        {
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ProductKeyValueOut"])
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductOut"])
    types["GoogleCloudVisionV1p4beta1CelebrityIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CelebrityIn"])
    types["GoogleCloudVisionV1p4beta1CelebrityOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CelebrityOut"])
    types["GoogleCloudVisionV1p4beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p4beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1GcsDestinationOut"])
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
    types["GoogleCloudVisionV1p4beta1EntityAnnotationIn"] = t.struct(
        {
            "topicality": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "locale": t.string().optional(),
            "confidence": t.number().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PropertyIn"])
            ).optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1LocationInfoIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1EntityAnnotationOut"] = t.struct(
        {
            "topicality": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "locale": t.string().optional(),
            "confidence": t.number().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PropertyOut"])
            ).optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1LocationInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
    types["AnnotateImageResponseIn"] = t.struct(
        {
            "labelAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "context": t.proxy(renames["ImageAnnotationContextIn"]).optional(),
            "cropHintsAnnotation": t.proxy(renames["CropHintsAnnotationIn"]).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(renames["LocalizedObjectAnnotationIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["ImagePropertiesIn"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "webDetection": t.proxy(renames["WebDetectionIn"]).optional(),
            "productSearchResults": t.proxy(
                renames["ProductSearchResultsIn"]
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["SafeSearchAnnotationIn"]
            ).optional(),
            "faceAnnotations": t.array(t.proxy(renames["FaceAnnotationIn"])).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "fullTextAnnotation": t.proxy(renames["TextAnnotationIn"]).optional(),
        }
    ).named(renames["AnnotateImageResponseIn"])
    types["AnnotateImageResponseOut"] = t.struct(
        {
            "labelAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "context": t.proxy(renames["ImageAnnotationContextOut"]).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["CropHintsAnnotationOut"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(renames["LocalizedObjectAnnotationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["ImagePropertiesOut"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "webDetection": t.proxy(renames["WebDetectionOut"]).optional(),
            "productSearchResults": t.proxy(
                renames["ProductSearchResultsOut"]
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["SafeSearchAnnotationOut"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["FaceAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "fullTextAnnotation": t.proxy(renames["TextAnnotationOut"]).optional(),
        }
    ).named(renames["AnnotateImageResponseOut"])
    types["ListReferenceImagesResponseIn"] = t.struct(
        {
            "referenceImages": t.array(t.proxy(renames["ReferenceImageIn"])).optional(),
            "pageSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReferenceImagesResponseIn"])
    types["ListReferenceImagesResponseOut"] = t.struct(
        {
            "referenceImages": t.array(
                t.proxy(renames["ReferenceImageOut"])
            ).optional(),
            "pageSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReferenceImagesResponseOut"])
    types["GoogleCloudVisionV1p3beta1EntityAnnotationIn"] = t.struct(
        {
            "mid": t.string().optional(),
            "confidence": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PropertyIn"])
            ).optional(),
            "description": t.string().optional(),
            "score": t.number().optional(),
            "topicality": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1LocationInfoIn"])
            ).optional(),
            "locale": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1EntityAnnotationOut"] = t.struct(
        {
            "mid": t.string().optional(),
            "confidence": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PropertyOut"])
            ).optional(),
            "description": t.string().optional(),
            "score": t.number().optional(),
            "topicality": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1LocationInfoOut"])
            ).optional(),
            "locale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
    types["AsyncBatchAnnotateImagesRequestIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
        }
    ).named(renames["AsyncBatchAnnotateImagesRequestIn"])
    types["AsyncBatchAnnotateImagesRequestOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "requests": t.array(t.proxy(renames["AnnotateImageRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateImagesRequestOut"])
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
    types["GoogleCloudVisionV1p1beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p1beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1GcsSourceOut"])
    types["GoogleCloudVisionV1p3beta1ColorInfoIn"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p3beta1ColorInfoOut"] = t.struct(
        {
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ColorInfoOut"])
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
    types["BoundingPolyIn"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["NormalizedVertexIn"])
            ).optional(),
            "vertices": t.array(t.proxy(renames["VertexIn"])).optional(),
        }
    ).named(renames["BoundingPolyIn"])
    types["BoundingPolyOut"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["NormalizedVertexOut"])
            ).optional(),
            "vertices": t.array(t.proxy(renames["VertexOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BoundingPolyOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn"] = t.struct(
        {
            "position": t.proxy(
                renames["GoogleCloudVisionV1p1beta1PositionIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn"])
    types["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut"] = t.struct(
        {
            "position": t.proxy(
                renames["GoogleCloudVisionV1p1beta1PositionOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsSourceOut"])
    types["ProductSearchResultsIn"] = t.struct(
        {
            "indexTime": t.string().optional(),
            "productGroupedResults": t.array(
                t.proxy(renames["GroupedResultIn"])
            ).optional(),
            "results": t.array(t.proxy(renames["ResultIn"])).optional(),
        }
    ).named(renames["ProductSearchResultsIn"])
    types["ProductSearchResultsOut"] = t.struct(
        {
            "indexTime": t.string().optional(),
            "productGroupedResults": t.array(
                t.proxy(renames["GroupedResultOut"])
            ).optional(),
            "results": t.array(t.proxy(renames["ResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSearchResultsOut"])
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
    types["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"]
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p3beta1WebDetectionIn"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1CropHintsAnnotationIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductSearchResultsIn"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationIn"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationIn"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImagePropertiesIn"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"]
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p3beta1WebDetectionOut"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1CropHintsAnnotationOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductSearchResultsOut"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationOut"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationOut"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImagePropertiesOut"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p3beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p3beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1GcsSourceOut"])
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
    types["GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusIn"])).optional(),
            "referenceImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ReferenceImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn"])
    types["GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "referenceImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ReferenceImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut"])
    types["ObjectAnnotationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "mid": t.string().optional(),
        }
    ).named(renames["ObjectAnnotationIn"])
    types["ObjectAnnotationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectAnnotationOut"])
    types["GoogleCloudVisionV1p3beta1PageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BlockIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "width": t.integer().optional(),
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
            "confidence": t.number().optional(),
            "width": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PageOut"])
    types["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "spoof": t.string().optional(),
            "racy": t.string().optional(),
            "violence": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "spoof": t.string().optional(),
            "racy": t.string().optional(),
            "violence": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"])
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
    types["GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn"] = t.struct(
        {"label": t.string().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut"])
    types["GoogleCloudVisionV1p1beta1OperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p1beta1OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1OperationMetadataOut"])
    types[
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut"]
    )
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
    types["ImageSourceIn"] = t.struct(
        {"gcsImageUri": t.string().optional(), "imageUri": t.string().optional()}
    ).named(renames["ImageSourceIn"])
    types["ImageSourceOut"] = t.struct(
        {
            "gcsImageUri": t.string().optional(),
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageSourceOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "score": t.number().optional(),
            "description": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "score": t.number().optional(),
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"])
    types["GoogleCloudVisionV1p1beta1SymbolIn"] = t.struct(
        {
            "text": t.string().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SymbolIn"])
    types["GoogleCloudVisionV1p1beta1SymbolOut"] = t.struct(
        {
            "text": t.string().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SymbolOut"])
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
    types["GoogleCloudVisionV1p2beta1InputConfigIn"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsSourceIn"]
            ).optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1InputConfigIn"])
    types["GoogleCloudVisionV1p2beta1InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsSourceOut"]
            ).optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1InputConfigOut"])
    types["InputConfigIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceIn"]).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["InputConfigIn"])
    types["InputConfigOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputConfigOut"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "rollAngle": t.number().optional(),
            "tiltAngle": t.number().optional(),
            "panAngle": t.number().optional(),
            "joyLikelihood": t.string().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "surpriseLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "blurredLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "recognitionResult": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceRecognitionResultIn"])
            ).optional(),
            "sorrowLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "rollAngle": t.number().optional(),
            "tiltAngle": t.number().optional(),
            "panAngle": t.number().optional(),
            "joyLikelihood": t.string().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "surpriseLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "blurredLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "recognitionResult": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceRecognitionResultOut"])
            ).optional(),
            "sorrowLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationOut"])
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
    types["GoogleCloudVisionV1p3beta1NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1NormalizedVertexIn"])
    types["GoogleCloudVisionV1p3beta1NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1NormalizedVertexOut"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"])
    types["GoogleCloudVisionV1p4beta1PropertyIn"] = t.struct(
        {
            "value": t.string().optional(),
            "uint64Value": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PropertyIn"])
    types["GoogleCloudVisionV1p4beta1PropertyOut"] = t.struct(
        {
            "value": t.string().optional(),
            "uint64Value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PropertyOut"])
    types["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudVisionV1p2beta1PositionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudVisionV1p2beta1PositionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"])
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
    types["GoogleCloudVisionV1p4beta1AnnotateFileResponseIn"] = t.struct(
        {
            "totalPages": t.integer().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1InputConfigIn"]
            ).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p4beta1AnnotateFileResponseOut"] = t.struct(
        {
            "totalPages": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1InputConfigOut"]
            ).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateFileResponseOut"])
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
    types["PurgeProductsRequestIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "productSetPurgeConfig": t.proxy(
                renames["ProductSetPurgeConfigIn"]
            ).optional(),
            "deleteOrphanProducts": t.boolean().optional(),
        }
    ).named(renames["PurgeProductsRequestIn"])
    types["PurgeProductsRequestOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "productSetPurgeConfig": t.proxy(
                renames["ProductSetPurgeConfigOut"]
            ).optional(),
            "deleteOrphanProducts": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PurgeProductsRequestOut"])
    types["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "racy": t.string().optional(),
            "medical": t.string().optional(),
            "violence": t.string().optional(),
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "racy": t.string().optional(),
            "medical": t.string().optional(),
            "violence": t.string().optional(),
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1ColorInfoIn"] = t.struct(
        {
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "pixelFraction": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p1beta1ColorInfoOut"] = t.struct(
        {
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "pixelFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ColorInfoOut"])
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
    types["DominantColorsAnnotationIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ColorInfoIn"])).optional()}
    ).named(renames["DominantColorsAnnotationIn"])
    types["DominantColorsAnnotationOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ColorInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DominantColorsAnnotationOut"])
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
    types["CropHintsParamsIn"] = t.struct(
        {"aspectRatios": t.array(t.number()).optional()}
    ).named(renames["CropHintsParamsIn"])
    types["CropHintsParamsOut"] = t.struct(
        {
            "aspectRatios": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropHintsParamsOut"])
    types["GoogleCloudVisionV1p4beta1CropHintIn"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CropHintIn"])
    types["GoogleCloudVisionV1p4beta1CropHintOut"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CropHintOut"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"])
    types["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "violence": t.string().optional(),
            "medical": t.string().optional(),
            "adult": t.string().optional(),
            "racy": t.string().optional(),
            "spoof": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "violence": t.string().optional(),
            "medical": t.string().optional(),
            "adult": t.string().optional(),
            "racy": t.string().optional(),
            "spoof": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"])
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
    types["AsyncAnnotateFileResponseIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"]).optional()}
    ).named(renames["AsyncAnnotateFileResponseIn"])
    types["AsyncAnnotateFileResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncAnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p3beta1BatchOperationMetadataIn"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BatchOperationMetadataIn"])
    types["GoogleCloudVisionV1p3beta1BatchOperationMetadataOut"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BatchOperationMetadataOut"])
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
    types["FaceAnnotationIn"] = t.struct(
        {
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "landmarkingConfidence": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "fdBoundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "headwearLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "landmarks": t.array(t.proxy(renames["LandmarkIn"])).optional(),
            "panAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "joyLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
        }
    ).named(renames["FaceAnnotationIn"])
    types["FaceAnnotationOut"] = t.struct(
        {
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "landmarkingConfidence": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "fdBoundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "headwearLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "landmarks": t.array(t.proxy(renames["LandmarkOut"])).optional(),
            "panAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "joyLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FaceAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1InputConfigIn"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p1beta1GcsSourceIn"]
            ).optional(),
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1InputConfigIn"])
    types["GoogleCloudVisionV1p1beta1InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p1beta1GcsSourceOut"]
            ).optional(),
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1InputConfigOut"])
    types["ImportProductSetsGcsSourceIn"] = t.struct(
        {"csvFileUri": t.string().optional()}
    ).named(renames["ImportProductSetsGcsSourceIn"])
    types["ImportProductSetsGcsSourceOut"] = t.struct(
        {
            "csvFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsGcsSourceOut"])
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
    types["GoogleCloudVisionV1p2beta1PropertyIn"] = t.struct(
        {
            "uint64Value": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PropertyIn"])
    types["GoogleCloudVisionV1p2beta1PropertyOut"] = t.struct(
        {
            "uint64Value": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PropertyOut"])
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
    types["GoogleCloudVisionV1p2beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p2beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1GcsDestinationOut"])
    types["GoogleCloudVisionV1p4beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p4beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1GcsSourceOut"])
    types[
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut"]
    )
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
    types["GoogleCloudVisionV1p3beta1FaceAnnotationIn"] = t.struct(
        {
            "headwearLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "surpriseLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "angerLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "rollAngle": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1FaceAnnotationOut"] = t.struct(
        {
            "headwearLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "surpriseLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "angerLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "sorrowLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "rollAngle": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationOut"])
    types["WebEntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["WebEntityIn"])
    types["WebEntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebEntityOut"])
    types["GoogleCloudVisionV1p4beta1WordIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1SymbolIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WordIn"])
    types["GoogleCloudVisionV1p4beta1WordOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1SymbolOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WordOut"])
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
    types["GoogleCloudVisionV1p2beta1WordIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1SymbolIn"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WordIn"])
    types["GoogleCloudVisionV1p2beta1WordOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1SymbolOut"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WordOut"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn"] = t.struct(
        {"languageCode": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut"])
    types["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"])
    types["GoogleCloudVisionV1p3beta1BoundingPolyIn"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1NormalizedVertexIn"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1VertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"])
    types["GoogleCloudVisionV1p3beta1BoundingPolyOut"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1NormalizedVertexOut"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1VertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"])
    types["LatLngIn"] = t.struct(
        {"longitude": t.number().optional(), "latitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["GoogleCloudVisionV1p4beta1ReferenceImageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "uri": t.string(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ReferenceImageIn"])
    types["GoogleCloudVisionV1p4beta1ReferenceImageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "uri": t.string(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ReferenceImageOut"])
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
    types["GoogleCloudVisionV1p1beta1WebDetectionIn"] = t.struct(
        {
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionOut"] = t.struct(
        {
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionOut"])
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
    types["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn"] = t.struct(
        {"isPrefix": t.boolean().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut"] = t.struct(
        {
            "isPrefix": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut"])
    types["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"] = t.struct(
        {
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1CropHintsAnnotationIn"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationIn"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImagePropertiesIn"]
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p1beta1WebDetectionIn"]
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"] = t.struct(
        {
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1CropHintsAnnotationOut"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationOut"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImagePropertiesOut"]
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p1beta1WebDetectionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationIn"] = t.struct(
        {
            "text": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationOut"] = t.struct(
        {
            "text": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "score": t.number().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "score": t.number().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut"])
    types["RemoveProductFromProductSetRequestIn"] = t.struct(
        {"product": t.string()}
    ).named(renames["RemoveProductFromProductSetRequestIn"])
    types["RemoveProductFromProductSetRequestOut"] = t.struct(
        {"product": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveProductFromProductSetRequestOut"])
    types["GcsDestinationIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["GoogleCloudVisionV1p2beta1ImageAnnotationContextIn"] = t.struct(
        {"uri": t.string().optional(), "pageNumber": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextIn"])
    types["GoogleCloudVisionV1p2beta1ImageAnnotationContextOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "pageNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextOut"])
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
    types["EntityAnnotationIn"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["PropertyIn"])).optional(),
            "description": t.string().optional(),
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "locale": t.string().optional(),
            "score": t.number().optional(),
            "confidence": t.number().optional(),
            "locations": t.array(t.proxy(renames["LocationInfoIn"])).optional(),
            "topicality": t.number().optional(),
        }
    ).named(renames["EntityAnnotationIn"])
    types["EntityAnnotationOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["PropertyOut"])).optional(),
            "description": t.string().optional(),
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "locale": t.string().optional(),
            "score": t.number().optional(),
            "confidence": t.number().optional(),
            "locations": t.array(t.proxy(renames["LocationInfoOut"])).optional(),
            "topicality": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1NormalizedVertexIn"])
    types["GoogleCloudVisionV1p1beta1NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1NormalizedVertexOut"])
    types["GoogleCloudVisionV1p2beta1OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p2beta1OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1OperationMetadataOut"])
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
    types["ImageAnnotationContextIn"] = t.struct(
        {"uri": t.string().optional(), "pageNumber": t.integer().optional()}
    ).named(renames["ImageAnnotationContextIn"])
    types["ImageAnnotationContextOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "pageNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageAnnotationContextOut"])
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
    types["LocalizedObjectAnnotationIn"] = t.struct(
        {
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocalizedObjectAnnotationIn"])
    types["LocalizedObjectAnnotationOut"] = t.struct(
        {
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedObjectAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut"])
    types["GoogleCloudVisionV1p1beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p1beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1GcsDestinationOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"] = t.struct(
        {"url": t.string().optional(), "score": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
    types["ColorIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["GoogleCloudVisionV1p4beta1ColorInfoIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "pixelFraction": t.number().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p4beta1ColorInfoOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "pixelFraction": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ColorInfoOut"])
    types["ImportProductSetsInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportProductSetsGcsSourceIn"]).optional()}
    ).named(renames["ImportProductSetsInputConfigIn"])
    types["ImportProductSetsInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportProductSetsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsInputConfigOut"])
    types["GoogleCloudVisionV1p4beta1ParagraphIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WordIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ParagraphIn"])
    types["GoogleCloudVisionV1p4beta1ParagraphOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ParagraphOut"])
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
    types["WebLabelIn"] = t.struct(
        {"label": t.string().optional(), "languageCode": t.string().optional()}
    ).named(renames["WebLabelIn"])
    types["WebLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebLabelOut"])
    types["SafeSearchAnnotationIn"] = t.struct(
        {
            "adult": t.string().optional(),
            "violence": t.string().optional(),
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "spoof": t.string().optional(),
        }
    ).named(renames["SafeSearchAnnotationIn"])
    types["SafeSearchAnnotationOut"] = t.struct(
        {
            "adult": t.string().optional(),
            "violence": t.string().optional(),
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "spoof": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeSearchAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1BlockIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ParagraphIn"])
            ).optional(),
            "blockType": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1BlockIn"])
    types["GoogleCloudVisionV1p1beta1BlockOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ParagraphOut"])
            ).optional(),
            "blockType": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1BlockOut"])
    types["GoogleCloudVisionV1p4beta1ImageAnnotationContextIn"] = t.struct(
        {"uri": t.string().optional(), "pageNumber": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextIn"])
    types["GoogleCloudVisionV1p4beta1ImageAnnotationContextOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "pageNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextOut"])
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
    types["BlockIn"] = t.struct(
        {
            "blockType": t.string().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "paragraphs": t.array(t.proxy(renames["ParagraphIn"])).optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["BlockIn"])
    types["BlockOut"] = t.struct(
        {
            "blockType": t.string().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "paragraphs": t.array(t.proxy(renames["ParagraphOut"])).optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlockOut"])
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
    types["GoogleCloudVisionV1p4beta1OutputConfigIn"] = t.struct(
        {
            "batchSize": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p4beta1GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OutputConfigIn"])
    types["GoogleCloudVisionV1p4beta1OutputConfigOut"] = t.struct(
        {
            "batchSize": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p4beta1GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OutputConfigOut"])
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
    types["GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn"] = t.struct(
        {"label": t.string().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionIn"] = t.struct(
        {
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionOut"] = t.struct(
        {
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionOut"])
    types["ParagraphIn"] = t.struct(
        {
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "confidence": t.number().optional(),
            "words": t.array(t.proxy(renames["WordIn"])).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
        }
    ).named(renames["ParagraphIn"])
    types["ParagraphOut"] = t.struct(
        {
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "confidence": t.number().optional(),
            "words": t.array(t.proxy(renames["WordOut"])).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphOut"])
    types["GoogleCloudVisionV1p4beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p4beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocationInfoOut"])
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
    types["ProductSetIn"] = t.struct(
        {"displayName": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ProductSetIn"])
    types["ProductSetOut"] = t.struct(
        {
            "indexError": t.proxy(renames["StatusOut"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "indexTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSetOut"])
    types["GoogleCloudVisionV1p4beta1BatchOperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "submitTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BatchOperationMetadataIn"])
    types["GoogleCloudVisionV1p4beta1BatchOperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "submitTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BatchOperationMetadataOut"])
    types["BatchAnnotateImagesRequestIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
        }
    ).named(renames["BatchAnnotateImagesRequestIn"])
    types["BatchAnnotateImagesRequestOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "requests": t.array(t.proxy(renames["AnnotateImageRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchAnnotateImagesRequestOut"])
    types["WebDetectionIn"] = t.struct(
        {
            "partialMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "webEntities": t.array(t.proxy(renames["WebEntityIn"])).optional(),
            "visuallySimilarImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "bestGuessLabels": t.array(t.proxy(renames["WebLabelIn"])).optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["WebPageIn"])
            ).optional(),
        }
    ).named(renames["WebDetectionIn"])
    types["WebDetectionOut"] = t.struct(
        {
            "partialMatchingImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "webEntities": t.array(t.proxy(renames["WebEntityOut"])).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "bestGuessLabels": t.array(t.proxy(renames["WebLabelOut"])).optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageOut"])).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["WebPageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebDetectionOut"])
    types["GoogleCloudVisionV1p1beta1ImageAnnotationContextIn"] = t.struct(
        {"pageNumber": t.integer().optional(), "uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextIn"])
    types["GoogleCloudVisionV1p1beta1ImageAnnotationContextOut"] = t.struct(
        {
            "pageNumber": t.integer().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextOut"])
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
    types["GoogleCloudVisionV1p1beta1PositionIn"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "z": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PositionIn"])
    types["GoogleCloudVisionV1p1beta1PositionOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "z": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PositionOut"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationIn"] = t.struct(
        {
            "text": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationOut"] = t.struct(
        {
            "text": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationOut"])
    types["GoogleCloudVisionV1p1beta1CropHintIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1CropHintIn"])
    types["GoogleCloudVisionV1p1beta1CropHintOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1CropHintOut"])
    types["GoogleCloudVisionV1p2beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p2beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocationInfoOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"] = t.struct(
        {
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "url": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"] = t.struct(
        {
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "url": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"])
    types["TextPropertyIn"] = t.struct(
        {
            "detectedBreak": t.proxy(renames["DetectedBreakIn"]).optional(),
            "detectedLanguages": t.array(
                t.proxy(renames["DetectedLanguageIn"])
            ).optional(),
        }
    ).named(renames["TextPropertyIn"])
    types["TextPropertyOut"] = t.struct(
        {
            "detectedBreak": t.proxy(renames["DetectedBreakOut"]).optional(),
            "detectedLanguages": t.array(
                t.proxy(renames["DetectedLanguageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPropertyOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn"] = t.struct(
        {"label": t.string().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut"])
    types["PositionIn"] = t.struct(
        {
            "z": t.number().optional(),
            "x": t.number().optional(),
            "y": t.number().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "z": t.number().optional(),
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
    types["BatchOperationMetadataIn"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["BatchOperationMetadataIn"])
    types["BatchOperationMetadataOut"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOperationMetadataOut"])
    types["AddProductToProductSetRequestIn"] = t.struct({"product": t.string()}).named(
        renames["AddProductToProductSetRequestIn"]
    )
    types["AddProductToProductSetRequestOut"] = t.struct(
        {"product": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddProductToProductSetRequestOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionIn"] = t.struct(
        {
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionOut"] = t.struct(
        {
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionOut"])
    types["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1SymbolIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SymbolIn"])
    types["GoogleCloudVisionV1p2beta1SymbolOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SymbolOut"])
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
    types["GoogleCloudVisionV1p3beta1PositionIn"] = t.struct(
        {
            "y": t.number().optional(),
            "z": t.number().optional(),
            "x": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PositionIn"])
    types["GoogleCloudVisionV1p3beta1PositionOut"] = t.struct(
        {
            "y": t.number().optional(),
            "z": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PositionOut"])
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
            "url": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"])
    types["FeatureIn"] = t.struct(
        {
            "model": t.string().optional(),
            "type": t.string().optional(),
            "maxResults": t.integer().optional(),
        }
    ).named(renames["FeatureIn"])
    types["FeatureOut"] = t.struct(
        {
            "model": t.string().optional(),
            "type": t.string().optional(),
            "maxResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["GoogleCloudVisionV1p1beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p1beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocationInfoOut"])
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
    types["GoogleCloudVisionV1p3beta1WebDetectionIn"] = t.struct(
        {
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageIn"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionOut"] = t.struct(
        {
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageOut"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionOut"])
    types["ProductIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(t.proxy(renames["KeyValueOut"])).optional(),
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "image": t.string().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductIn"]
            ).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "image": t.string().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductOut"]
            ).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"])
    types["GoogleCloudVisionV1p4beta1PageIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BlockIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PageIn"])
    types["GoogleCloudVisionV1p4beta1PageOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BlockOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PageOut"])
    types["AnnotateFileRequestIn"] = t.struct(
        {
            "pages": t.array(t.integer()).optional(),
            "imageContext": t.proxy(renames["ImageContextIn"]).optional(),
            "inputConfig": t.proxy(renames["InputConfigIn"]),
            "features": t.array(t.proxy(renames["FeatureIn"])),
        }
    ).named(renames["AnnotateFileRequestIn"])
    types["AnnotateFileRequestOut"] = t.struct(
        {
            "pages": t.array(t.integer()).optional(),
            "imageContext": t.proxy(renames["ImageContextOut"]).optional(),
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "features": t.array(t.proxy(renames["FeatureOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateFileRequestOut"])
    types["GoogleCloudVisionV1p3beta1WordIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1SymbolIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WordIn"])
    types["GoogleCloudVisionV1p3beta1WordOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1SymbolOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WordOut"])
    types["GoogleCloudVisionV1p2beta1AnnotateFileResponseIn"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p2beta1InputConfigIn"]
            ).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"])
            ).optional(),
            "totalPages": t.integer().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p2beta1AnnotateFileResponseOut"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p2beta1InputConfigOut"]
            ).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"])
            ).optional(),
            "totalPages": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p2beta1EntityAnnotationIn"] = t.struct(
        {
            "topicality": t.number().optional(),
            "description": t.string().optional(),
            "confidence": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PropertyIn"])
            ).optional(),
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1LocationInfoIn"])
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "locale": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1EntityAnnotationOut"] = t.struct(
        {
            "topicality": t.number().optional(),
            "description": t.string().optional(),
            "confidence": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PropertyOut"])
            ).optional(),
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1LocationInfoOut"])
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "locale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
    types["DetectedLanguageIn"] = t.struct(
        {"languageCode": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["DetectedLanguageIn"])
    types["DetectedLanguageOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectedLanguageOut"])
    types["ListProductSetsResponseIn"] = t.struct(
        {
            "productSets": t.array(t.proxy(renames["ProductSetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProductSetsResponseIn"])
    types["ListProductSetsResponseOut"] = t.struct(
        {
            "productSets": t.array(t.proxy(renames["ProductSetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductSetsResponseOut"])
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
    types["ImportProductSetsRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["ImportProductSetsInputConfigIn"])}
    ).named(renames["ImportProductSetsRequestIn"])
    types["ImportProductSetsRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["ImportProductSetsInputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsRequestOut"])
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
    types["LatLongRectIn"] = t.struct(
        {
            "maxLatLng": t.proxy(renames["LatLngIn"]).optional(),
            "minLatLng": t.proxy(renames["LatLngIn"]).optional(),
        }
    ).named(renames["LatLongRectIn"])
    types["LatLongRectOut"] = t.struct(
        {
            "maxLatLng": t.proxy(renames["LatLngOut"]).optional(),
            "minLatLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLongRectOut"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"
                    ]
                )
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
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"
                    ]
                )
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut"])
    types["GoogleCloudVisionV1p3beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p3beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocationInfoOut"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "score": t.number().optional(),
            "image": t.string().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "score": t.number().optional(),
            "image": t.string().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"])
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
    types["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"] = t.struct(
        {
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextIn"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1CropHintsAnnotationIn"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p2beta1WebDetectionIn"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImagePropertiesIn"]
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"]
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationIn"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductSearchResultsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"] = t.struct(
        {
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextOut"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1CropHintsAnnotationOut"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p2beta1WebDetectionOut"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImagePropertiesOut"]
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationOut"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductSearchResultsOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"])
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
    types["GoogleCloudVisionV1p1beta1FaceAnnotationIn"] = t.struct(
        {
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "sorrowLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "detectionConfidence": t.number().optional(),
            "tiltAngle": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "panAngle": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1FaceAnnotationOut"] = t.struct(
        {
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "sorrowLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "detectionConfidence": t.number().optional(),
            "tiltAngle": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "panAngle": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationOut"])
    types["LandmarkIn"] = t.struct(
        {
            "position": t.proxy(renames["PositionIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["LandmarkIn"])
    types["LandmarkOut"] = t.struct(
        {
            "position": t.proxy(renames["PositionOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LandmarkOut"])
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
    types["GoogleCloudVisionV1p1beta1PropertyIn"] = t.struct(
        {
            "value": t.string().optional(),
            "uint64Value": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PropertyIn"])
    types["GoogleCloudVisionV1p1beta1PropertyOut"] = t.struct(
        {
            "value": t.string().optional(),
            "uint64Value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PropertyOut"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductIn"]
            ).optional(),
            "image": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "score": t.number().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductOut"]
            ).optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsIn"] = t.struct(
        {
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsOut"] = t.struct(
        {
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsOut"])
    types["ReferenceImageIn"] = t.struct(
        {
            "boundingPolys": t.array(t.proxy(renames["BoundingPolyIn"])).optional(),
            "uri": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["ReferenceImageIn"])
    types["ReferenceImageOut"] = t.struct(
        {
            "boundingPolys": t.array(t.proxy(renames["BoundingPolyOut"])).optional(),
            "uri": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceImageOut"])
    types["GoogleCloudVisionV1p4beta1OperationMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p4beta1OperationMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OperationMetadataOut"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationIn"] = t.struct(
        {
            "text": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationOut"] = t.struct(
        {
            "text": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p2beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1GcsSourceOut"])
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
    types["WebDetectionParamsIn"] = t.struct(
        {"includeGeoResults": t.boolean().optional()}
    ).named(renames["WebDetectionParamsIn"])
    types["WebDetectionParamsOut"] = t.struct(
        {
            "includeGeoResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebDetectionParamsOut"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsIn"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p2beta1ProductSearchResultsOut"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductSearchResultsOut"])
    types["CropHintsAnnotationIn"] = t.struct(
        {"cropHints": t.array(t.proxy(renames["CropHintIn"])).optional()}
    ).named(renames["CropHintsAnnotationIn"])
    types["CropHintsAnnotationOut"] = t.struct(
        {
            "cropHints": t.array(t.proxy(renames["CropHintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropHintsAnnotationOut"])
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
    types[
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"]
    )
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
    types["SymbolIn"] = t.struct(
        {
            "text": t.string().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["SymbolIn"])
    types["SymbolOut"] = t.struct(
        {
            "text": t.string().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SymbolOut"])
    types["GoogleCloudVisionV1p1beta1ParagraphIn"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WordIn"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ParagraphIn"])
    types["GoogleCloudVisionV1p1beta1ParagraphOut"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WordOut"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ParagraphOut"])
    types["AsyncBatchAnnotateImagesResponseIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"]).optional()}
    ).named(renames["AsyncBatchAnnotateImagesResponseIn"])
    types["AsyncBatchAnnotateImagesResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateImagesResponseOut"])
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
    types["GoogleCloudVisionV1p3beta1ProductIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "productCategory": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ProductKeyValueIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductIn"])
    types["GoogleCloudVisionV1p3beta1ProductOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "productCategory": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ProductKeyValueOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductOut"])
    types["GoogleCloudVisionV1p3beta1SymbolIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SymbolIn"])
    types["GoogleCloudVisionV1p3beta1SymbolOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SymbolOut"])
    types["ProductSearchParamsIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "productSet": t.string().optional(),
            "productCategories": t.array(t.string()).optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
        }
    ).named(renames["ProductSearchParamsIn"])
    types["ProductSearchParamsOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "productSet": t.string().optional(),
            "productCategories": t.array(t.string()).optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSearchParamsOut"])
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
    types["GoogleCloudVisionV1p2beta1PositionIn"] = t.struct(
        {
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PositionIn"])
    types["GoogleCloudVisionV1p2beta1PositionOut"] = t.struct(
        {
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PositionOut"])
    types["GoogleCloudVisionV1p2beta1VertexIn"] = t.struct(
        {"y": t.integer().optional(), "x": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1VertexIn"])
    types["GoogleCloudVisionV1p2beta1VertexOut"] = t.struct(
        {
            "y": t.integer().optional(),
            "x": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1VertexOut"])
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
    types["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "score": t.number().optional(),
            "description": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "score": t.number().optional(),
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"])
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
    types["GoogleCloudVisionV1p3beta1AnnotateFileResponseIn"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p3beta1InputConfigIn"]
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"])
            ).optional(),
            "totalPages": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p3beta1AnnotateFileResponseOut"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p3beta1InputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"])
            ).optional(),
            "totalPages": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateFileResponseOut"])
    types["WebPageIn"] = t.struct(
        {
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "score": t.number().optional(),
            "url": t.string().optional(),
            "partialMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
        }
    ).named(renames["WebPageIn"])
    types["WebPageOut"] = t.struct(
        {
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageOut"])).optional(),
            "score": t.number().optional(),
            "url": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebPageOut"])
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
    types["GoogleCloudVisionV1p1beta1AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p1beta1InputConfigIn"]
            ).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"])
            ).optional(),
            "totalPages": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p1beta1AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p1beta1InputConfigOut"]
            ).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"])
            ).optional(),
            "totalPages": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateFileResponseOut"])

    functions = {}
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
    functions["projectsOperationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsImagesAsyncBatchAnnotate"] = vision.post(
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
    functions["projectsImagesAnnotate"] = vision.post(
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
    functions["projectsFilesAnnotate"] = vision.post(
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
    functions["projectsFilesAsyncBatchAnnotate"] = vision.post(
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
    functions["projectsLocationsOperationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsDelete"] = vision.get(
        "v1/{parent}/products",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsPurge"] = vision.get(
        "v1/{parent}/products",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsPatch"] = vision.get(
        "v1/{parent}/products",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCreate"] = vision.get(
        "v1/{parent}/products",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsGet"] = vision.get(
        "v1/{parent}/products",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsList"] = vision.get(
        "v1/{parent}/products",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesGet"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesList"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesCreate"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesDelete"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsProductSetsImport"] = vision.get(
        "v1/{parent}/productSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsDelete"] = vision.get(
        "v1/{parent}/productSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsRemoveProduct"] = vision.get(
        "v1/{parent}/productSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsAddProduct"] = vision.get(
        "v1/{parent}/productSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsPatch"] = vision.get(
        "v1/{parent}/productSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsCreate"] = vision.get(
        "v1/{parent}/productSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsGet"] = vision.get(
        "v1/{parent}/productSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsList"] = vision.get(
        "v1/{parent}/productSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsProductsList"] = vision.get(
        "v1/{name}/products",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsInProductSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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
    functions["imagesAsyncBatchAnnotate"] = vision.post(
        "v1/images:annotate",
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
    functions["imagesAnnotate"] = vision.post(
        "v1/images:annotate",
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

    return Import(
        importer="vision", renames=renames, types=Box(types), functions=Box(functions)
    )
