from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_docs() -> Import:
    docs = HTTPRuntime("https://docs.googleapis.com/")

    renames = {
        "ErrorResponse": "_docs_1_ErrorResponse",
        "FootnoteIn": "_docs_2_FootnoteIn",
        "FootnoteOut": "_docs_3_FootnoteOut",
        "ReplaceNamedRangeContentRequestIn": "_docs_4_ReplaceNamedRangeContentRequestIn",
        "ReplaceNamedRangeContentRequestOut": "_docs_5_ReplaceNamedRangeContentRequestOut",
        "NestingLevelIn": "_docs_6_NestingLevelIn",
        "NestingLevelOut": "_docs_7_NestingLevelOut",
        "EmbeddedDrawingPropertiesSuggestionStateIn": "_docs_8_EmbeddedDrawingPropertiesSuggestionStateIn",
        "EmbeddedDrawingPropertiesSuggestionStateOut": "_docs_9_EmbeddedDrawingPropertiesSuggestionStateOut",
        "NestingLevelSuggestionStateIn": "_docs_10_NestingLevelSuggestionStateIn",
        "NestingLevelSuggestionStateOut": "_docs_11_NestingLevelSuggestionStateOut",
        "CreateFootnoteResponseIn": "_docs_12_CreateFootnoteResponseIn",
        "CreateFootnoteResponseOut": "_docs_13_CreateFootnoteResponseOut",
        "PersonPropertiesIn": "_docs_14_PersonPropertiesIn",
        "PersonPropertiesOut": "_docs_15_PersonPropertiesOut",
        "SuggestedPositionedObjectPropertiesIn": "_docs_16_SuggestedPositionedObjectPropertiesIn",
        "SuggestedPositionedObjectPropertiesOut": "_docs_17_SuggestedPositionedObjectPropertiesOut",
        "EquationIn": "_docs_18_EquationIn",
        "EquationOut": "_docs_19_EquationOut",
        "InlineObjectIn": "_docs_20_InlineObjectIn",
        "InlineObjectOut": "_docs_21_InlineObjectOut",
        "ResponseIn": "_docs_22_ResponseIn",
        "ResponseOut": "_docs_23_ResponseOut",
        "BatchUpdateDocumentResponseIn": "_docs_24_BatchUpdateDocumentResponseIn",
        "BatchUpdateDocumentResponseOut": "_docs_25_BatchUpdateDocumentResponseOut",
        "SizeSuggestionStateIn": "_docs_26_SizeSuggestionStateIn",
        "SizeSuggestionStateOut": "_docs_27_SizeSuggestionStateOut",
        "ParagraphIn": "_docs_28_ParagraphIn",
        "ParagraphOut": "_docs_29_ParagraphOut",
        "BatchUpdateDocumentRequestIn": "_docs_30_BatchUpdateDocumentRequestIn",
        "BatchUpdateDocumentRequestOut": "_docs_31_BatchUpdateDocumentRequestOut",
        "SuggestedNamedStylesIn": "_docs_32_SuggestedNamedStylesIn",
        "SuggestedNamedStylesOut": "_docs_33_SuggestedNamedStylesOut",
        "InsertTableRowRequestIn": "_docs_34_InsertTableRowRequestIn",
        "InsertTableRowRequestOut": "_docs_35_InsertTableRowRequestOut",
        "DeleteHeaderRequestIn": "_docs_36_DeleteHeaderRequestIn",
        "DeleteHeaderRequestOut": "_docs_37_DeleteHeaderRequestOut",
        "TabStopIn": "_docs_38_TabStopIn",
        "TabStopOut": "_docs_39_TabStopOut",
        "ListIn": "_docs_40_ListIn",
        "ListOut": "_docs_41_ListOut",
        "EmbeddedObjectBorderIn": "_docs_42_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_docs_43_EmbeddedObjectBorderOut",
        "DocumentIn": "_docs_44_DocumentIn",
        "DocumentOut": "_docs_45_DocumentOut",
        "PersonIn": "_docs_46_PersonIn",
        "PersonOut": "_docs_47_PersonOut",
        "ParagraphStyleSuggestionStateIn": "_docs_48_ParagraphStyleSuggestionStateIn",
        "ParagraphStyleSuggestionStateOut": "_docs_49_ParagraphStyleSuggestionStateOut",
        "SuggestedTableCellStyleIn": "_docs_50_SuggestedTableCellStyleIn",
        "SuggestedTableCellStyleOut": "_docs_51_SuggestedTableCellStyleOut",
        "UpdateSectionStyleRequestIn": "_docs_52_UpdateSectionStyleRequestIn",
        "UpdateSectionStyleRequestOut": "_docs_53_UpdateSectionStyleRequestOut",
        "NamedRangeIn": "_docs_54_NamedRangeIn",
        "NamedRangeOut": "_docs_55_NamedRangeOut",
        "LocationIn": "_docs_56_LocationIn",
        "LocationOut": "_docs_57_LocationOut",
        "TextStyleIn": "_docs_58_TextStyleIn",
        "TextStyleOut": "_docs_59_TextStyleOut",
        "SectionColumnPropertiesIn": "_docs_60_SectionColumnPropertiesIn",
        "SectionColumnPropertiesOut": "_docs_61_SectionColumnPropertiesOut",
        "DeleteTableColumnRequestIn": "_docs_62_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_docs_63_DeleteTableColumnRequestOut",
        "LinkedContentReferenceSuggestionStateIn": "_docs_64_LinkedContentReferenceSuggestionStateIn",
        "LinkedContentReferenceSuggestionStateOut": "_docs_65_LinkedContentReferenceSuggestionStateOut",
        "InsertTableRequestIn": "_docs_66_InsertTableRequestIn",
        "InsertTableRequestOut": "_docs_67_InsertTableRequestOut",
        "ParagraphBorderIn": "_docs_68_ParagraphBorderIn",
        "ParagraphBorderOut": "_docs_69_ParagraphBorderOut",
        "EmbeddedDrawingPropertiesIn": "_docs_70_EmbeddedDrawingPropertiesIn",
        "EmbeddedDrawingPropertiesOut": "_docs_71_EmbeddedDrawingPropertiesOut",
        "LinkIn": "_docs_72_LinkIn",
        "LinkOut": "_docs_73_LinkOut",
        "CropPropertiesIn": "_docs_74_CropPropertiesIn",
        "CropPropertiesOut": "_docs_75_CropPropertiesOut",
        "ParagraphElementIn": "_docs_76_ParagraphElementIn",
        "ParagraphElementOut": "_docs_77_ParagraphElementOut",
        "LinkedContentReferenceIn": "_docs_78_LinkedContentReferenceIn",
        "LinkedContentReferenceOut": "_docs_79_LinkedContentReferenceOut",
        "StructuralElementIn": "_docs_80_StructuralElementIn",
        "StructuralElementOut": "_docs_81_StructuralElementOut",
        "CreateHeaderRequestIn": "_docs_82_CreateHeaderRequestIn",
        "CreateHeaderRequestOut": "_docs_83_CreateHeaderRequestOut",
        "WeightedFontFamilyIn": "_docs_84_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_docs_85_WeightedFontFamilyOut",
        "SubstringMatchCriteriaIn": "_docs_86_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_docs_87_SubstringMatchCriteriaOut",
        "NamedRangesIn": "_docs_88_NamedRangesIn",
        "NamedRangesOut": "_docs_89_NamedRangesOut",
        "TableRowStyleSuggestionStateIn": "_docs_90_TableRowStyleSuggestionStateIn",
        "TableRowStyleSuggestionStateOut": "_docs_91_TableRowStyleSuggestionStateOut",
        "BodyIn": "_docs_92_BodyIn",
        "BodyOut": "_docs_93_BodyOut",
        "PositionedObjectPositioningIn": "_docs_94_PositionedObjectPositioningIn",
        "PositionedObjectPositioningOut": "_docs_95_PositionedObjectPositioningOut",
        "SuggestedBulletIn": "_docs_96_SuggestedBulletIn",
        "SuggestedBulletOut": "_docs_97_SuggestedBulletOut",
        "TableCellLocationIn": "_docs_98_TableCellLocationIn",
        "TableCellLocationOut": "_docs_99_TableCellLocationOut",
        "UpdateTableColumnPropertiesRequestIn": "_docs_100_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_docs_101_UpdateTableColumnPropertiesRequestOut",
        "DeletePositionedObjectRequestIn": "_docs_102_DeletePositionedObjectRequestIn",
        "DeletePositionedObjectRequestOut": "_docs_103_DeletePositionedObjectRequestOut",
        "UpdateTextStyleRequestIn": "_docs_104_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_docs_105_UpdateTextStyleRequestOut",
        "DocumentStyleSuggestionStateIn": "_docs_106_DocumentStyleSuggestionStateIn",
        "DocumentStyleSuggestionStateOut": "_docs_107_DocumentStyleSuggestionStateOut",
        "MergeTableCellsRequestIn": "_docs_108_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_docs_109_MergeTableCellsRequestOut",
        "SuggestedTextStyleIn": "_docs_110_SuggestedTextStyleIn",
        "SuggestedTextStyleOut": "_docs_111_SuggestedTextStyleOut",
        "SuggestedTableRowStyleIn": "_docs_112_SuggestedTableRowStyleIn",
        "SuggestedTableRowStyleOut": "_docs_113_SuggestedTableRowStyleOut",
        "TableOfContentsIn": "_docs_114_TableOfContentsIn",
        "TableOfContentsOut": "_docs_115_TableOfContentsOut",
        "ShadingIn": "_docs_116_ShadingIn",
        "ShadingOut": "_docs_117_ShadingOut",
        "EmbeddedObjectSuggestionStateIn": "_docs_118_EmbeddedObjectSuggestionStateIn",
        "EmbeddedObjectSuggestionStateOut": "_docs_119_EmbeddedObjectSuggestionStateOut",
        "CropPropertiesSuggestionStateIn": "_docs_120_CropPropertiesSuggestionStateIn",
        "CropPropertiesSuggestionStateOut": "_docs_121_CropPropertiesSuggestionStateOut",
        "PositionedObjectPropertiesSuggestionStateIn": "_docs_122_PositionedObjectPropertiesSuggestionStateIn",
        "PositionedObjectPropertiesSuggestionStateOut": "_docs_123_PositionedObjectPropertiesSuggestionStateOut",
        "InsertInlineSheetsChartResponseIn": "_docs_124_InsertInlineSheetsChartResponseIn",
        "InsertInlineSheetsChartResponseOut": "_docs_125_InsertInlineSheetsChartResponseOut",
        "ReplaceAllTextRequestIn": "_docs_126_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_docs_127_ReplaceAllTextRequestOut",
        "InsertTextRequestIn": "_docs_128_InsertTextRequestIn",
        "InsertTextRequestOut": "_docs_129_InsertTextRequestOut",
        "SheetsChartReferenceIn": "_docs_130_SheetsChartReferenceIn",
        "SheetsChartReferenceOut": "_docs_131_SheetsChartReferenceOut",
        "HorizontalRuleIn": "_docs_132_HorizontalRuleIn",
        "HorizontalRuleOut": "_docs_133_HorizontalRuleOut",
        "CreateNamedRangeRequestIn": "_docs_134_CreateNamedRangeRequestIn",
        "CreateNamedRangeRequestOut": "_docs_135_CreateNamedRangeRequestOut",
        "EndOfSegmentLocationIn": "_docs_136_EndOfSegmentLocationIn",
        "EndOfSegmentLocationOut": "_docs_137_EndOfSegmentLocationOut",
        "FootnoteReferenceIn": "_docs_138_FootnoteReferenceIn",
        "FootnoteReferenceOut": "_docs_139_FootnoteReferenceOut",
        "CreateFooterResponseIn": "_docs_140_CreateFooterResponseIn",
        "CreateFooterResponseOut": "_docs_141_CreateFooterResponseOut",
        "NamedStyleIn": "_docs_142_NamedStyleIn",
        "NamedStyleOut": "_docs_143_NamedStyleOut",
        "DocumentStyleIn": "_docs_144_DocumentStyleIn",
        "DocumentStyleOut": "_docs_145_DocumentStyleOut",
        "OptionalColorIn": "_docs_146_OptionalColorIn",
        "OptionalColorOut": "_docs_147_OptionalColorOut",
        "CreateParagraphBulletsRequestIn": "_docs_148_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_docs_149_CreateParagraphBulletsRequestOut",
        "TableCellStyleIn": "_docs_150_TableCellStyleIn",
        "TableCellStyleOut": "_docs_151_TableCellStyleOut",
        "RichLinkPropertiesIn": "_docs_152_RichLinkPropertiesIn",
        "RichLinkPropertiesOut": "_docs_153_RichLinkPropertiesOut",
        "WriteControlIn": "_docs_154_WriteControlIn",
        "WriteControlOut": "_docs_155_WriteControlOut",
        "PositionedObjectPropertiesIn": "_docs_156_PositionedObjectPropertiesIn",
        "PositionedObjectPropertiesOut": "_docs_157_PositionedObjectPropertiesOut",
        "TableIn": "_docs_158_TableIn",
        "TableOut": "_docs_159_TableOut",
        "PositionedObjectIn": "_docs_160_PositionedObjectIn",
        "PositionedObjectOut": "_docs_161_PositionedObjectOut",
        "TextStyleSuggestionStateIn": "_docs_162_TextStyleSuggestionStateIn",
        "TextStyleSuggestionStateOut": "_docs_163_TextStyleSuggestionStateOut",
        "ReplaceImageRequestIn": "_docs_164_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_docs_165_ReplaceImageRequestOut",
        "ImagePropertiesSuggestionStateIn": "_docs_166_ImagePropertiesSuggestionStateIn",
        "ImagePropertiesSuggestionStateOut": "_docs_167_ImagePropertiesSuggestionStateOut",
        "BulletSuggestionStateIn": "_docs_168_BulletSuggestionStateIn",
        "BulletSuggestionStateOut": "_docs_169_BulletSuggestionStateOut",
        "AutoTextIn": "_docs_170_AutoTextIn",
        "AutoTextOut": "_docs_171_AutoTextOut",
        "SheetsChartReferenceSuggestionStateIn": "_docs_172_SheetsChartReferenceSuggestionStateIn",
        "SheetsChartReferenceSuggestionStateOut": "_docs_173_SheetsChartReferenceSuggestionStateOut",
        "UpdateDocumentStyleRequestIn": "_docs_174_UpdateDocumentStyleRequestIn",
        "UpdateDocumentStyleRequestOut": "_docs_175_UpdateDocumentStyleRequestOut",
        "UpdateTableCellStyleRequestIn": "_docs_176_UpdateTableCellStyleRequestIn",
        "UpdateTableCellStyleRequestOut": "_docs_177_UpdateTableCellStyleRequestOut",
        "NamedStyleSuggestionStateIn": "_docs_178_NamedStyleSuggestionStateIn",
        "NamedStyleSuggestionStateOut": "_docs_179_NamedStyleSuggestionStateOut",
        "DeleteNamedRangeRequestIn": "_docs_180_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_docs_181_DeleteNamedRangeRequestOut",
        "SizeIn": "_docs_182_SizeIn",
        "SizeOut": "_docs_183_SizeOut",
        "SuggestedListPropertiesIn": "_docs_184_SuggestedListPropertiesIn",
        "SuggestedListPropertiesOut": "_docs_185_SuggestedListPropertiesOut",
        "TableCellStyleSuggestionStateIn": "_docs_186_TableCellStyleSuggestionStateIn",
        "TableCellStyleSuggestionStateOut": "_docs_187_TableCellStyleSuggestionStateOut",
        "DeleteContentRangeRequestIn": "_docs_188_DeleteContentRangeRequestIn",
        "DeleteContentRangeRequestOut": "_docs_189_DeleteContentRangeRequestOut",
        "TableRangeIn": "_docs_190_TableRangeIn",
        "TableRangeOut": "_docs_191_TableRangeOut",
        "FooterIn": "_docs_192_FooterIn",
        "FooterOut": "_docs_193_FooterOut",
        "RichLinkIn": "_docs_194_RichLinkIn",
        "RichLinkOut": "_docs_195_RichLinkOut",
        "TextRunIn": "_docs_196_TextRunIn",
        "TextRunOut": "_docs_197_TextRunOut",
        "TableColumnPropertiesIn": "_docs_198_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_docs_199_TableColumnPropertiesOut",
        "TableRowIn": "_docs_200_TableRowIn",
        "TableRowOut": "_docs_201_TableRowOut",
        "InlineObjectPropertiesSuggestionStateIn": "_docs_202_InlineObjectPropertiesSuggestionStateIn",
        "InlineObjectPropertiesSuggestionStateOut": "_docs_203_InlineObjectPropertiesSuggestionStateOut",
        "InsertPageBreakRequestIn": "_docs_204_InsertPageBreakRequestIn",
        "InsertPageBreakRequestOut": "_docs_205_InsertPageBreakRequestOut",
        "UpdateTableRowStyleRequestIn": "_docs_206_UpdateTableRowStyleRequestIn",
        "UpdateTableRowStyleRequestOut": "_docs_207_UpdateTableRowStyleRequestOut",
        "CreateFootnoteRequestIn": "_docs_208_CreateFootnoteRequestIn",
        "CreateFootnoteRequestOut": "_docs_209_CreateFootnoteRequestOut",
        "PageBreakIn": "_docs_210_PageBreakIn",
        "PageBreakOut": "_docs_211_PageBreakOut",
        "DeleteFooterRequestIn": "_docs_212_DeleteFooterRequestIn",
        "DeleteFooterRequestOut": "_docs_213_DeleteFooterRequestOut",
        "SuggestedParagraphStyleIn": "_docs_214_SuggestedParagraphStyleIn",
        "SuggestedParagraphStyleOut": "_docs_215_SuggestedParagraphStyleOut",
        "ColumnBreakIn": "_docs_216_ColumnBreakIn",
        "ColumnBreakOut": "_docs_217_ColumnBreakOut",
        "SuggestedInlineObjectPropertiesIn": "_docs_218_SuggestedInlineObjectPropertiesIn",
        "SuggestedInlineObjectPropertiesOut": "_docs_219_SuggestedInlineObjectPropertiesOut",
        "BulletIn": "_docs_220_BulletIn",
        "BulletOut": "_docs_221_BulletOut",
        "ObjectReferencesIn": "_docs_222_ObjectReferencesIn",
        "ObjectReferencesOut": "_docs_223_ObjectReferencesOut",
        "InlineObjectPropertiesIn": "_docs_224_InlineObjectPropertiesIn",
        "InlineObjectPropertiesOut": "_docs_225_InlineObjectPropertiesOut",
        "TableCellIn": "_docs_226_TableCellIn",
        "TableCellOut": "_docs_227_TableCellOut",
        "NamedStylesSuggestionStateIn": "_docs_228_NamedStylesSuggestionStateIn",
        "NamedStylesSuggestionStateOut": "_docs_229_NamedStylesSuggestionStateOut",
        "InsertInlineImageRequestIn": "_docs_230_InsertInlineImageRequestIn",
        "InsertInlineImageRequestOut": "_docs_231_InsertInlineImageRequestOut",
        "ListPropertiesIn": "_docs_232_ListPropertiesIn",
        "ListPropertiesOut": "_docs_233_ListPropertiesOut",
        "ColorIn": "_docs_234_ColorIn",
        "ColorOut": "_docs_235_ColorOut",
        "RequestIn": "_docs_236_RequestIn",
        "RequestOut": "_docs_237_RequestOut",
        "ImagePropertiesIn": "_docs_238_ImagePropertiesIn",
        "ImagePropertiesOut": "_docs_239_ImagePropertiesOut",
        "InsertTableColumnRequestIn": "_docs_240_InsertTableColumnRequestIn",
        "InsertTableColumnRequestOut": "_docs_241_InsertTableColumnRequestOut",
        "DeleteParagraphBulletsRequestIn": "_docs_242_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_docs_243_DeleteParagraphBulletsRequestOut",
        "SectionBreakIn": "_docs_244_SectionBreakIn",
        "SectionBreakOut": "_docs_245_SectionBreakOut",
        "TableRowStyleIn": "_docs_246_TableRowStyleIn",
        "TableRowStyleOut": "_docs_247_TableRowStyleOut",
        "PinTableHeaderRowsRequestIn": "_docs_248_PinTableHeaderRowsRequestIn",
        "PinTableHeaderRowsRequestOut": "_docs_249_PinTableHeaderRowsRequestOut",
        "NamedStylesIn": "_docs_250_NamedStylesIn",
        "NamedStylesOut": "_docs_251_NamedStylesOut",
        "PositionedObjectPositioningSuggestionStateIn": "_docs_252_PositionedObjectPositioningSuggestionStateIn",
        "PositionedObjectPositioningSuggestionStateOut": "_docs_253_PositionedObjectPositioningSuggestionStateOut",
        "InlineObjectElementIn": "_docs_254_InlineObjectElementIn",
        "InlineObjectElementOut": "_docs_255_InlineObjectElementOut",
        "DeleteTableRowRequestIn": "_docs_256_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_docs_257_DeleteTableRowRequestOut",
        "CreateNamedRangeResponseIn": "_docs_258_CreateNamedRangeResponseIn",
        "CreateNamedRangeResponseOut": "_docs_259_CreateNamedRangeResponseOut",
        "ShadingSuggestionStateIn": "_docs_260_ShadingSuggestionStateIn",
        "ShadingSuggestionStateOut": "_docs_261_ShadingSuggestionStateOut",
        "DimensionIn": "_docs_262_DimensionIn",
        "DimensionOut": "_docs_263_DimensionOut",
        "HeaderIn": "_docs_264_HeaderIn",
        "HeaderOut": "_docs_265_HeaderOut",
        "CreateHeaderResponseIn": "_docs_266_CreateHeaderResponseIn",
        "CreateHeaderResponseOut": "_docs_267_CreateHeaderResponseOut",
        "BackgroundSuggestionStateIn": "_docs_268_BackgroundSuggestionStateIn",
        "BackgroundSuggestionStateOut": "_docs_269_BackgroundSuggestionStateOut",
        "ParagraphStyleIn": "_docs_270_ParagraphStyleIn",
        "ParagraphStyleOut": "_docs_271_ParagraphStyleOut",
        "CreateFooterRequestIn": "_docs_272_CreateFooterRequestIn",
        "CreateFooterRequestOut": "_docs_273_CreateFooterRequestOut",
        "TableCellBorderIn": "_docs_274_TableCellBorderIn",
        "TableCellBorderOut": "_docs_275_TableCellBorderOut",
        "ReplaceAllTextResponseIn": "_docs_276_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_docs_277_ReplaceAllTextResponseOut",
        "UpdateParagraphStyleRequestIn": "_docs_278_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_docs_279_UpdateParagraphStyleRequestOut",
        "RgbColorIn": "_docs_280_RgbColorIn",
        "RgbColorOut": "_docs_281_RgbColorOut",
        "EmbeddedObjectBorderSuggestionStateIn": "_docs_282_EmbeddedObjectBorderSuggestionStateIn",
        "EmbeddedObjectBorderSuggestionStateOut": "_docs_283_EmbeddedObjectBorderSuggestionStateOut",
        "TableStyleIn": "_docs_284_TableStyleIn",
        "TableStyleOut": "_docs_285_TableStyleOut",
        "EmbeddedObjectIn": "_docs_286_EmbeddedObjectIn",
        "EmbeddedObjectOut": "_docs_287_EmbeddedObjectOut",
        "ListPropertiesSuggestionStateIn": "_docs_288_ListPropertiesSuggestionStateIn",
        "ListPropertiesSuggestionStateOut": "_docs_289_ListPropertiesSuggestionStateOut",
        "BackgroundIn": "_docs_290_BackgroundIn",
        "BackgroundOut": "_docs_291_BackgroundOut",
        "SectionStyleIn": "_docs_292_SectionStyleIn",
        "SectionStyleOut": "_docs_293_SectionStyleOut",
        "InsertInlineImageResponseIn": "_docs_294_InsertInlineImageResponseIn",
        "InsertInlineImageResponseOut": "_docs_295_InsertInlineImageResponseOut",
        "InsertSectionBreakRequestIn": "_docs_296_InsertSectionBreakRequestIn",
        "InsertSectionBreakRequestOut": "_docs_297_InsertSectionBreakRequestOut",
        "SuggestedDocumentStyleIn": "_docs_298_SuggestedDocumentStyleIn",
        "SuggestedDocumentStyleOut": "_docs_299_SuggestedDocumentStyleOut",
        "UnmergeTableCellsRequestIn": "_docs_300_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_docs_301_UnmergeTableCellsRequestOut",
        "RangeIn": "_docs_302_RangeIn",
        "RangeOut": "_docs_303_RangeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FootnoteIn"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "footnoteId": t.string().optional(),
        }
    ).named(renames["FootnoteIn"])
    types["FootnoteOut"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "footnoteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FootnoteOut"])
    types["ReplaceNamedRangeContentRequestIn"] = t.struct(
        {
            "text": t.string().optional(),
            "namedRangeName": t.string().optional(),
            "namedRangeId": t.string().optional(),
        }
    ).named(renames["ReplaceNamedRangeContentRequestIn"])
    types["ReplaceNamedRangeContentRequestOut"] = t.struct(
        {
            "text": t.string().optional(),
            "namedRangeName": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceNamedRangeContentRequestOut"])
    types["NestingLevelIn"] = t.struct(
        {
            "bulletAlignment": t.string().optional(),
            "glyphSymbol": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "glyphFormat": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "startNumber": t.integer().optional(),
            "glyphType": t.string().optional(),
        }
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "bulletAlignment": t.string().optional(),
            "glyphSymbol": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "glyphFormat": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "startNumber": t.integer().optional(),
            "glyphType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
    types["EmbeddedDrawingPropertiesSuggestionStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EmbeddedDrawingPropertiesSuggestionStateIn"])
    types["EmbeddedDrawingPropertiesSuggestionStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmbeddedDrawingPropertiesSuggestionStateOut"])
    types["NestingLevelSuggestionStateIn"] = t.struct(
        {
            "glyphFormatSuggested": t.boolean().optional(),
            "glyphTypeSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "startNumberSuggested": t.boolean().optional(),
            "glyphSymbolSuggested": t.boolean().optional(),
            "bulletAlignmentSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
        }
    ).named(renames["NestingLevelSuggestionStateIn"])
    types["NestingLevelSuggestionStateOut"] = t.struct(
        {
            "glyphFormatSuggested": t.boolean().optional(),
            "glyphTypeSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "startNumberSuggested": t.boolean().optional(),
            "glyphSymbolSuggested": t.boolean().optional(),
            "bulletAlignmentSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelSuggestionStateOut"])
    types["CreateFootnoteResponseIn"] = t.struct(
        {"footnoteId": t.string().optional()}
    ).named(renames["CreateFootnoteResponseIn"])
    types["CreateFootnoteResponseOut"] = t.struct(
        {
            "footnoteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFootnoteResponseOut"])
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
    types["SuggestedPositionedObjectPropertiesIn"] = t.struct(
        {
            "positionedObjectPropertiesSuggestionState": t.proxy(
                renames["PositionedObjectPropertiesSuggestionStateIn"]
            ).optional(),
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesIn"]
            ).optional(),
        }
    ).named(renames["SuggestedPositionedObjectPropertiesIn"])
    types["SuggestedPositionedObjectPropertiesOut"] = t.struct(
        {
            "positionedObjectPropertiesSuggestionState": t.proxy(
                renames["PositionedObjectPropertiesSuggestionStateOut"]
            ).optional(),
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedPositionedObjectPropertiesOut"])
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
    types["InlineObjectIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesIn"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInlineObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
        }
    ).named(renames["InlineObjectIn"])
    types["InlineObjectOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesOut"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInlineObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectOut"])
    types["ResponseIn"] = t.struct(
        {
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageResponseIn"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterResponseIn"]).optional(),
            "insertInlineSheetsChart": t.proxy(
                renames["InsertInlineSheetsChartResponseIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "createHeader": t.proxy(renames["CreateHeaderResponseIn"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeResponseIn"]
            ).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteResponseIn"]).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageResponseOut"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterResponseOut"]).optional(),
            "insertInlineSheetsChart": t.proxy(
                renames["InsertInlineSheetsChartResponseOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "createHeader": t.proxy(renames["CreateHeaderResponseOut"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeResponseOut"]
            ).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["BatchUpdateDocumentResponseIn"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "documentId": t.string().optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdateDocumentResponseIn"])
    types["BatchUpdateDocumentResponseOut"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "documentId": t.string().optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDocumentResponseOut"])
    types["SizeSuggestionStateIn"] = t.struct(
        {
            "heightSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
        }
    ).named(renames["SizeSuggestionStateIn"])
    types["SizeSuggestionStateOut"] = t.struct(
        {
            "heightSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SizeSuggestionStateOut"])
    types["ParagraphIn"] = t.struct(
        {
            "positionedObjectIds": t.array(t.string()).optional(),
            "suggestedBulletChanges": t.struct({"_": t.string().optional()}).optional(),
            "suggestedPositionedObjectIds": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "elements": t.array(t.proxy(renames["ParagraphElementIn"])).optional(),
            "suggestedParagraphStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "bullet": t.proxy(renames["BulletIn"]).optional(),
        }
    ).named(renames["ParagraphIn"])
    types["ParagraphOut"] = t.struct(
        {
            "positionedObjectIds": t.array(t.string()).optional(),
            "suggestedBulletChanges": t.struct({"_": t.string().optional()}).optional(),
            "suggestedPositionedObjectIds": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "elements": t.array(t.proxy(renames["ParagraphElementOut"])).optional(),
            "suggestedParagraphStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "bullet": t.proxy(renames["BulletOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphOut"])
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
    types["SuggestedNamedStylesIn"] = t.struct(
        {
            "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
            "namedStylesSuggestionState": t.proxy(
                renames["NamedStylesSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedNamedStylesIn"])
    types["SuggestedNamedStylesOut"] = t.struct(
        {
            "namedStyles": t.proxy(renames["NamedStylesOut"]).optional(),
            "namedStylesSuggestionState": t.proxy(
                renames["NamedStylesSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedNamedStylesOut"])
    types["InsertTableRowRequestIn"] = t.struct(
        {
            "insertBelow": t.boolean().optional(),
            "tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["InsertTableRowRequestIn"])
    types["InsertTableRowRequestOut"] = t.struct(
        {
            "insertBelow": t.boolean().optional(),
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRowRequestOut"])
    types["DeleteHeaderRequestIn"] = t.struct(
        {"headerId": t.string().optional()}
    ).named(renames["DeleteHeaderRequestIn"])
    types["DeleteHeaderRequestOut"] = t.struct(
        {
            "headerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteHeaderRequestOut"])
    types["TabStopIn"] = t.struct(
        {
            "alignment": t.string().optional(),
            "offset": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["TabStopIn"])
    types["TabStopOut"] = t.struct(
        {
            "alignment": t.string().optional(),
            "offset": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TabStopOut"])
    types["ListIn"] = t.struct(
        {
            "listProperties": t.proxy(renames["ListPropertiesIn"]).optional(),
            "suggestedListPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["ListIn"])
    types["ListOut"] = t.struct(
        {
            "listProperties": t.proxy(renames["ListPropertiesOut"]).optional(),
            "suggestedListPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOut"])
    types["EmbeddedObjectBorderIn"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "dashStyle": t.string().optional(),
            "propertyState": t.string().optional(),
        }
    ).named(renames["EmbeddedObjectBorderIn"])
    types["EmbeddedObjectBorderOut"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "propertyState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderOut"])
    types["DocumentIn"] = t.struct(
        {
            "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
            "revisionId": t.string().optional(),
            "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
            "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
            "body": t.proxy(renames["BodyIn"]).optional(),
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "namedRanges": t.struct({"_": t.string().optional()}).optional(),
            "footers": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "footnotes": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "documentId": t.string().optional(),
            "suggestedNamedStylesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDocumentStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestionsViewMode": t.string().optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleOut"]).optional(),
            "revisionId": t.string().optional(),
            "namedStyles": t.proxy(renames["NamedStylesOut"]).optional(),
            "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
            "body": t.proxy(renames["BodyOut"]).optional(),
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "namedRanges": t.struct({"_": t.string().optional()}).optional(),
            "footers": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "footnotes": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "documentId": t.string().optional(),
            "suggestedNamedStylesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDocumentStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestionsViewMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
    types["PersonIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "personProperties": t.proxy(renames["PersonPropertiesOut"]).optional(),
            "personId": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["ParagraphStyleSuggestionStateIn"] = t.struct(
        {
            "borderTopSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "lineSpacingSuggested": t.boolean().optional(),
            "keepLinesTogetherSuggested": t.boolean().optional(),
            "alignmentSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "indentEndSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "borderBetweenSuggested": t.boolean().optional(),
            "shadingSuggestionState": t.proxy(
                renames["ShadingSuggestionStateIn"]
            ).optional(),
            "pageBreakBeforeSuggested": t.boolean().optional(),
            "headingIdSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "keepWithNextSuggested": t.boolean().optional(),
            "directionSuggested": t.boolean().optional(),
            "avoidWidowAndOrphanSuggested": t.boolean().optional(),
            "spaceAboveSuggested": t.boolean().optional(),
            "spaceBelowSuggested": t.boolean().optional(),
            "namedStyleTypeSuggested": t.boolean().optional(),
            "spacingModeSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
        }
    ).named(renames["ParagraphStyleSuggestionStateIn"])
    types["ParagraphStyleSuggestionStateOut"] = t.struct(
        {
            "borderTopSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "lineSpacingSuggested": t.boolean().optional(),
            "keepLinesTogetherSuggested": t.boolean().optional(),
            "alignmentSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "indentEndSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "borderBetweenSuggested": t.boolean().optional(),
            "shadingSuggestionState": t.proxy(
                renames["ShadingSuggestionStateOut"]
            ).optional(),
            "pageBreakBeforeSuggested": t.boolean().optional(),
            "headingIdSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "keepWithNextSuggested": t.boolean().optional(),
            "directionSuggested": t.boolean().optional(),
            "avoidWidowAndOrphanSuggested": t.boolean().optional(),
            "spaceAboveSuggested": t.boolean().optional(),
            "spaceBelowSuggested": t.boolean().optional(),
            "namedStyleTypeSuggested": t.boolean().optional(),
            "spacingModeSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleSuggestionStateOut"])
    types["SuggestedTableCellStyleIn"] = t.struct(
        {
            "tableCellStyleSuggestionState": t.proxy(
                renames["TableCellStyleSuggestionStateIn"]
            ).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
        }
    ).named(renames["SuggestedTableCellStyleIn"])
    types["SuggestedTableCellStyleOut"] = t.struct(
        {
            "tableCellStyleSuggestionState": t.proxy(
                renames["TableCellStyleSuggestionStateOut"]
            ).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedTableCellStyleOut"])
    types["UpdateSectionStyleRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["RangeIn"]).optional(),
            "fields": t.string().optional(),
            "sectionStyle": t.proxy(renames["SectionStyleIn"]).optional(),
        }
    ).named(renames["UpdateSectionStyleRequestIn"])
    types["UpdateSectionStyleRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "fields": t.string().optional(),
            "sectionStyle": t.proxy(renames["SectionStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSectionStyleRequestOut"])
    types["NamedRangeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "ranges": t.array(t.proxy(renames["RangeIn"])).optional(),
            "namedRangeId": t.string().optional(),
        }
    ).named(renames["NamedRangeIn"])
    types["NamedRangeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "ranges": t.array(t.proxy(renames["RangeOut"])).optional(),
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedRangeOut"])
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
    types["TextStyleIn"] = t.struct(
        {
            "link": t.proxy(renames["LinkIn"]).optional(),
            "bold": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "italic": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "strikethrough": t.boolean().optional(),
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "link": t.proxy(renames["LinkOut"]).optional(),
            "bold": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "italic": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "strikethrough": t.boolean().optional(),
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
    types["SectionColumnPropertiesIn"] = t.struct(
        {
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "paddingEnd": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["SectionColumnPropertiesIn"])
    types["SectionColumnPropertiesOut"] = t.struct(
        {
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "paddingEnd": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionColumnPropertiesOut"])
    types["DeleteTableColumnRequestIn"] = t.struct(
        {"tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional()}
    ).named(renames["DeleteTableColumnRequestIn"])
    types["DeleteTableColumnRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableColumnRequestOut"])
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
    types["InsertTableRequestIn"] = t.struct(
        {
            "columns": t.integer().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "rows": t.integer().optional(),
        }
    ).named(renames["InsertTableRequestIn"])
    types["InsertTableRequestOut"] = t.struct(
        {
            "columns": t.integer().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "rows": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRequestOut"])
    types["ParagraphBorderIn"] = t.struct(
        {
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "dashStyle": t.string().optional(),
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
            "padding": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["ParagraphBorderIn"])
    types["ParagraphBorderOut"] = t.struct(
        {
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "padding": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphBorderOut"])
    types["EmbeddedDrawingPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EmbeddedDrawingPropertiesIn"]
    )
    types["EmbeddedDrawingPropertiesOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmbeddedDrawingPropertiesOut"])
    types["LinkIn"] = t.struct(
        {
            "bookmarkId": t.string().optional(),
            "url": t.string().optional(),
            "headingId": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "bookmarkId": t.string().optional(),
            "url": t.string().optional(),
            "headingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["CropPropertiesIn"] = t.struct(
        {
            "offsetTop": t.number().optional(),
            "offsetRight": t.number().optional(),
            "offsetBottom": t.number().optional(),
            "angle": t.number().optional(),
            "offsetLeft": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "offsetTop": t.number().optional(),
            "offsetRight": t.number().optional(),
            "offsetBottom": t.number().optional(),
            "angle": t.number().optional(),
            "offsetLeft": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
    types["ParagraphElementIn"] = t.struct(
        {
            "pageBreak": t.proxy(renames["PageBreakIn"]).optional(),
            "footnoteReference": t.proxy(renames["FootnoteReferenceIn"]).optional(),
            "richLink": t.proxy(renames["RichLinkIn"]).optional(),
            "horizontalRule": t.proxy(renames["HorizontalRuleIn"]).optional(),
            "endIndex": t.integer().optional(),
            "inlineObjectElement": t.proxy(renames["InlineObjectElementIn"]).optional(),
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
            "startIndex": t.integer().optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "equation": t.proxy(renames["EquationIn"]).optional(),
            "person": t.proxy(renames["PersonIn"]).optional(),
            "columnBreak": t.proxy(renames["ColumnBreakIn"]).optional(),
        }
    ).named(renames["ParagraphElementIn"])
    types["ParagraphElementOut"] = t.struct(
        {
            "pageBreak": t.proxy(renames["PageBreakOut"]).optional(),
            "footnoteReference": t.proxy(renames["FootnoteReferenceOut"]).optional(),
            "richLink": t.proxy(renames["RichLinkOut"]).optional(),
            "horizontalRule": t.proxy(renames["HorizontalRuleOut"]).optional(),
            "endIndex": t.integer().optional(),
            "inlineObjectElement": t.proxy(
                renames["InlineObjectElementOut"]
            ).optional(),
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "startIndex": t.integer().optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "equation": t.proxy(renames["EquationOut"]).optional(),
            "person": t.proxy(renames["PersonOut"]).optional(),
            "columnBreak": t.proxy(renames["ColumnBreakOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphElementOut"])
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
    types["StructuralElementIn"] = t.struct(
        {
            "sectionBreak": t.proxy(renames["SectionBreakIn"]).optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "startIndex": t.integer().optional(),
            "paragraph": t.proxy(renames["ParagraphIn"]).optional(),
            "endIndex": t.integer().optional(),
            "tableOfContents": t.proxy(renames["TableOfContentsIn"]).optional(),
        }
    ).named(renames["StructuralElementIn"])
    types["StructuralElementOut"] = t.struct(
        {
            "sectionBreak": t.proxy(renames["SectionBreakOut"]).optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "startIndex": t.integer().optional(),
            "paragraph": t.proxy(renames["ParagraphOut"]).optional(),
            "endIndex": t.integer().optional(),
            "tableOfContents": t.proxy(renames["TableOfContentsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuralElementOut"])
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
    types["TableRowStyleSuggestionStateIn"] = t.struct(
        {"minRowHeightSuggested": t.boolean().optional()}
    ).named(renames["TableRowStyleSuggestionStateIn"])
    types["TableRowStyleSuggestionStateOut"] = t.struct(
        {
            "minRowHeightSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowStyleSuggestionStateOut"])
    types["BodyIn"] = t.struct(
        {"content": t.array(t.proxy(renames["StructuralElementIn"])).optional()}
    ).named(renames["BodyIn"])
    types["BodyOut"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BodyOut"])
    types["PositionedObjectPositioningIn"] = t.struct(
        {
            "leftOffset": t.proxy(renames["DimensionIn"]).optional(),
            "layout": t.string().optional(),
            "topOffset": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningIn"])
    types["PositionedObjectPositioningOut"] = t.struct(
        {
            "leftOffset": t.proxy(renames["DimensionOut"]).optional(),
            "layout": t.string().optional(),
            "topOffset": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningOut"])
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
    types["TableCellLocationIn"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["TableCellLocationIn"])
    types["TableCellLocationOut"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellLocationOut"])
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["DeletePositionedObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeletePositionedObjectRequestIn"])
    types["DeletePositionedObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeletePositionedObjectRequestOut"])
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
    types["DocumentStyleSuggestionStateIn"] = t.struct(
        {
            "firstPageHeaderIdSuggested": t.boolean().optional(),
            "marginFooterSuggested": t.boolean().optional(),
            "defaultFooterIdSuggested": t.boolean().optional(),
            "useEvenPageHeaderFooterSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "pageNumberStartSuggested": t.boolean().optional(),
            "useFirstPageHeaderFooterSuggested": t.boolean().optional(),
            "useCustomHeaderFooterMarginsSuggested": t.boolean().optional(),
            "firstPageFooterIdSuggested": t.boolean().optional(),
            "evenPageFooterIdSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "pageSizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateIn"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "backgroundSuggestionState": t.proxy(
                renames["BackgroundSuggestionStateIn"]
            ).optional(),
            "marginHeaderSuggested": t.boolean().optional(),
            "defaultHeaderIdSuggested": t.boolean().optional(),
            "evenPageHeaderIdSuggested": t.boolean().optional(),
        }
    ).named(renames["DocumentStyleSuggestionStateIn"])
    types["DocumentStyleSuggestionStateOut"] = t.struct(
        {
            "firstPageHeaderIdSuggested": t.boolean().optional(),
            "marginFooterSuggested": t.boolean().optional(),
            "defaultFooterIdSuggested": t.boolean().optional(),
            "useEvenPageHeaderFooterSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "pageNumberStartSuggested": t.boolean().optional(),
            "useFirstPageHeaderFooterSuggested": t.boolean().optional(),
            "useCustomHeaderFooterMarginsSuggested": t.boolean().optional(),
            "firstPageFooterIdSuggested": t.boolean().optional(),
            "evenPageFooterIdSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "pageSizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateOut"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "backgroundSuggestionState": t.proxy(
                renames["BackgroundSuggestionStateOut"]
            ).optional(),
            "marginHeaderSuggested": t.boolean().optional(),
            "defaultHeaderIdSuggested": t.boolean().optional(),
            "evenPageHeaderIdSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentStyleSuggestionStateOut"])
    types["MergeTableCellsRequestIn"] = t.struct(
        {"tableRange": t.proxy(renames["TableRangeIn"]).optional()}
    ).named(renames["MergeTableCellsRequestIn"])
    types["MergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeTableCellsRequestOut"])
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
    types["SuggestedTableRowStyleIn"] = t.struct(
        {
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
            "tableRowStyleSuggestionState": t.proxy(
                renames["TableRowStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedTableRowStyleIn"])
    types["SuggestedTableRowStyleOut"] = t.struct(
        {
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "tableRowStyleSuggestionState": t.proxy(
                renames["TableRowStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedTableRowStyleOut"])
    types["TableOfContentsIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["TableOfContentsIn"])
    types["TableOfContentsOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOfContentsOut"])
    types["ShadingIn"] = t.struct(
        {"backgroundColor": t.proxy(renames["OptionalColorIn"]).optional()}
    ).named(renames["ShadingIn"])
    types["ShadingOut"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadingOut"])
    types["EmbeddedObjectSuggestionStateIn"] = t.struct(
        {
            "imagePropertiesSuggestionState": t.proxy(
                renames["ImagePropertiesSuggestionStateIn"]
            ).optional(),
            "linkedContentReferenceSuggestionState": t.proxy(
                renames["LinkedContentReferenceSuggestionStateIn"]
            ).optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "sizeSuggestionState": t.proxy(renames["SizeSuggestionStateIn"]).optional(),
            "embeddedObjectBorderSuggestionState": t.proxy(
                renames["EmbeddedObjectBorderSuggestionStateIn"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "titleSuggested": t.boolean().optional(),
            "descriptionSuggested": t.boolean().optional(),
            "embeddedDrawingPropertiesSuggestionState": t.proxy(
                renames["EmbeddedDrawingPropertiesSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["EmbeddedObjectSuggestionStateIn"])
    types["EmbeddedObjectSuggestionStateOut"] = t.struct(
        {
            "imagePropertiesSuggestionState": t.proxy(
                renames["ImagePropertiesSuggestionStateOut"]
            ).optional(),
            "linkedContentReferenceSuggestionState": t.proxy(
                renames["LinkedContentReferenceSuggestionStateOut"]
            ).optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "sizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateOut"]
            ).optional(),
            "embeddedObjectBorderSuggestionState": t.proxy(
                renames["EmbeddedObjectBorderSuggestionStateOut"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "titleSuggested": t.boolean().optional(),
            "descriptionSuggested": t.boolean().optional(),
            "embeddedDrawingPropertiesSuggestionState": t.proxy(
                renames["EmbeddedDrawingPropertiesSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectSuggestionStateOut"])
    types["CropPropertiesSuggestionStateIn"] = t.struct(
        {
            "offsetBottomSuggested": t.boolean().optional(),
            "offsetLeftSuggested": t.boolean().optional(),
            "offsetTopSuggested": t.boolean().optional(),
            "offsetRightSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
        }
    ).named(renames["CropPropertiesSuggestionStateIn"])
    types["CropPropertiesSuggestionStateOut"] = t.struct(
        {
            "offsetBottomSuggested": t.boolean().optional(),
            "offsetLeftSuggested": t.boolean().optional(),
            "offsetTopSuggested": t.boolean().optional(),
            "offsetRightSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesSuggestionStateOut"])
    types["PositionedObjectPropertiesSuggestionStateIn"] = t.struct(
        {
            "positioningSuggestionState": t.proxy(
                renames["PositionedObjectPositioningSuggestionStateIn"]
            ).optional(),
            "embeddedObjectSuggestionState": t.proxy(
                renames["EmbeddedObjectSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["PositionedObjectPropertiesSuggestionStateIn"])
    types["PositionedObjectPropertiesSuggestionStateOut"] = t.struct(
        {
            "positioningSuggestionState": t.proxy(
                renames["PositionedObjectPositioningSuggestionStateOut"]
            ).optional(),
            "embeddedObjectSuggestionState": t.proxy(
                renames["EmbeddedObjectSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPropertiesSuggestionStateOut"])
    types["InsertInlineSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["InsertInlineSheetsChartResponseIn"])
    types["InsertInlineSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineSheetsChartResponseOut"])
    types["ReplaceAllTextRequestIn"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaIn"]).optional(),
            "replaceText": t.string().optional(),
        }
    ).named(renames["ReplaceAllTextRequestIn"])
    types["ReplaceAllTextRequestOut"] = t.struct(
        {
            "containsText": t.proxy(renames["SubstringMatchCriteriaOut"]).optional(),
            "replaceText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextRequestOut"])
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
    types["SheetsChartReferenceIn"] = t.struct(
        {"spreadsheetId": t.string().optional(), "chartId": t.integer().optional()}
    ).named(renames["SheetsChartReferenceIn"])
    types["SheetsChartReferenceOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartReferenceOut"])
    types["HorizontalRuleIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["HorizontalRuleIn"])
    types["HorizontalRuleOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HorizontalRuleOut"])
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
    types["EndOfSegmentLocationIn"] = t.struct(
        {"segmentId": t.string().optional()}
    ).named(renames["EndOfSegmentLocationIn"])
    types["EndOfSegmentLocationOut"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndOfSegmentLocationOut"])
    types["FootnoteReferenceIn"] = t.struct(
        {
            "footnoteNumber": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "footnoteId": t.string().optional(),
        }
    ).named(renames["FootnoteReferenceIn"])
    types["FootnoteReferenceOut"] = t.struct(
        {
            "footnoteNumber": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "footnoteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FootnoteReferenceOut"])
    types["CreateFooterResponseIn"] = t.struct(
        {"footerId": t.string().optional()}
    ).named(renames["CreateFooterResponseIn"])
    types["CreateFooterResponseOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFooterResponseOut"])
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
    types["DocumentStyleIn"] = t.struct(
        {
            "evenPageHeaderId": t.string().optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "defaultFooterId": t.string().optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "marginHeader": t.proxy(renames["DimensionIn"]).optional(),
            "defaultHeaderId": t.string().optional(),
            "background": t.proxy(renames["BackgroundIn"]).optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginFooter": t.proxy(renames["DimensionIn"]).optional(),
            "firstPageFooterId": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "firstPageHeaderId": t.string().optional(),
            "useCustomHeaderFooterMargins": t.boolean().optional(),
            "useEvenPageHeaderFooter": t.boolean().optional(),
        }
    ).named(renames["DocumentStyleIn"])
    types["DocumentStyleOut"] = t.struct(
        {
            "evenPageHeaderId": t.string().optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "defaultFooterId": t.string().optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "marginHeader": t.proxy(renames["DimensionOut"]).optional(),
            "defaultHeaderId": t.string().optional(),
            "background": t.proxy(renames["BackgroundOut"]).optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginFooter": t.proxy(renames["DimensionOut"]).optional(),
            "firstPageFooterId": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "firstPageHeaderId": t.string().optional(),
            "useCustomHeaderFooterMargins": t.boolean().optional(),
            "useEvenPageHeaderFooter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentStyleOut"])
    types["OptionalColorIn"] = t.struct(
        {"color": t.proxy(renames["ColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
    types["CreateParagraphBulletsRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["RangeIn"]).optional(),
            "bulletPreset": t.string().optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestIn"])
    types["CreateParagraphBulletsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "bulletPreset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateParagraphBulletsRequestOut"])
    types["TableCellStyleIn"] = t.struct(
        {
            "rowSpan": t.integer().optional(),
            "borderLeft": t.proxy(renames["TableCellBorderIn"]).optional(),
            "borderRight": t.proxy(renames["TableCellBorderIn"]).optional(),
            "paddingLeft": t.proxy(renames["DimensionIn"]).optional(),
            "columnSpan": t.integer().optional(),
            "paddingBottom": t.proxy(renames["DimensionIn"]).optional(),
            "borderBottom": t.proxy(renames["TableCellBorderIn"]).optional(),
            "borderTop": t.proxy(renames["TableCellBorderIn"]).optional(),
            "paddingTop": t.proxy(renames["DimensionIn"]).optional(),
            "paddingRight": t.proxy(renames["DimensionIn"]).optional(),
            "contentAlignment": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
        }
    ).named(renames["TableCellStyleIn"])
    types["TableCellStyleOut"] = t.struct(
        {
            "rowSpan": t.integer().optional(),
            "borderLeft": t.proxy(renames["TableCellBorderOut"]).optional(),
            "borderRight": t.proxy(renames["TableCellBorderOut"]).optional(),
            "paddingLeft": t.proxy(renames["DimensionOut"]).optional(),
            "columnSpan": t.integer().optional(),
            "paddingBottom": t.proxy(renames["DimensionOut"]).optional(),
            "borderBottom": t.proxy(renames["TableCellBorderOut"]).optional(),
            "borderTop": t.proxy(renames["TableCellBorderOut"]).optional(),
            "paddingTop": t.proxy(renames["DimensionOut"]).optional(),
            "paddingRight": t.proxy(renames["DimensionOut"]).optional(),
            "contentAlignment": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellStyleOut"])
    types["RichLinkPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RichLinkPropertiesIn"]
    )
    types["RichLinkPropertiesOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "title": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichLinkPropertiesOut"])
    types["WriteControlIn"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "targetRevisionId": t.string().optional(),
        }
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "targetRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
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
    types["TableIn"] = t.struct(
        {
            "rows": t.integer().optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "columns": t.integer().optional(),
            "tableStyle": t.proxy(renames["TableStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "rows": t.integer().optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "columns": t.integer().optional(),
            "tableStyle": t.proxy(renames["TableStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["PositionedObjectIn"] = t.struct(
        {
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesIn"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "objectId": t.string().optional(),
            "suggestedPositionedObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
        }
    ).named(renames["PositionedObjectIn"])
    types["PositionedObjectOut"] = t.struct(
        {
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesOut"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "objectId": t.string().optional(),
            "suggestedPositionedObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectOut"])
    types["TextStyleSuggestionStateIn"] = t.struct(
        {
            "foregroundColorSuggested": t.boolean().optional(),
            "smallCapsSuggested": t.boolean().optional(),
            "boldSuggested": t.boolean().optional(),
            "linkSuggested": t.boolean().optional(),
            "italicSuggested": t.boolean().optional(),
            "strikethroughSuggested": t.boolean().optional(),
            "baselineOffsetSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "fontSizeSuggested": t.boolean().optional(),
            "weightedFontFamilySuggested": t.boolean().optional(),
            "underlineSuggested": t.boolean().optional(),
        }
    ).named(renames["TextStyleSuggestionStateIn"])
    types["TextStyleSuggestionStateOut"] = t.struct(
        {
            "foregroundColorSuggested": t.boolean().optional(),
            "smallCapsSuggested": t.boolean().optional(),
            "boldSuggested": t.boolean().optional(),
            "linkSuggested": t.boolean().optional(),
            "italicSuggested": t.boolean().optional(),
            "strikethroughSuggested": t.boolean().optional(),
            "baselineOffsetSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "fontSizeSuggested": t.boolean().optional(),
            "weightedFontFamilySuggested": t.boolean().optional(),
            "underlineSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleSuggestionStateOut"])
    types["ReplaceImageRequestIn"] = t.struct(
        {
            "imageReplaceMethod": t.string().optional(),
            "imageObjectId": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["ReplaceImageRequestIn"])
    types["ReplaceImageRequestOut"] = t.struct(
        {
            "imageReplaceMethod": t.string().optional(),
            "imageObjectId": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceImageRequestOut"])
    types["ImagePropertiesSuggestionStateIn"] = t.struct(
        {
            "contrastSuggested": t.boolean().optional(),
            "sourceUriSuggested": t.boolean().optional(),
            "cropPropertiesSuggestionState": t.proxy(
                renames["CropPropertiesSuggestionStateIn"]
            ).optional(),
            "transparencySuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "contentUriSuggested": t.boolean().optional(),
            "brightnessSuggested": t.boolean().optional(),
        }
    ).named(renames["ImagePropertiesSuggestionStateIn"])
    types["ImagePropertiesSuggestionStateOut"] = t.struct(
        {
            "contrastSuggested": t.boolean().optional(),
            "sourceUriSuggested": t.boolean().optional(),
            "cropPropertiesSuggestionState": t.proxy(
                renames["CropPropertiesSuggestionStateOut"]
            ).optional(),
            "transparencySuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "contentUriSuggested": t.boolean().optional(),
            "brightnessSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesSuggestionStateOut"])
    types["BulletSuggestionStateIn"] = t.struct(
        {
            "listIdSuggested": t.boolean().optional(),
            "nestingLevelSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["BulletSuggestionStateIn"])
    types["BulletSuggestionStateOut"] = t.struct(
        {
            "listIdSuggested": t.boolean().optional(),
            "nestingLevelSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletSuggestionStateOut"])
    types["AutoTextIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
    types["SheetsChartReferenceSuggestionStateIn"] = t.struct(
        {
            "spreadsheetIdSuggested": t.boolean().optional(),
            "chartIdSuggested": t.boolean().optional(),
        }
    ).named(renames["SheetsChartReferenceSuggestionStateIn"])
    types["SheetsChartReferenceSuggestionStateOut"] = t.struct(
        {
            "spreadsheetIdSuggested": t.boolean().optional(),
            "chartIdSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsChartReferenceSuggestionStateOut"])
    types["UpdateDocumentStyleRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
        }
    ).named(renames["UpdateDocumentStyleRequestIn"])
    types["UpdateDocumentStyleRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "documentStyle": t.proxy(renames["DocumentStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDocumentStyleRequestOut"])
    types["UpdateTableCellStyleRequestIn"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
        }
    ).named(renames["UpdateTableCellStyleRequestIn"])
    types["UpdateTableCellStyleRequestOut"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellStyleRequestOut"])
    types["NamedStyleSuggestionStateIn"] = t.struct(
        {
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateIn"]
            ).optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
            "namedStyleType": t.string().optional(),
        }
    ).named(renames["NamedStyleSuggestionStateIn"])
    types["NamedStyleSuggestionStateOut"] = t.struct(
        {
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateOut"]
            ).optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "namedStyleType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStyleSuggestionStateOut"])
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
    types["SuggestedListPropertiesIn"] = t.struct(
        {
            "listPropertiesSuggestionState": t.proxy(
                renames["ListPropertiesSuggestionStateIn"]
            ).optional(),
            "listProperties": t.proxy(renames["ListPropertiesIn"]).optional(),
        }
    ).named(renames["SuggestedListPropertiesIn"])
    types["SuggestedListPropertiesOut"] = t.struct(
        {
            "listPropertiesSuggestionState": t.proxy(
                renames["ListPropertiesSuggestionStateOut"]
            ).optional(),
            "listProperties": t.proxy(renames["ListPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedListPropertiesOut"])
    types["TableCellStyleSuggestionStateIn"] = t.struct(
        {
            "paddingTopSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "paddingLeftSuggested": t.boolean().optional(),
            "paddingBottomSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "contentAlignmentSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "rowSpanSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "columnSpanSuggested": t.boolean().optional(),
            "paddingRightSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
        }
    ).named(renames["TableCellStyleSuggestionStateIn"])
    types["TableCellStyleSuggestionStateOut"] = t.struct(
        {
            "paddingTopSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "paddingLeftSuggested": t.boolean().optional(),
            "paddingBottomSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "contentAlignmentSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "rowSpanSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "columnSpanSuggested": t.boolean().optional(),
            "paddingRightSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellStyleSuggestionStateOut"])
    types["DeleteContentRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["DeleteContentRangeRequestIn"])
    types["DeleteContentRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteContentRangeRequestOut"])
    types["TableRangeIn"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
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
    types["RichLinkIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["RichLinkIn"])
    types["RichLinkOut"] = t.struct(
        {
            "richLinkId": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "richLinkProperties": t.proxy(renames["RichLinkPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichLinkOut"])
    types["TextRunIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["TextRunIn"])
    types["TextRunOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextRunOut"])
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
    types["TableRowIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTableRowStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "tableCells": t.array(t.proxy(renames["TableCellIn"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "endIndex": t.integer().optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
        }
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTableRowStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "tableCells": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "endIndex": t.integer().optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
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
    types["UpdateTableRowStyleRequestIn"] = t.struct(
        {
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableRowStyleRequestIn"])
    types["UpdateTableRowStyleRequestOut"] = t.struct(
        {
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowStyleRequestOut"])
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
    types["PageBreakIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["PageBreakIn"])
    types["PageBreakOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBreakOut"])
    types["DeleteFooterRequestIn"] = t.struct(
        {"footerId": t.string().optional()}
    ).named(renames["DeleteFooterRequestIn"])
    types["DeleteFooterRequestOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFooterRequestOut"])
    types["SuggestedParagraphStyleIn"] = t.struct(
        {
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedParagraphStyleIn"])
    types["SuggestedParagraphStyleOut"] = t.struct(
        {
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedParagraphStyleOut"])
    types["ColumnBreakIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["ColumnBreakIn"])
    types["ColumnBreakOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnBreakOut"])
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
    types["BulletIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "nestingLevel": t.integer().optional(),
            "listId": t.string().optional(),
        }
    ).named(renames["BulletIn"])
    types["BulletOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "nestingLevel": t.integer().optional(),
            "listId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletOut"])
    types["ObjectReferencesIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["ObjectReferencesIn"])
    types["ObjectReferencesOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectReferencesOut"])
    types["InlineObjectPropertiesIn"] = t.struct(
        {"embeddedObject": t.proxy(renames["EmbeddedObjectIn"]).optional()}
    ).named(renames["InlineObjectPropertiesIn"])
    types["InlineObjectPropertiesOut"] = t.struct(
        {
            "embeddedObject": t.proxy(renames["EmbeddedObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectPropertiesOut"])
    types["TableCellIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
            "suggestedTableCellStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "suggestedTableCellStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
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
    types["InsertInlineImageRequestIn"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "objectSize": t.proxy(renames["SizeIn"]).optional(),
            "uri": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["InsertInlineImageRequestIn"])
    types["InsertInlineImageRequestOut"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "objectSize": t.proxy(renames["SizeOut"]).optional(),
            "uri": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineImageRequestOut"])
    types["ListPropertiesIn"] = t.struct(
        {"nestingLevels": t.array(t.proxy(renames["NestingLevelIn"])).optional()}
    ).named(renames["ListPropertiesIn"])
    types["ListPropertiesOut"] = t.struct(
        {
            "nestingLevels": t.array(t.proxy(renames["NestingLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPropertiesOut"])
    types["ColorIn"] = t.struct(
        {"rgbColor": t.proxy(renames["RgbColorIn"]).optional()}
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "rgbColor": t.proxy(renames["RgbColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["RequestIn"] = t.struct(
        {
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "updateTableRowStyle": t.proxy(
                renames["UpdateTableRowStyleRequestIn"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageRequestIn"]
            ).optional(),
            "insertPageBreak": t.proxy(renames["InsertPageBreakRequestIn"]).optional(),
            "deleteHeader": t.proxy(renames["DeleteHeaderRequestIn"]).optional(),
            "updateDocumentStyle": t.proxy(
                renames["UpdateDocumentStyleRequestIn"]
            ).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteRequestIn"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "updateSectionStyle": t.proxy(
                renames["UpdateSectionStyleRequestIn"]
            ).optional(),
            "updateTableCellStyle": t.proxy(
                renames["UpdateTableCellStyleRequestIn"]
            ).optional(),
            "deleteContentRange": t.proxy(
                renames["DeleteContentRangeRequestIn"]
            ).optional(),
            "insertTable": t.proxy(renames["InsertTableRequestIn"]).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "createHeader": t.proxy(renames["CreateHeaderRequestIn"]).optional(),
            "pinTableHeaderRows": t.proxy(
                renames["PinTableHeaderRowsRequestIn"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeRequestIn"]
            ).optional(),
            "insertTableColumn": t.proxy(
                renames["InsertTableColumnRequestIn"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterRequestIn"]).optional(),
            "insertTableRow": t.proxy(renames["InsertTableRowRequestIn"]).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "deleteFooter": t.proxy(renames["DeleteFooterRequestIn"]).optional(),
            "deletePositionedObject": t.proxy(
                renames["DeletePositionedObjectRequestIn"]
            ).optional(),
            "replaceNamedRangeContent": t.proxy(
                renames["ReplaceNamedRangeContentRequestIn"]
            ).optional(),
            "insertSectionBreak": t.proxy(
                renames["InsertSectionBreakRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "updateTableRowStyle": t.proxy(
                renames["UpdateTableRowStyleRequestOut"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageRequestOut"]
            ).optional(),
            "insertPageBreak": t.proxy(renames["InsertPageBreakRequestOut"]).optional(),
            "deleteHeader": t.proxy(renames["DeleteHeaderRequestOut"]).optional(),
            "updateDocumentStyle": t.proxy(
                renames["UpdateDocumentStyleRequestOut"]
            ).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteRequestOut"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "updateSectionStyle": t.proxy(
                renames["UpdateSectionStyleRequestOut"]
            ).optional(),
            "updateTableCellStyle": t.proxy(
                renames["UpdateTableCellStyleRequestOut"]
            ).optional(),
            "deleteContentRange": t.proxy(
                renames["DeleteContentRangeRequestOut"]
            ).optional(),
            "insertTable": t.proxy(renames["InsertTableRequestOut"]).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "createHeader": t.proxy(renames["CreateHeaderRequestOut"]).optional(),
            "pinTableHeaderRows": t.proxy(
                renames["PinTableHeaderRowsRequestOut"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeRequestOut"]
            ).optional(),
            "insertTableColumn": t.proxy(
                renames["InsertTableColumnRequestOut"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterRequestOut"]).optional(),
            "insertTableRow": t.proxy(renames["InsertTableRowRequestOut"]).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "deleteFooter": t.proxy(renames["DeleteFooterRequestOut"]).optional(),
            "deletePositionedObject": t.proxy(
                renames["DeletePositionedObjectRequestOut"]
            ).optional(),
            "replaceNamedRangeContent": t.proxy(
                renames["ReplaceNamedRangeContentRequestOut"]
            ).optional(),
            "insertSectionBreak": t.proxy(
                renames["InsertSectionBreakRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["ImagePropertiesIn"] = t.struct(
        {
            "brightness": t.number().optional(),
            "sourceUri": t.string().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "angle": t.number().optional(),
            "contrast": t.number().optional(),
            "transparency": t.number().optional(),
            "contentUri": t.string().optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "brightness": t.number().optional(),
            "sourceUri": t.string().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "angle": t.number().optional(),
            "contrast": t.number().optional(),
            "transparency": t.number().optional(),
            "contentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["InsertTableColumnRequestIn"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "insertRight": t.boolean().optional(),
        }
    ).named(renames["InsertTableColumnRequestIn"])
    types["InsertTableColumnRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "insertRight": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableColumnRequestOut"])
    types["DeleteParagraphBulletsRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["DeleteParagraphBulletsRequestIn"])
    types["DeleteParagraphBulletsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestOut"])
    types["SectionBreakIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "sectionStyle": t.proxy(renames["SectionStyleIn"]).optional(),
        }
    ).named(renames["SectionBreakIn"])
    types["SectionBreakOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "sectionStyle": t.proxy(renames["SectionStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionBreakOut"])
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
    types["PinTableHeaderRowsRequestIn"] = t.struct(
        {
            "pinnedHeaderRowsCount": t.integer().optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["PinTableHeaderRowsRequestIn"])
    types["PinTableHeaderRowsRequestOut"] = t.struct(
        {
            "pinnedHeaderRowsCount": t.integer().optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PinTableHeaderRowsRequestOut"])
    types["NamedStylesIn"] = t.struct(
        {"styles": t.array(t.proxy(renames["NamedStyleIn"])).optional()}
    ).named(renames["NamedStylesIn"])
    types["NamedStylesOut"] = t.struct(
        {
            "styles": t.array(t.proxy(renames["NamedStyleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStylesOut"])
    types["PositionedObjectPositioningSuggestionStateIn"] = t.struct(
        {
            "leftOffsetSuggested": t.boolean().optional(),
            "topOffsetSuggested": t.boolean().optional(),
            "layoutSuggested": t.boolean().optional(),
        }
    ).named(renames["PositionedObjectPositioningSuggestionStateIn"])
    types["PositionedObjectPositioningSuggestionStateOut"] = t.struct(
        {
            "leftOffsetSuggested": t.boolean().optional(),
            "topOffsetSuggested": t.boolean().optional(),
            "layoutSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningSuggestionStateOut"])
    types["InlineObjectElementIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "inlineObjectId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["InlineObjectElementIn"])
    types["InlineObjectElementOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "inlineObjectId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectElementOut"])
    types["DeleteTableRowRequestIn"] = t.struct(
        {"tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional()}
    ).named(renames["DeleteTableRowRequestIn"])
    types["DeleteTableRowRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableRowRequestOut"])
    types["CreateNamedRangeResponseIn"] = t.struct(
        {"namedRangeId": t.string().optional()}
    ).named(renames["CreateNamedRangeResponseIn"])
    types["CreateNamedRangeResponseOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNamedRangeResponseOut"])
    types["ShadingSuggestionStateIn"] = t.struct(
        {"backgroundColorSuggested": t.boolean().optional()}
    ).named(renames["ShadingSuggestionStateIn"])
    types["ShadingSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadingSuggestionStateOut"])
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
    types["HeaderIn"] = t.struct(
        {
            "headerId": t.string().optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
        }
    ).named(renames["HeaderIn"])
    types["HeaderOut"] = t.struct(
        {
            "headerId": t.string().optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeaderOut"])
    types["CreateHeaderResponseIn"] = t.struct(
        {"headerId": t.string().optional()}
    ).named(renames["CreateHeaderResponseIn"])
    types["CreateHeaderResponseOut"] = t.struct(
        {
            "headerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateHeaderResponseOut"])
    types["BackgroundSuggestionStateIn"] = t.struct(
        {"backgroundColorSuggested": t.boolean().optional()}
    ).named(renames["BackgroundSuggestionStateIn"])
    types["BackgroundSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundSuggestionStateOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "pageBreakBefore": t.boolean().optional(),
            "keepLinesTogether": t.boolean().optional(),
            "shading": t.proxy(renames["ShadingIn"]).optional(),
            "borderBetween": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "keepWithNext": t.boolean().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "lineSpacing": t.number().optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "headingId": t.string().optional(),
            "borderLeft": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "namedStyleType": t.string().optional(),
            "avoidWidowAndOrphan": t.boolean().optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "spacingMode": t.string().optional(),
            "borderTop": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "borderRight": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "direction": t.string().optional(),
            "alignment": t.string().optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
            "tabStops": t.array(t.proxy(renames["TabStopIn"])).optional(),
            "borderBottom": t.proxy(renames["ParagraphBorderIn"]).optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "pageBreakBefore": t.boolean().optional(),
            "keepLinesTogether": t.boolean().optional(),
            "shading": t.proxy(renames["ShadingOut"]).optional(),
            "borderBetween": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "keepWithNext": t.boolean().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "lineSpacing": t.number().optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "headingId": t.string().optional(),
            "borderLeft": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "namedStyleType": t.string().optional(),
            "avoidWidowAndOrphan": t.boolean().optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "spacingMode": t.string().optional(),
            "borderTop": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "borderRight": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "direction": t.string().optional(),
            "alignment": t.string().optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "tabStops": t.array(t.proxy(renames["TabStopOut"])).optional(),
            "borderBottom": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
    types["CreateFooterRequestIn"] = t.struct(
        {
            "type": t.string().optional(),
            "sectionBreakLocation": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["CreateFooterRequestIn"])
    types["CreateFooterRequestOut"] = t.struct(
        {
            "type": t.string().optional(),
            "sectionBreakLocation": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFooterRequestOut"])
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
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "fields": t.string().optional(),
            "range": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "fields": t.string().optional(),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])
    types["RgbColorIn"] = t.struct(
        {
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["RgbColorIn"])
    types["RgbColorOut"] = t.struct(
        {
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RgbColorOut"])
    types["EmbeddedObjectBorderSuggestionStateIn"] = t.struct(
        {
            "dashStyleSuggested": t.boolean().optional(),
            "propertyStateSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
            "colorSuggested": t.boolean().optional(),
        }
    ).named(renames["EmbeddedObjectBorderSuggestionStateIn"])
    types["EmbeddedObjectBorderSuggestionStateOut"] = t.struct(
        {
            "dashStyleSuggested": t.boolean().optional(),
            "propertyStateSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
            "colorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderSuggestionStateOut"])
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
    types["EmbeddedObjectIn"] = t.struct(
        {
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "title": t.string().optional(),
            "embeddedDrawingProperties": t.proxy(
                renames["EmbeddedDrawingPropertiesIn"]
            ).optional(),
            "linkedContentReference": t.proxy(
                renames["LinkedContentReferenceIn"]
            ).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "description": t.string().optional(),
            "embeddedObjectBorder": t.proxy(
                renames["EmbeddedObjectBorderIn"]
            ).optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["EmbeddedObjectIn"])
    types["EmbeddedObjectOut"] = t.struct(
        {
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "title": t.string().optional(),
            "embeddedDrawingProperties": t.proxy(
                renames["EmbeddedDrawingPropertiesOut"]
            ).optional(),
            "linkedContentReference": t.proxy(
                renames["LinkedContentReferenceOut"]
            ).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "description": t.string().optional(),
            "embeddedObjectBorder": t.proxy(
                renames["EmbeddedObjectBorderOut"]
            ).optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectOut"])
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
    types["BackgroundIn"] = t.struct(
        {"color": t.proxy(renames["OptionalColorIn"]).optional()}
    ).named(renames["BackgroundIn"])
    types["BackgroundOut"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundOut"])
    types["SectionStyleIn"] = t.struct(
        {
            "sectionType": t.string().optional(),
            "defaultFooterId": t.string().optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "firstPageFooterId": t.string().optional(),
            "columnProperties": t.array(
                t.proxy(renames["SectionColumnPropertiesIn"])
            ).optional(),
            "contentDirection": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "marginFooter": t.proxy(renames["DimensionIn"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "columnSeparatorStyle": t.string().optional(),
            "marginHeader": t.proxy(renames["DimensionIn"]).optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "defaultHeaderId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "evenPageHeaderId": t.string().optional(),
        }
    ).named(renames["SectionStyleIn"])
    types["SectionStyleOut"] = t.struct(
        {
            "sectionType": t.string().optional(),
            "defaultFooterId": t.string().optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "firstPageFooterId": t.string().optional(),
            "columnProperties": t.array(
                t.proxy(renames["SectionColumnPropertiesOut"])
            ).optional(),
            "contentDirection": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "marginFooter": t.proxy(renames["DimensionOut"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "columnSeparatorStyle": t.string().optional(),
            "marginHeader": t.proxy(renames["DimensionOut"]).optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "defaultHeaderId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "evenPageHeaderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionStyleOut"])
    types["InsertInlineImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["InsertInlineImageResponseIn"])
    types["InsertInlineImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineImageResponseOut"])
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
    types["SuggestedDocumentStyleIn"] = t.struct(
        {
            "documentStyleSuggestionState": t.proxy(
                renames["DocumentStyleSuggestionStateIn"]
            ).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
        }
    ).named(renames["SuggestedDocumentStyleIn"])
    types["SuggestedDocumentStyleOut"] = t.struct(
        {
            "documentStyleSuggestionState": t.proxy(
                renames["DocumentStyleSuggestionStateOut"]
            ).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedDocumentStyleOut"])
    types["UnmergeTableCellsRequestIn"] = t.struct(
        {"tableRange": t.proxy(renames["TableRangeIn"]).optional()}
    ).named(renames["UnmergeTableCellsRequestIn"])
    types["UnmergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeTableCellsRequestOut"])
    types["RangeIn"] = t.struct(
        {
            "endIndex": t.integer().optional(),
            "segmentId": t.string().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "endIndex": t.integer().optional(),
            "segmentId": t.string().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])

    functions = {}
    functions["documentsBatchUpdate"] = docs.post(
        "v1/documents",
        t.struct(
            {
                "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
                "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
                "revisionId": t.string().optional(),
                "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
                "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
                "body": t.proxy(renames["BodyIn"]).optional(),
                "lists": t.struct({"_": t.string().optional()}).optional(),
                "namedRanges": t.struct({"_": t.string().optional()}).optional(),
                "footers": t.struct({"_": t.string().optional()}).optional(),
                "headers": t.struct({"_": t.string().optional()}).optional(),
                "footnotes": t.struct({"_": t.string().optional()}).optional(),
                "title": t.string().optional(),
                "documentId": t.string().optional(),
                "suggestedNamedStylesChanges": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "suggestedDocumentStyleChanges": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "suggestionsViewMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsGet"] = docs.post(
        "v1/documents",
        t.struct(
            {
                "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
                "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
                "revisionId": t.string().optional(),
                "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
                "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
                "body": t.proxy(renames["BodyIn"]).optional(),
                "lists": t.struct({"_": t.string().optional()}).optional(),
                "namedRanges": t.struct({"_": t.string().optional()}).optional(),
                "footers": t.struct({"_": t.string().optional()}).optional(),
                "headers": t.struct({"_": t.string().optional()}).optional(),
                "footnotes": t.struct({"_": t.string().optional()}).optional(),
                "title": t.string().optional(),
                "documentId": t.string().optional(),
                "suggestedNamedStylesChanges": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "suggestedDocumentStyleChanges": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "suggestionsViewMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsCreate"] = docs.post(
        "v1/documents",
        t.struct(
            {
                "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
                "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
                "revisionId": t.string().optional(),
                "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
                "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
                "body": t.proxy(renames["BodyIn"]).optional(),
                "lists": t.struct({"_": t.string().optional()}).optional(),
                "namedRanges": t.struct({"_": t.string().optional()}).optional(),
                "footers": t.struct({"_": t.string().optional()}).optional(),
                "headers": t.struct({"_": t.string().optional()}).optional(),
                "footnotes": t.struct({"_": t.string().optional()}).optional(),
                "title": t.string().optional(),
                "documentId": t.string().optional(),
                "suggestedNamedStylesChanges": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "suggestedDocumentStyleChanges": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "suggestionsViewMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="docs", renames=renames, types=types, functions=functions)
