from typegraph import effects
from typegraph import t
from typegraph.importers.base.importer import Import
from typegraph import TypeGraph
from typegraph.runtimes.http import HTTPRuntime


def import_sheets() -> Import:
    sheets = HTTPRuntime("https://sheets.googleapis.com/")

    renames = {
        "ErrorResponse": "_sheets_1_ErrorResponse",
        "InsertRangeRequestIn": "_sheets_2_InsertRangeRequestIn",
        "InsertRangeRequestOut": "_sheets_3_InsertRangeRequestOut",
        "ClearValuesRequestIn": "_sheets_4_ClearValuesRequestIn",
        "ClearValuesRequestOut": "_sheets_5_ClearValuesRequestOut",
        "SearchDeveloperMetadataResponseIn": "_sheets_6_SearchDeveloperMetadataResponseIn",
        "SearchDeveloperMetadataResponseOut": "_sheets_7_SearchDeveloperMetadataResponseOut",
        "AddProtectedRangeResponseIn": "_sheets_8_AddProtectedRangeResponseIn",
        "AddProtectedRangeResponseOut": "_sheets_9_AddProtectedRangeResponseOut",
        "BigQueryDataSourceSpecIn": "_sheets_10_BigQueryDataSourceSpecIn",
        "BigQueryDataSourceSpecOut": "_sheets_11_BigQueryDataSourceSpecOut",
        "DuplicateFilterViewResponseIn": "_sheets_12_DuplicateFilterViewResponseIn",
        "DuplicateFilterViewResponseOut": "_sheets_13_DuplicateFilterViewResponseOut",
        "DeleteConditionalFormatRuleRequestIn": "_sheets_14_DeleteConditionalFormatRuleRequestIn",
        "DeleteConditionalFormatRuleRequestOut": "_sheets_15_DeleteConditionalFormatRuleRequestOut",
        "DataSourceObjectReferencesIn": "_sheets_16_DataSourceObjectReferencesIn",
        "DataSourceObjectReferencesOut": "_sheets_17_DataSourceObjectReferencesOut",
        "BasicFilterIn": "_sheets_18_BasicFilterIn",
        "BasicFilterOut": "_sheets_19_BasicFilterOut",
        "DeleteDuplicatesResponseIn": "_sheets_20_DeleteDuplicatesResponseIn",
        "DeleteDuplicatesResponseOut": "_sheets_21_DeleteDuplicatesResponseOut",
        "AddChartResponseIn": "_sheets_22_AddChartResponseIn",
        "AddChartResponseOut": "_sheets_23_AddChartResponseOut",
        "NumberFormatIn": "_sheets_24_NumberFormatIn",
        "NumberFormatOut": "_sheets_25_NumberFormatOut",
        "BatchUpdateSpreadsheetRequestIn": "_sheets_26_BatchUpdateSpreadsheetRequestIn",
        "BatchUpdateSpreadsheetRequestOut": "_sheets_27_BatchUpdateSpreadsheetRequestOut",
        "TrimWhitespaceRequestIn": "_sheets_28_TrimWhitespaceRequestIn",
        "TrimWhitespaceRequestOut": "_sheets_29_TrimWhitespaceRequestOut",
        "GridPropertiesIn": "_sheets_30_GridPropertiesIn",
        "GridPropertiesOut": "_sheets_31_GridPropertiesOut",
        "BatchClearValuesRequestIn": "_sheets_32_BatchClearValuesRequestIn",
        "BatchClearValuesRequestOut": "_sheets_33_BatchClearValuesRequestOut",
        "TextFormatIn": "_sheets_34_TextFormatIn",
        "TextFormatOut": "_sheets_35_TextFormatOut",
        "BatchUpdateSpreadsheetResponseIn": "_sheets_36_BatchUpdateSpreadsheetResponseIn",
        "BatchUpdateSpreadsheetResponseOut": "_sheets_37_BatchUpdateSpreadsheetResponseOut",
        "GradientRuleIn": "_sheets_38_GradientRuleIn",
        "GradientRuleOut": "_sheets_39_GradientRuleOut",
        "CreateDeveloperMetadataResponseIn": "_sheets_40_CreateDeveloperMetadataResponseIn",
        "CreateDeveloperMetadataResponseOut": "_sheets_41_CreateDeveloperMetadataResponseOut",
        "DeleteDeveloperMetadataRequestIn": "_sheets_42_DeleteDeveloperMetadataRequestIn",
        "DeleteDeveloperMetadataRequestOut": "_sheets_43_DeleteDeveloperMetadataRequestOut",
        "UpdateEmbeddedObjectPositionRequestIn": "_sheets_44_UpdateEmbeddedObjectPositionRequestIn",
        "UpdateEmbeddedObjectPositionRequestOut": "_sheets_45_UpdateEmbeddedObjectPositionRequestOut",
        "SlicerSpecIn": "_sheets_46_SlicerSpecIn",
        "SlicerSpecOut": "_sheets_47_SlicerSpecOut",
        "DataSourceSpecIn": "_sheets_48_DataSourceSpecIn",
        "DataSourceSpecOut": "_sheets_49_DataSourceSpecOut",
        "RepeatCellRequestIn": "_sheets_50_RepeatCellRequestIn",
        "RepeatCellRequestOut": "_sheets_51_RepeatCellRequestOut",
        "SpreadsheetPropertiesIn": "_sheets_52_SpreadsheetPropertiesIn",
        "SpreadsheetPropertiesOut": "_sheets_53_SpreadsheetPropertiesOut",
        "PivotGroupRuleIn": "_sheets_54_PivotGroupRuleIn",
        "PivotGroupRuleOut": "_sheets_55_PivotGroupRuleOut",
        "UpdateDataSourceRequestIn": "_sheets_56_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_sheets_57_UpdateDataSourceRequestOut",
        "DeleteFilterViewRequestIn": "_sheets_58_DeleteFilterViewRequestIn",
        "DeleteFilterViewRequestOut": "_sheets_59_DeleteFilterViewRequestOut",
        "MergeCellsRequestIn": "_sheets_60_MergeCellsRequestIn",
        "MergeCellsRequestOut": "_sheets_61_MergeCellsRequestOut",
        "DeleteDuplicatesRequestIn": "_sheets_62_DeleteDuplicatesRequestIn",
        "DeleteDuplicatesRequestOut": "_sheets_63_DeleteDuplicatesRequestOut",
        "DataSourceSheetPropertiesIn": "_sheets_64_DataSourceSheetPropertiesIn",
        "DataSourceSheetPropertiesOut": "_sheets_65_DataSourceSheetPropertiesOut",
        "RefreshDataSourceResponseIn": "_sheets_66_RefreshDataSourceResponseIn",
        "RefreshDataSourceResponseOut": "_sheets_67_RefreshDataSourceResponseOut",
        "DataSourceColumnReferenceIn": "_sheets_68_DataSourceColumnReferenceIn",
        "DataSourceColumnReferenceOut": "_sheets_69_DataSourceColumnReferenceOut",
        "MatchedValueRangeIn": "_sheets_70_MatchedValueRangeIn",
        "MatchedValueRangeOut": "_sheets_71_MatchedValueRangeOut",
        "BasicChartSpecIn": "_sheets_72_BasicChartSpecIn",
        "BasicChartSpecOut": "_sheets_73_BasicChartSpecOut",
        "BigQueryQuerySpecIn": "_sheets_74_BigQueryQuerySpecIn",
        "BigQueryQuerySpecOut": "_sheets_75_BigQueryQuerySpecOut",
        "UpdateEmbeddedObjectPositionResponseIn": "_sheets_76_UpdateEmbeddedObjectPositionResponseIn",
        "UpdateEmbeddedObjectPositionResponseOut": "_sheets_77_UpdateEmbeddedObjectPositionResponseOut",
        "UpdateChartSpecRequestIn": "_sheets_78_UpdateChartSpecRequestIn",
        "UpdateChartSpecRequestOut": "_sheets_79_UpdateChartSpecRequestOut",
        "UpdateBandingRequestIn": "_sheets_80_UpdateBandingRequestIn",
        "UpdateBandingRequestOut": "_sheets_81_UpdateBandingRequestOut",
        "ColorStyleIn": "_sheets_82_ColorStyleIn",
        "ColorStyleOut": "_sheets_83_ColorStyleOut",
        "FindReplaceResponseIn": "_sheets_84_FindReplaceResponseIn",
        "FindReplaceResponseOut": "_sheets_85_FindReplaceResponseOut",
        "AddProtectedRangeRequestIn": "_sheets_86_AddProtectedRangeRequestIn",
        "AddProtectedRangeRequestOut": "_sheets_87_AddProtectedRangeRequestOut",
        "ErrorValueIn": "_sheets_88_ErrorValueIn",
        "ErrorValueOut": "_sheets_89_ErrorValueOut",
        "AddSlicerRequestIn": "_sheets_90_AddSlicerRequestIn",
        "AddSlicerRequestOut": "_sheets_91_AddSlicerRequestOut",
        "OverlayPositionIn": "_sheets_92_OverlayPositionIn",
        "OverlayPositionOut": "_sheets_93_OverlayPositionOut",
        "InterpolationPointIn": "_sheets_94_InterpolationPointIn",
        "InterpolationPointOut": "_sheets_95_InterpolationPointOut",
        "ProtectedRangeIn": "_sheets_96_ProtectedRangeIn",
        "ProtectedRangeOut": "_sheets_97_ProtectedRangeOut",
        "EmbeddedObjectPositionIn": "_sheets_98_EmbeddedObjectPositionIn",
        "EmbeddedObjectPositionOut": "_sheets_99_EmbeddedObjectPositionOut",
        "PivotGroupValueMetadataIn": "_sheets_100_PivotGroupValueMetadataIn",
        "PivotGroupValueMetadataOut": "_sheets_101_PivotGroupValueMetadataOut",
        "DeleteDataSourceRequestIn": "_sheets_102_DeleteDataSourceRequestIn",
        "DeleteDataSourceRequestOut": "_sheets_103_DeleteDataSourceRequestOut",
        "TextToColumnsRequestIn": "_sheets_104_TextToColumnsRequestIn",
        "TextToColumnsRequestOut": "_sheets_105_TextToColumnsRequestOut",
        "PivotFilterCriteriaIn": "_sheets_106_PivotFilterCriteriaIn",
        "PivotFilterCriteriaOut": "_sheets_107_PivotFilterCriteriaOut",
        "ChartCustomNumberFormatOptionsIn": "_sheets_108_ChartCustomNumberFormatOptionsIn",
        "ChartCustomNumberFormatOptionsOut": "_sheets_109_ChartCustomNumberFormatOptionsOut",
        "BasicChartSeriesIn": "_sheets_110_BasicChartSeriesIn",
        "BasicChartSeriesOut": "_sheets_111_BasicChartSeriesOut",
        "IterativeCalculationSettingsIn": "_sheets_112_IterativeCalculationSettingsIn",
        "IterativeCalculationSettingsOut": "_sheets_113_IterativeCalculationSettingsOut",
        "ColorIn": "_sheets_114_ColorIn",
        "ColorOut": "_sheets_115_ColorOut",
        "DataSourceTableIn": "_sheets_116_DataSourceTableIn",
        "DataSourceTableOut": "_sheets_117_DataSourceTableOut",
        "LineStyleIn": "_sheets_118_LineStyleIn",
        "LineStyleOut": "_sheets_119_LineStyleOut",
        "BaselineValueFormatIn": "_sheets_120_BaselineValueFormatIn",
        "BaselineValueFormatOut": "_sheets_121_BaselineValueFormatOut",
        "DuplicateSheetResponseIn": "_sheets_122_DuplicateSheetResponseIn",
        "DuplicateSheetResponseOut": "_sheets_123_DuplicateSheetResponseOut",
        "UpdateSpreadsheetPropertiesRequestIn": "_sheets_124_UpdateSpreadsheetPropertiesRequestIn",
        "UpdateSpreadsheetPropertiesRequestOut": "_sheets_125_UpdateSpreadsheetPropertiesRequestOut",
        "UpdateConditionalFormatRuleResponseIn": "_sheets_126_UpdateConditionalFormatRuleResponseIn",
        "UpdateConditionalFormatRuleResponseOut": "_sheets_127_UpdateConditionalFormatRuleResponseOut",
        "PointStyleIn": "_sheets_128_PointStyleIn",
        "PointStyleOut": "_sheets_129_PointStyleOut",
        "ChartDataIn": "_sheets_130_ChartDataIn",
        "ChartDataOut": "_sheets_131_ChartDataOut",
        "DataSourceColumnIn": "_sheets_132_DataSourceColumnIn",
        "DataSourceColumnOut": "_sheets_133_DataSourceColumnOut",
        "AddFilterViewResponseIn": "_sheets_134_AddFilterViewResponseIn",
        "AddFilterViewResponseOut": "_sheets_135_AddFilterViewResponseOut",
        "FilterCriteriaIn": "_sheets_136_FilterCriteriaIn",
        "FilterCriteriaOut": "_sheets_137_FilterCriteriaOut",
        "ChartAxisViewWindowOptionsIn": "_sheets_138_ChartAxisViewWindowOptionsIn",
        "ChartAxisViewWindowOptionsOut": "_sheets_139_ChartAxisViewWindowOptionsOut",
        "ClearBasicFilterRequestIn": "_sheets_140_ClearBasicFilterRequestIn",
        "ClearBasicFilterRequestOut": "_sheets_141_ClearBasicFilterRequestOut",
        "HistogramSeriesIn": "_sheets_142_HistogramSeriesIn",
        "HistogramSeriesOut": "_sheets_143_HistogramSeriesOut",
        "DataSourceParameterIn": "_sheets_144_DataSourceParameterIn",
        "DataSourceParameterOut": "_sheets_145_DataSourceParameterOut",
        "BatchGetValuesByDataFilterRequestIn": "_sheets_146_BatchGetValuesByDataFilterRequestIn",
        "BatchGetValuesByDataFilterRequestOut": "_sheets_147_BatchGetValuesByDataFilterRequestOut",
        "CutPasteRequestIn": "_sheets_148_CutPasteRequestIn",
        "CutPasteRequestOut": "_sheets_149_CutPasteRequestOut",
        "DataSourceRefreshMonthlyScheduleIn": "_sheets_150_DataSourceRefreshMonthlyScheduleIn",
        "DataSourceRefreshMonthlyScheduleOut": "_sheets_151_DataSourceRefreshMonthlyScheduleOut",
        "UpdateNamedRangeRequestIn": "_sheets_152_UpdateNamedRangeRequestIn",
        "UpdateNamedRangeRequestOut": "_sheets_153_UpdateNamedRangeRequestOut",
        "BubbleChartSpecIn": "_sheets_154_BubbleChartSpecIn",
        "BubbleChartSpecOut": "_sheets_155_BubbleChartSpecOut",
        "PivotGroupLimitIn": "_sheets_156_PivotGroupLimitIn",
        "PivotGroupLimitOut": "_sheets_157_PivotGroupLimitOut",
        "CopyPasteRequestIn": "_sheets_158_CopyPasteRequestIn",
        "CopyPasteRequestOut": "_sheets_159_CopyPasteRequestOut",
        "TextFormatRunIn": "_sheets_160_TextFormatRunIn",
        "TextFormatRunOut": "_sheets_161_TextFormatRunOut",
        "FilterViewIn": "_sheets_162_FilterViewIn",
        "FilterViewOut": "_sheets_163_FilterViewOut",
        "UpdateFilterViewRequestIn": "_sheets_164_UpdateFilterViewRequestIn",
        "UpdateFilterViewRequestOut": "_sheets_165_UpdateFilterViewRequestOut",
        "BorderIn": "_sheets_166_BorderIn",
        "BorderOut": "_sheets_167_BorderOut",
        "HistogramChartSpecIn": "_sheets_168_HistogramChartSpecIn",
        "HistogramChartSpecOut": "_sheets_169_HistogramChartSpecOut",
        "AddSheetResponseIn": "_sheets_170_AddSheetResponseIn",
        "AddSheetResponseOut": "_sheets_171_AddSheetResponseOut",
        "PivotFilterSpecIn": "_sheets_172_PivotFilterSpecIn",
        "PivotFilterSpecOut": "_sheets_173_PivotFilterSpecOut",
        "CellDataIn": "_sheets_174_CellDataIn",
        "CellDataOut": "_sheets_175_CellDataOut",
        "DataFilterValueRangeIn": "_sheets_176_DataFilterValueRangeIn",
        "DataFilterValueRangeOut": "_sheets_177_DataFilterValueRangeOut",
        "DeleteConditionalFormatRuleResponseIn": "_sheets_178_DeleteConditionalFormatRuleResponseIn",
        "DeleteConditionalFormatRuleResponseOut": "_sheets_179_DeleteConditionalFormatRuleResponseOut",
        "BatchUpdateValuesByDataFilterRequestIn": "_sheets_180_BatchUpdateValuesByDataFilterRequestIn",
        "BatchUpdateValuesByDataFilterRequestOut": "_sheets_181_BatchUpdateValuesByDataFilterRequestOut",
        "PaddingIn": "_sheets_182_PaddingIn",
        "PaddingOut": "_sheets_183_PaddingOut",
        "SheetPropertiesIn": "_sheets_184_SheetPropertiesIn",
        "SheetPropertiesOut": "_sheets_185_SheetPropertiesOut",
        "AppendValuesResponseIn": "_sheets_186_AppendValuesResponseIn",
        "AppendValuesResponseOut": "_sheets_187_AppendValuesResponseOut",
        "DuplicateSheetRequestIn": "_sheets_188_DuplicateSheetRequestIn",
        "DuplicateSheetRequestOut": "_sheets_189_DuplicateSheetRequestOut",
        "BatchUpdateValuesByDataFilterResponseIn": "_sheets_190_BatchUpdateValuesByDataFilterResponseIn",
        "BatchUpdateValuesByDataFilterResponseOut": "_sheets_191_BatchUpdateValuesByDataFilterResponseOut",
        "WaterfallChartDomainIn": "_sheets_192_WaterfallChartDomainIn",
        "WaterfallChartDomainOut": "_sheets_193_WaterfallChartDomainOut",
        "DataSourceRefreshScheduleIn": "_sheets_194_DataSourceRefreshScheduleIn",
        "DataSourceRefreshScheduleOut": "_sheets_195_DataSourceRefreshScheduleOut",
        "UpdateDeveloperMetadataResponseIn": "_sheets_196_UpdateDeveloperMetadataResponseIn",
        "UpdateDeveloperMetadataResponseOut": "_sheets_197_UpdateDeveloperMetadataResponseOut",
        "AddBandingResponseIn": "_sheets_198_AddBandingResponseIn",
        "AddBandingResponseOut": "_sheets_199_AddBandingResponseOut",
        "CopySheetToAnotherSpreadsheetRequestIn": "_sheets_200_CopySheetToAnotherSpreadsheetRequestIn",
        "CopySheetToAnotherSpreadsheetRequestOut": "_sheets_201_CopySheetToAnotherSpreadsheetRequestOut",
        "EditorsIn": "_sheets_202_EditorsIn",
        "EditorsOut": "_sheets_203_EditorsOut",
        "TimeOfDayIn": "_sheets_204_TimeOfDayIn",
        "TimeOfDayOut": "_sheets_205_TimeOfDayOut",
        "BatchGetValuesByDataFilterResponseIn": "_sheets_206_BatchGetValuesByDataFilterResponseIn",
        "BatchGetValuesByDataFilterResponseOut": "_sheets_207_BatchGetValuesByDataFilterResponseOut",
        "ChartSourceRangeIn": "_sheets_208_ChartSourceRangeIn",
        "ChartSourceRangeOut": "_sheets_209_ChartSourceRangeOut",
        "UpdateConditionalFormatRuleRequestIn": "_sheets_210_UpdateConditionalFormatRuleRequestIn",
        "UpdateConditionalFormatRuleRequestOut": "_sheets_211_UpdateConditionalFormatRuleRequestOut",
        "CandlestickDomainIn": "_sheets_212_CandlestickDomainIn",
        "CandlestickDomainOut": "_sheets_213_CandlestickDomainOut",
        "ThemeColorPairIn": "_sheets_214_ThemeColorPairIn",
        "ThemeColorPairOut": "_sheets_215_ThemeColorPairOut",
        "RandomizeRangeRequestIn": "_sheets_216_RandomizeRangeRequestIn",
        "RandomizeRangeRequestOut": "_sheets_217_RandomizeRangeRequestOut",
        "BatchGetValuesResponseIn": "_sheets_218_BatchGetValuesResponseIn",
        "BatchGetValuesResponseOut": "_sheets_219_BatchGetValuesResponseOut",
        "AddDataSourceResponseIn": "_sheets_220_AddDataSourceResponseIn",
        "AddDataSourceResponseOut": "_sheets_221_AddDataSourceResponseOut",
        "DimensionPropertiesIn": "_sheets_222_DimensionPropertiesIn",
        "DimensionPropertiesOut": "_sheets_223_DimensionPropertiesOut",
        "BatchUpdateValuesResponseIn": "_sheets_224_BatchUpdateValuesResponseIn",
        "BatchUpdateValuesResponseOut": "_sheets_225_BatchUpdateValuesResponseOut",
        "HistogramRuleIn": "_sheets_226_HistogramRuleIn",
        "HistogramRuleOut": "_sheets_227_HistogramRuleOut",
        "TrimWhitespaceResponseIn": "_sheets_228_TrimWhitespaceResponseIn",
        "TrimWhitespaceResponseOut": "_sheets_229_TrimWhitespaceResponseOut",
        "ValueRangeIn": "_sheets_230_ValueRangeIn",
        "ValueRangeOut": "_sheets_231_ValueRangeOut",
        "PasteDataRequestIn": "_sheets_232_PasteDataRequestIn",
        "PasteDataRequestOut": "_sheets_233_PasteDataRequestOut",
        "UpdateDimensionPropertiesRequestIn": "_sheets_234_UpdateDimensionPropertiesRequestIn",
        "UpdateDimensionPropertiesRequestOut": "_sheets_235_UpdateDimensionPropertiesRequestOut",
        "DataExecutionStatusIn": "_sheets_236_DataExecutionStatusIn",
        "DataExecutionStatusOut": "_sheets_237_DataExecutionStatusOut",
        "ChartDateTimeRuleIn": "_sheets_238_ChartDateTimeRuleIn",
        "ChartDateTimeRuleOut": "_sheets_239_ChartDateTimeRuleOut",
        "BordersIn": "_sheets_240_BordersIn",
        "BordersOut": "_sheets_241_BordersOut",
        "KeyValueFormatIn": "_sheets_242_KeyValueFormatIn",
        "KeyValueFormatOut": "_sheets_243_KeyValueFormatOut",
        "ManualRuleIn": "_sheets_244_ManualRuleIn",
        "ManualRuleOut": "_sheets_245_ManualRuleOut",
        "SpreadsheetIn": "_sheets_246_SpreadsheetIn",
        "SpreadsheetOut": "_sheets_247_SpreadsheetOut",
        "RequestIn": "_sheets_248_RequestIn",
        "RequestOut": "_sheets_249_RequestOut",
        "AddDimensionGroupResponseIn": "_sheets_250_AddDimensionGroupResponseIn",
        "AddDimensionGroupResponseOut": "_sheets_251_AddDimensionGroupResponseOut",
        "NamedRangeIn": "_sheets_252_NamedRangeIn",
        "NamedRangeOut": "_sheets_253_NamedRangeOut",
        "DataSourceFormulaIn": "_sheets_254_DataSourceFormulaIn",
        "DataSourceFormulaOut": "_sheets_255_DataSourceFormulaOut",
        "AddFilterViewRequestIn": "_sheets_256_AddFilterViewRequestIn",
        "AddFilterViewRequestOut": "_sheets_257_AddFilterViewRequestOut",
        "DataLabelIn": "_sheets_258_DataLabelIn",
        "DataLabelOut": "_sheets_259_DataLabelOut",
        "UpdateSlicerSpecRequestIn": "_sheets_260_UpdateSlicerSpecRequestIn",
        "UpdateSlicerSpecRequestOut": "_sheets_261_UpdateSlicerSpecRequestOut",
        "UpdateValuesResponseIn": "_sheets_262_UpdateValuesResponseIn",
        "UpdateValuesResponseOut": "_sheets_263_UpdateValuesResponseOut",
        "TreemapChartSpecIn": "_sheets_264_TreemapChartSpecIn",
        "TreemapChartSpecOut": "_sheets_265_TreemapChartSpecOut",
        "UpdateProtectedRangeRequestIn": "_sheets_266_UpdateProtectedRangeRequestIn",
        "UpdateProtectedRangeRequestOut": "_sheets_267_UpdateProtectedRangeRequestOut",
        "DeleteDimensionGroupRequestIn": "_sheets_268_DeleteDimensionGroupRequestIn",
        "DeleteDimensionGroupRequestOut": "_sheets_269_DeleteDimensionGroupRequestOut",
        "DeleteDimensionGroupResponseIn": "_sheets_270_DeleteDimensionGroupResponseIn",
        "DeleteDimensionGroupResponseOut": "_sheets_271_DeleteDimensionGroupResponseOut",
        "UpdateSheetPropertiesRequestIn": "_sheets_272_UpdateSheetPropertiesRequestIn",
        "UpdateSheetPropertiesRequestOut": "_sheets_273_UpdateSheetPropertiesRequestOut",
        "GridCoordinateIn": "_sheets_274_GridCoordinateIn",
        "GridCoordinateOut": "_sheets_275_GridCoordinateOut",
        "DataValidationRuleIn": "_sheets_276_DataValidationRuleIn",
        "DataValidationRuleOut": "_sheets_277_DataValidationRuleOut",
        "BigQueryTableSpecIn": "_sheets_278_BigQueryTableSpecIn",
        "BigQueryTableSpecOut": "_sheets_279_BigQueryTableSpecOut",
        "DeleteBandingRequestIn": "_sheets_280_DeleteBandingRequestIn",
        "DeleteBandingRequestOut": "_sheets_281_DeleteBandingRequestOut",
        "UpdateDeveloperMetadataRequestIn": "_sheets_282_UpdateDeveloperMetadataRequestIn",
        "UpdateDeveloperMetadataRequestOut": "_sheets_283_UpdateDeveloperMetadataRequestOut",
        "ConditionalFormatRuleIn": "_sheets_284_ConditionalFormatRuleIn",
        "ConditionalFormatRuleOut": "_sheets_285_ConditionalFormatRuleOut",
        "WaterfallChartSeriesIn": "_sheets_286_WaterfallChartSeriesIn",
        "WaterfallChartSeriesOut": "_sheets_287_WaterfallChartSeriesOut",
        "DimensionRangeIn": "_sheets_288_DimensionRangeIn",
        "DimensionRangeOut": "_sheets_289_DimensionRangeOut",
        "DeleteProtectedRangeRequestIn": "_sheets_290_DeleteProtectedRangeRequestIn",
        "DeleteProtectedRangeRequestOut": "_sheets_291_DeleteProtectedRangeRequestOut",
        "BasicSeriesDataPointStyleOverrideIn": "_sheets_292_BasicSeriesDataPointStyleOverrideIn",
        "BasicSeriesDataPointStyleOverrideOut": "_sheets_293_BasicSeriesDataPointStyleOverrideOut",
        "SortSpecIn": "_sheets_294_SortSpecIn",
        "SortSpecOut": "_sheets_295_SortSpecOut",
        "DataSourceRefreshWeeklyScheduleIn": "_sheets_296_DataSourceRefreshWeeklyScheduleIn",
        "DataSourceRefreshWeeklyScheduleOut": "_sheets_297_DataSourceRefreshWeeklyScheduleOut",
        "DeveloperMetadataLookupIn": "_sheets_298_DeveloperMetadataLookupIn",
        "DeveloperMetadataLookupOut": "_sheets_299_DeveloperMetadataLookupOut",
        "DeleteRangeRequestIn": "_sheets_300_DeleteRangeRequestIn",
        "DeleteRangeRequestOut": "_sheets_301_DeleteRangeRequestOut",
        "OrgChartSpecIn": "_sheets_302_OrgChartSpecIn",
        "OrgChartSpecOut": "_sheets_303_OrgChartSpecOut",
        "ScorecardChartSpecIn": "_sheets_304_ScorecardChartSpecIn",
        "ScorecardChartSpecOut": "_sheets_305_ScorecardChartSpecOut",
        "TextPositionIn": "_sheets_306_TextPositionIn",
        "TextPositionOut": "_sheets_307_TextPositionOut",
        "PieChartSpecIn": "_sheets_308_PieChartSpecIn",
        "PieChartSpecOut": "_sheets_309_PieChartSpecOut",
        "WaterfallChartCustomSubtotalIn": "_sheets_310_WaterfallChartCustomSubtotalIn",
        "WaterfallChartCustomSubtotalOut": "_sheets_311_WaterfallChartCustomSubtotalOut",
        "ManualRuleGroupIn": "_sheets_312_ManualRuleGroupIn",
        "ManualRuleGroupOut": "_sheets_313_ManualRuleGroupOut",
        "MatchedDeveloperMetadataIn": "_sheets_314_MatchedDeveloperMetadataIn",
        "MatchedDeveloperMetadataOut": "_sheets_315_MatchedDeveloperMetadataOut",
        "PivotGroupSortValueBucketIn": "_sheets_316_PivotGroupSortValueBucketIn",
        "PivotGroupSortValueBucketOut": "_sheets_317_PivotGroupSortValueBucketOut",
        "PivotValueIn": "_sheets_318_PivotValueIn",
        "PivotValueOut": "_sheets_319_PivotValueOut",
        "LinkIn": "_sheets_320_LinkIn",
        "LinkOut": "_sheets_321_LinkOut",
        "WaterfallChartSpecIn": "_sheets_322_WaterfallChartSpecIn",
        "WaterfallChartSpecOut": "_sheets_323_WaterfallChartSpecOut",
        "RowDataIn": "_sheets_324_RowDataIn",
        "RowDataOut": "_sheets_325_RowDataOut",
        "AddSlicerResponseIn": "_sheets_326_AddSlicerResponseIn",
        "AddSlicerResponseOut": "_sheets_327_AddSlicerResponseOut",
        "DeleteDimensionRequestIn": "_sheets_328_DeleteDimensionRequestIn",
        "DeleteDimensionRequestOut": "_sheets_329_DeleteDimensionRequestOut",
        "AppendDimensionRequestIn": "_sheets_330_AppendDimensionRequestIn",
        "AppendDimensionRequestOut": "_sheets_331_AppendDimensionRequestOut",
        "EmbeddedObjectBorderIn": "_sheets_332_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_sheets_333_EmbeddedObjectBorderOut",
        "DataSourceChartPropertiesIn": "_sheets_334_DataSourceChartPropertiesIn",
        "DataSourceChartPropertiesOut": "_sheets_335_DataSourceChartPropertiesOut",
        "DataSourceIn": "_sheets_336_DataSourceIn",
        "DataSourceOut": "_sheets_337_DataSourceOut",
        "AddConditionalFormatRuleRequestIn": "_sheets_338_AddConditionalFormatRuleRequestIn",
        "AddConditionalFormatRuleRequestOut": "_sheets_339_AddConditionalFormatRuleRequestOut",
        "UpdateBordersRequestIn": "_sheets_340_UpdateBordersRequestIn",
        "UpdateBordersRequestOut": "_sheets_341_UpdateBordersRequestOut",
        "AddBandingRequestIn": "_sheets_342_AddBandingRequestIn",
        "AddBandingRequestOut": "_sheets_343_AddBandingRequestOut",
        "DataSourceObjectReferenceIn": "_sheets_344_DataSourceObjectReferenceIn",
        "DataSourceObjectReferenceOut": "_sheets_345_DataSourceObjectReferenceOut",
        "SlicerIn": "_sheets_346_SlicerIn",
        "SlicerOut": "_sheets_347_SlicerOut",
        "GridDataIn": "_sheets_348_GridDataIn",
        "GridDataOut": "_sheets_349_GridDataOut",
        "CandlestickChartSpecIn": "_sheets_350_CandlestickChartSpecIn",
        "CandlestickChartSpecOut": "_sheets_351_CandlestickChartSpecOut",
        "BatchClearValuesByDataFilterRequestIn": "_sheets_352_BatchClearValuesByDataFilterRequestIn",
        "BatchClearValuesByDataFilterRequestOut": "_sheets_353_BatchClearValuesByDataFilterRequestOut",
        "AddNamedRangeRequestIn": "_sheets_354_AddNamedRangeRequestIn",
        "AddNamedRangeRequestOut": "_sheets_355_AddNamedRangeRequestOut",
        "DataSourceRefreshDailyScheduleIn": "_sheets_356_DataSourceRefreshDailyScheduleIn",
        "DataSourceRefreshDailyScheduleOut": "_sheets_357_DataSourceRefreshDailyScheduleOut",
        "PivotTableIn": "_sheets_358_PivotTableIn",
        "PivotTableOut": "_sheets_359_PivotTableOut",
        "ConditionValueIn": "_sheets_360_ConditionValueIn",
        "ConditionValueOut": "_sheets_361_ConditionValueOut",
        "SortRangeRequestIn": "_sheets_362_SortRangeRequestIn",
        "SortRangeRequestOut": "_sheets_363_SortRangeRequestOut",
        "ResponseIn": "_sheets_364_ResponseIn",
        "ResponseOut": "_sheets_365_ResponseOut",
        "UpdateDataSourceResponseIn": "_sheets_366_UpdateDataSourceResponseIn",
        "UpdateDataSourceResponseOut": "_sheets_367_UpdateDataSourceResponseOut",
        "RefreshDataSourceRequestIn": "_sheets_368_RefreshDataSourceRequestIn",
        "RefreshDataSourceRequestOut": "_sheets_369_RefreshDataSourceRequestOut",
        "CandlestickSeriesIn": "_sheets_370_CandlestickSeriesIn",
        "CandlestickSeriesOut": "_sheets_371_CandlestickSeriesOut",
        "MoveDimensionRequestIn": "_sheets_372_MoveDimensionRequestIn",
        "MoveDimensionRequestOut": "_sheets_373_MoveDimensionRequestOut",
        "AddSheetRequestIn": "_sheets_374_AddSheetRequestIn",
        "AddSheetRequestOut": "_sheets_375_AddSheetRequestOut",
        "AutoFillRequestIn": "_sheets_376_AutoFillRequestIn",
        "AutoFillRequestOut": "_sheets_377_AutoFillRequestOut",
        "ChartGroupRuleIn": "_sheets_378_ChartGroupRuleIn",
        "ChartGroupRuleOut": "_sheets_379_ChartGroupRuleOut",
        "IntervalIn": "_sheets_380_IntervalIn",
        "IntervalOut": "_sheets_381_IntervalOut",
        "AddDimensionGroupRequestIn": "_sheets_382_AddDimensionGroupRequestIn",
        "AddDimensionGroupRequestOut": "_sheets_383_AddDimensionGroupRequestOut",
        "UpdateValuesByDataFilterResponseIn": "_sheets_384_UpdateValuesByDataFilterResponseIn",
        "UpdateValuesByDataFilterResponseOut": "_sheets_385_UpdateValuesByDataFilterResponseOut",
        "SetDataValidationRequestIn": "_sheets_386_SetDataValidationRequestIn",
        "SetDataValidationRequestOut": "_sheets_387_SetDataValidationRequestOut",
        "BatchClearValuesResponseIn": "_sheets_388_BatchClearValuesResponseIn",
        "BatchClearValuesResponseOut": "_sheets_389_BatchClearValuesResponseOut",
        "DeveloperMetadataIn": "_sheets_390_DeveloperMetadataIn",
        "DeveloperMetadataOut": "_sheets_391_DeveloperMetadataOut",
        "UnmergeCellsRequestIn": "_sheets_392_UnmergeCellsRequestIn",
        "UnmergeCellsRequestOut": "_sheets_393_UnmergeCellsRequestOut",
        "BooleanRuleIn": "_sheets_394_BooleanRuleIn",
        "BooleanRuleOut": "_sheets_395_BooleanRuleOut",
        "BandedRangeIn": "_sheets_396_BandedRangeIn",
        "BandedRangeOut": "_sheets_397_BandedRangeOut",
        "ClearValuesResponseIn": "_sheets_398_ClearValuesResponseIn",
        "ClearValuesResponseOut": "_sheets_399_ClearValuesResponseOut",
        "FilterSpecIn": "_sheets_400_FilterSpecIn",
        "FilterSpecOut": "_sheets_401_FilterSpecOut",
        "AddNamedRangeResponseIn": "_sheets_402_AddNamedRangeResponseIn",
        "AddNamedRangeResponseOut": "_sheets_403_AddNamedRangeResponseOut",
        "RefreshDataSourceObjectExecutionStatusIn": "_sheets_404_RefreshDataSourceObjectExecutionStatusIn",
        "RefreshDataSourceObjectExecutionStatusOut": "_sheets_405_RefreshDataSourceObjectExecutionStatusOut",
        "UpdateDimensionGroupRequestIn": "_sheets_406_UpdateDimensionGroupRequestIn",
        "UpdateDimensionGroupRequestOut": "_sheets_407_UpdateDimensionGroupRequestOut",
        "BooleanConditionIn": "_sheets_408_BooleanConditionIn",
        "BooleanConditionOut": "_sheets_409_BooleanConditionOut",
        "SearchDeveloperMetadataRequestIn": "_sheets_410_SearchDeveloperMetadataRequestIn",
        "SearchDeveloperMetadataRequestOut": "_sheets_411_SearchDeveloperMetadataRequestOut",
        "UpdateEmbeddedObjectBorderRequestIn": "_sheets_412_UpdateEmbeddedObjectBorderRequestIn",
        "UpdateEmbeddedObjectBorderRequestOut": "_sheets_413_UpdateEmbeddedObjectBorderRequestOut",
        "DeleteDeveloperMetadataResponseIn": "_sheets_414_DeleteDeveloperMetadataResponseIn",
        "DeleteDeveloperMetadataResponseOut": "_sheets_415_DeleteDeveloperMetadataResponseOut",
        "WaterfallChartColumnStyleIn": "_sheets_416_WaterfallChartColumnStyleIn",
        "WaterfallChartColumnStyleOut": "_sheets_417_WaterfallChartColumnStyleOut",
        "DeleteEmbeddedObjectRequestIn": "_sheets_418_DeleteEmbeddedObjectRequestIn",
        "DeleteEmbeddedObjectRequestOut": "_sheets_419_DeleteEmbeddedObjectRequestOut",
        "CellFormatIn": "_sheets_420_CellFormatIn",
        "CellFormatOut": "_sheets_421_CellFormatOut",
        "BandingPropertiesIn": "_sheets_422_BandingPropertiesIn",
        "BandingPropertiesOut": "_sheets_423_BandingPropertiesOut",
        "DeveloperMetadataLocationIn": "_sheets_424_DeveloperMetadataLocationIn",
        "DeveloperMetadataLocationOut": "_sheets_425_DeveloperMetadataLocationOut",
        "DimensionGroupIn": "_sheets_426_DimensionGroupIn",
        "DimensionGroupOut": "_sheets_427_DimensionGroupOut",
        "SourceAndDestinationIn": "_sheets_428_SourceAndDestinationIn",
        "SourceAndDestinationOut": "_sheets_429_SourceAndDestinationOut",
        "ChartHistogramRuleIn": "_sheets_430_ChartHistogramRuleIn",
        "ChartHistogramRuleOut": "_sheets_431_ChartHistogramRuleOut",
        "SheetIn": "_sheets_432_SheetIn",
        "SheetOut": "_sheets_433_SheetOut",
        "GetSpreadsheetByDataFilterRequestIn": "_sheets_434_GetSpreadsheetByDataFilterRequestIn",
        "GetSpreadsheetByDataFilterRequestOut": "_sheets_435_GetSpreadsheetByDataFilterRequestOut",
        "TextRotationIn": "_sheets_436_TextRotationIn",
        "TextRotationOut": "_sheets_437_TextRotationOut",
        "FindReplaceRequestIn": "_sheets_438_FindReplaceRequestIn",
        "FindReplaceRequestOut": "_sheets_439_FindReplaceRequestOut",
        "CreateDeveloperMetadataRequestIn": "_sheets_440_CreateDeveloperMetadataRequestIn",
        "CreateDeveloperMetadataRequestOut": "_sheets_441_CreateDeveloperMetadataRequestOut",
        "AddChartRequestIn": "_sheets_442_AddChartRequestIn",
        "AddChartRequestOut": "_sheets_443_AddChartRequestOut",
        "GridRangeIn": "_sheets_444_GridRangeIn",
        "GridRangeOut": "_sheets_445_GridRangeOut",
        "EmbeddedChartIn": "_sheets_446_EmbeddedChartIn",
        "EmbeddedChartOut": "_sheets_447_EmbeddedChartOut",
        "CandlestickDataIn": "_sheets_448_CandlestickDataIn",
        "CandlestickDataOut": "_sheets_449_CandlestickDataOut",
        "DataFilterIn": "_sheets_450_DataFilterIn",
        "DataFilterOut": "_sheets_451_DataFilterOut",
        "AddDataSourceRequestIn": "_sheets_452_AddDataSourceRequestIn",
        "AddDataSourceRequestOut": "_sheets_453_AddDataSourceRequestOut",
        "BasicChartAxisIn": "_sheets_454_BasicChartAxisIn",
        "BasicChartAxisOut": "_sheets_455_BasicChartAxisOut",
        "PivotGroupIn": "_sheets_456_PivotGroupIn",
        "PivotGroupOut": "_sheets_457_PivotGroupOut",
        "InsertDimensionRequestIn": "_sheets_458_InsertDimensionRequestIn",
        "InsertDimensionRequestOut": "_sheets_459_InsertDimensionRequestOut",
        "DeleteSheetRequestIn": "_sheets_460_DeleteSheetRequestIn",
        "DeleteSheetRequestOut": "_sheets_461_DeleteSheetRequestOut",
        "ChartSpecIn": "_sheets_462_ChartSpecIn",
        "ChartSpecOut": "_sheets_463_ChartSpecOut",
        "DataSourceSheetDimensionRangeIn": "_sheets_464_DataSourceSheetDimensionRangeIn",
        "DataSourceSheetDimensionRangeOut": "_sheets_465_DataSourceSheetDimensionRangeOut",
        "ExtendedValueIn": "_sheets_466_ExtendedValueIn",
        "ExtendedValueOut": "_sheets_467_ExtendedValueOut",
        "DateTimeRuleIn": "_sheets_468_DateTimeRuleIn",
        "DateTimeRuleOut": "_sheets_469_DateTimeRuleOut",
        "SpreadsheetThemeIn": "_sheets_470_SpreadsheetThemeIn",
        "SpreadsheetThemeOut": "_sheets_471_SpreadsheetThemeOut",
        "AppendCellsRequestIn": "_sheets_472_AppendCellsRequestIn",
        "AppendCellsRequestOut": "_sheets_473_AppendCellsRequestOut",
        "SetBasicFilterRequestIn": "_sheets_474_SetBasicFilterRequestIn",
        "SetBasicFilterRequestOut": "_sheets_475_SetBasicFilterRequestOut",
        "DeleteNamedRangeRequestIn": "_sheets_476_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_sheets_477_DeleteNamedRangeRequestOut",
        "UpdateCellsRequestIn": "_sheets_478_UpdateCellsRequestIn",
        "UpdateCellsRequestOut": "_sheets_479_UpdateCellsRequestOut",
        "BatchClearValuesByDataFilterResponseIn": "_sheets_480_BatchClearValuesByDataFilterResponseIn",
        "BatchClearValuesByDataFilterResponseOut": "_sheets_481_BatchClearValuesByDataFilterResponseOut",
        "DuplicateFilterViewRequestIn": "_sheets_482_DuplicateFilterViewRequestIn",
        "DuplicateFilterViewRequestOut": "_sheets_483_DuplicateFilterViewRequestOut",
        "BatchUpdateValuesRequestIn": "_sheets_484_BatchUpdateValuesRequestIn",
        "BatchUpdateValuesRequestOut": "_sheets_485_BatchUpdateValuesRequestOut",
        "TreemapChartColorScaleIn": "_sheets_486_TreemapChartColorScaleIn",
        "TreemapChartColorScaleOut": "_sheets_487_TreemapChartColorScaleOut",
        "BasicChartDomainIn": "_sheets_488_BasicChartDomainIn",
        "BasicChartDomainOut": "_sheets_489_BasicChartDomainOut",
        "AutoResizeDimensionsRequestIn": "_sheets_490_AutoResizeDimensionsRequestIn",
        "AutoResizeDimensionsRequestOut": "_sheets_491_AutoResizeDimensionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["InsertRangeRequestIn"] = t.struct(
        {
            "shiftDimension": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["InsertRangeRequestIn"])
    types["InsertRangeRequestOut"] = t.struct(
        {
            "shiftDimension": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertRangeRequestOut"])
    types["ClearValuesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClearValuesRequestIn"]
    )
    types["ClearValuesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearValuesRequestOut"])
    types["SearchDeveloperMetadataResponseIn"] = t.struct(
        {
            "matchedDeveloperMetadata": t.array(
                t.proxy(renames["MatchedDeveloperMetadataIn"])
            ).optional()
        }
    ).named(renames["SearchDeveloperMetadataResponseIn"])
    types["SearchDeveloperMetadataResponseOut"] = t.struct(
        {
            "matchedDeveloperMetadata": t.array(
                t.proxy(renames["MatchedDeveloperMetadataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDeveloperMetadataResponseOut"])
    types["AddProtectedRangeResponseIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeResponseIn"])
    types["AddProtectedRangeResponseOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeResponseOut"])
    types["BigQueryDataSourceSpecIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "tableSpec": t.proxy(renames["BigQueryTableSpecIn"]).optional(),
            "querySpec": t.proxy(renames["BigQueryQuerySpecIn"]).optional(),
        }
    ).named(renames["BigQueryDataSourceSpecIn"])
    types["BigQueryDataSourceSpecOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "tableSpec": t.proxy(renames["BigQueryTableSpecOut"]).optional(),
            "querySpec": t.proxy(renames["BigQueryQuerySpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDataSourceSpecOut"])
    types["DuplicateFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["DuplicateFilterViewResponseIn"])
    types["DuplicateFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewResponseOut"])
    types["DeleteConditionalFormatRuleRequestIn"] = t.struct(
        {"sheetId": t.integer().optional(), "index": t.integer().optional()}
    ).named(renames["DeleteConditionalFormatRuleRequestIn"])
    types["DeleteConditionalFormatRuleRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConditionalFormatRuleRequestOut"])
    types["DataSourceObjectReferencesIn"] = t.struct(
        {
            "references": t.array(
                t.proxy(renames["DataSourceObjectReferenceIn"])
            ).optional()
        }
    ).named(renames["DataSourceObjectReferencesIn"])
    types["DataSourceObjectReferencesOut"] = t.struct(
        {
            "references": t.array(
                t.proxy(renames["DataSourceObjectReferenceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceObjectReferencesOut"])
    types["BasicFilterIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
        }
    ).named(renames["BasicFilterIn"])
    types["BasicFilterOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicFilterOut"])
    types["DeleteDuplicatesResponseIn"] = t.struct(
        {"duplicatesRemovedCount": t.integer().optional()}
    ).named(renames["DeleteDuplicatesResponseIn"])
    types["DeleteDuplicatesResponseOut"] = t.struct(
        {
            "duplicatesRemovedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDuplicatesResponseOut"])
    types["AddChartResponseIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartResponseIn"])
    types["AddChartResponseOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartResponseOut"])
    types["NumberFormatIn"] = t.struct(
        {"pattern": t.string().optional(), "type": t.string().optional()}
    ).named(renames["NumberFormatIn"])
    types["NumberFormatOut"] = t.struct(
        {
            "pattern": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NumberFormatOut"])
    types["BatchUpdateSpreadsheetRequestIn"] = t.struct(
        {
            "includeSpreadsheetInResponse": t.boolean().optional(),
            "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
            "responseIncludeGridData": t.boolean().optional(),
            "responseRanges": t.array(t.string()).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetRequestIn"])
    types["BatchUpdateSpreadsheetRequestOut"] = t.struct(
        {
            "includeSpreadsheetInResponse": t.boolean().optional(),
            "requests": t.array(t.proxy(renames["RequestOut"])).optional(),
            "responseIncludeGridData": t.boolean().optional(),
            "responseRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetRequestOut"])
    types["TrimWhitespaceRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["TrimWhitespaceRequestIn"])
    types["TrimWhitespaceRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceRequestOut"])
    types["GridPropertiesIn"] = t.struct(
        {
            "rowGroupControlAfter": t.boolean().optional(),
            "frozenRowCount": t.integer().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
            "columnCount": t.integer().optional(),
            "hideGridlines": t.boolean().optional(),
            "frozenColumnCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
        }
    ).named(renames["GridPropertiesIn"])
    types["GridPropertiesOut"] = t.struct(
        {
            "rowGroupControlAfter": t.boolean().optional(),
            "frozenRowCount": t.integer().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
            "columnCount": t.integer().optional(),
            "hideGridlines": t.boolean().optional(),
            "frozenColumnCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridPropertiesOut"])
    types["BatchClearValuesRequestIn"] = t.struct(
        {"ranges": t.array(t.string()).optional()}
    ).named(renames["BatchClearValuesRequestIn"])
    types["BatchClearValuesRequestOut"] = t.struct(
        {
            "ranges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesRequestOut"])
    types["TextFormatIn"] = t.struct(
        {
            "link": t.proxy(renames["LinkIn"]).optional(),
            "bold": t.boolean().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "underline": t.boolean().optional(),
            "fontFamily": t.string().optional(),
            "fontSize": t.integer().optional(),
            "italic": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "strikethrough": t.boolean().optional(),
        }
    ).named(renames["TextFormatIn"])
    types["TextFormatOut"] = t.struct(
        {
            "link": t.proxy(renames["LinkOut"]).optional(),
            "bold": t.boolean().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "underline": t.boolean().optional(),
            "fontFamily": t.string().optional(),
            "fontSize": t.integer().optional(),
            "italic": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "strikethrough": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFormatOut"])
    types["BatchUpdateSpreadsheetResponseIn"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
            "spreadsheetId": t.string().optional(),
            "updatedSpreadsheet": t.proxy(renames["SpreadsheetIn"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetResponseIn"])
    types["BatchUpdateSpreadsheetResponseOut"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "spreadsheetId": t.string().optional(),
            "updatedSpreadsheet": t.proxy(renames["SpreadsheetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetResponseOut"])
    types["GradientRuleIn"] = t.struct(
        {
            "maxpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
            "midpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
            "minpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
        }
    ).named(renames["GradientRuleIn"])
    types["GradientRuleOut"] = t.struct(
        {
            "maxpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "midpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "minpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradientRuleOut"])
    types["CreateDeveloperMetadataResponseIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataResponseIn"])
    types["CreateDeveloperMetadataResponseOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataResponseOut"])
    types["DeleteDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilter": t.proxy(renames["DataFilterIn"]).optional()}
    ).named(renames["DeleteDeveloperMetadataRequestIn"])
    types["DeleteDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDeveloperMetadataRequestOut"])
    types["UpdateEmbeddedObjectPositionRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "newPosition": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "objectId": t.integer().optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionRequestIn"])
    types["UpdateEmbeddedObjectPositionRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "newPosition": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionRequestOut"])
    types["SlicerSpecIn"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "columnIndex": t.integer().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "applyToPivotTables": t.boolean().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "title": t.string().optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
            "dataRange": t.proxy(renames["GridRangeIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
        }
    ).named(renames["SlicerSpecIn"])
    types["SlicerSpecOut"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "columnIndex": t.integer().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "applyToPivotTables": t.boolean().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "title": t.string().optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "dataRange": t.proxy(renames["GridRangeOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerSpecOut"])
    types["DataSourceSpecIn"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "bigQuery": t.proxy(renames["BigQueryDataSourceSpecIn"]).optional(),
        }
    ).named(renames["DataSourceSpecIn"])
    types["DataSourceSpecOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["DataSourceParameterOut"])
            ).optional(),
            "bigQuery": t.proxy(renames["BigQueryDataSourceSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSpecOut"])
    types["RepeatCellRequestIn"] = t.struct(
        {
            "cell": t.proxy(renames["CellDataIn"]).optional(),
            "fields": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["RepeatCellRequestIn"])
    types["RepeatCellRequestOut"] = t.struct(
        {
            "cell": t.proxy(renames["CellDataOut"]).optional(),
            "fields": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepeatCellRequestOut"])
    types["SpreadsheetPropertiesIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "title": t.string().optional(),
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsIn"]
            ).optional(),
            "autoRecalc": t.string().optional(),
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeIn"]).optional(),
            "defaultFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "locale": t.string().optional(),
        }
    ).named(renames["SpreadsheetPropertiesIn"])
    types["SpreadsheetPropertiesOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "title": t.string().optional(),
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsOut"]
            ).optional(),
            "autoRecalc": t.string().optional(),
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeOut"]).optional(),
            "defaultFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "locale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetPropertiesOut"])
    types["PivotGroupRuleIn"] = t.struct(
        {
            "dateTimeRule": t.proxy(renames["DateTimeRuleIn"]).optional(),
            "manualRule": t.proxy(renames["ManualRuleIn"]).optional(),
            "histogramRule": t.proxy(renames["HistogramRuleIn"]).optional(),
        }
    ).named(renames["PivotGroupRuleIn"])
    types["PivotGroupRuleOut"] = t.struct(
        {
            "dateTimeRule": t.proxy(renames["DateTimeRuleOut"]).optional(),
            "manualRule": t.proxy(renames["ManualRuleOut"]).optional(),
            "histogramRule": t.proxy(renames["HistogramRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupRuleOut"])
    types["UpdateDataSourceRequestIn"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateDataSourceRequestIn"])
    types["UpdateDataSourceRequestOut"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestOut"])
    types["DeleteFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DeleteFilterViewRequestIn"])
    types["DeleteFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFilterViewRequestOut"])
    types["MergeCellsRequestIn"] = t.struct(
        {
            "mergeType": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["MergeCellsRequestIn"])
    types["MergeCellsRequestOut"] = t.struct(
        {
            "mergeType": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeCellsRequestOut"])
    types["DeleteDuplicatesRequestIn"] = t.struct(
        {
            "comparisonColumns": t.array(
                t.proxy(renames["DimensionRangeIn"])
            ).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["DeleteDuplicatesRequestIn"])
    types["DeleteDuplicatesRequestOut"] = t.struct(
        {
            "comparisonColumns": t.array(
                t.proxy(renames["DimensionRangeOut"])
            ).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDuplicatesRequestOut"])
    types["DataSourceSheetPropertiesIn"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["DataSourceColumnIn"])).optional(),
            "dataSourceId": t.string().optional(),
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
        }
    ).named(renames["DataSourceSheetPropertiesIn"])
    types["DataSourceSheetPropertiesOut"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["DataSourceColumnOut"])).optional(),
            "dataSourceId": t.string().optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSheetPropertiesOut"])
    types["RefreshDataSourceResponseIn"] = t.struct(
        {
            "statuses": t.array(
                t.proxy(renames["RefreshDataSourceObjectExecutionStatusIn"])
            ).optional()
        }
    ).named(renames["RefreshDataSourceResponseIn"])
    types["RefreshDataSourceResponseOut"] = t.struct(
        {
            "statuses": t.array(
                t.proxy(renames["RefreshDataSourceObjectExecutionStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshDataSourceResponseOut"])
    types["DataSourceColumnReferenceIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["DataSourceColumnReferenceIn"])
    types["DataSourceColumnReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceColumnReferenceOut"])
    types["MatchedValueRangeIn"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "valueRange": t.proxy(renames["ValueRangeIn"]).optional(),
        }
    ).named(renames["MatchedValueRangeIn"])
    types["MatchedValueRangeOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "valueRange": t.proxy(renames["ValueRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchedValueRangeOut"])
    types["BasicChartSpecIn"] = t.struct(
        {
            "lineSmoothing": t.boolean().optional(),
            "interpolateNulls": t.boolean().optional(),
            "threeDimensional": t.boolean().optional(),
            "headerCount": t.integer().optional(),
            "chartType": t.string().optional(),
            "compareMode": t.string().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "axis": t.array(t.proxy(renames["BasicChartAxisIn"])).optional(),
            "legendPosition": t.string().optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesIn"])).optional(),
            "stackedType": t.string().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainIn"])).optional(),
        }
    ).named(renames["BasicChartSpecIn"])
    types["BasicChartSpecOut"] = t.struct(
        {
            "lineSmoothing": t.boolean().optional(),
            "interpolateNulls": t.boolean().optional(),
            "threeDimensional": t.boolean().optional(),
            "headerCount": t.integer().optional(),
            "chartType": t.string().optional(),
            "compareMode": t.string().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "axis": t.array(t.proxy(renames["BasicChartAxisOut"])).optional(),
            "legendPosition": t.string().optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesOut"])).optional(),
            "stackedType": t.string().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSpecOut"])
    types["BigQueryQuerySpecIn"] = t.struct({"rawQuery": t.string().optional()}).named(
        renames["BigQueryQuerySpecIn"]
    )
    types["BigQueryQuerySpecOut"] = t.struct(
        {
            "rawQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryQuerySpecOut"])
    types["UpdateEmbeddedObjectPositionResponseIn"] = t.struct(
        {"position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional()}
    ).named(renames["UpdateEmbeddedObjectPositionResponseIn"])
    types["UpdateEmbeddedObjectPositionResponseOut"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionResponseOut"])
    types["UpdateChartSpecRequestIn"] = t.struct(
        {
            "spec": t.proxy(renames["ChartSpecIn"]).optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["UpdateChartSpecRequestIn"])
    types["UpdateChartSpecRequestOut"] = t.struct(
        {
            "spec": t.proxy(renames["ChartSpecOut"]).optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateChartSpecRequestOut"])
    types["UpdateBandingRequestIn"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateBandingRequestIn"])
    types["UpdateBandingRequestOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBandingRequestOut"])
    types["ColorStyleIn"] = t.struct(
        {
            "rgbColor": t.proxy(renames["ColorIn"]).optional(),
            "themeColor": t.string().optional(),
        }
    ).named(renames["ColorStyleIn"])
    types["ColorStyleOut"] = t.struct(
        {
            "rgbColor": t.proxy(renames["ColorOut"]).optional(),
            "themeColor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorStyleOut"])
    types["FindReplaceResponseIn"] = t.struct(
        {
            "valuesChanged": t.integer().optional(),
            "formulasChanged": t.integer().optional(),
            "rowsChanged": t.integer().optional(),
            "sheetsChanged": t.integer().optional(),
            "occurrencesChanged": t.integer().optional(),
        }
    ).named(renames["FindReplaceResponseIn"])
    types["FindReplaceResponseOut"] = t.struct(
        {
            "valuesChanged": t.integer().optional(),
            "formulasChanged": t.integer().optional(),
            "rowsChanged": t.integer().optional(),
            "sheetsChanged": t.integer().optional(),
            "occurrencesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceResponseOut"])
    types["AddProtectedRangeRequestIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeRequestIn"])
    types["AddProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeRequestOut"])
    types["ErrorValueIn"] = t.struct(
        {"message": t.string().optional(), "type": t.string().optional()}
    ).named(renames["ErrorValueIn"])
    types["ErrorValueOut"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorValueOut"])
    types["AddSlicerRequestIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerRequestIn"])
    types["AddSlicerRequestOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerRequestOut"])
    types["OverlayPositionIn"] = t.struct(
        {
            "widthPixels": t.integer().optional(),
            "offsetXPixels": t.integer().optional(),
            "offsetYPixels": t.integer().optional(),
            "anchorCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "heightPixels": t.integer().optional(),
        }
    ).named(renames["OverlayPositionIn"])
    types["OverlayPositionOut"] = t.struct(
        {
            "widthPixels": t.integer().optional(),
            "offsetXPixels": t.integer().optional(),
            "offsetYPixels": t.integer().optional(),
            "anchorCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "heightPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OverlayPositionOut"])
    types["InterpolationPointIn"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["InterpolationPointIn"])
    types["InterpolationPointOut"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InterpolationPointOut"])
    types["ProtectedRangeIn"] = t.struct(
        {
            "protectedRangeId": t.integer().optional(),
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "editors": t.proxy(renames["EditorsIn"]).optional(),
            "namedRangeId": t.string().optional(),
            "warningOnly": t.boolean().optional(),
            "requestingUserCanEdit": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ProtectedRangeIn"])
    types["ProtectedRangeOut"] = t.struct(
        {
            "protectedRangeId": t.integer().optional(),
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "editors": t.proxy(renames["EditorsOut"]).optional(),
            "namedRangeId": t.string().optional(),
            "warningOnly": t.boolean().optional(),
            "requestingUserCanEdit": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProtectedRangeOut"])
    types["EmbeddedObjectPositionIn"] = t.struct(
        {
            "overlayPosition": t.proxy(renames["OverlayPositionIn"]).optional(),
            "newSheet": t.boolean().optional(),
            "sheetId": t.integer().optional(),
        }
    ).named(renames["EmbeddedObjectPositionIn"])
    types["EmbeddedObjectPositionOut"] = t.struct(
        {
            "overlayPosition": t.proxy(renames["OverlayPositionOut"]).optional(),
            "newSheet": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectPositionOut"])
    types["PivotGroupValueMetadataIn"] = t.struct(
        {
            "collapsed": t.boolean().optional(),
            "value": t.proxy(renames["ExtendedValueIn"]).optional(),
        }
    ).named(renames["PivotGroupValueMetadataIn"])
    types["PivotGroupValueMetadataOut"] = t.struct(
        {
            "collapsed": t.boolean().optional(),
            "value": t.proxy(renames["ExtendedValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupValueMetadataOut"])
    types["DeleteDataSourceRequestIn"] = t.struct(
        {"dataSourceId": t.string().optional()}
    ).named(renames["DeleteDataSourceRequestIn"])
    types["DeleteDataSourceRequestOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDataSourceRequestOut"])
    types["TextToColumnsRequestIn"] = t.struct(
        {
            "delimiter": t.string().optional(),
            "delimiterType": t.string().optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["TextToColumnsRequestIn"])
    types["TextToColumnsRequestOut"] = t.struct(
        {
            "delimiter": t.string().optional(),
            "delimiterType": t.string().optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextToColumnsRequestOut"])
    types["PivotFilterCriteriaIn"] = t.struct(
        {
            "visibleValues": t.array(t.string()).optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "visibleByDefault": t.boolean().optional(),
        }
    ).named(renames["PivotFilterCriteriaIn"])
    types["PivotFilterCriteriaOut"] = t.struct(
        {
            "visibleValues": t.array(t.string()).optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "visibleByDefault": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotFilterCriteriaOut"])
    types["ChartCustomNumberFormatOptionsIn"] = t.struct(
        {"prefix": t.string().optional(), "suffix": t.string().optional()}
    ).named(renames["ChartCustomNumberFormatOptionsIn"])
    types["ChartCustomNumberFormatOptionsOut"] = t.struct(
        {
            "prefix": t.string().optional(),
            "suffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartCustomNumberFormatOptionsOut"])
    types["BasicChartSeriesIn"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideIn"])
            ).optional(),
            "targetAxis": t.string().optional(),
            "type": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "lineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
        }
    ).named(renames["BasicChartSeriesIn"])
    types["BasicChartSeriesOut"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideOut"])
            ).optional(),
            "targetAxis": t.string().optional(),
            "type": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "lineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSeriesOut"])
    types["IterativeCalculationSettingsIn"] = t.struct(
        {
            "convergenceThreshold": t.number().optional(),
            "maxIterations": t.integer().optional(),
        }
    ).named(renames["IterativeCalculationSettingsIn"])
    types["IterativeCalculationSettingsOut"] = t.struct(
        {
            "convergenceThreshold": t.number().optional(),
            "maxIterations": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IterativeCalculationSettingsOut"])
    types["ColorIn"] = t.struct(
        {
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["DataSourceTableIn"] = t.struct(
        {
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceIn"])
            ).optional(),
            "columnSelectionType": t.string().optional(),
            "rowLimit": t.integer().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
        }
    ).named(renames["DataSourceTableIn"])
    types["DataSourceTableOut"] = t.struct(
        {
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "dataSourceId": t.string().optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceOut"])
            ).optional(),
            "columnSelectionType": t.string().optional(),
            "rowLimit": t.integer().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceTableOut"])
    types["LineStyleIn"] = t.struct(
        {"type": t.string().optional(), "width": t.integer().optional()}
    ).named(renames["LineStyleIn"])
    types["LineStyleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineStyleOut"])
    types["BaselineValueFormatIn"] = t.struct(
        {
            "comparisonType": t.string().optional(),
            "negativeColor": t.proxy(renames["ColorIn"]).optional(),
            "description": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "positiveColor": t.proxy(renames["ColorIn"]).optional(),
            "position": t.proxy(renames["TextPositionIn"]).optional(),
        }
    ).named(renames["BaselineValueFormatIn"])
    types["BaselineValueFormatOut"] = t.struct(
        {
            "comparisonType": t.string().optional(),
            "negativeColor": t.proxy(renames["ColorOut"]).optional(),
            "description": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "positiveColor": t.proxy(renames["ColorOut"]).optional(),
            "position": t.proxy(renames["TextPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BaselineValueFormatOut"])
    types["DuplicateSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["DuplicateSheetResponseIn"])
    types["DuplicateSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetResponseOut"])
    types["UpdateSpreadsheetPropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
        }
    ).named(renames["UpdateSpreadsheetPropertiesRequestIn"])
    types["UpdateSpreadsheetPropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSpreadsheetPropertiesRequestOut"])
    types["UpdateConditionalFormatRuleResponseIn"] = t.struct(
        {
            "newRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "oldIndex": t.integer().optional(),
            "newIndex": t.integer().optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseIn"])
    types["UpdateConditionalFormatRuleResponseOut"] = t.struct(
        {
            "newRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "oldIndex": t.integer().optional(),
            "newIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseOut"])
    types["PointStyleIn"] = t.struct(
        {"shape": t.string().optional(), "size": t.number().optional()}
    ).named(renames["PointStyleIn"])
    types["PointStyleOut"] = t.struct(
        {
            "shape": t.string().optional(),
            "size": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PointStyleOut"])
    types["ChartDataIn"] = t.struct(
        {
            "sourceRange": t.proxy(renames["ChartSourceRangeIn"]).optional(),
            "groupRule": t.proxy(renames["ChartGroupRuleIn"]).optional(),
            "columnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "aggregateType": t.string().optional(),
        }
    ).named(renames["ChartDataIn"])
    types["ChartDataOut"] = t.struct(
        {
            "sourceRange": t.proxy(renames["ChartSourceRangeOut"]).optional(),
            "groupRule": t.proxy(renames["ChartGroupRuleOut"]).optional(),
            "columnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "aggregateType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDataOut"])
    types["DataSourceColumnIn"] = t.struct(
        {
            "formula": t.string().optional(),
            "reference": t.proxy(renames["DataSourceColumnReferenceIn"]).optional(),
        }
    ).named(renames["DataSourceColumnIn"])
    types["DataSourceColumnOut"] = t.struct(
        {
            "formula": t.string().optional(),
            "reference": t.proxy(renames["DataSourceColumnReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceColumnOut"])
    types["AddFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewResponseIn"])
    types["AddFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewResponseOut"])
    types["FilterCriteriaIn"] = t.struct(
        {
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorIn"]).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "hiddenValues": t.array(t.string()).optional(),
        }
    ).named(renames["FilterCriteriaIn"])
    types["FilterCriteriaOut"] = t.struct(
        {
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorOut"]).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "hiddenValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterCriteriaOut"])
    types["ChartAxisViewWindowOptionsIn"] = t.struct(
        {
            "viewWindowMax": t.number().optional(),
            "viewWindowMin": t.number().optional(),
            "viewWindowMode": t.string().optional(),
        }
    ).named(renames["ChartAxisViewWindowOptionsIn"])
    types["ChartAxisViewWindowOptionsOut"] = t.struct(
        {
            "viewWindowMax": t.number().optional(),
            "viewWindowMin": t.number().optional(),
            "viewWindowMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartAxisViewWindowOptionsOut"])
    types["ClearBasicFilterRequestIn"] = t.struct(
        {"sheetId": t.integer().optional()}
    ).named(renames["ClearBasicFilterRequestIn"])
    types["ClearBasicFilterRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearBasicFilterRequestOut"])
    types["HistogramSeriesIn"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataIn"]).optional(),
            "barColor": t.proxy(renames["ColorIn"]).optional(),
            "barColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["HistogramSeriesIn"])
    types["HistogramSeriesOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "barColor": t.proxy(renames["ColorOut"]).optional(),
            "barColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramSeriesOut"])
    types["DataSourceParameterIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
        }
    ).named(renames["DataSourceParameterIn"])
    types["DataSourceParameterOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceParameterOut"])
    types["BatchGetValuesByDataFilterRequestIn"] = t.struct(
        {
            "majorDimension": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "dateTimeRenderOption": t.string().optional(),
            "valueRenderOption": t.string().optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestIn"])
    types["BatchGetValuesByDataFilterRequestOut"] = t.struct(
        {
            "majorDimension": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "dateTimeRenderOption": t.string().optional(),
            "valueRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestOut"])
    types["CutPasteRequestIn"] = t.struct(
        {
            "destination": t.proxy(renames["GridCoordinateIn"]).optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "pasteType": t.string().optional(),
        }
    ).named(renames["CutPasteRequestIn"])
    types["CutPasteRequestOut"] = t.struct(
        {
            "destination": t.proxy(renames["GridCoordinateOut"]).optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "pasteType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutPasteRequestOut"])
    types["DataSourceRefreshMonthlyScheduleIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "daysOfMonth": t.array(t.integer()).optional(),
        }
    ).named(renames["DataSourceRefreshMonthlyScheduleIn"])
    types["DataSourceRefreshMonthlyScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "daysOfMonth": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshMonthlyScheduleOut"])
    types["UpdateNamedRangeRequestIn"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateNamedRangeRequestIn"])
    types["UpdateNamedRangeRequestOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateNamedRangeRequestOut"])
    types["BubbleChartSpecIn"] = t.struct(
        {
            "bubbleMaxRadiusSize": t.integer().optional(),
            "groupIds": t.proxy(renames["ChartDataIn"]).optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "legendPosition": t.string().optional(),
            "bubbleSizes": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "bubbleLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatIn"]).optional(),
            "bubbleBorderColor": t.proxy(renames["ColorIn"]).optional(),
            "bubbleOpacity": t.number().optional(),
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["BubbleChartSpecIn"])
    types["BubbleChartSpecOut"] = t.struct(
        {
            "bubbleMaxRadiusSize": t.integer().optional(),
            "groupIds": t.proxy(renames["ChartDataOut"]).optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "legendPosition": t.string().optional(),
            "bubbleSizes": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "bubbleLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatOut"]).optional(),
            "bubbleBorderColor": t.proxy(renames["ColorOut"]).optional(),
            "bubbleOpacity": t.number().optional(),
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BubbleChartSpecOut"])
    types["PivotGroupLimitIn"] = t.struct(
        {"countLimit": t.integer().optional(), "applyOrder": t.integer().optional()}
    ).named(renames["PivotGroupLimitIn"])
    types["PivotGroupLimitOut"] = t.struct(
        {
            "countLimit": t.integer().optional(),
            "applyOrder": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupLimitOut"])
    types["CopyPasteRequestIn"] = t.struct(
        {
            "pasteOrientation": t.string().optional(),
            "pasteType": t.string().optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "destination": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["CopyPasteRequestIn"])
    types["CopyPasteRequestOut"] = t.struct(
        {
            "pasteOrientation": t.string().optional(),
            "pasteType": t.string().optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "destination": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyPasteRequestOut"])
    types["TextFormatRunIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "format": t.proxy(renames["TextFormatIn"]).optional(),
        }
    ).named(renames["TextFormatRunIn"])
    types["TextFormatRunOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "format": t.proxy(renames["TextFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFormatRunOut"])
    types["FilterViewIn"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "namedRangeId": t.string().optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "title": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "filterViewId": t.integer().optional(),
        }
    ).named(renames["FilterViewIn"])
    types["FilterViewOut"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "namedRangeId": t.string().optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "title": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "filterViewId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterViewOut"])
    types["UpdateFilterViewRequestIn"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateFilterViewRequestIn"])
    types["UpdateFilterViewRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFilterViewRequestOut"])
    types["BorderIn"] = t.struct(
        {
            "style": t.string().optional(),
            "width": t.integer().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BorderIn"])
    types["BorderOut"] = t.struct(
        {
            "style": t.string().optional(),
            "width": t.integer().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BorderOut"])
    types["HistogramChartSpecIn"] = t.struct(
        {
            "showItemDividers": t.boolean().optional(),
            "outlierPercentile": t.number().optional(),
            "bucketSize": t.number().optional(),
            "series": t.array(t.proxy(renames["HistogramSeriesIn"])).optional(),
            "legendPosition": t.string().optional(),
        }
    ).named(renames["HistogramChartSpecIn"])
    types["HistogramChartSpecOut"] = t.struct(
        {
            "showItemDividers": t.boolean().optional(),
            "outlierPercentile": t.number().optional(),
            "bucketSize": t.number().optional(),
            "series": t.array(t.proxy(renames["HistogramSeriesOut"])).optional(),
            "legendPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramChartSpecOut"])
    types["AddSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetResponseIn"])
    types["AddSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetResponseOut"])
    types["PivotFilterSpecIn"] = t.struct(
        {
            "columnOffsetIndex": t.integer().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "filterCriteria": t.proxy(renames["PivotFilterCriteriaIn"]).optional(),
        }
    ).named(renames["PivotFilterSpecIn"])
    types["PivotFilterSpecOut"] = t.struct(
        {
            "columnOffsetIndex": t.integer().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "filterCriteria": t.proxy(renames["PivotFilterCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotFilterSpecOut"])
    types["CellDataIn"] = t.struct(
        {
            "effectiveValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunIn"])).optional(),
            "userEnteredValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "formattedValue": t.string().optional(),
            "effectiveFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableIn"]).optional(),
            "note": t.string().optional(),
            "hyperlink": t.string().optional(),
            "dataValidation": t.proxy(renames["DataValidationRuleIn"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableIn"]).optional(),
        }
    ).named(renames["CellDataIn"])
    types["CellDataOut"] = t.struct(
        {
            "effectiveValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunOut"])).optional(),
            "userEnteredValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "formattedValue": t.string().optional(),
            "effectiveFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableOut"]).optional(),
            "note": t.string().optional(),
            "hyperlink": t.string().optional(),
            "dataSourceFormula": t.proxy(renames["DataSourceFormulaOut"]).optional(),
            "dataValidation": t.proxy(renames["DataValidationRuleOut"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellDataOut"])
    types["DataFilterValueRangeIn"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterIn"]).optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "majorDimension": t.string().optional(),
        }
    ).named(renames["DataFilterValueRangeIn"])
    types["DataFilterValueRangeOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "majorDimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataFilterValueRangeOut"])
    types["DeleteConditionalFormatRuleResponseIn"] = t.struct(
        {"rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional()}
    ).named(renames["DeleteConditionalFormatRuleResponseIn"])
    types["DeleteConditionalFormatRuleResponseOut"] = t.struct(
        {
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConditionalFormatRuleResponseOut"])
    types["BatchUpdateValuesByDataFilterRequestIn"] = t.struct(
        {
            "responseValueRenderOption": t.string().optional(),
            "data": t.array(t.proxy(renames["DataFilterValueRangeIn"])).optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "valueInputOption": t.string().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestIn"])
    types["BatchUpdateValuesByDataFilterRequestOut"] = t.struct(
        {
            "responseValueRenderOption": t.string().optional(),
            "data": t.array(t.proxy(renames["DataFilterValueRangeOut"])).optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "valueInputOption": t.string().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestOut"])
    types["PaddingIn"] = t.struct(
        {
            "left": t.integer().optional(),
            "top": t.integer().optional(),
            "right": t.integer().optional(),
            "bottom": t.integer().optional(),
        }
    ).named(renames["PaddingIn"])
    types["PaddingOut"] = t.struct(
        {
            "left": t.integer().optional(),
            "top": t.integer().optional(),
            "right": t.integer().optional(),
            "bottom": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaddingOut"])
    types["SheetPropertiesIn"] = t.struct(
        {
            "hidden": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesIn"]).optional(),
            "index": t.integer().optional(),
            "title": t.string().optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "sheetType": t.string().optional(),
            "tabColor": t.proxy(renames["ColorIn"]).optional(),
            "rightToLeft": t.boolean().optional(),
        }
    ).named(renames["SheetPropertiesIn"])
    types["SheetPropertiesOut"] = t.struct(
        {
            "hidden": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesOut"]).optional(),
            "index": t.integer().optional(),
            "dataSourceSheetProperties": t.proxy(
                renames["DataSourceSheetPropertiesOut"]
            ).optional(),
            "title": t.string().optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "sheetType": t.string().optional(),
            "tabColor": t.proxy(renames["ColorOut"]).optional(),
            "rightToLeft": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetPropertiesOut"])
    types["AppendValuesResponseIn"] = t.struct(
        {
            "updates": t.proxy(renames["UpdateValuesResponseIn"]).optional(),
            "spreadsheetId": t.string().optional(),
            "tableRange": t.string().optional(),
        }
    ).named(renames["AppendValuesResponseIn"])
    types["AppendValuesResponseOut"] = t.struct(
        {
            "updates": t.proxy(renames["UpdateValuesResponseOut"]).optional(),
            "spreadsheetId": t.string().optional(),
            "tableRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendValuesResponseOut"])
    types["DuplicateSheetRequestIn"] = t.struct(
        {
            "newSheetId": t.integer().optional(),
            "insertSheetIndex": t.integer().optional(),
            "sourceSheetId": t.integer().optional(),
            "newSheetName": t.string().optional(),
        }
    ).named(renames["DuplicateSheetRequestIn"])
    types["DuplicateSheetRequestOut"] = t.struct(
        {
            "newSheetId": t.integer().optional(),
            "insertSheetIndex": t.integer().optional(),
            "sourceSheetId": t.integer().optional(),
            "newSheetName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetRequestOut"])
    types["BatchUpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseIn"])
            ).optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseIn"])
    types["BatchUpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseOut"])
            ).optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseOut"])
    types["WaterfallChartDomainIn"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataIn"]).optional(),
            "reversed": t.boolean().optional(),
        }
    ).named(renames["WaterfallChartDomainIn"])
    types["WaterfallChartDomainOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "reversed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartDomainOut"])
    types["DataSourceRefreshScheduleIn"] = t.struct(
        {
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleIn"]
            ).optional(),
            "refreshScope": t.string().optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleIn"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleIn"]
            ).optional(),
        }
    ).named(renames["DataSourceRefreshScheduleIn"])
    types["DataSourceRefreshScheduleOut"] = t.struct(
        {
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleOut"]
            ).optional(),
            "refreshScope": t.string().optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleOut"]
            ).optional(),
            "nextRun": t.proxy(renames["IntervalOut"]).optional(),
            "enabled": t.boolean().optional(),
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshScheduleOut"])
    types["UpdateDeveloperMetadataResponseIn"] = t.struct(
        {
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional()
        }
    ).named(renames["UpdateDeveloperMetadataResponseIn"])
    types["UpdateDeveloperMetadataResponseOut"] = t.struct(
        {
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataResponseOut"])
    types["AddBandingResponseIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingResponseIn"])
    types["AddBandingResponseOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingResponseOut"])
    types["CopySheetToAnotherSpreadsheetRequestIn"] = t.struct(
        {"destinationSpreadsheetId": t.string().optional()}
    ).named(renames["CopySheetToAnotherSpreadsheetRequestIn"])
    types["CopySheetToAnotherSpreadsheetRequestOut"] = t.struct(
        {
            "destinationSpreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopySheetToAnotherSpreadsheetRequestOut"])
    types["EditorsIn"] = t.struct(
        {
            "groups": t.array(t.string()).optional(),
            "users": t.array(t.string()).optional(),
            "domainUsersCanEdit": t.boolean().optional(),
        }
    ).named(renames["EditorsIn"])
    types["EditorsOut"] = t.struct(
        {
            "groups": t.array(t.string()).optional(),
            "users": t.array(t.string()).optional(),
            "domainUsersCanEdit": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditorsOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["BatchGetValuesByDataFilterResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "valueRanges": t.array(t.proxy(renames["MatchedValueRangeIn"])).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterResponseIn"])
    types["BatchGetValuesByDataFilterResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "valueRanges": t.array(t.proxy(renames["MatchedValueRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterResponseOut"])
    types["ChartSourceRangeIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["GridRangeIn"])).optional()}
    ).named(renames["ChartSourceRangeIn"])
    types["ChartSourceRangeOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSourceRangeOut"])
    types["UpdateConditionalFormatRuleRequestIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "newIndex": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestIn"])
    types["UpdateConditionalFormatRuleRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "newIndex": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestOut"])
    types["CandlestickDomainIn"] = t.struct(
        {
            "reversed": t.boolean().optional(),
            "data": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["CandlestickDomainIn"])
    types["CandlestickDomainOut"] = t.struct(
        {
            "reversed": t.boolean().optional(),
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickDomainOut"])
    types["ThemeColorPairIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorStyleIn"]).optional(),
            "colorType": t.string().optional(),
        }
    ).named(renames["ThemeColorPairIn"])
    types["ThemeColorPairOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorStyleOut"]).optional(),
            "colorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThemeColorPairOut"])
    types["RandomizeRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["RandomizeRangeRequestIn"])
    types["RandomizeRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RandomizeRangeRequestOut"])
    types["BatchGetValuesResponseIn"] = t.struct(
        {
            "valueRanges": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["BatchGetValuesResponseIn"])
    types["BatchGetValuesResponseOut"] = t.struct(
        {
            "valueRanges": t.array(t.proxy(renames["ValueRangeOut"])).optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesResponseOut"])
    types["AddDataSourceResponseIn"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceIn"]).optional(),
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
        }
    ).named(renames["AddDataSourceResponseIn"])
    types["AddDataSourceResponseOut"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDataSourceResponseOut"])
    types["DimensionPropertiesIn"] = t.struct(
        {
            "hiddenByUser": t.boolean().optional(),
            "pixelSize": t.integer().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "hiddenByFilter": t.boolean().optional(),
        }
    ).named(renames["DimensionPropertiesIn"])
    types["DimensionPropertiesOut"] = t.struct(
        {
            "hiddenByUser": t.boolean().optional(),
            "pixelSize": t.integer().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "hiddenByFilter": t.boolean().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionPropertiesOut"])
    types["BatchUpdateValuesResponseIn"] = t.struct(
        {
            "totalUpdatedSheets": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "responses": t.array(t.proxy(renames["UpdateValuesResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdateValuesResponseIn"])
    types["BatchUpdateValuesResponseOut"] = t.struct(
        {
            "totalUpdatedSheets": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesResponseOut"])
    types["HistogramRuleIn"] = t.struct(
        {
            "interval": t.number().optional(),
            "end": t.number().optional(),
            "start": t.number().optional(),
        }
    ).named(renames["HistogramRuleIn"])
    types["HistogramRuleOut"] = t.struct(
        {
            "interval": t.number().optional(),
            "end": t.number().optional(),
            "start": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramRuleOut"])
    types["TrimWhitespaceResponseIn"] = t.struct(
        {"cellsChangedCount": t.integer().optional()}
    ).named(renames["TrimWhitespaceResponseIn"])
    types["TrimWhitespaceResponseOut"] = t.struct(
        {
            "cellsChangedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceResponseOut"])
    types["ValueRangeIn"] = t.struct(
        {
            "range": t.string().optional(),
            "majorDimension": t.string().optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
        }
    ).named(renames["ValueRangeIn"])
    types["ValueRangeOut"] = t.struct(
        {
            "range": t.string().optional(),
            "majorDimension": t.string().optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueRangeOut"])
    types["PasteDataRequestIn"] = t.struct(
        {
            "coordinate": t.proxy(renames["GridCoordinateIn"]).optional(),
            "type": t.string().optional(),
            "data": t.string().optional(),
            "html": t.boolean().optional(),
            "delimiter": t.string().optional(),
        }
    ).named(renames["PasteDataRequestIn"])
    types["PasteDataRequestOut"] = t.struct(
        {
            "coordinate": t.proxy(renames["GridCoordinateOut"]).optional(),
            "type": t.string().optional(),
            "data": t.string().optional(),
            "html": t.boolean().optional(),
            "delimiter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasteDataRequestOut"])
    types["UpdateDimensionPropertiesRequestIn"] = t.struct(
        {
            "properties": t.proxy(renames["DimensionPropertiesIn"]).optional(),
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
            "fields": t.string().optional(),
            "dataSourceSheetRange": t.proxy(
                renames["DataSourceSheetDimensionRangeIn"]
            ).optional(),
        }
    ).named(renames["UpdateDimensionPropertiesRequestIn"])
    types["UpdateDimensionPropertiesRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["DimensionPropertiesOut"]).optional(),
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "fields": t.string().optional(),
            "dataSourceSheetRange": t.proxy(
                renames["DataSourceSheetDimensionRangeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDimensionPropertiesRequestOut"])
    types["DataExecutionStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "errorMessage": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "errorCode": t.string().optional(),
        }
    ).named(renames["DataExecutionStatusIn"])
    types["DataExecutionStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "errorMessage": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "errorCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataExecutionStatusOut"])
    types["ChartDateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ChartDateTimeRuleIn"]
    )
    types["ChartDateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDateTimeRuleOut"])
    types["BordersIn"] = t.struct(
        {
            "right": t.proxy(renames["BorderIn"]).optional(),
            "left": t.proxy(renames["BorderIn"]).optional(),
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["BordersIn"])
    types["BordersOut"] = t.struct(
        {
            "right": t.proxy(renames["BorderOut"]).optional(),
            "left": t.proxy(renames["BorderOut"]).optional(),
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BordersOut"])
    types["KeyValueFormatIn"] = t.struct(
        {
            "position": t.proxy(renames["TextPositionIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
        }
    ).named(renames["KeyValueFormatIn"])
    types["KeyValueFormatOut"] = t.struct(
        {
            "position": t.proxy(renames["TextPositionOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueFormatOut"])
    types["ManualRuleIn"] = t.struct(
        {"groups": t.array(t.proxy(renames["ManualRuleGroupIn"])).optional()}
    ).named(renames["ManualRuleIn"])
    types["ManualRuleOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["ManualRuleGroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualRuleOut"])
    types["SpreadsheetIn"] = t.struct(
        {
            "spreadsheetUrl": t.string().optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
            "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["SpreadsheetIn"])
    types["SpreadsheetOut"] = t.struct(
        {
            "spreadsheetUrl": t.string().optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "dataSourceSchedules": t.array(
                t.proxy(renames["DataSourceRefreshScheduleOut"])
            ).optional(),
            "sheets": t.array(t.proxy(renames["SheetOut"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesOut"]).optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeOut"])).optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetOut"])
    types["RequestIn"] = t.struct(
        {
            "updateBorders": t.proxy(renames["UpdateBordersRequestIn"]).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestIn"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestIn"]
            ).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestIn"]).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestIn"]
            ).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestIn"]
            ).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestIn"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestIn"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestIn"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestIn"]
            ).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestIn"]
            ).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestIn"]
            ).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestIn"]
            ).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestIn"]).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestIn"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestIn"]
            ).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestIn"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestIn"]).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestIn"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestIn"]
            ).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestIn"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestIn"]
            ).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestIn"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestIn"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestIn"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestIn"]).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestIn"]).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestIn"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestIn"]).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestIn"]
            ).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestIn"]).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestIn"]
            ).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestIn"]
            ).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestIn"]
            ).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestIn"]
            ).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestIn"]
            ).optional(),
            "pasteData": t.proxy(renames["PasteDataRequestIn"]).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestIn"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestIn"]
            ).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestIn"]).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestIn"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestIn"]).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestIn"]
            ).optional(),
            "copyPaste": t.proxy(renames["CopyPasteRequestIn"]).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestIn"]
            ).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestIn"]).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestIn"]
            ).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestIn"]).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestIn"]).optional(),
            "updateBanding": t.proxy(renames["UpdateBandingRequestIn"]).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestIn"]).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestIn"]).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestIn"]
            ).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestIn"]).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestIn"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestIn"]).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestIn"]).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestIn"]).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestIn"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestIn"]).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestIn"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestIn"]).optional(),
            "addChart": t.proxy(renames["AddChartRequestIn"]).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestIn"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "updateBorders": t.proxy(renames["UpdateBordersRequestOut"]).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestOut"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestOut"]
            ).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestOut"]).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestOut"]
            ).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestOut"]
            ).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestOut"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestOut"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestOut"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestOut"]
            ).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestOut"]
            ).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestOut"]
            ).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestOut"]
            ).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestOut"]).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestOut"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestOut"]
            ).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestOut"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestOut"]).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestOut"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestOut"]
            ).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestOut"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestOut"]
            ).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestOut"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestOut"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestOut"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestOut"]).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestOut"]).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestOut"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestOut"]).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestOut"]
            ).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestOut"]).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestOut"]
            ).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestOut"]
            ).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestOut"]
            ).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestOut"]
            ).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestOut"]
            ).optional(),
            "pasteData": t.proxy(renames["PasteDataRequestOut"]).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestOut"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestOut"]
            ).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestOut"]).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestOut"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestOut"]).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestOut"]
            ).optional(),
            "copyPaste": t.proxy(renames["CopyPasteRequestOut"]).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestOut"]
            ).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestOut"]).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestOut"]
            ).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestOut"]).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestOut"]).optional(),
            "updateBanding": t.proxy(renames["UpdateBandingRequestOut"]).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestOut"]).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestOut"]).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestOut"]
            ).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestOut"]).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestOut"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestOut"]).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestOut"]).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestOut"]).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestOut"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestOut"]).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestOut"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestOut"]).optional(),
            "addChart": t.proxy(renames["AddChartRequestOut"]).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestOut"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["AddDimensionGroupResponseIn"] = t.struct(
        {"dimensionGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional()}
    ).named(renames["AddDimensionGroupResponseIn"])
    types["AddDimensionGroupResponseOut"] = t.struct(
        {
            "dimensionGroups": t.array(
                t.proxy(renames["DimensionGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDimensionGroupResponseOut"])
    types["NamedRangeIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "namedRangeId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["NamedRangeIn"])
    types["NamedRangeOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "namedRangeId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedRangeOut"])
    types["DataSourceFormulaIn"] = t.struct(
        {"dataSourceId": t.string().optional()}
    ).named(renames["DataSourceFormulaIn"])
    types["DataSourceFormulaOut"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceFormulaOut"])
    types["AddFilterViewRequestIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewRequestIn"])
    types["AddFilterViewRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewRequestOut"])
    types["DataLabelIn"] = t.struct(
        {
            "customLabelData": t.proxy(renames["ChartDataIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "type": t.string().optional(),
            "placement": t.string().optional(),
        }
    ).named(renames["DataLabelIn"])
    types["DataLabelOut"] = t.struct(
        {
            "customLabelData": t.proxy(renames["ChartDataOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "type": t.string().optional(),
            "placement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLabelOut"])
    types["UpdateSlicerSpecRequestIn"] = t.struct(
        {
            "slicerId": t.integer().optional(),
            "fields": t.string().optional(),
            "spec": t.proxy(renames["SlicerSpecIn"]).optional(),
        }
    ).named(renames["UpdateSlicerSpecRequestIn"])
    types["UpdateSlicerSpecRequestOut"] = t.struct(
        {
            "slicerId": t.integer().optional(),
            "fields": t.string().optional(),
            "spec": t.proxy(renames["SlicerSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlicerSpecRequestOut"])
    types["UpdateValuesResponseIn"] = t.struct(
        {
            "updatedColumns": t.integer().optional(),
            "updatedCells": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["UpdateValuesResponseIn"])
    types["UpdateValuesResponseOut"] = t.struct(
        {
            "updatedColumns": t.integer().optional(),
            "updatedCells": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesResponseOut"])
    types["TreemapChartSpecIn"] = t.struct(
        {
            "hintedLevels": t.integer().optional(),
            "maxValue": t.number().optional(),
            "colorScale": t.proxy(renames["TreemapChartColorScaleIn"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "levels": t.integer().optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "colorData": t.proxy(renames["ChartDataIn"]).optional(),
            "sizeData": t.proxy(renames["ChartDataIn"]).optional(),
            "minValue": t.number().optional(),
        }
    ).named(renames["TreemapChartSpecIn"])
    types["TreemapChartSpecOut"] = t.struct(
        {
            "hintedLevels": t.integer().optional(),
            "maxValue": t.number().optional(),
            "colorScale": t.proxy(renames["TreemapChartColorScaleOut"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "levels": t.integer().optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "colorData": t.proxy(renames["ChartDataOut"]).optional(),
            "sizeData": t.proxy(renames["ChartDataOut"]).optional(),
            "minValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartSpecOut"])
    types["UpdateProtectedRangeRequestIn"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateProtectedRangeRequestIn"])
    types["UpdateProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateProtectedRangeRequestOut"])
    types["DeleteDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionGroupRequestIn"])
    types["DeleteDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionGroupRequestOut"])
    types["DeleteDimensionGroupResponseIn"] = t.struct(
        {"dimensionGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional()}
    ).named(renames["DeleteDimensionGroupResponseIn"])
    types["DeleteDimensionGroupResponseOut"] = t.struct(
        {
            "dimensionGroups": t.array(
                t.proxy(renames["DimensionGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionGroupResponseOut"])
    types["UpdateSheetPropertiesRequestIn"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateSheetPropertiesRequestIn"])
    types["UpdateSheetPropertiesRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSheetPropertiesRequestOut"])
    types["GridCoordinateIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
        }
    ).named(renames["GridCoordinateIn"])
    types["GridCoordinateOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridCoordinateOut"])
    types["DataValidationRuleIn"] = t.struct(
        {
            "strict": t.boolean().optional(),
            "showCustomUi": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "inputMessage": t.string().optional(),
        }
    ).named(renames["DataValidationRuleIn"])
    types["DataValidationRuleOut"] = t.struct(
        {
            "strict": t.boolean().optional(),
            "showCustomUi": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "inputMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataValidationRuleOut"])
    types["BigQueryTableSpecIn"] = t.struct(
        {
            "tableProjectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
        }
    ).named(renames["BigQueryTableSpecIn"])
    types["BigQueryTableSpecOut"] = t.struct(
        {
            "tableProjectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryTableSpecOut"])
    types["DeleteBandingRequestIn"] = t.struct(
        {"bandedRangeId": t.integer().optional()}
    ).named(renames["DeleteBandingRequestIn"])
    types["DeleteBandingRequestOut"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBandingRequestOut"])
    types["UpdateDeveloperMetadataRequestIn"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestIn"])
    types["UpdateDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestOut"])
    types["ConditionalFormatRuleIn"] = t.struct(
        {
            "ranges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "gradientRule": t.proxy(renames["GradientRuleIn"]).optional(),
            "booleanRule": t.proxy(renames["BooleanRuleIn"]).optional(),
        }
    ).named(renames["ConditionalFormatRuleIn"])
    types["ConditionalFormatRuleOut"] = t.struct(
        {
            "ranges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "gradientRule": t.proxy(renames["GradientRuleOut"]).optional(),
            "booleanRule": t.proxy(renames["BooleanRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionalFormatRuleOut"])
    types["WaterfallChartSeriesIn"] = t.struct(
        {
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "data": t.proxy(renames["ChartDataIn"]).optional(),
            "hideTrailingSubtotal": t.boolean().optional(),
            "subtotalColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "positiveColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "customSubtotals": t.array(
                t.proxy(renames["WaterfallChartCustomSubtotalIn"])
            ).optional(),
        }
    ).named(renames["WaterfallChartSeriesIn"])
    types["WaterfallChartSeriesOut"] = t.struct(
        {
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "hideTrailingSubtotal": t.boolean().optional(),
            "subtotalColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "positiveColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "customSubtotals": t.array(
                t.proxy(renames["WaterfallChartCustomSubtotalOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSeriesOut"])
    types["DimensionRangeIn"] = t.struct(
        {
            "dimension": t.string().optional(),
            "endIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["DimensionRangeIn"])
    types["DimensionRangeOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "endIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionRangeOut"])
    types["DeleteProtectedRangeRequestIn"] = t.struct(
        {"protectedRangeId": t.integer().optional()}
    ).named(renames["DeleteProtectedRangeRequestIn"])
    types["DeleteProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteProtectedRangeRequestOut"])
    types["BasicSeriesDataPointStyleOverrideIn"] = t.struct(
        {
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideIn"])
    types["BasicSeriesDataPointStyleOverrideOut"] = t.struct(
        {
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideOut"])
    types["SortSpecIn"] = t.struct(
        {
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "sortOrder": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "dimensionIndex": t.integer().optional(),
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
        }
    ).named(renames["SortSpecIn"])
    types["SortSpecOut"] = t.struct(
        {
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "sortOrder": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "dimensionIndex": t.integer().optional(),
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortSpecOut"])
    types["DataSourceRefreshWeeklyScheduleIn"] = t.struct(
        {
            "daysOfWeek": t.array(t.string()).optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DataSourceRefreshWeeklyScheduleIn"])
    types["DataSourceRefreshWeeklyScheduleOut"] = t.struct(
        {
            "daysOfWeek": t.array(t.string()).optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshWeeklyScheduleOut"])
    types["DeveloperMetadataLookupIn"] = t.struct(
        {
            "visibility": t.string().optional(),
            "metadataKey": t.string().optional(),
            "metadataId": t.integer().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationIn"]
            ).optional(),
            "locationMatchingStrategy": t.string().optional(),
            "locationType": t.string().optional(),
            "metadataValue": t.string().optional(),
        }
    ).named(renames["DeveloperMetadataLookupIn"])
    types["DeveloperMetadataLookupOut"] = t.struct(
        {
            "visibility": t.string().optional(),
            "metadataKey": t.string().optional(),
            "metadataId": t.integer().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationOut"]
            ).optional(),
            "locationMatchingStrategy": t.string().optional(),
            "locationType": t.string().optional(),
            "metadataValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLookupOut"])
    types["DeleteRangeRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "shiftDimension": t.string().optional(),
        }
    ).named(renames["DeleteRangeRequestIn"])
    types["DeleteRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "shiftDimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteRangeRequestOut"])
    types["OrgChartSpecIn"] = t.struct(
        {
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "tooltips": t.proxy(renames["ChartDataIn"]).optional(),
            "nodeColor": t.proxy(renames["ColorIn"]).optional(),
            "selectedNodeColor": t.proxy(renames["ColorIn"]).optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "nodeSize": t.string().optional(),
        }
    ).named(renames["OrgChartSpecIn"])
    types["OrgChartSpecOut"] = t.struct(
        {
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "tooltips": t.proxy(renames["ChartDataOut"]).optional(),
            "nodeColor": t.proxy(renames["ColorOut"]).optional(),
            "selectedNodeColor": t.proxy(renames["ColorOut"]).optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "nodeSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgChartSpecOut"])
    types["ScorecardChartSpecIn"] = t.struct(
        {
            "keyValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "numberFormatSource": t.string().optional(),
            "keyValueFormat": t.proxy(renames["KeyValueFormatIn"]).optional(),
            "aggregateType": t.string().optional(),
            "scaleFactor": t.number().optional(),
            "baselineValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "baselineValueFormat": t.proxy(renames["BaselineValueFormatIn"]).optional(),
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsIn"]
            ).optional(),
        }
    ).named(renames["ScorecardChartSpecIn"])
    types["ScorecardChartSpecOut"] = t.struct(
        {
            "keyValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "numberFormatSource": t.string().optional(),
            "keyValueFormat": t.proxy(renames["KeyValueFormatOut"]).optional(),
            "aggregateType": t.string().optional(),
            "scaleFactor": t.number().optional(),
            "baselineValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "baselineValueFormat": t.proxy(
                renames["BaselineValueFormatOut"]
            ).optional(),
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScorecardChartSpecOut"])
    types["TextPositionIn"] = t.struct(
        {"horizontalAlignment": t.string().optional()}
    ).named(renames["TextPositionIn"])
    types["TextPositionOut"] = t.struct(
        {
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPositionOut"])
    types["PieChartSpecIn"] = t.struct(
        {
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
            "pieHole": t.number().optional(),
            "threeDimensional": t.boolean().optional(),
            "legendPosition": t.string().optional(),
        }
    ).named(renames["PieChartSpecIn"])
    types["PieChartSpecOut"] = t.struct(
        {
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "pieHole": t.number().optional(),
            "threeDimensional": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PieChartSpecOut"])
    types["WaterfallChartCustomSubtotalIn"] = t.struct(
        {
            "subtotalIndex": t.integer().optional(),
            "dataIsSubtotal": t.boolean().optional(),
            "label": t.string().optional(),
        }
    ).named(renames["WaterfallChartCustomSubtotalIn"])
    types["WaterfallChartCustomSubtotalOut"] = t.struct(
        {
            "subtotalIndex": t.integer().optional(),
            "dataIsSubtotal": t.boolean().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartCustomSubtotalOut"])
    types["ManualRuleGroupIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ExtendedValueIn"])).optional(),
            "groupName": t.proxy(renames["ExtendedValueIn"]).optional(),
        }
    ).named(renames["ManualRuleGroupIn"])
    types["ManualRuleGroupOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ExtendedValueOut"])).optional(),
            "groupName": t.proxy(renames["ExtendedValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualRuleGroupOut"])
    types["MatchedDeveloperMetadataIn"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
        }
    ).named(renames["MatchedDeveloperMetadataIn"])
    types["MatchedDeveloperMetadataOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchedDeveloperMetadataOut"])
    types["PivotGroupSortValueBucketIn"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["ExtendedValueIn"])).optional(),
            "valuesIndex": t.integer().optional(),
        }
    ).named(renames["PivotGroupSortValueBucketIn"])
    types["PivotGroupSortValueBucketOut"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["ExtendedValueOut"])).optional(),
            "valuesIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupSortValueBucketOut"])
    types["PivotValueIn"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "formula": t.string().optional(),
            "name": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "summarizeFunction": t.string().optional(),
            "calculatedDisplayType": t.string().optional(),
        }
    ).named(renames["PivotValueIn"])
    types["PivotValueOut"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "formula": t.string().optional(),
            "name": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "summarizeFunction": t.string().optional(),
            "calculatedDisplayType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueOut"])
    types["LinkIn"] = t.struct({"uri": t.string().optional()}).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["WaterfallChartSpecIn"] = t.struct(
        {
            "firstValueIsTotal": t.boolean().optional(),
            "domain": t.proxy(renames["WaterfallChartDomainIn"]).optional(),
            "series": t.array(t.proxy(renames["WaterfallChartSeriesIn"])).optional(),
            "stackedType": t.string().optional(),
            "hideConnectorLines": t.boolean().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "connectorLineStyle": t.proxy(renames["LineStyleIn"]).optional(),
        }
    ).named(renames["WaterfallChartSpecIn"])
    types["WaterfallChartSpecOut"] = t.struct(
        {
            "firstValueIsTotal": t.boolean().optional(),
            "domain": t.proxy(renames["WaterfallChartDomainOut"]).optional(),
            "series": t.array(t.proxy(renames["WaterfallChartSeriesOut"])).optional(),
            "stackedType": t.string().optional(),
            "hideConnectorLines": t.boolean().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "connectorLineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSpecOut"])
    types["RowDataIn"] = t.struct(
        {"values": t.array(t.proxy(renames["CellDataIn"])).optional()}
    ).named(renames["RowDataIn"])
    types["RowDataOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CellDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowDataOut"])
    types["AddSlicerResponseIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerResponseIn"])
    types["AddSlicerResponseOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerResponseOut"])
    types["DeleteDimensionRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionRequestIn"])
    types["DeleteDimensionRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionRequestOut"])
    types["AppendDimensionRequestIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "length": t.integer().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["AppendDimensionRequestIn"])
    types["AppendDimensionRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "length": t.integer().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendDimensionRequestOut"])
    types["EmbeddedObjectBorderIn"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderIn"])
    types["EmbeddedObjectBorderOut"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderOut"])
    types["DataSourceChartPropertiesIn"] = t.struct(
        {"dataSourceId": t.string().optional()}
    ).named(renames["DataSourceChartPropertiesIn"])
    types["DataSourceChartPropertiesOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceChartPropertiesOut"])
    types["DataSourceIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "spec": t.proxy(renames["DataSourceSpecIn"]).optional(),
            "calculatedColumns": t.array(
                t.proxy(renames["DataSourceColumnIn"])
            ).optional(),
            "dataSourceId": t.string().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "spec": t.proxy(renames["DataSourceSpecOut"]).optional(),
            "calculatedColumns": t.array(
                t.proxy(renames["DataSourceColumnOut"])
            ).optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["AddConditionalFormatRuleRequestIn"] = t.struct(
        {
            "rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["AddConditionalFormatRuleRequestIn"])
    types["AddConditionalFormatRuleRequestOut"] = t.struct(
        {
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddConditionalFormatRuleRequestOut"])
    types["UpdateBordersRequestIn"] = t.struct(
        {
            "right": t.proxy(renames["BorderIn"]).optional(),
            "left": t.proxy(renames["BorderIn"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
            "innerVertical": t.proxy(renames["BorderIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "bottom": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["UpdateBordersRequestIn"])
    types["UpdateBordersRequestOut"] = t.struct(
        {
            "right": t.proxy(renames["BorderOut"]).optional(),
            "left": t.proxy(renames["BorderOut"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "innerVertical": t.proxy(renames["BorderOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBordersRequestOut"])
    types["AddBandingRequestIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingRequestIn"])
    types["AddBandingRequestOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingRequestOut"])
    types["DataSourceObjectReferenceIn"] = t.struct(
        {
            "sheetId": t.string().optional(),
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
            "chartId": t.integer().optional(),
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
        }
    ).named(renames["DataSourceObjectReferenceIn"])
    types["DataSourceObjectReferenceOut"] = t.struct(
        {
            "sheetId": t.string().optional(),
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "chartId": t.integer().optional(),
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceObjectReferenceOut"])
    types["SlicerIn"] = t.struct(
        {
            "spec": t.proxy(renames["SlicerSpecIn"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "slicerId": t.integer().optional(),
        }
    ).named(renames["SlicerIn"])
    types["SlicerOut"] = t.struct(
        {
            "spec": t.proxy(renames["SlicerSpecOut"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "slicerId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerOut"])
    types["GridDataIn"] = t.struct(
        {
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
            "startColumn": t.integer().optional(),
            "rowData": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
            "startRow": t.integer().optional(),
        }
    ).named(renames["GridDataIn"])
    types["GridDataOut"] = t.struct(
        {
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "startColumn": t.integer().optional(),
            "rowData": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "startRow": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridDataOut"])
    types["CandlestickChartSpecIn"] = t.struct(
        {
            "domain": t.proxy(renames["CandlestickDomainIn"]).optional(),
            "data": t.array(t.proxy(renames["CandlestickDataIn"])).optional(),
        }
    ).named(renames["CandlestickChartSpecIn"])
    types["CandlestickChartSpecOut"] = t.struct(
        {
            "domain": t.proxy(renames["CandlestickDomainOut"]).optional(),
            "data": t.array(t.proxy(renames["CandlestickDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickChartSpecOut"])
    types["BatchClearValuesByDataFilterRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["BatchClearValuesByDataFilterRequestIn"])
    types["BatchClearValuesByDataFilterRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterRequestOut"])
    types["AddNamedRangeRequestIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeRequestIn"])
    types["AddNamedRangeRequestOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeRequestOut"])
    types["DataSourceRefreshDailyScheduleIn"] = t.struct(
        {"startTime": t.proxy(renames["TimeOfDayIn"]).optional()}
    ).named(renames["DataSourceRefreshDailyScheduleIn"])
    types["DataSourceRefreshDailyScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshDailyScheduleOut"])
    types["PivotTableIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["PivotValueIn"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "rows": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "valueLayout": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecIn"])).optional(),
        }
    ).named(renames["PivotTableIn"])
    types["PivotTableOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["PivotValueOut"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "rows": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "valueLayout": t.string().optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotTableOut"])
    types["ConditionValueIn"] = t.struct(
        {
            "userEnteredValue": t.string().optional(),
            "relativeDate": t.string().optional(),
        }
    ).named(renames["ConditionValueIn"])
    types["ConditionValueOut"] = t.struct(
        {
            "userEnteredValue": t.string().optional(),
            "relativeDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionValueOut"])
    types["SortRangeRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
        }
    ).named(renames["SortRangeRequestIn"])
    types["SortRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortRangeRequestOut"])
    types["ResponseIn"] = t.struct(
        {
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseIn"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseIn"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseIn"]
            ).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseIn"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseIn"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseIn"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseIn"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseIn"]
            ).optional(),
            "addSheet": t.proxy(renames["AddSheetResponseIn"]).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseIn"]).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseIn"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseIn"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseIn"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseIn"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingResponseIn"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseIn"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseIn"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseIn"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseIn"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseIn"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseIn"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseIn"]).optional(),
            "addChart": t.proxy(renames["AddChartResponseIn"]).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseOut"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseOut"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseOut"]
            ).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseOut"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseOut"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseOut"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseOut"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseOut"]
            ).optional(),
            "addSheet": t.proxy(renames["AddSheetResponseOut"]).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseOut"]).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseOut"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseOut"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseOut"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseOut"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingResponseOut"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseOut"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseOut"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseOut"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseOut"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseOut"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseOut"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseOut"]).optional(),
            "addChart": t.proxy(renames["AddChartResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["UpdateDataSourceResponseIn"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
            "dataSource": t.proxy(renames["DataSourceIn"]).optional(),
        }
    ).named(renames["UpdateDataSourceResponseIn"])
    types["UpdateDataSourceResponseOut"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDataSourceResponseOut"])
    types["RefreshDataSourceRequestIn"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "isAll": t.boolean().optional(),
            "force": t.boolean().optional(),
            "references": t.proxy(renames["DataSourceObjectReferencesIn"]).optional(),
        }
    ).named(renames["RefreshDataSourceRequestIn"])
    types["RefreshDataSourceRequestOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "isAll": t.boolean().optional(),
            "force": t.boolean().optional(),
            "references": t.proxy(renames["DataSourceObjectReferencesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshDataSourceRequestOut"])
    types["CandlestickSeriesIn"] = t.struct(
        {"data": t.proxy(renames["ChartDataIn"]).optional()}
    ).named(renames["CandlestickSeriesIn"])
    types["CandlestickSeriesOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickSeriesOut"])
    types["MoveDimensionRequestIn"] = t.struct(
        {
            "destinationIndex": t.integer().optional(),
            "source": t.proxy(renames["DimensionRangeIn"]).optional(),
        }
    ).named(renames["MoveDimensionRequestIn"])
    types["MoveDimensionRequestOut"] = t.struct(
        {
            "destinationIndex": t.integer().optional(),
            "source": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveDimensionRequestOut"])
    types["AddSheetRequestIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetRequestIn"])
    types["AddSheetRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetRequestOut"])
    types["AutoFillRequestIn"] = t.struct(
        {
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationIn"]
            ).optional(),
            "useAlternateSeries": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["AutoFillRequestIn"])
    types["AutoFillRequestOut"] = t.struct(
        {
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationOut"]
            ).optional(),
            "useAlternateSeries": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoFillRequestOut"])
    types["ChartGroupRuleIn"] = t.struct(
        {
            "histogramRule": t.proxy(renames["ChartHistogramRuleIn"]).optional(),
            "dateTimeRule": t.proxy(renames["ChartDateTimeRuleIn"]).optional(),
        }
    ).named(renames["ChartGroupRuleIn"])
    types["ChartGroupRuleOut"] = t.struct(
        {
            "histogramRule": t.proxy(renames["ChartHistogramRuleOut"]).optional(),
            "dateTimeRule": t.proxy(renames["ChartDateTimeRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartGroupRuleOut"])
    types["IntervalIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["IntervalIn"])
    types["IntervalOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntervalOut"])
    types["AddDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["AddDimensionGroupRequestIn"])
    types["AddDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDimensionGroupRequestOut"])
    types["UpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
            "updatedCells": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedColumns": t.integer().optional(),
            "dataFilter": t.proxy(renames["DataFilterIn"]).optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseIn"])
    types["UpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "updatedCells": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedColumns": t.integer().optional(),
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseOut"])
    types["SetDataValidationRequestIn"] = t.struct(
        {
            "rule": t.proxy(renames["DataValidationRuleIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["SetDataValidationRequestIn"])
    types["SetDataValidationRequestOut"] = t.struct(
        {
            "rule": t.proxy(renames["DataValidationRuleOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetDataValidationRequestOut"])
    types["BatchClearValuesResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "clearedRanges": t.array(t.string()).optional(),
        }
    ).named(renames["BatchClearValuesResponseIn"])
    types["BatchClearValuesResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "clearedRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesResponseOut"])
    types["DeveloperMetadataIn"] = t.struct(
        {
            "metadataKey": t.string().optional(),
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "metadataId": t.integer().optional(),
            "location": t.proxy(renames["DeveloperMetadataLocationIn"]).optional(),
        }
    ).named(renames["DeveloperMetadataIn"])
    types["DeveloperMetadataOut"] = t.struct(
        {
            "metadataKey": t.string().optional(),
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "metadataId": t.integer().optional(),
            "location": t.proxy(renames["DeveloperMetadataLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataOut"])
    types["UnmergeCellsRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["UnmergeCellsRequestIn"])
    types["UnmergeCellsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeCellsRequestOut"])
    types["BooleanRuleIn"] = t.struct(
        {
            "format": t.proxy(renames["CellFormatIn"]).optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
        }
    ).named(renames["BooleanRuleIn"])
    types["BooleanRuleOut"] = t.struct(
        {
            "format": t.proxy(renames["CellFormatOut"]).optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanRuleOut"])
    types["BandedRangeIn"] = t.struct(
        {
            "rowProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
            "columnProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
            "bandedRangeId": t.integer().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["BandedRangeIn"])
    types["BandedRangeOut"] = t.struct(
        {
            "rowProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "columnProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "bandedRangeId": t.integer().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandedRangeOut"])
    types["ClearValuesResponseIn"] = t.struct(
        {"clearedRange": t.string().optional(), "spreadsheetId": t.string().optional()}
    ).named(renames["ClearValuesResponseIn"])
    types["ClearValuesResponseOut"] = t.struct(
        {
            "clearedRange": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearValuesResponseOut"])
    types["FilterSpecIn"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
            "columnIndex": t.integer().optional(),
        }
    ).named(renames["FilterSpecIn"])
    types["FilterSpecOut"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "columnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterSpecOut"])
    types["AddNamedRangeResponseIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeResponseIn"])
    types["AddNamedRangeResponseOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeResponseOut"])
    types["RefreshDataSourceObjectExecutionStatusIn"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
            "reference": t.proxy(renames["DataSourceObjectReferenceIn"]).optional(),
        }
    ).named(renames["RefreshDataSourceObjectExecutionStatusIn"])
    types["RefreshDataSourceObjectExecutionStatusOut"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "reference": t.proxy(renames["DataSourceObjectReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshDataSourceObjectExecutionStatusOut"])
    types["UpdateDimensionGroupRequestIn"] = t.struct(
        {
            "dimensionGroup": t.proxy(renames["DimensionGroupIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateDimensionGroupRequestIn"])
    types["UpdateDimensionGroupRequestOut"] = t.struct(
        {
            "dimensionGroup": t.proxy(renames["DimensionGroupOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDimensionGroupRequestOut"])
    types["BooleanConditionIn"] = t.struct(
        {
            "type": t.string().optional(),
            "values": t.array(t.proxy(renames["ConditionValueIn"])).optional(),
        }
    ).named(renames["BooleanConditionIn"])
    types["BooleanConditionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "values": t.array(t.proxy(renames["ConditionValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanConditionOut"])
    types["SearchDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["SearchDeveloperMetadataRequestIn"])
    types["SearchDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDeveloperMetadataRequestOut"])
    types["UpdateEmbeddedObjectBorderRequestIn"] = t.struct(
        {
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.integer().optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestIn"])
    types["UpdateEmbeddedObjectBorderRequestOut"] = t.struct(
        {
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestOut"])
    types["DeleteDeveloperMetadataResponseIn"] = t.struct(
        {
            "deletedDeveloperMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional()
        }
    ).named(renames["DeleteDeveloperMetadataResponseIn"])
    types["DeleteDeveloperMetadataResponseOut"] = t.struct(
        {
            "deletedDeveloperMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDeveloperMetadataResponseOut"])
    types["WaterfallChartColumnStyleIn"] = t.struct(
        {
            "label": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["WaterfallChartColumnStyleIn"])
    types["WaterfallChartColumnStyleOut"] = t.struct(
        {
            "label": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartColumnStyleOut"])
    types["DeleteEmbeddedObjectRequestIn"] = t.struct(
        {"objectId": t.integer().optional()}
    ).named(renames["DeleteEmbeddedObjectRequestIn"])
    types["DeleteEmbeddedObjectRequestOut"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteEmbeddedObjectRequestOut"])
    types["CellFormatIn"] = t.struct(
        {
            "textRotation": t.proxy(renames["TextRotationIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "padding": t.proxy(renames["PaddingIn"]).optional(),
            "textDirection": t.string().optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "verticalAlignment": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "wrapStrategy": t.string().optional(),
            "borders": t.proxy(renames["BordersIn"]).optional(),
            "numberFormat": t.proxy(renames["NumberFormatIn"]).optional(),
        }
    ).named(renames["CellFormatIn"])
    types["CellFormatOut"] = t.struct(
        {
            "textRotation": t.proxy(renames["TextRotationOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "padding": t.proxy(renames["PaddingOut"]).optional(),
            "textDirection": t.string().optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "verticalAlignment": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "wrapStrategy": t.string().optional(),
            "borders": t.proxy(renames["BordersOut"]).optional(),
            "numberFormat": t.proxy(renames["NumberFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellFormatOut"])
    types["BandingPropertiesIn"] = t.struct(
        {
            "firstBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "firstBandColor": t.proxy(renames["ColorIn"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "footerColor": t.proxy(renames["ColorIn"]).optional(),
            "secondBandColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["BandingPropertiesIn"])
    types["BandingPropertiesOut"] = t.struct(
        {
            "firstBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "firstBandColor": t.proxy(renames["ColorOut"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "footerColor": t.proxy(renames["ColorOut"]).optional(),
            "secondBandColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandingPropertiesOut"])
    types["DeveloperMetadataLocationIn"] = t.struct(
        {
            "spreadsheet": t.boolean().optional(),
            "locationType": t.string().optional(),
            "sheetId": t.integer().optional(),
            "dimensionRange": t.proxy(renames["DimensionRangeIn"]).optional(),
        }
    ).named(renames["DeveloperMetadataLocationIn"])
    types["DeveloperMetadataLocationOut"] = t.struct(
        {
            "spreadsheet": t.boolean().optional(),
            "locationType": t.string().optional(),
            "sheetId": t.integer().optional(),
            "dimensionRange": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLocationOut"])
    types["DimensionGroupIn"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
            "depth": t.integer().optional(),
            "collapsed": t.boolean().optional(),
        }
    ).named(renames["DimensionGroupIn"])
    types["DimensionGroupOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "depth": t.integer().optional(),
            "collapsed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionGroupOut"])
    types["SourceAndDestinationIn"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "dimension": t.string().optional(),
            "fillLength": t.integer().optional(),
        }
    ).named(renames["SourceAndDestinationIn"])
    types["SourceAndDestinationOut"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "dimension": t.string().optional(),
            "fillLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceAndDestinationOut"])
    types["ChartHistogramRuleIn"] = t.struct(
        {
            "intervalSize": t.number().optional(),
            "maxValue": t.number().optional(),
            "minValue": t.number().optional(),
        }
    ).named(renames["ChartHistogramRuleIn"])
    types["ChartHistogramRuleOut"] = t.struct(
        {
            "intervalSize": t.number().optional(),
            "maxValue": t.number().optional(),
            "minValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartHistogramRuleOut"])
    types["SheetIn"] = t.struct(
        {
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "data": t.array(t.proxy(renames["GridDataIn"])).optional(),
            "columnGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartIn"])).optional(),
            "protectedRanges": t.array(t.proxy(renames["ProtectedRangeIn"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterIn"]).optional(),
            "slicers": t.array(t.proxy(renames["SlicerIn"])).optional(),
            "properties": t.proxy(renames["SheetPropertiesIn"]).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewIn"])).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleIn"])
            ).optional(),
            "merges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "bandedRanges": t.array(t.proxy(renames["BandedRangeIn"])).optional(),
        }
    ).named(renames["SheetIn"])
    types["SheetOut"] = t.struct(
        {
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "data": t.array(t.proxy(renames["GridDataOut"])).optional(),
            "columnGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartOut"])).optional(),
            "protectedRanges": t.array(
                t.proxy(renames["ProtectedRangeOut"])
            ).optional(),
            "basicFilter": t.proxy(renames["BasicFilterOut"]).optional(),
            "slicers": t.array(t.proxy(renames["SlicerOut"])).optional(),
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewOut"])).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleOut"])
            ).optional(),
            "merges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "bandedRanges": t.array(t.proxy(renames["BandedRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetOut"])
    types["GetSpreadsheetByDataFilterRequestIn"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "includeGridData": t.boolean().optional(),
        }
    ).named(renames["GetSpreadsheetByDataFilterRequestIn"])
    types["GetSpreadsheetByDataFilterRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "includeGridData": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSpreadsheetByDataFilterRequestOut"])
    types["TextRotationIn"] = t.struct(
        {"vertical": t.boolean().optional(), "angle": t.integer().optional()}
    ).named(renames["TextRotationIn"])
    types["TextRotationOut"] = t.struct(
        {
            "vertical": t.boolean().optional(),
            "angle": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextRotationOut"])
    types["FindReplaceRequestIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "matchCase": t.boolean().optional(),
            "allSheets": t.boolean().optional(),
            "matchEntireCell": t.boolean().optional(),
            "includeFormulas": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "find": t.string().optional(),
            "replacement": t.string().optional(),
            "searchByRegex": t.boolean().optional(),
        }
    ).named(renames["FindReplaceRequestIn"])
    types["FindReplaceRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "matchCase": t.boolean().optional(),
            "allSheets": t.boolean().optional(),
            "matchEntireCell": t.boolean().optional(),
            "includeFormulas": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "find": t.string().optional(),
            "replacement": t.string().optional(),
            "searchByRegex": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceRequestOut"])
    types["CreateDeveloperMetadataRequestIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataRequestIn"])
    types["CreateDeveloperMetadataRequestOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataRequestOut"])
    types["AddChartRequestIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartRequestIn"])
    types["AddChartRequestOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartRequestOut"])
    types["GridRangeIn"] = t.struct(
        {
            "startRowIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startColumnIndex": t.integer().optional(),
            "endRowIndex": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
        }
    ).named(renames["GridRangeIn"])
    types["GridRangeOut"] = t.struct(
        {
            "startRowIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startColumnIndex": t.integer().optional(),
            "endRowIndex": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridRangeOut"])
    types["EmbeddedChartIn"] = t.struct(
        {
            "spec": t.proxy(renames["ChartSpecIn"]).optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["EmbeddedChartIn"])
    types["EmbeddedChartOut"] = t.struct(
        {
            "spec": t.proxy(renames["ChartSpecOut"]).optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedChartOut"])
    types["CandlestickDataIn"] = t.struct(
        {
            "highSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "lowSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "openSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
        }
    ).named(renames["CandlestickDataIn"])
    types["CandlestickDataOut"] = t.struct(
        {
            "highSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "lowSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "openSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickDataOut"])
    types["DataFilterIn"] = t.struct(
        {
            "a1Range": t.string().optional(),
            "gridRange": t.proxy(renames["GridRangeIn"]).optional(),
            "developerMetadataLookup": t.proxy(
                renames["DeveloperMetadataLookupIn"]
            ).optional(),
        }
    ).named(renames["DataFilterIn"])
    types["DataFilterOut"] = t.struct(
        {
            "a1Range": t.string().optional(),
            "gridRange": t.proxy(renames["GridRangeOut"]).optional(),
            "developerMetadataLookup": t.proxy(
                renames["DeveloperMetadataLookupOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataFilterOut"])
    types["AddDataSourceRequestIn"] = t.struct(
        {"dataSource": t.proxy(renames["DataSourceIn"]).optional()}
    ).named(renames["AddDataSourceRequestIn"])
    types["AddDataSourceRequestOut"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDataSourceRequestOut"])
    types["BasicChartAxisIn"] = t.struct(
        {
            "position": t.string().optional(),
            "title": t.string().optional(),
            "format": t.proxy(renames["TextFormatIn"]).optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsIn"]
            ).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
        }
    ).named(renames["BasicChartAxisIn"])
    types["BasicChartAxisOut"] = t.struct(
        {
            "position": t.string().optional(),
            "title": t.string().optional(),
            "format": t.proxy(renames["TextFormatOut"]).optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsOut"]
            ).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartAxisOut"])
    types["PivotGroupIn"] = t.struct(
        {
            "sourceColumnOffset": t.integer().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataIn"])
            ).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "label": t.string().optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketIn"]).optional(),
            "groupRule": t.proxy(renames["PivotGroupRuleIn"]).optional(),
            "repeatHeadings": t.boolean().optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitIn"]).optional(),
            "showTotals": t.boolean().optional(),
            "sortOrder": t.string().optional(),
        }
    ).named(renames["PivotGroupIn"])
    types["PivotGroupOut"] = t.struct(
        {
            "sourceColumnOffset": t.integer().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataOut"])
            ).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "label": t.string().optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketOut"]).optional(),
            "groupRule": t.proxy(renames["PivotGroupRuleOut"]).optional(),
            "repeatHeadings": t.boolean().optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitOut"]).optional(),
            "showTotals": t.boolean().optional(),
            "sortOrder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupOut"])
    types["InsertDimensionRequestIn"] = t.struct(
        {
            "inheritFromBefore": t.boolean().optional(),
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
        }
    ).named(renames["InsertDimensionRequestIn"])
    types["InsertDimensionRequestOut"] = t.struct(
        {
            "inheritFromBefore": t.boolean().optional(),
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertDimensionRequestOut"])
    types["DeleteSheetRequestIn"] = t.struct({"sheetId": t.integer().optional()}).named(
        renames["DeleteSheetRequestIn"]
    )
    types["DeleteSheetRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteSheetRequestOut"])
    types["ChartSpecIn"] = t.struct(
        {
            "treemapChart": t.proxy(renames["TreemapChartSpecIn"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesIn"]
            ).optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecIn"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "pieChart": t.proxy(renames["PieChartSpecIn"]).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecIn"]).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "subtitle": t.string().optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecIn"]).optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "maximized": t.boolean().optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "altText": t.string().optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecIn"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "candlestickChart": t.proxy(renames["CandlestickChartSpecIn"]).optional(),
            "fontName": t.string().optional(),
            "basicChart": t.proxy(renames["BasicChartSpecIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ChartSpecIn"])
    types["ChartSpecOut"] = t.struct(
        {
            "treemapChart": t.proxy(renames["TreemapChartSpecOut"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesOut"]
            ).optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecOut"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "pieChart": t.proxy(renames["PieChartSpecOut"]).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecOut"]).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "subtitle": t.string().optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecOut"]).optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "maximized": t.boolean().optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "altText": t.string().optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecOut"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "candlestickChart": t.proxy(renames["CandlestickChartSpecOut"]).optional(),
            "fontName": t.string().optional(),
            "basicChart": t.proxy(renames["BasicChartSpecOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSpecOut"])
    types["DataSourceSheetDimensionRangeIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "columnReferences": t.array(
                t.proxy(renames["DataSourceColumnReferenceIn"])
            ).optional(),
        }
    ).named(renames["DataSourceSheetDimensionRangeIn"])
    types["DataSourceSheetDimensionRangeOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "columnReferences": t.array(
                t.proxy(renames["DataSourceColumnReferenceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSheetDimensionRangeOut"])
    types["ExtendedValueIn"] = t.struct(
        {
            "errorValue": t.proxy(renames["ErrorValueIn"]).optional(),
            "formulaValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "numberValue": t.number().optional(),
        }
    ).named(renames["ExtendedValueIn"])
    types["ExtendedValueOut"] = t.struct(
        {
            "errorValue": t.proxy(renames["ErrorValueOut"]).optional(),
            "formulaValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "numberValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedValueOut"])
    types["DateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DateTimeRuleIn"]
    )
    types["DateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeRuleOut"])
    types["SpreadsheetThemeIn"] = t.struct(
        {
            "primaryFontFamily": t.string().optional(),
            "themeColors": t.array(t.proxy(renames["ThemeColorPairIn"])).optional(),
        }
    ).named(renames["SpreadsheetThemeIn"])
    types["SpreadsheetThemeOut"] = t.struct(
        {
            "primaryFontFamily": t.string().optional(),
            "themeColors": t.array(t.proxy(renames["ThemeColorPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetThemeOut"])
    types["AppendCellsRequestIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "rows": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["AppendCellsRequestIn"])
    types["AppendCellsRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "rows": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendCellsRequestOut"])
    types["SetBasicFilterRequestIn"] = t.struct(
        {"filter": t.proxy(renames["BasicFilterIn"]).optional()}
    ).named(renames["SetBasicFilterRequestIn"])
    types["SetBasicFilterRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["BasicFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetBasicFilterRequestOut"])
    types["DeleteNamedRangeRequestIn"] = t.struct(
        {"namedRangeId": t.string().optional()}
    ).named(renames["DeleteNamedRangeRequestIn"])
    types["DeleteNamedRangeRequestOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteNamedRangeRequestOut"])
    types["UpdateCellsRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "rows": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "start": t.proxy(renames["GridCoordinateIn"]).optional(),
        }
    ).named(renames["UpdateCellsRequestIn"])
    types["UpdateCellsRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "rows": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "start": t.proxy(renames["GridCoordinateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCellsRequestOut"])
    types["BatchClearValuesByDataFilterResponseIn"] = t.struct(
        {
            "clearedRanges": t.array(t.string()).optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterResponseIn"])
    types["BatchClearValuesByDataFilterResponseOut"] = t.struct(
        {
            "clearedRanges": t.array(t.string()).optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterResponseOut"])
    types["DuplicateFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DuplicateFilterViewRequestIn"])
    types["DuplicateFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewRequestOut"])
    types["BatchUpdateValuesRequestIn"] = t.struct(
        {
            "includeValuesInResponse": t.boolean().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
            "valueInputOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesRequestIn"])
    types["BatchUpdateValuesRequestOut"] = t.struct(
        {
            "includeValuesInResponse": t.boolean().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "data": t.array(t.proxy(renames["ValueRangeOut"])).optional(),
            "valueInputOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesRequestOut"])
    types["TreemapChartColorScaleIn"] = t.struct(
        {
            "minValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "noDataColor": t.proxy(renames["ColorIn"]).optional(),
            "maxValueColor": t.proxy(renames["ColorIn"]).optional(),
            "maxValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "minValueColor": t.proxy(renames["ColorIn"]).optional(),
            "noDataColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "midValueColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleIn"])
    types["TreemapChartColorScaleOut"] = t.struct(
        {
            "minValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "noDataColor": t.proxy(renames["ColorOut"]).optional(),
            "maxValueColor": t.proxy(renames["ColorOut"]).optional(),
            "maxValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "minValueColor": t.proxy(renames["ColorOut"]).optional(),
            "noDataColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "midValueColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleOut"])
    types["BasicChartDomainIn"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
            "reversed": t.boolean().optional(),
        }
    ).named(renames["BasicChartDomainIn"])
    types["BasicChartDomainOut"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "reversed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartDomainOut"])
    types["AutoResizeDimensionsRequestIn"] = t.struct(
        {
            "dimensions": t.proxy(renames["DimensionRangeIn"]).optional(),
            "dataSourceSheetDimensions": t.proxy(
                renames["DataSourceSheetDimensionRangeIn"]
            ).optional(),
        }
    ).named(renames["AutoResizeDimensionsRequestIn"])
    types["AutoResizeDimensionsRequestOut"] = t.struct(
        {
            "dimensions": t.proxy(renames["DimensionRangeOut"]).optional(),
            "dataSourceSheetDimensions": t.proxy(
                renames["DataSourceSheetDimensionRangeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoResizeDimensionsRequestOut"])

    functions = {}
    functions["spreadsheetsGetByDataFilter"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}",
        t.struct(
            {
                "ranges": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsCreate"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}",
        t.struct(
            {
                "ranges": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsBatchUpdate"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}",
        t.struct(
            {
                "ranges": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsGet"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}",
        t.struct(
            {
                "ranges": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchUpdateByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesClear"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesAppend"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchClearByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesUpdate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchGetByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchUpdate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchClear"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchClear",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "ranges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsDeveloperMetadataGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/developerMetadata:search",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchDeveloperMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsDeveloperMetadataSearch"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/developerMetadata:search",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchDeveloperMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsSheetsCopyTo"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/sheets/{sheetId}:copyTo",
        t.struct(
            {
                "sheetId": t.integer().optional(),
                "spreadsheetId": t.string().optional(),
                "destinationSpreadsheetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SheetPropertiesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="sheets", renames=renames, types=types, functions=functions)
