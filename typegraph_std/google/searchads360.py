from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_searchads360():
    searchads360 = HTTPRuntime("https://searchads360.googleapis.com/")

    renames = {
        "ErrorResponse": "_searchads360_1_ErrorResponse",
        "GoogleAdsSearchads360V0Common__GenderInfoIn": "_searchads360_2_GoogleAdsSearchads360V0Common__GenderInfoIn",
        "GoogleAdsSearchads360V0Common__GenderInfoOut": "_searchads360_3_GoogleAdsSearchads360V0Common__GenderInfoOut",
        "GoogleAdsSearchads360V0Resources__CustomerClientIn": "_searchads360_4_GoogleAdsSearchads360V0Resources__CustomerClientIn",
        "GoogleAdsSearchads360V0Resources__CustomerClientOut": "_searchads360_5_GoogleAdsSearchads360V0Resources__CustomerClientOut",
        "GoogleAdsSearchads360V0Common__MaximizeConversionsIn": "_searchads360_6_GoogleAdsSearchads360V0Common__MaximizeConversionsIn",
        "GoogleAdsSearchads360V0Common__MaximizeConversionsOut": "_searchads360_7_GoogleAdsSearchads360V0Common__MaximizeConversionsOut",
        "GoogleAdsSearchads360V0Resources__CampaignBudgetIn": "_searchads360_8_GoogleAdsSearchads360V0Resources__CampaignBudgetIn",
        "GoogleAdsSearchads360V0Resources__CampaignBudgetOut": "_searchads360_9_GoogleAdsSearchads360V0Resources__CampaignBudgetOut",
        "GoogleAdsSearchads360V0Services__ListCustomColumnsResponseIn": "_searchads360_10_GoogleAdsSearchads360V0Services__ListCustomColumnsResponseIn",
        "GoogleAdsSearchads360V0Services__ListCustomColumnsResponseOut": "_searchads360_11_GoogleAdsSearchads360V0Services__ListCustomColumnsResponseOut",
        "GoogleAdsSearchads360V0Errors__ErrorDetailsIn": "_searchads360_12_GoogleAdsSearchads360V0Errors__ErrorDetailsIn",
        "GoogleAdsSearchads360V0Errors__ErrorDetailsOut": "_searchads360_13_GoogleAdsSearchads360V0Errors__ErrorDetailsOut",
        "GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn": "_searchads360_14_GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut": "_searchads360_15_GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut",
        "GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn": "_searchads360_16_GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn",
        "GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut": "_searchads360_17_GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut",
        "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoIn": "_searchads360_18_GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoOut": "_searchads360_19_GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoOut",
        "GoogleAdsSearchads360V0Resources__CampaignLabelIn": "_searchads360_20_GoogleAdsSearchads360V0Resources__CampaignLabelIn",
        "GoogleAdsSearchads360V0Resources__CampaignLabelOut": "_searchads360_21_GoogleAdsSearchads360V0Resources__CampaignLabelOut",
        "GoogleAdsSearchads360V0Common__MetricsIn": "_searchads360_22_GoogleAdsSearchads360V0Common__MetricsIn",
        "GoogleAdsSearchads360V0Common__MetricsOut": "_searchads360_23_GoogleAdsSearchads360V0Common__MetricsOut",
        "GoogleAdsSearchads360V0Resources__LabelIn": "_searchads360_24_GoogleAdsSearchads360V0Resources__LabelIn",
        "GoogleAdsSearchads360V0Resources__LabelOut": "_searchads360_25_GoogleAdsSearchads360V0Resources__LabelOut",
        "GoogleAdsSearchads360V0Common__TargetRoasIn": "_searchads360_26_GoogleAdsSearchads360V0Common__TargetRoasIn",
        "GoogleAdsSearchads360V0Common__TargetRoasOut": "_searchads360_27_GoogleAdsSearchads360V0Common__TargetRoasOut",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestIn": "_searchads360_28_GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestIn",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestOut": "_searchads360_29_GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestOut",
        "GoogleAdsSearchads360V0Common__DeviceInfoIn": "_searchads360_30_GoogleAdsSearchads360V0Common__DeviceInfoIn",
        "GoogleAdsSearchads360V0Common__DeviceInfoOut": "_searchads360_31_GoogleAdsSearchads360V0Common__DeviceInfoOut",
        "GoogleAdsSearchads360V0Resources__LocationViewIn": "_searchads360_32_GoogleAdsSearchads360V0Resources__LocationViewIn",
        "GoogleAdsSearchads360V0Resources__LocationViewOut": "_searchads360_33_GoogleAdsSearchads360V0Resources__LocationViewOut",
        "GoogleAdsSearchads360V0Common__CustomParameterIn": "_searchads360_34_GoogleAdsSearchads360V0Common__CustomParameterIn",
        "GoogleAdsSearchads360V0Common__CustomParameterOut": "_searchads360_35_GoogleAdsSearchads360V0Common__CustomParameterOut",
        "GoogleAdsSearchads360V0Resources__CustomerIn": "_searchads360_36_GoogleAdsSearchads360V0Resources__CustomerIn",
        "GoogleAdsSearchads360V0Resources__CustomerOut": "_searchads360_37_GoogleAdsSearchads360V0Resources__CustomerOut",
        "GoogleAdsSearchads360V0Common__MobileAppAssetIn": "_searchads360_38_GoogleAdsSearchads360V0Common__MobileAppAssetIn",
        "GoogleAdsSearchads360V0Common__MobileAppAssetOut": "_searchads360_39_GoogleAdsSearchads360V0Common__MobileAppAssetOut",
        "GoogleAdsSearchads360V0Common__PercentCpcIn": "_searchads360_40_GoogleAdsSearchads360V0Common__PercentCpcIn",
        "GoogleAdsSearchads360V0Common__PercentCpcOut": "_searchads360_41_GoogleAdsSearchads360V0Common__PercentCpcOut",
        "GoogleAdsSearchads360V0Common__ManualCpmIn": "_searchads360_42_GoogleAdsSearchads360V0Common__ManualCpmIn",
        "GoogleAdsSearchads360V0Common__ManualCpmOut": "_searchads360_43_GoogleAdsSearchads360V0Common__ManualCpmOut",
        "GoogleAdsSearchads360V0Resources__AssetIn": "_searchads360_44_GoogleAdsSearchads360V0Resources__AssetIn",
        "GoogleAdsSearchads360V0Resources__AssetOut": "_searchads360_45_GoogleAdsSearchads360V0Resources__AssetOut",
        "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn": "_searchads360_46_GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut": "_searchads360_47_GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut",
        "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn": "_searchads360_48_GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn",
        "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut": "_searchads360_49_GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut",
        "GoogleAdsSearchads360V0Common__TargetImpressionShareIn": "_searchads360_50_GoogleAdsSearchads360V0Common__TargetImpressionShareIn",
        "GoogleAdsSearchads360V0Common__TargetImpressionShareOut": "_searchads360_51_GoogleAdsSearchads360V0Common__TargetImpressionShareOut",
        "GoogleAdsSearchads360V0Resources__BiddingStrategyIn": "_searchads360_52_GoogleAdsSearchads360V0Resources__BiddingStrategyIn",
        "GoogleAdsSearchads360V0Resources__BiddingStrategyOut": "_searchads360_53_GoogleAdsSearchads360V0Resources__BiddingStrategyOut",
        "GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementIn": "_searchads360_54_GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementIn",
        "GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementOut": "_searchads360_55_GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementOut",
        "GoogleAdsSearchads360V0Resources__AdGroupLabelIn": "_searchads360_56_GoogleAdsSearchads360V0Resources__AdGroupLabelIn",
        "GoogleAdsSearchads360V0Resources__AdGroupLabelOut": "_searchads360_57_GoogleAdsSearchads360V0Resources__AdGroupLabelOut",
        "GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn": "_searchads360_58_GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut": "_searchads360_59_GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut",
        "GoogleAdsSearchads360V0Resources__AdGroupIn": "_searchads360_60_GoogleAdsSearchads360V0Resources__AdGroupIn",
        "GoogleAdsSearchads360V0Resources__AdGroupOut": "_searchads360_61_GoogleAdsSearchads360V0Resources__AdGroupOut",
        "GoogleAdsSearchads360V0Common__WebpageConditionInfoIn": "_searchads360_62_GoogleAdsSearchads360V0Common__WebpageConditionInfoIn",
        "GoogleAdsSearchads360V0Common__WebpageConditionInfoOut": "_searchads360_63_GoogleAdsSearchads360V0Common__WebpageConditionInfoOut",
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn": "_searchads360_64_GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut": "_searchads360_65_GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut",
        "GoogleAdsSearchads360V0Resources__SearchAds360FieldIn": "_searchads360_66_GoogleAdsSearchads360V0Resources__SearchAds360FieldIn",
        "GoogleAdsSearchads360V0Resources__SearchAds360FieldOut": "_searchads360_67_GoogleAdsSearchads360V0Resources__SearchAds360FieldOut",
        "GoogleAdsSearchads360V0Resources__ConversionActionIn": "_searchads360_68_GoogleAdsSearchads360V0Resources__ConversionActionIn",
        "GoogleAdsSearchads360V0Resources__ConversionActionOut": "_searchads360_69_GoogleAdsSearchads360V0Resources__ConversionActionOut",
        "GoogleAdsSearchads360V0Resources__AssetSetIn": "_searchads360_70_GoogleAdsSearchads360V0Resources__AssetSetIn",
        "GoogleAdsSearchads360V0Resources__AssetSetOut": "_searchads360_71_GoogleAdsSearchads360V0Resources__AssetSetOut",
        "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingIn": "_searchads360_72_GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingIn",
        "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut": "_searchads360_73_GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut",
        "GoogleAdsSearchads360V0Services__SearchAds360RowIn": "_searchads360_74_GoogleAdsSearchads360V0Services__SearchAds360RowIn",
        "GoogleAdsSearchads360V0Services__SearchAds360RowOut": "_searchads360_75_GoogleAdsSearchads360V0Services__SearchAds360RowOut",
        "GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingIn": "_searchads360_76_GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut": "_searchads360_77_GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut",
        "GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn": "_searchads360_78_GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn",
        "GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut": "_searchads360_79_GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut",
        "GoogleAdsSearchads360V0Resources__GenderViewIn": "_searchads360_80_GoogleAdsSearchads360V0Resources__GenderViewIn",
        "GoogleAdsSearchads360V0Resources__GenderViewOut": "_searchads360_81_GoogleAdsSearchads360V0Resources__GenderViewOut",
        "GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn": "_searchads360_82_GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn",
        "GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut": "_searchads360_83_GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut",
        "GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseIn": "_searchads360_84_GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseIn",
        "GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseOut": "_searchads360_85_GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseOut",
        "GoogleAdsSearchads360V0Common__SegmentsIn": "_searchads360_86_GoogleAdsSearchads360V0Common__SegmentsIn",
        "GoogleAdsSearchads360V0Common__SegmentsOut": "_searchads360_87_GoogleAdsSearchads360V0Common__SegmentsOut",
        "GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn": "_searchads360_88_GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn",
        "GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut": "_searchads360_89_GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut",
        "GoogleAdsSearchads360V0Common__KeywordInfoIn": "_searchads360_90_GoogleAdsSearchads360V0Common__KeywordInfoIn",
        "GoogleAdsSearchads360V0Common__KeywordInfoOut": "_searchads360_91_GoogleAdsSearchads360V0Common__KeywordInfoOut",
        "GoogleAdsSearchads360V0Common__ListingGroupInfoIn": "_searchads360_92_GoogleAdsSearchads360V0Common__ListingGroupInfoIn",
        "GoogleAdsSearchads360V0Common__ListingGroupInfoOut": "_searchads360_93_GoogleAdsSearchads360V0Common__ListingGroupInfoOut",
        "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationIn": "_searchads360_94_GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationIn",
        "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationOut": "_searchads360_95_GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationOut",
        "GoogleAdsSearchads360V0Resources__AdGroupCriterionIn": "_searchads360_96_GoogleAdsSearchads360V0Resources__AdGroupCriterionIn",
        "GoogleAdsSearchads360V0Resources__AdGroupCriterionOut": "_searchads360_97_GoogleAdsSearchads360V0Resources__AdGroupCriterionOut",
        "GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn": "_searchads360_98_GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn",
        "GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut": "_searchads360_99_GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut",
        "GoogleAdsSearchads360V0Common__EnhancedCpcIn": "_searchads360_100_GoogleAdsSearchads360V0Common__EnhancedCpcIn",
        "GoogleAdsSearchads360V0Common__EnhancedCpcOut": "_searchads360_101_GoogleAdsSearchads360V0Common__EnhancedCpcOut",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseIn": "_searchads360_102_GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseIn",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut": "_searchads360_103_GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut",
        "GoogleAdsSearchads360V0Common__AgeRangeInfoIn": "_searchads360_104_GoogleAdsSearchads360V0Common__AgeRangeInfoIn",
        "GoogleAdsSearchads360V0Common__AgeRangeInfoOut": "_searchads360_105_GoogleAdsSearchads360V0Common__AgeRangeInfoOut",
        "GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoIn": "_searchads360_106_GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoIn",
        "GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoOut": "_searchads360_107_GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoOut",
        "GoogleAdsSearchads360V0Common__FrequencyCapEntryIn": "_searchads360_108_GoogleAdsSearchads360V0Common__FrequencyCapEntryIn",
        "GoogleAdsSearchads360V0Common__FrequencyCapEntryOut": "_searchads360_109_GoogleAdsSearchads360V0Common__FrequencyCapEntryOut",
        "GoogleAdsSearchads360V0Resources__CampaignIn": "_searchads360_110_GoogleAdsSearchads360V0Resources__CampaignIn",
        "GoogleAdsSearchads360V0Resources__CampaignOut": "_searchads360_111_GoogleAdsSearchads360V0Resources__CampaignOut",
        "GoogleAdsSearchads360V0Resources__KeywordViewIn": "_searchads360_112_GoogleAdsSearchads360V0Resources__KeywordViewIn",
        "GoogleAdsSearchads360V0Resources__KeywordViewOut": "_searchads360_113_GoogleAdsSearchads360V0Resources__KeywordViewOut",
        "GoogleAdsSearchads360V0Common__TargetSpendIn": "_searchads360_114_GoogleAdsSearchads360V0Common__TargetSpendIn",
        "GoogleAdsSearchads360V0Common__TargetSpendOut": "_searchads360_115_GoogleAdsSearchads360V0Common__TargetSpendOut",
        "GoogleAdsSearchads360V0Resources__CampaignCriterionIn": "_searchads360_116_GoogleAdsSearchads360V0Resources__CampaignCriterionIn",
        "GoogleAdsSearchads360V0Resources__CampaignCriterionOut": "_searchads360_117_GoogleAdsSearchads360V0Resources__CampaignCriterionOut",
        "GoogleAdsSearchads360V0Common__TextLabelIn": "_searchads360_118_GoogleAdsSearchads360V0Common__TextLabelIn",
        "GoogleAdsSearchads360V0Common__TextLabelOut": "_searchads360_119_GoogleAdsSearchads360V0Common__TextLabelOut",
        "GoogleAdsSearchads360V0Resources__AdIn": "_searchads360_120_GoogleAdsSearchads360V0Resources__AdIn",
        "GoogleAdsSearchads360V0Resources__AdOut": "_searchads360_121_GoogleAdsSearchads360V0Resources__AdOut",
        "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsIn": "_searchads360_122_GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsIn",
        "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut": "_searchads360_123_GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut",
        "GoogleAdsSearchads360V0Common__LanguageInfoIn": "_searchads360_124_GoogleAdsSearchads360V0Common__LanguageInfoIn",
        "GoogleAdsSearchads360V0Common__LanguageInfoOut": "_searchads360_125_GoogleAdsSearchads360V0Common__LanguageInfoOut",
        "GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn": "_searchads360_126_GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn",
        "GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut": "_searchads360_127_GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut",
        "GoogleAdsSearchads360V0Common__TargetRestrictionIn": "_searchads360_128_GoogleAdsSearchads360V0Common__TargetRestrictionIn",
        "GoogleAdsSearchads360V0Common__TargetRestrictionOut": "_searchads360_129_GoogleAdsSearchads360V0Common__TargetRestrictionOut",
        "GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn": "_searchads360_130_GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut": "_searchads360_131_GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut",
        "GoogleAdsSearchads360V0Resources__ConversionTrackingSettingIn": "_searchads360_132_GoogleAdsSearchads360V0Resources__ConversionTrackingSettingIn",
        "GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut": "_searchads360_133_GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut",
        "GoogleAdsSearchads360V0Common__ValueIn": "_searchads360_134_GoogleAdsSearchads360V0Common__ValueIn",
        "GoogleAdsSearchads360V0Common__ValueOut": "_searchads360_135_GoogleAdsSearchads360V0Common__ValueOut",
        "GoogleAdsSearchads360V0Resources__CustomColumnIn": "_searchads360_136_GoogleAdsSearchads360V0Resources__CustomColumnIn",
        "GoogleAdsSearchads360V0Resources__CustomColumnOut": "_searchads360_137_GoogleAdsSearchads360V0Resources__CustomColumnOut",
        "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewIn": "_searchads360_138_GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewIn",
        "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewOut": "_searchads360_139_GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewOut",
        "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingIn": "_searchads360_140_GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingOut": "_searchads360_141_GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingOut",
        "GoogleAdsSearchads360V0Errors__ErrorCodeIn": "_searchads360_142_GoogleAdsSearchads360V0Errors__ErrorCodeIn",
        "GoogleAdsSearchads360V0Errors__ErrorCodeOut": "_searchads360_143_GoogleAdsSearchads360V0Errors__ErrorCodeOut",
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn": "_searchads360_144_GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut": "_searchads360_145_GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut",
        "GoogleAdsSearchads360V0Errors__SearchAds360FailureIn": "_searchads360_146_GoogleAdsSearchads360V0Errors__SearchAds360FailureIn",
        "GoogleAdsSearchads360V0Errors__SearchAds360FailureOut": "_searchads360_147_GoogleAdsSearchads360V0Errors__SearchAds360FailureOut",
        "GoogleAdsSearchads360V0Errors__ErrorLocationIn": "_searchads360_148_GoogleAdsSearchads360V0Errors__ErrorLocationIn",
        "GoogleAdsSearchads360V0Errors__ErrorLocationOut": "_searchads360_149_GoogleAdsSearchads360V0Errors__ErrorLocationOut",
        "GoogleAdsSearchads360V0Services__CustomColumnHeaderIn": "_searchads360_150_GoogleAdsSearchads360V0Services__CustomColumnHeaderIn",
        "GoogleAdsSearchads360V0Services__CustomColumnHeaderOut": "_searchads360_151_GoogleAdsSearchads360V0Services__CustomColumnHeaderOut",
        "GoogleAdsSearchads360V0Common__LocationInfoIn": "_searchads360_152_GoogleAdsSearchads360V0Common__LocationInfoIn",
        "GoogleAdsSearchads360V0Common__LocationInfoOut": "_searchads360_153_GoogleAdsSearchads360V0Common__LocationInfoOut",
        "GoogleAdsSearchads360V0Resources__UserListIn": "_searchads360_154_GoogleAdsSearchads360V0Resources__UserListIn",
        "GoogleAdsSearchads360V0Resources__UserListOut": "_searchads360_155_GoogleAdsSearchads360V0Resources__UserListOut",
        "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingIn": "_searchads360_156_GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingOut": "_searchads360_157_GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingOut",
        "GoogleAdsSearchads360V0Common__KeywordIn": "_searchads360_158_GoogleAdsSearchads360V0Common__KeywordIn",
        "GoogleAdsSearchads360V0Common__KeywordOut": "_searchads360_159_GoogleAdsSearchads360V0Common__KeywordOut",
        "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsIn": "_searchads360_160_GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsIn",
        "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut": "_searchads360_161_GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut",
        "GoogleAdsSearchads360V0Resources__WebpageViewIn": "_searchads360_162_GoogleAdsSearchads360V0Resources__WebpageViewIn",
        "GoogleAdsSearchads360V0Resources__WebpageViewOut": "_searchads360_163_GoogleAdsSearchads360V0Resources__WebpageViewOut",
        "GoogleAdsSearchads360V0Common__LocationGroupInfoIn": "_searchads360_164_GoogleAdsSearchads360V0Common__LocationGroupInfoIn",
        "GoogleAdsSearchads360V0Common__LocationGroupInfoOut": "_searchads360_165_GoogleAdsSearchads360V0Common__LocationGroupInfoOut",
        "GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn": "_searchads360_166_GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn",
        "GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut": "_searchads360_167_GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut",
        "GoogleAdsSearchads360V0Common__TargetCpaIn": "_searchads360_168_GoogleAdsSearchads360V0Common__TargetCpaIn",
        "GoogleAdsSearchads360V0Common__TargetCpaOut": "_searchads360_169_GoogleAdsSearchads360V0Common__TargetCpaOut",
        "GoogleAdsSearchads360V0Common__TargetingSettingIn": "_searchads360_170_GoogleAdsSearchads360V0Common__TargetingSettingIn",
        "GoogleAdsSearchads360V0Common__TargetingSettingOut": "_searchads360_171_GoogleAdsSearchads360V0Common__TargetingSettingOut",
        "GoogleAdsSearchads360V0Resources__AdGroupAdIn": "_searchads360_172_GoogleAdsSearchads360V0Resources__AdGroupAdIn",
        "GoogleAdsSearchads360V0Resources__AdGroupAdOut": "_searchads360_173_GoogleAdsSearchads360V0Resources__AdGroupAdOut",
        "GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn": "_searchads360_174_GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn",
        "GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut": "_searchads360_175_GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut",
        "GoogleAdsSearchads360V0Common__MaximizeConversionValueIn": "_searchads360_176_GoogleAdsSearchads360V0Common__MaximizeConversionValueIn",
        "GoogleAdsSearchads360V0Common__MaximizeConversionValueOut": "_searchads360_177_GoogleAdsSearchads360V0Common__MaximizeConversionValueOut",
        "GoogleAdsSearchads360V0Common__TargetCpmIn": "_searchads360_178_GoogleAdsSearchads360V0Common__TargetCpmIn",
        "GoogleAdsSearchads360V0Common__TargetCpmOut": "_searchads360_179_GoogleAdsSearchads360V0Common__TargetCpmOut",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360RequestIn": "_searchads360_180_GoogleAdsSearchads360V0Services__SearchSearchAds360RequestIn",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360RequestOut": "_searchads360_181_GoogleAdsSearchads360V0Services__SearchSearchAds360RequestOut",
        "GoogleAdsSearchads360V0Resources__AgeRangeViewIn": "_searchads360_182_GoogleAdsSearchads360V0Resources__AgeRangeViewIn",
        "GoogleAdsSearchads360V0Resources__AgeRangeViewOut": "_searchads360_183_GoogleAdsSearchads360V0Resources__AgeRangeViewOut",
        "GoogleAdsSearchads360V0Common__ManualCpaIn": "_searchads360_184_GoogleAdsSearchads360V0Common__ManualCpaIn",
        "GoogleAdsSearchads360V0Common__ManualCpaOut": "_searchads360_185_GoogleAdsSearchads360V0Common__ManualCpaOut",
        "GoogleAdsSearchads360V0Common__UserListInfoIn": "_searchads360_186_GoogleAdsSearchads360V0Common__UserListInfoIn",
        "GoogleAdsSearchads360V0Common__UserListInfoOut": "_searchads360_187_GoogleAdsSearchads360V0Common__UserListInfoOut",
        "GoogleAdsSearchads360V0Common__TargetOutrankShareIn": "_searchads360_188_GoogleAdsSearchads360V0Common__TargetOutrankShareIn",
        "GoogleAdsSearchads360V0Common__TargetOutrankShareOut": "_searchads360_189_GoogleAdsSearchads360V0Common__TargetOutrankShareOut",
        "GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn": "_searchads360_190_GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn",
        "GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut": "_searchads360_191_GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseIn": "_searchads360_192_GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseIn",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseOut": "_searchads360_193_GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseOut",
        "GoogleAdsSearchads360V0Resources__ProductGroupViewIn": "_searchads360_194_GoogleAdsSearchads360V0Resources__ProductGroupViewIn",
        "GoogleAdsSearchads360V0Resources__ProductGroupViewOut": "_searchads360_195_GoogleAdsSearchads360V0Resources__ProductGroupViewOut",
        "GoogleAdsSearchads360V0Common__ManualCpcIn": "_searchads360_196_GoogleAdsSearchads360V0Common__ManualCpcIn",
        "GoogleAdsSearchads360V0Common__ManualCpcOut": "_searchads360_197_GoogleAdsSearchads360V0Common__ManualCpcOut",
        "GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn": "_searchads360_198_GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn",
        "GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut": "_searchads360_199_GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut",
        "GoogleAdsSearchads360V0Common__WebpageInfoIn": "_searchads360_200_GoogleAdsSearchads360V0Common__WebpageInfoIn",
        "GoogleAdsSearchads360V0Common__WebpageInfoOut": "_searchads360_201_GoogleAdsSearchads360V0Common__WebpageInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAdsSearchads360V0Common__GenderInfoIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__GenderInfoIn"])
    types["GoogleAdsSearchads360V0Common__GenderInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__GenderInfoOut"])
    types["GoogleAdsSearchads360V0Resources__CustomerClientIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerClientIn"])
    types["GoogleAdsSearchads360V0Resources__CustomerClientOut"] = t.struct(
        {
            "level": t.string().optional(),
            "hidden": t.boolean().optional(),
            "status": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "timeZone": t.string().optional(),
            "clientCustomer": t.string().optional(),
            "appliedLabels": t.array(t.string()).optional(),
            "resourceName": t.string().optional(),
            "manager": t.boolean().optional(),
            "id": t.string().optional(),
            "currencyCode": t.string().optional(),
            "testAccount": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerClientOut"])
    types["GoogleAdsSearchads360V0Common__MaximizeConversionsIn"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "targetCpaMicros": t.string().optional(),
            "cpcBidFloorMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MaximizeConversionsIn"])
    types["GoogleAdsSearchads360V0Common__MaximizeConversionsOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "targetCpaMicros": t.string().optional(),
            "cpcBidFloorMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MaximizeConversionsOut"])
    types["GoogleAdsSearchads360V0Resources__CampaignBudgetIn"] = t.struct(
        {
            "deliveryMethod": t.string().optional(),
            "resourceName": t.string().optional(),
            "amountMicros": t.string().optional(),
            "period": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignBudgetIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignBudgetOut"] = t.struct(
        {
            "deliveryMethod": t.string().optional(),
            "resourceName": t.string().optional(),
            "amountMicros": t.string().optional(),
            "period": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignBudgetOut"])
    types["GoogleAdsSearchads360V0Services__ListCustomColumnsResponseIn"] = t.struct(
        {
            "customColumns": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Resources__CustomColumnIn"])
            ).optional()
        }
    ).named(renames["GoogleAdsSearchads360V0Services__ListCustomColumnsResponseIn"])
    types["GoogleAdsSearchads360V0Services__ListCustomColumnsResponseOut"] = t.struct(
        {
            "customColumns": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Resources__CustomColumnOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__ListCustomColumnsResponseOut"])
    types["GoogleAdsSearchads360V0Errors__ErrorDetailsIn"] = t.struct(
        {
            "quotaErrorDetails": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn"]
            ).optional(),
            "unpublishedErrorCode": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__ErrorDetailsIn"])
    types["GoogleAdsSearchads360V0Errors__ErrorDetailsOut"] = t.struct(
        {
            "quotaErrorDetails": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut"]
            ).optional(),
            "unpublishedErrorCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__ErrorDetailsOut"])
    types["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn"] = t.struct(
        {
            "adTrackingId": t.string().optional(),
            "headline": t.string().optional(),
            "displayUrl": t.string().optional(),
            "displayMobileUrl": t.string().optional(),
            "description1": t.string().optional(),
            "description2": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn"])
    types["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut"] = t.struct(
        {
            "adTrackingId": t.string().optional(),
            "headline": t.string().optional(),
            "displayUrl": t.string().optional(),
            "displayMobileUrl": t.string().optional(),
            "description1": t.string().optional(),
            "description2": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut"])
    types[
        "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoIn"
    ] = t.struct(
        {
            "path1": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "path2": t.string().optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoIn"]
    )
    types[
        "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoOut"
    ] = t.struct(
        {
            "path1": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "path2": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoOut"]
    )
    types["GoogleAdsSearchads360V0Resources__CampaignLabelIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "label": t.string().optional(),
            "campaign": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignLabelIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignLabelOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "label": t.string().optional(),
            "campaign": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignLabelOut"])
    types["GoogleAdsSearchads360V0Common__MetricsIn"] = t.struct(
        {
            "clicks": t.string().optional(),
            "searchExactMatchImpressionShare": t.number().optional(),
            "searchRankLostTopImpressionShare": t.number().optional(),
            "conversionsValue": t.number().optional(),
            "historicalCreativeQualityScore": t.string().optional(),
            "valuePerAllConversionsByConversionDate": t.number().optional(),
            "conversionsFromInteractionsRate": t.number().optional(),
            "historicalQualityScore": t.string().optional(),
            "conversionsByConversionDate": t.number().optional(),
            "averageCpm": t.number().optional(),
            "costMicros": t.string().optional(),
            "ctr": t.number().optional(),
            "mobileFriendlyClicksPercentage": t.number().optional(),
            "invalidClickRate": t.number().optional(),
            "searchClickShare": t.number().optional(),
            "allConversionsFromOtherEngagement": t.number().optional(),
            "interactionEventTypes": t.array(t.string()).optional(),
            "interactions": t.string().optional(),
            "valuePerConversionsByConversionDate": t.number().optional(),
            "allConversionsValueByConversionDate": t.number().optional(),
            "valuePerConversion": t.number().optional(),
            "searchBudgetLostImpressionShare": t.number().optional(),
            "contentImpressionShare": t.number().optional(),
            "costPerCurrentModelAttributedConversion": t.number().optional(),
            "topImpressionPercentage": t.number().optional(),
            "contentRankLostImpressionShare": t.number().optional(),
            "searchRankLostAbsoluteTopImpressionShare": t.number().optional(),
            "allConversionsFromClickToCall": t.number().optional(),
            "allConversionsValuePerCost": t.number().optional(),
            "conversionsFromInteractionsValuePerInteraction": t.number().optional(),
            "conversions": t.number().optional(),
            "searchTopImpressionShare": t.number().optional(),
            "crossDeviceConversionsValue": t.number().optional(),
            "allConversionsFromStoreVisit": t.number().optional(),
            "allConversionsFromOrder": t.number().optional(),
            "conversionsValueByConversionDate": t.number().optional(),
            "searchBudgetLostTopImpressionShare": t.number().optional(),
            "allConversionsByConversionDate": t.number().optional(),
            "allConversionsFromMenu": t.number().optional(),
            "searchAbsoluteTopImpressionShare": t.number().optional(),
            "allConversionsFromStoreWebsite": t.number().optional(),
            "allConversionsValue": t.number().optional(),
            "costPerAllConversions": t.number().optional(),
            "averageCost": t.number().optional(),
            "allConversionsFromDirections": t.number().optional(),
            "visits": t.number().optional(),
            "clientAccountConversionsValue": t.number().optional(),
            "searchRankLostImpressionShare": t.number().optional(),
            "allConversionsFromInteractionsRate": t.number().optional(),
            "clientAccountConversions": t.number().optional(),
            "absoluteTopImpressionPercentage": t.number().optional(),
            "interactionRate": t.number().optional(),
            "allConversionsFromInteractionsValuePerInteraction": t.number().optional(),
            "valuePerAllConversions": t.number().optional(),
            "costPerConversion": t.number().optional(),
            "conversionsValuePerCost": t.number().optional(),
            "averageCpc": t.number().optional(),
            "impressions": t.string().optional(),
            "clientAccountViewThroughConversions": t.string().optional(),
            "contentBudgetLostImpressionShare": t.number().optional(),
            "historicalLandingPageQualityScore": t.string().optional(),
            "historicalSearchPredictedCtr": t.string().optional(),
            "invalidClicks": t.string().optional(),
            "crossDeviceConversions": t.number().optional(),
            "searchBudgetLostAbsoluteTopImpressionShare": t.number().optional(),
            "allConversions": t.number().optional(),
            "searchImpressionShare": t.number().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MetricsIn"])
    types["GoogleAdsSearchads360V0Common__MetricsOut"] = t.struct(
        {
            "clicks": t.string().optional(),
            "searchExactMatchImpressionShare": t.number().optional(),
            "searchRankLostTopImpressionShare": t.number().optional(),
            "conversionsValue": t.number().optional(),
            "historicalCreativeQualityScore": t.string().optional(),
            "valuePerAllConversionsByConversionDate": t.number().optional(),
            "conversionsFromInteractionsRate": t.number().optional(),
            "historicalQualityScore": t.string().optional(),
            "conversionsByConversionDate": t.number().optional(),
            "averageCpm": t.number().optional(),
            "costMicros": t.string().optional(),
            "ctr": t.number().optional(),
            "mobileFriendlyClicksPercentage": t.number().optional(),
            "invalidClickRate": t.number().optional(),
            "searchClickShare": t.number().optional(),
            "allConversionsFromOtherEngagement": t.number().optional(),
            "interactionEventTypes": t.array(t.string()).optional(),
            "interactions": t.string().optional(),
            "valuePerConversionsByConversionDate": t.number().optional(),
            "allConversionsValueByConversionDate": t.number().optional(),
            "valuePerConversion": t.number().optional(),
            "searchBudgetLostImpressionShare": t.number().optional(),
            "contentImpressionShare": t.number().optional(),
            "costPerCurrentModelAttributedConversion": t.number().optional(),
            "topImpressionPercentage": t.number().optional(),
            "contentRankLostImpressionShare": t.number().optional(),
            "searchRankLostAbsoluteTopImpressionShare": t.number().optional(),
            "allConversionsFromClickToCall": t.number().optional(),
            "allConversionsValuePerCost": t.number().optional(),
            "conversionsFromInteractionsValuePerInteraction": t.number().optional(),
            "conversions": t.number().optional(),
            "searchTopImpressionShare": t.number().optional(),
            "crossDeviceConversionsValue": t.number().optional(),
            "allConversionsFromStoreVisit": t.number().optional(),
            "allConversionsFromOrder": t.number().optional(),
            "conversionsValueByConversionDate": t.number().optional(),
            "searchBudgetLostTopImpressionShare": t.number().optional(),
            "allConversionsByConversionDate": t.number().optional(),
            "allConversionsFromMenu": t.number().optional(),
            "searchAbsoluteTopImpressionShare": t.number().optional(),
            "allConversionsFromStoreWebsite": t.number().optional(),
            "allConversionsValue": t.number().optional(),
            "costPerAllConversions": t.number().optional(),
            "averageCost": t.number().optional(),
            "allConversionsFromDirections": t.number().optional(),
            "visits": t.number().optional(),
            "clientAccountConversionsValue": t.number().optional(),
            "searchRankLostImpressionShare": t.number().optional(),
            "allConversionsFromInteractionsRate": t.number().optional(),
            "clientAccountConversions": t.number().optional(),
            "absoluteTopImpressionPercentage": t.number().optional(),
            "interactionRate": t.number().optional(),
            "allConversionsFromInteractionsValuePerInteraction": t.number().optional(),
            "valuePerAllConversions": t.number().optional(),
            "costPerConversion": t.number().optional(),
            "conversionsValuePerCost": t.number().optional(),
            "averageCpc": t.number().optional(),
            "impressions": t.string().optional(),
            "clientAccountViewThroughConversions": t.string().optional(),
            "contentBudgetLostImpressionShare": t.number().optional(),
            "historicalLandingPageQualityScore": t.string().optional(),
            "historicalSearchPredictedCtr": t.string().optional(),
            "invalidClicks": t.string().optional(),
            "crossDeviceConversions": t.number().optional(),
            "searchBudgetLostAbsoluteTopImpressionShare": t.number().optional(),
            "allConversions": t.number().optional(),
            "searchImpressionShare": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MetricsOut"])
    types["GoogleAdsSearchads360V0Resources__LabelIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "textLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TextLabelIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__LabelIn"])
    types["GoogleAdsSearchads360V0Resources__LabelOut"] = t.struct(
        {
            "id": t.string().optional(),
            "status": t.string().optional(),
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "textLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TextLabelOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__LabelOut"])
    types["GoogleAdsSearchads360V0Common__TargetRoasIn"] = t.struct(
        {
            "cpcBidFloorMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "targetRoas": t.number(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetRoasIn"])
    types["GoogleAdsSearchads360V0Common__TargetRoasOut"] = t.struct(
        {
            "cpcBidFloorMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "targetRoas": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetRoasOut"])
    types[
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestIn"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "query": t.string(),
            "pageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestIn"]
    )
    types[
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestOut"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "query": t.string(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestOut"]
    )
    types["GoogleAdsSearchads360V0Common__DeviceInfoIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__DeviceInfoIn"])
    types["GoogleAdsSearchads360V0Common__DeviceInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__DeviceInfoOut"])
    types["GoogleAdsSearchads360V0Resources__LocationViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__LocationViewIn"])
    types["GoogleAdsSearchads360V0Resources__LocationViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__LocationViewOut"])
    types["GoogleAdsSearchads360V0Common__CustomParameterIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__CustomParameterIn"])
    types["GoogleAdsSearchads360V0Common__CustomParameterOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__CustomParameterOut"])
    types["GoogleAdsSearchads360V0Resources__CustomerIn"] = t.struct(
        {
            "trackingUrlTemplate": t.string().optional(),
            "currencyCode": t.string().optional(),
            "finalUrlSuffix": t.string().optional(),
            "timeZone": t.string().optional(),
            "autoTaggingEnabled": t.boolean().optional(),
            "descriptiveName": t.string().optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerIn"])
    types["GoogleAdsSearchads360V0Resources__CustomerOut"] = t.struct(
        {
            "trackingUrlTemplate": t.string().optional(),
            "doubleClickCampaignManagerSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut"
                ]
            ).optional(),
            "conversionTrackingSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut"
                ]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "id": t.string().optional(),
            "engineId": t.string().optional(),
            "manager": t.boolean().optional(),
            "currencyCode": t.string().optional(),
            "status": t.string().optional(),
            "finalUrlSuffix": t.string().optional(),
            "accountType": t.string().optional(),
            "timeZone": t.string().optional(),
            "accountStatus": t.string().optional(),
            "autoTaggingEnabled": t.boolean().optional(),
            "creationTime": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerOut"])
    types["GoogleAdsSearchads360V0Common__MobileAppAssetIn"] = t.struct(
        {"appId": t.string(), "appStore": t.string()}
    ).named(renames["GoogleAdsSearchads360V0Common__MobileAppAssetIn"])
    types["GoogleAdsSearchads360V0Common__MobileAppAssetOut"] = t.struct(
        {
            "appId": t.string(),
            "appStore": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MobileAppAssetOut"])
    types["GoogleAdsSearchads360V0Common__PercentCpcIn"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "enhancedCpcEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__PercentCpcIn"])
    types["GoogleAdsSearchads360V0Common__PercentCpcOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "enhancedCpcEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__PercentCpcOut"])
    types["GoogleAdsSearchads360V0Common__ManualCpmIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpmIn"])
    types["GoogleAdsSearchads360V0Common__ManualCpmOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpmOut"])
    types["GoogleAdsSearchads360V0Resources__AssetIn"] = t.struct(
        {
            "mobileAppAsset": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MobileAppAssetIn"]
            ).optional(),
            "resourceName": t.string().optional(),
            "finalUrls": t.array(t.string()).optional(),
            "trackingUrlTemplate": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AssetIn"])
    types["GoogleAdsSearchads360V0Resources__AssetOut"] = t.struct(
        {
            "mobileAppAsset": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MobileAppAssetOut"]
            ).optional(),
            "resourceName": t.string().optional(),
            "creationTime": t.string().optional(),
            "finalUrls": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "trackingUrlTemplate": t.string().optional(),
            "engineStatus": t.string().optional(),
            "status": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AssetOut"])
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn"
    ] = t.struct(
        {
            "languageCode": t.string(),
            "useSuppliedUrlsOnly": t.boolean().optional(),
            "domainName": t.string(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut"
    ] = t.struct(
        {
            "languageCode": t.string(),
            "useSuppliedUrlsOnly": t.boolean().optional(),
            "domainName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn"
    ] = t.struct(
        {
            "alwaysUseDefaultValue": t.boolean().optional(),
            "defaultCurrencyCode": t.string().optional(),
            "defaultValue": t.number().optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut"
    ] = t.struct(
        {
            "alwaysUseDefaultValue": t.boolean().optional(),
            "defaultCurrencyCode": t.string().optional(),
            "defaultValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut"]
    )
    types["GoogleAdsSearchads360V0Common__TargetImpressionShareIn"] = t.struct(
        {
            "location": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "locationFractionMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetImpressionShareIn"])
    types["GoogleAdsSearchads360V0Common__TargetImpressionShareOut"] = t.struct(
        {
            "location": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "locationFractionMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetImpressionShareOut"])
    types["GoogleAdsSearchads360V0Resources__BiddingStrategyIn"] = t.struct(
        {
            "targetSpend": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetSpendIn"]
            ).optional(),
            "targetImpressionShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetImpressionShareIn"]
            ).optional(),
            "targetRoas": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetRoasIn"]
            ).optional(),
            "resourceName": t.string().optional(),
            "maximizeConversions": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionsIn"]
            ).optional(),
            "targetOutrankShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetOutrankShareIn"]
            ).optional(),
            "maximizeConversionValue": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueIn"]
            ).optional(),
            "enhancedCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__EnhancedCpcIn"]
            ).optional(),
            "targetCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpaIn"]
            ).optional(),
            "name": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__BiddingStrategyIn"])
    types["GoogleAdsSearchads360V0Resources__BiddingStrategyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "targetSpend": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetSpendOut"]
            ).optional(),
            "targetImpressionShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetImpressionShareOut"]
            ).optional(),
            "status": t.string().optional(),
            "targetRoas": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetRoasOut"]
            ).optional(),
            "campaignCount": t.string().optional(),
            "id": t.string().optional(),
            "effectiveCurrencyCode": t.string().optional(),
            "nonRemovedCampaignCount": t.string().optional(),
            "resourceName": t.string().optional(),
            "maximizeConversions": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionsOut"]
            ).optional(),
            "targetOutrankShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetOutrankShareOut"]
            ).optional(),
            "maximizeConversionValue": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueOut"]
            ).optional(),
            "enhancedCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__EnhancedCpcOut"]
            ).optional(),
            "targetCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpaOut"]
            ).optional(),
            "name": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__BiddingStrategyOut"])
    types["GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementIn"] = t.struct(
        {"fieldName": t.string().optional(), "index": t.integer().optional()}
    ).named(renames["GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementIn"])
    types["GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementOut"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupLabelIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "adGroup": t.string().optional(),
            "label": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupLabelIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupLabelOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "adGroup": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupLabelOut"])
    types["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn"])
    types["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupIn"] = t.struct(
        {
            "status": t.string().optional(),
            "cpcBidMicros": t.string().optional(),
            "type": t.string().optional(),
            "resourceName": t.string().optional(),
            "adRotationMode": t.string().optional(),
            "targetingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetingSettingIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupOut"] = t.struct(
        {
            "id": t.string().optional(),
            "status": t.string().optional(),
            "engineStatus": t.string().optional(),
            "cpcBidMicros": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "startDate": t.string().optional(),
            "resourceName": t.string().optional(),
            "engineId": t.string().optional(),
            "adRotationMode": t.string().optional(),
            "endDate": t.string().optional(),
            "targetingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetingSettingOut"]
            ).optional(),
            "name": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "creationTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupOut"])
    types["GoogleAdsSearchads360V0Common__WebpageConditionInfoIn"] = t.struct(
        {
            "operand": t.string().optional(),
            "argument": t.string().optional(),
            "operator": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__WebpageConditionInfoIn"])
    types["GoogleAdsSearchads360V0Common__WebpageConditionInfoOut"] = t.struct(
        {
            "operand": t.string().optional(),
            "argument": t.string().optional(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__WebpageConditionInfoOut"])
    types["GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn"] = t.struct(
        {
            "path2": t.string().optional(),
            "headline": t.string().optional(),
            "path1": t.string().optional(),
            "headline2": t.string().optional(),
            "description2": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "description1": t.string().optional(),
            "headline3": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn"])
    types[
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut"
    ] = t.struct(
        {
            "path2": t.string().optional(),
            "headline": t.string().optional(),
            "path1": t.string().optional(),
            "headline2": t.string().optional(),
            "description2": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "description1": t.string().optional(),
            "headline3": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut"]
    )
    types["GoogleAdsSearchads360V0Resources__SearchAds360FieldIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldIn"])
    types["GoogleAdsSearchads360V0Resources__SearchAds360FieldOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "segments": t.array(t.string()).optional(),
            "selectableWith": t.array(t.string()).optional(),
            "dataType": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "isRepeated": t.boolean().optional(),
            "enumValues": t.array(t.string()).optional(),
            "attributeResources": t.array(t.string()).optional(),
            "sortable": t.boolean().optional(),
            "selectable": t.boolean().optional(),
            "typeUrl": t.string().optional(),
            "filterable": t.boolean().optional(),
            "name": t.string().optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldOut"])
    types["GoogleAdsSearchads360V0Resources__ConversionActionIn"] = t.struct(
        {
            "valueSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn"
                ]
            ).optional(),
            "category": t.string().optional(),
            "name": t.string().optional(),
            "attributionModelSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsIn"
                ]
            ).optional(),
            "status": t.string().optional(),
            "clickThroughLookbackWindowDays": t.string().optional(),
            "resourceName": t.string().optional(),
            "appId": t.string().optional(),
            "includeInClientAccountConversionsMetric": t.boolean().optional(),
            "type": t.string().optional(),
            "primaryForGoal": t.boolean().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__ConversionActionIn"])
    types["GoogleAdsSearchads360V0Resources__ConversionActionOut"] = t.struct(
        {
            "valueSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut"
                ]
            ).optional(),
            "category": t.string().optional(),
            "name": t.string().optional(),
            "includeInConversionsMetric": t.boolean().optional(),
            "attributionModelSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut"
                ]
            ).optional(),
            "status": t.string().optional(),
            "ownerCustomer": t.string().optional(),
            "floodlightSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut"
                ]
            ).optional(),
            "clickThroughLookbackWindowDays": t.string().optional(),
            "resourceName": t.string().optional(),
            "appId": t.string().optional(),
            "includeInClientAccountConversionsMetric": t.boolean().optional(),
            "type": t.string().optional(),
            "primaryForGoal": t.boolean().optional(),
            "creationTime": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__ConversionActionOut"])
    types["GoogleAdsSearchads360V0Resources__AssetSetIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__AssetSetIn"])
    types["GoogleAdsSearchads360V0Resources__AssetSetOut"] = t.struct(
        {
            "id": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AssetSetOut"])
    types[
        "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut"
    ] = t.struct(
        {
            "timeZone": t.string().optional(),
            "advertiserId": t.string().optional(),
            "networkId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut"
        ]
    )
    types["GoogleAdsSearchads360V0Services__SearchAds360RowIn"] = t.struct(
        {
            "customerClient": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerClientIn"]
            ).optional(),
            "segments": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SegmentsIn"]
            ).optional(),
            "campaign": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignIn"]
            ).optional(),
            "metrics": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MetricsIn"]
            ).optional(),
            "biddingStrategy": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__BiddingStrategyIn"]
            ).optional(),
            "locationView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__LocationViewIn"]
            ).optional(),
            "customer": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerIn"]
            ).optional(),
            "campaignCriterion": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignCriterionIn"]
            ).optional(),
            "customColumns": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__ValueIn"])
            ).optional(),
            "ageRangeView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AgeRangeViewIn"]
            ).optional(),
            "adGroupLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupLabelIn"]
            ).optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__UserListIn"]
            ).optional(),
            "campaignLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignLabelIn"]
            ).optional(),
            "adGroupCriterionLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn"]
            ).optional(),
            "adGroupAdLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn"]
            ).optional(),
            "webpageView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__WebpageViewIn"]
            ).optional(),
            "productGroupView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__ProductGroupViewIn"]
            ).optional(),
            "assetSet": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AssetSetIn"]
            ).optional(),
            "campaignAudienceView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn"]
            ).optional(),
            "conversionAction": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__ConversionActionIn"]
            ).optional(),
            "adGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupIn"]
            ).optional(),
            "adGroupAd": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAdIn"]
            ).optional(),
            "customerManagerLink": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn"]
            ).optional(),
            "keywordView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__KeywordViewIn"]
            ).optional(),
            "adGroupBidModifier": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn"]
            ).optional(),
            "dynamicSearchAdsSearchTermView": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewIn"
                ]
            ).optional(),
            "genderView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__GenderViewIn"]
            ).optional(),
            "campaignBudget": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignBudgetIn"]
            ).optional(),
            "adGroupAudienceView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn"]
            ).optional(),
            "label": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__LabelIn"]
            ).optional(),
            "asset": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AssetIn"]
            ).optional(),
            "adGroupCriterion": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchAds360RowIn"])
    types["GoogleAdsSearchads360V0Services__SearchAds360RowOut"] = t.struct(
        {
            "customerClient": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerClientOut"]
            ).optional(),
            "segments": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SegmentsOut"]
            ).optional(),
            "campaign": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignOut"]
            ).optional(),
            "metrics": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MetricsOut"]
            ).optional(),
            "biddingStrategy": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__BiddingStrategyOut"]
            ).optional(),
            "locationView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__LocationViewOut"]
            ).optional(),
            "customer": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerOut"]
            ).optional(),
            "campaignCriterion": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignCriterionOut"]
            ).optional(),
            "customColumns": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__ValueOut"])
            ).optional(),
            "ageRangeView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AgeRangeViewOut"]
            ).optional(),
            "adGroupLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupLabelOut"]
            ).optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__UserListOut"]
            ).optional(),
            "campaignLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignLabelOut"]
            ).optional(),
            "adGroupCriterionLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut"]
            ).optional(),
            "adGroupAdLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut"]
            ).optional(),
            "webpageView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__WebpageViewOut"]
            ).optional(),
            "productGroupView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__ProductGroupViewOut"]
            ).optional(),
            "assetSet": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AssetSetOut"]
            ).optional(),
            "campaignAudienceView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut"]
            ).optional(),
            "conversionAction": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__ConversionActionOut"]
            ).optional(),
            "adGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupOut"]
            ).optional(),
            "adGroupAd": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAdOut"]
            ).optional(),
            "customerManagerLink": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut"]
            ).optional(),
            "keywordView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__KeywordViewOut"]
            ).optional(),
            "adGroupBidModifier": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut"]
            ).optional(),
            "dynamicSearchAdsSearchTermView": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewOut"
                ]
            ).optional(),
            "genderView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__GenderViewOut"]
            ).optional(),
            "campaignBudget": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignBudgetOut"]
            ).optional(),
            "adGroupAudienceView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut"]
            ).optional(),
            "label": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__LabelOut"]
            ).optional(),
            "asset": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AssetOut"]
            ).optional(),
            "adGroupCriterion": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchAds360RowOut"])
    types["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingIn"])
    types["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut"])
    types["GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn"] = t.struct(
        {
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorLocationIn"]
            ).optional(),
            "message": t.string().optional(),
            "details": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorDetailsIn"]
            ).optional(),
            "trigger": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ValueIn"]
            ).optional(),
            "errorCode": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorCodeIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn"])
    types["GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut"] = t.struct(
        {
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorLocationOut"]
            ).optional(),
            "message": t.string().optional(),
            "details": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorDetailsOut"]
            ).optional(),
            "trigger": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ValueOut"]
            ).optional(),
            "errorCode": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorCodeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut"])
    types["GoogleAdsSearchads360V0Resources__GenderViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__GenderViewIn"])
    types["GoogleAdsSearchads360V0Resources__GenderViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__GenderViewOut"])
    types["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn"] = t.struct(
        {
            "targetPartnerSearchNetwork": t.boolean().optional(),
            "targetGoogleSearch": t.boolean().optional(),
            "targetContentNetwork": t.boolean().optional(),
            "targetSearchNetwork": t.boolean().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn"])
    types["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut"] = t.struct(
        {
            "targetPartnerSearchNetwork": t.boolean().optional(),
            "targetGoogleSearch": t.boolean().optional(),
            "targetContentNetwork": t.boolean().optional(),
            "targetSearchNetwork": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut"])
    types[
        "GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseIn"
    ] = t.struct({"resourceNames": t.array(t.string()).optional()}).named(
        renames["GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseIn"]
    )
    types[
        "GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseOut"
    ] = t.struct(
        {
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseOut"]
    )
    types["GoogleAdsSearchads360V0Common__SegmentsIn"] = t.struct(
        {
            "device": t.string().optional(),
            "dayOfWeek": t.string().optional(),
            "conversionActionName": t.string().optional(),
            "month": t.string().optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordIn"]
            ).optional(),
            "year": t.integer().optional(),
            "week": t.string().optional(),
            "adNetworkType": t.string().optional(),
            "quarter": t.string().optional(),
            "conversionAction": t.string().optional(),
            "conversionActionCategory": t.string().optional(),
            "date": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SegmentsIn"])
    types["GoogleAdsSearchads360V0Common__SegmentsOut"] = t.struct(
        {
            "device": t.string().optional(),
            "dayOfWeek": t.string().optional(),
            "conversionActionName": t.string().optional(),
            "month": t.string().optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordOut"]
            ).optional(),
            "year": t.integer().optional(),
            "week": t.string().optional(),
            "adNetworkType": t.string().optional(),
            "quarter": t.string().optional(),
            "conversionAction": t.string().optional(),
            "conversionActionCategory": t.string().optional(),
            "date": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SegmentsOut"])
    types["GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut"])
    types["GoogleAdsSearchads360V0Common__KeywordInfoIn"] = t.struct(
        {"text": t.string().optional(), "matchType": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__KeywordInfoIn"])
    types["GoogleAdsSearchads360V0Common__KeywordInfoOut"] = t.struct(
        {
            "text": t.string().optional(),
            "matchType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__KeywordInfoOut"])
    types["GoogleAdsSearchads360V0Common__ListingGroupInfoIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ListingGroupInfoIn"])
    types["GoogleAdsSearchads360V0Common__ListingGroupInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__ListingGroupInfoOut"])
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationIn"
    ] = t.struct({"conversionActions": t.array(t.string()).optional()}).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationOut"
    ] = t.struct(
        {
            "conversionActions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationOut"]
    )
    types["GoogleAdsSearchads360V0Resources__AdGroupCriterionIn"] = t.struct(
        {
            "adGroup": t.string().optional(),
            "resourceName": t.string().optional(),
            "ageRange": t.proxy(
                renames["GoogleAdsSearchads360V0Common__AgeRangeInfoIn"]
            ).optional(),
            "finalUrlSuffix": t.string().optional(),
            "bidModifier": t.number().optional(),
            "listingGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ListingGroupInfoIn"]
            ).optional(),
            "negative": t.boolean().optional(),
            "cpcBidMicros": t.string().optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoIn"]
            ).optional(),
            "webpage": t.proxy(
                renames["GoogleAdsSearchads360V0Common__WebpageInfoIn"]
            ).optional(),
            "status": t.string().optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Common__UserListInfoIn"]
            ).optional(),
            "gender": t.proxy(
                renames["GoogleAdsSearchads360V0Common__GenderInfoIn"]
            ).optional(),
            "trackingUrlTemplate": t.string().optional(),
            "finalUrls": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupCriterionOut"] = t.struct(
        {
            "adGroup": t.string().optional(),
            "resourceName": t.string().optional(),
            "creationTime": t.string().optional(),
            "ageRange": t.proxy(
                renames["GoogleAdsSearchads360V0Common__AgeRangeInfoOut"]
            ).optional(),
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationInfoOut"]
            ).optional(),
            "engineId": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "effectiveCpcBidMicros": t.string().optional(),
            "finalUrlSuffix": t.string().optional(),
            "bidModifier": t.number().optional(),
            "listingGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ListingGroupInfoOut"]
            ).optional(),
            "negative": t.boolean().optional(),
            "cpcBidMicros": t.string().optional(),
            "qualityInfo": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoOut"
                ]
            ).optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoOut"]
            ).optional(),
            "type": t.string().optional(),
            "criterionId": t.string().optional(),
            "webpage": t.proxy(
                renames["GoogleAdsSearchads360V0Common__WebpageInfoOut"]
            ).optional(),
            "status": t.string().optional(),
            "engineStatus": t.string().optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Common__UserListInfoOut"]
            ).optional(),
            "gender": t.proxy(
                renames["GoogleAdsSearchads360V0Common__GenderInfoOut"]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "trackingUrlTemplate": t.string().optional(),
            "finalUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn"] = t.struct(
        {
            "bidModifier": t.number().optional(),
            "resourceName": t.string().optional(),
            "device": t.proxy(
                renames["GoogleAdsSearchads360V0Common__DeviceInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut"] = t.struct(
        {
            "bidModifier": t.number().optional(),
            "resourceName": t.string().optional(),
            "device": t.proxy(
                renames["GoogleAdsSearchads360V0Common__DeviceInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut"])
    types["GoogleAdsSearchads360V0Common__EnhancedCpcIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__EnhancedCpcIn"])
    types["GoogleAdsSearchads360V0Common__EnhancedCpcOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__EnhancedCpcOut"])
    types["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Services__SearchAds360RowIn"])
            ).optional(),
            "customColumnHeaders": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Services__CustomColumnHeaderIn"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalResultsCount": t.string().optional(),
            "fieldMask": t.string().optional(),
            "summaryRow": t.proxy(
                renames["GoogleAdsSearchads360V0Services__SearchAds360RowIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseIn"])
    types["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Services__SearchAds360RowOut"])
            ).optional(),
            "customColumnHeaders": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Services__CustomColumnHeaderOut"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalResultsCount": t.string().optional(),
            "fieldMask": t.string().optional(),
            "summaryRow": t.proxy(
                renames["GoogleAdsSearchads360V0Services__SearchAds360RowOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut"])
    types["GoogleAdsSearchads360V0Common__AgeRangeInfoIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__AgeRangeInfoIn"])
    types["GoogleAdsSearchads360V0Common__AgeRangeInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__AgeRangeInfoOut"])
    types["GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoIn"])
    types[
        "GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoOut"
    ] = t.struct(
        {
            "qualityScore": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoOut"]
    )
    types["GoogleAdsSearchads360V0Common__FrequencyCapEntryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__FrequencyCapEntryIn"])
    types["GoogleAdsSearchads360V0Common__FrequencyCapEntryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__FrequencyCapEntryOut"])
    types["GoogleAdsSearchads360V0Resources__CampaignIn"] = t.struct(
        {
            "geoTargetTypeSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingIn"
                ]
            ).optional(),
            "adServingOptimizationStatus": t.string().optional(),
            "campaignBudget": t.string().optional(),
            "excludedParentAssetFieldTypes": t.array(t.string()).optional(),
            "selectiveOptimization": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationIn"
                ]
            ).optional(),
            "name": t.string().optional(),
            "targetRoas": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetRoasIn"]
            ).optional(),
            "targetCpm": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpmIn"]
            ).optional(),
            "trackingUrlTemplate": t.string().optional(),
            "dynamicSearchAdsSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn"
                ]
            ).optional(),
            "frequencyCaps": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__FrequencyCapEntryIn"])
            ).optional(),
            "targetCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpaIn"]
            ).optional(),
            "resourceName": t.string().optional(),
            "biddingStrategy": t.string().optional(),
            "maximizeConversions": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionsIn"]
            ).optional(),
            "realTimeBiddingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn"]
            ).optional(),
            "targetImpressionShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetImpressionShareIn"]
            ).optional(),
            "startDate": t.string().optional(),
            "urlCustomParameters": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__CustomParameterIn"])
            ).optional(),
            "finalUrlSuffix": t.string().optional(),
            "urlExpansionOptOut": t.boolean().optional(),
            "advertisingChannelSubType": t.string().optional(),
            "percentCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__PercentCpcIn"]
            ).optional(),
            "optimizationGoalSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingIn"
                ]
            ).optional(),
            "maximizeConversionValue": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueIn"]
            ).optional(),
            "targetSpend": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetSpendIn"]
            ).optional(),
            "status": t.string().optional(),
            "advertisingChannelType": t.string().optional(),
            "manualCpm": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpmIn"]
            ).optional(),
            "manualCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpcIn"]
            ).optional(),
            "endDate": t.string().optional(),
            "manualCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpaIn"]
            ).optional(),
            "shoppingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn"]
            ).optional(),
            "networkSettings": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignOut"] = t.struct(
        {
            "geoTargetTypeSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingOut"
                ]
            ).optional(),
            "adServingOptimizationStatus": t.string().optional(),
            "campaignBudget": t.string().optional(),
            "excludedParentAssetFieldTypes": t.array(t.string()).optional(),
            "selectiveOptimization": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationOut"
                ]
            ).optional(),
            "name": t.string().optional(),
            "targetRoas": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetRoasOut"]
            ).optional(),
            "targetCpm": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpmOut"]
            ).optional(),
            "trackingUrlTemplate": t.string().optional(),
            "dynamicSearchAdsSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut"
                ]
            ).optional(),
            "frequencyCaps": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__FrequencyCapEntryOut"])
            ).optional(),
            "targetCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpaOut"]
            ).optional(),
            "resourceName": t.string().optional(),
            "biddingStrategy": t.string().optional(),
            "creationTime": t.string().optional(),
            "maximizeConversions": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionsOut"]
            ).optional(),
            "engineId": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "realTimeBiddingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut"]
            ).optional(),
            "targetImpressionShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetImpressionShareOut"]
            ).optional(),
            "startDate": t.string().optional(),
            "urlCustomParameters": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__CustomParameterOut"])
            ).optional(),
            "biddingStrategyType": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "finalUrlSuffix": t.string().optional(),
            "urlExpansionOptOut": t.boolean().optional(),
            "advertisingChannelSubType": t.string().optional(),
            "percentCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__PercentCpcOut"]
            ).optional(),
            "optimizationGoalSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingOut"
                ]
            ).optional(),
            "maximizeConversionValue": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueOut"]
            ).optional(),
            "servingStatus": t.string().optional(),
            "targetSpend": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetSpendOut"]
            ).optional(),
            "status": t.string().optional(),
            "advertisingChannelType": t.string().optional(),
            "trackingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut"]
            ).optional(),
            "manualCpm": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpmOut"]
            ).optional(),
            "manualCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpcOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "biddingStrategySystemStatus": t.string().optional(),
            "endDate": t.string().optional(),
            "manualCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpaOut"]
            ).optional(),
            "shoppingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut"]
            ).optional(),
            "networkSettings": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut"]
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignOut"])
    types["GoogleAdsSearchads360V0Resources__KeywordViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__KeywordViewIn"])
    types["GoogleAdsSearchads360V0Resources__KeywordViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__KeywordViewOut"])
    types["GoogleAdsSearchads360V0Common__TargetSpendIn"] = t.struct(
        {
            "targetSpendMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetSpendIn"])
    types["GoogleAdsSearchads360V0Common__TargetSpendOut"] = t.struct(
        {
            "targetSpendMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetSpendOut"])
    types["GoogleAdsSearchads360V0Resources__CampaignCriterionIn"] = t.struct(
        {
            "language": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LanguageInfoIn"]
            ).optional(),
            "negative": t.boolean().optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoIn"]
            ).optional(),
            "gender": t.proxy(
                renames["GoogleAdsSearchads360V0Common__GenderInfoIn"]
            ).optional(),
            "ageRange": t.proxy(
                renames["GoogleAdsSearchads360V0Common__AgeRangeInfoIn"]
            ).optional(),
            "locationGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationGroupInfoIn"]
            ).optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Common__UserListInfoIn"]
            ).optional(),
            "resourceName": t.string().optional(),
            "webpage": t.proxy(
                renames["GoogleAdsSearchads360V0Common__WebpageInfoIn"]
            ).optional(),
            "bidModifier": t.number().optional(),
            "status": t.string().optional(),
            "device": t.proxy(
                renames["GoogleAdsSearchads360V0Common__DeviceInfoIn"]
            ).optional(),
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignCriterionIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignCriterionOut"] = t.struct(
        {
            "language": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LanguageInfoOut"]
            ).optional(),
            "negative": t.boolean().optional(),
            "criterionId": t.string().optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoOut"]
            ).optional(),
            "gender": t.proxy(
                renames["GoogleAdsSearchads360V0Common__GenderInfoOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "ageRange": t.proxy(
                renames["GoogleAdsSearchads360V0Common__AgeRangeInfoOut"]
            ).optional(),
            "locationGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationGroupInfoOut"]
            ).optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Common__UserListInfoOut"]
            ).optional(),
            "resourceName": t.string().optional(),
            "webpage": t.proxy(
                renames["GoogleAdsSearchads360V0Common__WebpageInfoOut"]
            ).optional(),
            "bidModifier": t.number().optional(),
            "status": t.string().optional(),
            "device": t.proxy(
                renames["GoogleAdsSearchads360V0Common__DeviceInfoOut"]
            ).optional(),
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationInfoOut"]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignCriterionOut"])
    types["GoogleAdsSearchads360V0Common__TextLabelIn"] = t.struct(
        {"backgroundColor": t.string().optional(), "description": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TextLabelIn"])
    types["GoogleAdsSearchads360V0Common__TextLabelOut"] = t.struct(
        {
            "backgroundColor": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TextLabelOut"])
    types["GoogleAdsSearchads360V0Resources__AdIn"] = t.struct(
        {
            "productAd": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn"]
            ).optional(),
            "expandedDynamicSearchAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn"
                ]
            ).optional(),
            "name": t.string().optional(),
            "responsiveSearchAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoIn"
                ]
            ).optional(),
            "expandedTextAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn"
                ]
            ).optional(),
            "displayUrl": t.string().optional(),
            "resourceName": t.string().optional(),
            "finalUrls": t.array(t.string()).optional(),
            "textAd": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdIn"])
    types["GoogleAdsSearchads360V0Resources__AdOut"] = t.struct(
        {
            "productAd": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut"]
            ).optional(),
            "expandedDynamicSearchAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut"
                ]
            ).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "responsiveSearchAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoOut"
                ]
            ).optional(),
            "type": t.string().optional(),
            "expandedTextAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut"
                ]
            ).optional(),
            "displayUrl": t.string().optional(),
            "resourceName": t.string().optional(),
            "finalUrls": t.array(t.string()).optional(),
            "textAd": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdOut"])
    types[
        "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsIn"
    ] = t.struct({"attributionModel": t.string().optional()}).named(
        renames[
            "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsIn"
        ]
    )
    types[
        "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut"
    ] = t.struct(
        {
            "dataDrivenModelStatus": t.string().optional(),
            "attributionModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut"
        ]
    )
    types["GoogleAdsSearchads360V0Common__LanguageInfoIn"] = t.struct(
        {"languageConstant": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__LanguageInfoIn"])
    types["GoogleAdsSearchads360V0Common__LanguageInfoOut"] = t.struct(
        {
            "languageConstant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__LanguageInfoOut"])
    types["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn"] = t.struct(
        {
            "rateScope": t.string().optional(),
            "retryDelay": t.string().optional(),
            "rateName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn"])
    types["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut"] = t.struct(
        {
            "rateScope": t.string().optional(),
            "retryDelay": t.string().optional(),
            "rateName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut"])
    types["GoogleAdsSearchads360V0Common__TargetRestrictionIn"] = t.struct(
        {"bidOnly": t.boolean().optional(), "targetingDimension": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TargetRestrictionIn"])
    types["GoogleAdsSearchads360V0Common__TargetRestrictionOut"] = t.struct(
        {
            "bidOnly": t.boolean().optional(),
            "targetingDimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetRestrictionOut"])
    types["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn"] = t.struct(
        {
            "enableLocal": t.boolean().optional(),
            "campaignPriority": t.integer().optional(),
            "feedLabel": t.string().optional(),
            "merchantId": t.string().optional(),
            "useVehicleInventory": t.boolean().optional(),
            "salesCountry": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn"])
    types["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut"] = t.struct(
        {
            "enableLocal": t.boolean().optional(),
            "campaignPriority": t.integer().optional(),
            "feedLabel": t.string().optional(),
            "merchantId": t.string().optional(),
            "useVehicleInventory": t.boolean().optional(),
            "salesCountry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut"])
    types["GoogleAdsSearchads360V0Resources__ConversionTrackingSettingIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__ConversionTrackingSettingIn"])
    types["GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut"] = t.struct(
        {
            "googleAdsConversionCustomer": t.string().optional(),
            "crossAccountConversionTrackingId": t.string().optional(),
            "enhancedConversionsForLeadsEnabled": t.boolean().optional(),
            "conversionTrackingStatus": t.string().optional(),
            "conversionTrackingId": t.string().optional(),
            "googleAdsCrossAccountConversionTrackingId": t.string().optional(),
            "acceptedCustomerDataTerms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut"])
    types["GoogleAdsSearchads360V0Common__ValueIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "floatValue": t.number().optional(),
            "int64Value": t.string().optional(),
            "doubleValue": t.number().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__ValueIn"])
    types["GoogleAdsSearchads360V0Common__ValueOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "floatValue": t.number().optional(),
            "int64Value": t.string().optional(),
            "doubleValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__ValueOut"])
    types["GoogleAdsSearchads360V0Resources__CustomColumnIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomColumnIn"])
    types["GoogleAdsSearchads360V0Resources__CustomColumnOut"] = t.struct(
        {
            "referencesAttributes": t.boolean().optional(),
            "referencesMetrics": t.boolean().optional(),
            "referencedSystemColumns": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "queryable": t.boolean().optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomColumnOut"])
    types[
        "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewOut"
    ] = t.struct(
        {
            "resourceName": t.string().optional(),
            "landingPage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewOut"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingIn"
    ] = t.struct(
        {
            "positiveGeoTargetType": t.string().optional(),
            "negativeGeoTargetType": t.string().optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingOut"
    ] = t.struct(
        {
            "positiveGeoTargetType": t.string().optional(),
            "negativeGeoTargetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingOut"]
    )
    types["GoogleAdsSearchads360V0Errors__ErrorCodeIn"] = t.struct(
        {
            "distinctError": t.string().optional(),
            "quotaError": t.string().optional(),
            "authorizationError": t.string().optional(),
            "sizeLimitError": t.string().optional(),
            "internalError": t.string().optional(),
            "dateError": t.string().optional(),
            "queryError": t.string().optional(),
            "authenticationError": t.string().optional(),
            "dateRangeError": t.string().optional(),
            "requestError": t.string().optional(),
            "customColumnError": t.string().optional(),
            "headerError": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__ErrorCodeIn"])
    types["GoogleAdsSearchads360V0Errors__ErrorCodeOut"] = t.struct(
        {
            "distinctError": t.string().optional(),
            "quotaError": t.string().optional(),
            "authorizationError": t.string().optional(),
            "sizeLimitError": t.string().optional(),
            "internalError": t.string().optional(),
            "dateError": t.string().optional(),
            "queryError": t.string().optional(),
            "authenticationError": t.string().optional(),
            "dateRangeError": t.string().optional(),
            "requestError": t.string().optional(),
            "customColumnError": t.string().optional(),
            "headerError": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__ErrorCodeOut"])
    types[
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn"
    ] = t.struct(
        {
            "description1": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "description2": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn"
        ]
    )
    types[
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut"
    ] = t.struct(
        {
            "description1": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "description2": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut"
        ]
    )
    types["GoogleAdsSearchads360V0Errors__SearchAds360FailureIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn"])
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__SearchAds360FailureIn"])
    types["GoogleAdsSearchads360V0Errors__SearchAds360FailureOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__SearchAds360FailureOut"])
    types["GoogleAdsSearchads360V0Errors__ErrorLocationIn"] = t.struct(
        {
            "fieldPathElements": t.array(
                t.proxy(
                    renames[
                        "GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__ErrorLocationIn"])
    types["GoogleAdsSearchads360V0Errors__ErrorLocationOut"] = t.struct(
        {
            "fieldPathElements": t.array(
                t.proxy(
                    renames[
                        "GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__ErrorLocationOut"])
    types["GoogleAdsSearchads360V0Services__CustomColumnHeaderIn"] = t.struct(
        {
            "id": t.string().optional(),
            "referencesMetrics": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__CustomColumnHeaderIn"])
    types["GoogleAdsSearchads360V0Services__CustomColumnHeaderOut"] = t.struct(
        {
            "id": t.string().optional(),
            "referencesMetrics": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__CustomColumnHeaderOut"])
    types["GoogleAdsSearchads360V0Common__LocationInfoIn"] = t.struct(
        {"geoTargetConstant": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__LocationInfoIn"])
    types["GoogleAdsSearchads360V0Common__LocationInfoOut"] = t.struct(
        {
            "geoTargetConstant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__LocationInfoOut"])
    types["GoogleAdsSearchads360V0Resources__UserListIn"] = t.struct(
        {"name": t.string().optional(), "resourceName": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__UserListIn"])
    types["GoogleAdsSearchads360V0Resources__UserListOut"] = t.struct(
        {
            "name": t.string().optional(),
            "resourceName": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__UserListOut"])
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingIn"
    ] = t.struct({"optimizationGoalTypes": t.array(t.string()).optional()}).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingOut"
    ] = t.struct(
        {
            "optimizationGoalTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingOut"]
    )
    types["GoogleAdsSearchads360V0Common__KeywordIn"] = t.struct(
        {
            "info": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoIn"]
            ).optional(),
            "adGroupCriterion": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__KeywordIn"])
    types["GoogleAdsSearchads360V0Common__KeywordOut"] = t.struct(
        {
            "info": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoOut"]
            ).optional(),
            "adGroupCriterion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__KeywordOut"])
    types[
        "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsIn"
        ]
    )
    types[
        "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut"
    ] = t.struct(
        {
            "activityGroupTag": t.string().optional(),
            "activityId": t.string().optional(),
            "activityTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut"
        ]
    )
    types["GoogleAdsSearchads360V0Resources__WebpageViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__WebpageViewIn"])
    types["GoogleAdsSearchads360V0Resources__WebpageViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__WebpageViewOut"])
    types["GoogleAdsSearchads360V0Common__LocationGroupInfoIn"] = t.struct(
        {
            "radiusUnits": t.string().optional(),
            "radius": t.string().optional(),
            "feedItemSets": t.array(t.string()).optional(),
            "geoTargetConstants": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__LocationGroupInfoIn"])
    types["GoogleAdsSearchads360V0Common__LocationGroupInfoOut"] = t.struct(
        {
            "radiusUnits": t.string().optional(),
            "radius": t.string().optional(),
            "feedItemSets": t.array(t.string()).optional(),
            "geoTargetConstants": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__LocationGroupInfoOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn"] = t.struct(
        {
            "label": t.string().optional(),
            "resourceName": t.string().optional(),
            "adGroupAd": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "resourceName": t.string().optional(),
            "adGroupAd": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut"])
    types["GoogleAdsSearchads360V0Common__TargetCpaIn"] = t.struct(
        {
            "cpcBidFloorMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "targetCpaMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetCpaIn"])
    types["GoogleAdsSearchads360V0Common__TargetCpaOut"] = t.struct(
        {
            "cpcBidFloorMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "targetCpaMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetCpaOut"])
    types["GoogleAdsSearchads360V0Common__TargetingSettingIn"] = t.struct(
        {
            "targetRestrictions": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__TargetRestrictionIn"])
            ).optional()
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetingSettingIn"])
    types["GoogleAdsSearchads360V0Common__TargetingSettingOut"] = t.struct(
        {
            "targetRestrictions": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__TargetRestrictionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetingSettingOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAdIn"] = t.struct(
        {
            "ad": t.proxy(renames["GoogleAdsSearchads360V0Resources__AdIn"]).optional(),
            "resourceName": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAdIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAdOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "creationTime": t.string().optional(),
            "engineStatus": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "ad": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdOut"]
            ).optional(),
            "engineId": t.string().optional(),
            "resourceName": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAdOut"])
    types["GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn"] = t.struct(
        {"status": t.string().optional(), "resourceName": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn"])
    types["GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut"] = t.struct(
        {
            "managerCustomer": t.string().optional(),
            "status": t.string().optional(),
            "managerLinkId": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut"])
    types["GoogleAdsSearchads360V0Common__MaximizeConversionValueIn"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "targetRoas": t.number().optional(),
            "cpcBidFloorMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueIn"])
    types["GoogleAdsSearchads360V0Common__MaximizeConversionValueOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "targetRoas": t.number().optional(),
            "cpcBidFloorMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueOut"])
    types["GoogleAdsSearchads360V0Common__TargetCpmIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TargetCpmIn"])
    types["GoogleAdsSearchads360V0Common__TargetCpmOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TargetCpmOut"])
    types["GoogleAdsSearchads360V0Services__SearchSearchAds360RequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "query": t.string(),
            "summaryRowSetting": t.string().optional(),
            "returnTotalResultsCount": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchSearchAds360RequestIn"])
    types["GoogleAdsSearchads360V0Services__SearchSearchAds360RequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "query": t.string(),
            "summaryRowSetting": t.string().optional(),
            "returnTotalResultsCount": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchSearchAds360RequestOut"])
    types["GoogleAdsSearchads360V0Resources__AgeRangeViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__AgeRangeViewIn"])
    types["GoogleAdsSearchads360V0Resources__AgeRangeViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AgeRangeViewOut"])
    types["GoogleAdsSearchads360V0Common__ManualCpaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpaIn"])
    types["GoogleAdsSearchads360V0Common__ManualCpaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpaOut"])
    types["GoogleAdsSearchads360V0Common__UserListInfoIn"] = t.struct(
        {"userList": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__UserListInfoIn"])
    types["GoogleAdsSearchads360V0Common__UserListInfoOut"] = t.struct(
        {
            "userList": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__UserListInfoOut"])
    types["GoogleAdsSearchads360V0Common__TargetOutrankShareIn"] = t.struct(
        {"cpcBidCeilingMicros": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TargetOutrankShareIn"])
    types["GoogleAdsSearchads360V0Common__TargetOutrankShareOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetOutrankShareOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "adGroupCriterion": t.string().optional(),
            "label": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "adGroupCriterion": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut"])
    types[
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalResultsCount": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldIn"]
                )
            ).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseIn"]
    )
    types[
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalResultsCount": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseOut"]
    )
    types["GoogleAdsSearchads360V0Resources__ProductGroupViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__ProductGroupViewIn"])
    types["GoogleAdsSearchads360V0Resources__ProductGroupViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__ProductGroupViewOut"])
    types["GoogleAdsSearchads360V0Common__ManualCpcIn"] = t.struct(
        {"enhancedCpcEnabled": t.boolean().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpcIn"])
    types["GoogleAdsSearchads360V0Common__ManualCpcOut"] = t.struct(
        {
            "enhancedCpcEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpcOut"])
    types["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn"] = t.struct(
        {"optIn": t.boolean().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn"])
    types["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut"] = t.struct(
        {
            "optIn": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut"])
    types["GoogleAdsSearchads360V0Common__WebpageInfoIn"] = t.struct(
        {
            "conditions": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Common__WebpageConditionInfoIn"]
                )
            ).optional(),
            "criterionName": t.string().optional(),
            "coveragePercentage": t.number().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__WebpageInfoIn"])
    types["GoogleAdsSearchads360V0Common__WebpageInfoOut"] = t.struct(
        {
            "conditions": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Common__WebpageConditionInfoOut"]
                )
            ).optional(),
            "criterionName": t.string().optional(),
            "coveragePercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__WebpageInfoOut"])

    functions = {}
    functions["customersListAccessibleCustomers"] = searchads360.get(
        "v0/customers:listAccessibleCustomers",
        t.struct({"auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersSearchAds360Search"] = searchads360.post(
        "v0/customers/{customerId}/searchAds360:search",
        t.struct(
            {
                "customerId": t.string(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "summaryRowSetting": t.string().optional(),
                "returnTotalResultsCount": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersCustomColumnsGet"] = searchads360.get(
        "v0/customers/{customerId}/customColumns",
        t.struct({"customerId": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames["GoogleAdsSearchads360V0Services__ListCustomColumnsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersCustomColumnsList"] = searchads360.get(
        "v0/customers/{customerId}/customColumns",
        t.struct({"customerId": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames["GoogleAdsSearchads360V0Services__ListCustomColumnsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["searchAds360FieldsSearch"] = searchads360.get(
        "v0/{resourceName}",
        t.struct({"resourceName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["searchAds360FieldsGet"] = searchads360.get(
        "v0/{resourceName}",
        t.struct({"resourceName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="searchads360",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
