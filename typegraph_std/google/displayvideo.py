from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_displayvideo() -> Import:
    displayvideo = HTTPRuntime("https://displayvideo.googleapis.com/")

    renames = {
        "ErrorResponse": "_displayvideo_1_ErrorResponse",
        "GeoRegionAssignedTargetingOptionDetailsIn": "_displayvideo_2_GeoRegionAssignedTargetingOptionDetailsIn",
        "GeoRegionAssignedTargetingOptionDetailsOut": "_displayvideo_3_GeoRegionAssignedTargetingOptionDetailsOut",
        "InStreamAdIn": "_displayvideo_4_InStreamAdIn",
        "InStreamAdOut": "_displayvideo_5_InStreamAdOut",
        "DeviceMakeModelAssignedTargetingOptionDetailsIn": "_displayvideo_6_DeviceMakeModelAssignedTargetingOptionDetailsIn",
        "DeviceMakeModelAssignedTargetingOptionDetailsOut": "_displayvideo_7_DeviceMakeModelAssignedTargetingOptionDetailsOut",
        "TrackingFloodlightActivityConfigIn": "_displayvideo_8_TrackingFloodlightActivityConfigIn",
        "TrackingFloodlightActivityConfigOut": "_displayvideo_9_TrackingFloodlightActivityConfigOut",
        "RateDetailsIn": "_displayvideo_10_RateDetailsIn",
        "RateDetailsOut": "_displayvideo_11_RateDetailsOut",
        "EditGuaranteedOrderReadAccessorsResponseIn": "_displayvideo_12_EditGuaranteedOrderReadAccessorsResponseIn",
        "EditGuaranteedOrderReadAccessorsResponseOut": "_displayvideo_13_EditGuaranteedOrderReadAccessorsResponseOut",
        "InsertionOrderBudgetSegmentIn": "_displayvideo_14_InsertionOrderBudgetSegmentIn",
        "InsertionOrderBudgetSegmentOut": "_displayvideo_15_InsertionOrderBudgetSegmentOut",
        "ReviewStatusInfoIn": "_displayvideo_16_ReviewStatusInfoIn",
        "ReviewStatusInfoOut": "_displayvideo_17_ReviewStatusInfoOut",
        "ListYoutubeAdGroupAdsResponseIn": "_displayvideo_18_ListYoutubeAdGroupAdsResponseIn",
        "ListYoutubeAdGroupAdsResponseOut": "_displayvideo_19_ListYoutubeAdGroupAdsResponseOut",
        "DayAndTimeAssignedTargetingOptionDetailsIn": "_displayvideo_20_DayAndTimeAssignedTargetingOptionDetailsIn",
        "DayAndTimeAssignedTargetingOptionDetailsOut": "_displayvideo_21_DayAndTimeAssignedTargetingOptionDetailsOut",
        "TargetFrequencyIn": "_displayvideo_22_TargetFrequencyIn",
        "TargetFrequencyOut": "_displayvideo_23_TargetFrequencyOut",
        "GenderAssignedTargetingOptionDetailsIn": "_displayvideo_24_GenderAssignedTargetingOptionDetailsIn",
        "GenderAssignedTargetingOptionDetailsOut": "_displayvideo_25_GenderAssignedTargetingOptionDetailsOut",
        "ListCustomBiddingScriptsResponseIn": "_displayvideo_26_ListCustomBiddingScriptsResponseIn",
        "ListCustomBiddingScriptsResponseOut": "_displayvideo_27_ListCustomBiddingScriptsResponseOut",
        "ReplaceSitesRequestIn": "_displayvideo_28_ReplaceSitesRequestIn",
        "ReplaceSitesRequestOut": "_displayvideo_29_ReplaceSitesRequestOut",
        "ContentOutstreamPositionAssignedTargetingOptionDetailsIn": "_displayvideo_30_ContentOutstreamPositionAssignedTargetingOptionDetailsIn",
        "ContentOutstreamPositionAssignedTargetingOptionDetailsOut": "_displayvideo_31_ContentOutstreamPositionAssignedTargetingOptionDetailsOut",
        "LocationListIn": "_displayvideo_32_LocationListIn",
        "LocationListOut": "_displayvideo_33_LocationListOut",
        "SessionPositionAssignedTargetingOptionDetailsIn": "_displayvideo_34_SessionPositionAssignedTargetingOptionDetailsIn",
        "SessionPositionAssignedTargetingOptionDetailsOut": "_displayvideo_35_SessionPositionAssignedTargetingOptionDetailsOut",
        "NegativeKeywordIn": "_displayvideo_36_NegativeKeywordIn",
        "NegativeKeywordOut": "_displayvideo_37_NegativeKeywordOut",
        "DeviceMakeModelTargetingOptionDetailsIn": "_displayvideo_38_DeviceMakeModelTargetingOptionDetailsIn",
        "DeviceMakeModelTargetingOptionDetailsOut": "_displayvideo_39_DeviceMakeModelTargetingOptionDetailsOut",
        "ProductMatchDimensionIn": "_displayvideo_40_ProductMatchDimensionIn",
        "ProductMatchDimensionOut": "_displayvideo_41_ProductMatchDimensionOut",
        "ProductFeedDataIn": "_displayvideo_42_ProductFeedDataIn",
        "ProductFeedDataOut": "_displayvideo_43_ProductFeedDataOut",
        "DoubleVerifyDisplayViewabilityIn": "_displayvideo_44_DoubleVerifyDisplayViewabilityIn",
        "DoubleVerifyDisplayViewabilityOut": "_displayvideo_45_DoubleVerifyDisplayViewabilityOut",
        "CustomListTargetingSettingIn": "_displayvideo_46_CustomListTargetingSettingIn",
        "CustomListTargetingSettingOut": "_displayvideo_47_CustomListTargetingSettingOut",
        "AudienceGroupAssignedTargetingOptionDetailsIn": "_displayvideo_48_AudienceGroupAssignedTargetingOptionDetailsIn",
        "AudienceGroupAssignedTargetingOptionDetailsOut": "_displayvideo_49_AudienceGroupAssignedTargetingOptionDetailsOut",
        "IntegrationDetailsIn": "_displayvideo_50_IntegrationDetailsIn",
        "IntegrationDetailsOut": "_displayvideo_51_IntegrationDetailsOut",
        "ExchangeTargetingOptionDetailsIn": "_displayvideo_52_ExchangeTargetingOptionDetailsIn",
        "ExchangeTargetingOptionDetailsOut": "_displayvideo_53_ExchangeTargetingOptionDetailsOut",
        "AppCategoryTargetingOptionDetailsIn": "_displayvideo_54_AppCategoryTargetingOptionDetailsIn",
        "AppCategoryTargetingOptionDetailsOut": "_displayvideo_55_AppCategoryTargetingOptionDetailsOut",
        "OperatingSystemTargetingOptionDetailsIn": "_displayvideo_56_OperatingSystemTargetingOptionDetailsIn",
        "OperatingSystemTargetingOptionDetailsOut": "_displayvideo_57_OperatingSystemTargetingOptionDetailsOut",
        "InventorySourceDisplayCreativeConfigIn": "_displayvideo_58_InventorySourceDisplayCreativeConfigIn",
        "InventorySourceDisplayCreativeConfigOut": "_displayvideo_59_InventorySourceDisplayCreativeConfigOut",
        "ThirdPartyUrlIn": "_displayvideo_60_ThirdPartyUrlIn",
        "ThirdPartyUrlOut": "_displayvideo_61_ThirdPartyUrlOut",
        "ContactInfoIn": "_displayvideo_62_ContactInfoIn",
        "ContactInfoOut": "_displayvideo_63_ContactInfoOut",
        "ThirdPartyVerifierAssignedTargetingOptionDetailsIn": "_displayvideo_64_ThirdPartyVerifierAssignedTargetingOptionDetailsIn",
        "ThirdPartyVerifierAssignedTargetingOptionDetailsOut": "_displayvideo_65_ThirdPartyVerifierAssignedTargetingOptionDetailsOut",
        "ContentStreamTypeAssignedTargetingOptionDetailsIn": "_displayvideo_66_ContentStreamTypeAssignedTargetingOptionDetailsIn",
        "ContentStreamTypeAssignedTargetingOptionDetailsOut": "_displayvideo_67_ContentStreamTypeAssignedTargetingOptionDetailsOut",
        "GuaranteedOrderStatusIn": "_displayvideo_68_GuaranteedOrderStatusIn",
        "GuaranteedOrderStatusOut": "_displayvideo_69_GuaranteedOrderStatusOut",
        "InventorySourceStatusIn": "_displayvideo_70_InventorySourceStatusIn",
        "InventorySourceStatusOut": "_displayvideo_71_InventorySourceStatusOut",
        "FrequencyCapIn": "_displayvideo_72_FrequencyCapIn",
        "FrequencyCapOut": "_displayvideo_73_FrequencyCapOut",
        "GoogleAudienceIn": "_displayvideo_74_GoogleAudienceIn",
        "GoogleAudienceOut": "_displayvideo_75_GoogleAudienceOut",
        "ViewabilityAssignedTargetingOptionDetailsIn": "_displayvideo_76_ViewabilityAssignedTargetingOptionDetailsIn",
        "ViewabilityAssignedTargetingOptionDetailsOut": "_displayvideo_77_ViewabilityAssignedTargetingOptionDetailsOut",
        "PoiTargetingOptionDetailsIn": "_displayvideo_78_PoiTargetingOptionDetailsIn",
        "PoiTargetingOptionDetailsOut": "_displayvideo_79_PoiTargetingOptionDetailsOut",
        "VideoPlayerSizeAssignedTargetingOptionDetailsIn": "_displayvideo_80_VideoPlayerSizeAssignedTargetingOptionDetailsIn",
        "VideoPlayerSizeAssignedTargetingOptionDetailsOut": "_displayvideo_81_VideoPlayerSizeAssignedTargetingOptionDetailsOut",
        "NegativeKeywordListAssignedTargetingOptionDetailsIn": "_displayvideo_82_NegativeKeywordListAssignedTargetingOptionDetailsIn",
        "NegativeKeywordListAssignedTargetingOptionDetailsOut": "_displayvideo_83_NegativeKeywordListAssignedTargetingOptionDetailsOut",
        "InventorySourceAccessorsPartnerAccessorIn": "_displayvideo_84_InventorySourceAccessorsPartnerAccessorIn",
        "InventorySourceAccessorsPartnerAccessorOut": "_displayvideo_85_InventorySourceAccessorsPartnerAccessorOut",
        "CustomListGroupIn": "_displayvideo_86_CustomListGroupIn",
        "CustomListGroupOut": "_displayvideo_87_CustomListGroupOut",
        "DisplayVideoSourceAdIn": "_displayvideo_88_DisplayVideoSourceAdIn",
        "DisplayVideoSourceAdOut": "_displayvideo_89_DisplayVideoSourceAdOut",
        "GoogleAudienceGroupIn": "_displayvideo_90_GoogleAudienceGroupIn",
        "GoogleAudienceGroupOut": "_displayvideo_91_GoogleAudienceGroupOut",
        "ListCombinedAudiencesResponseIn": "_displayvideo_92_ListCombinedAudiencesResponseIn",
        "ListCombinedAudiencesResponseOut": "_displayvideo_93_ListCombinedAudiencesResponseOut",
        "GoogleAudienceTargetingSettingIn": "_displayvideo_94_GoogleAudienceTargetingSettingIn",
        "GoogleAudienceTargetingSettingOut": "_displayvideo_95_GoogleAudienceTargetingSettingOut",
        "HouseholdIncomeAssignedTargetingOptionDetailsIn": "_displayvideo_96_HouseholdIncomeAssignedTargetingOptionDetailsIn",
        "HouseholdIncomeAssignedTargetingOptionDetailsOut": "_displayvideo_97_HouseholdIncomeAssignedTargetingOptionDetailsOut",
        "CustomBiddingAlgorithmIn": "_displayvideo_98_CustomBiddingAlgorithmIn",
        "CustomBiddingAlgorithmOut": "_displayvideo_99_CustomBiddingAlgorithmOut",
        "ListLineItemAssignedTargetingOptionsResponseIn": "_displayvideo_100_ListLineItemAssignedTargetingOptionsResponseIn",
        "ListLineItemAssignedTargetingOptionsResponseOut": "_displayvideo_101_ListLineItemAssignedTargetingOptionsResponseOut",
        "ExitEventIn": "_displayvideo_102_ExitEventIn",
        "ExitEventOut": "_displayvideo_103_ExitEventOut",
        "SensitiveCategoryAssignedTargetingOptionDetailsIn": "_displayvideo_104_SensitiveCategoryAssignedTargetingOptionDetailsIn",
        "SensitiveCategoryAssignedTargetingOptionDetailsOut": "_displayvideo_105_SensitiveCategoryAssignedTargetingOptionDetailsOut",
        "AdlooxIn": "_displayvideo_106_AdlooxIn",
        "AdlooxOut": "_displayvideo_107_AdlooxOut",
        "BrowserTargetingOptionDetailsIn": "_displayvideo_108_BrowserTargetingOptionDetailsIn",
        "BrowserTargetingOptionDetailsOut": "_displayvideo_109_BrowserTargetingOptionDetailsOut",
        "ListGoogleAudiencesResponseIn": "_displayvideo_110_ListGoogleAudiencesResponseIn",
        "ListGoogleAudiencesResponseOut": "_displayvideo_111_ListGoogleAudiencesResponseOut",
        "PartnerIn": "_displayvideo_112_PartnerIn",
        "PartnerOut": "_displayvideo_113_PartnerOut",
        "ListCustomBiddingAlgorithmsResponseIn": "_displayvideo_114_ListCustomBiddingAlgorithmsResponseIn",
        "ListCustomBiddingAlgorithmsResponseOut": "_displayvideo_115_ListCustomBiddingAlgorithmsResponseOut",
        "IdFilterIn": "_displayvideo_116_IdFilterIn",
        "IdFilterOut": "_displayvideo_117_IdFilterOut",
        "TargetingOptionIn": "_displayvideo_118_TargetingOptionIn",
        "TargetingOptionOut": "_displayvideo_119_TargetingOptionOut",
        "ListAssignedInventorySourcesResponseIn": "_displayvideo_120_ListAssignedInventorySourcesResponseIn",
        "ListAssignedInventorySourcesResponseOut": "_displayvideo_121_ListAssignedInventorySourcesResponseOut",
        "DimensionsIn": "_displayvideo_122_DimensionsIn",
        "DimensionsOut": "_displayvideo_123_DimensionsOut",
        "AssignedLocationIn": "_displayvideo_124_AssignedLocationIn",
        "AssignedLocationOut": "_displayvideo_125_AssignedLocationOut",
        "ListCampaignAssignedTargetingOptionsResponseIn": "_displayvideo_126_ListCampaignAssignedTargetingOptionsResponseIn",
        "ListCampaignAssignedTargetingOptionsResponseOut": "_displayvideo_127_ListCampaignAssignedTargetingOptionsResponseOut",
        "EditGuaranteedOrderReadAccessorsRequestIn": "_displayvideo_128_EditGuaranteedOrderReadAccessorsRequestIn",
        "EditGuaranteedOrderReadAccessorsRequestOut": "_displayvideo_129_EditGuaranteedOrderReadAccessorsRequestOut",
        "InvoiceIn": "_displayvideo_130_InvoiceIn",
        "InvoiceOut": "_displayvideo_131_InvoiceOut",
        "ActivateManualTriggerRequestIn": "_displayvideo_132_ActivateManualTriggerRequestIn",
        "ActivateManualTriggerRequestOut": "_displayvideo_133_ActivateManualTriggerRequestOut",
        "HouseholdIncomeTargetingOptionDetailsIn": "_displayvideo_134_HouseholdIncomeTargetingOptionDetailsIn",
        "HouseholdIncomeTargetingOptionDetailsOut": "_displayvideo_135_HouseholdIncomeTargetingOptionDetailsOut",
        "DoubleVerifyBrandSafetyCategoriesIn": "_displayvideo_136_DoubleVerifyBrandSafetyCategoriesIn",
        "DoubleVerifyBrandSafetyCategoriesOut": "_displayvideo_137_DoubleVerifyBrandSafetyCategoriesOut",
        "BiddingStrategyIn": "_displayvideo_138_BiddingStrategyIn",
        "BiddingStrategyOut": "_displayvideo_139_BiddingStrategyOut",
        "AudioContentTypeTargetingOptionDetailsIn": "_displayvideo_140_AudioContentTypeTargetingOptionDetailsIn",
        "AudioContentTypeTargetingOptionDetailsOut": "_displayvideo_141_AudioContentTypeTargetingOptionDetailsOut",
        "MobileDeviceIdListIn": "_displayvideo_142_MobileDeviceIdListIn",
        "MobileDeviceIdListOut": "_displayvideo_143_MobileDeviceIdListOut",
        "CarrierAndIspAssignedTargetingOptionDetailsIn": "_displayvideo_144_CarrierAndIspAssignedTargetingOptionDetailsIn",
        "CarrierAndIspAssignedTargetingOptionDetailsOut": "_displayvideo_145_CarrierAndIspAssignedTargetingOptionDetailsOut",
        "AdvertiserCreativeConfigIn": "_displayvideo_146_AdvertiserCreativeConfigIn",
        "AdvertiserCreativeConfigOut": "_displayvideo_147_AdvertiserCreativeConfigOut",
        "YoutubeVideoDetailsIn": "_displayvideo_148_YoutubeVideoDetailsIn",
        "YoutubeVideoDetailsOut": "_displayvideo_149_YoutubeVideoDetailsOut",
        "AudioVideoOffsetIn": "_displayvideo_150_AudioVideoOffsetIn",
        "AudioVideoOffsetOut": "_displayvideo_151_AudioVideoOffsetOut",
        "ListPartnerAssignedTargetingOptionsResponseIn": "_displayvideo_152_ListPartnerAssignedTargetingOptionsResponseIn",
        "ListPartnerAssignedTargetingOptionsResponseOut": "_displayvideo_153_ListPartnerAssignedTargetingOptionsResponseOut",
        "BulkEditNegativeKeywordsResponseIn": "_displayvideo_154_BulkEditNegativeKeywordsResponseIn",
        "BulkEditNegativeKeywordsResponseOut": "_displayvideo_155_BulkEditNegativeKeywordsResponseOut",
        "FirstAndThirdPartyAudienceTargetingSettingIn": "_displayvideo_156_FirstAndThirdPartyAudienceTargetingSettingIn",
        "FirstAndThirdPartyAudienceTargetingSettingOut": "_displayvideo_157_FirstAndThirdPartyAudienceTargetingSettingOut",
        "ListChannelsResponseIn": "_displayvideo_158_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_displayvideo_159_ListChannelsResponseOut",
        "CreativeIn": "_displayvideo_160_CreativeIn",
        "CreativeOut": "_displayvideo_161_CreativeOut",
        "AuthorizedSellerStatusTargetingOptionDetailsIn": "_displayvideo_162_AuthorizedSellerStatusTargetingOptionDetailsIn",
        "AuthorizedSellerStatusTargetingOptionDetailsOut": "_displayvideo_163_AuthorizedSellerStatusTargetingOptionDetailsOut",
        "UrlAssignedTargetingOptionDetailsIn": "_displayvideo_164_UrlAssignedTargetingOptionDetailsIn",
        "UrlAssignedTargetingOptionDetailsOut": "_displayvideo_165_UrlAssignedTargetingOptionDetailsOut",
        "EnvironmentTargetingOptionDetailsIn": "_displayvideo_166_EnvironmentTargetingOptionDetailsIn",
        "EnvironmentTargetingOptionDetailsOut": "_displayvideo_167_EnvironmentTargetingOptionDetailsOut",
        "ListNegativeKeywordListsResponseIn": "_displayvideo_168_ListNegativeKeywordListsResponseIn",
        "ListNegativeKeywordListsResponseOut": "_displayvideo_169_ListNegativeKeywordListsResponseOut",
        "YoutubeAdGroupIn": "_displayvideo_170_YoutubeAdGroupIn",
        "YoutubeAdGroupOut": "_displayvideo_171_YoutubeAdGroupOut",
        "DeleteAssignedTargetingOptionsRequestIn": "_displayvideo_172_DeleteAssignedTargetingOptionsRequestIn",
        "DeleteAssignedTargetingOptionsRequestOut": "_displayvideo_173_DeleteAssignedTargetingOptionsRequestOut",
        "LanguageTargetingOptionDetailsIn": "_displayvideo_174_LanguageTargetingOptionDetailsIn",
        "LanguageTargetingOptionDetailsOut": "_displayvideo_175_LanguageTargetingOptionDetailsOut",
        "InventorySourceGroupAssignedTargetingOptionDetailsIn": "_displayvideo_176_InventorySourceGroupAssignedTargetingOptionDetailsIn",
        "InventorySourceGroupAssignedTargetingOptionDetailsOut": "_displayvideo_177_InventorySourceGroupAssignedTargetingOptionDetailsOut",
        "BulkEditAssignedLocationsRequestIn": "_displayvideo_178_BulkEditAssignedLocationsRequestIn",
        "BulkEditAssignedLocationsRequestOut": "_displayvideo_179_BulkEditAssignedLocationsRequestOut",
        "AuditAdvertiserResponseIn": "_displayvideo_180_AuditAdvertiserResponseIn",
        "AuditAdvertiserResponseOut": "_displayvideo_181_AuditAdvertiserResponseOut",
        "SiteIn": "_displayvideo_182_SiteIn",
        "SiteOut": "_displayvideo_183_SiteOut",
        "ListInventorySourceGroupsResponseIn": "_displayvideo_184_ListInventorySourceGroupsResponseIn",
        "ListInventorySourceGroupsResponseOut": "_displayvideo_185_ListInventorySourceGroupsResponseOut",
        "AgeRangeAssignedTargetingOptionDetailsIn": "_displayvideo_186_AgeRangeAssignedTargetingOptionDetailsIn",
        "AgeRangeAssignedTargetingOptionDetailsOut": "_displayvideo_187_AgeRangeAssignedTargetingOptionDetailsOut",
        "DoubleVerifyAppStarRatingIn": "_displayvideo_188_DoubleVerifyAppStarRatingIn",
        "DoubleVerifyAppStarRatingOut": "_displayvideo_189_DoubleVerifyAppStarRatingOut",
        "LineItemFlightIn": "_displayvideo_190_LineItemFlightIn",
        "LineItemFlightOut": "_displayvideo_191_LineItemFlightOut",
        "BulkListAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_192_BulkListAdvertiserAssignedTargetingOptionsResponseIn",
        "BulkListAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_193_BulkListAdvertiserAssignedTargetingOptionsResponseOut",
        "BulkEditAssignedTargetingOptionsResponseIn": "_displayvideo_194_BulkEditAssignedTargetingOptionsResponseIn",
        "BulkEditAssignedTargetingOptionsResponseOut": "_displayvideo_195_BulkEditAssignedTargetingOptionsResponseOut",
        "InventorySourceAccessorsIn": "_displayvideo_196_InventorySourceAccessorsIn",
        "InventorySourceAccessorsOut": "_displayvideo_197_InventorySourceAccessorsOut",
        "YoutubeAndPartnersThirdPartyMeasurementSettingsIn": "_displayvideo_198_YoutubeAndPartnersThirdPartyMeasurementSettingsIn",
        "YoutubeAndPartnersThirdPartyMeasurementSettingsOut": "_displayvideo_199_YoutubeAndPartnersThirdPartyMeasurementSettingsOut",
        "ImageAssetIn": "_displayvideo_200_ImageAssetIn",
        "ImageAssetOut": "_displayvideo_201_ImageAssetOut",
        "FirstAndThirdPartyAudienceIn": "_displayvideo_202_FirstAndThirdPartyAudienceIn",
        "FirstAndThirdPartyAudienceOut": "_displayvideo_203_FirstAndThirdPartyAudienceOut",
        "DigitalContentLabelTargetingOptionDetailsIn": "_displayvideo_204_DigitalContentLabelTargetingOptionDetailsIn",
        "DigitalContentLabelTargetingOptionDetailsOut": "_displayvideo_205_DigitalContentLabelTargetingOptionDetailsOut",
        "BumperAdIn": "_displayvideo_206_BumperAdIn",
        "BumperAdOut": "_displayvideo_207_BumperAdOut",
        "AdvertiserDataAccessConfigIn": "_displayvideo_208_AdvertiserDataAccessConfigIn",
        "AdvertiserDataAccessConfigOut": "_displayvideo_209_AdvertiserDataAccessConfigOut",
        "MeasurementConfigIn": "_displayvideo_210_MeasurementConfigIn",
        "MeasurementConfigOut": "_displayvideo_211_MeasurementConfigOut",
        "EnvironmentAssignedTargetingOptionDetailsIn": "_displayvideo_212_EnvironmentAssignedTargetingOptionDetailsIn",
        "EnvironmentAssignedTargetingOptionDetailsOut": "_displayvideo_213_EnvironmentAssignedTargetingOptionDetailsOut",
        "MastheadAdIn": "_displayvideo_214_MastheadAdIn",
        "MastheadAdOut": "_displayvideo_215_MastheadAdOut",
        "DeviceTypeAssignedTargetingOptionDetailsIn": "_displayvideo_216_DeviceTypeAssignedTargetingOptionDetailsIn",
        "DeviceTypeAssignedTargetingOptionDetailsOut": "_displayvideo_217_DeviceTypeAssignedTargetingOptionDetailsOut",
        "ScriptErrorIn": "_displayvideo_218_ScriptErrorIn",
        "ScriptErrorOut": "_displayvideo_219_ScriptErrorOut",
        "ContactInfoListIn": "_displayvideo_220_ContactInfoListIn",
        "ContactInfoListOut": "_displayvideo_221_ContactInfoListOut",
        "ContentGenreTargetingOptionDetailsIn": "_displayvideo_222_ContentGenreTargetingOptionDetailsIn",
        "ContentGenreTargetingOptionDetailsOut": "_displayvideo_223_ContentGenreTargetingOptionDetailsOut",
        "BulkEditAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_224_BulkEditAdvertiserAssignedTargetingOptionsResponseIn",
        "BulkEditAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_225_BulkEditAdvertiserAssignedTargetingOptionsResponseOut",
        "SdfDownloadTaskMetadataIn": "_displayvideo_226_SdfDownloadTaskMetadataIn",
        "SdfDownloadTaskMetadataOut": "_displayvideo_227_SdfDownloadTaskMetadataOut",
        "OperationIn": "_displayvideo_228_OperationIn",
        "OperationOut": "_displayvideo_229_OperationOut",
        "ViewabilityTargetingOptionDetailsIn": "_displayvideo_230_ViewabilityTargetingOptionDetailsIn",
        "ViewabilityTargetingOptionDetailsOut": "_displayvideo_231_ViewabilityTargetingOptionDetailsOut",
        "AppCategoryAssignedTargetingOptionDetailsIn": "_displayvideo_232_AppCategoryAssignedTargetingOptionDetailsIn",
        "AppCategoryAssignedTargetingOptionDetailsOut": "_displayvideo_233_AppCategoryAssignedTargetingOptionDetailsOut",
        "BusinessChainTargetingOptionDetailsIn": "_displayvideo_234_BusinessChainTargetingOptionDetailsIn",
        "BusinessChainTargetingOptionDetailsOut": "_displayvideo_235_BusinessChainTargetingOptionDetailsOut",
        "ListSitesResponseIn": "_displayvideo_236_ListSitesResponseIn",
        "ListSitesResponseOut": "_displayvideo_237_ListSitesResponseOut",
        "ContentDurationAssignedTargetingOptionDetailsIn": "_displayvideo_238_ContentDurationAssignedTargetingOptionDetailsIn",
        "ContentDurationAssignedTargetingOptionDetailsOut": "_displayvideo_239_ContentDurationAssignedTargetingOptionDetailsOut",
        "BulkEditAssignedUserRolesResponseIn": "_displayvideo_240_BulkEditAssignedUserRolesResponseIn",
        "BulkEditAssignedUserRolesResponseOut": "_displayvideo_241_BulkEditAssignedUserRolesResponseOut",
        "LineItemBudgetIn": "_displayvideo_242_LineItemBudgetIn",
        "LineItemBudgetOut": "_displayvideo_243_LineItemBudgetOut",
        "ListYoutubeAdGroupAssignedTargetingOptionsResponseIn": "_displayvideo_244_ListYoutubeAdGroupAssignedTargetingOptionsResponseIn",
        "ListYoutubeAdGroupAssignedTargetingOptionsResponseOut": "_displayvideo_245_ListYoutubeAdGroupAssignedTargetingOptionsResponseOut",
        "YoutubeChannelAssignedTargetingOptionDetailsIn": "_displayvideo_246_YoutubeChannelAssignedTargetingOptionDetailsIn",
        "YoutubeChannelAssignedTargetingOptionDetailsOut": "_displayvideo_247_YoutubeChannelAssignedTargetingOptionDetailsOut",
        "BulkUpdateLineItemsResponseIn": "_displayvideo_248_BulkUpdateLineItemsResponseIn",
        "BulkUpdateLineItemsResponseOut": "_displayvideo_249_BulkUpdateLineItemsResponseOut",
        "BulkEditAssignedLocationsResponseIn": "_displayvideo_250_BulkEditAssignedLocationsResponseIn",
        "BulkEditAssignedLocationsResponseOut": "_displayvideo_251_BulkEditAssignedLocationsResponseOut",
        "SensitiveCategoryTargetingOptionDetailsIn": "_displayvideo_252_SensitiveCategoryTargetingOptionDetailsIn",
        "SensitiveCategoryTargetingOptionDetailsOut": "_displayvideo_253_SensitiveCategoryTargetingOptionDetailsOut",
        "AppAssignedTargetingOptionDetailsIn": "_displayvideo_254_AppAssignedTargetingOptionDetailsIn",
        "AppAssignedTargetingOptionDetailsOut": "_displayvideo_255_AppAssignedTargetingOptionDetailsOut",
        "ListInsertionOrderAssignedTargetingOptionsResponseIn": "_displayvideo_256_ListInsertionOrderAssignedTargetingOptionsResponseIn",
        "ListInsertionOrderAssignedTargetingOptionsResponseOut": "_displayvideo_257_ListInsertionOrderAssignedTargetingOptionsResponseOut",
        "CreateAssetRequestIn": "_displayvideo_258_CreateAssetRequestIn",
        "CreateAssetRequestOut": "_displayvideo_259_CreateAssetRequestOut",
        "DuplicateLineItemResponseIn": "_displayvideo_260_DuplicateLineItemResponseIn",
        "DuplicateLineItemResponseOut": "_displayvideo_261_DuplicateLineItemResponseOut",
        "YoutubeAndPartnersInventorySourceConfigIn": "_displayvideo_262_YoutubeAndPartnersInventorySourceConfigIn",
        "YoutubeAndPartnersInventorySourceConfigOut": "_displayvideo_263_YoutubeAndPartnersInventorySourceConfigOut",
        "InventorySourceGroupIn": "_displayvideo_264_InventorySourceGroupIn",
        "InventorySourceGroupOut": "_displayvideo_265_InventorySourceGroupOut",
        "CmHybridConfigIn": "_displayvideo_266_CmHybridConfigIn",
        "CmHybridConfigOut": "_displayvideo_267_CmHybridConfigOut",
        "DeactivateManualTriggerRequestIn": "_displayvideo_268_DeactivateManualTriggerRequestIn",
        "DeactivateManualTriggerRequestOut": "_displayvideo_269_DeactivateManualTriggerRequestOut",
        "UserRewardedContentAssignedTargetingOptionDetailsIn": "_displayvideo_270_UserRewardedContentAssignedTargetingOptionDetailsIn",
        "UserRewardedContentAssignedTargetingOptionDetailsOut": "_displayvideo_271_UserRewardedContentAssignedTargetingOptionDetailsOut",
        "LanguageAssignedTargetingOptionDetailsIn": "_displayvideo_272_LanguageAssignedTargetingOptionDetailsIn",
        "LanguageAssignedTargetingOptionDetailsOut": "_displayvideo_273_LanguageAssignedTargetingOptionDetailsOut",
        "ListInventorySourcesResponseIn": "_displayvideo_274_ListInventorySourcesResponseIn",
        "ListInventorySourcesResponseOut": "_displayvideo_275_ListInventorySourcesResponseOut",
        "CustomBiddingModelDetailsIn": "_displayvideo_276_CustomBiddingModelDetailsIn",
        "CustomBiddingModelDetailsOut": "_displayvideo_277_CustomBiddingModelDetailsOut",
        "PartnerCostIn": "_displayvideo_278_PartnerCostIn",
        "PartnerCostOut": "_displayvideo_279_PartnerCostOut",
        "PublisherReviewStatusIn": "_displayvideo_280_PublisherReviewStatusIn",
        "PublisherReviewStatusOut": "_displayvideo_281_PublisherReviewStatusOut",
        "ListCustomListsResponseIn": "_displayvideo_282_ListCustomListsResponseIn",
        "ListCustomListsResponseOut": "_displayvideo_283_ListCustomListsResponseOut",
        "AdvertiserAdServerConfigIn": "_displayvideo_284_AdvertiserAdServerConfigIn",
        "AdvertiserAdServerConfigOut": "_displayvideo_285_AdvertiserAdServerConfigOut",
        "BusinessChainSearchTermsIn": "_displayvideo_286_BusinessChainSearchTermsIn",
        "BusinessChainSearchTermsOut": "_displayvideo_287_BusinessChainSearchTermsOut",
        "DateRangeIn": "_displayvideo_288_DateRangeIn",
        "DateRangeOut": "_displayvideo_289_DateRangeOut",
        "ReplaceNegativeKeywordsResponseIn": "_displayvideo_290_ReplaceNegativeKeywordsResponseIn",
        "ReplaceNegativeKeywordsResponseOut": "_displayvideo_291_ReplaceNegativeKeywordsResponseOut",
        "TimeRangeIn": "_displayvideo_292_TimeRangeIn",
        "TimeRangeOut": "_displayvideo_293_TimeRangeOut",
        "EditCustomerMatchMembersRequestIn": "_displayvideo_294_EditCustomerMatchMembersRequestIn",
        "EditCustomerMatchMembersRequestOut": "_displayvideo_295_EditCustomerMatchMembersRequestOut",
        "SdfConfigIn": "_displayvideo_296_SdfConfigIn",
        "SdfConfigOut": "_displayvideo_297_SdfConfigOut",
        "PrismaConfigIn": "_displayvideo_298_PrismaConfigIn",
        "PrismaConfigOut": "_displayvideo_299_PrismaConfigOut",
        "PoiAssignedTargetingOptionDetailsIn": "_displayvideo_300_PoiAssignedTargetingOptionDetailsIn",
        "PoiAssignedTargetingOptionDetailsOut": "_displayvideo_301_PoiAssignedTargetingOptionDetailsOut",
        "CustomBiddingScriptIn": "_displayvideo_302_CustomBiddingScriptIn",
        "CustomBiddingScriptOut": "_displayvideo_303_CustomBiddingScriptOut",
        "ExchangeReviewStatusIn": "_displayvideo_304_ExchangeReviewStatusIn",
        "ExchangeReviewStatusOut": "_displayvideo_305_ExchangeReviewStatusOut",
        "PerformanceGoalIn": "_displayvideo_306_PerformanceGoalIn",
        "PerformanceGoalOut": "_displayvideo_307_PerformanceGoalOut",
        "VideoAdSequenceStepIn": "_displayvideo_308_VideoAdSequenceStepIn",
        "VideoAdSequenceStepOut": "_displayvideo_309_VideoAdSequenceStepOut",
        "AuthorizedSellerStatusAssignedTargetingOptionDetailsIn": "_displayvideo_310_AuthorizedSellerStatusAssignedTargetingOptionDetailsIn",
        "AuthorizedSellerStatusAssignedTargetingOptionDetailsOut": "_displayvideo_311_AuthorizedSellerStatusAssignedTargetingOptionDetailsOut",
        "BulkEditPartnerAssignedTargetingOptionsRequestIn": "_displayvideo_312_BulkEditPartnerAssignedTargetingOptionsRequestIn",
        "BulkEditPartnerAssignedTargetingOptionsRequestOut": "_displayvideo_313_BulkEditPartnerAssignedTargetingOptionsRequestOut",
        "AssetAssociationIn": "_displayvideo_314_AssetAssociationIn",
        "AssetAssociationOut": "_displayvideo_315_AssetAssociationOut",
        "InventorySourceIn": "_displayvideo_316_InventorySourceIn",
        "InventorySourceOut": "_displayvideo_317_InventorySourceOut",
        "AudioContentTypeAssignedTargetingOptionDetailsIn": "_displayvideo_318_AudioContentTypeAssignedTargetingOptionDetailsIn",
        "AudioContentTypeAssignedTargetingOptionDetailsOut": "_displayvideo_319_AudioContentTypeAssignedTargetingOptionDetailsOut",
        "SubExchangeTargetingOptionDetailsIn": "_displayvideo_320_SubExchangeTargetingOptionDetailsIn",
        "SubExchangeTargetingOptionDetailsOut": "_displayvideo_321_SubExchangeTargetingOptionDetailsOut",
        "FloodlightGroupIn": "_displayvideo_322_FloodlightGroupIn",
        "FloodlightGroupOut": "_displayvideo_323_FloodlightGroupOut",
        "AssignedTargetingOptionIn": "_displayvideo_324_AssignedTargetingOptionIn",
        "AssignedTargetingOptionOut": "_displayvideo_325_AssignedTargetingOptionOut",
        "CampaignGoalIn": "_displayvideo_326_CampaignGoalIn",
        "CampaignGoalOut": "_displayvideo_327_CampaignGoalOut",
        "DoubleVerifyVideoViewabilityIn": "_displayvideo_328_DoubleVerifyVideoViewabilityIn",
        "DoubleVerifyVideoViewabilityOut": "_displayvideo_329_DoubleVerifyVideoViewabilityOut",
        "DoubleVerifyIn": "_displayvideo_330_DoubleVerifyIn",
        "DoubleVerifyOut": "_displayvideo_331_DoubleVerifyOut",
        "ListGuaranteedOrdersResponseIn": "_displayvideo_332_ListGuaranteedOrdersResponseIn",
        "ListGuaranteedOrdersResponseOut": "_displayvideo_333_ListGuaranteedOrdersResponseOut",
        "ExchangeAssignedTargetingOptionDetailsIn": "_displayvideo_334_ExchangeAssignedTargetingOptionDetailsIn",
        "ExchangeAssignedTargetingOptionDetailsOut": "_displayvideo_335_ExchangeAssignedTargetingOptionDetailsOut",
        "ListYoutubeAdGroupsResponseIn": "_displayvideo_336_ListYoutubeAdGroupsResponseIn",
        "ListYoutubeAdGroupsResponseOut": "_displayvideo_337_ListYoutubeAdGroupsResponseOut",
        "BulkEditAssignedTargetingOptionsRequestIn": "_displayvideo_338_BulkEditAssignedTargetingOptionsRequestIn",
        "BulkEditAssignedTargetingOptionsRequestOut": "_displayvideo_339_BulkEditAssignedTargetingOptionsRequestOut",
        "SdfDownloadTaskIn": "_displayvideo_340_SdfDownloadTaskIn",
        "SdfDownloadTaskOut": "_displayvideo_341_SdfDownloadTaskOut",
        "LookupInvoiceCurrencyResponseIn": "_displayvideo_342_LookupInvoiceCurrencyResponseIn",
        "LookupInvoiceCurrencyResponseOut": "_displayvideo_343_LookupInvoiceCurrencyResponseOut",
        "YoutubeAdGroupAdIn": "_displayvideo_344_YoutubeAdGroupAdIn",
        "YoutubeAdGroupAdOut": "_displayvideo_345_YoutubeAdGroupAdOut",
        "NativeContentPositionTargetingOptionDetailsIn": "_displayvideo_346_NativeContentPositionTargetingOptionDetailsIn",
        "NativeContentPositionTargetingOptionDetailsOut": "_displayvideo_347_NativeContentPositionTargetingOptionDetailsOut",
        "SearchTargetingOptionsRequestIn": "_displayvideo_348_SearchTargetingOptionsRequestIn",
        "SearchTargetingOptionsRequestOut": "_displayvideo_349_SearchTargetingOptionsRequestOut",
        "AdvertiserBillingConfigIn": "_displayvideo_350_AdvertiserBillingConfigIn",
        "AdvertiserBillingConfigOut": "_displayvideo_351_AdvertiserBillingConfigOut",
        "GoogleBytestreamMediaIn": "_displayvideo_352_GoogleBytestreamMediaIn",
        "GoogleBytestreamMediaOut": "_displayvideo_353_GoogleBytestreamMediaOut",
        "FixedBidStrategyIn": "_displayvideo_354_FixedBidStrategyIn",
        "FixedBidStrategyOut": "_displayvideo_355_FixedBidStrategyOut",
        "BusinessChainAssignedTargetingOptionDetailsIn": "_displayvideo_356_BusinessChainAssignedTargetingOptionDetailsIn",
        "BusinessChainAssignedTargetingOptionDetailsOut": "_displayvideo_357_BusinessChainAssignedTargetingOptionDetailsOut",
        "BulkEditSitesRequestIn": "_displayvideo_358_BulkEditSitesRequestIn",
        "BulkEditSitesRequestOut": "_displayvideo_359_BulkEditSitesRequestOut",
        "ManualTriggerIn": "_displayvideo_360_ManualTriggerIn",
        "ManualTriggerOut": "_displayvideo_361_ManualTriggerOut",
        "BulkEditNegativeKeywordsRequestIn": "_displayvideo_362_BulkEditNegativeKeywordsRequestIn",
        "BulkEditNegativeKeywordsRequestOut": "_displayvideo_363_BulkEditNegativeKeywordsRequestOut",
        "DoubleVerifyFraudInvalidTrafficIn": "_displayvideo_364_DoubleVerifyFraudInvalidTrafficIn",
        "DoubleVerifyFraudInvalidTrafficOut": "_displayvideo_365_DoubleVerifyFraudInvalidTrafficOut",
        "UserRewardedContentTargetingOptionDetailsIn": "_displayvideo_366_UserRewardedContentTargetingOptionDetailsIn",
        "UserRewardedContentTargetingOptionDetailsOut": "_displayvideo_367_UserRewardedContentTargetingOptionDetailsOut",
        "OmidAssignedTargetingOptionDetailsIn": "_displayvideo_368_OmidAssignedTargetingOptionDetailsIn",
        "OmidAssignedTargetingOptionDetailsOut": "_displayvideo_369_OmidAssignedTargetingOptionDetailsOut",
        "ChannelIn": "_displayvideo_370_ChannelIn",
        "ChannelOut": "_displayvideo_371_ChannelOut",
        "CampaignIn": "_displayvideo_372_CampaignIn",
        "CampaignOut": "_displayvideo_373_CampaignOut",
        "ListAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_374_ListAdvertiserAssignedTargetingOptionsResponseIn",
        "ListAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_375_ListAdvertiserAssignedTargetingOptionsResponseOut",
        "EditCustomerMatchMembersResponseIn": "_displayvideo_376_EditCustomerMatchMembersResponseIn",
        "EditCustomerMatchMembersResponseOut": "_displayvideo_377_EditCustomerMatchMembersResponseOut",
        "BulkListCampaignAssignedTargetingOptionsResponseIn": "_displayvideo_378_BulkListCampaignAssignedTargetingOptionsResponseIn",
        "BulkListCampaignAssignedTargetingOptionsResponseOut": "_displayvideo_379_BulkListCampaignAssignedTargetingOptionsResponseOut",
        "TranscodeIn": "_displayvideo_380_TranscodeIn",
        "TranscodeOut": "_displayvideo_381_TranscodeOut",
        "AdvertiserSdfConfigIn": "_displayvideo_382_AdvertiserSdfConfigIn",
        "AdvertiserSdfConfigOut": "_displayvideo_383_AdvertiserSdfConfigOut",
        "ContentDurationTargetingOptionDetailsIn": "_displayvideo_384_ContentDurationTargetingOptionDetailsIn",
        "ContentDurationTargetingOptionDetailsOut": "_displayvideo_385_ContentDurationTargetingOptionDetailsOut",
        "ContentStreamTypeTargetingOptionDetailsIn": "_displayvideo_386_ContentStreamTypeTargetingOptionDetailsIn",
        "ContentStreamTypeTargetingOptionDetailsOut": "_displayvideo_387_ContentStreamTypeTargetingOptionDetailsOut",
        "MobileAppIn": "_displayvideo_388_MobileAppIn",
        "MobileAppOut": "_displayvideo_389_MobileAppOut",
        "PartnerAdServerConfigIn": "_displayvideo_390_PartnerAdServerConfigIn",
        "PartnerAdServerConfigOut": "_displayvideo_391_PartnerAdServerConfigOut",
        "YoutubeVideoAssignedTargetingOptionDetailsIn": "_displayvideo_392_YoutubeVideoAssignedTargetingOptionDetailsIn",
        "YoutubeVideoAssignedTargetingOptionDetailsOut": "_displayvideo_393_YoutubeVideoAssignedTargetingOptionDetailsOut",
        "AssetIn": "_displayvideo_394_AssetIn",
        "AssetOut": "_displayvideo_395_AssetOut",
        "ConversionCountingConfigIn": "_displayvideo_396_ConversionCountingConfigIn",
        "ConversionCountingConfigOut": "_displayvideo_397_ConversionCountingConfigOut",
        "ExchangeConfigIn": "_displayvideo_398_ExchangeConfigIn",
        "ExchangeConfigOut": "_displayvideo_399_ExchangeConfigOut",
        "ChannelAssignedTargetingOptionDetailsIn": "_displayvideo_400_ChannelAssignedTargetingOptionDetailsIn",
        "ChannelAssignedTargetingOptionDetailsOut": "_displayvideo_401_ChannelAssignedTargetingOptionDetailsOut",
        "ListTargetingOptionsResponseIn": "_displayvideo_402_ListTargetingOptionsResponseIn",
        "ListTargetingOptionsResponseOut": "_displayvideo_403_ListTargetingOptionsResponseOut",
        "YoutubeAndPartnersSettingsIn": "_displayvideo_404_YoutubeAndPartnersSettingsIn",
        "YoutubeAndPartnersSettingsOut": "_displayvideo_405_YoutubeAndPartnersSettingsOut",
        "MaximizeSpendBidStrategyIn": "_displayvideo_406_MaximizeSpendBidStrategyIn",
        "MaximizeSpendBidStrategyOut": "_displayvideo_407_MaximizeSpendBidStrategyOut",
        "CarrierAndIspTargetingOptionDetailsIn": "_displayvideo_408_CarrierAndIspTargetingOptionDetailsIn",
        "CarrierAndIspTargetingOptionDetailsOut": "_displayvideo_409_CarrierAndIspTargetingOptionDetailsOut",
        "InventorySourceFilterIn": "_displayvideo_410_InventorySourceFilterIn",
        "InventorySourceFilterOut": "_displayvideo_411_InventorySourceFilterOut",
        "GuaranteedOrderIn": "_displayvideo_412_GuaranteedOrderIn",
        "GuaranteedOrderOut": "_displayvideo_413_GuaranteedOrderOut",
        "OnScreenPositionAssignedTargetingOptionDetailsIn": "_displayvideo_414_OnScreenPositionAssignedTargetingOptionDetailsIn",
        "OnScreenPositionAssignedTargetingOptionDetailsOut": "_displayvideo_415_OnScreenPositionAssignedTargetingOptionDetailsOut",
        "TargetingExpansionConfigIn": "_displayvideo_416_TargetingExpansionConfigIn",
        "TargetingExpansionConfigOut": "_displayvideo_417_TargetingExpansionConfigOut",
        "ListLineItemsResponseIn": "_displayvideo_418_ListLineItemsResponseIn",
        "ListLineItemsResponseOut": "_displayvideo_419_ListLineItemsResponseOut",
        "EmptyIn": "_displayvideo_420_EmptyIn",
        "EmptyOut": "_displayvideo_421_EmptyOut",
        "DateIn": "_displayvideo_422_DateIn",
        "DateOut": "_displayvideo_423_DateOut",
        "EditInventorySourceReadWriteAccessorsRequestIn": "_displayvideo_424_EditInventorySourceReadWriteAccessorsRequestIn",
        "EditInventorySourceReadWriteAccessorsRequestOut": "_displayvideo_425_EditInventorySourceReadWriteAccessorsRequestOut",
        "ListManualTriggersResponseIn": "_displayvideo_426_ListManualTriggersResponseIn",
        "ListManualTriggersResponseOut": "_displayvideo_427_ListManualTriggersResponseOut",
        "BulkEditSitesResponseIn": "_displayvideo_428_BulkEditSitesResponseIn",
        "BulkEditSitesResponseOut": "_displayvideo_429_BulkEditSitesResponseOut",
        "ProximityLocationListAssignedTargetingOptionDetailsIn": "_displayvideo_430_ProximityLocationListAssignedTargetingOptionDetailsIn",
        "ProximityLocationListAssignedTargetingOptionDetailsOut": "_displayvideo_431_ProximityLocationListAssignedTargetingOptionDetailsOut",
        "NonSkippableAdIn": "_displayvideo_432_NonSkippableAdIn",
        "NonSkippableAdOut": "_displayvideo_433_NonSkippableAdOut",
        "RegionalLocationListAssignedTargetingOptionDetailsIn": "_displayvideo_434_RegionalLocationListAssignedTargetingOptionDetailsIn",
        "RegionalLocationListAssignedTargetingOptionDetailsOut": "_displayvideo_435_RegionalLocationListAssignedTargetingOptionDetailsOut",
        "ListInvoicesResponseIn": "_displayvideo_436_ListInvoicesResponseIn",
        "ListInvoicesResponseOut": "_displayvideo_437_ListInvoicesResponseOut",
        "VideoPlayerSizeTargetingOptionDetailsIn": "_displayvideo_438_VideoPlayerSizeTargetingOptionDetailsIn",
        "VideoPlayerSizeTargetingOptionDetailsOut": "_displayvideo_439_VideoPlayerSizeTargetingOptionDetailsOut",
        "BulkUpdateLineItemsRequestIn": "_displayvideo_440_BulkUpdateLineItemsRequestIn",
        "BulkUpdateLineItemsRequestOut": "_displayvideo_441_BulkUpdateLineItemsRequestOut",
        "ListNegativeKeywordsResponseIn": "_displayvideo_442_ListNegativeKeywordsResponseIn",
        "ListNegativeKeywordsResponseOut": "_displayvideo_443_ListNegativeKeywordsResponseOut",
        "DuplicateLineItemRequestIn": "_displayvideo_444_DuplicateLineItemRequestIn",
        "DuplicateLineItemRequestOut": "_displayvideo_445_DuplicateLineItemRequestOut",
        "ContentInstreamPositionAssignedTargetingOptionDetailsIn": "_displayvideo_446_ContentInstreamPositionAssignedTargetingOptionDetailsIn",
        "ContentInstreamPositionAssignedTargetingOptionDetailsOut": "_displayvideo_447_ContentInstreamPositionAssignedTargetingOptionDetailsOut",
        "ListUsersResponseIn": "_displayvideo_448_ListUsersResponseIn",
        "ListUsersResponseOut": "_displayvideo_449_ListUsersResponseOut",
        "BrowserAssignedTargetingOptionDetailsIn": "_displayvideo_450_BrowserAssignedTargetingOptionDetailsIn",
        "BrowserAssignedTargetingOptionDetailsOut": "_displayvideo_451_BrowserAssignedTargetingOptionDetailsOut",
        "SearchTargetingOptionsResponseIn": "_displayvideo_452_SearchTargetingOptionsResponseIn",
        "SearchTargetingOptionsResponseOut": "_displayvideo_453_SearchTargetingOptionsResponseOut",
        "GenerateDefaultLineItemRequestIn": "_displayvideo_454_GenerateDefaultLineItemRequestIn",
        "GenerateDefaultLineItemRequestOut": "_displayvideo_455_GenerateDefaultLineItemRequestOut",
        "BulkEditAdvertiserAssignedTargetingOptionsRequestIn": "_displayvideo_456_BulkEditAdvertiserAssignedTargetingOptionsRequestIn",
        "BulkEditAdvertiserAssignedTargetingOptionsRequestOut": "_displayvideo_457_BulkEditAdvertiserAssignedTargetingOptionsRequestOut",
        "ReplaceSitesResponseIn": "_displayvideo_458_ReplaceSitesResponseIn",
        "ReplaceSitesResponseOut": "_displayvideo_459_ReplaceSitesResponseOut",
        "UniversalAdIdIn": "_displayvideo_460_UniversalAdIdIn",
        "UniversalAdIdOut": "_displayvideo_461_UniversalAdIdOut",
        "GenderTargetingOptionDetailsIn": "_displayvideo_462_GenderTargetingOptionDetailsIn",
        "GenderTargetingOptionDetailsOut": "_displayvideo_463_GenderTargetingOptionDetailsOut",
        "OmidTargetingOptionDetailsIn": "_displayvideo_464_OmidTargetingOptionDetailsIn",
        "OmidTargetingOptionDetailsOut": "_displayvideo_465_OmidTargetingOptionDetailsOut",
        "FirstAndThirdPartyAudienceGroupIn": "_displayvideo_466_FirstAndThirdPartyAudienceGroupIn",
        "FirstAndThirdPartyAudienceGroupOut": "_displayvideo_467_FirstAndThirdPartyAudienceGroupOut",
        "ListAssignedLocationsResponseIn": "_displayvideo_468_ListAssignedLocationsResponseIn",
        "ListAssignedLocationsResponseOut": "_displayvideo_469_ListAssignedLocationsResponseOut",
        "BulkListAdGroupAssignedTargetingOptionsResponseIn": "_displayvideo_470_BulkListAdGroupAssignedTargetingOptionsResponseIn",
        "BulkListAdGroupAssignedTargetingOptionsResponseOut": "_displayvideo_471_BulkListAdGroupAssignedTargetingOptionsResponseOut",
        "CreateAssetResponseIn": "_displayvideo_472_CreateAssetResponseIn",
        "CreateAssetResponseOut": "_displayvideo_473_CreateAssetResponseOut",
        "TimerEventIn": "_displayvideo_474_TimerEventIn",
        "TimerEventOut": "_displayvideo_475_TimerEventOut",
        "PartnerDataAccessConfigIn": "_displayvideo_476_PartnerDataAccessConfigIn",
        "PartnerDataAccessConfigOut": "_displayvideo_477_PartnerDataAccessConfigOut",
        "InventorySourceVideoCreativeConfigIn": "_displayvideo_478_InventorySourceVideoCreativeConfigIn",
        "InventorySourceVideoCreativeConfigOut": "_displayvideo_479_InventorySourceVideoCreativeConfigOut",
        "BudgetSummaryIn": "_displayvideo_480_BudgetSummaryIn",
        "BudgetSummaryOut": "_displayvideo_481_BudgetSummaryOut",
        "KeywordAssignedTargetingOptionDetailsIn": "_displayvideo_482_KeywordAssignedTargetingOptionDetailsIn",
        "KeywordAssignedTargetingOptionDetailsOut": "_displayvideo_483_KeywordAssignedTargetingOptionDetailsOut",
        "ListCreativesResponseIn": "_displayvideo_484_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_displayvideo_485_ListCreativesResponseOut",
        "ActiveViewVideoViewabilityMetricConfigIn": "_displayvideo_486_ActiveViewVideoViewabilityMetricConfigIn",
        "ActiveViewVideoViewabilityMetricConfigOut": "_displayvideo_487_ActiveViewVideoViewabilityMetricConfigOut",
        "GeoRegionTargetingOptionDetailsIn": "_displayvideo_488_GeoRegionTargetingOptionDetailsIn",
        "GeoRegionTargetingOptionDetailsOut": "_displayvideo_489_GeoRegionTargetingOptionDetailsOut",
        "DigitalContentLabelAssignedTargetingOptionDetailsIn": "_displayvideo_490_DigitalContentLabelAssignedTargetingOptionDetailsIn",
        "DigitalContentLabelAssignedTargetingOptionDetailsOut": "_displayvideo_491_DigitalContentLabelAssignedTargetingOptionDetailsOut",
        "CombinedAudienceGroupIn": "_displayvideo_492_CombinedAudienceGroupIn",
        "CombinedAudienceGroupOut": "_displayvideo_493_CombinedAudienceGroupOut",
        "VideoPerformanceAdIn": "_displayvideo_494_VideoPerformanceAdIn",
        "VideoPerformanceAdOut": "_displayvideo_495_VideoPerformanceAdOut",
        "BulkListAssignedTargetingOptionsResponseIn": "_displayvideo_496_BulkListAssignedTargetingOptionsResponseIn",
        "BulkListAssignedTargetingOptionsResponseOut": "_displayvideo_497_BulkListAssignedTargetingOptionsResponseOut",
        "VideoDiscoveryAdIn": "_displayvideo_498_VideoDiscoveryAdIn",
        "VideoDiscoveryAdOut": "_displayvideo_499_VideoDiscoveryAdOut",
        "CampaignFlightIn": "_displayvideo_500_CampaignFlightIn",
        "CampaignFlightOut": "_displayvideo_501_CampaignFlightOut",
        "BulkEditAssignedUserRolesRequestIn": "_displayvideo_502_BulkEditAssignedUserRolesRequestIn",
        "BulkEditAssignedUserRolesRequestOut": "_displayvideo_503_BulkEditAssignedUserRolesRequestOut",
        "ParentalStatusAssignedTargetingOptionDetailsIn": "_displayvideo_504_ParentalStatusAssignedTargetingOptionDetailsIn",
        "ParentalStatusAssignedTargetingOptionDetailsOut": "_displayvideo_505_ParentalStatusAssignedTargetingOptionDetailsOut",
        "NegativeKeywordListIn": "_displayvideo_506_NegativeKeywordListIn",
        "NegativeKeywordListOut": "_displayvideo_507_NegativeKeywordListOut",
        "YoutubeAndPartnersBiddingStrategyIn": "_displayvideo_508_YoutubeAndPartnersBiddingStrategyIn",
        "YoutubeAndPartnersBiddingStrategyOut": "_displayvideo_509_YoutubeAndPartnersBiddingStrategyOut",
        "OnScreenPositionTargetingOptionDetailsIn": "_displayvideo_510_OnScreenPositionTargetingOptionDetailsIn",
        "OnScreenPositionTargetingOptionDetailsOut": "_displayvideo_511_OnScreenPositionTargetingOptionDetailsOut",
        "InventorySourceAccessorsAdvertiserAccessorsIn": "_displayvideo_512_InventorySourceAccessorsAdvertiserAccessorsIn",
        "InventorySourceAccessorsAdvertiserAccessorsOut": "_displayvideo_513_InventorySourceAccessorsAdvertiserAccessorsOut",
        "BulkEditAssignedInventorySourcesRequestIn": "_displayvideo_514_BulkEditAssignedInventorySourcesRequestIn",
        "BulkEditAssignedInventorySourcesRequestOut": "_displayvideo_515_BulkEditAssignedInventorySourcesRequestOut",
        "InsertionOrderBudgetIn": "_displayvideo_516_InsertionOrderBudgetIn",
        "InsertionOrderBudgetOut": "_displayvideo_517_InsertionOrderBudgetOut",
        "GeoRegionSearchTermsIn": "_displayvideo_518_GeoRegionSearchTermsIn",
        "GeoRegionSearchTermsOut": "_displayvideo_519_GeoRegionSearchTermsOut",
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn": "_displayvideo_520_EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn",
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut": "_displayvideo_521_EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut",
        "AdvertiserTargetingConfigIn": "_displayvideo_522_AdvertiserTargetingConfigIn",
        "AdvertiserTargetingConfigOut": "_displayvideo_523_AdvertiserTargetingConfigOut",
        "AssignedInventorySourceIn": "_displayvideo_524_AssignedInventorySourceIn",
        "AssignedInventorySourceOut": "_displayvideo_525_AssignedInventorySourceOut",
        "LineItemAssignedTargetingOptionIn": "_displayvideo_526_LineItemAssignedTargetingOptionIn",
        "LineItemAssignedTargetingOptionOut": "_displayvideo_527_LineItemAssignedTargetingOptionOut",
        "ThirdPartyVendorConfigIn": "_displayvideo_528_ThirdPartyVendorConfigIn",
        "ThirdPartyVendorConfigOut": "_displayvideo_529_ThirdPartyVendorConfigOut",
        "ListFirstAndThirdPartyAudiencesResponseIn": "_displayvideo_530_ListFirstAndThirdPartyAudiencesResponseIn",
        "ListFirstAndThirdPartyAudiencesResponseOut": "_displayvideo_531_ListFirstAndThirdPartyAudiencesResponseOut",
        "NativeContentPositionAssignedTargetingOptionDetailsIn": "_displayvideo_532_NativeContentPositionAssignedTargetingOptionDetailsIn",
        "NativeContentPositionAssignedTargetingOptionDetailsOut": "_displayvideo_533_NativeContentPositionAssignedTargetingOptionDetailsOut",
        "CreativeConfigIn": "_displayvideo_534_CreativeConfigIn",
        "CreativeConfigOut": "_displayvideo_535_CreativeConfigOut",
        "BulkEditAssignedInventorySourcesResponseIn": "_displayvideo_536_BulkEditAssignedInventorySourcesResponseIn",
        "BulkEditAssignedInventorySourcesResponseOut": "_displayvideo_537_BulkEditAssignedInventorySourcesResponseOut",
        "CreateAssignedTargetingOptionsRequestIn": "_displayvideo_538_CreateAssignedTargetingOptionsRequestIn",
        "CreateAssignedTargetingOptionsRequestOut": "_displayvideo_539_CreateAssignedTargetingOptionsRequestOut",
        "CustomLabelIn": "_displayvideo_540_CustomLabelIn",
        "CustomLabelOut": "_displayvideo_541_CustomLabelOut",
        "ObaIconIn": "_displayvideo_542_ObaIconIn",
        "ObaIconOut": "_displayvideo_543_ObaIconOut",
        "IntegralAdScienceIn": "_displayvideo_544_IntegralAdScienceIn",
        "IntegralAdScienceOut": "_displayvideo_545_IntegralAdScienceOut",
        "AudioAdIn": "_displayvideo_546_AudioAdIn",
        "AudioAdOut": "_displayvideo_547_AudioAdOut",
        "DeviceTypeTargetingOptionDetailsIn": "_displayvideo_548_DeviceTypeTargetingOptionDetailsIn",
        "DeviceTypeTargetingOptionDetailsOut": "_displayvideo_549_DeviceTypeTargetingOptionDetailsOut",
        "CustomBiddingScriptRefIn": "_displayvideo_550_CustomBiddingScriptRefIn",
        "CustomBiddingScriptRefOut": "_displayvideo_551_CustomBiddingScriptRefOut",
        "BulkListInsertionOrderAssignedTargetingOptionsResponseIn": "_displayvideo_552_BulkListInsertionOrderAssignedTargetingOptionsResponseIn",
        "BulkListInsertionOrderAssignedTargetingOptionsResponseOut": "_displayvideo_553_BulkListInsertionOrderAssignedTargetingOptionsResponseOut",
        "CampaignBudgetIn": "_displayvideo_554_CampaignBudgetIn",
        "CampaignBudgetOut": "_displayvideo_555_CampaignBudgetOut",
        "CategoryTargetingOptionDetailsIn": "_displayvideo_556_CategoryTargetingOptionDetailsIn",
        "CategoryTargetingOptionDetailsOut": "_displayvideo_557_CategoryTargetingOptionDetailsOut",
        "ContentOutstreamPositionTargetingOptionDetailsIn": "_displayvideo_558_ContentOutstreamPositionTargetingOptionDetailsIn",
        "ContentOutstreamPositionTargetingOptionDetailsOut": "_displayvideo_559_ContentOutstreamPositionTargetingOptionDetailsOut",
        "AdUrlIn": "_displayvideo_560_AdUrlIn",
        "AdUrlOut": "_displayvideo_561_AdUrlOut",
        "PacingIn": "_displayvideo_562_PacingIn",
        "PacingOut": "_displayvideo_563_PacingOut",
        "CategoryAssignedTargetingOptionDetailsIn": "_displayvideo_564_CategoryAssignedTargetingOptionDetailsIn",
        "CategoryAssignedTargetingOptionDetailsOut": "_displayvideo_565_CategoryAssignedTargetingOptionDetailsOut",
        "ListCampaignsResponseIn": "_displayvideo_566_ListCampaignsResponseIn",
        "ListCampaignsResponseOut": "_displayvideo_567_ListCampaignsResponseOut",
        "ListLocationListsResponseIn": "_displayvideo_568_ListLocationListsResponseIn",
        "ListLocationListsResponseOut": "_displayvideo_569_ListLocationListsResponseOut",
        "ThirdPartyOnlyConfigIn": "_displayvideo_570_ThirdPartyOnlyConfigIn",
        "ThirdPartyOnlyConfigOut": "_displayvideo_571_ThirdPartyOnlyConfigOut",
        "InventorySourceAssignedTargetingOptionDetailsIn": "_displayvideo_572_InventorySourceAssignedTargetingOptionDetailsIn",
        "InventorySourceAssignedTargetingOptionDetailsOut": "_displayvideo_573_InventorySourceAssignedTargetingOptionDetailsOut",
        "LineItemIn": "_displayvideo_574_LineItemIn",
        "LineItemOut": "_displayvideo_575_LineItemOut",
        "PartnerGeneralConfigIn": "_displayvideo_576_PartnerGeneralConfigIn",
        "PartnerGeneralConfigOut": "_displayvideo_577_PartnerGeneralConfigOut",
        "ParentEntityFilterIn": "_displayvideo_578_ParentEntityFilterIn",
        "ParentEntityFilterOut": "_displayvideo_579_ParentEntityFilterOut",
        "PerformanceGoalBidStrategyIn": "_displayvideo_580_PerformanceGoalBidStrategyIn",
        "PerformanceGoalBidStrategyOut": "_displayvideo_581_PerformanceGoalBidStrategyOut",
        "ReplaceNegativeKeywordsRequestIn": "_displayvideo_582_ReplaceNegativeKeywordsRequestIn",
        "ReplaceNegativeKeywordsRequestOut": "_displayvideo_583_ReplaceNegativeKeywordsRequestOut",
        "OperatingSystemAssignedTargetingOptionDetailsIn": "_displayvideo_584_OperatingSystemAssignedTargetingOptionDetailsIn",
        "OperatingSystemAssignedTargetingOptionDetailsOut": "_displayvideo_585_OperatingSystemAssignedTargetingOptionDetailsOut",
        "ContentInstreamPositionTargetingOptionDetailsIn": "_displayvideo_586_ContentInstreamPositionTargetingOptionDetailsIn",
        "ContentInstreamPositionTargetingOptionDetailsOut": "_displayvideo_587_ContentInstreamPositionTargetingOptionDetailsOut",
        "UserIn": "_displayvideo_588_UserIn",
        "UserOut": "_displayvideo_589_UserOut",
        "AdvertiserIn": "_displayvideo_590_AdvertiserIn",
        "AdvertiserOut": "_displayvideo_591_AdvertiserOut",
        "CombinedAudienceIn": "_displayvideo_592_CombinedAudienceIn",
        "CombinedAudienceOut": "_displayvideo_593_CombinedAudienceOut",
        "PartnerRevenueModelIn": "_displayvideo_594_PartnerRevenueModelIn",
        "PartnerRevenueModelOut": "_displayvideo_595_PartnerRevenueModelOut",
        "CreateSdfDownloadTaskRequestIn": "_displayvideo_596_CreateSdfDownloadTaskRequestIn",
        "CreateSdfDownloadTaskRequestOut": "_displayvideo_597_CreateSdfDownloadTaskRequestOut",
        "ListAdvertisersResponseIn": "_displayvideo_598_ListAdvertisersResponseIn",
        "ListAdvertisersResponseOut": "_displayvideo_599_ListAdvertisersResponseOut",
        "AgeRangeTargetingOptionDetailsIn": "_displayvideo_600_AgeRangeTargetingOptionDetailsIn",
        "AgeRangeTargetingOptionDetailsOut": "_displayvideo_601_AgeRangeTargetingOptionDetailsOut",
        "ListInsertionOrdersResponseIn": "_displayvideo_602_ListInsertionOrdersResponseIn",
        "ListInsertionOrdersResponseOut": "_displayvideo_603_ListInsertionOrdersResponseOut",
        "CombinedAudienceTargetingSettingIn": "_displayvideo_604_CombinedAudienceTargetingSettingIn",
        "CombinedAudienceTargetingSettingOut": "_displayvideo_605_CombinedAudienceTargetingSettingOut",
        "CounterEventIn": "_displayvideo_606_CounterEventIn",
        "CounterEventOut": "_displayvideo_607_CounterEventOut",
        "CmTrackingAdIn": "_displayvideo_608_CmTrackingAdIn",
        "CmTrackingAdOut": "_displayvideo_609_CmTrackingAdOut",
        "BulkEditPartnerAssignedTargetingOptionsResponseIn": "_displayvideo_610_BulkEditPartnerAssignedTargetingOptionsResponseIn",
        "BulkEditPartnerAssignedTargetingOptionsResponseOut": "_displayvideo_611_BulkEditPartnerAssignedTargetingOptionsResponseOut",
        "ExchangeConfigEnabledExchangeIn": "_displayvideo_612_ExchangeConfigEnabledExchangeIn",
        "ExchangeConfigEnabledExchangeOut": "_displayvideo_613_ExchangeConfigEnabledExchangeOut",
        "PrismaCpeCodeIn": "_displayvideo_614_PrismaCpeCodeIn",
        "PrismaCpeCodeOut": "_displayvideo_615_PrismaCpeCodeOut",
        "PoiSearchTermsIn": "_displayvideo_616_PoiSearchTermsIn",
        "PoiSearchTermsOut": "_displayvideo_617_PoiSearchTermsOut",
        "ListPartnersResponseIn": "_displayvideo_618_ListPartnersResponseIn",
        "ListPartnersResponseOut": "_displayvideo_619_ListPartnersResponseOut",
        "YoutubeAdGroupAssignedTargetingOptionIn": "_displayvideo_620_YoutubeAdGroupAssignedTargetingOptionIn",
        "YoutubeAdGroupAssignedTargetingOptionOut": "_displayvideo_621_YoutubeAdGroupAssignedTargetingOptionOut",
        "LookbackWindowIn": "_displayvideo_622_LookbackWindowIn",
        "LookbackWindowOut": "_displayvideo_623_LookbackWindowOut",
        "AssignedUserRoleIn": "_displayvideo_624_AssignedUserRoleIn",
        "AssignedUserRoleOut": "_displayvideo_625_AssignedUserRoleOut",
        "VideoAdSequenceSettingsIn": "_displayvideo_626_VideoAdSequenceSettingsIn",
        "VideoAdSequenceSettingsOut": "_displayvideo_627_VideoAdSequenceSettingsOut",
        "ContentGenreAssignedTargetingOptionDetailsIn": "_displayvideo_628_ContentGenreAssignedTargetingOptionDetailsIn",
        "ContentGenreAssignedTargetingOptionDetailsOut": "_displayvideo_629_ContentGenreAssignedTargetingOptionDetailsOut",
        "StatusIn": "_displayvideo_630_StatusIn",
        "StatusOut": "_displayvideo_631_StatusOut",
        "CommonInStreamAttributeIn": "_displayvideo_632_CommonInStreamAttributeIn",
        "CommonInStreamAttributeOut": "_displayvideo_633_CommonInStreamAttributeOut",
        "AdvertiserGeneralConfigIn": "_displayvideo_634_AdvertiserGeneralConfigIn",
        "AdvertiserGeneralConfigOut": "_displayvideo_635_AdvertiserGeneralConfigOut",
        "ParentalStatusTargetingOptionDetailsIn": "_displayvideo_636_ParentalStatusTargetingOptionDetailsIn",
        "ParentalStatusTargetingOptionDetailsOut": "_displayvideo_637_ParentalStatusTargetingOptionDetailsOut",
        "MoneyIn": "_displayvideo_638_MoneyIn",
        "MoneyOut": "_displayvideo_639_MoneyOut",
        "SubExchangeAssignedTargetingOptionDetailsIn": "_displayvideo_640_SubExchangeAssignedTargetingOptionDetailsIn",
        "SubExchangeAssignedTargetingOptionDetailsOut": "_displayvideo_641_SubExchangeAssignedTargetingOptionDetailsOut",
        "InsertionOrderIn": "_displayvideo_642_InsertionOrderIn",
        "InsertionOrderOut": "_displayvideo_643_InsertionOrderOut",
        "CustomListIn": "_displayvideo_644_CustomListIn",
        "CustomListOut": "_displayvideo_645_CustomListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GeoRegionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["GeoRegionAssignedTargetingOptionDetailsIn"])
    types["GeoRegionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "geoRegionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionAssignedTargetingOptionDetailsOut"])
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
    types["DeviceMakeModelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"])
    types["DeviceMakeModelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMakeModelAssignedTargetingOptionDetailsOut"])
    types["TrackingFloodlightActivityConfigIn"] = t.struct(
        {
            "postClickLookbackWindowDays": t.integer(),
            "floodlightActivityId": t.string(),
            "postViewLookbackWindowDays": t.integer(),
        }
    ).named(renames["TrackingFloodlightActivityConfigIn"])
    types["TrackingFloodlightActivityConfigOut"] = t.struct(
        {
            "postClickLookbackWindowDays": t.integer(),
            "floodlightActivityId": t.string(),
            "postViewLookbackWindowDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackingFloodlightActivityConfigOut"])
    types["RateDetailsIn"] = t.struct(
        {
            "inventorySourceRateType": t.string().optional(),
            "rate": t.proxy(renames["MoneyIn"]).optional(),
            "unitsPurchased": t.string(),
        }
    ).named(renames["RateDetailsIn"])
    types["RateDetailsOut"] = t.struct(
        {
            "inventorySourceRateType": t.string().optional(),
            "rate": t.proxy(renames["MoneyOut"]).optional(),
            "unitsPurchased": t.string(),
            "minimumSpend": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateDetailsOut"])
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
    types["ReviewStatusInfoIn"] = t.struct(
        {
            "approvalStatus": t.string().optional(),
            "exchangeReviewStatuses": t.array(
                t.proxy(renames["ExchangeReviewStatusIn"])
            ).optional(),
            "creativeAndLandingPageReviewStatus": t.string().optional(),
            "publisherReviewStatuses": t.array(
                t.proxy(renames["PublisherReviewStatusIn"])
            ).optional(),
            "contentAndPolicyReviewStatus": t.string().optional(),
        }
    ).named(renames["ReviewStatusInfoIn"])
    types["ReviewStatusInfoOut"] = t.struct(
        {
            "approvalStatus": t.string().optional(),
            "exchangeReviewStatuses": t.array(
                t.proxy(renames["ExchangeReviewStatusOut"])
            ).optional(),
            "creativeAndLandingPageReviewStatus": t.string().optional(),
            "publisherReviewStatuses": t.array(
                t.proxy(renames["PublisherReviewStatusOut"])
            ).optional(),
            "contentAndPolicyReviewStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewStatusInfoOut"])
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
    types["DayAndTimeAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "endHour": t.integer(),
            "timeZoneResolution": t.string(),
            "dayOfWeek": t.string(),
            "startHour": t.integer(),
        }
    ).named(renames["DayAndTimeAssignedTargetingOptionDetailsIn"])
    types["DayAndTimeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "endHour": t.integer(),
            "timeZoneResolution": t.string(),
            "dayOfWeek": t.string(),
            "startHour": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayAndTimeAssignedTargetingOptionDetailsOut"])
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
    types["GenderAssignedTargetingOptionDetailsIn"] = t.struct(
        {"gender": t.string().optional()}
    ).named(renames["GenderAssignedTargetingOptionDetailsIn"])
    types["GenderAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderAssignedTargetingOptionDetailsOut"])
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
    types["ReplaceSitesRequestIn"] = t.struct(
        {
            "newSites": t.array(t.proxy(renames["SiteIn"])).optional(),
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
        }
    ).named(renames["ReplaceSitesRequestIn"])
    types["ReplaceSitesRequestOut"] = t.struct(
        {
            "newSites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceSitesRequestOut"])
    types["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"contentOutstreamPosition": t.string().optional()}
    ).named(renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"])
    types["ContentOutstreamPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "adType": t.string().optional(),
            "contentOutstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOutstreamPositionAssignedTargetingOptionDetailsOut"])
    types["LocationListIn"] = t.struct(
        {
            "advertiserId": t.string(),
            "displayName": t.string(),
            "locationType": t.string(),
        }
    ).named(renames["LocationListIn"])
    types["LocationListOut"] = t.struct(
        {
            "locationListId": t.string().optional(),
            "name": t.string().optional(),
            "advertiserId": t.string(),
            "displayName": t.string(),
            "locationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationListOut"])
    types["SessionPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"sessionPosition": t.string().optional()}
    ).named(renames["SessionPositionAssignedTargetingOptionDetailsIn"])
    types["SessionPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "sessionPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionPositionAssignedTargetingOptionDetailsOut"])
    types["NegativeKeywordIn"] = t.struct({"keywordValue": t.string()}).named(
        renames["NegativeKeywordIn"]
    )
    types["NegativeKeywordOut"] = t.struct(
        {
            "keywordValue": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordOut"])
    types["DeviceMakeModelTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeviceMakeModelTargetingOptionDetailsIn"])
    types["DeviceMakeModelTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMakeModelTargetingOptionDetailsOut"])
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
    types["ProductFeedDataIn"] = t.struct(
        {
            "productMatchDimensions": t.array(
                t.proxy(renames["ProductMatchDimensionIn"])
            ).optional(),
            "isFeedDisabled": t.boolean().optional(),
            "productMatchType": t.string().optional(),
        }
    ).named(renames["ProductFeedDataIn"])
    types["ProductFeedDataOut"] = t.struct(
        {
            "productMatchDimensions": t.array(
                t.proxy(renames["ProductMatchDimensionOut"])
            ).optional(),
            "isFeedDisabled": t.boolean().optional(),
            "productMatchType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductFeedDataOut"])
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
    types["CustomListTargetingSettingIn"] = t.struct(
        {"customListId": t.string()}
    ).named(renames["CustomListTargetingSettingIn"])
    types["CustomListTargetingSettingOut"] = t.struct(
        {
            "customListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListTargetingSettingOut"])
    types["AudienceGroupAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "includedCombinedAudienceGroup": t.proxy(
                renames["CombinedAudienceGroupIn"]
            ).optional(),
            "excludedFirstAndThirdPartyAudienceGroup": t.proxy(
                renames["FirstAndThirdPartyAudienceGroupIn"]
            ).optional(),
            "excludedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupIn"]
            ).optional(),
            "includedCustomListGroup": t.proxy(renames["CustomListGroupIn"]).optional(),
            "includedFirstAndThirdPartyAudienceGroups": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceGroupIn"])
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
            "excludedFirstAndThirdPartyAudienceGroup": t.proxy(
                renames["FirstAndThirdPartyAudienceGroupOut"]
            ).optional(),
            "excludedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupOut"]
            ).optional(),
            "includedCustomListGroup": t.proxy(
                renames["CustomListGroupOut"]
            ).optional(),
            "includedFirstAndThirdPartyAudienceGroups": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceGroupOut"])
            ).optional(),
            "includedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudienceGroupAssignedTargetingOptionDetailsOut"])
    types["IntegrationDetailsIn"] = t.struct(
        {"integrationCode": t.string().optional(), "details": t.string().optional()}
    ).named(renames["IntegrationDetailsIn"])
    types["IntegrationDetailsOut"] = t.struct(
        {
            "integrationCode": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegrationDetailsOut"])
    types["ExchangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ExchangeTargetingOptionDetailsIn"])
    types["ExchangeTargetingOptionDetailsOut"] = t.struct(
        {
            "exchange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeTargetingOptionDetailsOut"])
    types["AppCategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppCategoryTargetingOptionDetailsIn"])
    types["AppCategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppCategoryTargetingOptionDetailsOut"])
    types["OperatingSystemTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OperatingSystemTargetingOptionDetailsIn"])
    types["OperatingSystemTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemTargetingOptionDetailsOut"])
    types["InventorySourceDisplayCreativeConfigIn"] = t.struct(
        {"creativeSize": t.proxy(renames["DimensionsIn"]).optional()}
    ).named(renames["InventorySourceDisplayCreativeConfigIn"])
    types["InventorySourceDisplayCreativeConfigOut"] = t.struct(
        {
            "creativeSize": t.proxy(renames["DimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceDisplayCreativeConfigOut"])
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
    types["ContactInfoIn"] = t.struct(
        {
            "hashedEmails": t.array(t.string()).optional(),
            "countryCode": t.string().optional(),
            "hashedFirstName": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "hashedPhoneNumbers": t.array(t.string()).optional(),
            "zipCodes": t.array(t.string()).optional(),
        }
    ).named(renames["ContactInfoIn"])
    types["ContactInfoOut"] = t.struct(
        {
            "hashedEmails": t.array(t.string()).optional(),
            "countryCode": t.string().optional(),
            "hashedFirstName": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "hashedPhoneNumbers": t.array(t.string()).optional(),
            "zipCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoOut"])
    types["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "adloox": t.proxy(renames["AdlooxIn"]).optional(),
            "doubleVerify": t.proxy(renames["DoubleVerifyIn"]).optional(),
            "integralAdScience": t.proxy(renames["IntegralAdScienceIn"]).optional(),
        }
    ).named(renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"])
    types["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "adloox": t.proxy(renames["AdlooxOut"]).optional(),
            "doubleVerify": t.proxy(renames["DoubleVerifyOut"]).optional(),
            "integralAdScience": t.proxy(renames["IntegralAdScienceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"])
    types["ContentStreamTypeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"])
    types["ContentStreamTypeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "contentStreamType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentStreamTypeAssignedTargetingOptionDetailsOut"])
    types["GuaranteedOrderStatusIn"] = t.struct(
        {
            "entityPauseReason": t.string().optional(),
            "entityStatus": t.string().optional(),
        }
    ).named(renames["GuaranteedOrderStatusIn"])
    types["GuaranteedOrderStatusOut"] = t.struct(
        {
            "configStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
            "entityStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedOrderStatusOut"])
    types["InventorySourceStatusIn"] = t.struct(
        {
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
        }
    ).named(renames["InventorySourceStatusIn"])
    types["InventorySourceStatusOut"] = t.struct(
        {
            "configStatus": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
            "sellerStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceStatusOut"])
    types["FrequencyCapIn"] = t.struct(
        {
            "maxImpressions": t.integer().optional(),
            "timeUnitCount": t.integer().optional(),
            "timeUnit": t.string().optional(),
            "maxViews": t.integer().optional(),
            "unlimited": t.boolean().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "maxImpressions": t.integer().optional(),
            "timeUnitCount": t.integer().optional(),
            "timeUnit": t.string().optional(),
            "maxViews": t.integer().optional(),
            "unlimited": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
    types["GoogleAudienceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAudienceIn"]
    )
    types["GoogleAudienceOut"] = t.struct(
        {
            "googleAudienceId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "googleAudienceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceOut"])
    types["ViewabilityAssignedTargetingOptionDetailsIn"] = t.struct(
        {"viewability": t.string().optional()}
    ).named(renames["ViewabilityAssignedTargetingOptionDetailsIn"])
    types["ViewabilityAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "viewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewabilityAssignedTargetingOptionDetailsOut"])
    types["PoiTargetingOptionDetailsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PoiTargetingOptionDetailsIn"]
    )
    types["PoiTargetingOptionDetailsOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiTargetingOptionDetailsOut"])
    types["VideoPlayerSizeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"videoPlayerSize": t.string().optional()}
    ).named(renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"])
    types["VideoPlayerSizeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "videoPlayerSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerSizeAssignedTargetingOptionDetailsOut"])
    types["NegativeKeywordListAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negativeKeywordListId": t.string()}
    ).named(renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"])
    types["NegativeKeywordListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negativeKeywordListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordListAssignedTargetingOptionDetailsOut"])
    types["InventorySourceAccessorsPartnerAccessorIn"] = t.struct(
        {"partnerId": t.string().optional()}
    ).named(renames["InventorySourceAccessorsPartnerAccessorIn"])
    types["InventorySourceAccessorsPartnerAccessorOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsPartnerAccessorOut"])
    types["CustomListGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["CustomListTargetingSettingIn"]))}
    ).named(renames["CustomListGroupIn"])
    types["CustomListGroupOut"] = t.struct(
        {
            "settings": t.array(t.proxy(renames["CustomListTargetingSettingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListGroupOut"])
    types["DisplayVideoSourceAdIn"] = t.struct(
        {"creativeId": t.string().optional()}
    ).named(renames["DisplayVideoSourceAdIn"])
    types["DisplayVideoSourceAdOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayVideoSourceAdOut"])
    types["GoogleAudienceGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["GoogleAudienceTargetingSettingIn"]))}
    ).named(renames["GoogleAudienceGroupIn"])
    types["GoogleAudienceGroupOut"] = t.struct(
        {
            "settings": t.array(t.proxy(renames["GoogleAudienceTargetingSettingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceGroupOut"])
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
    types["GoogleAudienceTargetingSettingIn"] = t.struct(
        {"googleAudienceId": t.string()}
    ).named(renames["GoogleAudienceTargetingSettingIn"])
    types["GoogleAudienceTargetingSettingOut"] = t.struct(
        {
            "googleAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceTargetingSettingOut"])
    types["HouseholdIncomeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"householdIncome": t.string().optional()}
    ).named(renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"])
    types["HouseholdIncomeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "householdIncome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HouseholdIncomeAssignedTargetingOptionDetailsOut"])
    types["CustomBiddingAlgorithmIn"] = t.struct(
        {
            "customBiddingAlgorithmType": t.string(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "displayName": t.string(),
            "entityStatus": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
        }
    ).named(renames["CustomBiddingAlgorithmIn"])
    types["CustomBiddingAlgorithmOut"] = t.struct(
        {
            "customBiddingAlgorithmType": t.string(),
            "partnerId": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "modelDetails": t.array(
                t.proxy(renames["CustomBiddingModelDetailsOut"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "entityStatus": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingAlgorithmOut"])
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
    types["ExitEventIn"] = t.struct(
        {
            "url": t.string(),
            "type": t.string(),
            "reportingName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ExitEventIn"])
    types["ExitEventOut"] = t.struct(
        {
            "url": t.string(),
            "type": t.string(),
            "reportingName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExitEventOut"])
    types["SensitiveCategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"excludedSensitiveCategory": t.string()}
    ).named(renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"])
    types["SensitiveCategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "excludedSensitiveCategory": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveCategoryAssignedTargetingOptionDetailsOut"])
    types["AdlooxIn"] = t.struct(
        {"excludedAdlooxCategories": t.array(t.string()).optional()}
    ).named(renames["AdlooxIn"])
    types["AdlooxOut"] = t.struct(
        {
            "excludedAdlooxCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdlooxOut"])
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
            "nextPageToken": t.string().optional(),
            "googleAudiences": t.array(t.proxy(renames["GoogleAudienceIn"])).optional(),
        }
    ).named(renames["ListGoogleAudiencesResponseIn"])
    types["ListGoogleAudiencesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "googleAudiences": t.array(
                t.proxy(renames["GoogleAudienceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGoogleAudiencesResponseOut"])
    types["PartnerIn"] = t.struct(
        {
            "exchangeConfig": t.proxy(renames["ExchangeConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "adServerConfig": t.proxy(renames["PartnerAdServerConfigIn"]).optional(),
            "generalConfig": t.proxy(renames["PartnerGeneralConfigIn"]).optional(),
            "dataAccessConfig": t.proxy(
                renames["PartnerDataAccessConfigIn"]
            ).optional(),
        }
    ).named(renames["PartnerIn"])
    types["PartnerOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "partnerId": t.string().optional(),
            "name": t.string().optional(),
            "exchangeConfig": t.proxy(renames["ExchangeConfigOut"]).optional(),
            "displayName": t.string().optional(),
            "adServerConfig": t.proxy(renames["PartnerAdServerConfigOut"]).optional(),
            "generalConfig": t.proxy(renames["PartnerGeneralConfigOut"]).optional(),
            "entityStatus": t.string().optional(),
            "dataAccessConfig": t.proxy(
                renames["PartnerDataAccessConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerOut"])
    types["ListCustomBiddingAlgorithmsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customBiddingAlgorithms": t.array(
                t.proxy(renames["CustomBiddingAlgorithmIn"])
            ).optional(),
        }
    ).named(renames["ListCustomBiddingAlgorithmsResponseIn"])
    types["ListCustomBiddingAlgorithmsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customBiddingAlgorithms": t.array(
                t.proxy(renames["CustomBiddingAlgorithmOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomBiddingAlgorithmsResponseOut"])
    types["IdFilterIn"] = t.struct(
        {
            "mediaProductIds": t.array(t.string()).optional(),
            "adGroupAdIds": t.array(t.string()).optional(),
            "campaignIds": t.array(t.string()).optional(),
            "adGroupIds": t.array(t.string()).optional(),
            "lineItemIds": t.array(t.string()).optional(),
            "insertionOrderIds": t.array(t.string()).optional(),
        }
    ).named(renames["IdFilterIn"])
    types["IdFilterOut"] = t.struct(
        {
            "mediaProductIds": t.array(t.string()).optional(),
            "adGroupAdIds": t.array(t.string()).optional(),
            "campaignIds": t.array(t.string()).optional(),
            "adGroupIds": t.array(t.string()).optional(),
            "lineItemIds": t.array(t.string()).optional(),
            "insertionOrderIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdFilterOut"])
    types["TargetingOptionIn"] = t.struct(
        {
            "subExchangeDetails": t.proxy(
                renames["SubExchangeTargetingOptionDetailsIn"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusTargetingOptionDetailsIn"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspTargetingOptionDetailsIn"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusTargetingOptionDetailsIn"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryTargetingOptionDetailsIn"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentTargetingOptionDetailsIn"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryTargetingOptionDetailsIn"]
            ).optional(),
            "digitalContentLabelDetails": t.proxy(
                renames["DigitalContentLabelTargetingOptionDetailsIn"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelTargetingOptionDetailsIn"]
            ).optional(),
            "poiDetails": t.proxy(renames["PoiTargetingOptionDetailsIn"]).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreTargetingOptionDetailsIn"]
            ).optional(),
            "sensitiveCategoryDetails": t.proxy(
                renames["SensitiveCategoryTargetingOptionDetailsIn"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeTargetingOptionDetailsIn"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemTargetingOptionDetailsIn"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeTargetingOptionDetailsIn"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeTargetingOptionDetailsIn"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionTargetingOptionDetailsIn"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainTargetingOptionDetailsIn"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeTargetingOptionDetailsIn"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageTargetingOptionDetailsIn"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionTargetingOptionDetailsIn"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentTargetingOptionDetailsIn"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionTargetingOptionDetailsIn"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeTargetingOptionDetailsIn"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionTargetingOptionDetailsIn"]
            ).optional(),
            "omidDetails": t.proxy(renames["OmidTargetingOptionDetailsIn"]).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityTargetingOptionDetailsIn"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionTargetingOptionDetailsIn"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserTargetingOptionDetailsIn"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationTargetingOptionDetailsIn"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderTargetingOptionDetailsIn"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeTargetingOptionDetailsIn"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeTargetingOptionDetailsIn"]
            ).optional(),
        }
    ).named(renames["TargetingOptionIn"])
    types["TargetingOptionOut"] = t.struct(
        {
            "subExchangeDetails": t.proxy(
                renames["SubExchangeTargetingOptionDetailsOut"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusTargetingOptionDetailsOut"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspTargetingOptionDetailsOut"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusTargetingOptionDetailsOut"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryTargetingOptionDetailsOut"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentTargetingOptionDetailsOut"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryTargetingOptionDetailsOut"]
            ).optional(),
            "digitalContentLabelDetails": t.proxy(
                renames["DigitalContentLabelTargetingOptionDetailsOut"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelTargetingOptionDetailsOut"]
            ).optional(),
            "poiDetails": t.proxy(renames["PoiTargetingOptionDetailsOut"]).optional(),
            "targetingType": t.string().optional(),
            "name": t.string().optional(),
            "targetingOptionId": t.string().optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreTargetingOptionDetailsOut"]
            ).optional(),
            "sensitiveCategoryDetails": t.proxy(
                renames["SensitiveCategoryTargetingOptionDetailsOut"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeTargetingOptionDetailsOut"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemTargetingOptionDetailsOut"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeTargetingOptionDetailsOut"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeTargetingOptionDetailsOut"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionTargetingOptionDetailsOut"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainTargetingOptionDetailsOut"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeTargetingOptionDetailsOut"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageTargetingOptionDetailsOut"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionTargetingOptionDetailsOut"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentTargetingOptionDetailsOut"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionTargetingOptionDetailsOut"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeTargetingOptionDetailsOut"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionTargetingOptionDetailsOut"]
            ).optional(),
            "omidDetails": t.proxy(renames["OmidTargetingOptionDetailsOut"]).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityTargetingOptionDetailsOut"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionTargetingOptionDetailsOut"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserTargetingOptionDetailsOut"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationTargetingOptionDetailsOut"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderTargetingOptionDetailsOut"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeTargetingOptionDetailsOut"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeTargetingOptionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingOptionOut"])
    types["ListAssignedInventorySourcesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceIn"])
            ).optional(),
        }
    ).named(renames["ListAssignedInventorySourcesResponseIn"])
    types["ListAssignedInventorySourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssignedInventorySourcesResponseOut"])
    types["DimensionsIn"] = t.struct(
        {"widthPixels": t.integer().optional(), "heightPixels": t.integer().optional()}
    ).named(renames["DimensionsIn"])
    types["DimensionsOut"] = t.struct(
        {
            "widthPixels": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionsOut"])
    types["AssignedLocationIn"] = t.struct({"targetingOptionId": t.string()}).named(
        renames["AssignedLocationIn"]
    )
    types["AssignedLocationOut"] = t.struct(
        {
            "assignedLocationId": t.string().optional(),
            "name": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedLocationOut"])
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
    types["EditGuaranteedOrderReadAccessorsRequestIn"] = t.struct(
        {
            "addedAdvertisers": t.array(t.string()).optional(),
            "removedAdvertisers": t.array(t.string()).optional(),
            "partnerId": t.string(),
            "readAccessInherited": t.boolean().optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsRequestIn"])
    types["EditGuaranteedOrderReadAccessorsRequestOut"] = t.struct(
        {
            "addedAdvertisers": t.array(t.string()).optional(),
            "removedAdvertisers": t.array(t.string()).optional(),
            "partnerId": t.string(),
            "readAccessInherited": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsRequestOut"])
    types["InvoiceIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "invoiceId": t.string().optional(),
            "serviceDateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "totalAmountMicros": t.string().optional(),
            "dueDate": t.proxy(renames["DateIn"]).optional(),
            "budgetSummaries": t.array(t.proxy(renames["BudgetSummaryIn"])).optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "issueDate": t.proxy(renames["DateIn"]).optional(),
            "correctedInvoiceId": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "paymentsProfileId": t.string().optional(),
            "purchaseOrderNumber": t.string().optional(),
            "subtotalAmountMicros": t.string().optional(),
            "displayName": t.string().optional(),
            "invoiceType": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "name": t.string().optional(),
            "budgetInvoiceGroupingId": t.string().optional(),
            "nonBudgetMicros": t.string().optional(),
        }
    ).named(renames["InvoiceIn"])
    types["InvoiceOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "invoiceId": t.string().optional(),
            "serviceDateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "totalAmountMicros": t.string().optional(),
            "dueDate": t.proxy(renames["DateOut"]).optional(),
            "budgetSummaries": t.array(t.proxy(renames["BudgetSummaryOut"])).optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "issueDate": t.proxy(renames["DateOut"]).optional(),
            "correctedInvoiceId": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "paymentsProfileId": t.string().optional(),
            "purchaseOrderNumber": t.string().optional(),
            "subtotalAmountMicros": t.string().optional(),
            "displayName": t.string().optional(),
            "invoiceType": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "name": t.string().optional(),
            "budgetInvoiceGroupingId": t.string().optional(),
            "nonBudgetMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceOut"])
    types["ActivateManualTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivateManualTriggerRequestIn"])
    types["ActivateManualTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateManualTriggerRequestOut"])
    types["HouseholdIncomeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["HouseholdIncomeTargetingOptionDetailsIn"])
    types["HouseholdIncomeTargetingOptionDetailsOut"] = t.struct(
        {
            "householdIncome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HouseholdIncomeTargetingOptionDetailsOut"])
    types["DoubleVerifyBrandSafetyCategoriesIn"] = t.struct(
        {
            "avoidedMediumSeverityCategories": t.array(t.string()).optional(),
            "avoidUnknownBrandSafetyCategory": t.boolean().optional(),
            "avoidedHighSeverityCategories": t.array(t.string()).optional(),
        }
    ).named(renames["DoubleVerifyBrandSafetyCategoriesIn"])
    types["DoubleVerifyBrandSafetyCategoriesOut"] = t.struct(
        {
            "avoidedMediumSeverityCategories": t.array(t.string()).optional(),
            "avoidUnknownBrandSafetyCategory": t.boolean().optional(),
            "avoidedHighSeverityCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyBrandSafetyCategoriesOut"])
    types["BiddingStrategyIn"] = t.struct(
        {
            "performanceGoalAutoBid": t.proxy(
                renames["PerformanceGoalBidStrategyIn"]
            ).optional(),
            "fixedBid": t.proxy(renames["FixedBidStrategyIn"]).optional(),
            "maximizeSpendAutoBid": t.proxy(
                renames["MaximizeSpendBidStrategyIn"]
            ).optional(),
        }
    ).named(renames["BiddingStrategyIn"])
    types["BiddingStrategyOut"] = t.struct(
        {
            "performanceGoalAutoBid": t.proxy(
                renames["PerformanceGoalBidStrategyOut"]
            ).optional(),
            "fixedBid": t.proxy(renames["FixedBidStrategyOut"]).optional(),
            "maximizeSpendAutoBid": t.proxy(
                renames["MaximizeSpendBidStrategyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiddingStrategyOut"])
    types["AudioContentTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AudioContentTypeTargetingOptionDetailsIn"])
    types["AudioContentTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "audioContentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioContentTypeTargetingOptionDetailsOut"])
    types["MobileDeviceIdListIn"] = t.struct(
        {"mobileDeviceIds": t.array(t.string()).optional()}
    ).named(renames["MobileDeviceIdListIn"])
    types["MobileDeviceIdListOut"] = t.struct(
        {
            "mobileDeviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileDeviceIdListOut"])
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
    types["AdvertiserCreativeConfigIn"] = t.struct(
        {
            "dynamicCreativeEnabled": t.boolean().optional(),
            "obaComplianceDisabled": t.boolean().optional(),
            "iasClientId": t.string().optional(),
            "videoCreativeDataSharingAuthorized": t.boolean().optional(),
        }
    ).named(renames["AdvertiserCreativeConfigIn"])
    types["AdvertiserCreativeConfigOut"] = t.struct(
        {
            "dynamicCreativeEnabled": t.boolean().optional(),
            "obaComplianceDisabled": t.boolean().optional(),
            "iasClientId": t.string().optional(),
            "videoCreativeDataSharingAuthorized": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserCreativeConfigOut"])
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
    types["FirstAndThirdPartyAudienceTargetingSettingIn"] = t.struct(
        {"recency": t.string().optional(), "firstAndThirdPartyAudienceId": t.string()}
    ).named(renames["FirstAndThirdPartyAudienceTargetingSettingIn"])
    types["FirstAndThirdPartyAudienceTargetingSettingOut"] = t.struct(
        {
            "recency": t.string().optional(),
            "firstAndThirdPartyAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceTargetingSettingOut"])
    types["ListChannelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
        }
    ).named(renames["ListChannelsResponseIn"])
    types["ListChannelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChannelsResponseOut"])
    types["CreativeIn"] = t.struct(
        {
            "requireHtml5": t.boolean().optional(),
            "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
            "notes": t.string().optional(),
            "requireMraid": t.boolean().optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
            "entityStatus": t.string(),
            "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
            "creativeType": t.string(),
            "appendedTag": t.string().optional(),
            "skippable": t.boolean().optional(),
            "trackerUrls": t.array(t.string()).optional(),
            "iasCampaignMonitoring": t.boolean().optional(),
            "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
            "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
            "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
            "jsTrackerUrl": t.string().optional(),
            "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
            "requirePingForAttribution": t.boolean().optional(),
            "additionalDimensions": t.array(
                t.proxy(renames["DimensionsIn"])
            ).optional(),
            "thirdPartyUrls": t.array(t.proxy(renames["ThirdPartyUrlIn"])).optional(),
            "hostingSource": t.string(),
            "vastTagUrl": t.string().optional(),
            "integrationCode": t.string().optional(),
            "displayName": t.string(),
            "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
            "companionCreativeIds": t.array(t.string()).optional(),
            "expandOnHover": t.boolean().optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]),
            "expandingDirection": t.string().optional(),
            "thirdPartyTag": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "requireHtml5": t.boolean().optional(),
            "transcodes": t.array(t.proxy(renames["TranscodeOut"])).optional(),
            "lineItemIds": t.array(t.string()).optional(),
            "skipOffset": t.proxy(renames["AudioVideoOffsetOut"]).optional(),
            "dynamic": t.boolean().optional(),
            "reviewStatus": t.proxy(renames["ReviewStatusInfoOut"]).optional(),
            "notes": t.string().optional(),
            "requireMraid": t.boolean().optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdOut"]).optional(),
            "createTime": t.string().optional(),
            "html5Video": t.boolean().optional(),
            "entityStatus": t.string(),
            "counterEvents": t.array(t.proxy(renames["CounterEventOut"])).optional(),
            "creativeType": t.string(),
            "appendedTag": t.string().optional(),
            "oggAudio": t.boolean().optional(),
            "skippable": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "vpaid": t.boolean().optional(),
            "name": t.string().optional(),
            "trackerUrls": t.array(t.string()).optional(),
            "iasCampaignMonitoring": t.boolean().optional(),
            "advertiserId": t.string().optional(),
            "cmPlacementId": t.string().optional(),
            "mp3Audio": t.boolean().optional(),
            "progressOffset": t.proxy(renames["AudioVideoOffsetOut"]).optional(),
            "cmTrackingAd": t.proxy(renames["CmTrackingAdOut"]).optional(),
            "timerEvents": t.array(t.proxy(renames["TimerEventOut"])).optional(),
            "jsTrackerUrl": t.string().optional(),
            "obaIcon": t.proxy(renames["ObaIconOut"]).optional(),
            "requirePingForAttribution": t.boolean().optional(),
            "creativeAttributes": t.array(t.string()).optional(),
            "additionalDimensions": t.array(
                t.proxy(renames["DimensionsOut"])
            ).optional(),
            "thirdPartyUrls": t.array(t.proxy(renames["ThirdPartyUrlOut"])).optional(),
            "hostingSource": t.string(),
            "vastTagUrl": t.string().optional(),
            "mediaDuration": t.string().optional(),
            "integrationCode": t.string().optional(),
            "displayName": t.string(),
            "exitEvents": t.array(t.proxy(renames["ExitEventOut"])),
            "creativeId": t.string().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "expandOnHover": t.boolean().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]),
            "expandingDirection": t.string().optional(),
            "thirdPartyTag": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetAssociationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["AuthorizedSellerStatusTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizedSellerStatusTargetingOptionDetailsIn"])
    types["AuthorizedSellerStatusTargetingOptionDetailsOut"] = t.struct(
        {
            "authorizedSellerStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedSellerStatusTargetingOptionDetailsOut"])
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
    types["EnvironmentTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EnvironmentTargetingOptionDetailsIn"])
    types["EnvironmentTargetingOptionDetailsOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentTargetingOptionDetailsOut"])
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
    types["YoutubeAdGroupIn"] = t.struct(
        {
            "adGroupFormat": t.string().optional(),
            "name": t.string().optional(),
            "youtubeAdIds": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
            "displayName": t.string().optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigIn"]
            ).optional(),
            "entityStatus": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyIn"]
            ).optional(),
            "adGroupId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "productFeedData": t.proxy(renames["ProductFeedDataIn"]).optional(),
        }
    ).named(renames["YoutubeAdGroupIn"])
    types["YoutubeAdGroupOut"] = t.struct(
        {
            "adGroupFormat": t.string().optional(),
            "name": t.string().optional(),
            "youtubeAdIds": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
            "displayName": t.string().optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigOut"]
            ).optional(),
            "entityStatus": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyOut"]
            ).optional(),
            "adGroupId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "productFeedData": t.proxy(renames["ProductFeedDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupOut"])
    types["DeleteAssignedTargetingOptionsRequestIn"] = t.struct(
        {"targetingType": t.string(), "assignedTargetingOptionIds": t.array(t.string())}
    ).named(renames["DeleteAssignedTargetingOptionsRequestIn"])
    types["DeleteAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "targetingType": t.string(),
            "assignedTargetingOptionIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteAssignedTargetingOptionsRequestOut"])
    types["LanguageTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["LanguageTargetingOptionDetailsIn"])
    types["LanguageTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageTargetingOptionDetailsOut"])
    types["InventorySourceGroupAssignedTargetingOptionDetailsIn"] = t.struct(
        {"inventorySourceGroupId": t.string()}
    ).named(renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"])
    types["InventorySourceGroupAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "inventorySourceGroupId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceGroupAssignedTargetingOptionDetailsOut"])
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
            "negativelyTargetedChannelsCount": t.string().optional(),
            "negativeKeywordListsCount": t.string().optional(),
            "channelsCount": t.string().optional(),
            "adGroupCriteriaCount": t.string().optional(),
            "usedLineItemsCount": t.string().optional(),
            "campaignCriteriaCount": t.string().optional(),
            "usedInsertionOrdersCount": t.string().optional(),
            "usedCampaignsCount": t.string().optional(),
        }
    ).named(renames["AuditAdvertiserResponseIn"])
    types["AuditAdvertiserResponseOut"] = t.struct(
        {
            "negativelyTargetedChannelsCount": t.string().optional(),
            "negativeKeywordListsCount": t.string().optional(),
            "channelsCount": t.string().optional(),
            "adGroupCriteriaCount": t.string().optional(),
            "usedLineItemsCount": t.string().optional(),
            "campaignCriteriaCount": t.string().optional(),
            "usedInsertionOrdersCount": t.string().optional(),
            "usedCampaignsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditAdvertiserResponseOut"])
    types["SiteIn"] = t.struct({"urlOrAppId": t.string()}).named(renames["SiteIn"])
    types["SiteOut"] = t.struct(
        {
            "name": t.string().optional(),
            "urlOrAppId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteOut"])
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
    types["AgeRangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"ageRange": t.string().optional()}
    ).named(renames["AgeRangeAssignedTargetingOptionDetailsIn"])
    types["AgeRangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeAssignedTargetingOptionDetailsOut"])
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
    types["LineItemFlightIn"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "flightDateType": t.string(),
        }
    ).named(renames["LineItemFlightIn"])
    types["LineItemFlightOut"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "flightDateType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemFlightOut"])
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
    types["BulkEditAssignedTargetingOptionsResponseIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["BulkEditAssignedTargetingOptionsResponseIn"])
    types["BulkEditAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "updatedLineItemIds": t.array(t.string()).optional(),
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsResponseOut"])
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
    types["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"] = t.struct(
        {
            "brandSafetyVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "brandLiftVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "viewabilityVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "reachVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
        }
    ).named(renames["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"])
    types["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"] = t.struct(
        {
            "brandSafetyVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "brandLiftVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "viewabilityVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "reachVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"])
    types["ImageAssetIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "fullSize": t.proxy(renames["DimensionsIn"]).optional(),
            "fileSize": t.string().optional(),
        }
    ).named(renames["ImageAssetIn"])
    types["ImageAssetOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "fullSize": t.proxy(renames["DimensionsOut"]).optional(),
            "fileSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageAssetOut"])
    types["FirstAndThirdPartyAudienceIn"] = t.struct(
        {
            "appId": t.string().optional(),
            "firstAndThirdPartyAudienceType": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "membershipDurationDays": t.string().optional(),
            "audienceType": t.string().optional(),
            "mobileDeviceIdList": t.proxy(renames["MobileDeviceIdListIn"]).optional(),
            "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceIn"])
    types["FirstAndThirdPartyAudienceOut"] = t.struct(
        {
            "appId": t.string().optional(),
            "displayMobileAppAudienceSize": t.string().optional(),
            "youtubeAudienceSize": t.string().optional(),
            "firstAndThirdPartyAudienceType": t.string().optional(),
            "displayName": t.string().optional(),
            "activeDisplayAudienceSize": t.string().optional(),
            "description": t.string().optional(),
            "membershipDurationDays": t.string().optional(),
            "audienceType": t.string().optional(),
            "audienceSource": t.string().optional(),
            "displayAudienceSize": t.string().optional(),
            "displayMobileWebAudienceSize": t.string().optional(),
            "displayDesktopAudienceSize": t.string().optional(),
            "gmailAudienceSize": t.string().optional(),
            "firstAndThirdPartyAudienceId": t.string().optional(),
            "name": t.string().optional(),
            "mobileDeviceIdList": t.proxy(renames["MobileDeviceIdListOut"]).optional(),
            "contactInfoList": t.proxy(renames["ContactInfoListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceOut"])
    types["DigitalContentLabelTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DigitalContentLabelTargetingOptionDetailsIn"])
    types["DigitalContentLabelTargetingOptionDetailsOut"] = t.struct(
        {
            "contentRatingTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigitalContentLabelTargetingOptionDetailsOut"])
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
    types["AdvertiserDataAccessConfigIn"] = t.struct(
        {"sdfConfig": t.proxy(renames["AdvertiserSdfConfigIn"]).optional()}
    ).named(renames["AdvertiserDataAccessConfigIn"])
    types["AdvertiserDataAccessConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["AdvertiserSdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserDataAccessConfigOut"])
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
    types["EnvironmentAssignedTargetingOptionDetailsIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["EnvironmentAssignedTargetingOptionDetailsIn"])
    types["EnvironmentAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentAssignedTargetingOptionDetailsOut"])
    types["MastheadAdIn"] = t.struct(
        {
            "autoplayVideoDuration": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "videoAspectRatio": t.string().optional(),
            "callToActionTrackingUrl": t.string().optional(),
            "headline": t.string().optional(),
            "callToActionButtonLabel": t.string().optional(),
            "description": t.string().optional(),
            "companionYoutubeVideos": t.array(
                t.proxy(renames["YoutubeVideoDetailsIn"])
            ).optional(),
            "autoplayVideoStartMillisecond": t.string().optional(),
            "showChannelArt": t.boolean().optional(),
            "callToActionFinalUrl": t.string().optional(),
        }
    ).named(renames["MastheadAdIn"])
    types["MastheadAdOut"] = t.struct(
        {
            "autoplayVideoDuration": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "videoAspectRatio": t.string().optional(),
            "callToActionTrackingUrl": t.string().optional(),
            "headline": t.string().optional(),
            "callToActionButtonLabel": t.string().optional(),
            "description": t.string().optional(),
            "companionYoutubeVideos": t.array(
                t.proxy(renames["YoutubeVideoDetailsOut"])
            ).optional(),
            "autoplayVideoStartMillisecond": t.string().optional(),
            "showChannelArt": t.boolean().optional(),
            "callToActionFinalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MastheadAdOut"])
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
    types["ScriptErrorIn"] = t.struct(
        {
            "errorCode": t.string().optional(),
            "line": t.string().optional(),
            "errorMessage": t.string().optional(),
            "column": t.string().optional(),
        }
    ).named(renames["ScriptErrorIn"])
    types["ScriptErrorOut"] = t.struct(
        {
            "errorCode": t.string().optional(),
            "line": t.string().optional(),
            "errorMessage": t.string().optional(),
            "column": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptErrorOut"])
    types["ContactInfoListIn"] = t.struct(
        {"contactInfos": t.array(t.proxy(renames["ContactInfoIn"])).optional()}
    ).named(renames["ContactInfoListIn"])
    types["ContactInfoListOut"] = t.struct(
        {
            "contactInfos": t.array(t.proxy(renames["ContactInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoListOut"])
    types["ContentGenreTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentGenreTargetingOptionDetailsIn"])
    types["ContentGenreTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentGenreTargetingOptionDetailsOut"])
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
    types["SdfDownloadTaskMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "version": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["SdfDownloadTaskMetadataIn"])
    types["SdfDownloadTaskMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "version": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfDownloadTaskMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["ViewabilityTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ViewabilityTargetingOptionDetailsIn"])
    types["ViewabilityTargetingOptionDetailsOut"] = t.struct(
        {
            "viewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewabilityTargetingOptionDetailsOut"])
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
    types["BusinessChainTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["BusinessChainTargetingOptionDetailsIn"])
    types["BusinessChainTargetingOptionDetailsOut"] = t.struct(
        {
            "businessChain": t.string().optional(),
            "geoRegionType": t.string().optional(),
            "geoRegion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessChainTargetingOptionDetailsOut"])
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
    types["LineItemBudgetIn"] = t.struct(
        {"budgetAllocationType": t.string(), "maxAmount": t.string().optional()}
    ).named(renames["LineItemBudgetIn"])
    types["LineItemBudgetOut"] = t.struct(
        {
            "budgetUnit": t.string().optional(),
            "budgetAllocationType": t.string(),
            "maxAmount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemBudgetOut"])
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
    types["BulkUpdateLineItemsResponseIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "updatedLineItemIds": t.array(t.string()).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
            "skippedLineItemIds": t.array(t.string()).optional(),
        }
    ).named(renames["BulkUpdateLineItemsResponseIn"])
    types["BulkUpdateLineItemsResponseOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "updatedLineItemIds": t.array(t.string()).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
            "skippedLineItemIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkUpdateLineItemsResponseOut"])
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
    types["SensitiveCategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SensitiveCategoryTargetingOptionDetailsIn"])
    types["SensitiveCategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "sensitiveCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveCategoryTargetingOptionDetailsOut"])
    types["AppAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "appPlatform": t.string().optional(),
            "negative": t.boolean().optional(),
            "appId": t.string(),
        }
    ).named(renames["AppAssignedTargetingOptionDetailsIn"])
    types["AppAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "appPlatform": t.string().optional(),
            "negative": t.boolean().optional(),
            "appId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppAssignedTargetingOptionDetailsOut"])
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
    types["CreateAssetRequestIn"] = t.struct({"filename": t.string()}).named(
        renames["CreateAssetRequestIn"]
    )
    types["CreateAssetRequestOut"] = t.struct(
        {"filename": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateAssetRequestOut"])
    types["DuplicateLineItemResponseIn"] = t.struct(
        {"duplicateLineItemId": t.string().optional()}
    ).named(renames["DuplicateLineItemResponseIn"])
    types["DuplicateLineItemResponseOut"] = t.struct(
        {
            "duplicateLineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateLineItemResponseOut"])
    types["YoutubeAndPartnersInventorySourceConfigIn"] = t.struct(
        {
            "includeYoutubeVideos": t.boolean().optional(),
            "includeYoutubeSearch": t.boolean().optional(),
            "includeYoutubeVideoPartners": t.boolean().optional(),
        }
    ).named(renames["YoutubeAndPartnersInventorySourceConfigIn"])
    types["YoutubeAndPartnersInventorySourceConfigOut"] = t.struct(
        {
            "includeYoutubeVideos": t.boolean().optional(),
            "includeYoutubeSearch": t.boolean().optional(),
            "includeYoutubeVideoPartners": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersInventorySourceConfigOut"])
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
    types["CmHybridConfigIn"] = t.struct(
        {
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "cmFloodlightLinkingAuthorized": t.boolean(),
            "cmFloodlightConfigId": t.string(),
            "cmAccountId": t.string(),
            "cmSyncableSiteIds": t.array(t.string()).optional(),
        }
    ).named(renames["CmHybridConfigIn"])
    types["CmHybridConfigOut"] = t.struct(
        {
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "cmFloodlightLinkingAuthorized": t.boolean(),
            "cmFloodlightConfigId": t.string(),
            "cmAccountId": t.string(),
            "cmSyncableSiteIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmHybridConfigOut"])
    types["DeactivateManualTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateManualTriggerRequestIn"])
    types["DeactivateManualTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateManualTriggerRequestOut"])
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
    types["CustomBiddingModelDetailsIn"] = t.struct(
        {"readinessState": t.string().optional(), "advertiserId": t.string().optional()}
    ).named(renames["CustomBiddingModelDetailsIn"])
    types["CustomBiddingModelDetailsOut"] = t.struct(
        {
            "readinessState": t.string().optional(),
            "suspensionState": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingModelDetailsOut"])
    types["PartnerCostIn"] = t.struct(
        {
            "invoiceType": t.string().optional(),
            "feePercentageMillis": t.string().optional(),
            "feeAmount": t.string().optional(),
            "costType": t.string(),
            "feeType": t.string(),
        }
    ).named(renames["PartnerCostIn"])
    types["PartnerCostOut"] = t.struct(
        {
            "invoiceType": t.string().optional(),
            "feePercentageMillis": t.string().optional(),
            "feeAmount": t.string().optional(),
            "costType": t.string(),
            "feeType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerCostOut"])
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
    types["PrismaConfigIn"] = t.struct(
        {
            "supplier": t.string(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeIn"]),
            "prismaType": t.string(),
        }
    ).named(renames["PrismaConfigIn"])
    types["PrismaConfigOut"] = t.struct(
        {
            "supplier": t.string(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeOut"]),
            "prismaType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrismaConfigOut"])
    types["PoiAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "proximityRadiusUnit": t.string(),
            "targetingOptionId": t.string(),
            "proximityRadiusAmount": t.number(),
        }
    ).named(renames["PoiAssignedTargetingOptionDetailsIn"])
    types["PoiAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "proximityRadiusUnit": t.string(),
            "longitude": t.number().optional(),
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "latitude": t.number().optional(),
            "proximityRadiusAmount": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiAssignedTargetingOptionDetailsOut"])
    types["CustomBiddingScriptIn"] = t.struct(
        {"script": t.proxy(renames["CustomBiddingScriptRefIn"]).optional()}
    ).named(renames["CustomBiddingScriptIn"])
    types["CustomBiddingScriptOut"] = t.struct(
        {
            "customBiddingScriptId": t.string().optional(),
            "active": t.boolean().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "name": t.string().optional(),
            "script": t.proxy(renames["CustomBiddingScriptRefOut"]).optional(),
            "errors": t.array(t.proxy(renames["ScriptErrorOut"])).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingScriptOut"])
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
    types["PerformanceGoalIn"] = t.struct(
        {
            "performanceGoalPercentageMicros": t.string().optional(),
            "performanceGoalString": t.string().optional(),
            "performanceGoalAmountMicros": t.string().optional(),
            "performanceGoalType": t.string(),
        }
    ).named(renames["PerformanceGoalIn"])
    types["PerformanceGoalOut"] = t.struct(
        {
            "performanceGoalPercentageMicros": t.string().optional(),
            "performanceGoalString": t.string().optional(),
            "performanceGoalAmountMicros": t.string().optional(),
            "performanceGoalType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceGoalOut"])
    types["VideoAdSequenceStepIn"] = t.struct(
        {
            "previousStepId": t.string().optional(),
            "stepId": t.string().optional(),
            "interactionType": t.string().optional(),
            "adGroupId": t.string().optional(),
        }
    ).named(renames["VideoAdSequenceStepIn"])
    types["VideoAdSequenceStepOut"] = t.struct(
        {
            "previousStepId": t.string().optional(),
            "stepId": t.string().optional(),
            "interactionType": t.string().optional(),
            "adGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAdSequenceStepOut"])
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
    types["BulkEditPartnerAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
            ).optional(),
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
            ).optional(),
        }
    ).named(renames["BulkEditPartnerAssignedTargetingOptionsRequestIn"])
    types["BulkEditPartnerAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditPartnerAssignedTargetingOptionsRequestOut"])
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
    types["InventorySourceIn"] = t.struct(
        {
            "readWriteAccessors": t.proxy(
                renames["InventorySourceAccessorsIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "subSitePropertyId": t.string().optional(),
            "publisherName": t.string().optional(),
            "guaranteedOrderId": t.string().optional(),
            "commitment": t.string().optional(),
            "inventorySourceType": t.string().optional(),
            "dealId": t.string().optional(),
            "status": t.proxy(renames["InventorySourceStatusIn"]).optional(),
            "deliveryMethod": t.string().optional(),
            "rateDetails": t.proxy(renames["RateDetailsIn"]),
            "creativeConfigs": t.array(t.proxy(renames["CreativeConfigIn"])).optional(),
            "exchange": t.string().optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
        }
    ).named(renames["InventorySourceIn"])
    types["InventorySourceOut"] = t.struct(
        {
            "readWriteAccessors": t.proxy(
                renames["InventorySourceAccessorsOut"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "inventorySourceProductType": t.string().optional(),
            "subSitePropertyId": t.string().optional(),
            "publisherName": t.string().optional(),
            "readPartnerIds": t.array(t.string()).optional(),
            "guaranteedOrderId": t.string().optional(),
            "commitment": t.string().optional(),
            "inventorySourceType": t.string().optional(),
            "dealId": t.string().optional(),
            "status": t.proxy(renames["InventorySourceStatusOut"]).optional(),
            "deliveryMethod": t.string().optional(),
            "rateDetails": t.proxy(renames["RateDetailsOut"]),
            "updateTime": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "inventorySourceId": t.string().optional(),
            "creativeConfigs": t.array(
                t.proxy(renames["CreativeConfigOut"])
            ).optional(),
            "exchange": t.string().optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceOut"])
    types["AudioContentTypeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"audioContentType": t.string().optional()}
    ).named(renames["AudioContentTypeAssignedTargetingOptionDetailsIn"])
    types["AudioContentTypeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "audioContentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioContentTypeAssignedTargetingOptionDetailsOut"])
    types["SubExchangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SubExchangeTargetingOptionDetailsIn"])
    types["SubExchangeTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubExchangeTargetingOptionDetailsOut"])
    types["FloodlightGroupIn"] = t.struct(
        {
            "lookbackWindow": t.proxy(renames["LookbackWindowIn"]),
            "webTagType": t.string(),
            "activeViewConfig": t.proxy(
                renames["ActiveViewVideoViewabilityMetricConfigIn"]
            ).optional(),
            "customVariables": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string(),
        }
    ).named(renames["FloodlightGroupIn"])
    types["FloodlightGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "lookbackWindow": t.proxy(renames["LookbackWindowOut"]),
            "webTagType": t.string(),
            "floodlightGroupId": t.string().optional(),
            "activeViewConfig": t.proxy(
                renames["ActiveViewVideoViewabilityMetricConfigOut"]
            ).optional(),
            "customVariables": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightGroupOut"])
    types["AssignedTargetingOptionIn"] = t.struct(
        {
            "youtubeVideoDetails": t.proxy(
                renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "urlDetails": t.proxy(
                renames["UrlAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "appDetails": t.proxy(
                renames["AppAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "inventorySourceDetails": t.proxy(
                renames["InventorySourceAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "youtubeChannelDetails": t.proxy(
                renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "proximityLocationListDetails": t.proxy(
                renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "sensitiveCategoryExclusionDetails": t.proxy(
                renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "regionalLocationListDetails": t.proxy(
                renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "keywordDetails": t.proxy(
                renames["KeywordAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "channelDetails": t.proxy(
                renames["ChannelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "omidDetails": t.proxy(
                renames["OmidAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "sessionPositionDetails": t.proxy(
                renames["SessionPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "thirdPartyVerifierDetails": t.proxy(
                renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "poiDetails": t.proxy(
                renames["PoiAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "negativeKeywordListDetails": t.proxy(
                renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "digitalContentLabelExclusionDetails": t.proxy(
                renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "inventorySourceGroupDetails": t.proxy(
                renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "audienceGroupDetails": t.proxy(
                renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "dayAndTimeDetails": t.proxy(
                renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
            ).optional(),
        }
    ).named(renames["AssignedTargetingOptionIn"])
    types["AssignedTargetingOptionOut"] = t.struct(
        {
            "youtubeVideoDetails": t.proxy(
                renames["YoutubeVideoAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "urlDetails": t.proxy(
                renames["UrlAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "appDetails": t.proxy(
                renames["AppAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inventorySourceDetails": t.proxy(
                renames["InventorySourceAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "assignedTargetingOptionIdAlias": t.string().optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "youtubeChannelDetails": t.proxy(
                renames["YoutubeChannelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "proximityLocationListDetails": t.proxy(
                renames["ProximityLocationListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "sensitiveCategoryExclusionDetails": t.proxy(
                renames["SensitiveCategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "regionalLocationListDetails": t.proxy(
                renames["RegionalLocationListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "keywordDetails": t.proxy(
                renames["KeywordAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "channelDetails": t.proxy(
                renames["ChannelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "omidDetails": t.proxy(
                renames["OmidAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "sessionPositionDetails": t.proxy(
                renames["SessionPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "thirdPartyVerifierDetails": t.proxy(
                renames["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "poiDetails": t.proxy(
                renames["PoiAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inheritance": t.string().optional(),
            "targetingType": t.string().optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "negativeKeywordListDetails": t.proxy(
                renames["NegativeKeywordListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "digitalContentLabelExclusionDetails": t.proxy(
                renames["DigitalContentLabelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "assignedTargetingOptionId": t.string().optional(),
            "inventorySourceGroupDetails": t.proxy(
                renames["InventorySourceGroupAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "audienceGroupDetails": t.proxy(
                renames["AudienceGroupAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "dayAndTimeDetails": t.proxy(
                renames["DayAndTimeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedTargetingOptionOut"])
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
    types["DoubleVerifyVideoViewabilityIn"] = t.struct(
        {
            "playerImpressionRate": t.string().optional(),
            "videoIab": t.string().optional(),
            "videoViewableRate": t.string().optional(),
        }
    ).named(renames["DoubleVerifyVideoViewabilityIn"])
    types["DoubleVerifyVideoViewabilityOut"] = t.struct(
        {
            "playerImpressionRate": t.string().optional(),
            "videoIab": t.string().optional(),
            "videoViewableRate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyVideoViewabilityOut"])
    types["DoubleVerifyIn"] = t.struct(
        {
            "brandSafetyCategories": t.proxy(
                renames["DoubleVerifyBrandSafetyCategoriesIn"]
            ).optional(),
            "fraudInvalidTraffic": t.proxy(
                renames["DoubleVerifyFraudInvalidTrafficIn"]
            ).optional(),
            "videoViewability": t.proxy(
                renames["DoubleVerifyVideoViewabilityIn"]
            ).optional(),
            "customSegmentId": t.string().optional(),
            "appStarRating": t.proxy(renames["DoubleVerifyAppStarRatingIn"]).optional(),
            "avoidedAgeRatings": t.array(t.string()).optional(),
            "displayViewability": t.proxy(
                renames["DoubleVerifyDisplayViewabilityIn"]
            ).optional(),
        }
    ).named(renames["DoubleVerifyIn"])
    types["DoubleVerifyOut"] = t.struct(
        {
            "brandSafetyCategories": t.proxy(
                renames["DoubleVerifyBrandSafetyCategoriesOut"]
            ).optional(),
            "fraudInvalidTraffic": t.proxy(
                renames["DoubleVerifyFraudInvalidTrafficOut"]
            ).optional(),
            "videoViewability": t.proxy(
                renames["DoubleVerifyVideoViewabilityOut"]
            ).optional(),
            "customSegmentId": t.string().optional(),
            "appStarRating": t.proxy(
                renames["DoubleVerifyAppStarRatingOut"]
            ).optional(),
            "avoidedAgeRatings": t.array(t.string()).optional(),
            "displayViewability": t.proxy(
                renames["DoubleVerifyDisplayViewabilityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyOut"])
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
    types["ExchangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"exchange": t.string()}
    ).named(renames["ExchangeAssignedTargetingOptionDetailsIn"])
    types["ExchangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {"exchange": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExchangeAssignedTargetingOptionDetailsOut"])
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
    types["BulkEditAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "lineItemIds": t.array(t.string()),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
            ).optional(),
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
            ).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsRequestIn"])
    types["BulkEditAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "lineItemIds": t.array(t.string()),
            "deleteRequests": t.array(
                t.proxy(renames["DeleteAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "createRequests": t.array(
                t.proxy(renames["CreateAssignedTargetingOptionsRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsRequestOut"])
    types["SdfDownloadTaskIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["SdfDownloadTaskIn"])
    types["SdfDownloadTaskOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfDownloadTaskOut"])
    types["LookupInvoiceCurrencyResponseIn"] = t.struct(
        {"currencyCode": t.string().optional()}
    ).named(renames["LookupInvoiceCurrencyResponseIn"])
    types["LookupInvoiceCurrencyResponseOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupInvoiceCurrencyResponseOut"])
    types["YoutubeAdGroupAdIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "adGroupAdId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "videoPerformanceAd": t.proxy(renames["VideoPerformanceAdIn"]).optional(),
            "displayVideoSourceAd": t.proxy(
                renames["DisplayVideoSourceAdIn"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "videoDiscoverAd": t.proxy(renames["VideoDiscoveryAdIn"]).optional(),
            "audioAd": t.proxy(renames["AudioAdIn"]).optional(),
            "name": t.string().optional(),
            "adUrls": t.array(t.proxy(renames["AdUrlIn"])).optional(),
            "nonSkippableAd": t.proxy(renames["NonSkippableAdIn"]).optional(),
            "inStreamAd": t.proxy(renames["InStreamAdIn"]).optional(),
            "mastheadAd": t.proxy(renames["MastheadAdIn"]).optional(),
            "entityStatus": t.string().optional(),
            "bumperAd": t.proxy(renames["BumperAdIn"]).optional(),
        }
    ).named(renames["YoutubeAdGroupAdIn"])
    types["YoutubeAdGroupAdOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "adGroupAdId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "videoPerformanceAd": t.proxy(renames["VideoPerformanceAdOut"]).optional(),
            "displayVideoSourceAd": t.proxy(
                renames["DisplayVideoSourceAdOut"]
            ).optional(),
            "advertiserId": t.string().optional(),
            "videoDiscoverAd": t.proxy(renames["VideoDiscoveryAdOut"]).optional(),
            "audioAd": t.proxy(renames["AudioAdOut"]).optional(),
            "name": t.string().optional(),
            "adUrls": t.array(t.proxy(renames["AdUrlOut"])).optional(),
            "nonSkippableAd": t.proxy(renames["NonSkippableAdOut"]).optional(),
            "inStreamAd": t.proxy(renames["InStreamAdOut"]).optional(),
            "mastheadAd": t.proxy(renames["MastheadAdOut"]).optional(),
            "entityStatus": t.string().optional(),
            "bumperAd": t.proxy(renames["BumperAdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupAdOut"])
    types["NativeContentPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["NativeContentPositionTargetingOptionDetailsIn"])
    types["NativeContentPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentPositionTargetingOptionDetailsOut"])
    types["SearchTargetingOptionsRequestIn"] = t.struct(
        {
            "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
            "pageToken": t.string().optional(),
            "advertiserId": t.string(),
            "pageSize": t.integer().optional(),
            "businessChainSearchTerms": t.proxy(
                renames["BusinessChainSearchTermsIn"]
            ).optional(),
            "geoRegionSearchTerms": t.proxy(
                renames["GeoRegionSearchTermsIn"]
            ).optional(),
        }
    ).named(renames["SearchTargetingOptionsRequestIn"])
    types["SearchTargetingOptionsRequestOut"] = t.struct(
        {
            "poiSearchTerms": t.proxy(renames["PoiSearchTermsOut"]).optional(),
            "pageToken": t.string().optional(),
            "advertiserId": t.string(),
            "pageSize": t.integer().optional(),
            "businessChainSearchTerms": t.proxy(
                renames["BusinessChainSearchTermsOut"]
            ).optional(),
            "geoRegionSearchTerms": t.proxy(
                renames["GeoRegionSearchTermsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTargetingOptionsRequestOut"])
    types["AdvertiserBillingConfigIn"] = t.struct(
        {"billingProfileId": t.string().optional()}
    ).named(renames["AdvertiserBillingConfigIn"])
    types["AdvertiserBillingConfigOut"] = t.struct(
        {
            "billingProfileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserBillingConfigOut"])
    types["GoogleBytestreamMediaIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["GoogleBytestreamMediaIn"])
    types["GoogleBytestreamMediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleBytestreamMediaOut"])
    types["FixedBidStrategyIn"] = t.struct(
        {"bidAmountMicros": t.string().optional()}
    ).named(renames["FixedBidStrategyIn"])
    types["FixedBidStrategyOut"] = t.struct(
        {
            "bidAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixedBidStrategyOut"])
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
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessChainAssignedTargetingOptionDetailsOut"])
    types["BulkEditSitesRequestIn"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
            "deletedSites": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["BulkEditSitesRequestIn"])
    types["BulkEditSitesRequestOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "createdSites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "deletedSites": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditSitesRequestOut"])
    types["ManualTriggerIn"] = t.struct(
        {
            "activationDurationMinutes": t.string(),
            "displayName": t.string(),
            "advertiserId": t.string(),
        }
    ).named(renames["ManualTriggerIn"])
    types["ManualTriggerOut"] = t.struct(
        {
            "name": t.string().optional(),
            "triggerId": t.string().optional(),
            "activationDurationMinutes": t.string(),
            "displayName": t.string(),
            "advertiserId": t.string(),
            "state": t.string().optional(),
            "latestActivationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualTriggerOut"])
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
    types["UserRewardedContentTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UserRewardedContentTargetingOptionDetailsIn"])
    types["UserRewardedContentTargetingOptionDetailsOut"] = t.struct(
        {
            "userRewardedContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRewardedContentTargetingOptionDetailsOut"])
    types["OmidAssignedTargetingOptionDetailsIn"] = t.struct(
        {"omid": t.string().optional()}
    ).named(renames["OmidAssignedTargetingOptionDetailsIn"])
    types["OmidAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "omid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmidAssignedTargetingOptionDetailsOut"])
    types["ChannelIn"] = t.struct(
        {
            "displayName": t.string(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "positivelyTargetedLineItemCount": t.string().optional(),
            "displayName": t.string(),
            "partnerId": t.string().optional(),
            "negativelyTargetedLineItemCount": t.string().optional(),
            "name": t.string().optional(),
            "channelId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["CampaignIn"] = t.struct(
        {
            "campaignBudgets": t.array(t.proxy(renames["CampaignBudgetIn"])).optional(),
            "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
            "entityStatus": t.string(),
            "displayName": t.string(),
            "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
        }
    ).named(renames["CampaignIn"])
    types["CampaignOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "campaignBudgets": t.array(
                t.proxy(renames["CampaignBudgetOut"])
            ).optional(),
            "campaignGoal": t.proxy(renames["CampaignGoalOut"]),
            "campaignId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "entityStatus": t.string(),
            "displayName": t.string(),
            "campaignFlight": t.proxy(renames["CampaignFlightOut"]),
            "name": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignOut"])
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
    types["EditCustomerMatchMembersResponseIn"] = t.struct(
        {"firstAndThirdPartyAudienceId": t.string()}
    ).named(renames["EditCustomerMatchMembersResponseIn"])
    types["EditCustomerMatchMembersResponseOut"] = t.struct(
        {
            "firstAndThirdPartyAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditCustomerMatchMembersResponseOut"])
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
    types["TranscodeIn"] = t.struct(
        {
            "dimensions": t.proxy(renames["DimensionsIn"]).optional(),
            "frameRate": t.number().optional(),
            "audioBitRateKbps": t.string().optional(),
            "bitRateKbps": t.string().optional(),
            "name": t.string().optional(),
            "mimeType": t.string().optional(),
            "transcoded": t.boolean().optional(),
            "fileSizeBytes": t.string().optional(),
            "audioSampleRateHz": t.string().optional(),
        }
    ).named(renames["TranscodeIn"])
    types["TranscodeOut"] = t.struct(
        {
            "dimensions": t.proxy(renames["DimensionsOut"]).optional(),
            "frameRate": t.number().optional(),
            "audioBitRateKbps": t.string().optional(),
            "bitRateKbps": t.string().optional(),
            "name": t.string().optional(),
            "mimeType": t.string().optional(),
            "transcoded": t.boolean().optional(),
            "fileSizeBytes": t.string().optional(),
            "audioSampleRateHz": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscodeOut"])
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
    types["ContentDurationTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentDurationTargetingOptionDetailsIn"])
    types["ContentDurationTargetingOptionDetailsOut"] = t.struct(
        {
            "contentDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentDurationTargetingOptionDetailsOut"])
    types["ContentStreamTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentStreamTypeTargetingOptionDetailsIn"])
    types["ContentStreamTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "contentStreamType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentStreamTypeTargetingOptionDetailsOut"])
    types["MobileAppIn"] = t.struct({"appId": t.string()}).named(renames["MobileAppIn"])
    types["MobileAppOut"] = t.struct(
        {
            "appId": t.string(),
            "publisher": t.string().optional(),
            "displayName": t.string().optional(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileAppOut"])
    types["PartnerAdServerConfigIn"] = t.struct(
        {"measurementConfig": t.proxy(renames["MeasurementConfigIn"]).optional()}
    ).named(renames["PartnerAdServerConfigIn"])
    types["PartnerAdServerConfigOut"] = t.struct(
        {
            "measurementConfig": t.proxy(renames["MeasurementConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerAdServerConfigOut"])
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
    types["YoutubeAndPartnersSettingsIn"] = t.struct(
        {
            "targetFrequency": t.proxy(renames["TargetFrequencyIn"]).optional(),
            "inventorySourceSettings": t.proxy(
                renames["YoutubeAndPartnersInventorySourceConfigIn"]
            ).optional(),
            "videoAdSequenceSettings": t.proxy(
                renames["VideoAdSequenceSettingsIn"]
            ).optional(),
            "leadFormId": t.string().optional(),
            "linkedMerchantId": t.string().optional(),
            "thirdPartyMeasurementSettings": t.proxy(
                renames["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"]
            ).optional(),
            "relatedVideoIds": t.array(t.string()).optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyIn"]
            ).optional(),
            "viewFrequencyCap": t.proxy(renames["FrequencyCapIn"]).optional(),
            "contentCategory": t.string().optional(),
        }
    ).named(renames["YoutubeAndPartnersSettingsIn"])
    types["YoutubeAndPartnersSettingsOut"] = t.struct(
        {
            "targetFrequency": t.proxy(renames["TargetFrequencyOut"]).optional(),
            "inventorySourceSettings": t.proxy(
                renames["YoutubeAndPartnersInventorySourceConfigOut"]
            ).optional(),
            "videoAdSequenceSettings": t.proxy(
                renames["VideoAdSequenceSettingsOut"]
            ).optional(),
            "leadFormId": t.string().optional(),
            "linkedMerchantId": t.string().optional(),
            "thirdPartyMeasurementSettings": t.proxy(
                renames["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"]
            ).optional(),
            "relatedVideoIds": t.array(t.string()).optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyOut"]
            ).optional(),
            "viewFrequencyCap": t.proxy(renames["FrequencyCapOut"]).optional(),
            "contentCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersSettingsOut"])
    types["MaximizeSpendBidStrategyIn"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalType": t.string(),
            "raiseBidForDeals": t.boolean().optional(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
        }
    ).named(renames["MaximizeSpendBidStrategyIn"])
    types["MaximizeSpendBidStrategyOut"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalType": t.string(),
            "raiseBidForDeals": t.boolean().optional(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaximizeSpendBidStrategyOut"])
    types["CarrierAndIspTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CarrierAndIspTargetingOptionDetailsIn"])
    types["CarrierAndIspTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarrierAndIspTargetingOptionDetailsOut"])
    types["InventorySourceFilterIn"] = t.struct(
        {"inventorySourceIds": t.array(t.string()).optional()}
    ).named(renames["InventorySourceFilterIn"])
    types["InventorySourceFilterOut"] = t.struct(
        {
            "inventorySourceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceFilterOut"])
    types["GuaranteedOrderIn"] = t.struct(
        {
            "readWriteAdvertiserId": t.string().optional(),
            "readWritePartnerId": t.string().optional(),
            "defaultCampaignId": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "publisherName": t.string(),
            "exchange": t.string(),
            "displayName": t.string(),
            "readAccessInherited": t.boolean().optional(),
            "status": t.proxy(renames["GuaranteedOrderStatusIn"]).optional(),
        }
    ).named(renames["GuaranteedOrderIn"])
    types["GuaranteedOrderOut"] = t.struct(
        {
            "readWriteAdvertiserId": t.string().optional(),
            "guaranteedOrderId": t.string().optional(),
            "readWritePartnerId": t.string().optional(),
            "legacyGuaranteedOrderId": t.string().optional(),
            "defaultCampaignId": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "publisherName": t.string(),
            "exchange": t.string(),
            "displayName": t.string(),
            "readAccessInherited": t.boolean().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "status": t.proxy(renames["GuaranteedOrderStatusOut"]).optional(),
            "defaultAdvertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedOrderOut"])
    types["OnScreenPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["OnScreenPositionAssignedTargetingOptionDetailsIn"])
    types["OnScreenPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "onScreenPosition": t.string().optional(),
            "targetingOptionId": t.string(),
            "adType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnScreenPositionAssignedTargetingOptionDetailsOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["EditInventorySourceReadWriteAccessorsRequestIn"] = t.struct(
        {
            "partnerId": t.string(),
            "assignPartner": t.boolean().optional(),
            "advertisersUpdate": t.proxy(
                renames[
                    "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"
                ]
            ).optional(),
        }
    ).named(renames["EditInventorySourceReadWriteAccessorsRequestIn"])
    types["EditInventorySourceReadWriteAccessorsRequestOut"] = t.struct(
        {
            "partnerId": t.string(),
            "assignPartner": t.boolean().optional(),
            "advertisersUpdate": t.proxy(
                renames[
                    "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditInventorySourceReadWriteAccessorsRequestOut"])
    types["ListManualTriggersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "manualTriggers": t.array(t.proxy(renames["ManualTriggerIn"])).optional(),
        }
    ).named(renames["ListManualTriggersResponseIn"])
    types["ListManualTriggersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "manualTriggers": t.array(t.proxy(renames["ManualTriggerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListManualTriggersResponseOut"])
    types["BulkEditSitesResponseIn"] = t.struct(
        {"sites": t.array(t.proxy(renames["SiteIn"])).optional()}
    ).named(renames["BulkEditSitesResponseIn"])
    types["BulkEditSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditSitesResponseOut"])
    types["ProximityLocationListAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "proximityRadiusUnit": t.string(),
            "proximityLocationListId": t.string(),
            "proximityRadius": t.number(),
        }
    ).named(renames["ProximityLocationListAssignedTargetingOptionDetailsIn"])
    types["ProximityLocationListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "proximityRadiusUnit": t.string(),
            "proximityLocationListId": t.string(),
            "proximityRadius": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProximityLocationListAssignedTargetingOptionDetailsOut"])
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
    types["VideoPlayerSizeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VideoPlayerSizeTargetingOptionDetailsIn"])
    types["VideoPlayerSizeTargetingOptionDetailsOut"] = t.struct(
        {
            "videoPlayerSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerSizeTargetingOptionDetailsOut"])
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
    types["DuplicateLineItemRequestIn"] = t.struct(
        {"targetDisplayName": t.string().optional()}
    ).named(renames["DuplicateLineItemRequestIn"])
    types["DuplicateLineItemRequestOut"] = t.struct(
        {
            "targetDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateLineItemRequestOut"])
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
    types["BrowserAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["BrowserAssignedTargetingOptionDetailsIn"])
    types["BrowserAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserAssignedTargetingOptionDetailsOut"])
    types["SearchTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targetingOptions": t.array(
                t.proxy(renames["TargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["SearchTargetingOptionsResponseIn"])
    types["SearchTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targetingOptions": t.array(
                t.proxy(renames["TargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTargetingOptionsResponseOut"])
    types["GenerateDefaultLineItemRequestIn"] = t.struct(
        {
            "insertionOrderId": t.string(),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
            "lineItemType": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["GenerateDefaultLineItemRequestIn"])
    types["GenerateDefaultLineItemRequestOut"] = t.struct(
        {
            "insertionOrderId": t.string(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "lineItemType": t.string(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateDefaultLineItemRequestOut"])
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
    types["ReplaceSitesResponseIn"] = t.struct(
        {"sites": t.array(t.proxy(renames["SiteIn"])).optional()}
    ).named(renames["ReplaceSitesResponseIn"])
    types["ReplaceSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceSitesResponseOut"])
    types["UniversalAdIdIn"] = t.struct(
        {"id": t.string().optional(), "registry": t.string().optional()}
    ).named(renames["UniversalAdIdIn"])
    types["UniversalAdIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "registry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UniversalAdIdOut"])
    types["GenderTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenderTargetingOptionDetailsIn"])
    types["GenderTargetingOptionDetailsOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderTargetingOptionDetailsOut"])
    types["OmidTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OmidTargetingOptionDetailsIn"])
    types["OmidTargetingOptionDetailsOut"] = t.struct(
        {
            "omid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmidTargetingOptionDetailsOut"])
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
    types["ListAssignedLocationsResponseIn"] = t.struct(
        {
            "assignedLocations": t.array(
                t.proxy(renames["AssignedLocationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssignedLocationsResponseIn"])
    types["ListAssignedLocationsResponseOut"] = t.struct(
        {
            "assignedLocations": t.array(
                t.proxy(renames["AssignedLocationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssignedLocationsResponseOut"])
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
    types["CreateAssetResponseIn"] = t.struct(
        {"asset": t.proxy(renames["AssetIn"]).optional()}
    ).named(renames["CreateAssetResponseIn"])
    types["CreateAssetResponseOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAssetResponseOut"])
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
    types["PartnerDataAccessConfigIn"] = t.struct(
        {"sdfConfig": t.proxy(renames["SdfConfigIn"]).optional()}
    ).named(renames["PartnerDataAccessConfigIn"])
    types["PartnerDataAccessConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["SdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerDataAccessConfigOut"])
    types["InventorySourceVideoCreativeConfigIn"] = t.struct(
        {"duration": t.string().optional()}
    ).named(renames["InventorySourceVideoCreativeConfigIn"])
    types["InventorySourceVideoCreativeConfigOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceVideoCreativeConfigOut"])
    types["BudgetSummaryIn"] = t.struct(
        {
            "externalBudgetId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "preTaxAmountMicros": t.string().optional(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeIn"]).optional(),
            "taxAmountMicros": t.string().optional(),
        }
    ).named(renames["BudgetSummaryIn"])
    types["BudgetSummaryOut"] = t.struct(
        {
            "externalBudgetId": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "preTaxAmountMicros": t.string().optional(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeOut"]).optional(),
            "taxAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BudgetSummaryOut"])
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
    types["ActiveViewVideoViewabilityMetricConfigIn"] = t.struct(
        {
            "minimumVolume": t.string(),
            "minimumDuration": t.string().optional(),
            "minimumViewability": t.string(),
            "minimumQuartile": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["ActiveViewVideoViewabilityMetricConfigIn"])
    types["ActiveViewVideoViewabilityMetricConfigOut"] = t.struct(
        {
            "minimumVolume": t.string(),
            "minimumDuration": t.string().optional(),
            "minimumViewability": t.string(),
            "minimumQuartile": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActiveViewVideoViewabilityMetricConfigOut"])
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
    types["DigitalContentLabelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"excludedContentRatingTier": t.string()}
    ).named(renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"])
    types["DigitalContentLabelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "excludedContentRatingTier": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigitalContentLabelAssignedTargetingOptionDetailsOut"])
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
    types["VideoPerformanceAdIn"] = t.struct(
        {
            "displayUrlBreadcrumb1": t.string().optional(),
            "displayUrlBreadcrumb2": t.string().optional(),
            "headlines": t.array(t.string()).optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "trackingUrl": t.string().optional(),
            "companionBanners": t.array(t.proxy(renames["ImageAssetIn"])).optional(),
            "videos": t.array(t.proxy(renames["YoutubeVideoDetailsIn"])).optional(),
            "domain": t.string().optional(),
            "actionButtonLabels": t.array(t.string()).optional(),
            "longHeadlines": t.array(t.string()).optional(),
            "descriptions": t.array(t.string()).optional(),
            "finalUrl": t.string().optional(),
        }
    ).named(renames["VideoPerformanceAdIn"])
    types["VideoPerformanceAdOut"] = t.struct(
        {
            "displayUrlBreadcrumb1": t.string().optional(),
            "displayUrlBreadcrumb2": t.string().optional(),
            "headlines": t.array(t.string()).optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "trackingUrl": t.string().optional(),
            "companionBanners": t.array(t.proxy(renames["ImageAssetOut"])).optional(),
            "videos": t.array(t.proxy(renames["YoutubeVideoDetailsOut"])).optional(),
            "domain": t.string().optional(),
            "actionButtonLabels": t.array(t.string()).optional(),
            "longHeadlines": t.array(t.string()).optional(),
            "descriptions": t.array(t.string()).optional(),
            "finalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPerformanceAdOut"])
    types["BulkListAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "lineItemAssignedTargetingOptions": t.array(
                t.proxy(renames["LineItemAssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["BulkListAssignedTargetingOptionsResponseIn"])
    types["BulkListAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "lineItemAssignedTargetingOptions": t.array(
                t.proxy(renames["LineItemAssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListAssignedTargetingOptionsResponseOut"])
    types["VideoDiscoveryAdIn"] = t.struct(
        {
            "description1": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "headline": t.string().optional(),
            "description2": t.string().optional(),
            "thumbnail": t.string().optional(),
        }
    ).named(renames["VideoDiscoveryAdIn"])
    types["VideoDiscoveryAdOut"] = t.struct(
        {
            "description1": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "headline": t.string().optional(),
            "description2": t.string().optional(),
            "thumbnail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoDiscoveryAdOut"])
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
    types["BulkEditAssignedUserRolesRequestIn"] = t.struct(
        {
            "deletedAssignedUserRoles": t.array(t.string()).optional(),
            "createdAssignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleIn"])
            ).optional(),
        }
    ).named(renames["BulkEditAssignedUserRolesRequestIn"])
    types["BulkEditAssignedUserRolesRequestOut"] = t.struct(
        {
            "deletedAssignedUserRoles": t.array(t.string()).optional(),
            "createdAssignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedUserRolesRequestOut"])
    types["ParentalStatusAssignedTargetingOptionDetailsIn"] = t.struct(
        {"parentalStatus": t.string().optional()}
    ).named(renames["ParentalStatusAssignedTargetingOptionDetailsIn"])
    types["ParentalStatusAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "parentalStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentalStatusAssignedTargetingOptionDetailsOut"])
    types["NegativeKeywordListIn"] = t.struct({"displayName": t.string()}).named(
        renames["NegativeKeywordListIn"]
    )
    types["NegativeKeywordListOut"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "negativeKeywordListId": t.string().optional(),
            "targetedLineItemCount": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordListOut"])
    types["YoutubeAndPartnersBiddingStrategyIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string().optional()}
    ).named(renames["YoutubeAndPartnersBiddingStrategyIn"])
    types["YoutubeAndPartnersBiddingStrategyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "adGroupEffectiveTargetCpaSource": t.string().optional(),
            "adGroupEffectiveTargetCpaValue": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersBiddingStrategyOut"])
    types["OnScreenPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OnScreenPositionTargetingOptionDetailsIn"])
    types["OnScreenPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "onScreenPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnScreenPositionTargetingOptionDetailsOut"])
    types["InventorySourceAccessorsAdvertiserAccessorsIn"] = t.struct(
        {"advertiserIds": t.array(t.string()).optional()}
    ).named(renames["InventorySourceAccessorsAdvertiserAccessorsIn"])
    types["InventorySourceAccessorsAdvertiserAccessorsOut"] = t.struct(
        {
            "advertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsAdvertiserAccessorsOut"])
    types["BulkEditAssignedInventorySourcesRequestIn"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "createdAssignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceIn"])
            ).optional(),
            "deletedAssignedInventorySources": t.array(t.string()).optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesRequestIn"])
    types["BulkEditAssignedInventorySourcesRequestOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "createdAssignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceOut"])
            ).optional(),
            "deletedAssignedInventorySources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesRequestOut"])
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
    types["GeoRegionSearchTermsIn"] = t.struct(
        {"geoRegionQuery": t.string().optional()}
    ).named(renames["GeoRegionSearchTermsIn"])
    types["GeoRegionSearchTermsOut"] = t.struct(
        {
            "geoRegionQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionSearchTermsOut"])
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
    types["AdvertiserTargetingConfigIn"] = t.struct(
        {"exemptTvFromViewabilityTargeting": t.boolean().optional()}
    ).named(renames["AdvertiserTargetingConfigIn"])
    types["AdvertiserTargetingConfigOut"] = t.struct(
        {
            "exemptTvFromViewabilityTargeting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserTargetingConfigOut"])
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
    types["LineItemAssignedTargetingOptionIn"] = t.struct(
        {
            "assignedTargetingOption": t.proxy(
                renames["AssignedTargetingOptionIn"]
            ).optional(),
            "lineItemId": t.string().optional(),
        }
    ).named(renames["LineItemAssignedTargetingOptionIn"])
    types["LineItemAssignedTargetingOptionOut"] = t.struct(
        {
            "assignedTargetingOption": t.proxy(
                renames["AssignedTargetingOptionOut"]
            ).optional(),
            "lineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemAssignedTargetingOptionOut"])
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
    types["NativeContentPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"contentPosition": t.string().optional()}
    ).named(renames["NativeContentPositionAssignedTargetingOptionDetailsIn"])
    types["NativeContentPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "contentPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentPositionAssignedTargetingOptionDetailsOut"])
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
    types["CustomLabelIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["CustomLabelIn"])
    types["CustomLabelOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomLabelOut"])
    types["ObaIconIn"] = t.struct(
        {
            "resourceMimeType": t.string().optional(),
            "program": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]).optional(),
            "clickTrackingUrl": t.string(),
            "position": t.string().optional(),
            "landingPageUrl": t.string(),
            "resourceUrl": t.string().optional(),
            "viewTrackingUrl": t.string(),
        }
    ).named(renames["ObaIconIn"])
    types["ObaIconOut"] = t.struct(
        {
            "resourceMimeType": t.string().optional(),
            "program": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]).optional(),
            "clickTrackingUrl": t.string(),
            "position": t.string().optional(),
            "landingPageUrl": t.string(),
            "resourceUrl": t.string().optional(),
            "viewTrackingUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObaIconOut"])
    types["IntegralAdScienceIn"] = t.struct(
        {
            "customSegmentId": t.array(t.string()).optional(),
            "excludedDrugsRisk": t.string().optional(),
            "excludedAdFraudRisk": t.string().optional(),
            "traqScoreOption": t.string().optional(),
            "displayViewability": t.string().optional(),
            "excludedHateSpeechRisk": t.string().optional(),
            "excludeUnrateable": t.boolean().optional(),
            "excludedAdultRisk": t.string().optional(),
            "excludedGamblingRisk": t.string().optional(),
            "excludedOffensiveLanguageRisk": t.string().optional(),
            "videoViewability": t.string().optional(),
            "excludedAlcoholRisk": t.string().optional(),
            "excludedIllegalDownloadsRisk": t.string().optional(),
            "excludedViolenceRisk": t.string().optional(),
        }
    ).named(renames["IntegralAdScienceIn"])
    types["IntegralAdScienceOut"] = t.struct(
        {
            "customSegmentId": t.array(t.string()).optional(),
            "excludedDrugsRisk": t.string().optional(),
            "excludedAdFraudRisk": t.string().optional(),
            "traqScoreOption": t.string().optional(),
            "displayViewability": t.string().optional(),
            "excludedHateSpeechRisk": t.string().optional(),
            "excludeUnrateable": t.boolean().optional(),
            "excludedAdultRisk": t.string().optional(),
            "excludedGamblingRisk": t.string().optional(),
            "excludedOffensiveLanguageRisk": t.string().optional(),
            "videoViewability": t.string().optional(),
            "excludedAlcoholRisk": t.string().optional(),
            "excludedIllegalDownloadsRisk": t.string().optional(),
            "excludedViolenceRisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegralAdScienceOut"])
    types["AudioAdIn"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "displayUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "finalUrl": t.string().optional(),
        }
    ).named(renames["AudioAdIn"])
    types["AudioAdOut"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "displayUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "finalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioAdOut"])
    types["DeviceTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeviceTypeTargetingOptionDetailsIn"])
    types["DeviceTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTypeTargetingOptionDetailsOut"])
    types["CustomBiddingScriptRefIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["CustomBiddingScriptRefIn"])
    types["CustomBiddingScriptRefOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingScriptRefOut"])
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
    types["CampaignBudgetIn"] = t.struct(
        {
            "externalBudgetSource": t.string(),
            "budgetId": t.string().optional(),
            "budgetUnit": t.string(),
            "displayName": t.string(),
            "dateRange": t.proxy(renames["DateRangeIn"]),
            "invoiceGroupingId": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "prismaConfig": t.proxy(renames["PrismaConfigIn"]).optional(),
            "budgetAmountMicros": t.string(),
        }
    ).named(renames["CampaignBudgetIn"])
    types["CampaignBudgetOut"] = t.struct(
        {
            "externalBudgetSource": t.string(),
            "budgetId": t.string().optional(),
            "budgetUnit": t.string(),
            "displayName": t.string(),
            "dateRange": t.proxy(renames["DateRangeOut"]),
            "invoiceGroupingId": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "prismaConfig": t.proxy(renames["PrismaConfigOut"]).optional(),
            "budgetAmountMicros": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignBudgetOut"])
    types["CategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CategoryTargetingOptionDetailsIn"])
    types["CategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryTargetingOptionDetailsOut"])
    types["ContentOutstreamPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentOutstreamPositionTargetingOptionDetailsIn"])
    types["ContentOutstreamPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentOutstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOutstreamPositionTargetingOptionDetailsOut"])
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
    types["PacingIn"] = t.struct(
        {
            "dailyMaxImpressions": t.string().optional(),
            "dailyMaxMicros": t.string().optional(),
            "pacingType": t.string(),
            "pacingPeriod": t.string(),
        }
    ).named(renames["PacingIn"])
    types["PacingOut"] = t.struct(
        {
            "dailyMaxImpressions": t.string().optional(),
            "dailyMaxMicros": t.string().optional(),
            "pacingType": t.string(),
            "pacingPeriod": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PacingOut"])
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
    types["ThirdPartyOnlyConfigIn"] = t.struct(
        {"pixelOrderIdReportingEnabled": t.boolean().optional()}
    ).named(renames["ThirdPartyOnlyConfigIn"])
    types["ThirdPartyOnlyConfigOut"] = t.struct(
        {
            "pixelOrderIdReportingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyOnlyConfigOut"])
    types["InventorySourceAssignedTargetingOptionDetailsIn"] = t.struct(
        {"inventorySourceId": t.string()}
    ).named(renames["InventorySourceAssignedTargetingOptionDetailsIn"])
    types["InventorySourceAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "inventorySourceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAssignedTargetingOptionDetailsOut"])
    types["LineItemIn"] = t.struct(
        {
            "entityStatus": t.string(),
            "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
            "budget": t.proxy(renames["LineItemBudgetIn"]),
            "excludeNewExchanges": t.boolean().optional(),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigIn"]
            ).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
            "insertionOrderId": t.string(),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "displayName": t.string(),
            "conversionCounting": t.proxy(
                renames["ConversionCountingConfigIn"]
            ).optional(),
            "creativeIds": t.array(t.string()).optional(),
            "lineItemType": t.string(),
            "flight": t.proxy(renames["LineItemFlightIn"]),
            "pacing": t.proxy(renames["PacingIn"]),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
        }
    ).named(renames["LineItemIn"])
    types["LineItemOut"] = t.struct(
        {
            "entityStatus": t.string(),
            "bidStrategy": t.proxy(renames["BiddingStrategyOut"]),
            "budget": t.proxy(renames["LineItemBudgetOut"]),
            "excludeNewExchanges": t.boolean().optional(),
            "lineItemId": t.string().optional(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigOut"]
            ).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelOut"]),
            "insertionOrderId": t.string(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "advertiserId": t.string().optional(),
            "campaignId": t.string().optional(),
            "displayName": t.string(),
            "conversionCounting": t.proxy(
                renames["ConversionCountingConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "creativeIds": t.array(t.string()).optional(),
            "youtubeAndPartnersSettings": t.proxy(
                renames["YoutubeAndPartnersSettingsOut"]
            ).optional(),
            "lineItemType": t.string(),
            "flight": t.proxy(renames["LineItemFlightOut"]),
            "name": t.string().optional(),
            "reservationType": t.string().optional(),
            "pacing": t.proxy(renames["PacingOut"]),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostOut"])).optional(),
            "warningMessages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemOut"])
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
    types["ParentEntityFilterIn"] = t.struct(
        {
            "filterType": t.string(),
            "filterIds": t.array(t.string()).optional(),
            "fileType": t.array(t.string()),
        }
    ).named(renames["ParentEntityFilterIn"])
    types["ParentEntityFilterOut"] = t.struct(
        {
            "filterType": t.string(),
            "filterIds": t.array(t.string()).optional(),
            "fileType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentEntityFilterOut"])
    types["PerformanceGoalBidStrategyIn"] = t.struct(
        {
            "performanceGoalAmountMicros": t.string(),
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalType": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
        }
    ).named(renames["PerformanceGoalBidStrategyIn"])
    types["PerformanceGoalBidStrategyOut"] = t.struct(
        {
            "performanceGoalAmountMicros": t.string(),
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalType": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceGoalBidStrategyOut"])
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
    types["ContentInstreamPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentInstreamPositionTargetingOptionDetailsIn"])
    types["ContentInstreamPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentInstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentInstreamPositionTargetingOptionDetailsOut"])
    types["UserIn"] = t.struct(
        {
            "displayName": t.string(),
            "assignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleIn"])
            ).optional(),
            "email": t.string(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string().optional(),
            "assignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleOut"])
            ).optional(),
            "userId": t.string().optional(),
            "email": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["AdvertiserIn"] = t.struct(
        {
            "entityStatus": t.string(),
            "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
            "billingConfig": t.proxy(renames["AdvertiserBillingConfigIn"]).optional(),
            "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
            "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
            "dataAccessConfig": t.proxy(
                renames["AdvertiserDataAccessConfigIn"]
            ).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "displayName": t.string(),
            "prismaEnabled": t.boolean().optional(),
            "partnerId": t.string(),
            "servingConfig": t.proxy(renames["AdvertiserTargetingConfigIn"]).optional(),
        }
    ).named(renames["AdvertiserIn"])
    types["AdvertiserOut"] = t.struct(
        {
            "entityStatus": t.string(),
            "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigOut"]),
            "billingConfig": t.proxy(renames["AdvertiserBillingConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "generalConfig": t.proxy(renames["AdvertiserGeneralConfigOut"]),
            "advertiserId": t.string().optional(),
            "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigOut"]),
            "dataAccessConfig": t.proxy(
                renames["AdvertiserDataAccessConfigOut"]
            ).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "displayName": t.string(),
            "prismaEnabled": t.boolean().optional(),
            "partnerId": t.string(),
            "servingConfig": t.proxy(
                renames["AdvertiserTargetingConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserOut"])
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
    types["CreateSdfDownloadTaskRequestIn"] = t.struct(
        {
            "version": t.string(),
            "parentEntityFilter": t.proxy(renames["ParentEntityFilterIn"]).optional(),
            "inventorySourceFilter": t.proxy(
                renames["InventorySourceFilterIn"]
            ).optional(),
            "idFilter": t.proxy(renames["IdFilterIn"]).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["CreateSdfDownloadTaskRequestIn"])
    types["CreateSdfDownloadTaskRequestOut"] = t.struct(
        {
            "version": t.string(),
            "parentEntityFilter": t.proxy(renames["ParentEntityFilterOut"]).optional(),
            "inventorySourceFilter": t.proxy(
                renames["InventorySourceFilterOut"]
            ).optional(),
            "idFilter": t.proxy(renames["IdFilterOut"]).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSdfDownloadTaskRequestOut"])
    types["ListAdvertisersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "advertisers": t.array(t.proxy(renames["AdvertiserIn"])).optional(),
        }
    ).named(renames["ListAdvertisersResponseIn"])
    types["ListAdvertisersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "advertisers": t.array(t.proxy(renames["AdvertiserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAdvertisersResponseOut"])
    types["AgeRangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AgeRangeTargetingOptionDetailsIn"])
    types["AgeRangeTargetingOptionDetailsOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeTargetingOptionDetailsOut"])
    types["ListInsertionOrdersResponseIn"] = t.struct(
        {
            "insertionOrders": t.array(t.proxy(renames["InsertionOrderIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInsertionOrdersResponseIn"])
    types["ListInsertionOrdersResponseOut"] = t.struct(
        {
            "insertionOrders": t.array(
                t.proxy(renames["InsertionOrderOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInsertionOrdersResponseOut"])
    types["CombinedAudienceTargetingSettingIn"] = t.struct(
        {"combinedAudienceId": t.string()}
    ).named(renames["CombinedAudienceTargetingSettingIn"])
    types["CombinedAudienceTargetingSettingOut"] = t.struct(
        {
            "combinedAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CombinedAudienceTargetingSettingOut"])
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
    types["CmTrackingAdIn"] = t.struct(
        {
            "cmAdId": t.string().optional(),
            "cmCreativeId": t.string().optional(),
            "cmPlacementId": t.string().optional(),
        }
    ).named(renames["CmTrackingAdIn"])
    types["CmTrackingAdOut"] = t.struct(
        {
            "cmAdId": t.string().optional(),
            "cmCreativeId": t.string().optional(),
            "cmPlacementId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmTrackingAdOut"])
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
    types["ExchangeConfigEnabledExchangeIn"] = t.struct(
        {"exchange": t.string().optional()}
    ).named(renames["ExchangeConfigEnabledExchangeIn"])
    types["ExchangeConfigEnabledExchangeOut"] = t.struct(
        {
            "seatId": t.string().optional(),
            "googleAdManagerBuyerNetworkId": t.string().optional(),
            "exchange": t.string().optional(),
            "googleAdManagerAgencyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeConfigEnabledExchangeOut"])
    types["PrismaCpeCodeIn"] = t.struct(
        {
            "prismaProductCode": t.string().optional(),
            "prismaEstimateCode": t.string().optional(),
            "prismaClientCode": t.string().optional(),
        }
    ).named(renames["PrismaCpeCodeIn"])
    types["PrismaCpeCodeOut"] = t.struct(
        {
            "prismaProductCode": t.string().optional(),
            "prismaEstimateCode": t.string().optional(),
            "prismaClientCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrismaCpeCodeOut"])
    types["PoiSearchTermsIn"] = t.struct({"poiQuery": t.string().optional()}).named(
        renames["PoiSearchTermsIn"]
    )
    types["PoiSearchTermsOut"] = t.struct(
        {
            "poiQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiSearchTermsOut"])
    types["ListPartnersResponseIn"] = t.struct(
        {
            "partners": t.array(t.proxy(renames["PartnerIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPartnersResponseIn"])
    types["ListPartnersResponseOut"] = t.struct(
        {
            "partners": t.array(t.proxy(renames["PartnerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPartnersResponseOut"])
    types["YoutubeAdGroupAssignedTargetingOptionIn"] = t.struct(
        {
            "assignedTargetingOption": t.proxy(
                renames["AssignedTargetingOptionIn"]
            ).optional(),
            "youtubeAdGroupId": t.string().optional(),
        }
    ).named(renames["YoutubeAdGroupAssignedTargetingOptionIn"])
    types["YoutubeAdGroupAssignedTargetingOptionOut"] = t.struct(
        {
            "assignedTargetingOption": t.proxy(
                renames["AssignedTargetingOptionOut"]
            ).optional(),
            "youtubeAdGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupAssignedTargetingOptionOut"])
    types["LookbackWindowIn"] = t.struct(
        {"clickDays": t.integer().optional(), "impressionDays": t.integer().optional()}
    ).named(renames["LookbackWindowIn"])
    types["LookbackWindowOut"] = t.struct(
        {
            "clickDays": t.integer().optional(),
            "impressionDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookbackWindowOut"])
    types["AssignedUserRoleIn"] = t.struct(
        {
            "userRole": t.string(),
            "advertiserId": t.string().optional(),
            "partnerId": t.string().optional(),
        }
    ).named(renames["AssignedUserRoleIn"])
    types["AssignedUserRoleOut"] = t.struct(
        {
            "userRole": t.string(),
            "advertiserId": t.string().optional(),
            "assignedUserRoleId": t.string().optional(),
            "partnerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedUserRoleOut"])
    types["VideoAdSequenceSettingsIn"] = t.struct(
        {
            "minimumDuration": t.string().optional(),
            "steps": t.array(t.proxy(renames["VideoAdSequenceStepIn"])).optional(),
        }
    ).named(renames["VideoAdSequenceSettingsIn"])
    types["VideoAdSequenceSettingsOut"] = t.struct(
        {
            "minimumDuration": t.string().optional(),
            "steps": t.array(t.proxy(renames["VideoAdSequenceStepOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAdSequenceSettingsOut"])
    types["ContentGenreAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["ContentGenreAssignedTargetingOptionDetailsIn"])
    types["ContentGenreAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentGenreAssignedTargetingOptionDetailsOut"])
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
    types["CommonInStreamAttributeIn"] = t.struct(
        {
            "companionBanner": t.proxy(renames["ImageAssetIn"]).optional(),
            "finalUrl": t.string().optional(),
            "actionHeadline": t.string().optional(),
            "trackingUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "displayUrl": t.string().optional(),
            "actionButtonLabel": t.string().optional(),
        }
    ).named(renames["CommonInStreamAttributeIn"])
    types["CommonInStreamAttributeOut"] = t.struct(
        {
            "companionBanner": t.proxy(renames["ImageAssetOut"]).optional(),
            "finalUrl": t.string().optional(),
            "actionHeadline": t.string().optional(),
            "trackingUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "displayUrl": t.string().optional(),
            "actionButtonLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonInStreamAttributeOut"])
    types["AdvertiserGeneralConfigIn"] = t.struct(
        {"currencyCode": t.string(), "domainUrl": t.string()}
    ).named(renames["AdvertiserGeneralConfigIn"])
    types["AdvertiserGeneralConfigOut"] = t.struct(
        {
            "currencyCode": t.string(),
            "domainUrl": t.string(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserGeneralConfigOut"])
    types["ParentalStatusTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ParentalStatusTargetingOptionDetailsIn"])
    types["ParentalStatusTargetingOptionDetailsOut"] = t.struct(
        {
            "parentalStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentalStatusTargetingOptionDetailsOut"])
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
    types["SubExchangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["SubExchangeAssignedTargetingOptionDetailsIn"])
    types["SubExchangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubExchangeAssignedTargetingOptionDetailsOut"])
    types["InsertionOrderIn"] = t.struct(
        {
            "displayName": t.string(),
            "entityStatus": t.string(),
            "pacing": t.proxy(renames["PacingIn"]),
            "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
            "billableOutcome": t.string().optional(),
            "campaignId": t.string(),
            "insertionOrderType": t.string().optional(),
        }
    ).named(renames["InsertionOrderIn"])
    types["InsertionOrderOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "reservationType": t.string().optional(),
            "displayName": t.string(),
            "entityStatus": t.string(),
            "pacing": t.proxy(renames["PacingOut"]),
            "budget": t.proxy(renames["InsertionOrderBudgetOut"]),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostOut"])).optional(),
            "insertionOrderId": t.string().optional(),
            "name": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "bidStrategy": t.proxy(renames["BiddingStrategyOut"]).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "performanceGoal": t.proxy(renames["PerformanceGoalOut"]),
            "advertiserId": t.string().optional(),
            "billableOutcome": t.string().optional(),
            "campaignId": t.string(),
            "insertionOrderType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderOut"])
    types["CustomListIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CustomListIn"]
    )
    types["CustomListOut"] = t.struct(
        {
            "customListId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListOut"])

    functions = {}
    functions["floodlightGroupsGet"] = displayvideo.patch(
        "v2/floodlightGroups/{floodlightGroupId}",
        t.struct(
            {
                "updateMask": t.string(),
                "partnerId": t.string(),
                "floodlightGroupId": t.string().optional(),
                "lookbackWindow": t.proxy(renames["LookbackWindowIn"]),
                "webTagType": t.string(),
                "activeViewConfig": t.proxy(
                    renames["ActiveViewVideoViewabilityMetricConfigIn"]
                ).optional(),
                "customVariables": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string(),
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
                "updateMask": t.string(),
                "partnerId": t.string(),
                "floodlightGroupId": t.string().optional(),
                "lookbackWindow": t.proxy(renames["LookbackWindowIn"]),
                "webTagType": t.string(),
                "activeViewConfig": t.proxy(
                    renames["ActiveViewVideoViewabilityMetricConfigIn"]
                ).optional(),
                "customVariables": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleAudiencesList"] = displayvideo.get(
        "v2/googleAudiences/{googleAudienceId}",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "googleAudienceId": t.string(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleAudiencesGet"] = displayvideo.get(
        "v2/googleAudiences/{googleAudienceId}",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "googleAudienceId": t.string(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAudienceOut"]),
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
    functions["partnersList"] = displayvideo.post(
        "v2/partners/{partnerId}:editAssignedTargetingOptions",
        t.struct(
            {
                "partnerId": t.string(),
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
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
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
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
                "deleteRequests": t.array(
                    t.proxy(renames["DeleteAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "createRequests": t.array(
                    t.proxy(renames["CreateAssignedTargetingOptionsRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditPartnerAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "partnersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.post(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "partnerId": t.string(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
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
                "targetingType": t.string(),
                "partnerId": t.string(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersTargetingTypesAssignedTargetingOptionsGet"] = displayvideo.post(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "partnerId": t.string(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
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
                "targetingType": t.string(),
                "partnerId": t.string(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsGet"] = displayvideo.get(
        "v2/partners/{partnerId}/channels",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsPatch"] = displayvideo.get(
        "v2/partners/{partnerId}/channels",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsCreate"] = displayvideo.get(
        "v2/partners/{partnerId}/channels",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsList"] = displayvideo.get(
        "v2/partners/{partnerId}/channels",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesBulkEdit"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesDelete"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesList"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesReplace"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesCreate"] = displayvideo.post(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "channelId": t.string(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "urlOrAppId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersAudit"] = displayvideo.get(
        "v2/advertisers/{advertiserId}:listAssignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersDelete"] = displayvideo.get(
        "v2/advertisers/{advertiserId}:listAssignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}:listAssignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}:listAssignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}:listAssignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}:listAssignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersEditAssignedTargetingOptions"] = displayvideo.get(
        "v2/advertisers/{advertiserId}:listAssignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersListAssignedTargetingOptions"] = displayvideo.get(
        "v2/advertisers/{advertiserId}:listAssignedTargetingOptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsCreate"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "campaignId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCampaignsListAssignedTargetingOptions"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/campaigns/{campaignId}",
        t.struct(
            {
                "campaignId": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "campaignId": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "campaignId": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "campaignId": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "campaignId": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "assignedTargetingOptionId": t.string(),
                "campaignId": t.string(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
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
                "assignedTargetingOptionId": t.string(),
                "campaignId": t.string(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupAdsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroupAds",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupAdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInvoicesList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/invoices:lookupInvoiceCurrency",
        t.struct(
            {
                "invoiceMonth": t.string().optional(),
                "advertiserId": t.string(),
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
                "invoiceMonth": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupInvoiceCurrencyResponseOut"]),
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
        "advertisersNegativeKeywordListsNegativeKeywordsList"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string(),
                "negativeKeywordListId": t.string(),
                "createdNegativeKeywords": t.array(
                    t.proxy(renames["NegativeKeywordIn"])
                ).optional(),
                "deletedNegativeKeywords": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsDelete"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string(),
                "negativeKeywordListId": t.string(),
                "createdNegativeKeywords": t.array(
                    t.proxy(renames["NegativeKeywordIn"])
                ).optional(),
                "deletedNegativeKeywords": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsReplace"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string(),
                "negativeKeywordListId": t.string(),
                "createdNegativeKeywords": t.array(
                    t.proxy(renames["NegativeKeywordIn"])
                ).optional(),
                "deletedNegativeKeywords": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsCreate"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string(),
                "negativeKeywordListId": t.string(),
                "createdNegativeKeywords": t.array(
                    t.proxy(renames["NegativeKeywordIn"])
                ).optional(),
                "deletedNegativeKeywords": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersNegativeKeywordListsNegativeKeywordsBulkEdit"
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}/negativeKeywords:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string(),
                "negativeKeywordListId": t.string(),
                "createdNegativeKeywords": t.array(
                    t.proxy(renames["NegativeKeywordIn"])
                ).optional(),
                "deletedNegativeKeywords": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditNegativeKeywordsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
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
        "advertisersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
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
        "advertisersTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
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
        "advertisersTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
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
    functions["advertisersChannelsPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
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
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "partnerId": t.string().optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "deletedSites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites:bulkEdit",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "partnerId": t.string().optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "deletedSites": t.array(t.string()).optional(),
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
                "partnerId": t.string().optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "deletedSites": t.array(t.string()).optional(),
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
                "partnerId": t.string().optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "deletedSites": t.array(t.string()).optional(),
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
                "partnerId": t.string().optional(),
                "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
                "deletedSites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkEditSitesResponseOut"]),
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
    functions["advertisersLocationListsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "locationListId": t.string(),
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
                "advertiserId": t.string(),
                "locationListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "locationListId": t.string(),
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
                "advertiserId": t.string(),
                "locationListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsBulkEdit"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "locationListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssignedLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "locationListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssignedLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsDelete"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "locationListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssignedLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "orderBy": t.string().optional(),
                "locationListId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssignedLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "requireHtml5": t.boolean().optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "entityStatus": t.string(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "creativeType": t.string(),
                "appendedTag": t.string().optional(),
                "skippable": t.boolean().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "iasCampaignMonitoring": t.boolean().optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "jsTrackerUrl": t.string().optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "hostingSource": t.string(),
                "vastTagUrl": t.string().optional(),
                "integrationCode": t.string().optional(),
                "displayName": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "companionCreativeIds": t.array(t.string()).optional(),
                "expandOnHover": t.boolean().optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandingDirection": t.string().optional(),
                "thirdPartyTag": t.string().optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "requireHtml5": t.boolean().optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "entityStatus": t.string(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "creativeType": t.string(),
                "appendedTag": t.string().optional(),
                "skippable": t.boolean().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "iasCampaignMonitoring": t.boolean().optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "jsTrackerUrl": t.string().optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "hostingSource": t.string(),
                "vastTagUrl": t.string().optional(),
                "integrationCode": t.string().optional(),
                "displayName": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "companionCreativeIds": t.array(t.string()).optional(),
                "expandOnHover": t.boolean().optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandingDirection": t.string().optional(),
                "thirdPartyTag": t.string().optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
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
                "requireHtml5": t.boolean().optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "entityStatus": t.string(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "creativeType": t.string(),
                "appendedTag": t.string().optional(),
                "skippable": t.boolean().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "iasCampaignMonitoring": t.boolean().optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "jsTrackerUrl": t.string().optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "hostingSource": t.string(),
                "vastTagUrl": t.string().optional(),
                "integrationCode": t.string().optional(),
                "displayName": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "companionCreativeIds": t.array(t.string()).optional(),
                "expandOnHover": t.boolean().optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandingDirection": t.string().optional(),
                "thirdPartyTag": t.string().optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
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
                "requireHtml5": t.boolean().optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "entityStatus": t.string(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "creativeType": t.string(),
                "appendedTag": t.string().optional(),
                "skippable": t.boolean().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "iasCampaignMonitoring": t.boolean().optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "jsTrackerUrl": t.string().optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "hostingSource": t.string(),
                "vastTagUrl": t.string().optional(),
                "integrationCode": t.string().optional(),
                "displayName": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "companionCreativeIds": t.array(t.string()).optional(),
                "expandOnHover": t.boolean().optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandingDirection": t.string().optional(),
                "thirdPartyTag": t.string().optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
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
                "requireHtml5": t.boolean().optional(),
                "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "notes": t.string().optional(),
                "requireMraid": t.boolean().optional(),
                "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
                "entityStatus": t.string(),
                "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
                "creativeType": t.string(),
                "appendedTag": t.string().optional(),
                "skippable": t.boolean().optional(),
                "trackerUrls": t.array(t.string()).optional(),
                "iasCampaignMonitoring": t.boolean().optional(),
                "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
                "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
                "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
                "jsTrackerUrl": t.string().optional(),
                "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
                "requirePingForAttribution": t.boolean().optional(),
                "additionalDimensions": t.array(
                    t.proxy(renames["DimensionsIn"])
                ).optional(),
                "thirdPartyUrls": t.array(
                    t.proxy(renames["ThirdPartyUrlIn"])
                ).optional(),
                "hostingSource": t.string(),
                "vastTagUrl": t.string().optional(),
                "integrationCode": t.string().optional(),
                "displayName": t.string(),
                "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
                "companionCreativeIds": t.array(t.string()).optional(),
                "expandOnHover": t.boolean().optional(),
                "dimensions": t.proxy(renames["DimensionsIn"]),
                "expandingDirection": t.string().optional(),
                "thirdPartyTag": t.string().optional(),
                "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupsResponseOut"]),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
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
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "youtubeAdGroupId": t.string(),
                "targetingType": t.string(),
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
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "youtubeAdGroupId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:deactivate",
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
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:deactivate",
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
    functions["advertisersManualTriggersGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:deactivate",
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
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:deactivate",
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
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:deactivate",
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
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}:deactivate",
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
    functions[
        "advertisersLineItemsBulkEditAssignedTargetingOptions"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsGenerateDefault"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsDelete"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsBulkUpdate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsDuplicate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsBulkListAssignedTargetingOptions"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems:bulkListAssignedTargetingOptions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "lineItemIds": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BulkListAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "assignedTargetingOptionId": t.string(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersDelete"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersListAssignedTargetingOptions"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "advertiserId": t.string(),
                "insertionOrderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "insertionOrderId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "insertionOrderId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "insertionOrderId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "insertionOrderId": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInsertionOrderAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsList"] = displayvideo.post(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "customBiddingAlgorithmType": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "entityStatus": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
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
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "entityStatus": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
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
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "entityStatus": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
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
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "entityStatus": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
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
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "entityStatus": t.string().optional(),
                "sharedAdvertiserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingAlgorithmOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsCreate"] = displayvideo.get(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts/{customBiddingScriptId}",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "customBiddingScriptId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingScriptOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsList"] = displayvideo.get(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts/{customBiddingScriptId}",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "customBiddingScriptId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingScriptOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsGet"] = displayvideo.get(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts/{customBiddingScriptId}",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "customBiddingScriptId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomBiddingScriptOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customListsList"] = displayvideo.get(
        "v2/customLists/{customListId}",
        t.struct(
            {
                "customListId": t.string(),
                "advertiserId": t.string().optional(),
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
                "customListId": t.string(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersPatch"] = displayvideo.get(
        "v2/users",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersCreate"] = displayvideo.get(
        "v2/users",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersBulkEditAssignedUserRoles"] = displayvideo.get(
        "v2/users",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGet"] = displayvideo.get(
        "v2/users",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = displayvideo.get(
        "v2/users",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = displayvideo.get(
        "v2/users",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsDelete"] = displayvideo.post(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsPatch"] = displayvideo.post(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsGet"] = displayvideo.post(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsList"] = displayvideo.post(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsCreate"] = displayvideo.post(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "advertiserId": t.string().optional(),
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
                "partnerId": t.string().optional(),
                "inventorySourceGroupId": t.string(),
                "advertiserId": t.string().optional(),
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
                "partnerId": t.string().optional(),
                "inventorySourceGroupId": t.string(),
                "advertiserId": t.string().optional(),
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
                "partnerId": t.string().optional(),
                "inventorySourceGroupId": t.string(),
                "advertiserId": t.string().optional(),
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
                "partnerId": t.string().optional(),
                "inventorySourceGroupId": t.string(),
                "advertiserId": t.string().optional(),
                "inventorySourceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedInventorySourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["combinedAudiencesGet"] = displayvideo.get(
        "v2/combinedAudiences",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCombinedAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sdfdownloadtasksCreate"] = displayvideo.post(
        "v2/sdfdownloadtasks",
        t.struct(
            {
                "version": t.string(),
                "parentEntityFilter": t.proxy(
                    renames["ParentEntityFilterIn"]
                ).optional(),
                "inventorySourceFilter": t.proxy(
                    renames["InventorySourceFilterIn"]
                ).optional(),
                "idFilter": t.proxy(renames["IdFilterIn"]).optional(),
                "partnerId": t.string().optional(),
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
    functions["targetingTypesTargetingOptionsList"] = displayvideo.post(
        "v2/targetingTypes/{targetingType}/targetingOptions:search",
        t.struct(
            {
                "targetingType": t.string(),
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
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
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
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
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesCreate"] = displayvideo.get(
        "v2/inventorySources",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesGet"] = displayvideo.get(
        "v2/inventorySources",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersList"] = displayvideo.post(
        "v2/guaranteedOrders/{guaranteedOrderId}:editGuaranteedOrderReadAccessors",
        t.struct(
            {
                "guaranteedOrderId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
                "partnerId": t.string(),
                "readAccessInherited": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditGuaranteedOrderReadAccessorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersGet"] = displayvideo.post(
        "v2/guaranteedOrders/{guaranteedOrderId}:editGuaranteedOrderReadAccessors",
        t.struct(
            {
                "guaranteedOrderId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
                "partnerId": t.string(),
                "readAccessInherited": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditGuaranteedOrderReadAccessorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersCreate"] = displayvideo.post(
        "v2/guaranteedOrders/{guaranteedOrderId}:editGuaranteedOrderReadAccessors",
        t.struct(
            {
                "guaranteedOrderId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
                "partnerId": t.string(),
                "readAccessInherited": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditGuaranteedOrderReadAccessorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersPatch"] = displayvideo.post(
        "v2/guaranteedOrders/{guaranteedOrderId}:editGuaranteedOrderReadAccessors",
        t.struct(
            {
                "guaranteedOrderId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
                "partnerId": t.string(),
                "readAccessInherited": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditGuaranteedOrderReadAccessorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersEditGuaranteedOrderReadAccessors"] = displayvideo.post(
        "v2/guaranteedOrders/{guaranteedOrderId}:editGuaranteedOrderReadAccessors",
        t.struct(
            {
                "guaranteedOrderId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
                "partnerId": t.string(),
                "readAccessInherited": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditGuaranteedOrderReadAccessorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesPatch"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string(),
                "appId": t.string().optional(),
                "firstAndThirdPartyAudienceType": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "membershipDurationDays": t.string().optional(),
                "audienceType": t.string().optional(),
                "mobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FirstAndThirdPartyAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "firstAndThirdPartyAudiencesEditCustomerMatchMembers"
    ] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string(),
                "appId": t.string().optional(),
                "firstAndThirdPartyAudienceType": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "membershipDurationDays": t.string().optional(),
                "audienceType": t.string().optional(),
                "mobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FirstAndThirdPartyAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesGet"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string(),
                "appId": t.string().optional(),
                "firstAndThirdPartyAudienceType": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "membershipDurationDays": t.string().optional(),
                "audienceType": t.string().optional(),
                "mobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FirstAndThirdPartyAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesList"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string(),
                "appId": t.string().optional(),
                "firstAndThirdPartyAudienceType": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "membershipDurationDays": t.string().optional(),
                "audienceType": t.string().optional(),
                "mobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FirstAndThirdPartyAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesCreate"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences",
        t.struct(
            {
                "advertiserId": t.string(),
                "appId": t.string().optional(),
                "firstAndThirdPartyAudienceType": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "membershipDurationDays": t.string().optional(),
                "audienceType": t.string().optional(),
                "mobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FirstAndThirdPartyAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="displayvideo",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
