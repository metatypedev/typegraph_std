from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_docs() -> Import:
    docs = HTTPRuntime("https://docs.googleapis.com/")

    renames = {
        "ErrorResponse": "_docs_1_ErrorResponse",
        "ShadingSuggestionStateIn": "_docs_2_ShadingSuggestionStateIn",
        "ShadingSuggestionStateOut": "_docs_3_ShadingSuggestionStateOut",
        "UpdateTableColumnPropertiesRequestIn": "_docs_4_UpdateTableColumnPropertiesRequestIn",
        "UpdateTableColumnPropertiesRequestOut": "_docs_5_UpdateTableColumnPropertiesRequestOut",
        "PositionedObjectIn": "_docs_6_PositionedObjectIn",
        "PositionedObjectOut": "_docs_7_PositionedObjectOut",
        "OptionalColorIn": "_docs_8_OptionalColorIn",
        "OptionalColorOut": "_docs_9_OptionalColorOut",
        "RangeIn": "_docs_10_RangeIn",
        "RangeOut": "_docs_11_RangeOut",
        "BatchUpdateDocumentResponseIn": "_docs_12_BatchUpdateDocumentResponseIn",
        "BatchUpdateDocumentResponseOut": "_docs_13_BatchUpdateDocumentResponseOut",
        "UpdateDocumentStyleRequestIn": "_docs_14_UpdateDocumentStyleRequestIn",
        "UpdateDocumentStyleRequestOut": "_docs_15_UpdateDocumentStyleRequestOut",
        "LinkedContentReferenceSuggestionStateIn": "_docs_16_LinkedContentReferenceSuggestionStateIn",
        "LinkedContentReferenceSuggestionStateOut": "_docs_17_LinkedContentReferenceSuggestionStateOut",
        "CreateParagraphBulletsRequestIn": "_docs_18_CreateParagraphBulletsRequestIn",
        "CreateParagraphBulletsRequestOut": "_docs_19_CreateParagraphBulletsRequestOut",
        "LinkedContentReferenceIn": "_docs_20_LinkedContentReferenceIn",
        "LinkedContentReferenceOut": "_docs_21_LinkedContentReferenceOut",
        "InsertInlineSheetsChartResponseIn": "_docs_22_InsertInlineSheetsChartResponseIn",
        "InsertInlineSheetsChartResponseOut": "_docs_23_InsertInlineSheetsChartResponseOut",
        "PinTableHeaderRowsRequestIn": "_docs_24_PinTableHeaderRowsRequestIn",
        "PinTableHeaderRowsRequestOut": "_docs_25_PinTableHeaderRowsRequestOut",
        "InlineObjectPropertiesIn": "_docs_26_InlineObjectPropertiesIn",
        "InlineObjectPropertiesOut": "_docs_27_InlineObjectPropertiesOut",
        "InsertTableColumnRequestIn": "_docs_28_InsertTableColumnRequestIn",
        "InsertTableColumnRequestOut": "_docs_29_InsertTableColumnRequestOut",
        "BackgroundSuggestionStateIn": "_docs_30_BackgroundSuggestionStateIn",
        "BackgroundSuggestionStateOut": "_docs_31_BackgroundSuggestionStateOut",
        "ParagraphStyleSuggestionStateIn": "_docs_32_ParagraphStyleSuggestionStateIn",
        "ParagraphStyleSuggestionStateOut": "_docs_33_ParagraphStyleSuggestionStateOut",
        "ListIn": "_docs_34_ListIn",
        "ListOut": "_docs_35_ListOut",
        "CreateNamedRangeRequestIn": "_docs_36_CreateNamedRangeRequestIn",
        "CreateNamedRangeRequestOut": "_docs_37_CreateNamedRangeRequestOut",
        "PositionedObjectPositioningIn": "_docs_38_PositionedObjectPositioningIn",
        "PositionedObjectPositioningOut": "_docs_39_PositionedObjectPositioningOut",
        "TableStyleIn": "_docs_40_TableStyleIn",
        "TableStyleOut": "_docs_41_TableStyleOut",
        "ListPropertiesIn": "_docs_42_ListPropertiesIn",
        "ListPropertiesOut": "_docs_43_ListPropertiesOut",
        "FootnoteReferenceIn": "_docs_44_FootnoteReferenceIn",
        "FootnoteReferenceOut": "_docs_45_FootnoteReferenceOut",
        "ObjectReferencesIn": "_docs_46_ObjectReferencesIn",
        "ObjectReferencesOut": "_docs_47_ObjectReferencesOut",
        "AutoTextIn": "_docs_48_AutoTextIn",
        "AutoTextOut": "_docs_49_AutoTextOut",
        "TabStopIn": "_docs_50_TabStopIn",
        "TabStopOut": "_docs_51_TabStopOut",
        "LocationIn": "_docs_52_LocationIn",
        "LocationOut": "_docs_53_LocationOut",
        "SuggestedPositionedObjectPropertiesIn": "_docs_54_SuggestedPositionedObjectPropertiesIn",
        "SuggestedPositionedObjectPropertiesOut": "_docs_55_SuggestedPositionedObjectPropertiesOut",
        "DeleteNamedRangeRequestIn": "_docs_56_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_docs_57_DeleteNamedRangeRequestOut",
        "SectionColumnPropertiesIn": "_docs_58_SectionColumnPropertiesIn",
        "SectionColumnPropertiesOut": "_docs_59_SectionColumnPropertiesOut",
        "CreateFooterResponseIn": "_docs_60_CreateFooterResponseIn",
        "CreateFooterResponseOut": "_docs_61_CreateFooterResponseOut",
        "SizeIn": "_docs_62_SizeIn",
        "SizeOut": "_docs_63_SizeOut",
        "TableIn": "_docs_64_TableIn",
        "TableOut": "_docs_65_TableOut",
        "FootnoteIn": "_docs_66_FootnoteIn",
        "FootnoteOut": "_docs_67_FootnoteOut",
        "DocumentStyleSuggestionStateIn": "_docs_68_DocumentStyleSuggestionStateIn",
        "DocumentStyleSuggestionStateOut": "_docs_69_DocumentStyleSuggestionStateOut",
        "EmbeddedObjectIn": "_docs_70_EmbeddedObjectIn",
        "EmbeddedObjectOut": "_docs_71_EmbeddedObjectOut",
        "CreateFootnoteRequestIn": "_docs_72_CreateFootnoteRequestIn",
        "CreateFootnoteRequestOut": "_docs_73_CreateFootnoteRequestOut",
        "SheetsChartReferenceIn": "_docs_74_SheetsChartReferenceIn",
        "SheetsChartReferenceOut": "_docs_75_SheetsChartReferenceOut",
        "ParagraphBorderIn": "_docs_76_ParagraphBorderIn",
        "ParagraphBorderOut": "_docs_77_ParagraphBorderOut",
        "NamedStyleIn": "_docs_78_NamedStyleIn",
        "NamedStyleOut": "_docs_79_NamedStyleOut",
        "EmbeddedObjectBorderSuggestionStateIn": "_docs_80_EmbeddedObjectBorderSuggestionStateIn",
        "EmbeddedObjectBorderSuggestionStateOut": "_docs_81_EmbeddedObjectBorderSuggestionStateOut",
        "InlineObjectIn": "_docs_82_InlineObjectIn",
        "InlineObjectOut": "_docs_83_InlineObjectOut",
        "InsertTextRequestIn": "_docs_84_InsertTextRequestIn",
        "InsertTextRequestOut": "_docs_85_InsertTextRequestOut",
        "TableCellLocationIn": "_docs_86_TableCellLocationIn",
        "TableCellLocationOut": "_docs_87_TableCellLocationOut",
        "SuggestedTextStyleIn": "_docs_88_SuggestedTextStyleIn",
        "SuggestedTextStyleOut": "_docs_89_SuggestedTextStyleOut",
        "FooterIn": "_docs_90_FooterIn",
        "FooterOut": "_docs_91_FooterOut",
        "ListPropertiesSuggestionStateIn": "_docs_92_ListPropertiesSuggestionStateIn",
        "ListPropertiesSuggestionStateOut": "_docs_93_ListPropertiesSuggestionStateOut",
        "CreateHeaderRequestIn": "_docs_94_CreateHeaderRequestIn",
        "CreateHeaderRequestOut": "_docs_95_CreateHeaderRequestOut",
        "SuggestedTableCellStyleIn": "_docs_96_SuggestedTableCellStyleIn",
        "SuggestedTableCellStyleOut": "_docs_97_SuggestedTableCellStyleOut",
        "PositionedObjectPropertiesSuggestionStateIn": "_docs_98_PositionedObjectPropertiesSuggestionStateIn",
        "PositionedObjectPropertiesSuggestionStateOut": "_docs_99_PositionedObjectPropertiesSuggestionStateOut",
        "TableRangeIn": "_docs_100_TableRangeIn",
        "TableRangeOut": "_docs_101_TableRangeOut",
        "ReplaceNamedRangeContentRequestIn": "_docs_102_ReplaceNamedRangeContentRequestIn",
        "ReplaceNamedRangeContentRequestOut": "_docs_103_ReplaceNamedRangeContentRequestOut",
        "ReplaceAllTextRequestIn": "_docs_104_ReplaceAllTextRequestIn",
        "ReplaceAllTextRequestOut": "_docs_105_ReplaceAllTextRequestOut",
        "NamedStylesIn": "_docs_106_NamedStylesIn",
        "NamedStylesOut": "_docs_107_NamedStylesOut",
        "TableOfContentsIn": "_docs_108_TableOfContentsIn",
        "TableOfContentsOut": "_docs_109_TableOfContentsOut",
        "NamedStylesSuggestionStateIn": "_docs_110_NamedStylesSuggestionStateIn",
        "NamedStylesSuggestionStateOut": "_docs_111_NamedStylesSuggestionStateOut",
        "TableCellStyleSuggestionStateIn": "_docs_112_TableCellStyleSuggestionStateIn",
        "TableCellStyleSuggestionStateOut": "_docs_113_TableCellStyleSuggestionStateOut",
        "ResponseIn": "_docs_114_ResponseIn",
        "ResponseOut": "_docs_115_ResponseOut",
        "SheetsChartReferenceSuggestionStateIn": "_docs_116_SheetsChartReferenceSuggestionStateIn",
        "SheetsChartReferenceSuggestionStateOut": "_docs_117_SheetsChartReferenceSuggestionStateOut",
        "WeightedFontFamilyIn": "_docs_118_WeightedFontFamilyIn",
        "WeightedFontFamilyOut": "_docs_119_WeightedFontFamilyOut",
        "InsertInlineImageRequestIn": "_docs_120_InsertInlineImageRequestIn",
        "InsertInlineImageRequestOut": "_docs_121_InsertInlineImageRequestOut",
        "TextStyleIn": "_docs_122_TextStyleIn",
        "TextStyleOut": "_docs_123_TextStyleOut",
        "SizeSuggestionStateIn": "_docs_124_SizeSuggestionStateIn",
        "SizeSuggestionStateOut": "_docs_125_SizeSuggestionStateOut",
        "CropPropertiesSuggestionStateIn": "_docs_126_CropPropertiesSuggestionStateIn",
        "CropPropertiesSuggestionStateOut": "_docs_127_CropPropertiesSuggestionStateOut",
        "TextStyleSuggestionStateIn": "_docs_128_TextStyleSuggestionStateIn",
        "TextStyleSuggestionStateOut": "_docs_129_TextStyleSuggestionStateOut",
        "EmbeddedObjectBorderIn": "_docs_130_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_docs_131_EmbeddedObjectBorderOut",
        "InlineObjectElementIn": "_docs_132_InlineObjectElementIn",
        "InlineObjectElementOut": "_docs_133_InlineObjectElementOut",
        "CreateHeaderResponseIn": "_docs_134_CreateHeaderResponseIn",
        "CreateHeaderResponseOut": "_docs_135_CreateHeaderResponseOut",
        "BackgroundIn": "_docs_136_BackgroundIn",
        "BackgroundOut": "_docs_137_BackgroundOut",
        "EmbeddedDrawingPropertiesSuggestionStateIn": "_docs_138_EmbeddedDrawingPropertiesSuggestionStateIn",
        "EmbeddedDrawingPropertiesSuggestionStateOut": "_docs_139_EmbeddedDrawingPropertiesSuggestionStateOut",
        "EmbeddedObjectSuggestionStateIn": "_docs_140_EmbeddedObjectSuggestionStateIn",
        "EmbeddedObjectSuggestionStateOut": "_docs_141_EmbeddedObjectSuggestionStateOut",
        "PersonPropertiesIn": "_docs_142_PersonPropertiesIn",
        "PersonPropertiesOut": "_docs_143_PersonPropertiesOut",
        "InsertTableRequestIn": "_docs_144_InsertTableRequestIn",
        "InsertTableRequestOut": "_docs_145_InsertTableRequestOut",
        "EquationIn": "_docs_146_EquationIn",
        "EquationOut": "_docs_147_EquationOut",
        "UpdateTableCellStyleRequestIn": "_docs_148_UpdateTableCellStyleRequestIn",
        "UpdateTableCellStyleRequestOut": "_docs_149_UpdateTableCellStyleRequestOut",
        "BulletIn": "_docs_150_BulletIn",
        "BulletOut": "_docs_151_BulletOut",
        "DocumentIn": "_docs_152_DocumentIn",
        "DocumentOut": "_docs_153_DocumentOut",
        "BatchUpdateDocumentRequestIn": "_docs_154_BatchUpdateDocumentRequestIn",
        "BatchUpdateDocumentRequestOut": "_docs_155_BatchUpdateDocumentRequestOut",
        "InsertSectionBreakRequestIn": "_docs_156_InsertSectionBreakRequestIn",
        "InsertSectionBreakRequestOut": "_docs_157_InsertSectionBreakRequestOut",
        "UpdateParagraphStyleRequestIn": "_docs_158_UpdateParagraphStyleRequestIn",
        "UpdateParagraphStyleRequestOut": "_docs_159_UpdateParagraphStyleRequestOut",
        "PositionedObjectPropertiesIn": "_docs_160_PositionedObjectPropertiesIn",
        "PositionedObjectPropertiesOut": "_docs_161_PositionedObjectPropertiesOut",
        "SectionBreakIn": "_docs_162_SectionBreakIn",
        "SectionBreakOut": "_docs_163_SectionBreakOut",
        "SuggestedDocumentStyleIn": "_docs_164_SuggestedDocumentStyleIn",
        "SuggestedDocumentStyleOut": "_docs_165_SuggestedDocumentStyleOut",
        "NamedStyleSuggestionStateIn": "_docs_166_NamedStyleSuggestionStateIn",
        "NamedStyleSuggestionStateOut": "_docs_167_NamedStyleSuggestionStateOut",
        "TextRunIn": "_docs_168_TextRunIn",
        "TextRunOut": "_docs_169_TextRunOut",
        "NestingLevelSuggestionStateIn": "_docs_170_NestingLevelSuggestionStateIn",
        "NestingLevelSuggestionStateOut": "_docs_171_NestingLevelSuggestionStateOut",
        "ImagePropertiesSuggestionStateIn": "_docs_172_ImagePropertiesSuggestionStateIn",
        "ImagePropertiesSuggestionStateOut": "_docs_173_ImagePropertiesSuggestionStateOut",
        "SuggestedInlineObjectPropertiesIn": "_docs_174_SuggestedInlineObjectPropertiesIn",
        "SuggestedInlineObjectPropertiesOut": "_docs_175_SuggestedInlineObjectPropertiesOut",
        "RichLinkPropertiesIn": "_docs_176_RichLinkPropertiesIn",
        "RichLinkPropertiesOut": "_docs_177_RichLinkPropertiesOut",
        "InlineObjectPropertiesSuggestionStateIn": "_docs_178_InlineObjectPropertiesSuggestionStateIn",
        "InlineObjectPropertiesSuggestionStateOut": "_docs_179_InlineObjectPropertiesSuggestionStateOut",
        "InsertPageBreakRequestIn": "_docs_180_InsertPageBreakRequestIn",
        "InsertPageBreakRequestOut": "_docs_181_InsertPageBreakRequestOut",
        "PositionedObjectPositioningSuggestionStateIn": "_docs_182_PositionedObjectPositioningSuggestionStateIn",
        "PositionedObjectPositioningSuggestionStateOut": "_docs_183_PositionedObjectPositioningSuggestionStateOut",
        "NestingLevelIn": "_docs_184_NestingLevelIn",
        "NestingLevelOut": "_docs_185_NestingLevelOut",
        "UpdateTableRowStyleRequestIn": "_docs_186_UpdateTableRowStyleRequestIn",
        "UpdateTableRowStyleRequestOut": "_docs_187_UpdateTableRowStyleRequestOut",
        "PersonIn": "_docs_188_PersonIn",
        "PersonOut": "_docs_189_PersonOut",
        "NamedRangeIn": "_docs_190_NamedRangeIn",
        "NamedRangeOut": "_docs_191_NamedRangeOut",
        "MergeTableCellsRequestIn": "_docs_192_MergeTableCellsRequestIn",
        "MergeTableCellsRequestOut": "_docs_193_MergeTableCellsRequestOut",
        "RichLinkIn": "_docs_194_RichLinkIn",
        "RichLinkOut": "_docs_195_RichLinkOut",
        "CreateNamedRangeResponseIn": "_docs_196_CreateNamedRangeResponseIn",
        "CreateNamedRangeResponseOut": "_docs_197_CreateNamedRangeResponseOut",
        "SuggestedBulletIn": "_docs_198_SuggestedBulletIn",
        "SuggestedBulletOut": "_docs_199_SuggestedBulletOut",
        "RequestIn": "_docs_200_RequestIn",
        "RequestOut": "_docs_201_RequestOut",
        "ImagePropertiesIn": "_docs_202_ImagePropertiesIn",
        "ImagePropertiesOut": "_docs_203_ImagePropertiesOut",
        "HeaderIn": "_docs_204_HeaderIn",
        "HeaderOut": "_docs_205_HeaderOut",
        "TableRowStyleSuggestionStateIn": "_docs_206_TableRowStyleSuggestionStateIn",
        "TableRowStyleSuggestionStateOut": "_docs_207_TableRowStyleSuggestionStateOut",
        "ParagraphStyleIn": "_docs_208_ParagraphStyleIn",
        "ParagraphStyleOut": "_docs_209_ParagraphStyleOut",
        "ParagraphElementIn": "_docs_210_ParagraphElementIn",
        "ParagraphElementOut": "_docs_211_ParagraphElementOut",
        "TableColumnPropertiesIn": "_docs_212_TableColumnPropertiesIn",
        "TableColumnPropertiesOut": "_docs_213_TableColumnPropertiesOut",
        "SuggestedParagraphStyleIn": "_docs_214_SuggestedParagraphStyleIn",
        "SuggestedParagraphStyleOut": "_docs_215_SuggestedParagraphStyleOut",
        "UnmergeTableCellsRequestIn": "_docs_216_UnmergeTableCellsRequestIn",
        "UnmergeTableCellsRequestOut": "_docs_217_UnmergeTableCellsRequestOut",
        "LinkIn": "_docs_218_LinkIn",
        "LinkOut": "_docs_219_LinkOut",
        "TableRowIn": "_docs_220_TableRowIn",
        "TableRowOut": "_docs_221_TableRowOut",
        "DeleteParagraphBulletsRequestIn": "_docs_222_DeleteParagraphBulletsRequestIn",
        "DeleteParagraphBulletsRequestOut": "_docs_223_DeleteParagraphBulletsRequestOut",
        "PageBreakIn": "_docs_224_PageBreakIn",
        "PageBreakOut": "_docs_225_PageBreakOut",
        "HorizontalRuleIn": "_docs_226_HorizontalRuleIn",
        "HorizontalRuleOut": "_docs_227_HorizontalRuleOut",
        "InsertInlineImageResponseIn": "_docs_228_InsertInlineImageResponseIn",
        "InsertInlineImageResponseOut": "_docs_229_InsertInlineImageResponseOut",
        "SectionStyleIn": "_docs_230_SectionStyleIn",
        "SectionStyleOut": "_docs_231_SectionStyleOut",
        "StructuralElementIn": "_docs_232_StructuralElementIn",
        "StructuralElementOut": "_docs_233_StructuralElementOut",
        "TableCellIn": "_docs_234_TableCellIn",
        "TableCellOut": "_docs_235_TableCellOut",
        "InsertTableRowRequestIn": "_docs_236_InsertTableRowRequestIn",
        "InsertTableRowRequestOut": "_docs_237_InsertTableRowRequestOut",
        "DeleteHeaderRequestIn": "_docs_238_DeleteHeaderRequestIn",
        "DeleteHeaderRequestOut": "_docs_239_DeleteHeaderRequestOut",
        "DeleteTableRowRequestIn": "_docs_240_DeleteTableRowRequestIn",
        "DeleteTableRowRequestOut": "_docs_241_DeleteTableRowRequestOut",
        "ColumnBreakIn": "_docs_242_ColumnBreakIn",
        "ColumnBreakOut": "_docs_243_ColumnBreakOut",
        "SubstringMatchCriteriaIn": "_docs_244_SubstringMatchCriteriaIn",
        "SubstringMatchCriteriaOut": "_docs_245_SubstringMatchCriteriaOut",
        "EmbeddedDrawingPropertiesIn": "_docs_246_EmbeddedDrawingPropertiesIn",
        "EmbeddedDrawingPropertiesOut": "_docs_247_EmbeddedDrawingPropertiesOut",
        "TableCellStyleIn": "_docs_248_TableCellStyleIn",
        "TableCellStyleOut": "_docs_249_TableCellStyleOut",
        "ReplaceImageRequestIn": "_docs_250_ReplaceImageRequestIn",
        "ReplaceImageRequestOut": "_docs_251_ReplaceImageRequestOut",
        "ColorIn": "_docs_252_ColorIn",
        "ColorOut": "_docs_253_ColorOut",
        "EndOfSegmentLocationIn": "_docs_254_EndOfSegmentLocationIn",
        "EndOfSegmentLocationOut": "_docs_255_EndOfSegmentLocationOut",
        "BodyIn": "_docs_256_BodyIn",
        "BodyOut": "_docs_257_BodyOut",
        "DeleteFooterRequestIn": "_docs_258_DeleteFooterRequestIn",
        "DeleteFooterRequestOut": "_docs_259_DeleteFooterRequestOut",
        "DeletePositionedObjectRequestIn": "_docs_260_DeletePositionedObjectRequestIn",
        "DeletePositionedObjectRequestOut": "_docs_261_DeletePositionedObjectRequestOut",
        "RgbColorIn": "_docs_262_RgbColorIn",
        "RgbColorOut": "_docs_263_RgbColorOut",
        "SuggestedListPropertiesIn": "_docs_264_SuggestedListPropertiesIn",
        "SuggestedListPropertiesOut": "_docs_265_SuggestedListPropertiesOut",
        "WriteControlIn": "_docs_266_WriteControlIn",
        "WriteControlOut": "_docs_267_WriteControlOut",
        "CreateFooterRequestIn": "_docs_268_CreateFooterRequestIn",
        "CreateFooterRequestOut": "_docs_269_CreateFooterRequestOut",
        "DeleteContentRangeRequestIn": "_docs_270_DeleteContentRangeRequestIn",
        "DeleteContentRangeRequestOut": "_docs_271_DeleteContentRangeRequestOut",
        "DimensionIn": "_docs_272_DimensionIn",
        "DimensionOut": "_docs_273_DimensionOut",
        "SuggestedTableRowStyleIn": "_docs_274_SuggestedTableRowStyleIn",
        "SuggestedTableRowStyleOut": "_docs_275_SuggestedTableRowStyleOut",
        "DocumentStyleIn": "_docs_276_DocumentStyleIn",
        "DocumentStyleOut": "_docs_277_DocumentStyleOut",
        "BulletSuggestionStateIn": "_docs_278_BulletSuggestionStateIn",
        "BulletSuggestionStateOut": "_docs_279_BulletSuggestionStateOut",
        "CreateFootnoteResponseIn": "_docs_280_CreateFootnoteResponseIn",
        "CreateFootnoteResponseOut": "_docs_281_CreateFootnoteResponseOut",
        "UpdateTextStyleRequestIn": "_docs_282_UpdateTextStyleRequestIn",
        "UpdateTextStyleRequestOut": "_docs_283_UpdateTextStyleRequestOut",
        "TableRowStyleIn": "_docs_284_TableRowStyleIn",
        "TableRowStyleOut": "_docs_285_TableRowStyleOut",
        "UpdateSectionStyleRequestIn": "_docs_286_UpdateSectionStyleRequestIn",
        "UpdateSectionStyleRequestOut": "_docs_287_UpdateSectionStyleRequestOut",
        "CropPropertiesIn": "_docs_288_CropPropertiesIn",
        "CropPropertiesOut": "_docs_289_CropPropertiesOut",
        "SuggestedNamedStylesIn": "_docs_290_SuggestedNamedStylesIn",
        "SuggestedNamedStylesOut": "_docs_291_SuggestedNamedStylesOut",
        "DeleteTableColumnRequestIn": "_docs_292_DeleteTableColumnRequestIn",
        "DeleteTableColumnRequestOut": "_docs_293_DeleteTableColumnRequestOut",
        "TableCellBorderIn": "_docs_294_TableCellBorderIn",
        "TableCellBorderOut": "_docs_295_TableCellBorderOut",
        "ShadingIn": "_docs_296_ShadingIn",
        "ShadingOut": "_docs_297_ShadingOut",
        "ReplaceAllTextResponseIn": "_docs_298_ReplaceAllTextResponseIn",
        "ReplaceAllTextResponseOut": "_docs_299_ReplaceAllTextResponseOut",
        "NamedRangesIn": "_docs_300_NamedRangesIn",
        "NamedRangesOut": "_docs_301_NamedRangesOut",
        "ParagraphIn": "_docs_302_ParagraphIn",
        "ParagraphOut": "_docs_303_ParagraphOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ShadingSuggestionStateIn"] = t.struct(
        {"backgroundColorSuggested": t.boolean().optional()}
    ).named(renames["ShadingSuggestionStateIn"])
    types["ShadingSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadingSuggestionStateOut"])
    types["UpdateTableColumnPropertiesRequestIn"] = t.struct(
        {
            "columnIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesIn"]
            ).optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestIn"])
    types["UpdateTableColumnPropertiesRequestOut"] = t.struct(
        {
            "columnIndices": t.array(t.integer()).optional(),
            "fields": t.string().optional(),
            "tableColumnProperties": t.proxy(
                renames["TableColumnPropertiesOut"]
            ).optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableColumnPropertiesRequestOut"])
    types["PositionedObjectIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesIn"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionId": t.string().optional(),
            "suggestedPositionedObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["PositionedObjectIn"])
    types["PositionedObjectOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "positionedObjectProperties": t.proxy(
                renames["PositionedObjectPropertiesOut"]
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionId": t.string().optional(),
            "suggestedPositionedObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectOut"])
    types["OptionalColorIn"] = t.struct(
        {"color": t.proxy(renames["ColorIn"]).optional()}
    ).named(renames["OptionalColorIn"])
    types["OptionalColorOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionalColorOut"])
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
    types["BatchUpdateDocumentResponseIn"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
            "documentId": t.string().optional(),
        }
    ).named(renames["BatchUpdateDocumentResponseIn"])
    types["BatchUpdateDocumentResponseOut"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "documentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDocumentResponseOut"])
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
    types["InsertInlineSheetsChartResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["InsertInlineSheetsChartResponseIn"])
    types["InsertInlineSheetsChartResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineSheetsChartResponseOut"])
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
    types["InlineObjectPropertiesIn"] = t.struct(
        {"embeddedObject": t.proxy(renames["EmbeddedObjectIn"]).optional()}
    ).named(renames["InlineObjectPropertiesIn"])
    types["InlineObjectPropertiesOut"] = t.struct(
        {
            "embeddedObject": t.proxy(renames["EmbeddedObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectPropertiesOut"])
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
    types["BackgroundSuggestionStateIn"] = t.struct(
        {"backgroundColorSuggested": t.boolean().optional()}
    ).named(renames["BackgroundSuggestionStateIn"])
    types["BackgroundSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundSuggestionStateOut"])
    types["ParagraphStyleSuggestionStateIn"] = t.struct(
        {
            "directionSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "spacingModeSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "indentEndSuggested": t.boolean().optional(),
            "keepWithNextSuggested": t.boolean().optional(),
            "spaceAboveSuggested": t.boolean().optional(),
            "borderBetweenSuggested": t.boolean().optional(),
            "avoidWidowAndOrphanSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "spaceBelowSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "headingIdSuggested": t.boolean().optional(),
            "shadingSuggestionState": t.proxy(
                renames["ShadingSuggestionStateIn"]
            ).optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "lineSpacingSuggested": t.boolean().optional(),
            "keepLinesTogetherSuggested": t.boolean().optional(),
            "namedStyleTypeSuggested": t.boolean().optional(),
            "pageBreakBeforeSuggested": t.boolean().optional(),
            "alignmentSuggested": t.boolean().optional(),
        }
    ).named(renames["ParagraphStyleSuggestionStateIn"])
    types["ParagraphStyleSuggestionStateOut"] = t.struct(
        {
            "directionSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "spacingModeSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "indentEndSuggested": t.boolean().optional(),
            "keepWithNextSuggested": t.boolean().optional(),
            "spaceAboveSuggested": t.boolean().optional(),
            "borderBetweenSuggested": t.boolean().optional(),
            "avoidWidowAndOrphanSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "spaceBelowSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "headingIdSuggested": t.boolean().optional(),
            "shadingSuggestionState": t.proxy(
                renames["ShadingSuggestionStateOut"]
            ).optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "lineSpacingSuggested": t.boolean().optional(),
            "keepLinesTogetherSuggested": t.boolean().optional(),
            "namedStyleTypeSuggested": t.boolean().optional(),
            "pageBreakBeforeSuggested": t.boolean().optional(),
            "alignmentSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleSuggestionStateOut"])
    types["ListIn"] = t.struct(
        {
            "suggestedInsertionId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedListPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "listProperties": t.proxy(renames["ListPropertiesIn"]).optional(),
        }
    ).named(renames["ListIn"])
    types["ListOut"] = t.struct(
        {
            "suggestedInsertionId": t.string().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedListPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "listProperties": t.proxy(renames["ListPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOut"])
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
    types["ListPropertiesIn"] = t.struct(
        {"nestingLevels": t.array(t.proxy(renames["NestingLevelIn"])).optional()}
    ).named(renames["ListPropertiesIn"])
    types["ListPropertiesOut"] = t.struct(
        {
            "nestingLevels": t.array(t.proxy(renames["NestingLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPropertiesOut"])
    types["FootnoteReferenceIn"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "footnoteNumber": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "footnoteId": t.string().optional(),
        }
    ).named(renames["FootnoteReferenceIn"])
    types["FootnoteReferenceOut"] = t.struct(
        {
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "footnoteNumber": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "footnoteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FootnoteReferenceOut"])
    types["ObjectReferencesIn"] = t.struct(
        {"objectIds": t.array(t.string()).optional()}
    ).named(renames["ObjectReferencesIn"])
    types["ObjectReferencesOut"] = t.struct(
        {
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectReferencesOut"])
    types["AutoTextIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["AutoTextIn"])
    types["AutoTextOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoTextOut"])
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
    types["CreateFooterResponseIn"] = t.struct(
        {"footerId": t.string().optional()}
    ).named(renames["CreateFooterResponseIn"])
    types["CreateFooterResponseOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFooterResponseOut"])
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
    types["TableIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "rows": t.integer().optional(),
            "tableStyle": t.proxy(renames["TableStyleIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "columns": t.integer().optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "rows": t.integer().optional(),
            "tableStyle": t.proxy(renames["TableStyleOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "tableRows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "columns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
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
    types["DocumentStyleSuggestionStateIn"] = t.struct(
        {
            "marginTopSuggested": t.boolean().optional(),
            "useCustomHeaderFooterMarginsSuggested": t.boolean().optional(),
            "useEvenPageHeaderFooterSuggested": t.boolean().optional(),
            "marginFooterSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "evenPageHeaderIdSuggested": t.boolean().optional(),
            "evenPageFooterIdSuggested": t.boolean().optional(),
            "useFirstPageHeaderFooterSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "defaultHeaderIdSuggested": t.boolean().optional(),
            "marginHeaderSuggested": t.boolean().optional(),
            "firstPageFooterIdSuggested": t.boolean().optional(),
            "firstPageHeaderIdSuggested": t.boolean().optional(),
            "backgroundSuggestionState": t.proxy(
                renames["BackgroundSuggestionStateIn"]
            ).optional(),
            "pageNumberStartSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "defaultFooterIdSuggested": t.boolean().optional(),
            "pageSizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["DocumentStyleSuggestionStateIn"])
    types["DocumentStyleSuggestionStateOut"] = t.struct(
        {
            "marginTopSuggested": t.boolean().optional(),
            "useCustomHeaderFooterMarginsSuggested": t.boolean().optional(),
            "useEvenPageHeaderFooterSuggested": t.boolean().optional(),
            "marginFooterSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "evenPageHeaderIdSuggested": t.boolean().optional(),
            "evenPageFooterIdSuggested": t.boolean().optional(),
            "useFirstPageHeaderFooterSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "defaultHeaderIdSuggested": t.boolean().optional(),
            "marginHeaderSuggested": t.boolean().optional(),
            "firstPageFooterIdSuggested": t.boolean().optional(),
            "firstPageHeaderIdSuggested": t.boolean().optional(),
            "backgroundSuggestionState": t.proxy(
                renames["BackgroundSuggestionStateOut"]
            ).optional(),
            "pageNumberStartSuggested": t.boolean().optional(),
            "marginLeftSuggested": t.boolean().optional(),
            "defaultFooterIdSuggested": t.boolean().optional(),
            "pageSizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentStyleSuggestionStateOut"])
    types["EmbeddedObjectIn"] = t.struct(
        {
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "description": t.string().optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "title": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesIn"]).optional(),
            "embeddedObjectBorder": t.proxy(
                renames["EmbeddedObjectBorderIn"]
            ).optional(),
            "linkedContentReference": t.proxy(
                renames["LinkedContentReferenceIn"]
            ).optional(),
            "embeddedDrawingProperties": t.proxy(
                renames["EmbeddedDrawingPropertiesIn"]
            ).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
        }
    ).named(renames["EmbeddedObjectIn"])
    types["EmbeddedObjectOut"] = t.struct(
        {
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "description": t.string().optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "title": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "imageProperties": t.proxy(renames["ImagePropertiesOut"]).optional(),
            "embeddedObjectBorder": t.proxy(
                renames["EmbeddedObjectBorderOut"]
            ).optional(),
            "linkedContentReference": t.proxy(
                renames["LinkedContentReferenceOut"]
            ).optional(),
            "embeddedDrawingProperties": t.proxy(
                renames["EmbeddedDrawingPropertiesOut"]
            ).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectOut"])
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
    types["ParagraphBorderIn"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "padding": t.proxy(renames["DimensionIn"]).optional(),
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["ParagraphBorderIn"])
    types["ParagraphBorderOut"] = t.struct(
        {
            "dashStyle": t.string().optional(),
            "padding": t.proxy(renames["DimensionOut"]).optional(),
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphBorderOut"])
    types["NamedStyleIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "namedStyleType": t.string().optional(),
        }
    ).named(renames["NamedStyleIn"])
    types["NamedStyleOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "namedStyleType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStyleOut"])
    types["EmbeddedObjectBorderSuggestionStateIn"] = t.struct(
        {
            "dashStyleSuggested": t.boolean().optional(),
            "colorSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
            "propertyStateSuggested": t.boolean().optional(),
        }
    ).named(renames["EmbeddedObjectBorderSuggestionStateIn"])
    types["EmbeddedObjectBorderSuggestionStateOut"] = t.struct(
        {
            "dashStyleSuggested": t.boolean().optional(),
            "colorSuggested": t.boolean().optional(),
            "widthSuggested": t.boolean().optional(),
            "propertyStateSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderSuggestionStateOut"])
    types["InlineObjectIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInlineObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesIn"]
            ).optional(),
            "objectId": t.string().optional(),
            "suggestedInsertionId": t.string().optional(),
        }
    ).named(renames["InlineObjectIn"])
    types["InlineObjectOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInlineObjectPropertiesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesOut"]
            ).optional(),
            "objectId": t.string().optional(),
            "suggestedInsertionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineObjectOut"])
    types["InsertTextRequestIn"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["InsertTextRequestIn"])
    types["InsertTextRequestOut"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTextRequestOut"])
    types["TableCellLocationIn"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
        }
    ).named(renames["TableCellLocationIn"])
    types["TableCellLocationOut"] = t.struct(
        {
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellLocationOut"])
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
    types["FooterIn"] = t.struct(
        {
            "footerId": t.string().optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
        }
    ).named(renames["FooterIn"])
    types["FooterOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FooterOut"])
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
    types["TableRangeIn"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional(),
            "rowSpan": t.integer().optional(),
            "columnSpan": t.integer().optional(),
        }
    ).named(renames["TableRangeIn"])
    types["TableRangeOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "columnSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRangeOut"])
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
    types["NamedStylesIn"] = t.struct(
        {"styles": t.array(t.proxy(renames["NamedStyleIn"])).optional()}
    ).named(renames["NamedStylesIn"])
    types["NamedStylesOut"] = t.struct(
        {
            "styles": t.array(t.proxy(renames["NamedStyleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedStylesOut"])
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
            "backgroundColorSuggested": t.boolean().optional(),
            "columnSpanSuggested": t.boolean().optional(),
            "paddingLeftSuggested": t.boolean().optional(),
            "paddingTopSuggested": t.boolean().optional(),
            "rowSpanSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "contentAlignmentSuggested": t.boolean().optional(),
            "paddingBottomSuggested": t.boolean().optional(),
            "paddingRightSuggested": t.boolean().optional(),
        }
    ).named(renames["TableCellStyleSuggestionStateIn"])
    types["TableCellStyleSuggestionStateOut"] = t.struct(
        {
            "backgroundColorSuggested": t.boolean().optional(),
            "columnSpanSuggested": t.boolean().optional(),
            "paddingLeftSuggested": t.boolean().optional(),
            "paddingTopSuggested": t.boolean().optional(),
            "rowSpanSuggested": t.boolean().optional(),
            "borderRightSuggested": t.boolean().optional(),
            "borderBottomSuggested": t.boolean().optional(),
            "borderLeftSuggested": t.boolean().optional(),
            "borderTopSuggested": t.boolean().optional(),
            "contentAlignmentSuggested": t.boolean().optional(),
            "paddingBottomSuggested": t.boolean().optional(),
            "paddingRightSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellStyleSuggestionStateOut"])
    types["ResponseIn"] = t.struct(
        {
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageResponseIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseIn"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteResponseIn"]).optional(),
            "createFooter": t.proxy(renames["CreateFooterResponseIn"]).optional(),
            "createHeader": t.proxy(renames["CreateHeaderResponseIn"]).optional(),
            "insertInlineSheetsChart": t.proxy(
                renames["InsertInlineSheetsChartResponseIn"]
            ).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeResponseIn"]
            ).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageResponseOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextResponseOut"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteResponseOut"]).optional(),
            "createFooter": t.proxy(renames["CreateFooterResponseOut"]).optional(),
            "createHeader": t.proxy(renames["CreateHeaderResponseOut"]).optional(),
            "insertInlineSheetsChart": t.proxy(
                renames["InsertInlineSheetsChartResponseOut"]
            ).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
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
    types["InsertInlineImageRequestIn"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "uri": t.string().optional(),
            "objectSize": t.proxy(renames["SizeIn"]).optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["InsertInlineImageRequestIn"])
    types["InsertInlineImageRequestOut"] = t.struct(
        {
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "uri": t.string().optional(),
            "objectSize": t.proxy(renames["SizeOut"]).optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineImageRequestOut"])
    types["TextStyleIn"] = t.struct(
        {
            "fontSize": t.proxy(renames["DimensionIn"]).optional(),
            "italic": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "strikethrough": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyIn"]).optional(),
            "bold": t.boolean().optional(),
        }
    ).named(renames["TextStyleIn"])
    types["TextStyleOut"] = t.struct(
        {
            "fontSize": t.proxy(renames["DimensionOut"]).optional(),
            "italic": t.boolean().optional(),
            "smallCaps": t.boolean().optional(),
            "underline": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "strikethrough": t.boolean().optional(),
            "baselineOffset": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "weightedFontFamily": t.proxy(renames["WeightedFontFamilyOut"]).optional(),
            "bold": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleOut"])
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
    types["CropPropertiesSuggestionStateIn"] = t.struct(
        {
            "offsetLeftSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "offsetBottomSuggested": t.boolean().optional(),
            "offsetTopSuggested": t.boolean().optional(),
            "offsetRightSuggested": t.boolean().optional(),
        }
    ).named(renames["CropPropertiesSuggestionStateIn"])
    types["CropPropertiesSuggestionStateOut"] = t.struct(
        {
            "offsetLeftSuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "offsetBottomSuggested": t.boolean().optional(),
            "offsetTopSuggested": t.boolean().optional(),
            "offsetRightSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesSuggestionStateOut"])
    types["TextStyleSuggestionStateIn"] = t.struct(
        {
            "foregroundColorSuggested": t.boolean().optional(),
            "boldSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "weightedFontFamilySuggested": t.boolean().optional(),
            "smallCapsSuggested": t.boolean().optional(),
            "italicSuggested": t.boolean().optional(),
            "fontSizeSuggested": t.boolean().optional(),
            "linkSuggested": t.boolean().optional(),
            "baselineOffsetSuggested": t.boolean().optional(),
            "underlineSuggested": t.boolean().optional(),
            "strikethroughSuggested": t.boolean().optional(),
        }
    ).named(renames["TextStyleSuggestionStateIn"])
    types["TextStyleSuggestionStateOut"] = t.struct(
        {
            "foregroundColorSuggested": t.boolean().optional(),
            "boldSuggested": t.boolean().optional(),
            "backgroundColorSuggested": t.boolean().optional(),
            "weightedFontFamilySuggested": t.boolean().optional(),
            "smallCapsSuggested": t.boolean().optional(),
            "italicSuggested": t.boolean().optional(),
            "fontSizeSuggested": t.boolean().optional(),
            "linkSuggested": t.boolean().optional(),
            "baselineOffsetSuggested": t.boolean().optional(),
            "underlineSuggested": t.boolean().optional(),
            "strikethroughSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStyleSuggestionStateOut"])
    types["EmbeddedObjectBorderIn"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
            "propertyState": t.string().optional(),
            "dashStyle": t.string().optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderIn"])
    types["EmbeddedObjectBorderOut"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "propertyState": t.string().optional(),
            "dashStyle": t.string().optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderOut"])
    types["InlineObjectElementIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "inlineObjectId": t.string().optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["InlineObjectElementIn"])
    types["InlineObjectElementOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "inlineObjectId": t.string().optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
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
    types["BackgroundIn"] = t.struct(
        {"color": t.proxy(renames["OptionalColorIn"]).optional()}
    ).named(renames["BackgroundIn"])
    types["BackgroundOut"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundOut"])
    types["EmbeddedDrawingPropertiesSuggestionStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EmbeddedDrawingPropertiesSuggestionStateIn"])
    types["EmbeddedDrawingPropertiesSuggestionStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmbeddedDrawingPropertiesSuggestionStateOut"])
    types["EmbeddedObjectSuggestionStateIn"] = t.struct(
        {
            "marginLeftSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "titleSuggested": t.boolean().optional(),
            "sizeSuggestionState": t.proxy(renames["SizeSuggestionStateIn"]).optional(),
            "descriptionSuggested": t.boolean().optional(),
            "linkedContentReferenceSuggestionState": t.proxy(
                renames["LinkedContentReferenceSuggestionStateIn"]
            ).optional(),
            "imagePropertiesSuggestionState": t.proxy(
                renames["ImagePropertiesSuggestionStateIn"]
            ).optional(),
            "embeddedDrawingPropertiesSuggestionState": t.proxy(
                renames["EmbeddedDrawingPropertiesSuggestionStateIn"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "embeddedObjectBorderSuggestionState": t.proxy(
                renames["EmbeddedObjectBorderSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["EmbeddedObjectSuggestionStateIn"])
    types["EmbeddedObjectSuggestionStateOut"] = t.struct(
        {
            "marginLeftSuggested": t.boolean().optional(),
            "marginBottomSuggested": t.boolean().optional(),
            "marginRightSuggested": t.boolean().optional(),
            "titleSuggested": t.boolean().optional(),
            "sizeSuggestionState": t.proxy(
                renames["SizeSuggestionStateOut"]
            ).optional(),
            "descriptionSuggested": t.boolean().optional(),
            "linkedContentReferenceSuggestionState": t.proxy(
                renames["LinkedContentReferenceSuggestionStateOut"]
            ).optional(),
            "imagePropertiesSuggestionState": t.proxy(
                renames["ImagePropertiesSuggestionStateOut"]
            ).optional(),
            "embeddedDrawingPropertiesSuggestionState": t.proxy(
                renames["EmbeddedDrawingPropertiesSuggestionStateOut"]
            ).optional(),
            "marginTopSuggested": t.boolean().optional(),
            "embeddedObjectBorderSuggestionState": t.proxy(
                renames["EmbeddedObjectBorderSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectSuggestionStateOut"])
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
    types["InsertTableRequestIn"] = t.struct(
        {
            "columns": t.integer().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "rows": t.integer().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
        }
    ).named(renames["InsertTableRequestIn"])
    types["InsertTableRequestOut"] = t.struct(
        {
            "columns": t.integer().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "rows": t.integer().optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertTableRequestOut"])
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
    types["UpdateTableCellStyleRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeIn"]).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["UpdateTableCellStyleRequestIn"])
    types["UpdateTableCellStyleRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableCellStyleRequestOut"])
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
    types["DocumentIn"] = t.struct(
        {
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "suggestedNamedStylesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleIn"]).optional(),
            "namedRanges": t.struct({"_": t.string().optional()}).optional(),
            "namedStyles": t.proxy(renames["NamedStylesIn"]).optional(),
            "documentId": t.string().optional(),
            "body": t.proxy(renames["BodyIn"]).optional(),
            "revisionId": t.string().optional(),
            "title": t.string().optional(),
            "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
            "suggestedDocumentStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "footers": t.struct({"_": t.string().optional()}).optional(),
            "suggestionsViewMode": t.string().optional(),
            "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "footnotes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "lists": t.struct({"_": t.string().optional()}).optional(),
            "suggestedNamedStylesChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "documentStyle": t.proxy(renames["DocumentStyleOut"]).optional(),
            "namedRanges": t.struct({"_": t.string().optional()}).optional(),
            "namedStyles": t.proxy(renames["NamedStylesOut"]).optional(),
            "documentId": t.string().optional(),
            "body": t.proxy(renames["BodyOut"]).optional(),
            "revisionId": t.string().optional(),
            "title": t.string().optional(),
            "inlineObjects": t.struct({"_": t.string().optional()}).optional(),
            "suggestedDocumentStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "footers": t.struct({"_": t.string().optional()}).optional(),
            "suggestionsViewMode": t.string().optional(),
            "positionedObjects": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "footnotes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
    types["BatchUpdateDocumentRequestIn"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
        }
    ).named(renames["BatchUpdateDocumentRequestIn"])
    types["BatchUpdateDocumentRequestOut"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "requests": t.array(t.proxy(renames["RequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDocumentRequestOut"])
    types["InsertSectionBreakRequestIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationIn"]
            ).optional(),
            "sectionType": t.string().optional(),
        }
    ).named(renames["InsertSectionBreakRequestIn"])
    types["InsertSectionBreakRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]).optional(),
            "endOfSegmentLocation": t.proxy(
                renames["EndOfSegmentLocationOut"]
            ).optional(),
            "sectionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertSectionBreakRequestOut"])
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
    types["TextRunIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "content": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["TextRunIn"])
    types["TextRunOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "content": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextRunOut"])
    types["NestingLevelSuggestionStateIn"] = t.struct(
        {
            "glyphFormatSuggested": t.boolean().optional(),
            "startNumberSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateIn"]
            ).optional(),
            "glyphTypeSuggested": t.boolean().optional(),
            "bulletAlignmentSuggested": t.boolean().optional(),
            "glyphSymbolSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
        }
    ).named(renames["NestingLevelSuggestionStateIn"])
    types["NestingLevelSuggestionStateOut"] = t.struct(
        {
            "glyphFormatSuggested": t.boolean().optional(),
            "startNumberSuggested": t.boolean().optional(),
            "indentStartSuggested": t.boolean().optional(),
            "textStyleSuggestionState": t.proxy(
                renames["TextStyleSuggestionStateOut"]
            ).optional(),
            "glyphTypeSuggested": t.boolean().optional(),
            "bulletAlignmentSuggested": t.boolean().optional(),
            "glyphSymbolSuggested": t.boolean().optional(),
            "indentFirstLineSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelSuggestionStateOut"])
    types["ImagePropertiesSuggestionStateIn"] = t.struct(
        {
            "cropPropertiesSuggestionState": t.proxy(
                renames["CropPropertiesSuggestionStateIn"]
            ).optional(),
            "contentUriSuggested": t.boolean().optional(),
            "contrastSuggested": t.boolean().optional(),
            "sourceUriSuggested": t.boolean().optional(),
            "transparencySuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "brightnessSuggested": t.boolean().optional(),
        }
    ).named(renames["ImagePropertiesSuggestionStateIn"])
    types["ImagePropertiesSuggestionStateOut"] = t.struct(
        {
            "cropPropertiesSuggestionState": t.proxy(
                renames["CropPropertiesSuggestionStateOut"]
            ).optional(),
            "contentUriSuggested": t.boolean().optional(),
            "contrastSuggested": t.boolean().optional(),
            "sourceUriSuggested": t.boolean().optional(),
            "transparencySuggested": t.boolean().optional(),
            "angleSuggested": t.boolean().optional(),
            "brightnessSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesSuggestionStateOut"])
    types["SuggestedInlineObjectPropertiesIn"] = t.struct(
        {
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesIn"]
            ).optional(),
            "inlineObjectPropertiesSuggestionState": t.proxy(
                renames["InlineObjectPropertiesSuggestionStateIn"]
            ).optional(),
        }
    ).named(renames["SuggestedInlineObjectPropertiesIn"])
    types["SuggestedInlineObjectPropertiesOut"] = t.struct(
        {
            "inlineObjectProperties": t.proxy(
                renames["InlineObjectPropertiesOut"]
            ).optional(),
            "inlineObjectPropertiesSuggestionState": t.proxy(
                renames["InlineObjectPropertiesSuggestionStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestedInlineObjectPropertiesOut"])
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
    types["PositionedObjectPositioningSuggestionStateIn"] = t.struct(
        {
            "leftOffsetSuggested": t.boolean().optional(),
            "layoutSuggested": t.boolean().optional(),
            "topOffsetSuggested": t.boolean().optional(),
        }
    ).named(renames["PositionedObjectPositioningSuggestionStateIn"])
    types["PositionedObjectPositioningSuggestionStateOut"] = t.struct(
        {
            "leftOffsetSuggested": t.boolean().optional(),
            "layoutSuggested": t.boolean().optional(),
            "topOffsetSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionedObjectPositioningSuggestionStateOut"])
    types["NestingLevelIn"] = t.struct(
        {
            "glyphType": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "glyphFormat": t.string().optional(),
            "startNumber": t.integer().optional(),
            "bulletAlignment": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "glyphSymbol": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["NestingLevelIn"])
    types["NestingLevelOut"] = t.struct(
        {
            "glyphType": t.string().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "glyphFormat": t.string().optional(),
            "startNumber": t.integer().optional(),
            "bulletAlignment": t.string().optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "glyphSymbol": t.string().optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestingLevelOut"])
    types["UpdateTableRowStyleRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
            "tableStartLocation": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["UpdateTableRowStyleRequestIn"])
    types["UpdateTableRowStyleRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "rowIndices": t.array(t.integer()).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "tableStartLocation": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableRowStyleRequestOut"])
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
            "personId": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "personProperties": t.proxy(renames["PersonPropertiesOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["NamedRangeIn"] = t.struct(
        {
            "ranges": t.array(t.proxy(renames["RangeIn"])).optional(),
            "namedRangeId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["NamedRangeIn"])
    types["NamedRangeOut"] = t.struct(
        {
            "ranges": t.array(t.proxy(renames["RangeOut"])).optional(),
            "namedRangeId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedRangeOut"])
    types["MergeTableCellsRequestIn"] = t.struct(
        {"tableRange": t.proxy(renames["TableRangeIn"]).optional()}
    ).named(renames["MergeTableCellsRequestIn"])
    types["MergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeTableCellsRequestOut"])
    types["RichLinkIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["RichLinkIn"])
    types["RichLinkOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "richLinkProperties": t.proxy(renames["RichLinkPropertiesOut"]).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "richLinkId": t.string().optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichLinkOut"])
    types["CreateNamedRangeResponseIn"] = t.struct(
        {"namedRangeId": t.string().optional()}
    ).named(renames["CreateNamedRangeResponseIn"])
    types["CreateNamedRangeResponseOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNamedRangeResponseOut"])
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
    types["RequestIn"] = t.struct(
        {
            "updateTableRowStyle": t.proxy(
                renames["UpdateTableRowStyleRequestIn"]
            ).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeRequestIn"]
            ).optional(),
            "insertTable": t.proxy(renames["InsertTableRequestIn"]).optional(),
            "deleteFooter": t.proxy(renames["DeleteFooterRequestIn"]).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestIn"]
            ).optional(),
            "insertTableRow": t.proxy(renames["InsertTableRowRequestIn"]).optional(),
            "insertTableColumn": t.proxy(
                renames["InsertTableColumnRequestIn"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestIn"]).optional(),
            "updateTableCellStyle": t.proxy(
                renames["UpdateTableCellStyleRequestIn"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestIn"]).optional(),
            "insertPageBreak": t.proxy(renames["InsertPageBreakRequestIn"]).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageRequestIn"]
            ).optional(),
            "createHeader": t.proxy(renames["CreateHeaderRequestIn"]).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestIn"]
            ).optional(),
            "updateSectionStyle": t.proxy(
                renames["UpdateSectionStyleRequestIn"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestIn"]
            ).optional(),
            "replaceNamedRangeContent": t.proxy(
                renames["ReplaceNamedRangeContentRequestIn"]
            ).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestIn"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestIn"]).optional(),
            "insertSectionBreak": t.proxy(
                renames["InsertSectionBreakRequestIn"]
            ).optional(),
            "updateDocumentStyle": t.proxy(
                renames["UpdateDocumentStyleRequestIn"]
            ).optional(),
            "insertText": t.proxy(renames["InsertTextRequestIn"]).optional(),
            "deleteContentRange": t.proxy(
                renames["DeleteContentRangeRequestIn"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestIn"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteRequestIn"]).optional(),
            "createFooter": t.proxy(renames["CreateFooterRequestIn"]).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestIn"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestIn"]
            ).optional(),
            "pinTableHeaderRows": t.proxy(
                renames["PinTableHeaderRowsRequestIn"]
            ).optional(),
            "deleteHeader": t.proxy(renames["DeleteHeaderRequestIn"]).optional(),
            "deletePositionedObject": t.proxy(
                renames["DeletePositionedObjectRequestIn"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "updateTableRowStyle": t.proxy(
                renames["UpdateTableRowStyleRequestOut"]
            ).optional(),
            "createNamedRange": t.proxy(
                renames["CreateNamedRangeRequestOut"]
            ).optional(),
            "insertTable": t.proxy(renames["InsertTableRequestOut"]).optional(),
            "deleteFooter": t.proxy(renames["DeleteFooterRequestOut"]).optional(),
            "updateParagraphStyle": t.proxy(
                renames["UpdateParagraphStyleRequestOut"]
            ).optional(),
            "insertTableRow": t.proxy(renames["InsertTableRowRequestOut"]).optional(),
            "insertTableColumn": t.proxy(
                renames["InsertTableColumnRequestOut"]
            ).optional(),
            "replaceAllText": t.proxy(renames["ReplaceAllTextRequestOut"]).optional(),
            "updateTableCellStyle": t.proxy(
                renames["UpdateTableCellStyleRequestOut"]
            ).optional(),
            "updateTextStyle": t.proxy(renames["UpdateTextStyleRequestOut"]).optional(),
            "insertPageBreak": t.proxy(renames["InsertPageBreakRequestOut"]).optional(),
            "insertInlineImage": t.proxy(
                renames["InsertInlineImageRequestOut"]
            ).optional(),
            "createHeader": t.proxy(renames["CreateHeaderRequestOut"]).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "deleteTableColumn": t.proxy(
                renames["DeleteTableColumnRequestOut"]
            ).optional(),
            "updateSectionStyle": t.proxy(
                renames["UpdateSectionStyleRequestOut"]
            ).optional(),
            "unmergeTableCells": t.proxy(
                renames["UnmergeTableCellsRequestOut"]
            ).optional(),
            "replaceNamedRangeContent": t.proxy(
                renames["ReplaceNamedRangeContentRequestOut"]
            ).optional(),
            "deleteParagraphBullets": t.proxy(
                renames["DeleteParagraphBulletsRequestOut"]
            ).optional(),
            "replaceImage": t.proxy(renames["ReplaceImageRequestOut"]).optional(),
            "insertSectionBreak": t.proxy(
                renames["InsertSectionBreakRequestOut"]
            ).optional(),
            "updateDocumentStyle": t.proxy(
                renames["UpdateDocumentStyleRequestOut"]
            ).optional(),
            "insertText": t.proxy(renames["InsertTextRequestOut"]).optional(),
            "deleteContentRange": t.proxy(
                renames["DeleteContentRangeRequestOut"]
            ).optional(),
            "deleteTableRow": t.proxy(renames["DeleteTableRowRequestOut"]).optional(),
            "createFootnote": t.proxy(renames["CreateFootnoteRequestOut"]).optional(),
            "createFooter": t.proxy(renames["CreateFooterRequestOut"]).optional(),
            "mergeTableCells": t.proxy(renames["MergeTableCellsRequestOut"]).optional(),
            "updateTableColumnProperties": t.proxy(
                renames["UpdateTableColumnPropertiesRequestOut"]
            ).optional(),
            "pinTableHeaderRows": t.proxy(
                renames["PinTableHeaderRowsRequestOut"]
            ).optional(),
            "deleteHeader": t.proxy(renames["DeleteHeaderRequestOut"]).optional(),
            "deletePositionedObject": t.proxy(
                renames["DeletePositionedObjectRequestOut"]
            ).optional(),
            "createParagraphBullets": t.proxy(
                renames["CreateParagraphBulletsRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["ImagePropertiesIn"] = t.struct(
        {
            "brightness": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesIn"]).optional(),
            "sourceUri": t.string().optional(),
            "contentUri": t.string().optional(),
            "angle": t.number().optional(),
            "transparency": t.number().optional(),
            "contrast": t.number().optional(),
        }
    ).named(renames["ImagePropertiesIn"])
    types["ImagePropertiesOut"] = t.struct(
        {
            "brightness": t.number().optional(),
            "cropProperties": t.proxy(renames["CropPropertiesOut"]).optional(),
            "sourceUri": t.string().optional(),
            "contentUri": t.string().optional(),
            "angle": t.number().optional(),
            "transparency": t.number().optional(),
            "contrast": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagePropertiesOut"])
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
    types["TableRowStyleSuggestionStateIn"] = t.struct(
        {"minRowHeightSuggested": t.boolean().optional()}
    ).named(renames["TableRowStyleSuggestionStateIn"])
    types["TableRowStyleSuggestionStateOut"] = t.struct(
        {
            "minRowHeightSuggested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowStyleSuggestionStateOut"])
    types["ParagraphStyleIn"] = t.struct(
        {
            "keepWithNext": t.boolean().optional(),
            "namedStyleType": t.string().optional(),
            "avoidWidowAndOrphan": t.boolean().optional(),
            "borderLeft": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "borderTop": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "keepLinesTogether": t.boolean().optional(),
            "indentEnd": t.proxy(renames["DimensionIn"]).optional(),
            "shading": t.proxy(renames["ShadingIn"]).optional(),
            "direction": t.string().optional(),
            "pageBreakBefore": t.boolean().optional(),
            "indentFirstLine": t.proxy(renames["DimensionIn"]).optional(),
            "borderRight": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "indentStart": t.proxy(renames["DimensionIn"]).optional(),
            "tabStops": t.array(t.proxy(renames["TabStopIn"])).optional(),
            "spacingMode": t.string().optional(),
            "spaceBelow": t.proxy(renames["DimensionIn"]).optional(),
            "borderBetween": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "borderBottom": t.proxy(renames["ParagraphBorderIn"]).optional(),
            "headingId": t.string().optional(),
            "lineSpacing": t.number().optional(),
            "alignment": t.string().optional(),
            "spaceAbove": t.proxy(renames["DimensionIn"]).optional(),
        }
    ).named(renames["ParagraphStyleIn"])
    types["ParagraphStyleOut"] = t.struct(
        {
            "keepWithNext": t.boolean().optional(),
            "namedStyleType": t.string().optional(),
            "avoidWidowAndOrphan": t.boolean().optional(),
            "borderLeft": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "borderTop": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "keepLinesTogether": t.boolean().optional(),
            "indentEnd": t.proxy(renames["DimensionOut"]).optional(),
            "shading": t.proxy(renames["ShadingOut"]).optional(),
            "direction": t.string().optional(),
            "pageBreakBefore": t.boolean().optional(),
            "indentFirstLine": t.proxy(renames["DimensionOut"]).optional(),
            "borderRight": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "indentStart": t.proxy(renames["DimensionOut"]).optional(),
            "tabStops": t.array(t.proxy(renames["TabStopOut"])).optional(),
            "spacingMode": t.string().optional(),
            "spaceBelow": t.proxy(renames["DimensionOut"]).optional(),
            "borderBetween": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "borderBottom": t.proxy(renames["ParagraphBorderOut"]).optional(),
            "headingId": t.string().optional(),
            "lineSpacing": t.number().optional(),
            "alignment": t.string().optional(),
            "spaceAbove": t.proxy(renames["DimensionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphStyleOut"])
    types["ParagraphElementIn"] = t.struct(
        {
            "textRun": t.proxy(renames["TextRunIn"]).optional(),
            "horizontalRule": t.proxy(renames["HorizontalRuleIn"]).optional(),
            "autoText": t.proxy(renames["AutoTextIn"]).optional(),
            "person": t.proxy(renames["PersonIn"]).optional(),
            "endIndex": t.integer().optional(),
            "columnBreak": t.proxy(renames["ColumnBreakIn"]).optional(),
            "richLink": t.proxy(renames["RichLinkIn"]).optional(),
            "startIndex": t.integer().optional(),
            "footnoteReference": t.proxy(renames["FootnoteReferenceIn"]).optional(),
            "equation": t.proxy(renames["EquationIn"]).optional(),
            "inlineObjectElement": t.proxy(renames["InlineObjectElementIn"]).optional(),
            "pageBreak": t.proxy(renames["PageBreakIn"]).optional(),
        }
    ).named(renames["ParagraphElementIn"])
    types["ParagraphElementOut"] = t.struct(
        {
            "textRun": t.proxy(renames["TextRunOut"]).optional(),
            "horizontalRule": t.proxy(renames["HorizontalRuleOut"]).optional(),
            "autoText": t.proxy(renames["AutoTextOut"]).optional(),
            "person": t.proxy(renames["PersonOut"]).optional(),
            "endIndex": t.integer().optional(),
            "columnBreak": t.proxy(renames["ColumnBreakOut"]).optional(),
            "richLink": t.proxy(renames["RichLinkOut"]).optional(),
            "startIndex": t.integer().optional(),
            "footnoteReference": t.proxy(renames["FootnoteReferenceOut"]).optional(),
            "equation": t.proxy(renames["EquationOut"]).optional(),
            "inlineObjectElement": t.proxy(
                renames["InlineObjectElementOut"]
            ).optional(),
            "pageBreak": t.proxy(renames["PageBreakOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphElementOut"])
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
    types["UnmergeTableCellsRequestIn"] = t.struct(
        {"tableRange": t.proxy(renames["TableRangeIn"]).optional()}
    ).named(renames["UnmergeTableCellsRequestIn"])
    types["UnmergeTableCellsRequestOut"] = t.struct(
        {
            "tableRange": t.proxy(renames["TableRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeTableCellsRequestOut"])
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
    types["TableRowIn"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "startIndex": t.integer().optional(),
            "suggestedTableRowStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleIn"]).optional(),
            "tableCells": t.array(t.proxy(renames["TableCellIn"])).optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "startIndex": t.integer().optional(),
            "suggestedTableRowStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "tableRowStyle": t.proxy(renames["TableRowStyleOut"]).optional(),
            "tableCells": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["DeleteParagraphBulletsRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["DeleteParagraphBulletsRequestIn"])
    types["DeleteParagraphBulletsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteParagraphBulletsRequestOut"])
    types["PageBreakIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
        }
    ).named(renames["PageBreakIn"])
    types["PageBreakOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageBreakOut"])
    types["HorizontalRuleIn"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
        }
    ).named(renames["HorizontalRuleIn"])
    types["HorizontalRuleOut"] = t.struct(
        {
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HorizontalRuleOut"])
    types["InsertInlineImageResponseIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["InsertInlineImageResponseIn"])
    types["InsertInlineImageResponseOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertInlineImageResponseOut"])
    types["SectionStyleIn"] = t.struct(
        {
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "marginHeader": t.proxy(renames["DimensionIn"]).optional(),
            "columnProperties": t.array(
                t.proxy(renames["SectionColumnPropertiesIn"])
            ).optional(),
            "pageNumberStart": t.integer().optional(),
            "columnSeparatorStyle": t.string().optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "defaultHeaderId": t.string().optional(),
            "firstPageHeaderId": t.string().optional(),
            "contentDirection": t.string().optional(),
            "evenPageFooterId": t.string().optional(),
            "marginFooter": t.proxy(renames["DimensionIn"]).optional(),
            "evenPageHeaderId": t.string().optional(),
            "defaultFooterId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "firstPageFooterId": t.string().optional(),
            "sectionType": t.string().optional(),
        }
    ).named(renames["SectionStyleIn"])
    types["SectionStyleOut"] = t.struct(
        {
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "marginHeader": t.proxy(renames["DimensionOut"]).optional(),
            "columnProperties": t.array(
                t.proxy(renames["SectionColumnPropertiesOut"])
            ).optional(),
            "pageNumberStart": t.integer().optional(),
            "columnSeparatorStyle": t.string().optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "defaultHeaderId": t.string().optional(),
            "firstPageHeaderId": t.string().optional(),
            "contentDirection": t.string().optional(),
            "evenPageFooterId": t.string().optional(),
            "marginFooter": t.proxy(renames["DimensionOut"]).optional(),
            "evenPageHeaderId": t.string().optional(),
            "defaultFooterId": t.string().optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "firstPageFooterId": t.string().optional(),
            "sectionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionStyleOut"])
    types["StructuralElementIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "table": t.proxy(renames["TableIn"]).optional(),
            "tableOfContents": t.proxy(renames["TableOfContentsIn"]).optional(),
            "paragraph": t.proxy(renames["ParagraphIn"]).optional(),
            "endIndex": t.integer().optional(),
            "sectionBreak": t.proxy(renames["SectionBreakIn"]).optional(),
        }
    ).named(renames["StructuralElementIn"])
    types["StructuralElementOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "table": t.proxy(renames["TableOut"]).optional(),
            "tableOfContents": t.proxy(renames["TableOfContentsOut"]).optional(),
            "paragraph": t.proxy(renames["ParagraphOut"]).optional(),
            "endIndex": t.integer().optional(),
            "sectionBreak": t.proxy(renames["SectionBreakOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuralElementOut"])
    types["TableCellIn"] = t.struct(
        {
            "tableCellStyle": t.proxy(renames["TableCellStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "endIndex": t.integer().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementIn"])).optional(),
            "suggestedTableCellStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "tableCellStyle": t.proxy(renames["TableCellStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "endIndex": t.integer().optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "suggestedTableCellStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
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
    types["DeleteHeaderRequestIn"] = t.struct(
        {"headerId": t.string().optional()}
    ).named(renames["DeleteHeaderRequestIn"])
    types["DeleteHeaderRequestOut"] = t.struct(
        {
            "headerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteHeaderRequestOut"])
    types["DeleteTableRowRequestIn"] = t.struct(
        {"tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional()}
    ).named(renames["DeleteTableRowRequestIn"])
    types["DeleteTableRowRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableRowRequestOut"])
    types["ColumnBreakIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
        }
    ).named(renames["ColumnBreakIn"])
    types["ColumnBreakOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "suggestedInsertionIds": t.array(t.string()).optional(),
            "suggestedTextStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "suggestedDeletionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnBreakOut"])
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
    types["EmbeddedDrawingPropertiesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EmbeddedDrawingPropertiesIn"]
    )
    types["EmbeddedDrawingPropertiesOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmbeddedDrawingPropertiesOut"])
    types["TableCellStyleIn"] = t.struct(
        {
            "paddingRight": t.proxy(renames["DimensionIn"]).optional(),
            "columnSpan": t.integer().optional(),
            "contentAlignment": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorIn"]).optional(),
            "borderTop": t.proxy(renames["TableCellBorderIn"]).optional(),
            "borderLeft": t.proxy(renames["TableCellBorderIn"]).optional(),
            "paddingBottom": t.proxy(renames["DimensionIn"]).optional(),
            "paddingTop": t.proxy(renames["DimensionIn"]).optional(),
            "rowSpan": t.integer().optional(),
            "paddingLeft": t.proxy(renames["DimensionIn"]).optional(),
            "borderRight": t.proxy(renames["TableCellBorderIn"]).optional(),
            "borderBottom": t.proxy(renames["TableCellBorderIn"]).optional(),
        }
    ).named(renames["TableCellStyleIn"])
    types["TableCellStyleOut"] = t.struct(
        {
            "paddingRight": t.proxy(renames["DimensionOut"]).optional(),
            "columnSpan": t.integer().optional(),
            "contentAlignment": t.string().optional(),
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "borderTop": t.proxy(renames["TableCellBorderOut"]).optional(),
            "borderLeft": t.proxy(renames["TableCellBorderOut"]).optional(),
            "paddingBottom": t.proxy(renames["DimensionOut"]).optional(),
            "paddingTop": t.proxy(renames["DimensionOut"]).optional(),
            "rowSpan": t.integer().optional(),
            "paddingLeft": t.proxy(renames["DimensionOut"]).optional(),
            "borderRight": t.proxy(renames["TableCellBorderOut"]).optional(),
            "borderBottom": t.proxy(renames["TableCellBorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellStyleOut"])
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
    types["ColorIn"] = t.struct(
        {"rgbColor": t.proxy(renames["RgbColorIn"]).optional()}
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "rgbColor": t.proxy(renames["RgbColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["EndOfSegmentLocationIn"] = t.struct(
        {"segmentId": t.string().optional()}
    ).named(renames["EndOfSegmentLocationIn"])
    types["EndOfSegmentLocationOut"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndOfSegmentLocationOut"])
    types["BodyIn"] = t.struct(
        {"content": t.array(t.proxy(renames["StructuralElementIn"])).optional()}
    ).named(renames["BodyIn"])
    types["BodyOut"] = t.struct(
        {
            "content": t.array(t.proxy(renames["StructuralElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BodyOut"])
    types["DeleteFooterRequestIn"] = t.struct(
        {"footerId": t.string().optional()}
    ).named(renames["DeleteFooterRequestIn"])
    types["DeleteFooterRequestOut"] = t.struct(
        {
            "footerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFooterRequestOut"])
    types["DeletePositionedObjectRequestIn"] = t.struct(
        {"objectId": t.string().optional()}
    ).named(renames["DeletePositionedObjectRequestIn"])
    types["DeletePositionedObjectRequestOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeletePositionedObjectRequestOut"])
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
    types["DeleteContentRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["RangeIn"]).optional()}
    ).named(renames["DeleteContentRangeRequestIn"])
    types["DeleteContentRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteContentRangeRequestOut"])
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
    types["DocumentStyleIn"] = t.struct(
        {
            "defaultHeaderId": t.string().optional(),
            "background": t.proxy(renames["BackgroundIn"]).optional(),
            "marginBottom": t.proxy(renames["DimensionIn"]).optional(),
            "useCustomHeaderFooterMargins": t.boolean().optional(),
            "marginFooter": t.proxy(renames["DimensionIn"]).optional(),
            "marginHeader": t.proxy(renames["DimensionIn"]).optional(),
            "pageNumberStart": t.integer().optional(),
            "evenPageHeaderId": t.string().optional(),
            "marginRight": t.proxy(renames["DimensionIn"]).optional(),
            "pageSize": t.proxy(renames["SizeIn"]).optional(),
            "defaultFooterId": t.string().optional(),
            "firstPageFooterId": t.string().optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginLeft": t.proxy(renames["DimensionIn"]).optional(),
            "marginTop": t.proxy(renames["DimensionIn"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "useEvenPageHeaderFooter": t.boolean().optional(),
            "firstPageHeaderId": t.string().optional(),
        }
    ).named(renames["DocumentStyleIn"])
    types["DocumentStyleOut"] = t.struct(
        {
            "defaultHeaderId": t.string().optional(),
            "background": t.proxy(renames["BackgroundOut"]).optional(),
            "marginBottom": t.proxy(renames["DimensionOut"]).optional(),
            "useCustomHeaderFooterMargins": t.boolean().optional(),
            "marginFooter": t.proxy(renames["DimensionOut"]).optional(),
            "marginHeader": t.proxy(renames["DimensionOut"]).optional(),
            "pageNumberStart": t.integer().optional(),
            "evenPageHeaderId": t.string().optional(),
            "marginRight": t.proxy(renames["DimensionOut"]).optional(),
            "pageSize": t.proxy(renames["SizeOut"]).optional(),
            "defaultFooterId": t.string().optional(),
            "firstPageFooterId": t.string().optional(),
            "useFirstPageHeaderFooter": t.boolean().optional(),
            "marginLeft": t.proxy(renames["DimensionOut"]).optional(),
            "marginTop": t.proxy(renames["DimensionOut"]).optional(),
            "evenPageFooterId": t.string().optional(),
            "useEvenPageHeaderFooter": t.boolean().optional(),
            "firstPageHeaderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentStyleOut"])
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
    types["CreateFootnoteResponseIn"] = t.struct(
        {"footnoteId": t.string().optional()}
    ).named(renames["CreateFootnoteResponseIn"])
    types["CreateFootnoteResponseOut"] = t.struct(
        {
            "footnoteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFootnoteResponseOut"])
    types["UpdateTextStyleRequestIn"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleIn"]).optional(),
            "range": t.proxy(renames["RangeIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateTextStyleRequestIn"])
    types["UpdateTextStyleRequestOut"] = t.struct(
        {
            "textStyle": t.proxy(renames["TextStyleOut"]).optional(),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTextStyleRequestOut"])
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
    types["UpdateSectionStyleRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["RangeIn"]).optional(),
            "sectionStyle": t.proxy(renames["SectionStyleIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateSectionStyleRequestIn"])
    types["UpdateSectionStyleRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "sectionStyle": t.proxy(renames["SectionStyleOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSectionStyleRequestOut"])
    types["CropPropertiesIn"] = t.struct(
        {
            "offsetLeft": t.number().optional(),
            "angle": t.number().optional(),
            "offsetRight": t.number().optional(),
            "offsetBottom": t.number().optional(),
            "offsetTop": t.number().optional(),
        }
    ).named(renames["CropPropertiesIn"])
    types["CropPropertiesOut"] = t.struct(
        {
            "offsetLeft": t.number().optional(),
            "angle": t.number().optional(),
            "offsetRight": t.number().optional(),
            "offsetBottom": t.number().optional(),
            "offsetTop": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropPropertiesOut"])
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
    types["DeleteTableColumnRequestIn"] = t.struct(
        {"tableCellLocation": t.proxy(renames["TableCellLocationIn"]).optional()}
    ).named(renames["DeleteTableColumnRequestIn"])
    types["DeleteTableColumnRequestOut"] = t.struct(
        {
            "tableCellLocation": t.proxy(renames["TableCellLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteTableColumnRequestOut"])
    types["TableCellBorderIn"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorIn"]).optional(),
            "width": t.proxy(renames["DimensionIn"]).optional(),
            "dashStyle": t.string().optional(),
        }
    ).named(renames["TableCellBorderIn"])
    types["TableCellBorderOut"] = t.struct(
        {
            "color": t.proxy(renames["OptionalColorOut"]).optional(),
            "width": t.proxy(renames["DimensionOut"]).optional(),
            "dashStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellBorderOut"])
    types["ShadingIn"] = t.struct(
        {"backgroundColor": t.proxy(renames["OptionalColorIn"]).optional()}
    ).named(renames["ShadingIn"])
    types["ShadingOut"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["OptionalColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShadingOut"])
    types["ReplaceAllTextResponseIn"] = t.struct(
        {"occurrencesChanged": t.integer().optional()}
    ).named(renames["ReplaceAllTextResponseIn"])
    types["ReplaceAllTextResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAllTextResponseOut"])
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
    types["ParagraphIn"] = t.struct(
        {
            "suggestedBulletChanges": t.struct({"_": t.string().optional()}).optional(),
            "bullet": t.proxy(renames["BulletIn"]).optional(),
            "elements": t.array(t.proxy(renames["ParagraphElementIn"])).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleIn"]).optional(),
            "suggestedParagraphStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "positionedObjectIds": t.array(t.string()).optional(),
            "suggestedPositionedObjectIds": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["ParagraphIn"])
    types["ParagraphOut"] = t.struct(
        {
            "suggestedBulletChanges": t.struct({"_": t.string().optional()}).optional(),
            "bullet": t.proxy(renames["BulletOut"]).optional(),
            "elements": t.array(t.proxy(renames["ParagraphElementOut"])).optional(),
            "paragraphStyle": t.proxy(renames["ParagraphStyleOut"]).optional(),
            "suggestedParagraphStyleChanges": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "positionedObjectIds": t.array(t.string()).optional(),
            "suggestedPositionedObjectIds": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParagraphOut"])

    functions = {}
    functions["documentsCreate"] = docs.get(
        "v1/documents/{documentId}",
        t.struct(
            {
                "documentId": t.string().optional(),
                "suggestionsViewMode": t.string().optional(),
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
                "documentId": t.string().optional(),
                "suggestionsViewMode": t.string().optional(),
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
                "documentId": t.string().optional(),
                "suggestionsViewMode": t.string().optional(),
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
