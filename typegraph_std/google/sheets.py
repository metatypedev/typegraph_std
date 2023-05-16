from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_sheets() -> Import:
    sheets = HTTPRuntime("https://sheets.googleapis.com/")

    renames = {
        "ErrorResponse": "_sheets_1_ErrorResponse",
        "EmbeddedObjectPositionIn": "_sheets_2_EmbeddedObjectPositionIn",
        "EmbeddedObjectPositionOut": "_sheets_3_EmbeddedObjectPositionOut",
        "UpdateDeveloperMetadataResponseIn": "_sheets_4_UpdateDeveloperMetadataResponseIn",
        "UpdateDeveloperMetadataResponseOut": "_sheets_5_UpdateDeveloperMetadataResponseOut",
        "BigQueryTableSpecIn": "_sheets_6_BigQueryTableSpecIn",
        "BigQueryTableSpecOut": "_sheets_7_BigQueryTableSpecOut",
        "UpdateDataSourceResponseIn": "_sheets_8_UpdateDataSourceResponseIn",
        "UpdateDataSourceResponseOut": "_sheets_9_UpdateDataSourceResponseOut",
        "BigQueryDataSourceSpecIn": "_sheets_10_BigQueryDataSourceSpecIn",
        "BigQueryDataSourceSpecOut": "_sheets_11_BigQueryDataSourceSpecOut",
        "BaselineValueFormatIn": "_sheets_12_BaselineValueFormatIn",
        "BaselineValueFormatOut": "_sheets_13_BaselineValueFormatOut",
        "DataSourceSheetPropertiesIn": "_sheets_14_DataSourceSheetPropertiesIn",
        "DataSourceSheetPropertiesOut": "_sheets_15_DataSourceSheetPropertiesOut",
        "DeleteRangeRequestIn": "_sheets_16_DeleteRangeRequestIn",
        "DeleteRangeRequestOut": "_sheets_17_DeleteRangeRequestOut",
        "AddBandingResponseIn": "_sheets_18_AddBandingResponseIn",
        "AddBandingResponseOut": "_sheets_19_AddBandingResponseOut",
        "UpdateDimensionPropertiesRequestIn": "_sheets_20_UpdateDimensionPropertiesRequestIn",
        "UpdateDimensionPropertiesRequestOut": "_sheets_21_UpdateDimensionPropertiesRequestOut",
        "ProtectedRangeIn": "_sheets_22_ProtectedRangeIn",
        "ProtectedRangeOut": "_sheets_23_ProtectedRangeOut",
        "UpdateSheetPropertiesRequestIn": "_sheets_24_UpdateSheetPropertiesRequestIn",
        "UpdateSheetPropertiesRequestOut": "_sheets_25_UpdateSheetPropertiesRequestOut",
        "ManualRuleGroupIn": "_sheets_26_ManualRuleGroupIn",
        "ManualRuleGroupOut": "_sheets_27_ManualRuleGroupOut",
        "DeleteConditionalFormatRuleRequestIn": "_sheets_28_DeleteConditionalFormatRuleRequestIn",
        "DeleteConditionalFormatRuleRequestOut": "_sheets_29_DeleteConditionalFormatRuleRequestOut",
        "UpdateEmbeddedObjectPositionRequestIn": "_sheets_30_UpdateEmbeddedObjectPositionRequestIn",
        "UpdateEmbeddedObjectPositionRequestOut": "_sheets_31_UpdateEmbeddedObjectPositionRequestOut",
        "GridPropertiesIn": "_sheets_32_GridPropertiesIn",
        "GridPropertiesOut": "_sheets_33_GridPropertiesOut",
        "SourceAndDestinationIn": "_sheets_34_SourceAndDestinationIn",
        "SourceAndDestinationOut": "_sheets_35_SourceAndDestinationOut",
        "TrimWhitespaceRequestIn": "_sheets_36_TrimWhitespaceRequestIn",
        "TrimWhitespaceRequestOut": "_sheets_37_TrimWhitespaceRequestOut",
        "PivotGroupLimitIn": "_sheets_38_PivotGroupLimitIn",
        "PivotGroupLimitOut": "_sheets_39_PivotGroupLimitOut",
        "BatchUpdateSpreadsheetRequestIn": "_sheets_40_BatchUpdateSpreadsheetRequestIn",
        "BatchUpdateSpreadsheetRequestOut": "_sheets_41_BatchUpdateSpreadsheetRequestOut",
        "DeleteEmbeddedObjectRequestIn": "_sheets_42_DeleteEmbeddedObjectRequestIn",
        "DeleteEmbeddedObjectRequestOut": "_sheets_43_DeleteEmbeddedObjectRequestOut",
        "SpreadsheetThemeIn": "_sheets_44_SpreadsheetThemeIn",
        "SpreadsheetThemeOut": "_sheets_45_SpreadsheetThemeOut",
        "AddSlicerRequestIn": "_sheets_46_AddSlicerRequestIn",
        "AddSlicerRequestOut": "_sheets_47_AddSlicerRequestOut",
        "DeleteDimensionRequestIn": "_sheets_48_DeleteDimensionRequestIn",
        "DeleteDimensionRequestOut": "_sheets_49_DeleteDimensionRequestOut",
        "AddChartResponseIn": "_sheets_50_AddChartResponseIn",
        "AddChartResponseOut": "_sheets_51_AddChartResponseOut",
        "ResponseIn": "_sheets_52_ResponseIn",
        "ResponseOut": "_sheets_53_ResponseOut",
        "DataSourceRefreshMonthlyScheduleIn": "_sheets_54_DataSourceRefreshMonthlyScheduleIn",
        "DataSourceRefreshMonthlyScheduleOut": "_sheets_55_DataSourceRefreshMonthlyScheduleOut",
        "ConditionalFormatRuleIn": "_sheets_56_ConditionalFormatRuleIn",
        "ConditionalFormatRuleOut": "_sheets_57_ConditionalFormatRuleOut",
        "DataSourceObjectReferencesIn": "_sheets_58_DataSourceObjectReferencesIn",
        "DataSourceObjectReferencesOut": "_sheets_59_DataSourceObjectReferencesOut",
        "HistogramChartSpecIn": "_sheets_60_HistogramChartSpecIn",
        "HistogramChartSpecOut": "_sheets_61_HistogramChartSpecOut",
        "LinkIn": "_sheets_62_LinkIn",
        "LinkOut": "_sheets_63_LinkOut",
        "AddBandingRequestIn": "_sheets_64_AddBandingRequestIn",
        "AddBandingRequestOut": "_sheets_65_AddBandingRequestOut",
        "GetSpreadsheetByDataFilterRequestIn": "_sheets_66_GetSpreadsheetByDataFilterRequestIn",
        "GetSpreadsheetByDataFilterRequestOut": "_sheets_67_GetSpreadsheetByDataFilterRequestOut",
        "WaterfallChartSpecIn": "_sheets_68_WaterfallChartSpecIn",
        "WaterfallChartSpecOut": "_sheets_69_WaterfallChartSpecOut",
        "DeveloperMetadataIn": "_sheets_70_DeveloperMetadataIn",
        "DeveloperMetadataOut": "_sheets_71_DeveloperMetadataOut",
        "ManualRuleIn": "_sheets_72_ManualRuleIn",
        "ManualRuleOut": "_sheets_73_ManualRuleOut",
        "SheetIn": "_sheets_74_SheetIn",
        "SheetOut": "_sheets_75_SheetOut",
        "DeleteDeveloperMetadataResponseIn": "_sheets_76_DeleteDeveloperMetadataResponseIn",
        "DeleteDeveloperMetadataResponseOut": "_sheets_77_DeleteDeveloperMetadataResponseOut",
        "WaterfallChartDomainIn": "_sheets_78_WaterfallChartDomainIn",
        "WaterfallChartDomainOut": "_sheets_79_WaterfallChartDomainOut",
        "AddNamedRangeResponseIn": "_sheets_80_AddNamedRangeResponseIn",
        "AddNamedRangeResponseOut": "_sheets_81_AddNamedRangeResponseOut",
        "DataSourceTableIn": "_sheets_82_DataSourceTableIn",
        "DataSourceTableOut": "_sheets_83_DataSourceTableOut",
        "DataSourceColumnIn": "_sheets_84_DataSourceColumnIn",
        "DataSourceColumnOut": "_sheets_85_DataSourceColumnOut",
        "DataSourceRefreshDailyScheduleIn": "_sheets_86_DataSourceRefreshDailyScheduleIn",
        "DataSourceRefreshDailyScheduleOut": "_sheets_87_DataSourceRefreshDailyScheduleOut",
        "UpdateBordersRequestIn": "_sheets_88_UpdateBordersRequestIn",
        "UpdateBordersRequestOut": "_sheets_89_UpdateBordersRequestOut",
        "PasteDataRequestIn": "_sheets_90_PasteDataRequestIn",
        "PasteDataRequestOut": "_sheets_91_PasteDataRequestOut",
        "DeleteFilterViewRequestIn": "_sheets_92_DeleteFilterViewRequestIn",
        "DeleteFilterViewRequestOut": "_sheets_93_DeleteFilterViewRequestOut",
        "BasicChartDomainIn": "_sheets_94_BasicChartDomainIn",
        "BasicChartDomainOut": "_sheets_95_BasicChartDomainOut",
        "ClearValuesResponseIn": "_sheets_96_ClearValuesResponseIn",
        "ClearValuesResponseOut": "_sheets_97_ClearValuesResponseOut",
        "DataSourceSheetDimensionRangeIn": "_sheets_98_DataSourceSheetDimensionRangeIn",
        "DataSourceSheetDimensionRangeOut": "_sheets_99_DataSourceSheetDimensionRangeOut",
        "CopySheetToAnotherSpreadsheetRequestIn": "_sheets_100_CopySheetToAnotherSpreadsheetRequestIn",
        "CopySheetToAnotherSpreadsheetRequestOut": "_sheets_101_CopySheetToAnotherSpreadsheetRequestOut",
        "UpdateBandingRequestIn": "_sheets_102_UpdateBandingRequestIn",
        "UpdateBandingRequestOut": "_sheets_103_UpdateBandingRequestOut",
        "BooleanConditionIn": "_sheets_104_BooleanConditionIn",
        "BooleanConditionOut": "_sheets_105_BooleanConditionOut",
        "BatchUpdateValuesByDataFilterRequestIn": "_sheets_106_BatchUpdateValuesByDataFilterRequestIn",
        "BatchUpdateValuesByDataFilterRequestOut": "_sheets_107_BatchUpdateValuesByDataFilterRequestOut",
        "InterpolationPointIn": "_sheets_108_InterpolationPointIn",
        "InterpolationPointOut": "_sheets_109_InterpolationPointOut",
        "SlicerIn": "_sheets_110_SlicerIn",
        "SlicerOut": "_sheets_111_SlicerOut",
        "GridCoordinateIn": "_sheets_112_GridCoordinateIn",
        "GridCoordinateOut": "_sheets_113_GridCoordinateOut",
        "EditorsIn": "_sheets_114_EditorsIn",
        "EditorsOut": "_sheets_115_EditorsOut",
        "ClearValuesRequestIn": "_sheets_116_ClearValuesRequestIn",
        "ClearValuesRequestOut": "_sheets_117_ClearValuesRequestOut",
        "BigQueryQuerySpecIn": "_sheets_118_BigQueryQuerySpecIn",
        "BigQueryQuerySpecOut": "_sheets_119_BigQueryQuerySpecOut",
        "MatchedDeveloperMetadataIn": "_sheets_120_MatchedDeveloperMetadataIn",
        "MatchedDeveloperMetadataOut": "_sheets_121_MatchedDeveloperMetadataOut",
        "UpdateProtectedRangeRequestIn": "_sheets_122_UpdateProtectedRangeRequestIn",
        "UpdateProtectedRangeRequestOut": "_sheets_123_UpdateProtectedRangeRequestOut",
        "PieChartSpecIn": "_sheets_124_PieChartSpecIn",
        "PieChartSpecOut": "_sheets_125_PieChartSpecOut",
        "BandingPropertiesIn": "_sheets_126_BandingPropertiesIn",
        "BandingPropertiesOut": "_sheets_127_BandingPropertiesOut",
        "ScorecardChartSpecIn": "_sheets_128_ScorecardChartSpecIn",
        "ScorecardChartSpecOut": "_sheets_129_ScorecardChartSpecOut",
        "FilterCriteriaIn": "_sheets_130_FilterCriteriaIn",
        "FilterCriteriaOut": "_sheets_131_FilterCriteriaOut",
        "OverlayPositionIn": "_sheets_132_OverlayPositionIn",
        "OverlayPositionOut": "_sheets_133_OverlayPositionOut",
        "UpdateFilterViewRequestIn": "_sheets_134_UpdateFilterViewRequestIn",
        "UpdateFilterViewRequestOut": "_sheets_135_UpdateFilterViewRequestOut",
        "AppendValuesResponseIn": "_sheets_136_AppendValuesResponseIn",
        "AppendValuesResponseOut": "_sheets_137_AppendValuesResponseOut",
        "DimensionGroupIn": "_sheets_138_DimensionGroupIn",
        "DimensionGroupOut": "_sheets_139_DimensionGroupOut",
        "CandlestickDataIn": "_sheets_140_CandlestickDataIn",
        "CandlestickDataOut": "_sheets_141_CandlestickDataOut",
        "UnmergeCellsRequestIn": "_sheets_142_UnmergeCellsRequestIn",
        "UnmergeCellsRequestOut": "_sheets_143_UnmergeCellsRequestOut",
        "UpdateDimensionGroupRequestIn": "_sheets_144_UpdateDimensionGroupRequestIn",
        "UpdateDimensionGroupRequestOut": "_sheets_145_UpdateDimensionGroupRequestOut",
        "BooleanRuleIn": "_sheets_146_BooleanRuleIn",
        "BooleanRuleOut": "_sheets_147_BooleanRuleOut",
        "WaterfallChartColumnStyleIn": "_sheets_148_WaterfallChartColumnStyleIn",
        "WaterfallChartColumnStyleOut": "_sheets_149_WaterfallChartColumnStyleOut",
        "DataSourceChartPropertiesIn": "_sheets_150_DataSourceChartPropertiesIn",
        "DataSourceChartPropertiesOut": "_sheets_151_DataSourceChartPropertiesOut",
        "DeveloperMetadataLookupIn": "_sheets_152_DeveloperMetadataLookupIn",
        "DeveloperMetadataLookupOut": "_sheets_153_DeveloperMetadataLookupOut",
        "SlicerSpecIn": "_sheets_154_SlicerSpecIn",
        "SlicerSpecOut": "_sheets_155_SlicerSpecOut",
        "ErrorValueIn": "_sheets_156_ErrorValueIn",
        "ErrorValueOut": "_sheets_157_ErrorValueOut",
        "BasicFilterIn": "_sheets_158_BasicFilterIn",
        "BasicFilterOut": "_sheets_159_BasicFilterOut",
        "AddNamedRangeRequestIn": "_sheets_160_AddNamedRangeRequestIn",
        "AddNamedRangeRequestOut": "_sheets_161_AddNamedRangeRequestOut",
        "InsertRangeRequestIn": "_sheets_162_InsertRangeRequestIn",
        "InsertRangeRequestOut": "_sheets_163_InsertRangeRequestOut",
        "DataExecutionStatusIn": "_sheets_164_DataExecutionStatusIn",
        "DataExecutionStatusOut": "_sheets_165_DataExecutionStatusOut",
        "BatchClearValuesRequestIn": "_sheets_166_BatchClearValuesRequestIn",
        "BatchClearValuesRequestOut": "_sheets_167_BatchClearValuesRequestOut",
        "BatchGetValuesByDataFilterRequestIn": "_sheets_168_BatchGetValuesByDataFilterRequestIn",
        "BatchGetValuesByDataFilterRequestOut": "_sheets_169_BatchGetValuesByDataFilterRequestOut",
        "AddDimensionGroupRequestIn": "_sheets_170_AddDimensionGroupRequestIn",
        "AddDimensionGroupRequestOut": "_sheets_171_AddDimensionGroupRequestOut",
        "AddSheetRequestIn": "_sheets_172_AddSheetRequestIn",
        "AddSheetRequestOut": "_sheets_173_AddSheetRequestOut",
        "DeleteDataSourceRequestIn": "_sheets_174_DeleteDataSourceRequestIn",
        "DeleteDataSourceRequestOut": "_sheets_175_DeleteDataSourceRequestOut",
        "TextFormatIn": "_sheets_176_TextFormatIn",
        "TextFormatOut": "_sheets_177_TextFormatOut",
        "PivotGroupValueMetadataIn": "_sheets_178_PivotGroupValueMetadataIn",
        "PivotGroupValueMetadataOut": "_sheets_179_PivotGroupValueMetadataOut",
        "NumberFormatIn": "_sheets_180_NumberFormatIn",
        "NumberFormatOut": "_sheets_181_NumberFormatOut",
        "DataSourceRefreshScheduleIn": "_sheets_182_DataSourceRefreshScheduleIn",
        "DataSourceRefreshScheduleOut": "_sheets_183_DataSourceRefreshScheduleOut",
        "DataSourceObjectReferenceIn": "_sheets_184_DataSourceObjectReferenceIn",
        "DataSourceObjectReferenceOut": "_sheets_185_DataSourceObjectReferenceOut",
        "UpdateDataSourceRequestIn": "_sheets_186_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_sheets_187_UpdateDataSourceRequestOut",
        "PointStyleIn": "_sheets_188_PointStyleIn",
        "PointStyleOut": "_sheets_189_PointStyleOut",
        "AddFilterViewResponseIn": "_sheets_190_AddFilterViewResponseIn",
        "AddFilterViewResponseOut": "_sheets_191_AddFilterViewResponseOut",
        "RepeatCellRequestIn": "_sheets_192_RepeatCellRequestIn",
        "RepeatCellRequestOut": "_sheets_193_RepeatCellRequestOut",
        "ChartDataIn": "_sheets_194_ChartDataIn",
        "ChartDataOut": "_sheets_195_ChartDataOut",
        "DeleteDuplicatesRequestIn": "_sheets_196_DeleteDuplicatesRequestIn",
        "DeleteDuplicatesRequestOut": "_sheets_197_DeleteDuplicatesRequestOut",
        "CopyPasteRequestIn": "_sheets_198_CopyPasteRequestIn",
        "CopyPasteRequestOut": "_sheets_199_CopyPasteRequestOut",
        "ConditionValueIn": "_sheets_200_ConditionValueIn",
        "ConditionValueOut": "_sheets_201_ConditionValueOut",
        "SortSpecIn": "_sheets_202_SortSpecIn",
        "SortSpecOut": "_sheets_203_SortSpecOut",
        "PivotGroupRuleIn": "_sheets_204_PivotGroupRuleIn",
        "PivotGroupRuleOut": "_sheets_205_PivotGroupRuleOut",
        "DataLabelIn": "_sheets_206_DataLabelIn",
        "DataLabelOut": "_sheets_207_DataLabelOut",
        "BasicChartSpecIn": "_sheets_208_BasicChartSpecIn",
        "BasicChartSpecOut": "_sheets_209_BasicChartSpecOut",
        "BatchClearValuesResponseIn": "_sheets_210_BatchClearValuesResponseIn",
        "BatchClearValuesResponseOut": "_sheets_211_BatchClearValuesResponseOut",
        "MatchedValueRangeIn": "_sheets_212_MatchedValueRangeIn",
        "MatchedValueRangeOut": "_sheets_213_MatchedValueRangeOut",
        "MoveDimensionRequestIn": "_sheets_214_MoveDimensionRequestIn",
        "MoveDimensionRequestOut": "_sheets_215_MoveDimensionRequestOut",
        "TextPositionIn": "_sheets_216_TextPositionIn",
        "TextPositionOut": "_sheets_217_TextPositionOut",
        "CandlestickDomainIn": "_sheets_218_CandlestickDomainIn",
        "CandlestickDomainOut": "_sheets_219_CandlestickDomainOut",
        "ColorIn": "_sheets_220_ColorIn",
        "ColorOut": "_sheets_221_ColorOut",
        "AddDataSourceRequestIn": "_sheets_222_AddDataSourceRequestIn",
        "AddDataSourceRequestOut": "_sheets_223_AddDataSourceRequestOut",
        "FilterSpecIn": "_sheets_224_FilterSpecIn",
        "FilterSpecOut": "_sheets_225_FilterSpecOut",
        "UpdateEmbeddedObjectBorderRequestIn": "_sheets_226_UpdateEmbeddedObjectBorderRequestIn",
        "UpdateEmbeddedObjectBorderRequestOut": "_sheets_227_UpdateEmbeddedObjectBorderRequestOut",
        "ChartDateTimeRuleIn": "_sheets_228_ChartDateTimeRuleIn",
        "ChartDateTimeRuleOut": "_sheets_229_ChartDateTimeRuleOut",
        "BorderIn": "_sheets_230_BorderIn",
        "BorderOut": "_sheets_231_BorderOut",
        "AutoFillRequestIn": "_sheets_232_AutoFillRequestIn",
        "AutoFillRequestOut": "_sheets_233_AutoFillRequestOut",
        "PivotGroupIn": "_sheets_234_PivotGroupIn",
        "PivotGroupOut": "_sheets_235_PivotGroupOut",
        "PaddingIn": "_sheets_236_PaddingIn",
        "PaddingOut": "_sheets_237_PaddingOut",
        "PivotTableIn": "_sheets_238_PivotTableIn",
        "PivotTableOut": "_sheets_239_PivotTableOut",
        "SortRangeRequestIn": "_sheets_240_SortRangeRequestIn",
        "SortRangeRequestOut": "_sheets_241_SortRangeRequestOut",
        "DeleteDimensionGroupRequestIn": "_sheets_242_DeleteDimensionGroupRequestIn",
        "DeleteDimensionGroupRequestOut": "_sheets_243_DeleteDimensionGroupRequestOut",
        "DuplicateSheetResponseIn": "_sheets_244_DuplicateSheetResponseIn",
        "DuplicateSheetResponseOut": "_sheets_245_DuplicateSheetResponseOut",
        "DeleteNamedRangeRequestIn": "_sheets_246_DeleteNamedRangeRequestIn",
        "DeleteNamedRangeRequestOut": "_sheets_247_DeleteNamedRangeRequestOut",
        "NamedRangeIn": "_sheets_248_NamedRangeIn",
        "NamedRangeOut": "_sheets_249_NamedRangeOut",
        "DataSourceColumnReferenceIn": "_sheets_250_DataSourceColumnReferenceIn",
        "DataSourceColumnReferenceOut": "_sheets_251_DataSourceColumnReferenceOut",
        "ChartGroupRuleIn": "_sheets_252_ChartGroupRuleIn",
        "ChartGroupRuleOut": "_sheets_253_ChartGroupRuleOut",
        "KeyValueFormatIn": "_sheets_254_KeyValueFormatIn",
        "KeyValueFormatOut": "_sheets_255_KeyValueFormatOut",
        "BatchGetValuesResponseIn": "_sheets_256_BatchGetValuesResponseIn",
        "BatchGetValuesResponseOut": "_sheets_257_BatchGetValuesResponseOut",
        "CellDataIn": "_sheets_258_CellDataIn",
        "CellDataOut": "_sheets_259_CellDataOut",
        "DataSourceSpecIn": "_sheets_260_DataSourceSpecIn",
        "DataSourceSpecOut": "_sheets_261_DataSourceSpecOut",
        "FindReplaceRequestIn": "_sheets_262_FindReplaceRequestIn",
        "FindReplaceRequestOut": "_sheets_263_FindReplaceRequestOut",
        "AddProtectedRangeRequestIn": "_sheets_264_AddProtectedRangeRequestIn",
        "AddProtectedRangeRequestOut": "_sheets_265_AddProtectedRangeRequestOut",
        "DeleteDeveloperMetadataRequestIn": "_sheets_266_DeleteDeveloperMetadataRequestIn",
        "DeleteDeveloperMetadataRequestOut": "_sheets_267_DeleteDeveloperMetadataRequestOut",
        "ExtendedValueIn": "_sheets_268_ExtendedValueIn",
        "ExtendedValueOut": "_sheets_269_ExtendedValueOut",
        "ChartSourceRangeIn": "_sheets_270_ChartSourceRangeIn",
        "ChartSourceRangeOut": "_sheets_271_ChartSourceRangeOut",
        "GridDataIn": "_sheets_272_GridDataIn",
        "GridDataOut": "_sheets_273_GridDataOut",
        "PivotValueIn": "_sheets_274_PivotValueIn",
        "PivotValueOut": "_sheets_275_PivotValueOut",
        "CandlestickSeriesIn": "_sheets_276_CandlestickSeriesIn",
        "CandlestickSeriesOut": "_sheets_277_CandlestickSeriesOut",
        "SheetPropertiesIn": "_sheets_278_SheetPropertiesIn",
        "SheetPropertiesOut": "_sheets_279_SheetPropertiesOut",
        "ThemeColorPairIn": "_sheets_280_ThemeColorPairIn",
        "ThemeColorPairOut": "_sheets_281_ThemeColorPairOut",
        "MergeCellsRequestIn": "_sheets_282_MergeCellsRequestIn",
        "MergeCellsRequestOut": "_sheets_283_MergeCellsRequestOut",
        "ChartSpecIn": "_sheets_284_ChartSpecIn",
        "ChartSpecOut": "_sheets_285_ChartSpecOut",
        "RandomizeRangeRequestIn": "_sheets_286_RandomizeRangeRequestIn",
        "RandomizeRangeRequestOut": "_sheets_287_RandomizeRangeRequestOut",
        "UpdateSlicerSpecRequestIn": "_sheets_288_UpdateSlicerSpecRequestIn",
        "UpdateSlicerSpecRequestOut": "_sheets_289_UpdateSlicerSpecRequestOut",
        "SetBasicFilterRequestIn": "_sheets_290_SetBasicFilterRequestIn",
        "SetBasicFilterRequestOut": "_sheets_291_SetBasicFilterRequestOut",
        "AddProtectedRangeResponseIn": "_sheets_292_AddProtectedRangeResponseIn",
        "AddProtectedRangeResponseOut": "_sheets_293_AddProtectedRangeResponseOut",
        "GradientRuleIn": "_sheets_294_GradientRuleIn",
        "GradientRuleOut": "_sheets_295_GradientRuleOut",
        "DataSourceIn": "_sheets_296_DataSourceIn",
        "DataSourceOut": "_sheets_297_DataSourceOut",
        "DateTimeRuleIn": "_sheets_298_DateTimeRuleIn",
        "DateTimeRuleOut": "_sheets_299_DateTimeRuleOut",
        "BatchUpdateSpreadsheetResponseIn": "_sheets_300_BatchUpdateSpreadsheetResponseIn",
        "BatchUpdateSpreadsheetResponseOut": "_sheets_301_BatchUpdateSpreadsheetResponseOut",
        "BatchUpdateValuesResponseIn": "_sheets_302_BatchUpdateValuesResponseIn",
        "BatchUpdateValuesResponseOut": "_sheets_303_BatchUpdateValuesResponseOut",
        "CutPasteRequestIn": "_sheets_304_CutPasteRequestIn",
        "CutPasteRequestOut": "_sheets_305_CutPasteRequestOut",
        "TextToColumnsRequestIn": "_sheets_306_TextToColumnsRequestIn",
        "TextToColumnsRequestOut": "_sheets_307_TextToColumnsRequestOut",
        "DuplicateFilterViewResponseIn": "_sheets_308_DuplicateFilterViewResponseIn",
        "DuplicateFilterViewResponseOut": "_sheets_309_DuplicateFilterViewResponseOut",
        "AddDataSourceResponseIn": "_sheets_310_AddDataSourceResponseIn",
        "AddDataSourceResponseOut": "_sheets_311_AddDataSourceResponseOut",
        "DataFilterValueRangeIn": "_sheets_312_DataFilterValueRangeIn",
        "DataFilterValueRangeOut": "_sheets_313_DataFilterValueRangeOut",
        "BatchClearValuesByDataFilterRequestIn": "_sheets_314_BatchClearValuesByDataFilterRequestIn",
        "BatchClearValuesByDataFilterRequestOut": "_sheets_315_BatchClearValuesByDataFilterRequestOut",
        "TrimWhitespaceResponseIn": "_sheets_316_TrimWhitespaceResponseIn",
        "TrimWhitespaceResponseOut": "_sheets_317_TrimWhitespaceResponseOut",
        "DataValidationRuleIn": "_sheets_318_DataValidationRuleIn",
        "DataValidationRuleOut": "_sheets_319_DataValidationRuleOut",
        "DeleteBandingRequestIn": "_sheets_320_DeleteBandingRequestIn",
        "DeleteBandingRequestOut": "_sheets_321_DeleteBandingRequestOut",
        "AddSlicerResponseIn": "_sheets_322_AddSlicerResponseIn",
        "AddSlicerResponseOut": "_sheets_323_AddSlicerResponseOut",
        "CreateDeveloperMetadataRequestIn": "_sheets_324_CreateDeveloperMetadataRequestIn",
        "CreateDeveloperMetadataRequestOut": "_sheets_325_CreateDeveloperMetadataRequestOut",
        "EmbeddedChartIn": "_sheets_326_EmbeddedChartIn",
        "EmbeddedChartOut": "_sheets_327_EmbeddedChartOut",
        "AddFilterViewRequestIn": "_sheets_328_AddFilterViewRequestIn",
        "AddFilterViewRequestOut": "_sheets_329_AddFilterViewRequestOut",
        "DataSourceFormulaIn": "_sheets_330_DataSourceFormulaIn",
        "DataSourceFormulaOut": "_sheets_331_DataSourceFormulaOut",
        "DeleteDuplicatesResponseIn": "_sheets_332_DeleteDuplicatesResponseIn",
        "DeleteDuplicatesResponseOut": "_sheets_333_DeleteDuplicatesResponseOut",
        "BordersIn": "_sheets_334_BordersIn",
        "BordersOut": "_sheets_335_BordersOut",
        "SpreadsheetIn": "_sheets_336_SpreadsheetIn",
        "SpreadsheetOut": "_sheets_337_SpreadsheetOut",
        "RefreshDataSourceObjectExecutionStatusIn": "_sheets_338_RefreshDataSourceObjectExecutionStatusIn",
        "RefreshDataSourceObjectExecutionStatusOut": "_sheets_339_RefreshDataSourceObjectExecutionStatusOut",
        "AddDimensionGroupResponseIn": "_sheets_340_AddDimensionGroupResponseIn",
        "AddDimensionGroupResponseOut": "_sheets_341_AddDimensionGroupResponseOut",
        "TextFormatRunIn": "_sheets_342_TextFormatRunIn",
        "TextFormatRunOut": "_sheets_343_TextFormatRunOut",
        "DeleteConditionalFormatRuleResponseIn": "_sheets_344_DeleteConditionalFormatRuleResponseIn",
        "DeleteConditionalFormatRuleResponseOut": "_sheets_345_DeleteConditionalFormatRuleResponseOut",
        "BandedRangeIn": "_sheets_346_BandedRangeIn",
        "BandedRangeOut": "_sheets_347_BandedRangeOut",
        "OrgChartSpecIn": "_sheets_348_OrgChartSpecIn",
        "OrgChartSpecOut": "_sheets_349_OrgChartSpecOut",
        "ChartCustomNumberFormatOptionsIn": "_sheets_350_ChartCustomNumberFormatOptionsIn",
        "ChartCustomNumberFormatOptionsOut": "_sheets_351_ChartCustomNumberFormatOptionsOut",
        "IntervalIn": "_sheets_352_IntervalIn",
        "IntervalOut": "_sheets_353_IntervalOut",
        "TextRotationIn": "_sheets_354_TextRotationIn",
        "TextRotationOut": "_sheets_355_TextRotationOut",
        "UpdateValuesResponseIn": "_sheets_356_UpdateValuesResponseIn",
        "UpdateValuesResponseOut": "_sheets_357_UpdateValuesResponseOut",
        "DeleteSheetRequestIn": "_sheets_358_DeleteSheetRequestIn",
        "DeleteSheetRequestOut": "_sheets_359_DeleteSheetRequestOut",
        "DeleteProtectedRangeRequestIn": "_sheets_360_DeleteProtectedRangeRequestIn",
        "DeleteProtectedRangeRequestOut": "_sheets_361_DeleteProtectedRangeRequestOut",
        "CellFormatIn": "_sheets_362_CellFormatIn",
        "CellFormatOut": "_sheets_363_CellFormatOut",
        "BatchUpdateValuesByDataFilterResponseIn": "_sheets_364_BatchUpdateValuesByDataFilterResponseIn",
        "BatchUpdateValuesByDataFilterResponseOut": "_sheets_365_BatchUpdateValuesByDataFilterResponseOut",
        "IterativeCalculationSettingsIn": "_sheets_366_IterativeCalculationSettingsIn",
        "IterativeCalculationSettingsOut": "_sheets_367_IterativeCalculationSettingsOut",
        "SearchDeveloperMetadataResponseIn": "_sheets_368_SearchDeveloperMetadataResponseIn",
        "SearchDeveloperMetadataResponseOut": "_sheets_369_SearchDeveloperMetadataResponseOut",
        "HistogramSeriesIn": "_sheets_370_HistogramSeriesIn",
        "HistogramSeriesOut": "_sheets_371_HistogramSeriesOut",
        "SearchDeveloperMetadataRequestIn": "_sheets_372_SearchDeveloperMetadataRequestIn",
        "SearchDeveloperMetadataRequestOut": "_sheets_373_SearchDeveloperMetadataRequestOut",
        "CandlestickChartSpecIn": "_sheets_374_CandlestickChartSpecIn",
        "CandlestickChartSpecOut": "_sheets_375_CandlestickChartSpecOut",
        "BatchGetValuesByDataFilterResponseIn": "_sheets_376_BatchGetValuesByDataFilterResponseIn",
        "BatchGetValuesByDataFilterResponseOut": "_sheets_377_BatchGetValuesByDataFilterResponseOut",
        "HistogramRuleIn": "_sheets_378_HistogramRuleIn",
        "HistogramRuleOut": "_sheets_379_HistogramRuleOut",
        "RequestIn": "_sheets_380_RequestIn",
        "RequestOut": "_sheets_381_RequestOut",
        "UpdateConditionalFormatRuleRequestIn": "_sheets_382_UpdateConditionalFormatRuleRequestIn",
        "UpdateConditionalFormatRuleRequestOut": "_sheets_383_UpdateConditionalFormatRuleRequestOut",
        "DataFilterIn": "_sheets_384_DataFilterIn",
        "DataFilterOut": "_sheets_385_DataFilterOut",
        "ColorStyleIn": "_sheets_386_ColorStyleIn",
        "ColorStyleOut": "_sheets_387_ColorStyleOut",
        "TreemapChartSpecIn": "_sheets_388_TreemapChartSpecIn",
        "TreemapChartSpecOut": "_sheets_389_TreemapChartSpecOut",
        "ClearBasicFilterRequestIn": "_sheets_390_ClearBasicFilterRequestIn",
        "ClearBasicFilterRequestOut": "_sheets_391_ClearBasicFilterRequestOut",
        "AppendCellsRequestIn": "_sheets_392_AppendCellsRequestIn",
        "AppendCellsRequestOut": "_sheets_393_AppendCellsRequestOut",
        "TreemapChartColorScaleIn": "_sheets_394_TreemapChartColorScaleIn",
        "TreemapChartColorScaleOut": "_sheets_395_TreemapChartColorScaleOut",
        "BatchUpdateValuesRequestIn": "_sheets_396_BatchUpdateValuesRequestIn",
        "BatchUpdateValuesRequestOut": "_sheets_397_BatchUpdateValuesRequestOut",
        "DeleteDimensionGroupResponseIn": "_sheets_398_DeleteDimensionGroupResponseIn",
        "DeleteDimensionGroupResponseOut": "_sheets_399_DeleteDimensionGroupResponseOut",
        "RowDataIn": "_sheets_400_RowDataIn",
        "RowDataOut": "_sheets_401_RowDataOut",
        "BatchClearValuesByDataFilterResponseIn": "_sheets_402_BatchClearValuesByDataFilterResponseIn",
        "BatchClearValuesByDataFilterResponseOut": "_sheets_403_BatchClearValuesByDataFilterResponseOut",
        "DataSourceRefreshWeeklyScheduleIn": "_sheets_404_DataSourceRefreshWeeklyScheduleIn",
        "DataSourceRefreshWeeklyScheduleOut": "_sheets_405_DataSourceRefreshWeeklyScheduleOut",
        "UpdateConditionalFormatRuleResponseIn": "_sheets_406_UpdateConditionalFormatRuleResponseIn",
        "UpdateConditionalFormatRuleResponseOut": "_sheets_407_UpdateConditionalFormatRuleResponseOut",
        "FindReplaceResponseIn": "_sheets_408_FindReplaceResponseIn",
        "FindReplaceResponseOut": "_sheets_409_FindReplaceResponseOut",
        "UpdateCellsRequestIn": "_sheets_410_UpdateCellsRequestIn",
        "UpdateCellsRequestOut": "_sheets_411_UpdateCellsRequestOut",
        "PivotFilterSpecIn": "_sheets_412_PivotFilterSpecIn",
        "PivotFilterSpecOut": "_sheets_413_PivotFilterSpecOut",
        "GridRangeIn": "_sheets_414_GridRangeIn",
        "GridRangeOut": "_sheets_415_GridRangeOut",
        "FilterViewIn": "_sheets_416_FilterViewIn",
        "FilterViewOut": "_sheets_417_FilterViewOut",
        "PivotFilterCriteriaIn": "_sheets_418_PivotFilterCriteriaIn",
        "PivotFilterCriteriaOut": "_sheets_419_PivotFilterCriteriaOut",
        "BasicChartAxisIn": "_sheets_420_BasicChartAxisIn",
        "BasicChartAxisOut": "_sheets_421_BasicChartAxisOut",
        "BasicSeriesDataPointStyleOverrideIn": "_sheets_422_BasicSeriesDataPointStyleOverrideIn",
        "BasicSeriesDataPointStyleOverrideOut": "_sheets_423_BasicSeriesDataPointStyleOverrideOut",
        "BasicChartSeriesIn": "_sheets_424_BasicChartSeriesIn",
        "BasicChartSeriesOut": "_sheets_425_BasicChartSeriesOut",
        "LineStyleIn": "_sheets_426_LineStyleIn",
        "LineStyleOut": "_sheets_427_LineStyleOut",
        "AddSheetResponseIn": "_sheets_428_AddSheetResponseIn",
        "AddSheetResponseOut": "_sheets_429_AddSheetResponseOut",
        "DuplicateFilterViewRequestIn": "_sheets_430_DuplicateFilterViewRequestIn",
        "DuplicateFilterViewRequestOut": "_sheets_431_DuplicateFilterViewRequestOut",
        "UpdateEmbeddedObjectPositionResponseIn": "_sheets_432_UpdateEmbeddedObjectPositionResponseIn",
        "UpdateEmbeddedObjectPositionResponseOut": "_sheets_433_UpdateEmbeddedObjectPositionResponseOut",
        "UpdateDeveloperMetadataRequestIn": "_sheets_434_UpdateDeveloperMetadataRequestIn",
        "UpdateDeveloperMetadataRequestOut": "_sheets_435_UpdateDeveloperMetadataRequestOut",
        "UpdateNamedRangeRequestIn": "_sheets_436_UpdateNamedRangeRequestIn",
        "UpdateNamedRangeRequestOut": "_sheets_437_UpdateNamedRangeRequestOut",
        "RefreshDataSourceResponseIn": "_sheets_438_RefreshDataSourceResponseIn",
        "RefreshDataSourceResponseOut": "_sheets_439_RefreshDataSourceResponseOut",
        "UpdateValuesByDataFilterResponseIn": "_sheets_440_UpdateValuesByDataFilterResponseIn",
        "UpdateValuesByDataFilterResponseOut": "_sheets_441_UpdateValuesByDataFilterResponseOut",
        "UpdateChartSpecRequestIn": "_sheets_442_UpdateChartSpecRequestIn",
        "UpdateChartSpecRequestOut": "_sheets_443_UpdateChartSpecRequestOut",
        "SetDataValidationRequestIn": "_sheets_444_SetDataValidationRequestIn",
        "SetDataValidationRequestOut": "_sheets_445_SetDataValidationRequestOut",
        "ValueRangeIn": "_sheets_446_ValueRangeIn",
        "ValueRangeOut": "_sheets_447_ValueRangeOut",
        "UpdateSpreadsheetPropertiesRequestIn": "_sheets_448_UpdateSpreadsheetPropertiesRequestIn",
        "UpdateSpreadsheetPropertiesRequestOut": "_sheets_449_UpdateSpreadsheetPropertiesRequestOut",
        "DuplicateSheetRequestIn": "_sheets_450_DuplicateSheetRequestIn",
        "DuplicateSheetRequestOut": "_sheets_451_DuplicateSheetRequestOut",
        "EmbeddedObjectBorderIn": "_sheets_452_EmbeddedObjectBorderIn",
        "EmbeddedObjectBorderOut": "_sheets_453_EmbeddedObjectBorderOut",
        "SpreadsheetPropertiesIn": "_sheets_454_SpreadsheetPropertiesIn",
        "SpreadsheetPropertiesOut": "_sheets_455_SpreadsheetPropertiesOut",
        "ChartHistogramRuleIn": "_sheets_456_ChartHistogramRuleIn",
        "ChartHistogramRuleOut": "_sheets_457_ChartHistogramRuleOut",
        "BubbleChartSpecIn": "_sheets_458_BubbleChartSpecIn",
        "BubbleChartSpecOut": "_sheets_459_BubbleChartSpecOut",
        "DimensionRangeIn": "_sheets_460_DimensionRangeIn",
        "DimensionRangeOut": "_sheets_461_DimensionRangeOut",
        "AppendDimensionRequestIn": "_sheets_462_AppendDimensionRequestIn",
        "AppendDimensionRequestOut": "_sheets_463_AppendDimensionRequestOut",
        "AddConditionalFormatRuleRequestIn": "_sheets_464_AddConditionalFormatRuleRequestIn",
        "AddConditionalFormatRuleRequestOut": "_sheets_465_AddConditionalFormatRuleRequestOut",
        "WaterfallChartSeriesIn": "_sheets_466_WaterfallChartSeriesIn",
        "WaterfallChartSeriesOut": "_sheets_467_WaterfallChartSeriesOut",
        "WaterfallChartCustomSubtotalIn": "_sheets_468_WaterfallChartCustomSubtotalIn",
        "WaterfallChartCustomSubtotalOut": "_sheets_469_WaterfallChartCustomSubtotalOut",
        "ChartAxisViewWindowOptionsIn": "_sheets_470_ChartAxisViewWindowOptionsIn",
        "ChartAxisViewWindowOptionsOut": "_sheets_471_ChartAxisViewWindowOptionsOut",
        "AutoResizeDimensionsRequestIn": "_sheets_472_AutoResizeDimensionsRequestIn",
        "AutoResizeDimensionsRequestOut": "_sheets_473_AutoResizeDimensionsRequestOut",
        "PivotGroupSortValueBucketIn": "_sheets_474_PivotGroupSortValueBucketIn",
        "PivotGroupSortValueBucketOut": "_sheets_475_PivotGroupSortValueBucketOut",
        "DeveloperMetadataLocationIn": "_sheets_476_DeveloperMetadataLocationIn",
        "DeveloperMetadataLocationOut": "_sheets_477_DeveloperMetadataLocationOut",
        "DataSourceParameterIn": "_sheets_478_DataSourceParameterIn",
        "DataSourceParameterOut": "_sheets_479_DataSourceParameterOut",
        "DimensionPropertiesIn": "_sheets_480_DimensionPropertiesIn",
        "DimensionPropertiesOut": "_sheets_481_DimensionPropertiesOut",
        "InsertDimensionRequestIn": "_sheets_482_InsertDimensionRequestIn",
        "InsertDimensionRequestOut": "_sheets_483_InsertDimensionRequestOut",
        "TimeOfDayIn": "_sheets_484_TimeOfDayIn",
        "TimeOfDayOut": "_sheets_485_TimeOfDayOut",
        "RefreshDataSourceRequestIn": "_sheets_486_RefreshDataSourceRequestIn",
        "RefreshDataSourceRequestOut": "_sheets_487_RefreshDataSourceRequestOut",
        "AddChartRequestIn": "_sheets_488_AddChartRequestIn",
        "AddChartRequestOut": "_sheets_489_AddChartRequestOut",
        "CreateDeveloperMetadataResponseIn": "_sheets_490_CreateDeveloperMetadataResponseIn",
        "CreateDeveloperMetadataResponseOut": "_sheets_491_CreateDeveloperMetadataResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["BigQueryTableSpecIn"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "tableProjectId": t.string().optional(),
        }
    ).named(renames["BigQueryTableSpecIn"])
    types["BigQueryTableSpecOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "tableProjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryTableSpecOut"])
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
    types["BigQueryDataSourceSpecIn"] = t.struct(
        {
            "tableSpec": t.proxy(renames["BigQueryTableSpecIn"]).optional(),
            "projectId": t.string().optional(),
            "querySpec": t.proxy(renames["BigQueryQuerySpecIn"]).optional(),
        }
    ).named(renames["BigQueryDataSourceSpecIn"])
    types["BigQueryDataSourceSpecOut"] = t.struct(
        {
            "tableSpec": t.proxy(renames["BigQueryTableSpecOut"]).optional(),
            "projectId": t.string().optional(),
            "querySpec": t.proxy(renames["BigQueryQuerySpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDataSourceSpecOut"])
    types["BaselineValueFormatIn"] = t.struct(
        {
            "description": t.string().optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "negativeColor": t.proxy(renames["ColorIn"]).optional(),
            "position": t.proxy(renames["TextPositionIn"]).optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "positiveColor": t.proxy(renames["ColorIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "comparisonType": t.string().optional(),
        }
    ).named(renames["BaselineValueFormatIn"])
    types["BaselineValueFormatOut"] = t.struct(
        {
            "description": t.string().optional(),
            "positiveColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "negativeColor": t.proxy(renames["ColorOut"]).optional(),
            "position": t.proxy(renames["TextPositionOut"]).optional(),
            "negativeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "positiveColor": t.proxy(renames["ColorOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "comparisonType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BaselineValueFormatOut"])
    types["DataSourceSheetPropertiesIn"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["DataSourceColumnIn"])).optional(),
            "dataExecutionStatus": t.proxy(renames["DataExecutionStatusIn"]).optional(),
        }
    ).named(renames["DataSourceSheetPropertiesIn"])
    types["DataSourceSheetPropertiesOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["DataSourceColumnOut"])).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceSheetPropertiesOut"])
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
    types["AddBandingResponseIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingResponseIn"])
    types["AddBandingResponseOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingResponseOut"])
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
    types["ProtectedRangeIn"] = t.struct(
        {
            "warningOnly": t.boolean().optional(),
            "requestingUserCanEdit": t.boolean().optional(),
            "namedRangeId": t.string().optional(),
            "description": t.string().optional(),
            "editors": t.proxy(renames["EditorsIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "protectedRangeId": t.integer().optional(),
        }
    ).named(renames["ProtectedRangeIn"])
    types["ProtectedRangeOut"] = t.struct(
        {
            "warningOnly": t.boolean().optional(),
            "requestingUserCanEdit": t.boolean().optional(),
            "namedRangeId": t.string().optional(),
            "description": t.string().optional(),
            "editors": t.proxy(renames["EditorsOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "unprotectedRanges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "protectedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProtectedRangeOut"])
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
    types["UpdateEmbeddedObjectPositionRequestIn"] = t.struct(
        {
            "newPosition": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "objectId": t.integer().optional(),
            "fields": t.string().optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionRequestIn"])
    types["UpdateEmbeddedObjectPositionRequestOut"] = t.struct(
        {
            "newPosition": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "objectId": t.integer().optional(),
            "fields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionRequestOut"])
    types["GridPropertiesIn"] = t.struct(
        {
            "hideGridlines": t.boolean().optional(),
            "frozenColumnCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
            "columnCount": t.integer().optional(),
            "frozenRowCount": t.integer().optional(),
            "rowGroupControlAfter": t.boolean().optional(),
        }
    ).named(renames["GridPropertiesIn"])
    types["GridPropertiesOut"] = t.struct(
        {
            "hideGridlines": t.boolean().optional(),
            "frozenColumnCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "columnGroupControlAfter": t.boolean().optional(),
            "columnCount": t.integer().optional(),
            "frozenRowCount": t.integer().optional(),
            "rowGroupControlAfter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridPropertiesOut"])
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
    types["TrimWhitespaceRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["TrimWhitespaceRequestIn"])
    types["TrimWhitespaceRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceRequestOut"])
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
    types["DeleteEmbeddedObjectRequestIn"] = t.struct(
        {"objectId": t.integer().optional()}
    ).named(renames["DeleteEmbeddedObjectRequestIn"])
    types["DeleteEmbeddedObjectRequestOut"] = t.struct(
        {
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteEmbeddedObjectRequestOut"])
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
    types["AddSlicerRequestIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerRequestIn"])
    types["AddSlicerRequestOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerRequestOut"])
    types["DeleteDimensionRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionRequestIn"])
    types["DeleteDimensionRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionRequestOut"])
    types["AddChartResponseIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartResponseIn"])
    types["AddChartResponseOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartResponseOut"])
    types["ResponseIn"] = t.struct(
        {
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseIn"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseIn"]
            ).optional(),
            "addSheet": t.proxy(renames["AddSheetResponseIn"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseIn"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingResponseIn"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseIn"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseIn"]
            ).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseIn"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseIn"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseIn"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseIn"]
            ).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseIn"]).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseIn"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseIn"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseIn"]).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseIn"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartResponseIn"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseIn"]
            ).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseIn"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseIn"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseIn"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseIn"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseIn"]).optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleResponseOut"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataResponseOut"]
            ).optional(),
            "addSheet": t.proxy(renames["AddSheetResponseOut"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceResponseOut"]
            ).optional(),
            "addBanding": t.proxy(renames["AddBandingResponseOut"]).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupResponseOut"]
            ).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesResponseOut"]
            ).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataResponseOut"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceResponseOut"]).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceResponseOut"]
            ).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewResponseOut"]
            ).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetResponseOut"]).optional(),
            "findReplace": t.proxy(renames["FindReplaceResponseOut"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleResponseOut"]
            ).optional(),
            "addSlicer": t.proxy(renames["AddSlicerResponseOut"]).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionResponseOut"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartResponseOut"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupResponseOut"]
            ).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataResponseOut"]
            ).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceResponseOut"]).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewResponseOut"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeResponseOut"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
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
            "gradientRule": t.proxy(renames["GradientRuleIn"]).optional(),
            "booleanRule": t.proxy(renames["BooleanRuleIn"]).optional(),
            "ranges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
        }
    ).named(renames["ConditionalFormatRuleIn"])
    types["ConditionalFormatRuleOut"] = t.struct(
        {
            "gradientRule": t.proxy(renames["GradientRuleOut"]).optional(),
            "booleanRule": t.proxy(renames["BooleanRuleOut"]).optional(),
            "ranges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionalFormatRuleOut"])
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
    types["HistogramChartSpecIn"] = t.struct(
        {
            "series": t.array(t.proxy(renames["HistogramSeriesIn"])).optional(),
            "bucketSize": t.number().optional(),
            "showItemDividers": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "outlierPercentile": t.number().optional(),
        }
    ).named(renames["HistogramChartSpecIn"])
    types["HistogramChartSpecOut"] = t.struct(
        {
            "series": t.array(t.proxy(renames["HistogramSeriesOut"])).optional(),
            "bucketSize": t.number().optional(),
            "showItemDividers": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "outlierPercentile": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramChartSpecOut"])
    types["LinkIn"] = t.struct({"uri": t.string().optional()}).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["AddBandingRequestIn"] = t.struct(
        {"bandedRange": t.proxy(renames["BandedRangeIn"]).optional()}
    ).named(renames["AddBandingRequestIn"])
    types["AddBandingRequestOut"] = t.struct(
        {
            "bandedRange": t.proxy(renames["BandedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddBandingRequestOut"])
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
    types["WaterfallChartSpecIn"] = t.struct(
        {
            "domain": t.proxy(renames["WaterfallChartDomainIn"]).optional(),
            "hideConnectorLines": t.boolean().optional(),
            "series": t.array(t.proxy(renames["WaterfallChartSeriesIn"])).optional(),
            "firstValueIsTotal": t.boolean().optional(),
            "connectorLineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "stackedType": t.string().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
        }
    ).named(renames["WaterfallChartSpecIn"])
    types["WaterfallChartSpecOut"] = t.struct(
        {
            "domain": t.proxy(renames["WaterfallChartDomainOut"]).optional(),
            "hideConnectorLines": t.boolean().optional(),
            "series": t.array(t.proxy(renames["WaterfallChartSeriesOut"])).optional(),
            "firstValueIsTotal": t.boolean().optional(),
            "connectorLineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "stackedType": t.string().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSpecOut"])
    types["DeveloperMetadataIn"] = t.struct(
        {
            "visibility": t.string().optional(),
            "location": t.proxy(renames["DeveloperMetadataLocationIn"]).optional(),
            "metadataId": t.integer().optional(),
            "metadataKey": t.string().optional(),
            "metadataValue": t.string().optional(),
        }
    ).named(renames["DeveloperMetadataIn"])
    types["DeveloperMetadataOut"] = t.struct(
        {
            "visibility": t.string().optional(),
            "location": t.proxy(renames["DeveloperMetadataLocationOut"]).optional(),
            "metadataId": t.integer().optional(),
            "metadataKey": t.string().optional(),
            "metadataValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataOut"])
    types["ManualRuleIn"] = t.struct(
        {"groups": t.array(t.proxy(renames["ManualRuleGroupIn"])).optional()}
    ).named(renames["ManualRuleIn"])
    types["ManualRuleOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["ManualRuleGroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualRuleOut"])
    types["SheetIn"] = t.struct(
        {
            "columnGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "properties": t.proxy(renames["SheetPropertiesIn"]).optional(),
            "protectedRanges": t.array(t.proxy(renames["ProtectedRangeIn"])).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleIn"])
            ).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupIn"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "slicers": t.array(t.proxy(renames["SlicerIn"])).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewIn"])).optional(),
            "merges": t.array(t.proxy(renames["GridRangeIn"])).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartIn"])).optional(),
            "bandedRanges": t.array(t.proxy(renames["BandedRangeIn"])).optional(),
            "data": t.array(t.proxy(renames["GridDataIn"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterIn"]).optional(),
        }
    ).named(renames["SheetIn"])
    types["SheetOut"] = t.struct(
        {
            "columnGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "protectedRanges": t.array(
                t.proxy(renames["ProtectedRangeOut"])
            ).optional(),
            "conditionalFormats": t.array(
                t.proxy(renames["ConditionalFormatRuleOut"])
            ).optional(),
            "rowGroups": t.array(t.proxy(renames["DimensionGroupOut"])).optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "slicers": t.array(t.proxy(renames["SlicerOut"])).optional(),
            "filterViews": t.array(t.proxy(renames["FilterViewOut"])).optional(),
            "merges": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "charts": t.array(t.proxy(renames["EmbeddedChartOut"])).optional(),
            "bandedRanges": t.array(t.proxy(renames["BandedRangeOut"])).optional(),
            "data": t.array(t.proxy(renames["GridDataOut"])).optional(),
            "basicFilter": t.proxy(renames["BasicFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetOut"])
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
    types["AddNamedRangeResponseIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeResponseIn"])
    types["AddNamedRangeResponseOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeResponseOut"])
    types["DataSourceTableIn"] = t.struct(
        {
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceIn"])
            ).optional(),
            "columnSelectionType": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "dataSourceId": t.string().optional(),
            "rowLimit": t.integer().optional(),
        }
    ).named(renames["DataSourceTableIn"])
    types["DataSourceTableOut"] = t.struct(
        {
            "columns": t.array(
                t.proxy(renames["DataSourceColumnReferenceOut"])
            ).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "columnSelectionType": t.string().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "dataSourceId": t.string().optional(),
            "rowLimit": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceTableOut"])
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
    types["DataSourceRefreshDailyScheduleIn"] = t.struct(
        {"startTime": t.proxy(renames["TimeOfDayIn"]).optional()}
    ).named(renames["DataSourceRefreshDailyScheduleIn"])
    types["DataSourceRefreshDailyScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshDailyScheduleOut"])
    types["UpdateBordersRequestIn"] = t.struct(
        {
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "innerVertical": t.proxy(renames["BorderIn"]).optional(),
            "top": t.proxy(renames["BorderIn"]).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "right": t.proxy(renames["BorderIn"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderIn"]).optional(),
            "left": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["UpdateBordersRequestIn"])
    types["UpdateBordersRequestOut"] = t.struct(
        {
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "innerVertical": t.proxy(renames["BorderOut"]).optional(),
            "top": t.proxy(renames["BorderOut"]).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "right": t.proxy(renames["BorderOut"]).optional(),
            "innerHorizontal": t.proxy(renames["BorderOut"]).optional(),
            "left": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBordersRequestOut"])
    types["PasteDataRequestIn"] = t.struct(
        {
            "data": t.string().optional(),
            "coordinate": t.proxy(renames["GridCoordinateIn"]).optional(),
            "html": t.boolean().optional(),
            "delimiter": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PasteDataRequestIn"])
    types["PasteDataRequestOut"] = t.struct(
        {
            "data": t.string().optional(),
            "coordinate": t.proxy(renames["GridCoordinateOut"]).optional(),
            "html": t.boolean().optional(),
            "delimiter": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasteDataRequestOut"])
    types["DeleteFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DeleteFilterViewRequestIn"])
    types["DeleteFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteFilterViewRequestOut"])
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
    types["CopySheetToAnotherSpreadsheetRequestIn"] = t.struct(
        {"destinationSpreadsheetId": t.string().optional()}
    ).named(renames["CopySheetToAnotherSpreadsheetRequestIn"])
    types["CopySheetToAnotherSpreadsheetRequestOut"] = t.struct(
        {
            "destinationSpreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopySheetToAnotherSpreadsheetRequestOut"])
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
    types["BatchUpdateValuesByDataFilterRequestIn"] = t.struct(
        {
            "responseDateTimeRenderOption": t.string().optional(),
            "data": t.array(t.proxy(renames["DataFilterValueRangeIn"])).optional(),
            "valueInputOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
            "includeValuesInResponse": t.boolean().optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestIn"])
    types["BatchUpdateValuesByDataFilterRequestOut"] = t.struct(
        {
            "responseDateTimeRenderOption": t.string().optional(),
            "data": t.array(t.proxy(renames["DataFilterValueRangeOut"])).optional(),
            "valueInputOption": t.string().optional(),
            "responseValueRenderOption": t.string().optional(),
            "includeValuesInResponse": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterRequestOut"])
    types["InterpolationPointIn"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["InterpolationPointIn"])
    types["InterpolationPointOut"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InterpolationPointOut"])
    types["SlicerIn"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "spec": t.proxy(renames["SlicerSpecIn"]).optional(),
            "slicerId": t.integer().optional(),
        }
    ).named(renames["SlicerIn"])
    types["SlicerOut"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "spec": t.proxy(renames["SlicerSpecOut"]).optional(),
            "slicerId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerOut"])
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
    types["EditorsIn"] = t.struct(
        {
            "users": t.array(t.string()).optional(),
            "domainUsersCanEdit": t.boolean().optional(),
            "groups": t.array(t.string()).optional(),
        }
    ).named(renames["EditorsIn"])
    types["EditorsOut"] = t.struct(
        {
            "users": t.array(t.string()).optional(),
            "domainUsersCanEdit": t.boolean().optional(),
            "groups": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditorsOut"])
    types["ClearValuesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClearValuesRequestIn"]
    )
    types["ClearValuesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearValuesRequestOut"])
    types["BigQueryQuerySpecIn"] = t.struct({"rawQuery": t.string().optional()}).named(
        renames["BigQueryQuerySpecIn"]
    )
    types["BigQueryQuerySpecOut"] = t.struct(
        {
            "rawQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryQuerySpecOut"])
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
    types["PieChartSpecIn"] = t.struct(
        {
            "threeDimensional": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "pieHole": t.number().optional(),
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["PieChartSpecIn"])
    types["PieChartSpecOut"] = t.struct(
        {
            "threeDimensional": t.boolean().optional(),
            "legendPosition": t.string().optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "pieHole": t.number().optional(),
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PieChartSpecOut"])
    types["BandingPropertiesIn"] = t.struct(
        {
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "secondBandColor": t.proxy(renames["ColorIn"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "footerColor": t.proxy(renames["ColorIn"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "firstBandColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "firstBandColor": t.proxy(renames["ColorIn"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["BandingPropertiesIn"])
    types["BandingPropertiesOut"] = t.struct(
        {
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "secondBandColor": t.proxy(renames["ColorOut"]).optional(),
            "secondBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "footerColor": t.proxy(renames["ColorOut"]).optional(),
            "footerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "firstBandColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "firstBandColor": t.proxy(renames["ColorOut"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandingPropertiesOut"])
    types["ScorecardChartSpecIn"] = t.struct(
        {
            "keyValueFormat": t.proxy(renames["KeyValueFormatIn"]).optional(),
            "aggregateType": t.string().optional(),
            "baselineValueFormat": t.proxy(renames["BaselineValueFormatIn"]).optional(),
            "scaleFactor": t.number().optional(),
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsIn"]
            ).optional(),
            "keyValueData": t.proxy(renames["ChartDataIn"]).optional(),
            "numberFormatSource": t.string().optional(),
            "baselineValueData": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["ScorecardChartSpecIn"])
    types["ScorecardChartSpecOut"] = t.struct(
        {
            "keyValueFormat": t.proxy(renames["KeyValueFormatOut"]).optional(),
            "aggregateType": t.string().optional(),
            "baselineValueFormat": t.proxy(
                renames["BaselineValueFormatOut"]
            ).optional(),
            "scaleFactor": t.number().optional(),
            "customFormatOptions": t.proxy(
                renames["ChartCustomNumberFormatOptionsOut"]
            ).optional(),
            "keyValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "numberFormatSource": t.string().optional(),
            "baselineValueData": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScorecardChartSpecOut"])
    types["FilterCriteriaIn"] = t.struct(
        {
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "hiddenValues": t.array(t.string()).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorIn"]).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
        }
    ).named(renames["FilterCriteriaIn"])
    types["FilterCriteriaOut"] = t.struct(
        {
            "visibleForegroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "visibleBackgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "hiddenValues": t.array(t.string()).optional(),
            "visibleForegroundColor": t.proxy(renames["ColorOut"]).optional(),
            "visibleBackgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterCriteriaOut"])
    types["OverlayPositionIn"] = t.struct(
        {
            "anchorCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "offsetXPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "offsetYPixels": t.integer().optional(),
            "heightPixels": t.integer().optional(),
        }
    ).named(renames["OverlayPositionIn"])
    types["OverlayPositionOut"] = t.struct(
        {
            "anchorCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "offsetXPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "offsetYPixels": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OverlayPositionOut"])
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
    types["AppendValuesResponseIn"] = t.struct(
        {
            "tableRange": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "updates": t.proxy(renames["UpdateValuesResponseIn"]).optional(),
        }
    ).named(renames["AppendValuesResponseIn"])
    types["AppendValuesResponseOut"] = t.struct(
        {
            "tableRange": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "updates": t.proxy(renames["UpdateValuesResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendValuesResponseOut"])
    types["DimensionGroupIn"] = t.struct(
        {
            "collapsed": t.boolean().optional(),
            "depth": t.integer().optional(),
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
        }
    ).named(renames["DimensionGroupIn"])
    types["DimensionGroupOut"] = t.struct(
        {
            "collapsed": t.boolean().optional(),
            "depth": t.integer().optional(),
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionGroupOut"])
    types["CandlestickDataIn"] = t.struct(
        {
            "lowSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "highSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
            "openSeries": t.proxy(renames["CandlestickSeriesIn"]).optional(),
        }
    ).named(renames["CandlestickDataIn"])
    types["CandlestickDataOut"] = t.struct(
        {
            "lowSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "closeSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "highSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "openSeries": t.proxy(renames["CandlestickSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickDataOut"])
    types["UnmergeCellsRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["UnmergeCellsRequestIn"])
    types["UnmergeCellsRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmergeCellsRequestOut"])
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
    types["DeveloperMetadataLookupIn"] = t.struct(
        {
            "locationType": t.string().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationIn"]
            ).optional(),
            "visibility": t.string().optional(),
            "metadataValue": t.string().optional(),
            "metadataId": t.integer().optional(),
            "locationMatchingStrategy": t.string().optional(),
            "metadataKey": t.string().optional(),
        }
    ).named(renames["DeveloperMetadataLookupIn"])
    types["DeveloperMetadataLookupOut"] = t.struct(
        {
            "locationType": t.string().optional(),
            "metadataLocation": t.proxy(
                renames["DeveloperMetadataLocationOut"]
            ).optional(),
            "visibility": t.string().optional(),
            "metadataValue": t.string().optional(),
            "metadataId": t.integer().optional(),
            "locationMatchingStrategy": t.string().optional(),
            "metadataKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLookupOut"])
    types["SlicerSpecIn"] = t.struct(
        {
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "dataRange": t.proxy(renames["GridRangeIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "columnIndex": t.integer().optional(),
            "title": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "applyToPivotTables": t.boolean().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
        }
    ).named(renames["SlicerSpecIn"])
    types["SlicerSpecOut"] = t.struct(
        {
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "dataRange": t.proxy(renames["GridRangeOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "columnIndex": t.integer().optional(),
            "title": t.string().optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "applyToPivotTables": t.boolean().optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlicerSpecOut"])
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
    types["BasicFilterIn"] = t.struct(
        {
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BasicFilterIn"])
    types["BasicFilterOut"] = t.struct(
        {
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicFilterOut"])
    types["AddNamedRangeRequestIn"] = t.struct(
        {"namedRange": t.proxy(renames["NamedRangeIn"]).optional()}
    ).named(renames["AddNamedRangeRequestIn"])
    types["AddNamedRangeRequestOut"] = t.struct(
        {
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNamedRangeRequestOut"])
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
    types["DataExecutionStatusIn"] = t.struct(
        {
            "lastRefreshTime": t.string().optional(),
            "state": t.string().optional(),
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["DataExecutionStatusIn"])
    types["DataExecutionStatusOut"] = t.struct(
        {
            "lastRefreshTime": t.string().optional(),
            "state": t.string().optional(),
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataExecutionStatusOut"])
    types["BatchClearValuesRequestIn"] = t.struct(
        {"ranges": t.array(t.string()).optional()}
    ).named(renames["BatchClearValuesRequestIn"])
    types["BatchClearValuesRequestOut"] = t.struct(
        {
            "ranges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesRequestOut"])
    types["BatchGetValuesByDataFilterRequestIn"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
            "dateTimeRenderOption": t.string().optional(),
            "majorDimension": t.string().optional(),
            "valueRenderOption": t.string().optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestIn"])
    types["BatchGetValuesByDataFilterRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "dateTimeRenderOption": t.string().optional(),
            "majorDimension": t.string().optional(),
            "valueRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesByDataFilterRequestOut"])
    types["AddDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["AddDimensionGroupRequestIn"])
    types["AddDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDimensionGroupRequestOut"])
    types["AddSheetRequestIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetRequestIn"])
    types["AddSheetRequestOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetRequestOut"])
    types["DeleteDataSourceRequestIn"] = t.struct(
        {"dataSourceId": t.string().optional()}
    ).named(renames["DeleteDataSourceRequestIn"])
    types["DeleteDataSourceRequestOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDataSourceRequestOut"])
    types["TextFormatIn"] = t.struct(
        {
            "link": t.proxy(renames["LinkIn"]).optional(),
            "strikethrough": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "underline": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "bold": t.boolean().optional(),
            "fontFamily": t.string().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "italic": t.boolean().optional(),
        }
    ).named(renames["TextFormatIn"])
    types["TextFormatOut"] = t.struct(
        {
            "link": t.proxy(renames["LinkOut"]).optional(),
            "strikethrough": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "underline": t.boolean().optional(),
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "bold": t.boolean().optional(),
            "fontFamily": t.string().optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "italic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFormatOut"])
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
    types["DataSourceRefreshScheduleIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleIn"]
            ).optional(),
            "refreshScope": t.string().optional(),
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleIn"]
            ).optional(),
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleIn"]
            ).optional(),
        }
    ).named(renames["DataSourceRefreshScheduleIn"])
    types["DataSourceRefreshScheduleOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "monthlySchedule": t.proxy(
                renames["DataSourceRefreshMonthlyScheduleOut"]
            ).optional(),
            "refreshScope": t.string().optional(),
            "weeklySchedule": t.proxy(
                renames["DataSourceRefreshWeeklyScheduleOut"]
            ).optional(),
            "dailySchedule": t.proxy(
                renames["DataSourceRefreshDailyScheduleOut"]
            ).optional(),
            "nextRun": t.proxy(renames["IntervalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRefreshScheduleOut"])
    types["DataSourceObjectReferenceIn"] = t.struct(
        {
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateIn"]).optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
            "chartId": t.integer().optional(),
            "sheetId": t.string().optional(),
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateIn"]
            ).optional(),
        }
    ).named(renames["DataSourceObjectReferenceIn"])
    types["DataSourceObjectReferenceOut"] = t.struct(
        {
            "dataSourceFormulaCell": t.proxy(renames["GridCoordinateOut"]).optional(),
            "dataSourcePivotTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "chartId": t.integer().optional(),
            "sheetId": t.string().optional(),
            "dataSourceTableAnchorCell": t.proxy(
                renames["GridCoordinateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceObjectReferenceOut"])
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
    types["AddFilterViewResponseIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewResponseIn"])
    types["AddFilterViewResponseOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewResponseOut"])
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
    types["ChartDataIn"] = t.struct(
        {
            "columnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "sourceRange": t.proxy(renames["ChartSourceRangeIn"]).optional(),
            "groupRule": t.proxy(renames["ChartGroupRuleIn"]).optional(),
            "aggregateType": t.string().optional(),
        }
    ).named(renames["ChartDataIn"])
    types["ChartDataOut"] = t.struct(
        {
            "columnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "sourceRange": t.proxy(renames["ChartSourceRangeOut"]).optional(),
            "groupRule": t.proxy(renames["ChartGroupRuleOut"]).optional(),
            "aggregateType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDataOut"])
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
    types["CopyPasteRequestIn"] = t.struct(
        {
            "destination": t.proxy(renames["GridRangeIn"]).optional(),
            "pasteType": t.string().optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "pasteOrientation": t.string().optional(),
        }
    ).named(renames["CopyPasteRequestIn"])
    types["CopyPasteRequestOut"] = t.struct(
        {
            "destination": t.proxy(renames["GridRangeOut"]).optional(),
            "pasteType": t.string().optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "pasteOrientation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyPasteRequestOut"])
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
    types["SortSpecIn"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "foregroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "dimensionIndex": t.integer().optional(),
            "foregroundColor": t.proxy(renames["ColorIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
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
            "foregroundColor": t.proxy(renames["ColorOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortSpecOut"])
    types["PivotGroupRuleIn"] = t.struct(
        {
            "manualRule": t.proxy(renames["ManualRuleIn"]).optional(),
            "dateTimeRule": t.proxy(renames["DateTimeRuleIn"]).optional(),
            "histogramRule": t.proxy(renames["HistogramRuleIn"]).optional(),
        }
    ).named(renames["PivotGroupRuleIn"])
    types["PivotGroupRuleOut"] = t.struct(
        {
            "manualRule": t.proxy(renames["ManualRuleOut"]).optional(),
            "dateTimeRule": t.proxy(renames["DateTimeRuleOut"]).optional(),
            "histogramRule": t.proxy(renames["HistogramRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupRuleOut"])
    types["DataLabelIn"] = t.struct(
        {
            "type": t.string().optional(),
            "customLabelData": t.proxy(renames["ChartDataIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "placement": t.string().optional(),
        }
    ).named(renames["DataLabelIn"])
    types["DataLabelOut"] = t.struct(
        {
            "type": t.string().optional(),
            "customLabelData": t.proxy(renames["ChartDataOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "placement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLabelOut"])
    types["BasicChartSpecIn"] = t.struct(
        {
            "compareMode": t.string().optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesIn"])).optional(),
            "stackedType": t.string().optional(),
            "lineSmoothing": t.boolean().optional(),
            "headerCount": t.integer().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "legendPosition": t.string().optional(),
            "axis": t.array(t.proxy(renames["BasicChartAxisIn"])).optional(),
            "interpolateNulls": t.boolean().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainIn"])).optional(),
            "threeDimensional": t.boolean().optional(),
            "chartType": t.string().optional(),
        }
    ).named(renames["BasicChartSpecIn"])
    types["BasicChartSpecOut"] = t.struct(
        {
            "compareMode": t.string().optional(),
            "series": t.array(t.proxy(renames["BasicChartSeriesOut"])).optional(),
            "stackedType": t.string().optional(),
            "lineSmoothing": t.boolean().optional(),
            "headerCount": t.integer().optional(),
            "totalDataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "legendPosition": t.string().optional(),
            "axis": t.array(t.proxy(renames["BasicChartAxisOut"])).optional(),
            "interpolateNulls": t.boolean().optional(),
            "domains": t.array(t.proxy(renames["BasicChartDomainOut"])).optional(),
            "threeDimensional": t.boolean().optional(),
            "chartType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSpecOut"])
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
    types["TextPositionIn"] = t.struct(
        {"horizontalAlignment": t.string().optional()}
    ).named(renames["TextPositionIn"])
    types["TextPositionOut"] = t.struct(
        {
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPositionOut"])
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
    types["AddDataSourceRequestIn"] = t.struct(
        {"dataSource": t.proxy(renames["DataSourceIn"]).optional()}
    ).named(renames["AddDataSourceRequestIn"])
    types["AddDataSourceRequestOut"] = t.struct(
        {
            "dataSource": t.proxy(renames["DataSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDataSourceRequestOut"])
    types["FilterSpecIn"] = t.struct(
        {
            "columnIndex": t.integer().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
        }
    ).named(renames["FilterSpecIn"])
    types["FilterSpecOut"] = t.struct(
        {
            "columnIndex": t.integer().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "filterCriteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterSpecOut"])
    types["UpdateEmbeddedObjectBorderRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
            "objectId": t.integer().optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestIn"])
    types["UpdateEmbeddedObjectBorderRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "objectId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectBorderRequestOut"])
    types["ChartDateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ChartDateTimeRuleIn"]
    )
    types["ChartDateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartDateTimeRuleOut"])
    types["BorderIn"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "width": t.integer().optional(),
            "style": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["BorderIn"])
    types["BorderOut"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "width": t.integer().optional(),
            "style": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BorderOut"])
    types["AutoFillRequestIn"] = t.struct(
        {
            "useAlternateSeries": t.boolean().optional(),
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationIn"]
            ).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["AutoFillRequestIn"])
    types["AutoFillRequestOut"] = t.struct(
        {
            "useAlternateSeries": t.boolean().optional(),
            "sourceAndDestination": t.proxy(
                renames["SourceAndDestinationOut"]
            ).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoFillRequestOut"])
    types["PivotGroupIn"] = t.struct(
        {
            "sourceColumnOffset": t.integer().optional(),
            "showTotals": t.boolean().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "label": t.string().optional(),
            "sortOrder": t.string().optional(),
            "repeatHeadings": t.boolean().optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitIn"]).optional(),
            "groupRule": t.proxy(renames["PivotGroupRuleIn"]).optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataIn"])
            ).optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketIn"]).optional(),
        }
    ).named(renames["PivotGroupIn"])
    types["PivotGroupOut"] = t.struct(
        {
            "sourceColumnOffset": t.integer().optional(),
            "showTotals": t.boolean().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "label": t.string().optional(),
            "sortOrder": t.string().optional(),
            "repeatHeadings": t.boolean().optional(),
            "groupLimit": t.proxy(renames["PivotGroupLimitOut"]).optional(),
            "groupRule": t.proxy(renames["PivotGroupRuleOut"]).optional(),
            "valueMetadata": t.array(
                t.proxy(renames["PivotGroupValueMetadataOut"])
            ).optional(),
            "valueBucket": t.proxy(renames["PivotGroupSortValueBucketOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotGroupOut"])
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
    types["PivotTableIn"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecIn"])).optional(),
            "values": t.array(t.proxy(renames["PivotValueIn"])).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "valueLayout": t.string().optional(),
            "rows": t.array(t.proxy(renames["PivotGroupIn"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PivotTableIn"])
    types["PivotTableOut"] = t.struct(
        {
            "filterSpecs": t.array(t.proxy(renames["PivotFilterSpecOut"])).optional(),
            "values": t.array(t.proxy(renames["PivotValueOut"])).optional(),
            "dataExecutionStatus": t.proxy(
                renames["DataExecutionStatusOut"]
            ).optional(),
            "dataSourceId": t.string().optional(),
            "columns": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "valueLayout": t.string().optional(),
            "rows": t.array(t.proxy(renames["PivotGroupOut"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotTableOut"])
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
    types["DeleteDimensionGroupRequestIn"] = t.struct(
        {"range": t.proxy(renames["DimensionRangeIn"]).optional()}
    ).named(renames["DeleteDimensionGroupRequestIn"])
    types["DeleteDimensionGroupRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDimensionGroupRequestOut"])
    types["DuplicateSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["DuplicateSheetResponseIn"])
    types["DuplicateSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetResponseOut"])
    types["DeleteNamedRangeRequestIn"] = t.struct(
        {"namedRangeId": t.string().optional()}
    ).named(renames["DeleteNamedRangeRequestIn"])
    types["DeleteNamedRangeRequestOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteNamedRangeRequestOut"])
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
    types["DataSourceColumnReferenceIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["DataSourceColumnReferenceIn"])
    types["DataSourceColumnReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceColumnReferenceOut"])
    types["ChartGroupRuleIn"] = t.struct(
        {
            "dateTimeRule": t.proxy(renames["ChartDateTimeRuleIn"]).optional(),
            "histogramRule": t.proxy(renames["ChartHistogramRuleIn"]).optional(),
        }
    ).named(renames["ChartGroupRuleIn"])
    types["ChartGroupRuleOut"] = t.struct(
        {
            "dateTimeRule": t.proxy(renames["ChartDateTimeRuleOut"]).optional(),
            "histogramRule": t.proxy(renames["ChartHistogramRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartGroupRuleOut"])
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
    types["BatchGetValuesResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "valueRanges": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
        }
    ).named(renames["BatchGetValuesResponseIn"])
    types["BatchGetValuesResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "valueRanges": t.array(t.proxy(renames["ValueRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetValuesResponseOut"])
    types["CellDataIn"] = t.struct(
        {
            "userEnteredValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableIn"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableIn"]).optional(),
            "hyperlink": t.string().optional(),
            "formattedValue": t.string().optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunIn"])).optional(),
            "note": t.string().optional(),
            "effectiveFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "dataValidation": t.proxy(renames["DataValidationRuleIn"]).optional(),
            "effectiveValue": t.proxy(renames["ExtendedValueIn"]).optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatIn"]).optional(),
        }
    ).named(renames["CellDataIn"])
    types["CellDataOut"] = t.struct(
        {
            "userEnteredValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "dataSourceTable": t.proxy(renames["DataSourceTableOut"]).optional(),
            "pivotTable": t.proxy(renames["PivotTableOut"]).optional(),
            "hyperlink": t.string().optional(),
            "formattedValue": t.string().optional(),
            "textFormatRuns": t.array(t.proxy(renames["TextFormatRunOut"])).optional(),
            "note": t.string().optional(),
            "effectiveFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "dataValidation": t.proxy(renames["DataValidationRuleOut"]).optional(),
            "effectiveValue": t.proxy(renames["ExtendedValueOut"]).optional(),
            "dataSourceFormula": t.proxy(renames["DataSourceFormulaOut"]).optional(),
            "userEnteredFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellDataOut"])
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
    types["FindReplaceRequestIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "replacement": t.string().optional(),
            "matchCase": t.boolean().optional(),
            "includeFormulas": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "searchByRegex": t.boolean().optional(),
            "matchEntireCell": t.boolean().optional(),
            "find": t.string().optional(),
            "allSheets": t.boolean().optional(),
        }
    ).named(renames["FindReplaceRequestIn"])
    types["FindReplaceRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "replacement": t.string().optional(),
            "matchCase": t.boolean().optional(),
            "includeFormulas": t.boolean().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "searchByRegex": t.boolean().optional(),
            "matchEntireCell": t.boolean().optional(),
            "find": t.string().optional(),
            "allSheets": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceRequestOut"])
    types["AddProtectedRangeRequestIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeRequestIn"])
    types["AddProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeRequestOut"])
    types["DeleteDeveloperMetadataRequestIn"] = t.struct(
        {"dataFilter": t.proxy(renames["DataFilterIn"]).optional()}
    ).named(renames["DeleteDeveloperMetadataRequestIn"])
    types["DeleteDeveloperMetadataRequestOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDeveloperMetadataRequestOut"])
    types["ExtendedValueIn"] = t.struct(
        {
            "numberValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "errorValue": t.proxy(renames["ErrorValueIn"]).optional(),
            "formulaValue": t.string().optional(),
        }
    ).named(renames["ExtendedValueIn"])
    types["ExtendedValueOut"] = t.struct(
        {
            "numberValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "errorValue": t.proxy(renames["ErrorValueOut"]).optional(),
            "formulaValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedValueOut"])
    types["ChartSourceRangeIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["GridRangeIn"])).optional()}
    ).named(renames["ChartSourceRangeIn"])
    types["ChartSourceRangeOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["GridRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSourceRangeOut"])
    types["GridDataIn"] = t.struct(
        {
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesIn"])
            ).optional(),
            "rowData": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "startColumn": t.integer().optional(),
            "startRow": t.integer().optional(),
        }
    ).named(renames["GridDataIn"])
    types["GridDataOut"] = t.struct(
        {
            "rowMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "columnMetadata": t.array(
                t.proxy(renames["DimensionPropertiesOut"])
            ).optional(),
            "rowData": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "startColumn": t.integer().optional(),
            "startRow": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridDataOut"])
    types["PivotValueIn"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "name": t.string().optional(),
            "summarizeFunction": t.string().optional(),
            "calculatedDisplayType": t.string().optional(),
            "formula": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
        }
    ).named(renames["PivotValueIn"])
    types["PivotValueOut"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "name": t.string().optional(),
            "summarizeFunction": t.string().optional(),
            "calculatedDisplayType": t.string().optional(),
            "formula": t.string().optional(),
            "sourceColumnOffset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueOut"])
    types["CandlestickSeriesIn"] = t.struct(
        {"data": t.proxy(renames["ChartDataIn"]).optional()}
    ).named(renames["CandlestickSeriesIn"])
    types["CandlestickSeriesOut"] = t.struct(
        {
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandlestickSeriesOut"])
    types["SheetPropertiesIn"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "hidden": t.boolean().optional(),
            "sheetType": t.string().optional(),
            "tabColor": t.proxy(renames["ColorIn"]).optional(),
            "rightToLeft": t.boolean().optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "index": t.integer().optional(),
            "title": t.string().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesIn"]).optional(),
        }
    ).named(renames["SheetPropertiesIn"])
    types["SheetPropertiesOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "hidden": t.boolean().optional(),
            "dataSourceSheetProperties": t.proxy(
                renames["DataSourceSheetPropertiesOut"]
            ).optional(),
            "sheetType": t.string().optional(),
            "tabColor": t.proxy(renames["ColorOut"]).optional(),
            "rightToLeft": t.boolean().optional(),
            "tabColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "index": t.integer().optional(),
            "title": t.string().optional(),
            "gridProperties": t.proxy(renames["GridPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetPropertiesOut"])
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
    types["ChartSpecIn"] = t.struct(
        {
            "candlestickChart": t.proxy(renames["CandlestickChartSpecIn"]).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "fontName": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecIn"]).optional(),
            "maximized": t.boolean().optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "title": t.string().optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesIn"]
            ).optional(),
            "pieChart": t.proxy(renames["PieChartSpecIn"]).optional(),
            "basicChart": t.proxy(renames["BasicChartSpecIn"]).optional(),
            "subtitle": t.string().optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "altText": t.string().optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecIn"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "treemapChart": t.proxy(renames["TreemapChartSpecIn"]).optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecIn"]).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecIn"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatIn"]).optional(),
        }
    ).named(renames["ChartSpecIn"])
    types["ChartSpecOut"] = t.struct(
        {
            "candlestickChart": t.proxy(renames["CandlestickChartSpecOut"]).optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "fontName": t.string().optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "orgChart": t.proxy(renames["OrgChartSpecOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "bubbleChart": t.proxy(renames["BubbleChartSpecOut"]).optional(),
            "maximized": t.boolean().optional(),
            "subtitleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "subtitleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "title": t.string().optional(),
            "dataSourceChartProperties": t.proxy(
                renames["DataSourceChartPropertiesOut"]
            ).optional(),
            "pieChart": t.proxy(renames["PieChartSpecOut"]).optional(),
            "basicChart": t.proxy(renames["BasicChartSpecOut"]).optional(),
            "subtitle": t.string().optional(),
            "hiddenDimensionStrategy": t.string().optional(),
            "altText": t.string().optional(),
            "waterfallChart": t.proxy(renames["WaterfallChartSpecOut"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "treemapChart": t.proxy(renames["TreemapChartSpecOut"]).optional(),
            "histogramChart": t.proxy(renames["HistogramChartSpecOut"]).optional(),
            "scorecardChart": t.proxy(renames["ScorecardChartSpecOut"]).optional(),
            "titleTextFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartSpecOut"])
    types["RandomizeRangeRequestIn"] = t.struct(
        {"range": t.proxy(renames["GridRangeIn"]).optional()}
    ).named(renames["RandomizeRangeRequestIn"])
    types["RandomizeRangeRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RandomizeRangeRequestOut"])
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
    types["SetBasicFilterRequestIn"] = t.struct(
        {"filter": t.proxy(renames["BasicFilterIn"]).optional()}
    ).named(renames["SetBasicFilterRequestIn"])
    types["SetBasicFilterRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["BasicFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetBasicFilterRequestOut"])
    types["AddProtectedRangeResponseIn"] = t.struct(
        {"protectedRange": t.proxy(renames["ProtectedRangeIn"]).optional()}
    ).named(renames["AddProtectedRangeResponseIn"])
    types["AddProtectedRangeResponseOut"] = t.struct(
        {
            "protectedRange": t.proxy(renames["ProtectedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddProtectedRangeResponseOut"])
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
    types["DateTimeRuleIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DateTimeRuleIn"]
    )
    types["DateTimeRuleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeRuleOut"])
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
    types["BatchUpdateValuesResponseIn"] = t.struct(
        {
            "totalUpdatedSheets": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "responses": t.array(t.proxy(renames["UpdateValuesResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdateValuesResponseIn"])
    types["BatchUpdateValuesResponseOut"] = t.struct(
        {
            "totalUpdatedSheets": t.integer().optional(),
            "spreadsheetId": t.string().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesResponseOut"])
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
    types["TextToColumnsRequestIn"] = t.struct(
        {
            "delimiter": t.string().optional(),
            "source": t.proxy(renames["GridRangeIn"]).optional(),
            "delimiterType": t.string().optional(),
        }
    ).named(renames["TextToColumnsRequestIn"])
    types["TextToColumnsRequestOut"] = t.struct(
        {
            "delimiter": t.string().optional(),
            "source": t.proxy(renames["GridRangeOut"]).optional(),
            "delimiterType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextToColumnsRequestOut"])
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
    types["BatchClearValuesByDataFilterRequestIn"] = t.struct(
        {"dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional()}
    ).named(renames["BatchClearValuesByDataFilterRequestIn"])
    types["BatchClearValuesByDataFilterRequestOut"] = t.struct(
        {
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchClearValuesByDataFilterRequestOut"])
    types["TrimWhitespaceResponseIn"] = t.struct(
        {"cellsChangedCount": t.integer().optional()}
    ).named(renames["TrimWhitespaceResponseIn"])
    types["TrimWhitespaceResponseOut"] = t.struct(
        {
            "cellsChangedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrimWhitespaceResponseOut"])
    types["DataValidationRuleIn"] = t.struct(
        {
            "inputMessage": t.string().optional(),
            "condition": t.proxy(renames["BooleanConditionIn"]).optional(),
            "showCustomUi": t.boolean().optional(),
            "strict": t.boolean().optional(),
        }
    ).named(renames["DataValidationRuleIn"])
    types["DataValidationRuleOut"] = t.struct(
        {
            "inputMessage": t.string().optional(),
            "condition": t.proxy(renames["BooleanConditionOut"]).optional(),
            "showCustomUi": t.boolean().optional(),
            "strict": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataValidationRuleOut"])
    types["DeleteBandingRequestIn"] = t.struct(
        {"bandedRangeId": t.integer().optional()}
    ).named(renames["DeleteBandingRequestIn"])
    types["DeleteBandingRequestOut"] = t.struct(
        {
            "bandedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBandingRequestOut"])
    types["AddSlicerResponseIn"] = t.struct(
        {"slicer": t.proxy(renames["SlicerIn"]).optional()}
    ).named(renames["AddSlicerResponseIn"])
    types["AddSlicerResponseOut"] = t.struct(
        {
            "slicer": t.proxy(renames["SlicerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSlicerResponseOut"])
    types["CreateDeveloperMetadataRequestIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataRequestIn"])
    types["CreateDeveloperMetadataRequestOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataRequestOut"])
    types["EmbeddedChartIn"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional(),
            "chartId": t.integer().optional(),
            "spec": t.proxy(renames["ChartSpecIn"]).optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderIn"]).optional(),
        }
    ).named(renames["EmbeddedChartIn"])
    types["EmbeddedChartOut"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "chartId": t.integer().optional(),
            "spec": t.proxy(renames["ChartSpecOut"]).optional(),
            "border": t.proxy(renames["EmbeddedObjectBorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbeddedChartOut"])
    types["AddFilterViewRequestIn"] = t.struct(
        {"filter": t.proxy(renames["FilterViewIn"]).optional()}
    ).named(renames["AddFilterViewRequestIn"])
    types["AddFilterViewRequestOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterViewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFilterViewRequestOut"])
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
    types["DeleteDuplicatesResponseIn"] = t.struct(
        {"duplicatesRemovedCount": t.integer().optional()}
    ).named(renames["DeleteDuplicatesResponseIn"])
    types["DeleteDuplicatesResponseOut"] = t.struct(
        {
            "duplicatesRemovedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteDuplicatesResponseOut"])
    types["BordersIn"] = t.struct(
        {
            "top": t.proxy(renames["BorderIn"]).optional(),
            "bottom": t.proxy(renames["BorderIn"]).optional(),
            "right": t.proxy(renames["BorderIn"]).optional(),
            "left": t.proxy(renames["BorderIn"]).optional(),
        }
    ).named(renames["BordersIn"])
    types["BordersOut"] = t.struct(
        {
            "top": t.proxy(renames["BorderOut"]).optional(),
            "bottom": t.proxy(renames["BorderOut"]).optional(),
            "right": t.proxy(renames["BorderOut"]).optional(),
            "left": t.proxy(renames["BorderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BordersOut"])
    types["SpreadsheetIn"] = t.struct(
        {
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeIn"])).optional(),
            "sheets": t.array(t.proxy(renames["SheetIn"])).optional(),
            "spreadsheetId": t.string().optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional(),
            "spreadsheetUrl": t.string().optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesIn"]).optional(),
        }
    ).named(renames["SpreadsheetIn"])
    types["SpreadsheetOut"] = t.struct(
        {
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "dataSourceSchedules": t.array(
                t.proxy(renames["DataSourceRefreshScheduleOut"])
            ).optional(),
            "namedRanges": t.array(t.proxy(renames["NamedRangeOut"])).optional(),
            "sheets": t.array(t.proxy(renames["SheetOut"])).optional(),
            "spreadsheetId": t.string().optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "spreadsheetUrl": t.string().optional(),
            "properties": t.proxy(renames["SpreadsheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetOut"])
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
    types["DeleteConditionalFormatRuleResponseIn"] = t.struct(
        {"rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional()}
    ).named(renames["DeleteConditionalFormatRuleResponseIn"])
    types["DeleteConditionalFormatRuleResponseOut"] = t.struct(
        {
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConditionalFormatRuleResponseOut"])
    types["BandedRangeIn"] = t.struct(
        {
            "columnProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
            "bandedRangeId": t.integer().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "rowProperties": t.proxy(renames["BandingPropertiesIn"]).optional(),
        }
    ).named(renames["BandedRangeIn"])
    types["BandedRangeOut"] = t.struct(
        {
            "columnProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "bandedRangeId": t.integer().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "rowProperties": t.proxy(renames["BandingPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandedRangeOut"])
    types["OrgChartSpecIn"] = t.struct(
        {
            "tooltips": t.proxy(renames["ChartDataIn"]).optional(),
            "selectedNodeColor": t.proxy(renames["ColorIn"]).optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "nodeSize": t.string().optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "nodeColor": t.proxy(renames["ColorIn"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["OrgChartSpecIn"])
    types["OrgChartSpecOut"] = t.struct(
        {
            "tooltips": t.proxy(renames["ChartDataOut"]).optional(),
            "selectedNodeColor": t.proxy(renames["ColorOut"]).optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "nodeSize": t.string().optional(),
            "nodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "nodeColor": t.proxy(renames["ColorOut"]).optional(),
            "selectedNodeColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgChartSpecOut"])
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
    types["UpdateValuesResponseIn"] = t.struct(
        {
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
            "updatedColumns": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "updatedCells": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "spreadsheetId": t.string().optional(),
        }
    ).named(renames["UpdateValuesResponseIn"])
    types["UpdateValuesResponseOut"] = t.struct(
        {
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "updatedColumns": t.integer().optional(),
            "updatedRows": t.integer().optional(),
            "updatedCells": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "spreadsheetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesResponseOut"])
    types["DeleteSheetRequestIn"] = t.struct({"sheetId": t.integer().optional()}).named(
        renames["DeleteSheetRequestIn"]
    )
    types["DeleteSheetRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteSheetRequestOut"])
    types["DeleteProtectedRangeRequestIn"] = t.struct(
        {"protectedRangeId": t.integer().optional()}
    ).named(renames["DeleteProtectedRangeRequestIn"])
    types["DeleteProtectedRangeRequestOut"] = t.struct(
        {
            "protectedRangeId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteProtectedRangeRequestOut"])
    types["CellFormatIn"] = t.struct(
        {
            "padding": t.proxy(renames["PaddingIn"]).optional(),
            "verticalAlignment": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "numberFormat": t.proxy(renames["NumberFormatIn"]).optional(),
            "backgroundColor": t.proxy(renames["ColorIn"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "borders": t.proxy(renames["BordersIn"]).optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "textDirection": t.string().optional(),
            "textRotation": t.proxy(renames["TextRotationIn"]).optional(),
            "wrapStrategy": t.string().optional(),
        }
    ).named(renames["CellFormatIn"])
    types["CellFormatOut"] = t.struct(
        {
            "padding": t.proxy(renames["PaddingOut"]).optional(),
            "verticalAlignment": t.string().optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "numberFormat": t.proxy(renames["NumberFormatOut"]).optional(),
            "backgroundColor": t.proxy(renames["ColorOut"]).optional(),
            "backgroundColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "borders": t.proxy(renames["BordersOut"]).optional(),
            "hyperlinkDisplayType": t.string().optional(),
            "textDirection": t.string().optional(),
            "textRotation": t.proxy(renames["TextRotationOut"]).optional(),
            "wrapStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellFormatOut"])
    types["BatchUpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseIn"])
            ).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseIn"])
    types["BatchUpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "spreadsheetId": t.string().optional(),
            "totalUpdatedSheets": t.integer().optional(),
            "totalUpdatedCells": t.integer().optional(),
            "totalUpdatedRows": t.integer().optional(),
            "totalUpdatedColumns": t.integer().optional(),
            "responses": t.array(
                t.proxy(renames["UpdateValuesByDataFilterResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesByDataFilterResponseOut"])
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
    types["RequestIn"] = t.struct(
        {
            "updateBanding": t.proxy(renames["UpdateBandingRequestIn"]).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestIn"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestIn"]
            ).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestIn"]
            ).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestIn"]
            ).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestIn"]).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestIn"]
            ).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestIn"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestIn"]).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestIn"]
            ).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestIn"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestIn"]
            ).optional(),
            "updateBorders": t.proxy(renames["UpdateBordersRequestIn"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestIn"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestIn"]
            ).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestIn"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestIn"]).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestIn"]).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestIn"]).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestIn"]
            ).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestIn"]
            ).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestIn"]).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestIn"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestIn"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestIn"]).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestIn"]).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestIn"]
            ).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestIn"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestIn"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartRequestIn"]).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestIn"]
            ).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestIn"]).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestIn"]).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestIn"]
            ).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestIn"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestIn"]
            ).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestIn"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestIn"]).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestIn"]).optional(),
            "copyPaste": t.proxy(renames["CopyPasteRequestIn"]).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestIn"]
            ).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestIn"]
            ).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestIn"]).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestIn"]
            ).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestIn"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestIn"]
            ).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestIn"]).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestIn"]).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestIn"]
            ).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestIn"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestIn"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestIn"]
            ).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestIn"]).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestIn"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestIn"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestIn"]).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestIn"]).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestIn"]).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestIn"]).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestIn"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestIn"]
            ).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestIn"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestIn"]
            ).optional(),
            "pasteData": t.proxy(renames["PasteDataRequestIn"]).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "updateBanding": t.proxy(renames["UpdateBandingRequestOut"]).optional(),
            "appendDimension": t.proxy(renames["AppendDimensionRequestOut"]).optional(),
            "deleteDuplicates": t.proxy(
                renames["DeleteDuplicatesRequestOut"]
            ).optional(),
            "updateSpreadsheetProperties": t.proxy(
                renames["UpdateSpreadsheetPropertiesRequestOut"]
            ).optional(),
            "updateDimensionProperties": t.proxy(
                renames["UpdateDimensionPropertiesRequestOut"]
            ).optional(),
            "addFilterView": t.proxy(renames["AddFilterViewRequestOut"]).optional(),
            "deleteProtectedRange": t.proxy(
                renames["DeleteProtectedRangeRequestOut"]
            ).optional(),
            "autoResizeDimensions": t.proxy(
                renames["AutoResizeDimensionsRequestOut"]
            ).optional(),
            "setBasicFilter": t.proxy(renames["SetBasicFilterRequestOut"]).optional(),
            "updateNamedRange": t.proxy(
                renames["UpdateNamedRangeRequestOut"]
            ).optional(),
            "deleteDimension": t.proxy(renames["DeleteDimensionRequestOut"]).optional(),
            "updateDeveloperMetadata": t.proxy(
                renames["UpdateDeveloperMetadataRequestOut"]
            ).optional(),
            "updateBorders": t.proxy(renames["UpdateBordersRequestOut"]).optional(),
            "updateConditionalFormatRule": t.proxy(
                renames["UpdateConditionalFormatRuleRequestOut"]
            ).optional(),
            "updateFilterView": t.proxy(
                renames["UpdateFilterViewRequestOut"]
            ).optional(),
            "unmergeCells": t.proxy(renames["UnmergeCellsRequestOut"]).optional(),
            "deleteSheet": t.proxy(renames["DeleteSheetRequestOut"]).optional(),
            "addSlicer": t.proxy(renames["AddSlicerRequestOut"]).optional(),
            "appendCells": t.proxy(renames["AppendCellsRequestOut"]).optional(),
            "deleteFilterView": t.proxy(
                renames["DeleteFilterViewRequestOut"]
            ).optional(),
            "updateSheetProperties": t.proxy(
                renames["UpdateSheetPropertiesRequestOut"]
            ).optional(),
            "autoFill": t.proxy(renames["AutoFillRequestOut"]).optional(),
            "updateChartSpec": t.proxy(renames["UpdateChartSpecRequestOut"]).optional(),
            "duplicateSheet": t.proxy(renames["DuplicateSheetRequestOut"]).optional(),
            "addDataSource": t.proxy(renames["AddDataSourceRequestOut"]).optional(),
            "addBanding": t.proxy(renames["AddBandingRequestOut"]).optional(),
            "deleteEmbeddedObject": t.proxy(
                renames["DeleteEmbeddedObjectRequestOut"]
            ).optional(),
            "randomizeRange": t.proxy(renames["RandomizeRangeRequestOut"]).optional(),
            "addProtectedRange": t.proxy(
                renames["AddProtectedRangeRequestOut"]
            ).optional(),
            "addChart": t.proxy(renames["AddChartRequestOut"]).optional(),
            "duplicateFilterView": t.proxy(
                renames["DuplicateFilterViewRequestOut"]
            ).optional(),
            "updateCells": t.proxy(renames["UpdateCellsRequestOut"]).optional(),
            "deleteRange": t.proxy(renames["DeleteRangeRequestOut"]).optional(),
            "updateEmbeddedObjectBorder": t.proxy(
                renames["UpdateEmbeddedObjectBorderRequestOut"]
            ).optional(),
            "addConditionalFormatRule": t.proxy(
                renames["AddConditionalFormatRuleRequestOut"]
            ).optional(),
            "updateEmbeddedObjectPosition": t.proxy(
                renames["UpdateEmbeddedObjectPositionRequestOut"]
            ).optional(),
            "updateSlicerSpec": t.proxy(
                renames["UpdateSlicerSpecRequestOut"]
            ).optional(),
            "trimWhitespace": t.proxy(renames["TrimWhitespaceRequestOut"]).optional(),
            "moveDimension": t.proxy(renames["MoveDimensionRequestOut"]).optional(),
            "copyPaste": t.proxy(renames["CopyPasteRequestOut"]).optional(),
            "updateDimensionGroup": t.proxy(
                renames["UpdateDimensionGroupRequestOut"]
            ).optional(),
            "updateProtectedRange": t.proxy(
                renames["UpdateProtectedRangeRequestOut"]
            ).optional(),
            "sortRange": t.proxy(renames["SortRangeRequestOut"]).optional(),
            "deleteDataSource": t.proxy(
                renames["DeleteDataSourceRequestOut"]
            ).optional(),
            "createDeveloperMetadata": t.proxy(
                renames["CreateDeveloperMetadataRequestOut"]
            ).optional(),
            "deleteDeveloperMetadata": t.proxy(
                renames["DeleteDeveloperMetadataRequestOut"]
            ).optional(),
            "deleteBanding": t.proxy(renames["DeleteBandingRequestOut"]).optional(),
            "insertRange": t.proxy(renames["InsertRangeRequestOut"]).optional(),
            "clearBasicFilter": t.proxy(
                renames["ClearBasicFilterRequestOut"]
            ).optional(),
            "refreshDataSource": t.proxy(
                renames["RefreshDataSourceRequestOut"]
            ).optional(),
            "deleteNamedRange": t.proxy(
                renames["DeleteNamedRangeRequestOut"]
            ).optional(),
            "deleteDimensionGroup": t.proxy(
                renames["DeleteDimensionGroupRequestOut"]
            ).optional(),
            "mergeCells": t.proxy(renames["MergeCellsRequestOut"]).optional(),
            "setDataValidation": t.proxy(
                renames["SetDataValidationRequestOut"]
            ).optional(),
            "deleteConditionalFormatRule": t.proxy(
                renames["DeleteConditionalFormatRuleRequestOut"]
            ).optional(),
            "addNamedRange": t.proxy(renames["AddNamedRangeRequestOut"]).optional(),
            "findReplace": t.proxy(renames["FindReplaceRequestOut"]).optional(),
            "insertDimension": t.proxy(renames["InsertDimensionRequestOut"]).optional(),
            "addSheet": t.proxy(renames["AddSheetRequestOut"]).optional(),
            "cutPaste": t.proxy(renames["CutPasteRequestOut"]).optional(),
            "addDimensionGroup": t.proxy(
                renames["AddDimensionGroupRequestOut"]
            ).optional(),
            "repeatCell": t.proxy(renames["RepeatCellRequestOut"]).optional(),
            "updateDataSource": t.proxy(
                renames["UpdateDataSourceRequestOut"]
            ).optional(),
            "pasteData": t.proxy(renames["PasteDataRequestOut"]).optional(),
            "textToColumns": t.proxy(renames["TextToColumnsRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["UpdateConditionalFormatRuleRequestIn"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "index": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestIn"])
    types["UpdateConditionalFormatRuleRequestOut"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "index": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "rule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleRequestOut"])
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
    types["TreemapChartSpecIn"] = t.struct(
        {
            "headerColor": t.proxy(renames["ColorIn"]).optional(),
            "hintedLevels": t.integer().optional(),
            "maxValue": t.number().optional(),
            "minValue": t.number().optional(),
            "sizeData": t.proxy(renames["ChartDataIn"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "colorData": t.proxy(renames["ChartDataIn"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "colorScale": t.proxy(renames["TreemapChartColorScaleIn"]).optional(),
            "textFormat": t.proxy(renames["TextFormatIn"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "labels": t.proxy(renames["ChartDataIn"]).optional(),
            "levels": t.integer().optional(),
        }
    ).named(renames["TreemapChartSpecIn"])
    types["TreemapChartSpecOut"] = t.struct(
        {
            "headerColor": t.proxy(renames["ColorOut"]).optional(),
            "hintedLevels": t.integer().optional(),
            "maxValue": t.number().optional(),
            "minValue": t.number().optional(),
            "sizeData": t.proxy(renames["ChartDataOut"]).optional(),
            "headerColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "colorData": t.proxy(renames["ChartDataOut"]).optional(),
            "parentLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "colorScale": t.proxy(renames["TreemapChartColorScaleOut"]).optional(),
            "textFormat": t.proxy(renames["TextFormatOut"]).optional(),
            "hideTooltips": t.boolean().optional(),
            "labels": t.proxy(renames["ChartDataOut"]).optional(),
            "levels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartSpecOut"])
    types["ClearBasicFilterRequestIn"] = t.struct(
        {"sheetId": t.integer().optional()}
    ).named(renames["ClearBasicFilterRequestIn"])
    types["ClearBasicFilterRequestOut"] = t.struct(
        {
            "sheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearBasicFilterRequestOut"])
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
    types["TreemapChartColorScaleIn"] = t.struct(
        {
            "maxValueColor": t.proxy(renames["ColorIn"]).optional(),
            "minValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "maxValueColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "midValueColor": t.proxy(renames["ColorIn"]).optional(),
            "minValueColor": t.proxy(renames["ColorIn"]).optional(),
            "noDataColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "noDataColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleIn"])
    types["TreemapChartColorScaleOut"] = t.struct(
        {
            "maxValueColor": t.proxy(renames["ColorOut"]).optional(),
            "minValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "midValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "maxValueColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "midValueColor": t.proxy(renames["ColorOut"]).optional(),
            "minValueColor": t.proxy(renames["ColorOut"]).optional(),
            "noDataColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "noDataColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TreemapChartColorScaleOut"])
    types["BatchUpdateValuesRequestIn"] = t.struct(
        {
            "includeValuesInResponse": t.boolean().optional(),
            "responseValueRenderOption": t.string().optional(),
            "valueInputOption": t.string().optional(),
            "data": t.array(t.proxy(renames["ValueRangeIn"])).optional(),
            "responseDateTimeRenderOption": t.string().optional(),
        }
    ).named(renames["BatchUpdateValuesRequestIn"])
    types["BatchUpdateValuesRequestOut"] = t.struct(
        {
            "includeValuesInResponse": t.boolean().optional(),
            "responseValueRenderOption": t.string().optional(),
            "valueInputOption": t.string().optional(),
            "data": t.array(t.proxy(renames["ValueRangeOut"])).optional(),
            "responseDateTimeRenderOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateValuesRequestOut"])
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
    types["RowDataIn"] = t.struct(
        {"values": t.array(t.proxy(renames["CellDataIn"])).optional()}
    ).named(renames["RowDataIn"])
    types["RowDataOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CellDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowDataOut"])
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
    types["UpdateConditionalFormatRuleResponseIn"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "oldIndex": t.integer().optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
            "newRule": t.proxy(renames["ConditionalFormatRuleIn"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseIn"])
    types["UpdateConditionalFormatRuleResponseOut"] = t.struct(
        {
            "newIndex": t.integer().optional(),
            "oldIndex": t.integer().optional(),
            "oldRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "newRule": t.proxy(renames["ConditionalFormatRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConditionalFormatRuleResponseOut"])
    types["FindReplaceResponseIn"] = t.struct(
        {
            "rowsChanged": t.integer().optional(),
            "occurrencesChanged": t.integer().optional(),
            "sheetsChanged": t.integer().optional(),
            "formulasChanged": t.integer().optional(),
            "valuesChanged": t.integer().optional(),
        }
    ).named(renames["FindReplaceResponseIn"])
    types["FindReplaceResponseOut"] = t.struct(
        {
            "rowsChanged": t.integer().optional(),
            "occurrencesChanged": t.integer().optional(),
            "sheetsChanged": t.integer().optional(),
            "formulasChanged": t.integer().optional(),
            "valuesChanged": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindReplaceResponseOut"])
    types["UpdateCellsRequestIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowDataIn"])).optional(),
            "fields": t.string().optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
            "start": t.proxy(renames["GridCoordinateIn"]).optional(),
        }
    ).named(renames["UpdateCellsRequestIn"])
    types["UpdateCellsRequestOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowDataOut"])).optional(),
            "fields": t.string().optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "start": t.proxy(renames["GridCoordinateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCellsRequestOut"])
    types["PivotFilterSpecIn"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceIn"]
            ).optional(),
            "columnOffsetIndex": t.integer().optional(),
            "filterCriteria": t.proxy(renames["PivotFilterCriteriaIn"]).optional(),
        }
    ).named(renames["PivotFilterSpecIn"])
    types["PivotFilterSpecOut"] = t.struct(
        {
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "columnOffsetIndex": t.integer().optional(),
            "filterCriteria": t.proxy(renames["PivotFilterCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotFilterSpecOut"])
    types["GridRangeIn"] = t.struct(
        {
            "startRowIndex": t.integer().optional(),
            "startColumnIndex": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "endRowIndex": t.integer().optional(),
        }
    ).named(renames["GridRangeIn"])
    types["GridRangeOut"] = t.struct(
        {
            "startRowIndex": t.integer().optional(),
            "startColumnIndex": t.integer().optional(),
            "endColumnIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "endRowIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridRangeOut"])
    types["FilterViewIn"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "title": t.string().optional(),
            "filterViewId": t.integer().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecIn"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecIn"])).optional(),
            "range": t.proxy(renames["GridRangeIn"]).optional(),
        }
    ).named(renames["FilterViewIn"])
    types["FilterViewOut"] = t.struct(
        {
            "namedRangeId": t.string().optional(),
            "title": t.string().optional(),
            "filterViewId": t.integer().optional(),
            "sortSpecs": t.array(t.proxy(renames["SortSpecOut"])).optional(),
            "criteria": t.struct({"_": t.string().optional()}).optional(),
            "filterSpecs": t.array(t.proxy(renames["FilterSpecOut"])).optional(),
            "range": t.proxy(renames["GridRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterViewOut"])
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
    types["BasicChartAxisIn"] = t.struct(
        {
            "title": t.string().optional(),
            "format": t.proxy(renames["TextFormatIn"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionIn"]).optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsIn"]
            ).optional(),
            "position": t.string().optional(),
        }
    ).named(renames["BasicChartAxisIn"])
    types["BasicChartAxisOut"] = t.struct(
        {
            "title": t.string().optional(),
            "format": t.proxy(renames["TextFormatOut"]).optional(),
            "titleTextPosition": t.proxy(renames["TextPositionOut"]).optional(),
            "viewWindowOptions": t.proxy(
                renames["ChartAxisViewWindowOptionsOut"]
            ).optional(),
            "position": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartAxisOut"])
    types["BasicSeriesDataPointStyleOverrideIn"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideIn"])
    types["BasicSeriesDataPointStyleOverrideOut"] = t.struct(
        {
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSeriesDataPointStyleOverrideOut"])
    types["BasicChartSeriesIn"] = t.struct(
        {
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideIn"])
            ).optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "lineStyle": t.proxy(renames["LineStyleIn"]).optional(),
            "targetAxis": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleIn"]).optional(),
            "type": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
        }
    ).named(renames["BasicChartSeriesIn"])
    types["BasicChartSeriesOut"] = t.struct(
        {
            "styleOverrides": t.array(
                t.proxy(renames["BasicSeriesDataPointStyleOverrideOut"])
            ).optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "lineStyle": t.proxy(renames["LineStyleOut"]).optional(),
            "targetAxis": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "pointStyle": t.proxy(renames["PointStyleOut"]).optional(),
            "type": t.string().optional(),
            "colorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicChartSeriesOut"])
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
    types["AddSheetResponseIn"] = t.struct(
        {"properties": t.proxy(renames["SheetPropertiesIn"]).optional()}
    ).named(renames["AddSheetResponseIn"])
    types["AddSheetResponseOut"] = t.struct(
        {
            "properties": t.proxy(renames["SheetPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSheetResponseOut"])
    types["DuplicateFilterViewRequestIn"] = t.struct(
        {"filterId": t.integer().optional()}
    ).named(renames["DuplicateFilterViewRequestIn"])
    types["DuplicateFilterViewRequestOut"] = t.struct(
        {
            "filterId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateFilterViewRequestOut"])
    types["UpdateEmbeddedObjectPositionResponseIn"] = t.struct(
        {"position": t.proxy(renames["EmbeddedObjectPositionIn"]).optional()}
    ).named(renames["UpdateEmbeddedObjectPositionResponseIn"])
    types["UpdateEmbeddedObjectPositionResponseOut"] = t.struct(
        {
            "position": t.proxy(renames["EmbeddedObjectPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEmbeddedObjectPositionResponseOut"])
    types["UpdateDeveloperMetadataRequestIn"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional(),
            "fields": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestIn"])
    types["UpdateDeveloperMetadataRequestOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "fields": t.string().optional(),
            "dataFilters": t.array(t.proxy(renames["DataFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeveloperMetadataRequestOut"])
    types["UpdateNamedRangeRequestIn"] = t.struct(
        {
            "fields": t.string().optional(),
            "namedRange": t.proxy(renames["NamedRangeIn"]).optional(),
        }
    ).named(renames["UpdateNamedRangeRequestIn"])
    types["UpdateNamedRangeRequestOut"] = t.struct(
        {
            "fields": t.string().optional(),
            "namedRange": t.proxy(renames["NamedRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateNamedRangeRequestOut"])
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
    types["UpdateValuesByDataFilterResponseIn"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterIn"]).optional(),
            "updatedColumns": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedCells": t.integer().optional(),
            "updatedData": t.proxy(renames["ValueRangeIn"]).optional(),
            "updatedRows": t.integer().optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseIn"])
    types["UpdateValuesByDataFilterResponseOut"] = t.struct(
        {
            "dataFilter": t.proxy(renames["DataFilterOut"]).optional(),
            "updatedColumns": t.integer().optional(),
            "updatedRange": t.string().optional(),
            "updatedCells": t.integer().optional(),
            "updatedData": t.proxy(renames["ValueRangeOut"]).optional(),
            "updatedRows": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateValuesByDataFilterResponseOut"])
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
    types["DuplicateSheetRequestIn"] = t.struct(
        {
            "newSheetName": t.string().optional(),
            "newSheetId": t.integer().optional(),
            "insertSheetIndex": t.integer().optional(),
            "sourceSheetId": t.integer().optional(),
        }
    ).named(renames["DuplicateSheetRequestIn"])
    types["DuplicateSheetRequestOut"] = t.struct(
        {
            "newSheetName": t.string().optional(),
            "newSheetId": t.integer().optional(),
            "insertSheetIndex": t.integer().optional(),
            "sourceSheetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateSheetRequestOut"])
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
    types["SpreadsheetPropertiesIn"] = t.struct(
        {
            "locale": t.string().optional(),
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeIn"]).optional(),
            "timeZone": t.string().optional(),
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsIn"]
            ).optional(),
            "defaultFormat": t.proxy(renames["CellFormatIn"]).optional(),
            "autoRecalc": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["SpreadsheetPropertiesIn"])
    types["SpreadsheetPropertiesOut"] = t.struct(
        {
            "locale": t.string().optional(),
            "spreadsheetTheme": t.proxy(renames["SpreadsheetThemeOut"]).optional(),
            "timeZone": t.string().optional(),
            "iterativeCalculationSettings": t.proxy(
                renames["IterativeCalculationSettingsOut"]
            ).optional(),
            "defaultFormat": t.proxy(renames["CellFormatOut"]).optional(),
            "autoRecalc": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpreadsheetPropertiesOut"])
    types["ChartHistogramRuleIn"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "minValue": t.number().optional(),
            "intervalSize": t.number().optional(),
        }
    ).named(renames["ChartHistogramRuleIn"])
    types["ChartHistogramRuleOut"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "minValue": t.number().optional(),
            "intervalSize": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartHistogramRuleOut"])
    types["BubbleChartSpecIn"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleMaxRadiusSize": t.integer().optional(),
            "series": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleBorderColor": t.proxy(renames["ColorIn"]).optional(),
            "bubbleSizes": t.proxy(renames["ChartDataIn"]).optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatIn"]).optional(),
            "bubbleOpacity": t.number().optional(),
            "bubbleLabels": t.proxy(renames["ChartDataIn"]).optional(),
            "legendPosition": t.string().optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleIn"]).optional(),
            "groupIds": t.proxy(renames["ChartDataIn"]).optional(),
        }
    ).named(renames["BubbleChartSpecIn"])
    types["BubbleChartSpecOut"] = t.struct(
        {
            "domain": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleMaxRadiusSize": t.integer().optional(),
            "series": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleBorderColor": t.proxy(renames["ColorOut"]).optional(),
            "bubbleSizes": t.proxy(renames["ChartDataOut"]).optional(),
            "bubbleTextStyle": t.proxy(renames["TextFormatOut"]).optional(),
            "bubbleOpacity": t.number().optional(),
            "bubbleLabels": t.proxy(renames["ChartDataOut"]).optional(),
            "legendPosition": t.string().optional(),
            "bubbleMinRadiusSize": t.integer().optional(),
            "bubbleBorderColorStyle": t.proxy(renames["ColorStyleOut"]).optional(),
            "groupIds": t.proxy(renames["ChartDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BubbleChartSpecOut"])
    types["DimensionRangeIn"] = t.struct(
        {
            "dimension": t.string().optional(),
            "startIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["DimensionRangeIn"])
    types["DimensionRangeOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "startIndex": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionRangeOut"])
    types["AppendDimensionRequestIn"] = t.struct(
        {
            "length": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["AppendDimensionRequestIn"])
    types["AppendDimensionRequestOut"] = t.struct(
        {
            "length": t.integer().optional(),
            "sheetId": t.integer().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppendDimensionRequestOut"])
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
    types["WaterfallChartSeriesIn"] = t.struct(
        {
            "dataLabel": t.proxy(renames["DataLabelIn"]).optional(),
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "subtotalColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "customSubtotals": t.array(
                t.proxy(renames["WaterfallChartCustomSubtotalIn"])
            ).optional(),
            "data": t.proxy(renames["ChartDataIn"]).optional(),
            "positiveColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleIn"]
            ).optional(),
            "hideTrailingSubtotal": t.boolean().optional(),
        }
    ).named(renames["WaterfallChartSeriesIn"])
    types["WaterfallChartSeriesOut"] = t.struct(
        {
            "dataLabel": t.proxy(renames["DataLabelOut"]).optional(),
            "negativeColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "subtotalColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "customSubtotals": t.array(
                t.proxy(renames["WaterfallChartCustomSubtotalOut"])
            ).optional(),
            "data": t.proxy(renames["ChartDataOut"]).optional(),
            "positiveColumnsStyle": t.proxy(
                renames["WaterfallChartColumnStyleOut"]
            ).optional(),
            "hideTrailingSubtotal": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterfallChartSeriesOut"])
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
    types["ChartAxisViewWindowOptionsIn"] = t.struct(
        {
            "viewWindowMin": t.number().optional(),
            "viewWindowMax": t.number().optional(),
            "viewWindowMode": t.string().optional(),
        }
    ).named(renames["ChartAxisViewWindowOptionsIn"])
    types["ChartAxisViewWindowOptionsOut"] = t.struct(
        {
            "viewWindowMin": t.number().optional(),
            "viewWindowMax": t.number().optional(),
            "viewWindowMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChartAxisViewWindowOptionsOut"])
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
    types["DeveloperMetadataLocationIn"] = t.struct(
        {
            "dimensionRange": t.proxy(renames["DimensionRangeIn"]).optional(),
            "spreadsheet": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "locationType": t.string().optional(),
        }
    ).named(renames["DeveloperMetadataLocationIn"])
    types["DeveloperMetadataLocationOut"] = t.struct(
        {
            "dimensionRange": t.proxy(renames["DimensionRangeOut"]).optional(),
            "spreadsheet": t.boolean().optional(),
            "sheetId": t.integer().optional(),
            "locationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperMetadataLocationOut"])
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
    types["DimensionPropertiesIn"] = t.struct(
        {
            "hiddenByFilter": t.boolean().optional(),
            "pixelSize": t.integer().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataIn"])
            ).optional(),
            "hiddenByUser": t.boolean().optional(),
        }
    ).named(renames["DimensionPropertiesIn"])
    types["DimensionPropertiesOut"] = t.struct(
        {
            "hiddenByFilter": t.boolean().optional(),
            "dataSourceColumnReference": t.proxy(
                renames["DataSourceColumnReferenceOut"]
            ).optional(),
            "pixelSize": t.integer().optional(),
            "developerMetadata": t.array(
                t.proxy(renames["DeveloperMetadataOut"])
            ).optional(),
            "hiddenByUser": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionPropertiesOut"])
    types["InsertDimensionRequestIn"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeIn"]).optional(),
            "inheritFromBefore": t.boolean().optional(),
        }
    ).named(renames["InsertDimensionRequestIn"])
    types["InsertDimensionRequestOut"] = t.struct(
        {
            "range": t.proxy(renames["DimensionRangeOut"]).optional(),
            "inheritFromBefore": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertDimensionRequestOut"])
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
    types["RefreshDataSourceRequestIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "isAll": t.boolean().optional(),
            "dataSourceId": t.string().optional(),
            "references": t.proxy(renames["DataSourceObjectReferencesIn"]).optional(),
        }
    ).named(renames["RefreshDataSourceRequestIn"])
    types["RefreshDataSourceRequestOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "isAll": t.boolean().optional(),
            "dataSourceId": t.string().optional(),
            "references": t.proxy(renames["DataSourceObjectReferencesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefreshDataSourceRequestOut"])
    types["AddChartRequestIn"] = t.struct(
        {"chart": t.proxy(renames["EmbeddedChartIn"]).optional()}
    ).named(renames["AddChartRequestIn"])
    types["AddChartRequestOut"] = t.struct(
        {
            "chart": t.proxy(renames["EmbeddedChartOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddChartRequestOut"])
    types["CreateDeveloperMetadataResponseIn"] = t.struct(
        {"developerMetadata": t.proxy(renames["DeveloperMetadataIn"]).optional()}
    ).named(renames["CreateDeveloperMetadataResponseIn"])
    types["CreateDeveloperMetadataResponseOut"] = t.struct(
        {
            "developerMetadata": t.proxy(renames["DeveloperMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDeveloperMetadataResponseOut"])

    functions = {}
    functions["spreadsheetsBatchUpdate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}:getByDataFilter",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsGet"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}:getByDataFilter",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsCreate"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}:getByDataFilter",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spreadsheetsGetByDataFilter"] = sheets.post(
        "v4/spreadsheets/{spreadsheetId}:getByDataFilter",
        t.struct(
            {
                "spreadsheetId": t.string().optional(),
                "includeGridData": t.boolean().optional(),
                "dataFilters": t.array(t.proxy(renames["DataFilterIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpreadsheetOut"]),
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

    return Import(
        importer="sheets", renames=renames, types=Box(types), functions=Box(functions)
    )
