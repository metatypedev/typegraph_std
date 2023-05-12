from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_searchads360() -> Import:
    searchads360 = HTTPRuntime("https://searchads360.googleapis.com/")

    renames = {
        "ErrorResponse": "_searchads360_1_ErrorResponse",
        "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoIn": "_searchads360_2_GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoOut": "_searchads360_3_GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoOut",
        "GoogleAdsSearchads360V0Common__ManualCpaIn": "_searchads360_4_GoogleAdsSearchads360V0Common__ManualCpaIn",
        "GoogleAdsSearchads360V0Common__ManualCpaOut": "_searchads360_5_GoogleAdsSearchads360V0Common__ManualCpaOut",
        "GoogleAdsSearchads360V0Common__TextLabelIn": "_searchads360_6_GoogleAdsSearchads360V0Common__TextLabelIn",
        "GoogleAdsSearchads360V0Common__TextLabelOut": "_searchads360_7_GoogleAdsSearchads360V0Common__TextLabelOut",
        "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsIn": "_searchads360_8_GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsIn",
        "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut": "_searchads360_9_GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut",
        "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsIn": "_searchads360_10_GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsIn",
        "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut": "_searchads360_11_GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut",
        "GoogleAdsSearchads360V0Common__KeywordIn": "_searchads360_12_GoogleAdsSearchads360V0Common__KeywordIn",
        "GoogleAdsSearchads360V0Common__KeywordOut": "_searchads360_13_GoogleAdsSearchads360V0Common__KeywordOut",
        "GoogleAdsSearchads360V0Resources__CampaignBudgetIn": "_searchads360_14_GoogleAdsSearchads360V0Resources__CampaignBudgetIn",
        "GoogleAdsSearchads360V0Resources__CampaignBudgetOut": "_searchads360_15_GoogleAdsSearchads360V0Resources__CampaignBudgetOut",
        "GoogleAdsSearchads360V0Resources__CampaignCriterionIn": "_searchads360_16_GoogleAdsSearchads360V0Resources__CampaignCriterionIn",
        "GoogleAdsSearchads360V0Resources__CampaignCriterionOut": "_searchads360_17_GoogleAdsSearchads360V0Resources__CampaignCriterionOut",
        "GoogleAdsSearchads360V0Common__FrequencyCapEntryIn": "_searchads360_18_GoogleAdsSearchads360V0Common__FrequencyCapEntryIn",
        "GoogleAdsSearchads360V0Common__FrequencyCapEntryOut": "_searchads360_19_GoogleAdsSearchads360V0Common__FrequencyCapEntryOut",
        "GoogleAdsSearchads360V0Common__WebpageConditionInfoIn": "_searchads360_20_GoogleAdsSearchads360V0Common__WebpageConditionInfoIn",
        "GoogleAdsSearchads360V0Common__WebpageConditionInfoOut": "_searchads360_21_GoogleAdsSearchads360V0Common__WebpageConditionInfoOut",
        "GoogleAdsSearchads360V0Resources__CampaignIn": "_searchads360_22_GoogleAdsSearchads360V0Resources__CampaignIn",
        "GoogleAdsSearchads360V0Resources__CampaignOut": "_searchads360_23_GoogleAdsSearchads360V0Resources__CampaignOut",
        "GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoIn": "_searchads360_24_GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoIn",
        "GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoOut": "_searchads360_25_GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoOut",
        "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingIn": "_searchads360_26_GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingOut": "_searchads360_27_GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingOut",
        "GoogleAdsSearchads360V0Resources__CampaignLabelIn": "_searchads360_28_GoogleAdsSearchads360V0Resources__CampaignLabelIn",
        "GoogleAdsSearchads360V0Resources__CampaignLabelOut": "_searchads360_29_GoogleAdsSearchads360V0Resources__CampaignLabelOut",
        "GoogleAdsSearchads360V0Common__DeviceInfoIn": "_searchads360_30_GoogleAdsSearchads360V0Common__DeviceInfoIn",
        "GoogleAdsSearchads360V0Common__DeviceInfoOut": "_searchads360_31_GoogleAdsSearchads360V0Common__DeviceInfoOut",
        "GoogleAdsSearchads360V0Services__CustomColumnHeaderIn": "_searchads360_32_GoogleAdsSearchads360V0Services__CustomColumnHeaderIn",
        "GoogleAdsSearchads360V0Services__CustomColumnHeaderOut": "_searchads360_33_GoogleAdsSearchads360V0Services__CustomColumnHeaderOut",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360RequestIn": "_searchads360_34_GoogleAdsSearchads360V0Services__SearchSearchAds360RequestIn",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360RequestOut": "_searchads360_35_GoogleAdsSearchads360V0Services__SearchSearchAds360RequestOut",
        "GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingIn": "_searchads360_36_GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut": "_searchads360_37_GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut",
        "GoogleAdsSearchads360V0Common__ListingGroupInfoIn": "_searchads360_38_GoogleAdsSearchads360V0Common__ListingGroupInfoIn",
        "GoogleAdsSearchads360V0Common__ListingGroupInfoOut": "_searchads360_39_GoogleAdsSearchads360V0Common__ListingGroupInfoOut",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseIn": "_searchads360_40_GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseIn",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseOut": "_searchads360_41_GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseOut",
        "GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn": "_searchads360_42_GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn",
        "GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut": "_searchads360_43_GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut",
        "GoogleAdsSearchads360V0Common__TargetSpendIn": "_searchads360_44_GoogleAdsSearchads360V0Common__TargetSpendIn",
        "GoogleAdsSearchads360V0Common__TargetSpendOut": "_searchads360_45_GoogleAdsSearchads360V0Common__TargetSpendOut",
        "GoogleAdsSearchads360V0Common__LanguageInfoIn": "_searchads360_46_GoogleAdsSearchads360V0Common__LanguageInfoIn",
        "GoogleAdsSearchads360V0Common__LanguageInfoOut": "_searchads360_47_GoogleAdsSearchads360V0Common__LanguageInfoOut",
        "GoogleAdsSearchads360V0Services__ListCustomColumnsResponseIn": "_searchads360_48_GoogleAdsSearchads360V0Services__ListCustomColumnsResponseIn",
        "GoogleAdsSearchads360V0Services__ListCustomColumnsResponseOut": "_searchads360_49_GoogleAdsSearchads360V0Services__ListCustomColumnsResponseOut",
        "GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn": "_searchads360_50_GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn",
        "GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut": "_searchads360_51_GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut",
        "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewIn": "_searchads360_52_GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewIn",
        "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewOut": "_searchads360_53_GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewOut",
        "GoogleAdsSearchads360V0Resources__BiddingStrategyIn": "_searchads360_54_GoogleAdsSearchads360V0Resources__BiddingStrategyIn",
        "GoogleAdsSearchads360V0Resources__BiddingStrategyOut": "_searchads360_55_GoogleAdsSearchads360V0Resources__BiddingStrategyOut",
        "GoogleAdsSearchads360V0Common__CustomParameterIn": "_searchads360_56_GoogleAdsSearchads360V0Common__CustomParameterIn",
        "GoogleAdsSearchads360V0Common__CustomParameterOut": "_searchads360_57_GoogleAdsSearchads360V0Common__CustomParameterOut",
        "GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn": "_searchads360_58_GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn",
        "GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut": "_searchads360_59_GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut",
        "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationIn": "_searchads360_60_GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationIn",
        "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationOut": "_searchads360_61_GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationOut",
        "GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementIn": "_searchads360_62_GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementIn",
        "GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementOut": "_searchads360_63_GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElementOut",
        "GoogleAdsSearchads360V0Errors__ErrorDetailsIn": "_searchads360_64_GoogleAdsSearchads360V0Errors__ErrorDetailsIn",
        "GoogleAdsSearchads360V0Errors__ErrorDetailsOut": "_searchads360_65_GoogleAdsSearchads360V0Errors__ErrorDetailsOut",
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn": "_searchads360_66_GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut": "_searchads360_67_GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut",
        "GoogleAdsSearchads360V0Resources__ConversionTrackingSettingIn": "_searchads360_68_GoogleAdsSearchads360V0Resources__ConversionTrackingSettingIn",
        "GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut": "_searchads360_69_GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestIn": "_searchads360_70_GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestIn",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestOut": "_searchads360_71_GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestOut",
        "GoogleAdsSearchads360V0Resources__AdGroupCriterionIn": "_searchads360_72_GoogleAdsSearchads360V0Resources__AdGroupCriterionIn",
        "GoogleAdsSearchads360V0Resources__AdGroupCriterionOut": "_searchads360_73_GoogleAdsSearchads360V0Resources__AdGroupCriterionOut",
        "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn": "_searchads360_74_GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn",
        "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut": "_searchads360_75_GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut",
        "GoogleAdsSearchads360V0Resources__AdGroupIn": "_searchads360_76_GoogleAdsSearchads360V0Resources__AdGroupIn",
        "GoogleAdsSearchads360V0Resources__AdGroupOut": "_searchads360_77_GoogleAdsSearchads360V0Resources__AdGroupOut",
        "GoogleAdsSearchads360V0Resources__CustomerClientIn": "_searchads360_78_GoogleAdsSearchads360V0Resources__CustomerClientIn",
        "GoogleAdsSearchads360V0Resources__CustomerClientOut": "_searchads360_79_GoogleAdsSearchads360V0Resources__CustomerClientOut",
        "GoogleAdsSearchads360V0Common__TargetRoasIn": "_searchads360_80_GoogleAdsSearchads360V0Common__TargetRoasIn",
        "GoogleAdsSearchads360V0Common__TargetRoasOut": "_searchads360_81_GoogleAdsSearchads360V0Common__TargetRoasOut",
        "GoogleAdsSearchads360V0Common__WebpageInfoIn": "_searchads360_82_GoogleAdsSearchads360V0Common__WebpageInfoIn",
        "GoogleAdsSearchads360V0Common__WebpageInfoOut": "_searchads360_83_GoogleAdsSearchads360V0Common__WebpageInfoOut",
        "GoogleAdsSearchads360V0Resources__CustomerIn": "_searchads360_84_GoogleAdsSearchads360V0Resources__CustomerIn",
        "GoogleAdsSearchads360V0Resources__CustomerOut": "_searchads360_85_GoogleAdsSearchads360V0Resources__CustomerOut",
        "GoogleAdsSearchads360V0Common__UserListInfoIn": "_searchads360_86_GoogleAdsSearchads360V0Common__UserListInfoIn",
        "GoogleAdsSearchads360V0Common__UserListInfoOut": "_searchads360_87_GoogleAdsSearchads360V0Common__UserListInfoOut",
        "GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn": "_searchads360_88_GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn",
        "GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut": "_searchads360_89_GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut",
        "GoogleAdsSearchads360V0Resources__AgeRangeViewIn": "_searchads360_90_GoogleAdsSearchads360V0Resources__AgeRangeViewIn",
        "GoogleAdsSearchads360V0Resources__AgeRangeViewOut": "_searchads360_91_GoogleAdsSearchads360V0Resources__AgeRangeViewOut",
        "GoogleAdsSearchads360V0Common__ValueIn": "_searchads360_92_GoogleAdsSearchads360V0Common__ValueIn",
        "GoogleAdsSearchads360V0Common__ValueOut": "_searchads360_93_GoogleAdsSearchads360V0Common__ValueOut",
        "GoogleAdsSearchads360V0Resources__AdIn": "_searchads360_94_GoogleAdsSearchads360V0Resources__AdIn",
        "GoogleAdsSearchads360V0Resources__AdOut": "_searchads360_95_GoogleAdsSearchads360V0Resources__AdOut",
        "GoogleAdsSearchads360V0Common__TargetCpmIn": "_searchads360_96_GoogleAdsSearchads360V0Common__TargetCpmIn",
        "GoogleAdsSearchads360V0Common__TargetCpmOut": "_searchads360_97_GoogleAdsSearchads360V0Common__TargetCpmOut",
        "GoogleAdsSearchads360V0Common__LocationInfoIn": "_searchads360_98_GoogleAdsSearchads360V0Common__LocationInfoIn",
        "GoogleAdsSearchads360V0Common__LocationInfoOut": "_searchads360_99_GoogleAdsSearchads360V0Common__LocationInfoOut",
        "GoogleAdsSearchads360V0Resources__AdGroupLabelIn": "_searchads360_100_GoogleAdsSearchads360V0Resources__AdGroupLabelIn",
        "GoogleAdsSearchads360V0Resources__AdGroupLabelOut": "_searchads360_101_GoogleAdsSearchads360V0Resources__AdGroupLabelOut",
        "GoogleAdsSearchads360V0Resources__LocationViewIn": "_searchads360_102_GoogleAdsSearchads360V0Resources__LocationViewIn",
        "GoogleAdsSearchads360V0Resources__LocationViewOut": "_searchads360_103_GoogleAdsSearchads360V0Resources__LocationViewOut",
        "GoogleAdsSearchads360V0Services__SearchAds360RowIn": "_searchads360_104_GoogleAdsSearchads360V0Services__SearchAds360RowIn",
        "GoogleAdsSearchads360V0Services__SearchAds360RowOut": "_searchads360_105_GoogleAdsSearchads360V0Services__SearchAds360RowOut",
        "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingIn": "_searchads360_106_GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingIn",
        "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut": "_searchads360_107_GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut",
        "GoogleAdsSearchads360V0Common__MaximizeConversionValueIn": "_searchads360_108_GoogleAdsSearchads360V0Common__MaximizeConversionValueIn",
        "GoogleAdsSearchads360V0Common__MaximizeConversionValueOut": "_searchads360_109_GoogleAdsSearchads360V0Common__MaximizeConversionValueOut",
        "GoogleAdsSearchads360V0Common__TargetImpressionShareIn": "_searchads360_110_GoogleAdsSearchads360V0Common__TargetImpressionShareIn",
        "GoogleAdsSearchads360V0Common__TargetImpressionShareOut": "_searchads360_111_GoogleAdsSearchads360V0Common__TargetImpressionShareOut",
        "GoogleAdsSearchads360V0Common__MetricsIn": "_searchads360_112_GoogleAdsSearchads360V0Common__MetricsIn",
        "GoogleAdsSearchads360V0Common__MetricsOut": "_searchads360_113_GoogleAdsSearchads360V0Common__MetricsOut",
        "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingIn": "_searchads360_114_GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingOut": "_searchads360_115_GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingOut",
        "GoogleAdsSearchads360V0Resources__KeywordViewIn": "_searchads360_116_GoogleAdsSearchads360V0Resources__KeywordViewIn",
        "GoogleAdsSearchads360V0Resources__KeywordViewOut": "_searchads360_117_GoogleAdsSearchads360V0Resources__KeywordViewOut",
        "GoogleAdsSearchads360V0Errors__SearchAds360FailureIn": "_searchads360_118_GoogleAdsSearchads360V0Errors__SearchAds360FailureIn",
        "GoogleAdsSearchads360V0Errors__SearchAds360FailureOut": "_searchads360_119_GoogleAdsSearchads360V0Errors__SearchAds360FailureOut",
        "GoogleAdsSearchads360V0Common__TargetRestrictionIn": "_searchads360_120_GoogleAdsSearchads360V0Common__TargetRestrictionIn",
        "GoogleAdsSearchads360V0Common__TargetRestrictionOut": "_searchads360_121_GoogleAdsSearchads360V0Common__TargetRestrictionOut",
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn": "_searchads360_122_GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut": "_searchads360_123_GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut",
        "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn": "_searchads360_124_GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut": "_searchads360_125_GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut",
        "GoogleAdsSearchads360V0Common__AgeRangeInfoIn": "_searchads360_126_GoogleAdsSearchads360V0Common__AgeRangeInfoIn",
        "GoogleAdsSearchads360V0Common__AgeRangeInfoOut": "_searchads360_127_GoogleAdsSearchads360V0Common__AgeRangeInfoOut",
        "GoogleAdsSearchads360V0Common__KeywordInfoIn": "_searchads360_128_GoogleAdsSearchads360V0Common__KeywordInfoIn",
        "GoogleAdsSearchads360V0Common__KeywordInfoOut": "_searchads360_129_GoogleAdsSearchads360V0Common__KeywordInfoOut",
        "GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn": "_searchads360_130_GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut": "_searchads360_131_GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut",
        "GoogleAdsSearchads360V0Common__GenderInfoIn": "_searchads360_132_GoogleAdsSearchads360V0Common__GenderInfoIn",
        "GoogleAdsSearchads360V0Common__GenderInfoOut": "_searchads360_133_GoogleAdsSearchads360V0Common__GenderInfoOut",
        "GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn": "_searchads360_134_GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn",
        "GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut": "_searchads360_135_GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut",
        "GoogleAdsSearchads360V0Resources__ProductGroupViewIn": "_searchads360_136_GoogleAdsSearchads360V0Resources__ProductGroupViewIn",
        "GoogleAdsSearchads360V0Resources__ProductGroupViewOut": "_searchads360_137_GoogleAdsSearchads360V0Resources__ProductGroupViewOut",
        "GoogleAdsSearchads360V0Errors__ErrorLocationIn": "_searchads360_138_GoogleAdsSearchads360V0Errors__ErrorLocationIn",
        "GoogleAdsSearchads360V0Errors__ErrorLocationOut": "_searchads360_139_GoogleAdsSearchads360V0Errors__ErrorLocationOut",
        "GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn": "_searchads360_140_GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn",
        "GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut": "_searchads360_141_GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut",
        "GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn": "_searchads360_142_GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn",
        "GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut": "_searchads360_143_GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut",
        "GoogleAdsSearchads360V0Common__PercentCpcIn": "_searchads360_144_GoogleAdsSearchads360V0Common__PercentCpcIn",
        "GoogleAdsSearchads360V0Common__PercentCpcOut": "_searchads360_145_GoogleAdsSearchads360V0Common__PercentCpcOut",
        "GoogleAdsSearchads360V0Resources__AdGroupAdIn": "_searchads360_146_GoogleAdsSearchads360V0Resources__AdGroupAdIn",
        "GoogleAdsSearchads360V0Resources__AdGroupAdOut": "_searchads360_147_GoogleAdsSearchads360V0Resources__AdGroupAdOut",
        "GoogleAdsSearchads360V0Common__TargetCpaIn": "_searchads360_148_GoogleAdsSearchads360V0Common__TargetCpaIn",
        "GoogleAdsSearchads360V0Common__TargetCpaOut": "_searchads360_149_GoogleAdsSearchads360V0Common__TargetCpaOut",
        "GoogleAdsSearchads360V0Common__TargetOutrankShareIn": "_searchads360_150_GoogleAdsSearchads360V0Common__TargetOutrankShareIn",
        "GoogleAdsSearchads360V0Common__TargetOutrankShareOut": "_searchads360_151_GoogleAdsSearchads360V0Common__TargetOutrankShareOut",
        "GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn": "_searchads360_152_GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn",
        "GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut": "_searchads360_153_GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut",
        "GoogleAdsSearchads360V0Errors__ErrorCodeIn": "_searchads360_154_GoogleAdsSearchads360V0Errors__ErrorCodeIn",
        "GoogleAdsSearchads360V0Errors__ErrorCodeOut": "_searchads360_155_GoogleAdsSearchads360V0Errors__ErrorCodeOut",
        "GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn": "_searchads360_156_GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn",
        "GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut": "_searchads360_157_GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut",
        "GoogleAdsSearchads360V0Common__ManualCpmIn": "_searchads360_158_GoogleAdsSearchads360V0Common__ManualCpmIn",
        "GoogleAdsSearchads360V0Common__ManualCpmOut": "_searchads360_159_GoogleAdsSearchads360V0Common__ManualCpmOut",
        "GoogleAdsSearchads360V0Resources__UserListIn": "_searchads360_160_GoogleAdsSearchads360V0Resources__UserListIn",
        "GoogleAdsSearchads360V0Resources__UserListOut": "_searchads360_161_GoogleAdsSearchads360V0Resources__UserListOut",
        "GoogleAdsSearchads360V0Resources__ConversionActionIn": "_searchads360_162_GoogleAdsSearchads360V0Resources__ConversionActionIn",
        "GoogleAdsSearchads360V0Resources__ConversionActionOut": "_searchads360_163_GoogleAdsSearchads360V0Resources__ConversionActionOut",
        "GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn": "_searchads360_164_GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn",
        "GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut": "_searchads360_165_GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut",
        "GoogleAdsSearchads360V0Common__MaximizeConversionsIn": "_searchads360_166_GoogleAdsSearchads360V0Common__MaximizeConversionsIn",
        "GoogleAdsSearchads360V0Common__MaximizeConversionsOut": "_searchads360_167_GoogleAdsSearchads360V0Common__MaximizeConversionsOut",
        "GoogleAdsSearchads360V0Common__TargetingSettingIn": "_searchads360_168_GoogleAdsSearchads360V0Common__TargetingSettingIn",
        "GoogleAdsSearchads360V0Common__TargetingSettingOut": "_searchads360_169_GoogleAdsSearchads360V0Common__TargetingSettingOut",
        "GoogleAdsSearchads360V0Common__EnhancedCpcIn": "_searchads360_170_GoogleAdsSearchads360V0Common__EnhancedCpcIn",
        "GoogleAdsSearchads360V0Common__EnhancedCpcOut": "_searchads360_171_GoogleAdsSearchads360V0Common__EnhancedCpcOut",
        "GoogleAdsSearchads360V0Common__LocationGroupInfoIn": "_searchads360_172_GoogleAdsSearchads360V0Common__LocationGroupInfoIn",
        "GoogleAdsSearchads360V0Common__LocationGroupInfoOut": "_searchads360_173_GoogleAdsSearchads360V0Common__LocationGroupInfoOut",
        "GoogleAdsSearchads360V0Resources__WebpageViewIn": "_searchads360_174_GoogleAdsSearchads360V0Resources__WebpageViewIn",
        "GoogleAdsSearchads360V0Resources__WebpageViewOut": "_searchads360_175_GoogleAdsSearchads360V0Resources__WebpageViewOut",
        "GoogleAdsSearchads360V0Resources__SearchAds360FieldIn": "_searchads360_176_GoogleAdsSearchads360V0Resources__SearchAds360FieldIn",
        "GoogleAdsSearchads360V0Resources__SearchAds360FieldOut": "_searchads360_177_GoogleAdsSearchads360V0Resources__SearchAds360FieldOut",
        "GoogleAdsSearchads360V0Common__SegmentsIn": "_searchads360_178_GoogleAdsSearchads360V0Common__SegmentsIn",
        "GoogleAdsSearchads360V0Common__SegmentsOut": "_searchads360_179_GoogleAdsSearchads360V0Common__SegmentsOut",
        "GoogleAdsSearchads360V0Common__ManualCpcIn": "_searchads360_180_GoogleAdsSearchads360V0Common__ManualCpcIn",
        "GoogleAdsSearchads360V0Common__ManualCpcOut": "_searchads360_181_GoogleAdsSearchads360V0Common__ManualCpcOut",
        "GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn": "_searchads360_182_GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn",
        "GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut": "_searchads360_183_GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut",
        "GoogleAdsSearchads360V0Resources__CustomColumnIn": "_searchads360_184_GoogleAdsSearchads360V0Resources__CustomColumnIn",
        "GoogleAdsSearchads360V0Resources__CustomColumnOut": "_searchads360_185_GoogleAdsSearchads360V0Resources__CustomColumnOut",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseIn": "_searchads360_186_GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseIn",
        "GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut": "_searchads360_187_GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut",
        "GoogleAdsSearchads360V0Resources__GenderViewIn": "_searchads360_188_GoogleAdsSearchads360V0Resources__GenderViewIn",
        "GoogleAdsSearchads360V0Resources__GenderViewOut": "_searchads360_189_GoogleAdsSearchads360V0Resources__GenderViewOut",
        "GoogleAdsSearchads360V0Resources__LabelIn": "_searchads360_190_GoogleAdsSearchads360V0Resources__LabelIn",
        "GoogleAdsSearchads360V0Resources__LabelOut": "_searchads360_191_GoogleAdsSearchads360V0Resources__LabelOut",
        "GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn": "_searchads360_192_GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn",
        "GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut": "_searchads360_193_GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleAdsSearchads360V0Common__ManualCpaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpaIn"])
    types["GoogleAdsSearchads360V0Common__ManualCpaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpaOut"])
    types["GoogleAdsSearchads360V0Common__TextLabelIn"] = t.struct(
        {"description": t.string().optional(), "backgroundColor": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TextLabelIn"])
    types["GoogleAdsSearchads360V0Common__TextLabelOut"] = t.struct(
        {
            "description": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TextLabelOut"])
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
            "activityId": t.string().optional(),
            "activityGroupTag": t.string().optional(),
            "activityTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut"
        ]
    )
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
            "attributionModel": t.string().optional(),
            "dataDrivenModelStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut"
        ]
    )
    types["GoogleAdsSearchads360V0Common__KeywordIn"] = t.struct(
        {
            "adGroupCriterion": t.string().optional(),
            "info": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__KeywordIn"])
    types["GoogleAdsSearchads360V0Common__KeywordOut"] = t.struct(
        {
            "adGroupCriterion": t.string().optional(),
            "info": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__KeywordOut"])
    types["GoogleAdsSearchads360V0Resources__CampaignBudgetIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "period": t.string().optional(),
            "deliveryMethod": t.string().optional(),
            "amountMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignBudgetIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignBudgetOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "period": t.string().optional(),
            "deliveryMethod": t.string().optional(),
            "amountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignBudgetOut"])
    types["GoogleAdsSearchads360V0Resources__CampaignCriterionIn"] = t.struct(
        {
            "ageRange": t.proxy(
                renames["GoogleAdsSearchads360V0Common__AgeRangeInfoIn"]
            ).optional(),
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationInfoIn"]
            ).optional(),
            "negative": t.boolean().optional(),
            "webpage": t.proxy(
                renames["GoogleAdsSearchads360V0Common__WebpageInfoIn"]
            ).optional(),
            "resourceName": t.string().optional(),
            "locationGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationGroupInfoIn"]
            ).optional(),
            "language": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LanguageInfoIn"]
            ).optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoIn"]
            ).optional(),
            "device": t.proxy(
                renames["GoogleAdsSearchads360V0Common__DeviceInfoIn"]
            ).optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Common__UserListInfoIn"]
            ).optional(),
            "status": t.string().optional(),
            "gender": t.proxy(
                renames["GoogleAdsSearchads360V0Common__GenderInfoIn"]
            ).optional(),
            "bidModifier": t.number().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignCriterionIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignCriterionOut"] = t.struct(
        {
            "ageRange": t.proxy(
                renames["GoogleAdsSearchads360V0Common__AgeRangeInfoOut"]
            ).optional(),
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationInfoOut"]
            ).optional(),
            "negative": t.boolean().optional(),
            "webpage": t.proxy(
                renames["GoogleAdsSearchads360V0Common__WebpageInfoOut"]
            ).optional(),
            "criterionId": t.string().optional(),
            "resourceName": t.string().optional(),
            "locationGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationGroupInfoOut"]
            ).optional(),
            "language": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LanguageInfoOut"]
            ).optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoOut"]
            ).optional(),
            "device": t.proxy(
                renames["GoogleAdsSearchads360V0Common__DeviceInfoOut"]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Common__UserListInfoOut"]
            ).optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "status": t.string().optional(),
            "gender": t.proxy(
                renames["GoogleAdsSearchads360V0Common__GenderInfoOut"]
            ).optional(),
            "bidModifier": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignCriterionOut"])
    types["GoogleAdsSearchads360V0Common__FrequencyCapEntryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__FrequencyCapEntryIn"])
    types["GoogleAdsSearchads360V0Common__FrequencyCapEntryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__FrequencyCapEntryOut"])
    types["GoogleAdsSearchads360V0Common__WebpageConditionInfoIn"] = t.struct(
        {
            "argument": t.string().optional(),
            "operator": t.string().optional(),
            "operand": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__WebpageConditionInfoIn"])
    types["GoogleAdsSearchads360V0Common__WebpageConditionInfoOut"] = t.struct(
        {
            "argument": t.string().optional(),
            "operator": t.string().optional(),
            "operand": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__WebpageConditionInfoOut"])
    types["GoogleAdsSearchads360V0Resources__CampaignIn"] = t.struct(
        {
            "dynamicSearchAdsSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn"
                ]
            ).optional(),
            "endDate": t.string().optional(),
            "shoppingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn"]
            ).optional(),
            "optimizationGoalSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingIn"
                ]
            ).optional(),
            "selectiveOptimization": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationIn"
                ]
            ).optional(),
            "finalUrlSuffix": t.string().optional(),
            "maximizeConversionValue": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueIn"]
            ).optional(),
            "urlExpansionOptOut": t.boolean().optional(),
            "campaignBudget": t.string().optional(),
            "targetCpm": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpmIn"]
            ).optional(),
            "startDate": t.string().optional(),
            "maximizeConversions": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionsIn"]
            ).optional(),
            "realTimeBiddingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn"]
            ).optional(),
            "manualCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpaIn"]
            ).optional(),
            "biddingStrategy": t.string().optional(),
            "adServingOptimizationStatus": t.string().optional(),
            "geoTargetTypeSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingIn"
                ]
            ).optional(),
            "excludedParentAssetFieldTypes": t.array(t.string()).optional(),
            "networkSettings": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn"]
            ).optional(),
            "urlCustomParameters": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__CustomParameterIn"])
            ).optional(),
            "resourceName": t.string().optional(),
            "trackingUrlTemplate": t.string().optional(),
            "targetCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpaIn"]
            ).optional(),
            "frequencyCaps": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__FrequencyCapEntryIn"])
            ).optional(),
            "targetRoas": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetRoasIn"]
            ).optional(),
            "advertisingChannelType": t.string().optional(),
            "status": t.string().optional(),
            "percentCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__PercentCpcIn"]
            ).optional(),
            "targetImpressionShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetImpressionShareIn"]
            ).optional(),
            "manualCpm": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpmIn"]
            ).optional(),
            "manualCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpcIn"]
            ).optional(),
            "name": t.string().optional(),
            "advertisingChannelSubType": t.string().optional(),
            "targetSpend": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetSpendIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignOut"] = t.struct(
        {
            "dynamicSearchAdsSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut"
                ]
            ).optional(),
            "endDate": t.string().optional(),
            "shoppingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut"]
            ).optional(),
            "optimizationGoalSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSettingOut"
                ]
            ).optional(),
            "selectiveOptimization": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimizationOut"
                ]
            ).optional(),
            "finalUrlSuffix": t.string().optional(),
            "maximizeConversionValue": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueOut"]
            ).optional(),
            "urlExpansionOptOut": t.boolean().optional(),
            "servingStatus": t.string().optional(),
            "campaignBudget": t.string().optional(),
            "targetCpm": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpmOut"]
            ).optional(),
            "startDate": t.string().optional(),
            "maximizeConversions": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionsOut"]
            ).optional(),
            "realTimeBiddingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut"]
            ).optional(),
            "manualCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpaOut"]
            ).optional(),
            "biddingStrategy": t.string().optional(),
            "adServingOptimizationStatus": t.string().optional(),
            "id": t.string().optional(),
            "geoTargetTypeSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSettingOut"
                ]
            ).optional(),
            "excludedParentAssetFieldTypes": t.array(t.string()).optional(),
            "networkSettings": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut"]
            ).optional(),
            "urlCustomParameters": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__CustomParameterOut"])
            ).optional(),
            "resourceName": t.string().optional(),
            "trackingUrlTemplate": t.string().optional(),
            "targetCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpaOut"]
            ).optional(),
            "frequencyCaps": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__FrequencyCapEntryOut"])
            ).optional(),
            "targetRoas": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetRoasOut"]
            ).optional(),
            "advertisingChannelType": t.string().optional(),
            "status": t.string().optional(),
            "creationTime": t.string().optional(),
            "createTime": t.string().optional(),
            "percentCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__PercentCpcOut"]
            ).optional(),
            "trackingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut"]
            ).optional(),
            "engineId": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "targetImpressionShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetImpressionShareOut"]
            ).optional(),
            "manualCpm": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpmOut"]
            ).optional(),
            "manualCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ManualCpcOut"]
            ).optional(),
            "name": t.string().optional(),
            "biddingStrategyType": t.string().optional(),
            "advertisingChannelSubType": t.string().optional(),
            "targetSpend": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetSpendOut"]
            ).optional(),
            "biddingStrategySystemStatus": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignOut"])
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
    types["GoogleAdsSearchads360V0Resources__CampaignLabelIn"] = t.struct(
        {
            "label": t.string().optional(),
            "campaign": t.string().optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignLabelIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "campaign": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignLabelOut"])
    types["GoogleAdsSearchads360V0Common__DeviceInfoIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__DeviceInfoIn"])
    types["GoogleAdsSearchads360V0Common__DeviceInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__DeviceInfoOut"])
    types["GoogleAdsSearchads360V0Services__CustomColumnHeaderIn"] = t.struct(
        {
            "referencesMetrics": t.boolean().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__CustomColumnHeaderIn"])
    types["GoogleAdsSearchads360V0Services__CustomColumnHeaderOut"] = t.struct(
        {
            "referencesMetrics": t.boolean().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__CustomColumnHeaderOut"])
    types["GoogleAdsSearchads360V0Services__SearchSearchAds360RequestIn"] = t.struct(
        {
            "returnTotalResultsCount": t.boolean().optional(),
            "query": t.string(),
            "summaryRowSetting": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchSearchAds360RequestIn"])
    types["GoogleAdsSearchads360V0Services__SearchSearchAds360RequestOut"] = t.struct(
        {
            "returnTotalResultsCount": t.boolean().optional(),
            "query": t.string(),
            "summaryRowSetting": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchSearchAds360RequestOut"])
    types["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingIn"])
    types["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_TrackingSettingOut"])
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
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldIn"]
                )
            ).optional(),
            "totalResultsCount": t.string().optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseIn"]
    )
    types[
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldOut"]
                )
            ).optional(),
            "totalResultsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseOut"]
    )
    types["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn"] = t.struct(
        {
            "label": t.string().optional(),
            "resourceName": t.string().optional(),
            "adGroupCriterion": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "resourceName": t.string().optional(),
            "adGroupCriterion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut"])
    types["GoogleAdsSearchads360V0Common__TargetSpendIn"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "targetSpendMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetSpendIn"])
    types["GoogleAdsSearchads360V0Common__TargetSpendOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "targetSpendMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetSpendOut"])
    types["GoogleAdsSearchads360V0Common__LanguageInfoIn"] = t.struct(
        {"languageConstant": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__LanguageInfoIn"])
    types["GoogleAdsSearchads360V0Common__LanguageInfoOut"] = t.struct(
        {
            "languageConstant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__LanguageInfoOut"])
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
    types["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn"] = t.struct(
        {
            "targetPartnerSearchNetwork": t.boolean().optional(),
            "targetContentNetwork": t.boolean().optional(),
            "targetGoogleSearch": t.boolean().optional(),
            "targetSearchNetwork": t.boolean().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsIn"])
    types["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut"] = t.struct(
        {
            "targetPartnerSearchNetwork": t.boolean().optional(),
            "targetContentNetwork": t.boolean().optional(),
            "targetGoogleSearch": t.boolean().optional(),
            "targetSearchNetwork": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_NetworkSettingsOut"])
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
    types["GoogleAdsSearchads360V0Resources__BiddingStrategyIn"] = t.struct(
        {
            "targetCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpaIn"]
            ).optional(),
            "targetSpend": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetSpendIn"]
            ).optional(),
            "targetImpressionShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetImpressionShareIn"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "resourceName": t.string().optional(),
            "targetRoas": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetRoasIn"]
            ).optional(),
            "name": t.string().optional(),
            "maximizeConversionValue": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueIn"]
            ).optional(),
            "enhancedCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__EnhancedCpcIn"]
            ).optional(),
            "maximizeConversions": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionsIn"]
            ).optional(),
            "targetOutrankShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetOutrankShareIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__BiddingStrategyIn"])
    types["GoogleAdsSearchads360V0Resources__BiddingStrategyOut"] = t.struct(
        {
            "targetCpa": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetCpaOut"]
            ).optional(),
            "targetSpend": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetSpendOut"]
            ).optional(),
            "nonRemovedCampaignCount": t.string().optional(),
            "targetImpressionShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetImpressionShareOut"]
            ).optional(),
            "type": t.string().optional(),
            "currencyCode": t.string().optional(),
            "status": t.string().optional(),
            "resourceName": t.string().optional(),
            "targetRoas": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetRoasOut"]
            ).optional(),
            "effectiveCurrencyCode": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "maximizeConversionValue": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueOut"]
            ).optional(),
            "enhancedCpc": t.proxy(
                renames["GoogleAdsSearchads360V0Common__EnhancedCpcOut"]
            ).optional(),
            "maximizeConversions": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MaximizeConversionsOut"]
            ).optional(),
            "campaignCount": t.string().optional(),
            "targetOutrankShare": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetOutrankShareOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__BiddingStrategyOut"])
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
    types["GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "bidModifier": t.number().optional(),
            "device": t.proxy(
                renames["GoogleAdsSearchads360V0Common__DeviceInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "bidModifier": t.number().optional(),
            "device": t.proxy(
                renames["GoogleAdsSearchads360V0Common__DeviceInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut"])
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
    types["GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn"] = t.struct(
        {
            "headline2": t.string().optional(),
            "headline3": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "description1": t.string().optional(),
            "description2": t.string().optional(),
            "path2": t.string().optional(),
            "path1": t.string().optional(),
            "headline": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn"])
    types[
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut"
    ] = t.struct(
        {
            "headline2": t.string().optional(),
            "headline3": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "description1": t.string().optional(),
            "description2": t.string().optional(),
            "path2": t.string().optional(),
            "path1": t.string().optional(),
            "headline": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut"]
    )
    types["GoogleAdsSearchads360V0Resources__ConversionTrackingSettingIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__ConversionTrackingSettingIn"])
    types["GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut"] = t.struct(
        {
            "enhancedConversionsForLeadsEnabled": t.boolean().optional(),
            "acceptedCustomerDataTerms": t.boolean().optional(),
            "googleAdsCrossAccountConversionTrackingId": t.string().optional(),
            "crossAccountConversionTrackingId": t.string().optional(),
            "conversionTrackingStatus": t.string().optional(),
            "conversionTrackingId": t.string().optional(),
            "googleAdsConversionCustomer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut"])
    types[
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestIn"
    ] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "query": t.string(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestIn"]
    )
    types[
        "GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestOut"
    ] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "query": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequestOut"]
    )
    types["GoogleAdsSearchads360V0Resources__AdGroupCriterionIn"] = t.struct(
        {
            "cpcBidMicros": t.string().optional(),
            "resourceName": t.string().optional(),
            "adGroup": t.string().optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Common__UserListInfoIn"]
            ).optional(),
            "bidModifier": t.number().optional(),
            "listingGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ListingGroupInfoIn"]
            ).optional(),
            "gender": t.proxy(
                renames["GoogleAdsSearchads360V0Common__GenderInfoIn"]
            ).optional(),
            "status": t.string().optional(),
            "negative": t.boolean().optional(),
            "finalUrlSuffix": t.string().optional(),
            "ageRange": t.proxy(
                renames["GoogleAdsSearchads360V0Common__AgeRangeInfoIn"]
            ).optional(),
            "webpage": t.proxy(
                renames["GoogleAdsSearchads360V0Common__WebpageInfoIn"]
            ).optional(),
            "finalUrls": t.array(t.string()).optional(),
            "trackingUrlTemplate": t.string().optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupCriterionOut"] = t.struct(
        {
            "cpcBidMicros": t.string().optional(),
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Common__LocationInfoOut"]
            ).optional(),
            "resourceName": t.string().optional(),
            "criterionId": t.string().optional(),
            "adGroup": t.string().optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Common__UserListInfoOut"]
            ).optional(),
            "creationTime": t.string().optional(),
            "bidModifier": t.number().optional(),
            "listingGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ListingGroupInfoOut"]
            ).optional(),
            "gender": t.proxy(
                renames["GoogleAdsSearchads360V0Common__GenderInfoOut"]
            ).optional(),
            "status": t.string().optional(),
            "negative": t.boolean().optional(),
            "finalUrlSuffix": t.string().optional(),
            "engineId": t.string().optional(),
            "ageRange": t.proxy(
                renames["GoogleAdsSearchads360V0Common__AgeRangeInfoOut"]
            ).optional(),
            "webpage": t.proxy(
                renames["GoogleAdsSearchads360V0Common__WebpageInfoOut"]
            ).optional(),
            "labels": t.array(t.string()).optional(),
            "finalUrls": t.array(t.string()).optional(),
            "lastModifiedTime": t.string().optional(),
            "trackingUrlTemplate": t.string().optional(),
            "type": t.string().optional(),
            "qualityInfo": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfoOut"
                ]
            ).optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordInfoOut"]
            ).optional(),
            "engineStatus": t.string().optional(),
            "effectiveCpcBidMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionOut"])
    types[
        "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn"
    ] = t.struct(
        {
            "defaultCurrencyCode": t.string().optional(),
            "defaultValue": t.number().optional(),
            "alwaysUseDefaultValue": t.boolean().optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut"
    ] = t.struct(
        {
            "defaultCurrencyCode": t.string().optional(),
            "defaultValue": t.number().optional(),
            "alwaysUseDefaultValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut"]
    )
    types["GoogleAdsSearchads360V0Resources__AdGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "status": t.string().optional(),
            "cpcBidMicros": t.string().optional(),
            "adRotationMode": t.string().optional(),
            "type": t.string().optional(),
            "targetingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetingSettingIn"]
            ).optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "startDate": t.string().optional(),
            "creationTime": t.string().optional(),
            "status": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "cpcBidMicros": t.string().optional(),
            "languageCode": t.string().optional(),
            "adRotationMode": t.string().optional(),
            "id": t.string().optional(),
            "engineStatus": t.string().optional(),
            "engineId": t.string().optional(),
            "type": t.string().optional(),
            "targetingSetting": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TargetingSettingOut"]
            ).optional(),
            "endDate": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupOut"])
    types["GoogleAdsSearchads360V0Resources__CustomerClientIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerClientIn"])
    types["GoogleAdsSearchads360V0Resources__CustomerClientOut"] = t.struct(
        {
            "clientCustomer": t.string().optional(),
            "testAccount": t.boolean().optional(),
            "currencyCode": t.string().optional(),
            "id": t.string().optional(),
            "appliedLabels": t.array(t.string()).optional(),
            "resourceName": t.string().optional(),
            "hidden": t.boolean().optional(),
            "descriptiveName": t.string().optional(),
            "manager": t.boolean().optional(),
            "status": t.string().optional(),
            "level": t.string().optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerClientOut"])
    types["GoogleAdsSearchads360V0Common__TargetRoasIn"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "cpcBidFloorMicros": t.string().optional(),
            "targetRoas": t.number(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetRoasIn"])
    types["GoogleAdsSearchads360V0Common__TargetRoasOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "cpcBidFloorMicros": t.string().optional(),
            "targetRoas": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetRoasOut"])
    types["GoogleAdsSearchads360V0Common__WebpageInfoIn"] = t.struct(
        {
            "criterionName": t.string().optional(),
            "coveragePercentage": t.number().optional(),
            "conditions": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Common__WebpageConditionInfoIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__WebpageInfoIn"])
    types["GoogleAdsSearchads360V0Common__WebpageInfoOut"] = t.struct(
        {
            "criterionName": t.string().optional(),
            "coveragePercentage": t.number().optional(),
            "conditions": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Common__WebpageConditionInfoOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__WebpageInfoOut"])
    types["GoogleAdsSearchads360V0Resources__CustomerIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "resourceName": t.string().optional(),
            "trackingUrlTemplate": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "autoTaggingEnabled": t.boolean().optional(),
            "timeZone": t.string().optional(),
            "finalUrlSuffix": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerIn"])
    types["GoogleAdsSearchads360V0Resources__CustomerOut"] = t.struct(
        {
            "id": t.string().optional(),
            "accountType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "creationTime": t.string().optional(),
            "resourceName": t.string().optional(),
            "engineId": t.string().optional(),
            "trackingUrlTemplate": t.string().optional(),
            "accountStatus": t.string().optional(),
            "status": t.string().optional(),
            "manager": t.boolean().optional(),
            "descriptiveName": t.string().optional(),
            "autoTaggingEnabled": t.boolean().optional(),
            "timeZone": t.string().optional(),
            "finalUrlSuffix": t.string().optional(),
            "conversionTrackingSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources__ConversionTrackingSettingOut"
                ]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "doubleClickCampaignManagerSetting": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerOut"])
    types["GoogleAdsSearchads360V0Common__UserListInfoIn"] = t.struct(
        {"userList": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__UserListInfoIn"])
    types["GoogleAdsSearchads360V0Common__UserListInfoOut"] = t.struct(
        {
            "userList": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__UserListInfoOut"])
    types["GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn"])
    types["GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut"])
    types["GoogleAdsSearchads360V0Resources__AgeRangeViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__AgeRangeViewIn"])
    types["GoogleAdsSearchads360V0Resources__AgeRangeViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AgeRangeViewOut"])
    types["GoogleAdsSearchads360V0Common__ValueIn"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "floatValue": t.number().optional(),
            "int64Value": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__ValueIn"])
    types["GoogleAdsSearchads360V0Common__ValueOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "floatValue": t.number().optional(),
            "int64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__ValueOut"])
    types["GoogleAdsSearchads360V0Resources__AdIn"] = t.struct(
        {
            "responsiveSearchAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoIn"
                ]
            ).optional(),
            "resourceName": t.string().optional(),
            "textAd": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn"]
            ).optional(),
            "finalUrls": t.array(t.string()).optional(),
            "expandedDynamicSearchAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn"
                ]
            ).optional(),
            "name": t.string().optional(),
            "productAd": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn"]
            ).optional(),
            "displayUrl": t.string().optional(),
            "expandedTextAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdIn"])
    types["GoogleAdsSearchads360V0Resources__AdOut"] = t.struct(
        {
            "responsiveSearchAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfoOut"
                ]
            ).optional(),
            "resourceName": t.string().optional(),
            "type": t.string().optional(),
            "textAd": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut"]
            ).optional(),
            "finalUrls": t.array(t.string()).optional(),
            "expandedDynamicSearchAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut"
                ]
            ).optional(),
            "name": t.string().optional(),
            "productAd": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut"]
            ).optional(),
            "displayUrl": t.string().optional(),
            "expandedTextAd": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfoOut"
                ]
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdOut"])
    types["GoogleAdsSearchads360V0Common__TargetCpmIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TargetCpmIn"])
    types["GoogleAdsSearchads360V0Common__TargetCpmOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TargetCpmOut"])
    types["GoogleAdsSearchads360V0Common__LocationInfoIn"] = t.struct(
        {"geoTargetConstant": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__LocationInfoIn"])
    types["GoogleAdsSearchads360V0Common__LocationInfoOut"] = t.struct(
        {
            "geoTargetConstant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__LocationInfoOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupLabelIn"] = t.struct(
        {
            "label": t.string().optional(),
            "resourceName": t.string().optional(),
            "adGroup": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupLabelIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupLabelOut"] = t.struct(
        {
            "label": t.string().optional(),
            "resourceName": t.string().optional(),
            "adGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupLabelOut"])
    types["GoogleAdsSearchads360V0Resources__LocationViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__LocationViewIn"])
    types["GoogleAdsSearchads360V0Resources__LocationViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__LocationViewOut"])
    types["GoogleAdsSearchads360V0Services__SearchAds360RowIn"] = t.struct(
        {
            "adGroupLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupLabelIn"]
            ).optional(),
            "customer": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerIn"]
            ).optional(),
            "conversionAction": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__ConversionActionIn"]
            ).optional(),
            "campaignCriterion": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignCriterionIn"]
            ).optional(),
            "adGroupAdLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn"]
            ).optional(),
            "metrics": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MetricsIn"]
            ).optional(),
            "customerManagerLink": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn"]
            ).optional(),
            "keywordView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__KeywordViewIn"]
            ).optional(),
            "campaignLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignLabelIn"]
            ).optional(),
            "adGroupAudienceView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn"]
            ).optional(),
            "adGroupAd": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAdIn"]
            ).optional(),
            "dynamicSearchAdsSearchTermView": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewIn"
                ]
            ).optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__UserListIn"]
            ).optional(),
            "segments": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SegmentsIn"]
            ).optional(),
            "adGroupBidModifier": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupBidModifierIn"]
            ).optional(),
            "locationView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__LocationViewIn"]
            ).optional(),
            "adGroupCriterionLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelIn"]
            ).optional(),
            "customColumns": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__ValueIn"])
            ).optional(),
            "label": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__LabelIn"]
            ).optional(),
            "adGroupCriterion": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionIn"]
            ).optional(),
            "biddingStrategy": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__BiddingStrategyIn"]
            ).optional(),
            "adGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupIn"]
            ).optional(),
            "customerClient": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerClientIn"]
            ).optional(),
            "productGroupView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__ProductGroupViewIn"]
            ).optional(),
            "genderView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__GenderViewIn"]
            ).optional(),
            "webpageView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__WebpageViewIn"]
            ).optional(),
            "campaign": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignIn"]
            ).optional(),
            "ageRangeView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AgeRangeViewIn"]
            ).optional(),
            "campaignBudget": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignBudgetIn"]
            ).optional(),
            "campaignAudienceView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignAudienceViewIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchAds360RowIn"])
    types["GoogleAdsSearchads360V0Services__SearchAds360RowOut"] = t.struct(
        {
            "adGroupLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupLabelOut"]
            ).optional(),
            "customer": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerOut"]
            ).optional(),
            "conversionAction": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__ConversionActionOut"]
            ).optional(),
            "campaignCriterion": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignCriterionOut"]
            ).optional(),
            "adGroupAdLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut"]
            ).optional(),
            "metrics": t.proxy(
                renames["GoogleAdsSearchads360V0Common__MetricsOut"]
            ).optional(),
            "customerManagerLink": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut"]
            ).optional(),
            "keywordView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__KeywordViewOut"]
            ).optional(),
            "campaignLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignLabelOut"]
            ).optional(),
            "adGroupAudienceView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut"]
            ).optional(),
            "adGroupAd": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupAdOut"]
            ).optional(),
            "dynamicSearchAdsSearchTermView": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermViewOut"
                ]
            ).optional(),
            "userList": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__UserListOut"]
            ).optional(),
            "segments": t.proxy(
                renames["GoogleAdsSearchads360V0Common__SegmentsOut"]
            ).optional(),
            "adGroupBidModifier": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupBidModifierOut"]
            ).optional(),
            "locationView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__LocationViewOut"]
            ).optional(),
            "adGroupCriterionLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionLabelOut"]
            ).optional(),
            "customColumns": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Common__ValueOut"])
            ).optional(),
            "label": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__LabelOut"]
            ).optional(),
            "adGroupCriterion": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupCriterionOut"]
            ).optional(),
            "biddingStrategy": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__BiddingStrategyOut"]
            ).optional(),
            "adGroup": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdGroupOut"]
            ).optional(),
            "customerClient": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CustomerClientOut"]
            ).optional(),
            "productGroupView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__ProductGroupViewOut"]
            ).optional(),
            "genderView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__GenderViewOut"]
            ).optional(),
            "webpageView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__WebpageViewOut"]
            ).optional(),
            "campaign": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignOut"]
            ).optional(),
            "ageRangeView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AgeRangeViewOut"]
            ).optional(),
            "campaignBudget": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignBudgetOut"]
            ).optional(),
            "campaignAudienceView": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__CampaignAudienceViewOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchAds360RowOut"])
    types[
        "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut"
    ] = t.struct(
        {
            "networkId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSettingOut"
        ]
    )
    types["GoogleAdsSearchads360V0Common__MaximizeConversionValueIn"] = t.struct(
        {
            "cpcBidFloorMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "targetRoas": t.number().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueIn"])
    types["GoogleAdsSearchads360V0Common__MaximizeConversionValueOut"] = t.struct(
        {
            "cpcBidFloorMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "targetRoas": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MaximizeConversionValueOut"])
    types["GoogleAdsSearchads360V0Common__TargetImpressionShareIn"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "locationFractionMicros": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetImpressionShareIn"])
    types["GoogleAdsSearchads360V0Common__TargetImpressionShareOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "locationFractionMicros": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetImpressionShareOut"])
    types["GoogleAdsSearchads360V0Common__MetricsIn"] = t.struct(
        {
            "allConversions": t.number().optional(),
            "historicalQualityScore": t.string().optional(),
            "allConversionsValueByConversionDate": t.number().optional(),
            "valuePerConversionsByConversionDate": t.number().optional(),
            "costPerCurrentModelAttributedConversion": t.number().optional(),
            "allConversionsFromStoreVisit": t.number().optional(),
            "valuePerAllConversionsByConversionDate": t.number().optional(),
            "searchTopImpressionShare": t.number().optional(),
            "searchBudgetLostAbsoluteTopImpressionShare": t.number().optional(),
            "clicks": t.string().optional(),
            "clientAccountConversions": t.number().optional(),
            "averageCpm": t.number().optional(),
            "searchExactMatchImpressionShare": t.number().optional(),
            "allConversionsFromMenu": t.number().optional(),
            "absoluteTopImpressionPercentage": t.number().optional(),
            "impressions": t.string().optional(),
            "contentBudgetLostImpressionShare": t.number().optional(),
            "costPerConversion": t.number().optional(),
            "allConversionsFromDirections": t.number().optional(),
            "conversionsValue": t.number().optional(),
            "crossDeviceConversions": t.number().optional(),
            "crossDeviceConversionsValue": t.number().optional(),
            "historicalLandingPageQualityScore": t.string().optional(),
            "averageCost": t.number().optional(),
            "ctr": t.number().optional(),
            "interactionEventTypes": t.array(t.string()).optional(),
            "allConversionsFromInteractionsRate": t.number().optional(),
            "topImpressionPercentage": t.number().optional(),
            "contentImpressionShare": t.number().optional(),
            "historicalCreativeQualityScore": t.string().optional(),
            "interactionRate": t.number().optional(),
            "interactions": t.string().optional(),
            "conversionsFromInteractionsRate": t.number().optional(),
            "averageCpc": t.number().optional(),
            "historicalSearchPredictedCtr": t.string().optional(),
            "searchRankLostTopImpressionShare": t.number().optional(),
            "allConversionsFromOtherEngagement": t.number().optional(),
            "invalidClicks": t.string().optional(),
            "clientAccountViewThroughConversions": t.string().optional(),
            "clientAccountConversionsValue": t.number().optional(),
            "searchClickShare": t.number().optional(),
            "allConversionsFromStoreWebsite": t.number().optional(),
            "invalidClickRate": t.number().optional(),
            "searchRankLostAbsoluteTopImpressionShare": t.number().optional(),
            "conversions": t.number().optional(),
            "searchImpressionShare": t.number().optional(),
            "conversionsByConversionDate": t.number().optional(),
            "costMicros": t.string().optional(),
            "visits": t.number().optional(),
            "allConversionsValuePerCost": t.number().optional(),
            "conversionsValueByConversionDate": t.number().optional(),
            "valuePerAllConversions": t.number().optional(),
            "searchBudgetLostTopImpressionShare": t.number().optional(),
            "contentRankLostImpressionShare": t.number().optional(),
            "mobileFriendlyClicksPercentage": t.number().optional(),
            "allConversionsFromClickToCall": t.number().optional(),
            "conversionsFromInteractionsValuePerInteraction": t.number().optional(),
            "costPerAllConversions": t.number().optional(),
            "searchRankLostImpressionShare": t.number().optional(),
            "searchBudgetLostImpressionShare": t.number().optional(),
            "allConversionsValue": t.number().optional(),
            "allConversionsByConversionDate": t.number().optional(),
            "conversionsValuePerCost": t.number().optional(),
            "allConversionsFromOrder": t.number().optional(),
            "valuePerConversion": t.number().optional(),
            "allConversionsFromInteractionsValuePerInteraction": t.number().optional(),
            "searchAbsoluteTopImpressionShare": t.number().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MetricsIn"])
    types["GoogleAdsSearchads360V0Common__MetricsOut"] = t.struct(
        {
            "allConversions": t.number().optional(),
            "historicalQualityScore": t.string().optional(),
            "allConversionsValueByConversionDate": t.number().optional(),
            "valuePerConversionsByConversionDate": t.number().optional(),
            "costPerCurrentModelAttributedConversion": t.number().optional(),
            "allConversionsFromStoreVisit": t.number().optional(),
            "valuePerAllConversionsByConversionDate": t.number().optional(),
            "searchTopImpressionShare": t.number().optional(),
            "searchBudgetLostAbsoluteTopImpressionShare": t.number().optional(),
            "clicks": t.string().optional(),
            "clientAccountConversions": t.number().optional(),
            "averageCpm": t.number().optional(),
            "searchExactMatchImpressionShare": t.number().optional(),
            "allConversionsFromMenu": t.number().optional(),
            "absoluteTopImpressionPercentage": t.number().optional(),
            "impressions": t.string().optional(),
            "contentBudgetLostImpressionShare": t.number().optional(),
            "costPerConversion": t.number().optional(),
            "allConversionsFromDirections": t.number().optional(),
            "conversionsValue": t.number().optional(),
            "crossDeviceConversions": t.number().optional(),
            "crossDeviceConversionsValue": t.number().optional(),
            "historicalLandingPageQualityScore": t.string().optional(),
            "averageCost": t.number().optional(),
            "ctr": t.number().optional(),
            "interactionEventTypes": t.array(t.string()).optional(),
            "allConversionsFromInteractionsRate": t.number().optional(),
            "topImpressionPercentage": t.number().optional(),
            "contentImpressionShare": t.number().optional(),
            "historicalCreativeQualityScore": t.string().optional(),
            "interactionRate": t.number().optional(),
            "interactions": t.string().optional(),
            "conversionsFromInteractionsRate": t.number().optional(),
            "averageCpc": t.number().optional(),
            "historicalSearchPredictedCtr": t.string().optional(),
            "searchRankLostTopImpressionShare": t.number().optional(),
            "allConversionsFromOtherEngagement": t.number().optional(),
            "invalidClicks": t.string().optional(),
            "clientAccountViewThroughConversions": t.string().optional(),
            "clientAccountConversionsValue": t.number().optional(),
            "searchClickShare": t.number().optional(),
            "allConversionsFromStoreWebsite": t.number().optional(),
            "invalidClickRate": t.number().optional(),
            "searchRankLostAbsoluteTopImpressionShare": t.number().optional(),
            "conversions": t.number().optional(),
            "searchImpressionShare": t.number().optional(),
            "conversionsByConversionDate": t.number().optional(),
            "costMicros": t.string().optional(),
            "visits": t.number().optional(),
            "allConversionsValuePerCost": t.number().optional(),
            "conversionsValueByConversionDate": t.number().optional(),
            "valuePerAllConversions": t.number().optional(),
            "searchBudgetLostTopImpressionShare": t.number().optional(),
            "contentRankLostImpressionShare": t.number().optional(),
            "mobileFriendlyClicksPercentage": t.number().optional(),
            "allConversionsFromClickToCall": t.number().optional(),
            "conversionsFromInteractionsValuePerInteraction": t.number().optional(),
            "costPerAllConversions": t.number().optional(),
            "searchRankLostImpressionShare": t.number().optional(),
            "searchBudgetLostImpressionShare": t.number().optional(),
            "allConversionsValue": t.number().optional(),
            "allConversionsByConversionDate": t.number().optional(),
            "conversionsValuePerCost": t.number().optional(),
            "allConversionsFromOrder": t.number().optional(),
            "valuePerConversion": t.number().optional(),
            "allConversionsFromInteractionsValuePerInteraction": t.number().optional(),
            "searchAbsoluteTopImpressionShare": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MetricsOut"])
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
    types["GoogleAdsSearchads360V0Resources__KeywordViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__KeywordViewIn"])
    types["GoogleAdsSearchads360V0Resources__KeywordViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__KeywordViewOut"])
    types["GoogleAdsSearchads360V0Errors__SearchAds360FailureIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn"])
            ).optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__SearchAds360FailureIn"])
    types["GoogleAdsSearchads360V0Errors__SearchAds360FailureOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut"])
            ).optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__SearchAds360FailureOut"])
    types["GoogleAdsSearchads360V0Common__TargetRestrictionIn"] = t.struct(
        {"targetingDimension": t.string().optional(), "bidOnly": t.boolean().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TargetRestrictionIn"])
    types["GoogleAdsSearchads360V0Common__TargetRestrictionOut"] = t.struct(
        {
            "targetingDimension": t.string().optional(),
            "bidOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetRestrictionOut"])
    types[
        "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoIn"
    ] = t.struct(
        {
            "description2": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "description1": t.string().optional(),
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
            "description2": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "description1": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfoOut"
        ]
    )
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn"
    ] = t.struct(
        {
            "useSuppliedUrlsOnly": t.boolean().optional(),
            "domainName": t.string(),
            "languageCode": t.string(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingIn"]
    )
    types[
        "GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut"
    ] = t.struct(
        {
            "useSuppliedUrlsOnly": t.boolean().optional(),
            "domainName": t.string(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSettingOut"]
    )
    types["GoogleAdsSearchads360V0Common__AgeRangeInfoIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__AgeRangeInfoIn"])
    types["GoogleAdsSearchads360V0Common__AgeRangeInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__AgeRangeInfoOut"])
    types["GoogleAdsSearchads360V0Common__KeywordInfoIn"] = t.struct(
        {"matchType": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__KeywordInfoIn"])
    types["GoogleAdsSearchads360V0Common__KeywordInfoOut"] = t.struct(
        {
            "matchType": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__KeywordInfoOut"])
    types["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn"] = t.struct(
        {
            "description2": t.string().optional(),
            "displayMobileUrl": t.string().optional(),
            "description1": t.string().optional(),
            "headline": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "displayUrl": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoIn"])
    types["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut"] = t.struct(
        {
            "description2": t.string().optional(),
            "displayMobileUrl": t.string().optional(),
            "description1": t.string().optional(),
            "headline": t.string().optional(),
            "adTrackingId": t.string().optional(),
            "displayUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360TextAdInfoOut"])
    types["GoogleAdsSearchads360V0Common__GenderInfoIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__GenderInfoIn"])
    types["GoogleAdsSearchads360V0Common__GenderInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__GenderInfoOut"])
    types["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoIn"])
    types["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfoOut"])
    types["GoogleAdsSearchads360V0Resources__ProductGroupViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__ProductGroupViewIn"])
    types["GoogleAdsSearchads360V0Resources__ProductGroupViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__ProductGroupViewOut"])
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
    types["GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn"] = t.struct(
        {"resourceName": t.string().optional(), "status": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerManagerLinkIn"])
    types["GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut"] = t.struct(
        {
            "managerLinkId": t.string().optional(),
            "resourceName": t.string().optional(),
            "managerCustomer": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomerManagerLinkOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn"] = t.struct(
        {
            "adGroupAd": t.string().optional(),
            "label": t.string().optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAdLabelIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut"] = t.struct(
        {
            "adGroupAd": t.string().optional(),
            "label": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAdLabelOut"])
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
    types["GoogleAdsSearchads360V0Resources__AdGroupAdIn"] = t.struct(
        {
            "ad": t.proxy(renames["GoogleAdsSearchads360V0Resources__AdIn"]).optional(),
            "status": t.string().optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAdIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAdOut"] = t.struct(
        {
            "lastModifiedTime": t.string().optional(),
            "ad": t.proxy(
                renames["GoogleAdsSearchads360V0Resources__AdOut"]
            ).optional(),
            "creationTime": t.string().optional(),
            "engineStatus": t.string().optional(),
            "status": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "resourceName": t.string().optional(),
            "engineId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAdOut"])
    types["GoogleAdsSearchads360V0Common__TargetCpaIn"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "targetCpaMicros": t.string().optional(),
            "cpcBidFloorMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetCpaIn"])
    types["GoogleAdsSearchads360V0Common__TargetCpaOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "targetCpaMicros": t.string().optional(),
            "cpcBidFloorMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetCpaOut"])
    types["GoogleAdsSearchads360V0Common__TargetOutrankShareIn"] = t.struct(
        {"cpcBidCeilingMicros": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__TargetOutrankShareIn"])
    types["GoogleAdsSearchads360V0Common__TargetOutrankShareOut"] = t.struct(
        {
            "cpcBidCeilingMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__TargetOutrankShareOut"])
    types["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn"] = t.struct(
        {"optIn": t.boolean().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingIn"])
    types["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut"] = t.struct(
        {
            "optIn": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__RealTimeBiddingSettingOut"])
    types["GoogleAdsSearchads360V0Errors__ErrorCodeIn"] = t.struct(
        {
            "internalError": t.string().optional(),
            "dateRangeError": t.string().optional(),
            "sizeLimitError": t.string().optional(),
            "authorizationError": t.string().optional(),
            "requestError": t.string().optional(),
            "headerError": t.string().optional(),
            "dateError": t.string().optional(),
            "queryError": t.string().optional(),
            "quotaError": t.string().optional(),
            "authenticationError": t.string().optional(),
            "distinctError": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__ErrorCodeIn"])
    types["GoogleAdsSearchads360V0Errors__ErrorCodeOut"] = t.struct(
        {
            "internalError": t.string().optional(),
            "dateRangeError": t.string().optional(),
            "sizeLimitError": t.string().optional(),
            "authorizationError": t.string().optional(),
            "requestError": t.string().optional(),
            "headerError": t.string().optional(),
            "dateError": t.string().optional(),
            "queryError": t.string().optional(),
            "quotaError": t.string().optional(),
            "authenticationError": t.string().optional(),
            "distinctError": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__ErrorCodeOut"])
    types["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "feedLabel": t.string().optional(),
            "campaignPriority": t.integer().optional(),
            "salesCountry": t.string().optional(),
            "useVehicleInventory": t.boolean().optional(),
            "enableLocal": t.boolean().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingIn"])
    types["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "feedLabel": t.string().optional(),
            "campaignPriority": t.integer().optional(),
            "salesCountry": t.string().optional(),
            "useVehicleInventory": t.boolean().optional(),
            "enableLocal": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources_Campaign_ShoppingSettingOut"])
    types["GoogleAdsSearchads360V0Common__ManualCpmIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpmIn"])
    types["GoogleAdsSearchads360V0Common__ManualCpmOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpmOut"])
    types["GoogleAdsSearchads360V0Resources__UserListIn"] = t.struct(
        {"name": t.string().optional(), "resourceName": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__UserListIn"])
    types["GoogleAdsSearchads360V0Resources__UserListOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__UserListOut"])
    types["GoogleAdsSearchads360V0Resources__ConversionActionIn"] = t.struct(
        {
            "clickThroughLookbackWindowDays": t.string().optional(),
            "primaryForGoal": t.boolean().optional(),
            "type": t.string().optional(),
            "attributionModelSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsIn"
                ]
            ).optional(),
            "valueSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsIn"
                ]
            ).optional(),
            "includeInClientAccountConversionsMetric": t.boolean().optional(),
            "category": t.string().optional(),
            "appId": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__ConversionActionIn"])
    types["GoogleAdsSearchads360V0Resources__ConversionActionOut"] = t.struct(
        {
            "clickThroughLookbackWindowDays": t.string().optional(),
            "creationTime": t.string().optional(),
            "primaryForGoal": t.boolean().optional(),
            "ownerCustomer": t.string().optional(),
            "type": t.string().optional(),
            "attributionModelSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettingsOut"
                ]
            ).optional(),
            "floodlightSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettingsOut"
                ]
            ).optional(),
            "valueSettings": t.proxy(
                renames[
                    "GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettingsOut"
                ]
            ).optional(),
            "includeInClientAccountConversionsMetric": t.boolean().optional(),
            "includeInConversionsMetric": t.boolean().optional(),
            "category": t.string().optional(),
            "id": t.string().optional(),
            "appId": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__ConversionActionOut"])
    types["GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn"] = t.struct(
        {
            "trigger": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ValueIn"]
            ).optional(),
            "details": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorDetailsIn"]
            ).optional(),
            "message": t.string().optional(),
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorLocationIn"]
            ).optional(),
            "errorCode": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorCodeIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__SearchAds360ErrorIn"])
    types["GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut"] = t.struct(
        {
            "trigger": t.proxy(
                renames["GoogleAdsSearchads360V0Common__ValueOut"]
            ).optional(),
            "details": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorDetailsOut"]
            ).optional(),
            "message": t.string().optional(),
            "location": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorLocationOut"]
            ).optional(),
            "errorCode": t.proxy(
                renames["GoogleAdsSearchads360V0Errors__ErrorCodeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__SearchAds360ErrorOut"])
    types["GoogleAdsSearchads360V0Common__MaximizeConversionsIn"] = t.struct(
        {
            "cpcBidFloorMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "targetCpaMicros": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MaximizeConversionsIn"])
    types["GoogleAdsSearchads360V0Common__MaximizeConversionsOut"] = t.struct(
        {
            "cpcBidFloorMicros": t.string().optional(),
            "cpcBidCeilingMicros": t.string().optional(),
            "targetCpaMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__MaximizeConversionsOut"])
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
    types["GoogleAdsSearchads360V0Common__EnhancedCpcIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__EnhancedCpcIn"])
    types["GoogleAdsSearchads360V0Common__EnhancedCpcOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__EnhancedCpcOut"])
    types["GoogleAdsSearchads360V0Common__LocationGroupInfoIn"] = t.struct(
        {
            "feedItemSets": t.array(t.string()).optional(),
            "geoTargetConstants": t.array(t.string()).optional(),
            "radiusUnits": t.string().optional(),
            "radius": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__LocationGroupInfoIn"])
    types["GoogleAdsSearchads360V0Common__LocationGroupInfoOut"] = t.struct(
        {
            "feedItemSets": t.array(t.string()).optional(),
            "geoTargetConstants": t.array(t.string()).optional(),
            "radiusUnits": t.string().optional(),
            "radius": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__LocationGroupInfoOut"])
    types["GoogleAdsSearchads360V0Resources__WebpageViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__WebpageViewIn"])
    types["GoogleAdsSearchads360V0Resources__WebpageViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__WebpageViewOut"])
    types["GoogleAdsSearchads360V0Resources__SearchAds360FieldIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldIn"])
    types["GoogleAdsSearchads360V0Resources__SearchAds360FieldOut"] = t.struct(
        {
            "isRepeated": t.boolean().optional(),
            "metrics": t.array(t.string()).optional(),
            "selectable": t.boolean().optional(),
            "enumValues": t.array(t.string()).optional(),
            "filterable": t.boolean().optional(),
            "typeUrl": t.string().optional(),
            "selectableWith": t.array(t.string()).optional(),
            "segments": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "attributeResources": t.array(t.string()).optional(),
            "sortable": t.boolean().optional(),
            "category": t.string().optional(),
            "dataType": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__SearchAds360FieldOut"])
    types["GoogleAdsSearchads360V0Common__SegmentsIn"] = t.struct(
        {
            "quarter": t.string().optional(),
            "conversionAction": t.string().optional(),
            "year": t.integer().optional(),
            "conversionActionName": t.string().optional(),
            "week": t.string().optional(),
            "conversionActionCategory": t.string().optional(),
            "dayOfWeek": t.string().optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordIn"]
            ).optional(),
            "date": t.string().optional(),
            "month": t.string().optional(),
            "device": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SegmentsIn"])
    types["GoogleAdsSearchads360V0Common__SegmentsOut"] = t.struct(
        {
            "quarter": t.string().optional(),
            "conversionAction": t.string().optional(),
            "year": t.integer().optional(),
            "conversionActionName": t.string().optional(),
            "week": t.string().optional(),
            "conversionActionCategory": t.string().optional(),
            "dayOfWeek": t.string().optional(),
            "keyword": t.proxy(
                renames["GoogleAdsSearchads360V0Common__KeywordOut"]
            ).optional(),
            "date": t.string().optional(),
            "month": t.string().optional(),
            "device": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__SegmentsOut"])
    types["GoogleAdsSearchads360V0Common__ManualCpcIn"] = t.struct(
        {"enhancedCpcEnabled": t.boolean().optional()}
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpcIn"])
    types["GoogleAdsSearchads360V0Common__ManualCpcOut"] = t.struct(
        {
            "enhancedCpcEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Common__ManualCpcOut"])
    types["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn"] = t.struct(
        {
            "retryDelay": t.string().optional(),
            "rateScope": t.string().optional(),
            "rateName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsIn"])
    types["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut"] = t.struct(
        {
            "retryDelay": t.string().optional(),
            "rateScope": t.string().optional(),
            "rateName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Errors__QuotaErrorDetailsOut"])
    types["GoogleAdsSearchads360V0Resources__CustomColumnIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomColumnIn"])
    types["GoogleAdsSearchads360V0Resources__CustomColumnOut"] = t.struct(
        {
            "id": t.string().optional(),
            "valueType": t.string().optional(),
            "resourceName": t.string().optional(),
            "referencesAttributes": t.boolean().optional(),
            "referencedSystemColumns": t.array(t.string()).optional(),
            "queryable": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "referencesMetrics": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__CustomColumnOut"])
    types["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseIn"] = t.struct(
        {
            "customColumnHeaders": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Services__CustomColumnHeaderIn"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Services__SearchAds360RowIn"])
            ).optional(),
            "fieldMask": t.string().optional(),
            "totalResultsCount": t.string().optional(),
            "summaryRow": t.proxy(
                renames["GoogleAdsSearchads360V0Services__SearchAds360RowIn"]
            ).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseIn"])
    types["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut"] = t.struct(
        {
            "customColumnHeaders": t.array(
                t.proxy(
                    renames["GoogleAdsSearchads360V0Services__CustomColumnHeaderOut"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleAdsSearchads360V0Services__SearchAds360RowOut"])
            ).optional(),
            "fieldMask": t.string().optional(),
            "totalResultsCount": t.string().optional(),
            "summaryRow": t.proxy(
                renames["GoogleAdsSearchads360V0Services__SearchAds360RowOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut"])
    types["GoogleAdsSearchads360V0Resources__GenderViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__GenderViewIn"])
    types["GoogleAdsSearchads360V0Resources__GenderViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__GenderViewOut"])
    types["GoogleAdsSearchads360V0Resources__LabelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "textLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TextLabelIn"]
            ).optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__LabelIn"])
    types["GoogleAdsSearchads360V0Resources__LabelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "status": t.string().optional(),
            "textLabel": t.proxy(
                renames["GoogleAdsSearchads360V0Common__TextLabelOut"]
            ).optional(),
            "id": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__LabelOut"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewIn"])
    types["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsSearchads360V0Resources__AdGroupAudienceViewOut"])

    functions = {}
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
    functions["customersSearchAds360Search"] = searchads360.post(
        "v0/customers/{customerId}/searchAds360:search",
        t.struct(
            {
                "customerId": t.string(),
                "returnTotalResultsCount": t.boolean().optional(),
                "query": t.string(),
                "summaryRowSetting": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="searchads360",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
