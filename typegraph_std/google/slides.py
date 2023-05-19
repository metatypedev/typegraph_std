from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_slides() -> Import:
    slides = HTTPRuntime("https://slides.googleapis.com/")

    renames = {
        "ErrorResponse": "_slides_1_ErrorResponse",
        "TextElementIn": "_slides_2_TextElementIn",
        "TextElementOut": "_slides_3_TextElementOut",
        "SheetsChartPropertiesIn": "_slides_4_SheetsChartPropertiesIn",
        "SheetsChartPropertiesOut": "_slides_5_SheetsChartPropertiesOut",
        "UpdateParagraphStyleRequestIn": "_slides_6_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_slides_7_UpdateParagraphStyleRequestOut",
        "SlidePropertiesIn": "_slides_8_SlidePropertiesIn",
        "SlidePropertiesOut": "_slides_9_SlidePropertiesOut",
        "ReplaceAllShapesWithSheetsChartResponseIn": "_slides_10_ReplaceAllShapesWithSheetsChartResponseIn",
        "ReplaceAllShapesWithSheetsChartResponseOut": "_slides_11_ReplaceAllShapesWithSheetsChartResponseOut",
        "UpdateTableColumnPropertiesRequestIn": "_slides_12_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_slides_13_UpdateTableColumnPropertiesRequestOut",
        "LayoutPropertiesIn": "_slides_14_LayoutPropertiesIn",
        "LayoutPropertiesOut": "_slides_15_LayoutPropertiesOut",
        "TableBorderFillIn": "_slides_16_TableBorderFillIn",
        "TableBorderFillOut": "_slides_17_TableBorderFillOut",
        "UpdateLineCategoryRequestIn": "_slides_18_UpdateLineCategoryRequestIn",
        "UpdateLineCategoryRequestOut": "_slides_19_UpdateLineCategoryRequestOut",
        "LayoutReferenceIn": "_slides_20_LayoutReferenceIn",
        "LayoutReferenceOut": "_slides_21_LayoutReferenceOut",
        "ReplaceImageRequestIn": "_slides_22_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_slides_23_ReplaceImageRequestOut",
        "TableColumnPropertiesIn": "_slides_24_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_slides_25_TableColumnPropertiesOut",
        "RangeIn": "_slides_26_RangeIn",
        "RangeOut": "_slides_27_RangeOut",
        "ThemeColorPairIn": "_slides_28_ThemeColorPairIn",
        "ThemeColorPairOut": "_slides_29_ThemeColorPairOut",
        "ReplaceAllTextResponseIn": "_slides_30_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_slides_31_ReplaceAllTextResponseOut",
        "DeleteTableRowRequestIn": "_slides_32_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_slides_33_DeleteTableRowRequestOut",
        "OutlineIn": "_slides_34_OutlineIn",
        "OutlineOut": "_slides_35_OutlineOut",
        "UpdatePageElementAltTextRequestIn": "_slides_36_UpdatePageElementAltTextRequestIn",
        "UpdatePageElementAltTextRequestOut": "_slides_37_UpdatePageElementAltTextRequestOut",
        "CreateParagraphBulletsRequestIn": "_slides_38_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_slides_39_CreateParagraphBulletsRequestOut",
        "LinePropertiesIn": "_slides_40_LinePropertiesIn",
        "LinePropertiesOut": "_slides_41_LinePropertiesOut",
        "SubstringMatchCriteriaIn": "_slides_42_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_slides_43_SubstringMatchCriteriaOut",
        "UpdateTableBorderPropertiesRequestIn": "_slides_44_UpdateTableBorderPropertiesRequestIn",
        "UpdateTableBorderPropertiesRequestOut": "_slides_45_UpdateTableBorderPropertiesRequestOut",
        "LineIn": "_slides_46_LineIn",
        "LineOut": "_slides_47_LineOut",
        "BulletIn": "_slides_48_BulletIn",
        "BulletOut": "_slides_49_BulletOut",
        "SheetsChartIn": "_slides_50_SheetsChartIn",
        "SheetsChartOut": "_slides_51_SheetsChartOut",
        "OptionalColorIn": "_slides_52_OptionalColorIn",
        "OptionalColorOut": "_slides_53_OptionalColorOut",
        "CreateImageResponseIn": "_slides_54_CreateImageResponseIn",
        "CreateImageResponseOut": "_slides_55_CreateImageResponseOut",
        "TextStyleIn": "_slides_56_TextStyleIn",
        "TextStyleOut": "_slides_57_TextStyleOut",
        "CreateShapeRequestIn": "_slides_58_CreateShapeRequestIn",
        "CreateShapeRequestOut": "_slides_59_CreateShapeRequestOut",
        "TextRunIn": "_slides_60_TextRunIn",
        "TextRunOut": "_slides_61_TextRunOut",
        "UpdateLinePropertiesRequestIn": "_slides_62_UpdateLinePropertiesRequestIn",
        "UpdateLinePropertiesRequestOut": "_slides_63_UpdateLinePropertiesRequestOut",
        "DeleteTextRequestIn": "_slides_64_DeleteTextRequestIn",
        "DeleteTextRequestOut": "_slides_65_DeleteTextRequestOut",
        "WordArtIn": "_slides_66_WordArtIn",
        "WordArtOut": "_slides_67_WordArtOut",
        "TableRowPropertiesIn": "_slides_68_TableRowPropertiesIn",
        "TableRowPropertiesOut": "_slides_69_TableRowPropertiesOut",
        "PageBackgroundFillIn": "_slides_70_PageBackgroundFillIn",
        "PageBackgroundFillOut": "_slides_71_PageBackgroundFillOut",
        "DimensionIn": "_slides_72_DimensionIn",
        "DimensionOut": "_slides_73_DimensionOut",
        "TableRangeIn": "_slides_74_TableRangeIn",
        "TableRangeOut": "_slides_75_TableRangeOut",
        "PageElementIn": "_slides_76_PageElementIn",
        "PageElementOut": "_slides_77_PageElementOut",
        "UpdateTableRowPropertiesRequestIn": "_slides_78_UpdateTableRowPropertiesRequestIn",
        "UpdateTableRowPropertiesRequestOut": "_slides_79_UpdateTableRowPropertiesRequestOut",
        "LineFillIn": "_slides_80_LineFillIn",
        "LineFillOut": "_slides_81_LineFillOut",
        "MasterPropertiesIn": "_slides_82_MasterPropertiesIn",
        "MasterPropertiesOut": "_slides_83_MasterPropertiesOut",
        "UpdateImagePropertiesRequestIn": "_slides_84_UpdateImagePropertiesRequestIn",
        "UpdateImagePropertiesRequestOut": "_slides_85_UpdateImagePropertiesRequestOut",
        "TextContentIn": "_slides_86_TextContentIn",
        "TextContentOut": "_slides_87_TextContentOut",
        "WeightedFontFamilyIn": "_slides_88_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_slides_89_WeightedFontFamilyOut",
        "OpaqueColorIn": "_slides_90_OpaqueColorIn",
        "OpaqueColorOut": "_slides_91_OpaqueColorOut",
        "CreateVideoResponseIn": "_slides_92_CreateVideoResponseIn",
        "CreateVideoResponseOut": "_slides_93_CreateVideoResponseOut",
        "ReplaceAllShapesWithSheetsChartRequestIn": "_slides_94_ReplaceAllShapesWithSheetsChartRequestIn",
        "ReplaceAllShapesWithSheetsChartRequestOut": "_slides_95_ReplaceAllShapesWithSheetsChartRequestOut",
        "LineConnectionIn": "_slides_96_LineConnectionIn",
        "LineConnectionOut": "_slides_97_LineConnectionOut",
        "PageIn": "_slides_98_PageIn",
        "PageOut": "_slides_99_PageOut",
        "ReplaceAllTextRequestIn": "_slides_100_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_slides_101_ReplaceAllTextRequestOut",
        "ParagraphMarkerIn": "_slides_102_ParagraphMarkerIn",
        "ParagraphMarkerOut": "_slides_103_ParagraphMarkerOut",
        "DeleteParagraphBulletsRequestIn": "_slides_104_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_slides_105_DeleteParagraphBulletsRequestOut",
        "PageElementPropertiesIn": "_slides_106_PageElementPropertiesIn",
        "PageElementPropertiesOut": "_slides_107_PageElementPropertiesOut",
        "ImagePropertiesIn": "_slides_108_ImagePropertiesIn",
        "ImagePropertiesOut": "_slides_109_ImagePropertiesOut",
        "CreateTableResponseIn": "_slides_110_CreateTableResponseIn",
        "CreateTableResponseOut": "_slides_111_CreateTableResponseOut",
        "ColorSchemeIn": "_slides_112_ColorSchemeIn",
        "ColorSchemeOut": "_slides_113_ColorSchemeOut",
        "NestingLevelIn": "_slides_114_NestingLevelIn",
        "NestingLevelOut": "_slides_115_NestingLevelOut",
        "ParagraphStyleIn": "_slides_116_ParagraphStyleIn",
        "ParagraphStyleOut": "_slides_117_ParagraphStyleOut",
        "TableBorderRowIn": "_slides_118_TableBorderRowIn",
        "TableBorderRowOut": "_slides_119_TableBorderRowOut",
        "ShadowIn": "_slides_120_ShadowIn",
        "ShadowOut": "_slides_121_ShadowOut",
        "TableBorderCellIn": "_slides_122_TableBorderCellIn",
        "TableBorderCellOut": "_slides_123_TableBorderCellOut",
        "TableCellLocationIn": "_slides_124_TableCellLocationIn",
        "TableCellLocationOut": "_slides_125_TableCellLocationOut",
        "UngroupObjectsRequestIn": "_slides_126_UngroupObjectsRequestIn",
        "UngroupObjectsRequestOut": "_slides_127_UngroupObjectsRequestOut",
        "CreateLineRequestIn": "_slides_128_CreateLineRequestIn",
        "CreateLineRequestOut": "_slides_129_CreateLineRequestOut",
        "TableRowIn": "_slides_130_TableRowIn",
        "TableRowOut": "_slides_131_TableRowOut",
        "StretchedPictureFillIn": "_slides_132_StretchedPictureFillIn",
        "StretchedPictureFillOut": "_slides_133_StretchedPictureFillOut",
        "NotesPropertiesIn": "_slides_134_NotesPropertiesIn",
        "NotesPropertiesOut": "_slides_135_NotesPropertiesOut",
        "ShapeBackgroundFillIn": "_slides_136_ShapeBackgroundFillIn",
        "ShapeBackgroundFillOut": "_slides_137_ShapeBackgroundFillOut",
        "RequestIn": "_slides_138_RequestIn",
        "RequestOut": "_slides_139_RequestOut",
        "ResponseIn": "_slides_140_ResponseIn",
        "ResponseOut": "_slides_141_ResponseOut",
        "GroupObjectsResponseIn": "_slides_142_GroupObjectsResponseIn",
        "GroupObjectsResponseOut": "_slides_143_GroupObjectsResponseOut",
        "UpdateSlidePropertiesRequestIn": "_slides_144_UpdateSlidePropertiesRequestIn",
        "UpdateSlidePropertiesRequestOut": "_slides_145_UpdateSlidePropertiesRequestOut",
        "CreateSlideRequestIn": "_slides_146_CreateSlideRequestIn",
        "CreateSlideRequestOut": "_slides_147_CreateSlideRequestOut",
        "CreateSheetsChartRequestIn": "_slides_148_CreateSheetsChartRequestIn",
        "CreateSheetsChartRequestOut": "_slides_149_CreateSheetsChartRequestOut",
        "UpdateTextStyleRequestIn": "_slides_150_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_slides_151_UpdateTextStyleRequestOut",
        "InsertTextRequestIn": "_slides_152_InsertTextRequestIn",
        "InsertTextRequestOut": "_slides_153_InsertTextRequestOut",
        "CropPropertiesIn": "_slides_154_CropPropertiesIn",
        "CropPropertiesOut": "_slides_155_CropPropertiesOut",
        "ImageIn": "_slides_156_ImageIn",
        "ImageOut": "_slides_157_ImageOut",
        "AutoTextIn": "_slides_158_AutoTextIn",
        "AutoTextOut": "_slides_159_AutoTextOut",
        "UpdateShapePropertiesRequestIn": "_slides_160_UpdateShapePropertiesRequestIn",
        "UpdateShapePropertiesRequestOut": "_slides_161_UpdateShapePropertiesRequestOut",
        "PlaceholderIn": "_slides_162_PlaceholderIn",
        "PlaceholderOut": "_slides_163_PlaceholderOut",
        "ShapeIn": "_slides_164_ShapeIn",
        "ShapeOut": "_slides_165_ShapeOut",
        "PagePropertiesIn": "_slides_166_PagePropertiesIn",
        "PagePropertiesOut": "_slides_167_PagePropertiesOut",
        "LayoutPlaceholderIdMappingIn": "_slides_168_LayoutPlaceholderIdMappingIn",
        "LayoutPlaceholderIdMappingOut": "_slides_169_LayoutPlaceholderIdMappingOut",
        "RerouteLineRequestIn": "_slides_170_RerouteLineRequestIn",
        "RerouteLineRequestOut": "_slides_171_RerouteLineRequestOut",
        "DuplicateObjectRequestIn": "_slides_172_DuplicateObjectRequestIn",
        "DuplicateObjectRequestOut": "_slides_173_DuplicateObjectRequestOut",
        "InsertTableRowsRequestIn": "_slides_174_InsertTableRowsRequestIn",
        "InsertTableRowsRequestOut": "_slides_175_InsertTableRowsRequestOut",
        "UpdateTableCellPropertiesRequestIn": "_slides_176_UpdateTableCellPropertiesRequestIn",
        "UpdateTableCellPropertiesRequestOut": "_slides_177_UpdateTableCellPropertiesRequestOut",
        "TableCellBackgroundFillIn": "_slides_178_TableCellBackgroundFillIn",
        "TableCellBackgroundFillOut": "_slides_179_TableCellBackgroundFillOut",
        "DeleteObjectRequestIn": "_slides_180_DeleteObjectRequestIn",
        "DeleteObjectRequestOut": "_slides_181_DeleteObjectRequestOut",
        "RgbColorIn": "_slides_182_RgbColorIn",
        "RgbColorOut": "_slides_183_RgbColorOut",
        "UpdateSlidesPositionRequestIn": "_slides_184_UpdateSlidesPositionRequestIn",
        "UpdateSlidesPositionRequestOut": "_slides_185_UpdateSlidesPositionRequestOut",
        "TableBorderPropertiesIn": "_slides_186_TableBorderPropertiesIn",
        "TableBorderPropertiesOut": "_slides_187_TableBorderPropertiesOut",
        "UpdatePagePropertiesRequestIn": "_slides_188_UpdatePagePropertiesRequestIn",
        "UpdatePagePropertiesRequestOut": "_slides_189_UpdatePagePropertiesRequestOut",
        "GroupObjectsRequestIn": "_slides_190_GroupObjectsRequestIn",
        "GroupObjectsRequestOut": "_slides_191_GroupObjectsRequestOut",
        "ShapePropertiesIn": "_slides_192_ShapePropertiesIn",
        "ShapePropertiesOut": "_slides_193_ShapePropertiesOut",
        "DeleteTableColumnRequestIn": "_slides_194_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_slides_195_DeleteTableColumnRequestOut",
        "CreateShapeResponseIn": "_slides_196_CreateShapeResponseIn",
        "CreateShapeResponseOut": "_slides_197_CreateShapeResponseOut",
        "CreateTableRequestIn": "_slides_198_CreateTableRequestIn",
        "CreateTableRequestOut": "_slides_199_CreateTableRequestOut",
        "BatchUpdatePresentationResponseIn": "_slides_200_BatchUpdatePresentationResponseIn",
        "BatchUpdatePresentationResponseOut": "_slides_201_BatchUpdatePresentationResponseOut",
        "ReplaceAllShapesWithImageRequestIn": "_slides_202_ReplaceAllShapesWithImageRequestIn",
        "ReplaceAllShapesWithImageRequestOut": "_slides_203_ReplaceAllShapesWithImageRequestOut",
        "WriteControlIn": "_slides_204_WriteControlIn",
        "WriteControlOut": "_slides_205_WriteControlOut",
        "UnmergeTableCellsRequestIn": "_slides_206_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_slides_207_UnmergeTableCellsRequestOut",
        "MergeTableCellsRequestIn": "_slides_208_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_slides_209_MergeTableCellsRequestOut",
        "SizeIn": "_slides_210_SizeIn",
        "SizeOut": "_slides_211_SizeOut",
        "CreateSheetsChartResponseIn": "_slides_212_CreateSheetsChartResponseIn",
        "CreateSheetsChartResponseOut": "_slides_213_CreateSheetsChartResponseOut",
        "CreateImageRequestIn": "_slides_214_CreateImageRequestIn",
        "CreateImageRequestOut": "_slides_215_CreateImageRequestOut",
        "TableIn": "_slides_216_TableIn",
        "TableOut": "_slides_217_TableOut",
        "CreateSlideResponseIn": "_slides_218_CreateSlideResponseIn",
        "CreateSlideResponseOut": "_slides_219_CreateSlideResponseOut",
        "RefreshSheetsChartRequestIn": "_slides_220_RefreshSheetsChartRequestIn",
        "RefreshSheetsChartRequestOut": "_slides_221_RefreshSheetsChartRequestOut",
        "ReplaceAllShapesWithImageResponseIn": "_slides_222_ReplaceAllShapesWithImageResponseIn",
        "ReplaceAllShapesWithImageResponseOut": "_slides_223_ReplaceAllShapesWithImageResponseOut",
        "UpdateVideoPropertiesRequestIn": "_slides_224_UpdateVideoPropertiesRequestIn",
        "UpdateVideoPropertiesRequestOut": "_slides_225_UpdateVideoPropertiesRequestOut",
        "TableCellIn": "_slides_226_TableCellIn",
        "TableCellOut": "_slides_227_TableCellOut",
        "ListIn": "_slides_228_ListIn",
        "ListOut": "_slides_229_ListOut",
        "PresentationIn": "_slides_230_PresentationIn",
        "PresentationOut": "_slides_231_PresentationOut",
        "LinkIn": "_slides_232_LinkIn",
        "LinkOut": "_slides_233_LinkOut",
        "VideoPropertiesIn": "_slides_234_VideoPropertiesIn",
        "VideoPropertiesOut": "_slides_235_VideoPropertiesOut",
        "ColorStopIn": "_slides_236_ColorStopIn",
        "ColorStopOut": "_slides_237_ColorStopOut",
        "SolidFillIn": "_slides_238_SolidFillIn",
        "SolidFillOut": "_slides_239_SolidFillOut",
        "AutofitIn": "_slides_240_AutofitIn",
        "AutofitOut": "_slides_241_AutofitOut",
        "ThumbnailIn": "_slides_242_ThumbnailIn",
        "ThumbnailOut": "_slides_243_ThumbnailOut",
        "RecolorIn": "_slides_244_RecolorIn",
        "RecolorOut": "_slides_245_RecolorOut",
        "InsertTableColumnsRequestIn": "_slides_246_InsertTableColumnsRequestIn",
        "InsertTableColumnsRequestOut": "_slides_247_InsertTableColumnsRequestOut",
        "BatchUpdatePresentationRequestIn": "_slides_248_BatchUpdatePresentationRequestIn",
        "BatchUpdatePresentationRequestOut": "_slides_249_BatchUpdatePresentationRequestOut",
        "AffineTransformIn": "_slides_250_AffineTransformIn",
        "AffineTransformOut": "_slides_251_AffineTransformOut",
        "TableCellPropertiesIn": "_slides_252_TableCellPropertiesIn",
        "TableCellPropertiesOut": "_slides_253_TableCellPropertiesOut",
        "GroupIn": "_slides_254_GroupIn",
        "GroupOut": "_slides_255_GroupOut",
        "DuplicateObjectResponseIn": "_slides_256_DuplicateObjectResponseIn",
        "DuplicateObjectResponseOut": "_slides_257_DuplicateObjectResponseOut",
        "CreateLineResponseIn": "_slides_258_CreateLineResponseIn",
        "CreateLineResponseOut": "_slides_259_CreateLineResponseOut",
        "UpdatePageElementTransformRequestIn": "_slides_260_UpdatePageElementTransformRequestIn",
        "UpdatePageElementTransformRequestOut": "_slides_261_UpdatePageElementTransformRequestOut",
        "UpdatePageElementsZOrderRequestIn": "_slides_262_UpdatePageElementsZOrderRequestIn",
        "UpdatePageElementsZOrderRequestOut": "_slides_263_UpdatePageElementsZOrderRequestOut",
        "VideoIn": "_slides_264_VideoIn",
        "VideoOut": "_slides_265_VideoOut",
        "OutlineFillIn": "_slides_266_OutlineFillIn",
        "OutlineFillOut": "_slides_267_OutlineFillOut",
        "CreateVideoRequestIn": "_slides_268_CreateVideoRequestIn",
        "CreateVideoRequestOut": "_slides_269_CreateVideoRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TextElementIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "paragraphMarker": t.proxy(renames["ParagraphMarkerIn"]).optional(),
            "endIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
        }
    ).named(renames["TextElementIn"])
    types["TextElementOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "paragraphMarker": t.proxy(renames["ParagraphMarkerOut"]).optional(),
            "endIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextElementOut"])
    types["SheetsChartPropertiesIn"] = t.struct(
        {"chartImageProperties": t.proxy(renames["ImagePropertiesIn"]).optional()}
    ).named(renames["SheetsChartPropertiesIn"])
    types["SheetsChartPropertiesOut"] = t.struct(
        {
            "chartImageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartPropertiesOut"])
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "style": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "style": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])
    types["SlidePropertiesIn"] = t.struct(
        {
            "layoutObjectId": t.string().optional(),
            "notesPage": t.proxy(renames["PageIn"]).optional(),
            "masterObjectId": t.string().optional(),
            "isSkipped": t.boolean().optional(),
        }
    ).named(renames["SlidePropertiesIn"])
    types["SlidePropertiesOut"] = t.struct(
        {
            "layoutObjectId": t.string().optional(),
            "notesPage": t.proxy(renames["PageOut"]).optional(),
            "masterObjectId": t.string().optional(),
            "isSkipped": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlidePropertiesOut"])
    types["ReplaceAllShapesWithSheetsChartResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseIn"])
    types["ReplaceAllShapesWithSheetsChartResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseOut"])
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "objectId": t.string().optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["LayoutPropertiesIn"] = t.struct(
        {
            "masterObjectId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LayoutPropertiesIn"])
    types["LayoutPropertiesOut"] = t.struct(
        {
            "masterObjectId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutPropertiesOut"])
    types["TableBorderFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["TableBorderFillIn"])
    types["TableBorderFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderFillOut"])
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
    types["ReplaceImageRequestIn"] = t.struct(
        {
            "imageObjectId": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ReplaceImageRequestIn"])
    types["ReplaceImageRequestOut"] = t.struct(
        {
            "imageObjectId": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceImageRequestOut"])
    types["TableColumnPropertiesIn"] = t.struct(
        {"columnWidth": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableColumnPropertiesIn"])
    types["TableColumnPropertiesOut"] = t.struct(
        {
            "columnWidth": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableColumnPropertiesOut"])
    types["RangeIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
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
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
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
    types["OutlineIn"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "dashStyle": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillIn"]).optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["OutlineIn"])
    types["OutlineOut"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "dashStyle": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillOut"]).optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineOut"])
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
    types["CreateParagraphBulletsRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "objectId": t.string().optional(),
            "bulletPreset": t.string().optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestIn"])
    types["CreateParagraphBulletsRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "objectId": t.string().optional(),
            "bulletPreset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestOut"])
    types["LinePropertiesIn"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "startArrow": t.string().optional(),
            "endArrow": t.string().optional(),
            "dashStyle": t.string().optional(),
            "lineFill": t.proxy(renames["LineFillIn"]).optional(),
            "startConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionIn"]).optional(),
        }
    ).named(renames["LinePropertiesIn"])
    types["LinePropertiesOut"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "startArrow": t.string().optional(),
            "endArrow": t.string().optional(),
            "dashStyle": t.string().optional(),
            "lineFill": t.proxy(renames["LineFillOut"]).optional(),
            "startConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinePropertiesOut"])
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
    types["UpdateTableBorderPropertiesRequestIn"] = t.struct(
        {
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesIn"]
            ).optional(),
            "fields": t.string().optional(),
            "borderPosition": t.string().optional(),
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestIn"])
    types["UpdateTableBorderPropertiesRequestOut"] = t.struct(
        {
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesOut"]
            ).optional(),
            "fields": t.string().optional(),
            "borderPosition": t.string().optional(),
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestOut"])
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
    types["SheetsChartIn"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesIn"]
            ).optional(),
        }
    ).named(renames["SheetsChartIn"])
    types["SheetsChartOut"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartOut"])
    types["OptionalColorIn"] = t.struct(
        {"opaqueColor": t.proxy(renames["OpaqueColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "opaqueColor": t.proxy(renames["OpaqueColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
    types["CreateImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateImageResponseIn"])
    types["CreateImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageResponseOut"])
    types["TextStyleIn"] = t.struct(
        {
            "fontFamily": t.string().optional(),
            "italic": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "strikethrough": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "baselineOffset": t.string().optional(),
            "smallCaps": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "bold": t.boolean().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "fontFamily": t.string().optional(),
            "italic": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "strikethrough": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "baselineOffset": t.string().optional(),
            "smallCaps": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "bold": t.boolean().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
    types["CreateShapeRequestIn"] = t.struct(
        {
            "shapeType": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["CreateShapeRequestIn"])
    types["CreateShapeRequestOut"] = t.struct(
        {
            "shapeType": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeRequestOut"])
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
    types["UpdateLinePropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesIn"]).optional(),
        }
    ).named(renames["UpdateLinePropertiesRequestIn"])
    types["UpdateLinePropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateLinePropertiesRequestOut"])
    types["DeleteTextRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["DeleteTextRequestIn"])
    types["DeleteTextRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTextRequestOut"])
    types["WordArtIn"] = t.struct({"renderedText": t.string().optional()}).named(
        renames["WordArtIn"]
    )
    types["WordArtOut"] = t.struct(
        {
            "renderedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordArtOut"])
    types["TableRowPropertiesIn"] = t.struct(
        {"minRowHeight": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableRowPropertiesIn"])
    types["TableRowPropertiesOut"] = t.struct(
        {
            "minRowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowPropertiesOut"])
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
    types["DimensionIn"] = t.struct(
        {"magnitude": t.number().optional(), "unit": t.string().optional()}
    ).named(renames["DimensionIn"])
    types["DimensionOut"] = t.struct(
        {
            "magnitude": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOut"])
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
    types["PageElementIn"] = t.struct(
        {
            "title": t.string().optional(),
            "line": t.proxy(renames["LineIn"]).optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "objectId": t.string().optional(),
            "shape": t.proxy(renames["ShapeIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "sheetsChart": t.proxy(renames["SheetsChartIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "description": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "elementGroup": t.proxy(renames["GroupIn"]).optional(),
            "wordArt": t.proxy(renames["WordArtIn"]).optional(),
            "video": t.proxy(renames["VideoIn"]).optional(),
        }
    ).named(renames["PageElementIn"])
    types["PageElementOut"] = t.struct(
        {
            "title": t.string().optional(),
            "line": t.proxy(renames["LineOut"]).optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "objectId": t.string().optional(),
            "shape": t.proxy(renames["ShapeOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "sheetsChart": t.proxy(renames["SheetsChartOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "description": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "elementGroup": t.proxy(renames["GroupOut"]).optional(),
            "wordArt": t.proxy(renames["WordArtOut"]).optional(),
            "video": t.proxy(renames["VideoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementOut"])
    types["UpdateTableRowPropertiesRequestIn"] = t.struct(
        {
            "rowIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestIn"])
    types["UpdateTableRowPropertiesRequestOut"] = t.struct(
        {
            "rowIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestOut"])
    types["LineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["LineFillIn"])
    types["LineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineFillOut"])
    types["MasterPropertiesIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["MasterPropertiesIn"])
    types["MasterPropertiesOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterPropertiesOut"])
    types["UpdateImagePropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
        }
    ).named(renames["UpdateImagePropertiesRequestIn"])
    types["UpdateImagePropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateImagePropertiesRequestOut"])
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
    types["CreateVideoResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateVideoResponseIn"])
    types["CreateVideoResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoResponseOut"])
    types["ReplaceAllShapesWithSheetsChartRequestIn"] = t.struct(
        {
            "linkingMode": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestIn"])
    types["ReplaceAllShapesWithSheetsChartRequestOut"] = t.struct(
        {
            "linkingMode": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestOut"])
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
    types["PageIn"] = t.struct(
        {
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesIn"]).optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesIn"]).optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
            "pageElements": t.array(t.proxy(renames["PageElementIn"])).optional(),
            "revisionId": t.string().optional(),
            "pageType": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesOut"]).optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesOut"]).optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "pageElements": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "revisionId": t.string().optional(),
            "pageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["ReplaceAllTextRequestIn"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "replaceText": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
        }
    ).named(renames["ReplaceAllTextRequestIn"])
    types["ReplaceAllTextRequestOut"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "replaceText": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextRequestOut"])
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
    types["DeleteParagraphBulletsRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestIn"])
    types["DeleteParagraphBulletsRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestOut"])
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
    types["ImagePropertiesIn"] = t.struct(
        {
            "transparency": t.number().optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
            "brightness": t.number().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "contrast": t.number().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "recolor": t.proxy(renames["RecolorIn"]).optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "transparency": t.number().optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "brightness": t.number().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "contrast": t.number().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "recolor": t.proxy(renames["RecolorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["CreateTableResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateTableResponseIn"])
    types["CreateTableResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableResponseOut"])
    types["ColorSchemeIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ThemeColorPairIn"])).optional()}
    ).named(renames["ColorSchemeIn"])
    types["ColorSchemeOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ThemeColorPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorSchemeOut"])
    types["NestingLevelIn"] = t.struct(
        {"bulletStyle": t.proxy(renames["TextStyleIn"]).optional()}
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "alignment": t.string().optional(),
            "lineSpacing": t.number().optional(),
            "spacingMode": t.string().optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "direction": t.string().optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "alignment": t.string().optional(),
            "lineSpacing": t.number().optional(),
            "spacingMode": t.string().optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "direction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
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
    types["ShadowIn"] = t.struct(
        {
            "alignment": t.string().optional(),
            "alpha": t.number().optional(),
            "rotateWithShape": t.boolean().optional(),
            "propertyState": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "blurRadius": t.proxy(renames["DimensionIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ShadowIn"])
    types["ShadowOut"] = t.struct(
        {
            "alignment": t.string().optional(),
            "alpha": t.number().optional(),
            "rotateWithShape": t.boolean().optional(),
            "propertyState": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "blurRadius": t.proxy(renames["DimensionOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadowOut"])
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
    types["UngroupObjectsRequestIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["UngroupObjectsRequestIn"])
    types["UngroupObjectsRequestOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UngroupObjectsRequestOut"])
    types["CreateLineRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "category": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "lineCategory": t.string().optional(),
        }
    ).named(renames["CreateLineRequestIn"])
    types["CreateLineRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "category": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "lineCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineRequestOut"])
    types["TableRowIn"] = t.struct(
        {
            "rowHeight": t.proxy(renames["DimensionIn"]).optional(),
            "tableCells": t.array(t.proxy(renames["TableCellIn"])).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
        }
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "rowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "tableCells": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["StretchedPictureFillIn"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
        }
    ).named(renames["StretchedPictureFillIn"])
    types["StretchedPictureFillOut"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StretchedPictureFillOut"])
    types["NotesPropertiesIn"] = t.struct(
        {"speakerNotesObjectId": t.string().optional()}
    ).named(renames["NotesPropertiesIn"])
    types["NotesPropertiesOut"] = t.struct(
        {
            "speakerNotesObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotesPropertiesOut"])
    types["ShapeBackgroundFillIn"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
        }
    ).named(renames["ShapeBackgroundFillIn"])
    types["ShapeBackgroundFillOut"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapeBackgroundFillOut"])
    types["RequestIn"] = t.struct(
        {
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestIn"]).optional(),
            "createTable": t.proxy(renames["CreateTableRequestIn"]).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestIn"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestIn"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestIn"]).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestIn"]).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestIn"]
            ).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestIn"]
            ).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestIn"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestIn"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestIn"]
            ).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestIn"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestIn"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestIn"]).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestIn"]).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestIn"]
            ).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestIn"]
            ).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestIn"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestIn"]
            ).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestIn"]
            ).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestIn"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestIn"]).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestIn"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestIn"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestIn"]).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestIn"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestIn"]
            ).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestIn"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestIn"]
            ).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestIn"]).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestOut"]).optional(),
            "createTable": t.proxy(renames["CreateTableRequestOut"]).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestOut"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestOut"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestOut"]).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestOut"]).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestOut"]
            ).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestOut"]
            ).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestOut"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestOut"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestOut"]
            ).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestOut"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestOut"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestOut"]).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestOut"]).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestOut"]
            ).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestOut"]
            ).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestOut"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestOut"]
            ).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestOut"]
            ).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestOut"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestOut"]).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestOut"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestOut"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestOut"]).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestOut"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestOut"]
            ).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestOut"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestOut"]
            ).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestOut"]).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["ResponseIn"] = t.struct(
        {
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseIn"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineResponseIn"]).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectResponseIn"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseIn"]).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseIn"]).optional(),
            "createTable": t.proxy(renames["CreateTableResponseIn"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseIn"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseIn"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseIn"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseIn"]).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseOut"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineResponseOut"]).optional(),
            "duplicateObject": t.proxy(
                renames["DuplicateObjectResponseOut"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseOut"]).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseOut"]).optional(),
            "createTable": t.proxy(renames["CreateTableResponseOut"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseOut"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseOut"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseOut"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["GroupObjectsResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["GroupObjectsResponseIn"])
    types["GroupObjectsResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupObjectsResponseOut"])
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
    types["CreateSlideRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingIn"])
            ).optional(),
            "insertionIndex": t.integer().optional(),
            "slideLayoutReference": t.proxy(renames["LayoutReferenceIn"]).optional(),
        }
    ).named(renames["CreateSlideRequestIn"])
    types["CreateSlideRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingOut"])
            ).optional(),
            "insertionIndex": t.integer().optional(),
            "slideLayoutReference": t.proxy(renames["LayoutReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideRequestOut"])
    types["CreateSheetsChartRequestIn"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "linkingMode": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
        }
    ).named(renames["CreateSheetsChartRequestIn"])
    types["CreateSheetsChartRequestOut"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "linkingMode": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartRequestOut"])
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
    types["InsertTextRequestIn"] = t.struct(
        {
            "text": t.string().optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "insertionIndex": t.integer().optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "text": t.string().optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "insertionIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
    types["CropPropertiesIn"] = t.struct(
        {
            "leftOffset": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "angle": t.number().optional(),
            "rightOffset": t.number().optional(),
            "topOffset": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "leftOffset": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "angle": t.number().optional(),
            "rightOffset": t.number().optional(),
            "topOffset": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
    types["ImageIn"] = t.struct(
        {
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "contentUrl": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "sourceUrl": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "contentUrl": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "sourceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["AutoTextIn"] = t.struct(
        {
            "content": t.string().optional(),
            "type": t.string().optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "content": t.string().optional(),
            "type": t.string().optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
    types["UpdateShapePropertiesRequestIn"] = t.struct(
        {
            "shapeProperties": t.proxy(renames["ShapePropertiesIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateShapePropertiesRequestIn"])
    types["UpdateShapePropertiesRequestOut"] = t.struct(
        {
            "shapeProperties": t.proxy(renames["ShapePropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateShapePropertiesRequestOut"])
    types["PlaceholderIn"] = t.struct(
        {
            "parentObjectId": t.string().optional(),
            "type": t.string().optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["PlaceholderIn"])
    types["PlaceholderOut"] = t.struct(
        {
            "parentObjectId": t.string().optional(),
            "type": t.string().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceholderOut"])
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
    types["RerouteLineRequestIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["RerouteLineRequestIn"]
    )
    types["RerouteLineRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RerouteLineRequestOut"])
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
    types["InsertTableRowsRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "tableObjectId": t.string().optional(),
            "number": t.integer().optional(),
            "insertBelow": t.boolean().optional(),
        }
    ).named(renames["InsertTableRowsRequestIn"])
    types["InsertTableRowsRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "tableObjectId": t.string().optional(),
            "number": t.integer().optional(),
            "insertBelow": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRowsRequestOut"])
    types["UpdateTableCellPropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestIn"])
    types["UpdateTableCellPropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestOut"])
    types["TableCellBackgroundFillIn"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
            "propertyState": t.string().optional(),
        }
    ).named(renames["TableCellBackgroundFillIn"])
    types["TableCellBackgroundFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "propertyState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellBackgroundFillOut"])
    types["DeleteObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeleteObjectRequestIn"])
    types["DeleteObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteObjectRequestOut"])
    types["RgbColorIn"] = t.struct(
        {
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
        }
    ).named(renames["RgbColorIn"])
    types["RgbColorOut"] = t.struct(
        {
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RgbColorOut"])
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
    types["TableBorderPropertiesIn"] = t.struct(
        {
            "tableBorderFill": t.proxy(renames["TableBorderFillIn"]).optional(),
            "dashStyle": t.string().optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["TableBorderPropertiesIn"])
    types["TableBorderPropertiesOut"] = t.struct(
        {
            "tableBorderFill": t.proxy(renames["TableBorderFillOut"]).optional(),
            "dashStyle": t.string().optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderPropertiesOut"])
    types["UpdatePagePropertiesRequestIn"] = t.struct(
        {
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestIn"])
    types["UpdatePagePropertiesRequestOut"] = t.struct(
        {
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestOut"])
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
    types["ShapePropertiesIn"] = t.struct(
        {
            "contentAlignment": t.string().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "shapeBackgroundFill": t.proxy(renames["ShapeBackgroundFillIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "autofit": t.proxy(renames["AutofitIn"]).optional(),
        }
    ).named(renames["ShapePropertiesIn"])
    types["ShapePropertiesOut"] = t.struct(
        {
            "contentAlignment": t.string().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "shapeBackgroundFill": t.proxy(
                renames["ShapeBackgroundFillOut"]
            ).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "autofit": t.proxy(renames["AutofitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapePropertiesOut"])
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
    types["CreateShapeResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateShapeResponseIn"])
    types["CreateShapeResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeResponseOut"])
    types["CreateTableRequestIn"] = t.struct(
        {
            "rows": t.integer().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "columns": t.integer().optional(),
        }
    ).named(renames["CreateTableRequestIn"])
    types["CreateTableRequestOut"] = t.struct(
        {
            "rows": t.integer().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "columns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableRequestOut"])
    types["BatchUpdatePresentationResponseIn"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "presentationId": t.string().optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdatePresentationResponseIn"])
    types["BatchUpdatePresentationResponseOut"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "presentationId": t.string().optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePresentationResponseOut"])
    types["ReplaceAllShapesWithImageRequestIn"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "imageUrl": t.string().optional(),
            "replaceMethod": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestIn"])
    types["ReplaceAllShapesWithImageRequestOut"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "imageUrl": t.string().optional(),
            "replaceMethod": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestOut"])
    types["WriteControlIn"] = t.struct(
        {"requiredRevisionId": t.string().optional()}
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
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
    types["CreateSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSheetsChartResponseIn"])
    types["CreateSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartResponseOut"])
    types["CreateImageRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "url": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
        }
    ).named(renames["CreateImageRequestIn"])
    types["CreateImageRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "url": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageRequestOut"])
    types["TableIn"] = t.struct(
        {
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesIn"])
            ).optional(),
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesOut"])
            ).optional(),
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["CreateSlideResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSlideResponseIn"])
    types["CreateSlideResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideResponseOut"])
    types["RefreshSheetsChartRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["RefreshSheetsChartRequestIn"])
    types["RefreshSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshSheetsChartRequestOut"])
    types["ReplaceAllShapesWithImageResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithImageResponseIn"])
    types["ReplaceAllShapesWithImageResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageResponseOut"])
    types["UpdateVideoPropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestIn"])
    types["UpdateVideoPropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestOut"])
    types["TableCellIn"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
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
    types["PresentationIn"] = t.struct(
        {
            "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "masters": t.array(t.proxy(renames["PageIn"])).optional(),
            "notesMaster": t.proxy(renames["PageIn"]).optional(),
            "presentationId": t.string().optional(),
            "revisionId": t.string().optional(),
            "slides": t.array(t.proxy(renames["PageIn"])).optional(),
            "title": t.string().optional(),
            "locale": t.string().optional(),
        }
    ).named(renames["PresentationIn"])
    types["PresentationOut"] = t.struct(
        {
            "layouts": t.array(t.proxy(renames["PageOut"])).optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "masters": t.array(t.proxy(renames["PageOut"])).optional(),
            "notesMaster": t.proxy(renames["PageOut"]).optional(),
            "presentationId": t.string().optional(),
            "revisionId": t.string().optional(),
            "slides": t.array(t.proxy(renames["PageOut"])).optional(),
            "title": t.string().optional(),
            "locale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationOut"])
    types["LinkIn"] = t.struct(
        {
            "slideIndex": t.integer().optional(),
            "relativeLink": t.string().optional(),
            "url": t.string().optional(),
            "pageObjectId": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "slideIndex": t.integer().optional(),
            "relativeLink": t.string().optional(),
            "url": t.string().optional(),
            "pageObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["VideoPropertiesIn"] = t.struct(
        {
            "autoPlay": t.boolean().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "start": t.integer().optional(),
            "end": t.integer().optional(),
            "mute": t.boolean().optional(),
        }
    ).named(renames["VideoPropertiesIn"])
    types["VideoPropertiesOut"] = t.struct(
        {
            "autoPlay": t.boolean().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "start": t.integer().optional(),
            "end": t.integer().optional(),
            "mute": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPropertiesOut"])
    types["ColorStopIn"] = t.struct(
        {
            "position": t.number().optional(),
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ColorStopIn"])
    types["ColorStopOut"] = t.struct(
        {
            "position": t.number().optional(),
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorStopOut"])
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
    types["ThumbnailIn"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "contentUrl": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
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
    types["InsertTableColumnsRequestIn"] = t.struct(
        {
            "insertRight": t.boolean().optional(),
            "number": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "tableObjectId": t.string().optional(),
        }
    ).named(renames["InsertTableColumnsRequestIn"])
    types["InsertTableColumnsRequestOut"] = t.struct(
        {
            "insertRight": t.boolean().optional(),
            "number": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "tableObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableColumnsRequestOut"])
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
    types["AffineTransformIn"] = t.struct(
        {
            "scaleY": t.number().optional(),
            "scaleX": t.number().optional(),
            "shearY": t.number().optional(),
            "shearX": t.number().optional(),
            "translateX": t.number().optional(),
            "translateY": t.number().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["AffineTransformIn"])
    types["AffineTransformOut"] = t.struct(
        {
            "scaleY": t.number().optional(),
            "scaleX": t.number().optional(),
            "shearY": t.number().optional(),
            "shearX": t.number().optional(),
            "translateX": t.number().optional(),
            "translateY": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AffineTransformOut"])
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
    types["GroupIn"] = t.struct(
        {"children": t.array(t.proxy(renames["PageElementIn"])).optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "children": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["DuplicateObjectResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DuplicateObjectResponseIn"])
    types["DuplicateObjectResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateObjectResponseOut"])
    types["CreateLineResponseIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["CreateLineResponseIn"]
    )
    types["CreateLineResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineResponseOut"])
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
    types["VideoIn"] = t.struct(
        {
            "source": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesIn"]).optional(),
            "url": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["VideoIn"])
    types["VideoOut"] = t.struct(
        {
            "source": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesOut"]).optional(),
            "url": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOut"])
    types["OutlineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["OutlineFillIn"])
    types["OutlineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineFillOut"])
    types["CreateVideoRequestIn"] = t.struct(
        {
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "source": t.string().optional(),
            "objectId": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CreateVideoRequestIn"])
    types["CreateVideoRequestOut"] = t.struct(
        {
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "source": t.string().optional(),
            "objectId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoRequestOut"])

    functions = {}
    functions["presentationsGet"] = slides.post(
        "v1/presentations",
        t.struct(
            {
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "presentationId": t.string().optional(),
                "revisionId": t.string().optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "title": t.string().optional(),
                "locale": t.string().optional(),
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
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "presentationId": t.string().optional(),
                "revisionId": t.string().optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "title": t.string().optional(),
                "locale": t.string().optional(),
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
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "presentationId": t.string().optional(),
                "revisionId": t.string().optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "title": t.string().optional(),
                "locale": t.string().optional(),
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

    return Import(
        importer="slides", renames=renames, types=Box(types), functions=Box(functions)
    )
