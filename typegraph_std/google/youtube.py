from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_youtube() -> Import:
    youtube = HTTPRuntime("https://youtube.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtube_1_ErrorResponse",
        "ChannelToStoreLinkDetailsIn": "_youtube_2_ChannelToStoreLinkDetailsIn",
        "ChannelToStoreLinkDetailsOut": "_youtube_3_ChannelToStoreLinkDetailsOut",
        "ThirdPartyLinkIn": "_youtube_4_ThirdPartyLinkIn",
        "ThirdPartyLinkOut": "_youtube_5_ThirdPartyLinkOut",
        "WatchSettingsIn": "_youtube_6_WatchSettingsIn",
        "WatchSettingsOut": "_youtube_7_WatchSettingsOut",
        "I18nLanguageSnippetIn": "_youtube_8_I18nLanguageSnippetIn",
        "I18nLanguageSnippetOut": "_youtube_9_I18nLanguageSnippetOut",
        "VideoMonetizationDetailsIn": "_youtube_10_VideoMonetizationDetailsIn",
        "VideoMonetizationDetailsOut": "_youtube_11_VideoMonetizationDetailsOut",
        "ThirdPartyLinkStatusIn": "_youtube_12_ThirdPartyLinkStatusIn",
        "ThirdPartyLinkStatusOut": "_youtube_13_ThirdPartyLinkStatusOut",
        "CuepointIn": "_youtube_14_CuepointIn",
        "CuepointOut": "_youtube_15_CuepointOut",
        "IngestionInfoIn": "_youtube_16_IngestionInfoIn",
        "IngestionInfoOut": "_youtube_17_IngestionInfoOut",
        "PlaylistItemContentDetailsIn": "_youtube_18_PlaylistItemContentDetailsIn",
        "PlaylistItemContentDetailsOut": "_youtube_19_PlaylistItemContentDetailsOut",
        "ActivityContentDetailsChannelItemIn": "_youtube_20_ActivityContentDetailsChannelItemIn",
        "ActivityContentDetailsChannelItemOut": "_youtube_21_ActivityContentDetailsChannelItemOut",
        "MembershipsLevelIn": "_youtube_22_MembershipsLevelIn",
        "MembershipsLevelOut": "_youtube_23_MembershipsLevelOut",
        "ChannelLocalizationIn": "_youtube_24_ChannelLocalizationIn",
        "ChannelLocalizationOut": "_youtube_25_ChannelLocalizationOut",
        "VideoListResponseIn": "_youtube_26_VideoListResponseIn",
        "VideoListResponseOut": "_youtube_27_VideoListResponseOut",
        "ChannelSectionLocalizationIn": "_youtube_28_ChannelSectionLocalizationIn",
        "ChannelSectionLocalizationOut": "_youtube_29_ChannelSectionLocalizationOut",
        "ChannelContentOwnerDetailsIn": "_youtube_30_ChannelContentOwnerDetailsIn",
        "ChannelContentOwnerDetailsOut": "_youtube_31_ChannelContentOwnerDetailsOut",
        "LiveBroadcastContentDetailsIn": "_youtube_32_LiveBroadcastContentDetailsIn",
        "LiveBroadcastContentDetailsOut": "_youtube_33_LiveBroadcastContentDetailsOut",
        "LiveBroadcastStatisticsIn": "_youtube_34_LiveBroadcastStatisticsIn",
        "LiveBroadcastStatisticsOut": "_youtube_35_LiveBroadcastStatisticsOut",
        "VideoIn": "_youtube_36_VideoIn",
        "VideoOut": "_youtube_37_VideoOut",
        "VideoAbuseReportSecondaryReasonIn": "_youtube_38_VideoAbuseReportSecondaryReasonIn",
        "VideoAbuseReportSecondaryReasonOut": "_youtube_39_VideoAbuseReportSecondaryReasonOut",
        "LiveChatMemberMilestoneChatDetailsIn": "_youtube_40_LiveChatMemberMilestoneChatDetailsIn",
        "LiveChatMemberMilestoneChatDetailsOut": "_youtube_41_LiveChatMemberMilestoneChatDetailsOut",
        "VideoSnippetIn": "_youtube_42_VideoSnippetIn",
        "VideoSnippetOut": "_youtube_43_VideoSnippetOut",
        "MembershipsDurationIn": "_youtube_44_MembershipsDurationIn",
        "MembershipsDurationOut": "_youtube_45_MembershipsDurationOut",
        "PlaylistIn": "_youtube_46_PlaylistIn",
        "PlaylistOut": "_youtube_47_PlaylistOut",
        "ActivityContentDetailsBulletinIn": "_youtube_48_ActivityContentDetailsBulletinIn",
        "ActivityContentDetailsBulletinOut": "_youtube_49_ActivityContentDetailsBulletinOut",
        "ActivityContentDetailsRecommendationIn": "_youtube_50_ActivityContentDetailsRecommendationIn",
        "ActivityContentDetailsRecommendationOut": "_youtube_51_ActivityContentDetailsRecommendationOut",
        "VideoFileDetailsAudioStreamIn": "_youtube_52_VideoFileDetailsAudioStreamIn",
        "VideoFileDetailsAudioStreamOut": "_youtube_53_VideoFileDetailsAudioStreamOut",
        "ChannelSectionSnippetIn": "_youtube_54_ChannelSectionSnippetIn",
        "ChannelSectionSnippetOut": "_youtube_55_ChannelSectionSnippetOut",
        "MembershipsDetailsIn": "_youtube_56_MembershipsDetailsIn",
        "MembershipsDetailsOut": "_youtube_57_MembershipsDetailsOut",
        "EntityIn": "_youtube_58_EntityIn",
        "EntityOut": "_youtube_59_EntityOut",
        "TestItemTestItemSnippetIn": "_youtube_60_TestItemTestItemSnippetIn",
        "TestItemTestItemSnippetOut": "_youtube_61_TestItemTestItemSnippetOut",
        "CommentThreadSnippetIn": "_youtube_62_CommentThreadSnippetIn",
        "CommentThreadSnippetOut": "_youtube_63_CommentThreadSnippetOut",
        "LiveChatSuperStickerDetailsIn": "_youtube_64_LiveChatSuperStickerDetailsIn",
        "LiveChatSuperStickerDetailsOut": "_youtube_65_LiveChatSuperStickerDetailsOut",
        "LiveChatNewSponsorDetailsIn": "_youtube_66_LiveChatNewSponsorDetailsIn",
        "LiveChatNewSponsorDetailsOut": "_youtube_67_LiveChatNewSponsorDetailsOut",
        "CommentThreadIn": "_youtube_68_CommentThreadIn",
        "CommentThreadOut": "_youtube_69_CommentThreadOut",
        "SearchResultIn": "_youtube_70_SearchResultIn",
        "SearchResultOut": "_youtube_71_SearchResultOut",
        "LiveChatTextMessageDetailsIn": "_youtube_72_LiveChatTextMessageDetailsIn",
        "LiveChatTextMessageDetailsOut": "_youtube_73_LiveChatTextMessageDetailsOut",
        "PlaylistStatusIn": "_youtube_74_PlaylistStatusIn",
        "PlaylistStatusOut": "_youtube_75_PlaylistStatusOut",
        "ActivityContentDetailsPromotedItemIn": "_youtube_76_ActivityContentDetailsPromotedItemIn",
        "ActivityContentDetailsPromotedItemOut": "_youtube_77_ActivityContentDetailsPromotedItemOut",
        "ContentRatingIn": "_youtube_78_ContentRatingIn",
        "ContentRatingOut": "_youtube_79_ContentRatingOut",
        "CaptionListResponseIn": "_youtube_80_CaptionListResponseIn",
        "CaptionListResponseOut": "_youtube_81_CaptionListResponseOut",
        "LiveChatGiftMembershipReceivedDetailsIn": "_youtube_82_LiveChatGiftMembershipReceivedDetailsIn",
        "LiveChatGiftMembershipReceivedDetailsOut": "_youtube_83_LiveChatGiftMembershipReceivedDetailsOut",
        "CommentSnippetAuthorChannelIdIn": "_youtube_84_CommentSnippetAuthorChannelIdIn",
        "CommentSnippetAuthorChannelIdOut": "_youtube_85_CommentSnippetAuthorChannelIdOut",
        "ChannelSnippetIn": "_youtube_86_ChannelSnippetIn",
        "ChannelSnippetOut": "_youtube_87_ChannelSnippetOut",
        "CdnSettingsIn": "_youtube_88_CdnSettingsIn",
        "CdnSettingsOut": "_youtube_89_CdnSettingsOut",
        "ChannelSectionListResponseIn": "_youtube_90_ChannelSectionListResponseIn",
        "ChannelSectionListResponseOut": "_youtube_91_ChannelSectionListResponseOut",
        "PlaylistItemStatusIn": "_youtube_92_PlaylistItemStatusIn",
        "PlaylistItemStatusOut": "_youtube_93_PlaylistItemStatusOut",
        "SuperChatEventIn": "_youtube_94_SuperChatEventIn",
        "SuperChatEventOut": "_youtube_95_SuperChatEventOut",
        "SearchListResponseIn": "_youtube_96_SearchListResponseIn",
        "SearchListResponseOut": "_youtube_97_SearchListResponseOut",
        "PlaylistItemSnippetIn": "_youtube_98_PlaylistItemSnippetIn",
        "PlaylistItemSnippetOut": "_youtube_99_PlaylistItemSnippetOut",
        "ChannelTopicDetailsIn": "_youtube_100_ChannelTopicDetailsIn",
        "ChannelTopicDetailsOut": "_youtube_101_ChannelTopicDetailsOut",
        "LiveChatUserBannedMessageDetailsIn": "_youtube_102_LiveChatUserBannedMessageDetailsIn",
        "LiveChatUserBannedMessageDetailsOut": "_youtube_103_LiveChatUserBannedMessageDetailsOut",
        "ThirdPartyLinkSnippetIn": "_youtube_104_ThirdPartyLinkSnippetIn",
        "ThirdPartyLinkSnippetOut": "_youtube_105_ThirdPartyLinkSnippetOut",
        "LiveChatMembershipGiftingDetailsIn": "_youtube_106_LiveChatMembershipGiftingDetailsIn",
        "LiveChatMembershipGiftingDetailsOut": "_youtube_107_LiveChatMembershipGiftingDetailsOut",
        "SubscriptionSubscriberSnippetIn": "_youtube_108_SubscriptionSubscriberSnippetIn",
        "SubscriptionSubscriberSnippetOut": "_youtube_109_SubscriptionSubscriberSnippetOut",
        "VideoContentDetailsIn": "_youtube_110_VideoContentDetailsIn",
        "VideoContentDetailsOut": "_youtube_111_VideoContentDetailsOut",
        "I18nRegionSnippetIn": "_youtube_112_I18nRegionSnippetIn",
        "I18nRegionSnippetOut": "_youtube_113_I18nRegionSnippetOut",
        "LiveChatMessageAuthorDetailsIn": "_youtube_114_LiveChatMessageAuthorDetailsIn",
        "LiveChatMessageAuthorDetailsOut": "_youtube_115_LiveChatMessageAuthorDetailsOut",
        "VideoCategoryListResponseIn": "_youtube_116_VideoCategoryListResponseIn",
        "VideoCategoryListResponseOut": "_youtube_117_VideoCategoryListResponseOut",
        "PlaylistItemIn": "_youtube_118_PlaylistItemIn",
        "PlaylistItemOut": "_youtube_119_PlaylistItemOut",
        "CommentThreadRepliesIn": "_youtube_120_CommentThreadRepliesIn",
        "CommentThreadRepliesOut": "_youtube_121_CommentThreadRepliesOut",
        "LiveChatMessageListResponseIn": "_youtube_122_LiveChatMessageListResponseIn",
        "LiveChatMessageListResponseOut": "_youtube_123_LiveChatMessageListResponseOut",
        "ActivityContentDetailsSocialIn": "_youtube_124_ActivityContentDetailsSocialIn",
        "ActivityContentDetailsSocialOut": "_youtube_125_ActivityContentDetailsSocialOut",
        "I18nRegionIn": "_youtube_126_I18nRegionIn",
        "I18nRegionOut": "_youtube_127_I18nRegionOut",
        "VideoTopicDetailsIn": "_youtube_128_VideoTopicDetailsIn",
        "VideoTopicDetailsOut": "_youtube_129_VideoTopicDetailsOut",
        "PlaylistListResponseIn": "_youtube_130_PlaylistListResponseIn",
        "PlaylistListResponseOut": "_youtube_131_PlaylistListResponseOut",
        "InvideoBrandingIn": "_youtube_132_InvideoBrandingIn",
        "InvideoBrandingOut": "_youtube_133_InvideoBrandingOut",
        "CommentIn": "_youtube_134_CommentIn",
        "CommentOut": "_youtube_135_CommentOut",
        "RelatedEntityIn": "_youtube_136_RelatedEntityIn",
        "RelatedEntityOut": "_youtube_137_RelatedEntityOut",
        "SuperChatEventSnippetIn": "_youtube_138_SuperChatEventSnippetIn",
        "SuperChatEventSnippetOut": "_youtube_139_SuperChatEventSnippetOut",
        "AccessPolicyIn": "_youtube_140_AccessPolicyIn",
        "AccessPolicyOut": "_youtube_141_AccessPolicyOut",
        "VideoStatusIn": "_youtube_142_VideoStatusIn",
        "VideoStatusOut": "_youtube_143_VideoStatusOut",
        "LiveBroadcastIn": "_youtube_144_LiveBroadcastIn",
        "LiveBroadcastOut": "_youtube_145_LiveBroadcastOut",
        "VideoProcessingDetailsIn": "_youtube_146_VideoProcessingDetailsIn",
        "VideoProcessingDetailsOut": "_youtube_147_VideoProcessingDetailsOut",
        "ActivityContentDetailsIn": "_youtube_148_ActivityContentDetailsIn",
        "ActivityContentDetailsOut": "_youtube_149_ActivityContentDetailsOut",
        "VideoAbuseReportIn": "_youtube_150_VideoAbuseReportIn",
        "VideoAbuseReportOut": "_youtube_151_VideoAbuseReportOut",
        "VideoProcessingDetailsProcessingProgressIn": "_youtube_152_VideoProcessingDetailsProcessingProgressIn",
        "VideoProcessingDetailsProcessingProgressOut": "_youtube_153_VideoProcessingDetailsProcessingProgressOut",
        "LiveChatMessageSnippetIn": "_youtube_154_LiveChatMessageSnippetIn",
        "LiveChatMessageSnippetOut": "_youtube_155_LiveChatMessageSnippetOut",
        "VideoSuggestionsTagSuggestionIn": "_youtube_156_VideoSuggestionsTagSuggestionIn",
        "VideoSuggestionsTagSuggestionOut": "_youtube_157_VideoSuggestionsTagSuggestionOut",
        "I18nLanguageListResponseIn": "_youtube_158_I18nLanguageListResponseIn",
        "I18nLanguageListResponseOut": "_youtube_159_I18nLanguageListResponseOut",
        "InvideoTimingIn": "_youtube_160_InvideoTimingIn",
        "InvideoTimingOut": "_youtube_161_InvideoTimingOut",
        "VideoAbuseReportReasonSnippetIn": "_youtube_162_VideoAbuseReportReasonSnippetIn",
        "VideoAbuseReportReasonSnippetOut": "_youtube_163_VideoAbuseReportReasonSnippetOut",
        "CommentSnippetIn": "_youtube_164_CommentSnippetIn",
        "CommentSnippetOut": "_youtube_165_CommentSnippetOut",
        "VideoAbuseReportReasonIn": "_youtube_166_VideoAbuseReportReasonIn",
        "VideoAbuseReportReasonOut": "_youtube_167_VideoAbuseReportReasonOut",
        "LanguageTagIn": "_youtube_168_LanguageTagIn",
        "LanguageTagOut": "_youtube_169_LanguageTagOut",
        "ChannelStatisticsIn": "_youtube_170_ChannelStatisticsIn",
        "ChannelStatisticsOut": "_youtube_171_ChannelStatisticsOut",
        "VideoStatisticsIn": "_youtube_172_VideoStatisticsIn",
        "VideoStatisticsOut": "_youtube_173_VideoStatisticsOut",
        "ChannelSettingsIn": "_youtube_174_ChannelSettingsIn",
        "ChannelSettingsOut": "_youtube_175_ChannelSettingsOut",
        "LiveChatBanIn": "_youtube_176_LiveChatBanIn",
        "LiveChatBanOut": "_youtube_177_LiveChatBanOut",
        "VideoLocalizationIn": "_youtube_178_VideoLocalizationIn",
        "VideoLocalizationOut": "_youtube_179_VideoLocalizationOut",
        "ChannelIn": "_youtube_180_ChannelIn",
        "ChannelOut": "_youtube_181_ChannelOut",
        "CommentThreadListResponseIn": "_youtube_182_CommentThreadListResponseIn",
        "CommentThreadListResponseOut": "_youtube_183_CommentThreadListResponseOut",
        "LiveStreamContentDetailsIn": "_youtube_184_LiveStreamContentDetailsIn",
        "LiveStreamContentDetailsOut": "_youtube_185_LiveStreamContentDetailsOut",
        "CaptionSnippetIn": "_youtube_186_CaptionSnippetIn",
        "CaptionSnippetOut": "_youtube_187_CaptionSnippetOut",
        "VideoFileDetailsIn": "_youtube_188_VideoFileDetailsIn",
        "VideoFileDetailsOut": "_youtube_189_VideoFileDetailsOut",
        "VideoLiveStreamingDetailsIn": "_youtube_190_VideoLiveStreamingDetailsIn",
        "VideoLiveStreamingDetailsOut": "_youtube_191_VideoLiveStreamingDetailsOut",
        "ActivityIn": "_youtube_192_ActivityIn",
        "ActivityOut": "_youtube_193_ActivityOut",
        "VideoCategoryIn": "_youtube_194_VideoCategoryIn",
        "VideoCategoryOut": "_youtube_195_VideoCategoryOut",
        "MembershipsLevelSnippetIn": "_youtube_196_MembershipsLevelSnippetIn",
        "MembershipsLevelSnippetOut": "_youtube_197_MembershipsLevelSnippetOut",
        "ChannelBrandingSettingsIn": "_youtube_198_ChannelBrandingSettingsIn",
        "ChannelBrandingSettingsOut": "_youtube_199_ChannelBrandingSettingsOut",
        "MemberIn": "_youtube_200_MemberIn",
        "MemberOut": "_youtube_201_MemberOut",
        "PlaylistSnippetIn": "_youtube_202_PlaylistSnippetIn",
        "PlaylistSnippetOut": "_youtube_203_PlaylistSnippetOut",
        "ThumbnailSetResponseIn": "_youtube_204_ThumbnailSetResponseIn",
        "ThumbnailSetResponseOut": "_youtube_205_ThumbnailSetResponseOut",
        "LevelDetailsIn": "_youtube_206_LevelDetailsIn",
        "LevelDetailsOut": "_youtube_207_LevelDetailsOut",
        "ChannelSectionIn": "_youtube_208_ChannelSectionIn",
        "ChannelSectionOut": "_youtube_209_ChannelSectionOut",
        "LiveChatModeratorListResponseIn": "_youtube_210_LiveChatModeratorListResponseIn",
        "LiveChatModeratorListResponseOut": "_youtube_211_LiveChatModeratorListResponseOut",
        "PlaylistLocalizationIn": "_youtube_212_PlaylistLocalizationIn",
        "PlaylistLocalizationOut": "_youtube_213_PlaylistLocalizationOut",
        "LiveStreamStatusIn": "_youtube_214_LiveStreamStatusIn",
        "LiveStreamStatusOut": "_youtube_215_LiveStreamStatusOut",
        "ActivitySnippetIn": "_youtube_216_ActivitySnippetIn",
        "ActivitySnippetOut": "_youtube_217_ActivitySnippetOut",
        "TestItemIn": "_youtube_218_TestItemIn",
        "TestItemOut": "_youtube_219_TestItemOut",
        "LocalizedStringIn": "_youtube_220_LocalizedStringIn",
        "LocalizedStringOut": "_youtube_221_LocalizedStringOut",
        "ChannelStatusIn": "_youtube_222_ChannelStatusIn",
        "ChannelStatusOut": "_youtube_223_ChannelStatusOut",
        "ChannelConversionPingIn": "_youtube_224_ChannelConversionPingIn",
        "ChannelConversionPingOut": "_youtube_225_ChannelConversionPingOut",
        "VideoFileDetailsVideoStreamIn": "_youtube_226_VideoFileDetailsVideoStreamIn",
        "VideoFileDetailsVideoStreamOut": "_youtube_227_VideoFileDetailsVideoStreamOut",
        "MonitorStreamInfoIn": "_youtube_228_MonitorStreamInfoIn",
        "MonitorStreamInfoOut": "_youtube_229_MonitorStreamInfoOut",
        "VideoGetRatingResponseIn": "_youtube_230_VideoGetRatingResponseIn",
        "VideoGetRatingResponseOut": "_youtube_231_VideoGetRatingResponseOut",
        "ActivityContentDetailsLikeIn": "_youtube_232_ActivityContentDetailsLikeIn",
        "ActivityContentDetailsLikeOut": "_youtube_233_ActivityContentDetailsLikeOut",
        "ActivityContentDetailsSubscriptionIn": "_youtube_234_ActivityContentDetailsSubscriptionIn",
        "ActivityContentDetailsSubscriptionOut": "_youtube_235_ActivityContentDetailsSubscriptionOut",
        "LiveChatMessageRetractedDetailsIn": "_youtube_236_LiveChatMessageRetractedDetailsIn",
        "LiveChatMessageRetractedDetailsOut": "_youtube_237_LiveChatMessageRetractedDetailsOut",
        "LiveChatModeratorSnippetIn": "_youtube_238_LiveChatModeratorSnippetIn",
        "LiveChatModeratorSnippetOut": "_youtube_239_LiveChatModeratorSnippetOut",
        "ImageSettingsIn": "_youtube_240_ImageSettingsIn",
        "ImageSettingsOut": "_youtube_241_ImageSettingsOut",
        "LiveStreamSnippetIn": "_youtube_242_LiveStreamSnippetIn",
        "LiveStreamSnippetOut": "_youtube_243_LiveStreamSnippetOut",
        "LiveStreamIn": "_youtube_244_LiveStreamIn",
        "LiveStreamOut": "_youtube_245_LiveStreamOut",
        "ChannelProfileDetailsIn": "_youtube_246_ChannelProfileDetailsIn",
        "ChannelProfileDetailsOut": "_youtube_247_ChannelProfileDetailsOut",
        "LiveChatSuperChatDetailsIn": "_youtube_248_LiveChatSuperChatDetailsIn",
        "LiveChatSuperChatDetailsOut": "_youtube_249_LiveChatSuperChatDetailsOut",
        "MembershipsLevelListResponseIn": "_youtube_250_MembershipsLevelListResponseIn",
        "MembershipsLevelListResponseOut": "_youtube_251_MembershipsLevelListResponseOut",
        "MembershipsDurationAtLevelIn": "_youtube_252_MembershipsDurationAtLevelIn",
        "MembershipsDurationAtLevelOut": "_youtube_253_MembershipsDurationAtLevelOut",
        "LiveChatMessageDeletedDetailsIn": "_youtube_254_LiveChatMessageDeletedDetailsIn",
        "LiveChatMessageDeletedDetailsOut": "_youtube_255_LiveChatMessageDeletedDetailsOut",
        "LiveBroadcastSnippetIn": "_youtube_256_LiveBroadcastSnippetIn",
        "LiveBroadcastSnippetOut": "_youtube_257_LiveBroadcastSnippetOut",
        "ChannelListResponseIn": "_youtube_258_ChannelListResponseIn",
        "ChannelListResponseOut": "_youtube_259_ChannelListResponseOut",
        "ResourceIdIn": "_youtube_260_ResourceIdIn",
        "ResourceIdOut": "_youtube_261_ResourceIdOut",
        "LocalizedPropertyIn": "_youtube_262_LocalizedPropertyIn",
        "LocalizedPropertyOut": "_youtube_263_LocalizedPropertyOut",
        "VideoProjectDetailsIn": "_youtube_264_VideoProjectDetailsIn",
        "VideoProjectDetailsOut": "_youtube_265_VideoProjectDetailsOut",
        "PlaylistItemListResponseIn": "_youtube_266_PlaylistItemListResponseIn",
        "PlaylistItemListResponseOut": "_youtube_267_PlaylistItemListResponseOut",
        "MemberSnippetIn": "_youtube_268_MemberSnippetIn",
        "MemberSnippetOut": "_youtube_269_MemberSnippetOut",
        "LiveChatModeratorIn": "_youtube_270_LiveChatModeratorIn",
        "LiveChatModeratorOut": "_youtube_271_LiveChatModeratorOut",
        "MemberListResponseIn": "_youtube_272_MemberListResponseIn",
        "MemberListResponseOut": "_youtube_273_MemberListResponseOut",
        "PageInfoIn": "_youtube_274_PageInfoIn",
        "PageInfoOut": "_youtube_275_PageInfoOut",
        "TokenPaginationIn": "_youtube_276_TokenPaginationIn",
        "TokenPaginationOut": "_youtube_277_TokenPaginationOut",
        "SearchResultSnippetIn": "_youtube_278_SearchResultSnippetIn",
        "SearchResultSnippetOut": "_youtube_279_SearchResultSnippetOut",
        "ChannelBannerResourceIn": "_youtube_280_ChannelBannerResourceIn",
        "ChannelBannerResourceOut": "_youtube_281_ChannelBannerResourceOut",
        "LiveStreamHealthStatusIn": "_youtube_282_LiveStreamHealthStatusIn",
        "LiveStreamHealthStatusOut": "_youtube_283_LiveStreamHealthStatusOut",
        "ThumbnailDetailsIn": "_youtube_284_ThumbnailDetailsIn",
        "ThumbnailDetailsOut": "_youtube_285_ThumbnailDetailsOut",
        "I18nRegionListResponseIn": "_youtube_286_I18nRegionListResponseIn",
        "I18nRegionListResponseOut": "_youtube_287_I18nRegionListResponseOut",
        "PropertyValueIn": "_youtube_288_PropertyValueIn",
        "PropertyValueOut": "_youtube_289_PropertyValueOut",
        "AbuseReportIn": "_youtube_290_AbuseReportIn",
        "AbuseReportOut": "_youtube_291_AbuseReportOut",
        "LiveChatFanFundingEventDetailsIn": "_youtube_292_LiveChatFanFundingEventDetailsIn",
        "LiveChatFanFundingEventDetailsOut": "_youtube_293_LiveChatFanFundingEventDetailsOut",
        "ChannelAuditDetailsIn": "_youtube_294_ChannelAuditDetailsIn",
        "ChannelAuditDetailsOut": "_youtube_295_ChannelAuditDetailsOut",
        "CommentListResponseIn": "_youtube_296_CommentListResponseIn",
        "CommentListResponseOut": "_youtube_297_CommentListResponseOut",
        "SubscriptionSnippetIn": "_youtube_298_SubscriptionSnippetIn",
        "SubscriptionSnippetOut": "_youtube_299_SubscriptionSnippetOut",
        "VideoRecordingDetailsIn": "_youtube_300_VideoRecordingDetailsIn",
        "VideoRecordingDetailsOut": "_youtube_301_VideoRecordingDetailsOut",
        "PlaylistPlayerIn": "_youtube_302_PlaylistPlayerIn",
        "PlaylistPlayerOut": "_youtube_303_PlaylistPlayerOut",
        "ChannelContentDetailsIn": "_youtube_304_ChannelContentDetailsIn",
        "ChannelContentDetailsOut": "_youtube_305_ChannelContentDetailsOut",
        "LiveStreamConfigurationIssueIn": "_youtube_306_LiveStreamConfigurationIssueIn",
        "LiveStreamConfigurationIssueOut": "_youtube_307_LiveStreamConfigurationIssueOut",
        "ActivityContentDetailsCommentIn": "_youtube_308_ActivityContentDetailsCommentIn",
        "ActivityContentDetailsCommentOut": "_youtube_309_ActivityContentDetailsCommentOut",
        "ThirdPartyLinkListResponseIn": "_youtube_310_ThirdPartyLinkListResponseIn",
        "ThirdPartyLinkListResponseOut": "_youtube_311_ThirdPartyLinkListResponseOut",
        "SubscriptionContentDetailsIn": "_youtube_312_SubscriptionContentDetailsIn",
        "SubscriptionContentDetailsOut": "_youtube_313_SubscriptionContentDetailsOut",
        "SubscriptionListResponseIn": "_youtube_314_SubscriptionListResponseIn",
        "SubscriptionListResponseOut": "_youtube_315_SubscriptionListResponseOut",
        "AbuseTypeIn": "_youtube_316_AbuseTypeIn",
        "AbuseTypeOut": "_youtube_317_AbuseTypeOut",
        "ActivityContentDetailsPlaylistItemIn": "_youtube_318_ActivityContentDetailsPlaylistItemIn",
        "ActivityContentDetailsPlaylistItemOut": "_youtube_319_ActivityContentDetailsPlaylistItemOut",
        "GeoPointIn": "_youtube_320_GeoPointIn",
        "GeoPointOut": "_youtube_321_GeoPointOut",
        "SuperStickerMetadataIn": "_youtube_322_SuperStickerMetadataIn",
        "SuperStickerMetadataOut": "_youtube_323_SuperStickerMetadataOut",
        "VideoPlayerIn": "_youtube_324_VideoPlayerIn",
        "VideoPlayerOut": "_youtube_325_VideoPlayerOut",
        "LiveBroadcastListResponseIn": "_youtube_326_LiveBroadcastListResponseIn",
        "LiveBroadcastListResponseOut": "_youtube_327_LiveBroadcastListResponseOut",
        "I18nLanguageIn": "_youtube_328_I18nLanguageIn",
        "I18nLanguageOut": "_youtube_329_I18nLanguageOut",
        "ChannelSectionTargetingIn": "_youtube_330_ChannelSectionTargetingIn",
        "ChannelSectionTargetingOut": "_youtube_331_ChannelSectionTargetingOut",
        "LiveChatMessageIn": "_youtube_332_LiveChatMessageIn",
        "LiveChatMessageOut": "_youtube_333_LiveChatMessageOut",
        "VideoAgeGatingIn": "_youtube_334_VideoAgeGatingIn",
        "VideoAgeGatingOut": "_youtube_335_VideoAgeGatingOut",
        "VideoContentDetailsRegionRestrictionIn": "_youtube_336_VideoContentDetailsRegionRestrictionIn",
        "VideoContentDetailsRegionRestrictionOut": "_youtube_337_VideoContentDetailsRegionRestrictionOut",
        "SubscriptionIn": "_youtube_338_SubscriptionIn",
        "SubscriptionOut": "_youtube_339_SubscriptionOut",
        "PlaylistContentDetailsIn": "_youtube_340_PlaylistContentDetailsIn",
        "PlaylistContentDetailsOut": "_youtube_341_PlaylistContentDetailsOut",
        "VideoAbuseReportReasonListResponseIn": "_youtube_342_VideoAbuseReportReasonListResponseIn",
        "VideoAbuseReportReasonListResponseOut": "_youtube_343_VideoAbuseReportReasonListResponseOut",
        "VideoCategorySnippetIn": "_youtube_344_VideoCategorySnippetIn",
        "VideoCategorySnippetOut": "_youtube_345_VideoCategorySnippetOut",
        "ActivityContentDetailsUploadIn": "_youtube_346_ActivityContentDetailsUploadIn",
        "ActivityContentDetailsUploadOut": "_youtube_347_ActivityContentDetailsUploadOut",
        "VideoRatingIn": "_youtube_348_VideoRatingIn",
        "VideoRatingOut": "_youtube_349_VideoRatingOut",
        "VideoSuggestionsIn": "_youtube_350_VideoSuggestionsIn",
        "VideoSuggestionsOut": "_youtube_351_VideoSuggestionsOut",
        "ActivityListResponseIn": "_youtube_352_ActivityListResponseIn",
        "ActivityListResponseOut": "_youtube_353_ActivityListResponseOut",
        "LiveChatBanSnippetIn": "_youtube_354_LiveChatBanSnippetIn",
        "LiveChatBanSnippetOut": "_youtube_355_LiveChatBanSnippetOut",
        "ActivityContentDetailsFavoriteIn": "_youtube_356_ActivityContentDetailsFavoriteIn",
        "ActivityContentDetailsFavoriteOut": "_youtube_357_ActivityContentDetailsFavoriteOut",
        "LiveBroadcastStatusIn": "_youtube_358_LiveBroadcastStatusIn",
        "LiveBroadcastStatusOut": "_youtube_359_LiveBroadcastStatusOut",
        "ThumbnailIn": "_youtube_360_ThumbnailIn",
        "ThumbnailOut": "_youtube_361_ThumbnailOut",
        "ChannelSectionContentDetailsIn": "_youtube_362_ChannelSectionContentDetailsIn",
        "ChannelSectionContentDetailsOut": "_youtube_363_ChannelSectionContentDetailsOut",
        "LiveStreamListResponseIn": "_youtube_364_LiveStreamListResponseIn",
        "LiveStreamListResponseOut": "_youtube_365_LiveStreamListResponseOut",
        "ChannelConversionPingsIn": "_youtube_366_ChannelConversionPingsIn",
        "ChannelConversionPingsOut": "_youtube_367_ChannelConversionPingsOut",
        "InvideoPositionIn": "_youtube_368_InvideoPositionIn",
        "InvideoPositionOut": "_youtube_369_InvideoPositionOut",
        "CaptionIn": "_youtube_370_CaptionIn",
        "CaptionOut": "_youtube_371_CaptionOut",
        "SuperChatEventListResponseIn": "_youtube_372_SuperChatEventListResponseIn",
        "SuperChatEventListResponseOut": "_youtube_373_SuperChatEventListResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ChannelToStoreLinkDetailsIn"] = t.struct(
        {
            "storeUrl": t.string().optional(),
            "storeName": t.string().optional(),
            "merchantId": t.string().optional(),
        }
    ).named(renames["ChannelToStoreLinkDetailsIn"])
    types["ChannelToStoreLinkDetailsOut"] = t.struct(
        {
            "storeUrl": t.string().optional(),
            "storeName": t.string().optional(),
            "merchantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelToStoreLinkDetailsOut"])
    types["ThirdPartyLinkIn"] = t.struct(
        {
            "linkingToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["ThirdPartyLinkStatusIn"]).optional(),
            "snippet": t.proxy(renames["ThirdPartyLinkSnippetIn"]).optional(),
        }
    ).named(renames["ThirdPartyLinkIn"])
    types["ThirdPartyLinkOut"] = t.struct(
        {
            "linkingToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["ThirdPartyLinkStatusOut"]).optional(),
            "snippet": t.proxy(renames["ThirdPartyLinkSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyLinkOut"])
    types["WatchSettingsIn"] = t.struct(
        {
            "featuredPlaylistId": t.string().optional(),
            "textColor": t.string().optional(),
            "backgroundColor": t.string().optional(),
        }
    ).named(renames["WatchSettingsIn"])
    types["WatchSettingsOut"] = t.struct(
        {
            "featuredPlaylistId": t.string().optional(),
            "textColor": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchSettingsOut"])
    types["I18nLanguageSnippetIn"] = t.struct(
        {"hl": t.string().optional(), "name": t.string().optional()}
    ).named(renames["I18nLanguageSnippetIn"])
    types["I18nLanguageSnippetOut"] = t.struct(
        {
            "hl": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nLanguageSnippetOut"])
    types["VideoMonetizationDetailsIn"] = t.struct(
        {"access": t.proxy(renames["AccessPolicyIn"]).optional()}
    ).named(renames["VideoMonetizationDetailsIn"])
    types["VideoMonetizationDetailsOut"] = t.struct(
        {
            "access": t.proxy(renames["AccessPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoMonetizationDetailsOut"])
    types["ThirdPartyLinkStatusIn"] = t.struct({"linkStatus": t.string()}).named(
        renames["ThirdPartyLinkStatusIn"]
    )
    types["ThirdPartyLinkStatusOut"] = t.struct(
        {
            "linkStatus": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyLinkStatusOut"])
    types["CuepointIn"] = t.struct(
        {
            "durationSecs": t.integer().optional(),
            "id": t.string().optional(),
            "insertionOffsetTimeMs": t.string().optional(),
            "etag": t.string(),
            "cueType": t.string(),
            "walltimeMs": t.string().optional(),
        }
    ).named(renames["CuepointIn"])
    types["CuepointOut"] = t.struct(
        {
            "durationSecs": t.integer().optional(),
            "id": t.string().optional(),
            "insertionOffsetTimeMs": t.string().optional(),
            "etag": t.string(),
            "cueType": t.string(),
            "walltimeMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CuepointOut"])
    types["IngestionInfoIn"] = t.struct(
        {
            "streamName": t.string().optional(),
            "ingestionAddress": t.string().optional(),
            "rtmpsIngestionAddress": t.string().optional(),
            "rtmpsBackupIngestionAddress": t.string().optional(),
            "backupIngestionAddress": t.string().optional(),
        }
    ).named(renames["IngestionInfoIn"])
    types["IngestionInfoOut"] = t.struct(
        {
            "streamName": t.string().optional(),
            "ingestionAddress": t.string().optional(),
            "rtmpsIngestionAddress": t.string().optional(),
            "rtmpsBackupIngestionAddress": t.string().optional(),
            "backupIngestionAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngestionInfoOut"])
    types["PlaylistItemContentDetailsIn"] = t.struct(
        {
            "videoId": t.string().optional(),
            "videoPublishedAt": t.string().optional(),
            "startAt": t.string().optional(),
            "note": t.string().optional(),
            "endAt": t.string().optional(),
        }
    ).named(renames["PlaylistItemContentDetailsIn"])
    types["PlaylistItemContentDetailsOut"] = t.struct(
        {
            "videoId": t.string().optional(),
            "videoPublishedAt": t.string().optional(),
            "startAt": t.string().optional(),
            "note": t.string().optional(),
            "endAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemContentDetailsOut"])
    types["ActivityContentDetailsChannelItemIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsChannelItemIn"])
    types["ActivityContentDetailsChannelItemOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsChannelItemOut"])
    types["MembershipsLevelIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["MembershipsLevelSnippetIn"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["MembershipsLevelIn"])
    types["MembershipsLevelOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["MembershipsLevelSnippetOut"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsLevelOut"])
    types["ChannelLocalizationIn"] = t.struct(
        {"description": t.string().optional(), "title": t.string().optional()}
    ).named(renames["ChannelLocalizationIn"])
    types["ChannelLocalizationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelLocalizationOut"])
    types["VideoListResponseIn"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoIn"])),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "prevPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
        }
    ).named(renames["VideoListResponseIn"])
    types["VideoListResponseOut"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoOut"])),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "prevPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoListResponseOut"])
    types["ChannelSectionLocalizationIn"] = t.struct(
        {"title": t.string().optional()}
    ).named(renames["ChannelSectionLocalizationIn"])
    types["ChannelSectionLocalizationOut"] = t.struct(
        {
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionLocalizationOut"])
    types["ChannelContentOwnerDetailsIn"] = t.struct(
        {"timeLinked": t.string().optional(), "contentOwner": t.string().optional()}
    ).named(renames["ChannelContentOwnerDetailsIn"])
    types["ChannelContentOwnerDetailsOut"] = t.struct(
        {
            "timeLinked": t.string().optional(),
            "contentOwner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelContentOwnerDetailsOut"])
    types["LiveBroadcastContentDetailsIn"] = t.struct(
        {
            "mesh": t.string().optional(),
            "enableDvr": t.boolean().optional(),
            "enableContentEncryption": t.boolean().optional(),
            "boundStreamId": t.string().optional(),
            "enableClosedCaptions": t.boolean().optional(),
            "enableEmbed": t.boolean().optional(),
            "closedCaptionsType": t.string(),
            "startWithSlate": t.boolean().optional(),
            "boundStreamLastUpdateTimeMs": t.string().optional(),
            "recordFromStart": t.boolean().optional(),
            "monitorStream": t.proxy(renames["MonitorStreamInfoIn"]).optional(),
            "latencyPreference": t.string().optional(),
            "enableAutoStop": t.boolean().optional(),
            "projection": t.string().optional(),
            "enableAutoStart": t.boolean().optional(),
            "stereoLayout": t.string().optional(),
            "enableLowLatency": t.boolean().optional(),
        }
    ).named(renames["LiveBroadcastContentDetailsIn"])
    types["LiveBroadcastContentDetailsOut"] = t.struct(
        {
            "mesh": t.string().optional(),
            "enableDvr": t.boolean().optional(),
            "enableContentEncryption": t.boolean().optional(),
            "boundStreamId": t.string().optional(),
            "enableClosedCaptions": t.boolean().optional(),
            "enableEmbed": t.boolean().optional(),
            "closedCaptionsType": t.string(),
            "startWithSlate": t.boolean().optional(),
            "boundStreamLastUpdateTimeMs": t.string().optional(),
            "recordFromStart": t.boolean().optional(),
            "monitorStream": t.proxy(renames["MonitorStreamInfoOut"]).optional(),
            "latencyPreference": t.string().optional(),
            "enableAutoStop": t.boolean().optional(),
            "projection": t.string().optional(),
            "enableAutoStart": t.boolean().optional(),
            "stereoLayout": t.string().optional(),
            "enableLowLatency": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastContentDetailsOut"])
    types["LiveBroadcastStatisticsIn"] = t.struct(
        {"concurrentViewers": t.string().optional()}
    ).named(renames["LiveBroadcastStatisticsIn"])
    types["LiveBroadcastStatisticsOut"] = t.struct(
        {
            "concurrentViewers": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastStatisticsOut"])
    types["VideoIn"] = t.struct(
        {
            "processingDetails": t.proxy(
                renames["VideoProcessingDetailsIn"]
            ).optional(),
            "monetizationDetails": t.proxy(
                renames["VideoMonetizationDetailsIn"]
            ).optional(),
            "player": t.proxy(renames["VideoPlayerIn"]).optional(),
            "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
            "kind": t.string().optional(),
            "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
            "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
            "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
            "status": t.proxy(renames["VideoStatusIn"]).optional(),
            "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
            "etag": t.string().optional(),
            "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
            "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
            "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "recordingDetails": t.proxy(renames["VideoRecordingDetailsIn"]).optional(),
            "id": t.string().optional(),
            "liveStreamingDetails": t.proxy(
                renames["VideoLiveStreamingDetailsIn"]
            ).optional(),
        }
    ).named(renames["VideoIn"])
    types["VideoOut"] = t.struct(
        {
            "processingDetails": t.proxy(
                renames["VideoProcessingDetailsOut"]
            ).optional(),
            "monetizationDetails": t.proxy(
                renames["VideoMonetizationDetailsOut"]
            ).optional(),
            "player": t.proxy(renames["VideoPlayerOut"]).optional(),
            "projectDetails": t.proxy(renames["VideoProjectDetailsOut"]).optional(),
            "kind": t.string().optional(),
            "suggestions": t.proxy(renames["VideoSuggestionsOut"]).optional(),
            "fileDetails": t.proxy(renames["VideoFileDetailsOut"]).optional(),
            "topicDetails": t.proxy(renames["VideoTopicDetailsOut"]).optional(),
            "status": t.proxy(renames["VideoStatusOut"]).optional(),
            "contentDetails": t.proxy(renames["VideoContentDetailsOut"]).optional(),
            "etag": t.string().optional(),
            "statistics": t.proxy(renames["VideoStatisticsOut"]).optional(),
            "ageGating": t.proxy(renames["VideoAgeGatingOut"]).optional(),
            "snippet": t.proxy(renames["VideoSnippetOut"]).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "recordingDetails": t.proxy(renames["VideoRecordingDetailsOut"]).optional(),
            "id": t.string().optional(),
            "liveStreamingDetails": t.proxy(
                renames["VideoLiveStreamingDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOut"])
    types["VideoAbuseReportSecondaryReasonIn"] = t.struct(
        {"label": t.string().optional(), "id": t.string().optional()}
    ).named(renames["VideoAbuseReportSecondaryReasonIn"])
    types["VideoAbuseReportSecondaryReasonOut"] = t.struct(
        {
            "label": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportSecondaryReasonOut"])
    types["LiveChatMemberMilestoneChatDetailsIn"] = t.struct(
        {
            "memberLevelName": t.string().optional(),
            "userComment": t.string().optional(),
            "memberMonth": t.integer().optional(),
        }
    ).named(renames["LiveChatMemberMilestoneChatDetailsIn"])
    types["LiveChatMemberMilestoneChatDetailsOut"] = t.struct(
        {
            "memberLevelName": t.string().optional(),
            "userComment": t.string().optional(),
            "memberMonth": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMemberMilestoneChatDetailsOut"])
    types["VideoSnippetIn"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "description": t.string().optional(),
            "localized": t.proxy(renames["VideoLocalizationIn"]).optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "defaultAudioLanguage": t.string().optional(),
            "categoryId": t.string().optional(),
            "channelTitle": t.string().optional(),
            "channelId": t.string().optional(),
            "liveBroadcastContent": t.string().optional(),
            "title": t.string().optional(),
            "tags": t.array(t.string()).optional(),
        }
    ).named(renames["VideoSnippetIn"])
    types["VideoSnippetOut"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "description": t.string().optional(),
            "localized": t.proxy(renames["VideoLocalizationOut"]).optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "defaultAudioLanguage": t.string().optional(),
            "categoryId": t.string().optional(),
            "channelTitle": t.string().optional(),
            "channelId": t.string().optional(),
            "liveBroadcastContent": t.string().optional(),
            "title": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoSnippetOut"])
    types["MembershipsDurationIn"] = t.struct(
        {
            "memberTotalDurationMonths": t.integer().optional(),
            "memberSince": t.string().optional(),
        }
    ).named(renames["MembershipsDurationIn"])
    types["MembershipsDurationOut"] = t.struct(
        {
            "memberTotalDurationMonths": t.integer().optional(),
            "memberSince": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsDurationOut"])
    types["PlaylistIn"] = t.struct(
        {
            "status": t.proxy(renames["PlaylistStatusIn"]).optional(),
            "contentDetails": t.proxy(renames["PlaylistContentDetailsIn"]).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "player": t.proxy(renames["PlaylistPlayerIn"]).optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["PlaylistSnippetIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlaylistIn"])
    types["PlaylistOut"] = t.struct(
        {
            "status": t.proxy(renames["PlaylistStatusOut"]).optional(),
            "contentDetails": t.proxy(renames["PlaylistContentDetailsOut"]).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "player": t.proxy(renames["PlaylistPlayerOut"]).optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["PlaylistSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistOut"])
    types["ActivityContentDetailsBulletinIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsBulletinIn"])
    types["ActivityContentDetailsBulletinOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsBulletinOut"])
    types["ActivityContentDetailsRecommendationIn"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
            "seedResourceId": t.proxy(renames["ResourceIdIn"]).optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["ActivityContentDetailsRecommendationIn"])
    types["ActivityContentDetailsRecommendationOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "seedResourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsRecommendationOut"])
    types["VideoFileDetailsAudioStreamIn"] = t.struct(
        {
            "vendor": t.string().optional(),
            "bitrateBps": t.string().optional(),
            "channelCount": t.integer().optional(),
            "codec": t.string().optional(),
        }
    ).named(renames["VideoFileDetailsAudioStreamIn"])
    types["VideoFileDetailsAudioStreamOut"] = t.struct(
        {
            "vendor": t.string().optional(),
            "bitrateBps": t.string().optional(),
            "channelCount": t.integer().optional(),
            "codec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFileDetailsAudioStreamOut"])
    types["ChannelSectionSnippetIn"] = t.struct(
        {
            "title": t.string().optional(),
            "type": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "style": t.string().optional(),
            "localized": t.proxy(renames["ChannelSectionLocalizationIn"]).optional(),
            "position": t.integer().optional(),
            "channelId": t.string().optional(),
        }
    ).named(renames["ChannelSectionSnippetIn"])
    types["ChannelSectionSnippetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "type": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "style": t.string().optional(),
            "localized": t.proxy(renames["ChannelSectionLocalizationOut"]).optional(),
            "position": t.integer().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionSnippetOut"])
    types["MembershipsDetailsIn"] = t.struct(
        {
            "accessibleLevels": t.array(t.string()).optional(),
            "membershipsDuration": t.proxy(renames["MembershipsDurationIn"]).optional(),
            "highestAccessibleLevel": t.string().optional(),
            "membershipsDurationAtLevels": t.array(
                t.proxy(renames["MembershipsDurationAtLevelIn"])
            ).optional(),
            "highestAccessibleLevelDisplayName": t.string().optional(),
        }
    ).named(renames["MembershipsDetailsIn"])
    types["MembershipsDetailsOut"] = t.struct(
        {
            "accessibleLevels": t.array(t.string()).optional(),
            "membershipsDuration": t.proxy(
                renames["MembershipsDurationOut"]
            ).optional(),
            "highestAccessibleLevel": t.string().optional(),
            "membershipsDurationAtLevels": t.array(
                t.proxy(renames["MembershipsDurationAtLevelOut"])
            ).optional(),
            "highestAccessibleLevelDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsDetailsOut"])
    types["EntityIn"] = t.struct(
        {"typeId": t.string(), "url": t.string(), "id": t.string()}
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "typeId": t.string(),
            "url": t.string(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["TestItemTestItemSnippetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TestItemTestItemSnippetIn"]
    )
    types["TestItemTestItemSnippetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TestItemTestItemSnippetOut"])
    types["CommentThreadSnippetIn"] = t.struct(
        {
            "videoId": t.string().optional(),
            "topLevelComment": t.proxy(renames["CommentIn"]).optional(),
            "totalReplyCount": t.integer().optional(),
            "channelId": t.string().optional(),
            "canReply": t.boolean().optional(),
            "isPublic": t.boolean().optional(),
        }
    ).named(renames["CommentThreadSnippetIn"])
    types["CommentThreadSnippetOut"] = t.struct(
        {
            "videoId": t.string().optional(),
            "topLevelComment": t.proxy(renames["CommentOut"]).optional(),
            "totalReplyCount": t.integer().optional(),
            "channelId": t.string().optional(),
            "canReply": t.boolean().optional(),
            "isPublic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentThreadSnippetOut"])
    types["LiveChatSuperStickerDetailsIn"] = t.struct(
        {
            "amountMicros": t.string().optional(),
            "amountDisplayString": t.string().optional(),
            "superStickerMetadata": t.proxy(
                renames["SuperStickerMetadataIn"]
            ).optional(),
            "currency": t.string().optional(),
            "tier": t.integer().optional(),
        }
    ).named(renames["LiveChatSuperStickerDetailsIn"])
    types["LiveChatSuperStickerDetailsOut"] = t.struct(
        {
            "amountMicros": t.string().optional(),
            "amountDisplayString": t.string().optional(),
            "superStickerMetadata": t.proxy(
                renames["SuperStickerMetadataOut"]
            ).optional(),
            "currency": t.string().optional(),
            "tier": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatSuperStickerDetailsOut"])
    types["LiveChatNewSponsorDetailsIn"] = t.struct(
        {"memberLevelName": t.string().optional(), "isUpgrade": t.boolean().optional()}
    ).named(renames["LiveChatNewSponsorDetailsIn"])
    types["LiveChatNewSponsorDetailsOut"] = t.struct(
        {
            "memberLevelName": t.string().optional(),
            "isUpgrade": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatNewSponsorDetailsOut"])
    types["CommentThreadIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "replies": t.proxy(renames["CommentThreadRepliesIn"]).optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["CommentThreadSnippetIn"]).optional(),
        }
    ).named(renames["CommentThreadIn"])
    types["CommentThreadOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "replies": t.proxy(renames["CommentThreadRepliesOut"]).optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["CommentThreadSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentThreadOut"])
    types["SearchResultIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.proxy(renames["ResourceIdIn"]).optional(),
            "snippet": t.proxy(renames["SearchResultSnippetIn"]).optional(),
        }
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.proxy(renames["ResourceIdOut"]).optional(),
            "snippet": t.proxy(renames["SearchResultSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["LiveChatTextMessageDetailsIn"] = t.struct(
        {"messageText": t.string().optional()}
    ).named(renames["LiveChatTextMessageDetailsIn"])
    types["LiveChatTextMessageDetailsOut"] = t.struct(
        {
            "messageText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatTextMessageDetailsOut"])
    types["PlaylistStatusIn"] = t.struct(
        {"privacyStatus": t.string().optional()}
    ).named(renames["PlaylistStatusIn"])
    types["PlaylistStatusOut"] = t.struct(
        {
            "privacyStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistStatusOut"])
    types["ActivityContentDetailsPromotedItemIn"] = t.struct(
        {
            "clickTrackingUrl": t.string().optional(),
            "forecastingUrl": t.array(t.string()).optional(),
            "customCtaButtonText": t.string().optional(),
            "impressionUrl": t.array(t.string()).optional(),
            "ctaType": t.string().optional(),
            "descriptionText": t.string().optional(),
            "videoId": t.string().optional(),
            "destinationUrl": t.string().optional(),
            "adTag": t.string().optional(),
            "creativeViewUrl": t.string().optional(),
        }
    ).named(renames["ActivityContentDetailsPromotedItemIn"])
    types["ActivityContentDetailsPromotedItemOut"] = t.struct(
        {
            "clickTrackingUrl": t.string().optional(),
            "forecastingUrl": t.array(t.string()).optional(),
            "customCtaButtonText": t.string().optional(),
            "impressionUrl": t.array(t.string()).optional(),
            "ctaType": t.string().optional(),
            "descriptionText": t.string().optional(),
            "videoId": t.string().optional(),
            "destinationUrl": t.string().optional(),
            "adTag": t.string().optional(),
            "creativeViewUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsPromotedItemOut"])
    types["ContentRatingIn"] = t.struct(
        {
            "mpaatRating": t.string().optional(),
            "cncRating": t.string().optional(),
            "kfcbRating": t.string().optional(),
            "oflcRating": t.string().optional(),
            "pefilmRating": t.string().optional(),
            "nfrcRating": t.string().optional(),
            "acbRating": t.string().optional(),
            "eefilmRating": t.string().optional(),
            "djctqRatingReasons": t.array(t.string()).optional(),
            "cscfRating": t.string().optional(),
            "bbfcRating": t.string().optional(),
            "nfvcbRating": t.string().optional(),
            "csaRating": t.string().optional(),
            "kmrbRating": t.string().optional(),
            "cbfcRating": t.string().optional(),
            "mocRating": t.string().optional(),
            "cccRating": t.string().optional(),
            "ilfilmRating": t.string().optional(),
            "incaaRating": t.string().optional(),
            "cnaRating": t.string().optional(),
            "czfilmRating": t.string().optional(),
            "ecbmctRating": t.string().optional(),
            "medietilsynetRating": t.string().optional(),
            "mccaaRating": t.string().optional(),
            "bfvcRating": t.string().optional(),
            "mpaaRating": t.string().optional(),
            "catvRating": t.string().optional(),
            "nmcRating": t.string().optional(),
            "moctwRating": t.string().optional(),
            "menaMpaaRating": t.string().optional(),
            "smsaRating": t.string().optional(),
            "grfilmRating": t.string().optional(),
            "agcomRating": t.string().optional(),
            "kijkwijzerRating": t.string().optional(),
            "mcstRating": t.string().optional(),
            "rcnofRating": t.string().optional(),
            "rteRating": t.string().optional(),
            "egfilmRating": t.string().optional(),
            "ytRating": t.string().optional(),
            "fpbRating": t.string().optional(),
            "nkclvRating": t.string().optional(),
            "fmocRating": t.string().optional(),
            "cicfRating": t.string().optional(),
            "nbcRating": t.string().optional(),
            "fcbmRating": t.string().optional(),
            "chvrsRating": t.string().optional(),
            "icaaRating": t.string().optional(),
            "russiaRating": t.string().optional(),
            "resorteviolenciaRating": t.string().optional(),
            "mekuRating": t.string().optional(),
            "mibacRating": t.string().optional(),
            "mdaRating": t.string().optional(),
            "lsfRating": t.string().optional(),
            "ifcoRating": t.string().optional(),
            "eirinRating": t.string().optional(),
            "catvfrRating": t.string().optional(),
            "fskRating": t.string().optional(),
            "mccypRating": t.string().optional(),
            "rtcRating": t.string().optional(),
            "fcoRating": t.string().optional(),
            "skfilmRating": t.string().optional(),
            "bmukkRating": t.string().optional(),
            "fpbRatingReasons": t.array(t.string()).optional(),
            "nbcplRating": t.string().optional(),
            "anatelRating": t.string().optional(),
            "mtrcbRating": t.string().optional(),
            "djctqRating": t.string().optional(),
            "smaisRating": t.string().optional(),
            "tvpgRating": t.string().optional(),
            "chfilmRating": t.string().optional(),
            "cceRating": t.string().optional(),
        }
    ).named(renames["ContentRatingIn"])
    types["ContentRatingOut"] = t.struct(
        {
            "mpaatRating": t.string().optional(),
            "cncRating": t.string().optional(),
            "kfcbRating": t.string().optional(),
            "oflcRating": t.string().optional(),
            "pefilmRating": t.string().optional(),
            "nfrcRating": t.string().optional(),
            "acbRating": t.string().optional(),
            "eefilmRating": t.string().optional(),
            "djctqRatingReasons": t.array(t.string()).optional(),
            "cscfRating": t.string().optional(),
            "bbfcRating": t.string().optional(),
            "nfvcbRating": t.string().optional(),
            "csaRating": t.string().optional(),
            "kmrbRating": t.string().optional(),
            "cbfcRating": t.string().optional(),
            "mocRating": t.string().optional(),
            "cccRating": t.string().optional(),
            "ilfilmRating": t.string().optional(),
            "incaaRating": t.string().optional(),
            "cnaRating": t.string().optional(),
            "czfilmRating": t.string().optional(),
            "ecbmctRating": t.string().optional(),
            "medietilsynetRating": t.string().optional(),
            "mccaaRating": t.string().optional(),
            "bfvcRating": t.string().optional(),
            "mpaaRating": t.string().optional(),
            "catvRating": t.string().optional(),
            "nmcRating": t.string().optional(),
            "moctwRating": t.string().optional(),
            "menaMpaaRating": t.string().optional(),
            "smsaRating": t.string().optional(),
            "grfilmRating": t.string().optional(),
            "agcomRating": t.string().optional(),
            "kijkwijzerRating": t.string().optional(),
            "mcstRating": t.string().optional(),
            "rcnofRating": t.string().optional(),
            "rteRating": t.string().optional(),
            "egfilmRating": t.string().optional(),
            "ytRating": t.string().optional(),
            "fpbRating": t.string().optional(),
            "nkclvRating": t.string().optional(),
            "fmocRating": t.string().optional(),
            "cicfRating": t.string().optional(),
            "nbcRating": t.string().optional(),
            "fcbmRating": t.string().optional(),
            "chvrsRating": t.string().optional(),
            "icaaRating": t.string().optional(),
            "russiaRating": t.string().optional(),
            "resorteviolenciaRating": t.string().optional(),
            "mekuRating": t.string().optional(),
            "mibacRating": t.string().optional(),
            "mdaRating": t.string().optional(),
            "lsfRating": t.string().optional(),
            "ifcoRating": t.string().optional(),
            "eirinRating": t.string().optional(),
            "catvfrRating": t.string().optional(),
            "fskRating": t.string().optional(),
            "mccypRating": t.string().optional(),
            "rtcRating": t.string().optional(),
            "fcoRating": t.string().optional(),
            "skfilmRating": t.string().optional(),
            "bmukkRating": t.string().optional(),
            "fpbRatingReasons": t.array(t.string()).optional(),
            "nbcplRating": t.string().optional(),
            "anatelRating": t.string().optional(),
            "mtrcbRating": t.string().optional(),
            "djctqRating": t.string().optional(),
            "smaisRating": t.string().optional(),
            "tvpgRating": t.string().optional(),
            "chfilmRating": t.string().optional(),
            "cceRating": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentRatingOut"])
    types["CaptionListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["CaptionIn"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
        }
    ).named(renames["CaptionListResponseIn"])
    types["CaptionListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["CaptionOut"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaptionListResponseOut"])
    types["LiveChatGiftMembershipReceivedDetailsIn"] = t.struct(
        {
            "gifterChannelId": t.string().optional(),
            "memberLevelName": t.string().optional(),
            "associatedMembershipGiftingMessageId": t.string().optional(),
        }
    ).named(renames["LiveChatGiftMembershipReceivedDetailsIn"])
    types["LiveChatGiftMembershipReceivedDetailsOut"] = t.struct(
        {
            "gifterChannelId": t.string().optional(),
            "memberLevelName": t.string().optional(),
            "associatedMembershipGiftingMessageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatGiftMembershipReceivedDetailsOut"])
    types["CommentSnippetAuthorChannelIdIn"] = t.struct({"value": t.string()}).named(
        renames["CommentSnippetAuthorChannelIdIn"]
    )
    types["CommentSnippetAuthorChannelIdOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommentSnippetAuthorChannelIdOut"])
    types["ChannelSnippetIn"] = t.struct(
        {
            "defaultLanguage": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "publishedAt": t.string().optional(),
            "title": t.string().optional(),
            "localized": t.proxy(renames["ChannelLocalizationIn"]).optional(),
            "description": t.string().optional(),
            "country": t.string().optional(),
            "customUrl": t.string().optional(),
        }
    ).named(renames["ChannelSnippetIn"])
    types["ChannelSnippetOut"] = t.struct(
        {
            "defaultLanguage": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "publishedAt": t.string().optional(),
            "title": t.string().optional(),
            "localized": t.proxy(renames["ChannelLocalizationOut"]).optional(),
            "description": t.string().optional(),
            "country": t.string().optional(),
            "customUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSnippetOut"])
    types["CdnSettingsIn"] = t.struct(
        {
            "ingestionInfo": t.proxy(renames["IngestionInfoIn"]).optional(),
            "ingestionType": t.string().optional(),
            "resolution": t.string().optional(),
            "frameRate": t.string().optional(),
            "format": t.string().optional(),
        }
    ).named(renames["CdnSettingsIn"])
    types["CdnSettingsOut"] = t.struct(
        {
            "ingestionInfo": t.proxy(renames["IngestionInfoOut"]).optional(),
            "ingestionType": t.string().optional(),
            "resolution": t.string().optional(),
            "frameRate": t.string().optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CdnSettingsOut"])
    types["ChannelSectionListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "items": t.array(t.proxy(renames["ChannelSectionIn"])).optional(),
            "visitorId": t.string().optional(),
        }
    ).named(renames["ChannelSectionListResponseIn"])
    types["ChannelSectionListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "items": t.array(t.proxy(renames["ChannelSectionOut"])).optional(),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionListResponseOut"])
    types["PlaylistItemStatusIn"] = t.struct(
        {"privacyStatus": t.string().optional()}
    ).named(renames["PlaylistItemStatusIn"])
    types["PlaylistItemStatusOut"] = t.struct(
        {
            "privacyStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemStatusOut"])
    types["SuperChatEventIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["SuperChatEventSnippetIn"]).optional(),
        }
    ).named(renames["SuperChatEventIn"])
    types["SuperChatEventOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["SuperChatEventSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperChatEventOut"])
    types["SearchListResponseIn"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "prevPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["SearchResultIn"])).optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "regionCode": t.string(),
        }
    ).named(renames["SearchListResponseIn"])
    types["SearchListResponseOut"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "prevPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchListResponseOut"])
    types["PlaylistItemSnippetIn"] = t.struct(
        {
            "title": t.string().optional(),
            "videoOwnerChannelId": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
            "description": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "channelTitle": t.string().optional(),
            "playlistId": t.string().optional(),
            "channelId": t.string().optional(),
            "videoOwnerChannelTitle": t.string().optional(),
            "position": t.integer().optional(),
            "publishedAt": t.string().optional(),
        }
    ).named(renames["PlaylistItemSnippetIn"])
    types["PlaylistItemSnippetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "videoOwnerChannelId": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "description": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "channelTitle": t.string().optional(),
            "playlistId": t.string().optional(),
            "channelId": t.string().optional(),
            "videoOwnerChannelTitle": t.string().optional(),
            "position": t.integer().optional(),
            "publishedAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemSnippetOut"])
    types["ChannelTopicDetailsIn"] = t.struct(
        {
            "topicIds": t.array(t.string()).optional(),
            "topicCategories": t.array(t.string()).optional(),
        }
    ).named(renames["ChannelTopicDetailsIn"])
    types["ChannelTopicDetailsOut"] = t.struct(
        {
            "topicIds": t.array(t.string()).optional(),
            "topicCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelTopicDetailsOut"])
    types["LiveChatUserBannedMessageDetailsIn"] = t.struct(
        {
            "bannedUserDetails": t.proxy(renames["ChannelProfileDetailsIn"]).optional(),
            "banType": t.string().optional(),
            "banDurationSeconds": t.string().optional(),
        }
    ).named(renames["LiveChatUserBannedMessageDetailsIn"])
    types["LiveChatUserBannedMessageDetailsOut"] = t.struct(
        {
            "bannedUserDetails": t.proxy(
                renames["ChannelProfileDetailsOut"]
            ).optional(),
            "banType": t.string().optional(),
            "banDurationSeconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatUserBannedMessageDetailsOut"])
    types["ThirdPartyLinkSnippetIn"] = t.struct(
        {
            "type": t.string().optional(),
            "channelToStoreLink": t.proxy(
                renames["ChannelToStoreLinkDetailsIn"]
            ).optional(),
        }
    ).named(renames["ThirdPartyLinkSnippetIn"])
    types["ThirdPartyLinkSnippetOut"] = t.struct(
        {
            "type": t.string().optional(),
            "channelToStoreLink": t.proxy(
                renames["ChannelToStoreLinkDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyLinkSnippetOut"])
    types["LiveChatMembershipGiftingDetailsIn"] = t.struct(
        {
            "giftMembershipsCount": t.integer().optional(),
            "giftMembershipsLevelName": t.string().optional(),
        }
    ).named(renames["LiveChatMembershipGiftingDetailsIn"])
    types["LiveChatMembershipGiftingDetailsOut"] = t.struct(
        {
            "giftMembershipsCount": t.integer().optional(),
            "giftMembershipsLevelName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMembershipGiftingDetailsOut"])
    types["SubscriptionSubscriberSnippetIn"] = t.struct(
        {
            "description": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "title": t.string().optional(),
            "channelId": t.string().optional(),
        }
    ).named(renames["SubscriptionSubscriberSnippetIn"])
    types["SubscriptionSubscriberSnippetOut"] = t.struct(
        {
            "description": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "title": t.string().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionSubscriberSnippetOut"])
    types["VideoContentDetailsIn"] = t.struct(
        {
            "definition": t.string().optional(),
            "licensedContent": t.boolean().optional(),
            "hasCustomThumbnail": t.boolean().optional(),
            "projection": t.string().optional(),
            "regionRestriction": t.proxy(
                renames["VideoContentDetailsRegionRestrictionIn"]
            ).optional(),
            "caption": t.string().optional(),
            "duration": t.string().optional(),
            "dimension": t.string().optional(),
            "contentRating": t.proxy(renames["ContentRatingIn"]).optional(),
            "countryRestriction": t.proxy(renames["AccessPolicyIn"]).optional(),
        }
    ).named(renames["VideoContentDetailsIn"])
    types["VideoContentDetailsOut"] = t.struct(
        {
            "definition": t.string().optional(),
            "licensedContent": t.boolean().optional(),
            "hasCustomThumbnail": t.boolean().optional(),
            "projection": t.string().optional(),
            "regionRestriction": t.proxy(
                renames["VideoContentDetailsRegionRestrictionOut"]
            ).optional(),
            "caption": t.string().optional(),
            "duration": t.string().optional(),
            "dimension": t.string().optional(),
            "contentRating": t.proxy(renames["ContentRatingOut"]).optional(),
            "countryRestriction": t.proxy(renames["AccessPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoContentDetailsOut"])
    types["I18nRegionSnippetIn"] = t.struct(
        {"gl": t.string().optional(), "name": t.string().optional()}
    ).named(renames["I18nRegionSnippetIn"])
    types["I18nRegionSnippetOut"] = t.struct(
        {
            "gl": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nRegionSnippetOut"])
    types["LiveChatMessageAuthorDetailsIn"] = t.struct(
        {
            "isChatModerator": t.boolean().optional(),
            "displayName": t.string().optional(),
            "isChatOwner": t.boolean().optional(),
            "isChatSponsor": t.boolean().optional(),
            "isVerified": t.boolean().optional(),
            "profileImageUrl": t.string().optional(),
            "channelUrl": t.string().optional(),
            "channelId": t.string().optional(),
        }
    ).named(renames["LiveChatMessageAuthorDetailsIn"])
    types["LiveChatMessageAuthorDetailsOut"] = t.struct(
        {
            "isChatModerator": t.boolean().optional(),
            "displayName": t.string().optional(),
            "isChatOwner": t.boolean().optional(),
            "isChatSponsor": t.boolean().optional(),
            "isVerified": t.boolean().optional(),
            "profileImageUrl": t.string().optional(),
            "channelUrl": t.string().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageAuthorDetailsOut"])
    types["VideoCategoryListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "prevPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoCategoryIn"])).optional(),
        }
    ).named(renames["VideoCategoryListResponseIn"])
    types["VideoCategoryListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "prevPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoCategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCategoryListResponseOut"])
    types["PlaylistItemIn"] = t.struct(
        {
            "status": t.proxy(renames["PlaylistItemStatusIn"]).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "contentDetails": t.proxy(
                renames["PlaylistItemContentDetailsIn"]
            ).optional(),
            "snippet": t.proxy(renames["PlaylistItemSnippetIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PlaylistItemIn"])
    types["PlaylistItemOut"] = t.struct(
        {
            "status": t.proxy(renames["PlaylistItemStatusOut"]).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "contentDetails": t.proxy(
                renames["PlaylistItemContentDetailsOut"]
            ).optional(),
            "snippet": t.proxy(renames["PlaylistItemSnippetOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemOut"])
    types["CommentThreadRepliesIn"] = t.struct(
        {"comments": t.array(t.proxy(renames["CommentIn"])).optional()}
    ).named(renames["CommentThreadRepliesIn"])
    types["CommentThreadRepliesOut"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentThreadRepliesOut"])
    types["LiveChatMessageListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string(),
            "visitorId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "offlineAt": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "items": t.array(t.proxy(renames["LiveChatMessageIn"])),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "pollingIntervalMillis": t.integer().optional(),
        }
    ).named(renames["LiveChatMessageListResponseIn"])
    types["LiveChatMessageListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string(),
            "visitorId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "offlineAt": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "items": t.array(t.proxy(renames["LiveChatMessageOut"])),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "pollingIntervalMillis": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageListResponseOut"])
    types["ActivityContentDetailsSocialIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
            "type": t.string().optional(),
            "author": t.string().optional(),
            "referenceUrl": t.string().optional(),
        }
    ).named(renames["ActivityContentDetailsSocialIn"])
    types["ActivityContentDetailsSocialOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "type": t.string().optional(),
            "author": t.string().optional(),
            "referenceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsSocialOut"])
    types["I18nRegionIn"] = t.struct(
        {
            "snippet": t.proxy(renames["I18nRegionSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["I18nRegionIn"])
    types["I18nRegionOut"] = t.struct(
        {
            "snippet": t.proxy(renames["I18nRegionSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nRegionOut"])
    types["VideoTopicDetailsIn"] = t.struct(
        {
            "relevantTopicIds": t.array(t.string()).optional(),
            "topicCategories": t.array(t.string()).optional(),
            "topicIds": t.array(t.string()).optional(),
        }
    ).named(renames["VideoTopicDetailsIn"])
    types["VideoTopicDetailsOut"] = t.struct(
        {
            "relevantTopicIds": t.array(t.string()).optional(),
            "topicCategories": t.array(t.string()).optional(),
            "topicIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoTopicDetailsOut"])
    types["PlaylistListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PlaylistIn"])).optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
        }
    ).named(renames["PlaylistListResponseIn"])
    types["PlaylistListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PlaylistOut"])).optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistListResponseOut"])
    types["InvideoBrandingIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "timing": t.proxy(renames["InvideoTimingIn"]).optional(),
            "imageBytes": t.string().optional(),
            "targetChannelId": t.string().optional(),
            "position": t.proxy(renames["InvideoPositionIn"]).optional(),
        }
    ).named(renames["InvideoBrandingIn"])
    types["InvideoBrandingOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "timing": t.proxy(renames["InvideoTimingOut"]).optional(),
            "imageBytes": t.string().optional(),
            "targetChannelId": t.string().optional(),
            "position": t.proxy(renames["InvideoPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvideoBrandingOut"])
    types["CommentIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["CommentSnippetIn"]).optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["CommentSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["RelatedEntityIn"] = t.struct({"entity": t.proxy(renames["EntityIn"])}).named(
        renames["RelatedEntityIn"]
    )
    types["RelatedEntityOut"] = t.struct(
        {
            "entity": t.proxy(renames["EntityOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedEntityOut"])
    types["SuperChatEventSnippetIn"] = t.struct(
        {
            "isSuperStickerEvent": t.boolean().optional(),
            "currency": t.string().optional(),
            "channelId": t.string().optional(),
            "supporterDetails": t.proxy(renames["ChannelProfileDetailsIn"]).optional(),
            "commentText": t.string().optional(),
            "displayString": t.string().optional(),
            "superStickerMetadata": t.proxy(
                renames["SuperStickerMetadataIn"]
            ).optional(),
            "createdAt": t.string().optional(),
            "messageType": t.integer().optional(),
            "amountMicros": t.string().optional(),
        }
    ).named(renames["SuperChatEventSnippetIn"])
    types["SuperChatEventSnippetOut"] = t.struct(
        {
            "isSuperStickerEvent": t.boolean().optional(),
            "currency": t.string().optional(),
            "channelId": t.string().optional(),
            "supporterDetails": t.proxy(renames["ChannelProfileDetailsOut"]).optional(),
            "commentText": t.string().optional(),
            "displayString": t.string().optional(),
            "superStickerMetadata": t.proxy(
                renames["SuperStickerMetadataOut"]
            ).optional(),
            "createdAt": t.string().optional(),
            "messageType": t.integer().optional(),
            "amountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperChatEventSnippetOut"])
    types["AccessPolicyIn"] = t.struct(
        {"exception": t.array(t.string()).optional(), "allowed": t.boolean().optional()}
    ).named(renames["AccessPolicyIn"])
    types["AccessPolicyOut"] = t.struct(
        {
            "exception": t.array(t.string()).optional(),
            "allowed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessPolicyOut"])
    types["VideoStatusIn"] = t.struct(
        {
            "madeForKids": t.boolean(),
            "privacyStatus": t.string().optional(),
            "failureReason": t.string().optional(),
            "uploadStatus": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "embeddable": t.boolean().optional(),
            "selfDeclaredMadeForKids": t.boolean(),
            "publicStatsViewable": t.boolean().optional(),
            "license": t.string().optional(),
            "publishAt": t.string().optional(),
        }
    ).named(renames["VideoStatusIn"])
    types["VideoStatusOut"] = t.struct(
        {
            "madeForKids": t.boolean(),
            "privacyStatus": t.string().optional(),
            "failureReason": t.string().optional(),
            "uploadStatus": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "embeddable": t.boolean().optional(),
            "selfDeclaredMadeForKids": t.boolean(),
            "publicStatsViewable": t.boolean().optional(),
            "license": t.string().optional(),
            "publishAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoStatusOut"])
    types["LiveBroadcastIn"] = t.struct(
        {
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "contentDetails": t.proxy(
                renames["LiveBroadcastContentDetailsIn"]
            ).optional(),
            "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
            "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
        }
    ).named(renames["LiveBroadcastIn"])
    types["LiveBroadcastOut"] = t.struct(
        {
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveBroadcastSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "contentDetails": t.proxy(
                renames["LiveBroadcastContentDetailsOut"]
            ).optional(),
            "status": t.proxy(renames["LiveBroadcastStatusOut"]).optional(),
            "statistics": t.proxy(renames["LiveBroadcastStatisticsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastOut"])
    types["VideoProcessingDetailsIn"] = t.struct(
        {
            "processingFailureReason": t.string().optional(),
            "thumbnailsAvailability": t.string().optional(),
            "processingProgress": t.proxy(
                renames["VideoProcessingDetailsProcessingProgressIn"]
            ).optional(),
            "processingStatus": t.string().optional(),
            "editorSuggestionsAvailability": t.string().optional(),
            "processingIssuesAvailability": t.string().optional(),
            "tagSuggestionsAvailability": t.string().optional(),
            "fileDetailsAvailability": t.string().optional(),
        }
    ).named(renames["VideoProcessingDetailsIn"])
    types["VideoProcessingDetailsOut"] = t.struct(
        {
            "processingFailureReason": t.string().optional(),
            "thumbnailsAvailability": t.string().optional(),
            "processingProgress": t.proxy(
                renames["VideoProcessingDetailsProcessingProgressOut"]
            ).optional(),
            "processingStatus": t.string().optional(),
            "editorSuggestionsAvailability": t.string().optional(),
            "processingIssuesAvailability": t.string().optional(),
            "tagSuggestionsAvailability": t.string().optional(),
            "fileDetailsAvailability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoProcessingDetailsOut"])
    types["ActivityContentDetailsIn"] = t.struct(
        {
            "playlistItem": t.proxy(
                renames["ActivityContentDetailsPlaylistItemIn"]
            ).optional(),
            "social": t.proxy(renames["ActivityContentDetailsSocialIn"]).optional(),
            "upload": t.proxy(renames["ActivityContentDetailsUploadIn"]).optional(),
            "recommendation": t.proxy(
                renames["ActivityContentDetailsRecommendationIn"]
            ).optional(),
            "bulletin": t.proxy(renames["ActivityContentDetailsBulletinIn"]).optional(),
            "subscription": t.proxy(
                renames["ActivityContentDetailsSubscriptionIn"]
            ).optional(),
            "like": t.proxy(renames["ActivityContentDetailsLikeIn"]).optional(),
            "promotedItem": t.proxy(
                renames["ActivityContentDetailsPromotedItemIn"]
            ).optional(),
            "comment": t.proxy(renames["ActivityContentDetailsCommentIn"]).optional(),
            "channelItem": t.proxy(
                renames["ActivityContentDetailsChannelItemIn"]
            ).optional(),
            "favorite": t.proxy(renames["ActivityContentDetailsFavoriteIn"]).optional(),
        }
    ).named(renames["ActivityContentDetailsIn"])
    types["ActivityContentDetailsOut"] = t.struct(
        {
            "playlistItem": t.proxy(
                renames["ActivityContentDetailsPlaylistItemOut"]
            ).optional(),
            "social": t.proxy(renames["ActivityContentDetailsSocialOut"]).optional(),
            "upload": t.proxy(renames["ActivityContentDetailsUploadOut"]).optional(),
            "recommendation": t.proxy(
                renames["ActivityContentDetailsRecommendationOut"]
            ).optional(),
            "bulletin": t.proxy(
                renames["ActivityContentDetailsBulletinOut"]
            ).optional(),
            "subscription": t.proxy(
                renames["ActivityContentDetailsSubscriptionOut"]
            ).optional(),
            "like": t.proxy(renames["ActivityContentDetailsLikeOut"]).optional(),
            "promotedItem": t.proxy(
                renames["ActivityContentDetailsPromotedItemOut"]
            ).optional(),
            "comment": t.proxy(renames["ActivityContentDetailsCommentOut"]).optional(),
            "channelItem": t.proxy(
                renames["ActivityContentDetailsChannelItemOut"]
            ).optional(),
            "favorite": t.proxy(
                renames["ActivityContentDetailsFavoriteOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsOut"])
    types["VideoAbuseReportIn"] = t.struct(
        {
            "reasonId": t.string().optional(),
            "videoId": t.string().optional(),
            "comments": t.string().optional(),
            "language": t.string().optional(),
            "secondaryReasonId": t.string().optional(),
        }
    ).named(renames["VideoAbuseReportIn"])
    types["VideoAbuseReportOut"] = t.struct(
        {
            "reasonId": t.string().optional(),
            "videoId": t.string().optional(),
            "comments": t.string().optional(),
            "language": t.string().optional(),
            "secondaryReasonId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportOut"])
    types["VideoProcessingDetailsProcessingProgressIn"] = t.struct(
        {
            "partsTotal": t.string().optional(),
            "partsProcessed": t.string().optional(),
            "timeLeftMs": t.string().optional(),
        }
    ).named(renames["VideoProcessingDetailsProcessingProgressIn"])
    types["VideoProcessingDetailsProcessingProgressOut"] = t.struct(
        {
            "partsTotal": t.string().optional(),
            "partsProcessed": t.string().optional(),
            "timeLeftMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoProcessingDetailsProcessingProgressOut"])
    types["LiveChatMessageSnippetIn"] = t.struct(
        {
            "type": t.string().optional(),
            "userBannedDetails": t.proxy(renames["LiveChatUserBannedMessageDetailsIn"]),
            "messageDeletedDetails": t.proxy(
                renames["LiveChatMessageDeletedDetailsIn"]
            ),
            "superChatDetails": t.proxy(
                renames["LiveChatSuperChatDetailsIn"]
            ).optional(),
            "memberMilestoneChatDetails": t.proxy(
                renames["LiveChatMemberMilestoneChatDetailsIn"]
            ).optional(),
            "displayMessage": t.string().optional(),
            "superStickerDetails": t.proxy(
                renames["LiveChatSuperStickerDetailsIn"]
            ).optional(),
            "textMessageDetails": t.proxy(
                renames["LiveChatTextMessageDetailsIn"]
            ).optional(),
            "giftMembershipReceivedDetails": t.proxy(
                renames["LiveChatGiftMembershipReceivedDetailsIn"]
            ).optional(),
            "authorChannelId": t.string().optional(),
            "messageRetractedDetails": t.proxy(
                renames["LiveChatMessageRetractedDetailsIn"]
            ),
            "hasDisplayContent": t.boolean().optional(),
            "newSponsorDetails": t.proxy(
                renames["LiveChatNewSponsorDetailsIn"]
            ).optional(),
            "publishedAt": t.string().optional(),
            "fanFundingEventDetails": t.proxy(
                renames["LiveChatFanFundingEventDetailsIn"]
            ).optional(),
            "liveChatId": t.string(),
            "membershipGiftingDetails": t.proxy(
                renames["LiveChatMembershipGiftingDetailsIn"]
            ).optional(),
        }
    ).named(renames["LiveChatMessageSnippetIn"])
    types["LiveChatMessageSnippetOut"] = t.struct(
        {
            "type": t.string().optional(),
            "userBannedDetails": t.proxy(
                renames["LiveChatUserBannedMessageDetailsOut"]
            ),
            "messageDeletedDetails": t.proxy(
                renames["LiveChatMessageDeletedDetailsOut"]
            ),
            "superChatDetails": t.proxy(
                renames["LiveChatSuperChatDetailsOut"]
            ).optional(),
            "memberMilestoneChatDetails": t.proxy(
                renames["LiveChatMemberMilestoneChatDetailsOut"]
            ).optional(),
            "displayMessage": t.string().optional(),
            "superStickerDetails": t.proxy(
                renames["LiveChatSuperStickerDetailsOut"]
            ).optional(),
            "textMessageDetails": t.proxy(
                renames["LiveChatTextMessageDetailsOut"]
            ).optional(),
            "giftMembershipReceivedDetails": t.proxy(
                renames["LiveChatGiftMembershipReceivedDetailsOut"]
            ).optional(),
            "authorChannelId": t.string().optional(),
            "messageRetractedDetails": t.proxy(
                renames["LiveChatMessageRetractedDetailsOut"]
            ),
            "hasDisplayContent": t.boolean().optional(),
            "newSponsorDetails": t.proxy(
                renames["LiveChatNewSponsorDetailsOut"]
            ).optional(),
            "publishedAt": t.string().optional(),
            "fanFundingEventDetails": t.proxy(
                renames["LiveChatFanFundingEventDetailsOut"]
            ).optional(),
            "liveChatId": t.string(),
            "membershipGiftingDetails": t.proxy(
                renames["LiveChatMembershipGiftingDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageSnippetOut"])
    types["VideoSuggestionsTagSuggestionIn"] = t.struct(
        {
            "categoryRestricts": t.array(t.string()).optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["VideoSuggestionsTagSuggestionIn"])
    types["VideoSuggestionsTagSuggestionOut"] = t.struct(
        {
            "categoryRestricts": t.array(t.string()).optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoSuggestionsTagSuggestionOut"])
    types["I18nLanguageListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["I18nLanguageIn"])).optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
        }
    ).named(renames["I18nLanguageListResponseIn"])
    types["I18nLanguageListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["I18nLanguageOut"])).optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nLanguageListResponseOut"])
    types["InvideoTimingIn"] = t.struct(
        {
            "offsetMs": t.string().optional(),
            "type": t.string().optional(),
            "durationMs": t.string().optional(),
        }
    ).named(renames["InvideoTimingIn"])
    types["InvideoTimingOut"] = t.struct(
        {
            "offsetMs": t.string().optional(),
            "type": t.string().optional(),
            "durationMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvideoTimingOut"])
    types["VideoAbuseReportReasonSnippetIn"] = t.struct(
        {
            "label": t.string().optional(),
            "secondaryReasons": t.array(
                t.proxy(renames["VideoAbuseReportSecondaryReasonIn"])
            ).optional(),
        }
    ).named(renames["VideoAbuseReportReasonSnippetIn"])
    types["VideoAbuseReportReasonSnippetOut"] = t.struct(
        {
            "label": t.string().optional(),
            "secondaryReasons": t.array(
                t.proxy(renames["VideoAbuseReportSecondaryReasonOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportReasonSnippetOut"])
    types["CommentSnippetIn"] = t.struct(
        {
            "canRate": t.boolean().optional(),
            "authorDisplayName": t.string().optional(),
            "channelId": t.string().optional(),
            "moderationStatus": t.string().optional(),
            "updatedAt": t.string().optional(),
            "videoId": t.string().optional(),
            "authorProfileImageUrl": t.string().optional(),
            "publishedAt": t.string().optional(),
            "parentId": t.string().optional(),
            "viewerRating": t.string().optional(),
            "authorChannelUrl": t.string().optional(),
            "authorChannelId": t.proxy(renames["CommentSnippetAuthorChannelIdIn"]),
            "likeCount": t.integer().optional(),
            "textDisplay": t.string().optional(),
            "textOriginal": t.string().optional(),
        }
    ).named(renames["CommentSnippetIn"])
    types["CommentSnippetOut"] = t.struct(
        {
            "canRate": t.boolean().optional(),
            "authorDisplayName": t.string().optional(),
            "channelId": t.string().optional(),
            "moderationStatus": t.string().optional(),
            "updatedAt": t.string().optional(),
            "videoId": t.string().optional(),
            "authorProfileImageUrl": t.string().optional(),
            "publishedAt": t.string().optional(),
            "parentId": t.string().optional(),
            "viewerRating": t.string().optional(),
            "authorChannelUrl": t.string().optional(),
            "authorChannelId": t.proxy(renames["CommentSnippetAuthorChannelIdOut"]),
            "likeCount": t.integer().optional(),
            "textDisplay": t.string().optional(),
            "textOriginal": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentSnippetOut"])
    types["VideoAbuseReportReasonIn"] = t.struct(
        {
            "id": t.string().optional(),
            "snippet": t.proxy(renames["VideoAbuseReportReasonSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["VideoAbuseReportReasonIn"])
    types["VideoAbuseReportReasonOut"] = t.struct(
        {
            "id": t.string().optional(),
            "snippet": t.proxy(renames["VideoAbuseReportReasonSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportReasonOut"])
    types["LanguageTagIn"] = t.struct({"value": t.string()}).named(
        renames["LanguageTagIn"]
    )
    types["LanguageTagOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LanguageTagOut"])
    types["ChannelStatisticsIn"] = t.struct(
        {
            "videoCount": t.string().optional(),
            "commentCount": t.string().optional(),
            "viewCount": t.string().optional(),
            "subscriberCount": t.string().optional(),
            "hiddenSubscriberCount": t.boolean().optional(),
        }
    ).named(renames["ChannelStatisticsIn"])
    types["ChannelStatisticsOut"] = t.struct(
        {
            "videoCount": t.string().optional(),
            "commentCount": t.string().optional(),
            "viewCount": t.string().optional(),
            "subscriberCount": t.string().optional(),
            "hiddenSubscriberCount": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelStatisticsOut"])
    types["VideoStatisticsIn"] = t.struct(
        {
            "viewCount": t.string().optional(),
            "dislikeCount": t.string().optional(),
            "favoriteCount": t.string().optional(),
            "likeCount": t.string().optional(),
            "commentCount": t.string().optional(),
        }
    ).named(renames["VideoStatisticsIn"])
    types["VideoStatisticsOut"] = t.struct(
        {
            "viewCount": t.string().optional(),
            "dislikeCount": t.string().optional(),
            "favoriteCount": t.string().optional(),
            "likeCount": t.string().optional(),
            "commentCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoStatisticsOut"])
    types["ChannelSettingsIn"] = t.struct(
        {
            "unsubscribedTrailer": t.string().optional(),
            "showRelatedChannels": t.boolean().optional(),
            "description": t.string().optional(),
            "defaultTab": t.string().optional(),
            "featuredChannelsUrls": t.array(t.string()).optional(),
            "country": t.string().optional(),
            "defaultLanguage": t.string(),
            "moderateComments": t.boolean().optional(),
            "showBrowseView": t.boolean().optional(),
            "profileColor": t.string().optional(),
            "title": t.string().optional(),
            "featuredChannelsTitle": t.string().optional(),
            "keywords": t.string().optional(),
            "trackingAnalyticsAccountId": t.string().optional(),
        }
    ).named(renames["ChannelSettingsIn"])
    types["ChannelSettingsOut"] = t.struct(
        {
            "unsubscribedTrailer": t.string().optional(),
            "showRelatedChannels": t.boolean().optional(),
            "description": t.string().optional(),
            "defaultTab": t.string().optional(),
            "featuredChannelsUrls": t.array(t.string()).optional(),
            "country": t.string().optional(),
            "defaultLanguage": t.string(),
            "moderateComments": t.boolean().optional(),
            "showBrowseView": t.boolean().optional(),
            "profileColor": t.string().optional(),
            "title": t.string().optional(),
            "featuredChannelsTitle": t.string().optional(),
            "keywords": t.string().optional(),
            "trackingAnalyticsAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSettingsOut"])
    types["LiveChatBanIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatBanSnippetIn"]).optional(),
        }
    ).named(renames["LiveChatBanIn"])
    types["LiveChatBanOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatBanSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatBanOut"])
    types["VideoLocalizationIn"] = t.struct(
        {"title": t.string().optional(), "description": t.string().optional()}
    ).named(renames["VideoLocalizationIn"])
    types["VideoLocalizationOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoLocalizationOut"])
    types["ChannelIn"] = t.struct(
        {
            "topicDetails": t.proxy(renames["ChannelTopicDetailsIn"]).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "snippet": t.proxy(renames["ChannelSnippetIn"]).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "contentOwnerDetails": t.proxy(
                renames["ChannelContentOwnerDetailsIn"]
            ).optional(),
            "conversionPings": t.proxy(renames["ChannelConversionPingsIn"]).optional(),
            "brandingSettings": t.proxy(
                renames["ChannelBrandingSettingsIn"]
            ).optional(),
            "statistics": t.proxy(renames["ChannelStatisticsIn"]).optional(),
            "id": t.string().optional(),
            "contentDetails": t.proxy(renames["ChannelContentDetailsIn"]).optional(),
            "status": t.proxy(renames["ChannelStatusIn"]).optional(),
            "auditDetails": t.proxy(renames["ChannelAuditDetailsIn"]).optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "topicDetails": t.proxy(renames["ChannelTopicDetailsOut"]).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "snippet": t.proxy(renames["ChannelSnippetOut"]).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "contentOwnerDetails": t.proxy(
                renames["ChannelContentOwnerDetailsOut"]
            ).optional(),
            "conversionPings": t.proxy(renames["ChannelConversionPingsOut"]).optional(),
            "brandingSettings": t.proxy(
                renames["ChannelBrandingSettingsOut"]
            ).optional(),
            "statistics": t.proxy(renames["ChannelStatisticsOut"]).optional(),
            "id": t.string().optional(),
            "contentDetails": t.proxy(renames["ChannelContentDetailsOut"]).optional(),
            "status": t.proxy(renames["ChannelStatusOut"]).optional(),
            "auditDetails": t.proxy(renames["ChannelAuditDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["CommentThreadListResponseIn"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentThreadIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["CommentThreadListResponseIn"])
    types["CommentThreadListResponseOut"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentThreadOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentThreadListResponseOut"])
    types["LiveStreamContentDetailsIn"] = t.struct(
        {
            "isReusable": t.boolean().optional(),
            "closedCaptionsIngestionUrl": t.string().optional(),
        }
    ).named(renames["LiveStreamContentDetailsIn"])
    types["LiveStreamContentDetailsOut"] = t.struct(
        {
            "isReusable": t.boolean().optional(),
            "closedCaptionsIngestionUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamContentDetailsOut"])
    types["CaptionSnippetIn"] = t.struct(
        {
            "isEasyReader": t.boolean().optional(),
            "status": t.string().optional(),
            "language": t.string().optional(),
            "isDraft": t.boolean().optional(),
            "trackKind": t.string().optional(),
            "failureReason": t.string().optional(),
            "isAutoSynced": t.boolean().optional(),
            "videoId": t.string().optional(),
            "isCC": t.boolean().optional(),
            "lastUpdated": t.string().optional(),
            "name": t.string().optional(),
            "isLarge": t.boolean().optional(),
            "audioTrackType": t.string().optional(),
        }
    ).named(renames["CaptionSnippetIn"])
    types["CaptionSnippetOut"] = t.struct(
        {
            "isEasyReader": t.boolean().optional(),
            "status": t.string().optional(),
            "language": t.string().optional(),
            "isDraft": t.boolean().optional(),
            "trackKind": t.string().optional(),
            "failureReason": t.string().optional(),
            "isAutoSynced": t.boolean().optional(),
            "videoId": t.string().optional(),
            "isCC": t.boolean().optional(),
            "lastUpdated": t.string().optional(),
            "name": t.string().optional(),
            "isLarge": t.boolean().optional(),
            "audioTrackType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaptionSnippetOut"])
    types["VideoFileDetailsIn"] = t.struct(
        {
            "fileType": t.string().optional(),
            "videoStreams": t.array(
                t.proxy(renames["VideoFileDetailsVideoStreamIn"])
            ).optional(),
            "creationTime": t.string().optional(),
            "durationMs": t.string().optional(),
            "audioStreams": t.array(
                t.proxy(renames["VideoFileDetailsAudioStreamIn"])
            ).optional(),
            "fileName": t.string().optional(),
            "container": t.string().optional(),
            "fileSize": t.string().optional(),
            "bitrateBps": t.string().optional(),
        }
    ).named(renames["VideoFileDetailsIn"])
    types["VideoFileDetailsOut"] = t.struct(
        {
            "fileType": t.string().optional(),
            "videoStreams": t.array(
                t.proxy(renames["VideoFileDetailsVideoStreamOut"])
            ).optional(),
            "creationTime": t.string().optional(),
            "durationMs": t.string().optional(),
            "audioStreams": t.array(
                t.proxy(renames["VideoFileDetailsAudioStreamOut"])
            ).optional(),
            "fileName": t.string().optional(),
            "container": t.string().optional(),
            "fileSize": t.string().optional(),
            "bitrateBps": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFileDetailsOut"])
    types["VideoLiveStreamingDetailsIn"] = t.struct(
        {
            "actualStartTime": t.string().optional(),
            "activeLiveChatId": t.string().optional(),
            "scheduledEndTime": t.string().optional(),
            "concurrentViewers": t.string().optional(),
            "actualEndTime": t.string().optional(),
            "scheduledStartTime": t.string().optional(),
        }
    ).named(renames["VideoLiveStreamingDetailsIn"])
    types["VideoLiveStreamingDetailsOut"] = t.struct(
        {
            "actualStartTime": t.string().optional(),
            "activeLiveChatId": t.string().optional(),
            "scheduledEndTime": t.string().optional(),
            "concurrentViewers": t.string().optional(),
            "actualEndTime": t.string().optional(),
            "scheduledStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoLiveStreamingDetailsOut"])
    types["ActivityIn"] = t.struct(
        {
            "contentDetails": t.proxy(renames["ActivityContentDetailsIn"]).optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["ActivitySnippetIn"]).optional(),
        }
    ).named(renames["ActivityIn"])
    types["ActivityOut"] = t.struct(
        {
            "contentDetails": t.proxy(renames["ActivityContentDetailsOut"]).optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["ActivitySnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityOut"])
    types["VideoCategoryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["VideoCategorySnippetIn"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["VideoCategoryIn"])
    types["VideoCategoryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["VideoCategorySnippetOut"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCategoryOut"])
    types["MembershipsLevelSnippetIn"] = t.struct(
        {
            "levelDetails": t.proxy(renames["LevelDetailsIn"]).optional(),
            "creatorChannelId": t.string().optional(),
        }
    ).named(renames["MembershipsLevelSnippetIn"])
    types["MembershipsLevelSnippetOut"] = t.struct(
        {
            "levelDetails": t.proxy(renames["LevelDetailsOut"]).optional(),
            "creatorChannelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsLevelSnippetOut"])
    types["ChannelBrandingSettingsIn"] = t.struct(
        {
            "channel": t.proxy(renames["ChannelSettingsIn"]).optional(),
            "image": t.proxy(renames["ImageSettingsIn"]).optional(),
            "hints": t.array(t.proxy(renames["PropertyValueIn"])).optional(),
            "watch": t.proxy(renames["WatchSettingsIn"]).optional(),
        }
    ).named(renames["ChannelBrandingSettingsIn"])
    types["ChannelBrandingSettingsOut"] = t.struct(
        {
            "channel": t.proxy(renames["ChannelSettingsOut"]).optional(),
            "image": t.proxy(renames["ImageSettingsOut"]).optional(),
            "hints": t.array(t.proxy(renames["PropertyValueOut"])).optional(),
            "watch": t.proxy(renames["WatchSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelBrandingSettingsOut"])
    types["MemberIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["MemberSnippetIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["MemberIn"])
    types["MemberOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["MemberSnippetOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberOut"])
    types["PlaylistSnippetIn"] = t.struct(
        {
            "channelId": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "publishedAt": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "localized": t.proxy(renames["PlaylistLocalizationIn"]).optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "thumbnailVideoId": t.string().optional(),
            "channelTitle": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["PlaylistSnippetIn"])
    types["PlaylistSnippetOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "publishedAt": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "localized": t.proxy(renames["PlaylistLocalizationOut"]).optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "thumbnailVideoId": t.string().optional(),
            "channelTitle": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistSnippetOut"])
    types["ThumbnailSetResponseIn"] = t.struct(
        {
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["ThumbnailDetailsIn"])).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ThumbnailSetResponseIn"])
    types["ThumbnailSetResponseOut"] = t.struct(
        {
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["ThumbnailDetailsOut"])).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailSetResponseOut"])
    types["LevelDetailsIn"] = t.struct({"displayName": t.string().optional()}).named(
        renames["LevelDetailsIn"]
    )
    types["LevelDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LevelDetailsOut"])
    types["ChannelSectionIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "contentDetails": t.proxy(
                renames["ChannelSectionContentDetailsIn"]
            ).optional(),
            "targeting": t.proxy(renames["ChannelSectionTargetingIn"]).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["ChannelSectionSnippetIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ChannelSectionIn"])
    types["ChannelSectionOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "contentDetails": t.proxy(
                renames["ChannelSectionContentDetailsOut"]
            ).optional(),
            "targeting": t.proxy(renames["ChannelSectionTargetingOut"]).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["ChannelSectionSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionOut"])
    types["LiveChatModeratorListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["LiveChatModeratorIn"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
        }
    ).named(renames["LiveChatModeratorListResponseIn"])
    types["LiveChatModeratorListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["LiveChatModeratorOut"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatModeratorListResponseOut"])
    types["PlaylistLocalizationIn"] = t.struct(
        {"title": t.string().optional(), "description": t.string().optional()}
    ).named(renames["PlaylistLocalizationIn"])
    types["PlaylistLocalizationOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistLocalizationOut"])
    types["LiveStreamStatusIn"] = t.struct(
        {
            "streamStatus": t.string(),
            "healthStatus": t.proxy(renames["LiveStreamHealthStatusIn"]).optional(),
        }
    ).named(renames["LiveStreamStatusIn"])
    types["LiveStreamStatusOut"] = t.struct(
        {
            "streamStatus": t.string(),
            "healthStatus": t.proxy(renames["LiveStreamHealthStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamStatusOut"])
    types["ActivitySnippetIn"] = t.struct(
        {
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "channelId": t.string().optional(),
            "publishedAt": t.string().optional(),
            "channelTitle": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "groupId": t.string().optional(),
        }
    ).named(renames["ActivitySnippetIn"])
    types["ActivitySnippetOut"] = t.struct(
        {
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "channelId": t.string().optional(),
            "publishedAt": t.string().optional(),
            "channelTitle": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "groupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitySnippetOut"])
    types["TestItemIn"] = t.struct(
        {
            "snippet": t.proxy(renames["TestItemTestItemSnippetIn"]),
            "gaia": t.string(),
            "featuredPart": t.boolean(),
            "id": t.string(),
        }
    ).named(renames["TestItemIn"])
    types["TestItemOut"] = t.struct(
        {
            "snippet": t.proxy(renames["TestItemTestItemSnippetOut"]),
            "gaia": t.string(),
            "featuredPart": t.boolean(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestItemOut"])
    types["LocalizedStringIn"] = t.struct(
        {"value": t.string(), "language": t.string()}
    ).named(renames["LocalizedStringIn"])
    types["LocalizedStringOut"] = t.struct(
        {
            "value": t.string(),
            "language": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedStringOut"])
    types["ChannelStatusIn"] = t.struct(
        {
            "privacyStatus": t.string().optional(),
            "madeForKids": t.boolean(),
            "selfDeclaredMadeForKids": t.boolean(),
            "longUploadsStatus": t.string().optional(),
            "isLinked": t.boolean().optional(),
        }
    ).named(renames["ChannelStatusIn"])
    types["ChannelStatusOut"] = t.struct(
        {
            "privacyStatus": t.string().optional(),
            "madeForKids": t.boolean(),
            "selfDeclaredMadeForKids": t.boolean(),
            "longUploadsStatus": t.string().optional(),
            "isLinked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelStatusOut"])
    types["ChannelConversionPingIn"] = t.struct(
        {"context": t.string().optional(), "conversionUrl": t.string().optional()}
    ).named(renames["ChannelConversionPingIn"])
    types["ChannelConversionPingOut"] = t.struct(
        {
            "context": t.string().optional(),
            "conversionUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelConversionPingOut"])
    types["VideoFileDetailsVideoStreamIn"] = t.struct(
        {
            "rotation": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "heightPixels": t.integer().optional(),
            "bitrateBps": t.string().optional(),
            "codec": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "vendor": t.string().optional(),
            "frameRateFps": t.number().optional(),
        }
    ).named(renames["VideoFileDetailsVideoStreamIn"])
    types["VideoFileDetailsVideoStreamOut"] = t.struct(
        {
            "rotation": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "heightPixels": t.integer().optional(),
            "bitrateBps": t.string().optional(),
            "codec": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "vendor": t.string().optional(),
            "frameRateFps": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFileDetailsVideoStreamOut"])
    types["MonitorStreamInfoIn"] = t.struct(
        {
            "broadcastStreamDelayMs": t.integer().optional(),
            "enableMonitorStream": t.boolean().optional(),
            "embedHtml": t.string().optional(),
        }
    ).named(renames["MonitorStreamInfoIn"])
    types["MonitorStreamInfoOut"] = t.struct(
        {
            "broadcastStreamDelayMs": t.integer().optional(),
            "enableMonitorStream": t.boolean().optional(),
            "embedHtml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitorStreamInfoOut"])
    types["VideoGetRatingResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoRatingIn"])).optional(),
        }
    ).named(renames["VideoGetRatingResponseIn"])
    types["VideoGetRatingResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoRatingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoGetRatingResponseOut"])
    types["ActivityContentDetailsLikeIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsLikeIn"])
    types["ActivityContentDetailsLikeOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsLikeOut"])
    types["ActivityContentDetailsSubscriptionIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsSubscriptionIn"])
    types["ActivityContentDetailsSubscriptionOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsSubscriptionOut"])
    types["LiveChatMessageRetractedDetailsIn"] = t.struct(
        {"retractedMessageId": t.string()}
    ).named(renames["LiveChatMessageRetractedDetailsIn"])
    types["LiveChatMessageRetractedDetailsOut"] = t.struct(
        {
            "retractedMessageId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageRetractedDetailsOut"])
    types["LiveChatModeratorSnippetIn"] = t.struct(
        {
            "liveChatId": t.string().optional(),
            "moderatorDetails": t.proxy(renames["ChannelProfileDetailsIn"]).optional(),
        }
    ).named(renames["LiveChatModeratorSnippetIn"])
    types["LiveChatModeratorSnippetOut"] = t.struct(
        {
            "liveChatId": t.string().optional(),
            "moderatorDetails": t.proxy(renames["ChannelProfileDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatModeratorSnippetOut"])
    types["ImageSettingsIn"] = t.struct(
        {
            "bannerTvLowImageUrl": t.string().optional(),
            "bannerMobileLowImageUrl": t.string().optional(),
            "backgroundImageUrl": t.proxy(renames["LocalizedPropertyIn"]).optional(),
            "bannerTabletLowImageUrl": t.string().optional(),
            "bannerTabletHdImageUrl": t.string().optional(),
            "bannerTvHighImageUrl": t.string().optional(),
            "largeBrandedBannerImageImapScript": t.proxy(
                renames["LocalizedPropertyIn"]
            ).optional(),
            "bannerTvImageUrl": t.string().optional(),
            "smallBrandedBannerImageUrl": t.proxy(
                renames["LocalizedPropertyIn"]
            ).optional(),
            "bannerMobileHdImageUrl": t.string().optional(),
            "bannerMobileImageUrl": t.string().optional(),
            "watchIconImageUrl": t.string(),
            "bannerExternalUrl": t.string().optional(),
            "smallBrandedBannerImageImapScript": t.proxy(
                renames["LocalizedPropertyIn"]
            ).optional(),
            "largeBrandedBannerImageUrl": t.proxy(
                renames["LocalizedPropertyIn"]
            ).optional(),
            "bannerTvMediumImageUrl": t.string().optional(),
            "bannerTabletImageUrl": t.string().optional(),
            "bannerMobileExtraHdImageUrl": t.string().optional(),
            "bannerTabletExtraHdImageUrl": t.string().optional(),
            "trackingImageUrl": t.string().optional(),
            "bannerImageUrl": t.string().optional(),
            "bannerMobileMediumHdImageUrl": t.string().optional(),
        }
    ).named(renames["ImageSettingsIn"])
    types["ImageSettingsOut"] = t.struct(
        {
            "bannerTvLowImageUrl": t.string().optional(),
            "bannerMobileLowImageUrl": t.string().optional(),
            "backgroundImageUrl": t.proxy(renames["LocalizedPropertyOut"]).optional(),
            "bannerTabletLowImageUrl": t.string().optional(),
            "bannerTabletHdImageUrl": t.string().optional(),
            "bannerTvHighImageUrl": t.string().optional(),
            "largeBrandedBannerImageImapScript": t.proxy(
                renames["LocalizedPropertyOut"]
            ).optional(),
            "bannerTvImageUrl": t.string().optional(),
            "smallBrandedBannerImageUrl": t.proxy(
                renames["LocalizedPropertyOut"]
            ).optional(),
            "bannerMobileHdImageUrl": t.string().optional(),
            "bannerMobileImageUrl": t.string().optional(),
            "watchIconImageUrl": t.string(),
            "bannerExternalUrl": t.string().optional(),
            "smallBrandedBannerImageImapScript": t.proxy(
                renames["LocalizedPropertyOut"]
            ).optional(),
            "largeBrandedBannerImageUrl": t.proxy(
                renames["LocalizedPropertyOut"]
            ).optional(),
            "bannerTvMediumImageUrl": t.string().optional(),
            "bannerTabletImageUrl": t.string().optional(),
            "bannerMobileExtraHdImageUrl": t.string().optional(),
            "bannerTabletExtraHdImageUrl": t.string().optional(),
            "trackingImageUrl": t.string().optional(),
            "bannerImageUrl": t.string().optional(),
            "bannerMobileMediumHdImageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageSettingsOut"])
    types["LiveStreamSnippetIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "channelId": t.string().optional(),
            "isDefaultStream": t.boolean(),
            "publishedAt": t.string().optional(),
        }
    ).named(renames["LiveStreamSnippetIn"])
    types["LiveStreamSnippetOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "channelId": t.string().optional(),
            "isDefaultStream": t.boolean(),
            "publishedAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamSnippetOut"])
    types["LiveStreamIn"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
            "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
            "etag": t.string().optional(),
            "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
            "contentDetails": t.proxy(renames["LiveStreamContentDetailsIn"]).optional(),
        }
    ).named(renames["LiveStreamIn"])
    types["LiveStreamOut"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["LiveStreamSnippetOut"]).optional(),
            "status": t.proxy(renames["LiveStreamStatusOut"]).optional(),
            "etag": t.string().optional(),
            "cdn": t.proxy(renames["CdnSettingsOut"]).optional(),
            "contentDetails": t.proxy(
                renames["LiveStreamContentDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamOut"])
    types["ChannelProfileDetailsIn"] = t.struct(
        {
            "channelId": t.string().optional(),
            "channelUrl": t.string().optional(),
            "profileImageUrl": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ChannelProfileDetailsIn"])
    types["ChannelProfileDetailsOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "channelUrl": t.string().optional(),
            "profileImageUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelProfileDetailsOut"])
    types["LiveChatSuperChatDetailsIn"] = t.struct(
        {
            "userComment": t.string().optional(),
            "currency": t.string().optional(),
            "amountMicros": t.string().optional(),
            "amountDisplayString": t.string().optional(),
            "tier": t.integer().optional(),
        }
    ).named(renames["LiveChatSuperChatDetailsIn"])
    types["LiveChatSuperChatDetailsOut"] = t.struct(
        {
            "userComment": t.string().optional(),
            "currency": t.string().optional(),
            "amountMicros": t.string().optional(),
            "amountDisplayString": t.string().optional(),
            "tier": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatSuperChatDetailsOut"])
    types["MembershipsLevelListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["MembershipsLevelIn"])).optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
        }
    ).named(renames["MembershipsLevelListResponseIn"])
    types["MembershipsLevelListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["MembershipsLevelOut"])).optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsLevelListResponseOut"])
    types["MembershipsDurationAtLevelIn"] = t.struct(
        {
            "memberTotalDurationMonths": t.integer().optional(),
            "memberSince": t.string().optional(),
            "level": t.string().optional(),
        }
    ).named(renames["MembershipsDurationAtLevelIn"])
    types["MembershipsDurationAtLevelOut"] = t.struct(
        {
            "memberTotalDurationMonths": t.integer().optional(),
            "memberSince": t.string().optional(),
            "level": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsDurationAtLevelOut"])
    types["LiveChatMessageDeletedDetailsIn"] = t.struct(
        {"deletedMessageId": t.string()}
    ).named(renames["LiveChatMessageDeletedDetailsIn"])
    types["LiveChatMessageDeletedDetailsOut"] = t.struct(
        {
            "deletedMessageId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageDeletedDetailsOut"])
    types["LiveBroadcastSnippetIn"] = t.struct(
        {
            "liveChatId": t.string().optional(),
            "description": t.string().optional(),
            "actualStartTime": t.string().optional(),
            "title": t.string().optional(),
            "actualEndTime": t.string().optional(),
            "isDefaultBroadcast": t.boolean().optional(),
            "scheduledStartTime": t.string().optional(),
            "scheduledEndTime": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "publishedAt": t.string().optional(),
            "channelId": t.string().optional(),
        }
    ).named(renames["LiveBroadcastSnippetIn"])
    types["LiveBroadcastSnippetOut"] = t.struct(
        {
            "liveChatId": t.string().optional(),
            "description": t.string().optional(),
            "actualStartTime": t.string().optional(),
            "title": t.string().optional(),
            "actualEndTime": t.string().optional(),
            "isDefaultBroadcast": t.boolean().optional(),
            "scheduledStartTime": t.string().optional(),
            "scheduledEndTime": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "publishedAt": t.string().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastSnippetOut"])
    types["ChannelListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "prevPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["ChannelIn"])),
            "kind": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "eventId": t.string().optional(),
        }
    ).named(renames["ChannelListResponseIn"])
    types["ChannelListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "prevPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["ChannelOut"])),
            "kind": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelListResponseOut"])
    types["ResourceIdIn"] = t.struct(
        {
            "channelId": t.string().optional(),
            "playlistId": t.string().optional(),
            "kind": t.string().optional(),
            "videoId": t.string().optional(),
        }
    ).named(renames["ResourceIdIn"])
    types["ResourceIdOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "playlistId": t.string().optional(),
            "kind": t.string().optional(),
            "videoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceIdOut"])
    types["LocalizedPropertyIn"] = t.struct(
        {
            "localized": t.array(t.proxy(renames["LocalizedStringIn"])),
            "defaultLanguage": t.proxy(renames["LanguageTagIn"]).optional(),
            "default": t.string(),
        }
    ).named(renames["LocalizedPropertyIn"])
    types["LocalizedPropertyOut"] = t.struct(
        {
            "localized": t.array(t.proxy(renames["LocalizedStringOut"])),
            "defaultLanguage": t.proxy(renames["LanguageTagOut"]).optional(),
            "default": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedPropertyOut"])
    types["VideoProjectDetailsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VideoProjectDetailsIn"]
    )
    types["VideoProjectDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VideoProjectDetailsOut"])
    types["PlaylistItemListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["PlaylistItemIn"])).optional(),
        }
    ).named(renames["PlaylistItemListResponseIn"])
    types["PlaylistItemListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["PlaylistItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemListResponseOut"])
    types["MemberSnippetIn"] = t.struct(
        {
            "memberDetails": t.proxy(renames["ChannelProfileDetailsIn"]).optional(),
            "creatorChannelId": t.string().optional(),
            "membershipsDetails": t.proxy(renames["MembershipsDetailsIn"]).optional(),
        }
    ).named(renames["MemberSnippetIn"])
    types["MemberSnippetOut"] = t.struct(
        {
            "memberDetails": t.proxy(renames["ChannelProfileDetailsOut"]).optional(),
            "creatorChannelId": t.string().optional(),
            "membershipsDetails": t.proxy(renames["MembershipsDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberSnippetOut"])
    types["LiveChatModeratorIn"] = t.struct(
        {
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatModeratorSnippetIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiveChatModeratorIn"])
    types["LiveChatModeratorOut"] = t.struct(
        {
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatModeratorSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatModeratorOut"])
    types["MemberListResponseIn"] = t.struct(
        {
            "pageInfo": t.proxy(renames["PageInfoIn"]),
            "items": t.array(t.proxy(renames["MemberIn"])).optional(),
            "etag": t.string().optional(),
            "eventId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
        }
    ).named(renames["MemberListResponseIn"])
    types["MemberListResponseOut"] = t.struct(
        {
            "pageInfo": t.proxy(renames["PageInfoOut"]),
            "items": t.array(t.proxy(renames["MemberOut"])).optional(),
            "etag": t.string().optional(),
            "eventId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberListResponseOut"])
    types["PageInfoIn"] = t.struct(
        {
            "resultsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
        }
    ).named(renames["PageInfoIn"])
    types["PageInfoOut"] = t.struct(
        {
            "resultsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageInfoOut"])
    types["TokenPaginationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TokenPaginationIn"]
    )
    types["TokenPaginationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TokenPaginationOut"])
    types["SearchResultSnippetIn"] = t.struct(
        {
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "description": t.string().optional(),
            "channelId": t.string().optional(),
            "liveBroadcastContent": t.string().optional(),
            "title": t.string().optional(),
            "publishedAt": t.string().optional(),
            "channelTitle": t.string().optional(),
        }
    ).named(renames["SearchResultSnippetIn"])
    types["SearchResultSnippetOut"] = t.struct(
        {
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "description": t.string().optional(),
            "channelId": t.string().optional(),
            "liveBroadcastContent": t.string().optional(),
            "title": t.string().optional(),
            "publishedAt": t.string().optional(),
            "channelTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultSnippetOut"])
    types["ChannelBannerResourceIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string(),
            "url": t.string().optional(),
        }
    ).named(renames["ChannelBannerResourceIn"])
    types["ChannelBannerResourceOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelBannerResourceOut"])
    types["LiveStreamHealthStatusIn"] = t.struct(
        {
            "configurationIssues": t.array(
                t.proxy(renames["LiveStreamConfigurationIssueIn"])
            ).optional(),
            "lastUpdateTimeSeconds": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["LiveStreamHealthStatusIn"])
    types["LiveStreamHealthStatusOut"] = t.struct(
        {
            "configurationIssues": t.array(
                t.proxy(renames["LiveStreamConfigurationIssueOut"])
            ).optional(),
            "lastUpdateTimeSeconds": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamHealthStatusOut"])
    types["ThumbnailDetailsIn"] = t.struct(
        {
            "maxres": t.proxy(renames["ThumbnailIn"]).optional(),
            "standard": t.proxy(renames["ThumbnailIn"]).optional(),
            "high": t.proxy(renames["ThumbnailIn"]).optional(),
            "medium": t.proxy(renames["ThumbnailIn"]).optional(),
            "default": t.proxy(renames["ThumbnailIn"]).optional(),
        }
    ).named(renames["ThumbnailDetailsIn"])
    types["ThumbnailDetailsOut"] = t.struct(
        {
            "maxres": t.proxy(renames["ThumbnailOut"]).optional(),
            "standard": t.proxy(renames["ThumbnailOut"]).optional(),
            "high": t.proxy(renames["ThumbnailOut"]).optional(),
            "medium": t.proxy(renames["ThumbnailOut"]).optional(),
            "default": t.proxy(renames["ThumbnailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailDetailsOut"])
    types["I18nRegionListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["I18nRegionIn"])).optional(),
        }
    ).named(renames["I18nRegionListResponseIn"])
    types["I18nRegionListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["I18nRegionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nRegionListResponseOut"])
    types["PropertyValueIn"] = t.struct(
        {"value": t.string().optional(), "property": t.string().optional()}
    ).named(renames["PropertyValueIn"])
    types["PropertyValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "property": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyValueOut"])
    types["AbuseReportIn"] = t.struct(
        {
            "relatedEntities": t.array(t.proxy(renames["RelatedEntityIn"])),
            "abuseTypes": t.array(t.proxy(renames["AbuseTypeIn"])),
            "description": t.string(),
            "subject": t.proxy(renames["EntityIn"]),
        }
    ).named(renames["AbuseReportIn"])
    types["AbuseReportOut"] = t.struct(
        {
            "relatedEntities": t.array(t.proxy(renames["RelatedEntityOut"])),
            "abuseTypes": t.array(t.proxy(renames["AbuseTypeOut"])),
            "description": t.string(),
            "subject": t.proxy(renames["EntityOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbuseReportOut"])
    types["LiveChatFanFundingEventDetailsIn"] = t.struct(
        {
            "userComment": t.string().optional(),
            "amountMicros": t.string().optional(),
            "currency": t.string().optional(),
            "amountDisplayString": t.string().optional(),
        }
    ).named(renames["LiveChatFanFundingEventDetailsIn"])
    types["LiveChatFanFundingEventDetailsOut"] = t.struct(
        {
            "userComment": t.string().optional(),
            "amountMicros": t.string().optional(),
            "currency": t.string().optional(),
            "amountDisplayString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatFanFundingEventDetailsOut"])
    types["ChannelAuditDetailsIn"] = t.struct(
        {
            "copyrightStrikesGoodStanding": t.boolean().optional(),
            "communityGuidelinesGoodStanding": t.boolean().optional(),
            "contentIdClaimsGoodStanding": t.boolean().optional(),
        }
    ).named(renames["ChannelAuditDetailsIn"])
    types["ChannelAuditDetailsOut"] = t.struct(
        {
            "copyrightStrikesGoodStanding": t.boolean().optional(),
            "communityGuidelinesGoodStanding": t.boolean().optional(),
            "contentIdClaimsGoodStanding": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelAuditDetailsOut"])
    types["CommentListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "items": t.array(t.proxy(renames["CommentIn"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "eventId": t.string().optional(),
        }
    ).named(renames["CommentListResponseIn"])
    types["CommentListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "items": t.array(t.proxy(renames["CommentOut"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentListResponseOut"])
    types["SubscriptionSnippetIn"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "channelTitle": t.string().optional(),
            "description": t.string().optional(),
            "channelId": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "title": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
        }
    ).named(renames["SubscriptionSnippetIn"])
    types["SubscriptionSnippetOut"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "channelTitle": t.string().optional(),
            "description": t.string().optional(),
            "channelId": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "title": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionSnippetOut"])
    types["VideoRecordingDetailsIn"] = t.struct(
        {
            "locationDescription": t.string().optional(),
            "location": t.proxy(renames["GeoPointIn"]).optional(),
            "recordingDate": t.string().optional(),
        }
    ).named(renames["VideoRecordingDetailsIn"])
    types["VideoRecordingDetailsOut"] = t.struct(
        {
            "locationDescription": t.string().optional(),
            "location": t.proxy(renames["GeoPointOut"]).optional(),
            "recordingDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoRecordingDetailsOut"])
    types["PlaylistPlayerIn"] = t.struct({"embedHtml": t.string().optional()}).named(
        renames["PlaylistPlayerIn"]
    )
    types["PlaylistPlayerOut"] = t.struct(
        {
            "embedHtml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistPlayerOut"])
    types["ChannelContentDetailsIn"] = t.struct(
        {
            "relatedPlaylists": t.struct(
                {
                    "watchHistory": t.string().optional(),
                    "likes": t.string().optional(),
                    "favorites": t.string().optional(),
                    "uploads": t.string().optional(),
                    "watchLater": t.string().optional(),
                }
            )
        }
    ).named(renames["ChannelContentDetailsIn"])
    types["ChannelContentDetailsOut"] = t.struct(
        {
            "relatedPlaylists": t.struct(
                {
                    "watchHistory": t.string().optional(),
                    "likes": t.string().optional(),
                    "favorites": t.string().optional(),
                    "uploads": t.string().optional(),
                    "watchLater": t.string().optional(),
                }
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelContentDetailsOut"])
    types["LiveStreamConfigurationIssueIn"] = t.struct(
        {
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "reason": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LiveStreamConfigurationIssueIn"])
    types["LiveStreamConfigurationIssueOut"] = t.struct(
        {
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "reason": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamConfigurationIssueOut"])
    types["ActivityContentDetailsCommentIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsCommentIn"])
    types["ActivityContentDetailsCommentOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsCommentOut"])
    types["ThirdPartyLinkListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["ThirdPartyLinkIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["ThirdPartyLinkListResponseIn"])
    types["ThirdPartyLinkListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["ThirdPartyLinkOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyLinkListResponseOut"])
    types["SubscriptionContentDetailsIn"] = t.struct(
        {
            "newItemCount": t.integer().optional(),
            "activityType": t.string().optional(),
            "totalItemCount": t.integer().optional(),
        }
    ).named(renames["SubscriptionContentDetailsIn"])
    types["SubscriptionContentDetailsOut"] = t.struct(
        {
            "newItemCount": t.integer().optional(),
            "activityType": t.string().optional(),
            "totalItemCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionContentDetailsOut"])
    types["SubscriptionListResponseIn"] = t.struct(
        {
            "pageInfo": t.proxy(renames["PageInfoIn"]),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "items": t.array(t.proxy(renames["SubscriptionIn"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "eventId": t.string().optional(),
        }
    ).named(renames["SubscriptionListResponseIn"])
    types["SubscriptionListResponseOut"] = t.struct(
        {
            "pageInfo": t.proxy(renames["PageInfoOut"]),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "items": t.array(t.proxy(renames["SubscriptionOut"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionListResponseOut"])
    types["AbuseTypeIn"] = t.struct({"id": t.string()}).named(renames["AbuseTypeIn"])
    types["AbuseTypeOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbuseTypeOut"])
    types["ActivityContentDetailsPlaylistItemIn"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
            "playlistItemId": t.string().optional(),
            "playlistId": t.string().optional(),
        }
    ).named(renames["ActivityContentDetailsPlaylistItemIn"])
    types["ActivityContentDetailsPlaylistItemOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "playlistItemId": t.string().optional(),
            "playlistId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsPlaylistItemOut"])
    types["GeoPointIn"] = t.struct(
        {
            "altitude": t.number().optional(),
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
        }
    ).named(renames["GeoPointIn"])
    types["GeoPointOut"] = t.struct(
        {
            "altitude": t.number().optional(),
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoPointOut"])
    types["SuperStickerMetadataIn"] = t.struct(
        {
            "stickerId": t.string().optional(),
            "altText": t.string().optional(),
            "altTextLanguage": t.string().optional(),
        }
    ).named(renames["SuperStickerMetadataIn"])
    types["SuperStickerMetadataOut"] = t.struct(
        {
            "stickerId": t.string().optional(),
            "altText": t.string().optional(),
            "altTextLanguage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperStickerMetadataOut"])
    types["VideoPlayerIn"] = t.struct(
        {
            "embedHtml": t.string().optional(),
            "embedWidth": t.string().optional(),
            "embedHeight": t.string(),
        }
    ).named(renames["VideoPlayerIn"])
    types["VideoPlayerOut"] = t.struct(
        {
            "embedHtml": t.string().optional(),
            "embedWidth": t.string().optional(),
            "embedHeight": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerOut"])
    types["LiveBroadcastListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "items": t.array(t.proxy(renames["LiveBroadcastIn"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "nextPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["LiveBroadcastListResponseIn"])
    types["LiveBroadcastListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "items": t.array(t.proxy(renames["LiveBroadcastOut"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastListResponseOut"])
    types["I18nLanguageIn"] = t.struct(
        {
            "snippet": t.proxy(renames["I18nLanguageSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["I18nLanguageIn"])
    types["I18nLanguageOut"] = t.struct(
        {
            "snippet": t.proxy(renames["I18nLanguageSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nLanguageOut"])
    types["ChannelSectionTargetingIn"] = t.struct(
        {
            "languages": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "countries": t.array(t.string()).optional(),
        }
    ).named(renames["ChannelSectionTargetingIn"])
    types["ChannelSectionTargetingOut"] = t.struct(
        {
            "languages": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "countries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionTargetingOut"])
    types["LiveChatMessageIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "authorDetails": t.proxy(
                renames["LiveChatMessageAuthorDetailsIn"]
            ).optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatMessageSnippetIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiveChatMessageIn"])
    types["LiveChatMessageOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "authorDetails": t.proxy(
                renames["LiveChatMessageAuthorDetailsOut"]
            ).optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatMessageSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageOut"])
    types["VideoAgeGatingIn"] = t.struct(
        {
            "videoGameRating": t.string().optional(),
            "alcoholContent": t.boolean().optional(),
            "restricted": t.boolean().optional(),
        }
    ).named(renames["VideoAgeGatingIn"])
    types["VideoAgeGatingOut"] = t.struct(
        {
            "videoGameRating": t.string().optional(),
            "alcoholContent": t.boolean().optional(),
            "restricted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAgeGatingOut"])
    types["VideoContentDetailsRegionRestrictionIn"] = t.struct(
        {
            "blocked": t.array(t.string()).optional(),
            "allowed": t.array(t.string()).optional(),
        }
    ).named(renames["VideoContentDetailsRegionRestrictionIn"])
    types["VideoContentDetailsRegionRestrictionOut"] = t.struct(
        {
            "blocked": t.array(t.string()).optional(),
            "allowed": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoContentDetailsRegionRestrictionOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "contentDetails": t.proxy(
                renames["SubscriptionContentDetailsIn"]
            ).optional(),
            "subscriberSnippet": t.proxy(
                renames["SubscriptionSubscriberSnippetIn"]
            ).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["SubscriptionSnippetIn"]).optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "contentDetails": t.proxy(
                renames["SubscriptionContentDetailsOut"]
            ).optional(),
            "subscriberSnippet": t.proxy(
                renames["SubscriptionSubscriberSnippetOut"]
            ).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["SubscriptionSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["PlaylistContentDetailsIn"] = t.struct(
        {"itemCount": t.integer().optional()}
    ).named(renames["PlaylistContentDetailsIn"])
    types["PlaylistContentDetailsOut"] = t.struct(
        {
            "itemCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistContentDetailsOut"])
    types["VideoAbuseReportReasonListResponseIn"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoAbuseReportReasonIn"])).optional(),
        }
    ).named(renames["VideoAbuseReportReasonListResponseIn"])
    types["VideoAbuseReportReasonListResponseOut"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoAbuseReportReasonOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportReasonListResponseOut"])
    types["VideoCategorySnippetIn"] = t.struct(
        {
            "title": t.string().optional(),
            "assignable": t.boolean(),
            "channelId": t.string().optional(),
        }
    ).named(renames["VideoCategorySnippetIn"])
    types["VideoCategorySnippetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "assignable": t.boolean(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCategorySnippetOut"])
    types["ActivityContentDetailsUploadIn"] = t.struct(
        {"videoId": t.string().optional()}
    ).named(renames["ActivityContentDetailsUploadIn"])
    types["ActivityContentDetailsUploadOut"] = t.struct(
        {
            "videoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsUploadOut"])
    types["VideoRatingIn"] = t.struct(
        {"rating": t.string().optional(), "videoId": t.string().optional()}
    ).named(renames["VideoRatingIn"])
    types["VideoRatingOut"] = t.struct(
        {
            "rating": t.string().optional(),
            "videoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoRatingOut"])
    types["VideoSuggestionsIn"] = t.struct(
        {
            "editorSuggestions": t.array(t.string()).optional(),
            "tagSuggestions": t.array(
                t.proxy(renames["VideoSuggestionsTagSuggestionIn"])
            ).optional(),
            "processingHints": t.array(t.string()).optional(),
            "processingWarnings": t.array(t.string()).optional(),
            "processingErrors": t.array(t.string()).optional(),
        }
    ).named(renames["VideoSuggestionsIn"])
    types["VideoSuggestionsOut"] = t.struct(
        {
            "editorSuggestions": t.array(t.string()).optional(),
            "tagSuggestions": t.array(
                t.proxy(renames["VideoSuggestionsTagSuggestionOut"])
            ).optional(),
            "processingHints": t.array(t.string()).optional(),
            "processingWarnings": t.array(t.string()).optional(),
            "processingErrors": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoSuggestionsOut"])
    types["ActivityListResponseIn"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "prevPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ActivityIn"])),
        }
    ).named(renames["ActivityListResponseIn"])
    types["ActivityListResponseOut"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "prevPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ActivityOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityListResponseOut"])
    types["LiveChatBanSnippetIn"] = t.struct(
        {
            "banDurationSeconds": t.string().optional(),
            "liveChatId": t.string().optional(),
            "type": t.string().optional(),
            "bannedUserDetails": t.proxy(renames["ChannelProfileDetailsIn"]),
        }
    ).named(renames["LiveChatBanSnippetIn"])
    types["LiveChatBanSnippetOut"] = t.struct(
        {
            "banDurationSeconds": t.string().optional(),
            "liveChatId": t.string().optional(),
            "type": t.string().optional(),
            "bannedUserDetails": t.proxy(renames["ChannelProfileDetailsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatBanSnippetOut"])
    types["ActivityContentDetailsFavoriteIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsFavoriteIn"])
    types["ActivityContentDetailsFavoriteOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsFavoriteOut"])
    types["LiveBroadcastStatusIn"] = t.struct(
        {
            "liveBroadcastPriority": t.string().optional(),
            "recordingStatus": t.string().optional(),
            "lifeCycleStatus": t.string().optional(),
            "madeForKids": t.boolean().optional(),
            "selfDeclaredMadeForKids": t.boolean().optional(),
            "privacyStatus": t.string().optional(),
        }
    ).named(renames["LiveBroadcastStatusIn"])
    types["LiveBroadcastStatusOut"] = t.struct(
        {
            "liveBroadcastPriority": t.string().optional(),
            "recordingStatus": t.string().optional(),
            "lifeCycleStatus": t.string().optional(),
            "madeForKids": t.boolean().optional(),
            "selfDeclaredMadeForKids": t.boolean().optional(),
            "privacyStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastStatusOut"])
    types["ThumbnailIn"] = t.struct(
        {
            "url": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "url": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
    types["ChannelSectionContentDetailsIn"] = t.struct(
        {
            "playlists": t.array(t.string()).optional(),
            "channels": t.array(t.string()).optional(),
        }
    ).named(renames["ChannelSectionContentDetailsIn"])
    types["ChannelSectionContentDetailsOut"] = t.struct(
        {
            "playlists": t.array(t.string()).optional(),
            "channels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionContentDetailsOut"])
    types["LiveStreamListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["LiveStreamIn"])).optional(),
            "kind": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "nextPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]),
            "prevPageToken": t.string().optional(),
        }
    ).named(renames["LiveStreamListResponseIn"])
    types["LiveStreamListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["LiveStreamOut"])).optional(),
            "kind": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "nextPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]),
            "prevPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamListResponseOut"])
    types["ChannelConversionPingsIn"] = t.struct(
        {"pings": t.array(t.proxy(renames["ChannelConversionPingIn"])).optional()}
    ).named(renames["ChannelConversionPingsIn"])
    types["ChannelConversionPingsOut"] = t.struct(
        {
            "pings": t.array(t.proxy(renames["ChannelConversionPingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelConversionPingsOut"])
    types["InvideoPositionIn"] = t.struct(
        {"cornerPosition": t.string().optional(), "type": t.string().optional()}
    ).named(renames["InvideoPositionIn"])
    types["InvideoPositionOut"] = t.struct(
        {
            "cornerPosition": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvideoPositionOut"])
    types["CaptionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CaptionIn"])
    types["CaptionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["CaptionSnippetOut"]).optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaptionOut"])
    types["SuperChatEventListResponseIn"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "items": t.array(t.proxy(renames["SuperChatEventIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]),
            "eventId": t.string().optional(),
        }
    ).named(renames["SuperChatEventListResponseIn"])
    types["SuperChatEventListResponseOut"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "items": t.array(t.proxy(renames["SuperChatEventOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperChatEventListResponseOut"])

    functions = {}
    functions["membershipsLevelsList"] = youtube.get(
        "youtube/v3/membershipsLevels",
        t.struct({"part": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipsLevelListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["i18nRegionsList"] = youtube.get(
        "youtube/v3/i18nRegions",
        t.struct(
            {
                "part": t.string().optional(),
                "hl": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["I18nRegionListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["abuseReportsInsert"] = youtube.post(
        "youtube/v3/abuseReports",
        t.struct(
            {
                "part": t.string().optional(),
                "relatedEntities": t.array(t.proxy(renames["RelatedEntityIn"])),
                "abuseTypes": t.array(t.proxy(renames["AbuseTypeIn"])),
                "description": t.string(),
                "subject": t.proxy(renames["EntityIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AbuseReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["testsInsert"] = youtube.post(
        "youtube/v3/tests",
        t.struct(
            {
                "externalChannelId": t.string(),
                "part": t.string(),
                "snippet": t.proxy(renames["TestItemTestItemSnippetIn"]),
                "gaia": t.string(),
                "featuredPart": t.boolean(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentThreadsList"] = youtube.post(
        "youtube/v3/commentThreads",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "replies": t.proxy(renames["CommentThreadRepliesIn"]).optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentThreadSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentThreadsInsert"] = youtube.post(
        "youtube/v3/commentThreads",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "replies": t.proxy(renames["CommentThreadRepliesIn"]).optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentThreadSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thirdPartyLinksUpdate"] = youtube.get(
        "youtube/v3/thirdPartyLinks",
        t.struct(
            {
                "part": t.string().optional(),
                "linkingToken": t.string().optional(),
                "externalChannelId": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThirdPartyLinkListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thirdPartyLinksInsert"] = youtube.get(
        "youtube/v3/thirdPartyLinks",
        t.struct(
            {
                "part": t.string().optional(),
                "linkingToken": t.string().optional(),
                "externalChannelId": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThirdPartyLinkListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thirdPartyLinksDelete"] = youtube.get(
        "youtube/v3/thirdPartyLinks",
        t.struct(
            {
                "part": t.string().optional(),
                "linkingToken": t.string().optional(),
                "externalChannelId": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThirdPartyLinkListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thirdPartyLinksList"] = youtube.get(
        "youtube/v3/thirdPartyLinks",
        t.struct(
            {
                "part": t.string().optional(),
                "linkingToken": t.string().optional(),
                "externalChannelId": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThirdPartyLinkListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsInsert"] = youtube.put(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "part": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsDownload"] = youtube.put(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "part": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsList"] = youtube.put(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "part": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsDelete"] = youtube.put(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "part": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsUpdate"] = youtube.put(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "part": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistsUpdate"] = youtube.get(
        "youtube/v3/playlists",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "mine": t.boolean().optional(),
                "id": t.string().optional(),
                "channelId": t.string().optional(),
                "part": t.string().optional(),
                "pageToken": t.string().optional(),
                "hl": t.string().optional(),
                "maxResults": t.integer().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistsDelete"] = youtube.get(
        "youtube/v3/playlists",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "mine": t.boolean().optional(),
                "id": t.string().optional(),
                "channelId": t.string().optional(),
                "part": t.string().optional(),
                "pageToken": t.string().optional(),
                "hl": t.string().optional(),
                "maxResults": t.integer().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistsInsert"] = youtube.get(
        "youtube/v3/playlists",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "mine": t.boolean().optional(),
                "id": t.string().optional(),
                "channelId": t.string().optional(),
                "part": t.string().optional(),
                "pageToken": t.string().optional(),
                "hl": t.string().optional(),
                "maxResults": t.integer().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistsList"] = youtube.get(
        "youtube/v3/playlists",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "mine": t.boolean().optional(),
                "id": t.string().optional(),
                "channelId": t.string().optional(),
                "part": t.string().optional(),
                "pageToken": t.string().optional(),
                "hl": t.string().optional(),
                "maxResults": t.integer().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["watermarksSet"] = youtube.post(
        "youtube/v3/watermarks/unset",
        t.struct(
            {
                "channelId": t.string(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["watermarksUnset"] = youtube.post(
        "youtube/v3/watermarks/unset",
        t.struct(
            {
                "channelId": t.string(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thumbnailsSet"] = youtube.post(
        "youtube/v3/thumbnails/set",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "videoId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThumbnailSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videoCategoriesList"] = youtube.get(
        "youtube/v3/videoCategories",
        t.struct(
            {
                "regionCode": t.string(),
                "id": t.string().optional(),
                "hl": t.string(),
                "part": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoCategoryListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videoAbuseReportReasonsList"] = youtube.get(
        "youtube/v3/videoAbuseReportReasons",
        t.struct(
            {
                "hl": t.string(),
                "part": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoAbuseReportReasonListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["youtubeV3UpdateCommentThreads"] = youtube.put(
        "youtube/v3/commentThreads",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "replies": t.proxy(renames["CommentThreadRepliesIn"]).optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentThreadSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelSectionsInsert"] = youtube.put(
        "youtube/v3/channelSections",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["ChannelSectionContentDetailsIn"]
                ).optional(),
                "targeting": t.proxy(renames["ChannelSectionTargetingIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["ChannelSectionSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelSectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelSectionsList"] = youtube.put(
        "youtube/v3/channelSections",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["ChannelSectionContentDetailsIn"]
                ).optional(),
                "targeting": t.proxy(renames["ChannelSectionTargetingIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["ChannelSectionSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelSectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelSectionsDelete"] = youtube.put(
        "youtube/v3/channelSections",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["ChannelSectionContentDetailsIn"]
                ).optional(),
                "targeting": t.proxy(renames["ChannelSectionTargetingIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["ChannelSectionSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelSectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelSectionsUpdate"] = youtube.put(
        "youtube/v3/channelSections",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["ChannelSectionContentDetailsIn"]
                ).optional(),
                "targeting": t.proxy(renames["ChannelSectionTargetingIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["ChannelSectionSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelSectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsMarkAsSpam"] = youtube.post(
        "youtube/v3/comments",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsList"] = youtube.post(
        "youtube/v3/comments",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsSetModerationStatus"] = youtube.post(
        "youtube/v3/comments",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsDelete"] = youtube.post(
        "youtube/v3/comments",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsUpdate"] = youtube.post(
        "youtube/v3/comments",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsInsert"] = youtube.post(
        "youtube/v3/comments",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["superChatEventsList"] = youtube.get(
        "youtube/v3/superChatEvents",
        t.struct(
            {
                "hl": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "part": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SuperChatEventListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelBannersInsert"] = youtube.post(
        "youtube/v3/channelBanners/insert",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "channelId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelBannerResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelsUpdate"] = youtube.get(
        "youtube/v3/channels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "id": t.string().optional(),
                "managedByMe": t.boolean().optional(),
                "part": t.string().optional(),
                "mySubscribers": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "forUsername": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "hl": t.string().optional(),
                "mine": t.boolean().optional(),
                "categoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelsList"] = youtube.get(
        "youtube/v3/channels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "id": t.string().optional(),
                "managedByMe": t.boolean().optional(),
                "part": t.string().optional(),
                "mySubscribers": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "forUsername": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "hl": t.string().optional(),
                "mine": t.boolean().optional(),
                "categoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveStreamsUpdate"] = youtube.post(
        "youtube/v3/liveStreams",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
                "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
                "etag": t.string().optional(),
                "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["LiveStreamContentDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveStreamsList"] = youtube.post(
        "youtube/v3/liveStreams",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
                "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
                "etag": t.string().optional(),
                "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["LiveStreamContentDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveStreamsDelete"] = youtube.post(
        "youtube/v3/liveStreams",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
                "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
                "etag": t.string().optional(),
                "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["LiveStreamContentDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveStreamsInsert"] = youtube.post(
        "youtube/v3/liveStreams",
        t.struct(
            {
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
                "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
                "etag": t.string().optional(),
                "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["LiveStreamContentDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["membersList"] = youtube.get(
        "youtube/v3/members",
        t.struct(
            {
                "part": t.string().optional(),
                "mode": t.string().optional(),
                "filterByMemberChannelId": t.string().optional(),
                "hasAccessToLevel": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MemberListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatMessagesList"] = youtube.post(
        "youtube/v3/liveChat/messages",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "authorDetails": t.proxy(
                    renames["LiveChatMessageAuthorDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["LiveChatMessageSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatMessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatMessagesDelete"] = youtube.post(
        "youtube/v3/liveChat/messages",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "authorDetails": t.proxy(
                    renames["LiveChatMessageAuthorDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["LiveChatMessageSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatMessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatMessagesInsert"] = youtube.post(
        "youtube/v3/liveChat/messages",
        t.struct(
            {
                "part": t.string().optional(),
                "etag": t.string().optional(),
                "authorDetails": t.proxy(
                    renames["LiveChatMessageAuthorDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["LiveChatMessageSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatMessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["searchList"] = youtube.get(
        "youtube/v3/search",
        t.struct(
            {
                "channelType": t.string().optional(),
                "publishedBefore": t.string().optional(),
                "videoCategoryId": t.string().optional(),
                "videoCaption": t.string().optional(),
                "safeSearch": t.string().optional(),
                "locationRadius": t.string().optional(),
                "videoLicense": t.string().optional(),
                "publishedAfter": t.string().optional(),
                "videoDimension": t.string().optional(),
                "forContentOwner": t.boolean().optional(),
                "videoEmbeddable": t.string().optional(),
                "relatedToVideoId": t.string().optional(),
                "part": t.string().optional(),
                "pageToken": t.string().optional(),
                "videoType": t.string().optional(),
                "channelId": t.string().optional(),
                "eventType": t.string().optional(),
                "forDeveloper": t.boolean().optional(),
                "order": t.string().optional(),
                "location": t.string().optional(),
                "relevanceLanguage": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "maxResults": t.integer().optional(),
                "videoDuration": t.string().optional(),
                "topicId": t.string().optional(),
                "type": t.string().optional(),
                "forMine": t.boolean().optional(),
                "q": t.string().optional(),
                "videoSyndicated": t.string().optional(),
                "regionCode": t.string().optional(),
                "videoDefinition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatModeratorsInsert"] = youtube.get(
        "youtube/v3/liveChat/moderators",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "liveChatId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatModeratorListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatModeratorsDelete"] = youtube.get(
        "youtube/v3/liveChat/moderators",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "liveChatId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatModeratorListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatModeratorsList"] = youtube.get(
        "youtube/v3/liveChat/moderators",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "liveChatId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatModeratorListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["activitiesList"] = youtube.get(
        "youtube/v3/activities",
        t.struct(
            {
                "part": t.string().optional(),
                "pageToken": t.string().optional(),
                "publishedAfter": t.string(),
                "channelId": t.string(),
                "maxResults": t.integer().optional(),
                "mine": t.boolean(),
                "home": t.boolean(),
                "publishedBefore": t.string(),
                "regionCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ActivityListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistItemsUpdate"] = youtube.get(
        "youtube/v3/playlistItems",
        t.struct(
            {
                "playlistId": t.string().optional(),
                "id": t.string(),
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "pageToken": t.string().optional(),
                "videoId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistItemListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistItemsDelete"] = youtube.get(
        "youtube/v3/playlistItems",
        t.struct(
            {
                "playlistId": t.string().optional(),
                "id": t.string(),
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "pageToken": t.string().optional(),
                "videoId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistItemListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistItemsInsert"] = youtube.get(
        "youtube/v3/playlistItems",
        t.struct(
            {
                "playlistId": t.string().optional(),
                "id": t.string(),
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "pageToken": t.string().optional(),
                "videoId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistItemListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistItemsList"] = youtube.get(
        "youtube/v3/playlistItems",
        t.struct(
            {
                "playlistId": t.string().optional(),
                "id": t.string(),
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "pageToken": t.string().optional(),
                "videoId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistItemListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosRate"] = youtube.put(
        "youtube/v3/videos",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "processingDetails": t.proxy(
                    renames["VideoProcessingDetailsIn"]
                ).optional(),
                "monetizationDetails": t.proxy(
                    renames["VideoMonetizationDetailsIn"]
                ).optional(),
                "player": t.proxy(renames["VideoPlayerIn"]).optional(),
                "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
                "kind": t.string().optional(),
                "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
                "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
                "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
                "status": t.proxy(renames["VideoStatusIn"]).optional(),
                "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
                "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
                "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "recordingDetails": t.proxy(
                    renames["VideoRecordingDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "liveStreamingDetails": t.proxy(
                    renames["VideoLiveStreamingDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosDelete"] = youtube.put(
        "youtube/v3/videos",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "processingDetails": t.proxy(
                    renames["VideoProcessingDetailsIn"]
                ).optional(),
                "monetizationDetails": t.proxy(
                    renames["VideoMonetizationDetailsIn"]
                ).optional(),
                "player": t.proxy(renames["VideoPlayerIn"]).optional(),
                "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
                "kind": t.string().optional(),
                "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
                "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
                "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
                "status": t.proxy(renames["VideoStatusIn"]).optional(),
                "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
                "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
                "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "recordingDetails": t.proxy(
                    renames["VideoRecordingDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "liveStreamingDetails": t.proxy(
                    renames["VideoLiveStreamingDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosInsert"] = youtube.put(
        "youtube/v3/videos",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "processingDetails": t.proxy(
                    renames["VideoProcessingDetailsIn"]
                ).optional(),
                "monetizationDetails": t.proxy(
                    renames["VideoMonetizationDetailsIn"]
                ).optional(),
                "player": t.proxy(renames["VideoPlayerIn"]).optional(),
                "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
                "kind": t.string().optional(),
                "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
                "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
                "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
                "status": t.proxy(renames["VideoStatusIn"]).optional(),
                "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
                "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
                "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "recordingDetails": t.proxy(
                    renames["VideoRecordingDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "liveStreamingDetails": t.proxy(
                    renames["VideoLiveStreamingDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosGetRating"] = youtube.put(
        "youtube/v3/videos",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "processingDetails": t.proxy(
                    renames["VideoProcessingDetailsIn"]
                ).optional(),
                "monetizationDetails": t.proxy(
                    renames["VideoMonetizationDetailsIn"]
                ).optional(),
                "player": t.proxy(renames["VideoPlayerIn"]).optional(),
                "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
                "kind": t.string().optional(),
                "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
                "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
                "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
                "status": t.proxy(renames["VideoStatusIn"]).optional(),
                "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
                "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
                "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "recordingDetails": t.proxy(
                    renames["VideoRecordingDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "liveStreamingDetails": t.proxy(
                    renames["VideoLiveStreamingDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosList"] = youtube.put(
        "youtube/v3/videos",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "processingDetails": t.proxy(
                    renames["VideoProcessingDetailsIn"]
                ).optional(),
                "monetizationDetails": t.proxy(
                    renames["VideoMonetizationDetailsIn"]
                ).optional(),
                "player": t.proxy(renames["VideoPlayerIn"]).optional(),
                "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
                "kind": t.string().optional(),
                "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
                "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
                "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
                "status": t.proxy(renames["VideoStatusIn"]).optional(),
                "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
                "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
                "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "recordingDetails": t.proxy(
                    renames["VideoRecordingDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "liveStreamingDetails": t.proxy(
                    renames["VideoLiveStreamingDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosReportAbuse"] = youtube.put(
        "youtube/v3/videos",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "processingDetails": t.proxy(
                    renames["VideoProcessingDetailsIn"]
                ).optional(),
                "monetizationDetails": t.proxy(
                    renames["VideoMonetizationDetailsIn"]
                ).optional(),
                "player": t.proxy(renames["VideoPlayerIn"]).optional(),
                "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
                "kind": t.string().optional(),
                "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
                "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
                "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
                "status": t.proxy(renames["VideoStatusIn"]).optional(),
                "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
                "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
                "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "recordingDetails": t.proxy(
                    renames["VideoRecordingDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "liveStreamingDetails": t.proxy(
                    renames["VideoLiveStreamingDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosUpdate"] = youtube.put(
        "youtube/v3/videos",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "processingDetails": t.proxy(
                    renames["VideoProcessingDetailsIn"]
                ).optional(),
                "monetizationDetails": t.proxy(
                    renames["VideoMonetizationDetailsIn"]
                ).optional(),
                "player": t.proxy(renames["VideoPlayerIn"]).optional(),
                "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
                "kind": t.string().optional(),
                "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
                "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
                "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
                "status": t.proxy(renames["VideoStatusIn"]).optional(),
                "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
                "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
                "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "recordingDetails": t.proxy(
                    renames["VideoRecordingDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "liveStreamingDetails": t.proxy(
                    renames["VideoLiveStreamingDetailsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatBansInsert"] = youtube.delete(
        "youtube/v3/liveChat/bans",
        t.struct({"id": t.string(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatBansDelete"] = youtube.delete(
        "youtube/v3/liveChat/bans",
        t.struct({"id": t.string(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["i18nLanguagesList"] = youtube.get(
        "youtube/v3/i18nLanguages",
        t.struct(
            {
                "hl": t.string(),
                "part": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["I18nLanguageListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsDelete"] = youtube.post(
        "youtube/v3/subscriptions",
        t.struct(
            {
                "part": t.string().optional(),
                "kind": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["SubscriptionContentDetailsIn"]
                ).optional(),
                "subscriberSnippet": t.proxy(
                    renames["SubscriptionSubscriberSnippetIn"]
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["SubscriptionSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsList"] = youtube.post(
        "youtube/v3/subscriptions",
        t.struct(
            {
                "part": t.string().optional(),
                "kind": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["SubscriptionContentDetailsIn"]
                ).optional(),
                "subscriberSnippet": t.proxy(
                    renames["SubscriptionSubscriberSnippetIn"]
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["SubscriptionSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsInsert"] = youtube.post(
        "youtube/v3/subscriptions",
        t.struct(
            {
                "part": t.string().optional(),
                "kind": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["SubscriptionContentDetailsIn"]
                ).optional(),
                "subscriberSnippet": t.proxy(
                    renames["SubscriptionSubscriberSnippetIn"]
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["SubscriptionSnippetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsBind"] = youtube.get(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "mine": t.boolean(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "broadcastStatus": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "broadcastType": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsUpdate"] = youtube.get(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "mine": t.boolean(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "broadcastStatus": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "broadcastType": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsTransition"] = youtube.get(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "mine": t.boolean(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "broadcastStatus": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "broadcastType": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsInsert"] = youtube.get(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "mine": t.boolean(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "broadcastStatus": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "broadcastType": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsInsertCuepoint"] = youtube.get(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "mine": t.boolean(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "broadcastStatus": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "broadcastType": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsDelete"] = youtube.get(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "mine": t.boolean(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "broadcastStatus": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "broadcastType": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsList"] = youtube.get(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "mine": t.boolean(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "broadcastStatus": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "broadcastType": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="youtube", renames=renames, types=Box(types), functions=Box(functions)
    )
