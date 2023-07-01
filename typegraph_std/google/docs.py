from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_docs():
    docs = HTTPRuntime("https://docs.googleapis.com/")

    renames = {
        "ErrorResponse": "_docs_1_ErrorResponse",
        "CreateHeaderRequestIn": "_docs_2_CreateHeaderRequestIn",
        "CreateHeaderRequestOut": "_docs_3_CreateHeaderRequestOut",
        "InsertSectionBreakRequestIn": "_docs_4_InsertSectionBreakRequestIn",
        "InsertSectionBreakRequestOut": "_docs_5_InsertSectionBreakRequestOut",
        "ShadingSuggestionStateIn": "_docs_6_ShadingSuggestionStateIn",
        "ShadingSuggestionStateOut": "_docs_7_ShadingSuggestionStateOut",
        "TableCellBorderIn": "_docs_8_TableCellBorderIn",
        "TableCellBorderOut": "_docs_9_TableCellBorderOut",
        "TableRowStyleIn": "_docs_10_TableRowStyleIn",
        "TableRowStyleOut": "_docs_11_TableRowStyleOut",
        "EmbeddedDrawingPropertiesIn": "_docs_12_EmbeddedDrawingPropertiesIn",
        "EmbeddedDrawingPropertiesOut": "_docs_13_EmbeddedDrawingPropertiesOut",
        "SizeSuggestionStateIn": "_docs_14_SizeSuggestionStateIn",
        "SizeSuggestionStateOut": "_docs_15_SizeSuggestionStateOut",
        "FooterIn": "_docs_16_FooterIn",
        "FooterOut": "_docs_17_FooterOut",
        "WriteControlIn": "_docs_18_WriteControlIn",
        "WriteControlOut": "_docs_19_WriteControlOut",
        "CreateParagraphBulletsRequestIn": "_docs_20_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_docs_21_CreateParagraphBulletsRequestOut",
        "SuggestedListPropertiesIn": "_docs_22_SuggestedListPropertiesIn",
        "SuggestedListPropertiesOut": "_docs_23_SuggestedListPropertiesOut",
        "MergeTableCellsRequestIn": "_docs_24_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_docs_25_MergeTableCellsRequestOut",
        "NestingLevelSuggestionStateIn": "_docs_26_NestingLevelSuggestionStateIn",
        "NestingLevelSuggestionStateOut": "_docs_27_NestingLevelSuggestionStateOut",
        "DocumentStyleSuggestionStateIn": "_docs_28_DocumentStyleSuggestionStateIn",
        "DocumentStyleSuggestionStateOut": "_docs_29_DocumentStyleSuggestionStateOut",
        "InsertTableRequestIn": "_docs_30_InsertTableRequestIn",
        "InsertTableRequestOut": "_docs_31_InsertTableRequestOut",
        "UpdateTableColumnPropertiesRequestIn": "_docs_32_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_docs_33_UpdateTableColumnPropertiesRequestOut",
        "OptionalColorIn": "_docs_34_OptionalColorIn",
        "OptionalColorOut": "_docs_35_OptionalColorOut",
        "BatchUpdateDocumentResponseIn": "_docs_36_BatchUpdateDocumentResponseIn",
        "BatchUpdateDocumentResponseOut": "_docs_37_BatchUpdateDocumentResponseOut",
        "TableStyleIn": "_docs_38_TableStyleIn",
        "TableStyleOut": "_docs_39_TableStyleOut",
        "CreateFootnoteResponseIn": "_docs_40_CreateFootnoteResponseIn",
        "CreateFootnoteResponseOut": "_docs_41_CreateFootnoteResponseOut",
        "TextRunIn": "_docs_42_TextRunIn",
        "TextRunOut": "_docs_43_TextRunOut",
        "TableColumnPropertiesIn": "_docs_44_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_docs_45_TableColumnPropertiesOut",
        "PersonPropertiesIn": "_docs_46_PersonPropertiesIn",
        "PersonPropertiesOut": "_docs_47_PersonPropertiesOut",
        "DocumentStyleIn": "_docs_48_DocumentStyleIn",
        "DocumentStyleOut": "_docs_49_DocumentStyleOut",
        "CreateNamedRangeResponseIn": "_docs_50_CreateNamedRangeResponseIn",
        "CreateNamedRangeResponseOut": "_docs_51_CreateNamedRangeResponseOut",
        "PageBreakIn": "_docs_52_PageBreakIn",
        "PageBreakOut": "_docs_53_PageBreakOut",
        "UpdateSectionStyleRequestIn": "_docs_54_UpdateSectionStyleRequestIn",
        "UpdateSectionStyleRequestOut": "_docs_55_UpdateSectionStyleRequestOut",
        "AutoTextIn": "_docs_56_AutoTextIn",
        "AutoTextOut": "_docs_57_AutoTextOut",
        "NamedRangesIn": "_docs_58_NamedRangesIn",
        "NamedRangesOut": "_docs_59_NamedRangesOut",
        "NamedStylesIn": "_docs_60_NamedStylesIn",
        "NamedStylesOut": "_docs_61_NamedStylesOut",
        "SectionColumnPropertiesIn": "_docs_62_SectionColumnPropertiesIn",
        "SectionColumnPropertiesOut": "_docs_63_SectionColumnPropertiesOut",
        "PositionedObjectIn": "_docs_64_PositionedObjectIn",
        "PositionedObjectOut": "_docs_65_PositionedObjectOut",
        "TextStyleIn": "_docs_66_TextStyleIn",
        "TextStyleOut": "_docs_67_TextStyleOut",
        "ParagraphElementIn": "_docs_68_ParagraphElementIn",
        "ParagraphElementOut": "_docs_69_ParagraphElementOut",
        "HeaderIn": "_docs_70_HeaderIn",
        "HeaderOut": "_docs_71_HeaderOut",
        "EmbeddedObjectSuggestionStateIn": "_docs_72_EmbeddedObjectSuggestionStateIn",
        "EmbeddedObjectSuggestionStateOut": "_docs_73_EmbeddedObjectSuggestionStateOut",
        "SheetsChartReferenceSuggestionStateIn": "_docs_74_SheetsChartReferenceSuggestionStateIn",
        "SheetsChartReferenceSuggestionStateOut": "_docs_75_SheetsChartReferenceSuggestionStateOut",
        "EndOfSegmentLocationIn": "_docs_76_EndOfSegmentLocationIn",
        "EndOfSegmentLocationOut": "_docs_77_EndOfSegmentLocationOut",
        "PinTableHeaderRowsRequestIn": "_docs_78_PinTableHeaderRowsRequestIn",
        "PinTableHeaderRowsRequestOut": "_docs_79_PinTableHeaderRowsRequestOut",
        "DimensionIn": "_docs_80_DimensionIn",
        "DimensionOut": "_docs_81_DimensionOut",
        "TableOfContentsIn": "_docs_82_TableOfContentsIn",
        "TableOfContentsOut": "_docs_83_TableOfContentsOut",
        "SuggestedBulletIn": "_docs_84_SuggestedBulletIn",
        "SuggestedBulletOut": "_docs_85_SuggestedBulletOut",
        "TabStopIn": "_docs_86_TabStopIn",
        "TabStopOut": "_docs_87_TabStopOut",
        "RangeIn": "_docs_88_RangeIn",
        "RangeOut": "_docs_89_RangeOut",
        "SheetsChartReferenceIn": "_docs_90_SheetsChartReferenceIn",
        "SheetsChartReferenceOut": "_docs_91_SheetsChartReferenceOut",
        "DeleteParagraphBulletsRequestIn": "_docs_92_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_docs_93_DeleteParagraphBulletsRequestOut",
        "InsertPageBreakRequestIn": "_docs_94_InsertPageBreakRequestIn",
        "InsertPageBreakRequestOut": "_docs_95_InsertPageBreakRequestOut",
        "PositionedObjectPositioningIn": "_docs_96_PositionedObjectPositioningIn",
        "PositionedObjectPositioningOut": "_docs_97_PositionedObjectPositioningOut",
        "CreateFooterResponseIn": "_docs_98_CreateFooterResponseIn",
        "CreateFooterResponseOut": "_docs_99_CreateFooterResponseOut",
        "ImagePropertiesSuggestionStateIn": "_docs_100_ImagePropertiesSuggestionStateIn",
        "ImagePropertiesSuggestionStateOut": "_docs_101_ImagePropertiesSuggestionStateOut",
        "ParagraphStyleIn": "_docs_102_ParagraphStyleIn",
        "ParagraphStyleOut": "_docs_103_ParagraphStyleOut",
        "DeleteTableRowRequestIn": "_docs_104_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_docs_105_DeleteTableRowRequestOut",
        "InlineObjectIn": "_docs_106_InlineObjectIn",
        "InlineObjectOut": "_docs_107_InlineObjectOut",
        "CropPropertiesIn": "_docs_108_CropPropertiesIn",
        "CropPropertiesOut": "_docs_109_CropPropertiesOut",
        "SuggestedTableCellStyleIn": "_docs_110_SuggestedTableCellStyleIn",
        "SuggestedTableCellStyleOut": "_docs_111_SuggestedTableCellStyleOut",
        "SuggestedInlineObjectPropertiesIn": "_docs_112_SuggestedInlineObjectPropertiesIn",
        "SuggestedInlineObjectPropertiesOut": "_docs_113_SuggestedInlineObjectPropertiesOut",
        "SuggestedParagraphStyleIn": "_docs_114_SuggestedParagraphStyleIn",
        "SuggestedParagraphStyleOut": "_docs_115_SuggestedParagraphStyleOut",
        "NestingLevelIn": "_docs_116_NestingLevelIn",
        "NestingLevelOut": "_docs_117_NestingLevelOut",
        "SizeIn": "_docs_118_SizeIn",
        "SizeOut": "_docs_119_SizeOut",
        "BulletSuggestionStateIn": "_docs_120_BulletSuggestionStateIn",
        "BulletSuggestionStateOut": "_docs_121_BulletSuggestionStateOut",
        "SectionStyleIn": "_docs_122_SectionStyleIn",
        "SectionStyleOut": "_docs_123_SectionStyleOut",
        "InsertTextRequestIn": "_docs_124_InsertTextRequestIn",
        "InsertTextRequestOut": "_docs_125_InsertTextRequestOut",
        "EmbeddedObjectIn": "_docs_126_EmbeddedObjectIn",
        "EmbeddedObjectOut": "_docs_127_EmbeddedObjectOut",
        "BodyIn": "_docs_128_BodyIn",
        "BodyOut": "_docs_129_BodyOut",
        "EmbeddedObjectBorderIn": "_docs_130_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_docs_131_EmbeddedObjectBorderOut",
        "ImagePropertiesIn": "_docs_132_ImagePropertiesIn",
        "ImagePropertiesOut": "_docs_133_ImagePropertiesOut",
        "ResponseIn": "_docs_134_ResponseIn",
        "ResponseOut": "_docs_135_ResponseOut",
        "NamedStylesSuggestionStateIn": "_docs_136_NamedStylesSuggestionStateIn",
        "NamedStylesSuggestionStateOut": "_docs_137_NamedStylesSuggestionStateOut",
        "TableCellStyleSuggestionStateIn": "_docs_138_TableCellStyleSuggestionStateIn",
        "TableCellStyleSuggestionStateOut": "_docs_139_TableCellStyleSuggestionStateOut",
        "PositionedObjectPropertiesIn": "_docs_140_PositionedObjectPropertiesIn",
        "PositionedObjectPropertiesOut": "_docs_141_PositionedObjectPropertiesOut",
        "ReplaceImageRequestIn": "_docs_142_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_docs_143_ReplaceImageRequestOut",
        "ShadingIn": "_docs_144_ShadingIn",
        "ShadingOut": "_docs_145_ShadingOut",
        "CreateNamedRangeRequestIn": "_docs_146_CreateNamedRangeRequestIn",
        "CreateNamedRangeRequestOut": "_docs_147_CreateNamedRangeRequestOut",
        "ReplaceAllTextRequestIn": "_docs_148_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_docs_149_ReplaceAllTextRequestOut",
        "BackgroundIn": "_docs_150_BackgroundIn",
        "BackgroundOut": "_docs_151_BackgroundOut",
        "ParagraphIn": "_docs_152_ParagraphIn",
        "ParagraphOut": "_docs_153_ParagraphOut",
        "RgbColorIn": "_docs_154_RgbColorIn",
        "RgbColorOut": "_docs_155_RgbColorOut",
        "SubstringMatchCriteriaIn": "_docs_156_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_docs_157_SubstringMatchCriteriaOut",
        "DocumentIn": "_docs_158_DocumentIn",
        "DocumentOut": "_docs_159_DocumentOut",
        "CreateFooterRequestIn": "_docs_160_CreateFooterRequestIn",
        "CreateFooterRequestOut": "_docs_161_CreateFooterRequestOut",
        "LinkedContentReferenceSuggestionStateIn": "_docs_162_LinkedContentReferenceSuggestionStateIn",
        "LinkedContentReferenceSuggestionStateOut": "_docs_163_LinkedContentReferenceSuggestionStateOut",
        "CropPropertiesSuggestionStateIn": "_docs_164_CropPropertiesSuggestionStateIn",
        "CropPropertiesSuggestionStateOut": "_docs_165_CropPropertiesSuggestionStateOut",
        "InlineObjectElementIn": "_docs_166_InlineObjectElementIn",
        "InlineObjectElementOut": "_docs_167_InlineObjectElementOut",
        "CreateHeaderResponseIn": "_docs_168_CreateHeaderResponseIn",
        "CreateHeaderResponseOut": "_docs_169_CreateHeaderResponseOut",
        "ObjectReferencesIn": "_docs_170_ObjectReferencesIn",
        "ObjectReferencesOut": "_docs_171_ObjectReferencesOut",
        "InsertInlineImageResponseIn": "_docs_172_InsertInlineImageResponseIn",
        "InsertInlineImageResponseOut": "_docs_173_InsertInlineImageResponseOut",
        "TableRangeIn": "_docs_174_TableRangeIn",
        "TableRangeOut": "_docs_175_TableRangeOut",
        "LocationIn": "_docs_176_LocationIn",
        "LocationOut": "_docs_177_LocationOut",
        "UpdateTableCellStyleRequestIn": "_docs_178_UpdateTableCellStyleRequestIn",
        "UpdateTableCellStyleRequestOut": "_docs_179_UpdateTableCellStyleRequestOut",
        "UpdateTableRowStyleRequestIn": "_docs_180_UpdateTableRowStyleRequestIn",
        "UpdateTableRowStyleRequestOut": "_docs_181_UpdateTableRowStyleRequestOut",
        "ListPropertiesSuggestionStateIn": "_docs_182_ListPropertiesSuggestionStateIn",
        "ListPropertiesSuggestionStateOut": "_docs_183_ListPropertiesSuggestionStateOut",
        "BackgroundSuggestionStateIn": "_docs_184_BackgroundSuggestionStateIn",
        "BackgroundSuggestionStateOut": "_docs_185_BackgroundSuggestionStateOut",
        "TableIn": "_docs_186_TableIn",
        "TableOut": "_docs_187_TableOut",
        "DeleteNamedRangeRequestIn": "_docs_188_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_docs_189_DeleteNamedRangeRequestOut",
        "LinkedContentReferenceIn": "_docs_190_LinkedContentReferenceIn",
        "LinkedContentReferenceOut": "_docs_191_LinkedContentReferenceOut",
        "UpdateDocumentStyleRequestIn": "_docs_192_UpdateDocumentStyleRequestIn",
        "UpdateDocumentStyleRequestOut": "_docs_193_UpdateDocumentStyleRequestOut",
        "StructuralElementIn": "_docs_194_StructuralElementIn",
        "StructuralElementOut": "_docs_195_StructuralElementOut",
        "ListIn": "_docs_196_ListIn",
        "ListOut": "_docs_197_ListOut",
        "FootnoteReferenceIn": "_docs_198_FootnoteReferenceIn",
        "FootnoteReferenceOut": "_docs_199_FootnoteReferenceOut",
        "InlineObjectPropertiesSuggestionStateIn": "_docs_200_InlineObjectPropertiesSuggestionStateIn",
        "InlineObjectPropertiesSuggestionStateOut": "_docs_201_InlineObjectPropertiesSuggestionStateOut",
        "ColorIn": "_docs_202_ColorIn",
        "ColorOut": "_docs_203_ColorOut",
        "UpdateTextStyleRequestIn": "_docs_204_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_docs_205_UpdateTextStyleRequestOut",
        "HorizontalRuleIn": "_docs_206_HorizontalRuleIn",
        "HorizontalRuleOut": "_docs_207_HorizontalRuleOut",
        "RequestIn": "_docs_208_RequestIn",
        "RequestOut": "_docs_209_RequestOut",
        "SuggestedTableRowStyleIn": "_docs_210_SuggestedTableRowStyleIn",
        "SuggestedTableRowStyleOut": "_docs_211_SuggestedTableRowStyleOut",
        "RichLinkIn": "_docs_212_RichLinkIn",
        "RichLinkOut": "_docs_213_RichLinkOut",
        "EmbeddedDrawingPropertiesSuggestionStateIn": "_docs_214_EmbeddedDrawingPropertiesSuggestionStateIn",
        "EmbeddedDrawingPropertiesSuggestionStateOut": "_docs_215_EmbeddedDrawingPropertiesSuggestionStateOut",
        "ParagraphStyleSuggestionStateIn": "_docs_216_ParagraphStyleSuggestionStateIn",
        "ParagraphStyleSuggestionStateOut": "_docs_217_ParagraphStyleSuggestionStateOut",
        "DeleteContentRangeRequestIn": "_docs_218_DeleteContentRangeRequestIn",
        "DeleteContentRangeRequestOut": "_docs_219_DeleteContentRangeRequestOut",
        "SuggestedPositionedObjectPropertiesIn": "_docs_220_SuggestedPositionedObjectPropertiesIn",
        "SuggestedPositionedObjectPropertiesOut": "_docs_221_SuggestedPositionedObjectPropertiesOut",
        "DeleteTableColumnRequestIn": "_docs_222_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_docs_223_DeleteTableColumnRequestOut",
        "UpdateParagraphStyleRequestIn": "_docs_224_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_docs_225_UpdateParagraphStyleRequestOut",
        "WeightedFontFamilyIn": "_docs_226_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_docs_227_WeightedFontFamilyOut",
        "InlineObjectPropertiesIn": "_docs_228_InlineObjectPropertiesIn",
        "InlineObjectPropertiesOut": "_docs_229_InlineObjectPropertiesOut",
        "InsertTableRowRequestIn": "_docs_230_InsertTableRowRequestIn",
        "InsertTableRowRequestOut": "_docs_231_InsertTableRowRequestOut",
        "InsertTableColumnRequestIn": "_docs_232_InsertTableColumnRequestIn",
        "InsertTableColumnRequestOut": "_docs_233_InsertTableColumnRequestOut",
        "LinkIn": "_docs_234_LinkIn",
        "LinkOut": "_docs_235_LinkOut",
        "PositionedObjectPropertiesSuggestionStateIn": "_docs_236_PositionedObjectPropertiesSuggestionStateIn",
        "PositionedObjectPropertiesSuggestionStateOut": "_docs_237_PositionedObjectPropertiesSuggestionStateOut",
        "InsertInlineImageRequestIn": "_docs_238_InsertInlineImageRequestIn",
        "InsertInlineImageRequestOut": "_docs_239_InsertInlineImageRequestOut",
        "NamedStyleSuggestionStateIn": "_docs_240_NamedStyleSuggestionStateIn",
        "NamedStyleSuggestionStateOut": "_docs_241_NamedStyleSuggestionStateOut",
        "UnmergeTableCellsRequestIn": "_docs_242_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_docs_243_UnmergeTableCellsRequestOut",
        "CreateFootnoteRequestIn": "_docs_244_CreateFootnoteRequestIn",
        "CreateFootnoteRequestOut": "_docs_245_CreateFootnoteRequestOut",
        "DeleteHeaderRequestIn": "_docs_246_DeleteHeaderRequestIn",
        "DeleteHeaderRequestOut": "_docs_247_DeleteHeaderRequestOut",
        "RichLinkPropertiesIn": "_docs_248_RichLinkPropertiesIn",
        "RichLinkPropertiesOut": "_docs_249_RichLinkPropertiesOut",
        "TableCellLocationIn": "_docs_250_TableCellLocationIn",
        "TableCellLocationOut": "_docs_251_TableCellLocationOut",
        "ColumnBreakIn": "_docs_252_ColumnBreakIn",
        "ColumnBreakOut": "_docs_253_ColumnBreakOut",
        "PersonIn": "_docs_254_PersonIn",
        "PersonOut": "_docs_255_PersonOut",
        "TableRowIn": "_docs_256_TableRowIn",
        "TableRowOut": "_docs_257_TableRowOut",
        "BulletIn": "_docs_258_BulletIn",
        "BulletOut": "_docs_259_BulletOut",
        "PositionedObjectPositioningSuggestionStateIn": "_docs_260_PositionedObjectPositioningSuggestionStateIn",
        "PositionedObjectPositioningSuggestionStateOut": "_docs_261_PositionedObjectPositioningSuggestionStateOut",
        "TableCellIn": "_docs_262_TableCellIn",
        "TableCellOut": "_docs_263_TableCellOut",
        "SectionBreakIn": "_docs_264_SectionBreakIn",
        "SectionBreakOut": "_docs_265_SectionBreakOut",
        "InsertInlineSheetsChartResponseIn": "_docs_266_InsertInlineSheetsChartResponseIn",
        "InsertInlineSheetsChartResponseOut": "_docs_267_InsertInlineSheetsChartResponseOut",
        "NamedRangeIn": "_docs_268_NamedRangeIn",
        "NamedRangeOut": "_docs_269_NamedRangeOut",
        "NamedStyleIn": "_docs_270_NamedStyleIn",
        "NamedStyleOut": "_docs_271_NamedStyleOut",
        "TableCellStyleIn": "_docs_272_TableCellStyleIn",
        "TableCellStyleOut": "_docs_273_TableCellStyleOut",
        "SuggestedTextStyleIn": "_docs_274_SuggestedTextStyleIn",
        "SuggestedTextStyleOut": "_docs_275_SuggestedTextStyleOut",
        "ParagraphBorderIn": "_docs_276_ParagraphBorderIn",
        "ParagraphBorderOut": "_docs_277_ParagraphBorderOut",
        "EmbeddedObjectBorderSuggestionStateIn": "_docs_278_EmbeddedObjectBorderSuggestionStateIn",
        "EmbeddedObjectBorderSuggestionStateOut": "_docs_279_EmbeddedObjectBorderSuggestionStateOut",
        "ListPropertiesIn": "_docs_280_ListPropertiesIn",
        "ListPropertiesOut": "_docs_281_ListPropertiesOut",
        "FootnoteIn": "_docs_282_FootnoteIn",
        "FootnoteOut": "_docs_283_FootnoteOut",
        "ReplaceNamedRangeContentRequestIn": "_docs_284_ReplaceNamedRangeContentRequestIn",
        "ReplaceNamedRangeContentRequestOut": "_docs_285_ReplaceNamedRangeContentRequestOut",
        "DeletePositionedObjectRequestIn": "_docs_286_DeletePositionedObjectRequestIn",
        "DeletePositionedObjectRequestOut": "_docs_287_DeletePositionedObjectRequestOut",
        "TableRowStyleSuggestionStateIn": "_docs_288_TableRowStyleSuggestionStateIn",
        "TableRowStyleSuggestionStateOut": "_docs_289_TableRowStyleSuggestionStateOut",
        "ReplaceAllTextResponseIn": "_docs_290_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_docs_291_ReplaceAllTextResponseOut",
        "EquationIn": "_docs_292_EquationIn",
        "EquationOut": "_docs_293_EquationOut",
        "TextStyleSuggestionStateIn": "_docs_294_TextStyleSuggestionStateIn",
        "TextStyleSuggestionStateOut": "_docs_295_TextStyleSuggestionStateOut",
        "DeleteFooterRequestIn": "_docs_296_DeleteFooterRequestIn",
        "DeleteFooterRequestOut": "_docs_297_DeleteFooterRequestOut",
        "SuggestedDocumentStyleIn": "_docs_298_SuggestedDocumentStyleIn",
        "SuggestedDocumentStyleOut": "_docs_299_SuggestedDocumentStyleOut",
        "BatchUpdateDocumentRequestIn": "_docs_300_BatchUpdateDocumentRequestIn",
        "BatchUpdateDocumentRequestOut": "_docs_301_BatchUpdateDocumentRequestOut",
        "SuggestedNamedStylesIn": "_docs_302_SuggestedNamedStylesIn",
        "SuggestedNamedStylesOut": "_docs_303_SuggestedNamedStylesOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CreateHeaderRequestIn"] = t.struct(
        {
            "type": t.string().optional(),
            "sectionBreakLocation": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["CreateHeaderRequestIn"])
    types["CreateHeaderRequestOut"] = t.struct(
        {
            "type": t.string().optional(),
            "sectionBreakLocation": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateHeaderRequestOut"])
    types["InsertSectionBreakRequestIn"] = t.struct(
        {
            "sectionType": t.string().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["InsertSectionBreakRequestIn"])
    types["InsertSectionBreakRequestOut"] = t.struct(
        {
            "sectionType": t.string().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertSectionBreakRequestOut"])
    types["ShadingSuggestionStateIn"] = t.struct(
        {"backgroundColorSuggested": t.boolean().optional()}
    ).named(renames["ShadingSuggestionStateIn"])
    types["ShadingSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadingSuggestionStateOut"])
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
    types["TableRowStyleIn"] = t.struct(
        {
            "preventOverflow": t.boolean().optional(),
            "minRowHeight": t.proxy(renames["DimensionIn"]).optional(),
            "tableHeader": t.boolean().optional(),
        }
    ).named(renames["TableRowStyleIn"])
    types["TableRowStyleOut"] = t.struct(
        {
            "preventOverflow": t.boolean().optional(),
            "minRowHeight": t.proxy(renames["DimensionOut"]).optional(),
            "tableHeader": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowStyleOut"])
    types["EmbeddedDrawingPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EmbeddedDrawingPropertiesIn"]
    )
    types["EmbeddedDrawingPropertiesOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmbeddedDrawingPropertiesOut"])
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
    types["MergeTableCellsRequestIn"] = t.struct(
        {"tableRange": t.proxy(renames["TableRangeIn"]).optional()}
    ).named(renames["MergeTableCellsRequestIn"])
    types["MergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeTableCellsRequestOut"])
    types["NestingLevelSuggestionStateIn"] = t.struct(
        {
            "startNumberSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
            "indentStartSuggested": t.boolean().optional(),
            "bulletAlignmentSuggested": t.boolean().optional(),
            "glyphFormatSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "glyphSymbolSuggested": t.boolean().optional(),
            "glyphTypeSuggested": t.boolean().optional(),
        }
    ).named(renames["NestingLevelSuggestionStateIn"])
    types["NestingLevelSuggestionStateOut"] = t.struct(
        {
            "startNumberSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "indentStartSuggested": t.boolean().optional(),
            "bulletAlignmentSuggested": t.boolean().optional(),
            "glyphFormatSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "glyphSymbolSuggested": t.boolean().optional(),
            "glyphTypeSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelSuggestionStateOut"])
    types["DocumentStyleSuggestionStateIn"] = t.struct(
        {
            "firstPageFooterIdSuggested": t.boolean().optional(),
            "pageNumberStartSuggested": t.boolean().optional(),
            "firstPageHeaderIdSuggested": t.boolean().optional(),
            "marginFooterSuggested": t.boolean().optional(),
            "useFirstPageHeaderFooterSuggested": t.boolean().optional(),
            "useEvenPageHeaderFooterSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "backgroundSuggestionState": t.proxy(
                renames["BackgroundSuggestionStateIn"]
            ).optional(),
            "marginHeaderSuggested": t.boolean().optional(),
            "defaultFooterIdSuggested": t.boolean().optional(),
            "evenPageHeaderIdSuggested": t.boolean().optional(),
            "evenPageFooterIdSuggested": t.boolean().optional(),
            "pageSizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateIn"]
            ).optional(),
            "marginRightSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "marginTopSuggested": t.boolean().optional(),
            "defaultHeaderIdSuggested": t.boolean().optional(),
            "useCustomHeaderFooterMarginsSuggested": t.boolean().optional(),
        }
    ).named(renames["DocumentStyleSuggestionStateIn"])
    types["DocumentStyleSuggestionStateOut"] = t.struct(
        {
            "firstPageFooterIdSuggested": t.boolean().optional(),
            "pageNumberStartSuggested": t.boolean().optional(),
            "firstPageHeaderIdSuggested": t.boolean().optional(),
            "marginFooterSuggested": t.boolean().optional(),
            "useFirstPageHeaderFooterSuggested": t.boolean().optional(),
            "useEvenPageHeaderFooterSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "backgroundSuggestionState": t.proxy(
                renames["BackgroundSuggestionStateOut"]
            ).optional(),
            "marginHeaderSuggested": t.boolean().optional(),
            "defaultFooterIdSuggested": t.boolean().optional(),
            "evenPageHeaderIdSuggested": t.boolean().optional(),
            "evenPageFooterIdSuggested": t.boolean().optional(),
            "pageSizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateOut"]
            ).optional(),
            "marginRightSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "marginTopSuggested": t.boolean().optional(),
            "defaultHeaderIdSuggested": t.boolean().optional(),
            "useCustomHeaderFooterMarginsSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentStyleSuggestionStateOut"])
    types["InsertTableRequestIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]).optional(),
            "columns": t.integer().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "rows": t.integer().optional(),
        }
    ).named(renames["InsertTableRequestIn"])
    types["InsertTableRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]).optional(),
            "columns": t.integer().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "rows": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRequestOut"])
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "columnIndices": t.array(t.integer()).optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["OptionalColorIn"] = t.struct(
        {"color": t.proxy(renames["ColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
    types["BatchUpdateDocumentResponseIn"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
            "documentId": t.string().optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
        }
    ).named(renames["BatchUpdateDocumentResponseIn"])
    types["BatchUpdateDocumentResponseOut"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "documentId": t.string().optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDocumentResponseOut"])
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
    types["CreateFootnoteResponseIn"] = t.struct(
        {"footnoteId": t.string().optional()}
    ).named(renames["CreateFootnoteResponseIn"])
    types["CreateFootnoteResponseOut"] = t.struct(
        {
            "footnoteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFootnoteResponseOut"])
    types["TextRunIn"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["TextRunIn"])
    types["TextRunOut"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextRunOut"])
    types["TableColumnPropertiesIn"] = t.struct(
        {
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "widthType": t.string().optional(),
        }
    ).named(renames["TableColumnPropertiesIn"])
    types["TableColumnPropertiesOut"] = t.struct(
        {
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "widthType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableColumnPropertiesOut"])
    types["PersonPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PersonPropertiesIn"]
    )
    types["PersonPropertiesOut"] = t.struct(
        {
            "email": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonPropertiesOut"])
    types["DocumentStyleIn"] = t.struct(
        {
            "evenPageHeaderId": t.string().optional(),
            "useCustomHeaderFooterMargins": t.boolean().optional(),
            "firstPageFooterId": t.string().optional(),
            "marginFooter": t.proxy(renames["DimensionIn"]).optional(),
            "useEvenPageHeaderFooter": t.boolean().optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "background": t.proxy(renames["BackgroundIn"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "defaultHeaderId": t.string().optional(),
            "defaultFooterId": t.string().optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "marginHeader": t.proxy(renames["DimensionIn"]).optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "evenPageFooterId": t.string().optional(),
        }
    ).named(renames["DocumentStyleIn"])
    types["DocumentStyleOut"] = t.struct(
        {
            "evenPageHeaderId": t.string().optional(),
            "useCustomHeaderFooterMargins": t.boolean().optional(),
            "firstPageFooterId": t.string().optional(),
            "marginFooter": t.proxy(renames["DimensionOut"]).optional(),
            "useEvenPageHeaderFooter": t.boolean().optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "background": t.proxy(renames["BackgroundOut"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "defaultHeaderId": t.string().optional(),
            "defaultFooterId": t.string().optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "marginHeader": t.proxy(renames["DimensionOut"]).optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentStyleOut"])
    types["CreateNamedRangeResponseIn"] = t.struct(
        {"namedRangeId": t.string().optional()}
    ).named(renames["CreateNamedRangeResponseIn"])
    types["CreateNamedRangeResponseOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNamedRangeResponseOut"])
    types["PageBreakIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["PageBreakIn"])
    types["PageBreakOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBreakOut"])
    types["UpdateSectionStyleRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "sectionStyle": t.proxy(renames["SectionStyleIn"]).optional(),
            "range": t.proxy(renames["RangeIn"]).optional(),
        }
    ).named(renames["UpdateSectionStyleRequestIn"])
    types["UpdateSectionStyleRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "sectionStyle": t.proxy(renames["SectionStyleOut"]).optional(),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSectionStyleRequestOut"])
    types["AutoTextIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
    types["NamedRangesIn"] = t.struct(
        {
            "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["NamedRangesIn"])
    types["NamedRangesOut"] = t.struct(
        {
            "namedRanges": t.array(t.proxy(renames["NamedRangeOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedRangesOut"])
    types["NamedStylesIn"] = t.struct(
        {"styles": t.array(t.proxy(renames["NamedStyleIn"])).optional()}
    ).named(renames["NamedStylesIn"])
    types["NamedStylesOut"] = t.struct(
        {
            "styles": t.array(t.proxy(renames["NamedStyleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStylesOut"])
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
    types["PositionedObjectIn"] = t.struct(
        {
            "suggestedInsertionId": t.string().optional(),
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesIn"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "objectId": t.string().optional(),
            "suggestedPositionedObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["PositionedObjectIn"])
    types["PositionedObjectOut"] = t.struct(
        {
            "suggestedInsertionId": t.string().optional(),
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesOut"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "objectId": t.string().optional(),
            "suggestedPositionedObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectOut"])
    types["TextStyleIn"] = t.struct(
        {
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "smallCaps": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "underline": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "strikethrough": t.boolean().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "italic": t.boolean().optional(),
            "bold": t.boolean().optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "smallCaps": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "underline": t.boolean().optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "strikethrough": t.boolean().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "italic": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
    types["ParagraphElementIn"] = t.struct(
        {
            "equation": t.proxy(renames["EquationIn"]).optional(),
            "inlineObjectElement": t.proxy(renames["InlineObjectElementIn"]).optional(),
            "footnoteReference": t.proxy(renames["FootnoteReferenceIn"]).optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "horizontalRule": t.proxy(renames["HorizontalRuleIn"]).optional(),
            "richLink": t.proxy(renames["RichLinkIn"]).optional(),
            "person": t.proxy(renames["PersonIn"]).optional(),
            "endIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
            "pageBreak": t.proxy(renames["PageBreakIn"]).optional(),
            "startIndex": t.integer().optional(),
            "columnBreak": t.proxy(renames["ColumnBreakIn"]).optional(),
        }
    ).named(renames["ParagraphElementIn"])
    types["ParagraphElementOut"] = t.struct(
        {
            "equation": t.proxy(renames["EquationOut"]).optional(),
            "inlineObjectElement": t.proxy(
                renames["InlineObjectElementOut"]
            ).optional(),
            "footnoteReference": t.proxy(renames["FootnoteReferenceOut"]).optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "horizontalRule": t.proxy(renames["HorizontalRuleOut"]).optional(),
            "richLink": t.proxy(renames["RichLinkOut"]).optional(),
            "person": t.proxy(renames["PersonOut"]).optional(),
            "endIndex": t.integer().optional(),
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "pageBreak": t.proxy(renames["PageBreakOut"]).optional(),
            "startIndex": t.integer().optional(),
            "columnBreak": t.proxy(renames["ColumnBreakOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphElementOut"])
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
    types["EmbeddedObjectSuggestionStateIn"] = t.struct(
        {
            "embeddedObjectBorderSuggestionState": t.proxy(
                renames["EmbeddedObjectBorderSuggestionStateIn"]
            ).optional(),
            "sizeSuggestionState": t.proxy(renames["SizeSuggestionStateIn"]).optional(),
            "titleSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "descriptionSuggested": t.boolean().optional(),
            "linkedContentReferenceSuggestionState": t.proxy(
                renames["LinkedContentReferenceSuggestionStateIn"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "embeddedDrawingPropertiesSuggestionState": t.proxy(
                renames["EmbeddedDrawingPropertiesSuggestionStateIn"]
            ).optional(),
            "imagePropertiesSuggestionState": t.proxy(
                renames["ImagePropertiesSuggestionStateIn"]
            ).optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
        }
    ).named(renames["EmbeddedObjectSuggestionStateIn"])
    types["EmbeddedObjectSuggestionStateOut"] = t.struct(
        {
            "embeddedObjectBorderSuggestionState": t.proxy(
                renames["EmbeddedObjectBorderSuggestionStateOut"]
            ).optional(),
            "sizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateOut"]
            ).optional(),
            "titleSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "descriptionSuggested": t.boolean().optional(),
            "linkedContentReferenceSuggestionState": t.proxy(
                renames["LinkedContentReferenceSuggestionStateOut"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "embeddedDrawingPropertiesSuggestionState": t.proxy(
                renames["EmbeddedDrawingPropertiesSuggestionStateOut"]
            ).optional(),
            "imagePropertiesSuggestionState": t.proxy(
                renames["ImagePropertiesSuggestionStateOut"]
            ).optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectSuggestionStateOut"])
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
    types["EndOfSegmentLocationIn"] = t.struct(
        {"segmentId": t.string().optional()}
    ).named(renames["EndOfSegmentLocationIn"])
    types["EndOfSegmentLocationOut"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndOfSegmentLocationOut"])
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
    types["TableOfContentsIn"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["TableOfContentsIn"])
    types["TableOfContentsOut"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOfContentsOut"])
    types["SuggestedBulletIn"] = t.struct(
        {
            "bullet": t.proxy(renames["BulletIn"]).optional(),
            "bulletSuggestionState": t.proxy(
                renames["BulletSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedBulletIn"])
    types["SuggestedBulletOut"] = t.struct(
        {
            "bullet": t.proxy(renames["BulletOut"]).optional(),
            "bulletSuggestionState": t.proxy(
                renames["BulletSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedBulletOut"])
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
    types["RangeIn"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
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
    types["DeleteParagraphBulletsRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["DeleteParagraphBulletsRequestIn"])
    types["DeleteParagraphBulletsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestOut"])
    types["InsertPageBreakRequestIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
        }
    ).named(renames["InsertPageBreakRequestIn"])
    types["InsertPageBreakRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertPageBreakRequestOut"])
    types["PositionedObjectPositioningIn"] = t.struct(
        {
            "topOffset": t.proxy(renames["DimensionIn"]).optional(),
            "leftOffset": t.proxy(renames["DimensionIn"]).optional(),
            "layout": t.string().optional(),
        }
    ).named(renames["PositionedObjectPositioningIn"])
    types["PositionedObjectPositioningOut"] = t.struct(
        {
            "topOffset": t.proxy(renames["DimensionOut"]).optional(),
            "leftOffset": t.proxy(renames["DimensionOut"]).optional(),
            "layout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningOut"])
    types["CreateFooterResponseIn"] = t.struct(
        {"footerId": t.string().optional()}
    ).named(renames["CreateFooterResponseIn"])
    types["CreateFooterResponseOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFooterResponseOut"])
    types["ImagePropertiesSuggestionStateIn"] = t.struct(
        {
            "cropPropertiesSuggestionState": t.proxy(
                renames["CropPropertiesSuggestionStateIn"]
            ).optional(),
            "contentUriSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "brightnessSuggested": t.boolean().optional(),
            "transparencySuggested": t.boolean().optional(),
            "sourceUriSuggested": t.boolean().optional(),
            "contrastSuggested": t.boolean().optional(),
        }
    ).named(renames["ImagePropertiesSuggestionStateIn"])
    types["ImagePropertiesSuggestionStateOut"] = t.struct(
        {
            "cropPropertiesSuggestionState": t.proxy(
                renames["CropPropertiesSuggestionStateOut"]
            ).optional(),
            "contentUriSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "brightnessSuggested": t.boolean().optional(),
            "transparencySuggested": t.boolean().optional(),
            "sourceUriSuggested": t.boolean().optional(),
            "contrastSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesSuggestionStateOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "borderRight": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "tabStops": t.array(t.proxy(renames["TabStopIn"])).optional(),
            "headingId": t.string().optional(),
            "alignment": t.string().optional(),
            "namedStyleType": t.string().optional(),
            "avoidWidowAndOrphan": t.boolean().optional(),
            "direction": t.string().optional(),
            "borderBottom": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "pageBreakBefore": t.boolean().optional(),
            "lineSpacing": t.number().optional(),
            "borderLeft": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "borderTop": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "borderBetween": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "keepLinesTogether": t.boolean().optional(),
            "shading": t.proxy(renames["ShadingIn"]).optional(),
            "spacingMode": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "keepWithNext": t.boolean().optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "borderRight": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "tabStops": t.array(t.proxy(renames["TabStopOut"])).optional(),
            "headingId": t.string().optional(),
            "alignment": t.string().optional(),
            "namedStyleType": t.string().optional(),
            "avoidWidowAndOrphan": t.boolean().optional(),
            "direction": t.string().optional(),
            "borderBottom": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "pageBreakBefore": t.boolean().optional(),
            "lineSpacing": t.number().optional(),
            "borderLeft": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "borderTop": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "borderBetween": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "keepLinesTogether": t.boolean().optional(),
            "shading": t.proxy(renames["ShadingOut"]).optional(),
            "spacingMode": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "keepWithNext": t.boolean().optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
    types["DeleteTableRowRequestIn"] = t.struct(
        {"tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional()}
    ).named(renames["DeleteTableRowRequestIn"])
    types["DeleteTableRowRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableRowRequestOut"])
    types["InlineObjectIn"] = t.struct(
        {
            "suggestedInlineObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "objectId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionId": t.string().optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesIn"]
            ).optional(),
        }
    ).named(renames["InlineObjectIn"])
    types["InlineObjectOut"] = t.struct(
        {
            "suggestedInlineObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "objectId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionId": t.string().optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectOut"])
    types["CropPropertiesIn"] = t.struct(
        {
            "angle": t.number().optional(),
            "offsetLeft": t.number().optional(),
            "offsetTop": t.number().optional(),
            "offsetRight": t.number().optional(),
            "offsetBottom": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "angle": t.number().optional(),
            "offsetLeft": t.number().optional(),
            "offsetTop": t.number().optional(),
            "offsetRight": t.number().optional(),
            "offsetBottom": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
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
    types["NestingLevelIn"] = t.struct(
        {
            "bulletAlignment": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "glyphSymbol": t.string().optional(),
            "startNumber": t.integer().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "glyphType": t.string().optional(),
            "glyphFormat": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "bulletAlignment": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "glyphSymbol": t.string().optional(),
            "startNumber": t.integer().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "glyphType": t.string().optional(),
            "glyphFormat": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
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
    types["BulletSuggestionStateIn"] = t.struct(
        {
            "nestingLevelSuggested": t.boolean().optional(),
            "listIdSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["BulletSuggestionStateIn"])
    types["BulletSuggestionStateOut"] = t.struct(
        {
            "nestingLevelSuggested": t.boolean().optional(),
            "listIdSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletSuggestionStateOut"])
    types["SectionStyleIn"] = t.struct(
        {
            "columnSeparatorStyle": t.string().optional(),
            "firstPageFooterId": t.string().optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "marginFooter": t.proxy(renames["DimensionIn"]).optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "defaultFooterId": t.string().optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "defaultHeaderId": t.string().optional(),
            "marginHeader": t.proxy(renames["DimensionIn"]).optional(),
            "evenPageHeaderId": t.string().optional(),
            "contentDirection": t.string().optional(),
            "sectionType": t.string().optional(),
            "columnProperties": t.array(
                t.proxy(renames["SectionColumnPropertiesIn"])
            ).optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
        }
    ).named(renames["SectionStyleIn"])
    types["SectionStyleOut"] = t.struct(
        {
            "columnSeparatorStyle": t.string().optional(),
            "firstPageFooterId": t.string().optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "marginFooter": t.proxy(renames["DimensionOut"]).optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "defaultFooterId": t.string().optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "firstPageHeaderId": t.string().optional(),
            "defaultHeaderId": t.string().optional(),
            "marginHeader": t.proxy(renames["DimensionOut"]).optional(),
            "evenPageHeaderId": t.string().optional(),
            "contentDirection": t.string().optional(),
            "sectionType": t.string().optional(),
            "columnProperties": t.array(
                t.proxy(renames["SectionColumnPropertiesOut"])
            ).optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "pageNumberStart": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionStyleOut"])
    types["InsertTextRequestIn"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "text": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "text": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
    types["EmbeddedObjectIn"] = t.struct(
        {
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "embeddedDrawingProperties": t.proxy(
                renames["EmbeddedDrawingPropertiesIn"]
            ).optional(),
            "embeddedObjectBorder": t.proxy(
                renames["EmbeddedObjectBorderIn"]
            ).optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "description": t.string().optional(),
            "linkedContentReference": t.proxy(
                renames["LinkedContentReferenceIn"]
            ).optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["EmbeddedObjectIn"])
    types["EmbeddedObjectOut"] = t.struct(
        {
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "embeddedDrawingProperties": t.proxy(
                renames["EmbeddedDrawingPropertiesOut"]
            ).optional(),
            "embeddedObjectBorder": t.proxy(
                renames["EmbeddedObjectBorderOut"]
            ).optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "description": t.string().optional(),
            "linkedContentReference": t.proxy(
                renames["LinkedContentReferenceOut"]
            ).optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectOut"])
    types["BodyIn"] = t.struct(
        {"content": t.array(t.proxy(renames["StructuralElementIn"])).optional()}
    ).named(renames["BodyIn"])
    types["BodyOut"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BodyOut"])
    types["EmbeddedObjectBorderIn"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "propertyState": t.string().optional(),
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderIn"])
    types["EmbeddedObjectBorderOut"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "propertyState": t.string().optional(),
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderOut"])
    types["ImagePropertiesIn"] = t.struct(
        {
            "contentUri": t.string().optional(),
            "brightness": t.number().optional(),
            "transparency": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "angle": t.number().optional(),
            "contrast": t.number().optional(),
            "sourceUri": t.string().optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "contentUri": t.string().optional(),
            "brightness": t.number().optional(),
            "transparency": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "angle": t.number().optional(),
            "contrast": t.number().optional(),
            "sourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
    types["ResponseIn"] = t.struct(
        {
            "insertInlineSheetsChart": t.proxy(
                renames["InsertInlineSheetsChartResponseIn"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterResponseIn"]).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageResponseIn"]
            ).optional(),
            "createHeader": t.proxy(renames["CreateHeaderResponseIn"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteResponseIn"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeResponseIn"]
            ).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "insertInlineSheetsChart": t.proxy(
                renames["InsertInlineSheetsChartResponseOut"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterResponseOut"]).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageResponseOut"]
            ).optional(),
            "createHeader": t.proxy(renames["CreateHeaderResponseOut"]).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteResponseOut"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
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
    types["TableCellStyleSuggestionStateIn"] = t.struct(
        {
            "borderTopSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "columnSpanSuggested": t.boolean().optional(),
            "paddingBottomSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "rowSpanSuggested": t.boolean().optional(),
            "paddingTopSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "paddingRightSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "contentAlignmentSuggested": t.boolean().optional(),
            "paddingLeftSuggested": t.boolean().optional(),
        }
    ).named(renames["TableCellStyleSuggestionStateIn"])
    types["TableCellStyleSuggestionStateOut"] = t.struct(
        {
            "borderTopSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "columnSpanSuggested": t.boolean().optional(),
            "paddingBottomSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "rowSpanSuggested": t.boolean().optional(),
            "paddingTopSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "paddingRightSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "contentAlignmentSuggested": t.boolean().optional(),
            "paddingLeftSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellStyleSuggestionStateOut"])
    types["PositionedObjectPropertiesIn"] = t.struct(
        {
            "positioning": t.proxy(renames["PositionedObjectPositioningIn"]).optional(),
            "embeddedObject": t.proxy(renames["EmbeddedObjectIn"]).optional(),
        }
    ).named(renames["PositionedObjectPropertiesIn"])
    types["PositionedObjectPropertiesOut"] = t.struct(
        {
            "positioning": t.proxy(
                renames["PositionedObjectPositioningOut"]
            ).optional(),
            "embeddedObject": t.proxy(renames["EmbeddedObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPropertiesOut"])
    types["ReplaceImageRequestIn"] = t.struct(
        {
            "imageObjectId": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["ReplaceImageRequestIn"])
    types["ReplaceImageRequestOut"] = t.struct(
        {
            "imageObjectId": t.string().optional(),
            "imageReplaceMethod": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceImageRequestOut"])
    types["ShadingIn"] = t.struct(
        {"backgroundColor": t.proxy(renames["OptionalColorIn"]).optional()}
    ).named(renames["ShadingIn"])
    types["ShadingOut"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadingOut"])
    types["CreateNamedRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional(), "name": t.string().optional()}
    ).named(renames["CreateNamedRangeRequestIn"])
    types["CreateNamedRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNamedRangeRequestOut"])
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
    types["BackgroundIn"] = t.struct(
        {"color": t.proxy(renames["OptionalColorIn"]).optional()}
    ).named(renames["BackgroundIn"])
    types["BackgroundOut"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundOut"])
    types["ParagraphIn"] = t.struct(
        {
            "suggestedPositionedObjectIds": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedParagraphStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "positionedObjectIds": t.array(t.string()).optional(),
            "elements": t.array(t.proxy(renames["ParagraphElementIn"])).optional(),
            "suggestedBulletChanges": t.struct({"_": t.string().optional()}).optional(),
            "bullet": t.proxy(renames["BulletIn"]).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
        }
    ).named(renames["ParagraphIn"])
    types["ParagraphOut"] = t.struct(
        {
            "suggestedPositionedObjectIds": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedParagraphStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "positionedObjectIds": t.array(t.string()).optional(),
            "elements": t.array(t.proxy(renames["ParagraphElementOut"])).optional(),
            "suggestedBulletChanges": t.struct({"_": t.string().optional()}).optional(),
            "bullet": t.proxy(renames["BulletOut"]).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphOut"])
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
    types["DocumentIn"] = t.struct(
        {
            "suggestionsViewMode": t.string().optional(),
            "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
            "title": t.string().optional(),
            "footnotes": t.struct({"_": t.string().optional()}).optional(),
            "revisionId": t.string().optional(),
            "footers": t.struct({"_": t.string().optional()}).optional(),
            "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
            "suggestedNamedStylesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "body": t.proxy(renames["BodyIn"]).optional(),
            "suggestedDocumentStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
            "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
            "namedRanges": t.struct({"_": t.string().optional()}).optional(),
            "documentId": t.string().optional(),
            "lists": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "suggestionsViewMode": t.string().optional(),
            "namedStyles": t.proxy(renames["NamedStylesOut"]).optional(),
            "title": t.string().optional(),
            "footnotes": t.struct({"_": t.string().optional()}).optional(),
            "revisionId": t.string().optional(),
            "footers": t.struct({"_": t.string().optional()}).optional(),
            "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
            "suggestedNamedStylesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "body": t.proxy(renames["BodyOut"]).optional(),
            "suggestedDocumentStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleOut"]).optional(),
            "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
            "namedRanges": t.struct({"_": t.string().optional()}).optional(),
            "documentId": t.string().optional(),
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
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
    types["CropPropertiesSuggestionStateIn"] = t.struct(
        {
            "offsetTopSuggested": t.boolean().optional(),
            "offsetLeftSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "offsetRightSuggested": t.boolean().optional(),
            "offsetBottomSuggested": t.boolean().optional(),
        }
    ).named(renames["CropPropertiesSuggestionStateIn"])
    types["CropPropertiesSuggestionStateOut"] = t.struct(
        {
            "offsetTopSuggested": t.boolean().optional(),
            "offsetLeftSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "offsetRightSuggested": t.boolean().optional(),
            "offsetBottomSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesSuggestionStateOut"])
    types["InlineObjectElementIn"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "inlineObjectId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["InlineObjectElementIn"])
    types["InlineObjectElementOut"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "inlineObjectId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectElementOut"])
    types["CreateHeaderResponseIn"] = t.struct(
        {"headerId": t.string().optional()}
    ).named(renames["CreateHeaderResponseIn"])
    types["CreateHeaderResponseOut"] = t.struct(
        {
            "headerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateHeaderResponseOut"])
    types["ObjectReferencesIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["ObjectReferencesIn"])
    types["ObjectReferencesOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectReferencesOut"])
    types["InsertInlineImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["InsertInlineImageResponseIn"])
    types["InsertInlineImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineImageResponseOut"])
    types["TableRangeIn"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "columnSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
    types["LocationIn"] = t.struct(
        {"index": t.integer().optional(), "segmentId": t.string().optional()}
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["UpdateTableCellStyleRequestIn"] = t.struct(
        {
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
            "fields": t.string().optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
        }
    ).named(renames["UpdateTableCellStyleRequestIn"])
    types["UpdateTableCellStyleRequestOut"] = t.struct(
        {
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "fields": t.string().optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellStyleRequestOut"])
    types["UpdateTableRowStyleRequestIn"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "fields": t.string().optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
        }
    ).named(renames["UpdateTableRowStyleRequestIn"])
    types["UpdateTableRowStyleRequestOut"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "fields": t.string().optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowStyleRequestOut"])
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
    types["BackgroundSuggestionStateIn"] = t.struct(
        {"backgroundColorSuggested": t.boolean().optional()}
    ).named(renames["BackgroundSuggestionStateIn"])
    types["BackgroundSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundSuggestionStateOut"])
    types["TableIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "tableStyle": t.proxy(renames["TableStyleIn"]).optional(),
            "rows": t.integer().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "columns": t.integer().optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "tableStyle": t.proxy(renames["TableStyleOut"]).optional(),
            "rows": t.integer().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "columns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["DeleteNamedRangeRequestIn"] = t.struct(
        {"namedRangeId": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DeleteNamedRangeRequestIn"])
    types["DeleteNamedRangeRequestOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteNamedRangeRequestOut"])
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
    types["StructuralElementIn"] = t.struct(
        {
            "paragraph": t.proxy(renames["ParagraphIn"]).optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "endIndex": t.integer().optional(),
            "sectionBreak": t.proxy(renames["SectionBreakIn"]).optional(),
            "tableOfContents": t.proxy(renames["TableOfContentsIn"]).optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["StructuralElementIn"])
    types["StructuralElementOut"] = t.struct(
        {
            "paragraph": t.proxy(renames["ParagraphOut"]).optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "endIndex": t.integer().optional(),
            "sectionBreak": t.proxy(renames["SectionBreakOut"]).optional(),
            "tableOfContents": t.proxy(renames["TableOfContentsOut"]).optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuralElementOut"])
    types["ListIn"] = t.struct(
        {
            "suggestedInsertionId": t.string().optional(),
            "listProperties": t.proxy(renames["ListPropertiesIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedListPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["ListIn"])
    types["ListOut"] = t.struct(
        {
            "suggestedInsertionId": t.string().optional(),
            "listProperties": t.proxy(renames["ListPropertiesOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedListPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOut"])
    types["FootnoteReferenceIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "footnoteId": t.string().optional(),
            "footnoteNumber": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["FootnoteReferenceIn"])
    types["FootnoteReferenceOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "footnoteId": t.string().optional(),
            "footnoteNumber": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FootnoteReferenceOut"])
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
    types["ColorIn"] = t.struct(
        {"rgbColor": t.proxy(renames["RgbColorIn"]).optional()}
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "rgbColor": t.proxy(renames["RgbColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["RangeIn"]).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
    types["HorizontalRuleIn"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["HorizontalRuleIn"])
    types["HorizontalRuleOut"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HorizontalRuleOut"])
    types["RequestIn"] = t.struct(
        {
            "insertTableRow": t.proxy(renames["InsertTableRowRequestIn"]).optional(),
            "createHeader": t.proxy(renames["CreateHeaderRequestIn"]).optional(),
            "replaceNamedRangeContent": t.proxy(
                renames["ReplaceNamedRangeContentRequestIn"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
            "insertTable": t.proxy(renames["InsertTableRequestIn"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "deletePositionedObject": t.proxy(
                renames["DeletePositionedObjectRequestIn"]
            ).optional(),
            "insertTableColumn": t.proxy(
                renames["InsertTableColumnRequestIn"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "pinTableHeaderRows": t.proxy(
                renames["PinTableHeaderRowsRequestIn"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterRequestIn"]).optional(),
            "deleteContentRange": t.proxy(
                renames["DeleteContentRangeRequestIn"]
            ).optional(),
            "deleteFooter": t.proxy(renames["DeleteFooterRequestIn"]).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "updateTableRowStyle": t.proxy(
                renames["UpdateTableRowStyleRequestIn"]
            ).optional(),
            "deleteHeader": t.proxy(renames["DeleteHeaderRequestIn"]).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageRequestIn"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteRequestIn"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeRequestIn"]
            ).optional(),
            "insertSectionBreak": t.proxy(
                renames["InsertSectionBreakRequestIn"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "insertPageBreak": t.proxy(renames["InsertPageBreakRequestIn"]).optional(),
            "updateDocumentStyle": t.proxy(
                renames["UpdateDocumentStyleRequestIn"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "updateSectionStyle": t.proxy(
                renames["UpdateSectionStyleRequestIn"]
            ).optional(),
            "updateTableCellStyle": t.proxy(
                renames["UpdateTableCellStyleRequestIn"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "insertTableRow": t.proxy(renames["InsertTableRowRequestOut"]).optional(),
            "createHeader": t.proxy(renames["CreateHeaderRequestOut"]).optional(),
            "replaceNamedRangeContent": t.proxy(
                renames["ReplaceNamedRangeContentRequestOut"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "insertTable": t.proxy(renames["InsertTableRequestOut"]).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "deletePositionedObject": t.proxy(
                renames["DeletePositionedObjectRequestOut"]
            ).optional(),
            "insertTableColumn": t.proxy(
                renames["InsertTableColumnRequestOut"]
            ).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "pinTableHeaderRows": t.proxy(
                renames["PinTableHeaderRowsRequestOut"]
            ).optional(),
            "createFooter": t.proxy(renames["CreateFooterRequestOut"]).optional(),
            "deleteContentRange": t.proxy(
                renames["DeleteContentRangeRequestOut"]
            ).optional(),
            "deleteFooter": t.proxy(renames["DeleteFooterRequestOut"]).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "updateTableRowStyle": t.proxy(
                renames["UpdateTableRowStyleRequestOut"]
            ).optional(),
            "deleteHeader": t.proxy(renames["DeleteHeaderRequestOut"]).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageRequestOut"]
            ).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteRequestOut"]).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeRequestOut"]
            ).optional(),
            "insertSectionBreak": t.proxy(
                renames["InsertSectionBreakRequestOut"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "insertPageBreak": t.proxy(renames["InsertPageBreakRequestOut"]).optional(),
            "updateDocumentStyle": t.proxy(
                renames["UpdateDocumentStyleRequestOut"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "updateSectionStyle": t.proxy(
                renames["UpdateSectionStyleRequestOut"]
            ).optional(),
            "updateTableCellStyle": t.proxy(
                renames["UpdateTableCellStyleRequestOut"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
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
    types["RichLinkIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["RichLinkIn"])
    types["RichLinkOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "richLinkId": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "richLinkProperties": t.proxy(renames["RichLinkPropertiesOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichLinkOut"])
    types["EmbeddedDrawingPropertiesSuggestionStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EmbeddedDrawingPropertiesSuggestionStateIn"])
    types["EmbeddedDrawingPropertiesSuggestionStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmbeddedDrawingPropertiesSuggestionStateOut"])
    types["ParagraphStyleSuggestionStateIn"] = t.struct(
        {
            "spacingModeSuggested": t.boolean().optional(),
            "pageBreakBeforeSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "lineSpacingSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "namedStyleTypeSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "directionSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "avoidWidowAndOrphanSuggested": t.boolean().optional(),
            "shadingSuggestionState": t.proxy(
                renames["ShadingSuggestionStateIn"]
            ).optional(),
            "headingIdSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "spaceBelowSuggested": t.boolean().optional(),
            "keepLinesTogetherSuggested": t.boolean().optional(),
            "borderBetweenSuggested": t.boolean().optional(),
            "alignmentSuggested": t.boolean().optional(),
            "spaceAboveSuggested": t.boolean().optional(),
            "indentEndSuggested": t.boolean().optional(),
            "keepWithNextSuggested": t.boolean().optional(),
        }
    ).named(renames["ParagraphStyleSuggestionStateIn"])
    types["ParagraphStyleSuggestionStateOut"] = t.struct(
        {
            "spacingModeSuggested": t.boolean().optional(),
            "pageBreakBeforeSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "lineSpacingSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "namedStyleTypeSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "directionSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "avoidWidowAndOrphanSuggested": t.boolean().optional(),
            "shadingSuggestionState": t.proxy(
                renames["ShadingSuggestionStateOut"]
            ).optional(),
            "headingIdSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "spaceBelowSuggested": t.boolean().optional(),
            "keepLinesTogetherSuggested": t.boolean().optional(),
            "borderBetweenSuggested": t.boolean().optional(),
            "alignmentSuggested": t.boolean().optional(),
            "spaceAboveSuggested": t.boolean().optional(),
            "indentEndSuggested": t.boolean().optional(),
            "keepWithNextSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleSuggestionStateOut"])
    types["DeleteContentRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["DeleteContentRangeRequestIn"])
    types["DeleteContentRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteContentRangeRequestOut"])
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
    types["DeleteTableColumnRequestIn"] = t.struct(
        {"tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional()}
    ).named(renames["DeleteTableColumnRequestIn"])
    types["DeleteTableColumnRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableColumnRequestOut"])
    types["UpdateParagraphStyleRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "range": t.proxy(renames["RangeIn"]).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestIn"])
    types["UpdateParagraphStyleRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParagraphStyleRequestOut"])
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
    types["InlineObjectPropertiesIn"] = t.struct(
        {"embeddedObject": t.proxy(renames["EmbeddedObjectIn"]).optional()}
    ).named(renames["InlineObjectPropertiesIn"])
    types["InlineObjectPropertiesOut"] = t.struct(
        {
            "embeddedObject": t.proxy(renames["EmbeddedObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectPropertiesOut"])
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
    types["InsertInlineImageRequestIn"] = t.struct(
        {
            "objectSize": t.proxy(renames["SizeIn"]).optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "uri": t.string().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
        }
    ).named(renames["InsertInlineImageRequestIn"])
    types["InsertInlineImageRequestOut"] = t.struct(
        {
            "objectSize": t.proxy(renames["SizeOut"]).optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "uri": t.string().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineImageRequestOut"])
    types["NamedStyleSuggestionStateIn"] = t.struct(
        {
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateIn"]
            ).optional(),
            "namedStyleType": t.string().optional(),
        }
    ).named(renames["NamedStyleSuggestionStateIn"])
    types["NamedStyleSuggestionStateOut"] = t.struct(
        {
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "paragraphStyleSuggestionState": t.proxy(
                renames["ParagraphStyleSuggestionStateOut"]
            ).optional(),
            "namedStyleType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStyleSuggestionStateOut"])
    types["UnmergeTableCellsRequestIn"] = t.struct(
        {"tableRange": t.proxy(renames["TableRangeIn"]).optional()}
    ).named(renames["UnmergeTableCellsRequestIn"])
    types["UnmergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeTableCellsRequestOut"])
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
    types["DeleteHeaderRequestIn"] = t.struct(
        {"headerId": t.string().optional()}
    ).named(renames["DeleteHeaderRequestIn"])
    types["DeleteHeaderRequestOut"] = t.struct(
        {
            "headerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteHeaderRequestOut"])
    types["RichLinkPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RichLinkPropertiesIn"]
    )
    types["RichLinkPropertiesOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "mimeType": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichLinkPropertiesOut"])
    types["TableCellLocationIn"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "columnIndex": t.integer().optional(),
        }
    ).named(renames["TableCellLocationIn"])
    types["TableCellLocationOut"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "columnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellLocationOut"])
    types["ColumnBreakIn"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["ColumnBreakIn"])
    types["ColumnBreakOut"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnBreakOut"])
    types["PersonIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "personProperties": t.proxy(renames["PersonPropertiesOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "personId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["TableRowIn"] = t.struct(
        {
            "suggestedTableRowStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
            "endIndex": t.integer().optional(),
            "tableCells": t.array(t.proxy(renames["TableCellIn"])).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "suggestedTableRowStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "endIndex": t.integer().optional(),
            "tableCells": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["BulletIn"] = t.struct(
        {
            "nestingLevel": t.integer().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "listId": t.string().optional(),
        }
    ).named(renames["BulletIn"])
    types["BulletOut"] = t.struct(
        {
            "nestingLevel": t.integer().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "listId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulletOut"])
    types["PositionedObjectPositioningSuggestionStateIn"] = t.struct(
        {
            "topOffsetSuggested": t.boolean().optional(),
            "layoutSuggested": t.boolean().optional(),
            "leftOffsetSuggested": t.boolean().optional(),
        }
    ).named(renames["PositionedObjectPositioningSuggestionStateIn"])
    types["PositionedObjectPositioningSuggestionStateOut"] = t.struct(
        {
            "topOffsetSuggested": t.boolean().optional(),
            "layoutSuggested": t.boolean().optional(),
            "leftOffsetSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningSuggestionStateOut"])
    types["TableCellIn"] = t.struct(
        {
            "suggestedTableCellStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "endIndex": t.integer().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "suggestedTableCellStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "endIndex": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
    types["SectionBreakIn"] = t.struct(
        {
            "sectionStyle": t.proxy(renames["SectionStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["SectionBreakIn"])
    types["SectionBreakOut"] = t.struct(
        {
            "sectionStyle": t.proxy(renames["SectionStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionBreakOut"])
    types["InsertInlineSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["InsertInlineSheetsChartResponseIn"])
    types["InsertInlineSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineSheetsChartResponseOut"])
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
    types["NamedStyleIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "namedStyleType": t.string().optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
        }
    ).named(renames["NamedStyleIn"])
    types["NamedStyleOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "namedStyleType": t.string().optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStyleOut"])
    types["TableCellStyleIn"] = t.struct(
        {
            "borderTop": t.proxy(renames["TableCellBorderIn"]).optional(),
            "borderRight": t.proxy(renames["TableCellBorderIn"]).optional(),
            "borderBottom": t.proxy(renames["TableCellBorderIn"]).optional(),
            "paddingRight": t.proxy(renames["DimensionIn"]).optional(),
            "contentAlignment": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "rowSpan": t.integer().optional(),
            "paddingBottom": t.proxy(renames["DimensionIn"]).optional(),
            "borderLeft": t.proxy(renames["TableCellBorderIn"]).optional(),
            "columnSpan": t.integer().optional(),
            "paddingTop": t.proxy(renames["DimensionIn"]).optional(),
            "paddingLeft": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["TableCellStyleIn"])
    types["TableCellStyleOut"] = t.struct(
        {
            "borderTop": t.proxy(renames["TableCellBorderOut"]).optional(),
            "borderRight": t.proxy(renames["TableCellBorderOut"]).optional(),
            "borderBottom": t.proxy(renames["TableCellBorderOut"]).optional(),
            "paddingRight": t.proxy(renames["DimensionOut"]).optional(),
            "contentAlignment": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "paddingBottom": t.proxy(renames["DimensionOut"]).optional(),
            "borderLeft": t.proxy(renames["TableCellBorderOut"]).optional(),
            "columnSpan": t.integer().optional(),
            "paddingTop": t.proxy(renames["DimensionOut"]).optional(),
            "paddingLeft": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellStyleOut"])
    types["SuggestedTextStyleIn"] = t.struct(
        {
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["SuggestedTextStyleIn"])
    types["SuggestedTextStyleOut"] = t.struct(
        {
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedTextStyleOut"])
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
    types["EmbeddedObjectBorderSuggestionStateIn"] = t.struct(
        {
            "colorSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
            "propertyStateSuggested": t.boolean().optional(),
            "dashStyleSuggested": t.boolean().optional(),
        }
    ).named(renames["EmbeddedObjectBorderSuggestionStateIn"])
    types["EmbeddedObjectBorderSuggestionStateOut"] = t.struct(
        {
            "colorSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
            "propertyStateSuggested": t.boolean().optional(),
            "dashStyleSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderSuggestionStateOut"])
    types["ListPropertiesIn"] = t.struct(
        {"nestingLevels": t.array(t.proxy(renames["NestingLevelIn"])).optional()}
    ).named(renames["ListPropertiesIn"])
    types["ListPropertiesOut"] = t.struct(
        {
            "nestingLevels": t.array(t.proxy(renames["NestingLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPropertiesOut"])
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
    types["ReplaceNamedRangeContentRequestIn"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "namedRangeName": t.string().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["ReplaceNamedRangeContentRequestIn"])
    types["ReplaceNamedRangeContentRequestOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "namedRangeName": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceNamedRangeContentRequestOut"])
    types["DeletePositionedObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeletePositionedObjectRequestIn"])
    types["DeletePositionedObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeletePositionedObjectRequestOut"])
    types["TableRowStyleSuggestionStateIn"] = t.struct(
        {"minRowHeightSuggested": t.boolean().optional()}
    ).named(renames["TableRowStyleSuggestionStateIn"])
    types["TableRowStyleSuggestionStateOut"] = t.struct(
        {
            "minRowHeightSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowStyleSuggestionStateOut"])
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
    types["EquationIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["EquationIn"])
    types["EquationOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EquationOut"])
    types["TextStyleSuggestionStateIn"] = t.struct(
        {
            "foregroundColorSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "underlineSuggested": t.boolean().optional(),
            "smallCapsSuggested": t.boolean().optional(),
            "weightedFontFamilySuggested": t.boolean().optional(),
            "baselineOffsetSuggested": t.boolean().optional(),
            "strikethroughSuggested": t.boolean().optional(),
            "linkSuggested": t.boolean().optional(),
            "boldSuggested": t.boolean().optional(),
            "fontSizeSuggested": t.boolean().optional(),
            "italicSuggested": t.boolean().optional(),
        }
    ).named(renames["TextStyleSuggestionStateIn"])
    types["TextStyleSuggestionStateOut"] = t.struct(
        {
            "foregroundColorSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "underlineSuggested": t.boolean().optional(),
            "smallCapsSuggested": t.boolean().optional(),
            "weightedFontFamilySuggested": t.boolean().optional(),
            "baselineOffsetSuggested": t.boolean().optional(),
            "strikethroughSuggested": t.boolean().optional(),
            "linkSuggested": t.boolean().optional(),
            "boldSuggested": t.boolean().optional(),
            "fontSizeSuggested": t.boolean().optional(),
            "italicSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleSuggestionStateOut"])
    types["DeleteFooterRequestIn"] = t.struct(
        {"footerId": t.string().optional()}
    ).named(renames["DeleteFooterRequestIn"])
    types["DeleteFooterRequestOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFooterRequestOut"])
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

    functions = {}
    functions["documentsCreate"] = docs.get(
        "v1/documents/{documentId}",
        t.struct(
            {
                "suggestionsViewMode": t.string().optional(),
                "documentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsBatchUpdate"] = docs.get(
        "v1/documents/{documentId}",
        t.struct(
            {
                "suggestionsViewMode": t.string().optional(),
                "documentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsGet"] = docs.get(
        "v1/documents/{documentId}",
        t.struct(
            {
                "suggestionsViewMode": t.string().optional(),
                "documentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="docs", renames=renames, types=Box(types), functions=Box(functions)
    )
