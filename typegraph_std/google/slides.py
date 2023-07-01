from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_slides():
    slides = HTTPRuntime("https://slides.googleapis.com/")

    renames = {
        "ErrorResponse": "_slides_1_ErrorResponse",
        "WriteControlIn": "_slides_2_WriteControlIn",
        "WriteControlOut": "_slides_3_WriteControlOut",
        "ListIn": "_slides_4_ListIn",
        "ListOut": "_slides_5_ListOut",
        "RequestIn": "_slides_6_RequestIn",
        "RequestOut": "_slides_7_RequestOut",
        "TableRangeIn": "_slides_8_TableRangeIn",
        "TableRangeOut": "_slides_9_TableRangeOut",
        "PlaceholderIn": "_slides_10_PlaceholderIn",
        "PlaceholderOut": "_slides_11_PlaceholderOut",
        "UpdatePagePropertiesRequestIn": "_slides_12_UpdatePagePropertiesRequestIn",
        "UpdatePagePropertiesRequestOut": "_slides_13_UpdatePagePropertiesRequestOut",
        "TableBorderPropertiesIn": "_slides_14_TableBorderPropertiesIn",
        "TableBorderPropertiesOut": "_slides_15_TableBorderPropertiesOut",
        "LineIn": "_slides_16_LineIn",
        "LineOut": "_slides_17_LineOut",
        "AutofitIn": "_slides_18_AutofitIn",
        "AutofitOut": "_slides_19_AutofitOut",
        "DeleteTableRowRequestIn": "_slides_20_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_slides_21_DeleteTableRowRequestOut",
        "RgbColorIn": "_slides_22_RgbColorIn",
        "RgbColorOut": "_slides_23_RgbColorOut",
        "DuplicateObjectResponseIn": "_slides_24_DuplicateObjectResponseIn",
        "DuplicateObjectResponseOut": "_slides_25_DuplicateObjectResponseOut",
        "CreateShapeResponseIn": "_slides_26_CreateShapeResponseIn",
        "CreateShapeResponseOut": "_slides_27_CreateShapeResponseOut",
        "CreateImageResponseIn": "_slides_28_CreateImageResponseIn",
        "CreateImageResponseOut": "_slides_29_CreateImageResponseOut",
        "CreateTableResponseIn": "_slides_30_CreateTableResponseIn",
        "CreateTableResponseOut": "_slides_31_CreateTableResponseOut",
        "TableCellBackgroundFillIn": "_slides_32_TableCellBackgroundFillIn",
        "TableCellBackgroundFillOut": "_slides_33_TableCellBackgroundFillOut",
        "UpdateTableRowPropertiesRequestIn": "_slides_34_UpdateTableRowPropertiesRequestIn",
        "UpdateTableRowPropertiesRequestOut": "_slides_35_UpdateTableRowPropertiesRequestOut",
        "UpdateTableBorderPropertiesRequestIn": "_slides_36_UpdateTableBorderPropertiesRequestIn",
        "UpdateTableBorderPropertiesRequestOut": "_slides_37_UpdateTableBorderPropertiesRequestOut",
        "OpaqueColorIn": "_slides_38_OpaqueColorIn",
        "OpaqueColorOut": "_slides_39_OpaqueColorOut",
        "SizeIn": "_slides_40_SizeIn",
        "SizeOut": "_slides_41_SizeOut",
        "CreateSheetsChartRequestIn": "_slides_42_CreateSheetsChartRequestIn",
        "CreateSheetsChartRequestOut": "_slides_43_CreateSheetsChartRequestOut",
        "UngroupObjectsRequestIn": "_slides_44_UngroupObjectsRequestIn",
        "UngroupObjectsRequestOut": "_slides_45_UngroupObjectsRequestOut",
        "LineFillIn": "_slides_46_LineFillIn",
        "LineFillOut": "_slides_47_LineFillOut",
        "TextElementIn": "_slides_48_TextElementIn",
        "TextElementOut": "_slides_49_TextElementOut",
        "UpdateTableCellPropertiesRequestIn": "_slides_50_UpdateTableCellPropertiesRequestIn",
        "UpdateTableCellPropertiesRequestOut": "_slides_51_UpdateTableCellPropertiesRequestOut",
        "CreateLineRequestIn": "_slides_52_CreateLineRequestIn",
        "CreateLineRequestOut": "_slides_53_CreateLineRequestOut",
        "UpdatePageElementsZOrderRequestIn": "_slides_54_UpdatePageElementsZOrderRequestIn",
        "UpdatePageElementsZOrderRequestOut": "_slides_55_UpdatePageElementsZOrderRequestOut",
        "AffineTransformIn": "_slides_56_AffineTransformIn",
        "AffineTransformOut": "_slides_57_AffineTransformOut",
        "LinePropertiesIn": "_slides_58_LinePropertiesIn",
        "LinePropertiesOut": "_slides_59_LinePropertiesOut",
        "UnmergeTableCellsRequestIn": "_slides_60_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_slides_61_UnmergeTableCellsRequestOut",
        "TableRowIn": "_slides_62_TableRowIn",
        "TableRowOut": "_slides_63_TableRowOut",
        "NotesPropertiesIn": "_slides_64_NotesPropertiesIn",
        "NotesPropertiesOut": "_slides_65_NotesPropertiesOut",
        "OutlineFillIn": "_slides_66_OutlineFillIn",
        "OutlineFillOut": "_slides_67_OutlineFillOut",
        "TableCellPropertiesIn": "_slides_68_TableCellPropertiesIn",
        "TableCellPropertiesOut": "_slides_69_TableCellPropertiesOut",
        "GroupIn": "_slides_70_GroupIn",
        "GroupOut": "_slides_71_GroupOut",
        "DuplicateObjectRequestIn": "_slides_72_DuplicateObjectRequestIn",
        "DuplicateObjectRequestOut": "_slides_73_DuplicateObjectRequestOut",
        "InsertTableColumnsRequestIn": "_slides_74_InsertTableColumnsRequestIn",
        "InsertTableColumnsRequestOut": "_slides_75_InsertTableColumnsRequestOut",
        "InsertTableRowsRequestIn": "_slides_76_InsertTableRowsRequestIn",
        "InsertTableRowsRequestOut": "_slides_77_InsertTableRowsRequestOut",
        "CreateVideoRequestIn": "_slides_78_CreateVideoRequestIn",
        "CreateVideoRequestOut": "_slides_79_CreateVideoRequestOut",
        "LinkIn": "_slides_80_LinkIn",
        "LinkOut": "_slides_81_LinkOut",
        "BatchUpdatePresentationResponseIn": "_slides_82_BatchUpdatePresentationResponseIn",
        "BatchUpdatePresentationResponseOut": "_slides_83_BatchUpdatePresentationResponseOut",
        "ColorSchemeIn": "_slides_84_ColorSchemeIn",
        "ColorSchemeOut": "_slides_85_ColorSchemeOut",
        "ReplaceAllTextRequestIn": "_slides_86_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_slides_87_ReplaceAllTextRequestOut",
        "ThumbnailIn": "_slides_88_ThumbnailIn",
        "ThumbnailOut": "_slides_89_ThumbnailOut",
        "RerouteLineRequestIn": "_slides_90_RerouteLineRequestIn",
        "RerouteLineRequestOut": "_slides_91_RerouteLineRequestOut",
        "TableCellIn": "_slides_92_TableCellIn",
        "TableCellOut": "_slides_93_TableCellOut",
        "TableBorderFillIn": "_slides_94_TableBorderFillIn",
        "TableBorderFillOut": "_slides_95_TableBorderFillOut",
        "LayoutPlaceholderIdMappingIn": "_slides_96_LayoutPlaceholderIdMappingIn",
        "LayoutPlaceholderIdMappingOut": "_slides_97_LayoutPlaceholderIdMappingOut",
        "CreateSlideResponseIn": "_slides_98_CreateSlideResponseIn",
        "CreateSlideResponseOut": "_slides_99_CreateSlideResponseOut",
        "PageIn": "_slides_100_PageIn",
        "PageOut": "_slides_101_PageOut",
        "ParagraphStyleIn": "_slides_102_ParagraphStyleIn",
        "ParagraphStyleOut": "_slides_103_ParagraphStyleOut",
        "UpdatePageElementTransformRequestIn": "_slides_104_UpdatePageElementTransformRequestIn",
        "UpdatePageElementTransformRequestOut": "_slides_105_UpdatePageElementTransformRequestOut",
        "TableColumnPropertiesIn": "_slides_106_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_slides_107_TableColumnPropertiesOut",
        "BulletIn": "_slides_108_BulletIn",
        "BulletOut": "_slides_109_BulletOut",
        "ColorStopIn": "_slides_110_ColorStopIn",
        "ColorStopOut": "_slides_111_ColorStopOut",
        "TextRunIn": "_slides_112_TextRunIn",
        "TextRunOut": "_slides_113_TextRunOut",
        "SlidePropertiesIn": "_slides_114_SlidePropertiesIn",
        "SlidePropertiesOut": "_slides_115_SlidePropertiesOut",
        "UpdateVideoPropertiesRequestIn": "_slides_116_UpdateVideoPropertiesRequestIn",
        "UpdateVideoPropertiesRequestOut": "_slides_117_UpdateVideoPropertiesRequestOut",
        "CropPropertiesIn": "_slides_118_CropPropertiesIn",
        "CropPropertiesOut": "_slides_119_CropPropertiesOut",
        "ReplaceImageRequestIn": "_slides_120_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_slides_121_ReplaceImageRequestOut",
        "DeleteTableColumnRequestIn": "_slides_122_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_slides_123_DeleteTableColumnRequestOut",
        "OutlineIn": "_slides_124_OutlineIn",
        "OutlineOut": "_slides_125_OutlineOut",
        "UpdateTextStyleRequestIn": "_slides_126_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_slides_127_UpdateTextStyleRequestOut",
        "SheetsChartIn": "_slides_128_SheetsChartIn",
        "SheetsChartOut": "_slides_129_SheetsChartOut",
        "LayoutReferenceIn": "_slides_130_LayoutReferenceIn",
        "LayoutReferenceOut": "_slides_131_LayoutReferenceOut",
        "DeleteParagraphBulletsRequestIn": "_slides_132_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_slides_133_DeleteParagraphBulletsRequestOut",
        "ImageIn": "_slides_134_ImageIn",
        "ImageOut": "_slides_135_ImageOut",
        "CreateShapeRequestIn": "_slides_136_CreateShapeRequestIn",
        "CreateShapeRequestOut": "_slides_137_CreateShapeRequestOut",
        "PagePropertiesIn": "_slides_138_PagePropertiesIn",
        "PagePropertiesOut": "_slides_139_PagePropertiesOut",
        "TableCellLocationIn": "_slides_140_TableCellLocationIn",
        "TableCellLocationOut": "_slides_141_TableCellLocationOut",
        "ImagePropertiesIn": "_slides_142_ImagePropertiesIn",
        "ImagePropertiesOut": "_slides_143_ImagePropertiesOut",
        "OptionalColorIn": "_slides_144_OptionalColorIn",
        "OptionalColorOut": "_slides_145_OptionalColorOut",
        "ReplaceAllTextResponseIn": "_slides_146_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_slides_147_ReplaceAllTextResponseOut",
        "InsertTextRequestIn": "_slides_148_InsertTextRequestIn",
        "InsertTextRequestOut": "_slides_149_InsertTextRequestOut",
        "ShapeBackgroundFillIn": "_slides_150_ShapeBackgroundFillIn",
        "ShapeBackgroundFillOut": "_slides_151_ShapeBackgroundFillOut",
        "TableRowPropertiesIn": "_slides_152_TableRowPropertiesIn",
        "TableRowPropertiesOut": "_slides_153_TableRowPropertiesOut",
        "SolidFillIn": "_slides_154_SolidFillIn",
        "SolidFillOut": "_slides_155_SolidFillOut",
        "CreateImageRequestIn": "_slides_156_CreateImageRequestIn",
        "CreateImageRequestOut": "_slides_157_CreateImageRequestOut",
        "ParagraphMarkerIn": "_slides_158_ParagraphMarkerIn",
        "ParagraphMarkerOut": "_slides_159_ParagraphMarkerOut",
        "TableBorderRowIn": "_slides_160_TableBorderRowIn",
        "TableBorderRowOut": "_slides_161_TableBorderRowOut",
        "ResponseIn": "_slides_162_ResponseIn",
        "ResponseOut": "_slides_163_ResponseOut",
        "UpdateLinePropertiesRequestIn": "_slides_164_UpdateLinePropertiesRequestIn",
        "UpdateLinePropertiesRequestOut": "_slides_165_UpdateLinePropertiesRequestOut",
        "RangeIn": "_slides_166_RangeIn",
        "RangeOut": "_slides_167_RangeOut",
        "LayoutPropertiesIn": "_slides_168_LayoutPropertiesIn",
        "LayoutPropertiesOut": "_slides_169_LayoutPropertiesOut",
        "PageElementIn": "_slides_170_PageElementIn",
        "PageElementOut": "_slides_171_PageElementOut",
        "ShapePropertiesIn": "_slides_172_ShapePropertiesIn",
        "ShapePropertiesOut": "_slides_173_ShapePropertiesOut",
        "PageElementPropertiesIn": "_slides_174_PageElementPropertiesIn",
        "PageElementPropertiesOut": "_slides_175_PageElementPropertiesOut",
        "PresentationIn": "_slides_176_PresentationIn",
        "PresentationOut": "_slides_177_PresentationOut",
        "SubstringMatchCriteriaIn": "_slides_178_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_slides_179_SubstringMatchCriteriaOut",
        "UpdateTableColumnPropertiesRequestIn": "_slides_180_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_slides_181_UpdateTableColumnPropertiesRequestOut",
        "UpdateSlidePropertiesRequestIn": "_slides_182_UpdateSlidePropertiesRequestIn",
        "UpdateSlidePropertiesRequestOut": "_slides_183_UpdateSlidePropertiesRequestOut",
        "CreateTableRequestIn": "_slides_184_CreateTableRequestIn",
        "CreateTableRequestOut": "_slides_185_CreateTableRequestOut",
        "TextContentIn": "_slides_186_TextContentIn",
        "TextContentOut": "_slides_187_TextContentOut",
        "NestingLevelIn": "_slides_188_NestingLevelIn",
        "NestingLevelOut": "_slides_189_NestingLevelOut",
        "CreateLineResponseIn": "_slides_190_CreateLineResponseIn",
        "CreateLineResponseOut": "_slides_191_CreateLineResponseOut",
        "BatchUpdatePresentationRequestIn": "_slides_192_BatchUpdatePresentationRequestIn",
        "BatchUpdatePresentationRequestOut": "_slides_193_BatchUpdatePresentationRequestOut",
        "LineConnectionIn": "_slides_194_LineConnectionIn",
        "LineConnectionOut": "_slides_195_LineConnectionOut",
        "ShapeIn": "_slides_196_ShapeIn",
        "ShapeOut": "_slides_197_ShapeOut",
        "GroupObjectsResponseIn": "_slides_198_GroupObjectsResponseIn",
        "GroupObjectsResponseOut": "_slides_199_GroupObjectsResponseOut",
        "ShadowIn": "_slides_200_ShadowIn",
        "ShadowOut": "_slides_201_ShadowOut",
        "UpdateSlidesPositionRequestIn": "_slides_202_UpdateSlidesPositionRequestIn",
        "UpdateSlidesPositionRequestOut": "_slides_203_UpdateSlidesPositionRequestOut",
        "CreateParagraphBulletsRequestIn": "_slides_204_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_slides_205_CreateParagraphBulletsRequestOut",
        "CreateSheetsChartResponseIn": "_slides_206_CreateSheetsChartResponseIn",
        "CreateSheetsChartResponseOut": "_slides_207_CreateSheetsChartResponseOut",
        "ReplaceAllShapesWithSheetsChartResponseIn": "_slides_208_ReplaceAllShapesWithSheetsChartResponseIn",
        "ReplaceAllShapesWithSheetsChartResponseOut": "_slides_209_ReplaceAllShapesWithSheetsChartResponseOut",
        "ReplaceAllShapesWithSheetsChartRequestIn": "_slides_210_ReplaceAllShapesWithSheetsChartRequestIn",
        "ReplaceAllShapesWithSheetsChartRequestOut": "_slides_211_ReplaceAllShapesWithSheetsChartRequestOut",
        "DeleteObjectRequestIn": "_slides_212_DeleteObjectRequestIn",
        "DeleteObjectRequestOut": "_slides_213_DeleteObjectRequestOut",
        "MergeTableCellsRequestIn": "_slides_214_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_slides_215_MergeTableCellsRequestOut",
        "TableBorderCellIn": "_slides_216_TableBorderCellIn",
        "TableBorderCellOut": "_slides_217_TableBorderCellOut",
        "CreateVideoResponseIn": "_slides_218_CreateVideoResponseIn",
        "CreateVideoResponseOut": "_slides_219_CreateVideoResponseOut",
        "VideoIn": "_slides_220_VideoIn",
        "VideoOut": "_slides_221_VideoOut",
        "PageBackgroundFillIn": "_slides_222_PageBackgroundFillIn",
        "PageBackgroundFillOut": "_slides_223_PageBackgroundFillOut",
        "TableIn": "_slides_224_TableIn",
        "TableOut": "_slides_225_TableOut",
        "UpdateImagePropertiesRequestIn": "_slides_226_UpdateImagePropertiesRequestIn",
        "UpdateImagePropertiesRequestOut": "_slides_227_UpdateImagePropertiesRequestOut",
        "UpdatePageElementAltTextRequestIn": "_slides_228_UpdatePageElementAltTextRequestIn",
        "UpdatePageElementAltTextRequestOut": "_slides_229_UpdatePageElementAltTextRequestOut",
        "TextStyleIn": "_slides_230_TextStyleIn",
        "TextStyleOut": "_slides_231_TextStyleOut",
        "WeightedFontFamilyIn": "_slides_232_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_slides_233_WeightedFontFamilyOut",
        "UpdateShapePropertiesRequestIn": "_slides_234_UpdateShapePropertiesRequestIn",
        "UpdateShapePropertiesRequestOut": "_slides_235_UpdateShapePropertiesRequestOut",
        "UpdateLineCategoryRequestIn": "_slides_236_UpdateLineCategoryRequestIn",
        "UpdateLineCategoryRequestOut": "_slides_237_UpdateLineCategoryRequestOut",
        "VideoPropertiesIn": "_slides_238_VideoPropertiesIn",
        "VideoPropertiesOut": "_slides_239_VideoPropertiesOut",
        "ReplaceAllShapesWithImageRequestIn": "_slides_240_ReplaceAllShapesWithImageRequestIn",
        "ReplaceAllShapesWithImageRequestOut": "_slides_241_ReplaceAllShapesWithImageRequestOut",
        "MasterPropertiesIn": "_slides_242_MasterPropertiesIn",
        "MasterPropertiesOut": "_slides_243_MasterPropertiesOut",
        "RecolorIn": "_slides_244_RecolorIn",
        "RecolorOut": "_slides_245_RecolorOut",
        "ThemeColorPairIn": "_slides_246_ThemeColorPairIn",
        "ThemeColorPairOut": "_slides_247_ThemeColorPairOut",
        "DimensionIn": "_slides_248_DimensionIn",
        "DimensionOut": "_slides_249_DimensionOut",
        "WordArtIn": "_slides_250_WordArtIn",
        "WordArtOut": "_slides_251_WordArtOut",
        "SheetsChartPropertiesIn": "_slides_252_SheetsChartPropertiesIn",
        "SheetsChartPropertiesOut": "_slides_253_SheetsChartPropertiesOut",
        "AutoTextIn": "_slides_254_AutoTextIn",
        "AutoTextOut": "_slides_255_AutoTextOut",
        "GroupObjectsRequestIn": "_slides_256_GroupObjectsRequestIn",
        "GroupObjectsRequestOut": "_slides_257_GroupObjectsRequestOut",
        "ReplaceAllShapesWithImageResponseIn": "_slides_258_ReplaceAllShapesWithImageResponseIn",
        "ReplaceAllShapesWithImageResponseOut": "_slides_259_ReplaceAllShapesWithImageResponseOut",
        "DeleteTextRequestIn": "_slides_260_DeleteTextRequestIn",
        "DeleteTextRequestOut": "_slides_261_DeleteTextRequestOut",
        "UpdateParagraphStyleRequestIn": "_slides_262_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_slides_263_UpdateParagraphStyleRequestOut",
        "CreateSlideRequestIn": "_slides_264_CreateSlideRequestIn",
        "CreateSlideRequestOut": "_slides_265_CreateSlideRequestOut",
        "StretchedPictureFillIn": "_slides_266_StretchedPictureFillIn",
        "StretchedPictureFillOut": "_slides_267_StretchedPictureFillOut",
        "RefreshSheetsChartRequestIn": "_slides_268_RefreshSheetsChartRequestIn",
        "RefreshSheetsChartRequestOut": "_slides_269_RefreshSheetsChartRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["WriteControlIn"] = t.struct(
        {"requiredRevisionId": t.string().optional()}
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
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
    types["RequestIn"] = t.struct(
        {
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestIn"]
            ).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestIn"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestIn"]).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestIn"]
            ).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestIn"]).optional(),
            "createLine": t.proxy(renames["CreateLineRequestIn"]).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestIn"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestIn"]
            ).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestIn"]).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestIn"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestIn"]).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestIn"]
            ).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestIn"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestIn"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestIn"]
            ).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestIn"]
            ).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestIn"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestIn"]).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestIn"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestIn"]).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestIn"]
            ).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestIn"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestIn"]
            ).optional(),
            "createTable": t.proxy(renames["CreateTableRequestIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestIn"]).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestIn"]
            ).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestIn"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestIn"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestIn"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestIn"]
            ).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestIn"]).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestOut"]
            ).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestOut"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestOut"]).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestOut"]
            ).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestOut"]).optional(),
            "createLine": t.proxy(renames["CreateLineRequestOut"]).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestOut"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestOut"]
            ).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestOut"]).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestOut"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestOut"]).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestOut"]
            ).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestOut"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestOut"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestOut"]
            ).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestOut"]
            ).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestOut"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestOut"]).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestOut"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestOut"]).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestOut"]
            ).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestOut"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestOut"]
            ).optional(),
            "createTable": t.proxy(renames["CreateTableRequestOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestOut"]).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestOut"]
            ).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestOut"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestOut"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestOut"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestOut"]
            ).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestOut"]).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["TableRangeIn"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
    types["PlaceholderIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "parentObjectId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PlaceholderIn"])
    types["PlaceholderOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "parentObjectId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceholderOut"])
    types["UpdatePagePropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestIn"])
    types["UpdatePagePropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestOut"])
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
    types["LineIn"] = t.struct(
        {
            "lineCategory": t.string().optional(),
            "lineType": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesIn"]).optional(),
        }
    ).named(renames["LineIn"])
    types["LineOut"] = t.struct(
        {
            "lineCategory": t.string().optional(),
            "lineType": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineOut"])
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
    types["DuplicateObjectResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DuplicateObjectResponseIn"])
    types["DuplicateObjectResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateObjectResponseOut"])
    types["CreateShapeResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateShapeResponseIn"])
    types["CreateShapeResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeResponseOut"])
    types["CreateImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateImageResponseIn"])
    types["CreateImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageResponseOut"])
    types["CreateTableResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateTableResponseIn"])
    types["CreateTableResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableResponseOut"])
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
    types["UpdateTableRowPropertiesRequestIn"] = t.struct(
        {
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestIn"])
    types["UpdateTableRowPropertiesRequestOut"] = t.struct(
        {
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestOut"])
    types["UpdateTableBorderPropertiesRequestIn"] = t.struct(
        {
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesIn"]
            ).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "borderPosition": t.string().optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestIn"])
    types["UpdateTableBorderPropertiesRequestOut"] = t.struct(
        {
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesOut"]
            ).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "borderPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestOut"])
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
    types["CreateSheetsChartRequestIn"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "spreadsheetId": t.string().optional(),
            "linkingMode": t.string().optional(),
        }
    ).named(renames["CreateSheetsChartRequestIn"])
    types["CreateSheetsChartRequestOut"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "spreadsheetId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartRequestOut"])
    types["UngroupObjectsRequestIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["UngroupObjectsRequestIn"])
    types["UngroupObjectsRequestOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UngroupObjectsRequestOut"])
    types["LineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["LineFillIn"])
    types["LineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineFillOut"])
    types["TextElementIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "paragraphMarker": t.proxy(renames["ParagraphMarkerIn"]).optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "endIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
        }
    ).named(renames["TextElementIn"])
    types["TextElementOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "paragraphMarker": t.proxy(renames["ParagraphMarkerOut"]).optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "endIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextElementOut"])
    types["UpdateTableCellPropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "fields": t.string().optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestIn"])
    types["UpdateTableCellPropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "fields": t.string().optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestOut"])
    types["CreateLineRequestIn"] = t.struct(
        {
            "category": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "lineCategory": t.string().optional(),
        }
    ).named(renames["CreateLineRequestIn"])
    types["CreateLineRequestOut"] = t.struct(
        {
            "category": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "lineCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineRequestOut"])
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
    types["AffineTransformIn"] = t.struct(
        {
            "scaleY": t.number().optional(),
            "translateY": t.number().optional(),
            "shearY": t.number().optional(),
            "unit": t.string().optional(),
            "translateX": t.number().optional(),
            "scaleX": t.number().optional(),
            "shearX": t.number().optional(),
        }
    ).named(renames["AffineTransformIn"])
    types["AffineTransformOut"] = t.struct(
        {
            "scaleY": t.number().optional(),
            "translateY": t.number().optional(),
            "shearY": t.number().optional(),
            "unit": t.string().optional(),
            "translateX": t.number().optional(),
            "scaleX": t.number().optional(),
            "shearX": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AffineTransformOut"])
    types["LinePropertiesIn"] = t.struct(
        {
            "startArrow": t.string().optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "lineFill": t.proxy(renames["LineFillIn"]).optional(),
            "startConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "dashStyle": t.string().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "endArrow": t.string().optional(),
        }
    ).named(renames["LinePropertiesIn"])
    types["LinePropertiesOut"] = t.struct(
        {
            "startArrow": t.string().optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "lineFill": t.proxy(renames["LineFillOut"]).optional(),
            "startConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "endArrow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinePropertiesOut"])
    types["UnmergeTableCellsRequestIn"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UnmergeTableCellsRequestIn"])
    types["UnmergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeTableCellsRequestOut"])
    types["TableRowIn"] = t.struct(
        {
            "tableCells": t.array(t.proxy(renames["TableCellIn"])).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
            "rowHeight": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "tableCells": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "rowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["NotesPropertiesIn"] = t.struct(
        {"speakerNotesObjectId": t.string().optional()}
    ).named(renames["NotesPropertiesIn"])
    types["NotesPropertiesOut"] = t.struct(
        {
            "speakerNotesObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotesPropertiesOut"])
    types["OutlineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["OutlineFillIn"])
    types["OutlineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineFillOut"])
    types["TableCellPropertiesIn"] = t.struct(
        {
            "tableCellBackgroundFill": t.proxy(
                renames["TableCellBackgroundFillIn"]
            ).optional(),
            "contentAlignment": t.string().optional(),
        }
    ).named(renames["TableCellPropertiesIn"])
    types["TableCellPropertiesOut"] = t.struct(
        {
            "tableCellBackgroundFill": t.proxy(
                renames["TableCellBackgroundFillOut"]
            ).optional(),
            "contentAlignment": t.string().optional(),
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
    types["InsertTableColumnsRequestIn"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "number": t.integer().optional(),
            "insertRight": t.boolean().optional(),
        }
    ).named(renames["InsertTableColumnsRequestIn"])
    types["InsertTableColumnsRequestOut"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "number": t.integer().optional(),
            "insertRight": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableColumnsRequestOut"])
    types["InsertTableRowsRequestIn"] = t.struct(
        {
            "insertBelow": t.boolean().optional(),
            "tableObjectId": t.string().optional(),
            "number": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["InsertTableRowsRequestIn"])
    types["InsertTableRowsRequestOut"] = t.struct(
        {
            "insertBelow": t.boolean().optional(),
            "tableObjectId": t.string().optional(),
            "number": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRowsRequestOut"])
    types["CreateVideoRequestIn"] = t.struct(
        {
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "id": t.string().optional(),
            "source": t.string().optional(),
        }
    ).named(renames["CreateVideoRequestIn"])
    types["CreateVideoRequestOut"] = t.struct(
        {
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "id": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoRequestOut"])
    types["LinkIn"] = t.struct(
        {
            "pageObjectId": t.string().optional(),
            "relativeLink": t.string().optional(),
            "slideIndex": t.integer().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "pageObjectId": t.string().optional(),
            "relativeLink": t.string().optional(),
            "slideIndex": t.integer().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
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
    types["ColorSchemeIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ThemeColorPairIn"])).optional()}
    ).named(renames["ColorSchemeIn"])
    types["ColorSchemeOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ThemeColorPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorSchemeOut"])
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
    types["RerouteLineRequestIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["RerouteLineRequestIn"]
    )
    types["RerouteLineRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RerouteLineRequestOut"])
    types["TableCellIn"] = t.struct(
        {
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
            "columnSpan": t.integer().optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "columnSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
    types["TableBorderFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["TableBorderFillIn"])
    types["TableBorderFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderFillOut"])
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
    types["CreateSlideResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSlideResponseIn"])
    types["CreateSlideResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideResponseOut"])
    types["PageIn"] = t.struct(
        {
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "pageElements": t.array(t.proxy(renames["PageElementIn"])).optional(),
            "objectId": t.string().optional(),
            "revisionId": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesIn"]).optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesIn"]).optional(),
            "pageType": t.string().optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesIn"]).optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "pageElements": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "objectId": t.string().optional(),
            "revisionId": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesOut"]).optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesOut"]).optional(),
            "pageType": t.string().optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "spacingMode": t.string().optional(),
            "direction": t.string().optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "lineSpacing": t.number().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "alignment": t.string().optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "spacingMode": t.string().optional(),
            "direction": t.string().optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "lineSpacing": t.number().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "alignment": t.string().optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
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
    types["TableColumnPropertiesIn"] = t.struct(
        {"columnWidth": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableColumnPropertiesIn"])
    types["TableColumnPropertiesOut"] = t.struct(
        {
            "columnWidth": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableColumnPropertiesOut"])
    types["BulletIn"] = t.struct(
        {
            "listId": t.string().optional(),
            "nestingLevel": t.integer().optional(),
            "bulletStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "glyph": t.string().optional(),
        }
    ).named(renames["BulletIn"])
    types["BulletOut"] = t.struct(
        {
            "listId": t.string().optional(),
            "nestingLevel": t.integer().optional(),
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "glyph": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletOut"])
    types["ColorStopIn"] = t.struct(
        {
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "alpha": t.number().optional(),
            "position": t.number().optional(),
        }
    ).named(renames["ColorStopIn"])
    types["ColorStopOut"] = t.struct(
        {
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "alpha": t.number().optional(),
            "position": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorStopOut"])
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
    types["SlidePropertiesIn"] = t.struct(
        {
            "isSkipped": t.boolean().optional(),
            "layoutObjectId": t.string().optional(),
            "notesPage": t.proxy(renames["PageIn"]).optional(),
            "masterObjectId": t.string().optional(),
        }
    ).named(renames["SlidePropertiesIn"])
    types["SlidePropertiesOut"] = t.struct(
        {
            "isSkipped": t.boolean().optional(),
            "layoutObjectId": t.string().optional(),
            "notesPage": t.proxy(renames["PageOut"]).optional(),
            "masterObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlidePropertiesOut"])
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
    types["CropPropertiesIn"] = t.struct(
        {
            "leftOffset": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "topOffset": t.number().optional(),
            "rightOffset": t.number().optional(),
            "angle": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "leftOffset": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "topOffset": t.number().optional(),
            "rightOffset": t.number().optional(),
            "angle": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
    types["ReplaceImageRequestIn"] = t.struct(
        {
            "url": t.string().optional(),
            "imageObjectId": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
        }
    ).named(renames["ReplaceImageRequestIn"])
    types["ReplaceImageRequestOut"] = t.struct(
        {
            "url": t.string().optional(),
            "imageObjectId": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceImageRequestOut"])
    types["DeleteTableColumnRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "tableObjectId": t.string().optional(),
        }
    ).named(renames["DeleteTableColumnRequestIn"])
    types["DeleteTableColumnRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "tableObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableColumnRequestOut"])
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
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "fields": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "fields": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
    types["SheetsChartIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "chartId": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesIn"]
            ).optional(),
        }
    ).named(renames["SheetsChartIn"])
    types["SheetsChartOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "chartId": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartOut"])
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
    types["ImageIn"] = t.struct(
        {
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "contentUrl": t.string().optional(),
            "sourceUrl": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "contentUrl": t.string().optional(),
            "sourceUrl": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
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
    types["ImagePropertiesIn"] = t.struct(
        {
            "contrast": t.number().optional(),
            "recolor": t.proxy(renames["RecolorIn"]).optional(),
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "transparency": t.number().optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
            "brightness": t.number().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "contrast": t.number().optional(),
            "recolor": t.proxy(renames["RecolorOut"]).optional(),
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "transparency": t.number().optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "brightness": t.number().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["OptionalColorIn"] = t.struct(
        {"opaqueColor": t.proxy(renames["OpaqueColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "opaqueColor": t.proxy(renames["OpaqueColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
    types["InsertTextRequestIn"] = t.struct(
        {
            "text": t.string().optional(),
            "insertionIndex": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "text": t.string().optional(),
            "insertionIndex": t.integer().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
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
    types["TableRowPropertiesIn"] = t.struct(
        {"minRowHeight": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableRowPropertiesIn"])
    types["TableRowPropertiesOut"] = t.struct(
        {
            "minRowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowPropertiesOut"])
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
    types["ResponseIn"] = t.struct(
        {
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseIn"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectResponseIn"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseIn"]).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseIn"]).optional(),
            "createTable": t.proxy(renames["CreateTableResponseIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseIn"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseIn"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineResponseIn"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseIn"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseIn"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseIn"]).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseOut"]
            ).optional(),
            "duplicateObject": t.proxy(
                renames["DuplicateObjectResponseOut"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseOut"]).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseOut"]).optional(),
            "createTable": t.proxy(renames["CreateTableResponseOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseOut"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseOut"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineResponseOut"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseOut"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseOut"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
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
    types["LayoutPropertiesIn"] = t.struct(
        {
            "masterObjectId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LayoutPropertiesIn"])
    types["LayoutPropertiesOut"] = t.struct(
        {
            "masterObjectId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutPropertiesOut"])
    types["PageElementIn"] = t.struct(
        {
            "table": t.proxy(renames["TableIn"]).optional(),
            "sheetsChart": t.proxy(renames["SheetsChartIn"]).optional(),
            "shape": t.proxy(renames["ShapeIn"]).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "description": t.string().optional(),
            "elementGroup": t.proxy(renames["GroupIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "objectId": t.string().optional(),
            "line": t.proxy(renames["LineIn"]).optional(),
            "title": t.string().optional(),
            "wordArt": t.proxy(renames["WordArtIn"]).optional(),
            "video": t.proxy(renames["VideoIn"]).optional(),
        }
    ).named(renames["PageElementIn"])
    types["PageElementOut"] = t.struct(
        {
            "table": t.proxy(renames["TableOut"]).optional(),
            "sheetsChart": t.proxy(renames["SheetsChartOut"]).optional(),
            "shape": t.proxy(renames["ShapeOut"]).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "description": t.string().optional(),
            "elementGroup": t.proxy(renames["GroupOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "objectId": t.string().optional(),
            "line": t.proxy(renames["LineOut"]).optional(),
            "title": t.string().optional(),
            "wordArt": t.proxy(renames["WordArtOut"]).optional(),
            "video": t.proxy(renames["VideoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementOut"])
    types["ShapePropertiesIn"] = t.struct(
        {
            "link": t.proxy(renames["LinkIn"]).optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "shapeBackgroundFill": t.proxy(renames["ShapeBackgroundFillIn"]).optional(),
            "autofit": t.proxy(renames["AutofitIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
            "contentAlignment": t.string().optional(),
        }
    ).named(renames["ShapePropertiesIn"])
    types["ShapePropertiesOut"] = t.struct(
        {
            "link": t.proxy(renames["LinkOut"]).optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "shapeBackgroundFill": t.proxy(
                renames["ShapeBackgroundFillOut"]
            ).optional(),
            "autofit": t.proxy(renames["AutofitOut"]).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "contentAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapePropertiesOut"])
    types["PageElementPropertiesIn"] = t.struct(
        {
            "size": t.proxy(renames["SizeIn"]).optional(),
            "pageObjectId": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
        }
    ).named(renames["PageElementPropertiesIn"])
    types["PageElementPropertiesOut"] = t.struct(
        {
            "size": t.proxy(renames["SizeOut"]).optional(),
            "pageObjectId": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementPropertiesOut"])
    types["PresentationIn"] = t.struct(
        {
            "title": t.string().optional(),
            "notesMaster": t.proxy(renames["PageIn"]).optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "presentationId": t.string().optional(),
            "masters": t.array(t.proxy(renames["PageIn"])).optional(),
            "locale": t.string().optional(),
            "slides": t.array(t.proxy(renames["PageIn"])).optional(),
            "revisionId": t.string().optional(),
            "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
        }
    ).named(renames["PresentationIn"])
    types["PresentationOut"] = t.struct(
        {
            "title": t.string().optional(),
            "notesMaster": t.proxy(renames["PageOut"]).optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "presentationId": t.string().optional(),
            "masters": t.array(t.proxy(renames["PageOut"])).optional(),
            "locale": t.string().optional(),
            "slides": t.array(t.proxy(renames["PageOut"])).optional(),
            "revisionId": t.string().optional(),
            "layouts": t.array(t.proxy(renames["PageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationOut"])
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
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
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
    types["CreateTableRequestIn"] = t.struct(
        {
            "rows": t.integer().optional(),
            "columns": t.integer().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["CreateTableRequestIn"])
    types["CreateTableRequestOut"] = t.struct(
        {
            "rows": t.integer().optional(),
            "columns": t.integer().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableRequestOut"])
    types["TextContentIn"] = t.struct(
        {
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "textElements": t.array(t.proxy(renames["TextElementIn"])).optional(),
        }
    ).named(renames["TextContentIn"])
    types["TextContentOut"] = t.struct(
        {
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "textElements": t.array(t.proxy(renames["TextElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextContentOut"])
    types["NestingLevelIn"] = t.struct(
        {"bulletStyle": t.proxy(renames["TextStyleIn"]).optional()}
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
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
    types["ShapeIn"] = t.struct(
        {
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "shapeType": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesIn"]).optional(),
        }
    ).named(renames["ShapeIn"])
    types["ShapeOut"] = t.struct(
        {
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "shapeType": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapeOut"])
    types["GroupObjectsResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["GroupObjectsResponseIn"])
    types["GroupObjectsResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupObjectsResponseOut"])
    types["ShadowIn"] = t.struct(
        {
            "blurRadius": t.proxy(renames["DimensionIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "propertyState": t.string().optional(),
            "alpha": t.number().optional(),
            "rotateWithShape": t.boolean().optional(),
            "type": t.string().optional(),
            "alignment": t.string().optional(),
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
        }
    ).named(renames["ShadowIn"])
    types["ShadowOut"] = t.struct(
        {
            "blurRadius": t.proxy(renames["DimensionOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "propertyState": t.string().optional(),
            "alpha": t.number().optional(),
            "rotateWithShape": t.boolean().optional(),
            "type": t.string().optional(),
            "alignment": t.string().optional(),
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadowOut"])
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
    types["CreateParagraphBulletsRequestIn"] = t.struct(
        {
            "bulletPreset": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestIn"])
    types["CreateParagraphBulletsRequestOut"] = t.struct(
        {
            "bulletPreset": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestOut"])
    types["CreateSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSheetsChartResponseIn"])
    types["CreateSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartResponseOut"])
    types["ReplaceAllShapesWithSheetsChartResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseIn"])
    types["ReplaceAllShapesWithSheetsChartResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseOut"])
    types["ReplaceAllShapesWithSheetsChartRequestIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "chartId": t.integer().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "linkingMode": t.string().optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestIn"])
    types["ReplaceAllShapesWithSheetsChartRequestOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "chartId": t.integer().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "linkingMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestOut"])
    types["DeleteObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeleteObjectRequestIn"])
    types["DeleteObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteObjectRequestOut"])
    types["MergeTableCellsRequestIn"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["MergeTableCellsRequestIn"])
    types["MergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeTableCellsRequestOut"])
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
    types["CreateVideoResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateVideoResponseIn"])
    types["CreateVideoResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoResponseOut"])
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
    types["PageBackgroundFillIn"] = t.struct(
        {
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillIn"]
            ).optional(),
            "propertyState": t.string().optional(),
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
        }
    ).named(renames["PageBackgroundFillIn"])
    types["PageBackgroundFillOut"] = t.struct(
        {
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillOut"]
            ).optional(),
            "propertyState": t.string().optional(),
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBackgroundFillOut"])
    types["TableIn"] = t.struct(
        {
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "columns": t.integer().optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesIn"])
            ).optional(),
            "rows": t.integer().optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "columns": t.integer().optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesOut"])
            ).optional(),
            "rows": t.integer().optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["UpdateImagePropertiesRequestIn"] = t.struct(
        {
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateImagePropertiesRequestIn"])
    types["UpdateImagePropertiesRequestOut"] = t.struct(
        {
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateImagePropertiesRequestOut"])
    types["UpdatePageElementAltTextRequestIn"] = t.struct(
        {
            "title": t.string().optional(),
            "objectId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["UpdatePageElementAltTextRequestIn"])
    types["UpdatePageElementAltTextRequestOut"] = t.struct(
        {
            "title": t.string().optional(),
            "objectId": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementAltTextRequestOut"])
    types["TextStyleIn"] = t.struct(
        {
            "underline": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "fontFamily": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "italic": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "strikethrough": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "bold": t.boolean().optional(),
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "underline": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "fontFamily": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "italic": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "strikethrough": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "bold": t.boolean().optional(),
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
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
    types["VideoPropertiesIn"] = t.struct(
        {
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "autoPlay": t.boolean().optional(),
            "mute": t.boolean().optional(),
            "end": t.integer().optional(),
            "start": t.integer().optional(),
        }
    ).named(renames["VideoPropertiesIn"])
    types["VideoPropertiesOut"] = t.struct(
        {
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "autoPlay": t.boolean().optional(),
            "mute": t.boolean().optional(),
            "end": t.integer().optional(),
            "start": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPropertiesOut"])
    types["ReplaceAllShapesWithImageRequestIn"] = t.struct(
        {
            "pageObjectIds": t.array(t.string()).optional(),
            "replaceMethod": t.string().optional(),
            "imageUrl": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestIn"])
    types["ReplaceAllShapesWithImageRequestOut"] = t.struct(
        {
            "pageObjectIds": t.array(t.string()).optional(),
            "replaceMethod": t.string().optional(),
            "imageUrl": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestOut"])
    types["MasterPropertiesIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["MasterPropertiesIn"])
    types["MasterPropertiesOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterPropertiesOut"])
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
    types["WordArtIn"] = t.struct({"renderedText": t.string().optional()}).named(
        renames["WordArtIn"]
    )
    types["WordArtOut"] = t.struct(
        {
            "renderedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordArtOut"])
    types["SheetsChartPropertiesIn"] = t.struct(
        {"chartImageProperties": t.proxy(renames["ImagePropertiesIn"]).optional()}
    ).named(renames["SheetsChartPropertiesIn"])
    types["SheetsChartPropertiesOut"] = t.struct(
        {
            "chartImageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartPropertiesOut"])
    types["AutoTextIn"] = t.struct(
        {
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "content": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "content": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
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
    types["ReplaceAllShapesWithImageResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithImageResponseIn"])
    types["ReplaceAllShapesWithImageResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageResponseOut"])
    types["DeleteTextRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["DeleteTextRequestIn"])
    types["DeleteTextRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTextRequestOut"])
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "style": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "style": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])
    types["CreateSlideRequestIn"] = t.struct(
        {
            "slideLayoutReference": t.proxy(renames["LayoutReferenceIn"]).optional(),
            "insertionIndex": t.integer().optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingIn"])
            ).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["CreateSlideRequestIn"])
    types["CreateSlideRequestOut"] = t.struct(
        {
            "slideLayoutReference": t.proxy(renames["LayoutReferenceOut"]).optional(),
            "insertionIndex": t.integer().optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingOut"])
            ).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideRequestOut"])
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
    types["RefreshSheetsChartRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["RefreshSheetsChartRequestIn"])
    types["RefreshSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshSheetsChartRequestOut"])

    functions = {}
    functions["presentationsBatchUpdate"] = slides.post(
        "v1/presentations",
        t.struct(
            {
                "title": t.string().optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "presentationId": t.string().optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "locale": t.string().optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "revisionId": t.string().optional(),
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsGet"] = slides.post(
        "v1/presentations",
        t.struct(
            {
                "title": t.string().optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "presentationId": t.string().optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "locale": t.string().optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "revisionId": t.string().optional(),
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
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
                "title": t.string().optional(),
                "notesMaster": t.proxy(renames["PageIn"]).optional(),
                "pageSize": t.proxy(renames["SizeIn"]).optional(),
                "presentationId": t.string().optional(),
                "masters": t.array(t.proxy(renames["PageIn"])).optional(),
                "locale": t.string().optional(),
                "slides": t.array(t.proxy(renames["PageIn"])).optional(),
                "revisionId": t.string().optional(),
                "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
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
                "pageObjectId": t.string().optional(),
                "presentationId": t.string().optional(),
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
                "pageObjectId": t.string().optional(),
                "presentationId": t.string().optional(),
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
