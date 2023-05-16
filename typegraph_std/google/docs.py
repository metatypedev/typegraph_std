from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_docs() -> Import:
    docs = HTTPRuntime("https://docs.googleapis.com/")

    renames = {
        "ErrorResponse": "_docs_1_ErrorResponse",
        "NestingLevelSuggestionStateIn": "_docs_2_NestingLevelSuggestionStateIn",
        "NestingLevelSuggestionStateOut": "_docs_3_NestingLevelSuggestionStateOut",
        "ImagePropertiesSuggestionStateIn": "_docs_4_ImagePropertiesSuggestionStateIn",
        "ImagePropertiesSuggestionStateOut": "_docs_5_ImagePropertiesSuggestionStateOut",
        "InlineObjectElementIn": "_docs_6_InlineObjectElementIn",
        "InlineObjectElementOut": "_docs_7_InlineObjectElementOut",
        "DimensionIn": "_docs_8_DimensionIn",
        "DimensionOut": "_docs_9_DimensionOut",
        "InsertTextRequestIn": "_docs_10_InsertTextRequestIn",
        "InsertTextRequestOut": "_docs_11_InsertTextRequestOut",
        "NamedStyleIn": "_docs_12_NamedStyleIn",
        "NamedStyleOut": "_docs_13_NamedStyleOut",
        "LinkedContentReferenceIn": "_docs_14_LinkedContentReferenceIn",
        "LinkedContentReferenceOut": "_docs_15_LinkedContentReferenceOut",
        "ReplaceAllTextRequestIn": "_docs_16_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_docs_17_ReplaceAllTextRequestOut",
        "DocumentStyleIn": "_docs_18_DocumentStyleIn",
        "DocumentStyleOut": "_docs_19_DocumentStyleOut",
        "FootnoteReferenceIn": "_docs_20_FootnoteReferenceIn",
        "FootnoteReferenceOut": "_docs_21_FootnoteReferenceOut",
        "InsertInlineSheetsChartResponseIn": "_docs_22_InsertInlineSheetsChartResponseIn",
        "InsertInlineSheetsChartResponseOut": "_docs_23_InsertInlineSheetsChartResponseOut",
        "CreateNamedRangeResponseIn": "_docs_24_CreateNamedRangeResponseIn",
        "CreateNamedRangeResponseOut": "_docs_25_CreateNamedRangeResponseOut",
        "DocumentIn": "_docs_26_DocumentIn",
        "DocumentOut": "_docs_27_DocumentOut",
        "TableRowStyleIn": "_docs_28_TableRowStyleIn",
        "TableRowStyleOut": "_docs_29_TableRowStyleOut",
        "SuggestedListPropertiesIn": "_docs_30_SuggestedListPropertiesIn",
        "SuggestedListPropertiesOut": "_docs_31_SuggestedListPropertiesOut",
        "ObjectReferencesIn": "_docs_32_ObjectReferencesIn",
        "ObjectReferencesOut": "_docs_33_ObjectReferencesOut",
        "CreateFooterResponseIn": "_docs_34_CreateFooterResponseIn",
        "CreateFooterResponseOut": "_docs_35_CreateFooterResponseOut",
        "CropPropertiesIn": "_docs_36_CropPropertiesIn",
        "CropPropertiesOut": "_docs_37_CropPropertiesOut",
        "SuggestedPositionedObjectPropertiesIn": "_docs_38_SuggestedPositionedObjectPropertiesIn",
        "SuggestedPositionedObjectPropertiesOut": "_docs_39_SuggestedPositionedObjectPropertiesOut",
        "ColumnBreakIn": "_docs_40_ColumnBreakIn",
        "ColumnBreakOut": "_docs_41_ColumnBreakOut",
        "BulletSuggestionStateIn": "_docs_42_BulletSuggestionStateIn",
        "BulletSuggestionStateOut": "_docs_43_BulletSuggestionStateOut",
        "ParagraphBorderIn": "_docs_44_ParagraphBorderIn",
        "ParagraphBorderOut": "_docs_45_ParagraphBorderOut",
        "ResponseIn": "_docs_46_ResponseIn",
        "ResponseOut": "_docs_47_ResponseOut",
        "TextStyleSuggestionStateIn": "_docs_48_TextStyleSuggestionStateIn",
        "TextStyleSuggestionStateOut": "_docs_49_TextStyleSuggestionStateOut",
        "CreateParagraphBulletsRequestIn": "_docs_50_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_docs_51_CreateParagraphBulletsRequestOut",
        "SectionColumnPropertiesIn": "_docs_52_SectionColumnPropertiesIn",
        "SectionColumnPropertiesOut": "_docs_53_SectionColumnPropertiesOut",
        "UpdateSectionStyleRequestIn": "_docs_54_UpdateSectionStyleRequestIn",
        "UpdateSectionStyleRequestOut": "_docs_55_UpdateSectionStyleRequestOut",
        "SubstringMatchCriteriaIn": "_docs_56_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_docs_57_SubstringMatchCriteriaOut",
        "RangeIn": "_docs_58_RangeIn",
        "RangeOut": "_docs_59_RangeOut",
        "InsertTableColumnRequestIn": "_docs_60_InsertTableColumnRequestIn",
        "InsertTableColumnRequestOut": "_docs_61_InsertTableColumnRequestOut",
        "EndOfSegmentLocationIn": "_docs_62_EndOfSegmentLocationIn",
        "EndOfSegmentLocationOut": "_docs_63_EndOfSegmentLocationOut",
        "EmbeddedDrawingPropertiesSuggestionStateIn": "_docs_64_EmbeddedDrawingPropertiesSuggestionStateIn",
        "EmbeddedDrawingPropertiesSuggestionStateOut": "_docs_65_EmbeddedDrawingPropertiesSuggestionStateOut",
        "UpdateParagraphStyleRequestIn": "_docs_66_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_docs_67_UpdateParagraphStyleRequestOut",
        "ReplaceAllTextResponseIn": "_docs_68_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_docs_69_ReplaceAllTextResponseOut",
        "PersonIn": "_docs_70_PersonIn",
        "PersonOut": "_docs_71_PersonOut",
        "NamedRangesIn": "_docs_72_NamedRangesIn",
        "NamedRangesOut": "_docs_73_NamedRangesOut",
        "TableCellBorderIn": "_docs_74_TableCellBorderIn",
        "TableCellBorderOut": "_docs_75_TableCellBorderOut",
        "TableCellStyleIn": "_docs_76_TableCellStyleIn",
        "TableCellStyleOut": "_docs_77_TableCellStyleOut",
        "TableCellStyleSuggestionStateIn": "_docs_78_TableCellStyleSuggestionStateIn",
        "TableCellStyleSuggestionStateOut": "_docs_79_TableCellStyleSuggestionStateOut",
        "SectionBreakIn": "_docs_80_SectionBreakIn",
        "SectionBreakOut": "_docs_81_SectionBreakOut",
        "UpdateDocumentStyleRequestIn": "_docs_82_UpdateDocumentStyleRequestIn",
        "UpdateDocumentStyleRequestOut": "_docs_83_UpdateDocumentStyleRequestOut",
        "PositionedObjectPropertiesSuggestionStateIn": "_docs_84_PositionedObjectPropertiesSuggestionStateIn",
        "PositionedObjectPropertiesSuggestionStateOut": "_docs_85_PositionedObjectPropertiesSuggestionStateOut",
        "FootnoteIn": "_docs_86_FootnoteIn",
        "FootnoteOut": "_docs_87_FootnoteOut",
        "InsertSectionBreakRequestIn": "_docs_88_InsertSectionBreakRequestIn",
        "InsertSectionBreakRequestOut": "_docs_89_InsertSectionBreakRequestOut",
        "TableStyleIn": "_docs_90_TableStyleIn",
        "TableStyleOut": "_docs_91_TableStyleOut",
        "SuggestedDocumentStyleIn": "_docs_92_SuggestedDocumentStyleIn",
        "SuggestedDocumentStyleOut": "_docs_93_SuggestedDocumentStyleOut",
        "TableIn": "_docs_94_TableIn",
        "TableOut": "_docs_95_TableOut",
        "TableColumnPropertiesIn": "_docs_96_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_docs_97_TableColumnPropertiesOut",
        "CreateFooterRequestIn": "_docs_98_CreateFooterRequestIn",
        "CreateFooterRequestOut": "_docs_99_CreateFooterRequestOut",
        "BodyIn": "_docs_100_BodyIn",
        "BodyOut": "_docs_101_BodyOut",
        "TableRangeIn": "_docs_102_TableRangeIn",
        "TableRangeOut": "_docs_103_TableRangeOut",
        "ShadingSuggestionStateIn": "_docs_104_ShadingSuggestionStateIn",
        "ShadingSuggestionStateOut": "_docs_105_ShadingSuggestionStateOut",
        "EmbeddedObjectSuggestionStateIn": "_docs_106_EmbeddedObjectSuggestionStateIn",
        "EmbeddedObjectSuggestionStateOut": "_docs_107_EmbeddedObjectSuggestionStateOut",
        "BackgroundIn": "_docs_108_BackgroundIn",
        "BackgroundOut": "_docs_109_BackgroundOut",
        "PageBreakIn": "_docs_110_PageBreakIn",
        "PageBreakOut": "_docs_111_PageBreakOut",
        "SizeIn": "_docs_112_SizeIn",
        "SizeOut": "_docs_113_SizeOut",
        "SuggestedTextStyleIn": "_docs_114_SuggestedTextStyleIn",
        "SuggestedTextStyleOut": "_docs_115_SuggestedTextStyleOut",
        "BatchUpdateDocumentResponseIn": "_docs_116_BatchUpdateDocumentResponseIn",
        "BatchUpdateDocumentResponseOut": "_docs_117_BatchUpdateDocumentResponseOut",
        "ListPropertiesSuggestionStateIn": "_docs_118_ListPropertiesSuggestionStateIn",
        "ListPropertiesSuggestionStateOut": "_docs_119_ListPropertiesSuggestionStateOut",
        "RichLinkPropertiesIn": "_docs_120_RichLinkPropertiesIn",
        "RichLinkPropertiesOut": "_docs_121_RichLinkPropertiesOut",
        "ReplaceNamedRangeContentRequestIn": "_docs_122_ReplaceNamedRangeContentRequestIn",
        "ReplaceNamedRangeContentRequestOut": "_docs_123_ReplaceNamedRangeContentRequestOut",
        "RichLinkIn": "_docs_124_RichLinkIn",
        "RichLinkOut": "_docs_125_RichLinkOut",
        "FooterIn": "_docs_126_FooterIn",
        "FooterOut": "_docs_127_FooterOut",
        "HeaderIn": "_docs_128_HeaderIn",
        "HeaderOut": "_docs_129_HeaderOut",
        "PositionedObjectPositioningIn": "_docs_130_PositionedObjectPositioningIn",
        "PositionedObjectPositioningOut": "_docs_131_PositionedObjectPositioningOut",
        "SizeSuggestionStateIn": "_docs_132_SizeSuggestionStateIn",
        "SizeSuggestionStateOut": "_docs_133_SizeSuggestionStateOut",
        "PinTableHeaderRowsRequestIn": "_docs_134_PinTableHeaderRowsRequestIn",
        "PinTableHeaderRowsRequestOut": "_docs_135_PinTableHeaderRowsRequestOut",
        "BulletIn": "_docs_136_BulletIn",
        "BulletOut": "_docs_137_BulletOut",
        "LocationIn": "_docs_138_LocationIn",
        "LocationOut": "_docs_139_LocationOut",
        "PositionedObjectIn": "_docs_140_PositionedObjectIn",
        "PositionedObjectOut": "_docs_141_PositionedObjectOut",
        "EmbeddedDrawingPropertiesIn": "_docs_142_EmbeddedDrawingPropertiesIn",
        "EmbeddedDrawingPropertiesOut": "_docs_143_EmbeddedDrawingPropertiesOut",
        "CreateFootnoteResponseIn": "_docs_144_CreateFootnoteResponseIn",
        "CreateFootnoteResponseOut": "_docs_145_CreateFootnoteResponseOut",
        "CropPropertiesSuggestionStateIn": "_docs_146_CropPropertiesSuggestionStateIn",
        "CropPropertiesSuggestionStateOut": "_docs_147_CropPropertiesSuggestionStateOut",
        "InsertInlineImageResponseIn": "_docs_148_InsertInlineImageResponseIn",
        "InsertInlineImageResponseOut": "_docs_149_InsertInlineImageResponseOut",
        "NamedStyleSuggestionStateIn": "_docs_150_NamedStyleSuggestionStateIn",
        "NamedStyleSuggestionStateOut": "_docs_151_NamedStyleSuggestionStateOut",
        "LinkIn": "_docs_152_LinkIn",
        "LinkOut": "_docs_153_LinkOut",
        "TabStopIn": "_docs_154_TabStopIn",
        "TabStopOut": "_docs_155_TabStopOut",
        "CreateFootnoteRequestIn": "_docs_156_CreateFootnoteRequestIn",
        "CreateFootnoteRequestOut": "_docs_157_CreateFootnoteRequestOut",
        "TableCellIn": "_docs_158_TableCellIn",
        "TableCellOut": "_docs_159_TableCellOut",
        "EmbeddedObjectIn": "_docs_160_EmbeddedObjectIn",
        "EmbeddedObjectOut": "_docs_161_EmbeddedObjectOut",
        "InsertPageBreakRequestIn": "_docs_162_InsertPageBreakRequestIn",
        "InsertPageBreakRequestOut": "_docs_163_InsertPageBreakRequestOut",
        "DeleteParagraphBulletsRequestIn": "_docs_164_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_docs_165_DeleteParagraphBulletsRequestOut",
        "UpdateTableCellStyleRequestIn": "_docs_166_UpdateTableCellStyleRequestIn",
        "UpdateTableCellStyleRequestOut": "_docs_167_UpdateTableCellStyleRequestOut",
        "CreateHeaderRequestIn": "_docs_168_CreateHeaderRequestIn",
        "CreateHeaderRequestOut": "_docs_169_CreateHeaderRequestOut",
        "DeleteTableColumnRequestIn": "_docs_170_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_docs_171_DeleteTableColumnRequestOut",
        "NamedStylesIn": "_docs_172_NamedStylesIn",
        "NamedStylesOut": "_docs_173_NamedStylesOut",
        "UpdateTableRowStyleRequestIn": "_docs_174_UpdateTableRowStyleRequestIn",
        "UpdateTableRowStyleRequestOut": "_docs_175_UpdateTableRowStyleRequestOut",
        "SuggestedNamedStylesIn": "_docs_176_SuggestedNamedStylesIn",
        "SuggestedNamedStylesOut": "_docs_177_SuggestedNamedStylesOut",
        "PositionedObjectPropertiesIn": "_docs_178_PositionedObjectPropertiesIn",
        "PositionedObjectPropertiesOut": "_docs_179_PositionedObjectPropertiesOut",
        "WriteControlIn": "_docs_180_WriteControlIn",
        "WriteControlOut": "_docs_181_WriteControlOut",
        "PersonPropertiesIn": "_docs_182_PersonPropertiesIn",
        "PersonPropertiesOut": "_docs_183_PersonPropertiesOut",
        "ListIn": "_docs_184_ListIn",
        "ListOut": "_docs_185_ListOut",
        "MergeTableCellsRequestIn": "_docs_186_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_docs_187_MergeTableCellsRequestOut",
        "NamedStylesSuggestionStateIn": "_docs_188_NamedStylesSuggestionStateIn",
        "NamedStylesSuggestionStateOut": "_docs_189_NamedStylesSuggestionStateOut",
        "OptionalColorIn": "_docs_190_OptionalColorIn",
        "OptionalColorOut": "_docs_191_OptionalColorOut",
        "DocumentStyleSuggestionStateIn": "_docs_192_DocumentStyleSuggestionStateIn",
        "DocumentStyleSuggestionStateOut": "_docs_193_DocumentStyleSuggestionStateOut",
        "EmbeddedObjectBorderSuggestionStateIn": "_docs_194_EmbeddedObjectBorderSuggestionStateIn",
        "EmbeddedObjectBorderSuggestionStateOut": "_docs_195_EmbeddedObjectBorderSuggestionStateOut",
        "DeleteHeaderRequestIn": "_docs_196_DeleteHeaderRequestIn",
        "DeleteHeaderRequestOut": "_docs_197_DeleteHeaderRequestOut",
        "NestingLevelIn": "_docs_198_NestingLevelIn",
        "NestingLevelOut": "_docs_199_NestingLevelOut",
        "SuggestedTableRowStyleIn": "_docs_200_SuggestedTableRowStyleIn",
        "SuggestedTableRowStyleOut": "_docs_201_SuggestedTableRowStyleOut",
        "NamedRangeIn": "_docs_202_NamedRangeIn",
        "NamedRangeOut": "_docs_203_NamedRangeOut",
        "LinkedContentReferenceSuggestionStateIn": "_docs_204_LinkedContentReferenceSuggestionStateIn",
        "LinkedContentReferenceSuggestionStateOut": "_docs_205_LinkedContentReferenceSuggestionStateOut",
        "ParagraphIn": "_docs_206_ParagraphIn",
        "ParagraphOut": "_docs_207_ParagraphOut",
        "InlineObjectPropertiesIn": "_docs_208_InlineObjectPropertiesIn",
        "InlineObjectPropertiesOut": "_docs_209_InlineObjectPropertiesOut",
        "ParagraphElementIn": "_docs_210_ParagraphElementIn",
        "ParagraphElementOut": "_docs_211_ParagraphElementOut",
        "EmbeddedObjectBorderIn": "_docs_212_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_docs_213_EmbeddedObjectBorderOut",
        "DeleteFooterRequestIn": "_docs_214_DeleteFooterRequestIn",
        "DeleteFooterRequestOut": "_docs_215_DeleteFooterRequestOut",
        "CreateHeaderResponseIn": "_docs_216_CreateHeaderResponseIn",
        "CreateHeaderResponseOut": "_docs_217_CreateHeaderResponseOut",
        "SectionStyleIn": "_docs_218_SectionStyleIn",
        "SectionStyleOut": "_docs_219_SectionStyleOut",
        "ColorIn": "_docs_220_ColorIn",
        "ColorOut": "_docs_221_ColorOut",
        "SuggestedInlineObjectPropertiesIn": "_docs_222_SuggestedInlineObjectPropertiesIn",
        "SuggestedInlineObjectPropertiesOut": "_docs_223_SuggestedInlineObjectPropertiesOut",
        "StructuralElementIn": "_docs_224_StructuralElementIn",
        "StructuralElementOut": "_docs_225_StructuralElementOut",
        "BatchUpdateDocumentRequestIn": "_docs_226_BatchUpdateDocumentRequestIn",
        "BatchUpdateDocumentRequestOut": "_docs_227_BatchUpdateDocumentRequestOut",
        "SheetsChartReferenceSuggestionStateIn": "_docs_228_SheetsChartReferenceSuggestionStateIn",
        "SheetsChartReferenceSuggestionStateOut": "_docs_229_SheetsChartReferenceSuggestionStateOut",
        "DeleteContentRangeRequestIn": "_docs_230_DeleteContentRangeRequestIn",
        "DeleteContentRangeRequestOut": "_docs_231_DeleteContentRangeRequestOut",
        "SuggestedTableCellStyleIn": "_docs_232_SuggestedTableCellStyleIn",
        "SuggestedTableCellStyleOut": "_docs_233_SuggestedTableCellStyleOut",
        "UpdateTextStyleRequestIn": "_docs_234_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_docs_235_UpdateTextStyleRequestOut",
        "InlineObjectPropertiesSuggestionStateIn": "_docs_236_InlineObjectPropertiesSuggestionStateIn",
        "InlineObjectPropertiesSuggestionStateOut": "_docs_237_InlineObjectPropertiesSuggestionStateOut",
        "TableRowIn": "_docs_238_TableRowIn",
        "TableRowOut": "_docs_239_TableRowOut",
        "SheetsChartReferenceIn": "_docs_240_SheetsChartReferenceIn",
        "SheetsChartReferenceOut": "_docs_241_SheetsChartReferenceOut",
        "InsertTableRequestIn": "_docs_242_InsertTableRequestIn",
        "InsertTableRequestOut": "_docs_243_InsertTableRequestOut",
        "ImagePropertiesIn": "_docs_244_ImagePropertiesIn",
        "ImagePropertiesOut": "_docs_245_ImagePropertiesOut",
        "HorizontalRuleIn": "_docs_246_HorizontalRuleIn",
        "HorizontalRuleOut": "_docs_247_HorizontalRuleOut",
        "DeleteTableRowRequestIn": "_docs_248_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_docs_249_DeleteTableRowRequestOut",
        "CreateNamedRangeRequestIn": "_docs_250_CreateNamedRangeRequestIn",
        "CreateNamedRangeRequestOut": "_docs_251_CreateNamedRangeRequestOut",
        "TableOfContentsIn": "_docs_252_TableOfContentsIn",
        "TableOfContentsOut": "_docs_253_TableOfContentsOut",
        "PositionedObjectPositioningSuggestionStateIn": "_docs_254_PositionedObjectPositioningSuggestionStateIn",
        "PositionedObjectPositioningSuggestionStateOut": "_docs_255_PositionedObjectPositioningSuggestionStateOut",
        "BackgroundSuggestionStateIn": "_docs_256_BackgroundSuggestionStateIn",
        "BackgroundSuggestionStateOut": "_docs_257_BackgroundSuggestionStateOut",
        "ShadingIn": "_docs_258_ShadingIn",
        "ShadingOut": "_docs_259_ShadingOut",
        "InlineObjectIn": "_docs_260_InlineObjectIn",
        "InlineObjectOut": "_docs_261_InlineObjectOut",
        "ReplaceImageRequestIn": "_docs_262_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_docs_263_ReplaceImageRequestOut",
        "TextStyleIn": "_docs_264_TextStyleIn",
        "TextStyleOut": "_docs_265_TextStyleOut",
        "ParagraphStyleSuggestionStateIn": "_docs_266_ParagraphStyleSuggestionStateIn",
        "ParagraphStyleSuggestionStateOut": "_docs_267_ParagraphStyleSuggestionStateOut",
        "ListPropertiesIn": "_docs_268_ListPropertiesIn",
        "ListPropertiesOut": "_docs_269_ListPropertiesOut",
        "InsertTableRowRequestIn": "_docs_270_InsertTableRowRequestIn",
        "InsertTableRowRequestOut": "_docs_271_InsertTableRowRequestOut",
        "RgbColorIn": "_docs_272_RgbColorIn",
        "RgbColorOut": "_docs_273_RgbColorOut",
        "EquationIn": "_docs_274_EquationIn",
        "EquationOut": "_docs_275_EquationOut",
        "SuggestedBulletIn": "_docs_276_SuggestedBulletIn",
        "SuggestedBulletOut": "_docs_277_SuggestedBulletOut",
        "WeightedFontFamilyIn": "_docs_278_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_docs_279_WeightedFontFamilyOut",
        "DeleteNamedRangeRequestIn": "_docs_280_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_docs_281_DeleteNamedRangeRequestOut",
        "UpdateTableColumnPropertiesRequestIn": "_docs_282_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_docs_283_UpdateTableColumnPropertiesRequestOut",
        "TableRowStyleSuggestionStateIn": "_docs_284_TableRowStyleSuggestionStateIn",
        "TableRowStyleSuggestionStateOut": "_docs_285_TableRowStyleSuggestionStateOut",
        "DeletePositionedObjectRequestIn": "_docs_286_DeletePositionedObjectRequestIn",
        "DeletePositionedObjectRequestOut": "_docs_287_DeletePositionedObjectRequestOut",
        "TableCellLocationIn": "_docs_288_TableCellLocationIn",
        "TableCellLocationOut": "_docs_289_TableCellLocationOut",
        "ParagraphStyleIn": "_docs_290_ParagraphStyleIn",
        "ParagraphStyleOut": "_docs_291_ParagraphStyleOut",
        "InsertInlineImageRequestIn": "_docs_292_InsertInlineImageRequestIn",
        "InsertInlineImageRequestOut": "_docs_293_InsertInlineImageRequestOut",
        "TextRunIn": "_docs_294_TextRunIn",
        "TextRunOut": "_docs_295_TextRunOut",
        "RequestIn": "_docs_296_RequestIn",
        "RequestOut": "_docs_297_RequestOut",
        "SuggestedParagraphStyleIn": "_docs_298_SuggestedParagraphStyleIn",
        "SuggestedParagraphStyleOut": "_docs_299_SuggestedParagraphStyleOut",
        "AutoTextIn": "_docs_300_AutoTextIn",
        "AutoTextOut": "_docs_301_AutoTextOut",
        "UnmergeTableCellsRequestIn": "_docs_302_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_docs_303_UnmergeTableCellsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NestingLevelSuggestionStateIn"] = t.struct(
        {
            "indentFirstLineSuggested": t.boolean().optional(),
            "glyphFormatSuggested": t.boolean().optional(),
            "bulletAlignmentSuggested": t.boolean().optional(),
            "glyphSymbolSuggested": t.boolean().optional(),
            "startNumberSuggested": t.boolean().optional(),
            "glyphTypeSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["NestingLevelSuggestionStateIn"])
    types["NestingLevelSuggestionStateOut"] = t.struct(
        {
            "indentFirstLineSuggested": t.boolean().optional(),
            "glyphFormatSuggested": t.boolean().optional(),
            "bulletAlignmentSuggested": t.boolean().optional(),
            "glyphSymbolSuggested": t.boolean().optional(),
            "startNumberSuggested": t.boolean().optional(),
            "glyphTypeSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelSuggestionStateOut"])
    types["ImagePropertiesSuggestionStateIn"] = t.struct(
        {
            "contrastSuggested": t.boolean().optional(),
            "brightnessSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "sourceUriSuggested": t.boolean().optional(),
            "contentUriSuggested": t.boolean().optional(),
            "transparencySuggested": t.boolean().optional(),
            "cropPropertiesSuggestionState": t.proxy(
                renames["CropPropertiesSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["ImagePropertiesSuggestionStateIn"])
    types["ImagePropertiesSuggestionStateOut"] = t.struct(
        {
            "contrastSuggested": t.boolean().optional(),
            "brightnessSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "sourceUriSuggested": t.boolean().optional(),
            "contentUriSuggested": t.boolean().optional(),
            "transparencySuggested": t.boolean().optional(),
            "cropPropertiesSuggestionState": t.proxy(
                renames["CropPropertiesSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesSuggestionStateOut"])
    types["InlineObjectElementIn"] = t.struct(
        {
            "inlineObjectId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["InlineObjectElementIn"])
    types["InlineObjectElementOut"] = t.struct(
        {
            "inlineObjectId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectElementOut"])
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
    types["InsertTextRequestIn"] = t.struct(
        {
            "text": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "text": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
    types["NamedStyleIn"] = t.struct(
        {
            "namedStyleType": t.string().optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["NamedStyleIn"])
    types["NamedStyleOut"] = t.struct(
        {
            "namedStyleType": t.string().optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStyleOut"])
    types["LinkedContentReferenceIn"] = t.struct(
        {"sheetsChartReference": t.proxy(renames["SheetsChartReferenceIn"]).optional()}
    ).named(renames["LinkedContentReferenceIn"])
    types["LinkedContentReferenceOut"] = t.struct(
        {
            "sheetsChartReference": t.proxy(
                renames["SheetsChartReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedContentReferenceOut"])
    types["ReplaceAllTextRequestIn"] = t.struct(
        {
            "replaceText": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
        }
    ).named(renames["ReplaceAllTextRequestIn"])
    types["ReplaceAllTextRequestOut"] = t.struct(
        {
            "replaceText": t.string().optional(),
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextRequestOut"])
    types["DocumentStyleIn"] = t.struct(
        {
            "background": t.proxy(renames["BackgroundIn"]).optional(),
            "pageNumberStart": t.integer().optional(),
            "defaultHeaderId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "firstPageFooterId": t.string().optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "useEvenPageHeaderFooter": t.boolean().optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "marginHeader": t.proxy(renames["DimensionIn"]).optional(),
            "useCustomHeaderFooterMargins": t.boolean().optional(),
            "defaultFooterId": t.string().optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "evenPageHeaderId": t.string().optional(),
            "marginFooter": t.proxy(renames["DimensionIn"]).optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "evenPageFooterId": t.string().optional(),
        }
    ).named(renames["DocumentStyleIn"])
    types["DocumentStyleOut"] = t.struct(
        {
            "background": t.proxy(renames["BackgroundOut"]).optional(),
            "pageNumberStart": t.integer().optional(),
            "defaultHeaderId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "firstPageFooterId": t.string().optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "useEvenPageHeaderFooter": t.boolean().optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "marginHeader": t.proxy(renames["DimensionOut"]).optional(),
            "useCustomHeaderFooterMargins": t.boolean().optional(),
            "defaultFooterId": t.string().optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "evenPageHeaderId": t.string().optional(),
            "marginFooter": t.proxy(renames["DimensionOut"]).optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "evenPageFooterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentStyleOut"])
    types["FootnoteReferenceIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "footnoteNumber": t.string().optional(),
            "footnoteId": t.string().optional(),
        }
    ).named(renames["FootnoteReferenceIn"])
    types["FootnoteReferenceOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "footnoteNumber": t.string().optional(),
            "footnoteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FootnoteReferenceOut"])
    types["InsertInlineSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["InsertInlineSheetsChartResponseIn"])
    types["InsertInlineSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineSheetsChartResponseOut"])
    types["CreateNamedRangeResponseIn"] = t.struct(
        {"namedRangeId": t.string().optional()}
    ).named(renames["CreateNamedRangeResponseIn"])
    types["CreateNamedRangeResponseOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNamedRangeResponseOut"])
    types["DocumentIn"] = t.struct(
        {
            "footers": t.struct({"_": t.string().optional()}).optional(),
            "suggestionsViewMode": t.string().optional(),
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "suggestedNamedStylesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
            "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
            "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
            "suggestedDocumentStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "body": t.proxy(renames["BodyIn"]).optional(),
            "revisionId": t.string().optional(),
            "documentId": t.string().optional(),
            "footnotes": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
            "namedRanges": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "footers": t.struct({"_": t.string().optional()}).optional(),
            "suggestionsViewMode": t.string().optional(),
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "suggestedNamedStylesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
            "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
            "namedStyles": t.proxy(renames["NamedStylesOut"]).optional(),
            "suggestedDocumentStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "body": t.proxy(renames["BodyOut"]).optional(),
            "revisionId": t.string().optional(),
            "documentId": t.string().optional(),
            "footnotes": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleOut"]).optional(),
            "namedRanges": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
    types["TableRowStyleIn"] = t.struct(
        {
            "minRowHeight": t.proxy(renames["DimensionIn"]).optional(),
            "tableHeader": t.boolean().optional(),
            "preventOverflow": t.boolean().optional(),
        }
    ).named(renames["TableRowStyleIn"])
    types["TableRowStyleOut"] = t.struct(
        {
            "minRowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "tableHeader": t.boolean().optional(),
            "preventOverflow": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowStyleOut"])
    types["SuggestedListPropertiesIn"] = t.struct(
        {
            "listProperties": t.proxy(renames["ListPropertiesIn"]).optional(),
            "listPropertiesSuggestionState": t.proxy(
                renames["ListPropertiesSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedListPropertiesIn"])
    types["SuggestedListPropertiesOut"] = t.struct(
        {
            "listProperties": t.proxy(renames["ListPropertiesOut"]).optional(),
            "listPropertiesSuggestionState": t.proxy(
                renames["ListPropertiesSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedListPropertiesOut"])
    types["ObjectReferencesIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["ObjectReferencesIn"])
    types["ObjectReferencesOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectReferencesOut"])
    types["CreateFooterResponseIn"] = t.struct(
        {"footerId": t.string().optional()}
    ).named(renames["CreateFooterResponseIn"])
    types["CreateFooterResponseOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFooterResponseOut"])
    types["CropPropertiesIn"] = t.struct(
        {
            "angle": t.number().optional(),
            "offsetBottom": t.number().optional(),
            "offsetTop": t.number().optional(),
            "offsetLeft": t.number().optional(),
            "offsetRight": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "angle": t.number().optional(),
            "offsetBottom": t.number().optional(),
            "offsetTop": t.number().optional(),
            "offsetLeft": t.number().optional(),
            "offsetRight": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
    types["SuggestedPositionedObjectPropertiesIn"] = t.struct(
        {
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesIn"]
            ).optional(),
            "positionedObjectPropertiesSuggestionState": t.proxy(
                renames["PositionedObjectPropertiesSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedPositionedObjectPropertiesIn"])
    types["SuggestedPositionedObjectPropertiesOut"] = t.struct(
        {
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesOut"]
            ).optional(),
            "positionedObjectPropertiesSuggestionState": t.proxy(
                renames["PositionedObjectPropertiesSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedPositionedObjectPropertiesOut"])
    types["ColumnBreakIn"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["ColumnBreakIn"])
    types["ColumnBreakOut"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnBreakOut"])
    types["BulletSuggestionStateIn"] = t.struct(
        {
            "listIdSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
            "nestingLevelSuggested": t.boolean().optional(),
        }
    ).named(renames["BulletSuggestionStateIn"])
    types["BulletSuggestionStateOut"] = t.struct(
        {
            "listIdSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "nestingLevelSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletSuggestionStateOut"])
    types["ParagraphBorderIn"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
            "dashStyle": t.string().optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "padding": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["ParagraphBorderIn"])
    types["ParagraphBorderOut"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "dashStyle": t.string().optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "padding": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphBorderOut"])
    types["ResponseIn"] = t.struct(
        {
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageResponseIn"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterResponseIn"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteResponseIn"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeResponseIn"]
            ).optional(),
            "insertInlineSheetsChart": t.proxy(
                renames["InsertInlineSheetsChartResponseIn"]
            ).optional(),
            "createHeader": t.proxy(renames["CreateHeaderResponseIn"]).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageResponseOut"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterResponseOut"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteResponseOut"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeResponseOut"]
            ).optional(),
            "insertInlineSheetsChart": t.proxy(
                renames["InsertInlineSheetsChartResponseOut"]
            ).optional(),
            "createHeader": t.proxy(renames["CreateHeaderResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["TextStyleSuggestionStateIn"] = t.struct(
        {
            "weightedFontFamilySuggested": t.boolean().optional(),
            "strikethroughSuggested": t.boolean().optional(),
            "linkSuggested": t.boolean().optional(),
            "boldSuggested": t.boolean().optional(),
            "italicSuggested": t.boolean().optional(),
            "fontSizeSuggested": t.boolean().optional(),
            "underlineSuggested": t.boolean().optional(),
            "baselineOffsetSuggested": t.boolean().optional(),
            "smallCapsSuggested": t.boolean().optional(),
            "foregroundColorSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
        }
    ).named(renames["TextStyleSuggestionStateIn"])
    types["TextStyleSuggestionStateOut"] = t.struct(
        {
            "weightedFontFamilySuggested": t.boolean().optional(),
            "strikethroughSuggested": t.boolean().optional(),
            "linkSuggested": t.boolean().optional(),
            "boldSuggested": t.boolean().optional(),
            "italicSuggested": t.boolean().optional(),
            "fontSizeSuggested": t.boolean().optional(),
            "underlineSuggested": t.boolean().optional(),
            "baselineOffsetSuggested": t.boolean().optional(),
            "smallCapsSuggested": t.boolean().optional(),
            "foregroundColorSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleSuggestionStateOut"])
    types["CreateParagraphBulletsRequestIn"] = t.struct(
        {
            "bulletPreset": t.string().optional(),
            "range": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestIn"])
    types["CreateParagraphBulletsRequestOut"] = t.struct(
        {
            "bulletPreset": t.string().optional(),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestOut"])
    types["SectionColumnPropertiesIn"] = t.struct(
        {
            "paddingEnd": t.proxy(renames["DimensionIn"]).optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["SectionColumnPropertiesIn"])
    types["SectionColumnPropertiesOut"] = t.struct(
        {
            "paddingEnd": t.proxy(renames["DimensionOut"]).optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionColumnPropertiesOut"])
    types["UpdateSectionStyleRequestIn"] = t.struct(
        {
            "sectionStyle": t.proxy(renames["SectionStyleIn"]).optional(),
            "fields": t.string().optional(),
            "range": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["UpdateSectionStyleRequestIn"])
    types["UpdateSectionStyleRequestOut"] = t.struct(
        {
            "sectionStyle": t.proxy(renames["SectionStyleOut"]).optional(),
            "fields": t.string().optional(),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSectionStyleRequestOut"])
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
    types["RangeIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "segmentId": t.string().optional(),
        }
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
    types["InsertTableColumnRequestIn"] = t.struct(
        {
            "insertRight": t.boolean().optional(),
            "tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["InsertTableColumnRequestIn"])
    types["InsertTableColumnRequestOut"] = t.struct(
        {
            "insertRight": t.boolean().optional(),
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableColumnRequestOut"])
    types["EndOfSegmentLocationIn"] = t.struct(
        {"segmentId": t.string().optional()}
    ).named(renames["EndOfSegmentLocationIn"])
    types["EndOfSegmentLocationOut"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndOfSegmentLocationOut"])
    types["EmbeddedDrawingPropertiesSuggestionStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EmbeddedDrawingPropertiesSuggestionStateIn"])
    types["EmbeddedDrawingPropertiesSuggestionStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmbeddedDrawingPropertiesSuggestionStateOut"])
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["RangeIn"]).optional(),
            "fields": t.string().optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "fields": t.string().optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
    types["PersonIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "personProperties": t.proxy(renames["PersonPropertiesOut"]).optional(),
            "personId": t.string().optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["NamedRangesIn"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
        }
    ).named(renames["NamedRangesIn"])
    types["NamedRangesOut"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedRangesOut"])
    types["TableCellBorderIn"] = t.struct(
        {
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "dashStyle": t.string().optional(),
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
        }
    ).named(renames["TableCellBorderIn"])
    types["TableCellBorderOut"] = t.struct(
        {
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellBorderOut"])
    types["TableCellStyleIn"] = t.struct(
        {
            "borderLeft": t.proxy(renames["TableCellBorderIn"]).optional(),
            "borderBottom": t.proxy(renames["TableCellBorderIn"]).optional(),
            "columnSpan": t.integer().optional(),
            "borderTop": t.proxy(renames["TableCellBorderIn"]).optional(),
            "rowSpan": t.integer().optional(),
            "paddingLeft": t.proxy(renames["DimensionIn"]).optional(),
            "borderRight": t.proxy(renames["TableCellBorderIn"]).optional(),
            "paddingTop": t.proxy(renames["DimensionIn"]).optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "paddingRight": t.proxy(renames["DimensionIn"]).optional(),
            "paddingBottom": t.proxy(renames["DimensionIn"]).optional(),
            "contentAlignment": t.string().optional(),
        }
    ).named(renames["TableCellStyleIn"])
    types["TableCellStyleOut"] = t.struct(
        {
            "borderLeft": t.proxy(renames["TableCellBorderOut"]).optional(),
            "borderBottom": t.proxy(renames["TableCellBorderOut"]).optional(),
            "columnSpan": t.integer().optional(),
            "borderTop": t.proxy(renames["TableCellBorderOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "paddingLeft": t.proxy(renames["DimensionOut"]).optional(),
            "borderRight": t.proxy(renames["TableCellBorderOut"]).optional(),
            "paddingTop": t.proxy(renames["DimensionOut"]).optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "paddingRight": t.proxy(renames["DimensionOut"]).optional(),
            "paddingBottom": t.proxy(renames["DimensionOut"]).optional(),
            "contentAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellStyleOut"])
    types["TableCellStyleSuggestionStateIn"] = t.struct(
        {
            "borderTopSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "rowSpanSuggested": t.boolean().optional(),
            "paddingBottomSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "contentAlignmentSuggested": t.boolean().optional(),
            "paddingLeftSuggested": t.boolean().optional(),
            "columnSpanSuggested": t.boolean().optional(),
            "paddingRightSuggested": t.boolean().optional(),
            "paddingTopSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
        }
    ).named(renames["TableCellStyleSuggestionStateIn"])
    types["TableCellStyleSuggestionStateOut"] = t.struct(
        {
            "borderTopSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "rowSpanSuggested": t.boolean().optional(),
            "paddingBottomSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "contentAlignmentSuggested": t.boolean().optional(),
            "paddingLeftSuggested": t.boolean().optional(),
            "columnSpanSuggested": t.boolean().optional(),
            "paddingRightSuggested": t.boolean().optional(),
            "paddingTopSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellStyleSuggestionStateOut"])
    types["SectionBreakIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "sectionStyle": t.proxy(renames["SectionStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["SectionBreakIn"])
    types["SectionBreakOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "sectionStyle": t.proxy(renames["SectionStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionBreakOut"])
    types["UpdateDocumentStyleRequestIn"] = t.struct(
        {
            "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateDocumentStyleRequestIn"])
    types["UpdateDocumentStyleRequestOut"] = t.struct(
        {
            "documentStyle": t.proxy(renames["DocumentStyleOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDocumentStyleRequestOut"])
    types["PositionedObjectPropertiesSuggestionStateIn"] = t.struct(
        {
            "embeddedObjectSuggestionState": t.proxy(
                renames["EmbeddedObjectSuggestionStateIn"]
            ).optional(),
            "positioningSuggestionState": t.proxy(
                renames["PositionedObjectPositioningSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["PositionedObjectPropertiesSuggestionStateIn"])
    types["PositionedObjectPropertiesSuggestionStateOut"] = t.struct(
        {
            "embeddedObjectSuggestionState": t.proxy(
                renames["EmbeddedObjectSuggestionStateOut"]
            ).optional(),
            "positioningSuggestionState": t.proxy(
                renames["PositionedObjectPositioningSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPropertiesSuggestionStateOut"])
    types["FootnoteIn"] = t.struct(
        {
            "footnoteId": t.string().optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
        }
    ).named(renames["FootnoteIn"])
    types["FootnoteOut"] = t.struct(
        {
            "footnoteId": t.string().optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FootnoteOut"])
    types["InsertSectionBreakRequestIn"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "sectionType": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["InsertSectionBreakRequestIn"])
    types["InsertSectionBreakRequestOut"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "sectionType": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertSectionBreakRequestOut"])
    types["TableStyleIn"] = t.struct(
        {
            "tableColumnProperties": t.array(
                t.proxy(renames["TableColumnPropertiesIn"])
            ).optional()
        }
    ).named(renames["TableStyleIn"])
    types["TableStyleOut"] = t.struct(
        {
            "tableColumnProperties": t.array(
                t.proxy(renames["TableColumnPropertiesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableStyleOut"])
    types["SuggestedDocumentStyleIn"] = t.struct(
        {
            "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
            "documentStyleSuggestionState": t.proxy(
                renames["DocumentStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedDocumentStyleIn"])
    types["SuggestedDocumentStyleOut"] = t.struct(
        {
            "documentStyle": t.proxy(renames["DocumentStyleOut"]).optional(),
            "documentStyleSuggestionState": t.proxy(
                renames["DocumentStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedDocumentStyleOut"])
    types["TableIn"] = t.struct(
        {
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "tableStyle": t.proxy(renames["TableStyleIn"]).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "columns": t.integer().optional(),
            "rows": t.integer().optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "tableStyle": t.proxy(renames["TableStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["TableColumnPropertiesIn"] = t.struct(
        {
            "widthType": t.string().optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["TableColumnPropertiesIn"])
    types["TableColumnPropertiesOut"] = t.struct(
        {
            "widthType": t.string().optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableColumnPropertiesOut"])
    types["CreateFooterRequestIn"] = t.struct(
        {
            "sectionBreakLocation": t.proxy(renames["LocationIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CreateFooterRequestIn"])
    types["CreateFooterRequestOut"] = t.struct(
        {
            "sectionBreakLocation": t.proxy(renames["LocationOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFooterRequestOut"])
    types["BodyIn"] = t.struct(
        {"content": t.array(t.proxy(renames["StructuralElementIn"])).optional()}
    ).named(renames["BodyIn"])
    types["BodyOut"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BodyOut"])
    types["TableRangeIn"] = t.struct(
        {
            "rowSpan": t.integer().optional(),
            "tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "columnSpan": t.integer().optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "rowSpan": t.integer().optional(),
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "columnSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
    types["ShadingSuggestionStateIn"] = t.struct(
        {"backgroundColorSuggested": t.boolean().optional()}
    ).named(renames["ShadingSuggestionStateIn"])
    types["ShadingSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadingSuggestionStateOut"])
    types["EmbeddedObjectSuggestionStateIn"] = t.struct(
        {
            "marginLeftSuggested": t.boolean().optional(),
            "sizeSuggestionState": t.proxy(renames["SizeSuggestionStateIn"]).optional(),
            "descriptionSuggested": t.boolean().optional(),
            "linkedContentReferenceSuggestionState": t.proxy(
                renames["LinkedContentReferenceSuggestionStateIn"]
            ).optional(),
            "titleSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "embeddedDrawingPropertiesSuggestionState": t.proxy(
                renames["EmbeddedDrawingPropertiesSuggestionStateIn"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "imagePropertiesSuggestionState": t.proxy(
                renames["ImagePropertiesSuggestionStateIn"]
            ).optional(),
            "embeddedObjectBorderSuggestionState": t.proxy(
                renames["EmbeddedObjectBorderSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["EmbeddedObjectSuggestionStateIn"])
    types["EmbeddedObjectSuggestionStateOut"] = t.struct(
        {
            "marginLeftSuggested": t.boolean().optional(),
            "sizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateOut"]
            ).optional(),
            "descriptionSuggested": t.boolean().optional(),
            "linkedContentReferenceSuggestionState": t.proxy(
                renames["LinkedContentReferenceSuggestionStateOut"]
            ).optional(),
            "titleSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "embeddedDrawingPropertiesSuggestionState": t.proxy(
                renames["EmbeddedDrawingPropertiesSuggestionStateOut"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "imagePropertiesSuggestionState": t.proxy(
                renames["ImagePropertiesSuggestionStateOut"]
            ).optional(),
            "embeddedObjectBorderSuggestionState": t.proxy(
                renames["EmbeddedObjectBorderSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectSuggestionStateOut"])
    types["BackgroundIn"] = t.struct(
        {"color": t.proxy(renames["OptionalColorIn"]).optional()}
    ).named(renames["BackgroundIn"])
    types["BackgroundOut"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundOut"])
    types["PageBreakIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["PageBreakIn"])
    types["PageBreakOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBreakOut"])
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
    types["SuggestedTextStyleIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedTextStyleIn"])
    types["SuggestedTextStyleOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedTextStyleOut"])
    types["BatchUpdateDocumentResponseIn"] = t.struct(
        {
            "documentId": t.string().optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdateDocumentResponseIn"])
    types["BatchUpdateDocumentResponseOut"] = t.struct(
        {
            "documentId": t.string().optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDocumentResponseOut"])
    types["ListPropertiesSuggestionStateIn"] = t.struct(
        {
            "nestingLevelsSuggestionStates": t.array(
                t.proxy(renames["NestingLevelSuggestionStateIn"])
            ).optional()
        }
    ).named(renames["ListPropertiesSuggestionStateIn"])
    types["ListPropertiesSuggestionStateOut"] = t.struct(
        {
            "nestingLevelsSuggestionStates": t.array(
                t.proxy(renames["NestingLevelSuggestionStateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPropertiesSuggestionStateOut"])
    types["RichLinkPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RichLinkPropertiesIn"]
    )
    types["RichLinkPropertiesOut"] = t.struct(
        {
            "title": t.string().optional(),
            "uri": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichLinkPropertiesOut"])
    types["ReplaceNamedRangeContentRequestIn"] = t.struct(
        {
            "namedRangeName": t.string().optional(),
            "text": t.string().optional(),
            "namedRangeId": t.string().optional(),
        }
    ).named(renames["ReplaceNamedRangeContentRequestIn"])
    types["ReplaceNamedRangeContentRequestOut"] = t.struct(
        {
            "namedRangeName": t.string().optional(),
            "text": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceNamedRangeContentRequestOut"])
    types["RichLinkIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["RichLinkIn"])
    types["RichLinkOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "richLinkId": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "richLinkProperties": t.proxy(renames["RichLinkPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichLinkOut"])
    types["FooterIn"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "footerId": t.string().optional(),
        }
    ).named(renames["FooterIn"])
    types["FooterOut"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FooterOut"])
    types["HeaderIn"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "headerId": t.string().optional(),
        }
    ).named(renames["HeaderIn"])
    types["HeaderOut"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "headerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeaderOut"])
    types["PositionedObjectPositioningIn"] = t.struct(
        {
            "topOffset": t.proxy(renames["DimensionIn"]).optional(),
            "layout": t.string().optional(),
            "leftOffset": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningIn"])
    types["PositionedObjectPositioningOut"] = t.struct(
        {
            "topOffset": t.proxy(renames["DimensionOut"]).optional(),
            "layout": t.string().optional(),
            "leftOffset": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningOut"])
    types["SizeSuggestionStateIn"] = t.struct(
        {
            "widthSuggested": t.boolean().optional(),
            "heightSuggested": t.boolean().optional(),
        }
    ).named(renames["SizeSuggestionStateIn"])
    types["SizeSuggestionStateOut"] = t.struct(
        {
            "widthSuggested": t.boolean().optional(),
            "heightSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SizeSuggestionStateOut"])
    types["PinTableHeaderRowsRequestIn"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "pinnedHeaderRowsCount": t.integer().optional(),
        }
    ).named(renames["PinTableHeaderRowsRequestIn"])
    types["PinTableHeaderRowsRequestOut"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "pinnedHeaderRowsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PinTableHeaderRowsRequestOut"])
    types["BulletIn"] = t.struct(
        {
            "nestingLevel": t.integer().optional(),
            "listId": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["BulletIn"])
    types["BulletOut"] = t.struct(
        {
            "nestingLevel": t.integer().optional(),
            "listId": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletOut"])
    types["LocationIn"] = t.struct(
        {"segmentId": t.string().optional(), "index": t.integer().optional()}
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["PositionedObjectIn"] = t.struct(
        {
            "suggestedPositionedObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
            "objectId": t.string().optional(),
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesIn"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["PositionedObjectIn"])
    types["PositionedObjectOut"] = t.struct(
        {
            "suggestedPositionedObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
            "objectId": t.string().optional(),
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesOut"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectOut"])
    types["EmbeddedDrawingPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EmbeddedDrawingPropertiesIn"]
    )
    types["EmbeddedDrawingPropertiesOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmbeddedDrawingPropertiesOut"])
    types["CreateFootnoteResponseIn"] = t.struct(
        {"footnoteId": t.string().optional()}
    ).named(renames["CreateFootnoteResponseIn"])
    types["CreateFootnoteResponseOut"] = t.struct(
        {
            "footnoteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFootnoteResponseOut"])
    types["CropPropertiesSuggestionStateIn"] = t.struct(
        {
            "offsetTopSuggested": t.boolean().optional(),
            "offsetBottomSuggested": t.boolean().optional(),
            "offsetRightSuggested": t.boolean().optional(),
            "offsetLeftSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
        }
    ).named(renames["CropPropertiesSuggestionStateIn"])
    types["CropPropertiesSuggestionStateOut"] = t.struct(
        {
            "offsetTopSuggested": t.boolean().optional(),
            "offsetBottomSuggested": t.boolean().optional(),
            "offsetRightSuggested": t.boolean().optional(),
            "offsetLeftSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesSuggestionStateOut"])
    types["InsertInlineImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["InsertInlineImageResponseIn"])
    types["InsertInlineImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineImageResponseOut"])
    types["NamedStyleSuggestionStateIn"] = t.struct(
        {
            "namedStyleType": t.string().optional(),
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateIn"]
            ).optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["NamedStyleSuggestionStateIn"])
    types["NamedStyleSuggestionStateOut"] = t.struct(
        {
            "namedStyleType": t.string().optional(),
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateOut"]
            ).optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStyleSuggestionStateOut"])
    types["LinkIn"] = t.struct(
        {
            "headingId": t.string().optional(),
            "url": t.string().optional(),
            "bookmarkId": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "headingId": t.string().optional(),
            "url": t.string().optional(),
            "bookmarkId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["TabStopIn"] = t.struct(
        {
            "offset": t.proxy(renames["DimensionIn"]).optional(),
            "alignment": t.string().optional(),
        }
    ).named(renames["TabStopIn"])
    types["TabStopOut"] = t.struct(
        {
            "offset": t.proxy(renames["DimensionOut"]).optional(),
            "alignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TabStopOut"])
    types["CreateFootnoteRequestIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
        }
    ).named(renames["CreateFootnoteRequestIn"])
    types["CreateFootnoteRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFootnoteRequestOut"])
    types["TableCellIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "suggestedTableCellStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "suggestedTableCellStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
    types["EmbeddedObjectIn"] = t.struct(
        {
            "embeddedDrawingProperties": t.proxy(
                renames["EmbeddedDrawingPropertiesIn"]
            ).optional(),
            "description": t.string().optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "linkedContentReference": t.proxy(
                renames["LinkedContentReferenceIn"]
            ).optional(),
            "title": t.string().optional(),
            "embeddedObjectBorder": t.proxy(
                renames["EmbeddedObjectBorderIn"]
            ).optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
        }
    ).named(renames["EmbeddedObjectIn"])
    types["EmbeddedObjectOut"] = t.struct(
        {
            "embeddedDrawingProperties": t.proxy(
                renames["EmbeddedDrawingPropertiesOut"]
            ).optional(),
            "description": t.string().optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "linkedContentReference": t.proxy(
                renames["LinkedContentReferenceOut"]
            ).optional(),
            "title": t.string().optional(),
            "embeddedObjectBorder": t.proxy(
                renames["EmbeddedObjectBorderOut"]
            ).optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectOut"])
    types["InsertPageBreakRequestIn"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["InsertPageBreakRequestIn"])
    types["InsertPageBreakRequestOut"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertPageBreakRequestOut"])
    types["DeleteParagraphBulletsRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["DeleteParagraphBulletsRequestIn"])
    types["DeleteParagraphBulletsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestOut"])
    types["UpdateTableCellStyleRequestIn"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "fields": t.string().optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
        }
    ).named(renames["UpdateTableCellStyleRequestIn"])
    types["UpdateTableCellStyleRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "fields": t.string().optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellStyleRequestOut"])
    types["CreateHeaderRequestIn"] = t.struct(
        {
            "sectionBreakLocation": t.proxy(renames["LocationIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CreateHeaderRequestIn"])
    types["CreateHeaderRequestOut"] = t.struct(
        {
            "sectionBreakLocation": t.proxy(renames["LocationOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateHeaderRequestOut"])
    types["DeleteTableColumnRequestIn"] = t.struct(
        {"tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional()}
    ).named(renames["DeleteTableColumnRequestIn"])
    types["DeleteTableColumnRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableColumnRequestOut"])
    types["NamedStylesIn"] = t.struct(
        {"styles": t.array(t.proxy(renames["NamedStyleIn"])).optional()}
    ).named(renames["NamedStylesIn"])
    types["NamedStylesOut"] = t.struct(
        {
            "styles": t.array(t.proxy(renames["NamedStyleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStylesOut"])
    types["UpdateTableRowStyleRequestIn"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableRowStyleRequestIn"])
    types["UpdateTableRowStyleRequestOut"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowStyleRequestOut"])
    types["SuggestedNamedStylesIn"] = t.struct(
        {
            "namedStylesSuggestionState": t.proxy(
                renames["NamedStylesSuggestionStateIn"]
            ).optional(),
            "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
        }
    ).named(renames["SuggestedNamedStylesIn"])
    types["SuggestedNamedStylesOut"] = t.struct(
        {
            "namedStylesSuggestionState": t.proxy(
                renames["NamedStylesSuggestionStateOut"]
            ).optional(),
            "namedStyles": t.proxy(renames["NamedStylesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedNamedStylesOut"])
    types["PositionedObjectPropertiesIn"] = t.struct(
        {
            "embeddedObject": t.proxy(renames["EmbeddedObjectIn"]).optional(),
            "positioning": t.proxy(renames["PositionedObjectPositioningIn"]).optional(),
        }
    ).named(renames["PositionedObjectPropertiesIn"])
    types["PositionedObjectPropertiesOut"] = t.struct(
        {
            "embeddedObject": t.proxy(renames["EmbeddedObjectOut"]).optional(),
            "positioning": t.proxy(
                renames["PositionedObjectPositioningOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPropertiesOut"])
    types["WriteControlIn"] = t.struct(
        {
            "targetRevisionId": t.string().optional(),
            "requiredRevisionId": t.string().optional(),
        }
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "targetRevisionId": t.string().optional(),
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
    types["PersonPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PersonPropertiesIn"]
    )
    types["PersonPropertiesOut"] = t.struct(
        {
            "name": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonPropertiesOut"])
    types["ListIn"] = t.struct(
        {
            "suggestedListPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
            "listProperties": t.proxy(renames["ListPropertiesIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["ListIn"])
    types["ListOut"] = t.struct(
        {
            "suggestedListPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
            "listProperties": t.proxy(renames["ListPropertiesOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOut"])
    types["MergeTableCellsRequestIn"] = t.struct(
        {"tableRange": t.proxy(renames["TableRangeIn"]).optional()}
    ).named(renames["MergeTableCellsRequestIn"])
    types["MergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeTableCellsRequestOut"])
    types["NamedStylesSuggestionStateIn"] = t.struct(
        {
            "stylesSuggestionStates": t.array(
                t.proxy(renames["NamedStyleSuggestionStateIn"])
            ).optional()
        }
    ).named(renames["NamedStylesSuggestionStateIn"])
    types["NamedStylesSuggestionStateOut"] = t.struct(
        {
            "stylesSuggestionStates": t.array(
                t.proxy(renames["NamedStyleSuggestionStateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStylesSuggestionStateOut"])
    types["OptionalColorIn"] = t.struct(
        {"color": t.proxy(renames["ColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
    types["DocumentStyleSuggestionStateIn"] = t.struct(
        {
            "useCustomHeaderFooterMarginsSuggested": t.boolean().optional(),
            "evenPageFooterIdSuggested": t.boolean().optional(),
            "defaultFooterIdSuggested": t.boolean().optional(),
            "marginHeaderSuggested": t.boolean().optional(),
            "useEvenPageHeaderFooterSuggested": t.boolean().optional(),
            "pageNumberStartSuggested": t.boolean().optional(),
            "marginFooterSuggested": t.boolean().optional(),
            "pageSizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateIn"]
            ).optional(),
            "evenPageHeaderIdSuggested": t.boolean().optional(),
            "firstPageFooterIdSuggested": t.boolean().optional(),
            "marginTopSuggested": t.boolean().optional(),
            "defaultHeaderIdSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "backgroundSuggestionState": t.proxy(
                renames["BackgroundSuggestionStateIn"]
            ).optional(),
            "firstPageHeaderIdSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "useFirstPageHeaderFooterSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
        }
    ).named(renames["DocumentStyleSuggestionStateIn"])
    types["DocumentStyleSuggestionStateOut"] = t.struct(
        {
            "useCustomHeaderFooterMarginsSuggested": t.boolean().optional(),
            "evenPageFooterIdSuggested": t.boolean().optional(),
            "defaultFooterIdSuggested": t.boolean().optional(),
            "marginHeaderSuggested": t.boolean().optional(),
            "useEvenPageHeaderFooterSuggested": t.boolean().optional(),
            "pageNumberStartSuggested": t.boolean().optional(),
            "marginFooterSuggested": t.boolean().optional(),
            "pageSizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateOut"]
            ).optional(),
            "evenPageHeaderIdSuggested": t.boolean().optional(),
            "firstPageFooterIdSuggested": t.boolean().optional(),
            "marginTopSuggested": t.boolean().optional(),
            "defaultHeaderIdSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "backgroundSuggestionState": t.proxy(
                renames["BackgroundSuggestionStateOut"]
            ).optional(),
            "firstPageHeaderIdSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "useFirstPageHeaderFooterSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentStyleSuggestionStateOut"])
    types["EmbeddedObjectBorderSuggestionStateIn"] = t.struct(
        {
            "propertyStateSuggested": t.boolean().optional(),
            "dashStyleSuggested": t.boolean().optional(),
            "colorSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
        }
    ).named(renames["EmbeddedObjectBorderSuggestionStateIn"])
    types["EmbeddedObjectBorderSuggestionStateOut"] = t.struct(
        {
            "propertyStateSuggested": t.boolean().optional(),
            "dashStyleSuggested": t.boolean().optional(),
            "colorSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderSuggestionStateOut"])
    types["DeleteHeaderRequestIn"] = t.struct(
        {"headerId": t.string().optional()}
    ).named(renames["DeleteHeaderRequestIn"])
    types["DeleteHeaderRequestOut"] = t.struct(
        {
            "headerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteHeaderRequestOut"])
    types["NestingLevelIn"] = t.struct(
        {
            "glyphType": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "startNumber": t.integer().optional(),
            "glyphSymbol": t.string().optional(),
            "bulletAlignment": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "glyphFormat": t.string().optional(),
        }
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "glyphType": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "startNumber": t.integer().optional(),
            "glyphSymbol": t.string().optional(),
            "bulletAlignment": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "glyphFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
    types["SuggestedTableRowStyleIn"] = t.struct(
        {
            "tableRowStyleSuggestionState": t.proxy(
                renames["TableRowStyleSuggestionStateIn"]
            ).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
        }
    ).named(renames["SuggestedTableRowStyleIn"])
    types["SuggestedTableRowStyleOut"] = t.struct(
        {
            "tableRowStyleSuggestionState": t.proxy(
                renames["TableRowStyleSuggestionStateOut"]
            ).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedTableRowStyleOut"])
    types["NamedRangeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "ranges": t.array(t.proxy(renames["RangeIn"])).optional(),
        }
    ).named(renames["NamedRangeIn"])
    types["NamedRangeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "ranges": t.array(t.proxy(renames["RangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedRangeOut"])
    types["LinkedContentReferenceSuggestionStateIn"] = t.struct(
        {
            "sheetsChartReferenceSuggestionState": t.proxy(
                renames["SheetsChartReferenceSuggestionStateIn"]
            ).optional()
        }
    ).named(renames["LinkedContentReferenceSuggestionStateIn"])
    types["LinkedContentReferenceSuggestionStateOut"] = t.struct(
        {
            "sheetsChartReferenceSuggestionState": t.proxy(
                renames["SheetsChartReferenceSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedContentReferenceSuggestionStateOut"])
    types["ParagraphIn"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["ParagraphElementIn"])).optional(),
            "suggestedBulletChanges": t.struct({"_": t.string().optional()}).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "bullet": t.proxy(renames["BulletIn"]).optional(),
            "positionedObjectIds": t.array(t.string()).optional(),
            "suggestedParagraphStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedPositionedObjectIds": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["ParagraphIn"])
    types["ParagraphOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["ParagraphElementOut"])).optional(),
            "suggestedBulletChanges": t.struct({"_": t.string().optional()}).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "bullet": t.proxy(renames["BulletOut"]).optional(),
            "positionedObjectIds": t.array(t.string()).optional(),
            "suggestedParagraphStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedPositionedObjectIds": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphOut"])
    types["InlineObjectPropertiesIn"] = t.struct(
        {"embeddedObject": t.proxy(renames["EmbeddedObjectIn"]).optional()}
    ).named(renames["InlineObjectPropertiesIn"])
    types["InlineObjectPropertiesOut"] = t.struct(
        {
            "embeddedObject": t.proxy(renames["EmbeddedObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectPropertiesOut"])
    types["ParagraphElementIn"] = t.struct(
        {
            "columnBreak": t.proxy(renames["ColumnBreakIn"]).optional(),
            "footnoteReference": t.proxy(renames["FootnoteReferenceIn"]).optional(),
            "inlineObjectElement": t.proxy(renames["InlineObjectElementIn"]).optional(),
            "horizontalRule": t.proxy(renames["HorizontalRuleIn"]).optional(),
            "richLink": t.proxy(renames["RichLinkIn"]).optional(),
            "equation": t.proxy(renames["EquationIn"]).optional(),
            "person": t.proxy(renames["PersonIn"]).optional(),
            "pageBreak": t.proxy(renames["PageBreakIn"]).optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["ParagraphElementIn"])
    types["ParagraphElementOut"] = t.struct(
        {
            "columnBreak": t.proxy(renames["ColumnBreakOut"]).optional(),
            "footnoteReference": t.proxy(renames["FootnoteReferenceOut"]).optional(),
            "inlineObjectElement": t.proxy(
                renames["InlineObjectElementOut"]
            ).optional(),
            "horizontalRule": t.proxy(renames["HorizontalRuleOut"]).optional(),
            "richLink": t.proxy(renames["RichLinkOut"]).optional(),
            "equation": t.proxy(renames["EquationOut"]).optional(),
            "person": t.proxy(renames["PersonOut"]).optional(),
            "pageBreak": t.proxy(renames["PageBreakOut"]).optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphElementOut"])
    types["EmbeddedObjectBorderIn"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "propertyState": t.string().optional(),
        }
    ).named(renames["EmbeddedObjectBorderIn"])
    types["EmbeddedObjectBorderOut"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "propertyState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderOut"])
    types["DeleteFooterRequestIn"] = t.struct(
        {"footerId": t.string().optional()}
    ).named(renames["DeleteFooterRequestIn"])
    types["DeleteFooterRequestOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFooterRequestOut"])
    types["CreateHeaderResponseIn"] = t.struct(
        {"headerId": t.string().optional()}
    ).named(renames["CreateHeaderResponseIn"])
    types["CreateHeaderResponseOut"] = t.struct(
        {
            "headerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateHeaderResponseOut"])
    types["SectionStyleIn"] = t.struct(
        {
            "firstPageFooterId": t.string().optional(),
            "defaultHeaderId": t.string().optional(),
            "defaultFooterId": t.string().optional(),
            "columnProperties": t.array(
                t.proxy(renames["SectionColumnPropertiesIn"])
            ).optional(),
            "evenPageFooterId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "columnSeparatorStyle": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "contentDirection": t.string().optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "evenPageHeaderId": t.string().optional(),
            "sectionType": t.string().optional(),
            "marginHeader": t.proxy(renames["DimensionIn"]).optional(),
            "marginFooter": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["SectionStyleIn"])
    types["SectionStyleOut"] = t.struct(
        {
            "firstPageFooterId": t.string().optional(),
            "defaultHeaderId": t.string().optional(),
            "defaultFooterId": t.string().optional(),
            "columnProperties": t.array(
                t.proxy(renames["SectionColumnPropertiesOut"])
            ).optional(),
            "evenPageFooterId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "columnSeparatorStyle": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "contentDirection": t.string().optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "evenPageHeaderId": t.string().optional(),
            "sectionType": t.string().optional(),
            "marginHeader": t.proxy(renames["DimensionOut"]).optional(),
            "marginFooter": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionStyleOut"])
    types["ColorIn"] = t.struct(
        {"rgbColor": t.proxy(renames["RgbColorIn"]).optional()}
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "rgbColor": t.proxy(renames["RgbColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["SuggestedInlineObjectPropertiesIn"] = t.struct(
        {
            "inlineObjectPropertiesSuggestionState": t.proxy(
                renames["InlineObjectPropertiesSuggestionStateIn"]
            ).optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesIn"]
            ).optional(),
        }
    ).named(renames["SuggestedInlineObjectPropertiesIn"])
    types["SuggestedInlineObjectPropertiesOut"] = t.struct(
        {
            "inlineObjectPropertiesSuggestionState": t.proxy(
                renames["InlineObjectPropertiesSuggestionStateOut"]
            ).optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedInlineObjectPropertiesOut"])
    types["StructuralElementIn"] = t.struct(
        {
            "endIndex": t.integer().optional(),
            "tableOfContents": t.proxy(renames["TableOfContentsIn"]).optional(),
            "startIndex": t.integer().optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "paragraph": t.proxy(renames["ParagraphIn"]).optional(),
            "sectionBreak": t.proxy(renames["SectionBreakIn"]).optional(),
        }
    ).named(renames["StructuralElementIn"])
    types["StructuralElementOut"] = t.struct(
        {
            "endIndex": t.integer().optional(),
            "tableOfContents": t.proxy(renames["TableOfContentsOut"]).optional(),
            "startIndex": t.integer().optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "paragraph": t.proxy(renames["ParagraphOut"]).optional(),
            "sectionBreak": t.proxy(renames["SectionBreakOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuralElementOut"])
    types["BatchUpdateDocumentRequestIn"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
        }
    ).named(renames["BatchUpdateDocumentRequestIn"])
    types["BatchUpdateDocumentRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RequestOut"])).optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDocumentRequestOut"])
    types["SheetsChartReferenceSuggestionStateIn"] = t.struct(
        {
            "chartIdSuggested": t.boolean().optional(),
            "spreadsheetIdSuggested": t.boolean().optional(),
        }
    ).named(renames["SheetsChartReferenceSuggestionStateIn"])
    types["SheetsChartReferenceSuggestionStateOut"] = t.struct(
        {
            "chartIdSuggested": t.boolean().optional(),
            "spreadsheetIdSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartReferenceSuggestionStateOut"])
    types["DeleteContentRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["DeleteContentRangeRequestIn"])
    types["DeleteContentRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteContentRangeRequestOut"])
    types["SuggestedTableCellStyleIn"] = t.struct(
        {
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
            "tableCellStyleSuggestionState": t.proxy(
                renames["TableCellStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedTableCellStyleIn"])
    types["SuggestedTableCellStyleOut"] = t.struct(
        {
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "tableCellStyleSuggestionState": t.proxy(
                renames["TableCellStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedTableCellStyleOut"])
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "range": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
    types["InlineObjectPropertiesSuggestionStateIn"] = t.struct(
        {
            "embeddedObjectSuggestionState": t.proxy(
                renames["EmbeddedObjectSuggestionStateIn"]
            ).optional()
        }
    ).named(renames["InlineObjectPropertiesSuggestionStateIn"])
    types["InlineObjectPropertiesSuggestionStateOut"] = t.struct(
        {
            "embeddedObjectSuggestionState": t.proxy(
                renames["EmbeddedObjectSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectPropertiesSuggestionStateOut"])
    types["TableRowIn"] = t.struct(
        {
            "tableCells": t.array(t.proxy(renames["TableCellIn"])).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
            "suggestedTableRowStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "endIndex": t.integer().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "tableCells": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "suggestedTableRowStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "endIndex": t.integer().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["SheetsChartReferenceIn"] = t.struct(
        {"chartId": t.integer().optional(), "spreadsheetId": t.string().optional()}
    ).named(renames["SheetsChartReferenceIn"])
    types["SheetsChartReferenceOut"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartReferenceOut"])
    types["InsertTableRequestIn"] = t.struct(
        {
            "rows": t.integer().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "columns": t.integer().optional(),
        }
    ).named(renames["InsertTableRequestIn"])
    types["InsertTableRequestOut"] = t.struct(
        {
            "rows": t.integer().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "columns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRequestOut"])
    types["ImagePropertiesIn"] = t.struct(
        {
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "contentUri": t.string().optional(),
            "angle": t.number().optional(),
            "brightness": t.number().optional(),
            "sourceUri": t.string().optional(),
            "transparency": t.number().optional(),
            "contrast": t.number().optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "contentUri": t.string().optional(),
            "angle": t.number().optional(),
            "brightness": t.number().optional(),
            "sourceUri": t.string().optional(),
            "transparency": t.number().optional(),
            "contrast": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["HorizontalRuleIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["HorizontalRuleIn"])
    types["HorizontalRuleOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HorizontalRuleOut"])
    types["DeleteTableRowRequestIn"] = t.struct(
        {"tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional()}
    ).named(renames["DeleteTableRowRequestIn"])
    types["DeleteTableRowRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableRowRequestOut"])
    types["CreateNamedRangeRequestIn"] = t.struct(
        {"name": t.string().optional(), "range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["CreateNamedRangeRequestIn"])
    types["CreateNamedRangeRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNamedRangeRequestOut"])
    types["TableOfContentsIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
        }
    ).named(renames["TableOfContentsIn"])
    types["TableOfContentsOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOfContentsOut"])
    types["PositionedObjectPositioningSuggestionStateIn"] = t.struct(
        {
            "topOffsetSuggested": t.boolean().optional(),
            "leftOffsetSuggested": t.boolean().optional(),
            "layoutSuggested": t.boolean().optional(),
        }
    ).named(renames["PositionedObjectPositioningSuggestionStateIn"])
    types["PositionedObjectPositioningSuggestionStateOut"] = t.struct(
        {
            "topOffsetSuggested": t.boolean().optional(),
            "leftOffsetSuggested": t.boolean().optional(),
            "layoutSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningSuggestionStateOut"])
    types["BackgroundSuggestionStateIn"] = t.struct(
        {"backgroundColorSuggested": t.boolean().optional()}
    ).named(renames["BackgroundSuggestionStateIn"])
    types["BackgroundSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundSuggestionStateOut"])
    types["ShadingIn"] = t.struct(
        {"backgroundColor": t.proxy(renames["OptionalColorIn"]).optional()}
    ).named(renames["ShadingIn"])
    types["ShadingOut"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadingOut"])
    types["InlineObjectIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "suggestedInlineObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionId": t.string().optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesIn"]
            ).optional(),
        }
    ).named(renames["InlineObjectIn"])
    types["InlineObjectOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "suggestedInlineObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionId": t.string().optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectOut"])
    types["ReplaceImageRequestIn"] = t.struct(
        {
            "imageReplaceMethod": t.string().optional(),
            "uri": t.string().optional(),
            "imageObjectId": t.string().optional(),
        }
    ).named(renames["ReplaceImageRequestIn"])
    types["ReplaceImageRequestOut"] = t.struct(
        {
            "imageReplaceMethod": t.string().optional(),
            "uri": t.string().optional(),
            "imageObjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceImageRequestOut"])
    types["TextStyleIn"] = t.struct(
        {
            "strikethrough": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
            "baselineOffset": t.string().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "bold": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "italic": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "smallCaps": t.boolean().optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "strikethrough": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "baselineOffset": t.string().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "bold": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "italic": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "smallCaps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
    types["ParagraphStyleSuggestionStateIn"] = t.struct(
        {
            "indentStartSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "spaceBelowSuggested": t.boolean().optional(),
            "borderBetweenSuggested": t.boolean().optional(),
            "keepLinesTogetherSuggested": t.boolean().optional(),
            "spacingModeSuggested": t.boolean().optional(),
            "indentEndSuggested": t.boolean().optional(),
            "directionSuggested": t.boolean().optional(),
            "lineSpacingSuggested": t.boolean().optional(),
            "keepWithNextSuggested": t.boolean().optional(),
            "headingIdSuggested": t.boolean().optional(),
            "pageBreakBeforeSuggested": t.boolean().optional(),
            "namedStyleTypeSuggested": t.boolean().optional(),
            "avoidWidowAndOrphanSuggested": t.boolean().optional(),
            "shadingSuggestionState": t.proxy(
                renames["ShadingSuggestionStateIn"]
            ).optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "spaceAboveSuggested": t.boolean().optional(),
            "alignmentSuggested": t.boolean().optional(),
        }
    ).named(renames["ParagraphStyleSuggestionStateIn"])
    types["ParagraphStyleSuggestionStateOut"] = t.struct(
        {
            "indentStartSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "spaceBelowSuggested": t.boolean().optional(),
            "borderBetweenSuggested": t.boolean().optional(),
            "keepLinesTogetherSuggested": t.boolean().optional(),
            "spacingModeSuggested": t.boolean().optional(),
            "indentEndSuggested": t.boolean().optional(),
            "directionSuggested": t.boolean().optional(),
            "lineSpacingSuggested": t.boolean().optional(),
            "keepWithNextSuggested": t.boolean().optional(),
            "headingIdSuggested": t.boolean().optional(),
            "pageBreakBeforeSuggested": t.boolean().optional(),
            "namedStyleTypeSuggested": t.boolean().optional(),
            "avoidWidowAndOrphanSuggested": t.boolean().optional(),
            "shadingSuggestionState": t.proxy(
                renames["ShadingSuggestionStateOut"]
            ).optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "spaceAboveSuggested": t.boolean().optional(),
            "alignmentSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleSuggestionStateOut"])
    types["ListPropertiesIn"] = t.struct(
        {"nestingLevels": t.array(t.proxy(renames["NestingLevelIn"])).optional()}
    ).named(renames["ListPropertiesIn"])
    types["ListPropertiesOut"] = t.struct(
        {
            "nestingLevels": t.array(t.proxy(renames["NestingLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPropertiesOut"])
    types["InsertTableRowRequestIn"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "insertBelow": t.boolean().optional(),
        }
    ).named(renames["InsertTableRowRequestIn"])
    types["InsertTableRowRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "insertBelow": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRowRequestOut"])
    types["RgbColorIn"] = t.struct(
        {
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
        }
    ).named(renames["RgbColorIn"])
    types["RgbColorOut"] = t.struct(
        {
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RgbColorOut"])
    types["EquationIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["EquationIn"])
    types["EquationOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EquationOut"])
    types["SuggestedBulletIn"] = t.struct(
        {
            "bulletSuggestionState": t.proxy(
                renames["BulletSuggestionStateIn"]
            ).optional(),
            "bullet": t.proxy(renames["BulletIn"]).optional(),
        }
    ).named(renames["SuggestedBulletIn"])
    types["SuggestedBulletOut"] = t.struct(
        {
            "bulletSuggestionState": t.proxy(
                renames["BulletSuggestionStateOut"]
            ).optional(),
            "bullet": t.proxy(renames["BulletOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedBulletOut"])
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
    types["DeleteNamedRangeRequestIn"] = t.struct(
        {"name": t.string().optional(), "namedRangeId": t.string().optional()}
    ).named(renames["DeleteNamedRangeRequestIn"])
    types["DeleteNamedRangeRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteNamedRangeRequestOut"])
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "fields": t.string().optional(),
            "columnIndices": t.array(t.integer()).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "fields": t.string().optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["TableRowStyleSuggestionStateIn"] = t.struct(
        {"minRowHeightSuggested": t.boolean().optional()}
    ).named(renames["TableRowStyleSuggestionStateIn"])
    types["TableRowStyleSuggestionStateOut"] = t.struct(
        {
            "minRowHeightSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowStyleSuggestionStateOut"])
    types["DeletePositionedObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeletePositionedObjectRequestIn"])
    types["DeletePositionedObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeletePositionedObjectRequestOut"])
    types["TableCellLocationIn"] = t.struct(
        {
            "columnIndex": t.integer().optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "rowIndex": t.integer().optional(),
        }
    ).named(renames["TableCellLocationIn"])
    types["TableCellLocationOut"] = t.struct(
        {
            "columnIndex": t.integer().optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "rowIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellLocationOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
            "spacingMode": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "borderBottom": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "tabStops": t.array(t.proxy(renames["TabStopIn"])).optional(),
            "alignment": t.string().optional(),
            "namedStyleType": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "borderLeft": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "borderTop": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "lineSpacing": t.number().optional(),
            "borderBetween": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "avoidWidowAndOrphan": t.boolean().optional(),
            "keepWithNext": t.boolean().optional(),
            "keepLinesTogether": t.boolean().optional(),
            "headingId": t.string().optional(),
            "direction": t.string().optional(),
            "shading": t.proxy(renames["ShadingIn"]).optional(),
            "borderRight": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "pageBreakBefore": t.boolean().optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "spacingMode": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "borderBottom": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "tabStops": t.array(t.proxy(renames["TabStopOut"])).optional(),
            "alignment": t.string().optional(),
            "namedStyleType": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "borderLeft": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "borderTop": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "lineSpacing": t.number().optional(),
            "borderBetween": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "avoidWidowAndOrphan": t.boolean().optional(),
            "keepWithNext": t.boolean().optional(),
            "keepLinesTogether": t.boolean().optional(),
            "headingId": t.string().optional(),
            "direction": t.string().optional(),
            "shading": t.proxy(renames["ShadingOut"]).optional(),
            "borderRight": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "pageBreakBefore": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
    types["InsertInlineImageRequestIn"] = t.struct(
        {
            "objectSize": t.proxy(renames["SizeIn"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["InsertInlineImageRequestIn"])
    types["InsertInlineImageRequestOut"] = t.struct(
        {
            "objectSize": t.proxy(renames["SizeOut"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineImageRequestOut"])
    types["TextRunIn"] = t.struct(
        {
            "content": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["TextRunIn"])
    types["TextRunOut"] = t.struct(
        {
            "content": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextRunOut"])
    types["RequestIn"] = t.struct(
        {
            "pinTableHeaderRows": t.proxy(
                renames["PinTableHeaderRowsRequestIn"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "insertSectionBreak": t.proxy(
                renames["InsertSectionBreakRequestIn"]
            ).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageRequestIn"]
            ).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "deleteFooter": t.proxy(renames["DeleteFooterRequestIn"]).optional(),
            "createFooter": t.proxy(renames["CreateFooterRequestIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "updateTableCellStyle": t.proxy(
                renames["UpdateTableCellStyleRequestIn"]
            ).optional(),
            "insertPageBreak": t.proxy(renames["InsertPageBreakRequestIn"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteRequestIn"]).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "deletePositionedObject": t.proxy(
                renames["DeletePositionedObjectRequestIn"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "insertTableColumn": t.proxy(
                renames["InsertTableColumnRequestIn"]
            ).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeRequestIn"]
            ).optional(),
            "insertTable": t.proxy(renames["InsertTableRequestIn"]).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "deleteHeader": t.proxy(renames["DeleteHeaderRequestIn"]).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
            "updateTableRowStyle": t.proxy(
                renames["UpdateTableRowStyleRequestIn"]
            ).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "updateSectionStyle": t.proxy(
                renames["UpdateSectionStyleRequestIn"]
            ).optional(),
            "replaceNamedRangeContent": t.proxy(
                renames["ReplaceNamedRangeContentRequestIn"]
            ).optional(),
            "insertTableRow": t.proxy(renames["InsertTableRowRequestIn"]).optional(),
            "updateDocumentStyle": t.proxy(
                renames["UpdateDocumentStyleRequestIn"]
            ).optional(),
            "deleteContentRange": t.proxy(
                renames["DeleteContentRangeRequestIn"]
            ).optional(),
            "createHeader": t.proxy(renames["CreateHeaderRequestIn"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "pinTableHeaderRows": t.proxy(
                renames["PinTableHeaderRowsRequestOut"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "insertSectionBreak": t.proxy(
                renames["InsertSectionBreakRequestOut"]
            ).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageRequestOut"]
            ).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "deleteFooter": t.proxy(renames["DeleteFooterRequestOut"]).optional(),
            "createFooter": t.proxy(renames["CreateFooterRequestOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "updateTableCellStyle": t.proxy(
                renames["UpdateTableCellStyleRequestOut"]
            ).optional(),
            "insertPageBreak": t.proxy(renames["InsertPageBreakRequestOut"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteRequestOut"]).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "deletePositionedObject": t.proxy(
                renames["DeletePositionedObjectRequestOut"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "insertTableColumn": t.proxy(
                renames["InsertTableColumnRequestOut"]
            ).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeRequestOut"]
            ).optional(),
            "insertTable": t.proxy(renames["InsertTableRequestOut"]).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "deleteHeader": t.proxy(renames["DeleteHeaderRequestOut"]).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "updateTableRowStyle": t.proxy(
                renames["UpdateTableRowStyleRequestOut"]
            ).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "updateSectionStyle": t.proxy(
                renames["UpdateSectionStyleRequestOut"]
            ).optional(),
            "replaceNamedRangeContent": t.proxy(
                renames["ReplaceNamedRangeContentRequestOut"]
            ).optional(),
            "insertTableRow": t.proxy(renames["InsertTableRowRequestOut"]).optional(),
            "updateDocumentStyle": t.proxy(
                renames["UpdateDocumentStyleRequestOut"]
            ).optional(),
            "deleteContentRange": t.proxy(
                renames["DeleteContentRangeRequestOut"]
            ).optional(),
            "createHeader": t.proxy(renames["CreateHeaderRequestOut"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["SuggestedParagraphStyleIn"] = t.struct(
        {
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateIn"]
            ).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
        }
    ).named(renames["SuggestedParagraphStyleIn"])
    types["SuggestedParagraphStyleOut"] = t.struct(
        {
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateOut"]
            ).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedParagraphStyleOut"])
    types["AutoTextIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "type": t.string().optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "type": t.string().optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
    types["UnmergeTableCellsRequestIn"] = t.struct(
        {"tableRange": t.proxy(renames["TableRangeIn"]).optional()}
    ).named(renames["UnmergeTableCellsRequestIn"])
    types["UnmergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeTableCellsRequestOut"])

    functions = {}
    functions["documentsCreate"] = docs.post(
        "v1/documents/{documentId}:batchUpdate",
        t.struct(
            {
                "documentId": t.string().optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
                "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateDocumentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsGet"] = docs.post(
        "v1/documents/{documentId}:batchUpdate",
        t.struct(
            {
                "documentId": t.string().optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
                "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateDocumentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsBatchUpdate"] = docs.post(
        "v1/documents/{documentId}:batchUpdate",
        t.struct(
            {
                "documentId": t.string().optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
                "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateDocumentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="docs", renames=renames, types=Box(types), functions=Box(functions)
    )
