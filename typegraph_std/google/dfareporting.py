from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_dfareporting() -> Import:
    dfareporting = HTTPRuntime("https://dfareporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_dfareporting_1_ErrorResponse",
        "AccountIn": "_dfareporting_2_AccountIn",
        "AccountOut": "_dfareporting_3_AccountOut",
        "MobileAppsListResponseIn": "_dfareporting_4_MobileAppsListResponseIn",
        "MobileAppsListResponseOut": "_dfareporting_5_MobileAppsListResponseOut",
        "UvarFilterIn": "_dfareporting_6_UvarFilterIn",
        "UvarFilterOut": "_dfareporting_7_UvarFilterOut",
        "OrdersListResponseIn": "_dfareporting_8_OrdersListResponseIn",
        "OrdersListResponseOut": "_dfareporting_9_OrdersListResponseOut",
        "RegionsListResponseIn": "_dfareporting_10_RegionsListResponseIn",
        "RegionsListResponseOut": "_dfareporting_11_RegionsListResponseOut",
        "MeasurementPartnerAdvertiserLinkIn": "_dfareporting_12_MeasurementPartnerAdvertiserLinkIn",
        "MeasurementPartnerAdvertiserLinkOut": "_dfareporting_13_MeasurementPartnerAdvertiserLinkOut",
        "UserRolePermissionIn": "_dfareporting_14_UserRolePermissionIn",
        "UserRolePermissionOut": "_dfareporting_15_UserRolePermissionOut",
        "PostalCodesListResponseIn": "_dfareporting_16_PostalCodesListResponseIn",
        "PostalCodesListResponseOut": "_dfareporting_17_PostalCodesListResponseOut",
        "TargetableRemarketingListsListResponseIn": "_dfareporting_18_TargetableRemarketingListsListResponseIn",
        "TargetableRemarketingListsListResponseOut": "_dfareporting_19_TargetableRemarketingListsListResponseOut",
        "DateRangeIn": "_dfareporting_20_DateRangeIn",
        "DateRangeOut": "_dfareporting_21_DateRangeOut",
        "AccountPermissionGroupsListResponseIn": "_dfareporting_22_AccountPermissionGroupsListResponseIn",
        "AccountPermissionGroupsListResponseOut": "_dfareporting_23_AccountPermissionGroupsListResponseOut",
        "PathReportCompatibleFieldsIn": "_dfareporting_24_PathReportCompatibleFieldsIn",
        "PathReportCompatibleFieldsOut": "_dfareporting_25_PathReportCompatibleFieldsOut",
        "VideoOffsetIn": "_dfareporting_26_VideoOffsetIn",
        "VideoOffsetOut": "_dfareporting_27_VideoOffsetOut",
        "CampaignCreativeAssociationIn": "_dfareporting_28_CampaignCreativeAssociationIn",
        "CampaignCreativeAssociationOut": "_dfareporting_29_CampaignCreativeAssociationOut",
        "EventTagOverrideIn": "_dfareporting_30_EventTagOverrideIn",
        "EventTagOverrideOut": "_dfareporting_31_EventTagOverrideOut",
        "OrderContactIn": "_dfareporting_32_OrderContactIn",
        "OrderContactOut": "_dfareporting_33_OrderContactOut",
        "SkippableSettingIn": "_dfareporting_34_SkippableSettingIn",
        "SkippableSettingOut": "_dfareporting_35_SkippableSettingOut",
        "ConversionIn": "_dfareporting_36_ConversionIn",
        "ConversionOut": "_dfareporting_37_ConversionOut",
        "CustomRichMediaEventsIn": "_dfareporting_38_CustomRichMediaEventsIn",
        "CustomRichMediaEventsOut": "_dfareporting_39_CustomRichMediaEventsOut",
        "UserDefinedVariableConfigurationIn": "_dfareporting_40_UserDefinedVariableConfigurationIn",
        "UserDefinedVariableConfigurationOut": "_dfareporting_41_UserDefinedVariableConfigurationOut",
        "UserProfileListIn": "_dfareporting_42_UserProfileListIn",
        "UserProfileListOut": "_dfareporting_43_UserProfileListOut",
        "SiteVideoSettingsIn": "_dfareporting_44_SiteVideoSettingsIn",
        "SiteVideoSettingsOut": "_dfareporting_45_SiteVideoSettingsOut",
        "PostalCodeIn": "_dfareporting_46_PostalCodeIn",
        "PostalCodeOut": "_dfareporting_47_PostalCodeOut",
        "DayPartTargetingIn": "_dfareporting_48_DayPartTargetingIn",
        "DayPartTargetingOut": "_dfareporting_49_DayPartTargetingOut",
        "CountriesListResponseIn": "_dfareporting_50_CountriesListResponseIn",
        "CountriesListResponseOut": "_dfareporting_51_CountriesListResponseOut",
        "ProjectsListResponseIn": "_dfareporting_52_ProjectsListResponseIn",
        "ProjectsListResponseOut": "_dfareporting_53_ProjectsListResponseOut",
        "BillingRateTieredRateIn": "_dfareporting_54_BillingRateTieredRateIn",
        "BillingRateTieredRateOut": "_dfareporting_55_BillingRateTieredRateOut",
        "CreativeCustomEventIn": "_dfareporting_56_CreativeCustomEventIn",
        "CreativeCustomEventOut": "_dfareporting_57_CreativeCustomEventOut",
        "DimensionIn": "_dfareporting_58_DimensionIn",
        "DimensionOut": "_dfareporting_59_DimensionOut",
        "TagSettingIn": "_dfareporting_60_TagSettingIn",
        "TagSettingOut": "_dfareporting_61_TagSettingOut",
        "DirectorySiteIn": "_dfareporting_62_DirectorySiteIn",
        "DirectorySiteOut": "_dfareporting_63_DirectorySiteOut",
        "PathToConversionReportCompatibleFieldsIn": "_dfareporting_64_PathToConversionReportCompatibleFieldsIn",
        "PathToConversionReportCompatibleFieldsOut": "_dfareporting_65_PathToConversionReportCompatibleFieldsOut",
        "UserRoleIn": "_dfareporting_66_UserRoleIn",
        "UserRoleOut": "_dfareporting_67_UserRoleOut",
        "FloodlightActivityDynamicTagIn": "_dfareporting_68_FloodlightActivityDynamicTagIn",
        "FloodlightActivityDynamicTagOut": "_dfareporting_69_FloodlightActivityDynamicTagOut",
        "CompanionSettingIn": "_dfareporting_70_CompanionSettingIn",
        "CompanionSettingOut": "_dfareporting_71_CompanionSettingOut",
        "CityIn": "_dfareporting_72_CityIn",
        "CityOut": "_dfareporting_73_CityOut",
        "DefaultClickThroughEventTagPropertiesIn": "_dfareporting_74_DefaultClickThroughEventTagPropertiesIn",
        "DefaultClickThroughEventTagPropertiesOut": "_dfareporting_75_DefaultClickThroughEventTagPropertiesOut",
        "SitesListResponseIn": "_dfareporting_76_SitesListResponseIn",
        "SitesListResponseOut": "_dfareporting_77_SitesListResponseOut",
        "CreativeGroupAssignmentIn": "_dfareporting_78_CreativeGroupAssignmentIn",
        "CreativeGroupAssignmentOut": "_dfareporting_79_CreativeGroupAssignmentOut",
        "DimensionValueListIn": "_dfareporting_80_DimensionValueListIn",
        "DimensionValueListOut": "_dfareporting_81_DimensionValueListOut",
        "CreativeAssignmentIn": "_dfareporting_82_CreativeAssignmentIn",
        "CreativeAssignmentOut": "_dfareporting_83_CreativeAssignmentOut",
        "AccountPermissionGroupIn": "_dfareporting_84_AccountPermissionGroupIn",
        "AccountPermissionGroupOut": "_dfareporting_85_AccountPermissionGroupOut",
        "AdvertiserInvoicesListResponseIn": "_dfareporting_86_AdvertiserInvoicesListResponseIn",
        "AdvertiserInvoicesListResponseOut": "_dfareporting_87_AdvertiserInvoicesListResponseOut",
        "BillingProfileIn": "_dfareporting_88_BillingProfileIn",
        "BillingProfileOut": "_dfareporting_89_BillingProfileOut",
        "PlacementAssignmentIn": "_dfareporting_90_PlacementAssignmentIn",
        "PlacementAssignmentOut": "_dfareporting_91_PlacementAssignmentOut",
        "ConversionsBatchInsertResponseIn": "_dfareporting_92_ConversionsBatchInsertResponseIn",
        "ConversionsBatchInsertResponseOut": "_dfareporting_93_ConversionsBatchInsertResponseOut",
        "CreativeFieldsListResponseIn": "_dfareporting_94_CreativeFieldsListResponseIn",
        "CreativeFieldsListResponseOut": "_dfareporting_95_CreativeFieldsListResponseOut",
        "LandingPageIn": "_dfareporting_96_LandingPageIn",
        "LandingPageOut": "_dfareporting_97_LandingPageOut",
        "ReportsConfigurationIn": "_dfareporting_98_ReportsConfigurationIn",
        "ReportsConfigurationOut": "_dfareporting_99_ReportsConfigurationOut",
        "UserProfileIn": "_dfareporting_100_UserProfileIn",
        "UserProfileOut": "_dfareporting_101_UserProfileOut",
        "PlacementIn": "_dfareporting_102_PlacementIn",
        "PlacementOut": "_dfareporting_103_PlacementOut",
        "CreativesListResponseIn": "_dfareporting_104_CreativesListResponseIn",
        "CreativesListResponseOut": "_dfareporting_105_CreativesListResponseOut",
        "RemarketingListsListResponseIn": "_dfareporting_106_RemarketingListsListResponseIn",
        "RemarketingListsListResponseOut": "_dfareporting_107_RemarketingListsListResponseOut",
        "OrderDocumentsListResponseIn": "_dfareporting_108_OrderDocumentsListResponseIn",
        "OrderDocumentsListResponseOut": "_dfareporting_109_OrderDocumentsListResponseOut",
        "TranscodeSettingIn": "_dfareporting_110_TranscodeSettingIn",
        "TranscodeSettingOut": "_dfareporting_111_TranscodeSettingOut",
        "MobileCarriersListResponseIn": "_dfareporting_112_MobileCarriersListResponseIn",
        "MobileCarriersListResponseOut": "_dfareporting_113_MobileCarriersListResponseOut",
        "OffsetPositionIn": "_dfareporting_114_OffsetPositionIn",
        "OffsetPositionOut": "_dfareporting_115_OffsetPositionOut",
        "ActivitiesIn": "_dfareporting_116_ActivitiesIn",
        "ActivitiesOut": "_dfareporting_117_ActivitiesOut",
        "FloodlightConfigurationsListResponseIn": "_dfareporting_118_FloodlightConfigurationsListResponseIn",
        "FloodlightConfigurationsListResponseOut": "_dfareporting_119_FloodlightConfigurationsListResponseOut",
        "AdvertiserIn": "_dfareporting_120_AdvertiserIn",
        "AdvertiserOut": "_dfareporting_121_AdvertiserOut",
        "PopupWindowPropertiesIn": "_dfareporting_122_PopupWindowPropertiesIn",
        "PopupWindowPropertiesOut": "_dfareporting_123_PopupWindowPropertiesOut",
        "ReportCompatibleFieldsIn": "_dfareporting_124_ReportCompatibleFieldsIn",
        "ReportCompatibleFieldsOut": "_dfareporting_125_ReportCompatibleFieldsOut",
        "MetrosListResponseIn": "_dfareporting_126_MetrosListResponseIn",
        "MetrosListResponseOut": "_dfareporting_127_MetrosListResponseOut",
        "UserRolePermissionGroupIn": "_dfareporting_128_UserRolePermissionGroupIn",
        "UserRolePermissionGroupOut": "_dfareporting_129_UserRolePermissionGroupOut",
        "AudienceSegmentGroupIn": "_dfareporting_130_AudienceSegmentGroupIn",
        "AudienceSegmentGroupOut": "_dfareporting_131_AudienceSegmentGroupOut",
        "ConnectionTypesListResponseIn": "_dfareporting_132_ConnectionTypesListResponseIn",
        "ConnectionTypesListResponseOut": "_dfareporting_133_ConnectionTypesListResponseOut",
        "PlatformTypeIn": "_dfareporting_134_PlatformTypeIn",
        "PlatformTypeOut": "_dfareporting_135_PlatformTypeOut",
        "CreativeGroupIn": "_dfareporting_136_CreativeGroupIn",
        "CreativeGroupOut": "_dfareporting_137_CreativeGroupOut",
        "CreativeAssetIn": "_dfareporting_138_CreativeAssetIn",
        "CreativeAssetOut": "_dfareporting_139_CreativeAssetOut",
        "AdsListResponseIn": "_dfareporting_140_AdsListResponseIn",
        "AdsListResponseOut": "_dfareporting_141_AdsListResponseOut",
        "CitiesListResponseIn": "_dfareporting_142_CitiesListResponseIn",
        "CitiesListResponseOut": "_dfareporting_143_CitiesListResponseOut",
        "UserRolePermissionsListResponseIn": "_dfareporting_144_UserRolePermissionsListResponseIn",
        "UserRolePermissionsListResponseOut": "_dfareporting_145_UserRolePermissionsListResponseOut",
        "FrequencyCapIn": "_dfareporting_146_FrequencyCapIn",
        "FrequencyCapOut": "_dfareporting_147_FrequencyCapOut",
        "EventFilterIn": "_dfareporting_148_EventFilterIn",
        "EventFilterOut": "_dfareporting_149_EventFilterOut",
        "BillingRatesListResponseIn": "_dfareporting_150_BillingRatesListResponseIn",
        "BillingRatesListResponseOut": "_dfareporting_151_BillingRatesListResponseOut",
        "ConversionsBatchInsertRequestIn": "_dfareporting_152_ConversionsBatchInsertRequestIn",
        "ConversionsBatchInsertRequestOut": "_dfareporting_153_ConversionsBatchInsertRequestOut",
        "ChangeLogIn": "_dfareporting_154_ChangeLogIn",
        "ChangeLogOut": "_dfareporting_155_ChangeLogOut",
        "CreativeGroupsListResponseIn": "_dfareporting_156_CreativeGroupsListResponseIn",
        "CreativeGroupsListResponseOut": "_dfareporting_157_CreativeGroupsListResponseOut",
        "RemarketingListShareIn": "_dfareporting_158_RemarketingListShareIn",
        "RemarketingListShareOut": "_dfareporting_159_RemarketingListShareOut",
        "SiteIn": "_dfareporting_160_SiteIn",
        "SiteOut": "_dfareporting_161_SiteOut",
        "AdvertiserLandingPagesListResponseIn": "_dfareporting_162_AdvertiserLandingPagesListResponseIn",
        "AdvertiserLandingPagesListResponseOut": "_dfareporting_163_AdvertiserLandingPagesListResponseOut",
        "SiteCompanionSettingIn": "_dfareporting_164_SiteCompanionSettingIn",
        "SiteCompanionSettingOut": "_dfareporting_165_SiteCompanionSettingOut",
        "GeoTargetingIn": "_dfareporting_166_GeoTargetingIn",
        "GeoTargetingOut": "_dfareporting_167_GeoTargetingOut",
        "CountryIn": "_dfareporting_168_CountryIn",
        "CountryOut": "_dfareporting_169_CountryOut",
        "AdvertiserGroupsListResponseIn": "_dfareporting_170_AdvertiserGroupsListResponseIn",
        "AdvertiserGroupsListResponseOut": "_dfareporting_171_AdvertiserGroupsListResponseOut",
        "AccountActiveAdSummaryIn": "_dfareporting_172_AccountActiveAdSummaryIn",
        "AccountActiveAdSummaryOut": "_dfareporting_173_AccountActiveAdSummaryOut",
        "RegionIn": "_dfareporting_174_RegionIn",
        "RegionOut": "_dfareporting_175_RegionOut",
        "CreativeFieldIn": "_dfareporting_176_CreativeFieldIn",
        "CreativeFieldOut": "_dfareporting_177_CreativeFieldOut",
        "DirectorySitesListResponseIn": "_dfareporting_178_DirectorySitesListResponseIn",
        "DirectorySitesListResponseOut": "_dfareporting_179_DirectorySitesListResponseOut",
        "SubaccountsListResponseIn": "_dfareporting_180_SubaccountsListResponseIn",
        "SubaccountsListResponseOut": "_dfareporting_181_SubaccountsListResponseOut",
        "AdBlockingConfigurationIn": "_dfareporting_182_AdBlockingConfigurationIn",
        "AdBlockingConfigurationOut": "_dfareporting_183_AdBlockingConfigurationOut",
        "CampaignSummaryIn": "_dfareporting_184_CampaignSummaryIn",
        "CampaignSummaryOut": "_dfareporting_185_CampaignSummaryOut",
        "ChannelGroupingRuleIn": "_dfareporting_186_ChannelGroupingRuleIn",
        "ChannelGroupingRuleOut": "_dfareporting_187_ChannelGroupingRuleOut",
        "CampaignCreativeAssociationsListResponseIn": "_dfareporting_188_CampaignCreativeAssociationsListResponseIn",
        "CampaignCreativeAssociationsListResponseOut": "_dfareporting_189_CampaignCreativeAssociationsListResponseOut",
        "PlacementsListResponseIn": "_dfareporting_190_PlacementsListResponseIn",
        "PlacementsListResponseOut": "_dfareporting_191_PlacementsListResponseOut",
        "ObjectFilterIn": "_dfareporting_192_ObjectFilterIn",
        "ObjectFilterOut": "_dfareporting_193_ObjectFilterOut",
        "ReachReportCompatibleFieldsIn": "_dfareporting_194_ReachReportCompatibleFieldsIn",
        "ReachReportCompatibleFieldsOut": "_dfareporting_195_ReachReportCompatibleFieldsOut",
        "AccountPermissionIn": "_dfareporting_196_AccountPermissionIn",
        "AccountPermissionOut": "_dfareporting_197_AccountPermissionOut",
        "TargetingTemplatesListResponseIn": "_dfareporting_198_TargetingTemplatesListResponseIn",
        "TargetingTemplatesListResponseOut": "_dfareporting_199_TargetingTemplatesListResponseOut",
        "PathReportDimensionValueIn": "_dfareporting_200_PathReportDimensionValueIn",
        "PathReportDimensionValueOut": "_dfareporting_201_PathReportDimensionValueOut",
        "CreativeAssetSelectionIn": "_dfareporting_202_CreativeAssetSelectionIn",
        "CreativeAssetSelectionOut": "_dfareporting_203_CreativeAssetSelectionOut",
        "SizesListResponseIn": "_dfareporting_204_SizesListResponseIn",
        "SizesListResponseOut": "_dfareporting_205_SizesListResponseOut",
        "ConversionsBatchUpdateResponseIn": "_dfareporting_206_ConversionsBatchUpdateResponseIn",
        "ConversionsBatchUpdateResponseOut": "_dfareporting_207_ConversionsBatchUpdateResponseOut",
        "UniversalAdIdIn": "_dfareporting_208_UniversalAdIdIn",
        "UniversalAdIdOut": "_dfareporting_209_UniversalAdIdOut",
        "CreativeAssetIdIn": "_dfareporting_210_CreativeAssetIdIn",
        "CreativeAssetIdOut": "_dfareporting_211_CreativeAssetIdOut",
        "UserRolesListResponseIn": "_dfareporting_212_UserRolesListResponseIn",
        "UserRolesListResponseOut": "_dfareporting_213_UserRolesListResponseOut",
        "AccountsListResponseIn": "_dfareporting_214_AccountsListResponseIn",
        "AccountsListResponseOut": "_dfareporting_215_AccountsListResponseOut",
        "SiteContactIn": "_dfareporting_216_SiteContactIn",
        "SiteContactOut": "_dfareporting_217_SiteContactOut",
        "EncryptionInfoIn": "_dfareporting_218_EncryptionInfoIn",
        "EncryptionInfoOut": "_dfareporting_219_EncryptionInfoOut",
        "OrderDocumentIn": "_dfareporting_220_OrderDocumentIn",
        "OrderDocumentOut": "_dfareporting_221_OrderDocumentOut",
        "ChannelGroupingIn": "_dfareporting_222_ChannelGroupingIn",
        "ChannelGroupingOut": "_dfareporting_223_ChannelGroupingOut",
        "VideoFormatIn": "_dfareporting_224_VideoFormatIn",
        "VideoFormatOut": "_dfareporting_225_VideoFormatOut",
        "CreativeFieldAssignmentIn": "_dfareporting_226_CreativeFieldAssignmentIn",
        "CreativeFieldAssignmentOut": "_dfareporting_227_CreativeFieldAssignmentOut",
        "ThirdPartyTrackingUrlIn": "_dfareporting_228_ThirdPartyTrackingUrlIn",
        "ThirdPartyTrackingUrlOut": "_dfareporting_229_ThirdPartyTrackingUrlOut",
        "ClickThroughUrlSuffixPropertiesIn": "_dfareporting_230_ClickThroughUrlSuffixPropertiesIn",
        "ClickThroughUrlSuffixPropertiesOut": "_dfareporting_231_ClickThroughUrlSuffixPropertiesOut",
        "AdSlotIn": "_dfareporting_232_AdSlotIn",
        "AdSlotOut": "_dfareporting_233_AdSlotOut",
        "OperatingSystemVersionsListResponseIn": "_dfareporting_234_OperatingSystemVersionsListResponseIn",
        "OperatingSystemVersionsListResponseOut": "_dfareporting_235_OperatingSystemVersionsListResponseOut",
        "ListPopulationClauseIn": "_dfareporting_236_ListPopulationClauseIn",
        "ListPopulationClauseOut": "_dfareporting_237_ListPopulationClauseOut",
        "FloodlightActivityPublisherDynamicTagIn": "_dfareporting_238_FloodlightActivityPublisherDynamicTagIn",
        "FloodlightActivityPublisherDynamicTagOut": "_dfareporting_239_FloodlightActivityPublisherDynamicTagOut",
        "RichMediaExitOverrideIn": "_dfareporting_240_RichMediaExitOverrideIn",
        "RichMediaExitOverrideOut": "_dfareporting_241_RichMediaExitOverrideOut",
        "SortedDimensionIn": "_dfareporting_242_SortedDimensionIn",
        "SortedDimensionOut": "_dfareporting_243_SortedDimensionOut",
        "MetroIn": "_dfareporting_244_MetroIn",
        "MetroOut": "_dfareporting_245_MetroOut",
        "CreativeFieldValueIn": "_dfareporting_246_CreativeFieldValueIn",
        "CreativeFieldValueOut": "_dfareporting_247_CreativeFieldValueOut",
        "PricingIn": "_dfareporting_248_PricingIn",
        "PricingOut": "_dfareporting_249_PricingOut",
        "TagDataIn": "_dfareporting_250_TagDataIn",
        "TagDataOut": "_dfareporting_251_TagDataOut",
        "DeliveryScheduleIn": "_dfareporting_252_DeliveryScheduleIn",
        "DeliveryScheduleOut": "_dfareporting_253_DeliveryScheduleOut",
        "CampaignsListResponseIn": "_dfareporting_254_CampaignsListResponseIn",
        "CampaignsListResponseOut": "_dfareporting_255_CampaignsListResponseOut",
        "CampaignIn": "_dfareporting_256_CampaignIn",
        "CampaignOut": "_dfareporting_257_CampaignOut",
        "FloodlightReportCompatibleFieldsIn": "_dfareporting_258_FloodlightReportCompatibleFieldsIn",
        "FloodlightReportCompatibleFieldsOut": "_dfareporting_259_FloodlightReportCompatibleFieldsOut",
        "PlacementStrategiesListResponseIn": "_dfareporting_260_PlacementStrategiesListResponseIn",
        "PlacementStrategiesListResponseOut": "_dfareporting_261_PlacementStrategiesListResponseOut",
        "CreativeOptimizationConfigurationIn": "_dfareporting_262_CreativeOptimizationConfigurationIn",
        "CreativeOptimizationConfigurationOut": "_dfareporting_263_CreativeOptimizationConfigurationOut",
        "EventTagIn": "_dfareporting_264_EventTagIn",
        "EventTagOut": "_dfareporting_265_EventTagOut",
        "OperatingSystemIn": "_dfareporting_266_OperatingSystemIn",
        "OperatingSystemOut": "_dfareporting_267_OperatingSystemOut",
        "PlatformTypesListResponseIn": "_dfareporting_268_PlatformTypesListResponseIn",
        "PlatformTypesListResponseOut": "_dfareporting_269_PlatformTypesListResponseOut",
        "CustomViewabilityMetricIn": "_dfareporting_270_CustomViewabilityMetricIn",
        "CustomViewabilityMetricOut": "_dfareporting_271_CustomViewabilityMetricOut",
        "PricingSchedulePricingPeriodIn": "_dfareporting_272_PricingSchedulePricingPeriodIn",
        "PricingSchedulePricingPeriodOut": "_dfareporting_273_PricingSchedulePricingPeriodOut",
        "InventoryItemIn": "_dfareporting_274_InventoryItemIn",
        "InventoryItemOut": "_dfareporting_275_InventoryItemOut",
        "AdvertiserGroupIn": "_dfareporting_276_AdvertiserGroupIn",
        "AdvertiserGroupOut": "_dfareporting_277_AdvertiserGroupOut",
        "ReportListIn": "_dfareporting_278_ReportListIn",
        "ReportListOut": "_dfareporting_279_ReportListOut",
        "SubaccountIn": "_dfareporting_280_SubaccountIn",
        "SubaccountOut": "_dfareporting_281_SubaccountOut",
        "SiteTranscodeSettingIn": "_dfareporting_282_SiteTranscodeSettingIn",
        "SiteTranscodeSettingOut": "_dfareporting_283_SiteTranscodeSettingOut",
        "CreativeIn": "_dfareporting_284_CreativeIn",
        "CreativeOut": "_dfareporting_285_CreativeOut",
        "ConnectionTypeIn": "_dfareporting_286_ConnectionTypeIn",
        "ConnectionTypeOut": "_dfareporting_287_ConnectionTypeOut",
        "BillingRateIn": "_dfareporting_288_BillingRateIn",
        "BillingRateOut": "_dfareporting_289_BillingRateOut",
        "AdIn": "_dfareporting_290_AdIn",
        "AdOut": "_dfareporting_291_AdOut",
        "ThirdPartyAuthenticationTokenIn": "_dfareporting_292_ThirdPartyAuthenticationTokenIn",
        "ThirdPartyAuthenticationTokenOut": "_dfareporting_293_ThirdPartyAuthenticationTokenOut",
        "CreativeRotationIn": "_dfareporting_294_CreativeRotationIn",
        "CreativeRotationOut": "_dfareporting_295_CreativeRotationOut",
        "DynamicTargetingKeysListResponseIn": "_dfareporting_296_DynamicTargetingKeysListResponseIn",
        "DynamicTargetingKeysListResponseOut": "_dfareporting_297_DynamicTargetingKeysListResponseOut",
        "ObaIconIn": "_dfareporting_298_ObaIconIn",
        "ObaIconOut": "_dfareporting_299_ObaIconOut",
        "PlacementGroupsListResponseIn": "_dfareporting_300_PlacementGroupsListResponseIn",
        "PlacementGroupsListResponseOut": "_dfareporting_301_PlacementGroupsListResponseOut",
        "FileIn": "_dfareporting_302_FileIn",
        "FileOut": "_dfareporting_303_FileOut",
        "MobileAppIn": "_dfareporting_304_MobileAppIn",
        "MobileAppOut": "_dfareporting_305_MobileAppOut",
        "LastModifiedInfoIn": "_dfareporting_306_LastModifiedInfoIn",
        "LastModifiedInfoOut": "_dfareporting_307_LastModifiedInfoOut",
        "BrowsersListResponseIn": "_dfareporting_308_BrowsersListResponseIn",
        "BrowsersListResponseOut": "_dfareporting_309_BrowsersListResponseOut",
        "ClickTagIn": "_dfareporting_310_ClickTagIn",
        "ClickTagOut": "_dfareporting_311_ClickTagOut",
        "CreativeFieldValuesListResponseIn": "_dfareporting_312_CreativeFieldValuesListResponseIn",
        "CreativeFieldValuesListResponseOut": "_dfareporting_313_CreativeFieldValuesListResponseOut",
        "ListTargetingExpressionIn": "_dfareporting_314_ListTargetingExpressionIn",
        "ListTargetingExpressionOut": "_dfareporting_315_ListTargetingExpressionOut",
        "DimensionValueIn": "_dfareporting_316_DimensionValueIn",
        "DimensionValueOut": "_dfareporting_317_DimensionValueOut",
        "DisjunctiveMatchStatementIn": "_dfareporting_318_DisjunctiveMatchStatementIn",
        "DisjunctiveMatchStatementOut": "_dfareporting_319_DisjunctiveMatchStatementOut",
        "CustomFloodlightVariableIn": "_dfareporting_320_CustomFloodlightVariableIn",
        "CustomFloodlightVariableOut": "_dfareporting_321_CustomFloodlightVariableOut",
        "InvoiceIn": "_dfareporting_322_InvoiceIn",
        "InvoiceOut": "_dfareporting_323_InvoiceOut",
        "PlacementsGenerateTagsResponseIn": "_dfareporting_324_PlacementsGenerateTagsResponseIn",
        "PlacementsGenerateTagsResponseOut": "_dfareporting_325_PlacementsGenerateTagsResponseOut",
        "BillingAssignmentIn": "_dfareporting_326_BillingAssignmentIn",
        "BillingAssignmentOut": "_dfareporting_327_BillingAssignmentOut",
        "ConversionErrorIn": "_dfareporting_328_ConversionErrorIn",
        "ConversionErrorOut": "_dfareporting_329_ConversionErrorOut",
        "RecipientIn": "_dfareporting_330_RecipientIn",
        "RecipientOut": "_dfareporting_331_RecipientOut",
        "OmnitureSettingsIn": "_dfareporting_332_OmnitureSettingsIn",
        "OmnitureSettingsOut": "_dfareporting_333_OmnitureSettingsOut",
        "LanguageIn": "_dfareporting_334_LanguageIn",
        "LanguageOut": "_dfareporting_335_LanguageOut",
        "ListPopulationTermIn": "_dfareporting_336_ListPopulationTermIn",
        "ListPopulationTermOut": "_dfareporting_337_ListPopulationTermOut",
        "BrowserIn": "_dfareporting_338_BrowserIn",
        "BrowserOut": "_dfareporting_339_BrowserOut",
        "MeasurementPartnerWrappingDataIn": "_dfareporting_340_MeasurementPartnerWrappingDataIn",
        "MeasurementPartnerWrappingDataOut": "_dfareporting_341_MeasurementPartnerWrappingDataOut",
        "RuleIn": "_dfareporting_342_RuleIn",
        "RuleOut": "_dfareporting_343_RuleOut",
        "FloodlightConfigurationIn": "_dfareporting_344_FloodlightConfigurationIn",
        "FloodlightConfigurationOut": "_dfareporting_345_FloodlightConfigurationOut",
        "SiteSkippableSettingIn": "_dfareporting_346_SiteSkippableSettingIn",
        "SiteSkippableSettingOut": "_dfareporting_347_SiteSkippableSettingOut",
        "CompatibleFieldsIn": "_dfareporting_348_CompatibleFieldsIn",
        "CompatibleFieldsOut": "_dfareporting_349_CompatibleFieldsOut",
        "OperatingSystemVersionIn": "_dfareporting_350_OperatingSystemVersionIn",
        "OperatingSystemVersionOut": "_dfareporting_351_OperatingSystemVersionOut",
        "CreativeAssetMetadataIn": "_dfareporting_352_CreativeAssetMetadataIn",
        "CreativeAssetMetadataOut": "_dfareporting_353_CreativeAssetMetadataOut",
        "ChangeLogsListResponseIn": "_dfareporting_354_ChangeLogsListResponseIn",
        "ChangeLogsListResponseOut": "_dfareporting_355_ChangeLogsListResponseOut",
        "OfflineUserAddressInfoIn": "_dfareporting_356_OfflineUserAddressInfoIn",
        "OfflineUserAddressInfoOut": "_dfareporting_357_OfflineUserAddressInfoOut",
        "PlacementTagIn": "_dfareporting_358_PlacementTagIn",
        "PlacementTagOut": "_dfareporting_359_PlacementTagOut",
        "AccountUserProfileIn": "_dfareporting_360_AccountUserProfileIn",
        "AccountUserProfileOut": "_dfareporting_361_AccountUserProfileOut",
        "UserIdentifierIn": "_dfareporting_362_UserIdentifierIn",
        "UserIdentifierOut": "_dfareporting_363_UserIdentifierOut",
        "VideoSettingsIn": "_dfareporting_364_VideoSettingsIn",
        "VideoSettingsOut": "_dfareporting_365_VideoSettingsOut",
        "CompanionClickThroughOverrideIn": "_dfareporting_366_CompanionClickThroughOverrideIn",
        "CompanionClickThroughOverrideOut": "_dfareporting_367_CompanionClickThroughOverrideOut",
        "MetricIn": "_dfareporting_368_MetricIn",
        "MetricOut": "_dfareporting_369_MetricOut",
        "AdvertisersListResponseIn": "_dfareporting_370_AdvertisersListResponseIn",
        "AdvertisersListResponseOut": "_dfareporting_371_AdvertisersListResponseOut",
        "KeyValueTargetingExpressionIn": "_dfareporting_372_KeyValueTargetingExpressionIn",
        "KeyValueTargetingExpressionOut": "_dfareporting_373_KeyValueTargetingExpressionOut",
        "UserRolePermissionGroupsListResponseIn": "_dfareporting_374_UserRolePermissionGroupsListResponseIn",
        "UserRolePermissionGroupsListResponseOut": "_dfareporting_375_UserRolePermissionGroupsListResponseOut",
        "TechnologyTargetingIn": "_dfareporting_376_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_dfareporting_377_TechnologyTargetingOut",
        "ConversionsBatchUpdateRequestIn": "_dfareporting_378_ConversionsBatchUpdateRequestIn",
        "ConversionsBatchUpdateRequestOut": "_dfareporting_379_ConversionsBatchUpdateRequestOut",
        "OperatingSystemsListResponseIn": "_dfareporting_380_OperatingSystemsListResponseIn",
        "OperatingSystemsListResponseOut": "_dfareporting_381_OperatingSystemsListResponseOut",
        "FloodlightActivityIn": "_dfareporting_382_FloodlightActivityIn",
        "FloodlightActivityOut": "_dfareporting_383_FloodlightActivityOut",
        "ReportIn": "_dfareporting_384_ReportIn",
        "ReportOut": "_dfareporting_385_ReportOut",
        "EventTagsListResponseIn": "_dfareporting_386_EventTagsListResponseIn",
        "EventTagsListResponseOut": "_dfareporting_387_EventTagsListResponseOut",
        "PricingScheduleIn": "_dfareporting_388_PricingScheduleIn",
        "PricingScheduleOut": "_dfareporting_389_PricingScheduleOut",
        "MobileCarrierIn": "_dfareporting_390_MobileCarrierIn",
        "MobileCarrierOut": "_dfareporting_391_MobileCarrierOut",
        "InventoryItemsListResponseIn": "_dfareporting_392_InventoryItemsListResponseIn",
        "InventoryItemsListResponseOut": "_dfareporting_393_InventoryItemsListResponseOut",
        "OptimizationActivityIn": "_dfareporting_394_OptimizationActivityIn",
        "OptimizationActivityOut": "_dfareporting_395_OptimizationActivityOut",
        "SiteSettingsIn": "_dfareporting_396_SiteSettingsIn",
        "SiteSettingsOut": "_dfareporting_397_SiteSettingsOut",
        "TargetableRemarketingListIn": "_dfareporting_398_TargetableRemarketingListIn",
        "TargetableRemarketingListOut": "_dfareporting_399_TargetableRemarketingListOut",
        "PlacementStrategyIn": "_dfareporting_400_PlacementStrategyIn",
        "PlacementStrategyOut": "_dfareporting_401_PlacementStrategyOut",
        "ProjectIn": "_dfareporting_402_ProjectIn",
        "ProjectOut": "_dfareporting_403_ProjectOut",
        "ContentCategoryIn": "_dfareporting_404_ContentCategoryIn",
        "ContentCategoryOut": "_dfareporting_405_ContentCategoryOut",
        "OrderIn": "_dfareporting_406_OrderIn",
        "OrderOut": "_dfareporting_407_OrderOut",
        "CreativeClickThroughUrlIn": "_dfareporting_408_CreativeClickThroughUrlIn",
        "CreativeClickThroughUrlOut": "_dfareporting_409_CreativeClickThroughUrlOut",
        "BillingAssignmentsListResponseIn": "_dfareporting_410_BillingAssignmentsListResponseIn",
        "BillingAssignmentsListResponseOut": "_dfareporting_411_BillingAssignmentsListResponseOut",
        "TargetingTemplateIn": "_dfareporting_412_TargetingTemplateIn",
        "TargetingTemplateOut": "_dfareporting_413_TargetingTemplateOut",
        "MeasurementPartnerCampaignLinkIn": "_dfareporting_414_MeasurementPartnerCampaignLinkIn",
        "MeasurementPartnerCampaignLinkOut": "_dfareporting_415_MeasurementPartnerCampaignLinkOut",
        "FileListIn": "_dfareporting_416_FileListIn",
        "FileListOut": "_dfareporting_417_FileListOut",
        "FloodlightActivityGroupIn": "_dfareporting_418_FloodlightActivityGroupIn",
        "FloodlightActivityGroupOut": "_dfareporting_419_FloodlightActivityGroupOut",
        "TargetWindowIn": "_dfareporting_420_TargetWindowIn",
        "TargetWindowOut": "_dfareporting_421_TargetWindowOut",
        "LanguagesListResponseIn": "_dfareporting_422_LanguagesListResponseIn",
        "LanguagesListResponseOut": "_dfareporting_423_LanguagesListResponseOut",
        "LookbackConfigurationIn": "_dfareporting_424_LookbackConfigurationIn",
        "LookbackConfigurationOut": "_dfareporting_425_LookbackConfigurationOut",
        "PlacementGroupIn": "_dfareporting_426_PlacementGroupIn",
        "PlacementGroupOut": "_dfareporting_427_PlacementGroupOut",
        "ContentCategoriesListResponseIn": "_dfareporting_428_ContentCategoriesListResponseIn",
        "ContentCategoriesListResponseOut": "_dfareporting_429_ContentCategoriesListResponseOut",
        "DimensionValueRequestIn": "_dfareporting_430_DimensionValueRequestIn",
        "DimensionValueRequestOut": "_dfareporting_431_DimensionValueRequestOut",
        "CrossDimensionReachReportCompatibleFieldsIn": "_dfareporting_432_CrossDimensionReachReportCompatibleFieldsIn",
        "CrossDimensionReachReportCompatibleFieldsOut": "_dfareporting_433_CrossDimensionReachReportCompatibleFieldsOut",
        "FloodlightActivityGroupsListResponseIn": "_dfareporting_434_FloodlightActivityGroupsListResponseIn",
        "FloodlightActivityGroupsListResponseOut": "_dfareporting_435_FloodlightActivityGroupsListResponseOut",
        "SizeIn": "_dfareporting_436_SizeIn",
        "SizeOut": "_dfareporting_437_SizeOut",
        "LanguageTargetingIn": "_dfareporting_438_LanguageTargetingIn",
        "LanguageTargetingOut": "_dfareporting_439_LanguageTargetingOut",
        "AccountPermissionsListResponseIn": "_dfareporting_440_AccountPermissionsListResponseIn",
        "AccountPermissionsListResponseOut": "_dfareporting_441_AccountPermissionsListResponseOut",
        "DeepLinkIn": "_dfareporting_442_DeepLinkIn",
        "DeepLinkOut": "_dfareporting_443_DeepLinkOut",
        "AudienceSegmentIn": "_dfareporting_444_AudienceSegmentIn",
        "AudienceSegmentOut": "_dfareporting_445_AudienceSegmentOut",
        "VideoFormatsListResponseIn": "_dfareporting_446_VideoFormatsListResponseIn",
        "VideoFormatsListResponseOut": "_dfareporting_447_VideoFormatsListResponseOut",
        "DimensionFilterIn": "_dfareporting_448_DimensionFilterIn",
        "DimensionFilterOut": "_dfareporting_449_DimensionFilterOut",
        "FloodlightActivitiesGenerateTagResponseIn": "_dfareporting_450_FloodlightActivitiesGenerateTagResponseIn",
        "FloodlightActivitiesGenerateTagResponseOut": "_dfareporting_451_FloodlightActivitiesGenerateTagResponseOut",
        "DfpSettingsIn": "_dfareporting_452_DfpSettingsIn",
        "DfpSettingsOut": "_dfareporting_453_DfpSettingsOut",
        "RemarketingListIn": "_dfareporting_454_RemarketingListIn",
        "RemarketingListOut": "_dfareporting_455_RemarketingListOut",
        "AccountUserProfilesListResponseIn": "_dfareporting_456_AccountUserProfilesListResponseIn",
        "AccountUserProfilesListResponseOut": "_dfareporting_457_AccountUserProfilesListResponseOut",
        "ClickThroughUrlIn": "_dfareporting_458_ClickThroughUrlIn",
        "ClickThroughUrlOut": "_dfareporting_459_ClickThroughUrlOut",
        "FlightIn": "_dfareporting_460_FlightIn",
        "FlightOut": "_dfareporting_461_FlightOut",
        "BillingProfilesListResponseIn": "_dfareporting_462_BillingProfilesListResponseIn",
        "BillingProfilesListResponseOut": "_dfareporting_463_BillingProfilesListResponseOut",
        "FloodlightActivitiesListResponseIn": "_dfareporting_464_FloodlightActivitiesListResponseIn",
        "FloodlightActivitiesListResponseOut": "_dfareporting_465_FloodlightActivitiesListResponseOut",
        "ListPopulationRuleIn": "_dfareporting_466_ListPopulationRuleIn",
        "ListPopulationRuleOut": "_dfareporting_467_ListPopulationRuleOut",
        "DirectorySiteSettingsIn": "_dfareporting_468_DirectorySiteSettingsIn",
        "DirectorySiteSettingsOut": "_dfareporting_469_DirectorySiteSettingsOut",
        "CustomViewabilityMetricConfigurationIn": "_dfareporting_470_CustomViewabilityMetricConfigurationIn",
        "CustomViewabilityMetricConfigurationOut": "_dfareporting_471_CustomViewabilityMetricConfigurationOut",
        "ConversionStatusIn": "_dfareporting_472_ConversionStatusIn",
        "ConversionStatusOut": "_dfareporting_473_ConversionStatusOut",
        "TagSettingsIn": "_dfareporting_474_TagSettingsIn",
        "TagSettingsOut": "_dfareporting_475_TagSettingsOut",
        "FsCommandIn": "_dfareporting_476_FsCommandIn",
        "FsCommandOut": "_dfareporting_477_FsCommandOut",
        "PathFilterIn": "_dfareporting_478_PathFilterIn",
        "PathFilterOut": "_dfareporting_479_PathFilterOut",
        "DynamicTargetingKeyIn": "_dfareporting_480_DynamicTargetingKeyIn",
        "DynamicTargetingKeyOut": "_dfareporting_481_DynamicTargetingKeyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AccountIn"] = t.struct(
        {
            "name": t.string().optional(),
            "nielsenOcrEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "defaultCreativeSizeId": t.string().optional(),
            "shareReportsWithTwitter": t.boolean().optional(),
            "availablePermissionIds": t.array(t.string()).optional(),
            "currencyId": t.string().optional(),
            "activeViewOptOut": t.boolean().optional(),
            "accountPermissionIds": t.array(t.string()).optional(),
            "maximumImageSize": t.string().optional(),
            "id": t.string().optional(),
            "locale": t.string().optional(),
            "accountProfile": t.string().optional(),
            "description": t.string().optional(),
            "reportsConfiguration": t.proxy(
                renames["ReportsConfigurationIn"]
            ).optional(),
            "activeAdsLimitTier": t.string().optional(),
            "active": t.boolean().optional(),
            "teaserSizeLimit": t.string().optional(),
            "countryId": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "nielsenOcrEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "defaultCreativeSizeId": t.string().optional(),
            "shareReportsWithTwitter": t.boolean().optional(),
            "availablePermissionIds": t.array(t.string()).optional(),
            "currencyId": t.string().optional(),
            "activeViewOptOut": t.boolean().optional(),
            "accountPermissionIds": t.array(t.string()).optional(),
            "maximumImageSize": t.string().optional(),
            "id": t.string().optional(),
            "locale": t.string().optional(),
            "accountProfile": t.string().optional(),
            "description": t.string().optional(),
            "reportsConfiguration": t.proxy(
                renames["ReportsConfigurationOut"]
            ).optional(),
            "activeAdsLimitTier": t.string().optional(),
            "active": t.boolean().optional(),
            "teaserSizeLimit": t.string().optional(),
            "countryId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["MobileAppsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "mobileApps": t.array(t.proxy(renames["MobileAppIn"])).optional(),
        }
    ).named(renames["MobileAppsListResponseIn"])
    types["MobileAppsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "mobileApps": t.array(t.proxy(renames["MobileAppOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileAppsListResponseOut"])
    types["UvarFilterIn"] = t.struct(
        {
            "index": t.string().optional(),
            "complement": t.boolean().optional(),
            "values": t.array(t.string()).optional(),
            "match": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UvarFilterIn"])
    types["UvarFilterOut"] = t.struct(
        {
            "index": t.string().optional(),
            "complement": t.boolean().optional(),
            "values": t.array(t.string()).optional(),
            "match": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UvarFilterOut"])
    types["OrdersListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "orders": t.array(t.proxy(renames["OrderIn"])).optional(),
        }
    ).named(renames["OrdersListResponseIn"])
    types["OrdersListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "orders": t.array(t.proxy(renames["OrderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersListResponseOut"])
    types["RegionsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "regions": t.array(t.proxy(renames["RegionIn"])).optional(),
        }
    ).named(renames["RegionsListResponseIn"])
    types["RegionsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "regions": t.array(t.proxy(renames["RegionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionsListResponseOut"])
    types["MeasurementPartnerAdvertiserLinkIn"] = t.struct(
        {
            "linkStatus": t.string().optional(),
            "partnerAdvertiserId": t.string().optional(),
            "measurementPartner": t.string().optional(),
        }
    ).named(renames["MeasurementPartnerAdvertiserLinkIn"])
    types["MeasurementPartnerAdvertiserLinkOut"] = t.struct(
        {
            "linkStatus": t.string().optional(),
            "partnerAdvertiserId": t.string().optional(),
            "measurementPartner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeasurementPartnerAdvertiserLinkOut"])
    types["UserRolePermissionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "availability": t.string().optional(),
            "permissionGroupId": t.string().optional(),
        }
    ).named(renames["UserRolePermissionIn"])
    types["UserRolePermissionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "availability": t.string().optional(),
            "permissionGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRolePermissionOut"])
    types["PostalCodesListResponseIn"] = t.struct(
        {
            "postalCodes": t.array(t.proxy(renames["PostalCodeIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PostalCodesListResponseIn"])
    types["PostalCodesListResponseOut"] = t.struct(
        {
            "postalCodes": t.array(t.proxy(renames["PostalCodeOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalCodesListResponseOut"])
    types["TargetableRemarketingListsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targetableRemarketingLists": t.array(
                t.proxy(renames["TargetableRemarketingListIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["TargetableRemarketingListsListResponseIn"])
    types["TargetableRemarketingListsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targetableRemarketingLists": t.array(
                t.proxy(renames["TargetableRemarketingListOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetableRemarketingListsListResponseOut"])
    types["DateRangeIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "startDate": t.string(),
            "endDate": t.string(),
            "relativeDateRange": t.string().optional(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "startDate": t.string(),
            "endDate": t.string(),
            "relativeDateRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
    types["AccountPermissionGroupsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountPermissionGroups": t.array(
                t.proxy(renames["AccountPermissionGroupIn"])
            ).optional(),
        }
    ).named(renames["AccountPermissionGroupsListResponseIn"])
    types["AccountPermissionGroupsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountPermissionGroups": t.array(
                t.proxy(renames["AccountPermissionGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountPermissionGroupsListResponseOut"])
    types["PathReportCompatibleFieldsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "pathFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "channelGroupings": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["PathReportCompatibleFieldsIn"])
    types["PathReportCompatibleFieldsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "pathFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "channelGroupings": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathReportCompatibleFieldsOut"])
    types["VideoOffsetIn"] = t.struct(
        {
            "offsetPercentage": t.integer().optional(),
            "offsetSeconds": t.integer().optional(),
        }
    ).named(renames["VideoOffsetIn"])
    types["VideoOffsetOut"] = t.struct(
        {
            "offsetPercentage": t.integer().optional(),
            "offsetSeconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOffsetOut"])
    types["CampaignCreativeAssociationIn"] = t.struct(
        {"creativeId": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["CampaignCreativeAssociationIn"])
    types["CampaignCreativeAssociationOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignCreativeAssociationOut"])
    types["EventTagOverrideIn"] = t.struct(
        {"enabled": t.boolean().optional(), "id": t.string().optional()}
    ).named(renames["EventTagOverrideIn"])
    types["EventTagOverrideOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTagOverrideOut"])
    types["OrderContactIn"] = t.struct(
        {
            "contactTitle": t.string().optional(),
            "contactInfo": t.string().optional(),
            "contactName": t.string().optional(),
            "signatureUserProfileId": t.string().optional(),
            "contactType": t.string().optional(),
        }
    ).named(renames["OrderContactIn"])
    types["OrderContactOut"] = t.struct(
        {
            "contactTitle": t.string().optional(),
            "contactInfo": t.string().optional(),
            "contactName": t.string().optional(),
            "signatureUserProfileId": t.string().optional(),
            "contactType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderContactOut"])
    types["SkippableSettingIn"] = t.struct(
        {
            "progressOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
            "kind": t.string().optional(),
            "skippable": t.boolean().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
        }
    ).named(renames["SkippableSettingIn"])
    types["SkippableSettingOut"] = t.struct(
        {
            "progressOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "kind": t.string().optional(),
            "skippable": t.boolean().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkippableSettingOut"])
    types["ConversionIn"] = t.struct(
        {
            "floodlightConfigurationId": t.string().optional(),
            "timestampMicros": t.string().optional(),
            "treatmentForUnderage": t.boolean().optional(),
            "impressionId": t.string().optional(),
            "userIdentifiers": t.array(t.proxy(renames["UserIdentifierIn"])).optional(),
            "encryptedUserId": t.string().optional(),
            "matchId": t.string().optional(),
            "floodlightActivityId": t.string().optional(),
            "customVariables": t.array(
                t.proxy(renames["CustomFloodlightVariableIn"])
            ).optional(),
            "mobileDeviceId": t.string().optional(),
            "value": t.number().optional(),
            "gclid": t.string().optional(),
            "childDirectedTreatment": t.boolean().optional(),
            "nonPersonalizedAd": t.boolean().optional(),
            "dclid": t.string().optional(),
            "kind": t.string().optional(),
            "encryptedUserIdCandidates": t.array(t.string()).optional(),
            "limitAdTracking": t.boolean().optional(),
            "quantity": t.string().optional(),
            "ordinal": t.string().optional(),
        }
    ).named(renames["ConversionIn"])
    types["ConversionOut"] = t.struct(
        {
            "floodlightConfigurationId": t.string().optional(),
            "timestampMicros": t.string().optional(),
            "treatmentForUnderage": t.boolean().optional(),
            "impressionId": t.string().optional(),
            "userIdentifiers": t.array(
                t.proxy(renames["UserIdentifierOut"])
            ).optional(),
            "encryptedUserId": t.string().optional(),
            "matchId": t.string().optional(),
            "floodlightActivityId": t.string().optional(),
            "customVariables": t.array(
                t.proxy(renames["CustomFloodlightVariableOut"])
            ).optional(),
            "mobileDeviceId": t.string().optional(),
            "value": t.number().optional(),
            "gclid": t.string().optional(),
            "childDirectedTreatment": t.boolean().optional(),
            "nonPersonalizedAd": t.boolean().optional(),
            "dclid": t.string().optional(),
            "kind": t.string().optional(),
            "encryptedUserIdCandidates": t.array(t.string()).optional(),
            "limitAdTracking": t.boolean().optional(),
            "quantity": t.string().optional(),
            "ordinal": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionOut"])
    types["CustomRichMediaEventsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "filteredEventIds": t.array(
                t.proxy(renames["DimensionValueIn"])
            ).optional(),
        }
    ).named(renames["CustomRichMediaEventsIn"])
    types["CustomRichMediaEventsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "filteredEventIds": t.array(
                t.proxy(renames["DimensionValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomRichMediaEventsOut"])
    types["UserDefinedVariableConfigurationIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "variableType": t.string().optional(),
            "reportName": t.string().optional(),
        }
    ).named(renames["UserDefinedVariableConfigurationIn"])
    types["UserDefinedVariableConfigurationOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "variableType": t.string().optional(),
            "reportName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDefinedVariableConfigurationOut"])
    types["UserProfileListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["UserProfileIn"])).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UserProfileListIn"])
    types["UserProfileListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["UserProfileOut"])).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserProfileListOut"])
    types["SiteVideoSettingsIn"] = t.struct(
        {
            "publisherSpecificationId": t.string().optional(),
            "transcodeSettings": t.proxy(renames["SiteTranscodeSettingIn"]).optional(),
            "obaSettings": t.proxy(renames["ObaIconIn"]).optional(),
            "companionSettings": t.proxy(renames["SiteCompanionSettingIn"]).optional(),
            "kind": t.string().optional(),
            "obaEnabled": t.boolean().optional(),
            "skippableSettings": t.proxy(renames["SiteSkippableSettingIn"]).optional(),
            "orientation": t.string().optional(),
        }
    ).named(renames["SiteVideoSettingsIn"])
    types["SiteVideoSettingsOut"] = t.struct(
        {
            "publisherSpecificationId": t.string().optional(),
            "transcodeSettings": t.proxy(renames["SiteTranscodeSettingOut"]).optional(),
            "obaSettings": t.proxy(renames["ObaIconOut"]).optional(),
            "companionSettings": t.proxy(renames["SiteCompanionSettingOut"]).optional(),
            "kind": t.string().optional(),
            "obaEnabled": t.boolean().optional(),
            "skippableSettings": t.proxy(renames["SiteSkippableSettingOut"]).optional(),
            "orientation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteVideoSettingsOut"])
    types["PostalCodeIn"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "code": t.string().optional(),
            "countryDartId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PostalCodeIn"])
    types["PostalCodeOut"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "code": t.string().optional(),
            "countryDartId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalCodeOut"])
    types["DayPartTargetingIn"] = t.struct(
        {
            "daysOfWeek": t.array(t.string()).optional(),
            "hoursOfDay": t.array(t.integer()).optional(),
            "userLocalTime": t.boolean().optional(),
        }
    ).named(renames["DayPartTargetingIn"])
    types["DayPartTargetingOut"] = t.struct(
        {
            "daysOfWeek": t.array(t.string()).optional(),
            "hoursOfDay": t.array(t.integer()).optional(),
            "userLocalTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartTargetingOut"])
    types["CountriesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "countries": t.array(t.proxy(renames["CountryIn"])).optional(),
        }
    ).named(renames["CountriesListResponseIn"])
    types["CountriesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "countries": t.array(t.proxy(renames["CountryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountriesListResponseOut"])
    types["ProjectsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "projects": t.array(t.proxy(renames["ProjectIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ProjectsListResponseIn"])
    types["ProjectsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "projects": t.array(t.proxy(renames["ProjectOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectsListResponseOut"])
    types["BillingRateTieredRateIn"] = t.struct(
        {
            "highValue": t.string().optional(),
            "lowValue": t.string().optional(),
            "rateInMicros": t.string().optional(),
        }
    ).named(renames["BillingRateTieredRateIn"])
    types["BillingRateTieredRateOut"] = t.struct(
        {
            "highValue": t.string().optional(),
            "lowValue": t.string().optional(),
            "rateInMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingRateTieredRateOut"])
    types["CreativeCustomEventIn"] = t.struct(
        {
            "targetType": t.string().optional(),
            "advertiserCustomEventType": t.string().optional(),
            "artworkType": t.string().optional(),
            "artworkLabel": t.string().optional(),
            "id": t.string().optional(),
            "advertiserCustomEventId": t.string().optional(),
            "exitClickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlIn"]
            ).optional(),
            "videoReportingId": t.string().optional(),
            "advertiserCustomEventName": t.string().optional(),
            "popupWindowProperties": t.proxy(
                renames["PopupWindowPropertiesIn"]
            ).optional(),
        }
    ).named(renames["CreativeCustomEventIn"])
    types["CreativeCustomEventOut"] = t.struct(
        {
            "targetType": t.string().optional(),
            "advertiserCustomEventType": t.string().optional(),
            "artworkType": t.string().optional(),
            "artworkLabel": t.string().optional(),
            "id": t.string().optional(),
            "advertiserCustomEventId": t.string().optional(),
            "exitClickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlOut"]
            ).optional(),
            "videoReportingId": t.string().optional(),
            "advertiserCustomEventName": t.string().optional(),
            "popupWindowProperties": t.proxy(
                renames["PopupWindowPropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeCustomEventOut"])
    types["DimensionIn"] = t.struct(
        {"name": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["DimensionIn"])
    types["DimensionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOut"])
    types["TagSettingIn"] = t.struct(
        {
            "includeClickThroughUrls": t.boolean().optional(),
            "includeClickTracking": t.boolean().optional(),
            "keywordOption": t.string().optional(),
            "additionalKeyValues": t.string().optional(),
        }
    ).named(renames["TagSettingIn"])
    types["TagSettingOut"] = t.struct(
        {
            "includeClickThroughUrls": t.boolean().optional(),
            "includeClickTracking": t.boolean().optional(),
            "keywordOption": t.string().optional(),
            "additionalKeyValues": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagSettingOut"])
    types["DirectorySiteIn"] = t.struct(
        {
            "interstitialTagFormats": t.array(t.string()).optional(),
            "settings": t.proxy(renames["DirectorySiteSettingsIn"]).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "id": t.string().optional(),
            "inpageTagFormats": t.array(t.string()).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["DirectorySiteIn"])
    types["DirectorySiteOut"] = t.struct(
        {
            "interstitialTagFormats": t.array(t.string()).optional(),
            "settings": t.proxy(renames["DirectorySiteSettingsOut"]).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "id": t.string().optional(),
            "inpageTagFormats": t.array(t.string()).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectorySiteOut"])
    types["PathToConversionReportCompatibleFieldsIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "perInteractionDimensions": t.array(
                t.proxy(renames["DimensionIn"])
            ).optional(),
            "customFloodlightVariables": t.array(
                t.proxy(renames["DimensionIn"])
            ).optional(),
            "conversionDimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PathToConversionReportCompatibleFieldsIn"])
    types["PathToConversionReportCompatibleFieldsOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "perInteractionDimensions": t.array(
                t.proxy(renames["DimensionOut"])
            ).optional(),
            "customFloodlightVariables": t.array(
                t.proxy(renames["DimensionOut"])
            ).optional(),
            "conversionDimensions": t.array(
                t.proxy(renames["DimensionOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathToConversionReportCompatibleFieldsOut"])
    types["UserRoleIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "parentUserRoleId": t.string().optional(),
            "permissions": t.array(t.proxy(renames["UserRolePermissionIn"])).optional(),
            "defaultUserRole": t.boolean().optional(),
            "id": t.string().optional(),
            "subaccountId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["UserRoleIn"])
    types["UserRoleOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "parentUserRoleId": t.string().optional(),
            "permissions": t.array(
                t.proxy(renames["UserRolePermissionOut"])
            ).optional(),
            "defaultUserRole": t.boolean().optional(),
            "id": t.string().optional(),
            "subaccountId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRoleOut"])
    types["FloodlightActivityDynamicTagIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["FloodlightActivityDynamicTagIn"])
    types["FloodlightActivityDynamicTagOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivityDynamicTagOut"])
    types["CompanionSettingIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "imageOnly": t.boolean().optional(),
            "companionsDisabled": t.boolean().optional(),
            "enabledSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
        }
    ).named(renames["CompanionSettingIn"])
    types["CompanionSettingOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "imageOnly": t.boolean().optional(),
            "companionsDisabled": t.boolean().optional(),
            "enabledSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanionSettingOut"])
    types["CityIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dartId": t.string().optional(),
            "regionCode": t.string().optional(),
            "kind": t.string().optional(),
            "countryCode": t.string().optional(),
            "countryDartId": t.string().optional(),
            "regionDartId": t.string().optional(),
            "metroCode": t.string().optional(),
            "metroDmaId": t.string().optional(),
        }
    ).named(renames["CityIn"])
    types["CityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dartId": t.string().optional(),
            "regionCode": t.string().optional(),
            "kind": t.string().optional(),
            "countryCode": t.string().optional(),
            "countryDartId": t.string().optional(),
            "regionDartId": t.string().optional(),
            "metroCode": t.string().optional(),
            "metroDmaId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CityOut"])
    types["DefaultClickThroughEventTagPropertiesIn"] = t.struct(
        {
            "overrideInheritedEventTag": t.boolean().optional(),
            "defaultClickThroughEventTagId": t.string().optional(),
        }
    ).named(renames["DefaultClickThroughEventTagPropertiesIn"])
    types["DefaultClickThroughEventTagPropertiesOut"] = t.struct(
        {
            "overrideInheritedEventTag": t.boolean().optional(),
            "defaultClickThroughEventTagId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultClickThroughEventTagPropertiesOut"])
    types["SitesListResponseIn"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SitesListResponseIn"])
    types["SitesListResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitesListResponseOut"])
    types["CreativeGroupAssignmentIn"] = t.struct(
        {
            "creativeGroupNumber": t.string().optional(),
            "creativeGroupId": t.string().optional(),
        }
    ).named(renames["CreativeGroupAssignmentIn"])
    types["CreativeGroupAssignmentOut"] = t.struct(
        {
            "creativeGroupNumber": t.string().optional(),
            "creativeGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeGroupAssignmentOut"])
    types["DimensionValueListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["DimensionValueIn"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["DimensionValueListIn"])
    types["DimensionValueListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["DimensionValueOut"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueListOut"])
    types["CreativeAssignmentIn"] = t.struct(
        {
            "companionCreativeOverrides": t.array(
                t.proxy(renames["CompanionClickThroughOverrideIn"])
            ).optional(),
            "sequence": t.integer().optional(),
            "creativeIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "weight": t.integer().optional(),
            "creativeGroupAssignments": t.array(
                t.proxy(renames["CreativeGroupAssignmentIn"])
            ).optional(),
            "richMediaExitOverrides": t.array(
                t.proxy(renames["RichMediaExitOverrideIn"])
            ).optional(),
            "sslCompliant": t.boolean().optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
            "startTime": t.string(),
            "endTime": t.string(),
            "applyEventTags": t.boolean().optional(),
            "active": t.boolean().optional(),
            "creativeId": t.string().optional(),
        }
    ).named(renames["CreativeAssignmentIn"])
    types["CreativeAssignmentOut"] = t.struct(
        {
            "companionCreativeOverrides": t.array(
                t.proxy(renames["CompanionClickThroughOverrideOut"])
            ).optional(),
            "sequence": t.integer().optional(),
            "creativeIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "weight": t.integer().optional(),
            "creativeGroupAssignments": t.array(
                t.proxy(renames["CreativeGroupAssignmentOut"])
            ).optional(),
            "richMediaExitOverrides": t.array(
                t.proxy(renames["RichMediaExitOverrideOut"])
            ).optional(),
            "sslCompliant": t.boolean().optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlOut"]).optional(),
            "startTime": t.string(),
            "endTime": t.string(),
            "applyEventTags": t.boolean().optional(),
            "active": t.boolean().optional(),
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeAssignmentOut"])
    types["AccountPermissionGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountPermissionGroupIn"])
    types["AccountPermissionGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountPermissionGroupOut"])
    types["AdvertiserInvoicesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "invoices": t.array(t.proxy(renames["InvoiceIn"])).optional(),
        }
    ).named(renames["AdvertiserInvoicesListResponseIn"])
    types["AdvertiserInvoicesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "invoices": t.array(t.proxy(renames["InvoiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserInvoicesListResponseOut"])
    types["BillingProfileIn"] = t.struct(
        {
            "isDefault": t.boolean().optional(),
            "currencyCode": t.string().optional(),
            "name": t.string().optional(),
            "consolidatedInvoice": t.boolean().optional(),
            "countryCode": t.string().optional(),
            "paymentsCustomerId": t.string().optional(),
            "kind": t.string().optional(),
            "purchaseOrder": t.string().optional(),
            "secondaryPaymentsCustomerId": t.string().optional(),
            "id": t.string().optional(),
            "invoiceLevel": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["BillingProfileIn"])
    types["BillingProfileOut"] = t.struct(
        {
            "isDefault": t.boolean().optional(),
            "currencyCode": t.string().optional(),
            "name": t.string().optional(),
            "consolidatedInvoice": t.boolean().optional(),
            "countryCode": t.string().optional(),
            "paymentsCustomerId": t.string().optional(),
            "kind": t.string().optional(),
            "purchaseOrder": t.string().optional(),
            "secondaryPaymentsCustomerId": t.string().optional(),
            "id": t.string().optional(),
            "invoiceLevel": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingProfileOut"])
    types["PlacementAssignmentIn"] = t.struct(
        {
            "sslRequired": t.boolean().optional(),
            "placementIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "placementId": t.string().optional(),
            "active": t.boolean().optional(),
        }
    ).named(renames["PlacementAssignmentIn"])
    types["PlacementAssignmentOut"] = t.struct(
        {
            "sslRequired": t.boolean().optional(),
            "placementIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "placementId": t.string().optional(),
            "active": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementAssignmentOut"])
    types["ConversionsBatchInsertResponseIn"] = t.struct(
        {
            "hasFailures": t.boolean().optional(),
            "kind": t.string().optional(),
            "status": t.array(t.proxy(renames["ConversionStatusIn"])).optional(),
        }
    ).named(renames["ConversionsBatchInsertResponseIn"])
    types["ConversionsBatchInsertResponseOut"] = t.struct(
        {
            "hasFailures": t.boolean().optional(),
            "kind": t.string().optional(),
            "status": t.array(t.proxy(renames["ConversionStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionsBatchInsertResponseOut"])
    types["CreativeFieldsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creativeFields": t.array(t.proxy(renames["CreativeFieldIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CreativeFieldsListResponseIn"])
    types["CreativeFieldsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creativeFields": t.array(t.proxy(renames["CreativeFieldOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldsListResponseOut"])
    types["LandingPageIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "advertiserId": t.string().optional(),
            "archived": t.boolean().optional(),
            "id": t.string().optional(),
            "deepLinks": t.array(t.proxy(renames["DeepLinkIn"])).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["LandingPageIn"])
    types["LandingPageOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "advertiserId": t.string().optional(),
            "archived": t.boolean().optional(),
            "id": t.string().optional(),
            "deepLinks": t.array(t.proxy(renames["DeepLinkOut"])).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LandingPageOut"])
    types["ReportsConfigurationIn"] = t.struct(
        {
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationIn"]
            ).optional(),
            "reportGenerationTimeZoneId": t.string().optional(),
            "exposureToConversionEnabled": t.boolean().optional(),
        }
    ).named(renames["ReportsConfigurationIn"])
    types["ReportsConfigurationOut"] = t.struct(
        {
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationOut"]
            ).optional(),
            "reportGenerationTimeZoneId": t.string().optional(),
            "exposureToConversionEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportsConfigurationOut"])
    types["UserProfileIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "subAccountName": t.string().optional(),
            "profileId": t.string().optional(),
            "accountId": t.string().optional(),
            "accountName": t.string().optional(),
            "userName": t.string().optional(),
            "subAccountId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UserProfileIn"])
    types["UserProfileOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "subAccountName": t.string().optional(),
            "profileId": t.string().optional(),
            "accountId": t.string().optional(),
            "accountName": t.string().optional(),
            "userName": t.string().optional(),
            "subAccountId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserProfileOut"])
    types["PlacementIn"] = t.struct(
        {
            "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
            "keyName": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "tagFormats": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
            "sslRequired": t.boolean().optional(),
            "name": t.string().optional(),
            "activeStatus": t.string().optional(),
            "paymentSource": t.string().optional(),
            "partnerWrappingData": t.proxy(
                renames["MeasurementPartnerWrappingDataIn"]
            ).optional(),
            "kind": t.string().optional(),
            "compatibility": t.string().optional(),
            "campaignIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "externalId": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
            "campaignId": t.string().optional(),
            "comment": t.string().optional(),
            "subaccountId": t.string().optional(),
            "placementGroupId": t.string().optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "adBlockingOptOut": t.boolean().optional(),
            "placementGroupIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "siteId": t.string().optional(),
            "directorySiteId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "contentCategoryId": t.string().optional(),
            "publisherUpdateInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "placementStrategyId": t.string().optional(),
            "paymentApproved": t.boolean().optional(),
            "videoActiveViewOptOut": t.boolean().optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationIn"]
            ).optional(),
            "vpaidAdapterChoice": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
            "primary": t.boolean().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "wrappingOptOut": t.boolean().optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
        }
    ).named(renames["PlacementIn"])
    types["PlacementOut"] = t.struct(
        {
            "pricingSchedule": t.proxy(renames["PricingScheduleOut"]).optional(),
            "keyName": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "tagFormats": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "videoSettings": t.proxy(renames["VideoSettingsOut"]).optional(),
            "sslRequired": t.boolean().optional(),
            "name": t.string().optional(),
            "activeStatus": t.string().optional(),
            "paymentSource": t.string().optional(),
            "partnerWrappingData": t.proxy(
                renames["MeasurementPartnerWrappingDataOut"]
            ).optional(),
            "kind": t.string().optional(),
            "compatibility": t.string().optional(),
            "campaignIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "externalId": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "tagSetting": t.proxy(renames["TagSettingOut"]).optional(),
            "campaignId": t.string().optional(),
            "comment": t.string().optional(),
            "subaccountId": t.string().optional(),
            "placementGroupId": t.string().optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "adBlockingOptOut": t.boolean().optional(),
            "placementGroupIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "siteId": t.string().optional(),
            "directorySiteId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "contentCategoryId": t.string().optional(),
            "publisherUpdateInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "placementStrategyId": t.string().optional(),
            "paymentApproved": t.boolean().optional(),
            "videoActiveViewOptOut": t.boolean().optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationOut"]
            ).optional(),
            "vpaidAdapterChoice": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
            "primary": t.boolean().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "wrappingOptOut": t.boolean().optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementOut"])
    types["CreativesListResponseIn"] = t.struct(
        {
            "creatives": t.array(t.proxy(renames["CreativeIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CreativesListResponseIn"])
    types["CreativesListResponseOut"] = t.struct(
        {
            "creatives": t.array(t.proxy(renames["CreativeOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativesListResponseOut"])
    types["RemarketingListsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "remarketingLists": t.array(
                t.proxy(renames["RemarketingListIn"])
            ).optional(),
        }
    ).named(renames["RemarketingListsListResponseIn"])
    types["RemarketingListsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "remarketingLists": t.array(
                t.proxy(renames["RemarketingListOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingListsListResponseOut"])
    types["OrderDocumentsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "orderDocuments": t.array(t.proxy(renames["OrderDocumentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["OrderDocumentsListResponseIn"])
    types["OrderDocumentsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "orderDocuments": t.array(t.proxy(renames["OrderDocumentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderDocumentsListResponseOut"])
    types["TranscodeSettingIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "enabledVideoFormats": t.array(t.integer()).optional(),
        }
    ).named(renames["TranscodeSettingIn"])
    types["TranscodeSettingOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "enabledVideoFormats": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscodeSettingOut"])
    types["MobileCarriersListResponseIn"] = t.struct(
        {
            "mobileCarriers": t.array(t.proxy(renames["MobileCarrierIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["MobileCarriersListResponseIn"])
    types["MobileCarriersListResponseOut"] = t.struct(
        {
            "mobileCarriers": t.array(t.proxy(renames["MobileCarrierOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileCarriersListResponseOut"])
    types["OffsetPositionIn"] = t.struct(
        {"top": t.integer().optional(), "left": t.integer().optional()}
    ).named(renames["OffsetPositionIn"])
    types["OffsetPositionOut"] = t.struct(
        {
            "top": t.integer().optional(),
            "left": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OffsetPositionOut"])
    types["ActivitiesIn"] = t.struct(
        {
            "metricNames": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "filters": t.array(t.proxy(renames["DimensionValueIn"])).optional(),
        }
    ).named(renames["ActivitiesIn"])
    types["ActivitiesOut"] = t.struct(
        {
            "metricNames": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "filters": t.array(t.proxy(renames["DimensionValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitiesOut"])
    types["FloodlightConfigurationsListResponseIn"] = t.struct(
        {
            "floodlightConfigurations": t.array(
                t.proxy(renames["FloodlightConfigurationIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["FloodlightConfigurationsListResponseIn"])
    types["FloodlightConfigurationsListResponseOut"] = t.struct(
        {
            "floodlightConfigurations": t.array(
                t.proxy(renames["FloodlightConfigurationOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightConfigurationsListResponseOut"])
    types["AdvertiserIn"] = t.struct(
        {
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "defaultEmail": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "clickThroughUrlSuffix": t.string().optional(),
            "suspended": t.boolean().optional(),
            "advertiserGroupId": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "subaccountId": t.string().optional(),
            "originalFloodlightConfigurationId": t.string().optional(),
            "name": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "measurementPartnerLink": t.proxy(
                renames["MeasurementPartnerAdvertiserLinkIn"]
            ).optional(),
            "defaultClickThroughEventTagId": t.string().optional(),
        }
    ).named(renames["AdvertiserIn"])
    types["AdvertiserOut"] = t.struct(
        {
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "defaultEmail": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "clickThroughUrlSuffix": t.string().optional(),
            "suspended": t.boolean().optional(),
            "advertiserGroupId": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "subaccountId": t.string().optional(),
            "originalFloodlightConfigurationId": t.string().optional(),
            "name": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "measurementPartnerLink": t.proxy(
                renames["MeasurementPartnerAdvertiserLinkOut"]
            ).optional(),
            "defaultClickThroughEventTagId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserOut"])
    types["PopupWindowPropertiesIn"] = t.struct(
        {
            "showStatusBar": t.boolean().optional(),
            "showMenuBar": t.boolean().optional(),
            "positionType": t.string().optional(),
            "offset": t.proxy(renames["OffsetPositionIn"]).optional(),
            "dimension": t.proxy(renames["SizeIn"]).optional(),
            "showAddressBar": t.boolean().optional(),
            "showToolBar": t.boolean().optional(),
            "title": t.string().optional(),
            "showScrollBar": t.boolean().optional(),
        }
    ).named(renames["PopupWindowPropertiesIn"])
    types["PopupWindowPropertiesOut"] = t.struct(
        {
            "showStatusBar": t.boolean().optional(),
            "showMenuBar": t.boolean().optional(),
            "positionType": t.string().optional(),
            "offset": t.proxy(renames["OffsetPositionOut"]).optional(),
            "dimension": t.proxy(renames["SizeOut"]).optional(),
            "showAddressBar": t.boolean().optional(),
            "showToolBar": t.boolean().optional(),
            "title": t.string().optional(),
            "showScrollBar": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PopupWindowPropertiesOut"])
    types["ReportCompatibleFieldsIn"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "kind": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "pivotedActivityMetrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["ReportCompatibleFieldsIn"])
    types["ReportCompatibleFieldsOut"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "kind": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "pivotedActivityMetrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportCompatibleFieldsOut"])
    types["MetrosListResponseIn"] = t.struct(
        {
            "metros": t.array(t.proxy(renames["MetroIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["MetrosListResponseIn"])
    types["MetrosListResponseOut"] = t.struct(
        {
            "metros": t.array(t.proxy(renames["MetroOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetrosListResponseOut"])
    types["UserRolePermissionGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["UserRolePermissionGroupIn"])
    types["UserRolePermissionGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRolePermissionGroupOut"])
    types["AudienceSegmentGroupIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "audienceSegments": t.array(
                t.proxy(renames["AudienceSegmentIn"])
            ).optional(),
        }
    ).named(renames["AudienceSegmentGroupIn"])
    types["AudienceSegmentGroupOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "audienceSegments": t.array(
                t.proxy(renames["AudienceSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudienceSegmentGroupOut"])
    types["ConnectionTypesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "connectionTypes": t.array(t.proxy(renames["ConnectionTypeIn"])).optional(),
        }
    ).named(renames["ConnectionTypesListResponseIn"])
    types["ConnectionTypesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "connectionTypes": t.array(
                t.proxy(renames["ConnectionTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionTypesListResponseOut"])
    types["PlatformTypeIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlatformTypeIn"])
    types["PlatformTypeOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformTypeOut"])
    types["CreativeGroupIn"] = t.struct(
        {
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "groupNumber": t.integer().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["CreativeGroupIn"])
    types["CreativeGroupOut"] = t.struct(
        {
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "groupNumber": t.integer().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeGroupOut"])
    types["CreativeAssetIn"] = t.struct(
        {
            "audioBitRate": t.integer().optional(),
            "artworkType": t.string().optional(),
            "position": t.proxy(renames["OffsetPositionIn"]).optional(),
            "mediaDuration": t.number().optional(),
            "pushdownDuration": t.number().optional(),
            "assetIdentifier": t.proxy(renames["CreativeAssetIdIn"]).optional(),
            "verticallyLocked": t.boolean().optional(),
            "hideFlashObjects": t.boolean().optional(),
            "active": t.boolean().optional(),
            "positionTopUnit": t.string().optional(),
            "fileSize": t.string().optional(),
            "customStartTimeValue": t.integer().optional(),
            "transparency": t.boolean().optional(),
            "flashVersion": t.integer().optional(),
            "sslCompliant": t.boolean().optional(),
            "originalBackup": t.boolean().optional(),
            "startTimeType": t.string().optional(),
            "expandedDimension": t.proxy(renames["SizeIn"]).optional(),
            "detectedFeatures": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "offset": t.proxy(renames["OffsetPositionIn"]).optional(),
            "durationType": t.string().optional(),
            "collapsedSize": t.proxy(renames["SizeIn"]).optional(),
            "zipFilename": t.string().optional(),
            "id": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "alignment": t.string().optional(),
            "frameRate": t.number().optional(),
            "audioSampleRate": t.integer().optional(),
            "displayType": t.string().optional(),
            "orientation": t.string().optional(),
            "hideSelectionBoxes": t.boolean().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "duration": t.integer().optional(),
            "pushdown": t.boolean().optional(),
            "mimeType": t.string().optional(),
            "positionLeftUnit": t.string().optional(),
            "actionScript3": t.boolean().optional(),
            "horizontallyLocked": t.boolean().optional(),
            "backupImageExit": t.proxy(renames["CreativeCustomEventIn"]).optional(),
            "windowMode": t.string().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "politeLoad": t.boolean().optional(),
            "progressiveServingUrl": t.string().optional(),
            "zipFilesize": t.string().optional(),
            "bitRate": t.integer().optional(),
            "streamingServingUrl": t.string().optional(),
            "childAssetType": t.string().optional(),
            "zIndex": t.integer().optional(),
        }
    ).named(renames["CreativeAssetIn"])
    types["CreativeAssetOut"] = t.struct(
        {
            "audioBitRate": t.integer().optional(),
            "artworkType": t.string().optional(),
            "position": t.proxy(renames["OffsetPositionOut"]).optional(),
            "mediaDuration": t.number().optional(),
            "pushdownDuration": t.number().optional(),
            "assetIdentifier": t.proxy(renames["CreativeAssetIdOut"]).optional(),
            "verticallyLocked": t.boolean().optional(),
            "hideFlashObjects": t.boolean().optional(),
            "active": t.boolean().optional(),
            "positionTopUnit": t.string().optional(),
            "fileSize": t.string().optional(),
            "customStartTimeValue": t.integer().optional(),
            "transparency": t.boolean().optional(),
            "flashVersion": t.integer().optional(),
            "sslCompliant": t.boolean().optional(),
            "originalBackup": t.boolean().optional(),
            "startTimeType": t.string().optional(),
            "expandedDimension": t.proxy(renames["SizeOut"]).optional(),
            "detectedFeatures": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "offset": t.proxy(renames["OffsetPositionOut"]).optional(),
            "durationType": t.string().optional(),
            "collapsedSize": t.proxy(renames["SizeOut"]).optional(),
            "zipFilename": t.string().optional(),
            "id": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "alignment": t.string().optional(),
            "frameRate": t.number().optional(),
            "audioSampleRate": t.integer().optional(),
            "displayType": t.string().optional(),
            "orientation": t.string().optional(),
            "hideSelectionBoxes": t.boolean().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "duration": t.integer().optional(),
            "pushdown": t.boolean().optional(),
            "mimeType": t.string().optional(),
            "positionLeftUnit": t.string().optional(),
            "actionScript3": t.boolean().optional(),
            "horizontallyLocked": t.boolean().optional(),
            "backupImageExit": t.proxy(renames["CreativeCustomEventOut"]).optional(),
            "windowMode": t.string().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "politeLoad": t.boolean().optional(),
            "progressiveServingUrl": t.string().optional(),
            "zipFilesize": t.string().optional(),
            "bitRate": t.integer().optional(),
            "streamingServingUrl": t.string().optional(),
            "childAssetType": t.string().optional(),
            "zIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeAssetOut"])
    types["AdsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "ads": t.array(t.proxy(renames["AdIn"])).optional(),
        }
    ).named(renames["AdsListResponseIn"])
    types["AdsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "ads": t.array(t.proxy(renames["AdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdsListResponseOut"])
    types["CitiesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "cities": t.array(t.proxy(renames["CityIn"])).optional(),
        }
    ).named(renames["CitiesListResponseIn"])
    types["CitiesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "cities": t.array(t.proxy(renames["CityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CitiesListResponseOut"])
    types["UserRolePermissionsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "userRolePermissions": t.array(
                t.proxy(renames["UserRolePermissionIn"])
            ).optional(),
        }
    ).named(renames["UserRolePermissionsListResponseIn"])
    types["UserRolePermissionsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "userRolePermissions": t.array(
                t.proxy(renames["UserRolePermissionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRolePermissionsListResponseOut"])
    types["FrequencyCapIn"] = t.struct(
        {"duration": t.string().optional(), "impressions": t.string().optional()}
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "impressions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
    types["EventFilterIn"] = t.struct(
        {
            "uvarFilter": t.proxy(renames["UvarFilterIn"]).optional(),
            "kind": t.string().optional(),
            "dimensionFilter": t.proxy(
                renames["PathReportDimensionValueIn"]
            ).optional(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "uvarFilter": t.proxy(renames["UvarFilterOut"]).optional(),
            "kind": t.string().optional(),
            "dimensionFilter": t.proxy(
                renames["PathReportDimensionValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
    types["BillingRatesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "billingRates": t.array(t.proxy(renames["BillingRateIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BillingRatesListResponseIn"])
    types["BillingRatesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "billingRates": t.array(t.proxy(renames["BillingRateOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingRatesListResponseOut"])
    types["ConversionsBatchInsertRequestIn"] = t.struct(
        {
            "conversions": t.array(t.proxy(renames["ConversionIn"])).optional(),
            "kind": t.string().optional(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoIn"]).optional(),
        }
    ).named(renames["ConversionsBatchInsertRequestIn"])
    types["ConversionsBatchInsertRequestOut"] = t.struct(
        {
            "conversions": t.array(t.proxy(renames["ConversionOut"])).optional(),
            "kind": t.string().optional(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionsBatchInsertRequestOut"])
    types["ChangeLogIn"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "action": t.string().optional(),
            "id": t.string().optional(),
            "userProfileId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "kind": t.string().optional(),
            "objectId": t.string().optional(),
            "newValue": t.string().optional(),
            "oldValue": t.string().optional(),
            "changeTime": t.string(),
            "objectType": t.string().optional(),
            "accountId": t.string().optional(),
            "userProfileName": t.string().optional(),
            "transactionId": t.string().optional(),
        }
    ).named(renames["ChangeLogIn"])
    types["ChangeLogOut"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "action": t.string().optional(),
            "id": t.string().optional(),
            "userProfileId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "kind": t.string().optional(),
            "objectId": t.string().optional(),
            "newValue": t.string().optional(),
            "oldValue": t.string().optional(),
            "changeTime": t.string(),
            "objectType": t.string().optional(),
            "accountId": t.string().optional(),
            "userProfileName": t.string().optional(),
            "transactionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeLogOut"])
    types["CreativeGroupsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "creativeGroups": t.array(t.proxy(renames["CreativeGroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CreativeGroupsListResponseIn"])
    types["CreativeGroupsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "creativeGroups": t.array(t.proxy(renames["CreativeGroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeGroupsListResponseOut"])
    types["RemarketingListShareIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "sharedAccountIds": t.array(t.string()).optional(),
            "remarketingListId": t.string().optional(),
        }
    ).named(renames["RemarketingListShareIn"])
    types["RemarketingListShareOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "sharedAccountIds": t.array(t.string()).optional(),
            "remarketingListId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingListShareOut"])
    types["SiteIn"] = t.struct(
        {
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "id": t.string().optional(),
            "keyName": t.string().optional(),
            "subaccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "directorySiteId": t.string().optional(),
            "kind": t.string().optional(),
            "approved": t.boolean().optional(),
            "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
            "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SiteIn"])
    types["SiteOut"] = t.struct(
        {
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "videoSettings": t.proxy(renames["SiteVideoSettingsOut"]).optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "id": t.string().optional(),
            "keyName": t.string().optional(),
            "subaccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "directorySiteId": t.string().optional(),
            "kind": t.string().optional(),
            "approved": t.boolean().optional(),
            "siteSettings": t.proxy(renames["SiteSettingsOut"]).optional(),
            "siteContacts": t.array(t.proxy(renames["SiteContactOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteOut"])
    types["AdvertiserLandingPagesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "landingPages": t.array(t.proxy(renames["LandingPageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AdvertiserLandingPagesListResponseIn"])
    types["AdvertiserLandingPagesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "landingPages": t.array(t.proxy(renames["LandingPageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserLandingPagesListResponseOut"])
    types["SiteCompanionSettingIn"] = t.struct(
        {
            "companionsDisabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "imageOnly": t.boolean().optional(),
            "enabledSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
        }
    ).named(renames["SiteCompanionSettingIn"])
    types["SiteCompanionSettingOut"] = t.struct(
        {
            "companionsDisabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "imageOnly": t.boolean().optional(),
            "enabledSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteCompanionSettingOut"])
    types["GeoTargetingIn"] = t.struct(
        {
            "countries": t.array(t.proxy(renames["CountryIn"])).optional(),
            "cities": t.array(t.proxy(renames["CityIn"])).optional(),
            "postalCodes": t.array(t.proxy(renames["PostalCodeIn"])).optional(),
            "metros": t.array(t.proxy(renames["MetroIn"])).optional(),
            "excludeCountries": t.boolean().optional(),
            "regions": t.array(t.proxy(renames["RegionIn"])).optional(),
        }
    ).named(renames["GeoTargetingIn"])
    types["GeoTargetingOut"] = t.struct(
        {
            "countries": t.array(t.proxy(renames["CountryOut"])).optional(),
            "cities": t.array(t.proxy(renames["CityOut"])).optional(),
            "postalCodes": t.array(t.proxy(renames["PostalCodeOut"])).optional(),
            "metros": t.array(t.proxy(renames["MetroOut"])).optional(),
            "excludeCountries": t.boolean().optional(),
            "regions": t.array(t.proxy(renames["RegionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoTargetingOut"])
    types["CountryIn"] = t.struct(
        {
            "sslEnabled": t.boolean().optional(),
            "countryCode": t.string().optional(),
            "dartId": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CountryIn"])
    types["CountryOut"] = t.struct(
        {
            "sslEnabled": t.boolean().optional(),
            "countryCode": t.string().optional(),
            "dartId": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountryOut"])
    types["AdvertiserGroupsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "advertiserGroups": t.array(
                t.proxy(renames["AdvertiserGroupIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AdvertiserGroupsListResponseIn"])
    types["AdvertiserGroupsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "advertiserGroups": t.array(
                t.proxy(renames["AdvertiserGroupOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserGroupsListResponseOut"])
    types["AccountActiveAdSummaryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "activeAds": t.string().optional(),
            "activeAdsLimitTier": t.string().optional(),
            "availableAds": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["AccountActiveAdSummaryIn"])
    types["AccountActiveAdSummaryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "activeAds": t.string().optional(),
            "activeAdsLimitTier": t.string().optional(),
            "availableAds": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountActiveAdSummaryOut"])
    types["RegionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "regionCode": t.string().optional(),
            "name": t.string().optional(),
            "countryCode": t.string().optional(),
            "dartId": t.string().optional(),
            "countryDartId": t.string().optional(),
        }
    ).named(renames["RegionIn"])
    types["RegionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "regionCode": t.string().optional(),
            "name": t.string().optional(),
            "countryCode": t.string().optional(),
            "dartId": t.string().optional(),
            "countryDartId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionOut"])
    types["CreativeFieldIn"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CreativeFieldIn"])
    types["CreativeFieldOut"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldOut"])
    types["DirectorySitesListResponseIn"] = t.struct(
        {
            "directorySites": t.array(t.proxy(renames["DirectorySiteIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DirectorySitesListResponseIn"])
    types["DirectorySitesListResponseOut"] = t.struct(
        {
            "directorySites": t.array(t.proxy(renames["DirectorySiteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectorySitesListResponseOut"])
    types["SubaccountsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "subaccounts": t.array(t.proxy(renames["SubaccountIn"])).optional(),
        }
    ).named(renames["SubaccountsListResponseIn"])
    types["SubaccountsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "subaccounts": t.array(t.proxy(renames["SubaccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubaccountsListResponseOut"])
    types["AdBlockingConfigurationIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdBlockingConfigurationIn"])
    types["AdBlockingConfigurationOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdBlockingConfigurationOut"])
    types["CampaignSummaryIn"] = t.struct(
        {
            "preTaxAmountMicros": t.string().optional(),
            "campaignId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "taxAmountMicros": t.string().optional(),
            "billingInvoiceCode": t.string().optional(),
        }
    ).named(renames["CampaignSummaryIn"])
    types["CampaignSummaryOut"] = t.struct(
        {
            "preTaxAmountMicros": t.string().optional(),
            "campaignId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "taxAmountMicros": t.string().optional(),
            "billingInvoiceCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignSummaryOut"])
    types["ChannelGroupingRuleIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "disjunctiveMatchStatements": t.array(
                t.proxy(renames["DisjunctiveMatchStatementIn"])
            ).optional(),
        }
    ).named(renames["ChannelGroupingRuleIn"])
    types["ChannelGroupingRuleOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "disjunctiveMatchStatements": t.array(
                t.proxy(renames["DisjunctiveMatchStatementOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelGroupingRuleOut"])
    types["CampaignCreativeAssociationsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "campaignCreativeAssociations": t.array(
                t.proxy(renames["CampaignCreativeAssociationIn"])
            ).optional(),
        }
    ).named(renames["CampaignCreativeAssociationsListResponseIn"])
    types["CampaignCreativeAssociationsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "campaignCreativeAssociations": t.array(
                t.proxy(renames["CampaignCreativeAssociationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignCreativeAssociationsListResponseOut"])
    types["PlacementsListResponseIn"] = t.struct(
        {
            "placements": t.array(t.proxy(renames["PlacementIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PlacementsListResponseIn"])
    types["PlacementsListResponseOut"] = t.struct(
        {
            "placements": t.array(t.proxy(renames["PlacementOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementsListResponseOut"])
    types["ObjectFilterIn"] = t.struct(
        {
            "status": t.string().optional(),
            "objectIds": t.array(t.string()).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ObjectFilterIn"])
    types["ObjectFilterOut"] = t.struct(
        {
            "status": t.string().optional(),
            "objectIds": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectFilterOut"])
    types["ReachReportCompatibleFieldsIn"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "kind": t.string().optional(),
            "reachByFrequencyMetrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "pivotedActivityMetrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
        }
    ).named(renames["ReachReportCompatibleFieldsIn"])
    types["ReachReportCompatibleFieldsOut"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "kind": t.string().optional(),
            "reachByFrequencyMetrics": t.array(
                t.proxy(renames["MetricOut"])
            ).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "pivotedActivityMetrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReachReportCompatibleFieldsOut"])
    types["AccountPermissionIn"] = t.struct(
        {
            "accountProfiles": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "permissionGroupId": t.string().optional(),
            "level": t.string().optional(),
        }
    ).named(renames["AccountPermissionIn"])
    types["AccountPermissionOut"] = t.struct(
        {
            "accountProfiles": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "permissionGroupId": t.string().optional(),
            "level": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountPermissionOut"])
    types["TargetingTemplatesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "targetingTemplates": t.array(
                t.proxy(renames["TargetingTemplateIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["TargetingTemplatesListResponseIn"])
    types["TargetingTemplatesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "targetingTemplates": t.array(
                t.proxy(renames["TargetingTemplateOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingTemplatesListResponseOut"])
    types["PathReportDimensionValueIn"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "matchType": t.string().optional(),
            "ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["PathReportDimensionValueIn"])
    types["PathReportDimensionValueOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "matchType": t.string().optional(),
            "ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathReportDimensionValueOut"])
    types["CreativeAssetSelectionIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
            "defaultAssetId": t.string().optional(),
        }
    ).named(renames["CreativeAssetSelectionIn"])
    types["CreativeAssetSelectionOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "defaultAssetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeAssetSelectionOut"])
    types["SizesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "sizes": t.array(t.proxy(renames["SizeIn"])).optional(),
        }
    ).named(renames["SizesListResponseIn"])
    types["SizesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "sizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SizesListResponseOut"])
    types["ConversionsBatchUpdateResponseIn"] = t.struct(
        {
            "status": t.array(t.proxy(renames["ConversionStatusIn"])).optional(),
            "kind": t.string().optional(),
            "hasFailures": t.boolean().optional(),
        }
    ).named(renames["ConversionsBatchUpdateResponseIn"])
    types["ConversionsBatchUpdateResponseOut"] = t.struct(
        {
            "status": t.array(t.proxy(renames["ConversionStatusOut"])).optional(),
            "kind": t.string().optional(),
            "hasFailures": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionsBatchUpdateResponseOut"])
    types["UniversalAdIdIn"] = t.struct(
        {"registry": t.string().optional(), "value": t.string().optional()}
    ).named(renames["UniversalAdIdIn"])
    types["UniversalAdIdOut"] = t.struct(
        {
            "registry": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UniversalAdIdOut"])
    types["CreativeAssetIdIn"] = t.struct(
        {"name": t.string().optional(), "type": t.string().optional()}
    ).named(renames["CreativeAssetIdIn"])
    types["CreativeAssetIdOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeAssetIdOut"])
    types["UserRolesListResponseIn"] = t.struct(
        {
            "userRoles": t.array(t.proxy(renames["UserRoleIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UserRolesListResponseIn"])
    types["UserRolesListResponseOut"] = t.struct(
        {
            "userRoles": t.array(t.proxy(renames["UserRoleOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRolesListResponseOut"])
    types["AccountsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "accounts": t.array(t.proxy(renames["AccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AccountsListResponseIn"])
    types["AccountsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "accounts": t.array(t.proxy(renames["AccountOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsListResponseOut"])
    types["SiteContactIn"] = t.struct(
        {
            "contactType": t.string().optional(),
            "address": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "email": t.string().optional(),
            "phone": t.string().optional(),
            "firstName": t.string().optional(),
            "lastName": t.string().optional(),
        }
    ).named(renames["SiteContactIn"])
    types["SiteContactOut"] = t.struct(
        {
            "contactType": t.string().optional(),
            "address": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "email": t.string().optional(),
            "phone": t.string().optional(),
            "firstName": t.string().optional(),
            "lastName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteContactOut"])
    types["EncryptionInfoIn"] = t.struct(
        {
            "encryptionEntityType": t.string().optional(),
            "encryptionEntityId": t.string().optional(),
            "encryptionSource": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["EncryptionInfoIn"])
    types["EncryptionInfoOut"] = t.struct(
        {
            "encryptionEntityType": t.string().optional(),
            "encryptionEntityId": t.string().optional(),
            "encryptionSource": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionInfoOut"])
    types["OrderDocumentIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "cancelled": t.boolean().optional(),
            "signed": t.boolean().optional(),
            "lastSentRecipients": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "type": t.string().optional(),
            "kind": t.string().optional(),
            "effectiveDate": t.string(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "advertiserId": t.string().optional(),
            "orderId": t.string().optional(),
            "amendedOrderDocumentId": t.string().optional(),
            "approvedByUserProfileIds": t.array(t.string()).optional(),
            "lastSentTime": t.string(),
            "createdInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
        }
    ).named(renames["OrderDocumentIn"])
    types["OrderDocumentOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "cancelled": t.boolean().optional(),
            "signed": t.boolean().optional(),
            "lastSentRecipients": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "type": t.string().optional(),
            "kind": t.string().optional(),
            "effectiveDate": t.string(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "advertiserId": t.string().optional(),
            "orderId": t.string().optional(),
            "amendedOrderDocumentId": t.string().optional(),
            "approvedByUserProfileIds": t.array(t.string()).optional(),
            "lastSentTime": t.string(),
            "createdInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderDocumentOut"])
    types["ChannelGroupingIn"] = t.struct(
        {
            "fallbackName": t.string().optional(),
            "rules": t.array(t.proxy(renames["ChannelGroupingRuleIn"])).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ChannelGroupingIn"])
    types["ChannelGroupingOut"] = t.struct(
        {
            "fallbackName": t.string().optional(),
            "rules": t.array(t.proxy(renames["ChannelGroupingRuleOut"])).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelGroupingOut"])
    types["VideoFormatIn"] = t.struct(
        {
            "targetBitRate": t.integer().optional(),
            "resolution": t.proxy(renames["SizeIn"]).optional(),
            "fileType": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.integer().optional(),
        }
    ).named(renames["VideoFormatIn"])
    types["VideoFormatOut"] = t.struct(
        {
            "targetBitRate": t.integer().optional(),
            "resolution": t.proxy(renames["SizeOut"]).optional(),
            "fileType": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFormatOut"])
    types["CreativeFieldAssignmentIn"] = t.struct(
        {
            "creativeFieldId": t.string().optional(),
            "creativeFieldValueId": t.string().optional(),
        }
    ).named(renames["CreativeFieldAssignmentIn"])
    types["CreativeFieldAssignmentOut"] = t.struct(
        {
            "creativeFieldId": t.string().optional(),
            "creativeFieldValueId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldAssignmentOut"])
    types["ThirdPartyTrackingUrlIn"] = t.struct(
        {"url": t.string().optional(), "thirdPartyUrlType": t.string().optional()}
    ).named(renames["ThirdPartyTrackingUrlIn"])
    types["ThirdPartyTrackingUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "thirdPartyUrlType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyTrackingUrlOut"])
    types["ClickThroughUrlSuffixPropertiesIn"] = t.struct(
        {
            "overrideInheritedSuffix": t.boolean().optional(),
            "clickThroughUrlSuffix": t.string().optional(),
        }
    ).named(renames["ClickThroughUrlSuffixPropertiesIn"])
    types["ClickThroughUrlSuffixPropertiesOut"] = t.struct(
        {
            "overrideInheritedSuffix": t.boolean().optional(),
            "clickThroughUrlSuffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClickThroughUrlSuffixPropertiesOut"])
    types["AdSlotIn"] = t.struct(
        {
            "primary": t.boolean().optional(),
            "width": t.string().optional(),
            "paymentSourceType": t.string().optional(),
            "height": t.string().optional(),
            "linkedPlacementId": t.string().optional(),
            "comment": t.string().optional(),
            "compatibility": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AdSlotIn"])
    types["AdSlotOut"] = t.struct(
        {
            "primary": t.boolean().optional(),
            "width": t.string().optional(),
            "paymentSourceType": t.string().optional(),
            "height": t.string().optional(),
            "linkedPlacementId": t.string().optional(),
            "comment": t.string().optional(),
            "compatibility": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSlotOut"])
    types["OperatingSystemVersionsListResponseIn"] = t.struct(
        {
            "operatingSystemVersions": t.array(
                t.proxy(renames["OperatingSystemVersionIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OperatingSystemVersionsListResponseIn"])
    types["OperatingSystemVersionsListResponseOut"] = t.struct(
        {
            "operatingSystemVersions": t.array(
                t.proxy(renames["OperatingSystemVersionOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemVersionsListResponseOut"])
    types["ListPopulationClauseIn"] = t.struct(
        {"terms": t.array(t.proxy(renames["ListPopulationTermIn"])).optional()}
    ).named(renames["ListPopulationClauseIn"])
    types["ListPopulationClauseOut"] = t.struct(
        {
            "terms": t.array(t.proxy(renames["ListPopulationTermOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPopulationClauseOut"])
    types["FloodlightActivityPublisherDynamicTagIn"] = t.struct(
        {
            "clickThrough": t.boolean().optional(),
            "directorySiteId": t.string().optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "siteId": t.string().optional(),
            "viewThrough": t.boolean().optional(),
            "dynamicTag": t.proxy(renames["FloodlightActivityDynamicTagIn"]).optional(),
        }
    ).named(renames["FloodlightActivityPublisherDynamicTagIn"])
    types["FloodlightActivityPublisherDynamicTagOut"] = t.struct(
        {
            "clickThrough": t.boolean().optional(),
            "directorySiteId": t.string().optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "siteId": t.string().optional(),
            "viewThrough": t.boolean().optional(),
            "dynamicTag": t.proxy(
                renames["FloodlightActivityDynamicTagOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivityPublisherDynamicTagOut"])
    types["RichMediaExitOverrideIn"] = t.struct(
        {
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
            "enabled": t.boolean().optional(),
            "exitId": t.string().optional(),
        }
    ).named(renames["RichMediaExitOverrideIn"])
    types["RichMediaExitOverrideOut"] = t.struct(
        {
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlOut"]).optional(),
            "enabled": t.boolean().optional(),
            "exitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichMediaExitOverrideOut"])
    types["SortedDimensionIn"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SortedDimensionIn"])
    types["SortedDimensionOut"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortedDimensionOut"])
    types["MetroIn"] = t.struct(
        {
            "countryDartId": t.string().optional(),
            "dartId": t.string().optional(),
            "dmaId": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "metroCode": t.string().optional(),
            "countryCode": t.string().optional(),
        }
    ).named(renames["MetroIn"])
    types["MetroOut"] = t.struct(
        {
            "countryDartId": t.string().optional(),
            "dartId": t.string().optional(),
            "dmaId": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "metroCode": t.string().optional(),
            "countryCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetroOut"])
    types["CreativeFieldValueIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["CreativeFieldValueIn"])
    types["CreativeFieldValueOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldValueOut"])
    types["PricingIn"] = t.struct(
        {
            "pricingType": t.string().optional(),
            "startDate": t.string(),
            "capCostType": t.string().optional(),
            "endDate": t.string(),
            "groupType": t.string().optional(),
            "flights": t.array(t.proxy(renames["FlightIn"])).optional(),
        }
    ).named(renames["PricingIn"])
    types["PricingOut"] = t.struct(
        {
            "pricingType": t.string().optional(),
            "startDate": t.string(),
            "capCostType": t.string().optional(),
            "endDate": t.string(),
            "groupType": t.string().optional(),
            "flights": t.array(t.proxy(renames["FlightOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingOut"])
    types["TagDataIn"] = t.struct(
        {
            "impressionTag": t.string().optional(),
            "clickTag": t.string().optional(),
            "creativeId": t.string().optional(),
            "format": t.string().optional(),
            "adId": t.string().optional(),
        }
    ).named(renames["TagDataIn"])
    types["TagDataOut"] = t.struct(
        {
            "impressionTag": t.string().optional(),
            "clickTag": t.string().optional(),
            "creativeId": t.string().optional(),
            "format": t.string().optional(),
            "adId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagDataOut"])
    types["DeliveryScheduleIn"] = t.struct(
        {
            "priority": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]).optional(),
            "hardCutoff": t.boolean().optional(),
            "impressionRatio": t.string().optional(),
        }
    ).named(renames["DeliveryScheduleIn"])
    types["DeliveryScheduleOut"] = t.struct(
        {
            "priority": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]).optional(),
            "hardCutoff": t.boolean().optional(),
            "impressionRatio": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryScheduleOut"])
    types["CampaignsListResponseIn"] = t.struct(
        {
            "campaigns": t.array(t.proxy(renames["CampaignIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CampaignsListResponseIn"])
    types["CampaignsListResponseOut"] = t.struct(
        {
            "campaigns": t.array(t.proxy(renames["CampaignOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignsListResponseOut"])
    types["CampaignIn"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultLandingPageId": t.string().optional(),
            "defaultClickThroughEventTagProperties": t.proxy(
                renames["DefaultClickThroughEventTagPropertiesIn"]
            ).optional(),
            "measurementPartnerLink": t.proxy(
                renames["MeasurementPartnerCampaignLinkIn"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "creativeGroupIds": t.array(t.string()).optional(),
            "billingInvoiceCode": t.string().optional(),
            "adBlockingConfiguration": t.proxy(
                renames["AdBlockingConfigurationIn"]
            ).optional(),
            "archived": t.boolean().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "additionalCreativeOptimizationConfigurations": t.array(
                t.proxy(renames["CreativeOptimizationConfigurationIn"])
            ).optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "startDate": t.string(),
            "advertiserGroupId": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "eventTagOverrides": t.array(
                t.proxy(renames["EventTagOverrideIn"])
            ).optional(),
            "clickThroughUrlSuffixProperties": t.proxy(
                renames["ClickThroughUrlSuffixPropertiesIn"]
            ).optional(),
            "comment": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "audienceSegmentGroups": t.array(
                t.proxy(renames["AudienceSegmentGroupIn"])
            ).optional(),
            "endDate": t.string(),
            "kind": t.string().optional(),
            "creativeOptimizationConfiguration": t.proxy(
                renames["CreativeOptimizationConfigurationIn"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "externalId": t.string().optional(),
        }
    ).named(renames["CampaignIn"])
    types["CampaignOut"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultLandingPageId": t.string().optional(),
            "defaultClickThroughEventTagProperties": t.proxy(
                renames["DefaultClickThroughEventTagPropertiesOut"]
            ).optional(),
            "measurementPartnerLink": t.proxy(
                renames["MeasurementPartnerCampaignLinkOut"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "creativeGroupIds": t.array(t.string()).optional(),
            "billingInvoiceCode": t.string().optional(),
            "adBlockingConfiguration": t.proxy(
                renames["AdBlockingConfigurationOut"]
            ).optional(),
            "archived": t.boolean().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "additionalCreativeOptimizationConfigurations": t.array(
                t.proxy(renames["CreativeOptimizationConfigurationOut"])
            ).optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "startDate": t.string(),
            "advertiserGroupId": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "eventTagOverrides": t.array(
                t.proxy(renames["EventTagOverrideOut"])
            ).optional(),
            "clickThroughUrlSuffixProperties": t.proxy(
                renames["ClickThroughUrlSuffixPropertiesOut"]
            ).optional(),
            "comment": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "audienceSegmentGroups": t.array(
                t.proxy(renames["AudienceSegmentGroupOut"])
            ).optional(),
            "endDate": t.string(),
            "kind": t.string().optional(),
            "creativeOptimizationConfiguration": t.proxy(
                renames["CreativeOptimizationConfigurationOut"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "externalId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignOut"])
    types["FloodlightReportCompatibleFieldsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["FloodlightReportCompatibleFieldsIn"])
    types["FloodlightReportCompatibleFieldsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightReportCompatibleFieldsOut"])
    types["PlacementStrategiesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "placementStrategies": t.array(
                t.proxy(renames["PlacementStrategyIn"])
            ).optional(),
        }
    ).named(renames["PlacementStrategiesListResponseIn"])
    types["PlacementStrategiesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "placementStrategies": t.array(
                t.proxy(renames["PlacementStrategyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementStrategiesListResponseOut"])
    types["CreativeOptimizationConfigurationIn"] = t.struct(
        {
            "optimizationActivitys": t.array(
                t.proxy(renames["OptimizationActivityIn"])
            ).optional(),
            "id": t.string().optional(),
            "optimizationModel": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CreativeOptimizationConfigurationIn"])
    types["CreativeOptimizationConfigurationOut"] = t.struct(
        {
            "optimizationActivitys": t.array(
                t.proxy(renames["OptimizationActivityOut"])
            ).optional(),
            "id": t.string().optional(),
            "optimizationModel": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOptimizationConfigurationOut"])
    types["EventTagIn"] = t.struct(
        {
            "siteFilterType": t.string().optional(),
            "campaignId": t.string().optional(),
            "siteIds": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "urlEscapeLevels": t.integer().optional(),
            "subaccountId": t.string().optional(),
            "type": t.string().optional(),
            "excludeFromAdxRequests": t.boolean().optional(),
            "campaignIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "url": t.string().optional(),
            "id": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
            "enabledByDefault": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["EventTagIn"])
    types["EventTagOut"] = t.struct(
        {
            "siteFilterType": t.string().optional(),
            "campaignId": t.string().optional(),
            "siteIds": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "urlEscapeLevels": t.integer().optional(),
            "subaccountId": t.string().optional(),
            "type": t.string().optional(),
            "excludeFromAdxRequests": t.boolean().optional(),
            "campaignIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "url": t.string().optional(),
            "id": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
            "enabledByDefault": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTagOut"])
    types["OperatingSystemIn"] = t.struct(
        {
            "desktop": t.boolean().optional(),
            "dartId": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "mobile": t.boolean().optional(),
        }
    ).named(renames["OperatingSystemIn"])
    types["OperatingSystemOut"] = t.struct(
        {
            "desktop": t.boolean().optional(),
            "dartId": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "mobile": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemOut"])
    types["PlatformTypesListResponseIn"] = t.struct(
        {
            "platformTypes": t.array(t.proxy(renames["PlatformTypeIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlatformTypesListResponseIn"])
    types["PlatformTypesListResponseOut"] = t.struct(
        {
            "platformTypes": t.array(t.proxy(renames["PlatformTypeOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformTypesListResponseOut"])
    types["CustomViewabilityMetricIn"] = t.struct(
        {
            "configuration": t.proxy(
                renames["CustomViewabilityMetricConfigurationIn"]
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CustomViewabilityMetricIn"])
    types["CustomViewabilityMetricOut"] = t.struct(
        {
            "configuration": t.proxy(
                renames["CustomViewabilityMetricConfigurationOut"]
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomViewabilityMetricOut"])
    types["PricingSchedulePricingPeriodIn"] = t.struct(
        {
            "rateOrCostNanos": t.string().optional(),
            "pricingComment": t.string().optional(),
            "units": t.string().optional(),
            "endDate": t.string(),
            "startDate": t.string(),
        }
    ).named(renames["PricingSchedulePricingPeriodIn"])
    types["PricingSchedulePricingPeriodOut"] = t.struct(
        {
            "rateOrCostNanos": t.string().optional(),
            "pricingComment": t.string().optional(),
            "units": t.string().optional(),
            "endDate": t.string(),
            "startDate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingSchedulePricingPeriodOut"])
    types["InventoryItemIn"] = t.struct(
        {
            "negotiationChannelId": t.string().optional(),
            "inPlan": t.boolean().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "name": t.string().optional(),
            "contentCategoryId": t.string().optional(),
            "estimatedConversionRate": t.string().optional(),
            "pricing": t.proxy(renames["PricingIn"]).optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "adSlots": t.array(t.proxy(renames["AdSlotIn"])).optional(),
            "advertiserId": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "orderId": t.string().optional(),
            "siteId": t.string().optional(),
            "estimatedClickThroughRate": t.string().optional(),
            "type": t.string().optional(),
            "rfpId": t.string().optional(),
            "kind": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["InventoryItemIn"])
    types["InventoryItemOut"] = t.struct(
        {
            "negotiationChannelId": t.string().optional(),
            "inPlan": t.boolean().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "name": t.string().optional(),
            "contentCategoryId": t.string().optional(),
            "estimatedConversionRate": t.string().optional(),
            "pricing": t.proxy(renames["PricingOut"]).optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "adSlots": t.array(t.proxy(renames["AdSlotOut"])).optional(),
            "advertiserId": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "orderId": t.string().optional(),
            "siteId": t.string().optional(),
            "estimatedClickThroughRate": t.string().optional(),
            "type": t.string().optional(),
            "rfpId": t.string().optional(),
            "kind": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryItemOut"])
    types["AdvertiserGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AdvertiserGroupIn"])
    types["AdvertiserGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserGroupOut"])
    types["ReportListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ReportIn"])).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ReportListIn"])
    types["ReportListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ReportOut"])).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportListOut"])
    types["SubaccountIn"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "availablePermissionIds": t.array(t.string()).optional(),
        }
    ).named(renames["SubaccountIn"])
    types["SubaccountOut"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "availablePermissionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubaccountOut"])
    types["SiteTranscodeSettingIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "enabledVideoFormats": t.array(t.integer()).optional(),
        }
    ).named(renames["SiteTranscodeSettingIn"])
    types["SiteTranscodeSettingOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "enabledVideoFormats": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteTranscodeSettingOut"])
    types["CreativeIn"] = t.struct(
        {
            "clickTags": t.array(t.proxy(renames["ClickTagIn"])).optional(),
            "archived": t.boolean().optional(),
            "compatibility": t.array(t.string()).optional(),
            "skippable": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "adTagKeys": t.array(t.string()).optional(),
            "subaccountId": t.string().optional(),
            "mediaDuration": t.number().optional(),
            "backupImageFeatures": t.array(t.string()).optional(),
            "htmlCode": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "requiredFlashPluginVersion": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "thirdPartyRichMediaImpressionsUrl": t.string().optional(),
            "thirdPartyBackupImageImpressionsUrl": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "studioCreativeId": t.string().optional(),
            "autoAdvanceImages": t.boolean().optional(),
            "dynamicAssetSelection": t.boolean().optional(),
            "companionCreatives": t.array(t.string()).optional(),
            "redirectUrl": t.string().optional(),
            "active": t.boolean().optional(),
            "studioAdvertiserId": t.string().optional(),
            "allowScriptAccess": t.boolean().optional(),
            "renderingId": t.string().optional(),
            "backupImageTargetWindow": t.proxy(renames["TargetWindowIn"]).optional(),
            "thirdPartyUrls": t.array(
                t.proxy(renames["ThirdPartyTrackingUrlIn"])
            ).optional(),
            "overrideCss": t.string().optional(),
            "totalFileSize": t.string().optional(),
            "artworkType": t.string().optional(),
            "creativeAssetSelection": t.proxy(renames["CreativeAssetSelectionIn"]),
            "backupImageClickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlIn"]
            ).optional(),
            "requiredFlashVersion": t.integer().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
            "commercialId": t.string().optional(),
            "studioTraffickedCreativeId": t.string().optional(),
            "htmlCodeLocked": t.boolean().optional(),
            "sslOverride": t.boolean().optional(),
            "kind": t.string().optional(),
            "exitCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "sslCompliant": t.boolean().optional(),
            "latestTraffickedCreativeId": t.string().optional(),
            "counterCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "name": t.string().optional(),
            "backupImageReportingLabel": t.string().optional(),
            "fsCommand": t.proxy(renames["FsCommandIn"]).optional(),
            "creativeFieldAssignments": t.array(
                t.proxy(renames["CreativeFieldAssignmentIn"])
            ).optional(),
            "type": t.string().optional(),
            "renderingIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "authoringTool": t.string().optional(),
            "progressOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
            "mediaDescription": t.string().optional(),
            "authoringSource": t.string().optional(),
            "creativeAssets": t.array(t.proxy(renames["CreativeAssetIn"])).optional(),
            "convertFlashToHtml5": t.boolean().optional(),
            "timerCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "adParameters": t.string().optional(),
            "accountId": t.string().optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
            "version": t.integer().optional(),
            "customKeyValues": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "clickTags": t.array(t.proxy(renames["ClickTagOut"])).optional(),
            "archived": t.boolean().optional(),
            "compatibility": t.array(t.string()).optional(),
            "skippable": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "adTagKeys": t.array(t.string()).optional(),
            "subaccountId": t.string().optional(),
            "mediaDuration": t.number().optional(),
            "backupImageFeatures": t.array(t.string()).optional(),
            "htmlCode": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "requiredFlashPluginVersion": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "thirdPartyRichMediaImpressionsUrl": t.string().optional(),
            "thirdPartyBackupImageImpressionsUrl": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "studioCreativeId": t.string().optional(),
            "autoAdvanceImages": t.boolean().optional(),
            "dynamicAssetSelection": t.boolean().optional(),
            "companionCreatives": t.array(t.string()).optional(),
            "redirectUrl": t.string().optional(),
            "active": t.boolean().optional(),
            "studioAdvertiserId": t.string().optional(),
            "allowScriptAccess": t.boolean().optional(),
            "renderingId": t.string().optional(),
            "backupImageTargetWindow": t.proxy(renames["TargetWindowOut"]).optional(),
            "thirdPartyUrls": t.array(
                t.proxy(renames["ThirdPartyTrackingUrlOut"])
            ).optional(),
            "overrideCss": t.string().optional(),
            "totalFileSize": t.string().optional(),
            "artworkType": t.string().optional(),
            "creativeAssetSelection": t.proxy(renames["CreativeAssetSelectionOut"]),
            "backupImageClickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlOut"]
            ).optional(),
            "requiredFlashVersion": t.integer().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "commercialId": t.string().optional(),
            "studioTraffickedCreativeId": t.string().optional(),
            "htmlCodeLocked": t.boolean().optional(),
            "sslOverride": t.boolean().optional(),
            "kind": t.string().optional(),
            "exitCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "sslCompliant": t.boolean().optional(),
            "latestTraffickedCreativeId": t.string().optional(),
            "counterCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "name": t.string().optional(),
            "backupImageReportingLabel": t.string().optional(),
            "fsCommand": t.proxy(renames["FsCommandOut"]).optional(),
            "creativeFieldAssignments": t.array(
                t.proxy(renames["CreativeFieldAssignmentOut"])
            ).optional(),
            "type": t.string().optional(),
            "renderingIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "authoringTool": t.string().optional(),
            "progressOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "mediaDescription": t.string().optional(),
            "authoringSource": t.string().optional(),
            "creativeAssets": t.array(t.proxy(renames["CreativeAssetOut"])).optional(),
            "convertFlashToHtml5": t.boolean().optional(),
            "timerCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "adParameters": t.string().optional(),
            "accountId": t.string().optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdOut"]).optional(),
            "version": t.integer().optional(),
            "customKeyValues": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "obaIcon": t.proxy(renames["ObaIconOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["ConnectionTypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ConnectionTypeIn"])
    types["ConnectionTypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionTypeOut"])
    types["BillingRateIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "unitOfMeasure": t.string().optional(),
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "name": t.string().optional(),
            "tieredRates": t.array(
                t.proxy(renames["BillingRateTieredRateIn"])
            ).optional(),
            "rateInMicros": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["BillingRateIn"])
    types["BillingRateOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "unitOfMeasure": t.string().optional(),
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "name": t.string().optional(),
            "tieredRates": t.array(
                t.proxy(renames["BillingRateTieredRateOut"])
            ).optional(),
            "rateInMicros": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingRateOut"])
    types["AdIn"] = t.struct(
        {
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "creativeGroupAssignments": t.array(
                t.proxy(renames["CreativeGroupAssignmentIn"])
            ).optional(),
            "sslRequired": t.boolean().optional(),
            "accountId": t.string().optional(),
            "deliverySchedule": t.proxy(renames["DeliveryScheduleIn"]).optional(),
            "defaultClickThroughEventTagProperties": t.proxy(
                renames["DefaultClickThroughEventTagPropertiesIn"]
            ).optional(),
            "kind": t.string().optional(),
            "audienceSegmentId": t.string().optional(),
            "archived": t.boolean().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "targetingTemplateId": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
            "advertiserId": t.string().optional(),
            "remarketingListExpression": t.proxy(
                renames["ListTargetingExpressionIn"]
            ).optional(),
            "dynamicClickTracker": t.boolean().optional(),
            "compatibility": t.string().optional(),
            "comments": t.string().optional(),
            "name": t.string().optional(),
            "placementAssignments": t.array(
                t.proxy(renames["PlacementAssignmentIn"])
            ).optional(),
            "startTime": t.string(),
            "type": t.string().optional(),
            "campaignIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "active": t.boolean().optional(),
            "sslCompliant": t.boolean().optional(),
            "keyValueTargetingExpression": t.proxy(
                renames["KeyValueTargetingExpressionIn"]
            ).optional(),
            "campaignId": t.string().optional(),
            "technologyTargeting": t.proxy(renames["TechnologyTargetingIn"]).optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "creativeRotation": t.proxy(renames["CreativeRotationIn"]).optional(),
            "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
            "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
            "eventTagOverrides": t.array(
                t.proxy(renames["EventTagOverrideIn"])
            ).optional(),
            "clickThroughUrlSuffixProperties": t.proxy(
                renames["ClickThroughUrlSuffixPropertiesIn"]
            ).optional(),
            "endTime": t.string(),
        }
    ).named(renames["AdIn"])
    types["AdOut"] = t.struct(
        {
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "creativeGroupAssignments": t.array(
                t.proxy(renames["CreativeGroupAssignmentOut"])
            ).optional(),
            "sslRequired": t.boolean().optional(),
            "accountId": t.string().optional(),
            "deliverySchedule": t.proxy(renames["DeliveryScheduleOut"]).optional(),
            "defaultClickThroughEventTagProperties": t.proxy(
                renames["DefaultClickThroughEventTagPropertiesOut"]
            ).optional(),
            "kind": t.string().optional(),
            "audienceSegmentId": t.string().optional(),
            "archived": t.boolean().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingOut"]).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "targetingTemplateId": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlOut"]).optional(),
            "advertiserId": t.string().optional(),
            "remarketingListExpression": t.proxy(
                renames["ListTargetingExpressionOut"]
            ).optional(),
            "dynamicClickTracker": t.boolean().optional(),
            "compatibility": t.string().optional(),
            "comments": t.string().optional(),
            "name": t.string().optional(),
            "placementAssignments": t.array(
                t.proxy(renames["PlacementAssignmentOut"])
            ).optional(),
            "startTime": t.string(),
            "type": t.string().optional(),
            "campaignIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "active": t.boolean().optional(),
            "sslCompliant": t.boolean().optional(),
            "keyValueTargetingExpression": t.proxy(
                renames["KeyValueTargetingExpressionOut"]
            ).optional(),
            "campaignId": t.string().optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "creativeRotation": t.proxy(renames["CreativeRotationOut"]).optional(),
            "dayPartTargeting": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "geoTargeting": t.proxy(renames["GeoTargetingOut"]).optional(),
            "eventTagOverrides": t.array(
                t.proxy(renames["EventTagOverrideOut"])
            ).optional(),
            "clickThroughUrlSuffixProperties": t.proxy(
                renames["ClickThroughUrlSuffixPropertiesOut"]
            ).optional(),
            "endTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdOut"])
    types["ThirdPartyAuthenticationTokenIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ThirdPartyAuthenticationTokenIn"])
    types["ThirdPartyAuthenticationTokenOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyAuthenticationTokenOut"])
    types["CreativeRotationIn"] = t.struct(
        {
            "creativeOptimizationConfigurationId": t.string().optional(),
            "weightCalculationStrategy": t.string().optional(),
            "creativeAssignments": t.array(
                t.proxy(renames["CreativeAssignmentIn"])
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CreativeRotationIn"])
    types["CreativeRotationOut"] = t.struct(
        {
            "creativeOptimizationConfigurationId": t.string().optional(),
            "weightCalculationStrategy": t.string().optional(),
            "creativeAssignments": t.array(
                t.proxy(renames["CreativeAssignmentOut"])
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRotationOut"])
    types["DynamicTargetingKeysListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "dynamicTargetingKeys": t.array(
                t.proxy(renames["DynamicTargetingKeyIn"])
            ).optional(),
        }
    ).named(renames["DynamicTargetingKeysListResponseIn"])
    types["DynamicTargetingKeysListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "dynamicTargetingKeys": t.array(
                t.proxy(renames["DynamicTargetingKeyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicTargetingKeysListResponseOut"])
    types["ObaIconIn"] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "yPosition": t.string().optional(),
            "iconViewTrackingUrl": t.string().optional(),
            "program": t.string().optional(),
            "iconClickTrackingUrl": t.string().optional(),
            "iconClickThroughUrl": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "xPosition": t.string().optional(),
        }
    ).named(renames["ObaIconIn"])
    types["ObaIconOut"] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "yPosition": t.string().optional(),
            "iconViewTrackingUrl": t.string().optional(),
            "program": t.string().optional(),
            "iconClickTrackingUrl": t.string().optional(),
            "iconClickThroughUrl": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "xPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObaIconOut"])
    types["PlacementGroupsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "placementGroups": t.array(t.proxy(renames["PlacementGroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PlacementGroupsListResponseIn"])
    types["PlacementGroupsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "placementGroups": t.array(
                t.proxy(renames["PlacementGroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementGroupsListResponseOut"])
    types["FileIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "urls": t.struct(
                {"apiUrl": t.string().optional(), "browserUrl": t.string().optional()}
            ).optional(),
            "fileName": t.string().optional(),
            "etag": t.string().optional(),
            "reportId": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "format": t.string().optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "urls": t.struct(
                {"apiUrl": t.string().optional(), "browserUrl": t.string().optional()}
            ).optional(),
            "fileName": t.string().optional(),
            "etag": t.string().optional(),
            "reportId": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "format": t.string().optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["MobileAppIn"] = t.struct(
        {
            "id": t.string().optional(),
            "publisherName": t.string().optional(),
            "kind": t.string().optional(),
            "directory": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["MobileAppIn"])
    types["MobileAppOut"] = t.struct(
        {
            "id": t.string().optional(),
            "publisherName": t.string().optional(),
            "kind": t.string().optional(),
            "directory": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileAppOut"])
    types["LastModifiedInfoIn"] = t.struct({"time": t.string().optional()}).named(
        renames["LastModifiedInfoIn"]
    )
    types["LastModifiedInfoOut"] = t.struct(
        {
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LastModifiedInfoOut"])
    types["BrowsersListResponseIn"] = t.struct(
        {
            "browsers": t.array(t.proxy(renames["BrowserIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BrowsersListResponseIn"])
    types["BrowsersListResponseOut"] = t.struct(
        {
            "browsers": t.array(t.proxy(renames["BrowserOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowsersListResponseOut"])
    types["ClickTagIn"] = t.struct(
        {
            "clickThroughUrl": t.proxy(renames["CreativeClickThroughUrlIn"]).optional(),
            "eventName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ClickTagIn"])
    types["ClickTagOut"] = t.struct(
        {
            "clickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlOut"]
            ).optional(),
            "eventName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClickTagOut"])
    types["CreativeFieldValuesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creativeFieldValues": t.array(
                t.proxy(renames["CreativeFieldValueIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CreativeFieldValuesListResponseIn"])
    types["CreativeFieldValuesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creativeFieldValues": t.array(
                t.proxy(renames["CreativeFieldValueOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldValuesListResponseOut"])
    types["ListTargetingExpressionIn"] = t.struct(
        {"expression": t.string().optional()}
    ).named(renames["ListTargetingExpressionIn"])
    types["ListTargetingExpressionOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetingExpressionOut"])
    types["DimensionValueIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "dimensionName": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "matchType": t.string().optional(),
        }
    ).named(renames["DimensionValueIn"])
    types["DimensionValueOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "dimensionName": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "matchType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueOut"])
    types["DisjunctiveMatchStatementIn"] = t.struct(
        {
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DisjunctiveMatchStatementIn"])
    types["DisjunctiveMatchStatementOut"] = t.struct(
        {
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisjunctiveMatchStatementOut"])
    types["CustomFloodlightVariableIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CustomFloodlightVariableIn"])
    types["CustomFloodlightVariableOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomFloodlightVariableOut"])
    types["InvoiceIn"] = t.struct(
        {
            "campaign_summaries": t.array(
                t.proxy(renames["CampaignSummaryIn"])
            ).optional(),
            "totalAmountMicros": t.string().optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "purchaseOrderNumber": t.string().optional(),
            "issueDate": t.string().optional(),
            "correctedInvoiceId": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "serviceStartDate": t.string().optional(),
            "subtotalAmountMicros": t.string().optional(),
            "id": t.string().optional(),
            "serviceEndDate": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "invoiceType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "dueDate": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
        }
    ).named(renames["InvoiceIn"])
    types["InvoiceOut"] = t.struct(
        {
            "campaign_summaries": t.array(
                t.proxy(renames["CampaignSummaryOut"])
            ).optional(),
            "totalAmountMicros": t.string().optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "purchaseOrderNumber": t.string().optional(),
            "issueDate": t.string().optional(),
            "correctedInvoiceId": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "serviceStartDate": t.string().optional(),
            "subtotalAmountMicros": t.string().optional(),
            "id": t.string().optional(),
            "serviceEndDate": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "invoiceType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "dueDate": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceOut"])
    types["PlacementsGenerateTagsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "placementTags": t.array(t.proxy(renames["PlacementTagIn"])).optional(),
        }
    ).named(renames["PlacementsGenerateTagsResponseIn"])
    types["PlacementsGenerateTagsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "placementTags": t.array(t.proxy(renames["PlacementTagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementsGenerateTagsResponseOut"])
    types["BillingAssignmentIn"] = t.struct(
        {
            "campaignId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["BillingAssignmentIn"])
    types["BillingAssignmentOut"] = t.struct(
        {
            "campaignId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingAssignmentOut"])
    types["ConversionErrorIn"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ConversionErrorIn"])
    types["ConversionErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionErrorOut"])
    types["RecipientIn"] = t.struct(
        {
            "deliveryType": t.string().optional(),
            "email": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RecipientIn"])
    types["RecipientOut"] = t.struct(
        {
            "deliveryType": t.string().optional(),
            "email": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipientOut"])
    types["OmnitureSettingsIn"] = t.struct(
        {
            "omnitureIntegrationEnabled": t.boolean().optional(),
            "omnitureCostDataEnabled": t.boolean().optional(),
        }
    ).named(renames["OmnitureSettingsIn"])
    types["OmnitureSettingsOut"] = t.struct(
        {
            "omnitureIntegrationEnabled": t.boolean().optional(),
            "omnitureCostDataEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmnitureSettingsOut"])
    types["LanguageIn"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LanguageIn"])
    types["LanguageOut"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageOut"])
    types["ListPopulationTermIn"] = t.struct(
        {
            "remarketingListId": t.string().optional(),
            "type": t.string().optional(),
            "negation": t.boolean().optional(),
            "operator": t.string().optional(),
            "variableName": t.string().optional(),
            "contains": t.boolean().optional(),
            "value": t.string().optional(),
            "variableFriendlyName": t.string().optional(),
        }
    ).named(renames["ListPopulationTermIn"])
    types["ListPopulationTermOut"] = t.struct(
        {
            "remarketingListId": t.string().optional(),
            "type": t.string().optional(),
            "negation": t.boolean().optional(),
            "operator": t.string().optional(),
            "variableName": t.string().optional(),
            "contains": t.boolean().optional(),
            "value": t.string().optional(),
            "variableFriendlyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPopulationTermOut"])
    types["BrowserIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "browserVersionId": t.string().optional(),
            "name": t.string().optional(),
            "minorVersion": t.string().optional(),
            "dartId": t.string().optional(),
            "majorVersion": t.string().optional(),
        }
    ).named(renames["BrowserIn"])
    types["BrowserOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "browserVersionId": t.string().optional(),
            "name": t.string().optional(),
            "minorVersion": t.string().optional(),
            "dartId": t.string().optional(),
            "majorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserOut"])
    types["MeasurementPartnerWrappingDataIn"] = t.struct(
        {
            "measurementPartner": t.string().optional(),
            "tagWrappingMode": t.string().optional(),
            "linkStatus": t.string().optional(),
            "wrappedTag": t.string().optional(),
        }
    ).named(renames["MeasurementPartnerWrappingDataIn"])
    types["MeasurementPartnerWrappingDataOut"] = t.struct(
        {
            "measurementPartner": t.string().optional(),
            "tagWrappingMode": t.string().optional(),
            "linkStatus": t.string().optional(),
            "wrappedTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeasurementPartnerWrappingDataOut"])
    types["RuleIn"] = t.struct(
        {
            "assetId": t.string().optional(),
            "name": t.string().optional(),
            "targetingTemplateId": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "assetId": t.string().optional(),
            "name": t.string().optional(),
            "targetingTemplateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["FloodlightConfigurationIn"] = t.struct(
        {
            "tagSettings": t.proxy(renames["TagSettingsIn"]).optional(),
            "kind": t.string().optional(),
            "subaccountId": t.string().optional(),
            "naturalSearchConversionAttributionOption": t.string().optional(),
            "customViewabilityMetric": t.proxy(
                renames["CustomViewabilityMetricIn"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "advertiserId": t.string().optional(),
            "userDefinedVariableConfigurations": t.array(
                t.proxy(renames["UserDefinedVariableConfigurationIn"])
            ).optional(),
            "firstDayOfWeek": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "exposureToConversionEnabled": t.boolean().optional(),
            "thirdPartyAuthenticationTokens": t.array(
                t.proxy(renames["ThirdPartyAuthenticationTokenIn"])
            ).optional(),
            "analyticsDataSharingEnabled": t.boolean().optional(),
            "inAppAttributionTrackingEnabled": t.boolean().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationIn"]
            ).optional(),
            "omnitureSettings": t.proxy(renames["OmnitureSettingsIn"]).optional(),
        }
    ).named(renames["FloodlightConfigurationIn"])
    types["FloodlightConfigurationOut"] = t.struct(
        {
            "tagSettings": t.proxy(renames["TagSettingsOut"]).optional(),
            "kind": t.string().optional(),
            "subaccountId": t.string().optional(),
            "naturalSearchConversionAttributionOption": t.string().optional(),
            "customViewabilityMetric": t.proxy(
                renames["CustomViewabilityMetricOut"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "advertiserId": t.string().optional(),
            "userDefinedVariableConfigurations": t.array(
                t.proxy(renames["UserDefinedVariableConfigurationOut"])
            ).optional(),
            "firstDayOfWeek": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "exposureToConversionEnabled": t.boolean().optional(),
            "thirdPartyAuthenticationTokens": t.array(
                t.proxy(renames["ThirdPartyAuthenticationTokenOut"])
            ).optional(),
            "analyticsDataSharingEnabled": t.boolean().optional(),
            "inAppAttributionTrackingEnabled": t.boolean().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationOut"]
            ).optional(),
            "omnitureSettings": t.proxy(renames["OmnitureSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightConfigurationOut"])
    types["SiteSkippableSettingIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "skippable": t.boolean().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
            "progressOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
        }
    ).named(renames["SiteSkippableSettingIn"])
    types["SiteSkippableSettingOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "skippable": t.boolean().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "progressOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteSkippableSettingOut"])
    types["CompatibleFieldsIn"] = t.struct(
        {
            "floodlightReportCompatibleFields": t.proxy(
                renames["FloodlightReportCompatibleFieldsIn"]
            ).optional(),
            "crossDimensionReachReportCompatibleFields": t.proxy(
                renames["CrossDimensionReachReportCompatibleFieldsIn"]
            ).optional(),
            "reachReportCompatibleFields": t.proxy(
                renames["ReachReportCompatibleFieldsIn"]
            ).optional(),
            "pathAttributionReportCompatibleFields": t.proxy(
                renames["PathReportCompatibleFieldsIn"]
            ).optional(),
            "reportCompatibleFields": t.proxy(
                renames["ReportCompatibleFieldsIn"]
            ).optional(),
            "kind": t.string().optional(),
            "pathToConversionReportCompatibleFields": t.proxy(
                renames["PathToConversionReportCompatibleFieldsIn"]
            ).optional(),
            "pathReportCompatibleFields": t.proxy(
                renames["PathReportCompatibleFieldsIn"]
            ).optional(),
        }
    ).named(renames["CompatibleFieldsIn"])
    types["CompatibleFieldsOut"] = t.struct(
        {
            "floodlightReportCompatibleFields": t.proxy(
                renames["FloodlightReportCompatibleFieldsOut"]
            ).optional(),
            "crossDimensionReachReportCompatibleFields": t.proxy(
                renames["CrossDimensionReachReportCompatibleFieldsOut"]
            ).optional(),
            "reachReportCompatibleFields": t.proxy(
                renames["ReachReportCompatibleFieldsOut"]
            ).optional(),
            "pathAttributionReportCompatibleFields": t.proxy(
                renames["PathReportCompatibleFieldsOut"]
            ).optional(),
            "reportCompatibleFields": t.proxy(
                renames["ReportCompatibleFieldsOut"]
            ).optional(),
            "kind": t.string().optional(),
            "pathToConversionReportCompatibleFields": t.proxy(
                renames["PathToConversionReportCompatibleFieldsOut"]
            ).optional(),
            "pathReportCompatibleFields": t.proxy(
                renames["PathReportCompatibleFieldsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompatibleFieldsOut"])
    types["OperatingSystemVersionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "operatingSystem": t.proxy(renames["OperatingSystemIn"]).optional(),
            "minorVersion": t.string().optional(),
            "majorVersion": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperatingSystemVersionIn"])
    types["OperatingSystemVersionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "operatingSystem": t.proxy(renames["OperatingSystemOut"]).optional(),
            "minorVersion": t.string().optional(),
            "majorVersion": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemVersionOut"])
    types["CreativeAssetMetadataIn"] = t.struct(
        {
            "clickTags": t.array(t.proxy(renames["ClickTagIn"])).optional(),
            "kind": t.string().optional(),
            "warnedValidationRules": t.array(t.string()).optional(),
            "richMedia": t.boolean().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "id": t.string().optional(),
            "exitCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "timerCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "detectedFeatures": t.array(t.string()).optional(),
            "assetIdentifier": t.proxy(renames["CreativeAssetIdIn"]).optional(),
            "counterCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
        }
    ).named(renames["CreativeAssetMetadataIn"])
    types["CreativeAssetMetadataOut"] = t.struct(
        {
            "clickTags": t.array(t.proxy(renames["ClickTagOut"])).optional(),
            "kind": t.string().optional(),
            "warnedValidationRules": t.array(t.string()).optional(),
            "richMedia": t.boolean().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "id": t.string().optional(),
            "exitCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "timerCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "detectedFeatures": t.array(t.string()).optional(),
            "assetIdentifier": t.proxy(renames["CreativeAssetIdOut"]).optional(),
            "counterCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeAssetMetadataOut"])
    types["ChangeLogsListResponseIn"] = t.struct(
        {
            "changeLogs": t.array(t.proxy(renames["ChangeLogIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ChangeLogsListResponseIn"])
    types["ChangeLogsListResponseOut"] = t.struct(
        {
            "changeLogs": t.array(t.proxy(renames["ChangeLogOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeLogsListResponseOut"])
    types["OfflineUserAddressInfoIn"] = t.struct(
        {
            "city": t.string().optional(),
            "countryCode": t.string().optional(),
            "hashedStreetAddress": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "hashedFirstName": t.string().optional(),
            "postalCode": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["OfflineUserAddressInfoIn"])
    types["OfflineUserAddressInfoOut"] = t.struct(
        {
            "city": t.string().optional(),
            "countryCode": t.string().optional(),
            "hashedStreetAddress": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "hashedFirstName": t.string().optional(),
            "postalCode": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfflineUserAddressInfoOut"])
    types["PlacementTagIn"] = t.struct(
        {
            "placementId": t.string().optional(),
            "tagDatas": t.array(t.proxy(renames["TagDataIn"])).optional(),
        }
    ).named(renames["PlacementTagIn"])
    types["PlacementTagOut"] = t.struct(
        {
            "placementId": t.string().optional(),
            "tagDatas": t.array(t.proxy(renames["TagDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementTagOut"])
    types["AccountUserProfileIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "userAccessType": t.string().optional(),
            "subaccountId": t.string().optional(),
            "campaignFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
            "kind": t.string().optional(),
            "email": t.string().optional(),
            "userRoleId": t.string().optional(),
            "siteFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
            "traffickerType": t.string().optional(),
            "id": t.string().optional(),
            "comments": t.string().optional(),
            "active": t.boolean().optional(),
            "userRoleFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
            "locale": t.string().optional(),
            "advertiserFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
        }
    ).named(renames["AccountUserProfileIn"])
    types["AccountUserProfileOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "userAccessType": t.string().optional(),
            "subaccountId": t.string().optional(),
            "campaignFilter": t.proxy(renames["ObjectFilterOut"]).optional(),
            "kind": t.string().optional(),
            "email": t.string().optional(),
            "userRoleId": t.string().optional(),
            "siteFilter": t.proxy(renames["ObjectFilterOut"]).optional(),
            "traffickerType": t.string().optional(),
            "id": t.string().optional(),
            "comments": t.string().optional(),
            "active": t.boolean().optional(),
            "userRoleFilter": t.proxy(renames["ObjectFilterOut"]).optional(),
            "locale": t.string().optional(),
            "advertiserFilter": t.proxy(renames["ObjectFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountUserProfileOut"])
    types["UserIdentifierIn"] = t.struct(
        {
            "hashedEmail": t.string().optional(),
            "addressInfo": t.proxy(renames["OfflineUserAddressInfoIn"]).optional(),
            "hashedPhoneNumber": t.string().optional(),
        }
    ).named(renames["UserIdentifierIn"])
    types["UserIdentifierOut"] = t.struct(
        {
            "hashedEmail": t.string().optional(),
            "addressInfo": t.proxy(renames["OfflineUserAddressInfoOut"]).optional(),
            "hashedPhoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserIdentifierOut"])
    types["VideoSettingsIn"] = t.struct(
        {
            "publisherSpecificationId": t.string().optional(),
            "orientation": t.string().optional(),
            "companionSettings": t.proxy(renames["CompanionSettingIn"]).optional(),
            "skippableSettings": t.proxy(renames["SkippableSettingIn"]).optional(),
            "transcodeSettings": t.proxy(renames["TranscodeSettingIn"]).optional(),
            "obaEnabled": t.boolean().optional(),
            "obaSettings": t.proxy(renames["ObaIconIn"]).optional(),
            "kind": t.string().optional(),
            "durationSeconds": t.integer().optional(),
        }
    ).named(renames["VideoSettingsIn"])
    types["VideoSettingsOut"] = t.struct(
        {
            "publisherSpecificationId": t.string().optional(),
            "orientation": t.string().optional(),
            "companionSettings": t.proxy(renames["CompanionSettingOut"]).optional(),
            "skippableSettings": t.proxy(renames["SkippableSettingOut"]).optional(),
            "transcodeSettings": t.proxy(renames["TranscodeSettingOut"]).optional(),
            "obaEnabled": t.boolean().optional(),
            "obaSettings": t.proxy(renames["ObaIconOut"]).optional(),
            "kind": t.string().optional(),
            "durationSeconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoSettingsOut"])
    types["CompanionClickThroughOverrideIn"] = t.struct(
        {
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
            "creativeId": t.string().optional(),
        }
    ).named(renames["CompanionClickThroughOverrideIn"])
    types["CompanionClickThroughOverrideOut"] = t.struct(
        {
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlOut"]).optional(),
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanionClickThroughOverrideOut"])
    types["MetricIn"] = t.struct(
        {"name": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["AdvertisersListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "advertisers": t.array(t.proxy(renames["AdvertiserIn"])).optional(),
        }
    ).named(renames["AdvertisersListResponseIn"])
    types["AdvertisersListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "advertisers": t.array(t.proxy(renames["AdvertiserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertisersListResponseOut"])
    types["KeyValueTargetingExpressionIn"] = t.struct(
        {"expression": t.string().optional()}
    ).named(renames["KeyValueTargetingExpressionIn"])
    types["KeyValueTargetingExpressionOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueTargetingExpressionOut"])
    types["UserRolePermissionGroupsListResponseIn"] = t.struct(
        {
            "userRolePermissionGroups": t.array(
                t.proxy(renames["UserRolePermissionGroupIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UserRolePermissionGroupsListResponseIn"])
    types["UserRolePermissionGroupsListResponseOut"] = t.struct(
        {
            "userRolePermissionGroups": t.array(
                t.proxy(renames["UserRolePermissionGroupOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRolePermissionGroupsListResponseOut"])
    types["TechnologyTargetingIn"] = t.struct(
        {
            "operatingSystems": t.array(
                t.proxy(renames["OperatingSystemIn"])
            ).optional(),
            "mobileCarriers": t.array(t.proxy(renames["MobileCarrierIn"])).optional(),
            "browsers": t.array(t.proxy(renames["BrowserIn"])).optional(),
            "operatingSystemVersions": t.array(
                t.proxy(renames["OperatingSystemVersionIn"])
            ).optional(),
            "platformTypes": t.array(t.proxy(renames["PlatformTypeIn"])).optional(),
            "connectionTypes": t.array(t.proxy(renames["ConnectionTypeIn"])).optional(),
        }
    ).named(renames["TechnologyTargetingIn"])
    types["TechnologyTargetingOut"] = t.struct(
        {
            "operatingSystems": t.array(
                t.proxy(renames["OperatingSystemOut"])
            ).optional(),
            "mobileCarriers": t.array(t.proxy(renames["MobileCarrierOut"])).optional(),
            "browsers": t.array(t.proxy(renames["BrowserOut"])).optional(),
            "operatingSystemVersions": t.array(
                t.proxy(renames["OperatingSystemVersionOut"])
            ).optional(),
            "platformTypes": t.array(t.proxy(renames["PlatformTypeOut"])).optional(),
            "connectionTypes": t.array(
                t.proxy(renames["ConnectionTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TechnologyTargetingOut"])
    types["ConversionsBatchUpdateRequestIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoIn"]).optional(),
            "conversions": t.array(t.proxy(renames["ConversionIn"])).optional(),
        }
    ).named(renames["ConversionsBatchUpdateRequestIn"])
    types["ConversionsBatchUpdateRequestOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "conversions": t.array(t.proxy(renames["ConversionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionsBatchUpdateRequestOut"])
    types["OperatingSystemsListResponseIn"] = t.struct(
        {
            "operatingSystems": t.array(
                t.proxy(renames["OperatingSystemIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OperatingSystemsListResponseIn"])
    types["OperatingSystemsListResponseOut"] = t.struct(
        {
            "operatingSystems": t.array(
                t.proxy(renames["OperatingSystemOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemsListResponseOut"])
    types["FloodlightActivityIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "attributionEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "floodlightActivityGroupTagString": t.string().optional(),
            "floodlightTagType": t.string().optional(),
            "countingMethod": t.string().optional(),
            "status": t.string().optional(),
            "defaultTags": t.array(
                t.proxy(renames["FloodlightActivityDynamicTagIn"])
            ).optional(),
            "cacheBustingType": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "expectedUrl": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "floodlightActivityGroupName": t.string().optional(),
            "secure": t.boolean().optional(),
            "tagFormat": t.string().optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "id": t.string().optional(),
            "sslRequired": t.boolean().optional(),
            "floodlightActivityGroupId": t.string().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "floodlightActivityGroupType": t.string().optional(),
            "advertiserId": t.string().optional(),
            "tagString": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "publisherTags": t.array(
                t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
            ).optional(),
            "userDefinedVariableTypes": t.array(t.string()).optional(),
        }
    ).named(renames["FloodlightActivityIn"])
    types["FloodlightActivityOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "attributionEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "floodlightActivityGroupTagString": t.string().optional(),
            "floodlightTagType": t.string().optional(),
            "countingMethod": t.string().optional(),
            "status": t.string().optional(),
            "defaultTags": t.array(
                t.proxy(renames["FloodlightActivityDynamicTagOut"])
            ).optional(),
            "cacheBustingType": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "expectedUrl": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "floodlightActivityGroupName": t.string().optional(),
            "secure": t.boolean().optional(),
            "tagFormat": t.string().optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "id": t.string().optional(),
            "sslRequired": t.boolean().optional(),
            "floodlightActivityGroupId": t.string().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "floodlightActivityGroupType": t.string().optional(),
            "advertiserId": t.string().optional(),
            "tagString": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "publisherTags": t.array(
                t.proxy(renames["FloodlightActivityPublisherDynamicTagOut"])
            ).optional(),
            "userDefinedVariableTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivityOut"])
    types["ReportIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "criteria": t.struct(
                {
                    "customRichMediaEvents": t.proxy(
                        renames["CustomRichMediaEventsIn"]
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "name": t.string().optional(),
            "fileName": t.string().optional(),
            "subAccountId": t.string().optional(),
            "pathCriteria": t.struct(
                {
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueIn"]
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "customChannelGrouping": t.proxy(
                        renames["ChannelGroupingIn"]
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "pathFilters": t.array(t.proxy(renames["PathFilterIn"])).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                }
            ).optional(),
            "floodlightCriteria": t.struct(
                {
                    "reportProperties": t.struct(
                        {
                            "includeUnattributedCookieConversions": t.boolean().optional(),
                            "includeAttributedIPConversions": t.boolean().optional(),
                            "includeUnattributedIPConversions": t.boolean().optional(),
                        }
                    ).optional(),
                    "customRichMediaEvents": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueIn"]
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "type": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "pathAttributionCriteria": t.struct(
                {
                    "metricNames": t.array(t.string()).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "customChannelGrouping": t.proxy(
                        renames["ChannelGroupingIn"]
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "pathFilters": t.array(t.proxy(renames["PathFilterIn"])).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueIn"]
                    ).optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "pathToConversionCriteria": t.struct(
                {
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueIn"]
                    ).optional(),
                    "conversionDimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "customFloodlightVariables": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "customRichMediaEvents": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "reportProperties": t.struct(
                        {
                            "includeUnattributedIPConversions": t.boolean().optional(),
                            "maximumClickInteractions": t.integer().optional(),
                            "includeAttributedIPConversions": t.boolean().optional(),
                            "impressionsLookbackWindow": t.integer().optional(),
                            "maximumImpressionInteractions": t.integer().optional(),
                            "maximumInteractionGap": t.integer().optional(),
                            "includeUnattributedCookieConversions": t.boolean().optional(),
                            "clicksLookbackWindow": t.integer().optional(),
                            "pivotOnInteractionPath": t.boolean().optional(),
                        }
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "perInteractionDimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                }
            ).optional(),
            "crossDimensionReachCriteria": t.struct(
                {
                    "overlapMetricNames": t.array(t.string()).optional(),
                    "dimension": t.string().optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "pivoted": t.boolean().optional(),
                    "breakdown": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "ownerProfileId": t.string().optional(),
            "reachCriteria": t.struct(
                {
                    "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                    "enableAllDimensionCombinations": t.boolean().optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "customRichMediaEvents": t.proxy(
                        renames["CustomRichMediaEventsIn"]
                    ).optional(),
                    "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                }
            ).optional(),
            "schedule": t.struct(
                {
                    "active": t.boolean().optional(),
                    "startDate": t.string(),
                    "expirationDate": t.string(),
                    "every": t.integer().optional(),
                    "repeats": t.string().optional(),
                    "timezone": t.string().optional(),
                    "repeatsOnWeekDays": t.array(t.string()).optional(),
                    "runsOnDayOfMonth": t.string().optional(),
                }
            ).optional(),
            "delivery": t.struct(
                {
                    "recipients": t.array(t.proxy(renames["RecipientIn"])).optional(),
                    "message": t.string().optional(),
                    "emailOwnerDeliveryType": t.string().optional(),
                    "emailOwner": t.boolean().optional(),
                }
            ).optional(),
            "format": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "criteria": t.struct(
                {
                    "customRichMediaEvents": t.proxy(
                        renames["CustomRichMediaEventsOut"]
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "activities": t.proxy(renames["ActivitiesOut"]).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "name": t.string().optional(),
            "fileName": t.string().optional(),
            "subAccountId": t.string().optional(),
            "pathCriteria": t.struct(
                {
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueOut"]
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "customChannelGrouping": t.proxy(
                        renames["ChannelGroupingOut"]
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "pathFilters": t.array(
                        t.proxy(renames["PathFilterOut"])
                    ).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                }
            ).optional(),
            "floodlightCriteria": t.struct(
                {
                    "reportProperties": t.struct(
                        {
                            "includeUnattributedCookieConversions": t.boolean().optional(),
                            "includeAttributedIPConversions": t.boolean().optional(),
                            "includeUnattributedIPConversions": t.boolean().optional(),
                        }
                    ).optional(),
                    "customRichMediaEvents": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueOut"]
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "type": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "pathAttributionCriteria": t.struct(
                {
                    "metricNames": t.array(t.string()).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "customChannelGrouping": t.proxy(
                        renames["ChannelGroupingOut"]
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "pathFilters": t.array(
                        t.proxy(renames["PathFilterOut"])
                    ).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueOut"]
                    ).optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "pathToConversionCriteria": t.struct(
                {
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueOut"]
                    ).optional(),
                    "conversionDimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "customFloodlightVariables": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "customRichMediaEvents": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "reportProperties": t.struct(
                        {
                            "includeUnattributedIPConversions": t.boolean().optional(),
                            "maximumClickInteractions": t.integer().optional(),
                            "includeAttributedIPConversions": t.boolean().optional(),
                            "impressionsLookbackWindow": t.integer().optional(),
                            "maximumImpressionInteractions": t.integer().optional(),
                            "maximumInteractionGap": t.integer().optional(),
                            "includeUnattributedCookieConversions": t.boolean().optional(),
                            "clicksLookbackWindow": t.integer().optional(),
                            "pivotOnInteractionPath": t.boolean().optional(),
                        }
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "perInteractionDimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                }
            ).optional(),
            "crossDimensionReachCriteria": t.struct(
                {
                    "overlapMetricNames": t.array(t.string()).optional(),
                    "dimension": t.string().optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "pivoted": t.boolean().optional(),
                    "breakdown": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "ownerProfileId": t.string().optional(),
            "reachCriteria": t.struct(
                {
                    "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                    "enableAllDimensionCombinations": t.boolean().optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "customRichMediaEvents": t.proxy(
                        renames["CustomRichMediaEventsOut"]
                    ).optional(),
                    "activities": t.proxy(renames["ActivitiesOut"]).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                }
            ).optional(),
            "schedule": t.struct(
                {
                    "active": t.boolean().optional(),
                    "startDate": t.string(),
                    "expirationDate": t.string(),
                    "every": t.integer().optional(),
                    "repeats": t.string().optional(),
                    "timezone": t.string().optional(),
                    "repeatsOnWeekDays": t.array(t.string()).optional(),
                    "runsOnDayOfMonth": t.string().optional(),
                }
            ).optional(),
            "delivery": t.struct(
                {
                    "recipients": t.array(t.proxy(renames["RecipientOut"])).optional(),
                    "message": t.string().optional(),
                    "emailOwnerDeliveryType": t.string().optional(),
                    "emailOwner": t.boolean().optional(),
                }
            ).optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["EventTagsListResponseIn"] = t.struct(
        {
            "eventTags": t.array(t.proxy(renames["EventTagIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["EventTagsListResponseIn"])
    types["EventTagsListResponseOut"] = t.struct(
        {
            "eventTags": t.array(t.proxy(renames["EventTagOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTagsListResponseOut"])
    types["PricingScheduleIn"] = t.struct(
        {
            "floodlightActivityId": t.string().optional(),
            "endDate": t.string(),
            "flighted": t.boolean().optional(),
            "pricingType": t.string().optional(),
            "pricingPeriods": t.array(
                t.proxy(renames["PricingSchedulePricingPeriodIn"])
            ).optional(),
            "capCostOption": t.string().optional(),
            "startDate": t.string(),
            "testingStartDate": t.string(),
        }
    ).named(renames["PricingScheduleIn"])
    types["PricingScheduleOut"] = t.struct(
        {
            "floodlightActivityId": t.string().optional(),
            "endDate": t.string(),
            "flighted": t.boolean().optional(),
            "pricingType": t.string().optional(),
            "pricingPeriods": t.array(
                t.proxy(renames["PricingSchedulePricingPeriodOut"])
            ).optional(),
            "capCostOption": t.string().optional(),
            "startDate": t.string(),
            "testingStartDate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingScheduleOut"])
    types["MobileCarrierIn"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "countryDartId": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["MobileCarrierIn"])
    types["MobileCarrierOut"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "countryDartId": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileCarrierOut"])
    types["InventoryItemsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inventoryItems": t.array(t.proxy(renames["InventoryItemIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["InventoryItemsListResponseIn"])
    types["InventoryItemsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inventoryItems": t.array(t.proxy(renames["InventoryItemOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryItemsListResponseOut"])
    types["OptimizationActivityIn"] = t.struct(
        {
            "floodlightActivityId": t.string().optional(),
            "floodlightActivityIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "weight": t.integer().optional(),
        }
    ).named(renames["OptimizationActivityIn"])
    types["OptimizationActivityOut"] = t.struct(
        {
            "floodlightActivityId": t.string().optional(),
            "floodlightActivityIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptimizationActivityOut"])
    types["SiteSettingsIn"] = t.struct(
        {
            "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
            "activeViewOptOut": t.boolean().optional(),
            "vpaidAdapterChoiceTemplate": t.string().optional(),
            "disableNewCookie": t.boolean().optional(),
            "adBlockingOptOut": t.boolean().optional(),
            "videoActiveViewOptOutTemplate": t.boolean().optional(),
        }
    ).named(renames["SiteSettingsIn"])
    types["SiteSettingsOut"] = t.struct(
        {
            "tagSetting": t.proxy(renames["TagSettingOut"]).optional(),
            "activeViewOptOut": t.boolean().optional(),
            "vpaidAdapterChoiceTemplate": t.string().optional(),
            "disableNewCookie": t.boolean().optional(),
            "adBlockingOptOut": t.boolean().optional(),
            "videoActiveViewOptOutTemplate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteSettingsOut"])
    types["TargetableRemarketingListIn"] = t.struct(
        {
            "lifeSpan": t.string().optional(),
            "subaccountId": t.string().optional(),
            "listSource": t.string().optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "listSize": t.string().optional(),
            "description": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "active": t.boolean().optional(),
        }
    ).named(renames["TargetableRemarketingListIn"])
    types["TargetableRemarketingListOut"] = t.struct(
        {
            "lifeSpan": t.string().optional(),
            "subaccountId": t.string().optional(),
            "listSource": t.string().optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "listSize": t.string().optional(),
            "description": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "active": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetableRemarketingListOut"])
    types["PlacementStrategyIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PlacementStrategyIn"])
    types["PlacementStrategyOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementStrategyOut"])
    types["ProjectIn"] = t.struct(
        {
            "clientName": t.string().optional(),
            "targetCpaNanos": t.string().optional(),
            "targetCpmNanos": t.string().optional(),
            "startDate": t.string(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "subaccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "budget": t.string().optional(),
            "targetImpressions": t.string().optional(),
            "id": t.string().optional(),
            "endDate": t.string(),
            "targetCpmActiveViewNanos": t.string().optional(),
            "overview": t.string().optional(),
            "audienceGender": t.string().optional(),
            "audienceAgeGroup": t.string().optional(),
            "advertiserId": t.string().optional(),
            "clientBillingCode": t.string().optional(),
            "targetConversions": t.string().optional(),
            "targetCpcNanos": t.string().optional(),
            "targetClicks": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "clientName": t.string().optional(),
            "targetCpaNanos": t.string().optional(),
            "targetCpmNanos": t.string().optional(),
            "startDate": t.string(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "subaccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "budget": t.string().optional(),
            "targetImpressions": t.string().optional(),
            "id": t.string().optional(),
            "endDate": t.string(),
            "targetCpmActiveViewNanos": t.string().optional(),
            "overview": t.string().optional(),
            "audienceGender": t.string().optional(),
            "audienceAgeGroup": t.string().optional(),
            "advertiserId": t.string().optional(),
            "clientBillingCode": t.string().optional(),
            "targetConversions": t.string().optional(),
            "targetCpcNanos": t.string().optional(),
            "targetClicks": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["ContentCategoryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ContentCategoryIn"])
    types["ContentCategoryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentCategoryOut"])
    types["OrderIn"] = t.struct(
        {
            "buyerOrganizationName": t.string().optional(),
            "kind": t.string().optional(),
            "comments": t.string().optional(),
            "id": t.string().optional(),
            "siteNames": t.array(t.string()).optional(),
            "sellerOrganizationName": t.string().optional(),
            "name": t.string().optional(),
            "planningTermId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "buyerInvoiceId": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "notes": t.string().optional(),
            "sellerOrderId": t.string().optional(),
            "accountId": t.string().optional(),
            "termsAndConditions": t.string().optional(),
            "projectId": t.string().optional(),
            "contacts": t.array(t.proxy(renames["OrderContactIn"])).optional(),
            "siteId": t.array(t.string()).optional(),
            "approverUserProfileIds": t.array(t.string()).optional(),
        }
    ).named(renames["OrderIn"])
    types["OrderOut"] = t.struct(
        {
            "buyerOrganizationName": t.string().optional(),
            "kind": t.string().optional(),
            "comments": t.string().optional(),
            "id": t.string().optional(),
            "siteNames": t.array(t.string()).optional(),
            "sellerOrganizationName": t.string().optional(),
            "name": t.string().optional(),
            "planningTermId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "buyerInvoiceId": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "notes": t.string().optional(),
            "sellerOrderId": t.string().optional(),
            "accountId": t.string().optional(),
            "termsAndConditions": t.string().optional(),
            "projectId": t.string().optional(),
            "contacts": t.array(t.proxy(renames["OrderContactOut"])).optional(),
            "siteId": t.array(t.string()).optional(),
            "approverUserProfileIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderOut"])
    types["CreativeClickThroughUrlIn"] = t.struct(
        {
            "landingPageId": t.string().optional(),
            "customClickThroughUrl": t.string().optional(),
            "computedClickThroughUrl": t.string().optional(),
        }
    ).named(renames["CreativeClickThroughUrlIn"])
    types["CreativeClickThroughUrlOut"] = t.struct(
        {
            "landingPageId": t.string().optional(),
            "customClickThroughUrl": t.string().optional(),
            "computedClickThroughUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeClickThroughUrlOut"])
    types["BillingAssignmentsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "billingAssignments": t.array(
                t.proxy(renames["BillingAssignmentIn"])
            ).optional(),
        }
    ).named(renames["BillingAssignmentsListResponseIn"])
    types["BillingAssignmentsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "billingAssignments": t.array(
                t.proxy(renames["BillingAssignmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingAssignmentsListResponseOut"])
    types["TargetingTemplateIn"] = t.struct(
        {
            "listTargetingExpression": t.proxy(
                renames["ListTargetingExpressionIn"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "technologyTargeting": t.proxy(renames["TechnologyTargetingIn"]).optional(),
            "id": t.string().optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
            "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
            "keyValueTargetingExpression": t.proxy(
                renames["KeyValueTargetingExpressionIn"]
            ).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["TargetingTemplateIn"])
    types["TargetingTemplateOut"] = t.struct(
        {
            "listTargetingExpression": t.proxy(
                renames["ListTargetingExpressionOut"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "id": t.string().optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingOut"]).optional(),
            "geoTargeting": t.proxy(renames["GeoTargetingOut"]).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "dayPartTargeting": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "keyValueTargetingExpression": t.proxy(
                renames["KeyValueTargetingExpressionOut"]
            ).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingTemplateOut"])
    types["MeasurementPartnerCampaignLinkIn"] = t.struct(
        {
            "linkStatus": t.string().optional(),
            "partnerCampaignId": t.string().optional(),
            "measurementPartner": t.string().optional(),
        }
    ).named(renames["MeasurementPartnerCampaignLinkIn"])
    types["MeasurementPartnerCampaignLinkOut"] = t.struct(
        {
            "linkStatus": t.string().optional(),
            "partnerCampaignId": t.string().optional(),
            "measurementPartner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeasurementPartnerCampaignLinkOut"])
    types["FileListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["FileIn"])).optional(),
        }
    ).named(renames["FileListIn"])
    types["FileListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["FileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileListOut"])
    types["FloodlightActivityGroupIn"] = t.struct(
        {
            "type": t.string().optional(),
            "tagString": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "floodlightConfigurationId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["FloodlightActivityGroupIn"])
    types["FloodlightActivityGroupOut"] = t.struct(
        {
            "type": t.string().optional(),
            "tagString": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "floodlightConfigurationId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivityGroupOut"])
    types["TargetWindowIn"] = t.struct(
        {
            "customHtml": t.string().optional(),
            "targetWindowOption": t.string().optional(),
        }
    ).named(renames["TargetWindowIn"])
    types["TargetWindowOut"] = t.struct(
        {
            "customHtml": t.string().optional(),
            "targetWindowOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetWindowOut"])
    types["LanguagesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "languages": t.array(t.proxy(renames["LanguageIn"])).optional(),
        }
    ).named(renames["LanguagesListResponseIn"])
    types["LanguagesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "languages": t.array(t.proxy(renames["LanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguagesListResponseOut"])
    types["LookbackConfigurationIn"] = t.struct(
        {
            "postImpressionActivitiesDuration": t.integer().optional(),
            "clickDuration": t.integer().optional(),
        }
    ).named(renames["LookbackConfigurationIn"])
    types["LookbackConfigurationOut"] = t.struct(
        {
            "postImpressionActivitiesDuration": t.integer().optional(),
            "clickDuration": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookbackConfigurationOut"])
    types["PlacementGroupIn"] = t.struct(
        {
            "childPlacementIds": t.array(t.string()).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "primaryPlacementIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "kind": t.string().optional(),
            "campaignIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "advertiserId": t.string().optional(),
            "siteId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "directorySiteId": t.string().optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "activeStatus": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "name": t.string().optional(),
            "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
            "externalId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "accountId": t.string().optional(),
            "campaignId": t.string().optional(),
            "comment": t.string().optional(),
            "primaryPlacementId": t.string().optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "placementGroupType": t.string().optional(),
            "contentCategoryId": t.string().optional(),
        }
    ).named(renames["PlacementGroupIn"])
    types["PlacementGroupOut"] = t.struct(
        {
            "childPlacementIds": t.array(t.string()).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "primaryPlacementIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "kind": t.string().optional(),
            "campaignIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "siteId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "directorySiteId": t.string().optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "activeStatus": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "name": t.string().optional(),
            "pricingSchedule": t.proxy(renames["PricingScheduleOut"]).optional(),
            "externalId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "accountId": t.string().optional(),
            "campaignId": t.string().optional(),
            "comment": t.string().optional(),
            "primaryPlacementId": t.string().optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "placementGroupType": t.string().optional(),
            "contentCategoryId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementGroupOut"])
    types["ContentCategoriesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "contentCategories": t.array(
                t.proxy(renames["ContentCategoryIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ContentCategoriesListResponseIn"])
    types["ContentCategoriesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "contentCategories": t.array(
                t.proxy(renames["ContentCategoryOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentCategoriesListResponseOut"])
    types["DimensionValueRequestIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "filters": t.array(t.proxy(renames["DimensionFilterIn"])).optional(),
            "startDate": t.string(),
            "endDate": t.string(),
            "dimensionName": t.string().optional(),
        }
    ).named(renames["DimensionValueRequestIn"])
    types["DimensionValueRequestOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "filters": t.array(t.proxy(renames["DimensionFilterOut"])).optional(),
            "startDate": t.string(),
            "endDate": t.string(),
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueRequestOut"])
    types["CrossDimensionReachReportCompatibleFieldsIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "overlapMetrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "breakdown": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CrossDimensionReachReportCompatibleFieldsIn"])
    types["CrossDimensionReachReportCompatibleFieldsOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "overlapMetrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "breakdown": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrossDimensionReachReportCompatibleFieldsOut"])
    types["FloodlightActivityGroupsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "floodlightActivityGroups": t.array(
                t.proxy(renames["FloodlightActivityGroupIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["FloodlightActivityGroupsListResponseIn"])
    types["FloodlightActivityGroupsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "floodlightActivityGroups": t.array(
                t.proxy(renames["FloodlightActivityGroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivityGroupsListResponseOut"])
    types["SizeIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "iab": t.boolean().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["SizeIn"])
    types["SizeOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "iab": t.boolean().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SizeOut"])
    types["LanguageTargetingIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["LanguageIn"])).optional()}
    ).named(renames["LanguageTargetingIn"])
    types["LanguageTargetingOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["LanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageTargetingOut"])
    types["AccountPermissionsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountPermissions": t.array(
                t.proxy(renames["AccountPermissionIn"])
            ).optional(),
        }
    ).named(renames["AccountPermissionsListResponseIn"])
    types["AccountPermissionsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountPermissions": t.array(
                t.proxy(renames["AccountPermissionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountPermissionsListResponseOut"])
    types["DeepLinkIn"] = t.struct(
        {
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
            "remarketingListIds": t.array(t.string()).optional(),
            "fallbackUrl": t.string().optional(),
            "kind": t.string().optional(),
            "appUrl": t.string().optional(),
        }
    ).named(renames["DeepLinkIn"])
    types["DeepLinkOut"] = t.struct(
        {
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "remarketingListIds": t.array(t.string()).optional(),
            "fallbackUrl": t.string().optional(),
            "kind": t.string().optional(),
            "appUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeepLinkOut"])
    types["AudienceSegmentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "allocation": t.integer().optional(),
        }
    ).named(renames["AudienceSegmentIn"])
    types["AudienceSegmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "allocation": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudienceSegmentOut"])
    types["VideoFormatsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "videoFormats": t.array(t.proxy(renames["VideoFormatIn"])).optional(),
        }
    ).named(renames["VideoFormatsListResponseIn"])
    types["VideoFormatsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "videoFormats": t.array(t.proxy(renames["VideoFormatOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFormatsListResponseOut"])
    types["DimensionFilterIn"] = t.struct(
        {
            "value": t.string().optional(),
            "dimensionName": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DimensionFilterIn"])
    types["DimensionFilterOut"] = t.struct(
        {
            "value": t.string().optional(),
            "dimensionName": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionFilterOut"])
    types["FloodlightActivitiesGenerateTagResponseIn"] = t.struct(
        {
            "floodlightActivityTag": t.string().optional(),
            "kind": t.string().optional(),
            "globalSiteTagGlobalSnippet": t.string().optional(),
        }
    ).named(renames["FloodlightActivitiesGenerateTagResponseIn"])
    types["FloodlightActivitiesGenerateTagResponseOut"] = t.struct(
        {
            "floodlightActivityTag": t.string().optional(),
            "kind": t.string().optional(),
            "globalSiteTagGlobalSnippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivitiesGenerateTagResponseOut"])
    types["DfpSettingsIn"] = t.struct(
        {
            "dfpNetworkCode": t.string().optional(),
            "programmaticPlacementAccepted": t.boolean().optional(),
            "publisherPortalOnly": t.boolean().optional(),
            "pubPaidPlacementAccepted": t.boolean().optional(),
            "dfpNetworkName": t.string().optional(),
        }
    ).named(renames["DfpSettingsIn"])
    types["DfpSettingsOut"] = t.struct(
        {
            "dfpNetworkCode": t.string().optional(),
            "programmaticPlacementAccepted": t.boolean().optional(),
            "publisherPortalOnly": t.boolean().optional(),
            "pubPaidPlacementAccepted": t.boolean().optional(),
            "dfpNetworkName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DfpSettingsOut"])
    types["RemarketingListIn"] = t.struct(
        {
            "description": t.string().optional(),
            "listSize": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "lifeSpan": t.string().optional(),
            "active": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "listPopulationRule": t.proxy(renames["ListPopulationRuleIn"]).optional(),
            "listSource": t.string().optional(),
        }
    ).named(renames["RemarketingListIn"])
    types["RemarketingListOut"] = t.struct(
        {
            "description": t.string().optional(),
            "listSize": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "lifeSpan": t.string().optional(),
            "active": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "listPopulationRule": t.proxy(renames["ListPopulationRuleOut"]).optional(),
            "listSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingListOut"])
    types["AccountUserProfilesListResponseIn"] = t.struct(
        {
            "accountUserProfiles": t.array(
                t.proxy(renames["AccountUserProfileIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountUserProfilesListResponseIn"])
    types["AccountUserProfilesListResponseOut"] = t.struct(
        {
            "accountUserProfiles": t.array(
                t.proxy(renames["AccountUserProfileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountUserProfilesListResponseOut"])
    types["ClickThroughUrlIn"] = t.struct(
        {
            "defaultLandingPage": t.boolean().optional(),
            "landingPageId": t.string().optional(),
            "computedClickThroughUrl": t.string().optional(),
            "customClickThroughUrl": t.string().optional(),
        }
    ).named(renames["ClickThroughUrlIn"])
    types["ClickThroughUrlOut"] = t.struct(
        {
            "defaultLandingPage": t.boolean().optional(),
            "landingPageId": t.string().optional(),
            "computedClickThroughUrl": t.string().optional(),
            "customClickThroughUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClickThroughUrlOut"])
    types["FlightIn"] = t.struct(
        {
            "rateOrCost": t.string().optional(),
            "endDate": t.string(),
            "startDate": t.string(),
            "units": t.string().optional(),
        }
    ).named(renames["FlightIn"])
    types["FlightOut"] = t.struct(
        {
            "rateOrCost": t.string().optional(),
            "endDate": t.string(),
            "startDate": t.string(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlightOut"])
    types["BillingProfilesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "billingProfiles": t.array(t.proxy(renames["BillingProfileIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BillingProfilesListResponseIn"])
    types["BillingProfilesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "billingProfiles": t.array(
                t.proxy(renames["BillingProfileOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingProfilesListResponseOut"])
    types["FloodlightActivitiesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "floodlightActivities": t.array(
                t.proxy(renames["FloodlightActivityIn"])
            ).optional(),
        }
    ).named(renames["FloodlightActivitiesListResponseIn"])
    types["FloodlightActivitiesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "floodlightActivities": t.array(
                t.proxy(renames["FloodlightActivityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivitiesListResponseOut"])
    types["ListPopulationRuleIn"] = t.struct(
        {
            "floodlightActivityId": t.string().optional(),
            "floodlightActivityName": t.string().optional(),
            "listPopulationClauses": t.array(
                t.proxy(renames["ListPopulationClauseIn"])
            ).optional(),
        }
    ).named(renames["ListPopulationRuleIn"])
    types["ListPopulationRuleOut"] = t.struct(
        {
            "floodlightActivityId": t.string().optional(),
            "floodlightActivityName": t.string().optional(),
            "listPopulationClauses": t.array(
                t.proxy(renames["ListPopulationClauseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPopulationRuleOut"])
    types["DirectorySiteSettingsIn"] = t.struct(
        {
            "dfpSettings": t.proxy(renames["DfpSettingsIn"]).optional(),
            "interstitialPlacementAccepted": t.boolean().optional(),
            "instreamVideoPlacementAccepted": t.boolean().optional(),
            "activeViewOptOut": t.boolean().optional(),
        }
    ).named(renames["DirectorySiteSettingsIn"])
    types["DirectorySiteSettingsOut"] = t.struct(
        {
            "dfpSettings": t.proxy(renames["DfpSettingsOut"]).optional(),
            "interstitialPlacementAccepted": t.boolean().optional(),
            "instreamVideoPlacementAccepted": t.boolean().optional(),
            "activeViewOptOut": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectorySiteSettingsOut"])
    types["CustomViewabilityMetricConfigurationIn"] = t.struct(
        {
            "audible": t.boolean().optional(),
            "viewabilityPercent": t.integer().optional(),
            "timeMillis": t.integer().optional(),
            "timePercent": t.integer().optional(),
        }
    ).named(renames["CustomViewabilityMetricConfigurationIn"])
    types["CustomViewabilityMetricConfigurationOut"] = t.struct(
        {
            "audible": t.boolean().optional(),
            "viewabilityPercent": t.integer().optional(),
            "timeMillis": t.integer().optional(),
            "timePercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomViewabilityMetricConfigurationOut"])
    types["ConversionStatusIn"] = t.struct(
        {
            "conversion": t.proxy(renames["ConversionIn"]).optional(),
            "errors": t.array(t.proxy(renames["ConversionErrorIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ConversionStatusIn"])
    types["ConversionStatusOut"] = t.struct(
        {
            "conversion": t.proxy(renames["ConversionOut"]).optional(),
            "errors": t.array(t.proxy(renames["ConversionErrorOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionStatusOut"])
    types["TagSettingsIn"] = t.struct(
        {
            "dynamicTagEnabled": t.boolean().optional(),
            "imageTagEnabled": t.boolean().optional(),
        }
    ).named(renames["TagSettingsIn"])
    types["TagSettingsOut"] = t.struct(
        {
            "dynamicTagEnabled": t.boolean().optional(),
            "imageTagEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagSettingsOut"])
    types["FsCommandIn"] = t.struct(
        {
            "windowHeight": t.integer().optional(),
            "windowWidth": t.integer().optional(),
            "positionOption": t.string().optional(),
            "left": t.integer().optional(),
            "top": t.integer().optional(),
        }
    ).named(renames["FsCommandIn"])
    types["FsCommandOut"] = t.struct(
        {
            "windowHeight": t.integer().optional(),
            "windowWidth": t.integer().optional(),
            "positionOption": t.string().optional(),
            "left": t.integer().optional(),
            "top": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FsCommandOut"])
    types["PathFilterIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional(),
            "pathMatchPosition": t.string().optional(),
        }
    ).named(renames["PathFilterIn"])
    types["PathFilterOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "pathMatchPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathFilterOut"])
    types["DynamicTargetingKeyIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "objectId": t.string().optional(),
            "objectType": t.string().optional(),
        }
    ).named(renames["DynamicTargetingKeyIn"])
    types["DynamicTargetingKeyOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "objectId": t.string().optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicTargetingKeyOut"])

    functions = {}
    functions["placementsGeneratetags"] = dfareporting.patch(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "keyName": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "sslRequired": t.boolean().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "paymentSource": t.string().optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "kind": t.string().optional(),
                "compatibility": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "subaccountId": t.string().optional(),
                "placementGroupId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "contentCategoryId": t.string().optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "placementStrategyId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "accountId": t.string().optional(),
                "primary": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsList"] = dfareporting.patch(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "keyName": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "sslRequired": t.boolean().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "paymentSource": t.string().optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "kind": t.string().optional(),
                "compatibility": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "subaccountId": t.string().optional(),
                "placementGroupId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "contentCategoryId": t.string().optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "placementStrategyId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "accountId": t.string().optional(),
                "primary": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "keyName": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "sslRequired": t.boolean().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "paymentSource": t.string().optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "kind": t.string().optional(),
                "compatibility": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "subaccountId": t.string().optional(),
                "placementGroupId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "contentCategoryId": t.string().optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "placementStrategyId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "accountId": t.string().optional(),
                "primary": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsInsert"] = dfareporting.patch(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "keyName": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "sslRequired": t.boolean().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "paymentSource": t.string().optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "kind": t.string().optional(),
                "compatibility": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "subaccountId": t.string().optional(),
                "placementGroupId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "contentCategoryId": t.string().optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "placementStrategyId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "accountId": t.string().optional(),
                "primary": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsGet"] = dfareporting.patch(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "keyName": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "sslRequired": t.boolean().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "paymentSource": t.string().optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "kind": t.string().optional(),
                "compatibility": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "subaccountId": t.string().optional(),
                "placementGroupId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "contentCategoryId": t.string().optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "placementStrategyId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "accountId": t.string().optional(),
                "primary": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "keyName": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "sslRequired": t.boolean().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "paymentSource": t.string().optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "kind": t.string().optional(),
                "compatibility": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "subaccountId": t.string().optional(),
                "placementGroupId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "contentCategoryId": t.string().optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "placementStrategyId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "accountId": t.string().optional(),
                "primary": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sizesList"] = dfareporting.post(
        "userprofiles/{profileId}/sizes",
        t.struct(
            {
                "profileId": t.string().optional(),
                "width": t.integer().optional(),
                "iab": t.boolean().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "height": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SizeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sizesGet"] = dfareporting.post(
        "userprofiles/{profileId}/sizes",
        t.struct(
            {
                "profileId": t.string().optional(),
                "width": t.integer().optional(),
                "iab": t.boolean().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "height": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SizeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sizesInsert"] = dfareporting.post(
        "userprofiles/{profileId}/sizes",
        t.struct(
            {
                "profileId": t.string().optional(),
                "width": t.integer().optional(),
                "iab": t.boolean().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "height": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SizeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["platformTypesGet"] = dfareporting.get(
        "userprofiles/{profileId}/platformTypes",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["PlatformTypesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["platformTypesList"] = dfareporting.get(
        "userprofiles/{profileId}/platformTypes",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["PlatformTypesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventoryItemsGet"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/inventoryItems",
        t.struct(
            {
                "orderId": t.string().optional(),
                "inPlan": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "sortField": t.string().optional(),
                "type": t.string().optional(),
                "siteId": t.string().optional(),
                "profileId": t.string().optional(),
                "projectId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "ids": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventoryItemsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventoryItemsList"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/inventoryItems",
        t.struct(
            {
                "orderId": t.string().optional(),
                "inPlan": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "sortField": t.string().optional(),
                "type": t.string().optional(),
                "siteId": t.string().optional(),
                "profileId": t.string().optional(),
                "projectId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "ids": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventoryItemsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGet"] = dfareporting.post(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "profileId": t.string().optional(),
                "etag": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "name": t.string().optional(),
                "fileName": t.string().optional(),
                "subAccountId": t.string().optional(),
                "pathCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "floodlightCriteria": t.struct(
                    {
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "type": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "ownerProfileId": t.string().optional(),
                "reachCriteria": t.struct(
                    {
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "schedule": t.struct(
                    {
                        "active": t.boolean().optional(),
                        "startDate": t.string(),
                        "expirationDate": t.string(),
                        "every": t.integer().optional(),
                        "repeats": t.string().optional(),
                        "timezone": t.string().optional(),
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                        "emailOwner": t.boolean().optional(),
                    }
                ).optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsPatch"] = dfareporting.post(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "profileId": t.string().optional(),
                "etag": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "name": t.string().optional(),
                "fileName": t.string().optional(),
                "subAccountId": t.string().optional(),
                "pathCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "floodlightCriteria": t.struct(
                    {
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "type": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "ownerProfileId": t.string().optional(),
                "reachCriteria": t.struct(
                    {
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "schedule": t.struct(
                    {
                        "active": t.boolean().optional(),
                        "startDate": t.string(),
                        "expirationDate": t.string(),
                        "every": t.integer().optional(),
                        "repeats": t.string().optional(),
                        "timezone": t.string().optional(),
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                        "emailOwner": t.boolean().optional(),
                    }
                ).optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "profileId": t.string().optional(),
                "etag": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "name": t.string().optional(),
                "fileName": t.string().optional(),
                "subAccountId": t.string().optional(),
                "pathCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "floodlightCriteria": t.struct(
                    {
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "type": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "ownerProfileId": t.string().optional(),
                "reachCriteria": t.struct(
                    {
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "schedule": t.struct(
                    {
                        "active": t.boolean().optional(),
                        "startDate": t.string(),
                        "expirationDate": t.string(),
                        "every": t.integer().optional(),
                        "repeats": t.string().optional(),
                        "timezone": t.string().optional(),
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                        "emailOwner": t.boolean().optional(),
                    }
                ).optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsRun"] = dfareporting.post(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "profileId": t.string().optional(),
                "etag": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "name": t.string().optional(),
                "fileName": t.string().optional(),
                "subAccountId": t.string().optional(),
                "pathCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "floodlightCriteria": t.struct(
                    {
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "type": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "ownerProfileId": t.string().optional(),
                "reachCriteria": t.struct(
                    {
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "schedule": t.struct(
                    {
                        "active": t.boolean().optional(),
                        "startDate": t.string(),
                        "expirationDate": t.string(),
                        "every": t.integer().optional(),
                        "repeats": t.string().optional(),
                        "timezone": t.string().optional(),
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                        "emailOwner": t.boolean().optional(),
                    }
                ).optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsDelete"] = dfareporting.post(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "profileId": t.string().optional(),
                "etag": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "name": t.string().optional(),
                "fileName": t.string().optional(),
                "subAccountId": t.string().optional(),
                "pathCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "floodlightCriteria": t.struct(
                    {
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "type": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "ownerProfileId": t.string().optional(),
                "reachCriteria": t.struct(
                    {
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "schedule": t.struct(
                    {
                        "active": t.boolean().optional(),
                        "startDate": t.string(),
                        "expirationDate": t.string(),
                        "every": t.integer().optional(),
                        "repeats": t.string().optional(),
                        "timezone": t.string().optional(),
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                        "emailOwner": t.boolean().optional(),
                    }
                ).optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsList"] = dfareporting.post(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "profileId": t.string().optional(),
                "etag": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "name": t.string().optional(),
                "fileName": t.string().optional(),
                "subAccountId": t.string().optional(),
                "pathCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "floodlightCriteria": t.struct(
                    {
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "type": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "ownerProfileId": t.string().optional(),
                "reachCriteria": t.struct(
                    {
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "schedule": t.struct(
                    {
                        "active": t.boolean().optional(),
                        "startDate": t.string(),
                        "expirationDate": t.string(),
                        "every": t.integer().optional(),
                        "repeats": t.string().optional(),
                        "timezone": t.string().optional(),
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                        "emailOwner": t.boolean().optional(),
                    }
                ).optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "profileId": t.string().optional(),
                "etag": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "name": t.string().optional(),
                "fileName": t.string().optional(),
                "subAccountId": t.string().optional(),
                "pathCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "floodlightCriteria": t.struct(
                    {
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "type": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "ownerProfileId": t.string().optional(),
                "reachCriteria": t.struct(
                    {
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "schedule": t.struct(
                    {
                        "active": t.boolean().optional(),
                        "startDate": t.string(),
                        "expirationDate": t.string(),
                        "every": t.integer().optional(),
                        "repeats": t.string().optional(),
                        "timezone": t.string().optional(),
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                        "emailOwner": t.boolean().optional(),
                    }
                ).optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsFilesList"] = dfareporting.get(
        "userprofiles/{profileId}/reports/{reportId}/files/{fileId}",
        t.struct(
            {
                "reportId": t.string().optional(),
                "profileId": t.string().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsFilesGet"] = dfareporting.get(
        "userprofiles/{profileId}/reports/{reportId}/files/{fileId}",
        t.struct(
            {
                "reportId": t.string().optional(),
                "profileId": t.string().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsCompatibleFieldsQuery"] = dfareporting.post(
        "userprofiles/{profileId}/reports/compatiblefields/query",
        t.struct(
            {
                "profileId": t.string().optional(),
                "etag": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "name": t.string().optional(),
                "fileName": t.string().optional(),
                "subAccountId": t.string().optional(),
                "pathCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "floodlightCriteria": t.struct(
                    {
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "type": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "ownerProfileId": t.string().optional(),
                "reachCriteria": t.struct(
                    {
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                    }
                ).optional(),
                "schedule": t.struct(
                    {
                        "active": t.boolean().optional(),
                        "startDate": t.string(),
                        "expirationDate": t.string(),
                        "every": t.integer().optional(),
                        "repeats": t.string().optional(),
                        "timezone": t.string().optional(),
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                        "emailOwner": t.boolean().optional(),
                    }
                ).optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CompatibleFieldsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["directorySitesGet"] = dfareporting.get(
        "userprofiles/{profileId}/directorySites",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "profileId": t.string().optional(),
                "sortField": t.string().optional(),
                "dfpNetworkCode": t.string().optional(),
                "ids": t.string().optional(),
                "acceptsInterstitialPlacements": t.boolean().optional(),
                "acceptsPublisherPaidPlacements": t.boolean().optional(),
                "acceptsInStreamVideoPlacements": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "active": t.boolean().optional(),
                "sortOrder": t.string().optional(),
                "searchString": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DirectorySitesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["directorySitesInsert"] = dfareporting.get(
        "userprofiles/{profileId}/directorySites",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "profileId": t.string().optional(),
                "sortField": t.string().optional(),
                "dfpNetworkCode": t.string().optional(),
                "ids": t.string().optional(),
                "acceptsInterstitialPlacements": t.boolean().optional(),
                "acceptsPublisherPaidPlacements": t.boolean().optional(),
                "acceptsInStreamVideoPlacements": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "active": t.boolean().optional(),
                "sortOrder": t.string().optional(),
                "searchString": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DirectorySitesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["directorySitesList"] = dfareporting.get(
        "userprofiles/{profileId}/directorySites",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "profileId": t.string().optional(),
                "sortField": t.string().optional(),
                "dfpNetworkCode": t.string().optional(),
                "ids": t.string().optional(),
                "acceptsInterstitialPlacements": t.boolean().optional(),
                "acceptsPublisherPaidPlacements": t.boolean().optional(),
                "acceptsInStreamVideoPlacements": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "active": t.boolean().optional(),
                "sortOrder": t.string().optional(),
                "searchString": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DirectorySitesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingRatesList"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles/{billingProfileId}/billingRates",
        t.struct(
            {
                "profileId": t.string().optional(),
                "billingProfileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingRatesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subaccountsGet"] = dfareporting.put(
        "userprofiles/{profileId}/subaccounts",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubaccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subaccountsList"] = dfareporting.put(
        "userprofiles/{profileId}/subaccounts",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubaccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subaccountsPatch"] = dfareporting.put(
        "userprofiles/{profileId}/subaccounts",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubaccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subaccountsInsert"] = dfareporting.put(
        "userprofiles/{profileId}/subaccounts",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubaccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subaccountsUpdate"] = dfareporting.put(
        "userprofiles/{profileId}/subaccounts",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubaccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeAssetsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/creativeAssets/{advertiserId}/creativeAssets",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "profileId": t.string().optional(),
                "clickTags": t.array(t.proxy(renames["ClickTagIn"])).optional(),
                "kind": t.string().optional(),
                "warnedValidationRules": t.array(t.string()).optional(),
                "richMedia": t.boolean().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "id": t.string().optional(),
                "exitCustomEvents": t.array(
                    t.proxy(renames["CreativeCustomEventIn"])
                ).optional(),
                "timerCustomEvents": t.array(
                    t.proxy(renames["CreativeCustomEventIn"])
                ).optional(),
                "detectedFeatures": t.array(t.string()).optional(),
                "assetIdentifier": t.proxy(renames["CreativeAssetIdIn"]).optional(),
                "counterCustomEvents": t.array(
                    t.proxy(renames["CreativeCustomEventIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeAssetMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mobileAppsGet"] = dfareporting.get(
        "userprofiles/{profileId}/mobileApps",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "directories": t.string().optional(),
                "ids": t.string().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MobileAppsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mobileAppsList"] = dfareporting.get(
        "userprofiles/{profileId}/mobileApps",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "directories": t.string().optional(),
                "ids": t.string().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MobileAppsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "active": t.boolean().optional(),
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightActivityId": t.string().optional(),
                "pageToken": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "active": t.boolean().optional(),
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightActivityId": t.string().optional(),
                "pageToken": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsGet"] = dfareporting.get(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "active": t.boolean().optional(),
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightActivityId": t.string().optional(),
                "pageToken": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "active": t.boolean().optional(),
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightActivityId": t.string().optional(),
                "pageToken": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsList"] = dfareporting.get(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "active": t.boolean().optional(),
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightActivityId": t.string().optional(),
                "pageToken": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesList"] = dfareporting.post(
        "userprofiles/{profileId}/placementStrategies",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesDelete"] = dfareporting.post(
        "userprofiles/{profileId}/placementStrategies",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesGet"] = dfareporting.post(
        "userprofiles/{profileId}/placementStrategies",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesPatch"] = dfareporting.post(
        "userprofiles/{profileId}/placementStrategies",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/placementStrategies",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesInsert"] = dfareporting.post(
        "userprofiles/{profileId}/placementStrategies",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTemplatesPatch"] = dfareporting.get(
        "userprofiles/{profileId}/targetingTemplates/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetingTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTemplatesInsert"] = dfareporting.get(
        "userprofiles/{profileId}/targetingTemplates/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetingTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTemplatesUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/targetingTemplates/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetingTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTemplatesList"] = dfareporting.get(
        "userprofiles/{profileId}/targetingTemplates/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetingTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTemplatesGet"] = dfareporting.get(
        "userprofiles/{profileId}/targetingTemplates/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetingTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/accounts",
        t.struct(
            {
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "ids": t.string().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/accounts",
        t.struct(
            {
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "ids": t.string().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = dfareporting.get(
        "userprofiles/{profileId}/accounts",
        t.struct(
            {
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "ids": t.string().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = dfareporting.get(
        "userprofiles/{profileId}/accounts",
        t.struct(
            {
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "maxResults": t.integer().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "ids": t.string().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsInsert"] = dfareporting.patch(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "siteFilterType": t.string().optional(),
                "campaignId": t.string().optional(),
                "siteIds": t.array(t.string()).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "urlEscapeLevels": t.integer().optional(),
                "subaccountId": t.string().optional(),
                "type": t.string().optional(),
                "excludeFromAdxRequests": t.boolean().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "url": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "name": t.string().optional(),
                "status": t.string().optional(),
                "enabledByDefault": t.boolean().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsDelete"] = dfareporting.patch(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "siteFilterType": t.string().optional(),
                "campaignId": t.string().optional(),
                "siteIds": t.array(t.string()).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "urlEscapeLevels": t.integer().optional(),
                "subaccountId": t.string().optional(),
                "type": t.string().optional(),
                "excludeFromAdxRequests": t.boolean().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "url": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "name": t.string().optional(),
                "status": t.string().optional(),
                "enabledByDefault": t.boolean().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsList"] = dfareporting.patch(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "siteFilterType": t.string().optional(),
                "campaignId": t.string().optional(),
                "siteIds": t.array(t.string()).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "urlEscapeLevels": t.integer().optional(),
                "subaccountId": t.string().optional(),
                "type": t.string().optional(),
                "excludeFromAdxRequests": t.boolean().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "url": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "name": t.string().optional(),
                "status": t.string().optional(),
                "enabledByDefault": t.boolean().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsGet"] = dfareporting.patch(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "siteFilterType": t.string().optional(),
                "campaignId": t.string().optional(),
                "siteIds": t.array(t.string()).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "urlEscapeLevels": t.integer().optional(),
                "subaccountId": t.string().optional(),
                "type": t.string().optional(),
                "excludeFromAdxRequests": t.boolean().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "url": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "name": t.string().optional(),
                "status": t.string().optional(),
                "enabledByDefault": t.boolean().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "siteFilterType": t.string().optional(),
                "campaignId": t.string().optional(),
                "siteIds": t.array(t.string()).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "urlEscapeLevels": t.integer().optional(),
                "subaccountId": t.string().optional(),
                "type": t.string().optional(),
                "excludeFromAdxRequests": t.boolean().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "url": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "name": t.string().optional(),
                "status": t.string().optional(),
                "enabledByDefault": t.boolean().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "siteFilterType": t.string().optional(),
                "campaignId": t.string().optional(),
                "siteIds": t.array(t.string()).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "urlEscapeLevels": t.integer().optional(),
                "subaccountId": t.string().optional(),
                "type": t.string().optional(),
                "excludeFromAdxRequests": t.boolean().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "url": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "name": t.string().optional(),
                "status": t.string().optional(),
                "enabledByDefault": t.boolean().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesInsert"] = dfareporting.put(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "id": t.string().optional(),
                "keyName": t.string().optional(),
                "subaccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "kind": t.string().optional(),
                "approved": t.boolean().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesPatch"] = dfareporting.put(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "id": t.string().optional(),
                "keyName": t.string().optional(),
                "subaccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "kind": t.string().optional(),
                "approved": t.boolean().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesGet"] = dfareporting.put(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "id": t.string().optional(),
                "keyName": t.string().optional(),
                "subaccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "kind": t.string().optional(),
                "approved": t.boolean().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesList"] = dfareporting.put(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "id": t.string().optional(),
                "keyName": t.string().optional(),
                "subaccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "kind": t.string().optional(),
                "approved": t.boolean().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesUpdate"] = dfareporting.put(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "id": t.string().optional(),
                "keyName": t.string().optional(),
                "subaccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "kind": t.string().optional(),
                "approved": t.boolean().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postalCodesList"] = dfareporting.get(
        "userprofiles/{profileId}/postalCodes/{code}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostalCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postalCodesGet"] = dfareporting.get(
        "userprofiles/{profileId}/postalCodes/{code}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostalCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountPermissionsList"] = dfareporting.get(
        "userprofiles/{profileId}/accountPermissions/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountPermissionsGet"] = dfareporting.get(
        "userprofiles/{profileId}/accountPermissions/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAssignmentsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles/{billingProfileId}/billingAssignments",
        t.struct(
            {
                "profileId": t.string().optional(),
                "billingProfileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAssignmentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAssignmentsList"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles/{billingProfileId}/billingAssignments",
        t.struct(
            {
                "profileId": t.string().optional(),
                "billingProfileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAssignmentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsInsert"] = dfareporting.patch(
        "userprofiles/{profileId}/ads",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupAssignments": t.array(
                    t.proxy(renames["CreativeGroupAssignmentIn"])
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "deliverySchedule": t.proxy(renames["DeliveryScheduleIn"]).optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "kind": t.string().optional(),
                "audienceSegmentId": t.string().optional(),
                "archived": t.boolean().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "targetingTemplateId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
                "advertiserId": t.string().optional(),
                "remarketingListExpression": t.proxy(
                    renames["ListTargetingExpressionIn"]
                ).optional(),
                "dynamicClickTracker": t.boolean().optional(),
                "compatibility": t.string().optional(),
                "comments": t.string().optional(),
                "name": t.string().optional(),
                "placementAssignments": t.array(
                    t.proxy(renames["PlacementAssignmentIn"])
                ).optional(),
                "startTime": t.string(),
                "type": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "active": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "keyValueTargetingExpression": t.proxy(
                    renames["KeyValueTargetingExpressionIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "technologyTargeting": t.proxy(
                    renames["TechnologyTargetingIn"]
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "creativeRotation": t.proxy(renames["CreativeRotationIn"]).optional(),
                "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
                "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsList"] = dfareporting.patch(
        "userprofiles/{profileId}/ads",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupAssignments": t.array(
                    t.proxy(renames["CreativeGroupAssignmentIn"])
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "deliverySchedule": t.proxy(renames["DeliveryScheduleIn"]).optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "kind": t.string().optional(),
                "audienceSegmentId": t.string().optional(),
                "archived": t.boolean().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "targetingTemplateId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
                "advertiserId": t.string().optional(),
                "remarketingListExpression": t.proxy(
                    renames["ListTargetingExpressionIn"]
                ).optional(),
                "dynamicClickTracker": t.boolean().optional(),
                "compatibility": t.string().optional(),
                "comments": t.string().optional(),
                "name": t.string().optional(),
                "placementAssignments": t.array(
                    t.proxy(renames["PlacementAssignmentIn"])
                ).optional(),
                "startTime": t.string(),
                "type": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "active": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "keyValueTargetingExpression": t.proxy(
                    renames["KeyValueTargetingExpressionIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "technologyTargeting": t.proxy(
                    renames["TechnologyTargetingIn"]
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "creativeRotation": t.proxy(renames["CreativeRotationIn"]).optional(),
                "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
                "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsGet"] = dfareporting.patch(
        "userprofiles/{profileId}/ads",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupAssignments": t.array(
                    t.proxy(renames["CreativeGroupAssignmentIn"])
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "deliverySchedule": t.proxy(renames["DeliveryScheduleIn"]).optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "kind": t.string().optional(),
                "audienceSegmentId": t.string().optional(),
                "archived": t.boolean().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "targetingTemplateId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
                "advertiserId": t.string().optional(),
                "remarketingListExpression": t.proxy(
                    renames["ListTargetingExpressionIn"]
                ).optional(),
                "dynamicClickTracker": t.boolean().optional(),
                "compatibility": t.string().optional(),
                "comments": t.string().optional(),
                "name": t.string().optional(),
                "placementAssignments": t.array(
                    t.proxy(renames["PlacementAssignmentIn"])
                ).optional(),
                "startTime": t.string(),
                "type": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "active": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "keyValueTargetingExpression": t.proxy(
                    renames["KeyValueTargetingExpressionIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "technologyTargeting": t.proxy(
                    renames["TechnologyTargetingIn"]
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "creativeRotation": t.proxy(renames["CreativeRotationIn"]).optional(),
                "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
                "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/ads",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupAssignments": t.array(
                    t.proxy(renames["CreativeGroupAssignmentIn"])
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "deliverySchedule": t.proxy(renames["DeliveryScheduleIn"]).optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "kind": t.string().optional(),
                "audienceSegmentId": t.string().optional(),
                "archived": t.boolean().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "targetingTemplateId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
                "advertiserId": t.string().optional(),
                "remarketingListExpression": t.proxy(
                    renames["ListTargetingExpressionIn"]
                ).optional(),
                "dynamicClickTracker": t.boolean().optional(),
                "compatibility": t.string().optional(),
                "comments": t.string().optional(),
                "name": t.string().optional(),
                "placementAssignments": t.array(
                    t.proxy(renames["PlacementAssignmentIn"])
                ).optional(),
                "startTime": t.string(),
                "type": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "active": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "keyValueTargetingExpression": t.proxy(
                    renames["KeyValueTargetingExpressionIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "technologyTargeting": t.proxy(
                    renames["TechnologyTargetingIn"]
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "creativeRotation": t.proxy(renames["CreativeRotationIn"]).optional(),
                "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
                "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/ads",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupAssignments": t.array(
                    t.proxy(renames["CreativeGroupAssignmentIn"])
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "deliverySchedule": t.proxy(renames["DeliveryScheduleIn"]).optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "kind": t.string().optional(),
                "audienceSegmentId": t.string().optional(),
                "archived": t.boolean().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "targetingTemplateId": t.string().optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
                "advertiserId": t.string().optional(),
                "remarketingListExpression": t.proxy(
                    renames["ListTargetingExpressionIn"]
                ).optional(),
                "dynamicClickTracker": t.boolean().optional(),
                "compatibility": t.string().optional(),
                "comments": t.string().optional(),
                "name": t.string().optional(),
                "placementAssignments": t.array(
                    t.proxy(renames["PlacementAssignmentIn"])
                ).optional(),
                "startTime": t.string(),
                "type": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "active": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "keyValueTargetingExpression": t.proxy(
                    renames["KeyValueTargetingExpressionIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "technologyTargeting": t.proxy(
                    renames["TechnologyTargetingIn"]
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "creativeRotation": t.proxy(renames["CreativeRotationIn"]).optional(),
                "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
                "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dynamicTargetingKeysDelete"] = dfareporting.get(
        "userprofiles/{profileId}/dynamicTargetingKeys",
        t.struct(
            {
                "names": t.string().optional(),
                "objectId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "objectType": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicTargetingKeysListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dynamicTargetingKeysInsert"] = dfareporting.get(
        "userprofiles/{profileId}/dynamicTargetingKeys",
        t.struct(
            {
                "names": t.string().optional(),
                "objectId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "objectType": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicTargetingKeysListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dynamicTargetingKeysList"] = dfareporting.get(
        "userprofiles/{profileId}/dynamicTargetingKeys",
        t.struct(
            {
                "names": t.string().optional(),
                "objectId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "objectType": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicTargetingKeysListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesList"] = dfareporting.post(
        "userprofiles/{profileId}/accountUserProfiles",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "userAccessType": t.string().optional(),
                "subaccountId": t.string().optional(),
                "campaignFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "kind": t.string().optional(),
                "email": t.string().optional(),
                "userRoleId": t.string().optional(),
                "siteFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "traffickerType": t.string().optional(),
                "id": t.string().optional(),
                "comments": t.string().optional(),
                "active": t.boolean().optional(),
                "userRoleFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "locale": t.string().optional(),
                "advertiserFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesGet"] = dfareporting.post(
        "userprofiles/{profileId}/accountUserProfiles",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "userAccessType": t.string().optional(),
                "subaccountId": t.string().optional(),
                "campaignFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "kind": t.string().optional(),
                "email": t.string().optional(),
                "userRoleId": t.string().optional(),
                "siteFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "traffickerType": t.string().optional(),
                "id": t.string().optional(),
                "comments": t.string().optional(),
                "active": t.boolean().optional(),
                "userRoleFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "locale": t.string().optional(),
                "advertiserFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/accountUserProfiles",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "userAccessType": t.string().optional(),
                "subaccountId": t.string().optional(),
                "campaignFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "kind": t.string().optional(),
                "email": t.string().optional(),
                "userRoleId": t.string().optional(),
                "siteFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "traffickerType": t.string().optional(),
                "id": t.string().optional(),
                "comments": t.string().optional(),
                "active": t.boolean().optional(),
                "userRoleFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "locale": t.string().optional(),
                "advertiserFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesPatch"] = dfareporting.post(
        "userprofiles/{profileId}/accountUserProfiles",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "userAccessType": t.string().optional(),
                "subaccountId": t.string().optional(),
                "campaignFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "kind": t.string().optional(),
                "email": t.string().optional(),
                "userRoleId": t.string().optional(),
                "siteFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "traffickerType": t.string().optional(),
                "id": t.string().optional(),
                "comments": t.string().optional(),
                "active": t.boolean().optional(),
                "userRoleFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "locale": t.string().optional(),
                "advertiserFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesInsert"] = dfareporting.post(
        "userprofiles/{profileId}/accountUserProfiles",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "userAccessType": t.string().optional(),
                "subaccountId": t.string().optional(),
                "campaignFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "kind": t.string().optional(),
                "email": t.string().optional(),
                "userRoleId": t.string().optional(),
                "siteFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "traffickerType": t.string().optional(),
                "id": t.string().optional(),
                "comments": t.string().optional(),
                "active": t.boolean().optional(),
                "userRoleFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "locale": t.string().optional(),
                "advertiserFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignCreativeAssociationsList"] = dfareporting.post(
        "userprofiles/{profileId}/campaigns/{campaignId}/campaignCreativeAssociations",
        t.struct(
            {
                "profileId": t.string().optional(),
                "campaignId": t.string().optional(),
                "creativeId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignCreativeAssociationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignCreativeAssociationsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/campaigns/{campaignId}/campaignCreativeAssociations",
        t.struct(
            {
                "profileId": t.string().optional(),
                "campaignId": t.string().optional(),
                "creativeId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignCreativeAssociationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolesGet"] = dfareporting.delete(
        "userprofiles/{profileId}/userRoles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolesList"] = dfareporting.delete(
        "userprofiles/{profileId}/userRoles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolesPatch"] = dfareporting.delete(
        "userprofiles/{profileId}/userRoles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolesInsert"] = dfareporting.delete(
        "userprofiles/{profileId}/userRoles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolesUpdate"] = dfareporting.delete(
        "userprofiles/{profileId}/userRoles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolesDelete"] = dfareporting.delete(
        "userprofiles/{profileId}/userRoles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["metrosList"] = dfareporting.get(
        "userprofiles/{profileId}/metros",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MetrosListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderDocumentsList"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/orderDocuments/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderDocumentsGet"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/orderDocuments/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["citiesList"] = dfareporting.get(
        "userprofiles/{profileId}/cities",
        t.struct(
            {
                "dartIds": t.string().optional(),
                "countryDartIds": t.string().optional(),
                "profileId": t.string().optional(),
                "namePrefix": t.string().optional(),
                "regionDartIds": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CitiesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/floodlightActivityGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "type": t.string().optional(),
                "tagString": t.string().optional(),
                "kind": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "floodlightConfigurationId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsPatch"] = dfareporting.post(
        "userprofiles/{profileId}/floodlightActivityGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "type": t.string().optional(),
                "tagString": t.string().optional(),
                "kind": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "floodlightConfigurationId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsGet"] = dfareporting.post(
        "userprofiles/{profileId}/floodlightActivityGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "type": t.string().optional(),
                "tagString": t.string().optional(),
                "kind": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "floodlightConfigurationId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsList"] = dfareporting.post(
        "userprofiles/{profileId}/floodlightActivityGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "type": t.string().optional(),
                "tagString": t.string().optional(),
                "kind": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "floodlightConfigurationId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/floodlightActivityGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "type": t.string().optional(),
                "tagString": t.string().optional(),
                "kind": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "floodlightConfigurationId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsList"] = dfareporting.patch(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "defaultLandingPageId": t.string().optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerCampaignLinkIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupIds": t.array(t.string()).optional(),
                "billingInvoiceCode": t.string().optional(),
                "adBlockingConfiguration": t.proxy(
                    renames["AdBlockingConfigurationIn"]
                ).optional(),
                "archived": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "additionalCreativeOptimizationConfigurations": t.array(
                    t.proxy(renames["CreativeOptimizationConfigurationIn"])
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "startDate": t.string(),
                "advertiserGroupId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "comment": t.string().optional(),
                "accountId": t.string().optional(),
                "audienceSegmentGroups": t.array(
                    t.proxy(renames["AudienceSegmentGroupIn"])
                ).optional(),
                "endDate": t.string(),
                "kind": t.string().optional(),
                "creativeOptimizationConfiguration": t.proxy(
                    renames["CreativeOptimizationConfigurationIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "externalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsInsert"] = dfareporting.patch(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "defaultLandingPageId": t.string().optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerCampaignLinkIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupIds": t.array(t.string()).optional(),
                "billingInvoiceCode": t.string().optional(),
                "adBlockingConfiguration": t.proxy(
                    renames["AdBlockingConfigurationIn"]
                ).optional(),
                "archived": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "additionalCreativeOptimizationConfigurations": t.array(
                    t.proxy(renames["CreativeOptimizationConfigurationIn"])
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "startDate": t.string(),
                "advertiserGroupId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "comment": t.string().optional(),
                "accountId": t.string().optional(),
                "audienceSegmentGroups": t.array(
                    t.proxy(renames["AudienceSegmentGroupIn"])
                ).optional(),
                "endDate": t.string(),
                "kind": t.string().optional(),
                "creativeOptimizationConfiguration": t.proxy(
                    renames["CreativeOptimizationConfigurationIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "externalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "defaultLandingPageId": t.string().optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerCampaignLinkIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupIds": t.array(t.string()).optional(),
                "billingInvoiceCode": t.string().optional(),
                "adBlockingConfiguration": t.proxy(
                    renames["AdBlockingConfigurationIn"]
                ).optional(),
                "archived": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "additionalCreativeOptimizationConfigurations": t.array(
                    t.proxy(renames["CreativeOptimizationConfigurationIn"])
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "startDate": t.string(),
                "advertiserGroupId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "comment": t.string().optional(),
                "accountId": t.string().optional(),
                "audienceSegmentGroups": t.array(
                    t.proxy(renames["AudienceSegmentGroupIn"])
                ).optional(),
                "endDate": t.string(),
                "kind": t.string().optional(),
                "creativeOptimizationConfiguration": t.proxy(
                    renames["CreativeOptimizationConfigurationIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "externalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsGet"] = dfareporting.patch(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "defaultLandingPageId": t.string().optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerCampaignLinkIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupIds": t.array(t.string()).optional(),
                "billingInvoiceCode": t.string().optional(),
                "adBlockingConfiguration": t.proxy(
                    renames["AdBlockingConfigurationIn"]
                ).optional(),
                "archived": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "additionalCreativeOptimizationConfigurations": t.array(
                    t.proxy(renames["CreativeOptimizationConfigurationIn"])
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "startDate": t.string(),
                "advertiserGroupId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "comment": t.string().optional(),
                "accountId": t.string().optional(),
                "audienceSegmentGroups": t.array(
                    t.proxy(renames["AudienceSegmentGroupIn"])
                ).optional(),
                "endDate": t.string(),
                "kind": t.string().optional(),
                "creativeOptimizationConfiguration": t.proxy(
                    renames["CreativeOptimizationConfigurationIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "externalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "defaultLandingPageId": t.string().optional(),
                "defaultClickThroughEventTagProperties": t.proxy(
                    renames["DefaultClickThroughEventTagPropertiesIn"]
                ).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerCampaignLinkIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "creativeGroupIds": t.array(t.string()).optional(),
                "billingInvoiceCode": t.string().optional(),
                "adBlockingConfiguration": t.proxy(
                    renames["AdBlockingConfigurationIn"]
                ).optional(),
                "archived": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "additionalCreativeOptimizationConfigurations": t.array(
                    t.proxy(renames["CreativeOptimizationConfigurationIn"])
                ).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "startDate": t.string(),
                "advertiserGroupId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "eventTagOverrides": t.array(
                    t.proxy(renames["EventTagOverrideIn"])
                ).optional(),
                "clickThroughUrlSuffixProperties": t.proxy(
                    renames["ClickThroughUrlSuffixPropertiesIn"]
                ).optional(),
                "comment": t.string().optional(),
                "accountId": t.string().optional(),
                "audienceSegmentGroups": t.array(
                    t.proxy(renames["AudienceSegmentGroupIn"])
                ).optional(),
                "endDate": t.string(),
                "kind": t.string().optional(),
                "creativeOptimizationConfiguration": t.proxy(
                    renames["CreativeOptimizationConfigurationIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "externalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesInsert"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "kind": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesList"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "kind": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesGet"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "kind": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "kind": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesDelete"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "kind": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "kind": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dimensionValuesQuery"] = dfareporting.post(
        "userprofiles/{profileId}/dimensionvalues/query",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "profileId": t.string().optional(),
                "pageToken": t.string().optional(),
                "kind": t.string().optional(),
                "filters": t.array(t.proxy(renames["DimensionFilterIn"])).optional(),
                "startDate": t.string(),
                "endDate": t.string(),
                "dimensionName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DimensionValueListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolePermissionGroupsGet"] = dfareporting.get(
        "userprofiles/{profileId}/userRolePermissionGroups",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UserRolePermissionGroupsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolePermissionGroupsList"] = dfareporting.get(
        "userprofiles/{profileId}/userRolePermissionGroups",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UserRolePermissionGroupsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesGet"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "ids": t.string().optional(),
                "sortOrder": t.string().optional(),
                "campaignIds": t.string().optional(),
                "subaccountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "archived": t.boolean().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserLandingPagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "ids": t.string().optional(),
                "sortOrder": t.string().optional(),
                "campaignIds": t.string().optional(),
                "subaccountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "archived": t.boolean().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserLandingPagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesPatch"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "ids": t.string().optional(),
                "sortOrder": t.string().optional(),
                "campaignIds": t.string().optional(),
                "subaccountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "archived": t.boolean().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserLandingPagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesInsert"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "ids": t.string().optional(),
                "sortOrder": t.string().optional(),
                "campaignIds": t.string().optional(),
                "subaccountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "archived": t.boolean().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserLandingPagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesList"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "ids": t.string().optional(),
                "sortOrder": t.string().optional(),
                "campaignIds": t.string().optional(),
                "subaccountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "archived": t.boolean().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserLandingPagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesList"] = dfareporting.get(
        "userprofiles/{profileId}",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGet"] = dfareporting.get(
        "userprofiles/{profileId}",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["languagesList"] = dfareporting.get(
        "userprofiles/{profileId}/languages",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LanguagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsList"] = dfareporting.get(
        "userprofiles/{profileId}/regions",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["RegionsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserInvoicesList"] = dfareporting.get(
        "userprofiles/{profileId}/advertisers/{advertiserId}/invoices",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "issueMonth": t.string().optional(),
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserInvoicesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersList"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/orders/{id}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersGet"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/orders/{id}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsBatchupdate"] = dfareporting.post(
        "userprofiles/{profileId}/conversions/batchinsert",
        t.struct(
            {
                "profileId": t.string().optional(),
                "conversions": t.array(t.proxy(renames["ConversionIn"])).optional(),
                "kind": t.string().optional(),
                "encryptionInfo": t.proxy(renames["EncryptionInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionsBatchInsertResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsBatchinsert"] = dfareporting.post(
        "userprofiles/{profileId}/conversions/batchinsert",
        t.struct(
            {
                "profileId": t.string().optional(),
                "conversions": t.array(t.proxy(renames["ConversionIn"])).optional(),
                "kind": t.string().optional(),
                "encryptionInfo": t.proxy(renames["EncryptionInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionsBatchInsertResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightConfigurationsList"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightConfigurations",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "tagSettings": t.proxy(renames["TagSettingsIn"]).optional(),
                "kind": t.string().optional(),
                "subaccountId": t.string().optional(),
                "naturalSearchConversionAttributionOption": t.string().optional(),
                "customViewabilityMetric": t.proxy(
                    renames["CustomViewabilityMetricIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserId": t.string().optional(),
                "userDefinedVariableConfigurations": t.array(
                    t.proxy(renames["UserDefinedVariableConfigurationIn"])
                ).optional(),
                "firstDayOfWeek": t.string().optional(),
                "accountId": t.string().optional(),
                "exposureToConversionEnabled": t.boolean().optional(),
                "thirdPartyAuthenticationTokens": t.array(
                    t.proxy(renames["ThirdPartyAuthenticationTokenIn"])
                ).optional(),
                "analyticsDataSharingEnabled": t.boolean().optional(),
                "inAppAttributionTrackingEnabled": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "omnitureSettings": t.proxy(renames["OmnitureSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightConfigurationsUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightConfigurations",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "tagSettings": t.proxy(renames["TagSettingsIn"]).optional(),
                "kind": t.string().optional(),
                "subaccountId": t.string().optional(),
                "naturalSearchConversionAttributionOption": t.string().optional(),
                "customViewabilityMetric": t.proxy(
                    renames["CustomViewabilityMetricIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserId": t.string().optional(),
                "userDefinedVariableConfigurations": t.array(
                    t.proxy(renames["UserDefinedVariableConfigurationIn"])
                ).optional(),
                "firstDayOfWeek": t.string().optional(),
                "accountId": t.string().optional(),
                "exposureToConversionEnabled": t.boolean().optional(),
                "thirdPartyAuthenticationTokens": t.array(
                    t.proxy(renames["ThirdPartyAuthenticationTokenIn"])
                ).optional(),
                "analyticsDataSharingEnabled": t.boolean().optional(),
                "inAppAttributionTrackingEnabled": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "omnitureSettings": t.proxy(renames["OmnitureSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightConfigurationsGet"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightConfigurations",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "tagSettings": t.proxy(renames["TagSettingsIn"]).optional(),
                "kind": t.string().optional(),
                "subaccountId": t.string().optional(),
                "naturalSearchConversionAttributionOption": t.string().optional(),
                "customViewabilityMetric": t.proxy(
                    renames["CustomViewabilityMetricIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserId": t.string().optional(),
                "userDefinedVariableConfigurations": t.array(
                    t.proxy(renames["UserDefinedVariableConfigurationIn"])
                ).optional(),
                "firstDayOfWeek": t.string().optional(),
                "accountId": t.string().optional(),
                "exposureToConversionEnabled": t.boolean().optional(),
                "thirdPartyAuthenticationTokens": t.array(
                    t.proxy(renames["ThirdPartyAuthenticationTokenIn"])
                ).optional(),
                "analyticsDataSharingEnabled": t.boolean().optional(),
                "inAppAttributionTrackingEnabled": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "omnitureSettings": t.proxy(renames["OmnitureSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightConfigurationsPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightConfigurations",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "tagSettings": t.proxy(renames["TagSettingsIn"]).optional(),
                "kind": t.string().optional(),
                "subaccountId": t.string().optional(),
                "naturalSearchConversionAttributionOption": t.string().optional(),
                "customViewabilityMetric": t.proxy(
                    renames["CustomViewabilityMetricIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserId": t.string().optional(),
                "userDefinedVariableConfigurations": t.array(
                    t.proxy(renames["UserDefinedVariableConfigurationIn"])
                ).optional(),
                "firstDayOfWeek": t.string().optional(),
                "accountId": t.string().optional(),
                "exposureToConversionEnabled": t.boolean().optional(),
                "thirdPartyAuthenticationTokens": t.array(
                    t.proxy(renames["ThirdPartyAuthenticationTokenIn"])
                ).optional(),
                "analyticsDataSharingEnabled": t.boolean().optional(),
                "inAppAttributionTrackingEnabled": t.boolean().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "omnitureSettings": t.proxy(renames["OmnitureSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsList"] = dfareporting.put(
        "userprofiles/{profileId}/advertiserGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsInsert"] = dfareporting.put(
        "userprofiles/{profileId}/advertiserGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsPatch"] = dfareporting.put(
        "userprofiles/{profileId}/advertiserGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsDelete"] = dfareporting.put(
        "userprofiles/{profileId}/advertiserGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsGet"] = dfareporting.put(
        "userprofiles/{profileId}/advertiserGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsUpdate"] = dfareporting.put(
        "userprofiles/{profileId}/advertiserGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contentCategoriesDelete"] = dfareporting.put(
        "userprofiles/{profileId}/contentCategories",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contentCategoriesInsert"] = dfareporting.put(
        "userprofiles/{profileId}/contentCategories",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contentCategoriesGet"] = dfareporting.put(
        "userprofiles/{profileId}/contentCategories",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contentCategoriesPatch"] = dfareporting.put(
        "userprofiles/{profileId}/contentCategories",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contentCategoriesList"] = dfareporting.put(
        "userprofiles/{profileId}/contentCategories",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contentCategoriesUpdate"] = dfareporting.put(
        "userprofiles/{profileId}/contentCategories",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativesPatch"] = dfareporting.get(
        "userprofiles/{profileId}/creatives/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativesUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/creatives/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativesList"] = dfareporting.get(
        "userprofiles/{profileId}/creatives/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativesInsert"] = dfareporting.get(
        "userprofiles/{profileId}/creatives/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativesGet"] = dfareporting.get(
        "userprofiles/{profileId}/creatives/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mobileCarriersGet"] = dfareporting.get(
        "userprofiles/{profileId}/mobileCarriers",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MobileCarriersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mobileCarriersList"] = dfareporting.get(
        "userprofiles/{profileId}/mobileCarriers",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MobileCarriersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operatingSystemsGet"] = dfareporting.get(
        "userprofiles/{profileId}/operatingSystems",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperatingSystemsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operatingSystemsList"] = dfareporting.get(
        "userprofiles/{profileId}/operatingSystems",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperatingSystemsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetableRemarketingListsList"] = dfareporting.get(
        "userprofiles/{profileId}/targetableRemarketingLists/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetableRemarketingListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetableRemarketingListsGet"] = dfareporting.get(
        "userprofiles/{profileId}/targetableRemarketingLists/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetableRemarketingListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersList"] = dfareporting.post(
        "userprofiles/{profileId}/advertisers",
        t.struct(
            {
                "profileId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "defaultEmail": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "suspended": t.boolean().optional(),
                "advertiserGroupId": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "subaccountId": t.string().optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersGet"] = dfareporting.post(
        "userprofiles/{profileId}/advertisers",
        t.struct(
            {
                "profileId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "defaultEmail": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "suspended": t.boolean().optional(),
                "advertiserGroupId": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "subaccountId": t.string().optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersPatch"] = dfareporting.post(
        "userprofiles/{profileId}/advertisers",
        t.struct(
            {
                "profileId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "defaultEmail": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "suspended": t.boolean().optional(),
                "advertiserGroupId": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "subaccountId": t.string().optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/advertisers",
        t.struct(
            {
                "profileId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "defaultEmail": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "suspended": t.boolean().optional(),
                "advertiserGroupId": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "subaccountId": t.string().optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsert"] = dfareporting.post(
        "userprofiles/{profileId}/advertisers",
        t.struct(
            {
                "profileId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "defaultEmail": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "suspended": t.boolean().optional(),
                "advertiserGroupId": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "subaccountId": t.string().optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "name": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videoFormatsList"] = dfareporting.get(
        "userprofiles/{profileId}/videoFormats/{id}",
        t.struct(
            {
                "id": t.integer().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoFormatOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videoFormatsGet"] = dfareporting.get(
        "userprofiles/{profileId}/videoFormats/{id}",
        t.struct(
            {
                "id": t.integer().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoFormatOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsInsert"] = dfareporting.patch(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "siteId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "directorySiteId": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "activeStatus": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "name": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "externalId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "placementGroupType": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsList"] = dfareporting.patch(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "siteId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "directorySiteId": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "activeStatus": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "name": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "externalId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "placementGroupType": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsGet"] = dfareporting.patch(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "siteId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "directorySiteId": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "activeStatus": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "name": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "externalId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "placementGroupType": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "siteId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "directorySiteId": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "activeStatus": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "name": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "externalId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "placementGroupType": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "siteId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "directorySiteId": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "activeStatus": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "name": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "externalId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "campaignId": t.string().optional(),
                "comment": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "placementGroupType": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountActiveAdSummariesGet"] = dfareporting.get(
        "userprofiles/{profileId}/accountActiveAdSummaries/{summaryAccountId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "summaryAccountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountActiveAdSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesList"] = dfareporting.get(
        "reports/{reportId}/files/{fileId}",
        t.struct(
            {
                "reportId": t.string().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesGet"] = dfareporting.get(
        "reports/{reportId}/files/{fileId}",
        t.struct(
            {
                "reportId": t.string().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingProfilesList"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingProfilesUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingProfilesGet"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changeLogsGet"] = dfareporting.get(
        "userprofiles/{profileId}/changeLogs",
        t.struct(
            {
                "ids": t.string().optional(),
                "objectType": t.string().optional(),
                "maxResults": t.integer().optional(),
                "minChangeTime": t.string().optional(),
                "objectIds": t.string().optional(),
                "action": t.string().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "maxChangeTime": t.string().optional(),
                "userProfileIds": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangeLogsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changeLogsList"] = dfareporting.get(
        "userprofiles/{profileId}/changeLogs",
        t.struct(
            {
                "ids": t.string().optional(),
                "objectType": t.string().optional(),
                "maxResults": t.integer().optional(),
                "minChangeTime": t.string().optional(),
                "objectIds": t.string().optional(),
                "action": t.string().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "maxChangeTime": t.string().optional(),
                "userProfileIds": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangeLogsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountPermissionGroupsGet"] = dfareporting.get(
        "userprofiles/{profileId}/accountPermissionGroups",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccountPermissionGroupsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountPermissionGroupsList"] = dfareporting.get(
        "userprofiles/{profileId}/accountPermissionGroups",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccountPermissionGroupsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolePermissionsGet"] = dfareporting.get(
        "userprofiles/{profileId}/userRolePermissions",
        t.struct(
            {
                "ids": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserRolePermissionsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolePermissionsList"] = dfareporting.get(
        "userprofiles/{profileId}/userRolePermissions",
        t.struct(
            {
                "ids": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserRolePermissionsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsGet"] = dfareporting.put(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsInsert"] = dfareporting.put(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsList"] = dfareporting.put(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsDelete"] = dfareporting.put(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsPatch"] = dfareporting.put(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsUpdate"] = dfareporting.put(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = dfareporting.get(
        "userprofiles/{profileId}/projects",
        t.struct(
            {
                "ids": t.string().optional(),
                "sortField": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "searchString": t.string().optional(),
                "pageToken": t.string().optional(),
                "sortOrder": t.string().optional(),
                "profileId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsList"] = dfareporting.get(
        "userprofiles/{profileId}/projects",
        t.struct(
            {
                "ids": t.string().optional(),
                "sortField": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "searchString": t.string().optional(),
                "pageToken": t.string().optional(),
                "sortOrder": t.string().optional(),
                "profileId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operatingSystemVersionsList"] = dfareporting.get(
        "userprofiles/{profileId}/operatingSystemVersions/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperatingSystemVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operatingSystemVersionsGet"] = dfareporting.get(
        "userprofiles/{profileId}/operatingSystemVersions/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperatingSystemVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["browsersList"] = dfareporting.get(
        "userprofiles/{profileId}/browsers",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["BrowsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["countriesList"] = dfareporting.get(
        "userprofiles/{profileId}/countries/{dartId}",
        t.struct(
            {
                "dartId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CountryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["countriesGet"] = dfareporting.get(
        "userprofiles/{profileId}/countries/{dartId}",
        t.struct(
            {
                "dartId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CountryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivitiesGet"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "countingMethod": t.string().optional(),
                "status": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "cacheBustingType": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "expectedUrl": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "secure": t.boolean().optional(),
                "tagFormat": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "tagString": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivitiesList"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "countingMethod": t.string().optional(),
                "status": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "cacheBustingType": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "expectedUrl": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "secure": t.boolean().optional(),
                "tagFormat": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "tagString": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivitiesInsert"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "countingMethod": t.string().optional(),
                "status": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "cacheBustingType": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "expectedUrl": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "secure": t.boolean().optional(),
                "tagFormat": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "tagString": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivitiesDelete"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "countingMethod": t.string().optional(),
                "status": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "cacheBustingType": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "expectedUrl": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "secure": t.boolean().optional(),
                "tagFormat": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "tagString": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivitiesUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "countingMethod": t.string().optional(),
                "status": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "cacheBustingType": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "expectedUrl": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "secure": t.boolean().optional(),
                "tagFormat": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "tagString": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivitiesGeneratetag"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "countingMethod": t.string().optional(),
                "status": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "cacheBustingType": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "expectedUrl": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "secure": t.boolean().optional(),
                "tagFormat": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "tagString": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivitiesPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "countingMethod": t.string().optional(),
                "status": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "cacheBustingType": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "expectedUrl": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "secure": t.boolean().optional(),
                "tagFormat": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "sslRequired": t.boolean().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "tagString": t.string().optional(),
                "sslCompliant": t.boolean().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListSharesPatch"] = dfareporting.get(
        "userprofiles/{profileId}/remarketingListShares/{remarketingListId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "remarketingListId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListShareOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListSharesUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/remarketingListShares/{remarketingListId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "remarketingListId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListShareOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListSharesGet"] = dfareporting.get(
        "userprofiles/{profileId}/remarketingListShares/{remarketingListId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "remarketingListId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListShareOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectionTypesGet"] = dfareporting.get(
        "userprofiles/{profileId}/connectionTypes",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionTypesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectionTypesList"] = dfareporting.get(
        "userprofiles/{profileId}/connectionTypes",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionTypesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsPatch"] = dfareporting.post(
        "userprofiles/{profileId}/creativeGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "groupNumber": t.integer().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsGet"] = dfareporting.post(
        "userprofiles/{profileId}/creativeGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "groupNumber": t.integer().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsList"] = dfareporting.post(
        "userprofiles/{profileId}/creativeGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "groupNumber": t.integer().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/creativeGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "groupNumber": t.integer().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/creativeGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "groupNumber": t.integer().optional(),
                "accountId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dfareporting",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
