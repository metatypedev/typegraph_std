from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_vision() -> Import:
    vision = HTTPRuntime("https://vision.googleapis.com/")

    renames = {
        "ErrorResponse": "_vision_1_ErrorResponse",
        "ProductIn": "_vision_2_ProductIn",
        "ProductOut": "_vision_3_ProductOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn": "_vision_4_GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut": "_vision_5_GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p4beta1ImagePropertiesIn": "_vision_6_GoogleCloudVisionV1p4beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p4beta1ImagePropertiesOut": "_vision_7_GoogleCloudVisionV1p4beta1ImagePropertiesOut",
        "GoogleCloudVisionV1p4beta1PositionIn": "_vision_8_GoogleCloudVisionV1p4beta1PositionIn",
        "GoogleCloudVisionV1p4beta1PositionOut": "_vision_9_GoogleCloudVisionV1p4beta1PositionOut",
        "GoogleCloudVisionV1p1beta1NormalizedVertexIn": "_vision_10_GoogleCloudVisionV1p1beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p1beta1NormalizedVertexOut": "_vision_11_GoogleCloudVisionV1p1beta1NormalizedVertexOut",
        "GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn": "_vision_12_GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut": "_vision_13_GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p2beta1BoundingPolyIn": "_vision_14_GoogleCloudVisionV1p2beta1BoundingPolyIn",
        "GoogleCloudVisionV1p2beta1BoundingPolyOut": "_vision_15_GoogleCloudVisionV1p2beta1BoundingPolyOut",
        "ProductSetPurgeConfigIn": "_vision_16_ProductSetPurgeConfigIn",
        "ProductSetPurgeConfigOut": "_vision_17_ProductSetPurgeConfigOut",
        "GoogleCloudVisionV1p3beta1EntityAnnotationIn": "_vision_18_GoogleCloudVisionV1p3beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p3beta1EntityAnnotationOut": "_vision_19_GoogleCloudVisionV1p3beta1EntityAnnotationOut",
        "GoogleCloudVisionV1p4beta1BatchOperationMetadataIn": "_vision_20_GoogleCloudVisionV1p4beta1BatchOperationMetadataIn",
        "GoogleCloudVisionV1p4beta1BatchOperationMetadataOut": "_vision_21_GoogleCloudVisionV1p4beta1BatchOperationMetadataOut",
        "WebEntityIn": "_vision_22_WebEntityIn",
        "WebEntityOut": "_vision_23_WebEntityOut",
        "GoogleCloudVisionV1p4beta1ImageAnnotationContextIn": "_vision_24_GoogleCloudVisionV1p4beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p4beta1ImageAnnotationContextOut": "_vision_25_GoogleCloudVisionV1p4beta1ImageAnnotationContextOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn": "_vision_26_GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut": "_vision_27_GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut",
        "GoogleCloudVisionV1p3beta1PositionIn": "_vision_28_GoogleCloudVisionV1p3beta1PositionIn",
        "GoogleCloudVisionV1p3beta1PositionOut": "_vision_29_GoogleCloudVisionV1p3beta1PositionOut",
        "CropHintsParamsIn": "_vision_30_CropHintsParamsIn",
        "CropHintsParamsOut": "_vision_31_CropHintsParamsOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn": "_vision_32_GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut": "_vision_33_GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p3beta1InputConfigIn": "_vision_34_GoogleCloudVisionV1p3beta1InputConfigIn",
        "GoogleCloudVisionV1p3beta1InputConfigOut": "_vision_35_GoogleCloudVisionV1p3beta1InputConfigOut",
        "ColorIn": "_vision_36_ColorIn",
        "ColorOut": "_vision_37_ColorOut",
        "OperationIn": "_vision_38_OperationIn",
        "OperationOut": "_vision_39_OperationOut",
        "GoogleCloudVisionV1p1beta1BoundingPolyIn": "_vision_40_GoogleCloudVisionV1p1beta1BoundingPolyIn",
        "GoogleCloudVisionV1p1beta1BoundingPolyOut": "_vision_41_GoogleCloudVisionV1p1beta1BoundingPolyOut",
        "WebImageIn": "_vision_42_WebImageIn",
        "WebImageOut": "_vision_43_WebImageOut",
        "GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn": "_vision_44_GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut": "_vision_45_GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn": "_vision_46_GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut": "_vision_47_GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn": "_vision_48_GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut": "_vision_49_GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn": "_vision_50_GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut": "_vision_51_GoogleCloudVisionV1p1beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p2beta1WordIn": "_vision_52_GoogleCloudVisionV1p2beta1WordIn",
        "GoogleCloudVisionV1p2beta1WordOut": "_vision_53_GoogleCloudVisionV1p2beta1WordOut",
        "LatLongRectIn": "_vision_54_LatLongRectIn",
        "LatLongRectOut": "_vision_55_LatLongRectOut",
        "GoogleCloudVisionV1p3beta1ProductIn": "_vision_56_GoogleCloudVisionV1p3beta1ProductIn",
        "GoogleCloudVisionV1p3beta1ProductOut": "_vision_57_GoogleCloudVisionV1p3beta1ProductOut",
        "GcsSourceIn": "_vision_58_GcsSourceIn",
        "GcsSourceOut": "_vision_59_GcsSourceOut",
        "TextPropertyIn": "_vision_60_TextPropertyIn",
        "TextPropertyOut": "_vision_61_TextPropertyOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn": "_vision_62_GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut": "_vision_63_GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p4beta1OutputConfigIn": "_vision_64_GoogleCloudVisionV1p4beta1OutputConfigIn",
        "GoogleCloudVisionV1p4beta1OutputConfigOut": "_vision_65_GoogleCloudVisionV1p4beta1OutputConfigOut",
        "GoogleCloudVisionV1p2beta1InputConfigIn": "_vision_66_GoogleCloudVisionV1p2beta1InputConfigIn",
        "GoogleCloudVisionV1p2beta1InputConfigOut": "_vision_67_GoogleCloudVisionV1p2beta1InputConfigOut",
        "GoogleCloudVisionV1p3beta1AnnotateImageResponseIn": "_vision_68_GoogleCloudVisionV1p3beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p3beta1AnnotateImageResponseOut": "_vision_69_GoogleCloudVisionV1p3beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p3beta1VertexIn": "_vision_70_GoogleCloudVisionV1p3beta1VertexIn",
        "GoogleCloudVisionV1p3beta1VertexOut": "_vision_71_GoogleCloudVisionV1p3beta1VertexOut",
        "GoogleCloudVisionV1p1beta1EntityAnnotationIn": "_vision_72_GoogleCloudVisionV1p1beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p1beta1EntityAnnotationOut": "_vision_73_GoogleCloudVisionV1p1beta1EntityAnnotationOut",
        "GoogleCloudVisionV1p4beta1ReferenceImageIn": "_vision_74_GoogleCloudVisionV1p4beta1ReferenceImageIn",
        "GoogleCloudVisionV1p4beta1ReferenceImageOut": "_vision_75_GoogleCloudVisionV1p4beta1ReferenceImageOut",
        "GoogleCloudVisionV1p3beta1PropertyIn": "_vision_76_GoogleCloudVisionV1p3beta1PropertyIn",
        "GoogleCloudVisionV1p3beta1PropertyOut": "_vision_77_GoogleCloudVisionV1p3beta1PropertyOut",
        "GoogleCloudVisionV1p4beta1ColorInfoIn": "_vision_78_GoogleCloudVisionV1p4beta1ColorInfoIn",
        "GoogleCloudVisionV1p4beta1ColorInfoOut": "_vision_79_GoogleCloudVisionV1p4beta1ColorInfoOut",
        "ImportProductSetsRequestIn": "_vision_80_ImportProductSetsRequestIn",
        "ImportProductSetsRequestOut": "_vision_81_ImportProductSetsRequestOut",
        "GoogleCloudVisionV1p2beta1ProductIn": "_vision_82_GoogleCloudVisionV1p2beta1ProductIn",
        "GoogleCloudVisionV1p2beta1ProductOut": "_vision_83_GoogleCloudVisionV1p2beta1ProductOut",
        "StatusIn": "_vision_84_StatusIn",
        "StatusOut": "_vision_85_StatusOut",
        "GoogleCloudVisionV1p1beta1ParagraphIn": "_vision_86_GoogleCloudVisionV1p1beta1ParagraphIn",
        "GoogleCloudVisionV1p1beta1ParagraphOut": "_vision_87_GoogleCloudVisionV1p1beta1ParagraphOut",
        "ResultIn": "_vision_88_ResultIn",
        "ResultOut": "_vision_89_ResultOut",
        "AsyncBatchAnnotateFilesResponseIn": "_vision_90_AsyncBatchAnnotateFilesResponseIn",
        "AsyncBatchAnnotateFilesResponseOut": "_vision_91_AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p3beta1PageIn": "_vision_92_GoogleCloudVisionV1p3beta1PageIn",
        "GoogleCloudVisionV1p3beta1PageOut": "_vision_93_GoogleCloudVisionV1p3beta1PageOut",
        "GoogleCloudVisionV1p3beta1OutputConfigIn": "_vision_94_GoogleCloudVisionV1p3beta1OutputConfigIn",
        "GoogleCloudVisionV1p3beta1OutputConfigOut": "_vision_95_GoogleCloudVisionV1p3beta1OutputConfigOut",
        "GoogleCloudVisionV1p3beta1BatchOperationMetadataIn": "_vision_96_GoogleCloudVisionV1p3beta1BatchOperationMetadataIn",
        "GoogleCloudVisionV1p3beta1BatchOperationMetadataOut": "_vision_97_GoogleCloudVisionV1p3beta1BatchOperationMetadataOut",
        "WordIn": "_vision_98_WordIn",
        "WordOut": "_vision_99_WordOut",
        "GoogleCloudVisionV1p1beta1AnnotateFileResponseIn": "_vision_100_GoogleCloudVisionV1p1beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p1beta1AnnotateFileResponseOut": "_vision_101_GoogleCloudVisionV1p1beta1AnnotateFileResponseOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn": "_vision_102_GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut": "_vision_103_GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn": "_vision_104_GoogleCloudVisionV1p2beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut": "_vision_105_GoogleCloudVisionV1p2beta1ProductSearchResultsResultOut",
        "GoogleCloudVisionV1p1beta1BlockIn": "_vision_106_GoogleCloudVisionV1p1beta1BlockIn",
        "GoogleCloudVisionV1p1beta1BlockOut": "_vision_107_GoogleCloudVisionV1p1beta1BlockOut",
        "ListProductsResponseIn": "_vision_108_ListProductsResponseIn",
        "ListProductsResponseOut": "_vision_109_ListProductsResponseOut",
        "ImportProductSetsResponseIn": "_vision_110_ImportProductSetsResponseIn",
        "ImportProductSetsResponseOut": "_vision_111_ImportProductSetsResponseOut",
        "BatchAnnotateImagesRequestIn": "_vision_112_BatchAnnotateImagesRequestIn",
        "BatchAnnotateImagesRequestOut": "_vision_113_BatchAnnotateImagesRequestOut",
        "GoogleCloudVisionV1p1beta1ImagePropertiesIn": "_vision_114_GoogleCloudVisionV1p1beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p1beta1ImagePropertiesOut": "_vision_115_GoogleCloudVisionV1p1beta1ImagePropertiesOut",
        "LatLngIn": "_vision_116_LatLngIn",
        "LatLngOut": "_vision_117_LatLngOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsIn": "_vision_118_GoogleCloudVisionV1p2beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsOut": "_vision_119_GoogleCloudVisionV1p2beta1ProductSearchResultsOut",
        "GcsDestinationIn": "_vision_120_GcsDestinationIn",
        "GcsDestinationOut": "_vision_121_GcsDestinationOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn": "_vision_122_GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut": "_vision_123_GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut",
        "TextAnnotationIn": "_vision_124_TextAnnotationIn",
        "TextAnnotationOut": "_vision_125_TextAnnotationOut",
        "GoogleCloudVisionV1p2beta1GcsDestinationIn": "_vision_126_GoogleCloudVisionV1p2beta1GcsDestinationIn",
        "GoogleCloudVisionV1p2beta1GcsDestinationOut": "_vision_127_GoogleCloudVisionV1p2beta1GcsDestinationOut",
        "GoogleCloudVisionV1p4beta1WordIn": "_vision_128_GoogleCloudVisionV1p4beta1WordIn",
        "GoogleCloudVisionV1p4beta1WordOut": "_vision_129_GoogleCloudVisionV1p4beta1WordOut",
        "GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn": "_vision_130_GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut": "_vision_131_GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut",
        "BoundingPolyIn": "_vision_132_BoundingPolyIn",
        "BoundingPolyOut": "_vision_133_BoundingPolyOut",
        "OutputConfigIn": "_vision_134_OutputConfigIn",
        "OutputConfigOut": "_vision_135_OutputConfigOut",
        "GoogleCloudVisionV1p1beta1LocationInfoIn": "_vision_136_GoogleCloudVisionV1p1beta1LocationInfoIn",
        "GoogleCloudVisionV1p1beta1LocationInfoOut": "_vision_137_GoogleCloudVisionV1p1beta1LocationInfoOut",
        "GoogleCloudVisionV1p4beta1OperationMetadataIn": "_vision_138_GoogleCloudVisionV1p4beta1OperationMetadataIn",
        "GoogleCloudVisionV1p4beta1OperationMetadataOut": "_vision_139_GoogleCloudVisionV1p4beta1OperationMetadataOut",
        "GoogleCloudVisionV1p2beta1AnnotateImageResponseIn": "_vision_140_GoogleCloudVisionV1p2beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p2beta1AnnotateImageResponseOut": "_vision_141_GoogleCloudVisionV1p2beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn": "_vision_142_GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut": "_vision_143_GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut",
        "ObjectAnnotationIn": "_vision_144_ObjectAnnotationIn",
        "ObjectAnnotationOut": "_vision_145_ObjectAnnotationOut",
        "GoogleCloudVisionV1p1beta1InputConfigIn": "_vision_146_GoogleCloudVisionV1p1beta1InputConfigIn",
        "GoogleCloudVisionV1p1beta1InputConfigOut": "_vision_147_GoogleCloudVisionV1p1beta1InputConfigOut",
        "AnnotateFileRequestIn": "_vision_148_AnnotateFileRequestIn",
        "AnnotateFileRequestOut": "_vision_149_AnnotateFileRequestOut",
        "GoogleCloudVisionV1p3beta1WebDetectionIn": "_vision_150_GoogleCloudVisionV1p3beta1WebDetectionIn",
        "GoogleCloudVisionV1p3beta1WebDetectionOut": "_vision_151_GoogleCloudVisionV1p3beta1WebDetectionOut",
        "BatchAnnotateFilesResponseIn": "_vision_152_BatchAnnotateFilesResponseIn",
        "BatchAnnotateFilesResponseOut": "_vision_153_BatchAnnotateFilesResponseOut",
        "SymbolIn": "_vision_154_SymbolIn",
        "SymbolOut": "_vision_155_SymbolOut",
        "GoogleCloudVisionV1p4beta1LocationInfoIn": "_vision_156_GoogleCloudVisionV1p4beta1LocationInfoIn",
        "GoogleCloudVisionV1p4beta1LocationInfoOut": "_vision_157_GoogleCloudVisionV1p4beta1LocationInfoOut",
        "BlockIn": "_vision_158_BlockIn",
        "BlockOut": "_vision_159_BlockOut",
        "GoogleCloudVisionV1p1beta1OperationMetadataIn": "_vision_160_GoogleCloudVisionV1p1beta1OperationMetadataIn",
        "GoogleCloudVisionV1p1beta1OperationMetadataOut": "_vision_161_GoogleCloudVisionV1p1beta1OperationMetadataOut",
        "GoogleCloudVisionV1p1beta1ProductKeyValueIn": "_vision_162_GoogleCloudVisionV1p1beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p1beta1ProductKeyValueOut": "_vision_163_GoogleCloudVisionV1p1beta1ProductKeyValueOut",
        "GoogleCloudVisionV1p3beta1BlockIn": "_vision_164_GoogleCloudVisionV1p3beta1BlockIn",
        "GoogleCloudVisionV1p3beta1BlockOut": "_vision_165_GoogleCloudVisionV1p3beta1BlockOut",
        "GoogleCloudVisionV1p1beta1PageIn": "_vision_166_GoogleCloudVisionV1p1beta1PageIn",
        "GoogleCloudVisionV1p1beta1PageOut": "_vision_167_GoogleCloudVisionV1p1beta1PageOut",
        "LocationInfoIn": "_vision_168_LocationInfoIn",
        "LocationInfoOut": "_vision_169_LocationInfoOut",
        "GoogleCloudVisionV1p2beta1NormalizedVertexIn": "_vision_170_GoogleCloudVisionV1p2beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p2beta1NormalizedVertexOut": "_vision_171_GoogleCloudVisionV1p2beta1NormalizedVertexOut",
        "ReferenceImageIn": "_vision_172_ReferenceImageIn",
        "ReferenceImageOut": "_vision_173_ReferenceImageOut",
        "GoogleCloudVisionV1p3beta1GcsDestinationIn": "_vision_174_GoogleCloudVisionV1p3beta1GcsDestinationIn",
        "GoogleCloudVisionV1p3beta1GcsDestinationOut": "_vision_175_GoogleCloudVisionV1p3beta1GcsDestinationOut",
        "GoogleCloudVisionV1p1beta1OutputConfigIn": "_vision_176_GoogleCloudVisionV1p1beta1OutputConfigIn",
        "GoogleCloudVisionV1p1beta1OutputConfigOut": "_vision_177_GoogleCloudVisionV1p1beta1OutputConfigOut",
        "GoogleCloudVisionV1p3beta1NormalizedVertexIn": "_vision_178_GoogleCloudVisionV1p3beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p3beta1NormalizedVertexOut": "_vision_179_GoogleCloudVisionV1p3beta1NormalizedVertexOut",
        "GoogleCloudVisionV1p3beta1WordIn": "_vision_180_GoogleCloudVisionV1p3beta1WordIn",
        "GoogleCloudVisionV1p3beta1WordOut": "_vision_181_GoogleCloudVisionV1p3beta1WordOut",
        "GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn": "_vision_182_GoogleCloudVisionV1p2beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut": "_vision_183_GoogleCloudVisionV1p2beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p2beta1EntityAnnotationIn": "_vision_184_GoogleCloudVisionV1p2beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p2beta1EntityAnnotationOut": "_vision_185_GoogleCloudVisionV1p2beta1EntityAnnotationOut",
        "AddProductToProductSetRequestIn": "_vision_186_AddProductToProductSetRequestIn",
        "AddProductToProductSetRequestOut": "_vision_187_AddProductToProductSetRequestOut",
        "CropHintIn": "_vision_188_CropHintIn",
        "CropHintOut": "_vision_189_CropHintOut",
        "InputConfigIn": "_vision_190_InputConfigIn",
        "InputConfigOut": "_vision_191_InputConfigOut",
        "ProductSetIn": "_vision_192_ProductSetIn",
        "ProductSetOut": "_vision_193_ProductSetOut",
        "GoogleCloudVisionV1p2beta1AnnotateFileResponseIn": "_vision_194_GoogleCloudVisionV1p2beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p2beta1AnnotateFileResponseOut": "_vision_195_GoogleCloudVisionV1p2beta1AnnotateFileResponseOut",
        "AnnotateImageRequestIn": "_vision_196_AnnotateImageRequestIn",
        "AnnotateImageRequestOut": "_vision_197_AnnotateImageRequestOut",
        "GoogleCloudVisionV1p3beta1SymbolIn": "_vision_198_GoogleCloudVisionV1p3beta1SymbolIn",
        "GoogleCloudVisionV1p3beta1SymbolOut": "_vision_199_GoogleCloudVisionV1p3beta1SymbolOut",
        "ListReferenceImagesResponseIn": "_vision_200_ListReferenceImagesResponseIn",
        "ListReferenceImagesResponseOut": "_vision_201_ListReferenceImagesResponseOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn": "_vision_202_GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut": "_vision_203_GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p1beta1ImageAnnotationContextIn": "_vision_204_GoogleCloudVisionV1p1beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p1beta1ImageAnnotationContextOut": "_vision_205_GoogleCloudVisionV1p1beta1ImageAnnotationContextOut",
        "GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseIn": "_vision_206_GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseOut": "_vision_207_GoogleCloudVisionV1p3beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p2beta1PageIn": "_vision_208_GoogleCloudVisionV1p2beta1PageIn",
        "GoogleCloudVisionV1p2beta1PageOut": "_vision_209_GoogleCloudVisionV1p2beta1PageOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationIn": "_vision_210_GoogleCloudVisionV1p3beta1TextAnnotationIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationOut": "_vision_211_GoogleCloudVisionV1p3beta1TextAnnotationOut",
        "LandmarkIn": "_vision_212_LandmarkIn",
        "LandmarkOut": "_vision_213_LandmarkOut",
        "GoogleCloudVisionV1p4beta1EntityAnnotationIn": "_vision_214_GoogleCloudVisionV1p4beta1EntityAnnotationIn",
        "GoogleCloudVisionV1p4beta1EntityAnnotationOut": "_vision_215_GoogleCloudVisionV1p4beta1EntityAnnotationOut",
        "GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn": "_vision_216_GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut": "_vision_217_GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut",
        "CropHintsAnnotationIn": "_vision_218_CropHintsAnnotationIn",
        "CropHintsAnnotationOut": "_vision_219_CropHintsAnnotationOut",
        "GoogleCloudVisionV1p2beta1OutputConfigIn": "_vision_220_GoogleCloudVisionV1p2beta1OutputConfigIn",
        "GoogleCloudVisionV1p2beta1OutputConfigOut": "_vision_221_GoogleCloudVisionV1p2beta1OutputConfigOut",
        "GoogleCloudVisionV1p2beta1OperationMetadataIn": "_vision_222_GoogleCloudVisionV1p2beta1OperationMetadataIn",
        "GoogleCloudVisionV1p2beta1OperationMetadataOut": "_vision_223_GoogleCloudVisionV1p2beta1OperationMetadataOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn": "_vision_224_GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut": "_vision_225_GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p4beta1ProductIn": "_vision_226_GoogleCloudVisionV1p4beta1ProductIn",
        "GoogleCloudVisionV1p4beta1ProductOut": "_vision_227_GoogleCloudVisionV1p4beta1ProductOut",
        "WebLabelIn": "_vision_228_WebLabelIn",
        "WebLabelOut": "_vision_229_WebLabelOut",
        "LocalizedObjectAnnotationIn": "_vision_230_LocalizedObjectAnnotationIn",
        "LocalizedObjectAnnotationOut": "_vision_231_LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p4beta1CropHintIn": "_vision_232_GoogleCloudVisionV1p4beta1CropHintIn",
        "GoogleCloudVisionV1p4beta1CropHintOut": "_vision_233_GoogleCloudVisionV1p4beta1CropHintOut",
        "GoogleCloudVisionV1p4beta1CropHintsAnnotationIn": "_vision_234_GoogleCloudVisionV1p4beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p4beta1CropHintsAnnotationOut": "_vision_235_GoogleCloudVisionV1p4beta1CropHintsAnnotationOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn": "_vision_236_GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut": "_vision_237_GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn": "_vision_238_GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut": "_vision_239_GoogleCloudVisionV1p4beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn": "_vision_240_GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut": "_vision_241_GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut",
        "PageIn": "_vision_242_PageIn",
        "PageOut": "_vision_243_PageOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn": "_vision_244_GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut": "_vision_245_GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn": "_vision_246_GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut": "_vision_247_GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut",
        "CancelOperationRequestIn": "_vision_248_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vision_249_CancelOperationRequestOut",
        "GoogleCloudVisionV1p3beta1AnnotateFileResponseIn": "_vision_250_GoogleCloudVisionV1p3beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p3beta1AnnotateFileResponseOut": "_vision_251_GoogleCloudVisionV1p3beta1AnnotateFileResponseOut",
        "GoogleCloudVisionV1p1beta1CropHintIn": "_vision_252_GoogleCloudVisionV1p1beta1CropHintIn",
        "GoogleCloudVisionV1p1beta1CropHintOut": "_vision_253_GoogleCloudVisionV1p1beta1CropHintOut",
        "DetectedBreakIn": "_vision_254_DetectedBreakIn",
        "DetectedBreakOut": "_vision_255_DetectedBreakOut",
        "GoogleCloudVisionV1p2beta1GcsSourceIn": "_vision_256_GoogleCloudVisionV1p2beta1GcsSourceIn",
        "GoogleCloudVisionV1p2beta1GcsSourceOut": "_vision_257_GoogleCloudVisionV1p2beta1GcsSourceOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn": "_vision_258_GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut": "_vision_259_GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p2beta1ImageAnnotationContextIn": "_vision_260_GoogleCloudVisionV1p2beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p2beta1ImageAnnotationContextOut": "_vision_261_GoogleCloudVisionV1p2beta1ImageAnnotationContextOut",
        "GoogleCloudVisionV1p4beta1BoundingPolyIn": "_vision_262_GoogleCloudVisionV1p4beta1BoundingPolyIn",
        "GoogleCloudVisionV1p4beta1BoundingPolyOut": "_vision_263_GoogleCloudVisionV1p4beta1BoundingPolyOut",
        "GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn": "_vision_264_GoogleCloudVisionV1p1beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut": "_vision_265_GoogleCloudVisionV1p1beta1DominantColorsAnnotationOut",
        "PurgeProductsRequestIn": "_vision_266_PurgeProductsRequestIn",
        "PurgeProductsRequestOut": "_vision_267_PurgeProductsRequestOut",
        "GoogleCloudVisionV1p1beta1WordIn": "_vision_268_GoogleCloudVisionV1p1beta1WordIn",
        "GoogleCloudVisionV1p1beta1WordOut": "_vision_269_GoogleCloudVisionV1p1beta1WordOut",
        "GoogleCloudVisionV1p4beta1InputConfigIn": "_vision_270_GoogleCloudVisionV1p4beta1InputConfigIn",
        "GoogleCloudVisionV1p4beta1InputConfigOut": "_vision_271_GoogleCloudVisionV1p4beta1InputConfigOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebImageIn": "_vision_272_GoogleCloudVisionV1p2beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebImageOut": "_vision_273_GoogleCloudVisionV1p2beta1WebDetectionWebImageOut",
        "ImageSourceIn": "_vision_274_ImageSourceIn",
        "ImageSourceOut": "_vision_275_ImageSourceOut",
        "AsyncBatchAnnotateImagesResponseIn": "_vision_276_AsyncBatchAnnotateImagesResponseIn",
        "AsyncBatchAnnotateImagesResponseOut": "_vision_277_AsyncBatchAnnotateImagesResponseOut",
        "GoogleCloudVisionV1p1beta1ProductIn": "_vision_278_GoogleCloudVisionV1p1beta1ProductIn",
        "GoogleCloudVisionV1p1beta1ProductOut": "_vision_279_GoogleCloudVisionV1p1beta1ProductOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn": "_vision_280_GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut": "_vision_281_GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut",
        "GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn": "_vision_282_GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut": "_vision_283_GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationIn": "_vision_284_GoogleCloudVisionV1p2beta1TextAnnotationIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationOut": "_vision_285_GoogleCloudVisionV1p2beta1TextAnnotationOut",
        "GoogleCloudVisionV1p2beta1WebDetectionIn": "_vision_286_GoogleCloudVisionV1p2beta1WebDetectionIn",
        "GoogleCloudVisionV1p2beta1WebDetectionOut": "_vision_287_GoogleCloudVisionV1p2beta1WebDetectionOut",
        "ImagePropertiesIn": "_vision_288_ImagePropertiesIn",
        "ImagePropertiesOut": "_vision_289_ImagePropertiesOut",
        "GoogleCloudVisionV1p1beta1GcsSourceIn": "_vision_290_GoogleCloudVisionV1p1beta1GcsSourceIn",
        "GoogleCloudVisionV1p1beta1GcsSourceOut": "_vision_291_GoogleCloudVisionV1p1beta1GcsSourceOut",
        "DominantColorsAnnotationIn": "_vision_292_DominantColorsAnnotationIn",
        "DominantColorsAnnotationOut": "_vision_293_DominantColorsAnnotationOut",
        "RemoveProductFromProductSetRequestIn": "_vision_294_RemoveProductFromProductSetRequestIn",
        "RemoveProductFromProductSetRequestOut": "_vision_295_RemoveProductFromProductSetRequestOut",
        "GoogleCloudVisionV1p3beta1ParagraphIn": "_vision_296_GoogleCloudVisionV1p3beta1ParagraphIn",
        "GoogleCloudVisionV1p3beta1ParagraphOut": "_vision_297_GoogleCloudVisionV1p3beta1ParagraphOut",
        "BatchAnnotateFilesRequestIn": "_vision_298_BatchAnnotateFilesRequestIn",
        "BatchAnnotateFilesRequestOut": "_vision_299_BatchAnnotateFilesRequestOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn": "_vision_300_GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut": "_vision_301_GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p4beta1PropertyIn": "_vision_302_GoogleCloudVisionV1p4beta1PropertyIn",
        "GoogleCloudVisionV1p4beta1PropertyOut": "_vision_303_GoogleCloudVisionV1p4beta1PropertyOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebPageIn": "_vision_304_GoogleCloudVisionV1p4beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebPageOut": "_vision_305_GoogleCloudVisionV1p4beta1WebDetectionWebPageOut",
        "AnnotateFileResponseIn": "_vision_306_AnnotateFileResponseIn",
        "AnnotateFileResponseOut": "_vision_307_AnnotateFileResponseOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn": "_vision_308_GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut": "_vision_309_GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn": "_vision_310_GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn",
        "GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut": "_vision_311_GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p2beta1ProductKeyValueIn": "_vision_312_GoogleCloudVisionV1p2beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p2beta1ProductKeyValueOut": "_vision_313_GoogleCloudVisionV1p2beta1ProductKeyValueOut",
        "DetectedLanguageIn": "_vision_314_DetectedLanguageIn",
        "DetectedLanguageOut": "_vision_315_DetectedLanguageOut",
        "PropertyIn": "_vision_316_PropertyIn",
        "PropertyOut": "_vision_317_PropertyOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn": "_vision_318_GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut": "_vision_319_GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut",
        "ImportProductSetsGcsSourceIn": "_vision_320_ImportProductSetsGcsSourceIn",
        "ImportProductSetsGcsSourceOut": "_vision_321_ImportProductSetsGcsSourceOut",
        "GoogleCloudVisionV1p1beta1ColorInfoIn": "_vision_322_GoogleCloudVisionV1p1beta1ColorInfoIn",
        "GoogleCloudVisionV1p1beta1ColorInfoOut": "_vision_323_GoogleCloudVisionV1p1beta1ColorInfoOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationIn": "_vision_324_GoogleCloudVisionV1p4beta1TextAnnotationIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationOut": "_vision_325_GoogleCloudVisionV1p4beta1TextAnnotationOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsIn": "_vision_326_GoogleCloudVisionV1p1beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsOut": "_vision_327_GoogleCloudVisionV1p1beta1ProductSearchResultsOut",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseIn": "_vision_328_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseOut": "_vision_329_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p2beta1CropHintIn": "_vision_330_GoogleCloudVisionV1p2beta1CropHintIn",
        "GoogleCloudVisionV1p2beta1CropHintOut": "_vision_331_GoogleCloudVisionV1p2beta1CropHintOut",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn": "_vision_332_GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut": "_vision_333_GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut",
        "GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn": "_vision_334_GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut": "_vision_335_GoogleCloudVisionV1p3beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn": "_vision_336_GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut": "_vision_337_GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut",
        "ListOperationsResponseIn": "_vision_338_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vision_339_ListOperationsResponseOut",
        "GoogleCloudVisionV1p4beta1FaceRecognitionResultIn": "_vision_340_GoogleCloudVisionV1p4beta1FaceRecognitionResultIn",
        "GoogleCloudVisionV1p4beta1FaceRecognitionResultOut": "_vision_341_GoogleCloudVisionV1p4beta1FaceRecognitionResultOut",
        "VertexIn": "_vision_342_VertexIn",
        "VertexOut": "_vision_343_VertexOut",
        "GoogleCloudVisionV1p1beta1WebDetectionIn": "_vision_344_GoogleCloudVisionV1p1beta1WebDetectionIn",
        "GoogleCloudVisionV1p1beta1WebDetectionOut": "_vision_345_GoogleCloudVisionV1p1beta1WebDetectionOut",
        "GoogleCloudVisionV1p2beta1ImagePropertiesIn": "_vision_346_GoogleCloudVisionV1p2beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p2beta1ImagePropertiesOut": "_vision_347_GoogleCloudVisionV1p2beta1ImagePropertiesOut",
        "SafeSearchAnnotationIn": "_vision_348_SafeSearchAnnotationIn",
        "SafeSearchAnnotationOut": "_vision_349_SafeSearchAnnotationOut",
        "GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn": "_vision_350_GoogleCloudVisionV1p3beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut": "_vision_351_GoogleCloudVisionV1p3beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p1beta1FaceAnnotationIn": "_vision_352_GoogleCloudVisionV1p1beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p1beta1FaceAnnotationOut": "_vision_353_GoogleCloudVisionV1p1beta1FaceAnnotationOut",
        "GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn": "_vision_354_GoogleCloudVisionV1p4beta1ImportProductSetsResponseIn",
        "GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut": "_vision_355_GoogleCloudVisionV1p4beta1ImportProductSetsResponseOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebPageIn": "_vision_356_GoogleCloudVisionV1p3beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebPageOut": "_vision_357_GoogleCloudVisionV1p3beta1WebDetectionWebPageOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn": "_vision_358_GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut": "_vision_359_GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut",
        "GoogleCloudVisionV1p2beta1SymbolIn": "_vision_360_GoogleCloudVisionV1p2beta1SymbolIn",
        "GoogleCloudVisionV1p2beta1SymbolOut": "_vision_361_GoogleCloudVisionV1p2beta1SymbolOut",
        "GoogleCloudVisionV1p1beta1CropHintsAnnotationIn": "_vision_362_GoogleCloudVisionV1p1beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p1beta1CropHintsAnnotationOut": "_vision_363_GoogleCloudVisionV1p1beta1CropHintsAnnotationOut",
        "GoogleCloudVisionV1p3beta1ImageAnnotationContextIn": "_vision_364_GoogleCloudVisionV1p3beta1ImageAnnotationContextIn",
        "GoogleCloudVisionV1p3beta1ImageAnnotationContextOut": "_vision_365_GoogleCloudVisionV1p3beta1ImageAnnotationContextOut",
        "GroupedResultIn": "_vision_366_GroupedResultIn",
        "GroupedResultOut": "_vision_367_GroupedResultOut",
        "GoogleCloudVisionV1p3beta1BoundingPolyIn": "_vision_368_GoogleCloudVisionV1p3beta1BoundingPolyIn",
        "GoogleCloudVisionV1p3beta1BoundingPolyOut": "_vision_369_GoogleCloudVisionV1p3beta1BoundingPolyOut",
        "GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn": "_vision_370_GoogleCloudVisionV1p4beta1DominantColorsAnnotationIn",
        "GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut": "_vision_371_GoogleCloudVisionV1p4beta1DominantColorsAnnotationOut",
        "GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn": "_vision_372_GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn",
        "GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut": "_vision_373_GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut",
        "GoogleCloudVisionV1p2beta1PositionIn": "_vision_374_GoogleCloudVisionV1p2beta1PositionIn",
        "GoogleCloudVisionV1p2beta1PositionOut": "_vision_375_GoogleCloudVisionV1p2beta1PositionOut",
        "ImportProductSetsInputConfigIn": "_vision_376_ImportProductSetsInputConfigIn",
        "ImportProductSetsInputConfigOut": "_vision_377_ImportProductSetsInputConfigOut",
        "ImageContextIn": "_vision_378_ImageContextIn",
        "ImageContextOut": "_vision_379_ImageContextOut",
        "GoogleCloudVisionV1p4beta1CelebrityIn": "_vision_380_GoogleCloudVisionV1p4beta1CelebrityIn",
        "GoogleCloudVisionV1p4beta1CelebrityOut": "_vision_381_GoogleCloudVisionV1p4beta1CelebrityOut",
        "GoogleCloudVisionV1p4beta1ProductKeyValueIn": "_vision_382_GoogleCloudVisionV1p4beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p4beta1ProductKeyValueOut": "_vision_383_GoogleCloudVisionV1p4beta1ProductKeyValueOut",
        "ProductSearchParamsIn": "_vision_384_ProductSearchParamsIn",
        "ProductSearchParamsOut": "_vision_385_ProductSearchParamsOut",
        "GoogleCloudVisionV1p3beta1LocationInfoIn": "_vision_386_GoogleCloudVisionV1p3beta1LocationInfoIn",
        "GoogleCloudVisionV1p3beta1LocationInfoOut": "_vision_387_GoogleCloudVisionV1p3beta1LocationInfoOut",
        "GoogleCloudVisionV1p4beta1VertexIn": "_vision_388_GoogleCloudVisionV1p4beta1VertexIn",
        "GoogleCloudVisionV1p4beta1VertexOut": "_vision_389_GoogleCloudVisionV1p4beta1VertexOut",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn": "_vision_390_GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut": "_vision_391_GoogleCloudVisionV1p3beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseIn": "_vision_392_GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseOut": "_vision_393_GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesResponseOut",
        "AnnotateImageResponseIn": "_vision_394_AnnotateImageResponseIn",
        "AnnotateImageResponseOut": "_vision_395_AnnotateImageResponseOut",
        "GoogleCloudVisionV1p4beta1GcsDestinationIn": "_vision_396_GoogleCloudVisionV1p4beta1GcsDestinationIn",
        "GoogleCloudVisionV1p4beta1GcsDestinationOut": "_vision_397_GoogleCloudVisionV1p4beta1GcsDestinationOut",
        "EntityAnnotationIn": "_vision_398_EntityAnnotationIn",
        "EntityAnnotationOut": "_vision_399_EntityAnnotationOut",
        "GoogleCloudVisionV1p3beta1ReferenceImageIn": "_vision_400_GoogleCloudVisionV1p3beta1ReferenceImageIn",
        "GoogleCloudVisionV1p3beta1ReferenceImageOut": "_vision_401_GoogleCloudVisionV1p3beta1ReferenceImageOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebPageIn": "_vision_402_GoogleCloudVisionV1p1beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebPageOut": "_vision_403_GoogleCloudVisionV1p1beta1WebDetectionWebPageOut",
        "GoogleCloudVisionV1p3beta1FaceAnnotationIn": "_vision_404_GoogleCloudVisionV1p3beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p3beta1FaceAnnotationOut": "_vision_405_GoogleCloudVisionV1p3beta1FaceAnnotationOut",
        "GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn": "_vision_406_GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn",
        "GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut": "_vision_407_GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut",
        "GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseIn": "_vision_408_GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseOut": "_vision_409_GoogleCloudVisionV1p4beta1BatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebImageIn": "_vision_410_GoogleCloudVisionV1p1beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebImageOut": "_vision_411_GoogleCloudVisionV1p1beta1WebDetectionWebImageOut",
        "GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn": "_vision_412_GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut": "_vision_413_GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut",
        "WebDetectionParamsIn": "_vision_414_WebDetectionParamsIn",
        "WebDetectionParamsOut": "_vision_415_WebDetectionParamsOut",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn": "_vision_416_GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut": "_vision_417_GoogleCloudVisionV1p2beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn": "_vision_418_GoogleCloudVisionV1p3beta1WebDetectionWebLabelIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut": "_vision_419_GoogleCloudVisionV1p3beta1WebDetectionWebLabelOut",
        "BatchAnnotateImagesResponseIn": "_vision_420_BatchAnnotateImagesResponseIn",
        "BatchAnnotateImagesResponseOut": "_vision_421_BatchAnnotateImagesResponseOut",
        "GoogleCloudVisionV1p3beta1WebDetectionWebImageIn": "_vision_422_GoogleCloudVisionV1p3beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p3beta1WebDetectionWebImageOut": "_vision_423_GoogleCloudVisionV1p3beta1WebDetectionWebImageOut",
        "GoogleCloudVisionV1p3beta1ColorInfoIn": "_vision_424_GoogleCloudVisionV1p3beta1ColorInfoIn",
        "GoogleCloudVisionV1p3beta1ColorInfoOut": "_vision_425_GoogleCloudVisionV1p3beta1ColorInfoOut",
        "GoogleCloudVisionV1p2beta1ColorInfoIn": "_vision_426_GoogleCloudVisionV1p2beta1ColorInfoIn",
        "GoogleCloudVisionV1p2beta1ColorInfoOut": "_vision_427_GoogleCloudVisionV1p2beta1ColorInfoOut",
        "GoogleCloudVisionV1p1beta1SymbolIn": "_vision_428_GoogleCloudVisionV1p1beta1SymbolIn",
        "GoogleCloudVisionV1p1beta1SymbolOut": "_vision_429_GoogleCloudVisionV1p1beta1SymbolOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn": "_vision_430_GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut": "_vision_431_GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut",
        "GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn": "_vision_432_GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseIn",
        "GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut": "_vision_433_GoogleCloudVisionV1p2beta1AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsIn": "_vision_434_GoogleCloudVisionV1p3beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsOut": "_vision_435_GoogleCloudVisionV1p3beta1ProductSearchResultsOut",
        "GoogleCloudVisionV1p3beta1OperationMetadataIn": "_vision_436_GoogleCloudVisionV1p3beta1OperationMetadataIn",
        "GoogleCloudVisionV1p3beta1OperationMetadataOut": "_vision_437_GoogleCloudVisionV1p3beta1OperationMetadataOut",
        "NormalizedVertexIn": "_vision_438_NormalizedVertexIn",
        "NormalizedVertexOut": "_vision_439_NormalizedVertexOut",
        "GoogleCloudVisionV1p1beta1PositionIn": "_vision_440_GoogleCloudVisionV1p1beta1PositionIn",
        "GoogleCloudVisionV1p1beta1PositionOut": "_vision_441_GoogleCloudVisionV1p1beta1PositionOut",
        "GoogleCloudVisionV1p3beta1ImagePropertiesIn": "_vision_442_GoogleCloudVisionV1p3beta1ImagePropertiesIn",
        "GoogleCloudVisionV1p3beta1ImagePropertiesOut": "_vision_443_GoogleCloudVisionV1p3beta1ImagePropertiesOut",
        "GoogleCloudVisionV1p4beta1FaceAnnotationIn": "_vision_444_GoogleCloudVisionV1p4beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p4beta1FaceAnnotationOut": "_vision_445_GoogleCloudVisionV1p4beta1FaceAnnotationOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsIn": "_vision_446_GoogleCloudVisionV1p4beta1ProductSearchResultsIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsOut": "_vision_447_GoogleCloudVisionV1p4beta1ProductSearchResultsOut",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseIn": "_vision_448_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseIn",
        "GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseOut": "_vision_449_GoogleCloudVisionV1p4beta1AsyncBatchAnnotateImagesResponseOut",
        "ColorInfoIn": "_vision_450_ColorInfoIn",
        "ColorInfoOut": "_vision_451_ColorInfoOut",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn": "_vision_452_GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut": "_vision_453_GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut",
        "GoogleCloudVisionV1p1beta1VertexIn": "_vision_454_GoogleCloudVisionV1p1beta1VertexIn",
        "GoogleCloudVisionV1p1beta1VertexOut": "_vision_455_GoogleCloudVisionV1p1beta1VertexOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn": "_vision_456_GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut": "_vision_457_GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut",
        "GoogleCloudVisionV1p2beta1CropHintsAnnotationIn": "_vision_458_GoogleCloudVisionV1p2beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p2beta1CropHintsAnnotationOut": "_vision_459_GoogleCloudVisionV1p2beta1CropHintsAnnotationOut",
        "GoogleCloudVisionV1p4beta1NormalizedVertexIn": "_vision_460_GoogleCloudVisionV1p4beta1NormalizedVertexIn",
        "GoogleCloudVisionV1p4beta1NormalizedVertexOut": "_vision_461_GoogleCloudVisionV1p4beta1NormalizedVertexOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn": "_vision_462_GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut": "_vision_463_GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut",
        "WebDetectionIn": "_vision_464_WebDetectionIn",
        "WebDetectionOut": "_vision_465_WebDetectionOut",
        "GoogleCloudVisionV1p4beta1WebDetectionWebImageIn": "_vision_466_GoogleCloudVisionV1p4beta1WebDetectionWebImageIn",
        "GoogleCloudVisionV1p4beta1WebDetectionWebImageOut": "_vision_467_GoogleCloudVisionV1p4beta1WebDetectionWebImageOut",
        "AsyncAnnotateFileRequestIn": "_vision_468_AsyncAnnotateFileRequestIn",
        "AsyncAnnotateFileRequestOut": "_vision_469_AsyncAnnotateFileRequestOut",
        "GoogleCloudVisionV1p4beta1AnnotateImageResponseIn": "_vision_470_GoogleCloudVisionV1p4beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p4beta1AnnotateImageResponseOut": "_vision_471_GoogleCloudVisionV1p4beta1AnnotateImageResponseOut",
        "GoogleCloudVisionV1p4beta1WebDetectionIn": "_vision_472_GoogleCloudVisionV1p4beta1WebDetectionIn",
        "GoogleCloudVisionV1p4beta1WebDetectionOut": "_vision_473_GoogleCloudVisionV1p4beta1WebDetectionOut",
        "TextDetectionParamsIn": "_vision_474_TextDetectionParamsIn",
        "TextDetectionParamsOut": "_vision_475_TextDetectionParamsOut",
        "GoogleCloudVisionV1p2beta1ParagraphIn": "_vision_476_GoogleCloudVisionV1p2beta1ParagraphIn",
        "GoogleCloudVisionV1p2beta1ParagraphOut": "_vision_477_GoogleCloudVisionV1p2beta1ParagraphOut",
        "GoogleCloudVisionV1p3beta1ProductKeyValueIn": "_vision_478_GoogleCloudVisionV1p3beta1ProductKeyValueIn",
        "GoogleCloudVisionV1p3beta1ProductKeyValueOut": "_vision_479_GoogleCloudVisionV1p3beta1ProductKeyValueOut",
        "GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn": "_vision_480_GoogleCloudVisionV1p3beta1ImportProductSetsResponseIn",
        "GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut": "_vision_481_GoogleCloudVisionV1p3beta1ImportProductSetsResponseOut",
        "GoogleCloudVisionV1p4beta1BlockIn": "_vision_482_GoogleCloudVisionV1p4beta1BlockIn",
        "GoogleCloudVisionV1p4beta1BlockOut": "_vision_483_GoogleCloudVisionV1p4beta1BlockOut",
        "GoogleCloudVisionV1p3beta1CropHintsAnnotationIn": "_vision_484_GoogleCloudVisionV1p3beta1CropHintsAnnotationIn",
        "GoogleCloudVisionV1p3beta1CropHintsAnnotationOut": "_vision_485_GoogleCloudVisionV1p3beta1CropHintsAnnotationOut",
        "FaceAnnotationIn": "_vision_486_FaceAnnotationIn",
        "FaceAnnotationOut": "_vision_487_FaceAnnotationOut",
        "KeyValueIn": "_vision_488_KeyValueIn",
        "KeyValueOut": "_vision_489_KeyValueOut",
        "FeatureIn": "_vision_490_FeatureIn",
        "FeatureOut": "_vision_491_FeatureOut",
        "GoogleCloudVisionV1p2beta1FaceAnnotationIn": "_vision_492_GoogleCloudVisionV1p2beta1FaceAnnotationIn",
        "GoogleCloudVisionV1p2beta1FaceAnnotationOut": "_vision_493_GoogleCloudVisionV1p2beta1FaceAnnotationOut",
        "GoogleCloudVisionV1p1beta1PropertyIn": "_vision_494_GoogleCloudVisionV1p1beta1PropertyIn",
        "GoogleCloudVisionV1p1beta1PropertyOut": "_vision_495_GoogleCloudVisionV1p1beta1PropertyOut",
        "ListProductSetsResponseIn": "_vision_496_ListProductSetsResponseIn",
        "ListProductSetsResponseOut": "_vision_497_ListProductSetsResponseOut",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn": "_vision_498_GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultIn",
        "GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut": "_vision_499_GoogleCloudVisionV1p2beta1ProductSearchResultsGroupedResultOut",
        "WebPageIn": "_vision_500_WebPageIn",
        "WebPageOut": "_vision_501_WebPageOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn": "_vision_502_GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut": "_vision_503_GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut",
        "GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseIn": "_vision_504_GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseIn",
        "GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseOut": "_vision_505_GoogleCloudVisionV1p1beta1AsyncBatchAnnotateFilesResponseOut",
        "GoogleCloudVisionV1p4beta1AnnotateFileResponseIn": "_vision_506_GoogleCloudVisionV1p4beta1AnnotateFileResponseIn",
        "GoogleCloudVisionV1p4beta1AnnotateFileResponseOut": "_vision_507_GoogleCloudVisionV1p4beta1AnnotateFileResponseOut",
        "GoogleCloudVisionV1p3beta1GcsSourceIn": "_vision_508_GoogleCloudVisionV1p3beta1GcsSourceIn",
        "GoogleCloudVisionV1p3beta1GcsSourceOut": "_vision_509_GoogleCloudVisionV1p3beta1GcsSourceOut",
        "GoogleCloudVisionV1p2beta1WebDetectionWebPageIn": "_vision_510_GoogleCloudVisionV1p2beta1WebDetectionWebPageIn",
        "GoogleCloudVisionV1p2beta1WebDetectionWebPageOut": "_vision_511_GoogleCloudVisionV1p2beta1WebDetectionWebPageOut",
        "ParagraphIn": "_vision_512_ParagraphIn",
        "ParagraphOut": "_vision_513_ParagraphOut",
        "GoogleCloudVisionV1p4beta1SymbolIn": "_vision_514_GoogleCloudVisionV1p4beta1SymbolIn",
        "GoogleCloudVisionV1p4beta1SymbolOut": "_vision_515_GoogleCloudVisionV1p4beta1SymbolOut",
        "PositionIn": "_vision_516_PositionIn",
        "PositionOut": "_vision_517_PositionOut",
        "GoogleCloudVisionV1p4beta1GcsSourceIn": "_vision_518_GoogleCloudVisionV1p4beta1GcsSourceIn",
        "GoogleCloudVisionV1p4beta1GcsSourceOut": "_vision_519_GoogleCloudVisionV1p4beta1GcsSourceOut",
        "GoogleCloudVisionV1p1beta1TextAnnotationIn": "_vision_520_GoogleCloudVisionV1p1beta1TextAnnotationIn",
        "GoogleCloudVisionV1p1beta1TextAnnotationOut": "_vision_521_GoogleCloudVisionV1p1beta1TextAnnotationOut",
        "ProductSearchResultsIn": "_vision_522_ProductSearchResultsIn",
        "ProductSearchResultsOut": "_vision_523_ProductSearchResultsOut",
        "BatchOperationMetadataIn": "_vision_524_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_vision_525_BatchOperationMetadataOut",
        "GoogleCloudVisionV1p4beta1ParagraphIn": "_vision_526_GoogleCloudVisionV1p4beta1ParagraphIn",
        "GoogleCloudVisionV1p4beta1ParagraphOut": "_vision_527_GoogleCloudVisionV1p4beta1ParagraphOut",
        "AsyncBatchAnnotateFilesRequestIn": "_vision_528_AsyncBatchAnnotateFilesRequestIn",
        "AsyncBatchAnnotateFilesRequestOut": "_vision_529_AsyncBatchAnnotateFilesRequestOut",
        "GoogleCloudVisionV1p1beta1AnnotateImageResponseIn": "_vision_530_GoogleCloudVisionV1p1beta1AnnotateImageResponseIn",
        "GoogleCloudVisionV1p1beta1AnnotateImageResponseOut": "_vision_531_GoogleCloudVisionV1p1beta1AnnotateImageResponseOut",
        "AsyncAnnotateFileResponseIn": "_vision_532_AsyncAnnotateFileResponseIn",
        "AsyncAnnotateFileResponseOut": "_vision_533_AsyncAnnotateFileResponseOut",
        "GoogleCloudVisionV1p2beta1VertexIn": "_vision_534_GoogleCloudVisionV1p2beta1VertexIn",
        "GoogleCloudVisionV1p2beta1VertexOut": "_vision_535_GoogleCloudVisionV1p2beta1VertexOut",
        "GoogleCloudVisionV1p4beta1PageIn": "_vision_536_GoogleCloudVisionV1p4beta1PageIn",
        "GoogleCloudVisionV1p4beta1PageOut": "_vision_537_GoogleCloudVisionV1p4beta1PageOut",
        "ImageAnnotationContextIn": "_vision_538_ImageAnnotationContextIn",
        "ImageAnnotationContextOut": "_vision_539_ImageAnnotationContextOut",
        "ImageIn": "_vision_540_ImageIn",
        "ImageOut": "_vision_541_ImageOut",
        "GoogleCloudVisionV1p3beta1CropHintIn": "_vision_542_GoogleCloudVisionV1p3beta1CropHintIn",
        "GoogleCloudVisionV1p3beta1CropHintOut": "_vision_543_GoogleCloudVisionV1p3beta1CropHintOut",
        "GoogleCloudVisionV1p1beta1GcsDestinationIn": "_vision_544_GoogleCloudVisionV1p1beta1GcsDestinationIn",
        "GoogleCloudVisionV1p1beta1GcsDestinationOut": "_vision_545_GoogleCloudVisionV1p1beta1GcsDestinationOut",
        "GoogleCloudVisionV1p2beta1BlockIn": "_vision_546_GoogleCloudVisionV1p2beta1BlockIn",
        "GoogleCloudVisionV1p2beta1BlockOut": "_vision_547_GoogleCloudVisionV1p2beta1BlockOut",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn": "_vision_548_GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn",
        "GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut": "_vision_549_GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut",
        "EmptyIn": "_vision_550_EmptyIn",
        "EmptyOut": "_vision_551_EmptyOut",
        "ListProductsInProductSetResponseIn": "_vision_552_ListProductsInProductSetResponseIn",
        "ListProductsInProductSetResponseOut": "_vision_553_ListProductsInProductSetResponseOut",
        "OperationMetadataIn": "_vision_554_OperationMetadataIn",
        "OperationMetadataOut": "_vision_555_OperationMetadataOut",
        "GoogleCloudVisionV1p2beta1LocationInfoIn": "_vision_556_GoogleCloudVisionV1p2beta1LocationInfoIn",
        "GoogleCloudVisionV1p2beta1LocationInfoOut": "_vision_557_GoogleCloudVisionV1p2beta1LocationInfoOut",
        "AsyncBatchAnnotateImagesRequestIn": "_vision_558_AsyncBatchAnnotateImagesRequestIn",
        "AsyncBatchAnnotateImagesRequestOut": "_vision_559_AsyncBatchAnnotateImagesRequestOut",
        "GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn": "_vision_560_GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn",
        "GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut": "_vision_561_GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut",
        "GoogleCloudVisionV1p2beta1PropertyIn": "_vision_562_GoogleCloudVisionV1p2beta1PropertyIn",
        "GoogleCloudVisionV1p2beta1PropertyOut": "_vision_563_GoogleCloudVisionV1p2beta1PropertyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ProductIn"] = t.struct(
        {
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(t.proxy(renames["KeyValueOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types[
        "GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "name": t.string().optional(),
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
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p2beta1ProductSearchResultsObjectAnnotationOut"]
    )
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
    types["GoogleCloudVisionV1p4beta1PositionIn"] = t.struct(
        {
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PositionIn"])
    types["GoogleCloudVisionV1p4beta1PositionOut"] = t.struct(
        {
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PositionOut"])
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
    types["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "racy": t.string().optional(),
            "violence": t.string().optional(),
            "medical": t.string().optional(),
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "racy": t.string().optional(),
            "violence": t.string().optional(),
            "medical": t.string().optional(),
            "spoof": t.string().optional(),
            "adult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1BoundingPolyIn"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1NormalizedVertexIn"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1VertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"])
    types["GoogleCloudVisionV1p2beta1BoundingPolyOut"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1NormalizedVertexOut"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1VertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"])
    types["ProductSetPurgeConfigIn"] = t.struct(
        {"productSetId": t.string().optional()}
    ).named(renames["ProductSetPurgeConfigIn"])
    types["ProductSetPurgeConfigOut"] = t.struct(
        {
            "productSetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSetPurgeConfigOut"])
    types["GoogleCloudVisionV1p3beta1EntityAnnotationIn"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PropertyIn"])
            ).optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "description": t.string().optional(),
            "confidence": t.number().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1LocationInfoIn"])
            ).optional(),
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1EntityAnnotationOut"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PropertyOut"])
            ).optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "description": t.string().optional(),
            "confidence": t.number().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1LocationInfoOut"])
            ).optional(),
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1BatchOperationMetadataIn"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BatchOperationMetadataIn"])
    types["GoogleCloudVisionV1p4beta1BatchOperationMetadataOut"] = t.struct(
        {
            "submitTime": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BatchOperationMetadataOut"])
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
    types["GoogleCloudVisionV1p3beta1PositionIn"] = t.struct(
        {
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PositionIn"])
    types["GoogleCloudVisionV1p3beta1PositionOut"] = t.struct(
        {
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PositionOut"])
    types["CropHintsParamsIn"] = t.struct(
        {"aspectRatios": t.array(t.number()).optional()}
    ).named(renames["CropHintsParamsIn"])
    types["CropHintsParamsOut"] = t.struct(
        {
            "aspectRatios": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropHintsParamsOut"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn"] = t.struct(
        {"confidence": t.number().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut"])
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
    types["ColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
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
    types["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "adult": t.string().optional(),
            "spoof": t.string().optional(),
            "violence": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "adult": t.string().optional(),
            "spoof": t.string().optional(),
            "violence": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudVisionV1p4beta1PositionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudVisionV1p4beta1PositionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut"])
    types["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"])
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
    types["GoogleCloudVisionV1p2beta1WordIn"] = t.struct(
        {
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1SymbolIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WordIn"])
    types["GoogleCloudVisionV1p2beta1WordOut"] = t.struct(
        {
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1SymbolOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WordOut"])
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
    types["GoogleCloudVisionV1p3beta1ProductIn"] = t.struct(
        {
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ProductKeyValueIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductIn"])
    types["GoogleCloudVisionV1p3beta1ProductOut"] = t.struct(
        {
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ProductKeyValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsSourceOut"])
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
    types["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn"] = t.struct(
        {"type": t.string().optional(), "isPrefix": t.boolean().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakIn"])
    types["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "isPrefix": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1TextAnnotationDetectedBreakOut"])
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
    types["GoogleCloudVisionV1p2beta1InputConfigIn"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsSourceIn"]
            ).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1InputConfigIn"])
    types["GoogleCloudVisionV1p2beta1InputConfigOut"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsSourceOut"]
            ).optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1InputConfigOut"])
    types["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"] = t.struct(
        {
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationIn"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p3beta1WebDetectionIn"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextIn"]
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationIn"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImagePropertiesIn"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationIn"])
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1CropHintsAnnotationIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductSearchResultsIn"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"] = t.struct(
        {
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1SafeSearchAnnotationOut"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p3beta1WebDetectionOut"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationOut"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ImagePropertiesOut"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationOut"])
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p3beta1CropHintsAnnotationOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductSearchResultsOut"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1EntityAnnotationOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"])
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
    types["GoogleCloudVisionV1p1beta1EntityAnnotationIn"] = t.struct(
        {
            "score": t.number().optional(),
            "locale": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "description": t.string().optional(),
            "topicality": t.number().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1LocationInfoIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PropertyIn"])
            ).optional(),
            "mid": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1EntityAnnotationOut"] = t.struct(
        {
            "score": t.number().optional(),
            "locale": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "description": t.string().optional(),
            "topicality": t.number().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1LocationInfoOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1PropertyOut"])
            ).optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
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
    types["GoogleCloudVisionV1p3beta1PropertyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "uint64Value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PropertyIn"])
    types["GoogleCloudVisionV1p3beta1PropertyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "uint64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1PropertyOut"])
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
    types["ImportProductSetsRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["ImportProductSetsInputConfigIn"])}
    ).named(renames["ImportProductSetsRequestIn"])
    types["ImportProductSetsRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["ImportProductSetsInputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsRequestOut"])
    types["GoogleCloudVisionV1p2beta1ProductIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "productCategory": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ProductKeyValueIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductIn"])
    types["GoogleCloudVisionV1p2beta1ProductOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "productCategory": t.string().optional(),
            "name": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ProductKeyValueOut"])
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ProductOut"])
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
    types["GoogleCloudVisionV1p1beta1ParagraphIn"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WordIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ParagraphIn"])
    types["GoogleCloudVisionV1p1beta1ParagraphOut"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WordOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ParagraphOut"])
    types["ResultIn"] = t.struct(
        {
            "image": t.string().optional(),
            "score": t.number().optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "image": t.string().optional(),
            "score": t.number().optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
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
    types["GoogleCloudVisionV1p3beta1OutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p3beta1GcsDestinationIn"]
            ).optional(),
            "batchSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1OutputConfigIn"])
    types["GoogleCloudVisionV1p3beta1OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p3beta1GcsDestinationOut"]
            ).optional(),
            "batchSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1OutputConfigOut"])
    types["GoogleCloudVisionV1p3beta1BatchOperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "submitTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BatchOperationMetadataIn"])
    types["GoogleCloudVisionV1p3beta1BatchOperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "submitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BatchOperationMetadataOut"])
    types["WordIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "symbols": t.array(t.proxy(renames["SymbolIn"])).optional(),
        }
    ).named(renames["WordIn"])
    types["WordOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "symbols": t.array(t.proxy(renames["SymbolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordOut"])
    types["GoogleCloudVisionV1p1beta1AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"])
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p1beta1InputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p1beta1AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"])
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p1beta1InputConfigOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"])
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
    types["GoogleCloudVisionV1p1beta1BlockIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ParagraphIn"])
            ).optional(),
            "blockType": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1BlockIn"])
    types["GoogleCloudVisionV1p1beta1BlockOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ParagraphOut"])
            ).optional(),
            "blockType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1BlockOut"])
    types["ListProductsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductIn"])).optional(),
        }
    ).named(renames["ListProductsResponseIn"])
    types["ListProductsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductsResponseOut"])
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
    types["GcsDestinationIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
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
    types["GoogleCloudVisionV1p2beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p2beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1GcsDestinationOut"])
    types["GoogleCloudVisionV1p4beta1WordIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1SymbolIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WordIn"])
    types["GoogleCloudVisionV1p4beta1WordOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1SymbolOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WordOut"])
    types["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"])
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
    types["GoogleCloudVisionV1p1beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p1beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocationInfoOut"])
    types["GoogleCloudVisionV1p4beta1OperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p4beta1OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1OperationMetadataOut"])
    types["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"] = t.struct(
        {
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationIn"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p2beta1WebDetectionIn"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1CropHintsAnnotationIn"]
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextIn"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationIn"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImagePropertiesIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductSearchResultsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"] = t.struct(
        {
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p2beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1SafeSearchAnnotationOut"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p2beta1WebDetectionOut"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1CropHintsAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImageAnnotationContextOut"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationOut"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ImagePropertiesOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p2beta1ProductSearchResultsOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "mid": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"])
    types["ObjectAnnotationIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
        }
    ).named(renames["ObjectAnnotationIn"])
    types["ObjectAnnotationOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "name": t.string().optional(),
            "mid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectAnnotationOut"])
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
    types["AnnotateFileRequestIn"] = t.struct(
        {
            "pages": t.array(t.integer()).optional(),
            "features": t.array(t.proxy(renames["FeatureIn"])),
            "imageContext": t.proxy(renames["ImageContextIn"]).optional(),
            "inputConfig": t.proxy(renames["InputConfigIn"]),
        }
    ).named(renames["AnnotateFileRequestIn"])
    types["AnnotateFileRequestOut"] = t.struct(
        {
            "pages": t.array(t.integer()).optional(),
            "features": t.array(t.proxy(renames["FeatureOut"])),
            "imageContext": t.proxy(renames["ImageContextOut"]).optional(),
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateFileRequestOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionIn"] = t.struct(
        {
            "visuallySimilarImages": t.array(
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
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionOut"] = t.struct(
        {
            "visuallySimilarImages": t.array(
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
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionOut"])
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
    types["SymbolIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["SymbolIn"])
    types["SymbolOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SymbolOut"])
    types["GoogleCloudVisionV1p4beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p4beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1LocationInfoOut"])
    types["BlockIn"] = t.struct(
        {
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "paragraphs": t.array(t.proxy(renames["ParagraphIn"])).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "blockType": t.string().optional(),
        }
    ).named(renames["BlockIn"])
    types["BlockOut"] = t.struct(
        {
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "paragraphs": t.array(t.proxy(renames["ParagraphOut"])).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "blockType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlockOut"])
    types["GoogleCloudVisionV1p1beta1OperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1OperationMetadataIn"])
    types["GoogleCloudVisionV1p1beta1OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1OperationMetadataOut"])
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
    types["GoogleCloudVisionV1p3beta1BlockIn"] = t.struct(
        {
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ParagraphIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "blockType": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BlockIn"])
    types["GoogleCloudVisionV1p3beta1BlockOut"] = t.struct(
        {
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1ParagraphOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "blockType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1BlockOut"])
    types["GoogleCloudVisionV1p1beta1PageIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "width": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1BlockIn"])
            ).optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PageIn"])
    types["GoogleCloudVisionV1p1beta1PageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "width": t.integer().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1BlockOut"])
            ).optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1PageOut"])
    types["LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["LocationInfoIn"])
    types["LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationInfoOut"])
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
    types["ReferenceImageIn"] = t.struct(
        {
            "boundingPolys": t.array(t.proxy(renames["BoundingPolyIn"])).optional(),
            "name": t.string().optional(),
            "uri": t.string(),
        }
    ).named(renames["ReferenceImageIn"])
    types["ReferenceImageOut"] = t.struct(
        {
            "boundingPolys": t.array(t.proxy(renames["BoundingPolyOut"])).optional(),
            "name": t.string().optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceImageOut"])
    types["GoogleCloudVisionV1p3beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p3beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1GcsDestinationOut"])
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
    types["GoogleCloudVisionV1p3beta1WordIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1SymbolIn"])
            ).optional(),
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
            "confidence": t.number().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1SymbolOut"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WordOut"])
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
    types["GoogleCloudVisionV1p2beta1EntityAnnotationIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PropertyIn"])
            ).optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1LocationInfoIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1EntityAnnotationOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1PropertyOut"])
            ).optional(),
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1LocationInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1EntityAnnotationOut"])
    types["AddProductToProductSetRequestIn"] = t.struct({"product": t.string()}).named(
        renames["AddProductToProductSetRequestIn"]
    )
    types["AddProductToProductSetRequestOut"] = t.struct(
        {"product": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddProductToProductSetRequestOut"])
    types["CropHintIn"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["CropHintIn"])
    types["CropHintOut"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropHintOut"])
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
    types["GoogleCloudVisionV1p2beta1AnnotateFileResponseIn"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p2beta1InputConfigIn"]
            ).optional(),
            "totalPages": t.integer().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p2beta1AnnotateFileResponseOut"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p2beta1InputConfigOut"]
            ).optional(),
            "totalPages": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1AnnotateImageResponseOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1AnnotateFileResponseOut"])
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
    types["GoogleCloudVisionV1p3beta1SymbolIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SymbolIn"])
    types["GoogleCloudVisionV1p3beta1SymbolOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1SymbolOut"])
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
    types["GoogleCloudVisionV1p2beta1PageIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1BlockIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PageIn"])
    types["GoogleCloudVisionV1p2beta1PageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1BlockOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PageOut"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationIn"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PageIn"])
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationOut"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1PageOut"])
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationOut"])
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
    types["GoogleCloudVisionV1p4beta1EntityAnnotationIn"] = t.struct(
        {
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1LocationInfoIn"])
            ).optional(),
            "description": t.string().optional(),
            "score": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PropertyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1EntityAnnotationOut"] = t.struct(
        {
            "topicality": t.number().optional(),
            "locale": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "mid": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1LocationInfoOut"])
            ).optional(),
            "description": t.string().optional(),
            "score": t.number().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1PropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
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
    types["CropHintsAnnotationIn"] = t.struct(
        {"cropHints": t.array(t.proxy(renames["CropHintIn"])).optional()}
    ).named(renames["CropHintsAnnotationIn"])
    types["CropHintsAnnotationOut"] = t.struct(
        {
            "cropHints": t.array(t.proxy(renames["CropHintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropHintsAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1OutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsDestinationIn"]
            ).optional(),
            "batchSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1OutputConfigIn"])
    types["GoogleCloudVisionV1p2beta1OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudVisionV1p2beta1GcsDestinationOut"]
            ).optional(),
            "batchSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1OutputConfigOut"])
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
    types["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"] = t.struct(
        {
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"])
    types["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"] = t.struct(
        {
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationDetectedBreakOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1TextAnnotationDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"])
    types["GoogleCloudVisionV1p4beta1ProductIn"] = t.struct(
        {
            "name": t.string().optional(),
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ProductKeyValueIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductIn"])
    types["GoogleCloudVisionV1p4beta1ProductOut"] = t.struct(
        {
            "name": t.string().optional(),
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ProductKeyValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductOut"])
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
    types["LocalizedObjectAnnotationIn"] = t.struct(
        {
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["LocalizedObjectAnnotationIn"])
    types["LocalizedObjectAnnotationOut"] = t.struct(
        {
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "languageCode": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedObjectAnnotationOut"])
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
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "product": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductIn"]
            ).optional(),
            "score": t.number().optional(),
            "image": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "product": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductOut"]
            ).optional(),
            "score": t.number().optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"])
    types["PageIn"] = t.struct(
        {
            "blocks": t.array(t.proxy(renames["BlockIn"])).optional(),
            "height": t.integer().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "blocks": t.array(t.proxy(renames["BlockOut"])).optional(),
            "height": t.integer().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut"])
    types[
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "mid": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p1beta1ProductSearchResultsObjectAnnotationOut"]
    )
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["GoogleCloudVisionV1p3beta1AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p3beta1InputConfigIn"]
            ).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p3beta1AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p3beta1InputConfigOut"]
            ).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1AnnotateImageResponseOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1AnnotateFileResponseOut"])
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
    types["GoogleCloudVisionV1p2beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p2beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1GcsSourceOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "score": t.number().optional(),
            "entityId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "score": t.number().optional(),
            "entityId": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"])
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
    types["GoogleCloudVisionV1p4beta1BoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1VertexIn"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1NormalizedVertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"])
    types["GoogleCloudVisionV1p4beta1BoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1VertexOut"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"])
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
    types["PurgeProductsRequestIn"] = t.struct(
        {
            "productSetPurgeConfig": t.proxy(
                renames["ProductSetPurgeConfigIn"]
            ).optional(),
            "force": t.boolean().optional(),
            "deleteOrphanProducts": t.boolean().optional(),
        }
    ).named(renames["PurgeProductsRequestIn"])
    types["PurgeProductsRequestOut"] = t.struct(
        {
            "productSetPurgeConfig": t.proxy(
                renames["ProductSetPurgeConfigOut"]
            ).optional(),
            "force": t.boolean().optional(),
            "deleteOrphanProducts": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PurgeProductsRequestOut"])
    types["GoogleCloudVisionV1p1beta1WordIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1SymbolIn"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WordIn"])
    types["GoogleCloudVisionV1p1beta1WordOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1SymbolOut"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WordOut"])
    types["GoogleCloudVisionV1p4beta1InputConfigIn"] = t.struct(
        {
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p4beta1GcsSourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1InputConfigIn"])
    types["GoogleCloudVisionV1p4beta1InputConfigOut"] = t.struct(
        {
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudVisionV1p4beta1GcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1InputConfigOut"])
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
    types["AsyncBatchAnnotateImagesResponseIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"]).optional()}
    ).named(renames["AsyncBatchAnnotateImagesResponseIn"])
    types["AsyncBatchAnnotateImagesResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateImagesResponseOut"])
    types["GoogleCloudVisionV1p1beta1ProductIn"] = t.struct(
        {
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ProductKeyValueIn"])
            ).optional(),
            "description": t.string().optional(),
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductIn"])
    types["GoogleCloudVisionV1p1beta1ProductOut"] = t.struct(
        {
            "productLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1ProductKeyValueOut"])
            ).optional(),
            "description": t.string().optional(),
            "productCategory": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductOut"])
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
    types["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "violence": t.string().optional(),
            "spoof": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "violence": t.string().optional(),
            "spoof": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"])
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
    types["GoogleCloudVisionV1p2beta1WebDetectionIn"] = t.struct(
        {
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionOut"] = t.struct(
        {
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebLabelOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionOut"])
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
    types["GoogleCloudVisionV1p1beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p1beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1GcsSourceOut"])
    types["DominantColorsAnnotationIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ColorInfoIn"])).optional()}
    ).named(renames["DominantColorsAnnotationIn"])
    types["DominantColorsAnnotationOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ColorInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DominantColorsAnnotationOut"])
    types["RemoveProductFromProductSetRequestIn"] = t.struct(
        {"product": t.string()}
    ).named(renames["RemoveProductFromProductSetRequestIn"])
    types["RemoveProductFromProductSetRequestOut"] = t.struct(
        {"product": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveProductFromProductSetRequestOut"])
    types["GoogleCloudVisionV1p3beta1ParagraphIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WordIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ParagraphIn"])
    types["GoogleCloudVisionV1p3beta1ParagraphOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p3beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ParagraphOut"])
    types["BatchAnnotateFilesRequestIn"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["AnnotateFileRequestIn"])),
            "parent": t.string().optional(),
        }
    ).named(renames["BatchAnnotateFilesRequestIn"])
    types["BatchAnnotateFilesRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["AnnotateFileRequestOut"])),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchAnnotateFilesRequestOut"])
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
    types["GoogleCloudVisionV1p4beta1PropertyIn"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PropertyIn"])
    types["GoogleCloudVisionV1p4beta1PropertyOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PropertyOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebPageIn"] = t.struct(
        {
            "url": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "pageTitle": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"])
    types["AnnotateFileResponseIn"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigIn"]).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["AnnotateImageResponseIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["AnnotateFileResponseIn"])
    types["AnnotateFileResponseOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigOut"]).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["AnnotateImageResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebEntityOut"])
    types["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"] = t.struct(
        {
            "spoof": t.string().optional(),
            "violence": t.string().optional(),
            "racy": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"] = t.struct(
        {
            "spoof": t.string().optional(),
            "violence": t.string().optional(),
            "racy": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"])
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
    types["PropertyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["PropertyIn"])
    types["PropertyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyOut"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn"] = t.struct(
        {"type": t.string().optional(), "isPrefix": t.boolean().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakIn"])
    types["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "isPrefix": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1TextAnnotationDetectedBreakOut"])
    types["ImportProductSetsGcsSourceIn"] = t.struct(
        {"csvFileUri": t.string().optional()}
    ).named(renames["ImportProductSetsGcsSourceIn"])
    types["ImportProductSetsGcsSourceOut"] = t.struct(
        {
            "csvFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsGcsSourceOut"])
    types["GoogleCloudVisionV1p1beta1ColorInfoIn"] = t.struct(
        {
            "score": t.number().optional(),
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p1beta1ColorInfoOut"] = t.struct(
        {
            "score": t.number().optional(),
            "pixelFraction": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ColorInfoOut"])
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
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p1beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"])
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
    types["GoogleCloudVisionV1p2beta1CropHintIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1CropHintIn"])
    types["GoogleCloudVisionV1p2beta1CropHintOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "importanceFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1CropHintOut"])
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
    types["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn"] = t.struct(
        {
            "position": t.proxy(
                renames["GoogleCloudVisionV1p3beta1PositionIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn"])
    types["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut"] = t.struct(
        {
            "position": t.proxy(
                renames["GoogleCloudVisionV1p3beta1PositionOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut"])
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
    types["VertexIn"] = t.struct(
        {"x": t.integer().optional(), "y": t.integer().optional()}
    ).named(renames["VertexIn"])
    types["VertexOut"] = t.struct(
        {
            "x": t.integer().optional(),
            "y": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VertexOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionIn"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionOut"] = t.struct(
        {
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"])
            ).optional(),
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionOut"])
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
    types["SafeSearchAnnotationIn"] = t.struct(
        {
            "spoof": t.string().optional(),
            "violence": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "racy": t.string().optional(),
        }
    ).named(renames["SafeSearchAnnotationIn"])
    types["SafeSearchAnnotationOut"] = t.struct(
        {
            "spoof": t.string().optional(),
            "violence": t.string().optional(),
            "adult": t.string().optional(),
            "medical": t.string().optional(),
            "racy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeSearchAnnotationOut"])
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
    types["GoogleCloudVisionV1p1beta1FaceAnnotationIn"] = t.struct(
        {
            "sorrowLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "blurredLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyIn"]
            ).optional(),
            "joyLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p1beta1FaceAnnotationOut"] = t.struct(
        {
            "sorrowLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "blurredLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "joyLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "underExposedLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1FaceAnnotationOut"])
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
    types["GoogleCloudVisionV1p3beta1WebDetectionWebPageIn"] = t.struct(
        {
            "url": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageIn"])
            ).optional(),
            "score": t.number().optional(),
            "pageTitle": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p3beta1WebDetectionWebPageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1WebDetectionWebImageOut"])
            ).optional(),
            "score": t.number().optional(),
            "pageTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1WebDetectionWebPageOut"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
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
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultIn"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsGroupedResultOut"])
    types["GoogleCloudVisionV1p2beta1SymbolIn"] = t.struct(
        {
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SymbolIn"])
    types["GoogleCloudVisionV1p2beta1SymbolOut"] = t.struct(
        {
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1SymbolOut"])
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
    types["GoogleCloudVisionV1p3beta1ImageAnnotationContextIn"] = t.struct(
        {"uri": t.string().optional(), "pageNumber": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextIn"])
    types["GoogleCloudVisionV1p3beta1ImageAnnotationContextOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "pageNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ImageAnnotationContextOut"])
    types["GroupedResultIn"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(renames["ObjectAnnotationIn"])
            ).optional(),
            "results": t.array(t.proxy(renames["ResultIn"])).optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
        }
    ).named(renames["GroupedResultIn"])
    types["GroupedResultOut"] = t.struct(
        {
            "objectAnnotations": t.array(
                t.proxy(renames["ObjectAnnotationOut"])
            ).optional(),
            "results": t.array(t.proxy(renames["ResultOut"])).optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupedResultOut"])
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
    types["GoogleCloudVisionV1p2beta1PositionIn"] = t.struct(
        {
            "z": t.number().optional(),
            "x": t.number().optional(),
            "y": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PositionIn"])
    types["GoogleCloudVisionV1p2beta1PositionOut"] = t.struct(
        {
            "z": t.number().optional(),
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PositionOut"])
    types["ImportProductSetsInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportProductSetsGcsSourceIn"]).optional()}
    ).named(renames["ImportProductSetsInputConfigIn"])
    types["ImportProductSetsInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportProductSetsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportProductSetsInputConfigOut"])
    types["ImageContextIn"] = t.struct(
        {
            "cropHintsParams": t.proxy(renames["CropHintsParamsIn"]).optional(),
            "languageHints": t.array(t.string()).optional(),
            "productSearchParams": t.proxy(renames["ProductSearchParamsIn"]).optional(),
            "latLongRect": t.proxy(renames["LatLongRectIn"]).optional(),
            "webDetectionParams": t.proxy(renames["WebDetectionParamsIn"]).optional(),
            "textDetectionParams": t.proxy(renames["TextDetectionParamsIn"]).optional(),
        }
    ).named(renames["ImageContextIn"])
    types["ImageContextOut"] = t.struct(
        {
            "cropHintsParams": t.proxy(renames["CropHintsParamsOut"]).optional(),
            "languageHints": t.array(t.string()).optional(),
            "productSearchParams": t.proxy(
                renames["ProductSearchParamsOut"]
            ).optional(),
            "latLongRect": t.proxy(renames["LatLongRectOut"]).optional(),
            "webDetectionParams": t.proxy(renames["WebDetectionParamsOut"]).optional(),
            "textDetectionParams": t.proxy(
                renames["TextDetectionParamsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageContextOut"])
    types["GoogleCloudVisionV1p4beta1CelebrityIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CelebrityIn"])
    types["GoogleCloudVisionV1p4beta1CelebrityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1CelebrityOut"])
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
    types["ProductSearchParamsIn"] = t.struct(
        {
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "productCategories": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "productSet": t.string().optional(),
        }
    ).named(renames["ProductSearchParamsIn"])
    types["ProductSearchParamsOut"] = t.struct(
        {
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "productCategories": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "productSet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSearchParamsOut"])
    types["GoogleCloudVisionV1p3beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p3beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocationInfoOut"])
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
    types["AnnotateImageResponseIn"] = t.struct(
        {
            "landmarkAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "productSearchResults": t.proxy(
                renames["ProductSearchResultsIn"]
            ).optional(),
            "faceAnnotations": t.array(t.proxy(renames["FaceAnnotationIn"])).optional(),
            "context": t.proxy(renames["ImageAnnotationContextIn"]).optional(),
            "webDetection": t.proxy(renames["WebDetectionIn"]).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["ImagePropertiesIn"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(renames["CropHintsAnnotationIn"]).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "fullTextAnnotation": t.proxy(renames["TextAnnotationIn"]).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["SafeSearchAnnotationIn"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["EntityAnnotationIn"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(renames["LocalizedObjectAnnotationIn"])
            ).optional(),
        }
    ).named(renames["AnnotateImageResponseIn"])
    types["AnnotateImageResponseOut"] = t.struct(
        {
            "landmarkAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "productSearchResults": t.proxy(
                renames["ProductSearchResultsOut"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["FaceAnnotationOut"])
            ).optional(),
            "context": t.proxy(renames["ImageAnnotationContextOut"]).optional(),
            "webDetection": t.proxy(renames["WebDetectionOut"]).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["ImagePropertiesOut"]
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["CropHintsAnnotationOut"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "fullTextAnnotation": t.proxy(renames["TextAnnotationOut"]).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["SafeSearchAnnotationOut"]
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["EntityAnnotationOut"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(renames["LocalizedObjectAnnotationOut"])
            ).optional(),
        }
    ).named(renames["AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p4beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p4beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1GcsDestinationOut"])
    types["EntityAnnotationIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationInfoIn"])).optional(),
            "properties": t.array(t.proxy(renames["PropertyIn"])).optional(),
            "mid": t.string().optional(),
            "topicality": t.number().optional(),
            "description": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "locale": t.string().optional(),
            "confidence": t.number().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["EntityAnnotationIn"])
    types["EntityAnnotationOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationInfoOut"])).optional(),
            "properties": t.array(t.proxy(renames["PropertyOut"])).optional(),
            "mid": t.string().optional(),
            "topicality": t.number().optional(),
            "description": t.string().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "locale": t.string().optional(),
            "confidence": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityAnnotationOut"])
    types["GoogleCloudVisionV1p3beta1ReferenceImageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "uri": t.string(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ReferenceImageIn"])
    types["GoogleCloudVisionV1p3beta1ReferenceImageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "uri": t.string(),
            "boundingPolys": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ReferenceImageOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"] = t.struct(
        {
            "url": t.string().optional(),
            "score": t.number().optional(),
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "score": t.number().optional(),
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebPageOut"])
    types["GoogleCloudVisionV1p3beta1FaceAnnotationIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
            "rollAngle": t.number().optional(),
            "panAngle": t.number().optional(),
            "joyLikelihood": t.string().optional(),
            "surpriseLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "detectionConfidence": t.number().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1FaceAnnotationOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "rollAngle": t.number().optional(),
            "panAngle": t.number().optional(),
            "joyLikelihood": t.string().optional(),
            "surpriseLikelihood": t.string().optional(),
            "blurredLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p3beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "detectionConfidence": t.number().optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1FaceAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"])
    types["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1TextAnnotationDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreakOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"])
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
    types["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"] = t.struct(
        {"score": t.number().optional(), "url": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"] = t.struct(
        {
            "score": t.number().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebImageOut"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn"] = t.struct(
        {"languageCode": t.string().optional(), "label": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelIn"])
    types["GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1WebDetectionWebLabelOut"])
    types["WebDetectionParamsIn"] = t.struct(
        {"includeGeoResults": t.boolean().optional()}
    ).named(renames["WebDetectionParamsIn"])
    types["WebDetectionParamsOut"] = t.struct(
        {
            "includeGeoResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebDetectionParamsOut"])
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
    types["GoogleCloudVisionV1p3beta1ColorInfoIn"] = t.struct(
        {
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "pixelFraction": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ColorInfoIn"])
    types["GoogleCloudVisionV1p3beta1ColorInfoOut"] = t.struct(
        {
            "score": t.number().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "pixelFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ColorInfoOut"])
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
    types["GoogleCloudVisionV1p1beta1SymbolIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "text": t.string().optional(),
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
            "confidence": t.number().optional(),
            "text": t.string().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p1beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1SymbolOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "score": t.number().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"])
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
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
            "indexTime": t.string().optional(),
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
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "indexTime": t.string().optional(),
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
    types["NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["NormalizedVertexIn"])
    types["NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NormalizedVertexOut"])
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
    types["GoogleCloudVisionV1p4beta1FaceAnnotationIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "blurredLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "recognitionResult": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceRecognitionResultIn"])
            ).optional(),
            "panAngle": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "sorrowLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p4beta1FaceAnnotationOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "blurredLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "headwearLikelihood": t.string().optional(),
            "landmarkingConfidence": t.number().optional(),
            "detectionConfidence": t.number().optional(),
            "underExposedLikelihood": t.string().optional(),
            "recognitionResult": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceRecognitionResultOut"])
            ).optional(),
            "panAngle": t.number().optional(),
            "angerLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "sorrowLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1FaceAnnotationOut"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsIn"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultIn"
                    ]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsIn"])
    types["GoogleCloudVisionV1p4beta1ProductSearchResultsOut"] = t.struct(
        {
            "productGroupedResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResultOut"
                    ]
                )
            ).optional(),
            "indexTime": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1ProductSearchResultsResultOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ProductSearchResultsOut"])
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
    types["ColorInfoIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "pixelFraction": t.number().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["ColorInfoIn"])
    types["ColorInfoOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "pixelFraction": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorInfoOut"])
    types[
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p4beta1ProductSearchResultsObjectAnnotationOut"]
    )
    types["GoogleCloudVisionV1p1beta1VertexIn"] = t.struct(
        {"x": t.integer().optional(), "y": t.integer().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1VertexIn"])
    types["GoogleCloudVisionV1p1beta1VertexOut"] = t.struct(
        {
            "x": t.integer().optional(),
            "y": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1VertexOut"])
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
    types["GoogleCloudVisionV1p4beta1NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1NormalizedVertexIn"])
    types["GoogleCloudVisionV1p4beta1NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1NormalizedVertexOut"])
    types[
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn"
    ] = t.struct(
        {
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationIn"]
    )
    types[
        "GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut"
    ] = t.struct(
        {
            "mid": t.string().optional(),
            "name": t.string().optional(),
            "score": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVisionV1p3beta1ProductSearchResultsObjectAnnotationOut"]
    )
    types["WebDetectionIn"] = t.struct(
        {
            "partialMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "visuallySimilarImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "bestGuessLabels": t.array(t.proxy(renames["WebLabelIn"])).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["WebPageIn"])
            ).optional(),
            "webEntities": t.array(t.proxy(renames["WebEntityIn"])).optional(),
        }
    ).named(renames["WebDetectionIn"])
    types["WebDetectionOut"] = t.struct(
        {
            "partialMatchingImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageOut"])).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "bestGuessLabels": t.array(t.proxy(renames["WebLabelOut"])).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["WebPageOut"])
            ).optional(),
            "webEntities": t.array(t.proxy(renames["WebEntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebDetectionOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"] = t.struct(
        {"url": t.string().optional(), "score": t.number().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
    types["AsyncAnnotateFileRequestIn"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "inputConfig": t.proxy(renames["InputConfigIn"]),
            "features": t.array(t.proxy(renames["FeatureIn"])),
            "imageContext": t.proxy(renames["ImageContextIn"]).optional(),
        }
    ).named(renames["AsyncAnnotateFileRequestIn"])
    types["AsyncAnnotateFileRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "features": t.array(t.proxy(renames["FeatureOut"])),
            "imageContext": t.proxy(renames["ImageContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncAnnotateFileRequestOut"])
    types["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"] = t.struct(
        {
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationIn"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationIn"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextIn"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductSearchResultsIn"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationIn"])
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1CropHintsAnnotationIn"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImagePropertiesIn"]
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p4beta1WebDetectionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"] = t.struct(
        {
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1FaceAnnotationOut"])
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p4beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationOut"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImageAnnotationContextOut"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1SafeSearchAnnotationOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ProductSearchResultsOut"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1EntityAnnotationOut"])
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1CropHintsAnnotationOut"]
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p4beta1ImagePropertiesOut"]
            ).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p4beta1WebDetectionOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"])
    types["GoogleCloudVisionV1p4beta1WebDetectionIn"] = t.struct(
        {
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelIn"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageIn"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionIn"])
    types["GoogleCloudVisionV1p4beta1WebDetectionOut"] = t.struct(
        {
            "bestGuessLabels": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebLabelOut"])
            ).optional(),
            "webEntities": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebEntityOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "visuallySimilarImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebImageOut"])
            ).optional(),
            "pagesWithMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WebDetectionWebPageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1WebDetectionOut"])
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
    types["GoogleCloudVisionV1p2beta1ParagraphIn"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WordIn"])
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
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
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1ParagraphOut"])
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
    types["GoogleCloudVisionV1p4beta1BlockIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ParagraphIn"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "blockType": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BlockIn"])
    types["GoogleCloudVisionV1p4beta1BlockOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1ParagraphOut"])
            ).optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "blockType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1BlockOut"])
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
    types["FaceAnnotationIn"] = t.struct(
        {
            "panAngle": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "underExposedLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "fdBoundingPoly": t.proxy(renames["BoundingPolyIn"]).optional(),
            "blurredLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "landmarks": t.array(t.proxy(renames["LandmarkIn"])).optional(),
        }
    ).named(renames["FaceAnnotationIn"])
    types["FaceAnnotationOut"] = t.struct(
        {
            "panAngle": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "boundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "underExposedLikelihood": t.string().optional(),
            "rollAngle": t.number().optional(),
            "landmarkingConfidence": t.number().optional(),
            "surpriseLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "fdBoundingPoly": t.proxy(renames["BoundingPolyOut"]).optional(),
            "blurredLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "landmarks": t.array(t.proxy(renames["LandmarkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FaceAnnotationOut"])
    types["KeyValueIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
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
    types["GoogleCloudVisionV1p2beta1FaceAnnotationIn"] = t.struct(
        {
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "surpriseLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "underExposedLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "rollAngle": t.number().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkIn"])
            ).optional(),
            "landmarkingConfidence": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "blurredLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationIn"])
    types["GoogleCloudVisionV1p2beta1FaceAnnotationOut"] = t.struct(
        {
            "fdBoundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "surpriseLikelihood": t.string().optional(),
            "tiltAngle": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "underExposedLikelihood": t.string().optional(),
            "joyLikelihood": t.string().optional(),
            "detectionConfidence": t.number().optional(),
            "rollAngle": t.number().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1FaceAnnotationLandmarkOut"])
            ).optional(),
            "landmarkingConfidence": t.number().optional(),
            "headwearLikelihood": t.string().optional(),
            "panAngle": t.number().optional(),
            "blurredLikelihood": t.string().optional(),
            "sorrowLikelihood": t.string().optional(),
            "angerLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1FaceAnnotationOut"])
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
    types["WebPageIn"] = t.struct(
        {
            "url": t.string().optional(),
            "pageTitle": t.string().optional(),
            "score": t.number().optional(),
            "partialMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageIn"])).optional(),
        }
    ).named(renames["WebPageIn"])
    types["WebPageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "pageTitle": t.string().optional(),
            "score": t.number().optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["WebImageOut"])
            ).optional(),
            "fullMatchingImages": t.array(t.proxy(renames["WebImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebPageOut"])
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
    types["GoogleCloudVisionV1p4beta1AnnotateFileResponseIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1InputConfigIn"]
            ).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateFileResponseIn"])
    types["GoogleCloudVisionV1p4beta1AnnotateFileResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudVisionV1p4beta1InputConfigOut"]
            ).optional(),
            "totalPages": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1AnnotateImageResponseOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1AnnotateFileResponseOut"])
    types["GoogleCloudVisionV1p3beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p3beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p3beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1GcsSourceOut"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"] = t.struct(
        {
            "score": t.number().optional(),
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageIn"])
            ).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageIn"])
    types["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"] = t.struct(
        {
            "score": t.number().optional(),
            "pageTitle": t.string().optional(),
            "fullMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "partialMatchingImages": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1WebDetectionWebImageOut"])
            ).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1WebDetectionWebPageOut"])
    types["ParagraphIn"] = t.struct(
        {
            "property": t.proxy(renames["TextPropertyIn"]).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyIn"]).optional(),
            "words": t.array(t.proxy(renames["WordIn"])).optional(),
        }
    ).named(renames["ParagraphIn"])
    types["ParagraphOut"] = t.struct(
        {
            "property": t.proxy(renames["TextPropertyOut"]).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(renames["BoundingPolyOut"]).optional(),
            "words": t.array(t.proxy(renames["WordOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphOut"])
    types["GoogleCloudVisionV1p4beta1SymbolIn"] = t.struct(
        {
            "text": t.string().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SymbolIn"])
    types["GoogleCloudVisionV1p4beta1SymbolOut"] = t.struct(
        {
            "text": t.string().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1SymbolOut"])
    types["PositionIn"] = t.struct(
        {
            "y": t.number().optional(),
            "z": t.number().optional(),
            "x": t.number().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "y": t.number().optional(),
            "z": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
    types["GoogleCloudVisionV1p4beta1GcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p4beta1GcsSourceIn"])
    types["GoogleCloudVisionV1p4beta1GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1GcsSourceOut"])
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
    types["ProductSearchResultsIn"] = t.struct(
        {
            "results": t.array(t.proxy(renames["ResultIn"])).optional(),
            "productGroupedResults": t.array(
                t.proxy(renames["GroupedResultIn"])
            ).optional(),
            "indexTime": t.string().optional(),
        }
    ).named(renames["ProductSearchResultsIn"])
    types["ProductSearchResultsOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["ResultOut"])).optional(),
            "productGroupedResults": t.array(
                t.proxy(renames["GroupedResultOut"])
            ).optional(),
            "indexTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSearchResultsOut"])
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
    types["GoogleCloudVisionV1p4beta1ParagraphIn"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyIn"]
            ).optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WordIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ParagraphIn"])
    types["GoogleCloudVisionV1p4beta1ParagraphOut"] = t.struct(
        {
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p4beta1BoundingPolyOut"]
            ).optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1WordOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1ParagraphOut"])
    types["AsyncBatchAnnotateFilesRequestIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "requests": t.array(t.proxy(renames["AsyncAnnotateFileRequestIn"])),
        }
    ).named(renames["AsyncBatchAnnotateFilesRequestIn"])
    types["AsyncBatchAnnotateFilesRequestOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "requests": t.array(t.proxy(renames["AsyncAnnotateFileRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateFilesRequestOut"])
    types["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"] = t.struct(
        {
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationIn"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationIn"])
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1CropHintsAnnotationIn"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductSearchResultsIn"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImagePropertiesIn"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationIn"]
                )
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextIn"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationIn"]
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p1beta1WebDetectionIn"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseIn"])
    types["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"] = t.struct(
        {
            "safeSearchAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1SafeSearchAnnotationOut"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1FaceAnnotationOut"])
            ).optional(),
            "cropHintsAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1CropHintsAnnotationOut"]
            ).optional(),
            "productSearchResults": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ProductSearchResultsOut"]
            ).optional(),
            "landmarkAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "logoAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
            "imagePropertiesAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImagePropertiesOut"]
            ).optional(),
            "localizedObjectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVisionV1p1beta1LocalizedObjectAnnotationOut"]
                )
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudVisionV1p1beta1ImageAnnotationContextOut"]
            ).optional(),
            "fullTextAnnotation": t.proxy(
                renames["GoogleCloudVisionV1p1beta1TextAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "webDetection": t.proxy(
                renames["GoogleCloudVisionV1p1beta1WebDetectionOut"]
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVisionV1p1beta1EntityAnnotationOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1AnnotateImageResponseOut"])
    types["AsyncAnnotateFileResponseIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"]).optional()}
    ).named(renames["AsyncAnnotateFileResponseIn"])
    types["AsyncAnnotateFileResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncAnnotateFileResponseOut"])
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
    types["GoogleCloudVisionV1p4beta1PageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "width": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BlockIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PageIn"])
    types["GoogleCloudVisionV1p4beta1PageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "confidence": t.number().optional(),
            "property": t.proxy(
                renames["GoogleCloudVisionV1p4beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "width": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudVisionV1p4beta1BlockOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p4beta1PageOut"])
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
    types["ImageIn"] = t.struct(
        {
            "source": t.proxy(renames["ImageSourceIn"]).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "source": t.proxy(renames["ImageSourceOut"]).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["GoogleCloudVisionV1p3beta1CropHintIn"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1CropHintIn"])
    types["GoogleCloudVisionV1p3beta1CropHintOut"] = t.struct(
        {
            "importanceFraction": t.number().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1CropHintOut"])
    types["GoogleCloudVisionV1p1beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudVisionV1p1beta1GcsDestinationIn"])
    types["GoogleCloudVisionV1p1beta1GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p1beta1GcsDestinationOut"])
    types["GoogleCloudVisionV1p2beta1BlockIn"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyIn"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ParagraphIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyIn"]
            ).optional(),
            "blockType": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BlockIn"])
    types["GoogleCloudVisionV1p2beta1BlockOut"] = t.struct(
        {
            "property": t.proxy(
                renames["GoogleCloudVisionV1p2beta1TextAnnotationTextPropertyOut"]
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudVisionV1p2beta1ParagraphOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "boundingBox": t.proxy(
                renames["GoogleCloudVisionV1p2beta1BoundingPolyOut"]
            ).optional(),
            "blockType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1BlockOut"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"] = t.struct(
        {
            "image": t.string().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductIn"]
            ).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultIn"])
    types["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"] = t.struct(
        {
            "image": t.string().optional(),
            "product": t.proxy(
                renames["GoogleCloudVisionV1p3beta1ProductOut"]
            ).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1ProductSearchResultsResultOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GoogleCloudVisionV1p2beta1LocationInfoIn"] = t.struct(
        {"latLng": t.proxy(renames["LatLngIn"]).optional()}
    ).named(renames["GoogleCloudVisionV1p2beta1LocationInfoIn"])
    types["GoogleCloudVisionV1p2beta1LocationInfoOut"] = t.struct(
        {
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1LocationInfoOut"])
    types["AsyncBatchAnnotateImagesRequestIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
        }
    ).named(renames["AsyncBatchAnnotateImagesRequestIn"])
    types["AsyncBatchAnnotateImagesRequestOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "requests": t.array(t.proxy(renames["AnnotateImageRequestOut"])),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsyncBatchAnnotateImagesRequestOut"])
    types["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"] = t.struct(
        {
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationIn"])
    types["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"] = t.struct(
        {
            "score": t.number().optional(),
            "mid": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudVisionV1p3beta1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p3beta1LocalizedObjectAnnotationOut"])
    types["GoogleCloudVisionV1p2beta1PropertyIn"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PropertyIn"])
    types["GoogleCloudVisionV1p2beta1PropertyOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "uint64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVisionV1p2beta1PropertyOut"])

    functions = {}
    functions["operationsGet"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsOperationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsAddProduct"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsPatch"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsGet"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsList"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsCreate"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsImport"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsRemoveProduct"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductSetsDelete"] = vision.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsFilesAsyncBatchAnnotate"] = vision.post(
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
    functions["projectsLocationsFilesAnnotate"] = vision.post(
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
    functions["projectsLocationsOperationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsPurge"] = vision.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "productCategory": t.string().optional(),
                "displayName": t.string().optional(),
                "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsGet"] = vision.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "productCategory": t.string().optional(),
                "displayName": t.string().optional(),
                "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCreate"] = vision.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "productCategory": t.string().optional(),
                "displayName": t.string().optional(),
                "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsList"] = vision.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "productCategory": t.string().optional(),
                "displayName": t.string().optional(),
                "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsDelete"] = vision.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "productCategory": t.string().optional(),
                "displayName": t.string().optional(),
                "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsPatch"] = vision.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "productCategory": t.string().optional(),
                "displayName": t.string().optional(),
                "productLabels": t.array(t.proxy(renames["KeyValueIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesDelete"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReferenceImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesList"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReferenceImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesCreate"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReferenceImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsReferenceImagesGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReferenceImageOut"]),
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
    functions["locationsOperationsGet"] = vision.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesAsyncBatchAnnotate"] = vision.post(
        "v1/files:annotate",
        t.struct(
            {
                "requests": t.array(t.proxy(renames["AnnotateFileRequestIn"])),
                "parent": t.string().optional(),
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
                "requests": t.array(t.proxy(renames["AnnotateFileRequestIn"])),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchAnnotateFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["imagesAnnotate"] = vision.post(
        "v1/images:asyncBatchAnnotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
                "outputConfig": t.proxy(renames["OutputConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["imagesAsyncBatchAnnotate"] = vision.post(
        "v1/images:asyncBatchAnnotate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(t.proxy(renames["AnnotateImageRequestIn"])),
                "outputConfig": t.proxy(renames["OutputConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vision", renames=renames, types=Box(types), functions=Box(functions)
    )
