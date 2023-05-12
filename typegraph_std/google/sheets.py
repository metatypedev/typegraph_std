from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_sheets() -> Import:
    sheets = HTTPRuntime("https://sheets.googleapis.com/")

    renames = {
        "ErrorResponse": "_sheets_1_ErrorResponse",
        "PivotGroupValueMetadataIn": "_sheets_2_PivotGroupValueMetadataIn",
        "PivotGroupValueMetadataOut": "_sheets_3_PivotGroupValueMetadataOut",
        "AddSheetRequestIn": "_sheets_4_AddSheetRequestIn",
        "AddSheetRequestOut": "_sheets_5_AddSheetRequestOut",
        "ScorecardChartSpecIn": "_sheets_6_ScorecardChartSpecIn",
        "ScorecardChartSpecOut": "_sheets_7_ScorecardChartSpecOut",
        "UpdateConditionalFormatRuleResponseIn": "_sheets_8_UpdateConditionalFormatRuleResponseIn",
        "UpdateConditionalFormatRuleResponseOut": "_sheets_9_UpdateConditionalFormatRuleResponseOut",
        "OrgChartSpecIn": "_sheets_10_OrgChartSpecIn",
        "OrgChartSpecOut": "_sheets_11_OrgChartSpecOut",
        "DataSourceColumnReferenceIn": "_sheets_12_DataSourceColumnReferenceIn",
        "DataSourceColumnReferenceOut": "_sheets_13_DataSourceColumnReferenceOut",
        "KeyValueFormatIn": "_sheets_14_KeyValueFormatIn",
        "KeyValueFormatOut": "_sheets_15_KeyValueFormatOut",
        "AddConditionalFormatRuleRequestIn": "_sheets_16_AddConditionalFormatRuleRequestIn",
        "AddConditionalFormatRuleRequestOut": "_sheets_17_AddConditionalFormatRuleRequestOut",
        "AddNamedRangeRequestIn": "_sheets_18_AddNamedRangeRequestIn",
        "AddNamedRangeRequestOut": "_sheets_19_AddNamedRangeRequestOut",
        "DataSourceRefreshWeeklyScheduleIn": "_sheets_20_DataSourceRefreshWeeklyScheduleIn",
        "DataSourceRefreshWeeklyScheduleOut": "_sheets_21_DataSourceRefreshWeeklyScheduleOut",
        "CandlestickDataIn": "_sheets_22_CandlestickDataIn",
        "CandlestickDataOut": "_sheets_23_CandlestickDataOut",
        "AddBandingRequestIn": "_sheets_24_AddBandingRequestIn",
        "AddBandingRequestOut": "_sheets_25_AddBandingRequestOut",
        "AppendValuesResponseIn": "_sheets_26_AppendValuesResponseIn",
        "AppendValuesResponseOut": "_sheets_27_AppendValuesResponseOut",
        "GradientRuleIn": "_sheets_28_GradientRuleIn",
        "GradientRuleOut": "_sheets_29_GradientRuleOut",
        "EditorsIn": "_sheets_30_EditorsIn",
        "EditorsOut": "_sheets_31_EditorsOut",
        "DuplicateFilterViewRequestIn": "_sheets_32_DuplicateFilterViewRequestIn",
        "DuplicateFilterViewRequestOut": "_sheets_33_DuplicateFilterViewRequestOut",
        "TextFormatRunIn": "_sheets_34_TextFormatRunIn",
        "TextFormatRunOut": "_sheets_35_TextFormatRunOut",
        "DataSourceObjectReferencesIn": "_sheets_36_DataSourceObjectReferencesIn",
        "DataSourceObjectReferencesOut": "_sheets_37_DataSourceObjectReferencesOut",
        "TextFormatIn": "_sheets_38_TextFormatIn",
        "TextFormatOut": "_sheets_39_TextFormatOut",
        "SpreadsheetIn": "_sheets_40_SpreadsheetIn",
        "SpreadsheetOut": "_sheets_41_SpreadsheetOut",
        "SortRangeRequestIn": "_sheets_42_SortRangeRequestIn",
        "SortRangeRequestOut": "_sheets_43_SortRangeRequestOut",
        "ProtectedRangeIn": "_sheets_44_ProtectedRangeIn",
        "ProtectedRangeOut": "_sheets_45_ProtectedRangeOut",
        "DeleteSheetRequestIn": "_sheets_46_DeleteSheetRequestIn",
        "DeleteSheetRequestOut": "_sheets_47_DeleteSheetRequestOut",
        "SheetIn": "_sheets_48_SheetIn",
        "SheetOut": "_sheets_49_SheetOut",
        "RandomizeRangeRequestIn": "_sheets_50_RandomizeRangeRequestIn",
        "RandomizeRangeRequestOut": "_sheets_51_RandomizeRangeRequestOut",
        "MatchedDeveloperMetadataIn": "_sheets_52_MatchedDeveloperMetadataIn",
        "MatchedDeveloperMetadataOut": "_sheets_53_MatchedDeveloperMetadataOut",
        "ResponseIn": "_sheets_54_ResponseIn",
        "ResponseOut": "_sheets_55_ResponseOut",
        "DataLabelIn": "_sheets_56_DataLabelIn",
        "DataLabelOut": "_sheets_57_DataLabelOut",
        "TreemapChartSpecIn": "_sheets_58_TreemapChartSpecIn",
        "TreemapChartSpecOut": "_sheets_59_TreemapChartSpecOut",
        "DataSourceRefreshDailyScheduleIn": "_sheets_60_DataSourceRefreshDailyScheduleIn",
        "DataSourceRefreshDailyScheduleOut": "_sheets_61_DataSourceRefreshDailyScheduleOut",
        "AddChartResponseIn": "_sheets_62_AddChartResponseIn",
        "AddChartResponseOut": "_sheets_63_AddChartResponseOut",
        "PasteDataRequestIn": "_sheets_64_PasteDataRequestIn",
        "PasteDataRequestOut": "_sheets_65_PasteDataRequestOut",
        "BatchUpdateValuesRequestIn": "_sheets_66_BatchUpdateValuesRequestIn",
        "BatchUpdateValuesRequestOut": "_sheets_67_BatchUpdateValuesRequestOut",
        "DuplicateSheetRequestIn": "_sheets_68_DuplicateSheetRequestIn",
        "DuplicateSheetRequestOut": "_sheets_69_DuplicateSheetRequestOut",
        "BigQueryTableSpecIn": "_sheets_70_BigQueryTableSpecIn",
        "BigQueryTableSpecOut": "_sheets_71_BigQueryTableSpecOut",
        "GridRangeIn": "_sheets_72_GridRangeIn",
        "GridRangeOut": "_sheets_73_GridRangeOut",
        "HistogramRuleIn": "_sheets_74_HistogramRuleIn",
        "HistogramRuleOut": "_sheets_75_HistogramRuleOut",
        "DataSourceObjectReferenceIn": "_sheets_76_DataSourceObjectReferenceIn",
        "DataSourceObjectReferenceOut": "_sheets_77_DataSourceObjectReferenceOut",
        "CopyPasteRequestIn": "_sheets_78_CopyPasteRequestIn",
        "CopyPasteRequestOut": "_sheets_79_CopyPasteRequestOut",
        "DataFilterIn": "_sheets_80_DataFilterIn",
        "DataFilterOut": "_sheets_81_DataFilterOut",
        "CopySheetToAnotherSpreadsheetRequestIn": "_sheets_82_CopySheetToAnotherSpreadsheetRequestIn",
        "CopySheetToAnotherSpreadsheetRequestOut": "_sheets_83_CopySheetToAnotherSpreadsheetRequestOut",
        "IterativeCalculationSettingsIn": "_sheets_84_IterativeCalculationSettingsIn",
        "IterativeCalculationSettingsOut": "_sheets_85_IterativeCalculationSettingsOut",
        "DataSourceChartPropertiesIn": "_sheets_86_DataSourceChartPropertiesIn",
        "DataSourceChartPropertiesOut": "_sheets_87_DataSourceChartPropertiesOut",
        "DataSourceParameterIn": "_sheets_88_DataSourceParameterIn",
        "DataSourceParameterOut": "_sheets_89_DataSourceParameterOut",
        "DataExecutionStatusIn": "_sheets_90_DataExecutionStatusIn",
        "DataExecutionStatusOut": "_sheets_91_DataExecutionStatusOut",
        "DuplicateFilterViewResponseIn": "_sheets_92_DuplicateFilterViewResponseIn",
        "DuplicateFilterViewResponseOut": "_sheets_93_DuplicateFilterViewResponseOut",
        "OverlayPositionIn": "_sheets_94_OverlayPositionIn",
        "OverlayPositionOut": "_sheets_95_OverlayPositionOut",
        "FilterSpecIn": "_sheets_96_FilterSpecIn",
        "FilterSpecOut": "_sheets_97_FilterSpecOut",
        "RefreshDataSourceResponseIn": "_sheets_98_RefreshDataSourceResponseIn",
        "RefreshDataSourceResponseOut": "_sheets_99_RefreshDataSourceResponseOut",
        "AddDataSourceResponseIn": "_sheets_100_AddDataSourceResponseIn",
        "AddDataSourceResponseOut": "_sheets_101_AddDataSourceResponseOut",
        "DeveloperMetadataIn": "_sheets_102_DeveloperMetadataIn",
        "DeveloperMetadataOut": "_sheets_103_DeveloperMetadataOut",
        "BatchGetValuesByDataFilterRequestIn": "_sheets_104_BatchGetValuesByDataFilterRequestIn",
        "BatchGetValuesByDataFilterRequestOut": "_sheets_105_BatchGetValuesByDataFilterRequestOut",
        "BasicSeriesDataPointStyleOverrideIn": "_sheets_106_BasicSeriesDataPointStyleOverrideIn",
        "BasicSeriesDataPointStyleOverrideOut": "_sheets_107_BasicSeriesDataPointStyleOverrideOut",
        "WaterfallChartColumnStyleIn": "_sheets_108_WaterfallChartColumnStyleIn",
        "WaterfallChartColumnStyleOut": "_sheets_109_WaterfallChartColumnStyleOut",
        "GridDataIn": "_sheets_110_GridDataIn",
        "GridDataOut": "_sheets_111_GridDataOut",
        "NumberFormatIn": "_sheets_112_NumberFormatIn",
        "NumberFormatOut": "_sheets_113_NumberFormatOut",
        "ChartDateTimeRuleIn": "_sheets_114_ChartDateTimeRuleIn",
        "ChartDateTimeRuleOut": "_sheets_115_ChartDateTimeRuleOut",
        "TextPositionIn": "_sheets_116_TextPositionIn",
        "TextPositionOut": "_sheets_117_TextPositionOut",
        "HistogramSeriesIn": "_sheets_118_HistogramSeriesIn",
        "HistogramSeriesOut": "_sheets_119_HistogramSeriesOut",
        "ClearBasicFilterRequestIn": "_sheets_120_ClearBasicFilterRequestIn",
        "ClearBasicFilterRequestOut": "_sheets_121_ClearBasicFilterRequestOut",
        "RefreshDataSourceRequestIn": "_sheets_122_RefreshDataSourceRequestIn",
        "RefreshDataSourceRequestOut": "_sheets_123_RefreshDataSourceRequestOut",
        "DeleteDimensionRequestIn": "_sheets_124_DeleteDimensionRequestIn",
        "DeleteDimensionRequestOut": "_sheets_125_DeleteDimensionRequestOut",
        "AutoFillRequestIn": "_sheets_126_AutoFillRequestIn",
        "AutoFillRequestOut": "_sheets_127_AutoFillRequestOut",
        "ErrorValueIn": "_sheets_128_ErrorValueIn",
        "ErrorValueOut": "_sheets_129_ErrorValueOut",
        "UpdateDimensionPropertiesRequestIn": "_sheets_130_UpdateDimensionPropertiesRequestIn",
        "UpdateDimensionPropertiesRequestOut": "_sheets_131_UpdateDimensionPropertiesRequestOut",
        "AddProtectedRangeRequestIn": "_sheets_132_AddProtectedRangeRequestIn",
        "AddProtectedRangeRequestOut": "_sheets_133_AddProtectedRangeRequestOut",
        "BandingPropertiesIn": "_sheets_134_BandingPropertiesIn",
        "BandingPropertiesOut": "_sheets_135_BandingPropertiesOut",
        "AddProtectedRangeResponseIn": "_sheets_136_AddProtectedRangeResponseIn",
        "AddProtectedRangeResponseOut": "_sheets_137_AddProtectedRangeResponseOut",
        "BasicFilterIn": "_sheets_138_BasicFilterIn",
        "BasicFilterOut": "_sheets_139_BasicFilterOut",
        "DeleteBandingRequestIn": "_sheets_140_DeleteBandingRequestIn",
        "DeleteBandingRequestOut": "_sheets_141_DeleteBandingRequestOut",
        "PivotFilterCriteriaIn": "_sheets_142_PivotFilterCriteriaIn",
        "PivotFilterCriteriaOut": "_sheets_143_PivotFilterCriteriaOut",
        "DimensionRangeIn": "_sheets_144_DimensionRangeIn",
        "DimensionRangeOut": "_sheets_145_DimensionRangeOut",
        "PivotGroupLimitIn": "_sheets_146_PivotGroupLimitIn",
        "PivotGroupLimitOut": "_sheets_147_PivotGroupLimitOut",
        "ManualRuleGroupIn": "_sheets_148_ManualRuleGroupIn",
        "ManualRuleGroupOut": "_sheets_149_ManualRuleGroupOut",
        "DuplicateSheetResponseIn": "_sheets_150_DuplicateSheetResponseIn",
        "DuplicateSheetResponseOut": "_sheets_151_DuplicateSheetResponseOut",
        "CandlestickChartSpecIn": "_sheets_152_CandlestickChartSpecIn",
        "CandlestickChartSpecOut": "_sheets_153_CandlestickChartSpecOut",
        "ColorStyleIn": "_sheets_154_ColorStyleIn",
        "ColorStyleOut": "_sheets_155_ColorStyleOut",
        "UpdateDeveloperMetadataRequestIn": "_sheets_156_UpdateDeveloperMetadataRequestIn",
        "UpdateDeveloperMetadataRequestOut": "_sheets_157_UpdateDeveloperMetadataRequestOut",
        "ChartAxisViewWindowOptionsIn": "_sheets_158_ChartAxisViewWindowOptionsIn",
        "ChartAxisViewWindowOptionsOut": "_sheets_159_ChartAxisViewWindowOptionsOut",
        "BasicChartSpecIn": "_sheets_160_BasicChartSpecIn",
        "BasicChartSpecOut": "_sheets_161_BasicChartSpecOut",
        "PivotValueIn": "_sheets_162_PivotValueIn",
        "PivotValueOut": "_sheets_163_PivotValueOut",
        "FindReplaceResponseIn": "_sheets_164_FindReplaceResponseIn",
        "FindReplaceResponseOut": "_sheets_165_FindReplaceResponseOut",
        "UpdateSheetPropertiesRequestIn": "_sheets_166_UpdateSheetPropertiesRequestIn",
        "UpdateSheetPropertiesRequestOut": "_sheets_167_UpdateSheetPropertiesRequestOut",
        "LineStyleIn": "_sheets_168_LineStyleIn",
        "LineStyleOut": "_sheets_169_LineStyleOut",
        "PointStyleIn": "_sheets_170_PointStyleIn",
        "PointStyleOut": "_sheets_171_PointStyleOut",
        "DataSourceSheetPropertiesIn": "_sheets_172_DataSourceSheetPropertiesIn",
        "DataSourceSheetPropertiesOut": "_sheets_173_DataSourceSheetPropertiesOut",
        "SlicerSpecIn": "_sheets_174_SlicerSpecIn",
        "SlicerSpecOut": "_sheets_175_SlicerSpecOut",
        "AddNamedRangeResponseIn": "_sheets_176_AddNamedRangeResponseIn",
        "AddNamedRangeResponseOut": "_sheets_177_AddNamedRangeResponseOut",
        "BubbleChartSpecIn": "_sheets_178_BubbleChartSpecIn",
        "BubbleChartSpecOut": "_sheets_179_BubbleChartSpecOut",
        "SetDataValidationRequestIn": "_sheets_180_SetDataValidationRequestIn",
        "SetDataValidationRequestOut": "_sheets_181_SetDataValidationRequestOut",
        "DeleteDuplicatesRequestIn": "_sheets_182_DeleteDuplicatesRequestIn",
        "DeleteDuplicatesRequestOut": "_sheets_183_DeleteDuplicatesRequestOut",
        "DeleteDeveloperMetadataRequestIn": "_sheets_184_DeleteDeveloperMetadataRequestIn",
        "DeleteDeveloperMetadataRequestOut": "_sheets_185_DeleteDeveloperMetadataRequestOut",
        "AddSlicerResponseIn": "_sheets_186_AddSlicerResponseIn",
        "AddSlicerResponseOut": "_sheets_187_AddSlicerResponseOut",
        "UpdateEmbeddedObjectBorderRequestIn": "_sheets_188_UpdateEmbeddedObjectBorderRequestIn",
        "UpdateEmbeddedObjectBorderRequestOut": "_sheets_189_UpdateEmbeddedObjectBorderRequestOut",
        "UpdateValuesResponseIn": "_sheets_190_UpdateValuesResponseIn",
        "UpdateValuesResponseOut": "_sheets_191_UpdateValuesResponseOut",
        "UpdateDataSourceResponseIn": "_sheets_192_UpdateDataSourceResponseIn",
        "UpdateDataSourceResponseOut": "_sheets_193_UpdateDataSourceResponseOut",
        "UpdateSlicerSpecRequestIn": "_sheets_194_UpdateSlicerSpecRequestIn",
        "UpdateSlicerSpecRequestOut": "_sheets_195_UpdateSlicerSpecRequestOut",
        "SetBasicFilterRequestIn": "_sheets_196_SetBasicFilterRequestIn",
        "SetBasicFilterRequestOut": "_sheets_197_SetBasicFilterRequestOut",
        "AddDimensionGroupRequestIn": "_sheets_198_AddDimensionGroupRequestIn",
        "AddDimensionGroupRequestOut": "_sheets_199_AddDimensionGroupRequestOut",
        "MergeCellsRequestIn": "_sheets_200_MergeCellsRequestIn",
        "MergeCellsRequestOut": "_sheets_201_MergeCellsRequestOut",
        "UpdateConditionalFormatRuleRequestIn": "_sheets_202_UpdateConditionalFormatRuleRequestIn",
        "UpdateConditionalFormatRuleRequestOut": "_sheets_203_UpdateConditionalFormatRuleRequestOut",
        "ManualRuleIn": "_sheets_204_ManualRuleIn",
        "ManualRuleOut": "_sheets_205_ManualRuleOut",
        "DataSourceIn": "_sheets_206_DataSourceIn",
        "DataSourceOut": "_sheets_207_DataSourceOut",
        "CandlestickSeriesIn": "_sheets_208_CandlestickSeriesIn",
        "CandlestickSeriesOut": "_sheets_209_CandlestickSeriesOut",
        "AddChartRequestIn": "_sheets_210_AddChartRequestIn",
        "AddChartRequestOut": "_sheets_211_AddChartRequestOut",
        "DataSourceColumnIn": "_sheets_212_DataSourceColumnIn",
        "DataSourceColumnOut": "_sheets_213_DataSourceColumnOut",
        "UnmergeCellsRequestIn": "_sheets_214_UnmergeCellsRequestIn",
        "UnmergeCellsRequestOut": "_sheets_215_UnmergeCellsRequestOut",
        "TimeOfDayIn": "_sheets_216_TimeOfDayIn",
        "TimeOfDayOut": "_sheets_217_TimeOfDayOut",
        "BorderIn": "_sheets_218_BorderIn",
        "BorderOut": "_sheets_219_BorderOut",
        "InsertDimensionRequestIn": "_sheets_220_InsertDimensionRequestIn",
        "InsertDimensionRequestOut": "_sheets_221_InsertDimensionRequestOut",
        "SortSpecIn": "_sheets_222_SortSpecIn",
        "SortSpecOut": "_sheets_223_SortSpecOut",
        "ClearValuesRequestIn": "_sheets_224_ClearValuesRequestIn",
        "ClearValuesRequestOut": "_sheets_225_ClearValuesRequestOut",
        "BatchUpdateValuesByDataFilterResponseIn": "_sheets_226_BatchUpdateValuesByDataFilterResponseIn",
        "BatchUpdateValuesByDataFilterResponseOut": "_sheets_227_BatchUpdateValuesByDataFilterResponseOut",
        "ExtendedValueIn": "_sheets_228_ExtendedValueIn",
        "ExtendedValueOut": "_sheets_229_ExtendedValueOut",
        "BatchUpdateValuesResponseIn": "_sheets_230_BatchUpdateValuesResponseIn",
        "BatchUpdateValuesResponseOut": "_sheets_231_BatchUpdateValuesResponseOut",
        "DataSourceFormulaIn": "_sheets_232_DataSourceFormulaIn",
        "DataSourceFormulaOut": "_sheets_233_DataSourceFormulaOut",
        "BatchClearValuesByDataFilterResponseIn": "_sheets_234_BatchClearValuesByDataFilterResponseIn",
        "BatchClearValuesByDataFilterResponseOut": "_sheets_235_BatchClearValuesByDataFilterResponseOut",
        "BasicChartDomainIn": "_sheets_236_BasicChartDomainIn",
        "BasicChartDomainOut": "_sheets_237_BasicChartDomainOut",
        "ChartSourceRangeIn": "_sheets_238_ChartSourceRangeIn",
        "ChartSourceRangeOut": "_sheets_239_ChartSourceRangeOut",
        "FindReplaceRequestIn": "_sheets_240_FindReplaceRequestIn",
        "FindReplaceRequestOut": "_sheets_241_FindReplaceRequestOut",
        "ConditionValueIn": "_sheets_242_ConditionValueIn",
        "ConditionValueOut": "_sheets_243_ConditionValueOut",
        "DeleteDeveloperMetadataResponseIn": "_sheets_244_DeleteDeveloperMetadataResponseIn",
        "DeleteDeveloperMetadataResponseOut": "_sheets_245_DeleteDeveloperMetadataResponseOut",
        "CellFormatIn": "_sheets_246_CellFormatIn",
        "CellFormatOut": "_sheets_247_CellFormatOut",
        "FilterViewIn": "_sheets_248_FilterViewIn",
        "FilterViewOut": "_sheets_249_FilterViewOut",
        "PivotFilterSpecIn": "_sheets_250_PivotFilterSpecIn",
        "PivotFilterSpecOut": "_sheets_251_PivotFilterSpecOut",
        "LinkIn": "_sheets_252_LinkIn",
        "LinkOut": "_sheets_253_LinkOut",
        "ColorIn": "_sheets_254_ColorIn",
        "ColorOut": "_sheets_255_ColorOut",
        "AddSlicerRequestIn": "_sheets_256_AddSlicerRequestIn",
        "AddSlicerRequestOut": "_sheets_257_AddSlicerRequestOut",
        "AutoResizeDimensionsRequestIn": "_sheets_258_AutoResizeDimensionsRequestIn",
        "AutoResizeDimensionsRequestOut": "_sheets_259_AutoResizeDimensionsRequestOut",
        "GetSpreadsheetByDataFilterRequestIn": "_sheets_260_GetSpreadsheetByDataFilterRequestIn",
        "GetSpreadsheetByDataFilterRequestOut": "_sheets_261_GetSpreadsheetByDataFilterRequestOut",
        "AddFilterViewResponseIn": "_sheets_262_AddFilterViewResponseIn",
        "AddFilterViewResponseOut": "_sheets_263_AddFilterViewResponseOut",
        "UpdateValuesByDataFilterResponseIn": "_sheets_264_UpdateValuesByDataFilterResponseIn",
        "UpdateValuesByDataFilterResponseOut": "_sheets_265_UpdateValuesByDataFilterResponseOut",
        "AddSheetResponseIn": "_sheets_266_AddSheetResponseIn",
        "AddSheetResponseOut": "_sheets_267_AddSheetResponseOut",
        "EmbeddedChartIn": "_sheets_268_EmbeddedChartIn",
        "EmbeddedChartOut": "_sheets_269_EmbeddedChartOut",
        "BooleanRuleIn": "_sheets_270_BooleanRuleIn",
        "BooleanRuleOut": "_sheets_271_BooleanRuleOut",
        "SpreadsheetPropertiesIn": "_sheets_272_SpreadsheetPropertiesIn",
        "SpreadsheetPropertiesOut": "_sheets_273_SpreadsheetPropertiesOut",
        "BasicChartSeriesIn": "_sheets_274_BasicChartSeriesIn",
        "BasicChartSeriesOut": "_sheets_275_BasicChartSeriesOut",
        "UpdateEmbeddedObjectPositionRequestIn": "_sheets_276_UpdateEmbeddedObjectPositionRequestIn",
        "UpdateEmbeddedObjectPositionRequestOut": "_sheets_277_UpdateEmbeddedObjectPositionRequestOut",
        "DimensionPropertiesIn": "_sheets_278_DimensionPropertiesIn",
        "DimensionPropertiesOut": "_sheets_279_DimensionPropertiesOut",
        "BatchClearValuesByDataFilterRequestIn": "_sheets_280_BatchClearValuesByDataFilterRequestIn",
        "BatchClearValuesByDataFilterRequestOut": "_sheets_281_BatchClearValuesByDataFilterRequestOut",
        "AppendCellsRequestIn": "_sheets_282_AppendCellsRequestIn",
        "AppendCellsRequestOut": "_sheets_283_AppendCellsRequestOut",
        "ChartSpecIn": "_sheets_284_ChartSpecIn",
        "ChartSpecOut": "_sheets_285_ChartSpecOut",
        "UpdateFilterViewRequestIn": "_sheets_286_UpdateFilterViewRequestIn",
        "UpdateFilterViewRequestOut": "_sheets_287_UpdateFilterViewRequestOut",
        "HistogramChartSpecIn": "_sheets_288_HistogramChartSpecIn",
        "HistogramChartSpecOut": "_sheets_289_HistogramChartSpecOut",
        "DeveloperMetadataLookupIn": "_sheets_290_DeveloperMetadataLookupIn",
        "DeveloperMetadataLookupOut": "_sheets_291_DeveloperMetadataLookupOut",
        "RequestIn": "_sheets_292_RequestIn",
        "RequestOut": "_sheets_293_RequestOut",
        "SourceAndDestinationIn": "_sheets_294_SourceAndDestinationIn",
        "SourceAndDestinationOut": "_sheets_295_SourceAndDestinationOut",
        "ChartGroupRuleIn": "_sheets_296_ChartGroupRuleIn",
        "ChartGroupRuleOut": "_sheets_297_ChartGroupRuleOut",
        "DataSourceSpecIn": "_sheets_298_DataSourceSpecIn",
        "DataSourceSpecOut": "_sheets_299_DataSourceSpecOut",
        "FilterCriteriaIn": "_sheets_300_FilterCriteriaIn",
        "FilterCriteriaOut": "_sheets_301_FilterCriteriaOut",
        "BatchGetValuesByDataFilterResponseIn": "_sheets_302_BatchGetValuesByDataFilterResponseIn",
        "BatchGetValuesByDataFilterResponseOut": "_sheets_303_BatchGetValuesByDataFilterResponseOut",
        "CutPasteRequestIn": "_sheets_304_CutPasteRequestIn",
        "CutPasteRequestOut": "_sheets_305_CutPasteRequestOut",
        "BordersIn": "_sheets_306_BordersIn",
        "BordersOut": "_sheets_307_BordersOut",
        "BaselineValueFormatIn": "_sheets_308_BaselineValueFormatIn",
        "BaselineValueFormatOut": "_sheets_309_BaselineValueFormatOut",
        "PivotGroupIn": "_sheets_310_PivotGroupIn",
        "PivotGroupOut": "_sheets_311_PivotGroupOut",
        "BatchClearValuesRequestIn": "_sheets_312_BatchClearValuesRequestIn",
        "BatchClearValuesRequestOut": "_sheets_313_BatchClearValuesRequestOut",
        "DeleteConditionalFormatRuleResponseIn": "_sheets_314_DeleteConditionalFormatRuleResponseIn",
        "DeleteConditionalFormatRuleResponseOut": "_sheets_315_DeleteConditionalFormatRuleResponseOut",
        "AppendDimensionRequestIn": "_sheets_316_AppendDimensionRequestIn",
        "AppendDimensionRequestOut": "_sheets_317_AppendDimensionRequestOut",
        "AddFilterViewRequestIn": "_sheets_318_AddFilterViewRequestIn",
        "AddFilterViewRequestOut": "_sheets_319_AddFilterViewRequestOut",
        "TreemapChartColorScaleIn": "_sheets_320_TreemapChartColorScaleIn",
        "TreemapChartColorScaleOut": "_sheets_321_TreemapChartColorScaleOut",
        "SpreadsheetThemeIn": "_sheets_322_SpreadsheetThemeIn",
        "SpreadsheetThemeOut": "_sheets_323_SpreadsheetThemeOut",
        "MatchedValueRangeIn": "_sheets_324_MatchedValueRangeIn",
        "MatchedValueRangeOut": "_sheets_325_MatchedValueRangeOut",
        "MoveDimensionRequestIn": "_sheets_326_MoveDimensionRequestIn",
        "MoveDimensionRequestOut": "_sheets_327_MoveDimensionRequestOut",
        "BatchUpdateSpreadsheetResponseIn": "_sheets_328_BatchUpdateSpreadsheetResponseIn",
        "BatchUpdateSpreadsheetResponseOut": "_sheets_329_BatchUpdateSpreadsheetResponseOut",
        "ThemeColorPairIn": "_sheets_330_ThemeColorPairIn",
        "ThemeColorPairOut": "_sheets_331_ThemeColorPairOut",
        "DeleteEmbeddedObjectRequestIn": "_sheets_332_DeleteEmbeddedObjectRequestIn",
        "DeleteEmbeddedObjectRequestOut": "_sheets_333_DeleteEmbeddedObjectRequestOut",
        "BandedRangeIn": "_sheets_334_BandedRangeIn",
        "BandedRangeOut": "_sheets_335_BandedRangeOut",
        "UpdateBordersRequestIn": "_sheets_336_UpdateBordersRequestIn",
        "UpdateBordersRequestOut": "_sheets_337_UpdateBordersRequestOut",
        "PivotTableIn": "_sheets_338_PivotTableIn",
        "PivotTableOut": "_sheets_339_PivotTableOut",
        "UpdateChartSpecRequestIn": "_sheets_340_UpdateChartSpecRequestIn",
        "UpdateChartSpecRequestOut": "_sheets_341_UpdateChartSpecRequestOut",
        "RefreshDataSourceObjectExecutionStatusIn": "_sheets_342_RefreshDataSourceObjectExecutionStatusIn",
        "RefreshDataSourceObjectExecutionStatusOut": "_sheets_343_RefreshDataSourceObjectExecutionStatusOut",
        "BooleanConditionIn": "_sheets_344_BooleanConditionIn",
        "BooleanConditionOut": "_sheets_345_BooleanConditionOut",
        "DataSourceTableIn": "_sheets_346_DataSourceTableIn",
        "DataSourceTableOut": "_sheets_347_DataSourceTableOut",
        "DeleteDataSourceRequestIn": "_sheets_348_DeleteDataSourceRequestIn",
        "DeleteDataSourceRequestOut": "_sheets_349_DeleteDataSourceRequestOut",
        "ChartDataIn": "_sheets_350_ChartDataIn",
        "ChartDataOut": "_sheets_351_ChartDataOut",
        "SlicerIn": "_sheets_352_SlicerIn",
        "SlicerOut": "_sheets_353_SlicerOut",
        "TextRotationIn": "_sheets_354_TextRotationIn",
        "TextRotationOut": "_sheets_355_TextRotationOut",
        "InsertRangeRequestIn": "_sheets_356_InsertRangeRequestIn",
        "InsertRangeRequestOut": "_sheets_357_InsertRangeRequestOut",
        "RepeatCellRequestIn": "_sheets_358_RepeatCellRequestIn",
        "RepeatCellRequestOut": "_sheets_359_RepeatCellRequestOut",
        "DeveloperMetadataLocationIn": "_sheets_360_DeveloperMetadataLocationIn",
        "DeveloperMetadataLocationOut": "_sheets_361_DeveloperMetadataLocationOut",
        "DeleteFilterViewRequestIn": "_sheets_362_DeleteFilterViewRequestIn",
        "DeleteFilterViewRequestOut": "_sheets_363_DeleteFilterViewRequestOut",
        "DeleteDimensionGroupResponseIn": "_sheets_364_DeleteDimensionGroupResponseIn",
        "DeleteDimensionGroupResponseOut": "_sheets_365_DeleteDimensionGroupResponseOut",
        "WaterfallChartSpecIn": "_sheets_366_WaterfallChartSpecIn",
        "WaterfallChartSpecOut": "_sheets_367_WaterfallChartSpecOut",
        "TrimWhitespaceRequestIn": "_sheets_368_TrimWhitespaceRequestIn",
        "TrimWhitespaceRequestOut": "_sheets_369_TrimWhitespaceRequestOut",
        "UpdateProtectedRangeRequestIn": "_sheets_370_UpdateProtectedRangeRequestIn",
        "UpdateProtectedRangeRequestOut": "_sheets_371_UpdateProtectedRangeRequestOut",
        "IntervalIn": "_sheets_372_IntervalIn",
        "IntervalOut": "_sheets_373_IntervalOut",
        "DimensionGroupIn": "_sheets_374_DimensionGroupIn",
        "DimensionGroupOut": "_sheets_375_DimensionGroupOut",
        "DataSourceSheetDimensionRangeIn": "_sheets_376_DataSourceSheetDimensionRangeIn",
        "DataSourceSheetDimensionRangeOut": "_sheets_377_DataSourceSheetDimensionRangeOut",
        "UpdateDimensionGroupRequestIn": "_sheets_378_UpdateDimensionGroupRequestIn",
        "UpdateDimensionGroupRequestOut": "_sheets_379_UpdateDimensionGroupRequestOut",
        "ChartHistogramRuleIn": "_sheets_380_ChartHistogramRuleIn",
        "ChartHistogramRuleOut": "_sheets_381_ChartHistogramRuleOut",
        "WaterfallChartDomainIn": "_sheets_382_WaterfallChartDomainIn",
        "WaterfallChartDomainOut": "_sheets_383_WaterfallChartDomainOut",
        "GridPropertiesIn": "_sheets_384_GridPropertiesIn",
        "GridPropertiesOut": "_sheets_385_GridPropertiesOut",
        "BatchUpdateValuesByDataFilterRequestIn": "_sheets_386_BatchUpdateValuesByDataFilterRequestIn",
        "BatchUpdateValuesByDataFilterRequestOut": "_sheets_387_BatchUpdateValuesByDataFilterRequestOut",
        "AddDataSourceRequestIn": "_sheets_388_AddDataSourceRequestIn",
        "AddDataSourceRequestOut": "_sheets_389_AddDataSourceRequestOut",
        "WaterfallChartCustomSubtotalIn": "_sheets_390_WaterfallChartCustomSubtotalIn",
        "WaterfallChartCustomSubtotalOut": "_sheets_391_WaterfallChartCustomSubtotalOut",
        "UpdateDataSourceRequestIn": "_sheets_392_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_sheets_393_UpdateDataSourceRequestOut",
        "BatchClearValuesResponseIn": "_sheets_394_BatchClearValuesResponseIn",
        "BatchClearValuesResponseOut": "_sheets_395_BatchClearValuesResponseOut",
        "UpdateSpreadsheetPropertiesRequestIn": "_sheets_396_UpdateSpreadsheetPropertiesRequestIn",
        "UpdateSpreadsheetPropertiesRequestOut": "_sheets_397_UpdateSpreadsheetPropertiesRequestOut",
        "SearchDeveloperMetadataResponseIn": "_sheets_398_SearchDeveloperMetadataResponseIn",
        "SearchDeveloperMetadataResponseOut": "_sheets_399_SearchDeveloperMetadataResponseOut",
        "RowDataIn": "_sheets_400_RowDataIn",
        "RowDataOut": "_sheets_401_RowDataOut",
        "CreateDeveloperMetadataResponseIn": "_sheets_402_CreateDeveloperMetadataResponseIn",
        "CreateDeveloperMetadataResponseOut": "_sheets_403_CreateDeveloperMetadataResponseOut",
        "SheetPropertiesIn": "_sheets_404_SheetPropertiesIn",
        "SheetPropertiesOut": "_sheets_405_SheetPropertiesOut",
        "PaddingIn": "_sheets_406_PaddingIn",
        "PaddingOut": "_sheets_407_PaddingOut",
        "ClearValuesResponseIn": "_sheets_408_ClearValuesResponseIn",
        "ClearValuesResponseOut": "_sheets_409_ClearValuesResponseOut",
        "InterpolationPointIn": "_sheets_410_InterpolationPointIn",
        "InterpolationPointOut": "_sheets_411_InterpolationPointOut",
        "DataValidationRuleIn": "_sheets_412_DataValidationRuleIn",
        "DataValidationRuleOut": "_sheets_413_DataValidationRuleOut",
        "NamedRangeIn": "_sheets_414_NamedRangeIn",
        "NamedRangeOut": "_sheets_415_NamedRangeOut",
        "DataSourceRefreshScheduleIn": "_sheets_416_DataSourceRefreshScheduleIn",
        "DataSourceRefreshScheduleOut": "_sheets_417_DataSourceRefreshScheduleOut",
        "ChartCustomNumberFormatOptionsIn": "_sheets_418_ChartCustomNumberFormatOptionsIn",
        "ChartCustomNumberFormatOptionsOut": "_sheets_419_ChartCustomNumberFormatOptionsOut",
        "PivotGroupRuleIn": "_sheets_420_PivotGroupRuleIn",
        "PivotGroupRuleOut": "_sheets_421_PivotGroupRuleOut",
        "BasicChartAxisIn": "_sheets_422_BasicChartAxisIn",
        "BasicChartAxisOut": "_sheets_423_BasicChartAxisOut",
        "TrimWhitespaceResponseIn": "_sheets_424_TrimWhitespaceResponseIn",
        "TrimWhitespaceResponseOut": "_sheets_425_TrimWhitespaceResponseOut",
        "AddDimensionGroupResponseIn": "_sheets_426_AddDimensionGroupResponseIn",
        "AddDimensionGroupResponseOut": "_sheets_427_AddDimensionGroupResponseOut",
        "PieChartSpecIn": "_sheets_428_PieChartSpecIn",
        "PieChartSpecOut": "_sheets_429_PieChartSpecOut",
        "GridCoordinateIn": "_sheets_430_GridCoordinateIn",
        "GridCoordinateOut": "_sheets_431_GridCoordinateOut",
        "BatchGetValuesResponseIn": "_sheets_432_BatchGetValuesResponseIn",
        "BatchGetValuesResponseOut": "_sheets_433_BatchGetValuesResponseOut",
        "EmbeddedObjectBorderIn": "_sheets_434_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_sheets_435_EmbeddedObjectBorderOut",
        "BatchUpdateSpreadsheetRequestIn": "_sheets_436_BatchUpdateSpreadsheetRequestIn",
        "BatchUpdateSpreadsheetRequestOut": "_sheets_437_BatchUpdateSpreadsheetRequestOut",
        "DeleteDimensionGroupRequestIn": "_sheets_438_DeleteDimensionGroupRequestIn",
        "DeleteDimensionGroupRequestOut": "_sheets_439_DeleteDimensionGroupRequestOut",
        "CandlestickDomainIn": "_sheets_440_CandlestickDomainIn",
        "CandlestickDomainOut": "_sheets_441_CandlestickDomainOut",
        "UpdateCellsRequestIn": "_sheets_442_UpdateCellsRequestIn",
        "UpdateCellsRequestOut": "_sheets_443_UpdateCellsRequestOut",
        "DeleteConditionalFormatRuleRequestIn": "_sheets_444_DeleteConditionalFormatRuleRequestIn",
        "DeleteConditionalFormatRuleRequestOut": "_sheets_445_DeleteConditionalFormatRuleRequestOut",
        "BigQueryDataSourceSpecIn": "_sheets_446_BigQueryDataSourceSpecIn",
        "BigQueryDataSourceSpecOut": "_sheets_447_BigQueryDataSourceSpecOut",
        "DataFilterValueRangeIn": "_sheets_448_DataFilterValueRangeIn",
        "DataFilterValueRangeOut": "_sheets_449_DataFilterValueRangeOut",
        "EmbeddedObjectPositionIn": "_sheets_450_EmbeddedObjectPositionIn",
        "EmbeddedObjectPositionOut": "_sheets_451_EmbeddedObjectPositionOut",
        "UpdateEmbeddedObjectPositionResponseIn": "_sheets_452_UpdateEmbeddedObjectPositionResponseIn",
        "UpdateEmbeddedObjectPositionResponseOut": "_sheets_453_UpdateEmbeddedObjectPositionResponseOut",
        "UpdateDeveloperMetadataResponseIn": "_sheets_454_UpdateDeveloperMetadataResponseIn",
        "UpdateDeveloperMetadataResponseOut": "_sheets_455_UpdateDeveloperMetadataResponseOut",
        "SearchDeveloperMetadataRequestIn": "_sheets_456_SearchDeveloperMetadataRequestIn",
        "SearchDeveloperMetadataRequestOut": "_sheets_457_SearchDeveloperMetadataRequestOut",
        "UpdateNamedRangeRequestIn": "_sheets_458_UpdateNamedRangeRequestIn",
        "UpdateNamedRangeRequestOut": "_sheets_459_UpdateNamedRangeRequestOut",
        "WaterfallChartSeriesIn": "_sheets_460_WaterfallChartSeriesIn",
        "WaterfallChartSeriesOut": "_sheets_461_WaterfallChartSeriesOut",
        "DeleteNamedRangeRequestIn": "_sheets_462_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_sheets_463_DeleteNamedRangeRequestOut",
        "UpdateBandingRequestIn": "_sheets_464_UpdateBandingRequestIn",
        "UpdateBandingRequestOut": "_sheets_465_UpdateBandingRequestOut",
        "ValueRangeIn": "_sheets_466_ValueRangeIn",
        "ValueRangeOut": "_sheets_467_ValueRangeOut",
        "CellDataIn": "_sheets_468_CellDataIn",
        "CellDataOut": "_sheets_469_CellDataOut",
        "DeleteDuplicatesResponseIn": "_sheets_470_DeleteDuplicatesResponseIn",
        "DeleteDuplicatesResponseOut": "_sheets_471_DeleteDuplicatesResponseOut",
        "TextToColumnsRequestIn": "_sheets_472_TextToColumnsRequestIn",
        "TextToColumnsRequestOut": "_sheets_473_TextToColumnsRequestOut",
        "CreateDeveloperMetadataRequestIn": "_sheets_474_CreateDeveloperMetadataRequestIn",
        "CreateDeveloperMetadataRequestOut": "_sheets_475_CreateDeveloperMetadataRequestOut",
        "DateTimeRuleIn": "_sheets_476_DateTimeRuleIn",
        "DateTimeRuleOut": "_sheets_477_DateTimeRuleOut",
        "DeleteRangeRequestIn": "_sheets_478_DeleteRangeRequestIn",
        "DeleteRangeRequestOut": "_sheets_479_DeleteRangeRequestOut",
        "BigQueryQuerySpecIn": "_sheets_480_BigQueryQuerySpecIn",
        "BigQueryQuerySpecOut": "_sheets_481_BigQueryQuerySpecOut",
        "AddBandingResponseIn": "_sheets_482_AddBandingResponseIn",
        "AddBandingResponseOut": "_sheets_483_AddBandingResponseOut",
        "DeleteProtectedRangeRequestIn": "_sheets_484_DeleteProtectedRangeRequestIn",
        "DeleteProtectedRangeRequestOut": "_sheets_485_DeleteProtectedRangeRequestOut",
        "PivotGroupSortValueBucketIn": "_sheets_486_PivotGroupSortValueBucketIn",
        "PivotGroupSortValueBucketOut": "_sheets_487_PivotGroupSortValueBucketOut",
        "DataSourceRefreshMonthlyScheduleIn": "_sheets_488_DataSourceRefreshMonthlyScheduleIn",
        "DataSourceRefreshMonthlyScheduleOut": "_sheets_489_DataSourceRefreshMonthlyScheduleOut",
        "ConditionalFormatRuleIn": "_sheets_490_ConditionalFormatRuleIn",
        "ConditionalFormatRuleOut": "_sheets_491_ConditionalFormatRuleOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AddSheetRequestIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetRequestIn"])
    types["AddSheetRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetRequestOut"])
    types["ScorecardChartSpecIn"] = t.struct(
        {
            "aggregateType": t.string().optional(),
            "numberFormatSource": t.string().optional(),
            "baselineValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "keyValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "scaleFactor": t.number().optional(),
            "keyValueFormat": t.proxy(renames["KeyValueFormatIn"]).optional(),
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsIn"]
            ).optional(),
            "baselineValueFormat": t.proxy(renames["BaselineValueFormatIn"]).optional(),
        }
    ).named(renames["ScorecardChartSpecIn"])
    types["ScorecardChartSpecOut"] = t.struct(
        {
            "aggregateType": t.string().optional(),
            "numberFormatSource": t.string().optional(),
            "baselineValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "keyValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "scaleFactor": t.number().optional(),
            "keyValueFormat": t.proxy(renames["KeyValueFormatOut"]).optional(),
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsOut"]
            ).optional(),
            "baselineValueFormat": t.proxy(
                renames["BaselineValueFormatOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScorecardChartSpecOut"])
    types["UpdateConditionalFormatRuleResponseIn"] = t.struct(
        {
            "oldIndex": t.integer().optional(),
            "newIndex": t.integer().optional(),
            "newRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseIn"])
    types["UpdateConditionalFormatRuleResponseOut"] = t.struct(
        {
            "oldIndex": t.integer().optional(),
            "newIndex": t.integer().optional(),
            "newRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseOut"])
    types["OrgChartSpecIn"] = t.struct(
        {
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "nodeColor": t.proxy(renames["ColorIn"]).optional(),
            "tooltips": t.proxy(renames["ChartDataIn"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "nodeSize": t.string().optional(),
            "selectedNodeColor": t.proxy(renames["ColorIn"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["OrgChartSpecIn"])
    types["OrgChartSpecOut"] = t.struct(
        {
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "nodeColor": t.proxy(renames["ColorOut"]).optional(),
            "tooltips": t.proxy(renames["ChartDataOut"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "nodeSize": t.string().optional(),
            "selectedNodeColor": t.proxy(renames["ColorOut"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgChartSpecOut"])
    types["DataSourceColumnReferenceIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["DataSourceColumnReferenceIn"])
    types["DataSourceColumnReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceColumnReferenceOut"])
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
    types["AddNamedRangeRequestIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeRequestIn"])
    types["AddNamedRangeRequestOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeRequestOut"])
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
    types["CandlestickDataIn"] = t.struct(
        {
            "openSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "highSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "lowSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
        }
    ).named(renames["CandlestickDataIn"])
    types["CandlestickDataOut"] = t.struct(
        {
            "openSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "highSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "lowSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickDataOut"])
    types["AddBandingRequestIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingRequestIn"])
    types["AddBandingRequestOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingRequestOut"])
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
    types["GradientRuleIn"] = t.struct(
        {
            "maxpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
            "minpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
            "midpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
        }
    ).named(renames["GradientRuleIn"])
    types["GradientRuleOut"] = t.struct(
        {
            "maxpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "minpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "midpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradientRuleOut"])
    types["EditorsIn"] = t.struct(
        {
            "domainUsersCanEdit": t.boolean().optional(),
            "groups": t.array(t.string()).optional(),
            "users": t.array(t.string()).optional(),
        }
    ).named(renames["EditorsIn"])
    types["EditorsOut"] = t.struct(
        {
            "domainUsersCanEdit": t.boolean().optional(),
            "groups": t.array(t.string()).optional(),
            "users": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditorsOut"])
    types["DuplicateFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DuplicateFilterViewRequestIn"])
    types["DuplicateFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewRequestOut"])
    types["TextFormatRunIn"] = t.struct(
        {
            "format": t.proxy(renames["TextFormatIn"]).optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["TextFormatRunIn"])
    types["TextFormatRunOut"] = t.struct(
        {
            "format": t.proxy(renames["TextFormatOut"]).optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFormatRunOut"])
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
    types["TextFormatIn"] = t.struct(
        {
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "underline": t.boolean().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "fontFamily": t.string().optional(),
            "strikethrough": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "italic": t.boolean().optional(),
            "bold": t.boolean().optional(),
        }
    ).named(renames["TextFormatIn"])
    types["TextFormatOut"] = t.struct(
        {
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "underline": t.boolean().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "fontFamily": t.string().optional(),
            "strikethrough": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "italic": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFormatOut"])
    types["SpreadsheetIn"] = t.struct(
        {
            "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
            "spreadsheetId": t.string().optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
            "spreadsheetUrl": t.string().optional(),
        }
    ).named(renames["SpreadsheetIn"])
    types["SpreadsheetOut"] = t.struct(
        {
            "dataSources": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "dataSourceSchedules": t.array(
                t.proxy(renames["DataSourceRefreshScheduleOut"])
            ).optional(),
            "sheets": t.array(t.proxy(renames["SheetOut"])).optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeOut"])).optional(),
            "spreadsheetId": t.string().optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesOut"]).optional(),
            "spreadsheetUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetOut"])
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
    types["ProtectedRangeIn"] = t.struct(
        {
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "description": t.string().optional(),
            "editors": t.proxy(renames["EditorsIn"]).optional(),
            "warningOnly": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "protectedRangeId": t.integer().optional(),
            "namedRangeId": t.string().optional(),
            "requestingUserCanEdit": t.boolean().optional(),
        }
    ).named(renames["ProtectedRangeIn"])
    types["ProtectedRangeOut"] = t.struct(
        {
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "description": t.string().optional(),
            "editors": t.proxy(renames["EditorsOut"]).optional(),
            "warningOnly": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "protectedRangeId": t.integer().optional(),
            "namedRangeId": t.string().optional(),
            "requestingUserCanEdit": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProtectedRangeOut"])
    types["DeleteSheetRequestIn"] = t.struct({"sheetId": t.integer().optional()}).named(
        renames["DeleteSheetRequestIn"]
    )
    types["DeleteSheetRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteSheetRequestOut"])
    types["SheetIn"] = t.struct(
        {
            "data": t.array(t.proxy(renames["GridDataIn"])).optional(),
            "merges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterIn"]).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewIn"])).optional(),
            "columnGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "properties": t.proxy(renames["SheetPropertiesIn"]).optional(),
            "slicers": t.array(t.proxy(renames["SlicerIn"])).optional(),
            "bandedRanges": t.array(t.proxy(renames["BandedRangeIn"])).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleIn"])
            ).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "protectedRanges": t.array(t.proxy(renames["ProtectedRangeIn"])).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartIn"])).optional(),
        }
    ).named(renames["SheetIn"])
    types["SheetOut"] = t.struct(
        {
            "data": t.array(t.proxy(renames["GridDataOut"])).optional(),
            "merges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterOut"]).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewOut"])).optional(),
            "columnGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "slicers": t.array(t.proxy(renames["SlicerOut"])).optional(),
            "bandedRanges": t.array(t.proxy(renames["BandedRangeOut"])).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleOut"])
            ).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "protectedRanges": t.array(
                t.proxy(renames["ProtectedRangeOut"])
            ).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetOut"])
    types["RandomizeRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["RandomizeRangeRequestIn"])
    types["RandomizeRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RandomizeRangeRequestOut"])
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
    types["ResponseIn"] = t.struct(
        {
            "addBanding": t.proxy(renames["AddBandingResponseIn"]).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseIn"]
            ).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseIn"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseIn"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseIn"]
            ).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseIn"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseIn"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseIn"]).optional(),
            "addChart": t.proxy(renames["AddChartResponseIn"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseIn"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseIn"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseIn"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseIn"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseIn"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseIn"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseIn"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseIn"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseIn"]).optional(),
            "addSheet": t.proxy(renames["AddSheetResponseIn"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseIn"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseIn"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseIn"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseIn"]
            ).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "addBanding": t.proxy(renames["AddBandingResponseOut"]).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseOut"]
            ).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseOut"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseOut"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseOut"]
            ).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseOut"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseOut"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseOut"]).optional(),
            "addChart": t.proxy(renames["AddChartResponseOut"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseOut"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseOut"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseOut"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseOut"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseOut"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseOut"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseOut"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseOut"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseOut"]).optional(),
            "addSheet": t.proxy(renames["AddSheetResponseOut"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseOut"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseOut"]).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseOut"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["DataLabelIn"] = t.struct(
        {
            "placement": t.string().optional(),
            "type": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "customLabelData": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["DataLabelIn"])
    types["DataLabelOut"] = t.struct(
        {
            "placement": t.string().optional(),
            "type": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "customLabelData": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLabelOut"])
    types["TreemapChartSpecIn"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "colorScale": t.proxy(renames["TreemapChartColorScaleIn"]).optional(),
            "colorData": t.proxy(renames["ChartDataIn"]).optional(),
            "levels": t.integer().optional(),
            "hintedLevels": t.integer().optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "sizeData": t.proxy(renames["ChartDataIn"]).optional(),
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "minValue": t.number().optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["TreemapChartSpecIn"])
    types["TreemapChartSpecOut"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "colorScale": t.proxy(renames["TreemapChartColorScaleOut"]).optional(),
            "colorData": t.proxy(renames["ChartDataOut"]).optional(),
            "levels": t.integer().optional(),
            "hintedLevels": t.integer().optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "sizeData": t.proxy(renames["ChartDataOut"]).optional(),
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "minValue": t.number().optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartSpecOut"])
    types["DataSourceRefreshDailyScheduleIn"] = t.struct(
        {"startTime": t.proxy(renames["TimeOfDayIn"]).optional()}
    ).named(renames["DataSourceRefreshDailyScheduleIn"])
    types["DataSourceRefreshDailyScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshDailyScheduleOut"])
    types["AddChartResponseIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartResponseIn"])
    types["AddChartResponseOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartResponseOut"])
    types["PasteDataRequestIn"] = t.struct(
        {
            "delimiter": t.string().optional(),
            "coordinate": t.proxy(renames["GridCoordinateIn"]).optional(),
            "type": t.string().optional(),
            "html": t.boolean().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["PasteDataRequestIn"])
    types["PasteDataRequestOut"] = t.struct(
        {
            "delimiter": t.string().optional(),
            "coordinate": t.proxy(renames["GridCoordinateOut"]).optional(),
            "type": t.string().optional(),
            "html": t.boolean().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasteDataRequestOut"])
    types["BatchUpdateValuesRequestIn"] = t.struct(
        {
            "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "valueInputOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesRequestIn"])
    types["BatchUpdateValuesRequestOut"] = t.struct(
        {
            "data": t.array(t.proxy(renames["ValueRangeOut"])).optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "valueInputOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesRequestOut"])
    types["DuplicateSheetRequestIn"] = t.struct(
        {
            "insertSheetIndex": t.integer().optional(),
            "sourceSheetId": t.integer().optional(),
            "newSheetName": t.string().optional(),
            "newSheetId": t.integer().optional(),
        }
    ).named(renames["DuplicateSheetRequestIn"])
    types["DuplicateSheetRequestOut"] = t.struct(
        {
            "insertSheetIndex": t.integer().optional(),
            "sourceSheetId": t.integer().optional(),
            "newSheetName": t.string().optional(),
            "newSheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetRequestOut"])
    types["BigQueryTableSpecIn"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableProjectId": t.string().optional(),
            "tableId": t.string().optional(),
        }
    ).named(renames["BigQueryTableSpecIn"])
    types["BigQueryTableSpecOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableProjectId": t.string().optional(),
            "tableId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryTableSpecOut"])
    types["GridRangeIn"] = t.struct(
        {
            "endRowIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
            "startRowIndex": t.integer().optional(),
            "startColumnIndex": t.integer().optional(),
        }
    ).named(renames["GridRangeIn"])
    types["GridRangeOut"] = t.struct(
        {
            "endRowIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
            "startRowIndex": t.integer().optional(),
            "startColumnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridRangeOut"])
    types["HistogramRuleIn"] = t.struct(
        {
            "end": t.number().optional(),
            "interval": t.number().optional(),
            "start": t.number().optional(),
        }
    ).named(renames["HistogramRuleIn"])
    types["HistogramRuleOut"] = t.struct(
        {
            "end": t.number().optional(),
            "interval": t.number().optional(),
            "start": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramRuleOut"])
    types["DataSourceObjectReferenceIn"] = t.struct(
        {
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "chartId": t.integer().optional(),
            "sheetId": t.string().optional(),
        }
    ).named(renames["DataSourceObjectReferenceIn"])
    types["DataSourceObjectReferenceOut"] = t.struct(
        {
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "chartId": t.integer().optional(),
            "sheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceObjectReferenceOut"])
    types["CopyPasteRequestIn"] = t.struct(
        {
            "destination": t.proxy(renames["GridRangeIn"]).optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "pasteOrientation": t.string().optional(),
            "pasteType": t.string().optional(),
        }
    ).named(renames["CopyPasteRequestIn"])
    types["CopyPasteRequestOut"] = t.struct(
        {
            "destination": t.proxy(renames["GridRangeOut"]).optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "pasteOrientation": t.string().optional(),
            "pasteType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyPasteRequestOut"])
    types["DataFilterIn"] = t.struct(
        {
            "developerMetadataLookup": t.proxy(
                renames["DeveloperMetadataLookupIn"]
            ).optional(),
            "gridRange": t.proxy(renames["GridRangeIn"]).optional(),
            "a1Range": t.string().optional(),
        }
    ).named(renames["DataFilterIn"])
    types["DataFilterOut"] = t.struct(
        {
            "developerMetadataLookup": t.proxy(
                renames["DeveloperMetadataLookupOut"]
            ).optional(),
            "gridRange": t.proxy(renames["GridRangeOut"]).optional(),
            "a1Range": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataFilterOut"])
    types["CopySheetToAnotherSpreadsheetRequestIn"] = t.struct(
        {"destinationSpreadsheetId": t.string().optional()}
    ).named(renames["CopySheetToAnotherSpreadsheetRequestIn"])
    types["CopySheetToAnotherSpreadsheetRequestOut"] = t.struct(
        {
            "destinationSpreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopySheetToAnotherSpreadsheetRequestOut"])
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
    types["DataSourceParameterIn"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DataSourceParameterIn"])
    types["DataSourceParameterOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceParameterOut"])
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
    types["DuplicateFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["DuplicateFilterViewResponseIn"])
    types["DuplicateFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewResponseOut"])
    types["OverlayPositionIn"] = t.struct(
        {
            "heightPixels": t.integer().optional(),
            "offsetXPixels": t.integer().optional(),
            "anchorCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "offsetYPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
        }
    ).named(renames["OverlayPositionIn"])
    types["OverlayPositionOut"] = t.struct(
        {
            "heightPixels": t.integer().optional(),
            "offsetXPixels": t.integer().optional(),
            "anchorCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "offsetYPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OverlayPositionOut"])
    types["FilterSpecIn"] = t.struct(
        {
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "columnIndex": t.integer().optional(),
        }
    ).named(renames["FilterSpecIn"])
    types["FilterSpecOut"] = t.struct(
        {
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "columnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterSpecOut"])
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
    types["DeveloperMetadataIn"] = t.struct(
        {
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "metadataKey": t.string().optional(),
            "metadataId": t.integer().optional(),
            "location": t.proxy(renames["DeveloperMetadataLocationIn"]).optional(),
        }
    ).named(renames["DeveloperMetadataIn"])
    types["DeveloperMetadataOut"] = t.struct(
        {
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "metadataKey": t.string().optional(),
            "metadataId": t.integer().optional(),
            "location": t.proxy(renames["DeveloperMetadataLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataOut"])
    types["BatchGetValuesByDataFilterRequestIn"] = t.struct(
        {
            "majorDimension": t.string().optional(),
            "valueRenderOption": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "dateTimeRenderOption": t.string().optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestIn"])
    types["BatchGetValuesByDataFilterRequestOut"] = t.struct(
        {
            "majorDimension": t.string().optional(),
            "valueRenderOption": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "dateTimeRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestOut"])
    types["BasicSeriesDataPointStyleOverrideIn"] = t.struct(
        {
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "index": t.integer().optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideIn"])
    types["BasicSeriesDataPointStyleOverrideOut"] = t.struct(
        {
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "index": t.integer().optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideOut"])
    types["WaterfallChartColumnStyleIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "label": t.string().optional(),
        }
    ).named(renames["WaterfallChartColumnStyleIn"])
    types["WaterfallChartColumnStyleOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartColumnStyleOut"])
    types["GridDataIn"] = t.struct(
        {
            "rowData": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "startColumn": t.integer().optional(),
            "startRow": t.integer().optional(),
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
        }
    ).named(renames["GridDataIn"])
    types["GridDataOut"] = t.struct(
        {
            "rowData": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "startColumn": t.integer().optional(),
            "startRow": t.integer().optional(),
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridDataOut"])
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
    types["ChartDateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ChartDateTimeRuleIn"]
    )
    types["ChartDateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDateTimeRuleOut"])
    types["TextPositionIn"] = t.struct(
        {"horizontalAlignment": t.string().optional()}
    ).named(renames["TextPositionIn"])
    types["TextPositionOut"] = t.struct(
        {
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPositionOut"])
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
    types["ClearBasicFilterRequestIn"] = t.struct(
        {"sheetId": t.integer().optional()}
    ).named(renames["ClearBasicFilterRequestIn"])
    types["ClearBasicFilterRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearBasicFilterRequestOut"])
    types["RefreshDataSourceRequestIn"] = t.struct(
        {
            "references": t.proxy(renames["DataSourceObjectReferencesIn"]).optional(),
            "dataSourceId": t.string().optional(),
            "force": t.boolean().optional(),
            "isAll": t.boolean().optional(),
        }
    ).named(renames["RefreshDataSourceRequestIn"])
    types["RefreshDataSourceRequestOut"] = t.struct(
        {
            "references": t.proxy(renames["DataSourceObjectReferencesOut"]).optional(),
            "dataSourceId": t.string().optional(),
            "force": t.boolean().optional(),
            "isAll": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshDataSourceRequestOut"])
    types["DeleteDimensionRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionRequestIn"])
    types["DeleteDimensionRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionRequestOut"])
    types["AutoFillRequestIn"] = t.struct(
        {
            "useAlternateSeries": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationIn"]
            ).optional(),
        }
    ).named(renames["AutoFillRequestIn"])
    types["AutoFillRequestOut"] = t.struct(
        {
            "useAlternateSeries": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoFillRequestOut"])
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
    types["AddProtectedRangeRequestIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeRequestIn"])
    types["AddProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeRequestOut"])
    types["BandingPropertiesIn"] = t.struct(
        {
            "footerColor": t.proxy(renames["ColorIn"]).optional(),
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "secondBandColor": t.proxy(renames["ColorIn"]).optional(),
            "firstBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "firstBandColor": t.proxy(renames["ColorIn"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BandingPropertiesIn"])
    types["BandingPropertiesOut"] = t.struct(
        {
            "footerColor": t.proxy(renames["ColorOut"]).optional(),
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "secondBandColor": t.proxy(renames["ColorOut"]).optional(),
            "firstBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "firstBandColor": t.proxy(renames["ColorOut"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandingPropertiesOut"])
    types["AddProtectedRangeResponseIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeResponseIn"])
    types["AddProtectedRangeResponseOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeResponseOut"])
    types["BasicFilterIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
        }
    ).named(renames["BasicFilterIn"])
    types["BasicFilterOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicFilterOut"])
    types["DeleteBandingRequestIn"] = t.struct(
        {"bandedRangeId": t.integer().optional()}
    ).named(renames["DeleteBandingRequestIn"])
    types["DeleteBandingRequestOut"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBandingRequestOut"])
    types["PivotFilterCriteriaIn"] = t.struct(
        {
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "visibleValues": t.array(t.string()).optional(),
            "visibleByDefault": t.boolean().optional(),
        }
    ).named(renames["PivotFilterCriteriaIn"])
    types["PivotFilterCriteriaOut"] = t.struct(
        {
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "visibleValues": t.array(t.string()).optional(),
            "visibleByDefault": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotFilterCriteriaOut"])
    types["DimensionRangeIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "dimension": t.string().optional(),
            "sheetId": t.integer().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["DimensionRangeIn"])
    types["DimensionRangeOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "dimension": t.string().optional(),
            "sheetId": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionRangeOut"])
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
    types["DuplicateSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["DuplicateSheetResponseIn"])
    types["DuplicateSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetResponseOut"])
    types["CandlestickChartSpecIn"] = t.struct(
        {
            "data": t.array(t.proxy(renames["CandlestickDataIn"])).optional(),
            "domain": t.proxy(renames["CandlestickDomainIn"]).optional(),
        }
    ).named(renames["CandlestickChartSpecIn"])
    types["CandlestickChartSpecOut"] = t.struct(
        {
            "data": t.array(t.proxy(renames["CandlestickDataOut"])).optional(),
            "domain": t.proxy(renames["CandlestickDomainOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickChartSpecOut"])
    types["ColorStyleIn"] = t.struct(
        {
            "themeColor": t.string().optional(),
            "rgbColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["ColorStyleIn"])
    types["ColorStyleOut"] = t.struct(
        {
            "themeColor": t.string().optional(),
            "rgbColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorStyleOut"])
    types["UpdateDeveloperMetadataRequestIn"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestIn"])
    types["UpdateDeveloperMetadataRequestOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestOut"])
    types["ChartAxisViewWindowOptionsIn"] = t.struct(
        {
            "viewWindowMode": t.string().optional(),
            "viewWindowMin": t.number().optional(),
            "viewWindowMax": t.number().optional(),
        }
    ).named(renames["ChartAxisViewWindowOptionsIn"])
    types["ChartAxisViewWindowOptionsOut"] = t.struct(
        {
            "viewWindowMode": t.string().optional(),
            "viewWindowMin": t.number().optional(),
            "viewWindowMax": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartAxisViewWindowOptionsOut"])
    types["BasicChartSpecIn"] = t.struct(
        {
            "lineSmoothing": t.boolean().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "interpolateNulls": t.boolean().optional(),
            "chartType": t.string().optional(),
            "stackedType": t.string().optional(),
            "headerCount": t.integer().optional(),
            "threeDimensional": t.boolean().optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesIn"])).optional(),
            "legendPosition": t.string().optional(),
            "compareMode": t.string().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainIn"])).optional(),
            "axis": t.array(t.proxy(renames["BasicChartAxisIn"])).optional(),
        }
    ).named(renames["BasicChartSpecIn"])
    types["BasicChartSpecOut"] = t.struct(
        {
            "lineSmoothing": t.boolean().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "interpolateNulls": t.boolean().optional(),
            "chartType": t.string().optional(),
            "stackedType": t.string().optional(),
            "headerCount": t.integer().optional(),
            "threeDimensional": t.boolean().optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesOut"])).optional(),
            "legendPosition": t.string().optional(),
            "compareMode": t.string().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainOut"])).optional(),
            "axis": t.array(t.proxy(renames["BasicChartAxisOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSpecOut"])
    types["PivotValueIn"] = t.struct(
        {
            "calculatedDisplayType": t.string().optional(),
            "formula": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "summarizeFunction": t.string().optional(),
            "name": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
        }
    ).named(renames["PivotValueIn"])
    types["PivotValueOut"] = t.struct(
        {
            "calculatedDisplayType": t.string().optional(),
            "formula": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "summarizeFunction": t.string().optional(),
            "name": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueOut"])
    types["FindReplaceResponseIn"] = t.struct(
        {
            "sheetsChanged": t.integer().optional(),
            "rowsChanged": t.integer().optional(),
            "valuesChanged": t.integer().optional(),
            "occurrencesChanged": t.integer().optional(),
            "formulasChanged": t.integer().optional(),
        }
    ).named(renames["FindReplaceResponseIn"])
    types["FindReplaceResponseOut"] = t.struct(
        {
            "sheetsChanged": t.integer().optional(),
            "rowsChanged": t.integer().optional(),
            "valuesChanged": t.integer().optional(),
            "occurrencesChanged": t.integer().optional(),
            "formulasChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceResponseOut"])
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
    types["PointStyleIn"] = t.struct(
        {"size": t.number().optional(), "shape": t.string().optional()}
    ).named(renames["PointStyleIn"])
    types["PointStyleOut"] = t.struct(
        {
            "size": t.number().optional(),
            "shape": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PointStyleOut"])
    types["DataSourceSheetPropertiesIn"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["DataSourceColumnIn"])).optional(),
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
            "dataSourceId": t.string().optional(),
        }
    ).named(renames["DataSourceSheetPropertiesIn"])
    types["DataSourceSheetPropertiesOut"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["DataSourceColumnOut"])).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSheetPropertiesOut"])
    types["SlicerSpecIn"] = t.struct(
        {
            "dataRange": t.proxy(renames["GridRangeIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "title": t.string().optional(),
            "applyToPivotTables": t.boolean().optional(),
            "horizontalAlignment": t.string().optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
            "columnIndex": t.integer().optional(),
        }
    ).named(renames["SlicerSpecIn"])
    types["SlicerSpecOut"] = t.struct(
        {
            "dataRange": t.proxy(renames["GridRangeOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "title": t.string().optional(),
            "applyToPivotTables": t.boolean().optional(),
            "horizontalAlignment": t.string().optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "columnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerSpecOut"])
    types["AddNamedRangeResponseIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeResponseIn"])
    types["AddNamedRangeResponseOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeResponseOut"])
    types["BubbleChartSpecIn"] = t.struct(
        {
            "bubbleOpacity": t.number().optional(),
            "groupIds": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleMaxRadiusSize": t.integer().optional(),
            "bubbleBorderColor": t.proxy(renames["ColorIn"]).optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatIn"]).optional(),
            "bubbleSizes": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "legendPosition": t.string().optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "bubbleLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["BubbleChartSpecIn"])
    types["BubbleChartSpecOut"] = t.struct(
        {
            "bubbleOpacity": t.number().optional(),
            "groupIds": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleMaxRadiusSize": t.integer().optional(),
            "bubbleBorderColor": t.proxy(renames["ColorOut"]).optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatOut"]).optional(),
            "bubbleSizes": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "legendPosition": t.string().optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "bubbleLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BubbleChartSpecOut"])
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
    types["DeleteDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilter": t.proxy(renames["DataFilterIn"]).optional()}
    ).named(renames["DeleteDeveloperMetadataRequestIn"])
    types["DeleteDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDeveloperMetadataRequestOut"])
    types["AddSlicerResponseIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerResponseIn"])
    types["AddSlicerResponseOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerResponseOut"])
    types["UpdateEmbeddedObjectBorderRequestIn"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "fields": t.string().optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestIn"])
    types["UpdateEmbeddedObjectBorderRequestOut"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "fields": t.string().optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestOut"])
    types["UpdateValuesResponseIn"] = t.struct(
        {
            "updatedColumns": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "updatedCells": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedRows": t.integer().optional(),
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
        }
    ).named(renames["UpdateValuesResponseIn"])
    types["UpdateValuesResponseOut"] = t.struct(
        {
            "updatedColumns": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "updatedCells": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedRows": t.integer().optional(),
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesResponseOut"])
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
    types["UpdateSlicerSpecRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "slicerId": t.integer().optional(),
            "spec": t.proxy(renames["SlicerSpecIn"]).optional(),
        }
    ).named(renames["UpdateSlicerSpecRequestIn"])
    types["UpdateSlicerSpecRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "slicerId": t.integer().optional(),
            "spec": t.proxy(renames["SlicerSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlicerSpecRequestOut"])
    types["SetBasicFilterRequestIn"] = t.struct(
        {"filter": t.proxy(renames["BasicFilterIn"]).optional()}
    ).named(renames["SetBasicFilterRequestIn"])
    types["SetBasicFilterRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["BasicFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetBasicFilterRequestOut"])
    types["AddDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["AddDimensionGroupRequestIn"])
    types["AddDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDimensionGroupRequestOut"])
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
    types["UpdateConditionalFormatRuleRequestIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "newIndex": t.integer().optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestIn"])
    types["UpdateConditionalFormatRuleRequestOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "newIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestOut"])
    types["ManualRuleIn"] = t.struct(
        {"groups": t.array(t.proxy(renames["ManualRuleGroupIn"])).optional()}
    ).named(renames["ManualRuleIn"])
    types["ManualRuleOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["ManualRuleGroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualRuleOut"])
    types["DataSourceIn"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "sheetId": t.integer().optional(),
            "spec": t.proxy(renames["DataSourceSpecIn"]).optional(),
            "calculatedColumns": t.array(
                t.proxy(renames["DataSourceColumnIn"])
            ).optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "sheetId": t.integer().optional(),
            "spec": t.proxy(renames["DataSourceSpecOut"]).optional(),
            "calculatedColumns": t.array(
                t.proxy(renames["DataSourceColumnOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["CandlestickSeriesIn"] = t.struct(
        {"data": t.proxy(renames["ChartDataIn"]).optional()}
    ).named(renames["CandlestickSeriesIn"])
    types["CandlestickSeriesOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickSeriesOut"])
    types["AddChartRequestIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartRequestIn"])
    types["AddChartRequestOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartRequestOut"])
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
    types["UnmergeCellsRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["UnmergeCellsRequestIn"])
    types["UnmergeCellsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeCellsRequestOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["BorderIn"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "style": t.string().optional(),
            "width": t.integer().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["BorderIn"])
    types["BorderOut"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "style": t.string().optional(),
            "width": t.integer().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BorderOut"])
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
    types["SortSpecIn"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "dimensionIndex": t.integer().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["SortSpecIn"])
    types["SortSpecOut"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "dimensionIndex": t.integer().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortSpecOut"])
    types["ClearValuesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClearValuesRequestIn"]
    )
    types["ClearValuesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearValuesRequestOut"])
    types["BatchUpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "totalUpdatedSheets": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseIn"])
            ).optional(),
            "totalUpdatedCells": t.integer().optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseIn"])
    types["BatchUpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "totalUpdatedSheets": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseOut"])
            ).optional(),
            "totalUpdatedCells": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseOut"])
    types["ExtendedValueIn"] = t.struct(
        {
            "formulaValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "errorValue": t.proxy(renames["ErrorValueIn"]).optional(),
        }
    ).named(renames["ExtendedValueIn"])
    types["ExtendedValueOut"] = t.struct(
        {
            "formulaValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "errorValue": t.proxy(renames["ErrorValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedValueOut"])
    types["BatchUpdateValuesResponseIn"] = t.struct(
        {
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(t.proxy(renames["UpdateValuesResponseIn"])).optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedColumns": t.integer().optional(),
        }
    ).named(renames["BatchUpdateValuesResponseIn"])
    types["BatchUpdateValuesResponseOut"] = t.struct(
        {
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesResponseOut"])
            ).optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesResponseOut"])
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
    types["BatchClearValuesByDataFilterResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "clearedRanges": t.array(t.string()).optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterResponseIn"])
    types["BatchClearValuesByDataFilterResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "clearedRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterResponseOut"])
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
    types["ChartSourceRangeIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["GridRangeIn"])).optional()}
    ).named(renames["ChartSourceRangeIn"])
    types["ChartSourceRangeOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSourceRangeOut"])
    types["FindReplaceRequestIn"] = t.struct(
        {
            "matchEntireCell": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "allSheets": t.boolean().optional(),
            "matchCase": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "find": t.string().optional(),
            "searchByRegex": t.boolean().optional(),
            "replacement": t.string().optional(),
            "includeFormulas": t.boolean().optional(),
        }
    ).named(renames["FindReplaceRequestIn"])
    types["FindReplaceRequestOut"] = t.struct(
        {
            "matchEntireCell": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "allSheets": t.boolean().optional(),
            "matchCase": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "find": t.string().optional(),
            "searchByRegex": t.boolean().optional(),
            "replacement": t.string().optional(),
            "includeFormulas": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceRequestOut"])
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
    types["CellFormatIn"] = t.struct(
        {
            "padding": t.proxy(renames["PaddingIn"]).optional(),
            "textRotation": t.proxy(renames["TextRotationIn"]).optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "textDirection": t.string().optional(),
            "borders": t.proxy(renames["BordersIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "verticalAlignment": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "wrapStrategy": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "numberFormat": t.proxy(renames["NumberFormatIn"]).optional(),
        }
    ).named(renames["CellFormatIn"])
    types["CellFormatOut"] = t.struct(
        {
            "padding": t.proxy(renames["PaddingOut"]).optional(),
            "textRotation": t.proxy(renames["TextRotationOut"]).optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "textDirection": t.string().optional(),
            "borders": t.proxy(renames["BordersOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "verticalAlignment": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "wrapStrategy": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "numberFormat": t.proxy(renames["NumberFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellFormatOut"])
    types["FilterViewIn"] = t.struct(
        {
            "title": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "namedRangeId": t.string().optional(),
            "filterViewId": t.integer().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
        }
    ).named(renames["FilterViewIn"])
    types["FilterViewOut"] = t.struct(
        {
            "title": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "namedRangeId": t.string().optional(),
            "filterViewId": t.integer().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterViewOut"])
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
    types["LinkIn"] = t.struct({"uri": t.string().optional()}).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["ColorIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["AddSlicerRequestIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerRequestIn"])
    types["AddSlicerRequestOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerRequestOut"])
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
    types["GetSpreadsheetByDataFilterRequestIn"] = t.struct(
        {
            "includeGridData": t.boolean().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
        }
    ).named(renames["GetSpreadsheetByDataFilterRequestIn"])
    types["GetSpreadsheetByDataFilterRequestOut"] = t.struct(
        {
            "includeGridData": t.boolean().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSpreadsheetByDataFilterRequestOut"])
    types["AddFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewResponseIn"])
    types["AddFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewResponseOut"])
    types["UpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterIn"]).optional(),
            "updatedRange": t.string().optional(),
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
            "updatedRows": t.integer().optional(),
            "updatedColumns": t.integer().optional(),
            "updatedCells": t.integer().optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseIn"])
    types["UpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "updatedRange": t.string().optional(),
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "updatedRows": t.integer().optional(),
            "updatedColumns": t.integer().optional(),
            "updatedCells": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseOut"])
    types["AddSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetResponseIn"])
    types["AddSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetResponseOut"])
    types["EmbeddedChartIn"] = t.struct(
        {
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "spec": t.proxy(renames["ChartSpecIn"]).optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["EmbeddedChartIn"])
    types["EmbeddedChartOut"] = t.struct(
        {
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "spec": t.proxy(renames["ChartSpecOut"]).optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedChartOut"])
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
    types["SpreadsheetPropertiesIn"] = t.struct(
        {
            "locale": t.string().optional(),
            "title": t.string().optional(),
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsIn"]
            ).optional(),
            "autoRecalc": t.string().optional(),
            "defaultFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeIn"]).optional(),
            "timeZone": t.string().optional(),
        }
    ).named(renames["SpreadsheetPropertiesIn"])
    types["SpreadsheetPropertiesOut"] = t.struct(
        {
            "locale": t.string().optional(),
            "title": t.string().optional(),
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsOut"]
            ).optional(),
            "autoRecalc": t.string().optional(),
            "defaultFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeOut"]).optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetPropertiesOut"])
    types["BasicChartSeriesIn"] = t.struct(
        {
            "lineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "targetAxis": t.string().optional(),
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideIn"])
            ).optional(),
            "type": t.string().optional(),
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["BasicChartSeriesIn"])
    types["BasicChartSeriesOut"] = t.struct(
        {
            "lineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "targetAxis": t.string().optional(),
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideOut"])
            ).optional(),
            "type": t.string().optional(),
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSeriesOut"])
    types["UpdateEmbeddedObjectPositionRequestIn"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "newPosition": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionRequestIn"])
    types["UpdateEmbeddedObjectPositionRequestOut"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "newPosition": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionRequestOut"])
    types["DimensionPropertiesIn"] = t.struct(
        {
            "hiddenByFilter": t.boolean().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "hiddenByUser": t.boolean().optional(),
            "pixelSize": t.integer().optional(),
        }
    ).named(renames["DimensionPropertiesIn"])
    types["DimensionPropertiesOut"] = t.struct(
        {
            "hiddenByFilter": t.boolean().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "hiddenByUser": t.boolean().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "pixelSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionPropertiesOut"])
    types["BatchClearValuesByDataFilterRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["BatchClearValuesByDataFilterRequestIn"])
    types["BatchClearValuesByDataFilterRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterRequestOut"])
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
    types["ChartSpecIn"] = t.struct(
        {
            "candlestickChart": t.proxy(renames["CandlestickChartSpecIn"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "treemapChart": t.proxy(renames["TreemapChartSpecIn"]).optional(),
            "altText": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "subtitle": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "maximized": t.boolean().optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecIn"]).optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecIn"]).optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesIn"]
            ).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecIn"]).optional(),
            "basicChart": t.proxy(renames["BasicChartSpecIn"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecIn"]).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecIn"]).optional(),
            "title": t.string().optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "pieChart": t.proxy(renames["PieChartSpecIn"]).optional(),
            "fontName": t.string().optional(),
        }
    ).named(renames["ChartSpecIn"])
    types["ChartSpecOut"] = t.struct(
        {
            "candlestickChart": t.proxy(renames["CandlestickChartSpecOut"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "treemapChart": t.proxy(renames["TreemapChartSpecOut"]).optional(),
            "altText": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "subtitle": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "maximized": t.boolean().optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecOut"]).optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecOut"]).optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesOut"]
            ).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecOut"]).optional(),
            "basicChart": t.proxy(renames["BasicChartSpecOut"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecOut"]).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecOut"]).optional(),
            "title": t.string().optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "pieChart": t.proxy(renames["PieChartSpecOut"]).optional(),
            "fontName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSpecOut"])
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
    types["HistogramChartSpecIn"] = t.struct(
        {
            "showItemDividers": t.boolean().optional(),
            "series": t.array(t.proxy(renames["HistogramSeriesIn"])).optional(),
            "outlierPercentile": t.number().optional(),
            "legendPosition": t.string().optional(),
            "bucketSize": t.number().optional(),
        }
    ).named(renames["HistogramChartSpecIn"])
    types["HistogramChartSpecOut"] = t.struct(
        {
            "showItemDividers": t.boolean().optional(),
            "series": t.array(t.proxy(renames["HistogramSeriesOut"])).optional(),
            "outlierPercentile": t.number().optional(),
            "legendPosition": t.string().optional(),
            "bucketSize": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramChartSpecOut"])
    types["DeveloperMetadataLookupIn"] = t.struct(
        {
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "locationMatchingStrategy": t.string().optional(),
            "metadataKey": t.string().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationIn"]
            ).optional(),
            "metadataId": t.integer().optional(),
            "locationType": t.string().optional(),
        }
    ).named(renames["DeveloperMetadataLookupIn"])
    types["DeveloperMetadataLookupOut"] = t.struct(
        {
            "metadataValue": t.string().optional(),
            "visibility": t.string().optional(),
            "locationMatchingStrategy": t.string().optional(),
            "metadataKey": t.string().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationOut"]
            ).optional(),
            "metadataId": t.integer().optional(),
            "locationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLookupOut"])
    types["RequestIn"] = t.struct(
        {
            "copyPaste": t.proxy(renames["CopyPasteRequestIn"]).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestIn"]
            ).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestIn"]
            ).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestIn"]
            ).optional(),
            "updateBanding": t.proxy(renames["UpdateBandingRequestIn"]).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestIn"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestIn"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestIn"]).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestIn"]).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestIn"]
            ).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestIn"]).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestIn"]).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestIn"]
            ).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestIn"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestIn"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestIn"]
            ).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestIn"]).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestIn"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestIn"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestIn"]).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestIn"]
            ).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestIn"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestIn"]).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestIn"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestIn"]).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestIn"]).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestIn"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestIn"]
            ).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestIn"]).optional(),
            "pasteData": t.proxy(renames["PasteDataRequestIn"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestIn"]).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestIn"]
            ).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestIn"]
            ).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestIn"]
            ).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestIn"]).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestIn"]).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestIn"]
            ).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestIn"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestIn"]
            ).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestIn"]).optional(),
            "updateBorders": t.proxy(renames["UpdateBordersRequestIn"]).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestIn"]).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestIn"]).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestIn"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestIn"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestIn"]).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestIn"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestIn"]
            ).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestIn"]).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestIn"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestIn"]
            ).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestIn"]
            ).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestIn"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestIn"]
            ).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestIn"]
            ).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestIn"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestIn"]
            ).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestIn"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestIn"]).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestIn"]).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestIn"]
            ).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestIn"]).optional(),
            "addChart": t.proxy(renames["AddChartRequestIn"]).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestIn"]
            ).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "copyPaste": t.proxy(renames["CopyPasteRequestOut"]).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestOut"]
            ).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestOut"]
            ).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestOut"]
            ).optional(),
            "updateBanding": t.proxy(renames["UpdateBandingRequestOut"]).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestOut"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestOut"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestOut"]).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestOut"]).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestOut"]
            ).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestOut"]).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestOut"]).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestOut"]
            ).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestOut"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestOut"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestOut"]
            ).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestOut"]).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestOut"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestOut"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestOut"]).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestOut"]
            ).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestOut"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestOut"]).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestOut"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestOut"]).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestOut"]).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestOut"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestOut"]
            ).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestOut"]).optional(),
            "pasteData": t.proxy(renames["PasteDataRequestOut"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestOut"]).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestOut"]
            ).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestOut"]
            ).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestOut"]
            ).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestOut"]).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestOut"]).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestOut"]
            ).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestOut"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestOut"]
            ).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestOut"]).optional(),
            "updateBorders": t.proxy(renames["UpdateBordersRequestOut"]).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestOut"]).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestOut"]).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestOut"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestOut"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestOut"]).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestOut"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestOut"]
            ).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestOut"]).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestOut"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestOut"]
            ).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestOut"]
            ).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestOut"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestOut"]
            ).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestOut"]
            ).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestOut"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestOut"]
            ).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestOut"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestOut"]).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestOut"]).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestOut"]
            ).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestOut"]).optional(),
            "addChart": t.proxy(renames["AddChartRequestOut"]).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["SourceAndDestinationIn"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "fillLength": t.integer().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["SourceAndDestinationIn"])
    types["SourceAndDestinationOut"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "fillLength": t.integer().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceAndDestinationOut"])
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
    types["FilterCriteriaIn"] = t.struct(
        {
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorIn"]).optional(),
            "hiddenValues": t.array(t.string()).optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
        }
    ).named(renames["FilterCriteriaIn"])
    types["FilterCriteriaOut"] = t.struct(
        {
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorOut"]).optional(),
            "hiddenValues": t.array(t.string()).optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterCriteriaOut"])
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
    types["BordersIn"] = t.struct(
        {
            "right": t.proxy(renames["BorderIn"]).optional(),
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "left": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["BordersIn"])
    types["BordersOut"] = t.struct(
        {
            "right": t.proxy(renames["BorderOut"]).optional(),
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "left": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BordersOut"])
    types["BaselineValueFormatIn"] = t.struct(
        {
            "positiveColor": t.proxy(renames["ColorIn"]).optional(),
            "comparisonType": t.string().optional(),
            "description": t.string().optional(),
            "position": t.proxy(renames["TextPositionIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "negativeColor": t.proxy(renames["ColorIn"]).optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BaselineValueFormatIn"])
    types["BaselineValueFormatOut"] = t.struct(
        {
            "positiveColor": t.proxy(renames["ColorOut"]).optional(),
            "comparisonType": t.string().optional(),
            "description": t.string().optional(),
            "position": t.proxy(renames["TextPositionOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "negativeColor": t.proxy(renames["ColorOut"]).optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BaselineValueFormatOut"])
    types["PivotGroupIn"] = t.struct(
        {
            "groupRule": t.proxy(renames["PivotGroupRuleIn"]).optional(),
            "label": t.string().optional(),
            "showTotals": t.boolean().optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitIn"]).optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataIn"])
            ).optional(),
            "sourceColumnOffset": t.integer().optional(),
            "sortOrder": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketIn"]).optional(),
            "repeatHeadings": t.boolean().optional(),
        }
    ).named(renames["PivotGroupIn"])
    types["PivotGroupOut"] = t.struct(
        {
            "groupRule": t.proxy(renames["PivotGroupRuleOut"]).optional(),
            "label": t.string().optional(),
            "showTotals": t.boolean().optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitOut"]).optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataOut"])
            ).optional(),
            "sourceColumnOffset": t.integer().optional(),
            "sortOrder": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketOut"]).optional(),
            "repeatHeadings": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupOut"])
    types["BatchClearValuesRequestIn"] = t.struct(
        {"ranges": t.array(t.string()).optional()}
    ).named(renames["BatchClearValuesRequestIn"])
    types["BatchClearValuesRequestOut"] = t.struct(
        {
            "ranges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesRequestOut"])
    types["DeleteConditionalFormatRuleResponseIn"] = t.struct(
        {"rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional()}
    ).named(renames["DeleteConditionalFormatRuleResponseIn"])
    types["DeleteConditionalFormatRuleResponseOut"] = t.struct(
        {
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConditionalFormatRuleResponseOut"])
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
    types["AddFilterViewRequestIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewRequestIn"])
    types["AddFilterViewRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewRequestOut"])
    types["TreemapChartColorScaleIn"] = t.struct(
        {
            "noDataColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "minValueColor": t.proxy(renames["ColorIn"]).optional(),
            "noDataColor": t.proxy(renames["ColorIn"]).optional(),
            "midValueColor": t.proxy(renames["ColorIn"]).optional(),
            "maxValueColor": t.proxy(renames["ColorIn"]).optional(),
            "minValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "maxValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleIn"])
    types["TreemapChartColorScaleOut"] = t.struct(
        {
            "noDataColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "minValueColor": t.proxy(renames["ColorOut"]).optional(),
            "noDataColor": t.proxy(renames["ColorOut"]).optional(),
            "midValueColor": t.proxy(renames["ColorOut"]).optional(),
            "maxValueColor": t.proxy(renames["ColorOut"]).optional(),
            "minValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "maxValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleOut"])
    types["SpreadsheetThemeIn"] = t.struct(
        {
            "themeColors": t.array(t.proxy(renames["ThemeColorPairIn"])).optional(),
            "primaryFontFamily": t.string().optional(),
        }
    ).named(renames["SpreadsheetThemeIn"])
    types["SpreadsheetThemeOut"] = t.struct(
        {
            "themeColors": t.array(t.proxy(renames["ThemeColorPairOut"])).optional(),
            "primaryFontFamily": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetThemeOut"])
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
    types["MoveDimensionRequestIn"] = t.struct(
        {
            "source": t.proxy(renames["DimensionRangeIn"]).optional(),
            "destinationIndex": t.integer().optional(),
        }
    ).named(renames["MoveDimensionRequestIn"])
    types["MoveDimensionRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["DimensionRangeOut"]).optional(),
            "destinationIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveDimensionRequestOut"])
    types["BatchUpdateSpreadsheetResponseIn"] = t.struct(
        {
            "updatedSpreadsheet": t.proxy(renames["SpreadsheetIn"]).optional(),
            "spreadsheetId": t.string().optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetResponseIn"])
    types["BatchUpdateSpreadsheetResponseOut"] = t.struct(
        {
            "updatedSpreadsheet": t.proxy(renames["SpreadsheetOut"]).optional(),
            "spreadsheetId": t.string().optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetResponseOut"])
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
    types["DeleteEmbeddedObjectRequestIn"] = t.struct(
        {"objectId": t.integer().optional()}
    ).named(renames["DeleteEmbeddedObjectRequestIn"])
    types["DeleteEmbeddedObjectRequestOut"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteEmbeddedObjectRequestOut"])
    types["BandedRangeIn"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "columnProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
            "rowProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
        }
    ).named(renames["BandedRangeIn"])
    types["BandedRangeOut"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "columnProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "rowProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandedRangeOut"])
    types["UpdateBordersRequestIn"] = t.struct(
        {
            "left": t.proxy(renames["BorderIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "right": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
            "innerVertical": t.proxy(renames["BorderIn"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["UpdateBordersRequestIn"])
    types["UpdateBordersRequestOut"] = t.struct(
        {
            "left": t.proxy(renames["BorderOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "right": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "innerVertical": t.proxy(renames["BorderOut"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBordersRequestOut"])
    types["PivotTableIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["PivotValueIn"])).optional(),
            "columns": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "dataSourceId": t.string().optional(),
            "valueLayout": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecIn"])).optional(),
            "rows": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PivotTableIn"])
    types["PivotTableOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["PivotValueOut"])).optional(),
            "columns": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "dataSourceId": t.string().optional(),
            "valueLayout": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecOut"])).optional(),
            "rows": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotTableOut"])
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
    types["RefreshDataSourceObjectExecutionStatusIn"] = t.struct(
        {
            "reference": t.proxy(renames["DataSourceObjectReferenceIn"]).optional(),
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
        }
    ).named(renames["RefreshDataSourceObjectExecutionStatusIn"])
    types["RefreshDataSourceObjectExecutionStatusOut"] = t.struct(
        {
            "reference": t.proxy(renames["DataSourceObjectReferenceOut"]).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshDataSourceObjectExecutionStatusOut"])
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
    types["DataSourceTableIn"] = t.struct(
        {
            "rowLimit": t.integer().optional(),
            "columnSelectionType": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceIn"])
            ).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
        }
    ).named(renames["DataSourceTableIn"])
    types["DataSourceTableOut"] = t.struct(
        {
            "rowLimit": t.integer().optional(),
            "columnSelectionType": t.string().optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "dataSourceId": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceOut"])
            ).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceTableOut"])
    types["DeleteDataSourceRequestIn"] = t.struct(
        {"dataSourceId": t.string().optional()}
    ).named(renames["DeleteDataSourceRequestIn"])
    types["DeleteDataSourceRequestOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDataSourceRequestOut"])
    types["ChartDataIn"] = t.struct(
        {
            "aggregateType": t.string().optional(),
            "sourceRange": t.proxy(renames["ChartSourceRangeIn"]).optional(),
            "groupRule": t.proxy(renames["ChartGroupRuleIn"]).optional(),
            "columnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
        }
    ).named(renames["ChartDataIn"])
    types["ChartDataOut"] = t.struct(
        {
            "aggregateType": t.string().optional(),
            "sourceRange": t.proxy(renames["ChartSourceRangeOut"]).optional(),
            "groupRule": t.proxy(renames["ChartGroupRuleOut"]).optional(),
            "columnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDataOut"])
    types["SlicerIn"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "slicerId": t.integer().optional(),
            "spec": t.proxy(renames["SlicerSpecIn"]).optional(),
        }
    ).named(renames["SlicerIn"])
    types["SlicerOut"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "slicerId": t.integer().optional(),
            "spec": t.proxy(renames["SlicerSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerOut"])
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
    types["InsertRangeRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "shiftDimension": t.string().optional(),
        }
    ).named(renames["InsertRangeRequestIn"])
    types["InsertRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "shiftDimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertRangeRequestOut"])
    types["RepeatCellRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "cell": t.proxy(renames["CellDataIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["RepeatCellRequestIn"])
    types["RepeatCellRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "cell": t.proxy(renames["CellDataOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepeatCellRequestOut"])
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
    types["DeleteFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DeleteFilterViewRequestIn"])
    types["DeleteFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFilterViewRequestOut"])
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
    types["WaterfallChartSpecIn"] = t.struct(
        {
            "domain": t.proxy(renames["WaterfallChartDomainIn"]).optional(),
            "firstValueIsTotal": t.boolean().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "stackedType": t.string().optional(),
            "hideConnectorLines": t.boolean().optional(),
            "connectorLineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "series": t.array(t.proxy(renames["WaterfallChartSeriesIn"])).optional(),
        }
    ).named(renames["WaterfallChartSpecIn"])
    types["WaterfallChartSpecOut"] = t.struct(
        {
            "domain": t.proxy(renames["WaterfallChartDomainOut"]).optional(),
            "firstValueIsTotal": t.boolean().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "stackedType": t.string().optional(),
            "hideConnectorLines": t.boolean().optional(),
            "connectorLineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "series": t.array(t.proxy(renames["WaterfallChartSeriesOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSpecOut"])
    types["TrimWhitespaceRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["TrimWhitespaceRequestIn"])
    types["TrimWhitespaceRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceRequestOut"])
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
    types["DimensionGroupIn"] = t.struct(
        {
            "depth": t.integer().optional(),
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
            "collapsed": t.boolean().optional(),
        }
    ).named(renames["DimensionGroupIn"])
    types["DimensionGroupOut"] = t.struct(
        {
            "depth": t.integer().optional(),
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "collapsed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionGroupOut"])
    types["DataSourceSheetDimensionRangeIn"] = t.struct(
        {
            "columnReferences": t.array(
                t.proxy(renames["DataSourceColumnReferenceIn"])
            ).optional(),
            "sheetId": t.integer().optional(),
        }
    ).named(renames["DataSourceSheetDimensionRangeIn"])
    types["DataSourceSheetDimensionRangeOut"] = t.struct(
        {
            "columnReferences": t.array(
                t.proxy(renames["DataSourceColumnReferenceOut"])
            ).optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSheetDimensionRangeOut"])
    types["UpdateDimensionGroupRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "dimensionGroup": t.proxy(renames["DimensionGroupIn"]).optional(),
        }
    ).named(renames["UpdateDimensionGroupRequestIn"])
    types["UpdateDimensionGroupRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "dimensionGroup": t.proxy(renames["DimensionGroupOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDimensionGroupRequestOut"])
    types["ChartHistogramRuleIn"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "intervalSize": t.number().optional(),
            "minValue": t.number().optional(),
        }
    ).named(renames["ChartHistogramRuleIn"])
    types["ChartHistogramRuleOut"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "intervalSize": t.number().optional(),
            "minValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartHistogramRuleOut"])
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
    types["GridPropertiesIn"] = t.struct(
        {
            "frozenColumnCount": t.integer().optional(),
            "columnCount": t.integer().optional(),
            "frozenRowCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "rowGroupControlAfter": t.boolean().optional(),
            "hideGridlines": t.boolean().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
        }
    ).named(renames["GridPropertiesIn"])
    types["GridPropertiesOut"] = t.struct(
        {
            "frozenColumnCount": t.integer().optional(),
            "columnCount": t.integer().optional(),
            "frozenRowCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "rowGroupControlAfter": t.boolean().optional(),
            "hideGridlines": t.boolean().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridPropertiesOut"])
    types["BatchUpdateValuesByDataFilterRequestIn"] = t.struct(
        {
            "data": t.array(t.proxy(renames["DataFilterValueRangeIn"])).optional(),
            "responseValueRenderOption": t.string().optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "valueInputOption": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestIn"])
    types["BatchUpdateValuesByDataFilterRequestOut"] = t.struct(
        {
            "data": t.array(t.proxy(renames["DataFilterValueRangeOut"])).optional(),
            "responseValueRenderOption": t.string().optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "valueInputOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestOut"])
    types["AddDataSourceRequestIn"] = t.struct(
        {"dataSource": t.proxy(renames["DataSourceIn"]).optional()}
    ).named(renames["AddDataSourceRequestIn"])
    types["AddDataSourceRequestOut"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDataSourceRequestOut"])
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
    types["RowDataIn"] = t.struct(
        {"values": t.array(t.proxy(renames["CellDataIn"])).optional()}
    ).named(renames["RowDataIn"])
    types["RowDataOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CellDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowDataOut"])
    types["CreateDeveloperMetadataResponseIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataResponseIn"])
    types["CreateDeveloperMetadataResponseOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataResponseOut"])
    types["SheetPropertiesIn"] = t.struct(
        {
            "sheetType": t.string().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesIn"]).optional(),
            "index": t.integer().optional(),
            "hidden": t.boolean().optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "sheetId": t.integer().optional(),
            "rightToLeft": t.boolean().optional(),
            "title": t.string().optional(),
            "tabColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["SheetPropertiesIn"])
    types["SheetPropertiesOut"] = t.struct(
        {
            "dataSourceSheetProperties": t.proxy(
                renames["DataSourceSheetPropertiesOut"]
            ).optional(),
            "sheetType": t.string().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesOut"]).optional(),
            "index": t.integer().optional(),
            "hidden": t.boolean().optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "sheetId": t.integer().optional(),
            "rightToLeft": t.boolean().optional(),
            "title": t.string().optional(),
            "tabColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetPropertiesOut"])
    types["PaddingIn"] = t.struct(
        {
            "right": t.integer().optional(),
            "bottom": t.integer().optional(),
            "left": t.integer().optional(),
            "top": t.integer().optional(),
        }
    ).named(renames["PaddingIn"])
    types["PaddingOut"] = t.struct(
        {
            "right": t.integer().optional(),
            "bottom": t.integer().optional(),
            "left": t.integer().optional(),
            "top": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaddingOut"])
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
    types["InterpolationPointIn"] = t.struct(
        {
            "value": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "type": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["InterpolationPointIn"])
    types["InterpolationPointOut"] = t.struct(
        {
            "value": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "type": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InterpolationPointOut"])
    types["DataValidationRuleIn"] = t.struct(
        {
            "showCustomUi": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "inputMessage": t.string().optional(),
            "strict": t.boolean().optional(),
        }
    ).named(renames["DataValidationRuleIn"])
    types["DataValidationRuleOut"] = t.struct(
        {
            "showCustomUi": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "inputMessage": t.string().optional(),
            "strict": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataValidationRuleOut"])
    types["NamedRangeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["NamedRangeIn"])
    types["NamedRangeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "namedRangeId": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedRangeOut"])
    types["DataSourceRefreshScheduleIn"] = t.struct(
        {
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleIn"]
            ).optional(),
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleIn"]
            ).optional(),
            "refreshScope": t.string().optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleIn"]
            ).optional(),
            "enabled": t.boolean().optional(),
        }
    ).named(renames["DataSourceRefreshScheduleIn"])
    types["DataSourceRefreshScheduleOut"] = t.struct(
        {
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleOut"]
            ).optional(),
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleOut"]
            ).optional(),
            "refreshScope": t.string().optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleOut"]
            ).optional(),
            "nextRun": t.proxy(renames["IntervalOut"]).optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshScheduleOut"])
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
    types["PivotGroupRuleIn"] = t.struct(
        {
            "histogramRule": t.proxy(renames["HistogramRuleIn"]).optional(),
            "dateTimeRule": t.proxy(renames["DateTimeRuleIn"]).optional(),
            "manualRule": t.proxy(renames["ManualRuleIn"]).optional(),
        }
    ).named(renames["PivotGroupRuleIn"])
    types["PivotGroupRuleOut"] = t.struct(
        {
            "histogramRule": t.proxy(renames["HistogramRuleOut"]).optional(),
            "dateTimeRule": t.proxy(renames["DateTimeRuleOut"]).optional(),
            "manualRule": t.proxy(renames["ManualRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupRuleOut"])
    types["BasicChartAxisIn"] = t.struct(
        {
            "title": t.string().optional(),
            "position": t.string().optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsIn"]
            ).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "format": t.proxy(renames["TextFormatIn"]).optional(),
        }
    ).named(renames["BasicChartAxisIn"])
    types["BasicChartAxisOut"] = t.struct(
        {
            "title": t.string().optional(),
            "position": t.string().optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsOut"]
            ).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "format": t.proxy(renames["TextFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartAxisOut"])
    types["TrimWhitespaceResponseIn"] = t.struct(
        {"cellsChangedCount": t.integer().optional()}
    ).named(renames["TrimWhitespaceResponseIn"])
    types["TrimWhitespaceResponseOut"] = t.struct(
        {
            "cellsChangedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceResponseOut"])
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
    types["PieChartSpecIn"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
            "legendPosition": t.string().optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "threeDimensional": t.boolean().optional(),
            "pieHole": t.number().optional(),
        }
    ).named(renames["PieChartSpecIn"])
    types["PieChartSpecOut"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "legendPosition": t.string().optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "threeDimensional": t.boolean().optional(),
            "pieHole": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PieChartSpecOut"])
    types["GridCoordinateIn"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
        }
    ).named(renames["GridCoordinateIn"])
    types["GridCoordinateOut"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "columnIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridCoordinateOut"])
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
    types["BatchUpdateSpreadsheetRequestIn"] = t.struct(
        {
            "responseIncludeGridData": t.boolean().optional(),
            "responseRanges": t.array(t.string()).optional(),
            "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
            "includeSpreadsheetInResponse": t.boolean().optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetRequestIn"])
    types["BatchUpdateSpreadsheetRequestOut"] = t.struct(
        {
            "responseIncludeGridData": t.boolean().optional(),
            "responseRanges": t.array(t.string()).optional(),
            "requests": t.array(t.proxy(renames["RequestOut"])).optional(),
            "includeSpreadsheetInResponse": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetRequestOut"])
    types["DeleteDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionGroupRequestIn"])
    types["DeleteDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionGroupRequestOut"])
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
    types["UpdateCellsRequestIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "start": t.proxy(renames["GridCoordinateIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateCellsRequestIn"])
    types["UpdateCellsRequestOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "start": t.proxy(renames["GridCoordinateOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCellsRequestOut"])
    types["DeleteConditionalFormatRuleRequestIn"] = t.struct(
        {"index": t.integer().optional(), "sheetId": t.integer().optional()}
    ).named(renames["DeleteConditionalFormatRuleRequestIn"])
    types["DeleteConditionalFormatRuleRequestOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConditionalFormatRuleRequestOut"])
    types["BigQueryDataSourceSpecIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "querySpec": t.proxy(renames["BigQueryQuerySpecIn"]).optional(),
            "tableSpec": t.proxy(renames["BigQueryTableSpecIn"]).optional(),
        }
    ).named(renames["BigQueryDataSourceSpecIn"])
    types["BigQueryDataSourceSpecOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "querySpec": t.proxy(renames["BigQueryQuerySpecOut"]).optional(),
            "tableSpec": t.proxy(renames["BigQueryTableSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDataSourceSpecOut"])
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
    types["EmbeddedObjectPositionIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "newSheet": t.boolean().optional(),
            "overlayPosition": t.proxy(renames["OverlayPositionIn"]).optional(),
        }
    ).named(renames["EmbeddedObjectPositionIn"])
    types["EmbeddedObjectPositionOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "newSheet": t.boolean().optional(),
            "overlayPosition": t.proxy(renames["OverlayPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectPositionOut"])
    types["UpdateEmbeddedObjectPositionResponseIn"] = t.struct(
        {"position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional()}
    ).named(renames["UpdateEmbeddedObjectPositionResponseIn"])
    types["UpdateEmbeddedObjectPositionResponseOut"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionResponseOut"])
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
    types["SearchDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["SearchDeveloperMetadataRequestIn"])
    types["SearchDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDeveloperMetadataRequestOut"])
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
    types["WaterfallChartSeriesIn"] = t.struct(
        {
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "customSubtotals": t.array(
                t.proxy(renames["WaterfallChartCustomSubtotalIn"])
            ).optional(),
            "data": t.proxy(renames["ChartDataIn"]).optional(),
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "subtotalColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "positiveColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "hideTrailingSubtotal": t.boolean().optional(),
        }
    ).named(renames["WaterfallChartSeriesIn"])
    types["WaterfallChartSeriesOut"] = t.struct(
        {
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "customSubtotals": t.array(
                t.proxy(renames["WaterfallChartCustomSubtotalOut"])
            ).optional(),
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "subtotalColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "positiveColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "hideTrailingSubtotal": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSeriesOut"])
    types["DeleteNamedRangeRequestIn"] = t.struct(
        {"namedRangeId": t.string().optional()}
    ).named(renames["DeleteNamedRangeRequestIn"])
    types["DeleteNamedRangeRequestOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteNamedRangeRequestOut"])
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
    types["ValueRangeIn"] = t.struct(
        {
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "range": t.string().optional(),
            "majorDimension": t.string().optional(),
        }
    ).named(renames["ValueRangeIn"])
    types["ValueRangeOut"] = t.struct(
        {
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "range": t.string().optional(),
            "majorDimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueRangeOut"])
    types["CellDataIn"] = t.struct(
        {
            "dataValidation": t.proxy(renames["DataValidationRuleIn"]).optional(),
            "hyperlink": t.string().optional(),
            "formattedValue": t.string().optional(),
            "note": t.string().optional(),
            "userEnteredValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableIn"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableIn"]).optional(),
            "effectiveValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "effectiveFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunIn"])).optional(),
        }
    ).named(renames["CellDataIn"])
    types["CellDataOut"] = t.struct(
        {
            "dataValidation": t.proxy(renames["DataValidationRuleOut"]).optional(),
            "hyperlink": t.string().optional(),
            "formattedValue": t.string().optional(),
            "note": t.string().optional(),
            "userEnteredValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableOut"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableOut"]).optional(),
            "effectiveValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "effectiveFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunOut"])).optional(),
            "dataSourceFormula": t.proxy(renames["DataSourceFormulaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellDataOut"])
    types["DeleteDuplicatesResponseIn"] = t.struct(
        {"duplicatesRemovedCount": t.integer().optional()}
    ).named(renames["DeleteDuplicatesResponseIn"])
    types["DeleteDuplicatesResponseOut"] = t.struct(
        {
            "duplicatesRemovedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDuplicatesResponseOut"])
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
    types["CreateDeveloperMetadataRequestIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataRequestIn"])
    types["CreateDeveloperMetadataRequestOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataRequestOut"])
    types["DateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DateTimeRuleIn"]
    )
    types["DateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeRuleOut"])
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
    types["BigQueryQuerySpecIn"] = t.struct({"rawQuery": t.string().optional()}).named(
        renames["BigQueryQuerySpecIn"]
    )
    types["BigQueryQuerySpecOut"] = t.struct(
        {
            "rawQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryQuerySpecOut"])
    types["AddBandingResponseIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingResponseIn"])
    types["AddBandingResponseOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingResponseOut"])
    types["DeleteProtectedRangeRequestIn"] = t.struct(
        {"protectedRangeId": t.integer().optional()}
    ).named(renames["DeleteProtectedRangeRequestIn"])
    types["DeleteProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteProtectedRangeRequestOut"])
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
    types["ConditionalFormatRuleIn"] = t.struct(
        {
            "ranges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "booleanRule": t.proxy(renames["BooleanRuleIn"]).optional(),
            "gradientRule": t.proxy(renames["GradientRuleIn"]).optional(),
        }
    ).named(renames["ConditionalFormatRuleIn"])
    types["ConditionalFormatRuleOut"] = t.struct(
        {
            "ranges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "booleanRule": t.proxy(renames["BooleanRuleOut"]).optional(),
            "gradientRule": t.proxy(renames["GradientRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionalFormatRuleOut"])

    functions = {}
    functions["spreadsheetsCreate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseIncludeGridData": t.boolean().optional(),
                "responseRanges": t.array(t.string()).optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
                "includeSpreadsheetInResponse": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateSpreadsheetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseIncludeGridData": t.boolean().optional(),
                "responseRanges": t.array(t.string()).optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
                "includeSpreadsheetInResponse": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateSpreadsheetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsGetByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseIncludeGridData": t.boolean().optional(),
                "responseRanges": t.array(t.string()).optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
                "includeSpreadsheetInResponse": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateSpreadsheetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsBatchUpdate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseIncludeGridData": t.boolean().optional(),
                "responseRanges": t.array(t.string()).optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
                "includeSpreadsheetInResponse": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateSpreadsheetResponseOut"]),
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
    functions["spreadsheetsValuesUpdate"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesAppend"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesClear"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchUpdateByDataFilter"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchGetByDataFilter"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchClearByDataFilter"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchUpdate"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchClear"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesGet"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchGet"] = sheets.get(
        "v4/spreadsheets/{spreadsheetId}/values:batchGet",
        t.struct(
            {
                "valueRenderOption": t.string().optional(),
                "spreadsheetId": t.string().optional(),
                "dateTimeRenderOption": t.string().optional(),
                "majorDimension": t.string().optional(),
                "ranges": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetValuesResponseOut"]),
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

    return Import(
        importer="sheets", renames=renames, types=Box(types), functions=Box(functions)
    )
