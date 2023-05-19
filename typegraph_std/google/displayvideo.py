from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_displayvideo() -> Import:
    displayvideo = HTTPRuntime("https://displayvideo.googleapis.com/")

    renames = {
        "ErrorResponse": "_displayvideo_1_ErrorResponse",
        "ListInvoicesResponseIn": "_displayvideo_2_ListInvoicesResponseIn",
        "ListInvoicesResponseOut": "_displayvideo_3_ListInvoicesResponseOut",
        "ListCreativesResponseIn": "_displayvideo_4_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_displayvideo_5_ListCreativesResponseOut",
        "PartnerCostIn": "_displayvideo_6_PartnerCostIn",
        "PartnerCostOut": "_displayvideo_7_PartnerCostOut",
        "ExchangeAssignedTargetingOptionDetailsIn": "_displayvideo_8_ExchangeAssignedTargetingOptionDetailsIn",
        "ExchangeAssignedTargetingOptionDetailsOut": "_displayvideo_9_ExchangeAssignedTargetingOptionDetailsOut",
        "AgeRangeTargetingOptionDetailsIn": "_displayvideo_10_AgeRangeTargetingOptionDetailsIn",
        "AgeRangeTargetingOptionDetailsOut": "_displayvideo_11_AgeRangeTargetingOptionDetailsOut",
        "InventorySourceFilterIn": "_displayvideo_12_InventorySourceFilterIn",
        "InventorySourceFilterOut": "_displayvideo_13_InventorySourceFilterOut",
        "SdfConfigIn": "_displayvideo_14_SdfConfigIn",
        "SdfConfigOut": "_displayvideo_15_SdfConfigOut",
        "LineItemAssignedTargetingOptionIn": "_displayvideo_16_LineItemAssignedTargetingOptionIn",
        "LineItemAssignedTargetingOptionOut": "_displayvideo_17_LineItemAssignedTargetingOptionOut",
        "ContentInstreamPositionAssignedTargetingOptionDetailsIn": "_displayvideo_18_ContentInstreamPositionAssignedTargetingOptionDetailsIn",
        "ContentInstreamPositionAssignedTargetingOptionDetailsOut": "_displayvideo_19_ContentInstreamPositionAssignedTargetingOptionDetailsOut",
        "GoogleAudienceGroupIn": "_displayvideo_20_GoogleAudienceGroupIn",
        "GoogleAudienceGroupOut": "_displayvideo_21_GoogleAudienceGroupOut",
        "DoubleVerifyBrandSafetyCategoriesIn": "_displayvideo_22_DoubleVerifyBrandSafetyCategoriesIn",
        "DoubleVerifyBrandSafetyCategoriesOut": "_displayvideo_23_DoubleVerifyBrandSafetyCategoriesOut",
        "UserRewardedContentTargetingOptionDetailsIn": "_displayvideo_24_UserRewardedContentTargetingOptionDetailsIn",
        "UserRewardedContentTargetingOptionDetailsOut": "_displayvideo_25_UserRewardedContentTargetingOptionDetailsOut",
        "InventorySourceAccessorsPartnerAccessorIn": "_displayvideo_26_InventorySourceAccessorsPartnerAccessorIn",
        "InventorySourceAccessorsPartnerAccessorOut": "_displayvideo_27_InventorySourceAccessorsPartnerAccessorOut",
        "ListCustomBiddingScriptsResponseIn": "_displayvideo_28_ListCustomBiddingScriptsResponseIn",
        "ListCustomBiddingScriptsResponseOut": "_displayvideo_29_ListCustomBiddingScriptsResponseOut",
        "EnvironmentAssignedTargetingOptionDetailsIn": "_displayvideo_30_EnvironmentAssignedTargetingOptionDetailsIn",
        "EnvironmentAssignedTargetingOptionDetailsOut": "_displayvideo_31_EnvironmentAssignedTargetingOptionDetailsOut",
        "LanguageTargetingOptionDetailsIn": "_displayvideo_32_LanguageTargetingOptionDetailsIn",
        "LanguageTargetingOptionDetailsOut": "_displayvideo_33_LanguageTargetingOptionDetailsOut",
        "OperatingSystemAssignedTargetingOptionDetailsIn": "_displayvideo_34_OperatingSystemAssignedTargetingOptionDetailsIn",
        "OperatingSystemAssignedTargetingOptionDetailsOut": "_displayvideo_35_OperatingSystemAssignedTargetingOptionDetailsOut",
        "FirstAndThirdPartyAudienceIn": "_displayvideo_36_FirstAndThirdPartyAudienceIn",
        "FirstAndThirdPartyAudienceOut": "_displayvideo_37_FirstAndThirdPartyAudienceOut",
        "ListTargetingOptionsResponseIn": "_displayvideo_38_ListTargetingOptionsResponseIn",
        "ListTargetingOptionsResponseOut": "_displayvideo_39_ListTargetingOptionsResponseOut",
        "ProductMatchDimensionIn": "_displayvideo_40_ProductMatchDimensionIn",
        "ProductMatchDimensionOut": "_displayvideo_41_ProductMatchDimensionOut",
        "FloodlightGroupIn": "_displayvideo_42_FloodlightGroupIn",
        "FloodlightGroupOut": "_displayvideo_43_FloodlightGroupOut",
        "PoiSearchTermsIn": "_displayvideo_44_PoiSearchTermsIn",
        "PoiSearchTermsOut": "_displayvideo_45_PoiSearchTermsOut",
        "AdvertiserAdServerConfigIn": "_displayvideo_46_AdvertiserAdServerConfigIn",
        "AdvertiserAdServerConfigOut": "_displayvideo_47_AdvertiserAdServerConfigOut",
        "PrismaCpeCodeIn": "_displayvideo_48_PrismaCpeCodeIn",
        "PrismaCpeCodeOut": "_displayvideo_49_PrismaCpeCodeOut",
        "BulkListAssignedTargetingOptionsResponseIn": "_displayvideo_50_BulkListAssignedTargetingOptionsResponseIn",
        "BulkListAssignedTargetingOptionsResponseOut": "_displayvideo_51_BulkListAssignedTargetingOptionsResponseOut",
        "LookupInvoiceCurrencyResponseIn": "_displayvideo_52_LookupInvoiceCurrencyResponseIn",
        "LookupInvoiceCurrencyResponseOut": "_displayvideo_53_LookupInvoiceCurrencyResponseOut",
        "ListManualTriggersResponseIn": "_displayvideo_54_ListManualTriggersResponseIn",
        "ListManualTriggersResponseOut": "_displayvideo_55_ListManualTriggersResponseOut",
        "PerformanceGoalIn": "_displayvideo_56_PerformanceGoalIn",
        "PerformanceGoalOut": "_displayvideo_57_PerformanceGoalOut",
        "ListLineItemAssignedTargetingOptionsResponseIn": "_displayvideo_58_ListLineItemAssignedTargetingOptionsResponseIn",
        "ListLineItemAssignedTargetingOptionsResponseOut": "_displayvideo_59_ListLineItemAssignedTargetingOptionsResponseOut",
        "ReplaceSitesRequestIn": "_displayvideo_60_ReplaceSitesRequestIn",
        "ReplaceSitesRequestOut": "_displayvideo_61_ReplaceSitesRequestOut",
        "ListYoutubeAdGroupAdsResponseIn": "_displayvideo_62_ListYoutubeAdGroupAdsResponseIn",
        "ListYoutubeAdGroupAdsResponseOut": "_displayvideo_63_ListYoutubeAdGroupAdsResponseOut",
        "ExchangeConfigIn": "_displayvideo_64_ExchangeConfigIn",
        "ExchangeConfigOut": "_displayvideo_65_ExchangeConfigOut",
        "AdUrlIn": "_displayvideo_66_AdUrlIn",
        "AdUrlOut": "_displayvideo_67_AdUrlOut",
        "TargetingExpansionConfigIn": "_displayvideo_68_TargetingExpansionConfigIn",
        "TargetingExpansionConfigOut": "_displayvideo_69_TargetingExpansionConfigOut",
        "PrismaConfigIn": "_displayvideo_70_PrismaConfigIn",
        "PrismaConfigOut": "_displayvideo_71_PrismaConfigOut",
        "AssignedInventorySourceIn": "_displayvideo_72_AssignedInventorySourceIn",
        "AssignedInventorySourceOut": "_displayvideo_73_AssignedInventorySourceOut",
        "YoutubeVideoDetailsIn": "_displayvideo_74_YoutubeVideoDetailsIn",
        "YoutubeVideoDetailsOut": "_displayvideo_75_YoutubeVideoDetailsOut",
        "ParentalStatusAssignedTargetingOptionDetailsIn": "_displayvideo_76_ParentalStatusAssignedTargetingOptionDetailsIn",
        "ParentalStatusAssignedTargetingOptionDetailsOut": "_displayvideo_77_ParentalStatusAssignedTargetingOptionDetailsOut",
        "ChannelAssignedTargetingOptionDetailsIn": "_displayvideo_78_ChannelAssignedTargetingOptionDetailsIn",
        "ChannelAssignedTargetingOptionDetailsOut": "_displayvideo_79_ChannelAssignedTargetingOptionDetailsOut",
        "BulkEditAssignedUserRolesRequestIn": "_displayvideo_80_BulkEditAssignedUserRolesRequestIn",
        "BulkEditAssignedUserRolesRequestOut": "_displayvideo_81_BulkEditAssignedUserRolesRequestOut",
        "BulkUpdateLineItemsResponseIn": "_displayvideo_82_BulkUpdateLineItemsResponseIn",
        "BulkUpdateLineItemsResponseOut": "_displayvideo_83_BulkUpdateLineItemsResponseOut",
        "BulkEditNegativeKeywordsResponseIn": "_displayvideo_84_BulkEditNegativeKeywordsResponseIn",
        "BulkEditNegativeKeywordsResponseOut": "_displayvideo_85_BulkEditNegativeKeywordsResponseOut",
        "EditInventorySourceReadWriteAccessorsRequestIn": "_displayvideo_86_EditInventorySourceReadWriteAccessorsRequestIn",
        "EditInventorySourceReadWriteAccessorsRequestOut": "_displayvideo_87_EditInventorySourceReadWriteAccessorsRequestOut",
        "DigitalContentLabelTargetingOptionDetailsIn": "_displayvideo_88_DigitalContentLabelTargetingOptionDetailsIn",
        "DigitalContentLabelTargetingOptionDetailsOut": "_displayvideo_89_DigitalContentLabelTargetingOptionDetailsOut",
        "HouseholdIncomeTargetingOptionDetailsIn": "_displayvideo_90_HouseholdIncomeTargetingOptionDetailsIn",
        "HouseholdIncomeTargetingOptionDetailsOut": "_displayvideo_91_HouseholdIncomeTargetingOptionDetailsOut",
        "CustomBiddingScriptRefIn": "_displayvideo_92_CustomBiddingScriptRefIn",
        "CustomBiddingScriptRefOut": "_displayvideo_93_CustomBiddingScriptRefOut",
        "ContentOutstreamPositionTargetingOptionDetailsIn": "_displayvideo_94_ContentOutstreamPositionTargetingOptionDetailsIn",
        "ContentOutstreamPositionTargetingOptionDetailsOut": "_displayvideo_95_ContentOutstreamPositionTargetingOptionDetailsOut",
        "OnScreenPositionAssignedTargetingOptionDetailsIn": "_displayvideo_96_OnScreenPositionAssignedTargetingOptionDetailsIn",
        "OnScreenPositionAssignedTargetingOptionDetailsOut": "_displayvideo_97_OnScreenPositionAssignedTargetingOptionDetailsOut",
        "ExchangeReviewStatusIn": "_displayvideo_98_ExchangeReviewStatusIn",
        "ExchangeReviewStatusOut": "_displayvideo_99_ExchangeReviewStatusOut",
        "GenderAssignedTargetingOptionDetailsIn": "_displayvideo_100_GenderAssignedTargetingOptionDetailsIn",
        "GenderAssignedTargetingOptionDetailsOut": "_displayvideo_101_GenderAssignedTargetingOptionDetailsOut",
        "ManualTriggerIn": "_displayvideo_102_ManualTriggerIn",
        "ManualTriggerOut": "_displayvideo_103_ManualTriggerOut",
        "MastheadAdIn": "_displayvideo_104_MastheadAdIn",
        "MastheadAdOut": "_displayvideo_105_MastheadAdOut",
        "ContentDurationAssignedTargetingOptionDetailsIn": "_displayvideo_106_ContentDurationAssignedTargetingOptionDetailsIn",
        "ContentDurationAssignedTargetingOptionDetailsOut": "_displayvideo_107_ContentDurationAssignedTargetingOptionDetailsOut",
        "ContentGenreTargetingOptionDetailsIn": "_displayvideo_108_ContentGenreTargetingOptionDetailsIn",
        "ContentGenreTargetingOptionDetailsOut": "_displayvideo_109_ContentGenreTargetingOptionDetailsOut",
        "UniversalAdIdIn": "_displayvideo_110_UniversalAdIdIn",
        "UniversalAdIdOut": "_displayvideo_111_UniversalAdIdOut",
        "ExchangeTargetingOptionDetailsIn": "_displayvideo_112_ExchangeTargetingOptionDetailsIn",
        "ExchangeTargetingOptionDetailsOut": "_displayvideo_113_ExchangeTargetingOptionDetailsOut",
        "ExchangeConfigEnabledExchangeIn": "_displayvideo_114_ExchangeConfigEnabledExchangeIn",
        "ExchangeConfigEnabledExchangeOut": "_displayvideo_115_ExchangeConfigEnabledExchangeOut",
        "InventorySourceAccessorsIn": "_displayvideo_116_InventorySourceAccessorsIn",
        "InventorySourceAccessorsOut": "_displayvideo_117_InventorySourceAccessorsOut",
        "NegativeKeywordIn": "_displayvideo_118_NegativeKeywordIn",
        "NegativeKeywordOut": "_displayvideo_119_NegativeKeywordOut",
        "ExitEventIn": "_displayvideo_120_ExitEventIn",
        "ExitEventOut": "_displayvideo_121_ExitEventOut",
        "DoubleVerifyVideoViewabilityIn": "_displayvideo_122_DoubleVerifyVideoViewabilityIn",
        "DoubleVerifyVideoViewabilityOut": "_displayvideo_123_DoubleVerifyVideoViewabilityOut",
        "ListLocationListsResponseIn": "_displayvideo_124_ListLocationListsResponseIn",
        "ListLocationListsResponseOut": "_displayvideo_125_ListLocationListsResponseOut",
        "DeviceMakeModelAssignedTargetingOptionDetailsIn": "_displayvideo_126_DeviceMakeModelAssignedTargetingOptionDetailsIn",
        "DeviceMakeModelAssignedTargetingOptionDetailsOut": "_displayvideo_127_DeviceMakeModelAssignedTargetingOptionDetailsOut",
        "RateDetailsIn": "_displayvideo_128_RateDetailsIn",
        "RateDetailsOut": "_displayvideo_129_RateDetailsOut",
        "CmHybridConfigIn": "_displayvideo_130_CmHybridConfigIn",
        "CmHybridConfigOut": "_displayvideo_131_CmHybridConfigOut",
        "SdfDownloadTaskIn": "_displayvideo_132_SdfDownloadTaskIn",
        "SdfDownloadTaskOut": "_displayvideo_133_SdfDownloadTaskOut",
        "ListCampaignsResponseIn": "_displayvideo_134_ListCampaignsResponseIn",
        "ListCampaignsResponseOut": "_displayvideo_135_ListCampaignsResponseOut",
        "DeviceMakeModelTargetingOptionDetailsIn": "_displayvideo_136_DeviceMakeModelTargetingOptionDetailsIn",
        "DeviceMakeModelTargetingOptionDetailsOut": "_displayvideo_137_DeviceMakeModelTargetingOptionDetailsOut",
        "TargetFrequencyIn": "_displayvideo_138_TargetFrequencyIn",
        "TargetFrequencyOut": "_displayvideo_139_TargetFrequencyOut",
        "BulkEditAssignedLocationsRequestIn": "_displayvideo_140_BulkEditAssignedLocationsRequestIn",
        "BulkEditAssignedLocationsRequestOut": "_displayvideo_141_BulkEditAssignedLocationsRequestOut",
        "AuditAdvertiserResponseIn": "_displayvideo_142_AuditAdvertiserResponseIn",
        "AuditAdvertiserResponseOut": "_displayvideo_143_AuditAdvertiserResponseOut",
        "ContactInfoIn": "_displayvideo_144_ContactInfoIn",
        "ContactInfoOut": "_displayvideo_145_ContactInfoOut",
        "AdlooxIn": "_displayvideo_146_AdlooxIn",
        "AdlooxOut": "_displayvideo_147_AdlooxOut",
        "YoutubeAdGroupIn": "_displayvideo_148_YoutubeAdGroupIn",
        "YoutubeAdGroupOut": "_displayvideo_149_YoutubeAdGroupOut",
        "OmidTargetingOptionDetailsIn": "_displayvideo_150_OmidTargetingOptionDetailsIn",
        "OmidTargetingOptionDetailsOut": "_displayvideo_151_OmidTargetingOptionDetailsOut",
        "InStreamAdIn": "_displayvideo_152_InStreamAdIn",
        "InStreamAdOut": "_displayvideo_153_InStreamAdOut",
        "CreateAssetResponseIn": "_displayvideo_154_CreateAssetResponseIn",
        "CreateAssetResponseOut": "_displayvideo_155_CreateAssetResponseOut",
        "VideoAdSequenceStepIn": "_displayvideo_156_VideoAdSequenceStepIn",
        "VideoAdSequenceStepOut": "_displayvideo_157_VideoAdSequenceStepOut",
        "YoutubeAndPartnersThirdPartyMeasurementSettingsIn": "_displayvideo_158_YoutubeAndPartnersThirdPartyMeasurementSettingsIn",
        "YoutubeAndPartnersThirdPartyMeasurementSettingsOut": "_displayvideo_159_YoutubeAndPartnersThirdPartyMeasurementSettingsOut",
        "BusinessChainAssignedTargetingOptionDetailsIn": "_displayvideo_160_BusinessChainAssignedTargetingOptionDetailsIn",
        "BusinessChainAssignedTargetingOptionDetailsOut": "_displayvideo_161_BusinessChainAssignedTargetingOptionDetailsOut",
        "YoutubeVideoAssignedTargetingOptionDetailsIn": "_displayvideo_162_YoutubeVideoAssignedTargetingOptionDetailsIn",
        "YoutubeVideoAssignedTargetingOptionDetailsOut": "_displayvideo_163_YoutubeVideoAssignedTargetingOptionDetailsOut",
        "GoogleAudienceIn": "_displayvideo_164_GoogleAudienceIn",
        "GoogleAudienceOut": "_displayvideo_165_GoogleAudienceOut",
        "YoutubeAndPartnersInventorySourceConfigIn": "_displayvideo_166_YoutubeAndPartnersInventorySourceConfigIn",
        "YoutubeAndPartnersInventorySourceConfigOut": "_displayvideo_167_YoutubeAndPartnersInventorySourceConfigOut",
        "CreativeIn": "_displayvideo_168_CreativeIn",
        "CreativeOut": "_displayvideo_169_CreativeOut",
        "BulkEditAdvertiserAssignedTargetingOptionsRequestIn": "_displayvideo_170_BulkEditAdvertiserAssignedTargetingOptionsRequestIn",
        "BulkEditAdvertiserAssignedTargetingOptionsRequestOut": "_displayvideo_171_BulkEditAdvertiserAssignedTargetingOptionsRequestOut",
        "ParentEntityFilterIn": "_displayvideo_172_ParentEntityFilterIn",
        "ParentEntityFilterOut": "_displayvideo_173_ParentEntityFilterOut",
        "NonSkippableAdIn": "_displayvideo_174_NonSkippableAdIn",
        "NonSkippableAdOut": "_displayvideo_175_NonSkippableAdOut",
        "PerformanceGoalBidStrategyIn": "_displayvideo_176_PerformanceGoalBidStrategyIn",
        "PerformanceGoalBidStrategyOut": "_displayvideo_177_PerformanceGoalBidStrategyOut",
        "TimerEventIn": "_displayvideo_178_TimerEventIn",
        "TimerEventOut": "_displayvideo_179_TimerEventOut",
        "InventorySourceAccessorsAdvertiserAccessorsIn": "_displayvideo_180_InventorySourceAccessorsAdvertiserAccessorsIn",
        "InventorySourceAccessorsAdvertiserAccessorsOut": "_displayvideo_181_InventorySourceAccessorsAdvertiserAccessorsOut",
        "CombinedAudienceGroupIn": "_displayvideo_182_CombinedAudienceGroupIn",
        "CombinedAudienceGroupOut": "_displayvideo_183_CombinedAudienceGroupOut",
        "ListPartnerAssignedTargetingOptionsResponseIn": "_displayvideo_184_ListPartnerAssignedTargetingOptionsResponseIn",
        "ListPartnerAssignedTargetingOptionsResponseOut": "_displayvideo_185_ListPartnerAssignedTargetingOptionsResponseOut",
        "AdvertiserBillingConfigIn": "_displayvideo_186_AdvertiserBillingConfigIn",
        "AdvertiserBillingConfigOut": "_displayvideo_187_AdvertiserBillingConfigOut",
        "DuplicateLineItemRequestIn": "_displayvideo_188_DuplicateLineItemRequestIn",
        "DuplicateLineItemRequestOut": "_displayvideo_189_DuplicateLineItemRequestOut",
        "CarrierAndIspTargetingOptionDetailsIn": "_displayvideo_190_CarrierAndIspTargetingOptionDetailsIn",
        "CarrierAndIspTargetingOptionDetailsOut": "_displayvideo_191_CarrierAndIspTargetingOptionDetailsOut",
        "EnvironmentTargetingOptionDetailsIn": "_displayvideo_192_EnvironmentTargetingOptionDetailsIn",
        "EnvironmentTargetingOptionDetailsOut": "_displayvideo_193_EnvironmentTargetingOptionDetailsOut",
        "ParentalStatusTargetingOptionDetailsIn": "_displayvideo_194_ParentalStatusTargetingOptionDetailsIn",
        "ParentalStatusTargetingOptionDetailsOut": "_displayvideo_195_ParentalStatusTargetingOptionDetailsOut",
        "DeviceTypeTargetingOptionDetailsIn": "_displayvideo_196_DeviceTypeTargetingOptionDetailsIn",
        "DeviceTypeTargetingOptionDetailsOut": "_displayvideo_197_DeviceTypeTargetingOptionDetailsOut",
        "AssetIn": "_displayvideo_198_AssetIn",
        "AssetOut": "_displayvideo_199_AssetOut",
        "CombinedAudienceTargetingSettingIn": "_displayvideo_200_CombinedAudienceTargetingSettingIn",
        "CombinedAudienceTargetingSettingOut": "_displayvideo_201_CombinedAudienceTargetingSettingOut",
        "CmTrackingAdIn": "_displayvideo_202_CmTrackingAdIn",
        "CmTrackingAdOut": "_displayvideo_203_CmTrackingAdOut",
        "FirstAndThirdPartyAudienceGroupIn": "_displayvideo_204_FirstAndThirdPartyAudienceGroupIn",
        "FirstAndThirdPartyAudienceGroupOut": "_displayvideo_205_FirstAndThirdPartyAudienceGroupOut",
        "AudioAdIn": "_displayvideo_206_AudioAdIn",
        "AudioAdOut": "_displayvideo_207_AudioAdOut",
        "LineItemFlightIn": "_displayvideo_208_LineItemFlightIn",
        "LineItemFlightOut": "_displayvideo_209_LineItemFlightOut",
        "CreativeConfigIn": "_displayvideo_210_CreativeConfigIn",
        "CreativeConfigOut": "_displayvideo_211_CreativeConfigOut",
        "SensitiveCategoryTargetingOptionDetailsIn": "_displayvideo_212_SensitiveCategoryTargetingOptionDetailsIn",
        "SensitiveCategoryTargetingOptionDetailsOut": "_displayvideo_213_SensitiveCategoryTargetingOptionDetailsOut",
        "AuthorizedSellerStatusAssignedTargetingOptionDetailsIn": "_displayvideo_214_AuthorizedSellerStatusAssignedTargetingOptionDetailsIn",
        "AuthorizedSellerStatusAssignedTargetingOptionDetailsOut": "_displayvideo_215_AuthorizedSellerStatusAssignedTargetingOptionDetailsOut",
        "EditGuaranteedOrderReadAccessorsResponseIn": "_displayvideo_216_EditGuaranteedOrderReadAccessorsResponseIn",
        "EditGuaranteedOrderReadAccessorsResponseOut": "_displayvideo_217_EditGuaranteedOrderReadAccessorsResponseOut",
        "DoubleVerifyDisplayViewabilityIn": "_displayvideo_218_DoubleVerifyDisplayViewabilityIn",
        "DoubleVerifyDisplayViewabilityOut": "_displayvideo_219_DoubleVerifyDisplayViewabilityOut",
        "BulkListCampaignAssignedTargetingOptionsResponseIn": "_displayvideo_220_BulkListCampaignAssignedTargetingOptionsResponseIn",
        "BulkListCampaignAssignedTargetingOptionsResponseOut": "_displayvideo_221_BulkListCampaignAssignedTargetingOptionsResponseOut",
        "ScriptErrorIn": "_displayvideo_222_ScriptErrorIn",
        "ScriptErrorOut": "_displayvideo_223_ScriptErrorOut",
        "DoubleVerifyAppStarRatingIn": "_displayvideo_224_DoubleVerifyAppStarRatingIn",
        "DoubleVerifyAppStarRatingOut": "_displayvideo_225_DoubleVerifyAppStarRatingOut",
        "IdFilterIn": "_displayvideo_226_IdFilterIn",
        "IdFilterOut": "_displayvideo_227_IdFilterOut",
        "OmidAssignedTargetingOptionDetailsIn": "_displayvideo_228_OmidAssignedTargetingOptionDetailsIn",
        "OmidAssignedTargetingOptionDetailsOut": "_displayvideo_229_OmidAssignedTargetingOptionDetailsOut",
        "ThirdPartyVerifierAssignedTargetingOptionDetailsIn": "_displayvideo_230_ThirdPartyVerifierAssignedTargetingOptionDetailsIn",
        "ThirdPartyVerifierAssignedTargetingOptionDetailsOut": "_displayvideo_231_ThirdPartyVerifierAssignedTargetingOptionDetailsOut",
        "UserIn": "_displayvideo_232_UserIn",
        "UserOut": "_displayvideo_233_UserOut",
        "PartnerRevenueModelIn": "_displayvideo_234_PartnerRevenueModelIn",
        "PartnerRevenueModelOut": "_displayvideo_235_PartnerRevenueModelOut",
        "NegativeKeywordListIn": "_displayvideo_236_NegativeKeywordListIn",
        "NegativeKeywordListOut": "_displayvideo_237_NegativeKeywordListOut",
        "ListYoutubeAdGroupAssignedTargetingOptionsResponseIn": "_displayvideo_238_ListYoutubeAdGroupAssignedTargetingOptionsResponseIn",
        "ListYoutubeAdGroupAssignedTargetingOptionsResponseOut": "_displayvideo_239_ListYoutubeAdGroupAssignedTargetingOptionsResponseOut",
        "ListChannelsResponseIn": "_displayvideo_240_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_displayvideo_241_ListChannelsResponseOut",
        "ListAssignedLocationsResponseIn": "_displayvideo_242_ListAssignedLocationsResponseIn",
        "ListAssignedLocationsResponseOut": "_displayvideo_243_ListAssignedLocationsResponseOut",
        "BulkEditAssignedInventorySourcesResponseIn": "_displayvideo_244_BulkEditAssignedInventorySourcesResponseIn",
        "BulkEditAssignedInventorySourcesResponseOut": "_displayvideo_245_BulkEditAssignedInventorySourcesResponseOut",
        "AudienceGroupAssignedTargetingOptionDetailsIn": "_displayvideo_246_AudienceGroupAssignedTargetingOptionDetailsIn",
        "AudienceGroupAssignedTargetingOptionDetailsOut": "_displayvideo_247_AudienceGroupAssignedTargetingOptionDetailsOut",
        "ListFirstAndThirdPartyAudiencesResponseIn": "_displayvideo_248_ListFirstAndThirdPartyAudiencesResponseIn",
        "ListFirstAndThirdPartyAudiencesResponseOut": "_displayvideo_249_ListFirstAndThirdPartyAudiencesResponseOut",
        "AssignedLocationIn": "_displayvideo_250_AssignedLocationIn",
        "AssignedLocationOut": "_displayvideo_251_AssignedLocationOut",
        "CustomBiddingScriptIn": "_displayvideo_252_CustomBiddingScriptIn",
        "CustomBiddingScriptOut": "_displayvideo_253_CustomBiddingScriptOut",
        "BudgetSummaryIn": "_displayvideo_254_BudgetSummaryIn",
        "BudgetSummaryOut": "_displayvideo_255_BudgetSummaryOut",
        "InsertionOrderIn": "_displayvideo_256_InsertionOrderIn",
        "InsertionOrderOut": "_displayvideo_257_InsertionOrderOut",
        "PacingIn": "_displayvideo_258_PacingIn",
        "PacingOut": "_displayvideo_259_PacingOut",
        "RegionalLocationListAssignedTargetingOptionDetailsIn": "_displayvideo_260_RegionalLocationListAssignedTargetingOptionDetailsIn",
        "RegionalLocationListAssignedTargetingOptionDetailsOut": "_displayvideo_261_RegionalLocationListAssignedTargetingOptionDetailsOut",
        "CampaignGoalIn": "_displayvideo_262_CampaignGoalIn",
        "CampaignGoalOut": "_displayvideo_263_CampaignGoalOut",
        "GeoRegionAssignedTargetingOptionDetailsIn": "_displayvideo_264_GeoRegionAssignedTargetingOptionDetailsIn",
        "GeoRegionAssignedTargetingOptionDetailsOut": "_displayvideo_265_GeoRegionAssignedTargetingOptionDetailsOut",
        "VideoPlayerSizeAssignedTargetingOptionDetailsIn": "_displayvideo_266_VideoPlayerSizeAssignedTargetingOptionDetailsIn",
        "VideoPlayerSizeAssignedTargetingOptionDetailsOut": "_displayvideo_267_VideoPlayerSizeAssignedTargetingOptionDetailsOut",
        "ListPartnersResponseIn": "_displayvideo_268_ListPartnersResponseIn",
        "ListPartnersResponseOut": "_displayvideo_269_ListPartnersResponseOut",
        "PoiTargetingOptionDetailsIn": "_displayvideo_270_PoiTargetingOptionDetailsIn",
        "PoiTargetingOptionDetailsOut": "_displayvideo_271_PoiTargetingOptionDetailsOut",
        "TrackingFloodlightActivityConfigIn": "_displayvideo_272_TrackingFloodlightActivityConfigIn",
        "TrackingFloodlightActivityConfigOut": "_displayvideo_273_TrackingFloodlightActivityConfigOut",
        "ListAdvertisersResponseIn": "_displayvideo_274_ListAdvertisersResponseIn",
        "ListAdvertisersResponseOut": "_displayvideo_275_ListAdvertisersResponseOut",
        "ChannelIn": "_displayvideo_276_ChannelIn",
        "ChannelOut": "_displayvideo_277_ChannelOut",
        "DimensionsIn": "_displayvideo_278_DimensionsIn",
        "DimensionsOut": "_displayvideo_279_DimensionsOut",
        "ContactInfoListIn": "_displayvideo_280_ContactInfoListIn",
        "ContactInfoListOut": "_displayvideo_281_ContactInfoListOut",
        "UrlAssignedTargetingOptionDetailsIn": "_displayvideo_282_UrlAssignedTargetingOptionDetailsIn",
        "UrlAssignedTargetingOptionDetailsOut": "_displayvideo_283_UrlAssignedTargetingOptionDetailsOut",
        "GuaranteedOrderIn": "_displayvideo_284_GuaranteedOrderIn",
        "GuaranteedOrderOut": "_displayvideo_285_GuaranteedOrderOut",
        "AdvertiserCreativeConfigIn": "_displayvideo_286_AdvertiserCreativeConfigIn",
        "AdvertiserCreativeConfigOut": "_displayvideo_287_AdvertiserCreativeConfigOut",
        "VideoPerformanceAdIn": "_displayvideo_288_VideoPerformanceAdIn",
        "VideoPerformanceAdOut": "_displayvideo_289_VideoPerformanceAdOut",
        "ListNegativeKeywordListsResponseIn": "_displayvideo_290_ListNegativeKeywordListsResponseIn",
        "ListNegativeKeywordListsResponseOut": "_displayvideo_291_ListNegativeKeywordListsResponseOut",
        "GuaranteedOrderStatusIn": "_displayvideo_292_GuaranteedOrderStatusIn",
        "GuaranteedOrderStatusOut": "_displayvideo_293_GuaranteedOrderStatusOut",
        "BulkEditNegativeKeywordsRequestIn": "_displayvideo_294_BulkEditNegativeKeywordsRequestIn",
        "BulkEditNegativeKeywordsRequestOut": "_displayvideo_295_BulkEditNegativeKeywordsRequestOut",
        "ReplaceNegativeKeywordsRequestIn": "_displayvideo_296_ReplaceNegativeKeywordsRequestIn",
        "ReplaceNegativeKeywordsRequestOut": "_displayvideo_297_ReplaceNegativeKeywordsRequestOut",
        "BulkEditSitesResponseIn": "_displayvideo_298_BulkEditSitesResponseIn",
        "BulkEditSitesResponseOut": "_displayvideo_299_BulkEditSitesResponseOut",
        "AuthorizedSellerStatusTargetingOptionDetailsIn": "_displayvideo_300_AuthorizedSellerStatusTargetingOptionDetailsIn",
        "AuthorizedSellerStatusTargetingOptionDetailsOut": "_displayvideo_301_AuthorizedSellerStatusTargetingOptionDetailsOut",
        "ProductFeedDataIn": "_displayvideo_302_ProductFeedDataIn",
        "ProductFeedDataOut": "_displayvideo_303_ProductFeedDataOut",
        "GoogleAudienceTargetingSettingIn": "_displayvideo_304_GoogleAudienceTargetingSettingIn",
        "GoogleAudienceTargetingSettingOut": "_displayvideo_305_GoogleAudienceTargetingSettingOut",
        "FrequencyCapIn": "_displayvideo_306_FrequencyCapIn",
        "FrequencyCapOut": "_displayvideo_307_FrequencyCapOut",
        "CommonInStreamAttributeIn": "_displayvideo_308_CommonInStreamAttributeIn",
        "CommonInStreamAttributeOut": "_displayvideo_309_CommonInStreamAttributeOut",
        "PartnerAdServerConfigIn": "_displayvideo_310_PartnerAdServerConfigIn",
        "PartnerAdServerConfigOut": "_displayvideo_311_PartnerAdServerConfigOut",
        "CreateAssignedTargetingOptionsRequestIn": "_displayvideo_312_CreateAssignedTargetingOptionsRequestIn",
        "CreateAssignedTargetingOptionsRequestOut": "_displayvideo_313_CreateAssignedTargetingOptionsRequestOut",
        "ReplaceNegativeKeywordsResponseIn": "_displayvideo_314_ReplaceNegativeKeywordsResponseIn",
        "ReplaceNegativeKeywordsResponseOut": "_displayvideo_315_ReplaceNegativeKeywordsResponseOut",
        "PartnerIn": "_displayvideo_316_PartnerIn",
        "PartnerOut": "_displayvideo_317_PartnerOut",
        "EmptyIn": "_displayvideo_318_EmptyIn",
        "EmptyOut": "_displayvideo_319_EmptyOut",
        "ContentInstreamPositionTargetingOptionDetailsIn": "_displayvideo_320_ContentInstreamPositionTargetingOptionDetailsIn",
        "ContentInstreamPositionTargetingOptionDetailsOut": "_displayvideo_321_ContentInstreamPositionTargetingOptionDetailsOut",
        "ListCustomListsResponseIn": "_displayvideo_322_ListCustomListsResponseIn",
        "ListCustomListsResponseOut": "_displayvideo_323_ListCustomListsResponseOut",
        "TargetingOptionIn": "_displayvideo_324_TargetingOptionIn",
        "TargetingOptionOut": "_displayvideo_325_TargetingOptionOut",
        "CategoryTargetingOptionDetailsIn": "_displayvideo_326_CategoryTargetingOptionDetailsIn",
        "CategoryTargetingOptionDetailsOut": "_displayvideo_327_CategoryTargetingOptionDetailsOut",
        "InventorySourceStatusIn": "_displayvideo_328_InventorySourceStatusIn",
        "InventorySourceStatusOut": "_displayvideo_329_InventorySourceStatusOut",
        "ActiveViewVideoViewabilityMetricConfigIn": "_displayvideo_330_ActiveViewVideoViewabilityMetricConfigIn",
        "ActiveViewVideoViewabilityMetricConfigOut": "_displayvideo_331_ActiveViewVideoViewabilityMetricConfigOut",
        "BumperAdIn": "_displayvideo_332_BumperAdIn",
        "BumperAdOut": "_displayvideo_333_BumperAdOut",
        "EditCustomerMatchMembersResponseIn": "_displayvideo_334_EditCustomerMatchMembersResponseIn",
        "EditCustomerMatchMembersResponseOut": "_displayvideo_335_EditCustomerMatchMembersResponseOut",
        "VideoDiscoveryAdIn": "_displayvideo_336_VideoDiscoveryAdIn",
        "VideoDiscoveryAdOut": "_displayvideo_337_VideoDiscoveryAdOut",
        "BulkEditAssignedUserRolesResponseIn": "_displayvideo_338_BulkEditAssignedUserRolesResponseIn",
        "BulkEditAssignedUserRolesResponseOut": "_displayvideo_339_BulkEditAssignedUserRolesResponseOut",
        "GeoRegionSearchTermsIn": "_displayvideo_340_GeoRegionSearchTermsIn",
        "GeoRegionSearchTermsOut": "_displayvideo_341_GeoRegionSearchTermsOut",
        "BulkListAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_342_BulkListAdvertiserAssignedTargetingOptionsResponseIn",
        "BulkListAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_343_BulkListAdvertiserAssignedTargetingOptionsResponseOut",
        "AdvertiserGeneralConfigIn": "_displayvideo_344_AdvertiserGeneralConfigIn",
        "AdvertiserGeneralConfigOut": "_displayvideo_345_AdvertiserGeneralConfigOut",
        "BulkUpdateLineItemsRequestIn": "_displayvideo_346_BulkUpdateLineItemsRequestIn",
        "BulkUpdateLineItemsRequestOut": "_displayvideo_347_BulkUpdateLineItemsRequestOut",
        "KeywordAssignedTargetingOptionDetailsIn": "_displayvideo_348_KeywordAssignedTargetingOptionDetailsIn",
        "KeywordAssignedTargetingOptionDetailsOut": "_displayvideo_349_KeywordAssignedTargetingOptionDetailsOut",
        "ListCombinedAudiencesResponseIn": "_displayvideo_350_ListCombinedAudiencesResponseIn",
        "ListCombinedAudiencesResponseOut": "_displayvideo_351_ListCombinedAudiencesResponseOut",
        "CustomBiddingModelDetailsIn": "_displayvideo_352_CustomBiddingModelDetailsIn",
        "CustomBiddingModelDetailsOut": "_displayvideo_353_CustomBiddingModelDetailsOut",
        "ListSitesResponseIn": "_displayvideo_354_ListSitesResponseIn",
        "ListSitesResponseOut": "_displayvideo_355_ListSitesResponseOut",
        "InvoiceIn": "_displayvideo_356_InvoiceIn",
        "InvoiceOut": "_displayvideo_357_InvoiceOut",
        "LocationListIn": "_displayvideo_358_LocationListIn",
        "LocationListOut": "_displayvideo_359_LocationListOut",
        "ListInventorySourcesResponseIn": "_displayvideo_360_ListInventorySourcesResponseIn",
        "ListInventorySourcesResponseOut": "_displayvideo_361_ListInventorySourcesResponseOut",
        "DeviceTypeAssignedTargetingOptionDetailsIn": "_displayvideo_362_DeviceTypeAssignedTargetingOptionDetailsIn",
        "DeviceTypeAssignedTargetingOptionDetailsOut": "_displayvideo_363_DeviceTypeAssignedTargetingOptionDetailsOut",
        "BulkListInsertionOrderAssignedTargetingOptionsResponseIn": "_displayvideo_364_BulkListInsertionOrderAssignedTargetingOptionsResponseIn",
        "BulkListInsertionOrderAssignedTargetingOptionsResponseOut": "_displayvideo_365_BulkListInsertionOrderAssignedTargetingOptionsResponseOut",
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn": "_displayvideo_366_EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn",
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut": "_displayvideo_367_EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut",
        "ListCampaignAssignedTargetingOptionsResponseIn": "_displayvideo_368_ListCampaignAssignedTargetingOptionsResponseIn",
        "ListCampaignAssignedTargetingOptionsResponseOut": "_displayvideo_369_ListCampaignAssignedTargetingOptionsResponseOut",
        "ThirdPartyUrlIn": "_displayvideo_370_ThirdPartyUrlIn",
        "ThirdPartyUrlOut": "_displayvideo_371_ThirdPartyUrlOut",
        "ListAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_372_ListAdvertiserAssignedTargetingOptionsResponseIn",
        "ListAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_373_ListAdvertiserAssignedTargetingOptionsResponseOut",
        "InventorySourceGroupIn": "_displayvideo_374_InventorySourceGroupIn",
        "InventorySourceGroupOut": "_displayvideo_375_InventorySourceGroupOut",
        "BusinessChainSearchTermsIn": "_displayvideo_376_BusinessChainSearchTermsIn",
        "BusinessChainSearchTermsOut": "_displayvideo_377_BusinessChainSearchTermsOut",
        "ContentOutstreamPositionAssignedTargetingOptionDetailsIn": "_displayvideo_378_ContentOutstreamPositionAssignedTargetingOptionDetailsIn",
        "ContentOutstreamPositionAssignedTargetingOptionDetailsOut": "_displayvideo_379_ContentOutstreamPositionAssignedTargetingOptionDetailsOut",
        "SdfDownloadTaskMetadataIn": "_displayvideo_380_SdfDownloadTaskMetadataIn",
        "SdfDownloadTaskMetadataOut": "_displayvideo_381_SdfDownloadTaskMetadataOut",
        "SearchTargetingOptionsRequestIn": "_displayvideo_382_SearchTargetingOptionsRequestIn",
        "SearchTargetingOptionsRequestOut": "_displayvideo_383_SearchTargetingOptionsRequestOut",
        "InventorySourceVideoCreativeConfigIn": "_displayvideo_384_InventorySourceVideoCreativeConfigIn",
        "InventorySourceVideoCreativeConfigOut": "_displayvideo_385_InventorySourceVideoCreativeConfigOut",
        "BulkEditAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_386_BulkEditAdvertiserAssignedTargetingOptionsResponseIn",
        "BulkEditAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_387_BulkEditAdvertiserAssignedTargetingOptionsResponseOut",
        "IntegrationDetailsIn": "_displayvideo_388_IntegrationDetailsIn",
        "IntegrationDetailsOut": "_displayvideo_389_IntegrationDetailsOut",
        "InventorySourceGroupAssignedTargetingOptionDetailsIn": "_displayvideo_390_InventorySourceGroupAssignedTargetingOptionDetailsIn",
        "InventorySourceGroupAssignedTargetingOptionDetailsOut": "_displayvideo_391_InventorySourceGroupAssignedTargetingOptionDetailsOut",
        "MoneyIn": "_displayvideo_392_MoneyIn",
        "MoneyOut": "_displayvideo_393_MoneyOut",
        "ContentStreamTypeAssignedTargetingOptionDetailsIn": "_displayvideo_394_ContentStreamTypeAssignedTargetingOptionDetailsIn",
        "ContentStreamTypeAssignedTargetingOptionDetailsOut": "_displayvideo_395_ContentStreamTypeAssignedTargetingOptionDetailsOut",
        "BiddingStrategyIn": "_displayvideo_396_BiddingStrategyIn",
        "BiddingStrategyOut": "_displayvideo_397_BiddingStrategyOut",
        "ContentGenreAssignedTargetingOptionDetailsIn": "_displayvideo_398_ContentGenreAssignedTargetingOptionDetailsIn",
        "ContentGenreAssignedTargetingOptionDetailsOut": "_displayvideo_399_ContentGenreAssignedTargetingOptionDetailsOut",
        "CampaignIn": "_displayvideo_400_CampaignIn",
        "CampaignOut": "_displayvideo_401_CampaignOut",
        "InsertionOrderBudgetIn": "_displayvideo_402_InsertionOrderBudgetIn",
        "InsertionOrderBudgetOut": "_displayvideo_403_InsertionOrderBudgetOut",
        "StatusIn": "_displayvideo_404_StatusIn",
        "StatusOut": "_displayvideo_405_StatusOut",
        "HouseholdIncomeAssignedTargetingOptionDetailsIn": "_displayvideo_406_HouseholdIncomeAssignedTargetingOptionDetailsIn",
        "HouseholdIncomeAssignedTargetingOptionDetailsOut": "_displayvideo_407_HouseholdIncomeAssignedTargetingOptionDetailsOut",
        "AudioVideoOffsetIn": "_displayvideo_408_AudioVideoOffsetIn",
        "AudioVideoOffsetOut": "_displayvideo_409_AudioVideoOffsetOut",
        "VideoAdSequenceSettingsIn": "_displayvideo_410_VideoAdSequenceSettingsIn",
        "VideoAdSequenceSettingsOut": "_displayvideo_411_VideoAdSequenceSettingsOut",
        "DateRangeIn": "_displayvideo_412_DateRangeIn",
        "DateRangeOut": "_displayvideo_413_DateRangeOut",
        "SubExchangeTargetingOptionDetailsIn": "_displayvideo_414_SubExchangeTargetingOptionDetailsIn",
        "SubExchangeTargetingOptionDetailsOut": "_displayvideo_415_SubExchangeTargetingOptionDetailsOut",
        "AdvertiserIn": "_displayvideo_416_AdvertiserIn",
        "AdvertiserOut": "_displayvideo_417_AdvertiserOut",
        "AssignedTargetingOptionIn": "_displayvideo_418_AssignedTargetingOptionIn",
        "AssignedTargetingOptionOut": "_displayvideo_419_AssignedTargetingOptionOut",
        "CreateAssetRequestIn": "_displayvideo_420_CreateAssetRequestIn",
        "CreateAssetRequestOut": "_displayvideo_421_CreateAssetRequestOut",
        "CarrierAndIspAssignedTargetingOptionDetailsIn": "_displayvideo_422_CarrierAndIspAssignedTargetingOptionDetailsIn",
        "CarrierAndIspAssignedTargetingOptionDetailsOut": "_displayvideo_423_CarrierAndIspAssignedTargetingOptionDetailsOut",
        "ViewabilityAssignedTargetingOptionDetailsIn": "_displayvideo_424_ViewabilityAssignedTargetingOptionDetailsIn",
        "ViewabilityAssignedTargetingOptionDetailsOut": "_displayvideo_425_ViewabilityAssignedTargetingOptionDetailsOut",
        "FixedBidStrategyIn": "_displayvideo_426_FixedBidStrategyIn",
        "FixedBidStrategyOut": "_displayvideo_427_FixedBidStrategyOut",
        "IntegralAdScienceIn": "_displayvideo_428_IntegralAdScienceIn",
        "IntegralAdScienceOut": "_displayvideo_429_IntegralAdScienceOut",
        "LineItemIn": "_displayvideo_430_LineItemIn",
        "LineItemOut": "_displayvideo_431_LineItemOut",
        "ListAssignedInventorySourcesResponseIn": "_displayvideo_432_ListAssignedInventorySourcesResponseIn",
        "ListAssignedInventorySourcesResponseOut": "_displayvideo_433_ListAssignedInventorySourcesResponseOut",
        "DoubleVerifyIn": "_displayvideo_434_DoubleVerifyIn",
        "DoubleVerifyOut": "_displayvideo_435_DoubleVerifyOut",
        "ThirdPartyOnlyConfigIn": "_displayvideo_436_ThirdPartyOnlyConfigIn",
        "ThirdPartyOnlyConfigOut": "_displayvideo_437_ThirdPartyOnlyConfigOut",
        "SiteIn": "_displayvideo_438_SiteIn",
        "SiteOut": "_displayvideo_439_SiteOut",
        "ConversionCountingConfigIn": "_displayvideo_440_ConversionCountingConfigIn",
        "ConversionCountingConfigOut": "_displayvideo_441_ConversionCountingConfigOut",
        "CombinedAudienceIn": "_displayvideo_442_CombinedAudienceIn",
        "CombinedAudienceOut": "_displayvideo_443_CombinedAudienceOut",
        "ReviewStatusInfoIn": "_displayvideo_444_ReviewStatusInfoIn",
        "ReviewStatusInfoOut": "_displayvideo_445_ReviewStatusInfoOut",
        "AppCategoryAssignedTargetingOptionDetailsIn": "_displayvideo_446_AppCategoryAssignedTargetingOptionDetailsIn",
        "AppCategoryAssignedTargetingOptionDetailsOut": "_displayvideo_447_AppCategoryAssignedTargetingOptionDetailsOut",
        "OperationIn": "_displayvideo_448_OperationIn",
        "OperationOut": "_displayvideo_449_OperationOut",
        "TimeRangeIn": "_displayvideo_450_TimeRangeIn",
        "TimeRangeOut": "_displayvideo_451_TimeRangeOut",
        "ListInsertionOrderAssignedTargetingOptionsResponseIn": "_displayvideo_452_ListInsertionOrderAssignedTargetingOptionsResponseIn",
        "ListInsertionOrderAssignedTargetingOptionsResponseOut": "_displayvideo_453_ListInsertionOrderAssignedTargetingOptionsResponseOut",
        "ThirdPartyVendorConfigIn": "_displayvideo_454_ThirdPartyVendorConfigIn",
        "ThirdPartyVendorConfigOut": "_displayvideo_455_ThirdPartyVendorConfigOut",
        "AppCategoryTargetingOptionDetailsIn": "_displayvideo_456_AppCategoryTargetingOptionDetailsIn",
        "AppCategoryTargetingOptionDetailsOut": "_displayvideo_457_AppCategoryTargetingOptionDetailsOut",
        "ListNegativeKeywordsResponseIn": "_displayvideo_458_ListNegativeKeywordsResponseIn",
        "ListNegativeKeywordsResponseOut": "_displayvideo_459_ListNegativeKeywordsResponseOut",
        "BulkEditSitesRequestIn": "_displayvideo_460_BulkEditSitesRequestIn",
        "BulkEditSitesRequestOut": "_displayvideo_461_BulkEditSitesRequestOut",
        "SubExchangeAssignedTargetingOptionDetailsIn": "_displayvideo_462_SubExchangeAssignedTargetingOptionDetailsIn",
        "SubExchangeAssignedTargetingOptionDetailsOut": "_displayvideo_463_SubExchangeAssignedTargetingOptionDetailsOut",
        "FirstAndThirdPartyAudienceTargetingSettingIn": "_displayvideo_464_FirstAndThirdPartyAudienceTargetingSettingIn",
        "FirstAndThirdPartyAudienceTargetingSettingOut": "_displayvideo_465_FirstAndThirdPartyAudienceTargetingSettingOut",
        "CustomBiddingAlgorithmIn": "_displayvideo_466_CustomBiddingAlgorithmIn",
        "CustomBiddingAlgorithmOut": "_displayvideo_467_CustomBiddingAlgorithmOut",
        "DuplicateLineItemResponseIn": "_displayvideo_468_DuplicateLineItemResponseIn",
        "DuplicateLineItemResponseOut": "_displayvideo_469_DuplicateLineItemResponseOut",
        "ActivateManualTriggerRequestIn": "_displayvideo_470_ActivateManualTriggerRequestIn",
        "ActivateManualTriggerRequestOut": "_displayvideo_471_ActivateManualTriggerRequestOut",
        "AgeRangeAssignedTargetingOptionDetailsIn": "_displayvideo_472_AgeRangeAssignedTargetingOptionDetailsIn",
        "AgeRangeAssignedTargetingOptionDetailsOut": "_displayvideo_473_AgeRangeAssignedTargetingOptionDetailsOut",
        "ListGuaranteedOrdersResponseIn": "_displayvideo_474_ListGuaranteedOrdersResponseIn",
        "ListGuaranteedOrdersResponseOut": "_displayvideo_475_ListGuaranteedOrdersResponseOut",
        "OnScreenPositionTargetingOptionDetailsIn": "_displayvideo_476_OnScreenPositionTargetingOptionDetailsIn",
        "OnScreenPositionTargetingOptionDetailsOut": "_displayvideo_477_OnScreenPositionTargetingOptionDetailsOut",
        "DateIn": "_displayvideo_478_DateIn",
        "DateOut": "_displayvideo_479_DateOut",
        "ListInsertionOrdersResponseIn": "_displayvideo_480_ListInsertionOrdersResponseIn",
        "ListInsertionOrdersResponseOut": "_displayvideo_481_ListInsertionOrdersResponseOut",
        "BulkListAdGroupAssignedTargetingOptionsResponseIn": "_displayvideo_482_BulkListAdGroupAssignedTargetingOptionsResponseIn",
        "BulkListAdGroupAssignedTargetingOptionsResponseOut": "_displayvideo_483_BulkListAdGroupAssignedTargetingOptionsResponseOut",
        "SensitiveCategoryAssignedTargetingOptionDetailsIn": "_displayvideo_484_SensitiveCategoryAssignedTargetingOptionDetailsIn",
        "SensitiveCategoryAssignedTargetingOptionDetailsOut": "_displayvideo_485_SensitiveCategoryAssignedTargetingOptionDetailsOut",
        "BulkEditAssignedTargetingOptionsRequestIn": "_displayvideo_486_BulkEditAssignedTargetingOptionsRequestIn",
        "BulkEditAssignedTargetingOptionsRequestOut": "_displayvideo_487_BulkEditAssignedTargetingOptionsRequestOut",
        "MobileAppIn": "_displayvideo_488_MobileAppIn",
        "MobileAppOut": "_displayvideo_489_MobileAppOut",
        "GenderTargetingOptionDetailsIn": "_displayvideo_490_GenderTargetingOptionDetailsIn",
        "GenderTargetingOptionDetailsOut": "_displayvideo_491_GenderTargetingOptionDetailsOut",
        "ObaIconIn": "_displayvideo_492_ObaIconIn",
        "ObaIconOut": "_displayvideo_493_ObaIconOut",
        "ContentStreamTypeTargetingOptionDetailsIn": "_displayvideo_494_ContentStreamTypeTargetingOptionDetailsIn",
        "ContentStreamTypeTargetingOptionDetailsOut": "_displayvideo_495_ContentStreamTypeTargetingOptionDetailsOut",
        "DigitalContentLabelAssignedTargetingOptionDetailsIn": "_displayvideo_496_DigitalContentLabelAssignedTargetingOptionDetailsIn",
        "DigitalContentLabelAssignedTargetingOptionDetailsOut": "_displayvideo_497_DigitalContentLabelAssignedTargetingOptionDetailsOut",
        "DeleteAssignedTargetingOptionsRequestIn": "_displayvideo_498_DeleteAssignedTargetingOptionsRequestIn",
        "DeleteAssignedTargetingOptionsRequestOut": "_displayvideo_499_DeleteAssignedTargetingOptionsRequestOut",
        "SearchTargetingOptionsResponseIn": "_displayvideo_500_SearchTargetingOptionsResponseIn",
        "SearchTargetingOptionsResponseOut": "_displayvideo_501_SearchTargetingOptionsResponseOut",
        "AdvertiserTargetingConfigIn": "_displayvideo_502_AdvertiserTargetingConfigIn",
        "AdvertiserTargetingConfigOut": "_displayvideo_503_AdvertiserTargetingConfigOut",
        "CustomLabelIn": "_displayvideo_504_CustomLabelIn",
        "CustomLabelOut": "_displayvideo_505_CustomLabelOut",
        "AudioContentTypeAssignedTargetingOptionDetailsIn": "_displayvideo_506_AudioContentTypeAssignedTargetingOptionDetailsIn",
        "AudioContentTypeAssignedTargetingOptionDetailsOut": "_displayvideo_507_AudioContentTypeAssignedTargetingOptionDetailsOut",
        "PartnerDataAccessConfigIn": "_displayvideo_508_PartnerDataAccessConfigIn",
        "PartnerDataAccessConfigOut": "_displayvideo_509_PartnerDataAccessConfigOut",
        "ContentDurationTargetingOptionDetailsIn": "_displayvideo_510_ContentDurationTargetingOptionDetailsIn",
        "ContentDurationTargetingOptionDetailsOut": "_displayvideo_511_ContentDurationTargetingOptionDetailsOut",
        "InventorySourceDisplayCreativeConfigIn": "_displayvideo_512_InventorySourceDisplayCreativeConfigIn",
        "InventorySourceDisplayCreativeConfigOut": "_displayvideo_513_InventorySourceDisplayCreativeConfigOut",
        "AdvertiserDataAccessConfigIn": "_displayvideo_514_AdvertiserDataAccessConfigIn",
        "AdvertiserDataAccessConfigOut": "_displayvideo_515_AdvertiserDataAccessConfigOut",
        "SessionPositionAssignedTargetingOptionDetailsIn": "_displayvideo_516_SessionPositionAssignedTargetingOptionDetailsIn",
        "SessionPositionAssignedTargetingOptionDetailsOut": "_displayvideo_517_SessionPositionAssignedTargetingOptionDetailsOut",
        "ListInventorySourceGroupsResponseIn": "_displayvideo_518_ListInventorySourceGroupsResponseIn",
        "ListInventorySourceGroupsResponseOut": "_displayvideo_519_ListInventorySourceGroupsResponseOut",
        "MobileDeviceIdListIn": "_displayvideo_520_MobileDeviceIdListIn",
        "MobileDeviceIdListOut": "_displayvideo_521_MobileDeviceIdListOut",
        "CategoryAssignedTargetingOptionDetailsIn": "_displayvideo_522_CategoryAssignedTargetingOptionDetailsIn",
        "CategoryAssignedTargetingOptionDetailsOut": "_displayvideo_523_CategoryAssignedTargetingOptionDetailsOut",
        "MeasurementConfigIn": "_displayvideo_524_MeasurementConfigIn",
        "MeasurementConfigOut": "_displayvideo_525_MeasurementConfigOut",
        "AssignedUserRoleIn": "_displayvideo_526_AssignedUserRoleIn",
        "AssignedUserRoleOut": "_displayvideo_527_AssignedUserRoleOut",
        "BrowserTargetingOptionDetailsIn": "_displayvideo_528_BrowserTargetingOptionDetailsIn",
        "BrowserTargetingOptionDetailsOut": "_displayvideo_529_BrowserTargetingOptionDetailsOut",
        "ListGoogleAudiencesResponseIn": "_displayvideo_530_ListGoogleAudiencesResponseIn",
        "ListGoogleAudiencesResponseOut": "_displayvideo_531_ListGoogleAudiencesResponseOut",
        "GeoRegionTargetingOptionDetailsIn": "_displayvideo_532_GeoRegionTargetingOptionDetailsIn",
        "GeoRegionTargetingOptionDetailsOut": "_displayvideo_533_GeoRegionTargetingOptionDetailsOut",
        "InventorySourceAssignedTargetingOptionDetailsIn": "_displayvideo_534_InventorySourceAssignedTargetingOptionDetailsIn",
        "InventorySourceAssignedTargetingOptionDetailsOut": "_displayvideo_535_InventorySourceAssignedTargetingOptionDetailsOut",
        "ListCustomBiddingAlgorithmsResponseIn": "_displayvideo_536_ListCustomBiddingAlgorithmsResponseIn",
        "ListCustomBiddingAlgorithmsResponseOut": "_displayvideo_537_ListCustomBiddingAlgorithmsResponseOut",
        "VideoPlayerSizeTargetingOptionDetailsIn": "_displayvideo_538_VideoPlayerSizeTargetingOptionDetailsIn",
        "VideoPlayerSizeTargetingOptionDetailsOut": "_displayvideo_539_VideoPlayerSizeTargetingOptionDetailsOut",
        "EditCustomerMatchMembersRequestIn": "_displayvideo_540_EditCustomerMatchMembersRequestIn",
        "EditCustomerMatchMembersRequestOut": "_displayvideo_541_EditCustomerMatchMembersRequestOut",
        "LanguageAssignedTargetingOptionDetailsIn": "_displayvideo_542_LanguageAssignedTargetingOptionDetailsIn",
        "LanguageAssignedTargetingOptionDetailsOut": "_displayvideo_543_LanguageAssignedTargetingOptionDetailsOut",
        "ImageAssetIn": "_displayvideo_544_ImageAssetIn",
        "ImageAssetOut": "_displayvideo_545_ImageAssetOut",
        "DisplayVideoSourceAdIn": "_displayvideo_546_DisplayVideoSourceAdIn",
        "DisplayVideoSourceAdOut": "_displayvideo_547_DisplayVideoSourceAdOut",
        "LookbackWindowIn": "_displayvideo_548_LookbackWindowIn",
        "LookbackWindowOut": "_displayvideo_549_LookbackWindowOut",
        "PoiAssignedTargetingOptionDetailsIn": "_displayvideo_550_PoiAssignedTargetingOptionDetailsIn",
        "PoiAssignedTargetingOptionDetailsOut": "_displayvideo_551_PoiAssignedTargetingOptionDetailsOut",
        "YoutubeAdGroupAssignedTargetingOptionIn": "_displayvideo_552_YoutubeAdGroupAssignedTargetingOptionIn",
        "YoutubeAdGroupAssignedTargetingOptionOut": "_displayvideo_553_YoutubeAdGroupAssignedTargetingOptionOut",
        "OperatingSystemTargetingOptionDetailsIn": "_displayvideo_554_OperatingSystemTargetingOptionDetailsIn",
        "OperatingSystemTargetingOptionDetailsOut": "_displayvideo_555_OperatingSystemTargetingOptionDetailsOut",
        "AssetAssociationIn": "_displayvideo_556_AssetAssociationIn",
        "AssetAssociationOut": "_displayvideo_557_AssetAssociationOut",
        "GenerateDefaultLineItemRequestIn": "_displayvideo_558_GenerateDefaultLineItemRequestIn",
        "GenerateDefaultLineItemRequestOut": "_displayvideo_559_GenerateDefaultLineItemRequestOut",
        "GoogleBytestreamMediaIn": "_displayvideo_560_GoogleBytestreamMediaIn",
        "GoogleBytestreamMediaOut": "_displayvideo_561_GoogleBytestreamMediaOut",
        "BulkEditAssignedLocationsResponseIn": "_displayvideo_562_BulkEditAssignedLocationsResponseIn",
        "BulkEditAssignedLocationsResponseOut": "_displayvideo_563_BulkEditAssignedLocationsResponseOut",
        "ListLineItemsResponseIn": "_displayvideo_564_ListLineItemsResponseIn",
        "ListLineItemsResponseOut": "_displayvideo_565_ListLineItemsResponseOut",
        "ListUsersResponseIn": "_displayvideo_566_ListUsersResponseIn",
        "ListUsersResponseOut": "_displayvideo_567_ListUsersResponseOut",
        "CampaignFlightIn": "_displayvideo_568_CampaignFlightIn",
        "CampaignFlightOut": "_displayvideo_569_CampaignFlightOut",
        "EditGuaranteedOrderReadAccessorsRequestIn": "_displayvideo_570_EditGuaranteedOrderReadAccessorsRequestIn",
        "EditGuaranteedOrderReadAccessorsRequestOut": "_displayvideo_571_EditGuaranteedOrderReadAccessorsRequestOut",
        "BulkEditPartnerAssignedTargetingOptionsResponseIn": "_displayvideo_572_BulkEditPartnerAssignedTargetingOptionsResponseIn",
        "BulkEditPartnerAssignedTargetingOptionsResponseOut": "_displayvideo_573_BulkEditPartnerAssignedTargetingOptionsResponseOut",
        "ViewabilityTargetingOptionDetailsIn": "_displayvideo_574_ViewabilityTargetingOptionDetailsIn",
        "ViewabilityTargetingOptionDetailsOut": "_displayvideo_575_ViewabilityTargetingOptionDetailsOut",
        "CustomListTargetingSettingIn": "_displayvideo_576_CustomListTargetingSettingIn",
        "CustomListTargetingSettingOut": "_displayvideo_577_CustomListTargetingSettingOut",
        "DeactivateManualTriggerRequestIn": "_displayvideo_578_DeactivateManualTriggerRequestIn",
        "DeactivateManualTriggerRequestOut": "_displayvideo_579_DeactivateManualTriggerRequestOut",
        "ListYoutubeAdGroupsResponseIn": "_displayvideo_580_ListYoutubeAdGroupsResponseIn",
        "ListYoutubeAdGroupsResponseOut": "_displayvideo_581_ListYoutubeAdGroupsResponseOut",
        "YoutubeChannelAssignedTargetingOptionDetailsIn": "_displayvideo_582_YoutubeChannelAssignedTargetingOptionDetailsIn",
        "YoutubeChannelAssignedTargetingOptionDetailsOut": "_displayvideo_583_YoutubeChannelAssignedTargetingOptionDetailsOut",
        "NegativeKeywordListAssignedTargetingOptionDetailsIn": "_displayvideo_584_NegativeKeywordListAssignedTargetingOptionDetailsIn",
        "NegativeKeywordListAssignedTargetingOptionDetailsOut": "_displayvideo_585_NegativeKeywordListAssignedTargetingOptionDetailsOut",
        "InsertionOrderBudgetSegmentIn": "_displayvideo_586_InsertionOrderBudgetSegmentIn",
        "InsertionOrderBudgetSegmentOut": "_displayvideo_587_InsertionOrderBudgetSegmentOut",
        "ReplaceSitesResponseIn": "_displayvideo_588_ReplaceSitesResponseIn",
        "ReplaceSitesResponseOut": "_displayvideo_589_ReplaceSitesResponseOut",
        "LineItemBudgetIn": "_displayvideo_590_LineItemBudgetIn",
        "LineItemBudgetOut": "_displayvideo_591_LineItemBudgetOut",
        "AudioContentTypeTargetingOptionDetailsIn": "_displayvideo_592_AudioContentTypeTargetingOptionDetailsIn",
        "AudioContentTypeTargetingOptionDetailsOut": "_displayvideo_593_AudioContentTypeTargetingOptionDetailsOut",
        "ProximityLocationListAssignedTargetingOptionDetailsIn": "_displayvideo_594_ProximityLocationListAssignedTargetingOptionDetailsIn",
        "ProximityLocationListAssignedTargetingOptionDetailsOut": "_displayvideo_595_ProximityLocationListAssignedTargetingOptionDetailsOut",
        "CustomListIn": "_displayvideo_596_CustomListIn",
        "CustomListOut": "_displayvideo_597_CustomListOut",
        "PublisherReviewStatusIn": "_displayvideo_598_PublisherReviewStatusIn",
        "PublisherReviewStatusOut": "_displayvideo_599_PublisherReviewStatusOut",
        "CustomListGroupIn": "_displayvideo_600_CustomListGroupIn",
        "CustomListGroupOut": "_displayvideo_601_CustomListGroupOut",
        "YoutubeAndPartnersSettingsIn": "_displayvideo_602_YoutubeAndPartnersSettingsIn",
        "YoutubeAndPartnersSettingsOut": "_displayvideo_603_YoutubeAndPartnersSettingsOut",
        "AppAssignedTargetingOptionDetailsIn": "_displayvideo_604_AppAssignedTargetingOptionDetailsIn",
        "AppAssignedTargetingOptionDetailsOut": "_displayvideo_605_AppAssignedTargetingOptionDetailsOut",
        "BulkEditPartnerAssignedTargetingOptionsRequestIn": "_displayvideo_606_BulkEditPartnerAssignedTargetingOptionsRequestIn",
        "BulkEditPartnerAssignedTargetingOptionsRequestOut": "_displayvideo_607_BulkEditPartnerAssignedTargetingOptionsRequestOut",
        "PartnerGeneralConfigIn": "_displayvideo_608_PartnerGeneralConfigIn",
        "PartnerGeneralConfigOut": "_displayvideo_609_PartnerGeneralConfigOut",
        "BulkEditAssignedInventorySourcesRequestIn": "_displayvideo_610_BulkEditAssignedInventorySourcesRequestIn",
        "BulkEditAssignedInventorySourcesRequestOut": "_displayvideo_611_BulkEditAssignedInventorySourcesRequestOut",
        "CampaignBudgetIn": "_displayvideo_612_CampaignBudgetIn",
        "CampaignBudgetOut": "_displayvideo_613_CampaignBudgetOut",
        "DoubleVerifyFraudInvalidTrafficIn": "_displayvideo_614_DoubleVerifyFraudInvalidTrafficIn",
        "DoubleVerifyFraudInvalidTrafficOut": "_displayvideo_615_DoubleVerifyFraudInvalidTrafficOut",
        "AdvertiserSdfConfigIn": "_displayvideo_616_AdvertiserSdfConfigIn",
        "AdvertiserSdfConfigOut": "_displayvideo_617_AdvertiserSdfConfigOut",
        "DayAndTimeAssignedTargetingOptionDetailsIn": "_displayvideo_618_DayAndTimeAssignedTargetingOptionDetailsIn",
        "DayAndTimeAssignedTargetingOptionDetailsOut": "_displayvideo_619_DayAndTimeAssignedTargetingOptionDetailsOut",
        "NativeContentPositionAssignedTargetingOptionDetailsIn": "_displayvideo_620_NativeContentPositionAssignedTargetingOptionDetailsIn",
        "NativeContentPositionAssignedTargetingOptionDetailsOut": "_displayvideo_621_NativeContentPositionAssignedTargetingOptionDetailsOut",
        "CounterEventIn": "_displayvideo_622_CounterEventIn",
        "CounterEventOut": "_displayvideo_623_CounterEventOut",
        "NativeContentPositionTargetingOptionDetailsIn": "_displayvideo_624_NativeContentPositionTargetingOptionDetailsIn",
        "NativeContentPositionTargetingOptionDetailsOut": "_displayvideo_625_NativeContentPositionTargetingOptionDetailsOut",
        "CreateSdfDownloadTaskRequestIn": "_displayvideo_626_CreateSdfDownloadTaskRequestIn",
        "CreateSdfDownloadTaskRequestOut": "_displayvideo_627_CreateSdfDownloadTaskRequestOut",
        "YoutubeAndPartnersBiddingStrategyIn": "_displayvideo_628_YoutubeAndPartnersBiddingStrategyIn",
        "YoutubeAndPartnersBiddingStrategyOut": "_displayvideo_629_YoutubeAndPartnersBiddingStrategyOut",
        "BrowserAssignedTargetingOptionDetailsIn": "_displayvideo_630_BrowserAssignedTargetingOptionDetailsIn",
        "BrowserAssignedTargetingOptionDetailsOut": "_displayvideo_631_BrowserAssignedTargetingOptionDetailsOut",
        "MaximizeSpendBidStrategyIn": "_displayvideo_632_MaximizeSpendBidStrategyIn",
        "MaximizeSpendBidStrategyOut": "_displayvideo_633_MaximizeSpendBidStrategyOut",
        "YoutubeAdGroupAdIn": "_displayvideo_634_YoutubeAdGroupAdIn",
        "YoutubeAdGroupAdOut": "_displayvideo_635_YoutubeAdGroupAdOut",
        "UserRewardedContentAssignedTargetingOptionDetailsIn": "_displayvideo_636_UserRewardedContentAssignedTargetingOptionDetailsIn",
        "UserRewardedContentAssignedTargetingOptionDetailsOut": "_displayvideo_637_UserRewardedContentAssignedTargetingOptionDetailsOut",
        "BusinessChainTargetingOptionDetailsIn": "_displayvideo_638_BusinessChainTargetingOptionDetailsIn",
        "BusinessChainTargetingOptionDetailsOut": "_displayvideo_639_BusinessChainTargetingOptionDetailsOut",
        "BulkEditAssignedTargetingOptionsResponseIn": "_displayvideo_640_BulkEditAssignedTargetingOptionsResponseIn",
        "BulkEditAssignedTargetingOptionsResponseOut": "_displayvideo_641_BulkEditAssignedTargetingOptionsResponseOut",
        "TranscodeIn": "_displayvideo_642_TranscodeIn",
        "TranscodeOut": "_displayvideo_643_TranscodeOut",
        "InventorySourceIn": "_displayvideo_644_InventorySourceIn",
        "InventorySourceOut": "_displayvideo_645_InventorySourceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListInvoicesResponseIn"] = t.struct(
        {
            "invoices": t.array(t.proxy(renames["InvoiceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInvoicesResponseIn"])
    types["ListInvoicesResponseOut"] = t.struct(
        {
            "invoices": t.array(t.proxy(renames["InvoiceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInvoicesResponseOut"])
    types["ListCreativesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creatives": t.array(t.proxy(renames["CreativeIn"])).optional(),
        }
    ).named(renames["ListCreativesResponseIn"])
    types["ListCreativesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creatives": t.array(t.proxy(renames["CreativeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativesResponseOut"])
    types["PartnerCostIn"] = t.struct(
        {
            "costType": t.string(),
            "feeType": t.string(),
            "feeAmount": t.string().optional(),
            "invoiceType": t.string().optional(),
            "feePercentageMillis": t.string().optional(),
        }
    ).named(renames["PartnerCostIn"])
    types["PartnerCostOut"] = t.struct(
        {
            "costType": t.string(),
            "feeType": t.string(),
            "feeAmount": t.string().optional(),
            "invoiceType": t.string().optional(),
            "feePercentageMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerCostOut"])
    types["ExchangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"exchange": t.string()}
    ).named(renames["ExchangeAssignedTargetingOptionDetailsIn"])
    types["ExchangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {"exchange": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExchangeAssignedTargetingOptionDetailsOut"])
    types["AgeRangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AgeRangeTargetingOptionDetailsIn"])
    types["AgeRangeTargetingOptionDetailsOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeTargetingOptionDetailsOut"])
    types["InventorySourceFilterIn"] = t.struct(
        {"inventorySourceIds": t.array(t.string()).optional()}
    ).named(renames["InventorySourceFilterIn"])
    types["InventorySourceFilterOut"] = t.struct(
        {
            "inventorySourceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceFilterOut"])
    types["SdfConfigIn"] = t.struct(
        {"adminEmail": t.string().optional(), "version": t.string()}
    ).named(renames["SdfConfigIn"])
    types["SdfConfigOut"] = t.struct(
        {
            "adminEmail": t.string().optional(),
            "version": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfConfigOut"])
    types["LineItemAssignedTargetingOptionIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "assignedTargetingOption": t.proxy(
                renames["AssignedTargetingOptionIn"]
            ).optional(),
        }
    ).named(renames["LineItemAssignedTargetingOptionIn"])
    types["LineItemAssignedTargetingOptionOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "assignedTargetingOption": t.proxy(
                renames["AssignedTargetingOptionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemAssignedTargetingOptionOut"])
    types["ContentInstreamPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"contentInstreamPosition": t.string().optional()}
    ).named(renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"])
    types["ContentInstreamPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "adType": t.string().optional(),
            "contentInstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentInstreamPositionAssignedTargetingOptionDetailsOut"])
    types["GoogleAudienceGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["GoogleAudienceTargetingSettingIn"]))}
    ).named(renames["GoogleAudienceGroupIn"])
    types["GoogleAudienceGroupOut"] = t.struct(
        {
            "settings": t.array(t.proxy(renames["GoogleAudienceTargetingSettingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceGroupOut"])
    types["DoubleVerifyBrandSafetyCategoriesIn"] = t.struct(
        {
            "avoidedMediumSeverityCategories": t.array(t.string()).optional(),
            "avoidedHighSeverityCategories": t.array(t.string()).optional(),
            "avoidUnknownBrandSafetyCategory": t.boolean().optional(),
        }
    ).named(renames["DoubleVerifyBrandSafetyCategoriesIn"])
    types["DoubleVerifyBrandSafetyCategoriesOut"] = t.struct(
        {
            "avoidedMediumSeverityCategories": t.array(t.string()).optional(),
            "avoidedHighSeverityCategories": t.array(t.string()).optional(),
            "avoidUnknownBrandSafetyCategory": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyBrandSafetyCategoriesOut"])
    types["UserRewardedContentTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UserRewardedContentTargetingOptionDetailsIn"])
    types["UserRewardedContentTargetingOptionDetailsOut"] = t.struct(
        {
            "userRewardedContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRewardedContentTargetingOptionDetailsOut"])
    types["InventorySourceAccessorsPartnerAccessorIn"] = t.struct(
        {"partnerId": t.string().optional()}
    ).named(renames["InventorySourceAccessorsPartnerAccessorIn"])
    types["InventorySourceAccessorsPartnerAccessorOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsPartnerAccessorOut"])
    types["ListCustomBiddingScriptsResponseIn"] = t.struct(
        {
            "customBiddingScripts": t.array(
                t.proxy(renames["CustomBiddingScriptIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCustomBiddingScriptsResponseIn"])
    types["ListCustomBiddingScriptsResponseOut"] = t.struct(
        {
            "customBiddingScripts": t.array(
                t.proxy(renames["CustomBiddingScriptOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomBiddingScriptsResponseOut"])
    types["EnvironmentAssignedTargetingOptionDetailsIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["EnvironmentAssignedTargetingOptionDetailsIn"])
    types["EnvironmentAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentAssignedTargetingOptionDetailsOut"])
    types["LanguageTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["LanguageTargetingOptionDetailsIn"])
    types["LanguageTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageTargetingOptionDetailsOut"])
    types["OperatingSystemAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["OperatingSystemAssignedTargetingOptionDetailsIn"])
    types["OperatingSystemAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemAssignedTargetingOptionDetailsOut"])
    types["FirstAndThirdPartyAudienceIn"] = t.struct(
        {
            "membershipDurationDays": t.string().optional(),
            "firstAndThirdPartyAudienceType": t.string().optional(),
            "description": t.string().optional(),
            "appId": t.string().optional(),
            "mobileDeviceIdList": t.proxy(renames["MobileDeviceIdListIn"]).optional(),
            "audienceType": t.string().optional(),
            "displayName": t.string().optional(),
            "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceIn"])
    types["FirstAndThirdPartyAudienceOut"] = t.struct(
        {
            "membershipDurationDays": t.string().optional(),
            "firstAndThirdPartyAudienceType": t.string().optional(),
            "audienceSource": t.string().optional(),
            "description": t.string().optional(),
            "gmailAudienceSize": t.string().optional(),
            "displayAudienceSize": t.string().optional(),
            "appId": t.string().optional(),
            "youtubeAudienceSize": t.string().optional(),
            "mobileDeviceIdList": t.proxy(renames["MobileDeviceIdListOut"]).optional(),
            "activeDisplayAudienceSize": t.string().optional(),
            "audienceType": t.string().optional(),
            "displayDesktopAudienceSize": t.string().optional(),
            "displayMobileWebAudienceSize": t.string().optional(),
            "displayName": t.string().optional(),
            "displayMobileAppAudienceSize": t.string().optional(),
            "contactInfoList": t.proxy(renames["ContactInfoListOut"]).optional(),
            "name": t.string().optional(),
            "firstAndThirdPartyAudienceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceOut"])
    types["ListTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targetingOptions": t.array(
                t.proxy(renames["TargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["ListTargetingOptionsResponseIn"])
    types["ListTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targetingOptions": t.array(
                t.proxy(renames["TargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetingOptionsResponseOut"])
    types["ProductMatchDimensionIn"] = t.struct(
        {
            "customLabel": t.proxy(renames["CustomLabelIn"]).optional(),
            "productOfferId": t.string().optional(),
        }
    ).named(renames["ProductMatchDimensionIn"])
    types["ProductMatchDimensionOut"] = t.struct(
        {
            "customLabel": t.proxy(renames["CustomLabelOut"]).optional(),
            "productOfferId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductMatchDimensionOut"])
    types["FloodlightGroupIn"] = t.struct(
        {
            "activeViewConfig": t.proxy(
                renames["ActiveViewVideoViewabilityMetricConfigIn"]
            ).optional(),
            "lookbackWindow": t.proxy(renames["LookbackWindowIn"]),
            "webTagType": t.string(),
            "displayName": t.string(),
            "customVariables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FloodlightGroupIn"])
    types["FloodlightGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "activeViewConfig": t.proxy(
                renames["ActiveViewVideoViewabilityMetricConfigOut"]
            ).optional(),
            "floodlightGroupId": t.string().optional(),
            "lookbackWindow": t.proxy(renames["LookbackWindowOut"]),
            "webTagType": t.string(),
            "displayName": t.string(),
            "customVariables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightGroupOut"])
    types["PoiSearchTermsIn"] = t.struct({"poiQuery": t.string().optional()}).named(
        renames["PoiSearchTermsIn"]
    )
    types["PoiSearchTermsOut"] = t.struct(
        {
            "poiQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiSearchTermsOut"])
    types["AdvertiserAdServerConfigIn"] = t.struct(
        {
            "cmHybridConfig": t.proxy(renames["CmHybridConfigIn"]).optional(),
            "thirdPartyOnlyConfig": t.proxy(
                renames["ThirdPartyOnlyConfigIn"]
            ).optional(),
        }
    ).named(renames["AdvertiserAdServerConfigIn"])
    types["AdvertiserAdServerConfigOut"] = t.struct(
        {
            "cmHybridConfig": t.proxy(renames["CmHybridConfigOut"]).optional(),
            "thirdPartyOnlyConfig": t.proxy(
                renames["ThirdPartyOnlyConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserAdServerConfigOut"])
    types["PrismaCpeCodeIn"] = t.struct(
        {
            "prismaEstimateCode": t.string().optional(),
            "prismaProductCode": t.string().optional(),
            "prismaClientCode": t.string().optional(),
        }
    ).named(renames["PrismaCpeCodeIn"])
    types["PrismaCpeCodeOut"] = t.struct(
        {
            "prismaEstimateCode": t.string().optional(),
            "prismaProductCode": t.string().optional(),
            "prismaClientCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrismaCpeCodeOut"])
    types["BulkListAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "lineItemAssignedTargetingOptions": t.array(
                t.proxy(renames["LineItemAssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["BulkListAssignedTargetingOptionsResponseIn"])
    types["BulkListAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "lineItemAssignedTargetingOptions": t.array(
                t.proxy(renames["LineItemAssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListAssignedTargetingOptionsResponseOut"])
    types["LookupInvoiceCurrencyResponseIn"] = t.struct(
        {"currencyCode": t.string().optional()}
    ).named(renames["LookupInvoiceCurrencyResponseIn"])
    types["LookupInvoiceCurrencyResponseOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupInvoiceCurrencyResponseOut"])
    types["ListManualTriggersResponseIn"] = t.struct(
        {
            "manualTriggers": t.array(t.proxy(renames["ManualTriggerIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListManualTriggersResponseIn"])
    types["ListManualTriggersResponseOut"] = t.struct(
        {
            "manualTriggers": t.array(t.proxy(renames["ManualTriggerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListManualTriggersResponseOut"])
    types["PerformanceGoalIn"] = t.struct(
        {
            "performanceGoalAmountMicros": t.string().optional(),
            "performanceGoalPercentageMicros": t.string().optional(),
            "performanceGoalString": t.string().optional(),
            "performanceGoalType": t.string(),
        }
    ).named(renames["PerformanceGoalIn"])
    types["PerformanceGoalOut"] = t.struct(
        {
            "performanceGoalAmountMicros": t.string().optional(),
            "performanceGoalPercentageMicros": t.string().optional(),
            "performanceGoalString": t.string().optional(),
            "performanceGoalType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceGoalOut"])
    types["ListLineItemAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["ListLineItemAssignedTargetingOptionsResponseIn"])
    types["ListLineItemAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLineItemAssignedTargetingOptionsResponseOut"])
    types["ReplaceSitesRequestIn"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
            "newSites": t.array(t.proxy(renames["SiteIn"])).optional(),
        }
    ).named(renames["ReplaceSitesRequestIn"])
    types["ReplaceSitesRequestOut"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
            "newSites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceSitesRequestOut"])
    types["ListYoutubeAdGroupAdsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "youtubeAdGroupAds": t.array(
                t.proxy(renames["YoutubeAdGroupAdIn"])
            ).optional(),
        }
    ).named(renames["ListYoutubeAdGroupAdsResponseIn"])
    types["ListYoutubeAdGroupAdsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "youtubeAdGroupAds": t.array(
                t.proxy(renames["YoutubeAdGroupAdOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListYoutubeAdGroupAdsResponseOut"])
    types["ExchangeConfigIn"] = t.struct(
        {
            "enabledExchanges": t.array(
                t.proxy(renames["ExchangeConfigEnabledExchangeIn"])
            ).optional()
        }
    ).named(renames["ExchangeConfigIn"])
    types["ExchangeConfigOut"] = t.struct(
        {
            "enabledExchanges": t.array(
                t.proxy(renames["ExchangeConfigEnabledExchangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeConfigOut"])
    types["AdUrlIn"] = t.struct(
        {"url": t.string().optional(), "type": t.string().optional()}
    ).named(renames["AdUrlIn"])
    types["AdUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUrlOut"])
    types["TargetingExpansionConfigIn"] = t.struct(
        {
            "excludeFirstPartyAudience": t.boolean(),
            "targetingExpansionLevel": t.string(),
        }
    ).named(renames["TargetingExpansionConfigIn"])
    types["TargetingExpansionConfigOut"] = t.struct(
        {
            "excludeFirstPartyAudience": t.boolean(),
            "targetingExpansionLevel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingExpansionConfigOut"])
    types["PrismaConfigIn"] = t.struct(
        {
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeIn"]),
            "prismaType": t.string(),
            "supplier": t.string(),
        }
    ).named(renames["PrismaConfigIn"])
    types["PrismaConfigOut"] = t.struct(
        {
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeOut"]),
            "prismaType": t.string(),
            "supplier": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrismaConfigOut"])
    types["AssignedInventorySourceIn"] = t.struct(
        {"inventorySourceId": t.string()}
    ).named(renames["AssignedInventorySourceIn"])
    types["AssignedInventorySourceOut"] = t.struct(
        {
            "assignedInventorySourceId": t.string().optional(),
            "name": t.string().optional(),
            "inventorySourceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedInventorySourceOut"])
    types["YoutubeVideoDetailsIn"] = t.struct(
        {"unavailableReason": t.string().optional(), "id": t.string().optional()}
    ).named(renames["YoutubeVideoDetailsIn"])
    types["YoutubeVideoDetailsOut"] = t.struct(
        {
            "unavailableReason": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeVideoDetailsOut"])
    types["ParentalStatusAssignedTargetingOptionDetailsIn"] = t.struct(
        {"parentalStatus": t.string().optional()}
    ).named(renames["ParentalStatusAssignedTargetingOptionDetailsIn"])
    types["ParentalStatusAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "parentalStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentalStatusAssignedTargetingOptionDetailsOut"])
    types["ChannelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "channelId": t.string()}
    ).named(renames["ChannelAssignedTargetingOptionDetailsIn"])
    types["ChannelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "channelId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelAssignedTargetingOptionDetailsOut"])
    types["BulkEditAssignedUserRolesRequestIn"] = t.struct(
        {
            "createdAssignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleIn"])
            ).optional(),
            "deletedAssignedUserRoles": t.array(t.string()).optional(),
        }
    ).named(renames["BulkEditAssignedUserRolesRequestIn"])
    types["BulkEditAssignedUserRolesRequestOut"] = t.struct(
        {
            "createdAssignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleOut"])
            ).optional(),
            "deletedAssignedUserRoles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedUserRolesRequestOut"])
    types["BulkUpdateLineItemsResponseIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "skippedLineItemIds": t.array(t.string()).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
            "updatedLineItemIds": t.array(t.string()).optional(),
        }
    ).named(renames["BulkUpdateLineItemsResponseIn"])
    types["BulkUpdateLineItemsResponseOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "skippedLineItemIds": t.array(t.string()).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
            "updatedLineItemIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkUpdateLineItemsResponseOut"])
    types["BulkEditNegativeKeywordsResponseIn"] = t.struct(
        {"negativeKeywords": t.array(t.proxy(renames["NegativeKeywordIn"])).optional()}
    ).named(renames["BulkEditNegativeKeywordsResponseIn"])
    types["BulkEditNegativeKeywordsResponseOut"] = t.struct(
        {
            "negativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditNegativeKeywordsResponseOut"])
    types["EditInventorySourceReadWriteAccessorsRequestIn"] = t.struct(
        {
            "advertisersUpdate": t.proxy(
                renames[
                    "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"
                ]
            ).optional(),
            "assignPartner": t.boolean().optional(),
            "partnerId": t.string(),
        }
    ).named(renames["EditInventorySourceReadWriteAccessorsRequestIn"])
    types["EditInventorySourceReadWriteAccessorsRequestOut"] = t.struct(
        {
            "advertisersUpdate": t.proxy(
                renames[
                    "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut"
                ]
            ).optional(),
            "assignPartner": t.boolean().optional(),
            "partnerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditInventorySourceReadWriteAccessorsRequestOut"])
    types["DigitalContentLabelTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DigitalContentLabelTargetingOptionDetailsIn"])
    types["DigitalContentLabelTargetingOptionDetailsOut"] = t.struct(
        {
            "contentRatingTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigitalContentLabelTargetingOptionDetailsOut"])
    types["HouseholdIncomeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["HouseholdIncomeTargetingOptionDetailsIn"])
    types["HouseholdIncomeTargetingOptionDetailsOut"] = t.struct(
        {
            "householdIncome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HouseholdIncomeTargetingOptionDetailsOut"])
    types["CustomBiddingScriptRefIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["CustomBiddingScriptRefIn"])
    types["CustomBiddingScriptRefOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingScriptRefOut"])
    types["ContentOutstreamPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentOutstreamPositionTargetingOptionDetailsIn"])
    types["ContentOutstreamPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentOutstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOutstreamPositionTargetingOptionDetailsOut"])
    types["OnScreenPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["OnScreenPositionAssignedTargetingOptionDetailsIn"])
    types["OnScreenPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "adType": t.string().optional(),
            "targetingOptionId": t.string(),
            "onScreenPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnScreenPositionAssignedTargetingOptionDetailsOut"])
    types["ExchangeReviewStatusIn"] = t.struct(
        {"status": t.string().optional(), "exchange": t.string().optional()}
    ).named(renames["ExchangeReviewStatusIn"])
    types["ExchangeReviewStatusOut"] = t.struct(
        {
            "status": t.string().optional(),
            "exchange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeReviewStatusOut"])
    types["GenderAssignedTargetingOptionDetailsIn"] = t.struct(
        {"gender": t.string().optional()}
    ).named(renames["GenderAssignedTargetingOptionDetailsIn"])
    types["GenderAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderAssignedTargetingOptionDetailsOut"])
    types["ManualTriggerIn"] = t.struct(
        {
            "advertiserId": t.string(),
            "activationDurationMinutes": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["ManualTriggerIn"])
    types["ManualTriggerOut"] = t.struct(
        {
            "latestActivationTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "state": t.string().optional(),
            "advertiserId": t.string(),
            "activationDurationMinutes": t.string(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualTriggerOut"])
    types["MastheadAdIn"] = t.struct(
        {
            "autoplayVideoDuration": t.string().optional(),
            "description": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "videoAspectRatio": t.string().optional(),
            "companionYoutubeVideos": t.array(
                t.proxy(renames["YoutubeVideoDetailsIn"])
            ).optional(),
            "callToActionFinalUrl": t.string().optional(),
            "callToActionButtonLabel": t.string().optional(),
            "callToActionTrackingUrl": t.string().optional(),
            "headline": t.string().optional(),
            "autoplayVideoStartMillisecond": t.string().optional(),
            "showChannelArt": t.boolean().optional(),
        }
    ).named(renames["MastheadAdIn"])
    types["MastheadAdOut"] = t.struct(
        {
            "autoplayVideoDuration": t.string().optional(),
            "description": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "videoAspectRatio": t.string().optional(),
            "companionYoutubeVideos": t.array(
                t.proxy(renames["YoutubeVideoDetailsOut"])
            ).optional(),
            "callToActionFinalUrl": t.string().optional(),
            "callToActionButtonLabel": t.string().optional(),
            "callToActionTrackingUrl": t.string().optional(),
            "headline": t.string().optional(),
            "autoplayVideoStartMillisecond": t.string().optional(),
            "showChannelArt": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MastheadAdOut"])
    types["ContentDurationAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["ContentDurationAssignedTargetingOptionDetailsIn"])
    types["ContentDurationAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "contentDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentDurationAssignedTargetingOptionDetailsOut"])
    types["ContentGenreTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentGenreTargetingOptionDetailsIn"])
    types["ContentGenreTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentGenreTargetingOptionDetailsOut"])
    types["UniversalAdIdIn"] = t.struct(
        {"registry": t.string().optional(), "id": t.string().optional()}
    ).named(renames["UniversalAdIdIn"])
    types["UniversalAdIdOut"] = t.struct(
        {
            "registry": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UniversalAdIdOut"])
    types["ExchangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ExchangeTargetingOptionDetailsIn"])
    types["ExchangeTargetingOptionDetailsOut"] = t.struct(
        {
            "exchange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeTargetingOptionDetailsOut"])
    types["ExchangeConfigEnabledExchangeIn"] = t.struct(
        {"exchange": t.string().optional()}
    ).named(renames["ExchangeConfigEnabledExchangeIn"])
    types["ExchangeConfigEnabledExchangeOut"] = t.struct(
        {
            "googleAdManagerAgencyId": t.string().optional(),
            "seatId": t.string().optional(),
            "googleAdManagerBuyerNetworkId": t.string().optional(),
            "exchange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeConfigEnabledExchangeOut"])
    types["InventorySourceAccessorsIn"] = t.struct(
        {
            "advertisers": t.proxy(
                renames["InventorySourceAccessorsAdvertiserAccessorsIn"]
            ).optional(),
            "partner": t.proxy(
                renames["InventorySourceAccessorsPartnerAccessorIn"]
            ).optional(),
        }
    ).named(renames["InventorySourceAccessorsIn"])
    types["InventorySourceAccessorsOut"] = t.struct(
        {
            "advertisers": t.proxy(
                renames["InventorySourceAccessorsAdvertiserAccessorsOut"]
            ).optional(),
            "partner": t.proxy(
                renames["InventorySourceAccessorsPartnerAccessorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsOut"])
    types["NegativeKeywordIn"] = t.struct({"keywordValue": t.string()}).named(
        renames["NegativeKeywordIn"]
    )
    types["NegativeKeywordOut"] = t.struct(
        {
            "name": t.string().optional(),
            "keywordValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordOut"])
    types["ExitEventIn"] = t.struct(
        {
            "name": t.string().optional(),
            "url": t.string(),
            "reportingName": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["ExitEventIn"])
    types["ExitEventOut"] = t.struct(
        {
            "name": t.string().optional(),
            "url": t.string(),
            "reportingName": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExitEventOut"])
    types["DoubleVerifyVideoViewabilityIn"] = t.struct(
        {
            "videoIab": t.string().optional(),
            "playerImpressionRate": t.string().optional(),
            "videoViewableRate": t.string().optional(),
        }
    ).named(renames["DoubleVerifyVideoViewabilityIn"])
    types["DoubleVerifyVideoViewabilityOut"] = t.struct(
        {
            "videoIab": t.string().optional(),
            "playerImpressionRate": t.string().optional(),
            "videoViewableRate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyVideoViewabilityOut"])
    types["ListLocationListsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locationLists": t.array(t.proxy(renames["LocationListIn"])).optional(),
        }
    ).named(renames["ListLocationListsResponseIn"])
    types["ListLocationListsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locationLists": t.array(t.proxy(renames["LocationListOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationListsResponseOut"])
    types["DeviceMakeModelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"])
    types["DeviceMakeModelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMakeModelAssignedTargetingOptionDetailsOut"])
    types["RateDetailsIn"] = t.struct(
        {
            "rate": t.proxy(renames["MoneyIn"]).optional(),
            "inventorySourceRateType": t.string().optional(),
            "unitsPurchased": t.string(),
        }
    ).named(renames["RateDetailsIn"])
    types["RateDetailsOut"] = t.struct(
        {
            "rate": t.proxy(renames["MoneyOut"]).optional(),
            "minimumSpend": t.proxy(renames["MoneyOut"]).optional(),
            "inventorySourceRateType": t.string().optional(),
            "unitsPurchased": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateDetailsOut"])
    types["CmHybridConfigIn"] = t.struct(
        {
            "cmFloodlightConfigId": t.string(),
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "cmAccountId": t.string(),
            "cmFloodlightLinkingAuthorized": t.boolean(),
            "cmSyncableSiteIds": t.array(t.string()).optional(),
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
        }
    ).named(renames["CmHybridConfigIn"])
    types["CmHybridConfigOut"] = t.struct(
        {
            "cmFloodlightConfigId": t.string(),
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "cmAccountId": t.string(),
            "cmFloodlightLinkingAuthorized": t.boolean(),
            "cmSyncableSiteIds": t.array(t.string()).optional(),
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmHybridConfigOut"])
    types["SdfDownloadTaskIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["SdfDownloadTaskIn"])
    types["SdfDownloadTaskOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfDownloadTaskOut"])
    types["ListCampaignsResponseIn"] = t.struct(
        {
            "campaigns": t.array(t.proxy(renames["CampaignIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCampaignsResponseIn"])
    types["ListCampaignsResponseOut"] = t.struct(
        {
            "campaigns": t.array(t.proxy(renames["CampaignOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCampaignsResponseOut"])
    types["DeviceMakeModelTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeviceMakeModelTargetingOptionDetailsIn"])
    types["DeviceMakeModelTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMakeModelTargetingOptionDetailsOut"])
    types["TargetFrequencyIn"] = t.struct(
        {
            "timeUnit": t.string().optional(),
            "timeUnitCount": t.integer().optional(),
            "targetCount": t.string().optional(),
        }
    ).named(renames["TargetFrequencyIn"])
    types["TargetFrequencyOut"] = t.struct(
        {
            "timeUnit": t.string().optional(),
            "timeUnitCount": t.integer().optional(),
            "targetCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetFrequencyOut"])
    types["BulkEditAssignedLocationsRequestIn"] = t.struct(
        {
            "deletedAssignedLocations": t.array(t.string()).optional(),
            "createdAssignedLocations": t.array(
                t.proxy(renames["AssignedLocationIn"])
            ).optional(),
        }
    ).named(renames["BulkEditAssignedLocationsRequestIn"])
    types["BulkEditAssignedLocationsRequestOut"] = t.struct(
        {
            "deletedAssignedLocations": t.array(t.string()).optional(),
            "createdAssignedLocations": t.array(
                t.proxy(renames["AssignedLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedLocationsRequestOut"])
    types["AuditAdvertiserResponseIn"] = t.struct(
        {
            "campaignCriteriaCount": t.string().optional(),
            "negativeKeywordListsCount": t.string().optional(),
            "adGroupCriteriaCount": t.string().optional(),
            "negativelyTargetedChannelsCount": t.string().optional(),
            "usedCampaignsCount": t.string().optional(),
            "channelsCount": t.string().optional(),
            "usedInsertionOrdersCount": t.string().optional(),
            "usedLineItemsCount": t.string().optional(),
        }
    ).named(renames["AuditAdvertiserResponseIn"])
    types["AuditAdvertiserResponseOut"] = t.struct(
        {
            "campaignCriteriaCount": t.string().optional(),
            "negativeKeywordListsCount": t.string().optional(),
            "adGroupCriteriaCount": t.string().optional(),
            "negativelyTargetedChannelsCount": t.string().optional(),
            "usedCampaignsCount": t.string().optional(),
            "channelsCount": t.string().optional(),
            "usedInsertionOrdersCount": t.string().optional(),
            "usedLineItemsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditAdvertiserResponseOut"])
    types["ContactInfoIn"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "zipCodes": t.array(t.string()).optional(),
            "hashedLastName": t.string().optional(),
            "hashedEmails": t.array(t.string()).optional(),
            "hashedFirstName": t.string().optional(),
            "hashedPhoneNumbers": t.array(t.string()).optional(),
        }
    ).named(renames["ContactInfoIn"])
    types["ContactInfoOut"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "zipCodes": t.array(t.string()).optional(),
            "hashedLastName": t.string().optional(),
            "hashedEmails": t.array(t.string()).optional(),
            "hashedFirstName": t.string().optional(),
            "hashedPhoneNumbers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoOut"])
    types["AdlooxIn"] = t.struct(
        {"excludedAdlooxCategories": t.array(t.string()).optional()}
    ).named(renames["AdlooxIn"])
    types["AdlooxOut"] = t.struct(
        {
            "excludedAdlooxCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdlooxOut"])
    types["YoutubeAdGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigIn"]
            ).optional(),
            "adGroupFormat": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyIn"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "productFeedData": t.proxy(renames["ProductFeedDataIn"]).optional(),
            "entityStatus": t.string().optional(),
            "youtubeAdIds": t.array(t.string()).optional(),
        }
    ).named(renames["YoutubeAdGroupIn"])
    types["YoutubeAdGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigOut"]
            ).optional(),
            "adGroupFormat": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyOut"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "productFeedData": t.proxy(renames["ProductFeedDataOut"]).optional(),
            "entityStatus": t.string().optional(),
            "youtubeAdIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupOut"])
    types["OmidTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OmidTargetingOptionDetailsIn"])
    types["OmidTargetingOptionDetailsOut"] = t.struct(
        {
            "omid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmidTargetingOptionDetailsOut"])
    types["InStreamAdIn"] = t.struct(
        {
            "commonInStreamAttribute": t.proxy(
                renames["CommonInStreamAttributeIn"]
            ).optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InStreamAdIn"])
    types["InStreamAdOut"] = t.struct(
        {
            "commonInStreamAttribute": t.proxy(
                renames["CommonInStreamAttributeOut"]
            ).optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InStreamAdOut"])
    types["CreateAssetResponseIn"] = t.struct(
        {"asset": t.proxy(renames["AssetIn"]).optional()}
    ).named(renames["CreateAssetResponseIn"])
    types["CreateAssetResponseOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAssetResponseOut"])
    types["VideoAdSequenceStepIn"] = t.struct(
        {
            "interactionType": t.string().optional(),
            "previousStepId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "stepId": t.string().optional(),
        }
    ).named(renames["VideoAdSequenceStepIn"])
    types["VideoAdSequenceStepOut"] = t.struct(
        {
            "interactionType": t.string().optional(),
            "previousStepId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "stepId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAdSequenceStepOut"])
    types["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"] = t.struct(
        {
            "reachVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "brandSafetyVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "viewabilityVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "brandLiftVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
        }
    ).named(renames["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"])
    types["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"] = t.struct(
        {
            "reachVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "brandSafetyVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "viewabilityVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "brandLiftVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"])
    types["BusinessChainAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "proximityRadiusAmount": t.number(),
            "proximityRadiusUnit": t.string(),
            "targetingOptionId": t.string(),
        }
    ).named(renames["BusinessChainAssignedTargetingOptionDetailsIn"])
    types["BusinessChainAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "proximityRadiusAmount": t.number(),
            "displayName": t.string().optional(),
            "proximityRadiusUnit": t.string(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessChainAssignedTargetingOptionDetailsOut"])
    types["YoutubeVideoAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "videoId": t.string().optional()}
    ).named(renames["YoutubeVideoAssignedTargetingOptionDetailsIn"])
    types["YoutubeVideoAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "videoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeVideoAssignedTargetingOptionDetailsOut"])
    types["GoogleAudienceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAudienceIn"]
    )
    types["GoogleAudienceOut"] = t.struct(
        {
            "googleAudienceType": t.string().optional(),
            "googleAudienceId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceOut"])
    types["YoutubeAndPartnersInventorySourceConfigIn"] = t.struct(
        {
            "includeYoutubeVideoPartners": t.boolean().optional(),
            "includeYoutubeSearch": t.boolean().optional(),
            "includeYoutubeVideos": t.boolean().optional(),
        }
    ).named(renames["YoutubeAndPartnersInventorySourceConfigIn"])
    types["YoutubeAndPartnersInventorySourceConfigOut"] = t.struct(
        {
            "includeYoutubeVideoPartners": t.boolean().optional(),
            "includeYoutubeSearch": t.boolean().optional(),
            "includeYoutubeVideos": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersInventorySourceConfigOut"])
    types["CreativeIn"] = t.struct(
        {
            "skippable": t.boolean().optional(),
            "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
            "entityStatus": t.string(),
            "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
            "jsTrackerUrl": t.string().optional(),
            "vastTagUrl": t.string().optional(),
            "notes": t.string().optional(),
            "additionalDimensions": t.array(
                t.proxy(renames["DimensionsIn"])
            ).optional(),
            "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
            "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]),
            "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
            "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
            "thirdPartyUrls": t.array(t.proxy(renames["ThirdPartyUrlIn"])).optional(),
            "creativeType": t.string(),
            "expandingDirection": t.string().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "thirdPartyTag": t.string().optional(),
            "requirePingForAttribution": t.boolean().optional(),
            "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
            "expandOnHover": t.boolean().optional(),
            "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
            "requireHtml5": t.boolean().optional(),
            "displayName": t.string(),
            "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
            "iasCampaignMonitoring": t.boolean().optional(),
            "integrationCode": t.string().optional(),
            "trackerUrls": t.array(t.string()).optional(),
            "appendedTag": t.string().optional(),
            "requireMraid": t.boolean().optional(),
            "hostingSource": t.string(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "skippable": t.boolean().optional(),
            "cmTrackingAd": t.proxy(renames["CmTrackingAdOut"]).optional(),
            "entityStatus": t.string(),
            "obaIcon": t.proxy(renames["ObaIconOut"]).optional(),
            "reviewStatus": t.proxy(renames["ReviewStatusInfoOut"]).optional(),
            "jsTrackerUrl": t.string().optional(),
            "vastTagUrl": t.string().optional(),
            "updateTime": t.string().optional(),
            "cmPlacementId": t.string().optional(),
            "notes": t.string().optional(),
            "additionalDimensions": t.array(
                t.proxy(renames["DimensionsOut"])
            ).optional(),
            "vpaid": t.boolean().optional(),
            "creativeId": t.string().optional(),
            "oggAudio": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "counterEvents": t.array(t.proxy(renames["CounterEventOut"])).optional(),
            "skipOffset": t.proxy(renames["AudioVideoOffsetOut"]).optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]),
            "mediaDuration": t.string().optional(),
            "name": t.string().optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdOut"]).optional(),
            "progressOffset": t.proxy(renames["AudioVideoOffsetOut"]).optional(),
            "mp3Audio": t.boolean().optional(),
            "thirdPartyUrls": t.array(t.proxy(renames["ThirdPartyUrlOut"])).optional(),
            "dynamic": t.boolean().optional(),
            "creativeType": t.string(),
            "lineItemIds": t.array(t.string()).optional(),
            "expandingDirection": t.string().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "thirdPartyTag": t.string().optional(),
            "html5Video": t.boolean().optional(),
            "requirePingForAttribution": t.boolean().optional(),
            "exitEvents": t.array(t.proxy(renames["ExitEventOut"])),
            "expandOnHover": t.boolean().optional(),
            "creativeAttributes": t.array(t.string()).optional(),
            "timerEvents": t.array(t.proxy(renames["TimerEventOut"])).optional(),
            "transcodes": t.array(t.proxy(renames["TranscodeOut"])).optional(),
            "requireHtml5": t.boolean().optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetAssociationOut"])),
            "iasCampaignMonitoring": t.boolean().optional(),
            "integrationCode": t.string().optional(),
            "trackerUrls": t.array(t.string()).optional(),
            "appendedTag": t.string().optional(),
            "requireMraid": t.boolean().optional(),
            "hostingSource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["BulkEditAdvertiserAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
            ).optional(),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
            ).optional(),
        }
    ).named(renames["BulkEditAdvertiserAssignedTargetingOptionsRequestIn"])
    types["BulkEditAdvertiserAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAdvertiserAssignedTargetingOptionsRequestOut"])
    types["ParentEntityFilterIn"] = t.struct(
        {
            "filterType": t.string(),
            "fileType": t.array(t.string()),
            "filterIds": t.array(t.string()).optional(),
        }
    ).named(renames["ParentEntityFilterIn"])
    types["ParentEntityFilterOut"] = t.struct(
        {
            "filterType": t.string(),
            "fileType": t.array(t.string()),
            "filterIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentEntityFilterOut"])
    types["NonSkippableAdIn"] = t.struct(
        {
            "commonInStreamAttribute": t.proxy(
                renames["CommonInStreamAttributeIn"]
            ).optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["NonSkippableAdIn"])
    types["NonSkippableAdOut"] = t.struct(
        {
            "commonInStreamAttribute": t.proxy(
                renames["CommonInStreamAttributeOut"]
            ).optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSkippableAdOut"])
    types["PerformanceGoalBidStrategyIn"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalType": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "performanceGoalAmountMicros": t.string(),
        }
    ).named(renames["PerformanceGoalBidStrategyIn"])
    types["PerformanceGoalBidStrategyOut"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalType": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "performanceGoalAmountMicros": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceGoalBidStrategyOut"])
    types["TimerEventIn"] = t.struct(
        {"reportingName": t.string(), "name": t.string()}
    ).named(renames["TimerEventIn"])
    types["TimerEventOut"] = t.struct(
        {
            "reportingName": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimerEventOut"])
    types["InventorySourceAccessorsAdvertiserAccessorsIn"] = t.struct(
        {"advertiserIds": t.array(t.string()).optional()}
    ).named(renames["InventorySourceAccessorsAdvertiserAccessorsIn"])
    types["InventorySourceAccessorsAdvertiserAccessorsOut"] = t.struct(
        {
            "advertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsAdvertiserAccessorsOut"])
    types["CombinedAudienceGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["CombinedAudienceTargetingSettingIn"]))}
    ).named(renames["CombinedAudienceGroupIn"])
    types["CombinedAudienceGroupOut"] = t.struct(
        {
            "settings": t.array(
                t.proxy(renames["CombinedAudienceTargetingSettingOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CombinedAudienceGroupOut"])
    types["ListPartnerAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["ListPartnerAssignedTargetingOptionsResponseIn"])
    types["ListPartnerAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPartnerAssignedTargetingOptionsResponseOut"])
    types["AdvertiserBillingConfigIn"] = t.struct(
        {"billingProfileId": t.string().optional()}
    ).named(renames["AdvertiserBillingConfigIn"])
    types["AdvertiserBillingConfigOut"] = t.struct(
        {
            "billingProfileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserBillingConfigOut"])
    types["DuplicateLineItemRequestIn"] = t.struct(
        {"targetDisplayName": t.string().optional()}
    ).named(renames["DuplicateLineItemRequestIn"])
    types["DuplicateLineItemRequestOut"] = t.struct(
        {
            "targetDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateLineItemRequestOut"])
    types["CarrierAndIspTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CarrierAndIspTargetingOptionDetailsIn"])
    types["CarrierAndIspTargetingOptionDetailsOut"] = t.struct(
        {
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarrierAndIspTargetingOptionDetailsOut"])
    types["EnvironmentTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EnvironmentTargetingOptionDetailsIn"])
    types["EnvironmentTargetingOptionDetailsOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentTargetingOptionDetailsOut"])
    types["ParentalStatusTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ParentalStatusTargetingOptionDetailsIn"])
    types["ParentalStatusTargetingOptionDetailsOut"] = t.struct(
        {
            "parentalStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentalStatusTargetingOptionDetailsOut"])
    types["DeviceTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeviceTypeTargetingOptionDetailsIn"])
    types["DeviceTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTypeTargetingOptionDetailsOut"])
    types["AssetIn"] = t.struct(
        {"mediaId": t.string().optional(), "content": t.string().optional()}
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "mediaId": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["CombinedAudienceTargetingSettingIn"] = t.struct(
        {"combinedAudienceId": t.string()}
    ).named(renames["CombinedAudienceTargetingSettingIn"])
    types["CombinedAudienceTargetingSettingOut"] = t.struct(
        {
            "combinedAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CombinedAudienceTargetingSettingOut"])
    types["CmTrackingAdIn"] = t.struct(
        {
            "cmPlacementId": t.string().optional(),
            "cmAdId": t.string().optional(),
            "cmCreativeId": t.string().optional(),
        }
    ).named(renames["CmTrackingAdIn"])
    types["CmTrackingAdOut"] = t.struct(
        {
            "cmPlacementId": t.string().optional(),
            "cmAdId": t.string().optional(),
            "cmCreativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmTrackingAdOut"])
    types["FirstAndThirdPartyAudienceGroupIn"] = t.struct(
        {
            "settings": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceTargetingSettingIn"])
            )
        }
    ).named(renames["FirstAndThirdPartyAudienceGroupIn"])
    types["FirstAndThirdPartyAudienceGroupOut"] = t.struct(
        {
            "settings": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceTargetingSettingOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceGroupOut"])
    types["AudioAdIn"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "finalUrl": t.string().optional(),
            "displayUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
        }
    ).named(renames["AudioAdIn"])
    types["AudioAdOut"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "finalUrl": t.string().optional(),
            "displayUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioAdOut"])
    types["LineItemFlightIn"] = t.struct(
        {
            "flightDateType": t.string(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
        }
    ).named(renames["LineItemFlightIn"])
    types["LineItemFlightOut"] = t.struct(
        {
            "flightDateType": t.string(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemFlightOut"])
    types["CreativeConfigIn"] = t.struct(
        {
            "creativeType": t.string().optional(),
            "videoCreativeConfig": t.proxy(
                renames["InventorySourceVideoCreativeConfigIn"]
            ).optional(),
            "displayCreativeConfig": t.proxy(
                renames["InventorySourceDisplayCreativeConfigIn"]
            ).optional(),
        }
    ).named(renames["CreativeConfigIn"])
    types["CreativeConfigOut"] = t.struct(
        {
            "creativeType": t.string().optional(),
            "videoCreativeConfig": t.proxy(
                renames["InventorySourceVideoCreativeConfigOut"]
            ).optional(),
            "displayCreativeConfig": t.proxy(
                renames["InventorySourceDisplayCreativeConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeConfigOut"])
    types["SensitiveCategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SensitiveCategoryTargetingOptionDetailsIn"])
    types["SensitiveCategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "sensitiveCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveCategoryTargetingOptionDetailsOut"])
    types["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"])
    types["AuthorizedSellerStatusAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "authorizedSellerStatus": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsOut"])
    types["EditGuaranteedOrderReadAccessorsResponseIn"] = t.struct(
        {
            "readAccessInherited": t.boolean().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsResponseIn"])
    types["EditGuaranteedOrderReadAccessorsResponseOut"] = t.struct(
        {
            "readAccessInherited": t.boolean().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsResponseOut"])
    types["DoubleVerifyDisplayViewabilityIn"] = t.struct(
        {"viewableDuring": t.string().optional(), "iab": t.string().optional()}
    ).named(renames["DoubleVerifyDisplayViewabilityIn"])
    types["DoubleVerifyDisplayViewabilityOut"] = t.struct(
        {
            "viewableDuring": t.string().optional(),
            "iab": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyDisplayViewabilityOut"])
    types["BulkListCampaignAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["BulkListCampaignAssignedTargetingOptionsResponseIn"])
    types["BulkListCampaignAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListCampaignAssignedTargetingOptionsResponseOut"])
    types["ScriptErrorIn"] = t.struct(
        {
            "line": t.string().optional(),
            "errorMessage": t.string().optional(),
            "column": t.string().optional(),
            "errorCode": t.string().optional(),
        }
    ).named(renames["ScriptErrorIn"])
    types["ScriptErrorOut"] = t.struct(
        {
            "line": t.string().optional(),
            "errorMessage": t.string().optional(),
            "column": t.string().optional(),
            "errorCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptErrorOut"])
    types["DoubleVerifyAppStarRatingIn"] = t.struct(
        {
            "avoidedStarRating": t.string().optional(),
            "avoidInsufficientStarRating": t.boolean().optional(),
        }
    ).named(renames["DoubleVerifyAppStarRatingIn"])
    types["DoubleVerifyAppStarRatingOut"] = t.struct(
        {
            "avoidedStarRating": t.string().optional(),
            "avoidInsufficientStarRating": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyAppStarRatingOut"])
    types["IdFilterIn"] = t.struct(
        {
            "lineItemIds": t.array(t.string()).optional(),
            "adGroupAdIds": t.array(t.string()).optional(),
            "mediaProductIds": t.array(t.string()).optional(),
            "insertionOrderIds": t.array(t.string()).optional(),
            "campaignIds": t.array(t.string()).optional(),
            "adGroupIds": t.array(t.string()).optional(),
        }
    ).named(renames["IdFilterIn"])
    types["IdFilterOut"] = t.struct(
        {
            "lineItemIds": t.array(t.string()).optional(),
            "adGroupAdIds": t.array(t.string()).optional(),
            "mediaProductIds": t.array(t.string()).optional(),
            "insertionOrderIds": t.array(t.string()).optional(),
            "campaignIds": t.array(t.string()).optional(),
            "adGroupIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdFilterOut"])
    types["OmidAssignedTargetingOptionDetailsIn"] = t.struct(
        {"omid": t.string().optional()}
    ).named(renames["OmidAssignedTargetingOptionDetailsIn"])
    types["OmidAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "omid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmidAssignedTargetingOptionDetailsOut"])
    types["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "doubleVerify": t.proxy(renames["DoubleVerifyIn"]).optional(),
            "adloox": t.proxy(renames["AdlooxIn"]).optional(),
            "integralAdScience": t.proxy(renames["IntegralAdScienceIn"]).optional(),
        }
    ).named(renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"])
    types["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "doubleVerify": t.proxy(renames["DoubleVerifyOut"]).optional(),
            "adloox": t.proxy(renames["AdlooxOut"]).optional(),
            "integralAdScience": t.proxy(renames["IntegralAdScienceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"])
    types["UserIn"] = t.struct(
        {
            "assignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleIn"])
            ).optional(),
            "email": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "assignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleOut"])
            ).optional(),
            "email": t.string(),
            "userId": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["PartnerRevenueModelIn"] = t.struct(
        {"markupType": t.string(), "markupAmount": t.string()}
    ).named(renames["PartnerRevenueModelIn"])
    types["PartnerRevenueModelOut"] = t.struct(
        {
            "markupType": t.string(),
            "markupAmount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerRevenueModelOut"])
    types["NegativeKeywordListIn"] = t.struct({"displayName": t.string()}).named(
        renames["NegativeKeywordListIn"]
    )
    types["NegativeKeywordListOut"] = t.struct(
        {
            "negativeKeywordListId": t.string().optional(),
            "displayName": t.string(),
            "targetedLineItemCount": t.string().optional(),
            "name": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordListOut"])
    types["ListYoutubeAdGroupAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["ListYoutubeAdGroupAssignedTargetingOptionsResponseIn"])
    types["ListYoutubeAdGroupAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListYoutubeAdGroupAssignedTargetingOptionsResponseOut"])
    types["ListChannelsResponseIn"] = t.struct(
        {
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListChannelsResponseIn"])
    types["ListChannelsResponseOut"] = t.struct(
        {
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChannelsResponseOut"])
    types["ListAssignedLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedLocations": t.array(
                t.proxy(renames["AssignedLocationIn"])
            ).optional(),
        }
    ).named(renames["ListAssignedLocationsResponseIn"])
    types["ListAssignedLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedLocations": t.array(
                t.proxy(renames["AssignedLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssignedLocationsResponseOut"])
    types["BulkEditAssignedInventorySourcesResponseIn"] = t.struct(
        {
            "assignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceIn"])
            ).optional()
        }
    ).named(renames["BulkEditAssignedInventorySourcesResponseIn"])
    types["BulkEditAssignedInventorySourcesResponseOut"] = t.struct(
        {
            "assignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesResponseOut"])
    types["AudienceGroupAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "includedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupIn"]
            ).optional(),
            "excludedFirstAndThirdPartyAudienceGroup": t.proxy(
                renames["FirstAndThirdPartyAudienceGroupIn"]
            ).optional(),
            "excludedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupIn"]
            ).optional(),
            "includedCustomListGroup": t.proxy(renames["CustomListGroupIn"]).optional(),
            "includedCombinedAudienceGroup": t.proxy(
                renames["CombinedAudienceGroupIn"]
            ).optional(),
            "includedFirstAndThirdPartyAudienceGroups": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceGroupIn"])
            ).optional(),
        }
    ).named(renames["AudienceGroupAssignedTargetingOptionDetailsIn"])
    types["AudienceGroupAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "includedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupOut"]
            ).optional(),
            "excludedFirstAndThirdPartyAudienceGroup": t.proxy(
                renames["FirstAndThirdPartyAudienceGroupOut"]
            ).optional(),
            "excludedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupOut"]
            ).optional(),
            "includedCustomListGroup": t.proxy(
                renames["CustomListGroupOut"]
            ).optional(),
            "includedCombinedAudienceGroup": t.proxy(
                renames["CombinedAudienceGroupOut"]
            ).optional(),
            "includedFirstAndThirdPartyAudienceGroups": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudienceGroupAssignedTargetingOptionDetailsOut"])
    types["ListFirstAndThirdPartyAudiencesResponseIn"] = t.struct(
        {
            "firstAndThirdPartyAudiences": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFirstAndThirdPartyAudiencesResponseIn"])
    types["ListFirstAndThirdPartyAudiencesResponseOut"] = t.struct(
        {
            "firstAndThirdPartyAudiences": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFirstAndThirdPartyAudiencesResponseOut"])
    types["AssignedLocationIn"] = t.struct({"targetingOptionId": t.string()}).named(
        renames["AssignedLocationIn"]
    )
    types["AssignedLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "targetingOptionId": t.string(),
            "assignedLocationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedLocationOut"])
    types["CustomBiddingScriptIn"] = t.struct(
        {"script": t.proxy(renames["CustomBiddingScriptRefIn"]).optional()}
    ).named(renames["CustomBiddingScriptIn"])
    types["CustomBiddingScriptOut"] = t.struct(
        {
            "active": t.boolean().optional(),
            "name": t.string().optional(),
            "errors": t.array(t.proxy(renames["ScriptErrorOut"])).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "customBiddingScriptId": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "script": t.proxy(renames["CustomBiddingScriptRefOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingScriptOut"])
    types["BudgetSummaryIn"] = t.struct(
        {
            "preTaxAmountMicros": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeIn"]).optional(),
            "taxAmountMicros": t.string().optional(),
            "externalBudgetId": t.string().optional(),
        }
    ).named(renames["BudgetSummaryIn"])
    types["BudgetSummaryOut"] = t.struct(
        {
            "preTaxAmountMicros": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeOut"]).optional(),
            "taxAmountMicros": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BudgetSummaryOut"])
    types["InsertionOrderIn"] = t.struct(
        {
            "entityStatus": t.string(),
            "insertionOrderType": t.string().optional(),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
            "pacing": t.proxy(renames["PacingIn"]),
            "billableOutcome": t.string().optional(),
            "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
            "campaignId": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["InsertionOrderIn"])
    types["InsertionOrderOut"] = t.struct(
        {
            "entityStatus": t.string(),
            "insertionOrderType": t.string().optional(),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostOut"])).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "bidStrategy": t.proxy(renames["BiddingStrategyOut"]).optional(),
            "pacing": t.proxy(renames["PacingOut"]),
            "billableOutcome": t.string().optional(),
            "performanceGoal": t.proxy(renames["PerformanceGoalOut"]),
            "updateTime": t.string().optional(),
            "reservationType": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "advertiserId": t.string().optional(),
            "budget": t.proxy(renames["InsertionOrderBudgetOut"]),
            "name": t.string().optional(),
            "campaignId": t.string(),
            "displayName": t.string(),
            "insertionOrderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderOut"])
    types["PacingIn"] = t.struct(
        {
            "dailyMaxMicros": t.string().optional(),
            "pacingPeriod": t.string(),
            "dailyMaxImpressions": t.string().optional(),
            "pacingType": t.string(),
        }
    ).named(renames["PacingIn"])
    types["PacingOut"] = t.struct(
        {
            "dailyMaxMicros": t.string().optional(),
            "pacingPeriod": t.string(),
            "dailyMaxImpressions": t.string().optional(),
            "pacingType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PacingOut"])
    types["RegionalLocationListAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "regionalLocationListId": t.string()}
    ).named(renames["RegionalLocationListAssignedTargetingOptionDetailsIn"])
    types["RegionalLocationListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "regionalLocationListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalLocationListAssignedTargetingOptionDetailsOut"])
    types["CampaignGoalIn"] = t.struct(
        {
            "campaignGoalType": t.string(),
            "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
        }
    ).named(renames["CampaignGoalIn"])
    types["CampaignGoalOut"] = t.struct(
        {
            "campaignGoalType": t.string(),
            "performanceGoal": t.proxy(renames["PerformanceGoalOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignGoalOut"])
    types["GeoRegionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["GeoRegionAssignedTargetingOptionDetailsIn"])
    types["GeoRegionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "geoRegionType": t.string().optional(),
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionAssignedTargetingOptionDetailsOut"])
    types["VideoPlayerSizeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"videoPlayerSize": t.string().optional()}
    ).named(renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"])
    types["VideoPlayerSizeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "videoPlayerSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerSizeAssignedTargetingOptionDetailsOut"])
    types["ListPartnersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "partners": t.array(t.proxy(renames["PartnerIn"])).optional(),
        }
    ).named(renames["ListPartnersResponseIn"])
    types["ListPartnersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "partners": t.array(t.proxy(renames["PartnerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPartnersResponseOut"])
    types["PoiTargetingOptionDetailsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PoiTargetingOptionDetailsIn"]
    )
    types["PoiTargetingOptionDetailsOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiTargetingOptionDetailsOut"])
    types["TrackingFloodlightActivityConfigIn"] = t.struct(
        {
            "floodlightActivityId": t.string(),
            "postViewLookbackWindowDays": t.integer(),
            "postClickLookbackWindowDays": t.integer(),
        }
    ).named(renames["TrackingFloodlightActivityConfigIn"])
    types["TrackingFloodlightActivityConfigOut"] = t.struct(
        {
            "floodlightActivityId": t.string(),
            "postViewLookbackWindowDays": t.integer(),
            "postClickLookbackWindowDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackingFloodlightActivityConfigOut"])
    types["ListAdvertisersResponseIn"] = t.struct(
        {
            "advertisers": t.array(t.proxy(renames["AdvertiserIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAdvertisersResponseIn"])
    types["ListAdvertisersResponseOut"] = t.struct(
        {
            "advertisers": t.array(t.proxy(renames["AdvertiserOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAdvertisersResponseOut"])
    types["ChannelIn"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "displayName": t.string(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "positivelyTargetedLineItemCount": t.string().optional(),
            "negativelyTargetedLineItemCount": t.string().optional(),
            "channelId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["DimensionsIn"] = t.struct(
        {"heightPixels": t.integer().optional(), "widthPixels": t.integer().optional()}
    ).named(renames["DimensionsIn"])
    types["DimensionsOut"] = t.struct(
        {
            "heightPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionsOut"])
    types["ContactInfoListIn"] = t.struct(
        {"contactInfos": t.array(t.proxy(renames["ContactInfoIn"])).optional()}
    ).named(renames["ContactInfoListIn"])
    types["ContactInfoListOut"] = t.struct(
        {
            "contactInfos": t.array(t.proxy(renames["ContactInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoListOut"])
    types["UrlAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "url": t.string()}
    ).named(renames["UrlAssignedTargetingOptionDetailsIn"])
    types["UrlAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "url": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlAssignedTargetingOptionDetailsOut"])
    types["GuaranteedOrderIn"] = t.struct(
        {
            "readWriteAdvertiserId": t.string().optional(),
            "readWritePartnerId": t.string().optional(),
            "displayName": t.string(),
            "status": t.proxy(renames["GuaranteedOrderStatusIn"]).optional(),
            "exchange": t.string(),
            "publisherName": t.string(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
            "defaultCampaignId": t.string().optional(),
        }
    ).named(renames["GuaranteedOrderIn"])
    types["GuaranteedOrderOut"] = t.struct(
        {
            "readWriteAdvertiserId": t.string().optional(),
            "readWritePartnerId": t.string().optional(),
            "legacyGuaranteedOrderId": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "status": t.proxy(renames["GuaranteedOrderStatusOut"]).optional(),
            "guaranteedOrderId": t.string().optional(),
            "exchange": t.string(),
            "updateTime": t.string().optional(),
            "publisherName": t.string(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
            "defaultAdvertiserId": t.string().optional(),
            "defaultCampaignId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedOrderOut"])
    types["AdvertiserCreativeConfigIn"] = t.struct(
        {
            "videoCreativeDataSharingAuthorized": t.boolean().optional(),
            "dynamicCreativeEnabled": t.boolean().optional(),
            "obaComplianceDisabled": t.boolean().optional(),
            "iasClientId": t.string().optional(),
        }
    ).named(renames["AdvertiserCreativeConfigIn"])
    types["AdvertiserCreativeConfigOut"] = t.struct(
        {
            "videoCreativeDataSharingAuthorized": t.boolean().optional(),
            "dynamicCreativeEnabled": t.boolean().optional(),
            "obaComplianceDisabled": t.boolean().optional(),
            "iasClientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserCreativeConfigOut"])
    types["VideoPerformanceAdIn"] = t.struct(
        {
            "videos": t.array(t.proxy(renames["YoutubeVideoDetailsIn"])).optional(),
            "actionButtonLabels": t.array(t.string()).optional(),
            "headlines": t.array(t.string()).optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "finalUrl": t.string().optional(),
            "descriptions": t.array(t.string()).optional(),
            "companionBanners": t.array(t.proxy(renames["ImageAssetIn"])).optional(),
            "trackingUrl": t.string().optional(),
            "displayUrlBreadcrumb1": t.string().optional(),
            "longHeadlines": t.array(t.string()).optional(),
            "domain": t.string().optional(),
            "displayUrlBreadcrumb2": t.string().optional(),
        }
    ).named(renames["VideoPerformanceAdIn"])
    types["VideoPerformanceAdOut"] = t.struct(
        {
            "videos": t.array(t.proxy(renames["YoutubeVideoDetailsOut"])).optional(),
            "actionButtonLabels": t.array(t.string()).optional(),
            "headlines": t.array(t.string()).optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "finalUrl": t.string().optional(),
            "descriptions": t.array(t.string()).optional(),
            "companionBanners": t.array(t.proxy(renames["ImageAssetOut"])).optional(),
            "trackingUrl": t.string().optional(),
            "displayUrlBreadcrumb1": t.string().optional(),
            "longHeadlines": t.array(t.string()).optional(),
            "domain": t.string().optional(),
            "displayUrlBreadcrumb2": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPerformanceAdOut"])
    types["ListNegativeKeywordListsResponseIn"] = t.struct(
        {
            "negativeKeywordLists": t.array(
                t.proxy(renames["NegativeKeywordListIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNegativeKeywordListsResponseIn"])
    types["ListNegativeKeywordListsResponseOut"] = t.struct(
        {
            "negativeKeywordLists": t.array(
                t.proxy(renames["NegativeKeywordListOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNegativeKeywordListsResponseOut"])
    types["GuaranteedOrderStatusIn"] = t.struct(
        {
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
        }
    ).named(renames["GuaranteedOrderStatusIn"])
    types["GuaranteedOrderStatusOut"] = t.struct(
        {
            "configStatus": t.string().optional(),
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedOrderStatusOut"])
    types["BulkEditNegativeKeywordsRequestIn"] = t.struct(
        {
            "createdNegativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordIn"])
            ).optional(),
            "deletedNegativeKeywords": t.array(t.string()).optional(),
        }
    ).named(renames["BulkEditNegativeKeywordsRequestIn"])
    types["BulkEditNegativeKeywordsRequestOut"] = t.struct(
        {
            "createdNegativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordOut"])
            ).optional(),
            "deletedNegativeKeywords": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditNegativeKeywordsRequestOut"])
    types["ReplaceNegativeKeywordsRequestIn"] = t.struct(
        {
            "newNegativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordIn"])
            ).optional()
        }
    ).named(renames["ReplaceNegativeKeywordsRequestIn"])
    types["ReplaceNegativeKeywordsRequestOut"] = t.struct(
        {
            "newNegativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceNegativeKeywordsRequestOut"])
    types["BulkEditSitesResponseIn"] = t.struct(
        {"sites": t.array(t.proxy(renames["SiteIn"])).optional()}
    ).named(renames["BulkEditSitesResponseIn"])
    types["BulkEditSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditSitesResponseOut"])
    types["AuthorizedSellerStatusTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizedSellerStatusTargetingOptionDetailsIn"])
    types["AuthorizedSellerStatusTargetingOptionDetailsOut"] = t.struct(
        {
            "authorizedSellerStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedSellerStatusTargetingOptionDetailsOut"])
    types["ProductFeedDataIn"] = t.struct(
        {
            "isFeedDisabled": t.boolean().optional(),
            "productMatchType": t.string().optional(),
            "productMatchDimensions": t.array(
                t.proxy(renames["ProductMatchDimensionIn"])
            ).optional(),
        }
    ).named(renames["ProductFeedDataIn"])
    types["ProductFeedDataOut"] = t.struct(
        {
            "isFeedDisabled": t.boolean().optional(),
            "productMatchType": t.string().optional(),
            "productMatchDimensions": t.array(
                t.proxy(renames["ProductMatchDimensionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductFeedDataOut"])
    types["GoogleAudienceTargetingSettingIn"] = t.struct(
        {"googleAudienceId": t.string()}
    ).named(renames["GoogleAudienceTargetingSettingIn"])
    types["GoogleAudienceTargetingSettingOut"] = t.struct(
        {
            "googleAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceTargetingSettingOut"])
    types["FrequencyCapIn"] = t.struct(
        {
            "unlimited": t.boolean().optional(),
            "timeUnit": t.string().optional(),
            "timeUnitCount": t.integer().optional(),
            "maxViews": t.integer().optional(),
            "maxImpressions": t.integer().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "unlimited": t.boolean().optional(),
            "timeUnit": t.string().optional(),
            "timeUnitCount": t.integer().optional(),
            "maxViews": t.integer().optional(),
            "maxImpressions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
    types["CommonInStreamAttributeIn"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "actionButtonLabel": t.string().optional(),
            "finalUrl": t.string().optional(),
            "actionHeadline": t.string().optional(),
            "companionBanner": t.proxy(renames["ImageAssetIn"]).optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "displayUrl": t.string().optional(),
        }
    ).named(renames["CommonInStreamAttributeIn"])
    types["CommonInStreamAttributeOut"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "actionButtonLabel": t.string().optional(),
            "finalUrl": t.string().optional(),
            "actionHeadline": t.string().optional(),
            "companionBanner": t.proxy(renames["ImageAssetOut"]).optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "displayUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonInStreamAttributeOut"])
    types["PartnerAdServerConfigIn"] = t.struct(
        {"measurementConfig": t.proxy(renames["MeasurementConfigIn"]).optional()}
    ).named(renames["PartnerAdServerConfigIn"])
    types["PartnerAdServerConfigOut"] = t.struct(
        {
            "measurementConfig": t.proxy(renames["MeasurementConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerAdServerConfigOut"])
    types["CreateAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "targetingType": t.string(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ),
        }
    ).named(renames["CreateAssignedTargetingOptionsRequestIn"])
    types["CreateAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "targetingType": t.string(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAssignedTargetingOptionsRequestOut"])
    types["ReplaceNegativeKeywordsResponseIn"] = t.struct(
        {"negativeKeywords": t.array(t.proxy(renames["NegativeKeywordIn"])).optional()}
    ).named(renames["ReplaceNegativeKeywordsResponseIn"])
    types["ReplaceNegativeKeywordsResponseOut"] = t.struct(
        {
            "negativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceNegativeKeywordsResponseOut"])
    types["PartnerIn"] = t.struct(
        {
            "adServerConfig": t.proxy(renames["PartnerAdServerConfigIn"]).optional(),
            "dataAccessConfig": t.proxy(
                renames["PartnerDataAccessConfigIn"]
            ).optional(),
            "exchangeConfig": t.proxy(renames["ExchangeConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "generalConfig": t.proxy(renames["PartnerGeneralConfigIn"]).optional(),
        }
    ).named(renames["PartnerIn"])
    types["PartnerOut"] = t.struct(
        {
            "adServerConfig": t.proxy(renames["PartnerAdServerConfigOut"]).optional(),
            "entityStatus": t.string().optional(),
            "dataAccessConfig": t.proxy(
                renames["PartnerDataAccessConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "partnerId": t.string().optional(),
            "name": t.string().optional(),
            "exchangeConfig": t.proxy(renames["ExchangeConfigOut"]).optional(),
            "displayName": t.string().optional(),
            "generalConfig": t.proxy(renames["PartnerGeneralConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ContentInstreamPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentInstreamPositionTargetingOptionDetailsIn"])
    types["ContentInstreamPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentInstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentInstreamPositionTargetingOptionDetailsOut"])
    types["ListCustomListsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customLists": t.array(t.proxy(renames["CustomListIn"])).optional(),
        }
    ).named(renames["ListCustomListsResponseIn"])
    types["ListCustomListsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customLists": t.array(t.proxy(renames["CustomListOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomListsResponseOut"])
    types["TargetingOptionIn"] = t.struct(
        {
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionTargetingOptionDetailsIn"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserTargetingOptionDetailsIn"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionTargetingOptionDetailsIn"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentTargetingOptionDetailsIn"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeTargetingOptionDetailsIn"]
            ).optional(),
            "poiDetails": t.proxy(renames["PoiTargetingOptionDetailsIn"]).optional(),
            "languageDetails": t.proxy(
                renames["LanguageTargetingOptionDetailsIn"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionTargetingOptionDetailsIn"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspTargetingOptionDetailsIn"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryTargetingOptionDetailsIn"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeTargetingOptionDetailsIn"]
            ).optional(),
            "omidDetails": t.proxy(renames["OmidTargetingOptionDetailsIn"]).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeTargetingOptionDetailsIn"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryTargetingOptionDetailsIn"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityTargetingOptionDetailsIn"]
            ).optional(),
            "digitalContentLabelDetails": t.proxy(
                renames["DigitalContentLabelTargetingOptionDetailsIn"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreTargetingOptionDetailsIn"]
            ).optional(),
            "sensitiveCategoryDetails": t.proxy(
                renames["SensitiveCategoryTargetingOptionDetailsIn"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeTargetingOptionDetailsIn"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainTargetingOptionDetailsIn"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderTargetingOptionDetailsIn"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeTargetingOptionDetailsIn"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelTargetingOptionDetailsIn"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeTargetingOptionDetailsIn"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionTargetingOptionDetailsIn"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionTargetingOptionDetailsIn"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeTargetingOptionDetailsIn"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusTargetingOptionDetailsIn"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeTargetingOptionDetailsIn"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemTargetingOptionDetailsIn"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationTargetingOptionDetailsIn"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusTargetingOptionDetailsIn"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentTargetingOptionDetailsIn"]
            ).optional(),
        }
    ).named(renames["TargetingOptionIn"])
    types["TargetingOptionOut"] = t.struct(
        {
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionTargetingOptionDetailsOut"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserTargetingOptionDetailsOut"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionTargetingOptionDetailsOut"]
            ).optional(),
            "targetingOptionId": t.string().optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentTargetingOptionDetailsOut"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeTargetingOptionDetailsOut"]
            ).optional(),
            "poiDetails": t.proxy(renames["PoiTargetingOptionDetailsOut"]).optional(),
            "languageDetails": t.proxy(
                renames["LanguageTargetingOptionDetailsOut"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionTargetingOptionDetailsOut"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspTargetingOptionDetailsOut"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryTargetingOptionDetailsOut"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeTargetingOptionDetailsOut"]
            ).optional(),
            "omidDetails": t.proxy(renames["OmidTargetingOptionDetailsOut"]).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeTargetingOptionDetailsOut"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryTargetingOptionDetailsOut"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityTargetingOptionDetailsOut"]
            ).optional(),
            "digitalContentLabelDetails": t.proxy(
                renames["DigitalContentLabelTargetingOptionDetailsOut"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreTargetingOptionDetailsOut"]
            ).optional(),
            "sensitiveCategoryDetails": t.proxy(
                renames["SensitiveCategoryTargetingOptionDetailsOut"]
            ).optional(),
            "targetingType": t.string().optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeTargetingOptionDetailsOut"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainTargetingOptionDetailsOut"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderTargetingOptionDetailsOut"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeTargetingOptionDetailsOut"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelTargetingOptionDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeTargetingOptionDetailsOut"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionTargetingOptionDetailsOut"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionTargetingOptionDetailsOut"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeTargetingOptionDetailsOut"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusTargetingOptionDetailsOut"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeTargetingOptionDetailsOut"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemTargetingOptionDetailsOut"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationTargetingOptionDetailsOut"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusTargetingOptionDetailsOut"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentTargetingOptionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingOptionOut"])
    types["CategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CategoryTargetingOptionDetailsIn"])
    types["CategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryTargetingOptionDetailsOut"])
    types["InventorySourceStatusIn"] = t.struct(
        {
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
        }
    ).named(renames["InventorySourceStatusIn"])
    types["InventorySourceStatusOut"] = t.struct(
        {
            "entityStatus": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "entityPauseReason": t.string().optional(),
            "sellerStatus": t.string().optional(),
            "configStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceStatusOut"])
    types["ActiveViewVideoViewabilityMetricConfigIn"] = t.struct(
        {
            "displayName": t.string(),
            "minimumQuartile": t.string().optional(),
            "minimumViewability": t.string(),
            "minimumDuration": t.string().optional(),
            "minimumVolume": t.string(),
        }
    ).named(renames["ActiveViewVideoViewabilityMetricConfigIn"])
    types["ActiveViewVideoViewabilityMetricConfigOut"] = t.struct(
        {
            "displayName": t.string(),
            "minimumQuartile": t.string().optional(),
            "minimumViewability": t.string(),
            "minimumDuration": t.string().optional(),
            "minimumVolume": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActiveViewVideoViewabilityMetricConfigOut"])
    types["BumperAdIn"] = t.struct(
        {
            "commonInStreamAttribute": t.proxy(
                renames["CommonInStreamAttributeIn"]
            ).optional()
        }
    ).named(renames["BumperAdIn"])
    types["BumperAdOut"] = t.struct(
        {
            "commonInStreamAttribute": t.proxy(
                renames["CommonInStreamAttributeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BumperAdOut"])
    types["EditCustomerMatchMembersResponseIn"] = t.struct(
        {"firstAndThirdPartyAudienceId": t.string()}
    ).named(renames["EditCustomerMatchMembersResponseIn"])
    types["EditCustomerMatchMembersResponseOut"] = t.struct(
        {
            "firstAndThirdPartyAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditCustomerMatchMembersResponseOut"])
    types["VideoDiscoveryAdIn"] = t.struct(
        {
            "description2": t.string().optional(),
            "description1": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "thumbnail": t.string().optional(),
            "headline": t.string().optional(),
        }
    ).named(renames["VideoDiscoveryAdIn"])
    types["VideoDiscoveryAdOut"] = t.struct(
        {
            "description2": t.string().optional(),
            "description1": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "thumbnail": t.string().optional(),
            "headline": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoDiscoveryAdOut"])
    types["BulkEditAssignedUserRolesResponseIn"] = t.struct(
        {
            "createdAssignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleIn"])
            ).optional()
        }
    ).named(renames["BulkEditAssignedUserRolesResponseIn"])
    types["BulkEditAssignedUserRolesResponseOut"] = t.struct(
        {
            "createdAssignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedUserRolesResponseOut"])
    types["GeoRegionSearchTermsIn"] = t.struct(
        {"geoRegionQuery": t.string().optional()}
    ).named(renames["GeoRegionSearchTermsIn"])
    types["GeoRegionSearchTermsOut"] = t.struct(
        {
            "geoRegionQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionSearchTermsOut"])
    types["BulkListAdvertiserAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["BulkListAdvertiserAssignedTargetingOptionsResponseIn"])
    types["BulkListAdvertiserAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"])
    types["AdvertiserGeneralConfigIn"] = t.struct(
        {"domainUrl": t.string(), "currencyCode": t.string()}
    ).named(renames["AdvertiserGeneralConfigIn"])
    types["AdvertiserGeneralConfigOut"] = t.struct(
        {
            "domainUrl": t.string(),
            "currencyCode": t.string(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserGeneralConfigOut"])
    types["BulkUpdateLineItemsRequestIn"] = t.struct(
        {
            "targetLineItem": t.proxy(renames["LineItemIn"]),
            "updateMask": t.string(),
            "lineItemIds": t.array(t.string()),
        }
    ).named(renames["BulkUpdateLineItemsRequestIn"])
    types["BulkUpdateLineItemsRequestOut"] = t.struct(
        {
            "targetLineItem": t.proxy(renames["LineItemOut"]),
            "updateMask": t.string(),
            "lineItemIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkUpdateLineItemsRequestOut"])
    types["KeywordAssignedTargetingOptionDetailsIn"] = t.struct(
        {"keyword": t.string(), "negative": t.boolean().optional()}
    ).named(renames["KeywordAssignedTargetingOptionDetailsIn"])
    types["KeywordAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "keyword": t.string(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeywordAssignedTargetingOptionDetailsOut"])
    types["ListCombinedAudiencesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "combinedAudiences": t.array(
                t.proxy(renames["CombinedAudienceIn"])
            ).optional(),
        }
    ).named(renames["ListCombinedAudiencesResponseIn"])
    types["ListCombinedAudiencesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "combinedAudiences": t.array(
                t.proxy(renames["CombinedAudienceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCombinedAudiencesResponseOut"])
    types["CustomBiddingModelDetailsIn"] = t.struct(
        {"readinessState": t.string().optional(), "advertiserId": t.string().optional()}
    ).named(renames["CustomBiddingModelDetailsIn"])
    types["CustomBiddingModelDetailsOut"] = t.struct(
        {
            "suspensionState": t.string().optional(),
            "readinessState": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingModelDetailsOut"])
    types["ListSitesResponseIn"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSitesResponseIn"])
    types["ListSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSitesResponseOut"])
    types["InvoiceIn"] = t.struct(
        {
            "purchaseOrderNumber": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "invoiceId": t.string().optional(),
            "dueDate": t.proxy(renames["DateIn"]).optional(),
            "budgetInvoiceGroupingId": t.string().optional(),
            "serviceDateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "name": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "displayName": t.string().optional(),
            "subtotalAmountMicros": t.string().optional(),
            "invoiceType": t.string().optional(),
            "correctedInvoiceId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "nonBudgetMicros": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "issueDate": t.proxy(renames["DateIn"]).optional(),
            "budgetSummaries": t.array(t.proxy(renames["BudgetSummaryIn"])).optional(),
            "pdfUrl": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["InvoiceIn"])
    types["InvoiceOut"] = t.struct(
        {
            "purchaseOrderNumber": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "invoiceId": t.string().optional(),
            "dueDate": t.proxy(renames["DateOut"]).optional(),
            "budgetInvoiceGroupingId": t.string().optional(),
            "serviceDateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "name": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "displayName": t.string().optional(),
            "subtotalAmountMicros": t.string().optional(),
            "invoiceType": t.string().optional(),
            "correctedInvoiceId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "nonBudgetMicros": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "issueDate": t.proxy(renames["DateOut"]).optional(),
            "budgetSummaries": t.array(t.proxy(renames["BudgetSummaryOut"])).optional(),
            "pdfUrl": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceOut"])
    types["LocationListIn"] = t.struct(
        {
            "locationType": t.string(),
            "displayName": t.string(),
            "advertiserId": t.string(),
        }
    ).named(renames["LocationListIn"])
    types["LocationListOut"] = t.struct(
        {
            "locationType": t.string(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "advertiserId": t.string(),
            "locationListId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationListOut"])
    types["ListInventorySourcesResponseIn"] = t.struct(
        {
            "inventorySources": t.array(
                t.proxy(renames["InventorySourceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInventorySourcesResponseIn"])
    types["ListInventorySourcesResponseOut"] = t.struct(
        {
            "inventorySources": t.array(
                t.proxy(renames["InventorySourceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInventorySourcesResponseOut"])
    types["DeviceTypeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"deviceType": t.string().optional()}
    ).named(renames["DeviceTypeAssignedTargetingOptionDetailsIn"])
    types["DeviceTypeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "youtubeAndPartnersBidMultiplier": t.number().optional(),
            "deviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTypeAssignedTargetingOptionDetailsOut"])
    types["BulkListInsertionOrderAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseIn"])
    types["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"])
    types["EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"] = t.struct(
        {
            "removedAdvertisers": t.array(t.string()).optional(),
            "addedAdvertisers": t.array(t.string()).optional(),
        }
    ).named(renames["EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"])
    types[
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut"
    ] = t.struct(
        {
            "removedAdvertisers": t.array(t.string()).optional(),
            "addedAdvertisers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut"]
    )
    types["ListCampaignAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["ListCampaignAssignedTargetingOptionsResponseIn"])
    types["ListCampaignAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCampaignAssignedTargetingOptionsResponseOut"])
    types["ThirdPartyUrlIn"] = t.struct(
        {"url": t.string().optional(), "type": t.string().optional()}
    ).named(renames["ThirdPartyUrlIn"])
    types["ThirdPartyUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyUrlOut"])
    types["ListAdvertiserAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAdvertiserAssignedTargetingOptionsResponseIn"])
    types["ListAdvertiserAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAdvertiserAssignedTargetingOptionsResponseOut"])
    types["InventorySourceGroupIn"] = t.struct({"displayName": t.string()}).named(
        renames["InventorySourceGroupIn"]
    )
    types["InventorySourceGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "inventorySourceGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceGroupOut"])
    types["BusinessChainSearchTermsIn"] = t.struct(
        {
            "businessChainQuery": t.string().optional(),
            "regionQuery": t.string().optional(),
        }
    ).named(renames["BusinessChainSearchTermsIn"])
    types["BusinessChainSearchTermsOut"] = t.struct(
        {
            "businessChainQuery": t.string().optional(),
            "regionQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessChainSearchTermsOut"])
    types["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"contentOutstreamPosition": t.string().optional()}
    ).named(renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"])
    types["ContentOutstreamPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "contentOutstreamPosition": t.string().optional(),
            "adType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOutstreamPositionAssignedTargetingOptionDetailsOut"])
    types["SdfDownloadTaskMetadataIn"] = t.struct(
        {
            "version": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["SdfDownloadTaskMetadataIn"])
    types["SdfDownloadTaskMetadataOut"] = t.struct(
        {
            "version": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfDownloadTaskMetadataOut"])
    types["SearchTargetingOptionsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "businessChainSearchTerms": t.proxy(
                renames["BusinessChainSearchTermsIn"]
            ).optional(),
            "geoRegionSearchTerms": t.proxy(
                renames["GeoRegionSearchTermsIn"]
            ).optional(),
            "advertiserId": t.string(),
            "pageToken": t.string().optional(),
            "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
        }
    ).named(renames["SearchTargetingOptionsRequestIn"])
    types["SearchTargetingOptionsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "businessChainSearchTerms": t.proxy(
                renames["BusinessChainSearchTermsOut"]
            ).optional(),
            "geoRegionSearchTerms": t.proxy(
                renames["GeoRegionSearchTermsOut"]
            ).optional(),
            "advertiserId": t.string(),
            "pageToken": t.string().optional(),
            "poiSearchTerms": t.proxy(renames["PoiSearchTermsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTargetingOptionsRequestOut"])
    types["InventorySourceVideoCreativeConfigIn"] = t.struct(
        {"duration": t.string().optional()}
    ).named(renames["InventorySourceVideoCreativeConfigIn"])
    types["InventorySourceVideoCreativeConfigOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceVideoCreativeConfigOut"])
    types["BulkEditAdvertiserAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "createdAssignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional()
        }
    ).named(renames["BulkEditAdvertiserAssignedTargetingOptionsResponseIn"])
    types["BulkEditAdvertiserAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "createdAssignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAdvertiserAssignedTargetingOptionsResponseOut"])
    types["IntegrationDetailsIn"] = t.struct(
        {"details": t.string().optional(), "integrationCode": t.string().optional()}
    ).named(renames["IntegrationDetailsIn"])
    types["IntegrationDetailsOut"] = t.struct(
        {
            "details": t.string().optional(),
            "integrationCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegrationDetailsOut"])
    types["InventorySourceGroupAssignedTargetingOptionDetailsIn"] = t.struct(
        {"inventorySourceGroupId": t.string()}
    ).named(renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"])
    types["InventorySourceGroupAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "inventorySourceGroupId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceGroupAssignedTargetingOptionDetailsOut"])
    types["MoneyIn"] = t.struct(
        {
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["ContentStreamTypeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"])
    types["ContentStreamTypeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "contentStreamType": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentStreamTypeAssignedTargetingOptionDetailsOut"])
    types["BiddingStrategyIn"] = t.struct(
        {
            "maximizeSpendAutoBid": t.proxy(
                renames["MaximizeSpendBidStrategyIn"]
            ).optional(),
            "fixedBid": t.proxy(renames["FixedBidStrategyIn"]).optional(),
            "performanceGoalAutoBid": t.proxy(
                renames["PerformanceGoalBidStrategyIn"]
            ).optional(),
        }
    ).named(renames["BiddingStrategyIn"])
    types["BiddingStrategyOut"] = t.struct(
        {
            "maximizeSpendAutoBid": t.proxy(
                renames["MaximizeSpendBidStrategyOut"]
            ).optional(),
            "fixedBid": t.proxy(renames["FixedBidStrategyOut"]).optional(),
            "performanceGoalAutoBid": t.proxy(
                renames["PerformanceGoalBidStrategyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiddingStrategyOut"])
    types["ContentGenreAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["ContentGenreAssignedTargetingOptionDetailsIn"])
    types["ContentGenreAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentGenreAssignedTargetingOptionDetailsOut"])
    types["CampaignIn"] = t.struct(
        {
            "entityStatus": t.string(),
            "campaignBudgets": t.array(t.proxy(renames["CampaignBudgetIn"])).optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "displayName": t.string(),
            "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
            "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
        }
    ).named(renames["CampaignIn"])
    types["CampaignOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "entityStatus": t.string(),
            "campaignBudgets": t.array(
                t.proxy(renames["CampaignBudgetOut"])
            ).optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "advertiserId": t.string().optional(),
            "campaignId": t.string().optional(),
            "displayName": t.string(),
            "campaignGoal": t.proxy(renames["CampaignGoalOut"]),
            "campaignFlight": t.proxy(renames["CampaignFlightOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignOut"])
    types["InsertionOrderBudgetIn"] = t.struct(
        {
            "budgetUnit": t.string(),
            "automationType": t.string().optional(),
            "budgetSegments": t.array(
                t.proxy(renames["InsertionOrderBudgetSegmentIn"])
            ),
        }
    ).named(renames["InsertionOrderBudgetIn"])
    types["InsertionOrderBudgetOut"] = t.struct(
        {
            "budgetUnit": t.string(),
            "automationType": t.string().optional(),
            "budgetSegments": t.array(
                t.proxy(renames["InsertionOrderBudgetSegmentOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderBudgetOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["HouseholdIncomeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"householdIncome": t.string().optional()}
    ).named(renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"])
    types["HouseholdIncomeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "householdIncome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HouseholdIncomeAssignedTargetingOptionDetailsOut"])
    types["AudioVideoOffsetIn"] = t.struct(
        {"percentage": t.string().optional(), "seconds": t.string().optional()}
    ).named(renames["AudioVideoOffsetIn"])
    types["AudioVideoOffsetOut"] = t.struct(
        {
            "percentage": t.string().optional(),
            "seconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioVideoOffsetOut"])
    types["VideoAdSequenceSettingsIn"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["VideoAdSequenceStepIn"])).optional(),
            "minimumDuration": t.string().optional(),
        }
    ).named(renames["VideoAdSequenceSettingsIn"])
    types["VideoAdSequenceSettingsOut"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["VideoAdSequenceStepOut"])).optional(),
            "minimumDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAdSequenceSettingsOut"])
    types["DateRangeIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
    types["SubExchangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SubExchangeTargetingOptionDetailsIn"])
    types["SubExchangeTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubExchangeTargetingOptionDetailsOut"])
    types["AdvertiserIn"] = t.struct(
        {
            "entityStatus": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
            "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
            "partnerId": t.string(),
            "dataAccessConfig": t.proxy(
                renames["AdvertiserDataAccessConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "billingConfig": t.proxy(renames["AdvertiserBillingConfigIn"]).optional(),
            "servingConfig": t.proxy(renames["AdvertiserTargetingConfigIn"]).optional(),
            "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
            "prismaEnabled": t.boolean().optional(),
        }
    ).named(renames["AdvertiserIn"])
    types["AdvertiserOut"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "name": t.string().optional(),
            "entityStatus": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigOut"]),
            "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigOut"]),
            "partnerId": t.string(),
            "dataAccessConfig": t.proxy(
                renames["AdvertiserDataAccessConfigOut"]
            ).optional(),
            "displayName": t.string(),
            "billingConfig": t.proxy(renames["AdvertiserBillingConfigOut"]).optional(),
            "servingConfig": t.proxy(
                renames["AdvertiserTargetingConfigOut"]
            ).optional(),
            "generalConfig": t.proxy(renames["AdvertiserGeneralConfigOut"]),
            "updateTime": t.string().optional(),
            "prismaEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserOut"])
    types["AssignedTargetingOptionIn"] = t.struct(
        {
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "sensitiveCategoryExclusionDetails": t.proxy(
                renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "proximityLocationListDetails": t.proxy(
                renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "omidDetails": t.proxy(
                renames["OmidAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "dayAndTimeDetails": t.proxy(
                renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "regionalLocationListDetails": t.proxy(
                renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "sessionPositionDetails": t.proxy(
                renames["SessionPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "appDetails": t.proxy(
                renames["AppAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "youtubeVideoDetails": t.proxy(
                renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "digitalContentLabelExclusionDetails": t.proxy(
                renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "youtubeChannelDetails": t.proxy(
                renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "keywordDetails": t.proxy(
                renames["KeywordAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "poiDetails": t.proxy(
                renames["PoiAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "channelDetails": t.proxy(
                renames["ChannelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "inventorySourceDetails": t.proxy(
                renames["InventorySourceAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "negativeKeywordListDetails": t.proxy(
                renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "inventorySourceGroupDetails": t.proxy(
                renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "urlDetails": t.proxy(
                renames["UrlAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "audienceGroupDetails": t.proxy(
                renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "thirdPartyVerifierDetails": t.proxy(
                renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
        }
    ).named(renames["AssignedTargetingOptionIn"])
    types["AssignedTargetingOptionOut"] = t.struct(
        {
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "sensitiveCategoryExclusionDetails": t.proxy(
                renames["SensitiveCategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "proximityLocationListDetails": t.proxy(
                renames["ProximityLocationListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "omidDetails": t.proxy(
                renames["OmidAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "dayAndTimeDetails": t.proxy(
                renames["DayAndTimeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "regionalLocationListDetails": t.proxy(
                renames["RegionalLocationListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "sessionPositionDetails": t.proxy(
                renames["SessionPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "appDetails": t.proxy(
                renames["AppAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inheritance": t.string().optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "youtubeVideoDetails": t.proxy(
                renames["YoutubeVideoAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "digitalContentLabelExclusionDetails": t.proxy(
                renames["DigitalContentLabelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "youtubeChannelDetails": t.proxy(
                renames["YoutubeChannelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "keywordDetails": t.proxy(
                renames["KeywordAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "poiDetails": t.proxy(
                renames["PoiAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "channelDetails": t.proxy(
                renames["ChannelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inventorySourceDetails": t.proxy(
                renames["InventorySourceAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "targetingType": t.string().optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "negativeKeywordListDetails": t.proxy(
                renames["NegativeKeywordListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inventorySourceGroupDetails": t.proxy(
                renames["InventorySourceGroupAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "assignedTargetingOptionIdAlias": t.string().optional(),
            "urlDetails": t.proxy(
                renames["UrlAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "audienceGroupDetails": t.proxy(
                renames["AudienceGroupAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "assignedTargetingOptionId": t.string().optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "thirdPartyVerifierDetails": t.proxy(
                renames["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedTargetingOptionOut"])
    types["CreateAssetRequestIn"] = t.struct({"filename": t.string()}).named(
        renames["CreateAssetRequestIn"]
    )
    types["CreateAssetRequestOut"] = t.struct(
        {"filename": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateAssetRequestOut"])
    types["CarrierAndIspAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["CarrierAndIspAssignedTargetingOptionDetailsIn"])
    types["CarrierAndIspAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarrierAndIspAssignedTargetingOptionDetailsOut"])
    types["ViewabilityAssignedTargetingOptionDetailsIn"] = t.struct(
        {"viewability": t.string().optional()}
    ).named(renames["ViewabilityAssignedTargetingOptionDetailsIn"])
    types["ViewabilityAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "viewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewabilityAssignedTargetingOptionDetailsOut"])
    types["FixedBidStrategyIn"] = t.struct(
        {"bidAmountMicros": t.string().optional()}
    ).named(renames["FixedBidStrategyIn"])
    types["FixedBidStrategyOut"] = t.struct(
        {
            "bidAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixedBidStrategyOut"])
    types["IntegralAdScienceIn"] = t.struct(
        {
            "customSegmentId": t.array(t.string()).optional(),
            "excludeUnrateable": t.boolean().optional(),
            "displayViewability": t.string().optional(),
            "excludedAlcoholRisk": t.string().optional(),
            "excludedGamblingRisk": t.string().optional(),
            "excludedAdultRisk": t.string().optional(),
            "excludedOffensiveLanguageRisk": t.string().optional(),
            "traqScoreOption": t.string().optional(),
            "excludedIllegalDownloadsRisk": t.string().optional(),
            "excludedDrugsRisk": t.string().optional(),
            "excludedViolenceRisk": t.string().optional(),
            "excludedAdFraudRisk": t.string().optional(),
            "videoViewability": t.string().optional(),
            "excludedHateSpeechRisk": t.string().optional(),
        }
    ).named(renames["IntegralAdScienceIn"])
    types["IntegralAdScienceOut"] = t.struct(
        {
            "customSegmentId": t.array(t.string()).optional(),
            "excludeUnrateable": t.boolean().optional(),
            "displayViewability": t.string().optional(),
            "excludedAlcoholRisk": t.string().optional(),
            "excludedGamblingRisk": t.string().optional(),
            "excludedAdultRisk": t.string().optional(),
            "excludedOffensiveLanguageRisk": t.string().optional(),
            "traqScoreOption": t.string().optional(),
            "excludedIllegalDownloadsRisk": t.string().optional(),
            "excludedDrugsRisk": t.string().optional(),
            "excludedViolenceRisk": t.string().optional(),
            "excludedAdFraudRisk": t.string().optional(),
            "videoViewability": t.string().optional(),
            "excludedHateSpeechRisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegralAdScienceOut"])
    types["LineItemIn"] = t.struct(
        {
            "flight": t.proxy(renames["LineItemFlightIn"]),
            "entityStatus": t.string(),
            "budget": t.proxy(renames["LineItemBudgetIn"]),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
            "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "conversionCounting": t.proxy(
                renames["ConversionCountingConfigIn"]
            ).optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigIn"]
            ).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "displayName": t.string(),
            "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
            "excludeNewExchanges": t.boolean().optional(),
            "creativeIds": t.array(t.string()).optional(),
            "insertionOrderId": t.string(),
            "pacing": t.proxy(renames["PacingIn"]),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
            "lineItemType": t.string(),
        }
    ).named(renames["LineItemIn"])
    types["LineItemOut"] = t.struct(
        {
            "flight": t.proxy(renames["LineItemFlightOut"]),
            "entityStatus": t.string(),
            "name": t.string().optional(),
            "budget": t.proxy(renames["LineItemBudgetOut"]),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostOut"])).optional(),
            "advertiserId": t.string().optional(),
            "bidStrategy": t.proxy(renames["BiddingStrategyOut"]),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "updateTime": t.string().optional(),
            "campaignId": t.string().optional(),
            "reservationType": t.string().optional(),
            "conversionCounting": t.proxy(
                renames["ConversionCountingConfigOut"]
            ).optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigOut"]
            ).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "displayName": t.string(),
            "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelOut"]),
            "excludeNewExchanges": t.boolean().optional(),
            "creativeIds": t.array(t.string()).optional(),
            "insertionOrderId": t.string(),
            "pacing": t.proxy(renames["PacingOut"]),
            "youtubeAndPartnersSettings": t.proxy(
                renames["YoutubeAndPartnersSettingsOut"]
            ).optional(),
            "lineItemId": t.string().optional(),
            "warningMessages": t.array(t.string()).optional(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "lineItemType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemOut"])
    types["ListAssignedInventorySourcesResponseIn"] = t.struct(
        {
            "assignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssignedInventorySourcesResponseIn"])
    types["ListAssignedInventorySourcesResponseOut"] = t.struct(
        {
            "assignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssignedInventorySourcesResponseOut"])
    types["DoubleVerifyIn"] = t.struct(
        {
            "displayViewability": t.proxy(
                renames["DoubleVerifyDisplayViewabilityIn"]
            ).optional(),
            "appStarRating": t.proxy(renames["DoubleVerifyAppStarRatingIn"]).optional(),
            "avoidedAgeRatings": t.array(t.string()).optional(),
            "fraudInvalidTraffic": t.proxy(
                renames["DoubleVerifyFraudInvalidTrafficIn"]
            ).optional(),
            "videoViewability": t.proxy(
                renames["DoubleVerifyVideoViewabilityIn"]
            ).optional(),
            "customSegmentId": t.string().optional(),
            "brandSafetyCategories": t.proxy(
                renames["DoubleVerifyBrandSafetyCategoriesIn"]
            ).optional(),
        }
    ).named(renames["DoubleVerifyIn"])
    types["DoubleVerifyOut"] = t.struct(
        {
            "displayViewability": t.proxy(
                renames["DoubleVerifyDisplayViewabilityOut"]
            ).optional(),
            "appStarRating": t.proxy(
                renames["DoubleVerifyAppStarRatingOut"]
            ).optional(),
            "avoidedAgeRatings": t.array(t.string()).optional(),
            "fraudInvalidTraffic": t.proxy(
                renames["DoubleVerifyFraudInvalidTrafficOut"]
            ).optional(),
            "videoViewability": t.proxy(
                renames["DoubleVerifyVideoViewabilityOut"]
            ).optional(),
            "customSegmentId": t.string().optional(),
            "brandSafetyCategories": t.proxy(
                renames["DoubleVerifyBrandSafetyCategoriesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyOut"])
    types["ThirdPartyOnlyConfigIn"] = t.struct(
        {"pixelOrderIdReportingEnabled": t.boolean().optional()}
    ).named(renames["ThirdPartyOnlyConfigIn"])
    types["ThirdPartyOnlyConfigOut"] = t.struct(
        {
            "pixelOrderIdReportingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyOnlyConfigOut"])
    types["SiteIn"] = t.struct({"urlOrAppId": t.string()}).named(renames["SiteIn"])
    types["SiteOut"] = t.struct(
        {
            "name": t.string().optional(),
            "urlOrAppId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteOut"])
    types["ConversionCountingConfigIn"] = t.struct(
        {
            "postViewCountPercentageMillis": t.string().optional(),
            "floodlightActivityConfigs": t.array(
                t.proxy(renames["TrackingFloodlightActivityConfigIn"])
            ).optional(),
        }
    ).named(renames["ConversionCountingConfigIn"])
    types["ConversionCountingConfigOut"] = t.struct(
        {
            "postViewCountPercentageMillis": t.string().optional(),
            "floodlightActivityConfigs": t.array(
                t.proxy(renames["TrackingFloodlightActivityConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionCountingConfigOut"])
    types["CombinedAudienceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CombinedAudienceIn"]
    )
    types["CombinedAudienceOut"] = t.struct(
        {
            "combinedAudienceId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CombinedAudienceOut"])
    types["ReviewStatusInfoIn"] = t.struct(
        {
            "approvalStatus": t.string().optional(),
            "creativeAndLandingPageReviewStatus": t.string().optional(),
            "contentAndPolicyReviewStatus": t.string().optional(),
            "publisherReviewStatuses": t.array(
                t.proxy(renames["PublisherReviewStatusIn"])
            ).optional(),
            "exchangeReviewStatuses": t.array(
                t.proxy(renames["ExchangeReviewStatusIn"])
            ).optional(),
        }
    ).named(renames["ReviewStatusInfoIn"])
    types["ReviewStatusInfoOut"] = t.struct(
        {
            "approvalStatus": t.string().optional(),
            "creativeAndLandingPageReviewStatus": t.string().optional(),
            "contentAndPolicyReviewStatus": t.string().optional(),
            "publisherReviewStatuses": t.array(
                t.proxy(renames["PublisherReviewStatusOut"])
            ).optional(),
            "exchangeReviewStatuses": t.array(
                t.proxy(renames["ExchangeReviewStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewStatusInfoOut"])
    types["AppCategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["AppCategoryAssignedTargetingOptionDetailsIn"])
    types["AppCategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppCategoryAssignedTargetingOptionDetailsOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["TimeRangeIn"] = t.struct(
        {"startTime": t.string(), "endTime": t.string()}
    ).named(renames["TimeRangeIn"])
    types["TimeRangeOut"] = t.struct(
        {
            "startTime": t.string(),
            "endTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeRangeOut"])
    types["ListInsertionOrderAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["ListInsertionOrderAssignedTargetingOptionsResponseIn"])
    types["ListInsertionOrderAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInsertionOrderAssignedTargetingOptionsResponseOut"])
    types["ThirdPartyVendorConfigIn"] = t.struct(
        {"placementId": t.string().optional(), "vendor": t.string().optional()}
    ).named(renames["ThirdPartyVendorConfigIn"])
    types["ThirdPartyVendorConfigOut"] = t.struct(
        {
            "placementId": t.string().optional(),
            "vendor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyVendorConfigOut"])
    types["AppCategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppCategoryTargetingOptionDetailsIn"])
    types["AppCategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppCategoryTargetingOptionDetailsOut"])
    types["ListNegativeKeywordsResponseIn"] = t.struct(
        {
            "negativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNegativeKeywordsResponseIn"])
    types["ListNegativeKeywordsResponseOut"] = t.struct(
        {
            "negativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNegativeKeywordsResponseOut"])
    types["BulkEditSitesRequestIn"] = t.struct(
        {
            "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
            "deletedSites": t.array(t.string()).optional(),
        }
    ).named(renames["BulkEditSitesRequestIn"])
    types["BulkEditSitesRequestOut"] = t.struct(
        {
            "createdSites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
            "deletedSites": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditSitesRequestOut"])
    types["SubExchangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["SubExchangeAssignedTargetingOptionDetailsIn"])
    types["SubExchangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubExchangeAssignedTargetingOptionDetailsOut"])
    types["FirstAndThirdPartyAudienceTargetingSettingIn"] = t.struct(
        {"firstAndThirdPartyAudienceId": t.string(), "recency": t.string().optional()}
    ).named(renames["FirstAndThirdPartyAudienceTargetingSettingIn"])
    types["FirstAndThirdPartyAudienceTargetingSettingOut"] = t.struct(
        {
            "firstAndThirdPartyAudienceId": t.string(),
            "recency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceTargetingSettingOut"])
    types["CustomBiddingAlgorithmIn"] = t.struct(
        {
            "customBiddingAlgorithmType": t.string(),
            "advertiserId": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "partnerId": t.string().optional(),
            "entityStatus": t.string().optional(),
        }
    ).named(renames["CustomBiddingAlgorithmIn"])
    types["CustomBiddingAlgorithmOut"] = t.struct(
        {
            "name": t.string().optional(),
            "customBiddingAlgorithmType": t.string(),
            "advertiserId": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "modelDetails": t.array(
                t.proxy(renames["CustomBiddingModelDetailsOut"])
            ).optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "displayName": t.string(),
            "partnerId": t.string().optional(),
            "entityStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingAlgorithmOut"])
    types["DuplicateLineItemResponseIn"] = t.struct(
        {"duplicateLineItemId": t.string().optional()}
    ).named(renames["DuplicateLineItemResponseIn"])
    types["DuplicateLineItemResponseOut"] = t.struct(
        {
            "duplicateLineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateLineItemResponseOut"])
    types["ActivateManualTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivateManualTriggerRequestIn"])
    types["ActivateManualTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateManualTriggerRequestOut"])
    types["AgeRangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"ageRange": t.string().optional()}
    ).named(renames["AgeRangeAssignedTargetingOptionDetailsIn"])
    types["AgeRangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeAssignedTargetingOptionDetailsOut"])
    types["ListGuaranteedOrdersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "guaranteedOrders": t.array(
                t.proxy(renames["GuaranteedOrderIn"])
            ).optional(),
        }
    ).named(renames["ListGuaranteedOrdersResponseIn"])
    types["ListGuaranteedOrdersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "guaranteedOrders": t.array(
                t.proxy(renames["GuaranteedOrderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGuaranteedOrdersResponseOut"])
    types["OnScreenPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OnScreenPositionTargetingOptionDetailsIn"])
    types["OnScreenPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "onScreenPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnScreenPositionTargetingOptionDetailsOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ListInsertionOrdersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "insertionOrders": t.array(t.proxy(renames["InsertionOrderIn"])).optional(),
        }
    ).named(renames["ListInsertionOrdersResponseIn"])
    types["ListInsertionOrdersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "insertionOrders": t.array(
                t.proxy(renames["InsertionOrderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInsertionOrdersResponseOut"])
    types["BulkListAdGroupAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "youtubeAdGroupAssignedTargetingOptions": t.array(
                t.proxy(renames["YoutubeAdGroupAssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["BulkListAdGroupAssignedTargetingOptionsResponseIn"])
    types["BulkListAdGroupAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "youtubeAdGroupAssignedTargetingOptions": t.array(
                t.proxy(renames["YoutubeAdGroupAssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListAdGroupAssignedTargetingOptionsResponseOut"])
    types["SensitiveCategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"excludedSensitiveCategory": t.string()}
    ).named(renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"])
    types["SensitiveCategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "excludedSensitiveCategory": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveCategoryAssignedTargetingOptionDetailsOut"])
    types["BulkEditAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "lineItemIds": t.array(t.string()),
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
            ).optional(),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
            ).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsRequestIn"])
    types["BulkEditAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "lineItemIds": t.array(t.string()),
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsRequestOut"])
    types["MobileAppIn"] = t.struct({"appId": t.string()}).named(renames["MobileAppIn"])
    types["MobileAppOut"] = t.struct(
        {
            "platform": t.string().optional(),
            "publisher": t.string().optional(),
            "appId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileAppOut"])
    types["GenderTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenderTargetingOptionDetailsIn"])
    types["GenderTargetingOptionDetailsOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderTargetingOptionDetailsOut"])
    types["ObaIconIn"] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "clickTrackingUrl": t.string(),
            "position": t.string().optional(),
            "landingPageUrl": t.string(),
            "viewTrackingUrl": t.string(),
            "program": t.string().optional(),
            "resourceMimeType": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]).optional(),
        }
    ).named(renames["ObaIconIn"])
    types["ObaIconOut"] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "clickTrackingUrl": t.string(),
            "position": t.string().optional(),
            "landingPageUrl": t.string(),
            "viewTrackingUrl": t.string(),
            "program": t.string().optional(),
            "resourceMimeType": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObaIconOut"])
    types["ContentStreamTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentStreamTypeTargetingOptionDetailsIn"])
    types["ContentStreamTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "contentStreamType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentStreamTypeTargetingOptionDetailsOut"])
    types["DigitalContentLabelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"excludedContentRatingTier": t.string()}
    ).named(renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"])
    types["DigitalContentLabelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "excludedContentRatingTier": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigitalContentLabelAssignedTargetingOptionDetailsOut"])
    types["DeleteAssignedTargetingOptionsRequestIn"] = t.struct(
        {"assignedTargetingOptionIds": t.array(t.string()), "targetingType": t.string()}
    ).named(renames["DeleteAssignedTargetingOptionsRequestIn"])
    types["DeleteAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "assignedTargetingOptionIds": t.array(t.string()),
            "targetingType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteAssignedTargetingOptionsRequestOut"])
    types["SearchTargetingOptionsResponseIn"] = t.struct(
        {
            "targetingOptions": t.array(
                t.proxy(renames["TargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchTargetingOptionsResponseIn"])
    types["SearchTargetingOptionsResponseOut"] = t.struct(
        {
            "targetingOptions": t.array(
                t.proxy(renames["TargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTargetingOptionsResponseOut"])
    types["AdvertiserTargetingConfigIn"] = t.struct(
        {"exemptTvFromViewabilityTargeting": t.boolean().optional()}
    ).named(renames["AdvertiserTargetingConfigIn"])
    types["AdvertiserTargetingConfigOut"] = t.struct(
        {
            "exemptTvFromViewabilityTargeting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserTargetingConfigOut"])
    types["CustomLabelIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["CustomLabelIn"])
    types["CustomLabelOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomLabelOut"])
    types["AudioContentTypeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"audioContentType": t.string().optional()}
    ).named(renames["AudioContentTypeAssignedTargetingOptionDetailsIn"])
    types["AudioContentTypeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "audioContentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioContentTypeAssignedTargetingOptionDetailsOut"])
    types["PartnerDataAccessConfigIn"] = t.struct(
        {"sdfConfig": t.proxy(renames["SdfConfigIn"]).optional()}
    ).named(renames["PartnerDataAccessConfigIn"])
    types["PartnerDataAccessConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["SdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerDataAccessConfigOut"])
    types["ContentDurationTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentDurationTargetingOptionDetailsIn"])
    types["ContentDurationTargetingOptionDetailsOut"] = t.struct(
        {
            "contentDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentDurationTargetingOptionDetailsOut"])
    types["InventorySourceDisplayCreativeConfigIn"] = t.struct(
        {"creativeSize": t.proxy(renames["DimensionsIn"]).optional()}
    ).named(renames["InventorySourceDisplayCreativeConfigIn"])
    types["InventorySourceDisplayCreativeConfigOut"] = t.struct(
        {
            "creativeSize": t.proxy(renames["DimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceDisplayCreativeConfigOut"])
    types["AdvertiserDataAccessConfigIn"] = t.struct(
        {"sdfConfig": t.proxy(renames["AdvertiserSdfConfigIn"]).optional()}
    ).named(renames["AdvertiserDataAccessConfigIn"])
    types["AdvertiserDataAccessConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["AdvertiserSdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserDataAccessConfigOut"])
    types["SessionPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"sessionPosition": t.string().optional()}
    ).named(renames["SessionPositionAssignedTargetingOptionDetailsIn"])
    types["SessionPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "sessionPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionPositionAssignedTargetingOptionDetailsOut"])
    types["ListInventorySourceGroupsResponseIn"] = t.struct(
        {
            "inventorySourceGroups": t.array(
                t.proxy(renames["InventorySourceGroupIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInventorySourceGroupsResponseIn"])
    types["ListInventorySourceGroupsResponseOut"] = t.struct(
        {
            "inventorySourceGroups": t.array(
                t.proxy(renames["InventorySourceGroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInventorySourceGroupsResponseOut"])
    types["MobileDeviceIdListIn"] = t.struct(
        {"mobileDeviceIds": t.array(t.string()).optional()}
    ).named(renames["MobileDeviceIdListIn"])
    types["MobileDeviceIdListOut"] = t.struct(
        {
            "mobileDeviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileDeviceIdListOut"])
    types["CategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["CategoryAssignedTargetingOptionDetailsIn"])
    types["CategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryAssignedTargetingOptionDetailsOut"])
    types["MeasurementConfigIn"] = t.struct(
        {
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
        }
    ).named(renames["MeasurementConfigIn"])
    types["MeasurementConfigOut"] = t.struct(
        {
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeasurementConfigOut"])
    types["AssignedUserRoleIn"] = t.struct(
        {
            "userRole": t.string(),
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
        }
    ).named(renames["AssignedUserRoleIn"])
    types["AssignedUserRoleOut"] = t.struct(
        {
            "assignedUserRoleId": t.string().optional(),
            "userRole": t.string(),
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedUserRoleOut"])
    types["BrowserTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["BrowserTargetingOptionDetailsIn"])
    types["BrowserTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserTargetingOptionDetailsOut"])
    types["ListGoogleAudiencesResponseIn"] = t.struct(
        {
            "googleAudiences": t.array(t.proxy(renames["GoogleAudienceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGoogleAudiencesResponseIn"])
    types["ListGoogleAudiencesResponseOut"] = t.struct(
        {
            "googleAudiences": t.array(
                t.proxy(renames["GoogleAudienceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGoogleAudiencesResponseOut"])
    types["GeoRegionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GeoRegionTargetingOptionDetailsIn"])
    types["GeoRegionTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "geoRegionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionTargetingOptionDetailsOut"])
    types["InventorySourceAssignedTargetingOptionDetailsIn"] = t.struct(
        {"inventorySourceId": t.string()}
    ).named(renames["InventorySourceAssignedTargetingOptionDetailsIn"])
    types["InventorySourceAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "inventorySourceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAssignedTargetingOptionDetailsOut"])
    types["ListCustomBiddingAlgorithmsResponseIn"] = t.struct(
        {
            "customBiddingAlgorithms": t.array(
                t.proxy(renames["CustomBiddingAlgorithmIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCustomBiddingAlgorithmsResponseIn"])
    types["ListCustomBiddingAlgorithmsResponseOut"] = t.struct(
        {
            "customBiddingAlgorithms": t.array(
                t.proxy(renames["CustomBiddingAlgorithmOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomBiddingAlgorithmsResponseOut"])
    types["VideoPlayerSizeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VideoPlayerSizeTargetingOptionDetailsIn"])
    types["VideoPlayerSizeTargetingOptionDetailsOut"] = t.struct(
        {
            "videoPlayerSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerSizeTargetingOptionDetailsOut"])
    types["EditCustomerMatchMembersRequestIn"] = t.struct(
        {
            "addedContactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
            "addedMobileDeviceIdList": t.proxy(
                renames["MobileDeviceIdListIn"]
            ).optional(),
            "advertiserId": t.string(),
        }
    ).named(renames["EditCustomerMatchMembersRequestIn"])
    types["EditCustomerMatchMembersRequestOut"] = t.struct(
        {
            "addedContactInfoList": t.proxy(renames["ContactInfoListOut"]).optional(),
            "addedMobileDeviceIdList": t.proxy(
                renames["MobileDeviceIdListOut"]
            ).optional(),
            "advertiserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditCustomerMatchMembersRequestOut"])
    types["LanguageAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["LanguageAssignedTargetingOptionDetailsIn"])
    types["LanguageAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageAssignedTargetingOptionDetailsOut"])
    types["ImageAssetIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "fileSize": t.string().optional(),
            "fullSize": t.proxy(renames["DimensionsIn"]).optional(),
        }
    ).named(renames["ImageAssetIn"])
    types["ImageAssetOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "fileSize": t.string().optional(),
            "fullSize": t.proxy(renames["DimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageAssetOut"])
    types["DisplayVideoSourceAdIn"] = t.struct(
        {"creativeId": t.string().optional()}
    ).named(renames["DisplayVideoSourceAdIn"])
    types["DisplayVideoSourceAdOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayVideoSourceAdOut"])
    types["LookbackWindowIn"] = t.struct(
        {"impressionDays": t.integer().optional(), "clickDays": t.integer().optional()}
    ).named(renames["LookbackWindowIn"])
    types["LookbackWindowOut"] = t.struct(
        {
            "impressionDays": t.integer().optional(),
            "clickDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookbackWindowOut"])
    types["PoiAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "proximityRadiusAmount": t.number(),
            "proximityRadiusUnit": t.string(),
        }
    ).named(renames["PoiAssignedTargetingOptionDetailsIn"])
    types["PoiAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "longitude": t.number().optional(),
            "proximityRadiusAmount": t.number(),
            "proximityRadiusUnit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiAssignedTargetingOptionDetailsOut"])
    types["YoutubeAdGroupAssignedTargetingOptionIn"] = t.struct(
        {
            "youtubeAdGroupId": t.string().optional(),
            "assignedTargetingOption": t.proxy(
                renames["AssignedTargetingOptionIn"]
            ).optional(),
        }
    ).named(renames["YoutubeAdGroupAssignedTargetingOptionIn"])
    types["YoutubeAdGroupAssignedTargetingOptionOut"] = t.struct(
        {
            "youtubeAdGroupId": t.string().optional(),
            "assignedTargetingOption": t.proxy(
                renames["AssignedTargetingOptionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupAssignedTargetingOptionOut"])
    types["OperatingSystemTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OperatingSystemTargetingOptionDetailsIn"])
    types["OperatingSystemTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemTargetingOptionDetailsOut"])
    types["AssetAssociationIn"] = t.struct(
        {"asset": t.proxy(renames["AssetIn"]).optional(), "role": t.string().optional()}
    ).named(renames["AssetAssociationIn"])
    types["AssetAssociationOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetAssociationOut"])
    types["GenerateDefaultLineItemRequestIn"] = t.struct(
        {
            "insertionOrderId": t.string(),
            "displayName": t.string(),
            "lineItemType": t.string(),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
        }
    ).named(renames["GenerateDefaultLineItemRequestIn"])
    types["GenerateDefaultLineItemRequestOut"] = t.struct(
        {
            "insertionOrderId": t.string(),
            "displayName": t.string(),
            "lineItemType": t.string(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateDefaultLineItemRequestOut"])
    types["GoogleBytestreamMediaIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["GoogleBytestreamMediaIn"])
    types["GoogleBytestreamMediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleBytestreamMediaOut"])
    types["BulkEditAssignedLocationsResponseIn"] = t.struct(
        {
            "assignedLocations": t.array(
                t.proxy(renames["AssignedLocationIn"])
            ).optional()
        }
    ).named(renames["BulkEditAssignedLocationsResponseIn"])
    types["BulkEditAssignedLocationsResponseOut"] = t.struct(
        {
            "assignedLocations": t.array(
                t.proxy(renames["AssignedLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedLocationsResponseOut"])
    types["ListLineItemsResponseIn"] = t.struct(
        {
            "lineItems": t.array(t.proxy(renames["LineItemIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLineItemsResponseIn"])
    types["ListLineItemsResponseOut"] = t.struct(
        {
            "lineItems": t.array(t.proxy(renames["LineItemOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLineItemsResponseOut"])
    types["ListUsersResponseIn"] = t.struct(
        {
            "users": t.array(t.proxy(renames["UserIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUsersResponseIn"])
    types["ListUsersResponseOut"] = t.struct(
        {
            "users": t.array(t.proxy(renames["UserOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsersResponseOut"])
    types["CampaignFlightIn"] = t.struct(
        {
            "plannedSpendAmountMicros": t.string().optional(),
            "plannedDates": t.proxy(renames["DateRangeIn"]),
        }
    ).named(renames["CampaignFlightIn"])
    types["CampaignFlightOut"] = t.struct(
        {
            "plannedSpendAmountMicros": t.string().optional(),
            "plannedDates": t.proxy(renames["DateRangeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignFlightOut"])
    types["EditGuaranteedOrderReadAccessorsRequestIn"] = t.struct(
        {
            "partnerId": t.string(),
            "removedAdvertisers": t.array(t.string()).optional(),
            "addedAdvertisers": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsRequestIn"])
    types["EditGuaranteedOrderReadAccessorsRequestOut"] = t.struct(
        {
            "partnerId": t.string(),
            "removedAdvertisers": t.array(t.string()).optional(),
            "addedAdvertisers": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsRequestOut"])
    types["BulkEditPartnerAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "createdAssignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional()
        }
    ).named(renames["BulkEditPartnerAssignedTargetingOptionsResponseIn"])
    types["BulkEditPartnerAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "createdAssignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditPartnerAssignedTargetingOptionsResponseOut"])
    types["ViewabilityTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ViewabilityTargetingOptionDetailsIn"])
    types["ViewabilityTargetingOptionDetailsOut"] = t.struct(
        {
            "viewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewabilityTargetingOptionDetailsOut"])
    types["CustomListTargetingSettingIn"] = t.struct(
        {"customListId": t.string()}
    ).named(renames["CustomListTargetingSettingIn"])
    types["CustomListTargetingSettingOut"] = t.struct(
        {
            "customListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListTargetingSettingOut"])
    types["DeactivateManualTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateManualTriggerRequestIn"])
    types["DeactivateManualTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateManualTriggerRequestOut"])
    types["ListYoutubeAdGroupsResponseIn"] = t.struct(
        {
            "youtubeAdGroups": t.array(t.proxy(renames["YoutubeAdGroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListYoutubeAdGroupsResponseIn"])
    types["ListYoutubeAdGroupsResponseOut"] = t.struct(
        {
            "youtubeAdGroups": t.array(
                t.proxy(renames["YoutubeAdGroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListYoutubeAdGroupsResponseOut"])
    types["YoutubeChannelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"channelId": t.string().optional(), "negative": t.boolean().optional()}
    ).named(renames["YoutubeChannelAssignedTargetingOptionDetailsIn"])
    types["YoutubeChannelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeChannelAssignedTargetingOptionDetailsOut"])
    types["NegativeKeywordListAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negativeKeywordListId": t.string()}
    ).named(renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"])
    types["NegativeKeywordListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negativeKeywordListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordListAssignedTargetingOptionDetailsOut"])
    types["InsertionOrderBudgetSegmentIn"] = t.struct(
        {
            "budgetAmountMicros": t.string(),
            "dateRange": t.proxy(renames["DateRangeIn"]),
            "description": t.string().optional(),
            "campaignBudgetId": t.string().optional(),
        }
    ).named(renames["InsertionOrderBudgetSegmentIn"])
    types["InsertionOrderBudgetSegmentOut"] = t.struct(
        {
            "budgetAmountMicros": t.string(),
            "dateRange": t.proxy(renames["DateRangeOut"]),
            "description": t.string().optional(),
            "campaignBudgetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderBudgetSegmentOut"])
    types["ReplaceSitesResponseIn"] = t.struct(
        {"sites": t.array(t.proxy(renames["SiteIn"])).optional()}
    ).named(renames["ReplaceSitesResponseIn"])
    types["ReplaceSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceSitesResponseOut"])
    types["LineItemBudgetIn"] = t.struct(
        {"maxAmount": t.string().optional(), "budgetAllocationType": t.string()}
    ).named(renames["LineItemBudgetIn"])
    types["LineItemBudgetOut"] = t.struct(
        {
            "maxAmount": t.string().optional(),
            "budgetUnit": t.string().optional(),
            "budgetAllocationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemBudgetOut"])
    types["AudioContentTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AudioContentTypeTargetingOptionDetailsIn"])
    types["AudioContentTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "audioContentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioContentTypeTargetingOptionDetailsOut"])
    types["ProximityLocationListAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "proximityRadiusUnit": t.string(),
            "proximityRadius": t.number(),
            "proximityLocationListId": t.string(),
        }
    ).named(renames["ProximityLocationListAssignedTargetingOptionDetailsIn"])
    types["ProximityLocationListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "proximityRadiusUnit": t.string(),
            "proximityRadius": t.number(),
            "proximityLocationListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProximityLocationListAssignedTargetingOptionDetailsOut"])
    types["CustomListIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CustomListIn"]
    )
    types["CustomListOut"] = t.struct(
        {
            "name": t.string().optional(),
            "customListId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListOut"])
    types["PublisherReviewStatusIn"] = t.struct(
        {"status": t.string().optional(), "publisherName": t.string().optional()}
    ).named(renames["PublisherReviewStatusIn"])
    types["PublisherReviewStatusOut"] = t.struct(
        {
            "status": t.string().optional(),
            "publisherName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherReviewStatusOut"])
    types["CustomListGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["CustomListTargetingSettingIn"]))}
    ).named(renames["CustomListGroupIn"])
    types["CustomListGroupOut"] = t.struct(
        {
            "settings": t.array(t.proxy(renames["CustomListTargetingSettingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListGroupOut"])
    types["YoutubeAndPartnersSettingsIn"] = t.struct(
        {
            "leadFormId": t.string().optional(),
            "inventorySourceSettings": t.proxy(
                renames["YoutubeAndPartnersInventorySourceConfigIn"]
            ).optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyIn"]
            ).optional(),
            "videoAdSequenceSettings": t.proxy(
                renames["VideoAdSequenceSettingsIn"]
            ).optional(),
            "viewFrequencyCap": t.proxy(renames["FrequencyCapIn"]).optional(),
            "targetFrequency": t.proxy(renames["TargetFrequencyIn"]).optional(),
            "contentCategory": t.string().optional(),
            "linkedMerchantId": t.string().optional(),
            "thirdPartyMeasurementSettings": t.proxy(
                renames["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"]
            ).optional(),
            "relatedVideoIds": t.array(t.string()).optional(),
        }
    ).named(renames["YoutubeAndPartnersSettingsIn"])
    types["YoutubeAndPartnersSettingsOut"] = t.struct(
        {
            "leadFormId": t.string().optional(),
            "inventorySourceSettings": t.proxy(
                renames["YoutubeAndPartnersInventorySourceConfigOut"]
            ).optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyOut"]
            ).optional(),
            "videoAdSequenceSettings": t.proxy(
                renames["VideoAdSequenceSettingsOut"]
            ).optional(),
            "viewFrequencyCap": t.proxy(renames["FrequencyCapOut"]).optional(),
            "targetFrequency": t.proxy(renames["TargetFrequencyOut"]).optional(),
            "contentCategory": t.string().optional(),
            "linkedMerchantId": t.string().optional(),
            "thirdPartyMeasurementSettings": t.proxy(
                renames["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"]
            ).optional(),
            "relatedVideoIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersSettingsOut"])
    types["AppAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "appPlatform": t.string().optional(),
            "appId": t.string(),
        }
    ).named(renames["AppAssignedTargetingOptionDetailsIn"])
    types["AppAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "appPlatform": t.string().optional(),
            "appId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppAssignedTargetingOptionDetailsOut"])
    types["BulkEditPartnerAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
            ).optional(),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
            ).optional(),
        }
    ).named(renames["BulkEditPartnerAssignedTargetingOptionsRequestIn"])
    types["BulkEditPartnerAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditPartnerAssignedTargetingOptionsRequestOut"])
    types["PartnerGeneralConfigIn"] = t.struct(
        {"timeZone": t.string().optional(), "currencyCode": t.string().optional()}
    ).named(renames["PartnerGeneralConfigIn"])
    types["PartnerGeneralConfigOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerGeneralConfigOut"])
    types["BulkEditAssignedInventorySourcesRequestIn"] = t.struct(
        {
            "createdAssignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceIn"])
            ).optional(),
            "partnerId": t.string().optional(),
            "deletedAssignedInventorySources": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesRequestIn"])
    types["BulkEditAssignedInventorySourcesRequestOut"] = t.struct(
        {
            "createdAssignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceOut"])
            ).optional(),
            "partnerId": t.string().optional(),
            "deletedAssignedInventorySources": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesRequestOut"])
    types["CampaignBudgetIn"] = t.struct(
        {
            "displayName": t.string(),
            "budgetAmountMicros": t.string(),
            "invoiceGroupingId": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]),
            "prismaConfig": t.proxy(renames["PrismaConfigIn"]).optional(),
            "budgetId": t.string().optional(),
            "budgetUnit": t.string(),
            "externalBudgetSource": t.string(),
        }
    ).named(renames["CampaignBudgetIn"])
    types["CampaignBudgetOut"] = t.struct(
        {
            "displayName": t.string(),
            "budgetAmountMicros": t.string(),
            "invoiceGroupingId": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]),
            "prismaConfig": t.proxy(renames["PrismaConfigOut"]).optional(),
            "budgetId": t.string().optional(),
            "budgetUnit": t.string(),
            "externalBudgetSource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignBudgetOut"])
    types["DoubleVerifyFraudInvalidTrafficIn"] = t.struct(
        {
            "avoidInsufficientOption": t.boolean().optional(),
            "avoidedFraudOption": t.string().optional(),
        }
    ).named(renames["DoubleVerifyFraudInvalidTrafficIn"])
    types["DoubleVerifyFraudInvalidTrafficOut"] = t.struct(
        {
            "avoidInsufficientOption": t.boolean().optional(),
            "avoidedFraudOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyFraudInvalidTrafficOut"])
    types["AdvertiserSdfConfigIn"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["SdfConfigIn"]).optional(),
            "overridePartnerSdfConfig": t.boolean().optional(),
        }
    ).named(renames["AdvertiserSdfConfigIn"])
    types["AdvertiserSdfConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["SdfConfigOut"]).optional(),
            "overridePartnerSdfConfig": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserSdfConfigOut"])
    types["DayAndTimeAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "timeZoneResolution": t.string(),
            "endHour": t.integer(),
            "startHour": t.integer(),
            "dayOfWeek": t.string(),
        }
    ).named(renames["DayAndTimeAssignedTargetingOptionDetailsIn"])
    types["DayAndTimeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "timeZoneResolution": t.string(),
            "endHour": t.integer(),
            "startHour": t.integer(),
            "dayOfWeek": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayAndTimeAssignedTargetingOptionDetailsOut"])
    types["NativeContentPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"contentPosition": t.string().optional()}
    ).named(renames["NativeContentPositionAssignedTargetingOptionDetailsIn"])
    types["NativeContentPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "contentPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentPositionAssignedTargetingOptionDetailsOut"])
    types["CounterEventIn"] = t.struct(
        {"name": t.string(), "reportingName": t.string()}
    ).named(renames["CounterEventIn"])
    types["CounterEventOut"] = t.struct(
        {
            "name": t.string(),
            "reportingName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterEventOut"])
    types["NativeContentPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["NativeContentPositionTargetingOptionDetailsIn"])
    types["NativeContentPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentPositionTargetingOptionDetailsOut"])
    types["CreateSdfDownloadTaskRequestIn"] = t.struct(
        {
            "parentEntityFilter": t.proxy(renames["ParentEntityFilterIn"]).optional(),
            "advertiserId": t.string().optional(),
            "inventorySourceFilter": t.proxy(
                renames["InventorySourceFilterIn"]
            ).optional(),
            "partnerId": t.string().optional(),
            "idFilter": t.proxy(renames["IdFilterIn"]).optional(),
            "version": t.string(),
        }
    ).named(renames["CreateSdfDownloadTaskRequestIn"])
    types["CreateSdfDownloadTaskRequestOut"] = t.struct(
        {
            "parentEntityFilter": t.proxy(renames["ParentEntityFilterOut"]).optional(),
            "advertiserId": t.string().optional(),
            "inventorySourceFilter": t.proxy(
                renames["InventorySourceFilterOut"]
            ).optional(),
            "partnerId": t.string().optional(),
            "idFilter": t.proxy(renames["IdFilterOut"]).optional(),
            "version": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSdfDownloadTaskRequestOut"])
    types["YoutubeAndPartnersBiddingStrategyIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string().optional()}
    ).named(renames["YoutubeAndPartnersBiddingStrategyIn"])
    types["YoutubeAndPartnersBiddingStrategyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "adGroupEffectiveTargetCpaValue": t.string().optional(),
            "adGroupEffectiveTargetCpaSource": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersBiddingStrategyOut"])
    types["BrowserAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["BrowserAssignedTargetingOptionDetailsIn"])
    types["BrowserAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserAssignedTargetingOptionDetailsOut"])
    types["MaximizeSpendBidStrategyIn"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "raiseBidForDeals": t.boolean().optional(),
            "performanceGoalType": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
        }
    ).named(renames["MaximizeSpendBidStrategyIn"])
    types["MaximizeSpendBidStrategyOut"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "raiseBidForDeals": t.boolean().optional(),
            "performanceGoalType": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaximizeSpendBidStrategyOut"])
    types["YoutubeAdGroupAdIn"] = t.struct(
        {
            "inStreamAd": t.proxy(renames["InStreamAdIn"]).optional(),
            "videoPerformanceAd": t.proxy(renames["VideoPerformanceAdIn"]).optional(),
            "displayName": t.string().optional(),
            "bumperAd": t.proxy(renames["BumperAdIn"]).optional(),
            "nonSkippableAd": t.proxy(renames["NonSkippableAdIn"]).optional(),
            "adGroupId": t.string().optional(),
            "name": t.string().optional(),
            "adUrls": t.array(t.proxy(renames["AdUrlIn"])).optional(),
            "videoDiscoverAd": t.proxy(renames["VideoDiscoveryAdIn"]).optional(),
            "adGroupAdId": t.string().optional(),
            "mastheadAd": t.proxy(renames["MastheadAdIn"]).optional(),
            "displayVideoSourceAd": t.proxy(
                renames["DisplayVideoSourceAdIn"]
            ).optional(),
            "audioAd": t.proxy(renames["AudioAdIn"]).optional(),
            "entityStatus": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["YoutubeAdGroupAdIn"])
    types["YoutubeAdGroupAdOut"] = t.struct(
        {
            "inStreamAd": t.proxy(renames["InStreamAdOut"]).optional(),
            "videoPerformanceAd": t.proxy(renames["VideoPerformanceAdOut"]).optional(),
            "displayName": t.string().optional(),
            "bumperAd": t.proxy(renames["BumperAdOut"]).optional(),
            "nonSkippableAd": t.proxy(renames["NonSkippableAdOut"]).optional(),
            "adGroupId": t.string().optional(),
            "name": t.string().optional(),
            "adUrls": t.array(t.proxy(renames["AdUrlOut"])).optional(),
            "videoDiscoverAd": t.proxy(renames["VideoDiscoveryAdOut"]).optional(),
            "adGroupAdId": t.string().optional(),
            "mastheadAd": t.proxy(renames["MastheadAdOut"]).optional(),
            "displayVideoSourceAd": t.proxy(
                renames["DisplayVideoSourceAdOut"]
            ).optional(),
            "audioAd": t.proxy(renames["AudioAdOut"]).optional(),
            "entityStatus": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupAdOut"])
    types["UserRewardedContentAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["UserRewardedContentAssignedTargetingOptionDetailsIn"])
    types["UserRewardedContentAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "userRewardedContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRewardedContentAssignedTargetingOptionDetailsOut"])
    types["BusinessChainTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["BusinessChainTargetingOptionDetailsIn"])
    types["BusinessChainTargetingOptionDetailsOut"] = t.struct(
        {
            "geoRegion": t.string().optional(),
            "geoRegionType": t.string().optional(),
            "businessChain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessChainTargetingOptionDetailsOut"])
    types["BulkEditAssignedTargetingOptionsResponseIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["BulkEditAssignedTargetingOptionsResponseIn"])
    types["BulkEditAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "failedLineItemIds": t.array(t.string()).optional(),
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "updatedLineItemIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsResponseOut"])
    types["TranscodeIn"] = t.struct(
        {
            "fileSizeBytes": t.string().optional(),
            "name": t.string().optional(),
            "bitRateKbps": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]).optional(),
            "audioSampleRateHz": t.string().optional(),
            "mimeType": t.string().optional(),
            "transcoded": t.boolean().optional(),
            "frameRate": t.number().optional(),
            "audioBitRateKbps": t.string().optional(),
        }
    ).named(renames["TranscodeIn"])
    types["TranscodeOut"] = t.struct(
        {
            "fileSizeBytes": t.string().optional(),
            "name": t.string().optional(),
            "bitRateKbps": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]).optional(),
            "audioSampleRateHz": t.string().optional(),
            "mimeType": t.string().optional(),
            "transcoded": t.boolean().optional(),
            "frameRate": t.number().optional(),
            "audioBitRateKbps": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscodeOut"])
    types["InventorySourceIn"] = t.struct(
        {
            "subSitePropertyId": t.string().optional(),
            "rateDetails": t.proxy(renames["RateDetailsIn"]),
            "creativeConfigs": t.array(t.proxy(renames["CreativeConfigIn"])).optional(),
            "guaranteedOrderId": t.string().optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "deliveryMethod": t.string().optional(),
            "displayName": t.string().optional(),
            "readWriteAccessors": t.proxy(
                renames["InventorySourceAccessorsIn"]
            ).optional(),
            "inventorySourceType": t.string().optional(),
            "status": t.proxy(renames["InventorySourceStatusIn"]).optional(),
            "commitment": t.string().optional(),
            "dealId": t.string().optional(),
            "exchange": t.string().optional(),
            "publisherName": t.string().optional(),
        }
    ).named(renames["InventorySourceIn"])
    types["InventorySourceOut"] = t.struct(
        {
            "inventorySourceId": t.string().optional(),
            "subSitePropertyId": t.string().optional(),
            "rateDetails": t.proxy(renames["RateDetailsOut"]),
            "creativeConfigs": t.array(
                t.proxy(renames["CreativeConfigOut"])
            ).optional(),
            "guaranteedOrderId": t.string().optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "inventorySourceProductType": t.string().optional(),
            "deliveryMethod": t.string().optional(),
            "displayName": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "readWriteAccessors": t.proxy(
                renames["InventorySourceAccessorsOut"]
            ).optional(),
            "inventorySourceType": t.string().optional(),
            "status": t.proxy(renames["InventorySourceStatusOut"]).optional(),
            "readPartnerIds": t.array(t.string()).optional(),
            "commitment": t.string().optional(),
            "updateTime": t.string().optional(),
            "dealId": t.string().optional(),
            "exchange": t.string().optional(),
            "publisherName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceOut"])

    functions = {}
    functions["customListsGet"] = displayvideo.get(
        "v2/customLists",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customListsList"] = displayvideo.get(
        "v2/customLists",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["combinedAudiencesGet"] = displayvideo.get(
        "v2/combinedAudiences",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCombinedAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["combinedAudiencesList"] = displayvideo.get(
        "v2/combinedAudiences",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCombinedAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsList"] = displayvideo.patch(
        "v2/inventorySourceGroups/{inventorySourceGroupId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsCreate"] = displayvideo.patch(
        "v2/inventorySourceGroups/{inventorySourceGroupId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsGet"] = displayvideo.patch(
        "v2/inventorySourceGroups/{inventorySourceGroupId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsDelete"] = displayvideo.patch(
        "v2/inventorySourceGroups/{inventorySourceGroupId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsPatch"] = displayvideo.patch(
        "v2/inventorySourceGroups/{inventorySourceGroupId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesDelete"
    ] = displayvideo.post(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string(),
                "partnerId": t.string().optional(),
                "inventorySourceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedInventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesBulkEdit"
    ] = displayvideo.post(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string(),
                "partnerId": t.string().optional(),
                "inventorySourceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedInventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsAssignedInventorySourcesList"] = displayvideo.post(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string(),
                "partnerId": t.string().optional(),
                "inventorySourceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedInventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesCreate"
    ] = displayvideo.post(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "inventorySourceGroupId": t.string(),
                "partnerId": t.string().optional(),
                "inventorySourceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedInventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesGet"] = displayvideo.get(
        "v2/inventorySources",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourcesEditInventorySourceReadWriteAccessors"
    ] = displayvideo.get(
        "v2/inventorySources",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesCreate"] = displayvideo.get(
        "v2/inventorySources",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesPatch"] = displayvideo.get(
        "v2/inventorySources",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesList"] = displayvideo.get(
        "v2/inventorySources",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersGet"] = displayvideo.get(
        "v2/guaranteedOrders",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuaranteedOrdersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersCreate"] = displayvideo.get(
        "v2/guaranteedOrders",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuaranteedOrdersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersPatch"] = displayvideo.get(
        "v2/guaranteedOrders",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuaranteedOrdersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersEditGuaranteedOrderReadAccessors"] = displayvideo.get(
        "v2/guaranteedOrders",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuaranteedOrdersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersList"] = displayvideo.get(
        "v2/guaranteedOrders",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuaranteedOrdersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersPatch"] = displayvideo.post(
        "v2/users",
        t.struct(
            {
                "assignedUserRoles": t.array(
                    t.proxy(renames["AssignedUserRoleIn"])
                ).optional(),
                "email": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = displayvideo.post(
        "v2/users",
        t.struct(
            {
                "assignedUserRoles": t.array(
                    t.proxy(renames["AssignedUserRoleIn"])
                ).optional(),
                "email": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = displayvideo.post(
        "v2/users",
        t.struct(
            {
                "assignedUserRoles": t.array(
                    t.proxy(renames["AssignedUserRoleIn"])
                ).optional(),
                "email": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGet"] = displayvideo.post(
        "v2/users",
        t.struct(
            {
                "assignedUserRoles": t.array(
                    t.proxy(renames["AssignedUserRoleIn"])
                ).optional(),
                "email": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersBulkEditAssignedUserRoles"] = displayvideo.post(
        "v2/users",
        t.struct(
            {
                "assignedUserRoles": t.array(
                    t.proxy(renames["AssignedUserRoleIn"])
                ).optional(),
                "email": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersCreate"] = displayvideo.post(
        "v2/users",
        t.struct(
            {
                "assignedUserRoles": t.array(
                    t.proxy(renames["AssignedUserRoleIn"])
                ).optional(),
                "email": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightGroupsPatch"] = displayvideo.get(
        "v2/floodlightGroups/{floodlightGroupId}",
        t.struct(
            {
                "floodlightGroupId": t.string(),
                "partnerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightGroupsGet"] = displayvideo.get(
        "v2/floodlightGroups/{floodlightGroupId}",
        t.struct(
            {
                "floodlightGroupId": t.string(),
                "partnerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsPatch"] = displayvideo.post(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "customBiddingAlgorithmType": t.string(),
                "advertiserId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "partnerId": t.string().optional(),
                "entityStatus": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingAlgorithmOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsGet"] = displayvideo.post(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "customBiddingAlgorithmType": t.string(),
                "advertiserId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "partnerId": t.string().optional(),
                "entityStatus": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingAlgorithmOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsUploadScript"] = displayvideo.post(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "customBiddingAlgorithmType": t.string(),
                "advertiserId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "partnerId": t.string().optional(),
                "entityStatus": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingAlgorithmOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsList"] = displayvideo.post(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "customBiddingAlgorithmType": t.string(),
                "advertiserId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "partnerId": t.string().optional(),
                "entityStatus": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingAlgorithmOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsCreate"] = displayvideo.post(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "customBiddingAlgorithmType": t.string(),
                "advertiserId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "partnerId": t.string().optional(),
                "entityStatus": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingAlgorithmOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsGet"] = displayvideo.post(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "script": t.proxy(renames["CustomBiddingScriptRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingScriptOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsList"] = displayvideo.post(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "script": t.proxy(renames["CustomBiddingScriptRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingScriptOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsCreate"] = displayvideo.post(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "script": t.proxy(renames["CustomBiddingScriptRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingScriptOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = displayvideo.post(
        "media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleBytestreamMediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaUpload"] = displayvideo.post(
        "media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleBytestreamMediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sdfdownloadtasksCreate"] = displayvideo.post(
        "v2/sdfdownloadtasks",
        t.struct(
            {
                "parentEntityFilter": t.proxy(
                    renames["ParentEntityFilterIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
                "inventorySourceFilter": t.proxy(
                    renames["InventorySourceFilterIn"]
                ).optional(),
                "partnerId": t.string().optional(),
                "idFilter": t.proxy(renames["IdFilterIn"]).optional(),
                "version": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sdfdownloadtasksOperationsGet"] = displayvideo.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleAudiencesGet"] = displayvideo.get(
        "v2/googleAudiences",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGoogleAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleAudiencesList"] = displayvideo.get(
        "v2/googleAudiences",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGoogleAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTypesTargetingOptionsGet"] = displayvideo.get(
        "v2/targetingTypes/{targetingType}/targetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTypesTargetingOptionsSearch"] = displayvideo.get(
        "v2/targetingTypes/{targetingType}/targetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTypesTargetingOptionsList"] = displayvideo.get(
        "v2/targetingTypes/{targetingType}/targetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersListAssignedTargetingOptions"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersPatch"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersGet"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersDelete"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreate"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersAudit"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersEditAssignedTargetingOptions"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersList"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsCreate"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "negativeKeywordListId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsDelete"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "negativeKeywordListId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsBulkEdit"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "negativeKeywordListId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsReplace"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "negativeKeywordListId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsNegativeKeywordsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "negativeKeywordListId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersListAssignedTargetingOptions"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "entityStatus": t.string(),
                "insertionOrderType": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "campaignId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "entityStatus": t.string(),
                "insertionOrderType": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "campaignId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "entityStatus": t.string(),
                "insertionOrderType": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "campaignId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "entityStatus": t.string(),
                "insertionOrderType": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "campaignId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "entityStatus": t.string(),
                "insertionOrderType": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "campaignId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "entityStatus": t.string(),
                "insertionOrderType": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "campaignId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/locationLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "locationType": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/locationLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "locationType": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/locationLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "locationType": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/locationLists",
        t.struct(
            {
                "advertiserId": t.string(),
                "locationType": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations:bulkEdit",
        t.struct(
            {
                "locationListId": t.string(),
                "advertiserId": t.string(),
                "deletedAssignedLocations": t.array(t.string()).optional(),
                "createdAssignedLocations": t.array(
                    t.proxy(renames["AssignedLocationIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations:bulkEdit",
        t.struct(
            {
                "locationListId": t.string(),
                "advertiserId": t.string(),
                "deletedAssignedLocations": t.array(t.string()).optional(),
                "createdAssignedLocations": t.array(
                    t.proxy(renames["AssignedLocationIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations:bulkEdit",
        t.struct(
            {
                "locationListId": t.string(),
                "advertiserId": t.string(),
                "deletedAssignedLocations": t.array(t.string()).optional(),
                "createdAssignedLocations": t.array(
                    t.proxy(renames["AssignedLocationIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsBulkEdit"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations:bulkEdit",
        t.struct(
            {
                "locationListId": t.string(),
                "advertiserId": t.string(),
                "deletedAssignedLocations": t.array(t.string()).optional(),
                "createdAssignedLocations": t.array(
                    t.proxy(renames["AssignedLocationIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersDeactivate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/manualTriggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListManualTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersActivate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/manualTriggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListManualTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/manualTriggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListManualTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/manualTriggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListManualTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/manualTriggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListManualTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/manualTriggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListManualTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersAssetsUpload"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/assets",
        t.struct(
            {
                "advertiserId": t.string(),
                "filename": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateAssetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "skippable": t.boolean().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "entityStatus": t.string(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "jsTrackerUrl": t.string().optional(),
                "vastTagUrl": t.string().optional(),
                "notes": t.string().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "expandingDirection": t.string().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "thirdPartyTag": t.string().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "expandOnHover": t.boolean().optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "requireHtml5": t.boolean().optional(),
                "displayName": t.string(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "integrationCode": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "appendedTag": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "hostingSource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "skippable": t.boolean().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "entityStatus": t.string(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "jsTrackerUrl": t.string().optional(),
                "vastTagUrl": t.string().optional(),
                "notes": t.string().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "expandingDirection": t.string().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "thirdPartyTag": t.string().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "expandOnHover": t.boolean().optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "requireHtml5": t.boolean().optional(),
                "displayName": t.string(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "integrationCode": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "appendedTag": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "hostingSource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "skippable": t.boolean().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "entityStatus": t.string(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "jsTrackerUrl": t.string().optional(),
                "vastTagUrl": t.string().optional(),
                "notes": t.string().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "expandingDirection": t.string().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "thirdPartyTag": t.string().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "expandOnHover": t.boolean().optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "requireHtml5": t.boolean().optional(),
                "displayName": t.string(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "integrationCode": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "appendedTag": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "hostingSource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "skippable": t.boolean().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "entityStatus": t.string(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "jsTrackerUrl": t.string().optional(),
                "vastTagUrl": t.string().optional(),
                "notes": t.string().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "expandingDirection": t.string().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "thirdPartyTag": t.string().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "expandOnHover": t.boolean().optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "requireHtml5": t.boolean().optional(),
                "displayName": t.string(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "integrationCode": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "appendedTag": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "hostingSource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "skippable": t.boolean().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "entityStatus": t.string(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "jsTrackerUrl": t.string().optional(),
                "vastTagUrl": t.string().optional(),
                "notes": t.string().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "expandingDirection": t.string().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "thirdPartyTag": t.string().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "expandOnHover": t.boolean().optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "requireHtml5": t.boolean().optional(),
                "displayName": t.string(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "integrationCode": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "appendedTag": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "hostingSource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInvoicesList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/invoices:lookupInvoiceCurrency",
        t.struct(
            {
                "advertiserId": t.string(),
                "invoiceMonth": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupInvoiceCurrencyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInvoicesLookupInvoiceCurrency"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/invoices:lookupInvoiceCurrency",
        t.struct(
            {
                "advertiserId": t.string(),
                "invoiceMonth": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupInvoiceCurrencyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesBulkEdit"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "urlOrAppId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesReplace"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "urlOrAppId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesList"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "urlOrAppId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesCreate"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "urlOrAppId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesDelete"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "urlOrAppId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersYoutubeAdGroupsBulkListAdGroupAssignedTargetingOptions"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups",
        t.struct(
            {
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups",
        t.struct(
            {
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups",
        t.struct(
            {
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersYoutubeAdGroupsTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups/{youtubeAdGroupId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "targetingType": t.string(),
                "assignedTargetingOptionId": t.string(),
                "youtubeAdGroupId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersYoutubeAdGroupsTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups/{youtubeAdGroupId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "targetingType": t.string(),
                "assignedTargetingOptionId": t.string(),
                "youtubeAdGroupId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsBulkListAssignedTargetingOptions"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsGenerateDefault"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsDuplicate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsBulkUpdate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsBulkEditAssignedTargetingOptions"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems:bulkEditAssignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "lineItemIds": t.array(t.string()),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsDelete"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "entityStatus": t.string(),
                "campaignBudgets": t.array(
                    t.proxy(renames["CampaignBudgetIn"])
                ).optional(),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "displayName": t.string(),
                "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
                "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsListAssignedTargetingOptions"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "entityStatus": t.string(),
                "campaignBudgets": t.array(
                    t.proxy(renames["CampaignBudgetIn"])
                ).optional(),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "displayName": t.string(),
                "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
                "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsList"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "entityStatus": t.string(),
                "campaignBudgets": t.array(
                    t.proxy(renames["CampaignBudgetIn"])
                ).optional(),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "displayName": t.string(),
                "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
                "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsCreate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "entityStatus": t.string(),
                "campaignBudgets": t.array(
                    t.proxy(renames["CampaignBudgetIn"])
                ).optional(),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "displayName": t.string(),
                "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
                "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsGet"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "entityStatus": t.string(),
                "campaignBudgets": t.array(
                    t.proxy(renames["CampaignBudgetIn"])
                ).optional(),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "displayName": t.string(),
                "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
                "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsPatch"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "entityStatus": t.string(),
                "campaignBudgets": t.array(
                    t.proxy(renames["CampaignBudgetIn"])
                ).optional(),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "displayName": t.string(),
                "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
                "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CampaignOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersCampaignsTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "campaignId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCampaignAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersCampaignsTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "campaignId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCampaignAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupAdsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroupAds/{youtubeAdGroupAdId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "youtubeAdGroupAdId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["YoutubeAdGroupAdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupAdsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroupAds/{youtubeAdGroupAdId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "youtubeAdGroupAdId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["YoutubeAdGroupAdOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersGet"] = displayvideo.post(
        "v2/partners/{partnerId}:editAssignedTargetingOptions",
        t.struct(
            {
                "partnerId": t.string(),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditPartnerAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersList"] = displayvideo.post(
        "v2/partners/{partnerId}:editAssignedTargetingOptions",
        t.struct(
            {
                "partnerId": t.string(),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditPartnerAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersEditAssignedTargetingOptions"] = displayvideo.post(
        "v2/partners/{partnerId}:editAssignedTargetingOptions",
        t.struct(
            {
                "partnerId": t.string(),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditPartnerAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersTargetingTypesAssignedTargetingOptionsGet"] = displayvideo.post(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "partnerId": t.string(),
                "targetingType": t.string(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersTargetingTypesAssignedTargetingOptionsList"] = displayvideo.post(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "partnerId": t.string(),
                "targetingType": t.string(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "partnersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.post(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "partnerId": t.string(),
                "targetingType": t.string(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "partnersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.post(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "partnerId": t.string(),
                "targetingType": t.string(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsCreate"] = displayvideo.patch(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "channelId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "updateMask": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsGet"] = displayvideo.patch(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "channelId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "updateMask": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsList"] = displayvideo.patch(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "channelId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "updateMask": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsPatch"] = displayvideo.patch(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "channelId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "updateMask": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesList"] = displayvideo.delete(
        "v2/partners/{partnerId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesReplace"] = displayvideo.delete(
        "v2/partners/{partnerId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesCreate"] = displayvideo.delete(
        "v2/partners/{partnerId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesBulkEdit"] = displayvideo.delete(
        "v2/partners/{partnerId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesDelete"] = displayvideo.delete(
        "v2/partners/{partnerId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesList"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences/{firstAndThirdPartyAudienceId}:editCustomerMatchMembers",
        t.struct(
            {
                "firstAndThirdPartyAudienceId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditCustomerMatchMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesPatch"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences/{firstAndThirdPartyAudienceId}:editCustomerMatchMembers",
        t.struct(
            {
                "firstAndThirdPartyAudienceId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditCustomerMatchMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesCreate"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences/{firstAndThirdPartyAudienceId}:editCustomerMatchMembers",
        t.struct(
            {
                "firstAndThirdPartyAudienceId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditCustomerMatchMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesGet"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences/{firstAndThirdPartyAudienceId}:editCustomerMatchMembers",
        t.struct(
            {
                "firstAndThirdPartyAudienceId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditCustomerMatchMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "firstAndThirdPartyAudiencesEditCustomerMatchMembers"
    ] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences/{firstAndThirdPartyAudienceId}:editCustomerMatchMembers",
        t.struct(
            {
                "firstAndThirdPartyAudienceId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditCustomerMatchMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="displayvideo",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
