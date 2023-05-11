from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_sheets() -> Import:
    sheets = HTTPRuntime("https://sheets.googleapis.com/")

    renames = {
        "ErrorResponse": "_sheets_1_ErrorResponse",
        "ResponseIn": "_sheets_2_ResponseIn",
        "ResponseOut": "_sheets_3_ResponseOut",
        "DuplicateFilterViewRequestIn": "_sheets_4_DuplicateFilterViewRequestIn",
        "DuplicateFilterViewRequestOut": "_sheets_5_DuplicateFilterViewRequestOut",
        "AddNamedRangeRequestIn": "_sheets_6_AddNamedRangeRequestIn",
        "AddNamedRangeRequestOut": "_sheets_7_AddNamedRangeRequestOut",
        "CreateDeveloperMetadataResponseIn": "_sheets_8_CreateDeveloperMetadataResponseIn",
        "CreateDeveloperMetadataResponseOut": "_sheets_9_CreateDeveloperMetadataResponseOut",
        "ChartHistogramRuleIn": "_sheets_10_ChartHistogramRuleIn",
        "ChartHistogramRuleOut": "_sheets_11_ChartHistogramRuleOut",
        "DataSourceSheetPropertiesIn": "_sheets_12_DataSourceSheetPropertiesIn",
        "DataSourceSheetPropertiesOut": "_sheets_13_DataSourceSheetPropertiesOut",
        "DataSourceRefreshDailyScheduleIn": "_sheets_14_DataSourceRefreshDailyScheduleIn",
        "DataSourceRefreshDailyScheduleOut": "_sheets_15_DataSourceRefreshDailyScheduleOut",
        "ManualRuleGroupIn": "_sheets_16_ManualRuleGroupIn",
        "ManualRuleGroupOut": "_sheets_17_ManualRuleGroupOut",
        "RandomizeRangeRequestIn": "_sheets_18_RandomizeRangeRequestIn",
        "RandomizeRangeRequestOut": "_sheets_19_RandomizeRangeRequestOut",
        "SlicerIn": "_sheets_20_SlicerIn",
        "SlicerOut": "_sheets_21_SlicerOut",
        "CandlestickDataIn": "_sheets_22_CandlestickDataIn",
        "CandlestickDataOut": "_sheets_23_CandlestickDataOut",
        "InsertRangeRequestIn": "_sheets_24_InsertRangeRequestIn",
        "InsertRangeRequestOut": "_sheets_25_InsertRangeRequestOut",
        "TreemapChartColorScaleIn": "_sheets_26_TreemapChartColorScaleIn",
        "TreemapChartColorScaleOut": "_sheets_27_TreemapChartColorScaleOut",
        "IterativeCalculationSettingsIn": "_sheets_28_IterativeCalculationSettingsIn",
        "IterativeCalculationSettingsOut": "_sheets_29_IterativeCalculationSettingsOut",
        "FilterSpecIn": "_sheets_30_FilterSpecIn",
        "FilterSpecOut": "_sheets_31_FilterSpecOut",
        "DeleteNamedRangeRequestIn": "_sheets_32_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_sheets_33_DeleteNamedRangeRequestOut",
        "DataSourceColumnReferenceIn": "_sheets_34_DataSourceColumnReferenceIn",
        "DataSourceColumnReferenceOut": "_sheets_35_DataSourceColumnReferenceOut",
        "AddSlicerResponseIn": "_sheets_36_AddSlicerResponseIn",
        "AddSlicerResponseOut": "_sheets_37_AddSlicerResponseOut",
        "DeleteDimensionGroupResponseIn": "_sheets_38_DeleteDimensionGroupResponseIn",
        "DeleteDimensionGroupResponseOut": "_sheets_39_DeleteDimensionGroupResponseOut",
        "DeleteDuplicatesRequestIn": "_sheets_40_DeleteDuplicatesRequestIn",
        "DeleteDuplicatesRequestOut": "_sheets_41_DeleteDuplicatesRequestOut",
        "HistogramSeriesIn": "_sheets_42_HistogramSeriesIn",
        "HistogramSeriesOut": "_sheets_43_HistogramSeriesOut",
        "SpreadsheetThemeIn": "_sheets_44_SpreadsheetThemeIn",
        "SpreadsheetThemeOut": "_sheets_45_SpreadsheetThemeOut",
        "OrgChartSpecIn": "_sheets_46_OrgChartSpecIn",
        "OrgChartSpecOut": "_sheets_47_OrgChartSpecOut",
        "SlicerSpecIn": "_sheets_48_SlicerSpecIn",
        "SlicerSpecOut": "_sheets_49_SlicerSpecOut",
        "FindReplaceRequestIn": "_sheets_50_FindReplaceRequestIn",
        "FindReplaceRequestOut": "_sheets_51_FindReplaceRequestOut",
        "TimeOfDayIn": "_sheets_52_TimeOfDayIn",
        "TimeOfDayOut": "_sheets_53_TimeOfDayOut",
        "GetSpreadsheetByDataFilterRequestIn": "_sheets_54_GetSpreadsheetByDataFilterRequestIn",
        "GetSpreadsheetByDataFilterRequestOut": "_sheets_55_GetSpreadsheetByDataFilterRequestOut",
        "DuplicateSheetRequestIn": "_sheets_56_DuplicateSheetRequestIn",
        "DuplicateSheetRequestOut": "_sheets_57_DuplicateSheetRequestOut",
        "OverlayPositionIn": "_sheets_58_OverlayPositionIn",
        "OverlayPositionOut": "_sheets_59_OverlayPositionOut",
        "DeleteBandingRequestIn": "_sheets_60_DeleteBandingRequestIn",
        "DeleteBandingRequestOut": "_sheets_61_DeleteBandingRequestOut",
        "BigQueryDataSourceSpecIn": "_sheets_62_BigQueryDataSourceSpecIn",
        "BigQueryDataSourceSpecOut": "_sheets_63_BigQueryDataSourceSpecOut",
        "ConditionalFormatRuleIn": "_sheets_64_ConditionalFormatRuleIn",
        "ConditionalFormatRuleOut": "_sheets_65_ConditionalFormatRuleOut",
        "UpdateChartSpecRequestIn": "_sheets_66_UpdateChartSpecRequestIn",
        "UpdateChartSpecRequestOut": "_sheets_67_UpdateChartSpecRequestOut",
        "MatchedValueRangeIn": "_sheets_68_MatchedValueRangeIn",
        "MatchedValueRangeOut": "_sheets_69_MatchedValueRangeOut",
        "GridCoordinateIn": "_sheets_70_GridCoordinateIn",
        "GridCoordinateOut": "_sheets_71_GridCoordinateOut",
        "UpdateEmbeddedObjectPositionRequestIn": "_sheets_72_UpdateEmbeddedObjectPositionRequestIn",
        "UpdateEmbeddedObjectPositionRequestOut": "_sheets_73_UpdateEmbeddedObjectPositionRequestOut",
        "UpdateConditionalFormatRuleResponseIn": "_sheets_74_UpdateConditionalFormatRuleResponseIn",
        "UpdateConditionalFormatRuleResponseOut": "_sheets_75_UpdateConditionalFormatRuleResponseOut",
        "GradientRuleIn": "_sheets_76_GradientRuleIn",
        "GradientRuleOut": "_sheets_77_GradientRuleOut",
        "PivotGroupLimitIn": "_sheets_78_PivotGroupLimitIn",
        "PivotGroupLimitOut": "_sheets_79_PivotGroupLimitOut",
        "PivotGroupRuleIn": "_sheets_80_PivotGroupRuleIn",
        "PivotGroupRuleOut": "_sheets_81_PivotGroupRuleOut",
        "UpdateDataSourceRequestIn": "_sheets_82_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_sheets_83_UpdateDataSourceRequestOut",
        "UpdateProtectedRangeRequestIn": "_sheets_84_UpdateProtectedRangeRequestIn",
        "UpdateProtectedRangeRequestOut": "_sheets_85_UpdateProtectedRangeRequestOut",
        "AddBandingRequestIn": "_sheets_86_AddBandingRequestIn",
        "AddBandingRequestOut": "_sheets_87_AddBandingRequestOut",
        "DataSourceParameterIn": "_sheets_88_DataSourceParameterIn",
        "DataSourceParameterOut": "_sheets_89_DataSourceParameterOut",
        "DataValidationRuleIn": "_sheets_90_DataValidationRuleIn",
        "DataValidationRuleOut": "_sheets_91_DataValidationRuleOut",
        "SheetPropertiesIn": "_sheets_92_SheetPropertiesIn",
        "SheetPropertiesOut": "_sheets_93_SheetPropertiesOut",
        "RowDataIn": "_sheets_94_RowDataIn",
        "RowDataOut": "_sheets_95_RowDataOut",
        "PivotGroupIn": "_sheets_96_PivotGroupIn",
        "PivotGroupOut": "_sheets_97_PivotGroupOut",
        "TreemapChartSpecIn": "_sheets_98_TreemapChartSpecIn",
        "TreemapChartSpecOut": "_sheets_99_TreemapChartSpecOut",
        "ErrorValueIn": "_sheets_100_ErrorValueIn",
        "ErrorValueOut": "_sheets_101_ErrorValueOut",
        "BatchClearValuesRequestIn": "_sheets_102_BatchClearValuesRequestIn",
        "BatchClearValuesRequestOut": "_sheets_103_BatchClearValuesRequestOut",
        "DeleteDuplicatesResponseIn": "_sheets_104_DeleteDuplicatesResponseIn",
        "DeleteDuplicatesResponseOut": "_sheets_105_DeleteDuplicatesResponseOut",
        "UpdateDimensionGroupRequestIn": "_sheets_106_UpdateDimensionGroupRequestIn",
        "UpdateDimensionGroupRequestOut": "_sheets_107_UpdateDimensionGroupRequestOut",
        "BigQueryTableSpecIn": "_sheets_108_BigQueryTableSpecIn",
        "BigQueryTableSpecOut": "_sheets_109_BigQueryTableSpecOut",
        "DateTimeRuleIn": "_sheets_110_DateTimeRuleIn",
        "DateTimeRuleOut": "_sheets_111_DateTimeRuleOut",
        "AddDimensionGroupRequestIn": "_sheets_112_AddDimensionGroupRequestIn",
        "AddDimensionGroupRequestOut": "_sheets_113_AddDimensionGroupRequestOut",
        "DeleteConditionalFormatRuleResponseIn": "_sheets_114_DeleteConditionalFormatRuleResponseIn",
        "DeleteConditionalFormatRuleResponseOut": "_sheets_115_DeleteConditionalFormatRuleResponseOut",
        "BatchClearValuesResponseIn": "_sheets_116_BatchClearValuesResponseIn",
        "BatchClearValuesResponseOut": "_sheets_117_BatchClearValuesResponseOut",
        "AddSheetResponseIn": "_sheets_118_AddSheetResponseIn",
        "AddSheetResponseOut": "_sheets_119_AddSheetResponseOut",
        "WaterfallChartCustomSubtotalIn": "_sheets_120_WaterfallChartCustomSubtotalIn",
        "WaterfallChartCustomSubtotalOut": "_sheets_121_WaterfallChartCustomSubtotalOut",
        "PivotValueIn": "_sheets_122_PivotValueIn",
        "PivotValueOut": "_sheets_123_PivotValueOut",
        "AppendDimensionRequestIn": "_sheets_124_AppendDimensionRequestIn",
        "AppendDimensionRequestOut": "_sheets_125_AppendDimensionRequestOut",
        "KeyValueFormatIn": "_sheets_126_KeyValueFormatIn",
        "KeyValueFormatOut": "_sheets_127_KeyValueFormatOut",
        "FilterCriteriaIn": "_sheets_128_FilterCriteriaIn",
        "FilterCriteriaOut": "_sheets_129_FilterCriteriaOut",
        "BooleanRuleIn": "_sheets_130_BooleanRuleIn",
        "BooleanRuleOut": "_sheets_131_BooleanRuleOut",
        "ClearValuesResponseIn": "_sheets_132_ClearValuesResponseIn",
        "ClearValuesResponseOut": "_sheets_133_ClearValuesResponseOut",
        "RefreshDataSourceRequestIn": "_sheets_134_RefreshDataSourceRequestIn",
        "RefreshDataSourceRequestOut": "_sheets_135_RefreshDataSourceRequestOut",
        "BasicFilterIn": "_sheets_136_BasicFilterIn",
        "BasicFilterOut": "_sheets_137_BasicFilterOut",
        "AddProtectedRangeResponseIn": "_sheets_138_AddProtectedRangeResponseIn",
        "AddProtectedRangeResponseOut": "_sheets_139_AddProtectedRangeResponseOut",
        "SearchDeveloperMetadataRequestIn": "_sheets_140_SearchDeveloperMetadataRequestIn",
        "SearchDeveloperMetadataRequestOut": "_sheets_141_SearchDeveloperMetadataRequestOut",
        "CandlestickChartSpecIn": "_sheets_142_CandlestickChartSpecIn",
        "CandlestickChartSpecOut": "_sheets_143_CandlestickChartSpecOut",
        "SpreadsheetIn": "_sheets_144_SpreadsheetIn",
        "SpreadsheetOut": "_sheets_145_SpreadsheetOut",
        "WaterfallChartSeriesIn": "_sheets_146_WaterfallChartSeriesIn",
        "WaterfallChartSeriesOut": "_sheets_147_WaterfallChartSeriesOut",
        "EmbeddedObjectPositionIn": "_sheets_148_EmbeddedObjectPositionIn",
        "EmbeddedObjectPositionOut": "_sheets_149_EmbeddedObjectPositionOut",
        "ChartAxisViewWindowOptionsIn": "_sheets_150_ChartAxisViewWindowOptionsIn",
        "ChartAxisViewWindowOptionsOut": "_sheets_151_ChartAxisViewWindowOptionsOut",
        "DataSourceTableIn": "_sheets_152_DataSourceTableIn",
        "DataSourceTableOut": "_sheets_153_DataSourceTableOut",
        "DataSourceSpecIn": "_sheets_154_DataSourceSpecIn",
        "DataSourceSpecOut": "_sheets_155_DataSourceSpecOut",
        "UpdateValuesByDataFilterResponseIn": "_sheets_156_UpdateValuesByDataFilterResponseIn",
        "UpdateValuesByDataFilterResponseOut": "_sheets_157_UpdateValuesByDataFilterResponseOut",
        "InsertDimensionRequestIn": "_sheets_158_InsertDimensionRequestIn",
        "InsertDimensionRequestOut": "_sheets_159_InsertDimensionRequestOut",
        "DataFilterValueRangeIn": "_sheets_160_DataFilterValueRangeIn",
        "DataFilterValueRangeOut": "_sheets_161_DataFilterValueRangeOut",
        "DataSourceChartPropertiesIn": "_sheets_162_DataSourceChartPropertiesIn",
        "DataSourceChartPropertiesOut": "_sheets_163_DataSourceChartPropertiesOut",
        "WaterfallChartSpecIn": "_sheets_164_WaterfallChartSpecIn",
        "WaterfallChartSpecOut": "_sheets_165_WaterfallChartSpecOut",
        "InterpolationPointIn": "_sheets_166_InterpolationPointIn",
        "InterpolationPointOut": "_sheets_167_InterpolationPointOut",
        "PaddingIn": "_sheets_168_PaddingIn",
        "PaddingOut": "_sheets_169_PaddingOut",
        "AddNamedRangeResponseIn": "_sheets_170_AddNamedRangeResponseIn",
        "AddNamedRangeResponseOut": "_sheets_171_AddNamedRangeResponseOut",
        "GridRangeIn": "_sheets_172_GridRangeIn",
        "GridRangeOut": "_sheets_173_GridRangeOut",
        "UpdateDeveloperMetadataResponseIn": "_sheets_174_UpdateDeveloperMetadataResponseIn",
        "UpdateDeveloperMetadataResponseOut": "_sheets_175_UpdateDeveloperMetadataResponseOut",
        "DeveloperMetadataLookupIn": "_sheets_176_DeveloperMetadataLookupIn",
        "DeveloperMetadataLookupOut": "_sheets_177_DeveloperMetadataLookupOut",
        "HistogramChartSpecIn": "_sheets_178_HistogramChartSpecIn",
        "HistogramChartSpecOut": "_sheets_179_HistogramChartSpecOut",
        "DataSourceObjectReferenceIn": "_sheets_180_DataSourceObjectReferenceIn",
        "DataSourceObjectReferenceOut": "_sheets_181_DataSourceObjectReferenceOut",
        "CreateDeveloperMetadataRequestIn": "_sheets_182_CreateDeveloperMetadataRequestIn",
        "CreateDeveloperMetadataRequestOut": "_sheets_183_CreateDeveloperMetadataRequestOut",
        "SetDataValidationRequestIn": "_sheets_184_SetDataValidationRequestIn",
        "SetDataValidationRequestOut": "_sheets_185_SetDataValidationRequestOut",
        "DeleteRangeRequestIn": "_sheets_186_DeleteRangeRequestIn",
        "DeleteRangeRequestOut": "_sheets_187_DeleteRangeRequestOut",
        "DataSourceObjectReferencesIn": "_sheets_188_DataSourceObjectReferencesIn",
        "DataSourceObjectReferencesOut": "_sheets_189_DataSourceObjectReferencesOut",
        "SortRangeRequestIn": "_sheets_190_SortRangeRequestIn",
        "SortRangeRequestOut": "_sheets_191_SortRangeRequestOut",
        "TextFormatRunIn": "_sheets_192_TextFormatRunIn",
        "TextFormatRunOut": "_sheets_193_TextFormatRunOut",
        "BatchClearValuesByDataFilterResponseIn": "_sheets_194_BatchClearValuesByDataFilterResponseIn",
        "BatchClearValuesByDataFilterResponseOut": "_sheets_195_BatchClearValuesByDataFilterResponseOut",
        "DuplicateSheetResponseIn": "_sheets_196_DuplicateSheetResponseIn",
        "DuplicateSheetResponseOut": "_sheets_197_DuplicateSheetResponseOut",
        "PivotTableIn": "_sheets_198_PivotTableIn",
        "PivotTableOut": "_sheets_199_PivotTableOut",
        "UpdateSheetPropertiesRequestIn": "_sheets_200_UpdateSheetPropertiesRequestIn",
        "UpdateSheetPropertiesRequestOut": "_sheets_201_UpdateSheetPropertiesRequestOut",
        "BandingPropertiesIn": "_sheets_202_BandingPropertiesIn",
        "BandingPropertiesOut": "_sheets_203_BandingPropertiesOut",
        "AddFilterViewResponseIn": "_sheets_204_AddFilterViewResponseIn",
        "AddFilterViewResponseOut": "_sheets_205_AddFilterViewResponseOut",
        "DataSourceFormulaIn": "_sheets_206_DataSourceFormulaIn",
        "DataSourceFormulaOut": "_sheets_207_DataSourceFormulaOut",
        "PivotFilterCriteriaIn": "_sheets_208_PivotFilterCriteriaIn",
        "PivotFilterCriteriaOut": "_sheets_209_PivotFilterCriteriaOut",
        "AddSheetRequestIn": "_sheets_210_AddSheetRequestIn",
        "AddSheetRequestOut": "_sheets_211_AddSheetRequestOut",
        "DeveloperMetadataLocationIn": "_sheets_212_DeveloperMetadataLocationIn",
        "DeveloperMetadataLocationOut": "_sheets_213_DeveloperMetadataLocationOut",
        "DeveloperMetadataIn": "_sheets_214_DeveloperMetadataIn",
        "DeveloperMetadataOut": "_sheets_215_DeveloperMetadataOut",
        "IntervalIn": "_sheets_216_IntervalIn",
        "IntervalOut": "_sheets_217_IntervalOut",
        "ChartCustomNumberFormatOptionsIn": "_sheets_218_ChartCustomNumberFormatOptionsIn",
        "ChartCustomNumberFormatOptionsOut": "_sheets_219_ChartCustomNumberFormatOptionsOut",
        "DataExecutionStatusIn": "_sheets_220_DataExecutionStatusIn",
        "DataExecutionStatusOut": "_sheets_221_DataExecutionStatusOut",
        "DataSourceRefreshMonthlyScheduleIn": "_sheets_222_DataSourceRefreshMonthlyScheduleIn",
        "DataSourceRefreshMonthlyScheduleOut": "_sheets_223_DataSourceRefreshMonthlyScheduleOut",
        "TextFormatIn": "_sheets_224_TextFormatIn",
        "TextFormatOut": "_sheets_225_TextFormatOut",
        "SetBasicFilterRequestIn": "_sheets_226_SetBasicFilterRequestIn",
        "SetBasicFilterRequestOut": "_sheets_227_SetBasicFilterRequestOut",
        "GridDataIn": "_sheets_228_GridDataIn",
        "GridDataOut": "_sheets_229_GridDataOut",
        "AutoFillRequestIn": "_sheets_230_AutoFillRequestIn",
        "AutoFillRequestOut": "_sheets_231_AutoFillRequestOut",
        "UpdateCellsRequestIn": "_sheets_232_UpdateCellsRequestIn",
        "UpdateCellsRequestOut": "_sheets_233_UpdateCellsRequestOut",
        "UpdateEmbeddedObjectBorderRequestIn": "_sheets_234_UpdateEmbeddedObjectBorderRequestIn",
        "UpdateEmbeddedObjectBorderRequestOut": "_sheets_235_UpdateEmbeddedObjectBorderRequestOut",
        "BatchUpdateValuesRequestIn": "_sheets_236_BatchUpdateValuesRequestIn",
        "BatchUpdateValuesRequestOut": "_sheets_237_BatchUpdateValuesRequestOut",
        "BatchGetValuesByDataFilterResponseIn": "_sheets_238_BatchGetValuesByDataFilterResponseIn",
        "BatchGetValuesByDataFilterResponseOut": "_sheets_239_BatchGetValuesByDataFilterResponseOut",
        "ScorecardChartSpecIn": "_sheets_240_ScorecardChartSpecIn",
        "ScorecardChartSpecOut": "_sheets_241_ScorecardChartSpecOut",
        "UpdateDeveloperMetadataRequestIn": "_sheets_242_UpdateDeveloperMetadataRequestIn",
        "UpdateDeveloperMetadataRequestOut": "_sheets_243_UpdateDeveloperMetadataRequestOut",
        "BooleanConditionIn": "_sheets_244_BooleanConditionIn",
        "BooleanConditionOut": "_sheets_245_BooleanConditionOut",
        "PieChartSpecIn": "_sheets_246_PieChartSpecIn",
        "PieChartSpecOut": "_sheets_247_PieChartSpecOut",
        "DeleteDataSourceRequestIn": "_sheets_248_DeleteDataSourceRequestIn",
        "DeleteDataSourceRequestOut": "_sheets_249_DeleteDataSourceRequestOut",
        "EmbeddedChartIn": "_sheets_250_EmbeddedChartIn",
        "EmbeddedChartOut": "_sheets_251_EmbeddedChartOut",
        "DeleteFilterViewRequestIn": "_sheets_252_DeleteFilterViewRequestIn",
        "DeleteFilterViewRequestOut": "_sheets_253_DeleteFilterViewRequestOut",
        "PivotGroupValueMetadataIn": "_sheets_254_PivotGroupValueMetadataIn",
        "PivotGroupValueMetadataOut": "_sheets_255_PivotGroupValueMetadataOut",
        "DataLabelIn": "_sheets_256_DataLabelIn",
        "DataLabelOut": "_sheets_257_DataLabelOut",
        "TrimWhitespaceRequestIn": "_sheets_258_TrimWhitespaceRequestIn",
        "TrimWhitespaceRequestOut": "_sheets_259_TrimWhitespaceRequestOut",
        "TrimWhitespaceResponseIn": "_sheets_260_TrimWhitespaceResponseIn",
        "TrimWhitespaceResponseOut": "_sheets_261_TrimWhitespaceResponseOut",
        "HistogramRuleIn": "_sheets_262_HistogramRuleIn",
        "HistogramRuleOut": "_sheets_263_HistogramRuleOut",
        "UpdateDimensionPropertiesRequestIn": "_sheets_264_UpdateDimensionPropertiesRequestIn",
        "UpdateDimensionPropertiesRequestOut": "_sheets_265_UpdateDimensionPropertiesRequestOut",
        "UpdateDataSourceResponseIn": "_sheets_266_UpdateDataSourceResponseIn",
        "UpdateDataSourceResponseOut": "_sheets_267_UpdateDataSourceResponseOut",
        "BatchUpdateValuesByDataFilterResponseIn": "_sheets_268_BatchUpdateValuesByDataFilterResponseIn",
        "BatchUpdateValuesByDataFilterResponseOut": "_sheets_269_BatchUpdateValuesByDataFilterResponseOut",
        "NumberFormatIn": "_sheets_270_NumberFormatIn",
        "NumberFormatOut": "_sheets_271_NumberFormatOut",
        "DimensionGroupIn": "_sheets_272_DimensionGroupIn",
        "DimensionGroupOut": "_sheets_273_DimensionGroupOut",
        "DeleteDeveloperMetadataResponseIn": "_sheets_274_DeleteDeveloperMetadataResponseIn",
        "DeleteDeveloperMetadataResponseOut": "_sheets_275_DeleteDeveloperMetadataResponseOut",
        "PasteDataRequestIn": "_sheets_276_PasteDataRequestIn",
        "PasteDataRequestOut": "_sheets_277_PasteDataRequestOut",
        "AddChartResponseIn": "_sheets_278_AddChartResponseIn",
        "AddChartResponseOut": "_sheets_279_AddChartResponseOut",
        "BandedRangeIn": "_sheets_280_BandedRangeIn",
        "BandedRangeOut": "_sheets_281_BandedRangeOut",
        "CellFormatIn": "_sheets_282_CellFormatIn",
        "CellFormatOut": "_sheets_283_CellFormatOut",
        "UnmergeCellsRequestIn": "_sheets_284_UnmergeCellsRequestIn",
        "UnmergeCellsRequestOut": "_sheets_285_UnmergeCellsRequestOut",
        "TextRotationIn": "_sheets_286_TextRotationIn",
        "TextRotationOut": "_sheets_287_TextRotationOut",
        "BatchUpdateSpreadsheetResponseIn": "_sheets_288_BatchUpdateSpreadsheetResponseIn",
        "BatchUpdateSpreadsheetResponseOut": "_sheets_289_BatchUpdateSpreadsheetResponseOut",
        "DeleteDimensionGroupRequestIn": "_sheets_290_DeleteDimensionGroupRequestIn",
        "DeleteDimensionGroupRequestOut": "_sheets_291_DeleteDimensionGroupRequestOut",
        "AddFilterViewRequestIn": "_sheets_292_AddFilterViewRequestIn",
        "AddFilterViewRequestOut": "_sheets_293_AddFilterViewRequestOut",
        "CopySheetToAnotherSpreadsheetRequestIn": "_sheets_294_CopySheetToAnotherSpreadsheetRequestIn",
        "CopySheetToAnotherSpreadsheetRequestOut": "_sheets_295_CopySheetToAnotherSpreadsheetRequestOut",
        "DuplicateFilterViewResponseIn": "_sheets_296_DuplicateFilterViewResponseIn",
        "DuplicateFilterViewResponseOut": "_sheets_297_DuplicateFilterViewResponseOut",
        "AddDataSourceResponseIn": "_sheets_298_AddDataSourceResponseIn",
        "AddDataSourceResponseOut": "_sheets_299_AddDataSourceResponseOut",
        "NamedRangeIn": "_sheets_300_NamedRangeIn",
        "NamedRangeOut": "_sheets_301_NamedRangeOut",
        "UpdateFilterViewRequestIn": "_sheets_302_UpdateFilterViewRequestIn",
        "UpdateFilterViewRequestOut": "_sheets_303_UpdateFilterViewRequestOut",
        "DataSourceSheetDimensionRangeIn": "_sheets_304_DataSourceSheetDimensionRangeIn",
        "DataSourceSheetDimensionRangeOut": "_sheets_305_DataSourceSheetDimensionRangeOut",
        "BasicChartDomainIn": "_sheets_306_BasicChartDomainIn",
        "BasicChartDomainOut": "_sheets_307_BasicChartDomainOut",
        "BatchUpdateValuesResponseIn": "_sheets_308_BatchUpdateValuesResponseIn",
        "BatchUpdateValuesResponseOut": "_sheets_309_BatchUpdateValuesResponseOut",
        "BordersIn": "_sheets_310_BordersIn",
        "BordersOut": "_sheets_311_BordersOut",
        "ChartDataIn": "_sheets_312_ChartDataIn",
        "ChartDataOut": "_sheets_313_ChartDataOut",
        "FindReplaceResponseIn": "_sheets_314_FindReplaceResponseIn",
        "FindReplaceResponseOut": "_sheets_315_FindReplaceResponseOut",
        "DimensionPropertiesIn": "_sheets_316_DimensionPropertiesIn",
        "DimensionPropertiesOut": "_sheets_317_DimensionPropertiesOut",
        "LineStyleIn": "_sheets_318_LineStyleIn",
        "LineStyleOut": "_sheets_319_LineStyleOut",
        "SearchDeveloperMetadataResponseIn": "_sheets_320_SearchDeveloperMetadataResponseIn",
        "SearchDeveloperMetadataResponseOut": "_sheets_321_SearchDeveloperMetadataResponseOut",
        "FilterViewIn": "_sheets_322_FilterViewIn",
        "FilterViewOut": "_sheets_323_FilterViewOut",
        "RepeatCellRequestIn": "_sheets_324_RepeatCellRequestIn",
        "RepeatCellRequestOut": "_sheets_325_RepeatCellRequestOut",
        "TextPositionIn": "_sheets_326_TextPositionIn",
        "TextPositionOut": "_sheets_327_TextPositionOut",
        "DimensionRangeIn": "_sheets_328_DimensionRangeIn",
        "DimensionRangeOut": "_sheets_329_DimensionRangeOut",
        "BatchClearValuesByDataFilterRequestIn": "_sheets_330_BatchClearValuesByDataFilterRequestIn",
        "BatchClearValuesByDataFilterRequestOut": "_sheets_331_BatchClearValuesByDataFilterRequestOut",
        "SourceAndDestinationIn": "_sheets_332_SourceAndDestinationIn",
        "SourceAndDestinationOut": "_sheets_333_SourceAndDestinationOut",
        "BasicChartSeriesIn": "_sheets_334_BasicChartSeriesIn",
        "BasicChartSeriesOut": "_sheets_335_BasicChartSeriesOut",
        "ChartGroupRuleIn": "_sheets_336_ChartGroupRuleIn",
        "ChartGroupRuleOut": "_sheets_337_ChartGroupRuleOut",
        "DeleteProtectedRangeRequestIn": "_sheets_338_DeleteProtectedRangeRequestIn",
        "DeleteProtectedRangeRequestOut": "_sheets_339_DeleteProtectedRangeRequestOut",
        "EmbeddedObjectBorderIn": "_sheets_340_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_sheets_341_EmbeddedObjectBorderOut",
        "AddSlicerRequestIn": "_sheets_342_AddSlicerRequestIn",
        "AddSlicerRequestOut": "_sheets_343_AddSlicerRequestOut",
        "BubbleChartSpecIn": "_sheets_344_BubbleChartSpecIn",
        "BubbleChartSpecOut": "_sheets_345_BubbleChartSpecOut",
        "MergeCellsRequestIn": "_sheets_346_MergeCellsRequestIn",
        "MergeCellsRequestOut": "_sheets_347_MergeCellsRequestOut",
        "ClearValuesRequestIn": "_sheets_348_ClearValuesRequestIn",
        "ClearValuesRequestOut": "_sheets_349_ClearValuesRequestOut",
        "BatchUpdateSpreadsheetRequestIn": "_sheets_350_BatchUpdateSpreadsheetRequestIn",
        "BatchUpdateSpreadsheetRequestOut": "_sheets_351_BatchUpdateSpreadsheetRequestOut",
        "UpdateBordersRequestIn": "_sheets_352_UpdateBordersRequestIn",
        "UpdateBordersRequestOut": "_sheets_353_UpdateBordersRequestOut",
        "SortSpecIn": "_sheets_354_SortSpecIn",
        "SortSpecOut": "_sheets_355_SortSpecOut",
        "ExtendedValueIn": "_sheets_356_ExtendedValueIn",
        "ExtendedValueOut": "_sheets_357_ExtendedValueOut",
        "RequestIn": "_sheets_358_RequestIn",
        "RequestOut": "_sheets_359_RequestOut",
        "AddChartRequestIn": "_sheets_360_AddChartRequestIn",
        "AddChartRequestOut": "_sheets_361_AddChartRequestOut",
        "UpdateEmbeddedObjectPositionResponseIn": "_sheets_362_UpdateEmbeddedObjectPositionResponseIn",
        "UpdateEmbeddedObjectPositionResponseOut": "_sheets_363_UpdateEmbeddedObjectPositionResponseOut",
        "BasicSeriesDataPointStyleOverrideIn": "_sheets_364_BasicSeriesDataPointStyleOverrideIn",
        "BasicSeriesDataPointStyleOverrideOut": "_sheets_365_BasicSeriesDataPointStyleOverrideOut",
        "ChartSourceRangeIn": "_sheets_366_ChartSourceRangeIn",
        "ChartSourceRangeOut": "_sheets_367_ChartSourceRangeOut",
        "DataSourceColumnIn": "_sheets_368_DataSourceColumnIn",
        "DataSourceColumnOut": "_sheets_369_DataSourceColumnOut",
        "ChartDateTimeRuleIn": "_sheets_370_ChartDateTimeRuleIn",
        "ChartDateTimeRuleOut": "_sheets_371_ChartDateTimeRuleOut",
        "DeleteSheetRequestIn": "_sheets_372_DeleteSheetRequestIn",
        "DeleteSheetRequestOut": "_sheets_373_DeleteSheetRequestOut",
        "AddProtectedRangeRequestIn": "_sheets_374_AddProtectedRangeRequestIn",
        "AddProtectedRangeRequestOut": "_sheets_375_AddProtectedRangeRequestOut",
        "DeleteConditionalFormatRuleRequestIn": "_sheets_376_DeleteConditionalFormatRuleRequestIn",
        "DeleteConditionalFormatRuleRequestOut": "_sheets_377_DeleteConditionalFormatRuleRequestOut",
        "ProtectedRangeIn": "_sheets_378_ProtectedRangeIn",
        "ProtectedRangeOut": "_sheets_379_ProtectedRangeOut",
        "WaterfallChartDomainIn": "_sheets_380_WaterfallChartDomainIn",
        "WaterfallChartDomainOut": "_sheets_381_WaterfallChartDomainOut",
        "AddDataSourceRequestIn": "_sheets_382_AddDataSourceRequestIn",
        "AddDataSourceRequestOut": "_sheets_383_AddDataSourceRequestOut",
        "ClearBasicFilterRequestIn": "_sheets_384_ClearBasicFilterRequestIn",
        "ClearBasicFilterRequestOut": "_sheets_385_ClearBasicFilterRequestOut",
        "CandlestickDomainIn": "_sheets_386_CandlestickDomainIn",
        "CandlestickDomainOut": "_sheets_387_CandlestickDomainOut",
        "BasicChartSpecIn": "_sheets_388_BasicChartSpecIn",
        "BasicChartSpecOut": "_sheets_389_BasicChartSpecOut",
        "DataSourceRefreshWeeklyScheduleIn": "_sheets_390_DataSourceRefreshWeeklyScheduleIn",
        "DataSourceRefreshWeeklyScheduleOut": "_sheets_391_DataSourceRefreshWeeklyScheduleOut",
        "ChartSpecIn": "_sheets_392_ChartSpecIn",
        "ChartSpecOut": "_sheets_393_ChartSpecOut",
        "RefreshDataSourceResponseIn": "_sheets_394_RefreshDataSourceResponseIn",
        "RefreshDataSourceResponseOut": "_sheets_395_RefreshDataSourceResponseOut",
        "GridPropertiesIn": "_sheets_396_GridPropertiesIn",
        "GridPropertiesOut": "_sheets_397_GridPropertiesOut",
        "BatchGetValuesByDataFilterRequestIn": "_sheets_398_BatchGetValuesByDataFilterRequestIn",
        "BatchGetValuesByDataFilterRequestOut": "_sheets_399_BatchGetValuesByDataFilterRequestOut",
        "AddBandingResponseIn": "_sheets_400_AddBandingResponseIn",
        "AddBandingResponseOut": "_sheets_401_AddBandingResponseOut",
        "CopyPasteRequestIn": "_sheets_402_CopyPasteRequestIn",
        "CopyPasteRequestOut": "_sheets_403_CopyPasteRequestOut",
        "BaselineValueFormatIn": "_sheets_404_BaselineValueFormatIn",
        "BaselineValueFormatOut": "_sheets_405_BaselineValueFormatOut",
        "DeleteEmbeddedObjectRequestIn": "_sheets_406_DeleteEmbeddedObjectRequestIn",
        "DeleteEmbeddedObjectRequestOut": "_sheets_407_DeleteEmbeddedObjectRequestOut",
        "UpdateNamedRangeRequestIn": "_sheets_408_UpdateNamedRangeRequestIn",
        "UpdateNamedRangeRequestOut": "_sheets_409_UpdateNamedRangeRequestOut",
        "AddDimensionGroupResponseIn": "_sheets_410_AddDimensionGroupResponseIn",
        "AddDimensionGroupResponseOut": "_sheets_411_AddDimensionGroupResponseOut",
        "MoveDimensionRequestIn": "_sheets_412_MoveDimensionRequestIn",
        "MoveDimensionRequestOut": "_sheets_413_MoveDimensionRequestOut",
        "CellDataIn": "_sheets_414_CellDataIn",
        "CellDataOut": "_sheets_415_CellDataOut",
        "LinkIn": "_sheets_416_LinkIn",
        "LinkOut": "_sheets_417_LinkOut",
        "DeleteDeveloperMetadataRequestIn": "_sheets_418_DeleteDeveloperMetadataRequestIn",
        "DeleteDeveloperMetadataRequestOut": "_sheets_419_DeleteDeveloperMetadataRequestOut",
        "BatchUpdateValuesByDataFilterRequestIn": "_sheets_420_BatchUpdateValuesByDataFilterRequestIn",
        "BatchUpdateValuesByDataFilterRequestOut": "_sheets_421_BatchUpdateValuesByDataFilterRequestOut",
        "UpdateSpreadsheetPropertiesRequestIn": "_sheets_422_UpdateSpreadsheetPropertiesRequestIn",
        "UpdateSpreadsheetPropertiesRequestOut": "_sheets_423_UpdateSpreadsheetPropertiesRequestOut",
        "RefreshDataSourceObjectExecutionStatusIn": "_sheets_424_RefreshDataSourceObjectExecutionStatusIn",
        "RefreshDataSourceObjectExecutionStatusOut": "_sheets_425_RefreshDataSourceObjectExecutionStatusOut",
        "BigQueryQuerySpecIn": "_sheets_426_BigQueryQuerySpecIn",
        "BigQueryQuerySpecOut": "_sheets_427_BigQueryQuerySpecOut",
        "DataSourceIn": "_sheets_428_DataSourceIn",
        "DataSourceOut": "_sheets_429_DataSourceOut",
        "UpdateSlicerSpecRequestIn": "_sheets_430_UpdateSlicerSpecRequestIn",
        "UpdateSlicerSpecRequestOut": "_sheets_431_UpdateSlicerSpecRequestOut",
        "BatchGetValuesResponseIn": "_sheets_432_BatchGetValuesResponseIn",
        "BatchGetValuesResponseOut": "_sheets_433_BatchGetValuesResponseOut",
        "CutPasteRequestIn": "_sheets_434_CutPasteRequestIn",
        "CutPasteRequestOut": "_sheets_435_CutPasteRequestOut",
        "AutoResizeDimensionsRequestIn": "_sheets_436_AutoResizeDimensionsRequestIn",
        "AutoResizeDimensionsRequestOut": "_sheets_437_AutoResizeDimensionsRequestOut",
        "ColorStyleIn": "_sheets_438_ColorStyleIn",
        "ColorStyleOut": "_sheets_439_ColorStyleOut",
        "ValueRangeIn": "_sheets_440_ValueRangeIn",
        "ValueRangeOut": "_sheets_441_ValueRangeOut",
        "CandlestickSeriesIn": "_sheets_442_CandlestickSeriesIn",
        "CandlestickSeriesOut": "_sheets_443_CandlestickSeriesOut",
        "UpdateBandingRequestIn": "_sheets_444_UpdateBandingRequestIn",
        "UpdateBandingRequestOut": "_sheets_445_UpdateBandingRequestOut",
        "EditorsIn": "_sheets_446_EditorsIn",
        "EditorsOut": "_sheets_447_EditorsOut",
        "BorderIn": "_sheets_448_BorderIn",
        "BorderOut": "_sheets_449_BorderOut",
        "SheetIn": "_sheets_450_SheetIn",
        "SheetOut": "_sheets_451_SheetOut",
        "WaterfallChartColumnStyleIn": "_sheets_452_WaterfallChartColumnStyleIn",
        "WaterfallChartColumnStyleOut": "_sheets_453_WaterfallChartColumnStyleOut",
        "UpdateConditionalFormatRuleRequestIn": "_sheets_454_UpdateConditionalFormatRuleRequestIn",
        "UpdateConditionalFormatRuleRequestOut": "_sheets_455_UpdateConditionalFormatRuleRequestOut",
        "ColorIn": "_sheets_456_ColorIn",
        "ColorOut": "_sheets_457_ColorOut",
        "AddConditionalFormatRuleRequestIn": "_sheets_458_AddConditionalFormatRuleRequestIn",
        "AddConditionalFormatRuleRequestOut": "_sheets_459_AddConditionalFormatRuleRequestOut",
        "DataFilterIn": "_sheets_460_DataFilterIn",
        "DataFilterOut": "_sheets_461_DataFilterOut",
        "ConditionValueIn": "_sheets_462_ConditionValueIn",
        "ConditionValueOut": "_sheets_463_ConditionValueOut",
        "DataSourceRefreshScheduleIn": "_sheets_464_DataSourceRefreshScheduleIn",
        "DataSourceRefreshScheduleOut": "_sheets_465_DataSourceRefreshScheduleOut",
        "UpdateValuesResponseIn": "_sheets_466_UpdateValuesResponseIn",
        "UpdateValuesResponseOut": "_sheets_467_UpdateValuesResponseOut",
        "MatchedDeveloperMetadataIn": "_sheets_468_MatchedDeveloperMetadataIn",
        "MatchedDeveloperMetadataOut": "_sheets_469_MatchedDeveloperMetadataOut",
        "ManualRuleIn": "_sheets_470_ManualRuleIn",
        "ManualRuleOut": "_sheets_471_ManualRuleOut",
        "DeleteDimensionRequestIn": "_sheets_472_DeleteDimensionRequestIn",
        "DeleteDimensionRequestOut": "_sheets_473_DeleteDimensionRequestOut",
        "SpreadsheetPropertiesIn": "_sheets_474_SpreadsheetPropertiesIn",
        "SpreadsheetPropertiesOut": "_sheets_475_SpreadsheetPropertiesOut",
        "BasicChartAxisIn": "_sheets_476_BasicChartAxisIn",
        "BasicChartAxisOut": "_sheets_477_BasicChartAxisOut",
        "PivotGroupSortValueBucketIn": "_sheets_478_PivotGroupSortValueBucketIn",
        "PivotGroupSortValueBucketOut": "_sheets_479_PivotGroupSortValueBucketOut",
        "AppendCellsRequestIn": "_sheets_480_AppendCellsRequestIn",
        "AppendCellsRequestOut": "_sheets_481_AppendCellsRequestOut",
        "PivotFilterSpecIn": "_sheets_482_PivotFilterSpecIn",
        "PivotFilterSpecOut": "_sheets_483_PivotFilterSpecOut",
        "PointStyleIn": "_sheets_484_PointStyleIn",
        "PointStyleOut": "_sheets_485_PointStyleOut",
        "AppendValuesResponseIn": "_sheets_486_AppendValuesResponseIn",
        "AppendValuesResponseOut": "_sheets_487_AppendValuesResponseOut",
        "ThemeColorPairIn": "_sheets_488_ThemeColorPairIn",
        "ThemeColorPairOut": "_sheets_489_ThemeColorPairOut",
        "TextToColumnsRequestIn": "_sheets_490_TextToColumnsRequestIn",
        "TextToColumnsRequestOut": "_sheets_491_TextToColumnsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ResponseIn"] = t.struct(
        {
            "addSheet": t.proxy(renames["AddSheetResponseIn"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseIn"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseIn"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingResponseIn"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseIn"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseIn"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseIn"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseIn"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseIn"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseIn"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseIn"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseIn"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseIn"]
            ).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseIn"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseIn"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseIn"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartResponseIn"]).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseIn"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseIn"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseIn"]
            ).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseIn"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseIn"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseIn"]
            ).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "addSheet": t.proxy(renames["AddSheetResponseOut"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseOut"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseOut"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingResponseOut"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseOut"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseOut"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseOut"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseOut"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseOut"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseOut"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseOut"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseOut"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseOut"]
            ).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseOut"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseOut"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseOut"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartResponseOut"]).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseOut"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseOut"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseOut"]
            ).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseOut"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseOut"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["DuplicateFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DuplicateFilterViewRequestIn"])
    types["DuplicateFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewRequestOut"])
    types["AddNamedRangeRequestIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeRequestIn"])
    types["AddNamedRangeRequestOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeRequestOut"])
    types["CreateDeveloperMetadataResponseIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataResponseIn"])
    types["CreateDeveloperMetadataResponseOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataResponseOut"])
    types["ChartHistogramRuleIn"] = t.struct(
        {
            "intervalSize": t.number().optional(),
            "minValue": t.number().optional(),
            "maxValue": t.number().optional(),
        }
    ).named(renames["ChartHistogramRuleIn"])
    types["ChartHistogramRuleOut"] = t.struct(
        {
            "intervalSize": t.number().optional(),
            "minValue": t.number().optional(),
            "maxValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartHistogramRuleOut"])
    types["DataSourceSheetPropertiesIn"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["DataSourceColumnIn"])).optional(),
        }
    ).named(renames["DataSourceSheetPropertiesIn"])
    types["DataSourceSheetPropertiesOut"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["DataSourceColumnOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSheetPropertiesOut"])
    types["DataSourceRefreshDailyScheduleIn"] = t.struct(
        {"startTime": t.proxy(renames["TimeOfDayIn"]).optional()}
    ).named(renames["DataSourceRefreshDailyScheduleIn"])
    types["DataSourceRefreshDailyScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshDailyScheduleOut"])
    types["ManualRuleGroupIn"] = t.struct(
        {
            "groupName": t.proxy(renames["ExtendedValueIn"]).optional(),
            "items": t.array(t.proxy(renames["ExtendedValueIn"])).optional(),
        }
    ).named(renames["ManualRuleGroupIn"])
    types["ManualRuleGroupOut"] = t.struct(
        {
            "groupName": t.proxy(renames["ExtendedValueOut"]).optional(),
            "items": t.array(t.proxy(renames["ExtendedValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualRuleGroupOut"])
    types["RandomizeRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["RandomizeRangeRequestIn"])
    types["RandomizeRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RandomizeRangeRequestOut"])
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
    types["CandlestickDataIn"] = t.struct(
        {
            "lowSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "openSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "highSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
        }
    ).named(renames["CandlestickDataIn"])
    types["CandlestickDataOut"] = t.struct(
        {
            "lowSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "openSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "highSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickDataOut"])
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
    types["TreemapChartColorScaleIn"] = t.struct(
        {
            "minValueColor": t.proxy(renames["ColorIn"]).optional(),
            "noDataColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "maxValueColor": t.proxy(renames["ColorIn"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "midValueColor": t.proxy(renames["ColorIn"]).optional(),
            "maxValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "minValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "noDataColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleIn"])
    types["TreemapChartColorScaleOut"] = t.struct(
        {
            "minValueColor": t.proxy(renames["ColorOut"]).optional(),
            "noDataColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "maxValueColor": t.proxy(renames["ColorOut"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "midValueColor": t.proxy(renames["ColorOut"]).optional(),
            "maxValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "minValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "noDataColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleOut"])
    types["IterativeCalculationSettingsIn"] = t.struct(
        {
            "maxIterations": t.integer().optional(),
            "convergenceThreshold": t.number().optional(),
        }
    ).named(renames["IterativeCalculationSettingsIn"])
    types["IterativeCalculationSettingsOut"] = t.struct(
        {
            "maxIterations": t.integer().optional(),
            "convergenceThreshold": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IterativeCalculationSettingsOut"])
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
    types["DeleteNamedRangeRequestIn"] = t.struct(
        {"namedRangeId": t.string().optional()}
    ).named(renames["DeleteNamedRangeRequestIn"])
    types["DeleteNamedRangeRequestOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteNamedRangeRequestOut"])
    types["DataSourceColumnReferenceIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["DataSourceColumnReferenceIn"])
    types["DataSourceColumnReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceColumnReferenceOut"])
    types["AddSlicerResponseIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerResponseIn"])
    types["AddSlicerResponseOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerResponseOut"])
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
    types["DeleteDuplicatesRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "comparisonColumns": t.array(
                t.proxy(renames["DimensionRangeIn"])
            ).optional(),
        }
    ).named(renames["DeleteDuplicatesRequestIn"])
    types["DeleteDuplicatesRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "comparisonColumns": t.array(
                t.proxy(renames["DimensionRangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDuplicatesRequestOut"])
    types["HistogramSeriesIn"] = t.struct(
        {
            "barColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "barColor": t.proxy(renames["ColorIn"]).optional(),
            "data": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["HistogramSeriesIn"])
    types["HistogramSeriesOut"] = t.struct(
        {
            "barColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "barColor": t.proxy(renames["ColorOut"]).optional(),
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramSeriesOut"])
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
    types["OrgChartSpecIn"] = t.struct(
        {
            "nodeSize": t.string().optional(),
            "tooltips": t.proxy(renames["ChartDataIn"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "nodeColor": t.proxy(renames["ColorIn"]).optional(),
            "selectedNodeColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["OrgChartSpecIn"])
    types["OrgChartSpecOut"] = t.struct(
        {
            "nodeSize": t.string().optional(),
            "tooltips": t.proxy(renames["ChartDataOut"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "nodeColor": t.proxy(renames["ColorOut"]).optional(),
            "selectedNodeColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgChartSpecOut"])
    types["SlicerSpecIn"] = t.struct(
        {
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "applyToPivotTables": t.boolean().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "title": t.string().optional(),
            "columnIndex": t.integer().optional(),
            "dataRange": t.proxy(renames["GridRangeIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
        }
    ).named(renames["SlicerSpecIn"])
    types["SlicerSpecOut"] = t.struct(
        {
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "applyToPivotTables": t.boolean().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "title": t.string().optional(),
            "columnIndex": t.integer().optional(),
            "dataRange": t.proxy(renames["GridRangeOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerSpecOut"])
    types["FindReplaceRequestIn"] = t.struct(
        {
            "replacement": t.string().optional(),
            "find": t.string().optional(),
            "sheetId": t.integer().optional(),
            "includeFormulas": t.boolean().optional(),
            "matchEntireCell": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "matchCase": t.boolean().optional(),
            "searchByRegex": t.boolean().optional(),
            "allSheets": t.boolean().optional(),
        }
    ).named(renames["FindReplaceRequestIn"])
    types["FindReplaceRequestOut"] = t.struct(
        {
            "replacement": t.string().optional(),
            "find": t.string().optional(),
            "sheetId": t.integer().optional(),
            "includeFormulas": t.boolean().optional(),
            "matchEntireCell": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "matchCase": t.boolean().optional(),
            "searchByRegex": t.boolean().optional(),
            "allSheets": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceRequestOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["DuplicateSheetRequestIn"] = t.struct(
        {
            "insertSheetIndex": t.integer().optional(),
            "newSheetId": t.integer().optional(),
            "sourceSheetId": t.integer().optional(),
            "newSheetName": t.string().optional(),
        }
    ).named(renames["DuplicateSheetRequestIn"])
    types["DuplicateSheetRequestOut"] = t.struct(
        {
            "insertSheetIndex": t.integer().optional(),
            "newSheetId": t.integer().optional(),
            "sourceSheetId": t.integer().optional(),
            "newSheetName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetRequestOut"])
    types["OverlayPositionIn"] = t.struct(
        {
            "anchorCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "heightPixels": t.integer().optional(),
            "offsetYPixels": t.integer().optional(),
            "offsetXPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
        }
    ).named(renames["OverlayPositionIn"])
    types["OverlayPositionOut"] = t.struct(
        {
            "anchorCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "heightPixels": t.integer().optional(),
            "offsetYPixels": t.integer().optional(),
            "offsetXPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OverlayPositionOut"])
    types["DeleteBandingRequestIn"] = t.struct(
        {"bandedRangeId": t.integer().optional()}
    ).named(renames["DeleteBandingRequestIn"])
    types["DeleteBandingRequestOut"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBandingRequestOut"])
    types["BigQueryDataSourceSpecIn"] = t.struct(
        {
            "querySpec": t.proxy(renames["BigQueryQuerySpecIn"]).optional(),
            "tableSpec": t.proxy(renames["BigQueryTableSpecIn"]).optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["BigQueryDataSourceSpecIn"])
    types["BigQueryDataSourceSpecOut"] = t.struct(
        {
            "querySpec": t.proxy(renames["BigQueryQuerySpecOut"]).optional(),
            "tableSpec": t.proxy(renames["BigQueryTableSpecOut"]).optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDataSourceSpecOut"])
    types["ConditionalFormatRuleIn"] = t.struct(
        {
            "booleanRule": t.proxy(renames["BooleanRuleIn"]).optional(),
            "ranges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "gradientRule": t.proxy(renames["GradientRuleIn"]).optional(),
        }
    ).named(renames["ConditionalFormatRuleIn"])
    types["ConditionalFormatRuleOut"] = t.struct(
        {
            "booleanRule": t.proxy(renames["BooleanRuleOut"]).optional(),
            "ranges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "gradientRule": t.proxy(renames["GradientRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionalFormatRuleOut"])
    types["UpdateChartSpecRequestIn"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "spec": t.proxy(renames["ChartSpecIn"]).optional(),
        }
    ).named(renames["UpdateChartSpecRequestIn"])
    types["UpdateChartSpecRequestOut"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "spec": t.proxy(renames["ChartSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateChartSpecRequestOut"])
    types["MatchedValueRangeIn"] = t.struct(
        {
            "valueRange": t.proxy(renames["ValueRangeIn"]).optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
        }
    ).named(renames["MatchedValueRangeIn"])
    types["MatchedValueRangeOut"] = t.struct(
        {
            "valueRange": t.proxy(renames["ValueRangeOut"]).optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchedValueRangeOut"])
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
    types["UpdateEmbeddedObjectPositionRequestIn"] = t.struct(
        {
            "newPosition": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.integer().optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionRequestIn"])
    types["UpdateEmbeddedObjectPositionRequestOut"] = t.struct(
        {
            "newPosition": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "fields": t.string().optional(),
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionRequestOut"])
    types["UpdateConditionalFormatRuleResponseIn"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "newRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "oldIndex": t.integer().optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseIn"])
    types["UpdateConditionalFormatRuleResponseOut"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "newRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "oldIndex": t.integer().optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseOut"])
    types["GradientRuleIn"] = t.struct(
        {
            "midpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
            "maxpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
            "minpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
        }
    ).named(renames["GradientRuleIn"])
    types["GradientRuleOut"] = t.struct(
        {
            "midpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "maxpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "minpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradientRuleOut"])
    types["PivotGroupLimitIn"] = t.struct(
        {"applyOrder": t.integer().optional(), "countLimit": t.integer().optional()}
    ).named(renames["PivotGroupLimitIn"])
    types["PivotGroupLimitOut"] = t.struct(
        {
            "applyOrder": t.integer().optional(),
            "countLimit": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupLimitOut"])
    types["PivotGroupRuleIn"] = t.struct(
        {
            "dateTimeRule": t.proxy(renames["DateTimeRuleIn"]).optional(),
            "histogramRule": t.proxy(renames["HistogramRuleIn"]).optional(),
            "manualRule": t.proxy(renames["ManualRuleIn"]).optional(),
        }
    ).named(renames["PivotGroupRuleIn"])
    types["PivotGroupRuleOut"] = t.struct(
        {
            "dateTimeRule": t.proxy(renames["DateTimeRuleOut"]).optional(),
            "histogramRule": t.proxy(renames["HistogramRuleOut"]).optional(),
            "manualRule": t.proxy(renames["ManualRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupRuleOut"])
    types["UpdateDataSourceRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "dataSource": t.proxy(renames["DataSourceIn"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestIn"])
    types["UpdateDataSourceRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestOut"])
    types["UpdateProtectedRangeRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional(),
        }
    ).named(renames["UpdateProtectedRangeRequestIn"])
    types["UpdateProtectedRangeRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateProtectedRangeRequestOut"])
    types["AddBandingRequestIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingRequestIn"])
    types["AddBandingRequestOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingRequestOut"])
    types["DataSourceParameterIn"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["DataSourceParameterIn"])
    types["DataSourceParameterOut"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceParameterOut"])
    types["DataValidationRuleIn"] = t.struct(
        {
            "strict": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "showCustomUi": t.boolean().optional(),
            "inputMessage": t.string().optional(),
        }
    ).named(renames["DataValidationRuleIn"])
    types["DataValidationRuleOut"] = t.struct(
        {
            "strict": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "showCustomUi": t.boolean().optional(),
            "inputMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataValidationRuleOut"])
    types["SheetPropertiesIn"] = t.struct(
        {
            "tabColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "title": t.string().optional(),
            "tabColor": t.proxy(renames["ColorIn"]).optional(),
            "sheetType": t.string().optional(),
            "hidden": t.boolean().optional(),
            "index": t.integer().optional(),
            "rightToLeft": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesIn"]).optional(),
        }
    ).named(renames["SheetPropertiesIn"])
    types["SheetPropertiesOut"] = t.struct(
        {
            "dataSourceSheetProperties": t.proxy(
                renames["DataSourceSheetPropertiesOut"]
            ).optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "title": t.string().optional(),
            "tabColor": t.proxy(renames["ColorOut"]).optional(),
            "sheetType": t.string().optional(),
            "hidden": t.boolean().optional(),
            "index": t.integer().optional(),
            "rightToLeft": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetPropertiesOut"])
    types["RowDataIn"] = t.struct(
        {"values": t.array(t.proxy(renames["CellDataIn"])).optional()}
    ).named(renames["RowDataIn"])
    types["RowDataOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CellDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowDataOut"])
    types["PivotGroupIn"] = t.struct(
        {
            "groupRule": t.proxy(renames["PivotGroupRuleIn"]).optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataIn"])
            ).optional(),
            "sortOrder": t.string().optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketIn"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "label": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitIn"]).optional(),
            "repeatHeadings": t.boolean().optional(),
            "showTotals": t.boolean().optional(),
        }
    ).named(renames["PivotGroupIn"])
    types["PivotGroupOut"] = t.struct(
        {
            "groupRule": t.proxy(renames["PivotGroupRuleOut"]).optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataOut"])
            ).optional(),
            "sortOrder": t.string().optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketOut"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "label": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitOut"]).optional(),
            "repeatHeadings": t.boolean().optional(),
            "showTotals": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupOut"])
    types["TreemapChartSpecIn"] = t.struct(
        {
            "colorScale": t.proxy(renames["TreemapChartColorScaleIn"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "levels": t.integer().optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "hintedLevels": t.integer().optional(),
            "sizeData": t.proxy(renames["ChartDataIn"]).optional(),
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "minValue": t.number().optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "colorData": t.proxy(renames["ChartDataIn"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "maxValue": t.number().optional(),
        }
    ).named(renames["TreemapChartSpecIn"])
    types["TreemapChartSpecOut"] = t.struct(
        {
            "colorScale": t.proxy(renames["TreemapChartColorScaleOut"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "levels": t.integer().optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "hintedLevels": t.integer().optional(),
            "sizeData": t.proxy(renames["ChartDataOut"]).optional(),
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "minValue": t.number().optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "colorData": t.proxy(renames["ChartDataOut"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "maxValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartSpecOut"])
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
    types["BatchClearValuesRequestIn"] = t.struct(
        {"ranges": t.array(t.string()).optional()}
    ).named(renames["BatchClearValuesRequestIn"])
    types["BatchClearValuesRequestOut"] = t.struct(
        {
            "ranges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesRequestOut"])
    types["DeleteDuplicatesResponseIn"] = t.struct(
        {"duplicatesRemovedCount": t.integer().optional()}
    ).named(renames["DeleteDuplicatesResponseIn"])
    types["DeleteDuplicatesResponseOut"] = t.struct(
        {
            "duplicatesRemovedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDuplicatesResponseOut"])
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
    types["BigQueryTableSpecIn"] = t.struct(
        {
            "tableId": t.string().optional(),
            "tableProjectId": t.string().optional(),
            "datasetId": t.string().optional(),
        }
    ).named(renames["BigQueryTableSpecIn"])
    types["BigQueryTableSpecOut"] = t.struct(
        {
            "tableId": t.string().optional(),
            "tableProjectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryTableSpecOut"])
    types["DateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DateTimeRuleIn"]
    )
    types["DateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeRuleOut"])
    types["AddDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["AddDimensionGroupRequestIn"])
    types["AddDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDimensionGroupRequestOut"])
    types["DeleteConditionalFormatRuleResponseIn"] = t.struct(
        {"rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional()}
    ).named(renames["DeleteConditionalFormatRuleResponseIn"])
    types["DeleteConditionalFormatRuleResponseOut"] = t.struct(
        {
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConditionalFormatRuleResponseOut"])
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
    types["AddSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetResponseIn"])
    types["AddSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetResponseOut"])
    types["WaterfallChartCustomSubtotalIn"] = t.struct(
        {
            "label": t.string().optional(),
            "subtotalIndex": t.integer().optional(),
            "dataIsSubtotal": t.boolean().optional(),
        }
    ).named(renames["WaterfallChartCustomSubtotalIn"])
    types["WaterfallChartCustomSubtotalOut"] = t.struct(
        {
            "label": t.string().optional(),
            "subtotalIndex": t.integer().optional(),
            "dataIsSubtotal": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartCustomSubtotalOut"])
    types["PivotValueIn"] = t.struct(
        {
            "name": t.string().optional(),
            "calculatedDisplayType": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "formula": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "summarizeFunction": t.string().optional(),
        }
    ).named(renames["PivotValueIn"])
    types["PivotValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "calculatedDisplayType": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "formula": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "summarizeFunction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueOut"])
    types["AppendDimensionRequestIn"] = t.struct(
        {
            "length": t.integer().optional(),
            "dimension": t.string().optional(),
            "sheetId": t.integer().optional(),
        }
    ).named(renames["AppendDimensionRequestIn"])
    types["AppendDimensionRequestOut"] = t.struct(
        {
            "length": t.integer().optional(),
            "dimension": t.string().optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendDimensionRequestOut"])
    types["KeyValueFormatIn"] = t.struct(
        {
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "position": t.proxy(renames["TextPositionIn"]).optional(),
        }
    ).named(renames["KeyValueFormatIn"])
    types["KeyValueFormatOut"] = t.struct(
        {
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "position": t.proxy(renames["TextPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueFormatOut"])
    types["FilterCriteriaIn"] = t.struct(
        {
            "hiddenValues": t.array(t.string()).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorIn"]).optional(),
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
        }
    ).named(renames["FilterCriteriaIn"])
    types["FilterCriteriaOut"] = t.struct(
        {
            "hiddenValues": t.array(t.string()).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorOut"]).optional(),
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterCriteriaOut"])
    types["BooleanRuleIn"] = t.struct(
        {
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "format": t.proxy(renames["CellFormatIn"]).optional(),
        }
    ).named(renames["BooleanRuleIn"])
    types["BooleanRuleOut"] = t.struct(
        {
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "format": t.proxy(renames["CellFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanRuleOut"])
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
    types["RefreshDataSourceRequestIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "dataSourceId": t.string().optional(),
            "references": t.proxy(renames["DataSourceObjectReferencesIn"]).optional(),
            "isAll": t.boolean().optional(),
        }
    ).named(renames["RefreshDataSourceRequestIn"])
    types["RefreshDataSourceRequestOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "dataSourceId": t.string().optional(),
            "references": t.proxy(renames["DataSourceObjectReferencesOut"]).optional(),
            "isAll": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshDataSourceRequestOut"])
    types["BasicFilterIn"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
        }
    ).named(renames["BasicFilterIn"])
    types["BasicFilterOut"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicFilterOut"])
    types["AddProtectedRangeResponseIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeResponseIn"])
    types["AddProtectedRangeResponseOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeResponseOut"])
    types["SearchDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["SearchDeveloperMetadataRequestIn"])
    types["SearchDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDeveloperMetadataRequestOut"])
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
    types["SpreadsheetIn"] = t.struct(
        {
            "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
            "spreadsheetUrl": t.string().optional(),
            "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["SpreadsheetIn"])
    types["SpreadsheetOut"] = t.struct(
        {
            "namedRanges": t.array(t.proxy(renames["NamedRangeOut"])).optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "spreadsheetUrl": t.string().optional(),
            "sheets": t.array(t.proxy(renames["SheetOut"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesOut"]).optional(),
            "spreadsheetId": t.string().optional(),
            "dataSourceSchedules": t.array(
                t.proxy(renames["DataSourceRefreshScheduleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetOut"])
    types["WaterfallChartSeriesIn"] = t.struct(
        {
            "hideTrailingSubtotal": t.boolean().optional(),
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "positiveColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "customSubtotals": t.array(
                t.proxy(renames["WaterfallChartCustomSubtotalIn"])
            ).optional(),
            "subtotalColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "data": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["WaterfallChartSeriesIn"])
    types["WaterfallChartSeriesOut"] = t.struct(
        {
            "hideTrailingSubtotal": t.boolean().optional(),
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "positiveColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "customSubtotals": t.array(
                t.proxy(renames["WaterfallChartCustomSubtotalOut"])
            ).optional(),
            "subtotalColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSeriesOut"])
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
    types["DataSourceTableIn"] = t.struct(
        {
            "columnSelectionType": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "dataSourceId": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "rowLimit": t.integer().optional(),
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceIn"])
            ).optional(),
        }
    ).named(renames["DataSourceTableIn"])
    types["DataSourceTableOut"] = t.struct(
        {
            "columnSelectionType": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "dataSourceId": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "rowLimit": t.integer().optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceTableOut"])
    types["DataSourceSpecIn"] = t.struct(
        {
            "bigQuery": t.proxy(renames["BigQueryDataSourceSpecIn"]).optional(),
            "parameters": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
        }
    ).named(renames["DataSourceSpecIn"])
    types["DataSourceSpecOut"] = t.struct(
        {
            "bigQuery": t.proxy(renames["BigQueryDataSourceSpecOut"]).optional(),
            "parameters": t.array(
                t.proxy(renames["DataSourceParameterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSpecOut"])
    types["UpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
            "updatedCells": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "dataFilter": t.proxy(renames["DataFilterIn"]).optional(),
            "updatedColumns": t.integer().optional(),
            "updatedRange": t.string().optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseIn"])
    types["UpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "updatedCells": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "updatedColumns": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseOut"])
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
    types["DataFilterValueRangeIn"] = t.struct(
        {
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "majorDimension": t.string().optional(),
            "dataFilter": t.proxy(renames["DataFilterIn"]).optional(),
        }
    ).named(renames["DataFilterValueRangeIn"])
    types["DataFilterValueRangeOut"] = t.struct(
        {
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "majorDimension": t.string().optional(),
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataFilterValueRangeOut"])
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
    types["WaterfallChartSpecIn"] = t.struct(
        {
            "connectorLineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "series": t.array(t.proxy(renames["WaterfallChartSeriesIn"])).optional(),
            "firstValueIsTotal": t.boolean().optional(),
            "stackedType": t.string().optional(),
            "domain": t.proxy(renames["WaterfallChartDomainIn"]).optional(),
            "hideConnectorLines": t.boolean().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
        }
    ).named(renames["WaterfallChartSpecIn"])
    types["WaterfallChartSpecOut"] = t.struct(
        {
            "connectorLineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "series": t.array(t.proxy(renames["WaterfallChartSeriesOut"])).optional(),
            "firstValueIsTotal": t.boolean().optional(),
            "stackedType": t.string().optional(),
            "domain": t.proxy(renames["WaterfallChartDomainOut"]).optional(),
            "hideConnectorLines": t.boolean().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSpecOut"])
    types["InterpolationPointIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "type": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["InterpolationPointIn"])
    types["InterpolationPointOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "type": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InterpolationPointOut"])
    types["PaddingIn"] = t.struct(
        {
            "top": t.integer().optional(),
            "bottom": t.integer().optional(),
            "left": t.integer().optional(),
            "right": t.integer().optional(),
        }
    ).named(renames["PaddingIn"])
    types["PaddingOut"] = t.struct(
        {
            "top": t.integer().optional(),
            "bottom": t.integer().optional(),
            "left": t.integer().optional(),
            "right": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaddingOut"])
    types["AddNamedRangeResponseIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeResponseIn"])
    types["AddNamedRangeResponseOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeResponseOut"])
    types["GridRangeIn"] = t.struct(
        {
            "startColumnIndex": t.integer().optional(),
            "endRowIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startRowIndex": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
        }
    ).named(renames["GridRangeIn"])
    types["GridRangeOut"] = t.struct(
        {
            "startColumnIndex": t.integer().optional(),
            "endRowIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startRowIndex": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridRangeOut"])
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
    types["DeveloperMetadataLookupIn"] = t.struct(
        {
            "metadataKey": t.string().optional(),
            "locationType": t.string().optional(),
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "metadataId": t.integer().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationIn"]
            ).optional(),
            "locationMatchingStrategy": t.string().optional(),
        }
    ).named(renames["DeveloperMetadataLookupIn"])
    types["DeveloperMetadataLookupOut"] = t.struct(
        {
            "metadataKey": t.string().optional(),
            "locationType": t.string().optional(),
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "metadataId": t.integer().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationOut"]
            ).optional(),
            "locationMatchingStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLookupOut"])
    types["HistogramChartSpecIn"] = t.struct(
        {
            "showItemDividers": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "series": t.array(t.proxy(renames["HistogramSeriesIn"])).optional(),
            "outlierPercentile": t.number().optional(),
            "bucketSize": t.number().optional(),
        }
    ).named(renames["HistogramChartSpecIn"])
    types["HistogramChartSpecOut"] = t.struct(
        {
            "showItemDividers": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "series": t.array(t.proxy(renames["HistogramSeriesOut"])).optional(),
            "outlierPercentile": t.number().optional(),
            "bucketSize": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramChartSpecOut"])
    types["DataSourceObjectReferenceIn"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
            "sheetId": t.string().optional(),
        }
    ).named(renames["DataSourceObjectReferenceIn"])
    types["DataSourceObjectReferenceOut"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "sheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceObjectReferenceOut"])
    types["CreateDeveloperMetadataRequestIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataRequestIn"])
    types["CreateDeveloperMetadataRequestOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataRequestOut"])
    types["SetDataValidationRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "rule": t.proxy(renames["DataValidationRuleIn"]).optional(),
        }
    ).named(renames["SetDataValidationRequestIn"])
    types["SetDataValidationRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "rule": t.proxy(renames["DataValidationRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetDataValidationRequestOut"])
    types["DeleteRangeRequestIn"] = t.struct(
        {
            "shiftDimension": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["DeleteRangeRequestIn"])
    types["DeleteRangeRequestOut"] = t.struct(
        {
            "shiftDimension": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteRangeRequestOut"])
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
    types["SortRangeRequestIn"] = t.struct(
        {
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["SortRangeRequestIn"])
    types["SortRangeRequestOut"] = t.struct(
        {
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortRangeRequestOut"])
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
    types["DuplicateSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["DuplicateSheetResponseIn"])
    types["DuplicateSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetResponseOut"])
    types["PivotTableIn"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecIn"])).optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "values": t.array(t.proxy(renames["PivotValueIn"])).optional(),
            "rows": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "valueLayout": t.string().optional(),
        }
    ).named(renames["PivotTableIn"])
    types["PivotTableOut"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecOut"])).optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "values": t.array(t.proxy(renames["PivotValueOut"])).optional(),
            "rows": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "valueLayout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotTableOut"])
    types["UpdateSheetPropertiesRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "properties": t.proxy(renames["SheetPropertiesIn"]).optional(),
        }
    ).named(renames["UpdateSheetPropertiesRequestIn"])
    types["UpdateSheetPropertiesRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSheetPropertiesRequestOut"])
    types["BandingPropertiesIn"] = t.struct(
        {
            "firstBandColor": t.proxy(renames["ColorIn"]).optional(),
            "footerColor": t.proxy(renames["ColorIn"]).optional(),
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "firstBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "secondBandColor": t.proxy(renames["ColorIn"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BandingPropertiesIn"])
    types["BandingPropertiesOut"] = t.struct(
        {
            "firstBandColor": t.proxy(renames["ColorOut"]).optional(),
            "footerColor": t.proxy(renames["ColorOut"]).optional(),
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "firstBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "secondBandColor": t.proxy(renames["ColorOut"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandingPropertiesOut"])
    types["AddFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewResponseIn"])
    types["AddFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewResponseOut"])
    types["DataSourceFormulaIn"] = t.struct(
        {"dataSourceId": t.string().optional()}
    ).named(renames["DataSourceFormulaIn"])
    types["DataSourceFormulaOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceFormulaOut"])
    types["PivotFilterCriteriaIn"] = t.struct(
        {
            "visibleValues": t.array(t.string()).optional(),
            "visibleByDefault": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
        }
    ).named(renames["PivotFilterCriteriaIn"])
    types["PivotFilterCriteriaOut"] = t.struct(
        {
            "visibleValues": t.array(t.string()).optional(),
            "visibleByDefault": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotFilterCriteriaOut"])
    types["AddSheetRequestIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetRequestIn"])
    types["AddSheetRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetRequestOut"])
    types["DeveloperMetadataLocationIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "dimensionRange": t.proxy(renames["DimensionRangeIn"]).optional(),
            "locationType": t.string().optional(),
            "spreadsheet": t.boolean().optional(),
        }
    ).named(renames["DeveloperMetadataLocationIn"])
    types["DeveloperMetadataLocationOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "dimensionRange": t.proxy(renames["DimensionRangeOut"]).optional(),
            "locationType": t.string().optional(),
            "spreadsheet": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLocationOut"])
    types["DeveloperMetadataIn"] = t.struct(
        {
            "location": t.proxy(renames["DeveloperMetadataLocationIn"]).optional(),
            "metadataId": t.integer().optional(),
            "metadataKey": t.string().optional(),
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
        }
    ).named(renames["DeveloperMetadataIn"])
    types["DeveloperMetadataOut"] = t.struct(
        {
            "location": t.proxy(renames["DeveloperMetadataLocationOut"]).optional(),
            "metadataId": t.integer().optional(),
            "metadataKey": t.string().optional(),
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataOut"])
    types["IntervalIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["IntervalIn"])
    types["IntervalOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntervalOut"])
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
    types["DataExecutionStatusIn"] = t.struct(
        {
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["DataExecutionStatusIn"])
    types["DataExecutionStatusOut"] = t.struct(
        {
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataExecutionStatusOut"])
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
    types["TextFormatIn"] = t.struct(
        {
            "underline": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "strikethrough": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "fontFamily": t.string().optional(),
            "fontSize": t.integer().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["TextFormatIn"])
    types["TextFormatOut"] = t.struct(
        {
            "underline": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "strikethrough": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "fontFamily": t.string().optional(),
            "fontSize": t.integer().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFormatOut"])
    types["SetBasicFilterRequestIn"] = t.struct(
        {"filter": t.proxy(renames["BasicFilterIn"]).optional()}
    ).named(renames["SetBasicFilterRequestIn"])
    types["SetBasicFilterRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["BasicFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetBasicFilterRequestOut"])
    types["GridDataIn"] = t.struct(
        {
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
            "rowData": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "startColumn": t.integer().optional(),
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
            "startRow": t.integer().optional(),
        }
    ).named(renames["GridDataIn"])
    types["GridDataOut"] = t.struct(
        {
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "rowData": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "startColumn": t.integer().optional(),
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "startRow": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridDataOut"])
    types["AutoFillRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "useAlternateSeries": t.boolean().optional(),
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationIn"]
            ).optional(),
        }
    ).named(renames["AutoFillRequestIn"])
    types["AutoFillRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "useAlternateSeries": t.boolean().optional(),
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoFillRequestOut"])
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
    types["UpdateEmbeddedObjectBorderRequestIn"] = t.struct(
        {
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
            "objectId": t.integer().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestIn"])
    types["UpdateEmbeddedObjectBorderRequestOut"] = t.struct(
        {
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "objectId": t.integer().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestOut"])
    types["BatchUpdateValuesRequestIn"] = t.struct(
        {
            "valueInputOption": t.string().optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesRequestIn"])
    types["BatchUpdateValuesRequestOut"] = t.struct(
        {
            "valueInputOption": t.string().optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "data": t.array(t.proxy(renames["ValueRangeOut"])).optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesRequestOut"])
    types["BatchGetValuesByDataFilterResponseIn"] = t.struct(
        {
            "valueRanges": t.array(t.proxy(renames["MatchedValueRangeIn"])).optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterResponseIn"])
    types["BatchGetValuesByDataFilterResponseOut"] = t.struct(
        {
            "valueRanges": t.array(t.proxy(renames["MatchedValueRangeOut"])).optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterResponseOut"])
    types["ScorecardChartSpecIn"] = t.struct(
        {
            "aggregateType": t.string().optional(),
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsIn"]
            ).optional(),
            "numberFormatSource": t.string().optional(),
            "scaleFactor": t.number().optional(),
            "baselineValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "keyValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "baselineValueFormat": t.proxy(renames["BaselineValueFormatIn"]).optional(),
            "keyValueFormat": t.proxy(renames["KeyValueFormatIn"]).optional(),
        }
    ).named(renames["ScorecardChartSpecIn"])
    types["ScorecardChartSpecOut"] = t.struct(
        {
            "aggregateType": t.string().optional(),
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsOut"]
            ).optional(),
            "numberFormatSource": t.string().optional(),
            "scaleFactor": t.number().optional(),
            "baselineValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "keyValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "baselineValueFormat": t.proxy(
                renames["BaselineValueFormatOut"]
            ).optional(),
            "keyValueFormat": t.proxy(renames["KeyValueFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScorecardChartSpecOut"])
    types["UpdateDeveloperMetadataRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestIn"])
    types["UpdateDeveloperMetadataRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestOut"])
    types["BooleanConditionIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ConditionValueIn"])).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["BooleanConditionIn"])
    types["BooleanConditionOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ConditionValueOut"])).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanConditionOut"])
    types["PieChartSpecIn"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "threeDimensional": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "pieHole": t.number().optional(),
        }
    ).named(renames["PieChartSpecIn"])
    types["PieChartSpecOut"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "threeDimensional": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "pieHole": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PieChartSpecOut"])
    types["DeleteDataSourceRequestIn"] = t.struct(
        {"dataSourceId": t.string().optional()}
    ).named(renames["DeleteDataSourceRequestIn"])
    types["DeleteDataSourceRequestOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDataSourceRequestOut"])
    types["EmbeddedChartIn"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
            "spec": t.proxy(renames["ChartSpecIn"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
        }
    ).named(renames["EmbeddedChartIn"])
    types["EmbeddedChartOut"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "spec": t.proxy(renames["ChartSpecOut"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedChartOut"])
    types["DeleteFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DeleteFilterViewRequestIn"])
    types["DeleteFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFilterViewRequestOut"])
    types["PivotGroupValueMetadataIn"] = t.struct(
        {
            "value": t.proxy(renames["ExtendedValueIn"]).optional(),
            "collapsed": t.boolean().optional(),
        }
    ).named(renames["PivotGroupValueMetadataIn"])
    types["PivotGroupValueMetadataOut"] = t.struct(
        {
            "value": t.proxy(renames["ExtendedValueOut"]).optional(),
            "collapsed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupValueMetadataOut"])
    types["DataLabelIn"] = t.struct(
        {
            "type": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "placement": t.string().optional(),
            "customLabelData": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["DataLabelIn"])
    types["DataLabelOut"] = t.struct(
        {
            "type": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "placement": t.string().optional(),
            "customLabelData": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLabelOut"])
    types["TrimWhitespaceRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["TrimWhitespaceRequestIn"])
    types["TrimWhitespaceRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceRequestOut"])
    types["TrimWhitespaceResponseIn"] = t.struct(
        {"cellsChangedCount": t.integer().optional()}
    ).named(renames["TrimWhitespaceResponseIn"])
    types["TrimWhitespaceResponseOut"] = t.struct(
        {
            "cellsChangedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceResponseOut"])
    types["HistogramRuleIn"] = t.struct(
        {
            "interval": t.number().optional(),
            "start": t.number().optional(),
            "end": t.number().optional(),
        }
    ).named(renames["HistogramRuleIn"])
    types["HistogramRuleOut"] = t.struct(
        {
            "interval": t.number().optional(),
            "start": t.number().optional(),
            "end": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramRuleOut"])
    types["UpdateDimensionPropertiesRequestIn"] = t.struct(
        {
            "properties": t.proxy(renames["DimensionPropertiesIn"]).optional(),
            "dataSourceSheetRange": t.proxy(
                renames["DataSourceSheetDimensionRangeIn"]
            ).optional(),
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateDimensionPropertiesRequestIn"])
    types["UpdateDimensionPropertiesRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["DimensionPropertiesOut"]).optional(),
            "dataSourceSheetRange": t.proxy(
                renames["DataSourceSheetDimensionRangeOut"]
            ).optional(),
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDimensionPropertiesRequestOut"])
    types["UpdateDataSourceResponseIn"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceIn"]).optional(),
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
        }
    ).named(renames["UpdateDataSourceResponseIn"])
    types["UpdateDataSourceResponseOut"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDataSourceResponseOut"])
    types["BatchUpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseIn"])
            ).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseIn"])
    types["BatchUpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseOut"])
    types["NumberFormatIn"] = t.struct(
        {"type": t.string().optional(), "pattern": t.string().optional()}
    ).named(renames["NumberFormatIn"])
    types["NumberFormatOut"] = t.struct(
        {
            "type": t.string().optional(),
            "pattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NumberFormatOut"])
    types["DimensionGroupIn"] = t.struct(
        {
            "collapsed": t.boolean().optional(),
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
            "depth": t.integer().optional(),
        }
    ).named(renames["DimensionGroupIn"])
    types["DimensionGroupOut"] = t.struct(
        {
            "collapsed": t.boolean().optional(),
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "depth": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionGroupOut"])
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
    types["PasteDataRequestIn"] = t.struct(
        {
            "coordinate": t.proxy(renames["GridCoordinateIn"]).optional(),
            "html": t.boolean().optional(),
            "type": t.string().optional(),
            "data": t.string().optional(),
            "delimiter": t.string().optional(),
        }
    ).named(renames["PasteDataRequestIn"])
    types["PasteDataRequestOut"] = t.struct(
        {
            "coordinate": t.proxy(renames["GridCoordinateOut"]).optional(),
            "html": t.boolean().optional(),
            "type": t.string().optional(),
            "data": t.string().optional(),
            "delimiter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasteDataRequestOut"])
    types["AddChartResponseIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartResponseIn"])
    types["AddChartResponseOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartResponseOut"])
    types["BandedRangeIn"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "rowProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "columnProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
        }
    ).named(renames["BandedRangeIn"])
    types["BandedRangeOut"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "rowProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "columnProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandedRangeOut"])
    types["CellFormatIn"] = t.struct(
        {
            "wrapStrategy": t.string().optional(),
            "padding": t.proxy(renames["PaddingIn"]).optional(),
            "borders": t.proxy(renames["BordersIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "numberFormat": t.proxy(renames["NumberFormatIn"]).optional(),
            "textRotation": t.proxy(renames["TextRotationIn"]).optional(),
            "verticalAlignment": t.string().optional(),
            "textDirection": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["CellFormatIn"])
    types["CellFormatOut"] = t.struct(
        {
            "wrapStrategy": t.string().optional(),
            "padding": t.proxy(renames["PaddingOut"]).optional(),
            "borders": t.proxy(renames["BordersOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "numberFormat": t.proxy(renames["NumberFormatOut"]).optional(),
            "textRotation": t.proxy(renames["TextRotationOut"]).optional(),
            "verticalAlignment": t.string().optional(),
            "textDirection": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellFormatOut"])
    types["UnmergeCellsRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["UnmergeCellsRequestIn"])
    types["UnmergeCellsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeCellsRequestOut"])
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
    types["BatchUpdateSpreadsheetResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "updatedSpreadsheet": t.proxy(renames["SpreadsheetIn"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetResponseIn"])
    types["BatchUpdateSpreadsheetResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "updatedSpreadsheet": t.proxy(renames["SpreadsheetOut"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetResponseOut"])
    types["DeleteDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionGroupRequestIn"])
    types["DeleteDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionGroupRequestOut"])
    types["AddFilterViewRequestIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewRequestIn"])
    types["AddFilterViewRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewRequestOut"])
    types["CopySheetToAnotherSpreadsheetRequestIn"] = t.struct(
        {"destinationSpreadsheetId": t.string().optional()}
    ).named(renames["CopySheetToAnotherSpreadsheetRequestIn"])
    types["CopySheetToAnotherSpreadsheetRequestOut"] = t.struct(
        {
            "destinationSpreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopySheetToAnotherSpreadsheetRequestOut"])
    types["DuplicateFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["DuplicateFilterViewResponseIn"])
    types["DuplicateFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewResponseOut"])
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
    types["UpdateFilterViewRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "filter": t.proxy(renames["FilterViewIn"]).optional(),
        }
    ).named(renames["UpdateFilterViewRequestIn"])
    types["UpdateFilterViewRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFilterViewRequestOut"])
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
    types["BasicChartDomainIn"] = t.struct(
        {
            "reversed": t.boolean().optional(),
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["BasicChartDomainIn"])
    types["BasicChartDomainOut"] = t.struct(
        {
            "reversed": t.boolean().optional(),
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartDomainOut"])
    types["BatchUpdateValuesResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(t.proxy(renames["UpdateValuesResponseIn"])).optional(),
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedRows": t.integer().optional(),
        }
    ).named(renames["BatchUpdateValuesResponseIn"])
    types["BatchUpdateValuesResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesResponseOut"])
            ).optional(),
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesResponseOut"])
    types["BordersIn"] = t.struct(
        {
            "left": t.proxy(renames["BorderIn"]).optional(),
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "right": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["BordersIn"])
    types["BordersOut"] = t.struct(
        {
            "left": t.proxy(renames["BorderOut"]).optional(),
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "right": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BordersOut"])
    types["ChartDataIn"] = t.struct(
        {
            "groupRule": t.proxy(renames["ChartGroupRuleIn"]).optional(),
            "columnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "sourceRange": t.proxy(renames["ChartSourceRangeIn"]).optional(),
            "aggregateType": t.string().optional(),
        }
    ).named(renames["ChartDataIn"])
    types["ChartDataOut"] = t.struct(
        {
            "groupRule": t.proxy(renames["ChartGroupRuleOut"]).optional(),
            "columnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "sourceRange": t.proxy(renames["ChartSourceRangeOut"]).optional(),
            "aggregateType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDataOut"])
    types["FindReplaceResponseIn"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "valuesChanged": t.integer().optional(),
            "sheetsChanged": t.integer().optional(),
            "formulasChanged": t.integer().optional(),
            "rowsChanged": t.integer().optional(),
        }
    ).named(renames["FindReplaceResponseIn"])
    types["FindReplaceResponseOut"] = t.struct(
        {
            "occurrencesChanged": t.integer().optional(),
            "valuesChanged": t.integer().optional(),
            "sheetsChanged": t.integer().optional(),
            "formulasChanged": t.integer().optional(),
            "rowsChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceResponseOut"])
    types["DimensionPropertiesIn"] = t.struct(
        {
            "hiddenByFilter": t.boolean().optional(),
            "hiddenByUser": t.boolean().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "pixelSize": t.integer().optional(),
        }
    ).named(renames["DimensionPropertiesIn"])
    types["DimensionPropertiesOut"] = t.struct(
        {
            "hiddenByFilter": t.boolean().optional(),
            "hiddenByUser": t.boolean().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "pixelSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionPropertiesOut"])
    types["LineStyleIn"] = t.struct(
        {"width": t.integer().optional(), "type": t.string().optional()}
    ).named(renames["LineStyleIn"])
    types["LineStyleOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineStyleOut"])
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
    types["FilterViewIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "namedRangeId": t.string().optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "title": t.string().optional(),
            "filterViewId": t.integer().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
        }
    ).named(renames["FilterViewIn"])
    types["FilterViewOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "namedRangeId": t.string().optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "title": t.string().optional(),
            "filterViewId": t.integer().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterViewOut"])
    types["RepeatCellRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "cell": t.proxy(renames["CellDataIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["RepeatCellRequestIn"])
    types["RepeatCellRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "cell": t.proxy(renames["CellDataOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepeatCellRequestOut"])
    types["TextPositionIn"] = t.struct(
        {"horizontalAlignment": t.string().optional()}
    ).named(renames["TextPositionIn"])
    types["TextPositionOut"] = t.struct(
        {
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPositionOut"])
    types["DimensionRangeIn"] = t.struct(
        {
            "endIndex": t.integer().optional(),
            "dimension": t.string().optional(),
            "sheetId": t.integer().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["DimensionRangeIn"])
    types["DimensionRangeOut"] = t.struct(
        {
            "endIndex": t.integer().optional(),
            "dimension": t.string().optional(),
            "sheetId": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionRangeOut"])
    types["BatchClearValuesByDataFilterRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["BatchClearValuesByDataFilterRequestIn"])
    types["BatchClearValuesByDataFilterRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterRequestOut"])
    types["SourceAndDestinationIn"] = t.struct(
        {
            "dimension": t.string().optional(),
            "fillLength": t.integer().optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["SourceAndDestinationIn"])
    types["SourceAndDestinationOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "fillLength": t.integer().optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceAndDestinationOut"])
    types["BasicChartSeriesIn"] = t.struct(
        {
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "type": t.string().optional(),
            "lineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideIn"])
            ).optional(),
            "targetAxis": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["BasicChartSeriesIn"])
    types["BasicChartSeriesOut"] = t.struct(
        {
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "type": t.string().optional(),
            "lineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideOut"])
            ).optional(),
            "targetAxis": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSeriesOut"])
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
    types["DeleteProtectedRangeRequestIn"] = t.struct(
        {"protectedRangeId": t.integer().optional()}
    ).named(renames["DeleteProtectedRangeRequestIn"])
    types["DeleteProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteProtectedRangeRequestOut"])
    types["EmbeddedObjectBorderIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderIn"])
    types["EmbeddedObjectBorderOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectBorderOut"])
    types["AddSlicerRequestIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerRequestIn"])
    types["AddSlicerRequestOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerRequestOut"])
    types["BubbleChartSpecIn"] = t.struct(
        {
            "bubbleSizes": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleBorderColor": t.proxy(renames["ColorIn"]).optional(),
            "bubbleOpacity": t.number().optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatIn"]).optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleMaxRadiusSize": t.integer().optional(),
            "groupIds": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "legendPosition": t.string().optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "bubbleLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["BubbleChartSpecIn"])
    types["BubbleChartSpecOut"] = t.struct(
        {
            "bubbleSizes": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleBorderColor": t.proxy(renames["ColorOut"]).optional(),
            "bubbleOpacity": t.number().optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatOut"]).optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleMaxRadiusSize": t.integer().optional(),
            "groupIds": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "legendPosition": t.string().optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "bubbleLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BubbleChartSpecOut"])
    types["MergeCellsRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "mergeType": t.string().optional(),
        }
    ).named(renames["MergeCellsRequestIn"])
    types["MergeCellsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "mergeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeCellsRequestOut"])
    types["ClearValuesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClearValuesRequestIn"]
    )
    types["ClearValuesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearValuesRequestOut"])
    types["BatchUpdateSpreadsheetRequestIn"] = t.struct(
        {
            "responseRanges": t.array(t.string()).optional(),
            "responseIncludeGridData": t.boolean().optional(),
            "includeSpreadsheetInResponse": t.boolean().optional(),
            "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetRequestIn"])
    types["BatchUpdateSpreadsheetRequestOut"] = t.struct(
        {
            "responseRanges": t.array(t.string()).optional(),
            "responseIncludeGridData": t.boolean().optional(),
            "includeSpreadsheetInResponse": t.boolean().optional(),
            "requests": t.array(t.proxy(renames["RequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetRequestOut"])
    types["UpdateBordersRequestIn"] = t.struct(
        {
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "innerVertical": t.proxy(renames["BorderIn"]).optional(),
            "right": t.proxy(renames["BorderIn"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "left": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["UpdateBordersRequestIn"])
    types["UpdateBordersRequestOut"] = t.struct(
        {
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "innerVertical": t.proxy(renames["BorderOut"]).optional(),
            "right": t.proxy(renames["BorderOut"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "left": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBordersRequestOut"])
    types["SortSpecIn"] = t.struct(
        {
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "dimensionIndex": t.integer().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "sortOrder": t.string().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["SortSpecIn"])
    types["SortSpecOut"] = t.struct(
        {
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "dimensionIndex": t.integer().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "sortOrder": t.string().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortSpecOut"])
    types["ExtendedValueIn"] = t.struct(
        {
            "numberValue": t.number().optional(),
            "errorValue": t.proxy(renames["ErrorValueIn"]).optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "formulaValue": t.string().optional(),
        }
    ).named(renames["ExtendedValueIn"])
    types["ExtendedValueOut"] = t.struct(
        {
            "numberValue": t.number().optional(),
            "errorValue": t.proxy(renames["ErrorValueOut"]).optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "formulaValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedValueOut"])
    types["RequestIn"] = t.struct(
        {
            "pasteData": t.proxy(renames["PasteDataRequestIn"]).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestIn"]
            ).optional(),
            "updateBorders": t.proxy(renames["UpdateBordersRequestIn"]).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestIn"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestIn"]).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestIn"]).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestIn"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestIn"]
            ).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestIn"]
            ).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestIn"]).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestIn"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestIn"]
            ).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestIn"]).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestIn"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestIn"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestIn"]).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestIn"]
            ).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestIn"]).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestIn"]
            ).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestIn"]
            ).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestIn"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestIn"]).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestIn"]
            ).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestIn"]
            ).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestIn"]
            ).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestIn"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartRequestIn"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestIn"]).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestIn"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestIn"]).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestIn"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestIn"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestIn"]
            ).optional(),
            "updateBanding": t.proxy(renames["UpdateBandingRequestIn"]).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestIn"]).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestIn"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestIn"]).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestIn"]).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestIn"]).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestIn"]).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestIn"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestIn"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestIn"]
            ).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestIn"]
            ).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestIn"]).optional(),
            "copyPaste": t.proxy(renames["CopyPasteRequestIn"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestIn"]
            ).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestIn"]
            ).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestIn"]).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestIn"]).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestIn"]
            ).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestIn"]).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestIn"]
            ).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestIn"]).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestIn"]).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestIn"]
            ).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestIn"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestIn"]
            ).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestIn"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestIn"]
            ).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestIn"]).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestIn"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestIn"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "pasteData": t.proxy(renames["PasteDataRequestOut"]).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestOut"]
            ).optional(),
            "updateBorders": t.proxy(renames["UpdateBordersRequestOut"]).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestOut"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestOut"]).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestOut"]).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestOut"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestOut"]
            ).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestOut"]
            ).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestOut"]).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestOut"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestOut"]
            ).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestOut"]).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestOut"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestOut"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestOut"]).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestOut"]
            ).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestOut"]).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestOut"]
            ).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestOut"]
            ).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestOut"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestOut"]).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestOut"]
            ).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestOut"]
            ).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestOut"]
            ).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestOut"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartRequestOut"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestOut"]).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestOut"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestOut"]).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestOut"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestOut"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestOut"]
            ).optional(),
            "updateBanding": t.proxy(renames["UpdateBandingRequestOut"]).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestOut"]).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestOut"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestOut"]).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestOut"]).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestOut"]).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestOut"]).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestOut"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestOut"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestOut"]
            ).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestOut"]
            ).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestOut"]).optional(),
            "copyPaste": t.proxy(renames["CopyPasteRequestOut"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestOut"]
            ).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestOut"]
            ).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestOut"]).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestOut"]).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestOut"]
            ).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestOut"]).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestOut"]
            ).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestOut"]).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestOut"]).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestOut"]
            ).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestOut"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestOut"]
            ).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestOut"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestOut"]
            ).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestOut"]).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestOut"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestOut"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["AddChartRequestIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartRequestIn"])
    types["AddChartRequestOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartRequestOut"])
    types["UpdateEmbeddedObjectPositionResponseIn"] = t.struct(
        {"position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional()}
    ).named(renames["UpdateEmbeddedObjectPositionResponseIn"])
    types["UpdateEmbeddedObjectPositionResponseOut"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionResponseOut"])
    types["BasicSeriesDataPointStyleOverrideIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "index": t.integer().optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideIn"])
    types["BasicSeriesDataPointStyleOverrideOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "index": t.integer().optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideOut"])
    types["ChartSourceRangeIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["GridRangeIn"])).optional()}
    ).named(renames["ChartSourceRangeIn"])
    types["ChartSourceRangeOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSourceRangeOut"])
    types["DataSourceColumnIn"] = t.struct(
        {
            "reference": t.proxy(renames["DataSourceColumnReferenceIn"]).optional(),
            "formula": t.string().optional(),
        }
    ).named(renames["DataSourceColumnIn"])
    types["DataSourceColumnOut"] = t.struct(
        {
            "reference": t.proxy(renames["DataSourceColumnReferenceOut"]).optional(),
            "formula": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceColumnOut"])
    types["ChartDateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ChartDateTimeRuleIn"]
    )
    types["ChartDateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDateTimeRuleOut"])
    types["DeleteSheetRequestIn"] = t.struct({"sheetId": t.integer().optional()}).named(
        renames["DeleteSheetRequestIn"]
    )
    types["DeleteSheetRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteSheetRequestOut"])
    types["AddProtectedRangeRequestIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeRequestIn"])
    types["AddProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeRequestOut"])
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
    types["ProtectedRangeIn"] = t.struct(
        {
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "requestingUserCanEdit": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "description": t.string().optional(),
            "editors": t.proxy(renames["EditorsIn"]).optional(),
            "namedRangeId": t.string().optional(),
            "protectedRangeId": t.integer().optional(),
            "warningOnly": t.boolean().optional(),
        }
    ).named(renames["ProtectedRangeIn"])
    types["ProtectedRangeOut"] = t.struct(
        {
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "requestingUserCanEdit": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "description": t.string().optional(),
            "editors": t.proxy(renames["EditorsOut"]).optional(),
            "namedRangeId": t.string().optional(),
            "protectedRangeId": t.integer().optional(),
            "warningOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProtectedRangeOut"])
    types["WaterfallChartDomainIn"] = t.struct(
        {
            "reversed": t.boolean().optional(),
            "data": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["WaterfallChartDomainIn"])
    types["WaterfallChartDomainOut"] = t.struct(
        {
            "reversed": t.boolean().optional(),
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartDomainOut"])
    types["AddDataSourceRequestIn"] = t.struct(
        {"dataSource": t.proxy(renames["DataSourceIn"]).optional()}
    ).named(renames["AddDataSourceRequestIn"])
    types["AddDataSourceRequestOut"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDataSourceRequestOut"])
    types["ClearBasicFilterRequestIn"] = t.struct(
        {"sheetId": t.integer().optional()}
    ).named(renames["ClearBasicFilterRequestIn"])
    types["ClearBasicFilterRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearBasicFilterRequestOut"])
    types["CandlestickDomainIn"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataIn"]).optional(),
            "reversed": t.boolean().optional(),
        }
    ).named(renames["CandlestickDomainIn"])
    types["CandlestickDomainOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "reversed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickDomainOut"])
    types["BasicChartSpecIn"] = t.struct(
        {
            "interpolateNulls": t.boolean().optional(),
            "stackedType": t.string().optional(),
            "axis": t.array(t.proxy(renames["BasicChartAxisIn"])).optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesIn"])).optional(),
            "compareMode": t.string().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "headerCount": t.integer().optional(),
            "lineSmoothing": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainIn"])).optional(),
            "threeDimensional": t.boolean().optional(),
            "chartType": t.string().optional(),
        }
    ).named(renames["BasicChartSpecIn"])
    types["BasicChartSpecOut"] = t.struct(
        {
            "interpolateNulls": t.boolean().optional(),
            "stackedType": t.string().optional(),
            "axis": t.array(t.proxy(renames["BasicChartAxisOut"])).optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesOut"])).optional(),
            "compareMode": t.string().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "headerCount": t.integer().optional(),
            "lineSmoothing": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainOut"])).optional(),
            "threeDimensional": t.boolean().optional(),
            "chartType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSpecOut"])
    types["DataSourceRefreshWeeklyScheduleIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "daysOfWeek": t.array(t.string()).optional(),
        }
    ).named(renames["DataSourceRefreshWeeklyScheduleIn"])
    types["DataSourceRefreshWeeklyScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "daysOfWeek": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshWeeklyScheduleOut"])
    types["ChartSpecIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecIn"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "fontName": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecIn"]).optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecIn"]).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecIn"]).optional(),
            "maximized": t.boolean().optional(),
            "candlestickChart": t.proxy(renames["CandlestickChartSpecIn"]).optional(),
            "altText": t.string().optional(),
            "treemapChart": t.proxy(renames["TreemapChartSpecIn"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "pieChart": t.proxy(renames["PieChartSpecIn"]).optional(),
            "basicChart": t.proxy(renames["BasicChartSpecIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesIn"]
            ).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecIn"]).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
        }
    ).named(renames["ChartSpecIn"])
    types["ChartSpecOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecOut"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "fontName": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecOut"]).optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecOut"]).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecOut"]).optional(),
            "maximized": t.boolean().optional(),
            "candlestickChart": t.proxy(renames["CandlestickChartSpecOut"]).optional(),
            "altText": t.string().optional(),
            "treemapChart": t.proxy(renames["TreemapChartSpecOut"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "pieChart": t.proxy(renames["PieChartSpecOut"]).optional(),
            "basicChart": t.proxy(renames["BasicChartSpecOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesOut"]
            ).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecOut"]).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSpecOut"])
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
    types["GridPropertiesIn"] = t.struct(
        {
            "columnCount": t.integer().optional(),
            "hideGridlines": t.boolean().optional(),
            "frozenRowCount": t.integer().optional(),
            "rowGroupControlAfter": t.boolean().optional(),
            "frozenColumnCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
        }
    ).named(renames["GridPropertiesIn"])
    types["GridPropertiesOut"] = t.struct(
        {
            "columnCount": t.integer().optional(),
            "hideGridlines": t.boolean().optional(),
            "frozenRowCount": t.integer().optional(),
            "rowGroupControlAfter": t.boolean().optional(),
            "frozenColumnCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridPropertiesOut"])
    types["BatchGetValuesByDataFilterRequestIn"] = t.struct(
        {
            "dateTimeRenderOption": t.string().optional(),
            "valueRenderOption": t.string().optional(),
            "majorDimension": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestIn"])
    types["BatchGetValuesByDataFilterRequestOut"] = t.struct(
        {
            "dateTimeRenderOption": t.string().optional(),
            "valueRenderOption": t.string().optional(),
            "majorDimension": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestOut"])
    types["AddBandingResponseIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingResponseIn"])
    types["AddBandingResponseOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingResponseOut"])
    types["CopyPasteRequestIn"] = t.struct(
        {
            "destination": t.proxy(renames["GridRangeIn"]).optional(),
            "pasteType": t.string().optional(),
            "pasteOrientation": t.string().optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["CopyPasteRequestIn"])
    types["CopyPasteRequestOut"] = t.struct(
        {
            "destination": t.proxy(renames["GridRangeOut"]).optional(),
            "pasteType": t.string().optional(),
            "pasteOrientation": t.string().optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyPasteRequestOut"])
    types["BaselineValueFormatIn"] = t.struct(
        {
            "position": t.proxy(renames["TextPositionIn"]).optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "negativeColor": t.proxy(renames["ColorIn"]).optional(),
            "description": t.string().optional(),
            "comparisonType": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "positiveColor": t.proxy(renames["ColorIn"]).optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BaselineValueFormatIn"])
    types["BaselineValueFormatOut"] = t.struct(
        {
            "position": t.proxy(renames["TextPositionOut"]).optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "negativeColor": t.proxy(renames["ColorOut"]).optional(),
            "description": t.string().optional(),
            "comparisonType": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "positiveColor": t.proxy(renames["ColorOut"]).optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BaselineValueFormatOut"])
    types["DeleteEmbeddedObjectRequestIn"] = t.struct(
        {"objectId": t.integer().optional()}
    ).named(renames["DeleteEmbeddedObjectRequestIn"])
    types["DeleteEmbeddedObjectRequestOut"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteEmbeddedObjectRequestOut"])
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
    types["CellDataIn"] = t.struct(
        {
            "note": t.string().optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunIn"])).optional(),
            "dataValidation": t.proxy(renames["DataValidationRuleIn"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableIn"]).optional(),
            "hyperlink": t.string().optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableIn"]).optional(),
            "userEnteredValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "effectiveFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "effectiveValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "formattedValue": t.string().optional(),
        }
    ).named(renames["CellDataIn"])
    types["CellDataOut"] = t.struct(
        {
            "note": t.string().optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunOut"])).optional(),
            "dataValidation": t.proxy(renames["DataValidationRuleOut"]).optional(),
            "dataSourceFormula": t.proxy(renames["DataSourceFormulaOut"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableOut"]).optional(),
            "hyperlink": t.string().optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableOut"]).optional(),
            "userEnteredValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "effectiveFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "effectiveValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "formattedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellDataOut"])
    types["LinkIn"] = t.struct({"uri": t.string().optional()}).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["DeleteDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilter": t.proxy(renames["DataFilterIn"]).optional()}
    ).named(renames["DeleteDeveloperMetadataRequestIn"])
    types["DeleteDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDeveloperMetadataRequestOut"])
    types["BatchUpdateValuesByDataFilterRequestIn"] = t.struct(
        {
            "valueInputOption": t.string().optional(),
            "data": t.array(t.proxy(renames["DataFilterValueRangeIn"])).optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "responseValueRenderOption": t.string().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestIn"])
    types["BatchUpdateValuesByDataFilterRequestOut"] = t.struct(
        {
            "valueInputOption": t.string().optional(),
            "data": t.array(t.proxy(renames["DataFilterValueRangeOut"])).optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "responseValueRenderOption": t.string().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestOut"])
    types["UpdateSpreadsheetPropertiesRequestIn"] = t.struct(
        {
            "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateSpreadsheetPropertiesRequestIn"])
    types["UpdateSpreadsheetPropertiesRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["SpreadsheetPropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSpreadsheetPropertiesRequestOut"])
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
    types["BigQueryQuerySpecIn"] = t.struct({"rawQuery": t.string().optional()}).named(
        renames["BigQueryQuerySpecIn"]
    )
    types["BigQueryQuerySpecOut"] = t.struct(
        {
            "rawQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryQuerySpecOut"])
    types["DataSourceIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "calculatedColumns": t.array(
                t.proxy(renames["DataSourceColumnIn"])
            ).optional(),
            "dataSourceId": t.string().optional(),
            "spec": t.proxy(renames["DataSourceSpecIn"]).optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "calculatedColumns": t.array(
                t.proxy(renames["DataSourceColumnOut"])
            ).optional(),
            "dataSourceId": t.string().optional(),
            "spec": t.proxy(renames["DataSourceSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
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
    types["CutPasteRequestIn"] = t.struct(
        {
            "pasteType": t.string().optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "destination": t.proxy(renames["GridCoordinateIn"]).optional(),
        }
    ).named(renames["CutPasteRequestIn"])
    types["CutPasteRequestOut"] = t.struct(
        {
            "pasteType": t.string().optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "destination": t.proxy(renames["GridCoordinateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutPasteRequestOut"])
    types["AutoResizeDimensionsRequestIn"] = t.struct(
        {
            "dataSourceSheetDimensions": t.proxy(
                renames["DataSourceSheetDimensionRangeIn"]
            ).optional(),
            "dimensions": t.proxy(renames["DimensionRangeIn"]).optional(),
        }
    ).named(renames["AutoResizeDimensionsRequestIn"])
    types["AutoResizeDimensionsRequestOut"] = t.struct(
        {
            "dataSourceSheetDimensions": t.proxy(
                renames["DataSourceSheetDimensionRangeOut"]
            ).optional(),
            "dimensions": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoResizeDimensionsRequestOut"])
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
    types["ValueRangeIn"] = t.struct(
        {
            "range": t.string().optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "majorDimension": t.string().optional(),
        }
    ).named(renames["ValueRangeIn"])
    types["ValueRangeOut"] = t.struct(
        {
            "range": t.string().optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "majorDimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueRangeOut"])
    types["CandlestickSeriesIn"] = t.struct(
        {"data": t.proxy(renames["ChartDataIn"]).optional()}
    ).named(renames["CandlestickSeriesIn"])
    types["CandlestickSeriesOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickSeriesOut"])
    types["UpdateBandingRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "bandedRange": t.proxy(renames["BandedRangeIn"]).optional(),
        }
    ).named(renames["UpdateBandingRequestIn"])
    types["UpdateBandingRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBandingRequestOut"])
    types["EditorsIn"] = t.struct(
        {
            "users": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "domainUsersCanEdit": t.boolean().optional(),
        }
    ).named(renames["EditorsIn"])
    types["EditorsOut"] = t.struct(
        {
            "users": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "domainUsersCanEdit": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditorsOut"])
    types["BorderIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "width": t.integer().optional(),
            "style": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BorderIn"])
    types["BorderOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "width": t.integer().optional(),
            "style": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BorderOut"])
    types["SheetIn"] = t.struct(
        {
            "bandedRanges": t.array(t.proxy(renames["BandedRangeIn"])).optional(),
            "columnGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartIn"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterIn"]).optional(),
            "data": t.array(t.proxy(renames["GridDataIn"])).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "properties": t.proxy(renames["SheetPropertiesIn"]).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleIn"])
            ).optional(),
            "merges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewIn"])).optional(),
            "slicers": t.array(t.proxy(renames["SlicerIn"])).optional(),
            "protectedRanges": t.array(t.proxy(renames["ProtectedRangeIn"])).optional(),
        }
    ).named(renames["SheetIn"])
    types["SheetOut"] = t.struct(
        {
            "bandedRanges": t.array(t.proxy(renames["BandedRangeOut"])).optional(),
            "columnGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartOut"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterOut"]).optional(),
            "data": t.array(t.proxy(renames["GridDataOut"])).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleOut"])
            ).optional(),
            "merges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewOut"])).optional(),
            "slicers": t.array(t.proxy(renames["SlicerOut"])).optional(),
            "protectedRanges": t.array(
                t.proxy(renames["ProtectedRangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetOut"])
    types["WaterfallChartColumnStyleIn"] = t.struct(
        {
            "label": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["WaterfallChartColumnStyleIn"])
    types["WaterfallChartColumnStyleOut"] = t.struct(
        {
            "label": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartColumnStyleOut"])
    types["UpdateConditionalFormatRuleRequestIn"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestIn"])
    types["UpdateConditionalFormatRuleRequestOut"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestOut"])
    types["ColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["AddConditionalFormatRuleRequestIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
        }
    ).named(renames["AddConditionalFormatRuleRequestIn"])
    types["AddConditionalFormatRuleRequestOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddConditionalFormatRuleRequestOut"])
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
    types["ConditionValueIn"] = t.struct(
        {
            "relativeDate": t.string().optional(),
            "userEnteredValue": t.string().optional(),
        }
    ).named(renames["ConditionValueIn"])
    types["ConditionValueOut"] = t.struct(
        {
            "relativeDate": t.string().optional(),
            "userEnteredValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionValueOut"])
    types["DataSourceRefreshScheduleIn"] = t.struct(
        {
            "refreshScope": t.string().optional(),
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleIn"]
            ).optional(),
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleIn"]
            ).optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleIn"]
            ).optional(),
            "enabled": t.boolean().optional(),
        }
    ).named(renames["DataSourceRefreshScheduleIn"])
    types["DataSourceRefreshScheduleOut"] = t.struct(
        {
            "refreshScope": t.string().optional(),
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleOut"]
            ).optional(),
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleOut"]
            ).optional(),
            "nextRun": t.proxy(renames["IntervalOut"]).optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleOut"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshScheduleOut"])
    types["UpdateValuesResponseIn"] = t.struct(
        {
            "updatedRows": t.integer().optional(),
            "updatedColumns": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
            "updatedCells": t.integer().optional(),
            "updatedRange": t.string().optional(),
        }
    ).named(renames["UpdateValuesResponseIn"])
    types["UpdateValuesResponseOut"] = t.struct(
        {
            "updatedRows": t.integer().optional(),
            "updatedColumns": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "updatedCells": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesResponseOut"])
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
    types["ManualRuleIn"] = t.struct(
        {"groups": t.array(t.proxy(renames["ManualRuleGroupIn"])).optional()}
    ).named(renames["ManualRuleIn"])
    types["ManualRuleOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["ManualRuleGroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualRuleOut"])
    types["DeleteDimensionRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionRequestIn"])
    types["DeleteDimensionRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionRequestOut"])
    types["SpreadsheetPropertiesIn"] = t.struct(
        {
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeIn"]).optional(),
            "locale": t.string().optional(),
            "autoRecalc": t.string().optional(),
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsIn"]
            ).optional(),
            "timeZone": t.string().optional(),
            "defaultFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["SpreadsheetPropertiesIn"])
    types["SpreadsheetPropertiesOut"] = t.struct(
        {
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeOut"]).optional(),
            "locale": t.string().optional(),
            "autoRecalc": t.string().optional(),
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "defaultFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetPropertiesOut"])
    types["BasicChartAxisIn"] = t.struct(
        {
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "title": t.string().optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsIn"]
            ).optional(),
            "position": t.string().optional(),
            "format": t.proxy(renames["TextFormatIn"]).optional(),
        }
    ).named(renames["BasicChartAxisIn"])
    types["BasicChartAxisOut"] = t.struct(
        {
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "title": t.string().optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsOut"]
            ).optional(),
            "position": t.string().optional(),
            "format": t.proxy(renames["TextFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartAxisOut"])
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
    types["AppendCellsRequestIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "sheetId": t.integer().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["AppendCellsRequestIn"])
    types["AppendCellsRequestOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "sheetId": t.integer().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendCellsRequestOut"])
    types["PivotFilterSpecIn"] = t.struct(
        {
            "columnOffsetIndex": t.integer().optional(),
            "filterCriteria": t.proxy(renames["PivotFilterCriteriaIn"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
        }
    ).named(renames["PivotFilterSpecIn"])
    types["PivotFilterSpecOut"] = t.struct(
        {
            "columnOffsetIndex": t.integer().optional(),
            "filterCriteria": t.proxy(renames["PivotFilterCriteriaOut"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotFilterSpecOut"])
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
    types["AppendValuesResponseIn"] = t.struct(
        {
            "tableRange": t.string().optional(),
            "updates": t.proxy(renames["UpdateValuesResponseIn"]).optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["AppendValuesResponseIn"])
    types["AppendValuesResponseOut"] = t.struct(
        {
            "tableRange": t.string().optional(),
            "updates": t.proxy(renames["UpdateValuesResponseOut"]).optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendValuesResponseOut"])
    types["ThemeColorPairIn"] = t.struct(
        {
            "colorType": t.string().optional(),
            "color": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["ThemeColorPairIn"])
    types["ThemeColorPairOut"] = t.struct(
        {
            "colorType": t.string().optional(),
            "color": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThemeColorPairOut"])
    types["TextToColumnsRequestIn"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "delimiter": t.string().optional(),
            "delimiterType": t.string().optional(),
        }
    ).named(renames["TextToColumnsRequestIn"])
    types["TextToColumnsRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "delimiter": t.string().optional(),
            "delimiterType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextToColumnsRequestOut"])

    functions = {}
    functions["spreadsheetsBatchUpdate"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}",
        t.struct(
            {
                "ranges": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "spreadsheetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsGetByDataFilter"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}",
        t.struct(
            {
                "ranges": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "spreadsheetId": t.string().optional(),
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
                "includeGridData": t.boolean().optional(),
                "spreadsheetId": t.string().optional(),
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
                "includeGridData": t.boolean().optional(),
                "spreadsheetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesUpdate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesAppend"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchUpdate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchGetByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchClear"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchClearByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchUpdateByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesClear"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values/{range}:clear",
        t.struct(
            {
                "range": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClearValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsSheetsCopyTo"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/sheets/{sheetId}:copyTo",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "sheetId": t.integer().optional(),
                "destinationSpreadsheetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SheetPropertiesOut"]),
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

    return Import(importer="sheets", renames=renames, types=types, functions=functions)
