from typegraph import effects
from typegraph import t
from typegraph.importers.base.importer import Import
from typegraph import TypeGraph
from typegraph.runtimes.http import HTTPRuntime


def import_slides() -> Import:
    slides = HTTPRuntime("https://slides.googleapis.com/")

    renames = {
        "ErrorResponse": "_slides_1_ErrorResponse",
        "DeleteTableRowRequestIn": "_slides_2_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_slides_3_DeleteTableRowRequestOut",
        "TableBorderFillIn": "_slides_4_TableBorderFillIn",
        "TableBorderFillOut": "_slides_5_TableBorderFillOut",
        "LineConnectionIn": "_slides_6_LineConnectionIn",
        "LineConnectionOut": "_slides_7_LineConnectionOut",
        "PageElementPropertiesIn": "_slides_8_PageElementPropertiesIn",
        "PageElementPropertiesOut": "_slides_9_PageElementPropertiesOut",
        "UpdatePageElementTransformRequestIn": "_slides_10_UpdatePageElementTransformRequestIn",
        "UpdatePageElementTransformRequestOut": "_slides_11_UpdatePageElementTransformRequestOut",
        "RerouteLineRequestIn": "_slides_12_RerouteLineRequestIn",
        "RerouteLineRequestOut": "_slides_13_RerouteLineRequestOut",
        "StretchedPictureFillIn": "_slides_14_StretchedPictureFillIn",
        "StretchedPictureFillOut": "_slides_15_StretchedPictureFillOut",
        "ShadowIn": "_slides_16_ShadowIn",
        "ShadowOut": "_slides_17_ShadowOut",
        "ShapeBackgroundFillIn": "_slides_18_ShapeBackgroundFillIn",
        "ShapeBackgroundFillOut": "_slides_19_ShapeBackgroundFillOut",
        "TextContentIn": "_slides_20_TextContentIn",
        "TextContentOut": "_slides_21_TextContentOut",
        "TableCellIn": "_slides_22_TableCellIn",
        "TableCellOut": "_slides_23_TableCellOut",
        "TableBorderRowIn": "_slides_24_TableBorderRowIn",
        "TableBorderRowOut": "_slides_25_TableBorderRowOut",
        "InsertTextRequestIn": "_slides_26_InsertTextRequestIn",
        "InsertTextRequestOut": "_slides_27_InsertTextRequestOut",
        "ColorStopIn": "_slides_28_ColorStopIn",
        "ColorStopOut": "_slides_29_ColorStopOut",
        "GroupIn": "_slides_30_GroupIn",
        "GroupOut": "_slides_31_GroupOut",
        "TableCellPropertiesIn": "_slides_32_TableCellPropertiesIn",
        "TableCellPropertiesOut": "_slides_33_TableCellPropertiesOut",
        "MasterPropertiesIn": "_slides_34_MasterPropertiesIn",
        "MasterPropertiesOut": "_slides_35_MasterPropertiesOut",
        "DeleteObjectRequestIn": "_slides_36_DeleteObjectRequestIn",
        "DeleteObjectRequestOut": "_slides_37_DeleteObjectRequestOut",
        "ReplaceAllShapesWithSheetsChartRequestIn": "_slides_38_ReplaceAllShapesWithSheetsChartRequestIn",
        "ReplaceAllShapesWithSheetsChartRequestOut": "_slides_39_ReplaceAllShapesWithSheetsChartRequestOut",
        "PageIn": "_slides_40_PageIn",
        "PageOut": "_slides_41_PageOut",
        "TextElementIn": "_slides_42_TextElementIn",
        "TextElementOut": "_slides_43_TextElementOut",
        "ParagraphMarkerIn": "_slides_44_ParagraphMarkerIn",
        "ParagraphMarkerOut": "_slides_45_ParagraphMarkerOut",
        "UpdateVideoPropertiesRequestIn": "_slides_46_UpdateVideoPropertiesRequestIn",
        "UpdateVideoPropertiesRequestOut": "_slides_47_UpdateVideoPropertiesRequestOut",
        "ThemeColorPairIn": "_slides_48_ThemeColorPairIn",
        "ThemeColorPairOut": "_slides_49_ThemeColorPairOut",
        "OutlineFillIn": "_slides_50_OutlineFillIn",
        "OutlineFillOut": "_slides_51_OutlineFillOut",
        "LayoutReferenceIn": "_slides_52_LayoutReferenceIn",
        "LayoutReferenceOut": "_slides_53_LayoutReferenceOut",
        "TableBorderCellIn": "_slides_54_TableBorderCellIn",
        "TableBorderCellOut": "_slides_55_TableBorderCellOut",
        "ReplaceAllTextRequestIn": "_slides_56_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_slides_57_ReplaceAllTextRequestOut",
        "UpdatePageElementsZOrderRequestIn": "_slides_58_UpdatePageElementsZOrderRequestIn",
        "UpdatePageElementsZOrderRequestOut": "_slides_59_UpdatePageElementsZOrderRequestOut",
        "UpdateTableCellPropertiesRequestIn": "_slides_60_UpdateTableCellPropertiesRequestIn",
        "UpdateTableCellPropertiesRequestOut": "_slides_61_UpdateTableCellPropertiesRequestOut",
        "ImagePropertiesIn": "_slides_62_ImagePropertiesIn",
        "ImagePropertiesOut": "_slides_63_ImagePropertiesOut",
        "UpdateTableBorderPropertiesRequestIn": "_slides_64_UpdateTableBorderPropertiesRequestIn",
        "UpdateTableBorderPropertiesRequestOut": "_slides_65_UpdateTableBorderPropertiesRequestOut",
        "DeleteParagraphBulletsRequestIn": "_slides_66_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_slides_67_DeleteParagraphBulletsRequestOut",
        "TableCellBackgroundFillIn": "_slides_68_TableCellBackgroundFillIn",
        "TableCellBackgroundFillOut": "_slides_69_TableCellBackgroundFillOut",
        "CreateImageResponseIn": "_slides_70_CreateImageResponseIn",
        "CreateImageResponseOut": "_slides_71_CreateImageResponseOut",
        "RangeIn": "_slides_72_RangeIn",
        "RangeOut": "_slides_73_RangeOut",
        "UpdateTableRowPropertiesRequestIn": "_slides_74_UpdateTableRowPropertiesRequestIn",
        "UpdateTableRowPropertiesRequestOut": "_slides_75_UpdateTableRowPropertiesRequestOut",
        "OpaqueColorIn": "_slides_76_OpaqueColorIn",
        "OpaqueColorOut": "_slides_77_OpaqueColorOut",
        "UpdateTextStyleRequestIn": "_slides_78_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_slides_79_UpdateTextStyleRequestOut",
        "CreateLineResponseIn": "_slides_80_CreateLineResponseIn",
        "CreateLineResponseOut": "_slides_81_CreateLineResponseOut",
        "SubstringMatchCriteriaIn": "_slides_82_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_slides_83_SubstringMatchCriteriaOut",
        "UpdateLineCategoryRequestIn": "_slides_84_UpdateLineCategoryRequestIn",
        "UpdateLineCategoryRequestOut": "_slides_85_UpdateLineCategoryRequestOut",
        "PageBackgroundFillIn": "_slides_86_PageBackgroundFillIn",
        "PageBackgroundFillOut": "_slides_87_PageBackgroundFillOut",
        "NestingLevelIn": "_slides_88_NestingLevelIn",
        "NestingLevelOut": "_slides_89_NestingLevelOut",
        "ShapePropertiesIn": "_slides_90_ShapePropertiesIn",
        "ShapePropertiesOut": "_slides_91_ShapePropertiesOut",
        "TableColumnPropertiesIn": "_slides_92_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_slides_93_TableColumnPropertiesOut",
        "TableCellLocationIn": "_slides_94_TableCellLocationIn",
        "TableCellLocationOut": "_slides_95_TableCellLocationOut",
        "TextRunIn": "_slides_96_TextRunIn",
        "TextRunOut": "_slides_97_TextRunOut",
        "PlaceholderIn": "_slides_98_PlaceholderIn",
        "PlaceholderOut": "_slides_99_PlaceholderOut",
        "CreateSlideResponseIn": "_slides_100_CreateSlideResponseIn",
        "CreateSlideResponseOut": "_slides_101_CreateSlideResponseOut",
        "InsertTableRowsRequestIn": "_slides_102_InsertTableRowsRequestIn",
        "InsertTableRowsRequestOut": "_slides_103_InsertTableRowsRequestOut",
        "DuplicateObjectResponseIn": "_slides_104_DuplicateObjectResponseIn",
        "DuplicateObjectResponseOut": "_slides_105_DuplicateObjectResponseOut",
        "UpdateShapePropertiesRequestIn": "_slides_106_UpdateShapePropertiesRequestIn",
        "UpdateShapePropertiesRequestOut": "_slides_107_UpdateShapePropertiesRequestOut",
        "UpdatePageElementAltTextRequestIn": "_slides_108_UpdatePageElementAltTextRequestIn",
        "UpdatePageElementAltTextRequestOut": "_slides_109_UpdatePageElementAltTextRequestOut",
        "WordArtIn": "_slides_110_WordArtIn",
        "WordArtOut": "_slides_111_WordArtOut",
        "VideoIn": "_slides_112_VideoIn",
        "VideoOut": "_slides_113_VideoOut",
        "NotesPropertiesIn": "_slides_114_NotesPropertiesIn",
        "NotesPropertiesOut": "_slides_115_NotesPropertiesOut",
        "CreateVideoResponseIn": "_slides_116_CreateVideoResponseIn",
        "CreateVideoResponseOut": "_slides_117_CreateVideoResponseOut",
        "UpdatePagePropertiesRequestIn": "_slides_118_UpdatePagePropertiesRequestIn",
        "UpdatePagePropertiesRequestOut": "_slides_119_UpdatePagePropertiesRequestOut",
        "CreateSlideRequestIn": "_slides_120_CreateSlideRequestIn",
        "CreateSlideRequestOut": "_slides_121_CreateSlideRequestOut",
        "OutlineIn": "_slides_122_OutlineIn",
        "OutlineOut": "_slides_123_OutlineOut",
        "MergeTableCellsRequestIn": "_slides_124_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_slides_125_MergeTableCellsRequestOut",
        "BatchUpdatePresentationResponseIn": "_slides_126_BatchUpdatePresentationResponseIn",
        "BatchUpdatePresentationResponseOut": "_slides_127_BatchUpdatePresentationResponseOut",
        "AffineTransformIn": "_slides_128_AffineTransformIn",
        "AffineTransformOut": "_slides_129_AffineTransformOut",
        "DeleteTableColumnRequestIn": "_slides_130_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_slides_131_DeleteTableColumnRequestOut",
        "CreateVideoRequestIn": "_slides_132_CreateVideoRequestIn",
        "CreateVideoRequestOut": "_slides_133_CreateVideoRequestOut",
        "UpdateImagePropertiesRequestIn": "_slides_134_UpdateImagePropertiesRequestIn",
        "UpdateImagePropertiesRequestOut": "_slides_135_UpdateImagePropertiesRequestOut",
        "ImageIn": "_slides_136_ImageIn",
        "ImageOut": "_slides_137_ImageOut",
        "SheetsChartPropertiesIn": "_slides_138_SheetsChartPropertiesIn",
        "SheetsChartPropertiesOut": "_slides_139_SheetsChartPropertiesOut",
        "ReplaceAllShapesWithImageResponseIn": "_slides_140_ReplaceAllShapesWithImageResponseIn",
        "ReplaceAllShapesWithImageResponseOut": "_slides_141_ReplaceAllShapesWithImageResponseOut",
        "ListIn": "_slides_142_ListIn",
        "ListOut": "_slides_143_ListOut",
        "CreateLineRequestIn": "_slides_144_CreateLineRequestIn",
        "CreateLineRequestOut": "_slides_145_CreateLineRequestOut",
        "BatchUpdatePresentationRequestIn": "_slides_146_BatchUpdatePresentationRequestIn",
        "BatchUpdatePresentationRequestOut": "_slides_147_BatchUpdatePresentationRequestOut",
        "UngroupObjectsRequestIn": "_slides_148_UngroupObjectsRequestIn",
        "UngroupObjectsRequestOut": "_slides_149_UngroupObjectsRequestOut",
        "CreateImageRequestIn": "_slides_150_CreateImageRequestIn",
        "CreateImageRequestOut": "_slides_151_CreateImageRequestOut",
        "DimensionIn": "_slides_152_DimensionIn",
        "DimensionOut": "_slides_153_DimensionOut",
        "TableRowPropertiesIn": "_slides_154_TableRowPropertiesIn",
        "TableRowPropertiesOut": "_slides_155_TableRowPropertiesOut",
        "ThumbnailIn": "_slides_156_ThumbnailIn",
        "ThumbnailOut": "_slides_157_ThumbnailOut",
        "LayoutPropertiesIn": "_slides_158_LayoutPropertiesIn",
        "LayoutPropertiesOut": "_slides_159_LayoutPropertiesOut",
        "UnmergeTableCellsRequestIn": "_slides_160_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_slides_161_UnmergeTableCellsRequestOut",
        "PresentationIn": "_slides_162_PresentationIn",
        "PresentationOut": "_slides_163_PresentationOut",
        "PageElementIn": "_slides_164_PageElementIn",
        "PageElementOut": "_slides_165_PageElementOut",
        "ShapeIn": "_slides_166_ShapeIn",
        "ShapeOut": "_slides_167_ShapeOut",
        "DeleteTextRequestIn": "_slides_168_DeleteTextRequestIn",
        "DeleteTextRequestOut": "_slides_169_DeleteTextRequestOut",
        "CreateParagraphBulletsRequestIn": "_slides_170_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_slides_171_CreateParagraphBulletsRequestOut",
        "ParagraphStyleIn": "_slides_172_ParagraphStyleIn",
        "ParagraphStyleOut": "_slides_173_ParagraphStyleOut",
        "CreateTableResponseIn": "_slides_174_CreateTableResponseIn",
        "CreateTableResponseOut": "_slides_175_CreateTableResponseOut",
        "VideoPropertiesIn": "_slides_176_VideoPropertiesIn",
        "VideoPropertiesOut": "_slides_177_VideoPropertiesOut",
        "ResponseIn": "_slides_178_ResponseIn",
        "ResponseOut": "_slides_179_ResponseOut",
        "LinkIn": "_slides_180_LinkIn",
        "LinkOut": "_slides_181_LinkOut",
        "ReplaceImageRequestIn": "_slides_182_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_slides_183_ReplaceImageRequestOut",
        "CreateTableRequestIn": "_slides_184_CreateTableRequestIn",
        "CreateTableRequestOut": "_slides_185_CreateTableRequestOut",
        "CreateSheetsChartRequestIn": "_slides_186_CreateSheetsChartRequestIn",
        "CreateSheetsChartRequestOut": "_slides_187_CreateSheetsChartRequestOut",
        "TextStyleIn": "_slides_188_TextStyleIn",
        "TextStyleOut": "_slides_189_TextStyleOut",
        "WeightedFontFamilyIn": "_slides_190_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_slides_191_WeightedFontFamilyOut",
        "TableBorderPropertiesIn": "_slides_192_TableBorderPropertiesIn",
        "TableBorderPropertiesOut": "_slides_193_TableBorderPropertiesOut",
        "TableRangeIn": "_slides_194_TableRangeIn",
        "TableRangeOut": "_slides_195_TableRangeOut",
        "CreateSheetsChartResponseIn": "_slides_196_CreateSheetsChartResponseIn",
        "CreateSheetsChartResponseOut": "_slides_197_CreateSheetsChartResponseOut",
        "LayoutPlaceholderIdMappingIn": "_slides_198_LayoutPlaceholderIdMappingIn",
        "LayoutPlaceholderIdMappingOut": "_slides_199_LayoutPlaceholderIdMappingOut",
        "UpdateParagraphStyleRequestIn": "_slides_200_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_slides_201_UpdateParagraphStyleRequestOut",
        "CropPropertiesIn": "_slides_202_CropPropertiesIn",
        "CropPropertiesOut": "_slides_203_CropPropertiesOut",
        "UpdateLinePropertiesRequestIn": "_slides_204_UpdateLinePropertiesRequestIn",
        "UpdateLinePropertiesRequestOut": "_slides_205_UpdateLinePropertiesRequestOut",
        "DuplicateObjectRequestIn": "_slides_206_DuplicateObjectRequestIn",
        "DuplicateObjectRequestOut": "_slides_207_DuplicateObjectRequestOut",
        "RgbColorIn": "_slides_208_RgbColorIn",
        "RgbColorOut": "_slides_209_RgbColorOut",
        "RefreshSheetsChartRequestIn": "_slides_210_RefreshSheetsChartRequestIn",
        "RefreshSheetsChartRequestOut": "_slides_211_RefreshSheetsChartRequestOut",
        "ReplaceAllShapesWithSheetsChartResponseIn": "_slides_212_ReplaceAllShapesWithSheetsChartResponseIn",
        "ReplaceAllShapesWithSheetsChartResponseOut": "_slides_213_ReplaceAllShapesWithSheetsChartResponseOut",
        "SizeIn": "_slides_214_SizeIn",
        "SizeOut": "_slides_215_SizeOut",
        "SolidFillIn": "_slides_216_SolidFillIn",
        "SolidFillOut": "_slides_217_SolidFillOut",
        "UpdateSlidesPositionRequestIn": "_slides_218_UpdateSlidesPositionRequestIn",
        "UpdateSlidesPositionRequestOut": "_slides_219_UpdateSlidesPositionRequestOut",
        "AutofitIn": "_slides_220_AutofitIn",
        "AutofitOut": "_slides_221_AutofitOut",
        "WriteControlIn": "_slides_222_WriteControlIn",
        "WriteControlOut": "_slides_223_WriteControlOut",
        "GroupObjectsRequestIn": "_slides_224_GroupObjectsRequestIn",
        "GroupObjectsRequestOut": "_slides_225_GroupObjectsRequestOut",
        "InsertTableColumnsRequestIn": "_slides_226_InsertTableColumnsRequestIn",
        "InsertTableColumnsRequestOut": "_slides_227_InsertTableColumnsRequestOut",
        "ColorSchemeIn": "_slides_228_ColorSchemeIn",
        "ColorSchemeOut": "_slides_229_ColorSchemeOut",
        "RecolorIn": "_slides_230_RecolorIn",
        "RecolorOut": "_slides_231_RecolorOut",
        "AutoTextIn": "_slides_232_AutoTextIn",
        "AutoTextOut": "_slides_233_AutoTextOut",
        "GroupObjectsResponseIn": "_slides_234_GroupObjectsResponseIn",
        "GroupObjectsResponseOut": "_slides_235_GroupObjectsResponseOut",
        "BulletIn": "_slides_236_BulletIn",
        "BulletOut": "_slides_237_BulletOut",
        "LinePropertiesIn": "_slides_238_LinePropertiesIn",
        "LinePropertiesOut": "_slides_239_LinePropertiesOut",
        "TableRowIn": "_slides_240_TableRowIn",
        "TableRowOut": "_slides_241_TableRowOut",
        "ReplaceAllTextResponseIn": "_slides_242_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_slides_243_ReplaceAllTextResponseOut",
        "PagePropertiesIn": "_slides_244_PagePropertiesIn",
        "PagePropertiesOut": "_slides_245_PagePropertiesOut",
        "SlidePropertiesIn": "_slides_246_SlidePropertiesIn",
        "SlidePropertiesOut": "_slides_247_SlidePropertiesOut",
        "SheetsChartIn": "_slides_248_SheetsChartIn",
        "SheetsChartOut": "_slides_249_SheetsChartOut",
        "CreateShapeResponseIn": "_slides_250_CreateShapeResponseIn",
        "CreateShapeResponseOut": "_slides_251_CreateShapeResponseOut",
        "UpdateTableColumnPropertiesRequestIn": "_slides_252_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_slides_253_UpdateTableColumnPropertiesRequestOut",
        "UpdateSlidePropertiesRequestIn": "_slides_254_UpdateSlidePropertiesRequestIn",
        "UpdateSlidePropertiesRequestOut": "_slides_255_UpdateSlidePropertiesRequestOut",
        "OptionalColorIn": "_slides_256_OptionalColorIn",
        "OptionalColorOut": "_slides_257_OptionalColorOut",
        "TableIn": "_slides_258_TableIn",
        "TableOut": "_slides_259_TableOut",
        "RequestIn": "_slides_260_RequestIn",
        "RequestOut": "_slides_261_RequestOut",
        "LineIn": "_slides_262_LineIn",
        "LineOut": "_slides_263_LineOut",
        "ReplaceAllShapesWithImageRequestIn": "_slides_264_ReplaceAllShapesWithImageRequestIn",
        "ReplaceAllShapesWithImageRequestOut": "_slides_265_ReplaceAllShapesWithImageRequestOut",
        "LineFillIn": "_slides_266_LineFillIn",
        "LineFillOut": "_slides_267_LineFillOut",
        "CreateShapeRequestIn": "_slides_268_CreateShapeRequestIn",
        "CreateShapeRequestOut": "_slides_269_CreateShapeRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TableBorderFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["TableBorderFillIn"])
    types["TableBorderFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableBorderFillOut"])
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
    types["UpdatePageElementTransformRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "applyMode": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
        }
    ).named(renames["UpdatePageElementTransformRequestIn"])
    types["UpdatePageElementTransformRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "applyMode": t.string().optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePageElementTransformRequestOut"])
    types["RerouteLineRequestIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["RerouteLineRequestIn"]
    )
    types["RerouteLineRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RerouteLineRequestOut"])
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
    types["ShadowIn"] = t.struct(
        {
            "color": t.proxy(renames["OpaqueColorIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "blurRadius": t.proxy(renames["DimensionIn"]).optional(),
            "rotateWithShape": t.boolean().optional(),
            "type": t.string().optional(),
            "alignment": t.string().optional(),
            "propertyState": t.string().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ShadowIn"])
    types["ShadowOut"] = t.struct(
        {
            "color": t.proxy(renames["OpaqueColorOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "blurRadius": t.proxy(renames["DimensionOut"]).optional(),
            "rotateWithShape": t.boolean().optional(),
            "type": t.string().optional(),
            "alignment": t.string().optional(),
            "propertyState": t.string().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadowOut"])
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
    types["TableCellIn"] = t.struct(
        {
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
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
    types["InsertTextRequestIn"] = t.struct(
        {
            "insertionIndex": t.integer().optional(),
            "text": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "insertionIndex": t.integer().optional(),
            "text": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
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
    types["GroupIn"] = t.struct(
        {"children": t.array(t.proxy(renames["PageElementIn"])).optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "children": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["MasterPropertiesIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["MasterPropertiesIn"])
    types["MasterPropertiesOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterPropertiesOut"])
    types["DeleteObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeleteObjectRequestIn"])
    types["DeleteObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteObjectRequestOut"])
    types["ReplaceAllShapesWithSheetsChartRequestIn"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "spreadsheetId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestIn"])
    types["ReplaceAllShapesWithSheetsChartRequestOut"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "spreadsheetId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "pageObjectIds": t.array(t.string()).optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartRequestOut"])
    types["PageIn"] = t.struct(
        {
            "notesProperties": t.proxy(renames["NotesPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesIn"]).optional(),
            "pageType": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesIn"]).optional(),
            "pageElements": t.array(t.proxy(renames["PageElementIn"])).optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "notesProperties": t.proxy(renames["NotesPropertiesOut"]).optional(),
            "objectId": t.string().optional(),
            "masterProperties": t.proxy(renames["MasterPropertiesOut"]).optional(),
            "pageType": t.string().optional(),
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "layoutProperties": t.proxy(renames["LayoutPropertiesOut"]).optional(),
            "pageElements": t.array(t.proxy(renames["PageElementOut"])).optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "revisionId": t.string().optional(),
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
    types["UpdateVideoPropertiesRequestIn"] = t.struct(
        {
            "videoProperties": t.proxy(renames["VideoPropertiesIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestIn"])
    types["UpdateVideoPropertiesRequestOut"] = t.struct(
        {
            "videoProperties": t.proxy(renames["VideoPropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateVideoPropertiesRequestOut"])
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
    types["OutlineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["OutlineFillIn"])
    types["OutlineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineFillOut"])
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
    types["ReplaceAllTextRequestIn"] = t.struct(
        {
            "pageObjectIds": t.array(t.string()).optional(),
            "replaceText": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
        }
    ).named(renames["ReplaceAllTextRequestIn"])
    types["ReplaceAllTextRequestOut"] = t.struct(
        {
            "pageObjectIds": t.array(t.string()).optional(),
            "replaceText": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextRequestOut"])
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
    types["UpdateTableCellPropertiesRequestIn"] = t.struct(
        {
            "tableCellProperties": t.proxy(renames["TableCellPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestIn"])
    types["UpdateTableCellPropertiesRequestOut"] = t.struct(
        {
            "tableCellProperties": t.proxy(
                renames["TableCellPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellPropertiesRequestOut"])
    types["ImagePropertiesIn"] = t.struct(
        {
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "contrast": t.number().optional(),
            "transparency": t.number().optional(),
            "brightness": t.number().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "recolor": t.proxy(renames["RecolorIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "contrast": t.number().optional(),
            "transparency": t.number().optional(),
            "brightness": t.number().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "recolor": t.proxy(renames["RecolorOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["UpdateTableBorderPropertiesRequestIn"] = t.struct(
        {
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesIn"]
            ).optional(),
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "borderPosition": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestIn"])
    types["UpdateTableBorderPropertiesRequestOut"] = t.struct(
        {
            "tableBorderProperties": t.proxy(
                renames["TableBorderPropertiesOut"]
            ).optional(),
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "borderPosition": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableBorderPropertiesRequestOut"])
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
    types["CreateImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateImageResponseIn"])
    types["CreateImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageResponseOut"])
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
    types["UpdateTableRowPropertiesRequestIn"] = t.struct(
        {
            "rowIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesIn"]).optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestIn"])
    types["UpdateTableRowPropertiesRequestOut"] = t.struct(
        {
            "rowIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "tableRowProperties": t.proxy(renames["TableRowPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowPropertiesRequestOut"])
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
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "style": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
    types["CreateLineResponseIn"] = t.struct({"objectId": t.string().optional()}).named(
        renames["CreateLineResponseIn"]
    )
    types["CreateLineResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLineResponseOut"])
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
    types["PageBackgroundFillIn"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillIn"]
            ).optional(),
            "solidFill": t.proxy(renames["SolidFillIn"]).optional(),
        }
    ).named(renames["PageBackgroundFillIn"])
    types["PageBackgroundFillOut"] = t.struct(
        {
            "propertyState": t.string().optional(),
            "stretchedPictureFill": t.proxy(
                renames["StretchedPictureFillOut"]
            ).optional(),
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBackgroundFillOut"])
    types["NestingLevelIn"] = t.struct(
        {"bulletStyle": t.proxy(renames["TextStyleIn"]).optional()}
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
    types["ShapePropertiesIn"] = t.struct(
        {
            "autofit": t.proxy(renames["AutofitIn"]).optional(),
            "shapeBackgroundFill": t.proxy(renames["ShapeBackgroundFillIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "contentAlignment": t.string().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "shadow": t.proxy(renames["ShadowIn"]).optional(),
        }
    ).named(renames["ShapePropertiesIn"])
    types["ShapePropertiesOut"] = t.struct(
        {
            "autofit": t.proxy(renames["AutofitOut"]).optional(),
            "shapeBackgroundFill": t.proxy(
                renames["ShapeBackgroundFillOut"]
            ).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "contentAlignment": t.string().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "shadow": t.proxy(renames["ShadowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapePropertiesOut"])
    types["TableColumnPropertiesIn"] = t.struct(
        {"columnWidth": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableColumnPropertiesIn"])
    types["TableColumnPropertiesOut"] = t.struct(
        {
            "columnWidth": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableColumnPropertiesOut"])
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
    types["CreateSlideResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSlideResponseIn"])
    types["CreateSlideResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideResponseOut"])
    types["InsertTableRowsRequestIn"] = t.struct(
        {
            "number": t.integer().optional(),
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "insertBelow": t.boolean().optional(),
        }
    ).named(renames["InsertTableRowsRequestIn"])
    types["InsertTableRowsRequestOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "tableObjectId": t.string().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "insertBelow": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRowsRequestOut"])
    types["DuplicateObjectResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DuplicateObjectResponseIn"])
    types["DuplicateObjectResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateObjectResponseOut"])
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
    types["WordArtIn"] = t.struct({"renderedText": t.string().optional()}).named(
        renames["WordArtIn"]
    )
    types["WordArtOut"] = t.struct(
        {
            "renderedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordArtOut"])
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
    types["NotesPropertiesIn"] = t.struct(
        {"speakerNotesObjectId": t.string().optional()}
    ).named(renames["NotesPropertiesIn"])
    types["NotesPropertiesOut"] = t.struct(
        {
            "speakerNotesObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotesPropertiesOut"])
    types["CreateVideoResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateVideoResponseIn"])
    types["CreateVideoResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVideoResponseOut"])
    types["UpdatePagePropertiesRequestIn"] = t.struct(
        {
            "pageProperties": t.proxy(renames["PagePropertiesIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestIn"])
    types["UpdatePagePropertiesRequestOut"] = t.struct(
        {
            "pageProperties": t.proxy(renames["PagePropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePagePropertiesRequestOut"])
    types["CreateSlideRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "insertionIndex": t.integer().optional(),
            "slideLayoutReference": t.proxy(renames["LayoutReferenceIn"]).optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingIn"])
            ).optional(),
        }
    ).named(renames["CreateSlideRequestIn"])
    types["CreateSlideRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "insertionIndex": t.integer().optional(),
            "slideLayoutReference": t.proxy(renames["LayoutReferenceOut"]).optional(),
            "placeholderIdMappings": t.array(
                t.proxy(renames["LayoutPlaceholderIdMappingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSlideRequestOut"])
    types["OutlineIn"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "propertyState": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillIn"]).optional(),
            "dashStyle": t.string().optional(),
        }
    ).named(renames["OutlineIn"])
    types["OutlineOut"] = t.struct(
        {
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "propertyState": t.string().optional(),
            "outlineFill": t.proxy(renames["OutlineFillOut"]).optional(),
            "dashStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutlineOut"])
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
    types["AffineTransformIn"] = t.struct(
        {
            "scaleX": t.number().optional(),
            "translateY": t.number().optional(),
            "unit": t.string().optional(),
            "shearX": t.number().optional(),
            "translateX": t.number().optional(),
            "scaleY": t.number().optional(),
            "shearY": t.number().optional(),
        }
    ).named(renames["AffineTransformIn"])
    types["AffineTransformOut"] = t.struct(
        {
            "scaleX": t.number().optional(),
            "translateY": t.number().optional(),
            "unit": t.string().optional(),
            "shearX": t.number().optional(),
            "translateX": t.number().optional(),
            "scaleY": t.number().optional(),
            "shearY": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AffineTransformOut"])
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
    types["SheetsChartPropertiesIn"] = t.struct(
        {"chartImageProperties": t.proxy(renames["ImagePropertiesIn"]).optional()}
    ).named(renames["SheetsChartPropertiesIn"])
    types["SheetsChartPropertiesOut"] = t.struct(
        {
            "chartImageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartPropertiesOut"])
    types["ReplaceAllShapesWithImageResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithImageResponseIn"])
    types["ReplaceAllShapesWithImageResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageResponseOut"])
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
    types["UngroupObjectsRequestIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["UngroupObjectsRequestIn"])
    types["UngroupObjectsRequestOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UngroupObjectsRequestOut"])
    types["CreateImageRequestIn"] = t.struct(
        {
            "url": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
        }
    ).named(renames["CreateImageRequestIn"])
    types["CreateImageRequestOut"] = t.struct(
        {
            "url": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateImageRequestOut"])
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
    types["TableRowPropertiesIn"] = t.struct(
        {"minRowHeight": t.proxy(renames["DimensionIn"]).optional()}
    ).named(renames["TableRowPropertiesIn"])
    types["TableRowPropertiesOut"] = t.struct(
        {
            "minRowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowPropertiesOut"])
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
    types["PresentationIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "notesMaster": t.proxy(renames["PageIn"]).optional(),
            "title": t.string().optional(),
            "layouts": t.array(t.proxy(renames["PageIn"])).optional(),
            "slides": t.array(t.proxy(renames["PageIn"])).optional(),
            "locale": t.string().optional(),
            "masters": t.array(t.proxy(renames["PageIn"])).optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "presentationId": t.string().optional(),
        }
    ).named(renames["PresentationIn"])
    types["PresentationOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "notesMaster": t.proxy(renames["PageOut"]).optional(),
            "title": t.string().optional(),
            "layouts": t.array(t.proxy(renames["PageOut"])).optional(),
            "slides": t.array(t.proxy(renames["PageOut"])).optional(),
            "locale": t.string().optional(),
            "masters": t.array(t.proxy(renames["PageOut"])).optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "presentationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationOut"])
    types["PageElementIn"] = t.struct(
        {
            "sheetsChart": t.proxy(renames["SheetsChartIn"]).optional(),
            "shape": t.proxy(renames["ShapeIn"]).optional(),
            "video": t.proxy(renames["VideoIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "objectId": t.string().optional(),
            "line": t.proxy(renames["LineIn"]).optional(),
            "elementGroup": t.proxy(renames["GroupIn"]).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "wordArt": t.proxy(renames["WordArtIn"]).optional(),
            "transform": t.proxy(renames["AffineTransformIn"]).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["PageElementIn"])
    types["PageElementOut"] = t.struct(
        {
            "sheetsChart": t.proxy(renames["SheetsChartOut"]).optional(),
            "shape": t.proxy(renames["ShapeOut"]).optional(),
            "video": t.proxy(renames["VideoOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "objectId": t.string().optional(),
            "line": t.proxy(renames["LineOut"]).optional(),
            "elementGroup": t.proxy(renames["GroupOut"]).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "wordArt": t.proxy(renames["WordArtOut"]).optional(),
            "transform": t.proxy(renames["AffineTransformOut"]).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageElementOut"])
    types["ShapeIn"] = t.struct(
        {
            "shapeType": t.string().optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesIn"]).optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "placeholder": t.proxy(renames["PlaceholderIn"]).optional(),
        }
    ).named(renames["ShapeIn"])
    types["ShapeOut"] = t.struct(
        {
            "shapeType": t.string().optional(),
            "shapeProperties": t.proxy(renames["ShapePropertiesOut"]).optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "placeholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShapeOut"])
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
    types["CreateParagraphBulletsRequestIn"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeIn"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "bulletPreset": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestIn"])
    types["CreateParagraphBulletsRequestOut"] = t.struct(
        {
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "bulletPreset": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "direction": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "lineSpacing": t.number().optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "alignment": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "spacingMode": t.string().optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "direction": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "lineSpacing": t.number().optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "alignment": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "spacingMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
    types["CreateTableResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateTableResponseIn"])
    types["CreateTableResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableResponseOut"])
    types["VideoPropertiesIn"] = t.struct(
        {
            "mute": t.boolean().optional(),
            "end": t.integer().optional(),
            "outline": t.proxy(renames["OutlineIn"]).optional(),
            "autoPlay": t.boolean().optional(),
            "start": t.integer().optional(),
        }
    ).named(renames["VideoPropertiesIn"])
    types["VideoPropertiesOut"] = t.struct(
        {
            "mute": t.boolean().optional(),
            "end": t.integer().optional(),
            "outline": t.proxy(renames["OutlineOut"]).optional(),
            "autoPlay": t.boolean().optional(),
            "start": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPropertiesOut"])
    types["ResponseIn"] = t.struct(
        {
            "createTable": t.proxy(renames["CreateTableResponseIn"]).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectResponseIn"]).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseIn"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseIn"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseIn"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseIn"]).optional(),
            "createLine": t.proxy(renames["CreateLineResponseIn"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseIn"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseIn"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseIn"]
            ).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "createTable": t.proxy(renames["CreateTableResponseOut"]).optional(),
            "duplicateObject": t.proxy(
                renames["DuplicateObjectResponseOut"]
            ).optional(),
            "createShape": t.proxy(renames["CreateShapeResponseOut"]).optional(),
            "createImage": t.proxy(renames["CreateImageResponseOut"]).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageResponseOut"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideResponseOut"]).optional(),
            "createLine": t.proxy(renames["CreateLineResponseOut"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartResponseOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "createVideo": t.proxy(renames["CreateVideoResponseOut"]).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsResponseOut"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["LinkIn"] = t.struct(
        {
            "url": t.string().optional(),
            "pageObjectId": t.string().optional(),
            "slideIndex": t.integer().optional(),
            "relativeLink": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "pageObjectId": t.string().optional(),
            "slideIndex": t.integer().optional(),
            "relativeLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
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
    types["CreateTableRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
        }
    ).named(renames["CreateTableRequestIn"])
    types["CreateTableRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableRequestOut"])
    types["CreateSheetsChartRequestIn"] = t.struct(
        {
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
            "objectId": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["CreateSheetsChartRequestIn"])
    types["CreateSheetsChartRequestOut"] = t.struct(
        {
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "linkingMode": t.string().optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartRequestOut"])
    types["TextStyleIn"] = t.struct(
        {
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "fontFamily": t.string().optional(),
            "italic": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "baselineOffset": t.string().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "bold": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "strikethrough": t.boolean().optional(),
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "fontFamily": t.string().optional(),
            "italic": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "baselineOffset": t.string().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "bold": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "strikethrough": t.boolean().optional(),
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
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
    types["TableRangeIn"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationIn"]).optional(),
            "rowSpan": t.integer().optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "location": t.proxy(renames["TableCellLocationOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
    types["CreateSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateSheetsChartResponseIn"])
    types["CreateSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSheetsChartResponseOut"])
    types["LayoutPlaceholderIdMappingIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "layoutPlaceholder": t.proxy(renames["PlaceholderIn"]).optional(),
            "layoutPlaceholderObjectId": t.string().optional(),
        }
    ).named(renames["LayoutPlaceholderIdMappingIn"])
    types["LayoutPlaceholderIdMappingOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "layoutPlaceholder": t.proxy(renames["PlaceholderOut"]).optional(),
            "layoutPlaceholderObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayoutPlaceholderIdMappingOut"])
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "style": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "textRange": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "style": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "textRange": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])
    types["CropPropertiesIn"] = t.struct(
        {
            "leftOffset": t.number().optional(),
            "angle": t.number().optional(),
            "rightOffset": t.number().optional(),
            "topOffset": t.number().optional(),
            "bottomOffset": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "leftOffset": t.number().optional(),
            "angle": t.number().optional(),
            "rightOffset": t.number().optional(),
            "topOffset": t.number().optional(),
            "bottomOffset": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
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
    types["RgbColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
        }
    ).named(renames["RgbColorIn"])
    types["RgbColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RgbColorOut"])
    types["RefreshSheetsChartRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["RefreshSheetsChartRequestIn"])
    types["RefreshSheetsChartRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshSheetsChartRequestOut"])
    types["ReplaceAllShapesWithSheetsChartResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseIn"])
    types["ReplaceAllShapesWithSheetsChartResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithSheetsChartResponseOut"])
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
    types["AutofitIn"] = t.struct(
        {
            "lineSpacingReduction": t.number().optional(),
            "fontScale": t.number().optional(),
            "autofitType": t.string().optional(),
        }
    ).named(renames["AutofitIn"])
    types["AutofitOut"] = t.struct(
        {
            "lineSpacingReduction": t.number().optional(),
            "fontScale": t.number().optional(),
            "autofitType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutofitOut"])
    types["WriteControlIn"] = t.struct(
        {"requiredRevisionId": t.string().optional()}
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
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
    types["InsertTableColumnsRequestIn"] = t.struct(
        {
            "insertRight": t.boolean().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "number": t.integer().optional(),
            "tableObjectId": t.string().optional(),
        }
    ).named(renames["InsertTableColumnsRequestIn"])
    types["InsertTableColumnsRequestOut"] = t.struct(
        {
            "insertRight": t.boolean().optional(),
            "cellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "number": t.integer().optional(),
            "tableObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableColumnsRequestOut"])
    types["ColorSchemeIn"] = t.struct(
        {"colors": t.array(t.proxy(renames["ThemeColorPairIn"])).optional()}
    ).named(renames["ColorSchemeIn"])
    types["ColorSchemeOut"] = t.struct(
        {
            "colors": t.array(t.proxy(renames["ThemeColorPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorSchemeOut"])
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
    types["AutoTextIn"] = t.struct(
        {
            "style": t.proxy(renames["TextStyleIn"]).optional(),
            "type": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "style": t.proxy(renames["TextStyleOut"]).optional(),
            "type": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
    types["GroupObjectsResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["GroupObjectsResponseIn"])
    types["GroupObjectsResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupObjectsResponseOut"])
    types["BulletIn"] = t.struct(
        {
            "glyph": t.string().optional(),
            "bulletStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "nestingLevel": t.integer().optional(),
            "listId": t.string().optional(),
        }
    ).named(renames["BulletIn"])
    types["BulletOut"] = t.struct(
        {
            "glyph": t.string().optional(),
            "bulletStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "nestingLevel": t.integer().optional(),
            "listId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletOut"])
    types["LinePropertiesIn"] = t.struct(
        {
            "link": t.proxy(renames["LinkIn"]).optional(),
            "lineFill": t.proxy(renames["LineFillIn"]).optional(),
            "weight": t.proxy(renames["DimensionIn"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "dashStyle": t.string().optional(),
            "startConnection": t.proxy(renames["LineConnectionIn"]).optional(),
            "endArrow": t.string().optional(),
            "startArrow": t.string().optional(),
        }
    ).named(renames["LinePropertiesIn"])
    types["LinePropertiesOut"] = t.struct(
        {
            "link": t.proxy(renames["LinkOut"]).optional(),
            "lineFill": t.proxy(renames["LineFillOut"]).optional(),
            "weight": t.proxy(renames["DimensionOut"]).optional(),
            "endConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "startConnection": t.proxy(renames["LineConnectionOut"]).optional(),
            "endArrow": t.string().optional(),
            "startArrow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinePropertiesOut"])
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
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
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
    types["SlidePropertiesIn"] = t.struct(
        {
            "layoutObjectId": t.string().optional(),
            "masterObjectId": t.string().optional(),
            "isSkipped": t.boolean().optional(),
            "notesPage": t.proxy(renames["PageIn"]).optional(),
        }
    ).named(renames["SlidePropertiesIn"])
    types["SlidePropertiesOut"] = t.struct(
        {
            "layoutObjectId": t.string().optional(),
            "masterObjectId": t.string().optional(),
            "isSkipped": t.boolean().optional(),
            "notesPage": t.proxy(renames["PageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlidePropertiesOut"])
    types["SheetsChartIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "chartId": t.integer().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesIn"]
            ).optional(),
            "contentUrl": t.string().optional(),
        }
    ).named(renames["SheetsChartIn"])
    types["SheetsChartOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "chartId": t.integer().optional(),
            "sheetsChartProperties": t.proxy(
                renames["SheetsChartPropertiesOut"]
            ).optional(),
            "contentUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartOut"])
    types["CreateShapeResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["CreateShapeResponseIn"])
    types["CreateShapeResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeResponseOut"])
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["UpdateSlidePropertiesRequestIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesIn"]).optional(),
        }
    ).named(renames["UpdateSlidePropertiesRequestIn"])
    types["UpdateSlidePropertiesRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "fields": t.string().optional(),
            "slideProperties": t.proxy(renames["SlidePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlidePropertiesRequestOut"])
    types["OptionalColorIn"] = t.struct(
        {"opaqueColor": t.proxy(renames["OpaqueColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "opaqueColor": t.proxy(renames["OpaqueColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
    types["TableIn"] = t.struct(
        {
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesIn"])
            ).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowIn"])
            ).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "tableColumns": t.array(
                t.proxy(renames["TableColumnPropertiesOut"])
            ).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "verticalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "horizontalBorderRows": t.array(
                t.proxy(renames["TableBorderRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["RequestIn"] = t.struct(
        {
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestIn"]).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestIn"]).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestIn"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestIn"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestIn"]
            ).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestIn"]
            ).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestIn"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestIn"]).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestIn"]
            ).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestIn"]
            ).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestIn"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestIn"]
            ).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestIn"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestIn"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestIn"]).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestIn"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestIn"]
            ).optional(),
            "createTable": t.proxy(renames["CreateTableRequestIn"]).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestIn"]).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestIn"]).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestIn"]).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestIn"]).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestIn"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestIn"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestIn"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestIn"]
            ).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestIn"]).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestIn"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestIn"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestIn"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "groupObjects": t.proxy(renames["GroupObjectsRequestOut"]).optional(),
            "insertTableRows": t.proxy(renames["InsertTableRowsRequestOut"]).optional(),
            "rerouteLine": t.proxy(renames["RerouteLineRequestOut"]).optional(),
            "replaceAllShapesWithSheetsChart": t.proxy(
                renames["ReplaceAllShapesWithSheetsChartRequestOut"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "updateTableBorderProperties": t.proxy(
                renames["UpdateTableBorderPropertiesRequestOut"]
            ).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "updatePageProperties": t.proxy(
                renames["UpdatePagePropertiesRequestOut"]
            ).optional(),
            "insertTableColumns": t.proxy(
                renames["InsertTableColumnsRequestOut"]
            ).optional(),
            "createImage": t.proxy(renames["CreateImageRequestOut"]).optional(),
            "updateLineProperties": t.proxy(
                renames["UpdateLinePropertiesRequestOut"]
            ).optional(),
            "updateVideoProperties": t.proxy(
                renames["UpdateVideoPropertiesRequestOut"]
            ).optional(),
            "updateTableRowProperties": t.proxy(
                renames["UpdateTableRowPropertiesRequestOut"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "refreshSheetsChart": t.proxy(
                renames["RefreshSheetsChartRequestOut"]
            ).optional(),
            "updatePageElementsZOrder": t.proxy(
                renames["UpdatePageElementsZOrderRequestOut"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "updatePageElementTransform": t.proxy(
                renames["UpdatePageElementTransformRequestOut"]
            ).optional(),
            "createLine": t.proxy(renames["CreateLineRequestOut"]).optional(),
            "updateSlideProperties": t.proxy(
                renames["UpdateSlidePropertiesRequestOut"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "updateSlidesPosition": t.proxy(
                renames["UpdateSlidesPositionRequestOut"]
            ).optional(),
            "createTable": t.proxy(renames["CreateTableRequestOut"]).optional(),
            "deleteObject": t.proxy(renames["DeleteObjectRequestOut"]).optional(),
            "deleteText": t.proxy(renames["DeleteTextRequestOut"]).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "duplicateObject": t.proxy(renames["DuplicateObjectRequestOut"]).optional(),
            "createShape": t.proxy(renames["CreateShapeRequestOut"]).optional(),
            "updateImageProperties": t.proxy(
                renames["UpdateImagePropertiesRequestOut"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "ungroupObjects": t.proxy(renames["UngroupObjectsRequestOut"]).optional(),
            "updateTableCellProperties": t.proxy(
                renames["UpdateTableCellPropertiesRequestOut"]
            ).optional(),
            "updateLineCategory": t.proxy(
                renames["UpdateLineCategoryRequestOut"]
            ).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "createSlide": t.proxy(renames["CreateSlideRequestOut"]).optional(),
            "updateShapeProperties": t.proxy(
                renames["UpdateShapePropertiesRequestOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "updatePageElementAltText": t.proxy(
                renames["UpdatePageElementAltTextRequestOut"]
            ).optional(),
            "replaceAllShapesWithImage": t.proxy(
                renames["ReplaceAllShapesWithImageRequestOut"]
            ).optional(),
            "createVideo": t.proxy(renames["CreateVideoRequestOut"]).optional(),
            "createSheetsChart": t.proxy(
                renames["CreateSheetsChartRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["LineIn"] = t.struct(
        {
            "lineType": t.string().optional(),
            "lineCategory": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesIn"]).optional(),
        }
    ).named(renames["LineIn"])
    types["LineOut"] = t.struct(
        {
            "lineType": t.string().optional(),
            "lineCategory": t.string().optional(),
            "lineProperties": t.proxy(renames["LinePropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineOut"])
    types["ReplaceAllShapesWithImageRequestIn"] = t.struct(
        {
            "pageObjectIds": t.array(t.string()).optional(),
            "replaceMethod": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "imageReplaceMethod": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestIn"])
    types["ReplaceAllShapesWithImageRequestOut"] = t.struct(
        {
            "pageObjectIds": t.array(t.string()).optional(),
            "replaceMethod": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "imageReplaceMethod": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllShapesWithImageRequestOut"])
    types["LineFillIn"] = t.struct(
        {"solidFill": t.proxy(renames["SolidFillIn"]).optional()}
    ).named(renames["LineFillIn"])
    types["LineFillOut"] = t.struct(
        {
            "solidFill": t.proxy(renames["SolidFillOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineFillOut"])
    types["CreateShapeRequestIn"] = t.struct(
        {
            "shapeType": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(renames["PageElementPropertiesIn"]).optional(),
        }
    ).named(renames["CreateShapeRequestIn"])
    types["CreateShapeRequestOut"] = t.struct(
        {
            "shapeType": t.string().optional(),
            "objectId": t.string().optional(),
            "elementProperties": t.proxy(
                renames["PageElementPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShapeRequestOut"])

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
    functions["presentationsPagesGet"] = slides.get(
        "v1/presentations/{presentationId}/pages/{pageObjectId}/thumbnail",
        t.struct(
            {
                "thumbnailProperties.thumbnailSize": t.string().optional(),
                "presentationId": t.string().optional(),
                "thumbnailProperties.mimeType": t.string().optional(),
                "pageObjectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThumbnailOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["presentationsPagesGetThumbnail"] = slides.get(
        "v1/presentations/{presentationId}/pages/{pageObjectId}/thumbnail",
        t.struct(
            {
                "thumbnailProperties.thumbnailSize": t.string().optional(),
                "presentationId": t.string().optional(),
                "thumbnailProperties.mimeType": t.string().optional(),
                "pageObjectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThumbnailOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="slides", renames=renames, types=types, functions=functions)
