from typegraph import effects
from typegraph import t
from typegraph.importers.base.importer import Import
from typegraph import TypeGraph
from typegraph.runtimes.http import HTTPRuntime


def import_docs() -> Import:
    docs = HTTPRuntime("https://slides.googleapis.com/")

    renames = {
        "ErrorResponse": "_docs_1_ErrorResponse",
        "ReplaceAllTextResponseIn": "_docs_2_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_docs_3_ReplaceAllTextResponseOut",
        "RequestIn": "_docs_4_RequestIn",
        "RequestOut": "_docs_5_RequestOut",
        "ParagraphStyleIn": "_docs_6_ParagraphStyleIn",
        "ParagraphStyleOut": "_docs_7_ParagraphStyleOut",
        "BatchUpdatePresentationResponseIn": "_docs_8_BatchUpdatePresentationResponseIn",
        "BatchUpdatePresentationResponseOut": "_docs_9_BatchUpdatePresentationResponseOut",
        "InsertTableRowsRequestIn": "_docs_10_InsertTableRowsRequestIn",
        "InsertTableRowsRequestOut": "_docs_11_InsertTableRowsRequestOut",
        "ResponseIn": "_docs_12_ResponseIn",
        "ResponseOut": "_docs_13_ResponseOut",
        "UpdatePageElementsZOrderRequestIn": "_docs_14_UpdatePageElementsZOrderRequestIn",
        "UpdatePageElementsZOrderRequestOut": "_docs_15_UpdatePageElementsZOrderRequestOut",
        "OptionalColorIn": "_docs_16_OptionalColorIn",
        "OptionalColorOut": "_docs_17_OptionalColorOut",
        "LayoutPropertiesIn": "_docs_18_LayoutPropertiesIn",
        "LayoutPropertiesOut": "_docs_19_LayoutPropertiesOut",
        "UpdateTableRowPropertiesRequestIn": "_docs_20_UpdateTableRowPropertiesRequestIn",
        "UpdateTableRowPropertiesRequestOut": "_docs_21_UpdateTableRowPropertiesRequestOut",
        "ShapeBackgroundFillIn": "_docs_22_ShapeBackgroundFillIn",
        "ShapeBackgroundFillOut": "_docs_23_ShapeBackgroundFillOut",
        "AutoTextIn": "_docs_24_AutoTextIn",
        "AutoTextOut": "_docs_25_AutoTextOut",
        "LineConnectionIn": "_docs_26_LineConnectionIn",
        "LineConnectionOut": "_docs_27_LineConnectionOut",
        "TextElementIn": "_docs_28_TextElementIn",
        "TextElementOut": "_docs_29_TextElementOut",
        "SheetsChartIn": "_docs_30_SheetsChartIn",
        "SheetsChartOut": "_docs_31_SheetsChartOut",
        "GroupObjectsResponseIn": "_docs_32_GroupObjectsResponseIn",
        "GroupObjectsResponseOut": "_docs_33_GroupObjectsResponseOut",
        "MasterPropertiesIn": "_docs_34_MasterPropertiesIn",
        "MasterPropertiesOut": "_docs_35_MasterPropertiesOut",
        "ReplaceAllShapesWithImageResponseIn": "_docs_36_ReplaceAllShapesWithImageResponseIn",
        "ReplaceAllShapesWithImageResponseOut": "_docs_37_ReplaceAllShapesWithImageResponseOut",
        "UpdateLinePropertiesRequestIn": "_docs_38_UpdateLinePropertiesRequestIn",
        "UpdateLinePropertiesRequestOut": "_docs_39_UpdateLinePropertiesRequestOut",
        "UpdateTableCellPropertiesRequestIn": "_docs_40_UpdateTableCellPropertiesRequestIn",
        "UpdateTableCellPropertiesRequestOut": "_docs_41_UpdateTableCellPropertiesRequestOut",
        "AffineTransformIn": "_docs_42_AffineTransformIn",
        "AffineTransformOut": "_docs_43_AffineTransformOut",
        "UpdateSlidePropertiesRequestIn": "_docs_44_UpdateSlidePropertiesRequestIn",
        "UpdateSlidePropertiesRequestOut": "_docs_45_UpdateSlidePropertiesRequestOut",
        "GroupIn": "_docs_46_GroupIn",
        "GroupOut": "_docs_47_GroupOut",
        "PagePropertiesIn": "_docs_48_PagePropertiesIn",
        "PagePropertiesOut": "_docs_49_PagePropertiesOut",
        "ShapeIn": "_docs_50_ShapeIn",
        "ShapeOut": "_docs_51_ShapeOut",
        "CreateSlideResponseIn": "_docs_52_CreateSlideResponseIn",
        "CreateSlideResponseOut": "_docs_53_CreateSlideResponseOut",
        "CreateParagraphBulletsRequestIn": "_docs_54_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_docs_55_CreateParagraphBulletsRequestOut",
        "TableColumnPropertiesIn": "_docs_56_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_docs_57_TableColumnPropertiesOut",
        "TextStyleIn": "_docs_58_TextStyleIn",
        "TextStyleOut": "_docs_59_TextStyleOut",
        "SizeIn": "_docs_60_SizeIn",
        "SizeOut": "_docs_61_SizeOut",
        "NotesPropertiesIn": "_docs_62_NotesPropertiesIn",
        "NotesPropertiesOut": "_docs_63_NotesPropertiesOut",
        "CreateTableRequestIn": "_docs_64_CreateTableRequestIn",
        "CreateTableRequestOut": "_docs_65_CreateTableRequestOut",
        "WordArtIn": "_docs_66_WordArtIn",
        "WordArtOut": "_docs_67_WordArtOut",
        "TableCellPropertiesIn": "_docs_68_TableCellPropertiesIn",
        "TableCellPropertiesOut": "_docs_69_TableCellPropertiesOut",
        "CreateVideoRequestIn": "_docs_70_CreateVideoRequestIn",
        "CreateVideoRequestOut": "_docs_71_CreateVideoRequestOut",
        "ThumbnailIn": "_docs_72_ThumbnailIn",
        "ThumbnailOut": "_docs_73_ThumbnailOut",
        "SheetsChartPropertiesIn": "_docs_74_SheetsChartPropertiesIn",
        "SheetsChartPropertiesOut": "_docs_75_SheetsChartPropertiesOut",
        "OutlineIn": "_docs_76_OutlineIn",
        "OutlineOut": "_docs_77_OutlineOut",
        "ShadowIn": "_docs_78_ShadowIn",
        "ShadowOut": "_docs_79_ShadowOut",
        "LinkIn": "_docs_80_LinkIn",
        "LinkOut": "_docs_81_LinkOut",
        "UpdatePageElementAltTextRequestIn": "_docs_82_UpdatePageElementAltTextRequestIn",
        "UpdatePageElementAltTextRequestOut": "_docs_83_UpdatePageElementAltTextRequestOut",
        "TableCellBackgroundFillIn": "_docs_84_TableCellBackgroundFillIn",
        "TableCellBackgroundFillOut": "_docs_85_TableCellBackgroundFillOut",
        "UpdateTableColumnPropertiesRequestIn": "_docs_86_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_docs_87_UpdateTableColumnPropertiesRequestOut",
        "UpdatePageElementTransformRequestIn": "_docs_88_UpdatePageElementTransformRequestIn",
        "UpdatePageElementTransformRequestOut": "_docs_89_UpdatePageElementTransformRequestOut",
        "InsertTextRequestIn": "_docs_90_InsertTextRequestIn",
        "InsertTextRequestOut": "_docs_91_InsertTextRequestOut",
        "TableRowPropertiesIn": "_docs_92_TableRowPropertiesIn",
        "TableRowPropertiesOut": "_docs_93_TableRowPropertiesOut",
        "TableRangeIn": "_docs_94_TableRangeIn",
        "TableRangeOut": "_docs_95_TableRangeOut",
        "CreateImageResponseIn": "_docs_96_CreateImageResponseIn",
        "CreateImageResponseOut": "_docs_97_CreateImageResponseOut",
        "TableBorderRowIn": "_docs_98_TableBorderRowIn",
        "TableBorderRowOut": "_docs_99_TableBorderRowOut",
        "BulletIn": "_docs_100_BulletIn",
        "BulletOut": "_docs_101_BulletOut",
        "CreateSlideRequestIn": "_docs_102_CreateSlideRequestIn",
        "CreateSlideRequestOut": "_docs_103_CreateSlideRequestOut",
        "AutofitIn": "_docs_104_AutofitIn",
        "AutofitOut": "_docs_105_AutofitOut",
        "UngroupObjectsRequestIn": "_docs_106_UngroupObjectsRequestIn",
        "UngroupObjectsRequestOut": "_docs_107_UngroupObjectsRequestOut",
        "CreateLineResponseIn": "_docs_108_CreateLineResponseIn",
        "CreateLineResponseOut": "_docs_109_CreateLineResponseOut",
        "ListIn": "_docs_110_ListIn",
        "ListOut": "_docs_111_ListOut",
        "CreateShapeResponseIn": "_docs_112_CreateShapeResponseIn",
        "CreateShapeResponseOut": "_docs_113_CreateShapeResponseOut",
        "LinePropertiesIn": "_docs_114_LinePropertiesIn",
        "LinePropertiesOut": "_docs_115_LinePropertiesOut",
        "CreateSheetsChartResponseIn": "_docs_116_CreateSheetsChartResponseIn",
        "CreateSheetsChartResponseOut": "_docs_117_CreateSheetsChartResponseOut",
        "ParagraphMarkerIn": "_docs_118_ParagraphMarkerIn",
        "ParagraphMarkerOut": "_docs_119_ParagraphMarkerOut",
        "PageIn": "_docs_120_PageIn",
        "PageOut": "_docs_121_PageOut",
        "ReplaceAllShapesWithSheetsChartRequestIn": "_docs_122_ReplaceAllShapesWithSheetsChartRequestIn",
        "ReplaceAllShapesWithSheetsChartRequestOut": "_docs_123_ReplaceAllShapesWithSheetsChartRequestOut",
        "LineFillIn": "_docs_124_LineFillIn",
        "LineFillOut": "_docs_125_LineFillOut",
        "UpdateImagePropertiesRequestIn": "_docs_126_UpdateImagePropertiesRequestIn",
        "UpdateImagePropertiesRequestOut": "_docs_127_UpdateImagePropertiesRequestOut",
        "InsertTableColumnsRequestIn": "_docs_128_InsertTableColumnsRequestIn",
        "InsertTableColumnsRequestOut": "_docs_129_InsertTableColumnsRequestOut",
        "ReplaceAllTextRequestIn": "_docs_130_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_docs_131_ReplaceAllTextRequestOut",
        "PageElementIn": "_docs_132_PageElementIn",
        "PageElementOut": "_docs_133_PageElementOut",
        "LayoutPlaceholderIdMappingIn": "_docs_134_LayoutPlaceholderIdMappingIn",
        "LayoutPlaceholderIdMappingOut": "_docs_135_LayoutPlaceholderIdMappingOut",
        "TableBorderCellIn": "_docs_136_TableBorderCellIn",
        "TableBorderCellOut": "_docs_137_TableBorderCellOut",
        "UpdateLineCategoryRequestIn": "_docs_138_UpdateLineCategoryRequestIn",
        "UpdateLineCategoryRequestOut": "_docs_139_UpdateLineCategoryRequestOut",
        "RecolorIn": "_docs_140_RecolorIn",
        "RecolorOut": "_docs_141_RecolorOut",
        "TableRowIn": "_docs_142_TableRowIn",
        "TableRowOut": "_docs_143_TableRowOut",
        "DimensionIn": "_docs_144_DimensionIn",
        "DimensionOut": "_docs_145_DimensionOut",
        "CropPropertiesIn": "_docs_146_CropPropertiesIn",
        "CropPropertiesOut": "_docs_147_CropPropertiesOut",
        "UpdateTextStyleRequestIn": "_docs_148_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_docs_149_UpdateTextStyleRequestOut",
        "TableIn": "_docs_150_TableIn",
        "TableOut": "_docs_151_TableOut",
        "OutlineFillIn": "_docs_152_OutlineFillIn",
        "OutlineFillOut": "_docs_153_OutlineFillOut",
        "UpdatePagePropertiesRequestIn": "_docs_154_UpdatePagePropertiesRequestIn",
        "UpdatePagePropertiesRequestOut": "_docs_155_UpdatePagePropertiesRequestOut",
        "BatchUpdatePresentationRequestIn": "_docs_156_BatchUpdatePresentationRequestIn",
        "BatchUpdatePresentationRequestOut": "_docs_157_BatchUpdatePresentationRequestOut",
        "RgbColorIn": "_docs_158_RgbColorIn",
        "RgbColorOut": "_docs_159_RgbColorOut",
        "PageBackgroundFillIn": "_docs_160_PageBackgroundFillIn",
        "PageBackgroundFillOut": "_docs_161_PageBackgroundFillOut",
        "DeleteObjectRequestIn": "_docs_162_DeleteObjectRequestIn",
        "DeleteObjectRequestOut": "_docs_163_DeleteObjectRequestOut",
        "VideoPropertiesIn": "_docs_164_VideoPropertiesIn",
        "VideoPropertiesOut": "_docs_165_VideoPropertiesOut",
        "PlaceholderIn": "_docs_166_PlaceholderIn",
        "PlaceholderOut": "_docs_167_PlaceholderOut",
        "MergeTableCellsRequestIn": "_docs_168_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_docs_169_MergeTableCellsRequestOut",
        "TableCellLocationIn": "_docs_170_TableCellLocationIn",
        "TableCellLocationOut": "_docs_171_TableCellLocationOut",
        "PresentationIn": "_docs_172_PresentationIn",
        "PresentationOut": "_docs_173_PresentationOut",
        "UpdateVideoPropertiesRequestIn": "_docs_174_UpdateVideoPropertiesRequestIn",
        "UpdateVideoPropertiesRequestOut": "_docs_175_UpdateVideoPropertiesRequestOut",
        "UpdateSlidesPositionRequestIn": "_docs_176_UpdateSlidesPositionRequestIn",
        "UpdateSlidesPositionRequestOut": "_docs_177_UpdateSlidesPositionRequestOut",
        "SubstringMatchCriteriaIn": "_docs_178_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_docs_179_SubstringMatchCriteriaOut",
        "TableBorderPropertiesIn": "_docs_180_TableBorderPropertiesIn",
        "TableBorderPropertiesOut": "_docs_181_TableBorderPropertiesOut",
        "SlidePropertiesIn": "_docs_182_SlidePropertiesIn",
        "SlidePropertiesOut": "_docs_183_SlidePropertiesOut",
        "SolidFillIn": "_docs_184_SolidFillIn",
        "SolidFillOut": "_docs_185_SolidFillOut",
        "DuplicateObjectRequestIn": "_docs_186_DuplicateObjectRequestIn",
        "DuplicateObjectRequestOut": "_docs_187_DuplicateObjectRequestOut",
        "ColorSchemeIn": "_docs_188_ColorSchemeIn",
        "ColorSchemeOut": "_docs_189_ColorSchemeOut",
        "LineIn": "_docs_190_LineIn",
        "LineOut": "_docs_191_LineOut",
        "GroupObjectsRequestIn": "_docs_192_GroupObjectsRequestIn",
        "GroupObjectsRequestOut": "_docs_193_GroupObjectsRequestOut",
        "CreateVideoResponseIn": "_docs_194_CreateVideoResponseIn",
        "CreateVideoResponseOut": "_docs_195_CreateVideoResponseOut",
        "ImageIn": "_docs_196_ImageIn",
        "ImageOut": "_docs_197_ImageOut",
        "StretchedPictureFillIn": "_docs_198_StretchedPictureFillIn",
        "StretchedPictureFillOut": "_docs_199_StretchedPictureFillOut",
        "UpdateShapePropertiesRequestIn": "_docs_200_UpdateShapePropertiesRequestIn",
        "UpdateShapePropertiesRequestOut": "_docs_201_UpdateShapePropertiesRequestOut",
        "VideoIn": "_docs_202_VideoIn",
        "VideoOut": "_docs_203_VideoOut",
        "RangeIn": "_docs_204_RangeIn",
        "RangeOut": "_docs_205_RangeOut",
        "DuplicateObjectResponseIn": "_docs_206_DuplicateObjectResponseIn",
        "DuplicateObjectResponseOut": "_docs_207_DuplicateObjectResponseOut",
        "DeleteTextRequestIn": "_docs_208_DeleteTextRequestIn",
        "DeleteTextRequestOut": "_docs_209_DeleteTextRequestOut",
        "ColorStopIn": "_docs_210_ColorStopIn",
        "ColorStopOut": "_docs_211_ColorStopOut",
        "LayoutReferenceIn": "_docs_212_LayoutReferenceIn",
        "LayoutReferenceOut": "_docs_213_LayoutReferenceOut",
        "DeleteTableRowRequestIn": "_docs_214_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_docs_215_DeleteTableRowRequestOut",
        "RefreshSheetsChartRequestIn": "_docs_216_RefreshSheetsChartRequestIn",
        "RefreshSheetsChartRequestOut": "_docs_217_RefreshSheetsChartRequestOut",
        "UnmergeTableCellsRequestIn": "_docs_218_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_docs_219_UnmergeTableCellsRequestOut",
        "ReplaceImageRequestIn": "_docs_220_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_docs_221_ReplaceImageRequestOut",
        "ReplaceAllShapesWithSheetsChartResponseIn": "_docs_222_ReplaceAllShapesWithSheetsChartResponseIn",
        "ReplaceAllShapesWithSheetsChartResponseOut": "_docs_223_ReplaceAllShapesWithSheetsChartResponseOut",
        "ImagePropertiesIn": "_docs_224_ImagePropertiesIn",
        "ImagePropertiesOut": "_docs_225_ImagePropertiesOut",
        "CreateSheetsChartRequestIn": "_docs_226_CreateSheetsChartRequestIn",
        "CreateSheetsChartRequestOut": "_docs_227_CreateSheetsChartRequestOut",
        "TextContentIn": "_docs_228_TextContentIn",
        "TextContentOut": "_docs_229_TextContentOut",
        "NestingLevelIn": "_docs_230_NestingLevelIn",
        "NestingLevelOut": "_docs_231_NestingLevelOut",
        "WriteControlIn": "_docs_232_WriteControlIn",
        "WriteControlOut": "_docs_233_WriteControlOut",
        "CreateLineRequestIn": "_docs_234_CreateLineRequestIn",
        "CreateLineRequestOut": "_docs_235_CreateLineRequestOut",
        "ThemeColorPairIn": "_docs_236_ThemeColorPairIn",
        "ThemeColorPairOut": "_docs_237_ThemeColorPairOut",
        "TextRunIn": "_docs_238_TextRunIn",
        "TextRunOut": "_docs_239_TextRunOut",
        "ShapePropertiesIn": "_docs_240_ShapePropertiesIn",
        "ShapePropertiesOut": "_docs_241_ShapePropertiesOut",
        "UpdateTableBorderPropertiesRequestIn": "_docs_242_UpdateTableBorderPropertiesRequestIn",
        "UpdateTableBorderPropertiesRequestOut": "_docs_243_UpdateTableBorderPropertiesRequestOut",
        "DeleteParagraphBulletsRequestIn": "_docs_244_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_docs_245_DeleteParagraphBulletsRequestOut",
        "TableCellIn": "_docs_246_TableCellIn",
        "TableCellOut": "_docs_247_TableCellOut",
        "ReplaceAllShapesWithImageRequestIn": "_docs_248_ReplaceAllShapesWithImageRequestIn",
        "ReplaceAllShapesWithImageRequestOut": "_docs_249_ReplaceAllShapesWithImageRequestOut",
        "WeightedFontFamilyIn": "_docs_250_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_docs_251_WeightedFontFamilyOut",
        "PageElementPropertiesIn": "_docs_252_PageElementPropertiesIn",
        "PageElementPropertiesOut": "_docs_253_PageElementPropertiesOut",
        "RerouteLineRequestIn": "_docs_254_RerouteLineRequestIn",
        "RerouteLineRequestOut": "_docs_255_RerouteLineRequestOut",
        "CreateTableResponseIn": "_docs_256_CreateTableResponseIn",
        "CreateTableResponseOut": "_docs_257_CreateTableResponseOut",
        "OpaqueColorIn": "_docs_258_OpaqueColorIn",
        "OpaqueColorOut": "_docs_259_OpaqueColorOut",
        "CreateShapeRequestIn": "_docs_260_CreateShapeRequestIn",
        "CreateShapeRequestOut": "_docs_261_CreateShapeRequestOut",
        "TableBorderFillIn": "_docs_262_TableBorderFillIn",
        "TableBorderFillOut": "_docs_263_TableBorderFillOut",
        "CreateImageRequestIn": "_docs_264_CreateImageRequestIn",
        "CreateImageRequestOut": "_docs_265_CreateImageRequestOut",
        "UpdateParagraphStyleRequestIn": "_docs_266_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_docs_267_UpdateParagraphStyleRequestOut",
        "DeleteTableColumnRequestIn": "_docs_268_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_docs_269_DeleteTableColumnRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
    types["RequestIn"] = t.struct(
        {
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestIn"]).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestIn"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestIn"]).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestIn"]).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestIn"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestIn"]).optional(),
            "createTable": t.proxy(renames["CreateTableRequestIn"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestIn"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestIn"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestIn"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestIn"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestIn"]).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestIn"]).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestIn"]
            ).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestIn"]).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestIn"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestIn"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestIn"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestIn"]
            ).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestIn"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestIn"]
            ).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestIn"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestIn"]
            ).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestIn"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestIn"]).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestIn"]
            ).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestIn"]
            ).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestIn"]
            ).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestIn"]
            ).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestIn"]
            ).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestOut"]).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestOut"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestOut"]).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestOut"]).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestOut"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestOut"]).optional(),
            "createTable": t.proxy(renames["CreateTableRequestOut"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestOut"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestOut"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestOut"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestOut"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestOut"]).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestOut"]).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestOut"]
            ).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestOut"]).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestOut"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestOut"]
            ).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestOut"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestOut"]
            ).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestOut"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestOut"]
            ).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestOut"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestOut"]
            ).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestOut"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestOut"]).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestOut"]
            ).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestOut"]
            ).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestOut"]
            ).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestOut"]
            ).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestOut"]
            ).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "direction": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "lineSpacing": t.number().optional(),
            "alignment": t.string().optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "spacingMode": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "direction": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "lineSpacing": t.number().optional(),
            "alignment": t.string().optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "spacingMode": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
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
    types["InsertTableRowsRequestIn"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "insertBelow": t.boolean().optional(),
            "number": t.integer().optional(),
        }
    ).named(renames["InsertTableRowsRequestIn"])
    types["InsertTableRowsRequestOut"] = t.struct(
        {
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "insertBelow": t.boolean().optional(),
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRowsRequestOut"])
    types["ResponseIn"] = t.struct(
        {
            "createShape": t.proxy(renames["CreateShapeResponseIn"]).optional(),
            "createTable": t.proxy(renames["CreateTableResponseIn"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseIn"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseIn"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectResponseIn"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseIn"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseIn"]).optional(),
            "createLine": t.proxy(renames["CreateLineResponseIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseIn"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseIn"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseIn"]
            ).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "createShape": t.proxy(renames["CreateShapeResponseOut"]).optional(),
            "createTable": t.proxy(renames["CreateTableResponseOut"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseOut"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseOut"]
            ).optional(),
            "duplicateObject": t.proxy(
                renames["DuplicateObjectResponseOut"]
            ).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseOut"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseOut"]).optional(),
            "createLine": t.proxy(renames["CreateLineResponseOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseOut"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseOut"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["UpdatePageElementsZOrderRequestIn"] = t.struct(
        {
            "operation": t.string().optional(),
            "pageElementObjectIds": t.array(t.string()).optional(),
        }
    ).named(renames["UpdatePageElementsZOrderRequestIn"])
    types["UpdatePageElementsZOrderRequestOut"] = t.struct(
        {
            "operation": t.string().optional(),
            "pageElementObjectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementsZOrderRequestOut"])
    types["OptionalColorIn"] = t.struct(
        {"opaqueColor": t.proxy(renames["OpaqueColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "opaqueColor": t.proxy(renames["OpaqueColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
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
    types["UpdateTableRowPropertiesRequestIn"] = t.struct(
        {
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestIn"])
    types["UpdateTableRowPropertiesRequestOut"] = t.struct(
        {
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestOut"])
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
    types["TextElementIn"] = t.struct(
        {
            "paragraphMarker": t.proxy(renames["ParagraphMarkerIn"]).optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
            "endIndex": t.integer().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["TextElementIn"])
    types["TextElementOut"] = t.struct(
        {
            "paragraphMarker": t.proxy(renames["ParagraphMarkerOut"]).optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "endIndex": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextElementOut"])
    types["SheetsChartIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesIn"]
            ).optional(),
            "chartId": t.integer().optional(),
            "contentUrl": t.string().optional(),
        }
    ).named(renames["SheetsChartIn"])
    types["SheetsChartOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesOut"]
            ).optional(),
            "chartId": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartOut"])
    types["GroupObjectsResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["GroupObjectsResponseIn"])
    types["GroupObjectsResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupObjectsResponseOut"])
    types["MasterPropertiesIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["MasterPropertiesIn"])
    types["MasterPropertiesOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterPropertiesOut"])
    types["ReplaceAllShapesWithImageResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithImageResponseIn"])
    types["ReplaceAllShapesWithImageResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageResponseOut"])
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
    types["AffineTransformIn"] = t.struct(
        {
            "translateX": t.number().optional(),
            "shearY": t.number().optional(),
            "unit": t.string().optional(),
            "translateY": t.number().optional(),
            "shearX": t.number().optional(),
            "scaleY": t.number().optional(),
            "scaleX": t.number().optional(),
        }
    ).named(renames["AffineTransformIn"])
    types["AffineTransformOut"] = t.struct(
        {
            "translateX": t.number().optional(),
            "shearY": t.number().optional(),
            "unit": t.string().optional(),
            "translateY": t.number().optional(),
            "shearX": t.number().optional(),
            "scaleY": t.number().optional(),
            "scaleX": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AffineTransformOut"])
    types["UpdateSlidePropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
        }
    ).named(renames["UpdateSlidePropertiesRequestIn"])
    types["UpdateSlidePropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlidePropertiesRequestOut"])
    types["GroupIn"] = t.struct(
        {"children": t.array(t.proxy(renames["PageElementIn"])).optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "children": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["ShapeIn"] = t.struct(
        {
            "shapeType": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesIn"]).optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
        }
    ).named(renames["ShapeIn"])
    types["ShapeOut"] = t.struct(
        {
            "shapeType": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesOut"]).optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapeOut"])
    types["CreateSlideResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSlideResponseIn"])
    types["CreateSlideResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideResponseOut"])
    types["CreateParagraphBulletsRequestIn"] = t.struct(
        {
            "bulletPreset": t.string().optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestIn"])
    types["CreateParagraphBulletsRequestOut"] = t.struct(
        {
            "bulletPreset": t.string().optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestOut"])
    types["TableColumnPropertiesIn"] = t.struct(
        {"columnWidth": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableColumnPropertiesIn"])
    types["TableColumnPropertiesOut"] = t.struct(
        {
            "columnWidth": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableColumnPropertiesOut"])
    types["TextStyleIn"] = t.struct(
        {
            "strikethrough": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "bold": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "underline": t.boolean().optional(),
            "fontFamily": t.string().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "smallCaps": t.boolean().optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "strikethrough": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "bold": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "underline": t.boolean().optional(),
            "fontFamily": t.string().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "smallCaps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
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
    types["NotesPropertiesIn"] = t.struct(
        {"speakerNotesObjectId": t.string().optional()}
    ).named(renames["NotesPropertiesIn"])
    types["NotesPropertiesOut"] = t.struct(
        {
            "speakerNotesObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotesPropertiesOut"])
    types["CreateTableRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "rows": t.integer().optional(),
            "columns": t.integer().optional(),
        }
    ).named(renames["CreateTableRequestIn"])
    types["CreateTableRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "rows": t.integer().optional(),
            "columns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableRequestOut"])
    types["WordArtIn"] = t.struct({"renderedText": t.string().optional()}).named(
        renames["WordArtIn"]
    )
    types["WordArtOut"] = t.struct(
        {
            "renderedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordArtOut"])
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
    types["CreateVideoRequestIn"] = t.struct(
        {
            "id": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "source": t.string().optional(),
        }
    ).named(renames["CreateVideoRequestIn"])
    types["CreateVideoRequestOut"] = t.struct(
        {
            "id": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoRequestOut"])
    types["ThumbnailIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "contentUrl": t.string().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "contentUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
    types["SheetsChartPropertiesIn"] = t.struct(
        {"chartImageProperties": t.proxy(renames["ImagePropertiesIn"]).optional()}
    ).named(renames["SheetsChartPropertiesIn"])
    types["SheetsChartPropertiesOut"] = t.struct(
        {
            "chartImageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartPropertiesOut"])
    types["OutlineIn"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "dashStyle": t.string().optional(),
            "propertyState": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillIn"]).optional(),
        }
    ).named(renames["OutlineIn"])
    types["OutlineOut"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "propertyState": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineOut"])
    types["ShadowIn"] = t.struct(
        {
            "blurRadius": t.proxy(renames["DimensionIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "propertyState": t.string().optional(),
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "alignment": t.string().optional(),
            "rotateWithShape": t.boolean().optional(),
            "alpha": t.number().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ShadowIn"])
    types["ShadowOut"] = t.struct(
        {
            "blurRadius": t.proxy(renames["DimensionOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "propertyState": t.string().optional(),
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "alignment": t.string().optional(),
            "rotateWithShape": t.boolean().optional(),
            "alpha": t.number().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadowOut"])
    types["LinkIn"] = t.struct(
        {
            "slideIndex": t.integer().optional(),
            "url": t.string().optional(),
            "relativeLink": t.string().optional(),
            "pageObjectId": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "slideIndex": t.integer().optional(),
            "url": t.string().optional(),
            "relativeLink": t.string().optional(),
            "pageObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
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
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "columnIndices": t.array(t.integer()).optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "columnIndices": t.array(t.integer()).optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["UpdatePageElementTransformRequestIn"] = t.struct(
        {
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "applyMode": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdatePageElementTransformRequestIn"])
    types["UpdatePageElementTransformRequestOut"] = t.struct(
        {
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "applyMode": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementTransformRequestOut"])
    types["InsertTextRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "text": t.string().optional(),
            "insertionIndex": t.integer().optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "text": t.string().optional(),
            "insertionIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
    types["TableRowPropertiesIn"] = t.struct(
        {"minRowHeight": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableRowPropertiesIn"])
    types["TableRowPropertiesOut"] = t.struct(
        {
            "minRowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowPropertiesOut"])
    types["TableRangeIn"] = t.struct(
        {
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "rowSpan": t.integer().optional(),
            "columnSpan": t.integer().optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "columnSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
    types["CreateImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateImageResponseIn"])
    types["CreateImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageResponseOut"])
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
    types["BulletIn"] = t.struct(
        {
            "nestingLevel": t.integer().optional(),
            "listId": t.string().optional(),
            "glyph": t.string().optional(),
            "bulletStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["BulletIn"])
    types["BulletOut"] = t.struct(
        {
            "nestingLevel": t.integer().optional(),
            "listId": t.string().optional(),
            "glyph": t.string().optional(),
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletOut"])
    types["CreateSlideRequestIn"] = t.struct(
        {
            "insertionIndex": t.integer().optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingIn"])
            ).optional(),
            "slideLayoutReference": t.proxy(renames["LayoutReferenceIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["CreateSlideRequestIn"])
    types["CreateSlideRequestOut"] = t.struct(
        {
            "insertionIndex": t.integer().optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingOut"])
            ).optional(),
            "slideLayoutReference": t.proxy(renames["LayoutReferenceOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideRequestOut"])
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
    types["UngroupObjectsRequestIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["UngroupObjectsRequestIn"])
    types["UngroupObjectsRequestOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UngroupObjectsRequestOut"])
    types["CreateLineResponseIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["CreateLineResponseIn"]
    )
    types["CreateLineResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineResponseOut"])
    types["ListIn"] = t.struct(
        {
            "listId": t.string().optional(),
            "nestingLevel": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ListIn"])
    types["ListOut"] = t.struct(
        {
            "listId": t.string().optional(),
            "nestingLevel": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOut"])
    types["CreateShapeResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateShapeResponseIn"])
    types["CreateShapeResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeResponseOut"])
    types["LinePropertiesIn"] = t.struct(
        {
            "lineFill": t.proxy(renames["LineFillIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "startArrow": t.string().optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "endArrow": t.string().optional(),
            "dashStyle": t.string().optional(),
            "startConnection": t.proxy(renames["LineConnectionIn"]).optional(),
        }
    ).named(renames["LinePropertiesIn"])
    types["LinePropertiesOut"] = t.struct(
        {
            "lineFill": t.proxy(renames["LineFillOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "startArrow": t.string().optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "endArrow": t.string().optional(),
            "dashStyle": t.string().optional(),
            "startConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinePropertiesOut"])
    types["CreateSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSheetsChartResponseIn"])
    types["CreateSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartResponseOut"])
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
    types["PageIn"] = t.struct(
        {
            "layoutProperties": t.proxy(renames["LayoutPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesIn"]).optional(),
            "pageType": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesIn"]).optional(),
            "pageElements": t.array(t.proxy(renames["PageElementIn"])).optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "layoutProperties": t.proxy(renames["LayoutPropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "notesProperties": t.proxy(renames["NotesPropertiesOut"]).optional(),
            "pageType": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesOut"]).optional(),
            "pageElements": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["ReplaceAllShapesWithSheetsChartRequestIn"] = t.struct(
        {
            "linkingMode": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "chartId": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestIn"])
    types["ReplaceAllShapesWithSheetsChartRequestOut"] = t.struct(
        {
            "linkingMode": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "chartId": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestOut"])
    types["LineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["LineFillIn"])
    types["LineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineFillOut"])
    types["UpdateImagePropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateImagePropertiesRequestIn"])
    types["UpdateImagePropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateImagePropertiesRequestOut"])
    types["InsertTableColumnsRequestIn"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "insertRight": t.boolean().optional(),
            "number": t.integer().optional(),
            "tableObjectId": t.string().optional(),
        }
    ).named(renames["InsertTableColumnsRequestIn"])
    types["InsertTableColumnsRequestOut"] = t.struct(
        {
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "insertRight": t.boolean().optional(),
            "number": t.integer().optional(),
            "tableObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableColumnsRequestOut"])
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
    types["PageElementIn"] = t.struct(
        {
            "description": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "wordArt": t.proxy(renames["WordArtIn"]).optional(),
            "line": t.proxy(renames["LineIn"]).optional(),
            "elementGroup": t.proxy(renames["GroupIn"]).optional(),
            "video": t.proxy(renames["VideoIn"]).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "shape": t.proxy(renames["ShapeIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "objectId": t.string().optional(),
            "title": t.string().optional(),
            "sheetsChart": t.proxy(renames["SheetsChartIn"]).optional(),
        }
    ).named(renames["PageElementIn"])
    types["PageElementOut"] = t.struct(
        {
            "description": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "wordArt": t.proxy(renames["WordArtOut"]).optional(),
            "line": t.proxy(renames["LineOut"]).optional(),
            "elementGroup": t.proxy(renames["GroupOut"]).optional(),
            "video": t.proxy(renames["VideoOut"]).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "shape": t.proxy(renames["ShapeOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "objectId": t.string().optional(),
            "title": t.string().optional(),
            "sheetsChart": t.proxy(renames["SheetsChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementOut"])
    types["LayoutPlaceholderIdMappingIn"] = t.struct(
        {
            "layoutPlaceholderObjectId": t.string().optional(),
            "layoutPlaceholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["LayoutPlaceholderIdMappingIn"])
    types["LayoutPlaceholderIdMappingOut"] = t.struct(
        {
            "layoutPlaceholderObjectId": t.string().optional(),
            "layoutPlaceholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutPlaceholderIdMappingOut"])
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
    types["CropPropertiesIn"] = t.struct(
        {
            "topOffset": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "rightOffset": t.number().optional(),
            "angle": t.number().optional(),
            "leftOffset": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "topOffset": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "rightOffset": t.number().optional(),
            "angle": t.number().optional(),
            "leftOffset": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
    types["TableIn"] = t.struct(
        {
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "columns": t.integer().optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "rows": t.integer().optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesIn"])
            ).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "columns": t.integer().optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "rows": t.integer().optional(),
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesOut"])
            ).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["OutlineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["OutlineFillIn"])
    types["OutlineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineFillOut"])
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
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
            "propertyState": t.string().optional(),
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillIn"]
            ).optional(),
        }
    ).named(renames["PageBackgroundFillIn"])
    types["PageBackgroundFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "propertyState": t.string().optional(),
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBackgroundFillOut"])
    types["DeleteObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeleteObjectRequestIn"])
    types["DeleteObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteObjectRequestOut"])
    types["VideoPropertiesIn"] = t.struct(
        {
            "start": t.integer().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "end": t.integer().optional(),
            "mute": t.boolean().optional(),
            "autoPlay": t.boolean().optional(),
        }
    ).named(renames["VideoPropertiesIn"])
    types["VideoPropertiesOut"] = t.struct(
        {
            "start": t.integer().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "end": t.integer().optional(),
            "mute": t.boolean().optional(),
            "autoPlay": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPropertiesOut"])
    types["PlaceholderIn"] = t.struct(
        {
            "type": t.string().optional(),
            "parentObjectId": t.string().optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["PlaceholderIn"])
    types["PlaceholderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "parentObjectId": t.string().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceholderOut"])
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
    types["PresentationIn"] = t.struct(
        {
            "masters": t.array(t.proxy(renames["PageIn"])).optional(),
            "presentationId": t.string().optional(),
            "revisionId": t.string().optional(),
            "slides": t.array(t.proxy(renames["PageIn"])).optional(),
            "locale": t.string().optional(),
            "title": t.string().optional(),
            "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
            "notesMaster": t.proxy(renames["PageIn"]).optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
        }
    ).named(renames["PresentationIn"])
    types["PresentationOut"] = t.struct(
        {
            "masters": t.array(t.proxy(renames["PageOut"])).optional(),
            "presentationId": t.string().optional(),
            "revisionId": t.string().optional(),
            "slides": t.array(t.proxy(renames["PageOut"])).optional(),
            "locale": t.string().optional(),
            "title": t.string().optional(),
            "layouts": t.array(t.proxy(renames["PageOut"])).optional(),
            "notesMaster": t.proxy(renames["PageOut"]).optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationOut"])
    types["UpdateVideoPropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesIn"]).optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestIn"])
    types["UpdateVideoPropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestOut"])
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
    types["TableBorderPropertiesIn"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "tableBorderFill": t.proxy(renames["TableBorderFillIn"]).optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["TableBorderPropertiesIn"])
    types["TableBorderPropertiesOut"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "tableBorderFill": t.proxy(renames["TableBorderFillOut"]).optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderPropertiesOut"])
    types["SlidePropertiesIn"] = t.struct(
        {
            "layoutObjectId": t.string().optional(),
            "masterObjectId": t.string().optional(),
            "notesPage": t.proxy(renames["PageIn"]).optional(),
            "isSkipped": t.boolean().optional(),
        }
    ).named(renames["SlidePropertiesIn"])
    types["SlidePropertiesOut"] = t.struct(
        {
            "layoutObjectId": t.string().optional(),
            "masterObjectId": t.string().optional(),
            "notesPage": t.proxy(renames["PageOut"]).optional(),
            "isSkipped": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlidePropertiesOut"])
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
    types["ColorSchemeIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ThemeColorPairIn"])).optional()}
    ).named(renames["ColorSchemeIn"])
    types["ColorSchemeOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ThemeColorPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorSchemeOut"])
    types["LineIn"] = t.struct(
        {
            "lineProperties": t.proxy(renames["LinePropertiesIn"]).optional(),
            "lineType": t.string().optional(),
            "lineCategory": t.string().optional(),
        }
    ).named(renames["LineIn"])
    types["LineOut"] = t.struct(
        {
            "lineProperties": t.proxy(renames["LinePropertiesOut"]).optional(),
            "lineType": t.string().optional(),
            "lineCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineOut"])
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
    types["CreateVideoResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateVideoResponseIn"])
    types["CreateVideoResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoResponseOut"])
    types["ImageIn"] = t.struct(
        {
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "contentUrl": t.string().optional(),
            "sourceUrl": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "contentUrl": t.string().optional(),
            "sourceUrl": t.string().optional(),
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
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
    types["VideoIn"] = t.struct(
        {
            "source": t.string().optional(),
            "id": t.string().optional(),
            "url": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesIn"]).optional(),
        }
    ).named(renames["VideoIn"])
    types["VideoOut"] = t.struct(
        {
            "source": t.string().optional(),
            "id": t.string().optional(),
            "url": t.string().optional(),
            "videoProperties": t.proxy(renames["VideoPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOut"])
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
    types["DuplicateObjectResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DuplicateObjectResponseIn"])
    types["DuplicateObjectResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateObjectResponseOut"])
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
    types["RefreshSheetsChartRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["RefreshSheetsChartRequestIn"])
    types["RefreshSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshSheetsChartRequestOut"])
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
    types["ReplaceAllShapesWithSheetsChartResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseIn"])
    types["ReplaceAllShapesWithSheetsChartResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseOut"])
    types["ImagePropertiesIn"] = t.struct(
        {
            "brightness": t.number().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "contrast": t.number().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "transparency": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "recolor": t.proxy(renames["RecolorIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "brightness": t.number().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "contrast": t.number().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "transparency": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "recolor": t.proxy(renames["RecolorOut"]).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["CreateSheetsChartRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "linkingMode": t.string().optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["CreateSheetsChartRequestIn"])
    types["CreateSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "linkingMode": t.string().optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartRequestOut"])
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
    types["NestingLevelIn"] = t.struct(
        {"bulletStyle": t.proxy(renames["TextStyleIn"]).optional()}
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
    types["WriteControlIn"] = t.struct(
        {"requiredRevisionId": t.string().optional()}
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
    types["CreateLineRequestIn"] = t.struct(
        {
            "category": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "lineCategory": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["CreateLineRequestIn"])
    types["CreateLineRequestOut"] = t.struct(
        {
            "category": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "lineCategory": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineRequestOut"])
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
    types["TextRunIn"] = t.struct(
        {
            "content": t.string().optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["TextRunIn"])
    types["TextRunOut"] = t.struct(
        {
            "content": t.string().optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextRunOut"])
    types["ShapePropertiesIn"] = t.struct(
        {
            "shapeBackgroundFill": t.proxy(renames["ShapeBackgroundFillIn"]).optional(),
            "contentAlignment": t.string().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "autofit": t.proxy(renames["AutofitIn"]).optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
        }
    ).named(renames["ShapePropertiesIn"])
    types["ShapePropertiesOut"] = t.struct(
        {
            "shapeBackgroundFill": t.proxy(
                renames["ShapeBackgroundFillOut"]
            ).optional(),
            "contentAlignment": t.string().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "autofit": t.proxy(renames["AutofitOut"]).optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapePropertiesOut"])
    types["UpdateTableBorderPropertiesRequestIn"] = t.struct(
        {
            "borderPosition": t.string().optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesIn"]
            ).optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestIn"])
    types["UpdateTableBorderPropertiesRequestOut"] = t.struct(
        {
            "borderPosition": t.string().optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestOut"])
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
    types["TableCellIn"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
    types["ReplaceAllShapesWithImageRequestIn"] = t.struct(
        {
            "replaceMethod": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "imageReplaceMethod": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestIn"])
    types["ReplaceAllShapesWithImageRequestOut"] = t.struct(
        {
            "replaceMethod": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "imageReplaceMethod": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestOut"])
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
    types["PageElementPropertiesIn"] = t.struct(
        {
            "pageObjectId": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
        }
    ).named(renames["PageElementPropertiesIn"])
    types["PageElementPropertiesOut"] = t.struct(
        {
            "pageObjectId": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementPropertiesOut"])
    types["RerouteLineRequestIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["RerouteLineRequestIn"]
    )
    types["RerouteLineRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RerouteLineRequestOut"])
    types["CreateTableResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateTableResponseIn"])
    types["CreateTableResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableResponseOut"])
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
    types["CreateShapeRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "shapeType": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
        }
    ).named(renames["CreateShapeRequestIn"])
    types["CreateShapeRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "shapeType": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeRequestOut"])
    types["TableBorderFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["TableBorderFillIn"])
    types["TableBorderFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderFillOut"])
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
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "style": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "fields": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "style": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "fields": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])
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

    functions = {}
    functions["presentationsBatchUpdate"] = docs.get(
        "v1/presentations/{presentationId}",
        t.struct(
            {"presentationId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsCreate"] = docs.get(
        "v1/presentations/{presentationId}",
        t.struct(
            {"presentationId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsGet"] = docs.get(
        "v1/presentations/{presentationId}",
        t.struct(
            {"presentationId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["PresentationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsPagesGet"] = docs.get(
        "v1/presentations/{presentationId}/pages/{pageObjectId}/thumbnail",
        t.struct(
            {
                "pageObjectId": t.string().optional(),
                "presentationId": t.string().optional(),
                "thumbnailProperties.thumbnailSize": t.string().optional(),
                "thumbnailProperties.mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThumbnailOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsPagesGetThumbnail"] = docs.get(
        "v1/presentations/{presentationId}/pages/{pageObjectId}/thumbnail",
        t.struct(
            {
                "pageObjectId": t.string().optional(),
                "presentationId": t.string().optional(),
                "thumbnailProperties.thumbnailSize": t.string().optional(),
                "thumbnailProperties.mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThumbnailOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="docs", renames=renames, types=types, functions=functions)
