from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_displayvideo():
    displayvideo = HTTPRuntime("https://displayvideo.googleapis.com/")

    renames = {
        "ErrorResponse": "_displayvideo_1_ErrorResponse",
        "PerformanceGoalBidStrategyIn": "_displayvideo_2_PerformanceGoalBidStrategyIn",
        "PerformanceGoalBidStrategyOut": "_displayvideo_3_PerformanceGoalBidStrategyOut",
        "BulkEditAssignedTargetingOptionsResponseIn": "_displayvideo_4_BulkEditAssignedTargetingOptionsResponseIn",
        "BulkEditAssignedTargetingOptionsResponseOut": "_displayvideo_5_BulkEditAssignedTargetingOptionsResponseOut",
        "SearchTargetingOptionsRequestIn": "_displayvideo_6_SearchTargetingOptionsRequestIn",
        "SearchTargetingOptionsRequestOut": "_displayvideo_7_SearchTargetingOptionsRequestOut",
        "CreateAssetRequestIn": "_displayvideo_8_CreateAssetRequestIn",
        "CreateAssetRequestOut": "_displayvideo_9_CreateAssetRequestOut",
        "SdfDownloadTaskIn": "_displayvideo_10_SdfDownloadTaskIn",
        "SdfDownloadTaskOut": "_displayvideo_11_SdfDownloadTaskOut",
        "LookbackWindowIn": "_displayvideo_12_LookbackWindowIn",
        "LookbackWindowOut": "_displayvideo_13_LookbackWindowOut",
        "ListYoutubeAdGroupAssignedTargetingOptionsResponseIn": "_displayvideo_14_ListYoutubeAdGroupAssignedTargetingOptionsResponseIn",
        "ListYoutubeAdGroupAssignedTargetingOptionsResponseOut": "_displayvideo_15_ListYoutubeAdGroupAssignedTargetingOptionsResponseOut",
        "DoubleVerifyDisplayViewabilityIn": "_displayvideo_16_DoubleVerifyDisplayViewabilityIn",
        "DoubleVerifyDisplayViewabilityOut": "_displayvideo_17_DoubleVerifyDisplayViewabilityOut",
        "YoutubeAndPartnersBiddingStrategyIn": "_displayvideo_18_YoutubeAndPartnersBiddingStrategyIn",
        "YoutubeAndPartnersBiddingStrategyOut": "_displayvideo_19_YoutubeAndPartnersBiddingStrategyOut",
        "TrackingFloodlightActivityConfigIn": "_displayvideo_20_TrackingFloodlightActivityConfigIn",
        "TrackingFloodlightActivityConfigOut": "_displayvideo_21_TrackingFloodlightActivityConfigOut",
        "FirstAndThirdPartyAudienceIn": "_displayvideo_22_FirstAndThirdPartyAudienceIn",
        "FirstAndThirdPartyAudienceOut": "_displayvideo_23_FirstAndThirdPartyAudienceOut",
        "DeviceMakeModelTargetingOptionDetailsIn": "_displayvideo_24_DeviceMakeModelTargetingOptionDetailsIn",
        "DeviceMakeModelTargetingOptionDetailsOut": "_displayvideo_25_DeviceMakeModelTargetingOptionDetailsOut",
        "CampaignBudgetIn": "_displayvideo_26_CampaignBudgetIn",
        "CampaignBudgetOut": "_displayvideo_27_CampaignBudgetOut",
        "ProductMatchDimensionIn": "_displayvideo_28_ProductMatchDimensionIn",
        "ProductMatchDimensionOut": "_displayvideo_29_ProductMatchDimensionOut",
        "MeasurementConfigIn": "_displayvideo_30_MeasurementConfigIn",
        "MeasurementConfigOut": "_displayvideo_31_MeasurementConfigOut",
        "BusinessChainAssignedTargetingOptionDetailsIn": "_displayvideo_32_BusinessChainAssignedTargetingOptionDetailsIn",
        "BusinessChainAssignedTargetingOptionDetailsOut": "_displayvideo_33_BusinessChainAssignedTargetingOptionDetailsOut",
        "UserRewardedContentAssignedTargetingOptionDetailsIn": "_displayvideo_34_UserRewardedContentAssignedTargetingOptionDetailsIn",
        "UserRewardedContentAssignedTargetingOptionDetailsOut": "_displayvideo_35_UserRewardedContentAssignedTargetingOptionDetailsOut",
        "GeoRegionSearchTermsIn": "_displayvideo_36_GeoRegionSearchTermsIn",
        "GeoRegionSearchTermsOut": "_displayvideo_37_GeoRegionSearchTermsOut",
        "ListInsertionOrderAssignedTargetingOptionsResponseIn": "_displayvideo_38_ListInsertionOrderAssignedTargetingOptionsResponseIn",
        "ListInsertionOrderAssignedTargetingOptionsResponseOut": "_displayvideo_39_ListInsertionOrderAssignedTargetingOptionsResponseOut",
        "EnvironmentTargetingOptionDetailsIn": "_displayvideo_40_EnvironmentTargetingOptionDetailsIn",
        "EnvironmentTargetingOptionDetailsOut": "_displayvideo_41_EnvironmentTargetingOptionDetailsOut",
        "ListManualTriggersResponseIn": "_displayvideo_42_ListManualTriggersResponseIn",
        "ListManualTriggersResponseOut": "_displayvideo_43_ListManualTriggersResponseOut",
        "DigitalContentLabelAssignedTargetingOptionDetailsIn": "_displayvideo_44_DigitalContentLabelAssignedTargetingOptionDetailsIn",
        "DigitalContentLabelAssignedTargetingOptionDetailsOut": "_displayvideo_45_DigitalContentLabelAssignedTargetingOptionDetailsOut",
        "GoogleAudienceGroupIn": "_displayvideo_46_GoogleAudienceGroupIn",
        "GoogleAudienceGroupOut": "_displayvideo_47_GoogleAudienceGroupOut",
        "CustomBiddingAlgorithmIn": "_displayvideo_48_CustomBiddingAlgorithmIn",
        "CustomBiddingAlgorithmOut": "_displayvideo_49_CustomBiddingAlgorithmOut",
        "ReplaceNegativeKeywordsResponseIn": "_displayvideo_50_ReplaceNegativeKeywordsResponseIn",
        "ReplaceNegativeKeywordsResponseOut": "_displayvideo_51_ReplaceNegativeKeywordsResponseOut",
        "PoiAssignedTargetingOptionDetailsIn": "_displayvideo_52_PoiAssignedTargetingOptionDetailsIn",
        "PoiAssignedTargetingOptionDetailsOut": "_displayvideo_53_PoiAssignedTargetingOptionDetailsOut",
        "BulkListAdGroupAssignedTargetingOptionsResponseIn": "_displayvideo_54_BulkListAdGroupAssignedTargetingOptionsResponseIn",
        "BulkListAdGroupAssignedTargetingOptionsResponseOut": "_displayvideo_55_BulkListAdGroupAssignedTargetingOptionsResponseOut",
        "ListPartnerAssignedTargetingOptionsResponseIn": "_displayvideo_56_ListPartnerAssignedTargetingOptionsResponseIn",
        "ListPartnerAssignedTargetingOptionsResponseOut": "_displayvideo_57_ListPartnerAssignedTargetingOptionsResponseOut",
        "ListCampaignsResponseIn": "_displayvideo_58_ListCampaignsResponseIn",
        "ListCampaignsResponseOut": "_displayvideo_59_ListCampaignsResponseOut",
        "ContentGenreAssignedTargetingOptionDetailsIn": "_displayvideo_60_ContentGenreAssignedTargetingOptionDetailsIn",
        "ContentGenreAssignedTargetingOptionDetailsOut": "_displayvideo_61_ContentGenreAssignedTargetingOptionDetailsOut",
        "ExchangeAssignedTargetingOptionDetailsIn": "_displayvideo_62_ExchangeAssignedTargetingOptionDetailsIn",
        "ExchangeAssignedTargetingOptionDetailsOut": "_displayvideo_63_ExchangeAssignedTargetingOptionDetailsOut",
        "ExchangeConfigEnabledExchangeIn": "_displayvideo_64_ExchangeConfigEnabledExchangeIn",
        "ExchangeConfigEnabledExchangeOut": "_displayvideo_65_ExchangeConfigEnabledExchangeOut",
        "BulkEditPartnerAssignedTargetingOptionsRequestIn": "_displayvideo_66_BulkEditPartnerAssignedTargetingOptionsRequestIn",
        "BulkEditPartnerAssignedTargetingOptionsRequestOut": "_displayvideo_67_BulkEditPartnerAssignedTargetingOptionsRequestOut",
        "EditCustomerMatchMembersResponseIn": "_displayvideo_68_EditCustomerMatchMembersResponseIn",
        "EditCustomerMatchMembersResponseOut": "_displayvideo_69_EditCustomerMatchMembersResponseOut",
        "CustomListIn": "_displayvideo_70_CustomListIn",
        "CustomListOut": "_displayvideo_71_CustomListOut",
        "ListCreativesResponseIn": "_displayvideo_72_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_displayvideo_73_ListCreativesResponseOut",
        "SiteIn": "_displayvideo_74_SiteIn",
        "SiteOut": "_displayvideo_75_SiteOut",
        "LineItemFlightIn": "_displayvideo_76_LineItemFlightIn",
        "LineItemFlightOut": "_displayvideo_77_LineItemFlightOut",
        "SdfConfigIn": "_displayvideo_78_SdfConfigIn",
        "SdfConfigOut": "_displayvideo_79_SdfConfigOut",
        "NegativeKeywordListIn": "_displayvideo_80_NegativeKeywordListIn",
        "NegativeKeywordListOut": "_displayvideo_81_NegativeKeywordListOut",
        "ChannelAssignedTargetingOptionDetailsIn": "_displayvideo_82_ChannelAssignedTargetingOptionDetailsIn",
        "ChannelAssignedTargetingOptionDetailsOut": "_displayvideo_83_ChannelAssignedTargetingOptionDetailsOut",
        "TranscodeIn": "_displayvideo_84_TranscodeIn",
        "TranscodeOut": "_displayvideo_85_TranscodeOut",
        "EditCustomerMatchMembersRequestIn": "_displayvideo_86_EditCustomerMatchMembersRequestIn",
        "EditCustomerMatchMembersRequestOut": "_displayvideo_87_EditCustomerMatchMembersRequestOut",
        "ChannelIn": "_displayvideo_88_ChannelIn",
        "ChannelOut": "_displayvideo_89_ChannelOut",
        "ListCombinedAudiencesResponseIn": "_displayvideo_90_ListCombinedAudiencesResponseIn",
        "ListCombinedAudiencesResponseOut": "_displayvideo_91_ListCombinedAudiencesResponseOut",
        "NegativeKeywordListAssignedTargetingOptionDetailsIn": "_displayvideo_92_NegativeKeywordListAssignedTargetingOptionDetailsIn",
        "NegativeKeywordListAssignedTargetingOptionDetailsOut": "_displayvideo_93_NegativeKeywordListAssignedTargetingOptionDetailsOut",
        "BulkEditAssignedUserRolesRequestIn": "_displayvideo_94_BulkEditAssignedUserRolesRequestIn",
        "BulkEditAssignedUserRolesRequestOut": "_displayvideo_95_BulkEditAssignedUserRolesRequestOut",
        "DimensionsIn": "_displayvideo_96_DimensionsIn",
        "DimensionsOut": "_displayvideo_97_DimensionsOut",
        "DayAndTimeAssignedTargetingOptionDetailsIn": "_displayvideo_98_DayAndTimeAssignedTargetingOptionDetailsIn",
        "DayAndTimeAssignedTargetingOptionDetailsOut": "_displayvideo_99_DayAndTimeAssignedTargetingOptionDetailsOut",
        "ListGuaranteedOrdersResponseIn": "_displayvideo_100_ListGuaranteedOrdersResponseIn",
        "ListGuaranteedOrdersResponseOut": "_displayvideo_101_ListGuaranteedOrdersResponseOut",
        "FirstAndThirdPartyAudienceTargetingSettingIn": "_displayvideo_102_FirstAndThirdPartyAudienceTargetingSettingIn",
        "FirstAndThirdPartyAudienceTargetingSettingOut": "_displayvideo_103_FirstAndThirdPartyAudienceTargetingSettingOut",
        "DoubleVerifyIn": "_displayvideo_104_DoubleVerifyIn",
        "DoubleVerifyOut": "_displayvideo_105_DoubleVerifyOut",
        "YoutubeVideoDetailsIn": "_displayvideo_106_YoutubeVideoDetailsIn",
        "YoutubeVideoDetailsOut": "_displayvideo_107_YoutubeVideoDetailsOut",
        "UserRewardedContentTargetingOptionDetailsIn": "_displayvideo_108_UserRewardedContentTargetingOptionDetailsIn",
        "UserRewardedContentTargetingOptionDetailsOut": "_displayvideo_109_UserRewardedContentTargetingOptionDetailsOut",
        "InventorySourceAssignedTargetingOptionDetailsIn": "_displayvideo_110_InventorySourceAssignedTargetingOptionDetailsIn",
        "InventorySourceAssignedTargetingOptionDetailsOut": "_displayvideo_111_InventorySourceAssignedTargetingOptionDetailsOut",
        "BulkEditAssignedUserRolesResponseIn": "_displayvideo_112_BulkEditAssignedUserRolesResponseIn",
        "BulkEditAssignedUserRolesResponseOut": "_displayvideo_113_BulkEditAssignedUserRolesResponseOut",
        "BulkEditSitesResponseIn": "_displayvideo_114_BulkEditSitesResponseIn",
        "BulkEditSitesResponseOut": "_displayvideo_115_BulkEditSitesResponseOut",
        "CustomBiddingScriptIn": "_displayvideo_116_CustomBiddingScriptIn",
        "CustomBiddingScriptOut": "_displayvideo_117_CustomBiddingScriptOut",
        "AssignedInventorySourceIn": "_displayvideo_118_AssignedInventorySourceIn",
        "AssignedInventorySourceOut": "_displayvideo_119_AssignedInventorySourceOut",
        "GeoRegionAssignedTargetingOptionDetailsIn": "_displayvideo_120_GeoRegionAssignedTargetingOptionDetailsIn",
        "GeoRegionAssignedTargetingOptionDetailsOut": "_displayvideo_121_GeoRegionAssignedTargetingOptionDetailsOut",
        "CreateSdfDownloadTaskRequestIn": "_displayvideo_122_CreateSdfDownloadTaskRequestIn",
        "CreateSdfDownloadTaskRequestOut": "_displayvideo_123_CreateSdfDownloadTaskRequestOut",
        "GeoRegionTargetingOptionDetailsIn": "_displayvideo_124_GeoRegionTargetingOptionDetailsIn",
        "GeoRegionTargetingOptionDetailsOut": "_displayvideo_125_GeoRegionTargetingOptionDetailsOut",
        "GuaranteedOrderStatusIn": "_displayvideo_126_GuaranteedOrderStatusIn",
        "GuaranteedOrderStatusOut": "_displayvideo_127_GuaranteedOrderStatusOut",
        "TimeRangeIn": "_displayvideo_128_TimeRangeIn",
        "TimeRangeOut": "_displayvideo_129_TimeRangeOut",
        "DoubleVerifyBrandSafetyCategoriesIn": "_displayvideo_130_DoubleVerifyBrandSafetyCategoriesIn",
        "DoubleVerifyBrandSafetyCategoriesOut": "_displayvideo_131_DoubleVerifyBrandSafetyCategoriesOut",
        "ListNegativeKeywordListsResponseIn": "_displayvideo_132_ListNegativeKeywordListsResponseIn",
        "ListNegativeKeywordListsResponseOut": "_displayvideo_133_ListNegativeKeywordListsResponseOut",
        "CombinedAudienceIn": "_displayvideo_134_CombinedAudienceIn",
        "CombinedAudienceOut": "_displayvideo_135_CombinedAudienceOut",
        "LineItemAssignedTargetingOptionIn": "_displayvideo_136_LineItemAssignedTargetingOptionIn",
        "LineItemAssignedTargetingOptionOut": "_displayvideo_137_LineItemAssignedTargetingOptionOut",
        "BulkEditAssignedLocationsResponseIn": "_displayvideo_138_BulkEditAssignedLocationsResponseIn",
        "BulkEditAssignedLocationsResponseOut": "_displayvideo_139_BulkEditAssignedLocationsResponseOut",
        "PrismaConfigIn": "_displayvideo_140_PrismaConfigIn",
        "PrismaConfigOut": "_displayvideo_141_PrismaConfigOut",
        "InStreamAdIn": "_displayvideo_142_InStreamAdIn",
        "InStreamAdOut": "_displayvideo_143_InStreamAdOut",
        "InventorySourceAccessorsPartnerAccessorIn": "_displayvideo_144_InventorySourceAccessorsPartnerAccessorIn",
        "InventorySourceAccessorsPartnerAccessorOut": "_displayvideo_145_InventorySourceAccessorsPartnerAccessorOut",
        "LanguageTargetingOptionDetailsIn": "_displayvideo_146_LanguageTargetingOptionDetailsIn",
        "LanguageTargetingOptionDetailsOut": "_displayvideo_147_LanguageTargetingOptionDetailsOut",
        "OnScreenPositionAssignedTargetingOptionDetailsIn": "_displayvideo_148_OnScreenPositionAssignedTargetingOptionDetailsIn",
        "OnScreenPositionAssignedTargetingOptionDetailsOut": "_displayvideo_149_OnScreenPositionAssignedTargetingOptionDetailsOut",
        "NativeContentPositionAssignedTargetingOptionDetailsIn": "_displayvideo_150_NativeContentPositionAssignedTargetingOptionDetailsIn",
        "NativeContentPositionAssignedTargetingOptionDetailsOut": "_displayvideo_151_NativeContentPositionAssignedTargetingOptionDetailsOut",
        "OnScreenPositionTargetingOptionDetailsIn": "_displayvideo_152_OnScreenPositionTargetingOptionDetailsIn",
        "OnScreenPositionTargetingOptionDetailsOut": "_displayvideo_153_OnScreenPositionTargetingOptionDetailsOut",
        "YoutubeAdGroupAdIn": "_displayvideo_154_YoutubeAdGroupAdIn",
        "YoutubeAdGroupAdOut": "_displayvideo_155_YoutubeAdGroupAdOut",
        "FirstAndThirdPartyAudienceGroupIn": "_displayvideo_156_FirstAndThirdPartyAudienceGroupIn",
        "FirstAndThirdPartyAudienceGroupOut": "_displayvideo_157_FirstAndThirdPartyAudienceGroupOut",
        "GoogleAudienceIn": "_displayvideo_158_GoogleAudienceIn",
        "GoogleAudienceOut": "_displayvideo_159_GoogleAudienceOut",
        "ImageAssetIn": "_displayvideo_160_ImageAssetIn",
        "ImageAssetOut": "_displayvideo_161_ImageAssetOut",
        "CombinedAudienceGroupIn": "_displayvideo_162_CombinedAudienceGroupIn",
        "CombinedAudienceGroupOut": "_displayvideo_163_CombinedAudienceGroupOut",
        "IdFilterIn": "_displayvideo_164_IdFilterIn",
        "IdFilterOut": "_displayvideo_165_IdFilterOut",
        "ContentStreamTypeTargetingOptionDetailsIn": "_displayvideo_166_ContentStreamTypeTargetingOptionDetailsIn",
        "ContentStreamTypeTargetingOptionDetailsOut": "_displayvideo_167_ContentStreamTypeTargetingOptionDetailsOut",
        "AssignedTargetingOptionIn": "_displayvideo_168_AssignedTargetingOptionIn",
        "AssignedTargetingOptionOut": "_displayvideo_169_AssignedTargetingOptionOut",
        "ExitEventIn": "_displayvideo_170_ExitEventIn",
        "ExitEventOut": "_displayvideo_171_ExitEventOut",
        "CarrierAndIspTargetingOptionDetailsIn": "_displayvideo_172_CarrierAndIspTargetingOptionDetailsIn",
        "CarrierAndIspTargetingOptionDetailsOut": "_displayvideo_173_CarrierAndIspTargetingOptionDetailsOut",
        "CustomBiddingModelDetailsIn": "_displayvideo_174_CustomBiddingModelDetailsIn",
        "CustomBiddingModelDetailsOut": "_displayvideo_175_CustomBiddingModelDetailsOut",
        "InsertionOrderIn": "_displayvideo_176_InsertionOrderIn",
        "InsertionOrderOut": "_displayvideo_177_InsertionOrderOut",
        "RegionalLocationListAssignedTargetingOptionDetailsIn": "_displayvideo_178_RegionalLocationListAssignedTargetingOptionDetailsIn",
        "RegionalLocationListAssignedTargetingOptionDetailsOut": "_displayvideo_179_RegionalLocationListAssignedTargetingOptionDetailsOut",
        "BrowserTargetingOptionDetailsIn": "_displayvideo_180_BrowserTargetingOptionDetailsIn",
        "BrowserTargetingOptionDetailsOut": "_displayvideo_181_BrowserTargetingOptionDetailsOut",
        "AdlooxIn": "_displayvideo_182_AdlooxIn",
        "AdlooxOut": "_displayvideo_183_AdlooxOut",
        "ScriptErrorIn": "_displayvideo_184_ScriptErrorIn",
        "ScriptErrorOut": "_displayvideo_185_ScriptErrorOut",
        "BulkEditAssignedLocationsRequestIn": "_displayvideo_186_BulkEditAssignedLocationsRequestIn",
        "BulkEditAssignedLocationsRequestOut": "_displayvideo_187_BulkEditAssignedLocationsRequestOut",
        "PublisherReviewStatusIn": "_displayvideo_188_PublisherReviewStatusIn",
        "PublisherReviewStatusOut": "_displayvideo_189_PublisherReviewStatusOut",
        "AdvertiserGeneralConfigIn": "_displayvideo_190_AdvertiserGeneralConfigIn",
        "AdvertiserGeneralConfigOut": "_displayvideo_191_AdvertiserGeneralConfigOut",
        "FloodlightGroupIn": "_displayvideo_192_FloodlightGroupIn",
        "FloodlightGroupOut": "_displayvideo_193_FloodlightGroupOut",
        "PacingIn": "_displayvideo_194_PacingIn",
        "PacingOut": "_displayvideo_195_PacingOut",
        "ContentInstreamPositionTargetingOptionDetailsIn": "_displayvideo_196_ContentInstreamPositionTargetingOptionDetailsIn",
        "ContentInstreamPositionTargetingOptionDetailsOut": "_displayvideo_197_ContentInstreamPositionTargetingOptionDetailsOut",
        "ListChannelsResponseIn": "_displayvideo_198_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_displayvideo_199_ListChannelsResponseOut",
        "ParentalStatusTargetingOptionDetailsIn": "_displayvideo_200_ParentalStatusTargetingOptionDetailsIn",
        "ParentalStatusTargetingOptionDetailsOut": "_displayvideo_201_ParentalStatusTargetingOptionDetailsOut",
        "InventorySourceVideoCreativeConfigIn": "_displayvideo_202_InventorySourceVideoCreativeConfigIn",
        "InventorySourceVideoCreativeConfigOut": "_displayvideo_203_InventorySourceVideoCreativeConfigOut",
        "InventorySourceStatusIn": "_displayvideo_204_InventorySourceStatusIn",
        "InventorySourceStatusOut": "_displayvideo_205_InventorySourceStatusOut",
        "YoutubeAdGroupAssignedTargetingOptionIn": "_displayvideo_206_YoutubeAdGroupAssignedTargetingOptionIn",
        "YoutubeAdGroupAssignedTargetingOptionOut": "_displayvideo_207_YoutubeAdGroupAssignedTargetingOptionOut",
        "YoutubeChannelAssignedTargetingOptionDetailsIn": "_displayvideo_208_YoutubeChannelAssignedTargetingOptionDetailsIn",
        "YoutubeChannelAssignedTargetingOptionDetailsOut": "_displayvideo_209_YoutubeChannelAssignedTargetingOptionDetailsOut",
        "EditGuaranteedOrderReadAccessorsRequestIn": "_displayvideo_210_EditGuaranteedOrderReadAccessorsRequestIn",
        "EditGuaranteedOrderReadAccessorsRequestOut": "_displayvideo_211_EditGuaranteedOrderReadAccessorsRequestOut",
        "ListAdvertisersResponseIn": "_displayvideo_212_ListAdvertisersResponseIn",
        "ListAdvertisersResponseOut": "_displayvideo_213_ListAdvertisersResponseOut",
        "BulkListAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_214_BulkListAdvertiserAssignedTargetingOptionsResponseIn",
        "BulkListAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_215_BulkListAdvertiserAssignedTargetingOptionsResponseOut",
        "SdfDownloadTaskMetadataIn": "_displayvideo_216_SdfDownloadTaskMetadataIn",
        "SdfDownloadTaskMetadataOut": "_displayvideo_217_SdfDownloadTaskMetadataOut",
        "DeviceTypeTargetingOptionDetailsIn": "_displayvideo_218_DeviceTypeTargetingOptionDetailsIn",
        "DeviceTypeTargetingOptionDetailsOut": "_displayvideo_219_DeviceTypeTargetingOptionDetailsOut",
        "SensitiveCategoryTargetingOptionDetailsIn": "_displayvideo_220_SensitiveCategoryTargetingOptionDetailsIn",
        "SensitiveCategoryTargetingOptionDetailsOut": "_displayvideo_221_SensitiveCategoryTargetingOptionDetailsOut",
        "UrlAssignedTargetingOptionDetailsIn": "_displayvideo_222_UrlAssignedTargetingOptionDetailsIn",
        "UrlAssignedTargetingOptionDetailsOut": "_displayvideo_223_UrlAssignedTargetingOptionDetailsOut",
        "BulkEditAssignedInventorySourcesRequestIn": "_displayvideo_224_BulkEditAssignedInventorySourcesRequestIn",
        "BulkEditAssignedInventorySourcesRequestOut": "_displayvideo_225_BulkEditAssignedInventorySourcesRequestOut",
        "BulkEditAssignedTargetingOptionsRequestIn": "_displayvideo_226_BulkEditAssignedTargetingOptionsRequestIn",
        "BulkEditAssignedTargetingOptionsRequestOut": "_displayvideo_227_BulkEditAssignedTargetingOptionsRequestOut",
        "NativeContentPositionTargetingOptionDetailsIn": "_displayvideo_228_NativeContentPositionTargetingOptionDetailsIn",
        "NativeContentPositionTargetingOptionDetailsOut": "_displayvideo_229_NativeContentPositionTargetingOptionDetailsOut",
        "PartnerGeneralConfigIn": "_displayvideo_230_PartnerGeneralConfigIn",
        "PartnerGeneralConfigOut": "_displayvideo_231_PartnerGeneralConfigOut",
        "ListYoutubeAdGroupAdsResponseIn": "_displayvideo_232_ListYoutubeAdGroupAdsResponseIn",
        "ListYoutubeAdGroupAdsResponseOut": "_displayvideo_233_ListYoutubeAdGroupAdsResponseOut",
        "UniversalAdIdIn": "_displayvideo_234_UniversalAdIdIn",
        "UniversalAdIdOut": "_displayvideo_235_UniversalAdIdOut",
        "AssetIn": "_displayvideo_236_AssetIn",
        "AssetOut": "_displayvideo_237_AssetOut",
        "EmptyIn": "_displayvideo_238_EmptyIn",
        "EmptyOut": "_displayvideo_239_EmptyOut",
        "GoogleBytestreamMediaIn": "_displayvideo_240_GoogleBytestreamMediaIn",
        "GoogleBytestreamMediaOut": "_displayvideo_241_GoogleBytestreamMediaOut",
        "BumperAdIn": "_displayvideo_242_BumperAdIn",
        "BumperAdOut": "_displayvideo_243_BumperAdOut",
        "PoiSearchTermsIn": "_displayvideo_244_PoiSearchTermsIn",
        "PoiSearchTermsOut": "_displayvideo_245_PoiSearchTermsOut",
        "ContentGenreTargetingOptionDetailsIn": "_displayvideo_246_ContentGenreTargetingOptionDetailsIn",
        "ContentGenreTargetingOptionDetailsOut": "_displayvideo_247_ContentGenreTargetingOptionDetailsOut",
        "OperationIn": "_displayvideo_248_OperationIn",
        "OperationOut": "_displayvideo_249_OperationOut",
        "ListAssignedInventorySourcesResponseIn": "_displayvideo_250_ListAssignedInventorySourcesResponseIn",
        "ListAssignedInventorySourcesResponseOut": "_displayvideo_251_ListAssignedInventorySourcesResponseOut",
        "BusinessChainSearchTermsIn": "_displayvideo_252_BusinessChainSearchTermsIn",
        "BusinessChainSearchTermsOut": "_displayvideo_253_BusinessChainSearchTermsOut",
        "YoutubeAndPartnersSettingsIn": "_displayvideo_254_YoutubeAndPartnersSettingsIn",
        "YoutubeAndPartnersSettingsOut": "_displayvideo_255_YoutubeAndPartnersSettingsOut",
        "GenderAssignedTargetingOptionDetailsIn": "_displayvideo_256_GenderAssignedTargetingOptionDetailsIn",
        "GenderAssignedTargetingOptionDetailsOut": "_displayvideo_257_GenderAssignedTargetingOptionDetailsOut",
        "VideoAdSequenceSettingsIn": "_displayvideo_258_VideoAdSequenceSettingsIn",
        "VideoAdSequenceSettingsOut": "_displayvideo_259_VideoAdSequenceSettingsOut",
        "OperatingSystemAssignedTargetingOptionDetailsIn": "_displayvideo_260_OperatingSystemAssignedTargetingOptionDetailsIn",
        "OperatingSystemAssignedTargetingOptionDetailsOut": "_displayvideo_261_OperatingSystemAssignedTargetingOptionDetailsOut",
        "MobileAppIn": "_displayvideo_262_MobileAppIn",
        "MobileAppOut": "_displayvideo_263_MobileAppOut",
        "CreateAssignedTargetingOptionsRequestIn": "_displayvideo_264_CreateAssignedTargetingOptionsRequestIn",
        "CreateAssignedTargetingOptionsRequestOut": "_displayvideo_265_CreateAssignedTargetingOptionsRequestOut",
        "CreativeIn": "_displayvideo_266_CreativeIn",
        "CreativeOut": "_displayvideo_267_CreativeOut",
        "MobileDeviceIdListIn": "_displayvideo_268_MobileDeviceIdListIn",
        "MobileDeviceIdListOut": "_displayvideo_269_MobileDeviceIdListOut",
        "MoneyIn": "_displayvideo_270_MoneyIn",
        "MoneyOut": "_displayvideo_271_MoneyOut",
        "ReplaceSitesResponseIn": "_displayvideo_272_ReplaceSitesResponseIn",
        "ReplaceSitesResponseOut": "_displayvideo_273_ReplaceSitesResponseOut",
        "SensitiveCategoryAssignedTargetingOptionDetailsIn": "_displayvideo_274_SensitiveCategoryAssignedTargetingOptionDetailsIn",
        "SensitiveCategoryAssignedTargetingOptionDetailsOut": "_displayvideo_275_SensitiveCategoryAssignedTargetingOptionDetailsOut",
        "PartnerIn": "_displayvideo_276_PartnerIn",
        "PartnerOut": "_displayvideo_277_PartnerOut",
        "BulkListCampaignAssignedTargetingOptionsResponseIn": "_displayvideo_278_BulkListCampaignAssignedTargetingOptionsResponseIn",
        "BulkListCampaignAssignedTargetingOptionsResponseOut": "_displayvideo_279_BulkListCampaignAssignedTargetingOptionsResponseOut",
        "ContentDurationTargetingOptionDetailsIn": "_displayvideo_280_ContentDurationTargetingOptionDetailsIn",
        "ContentDurationTargetingOptionDetailsOut": "_displayvideo_281_ContentDurationTargetingOptionDetailsOut",
        "AdUrlIn": "_displayvideo_282_AdUrlIn",
        "AdUrlOut": "_displayvideo_283_AdUrlOut",
        "CustomLabelIn": "_displayvideo_284_CustomLabelIn",
        "CustomLabelOut": "_displayvideo_285_CustomLabelOut",
        "LanguageAssignedTargetingOptionDetailsIn": "_displayvideo_286_LanguageAssignedTargetingOptionDetailsIn",
        "LanguageAssignedTargetingOptionDetailsOut": "_displayvideo_287_LanguageAssignedTargetingOptionDetailsOut",
        "InsertionOrderBudgetSegmentIn": "_displayvideo_288_InsertionOrderBudgetSegmentIn",
        "InsertionOrderBudgetSegmentOut": "_displayvideo_289_InsertionOrderBudgetSegmentOut",
        "AssetAssociationIn": "_displayvideo_290_AssetAssociationIn",
        "AssetAssociationOut": "_displayvideo_291_AssetAssociationOut",
        "DateIn": "_displayvideo_292_DateIn",
        "DateOut": "_displayvideo_293_DateOut",
        "ListCustomBiddingScriptsResponseIn": "_displayvideo_294_ListCustomBiddingScriptsResponseIn",
        "ListCustomBiddingScriptsResponseOut": "_displayvideo_295_ListCustomBiddingScriptsResponseOut",
        "CmHybridConfigIn": "_displayvideo_296_CmHybridConfigIn",
        "CmHybridConfigOut": "_displayvideo_297_CmHybridConfigOut",
        "PoiTargetingOptionDetailsIn": "_displayvideo_298_PoiTargetingOptionDetailsIn",
        "PoiTargetingOptionDetailsOut": "_displayvideo_299_PoiTargetingOptionDetailsOut",
        "InsertionOrderBudgetIn": "_displayvideo_300_InsertionOrderBudgetIn",
        "InsertionOrderBudgetOut": "_displayvideo_301_InsertionOrderBudgetOut",
        "EditGuaranteedOrderReadAccessorsResponseIn": "_displayvideo_302_EditGuaranteedOrderReadAccessorsResponseIn",
        "EditGuaranteedOrderReadAccessorsResponseOut": "_displayvideo_303_EditGuaranteedOrderReadAccessorsResponseOut",
        "BulkEditNegativeKeywordsRequestIn": "_displayvideo_304_BulkEditNegativeKeywordsRequestIn",
        "BulkEditNegativeKeywordsRequestOut": "_displayvideo_305_BulkEditNegativeKeywordsRequestOut",
        "AuthorizedSellerStatusTargetingOptionDetailsIn": "_displayvideo_306_AuthorizedSellerStatusTargetingOptionDetailsIn",
        "AuthorizedSellerStatusTargetingOptionDetailsOut": "_displayvideo_307_AuthorizedSellerStatusTargetingOptionDetailsOut",
        "AudioVideoOffsetIn": "_displayvideo_308_AudioVideoOffsetIn",
        "AudioVideoOffsetOut": "_displayvideo_309_AudioVideoOffsetOut",
        "EnvironmentAssignedTargetingOptionDetailsIn": "_displayvideo_310_EnvironmentAssignedTargetingOptionDetailsIn",
        "EnvironmentAssignedTargetingOptionDetailsOut": "_displayvideo_311_EnvironmentAssignedTargetingOptionDetailsOut",
        "GenderTargetingOptionDetailsIn": "_displayvideo_312_GenderTargetingOptionDetailsIn",
        "GenderTargetingOptionDetailsOut": "_displayvideo_313_GenderTargetingOptionDetailsOut",
        "SessionPositionAssignedTargetingOptionDetailsIn": "_displayvideo_314_SessionPositionAssignedTargetingOptionDetailsIn",
        "SessionPositionAssignedTargetingOptionDetailsOut": "_displayvideo_315_SessionPositionAssignedTargetingOptionDetailsOut",
        "AppCategoryAssignedTargetingOptionDetailsIn": "_displayvideo_316_AppCategoryAssignedTargetingOptionDetailsIn",
        "AppCategoryAssignedTargetingOptionDetailsOut": "_displayvideo_317_AppCategoryAssignedTargetingOptionDetailsOut",
        "DoubleVerifyVideoViewabilityIn": "_displayvideo_318_DoubleVerifyVideoViewabilityIn",
        "DoubleVerifyVideoViewabilityOut": "_displayvideo_319_DoubleVerifyVideoViewabilityOut",
        "AgeRangeAssignedTargetingOptionDetailsIn": "_displayvideo_320_AgeRangeAssignedTargetingOptionDetailsIn",
        "AgeRangeAssignedTargetingOptionDetailsOut": "_displayvideo_321_AgeRangeAssignedTargetingOptionDetailsOut",
        "NegativeKeywordIn": "_displayvideo_322_NegativeKeywordIn",
        "NegativeKeywordOut": "_displayvideo_323_NegativeKeywordOut",
        "StatusIn": "_displayvideo_324_StatusIn",
        "StatusOut": "_displayvideo_325_StatusOut",
        "MastheadAdIn": "_displayvideo_326_MastheadAdIn",
        "MastheadAdOut": "_displayvideo_327_MastheadAdOut",
        "ReviewStatusInfoIn": "_displayvideo_328_ReviewStatusInfoIn",
        "ReviewStatusInfoOut": "_displayvideo_329_ReviewStatusInfoOut",
        "ListNegativeKeywordsResponseIn": "_displayvideo_330_ListNegativeKeywordsResponseIn",
        "ListNegativeKeywordsResponseOut": "_displayvideo_331_ListNegativeKeywordsResponseOut",
        "ViewabilityTargetingOptionDetailsIn": "_displayvideo_332_ViewabilityTargetingOptionDetailsIn",
        "ViewabilityTargetingOptionDetailsOut": "_displayvideo_333_ViewabilityTargetingOptionDetailsOut",
        "OmidTargetingOptionDetailsIn": "_displayvideo_334_OmidTargetingOptionDetailsIn",
        "OmidTargetingOptionDetailsOut": "_displayvideo_335_OmidTargetingOptionDetailsOut",
        "ContentInstreamPositionAssignedTargetingOptionDetailsIn": "_displayvideo_336_ContentInstreamPositionAssignedTargetingOptionDetailsIn",
        "ContentInstreamPositionAssignedTargetingOptionDetailsOut": "_displayvideo_337_ContentInstreamPositionAssignedTargetingOptionDetailsOut",
        "ContentDurationAssignedTargetingOptionDetailsIn": "_displayvideo_338_ContentDurationAssignedTargetingOptionDetailsIn",
        "ContentDurationAssignedTargetingOptionDetailsOut": "_displayvideo_339_ContentDurationAssignedTargetingOptionDetailsOut",
        "BulkEditNegativeKeywordsResponseIn": "_displayvideo_340_BulkEditNegativeKeywordsResponseIn",
        "BulkEditNegativeKeywordsResponseOut": "_displayvideo_341_BulkEditNegativeKeywordsResponseOut",
        "ActiveViewVideoViewabilityMetricConfigIn": "_displayvideo_342_ActiveViewVideoViewabilityMetricConfigIn",
        "ActiveViewVideoViewabilityMetricConfigOut": "_displayvideo_343_ActiveViewVideoViewabilityMetricConfigOut",
        "ParentalStatusAssignedTargetingOptionDetailsIn": "_displayvideo_344_ParentalStatusAssignedTargetingOptionDetailsIn",
        "ParentalStatusAssignedTargetingOptionDetailsOut": "_displayvideo_345_ParentalStatusAssignedTargetingOptionDetailsOut",
        "LookupInvoiceCurrencyResponseIn": "_displayvideo_346_LookupInvoiceCurrencyResponseIn",
        "LookupInvoiceCurrencyResponseOut": "_displayvideo_347_LookupInvoiceCurrencyResponseOut",
        "LineItemIn": "_displayvideo_348_LineItemIn",
        "LineItemOut": "_displayvideo_349_LineItemOut",
        "ParentEntityFilterIn": "_displayvideo_350_ParentEntityFilterIn",
        "ParentEntityFilterOut": "_displayvideo_351_ParentEntityFilterOut",
        "ObaIconIn": "_displayvideo_352_ObaIconIn",
        "ObaIconOut": "_displayvideo_353_ObaIconOut",
        "BrowserAssignedTargetingOptionDetailsIn": "_displayvideo_354_BrowserAssignedTargetingOptionDetailsIn",
        "BrowserAssignedTargetingOptionDetailsOut": "_displayvideo_355_BrowserAssignedTargetingOptionDetailsOut",
        "AssignedLocationIn": "_displayvideo_356_AssignedLocationIn",
        "AssignedLocationOut": "_displayvideo_357_AssignedLocationOut",
        "TargetingExpansionConfigIn": "_displayvideo_358_TargetingExpansionConfigIn",
        "TargetingExpansionConfigOut": "_displayvideo_359_TargetingExpansionConfigOut",
        "ListCustomBiddingAlgorithmsResponseIn": "_displayvideo_360_ListCustomBiddingAlgorithmsResponseIn",
        "ListCustomBiddingAlgorithmsResponseOut": "_displayvideo_361_ListCustomBiddingAlgorithmsResponseOut",
        "ConversionCountingConfigIn": "_displayvideo_362_ConversionCountingConfigIn",
        "ConversionCountingConfigOut": "_displayvideo_363_ConversionCountingConfigOut",
        "OmidAssignedTargetingOptionDetailsIn": "_displayvideo_364_OmidAssignedTargetingOptionDetailsIn",
        "OmidAssignedTargetingOptionDetailsOut": "_displayvideo_365_OmidAssignedTargetingOptionDetailsOut",
        "AudioContentTypeTargetingOptionDetailsIn": "_displayvideo_366_AudioContentTypeTargetingOptionDetailsIn",
        "AudioContentTypeTargetingOptionDetailsOut": "_displayvideo_367_AudioContentTypeTargetingOptionDetailsOut",
        "ContentOutstreamPositionTargetingOptionDetailsIn": "_displayvideo_368_ContentOutstreamPositionTargetingOptionDetailsIn",
        "ContentOutstreamPositionTargetingOptionDetailsOut": "_displayvideo_369_ContentOutstreamPositionTargetingOptionDetailsOut",
        "VideoDiscoveryAdIn": "_displayvideo_370_VideoDiscoveryAdIn",
        "VideoDiscoveryAdOut": "_displayvideo_371_VideoDiscoveryAdOut",
        "ListGoogleAudiencesResponseIn": "_displayvideo_372_ListGoogleAudiencesResponseIn",
        "ListGoogleAudiencesResponseOut": "_displayvideo_373_ListGoogleAudiencesResponseOut",
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn": "_displayvideo_374_EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn",
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut": "_displayvideo_375_EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut",
        "UserIn": "_displayvideo_376_UserIn",
        "UserOut": "_displayvideo_377_UserOut",
        "InventorySourceDisplayCreativeConfigIn": "_displayvideo_378_InventorySourceDisplayCreativeConfigIn",
        "InventorySourceDisplayCreativeConfigOut": "_displayvideo_379_InventorySourceDisplayCreativeConfigOut",
        "ListYoutubeAdGroupsResponseIn": "_displayvideo_380_ListYoutubeAdGroupsResponseIn",
        "ListYoutubeAdGroupsResponseOut": "_displayvideo_381_ListYoutubeAdGroupsResponseOut",
        "VideoPlayerSizeAssignedTargetingOptionDetailsIn": "_displayvideo_382_VideoPlayerSizeAssignedTargetingOptionDetailsIn",
        "VideoPlayerSizeAssignedTargetingOptionDetailsOut": "_displayvideo_383_VideoPlayerSizeAssignedTargetingOptionDetailsOut",
        "AppAssignedTargetingOptionDetailsIn": "_displayvideo_384_AppAssignedTargetingOptionDetailsIn",
        "AppAssignedTargetingOptionDetailsOut": "_displayvideo_385_AppAssignedTargetingOptionDetailsOut",
        "BulkEditAdvertiserAssignedTargetingOptionsRequestIn": "_displayvideo_386_BulkEditAdvertiserAssignedTargetingOptionsRequestIn",
        "BulkEditAdvertiserAssignedTargetingOptionsRequestOut": "_displayvideo_387_BulkEditAdvertiserAssignedTargetingOptionsRequestOut",
        "ExchangeReviewStatusIn": "_displayvideo_388_ExchangeReviewStatusIn",
        "ExchangeReviewStatusOut": "_displayvideo_389_ExchangeReviewStatusOut",
        "CategoryAssignedTargetingOptionDetailsIn": "_displayvideo_390_CategoryAssignedTargetingOptionDetailsIn",
        "CategoryAssignedTargetingOptionDetailsOut": "_displayvideo_391_CategoryAssignedTargetingOptionDetailsOut",
        "SearchTargetingOptionsResponseIn": "_displayvideo_392_SearchTargetingOptionsResponseIn",
        "SearchTargetingOptionsResponseOut": "_displayvideo_393_SearchTargetingOptionsResponseOut",
        "LineItemBudgetIn": "_displayvideo_394_LineItemBudgetIn",
        "LineItemBudgetOut": "_displayvideo_395_LineItemBudgetOut",
        "PrismaCpeCodeIn": "_displayvideo_396_PrismaCpeCodeIn",
        "PrismaCpeCodeOut": "_displayvideo_397_PrismaCpeCodeOut",
        "VideoAdSequenceStepIn": "_displayvideo_398_VideoAdSequenceStepIn",
        "VideoAdSequenceStepOut": "_displayvideo_399_VideoAdSequenceStepOut",
        "YoutubeAndPartnersInventorySourceConfigIn": "_displayvideo_400_YoutubeAndPartnersInventorySourceConfigIn",
        "YoutubeAndPartnersInventorySourceConfigOut": "_displayvideo_401_YoutubeAndPartnersInventorySourceConfigOut",
        "MaximizeSpendBidStrategyIn": "_displayvideo_402_MaximizeSpendBidStrategyIn",
        "MaximizeSpendBidStrategyOut": "_displayvideo_403_MaximizeSpendBidStrategyOut",
        "AgeRangeTargetingOptionDetailsIn": "_displayvideo_404_AgeRangeTargetingOptionDetailsIn",
        "AgeRangeTargetingOptionDetailsOut": "_displayvideo_405_AgeRangeTargetingOptionDetailsOut",
        "YoutubeAndPartnersThirdPartyMeasurementSettingsIn": "_displayvideo_406_YoutubeAndPartnersThirdPartyMeasurementSettingsIn",
        "YoutubeAndPartnersThirdPartyMeasurementSettingsOut": "_displayvideo_407_YoutubeAndPartnersThirdPartyMeasurementSettingsOut",
        "GenerateDefaultLineItemRequestIn": "_displayvideo_408_GenerateDefaultLineItemRequestIn",
        "GenerateDefaultLineItemRequestOut": "_displayvideo_409_GenerateDefaultLineItemRequestOut",
        "GuaranteedOrderIn": "_displayvideo_410_GuaranteedOrderIn",
        "GuaranteedOrderOut": "_displayvideo_411_GuaranteedOrderOut",
        "DeactivateManualTriggerRequestIn": "_displayvideo_412_DeactivateManualTriggerRequestIn",
        "DeactivateManualTriggerRequestOut": "_displayvideo_413_DeactivateManualTriggerRequestOut",
        "DeviceMakeModelAssignedTargetingOptionDetailsIn": "_displayvideo_414_DeviceMakeModelAssignedTargetingOptionDetailsIn",
        "DeviceMakeModelAssignedTargetingOptionDetailsOut": "_displayvideo_415_DeviceMakeModelAssignedTargetingOptionDetailsOut",
        "ThirdPartyOnlyConfigIn": "_displayvideo_416_ThirdPartyOnlyConfigIn",
        "ThirdPartyOnlyConfigOut": "_displayvideo_417_ThirdPartyOnlyConfigOut",
        "CombinedAudienceTargetingSettingIn": "_displayvideo_418_CombinedAudienceTargetingSettingIn",
        "CombinedAudienceTargetingSettingOut": "_displayvideo_419_CombinedAudienceTargetingSettingOut",
        "SubExchangeAssignedTargetingOptionDetailsIn": "_displayvideo_420_SubExchangeAssignedTargetingOptionDetailsIn",
        "SubExchangeAssignedTargetingOptionDetailsOut": "_displayvideo_421_SubExchangeAssignedTargetingOptionDetailsOut",
        "ListCampaignAssignedTargetingOptionsResponseIn": "_displayvideo_422_ListCampaignAssignedTargetingOptionsResponseIn",
        "ListCampaignAssignedTargetingOptionsResponseOut": "_displayvideo_423_ListCampaignAssignedTargetingOptionsResponseOut",
        "ListPartnersResponseIn": "_displayvideo_424_ListPartnersResponseIn",
        "ListPartnersResponseOut": "_displayvideo_425_ListPartnersResponseOut",
        "IntegrationDetailsIn": "_displayvideo_426_IntegrationDetailsIn",
        "IntegrationDetailsOut": "_displayvideo_427_IntegrationDetailsOut",
        "ListTargetingOptionsResponseIn": "_displayvideo_428_ListTargetingOptionsResponseIn",
        "ListTargetingOptionsResponseOut": "_displayvideo_429_ListTargetingOptionsResponseOut",
        "HouseholdIncomeAssignedTargetingOptionDetailsIn": "_displayvideo_430_HouseholdIncomeAssignedTargetingOptionDetailsIn",
        "HouseholdIncomeAssignedTargetingOptionDetailsOut": "_displayvideo_431_HouseholdIncomeAssignedTargetingOptionDetailsOut",
        "TimerEventIn": "_displayvideo_432_TimerEventIn",
        "TimerEventOut": "_displayvideo_433_TimerEventOut",
        "BulkEditSitesRequestIn": "_displayvideo_434_BulkEditSitesRequestIn",
        "BulkEditSitesRequestOut": "_displayvideo_435_BulkEditSitesRequestOut",
        "InventorySourceIn": "_displayvideo_436_InventorySourceIn",
        "InventorySourceOut": "_displayvideo_437_InventorySourceOut",
        "ContentOutstreamPositionAssignedTargetingOptionDetailsIn": "_displayvideo_438_ContentOutstreamPositionAssignedTargetingOptionDetailsIn",
        "ContentOutstreamPositionAssignedTargetingOptionDetailsOut": "_displayvideo_439_ContentOutstreamPositionAssignedTargetingOptionDetailsOut",
        "ListLineItemsResponseIn": "_displayvideo_440_ListLineItemsResponseIn",
        "ListLineItemsResponseOut": "_displayvideo_441_ListLineItemsResponseOut",
        "AdvertiserTargetingConfigIn": "_displayvideo_442_AdvertiserTargetingConfigIn",
        "AdvertiserTargetingConfigOut": "_displayvideo_443_AdvertiserTargetingConfigOut",
        "BulkListInsertionOrderAssignedTargetingOptionsResponseIn": "_displayvideo_444_BulkListInsertionOrderAssignedTargetingOptionsResponseIn",
        "BulkListInsertionOrderAssignedTargetingOptionsResponseOut": "_displayvideo_445_BulkListInsertionOrderAssignedTargetingOptionsResponseOut",
        "CmTrackingAdIn": "_displayvideo_446_CmTrackingAdIn",
        "CmTrackingAdOut": "_displayvideo_447_CmTrackingAdOut",
        "BulkUpdateLineItemsRequestIn": "_displayvideo_448_BulkUpdateLineItemsRequestIn",
        "BulkUpdateLineItemsRequestOut": "_displayvideo_449_BulkUpdateLineItemsRequestOut",
        "VideoPerformanceAdIn": "_displayvideo_450_VideoPerformanceAdIn",
        "VideoPerformanceAdOut": "_displayvideo_451_VideoPerformanceAdOut",
        "AdvertiserDataAccessConfigIn": "_displayvideo_452_AdvertiserDataAccessConfigIn",
        "AdvertiserDataAccessConfigOut": "_displayvideo_453_AdvertiserDataAccessConfigOut",
        "FrequencyCapIn": "_displayvideo_454_FrequencyCapIn",
        "FrequencyCapOut": "_displayvideo_455_FrequencyCapOut",
        "ListSitesResponseIn": "_displayvideo_456_ListSitesResponseIn",
        "ListSitesResponseOut": "_displayvideo_457_ListSitesResponseOut",
        "AdvertiserBillingConfigIn": "_displayvideo_458_AdvertiserBillingConfigIn",
        "AdvertiserBillingConfigOut": "_displayvideo_459_AdvertiserBillingConfigOut",
        "ListInsertionOrdersResponseIn": "_displayvideo_460_ListInsertionOrdersResponseIn",
        "ListInsertionOrdersResponseOut": "_displayvideo_461_ListInsertionOrdersResponseOut",
        "ManualTriggerIn": "_displayvideo_462_ManualTriggerIn",
        "ManualTriggerOut": "_displayvideo_463_ManualTriggerOut",
        "AdvertiserCreativeConfigIn": "_displayvideo_464_AdvertiserCreativeConfigIn",
        "AdvertiserCreativeConfigOut": "_displayvideo_465_AdvertiserCreativeConfigOut",
        "ExchangeTargetingOptionDetailsIn": "_displayvideo_466_ExchangeTargetingOptionDetailsIn",
        "ExchangeTargetingOptionDetailsOut": "_displayvideo_467_ExchangeTargetingOptionDetailsOut",
        "PartnerDataAccessConfigIn": "_displayvideo_468_PartnerDataAccessConfigIn",
        "PartnerDataAccessConfigOut": "_displayvideo_469_PartnerDataAccessConfigOut",
        "DuplicateLineItemRequestIn": "_displayvideo_470_DuplicateLineItemRequestIn",
        "DuplicateLineItemRequestOut": "_displayvideo_471_DuplicateLineItemRequestOut",
        "BudgetSummaryIn": "_displayvideo_472_BudgetSummaryIn",
        "BudgetSummaryOut": "_displayvideo_473_BudgetSummaryOut",
        "CampaignGoalIn": "_displayvideo_474_CampaignGoalIn",
        "CampaignGoalOut": "_displayvideo_475_CampaignGoalOut",
        "CarrierAndIspAssignedTargetingOptionDetailsIn": "_displayvideo_476_CarrierAndIspAssignedTargetingOptionDetailsIn",
        "CarrierAndIspAssignedTargetingOptionDetailsOut": "_displayvideo_477_CarrierAndIspAssignedTargetingOptionDetailsOut",
        "CommonInStreamAttributeIn": "_displayvideo_478_CommonInStreamAttributeIn",
        "CommonInStreamAttributeOut": "_displayvideo_479_CommonInStreamAttributeOut",
        "AdvertiserAdServerConfigIn": "_displayvideo_480_AdvertiserAdServerConfigIn",
        "AdvertiserAdServerConfigOut": "_displayvideo_481_AdvertiserAdServerConfigOut",
        "KeywordAssignedTargetingOptionDetailsIn": "_displayvideo_482_KeywordAssignedTargetingOptionDetailsIn",
        "KeywordAssignedTargetingOptionDetailsOut": "_displayvideo_483_KeywordAssignedTargetingOptionDetailsOut",
        "ViewabilityAssignedTargetingOptionDetailsIn": "_displayvideo_484_ViewabilityAssignedTargetingOptionDetailsIn",
        "ViewabilityAssignedTargetingOptionDetailsOut": "_displayvideo_485_ViewabilityAssignedTargetingOptionDetailsOut",
        "ListInvoicesResponseIn": "_displayvideo_486_ListInvoicesResponseIn",
        "ListInvoicesResponseOut": "_displayvideo_487_ListInvoicesResponseOut",
        "AdvertiserSdfConfigIn": "_displayvideo_488_AdvertiserSdfConfigIn",
        "AdvertiserSdfConfigOut": "_displayvideo_489_AdvertiserSdfConfigOut",
        "ProductFeedDataIn": "_displayvideo_490_ProductFeedDataIn",
        "ProductFeedDataOut": "_displayvideo_491_ProductFeedDataOut",
        "CustomBiddingScriptRefIn": "_displayvideo_492_CustomBiddingScriptRefIn",
        "CustomBiddingScriptRefOut": "_displayvideo_493_CustomBiddingScriptRefOut",
        "ActivateManualTriggerRequestIn": "_displayvideo_494_ActivateManualTriggerRequestIn",
        "ActivateManualTriggerRequestOut": "_displayvideo_495_ActivateManualTriggerRequestOut",
        "ContactInfoIn": "_displayvideo_496_ContactInfoIn",
        "ContactInfoOut": "_displayvideo_497_ContactInfoOut",
        "IntegralAdScienceIn": "_displayvideo_498_IntegralAdScienceIn",
        "IntegralAdScienceOut": "_displayvideo_499_IntegralAdScienceOut",
        "DeleteAssignedTargetingOptionsRequestIn": "_displayvideo_500_DeleteAssignedTargetingOptionsRequestIn",
        "DeleteAssignedTargetingOptionsRequestOut": "_displayvideo_501_DeleteAssignedTargetingOptionsRequestOut",
        "AuthorizedSellerStatusAssignedTargetingOptionDetailsIn": "_displayvideo_502_AuthorizedSellerStatusAssignedTargetingOptionDetailsIn",
        "AuthorizedSellerStatusAssignedTargetingOptionDetailsOut": "_displayvideo_503_AuthorizedSellerStatusAssignedTargetingOptionDetailsOut",
        "DoubleVerifyFraudInvalidTrafficIn": "_displayvideo_504_DoubleVerifyFraudInvalidTrafficIn",
        "DoubleVerifyFraudInvalidTrafficOut": "_displayvideo_505_DoubleVerifyFraudInvalidTrafficOut",
        "YoutubeAdGroupIn": "_displayvideo_506_YoutubeAdGroupIn",
        "YoutubeAdGroupOut": "_displayvideo_507_YoutubeAdGroupOut",
        "AssignedUserRoleIn": "_displayvideo_508_AssignedUserRoleIn",
        "AssignedUserRoleOut": "_displayvideo_509_AssignedUserRoleOut",
        "PerformanceGoalIn": "_displayvideo_510_PerformanceGoalIn",
        "PerformanceGoalOut": "_displayvideo_511_PerformanceGoalOut",
        "CampaignFlightIn": "_displayvideo_512_CampaignFlightIn",
        "CampaignFlightOut": "_displayvideo_513_CampaignFlightOut",
        "LocationListIn": "_displayvideo_514_LocationListIn",
        "LocationListOut": "_displayvideo_515_LocationListOut",
        "ContentStreamTypeAssignedTargetingOptionDetailsIn": "_displayvideo_516_ContentStreamTypeAssignedTargetingOptionDetailsIn",
        "ContentStreamTypeAssignedTargetingOptionDetailsOut": "_displayvideo_517_ContentStreamTypeAssignedTargetingOptionDetailsOut",
        "CategoryTargetingOptionDetailsIn": "_displayvideo_518_CategoryTargetingOptionDetailsIn",
        "CategoryTargetingOptionDetailsOut": "_displayvideo_519_CategoryTargetingOptionDetailsOut",
        "HouseholdIncomeTargetingOptionDetailsIn": "_displayvideo_520_HouseholdIncomeTargetingOptionDetailsIn",
        "HouseholdIncomeTargetingOptionDetailsOut": "_displayvideo_521_HouseholdIncomeTargetingOptionDetailsOut",
        "AuditAdvertiserResponseIn": "_displayvideo_522_AuditAdvertiserResponseIn",
        "AuditAdvertiserResponseOut": "_displayvideo_523_AuditAdvertiserResponseOut",
        "BulkListAssignedTargetingOptionsResponseIn": "_displayvideo_524_BulkListAssignedTargetingOptionsResponseIn",
        "BulkListAssignedTargetingOptionsResponseOut": "_displayvideo_525_BulkListAssignedTargetingOptionsResponseOut",
        "ThirdPartyVerifierAssignedTargetingOptionDetailsIn": "_displayvideo_526_ThirdPartyVerifierAssignedTargetingOptionDetailsIn",
        "ThirdPartyVerifierAssignedTargetingOptionDetailsOut": "_displayvideo_527_ThirdPartyVerifierAssignedTargetingOptionDetailsOut",
        "BusinessChainTargetingOptionDetailsIn": "_displayvideo_528_BusinessChainTargetingOptionDetailsIn",
        "BusinessChainTargetingOptionDetailsOut": "_displayvideo_529_BusinessChainTargetingOptionDetailsOut",
        "DeviceTypeAssignedTargetingOptionDetailsIn": "_displayvideo_530_DeviceTypeAssignedTargetingOptionDetailsIn",
        "DeviceTypeAssignedTargetingOptionDetailsOut": "_displayvideo_531_DeviceTypeAssignedTargetingOptionDetailsOut",
        "ExchangeConfigIn": "_displayvideo_532_ExchangeConfigIn",
        "ExchangeConfigOut": "_displayvideo_533_ExchangeConfigOut",
        "VideoPlayerSizeTargetingOptionDetailsIn": "_displayvideo_534_VideoPlayerSizeTargetingOptionDetailsIn",
        "VideoPlayerSizeTargetingOptionDetailsOut": "_displayvideo_535_VideoPlayerSizeTargetingOptionDetailsOut",
        "ListAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_536_ListAdvertiserAssignedTargetingOptionsResponseIn",
        "ListAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_537_ListAdvertiserAssignedTargetingOptionsResponseOut",
        "ThirdPartyVendorConfigIn": "_displayvideo_538_ThirdPartyVendorConfigIn",
        "ThirdPartyVendorConfigOut": "_displayvideo_539_ThirdPartyVendorConfigOut",
        "ListInventorySourceGroupsResponseIn": "_displayvideo_540_ListInventorySourceGroupsResponseIn",
        "ListInventorySourceGroupsResponseOut": "_displayvideo_541_ListInventorySourceGroupsResponseOut",
        "DisplayVideoSourceAdIn": "_displayvideo_542_DisplayVideoSourceAdIn",
        "DisplayVideoSourceAdOut": "_displayvideo_543_DisplayVideoSourceAdOut",
        "NonSkippableAdIn": "_displayvideo_544_NonSkippableAdIn",
        "NonSkippableAdOut": "_displayvideo_545_NonSkippableAdOut",
        "DoubleVerifyAppStarRatingIn": "_displayvideo_546_DoubleVerifyAppStarRatingIn",
        "DoubleVerifyAppStarRatingOut": "_displayvideo_547_DoubleVerifyAppStarRatingOut",
        "TargetingOptionIn": "_displayvideo_548_TargetingOptionIn",
        "TargetingOptionOut": "_displayvideo_549_TargetingOptionOut",
        "CreativeConfigIn": "_displayvideo_550_CreativeConfigIn",
        "CreativeConfigOut": "_displayvideo_551_CreativeConfigOut",
        "ListLineItemAssignedTargetingOptionsResponseIn": "_displayvideo_552_ListLineItemAssignedTargetingOptionsResponseIn",
        "ListLineItemAssignedTargetingOptionsResponseOut": "_displayvideo_553_ListLineItemAssignedTargetingOptionsResponseOut",
        "BulkEditAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_554_BulkEditAdvertiserAssignedTargetingOptionsResponseIn",
        "BulkEditAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_555_BulkEditAdvertiserAssignedTargetingOptionsResponseOut",
        "AudioContentTypeAssignedTargetingOptionDetailsIn": "_displayvideo_556_AudioContentTypeAssignedTargetingOptionDetailsIn",
        "AudioContentTypeAssignedTargetingOptionDetailsOut": "_displayvideo_557_AudioContentTypeAssignedTargetingOptionDetailsOut",
        "BiddingStrategyIn": "_displayvideo_558_BiddingStrategyIn",
        "BiddingStrategyOut": "_displayvideo_559_BiddingStrategyOut",
        "BulkUpdateLineItemsResponseIn": "_displayvideo_560_BulkUpdateLineItemsResponseIn",
        "BulkUpdateLineItemsResponseOut": "_displayvideo_561_BulkUpdateLineItemsResponseOut",
        "AppCategoryTargetingOptionDetailsIn": "_displayvideo_562_AppCategoryTargetingOptionDetailsIn",
        "AppCategoryTargetingOptionDetailsOut": "_displayvideo_563_AppCategoryTargetingOptionDetailsOut",
        "DateRangeIn": "_displayvideo_564_DateRangeIn",
        "DateRangeOut": "_displayvideo_565_DateRangeOut",
        "ListCustomListsResponseIn": "_displayvideo_566_ListCustomListsResponseIn",
        "ListCustomListsResponseOut": "_displayvideo_567_ListCustomListsResponseOut",
        "InvoiceIn": "_displayvideo_568_InvoiceIn",
        "InvoiceOut": "_displayvideo_569_InvoiceOut",
        "PartnerAdServerConfigIn": "_displayvideo_570_PartnerAdServerConfigIn",
        "PartnerAdServerConfigOut": "_displayvideo_571_PartnerAdServerConfigOut",
        "PartnerCostIn": "_displayvideo_572_PartnerCostIn",
        "PartnerCostOut": "_displayvideo_573_PartnerCostOut",
        "CounterEventIn": "_displayvideo_574_CounterEventIn",
        "CounterEventOut": "_displayvideo_575_CounterEventOut",
        "InventorySourceFilterIn": "_displayvideo_576_InventorySourceFilterIn",
        "InventorySourceFilterOut": "_displayvideo_577_InventorySourceFilterOut",
        "YoutubeVideoAssignedTargetingOptionDetailsIn": "_displayvideo_578_YoutubeVideoAssignedTargetingOptionDetailsIn",
        "YoutubeVideoAssignedTargetingOptionDetailsOut": "_displayvideo_579_YoutubeVideoAssignedTargetingOptionDetailsOut",
        "CampaignIn": "_displayvideo_580_CampaignIn",
        "CampaignOut": "_displayvideo_581_CampaignOut",
        "PartnerRevenueModelIn": "_displayvideo_582_PartnerRevenueModelIn",
        "PartnerRevenueModelOut": "_displayvideo_583_PartnerRevenueModelOut",
        "AudienceGroupAssignedTargetingOptionDetailsIn": "_displayvideo_584_AudienceGroupAssignedTargetingOptionDetailsIn",
        "AudienceGroupAssignedTargetingOptionDetailsOut": "_displayvideo_585_AudienceGroupAssignedTargetingOptionDetailsOut",
        "CustomListTargetingSettingIn": "_displayvideo_586_CustomListTargetingSettingIn",
        "CustomListTargetingSettingOut": "_displayvideo_587_CustomListTargetingSettingOut",
        "ListAssignedLocationsResponseIn": "_displayvideo_588_ListAssignedLocationsResponseIn",
        "ListAssignedLocationsResponseOut": "_displayvideo_589_ListAssignedLocationsResponseOut",
        "RateDetailsIn": "_displayvideo_590_RateDetailsIn",
        "RateDetailsOut": "_displayvideo_591_RateDetailsOut",
        "BulkEditPartnerAssignedTargetingOptionsResponseIn": "_displayvideo_592_BulkEditPartnerAssignedTargetingOptionsResponseIn",
        "BulkEditPartnerAssignedTargetingOptionsResponseOut": "_displayvideo_593_BulkEditPartnerAssignedTargetingOptionsResponseOut",
        "EditInventorySourceReadWriteAccessorsRequestIn": "_displayvideo_594_EditInventorySourceReadWriteAccessorsRequestIn",
        "EditInventorySourceReadWriteAccessorsRequestOut": "_displayvideo_595_EditInventorySourceReadWriteAccessorsRequestOut",
        "BulkEditAssignedInventorySourcesResponseIn": "_displayvideo_596_BulkEditAssignedInventorySourcesResponseIn",
        "BulkEditAssignedInventorySourcesResponseOut": "_displayvideo_597_BulkEditAssignedInventorySourcesResponseOut",
        "InventorySourceGroupAssignedTargetingOptionDetailsIn": "_displayvideo_598_InventorySourceGroupAssignedTargetingOptionDetailsIn",
        "InventorySourceGroupAssignedTargetingOptionDetailsOut": "_displayvideo_599_InventorySourceGroupAssignedTargetingOptionDetailsOut",
        "OperatingSystemTargetingOptionDetailsIn": "_displayvideo_600_OperatingSystemTargetingOptionDetailsIn",
        "OperatingSystemTargetingOptionDetailsOut": "_displayvideo_601_OperatingSystemTargetingOptionDetailsOut",
        "ReplaceSitesRequestIn": "_displayvideo_602_ReplaceSitesRequestIn",
        "ReplaceSitesRequestOut": "_displayvideo_603_ReplaceSitesRequestOut",
        "CreateAssetResponseIn": "_displayvideo_604_CreateAssetResponseIn",
        "CreateAssetResponseOut": "_displayvideo_605_CreateAssetResponseOut",
        "DigitalContentLabelTargetingOptionDetailsIn": "_displayvideo_606_DigitalContentLabelTargetingOptionDetailsIn",
        "DigitalContentLabelTargetingOptionDetailsOut": "_displayvideo_607_DigitalContentLabelTargetingOptionDetailsOut",
        "ReplaceNegativeKeywordsRequestIn": "_displayvideo_608_ReplaceNegativeKeywordsRequestIn",
        "ReplaceNegativeKeywordsRequestOut": "_displayvideo_609_ReplaceNegativeKeywordsRequestOut",
        "ProximityLocationListAssignedTargetingOptionDetailsIn": "_displayvideo_610_ProximityLocationListAssignedTargetingOptionDetailsIn",
        "ProximityLocationListAssignedTargetingOptionDetailsOut": "_displayvideo_611_ProximityLocationListAssignedTargetingOptionDetailsOut",
        "ListUsersResponseIn": "_displayvideo_612_ListUsersResponseIn",
        "ListUsersResponseOut": "_displayvideo_613_ListUsersResponseOut",
        "SubExchangeTargetingOptionDetailsIn": "_displayvideo_614_SubExchangeTargetingOptionDetailsIn",
        "SubExchangeTargetingOptionDetailsOut": "_displayvideo_615_SubExchangeTargetingOptionDetailsOut",
        "InventorySourceAccessorsAdvertiserAccessorsIn": "_displayvideo_616_InventorySourceAccessorsAdvertiserAccessorsIn",
        "InventorySourceAccessorsAdvertiserAccessorsOut": "_displayvideo_617_InventorySourceAccessorsAdvertiserAccessorsOut",
        "ListLocationListsResponseIn": "_displayvideo_618_ListLocationListsResponseIn",
        "ListLocationListsResponseOut": "_displayvideo_619_ListLocationListsResponseOut",
        "TargetFrequencyIn": "_displayvideo_620_TargetFrequencyIn",
        "TargetFrequencyOut": "_displayvideo_621_TargetFrequencyOut",
        "ListInventorySourcesResponseIn": "_displayvideo_622_ListInventorySourcesResponseIn",
        "ListInventorySourcesResponseOut": "_displayvideo_623_ListInventorySourcesResponseOut",
        "FixedBidStrategyIn": "_displayvideo_624_FixedBidStrategyIn",
        "FixedBidStrategyOut": "_displayvideo_625_FixedBidStrategyOut",
        "InventorySourceGroupIn": "_displayvideo_626_InventorySourceGroupIn",
        "InventorySourceGroupOut": "_displayvideo_627_InventorySourceGroupOut",
        "CustomListGroupIn": "_displayvideo_628_CustomListGroupIn",
        "CustomListGroupOut": "_displayvideo_629_CustomListGroupOut",
        "AudioAdIn": "_displayvideo_630_AudioAdIn",
        "AudioAdOut": "_displayvideo_631_AudioAdOut",
        "ThirdPartyUrlIn": "_displayvideo_632_ThirdPartyUrlIn",
        "ThirdPartyUrlOut": "_displayvideo_633_ThirdPartyUrlOut",
        "InventorySourceAccessorsIn": "_displayvideo_634_InventorySourceAccessorsIn",
        "InventorySourceAccessorsOut": "_displayvideo_635_InventorySourceAccessorsOut",
        "DuplicateLineItemResponseIn": "_displayvideo_636_DuplicateLineItemResponseIn",
        "DuplicateLineItemResponseOut": "_displayvideo_637_DuplicateLineItemResponseOut",
        "ListFirstAndThirdPartyAudiencesResponseIn": "_displayvideo_638_ListFirstAndThirdPartyAudiencesResponseIn",
        "ListFirstAndThirdPartyAudiencesResponseOut": "_displayvideo_639_ListFirstAndThirdPartyAudiencesResponseOut",
        "ContactInfoListIn": "_displayvideo_640_ContactInfoListIn",
        "ContactInfoListOut": "_displayvideo_641_ContactInfoListOut",
        "GoogleAudienceTargetingSettingIn": "_displayvideo_642_GoogleAudienceTargetingSettingIn",
        "GoogleAudienceTargetingSettingOut": "_displayvideo_643_GoogleAudienceTargetingSettingOut",
        "AdvertiserIn": "_displayvideo_644_AdvertiserIn",
        "AdvertiserOut": "_displayvideo_645_AdvertiserOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PerformanceGoalBidStrategyIn"] = t.struct(
        {
            "performanceGoalType": t.string(),
            "performanceGoalAmountMicros": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
        }
    ).named(renames["PerformanceGoalBidStrategyIn"])
    types["PerformanceGoalBidStrategyOut"] = t.struct(
        {
            "performanceGoalType": t.string(),
            "performanceGoalAmountMicros": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceGoalBidStrategyOut"])
    types["BulkEditAssignedTargetingOptionsResponseIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["BulkEditAssignedTargetingOptionsResponseIn"])
    types["BulkEditAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
            "updatedLineItemIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsResponseOut"])
    types["SearchTargetingOptionsRequestIn"] = t.struct(
        {
            "geoRegionSearchTerms": t.proxy(
                renames["GeoRegionSearchTermsIn"]
            ).optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "businessChainSearchTerms": t.proxy(
                renames["BusinessChainSearchTermsIn"]
            ).optional(),
            "advertiserId": t.string(),
            "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
        }
    ).named(renames["SearchTargetingOptionsRequestIn"])
    types["SearchTargetingOptionsRequestOut"] = t.struct(
        {
            "geoRegionSearchTerms": t.proxy(
                renames["GeoRegionSearchTermsOut"]
            ).optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "businessChainSearchTerms": t.proxy(
                renames["BusinessChainSearchTermsOut"]
            ).optional(),
            "advertiserId": t.string(),
            "poiSearchTerms": t.proxy(renames["PoiSearchTermsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTargetingOptionsRequestOut"])
    types["CreateAssetRequestIn"] = t.struct({"filename": t.string()}).named(
        renames["CreateAssetRequestIn"]
    )
    types["CreateAssetRequestOut"] = t.struct(
        {"filename": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateAssetRequestOut"])
    types["SdfDownloadTaskIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["SdfDownloadTaskIn"])
    types["SdfDownloadTaskOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfDownloadTaskOut"])
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
    types["DoubleVerifyDisplayViewabilityIn"] = t.struct(
        {"iab": t.string().optional(), "viewableDuring": t.string().optional()}
    ).named(renames["DoubleVerifyDisplayViewabilityIn"])
    types["DoubleVerifyDisplayViewabilityOut"] = t.struct(
        {
            "iab": t.string().optional(),
            "viewableDuring": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyDisplayViewabilityOut"])
    types["YoutubeAndPartnersBiddingStrategyIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string().optional()}
    ).named(renames["YoutubeAndPartnersBiddingStrategyIn"])
    types["YoutubeAndPartnersBiddingStrategyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "adGroupEffectiveTargetCpaSource": t.string().optional(),
            "adGroupEffectiveTargetCpaValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersBiddingStrategyOut"])
    types["TrackingFloodlightActivityConfigIn"] = t.struct(
        {
            "floodlightActivityId": t.string(),
            "postClickLookbackWindowDays": t.integer(),
            "postViewLookbackWindowDays": t.integer(),
        }
    ).named(renames["TrackingFloodlightActivityConfigIn"])
    types["TrackingFloodlightActivityConfigOut"] = t.struct(
        {
            "floodlightActivityId": t.string(),
            "postClickLookbackWindowDays": t.integer(),
            "postViewLookbackWindowDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackingFloodlightActivityConfigOut"])
    types["FirstAndThirdPartyAudienceIn"] = t.struct(
        {
            "appId": t.string().optional(),
            "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
            "audienceType": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "firstAndThirdPartyAudienceType": t.string().optional(),
            "membershipDurationDays": t.string().optional(),
            "mobileDeviceIdList": t.proxy(renames["MobileDeviceIdListIn"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceIn"])
    types["FirstAndThirdPartyAudienceOut"] = t.struct(
        {
            "activeDisplayAudienceSize": t.string().optional(),
            "displayMobileAppAudienceSize": t.string().optional(),
            "appId": t.string().optional(),
            "contactInfoList": t.proxy(renames["ContactInfoListOut"]).optional(),
            "displayDesktopAudienceSize": t.string().optional(),
            "firstAndThirdPartyAudienceId": t.string().optional(),
            "audienceType": t.string().optional(),
            "displayName": t.string().optional(),
            "audienceSource": t.string().optional(),
            "displayMobileWebAudienceSize": t.string().optional(),
            "youtubeAudienceSize": t.string().optional(),
            "description": t.string().optional(),
            "firstAndThirdPartyAudienceType": t.string().optional(),
            "gmailAudienceSize": t.string().optional(),
            "membershipDurationDays": t.string().optional(),
            "name": t.string().optional(),
            "displayAudienceSize": t.string().optional(),
            "mobileDeviceIdList": t.proxy(renames["MobileDeviceIdListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceOut"])
    types["DeviceMakeModelTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeviceMakeModelTargetingOptionDetailsIn"])
    types["DeviceMakeModelTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMakeModelTargetingOptionDetailsOut"])
    types["CampaignBudgetIn"] = t.struct(
        {
            "budgetUnit": t.string(),
            "displayName": t.string(),
            "externalBudgetId": t.string().optional(),
            "budgetId": t.string().optional(),
            "budgetAmountMicros": t.string(),
            "prismaConfig": t.proxy(renames["PrismaConfigIn"]).optional(),
            "externalBudgetSource": t.string(),
            "dateRange": t.proxy(renames["DateRangeIn"]),
            "invoiceGroupingId": t.string().optional(),
        }
    ).named(renames["CampaignBudgetIn"])
    types["CampaignBudgetOut"] = t.struct(
        {
            "budgetUnit": t.string(),
            "displayName": t.string(),
            "externalBudgetId": t.string().optional(),
            "budgetId": t.string().optional(),
            "budgetAmountMicros": t.string(),
            "prismaConfig": t.proxy(renames["PrismaConfigOut"]).optional(),
            "externalBudgetSource": t.string(),
            "dateRange": t.proxy(renames["DateRangeOut"]),
            "invoiceGroupingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignBudgetOut"])
    types["ProductMatchDimensionIn"] = t.struct(
        {
            "productOfferId": t.string().optional(),
            "customLabel": t.proxy(renames["CustomLabelIn"]).optional(),
        }
    ).named(renames["ProductMatchDimensionIn"])
    types["ProductMatchDimensionOut"] = t.struct(
        {
            "productOfferId": t.string().optional(),
            "customLabel": t.proxy(renames["CustomLabelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductMatchDimensionOut"])
    types["MeasurementConfigIn"] = t.struct(
        {
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
        }
    ).named(renames["MeasurementConfigIn"])
    types["MeasurementConfigOut"] = t.struct(
        {
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeasurementConfigOut"])
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
            "proximityRadiusUnit": t.string(),
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessChainAssignedTargetingOptionDetailsOut"])
    types["UserRewardedContentAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["UserRewardedContentAssignedTargetingOptionDetailsIn"])
    types["UserRewardedContentAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "userRewardedContent": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRewardedContentAssignedTargetingOptionDetailsOut"])
    types["GeoRegionSearchTermsIn"] = t.struct(
        {"geoRegionQuery": t.string().optional()}
    ).named(renames["GeoRegionSearchTermsIn"])
    types["GeoRegionSearchTermsOut"] = t.struct(
        {
            "geoRegionQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionSearchTermsOut"])
    types["ListInsertionOrderAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInsertionOrderAssignedTargetingOptionsResponseIn"])
    types["ListInsertionOrderAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInsertionOrderAssignedTargetingOptionsResponseOut"])
    types["EnvironmentTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EnvironmentTargetingOptionDetailsIn"])
    types["EnvironmentTargetingOptionDetailsOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentTargetingOptionDetailsOut"])
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
    types["DigitalContentLabelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"excludedContentRatingTier": t.string()}
    ).named(renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"])
    types["DigitalContentLabelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "excludedContentRatingTier": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigitalContentLabelAssignedTargetingOptionDetailsOut"])
    types["GoogleAudienceGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["GoogleAudienceTargetingSettingIn"]))}
    ).named(renames["GoogleAudienceGroupIn"])
    types["GoogleAudienceGroupOut"] = t.struct(
        {
            "settings": t.array(t.proxy(renames["GoogleAudienceTargetingSettingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceGroupOut"])
    types["CustomBiddingAlgorithmIn"] = t.struct(
        {
            "customBiddingAlgorithmType": t.string(),
            "advertiserId": t.string().optional(),
            "entityStatus": t.string().optional(),
            "partnerId": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "displayName": t.string(),
        }
    ).named(renames["CustomBiddingAlgorithmIn"])
    types["CustomBiddingAlgorithmOut"] = t.struct(
        {
            "customBiddingAlgorithmType": t.string(),
            "advertiserId": t.string().optional(),
            "name": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "entityStatus": t.string().optional(),
            "partnerId": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "modelDetails": t.array(
                t.proxy(renames["CustomBiddingModelDetailsOut"])
            ).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingAlgorithmOut"])
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
            "proximityRadiusAmount": t.number(),
            "proximityRadiusUnit": t.string(),
            "longitude": t.number().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiAssignedTargetingOptionDetailsOut"])
    types["BulkListAdGroupAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "youtubeAdGroupAssignedTargetingOptions": t.array(
                t.proxy(renames["YoutubeAdGroupAssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["BulkListAdGroupAssignedTargetingOptionsResponseIn"])
    types["BulkListAdGroupAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "youtubeAdGroupAssignedTargetingOptions": t.array(
                t.proxy(renames["YoutubeAdGroupAssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListAdGroupAssignedTargetingOptionsResponseOut"])
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
    types["ListCampaignsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "campaigns": t.array(t.proxy(renames["CampaignIn"])).optional(),
        }
    ).named(renames["ListCampaignsResponseIn"])
    types["ListCampaignsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "campaigns": t.array(t.proxy(renames["CampaignOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCampaignsResponseOut"])
    types["ContentGenreAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["ContentGenreAssignedTargetingOptionDetailsIn"])
    types["ContentGenreAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentGenreAssignedTargetingOptionDetailsOut"])
    types["ExchangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"exchange": t.string()}
    ).named(renames["ExchangeAssignedTargetingOptionDetailsIn"])
    types["ExchangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {"exchange": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExchangeAssignedTargetingOptionDetailsOut"])
    types["ExchangeConfigEnabledExchangeIn"] = t.struct(
        {"exchange": t.string().optional()}
    ).named(renames["ExchangeConfigEnabledExchangeIn"])
    types["ExchangeConfigEnabledExchangeOut"] = t.struct(
        {
            "seatId": t.string().optional(),
            "exchange": t.string().optional(),
            "googleAdManagerAgencyId": t.string().optional(),
            "googleAdManagerBuyerNetworkId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeConfigEnabledExchangeOut"])
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
    types["EditCustomerMatchMembersResponseIn"] = t.struct(
        {"firstAndThirdPartyAudienceId": t.string()}
    ).named(renames["EditCustomerMatchMembersResponseIn"])
    types["EditCustomerMatchMembersResponseOut"] = t.struct(
        {
            "firstAndThirdPartyAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditCustomerMatchMembersResponseOut"])
    types["CustomListIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CustomListIn"]
    )
    types["CustomListOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "customListId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListOut"])
    types["ListCreativesResponseIn"] = t.struct(
        {
            "creatives": t.array(t.proxy(renames["CreativeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCreativesResponseIn"])
    types["ListCreativesResponseOut"] = t.struct(
        {
            "creatives": t.array(t.proxy(renames["CreativeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativesResponseOut"])
    types["SiteIn"] = t.struct({"urlOrAppId": t.string()}).named(renames["SiteIn"])
    types["SiteOut"] = t.struct(
        {
            "urlOrAppId": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteOut"])
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
    types["SdfConfigIn"] = t.struct(
        {"version": t.string(), "adminEmail": t.string().optional()}
    ).named(renames["SdfConfigIn"])
    types["SdfConfigOut"] = t.struct(
        {
            "version": t.string(),
            "adminEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfConfigOut"])
    types["NegativeKeywordListIn"] = t.struct({"displayName": t.string()}).named(
        renames["NegativeKeywordListIn"]
    )
    types["NegativeKeywordListOut"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string().optional(),
            "targetedLineItemCount": t.string().optional(),
            "advertiserId": t.string().optional(),
            "negativeKeywordListId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordListOut"])
    types["ChannelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"channelId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["ChannelAssignedTargetingOptionDetailsIn"])
    types["ChannelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "channelId": t.string(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelAssignedTargetingOptionDetailsOut"])
    types["TranscodeIn"] = t.struct(
        {
            "audioBitRateKbps": t.string().optional(),
            "fileSizeBytes": t.string().optional(),
            "transcoded": t.boolean().optional(),
            "name": t.string().optional(),
            "bitRateKbps": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]).optional(),
            "mimeType": t.string().optional(),
            "audioSampleRateHz": t.string().optional(),
            "frameRate": t.number().optional(),
        }
    ).named(renames["TranscodeIn"])
    types["TranscodeOut"] = t.struct(
        {
            "audioBitRateKbps": t.string().optional(),
            "fileSizeBytes": t.string().optional(),
            "transcoded": t.boolean().optional(),
            "name": t.string().optional(),
            "bitRateKbps": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]).optional(),
            "mimeType": t.string().optional(),
            "audioSampleRateHz": t.string().optional(),
            "frameRate": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscodeOut"])
    types["EditCustomerMatchMembersRequestIn"] = t.struct(
        {
            "addedMobileDeviceIdList": t.proxy(
                renames["MobileDeviceIdListIn"]
            ).optional(),
            "advertiserId": t.string(),
            "addedContactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
        }
    ).named(renames["EditCustomerMatchMembersRequestIn"])
    types["EditCustomerMatchMembersRequestOut"] = t.struct(
        {
            "addedMobileDeviceIdList": t.proxy(
                renames["MobileDeviceIdListOut"]
            ).optional(),
            "advertiserId": t.string(),
            "addedContactInfoList": t.proxy(renames["ContactInfoListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditCustomerMatchMembersRequestOut"])
    types["ChannelIn"] = t.struct(
        {
            "displayName": t.string(),
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "negativelyTargetedLineItemCount": t.string().optional(),
            "advertiserId": t.string().optional(),
            "positivelyTargetedLineItemCount": t.string().optional(),
            "partnerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
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
    types["NegativeKeywordListAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negativeKeywordListId": t.string()}
    ).named(renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"])
    types["NegativeKeywordListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negativeKeywordListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordListAssignedTargetingOptionDetailsOut"])
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
    types["ListGuaranteedOrdersResponseIn"] = t.struct(
        {
            "guaranteedOrders": t.array(
                t.proxy(renames["GuaranteedOrderIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGuaranteedOrdersResponseIn"])
    types["ListGuaranteedOrdersResponseOut"] = t.struct(
        {
            "guaranteedOrders": t.array(
                t.proxy(renames["GuaranteedOrderOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGuaranteedOrdersResponseOut"])
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
    types["DoubleVerifyIn"] = t.struct(
        {
            "videoViewability": t.proxy(
                renames["DoubleVerifyVideoViewabilityIn"]
            ).optional(),
            "displayViewability": t.proxy(
                renames["DoubleVerifyDisplayViewabilityIn"]
            ).optional(),
            "avoidedAgeRatings": t.array(t.string()).optional(),
            "appStarRating": t.proxy(renames["DoubleVerifyAppStarRatingIn"]).optional(),
            "customSegmentId": t.string().optional(),
            "fraudInvalidTraffic": t.proxy(
                renames["DoubleVerifyFraudInvalidTrafficIn"]
            ).optional(),
            "brandSafetyCategories": t.proxy(
                renames["DoubleVerifyBrandSafetyCategoriesIn"]
            ).optional(),
        }
    ).named(renames["DoubleVerifyIn"])
    types["DoubleVerifyOut"] = t.struct(
        {
            "videoViewability": t.proxy(
                renames["DoubleVerifyVideoViewabilityOut"]
            ).optional(),
            "displayViewability": t.proxy(
                renames["DoubleVerifyDisplayViewabilityOut"]
            ).optional(),
            "avoidedAgeRatings": t.array(t.string()).optional(),
            "appStarRating": t.proxy(
                renames["DoubleVerifyAppStarRatingOut"]
            ).optional(),
            "customSegmentId": t.string().optional(),
            "fraudInvalidTraffic": t.proxy(
                renames["DoubleVerifyFraudInvalidTrafficOut"]
            ).optional(),
            "brandSafetyCategories": t.proxy(
                renames["DoubleVerifyBrandSafetyCategoriesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyOut"])
    types["YoutubeVideoDetailsIn"] = t.struct(
        {"id": t.string().optional(), "unavailableReason": t.string().optional()}
    ).named(renames["YoutubeVideoDetailsIn"])
    types["YoutubeVideoDetailsOut"] = t.struct(
        {
            "id": t.string().optional(),
            "unavailableReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeVideoDetailsOut"])
    types["UserRewardedContentTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UserRewardedContentTargetingOptionDetailsIn"])
    types["UserRewardedContentTargetingOptionDetailsOut"] = t.struct(
        {
            "userRewardedContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRewardedContentTargetingOptionDetailsOut"])
    types["InventorySourceAssignedTargetingOptionDetailsIn"] = t.struct(
        {"inventorySourceId": t.string()}
    ).named(renames["InventorySourceAssignedTargetingOptionDetailsIn"])
    types["InventorySourceAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "inventorySourceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAssignedTargetingOptionDetailsOut"])
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
    types["BulkEditSitesResponseIn"] = t.struct(
        {"sites": t.array(t.proxy(renames["SiteIn"])).optional()}
    ).named(renames["BulkEditSitesResponseIn"])
    types["BulkEditSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditSitesResponseOut"])
    types["CustomBiddingScriptIn"] = t.struct(
        {"script": t.proxy(renames["CustomBiddingScriptRefIn"]).optional()}
    ).named(renames["CustomBiddingScriptIn"])
    types["CustomBiddingScriptOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "customBiddingScriptId": t.string().optional(),
            "active": t.boolean().optional(),
            "script": t.proxy(renames["CustomBiddingScriptRefOut"]).optional(),
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["ScriptErrorOut"])).optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingScriptOut"])
    types["AssignedInventorySourceIn"] = t.struct(
        {"inventorySourceId": t.string()}
    ).named(renames["AssignedInventorySourceIn"])
    types["AssignedInventorySourceOut"] = t.struct(
        {
            "assignedInventorySourceId": t.string().optional(),
            "inventorySourceId": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedInventorySourceOut"])
    types["GeoRegionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["GeoRegionAssignedTargetingOptionDetailsIn"])
    types["GeoRegionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "geoRegionType": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionAssignedTargetingOptionDetailsOut"])
    types["CreateSdfDownloadTaskRequestIn"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "inventorySourceFilter": t.proxy(
                renames["InventorySourceFilterIn"]
            ).optional(),
            "idFilter": t.proxy(renames["IdFilterIn"]).optional(),
            "version": t.string(),
            "parentEntityFilter": t.proxy(renames["ParentEntityFilterIn"]).optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["CreateSdfDownloadTaskRequestIn"])
    types["CreateSdfDownloadTaskRequestOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "inventorySourceFilter": t.proxy(
                renames["InventorySourceFilterOut"]
            ).optional(),
            "idFilter": t.proxy(renames["IdFilterOut"]).optional(),
            "version": t.string(),
            "parentEntityFilter": t.proxy(renames["ParentEntityFilterOut"]).optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSdfDownloadTaskRequestOut"])
    types["GeoRegionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GeoRegionTargetingOptionDetailsIn"])
    types["GeoRegionTargetingOptionDetailsOut"] = t.struct(
        {
            "geoRegionType": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionTargetingOptionDetailsOut"])
    types["GuaranteedOrderStatusIn"] = t.struct(
        {
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
        }
    ).named(renames["GuaranteedOrderStatusIn"])
    types["GuaranteedOrderStatusOut"] = t.struct(
        {
            "entityStatus": t.string().optional(),
            "configStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedOrderStatusOut"])
    types["TimeRangeIn"] = t.struct(
        {"endTime": t.string(), "startTime": t.string()}
    ).named(renames["TimeRangeIn"])
    types["TimeRangeOut"] = t.struct(
        {
            "endTime": t.string(),
            "startTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeRangeOut"])
    types["DoubleVerifyBrandSafetyCategoriesIn"] = t.struct(
        {
            "avoidUnknownBrandSafetyCategory": t.boolean().optional(),
            "avoidedHighSeverityCategories": t.array(t.string()).optional(),
            "avoidedMediumSeverityCategories": t.array(t.string()).optional(),
        }
    ).named(renames["DoubleVerifyBrandSafetyCategoriesIn"])
    types["DoubleVerifyBrandSafetyCategoriesOut"] = t.struct(
        {
            "avoidUnknownBrandSafetyCategory": t.boolean().optional(),
            "avoidedHighSeverityCategories": t.array(t.string()).optional(),
            "avoidedMediumSeverityCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyBrandSafetyCategoriesOut"])
    types["ListNegativeKeywordListsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "negativeKeywordLists": t.array(
                t.proxy(renames["NegativeKeywordListIn"])
            ).optional(),
        }
    ).named(renames["ListNegativeKeywordListsResponseIn"])
    types["ListNegativeKeywordListsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "negativeKeywordLists": t.array(
                t.proxy(renames["NegativeKeywordListOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNegativeKeywordListsResponseOut"])
    types["CombinedAudienceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CombinedAudienceIn"]
    )
    types["CombinedAudienceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "combinedAudienceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CombinedAudienceOut"])
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
    types["PrismaConfigIn"] = t.struct(
        {
            "supplier": t.string(),
            "prismaType": t.string(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeIn"]),
        }
    ).named(renames["PrismaConfigIn"])
    types["PrismaConfigOut"] = t.struct(
        {
            "supplier": t.string(),
            "prismaType": t.string(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrismaConfigOut"])
    types["InStreamAdIn"] = t.struct(
        {
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "commonInStreamAttribute": t.proxy(
                renames["CommonInStreamAttributeIn"]
            ).optional(),
        }
    ).named(renames["InStreamAdIn"])
    types["InStreamAdOut"] = t.struct(
        {
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "commonInStreamAttribute": t.proxy(
                renames["CommonInStreamAttributeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InStreamAdOut"])
    types["InventorySourceAccessorsPartnerAccessorIn"] = t.struct(
        {"partnerId": t.string().optional()}
    ).named(renames["InventorySourceAccessorsPartnerAccessorIn"])
    types["InventorySourceAccessorsPartnerAccessorOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsPartnerAccessorOut"])
    types["LanguageTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["LanguageTargetingOptionDetailsIn"])
    types["LanguageTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageTargetingOptionDetailsOut"])
    types["OnScreenPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["OnScreenPositionAssignedTargetingOptionDetailsIn"])
    types["OnScreenPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "onScreenPosition": t.string().optional(),
            "adType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnScreenPositionAssignedTargetingOptionDetailsOut"])
    types["NativeContentPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"contentPosition": t.string().optional()}
    ).named(renames["NativeContentPositionAssignedTargetingOptionDetailsIn"])
    types["NativeContentPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "contentPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentPositionAssignedTargetingOptionDetailsOut"])
    types["OnScreenPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OnScreenPositionTargetingOptionDetailsIn"])
    types["OnScreenPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "onScreenPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnScreenPositionTargetingOptionDetailsOut"])
    types["YoutubeAdGroupAdIn"] = t.struct(
        {
            "adGroupId": t.string().optional(),
            "mastheadAd": t.proxy(renames["MastheadAdIn"]).optional(),
            "videoDiscoverAd": t.proxy(renames["VideoDiscoveryAdIn"]).optional(),
            "inStreamAd": t.proxy(renames["InStreamAdIn"]).optional(),
            "advertiserId": t.string().optional(),
            "entityStatus": t.string().optional(),
            "adUrls": t.array(t.proxy(renames["AdUrlIn"])).optional(),
            "displayName": t.string().optional(),
            "adGroupAdId": t.string().optional(),
            "nonSkippableAd": t.proxy(renames["NonSkippableAdIn"]).optional(),
            "name": t.string().optional(),
            "audioAd": t.proxy(renames["AudioAdIn"]).optional(),
            "bumperAd": t.proxy(renames["BumperAdIn"]).optional(),
            "videoPerformanceAd": t.proxy(renames["VideoPerformanceAdIn"]).optional(),
            "displayVideoSourceAd": t.proxy(
                renames["DisplayVideoSourceAdIn"]
            ).optional(),
        }
    ).named(renames["YoutubeAdGroupAdIn"])
    types["YoutubeAdGroupAdOut"] = t.struct(
        {
            "adGroupId": t.string().optional(),
            "mastheadAd": t.proxy(renames["MastheadAdOut"]).optional(),
            "videoDiscoverAd": t.proxy(renames["VideoDiscoveryAdOut"]).optional(),
            "inStreamAd": t.proxy(renames["InStreamAdOut"]).optional(),
            "advertiserId": t.string().optional(),
            "entityStatus": t.string().optional(),
            "adUrls": t.array(t.proxy(renames["AdUrlOut"])).optional(),
            "displayName": t.string().optional(),
            "adGroupAdId": t.string().optional(),
            "nonSkippableAd": t.proxy(renames["NonSkippableAdOut"]).optional(),
            "name": t.string().optional(),
            "audioAd": t.proxy(renames["AudioAdOut"]).optional(),
            "bumperAd": t.proxy(renames["BumperAdOut"]).optional(),
            "videoPerformanceAd": t.proxy(renames["VideoPerformanceAdOut"]).optional(),
            "displayVideoSourceAd": t.proxy(
                renames["DisplayVideoSourceAdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupAdOut"])
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
    types["GoogleAudienceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAudienceIn"]
    )
    types["GoogleAudienceOut"] = t.struct(
        {
            "googleAudienceId": t.string().optional(),
            "displayName": t.string().optional(),
            "googleAudienceType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceOut"])
    types["ImageAssetIn"] = t.struct(
        {
            "fullSize": t.proxy(renames["DimensionsIn"]).optional(),
            "mimeType": t.string().optional(),
            "fileSize": t.string().optional(),
        }
    ).named(renames["ImageAssetIn"])
    types["ImageAssetOut"] = t.struct(
        {
            "fullSize": t.proxy(renames["DimensionsOut"]).optional(),
            "mimeType": t.string().optional(),
            "fileSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageAssetOut"])
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
    types["IdFilterIn"] = t.struct(
        {
            "campaignIds": t.array(t.string()).optional(),
            "adGroupAdIds": t.array(t.string()).optional(),
            "adGroupIds": t.array(t.string()).optional(),
            "mediaProductIds": t.array(t.string()).optional(),
            "insertionOrderIds": t.array(t.string()).optional(),
            "lineItemIds": t.array(t.string()).optional(),
        }
    ).named(renames["IdFilterIn"])
    types["IdFilterOut"] = t.struct(
        {
            "campaignIds": t.array(t.string()).optional(),
            "adGroupAdIds": t.array(t.string()).optional(),
            "adGroupIds": t.array(t.string()).optional(),
            "mediaProductIds": t.array(t.string()).optional(),
            "insertionOrderIds": t.array(t.string()).optional(),
            "lineItemIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdFilterOut"])
    types["ContentStreamTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentStreamTypeTargetingOptionDetailsIn"])
    types["ContentStreamTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "contentStreamType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentStreamTypeTargetingOptionDetailsOut"])
    types["AssignedTargetingOptionIn"] = t.struct(
        {
            "dayAndTimeDetails": t.proxy(
                renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "inventorySourceDetails": t.proxy(
                renames["InventorySourceAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "thirdPartyVerifierDetails": t.proxy(
                renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "channelDetails": t.proxy(
                renames["ChannelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "sensitiveCategoryExclusionDetails": t.proxy(
                renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "negativeKeywordListDetails": t.proxy(
                renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "omidDetails": t.proxy(
                renames["OmidAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "sessionPositionDetails": t.proxy(
                renames["SessionPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "regionalLocationListDetails": t.proxy(
                renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "appDetails": t.proxy(
                renames["AppAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "keywordDetails": t.proxy(
                renames["KeywordAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "urlDetails": t.proxy(
                renames["UrlAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "digitalContentLabelExclusionDetails": t.proxy(
                renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "youtubeChannelDetails": t.proxy(
                renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "proximityLocationListDetails": t.proxy(
                renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "poiDetails": t.proxy(
                renames["PoiAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "audienceGroupDetails": t.proxy(
                renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "inventorySourceGroupDetails": t.proxy(
                renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "youtubeVideoDetails": t.proxy(
                renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionAssignedTargetingOptionDetailsIn"]
            ).optional(),
        }
    ).named(renames["AssignedTargetingOptionIn"])
    types["AssignedTargetingOptionOut"] = t.struct(
        {
            "dayAndTimeDetails": t.proxy(
                renames["DayAndTimeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inventorySourceDetails": t.proxy(
                renames["InventorySourceAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "thirdPartyVerifierDetails": t.proxy(
                renames["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inheritance": t.string().optional(),
            "languageDetails": t.proxy(
                renames["LanguageAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "channelDetails": t.proxy(
                renames["ChannelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "sensitiveCategoryExclusionDetails": t.proxy(
                renames["SensitiveCategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "negativeKeywordListDetails": t.proxy(
                renames["NegativeKeywordListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "omidDetails": t.proxy(
                renames["OmidAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "sessionPositionDetails": t.proxy(
                renames["SessionPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "regionalLocationListDetails": t.proxy(
                renames["RegionalLocationListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "appDetails": t.proxy(
                renames["AppAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "keywordDetails": t.proxy(
                renames["KeywordAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "targetingType": t.string().optional(),
            "urlDetails": t.proxy(
                renames["UrlAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "digitalContentLabelExclusionDetails": t.proxy(
                renames["DigitalContentLabelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "youtubeChannelDetails": t.proxy(
                renames["YoutubeChannelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "assignedTargetingOptionId": t.string().optional(),
            "proximityLocationListDetails": t.proxy(
                renames["ProximityLocationListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "poiDetails": t.proxy(
                renames["PoiAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "audienceGroupDetails": t.proxy(
                renames["AudienceGroupAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inventorySourceGroupDetails": t.proxy(
                renames["InventorySourceGroupAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "youtubeVideoDetails": t.proxy(
                renames["YoutubeVideoAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "assignedTargetingOptionIdAlias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedTargetingOptionOut"])
    types["ExitEventIn"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "reportingName": t.string().optional(),
            "url": t.string(),
        }
    ).named(renames["ExitEventIn"])
    types["ExitEventOut"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "reportingName": t.string().optional(),
            "url": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExitEventOut"])
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
    types["InsertionOrderIn"] = t.struct(
        {
            "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
            "pacing": t.proxy(renames["PacingIn"]),
            "campaignId": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "displayName": t.string(),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "insertionOrderType": t.string().optional(),
            "entityStatus": t.string(),
            "billableOutcome": t.string().optional(),
            "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
            "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
        }
    ).named(renames["InsertionOrderIn"])
    types["InsertionOrderOut"] = t.struct(
        {
            "budget": t.proxy(renames["InsertionOrderBudgetOut"]),
            "pacing": t.proxy(renames["PacingOut"]),
            "campaignId": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostOut"])).optional(),
            "advertiserId": t.string().optional(),
            "updateTime": t.string().optional(),
            "reservationType": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "insertionOrderType": t.string().optional(),
            "entityStatus": t.string(),
            "insertionOrderId": t.string().optional(),
            "billableOutcome": t.string().optional(),
            "bidStrategy": t.proxy(renames["BiddingStrategyOut"]).optional(),
            "performanceGoal": t.proxy(renames["PerformanceGoalOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderOut"])
    types["RegionalLocationListAssignedTargetingOptionDetailsIn"] = t.struct(
        {"regionalLocationListId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["RegionalLocationListAssignedTargetingOptionDetailsIn"])
    types["RegionalLocationListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "regionalLocationListId": t.string(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalLocationListAssignedTargetingOptionDetailsOut"])
    types["BrowserTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["BrowserTargetingOptionDetailsIn"])
    types["BrowserTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserTargetingOptionDetailsOut"])
    types["AdlooxIn"] = t.struct(
        {"excludedAdlooxCategories": t.array(t.string()).optional()}
    ).named(renames["AdlooxIn"])
    types["AdlooxOut"] = t.struct(
        {
            "excludedAdlooxCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdlooxOut"])
    types["ScriptErrorIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "line": t.string().optional(),
            "column": t.string().optional(),
            "errorCode": t.string().optional(),
        }
    ).named(renames["ScriptErrorIn"])
    types["ScriptErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "line": t.string().optional(),
            "column": t.string().optional(),
            "errorCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptErrorOut"])
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
    types["AdvertiserGeneralConfigIn"] = t.struct(
        {"currencyCode": t.string(), "domainUrl": t.string()}
    ).named(renames["AdvertiserGeneralConfigIn"])
    types["AdvertiserGeneralConfigOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "currencyCode": t.string(),
            "domainUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserGeneralConfigOut"])
    types["FloodlightGroupIn"] = t.struct(
        {
            "lookbackWindow": t.proxy(renames["LookbackWindowIn"]),
            "customVariables": t.struct({"_": t.string().optional()}).optional(),
            "activeViewConfig": t.proxy(
                renames["ActiveViewVideoViewabilityMetricConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "webTagType": t.string(),
        }
    ).named(renames["FloodlightGroupIn"])
    types["FloodlightGroupOut"] = t.struct(
        {
            "lookbackWindow": t.proxy(renames["LookbackWindowOut"]),
            "name": t.string().optional(),
            "floodlightGroupId": t.string().optional(),
            "customVariables": t.struct({"_": t.string().optional()}).optional(),
            "activeViewConfig": t.proxy(
                renames["ActiveViewVideoViewabilityMetricConfigOut"]
            ).optional(),
            "displayName": t.string(),
            "webTagType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightGroupOut"])
    types["PacingIn"] = t.struct(
        {
            "pacingType": t.string(),
            "dailyMaxImpressions": t.string().optional(),
            "pacingPeriod": t.string(),
            "dailyMaxMicros": t.string().optional(),
        }
    ).named(renames["PacingIn"])
    types["PacingOut"] = t.struct(
        {
            "pacingType": t.string(),
            "dailyMaxImpressions": t.string().optional(),
            "pacingPeriod": t.string(),
            "dailyMaxMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PacingOut"])
    types["ContentInstreamPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentInstreamPositionTargetingOptionDetailsIn"])
    types["ContentInstreamPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentInstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentInstreamPositionTargetingOptionDetailsOut"])
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
    types["ParentalStatusTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ParentalStatusTargetingOptionDetailsIn"])
    types["ParentalStatusTargetingOptionDetailsOut"] = t.struct(
        {
            "parentalStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentalStatusTargetingOptionDetailsOut"])
    types["InventorySourceVideoCreativeConfigIn"] = t.struct(
        {"duration": t.string().optional()}
    ).named(renames["InventorySourceVideoCreativeConfigIn"])
    types["InventorySourceVideoCreativeConfigOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceVideoCreativeConfigOut"])
    types["InventorySourceStatusIn"] = t.struct(
        {
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
        }
    ).named(renames["InventorySourceStatusIn"])
    types["InventorySourceStatusOut"] = t.struct(
        {
            "sellerStatus": t.string().optional(),
            "configStatus": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceStatusOut"])
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
    types["EditGuaranteedOrderReadAccessorsRequestIn"] = t.struct(
        {
            "addedAdvertisers": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
            "partnerId": t.string(),
            "removedAdvertisers": t.array(t.string()).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsRequestIn"])
    types["EditGuaranteedOrderReadAccessorsRequestOut"] = t.struct(
        {
            "addedAdvertisers": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
            "partnerId": t.string(),
            "removedAdvertisers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsRequestOut"])
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
    types["SdfDownloadTaskMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["SdfDownloadTaskMetadataIn"])
    types["SdfDownloadTaskMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfDownloadTaskMetadataOut"])
    types["DeviceTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeviceTypeTargetingOptionDetailsIn"])
    types["DeviceTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTypeTargetingOptionDetailsOut"])
    types["SensitiveCategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SensitiveCategoryTargetingOptionDetailsIn"])
    types["SensitiveCategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "sensitiveCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveCategoryTargetingOptionDetailsOut"])
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
    types["BulkEditAssignedInventorySourcesRequestIn"] = t.struct(
        {
            "deletedAssignedInventorySources": t.array(t.string()).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "createdAssignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceIn"])
            ).optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesRequestIn"])
    types["BulkEditAssignedInventorySourcesRequestOut"] = t.struct(
        {
            "deletedAssignedInventorySources": t.array(t.string()).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "createdAssignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesRequestOut"])
    types["BulkEditAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
            ).optional(),
            "lineItemIds": t.array(t.string()),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
            ).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsRequestIn"])
    types["BulkEditAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "lineItemIds": t.array(t.string()),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsRequestOut"])
    types["NativeContentPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["NativeContentPositionTargetingOptionDetailsIn"])
    types["NativeContentPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentPositionTargetingOptionDetailsOut"])
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
    types["ListYoutubeAdGroupAdsResponseIn"] = t.struct(
        {
            "youtubeAdGroupAds": t.array(
                t.proxy(renames["YoutubeAdGroupAdIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListYoutubeAdGroupAdsResponseIn"])
    types["ListYoutubeAdGroupAdsResponseOut"] = t.struct(
        {
            "youtubeAdGroupAds": t.array(
                t.proxy(renames["YoutubeAdGroupAdOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListYoutubeAdGroupAdsResponseOut"])
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
    types["AssetIn"] = t.struct(
        {"content": t.string().optional(), "mediaId": t.string().optional()}
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "content": t.string().optional(),
            "mediaId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleBytestreamMediaIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["GoogleBytestreamMediaIn"])
    types["GoogleBytestreamMediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleBytestreamMediaOut"])
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
    types["PoiSearchTermsIn"] = t.struct({"poiQuery": t.string().optional()}).named(
        renames["PoiSearchTermsIn"]
    )
    types["PoiSearchTermsOut"] = t.struct(
        {
            "poiQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiSearchTermsOut"])
    types["ContentGenreTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentGenreTargetingOptionDetailsIn"])
    types["ContentGenreTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentGenreTargetingOptionDetailsOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["BusinessChainSearchTermsIn"] = t.struct(
        {
            "regionQuery": t.string().optional(),
            "businessChainQuery": t.string().optional(),
        }
    ).named(renames["BusinessChainSearchTermsIn"])
    types["BusinessChainSearchTermsOut"] = t.struct(
        {
            "regionQuery": t.string().optional(),
            "businessChainQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessChainSearchTermsOut"])
    types["YoutubeAndPartnersSettingsIn"] = t.struct(
        {
            "relatedVideoIds": t.array(t.string()).optional(),
            "leadFormId": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyIn"]
            ).optional(),
            "contentCategory": t.string().optional(),
            "linkedMerchantId": t.string().optional(),
            "thirdPartyMeasurementSettings": t.proxy(
                renames["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"]
            ).optional(),
            "videoAdSequenceSettings": t.proxy(
                renames["VideoAdSequenceSettingsIn"]
            ).optional(),
            "viewFrequencyCap": t.proxy(renames["FrequencyCapIn"]).optional(),
            "targetFrequency": t.proxy(renames["TargetFrequencyIn"]).optional(),
            "inventorySourceSettings": t.proxy(
                renames["YoutubeAndPartnersInventorySourceConfigIn"]
            ).optional(),
        }
    ).named(renames["YoutubeAndPartnersSettingsIn"])
    types["YoutubeAndPartnersSettingsOut"] = t.struct(
        {
            "relatedVideoIds": t.array(t.string()).optional(),
            "leadFormId": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyOut"]
            ).optional(),
            "contentCategory": t.string().optional(),
            "linkedMerchantId": t.string().optional(),
            "thirdPartyMeasurementSettings": t.proxy(
                renames["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"]
            ).optional(),
            "videoAdSequenceSettings": t.proxy(
                renames["VideoAdSequenceSettingsOut"]
            ).optional(),
            "viewFrequencyCap": t.proxy(renames["FrequencyCapOut"]).optional(),
            "targetFrequency": t.proxy(renames["TargetFrequencyOut"]).optional(),
            "inventorySourceSettings": t.proxy(
                renames["YoutubeAndPartnersInventorySourceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersSettingsOut"])
    types["GenderAssignedTargetingOptionDetailsIn"] = t.struct(
        {"gender": t.string().optional()}
    ).named(renames["GenderAssignedTargetingOptionDetailsIn"])
    types["GenderAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderAssignedTargetingOptionDetailsOut"])
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
    types["OperatingSystemAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["OperatingSystemAssignedTargetingOptionDetailsIn"])
    types["OperatingSystemAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemAssignedTargetingOptionDetailsOut"])
    types["MobileAppIn"] = t.struct({"appId": t.string()}).named(renames["MobileAppIn"])
    types["MobileAppOut"] = t.struct(
        {
            "platform": t.string().optional(),
            "appId": t.string(),
            "publisher": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileAppOut"])
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
    types["CreativeIn"] = t.struct(
        {
            "vastTagUrl": t.string().optional(),
            "requireHtml5": t.boolean().optional(),
            "thirdPartyTag": t.string().optional(),
            "thirdPartyUrls": t.array(t.proxy(renames["ThirdPartyUrlIn"])).optional(),
            "creativeType": t.string(),
            "dimensions": t.proxy(renames["DimensionsIn"]),
            "expandOnHover": t.boolean().optional(),
            "jsTrackerUrl": t.string().optional(),
            "appendedTag": t.string().optional(),
            "trackerUrls": t.array(t.string()).optional(),
            "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
            "hostingSource": t.string(),
            "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
            "requireMraid": t.boolean().optional(),
            "requirePingForAttribution": t.boolean().optional(),
            "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
            "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
            "iasCampaignMonitoring": t.boolean().optional(),
            "expandingDirection": t.string().optional(),
            "entityStatus": t.string(),
            "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
            "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
            "displayName": t.string(),
            "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
            "additionalDimensions": t.array(
                t.proxy(renames["DimensionsIn"])
            ).optional(),
            "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
            "notes": t.string().optional(),
            "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
            "skippable": t.boolean().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "integrationCode": t.string().optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "vastTagUrl": t.string().optional(),
            "requireHtml5": t.boolean().optional(),
            "thirdPartyTag": t.string().optional(),
            "thirdPartyUrls": t.array(t.proxy(renames["ThirdPartyUrlOut"])).optional(),
            "html5Video": t.boolean().optional(),
            "creativeType": t.string(),
            "dimensions": t.proxy(renames["DimensionsOut"]),
            "expandOnHover": t.boolean().optional(),
            "jsTrackerUrl": t.string().optional(),
            "appendedTag": t.string().optional(),
            "trackerUrls": t.array(t.string()).optional(),
            "dynamic": t.boolean().optional(),
            "obaIcon": t.proxy(renames["ObaIconOut"]).optional(),
            "hostingSource": t.string(),
            "universalAdId": t.proxy(renames["UniversalAdIdOut"]).optional(),
            "name": t.string().optional(),
            "requireMraid": t.boolean().optional(),
            "requirePingForAttribution": t.boolean().optional(),
            "reviewStatus": t.proxy(renames["ReviewStatusInfoOut"]).optional(),
            "updateTime": t.string().optional(),
            "counterEvents": t.array(t.proxy(renames["CounterEventOut"])).optional(),
            "vpaid": t.boolean().optional(),
            "mediaDuration": t.string().optional(),
            "transcodes": t.array(t.proxy(renames["TranscodeOut"])).optional(),
            "assets": t.array(t.proxy(renames["AssetAssociationOut"])),
            "createTime": t.string().optional(),
            "oggAudio": t.boolean().optional(),
            "iasCampaignMonitoring": t.boolean().optional(),
            "creativeAttributes": t.array(t.string()).optional(),
            "expandingDirection": t.string().optional(),
            "entityStatus": t.string(),
            "exitEvents": t.array(t.proxy(renames["ExitEventOut"])),
            "progressOffset": t.proxy(renames["AudioVideoOffsetOut"]).optional(),
            "cmPlacementId": t.string().optional(),
            "displayName": t.string(),
            "timerEvents": t.array(t.proxy(renames["TimerEventOut"])).optional(),
            "additionalDimensions": t.array(
                t.proxy(renames["DimensionsOut"])
            ).optional(),
            "skipOffset": t.proxy(renames["AudioVideoOffsetOut"]).optional(),
            "advertiserId": t.string().optional(),
            "notes": t.string().optional(),
            "lineItemIds": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "mp3Audio": t.boolean().optional(),
            "cmTrackingAd": t.proxy(renames["CmTrackingAdOut"]).optional(),
            "skippable": t.boolean().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "integrationCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["MobileDeviceIdListIn"] = t.struct(
        {"mobileDeviceIds": t.array(t.string()).optional()}
    ).named(renames["MobileDeviceIdListIn"])
    types["MobileDeviceIdListOut"] = t.struct(
        {
            "mobileDeviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileDeviceIdListOut"])
    types["MoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["ReplaceSitesResponseIn"] = t.struct(
        {"sites": t.array(t.proxy(renames["SiteIn"])).optional()}
    ).named(renames["ReplaceSitesResponseIn"])
    types["ReplaceSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceSitesResponseOut"])
    types["SensitiveCategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"excludedSensitiveCategory": t.string()}
    ).named(renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"])
    types["SensitiveCategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "excludedSensitiveCategory": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveCategoryAssignedTargetingOptionDetailsOut"])
    types["PartnerIn"] = t.struct(
        {
            "generalConfig": t.proxy(renames["PartnerGeneralConfigIn"]).optional(),
            "exchangeConfig": t.proxy(renames["ExchangeConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "dataAccessConfig": t.proxy(
                renames["PartnerDataAccessConfigIn"]
            ).optional(),
            "adServerConfig": t.proxy(renames["PartnerAdServerConfigIn"]).optional(),
        }
    ).named(renames["PartnerIn"])
    types["PartnerOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "generalConfig": t.proxy(renames["PartnerGeneralConfigOut"]).optional(),
            "partnerId": t.string().optional(),
            "name": t.string().optional(),
            "exchangeConfig": t.proxy(renames["ExchangeConfigOut"]).optional(),
            "entityStatus": t.string().optional(),
            "displayName": t.string().optional(),
            "dataAccessConfig": t.proxy(
                renames["PartnerDataAccessConfigOut"]
            ).optional(),
            "adServerConfig": t.proxy(renames["PartnerAdServerConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerOut"])
    types["BulkListCampaignAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["BulkListCampaignAssignedTargetingOptionsResponseIn"])
    types["BulkListCampaignAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListCampaignAssignedTargetingOptionsResponseOut"])
    types["ContentDurationTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentDurationTargetingOptionDetailsIn"])
    types["ContentDurationTargetingOptionDetailsOut"] = t.struct(
        {
            "contentDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentDurationTargetingOptionDetailsOut"])
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
    types["LanguageAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["LanguageAssignedTargetingOptionDetailsIn"])
    types["LanguageAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageAssignedTargetingOptionDetailsOut"])
    types["InsertionOrderBudgetSegmentIn"] = t.struct(
        {
            "budgetAmountMicros": t.string(),
            "campaignBudgetId": t.string().optional(),
            "description": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]),
        }
    ).named(renames["InsertionOrderBudgetSegmentIn"])
    types["InsertionOrderBudgetSegmentOut"] = t.struct(
        {
            "budgetAmountMicros": t.string(),
            "campaignBudgetId": t.string().optional(),
            "description": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderBudgetSegmentOut"])
    types["AssetAssociationIn"] = t.struct(
        {"role": t.string().optional(), "asset": t.proxy(renames["AssetIn"]).optional()}
    ).named(renames["AssetAssociationIn"])
    types["AssetAssociationOut"] = t.struct(
        {
            "role": t.string().optional(),
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetAssociationOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
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
    types["CmHybridConfigIn"] = t.struct(
        {
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "cmSyncableSiteIds": t.array(t.string()).optional(),
            "cmFloodlightLinkingAuthorized": t.boolean(),
            "cmAccountId": t.string(),
            "cmFloodlightConfigId": t.string(),
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
        }
    ).named(renames["CmHybridConfigIn"])
    types["CmHybridConfigOut"] = t.struct(
        {
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "cmSyncableSiteIds": t.array(t.string()).optional(),
            "cmFloodlightLinkingAuthorized": t.boolean(),
            "cmAccountId": t.string(),
            "cmFloodlightConfigId": t.string(),
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmHybridConfigOut"])
    types["PoiTargetingOptionDetailsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PoiTargetingOptionDetailsIn"]
    )
    types["PoiTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiTargetingOptionDetailsOut"])
    types["InsertionOrderBudgetIn"] = t.struct(
        {
            "budgetSegments": t.array(
                t.proxy(renames["InsertionOrderBudgetSegmentIn"])
            ),
            "budgetUnit": t.string(),
            "automationType": t.string().optional(),
        }
    ).named(renames["InsertionOrderBudgetIn"])
    types["InsertionOrderBudgetOut"] = t.struct(
        {
            "budgetSegments": t.array(
                t.proxy(renames["InsertionOrderBudgetSegmentOut"])
            ),
            "budgetUnit": t.string(),
            "automationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderBudgetOut"])
    types["EditGuaranteedOrderReadAccessorsResponseIn"] = t.struct(
        {
            "readAdvertiserIds": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsResponseIn"])
    types["EditGuaranteedOrderReadAccessorsResponseOut"] = t.struct(
        {
            "readAdvertiserIds": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsResponseOut"])
    types["BulkEditNegativeKeywordsRequestIn"] = t.struct(
        {
            "deletedNegativeKeywords": t.array(t.string()).optional(),
            "createdNegativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordIn"])
            ).optional(),
        }
    ).named(renames["BulkEditNegativeKeywordsRequestIn"])
    types["BulkEditNegativeKeywordsRequestOut"] = t.struct(
        {
            "deletedNegativeKeywords": t.array(t.string()).optional(),
            "createdNegativeKeywords": t.array(
                t.proxy(renames["NegativeKeywordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditNegativeKeywordsRequestOut"])
    types["AuthorizedSellerStatusTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizedSellerStatusTargetingOptionDetailsIn"])
    types["AuthorizedSellerStatusTargetingOptionDetailsOut"] = t.struct(
        {
            "authorizedSellerStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedSellerStatusTargetingOptionDetailsOut"])
    types["AudioVideoOffsetIn"] = t.struct(
        {"seconds": t.string().optional(), "percentage": t.string().optional()}
    ).named(renames["AudioVideoOffsetIn"])
    types["AudioVideoOffsetOut"] = t.struct(
        {
            "seconds": t.string().optional(),
            "percentage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioVideoOffsetOut"])
    types["EnvironmentAssignedTargetingOptionDetailsIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["EnvironmentAssignedTargetingOptionDetailsIn"])
    types["EnvironmentAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentAssignedTargetingOptionDetailsOut"])
    types["GenderTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenderTargetingOptionDetailsIn"])
    types["GenderTargetingOptionDetailsOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderTargetingOptionDetailsOut"])
    types["SessionPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"sessionPosition": t.string().optional()}
    ).named(renames["SessionPositionAssignedTargetingOptionDetailsIn"])
    types["SessionPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "sessionPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionPositionAssignedTargetingOptionDetailsOut"])
    types["AppCategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["AppCategoryAssignedTargetingOptionDetailsIn"])
    types["AppCategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppCategoryAssignedTargetingOptionDetailsOut"])
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
    types["AgeRangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"ageRange": t.string().optional()}
    ).named(renames["AgeRangeAssignedTargetingOptionDetailsIn"])
    types["AgeRangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeAssignedTargetingOptionDetailsOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["MastheadAdIn"] = t.struct(
        {
            "callToActionTrackingUrl": t.string().optional(),
            "autoplayVideoStartMillisecond": t.string().optional(),
            "videoAspectRatio": t.string().optional(),
            "description": t.string().optional(),
            "companionYoutubeVideos": t.array(
                t.proxy(renames["YoutubeVideoDetailsIn"])
            ).optional(),
            "headline": t.string().optional(),
            "callToActionButtonLabel": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "autoplayVideoDuration": t.string().optional(),
            "callToActionFinalUrl": t.string().optional(),
            "showChannelArt": t.boolean().optional(),
        }
    ).named(renames["MastheadAdIn"])
    types["MastheadAdOut"] = t.struct(
        {
            "callToActionTrackingUrl": t.string().optional(),
            "autoplayVideoStartMillisecond": t.string().optional(),
            "videoAspectRatio": t.string().optional(),
            "description": t.string().optional(),
            "companionYoutubeVideos": t.array(
                t.proxy(renames["YoutubeVideoDetailsOut"])
            ).optional(),
            "headline": t.string().optional(),
            "callToActionButtonLabel": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "autoplayVideoDuration": t.string().optional(),
            "callToActionFinalUrl": t.string().optional(),
            "showChannelArt": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MastheadAdOut"])
    types["ReviewStatusInfoIn"] = t.struct(
        {
            "approvalStatus": t.string().optional(),
            "creativeAndLandingPageReviewStatus": t.string().optional(),
            "publisherReviewStatuses": t.array(
                t.proxy(renames["PublisherReviewStatusIn"])
            ).optional(),
            "contentAndPolicyReviewStatus": t.string().optional(),
            "exchangeReviewStatuses": t.array(
                t.proxy(renames["ExchangeReviewStatusIn"])
            ).optional(),
        }
    ).named(renames["ReviewStatusInfoIn"])
    types["ReviewStatusInfoOut"] = t.struct(
        {
            "approvalStatus": t.string().optional(),
            "creativeAndLandingPageReviewStatus": t.string().optional(),
            "publisherReviewStatuses": t.array(
                t.proxy(renames["PublisherReviewStatusOut"])
            ).optional(),
            "contentAndPolicyReviewStatus": t.string().optional(),
            "exchangeReviewStatuses": t.array(
                t.proxy(renames["ExchangeReviewStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewStatusInfoOut"])
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
    types["ViewabilityTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ViewabilityTargetingOptionDetailsIn"])
    types["ViewabilityTargetingOptionDetailsOut"] = t.struct(
        {
            "viewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewabilityTargetingOptionDetailsOut"])
    types["OmidTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OmidTargetingOptionDetailsIn"])
    types["OmidTargetingOptionDetailsOut"] = t.struct(
        {
            "omid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmidTargetingOptionDetailsOut"])
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
    types["ContentDurationAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["ContentDurationAssignedTargetingOptionDetailsIn"])
    types["ContentDurationAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "contentDuration": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentDurationAssignedTargetingOptionDetailsOut"])
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
    types["ActiveViewVideoViewabilityMetricConfigIn"] = t.struct(
        {
            "minimumViewability": t.string(),
            "displayName": t.string(),
            "minimumDuration": t.string().optional(),
            "minimumQuartile": t.string().optional(),
            "minimumVolume": t.string(),
        }
    ).named(renames["ActiveViewVideoViewabilityMetricConfigIn"])
    types["ActiveViewVideoViewabilityMetricConfigOut"] = t.struct(
        {
            "minimumViewability": t.string(),
            "displayName": t.string(),
            "minimumDuration": t.string().optional(),
            "minimumQuartile": t.string().optional(),
            "minimumVolume": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActiveViewVideoViewabilityMetricConfigOut"])
    types["ParentalStatusAssignedTargetingOptionDetailsIn"] = t.struct(
        {"parentalStatus": t.string().optional()}
    ).named(renames["ParentalStatusAssignedTargetingOptionDetailsIn"])
    types["ParentalStatusAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "parentalStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentalStatusAssignedTargetingOptionDetailsOut"])
    types["LookupInvoiceCurrencyResponseIn"] = t.struct(
        {"currencyCode": t.string().optional()}
    ).named(renames["LookupInvoiceCurrencyResponseIn"])
    types["LookupInvoiceCurrencyResponseOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupInvoiceCurrencyResponseOut"])
    types["LineItemIn"] = t.struct(
        {
            "excludeNewExchanges": t.boolean().optional(),
            "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigIn"]
            ).optional(),
            "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
            "conversionCounting": t.proxy(
                renames["ConversionCountingConfigIn"]
            ).optional(),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
            "entityStatus": t.string(),
            "insertionOrderId": t.string(),
            "creativeIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "budget": t.proxy(renames["LineItemBudgetIn"]),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "pacing": t.proxy(renames["PacingIn"]),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "flight": t.proxy(renames["LineItemFlightIn"]),
            "lineItemType": t.string(),
        }
    ).named(renames["LineItemIn"])
    types["LineItemOut"] = t.struct(
        {
            "youtubeAndPartnersSettings": t.proxy(
                renames["YoutubeAndPartnersSettingsOut"]
            ).optional(),
            "excludeNewExchanges": t.boolean().optional(),
            "bidStrategy": t.proxy(renames["BiddingStrategyOut"]),
            "reservationType": t.string().optional(),
            "advertiserId": t.string().optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigOut"]
            ).optional(),
            "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelOut"]),
            "conversionCounting": t.proxy(
                renames["ConversionCountingConfigOut"]
            ).optional(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "entityStatus": t.string(),
            "insertionOrderId": t.string(),
            "creativeIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "budget": t.proxy(renames["LineItemBudgetOut"]),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostOut"])).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "lineItemId": t.string().optional(),
            "pacing": t.proxy(renames["PacingOut"]),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "campaignId": t.string().optional(),
            "updateTime": t.string().optional(),
            "flight": t.proxy(renames["LineItemFlightOut"]),
            "name": t.string().optional(),
            "lineItemType": t.string(),
            "warningMessages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemOut"])
    types["ParentEntityFilterIn"] = t.struct(
        {
            "fileType": t.array(t.string()),
            "filterIds": t.array(t.string()).optional(),
            "filterType": t.string(),
        }
    ).named(renames["ParentEntityFilterIn"])
    types["ParentEntityFilterOut"] = t.struct(
        {
            "fileType": t.array(t.string()),
            "filterIds": t.array(t.string()).optional(),
            "filterType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentEntityFilterOut"])
    types["ObaIconIn"] = t.struct(
        {
            "program": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]).optional(),
            "resourceMimeType": t.string().optional(),
            "viewTrackingUrl": t.string(),
            "position": t.string().optional(),
            "landingPageUrl": t.string(),
            "clickTrackingUrl": t.string(),
            "resourceUrl": t.string().optional(),
        }
    ).named(renames["ObaIconIn"])
    types["ObaIconOut"] = t.struct(
        {
            "program": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]).optional(),
            "resourceMimeType": t.string().optional(),
            "viewTrackingUrl": t.string(),
            "position": t.string().optional(),
            "landingPageUrl": t.string(),
            "clickTrackingUrl": t.string(),
            "resourceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObaIconOut"])
    types["BrowserAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["BrowserAssignedTargetingOptionDetailsIn"])
    types["BrowserAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserAssignedTargetingOptionDetailsOut"])
    types["AssignedLocationIn"] = t.struct({"targetingOptionId": t.string()}).named(
        renames["AssignedLocationIn"]
    )
    types["AssignedLocationOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "assignedLocationId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedLocationOut"])
    types["TargetingExpansionConfigIn"] = t.struct(
        {
            "excludeFirstPartyAudience": t.boolean().optional(),
            "targetingExpansionLevel": t.string(),
        }
    ).named(renames["TargetingExpansionConfigIn"])
    types["TargetingExpansionConfigOut"] = t.struct(
        {
            "excludeFirstPartyAudience": t.boolean().optional(),
            "targetingExpansionLevel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingExpansionConfigOut"])
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
    types["OmidAssignedTargetingOptionDetailsIn"] = t.struct(
        {"omid": t.string().optional()}
    ).named(renames["OmidAssignedTargetingOptionDetailsIn"])
    types["OmidAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "omid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmidAssignedTargetingOptionDetailsOut"])
    types["AudioContentTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AudioContentTypeTargetingOptionDetailsIn"])
    types["AudioContentTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "audioContentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioContentTypeTargetingOptionDetailsOut"])
    types["ContentOutstreamPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentOutstreamPositionTargetingOptionDetailsIn"])
    types["ContentOutstreamPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentOutstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOutstreamPositionTargetingOptionDetailsOut"])
    types["VideoDiscoveryAdIn"] = t.struct(
        {
            "description2": t.string().optional(),
            "description1": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "headline": t.string().optional(),
            "thumbnail": t.string().optional(),
        }
    ).named(renames["VideoDiscoveryAdIn"])
    types["VideoDiscoveryAdOut"] = t.struct(
        {
            "description2": t.string().optional(),
            "description1": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "headline": t.string().optional(),
            "thumbnail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoDiscoveryAdOut"])
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
    types["EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"] = t.struct(
        {
            "addedAdvertisers": t.array(t.string()).optional(),
            "removedAdvertisers": t.array(t.string()).optional(),
        }
    ).named(renames["EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"])
    types[
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut"
    ] = t.struct(
        {
            "addedAdvertisers": t.array(t.string()).optional(),
            "removedAdvertisers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut"]
    )
    types["UserIn"] = t.struct(
        {
            "assignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleIn"])
            ).optional(),
            "displayName": t.string(),
            "email": t.string(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "name": t.string().optional(),
            "assignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleOut"])
            ).optional(),
            "displayName": t.string(),
            "userId": t.string().optional(),
            "email": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["InventorySourceDisplayCreativeConfigIn"] = t.struct(
        {"creativeSize": t.proxy(renames["DimensionsIn"]).optional()}
    ).named(renames["InventorySourceDisplayCreativeConfigIn"])
    types["InventorySourceDisplayCreativeConfigOut"] = t.struct(
        {
            "creativeSize": t.proxy(renames["DimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceDisplayCreativeConfigOut"])
    types["ListYoutubeAdGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "youtubeAdGroups": t.array(t.proxy(renames["YoutubeAdGroupIn"])).optional(),
        }
    ).named(renames["ListYoutubeAdGroupsResponseIn"])
    types["ListYoutubeAdGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "youtubeAdGroups": t.array(
                t.proxy(renames["YoutubeAdGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListYoutubeAdGroupsResponseOut"])
    types["VideoPlayerSizeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"videoPlayerSize": t.string().optional()}
    ).named(renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"])
    types["VideoPlayerSizeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "videoPlayerSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerSizeAssignedTargetingOptionDetailsOut"])
    types["AppAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "appId": t.string(),
            "negative": t.boolean().optional(),
            "appPlatform": t.string().optional(),
        }
    ).named(renames["AppAssignedTargetingOptionDetailsIn"])
    types["AppAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "appId": t.string(),
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "appPlatform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppAssignedTargetingOptionDetailsOut"])
    types["BulkEditAdvertiserAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
            ).optional(),
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
            ).optional(),
        }
    ).named(renames["BulkEditAdvertiserAssignedTargetingOptionsRequestIn"])
    types["BulkEditAdvertiserAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAdvertiserAssignedTargetingOptionsRequestOut"])
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
    types["CategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["CategoryAssignedTargetingOptionDetailsIn"])
    types["CategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryAssignedTargetingOptionDetailsOut"])
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
    types["LineItemBudgetIn"] = t.struct(
        {"budgetAllocationType": t.string(), "maxAmount": t.string().optional()}
    ).named(renames["LineItemBudgetIn"])
    types["LineItemBudgetOut"] = t.struct(
        {
            "budgetAllocationType": t.string(),
            "budgetUnit": t.string().optional(),
            "maxAmount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemBudgetOut"])
    types["PrismaCpeCodeIn"] = t.struct(
        {
            "prismaClientCode": t.string().optional(),
            "prismaProductCode": t.string().optional(),
            "prismaEstimateCode": t.string().optional(),
        }
    ).named(renames["PrismaCpeCodeIn"])
    types["PrismaCpeCodeOut"] = t.struct(
        {
            "prismaClientCode": t.string().optional(),
            "prismaProductCode": t.string().optional(),
            "prismaEstimateCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrismaCpeCodeOut"])
    types["VideoAdSequenceStepIn"] = t.struct(
        {
            "interactionType": t.string().optional(),
            "previousStepId": t.string().optional(),
            "stepId": t.string().optional(),
            "adGroupId": t.string().optional(),
        }
    ).named(renames["VideoAdSequenceStepIn"])
    types["VideoAdSequenceStepOut"] = t.struct(
        {
            "interactionType": t.string().optional(),
            "previousStepId": t.string().optional(),
            "stepId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAdSequenceStepOut"])
    types["YoutubeAndPartnersInventorySourceConfigIn"] = t.struct(
        {
            "includeYoutubeSearch": t.boolean().optional(),
            "includeYoutubeVideos": t.boolean().optional(),
            "includeYoutubeVideoPartners": t.boolean().optional(),
        }
    ).named(renames["YoutubeAndPartnersInventorySourceConfigIn"])
    types["YoutubeAndPartnersInventorySourceConfigOut"] = t.struct(
        {
            "includeYoutubeSearch": t.boolean().optional(),
            "includeYoutubeVideos": t.boolean().optional(),
            "includeYoutubeVideoPartners": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersInventorySourceConfigOut"])
    types["MaximizeSpendBidStrategyIn"] = t.struct(
        {
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalType": t.string(),
            "raiseBidForDeals": t.boolean().optional(),
        }
    ).named(renames["MaximizeSpendBidStrategyIn"])
    types["MaximizeSpendBidStrategyOut"] = t.struct(
        {
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalType": t.string(),
            "raiseBidForDeals": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaximizeSpendBidStrategyOut"])
    types["AgeRangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AgeRangeTargetingOptionDetailsIn"])
    types["AgeRangeTargetingOptionDetailsOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeTargetingOptionDetailsOut"])
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
    types["GenerateDefaultLineItemRequestIn"] = t.struct(
        {
            "insertionOrderId": t.string(),
            "lineItemType": t.string(),
            "displayName": t.string(),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
        }
    ).named(renames["GenerateDefaultLineItemRequestIn"])
    types["GenerateDefaultLineItemRequestOut"] = t.struct(
        {
            "insertionOrderId": t.string(),
            "lineItemType": t.string(),
            "displayName": t.string(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateDefaultLineItemRequestOut"])
    types["GuaranteedOrderIn"] = t.struct(
        {
            "exchange": t.string(),
            "readAccessInherited": t.boolean().optional(),
            "defaultCampaignId": t.string().optional(),
            "status": t.proxy(renames["GuaranteedOrderStatusIn"]).optional(),
            "publisherName": t.string(),
            "readWriteAdvertiserId": t.string().optional(),
            "readWritePartnerId": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "displayName": t.string(),
        }
    ).named(renames["GuaranteedOrderIn"])
    types["GuaranteedOrderOut"] = t.struct(
        {
            "defaultAdvertiserId": t.string().optional(),
            "exchange": t.string(),
            "guaranteedOrderId": t.string().optional(),
            "readAccessInherited": t.boolean().optional(),
            "defaultCampaignId": t.string().optional(),
            "name": t.string().optional(),
            "legacyGuaranteedOrderId": t.string().optional(),
            "status": t.proxy(renames["GuaranteedOrderStatusOut"]).optional(),
            "updateTime": t.string().optional(),
            "publisherName": t.string(),
            "readWriteAdvertiserId": t.string().optional(),
            "readWritePartnerId": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedOrderOut"])
    types["DeactivateManualTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateManualTriggerRequestIn"])
    types["DeactivateManualTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateManualTriggerRequestOut"])
    types["DeviceMakeModelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"])
    types["DeviceMakeModelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMakeModelAssignedTargetingOptionDetailsOut"])
    types["ThirdPartyOnlyConfigIn"] = t.struct(
        {"pixelOrderIdReportingEnabled": t.boolean().optional()}
    ).named(renames["ThirdPartyOnlyConfigIn"])
    types["ThirdPartyOnlyConfigOut"] = t.struct(
        {
            "pixelOrderIdReportingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyOnlyConfigOut"])
    types["CombinedAudienceTargetingSettingIn"] = t.struct(
        {"combinedAudienceId": t.string()}
    ).named(renames["CombinedAudienceTargetingSettingIn"])
    types["CombinedAudienceTargetingSettingOut"] = t.struct(
        {
            "combinedAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CombinedAudienceTargetingSettingOut"])
    types["SubExchangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["SubExchangeAssignedTargetingOptionDetailsIn"])
    types["SubExchangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubExchangeAssignedTargetingOptionDetailsOut"])
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
    types["ListTargetingOptionsResponseIn"] = t.struct(
        {
            "targetingOptions": t.array(
                t.proxy(renames["TargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTargetingOptionsResponseIn"])
    types["ListTargetingOptionsResponseOut"] = t.struct(
        {
            "targetingOptions": t.array(
                t.proxy(renames["TargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetingOptionsResponseOut"])
    types["HouseholdIncomeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"householdIncome": t.string().optional()}
    ).named(renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"])
    types["HouseholdIncomeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "householdIncome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HouseholdIncomeAssignedTargetingOptionDetailsOut"])
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
    types["BulkEditSitesRequestIn"] = t.struct(
        {
            "deletedSites": t.array(t.string()).optional(),
            "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["BulkEditSitesRequestIn"])
    types["BulkEditSitesRequestOut"] = t.struct(
        {
            "deletedSites": t.array(t.string()).optional(),
            "createdSites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditSitesRequestOut"])
    types["InventorySourceIn"] = t.struct(
        {
            "guaranteedOrderId": t.string().optional(),
            "deliveryMethod": t.string().optional(),
            "readWriteAccessors": t.proxy(
                renames["InventorySourceAccessorsIn"]
            ).optional(),
            "publisherName": t.string().optional(),
            "rateDetails": t.proxy(renames["RateDetailsIn"]),
            "exchange": t.string().optional(),
            "commitment": t.string().optional(),
            "status": t.proxy(renames["InventorySourceStatusIn"]).optional(),
            "creativeConfigs": t.array(t.proxy(renames["CreativeConfigIn"])).optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "inventorySourceType": t.string().optional(),
            "dealId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["InventorySourceIn"])
    types["InventorySourceOut"] = t.struct(
        {
            "guaranteedOrderId": t.string().optional(),
            "deliveryMethod": t.string().optional(),
            "readWriteAccessors": t.proxy(
                renames["InventorySourceAccessorsOut"]
            ).optional(),
            "publisherName": t.string().optional(),
            "rateDetails": t.proxy(renames["RateDetailsOut"]),
            "name": t.string().optional(),
            "inventorySourceProductType": t.string().optional(),
            "exchange": t.string().optional(),
            "updateTime": t.string().optional(),
            "commitment": t.string().optional(),
            "status": t.proxy(renames["InventorySourceStatusOut"]).optional(),
            "creativeConfigs": t.array(
                t.proxy(renames["CreativeConfigOut"])
            ).optional(),
            "inventorySourceId": t.string().optional(),
            "readPartnerIds": t.array(t.string()).optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "inventorySourceType": t.string().optional(),
            "dealId": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceOut"])
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
    types["ListLineItemsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "lineItems": t.array(t.proxy(renames["LineItemIn"])).optional(),
        }
    ).named(renames["ListLineItemsResponseIn"])
    types["ListLineItemsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "lineItems": t.array(t.proxy(renames["LineItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLineItemsResponseOut"])
    types["AdvertiserTargetingConfigIn"] = t.struct(
        {"exemptTvFromViewabilityTargeting": t.boolean().optional()}
    ).named(renames["AdvertiserTargetingConfigIn"])
    types["AdvertiserTargetingConfigOut"] = t.struct(
        {
            "exemptTvFromViewabilityTargeting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserTargetingConfigOut"])
    types["BulkListInsertionOrderAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseIn"])
    types["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"])
    types["CmTrackingAdIn"] = t.struct(
        {
            "cmCreativeId": t.string().optional(),
            "cmAdId": t.string().optional(),
            "cmPlacementId": t.string().optional(),
        }
    ).named(renames["CmTrackingAdIn"])
    types["CmTrackingAdOut"] = t.struct(
        {
            "cmCreativeId": t.string().optional(),
            "cmAdId": t.string().optional(),
            "cmPlacementId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmTrackingAdOut"])
    types["BulkUpdateLineItemsRequestIn"] = t.struct(
        {
            "targetLineItem": t.proxy(renames["LineItemIn"]),
            "lineItemIds": t.array(t.string()),
            "updateMask": t.string(),
        }
    ).named(renames["BulkUpdateLineItemsRequestIn"])
    types["BulkUpdateLineItemsRequestOut"] = t.struct(
        {
            "targetLineItem": t.proxy(renames["LineItemOut"]),
            "lineItemIds": t.array(t.string()),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkUpdateLineItemsRequestOut"])
    types["VideoPerformanceAdIn"] = t.struct(
        {
            "actionButtonLabels": t.array(t.string()).optional(),
            "trackingUrl": t.string().optional(),
            "longHeadlines": t.array(t.string()).optional(),
            "domain": t.string().optional(),
            "finalUrl": t.string().optional(),
            "companionBanners": t.array(t.proxy(renames["ImageAssetIn"])).optional(),
            "videos": t.array(t.proxy(renames["YoutubeVideoDetailsIn"])).optional(),
            "displayUrlBreadcrumb1": t.string().optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "displayUrlBreadcrumb2": t.string().optional(),
            "headlines": t.array(t.string()).optional(),
            "descriptions": t.array(t.string()).optional(),
        }
    ).named(renames["VideoPerformanceAdIn"])
    types["VideoPerformanceAdOut"] = t.struct(
        {
            "actionButtonLabels": t.array(t.string()).optional(),
            "trackingUrl": t.string().optional(),
            "longHeadlines": t.array(t.string()).optional(),
            "domain": t.string().optional(),
            "finalUrl": t.string().optional(),
            "companionBanners": t.array(t.proxy(renames["ImageAssetOut"])).optional(),
            "videos": t.array(t.proxy(renames["YoutubeVideoDetailsOut"])).optional(),
            "displayUrlBreadcrumb1": t.string().optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "displayUrlBreadcrumb2": t.string().optional(),
            "headlines": t.array(t.string()).optional(),
            "descriptions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPerformanceAdOut"])
    types["AdvertiserDataAccessConfigIn"] = t.struct(
        {"sdfConfig": t.proxy(renames["AdvertiserSdfConfigIn"]).optional()}
    ).named(renames["AdvertiserDataAccessConfigIn"])
    types["AdvertiserDataAccessConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["AdvertiserSdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserDataAccessConfigOut"])
    types["FrequencyCapIn"] = t.struct(
        {
            "timeUnit": t.string().optional(),
            "unlimited": t.boolean().optional(),
            "maxViews": t.integer().optional(),
            "maxImpressions": t.integer().optional(),
            "timeUnitCount": t.integer().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "timeUnit": t.string().optional(),
            "unlimited": t.boolean().optional(),
            "maxViews": t.integer().optional(),
            "maxImpressions": t.integer().optional(),
            "timeUnitCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
    types["ListSitesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sites": t.array(t.proxy(renames["SiteIn"])).optional(),
        }
    ).named(renames["ListSitesResponseIn"])
    types["ListSitesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSitesResponseOut"])
    types["AdvertiserBillingConfigIn"] = t.struct(
        {"billingProfileId": t.string().optional()}
    ).named(renames["AdvertiserBillingConfigIn"])
    types["AdvertiserBillingConfigOut"] = t.struct(
        {
            "billingProfileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserBillingConfigOut"])
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
    types["ManualTriggerIn"] = t.struct(
        {
            "displayName": t.string(),
            "activationDurationMinutes": t.string(),
            "advertiserId": t.string(),
        }
    ).named(renames["ManualTriggerIn"])
    types["ManualTriggerOut"] = t.struct(
        {
            "latestActivationTime": t.string().optional(),
            "displayName": t.string(),
            "activationDurationMinutes": t.string(),
            "advertiserId": t.string(),
            "triggerId": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualTriggerOut"])
    types["AdvertiserCreativeConfigIn"] = t.struct(
        {
            "obaComplianceDisabled": t.boolean().optional(),
            "iasClientId": t.string().optional(),
            "videoCreativeDataSharingAuthorized": t.boolean().optional(),
            "dynamicCreativeEnabled": t.boolean().optional(),
        }
    ).named(renames["AdvertiserCreativeConfigIn"])
    types["AdvertiserCreativeConfigOut"] = t.struct(
        {
            "obaComplianceDisabled": t.boolean().optional(),
            "iasClientId": t.string().optional(),
            "videoCreativeDataSharingAuthorized": t.boolean().optional(),
            "dynamicCreativeEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserCreativeConfigOut"])
    types["ExchangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ExchangeTargetingOptionDetailsIn"])
    types["ExchangeTargetingOptionDetailsOut"] = t.struct(
        {
            "exchange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeTargetingOptionDetailsOut"])
    types["PartnerDataAccessConfigIn"] = t.struct(
        {"sdfConfig": t.proxy(renames["SdfConfigIn"]).optional()}
    ).named(renames["PartnerDataAccessConfigIn"])
    types["PartnerDataAccessConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["SdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerDataAccessConfigOut"])
    types["DuplicateLineItemRequestIn"] = t.struct(
        {"targetDisplayName": t.string().optional()}
    ).named(renames["DuplicateLineItemRequestIn"])
    types["DuplicateLineItemRequestOut"] = t.struct(
        {
            "targetDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateLineItemRequestOut"])
    types["BudgetSummaryIn"] = t.struct(
        {
            "totalAmountMicros": t.string().optional(),
            "preTaxAmountMicros": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeIn"]).optional(),
            "taxAmountMicros": t.string().optional(),
        }
    ).named(renames["BudgetSummaryIn"])
    types["BudgetSummaryOut"] = t.struct(
        {
            "totalAmountMicros": t.string().optional(),
            "preTaxAmountMicros": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeOut"]).optional(),
            "taxAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BudgetSummaryOut"])
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
    types["CarrierAndIspAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["CarrierAndIspAssignedTargetingOptionDetailsIn"])
    types["CarrierAndIspAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarrierAndIspAssignedTargetingOptionDetailsOut"])
    types["CommonInStreamAttributeIn"] = t.struct(
        {
            "displayUrl": t.string().optional(),
            "actionButtonLabel": t.string().optional(),
            "companionBanner": t.proxy(renames["ImageAssetIn"]).optional(),
            "actionHeadline": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "finalUrl": t.string().optional(),
            "trackingUrl": t.string().optional(),
        }
    ).named(renames["CommonInStreamAttributeIn"])
    types["CommonInStreamAttributeOut"] = t.struct(
        {
            "displayUrl": t.string().optional(),
            "actionButtonLabel": t.string().optional(),
            "companionBanner": t.proxy(renames["ImageAssetOut"]).optional(),
            "actionHeadline": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "finalUrl": t.string().optional(),
            "trackingUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonInStreamAttributeOut"])
    types["AdvertiserAdServerConfigIn"] = t.struct(
        {
            "thirdPartyOnlyConfig": t.proxy(
                renames["ThirdPartyOnlyConfigIn"]
            ).optional(),
            "cmHybridConfig": t.proxy(renames["CmHybridConfigIn"]).optional(),
        }
    ).named(renames["AdvertiserAdServerConfigIn"])
    types["AdvertiserAdServerConfigOut"] = t.struct(
        {
            "thirdPartyOnlyConfig": t.proxy(
                renames["ThirdPartyOnlyConfigOut"]
            ).optional(),
            "cmHybridConfig": t.proxy(renames["CmHybridConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserAdServerConfigOut"])
    types["KeywordAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "keyword": t.string()}
    ).named(renames["KeywordAssignedTargetingOptionDetailsIn"])
    types["KeywordAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "keyword": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeywordAssignedTargetingOptionDetailsOut"])
    types["ViewabilityAssignedTargetingOptionDetailsIn"] = t.struct(
        {"viewability": t.string().optional()}
    ).named(renames["ViewabilityAssignedTargetingOptionDetailsIn"])
    types["ViewabilityAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "viewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewabilityAssignedTargetingOptionDetailsOut"])
    types["ListInvoicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "invoices": t.array(t.proxy(renames["InvoiceIn"])).optional(),
        }
    ).named(renames["ListInvoicesResponseIn"])
    types["ListInvoicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "invoices": t.array(t.proxy(renames["InvoiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInvoicesResponseOut"])
    types["AdvertiserSdfConfigIn"] = t.struct(
        {
            "overridePartnerSdfConfig": t.boolean().optional(),
            "sdfConfig": t.proxy(renames["SdfConfigIn"]).optional(),
        }
    ).named(renames["AdvertiserSdfConfigIn"])
    types["AdvertiserSdfConfigOut"] = t.struct(
        {
            "overridePartnerSdfConfig": t.boolean().optional(),
            "sdfConfig": t.proxy(renames["SdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserSdfConfigOut"])
    types["ProductFeedDataIn"] = t.struct(
        {
            "productMatchType": t.string().optional(),
            "isFeedDisabled": t.boolean().optional(),
            "productMatchDimensions": t.array(
                t.proxy(renames["ProductMatchDimensionIn"])
            ).optional(),
        }
    ).named(renames["ProductFeedDataIn"])
    types["ProductFeedDataOut"] = t.struct(
        {
            "productMatchType": t.string().optional(),
            "isFeedDisabled": t.boolean().optional(),
            "productMatchDimensions": t.array(
                t.proxy(renames["ProductMatchDimensionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductFeedDataOut"])
    types["CustomBiddingScriptRefIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["CustomBiddingScriptRefIn"])
    types["CustomBiddingScriptRefOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingScriptRefOut"])
    types["ActivateManualTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivateManualTriggerRequestIn"])
    types["ActivateManualTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateManualTriggerRequestOut"])
    types["ContactInfoIn"] = t.struct(
        {
            "hashedPhoneNumbers": t.array(t.string()).optional(),
            "hashedEmails": t.array(t.string()).optional(),
            "zipCodes": t.array(t.string()).optional(),
            "countryCode": t.string().optional(),
            "hashedFirstName": t.string().optional(),
            "hashedLastName": t.string().optional(),
        }
    ).named(renames["ContactInfoIn"])
    types["ContactInfoOut"] = t.struct(
        {
            "hashedPhoneNumbers": t.array(t.string()).optional(),
            "hashedEmails": t.array(t.string()).optional(),
            "zipCodes": t.array(t.string()).optional(),
            "countryCode": t.string().optional(),
            "hashedFirstName": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoOut"])
    types["IntegralAdScienceIn"] = t.struct(
        {
            "excludedAlcoholRisk": t.string().optional(),
            "excludeUnrateable": t.boolean().optional(),
            "customSegmentId": t.array(t.string()).optional(),
            "excludedIllegalDownloadsRisk": t.string().optional(),
            "excludedGamblingRisk": t.string().optional(),
            "excludedViolenceRisk": t.string().optional(),
            "traqScoreOption": t.string().optional(),
            "displayViewability": t.string().optional(),
            "excludedDrugsRisk": t.string().optional(),
            "excludedAdFraudRisk": t.string().optional(),
            "excludedHateSpeechRisk": t.string().optional(),
            "excludedAdultRisk": t.string().optional(),
            "excludedOffensiveLanguageRisk": t.string().optional(),
            "videoViewability": t.string().optional(),
        }
    ).named(renames["IntegralAdScienceIn"])
    types["IntegralAdScienceOut"] = t.struct(
        {
            "excludedAlcoholRisk": t.string().optional(),
            "excludeUnrateable": t.boolean().optional(),
            "customSegmentId": t.array(t.string()).optional(),
            "excludedIllegalDownloadsRisk": t.string().optional(),
            "excludedGamblingRisk": t.string().optional(),
            "excludedViolenceRisk": t.string().optional(),
            "traqScoreOption": t.string().optional(),
            "displayViewability": t.string().optional(),
            "excludedDrugsRisk": t.string().optional(),
            "excludedAdFraudRisk": t.string().optional(),
            "excludedHateSpeechRisk": t.string().optional(),
            "excludedAdultRisk": t.string().optional(),
            "excludedOffensiveLanguageRisk": t.string().optional(),
            "videoViewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegralAdScienceOut"])
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
    types["DoubleVerifyFraudInvalidTrafficIn"] = t.struct(
        {
            "avoidedFraudOption": t.string().optional(),
            "avoidInsufficientOption": t.boolean().optional(),
        }
    ).named(renames["DoubleVerifyFraudInvalidTrafficIn"])
    types["DoubleVerifyFraudInvalidTrafficOut"] = t.struct(
        {
            "avoidedFraudOption": t.string().optional(),
            "avoidInsufficientOption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyFraudInvalidTrafficOut"])
    types["YoutubeAdGroupIn"] = t.struct(
        {
            "adGroupFormat": t.string().optional(),
            "name": t.string().optional(),
            "entityStatus": t.string().optional(),
            "advertiserId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyIn"]
            ).optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigIn"]
            ).optional(),
            "productFeedData": t.proxy(renames["ProductFeedDataIn"]).optional(),
            "lineItemId": t.string().optional(),
            "displayName": t.string().optional(),
            "youtubeAdIds": t.array(t.string()).optional(),
        }
    ).named(renames["YoutubeAdGroupIn"])
    types["YoutubeAdGroupOut"] = t.struct(
        {
            "adGroupFormat": t.string().optional(),
            "name": t.string().optional(),
            "entityStatus": t.string().optional(),
            "advertiserId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyOut"]
            ).optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigOut"]
            ).optional(),
            "productFeedData": t.proxy(renames["ProductFeedDataOut"]).optional(),
            "lineItemId": t.string().optional(),
            "displayName": t.string().optional(),
            "youtubeAdIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupOut"])
    types["AssignedUserRoleIn"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "userRole": t.string(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["AssignedUserRoleIn"])
    types["AssignedUserRoleOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "userRole": t.string(),
            "advertiserId": t.string().optional(),
            "assignedUserRoleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedUserRoleOut"])
    types["PerformanceGoalIn"] = t.struct(
        {
            "performanceGoalType": t.string(),
            "performanceGoalString": t.string().optional(),
            "performanceGoalPercentageMicros": t.string().optional(),
            "performanceGoalAmountMicros": t.string().optional(),
        }
    ).named(renames["PerformanceGoalIn"])
    types["PerformanceGoalOut"] = t.struct(
        {
            "performanceGoalType": t.string(),
            "performanceGoalString": t.string().optional(),
            "performanceGoalPercentageMicros": t.string().optional(),
            "performanceGoalAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceGoalOut"])
    types["CampaignFlightIn"] = t.struct(
        {
            "plannedDates": t.proxy(renames["DateRangeIn"]),
            "plannedSpendAmountMicros": t.string().optional(),
        }
    ).named(renames["CampaignFlightIn"])
    types["CampaignFlightOut"] = t.struct(
        {
            "plannedDates": t.proxy(renames["DateRangeOut"]),
            "plannedSpendAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignFlightOut"])
    types["LocationListIn"] = t.struct(
        {
            "advertiserId": t.string(),
            "displayName": t.string(),
            "locationType": t.string(),
        }
    ).named(renames["LocationListIn"])
    types["LocationListOut"] = t.struct(
        {
            "advertiserId": t.string(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "locationListId": t.string().optional(),
            "locationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationListOut"])
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
    types["CategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CategoryTargetingOptionDetailsIn"])
    types["CategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryTargetingOptionDetailsOut"])
    types["HouseholdIncomeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["HouseholdIncomeTargetingOptionDetailsIn"])
    types["HouseholdIncomeTargetingOptionDetailsOut"] = t.struct(
        {
            "householdIncome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HouseholdIncomeTargetingOptionDetailsOut"])
    types["AuditAdvertiserResponseIn"] = t.struct(
        {
            "usedInsertionOrdersCount": t.string().optional(),
            "campaignCriteriaCount": t.string().optional(),
            "negativeKeywordListsCount": t.string().optional(),
            "adGroupCriteriaCount": t.string().optional(),
            "usedLineItemsCount": t.string().optional(),
            "negativelyTargetedChannelsCount": t.string().optional(),
            "usedCampaignsCount": t.string().optional(),
            "channelsCount": t.string().optional(),
        }
    ).named(renames["AuditAdvertiserResponseIn"])
    types["AuditAdvertiserResponseOut"] = t.struct(
        {
            "usedInsertionOrdersCount": t.string().optional(),
            "campaignCriteriaCount": t.string().optional(),
            "negativeKeywordListsCount": t.string().optional(),
            "adGroupCriteriaCount": t.string().optional(),
            "usedLineItemsCount": t.string().optional(),
            "negativelyTargetedChannelsCount": t.string().optional(),
            "usedCampaignsCount": t.string().optional(),
            "channelsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditAdvertiserResponseOut"])
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
    types["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "integralAdScience": t.proxy(renames["IntegralAdScienceIn"]).optional(),
            "doubleVerify": t.proxy(renames["DoubleVerifyIn"]).optional(),
            "adloox": t.proxy(renames["AdlooxIn"]).optional(),
        }
    ).named(renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"])
    types["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "integralAdScience": t.proxy(renames["IntegralAdScienceOut"]).optional(),
            "doubleVerify": t.proxy(renames["DoubleVerifyOut"]).optional(),
            "adloox": t.proxy(renames["AdlooxOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"])
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
    types["VideoPlayerSizeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VideoPlayerSizeTargetingOptionDetailsIn"])
    types["VideoPlayerSizeTargetingOptionDetailsOut"] = t.struct(
        {
            "videoPlayerSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerSizeTargetingOptionDetailsOut"])
    types["ListAdvertiserAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["ListAdvertiserAssignedTargetingOptionsResponseIn"])
    types["ListAdvertiserAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAdvertiserAssignedTargetingOptionsResponseOut"])
    types["ThirdPartyVendorConfigIn"] = t.struct(
        {"vendor": t.string().optional(), "placementId": t.string().optional()}
    ).named(renames["ThirdPartyVendorConfigIn"])
    types["ThirdPartyVendorConfigOut"] = t.struct(
        {
            "vendor": t.string().optional(),
            "placementId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyVendorConfigOut"])
    types["ListInventorySourceGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inventorySourceGroups": t.array(
                t.proxy(renames["InventorySourceGroupIn"])
            ).optional(),
        }
    ).named(renames["ListInventorySourceGroupsResponseIn"])
    types["ListInventorySourceGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inventorySourceGroups": t.array(
                t.proxy(renames["InventorySourceGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInventorySourceGroupsResponseOut"])
    types["DisplayVideoSourceAdIn"] = t.struct(
        {"creativeId": t.string().optional()}
    ).named(renames["DisplayVideoSourceAdIn"])
    types["DisplayVideoSourceAdOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayVideoSourceAdOut"])
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
    types["DoubleVerifyAppStarRatingIn"] = t.struct(
        {
            "avoidInsufficientStarRating": t.boolean().optional(),
            "avoidedStarRating": t.string().optional(),
        }
    ).named(renames["DoubleVerifyAppStarRatingIn"])
    types["DoubleVerifyAppStarRatingOut"] = t.struct(
        {
            "avoidInsufficientStarRating": t.boolean().optional(),
            "avoidedStarRating": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyAppStarRatingOut"])
    types["TargetingOptionIn"] = t.struct(
        {
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeTargetingOptionDetailsIn"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusTargetingOptionDetailsIn"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderTargetingOptionDetailsIn"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeTargetingOptionDetailsIn"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelTargetingOptionDetailsIn"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspTargetingOptionDetailsIn"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeTargetingOptionDetailsIn"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionTargetingOptionDetailsIn"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemTargetingOptionDetailsIn"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionTargetingOptionDetailsIn"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryTargetingOptionDetailsIn"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreTargetingOptionDetailsIn"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityTargetingOptionDetailsIn"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationTargetingOptionDetailsIn"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeTargetingOptionDetailsIn"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeTargetingOptionDetailsIn"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeTargetingOptionDetailsIn"]
            ).optional(),
            "digitalContentLabelDetails": t.proxy(
                renames["DigitalContentLabelTargetingOptionDetailsIn"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainTargetingOptionDetailsIn"]
            ).optional(),
            "sensitiveCategoryDetails": t.proxy(
                renames["SensitiveCategoryTargetingOptionDetailsIn"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionTargetingOptionDetailsIn"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryTargetingOptionDetailsIn"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionTargetingOptionDetailsIn"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusTargetingOptionDetailsIn"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeTargetingOptionDetailsIn"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentTargetingOptionDetailsIn"]
            ).optional(),
            "poiDetails": t.proxy(renames["PoiTargetingOptionDetailsIn"]).optional(),
            "omidDetails": t.proxy(renames["OmidTargetingOptionDetailsIn"]).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionTargetingOptionDetailsIn"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserTargetingOptionDetailsIn"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentTargetingOptionDetailsIn"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageTargetingOptionDetailsIn"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeTargetingOptionDetailsIn"]
            ).optional(),
        }
    ).named(renames["TargetingOptionIn"])
    types["TargetingOptionOut"] = t.struct(
        {
            "targetingType": t.string().optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeTargetingOptionDetailsOut"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusTargetingOptionDetailsOut"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderTargetingOptionDetailsOut"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeTargetingOptionDetailsOut"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelTargetingOptionDetailsOut"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspTargetingOptionDetailsOut"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeTargetingOptionDetailsOut"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionTargetingOptionDetailsOut"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemTargetingOptionDetailsOut"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionTargetingOptionDetailsOut"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryTargetingOptionDetailsOut"]
            ).optional(),
            "targetingOptionId": t.string().optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreTargetingOptionDetailsOut"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityTargetingOptionDetailsOut"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationTargetingOptionDetailsOut"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeTargetingOptionDetailsOut"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeTargetingOptionDetailsOut"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeTargetingOptionDetailsOut"]
            ).optional(),
            "digitalContentLabelDetails": t.proxy(
                renames["DigitalContentLabelTargetingOptionDetailsOut"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainTargetingOptionDetailsOut"]
            ).optional(),
            "sensitiveCategoryDetails": t.proxy(
                renames["SensitiveCategoryTargetingOptionDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionTargetingOptionDetailsOut"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryTargetingOptionDetailsOut"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionTargetingOptionDetailsOut"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusTargetingOptionDetailsOut"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeTargetingOptionDetailsOut"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentTargetingOptionDetailsOut"]
            ).optional(),
            "poiDetails": t.proxy(renames["PoiTargetingOptionDetailsOut"]).optional(),
            "omidDetails": t.proxy(renames["OmidTargetingOptionDetailsOut"]).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionTargetingOptionDetailsOut"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserTargetingOptionDetailsOut"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentTargetingOptionDetailsOut"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageTargetingOptionDetailsOut"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeTargetingOptionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingOptionOut"])
    types["CreativeConfigIn"] = t.struct(
        {
            "videoCreativeConfig": t.proxy(
                renames["InventorySourceVideoCreativeConfigIn"]
            ).optional(),
            "creativeType": t.string().optional(),
            "displayCreativeConfig": t.proxy(
                renames["InventorySourceDisplayCreativeConfigIn"]
            ).optional(),
        }
    ).named(renames["CreativeConfigIn"])
    types["CreativeConfigOut"] = t.struct(
        {
            "videoCreativeConfig": t.proxy(
                renames["InventorySourceVideoCreativeConfigOut"]
            ).optional(),
            "creativeType": t.string().optional(),
            "displayCreativeConfig": t.proxy(
                renames["InventorySourceDisplayCreativeConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeConfigOut"])
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
    types["AudioContentTypeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"audioContentType": t.string().optional()}
    ).named(renames["AudioContentTypeAssignedTargetingOptionDetailsIn"])
    types["AudioContentTypeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "audioContentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioContentTypeAssignedTargetingOptionDetailsOut"])
    types["BiddingStrategyIn"] = t.struct(
        {
            "fixedBid": t.proxy(renames["FixedBidStrategyIn"]).optional(),
            "maximizeSpendAutoBid": t.proxy(
                renames["MaximizeSpendBidStrategyIn"]
            ).optional(),
            "performanceGoalAutoBid": t.proxy(
                renames["PerformanceGoalBidStrategyIn"]
            ).optional(),
        }
    ).named(renames["BiddingStrategyIn"])
    types["BiddingStrategyOut"] = t.struct(
        {
            "fixedBid": t.proxy(renames["FixedBidStrategyOut"]).optional(),
            "maximizeSpendAutoBid": t.proxy(
                renames["MaximizeSpendBidStrategyOut"]
            ).optional(),
            "performanceGoalAutoBid": t.proxy(
                renames["PerformanceGoalBidStrategyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiddingStrategyOut"])
    types["BulkUpdateLineItemsResponseIn"] = t.struct(
        {
            "skippedLineItemIds": t.array(t.string()).optional(),
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "updatedLineItemIds": t.array(t.string()).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
        }
    ).named(renames["BulkUpdateLineItemsResponseIn"])
    types["BulkUpdateLineItemsResponseOut"] = t.struct(
        {
            "skippedLineItemIds": t.array(t.string()).optional(),
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "updatedLineItemIds": t.array(t.string()).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkUpdateLineItemsResponseOut"])
    types["AppCategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppCategoryTargetingOptionDetailsIn"])
    types["AppCategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppCategoryTargetingOptionDetailsOut"])
    types["DateRangeIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
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
    types["InvoiceIn"] = t.struct(
        {
            "totalTaxAmountMicros": t.string().optional(),
            "budgetInvoiceGroupingId": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "nonBudgetMicros": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "subtotalAmountMicros": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "serviceDateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "paymentsAccountId": t.string().optional(),
            "budgetSummaries": t.array(t.proxy(renames["BudgetSummaryIn"])).optional(),
            "purchaseOrderNumber": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "correctedInvoiceId": t.string().optional(),
            "dueDate": t.proxy(renames["DateIn"]).optional(),
            "invoiceType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "issueDate": t.proxy(renames["DateIn"]).optional(),
            "invoiceId": t.string().optional(),
        }
    ).named(renames["InvoiceIn"])
    types["InvoiceOut"] = t.struct(
        {
            "totalTaxAmountMicros": t.string().optional(),
            "budgetInvoiceGroupingId": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "nonBudgetMicros": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "subtotalAmountMicros": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "serviceDateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "paymentsAccountId": t.string().optional(),
            "budgetSummaries": t.array(t.proxy(renames["BudgetSummaryOut"])).optional(),
            "purchaseOrderNumber": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "correctedInvoiceId": t.string().optional(),
            "dueDate": t.proxy(renames["DateOut"]).optional(),
            "invoiceType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "issueDate": t.proxy(renames["DateOut"]).optional(),
            "invoiceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceOut"])
    types["PartnerAdServerConfigIn"] = t.struct(
        {"measurementConfig": t.proxy(renames["MeasurementConfigIn"]).optional()}
    ).named(renames["PartnerAdServerConfigIn"])
    types["PartnerAdServerConfigOut"] = t.struct(
        {
            "measurementConfig": t.proxy(renames["MeasurementConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerAdServerConfigOut"])
    types["PartnerCostIn"] = t.struct(
        {
            "costType": t.string(),
            "feeType": t.string(),
            "invoiceType": t.string().optional(),
            "feeAmount": t.string().optional(),
            "feePercentageMillis": t.string().optional(),
        }
    ).named(renames["PartnerCostIn"])
    types["PartnerCostOut"] = t.struct(
        {
            "costType": t.string(),
            "feeType": t.string(),
            "invoiceType": t.string().optional(),
            "feeAmount": t.string().optional(),
            "feePercentageMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerCostOut"])
    types["CounterEventIn"] = t.struct(
        {"reportingName": t.string(), "name": t.string()}
    ).named(renames["CounterEventIn"])
    types["CounterEventOut"] = t.struct(
        {
            "reportingName": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterEventOut"])
    types["InventorySourceFilterIn"] = t.struct(
        {"inventorySourceIds": t.array(t.string()).optional()}
    ).named(renames["InventorySourceFilterIn"])
    types["InventorySourceFilterOut"] = t.struct(
        {
            "inventorySourceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceFilterOut"])
    types["YoutubeVideoAssignedTargetingOptionDetailsIn"] = t.struct(
        {"videoId": t.string().optional(), "negative": t.boolean().optional()}
    ).named(renames["YoutubeVideoAssignedTargetingOptionDetailsIn"])
    types["YoutubeVideoAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "videoId": t.string().optional(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeVideoAssignedTargetingOptionDetailsOut"])
    types["CampaignIn"] = t.struct(
        {
            "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
            "displayName": t.string(),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "campaignBudgets": t.array(t.proxy(renames["CampaignBudgetIn"])).optional(),
            "entityStatus": t.string(),
            "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
        }
    ).named(renames["CampaignIn"])
    types["CampaignOut"] = t.struct(
        {
            "name": t.string().optional(),
            "campaignId": t.string().optional(),
            "campaignGoal": t.proxy(renames["CampaignGoalOut"]),
            "displayName": t.string(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "campaignBudgets": t.array(
                t.proxy(renames["CampaignBudgetOut"])
            ).optional(),
            "entityStatus": t.string(),
            "advertiserId": t.string().optional(),
            "updateTime": t.string().optional(),
            "campaignFlight": t.proxy(renames["CampaignFlightOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignOut"])
    types["PartnerRevenueModelIn"] = t.struct(
        {"markupAmount": t.string(), "markupType": t.string()}
    ).named(renames["PartnerRevenueModelIn"])
    types["PartnerRevenueModelOut"] = t.struct(
        {
            "markupAmount": t.string(),
            "markupType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerRevenueModelOut"])
    types["AudienceGroupAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "includedCombinedAudienceGroup": t.proxy(
                renames["CombinedAudienceGroupIn"]
            ).optional(),
            "includedCustomListGroup": t.proxy(renames["CustomListGroupIn"]).optional(),
            "excludedFirstAndThirdPartyAudienceGroup": t.proxy(
                renames["FirstAndThirdPartyAudienceGroupIn"]
            ).optional(),
            "includedFirstAndThirdPartyAudienceGroups": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceGroupIn"])
            ).optional(),
            "excludedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupIn"]
            ).optional(),
            "includedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupIn"]
            ).optional(),
        }
    ).named(renames["AudienceGroupAssignedTargetingOptionDetailsIn"])
    types["AudienceGroupAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "includedCombinedAudienceGroup": t.proxy(
                renames["CombinedAudienceGroupOut"]
            ).optional(),
            "includedCustomListGroup": t.proxy(
                renames["CustomListGroupOut"]
            ).optional(),
            "excludedFirstAndThirdPartyAudienceGroup": t.proxy(
                renames["FirstAndThirdPartyAudienceGroupOut"]
            ).optional(),
            "includedFirstAndThirdPartyAudienceGroups": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceGroupOut"])
            ).optional(),
            "excludedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupOut"]
            ).optional(),
            "includedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudienceGroupAssignedTargetingOptionDetailsOut"])
    types["CustomListTargetingSettingIn"] = t.struct(
        {"customListId": t.string()}
    ).named(renames["CustomListTargetingSettingIn"])
    types["CustomListTargetingSettingOut"] = t.struct(
        {
            "customListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListTargetingSettingOut"])
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
    types["RateDetailsIn"] = t.struct(
        {
            "unitsPurchased": t.string(),
            "inventorySourceRateType": t.string().optional(),
            "rate": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["RateDetailsIn"])
    types["RateDetailsOut"] = t.struct(
        {
            "minimumSpend": t.proxy(renames["MoneyOut"]).optional(),
            "unitsPurchased": t.string(),
            "inventorySourceRateType": t.string().optional(),
            "rate": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateDetailsOut"])
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
    types["InventorySourceGroupAssignedTargetingOptionDetailsIn"] = t.struct(
        {"inventorySourceGroupId": t.string()}
    ).named(renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"])
    types["InventorySourceGroupAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "inventorySourceGroupId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceGroupAssignedTargetingOptionDetailsOut"])
    types["OperatingSystemTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OperatingSystemTargetingOptionDetailsIn"])
    types["OperatingSystemTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemTargetingOptionDetailsOut"])
    types["ReplaceSitesRequestIn"] = t.struct(
        {
            "newSites": t.array(t.proxy(renames["SiteIn"])).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["ReplaceSitesRequestIn"])
    types["ReplaceSitesRequestOut"] = t.struct(
        {
            "newSites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceSitesRequestOut"])
    types["CreateAssetResponseIn"] = t.struct(
        {"asset": t.proxy(renames["AssetIn"]).optional()}
    ).named(renames["CreateAssetResponseIn"])
    types["CreateAssetResponseOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAssetResponseOut"])
    types["DigitalContentLabelTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DigitalContentLabelTargetingOptionDetailsIn"])
    types["DigitalContentLabelTargetingOptionDetailsOut"] = t.struct(
        {
            "contentRatingTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigitalContentLabelTargetingOptionDetailsOut"])
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
    types["ProximityLocationListAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "proximityRadius": t.number(),
            "proximityLocationListId": t.string(),
            "proximityRadiusUnit": t.string(),
        }
    ).named(renames["ProximityLocationListAssignedTargetingOptionDetailsIn"])
    types["ProximityLocationListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "proximityRadius": t.number(),
            "proximityLocationListId": t.string(),
            "proximityRadiusUnit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProximityLocationListAssignedTargetingOptionDetailsOut"])
    types["ListUsersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "users": t.array(t.proxy(renames["UserIn"])).optional(),
        }
    ).named(renames["ListUsersResponseIn"])
    types["ListUsersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "users": t.array(t.proxy(renames["UserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsersResponseOut"])
    types["SubExchangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SubExchangeTargetingOptionDetailsIn"])
    types["SubExchangeTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubExchangeTargetingOptionDetailsOut"])
    types["InventorySourceAccessorsAdvertiserAccessorsIn"] = t.struct(
        {"advertiserIds": t.array(t.string()).optional()}
    ).named(renames["InventorySourceAccessorsAdvertiserAccessorsIn"])
    types["InventorySourceAccessorsAdvertiserAccessorsOut"] = t.struct(
        {
            "advertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsAdvertiserAccessorsOut"])
    types["ListLocationListsResponseIn"] = t.struct(
        {
            "locationLists": t.array(t.proxy(renames["LocationListIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationListsResponseIn"])
    types["ListLocationListsResponseOut"] = t.struct(
        {
            "locationLists": t.array(t.proxy(renames["LocationListOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationListsResponseOut"])
    types["TargetFrequencyIn"] = t.struct(
        {
            "timeUnitCount": t.integer().optional(),
            "targetCount": t.string().optional(),
            "timeUnit": t.string().optional(),
        }
    ).named(renames["TargetFrequencyIn"])
    types["TargetFrequencyOut"] = t.struct(
        {
            "timeUnitCount": t.integer().optional(),
            "targetCount": t.string().optional(),
            "timeUnit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetFrequencyOut"])
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
    types["FixedBidStrategyIn"] = t.struct(
        {"bidAmountMicros": t.string().optional()}
    ).named(renames["FixedBidStrategyIn"])
    types["FixedBidStrategyOut"] = t.struct(
        {
            "bidAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixedBidStrategyOut"])
    types["InventorySourceGroupIn"] = t.struct({"displayName": t.string()}).named(
        renames["InventorySourceGroupIn"]
    )
    types["InventorySourceGroupOut"] = t.struct(
        {
            "displayName": t.string(),
            "inventorySourceGroupId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceGroupOut"])
    types["CustomListGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["CustomListTargetingSettingIn"]))}
    ).named(renames["CustomListGroupIn"])
    types["CustomListGroupOut"] = t.struct(
        {
            "settings": t.array(t.proxy(renames["CustomListTargetingSettingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListGroupOut"])
    types["AudioAdIn"] = t.struct(
        {
            "finalUrl": t.string().optional(),
            "displayUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "trackingUrl": t.string().optional(),
        }
    ).named(renames["AudioAdIn"])
    types["AudioAdOut"] = t.struct(
        {
            "finalUrl": t.string().optional(),
            "displayUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "trackingUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioAdOut"])
    types["ThirdPartyUrlIn"] = t.struct(
        {"type": t.string().optional(), "url": t.string().optional()}
    ).named(renames["ThirdPartyUrlIn"])
    types["ThirdPartyUrlOut"] = t.struct(
        {
            "type": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyUrlOut"])
    types["InventorySourceAccessorsIn"] = t.struct(
        {
            "partner": t.proxy(
                renames["InventorySourceAccessorsPartnerAccessorIn"]
            ).optional(),
            "advertisers": t.proxy(
                renames["InventorySourceAccessorsAdvertiserAccessorsIn"]
            ).optional(),
        }
    ).named(renames["InventorySourceAccessorsIn"])
    types["InventorySourceAccessorsOut"] = t.struct(
        {
            "partner": t.proxy(
                renames["InventorySourceAccessorsPartnerAccessorOut"]
            ).optional(),
            "advertisers": t.proxy(
                renames["InventorySourceAccessorsAdvertiserAccessorsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsOut"])
    types["DuplicateLineItemResponseIn"] = t.struct(
        {"duplicateLineItemId": t.string().optional()}
    ).named(renames["DuplicateLineItemResponseIn"])
    types["DuplicateLineItemResponseOut"] = t.struct(
        {
            "duplicateLineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateLineItemResponseOut"])
    types["ListFirstAndThirdPartyAudiencesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "firstAndThirdPartyAudiences": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceIn"])
            ).optional(),
        }
    ).named(renames["ListFirstAndThirdPartyAudiencesResponseIn"])
    types["ListFirstAndThirdPartyAudiencesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "firstAndThirdPartyAudiences": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFirstAndThirdPartyAudiencesResponseOut"])
    types["ContactInfoListIn"] = t.struct(
        {"contactInfos": t.array(t.proxy(renames["ContactInfoIn"])).optional()}
    ).named(renames["ContactInfoListIn"])
    types["ContactInfoListOut"] = t.struct(
        {
            "contactInfos": t.array(t.proxy(renames["ContactInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoListOut"])
    types["GoogleAudienceTargetingSettingIn"] = t.struct(
        {"googleAudienceId": t.string()}
    ).named(renames["GoogleAudienceTargetingSettingIn"])
    types["GoogleAudienceTargetingSettingOut"] = t.struct(
        {
            "googleAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceTargetingSettingOut"])
    types["AdvertiserIn"] = t.struct(
        {
            "servingConfig": t.proxy(renames["AdvertiserTargetingConfigIn"]).optional(),
            "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
            "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
            "entityStatus": t.string(),
            "displayName": t.string(),
            "billingConfig": t.proxy(renames["AdvertiserBillingConfigIn"]).optional(),
            "dataAccessConfig": t.proxy(
                renames["AdvertiserDataAccessConfigIn"]
            ).optional(),
            "partnerId": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
            "prismaEnabled": t.boolean().optional(),
        }
    ).named(renames["AdvertiserIn"])
    types["AdvertiserOut"] = t.struct(
        {
            "name": t.string().optional(),
            "servingConfig": t.proxy(
                renames["AdvertiserTargetingConfigOut"]
            ).optional(),
            "generalConfig": t.proxy(renames["AdvertiserGeneralConfigOut"]),
            "advertiserId": t.string().optional(),
            "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigOut"]),
            "entityStatus": t.string(),
            "displayName": t.string(),
            "billingConfig": t.proxy(renames["AdvertiserBillingConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "dataAccessConfig": t.proxy(
                renames["AdvertiserDataAccessConfigOut"]
            ).optional(),
            "partnerId": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigOut"]),
            "prismaEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserOut"])

    functions = {}
    functions["targetingTypesTargetingOptionsList"] = displayvideo.post(
        "v2/targetingTypes/{targetingType}/targetingOptions:search",
        t.struct(
            {
                "targetingType": t.string(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "advertiserId": t.string(),
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTypesTargetingOptionsGet"] = displayvideo.post(
        "v2/targetingTypes/{targetingType}/targetingOptions:search",
        t.struct(
            {
                "targetingType": t.string(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "advertiserId": t.string(),
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTypesTargetingOptionsSearch"] = displayvideo.post(
        "v2/targetingTypes/{targetingType}/targetingOptions:search",
        t.struct(
            {
                "targetingType": t.string(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "advertiserId": t.string(),
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightGroupsGet"] = displayvideo.patch(
        "v2/floodlightGroups/{floodlightGroupId}",
        t.struct(
            {
                "partnerId": t.string(),
                "updateMask": t.string(),
                "floodlightGroupId": t.string().optional(),
                "lookbackWindow": t.proxy(renames["LookbackWindowIn"]),
                "customVariables": t.struct({"_": t.string().optional()}).optional(),
                "activeViewConfig": t.proxy(
                    renames["ActiveViewVideoViewabilityMetricConfigIn"]
                ).optional(),
                "displayName": t.string(),
                "webTagType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["floodlightGroupsPatch"] = displayvideo.patch(
        "v2/floodlightGroups/{floodlightGroupId}",
        t.struct(
            {
                "partnerId": t.string(),
                "updateMask": t.string(),
                "floodlightGroupId": t.string().optional(),
                "lookbackWindow": t.proxy(renames["LookbackWindowIn"]),
                "customVariables": t.struct({"_": t.string().optional()}).optional(),
                "activeViewConfig": t.proxy(
                    renames["ActiveViewVideoViewabilityMetricConfigIn"]
                ).optional(),
                "displayName": t.string(),
                "webTagType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightGroupOut"]),
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
    functions["partnersTargetingTypesAssignedTargetingOptionsGet"] = displayvideo.get(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "partnerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartnerAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "partnersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.get(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "partnerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartnerAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "partnersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.get(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "partnerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartnerAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersTargetingTypesAssignedTargetingOptionsList"] = displayvideo.get(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "partnerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartnerAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsCreate"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsList"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsPatch"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsGet"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesBulkEdit"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites:replace",
        t.struct(
            {
                "channelId": t.string(),
                "partnerId": t.string().optional(),
                "newSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplaceSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesList"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites:replace",
        t.struct(
            {
                "channelId": t.string(),
                "partnerId": t.string().optional(),
                "newSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplaceSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesCreate"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites:replace",
        t.struct(
            {
                "channelId": t.string(),
                "partnerId": t.string().optional(),
                "newSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplaceSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesDelete"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites:replace",
        t.struct(
            {
                "channelId": t.string(),
                "partnerId": t.string().optional(),
                "newSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplaceSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesReplace"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites:replace",
        t.struct(
            {
                "channelId": t.string(),
                "partnerId": t.string().optional(),
                "newSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplaceSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesList"] = displayvideo.get(
        "v2/inventorySources/{inventorySourceId}",
        t.struct(
            {
                "partnerId": t.string(),
                "inventorySourceId": t.string(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesCreate"] = displayvideo.get(
        "v2/inventorySources/{inventorySourceId}",
        t.struct(
            {
                "partnerId": t.string(),
                "inventorySourceId": t.string(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesPatch"] = displayvideo.get(
        "v2/inventorySources/{inventorySourceId}",
        t.struct(
            {
                "partnerId": t.string(),
                "inventorySourceId": t.string(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourcesEditInventorySourceReadWriteAccessors"
    ] = displayvideo.get(
        "v2/inventorySources/{inventorySourceId}",
        t.struct(
            {
                "partnerId": t.string(),
                "inventorySourceId": t.string(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesGet"] = displayvideo.get(
        "v2/inventorySources/{inventorySourceId}",
        t.struct(
            {
                "partnerId": t.string(),
                "inventorySourceId": t.string(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsUploadScript"] = displayvideo.post(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "customBiddingAlgorithmType": t.string(),
                "advertiserId": t.string().optional(),
                "entityStatus": t.string().optional(),
                "partnerId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
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
                "entityStatus": t.string().optional(),
                "partnerId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingAlgorithmOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsPatch"] = displayvideo.post(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "customBiddingAlgorithmType": t.string(),
                "advertiserId": t.string().optional(),
                "entityStatus": t.string().optional(),
                "partnerId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
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
                "entityStatus": t.string().optional(),
                "partnerId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
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
                "entityStatus": t.string().optional(),
                "partnerId": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingAlgorithmOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsCreate"] = displayvideo.get(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingScriptsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsGet"] = displayvideo.get(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingScriptsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsList"] = displayvideo.get(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingScriptsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersBulkEditAssignedUserRoles"] = displayvideo.get(
        "v2/users/{userId}",
        t.struct({"userId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersCreate"] = displayvideo.get(
        "v2/users/{userId}",
        t.struct({"userId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersPatch"] = displayvideo.get(
        "v2/users/{userId}",
        t.struct({"userId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = displayvideo.get(
        "v2/users/{userId}",
        t.struct({"userId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = displayvideo.get(
        "v2/users/{userId}",
        t.struct({"userId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGet"] = displayvideo.get(
        "v2/users/{userId}",
        t.struct({"userId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsPatch"] = displayvideo.get(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourceGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsGet"] = displayvideo.get(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourceGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsCreate"] = displayvideo.get(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourceGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsDelete"] = displayvideo.get(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourceGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsList"] = displayvideo.get(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourceGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesCreate"
    ] = displayvideo.post(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources:bulkEdit",
        t.struct(
            {
                "inventorySourceGroupId": t.string(),
                "deletedAssignedInventorySources": t.array(t.string()).optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "createdAssignedInventorySources": t.array(
                    t.proxy(renames["AssignedInventorySourceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesDelete"
    ] = displayvideo.post(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources:bulkEdit",
        t.struct(
            {
                "inventorySourceGroupId": t.string(),
                "deletedAssignedInventorySources": t.array(t.string()).optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "createdAssignedInventorySources": t.array(
                    t.proxy(renames["AssignedInventorySourceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsAssignedInventorySourcesList"] = displayvideo.post(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources:bulkEdit",
        t.struct(
            {
                "inventorySourceGroupId": t.string(),
                "deletedAssignedInventorySources": t.array(t.string()).optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "createdAssignedInventorySources": t.array(
                    t.proxy(renames["AssignedInventorySourceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesBulkEdit"
    ] = displayvideo.post(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources:bulkEdit",
        t.struct(
            {
                "inventorySourceGroupId": t.string(),
                "deletedAssignedInventorySources": t.array(t.string()).optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "createdAssignedInventorySources": t.array(
                    t.proxy(renames["AssignedInventorySourceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditAssignedInventorySourcesResponseOut"]),
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
    functions["firstAndThirdPartyAudiencesGet"] = displayvideo.get(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFirstAndThirdPartyAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesCreate"] = displayvideo.get(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFirstAndThirdPartyAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesEditCustomerMatchMembers"] = displayvideo.get(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFirstAndThirdPartyAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesPatch"] = displayvideo.get(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFirstAndThirdPartyAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesList"] = displayvideo.get(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFirstAndThirdPartyAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleAudiencesGet"] = displayvideo.get(
        "v2/googleAudiences",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGoogleAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sdfdownloadtasksCreate"] = displayvideo.post(
        "v2/sdfdownloadtasks",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "inventorySourceFilter": t.proxy(
                    renames["InventorySourceFilterIn"]
                ).optional(),
                "idFilter": t.proxy(renames["IdFilterIn"]).optional(),
                "version": t.string(),
                "parentEntityFilter": t.proxy(
                    renames["ParentEntityFilterIn"]
                ).optional(),
                "advertiserId": t.string().optional(),
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
    functions["advertisersAudit"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "partnerId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "partnerId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "partnerId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersListAssignedTargetingOptions"] = displayvideo.get(
        "v2/advertisers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "partnerId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "partnerId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "partnerId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "partnerId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "partnerId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdvertisersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsBulkUpdate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsGet"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsBulkListAssignedTargetingOptions"
    ] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsBulkEditAssignedTargetingOptions"
    ] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsGenerateDefault"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsDelete"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsCreate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsDuplicate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsList"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsPatch"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}",
        t.struct(
            {
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "lineItemId": t.string().optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "creativeIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "lineItemId": t.string(),
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
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
                "lineItemId": t.string(),
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
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
                "lineItemId": t.string(),
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
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
                "lineItemId": t.string(),
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInvoicesLookupInvoiceCurrency"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/invoices",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "loiSapinInvoiceType": t.string().optional(),
                "issueMonth": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvoicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInvoicesList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/invoices",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "loiSapinInvoiceType": t.string().optional(),
                "issueMonth": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvoicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "deletedSites": t.array(t.string()).optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "deletedSites": t.array(t.string()).optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "deletedSites": t.array(t.string()).optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesReplace"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "deletedSites": t.array(t.string()).optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesBulkEdit"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "deletedSites": t.array(t.string()).optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}:listAssignedTargetingOptions",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}:listAssignedTargetingOptions",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}:listAssignedTargetingOptions",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}:listAssignedTargetingOptions",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersDelete"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}:listAssignedTargetingOptions",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersListAssignedTargetingOptions"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}:listAssignedTargetingOptions",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "insertionOrderId": t.string(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "insertionOrderId": t.string(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "insertionOrderId": t.string(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "insertionOrderId": t.string(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsListAssignedTargetingOptions"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsList"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsCreate"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsGet"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsPatch"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsDelete"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "campaignId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersCampaignsTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "targetingType": t.string(),
                "assignedTargetingOptionId": t.string(),
                "campaignId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersCampaignsTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "targetingType": t.string(),
                "assignedTargetingOptionId": t.string(),
                "campaignId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}",
        t.struct(
            {
                "locationListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}",
        t.struct(
            {
                "locationListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}",
        t.struct(
            {
                "locationListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}",
        t.struct(
            {
                "locationListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
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
    functions["advertisersManualTriggersGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:activate",
        t.struct(
            {
                "triggerId": t.string(),
                "advertiserId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:activate",
        t.struct(
            {
                "triggerId": t.string(),
                "advertiserId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:activate",
        t.struct(
            {
                "triggerId": t.string(),
                "advertiserId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:activate",
        t.struct(
            {
                "triggerId": t.string(),
                "advertiserId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersDeactivate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:activate",
        t.struct(
            {
                "triggerId": t.string(),
                "advertiserId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersActivate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:activate",
        t.struct(
            {
                "triggerId": t.string(),
                "advertiserId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
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
    functions["advertisersYoutubeAdGroupAdsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroupAds",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupAdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupAdsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroupAds",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupAdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersYoutubeAdGroupsBulkListAdGroupAssignedTargetingOptions"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersYoutubeAdGroupsTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups/{youtubeAdGroupId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "youtubeAdGroupId": t.string(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersYoutubeAdGroupsTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups/{youtubeAdGroupId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "youtubeAdGroupId": t.string(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "vastTagUrl": t.string().optional(),
                "requireHtml5": t.boolean().optional(),
                "thirdPartyTag": t.string().optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandOnHover": t.boolean().optional(),
                "jsTrackerUrl": t.string().optional(),
                "appendedTag": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "hostingSource": t.string(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "requireMraid": t.boolean().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "expandingDirection": t.string().optional(),
                "entityStatus": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "displayName": t.string(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "skippable": t.boolean().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "integrationCode": t.string().optional(),
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
                "vastTagUrl": t.string().optional(),
                "requireHtml5": t.boolean().optional(),
                "thirdPartyTag": t.string().optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandOnHover": t.boolean().optional(),
                "jsTrackerUrl": t.string().optional(),
                "appendedTag": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "hostingSource": t.string(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "requireMraid": t.boolean().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "expandingDirection": t.string().optional(),
                "entityStatus": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "displayName": t.string(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "skippable": t.boolean().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "integrationCode": t.string().optional(),
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
                "vastTagUrl": t.string().optional(),
                "requireHtml5": t.boolean().optional(),
                "thirdPartyTag": t.string().optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandOnHover": t.boolean().optional(),
                "jsTrackerUrl": t.string().optional(),
                "appendedTag": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "hostingSource": t.string(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "requireMraid": t.boolean().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "expandingDirection": t.string().optional(),
                "entityStatus": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "displayName": t.string(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "skippable": t.boolean().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "integrationCode": t.string().optional(),
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
                "vastTagUrl": t.string().optional(),
                "requireHtml5": t.boolean().optional(),
                "thirdPartyTag": t.string().optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandOnHover": t.boolean().optional(),
                "jsTrackerUrl": t.string().optional(),
                "appendedTag": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "hostingSource": t.string(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "requireMraid": t.boolean().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "expandingDirection": t.string().optional(),
                "entityStatus": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "displayName": t.string(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "skippable": t.boolean().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "integrationCode": t.string().optional(),
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
                "vastTagUrl": t.string().optional(),
                "requireHtml5": t.boolean().optional(),
                "thirdPartyTag": t.string().optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "creativeType": t.string(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandOnHover": t.boolean().optional(),
                "jsTrackerUrl": t.string().optional(),
                "appendedTag": t.string().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "hostingSource": t.string(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "requireMraid": t.boolean().optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "iasCampaignMonitoring": t.boolean().optional(),
                "expandingDirection": t.string().optional(),
                "entityStatus": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "displayName": t.string(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "skippable": t.boolean().optional(),
                "companionCreativeIds": t.array(t.string()).optional(),
                "integrationCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsCreate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsDelete"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsGet"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsList"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsPatch"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string().optional(),
                "updateMask": t.string(),
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
        "advertisersNegativeKeywordListsNegativeKeywordsBulkEdit"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords/{keywordValue}",
        t.struct(
            {
                "advertiserId": t.string(),
                "keywordValue": t.string(),
                "negativeKeywordListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsList"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords/{keywordValue}",
        t.struct(
            {
                "advertiserId": t.string(),
                "keywordValue": t.string(),
                "negativeKeywordListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsReplace"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords/{keywordValue}",
        t.struct(
            {
                "advertiserId": t.string(),
                "keywordValue": t.string(),
                "negativeKeywordListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsCreate"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords/{keywordValue}",
        t.struct(
            {
                "advertiserId": t.string(),
                "keywordValue": t.string(),
                "negativeKeywordListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsDelete"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords/{keywordValue}",
        t.struct(
            {
                "advertiserId": t.string(),
                "keywordValue": t.string(),
                "negativeKeywordListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customListsList"] = displayvideo.get(
        "v2/customLists/{customListId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "customListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customListsGet"] = displayvideo.get(
        "v2/customLists/{customListId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "customListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersCreate"] = displayvideo.get(
        "v2/guaranteedOrders",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuaranteedOrdersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersGet"] = displayvideo.get(
        "v2/guaranteedOrders",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuaranteedOrdersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["combinedAudiencesList"] = displayvideo.get(
        "v2/combinedAudiences/{combinedAudienceId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "combinedAudienceId": t.string(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CombinedAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["combinedAudiencesGet"] = displayvideo.get(
        "v2/combinedAudiences/{combinedAudienceId}",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "combinedAudienceId": t.string(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CombinedAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="displayvideo",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
