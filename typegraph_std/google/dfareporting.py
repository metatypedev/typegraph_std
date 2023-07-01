from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_dfareporting():
    dfareporting = HTTPRuntime("https://dfareporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_dfareporting_1_ErrorResponse",
        "DeliveryScheduleIn": "_dfareporting_2_DeliveryScheduleIn",
        "DeliveryScheduleOut": "_dfareporting_3_DeliveryScheduleOut",
        "TargetingTemplateIn": "_dfareporting_4_TargetingTemplateIn",
        "TargetingTemplateOut": "_dfareporting_5_TargetingTemplateOut",
        "DynamicTargetingKeysListResponseIn": "_dfareporting_6_DynamicTargetingKeysListResponseIn",
        "DynamicTargetingKeysListResponseOut": "_dfareporting_7_DynamicTargetingKeysListResponseOut",
        "FileListIn": "_dfareporting_8_FileListIn",
        "FileListOut": "_dfareporting_9_FileListOut",
        "CreativeFieldAssignmentIn": "_dfareporting_10_CreativeFieldAssignmentIn",
        "CreativeFieldAssignmentOut": "_dfareporting_11_CreativeFieldAssignmentOut",
        "ObjectFilterIn": "_dfareporting_12_ObjectFilterIn",
        "ObjectFilterOut": "_dfareporting_13_ObjectFilterOut",
        "DisjunctiveMatchStatementIn": "_dfareporting_14_DisjunctiveMatchStatementIn",
        "DisjunctiveMatchStatementOut": "_dfareporting_15_DisjunctiveMatchStatementOut",
        "CreativeGroupAssignmentIn": "_dfareporting_16_CreativeGroupAssignmentIn",
        "CreativeGroupAssignmentOut": "_dfareporting_17_CreativeGroupAssignmentOut",
        "DimensionValueRequestIn": "_dfareporting_18_DimensionValueRequestIn",
        "DimensionValueRequestOut": "_dfareporting_19_DimensionValueRequestOut",
        "ConversionErrorIn": "_dfareporting_20_ConversionErrorIn",
        "ConversionErrorOut": "_dfareporting_21_ConversionErrorOut",
        "OperatingSystemIn": "_dfareporting_22_OperatingSystemIn",
        "OperatingSystemOut": "_dfareporting_23_OperatingSystemOut",
        "CreativeFieldsListResponseIn": "_dfareporting_24_CreativeFieldsListResponseIn",
        "CreativeFieldsListResponseOut": "_dfareporting_25_CreativeFieldsListResponseOut",
        "MeasurementPartnerWrappingDataIn": "_dfareporting_26_MeasurementPartnerWrappingDataIn",
        "MeasurementPartnerWrappingDataOut": "_dfareporting_27_MeasurementPartnerWrappingDataOut",
        "FileIn": "_dfareporting_28_FileIn",
        "FileOut": "_dfareporting_29_FileOut",
        "OperatingSystemsListResponseIn": "_dfareporting_30_OperatingSystemsListResponseIn",
        "OperatingSystemsListResponseOut": "_dfareporting_31_OperatingSystemsListResponseOut",
        "AccountUserProfileIn": "_dfareporting_32_AccountUserProfileIn",
        "AccountUserProfileOut": "_dfareporting_33_AccountUserProfileOut",
        "CustomViewabilityMetricConfigurationIn": "_dfareporting_34_CustomViewabilityMetricConfigurationIn",
        "CustomViewabilityMetricConfigurationOut": "_dfareporting_35_CustomViewabilityMetricConfigurationOut",
        "ChannelGroupingRuleIn": "_dfareporting_36_ChannelGroupingRuleIn",
        "ChannelGroupingRuleOut": "_dfareporting_37_ChannelGroupingRuleOut",
        "MetroIn": "_dfareporting_38_MetroIn",
        "MetroOut": "_dfareporting_39_MetroOut",
        "CreativeAssetMetadataIn": "_dfareporting_40_CreativeAssetMetadataIn",
        "CreativeAssetMetadataOut": "_dfareporting_41_CreativeAssetMetadataOut",
        "ProjectsListResponseIn": "_dfareporting_42_ProjectsListResponseIn",
        "ProjectsListResponseOut": "_dfareporting_43_ProjectsListResponseOut",
        "PopupWindowPropertiesIn": "_dfareporting_44_PopupWindowPropertiesIn",
        "PopupWindowPropertiesOut": "_dfareporting_45_PopupWindowPropertiesOut",
        "VideoSettingsIn": "_dfareporting_46_VideoSettingsIn",
        "VideoSettingsOut": "_dfareporting_47_VideoSettingsOut",
        "CampaignCreativeAssociationsListResponseIn": "_dfareporting_48_CampaignCreativeAssociationsListResponseIn",
        "CampaignCreativeAssociationsListResponseOut": "_dfareporting_49_CampaignCreativeAssociationsListResponseOut",
        "CreativeAssetIdIn": "_dfareporting_50_CreativeAssetIdIn",
        "CreativeAssetIdOut": "_dfareporting_51_CreativeAssetIdOut",
        "UserRolesListResponseIn": "_dfareporting_52_UserRolesListResponseIn",
        "UserRolesListResponseOut": "_dfareporting_53_UserRolesListResponseOut",
        "ReportIn": "_dfareporting_54_ReportIn",
        "ReportOut": "_dfareporting_55_ReportOut",
        "PlacementGroupsListResponseIn": "_dfareporting_56_PlacementGroupsListResponseIn",
        "PlacementGroupsListResponseOut": "_dfareporting_57_PlacementGroupsListResponseOut",
        "CreativeGroupsListResponseIn": "_dfareporting_58_CreativeGroupsListResponseIn",
        "CreativeGroupsListResponseOut": "_dfareporting_59_CreativeGroupsListResponseOut",
        "AdsListResponseIn": "_dfareporting_60_AdsListResponseIn",
        "AdsListResponseOut": "_dfareporting_61_AdsListResponseOut",
        "FloodlightActivityIn": "_dfareporting_62_FloodlightActivityIn",
        "FloodlightActivityOut": "_dfareporting_63_FloodlightActivityOut",
        "VideoOffsetIn": "_dfareporting_64_VideoOffsetIn",
        "VideoOffsetOut": "_dfareporting_65_VideoOffsetOut",
        "SubaccountIn": "_dfareporting_66_SubaccountIn",
        "SubaccountOut": "_dfareporting_67_SubaccountOut",
        "FloodlightConfigurationIn": "_dfareporting_68_FloodlightConfigurationIn",
        "FloodlightConfigurationOut": "_dfareporting_69_FloodlightConfigurationOut",
        "RecipientIn": "_dfareporting_70_RecipientIn",
        "RecipientOut": "_dfareporting_71_RecipientOut",
        "CreativeGroupIn": "_dfareporting_72_CreativeGroupIn",
        "CreativeGroupOut": "_dfareporting_73_CreativeGroupOut",
        "InventoryItemsListResponseIn": "_dfareporting_74_InventoryItemsListResponseIn",
        "InventoryItemsListResponseOut": "_dfareporting_75_InventoryItemsListResponseOut",
        "AdIn": "_dfareporting_76_AdIn",
        "AdOut": "_dfareporting_77_AdOut",
        "DimensionValueIn": "_dfareporting_78_DimensionValueIn",
        "DimensionValueOut": "_dfareporting_79_DimensionValueOut",
        "ConversionIn": "_dfareporting_80_ConversionIn",
        "ConversionOut": "_dfareporting_81_ConversionOut",
        "FrequencyCapIn": "_dfareporting_82_FrequencyCapIn",
        "FrequencyCapOut": "_dfareporting_83_FrequencyCapOut",
        "BillingRateIn": "_dfareporting_84_BillingRateIn",
        "BillingRateOut": "_dfareporting_85_BillingRateOut",
        "CreativeAssignmentIn": "_dfareporting_86_CreativeAssignmentIn",
        "CreativeAssignmentOut": "_dfareporting_87_CreativeAssignmentOut",
        "DimensionFilterIn": "_dfareporting_88_DimensionFilterIn",
        "DimensionFilterOut": "_dfareporting_89_DimensionFilterOut",
        "ContentCategoriesListResponseIn": "_dfareporting_90_ContentCategoriesListResponseIn",
        "ContentCategoriesListResponseOut": "_dfareporting_91_ContentCategoriesListResponseOut",
        "EventFilterIn": "_dfareporting_92_EventFilterIn",
        "EventFilterOut": "_dfareporting_93_EventFilterOut",
        "AdvertiserGroupsListResponseIn": "_dfareporting_94_AdvertiserGroupsListResponseIn",
        "AdvertiserGroupsListResponseOut": "_dfareporting_95_AdvertiserGroupsListResponseOut",
        "ConversionsBatchInsertResponseIn": "_dfareporting_96_ConversionsBatchInsertResponseIn",
        "ConversionsBatchInsertResponseOut": "_dfareporting_97_ConversionsBatchInsertResponseOut",
        "BrowserIn": "_dfareporting_98_BrowserIn",
        "BrowserOut": "_dfareporting_99_BrowserOut",
        "PlacementGroupIn": "_dfareporting_100_PlacementGroupIn",
        "PlacementGroupOut": "_dfareporting_101_PlacementGroupOut",
        "CustomRichMediaEventsIn": "_dfareporting_102_CustomRichMediaEventsIn",
        "CustomRichMediaEventsOut": "_dfareporting_103_CustomRichMediaEventsOut",
        "BillingRatesListResponseIn": "_dfareporting_104_BillingRatesListResponseIn",
        "BillingRatesListResponseOut": "_dfareporting_105_BillingRatesListResponseOut",
        "UserRolePermissionGroupsListResponseIn": "_dfareporting_106_UserRolePermissionGroupsListResponseIn",
        "UserRolePermissionGroupsListResponseOut": "_dfareporting_107_UserRolePermissionGroupsListResponseOut",
        "ClickThroughUrlIn": "_dfareporting_108_ClickThroughUrlIn",
        "ClickThroughUrlOut": "_dfareporting_109_ClickThroughUrlOut",
        "CompatibleFieldsIn": "_dfareporting_110_CompatibleFieldsIn",
        "CompatibleFieldsOut": "_dfareporting_111_CompatibleFieldsOut",
        "ClickThroughUrlSuffixPropertiesIn": "_dfareporting_112_ClickThroughUrlSuffixPropertiesIn",
        "ClickThroughUrlSuffixPropertiesOut": "_dfareporting_113_ClickThroughUrlSuffixPropertiesOut",
        "CreativeFieldValuesListResponseIn": "_dfareporting_114_CreativeFieldValuesListResponseIn",
        "CreativeFieldValuesListResponseOut": "_dfareporting_115_CreativeFieldValuesListResponseOut",
        "RemarketingListIn": "_dfareporting_116_RemarketingListIn",
        "RemarketingListOut": "_dfareporting_117_RemarketingListOut",
        "VideoFormatsListResponseIn": "_dfareporting_118_VideoFormatsListResponseIn",
        "VideoFormatsListResponseOut": "_dfareporting_119_VideoFormatsListResponseOut",
        "PlacementTagIn": "_dfareporting_120_PlacementTagIn",
        "PlacementTagOut": "_dfareporting_121_PlacementTagOut",
        "ReportCompatibleFieldsIn": "_dfareporting_122_ReportCompatibleFieldsIn",
        "ReportCompatibleFieldsOut": "_dfareporting_123_ReportCompatibleFieldsOut",
        "CustomViewabilityMetricIn": "_dfareporting_124_CustomViewabilityMetricIn",
        "CustomViewabilityMetricOut": "_dfareporting_125_CustomViewabilityMetricOut",
        "TagDataIn": "_dfareporting_126_TagDataIn",
        "TagDataOut": "_dfareporting_127_TagDataOut",
        "OperatingSystemVersionsListResponseIn": "_dfareporting_128_OperatingSystemVersionsListResponseIn",
        "OperatingSystemVersionsListResponseOut": "_dfareporting_129_OperatingSystemVersionsListResponseOut",
        "ConversionsBatchInsertRequestIn": "_dfareporting_130_ConversionsBatchInsertRequestIn",
        "ConversionsBatchInsertRequestOut": "_dfareporting_131_ConversionsBatchInsertRequestOut",
        "OfflineUserAddressInfoIn": "_dfareporting_132_OfflineUserAddressInfoIn",
        "OfflineUserAddressInfoOut": "_dfareporting_133_OfflineUserAddressInfoOut",
        "DateRangeIn": "_dfareporting_134_DateRangeIn",
        "DateRangeOut": "_dfareporting_135_DateRangeOut",
        "AdvertiserGroupIn": "_dfareporting_136_AdvertiserGroupIn",
        "AdvertiserGroupOut": "_dfareporting_137_AdvertiserGroupOut",
        "SortedDimensionIn": "_dfareporting_138_SortedDimensionIn",
        "SortedDimensionOut": "_dfareporting_139_SortedDimensionOut",
        "BrowsersListResponseIn": "_dfareporting_140_BrowsersListResponseIn",
        "BrowsersListResponseOut": "_dfareporting_141_BrowsersListResponseOut",
        "PlatformTypeIn": "_dfareporting_142_PlatformTypeIn",
        "PlatformTypeOut": "_dfareporting_143_PlatformTypeOut",
        "FloodlightActivityGroupIn": "_dfareporting_144_FloodlightActivityGroupIn",
        "FloodlightActivityGroupOut": "_dfareporting_145_FloodlightActivityGroupOut",
        "LanguageTargetingIn": "_dfareporting_146_LanguageTargetingIn",
        "LanguageTargetingOut": "_dfareporting_147_LanguageTargetingOut",
        "DefaultClickThroughEventTagPropertiesIn": "_dfareporting_148_DefaultClickThroughEventTagPropertiesIn",
        "DefaultClickThroughEventTagPropertiesOut": "_dfareporting_149_DefaultClickThroughEventTagPropertiesOut",
        "PricingSchedulePricingPeriodIn": "_dfareporting_150_PricingSchedulePricingPeriodIn",
        "PricingSchedulePricingPeriodOut": "_dfareporting_151_PricingSchedulePricingPeriodOut",
        "SizesListResponseIn": "_dfareporting_152_SizesListResponseIn",
        "SizesListResponseOut": "_dfareporting_153_SizesListResponseOut",
        "AdvertisersListResponseIn": "_dfareporting_154_AdvertisersListResponseIn",
        "AdvertisersListResponseOut": "_dfareporting_155_AdvertisersListResponseOut",
        "LandingPageIn": "_dfareporting_156_LandingPageIn",
        "LandingPageOut": "_dfareporting_157_LandingPageOut",
        "SiteIn": "_dfareporting_158_SiteIn",
        "SiteOut": "_dfareporting_159_SiteOut",
        "InventoryItemIn": "_dfareporting_160_InventoryItemIn",
        "InventoryItemOut": "_dfareporting_161_InventoryItemOut",
        "PricingScheduleIn": "_dfareporting_162_PricingScheduleIn",
        "PricingScheduleOut": "_dfareporting_163_PricingScheduleOut",
        "UserProfileListIn": "_dfareporting_164_UserProfileListIn",
        "UserProfileListOut": "_dfareporting_165_UserProfileListOut",
        "CrossDimensionReachReportCompatibleFieldsIn": "_dfareporting_166_CrossDimensionReachReportCompatibleFieldsIn",
        "CrossDimensionReachReportCompatibleFieldsOut": "_dfareporting_167_CrossDimensionReachReportCompatibleFieldsOut",
        "CreativeAssetIn": "_dfareporting_168_CreativeAssetIn",
        "CreativeAssetOut": "_dfareporting_169_CreativeAssetOut",
        "ThirdPartyAuthenticationTokenIn": "_dfareporting_170_ThirdPartyAuthenticationTokenIn",
        "ThirdPartyAuthenticationTokenOut": "_dfareporting_171_ThirdPartyAuthenticationTokenOut",
        "SiteSettingsIn": "_dfareporting_172_SiteSettingsIn",
        "SiteSettingsOut": "_dfareporting_173_SiteSettingsOut",
        "FloodlightReportCompatibleFieldsIn": "_dfareporting_174_FloodlightReportCompatibleFieldsIn",
        "FloodlightReportCompatibleFieldsOut": "_dfareporting_175_FloodlightReportCompatibleFieldsOut",
        "LanguagesListResponseIn": "_dfareporting_176_LanguagesListResponseIn",
        "LanguagesListResponseOut": "_dfareporting_177_LanguagesListResponseOut",
        "CountriesListResponseIn": "_dfareporting_178_CountriesListResponseIn",
        "CountriesListResponseOut": "_dfareporting_179_CountriesListResponseOut",
        "SiteContactIn": "_dfareporting_180_SiteContactIn",
        "SiteContactOut": "_dfareporting_181_SiteContactOut",
        "ConnectionTypesListResponseIn": "_dfareporting_182_ConnectionTypesListResponseIn",
        "ConnectionTypesListResponseOut": "_dfareporting_183_ConnectionTypesListResponseOut",
        "PlacementsGenerateTagsResponseIn": "_dfareporting_184_PlacementsGenerateTagsResponseIn",
        "PlacementsGenerateTagsResponseOut": "_dfareporting_185_PlacementsGenerateTagsResponseOut",
        "TechnologyTargetingIn": "_dfareporting_186_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_dfareporting_187_TechnologyTargetingOut",
        "ChangeLogIn": "_dfareporting_188_ChangeLogIn",
        "ChangeLogOut": "_dfareporting_189_ChangeLogOut",
        "ReportsConfigurationIn": "_dfareporting_190_ReportsConfigurationIn",
        "ReportsConfigurationOut": "_dfareporting_191_ReportsConfigurationOut",
        "TargetWindowIn": "_dfareporting_192_TargetWindowIn",
        "TargetWindowOut": "_dfareporting_193_TargetWindowOut",
        "PostalCodeIn": "_dfareporting_194_PostalCodeIn",
        "PostalCodeOut": "_dfareporting_195_PostalCodeOut",
        "FloodlightConfigurationsListResponseIn": "_dfareporting_196_FloodlightConfigurationsListResponseIn",
        "FloodlightConfigurationsListResponseOut": "_dfareporting_197_FloodlightConfigurationsListResponseOut",
        "CreativeOptimizationConfigurationIn": "_dfareporting_198_CreativeOptimizationConfigurationIn",
        "CreativeOptimizationConfigurationOut": "_dfareporting_199_CreativeOptimizationConfigurationOut",
        "CreativeIn": "_dfareporting_200_CreativeIn",
        "CreativeOut": "_dfareporting_201_CreativeOut",
        "AdvertiserLandingPagesListResponseIn": "_dfareporting_202_AdvertiserLandingPagesListResponseIn",
        "AdvertiserLandingPagesListResponseOut": "_dfareporting_203_AdvertiserLandingPagesListResponseOut",
        "ConversionsBatchUpdateRequestIn": "_dfareporting_204_ConversionsBatchUpdateRequestIn",
        "ConversionsBatchUpdateRequestOut": "_dfareporting_205_ConversionsBatchUpdateRequestOut",
        "UserProfileIn": "_dfareporting_206_UserProfileIn",
        "UserProfileOut": "_dfareporting_207_UserProfileOut",
        "DynamicTargetingKeyIn": "_dfareporting_208_DynamicTargetingKeyIn",
        "DynamicTargetingKeyOut": "_dfareporting_209_DynamicTargetingKeyOut",
        "CreativeFieldValueIn": "_dfareporting_210_CreativeFieldValueIn",
        "CreativeFieldValueOut": "_dfareporting_211_CreativeFieldValueOut",
        "BillingProfilesListResponseIn": "_dfareporting_212_BillingProfilesListResponseIn",
        "BillingProfilesListResponseOut": "_dfareporting_213_BillingProfilesListResponseOut",
        "UserRolePermissionGroupIn": "_dfareporting_214_UserRolePermissionGroupIn",
        "UserRolePermissionGroupOut": "_dfareporting_215_UserRolePermissionGroupOut",
        "BillingProfileIn": "_dfareporting_216_BillingProfileIn",
        "BillingProfileOut": "_dfareporting_217_BillingProfileOut",
        "UvarFilterIn": "_dfareporting_218_UvarFilterIn",
        "UvarFilterOut": "_dfareporting_219_UvarFilterOut",
        "RemarketingListsListResponseIn": "_dfareporting_220_RemarketingListsListResponseIn",
        "RemarketingListsListResponseOut": "_dfareporting_221_RemarketingListsListResponseOut",
        "RuleIn": "_dfareporting_222_RuleIn",
        "RuleOut": "_dfareporting_223_RuleOut",
        "TargetableRemarketingListIn": "_dfareporting_224_TargetableRemarketingListIn",
        "TargetableRemarketingListOut": "_dfareporting_225_TargetableRemarketingListOut",
        "CreativeClickThroughUrlIn": "_dfareporting_226_CreativeClickThroughUrlIn",
        "CreativeClickThroughUrlOut": "_dfareporting_227_CreativeClickThroughUrlOut",
        "PostalCodesListResponseIn": "_dfareporting_228_PostalCodesListResponseIn",
        "PostalCodesListResponseOut": "_dfareporting_229_PostalCodesListResponseOut",
        "ReportListIn": "_dfareporting_230_ReportListIn",
        "ReportListOut": "_dfareporting_231_ReportListOut",
        "BillingAssignmentIn": "_dfareporting_232_BillingAssignmentIn",
        "BillingAssignmentOut": "_dfareporting_233_BillingAssignmentOut",
        "CreativeRotationIn": "_dfareporting_234_CreativeRotationIn",
        "CreativeRotationOut": "_dfareporting_235_CreativeRotationOut",
        "FloodlightActivitiesListResponseIn": "_dfareporting_236_FloodlightActivitiesListResponseIn",
        "FloodlightActivitiesListResponseOut": "_dfareporting_237_FloodlightActivitiesListResponseOut",
        "PlacementIn": "_dfareporting_238_PlacementIn",
        "PlacementOut": "_dfareporting_239_PlacementOut",
        "OrdersListResponseIn": "_dfareporting_240_OrdersListResponseIn",
        "OrdersListResponseOut": "_dfareporting_241_OrdersListResponseOut",
        "UserRolePermissionsListResponseIn": "_dfareporting_242_UserRolePermissionsListResponseIn",
        "UserRolePermissionsListResponseOut": "_dfareporting_243_UserRolePermissionsListResponseOut",
        "DirectorySitesListResponseIn": "_dfareporting_244_DirectorySitesListResponseIn",
        "DirectorySitesListResponseOut": "_dfareporting_245_DirectorySitesListResponseOut",
        "ChannelGroupingIn": "_dfareporting_246_ChannelGroupingIn",
        "ChannelGroupingOut": "_dfareporting_247_ChannelGroupingOut",
        "SizeIn": "_dfareporting_248_SizeIn",
        "SizeOut": "_dfareporting_249_SizeOut",
        "OffsetPositionIn": "_dfareporting_250_OffsetPositionIn",
        "OffsetPositionOut": "_dfareporting_251_OffsetPositionOut",
        "DirectorySiteIn": "_dfareporting_252_DirectorySiteIn",
        "DirectorySiteOut": "_dfareporting_253_DirectorySiteOut",
        "DfpSettingsIn": "_dfareporting_254_DfpSettingsIn",
        "DfpSettingsOut": "_dfareporting_255_DfpSettingsOut",
        "BillingRateTieredRateIn": "_dfareporting_256_BillingRateTieredRateIn",
        "BillingRateTieredRateOut": "_dfareporting_257_BillingRateTieredRateOut",
        "LanguageIn": "_dfareporting_258_LanguageIn",
        "LanguageOut": "_dfareporting_259_LanguageOut",
        "OptimizationActivityIn": "_dfareporting_260_OptimizationActivityIn",
        "OptimizationActivityOut": "_dfareporting_261_OptimizationActivityOut",
        "CreativeFieldIn": "_dfareporting_262_CreativeFieldIn",
        "CreativeFieldOut": "_dfareporting_263_CreativeFieldOut",
        "PathToConversionReportCompatibleFieldsIn": "_dfareporting_264_PathToConversionReportCompatibleFieldsIn",
        "PathToConversionReportCompatibleFieldsOut": "_dfareporting_265_PathToConversionReportCompatibleFieldsOut",
        "SubaccountsListResponseIn": "_dfareporting_266_SubaccountsListResponseIn",
        "SubaccountsListResponseOut": "_dfareporting_267_SubaccountsListResponseOut",
        "AccountActiveAdSummaryIn": "_dfareporting_268_AccountActiveAdSummaryIn",
        "AccountActiveAdSummaryOut": "_dfareporting_269_AccountActiveAdSummaryOut",
        "DimensionIn": "_dfareporting_270_DimensionIn",
        "DimensionOut": "_dfareporting_271_DimensionOut",
        "UniversalAdIdIn": "_dfareporting_272_UniversalAdIdIn",
        "UniversalAdIdOut": "_dfareporting_273_UniversalAdIdOut",
        "OrderIn": "_dfareporting_274_OrderIn",
        "OrderOut": "_dfareporting_275_OrderOut",
        "EncryptionInfoIn": "_dfareporting_276_EncryptionInfoIn",
        "EncryptionInfoOut": "_dfareporting_277_EncryptionInfoOut",
        "PlacementStrategiesListResponseIn": "_dfareporting_278_PlacementStrategiesListResponseIn",
        "PlacementStrategiesListResponseOut": "_dfareporting_279_PlacementStrategiesListResponseOut",
        "CountryIn": "_dfareporting_280_CountryIn",
        "CountryOut": "_dfareporting_281_CountryOut",
        "ListPopulationClauseIn": "_dfareporting_282_ListPopulationClauseIn",
        "ListPopulationClauseOut": "_dfareporting_283_ListPopulationClauseOut",
        "CityIn": "_dfareporting_284_CityIn",
        "CityOut": "_dfareporting_285_CityOut",
        "SkippableSettingIn": "_dfareporting_286_SkippableSettingIn",
        "SkippableSettingOut": "_dfareporting_287_SkippableSettingOut",
        "EventTagIn": "_dfareporting_288_EventTagIn",
        "EventTagOut": "_dfareporting_289_EventTagOut",
        "ListTargetingExpressionIn": "_dfareporting_290_ListTargetingExpressionIn",
        "ListTargetingExpressionOut": "_dfareporting_291_ListTargetingExpressionOut",
        "CustomFloodlightVariableIn": "_dfareporting_292_CustomFloodlightVariableIn",
        "CustomFloodlightVariableOut": "_dfareporting_293_CustomFloodlightVariableOut",
        "MeasurementPartnerCampaignLinkIn": "_dfareporting_294_MeasurementPartnerCampaignLinkIn",
        "MeasurementPartnerCampaignLinkOut": "_dfareporting_295_MeasurementPartnerCampaignLinkOut",
        "AdvertiserIn": "_dfareporting_296_AdvertiserIn",
        "AdvertiserOut": "_dfareporting_297_AdvertiserOut",
        "EventTagsListResponseIn": "_dfareporting_298_EventTagsListResponseIn",
        "EventTagsListResponseOut": "_dfareporting_299_EventTagsListResponseOut",
        "GeoTargetingIn": "_dfareporting_300_GeoTargetingIn",
        "GeoTargetingOut": "_dfareporting_301_GeoTargetingOut",
        "AccountPermissionsListResponseIn": "_dfareporting_302_AccountPermissionsListResponseIn",
        "AccountPermissionsListResponseOut": "_dfareporting_303_AccountPermissionsListResponseOut",
        "MetricIn": "_dfareporting_304_MetricIn",
        "MetricOut": "_dfareporting_305_MetricOut",
        "LookbackConfigurationIn": "_dfareporting_306_LookbackConfigurationIn",
        "LookbackConfigurationOut": "_dfareporting_307_LookbackConfigurationOut",
        "SiteTranscodeSettingIn": "_dfareporting_308_SiteTranscodeSettingIn",
        "SiteTranscodeSettingOut": "_dfareporting_309_SiteTranscodeSettingOut",
        "AdvertiserInvoicesListResponseIn": "_dfareporting_310_AdvertiserInvoicesListResponseIn",
        "AdvertiserInvoicesListResponseOut": "_dfareporting_311_AdvertiserInvoicesListResponseOut",
        "CampaignSummaryIn": "_dfareporting_312_CampaignSummaryIn",
        "CampaignSummaryOut": "_dfareporting_313_CampaignSummaryOut",
        "InvoiceIn": "_dfareporting_314_InvoiceIn",
        "InvoiceOut": "_dfareporting_315_InvoiceOut",
        "MetrosListResponseIn": "_dfareporting_316_MetrosListResponseIn",
        "MetrosListResponseOut": "_dfareporting_317_MetrosListResponseOut",
        "TagSettingIn": "_dfareporting_318_TagSettingIn",
        "TagSettingOut": "_dfareporting_319_TagSettingOut",
        "CampaignsListResponseIn": "_dfareporting_320_CampaignsListResponseIn",
        "CampaignsListResponseOut": "_dfareporting_321_CampaignsListResponseOut",
        "CreativeCustomEventIn": "_dfareporting_322_CreativeCustomEventIn",
        "CreativeCustomEventOut": "_dfareporting_323_CreativeCustomEventOut",
        "UserRolePermissionIn": "_dfareporting_324_UserRolePermissionIn",
        "UserRolePermissionOut": "_dfareporting_325_UserRolePermissionOut",
        "ObaIconIn": "_dfareporting_326_ObaIconIn",
        "ObaIconOut": "_dfareporting_327_ObaIconOut",
        "PlacementAssignmentIn": "_dfareporting_328_PlacementAssignmentIn",
        "PlacementAssignmentOut": "_dfareporting_329_PlacementAssignmentOut",
        "ConversionStatusIn": "_dfareporting_330_ConversionStatusIn",
        "ConversionStatusOut": "_dfareporting_331_ConversionStatusOut",
        "PlacementStrategyIn": "_dfareporting_332_PlacementStrategyIn",
        "PlacementStrategyOut": "_dfareporting_333_PlacementStrategyOut",
        "ActivitiesIn": "_dfareporting_334_ActivitiesIn",
        "ActivitiesOut": "_dfareporting_335_ActivitiesOut",
        "PathFilterIn": "_dfareporting_336_PathFilterIn",
        "PathFilterOut": "_dfareporting_337_PathFilterOut",
        "ContentCategoryIn": "_dfareporting_338_ContentCategoryIn",
        "ContentCategoryOut": "_dfareporting_339_ContentCategoryOut",
        "AccountPermissionGroupsListResponseIn": "_dfareporting_340_AccountPermissionGroupsListResponseIn",
        "AccountPermissionGroupsListResponseOut": "_dfareporting_341_AccountPermissionGroupsListResponseOut",
        "DayPartTargetingIn": "_dfareporting_342_DayPartTargetingIn",
        "DayPartTargetingOut": "_dfareporting_343_DayPartTargetingOut",
        "SiteCompanionSettingIn": "_dfareporting_344_SiteCompanionSettingIn",
        "SiteCompanionSettingOut": "_dfareporting_345_SiteCompanionSettingOut",
        "AccountPermissionIn": "_dfareporting_346_AccountPermissionIn",
        "AccountPermissionOut": "_dfareporting_347_AccountPermissionOut",
        "AudienceSegmentGroupIn": "_dfareporting_348_AudienceSegmentGroupIn",
        "AudienceSegmentGroupOut": "_dfareporting_349_AudienceSegmentGroupOut",
        "RemarketingListShareIn": "_dfareporting_350_RemarketingListShareIn",
        "RemarketingListShareOut": "_dfareporting_351_RemarketingListShareOut",
        "AudienceSegmentIn": "_dfareporting_352_AudienceSegmentIn",
        "AudienceSegmentOut": "_dfareporting_353_AudienceSegmentOut",
        "EventTagOverrideIn": "_dfareporting_354_EventTagOverrideIn",
        "EventTagOverrideOut": "_dfareporting_355_EventTagOverrideOut",
        "CreativeAssetSelectionIn": "_dfareporting_356_CreativeAssetSelectionIn",
        "CreativeAssetSelectionOut": "_dfareporting_357_CreativeAssetSelectionOut",
        "FloodlightActivityDynamicTagIn": "_dfareporting_358_FloodlightActivityDynamicTagIn",
        "FloodlightActivityDynamicTagOut": "_dfareporting_359_FloodlightActivityDynamicTagOut",
        "MobileCarrierIn": "_dfareporting_360_MobileCarrierIn",
        "MobileCarrierOut": "_dfareporting_361_MobileCarrierOut",
        "ListPopulationRuleIn": "_dfareporting_362_ListPopulationRuleIn",
        "ListPopulationRuleOut": "_dfareporting_363_ListPopulationRuleOut",
        "MobileCarriersListResponseIn": "_dfareporting_364_MobileCarriersListResponseIn",
        "MobileCarriersListResponseOut": "_dfareporting_365_MobileCarriersListResponseOut",
        "UserRoleIn": "_dfareporting_366_UserRoleIn",
        "UserRoleOut": "_dfareporting_367_UserRoleOut",
        "AccountsListResponseIn": "_dfareporting_368_AccountsListResponseIn",
        "AccountsListResponseOut": "_dfareporting_369_AccountsListResponseOut",
        "TargetableRemarketingListsListResponseIn": "_dfareporting_370_TargetableRemarketingListsListResponseIn",
        "TargetableRemarketingListsListResponseOut": "_dfareporting_371_TargetableRemarketingListsListResponseOut",
        "SiteVideoSettingsIn": "_dfareporting_372_SiteVideoSettingsIn",
        "SiteVideoSettingsOut": "_dfareporting_373_SiteVideoSettingsOut",
        "OrderContactIn": "_dfareporting_374_OrderContactIn",
        "OrderContactOut": "_dfareporting_375_OrderContactOut",
        "PricingIn": "_dfareporting_376_PricingIn",
        "PricingOut": "_dfareporting_377_PricingOut",
        "MobileAppsListResponseIn": "_dfareporting_378_MobileAppsListResponseIn",
        "MobileAppsListResponseOut": "_dfareporting_379_MobileAppsListResponseOut",
        "UserIdentifierIn": "_dfareporting_380_UserIdentifierIn",
        "UserIdentifierOut": "_dfareporting_381_UserIdentifierOut",
        "KeyValueTargetingExpressionIn": "_dfareporting_382_KeyValueTargetingExpressionIn",
        "KeyValueTargetingExpressionOut": "_dfareporting_383_KeyValueTargetingExpressionOut",
        "PlatformTypesListResponseIn": "_dfareporting_384_PlatformTypesListResponseIn",
        "PlatformTypesListResponseOut": "_dfareporting_385_PlatformTypesListResponseOut",
        "FlightIn": "_dfareporting_386_FlightIn",
        "FlightOut": "_dfareporting_387_FlightOut",
        "RegionsListResponseIn": "_dfareporting_388_RegionsListResponseIn",
        "RegionsListResponseOut": "_dfareporting_389_RegionsListResponseOut",
        "CampaignCreativeAssociationIn": "_dfareporting_390_CampaignCreativeAssociationIn",
        "CampaignCreativeAssociationOut": "_dfareporting_391_CampaignCreativeAssociationOut",
        "DeepLinkIn": "_dfareporting_392_DeepLinkIn",
        "DeepLinkOut": "_dfareporting_393_DeepLinkOut",
        "CompanionSettingIn": "_dfareporting_394_CompanionSettingIn",
        "CompanionSettingOut": "_dfareporting_395_CompanionSettingOut",
        "SitesListResponseIn": "_dfareporting_396_SitesListResponseIn",
        "SitesListResponseOut": "_dfareporting_397_SitesListResponseOut",
        "ProjectIn": "_dfareporting_398_ProjectIn",
        "ProjectOut": "_dfareporting_399_ProjectOut",
        "ListPopulationTermIn": "_dfareporting_400_ListPopulationTermIn",
        "ListPopulationTermOut": "_dfareporting_401_ListPopulationTermOut",
        "OmnitureSettingsIn": "_dfareporting_402_OmnitureSettingsIn",
        "OmnitureSettingsOut": "_dfareporting_403_OmnitureSettingsOut",
        "DimensionValueListIn": "_dfareporting_404_DimensionValueListIn",
        "DimensionValueListOut": "_dfareporting_405_DimensionValueListOut",
        "VideoFormatIn": "_dfareporting_406_VideoFormatIn",
        "VideoFormatOut": "_dfareporting_407_VideoFormatOut",
        "CampaignIn": "_dfareporting_408_CampaignIn",
        "CampaignOut": "_dfareporting_409_CampaignOut",
        "RegionIn": "_dfareporting_410_RegionIn",
        "RegionOut": "_dfareporting_411_RegionOut",
        "PathReportDimensionValueIn": "_dfareporting_412_PathReportDimensionValueIn",
        "PathReportDimensionValueOut": "_dfareporting_413_PathReportDimensionValueOut",
        "AdSlotIn": "_dfareporting_414_AdSlotIn",
        "AdSlotOut": "_dfareporting_415_AdSlotOut",
        "MobileAppIn": "_dfareporting_416_MobileAppIn",
        "MobileAppOut": "_dfareporting_417_MobileAppOut",
        "FloodlightActivitiesGenerateTagResponseIn": "_dfareporting_418_FloodlightActivitiesGenerateTagResponseIn",
        "FloodlightActivitiesGenerateTagResponseOut": "_dfareporting_419_FloodlightActivitiesGenerateTagResponseOut",
        "AdBlockingConfigurationIn": "_dfareporting_420_AdBlockingConfigurationIn",
        "AdBlockingConfigurationOut": "_dfareporting_421_AdBlockingConfigurationOut",
        "LastModifiedInfoIn": "_dfareporting_422_LastModifiedInfoIn",
        "LastModifiedInfoOut": "_dfareporting_423_LastModifiedInfoOut",
        "BillingAssignmentsListResponseIn": "_dfareporting_424_BillingAssignmentsListResponseIn",
        "BillingAssignmentsListResponseOut": "_dfareporting_425_BillingAssignmentsListResponseOut",
        "AccountUserProfilesListResponseIn": "_dfareporting_426_AccountUserProfilesListResponseIn",
        "AccountUserProfilesListResponseOut": "_dfareporting_427_AccountUserProfilesListResponseOut",
        "TagSettingsIn": "_dfareporting_428_TagSettingsIn",
        "TagSettingsOut": "_dfareporting_429_TagSettingsOut",
        "ConversionsBatchUpdateResponseIn": "_dfareporting_430_ConversionsBatchUpdateResponseIn",
        "ConversionsBatchUpdateResponseOut": "_dfareporting_431_ConversionsBatchUpdateResponseOut",
        "MeasurementPartnerAdvertiserLinkIn": "_dfareporting_432_MeasurementPartnerAdvertiserLinkIn",
        "MeasurementPartnerAdvertiserLinkOut": "_dfareporting_433_MeasurementPartnerAdvertiserLinkOut",
        "FloodlightActivityPublisherDynamicTagIn": "_dfareporting_434_FloodlightActivityPublisherDynamicTagIn",
        "FloodlightActivityPublisherDynamicTagOut": "_dfareporting_435_FloodlightActivityPublisherDynamicTagOut",
        "ClickTagIn": "_dfareporting_436_ClickTagIn",
        "ClickTagOut": "_dfareporting_437_ClickTagOut",
        "TranscodeSettingIn": "_dfareporting_438_TranscodeSettingIn",
        "TranscodeSettingOut": "_dfareporting_439_TranscodeSettingOut",
        "AccountIn": "_dfareporting_440_AccountIn",
        "AccountOut": "_dfareporting_441_AccountOut",
        "CreativesListResponseIn": "_dfareporting_442_CreativesListResponseIn",
        "CreativesListResponseOut": "_dfareporting_443_CreativesListResponseOut",
        "ThirdPartyTrackingUrlIn": "_dfareporting_444_ThirdPartyTrackingUrlIn",
        "ThirdPartyTrackingUrlOut": "_dfareporting_445_ThirdPartyTrackingUrlOut",
        "FsCommandIn": "_dfareporting_446_FsCommandIn",
        "FsCommandOut": "_dfareporting_447_FsCommandOut",
        "ReachReportCompatibleFieldsIn": "_dfareporting_448_ReachReportCompatibleFieldsIn",
        "ReachReportCompatibleFieldsOut": "_dfareporting_449_ReachReportCompatibleFieldsOut",
        "ConnectionTypeIn": "_dfareporting_450_ConnectionTypeIn",
        "ConnectionTypeOut": "_dfareporting_451_ConnectionTypeOut",
        "FloodlightActivityGroupsListResponseIn": "_dfareporting_452_FloodlightActivityGroupsListResponseIn",
        "FloodlightActivityGroupsListResponseOut": "_dfareporting_453_FloodlightActivityGroupsListResponseOut",
        "PlacementsListResponseIn": "_dfareporting_454_PlacementsListResponseIn",
        "PlacementsListResponseOut": "_dfareporting_455_PlacementsListResponseOut",
        "AccountPermissionGroupIn": "_dfareporting_456_AccountPermissionGroupIn",
        "AccountPermissionGroupOut": "_dfareporting_457_AccountPermissionGroupOut",
        "DirectorySiteSettingsIn": "_dfareporting_458_DirectorySiteSettingsIn",
        "DirectorySiteSettingsOut": "_dfareporting_459_DirectorySiteSettingsOut",
        "RichMediaExitOverrideIn": "_dfareporting_460_RichMediaExitOverrideIn",
        "RichMediaExitOverrideOut": "_dfareporting_461_RichMediaExitOverrideOut",
        "OperatingSystemVersionIn": "_dfareporting_462_OperatingSystemVersionIn",
        "OperatingSystemVersionOut": "_dfareporting_463_OperatingSystemVersionOut",
        "CitiesListResponseIn": "_dfareporting_464_CitiesListResponseIn",
        "CitiesListResponseOut": "_dfareporting_465_CitiesListResponseOut",
        "CompanionClickThroughOverrideIn": "_dfareporting_466_CompanionClickThroughOverrideIn",
        "CompanionClickThroughOverrideOut": "_dfareporting_467_CompanionClickThroughOverrideOut",
        "ChangeLogsListResponseIn": "_dfareporting_468_ChangeLogsListResponseIn",
        "ChangeLogsListResponseOut": "_dfareporting_469_ChangeLogsListResponseOut",
        "PathReportCompatibleFieldsIn": "_dfareporting_470_PathReportCompatibleFieldsIn",
        "PathReportCompatibleFieldsOut": "_dfareporting_471_PathReportCompatibleFieldsOut",
        "UserDefinedVariableConfigurationIn": "_dfareporting_472_UserDefinedVariableConfigurationIn",
        "UserDefinedVariableConfigurationOut": "_dfareporting_473_UserDefinedVariableConfigurationOut",
        "TargetingTemplatesListResponseIn": "_dfareporting_474_TargetingTemplatesListResponseIn",
        "TargetingTemplatesListResponseOut": "_dfareporting_475_TargetingTemplatesListResponseOut",
        "SiteSkippableSettingIn": "_dfareporting_476_SiteSkippableSettingIn",
        "SiteSkippableSettingOut": "_dfareporting_477_SiteSkippableSettingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DeliveryScheduleIn"] = t.struct(
        {
            "priority": t.string().optional(),
            "impressionRatio": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]).optional(),
            "hardCutoff": t.boolean().optional(),
        }
    ).named(renames["DeliveryScheduleIn"])
    types["DeliveryScheduleOut"] = t.struct(
        {
            "priority": t.string().optional(),
            "impressionRatio": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]).optional(),
            "hardCutoff": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryScheduleOut"])
    types["TargetingTemplateIn"] = t.struct(
        {
            "keyValueTargetingExpression": t.proxy(
                renames["KeyValueTargetingExpressionIn"]
            ).optional(),
            "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
            "listTargetingExpression": t.proxy(
                renames["ListTargetingExpressionIn"]
            ).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "technologyTargeting": t.proxy(renames["TechnologyTargetingIn"]).optional(),
            "advertiserId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
        }
    ).named(renames["TargetingTemplateIn"])
    types["TargetingTemplateOut"] = t.struct(
        {
            "keyValueTargetingExpression": t.proxy(
                renames["KeyValueTargetingExpressionOut"]
            ).optional(),
            "geoTargeting": t.proxy(renames["GeoTargetingOut"]).optional(),
            "listTargetingExpression": t.proxy(
                renames["ListTargetingExpressionOut"]
            ).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "dayPartTargeting": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingTemplateOut"])
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
    types["FileListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["FileIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["FileListIn"])
    types["FileListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["FileOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileListOut"])
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
    types["ObjectFilterIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "objectIds": t.array(t.string()).optional(),
        }
    ).named(renames["ObjectFilterIn"])
    types["ObjectFilterOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "objectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectFilterOut"])
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
    types["CreativeGroupAssignmentIn"] = t.struct(
        {
            "creativeGroupId": t.string().optional(),
            "creativeGroupNumber": t.string().optional(),
        }
    ).named(renames["CreativeGroupAssignmentIn"])
    types["CreativeGroupAssignmentOut"] = t.struct(
        {
            "creativeGroupId": t.string().optional(),
            "creativeGroupNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeGroupAssignmentOut"])
    types["DimensionValueRequestIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "dimensionName": t.string().optional(),
            "endDate": t.string(),
            "filters": t.array(t.proxy(renames["DimensionFilterIn"])).optional(),
            "startDate": t.string(),
        }
    ).named(renames["DimensionValueRequestIn"])
    types["DimensionValueRequestOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "dimensionName": t.string().optional(),
            "endDate": t.string(),
            "filters": t.array(t.proxy(renames["DimensionFilterOut"])).optional(),
            "startDate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueRequestOut"])
    types["ConversionErrorIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "message": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ConversionErrorIn"])
    types["ConversionErrorOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "message": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionErrorOut"])
    types["OperatingSystemIn"] = t.struct(
        {
            "desktop": t.boolean().optional(),
            "mobile": t.boolean().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "dartId": t.string().optional(),
        }
    ).named(renames["OperatingSystemIn"])
    types["OperatingSystemOut"] = t.struct(
        {
            "desktop": t.boolean().optional(),
            "mobile": t.boolean().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "dartId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemOut"])
    types["CreativeFieldsListResponseIn"] = t.struct(
        {
            "creativeFields": t.array(t.proxy(renames["CreativeFieldIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CreativeFieldsListResponseIn"])
    types["CreativeFieldsListResponseOut"] = t.struct(
        {
            "creativeFields": t.array(t.proxy(renames["CreativeFieldOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldsListResponseOut"])
    types["MeasurementPartnerWrappingDataIn"] = t.struct(
        {
            "tagWrappingMode": t.string().optional(),
            "linkStatus": t.string().optional(),
            "wrappedTag": t.string().optional(),
            "measurementPartner": t.string().optional(),
        }
    ).named(renames["MeasurementPartnerWrappingDataIn"])
    types["MeasurementPartnerWrappingDataOut"] = t.struct(
        {
            "tagWrappingMode": t.string().optional(),
            "linkStatus": t.string().optional(),
            "wrappedTag": t.string().optional(),
            "measurementPartner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeasurementPartnerWrappingDataOut"])
    types["FileIn"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "lastModifiedTime": t.string().optional(),
            "fileName": t.string().optional(),
            "reportId": t.string().optional(),
            "etag": t.string().optional(),
            "format": t.string().optional(),
            "urls": t.struct(
                {"apiUrl": t.string().optional(), "browserUrl": t.string().optional()}
            ).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "lastModifiedTime": t.string().optional(),
            "fileName": t.string().optional(),
            "reportId": t.string().optional(),
            "etag": t.string().optional(),
            "format": t.string().optional(),
            "urls": t.struct(
                {"apiUrl": t.string().optional(), "browserUrl": t.string().optional()}
            ).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["OperatingSystemsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "operatingSystems": t.array(
                t.proxy(renames["OperatingSystemIn"])
            ).optional(),
        }
    ).named(renames["OperatingSystemsListResponseIn"])
    types["OperatingSystemsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "operatingSystems": t.array(
                t.proxy(renames["OperatingSystemOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemsListResponseOut"])
    types["AccountUserProfileIn"] = t.struct(
        {
            "siteFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
            "comments": t.string().optional(),
            "accountId": t.string().optional(),
            "userRoleFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
            "name": t.string().optional(),
            "active": t.boolean().optional(),
            "userAccessType": t.string().optional(),
            "kind": t.string().optional(),
            "email": t.string().optional(),
            "id": t.string().optional(),
            "locale": t.string().optional(),
            "advertiserFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
            "traffickerType": t.string().optional(),
            "userRoleId": t.string().optional(),
            "campaignFilter": t.proxy(renames["ObjectFilterIn"]).optional(),
            "subaccountId": t.string().optional(),
        }
    ).named(renames["AccountUserProfileIn"])
    types["AccountUserProfileOut"] = t.struct(
        {
            "siteFilter": t.proxy(renames["ObjectFilterOut"]).optional(),
            "comments": t.string().optional(),
            "accountId": t.string().optional(),
            "userRoleFilter": t.proxy(renames["ObjectFilterOut"]).optional(),
            "name": t.string().optional(),
            "active": t.boolean().optional(),
            "userAccessType": t.string().optional(),
            "kind": t.string().optional(),
            "email": t.string().optional(),
            "id": t.string().optional(),
            "locale": t.string().optional(),
            "advertiserFilter": t.proxy(renames["ObjectFilterOut"]).optional(),
            "traffickerType": t.string().optional(),
            "userRoleId": t.string().optional(),
            "campaignFilter": t.proxy(renames["ObjectFilterOut"]).optional(),
            "subaccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountUserProfileOut"])
    types["CustomViewabilityMetricConfigurationIn"] = t.struct(
        {
            "viewabilityPercent": t.integer().optional(),
            "timePercent": t.integer().optional(),
            "timeMillis": t.integer().optional(),
            "audible": t.boolean().optional(),
        }
    ).named(renames["CustomViewabilityMetricConfigurationIn"])
    types["CustomViewabilityMetricConfigurationOut"] = t.struct(
        {
            "viewabilityPercent": t.integer().optional(),
            "timePercent": t.integer().optional(),
            "timeMillis": t.integer().optional(),
            "audible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomViewabilityMetricConfigurationOut"])
    types["ChannelGroupingRuleIn"] = t.struct(
        {
            "disjunctiveMatchStatements": t.array(
                t.proxy(renames["DisjunctiveMatchStatementIn"])
            ).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ChannelGroupingRuleIn"])
    types["ChannelGroupingRuleOut"] = t.struct(
        {
            "disjunctiveMatchStatements": t.array(
                t.proxy(renames["DisjunctiveMatchStatementOut"])
            ).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelGroupingRuleOut"])
    types["MetroIn"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "name": t.string().optional(),
            "dartId": t.string().optional(),
            "kind": t.string().optional(),
            "dmaId": t.string().optional(),
            "metroCode": t.string().optional(),
            "countryDartId": t.string().optional(),
        }
    ).named(renames["MetroIn"])
    types["MetroOut"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "name": t.string().optional(),
            "dartId": t.string().optional(),
            "kind": t.string().optional(),
            "dmaId": t.string().optional(),
            "metroCode": t.string().optional(),
            "countryDartId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetroOut"])
    types["CreativeAssetMetadataIn"] = t.struct(
        {
            "counterCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "kind": t.string().optional(),
            "timerCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "detectedFeatures": t.array(t.string()).optional(),
            "exitCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "id": t.string().optional(),
            "richMedia": t.boolean().optional(),
            "warnedValidationRules": t.array(t.string()).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "assetIdentifier": t.proxy(renames["CreativeAssetIdIn"]).optional(),
            "clickTags": t.array(t.proxy(renames["ClickTagIn"])).optional(),
        }
    ).named(renames["CreativeAssetMetadataIn"])
    types["CreativeAssetMetadataOut"] = t.struct(
        {
            "counterCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "kind": t.string().optional(),
            "timerCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "detectedFeatures": t.array(t.string()).optional(),
            "exitCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "id": t.string().optional(),
            "richMedia": t.boolean().optional(),
            "warnedValidationRules": t.array(t.string()).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "assetIdentifier": t.proxy(renames["CreativeAssetIdOut"]).optional(),
            "clickTags": t.array(t.proxy(renames["ClickTagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeAssetMetadataOut"])
    types["ProjectsListResponseIn"] = t.struct(
        {
            "projects": t.array(t.proxy(renames["ProjectIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ProjectsListResponseIn"])
    types["ProjectsListResponseOut"] = t.struct(
        {
            "projects": t.array(t.proxy(renames["ProjectOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectsListResponseOut"])
    types["PopupWindowPropertiesIn"] = t.struct(
        {
            "dimension": t.proxy(renames["SizeIn"]).optional(),
            "showAddressBar": t.boolean().optional(),
            "positionType": t.string().optional(),
            "title": t.string().optional(),
            "showScrollBar": t.boolean().optional(),
            "showToolBar": t.boolean().optional(),
            "showMenuBar": t.boolean().optional(),
            "showStatusBar": t.boolean().optional(),
            "offset": t.proxy(renames["OffsetPositionIn"]).optional(),
        }
    ).named(renames["PopupWindowPropertiesIn"])
    types["PopupWindowPropertiesOut"] = t.struct(
        {
            "dimension": t.proxy(renames["SizeOut"]).optional(),
            "showAddressBar": t.boolean().optional(),
            "positionType": t.string().optional(),
            "title": t.string().optional(),
            "showScrollBar": t.boolean().optional(),
            "showToolBar": t.boolean().optional(),
            "showMenuBar": t.boolean().optional(),
            "showStatusBar": t.boolean().optional(),
            "offset": t.proxy(renames["OffsetPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PopupWindowPropertiesOut"])
    types["VideoSettingsIn"] = t.struct(
        {
            "durationSeconds": t.integer().optional(),
            "orientation": t.string().optional(),
            "skippableSettings": t.proxy(renames["SkippableSettingIn"]).optional(),
            "companionSettings": t.proxy(renames["CompanionSettingIn"]).optional(),
            "publisherSpecificationId": t.string().optional(),
            "obaSettings": t.proxy(renames["ObaIconIn"]).optional(),
            "transcodeSettings": t.proxy(renames["TranscodeSettingIn"]).optional(),
            "kind": t.string().optional(),
            "obaEnabled": t.boolean().optional(),
        }
    ).named(renames["VideoSettingsIn"])
    types["VideoSettingsOut"] = t.struct(
        {
            "durationSeconds": t.integer().optional(),
            "orientation": t.string().optional(),
            "skippableSettings": t.proxy(renames["SkippableSettingOut"]).optional(),
            "companionSettings": t.proxy(renames["CompanionSettingOut"]).optional(),
            "publisherSpecificationId": t.string().optional(),
            "obaSettings": t.proxy(renames["ObaIconOut"]).optional(),
            "transcodeSettings": t.proxy(renames["TranscodeSettingOut"]).optional(),
            "kind": t.string().optional(),
            "obaEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoSettingsOut"])
    types["CampaignCreativeAssociationsListResponseIn"] = t.struct(
        {
            "campaignCreativeAssociations": t.array(
                t.proxy(renames["CampaignCreativeAssociationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CampaignCreativeAssociationsListResponseIn"])
    types["CampaignCreativeAssociationsListResponseOut"] = t.struct(
        {
            "campaignCreativeAssociations": t.array(
                t.proxy(renames["CampaignCreativeAssociationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignCreativeAssociationsListResponseOut"])
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
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "userRoles": t.array(t.proxy(renames["UserRoleIn"])).optional(),
        }
    ).named(renames["UserRolesListResponseIn"])
    types["UserRolesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "userRoles": t.array(t.proxy(renames["UserRoleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRolesListResponseOut"])
    types["ReportIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "schedule": t.struct(
                {
                    "repeatsOnWeekDays": t.array(t.string()).optional(),
                    "every": t.integer().optional(),
                    "active": t.boolean().optional(),
                    "repeats": t.string().optional(),
                    "startDate": t.string(),
                    "timezone": t.string().optional(),
                    "runsOnDayOfMonth": t.string().optional(),
                    "expirationDate": t.string(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "format": t.string().optional(),
            "name": t.string().optional(),
            "criteria": t.struct(
                {
                    "customRichMediaEvents": t.proxy(
                        renames["CustomRichMediaEventsIn"]
                    ).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "pathCriteria": t.struct(
                {
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "customChannelGrouping": t.proxy(
                        renames["ChannelGroupingIn"]
                    ).optional(),
                    "pathFilters": t.array(t.proxy(renames["PathFilterIn"])).optional(),
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueIn"]
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "fileName": t.string().optional(),
            "ownerProfileId": t.string().optional(),
            "subAccountId": t.string().optional(),
            "floodlightCriteria": t.struct(
                {
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "reportProperties": t.struct(
                        {
                            "includeAttributedIPConversions": t.boolean().optional(),
                            "includeUnattributedCookieConversions": t.boolean().optional(),
                            "includeUnattributedIPConversions": t.boolean().optional(),
                        }
                    ).optional(),
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueIn"]
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "customRichMediaEvents": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                }
            ).optional(),
            "delivery": t.struct(
                {
                    "emailOwner": t.boolean().optional(),
                    "recipients": t.array(t.proxy(renames["RecipientIn"])).optional(),
                    "message": t.string().optional(),
                    "emailOwnerDeliveryType": t.string().optional(),
                }
            ).optional(),
            "type": t.string().optional(),
            "pathAttributionCriteria": t.struct(
                {
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueIn"]
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "customChannelGrouping": t.proxy(
                        renames["ChannelGroupingIn"]
                    ).optional(),
                    "pathFilters": t.array(t.proxy(renames["PathFilterIn"])).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                }
            ).optional(),
            "crossDimensionReachCriteria": t.struct(
                {
                    "breakdown": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "pivoted": t.boolean().optional(),
                    "overlapMetricNames": t.array(t.string()).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "dimension": t.string().optional(),
                }
            ).optional(),
            "reachCriteria": t.struct(
                {
                    "customRichMediaEvents": t.proxy(
                        renames["CustomRichMediaEventsIn"]
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "enableAllDimensionCombinations": t.boolean().optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                }
            ).optional(),
            "etag": t.string().optional(),
            "pathToConversionCriteria": t.struct(
                {
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueIn"]
                    ).optional(),
                    "customRichMediaEvents": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    "perInteractionDimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "customFloodlightVariables": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "reportProperties": t.struct(
                        {
                            "maximumInteractionGap": t.integer().optional(),
                            "includeUnattributedCookieConversions": t.boolean().optional(),
                            "maximumImpressionInteractions": t.integer().optional(),
                            "includeAttributedIPConversions": t.boolean().optional(),
                            "clicksLookbackWindow": t.integer().optional(),
                            "impressionsLookbackWindow": t.integer().optional(),
                            "includeUnattributedIPConversions": t.boolean().optional(),
                            "maximumClickInteractions": t.integer().optional(),
                            "pivotOnInteractionPath": t.boolean().optional(),
                        }
                    ).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueIn"])
                    ).optional(),
                    "conversionDimensions": t.array(
                        t.proxy(renames["SortedDimensionIn"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "schedule": t.struct(
                {
                    "repeatsOnWeekDays": t.array(t.string()).optional(),
                    "every": t.integer().optional(),
                    "active": t.boolean().optional(),
                    "repeats": t.string().optional(),
                    "startDate": t.string(),
                    "timezone": t.string().optional(),
                    "runsOnDayOfMonth": t.string().optional(),
                    "expirationDate": t.string(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "format": t.string().optional(),
            "name": t.string().optional(),
            "criteria": t.struct(
                {
                    "customRichMediaEvents": t.proxy(
                        renames["CustomRichMediaEventsOut"]
                    ).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "activities": t.proxy(renames["ActivitiesOut"]).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "pathCriteria": t.struct(
                {
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "customChannelGrouping": t.proxy(
                        renames["ChannelGroupingOut"]
                    ).optional(),
                    "pathFilters": t.array(
                        t.proxy(renames["PathFilterOut"])
                    ).optional(),
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueOut"]
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "fileName": t.string().optional(),
            "ownerProfileId": t.string().optional(),
            "subAccountId": t.string().optional(),
            "floodlightCriteria": t.struct(
                {
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "reportProperties": t.struct(
                        {
                            "includeAttributedIPConversions": t.boolean().optional(),
                            "includeUnattributedCookieConversions": t.boolean().optional(),
                            "includeUnattributedIPConversions": t.boolean().optional(),
                        }
                    ).optional(),
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueOut"]
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "customRichMediaEvents": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                }
            ).optional(),
            "delivery": t.struct(
                {
                    "emailOwner": t.boolean().optional(),
                    "recipients": t.array(t.proxy(renames["RecipientOut"])).optional(),
                    "message": t.string().optional(),
                    "emailOwnerDeliveryType": t.string().optional(),
                }
            ).optional(),
            "type": t.string().optional(),
            "pathAttributionCriteria": t.struct(
                {
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueOut"]
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "customChannelGrouping": t.proxy(
                        renames["ChannelGroupingOut"]
                    ).optional(),
                    "pathFilters": t.array(
                        t.proxy(renames["PathFilterOut"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                }
            ).optional(),
            "crossDimensionReachCriteria": t.struct(
                {
                    "breakdown": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "pivoted": t.boolean().optional(),
                    "overlapMetricNames": t.array(t.string()).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "dimension": t.string().optional(),
                }
            ).optional(),
            "reachCriteria": t.struct(
                {
                    "customRichMediaEvents": t.proxy(
                        renames["CustomRichMediaEventsOut"]
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                    "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                    "dimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "activities": t.proxy(renames["ActivitiesOut"]).optional(),
                    "dimensionFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "enableAllDimensionCombinations": t.boolean().optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                }
            ).optional(),
            "etag": t.string().optional(),
            "pathToConversionCriteria": t.struct(
                {
                    "floodlightConfigId": t.proxy(
                        renames["DimensionValueOut"]
                    ).optional(),
                    "customRichMediaEvents": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
                    "perInteractionDimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "customFloodlightVariables": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "reportProperties": t.struct(
                        {
                            "maximumInteractionGap": t.integer().optional(),
                            "includeUnattributedCookieConversions": t.boolean().optional(),
                            "maximumImpressionInteractions": t.integer().optional(),
                            "includeAttributedIPConversions": t.boolean().optional(),
                            "clicksLookbackWindow": t.integer().optional(),
                            "impressionsLookbackWindow": t.integer().optional(),
                            "includeUnattributedIPConversions": t.boolean().optional(),
                            "maximumClickInteractions": t.integer().optional(),
                            "pivotOnInteractionPath": t.boolean().optional(),
                        }
                    ).optional(),
                    "activityFilters": t.array(
                        t.proxy(renames["DimensionValueOut"])
                    ).optional(),
                    "conversionDimensions": t.array(
                        t.proxy(renames["SortedDimensionOut"])
                    ).optional(),
                    "metricNames": t.array(t.string()).optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["PlacementGroupsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "placementGroups": t.array(t.proxy(renames["PlacementGroupIn"])).optional(),
        }
    ).named(renames["PlacementGroupsListResponseIn"])
    types["PlacementGroupsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "placementGroups": t.array(
                t.proxy(renames["PlacementGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementGroupsListResponseOut"])
    types["CreativeGroupsListResponseIn"] = t.struct(
        {
            "creativeGroups": t.array(t.proxy(renames["CreativeGroupIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CreativeGroupsListResponseIn"])
    types["CreativeGroupsListResponseOut"] = t.struct(
        {
            "creativeGroups": t.array(t.proxy(renames["CreativeGroupOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeGroupsListResponseOut"])
    types["AdsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "ads": t.array(t.proxy(renames["AdIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AdsListResponseIn"])
    types["AdsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "ads": t.array(t.proxy(renames["AdOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdsListResponseOut"])
    types["FloodlightActivityIn"] = t.struct(
        {
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "expectedUrl": t.string().optional(),
            "floodlightActivityGroupName": t.string().optional(),
            "publisherTags": t.array(
                t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
            ).optional(),
            "accountId": t.string().optional(),
            "floodlightTagType": t.string().optional(),
            "notes": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "secure": t.boolean().optional(),
            "sslCompliant": t.boolean().optional(),
            "floodlightActivityGroupType": t.string().optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "cacheBustingType": t.string().optional(),
            "userDefinedVariableTypes": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "countingMethod": t.string().optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "floodlightActivityGroupTagString": t.string().optional(),
            "tagString": t.string().optional(),
            "tagFormat": t.string().optional(),
            "attributionEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "floodlightActivityGroupId": t.string().optional(),
            "defaultTags": t.array(
                t.proxy(renames["FloodlightActivityDynamicTagIn"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "sslRequired": t.boolean().optional(),
        }
    ).named(renames["FloodlightActivityIn"])
    types["FloodlightActivityOut"] = t.struct(
        {
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "expectedUrl": t.string().optional(),
            "floodlightActivityGroupName": t.string().optional(),
            "publisherTags": t.array(
                t.proxy(renames["FloodlightActivityPublisherDynamicTagOut"])
            ).optional(),
            "accountId": t.string().optional(),
            "floodlightTagType": t.string().optional(),
            "notes": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "secure": t.boolean().optional(),
            "sslCompliant": t.boolean().optional(),
            "floodlightActivityGroupType": t.string().optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "cacheBustingType": t.string().optional(),
            "userDefinedVariableTypes": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "countingMethod": t.string().optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "floodlightActivityGroupTagString": t.string().optional(),
            "tagString": t.string().optional(),
            "tagFormat": t.string().optional(),
            "attributionEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "floodlightActivityGroupId": t.string().optional(),
            "defaultTags": t.array(
                t.proxy(renames["FloodlightActivityDynamicTagOut"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "sslRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivityOut"])
    types["VideoOffsetIn"] = t.struct(
        {
            "offsetSeconds": t.integer().optional(),
            "offsetPercentage": t.integer().optional(),
        }
    ).named(renames["VideoOffsetIn"])
    types["VideoOffsetOut"] = t.struct(
        {
            "offsetSeconds": t.integer().optional(),
            "offsetPercentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOffsetOut"])
    types["SubaccountIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "availablePermissionIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SubaccountIn"])
    types["SubaccountOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "availablePermissionIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubaccountOut"])
    types["FloodlightConfigurationIn"] = t.struct(
        {
            "analyticsDataSharingEnabled": t.boolean().optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationIn"]
            ).optional(),
            "accountId": t.string().optional(),
            "inAppAttributionTrackingEnabled": t.boolean().optional(),
            "id": t.string().optional(),
            "advertiserId": t.string().optional(),
            "userDefinedVariableConfigurations": t.array(
                t.proxy(renames["UserDefinedVariableConfigurationIn"])
            ).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "customViewabilityMetric": t.proxy(
                renames["CustomViewabilityMetricIn"]
            ).optional(),
            "exposureToConversionEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "tagSettings": t.proxy(renames["TagSettingsIn"]).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "subaccountId": t.string().optional(),
            "firstDayOfWeek": t.string(),
            "omnitureSettings": t.proxy(renames["OmnitureSettingsIn"]).optional(),
            "thirdPartyAuthenticationTokens": t.array(
                t.proxy(renames["ThirdPartyAuthenticationTokenIn"])
            ).optional(),
            "naturalSearchConversionAttributionOption": t.string().optional(),
        }
    ).named(renames["FloodlightConfigurationIn"])
    types["FloodlightConfigurationOut"] = t.struct(
        {
            "analyticsDataSharingEnabled": t.boolean().optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationOut"]
            ).optional(),
            "accountId": t.string().optional(),
            "inAppAttributionTrackingEnabled": t.boolean().optional(),
            "id": t.string().optional(),
            "advertiserId": t.string().optional(),
            "userDefinedVariableConfigurations": t.array(
                t.proxy(renames["UserDefinedVariableConfigurationOut"])
            ).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "customViewabilityMetric": t.proxy(
                renames["CustomViewabilityMetricOut"]
            ).optional(),
            "exposureToConversionEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "tagSettings": t.proxy(renames["TagSettingsOut"]).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "subaccountId": t.string().optional(),
            "firstDayOfWeek": t.string(),
            "omnitureSettings": t.proxy(renames["OmnitureSettingsOut"]).optional(),
            "thirdPartyAuthenticationTokens": t.array(
                t.proxy(renames["ThirdPartyAuthenticationTokenOut"])
            ).optional(),
            "naturalSearchConversionAttributionOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightConfigurationOut"])
    types["RecipientIn"] = t.struct(
        {
            "email": t.string().optional(),
            "kind": t.string().optional(),
            "deliveryType": t.string().optional(),
        }
    ).named(renames["RecipientIn"])
    types["RecipientOut"] = t.struct(
        {
            "email": t.string().optional(),
            "kind": t.string().optional(),
            "deliveryType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipientOut"])
    types["CreativeGroupIn"] = t.struct(
        {
            "groupNumber": t.integer().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
        }
    ).named(renames["CreativeGroupIn"])
    types["CreativeGroupOut"] = t.struct(
        {
            "groupNumber": t.integer().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeGroupOut"])
    types["InventoryItemsListResponseIn"] = t.struct(
        {
            "inventoryItems": t.array(t.proxy(renames["InventoryItemIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["InventoryItemsListResponseIn"])
    types["InventoryItemsListResponseOut"] = t.struct(
        {
            "inventoryItems": t.array(t.proxy(renames["InventoryItemOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryItemsListResponseOut"])
    types["AdIn"] = t.struct(
        {
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "endTime": t.string(),
            "dynamicClickTracker": t.boolean().optional(),
            "subaccountId": t.string().optional(),
            "comments": t.string().optional(),
            "accountId": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "remarketingListExpression": t.proxy(
                renames["ListTargetingExpressionIn"]
            ).optional(),
            "deliverySchedule": t.proxy(renames["DeliveryScheduleIn"]).optional(),
            "campaignIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "archived": t.boolean().optional(),
            "geoTargeting": t.proxy(renames["GeoTargetingIn"]).optional(),
            "active": t.boolean().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "keyValueTargetingExpression": t.proxy(
                renames["KeyValueTargetingExpressionIn"]
            ).optional(),
            "defaultClickThroughEventTagProperties": t.proxy(
                renames["DefaultClickThroughEventTagPropertiesIn"]
            ).optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
            "compatibility": t.string().optional(),
            "campaignId": t.string().optional(),
            "audienceSegmentId": t.string().optional(),
            "targetingTemplateId": t.string().optional(),
            "type": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "creativeRotation": t.proxy(renames["CreativeRotationIn"]).optional(),
            "startTime": t.string(),
            "dayPartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
            "sslRequired": t.boolean().optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "technologyTargeting": t.proxy(renames["TechnologyTargetingIn"]).optional(),
            "id": t.string().optional(),
            "clickThroughUrlSuffixProperties": t.proxy(
                renames["ClickThroughUrlSuffixPropertiesIn"]
            ).optional(),
            "placementAssignments": t.array(
                t.proxy(renames["PlacementAssignmentIn"])
            ).optional(),
            "eventTagOverrides": t.array(
                t.proxy(renames["EventTagOverrideIn"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "creativeGroupAssignments": t.array(
                t.proxy(renames["CreativeGroupAssignmentIn"])
            ).optional(),
        }
    ).named(renames["AdIn"])
    types["AdOut"] = t.struct(
        {
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "endTime": t.string(),
            "dynamicClickTracker": t.boolean().optional(),
            "subaccountId": t.string().optional(),
            "comments": t.string().optional(),
            "accountId": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "remarketingListExpression": t.proxy(
                renames["ListTargetingExpressionOut"]
            ).optional(),
            "deliverySchedule": t.proxy(renames["DeliveryScheduleOut"]).optional(),
            "campaignIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "archived": t.boolean().optional(),
            "geoTargeting": t.proxy(renames["GeoTargetingOut"]).optional(),
            "active": t.boolean().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "keyValueTargetingExpression": t.proxy(
                renames["KeyValueTargetingExpressionOut"]
            ).optional(),
            "defaultClickThroughEventTagProperties": t.proxy(
                renames["DefaultClickThroughEventTagPropertiesOut"]
            ).optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlOut"]).optional(),
            "compatibility": t.string().optional(),
            "campaignId": t.string().optional(),
            "audienceSegmentId": t.string().optional(),
            "targetingTemplateId": t.string().optional(),
            "type": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingOut"]).optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "creativeRotation": t.proxy(renames["CreativeRotationOut"]).optional(),
            "startTime": t.string(),
            "dayPartTargeting": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "sslRequired": t.boolean().optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "id": t.string().optional(),
            "clickThroughUrlSuffixProperties": t.proxy(
                renames["ClickThroughUrlSuffixPropertiesOut"]
            ).optional(),
            "placementAssignments": t.array(
                t.proxy(renames["PlacementAssignmentOut"])
            ).optional(),
            "eventTagOverrides": t.array(
                t.proxy(renames["EventTagOverrideOut"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "creativeGroupAssignments": t.array(
                t.proxy(renames["CreativeGroupAssignmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdOut"])
    types["DimensionValueIn"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "kind": t.string().optional(),
            "matchType": t.string().optional(),
            "etag": t.string().optional(),
            "value": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["DimensionValueIn"])
    types["DimensionValueOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "kind": t.string().optional(),
            "matchType": t.string().optional(),
            "etag": t.string().optional(),
            "value": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueOut"])
    types["ConversionIn"] = t.struct(
        {
            "gclid": t.string().optional(),
            "mobileDeviceId": t.string().optional(),
            "matchId": t.string().optional(),
            "impressionId": t.string().optional(),
            "kind": t.string().optional(),
            "floodlightActivityId": t.string().optional(),
            "ordinal": t.string().optional(),
            "encryptedUserId": t.string().optional(),
            "encryptedUserIdCandidates": t.array(t.string()).optional(),
            "value": t.number().optional(),
            "customVariables": t.array(
                t.proxy(renames["CustomFloodlightVariableIn"])
            ).optional(),
            "childDirectedTreatment": t.boolean().optional(),
            "userIdentifiers": t.array(t.proxy(renames["UserIdentifierIn"])).optional(),
            "timestampMicros": t.string().optional(),
            "limitAdTracking": t.boolean().optional(),
            "treatmentForUnderage": t.boolean().optional(),
            "nonPersonalizedAd": t.boolean().optional(),
            "quantity": t.string().optional(),
            "dclid": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
        }
    ).named(renames["ConversionIn"])
    types["ConversionOut"] = t.struct(
        {
            "gclid": t.string().optional(),
            "mobileDeviceId": t.string().optional(),
            "matchId": t.string().optional(),
            "impressionId": t.string().optional(),
            "kind": t.string().optional(),
            "floodlightActivityId": t.string().optional(),
            "ordinal": t.string().optional(),
            "encryptedUserId": t.string().optional(),
            "encryptedUserIdCandidates": t.array(t.string()).optional(),
            "value": t.number().optional(),
            "customVariables": t.array(
                t.proxy(renames["CustomFloodlightVariableOut"])
            ).optional(),
            "childDirectedTreatment": t.boolean().optional(),
            "userIdentifiers": t.array(
                t.proxy(renames["UserIdentifierOut"])
            ).optional(),
            "timestampMicros": t.string().optional(),
            "limitAdTracking": t.boolean().optional(),
            "treatmentForUnderage": t.boolean().optional(),
            "nonPersonalizedAd": t.boolean().optional(),
            "quantity": t.string().optional(),
            "dclid": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionOut"])
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
    types["BillingRateIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "endDate": t.string().optional(),
            "name": t.string().optional(),
            "unitOfMeasure": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "startDate": t.string().optional(),
            "tieredRates": t.array(
                t.proxy(renames["BillingRateTieredRateIn"])
            ).optional(),
            "rateInMicros": t.string().optional(),
        }
    ).named(renames["BillingRateIn"])
    types["BillingRateOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "endDate": t.string().optional(),
            "name": t.string().optional(),
            "unitOfMeasure": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "startDate": t.string().optional(),
            "tieredRates": t.array(
                t.proxy(renames["BillingRateTieredRateOut"])
            ).optional(),
            "rateInMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingRateOut"])
    types["CreativeAssignmentIn"] = t.struct(
        {
            "sequence": t.integer().optional(),
            "active": t.boolean().optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
            "sslCompliant": t.boolean().optional(),
            "applyEventTags": t.boolean().optional(),
            "creativeGroupAssignments": t.array(
                t.proxy(renames["CreativeGroupAssignmentIn"])
            ).optional(),
            "creativeIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "endTime": t.string(),
            "companionCreativeOverrides": t.array(
                t.proxy(renames["CompanionClickThroughOverrideIn"])
            ).optional(),
            "richMediaExitOverrides": t.array(
                t.proxy(renames["RichMediaExitOverrideIn"])
            ).optional(),
            "creativeId": t.string().optional(),
            "startTime": t.string(),
            "weight": t.integer().optional(),
        }
    ).named(renames["CreativeAssignmentIn"])
    types["CreativeAssignmentOut"] = t.struct(
        {
            "sequence": t.integer().optional(),
            "active": t.boolean().optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlOut"]).optional(),
            "sslCompliant": t.boolean().optional(),
            "applyEventTags": t.boolean().optional(),
            "creativeGroupAssignments": t.array(
                t.proxy(renames["CreativeGroupAssignmentOut"])
            ).optional(),
            "creativeIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "endTime": t.string(),
            "companionCreativeOverrides": t.array(
                t.proxy(renames["CompanionClickThroughOverrideOut"])
            ).optional(),
            "richMediaExitOverrides": t.array(
                t.proxy(renames["RichMediaExitOverrideOut"])
            ).optional(),
            "creativeId": t.string().optional(),
            "startTime": t.string(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeAssignmentOut"])
    types["DimensionFilterIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "dimensionName": t.string().optional(),
        }
    ).named(renames["DimensionFilterIn"])
    types["DimensionFilterOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionFilterOut"])
    types["ContentCategoriesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "contentCategories": t.array(
                t.proxy(renames["ContentCategoryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ContentCategoriesListResponseIn"])
    types["ContentCategoriesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "contentCategories": t.array(
                t.proxy(renames["ContentCategoryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentCategoriesListResponseOut"])
    types["EventFilterIn"] = t.struct(
        {
            "dimensionFilter": t.proxy(
                renames["PathReportDimensionValueIn"]
            ).optional(),
            "kind": t.string().optional(),
            "uvarFilter": t.proxy(renames["UvarFilterIn"]).optional(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "dimensionFilter": t.proxy(
                renames["PathReportDimensionValueOut"]
            ).optional(),
            "kind": t.string().optional(),
            "uvarFilter": t.proxy(renames["UvarFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
    types["AdvertiserGroupsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "advertiserGroups": t.array(
                t.proxy(renames["AdvertiserGroupIn"])
            ).optional(),
        }
    ).named(renames["AdvertiserGroupsListResponseIn"])
    types["AdvertiserGroupsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "advertiserGroups": t.array(
                t.proxy(renames["AdvertiserGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserGroupsListResponseOut"])
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
    types["BrowserIn"] = t.struct(
        {
            "name": t.string().optional(),
            "majorVersion": t.string().optional(),
            "minorVersion": t.string().optional(),
            "dartId": t.string().optional(),
            "kind": t.string().optional(),
            "browserVersionId": t.string().optional(),
        }
    ).named(renames["BrowserIn"])
    types["BrowserOut"] = t.struct(
        {
            "name": t.string().optional(),
            "majorVersion": t.string().optional(),
            "minorVersion": t.string().optional(),
            "dartId": t.string().optional(),
            "kind": t.string().optional(),
            "browserVersionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserOut"])
    types["PlacementGroupIn"] = t.struct(
        {
            "primaryPlacementId": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "campaignIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "campaignId": t.string().optional(),
            "placementGroupType": t.string().optional(),
            "advertiserId": t.string().optional(),
            "kind": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "externalId": t.string().optional(),
            "name": t.string().optional(),
            "activeStatus": t.string().optional(),
            "childPlacementIds": t.array(t.string()).optional(),
            "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "comment": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "primaryPlacementIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "directorySiteId": t.string().optional(),
            "contentCategoryId": t.string().optional(),
            "siteId": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
        }
    ).named(renames["PlacementGroupIn"])
    types["PlacementGroupOut"] = t.struct(
        {
            "primaryPlacementId": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "campaignIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "campaignId": t.string().optional(),
            "placementGroupType": t.string().optional(),
            "advertiserId": t.string().optional(),
            "kind": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "externalId": t.string().optional(),
            "name": t.string().optional(),
            "activeStatus": t.string().optional(),
            "childPlacementIds": t.array(t.string()).optional(),
            "pricingSchedule": t.proxy(renames["PricingScheduleOut"]).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "comment": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "primaryPlacementIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "directorySiteId": t.string().optional(),
            "contentCategoryId": t.string().optional(),
            "siteId": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementGroupOut"])
    types["CustomRichMediaEventsIn"] = t.struct(
        {
            "filteredEventIds": t.array(
                t.proxy(renames["DimensionValueIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CustomRichMediaEventsIn"])
    types["CustomRichMediaEventsOut"] = t.struct(
        {
            "filteredEventIds": t.array(
                t.proxy(renames["DimensionValueOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomRichMediaEventsOut"])
    types["BillingRatesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "billingRates": t.array(t.proxy(renames["BillingRateIn"])).optional(),
        }
    ).named(renames["BillingRatesListResponseIn"])
    types["BillingRatesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "billingRates": t.array(t.proxy(renames["BillingRateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingRatesListResponseOut"])
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
    types["ClickThroughUrlIn"] = t.struct(
        {
            "landingPageId": t.string().optional(),
            "customClickThroughUrl": t.string().optional(),
            "computedClickThroughUrl": t.string().optional(),
            "defaultLandingPage": t.boolean().optional(),
        }
    ).named(renames["ClickThroughUrlIn"])
    types["ClickThroughUrlOut"] = t.struct(
        {
            "landingPageId": t.string().optional(),
            "customClickThroughUrl": t.string().optional(),
            "computedClickThroughUrl": t.string().optional(),
            "defaultLandingPage": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClickThroughUrlOut"])
    types["CompatibleFieldsIn"] = t.struct(
        {
            "pathAttributionReportCompatibleFields": t.proxy(
                renames["PathReportCompatibleFieldsIn"]
            ).optional(),
            "kind": t.string().optional(),
            "floodlightReportCompatibleFields": t.proxy(
                renames["FloodlightReportCompatibleFieldsIn"]
            ).optional(),
            "reportCompatibleFields": t.proxy(
                renames["ReportCompatibleFieldsIn"]
            ).optional(),
            "pathToConversionReportCompatibleFields": t.proxy(
                renames["PathToConversionReportCompatibleFieldsIn"]
            ).optional(),
            "pathReportCompatibleFields": t.proxy(
                renames["PathReportCompatibleFieldsIn"]
            ).optional(),
            "crossDimensionReachReportCompatibleFields": t.proxy(
                renames["CrossDimensionReachReportCompatibleFieldsIn"]
            ).optional(),
            "reachReportCompatibleFields": t.proxy(
                renames["ReachReportCompatibleFieldsIn"]
            ).optional(),
        }
    ).named(renames["CompatibleFieldsIn"])
    types["CompatibleFieldsOut"] = t.struct(
        {
            "pathAttributionReportCompatibleFields": t.proxy(
                renames["PathReportCompatibleFieldsOut"]
            ).optional(),
            "kind": t.string().optional(),
            "floodlightReportCompatibleFields": t.proxy(
                renames["FloodlightReportCompatibleFieldsOut"]
            ).optional(),
            "reportCompatibleFields": t.proxy(
                renames["ReportCompatibleFieldsOut"]
            ).optional(),
            "pathToConversionReportCompatibleFields": t.proxy(
                renames["PathToConversionReportCompatibleFieldsOut"]
            ).optional(),
            "pathReportCompatibleFields": t.proxy(
                renames["PathReportCompatibleFieldsOut"]
            ).optional(),
            "crossDimensionReachReportCompatibleFields": t.proxy(
                renames["CrossDimensionReachReportCompatibleFieldsOut"]
            ).optional(),
            "reachReportCompatibleFields": t.proxy(
                renames["ReachReportCompatibleFieldsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompatibleFieldsOut"])
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
    types["CreativeFieldValuesListResponseIn"] = t.struct(
        {
            "creativeFieldValues": t.array(
                t.proxy(renames["CreativeFieldValueIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CreativeFieldValuesListResponseIn"])
    types["CreativeFieldValuesListResponseOut"] = t.struct(
        {
            "creativeFieldValues": t.array(
                t.proxy(renames["CreativeFieldValueOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldValuesListResponseOut"])
    types["RemarketingListIn"] = t.struct(
        {
            "listSource": t.string().optional(),
            "active": t.boolean().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "listPopulationRule": t.proxy(renames["ListPopulationRuleIn"]).optional(),
            "subaccountId": t.string().optional(),
            "lifeSpan": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "description": t.string().optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "listSize": t.string().optional(),
        }
    ).named(renames["RemarketingListIn"])
    types["RemarketingListOut"] = t.struct(
        {
            "listSource": t.string().optional(),
            "active": t.boolean().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "listPopulationRule": t.proxy(renames["ListPopulationRuleOut"]).optional(),
            "subaccountId": t.string().optional(),
            "lifeSpan": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "description": t.string().optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "listSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingListOut"])
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
    types["ReportCompatibleFieldsIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "pivotedActivityMetrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReportCompatibleFieldsIn"])
    types["ReportCompatibleFieldsOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "pivotedActivityMetrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportCompatibleFieldsOut"])
    types["CustomViewabilityMetricIn"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "configuration": t.proxy(
                renames["CustomViewabilityMetricConfigurationIn"]
            ).optional(),
        }
    ).named(renames["CustomViewabilityMetricIn"])
    types["CustomViewabilityMetricOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "configuration": t.proxy(
                renames["CustomViewabilityMetricConfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomViewabilityMetricOut"])
    types["TagDataIn"] = t.struct(
        {
            "adId": t.string().optional(),
            "clickTag": t.string().optional(),
            "impressionTag": t.string().optional(),
            "creativeId": t.string().optional(),
            "format": t.string().optional(),
        }
    ).named(renames["TagDataIn"])
    types["TagDataOut"] = t.struct(
        {
            "adId": t.string().optional(),
            "clickTag": t.string().optional(),
            "impressionTag": t.string().optional(),
            "creativeId": t.string().optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagDataOut"])
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
    types["ConversionsBatchInsertRequestIn"] = t.struct(
        {
            "encryptionInfo": t.proxy(renames["EncryptionInfoIn"]).optional(),
            "conversions": t.array(t.proxy(renames["ConversionIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ConversionsBatchInsertRequestIn"])
    types["ConversionsBatchInsertRequestOut"] = t.struct(
        {
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "conversions": t.array(t.proxy(renames["ConversionOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionsBatchInsertRequestOut"])
    types["OfflineUserAddressInfoIn"] = t.struct(
        {
            "city": t.string().optional(),
            "hashedStreetAddress": t.string().optional(),
            "postalCode": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "hashedFirstName": t.string().optional(),
            "state": t.string().optional(),
            "countryCode": t.string().optional(),
        }
    ).named(renames["OfflineUserAddressInfoIn"])
    types["OfflineUserAddressInfoOut"] = t.struct(
        {
            "city": t.string().optional(),
            "hashedStreetAddress": t.string().optional(),
            "postalCode": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "hashedFirstName": t.string().optional(),
            "state": t.string().optional(),
            "countryCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfflineUserAddressInfoOut"])
    types["DateRangeIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "relativeDateRange": t.string().optional(),
            "startDate": t.string(),
            "endDate": t.string(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "relativeDateRange": t.string().optional(),
            "startDate": t.string(),
            "endDate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
    types["AdvertiserGroupIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["AdvertiserGroupIn"])
    types["AdvertiserGroupOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserGroupOut"])
    types["SortedDimensionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "sortOrder": t.string().optional(),
        }
    ).named(renames["SortedDimensionIn"])
    types["SortedDimensionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "sortOrder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortedDimensionOut"])
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
    types["PlatformTypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PlatformTypeIn"])
    types["PlatformTypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformTypeOut"])
    types["FloodlightActivityGroupIn"] = t.struct(
        {
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "name": t.string().optional(),
            "subaccountId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "advertiserId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "type": t.string().optional(),
            "accountId": t.string().optional(),
            "tagString": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
        }
    ).named(renames["FloodlightActivityGroupIn"])
    types["FloodlightActivityGroupOut"] = t.struct(
        {
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "name": t.string().optional(),
            "subaccountId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "advertiserId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "type": t.string().optional(),
            "accountId": t.string().optional(),
            "tagString": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivityGroupOut"])
    types["LanguageTargetingIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["LanguageIn"])).optional()}
    ).named(renames["LanguageTargetingIn"])
    types["LanguageTargetingOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["LanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageTargetingOut"])
    types["DefaultClickThroughEventTagPropertiesIn"] = t.struct(
        {
            "defaultClickThroughEventTagId": t.string().optional(),
            "overrideInheritedEventTag": t.boolean().optional(),
        }
    ).named(renames["DefaultClickThroughEventTagPropertiesIn"])
    types["DefaultClickThroughEventTagPropertiesOut"] = t.struct(
        {
            "defaultClickThroughEventTagId": t.string().optional(),
            "overrideInheritedEventTag": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultClickThroughEventTagPropertiesOut"])
    types["PricingSchedulePricingPeriodIn"] = t.struct(
        {
            "startDate": t.string(),
            "rateOrCostNanos": t.string().optional(),
            "endDate": t.string(),
            "units": t.string().optional(),
            "pricingComment": t.string().optional(),
        }
    ).named(renames["PricingSchedulePricingPeriodIn"])
    types["PricingSchedulePricingPeriodOut"] = t.struct(
        {
            "startDate": t.string(),
            "rateOrCostNanos": t.string().optional(),
            "endDate": t.string(),
            "units": t.string().optional(),
            "pricingComment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingSchedulePricingPeriodOut"])
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
    types["AdvertisersListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "advertisers": t.array(t.proxy(renames["AdvertiserIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AdvertisersListResponseIn"])
    types["AdvertisersListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "advertisers": t.array(t.proxy(renames["AdvertiserOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertisersListResponseOut"])
    types["LandingPageIn"] = t.struct(
        {
            "url": t.string().optional(),
            "advertiserId": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "deepLinks": t.array(t.proxy(renames["DeepLinkIn"])).optional(),
            "archived": t.boolean().optional(),
        }
    ).named(renames["LandingPageIn"])
    types["LandingPageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "advertiserId": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "deepLinks": t.array(t.proxy(renames["DeepLinkOut"])).optional(),
            "archived": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LandingPageOut"])
    types["SiteIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "accountId": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "keyName": t.string().optional(),
            "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
            "approved": t.boolean().optional(),
            "id": t.string().optional(),
            "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
            "name": t.string().optional(),
            "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
            "directorySiteId": t.string().optional(),
        }
    ).named(renames["SiteIn"])
    types["SiteOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "accountId": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "keyName": t.string().optional(),
            "siteContacts": t.array(t.proxy(renames["SiteContactOut"])).optional(),
            "approved": t.boolean().optional(),
            "id": t.string().optional(),
            "videoSettings": t.proxy(renames["SiteVideoSettingsOut"]).optional(),
            "name": t.string().optional(),
            "siteSettings": t.proxy(renames["SiteSettingsOut"]).optional(),
            "directorySiteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteOut"])
    types["InventoryItemIn"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "siteId": t.string().optional(),
            "orderId": t.string().optional(),
            "negotiationChannelId": t.string().optional(),
            "estimatedClickThroughRate": t.string().optional(),
            "rfpId": t.string().optional(),
            "pricing": t.proxy(renames["PricingIn"]).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "accountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "id": t.string().optional(),
            "projectId": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "contentCategoryId": t.string().optional(),
            "adSlots": t.array(t.proxy(renames["AdSlotIn"])).optional(),
            "kind": t.string().optional(),
            "estimatedConversionRate": t.string().optional(),
            "subaccountId": t.string().optional(),
            "inPlan": t.boolean().optional(),
        }
    ).named(renames["InventoryItemIn"])
    types["InventoryItemOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "siteId": t.string().optional(),
            "orderId": t.string().optional(),
            "negotiationChannelId": t.string().optional(),
            "estimatedClickThroughRate": t.string().optional(),
            "rfpId": t.string().optional(),
            "pricing": t.proxy(renames["PricingOut"]).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "accountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "id": t.string().optional(),
            "projectId": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "contentCategoryId": t.string().optional(),
            "adSlots": t.array(t.proxy(renames["AdSlotOut"])).optional(),
            "kind": t.string().optional(),
            "estimatedConversionRate": t.string().optional(),
            "subaccountId": t.string().optional(),
            "inPlan": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryItemOut"])
    types["PricingScheduleIn"] = t.struct(
        {
            "capCostOption": t.string().optional(),
            "flighted": t.boolean().optional(),
            "endDate": t.string(),
            "pricingType": t.string().optional(),
            "testingStartDate": t.string(),
            "pricingPeriods": t.array(
                t.proxy(renames["PricingSchedulePricingPeriodIn"])
            ).optional(),
            "floodlightActivityId": t.string().optional(),
            "startDate": t.string(),
        }
    ).named(renames["PricingScheduleIn"])
    types["PricingScheduleOut"] = t.struct(
        {
            "capCostOption": t.string().optional(),
            "flighted": t.boolean().optional(),
            "endDate": t.string(),
            "pricingType": t.string().optional(),
            "testingStartDate": t.string(),
            "pricingPeriods": t.array(
                t.proxy(renames["PricingSchedulePricingPeriodOut"])
            ).optional(),
            "floodlightActivityId": t.string().optional(),
            "startDate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingScheduleOut"])
    types["UserProfileListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["UserProfileIn"])).optional(),
        }
    ).named(renames["UserProfileListIn"])
    types["UserProfileListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["UserProfileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserProfileListOut"])
    types["CrossDimensionReachReportCompatibleFieldsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "breakdown": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "overlapMetrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["CrossDimensionReachReportCompatibleFieldsIn"])
    types["CrossDimensionReachReportCompatibleFieldsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "breakdown": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "overlapMetrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrossDimensionReachReportCompatibleFieldsOut"])
    types["CreativeAssetIn"] = t.struct(
        {
            "duration": t.integer().optional(),
            "originalBackup": t.boolean().optional(),
            "childAssetType": t.string().optional(),
            "id": t.string().optional(),
            "horizontallyLocked": t.boolean().optional(),
            "progressiveServingUrl": t.string().optional(),
            "position": t.proxy(renames["OffsetPositionIn"]).optional(),
            "frameRate": t.number().optional(),
            "collapsedSize": t.proxy(renames["SizeIn"]).optional(),
            "fileSize": t.string().optional(),
            "backupImageExit": t.proxy(renames["CreativeCustomEventIn"]).optional(),
            "detectedFeatures": t.array(t.string()).optional(),
            "audioBitRate": t.integer().optional(),
            "startTimeType": t.string().optional(),
            "positionLeftUnit": t.string().optional(),
            "displayType": t.string().optional(),
            "orientation": t.string().optional(),
            "active": t.boolean().optional(),
            "mimeType": t.string().optional(),
            "pushdownDuration": t.number().optional(),
            "durationType": t.string().optional(),
            "flashVersion": t.integer().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "pushdown": t.boolean().optional(),
            "bitRate": t.integer().optional(),
            "artworkType": t.string().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "alignment": t.string().optional(),
            "role": t.string().optional(),
            "zipFilesize": t.string().optional(),
            "customStartTimeValue": t.integer().optional(),
            "offset": t.proxy(renames["OffsetPositionIn"]).optional(),
            "hideFlashObjects": t.boolean().optional(),
            "windowMode": t.string().optional(),
            "streamingServingUrl": t.string().optional(),
            "verticallyLocked": t.boolean().optional(),
            "zIndex": t.integer().optional(),
            "mediaDuration": t.number().optional(),
            "sslCompliant": t.boolean().optional(),
            "actionScript3": t.boolean().optional(),
            "politeLoad": t.boolean().optional(),
            "transparency": t.boolean().optional(),
            "zipFilename": t.string().optional(),
            "audioSampleRate": t.integer().optional(),
            "positionTopUnit": t.string().optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "assetIdentifier": t.proxy(renames["CreativeAssetIdIn"]).optional(),
            "hideSelectionBoxes": t.boolean().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "expandedDimension": t.proxy(renames["SizeIn"]).optional(),
        }
    ).named(renames["CreativeAssetIn"])
    types["CreativeAssetOut"] = t.struct(
        {
            "duration": t.integer().optional(),
            "originalBackup": t.boolean().optional(),
            "childAssetType": t.string().optional(),
            "id": t.string().optional(),
            "horizontallyLocked": t.boolean().optional(),
            "progressiveServingUrl": t.string().optional(),
            "position": t.proxy(renames["OffsetPositionOut"]).optional(),
            "frameRate": t.number().optional(),
            "collapsedSize": t.proxy(renames["SizeOut"]).optional(),
            "fileSize": t.string().optional(),
            "backupImageExit": t.proxy(renames["CreativeCustomEventOut"]).optional(),
            "detectedFeatures": t.array(t.string()).optional(),
            "audioBitRate": t.integer().optional(),
            "startTimeType": t.string().optional(),
            "positionLeftUnit": t.string().optional(),
            "displayType": t.string().optional(),
            "orientation": t.string().optional(),
            "active": t.boolean().optional(),
            "mimeType": t.string().optional(),
            "pushdownDuration": t.number().optional(),
            "durationType": t.string().optional(),
            "flashVersion": t.integer().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "pushdown": t.boolean().optional(),
            "bitRate": t.integer().optional(),
            "artworkType": t.string().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "alignment": t.string().optional(),
            "role": t.string().optional(),
            "zipFilesize": t.string().optional(),
            "customStartTimeValue": t.integer().optional(),
            "offset": t.proxy(renames["OffsetPositionOut"]).optional(),
            "hideFlashObjects": t.boolean().optional(),
            "windowMode": t.string().optional(),
            "streamingServingUrl": t.string().optional(),
            "verticallyLocked": t.boolean().optional(),
            "zIndex": t.integer().optional(),
            "mediaDuration": t.number().optional(),
            "sslCompliant": t.boolean().optional(),
            "actionScript3": t.boolean().optional(),
            "politeLoad": t.boolean().optional(),
            "transparency": t.boolean().optional(),
            "zipFilename": t.string().optional(),
            "audioSampleRate": t.integer().optional(),
            "positionTopUnit": t.string().optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "assetIdentifier": t.proxy(renames["CreativeAssetIdOut"]).optional(),
            "hideSelectionBoxes": t.boolean().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "expandedDimension": t.proxy(renames["SizeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeAssetOut"])
    types["ThirdPartyAuthenticationTokenIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["ThirdPartyAuthenticationTokenIn"])
    types["ThirdPartyAuthenticationTokenOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyAuthenticationTokenOut"])
    types["SiteSettingsIn"] = t.struct(
        {
            "vpaidAdapterChoiceTemplate": t.string().optional(),
            "videoActiveViewOptOutTemplate": t.boolean().optional(),
            "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
            "activeViewOptOut": t.boolean().optional(),
            "disableNewCookie": t.boolean().optional(),
            "adBlockingOptOut": t.boolean().optional(),
        }
    ).named(renames["SiteSettingsIn"])
    types["SiteSettingsOut"] = t.struct(
        {
            "vpaidAdapterChoiceTemplate": t.string().optional(),
            "videoActiveViewOptOutTemplate": t.boolean().optional(),
            "tagSetting": t.proxy(renames["TagSettingOut"]).optional(),
            "activeViewOptOut": t.boolean().optional(),
            "disableNewCookie": t.boolean().optional(),
            "adBlockingOptOut": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteSettingsOut"])
    types["FloodlightReportCompatibleFieldsIn"] = t.struct(
        {
            "dimensionFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "kind": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["FloodlightReportCompatibleFieldsIn"])
    types["FloodlightReportCompatibleFieldsOut"] = t.struct(
        {
            "dimensionFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "kind": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightReportCompatibleFieldsOut"])
    types["LanguagesListResponseIn"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["LanguageIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LanguagesListResponseIn"])
    types["LanguagesListResponseOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["LanguageOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguagesListResponseOut"])
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
    types["SiteContactIn"] = t.struct(
        {
            "email": t.string().optional(),
            "title": t.string().optional(),
            "contactType": t.string().optional(),
            "phone": t.string().optional(),
            "firstName": t.string().optional(),
            "lastName": t.string().optional(),
            "id": t.string().optional(),
            "address": t.string().optional(),
        }
    ).named(renames["SiteContactIn"])
    types["SiteContactOut"] = t.struct(
        {
            "email": t.string().optional(),
            "title": t.string().optional(),
            "contactType": t.string().optional(),
            "phone": t.string().optional(),
            "firstName": t.string().optional(),
            "lastName": t.string().optional(),
            "id": t.string().optional(),
            "address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteContactOut"])
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
    types["PlacementsGenerateTagsResponseIn"] = t.struct(
        {
            "placementTags": t.array(t.proxy(renames["PlacementTagIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlacementsGenerateTagsResponseIn"])
    types["PlacementsGenerateTagsResponseOut"] = t.struct(
        {
            "placementTags": t.array(t.proxy(renames["PlacementTagOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementsGenerateTagsResponseOut"])
    types["TechnologyTargetingIn"] = t.struct(
        {
            "browsers": t.array(t.proxy(renames["BrowserIn"])).optional(),
            "platformTypes": t.array(t.proxy(renames["PlatformTypeIn"])).optional(),
            "operatingSystems": t.array(
                t.proxy(renames["OperatingSystemIn"])
            ).optional(),
            "connectionTypes": t.array(t.proxy(renames["ConnectionTypeIn"])).optional(),
            "mobileCarriers": t.array(t.proxy(renames["MobileCarrierIn"])).optional(),
            "operatingSystemVersions": t.array(
                t.proxy(renames["OperatingSystemVersionIn"])
            ).optional(),
        }
    ).named(renames["TechnologyTargetingIn"])
    types["TechnologyTargetingOut"] = t.struct(
        {
            "browsers": t.array(t.proxy(renames["BrowserOut"])).optional(),
            "platformTypes": t.array(t.proxy(renames["PlatformTypeOut"])).optional(),
            "operatingSystems": t.array(
                t.proxy(renames["OperatingSystemOut"])
            ).optional(),
            "connectionTypes": t.array(
                t.proxy(renames["ConnectionTypeOut"])
            ).optional(),
            "mobileCarriers": t.array(t.proxy(renames["MobileCarrierOut"])).optional(),
            "operatingSystemVersions": t.array(
                t.proxy(renames["OperatingSystemVersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TechnologyTargetingOut"])
    types["ChangeLogIn"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "fieldName": t.string().optional(),
            "id": t.string().optional(),
            "userProfileId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "userProfileName": t.string().optional(),
            "objectId": t.string().optional(),
            "newValue": t.string().optional(),
            "oldValue": t.string().optional(),
            "objectType": t.string().optional(),
            "action": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "changeTime": t.string(),
        }
    ).named(renames["ChangeLogIn"])
    types["ChangeLogOut"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "fieldName": t.string().optional(),
            "id": t.string().optional(),
            "userProfileId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "userProfileName": t.string().optional(),
            "objectId": t.string().optional(),
            "newValue": t.string().optional(),
            "oldValue": t.string().optional(),
            "objectType": t.string().optional(),
            "action": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "changeTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeLogOut"])
    types["ReportsConfigurationIn"] = t.struct(
        {
            "exposureToConversionEnabled": t.boolean().optional(),
            "reportGenerationTimeZoneId": t.string().optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationIn"]
            ).optional(),
        }
    ).named(renames["ReportsConfigurationIn"])
    types["ReportsConfigurationOut"] = t.struct(
        {
            "exposureToConversionEnabled": t.boolean().optional(),
            "reportGenerationTimeZoneId": t.string().optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportsConfigurationOut"])
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
    types["PostalCodeIn"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "id": t.string().optional(),
            "countryDartId": t.string().optional(),
            "code": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PostalCodeIn"])
    types["PostalCodeOut"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "id": t.string().optional(),
            "countryDartId": t.string().optional(),
            "code": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalCodeOut"])
    types["FloodlightConfigurationsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "floodlightConfigurations": t.array(
                t.proxy(renames["FloodlightConfigurationIn"])
            ).optional(),
        }
    ).named(renames["FloodlightConfigurationsListResponseIn"])
    types["FloodlightConfigurationsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "floodlightConfigurations": t.array(
                t.proxy(renames["FloodlightConfigurationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightConfigurationsListResponseOut"])
    types["CreativeOptimizationConfigurationIn"] = t.struct(
        {
            "optimizationModel": t.string().optional(),
            "name": t.string().optional(),
            "optimizationActivitys": t.array(
                t.proxy(renames["OptimizationActivityIn"])
            ).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CreativeOptimizationConfigurationIn"])
    types["CreativeOptimizationConfigurationOut"] = t.struct(
        {
            "optimizationModel": t.string().optional(),
            "name": t.string().optional(),
            "optimizationActivitys": t.array(
                t.proxy(renames["OptimizationActivityOut"])
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOptimizationConfigurationOut"])
    types["CreativeIn"] = t.struct(
        {
            "studioAdvertiserId": t.string().optional(),
            "backupImageFeatures": t.array(t.string()).optional(),
            "creativeAssets": t.array(t.proxy(renames["CreativeAssetIn"])).optional(),
            "adTagKeys": t.array(t.string()).optional(),
            "studioTraffickedCreativeId": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "dynamicAssetSelection": t.boolean().optional(),
            "backupImageTargetWindow": t.proxy(renames["TargetWindowIn"]).optional(),
            "convertFlashToHtml5": t.boolean().optional(),
            "autoAdvanceImages": t.boolean().optional(),
            "commercialId": t.string().optional(),
            "studioCreativeId": t.string().optional(),
            "advertiserId": t.string(),
            "requiredFlashVersion": t.integer().optional(),
            "compatibility": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "renderingId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "sslOverride": t.boolean().optional(),
            "archived": t.boolean().optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
            "thirdPartyBackupImageImpressionsUrl": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "htmlCode": t.string().optional(),
            "active": t.boolean().optional(),
            "version": t.integer().optional(),
            "artworkType": t.string().optional(),
            "type": t.string(),
            "creativeFieldAssignments": t.array(
                t.proxy(renames["CreativeFieldAssignmentIn"])
            ).optional(),
            "authoringTool": t.string().optional(),
            "overrideCss": t.string().optional(),
            "clickTags": t.array(t.proxy(renames["ClickTagIn"])).optional(),
            "customKeyValues": t.array(t.string()).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "latestTraffickedCreativeId": t.string().optional(),
            "backupImageReportingLabel": t.string().optional(),
            "companionCreatives": t.array(t.string()).optional(),
            "thirdPartyRichMediaImpressionsUrl": t.string().optional(),
            "name": t.string(),
            "kind": t.string().optional(),
            "fsCommand": t.proxy(renames["FsCommandIn"]).optional(),
            "thirdPartyUrls": t.array(
                t.proxy(renames["ThirdPartyTrackingUrlIn"])
            ).optional(),
            "htmlCodeLocked": t.boolean().optional(),
            "backgroundColor": t.string().optional(),
            "accountId": t.string().optional(),
            "counterCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "renderingIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "adParameters": t.string().optional(),
            "progressOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
            "timerCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "mediaDescription": t.string().optional(),
            "allowScriptAccess": t.boolean().optional(),
            "mediaDuration": t.number().optional(),
            "redirectUrl": t.string().optional(),
            "exitCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventIn"])
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "skipOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
            "backupImageClickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlIn"]
            ).optional(),
            "skippable": t.boolean().optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "requiredFlashPluginVersion": t.string().optional(),
            "totalFileSize": t.string().optional(),
            "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
            "authoringSource": t.string().optional(),
            "creativeAssetSelection": t.proxy(renames["CreativeAssetSelectionIn"]),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "studioAdvertiserId": t.string().optional(),
            "backupImageFeatures": t.array(t.string()).optional(),
            "creativeAssets": t.array(t.proxy(renames["CreativeAssetOut"])).optional(),
            "adTagKeys": t.array(t.string()).optional(),
            "studioTraffickedCreativeId": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "dynamicAssetSelection": t.boolean().optional(),
            "backupImageTargetWindow": t.proxy(renames["TargetWindowOut"]).optional(),
            "convertFlashToHtml5": t.boolean().optional(),
            "autoAdvanceImages": t.boolean().optional(),
            "commercialId": t.string().optional(),
            "studioCreativeId": t.string().optional(),
            "advertiserId": t.string(),
            "requiredFlashVersion": t.integer().optional(),
            "compatibility": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "renderingId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "sslOverride": t.boolean().optional(),
            "archived": t.boolean().optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdOut"]).optional(),
            "thirdPartyBackupImageImpressionsUrl": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "htmlCode": t.string().optional(),
            "active": t.boolean().optional(),
            "version": t.integer().optional(),
            "artworkType": t.string().optional(),
            "type": t.string(),
            "creativeFieldAssignments": t.array(
                t.proxy(renames["CreativeFieldAssignmentOut"])
            ).optional(),
            "authoringTool": t.string().optional(),
            "overrideCss": t.string().optional(),
            "clickTags": t.array(t.proxy(renames["ClickTagOut"])).optional(),
            "customKeyValues": t.array(t.string()).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "latestTraffickedCreativeId": t.string().optional(),
            "backupImageReportingLabel": t.string().optional(),
            "companionCreatives": t.array(t.string()).optional(),
            "thirdPartyRichMediaImpressionsUrl": t.string().optional(),
            "name": t.string(),
            "kind": t.string().optional(),
            "fsCommand": t.proxy(renames["FsCommandOut"]).optional(),
            "thirdPartyUrls": t.array(
                t.proxy(renames["ThirdPartyTrackingUrlOut"])
            ).optional(),
            "htmlCodeLocked": t.boolean().optional(),
            "backgroundColor": t.string().optional(),
            "accountId": t.string().optional(),
            "counterCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "renderingIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "adParameters": t.string().optional(),
            "progressOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "timerCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "mediaDescription": t.string().optional(),
            "allowScriptAccess": t.boolean().optional(),
            "mediaDuration": t.number().optional(),
            "redirectUrl": t.string().optional(),
            "exitCustomEvents": t.array(
                t.proxy(renames["CreativeCustomEventOut"])
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "skipOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "backupImageClickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlOut"]
            ).optional(),
            "skippable": t.boolean().optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "requiredFlashPluginVersion": t.string().optional(),
            "totalFileSize": t.string().optional(),
            "obaIcon": t.proxy(renames["ObaIconOut"]).optional(),
            "authoringSource": t.string().optional(),
            "creativeAssetSelection": t.proxy(renames["CreativeAssetSelectionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
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
    types["UserProfileIn"] = t.struct(
        {
            "userName": t.string().optional(),
            "profileId": t.string().optional(),
            "subAccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "accountName": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "subAccountName": t.string().optional(),
        }
    ).named(renames["UserProfileIn"])
    types["UserProfileOut"] = t.struct(
        {
            "userName": t.string().optional(),
            "profileId": t.string().optional(),
            "subAccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "accountName": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "subAccountName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserProfileOut"])
    types["DynamicTargetingKeyIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "objectType": t.string().optional(),
        }
    ).named(renames["DynamicTargetingKeyIn"])
    types["DynamicTargetingKeyOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicTargetingKeyOut"])
    types["CreativeFieldValueIn"] = t.struct(
        {
            "id": t.string().optional(),
            "value": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CreativeFieldValueIn"])
    types["CreativeFieldValueOut"] = t.struct(
        {
            "id": t.string().optional(),
            "value": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldValueOut"])
    types["BillingProfilesListResponseIn"] = t.struct(
        {
            "billingProfiles": t.array(t.proxy(renames["BillingProfileIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BillingProfilesListResponseIn"])
    types["BillingProfilesListResponseOut"] = t.struct(
        {
            "billingProfiles": t.array(
                t.proxy(renames["BillingProfileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingProfilesListResponseOut"])
    types["UserRolePermissionGroupIn"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["UserRolePermissionGroupIn"])
    types["UserRolePermissionGroupOut"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRolePermissionGroupOut"])
    types["BillingProfileIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "invoiceLevel": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "paymentsCustomerId": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "secondaryPaymentsCustomerId": t.string().optional(),
            "consolidatedInvoice": t.boolean().optional(),
            "countryCode": t.string().optional(),
            "currencyCode": t.string().optional(),
            "purchaseOrder": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
        }
    ).named(renames["BillingProfileIn"])
    types["BillingProfileOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "invoiceLevel": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "paymentsCustomerId": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "secondaryPaymentsCustomerId": t.string().optional(),
            "consolidatedInvoice": t.boolean().optional(),
            "countryCode": t.string().optional(),
            "currencyCode": t.string().optional(),
            "purchaseOrder": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingProfileOut"])
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
    types["RemarketingListsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "remarketingLists": t.array(
                t.proxy(renames["RemarketingListIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["RemarketingListsListResponseIn"])
    types["RemarketingListsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "remarketingLists": t.array(
                t.proxy(renames["RemarketingListOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingListsListResponseOut"])
    types["RuleIn"] = t.struct(
        {
            "targetingTemplateId": t.string().optional(),
            "assetId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "targetingTemplateId": t.string().optional(),
            "assetId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["TargetableRemarketingListIn"] = t.struct(
        {
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "listSize": t.string().optional(),
            "subaccountId": t.string().optional(),
            "description": t.string().optional(),
            "lifeSpan": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserId": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "listSource": t.string().optional(),
            "active": t.boolean().optional(),
        }
    ).named(renames["TargetableRemarketingListIn"])
    types["TargetableRemarketingListOut"] = t.struct(
        {
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "listSize": t.string().optional(),
            "subaccountId": t.string().optional(),
            "description": t.string().optional(),
            "lifeSpan": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserId": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "listSource": t.string().optional(),
            "active": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetableRemarketingListOut"])
    types["CreativeClickThroughUrlIn"] = t.struct(
        {
            "computedClickThroughUrl": t.string().optional(),
            "landingPageId": t.string().optional(),
            "customClickThroughUrl": t.string().optional(),
        }
    ).named(renames["CreativeClickThroughUrlIn"])
    types["CreativeClickThroughUrlOut"] = t.struct(
        {
            "computedClickThroughUrl": t.string().optional(),
            "landingPageId": t.string().optional(),
            "customClickThroughUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeClickThroughUrlOut"])
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
    types["ReportListIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["ReportIn"])).optional(),
        }
    ).named(renames["ReportListIn"])
    types["ReportListOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["ReportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportListOut"])
    types["BillingAssignmentIn"] = t.struct(
        {
            "subaccountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "campaignId": t.string().optional(),
        }
    ).named(renames["BillingAssignmentIn"])
    types["BillingAssignmentOut"] = t.struct(
        {
            "subaccountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "campaignId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingAssignmentOut"])
    types["CreativeRotationIn"] = t.struct(
        {
            "type": t.string().optional(),
            "creativeOptimizationConfigurationId": t.string().optional(),
            "creativeAssignments": t.array(
                t.proxy(renames["CreativeAssignmentIn"])
            ).optional(),
            "weightCalculationStrategy": t.string().optional(),
        }
    ).named(renames["CreativeRotationIn"])
    types["CreativeRotationOut"] = t.struct(
        {
            "type": t.string().optional(),
            "creativeOptimizationConfigurationId": t.string().optional(),
            "creativeAssignments": t.array(
                t.proxy(renames["CreativeAssignmentOut"])
            ).optional(),
            "weightCalculationStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRotationOut"])
    types["FloodlightActivitiesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "floodlightActivities": t.array(
                t.proxy(renames["FloodlightActivityIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["FloodlightActivitiesListResponseIn"])
    types["FloodlightActivitiesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "floodlightActivities": t.array(
                t.proxy(renames["FloodlightActivityOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivitiesListResponseOut"])
    types["PlacementIn"] = t.struct(
        {
            "placementGroupIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "campaignId": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "externalId": t.string().optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationIn"]
            ).optional(),
            "campaignIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "primary": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "vpaidAdapterChoice": t.string().optional(),
            "name": t.string().optional(),
            "subaccountId": t.string().optional(),
            "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
            "placementGroupId": t.string().optional(),
            "paymentSource": t.string().optional(),
            "keyName": t.string().optional(),
            "compatibility": t.string().optional(),
            "directorySiteId": t.string().optional(),
            "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
            "status": t.string().optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "contentCategoryId": t.string().optional(),
            "comment": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "partnerWrappingData": t.proxy(
                renames["MeasurementPartnerWrappingDataIn"]
            ).optional(),
            "wrappingOptOut": t.boolean().optional(),
            "kind": t.string().optional(),
            "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "tagFormats": t.array(t.string()).optional(),
            "activeStatus": t.string().optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "sslRequired": t.boolean().optional(),
            "accountId": t.string().optional(),
            "paymentApproved": t.boolean().optional(),
            "adBlockingOptOut": t.boolean().optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "publisherUpdateInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "id": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "videoActiveViewOptOut": t.boolean().optional(),
            "siteId": t.string().optional(),
        }
    ).named(renames["PlacementIn"])
    types["PlacementOut"] = t.struct(
        {
            "placementGroupIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "campaignId": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "externalId": t.string().optional(),
            "lookbackConfiguration": t.proxy(
                renames["LookbackConfigurationOut"]
            ).optional(),
            "campaignIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "primary": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "placementStrategyId": t.string().optional(),
            "vpaidAdapterChoice": t.string().optional(),
            "name": t.string().optional(),
            "subaccountId": t.string().optional(),
            "tagSetting": t.proxy(renames["TagSettingOut"]).optional(),
            "placementGroupId": t.string().optional(),
            "paymentSource": t.string().optional(),
            "keyName": t.string().optional(),
            "compatibility": t.string().optional(),
            "directorySiteId": t.string().optional(),
            "pricingSchedule": t.proxy(renames["PricingScheduleOut"]).optional(),
            "status": t.string().optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "contentCategoryId": t.string().optional(),
            "comment": t.string().optional(),
            "directorySiteIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "partnerWrappingData": t.proxy(
                renames["MeasurementPartnerWrappingDataOut"]
            ).optional(),
            "wrappingOptOut": t.boolean().optional(),
            "kind": t.string().optional(),
            "videoSettings": t.proxy(renames["VideoSettingsOut"]).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "tagFormats": t.array(t.string()).optional(),
            "activeStatus": t.string().optional(),
            "additionalSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "sslRequired": t.boolean().optional(),
            "accountId": t.string().optional(),
            "paymentApproved": t.boolean().optional(),
            "adBlockingOptOut": t.boolean().optional(),
            "siteIdDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "publisherUpdateInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "id": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "videoActiveViewOptOut": t.boolean().optional(),
            "siteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementOut"])
    types["OrdersListResponseIn"] = t.struct(
        {
            "orders": t.array(t.proxy(renames["OrderIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["OrdersListResponseIn"])
    types["OrdersListResponseOut"] = t.struct(
        {
            "orders": t.array(t.proxy(renames["OrderOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersListResponseOut"])
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
    types["DirectorySitesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "directorySites": t.array(t.proxy(renames["DirectorySiteIn"])).optional(),
        }
    ).named(renames["DirectorySitesListResponseIn"])
    types["DirectorySitesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "directorySites": t.array(t.proxy(renames["DirectorySiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectorySitesListResponseOut"])
    types["ChannelGroupingIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ChannelGroupingRuleIn"])).optional(),
            "name": t.string().optional(),
            "fallbackName": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ChannelGroupingIn"])
    types["ChannelGroupingOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ChannelGroupingRuleOut"])).optional(),
            "name": t.string().optional(),
            "fallbackName": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelGroupingOut"])
    types["SizeIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "height": t.integer().optional(),
            "id": t.string().optional(),
            "width": t.integer().optional(),
            "iab": t.boolean().optional(),
        }
    ).named(renames["SizeIn"])
    types["SizeOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "height": t.integer().optional(),
            "id": t.string().optional(),
            "width": t.integer().optional(),
            "iab": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SizeOut"])
    types["OffsetPositionIn"] = t.struct(
        {"left": t.integer().optional(), "top": t.integer().optional()}
    ).named(renames["OffsetPositionIn"])
    types["OffsetPositionOut"] = t.struct(
        {
            "left": t.integer().optional(),
            "top": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OffsetPositionOut"])
    types["DirectorySiteIn"] = t.struct(
        {
            "interstitialTagFormats": t.array(t.string()).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "inpageTagFormats": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "settings": t.proxy(renames["DirectorySiteSettingsIn"]).optional(),
            "name": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["DirectorySiteIn"])
    types["DirectorySiteOut"] = t.struct(
        {
            "interstitialTagFormats": t.array(t.string()).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "inpageTagFormats": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "settings": t.proxy(renames["DirectorySiteSettingsOut"]).optional(),
            "name": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectorySiteOut"])
    types["DfpSettingsIn"] = t.struct(
        {
            "dfpNetworkName": t.string().optional(),
            "programmaticPlacementAccepted": t.boolean().optional(),
            "publisherPortalOnly": t.boolean().optional(),
            "dfpNetworkCode": t.string().optional(),
            "pubPaidPlacementAccepted": t.boolean().optional(),
        }
    ).named(renames["DfpSettingsIn"])
    types["DfpSettingsOut"] = t.struct(
        {
            "dfpNetworkName": t.string().optional(),
            "programmaticPlacementAccepted": t.boolean().optional(),
            "publisherPortalOnly": t.boolean().optional(),
            "dfpNetworkCode": t.string().optional(),
            "pubPaidPlacementAccepted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DfpSettingsOut"])
    types["BillingRateTieredRateIn"] = t.struct(
        {
            "lowValue": t.string().optional(),
            "highValue": t.string().optional(),
            "rateInMicros": t.string().optional(),
        }
    ).named(renames["BillingRateTieredRateIn"])
    types["BillingRateTieredRateOut"] = t.struct(
        {
            "lowValue": t.string().optional(),
            "highValue": t.string().optional(),
            "rateInMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingRateTieredRateOut"])
    types["LanguageIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["LanguageIn"])
    types["LanguageOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageOut"])
    types["OptimizationActivityIn"] = t.struct(
        {
            "weight": t.integer().optional(),
            "floodlightActivityId": t.string().optional(),
            "floodlightActivityIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
        }
    ).named(renames["OptimizationActivityIn"])
    types["OptimizationActivityOut"] = t.struct(
        {
            "weight": t.integer().optional(),
            "floodlightActivityId": t.string().optional(),
            "floodlightActivityIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptimizationActivityOut"])
    types["CreativeFieldIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "id": t.string().optional(),
            "subaccountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CreativeFieldIn"])
    types["CreativeFieldOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "id": t.string().optional(),
            "subaccountId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeFieldOut"])
    types["PathToConversionReportCompatibleFieldsIn"] = t.struct(
        {
            "perInteractionDimensions": t.array(
                t.proxy(renames["DimensionIn"])
            ).optional(),
            "kind": t.string().optional(),
            "customFloodlightVariables": t.array(
                t.proxy(renames["DimensionIn"])
            ).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "conversionDimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["PathToConversionReportCompatibleFieldsIn"])
    types["PathToConversionReportCompatibleFieldsOut"] = t.struct(
        {
            "perInteractionDimensions": t.array(
                t.proxy(renames["DimensionOut"])
            ).optional(),
            "kind": t.string().optional(),
            "customFloodlightVariables": t.array(
                t.proxy(renames["DimensionOut"])
            ).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "conversionDimensions": t.array(
                t.proxy(renames["DimensionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathToConversionReportCompatibleFieldsOut"])
    types["SubaccountsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "subaccounts": t.array(t.proxy(renames["SubaccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SubaccountsListResponseIn"])
    types["SubaccountsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "subaccounts": t.array(t.proxy(renames["SubaccountOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubaccountsListResponseOut"])
    types["AccountActiveAdSummaryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "availableAds": t.string().optional(),
            "activeAds": t.string().optional(),
            "activeAdsLimitTier": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["AccountActiveAdSummaryIn"])
    types["AccountActiveAdSummaryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "availableAds": t.string().optional(),
            "activeAds": t.string().optional(),
            "activeAdsLimitTier": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountActiveAdSummaryOut"])
    types["DimensionIn"] = t.struct(
        {"kind": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DimensionIn"])
    types["DimensionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOut"])
    types["UniversalAdIdIn"] = t.struct(
        {"value": t.string().optional(), "registry": t.string().optional()}
    ).named(renames["UniversalAdIdIn"])
    types["UniversalAdIdOut"] = t.struct(
        {
            "value": t.string().optional(),
            "registry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UniversalAdIdOut"])
    types["OrderIn"] = t.struct(
        {
            "approverUserProfileIds": t.array(t.string()).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "planningTermId": t.string().optional(),
            "termsAndConditions": t.string().optional(),
            "buyerInvoiceId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "projectId": t.string().optional(),
            "contacts": t.array(t.proxy(renames["OrderContactIn"])).optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "buyerOrganizationName": t.string().optional(),
            "sellerOrderId": t.string().optional(),
            "id": t.string().optional(),
            "notes": t.string().optional(),
            "comments": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserId": t.string().optional(),
            "siteNames": t.array(t.string()).optional(),
            "sellerOrganizationName": t.string().optional(),
            "siteId": t.array(t.string()).optional(),
        }
    ).named(renames["OrderIn"])
    types["OrderOut"] = t.struct(
        {
            "approverUserProfileIds": t.array(t.string()).optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "planningTermId": t.string().optional(),
            "termsAndConditions": t.string().optional(),
            "buyerInvoiceId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "projectId": t.string().optional(),
            "contacts": t.array(t.proxy(renames["OrderContactOut"])).optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "buyerOrganizationName": t.string().optional(),
            "sellerOrderId": t.string().optional(),
            "id": t.string().optional(),
            "notes": t.string().optional(),
            "comments": t.string().optional(),
            "kind": t.string().optional(),
            "advertiserId": t.string().optional(),
            "siteNames": t.array(t.string()).optional(),
            "sellerOrganizationName": t.string().optional(),
            "siteId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderOut"])
    types["EncryptionInfoIn"] = t.struct(
        {
            "encryptionSource": t.string().optional(),
            "encryptionEntityType": t.string().optional(),
            "encryptionEntityId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["EncryptionInfoIn"])
    types["EncryptionInfoOut"] = t.struct(
        {
            "encryptionSource": t.string().optional(),
            "encryptionEntityType": t.string().optional(),
            "encryptionEntityId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionInfoOut"])
    types["PlacementStrategiesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "placementStrategies": t.array(
                t.proxy(renames["PlacementStrategyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PlacementStrategiesListResponseIn"])
    types["PlacementStrategiesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "placementStrategies": t.array(
                t.proxy(renames["PlacementStrategyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementStrategiesListResponseOut"])
    types["CountryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sslEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "countryCode": t.string().optional(),
            "dartId": t.string().optional(),
        }
    ).named(renames["CountryIn"])
    types["CountryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sslEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "countryCode": t.string().optional(),
            "dartId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountryOut"])
    types["ListPopulationClauseIn"] = t.struct(
        {"terms": t.array(t.proxy(renames["ListPopulationTermIn"])).optional()}
    ).named(renames["ListPopulationClauseIn"])
    types["ListPopulationClauseOut"] = t.struct(
        {
            "terms": t.array(t.proxy(renames["ListPopulationTermOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPopulationClauseOut"])
    types["CityIn"] = t.struct(
        {
            "metroDmaId": t.string().optional(),
            "metroCode": t.string().optional(),
            "regionDartId": t.string().optional(),
            "countryDartId": t.string().optional(),
            "dartId": t.string().optional(),
            "kind": t.string().optional(),
            "regionCode": t.string().optional(),
            "countryCode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CityIn"])
    types["CityOut"] = t.struct(
        {
            "metroDmaId": t.string().optional(),
            "metroCode": t.string().optional(),
            "regionDartId": t.string().optional(),
            "countryDartId": t.string().optional(),
            "dartId": t.string().optional(),
            "kind": t.string().optional(),
            "regionCode": t.string().optional(),
            "countryCode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CityOut"])
    types["SkippableSettingIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "progressOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
            "skippable": t.boolean().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
        }
    ).named(renames["SkippableSettingIn"])
    types["SkippableSettingOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "progressOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "skippable": t.boolean().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkippableSettingOut"])
    types["EventTagIn"] = t.struct(
        {
            "name": t.string().optional(),
            "campaignId": t.string().optional(),
            "enabledByDefault": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "campaignIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "siteFilterType": t.string().optional(),
            "url": t.string().optional(),
            "kind": t.string().optional(),
            "siteIds": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "urlEscapeLevels": t.integer().optional(),
            "subaccountId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "excludeFromAdxRequests": t.boolean().optional(),
        }
    ).named(renames["EventTagIn"])
    types["EventTagOut"] = t.struct(
        {
            "name": t.string().optional(),
            "campaignId": t.string().optional(),
            "enabledByDefault": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "accountId": t.string().optional(),
            "sslCompliant": t.boolean().optional(),
            "campaignIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "siteFilterType": t.string().optional(),
            "url": t.string().optional(),
            "kind": t.string().optional(),
            "siteIds": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "urlEscapeLevels": t.integer().optional(),
            "subaccountId": t.string().optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "excludeFromAdxRequests": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTagOut"])
    types["ListTargetingExpressionIn"] = t.struct(
        {"expression": t.string().optional()}
    ).named(renames["ListTargetingExpressionIn"])
    types["ListTargetingExpressionOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetingExpressionOut"])
    types["CustomFloodlightVariableIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["CustomFloodlightVariableIn"])
    types["CustomFloodlightVariableOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomFloodlightVariableOut"])
    types["MeasurementPartnerCampaignLinkIn"] = t.struct(
        {
            "partnerCampaignId": t.string().optional(),
            "measurementPartner": t.string().optional(),
            "linkStatus": t.string().optional(),
        }
    ).named(renames["MeasurementPartnerCampaignLinkIn"])
    types["MeasurementPartnerCampaignLinkOut"] = t.struct(
        {
            "partnerCampaignId": t.string().optional(),
            "measurementPartner": t.string().optional(),
            "linkStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeasurementPartnerCampaignLinkOut"])
    types["AdvertiserIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "defaultEmail": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "accountId": t.string().optional(),
            "clickThroughUrlSuffix": t.string().optional(),
            "subaccountId": t.string().optional(),
            "measurementPartnerLink": t.proxy(
                renames["MeasurementPartnerAdvertiserLinkIn"]
            ).optional(),
            "originalFloodlightConfigurationId": t.string().optional(),
            "defaultClickThroughEventTagId": t.string().optional(),
            "status": t.string().optional(),
            "advertiserGroupId": t.string().optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "suspended": t.boolean().optional(),
        }
    ).named(renames["AdvertiserIn"])
    types["AdvertiserOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "defaultEmail": t.string().optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "accountId": t.string().optional(),
            "clickThroughUrlSuffix": t.string().optional(),
            "subaccountId": t.string().optional(),
            "measurementPartnerLink": t.proxy(
                renames["MeasurementPartnerAdvertiserLinkOut"]
            ).optional(),
            "originalFloodlightConfigurationId": t.string().optional(),
            "defaultClickThroughEventTagId": t.string().optional(),
            "status": t.string().optional(),
            "advertiserGroupId": t.string().optional(),
            "floodlightConfigurationIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "floodlightConfigurationId": t.string().optional(),
            "suspended": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserOut"])
    types["EventTagsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "eventTags": t.array(t.proxy(renames["EventTagIn"])).optional(),
        }
    ).named(renames["EventTagsListResponseIn"])
    types["EventTagsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "eventTags": t.array(t.proxy(renames["EventTagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTagsListResponseOut"])
    types["GeoTargetingIn"] = t.struct(
        {
            "excludeCountries": t.boolean().optional(),
            "regions": t.array(t.proxy(renames["RegionIn"])).optional(),
            "countries": t.array(t.proxy(renames["CountryIn"])).optional(),
            "metros": t.array(t.proxy(renames["MetroIn"])).optional(),
            "cities": t.array(t.proxy(renames["CityIn"])).optional(),
            "postalCodes": t.array(t.proxy(renames["PostalCodeIn"])).optional(),
        }
    ).named(renames["GeoTargetingIn"])
    types["GeoTargetingOut"] = t.struct(
        {
            "excludeCountries": t.boolean().optional(),
            "regions": t.array(t.proxy(renames["RegionOut"])).optional(),
            "countries": t.array(t.proxy(renames["CountryOut"])).optional(),
            "metros": t.array(t.proxy(renames["MetroOut"])).optional(),
            "cities": t.array(t.proxy(renames["CityOut"])).optional(),
            "postalCodes": t.array(t.proxy(renames["PostalCodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoTargetingOut"])
    types["AccountPermissionsListResponseIn"] = t.struct(
        {
            "accountPermissions": t.array(
                t.proxy(renames["AccountPermissionIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountPermissionsListResponseIn"])
    types["AccountPermissionsListResponseOut"] = t.struct(
        {
            "accountPermissions": t.array(
                t.proxy(renames["AccountPermissionOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountPermissionsListResponseOut"])
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
    types["LookbackConfigurationIn"] = t.struct(
        {
            "clickDuration": t.integer().optional(),
            "postImpressionActivitiesDuration": t.integer().optional(),
        }
    ).named(renames["LookbackConfigurationIn"])
    types["LookbackConfigurationOut"] = t.struct(
        {
            "clickDuration": t.integer().optional(),
            "postImpressionActivitiesDuration": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookbackConfigurationOut"])
    types["SiteTranscodeSettingIn"] = t.struct(
        {
            "enabledVideoFormats": t.array(t.integer()).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SiteTranscodeSettingIn"])
    types["SiteTranscodeSettingOut"] = t.struct(
        {
            "enabledVideoFormats": t.array(t.integer()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteTranscodeSettingOut"])
    types["AdvertiserInvoicesListResponseIn"] = t.struct(
        {
            "invoices": t.array(t.proxy(renames["InvoiceIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AdvertiserInvoicesListResponseIn"])
    types["AdvertiserInvoicesListResponseOut"] = t.struct(
        {
            "invoices": t.array(t.proxy(renames["InvoiceOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserInvoicesListResponseOut"])
    types["CampaignSummaryIn"] = t.struct(
        {
            "taxAmountMicros": t.string().optional(),
            "preTaxAmountMicros": t.string().optional(),
            "billingInvoiceCode": t.string().optional(),
            "campaignId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
        }
    ).named(renames["CampaignSummaryIn"])
    types["CampaignSummaryOut"] = t.struct(
        {
            "taxAmountMicros": t.string().optional(),
            "preTaxAmountMicros": t.string().optional(),
            "billingInvoiceCode": t.string().optional(),
            "campaignId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignSummaryOut"])
    types["InvoiceIn"] = t.struct(
        {
            "dueDate": t.string().optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "correctedInvoiceId": t.string().optional(),
            "kind": t.string().optional(),
            "subtotalAmountMicros": t.string().optional(),
            "invoiceType": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "serviceEndDate": t.string().optional(),
            "serviceStartDate": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "campaign_summaries": t.array(
                t.proxy(renames["CampaignSummaryIn"])
            ).optional(),
            "id": t.string().optional(),
            "purchaseOrderNumber": t.string().optional(),
            "issueDate": t.string().optional(),
            "currencyCode": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "pdfUrl": t.string().optional(),
        }
    ).named(renames["InvoiceIn"])
    types["InvoiceOut"] = t.struct(
        {
            "dueDate": t.string().optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "correctedInvoiceId": t.string().optional(),
            "kind": t.string().optional(),
            "subtotalAmountMicros": t.string().optional(),
            "invoiceType": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "serviceEndDate": t.string().optional(),
            "serviceStartDate": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "campaign_summaries": t.array(
                t.proxy(renames["CampaignSummaryOut"])
            ).optional(),
            "id": t.string().optional(),
            "purchaseOrderNumber": t.string().optional(),
            "issueDate": t.string().optional(),
            "currencyCode": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceOut"])
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
    types["TagSettingIn"] = t.struct(
        {
            "includeClickTracking": t.boolean().optional(),
            "keywordOption": t.string().optional(),
            "additionalKeyValues": t.string().optional(),
            "includeClickThroughUrls": t.boolean().optional(),
        }
    ).named(renames["TagSettingIn"])
    types["TagSettingOut"] = t.struct(
        {
            "includeClickTracking": t.boolean().optional(),
            "keywordOption": t.string().optional(),
            "additionalKeyValues": t.string().optional(),
            "includeClickThroughUrls": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagSettingOut"])
    types["CampaignsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "campaigns": t.array(t.proxy(renames["CampaignIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CampaignsListResponseIn"])
    types["CampaignsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "campaigns": t.array(t.proxy(renames["CampaignOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignsListResponseOut"])
    types["CreativeCustomEventIn"] = t.struct(
        {
            "targetType": t.string().optional(),
            "advertiserCustomEventType": t.string().optional(),
            "exitClickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlIn"]
            ).optional(),
            "videoReportingId": t.string().optional(),
            "advertiserCustomEventName": t.string().optional(),
            "artworkType": t.string().optional(),
            "popupWindowProperties": t.proxy(
                renames["PopupWindowPropertiesIn"]
            ).optional(),
            "artworkLabel": t.string().optional(),
            "id": t.string().optional(),
            "advertiserCustomEventId": t.string().optional(),
        }
    ).named(renames["CreativeCustomEventIn"])
    types["CreativeCustomEventOut"] = t.struct(
        {
            "targetType": t.string().optional(),
            "advertiserCustomEventType": t.string().optional(),
            "exitClickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlOut"]
            ).optional(),
            "videoReportingId": t.string().optional(),
            "advertiserCustomEventName": t.string().optional(),
            "artworkType": t.string().optional(),
            "popupWindowProperties": t.proxy(
                renames["PopupWindowPropertiesOut"]
            ).optional(),
            "artworkLabel": t.string().optional(),
            "id": t.string().optional(),
            "advertiserCustomEventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeCustomEventOut"])
    types["UserRolePermissionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "permissionGroupId": t.string().optional(),
            "id": t.string().optional(),
            "availability": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["UserRolePermissionIn"])
    types["UserRolePermissionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "permissionGroupId": t.string().optional(),
            "id": t.string().optional(),
            "availability": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRolePermissionOut"])
    types["ObaIconIn"] = t.struct(
        {
            "yPosition": t.string().optional(),
            "program": t.string().optional(),
            "iconClickTrackingUrl": t.string().optional(),
            "iconViewTrackingUrl": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "iconClickThroughUrl": t.string().optional(),
            "xPosition": t.string().optional(),
        }
    ).named(renames["ObaIconIn"])
    types["ObaIconOut"] = t.struct(
        {
            "yPosition": t.string().optional(),
            "program": t.string().optional(),
            "iconClickTrackingUrl": t.string().optional(),
            "iconViewTrackingUrl": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "iconClickThroughUrl": t.string().optional(),
            "xPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObaIconOut"])
    types["PlacementAssignmentIn"] = t.struct(
        {
            "placementIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "active": t.boolean().optional(),
            "placementId": t.string().optional(),
            "sslRequired": t.boolean().optional(),
        }
    ).named(renames["PlacementAssignmentIn"])
    types["PlacementAssignmentOut"] = t.struct(
        {
            "placementIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "active": t.boolean().optional(),
            "placementId": t.string().optional(),
            "sslRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementAssignmentOut"])
    types["ConversionStatusIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ConversionErrorIn"])).optional(),
            "kind": t.string().optional(),
            "conversion": t.proxy(renames["ConversionIn"]).optional(),
        }
    ).named(renames["ConversionStatusIn"])
    types["ConversionStatusOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ConversionErrorOut"])).optional(),
            "kind": t.string().optional(),
            "conversion": t.proxy(renames["ConversionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionStatusOut"])
    types["PlacementStrategyIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PlacementStrategyIn"])
    types["PlacementStrategyOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementStrategyOut"])
    types["ActivitiesIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "metricNames": t.array(t.string()).optional(),
            "filters": t.array(t.proxy(renames["DimensionValueIn"])).optional(),
        }
    ).named(renames["ActivitiesIn"])
    types["ActivitiesOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "metricNames": t.array(t.string()).optional(),
            "filters": t.array(t.proxy(renames["DimensionValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitiesOut"])
    types["PathFilterIn"] = t.struct(
        {
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional(),
            "pathMatchPosition": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PathFilterIn"])
    types["PathFilterOut"] = t.struct(
        {
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "pathMatchPosition": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathFilterOut"])
    types["ContentCategoryIn"] = t.struct(
        {
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ContentCategoryIn"])
    types["ContentCategoryOut"] = t.struct(
        {
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentCategoryOut"])
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
    types["DayPartTargetingIn"] = t.struct(
        {
            "daysOfWeek": t.array(t.string()).optional(),
            "userLocalTime": t.boolean().optional(),
            "hoursOfDay": t.array(t.integer()).optional(),
        }
    ).named(renames["DayPartTargetingIn"])
    types["DayPartTargetingOut"] = t.struct(
        {
            "daysOfWeek": t.array(t.string()).optional(),
            "userLocalTime": t.boolean().optional(),
            "hoursOfDay": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartTargetingOut"])
    types["SiteCompanionSettingIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "companionsDisabled": t.boolean().optional(),
            "imageOnly": t.boolean().optional(),
            "enabledSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
        }
    ).named(renames["SiteCompanionSettingIn"])
    types["SiteCompanionSettingOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "companionsDisabled": t.boolean().optional(),
            "imageOnly": t.boolean().optional(),
            "enabledSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteCompanionSettingOut"])
    types["AccountPermissionIn"] = t.struct(
        {
            "level": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "permissionGroupId": t.string().optional(),
            "accountProfiles": t.array(t.string()).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AccountPermissionIn"])
    types["AccountPermissionOut"] = t.struct(
        {
            "level": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "permissionGroupId": t.string().optional(),
            "accountProfiles": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountPermissionOut"])
    types["AudienceSegmentGroupIn"] = t.struct(
        {
            "audienceSegments": t.array(
                t.proxy(renames["AudienceSegmentIn"])
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AudienceSegmentGroupIn"])
    types["AudienceSegmentGroupOut"] = t.struct(
        {
            "audienceSegments": t.array(
                t.proxy(renames["AudienceSegmentOut"])
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudienceSegmentGroupOut"])
    types["RemarketingListShareIn"] = t.struct(
        {
            "sharedAccountIds": t.array(t.string()).optional(),
            "remarketingListId": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RemarketingListShareIn"])
    types["RemarketingListShareOut"] = t.struct(
        {
            "sharedAccountIds": t.array(t.string()).optional(),
            "remarketingListId": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingListShareOut"])
    types["AudienceSegmentIn"] = t.struct(
        {
            "id": t.string().optional(),
            "allocation": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AudienceSegmentIn"])
    types["AudienceSegmentOut"] = t.struct(
        {
            "id": t.string().optional(),
            "allocation": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudienceSegmentOut"])
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
    types["MobileCarrierIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "countryDartId": t.string().optional(),
            "countryCode": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MobileCarrierIn"])
    types["MobileCarrierOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "countryDartId": t.string().optional(),
            "countryCode": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileCarrierOut"])
    types["ListPopulationRuleIn"] = t.struct(
        {
            "floodlightActivityName": t.string().optional(),
            "listPopulationClauses": t.array(
                t.proxy(renames["ListPopulationClauseIn"])
            ).optional(),
            "floodlightActivityId": t.string().optional(),
        }
    ).named(renames["ListPopulationRuleIn"])
    types["ListPopulationRuleOut"] = t.struct(
        {
            "floodlightActivityName": t.string().optional(),
            "listPopulationClauses": t.array(
                t.proxy(renames["ListPopulationClauseOut"])
            ).optional(),
            "floodlightActivityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPopulationRuleOut"])
    types["MobileCarriersListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "mobileCarriers": t.array(t.proxy(renames["MobileCarrierIn"])).optional(),
        }
    ).named(renames["MobileCarriersListResponseIn"])
    types["MobileCarriersListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "mobileCarriers": t.array(t.proxy(renames["MobileCarrierOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileCarriersListResponseOut"])
    types["UserRoleIn"] = t.struct(
        {
            "parentUserRoleId": t.string().optional(),
            "permissions": t.array(t.proxy(renames["UserRolePermissionIn"])).optional(),
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "defaultUserRole": t.boolean().optional(),
        }
    ).named(renames["UserRoleIn"])
    types["UserRoleOut"] = t.struct(
        {
            "parentUserRoleId": t.string().optional(),
            "permissions": t.array(
                t.proxy(renames["UserRolePermissionOut"])
            ).optional(),
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "subaccountId": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "defaultUserRole": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRoleOut"])
    types["AccountsListResponseIn"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["AccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountsListResponseIn"])
    types["AccountsListResponseOut"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["AccountOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsListResponseOut"])
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
    types["SiteVideoSettingsIn"] = t.struct(
        {
            "companionSettings": t.proxy(renames["SiteCompanionSettingIn"]).optional(),
            "publisherSpecificationId": t.string().optional(),
            "orientation": t.string().optional(),
            "skippableSettings": t.proxy(renames["SiteSkippableSettingIn"]).optional(),
            "obaEnabled": t.boolean().optional(),
            "transcodeSettings": t.proxy(renames["SiteTranscodeSettingIn"]).optional(),
            "obaSettings": t.proxy(renames["ObaIconIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SiteVideoSettingsIn"])
    types["SiteVideoSettingsOut"] = t.struct(
        {
            "companionSettings": t.proxy(renames["SiteCompanionSettingOut"]).optional(),
            "publisherSpecificationId": t.string().optional(),
            "orientation": t.string().optional(),
            "skippableSettings": t.proxy(renames["SiteSkippableSettingOut"]).optional(),
            "obaEnabled": t.boolean().optional(),
            "transcodeSettings": t.proxy(renames["SiteTranscodeSettingOut"]).optional(),
            "obaSettings": t.proxy(renames["ObaIconOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteVideoSettingsOut"])
    types["OrderContactIn"] = t.struct(
        {
            "contactTitle": t.string().optional(),
            "signatureUserProfileId": t.string().optional(),
            "contactInfo": t.string().optional(),
            "contactName": t.string().optional(),
            "contactType": t.string().optional(),
        }
    ).named(renames["OrderContactIn"])
    types["OrderContactOut"] = t.struct(
        {
            "contactTitle": t.string().optional(),
            "signatureUserProfileId": t.string().optional(),
            "contactInfo": t.string().optional(),
            "contactName": t.string().optional(),
            "contactType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderContactOut"])
    types["PricingIn"] = t.struct(
        {
            "groupType": t.string().optional(),
            "startDate": t.string(),
            "capCostType": t.string().optional(),
            "flights": t.array(t.proxy(renames["FlightIn"])).optional(),
            "endDate": t.string(),
            "pricingType": t.string().optional(),
        }
    ).named(renames["PricingIn"])
    types["PricingOut"] = t.struct(
        {
            "groupType": t.string().optional(),
            "startDate": t.string(),
            "capCostType": t.string().optional(),
            "flights": t.array(t.proxy(renames["FlightOut"])).optional(),
            "endDate": t.string(),
            "pricingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingOut"])
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
    types["UserIdentifierIn"] = t.struct(
        {
            "addressInfo": t.proxy(renames["OfflineUserAddressInfoIn"]).optional(),
            "hashedPhoneNumber": t.string().optional(),
            "hashedEmail": t.string().optional(),
        }
    ).named(renames["UserIdentifierIn"])
    types["UserIdentifierOut"] = t.struct(
        {
            "addressInfo": t.proxy(renames["OfflineUserAddressInfoOut"]).optional(),
            "hashedPhoneNumber": t.string().optional(),
            "hashedEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserIdentifierOut"])
    types["KeyValueTargetingExpressionIn"] = t.struct(
        {"expression": t.string().optional()}
    ).named(renames["KeyValueTargetingExpressionIn"])
    types["KeyValueTargetingExpressionOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueTargetingExpressionOut"])
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
    types["FlightIn"] = t.struct(
        {
            "units": t.string().optional(),
            "rateOrCost": t.string().optional(),
            "endDate": t.string(),
            "startDate": t.string(),
        }
    ).named(renames["FlightIn"])
    types["FlightOut"] = t.struct(
        {
            "units": t.string().optional(),
            "rateOrCost": t.string().optional(),
            "endDate": t.string(),
            "startDate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlightOut"])
    types["RegionsListResponseIn"] = t.struct(
        {
            "regions": t.array(t.proxy(renames["RegionIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RegionsListResponseIn"])
    types["RegionsListResponseOut"] = t.struct(
        {
            "regions": t.array(t.proxy(renames["RegionOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionsListResponseOut"])
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
    types["DeepLinkIn"] = t.struct(
        {
            "remarketingListIds": t.array(t.string()).optional(),
            "appUrl": t.string().optional(),
            "kind": t.string().optional(),
            "fallbackUrl": t.string().optional(),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
        }
    ).named(renames["DeepLinkIn"])
    types["DeepLinkOut"] = t.struct(
        {
            "remarketingListIds": t.array(t.string()).optional(),
            "appUrl": t.string().optional(),
            "kind": t.string().optional(),
            "fallbackUrl": t.string().optional(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeepLinkOut"])
    types["CompanionSettingIn"] = t.struct(
        {
            "companionsDisabled": t.boolean().optional(),
            "imageOnly": t.boolean().optional(),
            "kind": t.string().optional(),
            "enabledSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
        }
    ).named(renames["CompanionSettingIn"])
    types["CompanionSettingOut"] = t.struct(
        {
            "companionsDisabled": t.boolean().optional(),
            "imageOnly": t.boolean().optional(),
            "kind": t.string().optional(),
            "enabledSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanionSettingOut"])
    types["SitesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "sites": t.array(t.proxy(renames["SiteIn"])).optional(),
        }
    ).named(renames["SitesListResponseIn"])
    types["SitesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitesListResponseOut"])
    types["ProjectIn"] = t.struct(
        {
            "overview": t.string().optional(),
            "targetClicks": t.string().optional(),
            "id": t.string().optional(),
            "targetCpmNanos": t.string().optional(),
            "clientName": t.string().optional(),
            "targetImpressions": t.string().optional(),
            "advertiserId": t.string().optional(),
            "startDate": t.string(),
            "subaccountId": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "kind": t.string().optional(),
            "targetCpaNanos": t.string().optional(),
            "accountId": t.string().optional(),
            "audienceAgeGroup": t.string().optional(),
            "budget": t.string().optional(),
            "name": t.string().optional(),
            "audienceGender": t.string().optional(),
            "endDate": t.string(),
            "targetCpcNanos": t.string().optional(),
            "targetConversions": t.string().optional(),
            "clientBillingCode": t.string().optional(),
            "targetCpmActiveViewNanos": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "overview": t.string().optional(),
            "targetClicks": t.string().optional(),
            "id": t.string().optional(),
            "targetCpmNanos": t.string().optional(),
            "clientName": t.string().optional(),
            "targetImpressions": t.string().optional(),
            "advertiserId": t.string().optional(),
            "startDate": t.string(),
            "subaccountId": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "kind": t.string().optional(),
            "targetCpaNanos": t.string().optional(),
            "accountId": t.string().optional(),
            "audienceAgeGroup": t.string().optional(),
            "budget": t.string().optional(),
            "name": t.string().optional(),
            "audienceGender": t.string().optional(),
            "endDate": t.string(),
            "targetCpcNanos": t.string().optional(),
            "targetConversions": t.string().optional(),
            "clientBillingCode": t.string().optional(),
            "targetCpmActiveViewNanos": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["ListPopulationTermIn"] = t.struct(
        {
            "variableName": t.string().optional(),
            "type": t.string().optional(),
            "remarketingListId": t.string().optional(),
            "negation": t.boolean().optional(),
            "contains": t.boolean().optional(),
            "operator": t.string().optional(),
            "variableFriendlyName": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["ListPopulationTermIn"])
    types["ListPopulationTermOut"] = t.struct(
        {
            "variableName": t.string().optional(),
            "type": t.string().optional(),
            "remarketingListId": t.string().optional(),
            "negation": t.boolean().optional(),
            "contains": t.boolean().optional(),
            "operator": t.string().optional(),
            "variableFriendlyName": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPopulationTermOut"])
    types["OmnitureSettingsIn"] = t.struct(
        {
            "omnitureCostDataEnabled": t.boolean().optional(),
            "omnitureIntegrationEnabled": t.boolean().optional(),
        }
    ).named(renames["OmnitureSettingsIn"])
    types["OmnitureSettingsOut"] = t.struct(
        {
            "omnitureCostDataEnabled": t.boolean().optional(),
            "omnitureIntegrationEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmnitureSettingsOut"])
    types["DimensionValueListIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["DimensionValueIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DimensionValueListIn"])
    types["DimensionValueListOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["DimensionValueOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueListOut"])
    types["VideoFormatIn"] = t.struct(
        {
            "fileType": t.string().optional(),
            "kind": t.string().optional(),
            "resolution": t.proxy(renames["SizeIn"]).optional(),
            "targetBitRate": t.integer().optional(),
            "id": t.integer().optional(),
        }
    ).named(renames["VideoFormatIn"])
    types["VideoFormatOut"] = t.struct(
        {
            "fileType": t.string().optional(),
            "kind": t.string().optional(),
            "resolution": t.proxy(renames["SizeOut"]).optional(),
            "targetBitRate": t.integer().optional(),
            "id": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFormatOut"])
    types["CampaignIn"] = t.struct(
        {
            "measurementPartnerLink": t.proxy(
                renames["MeasurementPartnerCampaignLinkIn"]
            ).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueIn"]
            ).optional(),
            "accountId": t.string().optional(),
            "eventTagOverrides": t.array(
                t.proxy(renames["EventTagOverrideIn"])
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "billingInvoiceCode": t.string().optional(),
            "endDate": t.string(),
            "creativeGroupIds": t.array(t.string()).optional(),
            "comment": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "defaultClickThroughEventTagProperties": t.proxy(
                renames["DefaultClickThroughEventTagPropertiesIn"]
            ).optional(),
            "creativeOptimizationConfiguration": t.proxy(
                renames["CreativeOptimizationConfigurationIn"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "advertiserGroupId": t.string().optional(),
            "startDate": t.string(),
            "audienceSegmentGroups": t.array(
                t.proxy(renames["AudienceSegmentGroupIn"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "adBlockingConfiguration": t.proxy(
                renames["AdBlockingConfigurationIn"]
            ).optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
            "clickThroughUrlSuffixProperties": t.proxy(
                renames["ClickThroughUrlSuffixPropertiesIn"]
            ).optional(),
            "defaultLandingPageId": t.string().optional(),
            "externalId": t.string().optional(),
            "archived": t.boolean().optional(),
            "kind": t.string().optional(),
            "additionalCreativeOptimizationConfigurations": t.array(
                t.proxy(renames["CreativeOptimizationConfigurationIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CampaignIn"])
    types["CampaignOut"] = t.struct(
        {
            "measurementPartnerLink": t.proxy(
                renames["MeasurementPartnerCampaignLinkOut"]
            ).optional(),
            "advertiserIdDimensionValue": t.proxy(
                renames["DimensionValueOut"]
            ).optional(),
            "accountId": t.string().optional(),
            "eventTagOverrides": t.array(
                t.proxy(renames["EventTagOverrideOut"])
            ).optional(),
            "idDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "billingInvoiceCode": t.string().optional(),
            "endDate": t.string(),
            "creativeGroupIds": t.array(t.string()).optional(),
            "comment": t.string().optional(),
            "lastModifiedInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "defaultClickThroughEventTagProperties": t.proxy(
                renames["DefaultClickThroughEventTagPropertiesOut"]
            ).optional(),
            "creativeOptimizationConfiguration": t.proxy(
                renames["CreativeOptimizationConfigurationOut"]
            ).optional(),
            "subaccountId": t.string().optional(),
            "id": t.string().optional(),
            "advertiserGroupId": t.string().optional(),
            "startDate": t.string(),
            "audienceSegmentGroups": t.array(
                t.proxy(renames["AudienceSegmentGroupOut"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "adBlockingConfiguration": t.proxy(
                renames["AdBlockingConfigurationOut"]
            ).optional(),
            "createInfo": t.proxy(renames["LastModifiedInfoOut"]).optional(),
            "clickThroughUrlSuffixProperties": t.proxy(
                renames["ClickThroughUrlSuffixPropertiesOut"]
            ).optional(),
            "defaultLandingPageId": t.string().optional(),
            "externalId": t.string().optional(),
            "archived": t.boolean().optional(),
            "kind": t.string().optional(),
            "additionalCreativeOptimizationConfigurations": t.array(
                t.proxy(renames["CreativeOptimizationConfigurationOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignOut"])
    types["RegionIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "kind": t.string().optional(),
            "dartId": t.string().optional(),
            "countryDartId": t.string().optional(),
            "countryCode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RegionIn"])
    types["RegionOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "kind": t.string().optional(),
            "dartId": t.string().optional(),
            "countryDartId": t.string().optional(),
            "countryCode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionOut"])
    types["PathReportDimensionValueIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "dimensionName": t.string().optional(),
            "ids": t.array(t.string()).optional(),
            "matchType": t.string().optional(),
        }
    ).named(renames["PathReportDimensionValueIn"])
    types["PathReportDimensionValueOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "dimensionName": t.string().optional(),
            "ids": t.array(t.string()).optional(),
            "matchType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathReportDimensionValueOut"])
    types["AdSlotIn"] = t.struct(
        {
            "linkedPlacementId": t.string().optional(),
            "primary": t.boolean().optional(),
            "name": t.string().optional(),
            "compatibility": t.string().optional(),
            "paymentSourceType": t.string().optional(),
            "width": t.string().optional(),
            "comment": t.string().optional(),
            "height": t.string().optional(),
        }
    ).named(renames["AdSlotIn"])
    types["AdSlotOut"] = t.struct(
        {
            "linkedPlacementId": t.string().optional(),
            "primary": t.boolean().optional(),
            "name": t.string().optional(),
            "compatibility": t.string().optional(),
            "paymentSourceType": t.string().optional(),
            "width": t.string().optional(),
            "comment": t.string().optional(),
            "height": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSlotOut"])
    types["MobileAppIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "title": t.string().optional(),
            "publisherName": t.string().optional(),
            "id": t.string().optional(),
            "directory": t.string().optional(),
        }
    ).named(renames["MobileAppIn"])
    types["MobileAppOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "title": t.string().optional(),
            "publisherName": t.string().optional(),
            "id": t.string().optional(),
            "directory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileAppOut"])
    types["FloodlightActivitiesGenerateTagResponseIn"] = t.struct(
        {
            "globalSiteTagGlobalSnippet": t.string().optional(),
            "kind": t.string().optional(),
            "floodlightActivityTag": t.string().optional(),
        }
    ).named(renames["FloodlightActivitiesGenerateTagResponseIn"])
    types["FloodlightActivitiesGenerateTagResponseOut"] = t.struct(
        {
            "globalSiteTagGlobalSnippet": t.string().optional(),
            "kind": t.string().optional(),
            "floodlightActivityTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivitiesGenerateTagResponseOut"])
    types["AdBlockingConfigurationIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdBlockingConfigurationIn"])
    types["AdBlockingConfigurationOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdBlockingConfigurationOut"])
    types["LastModifiedInfoIn"] = t.struct({"time": t.string().optional()}).named(
        renames["LastModifiedInfoIn"]
    )
    types["LastModifiedInfoOut"] = t.struct(
        {
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LastModifiedInfoOut"])
    types["BillingAssignmentsListResponseIn"] = t.struct(
        {
            "billingAssignments": t.array(
                t.proxy(renames["BillingAssignmentIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BillingAssignmentsListResponseIn"])
    types["BillingAssignmentsListResponseOut"] = t.struct(
        {
            "billingAssignments": t.array(
                t.proxy(renames["BillingAssignmentOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingAssignmentsListResponseOut"])
    types["AccountUserProfilesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "accountUserProfiles": t.array(
                t.proxy(renames["AccountUserProfileIn"])
            ).optional(),
        }
    ).named(renames["AccountUserProfilesListResponseIn"])
    types["AccountUserProfilesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "accountUserProfiles": t.array(
                t.proxy(renames["AccountUserProfileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountUserProfilesListResponseOut"])
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
    types["ConversionsBatchUpdateResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "hasFailures": t.boolean().optional(),
            "status": t.array(t.proxy(renames["ConversionStatusIn"])).optional(),
        }
    ).named(renames["ConversionsBatchUpdateResponseIn"])
    types["ConversionsBatchUpdateResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "hasFailures": t.boolean().optional(),
            "status": t.array(t.proxy(renames["ConversionStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionsBatchUpdateResponseOut"])
    types["MeasurementPartnerAdvertiserLinkIn"] = t.struct(
        {
            "partnerAdvertiserId": t.string().optional(),
            "linkStatus": t.string().optional(),
            "measurementPartner": t.string().optional(),
        }
    ).named(renames["MeasurementPartnerAdvertiserLinkIn"])
    types["MeasurementPartnerAdvertiserLinkOut"] = t.struct(
        {
            "partnerAdvertiserId": t.string().optional(),
            "linkStatus": t.string().optional(),
            "measurementPartner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeasurementPartnerAdvertiserLinkOut"])
    types["FloodlightActivityPublisherDynamicTagIn"] = t.struct(
        {
            "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
            "dynamicTag": t.proxy(renames["FloodlightActivityDynamicTagIn"]).optional(),
            "siteId": t.string().optional(),
            "viewThrough": t.boolean().optional(),
            "clickThrough": t.boolean().optional(),
            "directorySiteId": t.string().optional(),
        }
    ).named(renames["FloodlightActivityPublisherDynamicTagIn"])
    types["FloodlightActivityPublisherDynamicTagOut"] = t.struct(
        {
            "siteIdDimensionValue": t.proxy(renames["DimensionValueOut"]).optional(),
            "dynamicTag": t.proxy(
                renames["FloodlightActivityDynamicTagOut"]
            ).optional(),
            "siteId": t.string().optional(),
            "viewThrough": t.boolean().optional(),
            "clickThrough": t.boolean().optional(),
            "directorySiteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightActivityPublisherDynamicTagOut"])
    types["ClickTagIn"] = t.struct(
        {
            "eventName": t.string().optional(),
            "name": t.string().optional(),
            "clickThroughUrl": t.proxy(renames["CreativeClickThroughUrlIn"]).optional(),
        }
    ).named(renames["ClickTagIn"])
    types["ClickTagOut"] = t.struct(
        {
            "eventName": t.string().optional(),
            "name": t.string().optional(),
            "clickThroughUrl": t.proxy(
                renames["CreativeClickThroughUrlOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClickTagOut"])
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
    types["AccountIn"] = t.struct(
        {
            "description": t.string().optional(),
            "teaserSizeLimit": t.string().optional(),
            "nielsenOcrEnabled": t.boolean().optional(),
            "reportsConfiguration": t.proxy(
                renames["ReportsConfigurationIn"]
            ).optional(),
            "name": t.string().optional(),
            "currencyId": t.string().optional(),
            "maximumImageSize": t.string().optional(),
            "accountPermissionIds": t.array(t.string()).optional(),
            "active": t.boolean().optional(),
            "id": t.string().optional(),
            "activeAdsLimitTier": t.string().optional(),
            "locale": t.string().optional(),
            "defaultCreativeSizeId": t.string().optional(),
            "shareReportsWithTwitter": t.boolean().optional(),
            "kind": t.string().optional(),
            "availablePermissionIds": t.array(t.string()).optional(),
            "activeViewOptOut": t.boolean().optional(),
            "accountProfile": t.string().optional(),
            "countryId": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "description": t.string().optional(),
            "teaserSizeLimit": t.string().optional(),
            "nielsenOcrEnabled": t.boolean().optional(),
            "reportsConfiguration": t.proxy(
                renames["ReportsConfigurationOut"]
            ).optional(),
            "name": t.string().optional(),
            "currencyId": t.string().optional(),
            "maximumImageSize": t.string().optional(),
            "accountPermissionIds": t.array(t.string()).optional(),
            "active": t.boolean().optional(),
            "id": t.string().optional(),
            "activeAdsLimitTier": t.string().optional(),
            "locale": t.string().optional(),
            "defaultCreativeSizeId": t.string().optional(),
            "shareReportsWithTwitter": t.boolean().optional(),
            "kind": t.string().optional(),
            "availablePermissionIds": t.array(t.string()).optional(),
            "activeViewOptOut": t.boolean().optional(),
            "accountProfile": t.string().optional(),
            "countryId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["CreativesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "creatives": t.array(t.proxy(renames["CreativeIn"])).optional(),
        }
    ).named(renames["CreativesListResponseIn"])
    types["CreativesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "creatives": t.array(t.proxy(renames["CreativeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativesListResponseOut"])
    types["ThirdPartyTrackingUrlIn"] = t.struct(
        {"thirdPartyUrlType": t.string().optional(), "url": t.string().optional()}
    ).named(renames["ThirdPartyTrackingUrlIn"])
    types["ThirdPartyTrackingUrlOut"] = t.struct(
        {
            "thirdPartyUrlType": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyTrackingUrlOut"])
    types["FsCommandIn"] = t.struct(
        {
            "windowHeight": t.integer().optional(),
            "top": t.integer().optional(),
            "windowWidth": t.integer().optional(),
            "left": t.integer().optional(),
            "positionOption": t.string().optional(),
        }
    ).named(renames["FsCommandIn"])
    types["FsCommandOut"] = t.struct(
        {
            "windowHeight": t.integer().optional(),
            "top": t.integer().optional(),
            "windowWidth": t.integer().optional(),
            "left": t.integer().optional(),
            "positionOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FsCommandOut"])
    types["ReachReportCompatibleFieldsIn"] = t.struct(
        {
            "reachByFrequencyMetrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "pivotedActivityMetrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReachReportCompatibleFieldsIn"])
    types["ReachReportCompatibleFieldsOut"] = t.struct(
        {
            "reachByFrequencyMetrics": t.array(
                t.proxy(renames["MetricOut"])
            ).optional(),
            "pivotedActivityMetrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensionFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReachReportCompatibleFieldsOut"])
    types["ConnectionTypeIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ConnectionTypeIn"])
    types["ConnectionTypeOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionTypeOut"])
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
    types["PlacementsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "placements": t.array(t.proxy(renames["PlacementIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlacementsListResponseIn"])
    types["PlacementsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "placements": t.array(t.proxy(renames["PlacementOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementsListResponseOut"])
    types["AccountPermissionGroupIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AccountPermissionGroupIn"])
    types["AccountPermissionGroupOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountPermissionGroupOut"])
    types["DirectorySiteSettingsIn"] = t.struct(
        {
            "activeViewOptOut": t.boolean().optional(),
            "dfpSettings": t.proxy(renames["DfpSettingsIn"]).optional(),
            "interstitialPlacementAccepted": t.boolean().optional(),
            "instreamVideoPlacementAccepted": t.boolean().optional(),
        }
    ).named(renames["DirectorySiteSettingsIn"])
    types["DirectorySiteSettingsOut"] = t.struct(
        {
            "activeViewOptOut": t.boolean().optional(),
            "dfpSettings": t.proxy(renames["DfpSettingsOut"]).optional(),
            "interstitialPlacementAccepted": t.boolean().optional(),
            "instreamVideoPlacementAccepted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectorySiteSettingsOut"])
    types["RichMediaExitOverrideIn"] = t.struct(
        {
            "exitId": t.string().optional(),
            "enabled": t.boolean().optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlIn"]).optional(),
        }
    ).named(renames["RichMediaExitOverrideIn"])
    types["RichMediaExitOverrideOut"] = t.struct(
        {
            "exitId": t.string().optional(),
            "enabled": t.boolean().optional(),
            "clickThroughUrl": t.proxy(renames["ClickThroughUrlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichMediaExitOverrideOut"])
    types["OperatingSystemVersionIn"] = t.struct(
        {
            "majorVersion": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "operatingSystem": t.proxy(renames["OperatingSystemIn"]).optional(),
            "minorVersion": t.string().optional(),
        }
    ).named(renames["OperatingSystemVersionIn"])
    types["OperatingSystemVersionOut"] = t.struct(
        {
            "majorVersion": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "operatingSystem": t.proxy(renames["OperatingSystemOut"]).optional(),
            "minorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemVersionOut"])
    types["CitiesListResponseIn"] = t.struct(
        {
            "cities": t.array(t.proxy(renames["CityIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CitiesListResponseIn"])
    types["CitiesListResponseOut"] = t.struct(
        {
            "cities": t.array(t.proxy(renames["CityOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CitiesListResponseOut"])
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
    types["ChangeLogsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "changeLogs": t.array(t.proxy(renames["ChangeLogIn"])).optional(),
        }
    ).named(renames["ChangeLogsListResponseIn"])
    types["ChangeLogsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "changeLogs": t.array(t.proxy(renames["ChangeLogOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeLogsListResponseOut"])
    types["PathReportCompatibleFieldsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "channelGroupings": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "pathFilters": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["PathReportCompatibleFieldsIn"])
    types["PathReportCompatibleFieldsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "channelGroupings": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "pathFilters": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathReportCompatibleFieldsOut"])
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
    types["TargetingTemplatesListResponseIn"] = t.struct(
        {
            "targetingTemplates": t.array(
                t.proxy(renames["TargetingTemplateIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["TargetingTemplatesListResponseIn"])
    types["TargetingTemplatesListResponseOut"] = t.struct(
        {
            "targetingTemplates": t.array(
                t.proxy(renames["TargetingTemplateOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingTemplatesListResponseOut"])
    types["SiteSkippableSettingIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
            "skippable": t.boolean().optional(),
            "progressOffset": t.proxy(renames["VideoOffsetIn"]).optional(),
        }
    ).named(renames["SiteSkippableSettingIn"])
    types["SiteSkippableSettingOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "skipOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "skippable": t.boolean().optional(),
            "progressOffset": t.proxy(renames["VideoOffsetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteSkippableSettingOut"])

    functions = {}
    functions["directorySitesInsert"] = dfareporting.get(
        "userprofiles/{profileId}/directorySites/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DirectorySiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["directorySitesList"] = dfareporting.get(
        "userprofiles/{profileId}/directorySites/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DirectorySiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["directorySitesGet"] = dfareporting.get(
        "userprofiles/{profileId}/directorySites/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DirectorySiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventoryItemsList"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/inventoryItems/{id}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventoryItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventoryItemsGet"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/inventoryItems/{id}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventoryItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserInvoicesList"] = dfareporting.get(
        "userprofiles/{profileId}/advertisers/{advertiserId}/invoices",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "issueMonth": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserInvoicesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "searchString": t.string().optional(),
                "sortField": t.string().optional(),
                "advertiserGroupIds": t.string().optional(),
                "archived": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "subaccountId": t.string().optional(),
                "atLeastOneOptimizationActivity": t.boolean().optional(),
                "advertiserIds": t.string().optional(),
                "excludedIds": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "maxResults": t.integer().optional(),
                "overriddenEventTagId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsGet"] = dfareporting.get(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "searchString": t.string().optional(),
                "sortField": t.string().optional(),
                "advertiserGroupIds": t.string().optional(),
                "archived": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "subaccountId": t.string().optional(),
                "atLeastOneOptimizationActivity": t.boolean().optional(),
                "advertiserIds": t.string().optional(),
                "excludedIds": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "maxResults": t.integer().optional(),
                "overriddenEventTagId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "searchString": t.string().optional(),
                "sortField": t.string().optional(),
                "advertiserGroupIds": t.string().optional(),
                "archived": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "subaccountId": t.string().optional(),
                "atLeastOneOptimizationActivity": t.boolean().optional(),
                "advertiserIds": t.string().optional(),
                "excludedIds": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "maxResults": t.integer().optional(),
                "overriddenEventTagId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "searchString": t.string().optional(),
                "sortField": t.string().optional(),
                "advertiserGroupIds": t.string().optional(),
                "archived": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "subaccountId": t.string().optional(),
                "atLeastOneOptimizationActivity": t.boolean().optional(),
                "advertiserIds": t.string().optional(),
                "excludedIds": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "maxResults": t.integer().optional(),
                "overriddenEventTagId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignsList"] = dfareporting.get(
        "userprofiles/{profileId}/campaigns",
        t.struct(
            {
                "searchString": t.string().optional(),
                "sortField": t.string().optional(),
                "advertiserGroupIds": t.string().optional(),
                "archived": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "subaccountId": t.string().optional(),
                "atLeastOneOptimizationActivity": t.boolean().optional(),
                "advertiserIds": t.string().optional(),
                "excludedIds": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "maxResults": t.integer().optional(),
                "overriddenEventTagId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesGet"] = dfareporting.post(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "profileId": t.string().optional(),
                "url": t.string().optional(),
                "advertiserId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "deepLinks": t.array(t.proxy(renames["DeepLinkIn"])).optional(),
                "archived": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LandingPageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesPatch"] = dfareporting.post(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "profileId": t.string().optional(),
                "url": t.string().optional(),
                "advertiserId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "deepLinks": t.array(t.proxy(renames["DeepLinkIn"])).optional(),
                "archived": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LandingPageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "profileId": t.string().optional(),
                "url": t.string().optional(),
                "advertiserId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "deepLinks": t.array(t.proxy(renames["DeepLinkIn"])).optional(),
                "archived": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LandingPageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesList"] = dfareporting.post(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "profileId": t.string().optional(),
                "url": t.string().optional(),
                "advertiserId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "deepLinks": t.array(t.proxy(renames["DeepLinkIn"])).optional(),
                "archived": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LandingPageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserLandingPagesInsert"] = dfareporting.post(
        "userprofiles/{profileId}/advertiserLandingPages",
        t.struct(
            {
                "profileId": t.string().optional(),
                "url": t.string().optional(),
                "advertiserId": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "deepLinks": t.array(t.proxy(renames["DeepLinkIn"])).optional(),
                "archived": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LandingPageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/accounts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/accounts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = dfareporting.get(
        "userprofiles/{profileId}/accounts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = dfareporting.get(
        "userprofiles/{profileId}/accounts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignCreativeAssociationsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/campaigns/{campaignId}/campaignCreativeAssociations",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "sortOrder": t.string().optional(),
                "pageToken": t.string().optional(),
                "campaignId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignCreativeAssociationsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["campaignCreativeAssociationsList"] = dfareporting.get(
        "userprofiles/{profileId}/campaigns/{campaignId}/campaignCreativeAssociations",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "sortOrder": t.string().optional(),
                "pageToken": t.string().optional(),
                "campaignId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignCreativeAssociationsListResponseOut"]),
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
    functions["dynamicTargetingKeysList"] = dfareporting.post(
        "userprofiles/{profileId}/dynamicTargetingKeys",
        t.struct(
            {
                "profileId": t.string().optional(),
                "objectId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "objectType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicTargetingKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dynamicTargetingKeysDelete"] = dfareporting.post(
        "userprofiles/{profileId}/dynamicTargetingKeys",
        t.struct(
            {
                "profileId": t.string().optional(),
                "objectId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "objectType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicTargetingKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dynamicTargetingKeysInsert"] = dfareporting.post(
        "userprofiles/{profileId}/dynamicTargetingKeys",
        t.struct(
            {
                "profileId": t.string().optional(),
                "objectId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "objectType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicTargetingKeyOut"]),
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
    functions["filesGet"] = dfareporting.get(
        "userprofiles/{profileId}/files",
        t.struct(
            {
                "profileId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "sortField": t.string().optional(),
                "pageToken": t.string().optional(),
                "sortOrder": t.string().optional(),
                "scope": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FileListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesList"] = dfareporting.get(
        "userprofiles/{profileId}/files",
        t.struct(
            {
                "profileId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "sortField": t.string().optional(),
                "pageToken": t.string().optional(),
                "sortOrder": t.string().optional(),
                "scope": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FileListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeAssetsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/creativeAssets/{advertiserId}/creativeAssets",
        t.struct(
            {
                "profileId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "counterCustomEvents": t.array(
                    t.proxy(renames["CreativeCustomEventIn"])
                ).optional(),
                "kind": t.string().optional(),
                "timerCustomEvents": t.array(
                    t.proxy(renames["CreativeCustomEventIn"])
                ).optional(),
                "detectedFeatures": t.array(t.string()).optional(),
                "exitCustomEvents": t.array(
                    t.proxy(renames["CreativeCustomEventIn"])
                ).optional(),
                "id": t.string().optional(),
                "richMedia": t.boolean().optional(),
                "warnedValidationRules": t.array(t.string()).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "assetIdentifier": t.proxy(renames["CreativeAssetIdIn"]).optional(),
                "clickTags": t.array(t.proxy(renames["ClickTagIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeAssetMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolePermissionGroupsList"] = dfareporting.get(
        "userprofiles/{profileId}/userRolePermissionGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserRolePermissionGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolePermissionGroupsGet"] = dfareporting.get(
        "userprofiles/{profileId}/userRolePermissionGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserRolePermissionGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dimensionValuesQuery"] = dfareporting.post(
        "userprofiles/{profileId}/dimensionvalues/query",
        t.struct(
            {
                "profileId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "kind": t.string().optional(),
                "dimensionName": t.string().optional(),
                "endDate": t.string(),
                "filters": t.array(t.proxy(renames["DimensionFilterIn"])).optional(),
                "startDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DimensionValueListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsBatchinsert"] = dfareporting.post(
        "userprofiles/{profileId}/conversions/batchupdate",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "encryptionInfo": t.proxy(renames["EncryptionInfoIn"]).optional(),
                "conversions": t.array(t.proxy(renames["ConversionIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionsBatchUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsBatchupdate"] = dfareporting.post(
        "userprofiles/{profileId}/conversions/batchupdate",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "encryptionInfo": t.proxy(renames["EncryptionInfoIn"]).optional(),
                "conversions": t.array(t.proxy(renames["ConversionIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionsBatchUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingProfilesGet"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles",
        t.struct(
            {
                "ids": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "profileId": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "currency_code": t.string().optional(),
                "sortOrder": t.string().optional(),
                "subaccountIds": t.string().optional(),
                "onlySuggestion": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingProfilesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingProfilesUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles",
        t.struct(
            {
                "ids": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "profileId": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "currency_code": t.string().optional(),
                "sortOrder": t.string().optional(),
                "subaccountIds": t.string().optional(),
                "onlySuggestion": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingProfilesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingProfilesList"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles",
        t.struct(
            {
                "ids": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "profileId": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "currency_code": t.string().optional(),
                "sortOrder": t.string().optional(),
                "subaccountIds": t.string().optional(),
                "onlySuggestion": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingProfilesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = dfareporting.get(
        "userprofiles/{profileId}/projects",
        t.struct(
            {
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "pageToken": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "ids": t.string().optional(),
                "profileId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "searchString": t.string().optional(),
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
                "sortField": t.string().optional(),
                "sortOrder": t.string().optional(),
                "pageToken": t.string().optional(),
                "advertiserIds": t.string().optional(),
                "ids": t.string().optional(),
                "profileId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "searchString": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectsListResponseOut"]),
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
    functions["creativeFieldsDelete"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsInsert"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsGet"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsList"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldsPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/creativeFields",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/ads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/ads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsList"] = dfareporting.get(
        "userprofiles/{profileId}/ads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/ads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adsGet"] = dfareporting.get(
        "userprofiles/{profileId}/ads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["citiesList"] = dfareporting.get(
        "userprofiles/{profileId}/cities",
        t.struct(
            {
                "dartIds": t.string().optional(),
                "countryDartIds": t.string().optional(),
                "namePrefix": t.string().optional(),
                "regionDartIds": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CitiesListResponseOut"]),
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
    functions["changeLogsList"] = dfareporting.get(
        "userprofiles/{profileId}/changeLogs/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangeLogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changeLogsGet"] = dfareporting.get(
        "userprofiles/{profileId}/changeLogs/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangeLogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersList"] = dfareporting.post(
        "userprofiles/{profileId}/advertisers",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "defaultEmail": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "subaccountId": t.string().optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "status": t.string().optional(),
                "advertiserGroupId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "suspended": t.boolean().optional(),
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
                "kind": t.string().optional(),
                "defaultEmail": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "subaccountId": t.string().optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "status": t.string().optional(),
                "advertiserGroupId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "suspended": t.boolean().optional(),
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
                "kind": t.string().optional(),
                "defaultEmail": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "subaccountId": t.string().optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "status": t.string().optional(),
                "advertiserGroupId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "suspended": t.boolean().optional(),
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
                "kind": t.string().optional(),
                "defaultEmail": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "subaccountId": t.string().optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "status": t.string().optional(),
                "advertiserGroupId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "suspended": t.boolean().optional(),
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
                "kind": t.string().optional(),
                "defaultEmail": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "clickThroughUrlSuffix": t.string().optional(),
                "subaccountId": t.string().optional(),
                "measurementPartnerLink": t.proxy(
                    renames["MeasurementPartnerAdvertiserLinkIn"]
                ).optional(),
                "originalFloodlightConfigurationId": t.string().optional(),
                "defaultClickThroughEventTagId": t.string().optional(),
                "status": t.string().optional(),
                "advertiserGroupId": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "suspended": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightConfigurationsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightConfigurations/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightConfigurationsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightConfigurations/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightConfigurationsList"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightConfigurations/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightConfigurationsGet"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightConfigurations/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contentCategoriesList"] = dfareporting.put(
        "userprofiles/{profileId}/contentCategories",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contentCategoriesDelete"] = dfareporting.put(
        "userprofiles/{profileId}/contentCategories",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
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
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
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
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
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
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
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
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentCategoryOut"]),
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
    functions["browsersList"] = dfareporting.get(
        "userprofiles/{profileId}/browsers",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["BrowsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sizesList"] = dfareporting.get(
        "userprofiles/{profileId}/sizes/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SizeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sizesInsert"] = dfareporting.get(
        "userprofiles/{profileId}/sizes/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SizeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sizesGet"] = dfareporting.get(
        "userprofiles/{profileId}/sizes/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SizeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingRatesList"] = dfareporting.get(
        "userprofiles/{profileId}/billingProfiles/{billingProfileId}/billingRates",
        t.struct(
            {
                "billingProfileId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingRatesListResponseOut"]),
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
    functions["remarketingListSharesUpdate"] = dfareporting.patch(
        "userprofiles/{profileId}/remarketingListShares",
        t.struct(
            {
                "id": t.string(),
                "profileId": t.string().optional(),
                "sharedAccountIds": t.array(t.string()).optional(),
                "remarketingListId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListShareOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListSharesGet"] = dfareporting.patch(
        "userprofiles/{profileId}/remarketingListShares",
        t.struct(
            {
                "id": t.string(),
                "profileId": t.string().optional(),
                "sharedAccountIds": t.array(t.string()).optional(),
                "remarketingListId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListShareOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListSharesPatch"] = dfareporting.patch(
        "userprofiles/{profileId}/remarketingListShares",
        t.struct(
            {
                "id": t.string(),
                "profileId": t.string().optional(),
                "sharedAccountIds": t.array(t.string()).optional(),
                "remarketingListId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListShareOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subaccountsPatch"] = dfareporting.put(
        "userprofiles/{profileId}/subaccounts",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
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
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubaccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subaccountsGet"] = dfareporting.put(
        "userprofiles/{profileId}/subaccounts",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
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
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
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
                "accountId": t.string().optional(),
                "availablePermissionIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubaccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userRolePermissionsGet"] = dfareporting.get(
        "userprofiles/{profileId}/userRolePermissions",
        t.struct(
            {
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
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
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserRolePermissionsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesGet"] = dfareporting.post(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "id": t.string().optional(),
                "value": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesPatch"] = dfareporting.post(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "id": t.string().optional(),
                "value": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesList"] = dfareporting.post(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "id": t.string().optional(),
                "value": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesDelete"] = dfareporting.post(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "id": t.string().optional(),
                "value": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "id": t.string().optional(),
                "value": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeFieldValuesInsert"] = dfareporting.post(
        "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
        t.struct(
            {
                "profileId": t.string().optional(),
                "creativeFieldId": t.string().optional(),
                "id": t.string().optional(),
                "value": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeFieldValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGet"] = dfareporting.get(
        "userprofiles",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["UserProfileListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesList"] = dfareporting.get(
        "userprofiles",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["UserProfileListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsPatch"] = dfareporting.post(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "placementGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "comment": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "siteId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsGet"] = dfareporting.post(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "placementGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "comment": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "siteId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "placementGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "comment": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "siteId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsList"] = dfareporting.post(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "placementGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "comment": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "siteId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementGroupsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/placementGroups",
        t.struct(
            {
                "profileId": t.string().optional(),
                "primaryPlacementId": t.string().optional(),
                "id": t.string().optional(),
                "accountId": t.string().optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "placementGroupType": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "externalId": t.string().optional(),
                "name": t.string().optional(),
                "activeStatus": t.string().optional(),
                "childPlacementIds": t.array(t.string()).optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "comment": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "primaryPlacementIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "contentCategoryId": t.string().optional(),
                "siteId": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightActivityGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsList"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightActivityGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightActivityGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightActivityGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivityGroupsGet"] = dfareporting.get(
        "userprofiles/{profileId}/floodlightActivityGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsList"] = dfareporting.post(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "externalId": t.string().optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "primary": t.boolean().optional(),
                "advertiserId": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "name": t.string().optional(),
                "subaccountId": t.string().optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "placementGroupId": t.string().optional(),
                "paymentSource": t.string().optional(),
                "keyName": t.string().optional(),
                "compatibility": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "status": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "contentCategoryId": t.string().optional(),
                "comment": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "kind": t.string().optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "activeStatus": t.string().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "siteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsGeneratetags"] = dfareporting.post(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "externalId": t.string().optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "primary": t.boolean().optional(),
                "advertiserId": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "name": t.string().optional(),
                "subaccountId": t.string().optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "placementGroupId": t.string().optional(),
                "paymentSource": t.string().optional(),
                "keyName": t.string().optional(),
                "compatibility": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "status": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "contentCategoryId": t.string().optional(),
                "comment": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "kind": t.string().optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "activeStatus": t.string().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "siteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsPatch"] = dfareporting.post(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "externalId": t.string().optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "primary": t.boolean().optional(),
                "advertiserId": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "name": t.string().optional(),
                "subaccountId": t.string().optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "placementGroupId": t.string().optional(),
                "paymentSource": t.string().optional(),
                "keyName": t.string().optional(),
                "compatibility": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "status": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "contentCategoryId": t.string().optional(),
                "comment": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "kind": t.string().optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "activeStatus": t.string().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "siteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsGet"] = dfareporting.post(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "externalId": t.string().optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "primary": t.boolean().optional(),
                "advertiserId": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "name": t.string().optional(),
                "subaccountId": t.string().optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "placementGroupId": t.string().optional(),
                "paymentSource": t.string().optional(),
                "keyName": t.string().optional(),
                "compatibility": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "status": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "contentCategoryId": t.string().optional(),
                "comment": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "kind": t.string().optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "activeStatus": t.string().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "siteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "externalId": t.string().optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "primary": t.boolean().optional(),
                "advertiserId": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "name": t.string().optional(),
                "subaccountId": t.string().optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "placementGroupId": t.string().optional(),
                "paymentSource": t.string().optional(),
                "keyName": t.string().optional(),
                "compatibility": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "status": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "contentCategoryId": t.string().optional(),
                "comment": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "kind": t.string().optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "activeStatus": t.string().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "siteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/placements",
        t.struct(
            {
                "profileId": t.string().optional(),
                "placementGroupIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "campaignId": t.string().optional(),
                "lastModifiedInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "externalId": t.string().optional(),
                "lookbackConfiguration": t.proxy(
                    renames["LookbackConfigurationIn"]
                ).optional(),
                "campaignIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "primary": t.boolean().optional(),
                "advertiserId": t.string().optional(),
                "placementStrategyId": t.string().optional(),
                "vpaidAdapterChoice": t.string().optional(),
                "name": t.string().optional(),
                "subaccountId": t.string().optional(),
                "tagSetting": t.proxy(renames["TagSettingIn"]).optional(),
                "placementGroupId": t.string().optional(),
                "paymentSource": t.string().optional(),
                "keyName": t.string().optional(),
                "compatibility": t.string().optional(),
                "directorySiteId": t.string().optional(),
                "pricingSchedule": t.proxy(renames["PricingScheduleIn"]).optional(),
                "status": t.string().optional(),
                "createInfo": t.proxy(renames["LastModifiedInfoIn"]).optional(),
                "contentCategoryId": t.string().optional(),
                "comment": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "partnerWrappingData": t.proxy(
                    renames["MeasurementPartnerWrappingDataIn"]
                ).optional(),
                "wrappingOptOut": t.boolean().optional(),
                "kind": t.string().optional(),
                "videoSettings": t.proxy(renames["VideoSettingsIn"]).optional(),
                "size": t.proxy(renames["SizeIn"]).optional(),
                "tagFormats": t.array(t.string()).optional(),
                "activeStatus": t.string().optional(),
                "additionalSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
                "sslRequired": t.boolean().optional(),
                "accountId": t.string().optional(),
                "paymentApproved": t.boolean().optional(),
                "adBlockingOptOut": t.boolean().optional(),
                "siteIdDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "publisherUpdateInfo": t.proxy(
                    renames["LastModifiedInfoIn"]
                ).optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "videoActiveViewOptOut": t.boolean().optional(),
                "siteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "campaignId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "definitionsOnly": t.boolean().optional(),
                "searchString": t.string().optional(),
                "eventTagTypes": t.string().optional(),
                "sortField": t.string().optional(),
                "enabled": t.boolean().optional(),
                "adId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "campaignId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "definitionsOnly": t.boolean().optional(),
                "searchString": t.string().optional(),
                "eventTagTypes": t.string().optional(),
                "sortField": t.string().optional(),
                "enabled": t.boolean().optional(),
                "adId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsGet"] = dfareporting.get(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "campaignId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "definitionsOnly": t.boolean().optional(),
                "searchString": t.string().optional(),
                "eventTagTypes": t.string().optional(),
                "sortField": t.string().optional(),
                "enabled": t.boolean().optional(),
                "adId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsDelete"] = dfareporting.get(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "campaignId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "definitionsOnly": t.boolean().optional(),
                "searchString": t.string().optional(),
                "eventTagTypes": t.string().optional(),
                "sortField": t.string().optional(),
                "enabled": t.boolean().optional(),
                "adId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "campaignId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "definitionsOnly": t.boolean().optional(),
                "searchString": t.string().optional(),
                "eventTagTypes": t.string().optional(),
                "sortField": t.string().optional(),
                "enabled": t.boolean().optional(),
                "adId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventTagsList"] = dfareporting.get(
        "userprofiles/{profileId}/eventTags",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "profileId": t.string().optional(),
                "ids": t.string().optional(),
                "campaignId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "definitionsOnly": t.boolean().optional(),
                "searchString": t.string().optional(),
                "eventTagTypes": t.string().optional(),
                "sortField": t.string().optional(),
                "enabled": t.boolean().optional(),
                "adId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventTagsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsList"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsDelete"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertiserGroupsGet"] = dfareporting.get(
        "userprofiles/{profileId}/advertiserGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesUpdate"] = dfareporting.post(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "keyName": t.string().optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "approved": t.boolean().optional(),
                "id": t.string().optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "name": t.string().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "directorySiteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesGet"] = dfareporting.post(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "keyName": t.string().optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "approved": t.boolean().optional(),
                "id": t.string().optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "name": t.string().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "directorySiteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesList"] = dfareporting.post(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "keyName": t.string().optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "approved": t.boolean().optional(),
                "id": t.string().optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "name": t.string().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "directorySiteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesPatch"] = dfareporting.post(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "keyName": t.string().optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "approved": t.boolean().optional(),
                "id": t.string().optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "name": t.string().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "directorySiteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesInsert"] = dfareporting.post(
        "userprofiles/{profileId}/sites",
        t.struct(
            {
                "profileId": t.string().optional(),
                "kind": t.string().optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "accountId": t.string().optional(),
                "directorySiteIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "keyName": t.string().optional(),
                "siteContacts": t.array(t.proxy(renames["SiteContactIn"])).optional(),
                "approved": t.boolean().optional(),
                "id": t.string().optional(),
                "videoSettings": t.proxy(renames["SiteVideoSettingsIn"]).optional(),
                "name": t.string().optional(),
                "siteSettings": t.proxy(renames["SiteSettingsIn"]).optional(),
                "directorySiteId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersList"] = dfareporting.get(
        "userprofiles/{profileId}/projects/{projectId}/orders/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "projectId": t.string().optional(),
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
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesPatch"] = dfareporting.get(
        "userprofiles/{profileId}/placementStrategies/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesList"] = dfareporting.get(
        "userprofiles/{profileId}/placementStrategies/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesDelete"] = dfareporting.get(
        "userprofiles/{profileId}/placementStrategies/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesInsert"] = dfareporting.get(
        "userprofiles/{profileId}/placementStrategies/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/placementStrategies/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placementStrategiesGet"] = dfareporting.get(
        "userprofiles/{profileId}/placementStrategies/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlacementStrategyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mobileAppsGet"] = dfareporting.get(
        "userprofiles/{profileId}/mobileApps",
        t.struct(
            {
                "ids": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "directories": t.string().optional(),
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
                "ids": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "searchString": t.string().optional(),
                "profileId": t.string().optional(),
                "directories": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MobileAppsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountPermissionGroupsList"] = dfareporting.get(
        "userprofiles/{profileId}/accountPermissionGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountPermissionGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountPermissionGroupsGet"] = dfareporting.get(
        "userprofiles/{profileId}/accountPermissionGroups/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountPermissionGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTemplatesPatch"] = dfareporting.get(
        "userprofiles/{profileId}/targetingTemplates/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
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
                "id": t.string().optional(),
                "profileId": t.string().optional(),
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
                "id": t.string().optional(),
                "profileId": t.string().optional(),
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
                "id": t.string().optional(),
                "profileId": t.string().optional(),
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
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetingTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videoFormatsList"] = dfareporting.get(
        "userprofiles/{profileId}/videoFormats/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.integer().optional(),
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
                "profileId": t.string().optional(),
                "id": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoFormatOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsInsert"] = dfareporting.put(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "profileId": t.string().optional(),
                "listSource": t.string().optional(),
                "active": t.boolean().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "listPopulationRule": t.proxy(
                    renames["ListPopulationRuleIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "lifeSpan": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "description": t.string().optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "listSize": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsGet"] = dfareporting.put(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "profileId": t.string().optional(),
                "listSource": t.string().optional(),
                "active": t.boolean().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "listPopulationRule": t.proxy(
                    renames["ListPopulationRuleIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "lifeSpan": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "description": t.string().optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "listSize": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsPatch"] = dfareporting.put(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "profileId": t.string().optional(),
                "listSource": t.string().optional(),
                "active": t.boolean().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "listPopulationRule": t.proxy(
                    renames["ListPopulationRuleIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "lifeSpan": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "description": t.string().optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "listSize": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsList"] = dfareporting.put(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "profileId": t.string().optional(),
                "listSource": t.string().optional(),
                "active": t.boolean().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "listPopulationRule": t.proxy(
                    renames["ListPopulationRuleIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "lifeSpan": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "description": t.string().optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "listSize": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["remarketingListsUpdate"] = dfareporting.put(
        "userprofiles/{profileId}/remarketingLists",
        t.struct(
            {
                "profileId": t.string().optional(),
                "listSource": t.string().optional(),
                "active": t.boolean().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "listPopulationRule": t.proxy(
                    renames["ListPopulationRuleIn"]
                ).optional(),
                "subaccountId": t.string().optional(),
                "lifeSpan": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "description": t.string().optional(),
                "advertiserId": t.string().optional(),
                "accountId": t.string().optional(),
                "listSize": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingListOut"]),
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
    functions["countriesGet"] = dfareporting.get(
        "userprofiles/{profileId}/countries",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CountriesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["countriesList"] = dfareporting.get(
        "userprofiles/{profileId}/countries",
        t.struct({"profileId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CountriesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/creativeGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsList"] = dfareporting.get(
        "userprofiles/{profileId}/creativeGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/creativeGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/creativeGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["creativeGroupsGet"] = dfareporting.get(
        "userprofiles/{profileId}/creativeGroups/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeGroupOut"]),
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
    functions["reportsRun"] = dfareporting.get(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "scope": t.string().optional(),
                "profileId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsPatch"] = dfareporting.get(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "scope": t.string().optional(),
                "profileId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "scope": t.string().optional(),
                "profileId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsInsert"] = dfareporting.get(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "scope": t.string().optional(),
                "profileId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGet"] = dfareporting.get(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "scope": t.string().optional(),
                "profileId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsDelete"] = dfareporting.get(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "scope": t.string().optional(),
                "profileId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsList"] = dfareporting.get(
        "userprofiles/{profileId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "scope": t.string().optional(),
                "profileId": t.string().optional(),
                "sortOrder": t.string().optional(),
                "sortField": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportListOut"]),
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
                "accountId": t.string().optional(),
                "schedule": t.struct(
                    {
                        "repeatsOnWeekDays": t.array(t.string()).optional(),
                        "every": t.integer().optional(),
                        "active": t.boolean().optional(),
                        "repeats": t.string().optional(),
                        "startDate": t.string(),
                        "timezone": t.string().optional(),
                        "runsOnDayOfMonth": t.string().optional(),
                        "expirationDate": t.string(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "format": t.string().optional(),
                "name": t.string().optional(),
                "criteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "pathCriteria": t.struct(
                    {
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "fileName": t.string().optional(),
                "ownerProfileId": t.string().optional(),
                "subAccountId": t.string().optional(),
                "floodlightCriteria": t.struct(
                    {
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                            }
                        ).optional(),
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    }
                ).optional(),
                "delivery": t.struct(
                    {
                        "emailOwner": t.boolean().optional(),
                        "recipients": t.array(
                            t.proxy(renames["RecipientIn"])
                        ).optional(),
                        "message": t.string().optional(),
                        "emailOwnerDeliveryType": t.string().optional(),
                    }
                ).optional(),
                "type": t.string().optional(),
                "pathAttributionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "customChannelGrouping": t.proxy(
                            renames["ChannelGroupingIn"]
                        ).optional(),
                        "pathFilters": t.array(
                            t.proxy(renames["PathFilterIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                    }
                ).optional(),
                "crossDimensionReachCriteria": t.struct(
                    {
                        "breakdown": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "pivoted": t.boolean().optional(),
                        "overlapMetricNames": t.array(t.string()).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "dimension": t.string().optional(),
                    }
                ).optional(),
                "reachCriteria": t.struct(
                    {
                        "customRichMediaEvents": t.proxy(
                            renames["CustomRichMediaEventsIn"]
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                        "reachByFrequencyMetricNames": t.array(t.string()).optional(),
                        "dimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                        "dimensionFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "enableAllDimensionCombinations": t.boolean().optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "pathToConversionCriteria": t.struct(
                    {
                        "floodlightConfigId": t.proxy(
                            renames["DimensionValueIn"]
                        ).optional(),
                        "customRichMediaEvents": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                        "perInteractionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "customFloodlightVariables": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "reportProperties": t.struct(
                            {
                                "maximumInteractionGap": t.integer().optional(),
                                "includeUnattributedCookieConversions": t.boolean().optional(),
                                "maximumImpressionInteractions": t.integer().optional(),
                                "includeAttributedIPConversions": t.boolean().optional(),
                                "clicksLookbackWindow": t.integer().optional(),
                                "impressionsLookbackWindow": t.integer().optional(),
                                "includeUnattributedIPConversions": t.boolean().optional(),
                                "maximumClickInteractions": t.integer().optional(),
                                "pivotOnInteractionPath": t.boolean().optional(),
                            }
                        ).optional(),
                        "activityFilters": t.array(
                            t.proxy(renames["DimensionValueIn"])
                        ).optional(),
                        "conversionDimensions": t.array(
                            t.proxy(renames["SortedDimensionIn"])
                        ).optional(),
                        "metricNames": t.array(t.string()).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CompatibleFieldsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAssignmentsList"] = dfareporting.post(
        "userprofiles/{profileId}/billingProfiles/{billingProfileId}/billingAssignments",
        t.struct(
            {
                "billingProfileId": t.string().optional(),
                "profileId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "accountId": t.string().optional(),
                "campaignId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAssignmentsInsert"] = dfareporting.post(
        "userprofiles/{profileId}/billingProfiles/{billingProfileId}/billingAssignments",
        t.struct(
            {
                "billingProfileId": t.string().optional(),
                "profileId": t.string().optional(),
                "subaccountId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "kind": t.string().optional(),
                "accountId": t.string().optional(),
                "campaignId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesUpdate"] = dfareporting.get(
        "userprofiles/{profileId}/accountUserProfiles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesList"] = dfareporting.get(
        "userprofiles/{profileId}/accountUserProfiles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesPatch"] = dfareporting.get(
        "userprofiles/{profileId}/accountUserProfiles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesInsert"] = dfareporting.get(
        "userprofiles/{profileId}/accountUserProfiles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountUserProfilesGet"] = dfareporting.get(
        "userprofiles/{profileId}/accountUserProfiles/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountUserProfileOut"]),
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
    functions["floodlightActivitiesDelete"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "expectedUrl": t.string().optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "accountId": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "secure": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "cacheBustingType": t.string().optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "countingMethod": t.string().optional(),
                "subaccountId": t.string().optional(),
                "status": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "tagString": t.string().optional(),
                "tagFormat": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "advertiserId": t.string().optional(),
                "sslRequired": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightActivitiesGet"] = dfareporting.patch(
        "userprofiles/{profileId}/floodlightActivities",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "expectedUrl": t.string().optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "accountId": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "secure": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "cacheBustingType": t.string().optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "countingMethod": t.string().optional(),
                "subaccountId": t.string().optional(),
                "status": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "tagString": t.string().optional(),
                "tagFormat": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "advertiserId": t.string().optional(),
                "sslRequired": t.boolean().optional(),
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
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "expectedUrl": t.string().optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "accountId": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "secure": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "cacheBustingType": t.string().optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "countingMethod": t.string().optional(),
                "subaccountId": t.string().optional(),
                "status": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "tagString": t.string().optional(),
                "tagFormat": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "advertiserId": t.string().optional(),
                "sslRequired": t.boolean().optional(),
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
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "expectedUrl": t.string().optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "accountId": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "secure": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "cacheBustingType": t.string().optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "countingMethod": t.string().optional(),
                "subaccountId": t.string().optional(),
                "status": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "tagString": t.string().optional(),
                "tagFormat": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "advertiserId": t.string().optional(),
                "sslRequired": t.boolean().optional(),
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
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "expectedUrl": t.string().optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "accountId": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "secure": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "cacheBustingType": t.string().optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "countingMethod": t.string().optional(),
                "subaccountId": t.string().optional(),
                "status": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "tagString": t.string().optional(),
                "tagFormat": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "advertiserId": t.string().optional(),
                "sslRequired": t.boolean().optional(),
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
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "expectedUrl": t.string().optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "accountId": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "secure": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "cacheBustingType": t.string().optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "countingMethod": t.string().optional(),
                "subaccountId": t.string().optional(),
                "status": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "tagString": t.string().optional(),
                "tagFormat": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "advertiserId": t.string().optional(),
                "sslRequired": t.boolean().optional(),
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
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "advertiserIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "expectedUrl": t.string().optional(),
                "floodlightActivityGroupName": t.string().optional(),
                "publisherTags": t.array(
                    t.proxy(renames["FloodlightActivityPublisherDynamicTagIn"])
                ).optional(),
                "accountId": t.string().optional(),
                "floodlightTagType": t.string().optional(),
                "notes": t.string().optional(),
                "floodlightConfigurationId": t.string().optional(),
                "secure": t.boolean().optional(),
                "sslCompliant": t.boolean().optional(),
                "floodlightActivityGroupType": t.string().optional(),
                "floodlightConfigurationIdDimensionValue": t.proxy(
                    renames["DimensionValueIn"]
                ).optional(),
                "idDimensionValue": t.proxy(renames["DimensionValueIn"]).optional(),
                "cacheBustingType": t.string().optional(),
                "userDefinedVariableTypes": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "countingMethod": t.string().optional(),
                "subaccountId": t.string().optional(),
                "status": t.string().optional(),
                "floodlightActivityGroupTagString": t.string().optional(),
                "tagString": t.string().optional(),
                "tagFormat": t.string().optional(),
                "attributionEnabled": t.boolean().optional(),
                "name": t.string().optional(),
                "floodlightActivityGroupId": t.string().optional(),
                "defaultTags": t.array(
                    t.proxy(renames["FloodlightActivityDynamicTagIn"])
                ).optional(),
                "advertiserId": t.string().optional(),
                "sslRequired": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightActivityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetableRemarketingListsList"] = dfareporting.get(
        "userprofiles/{profileId}/targetableRemarketingLists/{id}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "id": t.string().optional(),
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
                "profileId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TargetableRemarketingListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dfareporting",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
