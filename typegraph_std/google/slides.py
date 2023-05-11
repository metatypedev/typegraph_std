from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_slides() -> Import:
    slides = HTTPRuntime("https://slides.googleapis.com/")

    renames = {
        "ErrorResponse": "_slides_1_ErrorResponse",
        "TableRangeIn": "_slides_2_TableRangeIn",
        "TableRangeOut": "_slides_3_TableRangeOut",
        "ReplaceAllShapesWithSheetsChartResponseIn": "_slides_4_ReplaceAllShapesWithSheetsChartResponseIn",
        "ReplaceAllShapesWithSheetsChartResponseOut": "_slides_5_ReplaceAllShapesWithSheetsChartResponseOut",
        "MergeTableCellsRequestIn": "_slides_6_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_slides_7_MergeTableCellsRequestOut",
        "LineIn": "_slides_8_LineIn",
        "LineOut": "_slides_9_LineOut",
        "ParagraphMarkerIn": "_slides_10_ParagraphMarkerIn",
        "ParagraphMarkerOut": "_slides_11_ParagraphMarkerOut",
        "NestingLevelIn": "_slides_12_NestingLevelIn",
        "NestingLevelOut": "_slides_13_NestingLevelOut",
        "CreateImageResponseIn": "_slides_14_CreateImageResponseIn",
        "CreateImageResponseOut": "_slides_15_CreateImageResponseOut",
        "ThumbnailIn": "_slides_16_ThumbnailIn",
        "ThumbnailOut": "_slides_17_ThumbnailOut",
        "RgbColorIn": "_slides_18_RgbColorIn",
        "RgbColorOut": "_slides_19_RgbColorOut",
        "PageBackgroundFillIn": "_slides_20_PageBackgroundFillIn",
        "PageBackgroundFillOut": "_slides_21_PageBackgroundFillOut",
        "OpaqueColorIn": "_slides_22_OpaqueColorIn",
        "OpaqueColorOut": "_slides_23_OpaqueColorOut",
        "LayoutPlaceholderIdMappingIn": "_slides_24_LayoutPlaceholderIdMappingIn",
        "LayoutPlaceholderIdMappingOut": "_slides_25_LayoutPlaceholderIdMappingOut",
        "UpdateImagePropertiesRequestIn": "_slides_26_UpdateImagePropertiesRequestIn",
        "UpdateImagePropertiesRequestOut": "_slides_27_UpdateImagePropertiesRequestOut",
        "LayoutPropertiesIn": "_slides_28_LayoutPropertiesIn",
        "LayoutPropertiesOut": "_slides_29_LayoutPropertiesOut",
        "TableBorderCellIn": "_slides_30_TableBorderCellIn",
        "TableBorderCellOut": "_slides_31_TableBorderCellOut",
        "DeleteObjectRequestIn": "_slides_32_DeleteObjectRequestIn",
        "DeleteObjectRequestOut": "_slides_33_DeleteObjectRequestOut",
        "VideoIn": "_slides_34_VideoIn",
        "VideoOut": "_slides_35_VideoOut",
        "ResponseIn": "_slides_36_ResponseIn",
        "ResponseOut": "_slides_37_ResponseOut",
        "UpdatePageElementsZOrderRequestIn": "_slides_38_UpdatePageElementsZOrderRequestIn",
        "UpdatePageElementsZOrderRequestOut": "_slides_39_UpdatePageElementsZOrderRequestOut",
        "DimensionIn": "_slides_40_DimensionIn",
        "DimensionOut": "_slides_41_DimensionOut",
        "TableCellPropertiesIn": "_slides_42_TableCellPropertiesIn",
        "TableCellPropertiesOut": "_slides_43_TableCellPropertiesOut",
        "TableIn": "_slides_44_TableIn",
        "TableOut": "_slides_45_TableOut",
        "SizeIn": "_slides_46_SizeIn",
        "SizeOut": "_slides_47_SizeOut",
        "ColorSchemeIn": "_slides_48_ColorSchemeIn",
        "ColorSchemeOut": "_slides_49_ColorSchemeOut",
        "ColorStopIn": "_slides_50_ColorStopIn",
        "ColorStopOut": "_slides_51_ColorStopOut",
        "ReplaceAllTextResponseIn": "_slides_52_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_slides_53_ReplaceAllTextResponseOut",
        "UnmergeTableCellsRequestIn": "_slides_54_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_slides_55_UnmergeTableCellsRequestOut",
        "DeleteTextRequestIn": "_slides_56_DeleteTextRequestIn",
        "DeleteTextRequestOut": "_slides_57_DeleteTextRequestOut",
        "TableCellBackgroundFillIn": "_slides_58_TableCellBackgroundFillIn",
        "TableCellBackgroundFillOut": "_slides_59_TableCellBackgroundFillOut",
        "RecolorIn": "_slides_60_RecolorIn",
        "RecolorOut": "_slides_61_RecolorOut",
        "GroupIn": "_slides_62_GroupIn",
        "GroupOut": "_slides_63_GroupOut",
        "LinePropertiesIn": "_slides_64_LinePropertiesIn",
        "LinePropertiesOut": "_slides_65_LinePropertiesOut",
        "UpdateShapePropertiesRequestIn": "_slides_66_UpdateShapePropertiesRequestIn",
        "UpdateShapePropertiesRequestOut": "_slides_67_UpdateShapePropertiesRequestOut",
        "TableBorderPropertiesIn": "_slides_68_TableBorderPropertiesIn",
        "TableBorderPropertiesOut": "_slides_69_TableBorderPropertiesOut",
        "DuplicateObjectRequestIn": "_slides_70_DuplicateObjectRequestIn",
        "DuplicateObjectRequestOut": "_slides_71_DuplicateObjectRequestOut",
        "TableCellIn": "_slides_72_TableCellIn",
        "TableCellOut": "_slides_73_TableCellOut",
        "OptionalColorIn": "_slides_74_OptionalColorIn",
        "OptionalColorOut": "_slides_75_OptionalColorOut",
        "PageElementPropertiesIn": "_slides_76_PageElementPropertiesIn",
        "PageElementPropertiesOut": "_slides_77_PageElementPropertiesOut",
        "BatchUpdatePresentationRequestIn": "_slides_78_BatchUpdatePresentationRequestIn",
        "BatchUpdatePresentationRequestOut": "_slides_79_BatchUpdatePresentationRequestOut",
        "NotesPropertiesIn": "_slides_80_NotesPropertiesIn",
        "NotesPropertiesOut": "_slides_81_NotesPropertiesOut",
        "UpdateTableBorderPropertiesRequestIn": "_slides_82_UpdateTableBorderPropertiesRequestIn",
        "UpdateTableBorderPropertiesRequestOut": "_slides_83_UpdateTableBorderPropertiesRequestOut",
        "SlidePropertiesIn": "_slides_84_SlidePropertiesIn",
        "SlidePropertiesOut": "_slides_85_SlidePropertiesOut",
        "TextStyleIn": "_slides_86_TextStyleIn",
        "TextStyleOut": "_slides_87_TextStyleOut",
        "ThemeColorPairIn": "_slides_88_ThemeColorPairIn",
        "ThemeColorPairOut": "_slides_89_ThemeColorPairOut",
        "UpdateSlidePropertiesRequestIn": "_slides_90_UpdateSlidePropertiesRequestIn",
        "UpdateSlidePropertiesRequestOut": "_slides_91_UpdateSlidePropertiesRequestOut",
        "CreateShapeResponseIn": "_slides_92_CreateShapeResponseIn",
        "CreateShapeResponseOut": "_slides_93_CreateShapeResponseOut",
        "SubstringMatchCriteriaIn": "_slides_94_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_slides_95_SubstringMatchCriteriaOut",
        "LayoutReferenceIn": "_slides_96_LayoutReferenceIn",
        "LayoutReferenceOut": "_slides_97_LayoutReferenceOut",
        "VideoPropertiesIn": "_slides_98_VideoPropertiesIn",
        "VideoPropertiesOut": "_slides_99_VideoPropertiesOut",
        "TextRunIn": "_slides_100_TextRunIn",
        "TextRunOut": "_slides_101_TextRunOut",
        "UpdateTableCellPropertiesRequestIn": "_slides_102_UpdateTableCellPropertiesRequestIn",
        "UpdateTableCellPropertiesRequestOut": "_slides_103_UpdateTableCellPropertiesRequestOut",
        "UpdateTableColumnPropertiesRequestIn": "_slides_104_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_slides_105_UpdateTableColumnPropertiesRequestOut",
        "LineConnectionIn": "_slides_106_LineConnectionIn",
        "LineConnectionOut": "_slides_107_LineConnectionOut",
        "UpdateLineCategoryRequestIn": "_slides_108_UpdateLineCategoryRequestIn",
        "UpdateLineCategoryRequestOut": "_slides_109_UpdateLineCategoryRequestOut",
        "TextContentIn": "_slides_110_TextContentIn",
        "TextContentOut": "_slides_111_TextContentOut",
        "CreateLineRequestIn": "_slides_112_CreateLineRequestIn",
        "CreateLineRequestOut": "_slides_113_CreateLineRequestOut",
        "TableRowPropertiesIn": "_slides_114_TableRowPropertiesIn",
        "TableRowPropertiesOut": "_slides_115_TableRowPropertiesOut",
        "CreateVideoRequestIn": "_slides_116_CreateVideoRequestIn",
        "CreateVideoRequestOut": "_slides_117_CreateVideoRequestOut",
        "ListIn": "_slides_118_ListIn",
        "ListOut": "_slides_119_ListOut",
        "MasterPropertiesIn": "_slides_120_MasterPropertiesIn",
        "MasterPropertiesOut": "_slides_121_MasterPropertiesOut",
        "CreateTableRequestIn": "_slides_122_CreateTableRequestIn",
        "CreateTableRequestOut": "_slides_123_CreateTableRequestOut",
        "RefreshSheetsChartRequestIn": "_slides_124_RefreshSheetsChartRequestIn",
        "RefreshSheetsChartRequestOut": "_slides_125_RefreshSheetsChartRequestOut",
        "UpdatePageElementAltTextRequestIn": "_slides_126_UpdatePageElementAltTextRequestIn",
        "UpdatePageElementAltTextRequestOut": "_slides_127_UpdatePageElementAltTextRequestOut",
        "ShapePropertiesIn": "_slides_128_ShapePropertiesIn",
        "ShapePropertiesOut": "_slides_129_ShapePropertiesOut",
        "CreateVideoResponseIn": "_slides_130_CreateVideoResponseIn",
        "CreateVideoResponseOut": "_slides_131_CreateVideoResponseOut",
        "PageIn": "_slides_132_PageIn",
        "PageOut": "_slides_133_PageOut",
        "TextElementIn": "_slides_134_TextElementIn",
        "TextElementOut": "_slides_135_TextElementOut",
        "GroupObjectsResponseIn": "_slides_136_GroupObjectsResponseIn",
        "GroupObjectsResponseOut": "_slides_137_GroupObjectsResponseOut",
        "OutlineFillIn": "_slides_138_OutlineFillIn",
        "OutlineFillOut": "_slides_139_OutlineFillOut",
        "ReplaceAllShapesWithSheetsChartRequestIn": "_slides_140_ReplaceAllShapesWithSheetsChartRequestIn",
        "ReplaceAllShapesWithSheetsChartRequestOut": "_slides_141_ReplaceAllShapesWithSheetsChartRequestOut",
        "TableColumnPropertiesIn": "_slides_142_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_slides_143_TableColumnPropertiesOut",
        "BatchUpdatePresentationResponseIn": "_slides_144_BatchUpdatePresentationResponseIn",
        "BatchUpdatePresentationResponseOut": "_slides_145_BatchUpdatePresentationResponseOut",
        "WordArtIn": "_slides_146_WordArtIn",
        "WordArtOut": "_slides_147_WordArtOut",
        "TableBorderFillIn": "_slides_148_TableBorderFillIn",
        "TableBorderFillOut": "_slides_149_TableBorderFillOut",
        "CreateSlideRequestIn": "_slides_150_CreateSlideRequestIn",
        "CreateSlideRequestOut": "_slides_151_CreateSlideRequestOut",
        "ReplaceAllShapesWithImageRequestIn": "_slides_152_ReplaceAllShapesWithImageRequestIn",
        "ReplaceAllShapesWithImageRequestOut": "_slides_153_ReplaceAllShapesWithImageRequestOut",
        "ImageIn": "_slides_154_ImageIn",
        "ImageOut": "_slides_155_ImageOut",
        "ShapeBackgroundFillIn": "_slides_156_ShapeBackgroundFillIn",
        "ShapeBackgroundFillOut": "_slides_157_ShapeBackgroundFillOut",
        "CreateLineResponseIn": "_slides_158_CreateLineResponseIn",
        "CreateLineResponseOut": "_slides_159_CreateLineResponseOut",
        "CreateShapeRequestIn": "_slides_160_CreateShapeRequestIn",
        "CreateShapeRequestOut": "_slides_161_CreateShapeRequestOut",
        "CreateSheetsChartResponseIn": "_slides_162_CreateSheetsChartResponseIn",
        "CreateSheetsChartResponseOut": "_slides_163_CreateSheetsChartResponseOut",
        "ReplaceAllTextRequestIn": "_slides_164_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_slides_165_ReplaceAllTextRequestOut",
        "ParagraphStyleIn": "_slides_166_ParagraphStyleIn",
        "ParagraphStyleOut": "_slides_167_ParagraphStyleOut",
        "DeleteTableColumnRequestIn": "_slides_168_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_slides_169_DeleteTableColumnRequestOut",
        "CreateTableResponseIn": "_slides_170_CreateTableResponseIn",
        "CreateTableResponseOut": "_slides_171_CreateTableResponseOut",
        "PageElementIn": "_slides_172_PageElementIn",
        "PageElementOut": "_slides_173_PageElementOut",
        "CropPropertiesIn": "_slides_174_CropPropertiesIn",
        "CropPropertiesOut": "_slides_175_CropPropertiesOut",
        "SheetsChartPropertiesIn": "_slides_176_SheetsChartPropertiesIn",
        "SheetsChartPropertiesOut": "_slides_177_SheetsChartPropertiesOut",
        "WriteControlIn": "_slides_178_WriteControlIn",
        "WriteControlOut": "_slides_179_WriteControlOut",
        "ImagePropertiesIn": "_slides_180_ImagePropertiesIn",
        "ImagePropertiesOut": "_slides_181_ImagePropertiesOut",
        "CreateParagraphBulletsRequestIn": "_slides_182_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_slides_183_CreateParagraphBulletsRequestOut",
        "CreateImageRequestIn": "_slides_184_CreateImageRequestIn",
        "CreateImageRequestOut": "_slides_185_CreateImageRequestOut",
        "UpdateSlidesPositionRequestIn": "_slides_186_UpdateSlidesPositionRequestIn",
        "UpdateSlidesPositionRequestOut": "_slides_187_UpdateSlidesPositionRequestOut",
        "WeightedFontFamilyIn": "_slides_188_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_slides_189_WeightedFontFamilyOut",
        "ShadowIn": "_slides_190_ShadowIn",
        "ShadowOut": "_slides_191_ShadowOut",
        "GroupObjectsRequestIn": "_slides_192_GroupObjectsRequestIn",
        "GroupObjectsRequestOut": "_slides_193_GroupObjectsRequestOut",
        "RequestIn": "_slides_194_RequestIn",
        "RequestOut": "_slides_195_RequestOut",
        "DeleteParagraphBulletsRequestIn": "_slides_196_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_slides_197_DeleteParagraphBulletsRequestOut",
        "BulletIn": "_slides_198_BulletIn",
        "BulletOut": "_slides_199_BulletOut",
        "InsertTableColumnsRequestIn": "_slides_200_InsertTableColumnsRequestIn",
        "InsertTableColumnsRequestOut": "_slides_201_InsertTableColumnsRequestOut",
        "RerouteLineRequestIn": "_slides_202_RerouteLineRequestIn",
        "RerouteLineRequestOut": "_slides_203_RerouteLineRequestOut",
        "UpdateTableRowPropertiesRequestIn": "_slides_204_UpdateTableRowPropertiesRequestIn",
        "UpdateTableRowPropertiesRequestOut": "_slides_205_UpdateTableRowPropertiesRequestOut",
        "LinkIn": "_slides_206_LinkIn",
        "LinkOut": "_slides_207_LinkOut",
        "PresentationIn": "_slides_208_PresentationIn",
        "PresentationOut": "_slides_209_PresentationOut",
        "PagePropertiesIn": "_slides_210_PagePropertiesIn",
        "PagePropertiesOut": "_slides_211_PagePropertiesOut",
        "UpdatePagePropertiesRequestIn": "_slides_212_UpdatePagePropertiesRequestIn",
        "UpdatePagePropertiesRequestOut": "_slides_213_UpdatePagePropertiesRequestOut",
        "UpdateVideoPropertiesRequestIn": "_slides_214_UpdateVideoPropertiesRequestIn",
        "UpdateVideoPropertiesRequestOut": "_slides_215_UpdateVideoPropertiesRequestOut",
        "DeleteTableRowRequestIn": "_slides_216_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_slides_217_DeleteTableRowRequestOut",
        "UngroupObjectsRequestIn": "_slides_218_UngroupObjectsRequestIn",
        "UngroupObjectsRequestOut": "_slides_219_UngroupObjectsRequestOut",
        "UpdateTextStyleRequestIn": "_slides_220_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_slides_221_UpdateTextStyleRequestOut",
        "DuplicateObjectResponseIn": "_slides_222_DuplicateObjectResponseIn",
        "DuplicateObjectResponseOut": "_slides_223_DuplicateObjectResponseOut",
        "AutofitIn": "_slides_224_AutofitIn",
        "AutofitOut": "_slides_225_AutofitOut",
        "PlaceholderIn": "_slides_226_PlaceholderIn",
        "PlaceholderOut": "_slides_227_PlaceholderOut",
        "LineFillIn": "_slides_228_LineFillIn",
        "LineFillOut": "_slides_229_LineFillOut",
        "StretchedPictureFillIn": "_slides_230_StretchedPictureFillIn",
        "StretchedPictureFillOut": "_slides_231_StretchedPictureFillOut",
        "ReplaceImageRequestIn": "_slides_232_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_slides_233_ReplaceImageRequestOut",
        "SheetsChartIn": "_slides_234_SheetsChartIn",
        "SheetsChartOut": "_slides_235_SheetsChartOut",
        "ReplaceAllShapesWithImageResponseIn": "_slides_236_ReplaceAllShapesWithImageResponseIn",
        "ReplaceAllShapesWithImageResponseOut": "_slides_237_ReplaceAllShapesWithImageResponseOut",
        "InsertTextRequestIn": "_slides_238_InsertTextRequestIn",
        "InsertTextRequestOut": "_slides_239_InsertTextRequestOut",
        "SolidFillIn": "_slides_240_SolidFillIn",
        "SolidFillOut": "_slides_241_SolidFillOut",
        "TableCellLocationIn": "_slides_242_TableCellLocationIn",
        "TableCellLocationOut": "_slides_243_TableCellLocationOut",
        "CreateSheetsChartRequestIn": "_slides_244_CreateSheetsChartRequestIn",
        "CreateSheetsChartRequestOut": "_slides_245_CreateSheetsChartRequestOut",
        "RangeIn": "_slides_246_RangeIn",
        "RangeOut": "_slides_247_RangeOut",
        "TableBorderRowIn": "_slides_248_TableBorderRowIn",
        "TableBorderRowOut": "_slides_249_TableBorderRowOut",
        "TableRowIn": "_slides_250_TableRowIn",
        "TableRowOut": "_slides_251_TableRowOut",
        "ShapeIn": "_slides_252_ShapeIn",
        "ShapeOut": "_slides_253_ShapeOut",
        "AutoTextIn": "_slides_254_AutoTextIn",
        "AutoTextOut": "_slides_255_AutoTextOut",
        "UpdateLinePropertiesRequestIn": "_slides_256_UpdateLinePropertiesRequestIn",
        "UpdateLinePropertiesRequestOut": "_slides_257_UpdateLinePropertiesRequestOut",
        "CreateSlideResponseIn": "_slides_258_CreateSlideResponseIn",
        "CreateSlideResponseOut": "_slides_259_CreateSlideResponseOut",
        "UpdatePageElementTransformRequestIn": "_slides_260_UpdatePageElementTransformRequestIn",
        "UpdatePageElementTransformRequestOut": "_slides_261_UpdatePageElementTransformRequestOut",
        "AffineTransformIn": "_slides_262_AffineTransformIn",
        "AffineTransformOut": "_slides_263_AffineTransformOut",
        "OutlineIn": "_slides_264_OutlineIn",
        "OutlineOut": "_slides_265_OutlineOut",
        "InsertTableRowsRequestIn": "_slides_266_InsertTableRowsRequestIn",
        "InsertTableRowsRequestOut": "_slides_267_InsertTableRowsRequestOut",
        "UpdateParagraphStyleRequestIn": "_slides_268_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_slides_269_UpdateParagraphStyleRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TableRangeIn"] = t.struct(
        {
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
    types["ReplaceAllShapesWithSheetsChartResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseIn"])
    types["ReplaceAllShapesWithSheetsChartResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseOut"])
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
    types["LineIn"] = t.struct(
        {
            "lineProperties": t.proxy(renames["LinePropertiesIn"]).optional(),
            "lineCategory": t.string().optional(),
            "lineType": t.string().optional(),
        }
    ).named(renames["LineIn"])
    types["LineOut"] = t.struct(
        {
            "lineProperties": t.proxy(renames["LinePropertiesOut"]).optional(),
            "lineCategory": t.string().optional(),
            "lineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineOut"])
    types["ParagraphMarkerIn"] = t.struct(
        {
            "style": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "bullet": t.proxy(renames["BulletIn"]).optional(),
        }
    ).named(renames["ParagraphMarkerIn"])
    types["ParagraphMarkerOut"] = t.struct(
        {
            "style": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "bullet": t.proxy(renames["BulletOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphMarkerOut"])
    types["NestingLevelIn"] = t.struct(
        {"bulletStyle": t.proxy(renames["TextStyleIn"]).optional()}
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
    types["CreateImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateImageResponseIn"])
    types["CreateImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageResponseOut"])
    types["ThumbnailIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
    types["RgbColorIn"] = t.struct(
        {
            "green": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
        }
    ).named(renames["RgbColorIn"])
    types["RgbColorOut"] = t.struct(
        {
            "green": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RgbColorOut"])
    types["PageBackgroundFillIn"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillIn"]
            ).optional(),
        }
    ).named(renames["PageBackgroundFillIn"])
    types["PageBackgroundFillOut"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBackgroundFillOut"])
    types["OpaqueColorIn"] = t.struct(
        {
            "themeColor": t.string().optional(),
            "rgbColor": t.proxy(renames["RgbColorIn"]).optional(),
        }
    ).named(renames["OpaqueColorIn"])
    types["OpaqueColorOut"] = t.struct(
        {
            "themeColor": t.string().optional(),
            "rgbColor": t.proxy(renames["RgbColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpaqueColorOut"])
    types["LayoutPlaceholderIdMappingIn"] = t.struct(
        {
            "layoutPlaceholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "objectId": t.string().optional(),
            "layoutPlaceholderObjectId": t.string().optional(),
        }
    ).named(renames["LayoutPlaceholderIdMappingIn"])
    types["LayoutPlaceholderIdMappingOut"] = t.struct(
        {
            "layoutPlaceholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "objectId": t.string().optional(),
            "layoutPlaceholderObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutPlaceholderIdMappingOut"])
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
    types["LayoutPropertiesIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "masterObjectId": t.string().optional(),
        }
    ).named(renames["LayoutPropertiesIn"])
    types["LayoutPropertiesOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "masterObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutPropertiesOut"])
    types["TableBorderCellIn"] = t.struct(
        {
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesIn"]
            ).optional(),
        }
    ).named(renames["TableBorderCellIn"])
    types["TableBorderCellOut"] = t.struct(
        {
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderCellOut"])
    types["DeleteObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeleteObjectRequestIn"])
    types["DeleteObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteObjectRequestOut"])
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
    types["ResponseIn"] = t.struct(
        {
            "createTable": t.proxy(renames["CreateTableResponseIn"]).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectResponseIn"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseIn"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseIn"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseIn"]).optional(),
            "createLine": t.proxy(renames["CreateLineResponseIn"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseIn"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseIn"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseIn"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseIn"]).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "createTable": t.proxy(renames["CreateTableResponseOut"]).optional(),
            "duplicateObject": t.proxy(
                renames["DuplicateObjectResponseOut"]
            ).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseOut"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseOut"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseOut"]).optional(),
            "createLine": t.proxy(renames["CreateLineResponseOut"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseOut"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseOut"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseOut"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
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
    types["TableIn"] = t.struct(
        {
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
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
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["SizeIn"] = t.struct(
        {
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "height": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["SizeIn"])
    types["SizeOut"] = t.struct(
        {
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "height": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SizeOut"])
    types["ColorSchemeIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ThemeColorPairIn"])).optional()}
    ).named(renames["ColorSchemeIn"])
    types["ColorSchemeOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ThemeColorPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorSchemeOut"])
    types["ColorStopIn"] = t.struct(
        {
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "position": t.number().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ColorStopIn"])
    types["ColorStopOut"] = t.struct(
        {
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "position": t.number().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorStopOut"])
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
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
    types["DeleteTextRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["DeleteTextRequestIn"])
    types["DeleteTextRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTextRequestOut"])
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
    types["GroupIn"] = t.struct(
        {"children": t.array(t.proxy(renames["PageElementIn"])).optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "children": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["LinePropertiesIn"] = t.struct(
        {
            "endArrow": t.string().optional(),
            "startArrow": t.string().optional(),
            "dashStyle": t.string().optional(),
            "startConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "lineFill": t.proxy(renames["LineFillIn"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionIn"]).optional(),
        }
    ).named(renames["LinePropertiesIn"])
    types["LinePropertiesOut"] = t.struct(
        {
            "endArrow": t.string().optional(),
            "startArrow": t.string().optional(),
            "dashStyle": t.string().optional(),
            "startConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "lineFill": t.proxy(renames["LineFillOut"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinePropertiesOut"])
    types["UpdateShapePropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateShapePropertiesRequestIn"])
    types["UpdateShapePropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateShapePropertiesRequestOut"])
    types["TableBorderPropertiesIn"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "tableBorderFill": t.proxy(renames["TableBorderFillIn"]).optional(),
            "dashStyle": t.string().optional(),
        }
    ).named(renames["TableBorderPropertiesIn"])
    types["TableBorderPropertiesOut"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "tableBorderFill": t.proxy(renames["TableBorderFillOut"]).optional(),
            "dashStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderPropertiesOut"])
    types["DuplicateObjectRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "objectIds": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DuplicateObjectRequestIn"])
    types["DuplicateObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "objectIds": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateObjectRequestOut"])
    types["TableCellIn"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "rowSpan": t.integer().optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
    types["OptionalColorIn"] = t.struct(
        {"opaqueColor": t.proxy(renames["OpaqueColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "opaqueColor": t.proxy(renames["OpaqueColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
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
    types["BatchUpdatePresentationRequestIn"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
        }
    ).named(renames["BatchUpdatePresentationRequestIn"])
    types["BatchUpdatePresentationRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RequestOut"])).optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePresentationRequestOut"])
    types["NotesPropertiesIn"] = t.struct(
        {"speakerNotesObjectId": t.string().optional()}
    ).named(renames["NotesPropertiesIn"])
    types["NotesPropertiesOut"] = t.struct(
        {
            "speakerNotesObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotesPropertiesOut"])
    types["UpdateTableBorderPropertiesRequestIn"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "borderPosition": t.string().optional(),
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesIn"]
            ).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestIn"])
    types["UpdateTableBorderPropertiesRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "borderPosition": t.string().optional(),
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestOut"])
    types["SlidePropertiesIn"] = t.struct(
        {
            "notesPage": t.proxy(renames["PageIn"]).optional(),
            "masterObjectId": t.string().optional(),
            "isSkipped": t.boolean().optional(),
            "layoutObjectId": t.string().optional(),
        }
    ).named(renames["SlidePropertiesIn"])
    types["SlidePropertiesOut"] = t.struct(
        {
            "notesPage": t.proxy(renames["PageOut"]).optional(),
            "masterObjectId": t.string().optional(),
            "isSkipped": t.boolean().optional(),
            "layoutObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlidePropertiesOut"])
    types["TextStyleIn"] = t.struct(
        {
            "fontFamily": t.string().optional(),
            "smallCaps": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "strikethrough": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "baselineOffset": t.string().optional(),
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
            "italic": t.boolean().optional(),
            "bold": t.boolean().optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "fontFamily": t.string().optional(),
            "smallCaps": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "strikethrough": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "baselineOffset": t.string().optional(),
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "italic": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
    types["ThemeColorPairIn"] = t.struct(
        {
            "color": t.proxy(renames["RgbColorIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ThemeColorPairIn"])
    types["ThemeColorPairOut"] = t.struct(
        {
            "color": t.proxy(renames["RgbColorOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThemeColorPairOut"])
    types["UpdateSlidePropertiesRequestIn"] = t.struct(
        {
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateSlidePropertiesRequestIn"])
    types["UpdateSlidePropertiesRequestOut"] = t.struct(
        {
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlidePropertiesRequestOut"])
    types["CreateShapeResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateShapeResponseIn"])
    types["CreateShapeResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeResponseOut"])
    types["SubstringMatchCriteriaIn"] = t.struct(
        {"matchCase": t.boolean().optional(), "text": t.string().optional()}
    ).named(renames["SubstringMatchCriteriaIn"])
    types["SubstringMatchCriteriaOut"] = t.struct(
        {
            "matchCase": t.boolean().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubstringMatchCriteriaOut"])
    types["LayoutReferenceIn"] = t.struct(
        {"predefinedLayout": t.string().optional(), "layoutId": t.string().optional()}
    ).named(renames["LayoutReferenceIn"])
    types["LayoutReferenceOut"] = t.struct(
        {
            "predefinedLayout": t.string().optional(),
            "layoutId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutReferenceOut"])
    types["VideoPropertiesIn"] = t.struct(
        {
            "mute": t.boolean().optional(),
            "start": t.integer().optional(),
            "autoPlay": t.boolean().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "end": t.integer().optional(),
        }
    ).named(renames["VideoPropertiesIn"])
    types["VideoPropertiesOut"] = t.struct(
        {
            "mute": t.boolean().optional(),
            "start": t.integer().optional(),
            "autoPlay": t.boolean().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "end": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPropertiesOut"])
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
    types["UpdateTableCellPropertiesRequestIn"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestIn"])
    types["UpdateTableCellPropertiesRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestOut"])
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["LineConnectionIn"] = t.struct(
        {
            "connectedObjectId": t.string().optional(),
            "connectionSiteIndex": t.integer().optional(),
        }
    ).named(renames["LineConnectionIn"])
    types["LineConnectionOut"] = t.struct(
        {
            "connectedObjectId": t.string().optional(),
            "connectionSiteIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineConnectionOut"])
    types["UpdateLineCategoryRequestIn"] = t.struct(
        {"lineCategory": t.string().optional(), "objectId": t.string().optional()}
    ).named(renames["UpdateLineCategoryRequestIn"])
    types["UpdateLineCategoryRequestOut"] = t.struct(
        {
            "lineCategory": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateLineCategoryRequestOut"])
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
    types["CreateLineRequestIn"] = t.struct(
        {
            "category": t.string().optional(),
            "objectId": t.string().optional(),
            "lineCategory": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
        }
    ).named(renames["CreateLineRequestIn"])
    types["CreateLineRequestOut"] = t.struct(
        {
            "category": t.string().optional(),
            "objectId": t.string().optional(),
            "lineCategory": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineRequestOut"])
    types["TableRowPropertiesIn"] = t.struct(
        {"minRowHeight": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableRowPropertiesIn"])
    types["TableRowPropertiesOut"] = t.struct(
        {
            "minRowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowPropertiesOut"])
    types["CreateVideoRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "id": t.string().optional(),
            "source": t.string().optional(),
        }
    ).named(renames["CreateVideoRequestIn"])
    types["CreateVideoRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "id": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoRequestOut"])
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
    types["MasterPropertiesIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["MasterPropertiesIn"])
    types["MasterPropertiesOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterPropertiesOut"])
    types["CreateTableRequestIn"] = t.struct(
        {
            "columns": t.integer().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "rows": t.integer().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["CreateTableRequestIn"])
    types["CreateTableRequestOut"] = t.struct(
        {
            "columns": t.integer().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "rows": t.integer().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableRequestOut"])
    types["RefreshSheetsChartRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["RefreshSheetsChartRequestIn"])
    types["RefreshSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshSheetsChartRequestOut"])
    types["UpdatePageElementAltTextRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["UpdatePageElementAltTextRequestIn"])
    types["UpdatePageElementAltTextRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementAltTextRequestOut"])
    types["ShapePropertiesIn"] = t.struct(
        {
            "link": t.proxy(renames["LinkIn"]).optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "shapeBackgroundFill": t.proxy(renames["ShapeBackgroundFillIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
            "contentAlignment": t.string().optional(),
            "autofit": t.proxy(renames["AutofitIn"]).optional(),
        }
    ).named(renames["ShapePropertiesIn"])
    types["ShapePropertiesOut"] = t.struct(
        {
            "link": t.proxy(renames["LinkOut"]).optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "shapeBackgroundFill": t.proxy(
                renames["ShapeBackgroundFillOut"]
            ).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "contentAlignment": t.string().optional(),
            "autofit": t.proxy(renames["AutofitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapePropertiesOut"])
    types["CreateVideoResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateVideoResponseIn"])
    types["CreateVideoResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoResponseOut"])
    types["PageIn"] = t.struct(
        {
            "pageElements": t.array(t.proxy(renames["PageElementIn"])).optional(),
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesIn"]).optional(),
            "pageType": t.string().optional(),
            "revisionId": t.string().optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesIn"]).optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesIn"]).optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "pageElements": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesOut"]).optional(),
            "pageType": t.string().optional(),
            "revisionId": t.string().optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesOut"]).optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["TextElementIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "paragraphMarker": t.proxy(renames["ParagraphMarkerIn"]).optional(),
        }
    ).named(renames["TextElementIn"])
    types["TextElementOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "paragraphMarker": t.proxy(renames["ParagraphMarkerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextElementOut"])
    types["GroupObjectsResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["GroupObjectsResponseIn"])
    types["GroupObjectsResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupObjectsResponseOut"])
    types["OutlineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["OutlineFillIn"])
    types["OutlineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineFillOut"])
    types["ReplaceAllShapesWithSheetsChartRequestIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "linkingMode": t.string().optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestIn"])
    types["ReplaceAllShapesWithSheetsChartRequestOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "linkingMode": t.string().optional(),
            "chartId": t.integer().optional(),
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
    types["BatchUpdatePresentationResponseIn"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
            "presentationId": t.string().optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
        }
    ).named(renames["BatchUpdatePresentationResponseIn"])
    types["BatchUpdatePresentationResponseOut"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "presentationId": t.string().optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePresentationResponseOut"])
    types["WordArtIn"] = t.struct({"renderedText": t.string().optional()}).named(
        renames["WordArtIn"]
    )
    types["WordArtOut"] = t.struct(
        {
            "renderedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordArtOut"])
    types["TableBorderFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["TableBorderFillIn"])
    types["TableBorderFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderFillOut"])
    types["CreateSlideRequestIn"] = t.struct(
        {
            "slideLayoutReference": t.proxy(renames["LayoutReferenceIn"]).optional(),
            "objectId": t.string().optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingIn"])
            ).optional(),
            "insertionIndex": t.integer().optional(),
        }
    ).named(renames["CreateSlideRequestIn"])
    types["CreateSlideRequestOut"] = t.struct(
        {
            "slideLayoutReference": t.proxy(renames["LayoutReferenceOut"]).optional(),
            "objectId": t.string().optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingOut"])
            ).optional(),
            "insertionIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideRequestOut"])
    types["ReplaceAllShapesWithImageRequestIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "replaceMethod": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestIn"])
    types["ReplaceAllShapesWithImageRequestOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "replaceMethod": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestOut"])
    types["ImageIn"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "sourceUrl": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "sourceUrl": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
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
    types["CreateLineResponseIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["CreateLineResponseIn"]
    )
    types["CreateLineResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineResponseOut"])
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
    types["CreateSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSheetsChartResponseIn"])
    types["CreateSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartResponseOut"])
    types["ReplaceAllTextRequestIn"] = t.struct(
        {
            "replaceText": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
        }
    ).named(renames["ReplaceAllTextRequestIn"])
    types["ReplaceAllTextRequestOut"] = t.struct(
        {
            "replaceText": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextRequestOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "alignment": t.string().optional(),
            "direction": t.string().optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "lineSpacing": t.number().optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
            "spacingMode": t.string().optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "alignment": t.string().optional(),
            "direction": t.string().optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "lineSpacing": t.number().optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "spacingMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
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
    types["CreateTableResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateTableResponseIn"])
    types["CreateTableResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableResponseOut"])
    types["PageElementIn"] = t.struct(
        {
            "wordArt": t.proxy(renames["WordArtIn"]).optional(),
            "description": t.string().optional(),
            "line": t.proxy(renames["LineIn"]).optional(),
            "sheetsChart": t.proxy(renames["SheetsChartIn"]).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "shape": t.proxy(renames["ShapeIn"]).optional(),
            "video": t.proxy(renames["VideoIn"]).optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "title": t.string().optional(),
            "objectId": t.string().optional(),
            "elementGroup": t.proxy(renames["GroupIn"]).optional(),
        }
    ).named(renames["PageElementIn"])
    types["PageElementOut"] = t.struct(
        {
            "wordArt": t.proxy(renames["WordArtOut"]).optional(),
            "description": t.string().optional(),
            "line": t.proxy(renames["LineOut"]).optional(),
            "sheetsChart": t.proxy(renames["SheetsChartOut"]).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "shape": t.proxy(renames["ShapeOut"]).optional(),
            "video": t.proxy(renames["VideoOut"]).optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "title": t.string().optional(),
            "objectId": t.string().optional(),
            "elementGroup": t.proxy(renames["GroupOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementOut"])
    types["CropPropertiesIn"] = t.struct(
        {
            "bottomOffset": t.number().optional(),
            "angle": t.number().optional(),
            "leftOffset": t.number().optional(),
            "rightOffset": t.number().optional(),
            "topOffset": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "bottomOffset": t.number().optional(),
            "angle": t.number().optional(),
            "leftOffset": t.number().optional(),
            "rightOffset": t.number().optional(),
            "topOffset": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
    types["SheetsChartPropertiesIn"] = t.struct(
        {"chartImageProperties": t.proxy(renames["ImagePropertiesIn"]).optional()}
    ).named(renames["SheetsChartPropertiesIn"])
    types["SheetsChartPropertiesOut"] = t.struct(
        {
            "chartImageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartPropertiesOut"])
    types["WriteControlIn"] = t.struct(
        {"requiredRevisionId": t.string().optional()}
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
    types["ImagePropertiesIn"] = t.struct(
        {
            "recolor": t.proxy(renames["RecolorIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "brightness": t.number().optional(),
            "contrast": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "transparency": t.number().optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "recolor": t.proxy(renames["RecolorOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "brightness": t.number().optional(),
            "contrast": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "transparency": t.number().optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["CreateParagraphBulletsRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "bulletPreset": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestIn"])
    types["CreateParagraphBulletsRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "bulletPreset": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestOut"])
    types["CreateImageRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["CreateImageRequestIn"])
    types["CreateImageRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageRequestOut"])
    types["UpdateSlidesPositionRequestIn"] = t.struct(
        {
            "insertionIndex": t.integer().optional(),
            "slideObjectIds": t.array(t.string()).optional(),
        }
    ).named(renames["UpdateSlidesPositionRequestIn"])
    types["UpdateSlidesPositionRequestOut"] = t.struct(
        {
            "insertionIndex": t.integer().optional(),
            "slideObjectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlidesPositionRequestOut"])
    types["WeightedFontFamilyIn"] = t.struct(
        {"fontFamily": t.string().optional(), "weight": t.integer().optional()}
    ).named(renames["WeightedFontFamilyIn"])
    types["WeightedFontFamilyOut"] = t.struct(
        {
            "fontFamily": t.string().optional(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeightedFontFamilyOut"])
    types["ShadowIn"] = t.struct(
        {
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "alpha": t.number().optional(),
            "propertyState": t.string().optional(),
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "rotateWithShape": t.boolean().optional(),
            "blurRadius": t.proxy(renames["DimensionIn"]).optional(),
            "alignment": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ShadowIn"])
    types["ShadowOut"] = t.struct(
        {
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "alpha": t.number().optional(),
            "propertyState": t.string().optional(),
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "rotateWithShape": t.boolean().optional(),
            "blurRadius": t.proxy(renames["DimensionOut"]).optional(),
            "alignment": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadowOut"])
    types["GroupObjectsRequestIn"] = t.struct(
        {
            "groupObjectId": t.string().optional(),
            "childrenObjectIds": t.array(t.string()).optional(),
        }
    ).named(renames["GroupObjectsRequestIn"])
    types["GroupObjectsRequestOut"] = t.struct(
        {
            "groupObjectId": t.string().optional(),
            "childrenObjectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupObjectsRequestOut"])
    types["RequestIn"] = t.struct(
        {
            "createShape": t.proxy(renames["CreateShapeRequestIn"]).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestIn"]
            ).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestIn"]
            ).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestIn"]).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestIn"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestIn"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestIn"]).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestIn"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestIn"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestIn"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestIn"]).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestIn"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestIn"]).optional(),
            "createTable": t.proxy(renames["CreateTableRequestIn"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestIn"]
            ).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestIn"]).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestIn"]).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestIn"]
            ).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestIn"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestIn"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestIn"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestIn"]
            ).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestIn"]).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestIn"]
            ).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestIn"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestIn"]
            ).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "createImage": t.proxy(renames["CreateImageRequestIn"]).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestIn"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestIn"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestIn"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "createShape": t.proxy(renames["CreateShapeRequestOut"]).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestOut"]
            ).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestOut"]
            ).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestOut"]).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestOut"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestOut"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestOut"]).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestOut"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestOut"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestOut"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestOut"]).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestOut"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestOut"]).optional(),
            "createTable": t.proxy(renames["CreateTableRequestOut"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestOut"]
            ).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestOut"]).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestOut"]).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestOut"]
            ).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestOut"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestOut"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestOut"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestOut"]
            ).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestOut"]).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestOut"]
            ).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestOut"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestOut"]
            ).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "createImage": t.proxy(renames["CreateImageRequestOut"]).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestOut"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestOut"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestOut"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["DeleteParagraphBulletsRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestIn"])
    types["DeleteParagraphBulletsRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestOut"])
    types["BulletIn"] = t.struct(
        {
            "glyph": t.string().optional(),
            "bulletStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "listId": t.string().optional(),
            "nestingLevel": t.integer().optional(),
        }
    ).named(renames["BulletIn"])
    types["BulletOut"] = t.struct(
        {
            "glyph": t.string().optional(),
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "listId": t.string().optional(),
            "nestingLevel": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletOut"])
    types["InsertTableColumnsRequestIn"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "insertRight": t.boolean().optional(),
            "number": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["InsertTableColumnsRequestIn"])
    types["InsertTableColumnsRequestOut"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "insertRight": t.boolean().optional(),
            "number": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableColumnsRequestOut"])
    types["RerouteLineRequestIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["RerouteLineRequestIn"]
    )
    types["RerouteLineRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RerouteLineRequestOut"])
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
    types["LinkIn"] = t.struct(
        {
            "slideIndex": t.integer().optional(),
            "pageObjectId": t.string().optional(),
            "relativeLink": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "slideIndex": t.integer().optional(),
            "pageObjectId": t.string().optional(),
            "relativeLink": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["PresentationIn"] = t.struct(
        {
            "locale": t.string().optional(),
            "notesMaster": t.proxy(renames["PageIn"]).optional(),
            "slides": t.array(t.proxy(renames["PageIn"])).optional(),
            "title": t.string().optional(),
            "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
            "revisionId": t.string().optional(),
            "presentationId": t.string().optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "masters": t.array(t.proxy(renames["PageIn"])).optional(),
        }
    ).named(renames["PresentationIn"])
    types["PresentationOut"] = t.struct(
        {
            "locale": t.string().optional(),
            "notesMaster": t.proxy(renames["PageOut"]).optional(),
            "slides": t.array(t.proxy(renames["PageOut"])).optional(),
            "title": t.string().optional(),
            "layouts": t.array(t.proxy(renames["PageOut"])).optional(),
            "revisionId": t.string().optional(),
            "presentationId": t.string().optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "masters": t.array(t.proxy(renames["PageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationOut"])
    types["PagePropertiesIn"] = t.struct(
        {
            "colorScheme": t.proxy(renames["ColorSchemeIn"]).optional(),
            "pageBackgroundFill": t.proxy(renames["PageBackgroundFillIn"]).optional(),
        }
    ).named(renames["PagePropertiesIn"])
    types["PagePropertiesOut"] = t.struct(
        {
            "colorScheme": t.proxy(renames["ColorSchemeOut"]).optional(),
            "pageBackgroundFill": t.proxy(renames["PageBackgroundFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagePropertiesOut"])
    types["UpdatePagePropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestIn"])
    types["UpdatePagePropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestOut"])
    types["UpdateVideoPropertiesRequestIn"] = t.struct(
        {
            "videoProperties": t.proxy(renames["VideoPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestIn"])
    types["UpdateVideoPropertiesRequestOut"] = t.struct(
        {
            "videoProperties": t.proxy(renames["VideoPropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestOut"])
    types["DeleteTableRowRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "tableObjectId": t.string().optional(),
        }
    ).named(renames["DeleteTableRowRequestIn"])
    types["DeleteTableRowRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "tableObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableRowRequestOut"])
    types["UngroupObjectsRequestIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["UngroupObjectsRequestIn"])
    types["UngroupObjectsRequestOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UngroupObjectsRequestOut"])
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "objectId": t.string().optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "fields": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "objectId": t.string().optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "fields": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
    types["DuplicateObjectResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DuplicateObjectResponseIn"])
    types["DuplicateObjectResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateObjectResponseOut"])
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
    types["PlaceholderIn"] = t.struct(
        {
            "parentObjectId": t.string().optional(),
            "index": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PlaceholderIn"])
    types["PlaceholderOut"] = t.struct(
        {
            "parentObjectId": t.string().optional(),
            "index": t.integer().optional(),
            "type": t.string().optional(),
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
    types["ReplaceImageRequestIn"] = t.struct(
        {
            "url": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "imageObjectId": t.string().optional(),
        }
    ).named(renames["ReplaceImageRequestIn"])
    types["ReplaceImageRequestOut"] = t.struct(
        {
            "url": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "imageObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceImageRequestOut"])
    types["SheetsChartIn"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesIn"]
            ).optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["SheetsChartIn"])
    types["SheetsChartOut"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesOut"]
            ).optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartOut"])
    types["ReplaceAllShapesWithImageResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithImageResponseIn"])
    types["ReplaceAllShapesWithImageResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageResponseOut"])
    types["InsertTextRequestIn"] = t.struct(
        {
            "text": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "insertionIndex": t.integer().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "text": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "insertionIndex": t.integer().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
    types["SolidFillIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
        }
    ).named(renames["SolidFillIn"])
    types["SolidFillOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SolidFillOut"])
    types["TableCellLocationIn"] = t.struct(
        {"columnIndex": t.integer().optional(), "rowIndex": t.integer().optional()}
    ).named(renames["TableCellLocationIn"])
    types["TableCellLocationOut"] = t.struct(
        {
            "columnIndex": t.integer().optional(),
            "rowIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellLocationOut"])
    types["CreateSheetsChartRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "chartId": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["CreateSheetsChartRequestIn"])
    types["CreateSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "chartId": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartRequestOut"])
    types["RangeIn"] = t.struct(
        {
            "type": t.string().optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
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
    types["TableRowIn"] = t.struct(
        {
            "tableCells": t.array(t.proxy(renames["TableCellIn"])).optional(),
            "rowHeight": t.proxy(renames["DimensionIn"]).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
        }
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "tableCells": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "rowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["ShapeIn"] = t.struct(
        {
            "shapeProperties": t.proxy(renames["ShapePropertiesIn"]).optional(),
            "shapeType": t.string().optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
        }
    ).named(renames["ShapeIn"])
    types["ShapeOut"] = t.struct(
        {
            "shapeProperties": t.proxy(renames["ShapePropertiesOut"]).optional(),
            "shapeType": t.string().optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapeOut"])
    types["AutoTextIn"] = t.struct(
        {
            "type": t.string().optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "type": t.string().optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
    types["UpdateLinePropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateLinePropertiesRequestIn"])
    types["UpdateLinePropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateLinePropertiesRequestOut"])
    types["CreateSlideResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSlideResponseIn"])
    types["CreateSlideResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideResponseOut"])
    types["UpdatePageElementTransformRequestIn"] = t.struct(
        {
            "applyMode": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdatePageElementTransformRequestIn"])
    types["UpdatePageElementTransformRequestOut"] = t.struct(
        {
            "applyMode": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementTransformRequestOut"])
    types["AffineTransformIn"] = t.struct(
        {
            "translateX": t.number().optional(),
            "shearX": t.number().optional(),
            "scaleX": t.number().optional(),
            "shearY": t.number().optional(),
            "translateY": t.number().optional(),
            "unit": t.string().optional(),
            "scaleY": t.number().optional(),
        }
    ).named(renames["AffineTransformIn"])
    types["AffineTransformOut"] = t.struct(
        {
            "translateX": t.number().optional(),
            "shearX": t.number().optional(),
            "scaleX": t.number().optional(),
            "shearY": t.number().optional(),
            "translateY": t.number().optional(),
            "unit": t.string().optional(),
            "scaleY": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AffineTransformOut"])
    types["OutlineIn"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "dashStyle": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillIn"]).optional(),
            "propertyState": t.string().optional(),
        }
    ).named(renames["OutlineIn"])
    types["OutlineOut"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillOut"]).optional(),
            "propertyState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineOut"])
    types["InsertTableRowsRequestIn"] = t.struct(
        {
            "insertBelow": t.boolean().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "number": t.integer().optional(),
            "tableObjectId": t.string().optional(),
        }
    ).named(renames["InsertTableRowsRequestIn"])
    types["InsertTableRowsRequestOut"] = t.struct(
        {
            "insertBelow": t.boolean().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "number": t.integer().optional(),
            "tableObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRowsRequestOut"])
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "fields": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "style": t.proxy(renames["ParagraphStyleIn"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "fields": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "style": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])

    functions = {}
    functions["presentationsGet"] = slides.post(
        "v1/presentations",
        t.struct(
            {
                "locale": t.string().optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "title": t.string().optional(),
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
                "revisionId": t.string().optional(),
                "presentationId": t.string().optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsBatchUpdate"] = slides.post(
        "v1/presentations",
        t.struct(
            {
                "locale": t.string().optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "title": t.string().optional(),
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
                "revisionId": t.string().optional(),
                "presentationId": t.string().optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsCreate"] = slides.post(
        "v1/presentations",
        t.struct(
            {
                "locale": t.string().optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "title": t.string().optional(),
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
                "revisionId": t.string().optional(),
                "presentationId": t.string().optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "auth": t.string().optional(),
            }
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

    return Import(importer="slides", renames=renames, types=types, functions=functions)
