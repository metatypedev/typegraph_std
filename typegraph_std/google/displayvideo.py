from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_displayvideo() -> Import:
    displayvideo = HTTPRuntime("https://displayvideo.googleapis.com/")

    renames = {
        "ErrorResponse": "_displayvideo_1_ErrorResponse",
        "CustomListIn": "_displayvideo_2_CustomListIn",
        "CustomListOut": "_displayvideo_3_CustomListOut",
        "BulkEditAssignedTargetingOptionsRequestIn": "_displayvideo_4_BulkEditAssignedTargetingOptionsRequestIn",
        "BulkEditAssignedTargetingOptionsRequestOut": "_displayvideo_5_BulkEditAssignedTargetingOptionsRequestOut",
        "AdvertiserBillingConfigIn": "_displayvideo_6_AdvertiserBillingConfigIn",
        "AdvertiserBillingConfigOut": "_displayvideo_7_AdvertiserBillingConfigOut",
        "ListInsertionOrdersResponseIn": "_displayvideo_8_ListInsertionOrdersResponseIn",
        "ListInsertionOrdersResponseOut": "_displayvideo_9_ListInsertionOrdersResponseOut",
        "BulkEditAssignedInventorySourcesResponseIn": "_displayvideo_10_BulkEditAssignedInventorySourcesResponseIn",
        "BulkEditAssignedInventorySourcesResponseOut": "_displayvideo_11_BulkEditAssignedInventorySourcesResponseOut",
        "LanguageAssignedTargetingOptionDetailsIn": "_displayvideo_12_LanguageAssignedTargetingOptionDetailsIn",
        "LanguageAssignedTargetingOptionDetailsOut": "_displayvideo_13_LanguageAssignedTargetingOptionDetailsOut",
        "PartnerAdServerConfigIn": "_displayvideo_14_PartnerAdServerConfigIn",
        "PartnerAdServerConfigOut": "_displayvideo_15_PartnerAdServerConfigOut",
        "BulkListAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_16_BulkListAdvertiserAssignedTargetingOptionsResponseIn",
        "BulkListAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_17_BulkListAdvertiserAssignedTargetingOptionsResponseOut",
        "DisplayVideoSourceAdIn": "_displayvideo_18_DisplayVideoSourceAdIn",
        "DisplayVideoSourceAdOut": "_displayvideo_19_DisplayVideoSourceAdOut",
        "CampaignGoalIn": "_displayvideo_20_CampaignGoalIn",
        "CampaignGoalOut": "_displayvideo_21_CampaignGoalOut",
        "PoiSearchTermsIn": "_displayvideo_22_PoiSearchTermsIn",
        "PoiSearchTermsOut": "_displayvideo_23_PoiSearchTermsOut",
        "ContentGenreAssignedTargetingOptionDetailsIn": "_displayvideo_24_ContentGenreAssignedTargetingOptionDetailsIn",
        "ContentGenreAssignedTargetingOptionDetailsOut": "_displayvideo_25_ContentGenreAssignedTargetingOptionDetailsOut",
        "PoiTargetingOptionDetailsIn": "_displayvideo_26_PoiTargetingOptionDetailsIn",
        "PoiTargetingOptionDetailsOut": "_displayvideo_27_PoiTargetingOptionDetailsOut",
        "DeviceTypeAssignedTargetingOptionDetailsIn": "_displayvideo_28_DeviceTypeAssignedTargetingOptionDetailsIn",
        "DeviceTypeAssignedTargetingOptionDetailsOut": "_displayvideo_29_DeviceTypeAssignedTargetingOptionDetailsOut",
        "YoutubeAndPartnersInventorySourceConfigIn": "_displayvideo_30_YoutubeAndPartnersInventorySourceConfigIn",
        "YoutubeAndPartnersInventorySourceConfigOut": "_displayvideo_31_YoutubeAndPartnersInventorySourceConfigOut",
        "EmptyIn": "_displayvideo_32_EmptyIn",
        "EmptyOut": "_displayvideo_33_EmptyOut",
        "ExchangeReviewStatusIn": "_displayvideo_34_ExchangeReviewStatusIn",
        "ExchangeReviewStatusOut": "_displayvideo_35_ExchangeReviewStatusOut",
        "ListCampaignsResponseIn": "_displayvideo_36_ListCampaignsResponseIn",
        "ListCampaignsResponseOut": "_displayvideo_37_ListCampaignsResponseOut",
        "ListAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_38_ListAdvertiserAssignedTargetingOptionsResponseIn",
        "ListAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_39_ListAdvertiserAssignedTargetingOptionsResponseOut",
        "ListLocationListsResponseIn": "_displayvideo_40_ListLocationListsResponseIn",
        "ListLocationListsResponseOut": "_displayvideo_41_ListLocationListsResponseOut",
        "AgeRangeAssignedTargetingOptionDetailsIn": "_displayvideo_42_AgeRangeAssignedTargetingOptionDetailsIn",
        "AgeRangeAssignedTargetingOptionDetailsOut": "_displayvideo_43_AgeRangeAssignedTargetingOptionDetailsOut",
        "PerformanceGoalBidStrategyIn": "_displayvideo_44_PerformanceGoalBidStrategyIn",
        "PerformanceGoalBidStrategyOut": "_displayvideo_45_PerformanceGoalBidStrategyOut",
        "GoogleAudienceIn": "_displayvideo_46_GoogleAudienceIn",
        "GoogleAudienceOut": "_displayvideo_47_GoogleAudienceOut",
        "SdfDownloadTaskMetadataIn": "_displayvideo_48_SdfDownloadTaskMetadataIn",
        "SdfDownloadTaskMetadataOut": "_displayvideo_49_SdfDownloadTaskMetadataOut",
        "ParentalStatusTargetingOptionDetailsIn": "_displayvideo_50_ParentalStatusTargetingOptionDetailsIn",
        "ParentalStatusTargetingOptionDetailsOut": "_displayvideo_51_ParentalStatusTargetingOptionDetailsOut",
        "SdfConfigIn": "_displayvideo_52_SdfConfigIn",
        "SdfConfigOut": "_displayvideo_53_SdfConfigOut",
        "PartnerGeneralConfigIn": "_displayvideo_54_PartnerGeneralConfigIn",
        "PartnerGeneralConfigOut": "_displayvideo_55_PartnerGeneralConfigOut",
        "ListFirstAndThirdPartyAudiencesResponseIn": "_displayvideo_56_ListFirstAndThirdPartyAudiencesResponseIn",
        "ListFirstAndThirdPartyAudiencesResponseOut": "_displayvideo_57_ListFirstAndThirdPartyAudiencesResponseOut",
        "KeywordAssignedTargetingOptionDetailsIn": "_displayvideo_58_KeywordAssignedTargetingOptionDetailsIn",
        "KeywordAssignedTargetingOptionDetailsOut": "_displayvideo_59_KeywordAssignedTargetingOptionDetailsOut",
        "OnScreenPositionTargetingOptionDetailsIn": "_displayvideo_60_OnScreenPositionTargetingOptionDetailsIn",
        "OnScreenPositionTargetingOptionDetailsOut": "_displayvideo_61_OnScreenPositionTargetingOptionDetailsOut",
        "AssignedInventorySourceIn": "_displayvideo_62_AssignedInventorySourceIn",
        "AssignedInventorySourceOut": "_displayvideo_63_AssignedInventorySourceOut",
        "ListCreativesResponseIn": "_displayvideo_64_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_displayvideo_65_ListCreativesResponseOut",
        "BudgetSummaryIn": "_displayvideo_66_BudgetSummaryIn",
        "BudgetSummaryOut": "_displayvideo_67_BudgetSummaryOut",
        "DeviceTypeTargetingOptionDetailsIn": "_displayvideo_68_DeviceTypeTargetingOptionDetailsIn",
        "DeviceTypeTargetingOptionDetailsOut": "_displayvideo_69_DeviceTypeTargetingOptionDetailsOut",
        "BulkUpdateLineItemsRequestIn": "_displayvideo_70_BulkUpdateLineItemsRequestIn",
        "BulkUpdateLineItemsRequestOut": "_displayvideo_71_BulkUpdateLineItemsRequestOut",
        "PartnerCostIn": "_displayvideo_72_PartnerCostIn",
        "PartnerCostOut": "_displayvideo_73_PartnerCostOut",
        "ListTargetingOptionsResponseIn": "_displayvideo_74_ListTargetingOptionsResponseIn",
        "ListTargetingOptionsResponseOut": "_displayvideo_75_ListTargetingOptionsResponseOut",
        "ParentEntityFilterIn": "_displayvideo_76_ParentEntityFilterIn",
        "ParentEntityFilterOut": "_displayvideo_77_ParentEntityFilterOut",
        "ContentInstreamPositionTargetingOptionDetailsIn": "_displayvideo_78_ContentInstreamPositionTargetingOptionDetailsIn",
        "ContentInstreamPositionTargetingOptionDetailsOut": "_displayvideo_79_ContentInstreamPositionTargetingOptionDetailsOut",
        "ContentOutstreamPositionTargetingOptionDetailsIn": "_displayvideo_80_ContentOutstreamPositionTargetingOptionDetailsIn",
        "ContentOutstreamPositionTargetingOptionDetailsOut": "_displayvideo_81_ContentOutstreamPositionTargetingOptionDetailsOut",
        "GoogleBytestreamMediaIn": "_displayvideo_82_GoogleBytestreamMediaIn",
        "GoogleBytestreamMediaOut": "_displayvideo_83_GoogleBytestreamMediaOut",
        "CarrierAndIspTargetingOptionDetailsIn": "_displayvideo_84_CarrierAndIspTargetingOptionDetailsIn",
        "CarrierAndIspTargetingOptionDetailsOut": "_displayvideo_85_CarrierAndIspTargetingOptionDetailsOut",
        "AppAssignedTargetingOptionDetailsIn": "_displayvideo_86_AppAssignedTargetingOptionDetailsIn",
        "AppAssignedTargetingOptionDetailsOut": "_displayvideo_87_AppAssignedTargetingOptionDetailsOut",
        "MobileDeviceIdListIn": "_displayvideo_88_MobileDeviceIdListIn",
        "MobileDeviceIdListOut": "_displayvideo_89_MobileDeviceIdListOut",
        "LineItemIn": "_displayvideo_90_LineItemIn",
        "LineItemOut": "_displayvideo_91_LineItemOut",
        "InStreamAdIn": "_displayvideo_92_InStreamAdIn",
        "InStreamAdOut": "_displayvideo_93_InStreamAdOut",
        "GuaranteedOrderIn": "_displayvideo_94_GuaranteedOrderIn",
        "GuaranteedOrderOut": "_displayvideo_95_GuaranteedOrderOut",
        "CombinedAudienceGroupIn": "_displayvideo_96_CombinedAudienceGroupIn",
        "CombinedAudienceGroupOut": "_displayvideo_97_CombinedAudienceGroupOut",
        "GuaranteedOrderStatusIn": "_displayvideo_98_GuaranteedOrderStatusIn",
        "GuaranteedOrderStatusOut": "_displayvideo_99_GuaranteedOrderStatusOut",
        "IdFilterIn": "_displayvideo_100_IdFilterIn",
        "IdFilterOut": "_displayvideo_101_IdFilterOut",
        "EditCustomerMatchMembersResponseIn": "_displayvideo_102_EditCustomerMatchMembersResponseIn",
        "EditCustomerMatchMembersResponseOut": "_displayvideo_103_EditCustomerMatchMembersResponseOut",
        "InsertionOrderIn": "_displayvideo_104_InsertionOrderIn",
        "InsertionOrderOut": "_displayvideo_105_InsertionOrderOut",
        "BusinessChainAssignedTargetingOptionDetailsIn": "_displayvideo_106_BusinessChainAssignedTargetingOptionDetailsIn",
        "BusinessChainAssignedTargetingOptionDetailsOut": "_displayvideo_107_BusinessChainAssignedTargetingOptionDetailsOut",
        "FirstAndThirdPartyAudienceTargetingSettingIn": "_displayvideo_108_FirstAndThirdPartyAudienceTargetingSettingIn",
        "FirstAndThirdPartyAudienceTargetingSettingOut": "_displayvideo_109_FirstAndThirdPartyAudienceTargetingSettingOut",
        "VideoAdSequenceStepIn": "_displayvideo_110_VideoAdSequenceStepIn",
        "VideoAdSequenceStepOut": "_displayvideo_111_VideoAdSequenceStepOut",
        "AgeRangeTargetingOptionDetailsIn": "_displayvideo_112_AgeRangeTargetingOptionDetailsIn",
        "AgeRangeTargetingOptionDetailsOut": "_displayvideo_113_AgeRangeTargetingOptionDetailsOut",
        "AudienceGroupAssignedTargetingOptionDetailsIn": "_displayvideo_114_AudienceGroupAssignedTargetingOptionDetailsIn",
        "AudienceGroupAssignedTargetingOptionDetailsOut": "_displayvideo_115_AudienceGroupAssignedTargetingOptionDetailsOut",
        "IntegralAdScienceIn": "_displayvideo_116_IntegralAdScienceIn",
        "IntegralAdScienceOut": "_displayvideo_117_IntegralAdScienceOut",
        "CmHybridConfigIn": "_displayvideo_118_CmHybridConfigIn",
        "CmHybridConfigOut": "_displayvideo_119_CmHybridConfigOut",
        "PoiAssignedTargetingOptionDetailsIn": "_displayvideo_120_PoiAssignedTargetingOptionDetailsIn",
        "PoiAssignedTargetingOptionDetailsOut": "_displayvideo_121_PoiAssignedTargetingOptionDetailsOut",
        "ListNegativeKeywordListsResponseIn": "_displayvideo_122_ListNegativeKeywordListsResponseIn",
        "ListNegativeKeywordListsResponseOut": "_displayvideo_123_ListNegativeKeywordListsResponseOut",
        "LocationListIn": "_displayvideo_124_LocationListIn",
        "LocationListOut": "_displayvideo_125_LocationListOut",
        "LineItemBudgetIn": "_displayvideo_126_LineItemBudgetIn",
        "LineItemBudgetOut": "_displayvideo_127_LineItemBudgetOut",
        "InventorySourceDisplayCreativeConfigIn": "_displayvideo_128_InventorySourceDisplayCreativeConfigIn",
        "InventorySourceDisplayCreativeConfigOut": "_displayvideo_129_InventorySourceDisplayCreativeConfigOut",
        "VideoPerformanceAdIn": "_displayvideo_130_VideoPerformanceAdIn",
        "VideoPerformanceAdOut": "_displayvideo_131_VideoPerformanceAdOut",
        "ContentGenreTargetingOptionDetailsIn": "_displayvideo_132_ContentGenreTargetingOptionDetailsIn",
        "ContentGenreTargetingOptionDetailsOut": "_displayvideo_133_ContentGenreTargetingOptionDetailsOut",
        "EnvironmentAssignedTargetingOptionDetailsIn": "_displayvideo_134_EnvironmentAssignedTargetingOptionDetailsIn",
        "EnvironmentAssignedTargetingOptionDetailsOut": "_displayvideo_135_EnvironmentAssignedTargetingOptionDetailsOut",
        "PerformanceGoalIn": "_displayvideo_136_PerformanceGoalIn",
        "PerformanceGoalOut": "_displayvideo_137_PerformanceGoalOut",
        "CreateAssignedTargetingOptionsRequestIn": "_displayvideo_138_CreateAssignedTargetingOptionsRequestIn",
        "CreateAssignedTargetingOptionsRequestOut": "_displayvideo_139_CreateAssignedTargetingOptionsRequestOut",
        "GeoRegionSearchTermsIn": "_displayvideo_140_GeoRegionSearchTermsIn",
        "GeoRegionSearchTermsOut": "_displayvideo_141_GeoRegionSearchTermsOut",
        "YoutubeAndPartnersBiddingStrategyIn": "_displayvideo_142_YoutubeAndPartnersBiddingStrategyIn",
        "YoutubeAndPartnersBiddingStrategyOut": "_displayvideo_143_YoutubeAndPartnersBiddingStrategyOut",
        "InventorySourceIn": "_displayvideo_144_InventorySourceIn",
        "InventorySourceOut": "_displayvideo_145_InventorySourceOut",
        "CustomLabelIn": "_displayvideo_146_CustomLabelIn",
        "CustomLabelOut": "_displayvideo_147_CustomLabelOut",
        "AppCategoryAssignedTargetingOptionDetailsIn": "_displayvideo_148_AppCategoryAssignedTargetingOptionDetailsIn",
        "AppCategoryAssignedTargetingOptionDetailsOut": "_displayvideo_149_AppCategoryAssignedTargetingOptionDetailsOut",
        "ProductFeedDataIn": "_displayvideo_150_ProductFeedDataIn",
        "ProductFeedDataOut": "_displayvideo_151_ProductFeedDataOut",
        "EditInventorySourceReadWriteAccessorsRequestIn": "_displayvideo_152_EditInventorySourceReadWriteAccessorsRequestIn",
        "EditInventorySourceReadWriteAccessorsRequestOut": "_displayvideo_153_EditInventorySourceReadWriteAccessorsRequestOut",
        "RegionalLocationListAssignedTargetingOptionDetailsIn": "_displayvideo_154_RegionalLocationListAssignedTargetingOptionDetailsIn",
        "RegionalLocationListAssignedTargetingOptionDetailsOut": "_displayvideo_155_RegionalLocationListAssignedTargetingOptionDetailsOut",
        "CreativeIn": "_displayvideo_156_CreativeIn",
        "CreativeOut": "_displayvideo_157_CreativeOut",
        "ListLineItemAssignedTargetingOptionsResponseIn": "_displayvideo_158_ListLineItemAssignedTargetingOptionsResponseIn",
        "ListLineItemAssignedTargetingOptionsResponseOut": "_displayvideo_159_ListLineItemAssignedTargetingOptionsResponseOut",
        "ViewabilityAssignedTargetingOptionDetailsIn": "_displayvideo_160_ViewabilityAssignedTargetingOptionDetailsIn",
        "ViewabilityAssignedTargetingOptionDetailsOut": "_displayvideo_161_ViewabilityAssignedTargetingOptionDetailsOut",
        "BulkListAdGroupAssignedTargetingOptionsResponseIn": "_displayvideo_162_BulkListAdGroupAssignedTargetingOptionsResponseIn",
        "BulkListAdGroupAssignedTargetingOptionsResponseOut": "_displayvideo_163_BulkListAdGroupAssignedTargetingOptionsResponseOut",
        "BulkEditAdvertiserAssignedTargetingOptionsRequestIn": "_displayvideo_164_BulkEditAdvertiserAssignedTargetingOptionsRequestIn",
        "BulkEditAdvertiserAssignedTargetingOptionsRequestOut": "_displayvideo_165_BulkEditAdvertiserAssignedTargetingOptionsRequestOut",
        "CategoryTargetingOptionDetailsIn": "_displayvideo_166_CategoryTargetingOptionDetailsIn",
        "CategoryTargetingOptionDetailsOut": "_displayvideo_167_CategoryTargetingOptionDetailsOut",
        "CampaignBudgetIn": "_displayvideo_168_CampaignBudgetIn",
        "CampaignBudgetOut": "_displayvideo_169_CampaignBudgetOut",
        "CategoryAssignedTargetingOptionDetailsIn": "_displayvideo_170_CategoryAssignedTargetingOptionDetailsIn",
        "CategoryAssignedTargetingOptionDetailsOut": "_displayvideo_171_CategoryAssignedTargetingOptionDetailsOut",
        "FixedBidStrategyIn": "_displayvideo_172_FixedBidStrategyIn",
        "FixedBidStrategyOut": "_displayvideo_173_FixedBidStrategyOut",
        "ListCampaignAssignedTargetingOptionsResponseIn": "_displayvideo_174_ListCampaignAssignedTargetingOptionsResponseIn",
        "ListCampaignAssignedTargetingOptionsResponseOut": "_displayvideo_175_ListCampaignAssignedTargetingOptionsResponseOut",
        "TimerEventIn": "_displayvideo_176_TimerEventIn",
        "TimerEventOut": "_displayvideo_177_TimerEventOut",
        "TrackingFloodlightActivityConfigIn": "_displayvideo_178_TrackingFloodlightActivityConfigIn",
        "TrackingFloodlightActivityConfigOut": "_displayvideo_179_TrackingFloodlightActivityConfigOut",
        "LookupInvoiceCurrencyResponseIn": "_displayvideo_180_LookupInvoiceCurrencyResponseIn",
        "LookupInvoiceCurrencyResponseOut": "_displayvideo_181_LookupInvoiceCurrencyResponseOut",
        "YoutubeAdGroupIn": "_displayvideo_182_YoutubeAdGroupIn",
        "YoutubeAdGroupOut": "_displayvideo_183_YoutubeAdGroupOut",
        "AudioAdIn": "_displayvideo_184_AudioAdIn",
        "AudioAdOut": "_displayvideo_185_AudioAdOut",
        "DeleteAssignedTargetingOptionsRequestIn": "_displayvideo_186_DeleteAssignedTargetingOptionsRequestIn",
        "DeleteAssignedTargetingOptionsRequestOut": "_displayvideo_187_DeleteAssignedTargetingOptionsRequestOut",
        "DeviceMakeModelTargetingOptionDetailsIn": "_displayvideo_188_DeviceMakeModelTargetingOptionDetailsIn",
        "DeviceMakeModelTargetingOptionDetailsOut": "_displayvideo_189_DeviceMakeModelTargetingOptionDetailsOut",
        "ListYoutubeAdGroupAdsResponseIn": "_displayvideo_190_ListYoutubeAdGroupAdsResponseIn",
        "ListYoutubeAdGroupAdsResponseOut": "_displayvideo_191_ListYoutubeAdGroupAdsResponseOut",
        "ScriptErrorIn": "_displayvideo_192_ScriptErrorIn",
        "ScriptErrorOut": "_displayvideo_193_ScriptErrorOut",
        "ContentDurationTargetingOptionDetailsIn": "_displayvideo_194_ContentDurationTargetingOptionDetailsIn",
        "ContentDurationTargetingOptionDetailsOut": "_displayvideo_195_ContentDurationTargetingOptionDetailsOut",
        "BulkEditSitesRequestIn": "_displayvideo_196_BulkEditSitesRequestIn",
        "BulkEditSitesRequestOut": "_displayvideo_197_BulkEditSitesRequestOut",
        "BulkListCampaignAssignedTargetingOptionsResponseIn": "_displayvideo_198_BulkListCampaignAssignedTargetingOptionsResponseIn",
        "BulkListCampaignAssignedTargetingOptionsResponseOut": "_displayvideo_199_BulkListCampaignAssignedTargetingOptionsResponseOut",
        "ListCustomListsResponseIn": "_displayvideo_200_ListCustomListsResponseIn",
        "ListCustomListsResponseOut": "_displayvideo_201_ListCustomListsResponseOut",
        "DimensionsIn": "_displayvideo_202_DimensionsIn",
        "DimensionsOut": "_displayvideo_203_DimensionsOut",
        "CustomBiddingModelDetailsIn": "_displayvideo_204_CustomBiddingModelDetailsIn",
        "CustomBiddingModelDetailsOut": "_displayvideo_205_CustomBiddingModelDetailsOut",
        "PartnerIn": "_displayvideo_206_PartnerIn",
        "PartnerOut": "_displayvideo_207_PartnerOut",
        "CustomBiddingScriptIn": "_displayvideo_208_CustomBiddingScriptIn",
        "CustomBiddingScriptOut": "_displayvideo_209_CustomBiddingScriptOut",
        "BulkListInsertionOrderAssignedTargetingOptionsResponseIn": "_displayvideo_210_BulkListInsertionOrderAssignedTargetingOptionsResponseIn",
        "BulkListInsertionOrderAssignedTargetingOptionsResponseOut": "_displayvideo_211_BulkListInsertionOrderAssignedTargetingOptionsResponseOut",
        "InventorySourceGroupIn": "_displayvideo_212_InventorySourceGroupIn",
        "InventorySourceGroupOut": "_displayvideo_213_InventorySourceGroupOut",
        "EditCustomerMatchMembersRequestIn": "_displayvideo_214_EditCustomerMatchMembersRequestIn",
        "EditCustomerMatchMembersRequestOut": "_displayvideo_215_EditCustomerMatchMembersRequestOut",
        "BulkEditSitesResponseIn": "_displayvideo_216_BulkEditSitesResponseIn",
        "BulkEditSitesResponseOut": "_displayvideo_217_BulkEditSitesResponseOut",
        "CustomBiddingScriptRefIn": "_displayvideo_218_CustomBiddingScriptRefIn",
        "CustomBiddingScriptRefOut": "_displayvideo_219_CustomBiddingScriptRefOut",
        "BulkEditAssignedLocationsRequestIn": "_displayvideo_220_BulkEditAssignedLocationsRequestIn",
        "BulkEditAssignedLocationsRequestOut": "_displayvideo_221_BulkEditAssignedLocationsRequestOut",
        "ListYoutubeAdGroupAssignedTargetingOptionsResponseIn": "_displayvideo_222_ListYoutubeAdGroupAssignedTargetingOptionsResponseIn",
        "ListYoutubeAdGroupAssignedTargetingOptionsResponseOut": "_displayvideo_223_ListYoutubeAdGroupAssignedTargetingOptionsResponseOut",
        "SubExchangeAssignedTargetingOptionDetailsIn": "_displayvideo_224_SubExchangeAssignedTargetingOptionDetailsIn",
        "SubExchangeAssignedTargetingOptionDetailsOut": "_displayvideo_225_SubExchangeAssignedTargetingOptionDetailsOut",
        "ContactInfoListIn": "_displayvideo_226_ContactInfoListIn",
        "ContactInfoListOut": "_displayvideo_227_ContactInfoListOut",
        "PublisherReviewStatusIn": "_displayvideo_228_PublisherReviewStatusIn",
        "PublisherReviewStatusOut": "_displayvideo_229_PublisherReviewStatusOut",
        "AssetAssociationIn": "_displayvideo_230_AssetAssociationIn",
        "AssetAssociationOut": "_displayvideo_231_AssetAssociationOut",
        "ManualTriggerIn": "_displayvideo_232_ManualTriggerIn",
        "ManualTriggerOut": "_displayvideo_233_ManualTriggerOut",
        "MaximizeSpendBidStrategyIn": "_displayvideo_234_MaximizeSpendBidStrategyIn",
        "MaximizeSpendBidStrategyOut": "_displayvideo_235_MaximizeSpendBidStrategyOut",
        "ListInventorySourceGroupsResponseIn": "_displayvideo_236_ListInventorySourceGroupsResponseIn",
        "ListInventorySourceGroupsResponseOut": "_displayvideo_237_ListInventorySourceGroupsResponseOut",
        "ContentDurationAssignedTargetingOptionDetailsIn": "_displayvideo_238_ContentDurationAssignedTargetingOptionDetailsIn",
        "ContentDurationAssignedTargetingOptionDetailsOut": "_displayvideo_239_ContentDurationAssignedTargetingOptionDetailsOut",
        "InventorySourceGroupAssignedTargetingOptionDetailsIn": "_displayvideo_240_InventorySourceGroupAssignedTargetingOptionDetailsIn",
        "InventorySourceGroupAssignedTargetingOptionDetailsOut": "_displayvideo_241_InventorySourceGroupAssignedTargetingOptionDetailsOut",
        "ReplaceNegativeKeywordsRequestIn": "_displayvideo_242_ReplaceNegativeKeywordsRequestIn",
        "ReplaceNegativeKeywordsRequestOut": "_displayvideo_243_ReplaceNegativeKeywordsRequestOut",
        "ListYoutubeAdGroupsResponseIn": "_displayvideo_244_ListYoutubeAdGroupsResponseIn",
        "ListYoutubeAdGroupsResponseOut": "_displayvideo_245_ListYoutubeAdGroupsResponseOut",
        "ListAdvertisersResponseIn": "_displayvideo_246_ListAdvertisersResponseIn",
        "ListAdvertisersResponseOut": "_displayvideo_247_ListAdvertisersResponseOut",
        "PrismaConfigIn": "_displayvideo_248_PrismaConfigIn",
        "PrismaConfigOut": "_displayvideo_249_PrismaConfigOut",
        "ChannelIn": "_displayvideo_250_ChannelIn",
        "ChannelOut": "_displayvideo_251_ChannelOut",
        "LanguageTargetingOptionDetailsIn": "_displayvideo_252_LanguageTargetingOptionDetailsIn",
        "LanguageTargetingOptionDetailsOut": "_displayvideo_253_LanguageTargetingOptionDetailsOut",
        "AssetIn": "_displayvideo_254_AssetIn",
        "AssetOut": "_displayvideo_255_AssetOut",
        "ListPartnerAssignedTargetingOptionsResponseIn": "_displayvideo_256_ListPartnerAssignedTargetingOptionsResponseIn",
        "ListPartnerAssignedTargetingOptionsResponseOut": "_displayvideo_257_ListPartnerAssignedTargetingOptionsResponseOut",
        "CreateSdfDownloadTaskRequestIn": "_displayvideo_258_CreateSdfDownloadTaskRequestIn",
        "CreateSdfDownloadTaskRequestOut": "_displayvideo_259_CreateSdfDownloadTaskRequestOut",
        "ChannelAssignedTargetingOptionDetailsIn": "_displayvideo_260_ChannelAssignedTargetingOptionDetailsIn",
        "ChannelAssignedTargetingOptionDetailsOut": "_displayvideo_261_ChannelAssignedTargetingOptionDetailsOut",
        "PartnerRevenueModelIn": "_displayvideo_262_PartnerRevenueModelIn",
        "PartnerRevenueModelOut": "_displayvideo_263_PartnerRevenueModelOut",
        "YoutubeAndPartnersThirdPartyMeasurementSettingsIn": "_displayvideo_264_YoutubeAndPartnersThirdPartyMeasurementSettingsIn",
        "YoutubeAndPartnersThirdPartyMeasurementSettingsOut": "_displayvideo_265_YoutubeAndPartnersThirdPartyMeasurementSettingsOut",
        "LineItemFlightIn": "_displayvideo_266_LineItemFlightIn",
        "LineItemFlightOut": "_displayvideo_267_LineItemFlightOut",
        "ListChannelsResponseIn": "_displayvideo_268_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_displayvideo_269_ListChannelsResponseOut",
        "YoutubeChannelAssignedTargetingOptionDetailsIn": "_displayvideo_270_YoutubeChannelAssignedTargetingOptionDetailsIn",
        "YoutubeChannelAssignedTargetingOptionDetailsOut": "_displayvideo_271_YoutubeChannelAssignedTargetingOptionDetailsOut",
        "SensitiveCategoryAssignedTargetingOptionDetailsIn": "_displayvideo_272_SensitiveCategoryAssignedTargetingOptionDetailsIn",
        "SensitiveCategoryAssignedTargetingOptionDetailsOut": "_displayvideo_273_SensitiveCategoryAssignedTargetingOptionDetailsOut",
        "ListLineItemsResponseIn": "_displayvideo_274_ListLineItemsResponseIn",
        "ListLineItemsResponseOut": "_displayvideo_275_ListLineItemsResponseOut",
        "ExchangeConfigIn": "_displayvideo_276_ExchangeConfigIn",
        "ExchangeConfigOut": "_displayvideo_277_ExchangeConfigOut",
        "ListGoogleAudiencesResponseIn": "_displayvideo_278_ListGoogleAudiencesResponseIn",
        "ListGoogleAudiencesResponseOut": "_displayvideo_279_ListGoogleAudiencesResponseOut",
        "ListPartnersResponseIn": "_displayvideo_280_ListPartnersResponseIn",
        "ListPartnersResponseOut": "_displayvideo_281_ListPartnersResponseOut",
        "YoutubeAndPartnersSettingsIn": "_displayvideo_282_YoutubeAndPartnersSettingsIn",
        "YoutubeAndPartnersSettingsOut": "_displayvideo_283_YoutubeAndPartnersSettingsOut",
        "LookbackWindowIn": "_displayvideo_284_LookbackWindowIn",
        "LookbackWindowOut": "_displayvideo_285_LookbackWindowOut",
        "AppCategoryTargetingOptionDetailsIn": "_displayvideo_286_AppCategoryTargetingOptionDetailsIn",
        "AppCategoryTargetingOptionDetailsOut": "_displayvideo_287_AppCategoryTargetingOptionDetailsOut",
        "AdvertiserSdfConfigIn": "_displayvideo_288_AdvertiserSdfConfigIn",
        "AdvertiserSdfConfigOut": "_displayvideo_289_AdvertiserSdfConfigOut",
        "MobileAppIn": "_displayvideo_290_MobileAppIn",
        "MobileAppOut": "_displayvideo_291_MobileAppOut",
        "ListManualTriggersResponseIn": "_displayvideo_292_ListManualTriggersResponseIn",
        "ListManualTriggersResponseOut": "_displayvideo_293_ListManualTriggersResponseOut",
        "ContentInstreamPositionAssignedTargetingOptionDetailsIn": "_displayvideo_294_ContentInstreamPositionAssignedTargetingOptionDetailsIn",
        "ContentInstreamPositionAssignedTargetingOptionDetailsOut": "_displayvideo_295_ContentInstreamPositionAssignedTargetingOptionDetailsOut",
        "FrequencyCapIn": "_displayvideo_296_FrequencyCapIn",
        "FrequencyCapOut": "_displayvideo_297_FrequencyCapOut",
        "AdlooxIn": "_displayvideo_298_AdlooxIn",
        "AdlooxOut": "_displayvideo_299_AdlooxOut",
        "CreateAssetRequestIn": "_displayvideo_300_CreateAssetRequestIn",
        "CreateAssetRequestOut": "_displayvideo_301_CreateAssetRequestOut",
        "ListSitesResponseIn": "_displayvideo_302_ListSitesResponseIn",
        "ListSitesResponseOut": "_displayvideo_303_ListSitesResponseOut",
        "InventorySourceAccessorsIn": "_displayvideo_304_InventorySourceAccessorsIn",
        "InventorySourceAccessorsOut": "_displayvideo_305_InventorySourceAccessorsOut",
        "BulkUpdateLineItemsResponseIn": "_displayvideo_306_BulkUpdateLineItemsResponseIn",
        "BulkUpdateLineItemsResponseOut": "_displayvideo_307_BulkUpdateLineItemsResponseOut",
        "GeoRegionTargetingOptionDetailsIn": "_displayvideo_308_GeoRegionTargetingOptionDetailsIn",
        "GeoRegionTargetingOptionDetailsOut": "_displayvideo_309_GeoRegionTargetingOptionDetailsOut",
        "DoubleVerifyIn": "_displayvideo_310_DoubleVerifyIn",
        "DoubleVerifyOut": "_displayvideo_311_DoubleVerifyOut",
        "RateDetailsIn": "_displayvideo_312_RateDetailsIn",
        "RateDetailsOut": "_displayvideo_313_RateDetailsOut",
        "SearchTargetingOptionsRequestIn": "_displayvideo_314_SearchTargetingOptionsRequestIn",
        "SearchTargetingOptionsRequestOut": "_displayvideo_315_SearchTargetingOptionsRequestOut",
        "BulkEditAdvertiserAssignedTargetingOptionsResponseIn": "_displayvideo_316_BulkEditAdvertiserAssignedTargetingOptionsResponseIn",
        "BulkEditAdvertiserAssignedTargetingOptionsResponseOut": "_displayvideo_317_BulkEditAdvertiserAssignedTargetingOptionsResponseOut",
        "InventorySourceFilterIn": "_displayvideo_318_InventorySourceFilterIn",
        "InventorySourceFilterOut": "_displayvideo_319_InventorySourceFilterOut",
        "BusinessChainTargetingOptionDetailsIn": "_displayvideo_320_BusinessChainTargetingOptionDetailsIn",
        "BusinessChainTargetingOptionDetailsOut": "_displayvideo_321_BusinessChainTargetingOptionDetailsOut",
        "DoubleVerifyVideoViewabilityIn": "_displayvideo_322_DoubleVerifyVideoViewabilityIn",
        "DoubleVerifyVideoViewabilityOut": "_displayvideo_323_DoubleVerifyVideoViewabilityOut",
        "MoneyIn": "_displayvideo_324_MoneyIn",
        "MoneyOut": "_displayvideo_325_MoneyOut",
        "DuplicateLineItemRequestIn": "_displayvideo_326_DuplicateLineItemRequestIn",
        "DuplicateLineItemRequestOut": "_displayvideo_327_DuplicateLineItemRequestOut",
        "TargetingOptionIn": "_displayvideo_328_TargetingOptionIn",
        "TargetingOptionOut": "_displayvideo_329_TargetingOptionOut",
        "HouseholdIncomeAssignedTargetingOptionDetailsIn": "_displayvideo_330_HouseholdIncomeAssignedTargetingOptionDetailsIn",
        "HouseholdIncomeAssignedTargetingOptionDetailsOut": "_displayvideo_331_HouseholdIncomeAssignedTargetingOptionDetailsOut",
        "ProximityLocationListAssignedTargetingOptionDetailsIn": "_displayvideo_332_ProximityLocationListAssignedTargetingOptionDetailsIn",
        "ProximityLocationListAssignedTargetingOptionDetailsOut": "_displayvideo_333_ProximityLocationListAssignedTargetingOptionDetailsOut",
        "ContactInfoIn": "_displayvideo_334_ContactInfoIn",
        "ContactInfoOut": "_displayvideo_335_ContactInfoOut",
        "ThirdPartyOnlyConfigIn": "_displayvideo_336_ThirdPartyOnlyConfigIn",
        "ThirdPartyOnlyConfigOut": "_displayvideo_337_ThirdPartyOnlyConfigOut",
        "CombinedAudienceTargetingSettingIn": "_displayvideo_338_CombinedAudienceTargetingSettingIn",
        "CombinedAudienceTargetingSettingOut": "_displayvideo_339_CombinedAudienceTargetingSettingOut",
        "ContentOutstreamPositionAssignedTargetingOptionDetailsIn": "_displayvideo_340_ContentOutstreamPositionAssignedTargetingOptionDetailsIn",
        "ContentOutstreamPositionAssignedTargetingOptionDetailsOut": "_displayvideo_341_ContentOutstreamPositionAssignedTargetingOptionDetailsOut",
        "GenderTargetingOptionDetailsIn": "_displayvideo_342_GenderTargetingOptionDetailsIn",
        "GenderTargetingOptionDetailsOut": "_displayvideo_343_GenderTargetingOptionDetailsOut",
        "CounterEventIn": "_displayvideo_344_CounterEventIn",
        "CounterEventOut": "_displayvideo_345_CounterEventOut",
        "FirstAndThirdPartyAudienceIn": "_displayvideo_346_FirstAndThirdPartyAudienceIn",
        "FirstAndThirdPartyAudienceOut": "_displayvideo_347_FirstAndThirdPartyAudienceOut",
        "ListCustomBiddingScriptsResponseIn": "_displayvideo_348_ListCustomBiddingScriptsResponseIn",
        "ListCustomBiddingScriptsResponseOut": "_displayvideo_349_ListCustomBiddingScriptsResponseOut",
        "OperatingSystemAssignedTargetingOptionDetailsIn": "_displayvideo_350_OperatingSystemAssignedTargetingOptionDetailsIn",
        "OperatingSystemAssignedTargetingOptionDetailsOut": "_displayvideo_351_OperatingSystemAssignedTargetingOptionDetailsOut",
        "ContentStreamTypeAssignedTargetingOptionDetailsIn": "_displayvideo_352_ContentStreamTypeAssignedTargetingOptionDetailsIn",
        "ContentStreamTypeAssignedTargetingOptionDetailsOut": "_displayvideo_353_ContentStreamTypeAssignedTargetingOptionDetailsOut",
        "ListCustomBiddingAlgorithmsResponseIn": "_displayvideo_354_ListCustomBiddingAlgorithmsResponseIn",
        "ListCustomBiddingAlgorithmsResponseOut": "_displayvideo_355_ListCustomBiddingAlgorithmsResponseOut",
        "EditGuaranteedOrderReadAccessorsRequestIn": "_displayvideo_356_EditGuaranteedOrderReadAccessorsRequestIn",
        "EditGuaranteedOrderReadAccessorsRequestOut": "_displayvideo_357_EditGuaranteedOrderReadAccessorsRequestOut",
        "SdfDownloadTaskIn": "_displayvideo_358_SdfDownloadTaskIn",
        "SdfDownloadTaskOut": "_displayvideo_359_SdfDownloadTaskOut",
        "OperationIn": "_displayvideo_360_OperationIn",
        "OperationOut": "_displayvideo_361_OperationOut",
        "AdvertiserAdServerConfigIn": "_displayvideo_362_AdvertiserAdServerConfigIn",
        "AdvertiserAdServerConfigOut": "_displayvideo_363_AdvertiserAdServerConfigOut",
        "YoutubeVideoDetailsIn": "_displayvideo_364_YoutubeVideoDetailsIn",
        "YoutubeVideoDetailsOut": "_displayvideo_365_YoutubeVideoDetailsOut",
        "AudioContentTypeTargetingOptionDetailsIn": "_displayvideo_366_AudioContentTypeTargetingOptionDetailsIn",
        "AudioContentTypeTargetingOptionDetailsOut": "_displayvideo_367_AudioContentTypeTargetingOptionDetailsOut",
        "ListUsersResponseIn": "_displayvideo_368_ListUsersResponseIn",
        "ListUsersResponseOut": "_displayvideo_369_ListUsersResponseOut",
        "YoutubeVideoAssignedTargetingOptionDetailsIn": "_displayvideo_370_YoutubeVideoAssignedTargetingOptionDetailsIn",
        "YoutubeVideoAssignedTargetingOptionDetailsOut": "_displayvideo_371_YoutubeVideoAssignedTargetingOptionDetailsOut",
        "BiddingStrategyIn": "_displayvideo_372_BiddingStrategyIn",
        "BiddingStrategyOut": "_displayvideo_373_BiddingStrategyOut",
        "StatusIn": "_displayvideo_374_StatusIn",
        "StatusOut": "_displayvideo_375_StatusOut",
        "ReplaceSitesResponseIn": "_displayvideo_376_ReplaceSitesResponseIn",
        "ReplaceSitesResponseOut": "_displayvideo_377_ReplaceSitesResponseOut",
        "AssignedLocationIn": "_displayvideo_378_AssignedLocationIn",
        "AssignedLocationOut": "_displayvideo_379_AssignedLocationOut",
        "ReplaceNegativeKeywordsResponseIn": "_displayvideo_380_ReplaceNegativeKeywordsResponseIn",
        "ReplaceNegativeKeywordsResponseOut": "_displayvideo_381_ReplaceNegativeKeywordsResponseOut",
        "SiteIn": "_displayvideo_382_SiteIn",
        "SiteOut": "_displayvideo_383_SiteOut",
        "AssignedUserRoleIn": "_displayvideo_384_AssignedUserRoleIn",
        "AssignedUserRoleOut": "_displayvideo_385_AssignedUserRoleOut",
        "BulkEditAssignedUserRolesRequestIn": "_displayvideo_386_BulkEditAssignedUserRolesRequestIn",
        "BulkEditAssignedUserRolesRequestOut": "_displayvideo_387_BulkEditAssignedUserRolesRequestOut",
        "GenderAssignedTargetingOptionDetailsIn": "_displayvideo_388_GenderAssignedTargetingOptionDetailsIn",
        "GenderAssignedTargetingOptionDetailsOut": "_displayvideo_389_GenderAssignedTargetingOptionDetailsOut",
        "AdvertiserTargetingConfigIn": "_displayvideo_390_AdvertiserTargetingConfigIn",
        "AdvertiserTargetingConfigOut": "_displayvideo_391_AdvertiserTargetingConfigOut",
        "ListCombinedAudiencesResponseIn": "_displayvideo_392_ListCombinedAudiencesResponseIn",
        "ListCombinedAudiencesResponseOut": "_displayvideo_393_ListCombinedAudiencesResponseOut",
        "CmTrackingAdIn": "_displayvideo_394_CmTrackingAdIn",
        "CmTrackingAdOut": "_displayvideo_395_CmTrackingAdOut",
        "IntegrationDetailsIn": "_displayvideo_396_IntegrationDetailsIn",
        "IntegrationDetailsOut": "_displayvideo_397_IntegrationDetailsOut",
        "DoubleVerifyFraudInvalidTrafficIn": "_displayvideo_398_DoubleVerifyFraudInvalidTrafficIn",
        "DoubleVerifyFraudInvalidTrafficOut": "_displayvideo_399_DoubleVerifyFraudInvalidTrafficOut",
        "CarrierAndIspAssignedTargetingOptionDetailsIn": "_displayvideo_400_CarrierAndIspAssignedTargetingOptionDetailsIn",
        "CarrierAndIspAssignedTargetingOptionDetailsOut": "_displayvideo_401_CarrierAndIspAssignedTargetingOptionDetailsOut",
        "TranscodeIn": "_displayvideo_402_TranscodeIn",
        "TranscodeOut": "_displayvideo_403_TranscodeOut",
        "NegativeKeywordListAssignedTargetingOptionDetailsIn": "_displayvideo_404_NegativeKeywordListAssignedTargetingOptionDetailsIn",
        "NegativeKeywordListAssignedTargetingOptionDetailsOut": "_displayvideo_405_NegativeKeywordListAssignedTargetingOptionDetailsOut",
        "UniversalAdIdIn": "_displayvideo_406_UniversalAdIdIn",
        "UniversalAdIdOut": "_displayvideo_407_UniversalAdIdOut",
        "DigitalContentLabelAssignedTargetingOptionDetailsIn": "_displayvideo_408_DigitalContentLabelAssignedTargetingOptionDetailsIn",
        "DigitalContentLabelAssignedTargetingOptionDetailsOut": "_displayvideo_409_DigitalContentLabelAssignedTargetingOptionDetailsOut",
        "PartnerDataAccessConfigIn": "_displayvideo_410_PartnerDataAccessConfigIn",
        "PartnerDataAccessConfigOut": "_displayvideo_411_PartnerDataAccessConfigOut",
        "LineItemAssignedTargetingOptionIn": "_displayvideo_412_LineItemAssignedTargetingOptionIn",
        "LineItemAssignedTargetingOptionOut": "_displayvideo_413_LineItemAssignedTargetingOptionOut",
        "InvoiceIn": "_displayvideo_414_InvoiceIn",
        "InvoiceOut": "_displayvideo_415_InvoiceOut",
        "CampaignIn": "_displayvideo_416_CampaignIn",
        "CampaignOut": "_displayvideo_417_CampaignOut",
        "NonSkippableAdIn": "_displayvideo_418_NonSkippableAdIn",
        "NonSkippableAdOut": "_displayvideo_419_NonSkippableAdOut",
        "ListNegativeKeywordsResponseIn": "_displayvideo_420_ListNegativeKeywordsResponseIn",
        "ListNegativeKeywordsResponseOut": "_displayvideo_421_ListNegativeKeywordsResponseOut",
        "UrlAssignedTargetingOptionDetailsIn": "_displayvideo_422_UrlAssignedTargetingOptionDetailsIn",
        "UrlAssignedTargetingOptionDetailsOut": "_displayvideo_423_UrlAssignedTargetingOptionDetailsOut",
        "ImageAssetIn": "_displayvideo_424_ImageAssetIn",
        "ImageAssetOut": "_displayvideo_425_ImageAssetOut",
        "BulkEditPartnerAssignedTargetingOptionsResponseIn": "_displayvideo_426_BulkEditPartnerAssignedTargetingOptionsResponseIn",
        "BulkEditPartnerAssignedTargetingOptionsResponseOut": "_displayvideo_427_BulkEditPartnerAssignedTargetingOptionsResponseOut",
        "DateRangeIn": "_displayvideo_428_DateRangeIn",
        "DateRangeOut": "_displayvideo_429_DateRangeOut",
        "ActivateManualTriggerRequestIn": "_displayvideo_430_ActivateManualTriggerRequestIn",
        "ActivateManualTriggerRequestOut": "_displayvideo_431_ActivateManualTriggerRequestOut",
        "ThirdPartyUrlIn": "_displayvideo_432_ThirdPartyUrlIn",
        "ThirdPartyUrlOut": "_displayvideo_433_ThirdPartyUrlOut",
        "ContentStreamTypeTargetingOptionDetailsIn": "_displayvideo_434_ContentStreamTypeTargetingOptionDetailsIn",
        "ContentStreamTypeTargetingOptionDetailsOut": "_displayvideo_435_ContentStreamTypeTargetingOptionDetailsOut",
        "PrismaCpeCodeIn": "_displayvideo_436_PrismaCpeCodeIn",
        "PrismaCpeCodeOut": "_displayvideo_437_PrismaCpeCodeOut",
        "CustomListGroupIn": "_displayvideo_438_CustomListGroupIn",
        "CustomListGroupOut": "_displayvideo_439_CustomListGroupOut",
        "CombinedAudienceIn": "_displayvideo_440_CombinedAudienceIn",
        "CombinedAudienceOut": "_displayvideo_441_CombinedAudienceOut",
        "SessionPositionAssignedTargetingOptionDetailsIn": "_displayvideo_442_SessionPositionAssignedTargetingOptionDetailsIn",
        "SessionPositionAssignedTargetingOptionDetailsOut": "_displayvideo_443_SessionPositionAssignedTargetingOptionDetailsOut",
        "AudioContentTypeAssignedTargetingOptionDetailsIn": "_displayvideo_444_AudioContentTypeAssignedTargetingOptionDetailsIn",
        "AudioContentTypeAssignedTargetingOptionDetailsOut": "_displayvideo_445_AudioContentTypeAssignedTargetingOptionDetailsOut",
        "EditGuaranteedOrderReadAccessorsResponseIn": "_displayvideo_446_EditGuaranteedOrderReadAccessorsResponseIn",
        "EditGuaranteedOrderReadAccessorsResponseOut": "_displayvideo_447_EditGuaranteedOrderReadAccessorsResponseOut",
        "GoogleAudienceGroupIn": "_displayvideo_448_GoogleAudienceGroupIn",
        "GoogleAudienceGroupOut": "_displayvideo_449_GoogleAudienceGroupOut",
        "OmidTargetingOptionDetailsIn": "_displayvideo_450_OmidTargetingOptionDetailsIn",
        "OmidTargetingOptionDetailsOut": "_displayvideo_451_OmidTargetingOptionDetailsOut",
        "SensitiveCategoryTargetingOptionDetailsIn": "_displayvideo_452_SensitiveCategoryTargetingOptionDetailsIn",
        "SensitiveCategoryTargetingOptionDetailsOut": "_displayvideo_453_SensitiveCategoryTargetingOptionDetailsOut",
        "ReplaceSitesRequestIn": "_displayvideo_454_ReplaceSitesRequestIn",
        "ReplaceSitesRequestOut": "_displayvideo_455_ReplaceSitesRequestOut",
        "ListAssignedInventorySourcesResponseIn": "_displayvideo_456_ListAssignedInventorySourcesResponseIn",
        "ListAssignedInventorySourcesResponseOut": "_displayvideo_457_ListAssignedInventorySourcesResponseOut",
        "DayAndTimeAssignedTargetingOptionDetailsIn": "_displayvideo_458_DayAndTimeAssignedTargetingOptionDetailsIn",
        "DayAndTimeAssignedTargetingOptionDetailsOut": "_displayvideo_459_DayAndTimeAssignedTargetingOptionDetailsOut",
        "NativeContentPositionTargetingOptionDetailsIn": "_displayvideo_460_NativeContentPositionTargetingOptionDetailsIn",
        "NativeContentPositionTargetingOptionDetailsOut": "_displayvideo_461_NativeContentPositionTargetingOptionDetailsOut",
        "AdvertiserCreativeConfigIn": "_displayvideo_462_AdvertiserCreativeConfigIn",
        "AdvertiserCreativeConfigOut": "_displayvideo_463_AdvertiserCreativeConfigOut",
        "CustomBiddingAlgorithmIn": "_displayvideo_464_CustomBiddingAlgorithmIn",
        "CustomBiddingAlgorithmOut": "_displayvideo_465_CustomBiddingAlgorithmOut",
        "ListInsertionOrderAssignedTargetingOptionsResponseIn": "_displayvideo_466_ListInsertionOrderAssignedTargetingOptionsResponseIn",
        "ListInsertionOrderAssignedTargetingOptionsResponseOut": "_displayvideo_467_ListInsertionOrderAssignedTargetingOptionsResponseOut",
        "BrowserTargetingOptionDetailsIn": "_displayvideo_468_BrowserTargetingOptionDetailsIn",
        "BrowserTargetingOptionDetailsOut": "_displayvideo_469_BrowserTargetingOptionDetailsOut",
        "EnvironmentTargetingOptionDetailsIn": "_displayvideo_470_EnvironmentTargetingOptionDetailsIn",
        "EnvironmentTargetingOptionDetailsOut": "_displayvideo_471_EnvironmentTargetingOptionDetailsOut",
        "ThirdPartyVerifierAssignedTargetingOptionDetailsIn": "_displayvideo_472_ThirdPartyVerifierAssignedTargetingOptionDetailsIn",
        "ThirdPartyVerifierAssignedTargetingOptionDetailsOut": "_displayvideo_473_ThirdPartyVerifierAssignedTargetingOptionDetailsOut",
        "VideoPlayerSizeAssignedTargetingOptionDetailsIn": "_displayvideo_474_VideoPlayerSizeAssignedTargetingOptionDetailsIn",
        "VideoPlayerSizeAssignedTargetingOptionDetailsOut": "_displayvideo_475_VideoPlayerSizeAssignedTargetingOptionDetailsOut",
        "InventorySourceAccessorsAdvertiserAccessorsIn": "_displayvideo_476_InventorySourceAccessorsAdvertiserAccessorsIn",
        "InventorySourceAccessorsAdvertiserAccessorsOut": "_displayvideo_477_InventorySourceAccessorsAdvertiserAccessorsOut",
        "DeviceMakeModelAssignedTargetingOptionDetailsIn": "_displayvideo_478_DeviceMakeModelAssignedTargetingOptionDetailsIn",
        "DeviceMakeModelAssignedTargetingOptionDetailsOut": "_displayvideo_479_DeviceMakeModelAssignedTargetingOptionDetailsOut",
        "YoutubeAdGroupAdIn": "_displayvideo_480_YoutubeAdGroupAdIn",
        "YoutubeAdGroupAdOut": "_displayvideo_481_YoutubeAdGroupAdOut",
        "GeoRegionAssignedTargetingOptionDetailsIn": "_displayvideo_482_GeoRegionAssignedTargetingOptionDetailsIn",
        "GeoRegionAssignedTargetingOptionDetailsOut": "_displayvideo_483_GeoRegionAssignedTargetingOptionDetailsOut",
        "InsertionOrderBudgetSegmentIn": "_displayvideo_484_InsertionOrderBudgetSegmentIn",
        "InsertionOrderBudgetSegmentOut": "_displayvideo_485_InsertionOrderBudgetSegmentOut",
        "BulkEditAssignedInventorySourcesRequestIn": "_displayvideo_486_BulkEditAssignedInventorySourcesRequestIn",
        "BulkEditAssignedInventorySourcesRequestOut": "_displayvideo_487_BulkEditAssignedInventorySourcesRequestOut",
        "DoubleVerifyDisplayViewabilityIn": "_displayvideo_488_DoubleVerifyDisplayViewabilityIn",
        "DoubleVerifyDisplayViewabilityOut": "_displayvideo_489_DoubleVerifyDisplayViewabilityOut",
        "FloodlightGroupIn": "_displayvideo_490_FloodlightGroupIn",
        "FloodlightGroupOut": "_displayvideo_491_FloodlightGroupOut",
        "CampaignFlightIn": "_displayvideo_492_CampaignFlightIn",
        "CampaignFlightOut": "_displayvideo_493_CampaignFlightOut",
        "AudioVideoOffsetIn": "_displayvideo_494_AudioVideoOffsetIn",
        "AudioVideoOffsetOut": "_displayvideo_495_AudioVideoOffsetOut",
        "AssignedTargetingOptionIn": "_displayvideo_496_AssignedTargetingOptionIn",
        "AssignedTargetingOptionOut": "_displayvideo_497_AssignedTargetingOptionOut",
        "ParentalStatusAssignedTargetingOptionDetailsIn": "_displayvideo_498_ParentalStatusAssignedTargetingOptionDetailsIn",
        "ParentalStatusAssignedTargetingOptionDetailsOut": "_displayvideo_499_ParentalStatusAssignedTargetingOptionDetailsOut",
        "ExchangeTargetingOptionDetailsIn": "_displayvideo_500_ExchangeTargetingOptionDetailsIn",
        "ExchangeTargetingOptionDetailsOut": "_displayvideo_501_ExchangeTargetingOptionDetailsOut",
        "BrowserAssignedTargetingOptionDetailsIn": "_displayvideo_502_BrowserAssignedTargetingOptionDetailsIn",
        "BrowserAssignedTargetingOptionDetailsOut": "_displayvideo_503_BrowserAssignedTargetingOptionDetailsOut",
        "DateIn": "_displayvideo_504_DateIn",
        "DateOut": "_displayvideo_505_DateOut",
        "AdvertiserIn": "_displayvideo_506_AdvertiserIn",
        "AdvertiserOut": "_displayvideo_507_AdvertiserOut",
        "BulkEditAssignedUserRolesResponseIn": "_displayvideo_508_BulkEditAssignedUserRolesResponseIn",
        "BulkEditAssignedUserRolesResponseOut": "_displayvideo_509_BulkEditAssignedUserRolesResponseOut",
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn": "_displayvideo_510_EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn",
        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut": "_displayvideo_511_EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut",
        "AdvertiserDataAccessConfigIn": "_displayvideo_512_AdvertiserDataAccessConfigIn",
        "AdvertiserDataAccessConfigOut": "_displayvideo_513_AdvertiserDataAccessConfigOut",
        "CreateAssetResponseIn": "_displayvideo_514_CreateAssetResponseIn",
        "CreateAssetResponseOut": "_displayvideo_515_CreateAssetResponseOut",
        "AdUrlIn": "_displayvideo_516_AdUrlIn",
        "AdUrlOut": "_displayvideo_517_AdUrlOut",
        "InventorySourceStatusIn": "_displayvideo_518_InventorySourceStatusIn",
        "InventorySourceStatusOut": "_displayvideo_519_InventorySourceStatusOut",
        "NegativeKeywordListIn": "_displayvideo_520_NegativeKeywordListIn",
        "NegativeKeywordListOut": "_displayvideo_521_NegativeKeywordListOut",
        "YoutubeAdGroupAssignedTargetingOptionIn": "_displayvideo_522_YoutubeAdGroupAssignedTargetingOptionIn",
        "YoutubeAdGroupAssignedTargetingOptionOut": "_displayvideo_523_YoutubeAdGroupAssignedTargetingOptionOut",
        "CreativeConfigIn": "_displayvideo_524_CreativeConfigIn",
        "CreativeConfigOut": "_displayvideo_525_CreativeConfigOut",
        "OmidAssignedTargetingOptionDetailsIn": "_displayvideo_526_OmidAssignedTargetingOptionDetailsIn",
        "OmidAssignedTargetingOptionDetailsOut": "_displayvideo_527_OmidAssignedTargetingOptionDetailsOut",
        "ViewabilityTargetingOptionDetailsIn": "_displayvideo_528_ViewabilityTargetingOptionDetailsIn",
        "ViewabilityTargetingOptionDetailsOut": "_displayvideo_529_ViewabilityTargetingOptionDetailsOut",
        "FirstAndThirdPartyAudienceGroupIn": "_displayvideo_530_FirstAndThirdPartyAudienceGroupIn",
        "FirstAndThirdPartyAudienceGroupOut": "_displayvideo_531_FirstAndThirdPartyAudienceGroupOut",
        "OperatingSystemTargetingOptionDetailsIn": "_displayvideo_532_OperatingSystemTargetingOptionDetailsIn",
        "OperatingSystemTargetingOptionDetailsOut": "_displayvideo_533_OperatingSystemTargetingOptionDetailsOut",
        "OnScreenPositionAssignedTargetingOptionDetailsIn": "_displayvideo_534_OnScreenPositionAssignedTargetingOptionDetailsIn",
        "OnScreenPositionAssignedTargetingOptionDetailsOut": "_displayvideo_535_OnScreenPositionAssignedTargetingOptionDetailsOut",
        "InventorySourceAccessorsPartnerAccessorIn": "_displayvideo_536_InventorySourceAccessorsPartnerAccessorIn",
        "InventorySourceAccessorsPartnerAccessorOut": "_displayvideo_537_InventorySourceAccessorsPartnerAccessorOut",
        "MastheadAdIn": "_displayvideo_538_MastheadAdIn",
        "MastheadAdOut": "_displayvideo_539_MastheadAdOut",
        "InsertionOrderBudgetIn": "_displayvideo_540_InsertionOrderBudgetIn",
        "InsertionOrderBudgetOut": "_displayvideo_541_InsertionOrderBudgetOut",
        "ReviewStatusInfoIn": "_displayvideo_542_ReviewStatusInfoIn",
        "ReviewStatusInfoOut": "_displayvideo_543_ReviewStatusInfoOut",
        "AdvertiserGeneralConfigIn": "_displayvideo_544_AdvertiserGeneralConfigIn",
        "AdvertiserGeneralConfigOut": "_displayvideo_545_AdvertiserGeneralConfigOut",
        "DigitalContentLabelTargetingOptionDetailsIn": "_displayvideo_546_DigitalContentLabelTargetingOptionDetailsIn",
        "DigitalContentLabelTargetingOptionDetailsOut": "_displayvideo_547_DigitalContentLabelTargetingOptionDetailsOut",
        "NativeContentPositionAssignedTargetingOptionDetailsIn": "_displayvideo_548_NativeContentPositionAssignedTargetingOptionDetailsIn",
        "NativeContentPositionAssignedTargetingOptionDetailsOut": "_displayvideo_549_NativeContentPositionAssignedTargetingOptionDetailsOut",
        "UserRewardedContentAssignedTargetingOptionDetailsIn": "_displayvideo_550_UserRewardedContentAssignedTargetingOptionDetailsIn",
        "UserRewardedContentAssignedTargetingOptionDetailsOut": "_displayvideo_551_UserRewardedContentAssignedTargetingOptionDetailsOut",
        "BulkEditAssignedLocationsResponseIn": "_displayvideo_552_BulkEditAssignedLocationsResponseIn",
        "BulkEditAssignedLocationsResponseOut": "_displayvideo_553_BulkEditAssignedLocationsResponseOut",
        "ListGuaranteedOrdersResponseIn": "_displayvideo_554_ListGuaranteedOrdersResponseIn",
        "ListGuaranteedOrdersResponseOut": "_displayvideo_555_ListGuaranteedOrdersResponseOut",
        "VideoDiscoveryAdIn": "_displayvideo_556_VideoDiscoveryAdIn",
        "VideoDiscoveryAdOut": "_displayvideo_557_VideoDiscoveryAdOut",
        "BulkEditAssignedTargetingOptionsResponseIn": "_displayvideo_558_BulkEditAssignedTargetingOptionsResponseIn",
        "BulkEditAssignedTargetingOptionsResponseOut": "_displayvideo_559_BulkEditAssignedTargetingOptionsResponseOut",
        "NegativeKeywordIn": "_displayvideo_560_NegativeKeywordIn",
        "NegativeKeywordOut": "_displayvideo_561_NegativeKeywordOut",
        "ActiveViewVideoViewabilityMetricConfigIn": "_displayvideo_562_ActiveViewVideoViewabilityMetricConfigIn",
        "ActiveViewVideoViewabilityMetricConfigOut": "_displayvideo_563_ActiveViewVideoViewabilityMetricConfigOut",
        "BulkEditPartnerAssignedTargetingOptionsRequestIn": "_displayvideo_564_BulkEditPartnerAssignedTargetingOptionsRequestIn",
        "BulkEditPartnerAssignedTargetingOptionsRequestOut": "_displayvideo_565_BulkEditPartnerAssignedTargetingOptionsRequestOut",
        "BulkEditNegativeKeywordsResponseIn": "_displayvideo_566_BulkEditNegativeKeywordsResponseIn",
        "BulkEditNegativeKeywordsResponseOut": "_displayvideo_567_BulkEditNegativeKeywordsResponseOut",
        "ListInvoicesResponseIn": "_displayvideo_568_ListInvoicesResponseIn",
        "ListInvoicesResponseOut": "_displayvideo_569_ListInvoicesResponseOut",
        "TimeRangeIn": "_displayvideo_570_TimeRangeIn",
        "TimeRangeOut": "_displayvideo_571_TimeRangeOut",
        "DoubleVerifyBrandSafetyCategoriesIn": "_displayvideo_572_DoubleVerifyBrandSafetyCategoriesIn",
        "DoubleVerifyBrandSafetyCategoriesOut": "_displayvideo_573_DoubleVerifyBrandSafetyCategoriesOut",
        "BulkEditNegativeKeywordsRequestIn": "_displayvideo_574_BulkEditNegativeKeywordsRequestIn",
        "BulkEditNegativeKeywordsRequestOut": "_displayvideo_575_BulkEditNegativeKeywordsRequestOut",
        "BulkListAssignedTargetingOptionsResponseIn": "_displayvideo_576_BulkListAssignedTargetingOptionsResponseIn",
        "BulkListAssignedTargetingOptionsResponseOut": "_displayvideo_577_BulkListAssignedTargetingOptionsResponseOut",
        "InventorySourceVideoCreativeConfigIn": "_displayvideo_578_InventorySourceVideoCreativeConfigIn",
        "InventorySourceVideoCreativeConfigOut": "_displayvideo_579_InventorySourceVideoCreativeConfigOut",
        "UserIn": "_displayvideo_580_UserIn",
        "UserOut": "_displayvideo_581_UserOut",
        "MeasurementConfigIn": "_displayvideo_582_MeasurementConfigIn",
        "MeasurementConfigOut": "_displayvideo_583_MeasurementConfigOut",
        "AuditAdvertiserResponseIn": "_displayvideo_584_AuditAdvertiserResponseIn",
        "AuditAdvertiserResponseOut": "_displayvideo_585_AuditAdvertiserResponseOut",
        "UserRewardedContentTargetingOptionDetailsIn": "_displayvideo_586_UserRewardedContentTargetingOptionDetailsIn",
        "UserRewardedContentTargetingOptionDetailsOut": "_displayvideo_587_UserRewardedContentTargetingOptionDetailsOut",
        "BumperAdIn": "_displayvideo_588_BumperAdIn",
        "BumperAdOut": "_displayvideo_589_BumperAdOut",
        "VideoAdSequenceSettingsIn": "_displayvideo_590_VideoAdSequenceSettingsIn",
        "VideoAdSequenceSettingsOut": "_displayvideo_591_VideoAdSequenceSettingsOut",
        "ExitEventIn": "_displayvideo_592_ExitEventIn",
        "ExitEventOut": "_displayvideo_593_ExitEventOut",
        "BusinessChainSearchTermsIn": "_displayvideo_594_BusinessChainSearchTermsIn",
        "BusinessChainSearchTermsOut": "_displayvideo_595_BusinessChainSearchTermsOut",
        "GoogleAudienceTargetingSettingIn": "_displayvideo_596_GoogleAudienceTargetingSettingIn",
        "GoogleAudienceTargetingSettingOut": "_displayvideo_597_GoogleAudienceTargetingSettingOut",
        "ObaIconIn": "_displayvideo_598_ObaIconIn",
        "ObaIconOut": "_displayvideo_599_ObaIconOut",
        "SearchTargetingOptionsResponseIn": "_displayvideo_600_SearchTargetingOptionsResponseIn",
        "SearchTargetingOptionsResponseOut": "_displayvideo_601_SearchTargetingOptionsResponseOut",
        "InventorySourceAssignedTargetingOptionDetailsIn": "_displayvideo_602_InventorySourceAssignedTargetingOptionDetailsIn",
        "InventorySourceAssignedTargetingOptionDetailsOut": "_displayvideo_603_InventorySourceAssignedTargetingOptionDetailsOut",
        "DuplicateLineItemResponseIn": "_displayvideo_604_DuplicateLineItemResponseIn",
        "DuplicateLineItemResponseOut": "_displayvideo_605_DuplicateLineItemResponseOut",
        "DoubleVerifyAppStarRatingIn": "_displayvideo_606_DoubleVerifyAppStarRatingIn",
        "DoubleVerifyAppStarRatingOut": "_displayvideo_607_DoubleVerifyAppStarRatingOut",
        "ConversionCountingConfigIn": "_displayvideo_608_ConversionCountingConfigIn",
        "ConversionCountingConfigOut": "_displayvideo_609_ConversionCountingConfigOut",
        "HouseholdIncomeTargetingOptionDetailsIn": "_displayvideo_610_HouseholdIncomeTargetingOptionDetailsIn",
        "HouseholdIncomeTargetingOptionDetailsOut": "_displayvideo_611_HouseholdIncomeTargetingOptionDetailsOut",
        "DeactivateManualTriggerRequestIn": "_displayvideo_612_DeactivateManualTriggerRequestIn",
        "DeactivateManualTriggerRequestOut": "_displayvideo_613_DeactivateManualTriggerRequestOut",
        "ExchangeConfigEnabledExchangeIn": "_displayvideo_614_ExchangeConfigEnabledExchangeIn",
        "ExchangeConfigEnabledExchangeOut": "_displayvideo_615_ExchangeConfigEnabledExchangeOut",
        "SubExchangeTargetingOptionDetailsIn": "_displayvideo_616_SubExchangeTargetingOptionDetailsIn",
        "SubExchangeTargetingOptionDetailsOut": "_displayvideo_617_SubExchangeTargetingOptionDetailsOut",
        "ListInventorySourcesResponseIn": "_displayvideo_618_ListInventorySourcesResponseIn",
        "ListInventorySourcesResponseOut": "_displayvideo_619_ListInventorySourcesResponseOut",
        "TargetingExpansionConfigIn": "_displayvideo_620_TargetingExpansionConfigIn",
        "TargetingExpansionConfigOut": "_displayvideo_621_TargetingExpansionConfigOut",
        "ListAssignedLocationsResponseIn": "_displayvideo_622_ListAssignedLocationsResponseIn",
        "ListAssignedLocationsResponseOut": "_displayvideo_623_ListAssignedLocationsResponseOut",
        "CommonInStreamAttributeIn": "_displayvideo_624_CommonInStreamAttributeIn",
        "CommonInStreamAttributeOut": "_displayvideo_625_CommonInStreamAttributeOut",
        "PacingIn": "_displayvideo_626_PacingIn",
        "PacingOut": "_displayvideo_627_PacingOut",
        "TargetFrequencyIn": "_displayvideo_628_TargetFrequencyIn",
        "TargetFrequencyOut": "_displayvideo_629_TargetFrequencyOut",
        "VideoPlayerSizeTargetingOptionDetailsIn": "_displayvideo_630_VideoPlayerSizeTargetingOptionDetailsIn",
        "VideoPlayerSizeTargetingOptionDetailsOut": "_displayvideo_631_VideoPlayerSizeTargetingOptionDetailsOut",
        "GenerateDefaultLineItemRequestIn": "_displayvideo_632_GenerateDefaultLineItemRequestIn",
        "GenerateDefaultLineItemRequestOut": "_displayvideo_633_GenerateDefaultLineItemRequestOut",
        "CustomListTargetingSettingIn": "_displayvideo_634_CustomListTargetingSettingIn",
        "CustomListTargetingSettingOut": "_displayvideo_635_CustomListTargetingSettingOut",
        "ExchangeAssignedTargetingOptionDetailsIn": "_displayvideo_636_ExchangeAssignedTargetingOptionDetailsIn",
        "ExchangeAssignedTargetingOptionDetailsOut": "_displayvideo_637_ExchangeAssignedTargetingOptionDetailsOut",
        "AuthorizedSellerStatusAssignedTargetingOptionDetailsIn": "_displayvideo_638_AuthorizedSellerStatusAssignedTargetingOptionDetailsIn",
        "AuthorizedSellerStatusAssignedTargetingOptionDetailsOut": "_displayvideo_639_AuthorizedSellerStatusAssignedTargetingOptionDetailsOut",
        "AuthorizedSellerStatusTargetingOptionDetailsIn": "_displayvideo_640_AuthorizedSellerStatusTargetingOptionDetailsIn",
        "AuthorizedSellerStatusTargetingOptionDetailsOut": "_displayvideo_641_AuthorizedSellerStatusTargetingOptionDetailsOut",
        "ProductMatchDimensionIn": "_displayvideo_642_ProductMatchDimensionIn",
        "ProductMatchDimensionOut": "_displayvideo_643_ProductMatchDimensionOut",
        "ThirdPartyVendorConfigIn": "_displayvideo_644_ThirdPartyVendorConfigIn",
        "ThirdPartyVendorConfigOut": "_displayvideo_645_ThirdPartyVendorConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["LanguageAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["LanguageAssignedTargetingOptionDetailsIn"])
    types["LanguageAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageAssignedTargetingOptionDetailsOut"])
    types["PartnerAdServerConfigIn"] = t.struct(
        {"measurementConfig": t.proxy(renames["MeasurementConfigIn"]).optional()}
    ).named(renames["PartnerAdServerConfigIn"])
    types["PartnerAdServerConfigOut"] = t.struct(
        {
            "measurementConfig": t.proxy(renames["MeasurementConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerAdServerConfigOut"])
    types["BulkListAdvertiserAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
        }
    ).named(renames["BulkListAdvertiserAssignedTargetingOptionsResponseIn"])
    types["BulkListAdvertiserAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkListAdvertiserAssignedTargetingOptionsResponseOut"])
    types["DisplayVideoSourceAdIn"] = t.struct(
        {"creativeId": t.string().optional()}
    ).named(renames["DisplayVideoSourceAdIn"])
    types["DisplayVideoSourceAdOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayVideoSourceAdOut"])
    types["CampaignGoalIn"] = t.struct(
        {
            "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
            "campaignGoalType": t.string(),
        }
    ).named(renames["CampaignGoalIn"])
    types["CampaignGoalOut"] = t.struct(
        {
            "performanceGoal": t.proxy(renames["PerformanceGoalOut"]),
            "campaignGoalType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignGoalOut"])
    types["PoiSearchTermsIn"] = t.struct({"poiQuery": t.string().optional()}).named(
        renames["PoiSearchTermsIn"]
    )
    types["PoiSearchTermsOut"] = t.struct(
        {
            "poiQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiSearchTermsOut"])
    types["ContentGenreAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["ContentGenreAssignedTargetingOptionDetailsIn"])
    types["ContentGenreAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentGenreAssignedTargetingOptionDetailsOut"])
    types["PoiTargetingOptionDetailsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PoiTargetingOptionDetailsIn"]
    )
    types["PoiTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiTargetingOptionDetailsOut"])
    types["DeviceTypeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"deviceType": t.string().optional()}
    ).named(renames["DeviceTypeAssignedTargetingOptionDetailsIn"])
    types["DeviceTypeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "youtubeAndPartnersBidMultiplier": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTypeAssignedTargetingOptionDetailsOut"])
    types["YoutubeAndPartnersInventorySourceConfigIn"] = t.struct(
        {
            "includeYoutubeVideos": t.boolean().optional(),
            "includeYoutubeVideoPartners": t.boolean().optional(),
            "includeYoutubeSearch": t.boolean().optional(),
        }
    ).named(renames["YoutubeAndPartnersInventorySourceConfigIn"])
    types["YoutubeAndPartnersInventorySourceConfigOut"] = t.struct(
        {
            "includeYoutubeVideos": t.boolean().optional(),
            "includeYoutubeVideoPartners": t.boolean().optional(),
            "includeYoutubeSearch": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersInventorySourceConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExchangeReviewStatusIn"] = t.struct(
        {"exchange": t.string().optional(), "status": t.string().optional()}
    ).named(renames["ExchangeReviewStatusIn"])
    types["ExchangeReviewStatusOut"] = t.struct(
        {
            "exchange": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeReviewStatusOut"])
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
    types["AgeRangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"ageRange": t.string().optional()}
    ).named(renames["AgeRangeAssignedTargetingOptionDetailsIn"])
    types["AgeRangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeAssignedTargetingOptionDetailsOut"])
    types["PerformanceGoalBidStrategyIn"] = t.struct(
        {
            "performanceGoalType": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalAmountMicros": t.string(),
        }
    ).named(renames["PerformanceGoalBidStrategyIn"])
    types["PerformanceGoalBidStrategyOut"] = t.struct(
        {
            "performanceGoalType": t.string(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "performanceGoalAmountMicros": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceGoalBidStrategyOut"])
    types["GoogleAudienceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAudienceIn"]
    )
    types["GoogleAudienceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "googleAudienceId": t.string().optional(),
            "googleAudienceType": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceOut"])
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
    types["ParentalStatusTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ParentalStatusTargetingOptionDetailsIn"])
    types["ParentalStatusTargetingOptionDetailsOut"] = t.struct(
        {
            "parentalStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentalStatusTargetingOptionDetailsOut"])
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
    types["OnScreenPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OnScreenPositionTargetingOptionDetailsIn"])
    types["OnScreenPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "onScreenPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnScreenPositionTargetingOptionDetailsOut"])
    types["AssignedInventorySourceIn"] = t.struct(
        {"inventorySourceId": t.string()}
    ).named(renames["AssignedInventorySourceIn"])
    types["AssignedInventorySourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "inventorySourceId": t.string(),
            "assignedInventorySourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedInventorySourceOut"])
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
    types["BudgetSummaryIn"] = t.struct(
        {
            "preTaxAmountMicros": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeIn"]).optional(),
            "totalAmountMicros": t.string().optional(),
            "taxAmountMicros": t.string().optional(),
        }
    ).named(renames["BudgetSummaryIn"])
    types["BudgetSummaryOut"] = t.struct(
        {
            "preTaxAmountMicros": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeOut"]).optional(),
            "totalAmountMicros": t.string().optional(),
            "taxAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BudgetSummaryOut"])
    types["DeviceTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeviceTypeTargetingOptionDetailsIn"])
    types["DeviceTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTypeTargetingOptionDetailsOut"])
    types["BulkUpdateLineItemsRequestIn"] = t.struct(
        {
            "lineItemIds": t.array(t.string()),
            "targetLineItem": t.proxy(renames["LineItemIn"]),
            "updateMask": t.string(),
        }
    ).named(renames["BulkUpdateLineItemsRequestIn"])
    types["BulkUpdateLineItemsRequestOut"] = t.struct(
        {
            "lineItemIds": t.array(t.string()),
            "targetLineItem": t.proxy(renames["LineItemOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkUpdateLineItemsRequestOut"])
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
    types["ParentEntityFilterIn"] = t.struct(
        {
            "fileType": t.array(t.string()),
            "filterType": t.string(),
            "filterIds": t.array(t.string()).optional(),
        }
    ).named(renames["ParentEntityFilterIn"])
    types["ParentEntityFilterOut"] = t.struct(
        {
            "fileType": t.array(t.string()),
            "filterType": t.string(),
            "filterIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentEntityFilterOut"])
    types["ContentInstreamPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentInstreamPositionTargetingOptionDetailsIn"])
    types["ContentInstreamPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentInstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentInstreamPositionTargetingOptionDetailsOut"])
    types["ContentOutstreamPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentOutstreamPositionTargetingOptionDetailsIn"])
    types["ContentOutstreamPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentOutstreamPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOutstreamPositionTargetingOptionDetailsOut"])
    types["GoogleBytestreamMediaIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["GoogleBytestreamMediaIn"])
    types["GoogleBytestreamMediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleBytestreamMediaOut"])
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
    types["AppAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "appId": t.string(),
            "appPlatform": t.string().optional(),
        }
    ).named(renames["AppAssignedTargetingOptionDetailsIn"])
    types["AppAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "appId": t.string(),
            "appPlatform": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppAssignedTargetingOptionDetailsOut"])
    types["MobileDeviceIdListIn"] = t.struct(
        {"mobileDeviceIds": t.array(t.string()).optional()}
    ).named(renames["MobileDeviceIdListIn"])
    types["MobileDeviceIdListOut"] = t.struct(
        {
            "mobileDeviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileDeviceIdListOut"])
    types["LineItemIn"] = t.struct(
        {
            "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
            "pacing": t.proxy(renames["PacingIn"]),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "entityStatus": t.string(),
            "insertionOrderId": t.string(),
            "conversionCounting": t.proxy(
                renames["ConversionCountingConfigIn"]
            ).optional(),
            "excludeNewExchanges": t.boolean().optional(),
            "budget": t.proxy(renames["LineItemBudgetIn"]),
            "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
            "creativeIds": t.array(t.string()).optional(),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "displayName": t.string(),
            "flight": t.proxy(renames["LineItemFlightIn"]),
            "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigIn"]
            ).optional(),
            "lineItemType": t.string(),
        }
    ).named(renames["LineItemIn"])
    types["LineItemOut"] = t.struct(
        {
            "partnerCosts": t.array(t.proxy(renames["PartnerCostOut"])).optional(),
            "pacing": t.proxy(renames["PacingOut"]),
            "lineItemId": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "entityStatus": t.string(),
            "updateTime": t.string().optional(),
            "reservationType": t.string().optional(),
            "insertionOrderId": t.string(),
            "conversionCounting": t.proxy(
                renames["ConversionCountingConfigOut"]
            ).optional(),
            "campaignId": t.string().optional(),
            "excludeNewExchanges": t.boolean().optional(),
            "youtubeAndPartnersSettings": t.proxy(
                renames["YoutubeAndPartnersSettingsOut"]
            ).optional(),
            "name": t.string().optional(),
            "budget": t.proxy(renames["LineItemBudgetOut"]),
            "bidStrategy": t.proxy(renames["BiddingStrategyOut"]),
            "warningMessages": t.array(t.string()).optional(),
            "creativeIds": t.array(t.string()).optional(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "displayName": t.string(),
            "flight": t.proxy(renames["LineItemFlightOut"]),
            "advertiserId": t.string().optional(),
            "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelOut"]),
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigOut"]
            ).optional(),
            "lineItemType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineItemOut"])
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
    types["GuaranteedOrderIn"] = t.struct(
        {
            "readWriteAdvertiserId": t.string().optional(),
            "readAccessInherited": t.boolean().optional(),
            "exchange": t.string(),
            "displayName": t.string(),
            "defaultCampaignId": t.string().optional(),
            "readWritePartnerId": t.string().optional(),
            "publisherName": t.string(),
            "status": t.proxy(renames["GuaranteedOrderStatusIn"]).optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
        }
    ).named(renames["GuaranteedOrderIn"])
    types["GuaranteedOrderOut"] = t.struct(
        {
            "readWriteAdvertiserId": t.string().optional(),
            "readAccessInherited": t.boolean().optional(),
            "guaranteedOrderId": t.string().optional(),
            "exchange": t.string(),
            "displayName": t.string(),
            "defaultCampaignId": t.string().optional(),
            "defaultAdvertiserId": t.string().optional(),
            "readWritePartnerId": t.string().optional(),
            "publisherName": t.string(),
            "status": t.proxy(renames["GuaranteedOrderStatusOut"]).optional(),
            "legacyGuaranteedOrderId": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedOrderOut"])
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
    types["GuaranteedOrderStatusIn"] = t.struct(
        {
            "entityPauseReason": t.string().optional(),
            "entityStatus": t.string().optional(),
        }
    ).named(renames["GuaranteedOrderStatusIn"])
    types["GuaranteedOrderStatusOut"] = t.struct(
        {
            "entityPauseReason": t.string().optional(),
            "entityStatus": t.string().optional(),
            "configStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedOrderStatusOut"])
    types["IdFilterIn"] = t.struct(
        {
            "adGroupIds": t.array(t.string()).optional(),
            "mediaProductIds": t.array(t.string()).optional(),
            "lineItemIds": t.array(t.string()).optional(),
            "campaignIds": t.array(t.string()).optional(),
            "adGroupAdIds": t.array(t.string()).optional(),
            "insertionOrderIds": t.array(t.string()).optional(),
        }
    ).named(renames["IdFilterIn"])
    types["IdFilterOut"] = t.struct(
        {
            "adGroupIds": t.array(t.string()).optional(),
            "mediaProductIds": t.array(t.string()).optional(),
            "lineItemIds": t.array(t.string()).optional(),
            "campaignIds": t.array(t.string()).optional(),
            "adGroupAdIds": t.array(t.string()).optional(),
            "insertionOrderIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdFilterOut"])
    types["EditCustomerMatchMembersResponseIn"] = t.struct(
        {"firstAndThirdPartyAudienceId": t.string()}
    ).named(renames["EditCustomerMatchMembersResponseIn"])
    types["EditCustomerMatchMembersResponseOut"] = t.struct(
        {
            "firstAndThirdPartyAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditCustomerMatchMembersResponseOut"])
    types["InsertionOrderIn"] = t.struct(
        {
            "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
            "billableOutcome": t.string().optional(),
            "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
            "insertionOrderType": t.string().optional(),
            "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
            "pacing": t.proxy(renames["PacingIn"]),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "campaignId": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "entityStatus": t.string(),
            "displayName": t.string(),
            "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
        }
    ).named(renames["InsertionOrderIn"])
    types["InsertionOrderOut"] = t.struct(
        {
            "reservationType": t.string().optional(),
            "partnerCosts": t.array(t.proxy(renames["PartnerCostOut"])).optional(),
            "billableOutcome": t.string().optional(),
            "performanceGoal": t.proxy(renames["PerformanceGoalOut"]),
            "advertiserId": t.string().optional(),
            "insertionOrderType": t.string().optional(),
            "budget": t.proxy(renames["InsertionOrderBudgetOut"]),
            "pacing": t.proxy(renames["PacingOut"]),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "campaignId": t.string(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "entityStatus": t.string(),
            "displayName": t.string(),
            "bidStrategy": t.proxy(renames["BiddingStrategyOut"]).optional(),
            "insertionOrderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderOut"])
    types["BusinessChainAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "proximityRadiusUnit": t.string(),
            "proximityRadiusAmount": t.number(),
            "targetingOptionId": t.string(),
        }
    ).named(renames["BusinessChainAssignedTargetingOptionDetailsIn"])
    types["BusinessChainAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "proximityRadiusUnit": t.string(),
            "proximityRadiusAmount": t.number(),
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessChainAssignedTargetingOptionDetailsOut"])
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
    types["VideoAdSequenceStepIn"] = t.struct(
        {
            "previousStepId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "stepId": t.string().optional(),
            "interactionType": t.string().optional(),
        }
    ).named(renames["VideoAdSequenceStepIn"])
    types["VideoAdSequenceStepOut"] = t.struct(
        {
            "previousStepId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "stepId": t.string().optional(),
            "interactionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAdSequenceStepOut"])
    types["AgeRangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AgeRangeTargetingOptionDetailsIn"])
    types["AgeRangeTargetingOptionDetailsOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeTargetingOptionDetailsOut"])
    types["AudienceGroupAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "includedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupIn"]
            ).optional(),
            "excludedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupIn"]
            ).optional(),
            "includedCustomListGroup": t.proxy(renames["CustomListGroupIn"]).optional(),
            "includedFirstAndThirdPartyAudienceGroups": t.array(
                t.proxy(renames["FirstAndThirdPartyAudienceGroupIn"])
            ).optional(),
            "includedCombinedAudienceGroup": t.proxy(
                renames["CombinedAudienceGroupIn"]
            ).optional(),
            "excludedFirstAndThirdPartyAudienceGroup": t.proxy(
                renames["FirstAndThirdPartyAudienceGroupIn"]
            ).optional(),
        }
    ).named(renames["AudienceGroupAssignedTargetingOptionDetailsIn"])
    types["AudienceGroupAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "includedGoogleAudienceGroup": t.proxy(
                renames["GoogleAudienceGroupOut"]
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
            "includedCombinedAudienceGroup": t.proxy(
                renames["CombinedAudienceGroupOut"]
            ).optional(),
            "excludedFirstAndThirdPartyAudienceGroup": t.proxy(
                renames["FirstAndThirdPartyAudienceGroupOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudienceGroupAssignedTargetingOptionDetailsOut"])
    types["IntegralAdScienceIn"] = t.struct(
        {
            "excludedOffensiveLanguageRisk": t.string().optional(),
            "excludedHateSpeechRisk": t.string().optional(),
            "excludedGamblingRisk": t.string().optional(),
            "excludedIllegalDownloadsRisk": t.string().optional(),
            "displayViewability": t.string().optional(),
            "videoViewability": t.string().optional(),
            "customSegmentId": t.array(t.string()).optional(),
            "excludedViolenceRisk": t.string().optional(),
            "excludedAlcoholRisk": t.string().optional(),
            "excludedAdFraudRisk": t.string().optional(),
            "excludeUnrateable": t.boolean().optional(),
            "excludedAdultRisk": t.string().optional(),
            "excludedDrugsRisk": t.string().optional(),
            "traqScoreOption": t.string().optional(),
        }
    ).named(renames["IntegralAdScienceIn"])
    types["IntegralAdScienceOut"] = t.struct(
        {
            "excludedOffensiveLanguageRisk": t.string().optional(),
            "excludedHateSpeechRisk": t.string().optional(),
            "excludedGamblingRisk": t.string().optional(),
            "excludedIllegalDownloadsRisk": t.string().optional(),
            "displayViewability": t.string().optional(),
            "videoViewability": t.string().optional(),
            "customSegmentId": t.array(t.string()).optional(),
            "excludedViolenceRisk": t.string().optional(),
            "excludedAlcoholRisk": t.string().optional(),
            "excludedAdFraudRisk": t.string().optional(),
            "excludeUnrateable": t.boolean().optional(),
            "excludedAdultRisk": t.string().optional(),
            "excludedDrugsRisk": t.string().optional(),
            "traqScoreOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegralAdScienceOut"])
    types["CmHybridConfigIn"] = t.struct(
        {
            "cmAccountId": t.string(),
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "cmFloodlightConfigId": t.string(),
            "cmSyncableSiteIds": t.array(t.string()).optional(),
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "cmFloodlightLinkingAuthorized": t.boolean(),
        }
    ).named(renames["CmHybridConfigIn"])
    types["CmHybridConfigOut"] = t.struct(
        {
            "cmAccountId": t.string(),
            "dv360ToCmDataSharingEnabled": t.boolean().optional(),
            "cmFloodlightConfigId": t.string(),
            "cmSyncableSiteIds": t.array(t.string()).optional(),
            "dv360ToCmCostReportingEnabled": t.boolean().optional(),
            "cmFloodlightLinkingAuthorized": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmHybridConfigOut"])
    types["PoiAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "proximityRadiusAmount": t.number(),
            "proximityRadiusUnit": t.string(),
            "targetingOptionId": t.string(),
        }
    ).named(renames["PoiAssignedTargetingOptionDetailsIn"])
    types["PoiAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "proximityRadiusAmount": t.number(),
            "latitude": t.number().optional(),
            "proximityRadiusUnit": t.string(),
            "displayName": t.string().optional(),
            "longitude": t.number().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoiAssignedTargetingOptionDetailsOut"])
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
            "locationListId": t.string().optional(),
            "displayName": t.string(),
            "locationType": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationListOut"])
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
    types["InventorySourceDisplayCreativeConfigIn"] = t.struct(
        {"creativeSize": t.proxy(renames["DimensionsIn"]).optional()}
    ).named(renames["InventorySourceDisplayCreativeConfigIn"])
    types["InventorySourceDisplayCreativeConfigOut"] = t.struct(
        {
            "creativeSize": t.proxy(renames["DimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceDisplayCreativeConfigOut"])
    types["VideoPerformanceAdIn"] = t.struct(
        {
            "domain": t.string().optional(),
            "displayUrlBreadcrumb1": t.string().optional(),
            "actionButtonLabels": t.array(t.string()).optional(),
            "headlines": t.array(t.string()).optional(),
            "trackingUrl": t.string().optional(),
            "companionBanners": t.array(t.proxy(renames["ImageAssetIn"])).optional(),
            "videos": t.array(t.proxy(renames["YoutubeVideoDetailsIn"])).optional(),
            "finalUrl": t.string().optional(),
            "descriptions": t.array(t.string()).optional(),
            "displayUrlBreadcrumb2": t.string().optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "longHeadlines": t.array(t.string()).optional(),
        }
    ).named(renames["VideoPerformanceAdIn"])
    types["VideoPerformanceAdOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "displayUrlBreadcrumb1": t.string().optional(),
            "actionButtonLabels": t.array(t.string()).optional(),
            "headlines": t.array(t.string()).optional(),
            "trackingUrl": t.string().optional(),
            "companionBanners": t.array(t.proxy(renames["ImageAssetOut"])).optional(),
            "videos": t.array(t.proxy(renames["YoutubeVideoDetailsOut"])).optional(),
            "finalUrl": t.string().optional(),
            "descriptions": t.array(t.string()).optional(),
            "displayUrlBreadcrumb2": t.string().optional(),
            "customParameters": t.struct({"_": t.string().optional()}).optional(),
            "longHeadlines": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPerformanceAdOut"])
    types["ContentGenreTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentGenreTargetingOptionDetailsIn"])
    types["ContentGenreTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentGenreTargetingOptionDetailsOut"])
    types["EnvironmentAssignedTargetingOptionDetailsIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["EnvironmentAssignedTargetingOptionDetailsIn"])
    types["EnvironmentAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentAssignedTargetingOptionDetailsOut"])
    types["PerformanceGoalIn"] = t.struct(
        {
            "performanceGoalAmountMicros": t.string().optional(),
            "performanceGoalPercentageMicros": t.string().optional(),
            "performanceGoalType": t.string(),
            "performanceGoalString": t.string().optional(),
        }
    ).named(renames["PerformanceGoalIn"])
    types["PerformanceGoalOut"] = t.struct(
        {
            "performanceGoalAmountMicros": t.string().optional(),
            "performanceGoalPercentageMicros": t.string().optional(),
            "performanceGoalType": t.string(),
            "performanceGoalString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceGoalOut"])
    types["CreateAssignedTargetingOptionsRequestIn"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ),
            "targetingType": t.string(),
        }
    ).named(renames["CreateAssignedTargetingOptionsRequestIn"])
    types["CreateAssignedTargetingOptionsRequestOut"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ),
            "targetingType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAssignedTargetingOptionsRequestOut"])
    types["GeoRegionSearchTermsIn"] = t.struct(
        {"geoRegionQuery": t.string().optional()}
    ).named(renames["GeoRegionSearchTermsIn"])
    types["GeoRegionSearchTermsOut"] = t.struct(
        {
            "geoRegionQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionSearchTermsOut"])
    types["YoutubeAndPartnersBiddingStrategyIn"] = t.struct(
        {"value": t.string().optional(), "type": t.string().optional()}
    ).named(renames["YoutubeAndPartnersBiddingStrategyIn"])
    types["YoutubeAndPartnersBiddingStrategyOut"] = t.struct(
        {
            "adGroupEffectiveTargetCpaValue": t.string().optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "adGroupEffectiveTargetCpaSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersBiddingStrategyOut"])
    types["InventorySourceIn"] = t.struct(
        {
            "guaranteedOrderId": t.string().optional(),
            "exchange": t.string().optional(),
            "commitment": t.string().optional(),
            "dealId": t.string().optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "readWriteAccessors": t.proxy(
                renames["InventorySourceAccessorsIn"]
            ).optional(),
            "subSitePropertyId": t.string().optional(),
            "inventorySourceType": t.string().optional(),
            "status": t.proxy(renames["InventorySourceStatusIn"]).optional(),
            "publisherName": t.string().optional(),
            "displayName": t.string().optional(),
            "rateDetails": t.proxy(renames["RateDetailsIn"]),
            "creativeConfigs": t.array(t.proxy(renames["CreativeConfigIn"])).optional(),
            "deliveryMethod": t.string().optional(),
        }
    ).named(renames["InventorySourceIn"])
    types["InventorySourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "guaranteedOrderId": t.string().optional(),
            "exchange": t.string().optional(),
            "readPartnerIds": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "commitment": t.string().optional(),
            "dealId": t.string().optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "readWriteAccessors": t.proxy(
                renames["InventorySourceAccessorsOut"]
            ).optional(),
            "inventorySourceId": t.string().optional(),
            "subSitePropertyId": t.string().optional(),
            "inventorySourceType": t.string().optional(),
            "status": t.proxy(renames["InventorySourceStatusOut"]).optional(),
            "publisherName": t.string().optional(),
            "displayName": t.string().optional(),
            "inventorySourceProductType": t.string().optional(),
            "rateDetails": t.proxy(renames["RateDetailsOut"]),
            "creativeConfigs": t.array(
                t.proxy(renames["CreativeConfigOut"])
            ).optional(),
            "deliveryMethod": t.string().optional(),
            "readAdvertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceOut"])
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
    types["ProductFeedDataIn"] = t.struct(
        {
            "productMatchDimensions": t.array(
                t.proxy(renames["ProductMatchDimensionIn"])
            ).optional(),
            "productMatchType": t.string().optional(),
            "isFeedDisabled": t.boolean().optional(),
        }
    ).named(renames["ProductFeedDataIn"])
    types["ProductFeedDataOut"] = t.struct(
        {
            "productMatchDimensions": t.array(
                t.proxy(renames["ProductMatchDimensionOut"])
            ).optional(),
            "productMatchType": t.string().optional(),
            "isFeedDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductFeedDataOut"])
    types["EditInventorySourceReadWriteAccessorsRequestIn"] = t.struct(
        {
            "assignPartner": t.boolean().optional(),
            "partnerId": t.string(),
            "advertisersUpdate": t.proxy(
                renames[
                    "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"
                ]
            ).optional(),
        }
    ).named(renames["EditInventorySourceReadWriteAccessorsRequestIn"])
    types["EditInventorySourceReadWriteAccessorsRequestOut"] = t.struct(
        {
            "assignPartner": t.boolean().optional(),
            "partnerId": t.string(),
            "advertisersUpdate": t.proxy(
                renames[
                    "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditInventorySourceReadWriteAccessorsRequestOut"])
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
    types["CreativeIn"] = t.struct(
        {
            "displayName": t.string(),
            "requireMraid": t.boolean().optional(),
            "entityStatus": t.string(),
            "counterEvents": t.array(t.proxy(renames["CounterEventIn"])).optional(),
            "hostingSource": t.string(),
            "thirdPartyTag": t.string().optional(),
            "cmTrackingAd": t.proxy(renames["CmTrackingAdIn"]).optional(),
            "integrationCode": t.string().optional(),
            "skipOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
            "obaIcon": t.proxy(renames["ObaIconIn"]).optional(),
            "vastTagUrl": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetAssociationIn"])),
            "requirePingForAttribution": t.boolean().optional(),
            "skippable": t.boolean().optional(),
            "jsTrackerUrl": t.string().optional(),
            "appendedTag": t.string().optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdIn"]).optional(),
            "notes": t.string().optional(),
            "expandingDirection": t.string().optional(),
            "thirdPartyUrls": t.array(t.proxy(renames["ThirdPartyUrlIn"])).optional(),
            "timerEvents": t.array(t.proxy(renames["TimerEventIn"])).optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]),
            "expandOnHover": t.boolean().optional(),
            "trackerUrls": t.array(t.string()).optional(),
            "iasCampaignMonitoring": t.boolean().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "creativeType": t.string(),
            "requireHtml5": t.boolean().optional(),
            "progressOffset": t.proxy(renames["AudioVideoOffsetIn"]).optional(),
            "additionalDimensions": t.array(
                t.proxy(renames["DimensionsIn"])
            ).optional(),
            "exitEvents": t.array(t.proxy(renames["ExitEventIn"])),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "displayName": t.string(),
            "advertiserId": t.string().optional(),
            "requireMraid": t.boolean().optional(),
            "entityStatus": t.string(),
            "counterEvents": t.array(t.proxy(renames["CounterEventOut"])).optional(),
            "hostingSource": t.string(),
            "thirdPartyTag": t.string().optional(),
            "cmTrackingAd": t.proxy(renames["CmTrackingAdOut"]).optional(),
            "creativeAttributes": t.array(t.string()).optional(),
            "integrationCode": t.string().optional(),
            "dynamic": t.boolean().optional(),
            "skipOffset": t.proxy(renames["AudioVideoOffsetOut"]).optional(),
            "obaIcon": t.proxy(renames["ObaIconOut"]).optional(),
            "vastTagUrl": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetAssociationOut"])),
            "html5Video": t.boolean().optional(),
            "vpaid": t.boolean().optional(),
            "requirePingForAttribution": t.boolean().optional(),
            "creativeId": t.string().optional(),
            "createTime": t.string().optional(),
            "skippable": t.boolean().optional(),
            "jsTrackerUrl": t.string().optional(),
            "lineItemIds": t.array(t.string()).optional(),
            "transcodes": t.array(t.proxy(renames["TranscodeOut"])).optional(),
            "appendedTag": t.string().optional(),
            "reviewStatus": t.proxy(renames["ReviewStatusInfoOut"]).optional(),
            "universalAdId": t.proxy(renames["UniversalAdIdOut"]).optional(),
            "updateTime": t.string().optional(),
            "notes": t.string().optional(),
            "expandingDirection": t.string().optional(),
            "thirdPartyUrls": t.array(t.proxy(renames["ThirdPartyUrlOut"])).optional(),
            "timerEvents": t.array(t.proxy(renames["TimerEventOut"])).optional(),
            "mediaDuration": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]),
            "expandOnHover": t.boolean().optional(),
            "trackerUrls": t.array(t.string()).optional(),
            "iasCampaignMonitoring": t.boolean().optional(),
            "companionCreativeIds": t.array(t.string()).optional(),
            "oggAudio": t.boolean().optional(),
            "cmPlacementId": t.string().optional(),
            "creativeType": t.string(),
            "requireHtml5": t.boolean().optional(),
            "progressOffset": t.proxy(renames["AudioVideoOffsetOut"]).optional(),
            "additionalDimensions": t.array(
                t.proxy(renames["DimensionsOut"])
            ).optional(),
            "mp3Audio": t.boolean().optional(),
            "name": t.string().optional(),
            "exitEvents": t.array(t.proxy(renames["ExitEventOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
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
    types["ViewabilityAssignedTargetingOptionDetailsIn"] = t.struct(
        {"viewability": t.string().optional()}
    ).named(renames["ViewabilityAssignedTargetingOptionDetailsIn"])
    types["ViewabilityAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "viewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewabilityAssignedTargetingOptionDetailsOut"])
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
    types["CategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CategoryTargetingOptionDetailsIn"])
    types["CategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryTargetingOptionDetailsOut"])
    types["CampaignBudgetIn"] = t.struct(
        {
            "externalBudgetSource": t.string(),
            "budgetId": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]),
            "budgetAmountMicros": t.string(),
            "invoiceGroupingId": t.string().optional(),
            "displayName": t.string(),
            "budgetUnit": t.string(),
            "prismaConfig": t.proxy(renames["PrismaConfigIn"]).optional(),
        }
    ).named(renames["CampaignBudgetIn"])
    types["CampaignBudgetOut"] = t.struct(
        {
            "externalBudgetSource": t.string(),
            "budgetId": t.string().optional(),
            "externalBudgetId": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]),
            "budgetAmountMicros": t.string(),
            "invoiceGroupingId": t.string().optional(),
            "displayName": t.string(),
            "budgetUnit": t.string(),
            "prismaConfig": t.proxy(renames["PrismaConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignBudgetOut"])
    types["CategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["CategoryAssignedTargetingOptionDetailsIn"])
    types["CategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryAssignedTargetingOptionDetailsOut"])
    types["FixedBidStrategyIn"] = t.struct(
        {"bidAmountMicros": t.string().optional()}
    ).named(renames["FixedBidStrategyIn"])
    types["FixedBidStrategyOut"] = t.struct(
        {
            "bidAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixedBidStrategyOut"])
    types["ListCampaignAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCampaignAssignedTargetingOptionsResponseIn"])
    types["ListCampaignAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCampaignAssignedTargetingOptionsResponseOut"])
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
    types["TrackingFloodlightActivityConfigIn"] = t.struct(
        {
            "postViewLookbackWindowDays": t.integer(),
            "floodlightActivityId": t.string(),
            "postClickLookbackWindowDays": t.integer(),
        }
    ).named(renames["TrackingFloodlightActivityConfigIn"])
    types["TrackingFloodlightActivityConfigOut"] = t.struct(
        {
            "postViewLookbackWindowDays": t.integer(),
            "floodlightActivityId": t.string(),
            "postClickLookbackWindowDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackingFloodlightActivityConfigOut"])
    types["LookupInvoiceCurrencyResponseIn"] = t.struct(
        {"currencyCode": t.string().optional()}
    ).named(renames["LookupInvoiceCurrencyResponseIn"])
    types["LookupInvoiceCurrencyResponseOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupInvoiceCurrencyResponseOut"])
    types["YoutubeAdGroupIn"] = t.struct(
        {
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigIn"]
            ).optional(),
            "adGroupId": t.string().optional(),
            "entityStatus": t.string().optional(),
            "displayName": t.string().optional(),
            "lineItemId": t.string().optional(),
            "name": t.string().optional(),
            "adGroupFormat": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyIn"]
            ).optional(),
            "productFeedData": t.proxy(renames["ProductFeedDataIn"]).optional(),
            "advertiserId": t.string().optional(),
            "youtubeAdIds": t.array(t.string()).optional(),
        }
    ).named(renames["YoutubeAdGroupIn"])
    types["YoutubeAdGroupOut"] = t.struct(
        {
            "targetingExpansion": t.proxy(
                renames["TargetingExpansionConfigOut"]
            ).optional(),
            "adGroupId": t.string().optional(),
            "entityStatus": t.string().optional(),
            "displayName": t.string().optional(),
            "lineItemId": t.string().optional(),
            "name": t.string().optional(),
            "adGroupFormat": t.string().optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyOut"]
            ).optional(),
            "productFeedData": t.proxy(renames["ProductFeedDataOut"]).optional(),
            "advertiserId": t.string().optional(),
            "youtubeAdIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupOut"])
    types["AudioAdIn"] = t.struct(
        {
            "finalUrl": t.string().optional(),
            "trackingUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "displayUrl": t.string().optional(),
        }
    ).named(renames["AudioAdIn"])
    types["AudioAdOut"] = t.struct(
        {
            "finalUrl": t.string().optional(),
            "trackingUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "displayUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioAdOut"])
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
    types["DeviceMakeModelTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeviceMakeModelTargetingOptionDetailsIn"])
    types["DeviceMakeModelTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMakeModelTargetingOptionDetailsOut"])
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
    types["ScriptErrorIn"] = t.struct(
        {
            "line": t.string().optional(),
            "column": t.string().optional(),
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["ScriptErrorIn"])
    types["ScriptErrorOut"] = t.struct(
        {
            "line": t.string().optional(),
            "column": t.string().optional(),
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptErrorOut"])
    types["ContentDurationTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentDurationTargetingOptionDetailsIn"])
    types["ContentDurationTargetingOptionDetailsOut"] = t.struct(
        {
            "contentDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentDurationTargetingOptionDetailsOut"])
    types["BulkEditSitesRequestIn"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "deletedSites": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
            "createdSites": t.array(t.proxy(renames["SiteIn"])).optional(),
        }
    ).named(renames["BulkEditSitesRequestIn"])
    types["BulkEditSitesRequestOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "deletedSites": t.array(t.string()).optional(),
            "advertiserId": t.string().optional(),
            "createdSites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditSitesRequestOut"])
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
    types["CustomBiddingModelDetailsIn"] = t.struct(
        {"advertiserId": t.string().optional(), "readinessState": t.string().optional()}
    ).named(renames["CustomBiddingModelDetailsIn"])
    types["CustomBiddingModelDetailsOut"] = t.struct(
        {
            "suspensionState": t.string().optional(),
            "advertiserId": t.string().optional(),
            "readinessState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingModelDetailsOut"])
    types["PartnerIn"] = t.struct(
        {
            "exchangeConfig": t.proxy(renames["ExchangeConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "dataAccessConfig": t.proxy(
                renames["PartnerDataAccessConfigIn"]
            ).optional(),
            "adServerConfig": t.proxy(renames["PartnerAdServerConfigIn"]).optional(),
            "generalConfig": t.proxy(renames["PartnerGeneralConfigIn"]).optional(),
        }
    ).named(renames["PartnerIn"])
    types["PartnerOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "exchangeConfig": t.proxy(renames["ExchangeConfigOut"]).optional(),
            "partnerId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "entityStatus": t.string().optional(),
            "dataAccessConfig": t.proxy(
                renames["PartnerDataAccessConfigOut"]
            ).optional(),
            "adServerConfig": t.proxy(renames["PartnerAdServerConfigOut"]).optional(),
            "generalConfig": t.proxy(renames["PartnerGeneralConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerOut"])
    types["CustomBiddingScriptIn"] = t.struct(
        {"script": t.proxy(renames["CustomBiddingScriptRefIn"]).optional()}
    ).named(renames["CustomBiddingScriptIn"])
    types["CustomBiddingScriptOut"] = t.struct(
        {
            "customBiddingScriptId": t.string().optional(),
            "active": t.boolean().optional(),
            "errors": t.array(t.proxy(renames["ScriptErrorOut"])).optional(),
            "createTime": t.string().optional(),
            "script": t.proxy(renames["CustomBiddingScriptRefOut"]).optional(),
            "state": t.string().optional(),
            "customBiddingAlgorithmId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingScriptOut"])
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
    types["InventorySourceGroupIn"] = t.struct({"displayName": t.string()}).named(
        renames["InventorySourceGroupIn"]
    )
    types["InventorySourceGroupOut"] = t.struct(
        {
            "inventorySourceGroupId": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceGroupOut"])
    types["EditCustomerMatchMembersRequestIn"] = t.struct(
        {
            "advertiserId": t.string(),
            "addedContactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
            "addedMobileDeviceIdList": t.proxy(
                renames["MobileDeviceIdListIn"]
            ).optional(),
        }
    ).named(renames["EditCustomerMatchMembersRequestIn"])
    types["EditCustomerMatchMembersRequestOut"] = t.struct(
        {
            "advertiserId": t.string(),
            "addedContactInfoList": t.proxy(renames["ContactInfoListOut"]).optional(),
            "addedMobileDeviceIdList": t.proxy(
                renames["MobileDeviceIdListOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditCustomerMatchMembersRequestOut"])
    types["BulkEditSitesResponseIn"] = t.struct(
        {"sites": t.array(t.proxy(renames["SiteIn"])).optional()}
    ).named(renames["BulkEditSitesResponseIn"])
    types["BulkEditSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditSitesResponseOut"])
    types["CustomBiddingScriptRefIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["CustomBiddingScriptRefIn"])
    types["CustomBiddingScriptRefOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingScriptRefOut"])
    types["BulkEditAssignedLocationsRequestIn"] = t.struct(
        {
            "createdAssignedLocations": t.array(
                t.proxy(renames["AssignedLocationIn"])
            ).optional(),
            "deletedAssignedLocations": t.array(t.string()).optional(),
        }
    ).named(renames["BulkEditAssignedLocationsRequestIn"])
    types["BulkEditAssignedLocationsRequestOut"] = t.struct(
        {
            "createdAssignedLocations": t.array(
                t.proxy(renames["AssignedLocationOut"])
            ).optional(),
            "deletedAssignedLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedLocationsRequestOut"])
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
    types["SubExchangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string()}
    ).named(renames["SubExchangeAssignedTargetingOptionDetailsIn"])
    types["SubExchangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubExchangeAssignedTargetingOptionDetailsOut"])
    types["ContactInfoListIn"] = t.struct(
        {"contactInfos": t.array(t.proxy(renames["ContactInfoIn"])).optional()}
    ).named(renames["ContactInfoListIn"])
    types["ContactInfoListOut"] = t.struct(
        {
            "contactInfos": t.array(t.proxy(renames["ContactInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoListOut"])
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
    types["ManualTriggerIn"] = t.struct(
        {
            "activationDurationMinutes": t.string(),
            "advertiserId": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["ManualTriggerIn"])
    types["ManualTriggerOut"] = t.struct(
        {
            "activationDurationMinutes": t.string(),
            "advertiserId": t.string(),
            "triggerId": t.string().optional(),
            "displayName": t.string(),
            "latestActivationTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualTriggerOut"])
    types["MaximizeSpendBidStrategyIn"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "performanceGoalType": t.string(),
            "raiseBidForDeals": t.boolean().optional(),
        }
    ).named(renames["MaximizeSpendBidStrategyIn"])
    types["MaximizeSpendBidStrategyOut"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "maxAverageCpmBidAmountMicros": t.string().optional(),
            "performanceGoalType": t.string(),
            "raiseBidForDeals": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaximizeSpendBidStrategyOut"])
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
    types["InventorySourceGroupAssignedTargetingOptionDetailsIn"] = t.struct(
        {"inventorySourceGroupId": t.string()}
    ).named(renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"])
    types["InventorySourceGroupAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "inventorySourceGroupId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceGroupAssignedTargetingOptionDetailsOut"])
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
    types["PrismaConfigIn"] = t.struct(
        {
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeIn"]),
            "supplier": t.string(),
            "prismaType": t.string(),
        }
    ).named(renames["PrismaConfigIn"])
    types["PrismaConfigOut"] = t.struct(
        {
            "prismaCpeCode": t.proxy(renames["PrismaCpeCodeOut"]),
            "supplier": t.string(),
            "prismaType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrismaConfigOut"])
    types["ChannelIn"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "displayName": t.string(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "partnerId": t.string().optional(),
            "displayName": t.string(),
            "negativelyTargetedLineItemCount": t.string().optional(),
            "positivelyTargetedLineItemCount": t.string().optional(),
            "advertiserId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["LanguageTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["LanguageTargetingOptionDetailsIn"])
    types["LanguageTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageTargetingOptionDetailsOut"])
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
    types["ListPartnerAssignedTargetingOptionsResponseIn"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPartnerAssignedTargetingOptionsResponseIn"])
    types["ListPartnerAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "assignedTargetingOptions": t.array(
                t.proxy(renames["AssignedTargetingOptionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPartnerAssignedTargetingOptionsResponseOut"])
    types["CreateSdfDownloadTaskRequestIn"] = t.struct(
        {
            "idFilter": t.proxy(renames["IdFilterIn"]).optional(),
            "parentEntityFilter": t.proxy(renames["ParentEntityFilterIn"]).optional(),
            "inventorySourceFilter": t.proxy(
                renames["InventorySourceFilterIn"]
            ).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "version": t.string(),
        }
    ).named(renames["CreateSdfDownloadTaskRequestIn"])
    types["CreateSdfDownloadTaskRequestOut"] = t.struct(
        {
            "idFilter": t.proxy(renames["IdFilterOut"]).optional(),
            "parentEntityFilter": t.proxy(renames["ParentEntityFilterOut"]).optional(),
            "inventorySourceFilter": t.proxy(
                renames["InventorySourceFilterOut"]
            ).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "version": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSdfDownloadTaskRequestOut"])
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
    types["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"] = t.struct(
        {
            "viewabilityVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "brandLiftVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "reachVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
            "brandSafetyVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigIn"])
            ).optional(),
        }
    ).named(renames["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"])
    types["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"] = t.struct(
        {
            "viewabilityVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "brandLiftVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "reachVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "brandSafetyVendorConfigs": t.array(
                t.proxy(renames["ThirdPartyVendorConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"])
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
    types["YoutubeChannelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "channelId": t.string().optional()}
    ).named(renames["YoutubeChannelAssignedTargetingOptionDetailsIn"])
    types["YoutubeChannelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeChannelAssignedTargetingOptionDetailsOut"])
    types["SensitiveCategoryAssignedTargetingOptionDetailsIn"] = t.struct(
        {"excludedSensitiveCategory": t.string()}
    ).named(renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"])
    types["SensitiveCategoryAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "excludedSensitiveCategory": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveCategoryAssignedTargetingOptionDetailsOut"])
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
    types["YoutubeAndPartnersSettingsIn"] = t.struct(
        {
            "viewFrequencyCap": t.proxy(renames["FrequencyCapIn"]).optional(),
            "relatedVideoIds": t.array(t.string()).optional(),
            "inventorySourceSettings": t.proxy(
                renames["YoutubeAndPartnersInventorySourceConfigIn"]
            ).optional(),
            "thirdPartyMeasurementSettings": t.proxy(
                renames["YoutubeAndPartnersThirdPartyMeasurementSettingsIn"]
            ).optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyIn"]
            ).optional(),
            "leadFormId": t.string().optional(),
            "videoAdSequenceSettings": t.proxy(
                renames["VideoAdSequenceSettingsIn"]
            ).optional(),
            "linkedMerchantId": t.string().optional(),
            "targetFrequency": t.proxy(renames["TargetFrequencyIn"]).optional(),
            "contentCategory": t.string().optional(),
        }
    ).named(renames["YoutubeAndPartnersSettingsIn"])
    types["YoutubeAndPartnersSettingsOut"] = t.struct(
        {
            "viewFrequencyCap": t.proxy(renames["FrequencyCapOut"]).optional(),
            "relatedVideoIds": t.array(t.string()).optional(),
            "inventorySourceSettings": t.proxy(
                renames["YoutubeAndPartnersInventorySourceConfigOut"]
            ).optional(),
            "thirdPartyMeasurementSettings": t.proxy(
                renames["YoutubeAndPartnersThirdPartyMeasurementSettingsOut"]
            ).optional(),
            "biddingStrategy": t.proxy(
                renames["YoutubeAndPartnersBiddingStrategyOut"]
            ).optional(),
            "leadFormId": t.string().optional(),
            "videoAdSequenceSettings": t.proxy(
                renames["VideoAdSequenceSettingsOut"]
            ).optional(),
            "linkedMerchantId": t.string().optional(),
            "targetFrequency": t.proxy(renames["TargetFrequencyOut"]).optional(),
            "contentCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAndPartnersSettingsOut"])
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
    types["AppCategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppCategoryTargetingOptionDetailsIn"])
    types["AppCategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppCategoryTargetingOptionDetailsOut"])
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
    types["MobileAppIn"] = t.struct({"appId": t.string()}).named(renames["MobileAppIn"])
    types["MobileAppOut"] = t.struct(
        {
            "publisher": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileAppOut"])
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
    types["FrequencyCapIn"] = t.struct(
        {
            "maxImpressions": t.integer().optional(),
            "timeUnitCount": t.integer().optional(),
            "maxViews": t.integer().optional(),
            "timeUnit": t.string().optional(),
            "unlimited": t.boolean().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "maxImpressions": t.integer().optional(),
            "timeUnitCount": t.integer().optional(),
            "maxViews": t.integer().optional(),
            "timeUnit": t.string().optional(),
            "unlimited": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
    types["AdlooxIn"] = t.struct(
        {"excludedAdlooxCategories": t.array(t.string()).optional()}
    ).named(renames["AdlooxIn"])
    types["AdlooxOut"] = t.struct(
        {
            "excludedAdlooxCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdlooxOut"])
    types["CreateAssetRequestIn"] = t.struct({"filename": t.string()}).named(
        renames["CreateAssetRequestIn"]
    )
    types["CreateAssetRequestOut"] = t.struct(
        {"filename": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateAssetRequestOut"])
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
    types["DoubleVerifyIn"] = t.struct(
        {
            "customSegmentId": t.string().optional(),
            "displayViewability": t.proxy(
                renames["DoubleVerifyDisplayViewabilityIn"]
            ).optional(),
            "videoViewability": t.proxy(
                renames["DoubleVerifyVideoViewabilityIn"]
            ).optional(),
            "brandSafetyCategories": t.proxy(
                renames["DoubleVerifyBrandSafetyCategoriesIn"]
            ).optional(),
            "appStarRating": t.proxy(renames["DoubleVerifyAppStarRatingIn"]).optional(),
            "avoidedAgeRatings": t.array(t.string()).optional(),
            "fraudInvalidTraffic": t.proxy(
                renames["DoubleVerifyFraudInvalidTrafficIn"]
            ).optional(),
        }
    ).named(renames["DoubleVerifyIn"])
    types["DoubleVerifyOut"] = t.struct(
        {
            "customSegmentId": t.string().optional(),
            "displayViewability": t.proxy(
                renames["DoubleVerifyDisplayViewabilityOut"]
            ).optional(),
            "videoViewability": t.proxy(
                renames["DoubleVerifyVideoViewabilityOut"]
            ).optional(),
            "brandSafetyCategories": t.proxy(
                renames["DoubleVerifyBrandSafetyCategoriesOut"]
            ).optional(),
            "appStarRating": t.proxy(
                renames["DoubleVerifyAppStarRatingOut"]
            ).optional(),
            "avoidedAgeRatings": t.array(t.string()).optional(),
            "fraudInvalidTraffic": t.proxy(
                renames["DoubleVerifyFraudInvalidTrafficOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleVerifyOut"])
    types["RateDetailsIn"] = t.struct(
        {
            "unitsPurchased": t.string(),
            "inventorySourceRateType": t.string().optional(),
            "rate": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["RateDetailsIn"])
    types["RateDetailsOut"] = t.struct(
        {
            "unitsPurchased": t.string(),
            "minimumSpend": t.proxy(renames["MoneyOut"]).optional(),
            "inventorySourceRateType": t.string().optional(),
            "rate": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateDetailsOut"])
    types["SearchTargetingOptionsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
            "businessChainSearchTerms": t.proxy(
                renames["BusinessChainSearchTermsIn"]
            ).optional(),
            "geoRegionSearchTerms": t.proxy(
                renames["GeoRegionSearchTermsIn"]
            ).optional(),
            "advertiserId": t.string(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["SearchTargetingOptionsRequestIn"])
    types["SearchTargetingOptionsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "poiSearchTerms": t.proxy(renames["PoiSearchTermsOut"]).optional(),
            "businessChainSearchTerms": t.proxy(
                renames["BusinessChainSearchTermsOut"]
            ).optional(),
            "geoRegionSearchTerms": t.proxy(
                renames["GeoRegionSearchTermsOut"]
            ).optional(),
            "advertiserId": t.string(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTargetingOptionsRequestOut"])
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
    types["InventorySourceFilterIn"] = t.struct(
        {"inventorySourceIds": t.array(t.string()).optional()}
    ).named(renames["InventorySourceFilterIn"])
    types["InventorySourceFilterOut"] = t.struct(
        {
            "inventorySourceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceFilterOut"])
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
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["DuplicateLineItemRequestIn"] = t.struct(
        {"targetDisplayName": t.string().optional()}
    ).named(renames["DuplicateLineItemRequestIn"])
    types["DuplicateLineItemRequestOut"] = t.struct(
        {
            "targetDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateLineItemRequestOut"])
    types["TargetingOptionIn"] = t.struct(
        {
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentTargetingOptionDetailsIn"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeTargetingOptionDetailsIn"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionTargetingOptionDetailsIn"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainTargetingOptionDetailsIn"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeTargetingOptionDetailsIn"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreTargetingOptionDetailsIn"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionTargetingOptionDetailsIn"]
            ).optional(),
            "digitalContentLabelDetails": t.proxy(
                renames["DigitalContentLabelTargetingOptionDetailsIn"]
            ).optional(),
            "sensitiveCategoryDetails": t.proxy(
                renames["SensitiveCategoryTargetingOptionDetailsIn"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionTargetingOptionDetailsIn"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityTargetingOptionDetailsIn"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryTargetingOptionDetailsIn"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeTargetingOptionDetailsIn"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionTargetingOptionDetailsIn"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemTargetingOptionDetailsIn"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeTargetingOptionDetailsIn"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusTargetingOptionDetailsIn"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeTargetingOptionDetailsIn"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelTargetingOptionDetailsIn"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserTargetingOptionDetailsIn"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeTargetingOptionDetailsIn"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryTargetingOptionDetailsIn"]
            ).optional(),
            "omidDetails": t.proxy(renames["OmidTargetingOptionDetailsIn"]).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationTargetingOptionDetailsIn"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageTargetingOptionDetailsIn"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusTargetingOptionDetailsIn"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspTargetingOptionDetailsIn"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderTargetingOptionDetailsIn"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeTargetingOptionDetailsIn"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionTargetingOptionDetailsIn"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeTargetingOptionDetailsIn"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentTargetingOptionDetailsIn"]
            ).optional(),
            "poiDetails": t.proxy(renames["PoiTargetingOptionDetailsIn"]).optional(),
        }
    ).named(renames["TargetingOptionIn"])
    types["TargetingOptionOut"] = t.struct(
        {
            "targetingOptionId": t.string().optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentTargetingOptionDetailsOut"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeTargetingOptionDetailsOut"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionTargetingOptionDetailsOut"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainTargetingOptionDetailsOut"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeTargetingOptionDetailsOut"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreTargetingOptionDetailsOut"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionTargetingOptionDetailsOut"]
            ).optional(),
            "digitalContentLabelDetails": t.proxy(
                renames["DigitalContentLabelTargetingOptionDetailsOut"]
            ).optional(),
            "sensitiveCategoryDetails": t.proxy(
                renames["SensitiveCategoryTargetingOptionDetailsOut"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionTargetingOptionDetailsOut"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityTargetingOptionDetailsOut"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryTargetingOptionDetailsOut"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeTargetingOptionDetailsOut"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionTargetingOptionDetailsOut"]
            ).optional(),
            "targetingType": t.string().optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemTargetingOptionDetailsOut"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeTargetingOptionDetailsOut"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusTargetingOptionDetailsOut"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeTargetingOptionDetailsOut"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelTargetingOptionDetailsOut"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserTargetingOptionDetailsOut"]
            ).optional(),
            "exchangeDetails": t.proxy(
                renames["ExchangeTargetingOptionDetailsOut"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryTargetingOptionDetailsOut"]
            ).optional(),
            "omidDetails": t.proxy(renames["OmidTargetingOptionDetailsOut"]).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationTargetingOptionDetailsOut"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageTargetingOptionDetailsOut"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusTargetingOptionDetailsOut"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspTargetingOptionDetailsOut"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderTargetingOptionDetailsOut"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeTargetingOptionDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionTargetingOptionDetailsOut"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeTargetingOptionDetailsOut"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentTargetingOptionDetailsOut"]
            ).optional(),
            "poiDetails": t.proxy(renames["PoiTargetingOptionDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingOptionOut"])
    types["HouseholdIncomeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"householdIncome": t.string().optional()}
    ).named(renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"])
    types["HouseholdIncomeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "householdIncome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HouseholdIncomeAssignedTargetingOptionDetailsOut"])
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
    types["ContactInfoIn"] = t.struct(
        {
            "hashedFirstName": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "zipCodes": t.array(t.string()).optional(),
            "hashedPhoneNumbers": t.array(t.string()).optional(),
            "hashedEmails": t.array(t.string()).optional(),
            "countryCode": t.string().optional(),
        }
    ).named(renames["ContactInfoIn"])
    types["ContactInfoOut"] = t.struct(
        {
            "hashedFirstName": t.string().optional(),
            "hashedLastName": t.string().optional(),
            "zipCodes": t.array(t.string()).optional(),
            "hashedPhoneNumbers": t.array(t.string()).optional(),
            "hashedEmails": t.array(t.string()).optional(),
            "countryCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoOut"])
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
    types["GenderTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenderTargetingOptionDetailsIn"])
    types["GenderTargetingOptionDetailsOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderTargetingOptionDetailsOut"])
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
    types["FirstAndThirdPartyAudienceIn"] = t.struct(
        {
            "firstAndThirdPartyAudienceType": t.string().optional(),
            "appId": t.string().optional(),
            "audienceType": t.string().optional(),
            "mobileDeviceIdList": t.proxy(renames["MobileDeviceIdListIn"]).optional(),
            "contactInfoList": t.proxy(renames["ContactInfoListIn"]).optional(),
            "membershipDurationDays": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceIn"])
    types["FirstAndThirdPartyAudienceOut"] = t.struct(
        {
            "audienceSource": t.string().optional(),
            "youtubeAudienceSize": t.string().optional(),
            "firstAndThirdPartyAudienceId": t.string().optional(),
            "displayAudienceSize": t.string().optional(),
            "name": t.string().optional(),
            "displayDesktopAudienceSize": t.string().optional(),
            "gmailAudienceSize": t.string().optional(),
            "firstAndThirdPartyAudienceType": t.string().optional(),
            "displayMobileWebAudienceSize": t.string().optional(),
            "appId": t.string().optional(),
            "audienceType": t.string().optional(),
            "mobileDeviceIdList": t.proxy(renames["MobileDeviceIdListOut"]).optional(),
            "contactInfoList": t.proxy(renames["ContactInfoListOut"]).optional(),
            "displayMobileAppAudienceSize": t.string().optional(),
            "membershipDurationDays": t.string().optional(),
            "activeDisplayAudienceSize": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstAndThirdPartyAudienceOut"])
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
    types["OperatingSystemAssignedTargetingOptionDetailsIn"] = t.struct(
        {"targetingOptionId": t.string(), "negative": t.boolean().optional()}
    ).named(renames["OperatingSystemAssignedTargetingOptionDetailsIn"])
    types["OperatingSystemAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "targetingOptionId": t.string(),
            "displayName": t.string().optional(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemAssignedTargetingOptionDetailsOut"])
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
    types["EditGuaranteedOrderReadAccessorsRequestIn"] = t.struct(
        {
            "partnerId": t.string(),
            "addedAdvertisers": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
            "removedAdvertisers": t.array(t.string()).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsRequestIn"])
    types["EditGuaranteedOrderReadAccessorsRequestOut"] = t.struct(
        {
            "partnerId": t.string(),
            "addedAdvertisers": t.array(t.string()).optional(),
            "readAccessInherited": t.boolean().optional(),
            "removedAdvertisers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditGuaranteedOrderReadAccessorsRequestOut"])
    types["SdfDownloadTaskIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["SdfDownloadTaskIn"])
    types["SdfDownloadTaskOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdfDownloadTaskOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["AudioContentTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AudioContentTypeTargetingOptionDetailsIn"])
    types["AudioContentTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "audioContentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioContentTypeTargetingOptionDetailsOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ReplaceSitesResponseIn"] = t.struct(
        {"sites": t.array(t.proxy(renames["SiteIn"])).optional()}
    ).named(renames["ReplaceSitesResponseIn"])
    types["ReplaceSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceSitesResponseOut"])
    types["AssignedLocationIn"] = t.struct({"targetingOptionId": t.string()}).named(
        renames["AssignedLocationIn"]
    )
    types["AssignedLocationOut"] = t.struct(
        {
            "assignedLocationId": t.string().optional(),
            "targetingOptionId": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedLocationOut"])
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
    types["SiteIn"] = t.struct({"urlOrAppId": t.string()}).named(renames["SiteIn"])
    types["SiteOut"] = t.struct(
        {
            "name": t.string().optional(),
            "urlOrAppId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteOut"])
    types["AssignedUserRoleIn"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "userRole": t.string(),
            "partnerId": t.string().optional(),
        }
    ).named(renames["AssignedUserRoleIn"])
    types["AssignedUserRoleOut"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "userRole": t.string(),
            "partnerId": t.string().optional(),
            "assignedUserRoleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedUserRoleOut"])
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
    types["GenderAssignedTargetingOptionDetailsIn"] = t.struct(
        {"gender": t.string().optional()}
    ).named(renames["GenderAssignedTargetingOptionDetailsIn"])
    types["GenderAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderAssignedTargetingOptionDetailsOut"])
    types["AdvertiserTargetingConfigIn"] = t.struct(
        {"exemptTvFromViewabilityTargeting": t.boolean().optional()}
    ).named(renames["AdvertiserTargetingConfigIn"])
    types["AdvertiserTargetingConfigOut"] = t.struct(
        {
            "exemptTvFromViewabilityTargeting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserTargetingConfigOut"])
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
    types["CarrierAndIspAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["CarrierAndIspAssignedTargetingOptionDetailsIn"])
    types["CarrierAndIspAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarrierAndIspAssignedTargetingOptionDetailsOut"])
    types["TranscodeIn"] = t.struct(
        {
            "audioSampleRateHz": t.string().optional(),
            "name": t.string().optional(),
            "audioBitRateKbps": t.string().optional(),
            "mimeType": t.string().optional(),
            "bitRateKbps": t.string().optional(),
            "fileSizeBytes": t.string().optional(),
            "frameRate": t.number().optional(),
            "transcoded": t.boolean().optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]).optional(),
        }
    ).named(renames["TranscodeIn"])
    types["TranscodeOut"] = t.struct(
        {
            "audioSampleRateHz": t.string().optional(),
            "name": t.string().optional(),
            "audioBitRateKbps": t.string().optional(),
            "mimeType": t.string().optional(),
            "bitRateKbps": t.string().optional(),
            "fileSizeBytes": t.string().optional(),
            "frameRate": t.number().optional(),
            "transcoded": t.boolean().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscodeOut"])
    types["NegativeKeywordListAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negativeKeywordListId": t.string()}
    ).named(renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"])
    types["NegativeKeywordListAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negativeKeywordListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordListAssignedTargetingOptionDetailsOut"])
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
    types["DigitalContentLabelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"excludedContentRatingTier": t.string()}
    ).named(renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"])
    types["DigitalContentLabelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "excludedContentRatingTier": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigitalContentLabelAssignedTargetingOptionDetailsOut"])
    types["PartnerDataAccessConfigIn"] = t.struct(
        {"sdfConfig": t.proxy(renames["SdfConfigIn"]).optional()}
    ).named(renames["PartnerDataAccessConfigIn"])
    types["PartnerDataAccessConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["SdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerDataAccessConfigOut"])
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
    types["InvoiceIn"] = t.struct(
        {
            "subtotalAmountMicros": t.string().optional(),
            "nonBudgetMicros": t.string().optional(),
            "displayName": t.string().optional(),
            "budgetSummaries": t.array(t.proxy(renames["BudgetSummaryIn"])).optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "issueDate": t.proxy(renames["DateIn"]).optional(),
            "name": t.string().optional(),
            "invoiceId": t.string().optional(),
            "serviceDateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "purchaseOrderNumber": t.string().optional(),
            "budgetInvoiceGroupingId": t.string().optional(),
            "currencyCode": t.string().optional(),
            "dueDate": t.proxy(renames["DateIn"]).optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "correctedInvoiceId": t.string().optional(),
            "invoiceType": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
        }
    ).named(renames["InvoiceIn"])
    types["InvoiceOut"] = t.struct(
        {
            "subtotalAmountMicros": t.string().optional(),
            "nonBudgetMicros": t.string().optional(),
            "displayName": t.string().optional(),
            "budgetSummaries": t.array(t.proxy(renames["BudgetSummaryOut"])).optional(),
            "totalTaxAmountMicros": t.string().optional(),
            "pdfUrl": t.string().optional(),
            "paymentsProfileId": t.string().optional(),
            "issueDate": t.proxy(renames["DateOut"]).optional(),
            "name": t.string().optional(),
            "invoiceId": t.string().optional(),
            "serviceDateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "purchaseOrderNumber": t.string().optional(),
            "budgetInvoiceGroupingId": t.string().optional(),
            "currencyCode": t.string().optional(),
            "dueDate": t.proxy(renames["DateOut"]).optional(),
            "replacedInvoiceIds": t.array(t.string()).optional(),
            "correctedInvoiceId": t.string().optional(),
            "invoiceType": t.string().optional(),
            "totalAmountMicros": t.string().optional(),
            "paymentsAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceOut"])
    types["CampaignIn"] = t.struct(
        {
            "campaignFlight": t.proxy(renames["CampaignFlightIn"]),
            "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
            "displayName": t.string(),
            "entityStatus": t.string(),
            "campaignBudgets": t.array(t.proxy(renames["CampaignBudgetIn"])).optional(),
            "campaignGoal": t.proxy(renames["CampaignGoalIn"]),
        }
    ).named(renames["CampaignIn"])
    types["CampaignOut"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "campaignFlight": t.proxy(renames["CampaignFlightOut"]),
            "campaignId": t.string().optional(),
            "frequencyCap": t.proxy(renames["FrequencyCapOut"]),
            "displayName": t.string(),
            "entityStatus": t.string(),
            "updateTime": t.string().optional(),
            "campaignBudgets": t.array(
                t.proxy(renames["CampaignBudgetOut"])
            ).optional(),
            "campaignGoal": t.proxy(renames["CampaignGoalOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CampaignOut"])
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
    types["UrlAssignedTargetingOptionDetailsIn"] = t.struct(
        {"url": t.string(), "negative": t.boolean().optional()}
    ).named(renames["UrlAssignedTargetingOptionDetailsIn"])
    types["UrlAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "url": t.string(),
            "negative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlAssignedTargetingOptionDetailsOut"])
    types["ImageAssetIn"] = t.struct(
        {
            "fullSize": t.proxy(renames["DimensionsIn"]).optional(),
            "fileSize": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["ImageAssetIn"])
    types["ImageAssetOut"] = t.struct(
        {
            "fullSize": t.proxy(renames["DimensionsOut"]).optional(),
            "fileSize": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageAssetOut"])
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
    types["ActivateManualTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivateManualTriggerRequestIn"])
    types["ActivateManualTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateManualTriggerRequestOut"])
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
    types["ContentStreamTypeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContentStreamTypeTargetingOptionDetailsIn"])
    types["ContentStreamTypeTargetingOptionDetailsOut"] = t.struct(
        {
            "contentStreamType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentStreamTypeTargetingOptionDetailsOut"])
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
    types["CustomListGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["CustomListTargetingSettingIn"]))}
    ).named(renames["CustomListGroupIn"])
    types["CustomListGroupOut"] = t.struct(
        {
            "settings": t.array(t.proxy(renames["CustomListTargetingSettingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListGroupOut"])
    types["CombinedAudienceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CombinedAudienceIn"]
    )
    types["CombinedAudienceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "combinedAudienceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CombinedAudienceOut"])
    types["SessionPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"sessionPosition": t.string().optional()}
    ).named(renames["SessionPositionAssignedTargetingOptionDetailsIn"])
    types["SessionPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "sessionPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionPositionAssignedTargetingOptionDetailsOut"])
    types["AudioContentTypeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"audioContentType": t.string().optional()}
    ).named(renames["AudioContentTypeAssignedTargetingOptionDetailsIn"])
    types["AudioContentTypeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "audioContentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioContentTypeAssignedTargetingOptionDetailsOut"])
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
    types["GoogleAudienceGroupIn"] = t.struct(
        {"settings": t.array(t.proxy(renames["GoogleAudienceTargetingSettingIn"]))}
    ).named(renames["GoogleAudienceGroupIn"])
    types["GoogleAudienceGroupOut"] = t.struct(
        {
            "settings": t.array(t.proxy(renames["GoogleAudienceTargetingSettingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceGroupOut"])
    types["OmidTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OmidTargetingOptionDetailsIn"])
    types["OmidTargetingOptionDetailsOut"] = t.struct(
        {
            "omid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmidTargetingOptionDetailsOut"])
    types["SensitiveCategoryTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SensitiveCategoryTargetingOptionDetailsIn"])
    types["SensitiveCategoryTargetingOptionDetailsOut"] = t.struct(
        {
            "sensitiveCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveCategoryTargetingOptionDetailsOut"])
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
    types["DayAndTimeAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "endHour": t.integer(),
            "startHour": t.integer(),
            "dayOfWeek": t.string(),
            "timeZoneResolution": t.string(),
        }
    ).named(renames["DayAndTimeAssignedTargetingOptionDetailsIn"])
    types["DayAndTimeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "endHour": t.integer(),
            "startHour": t.integer(),
            "dayOfWeek": t.string(),
            "timeZoneResolution": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayAndTimeAssignedTargetingOptionDetailsOut"])
    types["NativeContentPositionTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["NativeContentPositionTargetingOptionDetailsIn"])
    types["NativeContentPositionTargetingOptionDetailsOut"] = t.struct(
        {
            "contentPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentPositionTargetingOptionDetailsOut"])
    types["AdvertiserCreativeConfigIn"] = t.struct(
        {
            "obaComplianceDisabled": t.boolean().optional(),
            "videoCreativeDataSharingAuthorized": t.boolean().optional(),
            "dynamicCreativeEnabled": t.boolean().optional(),
            "iasClientId": t.string().optional(),
        }
    ).named(renames["AdvertiserCreativeConfigIn"])
    types["AdvertiserCreativeConfigOut"] = t.struct(
        {
            "obaComplianceDisabled": t.boolean().optional(),
            "videoCreativeDataSharingAuthorized": t.boolean().optional(),
            "dynamicCreativeEnabled": t.boolean().optional(),
            "iasClientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserCreativeConfigOut"])
    types["CustomBiddingAlgorithmIn"] = t.struct(
        {
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "entityStatus": t.string().optional(),
            "customBiddingAlgorithmType": t.string(),
            "displayName": t.string(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["CustomBiddingAlgorithmIn"])
    types["CustomBiddingAlgorithmOut"] = t.struct(
        {
            "customBiddingAlgorithmId": t.string().optional(),
            "sharedAdvertiserIds": t.array(t.string()).optional(),
            "entityStatus": t.string().optional(),
            "customBiddingAlgorithmType": t.string(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "modelDetails": t.array(
                t.proxy(renames["CustomBiddingModelDetailsOut"])
            ).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomBiddingAlgorithmOut"])
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
    types["BrowserTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["BrowserTargetingOptionDetailsIn"])
    types["BrowserTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserTargetingOptionDetailsOut"])
    types["EnvironmentTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EnvironmentTargetingOptionDetailsIn"])
    types["EnvironmentTargetingOptionDetailsOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentTargetingOptionDetailsOut"])
    types["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"] = t.struct(
        {
            "doubleVerify": t.proxy(renames["DoubleVerifyIn"]).optional(),
            "integralAdScience": t.proxy(renames["IntegralAdScienceIn"]).optional(),
            "adloox": t.proxy(renames["AdlooxIn"]).optional(),
        }
    ).named(renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"])
    types["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "doubleVerify": t.proxy(renames["DoubleVerifyOut"]).optional(),
            "integralAdScience": t.proxy(renames["IntegralAdScienceOut"]).optional(),
            "adloox": t.proxy(renames["AdlooxOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"])
    types["VideoPlayerSizeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"videoPlayerSize": t.string().optional()}
    ).named(renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"])
    types["VideoPlayerSizeAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "videoPlayerSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerSizeAssignedTargetingOptionDetailsOut"])
    types["InventorySourceAccessorsAdvertiserAccessorsIn"] = t.struct(
        {"advertiserIds": t.array(t.string()).optional()}
    ).named(renames["InventorySourceAccessorsAdvertiserAccessorsIn"])
    types["InventorySourceAccessorsAdvertiserAccessorsOut"] = t.struct(
        {
            "advertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsAdvertiserAccessorsOut"])
    types["DeviceMakeModelAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"])
    types["DeviceMakeModelAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMakeModelAssignedTargetingOptionDetailsOut"])
    types["YoutubeAdGroupAdIn"] = t.struct(
        {
            "audioAd": t.proxy(renames["AudioAdIn"]).optional(),
            "advertiserId": t.string().optional(),
            "name": t.string().optional(),
            "mastheadAd": t.proxy(renames["MastheadAdIn"]).optional(),
            "entityStatus": t.string().optional(),
            "nonSkippableAd": t.proxy(renames["NonSkippableAdIn"]).optional(),
            "videoPerformanceAd": t.proxy(renames["VideoPerformanceAdIn"]).optional(),
            "adUrls": t.array(t.proxy(renames["AdUrlIn"])).optional(),
            "adGroupId": t.string().optional(),
            "videoDiscoverAd": t.proxy(renames["VideoDiscoveryAdIn"]).optional(),
            "bumperAd": t.proxy(renames["BumperAdIn"]).optional(),
            "inStreamAd": t.proxy(renames["InStreamAdIn"]).optional(),
            "displayName": t.string().optional(),
            "adGroupAdId": t.string().optional(),
            "displayVideoSourceAd": t.proxy(
                renames["DisplayVideoSourceAdIn"]
            ).optional(),
        }
    ).named(renames["YoutubeAdGroupAdIn"])
    types["YoutubeAdGroupAdOut"] = t.struct(
        {
            "audioAd": t.proxy(renames["AudioAdOut"]).optional(),
            "advertiserId": t.string().optional(),
            "name": t.string().optional(),
            "mastheadAd": t.proxy(renames["MastheadAdOut"]).optional(),
            "entityStatus": t.string().optional(),
            "nonSkippableAd": t.proxy(renames["NonSkippableAdOut"]).optional(),
            "videoPerformanceAd": t.proxy(renames["VideoPerformanceAdOut"]).optional(),
            "adUrls": t.array(t.proxy(renames["AdUrlOut"])).optional(),
            "adGroupId": t.string().optional(),
            "videoDiscoverAd": t.proxy(renames["VideoDiscoveryAdOut"]).optional(),
            "bumperAd": t.proxy(renames["BumperAdOut"]).optional(),
            "inStreamAd": t.proxy(renames["InStreamAdOut"]).optional(),
            "displayName": t.string().optional(),
            "adGroupAdId": t.string().optional(),
            "displayVideoSourceAd": t.proxy(
                renames["DisplayVideoSourceAdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeAdGroupAdOut"])
    types["GeoRegionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["GeoRegionAssignedTargetingOptionDetailsIn"])
    types["GeoRegionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "geoRegionType": t.string().optional(),
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoRegionAssignedTargetingOptionDetailsOut"])
    types["InsertionOrderBudgetSegmentIn"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeIn"]),
            "budgetAmountMicros": t.string(),
            "campaignBudgetId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["InsertionOrderBudgetSegmentIn"])
    types["InsertionOrderBudgetSegmentOut"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeOut"]),
            "budgetAmountMicros": t.string(),
            "campaignBudgetId": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderBudgetSegmentOut"])
    types["BulkEditAssignedInventorySourcesRequestIn"] = t.struct(
        {
            "createdAssignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceIn"])
            ).optional(),
            "deletedAssignedInventorySources": t.array(t.string()).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesRequestIn"])
    types["BulkEditAssignedInventorySourcesRequestOut"] = t.struct(
        {
            "createdAssignedInventorySources": t.array(
                t.proxy(renames["AssignedInventorySourceOut"])
            ).optional(),
            "deletedAssignedInventorySources": t.array(t.string()).optional(),
            "partnerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedInventorySourcesRequestOut"])
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
    types["FloodlightGroupIn"] = t.struct(
        {
            "displayName": t.string(),
            "lookbackWindow": t.proxy(renames["LookbackWindowIn"]),
            "activeViewConfig": t.proxy(
                renames["ActiveViewVideoViewabilityMetricConfigIn"]
            ).optional(),
            "customVariables": t.struct({"_": t.string().optional()}).optional(),
            "webTagType": t.string(),
        }
    ).named(renames["FloodlightGroupIn"])
    types["FloodlightGroupOut"] = t.struct(
        {
            "floodlightGroupId": t.string().optional(),
            "displayName": t.string(),
            "lookbackWindow": t.proxy(renames["LookbackWindowOut"]),
            "activeViewConfig": t.proxy(
                renames["ActiveViewVideoViewabilityMetricConfigOut"]
            ).optional(),
            "customVariables": t.struct({"_": t.string().optional()}).optional(),
            "webTagType": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloodlightGroupOut"])
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
    types["AssignedTargetingOptionIn"] = t.struct(
        {
            "exchangeDetails": t.proxy(
                renames["ExchangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "dayAndTimeDetails": t.proxy(
                renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "urlDetails": t.proxy(
                renames["UrlAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "genderDetails": t.proxy(
                renames["GenderAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "inventorySourceGroupDetails": t.proxy(
                renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "appDetails": t.proxy(
                renames["AppAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "keywordDetails": t.proxy(
                renames["KeywordAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "thirdPartyVerifierDetails": t.proxy(
                renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "proximityLocationListDetails": t.proxy(
                renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "youtubeVideoDetails": t.proxy(
                renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "omidDetails": t.proxy(
                renames["OmidAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "audienceGroupDetails": t.proxy(
                renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "inventorySourceDetails": t.proxy(
                renames["InventorySourceAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "sensitiveCategoryExclusionDetails": t.proxy(
                renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "negativeKeywordListDetails": t.proxy(
                renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "channelDetails": t.proxy(
                renames["ChannelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "youtubeChannelDetails": t.proxy(
                renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "digitalContentLabelExclusionDetails": t.proxy(
                renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "regionalLocationListDetails": t.proxy(
                renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "poiDetails": t.proxy(
                renames["PoiAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "sessionPositionDetails": t.proxy(
                renames["SessionPositionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeAssignedTargetingOptionDetailsIn"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
            ).optional(),
        }
    ).named(renames["AssignedTargetingOptionIn"])
    types["AssignedTargetingOptionOut"] = t.struct(
        {
            "exchangeDetails": t.proxy(
                renames["ExchangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "nativeContentPositionDetails": t.proxy(
                renames["NativeContentPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "householdIncomeDetails": t.proxy(
                renames["HouseholdIncomeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "dayAndTimeDetails": t.proxy(
                renames["DayAndTimeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "urlDetails": t.proxy(
                renames["UrlAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "appCategoryDetails": t.proxy(
                renames["AppCategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "genderDetails": t.proxy(
                renames["GenderAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inventorySourceGroupDetails": t.proxy(
                renames["InventorySourceGroupAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "userRewardedContentDetails": t.proxy(
                renames["UserRewardedContentAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "appDetails": t.proxy(
                renames["AppAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "keywordDetails": t.proxy(
                renames["KeywordAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "businessChainDetails": t.proxy(
                renames["BusinessChainAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "thirdPartyVerifierDetails": t.proxy(
                renames["ThirdPartyVerifierAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "proximityLocationListDetails": t.proxy(
                renames["ProximityLocationListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "assignedTargetingOptionIdAlias": t.string().optional(),
            "inheritance": t.string().optional(),
            "youtubeVideoDetails": t.proxy(
                renames["YoutubeVideoAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "omidDetails": t.proxy(
                renames["OmidAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "categoryDetails": t.proxy(
                renames["CategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentInstreamPositionDetails": t.proxy(
                renames["ContentInstreamPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "browserDetails": t.proxy(
                renames["BrowserAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "audienceGroupDetails": t.proxy(
                renames["AudienceGroupAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "inventorySourceDetails": t.proxy(
                renames["InventorySourceAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "sensitiveCategoryExclusionDetails": t.proxy(
                renames["SensitiveCategoryAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentOutstreamPositionDetails": t.proxy(
                renames["ContentOutstreamPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "negativeKeywordListDetails": t.proxy(
                renames["NegativeKeywordListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "channelDetails": t.proxy(
                renames["ChannelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentStreamTypeDetails": t.proxy(
                renames["ContentStreamTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentDurationDetails": t.proxy(
                renames["ContentDurationAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "youtubeChannelDetails": t.proxy(
                renames["YoutubeChannelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "targetingType": t.string().optional(),
            "parentalStatusDetails": t.proxy(
                renames["ParentalStatusAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "subExchangeDetails": t.proxy(
                renames["SubExchangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "digitalContentLabelExclusionDetails": t.proxy(
                renames["DigitalContentLabelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "environmentDetails": t.proxy(
                renames["EnvironmentAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "onScreenPositionDetails": t.proxy(
                renames["OnScreenPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "contentGenreDetails": t.proxy(
                renames["ContentGenreAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "regionalLocationListDetails": t.proxy(
                renames["RegionalLocationListAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "poiDetails": t.proxy(
                renames["PoiAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "carrierAndIspDetails": t.proxy(
                renames["CarrierAndIspAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "assignedTargetingOptionId": t.string().optional(),
            "sessionPositionDetails": t.proxy(
                renames["SessionPositionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "geoRegionDetails": t.proxy(
                renames["GeoRegionAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "languageDetails": t.proxy(
                renames["LanguageAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "viewabilityDetails": t.proxy(
                renames["ViewabilityAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "audioContentTypeDetails": t.proxy(
                renames["AudioContentTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "videoPlayerSizeDetails": t.proxy(
                renames["VideoPlayerSizeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "authorizedSellerStatusDetails": t.proxy(
                renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "operatingSystemDetails": t.proxy(
                renames["OperatingSystemAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "deviceTypeDetails": t.proxy(
                renames["DeviceTypeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "ageRangeDetails": t.proxy(
                renames["AgeRangeAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "deviceMakeModelDetails": t.proxy(
                renames["DeviceMakeModelAssignedTargetingOptionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignedTargetingOptionOut"])
    types["ParentalStatusAssignedTargetingOptionDetailsIn"] = t.struct(
        {"parentalStatus": t.string().optional()}
    ).named(renames["ParentalStatusAssignedTargetingOptionDetailsIn"])
    types["ParentalStatusAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "parentalStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParentalStatusAssignedTargetingOptionDetailsOut"])
    types["ExchangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ExchangeTargetingOptionDetailsIn"])
    types["ExchangeTargetingOptionDetailsOut"] = t.struct(
        {
            "exchange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeTargetingOptionDetailsOut"])
    types["BrowserAssignedTargetingOptionDetailsIn"] = t.struct(
        {"negative": t.boolean().optional(), "targetingOptionId": t.string()}
    ).named(renames["BrowserAssignedTargetingOptionDetailsIn"])
    types["BrowserAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "negative": t.boolean().optional(),
            "displayName": t.string().optional(),
            "targetingOptionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrowserAssignedTargetingOptionDetailsOut"])
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
    types["AdvertiserIn"] = t.struct(
        {
            "displayName": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsIn"]).optional(),
            "entityStatus": t.string(),
            "partnerId": t.string(),
            "servingConfig": t.proxy(renames["AdvertiserTargetingConfigIn"]).optional(),
            "prismaEnabled": t.boolean().optional(),
            "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
            "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
            "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
            "billingConfig": t.proxy(renames["AdvertiserBillingConfigIn"]).optional(),
            "dataAccessConfig": t.proxy(
                renames["AdvertiserDataAccessConfigIn"]
            ).optional(),
        }
    ).named(renames["AdvertiserIn"])
    types["AdvertiserOut"] = t.struct(
        {
            "displayName": t.string(),
            "integrationDetails": t.proxy(renames["IntegrationDetailsOut"]).optional(),
            "entityStatus": t.string(),
            "partnerId": t.string(),
            "servingConfig": t.proxy(
                renames["AdvertiserTargetingConfigOut"]
            ).optional(),
            "prismaEnabled": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigOut"]),
            "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigOut"]),
            "advertiserId": t.string().optional(),
            "name": t.string().optional(),
            "generalConfig": t.proxy(renames["AdvertiserGeneralConfigOut"]),
            "billingConfig": t.proxy(renames["AdvertiserBillingConfigOut"]).optional(),
            "dataAccessConfig": t.proxy(
                renames["AdvertiserDataAccessConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserOut"])
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
    types["AdvertiserDataAccessConfigIn"] = t.struct(
        {"sdfConfig": t.proxy(renames["AdvertiserSdfConfigIn"]).optional()}
    ).named(renames["AdvertiserDataAccessConfigIn"])
    types["AdvertiserDataAccessConfigOut"] = t.struct(
        {
            "sdfConfig": t.proxy(renames["AdvertiserSdfConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserDataAccessConfigOut"])
    types["CreateAssetResponseIn"] = t.struct(
        {"asset": t.proxy(renames["AssetIn"]).optional()}
    ).named(renames["CreateAssetResponseIn"])
    types["CreateAssetResponseOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAssetResponseOut"])
    types["AdUrlIn"] = t.struct(
        {"type": t.string().optional(), "url": t.string().optional()}
    ).named(renames["AdUrlIn"])
    types["AdUrlOut"] = t.struct(
        {
            "type": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUrlOut"])
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
            "entityStatus": t.string().optional(),
            "entityPauseReason": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceStatusOut"])
    types["NegativeKeywordListIn"] = t.struct({"displayName": t.string()}).named(
        renames["NegativeKeywordListIn"]
    )
    types["NegativeKeywordListOut"] = t.struct(
        {
            "negativeKeywordListId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "advertiserId": t.string().optional(),
            "targetedLineItemCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NegativeKeywordListOut"])
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
    types["CreativeConfigIn"] = t.struct(
        {
            "creativeType": t.string().optional(),
            "displayCreativeConfig": t.proxy(
                renames["InventorySourceDisplayCreativeConfigIn"]
            ).optional(),
            "videoCreativeConfig": t.proxy(
                renames["InventorySourceVideoCreativeConfigIn"]
            ).optional(),
        }
    ).named(renames["CreativeConfigIn"])
    types["CreativeConfigOut"] = t.struct(
        {
            "creativeType": t.string().optional(),
            "displayCreativeConfig": t.proxy(
                renames["InventorySourceDisplayCreativeConfigOut"]
            ).optional(),
            "videoCreativeConfig": t.proxy(
                renames["InventorySourceVideoCreativeConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeConfigOut"])
    types["OmidAssignedTargetingOptionDetailsIn"] = t.struct(
        {"omid": t.string().optional()}
    ).named(renames["OmidAssignedTargetingOptionDetailsIn"])
    types["OmidAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "omid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OmidAssignedTargetingOptionDetailsOut"])
    types["ViewabilityTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ViewabilityTargetingOptionDetailsIn"])
    types["ViewabilityTargetingOptionDetailsOut"] = t.struct(
        {
            "viewability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewabilityTargetingOptionDetailsOut"])
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
    types["OperatingSystemTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["OperatingSystemTargetingOptionDetailsIn"])
    types["OperatingSystemTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemTargetingOptionDetailsOut"])
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
    types["InventorySourceAccessorsPartnerAccessorIn"] = t.struct(
        {"partnerId": t.string().optional()}
    ).named(renames["InventorySourceAccessorsPartnerAccessorIn"])
    types["InventorySourceAccessorsPartnerAccessorOut"] = t.struct(
        {
            "partnerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAccessorsPartnerAccessorOut"])
    types["MastheadAdIn"] = t.struct(
        {
            "companionYoutubeVideos": t.array(
                t.proxy(renames["YoutubeVideoDetailsIn"])
            ).optional(),
            "showChannelArt": t.boolean().optional(),
            "headline": t.string().optional(),
            "callToActionFinalUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "description": t.string().optional(),
            "callToActionTrackingUrl": t.string().optional(),
            "videoAspectRatio": t.string().optional(),
            "autoplayVideoDuration": t.string().optional(),
            "callToActionButtonLabel": t.string().optional(),
            "autoplayVideoStartMillisecond": t.string().optional(),
        }
    ).named(renames["MastheadAdIn"])
    types["MastheadAdOut"] = t.struct(
        {
            "companionYoutubeVideos": t.array(
                t.proxy(renames["YoutubeVideoDetailsOut"])
            ).optional(),
            "showChannelArt": t.boolean().optional(),
            "headline": t.string().optional(),
            "callToActionFinalUrl": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "description": t.string().optional(),
            "callToActionTrackingUrl": t.string().optional(),
            "videoAspectRatio": t.string().optional(),
            "autoplayVideoDuration": t.string().optional(),
            "callToActionButtonLabel": t.string().optional(),
            "autoplayVideoStartMillisecond": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MastheadAdOut"])
    types["InsertionOrderBudgetIn"] = t.struct(
        {
            "budgetSegments": t.array(
                t.proxy(renames["InsertionOrderBudgetSegmentIn"])
            ),
            "automationType": t.string().optional(),
            "budgetUnit": t.string(),
        }
    ).named(renames["InsertionOrderBudgetIn"])
    types["InsertionOrderBudgetOut"] = t.struct(
        {
            "budgetSegments": t.array(
                t.proxy(renames["InsertionOrderBudgetSegmentOut"])
            ),
            "automationType": t.string().optional(),
            "budgetUnit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertionOrderBudgetOut"])
    types["ReviewStatusInfoIn"] = t.struct(
        {
            "exchangeReviewStatuses": t.array(
                t.proxy(renames["ExchangeReviewStatusIn"])
            ).optional(),
            "approvalStatus": t.string().optional(),
            "creativeAndLandingPageReviewStatus": t.string().optional(),
            "publisherReviewStatuses": t.array(
                t.proxy(renames["PublisherReviewStatusIn"])
            ).optional(),
            "contentAndPolicyReviewStatus": t.string().optional(),
        }
    ).named(renames["ReviewStatusInfoIn"])
    types["ReviewStatusInfoOut"] = t.struct(
        {
            "exchangeReviewStatuses": t.array(
                t.proxy(renames["ExchangeReviewStatusOut"])
            ).optional(),
            "approvalStatus": t.string().optional(),
            "creativeAndLandingPageReviewStatus": t.string().optional(),
            "publisherReviewStatuses": t.array(
                t.proxy(renames["PublisherReviewStatusOut"])
            ).optional(),
            "contentAndPolicyReviewStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewStatusInfoOut"])
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
    types["DigitalContentLabelTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DigitalContentLabelTargetingOptionDetailsIn"])
    types["DigitalContentLabelTargetingOptionDetailsOut"] = t.struct(
        {
            "contentRatingTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigitalContentLabelTargetingOptionDetailsOut"])
    types["NativeContentPositionAssignedTargetingOptionDetailsIn"] = t.struct(
        {"contentPosition": t.string().optional()}
    ).named(renames["NativeContentPositionAssignedTargetingOptionDetailsIn"])
    types["NativeContentPositionAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "contentPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentPositionAssignedTargetingOptionDetailsOut"])
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
    types["VideoDiscoveryAdIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "headline": t.string().optional(),
            "description2": t.string().optional(),
            "description1": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
        }
    ).named(renames["VideoDiscoveryAdIn"])
    types["VideoDiscoveryAdOut"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "headline": t.string().optional(),
            "description2": t.string().optional(),
            "description1": t.string().optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoDiscoveryAdOut"])
    types["BulkEditAssignedTargetingOptionsResponseIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["BulkEditAssignedTargetingOptionsResponseIn"])
    types["BulkEditAssignedTargetingOptionsResponseOut"] = t.struct(
        {
            "updatedLineItemIds": t.array(t.string()).optional(),
            "failedLineItemIds": t.array(t.string()).optional(),
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkEditAssignedTargetingOptionsResponseOut"])
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
    types["ActiveViewVideoViewabilityMetricConfigIn"] = t.struct(
        {
            "displayName": t.string(),
            "minimumVolume": t.string(),
            "minimumViewability": t.string(),
            "minimumDuration": t.string().optional(),
            "minimumQuartile": t.string().optional(),
        }
    ).named(renames["ActiveViewVideoViewabilityMetricConfigIn"])
    types["ActiveViewVideoViewabilityMetricConfigOut"] = t.struct(
        {
            "displayName": t.string(),
            "minimumVolume": t.string(),
            "minimumViewability": t.string(),
            "minimumDuration": t.string().optional(),
            "minimumQuartile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActiveViewVideoViewabilityMetricConfigOut"])
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
    types["InventorySourceVideoCreativeConfigIn"] = t.struct(
        {"duration": t.string().optional()}
    ).named(renames["InventorySourceVideoCreativeConfigIn"])
    types["InventorySourceVideoCreativeConfigOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceVideoCreativeConfigOut"])
    types["UserIn"] = t.struct(
        {
            "displayName": t.string(),
            "email": t.string(),
            "assignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleIn"])
            ).optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "displayName": t.string(),
            "email": t.string(),
            "name": t.string().optional(),
            "assignedUserRoles": t.array(
                t.proxy(renames["AssignedUserRoleOut"])
            ).optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
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
    types["AuditAdvertiserResponseIn"] = t.struct(
        {
            "negativeKeywordListsCount": t.string().optional(),
            "adGroupCriteriaCount": t.string().optional(),
            "campaignCriteriaCount": t.string().optional(),
            "usedInsertionOrdersCount": t.string().optional(),
            "usedLineItemsCount": t.string().optional(),
            "usedCampaignsCount": t.string().optional(),
            "channelsCount": t.string().optional(),
            "negativelyTargetedChannelsCount": t.string().optional(),
        }
    ).named(renames["AuditAdvertiserResponseIn"])
    types["AuditAdvertiserResponseOut"] = t.struct(
        {
            "negativeKeywordListsCount": t.string().optional(),
            "adGroupCriteriaCount": t.string().optional(),
            "campaignCriteriaCount": t.string().optional(),
            "usedInsertionOrdersCount": t.string().optional(),
            "usedLineItemsCount": t.string().optional(),
            "usedCampaignsCount": t.string().optional(),
            "channelsCount": t.string().optional(),
            "negativelyTargetedChannelsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditAdvertiserResponseOut"])
    types["UserRewardedContentTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UserRewardedContentTargetingOptionDetailsIn"])
    types["UserRewardedContentTargetingOptionDetailsOut"] = t.struct(
        {
            "userRewardedContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRewardedContentTargetingOptionDetailsOut"])
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
    types["ExitEventIn"] = t.struct(
        {
            "reportingName": t.string().optional(),
            "url": t.string(),
            "name": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["ExitEventIn"])
    types["ExitEventOut"] = t.struct(
        {
            "reportingName": t.string().optional(),
            "url": t.string(),
            "name": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExitEventOut"])
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
    types["GoogleAudienceTargetingSettingIn"] = t.struct(
        {"googleAudienceId": t.string()}
    ).named(renames["GoogleAudienceTargetingSettingIn"])
    types["GoogleAudienceTargetingSettingOut"] = t.struct(
        {
            "googleAudienceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAudienceTargetingSettingOut"])
    types["ObaIconIn"] = t.struct(
        {
            "program": t.string().optional(),
            "viewTrackingUrl": t.string(),
            "landingPageUrl": t.string(),
            "resourceUrl": t.string().optional(),
            "clickTrackingUrl": t.string(),
            "resourceMimeType": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsIn"]).optional(),
            "position": t.string().optional(),
        }
    ).named(renames["ObaIconIn"])
    types["ObaIconOut"] = t.struct(
        {
            "program": t.string().optional(),
            "viewTrackingUrl": t.string(),
            "landingPageUrl": t.string(),
            "resourceUrl": t.string().optional(),
            "clickTrackingUrl": t.string(),
            "resourceMimeType": t.string().optional(),
            "dimensions": t.proxy(renames["DimensionsOut"]).optional(),
            "position": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObaIconOut"])
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
    types["InventorySourceAssignedTargetingOptionDetailsIn"] = t.struct(
        {"inventorySourceId": t.string()}
    ).named(renames["InventorySourceAssignedTargetingOptionDetailsIn"])
    types["InventorySourceAssignedTargetingOptionDetailsOut"] = t.struct(
        {
            "inventorySourceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySourceAssignedTargetingOptionDetailsOut"])
    types["DuplicateLineItemResponseIn"] = t.struct(
        {"duplicateLineItemId": t.string().optional()}
    ).named(renames["DuplicateLineItemResponseIn"])
    types["DuplicateLineItemResponseOut"] = t.struct(
        {
            "duplicateLineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DuplicateLineItemResponseOut"])
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
    types["HouseholdIncomeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["HouseholdIncomeTargetingOptionDetailsIn"])
    types["HouseholdIncomeTargetingOptionDetailsOut"] = t.struct(
        {
            "householdIncome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HouseholdIncomeTargetingOptionDetailsOut"])
    types["DeactivateManualTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateManualTriggerRequestIn"])
    types["DeactivateManualTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateManualTriggerRequestOut"])
    types["ExchangeConfigEnabledExchangeIn"] = t.struct(
        {"exchange": t.string().optional()}
    ).named(renames["ExchangeConfigEnabledExchangeIn"])
    types["ExchangeConfigEnabledExchangeOut"] = t.struct(
        {
            "exchange": t.string().optional(),
            "googleAdManagerAgencyId": t.string().optional(),
            "seatId": t.string().optional(),
            "googleAdManagerBuyerNetworkId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExchangeConfigEnabledExchangeOut"])
    types["SubExchangeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SubExchangeTargetingOptionDetailsIn"])
    types["SubExchangeTargetingOptionDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubExchangeTargetingOptionDetailsOut"])
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
    types["CommonInStreamAttributeIn"] = t.struct(
        {
            "actionButtonLabel": t.string().optional(),
            "displayUrl": t.string().optional(),
            "trackingUrl": t.string().optional(),
            "companionBanner": t.proxy(renames["ImageAssetIn"]).optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsIn"]).optional(),
            "finalUrl": t.string().optional(),
            "actionHeadline": t.string().optional(),
        }
    ).named(renames["CommonInStreamAttributeIn"])
    types["CommonInStreamAttributeOut"] = t.struct(
        {
            "actionButtonLabel": t.string().optional(),
            "displayUrl": t.string().optional(),
            "trackingUrl": t.string().optional(),
            "companionBanner": t.proxy(renames["ImageAssetOut"]).optional(),
            "video": t.proxy(renames["YoutubeVideoDetailsOut"]).optional(),
            "finalUrl": t.string().optional(),
            "actionHeadline": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonInStreamAttributeOut"])
    types["PacingIn"] = t.struct(
        {
            "dailyMaxImpressions": t.string().optional(),
            "pacingPeriod": t.string(),
            "dailyMaxMicros": t.string().optional(),
            "pacingType": t.string(),
        }
    ).named(renames["PacingIn"])
    types["PacingOut"] = t.struct(
        {
            "dailyMaxImpressions": t.string().optional(),
            "pacingPeriod": t.string(),
            "dailyMaxMicros": t.string().optional(),
            "pacingType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PacingOut"])
    types["TargetFrequencyIn"] = t.struct(
        {
            "timeUnitCount": t.integer().optional(),
            "timeUnit": t.string().optional(),
            "targetCount": t.string().optional(),
        }
    ).named(renames["TargetFrequencyIn"])
    types["TargetFrequencyOut"] = t.struct(
        {
            "timeUnitCount": t.integer().optional(),
            "timeUnit": t.string().optional(),
            "targetCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetFrequencyOut"])
    types["VideoPlayerSizeTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VideoPlayerSizeTargetingOptionDetailsIn"])
    types["VideoPlayerSizeTargetingOptionDetailsOut"] = t.struct(
        {
            "videoPlayerSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerSizeTargetingOptionDetailsOut"])
    types["GenerateDefaultLineItemRequestIn"] = t.struct(
        {
            "lineItemType": t.string(),
            "insertionOrderId": t.string(),
            "displayName": t.string(),
            "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
        }
    ).named(renames["GenerateDefaultLineItemRequestIn"])
    types["GenerateDefaultLineItemRequestOut"] = t.struct(
        {
            "lineItemType": t.string(),
            "insertionOrderId": t.string(),
            "displayName": t.string(),
            "mobileApp": t.proxy(renames["MobileAppOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateDefaultLineItemRequestOut"])
    types["CustomListTargetingSettingIn"] = t.struct(
        {"customListId": t.string()}
    ).named(renames["CustomListTargetingSettingIn"])
    types["CustomListTargetingSettingOut"] = t.struct(
        {
            "customListId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomListTargetingSettingOut"])
    types["ExchangeAssignedTargetingOptionDetailsIn"] = t.struct(
        {"exchange": t.string()}
    ).named(renames["ExchangeAssignedTargetingOptionDetailsIn"])
    types["ExchangeAssignedTargetingOptionDetailsOut"] = t.struct(
        {"exchange": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExchangeAssignedTargetingOptionDetailsOut"])
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
    types["AuthorizedSellerStatusTargetingOptionDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizedSellerStatusTargetingOptionDetailsIn"])
    types["AuthorizedSellerStatusTargetingOptionDetailsOut"] = t.struct(
        {
            "authorizedSellerStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedSellerStatusTargetingOptionDetailsOut"])
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

    functions = {}
    functions["sdfdownloadtasksCreate"] = displayvideo.post(
        "v2/sdfdownloadtasks",
        t.struct(
            {
                "idFilter": t.proxy(renames["IdFilterIn"]).optional(),
                "parentEntityFilter": t.proxy(
                    renames["ParentEntityFilterIn"]
                ).optional(),
                "inventorySourceFilter": t.proxy(
                    renames["InventorySourceFilterIn"]
                ).optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
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
    functions["mediaUpload"] = displayvideo.get(
        "download/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleBytestreamMediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = displayvideo.get(
        "download/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleBytestreamMediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersBulkEditAssignedUserRoles"] = displayvideo.get(
        "v2/users",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersPatch"] = displayvideo.get(
        "v2/users",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTypesTargetingOptionsGet"] = displayvideo.post(
        "v2/targetingTypes/{targetingType}/targetingOptions:search",
        t.struct(
            {
                "targetingType": t.string(),
                "pageSize": t.integer().optional(),
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["targetingTypesTargetingOptionsList"] = displayvideo.post(
        "v2/targetingTypes/{targetingType}/targetingOptions:search",
        t.struct(
            {
                "targetingType": t.string(),
                "pageSize": t.integer().optional(),
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "poiSearchTerms": t.proxy(renames["PoiSearchTermsIn"]).optional(),
                "businessChainSearchTerms": t.proxy(
                    renames["BusinessChainSearchTermsIn"]
                ).optional(),
                "geoRegionSearchTerms": t.proxy(
                    renames["GeoRegionSearchTermsIn"]
                ).optional(),
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTargetingOptionsResponseOut"]),
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
    functions["floodlightGroupsPatch"] = displayvideo.get(
        "v2/floodlightGroups/{floodlightGroupId}",
        t.struct(
            {
                "partnerId": t.string(),
                "floodlightGroupId": t.string(),
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
                "partnerId": t.string(),
                "floodlightGroupId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FloodlightGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsCreate"] = displayvideo.get(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourceGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourceGroupsPatch"] = displayvideo.get(
        "v2/inventorySourceGroups",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventorySourceGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesCreate"
    ] = displayvideo.delete(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources/{assignedInventorySourceId}",
        t.struct(
            {
                "assignedInventorySourceId": t.string(),
                "inventorySourceGroupId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesList"
    ] = displayvideo.delete(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources/{assignedInventorySourceId}",
        t.struct(
            {
                "assignedInventorySourceId": t.string(),
                "inventorySourceGroupId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesBulkEdit"
    ] = displayvideo.delete(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources/{assignedInventorySourceId}",
        t.struct(
            {
                "assignedInventorySourceId": t.string(),
                "inventorySourceGroupId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourceGroupsAssignedInventorySourcesDelete"
    ] = displayvideo.delete(
        "v2/inventorySourceGroups/{inventorySourceGroupId}/assignedInventorySources/{assignedInventorySourceId}",
        t.struct(
            {
                "assignedInventorySourceId": t.string(),
                "inventorySourceGroupId": t.string(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersGet"] = displayvideo.get(
        "v2/partners",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartnersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersEditAssignedTargetingOptions"] = displayvideo.get(
        "v2/partners",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartnersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersList"] = displayvideo.get(
        "v2/partners",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartnersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "partnersTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.get(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "partnerId": t.string(),
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
        "partnersTargetingTypesAssignedTargetingOptionsCreate"
    ] = displayvideo.get(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "partnerId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersTargetingTypesAssignedTargetingOptionsList"] = displayvideo.get(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "partnerId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersTargetingTypesAssignedTargetingOptionsGet"] = displayvideo.get(
        "v2/partners/{partnerId}/targetingTypes/{targetingType}/assignedTargetingOptions/{assignedTargetingOptionId}",
        t.struct(
            {
                "partnerId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsList"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsCreate"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
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
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
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
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesCreate"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "channelId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesBulkEdit"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "channelId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesDelete"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "channelId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesReplace"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "channelId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersChannelsSitesList"] = displayvideo.get(
        "v2/partners/{partnerId}/channels/{channelId}/sites",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "partnerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "channelId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customListsGet"] = displayvideo.get(
        "v2/customLists",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "advertiserId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersPatch"] = displayvideo.post(
        "v2/guaranteedOrders/{guaranteedOrderId}:editGuaranteedOrderReadAccessors",
        t.struct(
            {
                "guaranteedOrderId": t.string(),
                "partnerId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "readAccessInherited": t.boolean().optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
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
                "partnerId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "readAccessInherited": t.boolean().optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
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
                "partnerId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "readAccessInherited": t.boolean().optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditGuaranteedOrderReadAccessorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["guaranteedOrdersList"] = displayvideo.post(
        "v2/guaranteedOrders/{guaranteedOrderId}:editGuaranteedOrderReadAccessors",
        t.struct(
            {
                "guaranteedOrderId": t.string(),
                "partnerId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "readAccessInherited": t.boolean().optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
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
                "partnerId": t.string(),
                "addedAdvertisers": t.array(t.string()).optional(),
                "readAccessInherited": t.boolean().optional(),
                "removedAdvertisers": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditGuaranteedOrderReadAccessorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["combinedAudiencesGet"] = displayvideo.get(
        "v2/combinedAudiences",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "partnerId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "advertiserId": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "partnerId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCombinedAudiencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersListAssignedTargetingOptions"] = displayvideo.post(
        "v2/advertisers",
        t.struct(
            {
                "displayName": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "partnerId": t.string(),
                "servingConfig": t.proxy(
                    renames["AdvertiserTargetingConfigIn"]
                ).optional(),
                "prismaEnabled": t.boolean().optional(),
                "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
                "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
                "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
                "billingConfig": t.proxy(
                    renames["AdvertiserBillingConfigIn"]
                ).optional(),
                "dataAccessConfig": t.proxy(
                    renames["AdvertiserDataAccessConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersEditAssignedTargetingOptions"] = displayvideo.post(
        "v2/advertisers",
        t.struct(
            {
                "displayName": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "partnerId": t.string(),
                "servingConfig": t.proxy(
                    renames["AdvertiserTargetingConfigIn"]
                ).optional(),
                "prismaEnabled": t.boolean().optional(),
                "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
                "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
                "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
                "billingConfig": t.proxy(
                    renames["AdvertiserBillingConfigIn"]
                ).optional(),
                "dataAccessConfig": t.proxy(
                    renames["AdvertiserDataAccessConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersGet"] = displayvideo.post(
        "v2/advertisers",
        t.struct(
            {
                "displayName": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "partnerId": t.string(),
                "servingConfig": t.proxy(
                    renames["AdvertiserTargetingConfigIn"]
                ).optional(),
                "prismaEnabled": t.boolean().optional(),
                "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
                "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
                "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
                "billingConfig": t.proxy(
                    renames["AdvertiserBillingConfigIn"]
                ).optional(),
                "dataAccessConfig": t.proxy(
                    renames["AdvertiserDataAccessConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersAudit"] = displayvideo.post(
        "v2/advertisers",
        t.struct(
            {
                "displayName": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "partnerId": t.string(),
                "servingConfig": t.proxy(
                    renames["AdvertiserTargetingConfigIn"]
                ).optional(),
                "prismaEnabled": t.boolean().optional(),
                "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
                "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
                "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
                "billingConfig": t.proxy(
                    renames["AdvertiserBillingConfigIn"]
                ).optional(),
                "dataAccessConfig": t.proxy(
                    renames["AdvertiserDataAccessConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersDelete"] = displayvideo.post(
        "v2/advertisers",
        t.struct(
            {
                "displayName": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "partnerId": t.string(),
                "servingConfig": t.proxy(
                    renames["AdvertiserTargetingConfigIn"]
                ).optional(),
                "prismaEnabled": t.boolean().optional(),
                "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
                "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
                "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
                "billingConfig": t.proxy(
                    renames["AdvertiserBillingConfigIn"]
                ).optional(),
                "dataAccessConfig": t.proxy(
                    renames["AdvertiserDataAccessConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersPatch"] = displayvideo.post(
        "v2/advertisers",
        t.struct(
            {
                "displayName": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "partnerId": t.string(),
                "servingConfig": t.proxy(
                    renames["AdvertiserTargetingConfigIn"]
                ).optional(),
                "prismaEnabled": t.boolean().optional(),
                "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
                "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
                "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
                "billingConfig": t.proxy(
                    renames["AdvertiserBillingConfigIn"]
                ).optional(),
                "dataAccessConfig": t.proxy(
                    renames["AdvertiserDataAccessConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersList"] = displayvideo.post(
        "v2/advertisers",
        t.struct(
            {
                "displayName": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "partnerId": t.string(),
                "servingConfig": t.proxy(
                    renames["AdvertiserTargetingConfigIn"]
                ).optional(),
                "prismaEnabled": t.boolean().optional(),
                "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
                "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
                "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
                "billingConfig": t.proxy(
                    renames["AdvertiserBillingConfigIn"]
                ).optional(),
                "dataAccessConfig": t.proxy(
                    renames["AdvertiserDataAccessConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreate"] = displayvideo.post(
        "v2/advertisers",
        t.struct(
            {
                "displayName": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "partnerId": t.string(),
                "servingConfig": t.proxy(
                    renames["AdvertiserTargetingConfigIn"]
                ).optional(),
                "prismaEnabled": t.boolean().optional(),
                "creativeConfig": t.proxy(renames["AdvertiserCreativeConfigIn"]),
                "adServerConfig": t.proxy(renames["AdvertiserAdServerConfigIn"]),
                "generalConfig": t.proxy(renames["AdvertiserGeneralConfigIn"]),
                "billingConfig": t.proxy(
                    renames["AdvertiserBillingConfigIn"]
                ).optional(),
                "dataAccessConfig": t.proxy(
                    renames["AdvertiserDataAccessConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdvertiserOut"]),
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
    functions["advertisersNegativeKeywordListsList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsDelete"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersNegativeKeywordListsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/negativeKeywordLists/{negativeKeywordListId}",
        t.struct(
            {
                "negativeKeywordListId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NegativeKeywordListOut"]),
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
    functions["advertisersInsertionOrdersDelete"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "insertionOrderId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "insertionOrderType": t.string().optional(),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "campaignId": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "displayName": t.string(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersGet"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "insertionOrderId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "insertionOrderType": t.string().optional(),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "campaignId": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "displayName": t.string(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersList"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "insertionOrderId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "insertionOrderType": t.string().optional(),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "campaignId": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "displayName": t.string(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersInsertionOrdersListAssignedTargetingOptions"
    ] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "insertionOrderId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "insertionOrderType": t.string().optional(),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "campaignId": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "displayName": t.string(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersCreate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "insertionOrderId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "insertionOrderType": t.string().optional(),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "campaignId": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "displayName": t.string(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InsertionOrderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInsertionOrdersPatch"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/insertionOrders/{insertionOrderId}",
        t.struct(
            {
                "insertionOrderId": t.string().optional(),
                "updateMask": t.string(),
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "billableOutcome": t.string().optional(),
                "performanceGoal": t.proxy(renames["PerformanceGoalIn"]),
                "insertionOrderType": t.string().optional(),
                "budget": t.proxy(renames["InsertionOrderBudgetIn"]),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "campaignId": t.string(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "entityStatus": t.string(),
                "displayName": t.string(),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]).optional(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "insertionOrderId": t.string(),
                "advertiserId": t.string(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "insertionOrderId": t.string(),
                "advertiserId": t.string(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "insertionOrderId": t.string(),
                "advertiserId": t.string(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "targetingType": t.string(),
                "pageToken": t.string().optional(),
                "insertionOrderId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInsertionOrderAssignedTargetingOptionsResponseOut"]),
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
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
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
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
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
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
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
                "exchangeDetails": t.proxy(
                    renames["ExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "nativeContentPositionDetails": t.proxy(
                    renames["NativeContentPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "householdIncomeDetails": t.proxy(
                    renames["HouseholdIncomeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "dayAndTimeDetails": t.proxy(
                    renames["DayAndTimeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "urlDetails": t.proxy(
                    renames["UrlAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appCategoryDetails": t.proxy(
                    renames["AppCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "genderDetails": t.proxy(
                    renames["GenderAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceGroupDetails": t.proxy(
                    renames["InventorySourceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "userRewardedContentDetails": t.proxy(
                    renames["UserRewardedContentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "appDetails": t.proxy(
                    renames["AppAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "keywordDetails": t.proxy(
                    renames["KeywordAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "businessChainDetails": t.proxy(
                    renames["BusinessChainAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "thirdPartyVerifierDetails": t.proxy(
                    renames["ThirdPartyVerifierAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "proximityLocationListDetails": t.proxy(
                    renames["ProximityLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeVideoDetails": t.proxy(
                    renames["YoutubeVideoAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "omidDetails": t.proxy(
                    renames["OmidAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "categoryDetails": t.proxy(
                    renames["CategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentInstreamPositionDetails": t.proxy(
                    renames["ContentInstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "browserDetails": t.proxy(
                    renames["BrowserAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audienceGroupDetails": t.proxy(
                    renames["AudienceGroupAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "inventorySourceDetails": t.proxy(
                    renames["InventorySourceAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sensitiveCategoryExclusionDetails": t.proxy(
                    renames["SensitiveCategoryAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentOutstreamPositionDetails": t.proxy(
                    renames["ContentOutstreamPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "negativeKeywordListDetails": t.proxy(
                    renames["NegativeKeywordListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "channelDetails": t.proxy(
                    renames["ChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentStreamTypeDetails": t.proxy(
                    renames["ContentStreamTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentDurationDetails": t.proxy(
                    renames["ContentDurationAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "youtubeChannelDetails": t.proxy(
                    renames["YoutubeChannelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "parentalStatusDetails": t.proxy(
                    renames["ParentalStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "subExchangeDetails": t.proxy(
                    renames["SubExchangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "digitalContentLabelExclusionDetails": t.proxy(
                    renames["DigitalContentLabelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "environmentDetails": t.proxy(
                    renames["EnvironmentAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "onScreenPositionDetails": t.proxy(
                    renames["OnScreenPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "contentGenreDetails": t.proxy(
                    renames["ContentGenreAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "regionalLocationListDetails": t.proxy(
                    renames["RegionalLocationListAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "poiDetails": t.proxy(
                    renames["PoiAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "carrierAndIspDetails": t.proxy(
                    renames["CarrierAndIspAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "sessionPositionDetails": t.proxy(
                    renames["SessionPositionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "geoRegionDetails": t.proxy(
                    renames["GeoRegionAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "languageDetails": t.proxy(
                    renames["LanguageAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "viewabilityDetails": t.proxy(
                    renames["ViewabilityAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "audioContentTypeDetails": t.proxy(
                    renames["AudioContentTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "videoPlayerSizeDetails": t.proxy(
                    renames["VideoPlayerSizeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "authorizedSellerStatusDetails": t.proxy(
                    renames["AuthorizedSellerStatusAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "operatingSystemDetails": t.proxy(
                    renames["OperatingSystemAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceTypeDetails": t.proxy(
                    renames["DeviceTypeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "ageRangeDetails": t.proxy(
                    renames["AgeRangeAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "deviceMakeModelDetails": t.proxy(
                    renames["DeviceMakeModelAssignedTargetingOptionDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignedTargetingOptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsGenerateDefault"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
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
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsDuplicate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsDelete"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsBulkUpdate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
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
    ] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
                "lineItemType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LineItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLineItemsCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/lineItems",
        t.struct(
            {
                "advertiserId": t.string().optional(),
                "partnerCosts": t.array(t.proxy(renames["PartnerCostIn"])).optional(),
                "pacing": t.proxy(renames["PacingIn"]),
                "frequencyCap": t.proxy(renames["FrequencyCapIn"]),
                "entityStatus": t.string(),
                "insertionOrderId": t.string(),
                "conversionCounting": t.proxy(
                    renames["ConversionCountingConfigIn"]
                ).optional(),
                "excludeNewExchanges": t.boolean().optional(),
                "budget": t.proxy(renames["LineItemBudgetIn"]),
                "bidStrategy": t.proxy(renames["BiddingStrategyIn"]),
                "creativeIds": t.array(t.string()).optional(),
                "mobileApp": t.proxy(renames["MobileAppIn"]).optional(),
                "integrationDetails": t.proxy(
                    renames["IntegrationDetailsIn"]
                ).optional(),
                "displayName": t.string(),
                "flight": t.proxy(renames["LineItemFlightIn"]),
                "partnerRevenueModel": t.proxy(renames["PartnerRevenueModelIn"]),
                "targetingExpansion": t.proxy(
                    renames["TargetingExpansionConfigIn"]
                ).optional(),
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
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLineItemAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsGet"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLineItemAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsDelete"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLineItemAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLineItemsTargetingTypesAssignedTargetingOptionsList"
    ] = displayvideo.get(
        "v2/advertisers/{advertiserId}/lineItems/{lineItemId}/targetingTypes/{targetingType}/assignedTargetingOptions",
        t.struct(
            {
                "targetingType": t.string(),
                "lineItemId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLineItemAssignedTargetingOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersInvoicesLookupInvoiceCurrency"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/invoices",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
    functions["advertisersManualTriggersList"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}",
        t.struct(
            {
                "triggerId": t.string().optional(),
                "advertiserId": t.string(),
                "updateMask": t.string(),
                "activationDurationMinutes": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersGet"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}",
        t.struct(
            {
                "triggerId": t.string().optional(),
                "advertiserId": t.string(),
                "updateMask": t.string(),
                "activationDurationMinutes": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersCreate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}",
        t.struct(
            {
                "triggerId": t.string().optional(),
                "advertiserId": t.string(),
                "updateMask": t.string(),
                "activationDurationMinutes": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersDeactivate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}",
        t.struct(
            {
                "triggerId": t.string().optional(),
                "advertiserId": t.string(),
                "updateMask": t.string(),
                "activationDurationMinutes": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersActivate"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}",
        t.struct(
            {
                "triggerId": t.string().optional(),
                "advertiserId": t.string(),
                "updateMask": t.string(),
                "activationDurationMinutes": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersManualTriggersPatch"] = displayvideo.patch(
        "v2/advertisers/{advertiserId}/manualTriggers/{triggerId}",
        t.struct(
            {
                "triggerId": t.string().optional(),
                "advertiserId": t.string(),
                "updateMask": t.string(),
                "activationDurationMinutes": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManualTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroups",
        t.struct(
            {
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
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
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "youtubeAdGroupId": t.string(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "targetingType": t.string(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "youtubeAdGroupId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupAssignedTargetingOptionsResponseOut"]),
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
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "campaignId": t.string(),
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
                "advertiserId": t.string(),
                "assignedTargetingOptionId": t.string(),
                "targetingType": t.string(),
                "campaignId": t.string(),
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
    functions["advertisersLocationListsAssignedLocationsList"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations/{assignedLocationId}",
        t.struct(
            {
                "locationListId": t.string(),
                "assignedLocationId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsCreate"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations/{assignedLocationId}",
        t.struct(
            {
                "locationListId": t.string(),
                "assignedLocationId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "advertisersLocationListsAssignedLocationsBulkEdit"
    ] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations/{assignedLocationId}",
        t.struct(
            {
                "locationListId": t.string(),
                "assignedLocationId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersLocationListsAssignedLocationsDelete"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/locationLists/{locationListId}/assignedLocations/{assignedLocationId}",
        t.struct(
            {
                "locationListId": t.string(),
                "assignedLocationId": t.string(),
                "advertiserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesCreate"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesDelete"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesPatch"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersCreativesList"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/creatives",
        t.struct(
            {
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsGet"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsList"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsPatch"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsCreate"] = displayvideo.post(
        "v2/advertisers/{advertiserId}/channels",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersChannelsSitesBulkEdit"] = displayvideo.delete(
        "v2/advertisers/{advertiserId}/channels/{channelId}/sites/{urlOrAppId}",
        t.struct(
            {
                "urlOrAppId": t.string(),
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "partnerId": t.string().optional(),
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
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "partnerId": t.string().optional(),
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
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "partnerId": t.string().optional(),
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
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "partnerId": t.string().optional(),
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
                "advertiserId": t.string().optional(),
                "channelId": t.string(),
                "partnerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["advertisersYoutubeAdGroupAdsGet"] = displayvideo.get(
        "v2/advertisers/{advertiserId}/youtubeAdGroupAds",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
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
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "advertiserId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListYoutubeAdGroupAdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesCreate"] = displayvideo.post(
        "v2/inventorySources/{inventorySourceId}:editInventorySourceReadWriteAccessors",
        t.struct(
            {
                "inventorySourceId": t.string(),
                "assignPartner": t.boolean().optional(),
                "partnerId": t.string(),
                "advertisersUpdate": t.proxy(
                    renames[
                        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceAccessorsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesPatch"] = displayvideo.post(
        "v2/inventorySources/{inventorySourceId}:editInventorySourceReadWriteAccessors",
        t.struct(
            {
                "inventorySourceId": t.string(),
                "assignPartner": t.boolean().optional(),
                "partnerId": t.string(),
                "advertisersUpdate": t.proxy(
                    renames[
                        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceAccessorsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesList"] = displayvideo.post(
        "v2/inventorySources/{inventorySourceId}:editInventorySourceReadWriteAccessors",
        t.struct(
            {
                "inventorySourceId": t.string(),
                "assignPartner": t.boolean().optional(),
                "partnerId": t.string(),
                "advertisersUpdate": t.proxy(
                    renames[
                        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceAccessorsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inventorySourcesGet"] = displayvideo.post(
        "v2/inventorySources/{inventorySourceId}:editInventorySourceReadWriteAccessors",
        t.struct(
            {
                "inventorySourceId": t.string(),
                "assignPartner": t.boolean().optional(),
                "partnerId": t.string(),
                "advertisersUpdate": t.proxy(
                    renames[
                        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceAccessorsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "inventorySourcesEditInventorySourceReadWriteAccessors"
    ] = displayvideo.post(
        "v2/inventorySources/{inventorySourceId}:editInventorySourceReadWriteAccessors",
        t.struct(
            {
                "inventorySourceId": t.string(),
                "assignPartner": t.boolean().optional(),
                "partnerId": t.string(),
                "advertisersUpdate": t.proxy(
                    renames[
                        "EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdateIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventorySourceAccessorsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesGet"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences/{firstAndThirdPartyAudienceId}:editCustomerMatchMembers",
        t.struct(
            {
                "firstAndThirdPartyAudienceId": t.string(),
                "advertiserId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
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
                "advertiserId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditCustomerMatchMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["firstAndThirdPartyAudiencesList"] = displayvideo.post(
        "v2/firstAndThirdPartyAudiences/{firstAndThirdPartyAudienceId}:editCustomerMatchMembers",
        t.struct(
            {
                "firstAndThirdPartyAudienceId": t.string(),
                "advertiserId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
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
                "advertiserId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
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
                "advertiserId": t.string(),
                "addedContactInfoList": t.proxy(
                    renames["ContactInfoListIn"]
                ).optional(),
                "addedMobileDeviceIdList": t.proxy(
                    renames["MobileDeviceIdListIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EditCustomerMatchMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsPatch"] = displayvideo.get(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingAlgorithmsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsCreate"] = displayvideo.get(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingAlgorithmsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsGet"] = displayvideo.get(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingAlgorithmsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsUploadScript"] = displayvideo.get(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingAlgorithmsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsList"] = displayvideo.get(
        "v2/customBiddingAlgorithms",
        t.struct(
            {
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingAlgorithmsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsGet"] = displayvideo.get(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingScriptsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customBiddingAlgorithmsScriptsCreate"] = displayvideo.get(
        "v2/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts",
        t.struct(
            {
                "customBiddingAlgorithmId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomBiddingScriptsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="displayvideo", renames=renames, types=types, functions=functions
    )
