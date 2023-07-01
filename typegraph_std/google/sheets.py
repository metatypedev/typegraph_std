from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_sheets():
    sheets = HTTPRuntime("https://sheets.googleapis.com/")

    renames = {
        "ErrorResponse": "_sheets_1_ErrorResponse",
        "PivotGroupValueMetadataIn": "_sheets_2_PivotGroupValueMetadataIn",
        "PivotGroupValueMetadataOut": "_sheets_3_PivotGroupValueMetadataOut",
        "AddDataSourceRequestIn": "_sheets_4_AddDataSourceRequestIn",
        "AddDataSourceRequestOut": "_sheets_5_AddDataSourceRequestOut",
        "ValueRangeIn": "_sheets_6_ValueRangeIn",
        "ValueRangeOut": "_sheets_7_ValueRangeOut",
        "PivotGroupSortValueBucketIn": "_sheets_8_PivotGroupSortValueBucketIn",
        "PivotGroupSortValueBucketOut": "_sheets_9_PivotGroupSortValueBucketOut",
        "AutoResizeDimensionsRequestIn": "_sheets_10_AutoResizeDimensionsRequestIn",
        "AutoResizeDimensionsRequestOut": "_sheets_11_AutoResizeDimensionsRequestOut",
        "InsertRangeRequestIn": "_sheets_12_InsertRangeRequestIn",
        "InsertRangeRequestOut": "_sheets_13_InsertRangeRequestOut",
        "DataSourceSheetPropertiesIn": "_sheets_14_DataSourceSheetPropertiesIn",
        "DataSourceSheetPropertiesOut": "_sheets_15_DataSourceSheetPropertiesOut",
        "ResponseIn": "_sheets_16_ResponseIn",
        "ResponseOut": "_sheets_17_ResponseOut",
        "TextFormatIn": "_sheets_18_TextFormatIn",
        "TextFormatOut": "_sheets_19_TextFormatOut",
        "BigQueryQuerySpecIn": "_sheets_20_BigQueryQuerySpecIn",
        "BigQueryQuerySpecOut": "_sheets_21_BigQueryQuerySpecOut",
        "PivotGroupLimitIn": "_sheets_22_PivotGroupLimitIn",
        "PivotGroupLimitOut": "_sheets_23_PivotGroupLimitOut",
        "DataSourceRefreshMonthlyScheduleIn": "_sheets_24_DataSourceRefreshMonthlyScheduleIn",
        "DataSourceRefreshMonthlyScheduleOut": "_sheets_25_DataSourceRefreshMonthlyScheduleOut",
        "UpdateValuesByDataFilterResponseIn": "_sheets_26_UpdateValuesByDataFilterResponseIn",
        "UpdateValuesByDataFilterResponseOut": "_sheets_27_UpdateValuesByDataFilterResponseOut",
        "AddFilterViewRequestIn": "_sheets_28_AddFilterViewRequestIn",
        "AddFilterViewRequestOut": "_sheets_29_AddFilterViewRequestOut",
        "ChartCustomNumberFormatOptionsIn": "_sheets_30_ChartCustomNumberFormatOptionsIn",
        "ChartCustomNumberFormatOptionsOut": "_sheets_31_ChartCustomNumberFormatOptionsOut",
        "InsertDimensionRequestIn": "_sheets_32_InsertDimensionRequestIn",
        "InsertDimensionRequestOut": "_sheets_33_InsertDimensionRequestOut",
        "DeleteSheetRequestIn": "_sheets_34_DeleteSheetRequestIn",
        "DeleteSheetRequestOut": "_sheets_35_DeleteSheetRequestOut",
        "UpdateFilterViewRequestIn": "_sheets_36_UpdateFilterViewRequestIn",
        "UpdateFilterViewRequestOut": "_sheets_37_UpdateFilterViewRequestOut",
        "TextPositionIn": "_sheets_38_TextPositionIn",
        "TextPositionOut": "_sheets_39_TextPositionOut",
        "UpdateBordersRequestIn": "_sheets_40_UpdateBordersRequestIn",
        "UpdateBordersRequestOut": "_sheets_41_UpdateBordersRequestOut",
        "ProtectedRangeIn": "_sheets_42_ProtectedRangeIn",
        "ProtectedRangeOut": "_sheets_43_ProtectedRangeOut",
        "KeyValueFormatIn": "_sheets_44_KeyValueFormatIn",
        "KeyValueFormatOut": "_sheets_45_KeyValueFormatOut",
        "UpdateSheetPropertiesRequestIn": "_sheets_46_UpdateSheetPropertiesRequestIn",
        "UpdateSheetPropertiesRequestOut": "_sheets_47_UpdateSheetPropertiesRequestOut",
        "AddSheetResponseIn": "_sheets_48_AddSheetResponseIn",
        "AddSheetResponseOut": "_sheets_49_AddSheetResponseOut",
        "WaterfallChartColumnStyleIn": "_sheets_50_WaterfallChartColumnStyleIn",
        "WaterfallChartColumnStyleOut": "_sheets_51_WaterfallChartColumnStyleOut",
        "ClearValuesResponseIn": "_sheets_52_ClearValuesResponseIn",
        "ClearValuesResponseOut": "_sheets_53_ClearValuesResponseOut",
        "SetBasicFilterRequestIn": "_sheets_54_SetBasicFilterRequestIn",
        "SetBasicFilterRequestOut": "_sheets_55_SetBasicFilterRequestOut",
        "DeleteNamedRangeRequestIn": "_sheets_56_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_sheets_57_DeleteNamedRangeRequestOut",
        "DeleteConditionalFormatRuleResponseIn": "_sheets_58_DeleteConditionalFormatRuleResponseIn",
        "DeleteConditionalFormatRuleResponseOut": "_sheets_59_DeleteConditionalFormatRuleResponseOut",
        "DataSourceIn": "_sheets_60_DataSourceIn",
        "DataSourceOut": "_sheets_61_DataSourceOut",
        "CopySheetToAnotherSpreadsheetRequestIn": "_sheets_62_CopySheetToAnotherSpreadsheetRequestIn",
        "CopySheetToAnotherSpreadsheetRequestOut": "_sheets_63_CopySheetToAnotherSpreadsheetRequestOut",
        "DeleteDuplicatesResponseIn": "_sheets_64_DeleteDuplicatesResponseIn",
        "DeleteDuplicatesResponseOut": "_sheets_65_DeleteDuplicatesResponseOut",
        "UpdateDataSourceRequestIn": "_sheets_66_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_sheets_67_UpdateDataSourceRequestOut",
        "DeveloperMetadataLocationIn": "_sheets_68_DeveloperMetadataLocationIn",
        "DeveloperMetadataLocationOut": "_sheets_69_DeveloperMetadataLocationOut",
        "ThemeColorPairIn": "_sheets_70_ThemeColorPairIn",
        "ThemeColorPairOut": "_sheets_71_ThemeColorPairOut",
        "DataSourceSheetDimensionRangeIn": "_sheets_72_DataSourceSheetDimensionRangeIn",
        "DataSourceSheetDimensionRangeOut": "_sheets_73_DataSourceSheetDimensionRangeOut",
        "BatchUpdateSpreadsheetRequestIn": "_sheets_74_BatchUpdateSpreadsheetRequestIn",
        "BatchUpdateSpreadsheetRequestOut": "_sheets_75_BatchUpdateSpreadsheetRequestOut",
        "AddSheetRequestIn": "_sheets_76_AddSheetRequestIn",
        "AddSheetRequestOut": "_sheets_77_AddSheetRequestOut",
        "OverlayPositionIn": "_sheets_78_OverlayPositionIn",
        "OverlayPositionOut": "_sheets_79_OverlayPositionOut",
        "UpdateDeveloperMetadataRequestIn": "_sheets_80_UpdateDeveloperMetadataRequestIn",
        "UpdateDeveloperMetadataRequestOut": "_sheets_81_UpdateDeveloperMetadataRequestOut",
        "BorderIn": "_sheets_82_BorderIn",
        "BorderOut": "_sheets_83_BorderOut",
        "AddFilterViewResponseIn": "_sheets_84_AddFilterViewResponseIn",
        "AddFilterViewResponseOut": "_sheets_85_AddFilterViewResponseOut",
        "BatchUpdateSpreadsheetResponseIn": "_sheets_86_BatchUpdateSpreadsheetResponseIn",
        "BatchUpdateSpreadsheetResponseOut": "_sheets_87_BatchUpdateSpreadsheetResponseOut",
        "SourceAndDestinationIn": "_sheets_88_SourceAndDestinationIn",
        "SourceAndDestinationOut": "_sheets_89_SourceAndDestinationOut",
        "BatchGetValuesResponseIn": "_sheets_90_BatchGetValuesResponseIn",
        "BatchGetValuesResponseOut": "_sheets_91_BatchGetValuesResponseOut",
        "DeleteBandingRequestIn": "_sheets_92_DeleteBandingRequestIn",
        "DeleteBandingRequestOut": "_sheets_93_DeleteBandingRequestOut",
        "UpdateConditionalFormatRuleRequestIn": "_sheets_94_UpdateConditionalFormatRuleRequestIn",
        "UpdateConditionalFormatRuleRequestOut": "_sheets_95_UpdateConditionalFormatRuleRequestOut",
        "NumberFormatIn": "_sheets_96_NumberFormatIn",
        "NumberFormatOut": "_sheets_97_NumberFormatOut",
        "UpdateConditionalFormatRuleResponseIn": "_sheets_98_UpdateConditionalFormatRuleResponseIn",
        "UpdateConditionalFormatRuleResponseOut": "_sheets_99_UpdateConditionalFormatRuleResponseOut",
        "DataLabelIn": "_sheets_100_DataLabelIn",
        "DataLabelOut": "_sheets_101_DataLabelOut",
        "PaddingIn": "_sheets_102_PaddingIn",
        "PaddingOut": "_sheets_103_PaddingOut",
        "AddDataSourceResponseIn": "_sheets_104_AddDataSourceResponseIn",
        "AddDataSourceResponseOut": "_sheets_105_AddDataSourceResponseOut",
        "DataExecutionStatusIn": "_sheets_106_DataExecutionStatusIn",
        "DataExecutionStatusOut": "_sheets_107_DataExecutionStatusOut",
        "RandomizeRangeRequestIn": "_sheets_108_RandomizeRangeRequestIn",
        "RandomizeRangeRequestOut": "_sheets_109_RandomizeRangeRequestOut",
        "AppendValuesResponseIn": "_sheets_110_AppendValuesResponseIn",
        "AppendValuesResponseOut": "_sheets_111_AppendValuesResponseOut",
        "DeleteDataSourceRequestIn": "_sheets_112_DeleteDataSourceRequestIn",
        "DeleteDataSourceRequestOut": "_sheets_113_DeleteDataSourceRequestOut",
        "BatchGetValuesByDataFilterRequestIn": "_sheets_114_BatchGetValuesByDataFilterRequestIn",
        "BatchGetValuesByDataFilterRequestOut": "_sheets_115_BatchGetValuesByDataFilterRequestOut",
        "BatchClearValuesResponseIn": "_sheets_116_BatchClearValuesResponseIn",
        "BatchClearValuesResponseOut": "_sheets_117_BatchClearValuesResponseOut",
        "AddConditionalFormatRuleRequestIn": "_sheets_118_AddConditionalFormatRuleRequestIn",
        "AddConditionalFormatRuleRequestOut": "_sheets_119_AddConditionalFormatRuleRequestOut",
        "CreateDeveloperMetadataResponseIn": "_sheets_120_CreateDeveloperMetadataResponseIn",
        "CreateDeveloperMetadataResponseOut": "_sheets_121_CreateDeveloperMetadataResponseOut",
        "DeleteDimensionRequestIn": "_sheets_122_DeleteDimensionRequestIn",
        "DeleteDimensionRequestOut": "_sheets_123_DeleteDimensionRequestOut",
        "AddChartRequestIn": "_sheets_124_AddChartRequestIn",
        "AddChartRequestOut": "_sheets_125_AddChartRequestOut",
        "ErrorValueIn": "_sheets_126_ErrorValueIn",
        "ErrorValueOut": "_sheets_127_ErrorValueOut",
        "TreemapChartColorScaleIn": "_sheets_128_TreemapChartColorScaleIn",
        "TreemapChartColorScaleOut": "_sheets_129_TreemapChartColorScaleOut",
        "WaterfallChartSeriesIn": "_sheets_130_WaterfallChartSeriesIn",
        "WaterfallChartSeriesOut": "_sheets_131_WaterfallChartSeriesOut",
        "DataSourceObjectReferencesIn": "_sheets_132_DataSourceObjectReferencesIn",
        "DataSourceObjectReferencesOut": "_sheets_133_DataSourceObjectReferencesOut",
        "SpreadsheetIn": "_sheets_134_SpreadsheetIn",
        "SpreadsheetOut": "_sheets_135_SpreadsheetOut",
        "HistogramSeriesIn": "_sheets_136_HistogramSeriesIn",
        "HistogramSeriesOut": "_sheets_137_HistogramSeriesOut",
        "DeveloperMetadataLookupIn": "_sheets_138_DeveloperMetadataLookupIn",
        "DeveloperMetadataLookupOut": "_sheets_139_DeveloperMetadataLookupOut",
        "PivotValueIn": "_sheets_140_PivotValueIn",
        "PivotValueOut": "_sheets_141_PivotValueOut",
        "ColorIn": "_sheets_142_ColorIn",
        "ColorOut": "_sheets_143_ColorOut",
        "BooleanConditionIn": "_sheets_144_BooleanConditionIn",
        "BooleanConditionOut": "_sheets_145_BooleanConditionOut",
        "DeleteDeveloperMetadataRequestIn": "_sheets_146_DeleteDeveloperMetadataRequestIn",
        "DeleteDeveloperMetadataRequestOut": "_sheets_147_DeleteDeveloperMetadataRequestOut",
        "DeleteRangeRequestIn": "_sheets_148_DeleteRangeRequestIn",
        "DeleteRangeRequestOut": "_sheets_149_DeleteRangeRequestOut",
        "ExtendedValueIn": "_sheets_150_ExtendedValueIn",
        "ExtendedValueOut": "_sheets_151_ExtendedValueOut",
        "PivotFilterSpecIn": "_sheets_152_PivotFilterSpecIn",
        "PivotFilterSpecOut": "_sheets_153_PivotFilterSpecOut",
        "UpdateEmbeddedObjectBorderRequestIn": "_sheets_154_UpdateEmbeddedObjectBorderRequestIn",
        "UpdateEmbeddedObjectBorderRequestOut": "_sheets_155_UpdateEmbeddedObjectBorderRequestOut",
        "ChartDataIn": "_sheets_156_ChartDataIn",
        "ChartDataOut": "_sheets_157_ChartDataOut",
        "UpdateProtectedRangeRequestIn": "_sheets_158_UpdateProtectedRangeRequestIn",
        "UpdateProtectedRangeRequestOut": "_sheets_159_UpdateProtectedRangeRequestOut",
        "SetDataValidationRequestIn": "_sheets_160_SetDataValidationRequestIn",
        "SetDataValidationRequestOut": "_sheets_161_SetDataValidationRequestOut",
        "AddNamedRangeResponseIn": "_sheets_162_AddNamedRangeResponseIn",
        "AddNamedRangeResponseOut": "_sheets_163_AddNamedRangeResponseOut",
        "BasicChartSpecIn": "_sheets_164_BasicChartSpecIn",
        "BasicChartSpecOut": "_sheets_165_BasicChartSpecOut",
        "ChartSpecIn": "_sheets_166_ChartSpecIn",
        "ChartSpecOut": "_sheets_167_ChartSpecOut",
        "RefreshDataSourceResponseIn": "_sheets_168_RefreshDataSourceResponseIn",
        "RefreshDataSourceResponseOut": "_sheets_169_RefreshDataSourceResponseOut",
        "TextRotationIn": "_sheets_170_TextRotationIn",
        "TextRotationOut": "_sheets_171_TextRotationOut",
        "ManualRuleIn": "_sheets_172_ManualRuleIn",
        "ManualRuleOut": "_sheets_173_ManualRuleOut",
        "ConditionalFormatRuleIn": "_sheets_174_ConditionalFormatRuleIn",
        "ConditionalFormatRuleOut": "_sheets_175_ConditionalFormatRuleOut",
        "SortSpecIn": "_sheets_176_SortSpecIn",
        "SortSpecOut": "_sheets_177_SortSpecOut",
        "DeleteDuplicatesRequestIn": "_sheets_178_DeleteDuplicatesRequestIn",
        "DeleteDuplicatesRequestOut": "_sheets_179_DeleteDuplicatesRequestOut",
        "AutoFillRequestIn": "_sheets_180_AutoFillRequestIn",
        "AutoFillRequestOut": "_sheets_181_AutoFillRequestOut",
        "PivotFilterCriteriaIn": "_sheets_182_PivotFilterCriteriaIn",
        "PivotFilterCriteriaOut": "_sheets_183_PivotFilterCriteriaOut",
        "CutPasteRequestIn": "_sheets_184_CutPasteRequestIn",
        "CutPasteRequestOut": "_sheets_185_CutPasteRequestOut",
        "UnmergeCellsRequestIn": "_sheets_186_UnmergeCellsRequestIn",
        "UnmergeCellsRequestOut": "_sheets_187_UnmergeCellsRequestOut",
        "DuplicateSheetResponseIn": "_sheets_188_DuplicateSheetResponseIn",
        "DuplicateSheetResponseOut": "_sheets_189_DuplicateSheetResponseOut",
        "TrimWhitespaceRequestIn": "_sheets_190_TrimWhitespaceRequestIn",
        "TrimWhitespaceRequestOut": "_sheets_191_TrimWhitespaceRequestOut",
        "TreemapChartSpecIn": "_sheets_192_TreemapChartSpecIn",
        "TreemapChartSpecOut": "_sheets_193_TreemapChartSpecOut",
        "PivotTableIn": "_sheets_194_PivotTableIn",
        "PivotTableOut": "_sheets_195_PivotTableOut",
        "MatchedValueRangeIn": "_sheets_196_MatchedValueRangeIn",
        "MatchedValueRangeOut": "_sheets_197_MatchedValueRangeOut",
        "CandlestickDomainIn": "_sheets_198_CandlestickDomainIn",
        "CandlestickDomainOut": "_sheets_199_CandlestickDomainOut",
        "FilterCriteriaIn": "_sheets_200_FilterCriteriaIn",
        "FilterCriteriaOut": "_sheets_201_FilterCriteriaOut",
        "BasicFilterIn": "_sheets_202_BasicFilterIn",
        "BasicFilterOut": "_sheets_203_BasicFilterOut",
        "RepeatCellRequestIn": "_sheets_204_RepeatCellRequestIn",
        "RepeatCellRequestOut": "_sheets_205_RepeatCellRequestOut",
        "MatchedDeveloperMetadataIn": "_sheets_206_MatchedDeveloperMetadataIn",
        "MatchedDeveloperMetadataOut": "_sheets_207_MatchedDeveloperMetadataOut",
        "AddChartResponseIn": "_sheets_208_AddChartResponseIn",
        "AddChartResponseOut": "_sheets_209_AddChartResponseOut",
        "SortRangeRequestIn": "_sheets_210_SortRangeRequestIn",
        "SortRangeRequestOut": "_sheets_211_SortRangeRequestOut",
        "BordersIn": "_sheets_212_BordersIn",
        "BordersOut": "_sheets_213_BordersOut",
        "EmbeddedObjectPositionIn": "_sheets_214_EmbeddedObjectPositionIn",
        "EmbeddedObjectPositionOut": "_sheets_215_EmbeddedObjectPositionOut",
        "SlicerIn": "_sheets_216_SlicerIn",
        "SlicerOut": "_sheets_217_SlicerOut",
        "DataSourceColumnIn": "_sheets_218_DataSourceColumnIn",
        "DataSourceColumnOut": "_sheets_219_DataSourceColumnOut",
        "DimensionPropertiesIn": "_sheets_220_DimensionPropertiesIn",
        "DimensionPropertiesOut": "_sheets_221_DimensionPropertiesOut",
        "BasicChartAxisIn": "_sheets_222_BasicChartAxisIn",
        "BasicChartAxisOut": "_sheets_223_BasicChartAxisOut",
        "WaterfallChartSpecIn": "_sheets_224_WaterfallChartSpecIn",
        "WaterfallChartSpecOut": "_sheets_225_WaterfallChartSpecOut",
        "HistogramRuleIn": "_sheets_226_HistogramRuleIn",
        "HistogramRuleOut": "_sheets_227_HistogramRuleOut",
        "UpdateSpreadsheetPropertiesRequestIn": "_sheets_228_UpdateSpreadsheetPropertiesRequestIn",
        "UpdateSpreadsheetPropertiesRequestOut": "_sheets_229_UpdateSpreadsheetPropertiesRequestOut",
        "AddBandingResponseIn": "_sheets_230_AddBandingResponseIn",
        "AddBandingResponseOut": "_sheets_231_AddBandingResponseOut",
        "AddSlicerResponseIn": "_sheets_232_AddSlicerResponseIn",
        "AddSlicerResponseOut": "_sheets_233_AddSlicerResponseOut",
        "BatchClearValuesByDataFilterResponseIn": "_sheets_234_BatchClearValuesByDataFilterResponseIn",
        "BatchClearValuesByDataFilterResponseOut": "_sheets_235_BatchClearValuesByDataFilterResponseOut",
        "DeleteEmbeddedObjectRequestIn": "_sheets_236_DeleteEmbeddedObjectRequestIn",
        "DeleteEmbeddedObjectRequestOut": "_sheets_237_DeleteEmbeddedObjectRequestOut",
        "DeleteConditionalFormatRuleRequestIn": "_sheets_238_DeleteConditionalFormatRuleRequestIn",
        "DeleteConditionalFormatRuleRequestOut": "_sheets_239_DeleteConditionalFormatRuleRequestOut",
        "WaterfallChartCustomSubtotalIn": "_sheets_240_WaterfallChartCustomSubtotalIn",
        "WaterfallChartCustomSubtotalOut": "_sheets_241_WaterfallChartCustomSubtotalOut",
        "DeleteFilterViewRequestIn": "_sheets_242_DeleteFilterViewRequestIn",
        "DeleteFilterViewRequestOut": "_sheets_243_DeleteFilterViewRequestOut",
        "TrimWhitespaceResponseIn": "_sheets_244_TrimWhitespaceResponseIn",
        "TrimWhitespaceResponseOut": "_sheets_245_TrimWhitespaceResponseOut",
        "DataSourceColumnReferenceIn": "_sheets_246_DataSourceColumnReferenceIn",
        "DataSourceColumnReferenceOut": "_sheets_247_DataSourceColumnReferenceOut",
        "GridDataIn": "_sheets_248_GridDataIn",
        "GridDataOut": "_sheets_249_GridDataOut",
        "DimensionGroupIn": "_sheets_250_DimensionGroupIn",
        "DimensionGroupOut": "_sheets_251_DimensionGroupOut",
        "UpdateEmbeddedObjectPositionResponseIn": "_sheets_252_UpdateEmbeddedObjectPositionResponseIn",
        "UpdateEmbeddedObjectPositionResponseOut": "_sheets_253_UpdateEmbeddedObjectPositionResponseOut",
        "TimeOfDayIn": "_sheets_254_TimeOfDayIn",
        "TimeOfDayOut": "_sheets_255_TimeOfDayOut",
        "DeveloperMetadataIn": "_sheets_256_DeveloperMetadataIn",
        "DeveloperMetadataOut": "_sheets_257_DeveloperMetadataOut",
        "DataSourceTableIn": "_sheets_258_DataSourceTableIn",
        "DataSourceTableOut": "_sheets_259_DataSourceTableOut",
        "ClearBasicFilterRequestIn": "_sheets_260_ClearBasicFilterRequestIn",
        "ClearBasicFilterRequestOut": "_sheets_261_ClearBasicFilterRequestOut",
        "BooleanRuleIn": "_sheets_262_BooleanRuleIn",
        "BooleanRuleOut": "_sheets_263_BooleanRuleOut",
        "EmbeddedObjectBorderIn": "_sheets_264_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_sheets_265_EmbeddedObjectBorderOut",
        "SlicerSpecIn": "_sheets_266_SlicerSpecIn",
        "SlicerSpecOut": "_sheets_267_SlicerSpecOut",
        "CandlestickSeriesIn": "_sheets_268_CandlestickSeriesIn",
        "CandlestickSeriesOut": "_sheets_269_CandlestickSeriesOut",
        "IterativeCalculationSettingsIn": "_sheets_270_IterativeCalculationSettingsIn",
        "IterativeCalculationSettingsOut": "_sheets_271_IterativeCalculationSettingsOut",
        "HistogramChartSpecIn": "_sheets_272_HistogramChartSpecIn",
        "HistogramChartSpecOut": "_sheets_273_HistogramChartSpecOut",
        "DataSourceParameterIn": "_sheets_274_DataSourceParameterIn",
        "DataSourceParameterOut": "_sheets_275_DataSourceParameterOut",
        "NamedRangeIn": "_sheets_276_NamedRangeIn",
        "NamedRangeOut": "_sheets_277_NamedRangeOut",
        "DataSourceRefreshScheduleIn": "_sheets_278_DataSourceRefreshScheduleIn",
        "DataSourceRefreshScheduleOut": "_sheets_279_DataSourceRefreshScheduleOut",
        "CreateDeveloperMetadataRequestIn": "_sheets_280_CreateDeveloperMetadataRequestIn",
        "CreateDeveloperMetadataRequestOut": "_sheets_281_CreateDeveloperMetadataRequestOut",
        "BatchGetValuesByDataFilterResponseIn": "_sheets_282_BatchGetValuesByDataFilterResponseIn",
        "BatchGetValuesByDataFilterResponseOut": "_sheets_283_BatchGetValuesByDataFilterResponseOut",
        "IntervalIn": "_sheets_284_IntervalIn",
        "IntervalOut": "_sheets_285_IntervalOut",
        "UpdateSlicerSpecRequestIn": "_sheets_286_UpdateSlicerSpecRequestIn",
        "UpdateSlicerSpecRequestOut": "_sheets_287_UpdateSlicerSpecRequestOut",
        "DataSourceFormulaIn": "_sheets_288_DataSourceFormulaIn",
        "DataSourceFormulaOut": "_sheets_289_DataSourceFormulaOut",
        "CopyPasteRequestIn": "_sheets_290_CopyPasteRequestIn",
        "CopyPasteRequestOut": "_sheets_291_CopyPasteRequestOut",
        "ChartSourceRangeIn": "_sheets_292_ChartSourceRangeIn",
        "ChartSourceRangeOut": "_sheets_293_ChartSourceRangeOut",
        "FilterViewIn": "_sheets_294_FilterViewIn",
        "FilterViewOut": "_sheets_295_FilterViewOut",
        "ManualRuleGroupIn": "_sheets_296_ManualRuleGroupIn",
        "ManualRuleGroupOut": "_sheets_297_ManualRuleGroupOut",
        "DeleteDeveloperMetadataResponseIn": "_sheets_298_DeleteDeveloperMetadataResponseIn",
        "DeleteDeveloperMetadataResponseOut": "_sheets_299_DeleteDeveloperMetadataResponseOut",
        "FindReplaceRequestIn": "_sheets_300_FindReplaceRequestIn",
        "FindReplaceRequestOut": "_sheets_301_FindReplaceRequestOut",
        "UpdateNamedRangeRequestIn": "_sheets_302_UpdateNamedRangeRequestIn",
        "UpdateNamedRangeRequestOut": "_sheets_303_UpdateNamedRangeRequestOut",
        "PasteDataRequestIn": "_sheets_304_PasteDataRequestIn",
        "PasteDataRequestOut": "_sheets_305_PasteDataRequestOut",
        "DeleteProtectedRangeRequestIn": "_sheets_306_DeleteProtectedRangeRequestIn",
        "DeleteProtectedRangeRequestOut": "_sheets_307_DeleteProtectedRangeRequestOut",
        "SearchDeveloperMetadataRequestIn": "_sheets_308_SearchDeveloperMetadataRequestIn",
        "SearchDeveloperMetadataRequestOut": "_sheets_309_SearchDeveloperMetadataRequestOut",
        "UpdateChartSpecRequestIn": "_sheets_310_UpdateChartSpecRequestIn",
        "UpdateChartSpecRequestOut": "_sheets_311_UpdateChartSpecRequestOut",
        "RefreshDataSourceObjectExecutionStatusIn": "_sheets_312_RefreshDataSourceObjectExecutionStatusIn",
        "RefreshDataSourceObjectExecutionStatusOut": "_sheets_313_RefreshDataSourceObjectExecutionStatusOut",
        "AddDimensionGroupRequestIn": "_sheets_314_AddDimensionGroupRequestIn",
        "AddDimensionGroupRequestOut": "_sheets_315_AddDimensionGroupRequestOut",
        "GridRangeIn": "_sheets_316_GridRangeIn",
        "GridRangeOut": "_sheets_317_GridRangeOut",
        "FindReplaceResponseIn": "_sheets_318_FindReplaceResponseIn",
        "FindReplaceResponseOut": "_sheets_319_FindReplaceResponseOut",
        "TextFormatRunIn": "_sheets_320_TextFormatRunIn",
        "TextFormatRunOut": "_sheets_321_TextFormatRunOut",
        "DateTimeRuleIn": "_sheets_322_DateTimeRuleIn",
        "DateTimeRuleOut": "_sheets_323_DateTimeRuleOut",
        "InterpolationPointIn": "_sheets_324_InterpolationPointIn",
        "InterpolationPointOut": "_sheets_325_InterpolationPointOut",
        "BubbleChartSpecIn": "_sheets_326_BubbleChartSpecIn",
        "BubbleChartSpecOut": "_sheets_327_BubbleChartSpecOut",
        "DuplicateSheetRequestIn": "_sheets_328_DuplicateSheetRequestIn",
        "DuplicateSheetRequestOut": "_sheets_329_DuplicateSheetRequestOut",
        "UpdateDataSourceResponseIn": "_sheets_330_UpdateDataSourceResponseIn",
        "UpdateDataSourceResponseOut": "_sheets_331_UpdateDataSourceResponseOut",
        "CellFormatIn": "_sheets_332_CellFormatIn",
        "CellFormatOut": "_sheets_333_CellFormatOut",
        "UpdateDeveloperMetadataResponseIn": "_sheets_334_UpdateDeveloperMetadataResponseIn",
        "UpdateDeveloperMetadataResponseOut": "_sheets_335_UpdateDeveloperMetadataResponseOut",
        "RequestIn": "_sheets_336_RequestIn",
        "RequestOut": "_sheets_337_RequestOut",
        "AddProtectedRangeRequestIn": "_sheets_338_AddProtectedRangeRequestIn",
        "AddProtectedRangeRequestOut": "_sheets_339_AddProtectedRangeRequestOut",
        "SheetIn": "_sheets_340_SheetIn",
        "SheetOut": "_sheets_341_SheetOut",
        "DimensionRangeIn": "_sheets_342_DimensionRangeIn",
        "DimensionRangeOut": "_sheets_343_DimensionRangeOut",
        "PivotGroupRuleIn": "_sheets_344_PivotGroupRuleIn",
        "PivotGroupRuleOut": "_sheets_345_PivotGroupRuleOut",
        "AppendCellsRequestIn": "_sheets_346_AppendCellsRequestIn",
        "AppendCellsRequestOut": "_sheets_347_AppendCellsRequestOut",
        "RowDataIn": "_sheets_348_RowDataIn",
        "RowDataOut": "_sheets_349_RowDataOut",
        "BandingPropertiesIn": "_sheets_350_BandingPropertiesIn",
        "BandingPropertiesOut": "_sheets_351_BandingPropertiesOut",
        "DataSourceSpecIn": "_sheets_352_DataSourceSpecIn",
        "DataSourceSpecOut": "_sheets_353_DataSourceSpecOut",
        "BasicChartSeriesIn": "_sheets_354_BasicChartSeriesIn",
        "BasicChartSeriesOut": "_sheets_355_BasicChartSeriesOut",
        "AddDimensionGroupResponseIn": "_sheets_356_AddDimensionGroupResponseIn",
        "AddDimensionGroupResponseOut": "_sheets_357_AddDimensionGroupResponseOut",
        "EditorsIn": "_sheets_358_EditorsIn",
        "EditorsOut": "_sheets_359_EditorsOut",
        "BigQueryTableSpecIn": "_sheets_360_BigQueryTableSpecIn",
        "BigQueryTableSpecOut": "_sheets_361_BigQueryTableSpecOut",
        "BatchUpdateValuesRequestIn": "_sheets_362_BatchUpdateValuesRequestIn",
        "BatchUpdateValuesRequestOut": "_sheets_363_BatchUpdateValuesRequestOut",
        "DataSourceChartPropertiesIn": "_sheets_364_DataSourceChartPropertiesIn",
        "DataSourceChartPropertiesOut": "_sheets_365_DataSourceChartPropertiesOut",
        "TextToColumnsRequestIn": "_sheets_366_TextToColumnsRequestIn",
        "TextToColumnsRequestOut": "_sheets_367_TextToColumnsRequestOut",
        "UpdateDimensionGroupRequestIn": "_sheets_368_UpdateDimensionGroupRequestIn",
        "UpdateDimensionGroupRequestOut": "_sheets_369_UpdateDimensionGroupRequestOut",
        "SpreadsheetPropertiesIn": "_sheets_370_SpreadsheetPropertiesIn",
        "SpreadsheetPropertiesOut": "_sheets_371_SpreadsheetPropertiesOut",
        "ChartAxisViewWindowOptionsIn": "_sheets_372_ChartAxisViewWindowOptionsIn",
        "ChartAxisViewWindowOptionsOut": "_sheets_373_ChartAxisViewWindowOptionsOut",
        "ScorecardChartSpecIn": "_sheets_374_ScorecardChartSpecIn",
        "ScorecardChartSpecOut": "_sheets_375_ScorecardChartSpecOut",
        "BigQueryDataSourceSpecIn": "_sheets_376_BigQueryDataSourceSpecIn",
        "BigQueryDataSourceSpecOut": "_sheets_377_BigQueryDataSourceSpecOut",
        "DataSourceRefreshDailyScheduleIn": "_sheets_378_DataSourceRefreshDailyScheduleIn",
        "DataSourceRefreshDailyScheduleOut": "_sheets_379_DataSourceRefreshDailyScheduleOut",
        "DataFilterValueRangeIn": "_sheets_380_DataFilterValueRangeIn",
        "DataFilterValueRangeOut": "_sheets_381_DataFilterValueRangeOut",
        "CandlestickDataIn": "_sheets_382_CandlestickDataIn",
        "CandlestickDataOut": "_sheets_383_CandlestickDataOut",
        "AppendDimensionRequestIn": "_sheets_384_AppendDimensionRequestIn",
        "AppendDimensionRequestOut": "_sheets_385_AppendDimensionRequestOut",
        "BandedRangeIn": "_sheets_386_BandedRangeIn",
        "BandedRangeOut": "_sheets_387_BandedRangeOut",
        "DataSourceObjectReferenceIn": "_sheets_388_DataSourceObjectReferenceIn",
        "DataSourceObjectReferenceOut": "_sheets_389_DataSourceObjectReferenceOut",
        "AddSlicerRequestIn": "_sheets_390_AddSlicerRequestIn",
        "AddSlicerRequestOut": "_sheets_391_AddSlicerRequestOut",
        "DuplicateFilterViewRequestIn": "_sheets_392_DuplicateFilterViewRequestIn",
        "DuplicateFilterViewRequestOut": "_sheets_393_DuplicateFilterViewRequestOut",
        "AddProtectedRangeResponseIn": "_sheets_394_AddProtectedRangeResponseIn",
        "AddProtectedRangeResponseOut": "_sheets_395_AddProtectedRangeResponseOut",
        "PieChartSpecIn": "_sheets_396_PieChartSpecIn",
        "PieChartSpecOut": "_sheets_397_PieChartSpecOut",
        "LinkIn": "_sheets_398_LinkIn",
        "LinkOut": "_sheets_399_LinkOut",
        "PivotGroupIn": "_sheets_400_PivotGroupIn",
        "PivotGroupOut": "_sheets_401_PivotGroupOut",
        "AddBandingRequestIn": "_sheets_402_AddBandingRequestIn",
        "AddBandingRequestOut": "_sheets_403_AddBandingRequestOut",
        "AddNamedRangeRequestIn": "_sheets_404_AddNamedRangeRequestIn",
        "AddNamedRangeRequestOut": "_sheets_405_AddNamedRangeRequestOut",
        "RefreshDataSourceRequestIn": "_sheets_406_RefreshDataSourceRequestIn",
        "RefreshDataSourceRequestOut": "_sheets_407_RefreshDataSourceRequestOut",
        "CandlestickChartSpecIn": "_sheets_408_CandlestickChartSpecIn",
        "CandlestickChartSpecOut": "_sheets_409_CandlestickChartSpecOut",
        "UpdateCellsRequestIn": "_sheets_410_UpdateCellsRequestIn",
        "UpdateCellsRequestOut": "_sheets_411_UpdateCellsRequestOut",
        "ColorStyleIn": "_sheets_412_ColorStyleIn",
        "ColorStyleOut": "_sheets_413_ColorStyleOut",
        "DeleteDimensionGroupResponseIn": "_sheets_414_DeleteDimensionGroupResponseIn",
        "DeleteDimensionGroupResponseOut": "_sheets_415_DeleteDimensionGroupResponseOut",
        "ClearValuesRequestIn": "_sheets_416_ClearValuesRequestIn",
        "ClearValuesRequestOut": "_sheets_417_ClearValuesRequestOut",
        "ChartDateTimeRuleIn": "_sheets_418_ChartDateTimeRuleIn",
        "ChartDateTimeRuleOut": "_sheets_419_ChartDateTimeRuleOut",
        "DataValidationRuleIn": "_sheets_420_DataValidationRuleIn",
        "DataValidationRuleOut": "_sheets_421_DataValidationRuleOut",
        "GradientRuleIn": "_sheets_422_GradientRuleIn",
        "GradientRuleOut": "_sheets_423_GradientRuleOut",
        "DataSourceRefreshWeeklyScheduleIn": "_sheets_424_DataSourceRefreshWeeklyScheduleIn",
        "DataSourceRefreshWeeklyScheduleOut": "_sheets_425_DataSourceRefreshWeeklyScheduleOut",
        "SheetPropertiesIn": "_sheets_426_SheetPropertiesIn",
        "SheetPropertiesOut": "_sheets_427_SheetPropertiesOut",
        "OrgChartSpecIn": "_sheets_428_OrgChartSpecIn",
        "OrgChartSpecOut": "_sheets_429_OrgChartSpecOut",
        "GridPropertiesIn": "_sheets_430_GridPropertiesIn",
        "GridPropertiesOut": "_sheets_431_GridPropertiesOut",
        "BasicChartDomainIn": "_sheets_432_BasicChartDomainIn",
        "BasicChartDomainOut": "_sheets_433_BasicChartDomainOut",
        "BatchUpdateValuesResponseIn": "_sheets_434_BatchUpdateValuesResponseIn",
        "BatchUpdateValuesResponseOut": "_sheets_435_BatchUpdateValuesResponseOut",
        "UpdateBandingRequestIn": "_sheets_436_UpdateBandingRequestIn",
        "UpdateBandingRequestOut": "_sheets_437_UpdateBandingRequestOut",
        "SearchDeveloperMetadataResponseIn": "_sheets_438_SearchDeveloperMetadataResponseIn",
        "SearchDeveloperMetadataResponseOut": "_sheets_439_SearchDeveloperMetadataResponseOut",
        "MoveDimensionRequestIn": "_sheets_440_MoveDimensionRequestIn",
        "MoveDimensionRequestOut": "_sheets_441_MoveDimensionRequestOut",
        "LineStyleIn": "_sheets_442_LineStyleIn",
        "LineStyleOut": "_sheets_443_LineStyleOut",
        "BatchUpdateValuesByDataFilterResponseIn": "_sheets_444_BatchUpdateValuesByDataFilterResponseIn",
        "BatchUpdateValuesByDataFilterResponseOut": "_sheets_445_BatchUpdateValuesByDataFilterResponseOut",
        "UpdateValuesResponseIn": "_sheets_446_UpdateValuesResponseIn",
        "UpdateValuesResponseOut": "_sheets_447_UpdateValuesResponseOut",
        "UpdateDimensionPropertiesRequestIn": "_sheets_448_UpdateDimensionPropertiesRequestIn",
        "UpdateDimensionPropertiesRequestOut": "_sheets_449_UpdateDimensionPropertiesRequestOut",
        "CellDataIn": "_sheets_450_CellDataIn",
        "CellDataOut": "_sheets_451_CellDataOut",
        "SpreadsheetThemeIn": "_sheets_452_SpreadsheetThemeIn",
        "SpreadsheetThemeOut": "_sheets_453_SpreadsheetThemeOut",
        "ChartHistogramRuleIn": "_sheets_454_ChartHistogramRuleIn",
        "ChartHistogramRuleOut": "_sheets_455_ChartHistogramRuleOut",
        "BatchUpdateValuesByDataFilterRequestIn": "_sheets_456_BatchUpdateValuesByDataFilterRequestIn",
        "BatchUpdateValuesByDataFilterRequestOut": "_sheets_457_BatchUpdateValuesByDataFilterRequestOut",
        "BasicSeriesDataPointStyleOverrideIn": "_sheets_458_BasicSeriesDataPointStyleOverrideIn",
        "BasicSeriesDataPointStyleOverrideOut": "_sheets_459_BasicSeriesDataPointStyleOverrideOut",
        "GridCoordinateIn": "_sheets_460_GridCoordinateIn",
        "GridCoordinateOut": "_sheets_461_GridCoordinateOut",
        "BatchClearValuesRequestIn": "_sheets_462_BatchClearValuesRequestIn",
        "BatchClearValuesRequestOut": "_sheets_463_BatchClearValuesRequestOut",
        "FilterSpecIn": "_sheets_464_FilterSpecIn",
        "FilterSpecOut": "_sheets_465_FilterSpecOut",
        "ChartGroupRuleIn": "_sheets_466_ChartGroupRuleIn",
        "ChartGroupRuleOut": "_sheets_467_ChartGroupRuleOut",
        "DataFilterIn": "_sheets_468_DataFilterIn",
        "DataFilterOut": "_sheets_469_DataFilterOut",
        "ConditionValueIn": "_sheets_470_ConditionValueIn",
        "ConditionValueOut": "_sheets_471_ConditionValueOut",
        "MergeCellsRequestIn": "_sheets_472_MergeCellsRequestIn",
        "MergeCellsRequestOut": "_sheets_473_MergeCellsRequestOut",
        "BaselineValueFormatIn": "_sheets_474_BaselineValueFormatIn",
        "BaselineValueFormatOut": "_sheets_475_BaselineValueFormatOut",
        "WaterfallChartDomainIn": "_sheets_476_WaterfallChartDomainIn",
        "WaterfallChartDomainOut": "_sheets_477_WaterfallChartDomainOut",
        "GetSpreadsheetByDataFilterRequestIn": "_sheets_478_GetSpreadsheetByDataFilterRequestIn",
        "GetSpreadsheetByDataFilterRequestOut": "_sheets_479_GetSpreadsheetByDataFilterRequestOut",
        "UpdateEmbeddedObjectPositionRequestIn": "_sheets_480_UpdateEmbeddedObjectPositionRequestIn",
        "UpdateEmbeddedObjectPositionRequestOut": "_sheets_481_UpdateEmbeddedObjectPositionRequestOut",
        "DeleteDimensionGroupRequestIn": "_sheets_482_DeleteDimensionGroupRequestIn",
        "DeleteDimensionGroupRequestOut": "_sheets_483_DeleteDimensionGroupRequestOut",
        "PointStyleIn": "_sheets_484_PointStyleIn",
        "PointStyleOut": "_sheets_485_PointStyleOut",
        "DuplicateFilterViewResponseIn": "_sheets_486_DuplicateFilterViewResponseIn",
        "DuplicateFilterViewResponseOut": "_sheets_487_DuplicateFilterViewResponseOut",
        "EmbeddedChartIn": "_sheets_488_EmbeddedChartIn",
        "EmbeddedChartOut": "_sheets_489_EmbeddedChartOut",
        "BatchClearValuesByDataFilterRequestIn": "_sheets_490_BatchClearValuesByDataFilterRequestIn",
        "BatchClearValuesByDataFilterRequestOut": "_sheets_491_BatchClearValuesByDataFilterRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AddDataSourceRequestIn"] = t.struct(
        {"dataSource": t.proxy(renames["DataSourceIn"]).optional()}
    ).named(renames["AddDataSourceRequestIn"])
    types["AddDataSourceRequestOut"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDataSourceRequestOut"])
    types["ValueRangeIn"] = t.struct(
        {
            "majorDimension": t.string().optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "range": t.string().optional(),
        }
    ).named(renames["ValueRangeIn"])
    types["ValueRangeOut"] = t.struct(
        {
            "majorDimension": t.string().optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "range": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueRangeOut"])
    types["PivotGroupSortValueBucketIn"] = t.struct(
        {
            "valuesIndex": t.integer().optional(),
            "buckets": t.array(t.proxy(renames["ExtendedValueIn"])).optional(),
        }
    ).named(renames["PivotGroupSortValueBucketIn"])
    types["PivotGroupSortValueBucketOut"] = t.struct(
        {
            "valuesIndex": t.integer().optional(),
            "buckets": t.array(t.proxy(renames["ExtendedValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupSortValueBucketOut"])
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
    types["DataSourceSheetPropertiesIn"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
            "columns": t.array(t.proxy(renames["DataSourceColumnIn"])).optional(),
            "dataSourceId": t.string().optional(),
        }
    ).named(renames["DataSourceSheetPropertiesIn"])
    types["DataSourceSheetPropertiesOut"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "columns": t.array(t.proxy(renames["DataSourceColumnOut"])).optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSheetPropertiesOut"])
    types["ResponseIn"] = t.struct(
        {
            "addSheet": t.proxy(renames["AddSheetResponseIn"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseIn"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseIn"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseIn"]).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseIn"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseIn"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseIn"]).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseIn"]).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseIn"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseIn"]
            ).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseIn"]
            ).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseIn"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseIn"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartResponseIn"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseIn"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseIn"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseIn"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseIn"]).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseIn"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseIn"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingResponseIn"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseIn"]
            ).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseIn"]
            ).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "addSheet": t.proxy(renames["AddSheetResponseOut"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseOut"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseOut"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseOut"]).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseOut"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseOut"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseOut"]).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseOut"]).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseOut"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseOut"]
            ).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseOut"]
            ).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseOut"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseOut"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartResponseOut"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseOut"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseOut"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseOut"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseOut"]).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseOut"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseOut"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingResponseOut"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseOut"]
            ).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["TextFormatIn"] = t.struct(
        {
            "strikethrough": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "bold": t.boolean().optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "fontFamily": t.string().optional(),
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "underline": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["TextFormatIn"])
    types["TextFormatOut"] = t.struct(
        {
            "strikethrough": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "bold": t.boolean().optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "fontFamily": t.string().optional(),
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "underline": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFormatOut"])
    types["BigQueryQuerySpecIn"] = t.struct({"rawQuery": t.string().optional()}).named(
        renames["BigQueryQuerySpecIn"]
    )
    types["BigQueryQuerySpecOut"] = t.struct(
        {
            "rawQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryQuerySpecOut"])
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
    types["DataSourceRefreshMonthlyScheduleIn"] = t.struct(
        {
            "daysOfMonth": t.array(t.integer()).optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DataSourceRefreshMonthlyScheduleIn"])
    types["DataSourceRefreshMonthlyScheduleOut"] = t.struct(
        {
            "daysOfMonth": t.array(t.integer()).optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshMonthlyScheduleOut"])
    types["UpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterIn"]).optional(),
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
            "updatedRows": t.integer().optional(),
            "updatedCells": t.integer().optional(),
            "updatedColumns": t.integer().optional(),
            "updatedRange": t.string().optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseIn"])
    types["UpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "updatedRows": t.integer().optional(),
            "updatedCells": t.integer().optional(),
            "updatedColumns": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseOut"])
    types["AddFilterViewRequestIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewRequestIn"])
    types["AddFilterViewRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewRequestOut"])
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
    types["TextPositionIn"] = t.struct(
        {"horizontalAlignment": t.string().optional()}
    ).named(renames["TextPositionIn"])
    types["TextPositionOut"] = t.struct(
        {
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPositionOut"])
    types["UpdateBordersRequestIn"] = t.struct(
        {
            "right": t.proxy(renames["BorderIn"]).optional(),
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "left": t.proxy(renames["BorderIn"]).optional(),
            "innerVertical": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["UpdateBordersRequestIn"])
    types["UpdateBordersRequestOut"] = t.struct(
        {
            "right": t.proxy(renames["BorderOut"]).optional(),
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "left": t.proxy(renames["BorderOut"]).optional(),
            "innerVertical": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBordersRequestOut"])
    types["ProtectedRangeIn"] = t.struct(
        {
            "requestingUserCanEdit": t.boolean().optional(),
            "protectedRangeId": t.integer().optional(),
            "warningOnly": t.boolean().optional(),
            "namedRangeId": t.string().optional(),
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "description": t.string().optional(),
            "editors": t.proxy(renames["EditorsIn"]).optional(),
        }
    ).named(renames["ProtectedRangeIn"])
    types["ProtectedRangeOut"] = t.struct(
        {
            "requestingUserCanEdit": t.boolean().optional(),
            "protectedRangeId": t.integer().optional(),
            "warningOnly": t.boolean().optional(),
            "namedRangeId": t.string().optional(),
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "description": t.string().optional(),
            "editors": t.proxy(renames["EditorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProtectedRangeOut"])
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
    types["AddSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetResponseIn"])
    types["AddSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetResponseOut"])
    types["WaterfallChartColumnStyleIn"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "label": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["WaterfallChartColumnStyleIn"])
    types["WaterfallChartColumnStyleOut"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "label": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartColumnStyleOut"])
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
    types["DeleteConditionalFormatRuleResponseIn"] = t.struct(
        {"rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional()}
    ).named(renames["DeleteConditionalFormatRuleResponseIn"])
    types["DeleteConditionalFormatRuleResponseOut"] = t.struct(
        {
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConditionalFormatRuleResponseOut"])
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
    types["CopySheetToAnotherSpreadsheetRequestIn"] = t.struct(
        {"destinationSpreadsheetId": t.string().optional()}
    ).named(renames["CopySheetToAnotherSpreadsheetRequestIn"])
    types["CopySheetToAnotherSpreadsheetRequestOut"] = t.struct(
        {
            "destinationSpreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopySheetToAnotherSpreadsheetRequestOut"])
    types["DeleteDuplicatesResponseIn"] = t.struct(
        {"duplicatesRemovedCount": t.integer().optional()}
    ).named(renames["DeleteDuplicatesResponseIn"])
    types["DeleteDuplicatesResponseOut"] = t.struct(
        {
            "duplicatesRemovedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDuplicatesResponseOut"])
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
    types["DeveloperMetadataLocationIn"] = t.struct(
        {
            "locationType": t.string().optional(),
            "spreadsheet": t.boolean().optional(),
            "dimensionRange": t.proxy(renames["DimensionRangeIn"]).optional(),
            "sheetId": t.integer().optional(),
        }
    ).named(renames["DeveloperMetadataLocationIn"])
    types["DeveloperMetadataLocationOut"] = t.struct(
        {
            "locationType": t.string().optional(),
            "spreadsheet": t.boolean().optional(),
            "dimensionRange": t.proxy(renames["DimensionRangeOut"]).optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLocationOut"])
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
    types["BatchUpdateSpreadsheetRequestIn"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RequestIn"])).optional(),
            "responseIncludeGridData": t.boolean().optional(),
            "includeSpreadsheetInResponse": t.boolean().optional(),
            "responseRanges": t.array(t.string()).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetRequestIn"])
    types["BatchUpdateSpreadsheetRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RequestOut"])).optional(),
            "responseIncludeGridData": t.boolean().optional(),
            "includeSpreadsheetInResponse": t.boolean().optional(),
            "responseRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetRequestOut"])
    types["AddSheetRequestIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetRequestIn"])
    types["AddSheetRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetRequestOut"])
    types["OverlayPositionIn"] = t.struct(
        {
            "offsetXPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "offsetYPixels": t.integer().optional(),
            "anchorCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "heightPixels": t.integer().optional(),
        }
    ).named(renames["OverlayPositionIn"])
    types["OverlayPositionOut"] = t.struct(
        {
            "offsetXPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "offsetYPixels": t.integer().optional(),
            "anchorCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "heightPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OverlayPositionOut"])
    types["UpdateDeveloperMetadataRequestIn"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "fields": t.string().optional(),
            "developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestIn"])
    types["UpdateDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "fields": t.string().optional(),
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestOut"])
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
    types["AddFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewResponseIn"])
    types["AddFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewResponseOut"])
    types["BatchUpdateSpreadsheetResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
            "updatedSpreadsheet": t.proxy(renames["SpreadsheetIn"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetResponseIn"])
    types["BatchUpdateSpreadsheetResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "updatedSpreadsheet": t.proxy(renames["SpreadsheetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateSpreadsheetResponseOut"])
    types["SourceAndDestinationIn"] = t.struct(
        {
            "fillLength": t.integer().optional(),
            "dimension": t.string().optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["SourceAndDestinationIn"])
    types["SourceAndDestinationOut"] = t.struct(
        {
            "fillLength": t.integer().optional(),
            "dimension": t.string().optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceAndDestinationOut"])
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
    types["DeleteBandingRequestIn"] = t.struct(
        {"bandedRangeId": t.integer().optional()}
    ).named(renames["DeleteBandingRequestIn"])
    types["DeleteBandingRequestOut"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBandingRequestOut"])
    types["UpdateConditionalFormatRuleRequestIn"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "index": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "sheetId": t.integer().optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestIn"])
    types["UpdateConditionalFormatRuleRequestOut"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "index": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestOut"])
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
    types["UpdateConditionalFormatRuleResponseIn"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "oldIndex": t.integer().optional(),
            "newRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseIn"])
    types["UpdateConditionalFormatRuleResponseOut"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "oldIndex": t.integer().optional(),
            "newRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseOut"])
    types["DataLabelIn"] = t.struct(
        {
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "customLabelData": t.proxy(renames["ChartDataIn"]).optional(),
            "type": t.string().optional(),
            "placement": t.string().optional(),
        }
    ).named(renames["DataLabelIn"])
    types["DataLabelOut"] = t.struct(
        {
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "customLabelData": t.proxy(renames["ChartDataOut"]).optional(),
            "type": t.string().optional(),
            "placement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLabelOut"])
    types["PaddingIn"] = t.struct(
        {
            "right": t.integer().optional(),
            "bottom": t.integer().optional(),
            "top": t.integer().optional(),
            "left": t.integer().optional(),
        }
    ).named(renames["PaddingIn"])
    types["PaddingOut"] = t.struct(
        {
            "right": t.integer().optional(),
            "bottom": t.integer().optional(),
            "top": t.integer().optional(),
            "left": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaddingOut"])
    types["AddDataSourceResponseIn"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
            "dataSource": t.proxy(renames["DataSourceIn"]).optional(),
        }
    ).named(renames["AddDataSourceResponseIn"])
    types["AddDataSourceResponseOut"] = t.struct(
        {
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDataSourceResponseOut"])
    types["DataExecutionStatusIn"] = t.struct(
        {
            "errorCode": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "state": t.string().optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["DataExecutionStatusIn"])
    types["DataExecutionStatusOut"] = t.struct(
        {
            "errorCode": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "state": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataExecutionStatusOut"])
    types["RandomizeRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["RandomizeRangeRequestIn"])
    types["RandomizeRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RandomizeRangeRequestOut"])
    types["AppendValuesResponseIn"] = t.struct(
        {
            "updates": t.proxy(renames["UpdateValuesResponseIn"]).optional(),
            "tableRange": t.string().optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["AppendValuesResponseIn"])
    types["AppendValuesResponseOut"] = t.struct(
        {
            "updates": t.proxy(renames["UpdateValuesResponseOut"]).optional(),
            "tableRange": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendValuesResponseOut"])
    types["DeleteDataSourceRequestIn"] = t.struct(
        {"dataSourceId": t.string().optional()}
    ).named(renames["DeleteDataSourceRequestIn"])
    types["DeleteDataSourceRequestOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDataSourceRequestOut"])
    types["BatchGetValuesByDataFilterRequestIn"] = t.struct(
        {
            "majorDimension": t.string().optional(),
            "dateTimeRenderOption": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "valueRenderOption": t.string().optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestIn"])
    types["BatchGetValuesByDataFilterRequestOut"] = t.struct(
        {
            "majorDimension": t.string().optional(),
            "dateTimeRenderOption": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "valueRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestOut"])
    types["BatchClearValuesResponseIn"] = t.struct(
        {
            "clearedRanges": t.array(t.string()).optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["BatchClearValuesResponseIn"])
    types["BatchClearValuesResponseOut"] = t.struct(
        {
            "clearedRanges": t.array(t.string()).optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesResponseOut"])
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
    types["CreateDeveloperMetadataResponseIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataResponseIn"])
    types["CreateDeveloperMetadataResponseOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataResponseOut"])
    types["DeleteDimensionRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionRequestIn"])
    types["DeleteDimensionRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionRequestOut"])
    types["AddChartRequestIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartRequestIn"])
    types["AddChartRequestOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartRequestOut"])
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
    types["TreemapChartColorScaleIn"] = t.struct(
        {
            "maxValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "minValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "minValueColor": t.proxy(renames["ColorIn"]).optional(),
            "midValueColor": t.proxy(renames["ColorIn"]).optional(),
            "maxValueColor": t.proxy(renames["ColorIn"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "noDataColor": t.proxy(renames["ColorIn"]).optional(),
            "noDataColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleIn"])
    types["TreemapChartColorScaleOut"] = t.struct(
        {
            "maxValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "minValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "minValueColor": t.proxy(renames["ColorOut"]).optional(),
            "midValueColor": t.proxy(renames["ColorOut"]).optional(),
            "maxValueColor": t.proxy(renames["ColorOut"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "noDataColor": t.proxy(renames["ColorOut"]).optional(),
            "noDataColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleOut"])
    types["WaterfallChartSeriesIn"] = t.struct(
        {
            "positiveColumnsStyle": t.proxy(
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
            "hideTrailingSubtotal": t.boolean().optional(),
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
        }
    ).named(renames["WaterfallChartSeriesIn"])
    types["WaterfallChartSeriesOut"] = t.struct(
        {
            "positiveColumnsStyle": t.proxy(
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
            "hideTrailingSubtotal": t.boolean().optional(),
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSeriesOut"])
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
    types["SpreadsheetIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
            "spreadsheetUrl": t.string().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
        }
    ).named(renames["SpreadsheetIn"])
    types["SpreadsheetOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesOut"]).optional(),
            "dataSourceSchedules": t.array(
                t.proxy(renames["DataSourceRefreshScheduleOut"])
            ).optional(),
            "spreadsheetUrl": t.string().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "sheets": t.array(t.proxy(renames["SheetOut"])).optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetOut"])
    types["HistogramSeriesIn"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataIn"]).optional(),
            "barColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "barColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["HistogramSeriesIn"])
    types["HistogramSeriesOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "barColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "barColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramSeriesOut"])
    types["DeveloperMetadataLookupIn"] = t.struct(
        {
            "locationType": t.string().optional(),
            "metadataKey": t.string().optional(),
            "metadataId": t.integer().optional(),
            "visibility": t.string().optional(),
            "metadataValue": t.string().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationIn"]
            ).optional(),
            "locationMatchingStrategy": t.string().optional(),
        }
    ).named(renames["DeveloperMetadataLookupIn"])
    types["DeveloperMetadataLookupOut"] = t.struct(
        {
            "locationType": t.string().optional(),
            "metadataKey": t.string().optional(),
            "metadataId": t.integer().optional(),
            "visibility": t.string().optional(),
            "metadataValue": t.string().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationOut"]
            ).optional(),
            "locationMatchingStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLookupOut"])
    types["PivotValueIn"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "sourceColumnOffset": t.integer().optional(),
            "calculatedDisplayType": t.string().optional(),
            "name": t.string().optional(),
            "formula": t.string().optional(),
            "summarizeFunction": t.string().optional(),
        }
    ).named(renames["PivotValueIn"])
    types["PivotValueOut"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "sourceColumnOffset": t.integer().optional(),
            "calculatedDisplayType": t.string().optional(),
            "name": t.string().optional(),
            "formula": t.string().optional(),
            "summarizeFunction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueOut"])
    types["ColorIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
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
    types["DeleteDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilter": t.proxy(renames["DataFilterIn"]).optional()}
    ).named(renames["DeleteDeveloperMetadataRequestIn"])
    types["DeleteDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDeveloperMetadataRequestOut"])
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
    types["ExtendedValueIn"] = t.struct(
        {
            "errorValue": t.proxy(renames["ErrorValueIn"]).optional(),
            "numberValue": t.number().optional(),
            "formulaValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["ExtendedValueIn"])
    types["ExtendedValueOut"] = t.struct(
        {
            "errorValue": t.proxy(renames["ErrorValueOut"]).optional(),
            "numberValue": t.number().optional(),
            "formulaValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedValueOut"])
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
    types["UpdateEmbeddedObjectBorderRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.integer().optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestIn"])
    types["UpdateEmbeddedObjectBorderRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "objectId": t.integer().optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestOut"])
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
    types["AddNamedRangeResponseIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeResponseIn"])
    types["AddNamedRangeResponseOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeResponseOut"])
    types["BasicChartSpecIn"] = t.struct(
        {
            "axis": t.array(t.proxy(renames["BasicChartAxisIn"])).optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "interpolateNulls": t.boolean().optional(),
            "stackedType": t.string().optional(),
            "legendPosition": t.string().optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesIn"])).optional(),
            "lineSmoothing": t.boolean().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainIn"])).optional(),
            "threeDimensional": t.boolean().optional(),
            "compareMode": t.string().optional(),
            "headerCount": t.integer().optional(),
            "chartType": t.string().optional(),
        }
    ).named(renames["BasicChartSpecIn"])
    types["BasicChartSpecOut"] = t.struct(
        {
            "axis": t.array(t.proxy(renames["BasicChartAxisOut"])).optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "interpolateNulls": t.boolean().optional(),
            "stackedType": t.string().optional(),
            "legendPosition": t.string().optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesOut"])).optional(),
            "lineSmoothing": t.boolean().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainOut"])).optional(),
            "threeDimensional": t.boolean().optional(),
            "compareMode": t.string().optional(),
            "headerCount": t.integer().optional(),
            "chartType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSpecOut"])
    types["ChartSpecIn"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "pieChart": t.proxy(renames["PieChartSpecIn"]).optional(),
            "maximized": t.boolean().optional(),
            "treemapChart": t.proxy(renames["TreemapChartSpecIn"]).optional(),
            "fontName": t.string().optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "candlestickChart": t.proxy(renames["CandlestickChartSpecIn"]).optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecIn"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecIn"]).optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesIn"]
            ).optional(),
            "basicChart": t.proxy(renames["BasicChartSpecIn"]).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecIn"]).optional(),
            "altText": t.string().optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecIn"]).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
        }
    ).named(renames["ChartSpecIn"])
    types["ChartSpecOut"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "pieChart": t.proxy(renames["PieChartSpecOut"]).optional(),
            "maximized": t.boolean().optional(),
            "treemapChart": t.proxy(renames["TreemapChartSpecOut"]).optional(),
            "fontName": t.string().optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "candlestickChart": t.proxy(renames["CandlestickChartSpecOut"]).optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecOut"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecOut"]).optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesOut"]
            ).optional(),
            "basicChart": t.proxy(renames["BasicChartSpecOut"]).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecOut"]).optional(),
            "altText": t.string().optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecOut"]).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
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
    types["TextRotationIn"] = t.struct(
        {"angle": t.integer().optional(), "vertical": t.boolean().optional()}
    ).named(renames["TextRotationIn"])
    types["TextRotationOut"] = t.struct(
        {
            "angle": t.integer().optional(),
            "vertical": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextRotationOut"])
    types["ManualRuleIn"] = t.struct(
        {"groups": t.array(t.proxy(renames["ManualRuleGroupIn"])).optional()}
    ).named(renames["ManualRuleIn"])
    types["ManualRuleOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["ManualRuleGroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualRuleOut"])
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
    types["SortSpecIn"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "dimensionIndex": t.integer().optional(),
        }
    ).named(renames["SortSpecIn"])
    types["SortSpecOut"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "dimensionIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortSpecOut"])
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
    types["AutoFillRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationIn"]
            ).optional(),
            "useAlternateSeries": t.boolean().optional(),
        }
    ).named(renames["AutoFillRequestIn"])
    types["AutoFillRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationOut"]
            ).optional(),
            "useAlternateSeries": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoFillRequestOut"])
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
    types["CutPasteRequestIn"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "pasteType": t.string().optional(),
            "destination": t.proxy(renames["GridCoordinateIn"]).optional(),
        }
    ).named(renames["CutPasteRequestIn"])
    types["CutPasteRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "pasteType": t.string().optional(),
            "destination": t.proxy(renames["GridCoordinateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutPasteRequestOut"])
    types["UnmergeCellsRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["UnmergeCellsRequestIn"])
    types["UnmergeCellsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeCellsRequestOut"])
    types["DuplicateSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["DuplicateSheetResponseIn"])
    types["DuplicateSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetResponseOut"])
    types["TrimWhitespaceRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["TrimWhitespaceRequestIn"])
    types["TrimWhitespaceRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceRequestOut"])
    types["TreemapChartSpecIn"] = t.struct(
        {
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "sizeData": t.proxy(renames["ChartDataIn"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "hintedLevels": t.integer().optional(),
            "colorScale": t.proxy(renames["TreemapChartColorScaleIn"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "levels": t.integer().optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "maxValue": t.number().optional(),
            "colorData": t.proxy(renames["ChartDataIn"]).optional(),
            "minValue": t.number().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
        }
    ).named(renames["TreemapChartSpecIn"])
    types["TreemapChartSpecOut"] = t.struct(
        {
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "sizeData": t.proxy(renames["ChartDataOut"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "hintedLevels": t.integer().optional(),
            "colorScale": t.proxy(renames["TreemapChartColorScaleOut"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "levels": t.integer().optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "maxValue": t.number().optional(),
            "colorData": t.proxy(renames["ChartDataOut"]).optional(),
            "minValue": t.number().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartSpecOut"])
    types["PivotTableIn"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecIn"])).optional(),
            "columns": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "valueLayout": t.string().optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "dataSourceId": t.string().optional(),
            "rows": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "values": t.array(t.proxy(renames["PivotValueIn"])).optional(),
        }
    ).named(renames["PivotTableIn"])
    types["PivotTableOut"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecOut"])).optional(),
            "columns": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "valueLayout": t.string().optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "dataSourceId": t.string().optional(),
            "rows": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "values": t.array(t.proxy(renames["PivotValueOut"])).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotTableOut"])
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
    types["FilterCriteriaIn"] = t.struct(
        {
            "hiddenValues": t.array(t.string()).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorIn"]).optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["FilterCriteriaIn"])
    types["FilterCriteriaOut"] = t.struct(
        {
            "hiddenValues": t.array(t.string()).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorOut"]).optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterCriteriaOut"])
    types["BasicFilterIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BasicFilterIn"])
    types["BasicFilterOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicFilterOut"])
    types["RepeatCellRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "cell": t.proxy(renames["CellDataIn"]).optional(),
        }
    ).named(renames["RepeatCellRequestIn"])
    types["RepeatCellRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "cell": t.proxy(renames["CellDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepeatCellRequestOut"])
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
    types["AddChartResponseIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartResponseIn"])
    types["AddChartResponseOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartResponseOut"])
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
    types["BordersIn"] = t.struct(
        {
            "left": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "right": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["BordersIn"])
    types["BordersOut"] = t.struct(
        {
            "left": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "right": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BordersOut"])
    types["EmbeddedObjectPositionIn"] = t.struct(
        {
            "newSheet": t.boolean().optional(),
            "overlayPosition": t.proxy(renames["OverlayPositionIn"]).optional(),
            "sheetId": t.integer().optional(),
        }
    ).named(renames["EmbeddedObjectPositionIn"])
    types["EmbeddedObjectPositionOut"] = t.struct(
        {
            "newSheet": t.boolean().optional(),
            "overlayPosition": t.proxy(renames["OverlayPositionOut"]).optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedObjectPositionOut"])
    types["SlicerIn"] = t.struct(
        {
            "slicerId": t.integer().optional(),
            "spec": t.proxy(renames["SlicerSpecIn"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
        }
    ).named(renames["SlicerIn"])
    types["SlicerOut"] = t.struct(
        {
            "slicerId": t.integer().optional(),
            "spec": t.proxy(renames["SlicerSpecOut"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerOut"])
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
            "pixelSize": t.integer().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionPropertiesOut"])
    types["BasicChartAxisIn"] = t.struct(
        {
            "format": t.proxy(renames["TextFormatIn"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "title": t.string().optional(),
            "position": t.string().optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsIn"]
            ).optional(),
        }
    ).named(renames["BasicChartAxisIn"])
    types["BasicChartAxisOut"] = t.struct(
        {
            "format": t.proxy(renames["TextFormatOut"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "title": t.string().optional(),
            "position": t.string().optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartAxisOut"])
    types["WaterfallChartSpecIn"] = t.struct(
        {
            "series": t.array(t.proxy(renames["WaterfallChartSeriesIn"])).optional(),
            "firstValueIsTotal": t.boolean().optional(),
            "stackedType": t.string().optional(),
            "connectorLineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "hideConnectorLines": t.boolean().optional(),
            "domain": t.proxy(renames["WaterfallChartDomainIn"]).optional(),
        }
    ).named(renames["WaterfallChartSpecIn"])
    types["WaterfallChartSpecOut"] = t.struct(
        {
            "series": t.array(t.proxy(renames["WaterfallChartSeriesOut"])).optional(),
            "firstValueIsTotal": t.boolean().optional(),
            "stackedType": t.string().optional(),
            "connectorLineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "hideConnectorLines": t.boolean().optional(),
            "domain": t.proxy(renames["WaterfallChartDomainOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSpecOut"])
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
    types["AddBandingResponseIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingResponseIn"])
    types["AddBandingResponseOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingResponseOut"])
    types["AddSlicerResponseIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerResponseIn"])
    types["AddSlicerResponseOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerResponseOut"])
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
    types["DeleteEmbeddedObjectRequestIn"] = t.struct(
        {"objectId": t.integer().optional()}
    ).named(renames["DeleteEmbeddedObjectRequestIn"])
    types["DeleteEmbeddedObjectRequestOut"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteEmbeddedObjectRequestOut"])
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
    types["WaterfallChartCustomSubtotalIn"] = t.struct(
        {
            "label": t.string().optional(),
            "dataIsSubtotal": t.boolean().optional(),
            "subtotalIndex": t.integer().optional(),
        }
    ).named(renames["WaterfallChartCustomSubtotalIn"])
    types["WaterfallChartCustomSubtotalOut"] = t.struct(
        {
            "label": t.string().optional(),
            "dataIsSubtotal": t.boolean().optional(),
            "subtotalIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartCustomSubtotalOut"])
    types["DeleteFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DeleteFilterViewRequestIn"])
    types["DeleteFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFilterViewRequestOut"])
    types["TrimWhitespaceResponseIn"] = t.struct(
        {"cellsChangedCount": t.integer().optional()}
    ).named(renames["TrimWhitespaceResponseIn"])
    types["TrimWhitespaceResponseOut"] = t.struct(
        {
            "cellsChangedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceResponseOut"])
    types["DataSourceColumnReferenceIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["DataSourceColumnReferenceIn"])
    types["DataSourceColumnReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceColumnReferenceOut"])
    types["GridDataIn"] = t.struct(
        {
            "startRow": t.integer().optional(),
            "rowData": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
            "startColumn": t.integer().optional(),
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
        }
    ).named(renames["GridDataIn"])
    types["GridDataOut"] = t.struct(
        {
            "startRow": t.integer().optional(),
            "rowData": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "startColumn": t.integer().optional(),
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridDataOut"])
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
    types["UpdateEmbeddedObjectPositionResponseIn"] = t.struct(
        {"position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional()}
    ).named(renames["UpdateEmbeddedObjectPositionResponseIn"])
    types["UpdateEmbeddedObjectPositionResponseOut"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionResponseOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["DeveloperMetadataIn"] = t.struct(
        {
            "metadataKey": t.string().optional(),
            "visibility": t.string().optional(),
            "metadataId": t.integer().optional(),
            "metadataValue": t.string().optional(),
            "location": t.proxy(renames["DeveloperMetadataLocationIn"]).optional(),
        }
    ).named(renames["DeveloperMetadataIn"])
    types["DeveloperMetadataOut"] = t.struct(
        {
            "metadataKey": t.string().optional(),
            "visibility": t.string().optional(),
            "metadataId": t.integer().optional(),
            "metadataValue": t.string().optional(),
            "location": t.proxy(renames["DeveloperMetadataLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataOut"])
    types["DataSourceTableIn"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceIn"])
            ).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "columnSelectionType": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "rowLimit": t.integer().optional(),
        }
    ).named(renames["DataSourceTableIn"])
    types["DataSourceTableOut"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceOut"])
            ).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "columnSelectionType": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "rowLimit": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceTableOut"])
    types["ClearBasicFilterRequestIn"] = t.struct(
        {"sheetId": t.integer().optional()}
    ).named(renames["ClearBasicFilterRequestIn"])
    types["ClearBasicFilterRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearBasicFilterRequestOut"])
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
    types["SlicerSpecIn"] = t.struct(
        {
            "dataRange": t.proxy(renames["GridRangeIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "columnIndex": t.integer().optional(),
            "applyToPivotTables": t.boolean().optional(),
            "title": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["SlicerSpecIn"])
    types["SlicerSpecOut"] = t.struct(
        {
            "dataRange": t.proxy(renames["GridRangeOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "columnIndex": t.integer().optional(),
            "applyToPivotTables": t.boolean().optional(),
            "title": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerSpecOut"])
    types["CandlestickSeriesIn"] = t.struct(
        {"data": t.proxy(renames["ChartDataIn"]).optional()}
    ).named(renames["CandlestickSeriesIn"])
    types["CandlestickSeriesOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickSeriesOut"])
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
    types["HistogramChartSpecIn"] = t.struct(
        {
            "legendPosition": t.string().optional(),
            "series": t.array(t.proxy(renames["HistogramSeriesIn"])).optional(),
            "showItemDividers": t.boolean().optional(),
            "bucketSize": t.number().optional(),
            "outlierPercentile": t.number().optional(),
        }
    ).named(renames["HistogramChartSpecIn"])
    types["HistogramChartSpecOut"] = t.struct(
        {
            "legendPosition": t.string().optional(),
            "series": t.array(t.proxy(renames["HistogramSeriesOut"])).optional(),
            "showItemDividers": t.boolean().optional(),
            "bucketSize": t.number().optional(),
            "outlierPercentile": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramChartSpecOut"])
    types["DataSourceParameterIn"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "namedRangeId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DataSourceParameterIn"])
    types["DataSourceParameterOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "namedRangeId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceParameterOut"])
    types["NamedRangeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "namedRangeId": t.string().optional(),
        }
    ).named(renames["NamedRangeIn"])
    types["NamedRangeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedRangeOut"])
    types["DataSourceRefreshScheduleIn"] = t.struct(
        {
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleIn"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleIn"]
            ).optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleIn"]
            ).optional(),
            "refreshScope": t.string().optional(),
        }
    ).named(renames["DataSourceRefreshScheduleIn"])
    types["DataSourceRefreshScheduleOut"] = t.struct(
        {
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleOut"]
            ).optional(),
            "nextRun": t.proxy(renames["IntervalOut"]).optional(),
            "enabled": t.boolean().optional(),
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleOut"]
            ).optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleOut"]
            ).optional(),
            "refreshScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshScheduleOut"])
    types["CreateDeveloperMetadataRequestIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataRequestIn"])
    types["CreateDeveloperMetadataRequestOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataRequestOut"])
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
    types["UpdateSlicerSpecRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "spec": t.proxy(renames["SlicerSpecIn"]).optional(),
            "slicerId": t.integer().optional(),
        }
    ).named(renames["UpdateSlicerSpecRequestIn"])
    types["UpdateSlicerSpecRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "spec": t.proxy(renames["SlicerSpecOut"]).optional(),
            "slicerId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSlicerSpecRequestOut"])
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
    types["CopyPasteRequestIn"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "pasteOrientation": t.string().optional(),
            "destination": t.proxy(renames["GridRangeIn"]).optional(),
            "pasteType": t.string().optional(),
        }
    ).named(renames["CopyPasteRequestIn"])
    types["CopyPasteRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "pasteOrientation": t.string().optional(),
            "destination": t.proxy(renames["GridRangeOut"]).optional(),
            "pasteType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyPasteRequestOut"])
    types["ChartSourceRangeIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["GridRangeIn"])).optional()}
    ).named(renames["ChartSourceRangeIn"])
    types["ChartSourceRangeOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSourceRangeOut"])
    types["FilterViewIn"] = t.struct(
        {
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "namedRangeId": t.string().optional(),
            "filterViewId": t.integer().optional(),
            "title": t.string().optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
        }
    ).named(renames["FilterViewIn"])
    types["FilterViewOut"] = t.struct(
        {
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "namedRangeId": t.string().optional(),
            "filterViewId": t.integer().optional(),
            "title": t.string().optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterViewOut"])
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
    types["FindReplaceRequestIn"] = t.struct(
        {
            "matchEntireCell": t.boolean().optional(),
            "find": t.string().optional(),
            "searchByRegex": t.boolean().optional(),
            "includeFormulas": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "replacement": t.string().optional(),
            "sheetId": t.integer().optional(),
            "matchCase": t.boolean().optional(),
            "allSheets": t.boolean().optional(),
        }
    ).named(renames["FindReplaceRequestIn"])
    types["FindReplaceRequestOut"] = t.struct(
        {
            "matchEntireCell": t.boolean().optional(),
            "find": t.string().optional(),
            "searchByRegex": t.boolean().optional(),
            "includeFormulas": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "replacement": t.string().optional(),
            "sheetId": t.integer().optional(),
            "matchCase": t.boolean().optional(),
            "allSheets": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceRequestOut"])
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
    types["PasteDataRequestIn"] = t.struct(
        {
            "type": t.string().optional(),
            "coordinate": t.proxy(renames["GridCoordinateIn"]).optional(),
            "html": t.boolean().optional(),
            "delimiter": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["PasteDataRequestIn"])
    types["PasteDataRequestOut"] = t.struct(
        {
            "type": t.string().optional(),
            "coordinate": t.proxy(renames["GridCoordinateOut"]).optional(),
            "html": t.boolean().optional(),
            "delimiter": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasteDataRequestOut"])
    types["DeleteProtectedRangeRequestIn"] = t.struct(
        {"protectedRangeId": t.integer().optional()}
    ).named(renames["DeleteProtectedRangeRequestIn"])
    types["DeleteProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteProtectedRangeRequestOut"])
    types["SearchDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["SearchDeveloperMetadataRequestIn"])
    types["SearchDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDeveloperMetadataRequestOut"])
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
    types["AddDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["AddDimensionGroupRequestIn"])
    types["AddDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDimensionGroupRequestOut"])
    types["GridRangeIn"] = t.struct(
        {
            "startColumnIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startRowIndex": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
            "endRowIndex": t.integer().optional(),
        }
    ).named(renames["GridRangeIn"])
    types["GridRangeOut"] = t.struct(
        {
            "startColumnIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startRowIndex": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
            "endRowIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridRangeOut"])
    types["FindReplaceResponseIn"] = t.struct(
        {
            "formulasChanged": t.integer().optional(),
            "occurrencesChanged": t.integer().optional(),
            "sheetsChanged": t.integer().optional(),
            "valuesChanged": t.integer().optional(),
            "rowsChanged": t.integer().optional(),
        }
    ).named(renames["FindReplaceResponseIn"])
    types["FindReplaceResponseOut"] = t.struct(
        {
            "formulasChanged": t.integer().optional(),
            "occurrencesChanged": t.integer().optional(),
            "sheetsChanged": t.integer().optional(),
            "valuesChanged": t.integer().optional(),
            "rowsChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceResponseOut"])
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
    types["DateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DateTimeRuleIn"]
    )
    types["DateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeRuleOut"])
    types["InterpolationPointIn"] = t.struct(
        {
            "value": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "type": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["InterpolationPointIn"])
    types["InterpolationPointOut"] = t.struct(
        {
            "value": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "type": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InterpolationPointOut"])
    types["BubbleChartSpecIn"] = t.struct(
        {
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "groupIds": t.proxy(renames["ChartDataIn"]).optional(),
            "legendPosition": t.string().optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "bubbleBorderColor": t.proxy(renames["ColorIn"]).optional(),
            "bubbleOpacity": t.number().optional(),
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleSizes": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatIn"]).optional(),
            "bubbleMaxRadiusSize": t.integer().optional(),
        }
    ).named(renames["BubbleChartSpecIn"])
    types["BubbleChartSpecOut"] = t.struct(
        {
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "groupIds": t.proxy(renames["ChartDataOut"]).optional(),
            "legendPosition": t.string().optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "bubbleBorderColor": t.proxy(renames["ColorOut"]).optional(),
            "bubbleOpacity": t.number().optional(),
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleSizes": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatOut"]).optional(),
            "bubbleMaxRadiusSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BubbleChartSpecOut"])
    types["DuplicateSheetRequestIn"] = t.struct(
        {
            "sourceSheetId": t.integer().optional(),
            "insertSheetIndex": t.integer().optional(),
            "newSheetName": t.string().optional(),
            "newSheetId": t.integer().optional(),
        }
    ).named(renames["DuplicateSheetRequestIn"])
    types["DuplicateSheetRequestOut"] = t.struct(
        {
            "sourceSheetId": t.integer().optional(),
            "insertSheetIndex": t.integer().optional(),
            "newSheetName": t.string().optional(),
            "newSheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetRequestOut"])
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
    types["CellFormatIn"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "verticalAlignment": t.string().optional(),
            "borders": t.proxy(renames["BordersIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "numberFormat": t.proxy(renames["NumberFormatIn"]).optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "textDirection": t.string().optional(),
            "textRotation": t.proxy(renames["TextRotationIn"]).optional(),
            "wrapStrategy": t.string().optional(),
            "padding": t.proxy(renames["PaddingIn"]).optional(),
        }
    ).named(renames["CellFormatIn"])
    types["CellFormatOut"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "verticalAlignment": t.string().optional(),
            "borders": t.proxy(renames["BordersOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "numberFormat": t.proxy(renames["NumberFormatOut"]).optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "textDirection": t.string().optional(),
            "textRotation": t.proxy(renames["TextRotationOut"]).optional(),
            "wrapStrategy": t.string().optional(),
            "padding": t.proxy(renames["PaddingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellFormatOut"])
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
    types["RequestIn"] = t.struct(
        {
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestIn"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestIn"]).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestIn"]).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestIn"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestIn"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestIn"]
            ).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestIn"]
            ).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestIn"]
            ).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestIn"]).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestIn"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestIn"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestIn"]).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestIn"]).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestIn"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestIn"]
            ).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestIn"]).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestIn"]).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestIn"]
            ).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestIn"]).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestIn"]
            ).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestIn"]).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestIn"]).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestIn"]).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestIn"]
            ).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestIn"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartRequestIn"]).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestIn"]
            ).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestIn"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestIn"]).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestIn"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestIn"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestIn"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestIn"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestIn"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestIn"]
            ).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestIn"]
            ).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestIn"]
            ).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestIn"]
            ).optional(),
            "copyPaste": t.proxy(renames["CopyPasteRequestIn"]).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestIn"]
            ).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestIn"]).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestIn"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestIn"]).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestIn"]
            ).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestIn"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestIn"]).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestIn"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestIn"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestIn"]
            ).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestIn"]).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestIn"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestIn"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestIn"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestIn"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestIn"]).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestIn"]).optional(),
            "updateBorders": t.proxy(renames["UpdateBordersRequestIn"]).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestIn"]
            ).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestIn"]
            ).optional(),
            "pasteData": t.proxy(renames["PasteDataRequestIn"]).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestIn"]
            ).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestIn"]).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestIn"]).optional(),
            "updateBanding": t.proxy(renames["UpdateBandingRequestIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestOut"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestOut"]).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestOut"]).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestOut"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestOut"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestOut"]
            ).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestOut"]
            ).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestOut"]
            ).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestOut"]).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestOut"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestOut"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestOut"]).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestOut"]).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestOut"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestOut"]
            ).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestOut"]).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestOut"]).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestOut"]
            ).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestOut"]).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestOut"]
            ).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestOut"]).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestOut"]).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestOut"]).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestOut"]
            ).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestOut"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartRequestOut"]).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestOut"]
            ).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestOut"]).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestOut"]).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestOut"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestOut"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestOut"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestOut"]
            ).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestOut"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestOut"]
            ).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestOut"]
            ).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestOut"]
            ).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestOut"]
            ).optional(),
            "copyPaste": t.proxy(renames["CopyPasteRequestOut"]).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestOut"]
            ).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestOut"]).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestOut"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestOut"]).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestOut"]
            ).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestOut"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestOut"]).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestOut"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestOut"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestOut"]
            ).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestOut"]).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestOut"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestOut"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestOut"]
            ).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestOut"]
            ).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestOut"]).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestOut"]).optional(),
            "updateBorders": t.proxy(renames["UpdateBordersRequestOut"]).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestOut"]
            ).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestOut"]
            ).optional(),
            "pasteData": t.proxy(renames["PasteDataRequestOut"]).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestOut"]
            ).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestOut"]).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestOut"]).optional(),
            "updateBanding": t.proxy(renames["UpdateBandingRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["AddProtectedRangeRequestIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeRequestIn"])
    types["AddProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeRequestOut"])
    types["SheetIn"] = t.struct(
        {
            "columnGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "protectedRanges": t.array(t.proxy(renames["ProtectedRangeIn"])).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartIn"])).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleIn"])
            ).optional(),
            "bandedRanges": t.array(t.proxy(renames["BandedRangeIn"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "data": t.array(t.proxy(renames["GridDataIn"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterIn"]).optional(),
            "properties": t.proxy(renames["SheetPropertiesIn"]).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewIn"])).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "merges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "slicers": t.array(t.proxy(renames["SlicerIn"])).optional(),
        }
    ).named(renames["SheetIn"])
    types["SheetOut"] = t.struct(
        {
            "columnGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "protectedRanges": t.array(
                t.proxy(renames["ProtectedRangeOut"])
            ).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartOut"])).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleOut"])
            ).optional(),
            "bandedRanges": t.array(t.proxy(renames["BandedRangeOut"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "data": t.array(t.proxy(renames["GridDataOut"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterOut"]).optional(),
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewOut"])).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "merges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "slicers": t.array(t.proxy(renames["SlicerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetOut"])
    types["DimensionRangeIn"] = t.struct(
        {
            "endIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["DimensionRangeIn"])
    types["DimensionRangeOut"] = t.struct(
        {
            "endIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionRangeOut"])
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
    types["AppendCellsRequestIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "fields": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowDataIn"])).optional(),
        }
    ).named(renames["AppendCellsRequestIn"])
    types["AppendCellsRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "fields": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendCellsRequestOut"])
    types["RowDataIn"] = t.struct(
        {"values": t.array(t.proxy(renames["CellDataIn"])).optional()}
    ).named(renames["RowDataIn"])
    types["RowDataOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CellDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowDataOut"])
    types["BandingPropertiesIn"] = t.struct(
        {
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "firstBandColor": t.proxy(renames["ColorIn"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "secondBandColor": t.proxy(renames["ColorIn"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "footerColor": t.proxy(renames["ColorIn"]).optional(),
            "firstBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BandingPropertiesIn"])
    types["BandingPropertiesOut"] = t.struct(
        {
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "firstBandColor": t.proxy(renames["ColorOut"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "secondBandColor": t.proxy(renames["ColorOut"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "footerColor": t.proxy(renames["ColorOut"]).optional(),
            "firstBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandingPropertiesOut"])
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
    types["BasicChartSeriesIn"] = t.struct(
        {
            "type": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "lineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideIn"])
            ).optional(),
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "targetAxis": t.string().optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["BasicChartSeriesIn"])
    types["BasicChartSeriesOut"] = t.struct(
        {
            "type": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "lineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideOut"])
            ).optional(),
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "targetAxis": t.string().optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSeriesOut"])
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
    types["BatchUpdateValuesRequestIn"] = t.struct(
        {
            "responseDateTimeRenderOption": t.string().optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
            "responseValueRenderOption": t.string().optional(),
            "valueInputOption": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesRequestIn"])
    types["BatchUpdateValuesRequestOut"] = t.struct(
        {
            "responseDateTimeRenderOption": t.string().optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "data": t.array(t.proxy(renames["ValueRangeOut"])).optional(),
            "responseValueRenderOption": t.string().optional(),
            "valueInputOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesRequestOut"])
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
    types["SpreadsheetPropertiesIn"] = t.struct(
        {
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsIn"]
            ).optional(),
            "autoRecalc": t.string().optional(),
            "defaultFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "timeZone": t.string().optional(),
            "locale": t.string().optional(),
            "title": t.string().optional(),
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeIn"]).optional(),
        }
    ).named(renames["SpreadsheetPropertiesIn"])
    types["SpreadsheetPropertiesOut"] = t.struct(
        {
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsOut"]
            ).optional(),
            "autoRecalc": t.string().optional(),
            "defaultFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "timeZone": t.string().optional(),
            "locale": t.string().optional(),
            "title": t.string().optional(),
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetPropertiesOut"])
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
    types["ScorecardChartSpecIn"] = t.struct(
        {
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsIn"]
            ).optional(),
            "keyValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "aggregateType": t.string().optional(),
            "numberFormatSource": t.string().optional(),
            "scaleFactor": t.number().optional(),
            "baselineValueFormat": t.proxy(renames["BaselineValueFormatIn"]).optional(),
            "baselineValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "keyValueFormat": t.proxy(renames["KeyValueFormatIn"]).optional(),
        }
    ).named(renames["ScorecardChartSpecIn"])
    types["ScorecardChartSpecOut"] = t.struct(
        {
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsOut"]
            ).optional(),
            "keyValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "aggregateType": t.string().optional(),
            "numberFormatSource": t.string().optional(),
            "scaleFactor": t.number().optional(),
            "baselineValueFormat": t.proxy(
                renames["BaselineValueFormatOut"]
            ).optional(),
            "baselineValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "keyValueFormat": t.proxy(renames["KeyValueFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScorecardChartSpecOut"])
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
    types["DataSourceRefreshDailyScheduleIn"] = t.struct(
        {"startTime": t.proxy(renames["TimeOfDayIn"]).optional()}
    ).named(renames["DataSourceRefreshDailyScheduleIn"])
    types["DataSourceRefreshDailyScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshDailyScheduleOut"])
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
    types["CandlestickDataIn"] = t.struct(
        {
            "openSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "highSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "lowSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
        }
    ).named(renames["CandlestickDataIn"])
    types["CandlestickDataOut"] = t.struct(
        {
            "openSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "highSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "lowSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickDataOut"])
    types["AppendDimensionRequestIn"] = t.struct(
        {
            "dimension": t.string().optional(),
            "length": t.integer().optional(),
            "sheetId": t.integer().optional(),
        }
    ).named(renames["AppendDimensionRequestIn"])
    types["AppendDimensionRequestOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "length": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendDimensionRequestOut"])
    types["BandedRangeIn"] = t.struct(
        {
            "columnProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "rowProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
            "bandedRangeId": t.integer().optional(),
        }
    ).named(renames["BandedRangeIn"])
    types["BandedRangeOut"] = t.struct(
        {
            "columnProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "rowProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "bandedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandedRangeOut"])
    types["DataSourceObjectReferenceIn"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "sheetId": t.string().optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
        }
    ).named(renames["DataSourceObjectReferenceIn"])
    types["DataSourceObjectReferenceOut"] = t.struct(
        {
            "chartId": t.integer().optional(),
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "sheetId": t.string().optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceObjectReferenceOut"])
    types["AddSlicerRequestIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerRequestIn"])
    types["AddSlicerRequestOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerRequestOut"])
    types["DuplicateFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DuplicateFilterViewRequestIn"])
    types["DuplicateFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewRequestOut"])
    types["AddProtectedRangeResponseIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeResponseIn"])
    types["AddProtectedRangeResponseOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeResponseOut"])
    types["PieChartSpecIn"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
            "pieHole": t.number().optional(),
            "legendPosition": t.string().optional(),
            "threeDimensional": t.boolean().optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["PieChartSpecIn"])
    types["PieChartSpecOut"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "pieHole": t.number().optional(),
            "legendPosition": t.string().optional(),
            "threeDimensional": t.boolean().optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PieChartSpecOut"])
    types["LinkIn"] = t.struct({"uri": t.string().optional()}).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["PivotGroupIn"] = t.struct(
        {
            "sourceColumnOffset": t.integer().optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketIn"]).optional(),
            "showTotals": t.boolean().optional(),
            "repeatHeadings": t.boolean().optional(),
            "groupRule": t.proxy(renames["PivotGroupRuleIn"]).optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitIn"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "label": t.string().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataIn"])
            ).optional(),
            "sortOrder": t.string().optional(),
        }
    ).named(renames["PivotGroupIn"])
    types["PivotGroupOut"] = t.struct(
        {
            "sourceColumnOffset": t.integer().optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketOut"]).optional(),
            "showTotals": t.boolean().optional(),
            "repeatHeadings": t.boolean().optional(),
            "groupRule": t.proxy(renames["PivotGroupRuleOut"]).optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitOut"]).optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "label": t.string().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataOut"])
            ).optional(),
            "sortOrder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupOut"])
    types["AddBandingRequestIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingRequestIn"])
    types["AddBandingRequestOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingRequestOut"])
    types["AddNamedRangeRequestIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeRequestIn"])
    types["AddNamedRangeRequestOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeRequestOut"])
    types["RefreshDataSourceRequestIn"] = t.struct(
        {
            "references": t.proxy(renames["DataSourceObjectReferencesIn"]).optional(),
            "force": t.boolean().optional(),
            "isAll": t.boolean().optional(),
            "dataSourceId": t.string().optional(),
        }
    ).named(renames["RefreshDataSourceRequestIn"])
    types["RefreshDataSourceRequestOut"] = t.struct(
        {
            "references": t.proxy(renames["DataSourceObjectReferencesOut"]).optional(),
            "force": t.boolean().optional(),
            "isAll": t.boolean().optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshDataSourceRequestOut"])
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
    types["UpdateCellsRequestIn"] = t.struct(
        {
            "start": t.proxy(renames["GridCoordinateIn"]).optional(),
            "rows": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateCellsRequestIn"])
    types["UpdateCellsRequestOut"] = t.struct(
        {
            "start": t.proxy(renames["GridCoordinateOut"]).optional(),
            "rows": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCellsRequestOut"])
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
    types["ClearValuesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClearValuesRequestIn"]
    )
    types["ClearValuesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearValuesRequestOut"])
    types["ChartDateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ChartDateTimeRuleIn"]
    )
    types["ChartDateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDateTimeRuleOut"])
    types["DataValidationRuleIn"] = t.struct(
        {
            "showCustomUi": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "strict": t.boolean().optional(),
            "inputMessage": t.string().optional(),
        }
    ).named(renames["DataValidationRuleIn"])
    types["DataValidationRuleOut"] = t.struct(
        {
            "showCustomUi": t.boolean().optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "strict": t.boolean().optional(),
            "inputMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataValidationRuleOut"])
    types["GradientRuleIn"] = t.struct(
        {
            "minpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
            "midpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
            "maxpoint": t.proxy(renames["InterpolationPointIn"]).optional(),
        }
    ).named(renames["GradientRuleIn"])
    types["GradientRuleOut"] = t.struct(
        {
            "minpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "midpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "maxpoint": t.proxy(renames["InterpolationPointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradientRuleOut"])
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
    types["SheetPropertiesIn"] = t.struct(
        {
            "rightToLeft": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesIn"]).optional(),
            "sheetType": t.string().optional(),
            "tabColor": t.proxy(renames["ColorIn"]).optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "hidden": t.boolean().optional(),
            "title": t.string().optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["SheetPropertiesIn"])
    types["SheetPropertiesOut"] = t.struct(
        {
            "rightToLeft": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesOut"]).optional(),
            "sheetType": t.string().optional(),
            "tabColor": t.proxy(renames["ColorOut"]).optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "hidden": t.boolean().optional(),
            "title": t.string().optional(),
            "dataSourceSheetProperties": t.proxy(
                renames["DataSourceSheetPropertiesOut"]
            ).optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetPropertiesOut"])
    types["OrgChartSpecIn"] = t.struct(
        {
            "tooltips": t.proxy(renames["ChartDataIn"]).optional(),
            "nodeSize": t.string().optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "nodeColor": t.proxy(renames["ColorIn"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "selectedNodeColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["OrgChartSpecIn"])
    types["OrgChartSpecOut"] = t.struct(
        {
            "tooltips": t.proxy(renames["ChartDataOut"]).optional(),
            "nodeSize": t.string().optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "nodeColor": t.proxy(renames["ColorOut"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "selectedNodeColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgChartSpecOut"])
    types["GridPropertiesIn"] = t.struct(
        {
            "frozenRowCount": t.integer().optional(),
            "frozenColumnCount": t.integer().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
            "rowCount": t.integer().optional(),
            "rowGroupControlAfter": t.boolean().optional(),
            "columnCount": t.integer().optional(),
            "hideGridlines": t.boolean().optional(),
        }
    ).named(renames["GridPropertiesIn"])
    types["GridPropertiesOut"] = t.struct(
        {
            "frozenRowCount": t.integer().optional(),
            "frozenColumnCount": t.integer().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
            "rowCount": t.integer().optional(),
            "rowGroupControlAfter": t.boolean().optional(),
            "columnCount": t.integer().optional(),
            "hideGridlines": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridPropertiesOut"])
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
    types["BatchUpdateValuesResponseIn"] = t.struct(
        {
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(t.proxy(renames["UpdateValuesResponseIn"])).optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesResponseIn"])
    types["BatchUpdateValuesResponseOut"] = t.struct(
        {
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesResponseOut"])
            ).optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesResponseOut"])
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
    types["BatchUpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "totalUpdatedRows": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseIn"])
            ).optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "totalUpdatedCells": t.integer().optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseIn"])
    types["BatchUpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "totalUpdatedRows": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseOut"])
            ).optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseOut"])
    types["UpdateValuesResponseIn"] = t.struct(
        {
            "updatedColumns": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedCells": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
        }
    ).named(renames["UpdateValuesResponseIn"])
    types["UpdateValuesResponseOut"] = t.struct(
        {
            "updatedColumns": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedCells": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesResponseOut"])
    types["UpdateDimensionPropertiesRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
            "properties": t.proxy(renames["DimensionPropertiesIn"]).optional(),
            "fields": t.string().optional(),
            "dataSourceSheetRange": t.proxy(
                renames["DataSourceSheetDimensionRangeIn"]
            ).optional(),
        }
    ).named(renames["UpdateDimensionPropertiesRequestIn"])
    types["UpdateDimensionPropertiesRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "properties": t.proxy(renames["DimensionPropertiesOut"]).optional(),
            "fields": t.string().optional(),
            "dataSourceSheetRange": t.proxy(
                renames["DataSourceSheetDimensionRangeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDimensionPropertiesRequestOut"])
    types["CellDataIn"] = t.struct(
        {
            "note": t.string().optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "userEnteredValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableIn"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableIn"]).optional(),
            "hyperlink": t.string().optional(),
            "dataValidation": t.proxy(renames["DataValidationRuleIn"]).optional(),
            "formattedValue": t.string().optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunIn"])).optional(),
            "effectiveValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "effectiveFormat": t.proxy(renames["CellFormatIn"]).optional(),
        }
    ).named(renames["CellDataIn"])
    types["CellDataOut"] = t.struct(
        {
            "note": t.string().optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "userEnteredValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableOut"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableOut"]).optional(),
            "hyperlink": t.string().optional(),
            "dataSourceFormula": t.proxy(renames["DataSourceFormulaOut"]).optional(),
            "dataValidation": t.proxy(renames["DataValidationRuleOut"]).optional(),
            "formattedValue": t.string().optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunOut"])).optional(),
            "effectiveValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "effectiveFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellDataOut"])
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
    types["BatchUpdateValuesByDataFilterRequestIn"] = t.struct(
        {
            "includeValuesInResponse": t.boolean().optional(),
            "valueInputOption": t.string().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
            "data": t.array(t.proxy(renames["DataFilterValueRangeIn"])).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestIn"])
    types["BatchUpdateValuesByDataFilterRequestOut"] = t.struct(
        {
            "includeValuesInResponse": t.boolean().optional(),
            "valueInputOption": t.string().optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
            "data": t.array(t.proxy(renames["DataFilterValueRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestOut"])
    types["BasicSeriesDataPointStyleOverrideIn"] = t.struct(
        {
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "index": t.integer().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideIn"])
    types["BasicSeriesDataPointStyleOverrideOut"] = t.struct(
        {
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "index": t.integer().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideOut"])
    types["GridCoordinateIn"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "columnIndex": t.integer().optional(),
        }
    ).named(renames["GridCoordinateIn"])
    types["GridCoordinateOut"] = t.struct(
        {
            "rowIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "columnIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridCoordinateOut"])
    types["BatchClearValuesRequestIn"] = t.struct(
        {"ranges": t.array(t.string()).optional()}
    ).named(renames["BatchClearValuesRequestIn"])
    types["BatchClearValuesRequestOut"] = t.struct(
        {
            "ranges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesRequestOut"])
    types["FilterSpecIn"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "columnIndex": t.integer().optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
        }
    ).named(renames["FilterSpecIn"])
    types["FilterSpecOut"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "columnIndex": t.integer().optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterSpecOut"])
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
    types["BaselineValueFormatIn"] = t.struct(
        {
            "positiveColor": t.proxy(renames["ColorIn"]).optional(),
            "comparisonType": t.string().optional(),
            "position": t.proxy(renames["TextPositionIn"]).optional(),
            "description": t.string().optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "negativeColor": t.proxy(renames["ColorIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BaselineValueFormatIn"])
    types["BaselineValueFormatOut"] = t.struct(
        {
            "positiveColor": t.proxy(renames["ColorOut"]).optional(),
            "comparisonType": t.string().optional(),
            "position": t.proxy(renames["TextPositionOut"]).optional(),
            "description": t.string().optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "negativeColor": t.proxy(renames["ColorOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BaselineValueFormatOut"])
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
    types["DeleteDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionGroupRequestIn"])
    types["DeleteDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionGroupRequestOut"])
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
    types["DuplicateFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["DuplicateFilterViewResponseIn"])
    types["DuplicateFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewResponseOut"])
    types["EmbeddedChartIn"] = t.struct(
        {
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
            "spec": t.proxy(renames["ChartSpecIn"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "chartId": t.integer().optional(),
        }
    ).named(renames["EmbeddedChartIn"])
    types["EmbeddedChartOut"] = t.struct(
        {
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "spec": t.proxy(renames["ChartSpecOut"]).optional(),
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "chartId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedChartOut"])
    types["BatchClearValuesByDataFilterRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["BatchClearValuesByDataFilterRequestIn"])
    types["BatchClearValuesByDataFilterRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterRequestOut"])

    functions = {}
    functions["spreadsheetsBatchUpdate"] = sheets.post(
        "v4/spreadsheets",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
                "spreadsheetUrl": t.string().optional(),
                "developerMetadata": t.array(
                    t.proxy(renames["DeveloperMetadataIn"])
                ).optional(),
                "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
                "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
                "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsGetByDataFilter"] = sheets.post(
        "v4/spreadsheets",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
                "spreadsheetUrl": t.string().optional(),
                "developerMetadata": t.array(
                    t.proxy(renames["DeveloperMetadataIn"])
                ).optional(),
                "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
                "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
                "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsGet"] = sheets.post(
        "v4/spreadsheets",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
                "spreadsheetUrl": t.string().optional(),
                "developerMetadata": t.array(
                    t.proxy(renames["DeveloperMetadataIn"])
                ).optional(),
                "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
                "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
                "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsCreate"] = sheets.post(
        "v4/spreadsheets",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
                "spreadsheetUrl": t.string().optional(),
                "developerMetadata": t.array(
                    t.proxy(renames["DeveloperMetadataIn"])
                ).optional(),
                "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
                "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
                "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesAppend"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchClearByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesUpdate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchClear"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesClear"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchGetByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchUpdateByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsValuesBatchUpdate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}/values:batchUpdate",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "responseDateTimeRenderOption": t.string().optional(),
                "includeValuesInResponse": t.boolean().optional(),
                "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
                "responseValueRenderOption": t.string().optional(),
                "valueInputOption": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateValuesResponseOut"]),
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

    return Import(
        importer="sheets", renames=renames, types=Box(types), functions=Box(functions)
    )
