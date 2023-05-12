from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_slides() -> Import:
    slides = HTTPRuntime("https://slides.googleapis.com/")

    renames = {
        "ErrorResponse": "_slides_1_ErrorResponse",
        "CreateLineResponseIn": "_slides_2_CreateLineResponseIn",
        "CreateLineResponseOut": "_slides_3_CreateLineResponseOut",
        "BatchUpdatePresentationRequestIn": "_slides_4_BatchUpdatePresentationRequestIn",
        "BatchUpdatePresentationRequestOut": "_slides_5_BatchUpdatePresentationRequestOut",
        "RgbColorIn": "_slides_6_RgbColorIn",
        "RgbColorOut": "_slides_7_RgbColorOut",
        "ParagraphMarkerIn": "_slides_8_ParagraphMarkerIn",
        "ParagraphMarkerOut": "_slides_9_ParagraphMarkerOut",
        "DuplicateObjectResponseIn": "_slides_10_DuplicateObjectResponseIn",
        "DuplicateObjectResponseOut": "_slides_11_DuplicateObjectResponseOut",
        "PageElementIn": "_slides_12_PageElementIn",
        "PageElementOut": "_slides_13_PageElementOut",
        "CreateParagraphBulletsRequestIn": "_slides_14_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_slides_15_CreateParagraphBulletsRequestOut",
        "UpdateSlidesPositionRequestIn": "_slides_16_UpdateSlidesPositionRequestIn",
        "UpdateSlidesPositionRequestOut": "_slides_17_UpdateSlidesPositionRequestOut",
        "UpdateTableRowPropertiesRequestIn": "_slides_18_UpdateTableRowPropertiesRequestIn",
        "UpdateTableRowPropertiesRequestOut": "_slides_19_UpdateTableRowPropertiesRequestOut",
        "PageElementPropertiesIn": "_slides_20_PageElementPropertiesIn",
        "PageElementPropertiesOut": "_slides_21_PageElementPropertiesOut",
        "DeleteParagraphBulletsRequestIn": "_slides_22_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_slides_23_DeleteParagraphBulletsRequestOut",
        "ColorStopIn": "_slides_24_ColorStopIn",
        "ColorStopOut": "_slides_25_ColorStopOut",
        "RerouteLineRequestIn": "_slides_26_RerouteLineRequestIn",
        "RerouteLineRequestOut": "_slides_27_RerouteLineRequestOut",
        "TextStyleIn": "_slides_28_TextStyleIn",
        "TextStyleOut": "_slides_29_TextStyleOut",
        "CreateShapeResponseIn": "_slides_30_CreateShapeResponseIn",
        "CreateShapeResponseOut": "_slides_31_CreateShapeResponseOut",
        "LayoutPropertiesIn": "_slides_32_LayoutPropertiesIn",
        "LayoutPropertiesOut": "_slides_33_LayoutPropertiesOut",
        "TableCellPropertiesIn": "_slides_34_TableCellPropertiesIn",
        "TableCellPropertiesOut": "_slides_35_TableCellPropertiesOut",
        "StretchedPictureFillIn": "_slides_36_StretchedPictureFillIn",
        "StretchedPictureFillOut": "_slides_37_StretchedPictureFillOut",
        "UpdateParagraphStyleRequestIn": "_slides_38_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_slides_39_UpdateParagraphStyleRequestOut",
        "UpdateImagePropertiesRequestIn": "_slides_40_UpdateImagePropertiesRequestIn",
        "UpdateImagePropertiesRequestOut": "_slides_41_UpdateImagePropertiesRequestOut",
        "AffineTransformIn": "_slides_42_AffineTransformIn",
        "AffineTransformOut": "_slides_43_AffineTransformOut",
        "OpaqueColorIn": "_slides_44_OpaqueColorIn",
        "OpaqueColorOut": "_slides_45_OpaqueColorOut",
        "ResponseIn": "_slides_46_ResponseIn",
        "ResponseOut": "_slides_47_ResponseOut",
        "MasterPropertiesIn": "_slides_48_MasterPropertiesIn",
        "MasterPropertiesOut": "_slides_49_MasterPropertiesOut",
        "TextElementIn": "_slides_50_TextElementIn",
        "TextElementOut": "_slides_51_TextElementOut",
        "SlidePropertiesIn": "_slides_52_SlidePropertiesIn",
        "SlidePropertiesOut": "_slides_53_SlidePropertiesOut",
        "UpdateTableColumnPropertiesRequestIn": "_slides_54_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_slides_55_UpdateTableColumnPropertiesRequestOut",
        "TableCellLocationIn": "_slides_56_TableCellLocationIn",
        "TableCellLocationOut": "_slides_57_TableCellLocationOut",
        "SizeIn": "_slides_58_SizeIn",
        "SizeOut": "_slides_59_SizeOut",
        "CreateTableResponseIn": "_slides_60_CreateTableResponseIn",
        "CreateTableResponseOut": "_slides_61_CreateTableResponseOut",
        "ReplaceImageRequestIn": "_slides_62_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_slides_63_ReplaceImageRequestOut",
        "WriteControlIn": "_slides_64_WriteControlIn",
        "WriteControlOut": "_slides_65_WriteControlOut",
        "ReplaceAllShapesWithSheetsChartRequestIn": "_slides_66_ReplaceAllShapesWithSheetsChartRequestIn",
        "ReplaceAllShapesWithSheetsChartRequestOut": "_slides_67_ReplaceAllShapesWithSheetsChartRequestOut",
        "TableColumnPropertiesIn": "_slides_68_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_slides_69_TableColumnPropertiesOut",
        "CreateVideoResponseIn": "_slides_70_CreateVideoResponseIn",
        "CreateVideoResponseOut": "_slides_71_CreateVideoResponseOut",
        "UpdateTextStyleRequestIn": "_slides_72_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_slides_73_UpdateTextStyleRequestOut",
        "UpdateLineCategoryRequestIn": "_slides_74_UpdateLineCategoryRequestIn",
        "UpdateLineCategoryRequestOut": "_slides_75_UpdateLineCategoryRequestOut",
        "TableRowIn": "_slides_76_TableRowIn",
        "TableRowOut": "_slides_77_TableRowOut",
        "MergeTableCellsRequestIn": "_slides_78_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_slides_79_MergeTableCellsRequestOut",
        "LinePropertiesIn": "_slides_80_LinePropertiesIn",
        "LinePropertiesOut": "_slides_81_LinePropertiesOut",
        "AutofitIn": "_slides_82_AutofitIn",
        "AutofitOut": "_slides_83_AutofitOut",
        "SheetsChartPropertiesIn": "_slides_84_SheetsChartPropertiesIn",
        "SheetsChartPropertiesOut": "_slides_85_SheetsChartPropertiesOut",
        "InsertTableRowsRequestIn": "_slides_86_InsertTableRowsRequestIn",
        "InsertTableRowsRequestOut": "_slides_87_InsertTableRowsRequestOut",
        "DeleteTableColumnRequestIn": "_slides_88_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_slides_89_DeleteTableColumnRequestOut",
        "ParagraphStyleIn": "_slides_90_ParagraphStyleIn",
        "ParagraphStyleOut": "_slides_91_ParagraphStyleOut",
        "RequestIn": "_slides_92_RequestIn",
        "RequestOut": "_slides_93_RequestOut",
        "CreateShapeRequestIn": "_slides_94_CreateShapeRequestIn",
        "CreateShapeRequestOut": "_slides_95_CreateShapeRequestOut",
        "PresentationIn": "_slides_96_PresentationIn",
        "PresentationOut": "_slides_97_PresentationOut",
        "DuplicateObjectRequestIn": "_slides_98_DuplicateObjectRequestIn",
        "DuplicateObjectRequestOut": "_slides_99_DuplicateObjectRequestOut",
        "ColorSchemeIn": "_slides_100_ColorSchemeIn",
        "ColorSchemeOut": "_slides_101_ColorSchemeOut",
        "PageIn": "_slides_102_PageIn",
        "PageOut": "_slides_103_PageOut",
        "UnmergeTableCellsRequestIn": "_slides_104_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_slides_105_UnmergeTableCellsRequestOut",
        "TableRowPropertiesIn": "_slides_106_TableRowPropertiesIn",
        "TableRowPropertiesOut": "_slides_107_TableRowPropertiesOut",
        "DeleteTextRequestIn": "_slides_108_DeleteTextRequestIn",
        "DeleteTextRequestOut": "_slides_109_DeleteTextRequestOut",
        "ReplaceAllTextRequestIn": "_slides_110_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_slides_111_ReplaceAllTextRequestOut",
        "OptionalColorIn": "_slides_112_OptionalColorIn",
        "OptionalColorOut": "_slides_113_OptionalColorOut",
        "UpdatePageElementTransformRequestIn": "_slides_114_UpdatePageElementTransformRequestIn",
        "UpdatePageElementTransformRequestOut": "_slides_115_UpdatePageElementTransformRequestOut",
        "PlaceholderIn": "_slides_116_PlaceholderIn",
        "PlaceholderOut": "_slides_117_PlaceholderOut",
        "LineFillIn": "_slides_118_LineFillIn",
        "LineFillOut": "_slides_119_LineFillOut",
        "OutlineFillIn": "_slides_120_OutlineFillIn",
        "OutlineFillOut": "_slides_121_OutlineFillOut",
        "SubstringMatchCriteriaIn": "_slides_122_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_slides_123_SubstringMatchCriteriaOut",
        "ImageIn": "_slides_124_ImageIn",
        "ImageOut": "_slides_125_ImageOut",
        "ReplaceAllShapesWithSheetsChartResponseIn": "_slides_126_ReplaceAllShapesWithSheetsChartResponseIn",
        "ReplaceAllShapesWithSheetsChartResponseOut": "_slides_127_ReplaceAllShapesWithSheetsChartResponseOut",
        "ReplaceAllTextResponseIn": "_slides_128_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_slides_129_ReplaceAllTextResponseOut",
        "CreateVideoRequestIn": "_slides_130_CreateVideoRequestIn",
        "CreateVideoRequestOut": "_slides_131_CreateVideoRequestOut",
        "InsertTextRequestIn": "_slides_132_InsertTextRequestIn",
        "InsertTextRequestOut": "_slides_133_InsertTextRequestOut",
        "ImagePropertiesIn": "_slides_134_ImagePropertiesIn",
        "ImagePropertiesOut": "_slides_135_ImagePropertiesOut",
        "TableBorderFillIn": "_slides_136_TableBorderFillIn",
        "TableBorderFillOut": "_slides_137_TableBorderFillOut",
        "SheetsChartIn": "_slides_138_SheetsChartIn",
        "SheetsChartOut": "_slides_139_SheetsChartOut",
        "ThumbnailIn": "_slides_140_ThumbnailIn",
        "ThumbnailOut": "_slides_141_ThumbnailOut",
        "ListIn": "_slides_142_ListIn",
        "ListOut": "_slides_143_ListOut",
        "TextRunIn": "_slides_144_TextRunIn",
        "TextRunOut": "_slides_145_TextRunOut",
        "RecolorIn": "_slides_146_RecolorIn",
        "RecolorOut": "_slides_147_RecolorOut",
        "LinkIn": "_slides_148_LinkIn",
        "LinkOut": "_slides_149_LinkOut",
        "LayoutPlaceholderIdMappingIn": "_slides_150_LayoutPlaceholderIdMappingIn",
        "LayoutPlaceholderIdMappingOut": "_slides_151_LayoutPlaceholderIdMappingOut",
        "VideoIn": "_slides_152_VideoIn",
        "VideoOut": "_slides_153_VideoOut",
        "UpdatePageElementsZOrderRequestIn": "_slides_154_UpdatePageElementsZOrderRequestIn",
        "UpdatePageElementsZOrderRequestOut": "_slides_155_UpdatePageElementsZOrderRequestOut",
        "ShadowIn": "_slides_156_ShadowIn",
        "ShadowOut": "_slides_157_ShadowOut",
        "TableBorderPropertiesIn": "_slides_158_TableBorderPropertiesIn",
        "TableBorderPropertiesOut": "_slides_159_TableBorderPropertiesOut",
        "UpdateTableCellPropertiesRequestIn": "_slides_160_UpdateTableCellPropertiesRequestIn",
        "UpdateTableCellPropertiesRequestOut": "_slides_161_UpdateTableCellPropertiesRequestOut",
        "UpdateVideoPropertiesRequestIn": "_slides_162_UpdateVideoPropertiesRequestIn",
        "UpdateVideoPropertiesRequestOut": "_slides_163_UpdateVideoPropertiesRequestOut",
        "AutoTextIn": "_slides_164_AutoTextIn",
        "AutoTextOut": "_slides_165_AutoTextOut",
        "RangeIn": "_slides_166_RangeIn",
        "RangeOut": "_slides_167_RangeOut",
        "RefreshSheetsChartRequestIn": "_slides_168_RefreshSheetsChartRequestIn",
        "RefreshSheetsChartRequestOut": "_slides_169_RefreshSheetsChartRequestOut",
        "VideoPropertiesIn": "_slides_170_VideoPropertiesIn",
        "VideoPropertiesOut": "_slides_171_VideoPropertiesOut",
        "ShapeBackgroundFillIn": "_slides_172_ShapeBackgroundFillIn",
        "ShapeBackgroundFillOut": "_slides_173_ShapeBackgroundFillOut",
        "CreateImageRequestIn": "_slides_174_CreateImageRequestIn",
        "CreateImageRequestOut": "_slides_175_CreateImageRequestOut",
        "CreateSlideResponseIn": "_slides_176_CreateSlideResponseIn",
        "CreateSlideResponseOut": "_slides_177_CreateSlideResponseOut",
        "OutlineIn": "_slides_178_OutlineIn",
        "OutlineOut": "_slides_179_OutlineOut",
        "InsertTableColumnsRequestIn": "_slides_180_InsertTableColumnsRequestIn",
        "InsertTableColumnsRequestOut": "_slides_181_InsertTableColumnsRequestOut",
        "DimensionIn": "_slides_182_DimensionIn",
        "DimensionOut": "_slides_183_DimensionOut",
        "CreateSheetsChartRequestIn": "_slides_184_CreateSheetsChartRequestIn",
        "CreateSheetsChartRequestOut": "_slides_185_CreateSheetsChartRequestOut",
        "UpdateSlidePropertiesRequestIn": "_slides_186_UpdateSlidePropertiesRequestIn",
        "UpdateSlidePropertiesRequestOut": "_slides_187_UpdateSlidePropertiesRequestOut",
        "UngroupObjectsRequestIn": "_slides_188_UngroupObjectsRequestIn",
        "UngroupObjectsRequestOut": "_slides_189_UngroupObjectsRequestOut",
        "LineIn": "_slides_190_LineIn",
        "LineOut": "_slides_191_LineOut",
        "NotesPropertiesIn": "_slides_192_NotesPropertiesIn",
        "NotesPropertiesOut": "_slides_193_NotesPropertiesOut",
        "DeleteObjectRequestIn": "_slides_194_DeleteObjectRequestIn",
        "DeleteObjectRequestOut": "_slides_195_DeleteObjectRequestOut",
        "NestingLevelIn": "_slides_196_NestingLevelIn",
        "NestingLevelOut": "_slides_197_NestingLevelOut",
        "PageBackgroundFillIn": "_slides_198_PageBackgroundFillIn",
        "PageBackgroundFillOut": "_slides_199_PageBackgroundFillOut",
        "ThemeColorPairIn": "_slides_200_ThemeColorPairIn",
        "ThemeColorPairOut": "_slides_201_ThemeColorPairOut",
        "TableIn": "_slides_202_TableIn",
        "TableOut": "_slides_203_TableOut",
        "ShapeIn": "_slides_204_ShapeIn",
        "ShapeOut": "_slides_205_ShapeOut",
        "CreateTableRequestIn": "_slides_206_CreateTableRequestIn",
        "CreateTableRequestOut": "_slides_207_CreateTableRequestOut",
        "LineConnectionIn": "_slides_208_LineConnectionIn",
        "LineConnectionOut": "_slides_209_LineConnectionOut",
        "LayoutReferenceIn": "_slides_210_LayoutReferenceIn",
        "LayoutReferenceOut": "_slides_211_LayoutReferenceOut",
        "ShapePropertiesIn": "_slides_212_ShapePropertiesIn",
        "ShapePropertiesOut": "_slides_213_ShapePropertiesOut",
        "GroupObjectsRequestIn": "_slides_214_GroupObjectsRequestIn",
        "GroupObjectsRequestOut": "_slides_215_GroupObjectsRequestOut",
        "ReplaceAllShapesWithImageResponseIn": "_slides_216_ReplaceAllShapesWithImageResponseIn",
        "ReplaceAllShapesWithImageResponseOut": "_slides_217_ReplaceAllShapesWithImageResponseOut",
        "TableCellBackgroundFillIn": "_slides_218_TableCellBackgroundFillIn",
        "TableCellBackgroundFillOut": "_slides_219_TableCellBackgroundFillOut",
        "TableRangeIn": "_slides_220_TableRangeIn",
        "TableRangeOut": "_slides_221_TableRangeOut",
        "WordArtIn": "_slides_222_WordArtIn",
        "WordArtOut": "_slides_223_WordArtOut",
        "GroupIn": "_slides_224_GroupIn",
        "GroupOut": "_slides_225_GroupOut",
        "TableBorderRowIn": "_slides_226_TableBorderRowIn",
        "TableBorderRowOut": "_slides_227_TableBorderRowOut",
        "CropPropertiesIn": "_slides_228_CropPropertiesIn",
        "CropPropertiesOut": "_slides_229_CropPropertiesOut",
        "UpdatePageElementAltTextRequestIn": "_slides_230_UpdatePageElementAltTextRequestIn",
        "UpdatePageElementAltTextRequestOut": "_slides_231_UpdatePageElementAltTextRequestOut",
        "BatchUpdatePresentationResponseIn": "_slides_232_BatchUpdatePresentationResponseIn",
        "BatchUpdatePresentationResponseOut": "_slides_233_BatchUpdatePresentationResponseOut",
        "ReplaceAllShapesWithImageRequestIn": "_slides_234_ReplaceAllShapesWithImageRequestIn",
        "ReplaceAllShapesWithImageRequestOut": "_slides_235_ReplaceAllShapesWithImageRequestOut",
        "UpdateShapePropertiesRequestIn": "_slides_236_UpdateShapePropertiesRequestIn",
        "UpdateShapePropertiesRequestOut": "_slides_237_UpdateShapePropertiesRequestOut",
        "TextContentIn": "_slides_238_TextContentIn",
        "TextContentOut": "_slides_239_TextContentOut",
        "CreateImageResponseIn": "_slides_240_CreateImageResponseIn",
        "CreateImageResponseOut": "_slides_241_CreateImageResponseOut",
        "CreateSlideRequestIn": "_slides_242_CreateSlideRequestIn",
        "CreateSlideRequestOut": "_slides_243_CreateSlideRequestOut",
        "UpdateTableBorderPropertiesRequestIn": "_slides_244_UpdateTableBorderPropertiesRequestIn",
        "UpdateTableBorderPropertiesRequestOut": "_slides_245_UpdateTableBorderPropertiesRequestOut",
        "TableCellIn": "_slides_246_TableCellIn",
        "TableCellOut": "_slides_247_TableCellOut",
        "PagePropertiesIn": "_slides_248_PagePropertiesIn",
        "PagePropertiesOut": "_slides_249_PagePropertiesOut",
        "DeleteTableRowRequestIn": "_slides_250_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_slides_251_DeleteTableRowRequestOut",
        "UpdateLinePropertiesRequestIn": "_slides_252_UpdateLinePropertiesRequestIn",
        "UpdateLinePropertiesRequestOut": "_slides_253_UpdateLinePropertiesRequestOut",
        "WeightedFontFamilyIn": "_slides_254_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_slides_255_WeightedFontFamilyOut",
        "UpdatePagePropertiesRequestIn": "_slides_256_UpdatePagePropertiesRequestIn",
        "UpdatePagePropertiesRequestOut": "_slides_257_UpdatePagePropertiesRequestOut",
        "TableBorderCellIn": "_slides_258_TableBorderCellIn",
        "TableBorderCellOut": "_slides_259_TableBorderCellOut",
        "BulletIn": "_slides_260_BulletIn",
        "BulletOut": "_slides_261_BulletOut",
        "CreateLineRequestIn": "_slides_262_CreateLineRequestIn",
        "CreateLineRequestOut": "_slides_263_CreateLineRequestOut",
        "CreateSheetsChartResponseIn": "_slides_264_CreateSheetsChartResponseIn",
        "CreateSheetsChartResponseOut": "_slides_265_CreateSheetsChartResponseOut",
        "SolidFillIn": "_slides_266_SolidFillIn",
        "SolidFillOut": "_slides_267_SolidFillOut",
        "GroupObjectsResponseIn": "_slides_268_GroupObjectsResponseIn",
        "GroupObjectsResponseOut": "_slides_269_GroupObjectsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CreateLineResponseIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["CreateLineResponseIn"]
    )
    types["CreateLineResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineResponseOut"])
    types["BatchUpdatePresentationRequestIn"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
        }
    ).named(renames["BatchUpdatePresentationRequestIn"])
    types["BatchUpdatePresentationRequestOut"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "requests": t.array(t.proxy(renames["RequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePresentationRequestOut"])
    types["RgbColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["RgbColorIn"])
    types["RgbColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RgbColorOut"])
    types["ParagraphMarkerIn"] = t.struct(
        {
            "bullet": t.proxy(renames["BulletIn"]).optional(),
            "style": t.proxy(renames["ParagraphStyleIn"]).optional(),
        }
    ).named(renames["ParagraphMarkerIn"])
    types["ParagraphMarkerOut"] = t.struct(
        {
            "bullet": t.proxy(renames["BulletOut"]).optional(),
            "style": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphMarkerOut"])
    types["DuplicateObjectResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DuplicateObjectResponseIn"])
    types["DuplicateObjectResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateObjectResponseOut"])
    types["PageElementIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementGroup": t.proxy(renames["GroupIn"]).optional(),
            "shape": t.proxy(renames["ShapeIn"]).optional(),
            "sheetsChart": t.proxy(renames["SheetsChartIn"]).optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "line": t.proxy(renames["LineIn"]).optional(),
            "video": t.proxy(renames["VideoIn"]).optional(),
            "wordArt": t.proxy(renames["WordArtIn"]).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["PageElementIn"])
    types["PageElementOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementGroup": t.proxy(renames["GroupOut"]).optional(),
            "shape": t.proxy(renames["ShapeOut"]).optional(),
            "sheetsChart": t.proxy(renames["SheetsChartOut"]).optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "line": t.proxy(renames["LineOut"]).optional(),
            "video": t.proxy(renames["VideoOut"]).optional(),
            "wordArt": t.proxy(renames["WordArtOut"]).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementOut"])
    types["CreateParagraphBulletsRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "bulletPreset": t.string().optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestIn"])
    types["CreateParagraphBulletsRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "bulletPreset": t.string().optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestOut"])
    types["UpdateSlidesPositionRequestIn"] = t.struct(
        {
            "slideObjectIds": t.array(t.string()).optional(),
            "insertionIndex": t.integer().optional(),
        }
    ).named(renames["UpdateSlidesPositionRequestIn"])
    types["UpdateSlidesPositionRequestOut"] = t.struct(
        {
            "slideObjectIds": t.array(t.string()).optional(),
            "insertionIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlidesPositionRequestOut"])
    types["UpdateTableRowPropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestIn"])
    types["UpdateTableRowPropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestOut"])
    types["PageElementPropertiesIn"] = t.struct(
        {
            "size": t.proxy(renames["SizeIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "pageObjectId": t.string().optional(),
        }
    ).named(renames["PageElementPropertiesIn"])
    types["PageElementPropertiesOut"] = t.struct(
        {
            "size": t.proxy(renames["SizeOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "pageObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementPropertiesOut"])
    types["DeleteParagraphBulletsRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestIn"])
    types["DeleteParagraphBulletsRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestOut"])
    types["ColorStopIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "position": t.number().optional(),
        }
    ).named(renames["ColorStopIn"])
    types["ColorStopOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "position": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorStopOut"])
    types["RerouteLineRequestIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["RerouteLineRequestIn"]
    )
    types["RerouteLineRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RerouteLineRequestOut"])
    types["TextStyleIn"] = t.struct(
        {
            "fontFamily": t.string().optional(),
            "italic": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "strikethrough": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
            "baselineOffset": t.string().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "bold": t.boolean().optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "fontFamily": t.string().optional(),
            "italic": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "strikethrough": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "baselineOffset": t.string().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "bold": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
    types["CreateShapeResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateShapeResponseIn"])
    types["CreateShapeResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeResponseOut"])
    types["LayoutPropertiesIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "masterObjectId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LayoutPropertiesIn"])
    types["LayoutPropertiesOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "masterObjectId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutPropertiesOut"])
    types["TableCellPropertiesIn"] = t.struct(
        {
            "contentAlignment": t.string().optional(),
            "tableCellBackgroundFill": t.proxy(
                renames["TableCellBackgroundFillIn"]
            ).optional(),
        }
    ).named(renames["TableCellPropertiesIn"])
    types["TableCellPropertiesOut"] = t.struct(
        {
            "contentAlignment": t.string().optional(),
            "tableCellBackgroundFill": t.proxy(
                renames["TableCellBackgroundFillOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellPropertiesOut"])
    types["StretchedPictureFillIn"] = t.struct(
        {
            "size": t.proxy(renames["SizeIn"]).optional(),
            "contentUrl": t.string().optional(),
        }
    ).named(renames["StretchedPictureFillIn"])
    types["StretchedPictureFillOut"] = t.struct(
        {
            "size": t.proxy(renames["SizeOut"]).optional(),
            "contentUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StretchedPictureFillOut"])
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "fields": t.string().optional(),
            "style": t.proxy(renames["ParagraphStyleIn"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "fields": t.string().optional(),
            "style": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])
    types["UpdateImagePropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateImagePropertiesRequestIn"])
    types["UpdateImagePropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateImagePropertiesRequestOut"])
    types["AffineTransformIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "shearX": t.number().optional(),
            "shearY": t.number().optional(),
            "translateY": t.number().optional(),
            "translateX": t.number().optional(),
            "scaleY": t.number().optional(),
            "scaleX": t.number().optional(),
        }
    ).named(renames["AffineTransformIn"])
    types["AffineTransformOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "shearX": t.number().optional(),
            "shearY": t.number().optional(),
            "translateY": t.number().optional(),
            "translateX": t.number().optional(),
            "scaleY": t.number().optional(),
            "scaleX": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AffineTransformOut"])
    types["OpaqueColorIn"] = t.struct(
        {
            "rgbColor": t.proxy(renames["RgbColorIn"]).optional(),
            "themeColor": t.string().optional(),
        }
    ).named(renames["OpaqueColorIn"])
    types["OpaqueColorOut"] = t.struct(
        {
            "rgbColor": t.proxy(renames["RgbColorOut"]).optional(),
            "themeColor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpaqueColorOut"])
    types["ResponseIn"] = t.struct(
        {
            "createImage": t.proxy(renames["CreateImageResponseIn"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseIn"]).optional(),
            "createLine": t.proxy(renames["CreateLineResponseIn"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseIn"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseIn"]).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectResponseIn"]).optional(),
            "createTable": t.proxy(renames["CreateTableResponseIn"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseIn"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseIn"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseIn"]).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "createImage": t.proxy(renames["CreateImageResponseOut"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseOut"]).optional(),
            "createLine": t.proxy(renames["CreateLineResponseOut"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseOut"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseOut"]).optional(),
            "duplicateObject": t.proxy(
                renames["DuplicateObjectResponseOut"]
            ).optional(),
            "createTable": t.proxy(renames["CreateTableResponseOut"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseOut"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseOut"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["MasterPropertiesIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["MasterPropertiesIn"])
    types["MasterPropertiesOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterPropertiesOut"])
    types["TextElementIn"] = t.struct(
        {
            "paragraphMarker": t.proxy(renames["ParagraphMarkerIn"]).optional(),
            "startIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["TextElementIn"])
    types["TextElementOut"] = t.struct(
        {
            "paragraphMarker": t.proxy(renames["ParagraphMarkerOut"]).optional(),
            "startIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextElementOut"])
    types["SlidePropertiesIn"] = t.struct(
        {
            "masterObjectId": t.string().optional(),
            "layoutObjectId": t.string().optional(),
            "isSkipped": t.boolean().optional(),
            "notesPage": t.proxy(renames["PageIn"]).optional(),
        }
    ).named(renames["SlidePropertiesIn"])
    types["SlidePropertiesOut"] = t.struct(
        {
            "masterObjectId": t.string().optional(),
            "layoutObjectId": t.string().optional(),
            "isSkipped": t.boolean().optional(),
            "notesPage": t.proxy(renames["PageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlidePropertiesOut"])
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "columnIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "columnIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["TableCellLocationIn"] = t.struct(
        {"rowIndex": t.integer().optional(), "columnIndex": t.integer().optional()}
    ).named(renames["TableCellLocationIn"])
    types["TableCellLocationOut"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellLocationOut"])
    types["SizeIn"] = t.struct(
        {
            "height": t.proxy(renames["DimensionIn"]).optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["SizeIn"])
    types["SizeOut"] = t.struct(
        {
            "height": t.proxy(renames["DimensionOut"]).optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SizeOut"])
    types["CreateTableResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateTableResponseIn"])
    types["CreateTableResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableResponseOut"])
    types["ReplaceImageRequestIn"] = t.struct(
        {
            "imageObjectId": t.string().optional(),
            "url": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
        }
    ).named(renames["ReplaceImageRequestIn"])
    types["ReplaceImageRequestOut"] = t.struct(
        {
            "imageObjectId": t.string().optional(),
            "url": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceImageRequestOut"])
    types["WriteControlIn"] = t.struct(
        {"requiredRevisionId": t.string().optional()}
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
    types["ReplaceAllShapesWithSheetsChartRequestIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "chartId": t.integer().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestIn"])
    types["ReplaceAllShapesWithSheetsChartRequestOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "chartId": t.integer().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestOut"])
    types["TableColumnPropertiesIn"] = t.struct(
        {"columnWidth": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableColumnPropertiesIn"])
    types["TableColumnPropertiesOut"] = t.struct(
        {
            "columnWidth": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableColumnPropertiesOut"])
    types["CreateVideoResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateVideoResponseIn"])
    types["CreateVideoResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoResponseOut"])
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "fields": t.string().optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "fields": t.string().optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
    types["UpdateLineCategoryRequestIn"] = t.struct(
        {"objectId": t.string().optional(), "lineCategory": t.string().optional()}
    ).named(renames["UpdateLineCategoryRequestIn"])
    types["UpdateLineCategoryRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "lineCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateLineCategoryRequestOut"])
    types["TableRowIn"] = t.struct(
        {
            "rowHeight": t.proxy(renames["DimensionIn"]).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
            "tableCells": t.array(t.proxy(renames["TableCellIn"])).optional(),
        }
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "rowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "tableCells": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["MergeTableCellsRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
        }
    ).named(renames["MergeTableCellsRequestIn"])
    types["MergeTableCellsRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeTableCellsRequestOut"])
    types["LinePropertiesIn"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "lineFill": t.proxy(renames["LineFillIn"]).optional(),
            "startConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "endArrow": t.string().optional(),
            "endConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "startArrow": t.string().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
        }
    ).named(renames["LinePropertiesIn"])
    types["LinePropertiesOut"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "lineFill": t.proxy(renames["LineFillOut"]).optional(),
            "startConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "endArrow": t.string().optional(),
            "endConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "startArrow": t.string().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinePropertiesOut"])
    types["AutofitIn"] = t.struct(
        {
            "lineSpacingReduction": t.number().optional(),
            "autofitType": t.string().optional(),
            "fontScale": t.number().optional(),
        }
    ).named(renames["AutofitIn"])
    types["AutofitOut"] = t.struct(
        {
            "lineSpacingReduction": t.number().optional(),
            "autofitType": t.string().optional(),
            "fontScale": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutofitOut"])
    types["SheetsChartPropertiesIn"] = t.struct(
        {"chartImageProperties": t.proxy(renames["ImagePropertiesIn"]).optional()}
    ).named(renames["SheetsChartPropertiesIn"])
    types["SheetsChartPropertiesOut"] = t.struct(
        {
            "chartImageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartPropertiesOut"])
    types["InsertTableRowsRequestIn"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "insertBelow": t.boolean().optional(),
            "number": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["InsertTableRowsRequestIn"])
    types["InsertTableRowsRequestOut"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "insertBelow": t.boolean().optional(),
            "number": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRowsRequestOut"])
    types["DeleteTableColumnRequestIn"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["DeleteTableColumnRequestIn"])
    types["DeleteTableColumnRequestOut"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableColumnRequestOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "direction": t.string().optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "spacingMode": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "lineSpacing": t.number().optional(),
            "alignment": t.string().optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "direction": t.string().optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "spacingMode": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "lineSpacing": t.number().optional(),
            "alignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
    types["RequestIn"] = t.struct(
        {
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestIn"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestIn"]).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestIn"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestIn"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestIn"]).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestIn"]
            ).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestIn"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestIn"]).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestIn"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestIn"]).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestIn"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestIn"]
            ).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestIn"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestIn"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestIn"]).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestIn"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestIn"]
            ).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestIn"]
            ).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestIn"]).optional(),
            "createTable": t.proxy(renames["CreateTableRequestIn"]).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestIn"]).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestIn"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestIn"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestIn"]).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestIn"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestIn"]).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestIn"]
            ).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestIn"]
            ).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestIn"]
            ).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestIn"]
            ).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestIn"]).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestOut"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestOut"]).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestOut"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestOut"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestOut"]).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestOut"]
            ).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestOut"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestOut"]).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestOut"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestOut"]).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestOut"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestOut"]
            ).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestOut"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestOut"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestOut"]).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestOut"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestOut"]
            ).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestOut"]
            ).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestOut"]).optional(),
            "createTable": t.proxy(renames["CreateTableRequestOut"]).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestOut"]).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestOut"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestOut"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestOut"]).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestOut"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestOut"]).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestOut"]
            ).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestOut"]
            ).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestOut"]
            ).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestOut"]
            ).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestOut"]).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["CreateShapeRequestIn"] = t.struct(
        {
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "shapeType": t.string().optional(),
        }
    ).named(renames["CreateShapeRequestIn"])
    types["CreateShapeRequestOut"] = t.struct(
        {
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "shapeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeRequestOut"])
    types["PresentationIn"] = t.struct(
        {
            "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
            "revisionId": t.string().optional(),
            "notesMaster": t.proxy(renames["PageIn"]).optional(),
            "slides": t.array(t.proxy(renames["PageIn"])).optional(),
            "presentationId": t.string().optional(),
            "title": t.string().optional(),
            "masters": t.array(t.proxy(renames["PageIn"])).optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "locale": t.string().optional(),
        }
    ).named(renames["PresentationIn"])
    types["PresentationOut"] = t.struct(
        {
            "layouts": t.array(t.proxy(renames["PageOut"])).optional(),
            "revisionId": t.string().optional(),
            "notesMaster": t.proxy(renames["PageOut"]).optional(),
            "slides": t.array(t.proxy(renames["PageOut"])).optional(),
            "presentationId": t.string().optional(),
            "title": t.string().optional(),
            "masters": t.array(t.proxy(renames["PageOut"])).optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "locale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationOut"])
    types["DuplicateObjectRequestIn"] = t.struct(
        {
            "objectIds": t.struct({"_": t.string().optional()}).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["DuplicateObjectRequestIn"])
    types["DuplicateObjectRequestOut"] = t.struct(
        {
            "objectIds": t.struct({"_": t.string().optional()}).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateObjectRequestOut"])
    types["ColorSchemeIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ThemeColorPairIn"])).optional()}
    ).named(renames["ColorSchemeIn"])
    types["ColorSchemeOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ThemeColorPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorSchemeOut"])
    types["PageIn"] = t.struct(
        {
            "pageElements": t.array(t.proxy(renames["PageElementIn"])).optional(),
            "objectId": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "revisionId": t.string().optional(),
            "pageType": t.string().optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesIn"]).optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesIn"]).optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesIn"]).optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "pageElements": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "objectId": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "revisionId": t.string().optional(),
            "pageType": t.string().optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesOut"]).optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesOut"]).optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["UnmergeTableCellsRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
        }
    ).named(renames["UnmergeTableCellsRequestIn"])
    types["UnmergeTableCellsRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeTableCellsRequestOut"])
    types["TableRowPropertiesIn"] = t.struct(
        {"minRowHeight": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableRowPropertiesIn"])
    types["TableRowPropertiesOut"] = t.struct(
        {
            "minRowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowPropertiesOut"])
    types["DeleteTextRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["DeleteTextRequestIn"])
    types["DeleteTextRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTextRequestOut"])
    types["ReplaceAllTextRequestIn"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "replaceText": t.string().optional(),
        }
    ).named(renames["ReplaceAllTextRequestIn"])
    types["ReplaceAllTextRequestOut"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "replaceText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextRequestOut"])
    types["OptionalColorIn"] = t.struct(
        {"opaqueColor": t.proxy(renames["OpaqueColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "opaqueColor": t.proxy(renames["OpaqueColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
    types["UpdatePageElementTransformRequestIn"] = t.struct(
        {
            "applyMode": t.string().optional(),
            "objectId": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
        }
    ).named(renames["UpdatePageElementTransformRequestIn"])
    types["UpdatePageElementTransformRequestOut"] = t.struct(
        {
            "applyMode": t.string().optional(),
            "objectId": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementTransformRequestOut"])
    types["PlaceholderIn"] = t.struct(
        {
            "type": t.string().optional(),
            "index": t.integer().optional(),
            "parentObjectId": t.string().optional(),
        }
    ).named(renames["PlaceholderIn"])
    types["PlaceholderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "index": t.integer().optional(),
            "parentObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceholderOut"])
    types["LineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["LineFillIn"])
    types["LineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineFillOut"])
    types["OutlineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["OutlineFillIn"])
    types["OutlineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineFillOut"])
    types["SubstringMatchCriteriaIn"] = t.struct(
        {"text": t.string().optional(), "matchCase": t.boolean().optional()}
    ).named(renames["SubstringMatchCriteriaIn"])
    types["SubstringMatchCriteriaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "matchCase": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubstringMatchCriteriaOut"])
    types["ImageIn"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "sourceUrl": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "sourceUrl": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["ReplaceAllShapesWithSheetsChartResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseIn"])
    types["ReplaceAllShapesWithSheetsChartResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseOut"])
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
    types["CreateVideoRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "source": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CreateVideoRequestIn"])
    types["CreateVideoRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "source": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoRequestOut"])
    types["InsertTextRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "text": t.string().optional(),
            "objectId": t.string().optional(),
            "insertionIndex": t.integer().optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "text": t.string().optional(),
            "objectId": t.string().optional(),
            "insertionIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
    types["ImagePropertiesIn"] = t.struct(
        {
            "brightness": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "recolor": t.proxy(renames["RecolorIn"]).optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
            "contrast": t.number().optional(),
            "transparency": t.number().optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "brightness": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "recolor": t.proxy(renames["RecolorOut"]).optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "contrast": t.number().optional(),
            "transparency": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["TableBorderFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["TableBorderFillIn"])
    types["TableBorderFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderFillOut"])
    types["SheetsChartIn"] = t.struct(
        {
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesIn"]
            ).optional(),
            "contentUrl": t.string().optional(),
            "chartId": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["SheetsChartIn"])
    types["SheetsChartOut"] = t.struct(
        {
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesOut"]
            ).optional(),
            "contentUrl": t.string().optional(),
            "chartId": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartOut"])
    types["ThumbnailIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
    types["ListIn"] = t.struct(
        {
            "nestingLevel": t.struct({"_": t.string().optional()}).optional(),
            "listId": t.string().optional(),
        }
    ).named(renames["ListIn"])
    types["ListOut"] = t.struct(
        {
            "nestingLevel": t.struct({"_": t.string().optional()}).optional(),
            "listId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOut"])
    types["TextRunIn"] = t.struct(
        {
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["TextRunIn"])
    types["TextRunOut"] = t.struct(
        {
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextRunOut"])
    types["RecolorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "recolorStops": t.array(t.proxy(renames["ColorStopIn"])).optional(),
        }
    ).named(renames["RecolorIn"])
    types["RecolorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "recolorStops": t.array(t.proxy(renames["ColorStopOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecolorOut"])
    types["LinkIn"] = t.struct(
        {
            "url": t.string().optional(),
            "pageObjectId": t.string().optional(),
            "relativeLink": t.string().optional(),
            "slideIndex": t.integer().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "pageObjectId": t.string().optional(),
            "relativeLink": t.string().optional(),
            "slideIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["LayoutPlaceholderIdMappingIn"] = t.struct(
        {
            "layoutPlaceholderObjectId": t.string().optional(),
            "objectId": t.string().optional(),
            "layoutPlaceholder": t.proxy(renames["PlaceholderIn"]).optional(),
        }
    ).named(renames["LayoutPlaceholderIdMappingIn"])
    types["LayoutPlaceholderIdMappingOut"] = t.struct(
        {
            "layoutPlaceholderObjectId": t.string().optional(),
            "objectId": t.string().optional(),
            "layoutPlaceholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutPlaceholderIdMappingOut"])
    types["VideoIn"] = t.struct(
        {
            "videoProperties": t.proxy(renames["VideoPropertiesIn"]).optional(),
            "url": t.string().optional(),
            "source": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["VideoIn"])
    types["VideoOut"] = t.struct(
        {
            "videoProperties": t.proxy(renames["VideoPropertiesOut"]).optional(),
            "url": t.string().optional(),
            "source": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOut"])
    types["UpdatePageElementsZOrderRequestIn"] = t.struct(
        {
            "pageElementObjectIds": t.array(t.string()).optional(),
            "operation": t.string().optional(),
        }
    ).named(renames["UpdatePageElementsZOrderRequestIn"])
    types["UpdatePageElementsZOrderRequestOut"] = t.struct(
        {
            "pageElementObjectIds": t.array(t.string()).optional(),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementsZOrderRequestOut"])
    types["ShadowIn"] = t.struct(
        {
            "blurRadius": t.proxy(renames["DimensionIn"]).optional(),
            "alpha": t.number().optional(),
            "rotateWithShape": t.boolean().optional(),
            "type": t.string().optional(),
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "alignment": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "propertyState": t.string().optional(),
        }
    ).named(renames["ShadowIn"])
    types["ShadowOut"] = t.struct(
        {
            "blurRadius": t.proxy(renames["DimensionOut"]).optional(),
            "alpha": t.number().optional(),
            "rotateWithShape": t.boolean().optional(),
            "type": t.string().optional(),
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "alignment": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "propertyState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadowOut"])
    types["TableBorderPropertiesIn"] = t.struct(
        {
            "tableBorderFill": t.proxy(renames["TableBorderFillIn"]).optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "dashStyle": t.string().optional(),
        }
    ).named(renames["TableBorderPropertiesIn"])
    types["TableBorderPropertiesOut"] = t.struct(
        {
            "tableBorderFill": t.proxy(renames["TableBorderFillOut"]).optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderPropertiesOut"])
    types["UpdateTableCellPropertiesRequestIn"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestIn"])
    types["UpdateTableCellPropertiesRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestOut"])
    types["UpdateVideoPropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesIn"]).optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestIn"])
    types["UpdateVideoPropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestOut"])
    types["AutoTextIn"] = t.struct(
        {
            "content": t.string().optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "content": t.string().optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
    types["RangeIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
    types["RefreshSheetsChartRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["RefreshSheetsChartRequestIn"])
    types["RefreshSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshSheetsChartRequestOut"])
    types["VideoPropertiesIn"] = t.struct(
        {
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "start": t.integer().optional(),
            "autoPlay": t.boolean().optional(),
            "mute": t.boolean().optional(),
            "end": t.integer().optional(),
        }
    ).named(renames["VideoPropertiesIn"])
    types["VideoPropertiesOut"] = t.struct(
        {
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "start": t.integer().optional(),
            "autoPlay": t.boolean().optional(),
            "mute": t.boolean().optional(),
            "end": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPropertiesOut"])
    types["ShapeBackgroundFillIn"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
            "propertyState": t.string().optional(),
        }
    ).named(renames["ShapeBackgroundFillIn"])
    types["ShapeBackgroundFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "propertyState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapeBackgroundFillOut"])
    types["CreateImageRequestIn"] = t.struct(
        {
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "url": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["CreateImageRequestIn"])
    types["CreateImageRequestOut"] = t.struct(
        {
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "url": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageRequestOut"])
    types["CreateSlideResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSlideResponseIn"])
    types["CreateSlideResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideResponseOut"])
    types["OutlineIn"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "propertyState": t.string().optional(),
            "dashStyle": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillIn"]).optional(),
        }
    ).named(renames["OutlineIn"])
    types["OutlineOut"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "propertyState": t.string().optional(),
            "dashStyle": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineOut"])
    types["InsertTableColumnsRequestIn"] = t.struct(
        {
            "number": t.integer().optional(),
            "insertRight": t.boolean().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "tableObjectId": t.string().optional(),
        }
    ).named(renames["InsertTableColumnsRequestIn"])
    types["InsertTableColumnsRequestOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "insertRight": t.boolean().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "tableObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableColumnsRequestOut"])
    types["DimensionIn"] = t.struct(
        {"unit": t.string().optional(), "magnitude": t.number().optional()}
    ).named(renames["DimensionIn"])
    types["DimensionOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "magnitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOut"])
    types["CreateSheetsChartRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "chartId": t.integer().optional(),
            "linkingMode": t.string().optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["CreateSheetsChartRequestIn"])
    types["CreateSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "chartId": t.integer().optional(),
            "linkingMode": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartRequestOut"])
    types["UpdateSlidePropertiesRequestIn"] = t.struct(
        {
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateSlidePropertiesRequestIn"])
    types["UpdateSlidePropertiesRequestOut"] = t.struct(
        {
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlidePropertiesRequestOut"])
    types["UngroupObjectsRequestIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["UngroupObjectsRequestIn"])
    types["UngroupObjectsRequestOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UngroupObjectsRequestOut"])
    types["LineIn"] = t.struct(
        {
            "lineCategory": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesIn"]).optional(),
            "lineType": t.string().optional(),
        }
    ).named(renames["LineIn"])
    types["LineOut"] = t.struct(
        {
            "lineCategory": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesOut"]).optional(),
            "lineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineOut"])
    types["NotesPropertiesIn"] = t.struct(
        {"speakerNotesObjectId": t.string().optional()}
    ).named(renames["NotesPropertiesIn"])
    types["NotesPropertiesOut"] = t.struct(
        {
            "speakerNotesObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotesPropertiesOut"])
    types["DeleteObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeleteObjectRequestIn"])
    types["DeleteObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteObjectRequestOut"])
    types["NestingLevelIn"] = t.struct(
        {"bulletStyle": t.proxy(renames["TextStyleIn"]).optional()}
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
    types["PageBackgroundFillIn"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillIn"]
            ).optional(),
            "propertyState": t.string().optional(),
        }
    ).named(renames["PageBackgroundFillIn"])
    types["PageBackgroundFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillOut"]
            ).optional(),
            "propertyState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBackgroundFillOut"])
    types["ThemeColorPairIn"] = t.struct(
        {
            "type": t.string().optional(),
            "color": t.proxy(renames["RgbColorIn"]).optional(),
        }
    ).named(renames["ThemeColorPairIn"])
    types["ThemeColorPairOut"] = t.struct(
        {
            "type": t.string().optional(),
            "color": t.proxy(renames["RgbColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThemeColorPairOut"])
    types["TableIn"] = t.struct(
        {
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "rows": t.integer().optional(),
            "columns": t.integer().optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesIn"])
            ).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "rows": t.integer().optional(),
            "columns": t.integer().optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["ShapeIn"] = t.struct(
        {
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesIn"]).optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "shapeType": t.string().optional(),
        }
    ).named(renames["ShapeIn"])
    types["ShapeOut"] = t.struct(
        {
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesOut"]).optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "shapeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapeOut"])
    types["CreateTableRequestIn"] = t.struct(
        {
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "columns": t.integer().optional(),
            "objectId": t.string().optional(),
            "rows": t.integer().optional(),
        }
    ).named(renames["CreateTableRequestIn"])
    types["CreateTableRequestOut"] = t.struct(
        {
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "columns": t.integer().optional(),
            "objectId": t.string().optional(),
            "rows": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableRequestOut"])
    types["LineConnectionIn"] = t.struct(
        {
            "connectionSiteIndex": t.integer().optional(),
            "connectedObjectId": t.string().optional(),
        }
    ).named(renames["LineConnectionIn"])
    types["LineConnectionOut"] = t.struct(
        {
            "connectionSiteIndex": t.integer().optional(),
            "connectedObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineConnectionOut"])
    types["LayoutReferenceIn"] = t.struct(
        {"layoutId": t.string().optional(), "predefinedLayout": t.string().optional()}
    ).named(renames["LayoutReferenceIn"])
    types["LayoutReferenceOut"] = t.struct(
        {
            "layoutId": t.string().optional(),
            "predefinedLayout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutReferenceOut"])
    types["ShapePropertiesIn"] = t.struct(
        {
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "autofit": t.proxy(renames["AutofitIn"]).optional(),
            "contentAlignment": t.string().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
            "shapeBackgroundFill": t.proxy(renames["ShapeBackgroundFillIn"]).optional(),
        }
    ).named(renames["ShapePropertiesIn"])
    types["ShapePropertiesOut"] = t.struct(
        {
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "autofit": t.proxy(renames["AutofitOut"]).optional(),
            "contentAlignment": t.string().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "shapeBackgroundFill": t.proxy(
                renames["ShapeBackgroundFillOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapePropertiesOut"])
    types["GroupObjectsRequestIn"] = t.struct(
        {
            "childrenObjectIds": t.array(t.string()).optional(),
            "groupObjectId": t.string().optional(),
        }
    ).named(renames["GroupObjectsRequestIn"])
    types["GroupObjectsRequestOut"] = t.struct(
        {
            "childrenObjectIds": t.array(t.string()).optional(),
            "groupObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupObjectsRequestOut"])
    types["ReplaceAllShapesWithImageResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithImageResponseIn"])
    types["ReplaceAllShapesWithImageResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageResponseOut"])
    types["TableCellBackgroundFillIn"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
        }
    ).named(renames["TableCellBackgroundFillIn"])
    types["TableCellBackgroundFillOut"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellBackgroundFillOut"])
    types["TableRangeIn"] = t.struct(
        {
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "columnSpan": t.integer().optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "columnSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
    types["WordArtIn"] = t.struct({"renderedText": t.string().optional()}).named(
        renames["WordArtIn"]
    )
    types["WordArtOut"] = t.struct(
        {
            "renderedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordArtOut"])
    types["GroupIn"] = t.struct(
        {"children": t.array(t.proxy(renames["PageElementIn"])).optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "children": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["TableBorderRowIn"] = t.struct(
        {"tableBorderCells": t.array(t.proxy(renames["TableBorderCellIn"])).optional()}
    ).named(renames["TableBorderRowIn"])
    types["TableBorderRowOut"] = t.struct(
        {
            "tableBorderCells": t.array(
                t.proxy(renames["TableBorderCellOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderRowOut"])
    types["CropPropertiesIn"] = t.struct(
        {
            "angle": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "rightOffset": t.number().optional(),
            "topOffset": t.number().optional(),
            "leftOffset": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "angle": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "rightOffset": t.number().optional(),
            "topOffset": t.number().optional(),
            "leftOffset": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
    types["UpdatePageElementAltTextRequestIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdatePageElementAltTextRequestIn"])
    types["UpdatePageElementAltTextRequestOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementAltTextRequestOut"])
    types["BatchUpdatePresentationResponseIn"] = t.struct(
        {
            "presentationId": t.string().optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdatePresentationResponseIn"])
    types["BatchUpdatePresentationResponseOut"] = t.struct(
        {
            "presentationId": t.string().optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePresentationResponseOut"])
    types["ReplaceAllShapesWithImageRequestIn"] = t.struct(
        {
            "replaceMethod": t.string().optional(),
            "imageUrl": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "imageReplaceMethod": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestIn"])
    types["ReplaceAllShapesWithImageRequestOut"] = t.struct(
        {
            "replaceMethod": t.string().optional(),
            "imageUrl": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "imageReplaceMethod": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestOut"])
    types["UpdateShapePropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesIn"]).optional(),
        }
    ).named(renames["UpdateShapePropertiesRequestIn"])
    types["UpdateShapePropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateShapePropertiesRequestOut"])
    types["TextContentIn"] = t.struct(
        {
            "textElements": t.array(t.proxy(renames["TextElementIn"])).optional(),
            "lists": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TextContentIn"])
    types["TextContentOut"] = t.struct(
        {
            "textElements": t.array(t.proxy(renames["TextElementOut"])).optional(),
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextContentOut"])
    types["CreateImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateImageResponseIn"])
    types["CreateImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageResponseOut"])
    types["CreateSlideRequestIn"] = t.struct(
        {
            "slideLayoutReference": t.proxy(renames["LayoutReferenceIn"]).optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingIn"])
            ).optional(),
            "objectId": t.string().optional(),
            "insertionIndex": t.integer().optional(),
        }
    ).named(renames["CreateSlideRequestIn"])
    types["CreateSlideRequestOut"] = t.struct(
        {
            "slideLayoutReference": t.proxy(renames["LayoutReferenceOut"]).optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingOut"])
            ).optional(),
            "objectId": t.string().optional(),
            "insertionIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideRequestOut"])
    types["UpdateTableBorderPropertiesRequestIn"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "objectId": t.string().optional(),
            "borderPosition": t.string().optional(),
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesIn"]
            ).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestIn"])
    types["UpdateTableBorderPropertiesRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "objectId": t.string().optional(),
            "borderPosition": t.string().optional(),
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesOut"]
            ).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestOut"])
    types["TableCellIn"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "rowSpan": t.integer().optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
    types["PagePropertiesIn"] = t.struct(
        {
            "pageBackgroundFill": t.proxy(renames["PageBackgroundFillIn"]).optional(),
            "colorScheme": t.proxy(renames["ColorSchemeIn"]).optional(),
        }
    ).named(renames["PagePropertiesIn"])
    types["PagePropertiesOut"] = t.struct(
        {
            "pageBackgroundFill": t.proxy(renames["PageBackgroundFillOut"]).optional(),
            "colorScheme": t.proxy(renames["ColorSchemeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagePropertiesOut"])
    types["DeleteTableRowRequestIn"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["DeleteTableRowRequestIn"])
    types["DeleteTableRowRequestOut"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableRowRequestOut"])
    types["UpdateLinePropertiesRequestIn"] = t.struct(
        {
            "lineProperties": t.proxy(renames["LinePropertiesIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateLinePropertiesRequestIn"])
    types["UpdateLinePropertiesRequestOut"] = t.struct(
        {
            "lineProperties": t.proxy(renames["LinePropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateLinePropertiesRequestOut"])
    types["WeightedFontFamilyIn"] = t.struct(
        {"weight": t.integer().optional(), "fontFamily": t.string().optional()}
    ).named(renames["WeightedFontFamilyIn"])
    types["WeightedFontFamilyOut"] = t.struct(
        {
            "weight": t.integer().optional(),
            "fontFamily": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeightedFontFamilyOut"])
    types["UpdatePagePropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestIn"])
    types["UpdatePagePropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestOut"])
    types["TableBorderCellIn"] = t.struct(
        {
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesIn"]
            ).optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["TableBorderCellIn"])
    types["TableBorderCellOut"] = t.struct(
        {
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesOut"]
            ).optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderCellOut"])
    types["BulletIn"] = t.struct(
        {
            "bulletStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "glyph": t.string().optional(),
            "listId": t.string().optional(),
            "nestingLevel": t.integer().optional(),
        }
    ).named(renames["BulletIn"])
    types["BulletOut"] = t.struct(
        {
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "glyph": t.string().optional(),
            "listId": t.string().optional(),
            "nestingLevel": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletOut"])
    types["CreateLineRequestIn"] = t.struct(
        {
            "lineCategory": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "category": t.string().optional(),
        }
    ).named(renames["CreateLineRequestIn"])
    types["CreateLineRequestOut"] = t.struct(
        {
            "lineCategory": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineRequestOut"])
    types["CreateSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSheetsChartResponseIn"])
    types["CreateSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartResponseOut"])
    types["SolidFillIn"] = t.struct(
        {
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["SolidFillIn"])
    types["SolidFillOut"] = t.struct(
        {
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SolidFillOut"])
    types["GroupObjectsResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["GroupObjectsResponseIn"])
    types["GroupObjectsResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupObjectsResponseOut"])

    functions = {}
    functions["presentationsBatchUpdate"] = slides.get(
        "v1/presentations/{presentationId}",
        t.struct(
            {"presentationId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsCreate"] = slides.get(
        "v1/presentations/{presentationId}",
        t.struct(
            {"presentationId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsGet"] = slides.get(
        "v1/presentations/{presentationId}",
        t.struct(
            {"presentationId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsPagesGetThumbnail"] = slides.get(
        "v1/presentations/{presentationId}/pages/{pageObjectId}",
        t.struct(
            {
                "presentationId": t.string().optional(),
                "pageObjectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsPagesGet"] = slides.get(
        "v1/presentations/{presentationId}/pages/{pageObjectId}",
        t.struct(
            {
                "presentationId": t.string().optional(),
                "pageObjectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="slides", renames=renames, types=Box(types), functions=Box(functions)
    )
