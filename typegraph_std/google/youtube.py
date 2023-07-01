from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_youtube():
    youtube = HTTPRuntime("https://youtube.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtube_1_ErrorResponse",
        "ChannelSectionTargetingIn": "_youtube_2_ChannelSectionTargetingIn",
        "ChannelSectionTargetingOut": "_youtube_3_ChannelSectionTargetingOut",
        "PageInfoIn": "_youtube_4_PageInfoIn",
        "PageInfoOut": "_youtube_5_PageInfoOut",
        "ActivityContentDetailsSubscriptionIn": "_youtube_6_ActivityContentDetailsSubscriptionIn",
        "ActivityContentDetailsSubscriptionOut": "_youtube_7_ActivityContentDetailsSubscriptionOut",
        "ChannelConversionPingIn": "_youtube_8_ChannelConversionPingIn",
        "ChannelConversionPingOut": "_youtube_9_ChannelConversionPingOut",
        "MembershipsLevelSnippetIn": "_youtube_10_MembershipsLevelSnippetIn",
        "MembershipsLevelSnippetOut": "_youtube_11_MembershipsLevelSnippetOut",
        "SubscriptionSubscriberSnippetIn": "_youtube_12_SubscriptionSubscriberSnippetIn",
        "SubscriptionSubscriberSnippetOut": "_youtube_13_SubscriptionSubscriberSnippetOut",
        "LiveStreamIn": "_youtube_14_LiveStreamIn",
        "LiveStreamOut": "_youtube_15_LiveStreamOut",
        "ImageSettingsIn": "_youtube_16_ImageSettingsIn",
        "ImageSettingsOut": "_youtube_17_ImageSettingsOut",
        "LiveChatModeratorSnippetIn": "_youtube_18_LiveChatModeratorSnippetIn",
        "LiveChatModeratorSnippetOut": "_youtube_19_LiveChatModeratorSnippetOut",
        "ChannelContentOwnerDetailsIn": "_youtube_20_ChannelContentOwnerDetailsIn",
        "ChannelContentOwnerDetailsOut": "_youtube_21_ChannelContentOwnerDetailsOut",
        "VideoRatingIn": "_youtube_22_VideoRatingIn",
        "VideoRatingOut": "_youtube_23_VideoRatingOut",
        "ActivityContentDetailsPlaylistItemIn": "_youtube_24_ActivityContentDetailsPlaylistItemIn",
        "ActivityContentDetailsPlaylistItemOut": "_youtube_25_ActivityContentDetailsPlaylistItemOut",
        "SuperChatEventListResponseIn": "_youtube_26_SuperChatEventListResponseIn",
        "SuperChatEventListResponseOut": "_youtube_27_SuperChatEventListResponseOut",
        "ChannelSectionIn": "_youtube_28_ChannelSectionIn",
        "ChannelSectionOut": "_youtube_29_ChannelSectionOut",
        "I18nLanguageListResponseIn": "_youtube_30_I18nLanguageListResponseIn",
        "I18nLanguageListResponseOut": "_youtube_31_I18nLanguageListResponseOut",
        "LiveChatMessageSnippetIn": "_youtube_32_LiveChatMessageSnippetIn",
        "LiveChatMessageSnippetOut": "_youtube_33_LiveChatMessageSnippetOut",
        "VideoFileDetailsVideoStreamIn": "_youtube_34_VideoFileDetailsVideoStreamIn",
        "VideoFileDetailsVideoStreamOut": "_youtube_35_VideoFileDetailsVideoStreamOut",
        "ChannelBannerResourceIn": "_youtube_36_ChannelBannerResourceIn",
        "ChannelBannerResourceOut": "_youtube_37_ChannelBannerResourceOut",
        "ThirdPartyLinkListResponseIn": "_youtube_38_ThirdPartyLinkListResponseIn",
        "ThirdPartyLinkListResponseOut": "_youtube_39_ThirdPartyLinkListResponseOut",
        "LiveChatNewSponsorDetailsIn": "_youtube_40_LiveChatNewSponsorDetailsIn",
        "LiveChatNewSponsorDetailsOut": "_youtube_41_LiveChatNewSponsorDetailsOut",
        "CommentIn": "_youtube_42_CommentIn",
        "CommentOut": "_youtube_43_CommentOut",
        "CommentThreadSnippetIn": "_youtube_44_CommentThreadSnippetIn",
        "CommentThreadSnippetOut": "_youtube_45_CommentThreadSnippetOut",
        "ChannelAuditDetailsIn": "_youtube_46_ChannelAuditDetailsIn",
        "ChannelAuditDetailsOut": "_youtube_47_ChannelAuditDetailsOut",
        "ChannelSectionListResponseIn": "_youtube_48_ChannelSectionListResponseIn",
        "ChannelSectionListResponseOut": "_youtube_49_ChannelSectionListResponseOut",
        "CommentThreadIn": "_youtube_50_CommentThreadIn",
        "CommentThreadOut": "_youtube_51_CommentThreadOut",
        "VideoIn": "_youtube_52_VideoIn",
        "VideoOut": "_youtube_53_VideoOut",
        "LiveChatTextMessageDetailsIn": "_youtube_54_LiveChatTextMessageDetailsIn",
        "LiveChatTextMessageDetailsOut": "_youtube_55_LiveChatTextMessageDetailsOut",
        "LiveBroadcastListResponseIn": "_youtube_56_LiveBroadcastListResponseIn",
        "LiveBroadcastListResponseOut": "_youtube_57_LiveBroadcastListResponseOut",
        "ChannelSectionLocalizationIn": "_youtube_58_ChannelSectionLocalizationIn",
        "ChannelSectionLocalizationOut": "_youtube_59_ChannelSectionLocalizationOut",
        "ChannelStatisticsIn": "_youtube_60_ChannelStatisticsIn",
        "ChannelStatisticsOut": "_youtube_61_ChannelStatisticsOut",
        "LiveBroadcastContentDetailsIn": "_youtube_62_LiveBroadcastContentDetailsIn",
        "LiveBroadcastContentDetailsOut": "_youtube_63_LiveBroadcastContentDetailsOut",
        "MemberListResponseIn": "_youtube_64_MemberListResponseIn",
        "MemberListResponseOut": "_youtube_65_MemberListResponseOut",
        "I18nRegionSnippetIn": "_youtube_66_I18nRegionSnippetIn",
        "I18nRegionSnippetOut": "_youtube_67_I18nRegionSnippetOut",
        "VideoListResponseIn": "_youtube_68_VideoListResponseIn",
        "VideoListResponseOut": "_youtube_69_VideoListResponseOut",
        "LiveChatMessageIn": "_youtube_70_LiveChatMessageIn",
        "LiveChatMessageOut": "_youtube_71_LiveChatMessageOut",
        "LiveChatMembershipGiftingDetailsIn": "_youtube_72_LiveChatMembershipGiftingDetailsIn",
        "LiveChatMembershipGiftingDetailsOut": "_youtube_73_LiveChatMembershipGiftingDetailsOut",
        "CaptionSnippetIn": "_youtube_74_CaptionSnippetIn",
        "CaptionSnippetOut": "_youtube_75_CaptionSnippetOut",
        "VideoFileDetailsAudioStreamIn": "_youtube_76_VideoFileDetailsAudioStreamIn",
        "VideoFileDetailsAudioStreamOut": "_youtube_77_VideoFileDetailsAudioStreamOut",
        "ChannelIn": "_youtube_78_ChannelIn",
        "ChannelOut": "_youtube_79_ChannelOut",
        "ActivityContentDetailsChannelItemIn": "_youtube_80_ActivityContentDetailsChannelItemIn",
        "ActivityContentDetailsChannelItemOut": "_youtube_81_ActivityContentDetailsChannelItemOut",
        "ChannelProfileDetailsIn": "_youtube_82_ChannelProfileDetailsIn",
        "ChannelProfileDetailsOut": "_youtube_83_ChannelProfileDetailsOut",
        "MemberSnippetIn": "_youtube_84_MemberSnippetIn",
        "MemberSnippetOut": "_youtube_85_MemberSnippetOut",
        "ThirdPartyLinkIn": "_youtube_86_ThirdPartyLinkIn",
        "ThirdPartyLinkOut": "_youtube_87_ThirdPartyLinkOut",
        "ActivityContentDetailsFavoriteIn": "_youtube_88_ActivityContentDetailsFavoriteIn",
        "ActivityContentDetailsFavoriteOut": "_youtube_89_ActivityContentDetailsFavoriteOut",
        "CommentListResponseIn": "_youtube_90_CommentListResponseIn",
        "CommentListResponseOut": "_youtube_91_CommentListResponseOut",
        "LiveBroadcastIn": "_youtube_92_LiveBroadcastIn",
        "LiveBroadcastOut": "_youtube_93_LiveBroadcastOut",
        "LiveChatSuperChatDetailsIn": "_youtube_94_LiveChatSuperChatDetailsIn",
        "LiveChatSuperChatDetailsOut": "_youtube_95_LiveChatSuperChatDetailsOut",
        "VideoRecordingDetailsIn": "_youtube_96_VideoRecordingDetailsIn",
        "VideoRecordingDetailsOut": "_youtube_97_VideoRecordingDetailsOut",
        "VideoStatusIn": "_youtube_98_VideoStatusIn",
        "VideoStatusOut": "_youtube_99_VideoStatusOut",
        "SuperChatEventIn": "_youtube_100_SuperChatEventIn",
        "SuperChatEventOut": "_youtube_101_SuperChatEventOut",
        "LiveStreamListResponseIn": "_youtube_102_LiveStreamListResponseIn",
        "LiveStreamListResponseOut": "_youtube_103_LiveStreamListResponseOut",
        "VideoProcessingDetailsIn": "_youtube_104_VideoProcessingDetailsIn",
        "VideoProcessingDetailsOut": "_youtube_105_VideoProcessingDetailsOut",
        "InvideoPositionIn": "_youtube_106_InvideoPositionIn",
        "InvideoPositionOut": "_youtube_107_InvideoPositionOut",
        "SearchResultIn": "_youtube_108_SearchResultIn",
        "SearchResultOut": "_youtube_109_SearchResultOut",
        "AbuseReportIn": "_youtube_110_AbuseReportIn",
        "AbuseReportOut": "_youtube_111_AbuseReportOut",
        "ChannelLocalizationIn": "_youtube_112_ChannelLocalizationIn",
        "ChannelLocalizationOut": "_youtube_113_ChannelLocalizationOut",
        "ThirdPartyLinkStatusIn": "_youtube_114_ThirdPartyLinkStatusIn",
        "ThirdPartyLinkStatusOut": "_youtube_115_ThirdPartyLinkStatusOut",
        "ContentRatingIn": "_youtube_116_ContentRatingIn",
        "ContentRatingOut": "_youtube_117_ContentRatingOut",
        "VideoCategoryListResponseIn": "_youtube_118_VideoCategoryListResponseIn",
        "VideoCategoryListResponseOut": "_youtube_119_VideoCategoryListResponseOut",
        "ChannelBrandingSettingsIn": "_youtube_120_ChannelBrandingSettingsIn",
        "ChannelBrandingSettingsOut": "_youtube_121_ChannelBrandingSettingsOut",
        "LiveStreamContentDetailsIn": "_youtube_122_LiveStreamContentDetailsIn",
        "LiveStreamContentDetailsOut": "_youtube_123_LiveStreamContentDetailsOut",
        "LiveBroadcastSnippetIn": "_youtube_124_LiveBroadcastSnippetIn",
        "LiveBroadcastSnippetOut": "_youtube_125_LiveBroadcastSnippetOut",
        "I18nLanguageSnippetIn": "_youtube_126_I18nLanguageSnippetIn",
        "I18nLanguageSnippetOut": "_youtube_127_I18nLanguageSnippetOut",
        "TestItemIn": "_youtube_128_TestItemIn",
        "TestItemOut": "_youtube_129_TestItemOut",
        "LiveStreamStatusIn": "_youtube_130_LiveStreamStatusIn",
        "LiveStreamStatusOut": "_youtube_131_LiveStreamStatusOut",
        "VideoLiveStreamingDetailsIn": "_youtube_132_VideoLiveStreamingDetailsIn",
        "VideoLiveStreamingDetailsOut": "_youtube_133_VideoLiveStreamingDetailsOut",
        "IngestionInfoIn": "_youtube_134_IngestionInfoIn",
        "IngestionInfoOut": "_youtube_135_IngestionInfoOut",
        "VideoSuggestionsTagSuggestionIn": "_youtube_136_VideoSuggestionsTagSuggestionIn",
        "VideoSuggestionsTagSuggestionOut": "_youtube_137_VideoSuggestionsTagSuggestionOut",
        "ThirdPartyLinkSnippetIn": "_youtube_138_ThirdPartyLinkSnippetIn",
        "ThirdPartyLinkSnippetOut": "_youtube_139_ThirdPartyLinkSnippetOut",
        "ActivityContentDetailsBulletinIn": "_youtube_140_ActivityContentDetailsBulletinIn",
        "ActivityContentDetailsBulletinOut": "_youtube_141_ActivityContentDetailsBulletinOut",
        "PlaylistSnippetIn": "_youtube_142_PlaylistSnippetIn",
        "PlaylistSnippetOut": "_youtube_143_PlaylistSnippetOut",
        "ActivityContentDetailsCommentIn": "_youtube_144_ActivityContentDetailsCommentIn",
        "ActivityContentDetailsCommentOut": "_youtube_145_ActivityContentDetailsCommentOut",
        "CommentThreadRepliesIn": "_youtube_146_CommentThreadRepliesIn",
        "CommentThreadRepliesOut": "_youtube_147_CommentThreadRepliesOut",
        "LanguageTagIn": "_youtube_148_LanguageTagIn",
        "LanguageTagOut": "_youtube_149_LanguageTagOut",
        "ChannelConversionPingsIn": "_youtube_150_ChannelConversionPingsIn",
        "ChannelConversionPingsOut": "_youtube_151_ChannelConversionPingsOut",
        "VideoAbuseReportReasonListResponseIn": "_youtube_152_VideoAbuseReportReasonListResponseIn",
        "VideoAbuseReportReasonListResponseOut": "_youtube_153_VideoAbuseReportReasonListResponseOut",
        "LiveStreamConfigurationIssueIn": "_youtube_154_LiveStreamConfigurationIssueIn",
        "LiveStreamConfigurationIssueOut": "_youtube_155_LiveStreamConfigurationIssueOut",
        "ActivityContentDetailsPromotedItemIn": "_youtube_156_ActivityContentDetailsPromotedItemIn",
        "ActivityContentDetailsPromotedItemOut": "_youtube_157_ActivityContentDetailsPromotedItemOut",
        "I18nRegionIn": "_youtube_158_I18nRegionIn",
        "I18nRegionOut": "_youtube_159_I18nRegionOut",
        "EntityIn": "_youtube_160_EntityIn",
        "EntityOut": "_youtube_161_EntityOut",
        "VideoCategoryIn": "_youtube_162_VideoCategoryIn",
        "VideoCategoryOut": "_youtube_163_VideoCategoryOut",
        "SubscriptionSnippetIn": "_youtube_164_SubscriptionSnippetIn",
        "SubscriptionSnippetOut": "_youtube_165_SubscriptionSnippetOut",
        "CommentThreadListResponseIn": "_youtube_166_CommentThreadListResponseIn",
        "CommentThreadListResponseOut": "_youtube_167_CommentThreadListResponseOut",
        "I18nRegionListResponseIn": "_youtube_168_I18nRegionListResponseIn",
        "I18nRegionListResponseOut": "_youtube_169_I18nRegionListResponseOut",
        "LiveChatUserBannedMessageDetailsIn": "_youtube_170_LiveChatUserBannedMessageDetailsIn",
        "LiveChatUserBannedMessageDetailsOut": "_youtube_171_LiveChatUserBannedMessageDetailsOut",
        "VideoTopicDetailsIn": "_youtube_172_VideoTopicDetailsIn",
        "VideoTopicDetailsOut": "_youtube_173_VideoTopicDetailsOut",
        "VideoContentDetailsRegionRestrictionIn": "_youtube_174_VideoContentDetailsRegionRestrictionIn",
        "VideoContentDetailsRegionRestrictionOut": "_youtube_175_VideoContentDetailsRegionRestrictionOut",
        "GeoPointIn": "_youtube_176_GeoPointIn",
        "GeoPointOut": "_youtube_177_GeoPointOut",
        "LiveChatModeratorIn": "_youtube_178_LiveChatModeratorIn",
        "LiveChatModeratorOut": "_youtube_179_LiveChatModeratorOut",
        "LocalizedPropertyIn": "_youtube_180_LocalizedPropertyIn",
        "LocalizedPropertyOut": "_youtube_181_LocalizedPropertyOut",
        "CaptionListResponseIn": "_youtube_182_CaptionListResponseIn",
        "CaptionListResponseOut": "_youtube_183_CaptionListResponseOut",
        "ActivityContentDetailsSocialIn": "_youtube_184_ActivityContentDetailsSocialIn",
        "ActivityContentDetailsSocialOut": "_youtube_185_ActivityContentDetailsSocialOut",
        "LiveChatMessageListResponseIn": "_youtube_186_LiveChatMessageListResponseIn",
        "LiveChatMessageListResponseOut": "_youtube_187_LiveChatMessageListResponseOut",
        "PropertyValueIn": "_youtube_188_PropertyValueIn",
        "PropertyValueOut": "_youtube_189_PropertyValueOut",
        "PlaylistItemListResponseIn": "_youtube_190_PlaylistItemListResponseIn",
        "PlaylistItemListResponseOut": "_youtube_191_PlaylistItemListResponseOut",
        "VideoPlayerIn": "_youtube_192_VideoPlayerIn",
        "VideoPlayerOut": "_youtube_193_VideoPlayerOut",
        "TestItemTestItemSnippetIn": "_youtube_194_TestItemTestItemSnippetIn",
        "TestItemTestItemSnippetOut": "_youtube_195_TestItemTestItemSnippetOut",
        "LiveChatBanSnippetIn": "_youtube_196_LiveChatBanSnippetIn",
        "LiveChatBanSnippetOut": "_youtube_197_LiveChatBanSnippetOut",
        "VideoContentDetailsIn": "_youtube_198_VideoContentDetailsIn",
        "VideoContentDetailsOut": "_youtube_199_VideoContentDetailsOut",
        "LiveChatModeratorListResponseIn": "_youtube_200_LiveChatModeratorListResponseIn",
        "LiveChatModeratorListResponseOut": "_youtube_201_LiveChatModeratorListResponseOut",
        "MembershipsDetailsIn": "_youtube_202_MembershipsDetailsIn",
        "MembershipsDetailsOut": "_youtube_203_MembershipsDetailsOut",
        "LiveChatBanIn": "_youtube_204_LiveChatBanIn",
        "LiveChatBanOut": "_youtube_205_LiveChatBanOut",
        "VideoAbuseReportIn": "_youtube_206_VideoAbuseReportIn",
        "VideoAbuseReportOut": "_youtube_207_VideoAbuseReportOut",
        "ResourceIdIn": "_youtube_208_ResourceIdIn",
        "ResourceIdOut": "_youtube_209_ResourceIdOut",
        "CaptionIn": "_youtube_210_CaptionIn",
        "CaptionOut": "_youtube_211_CaptionOut",
        "VideoAbuseReportReasonIn": "_youtube_212_VideoAbuseReportReasonIn",
        "VideoAbuseReportReasonOut": "_youtube_213_VideoAbuseReportReasonOut",
        "MembershipsLevelIn": "_youtube_214_MembershipsLevelIn",
        "MembershipsLevelOut": "_youtube_215_MembershipsLevelOut",
        "SearchResultSnippetIn": "_youtube_216_SearchResultSnippetIn",
        "SearchResultSnippetOut": "_youtube_217_SearchResultSnippetOut",
        "ThumbnailDetailsIn": "_youtube_218_ThumbnailDetailsIn",
        "ThumbnailDetailsOut": "_youtube_219_ThumbnailDetailsOut",
        "ChannelSnippetIn": "_youtube_220_ChannelSnippetIn",
        "ChannelSnippetOut": "_youtube_221_ChannelSnippetOut",
        "CommentSnippetIn": "_youtube_222_CommentSnippetIn",
        "CommentSnippetOut": "_youtube_223_CommentSnippetOut",
        "ActivityContentDetailsIn": "_youtube_224_ActivityContentDetailsIn",
        "ActivityContentDetailsOut": "_youtube_225_ActivityContentDetailsOut",
        "LiveChatMessageDeletedDetailsIn": "_youtube_226_LiveChatMessageDeletedDetailsIn",
        "LiveChatMessageDeletedDetailsOut": "_youtube_227_LiveChatMessageDeletedDetailsOut",
        "WatchSettingsIn": "_youtube_228_WatchSettingsIn",
        "WatchSettingsOut": "_youtube_229_WatchSettingsOut",
        "ChannelStatusIn": "_youtube_230_ChannelStatusIn",
        "ChannelStatusOut": "_youtube_231_ChannelStatusOut",
        "LiveChatMessageAuthorDetailsIn": "_youtube_232_LiveChatMessageAuthorDetailsIn",
        "LiveChatMessageAuthorDetailsOut": "_youtube_233_LiveChatMessageAuthorDetailsOut",
        "ThumbnailSetResponseIn": "_youtube_234_ThumbnailSetResponseIn",
        "ThumbnailSetResponseOut": "_youtube_235_ThumbnailSetResponseOut",
        "ChannelSectionSnippetIn": "_youtube_236_ChannelSectionSnippetIn",
        "ChannelSectionSnippetOut": "_youtube_237_ChannelSectionSnippetOut",
        "SearchListResponseIn": "_youtube_238_SearchListResponseIn",
        "SearchListResponseOut": "_youtube_239_SearchListResponseOut",
        "VideoSuggestionsIn": "_youtube_240_VideoSuggestionsIn",
        "VideoSuggestionsOut": "_youtube_241_VideoSuggestionsOut",
        "LocalizedStringIn": "_youtube_242_LocalizedStringIn",
        "LocalizedStringOut": "_youtube_243_LocalizedStringOut",
        "ActivityContentDetailsUploadIn": "_youtube_244_ActivityContentDetailsUploadIn",
        "ActivityContentDetailsUploadOut": "_youtube_245_ActivityContentDetailsUploadOut",
        "AbuseTypeIn": "_youtube_246_AbuseTypeIn",
        "AbuseTypeOut": "_youtube_247_AbuseTypeOut",
        "ActivityContentDetailsRecommendationIn": "_youtube_248_ActivityContentDetailsRecommendationIn",
        "ActivityContentDetailsRecommendationOut": "_youtube_249_ActivityContentDetailsRecommendationOut",
        "VideoAgeGatingIn": "_youtube_250_VideoAgeGatingIn",
        "VideoAgeGatingOut": "_youtube_251_VideoAgeGatingOut",
        "SubscriptionListResponseIn": "_youtube_252_SubscriptionListResponseIn",
        "SubscriptionListResponseOut": "_youtube_253_SubscriptionListResponseOut",
        "PlaylistItemSnippetIn": "_youtube_254_PlaylistItemSnippetIn",
        "PlaylistItemSnippetOut": "_youtube_255_PlaylistItemSnippetOut",
        "MembershipsLevelListResponseIn": "_youtube_256_MembershipsLevelListResponseIn",
        "MembershipsLevelListResponseOut": "_youtube_257_MembershipsLevelListResponseOut",
        "ActivitySnippetIn": "_youtube_258_ActivitySnippetIn",
        "ActivitySnippetOut": "_youtube_259_ActivitySnippetOut",
        "LiveChatMessageRetractedDetailsIn": "_youtube_260_LiveChatMessageRetractedDetailsIn",
        "LiveChatMessageRetractedDetailsOut": "_youtube_261_LiveChatMessageRetractedDetailsOut",
        "LiveBroadcastStatisticsIn": "_youtube_262_LiveBroadcastStatisticsIn",
        "LiveBroadcastStatisticsOut": "_youtube_263_LiveBroadcastStatisticsOut",
        "VideoGetRatingResponseIn": "_youtube_264_VideoGetRatingResponseIn",
        "VideoGetRatingResponseOut": "_youtube_265_VideoGetRatingResponseOut",
        "ActivityContentDetailsLikeIn": "_youtube_266_ActivityContentDetailsLikeIn",
        "ActivityContentDetailsLikeOut": "_youtube_267_ActivityContentDetailsLikeOut",
        "LiveBroadcastStatusIn": "_youtube_268_LiveBroadcastStatusIn",
        "LiveBroadcastStatusOut": "_youtube_269_LiveBroadcastStatusOut",
        "VideoLocalizationIn": "_youtube_270_VideoLocalizationIn",
        "VideoLocalizationOut": "_youtube_271_VideoLocalizationOut",
        "VideoAbuseReportSecondaryReasonIn": "_youtube_272_VideoAbuseReportSecondaryReasonIn",
        "VideoAbuseReportSecondaryReasonOut": "_youtube_273_VideoAbuseReportSecondaryReasonOut",
        "VideoProcessingDetailsProcessingProgressIn": "_youtube_274_VideoProcessingDetailsProcessingProgressIn",
        "VideoProcessingDetailsProcessingProgressOut": "_youtube_275_VideoProcessingDetailsProcessingProgressOut",
        "RelatedEntityIn": "_youtube_276_RelatedEntityIn",
        "RelatedEntityOut": "_youtube_277_RelatedEntityOut",
        "LiveChatGiftMembershipReceivedDetailsIn": "_youtube_278_LiveChatGiftMembershipReceivedDetailsIn",
        "LiveChatGiftMembershipReceivedDetailsOut": "_youtube_279_LiveChatGiftMembershipReceivedDetailsOut",
        "SuperStickerMetadataIn": "_youtube_280_SuperStickerMetadataIn",
        "SuperStickerMetadataOut": "_youtube_281_SuperStickerMetadataOut",
        "ActivityIn": "_youtube_282_ActivityIn",
        "ActivityOut": "_youtube_283_ActivityOut",
        "PlaylistLocalizationIn": "_youtube_284_PlaylistLocalizationIn",
        "PlaylistLocalizationOut": "_youtube_285_PlaylistLocalizationOut",
        "VideoFileDetailsIn": "_youtube_286_VideoFileDetailsIn",
        "VideoFileDetailsOut": "_youtube_287_VideoFileDetailsOut",
        "VideoAbuseReportReasonSnippetIn": "_youtube_288_VideoAbuseReportReasonSnippetIn",
        "VideoAbuseReportReasonSnippetOut": "_youtube_289_VideoAbuseReportReasonSnippetOut",
        "CommentSnippetAuthorChannelIdIn": "_youtube_290_CommentSnippetAuthorChannelIdIn",
        "CommentSnippetAuthorChannelIdOut": "_youtube_291_CommentSnippetAuthorChannelIdOut",
        "LiveStreamHealthStatusIn": "_youtube_292_LiveStreamHealthStatusIn",
        "LiveStreamHealthStatusOut": "_youtube_293_LiveStreamHealthStatusOut",
        "VideoMonetizationDetailsIn": "_youtube_294_VideoMonetizationDetailsIn",
        "VideoMonetizationDetailsOut": "_youtube_295_VideoMonetizationDetailsOut",
        "PlaylistItemIn": "_youtube_296_PlaylistItemIn",
        "PlaylistItemOut": "_youtube_297_PlaylistItemOut",
        "ActivityListResponseIn": "_youtube_298_ActivityListResponseIn",
        "ActivityListResponseOut": "_youtube_299_ActivityListResponseOut",
        "AccessPolicyIn": "_youtube_300_AccessPolicyIn",
        "AccessPolicyOut": "_youtube_301_AccessPolicyOut",
        "PlaylistItemStatusIn": "_youtube_302_PlaylistItemStatusIn",
        "PlaylistItemStatusOut": "_youtube_303_PlaylistItemStatusOut",
        "ChannelSectionContentDetailsIn": "_youtube_304_ChannelSectionContentDetailsIn",
        "ChannelSectionContentDetailsOut": "_youtube_305_ChannelSectionContentDetailsOut",
        "SubscriptionIn": "_youtube_306_SubscriptionIn",
        "SubscriptionOut": "_youtube_307_SubscriptionOut",
        "MemberIn": "_youtube_308_MemberIn",
        "MemberOut": "_youtube_309_MemberOut",
        "CdnSettingsIn": "_youtube_310_CdnSettingsIn",
        "CdnSettingsOut": "_youtube_311_CdnSettingsOut",
        "I18nLanguageIn": "_youtube_312_I18nLanguageIn",
        "I18nLanguageOut": "_youtube_313_I18nLanguageOut",
        "ChannelListResponseIn": "_youtube_314_ChannelListResponseIn",
        "ChannelListResponseOut": "_youtube_315_ChannelListResponseOut",
        "PlaylistContentDetailsIn": "_youtube_316_PlaylistContentDetailsIn",
        "PlaylistContentDetailsOut": "_youtube_317_PlaylistContentDetailsOut",
        "LiveChatFanFundingEventDetailsIn": "_youtube_318_LiveChatFanFundingEventDetailsIn",
        "LiveChatFanFundingEventDetailsOut": "_youtube_319_LiveChatFanFundingEventDetailsOut",
        "MonitorStreamInfoIn": "_youtube_320_MonitorStreamInfoIn",
        "MonitorStreamInfoOut": "_youtube_321_MonitorStreamInfoOut",
        "LiveChatMemberMilestoneChatDetailsIn": "_youtube_322_LiveChatMemberMilestoneChatDetailsIn",
        "LiveChatMemberMilestoneChatDetailsOut": "_youtube_323_LiveChatMemberMilestoneChatDetailsOut",
        "LevelDetailsIn": "_youtube_324_LevelDetailsIn",
        "LevelDetailsOut": "_youtube_325_LevelDetailsOut",
        "InvideoTimingIn": "_youtube_326_InvideoTimingIn",
        "InvideoTimingOut": "_youtube_327_InvideoTimingOut",
        "InvideoBrandingIn": "_youtube_328_InvideoBrandingIn",
        "InvideoBrandingOut": "_youtube_329_InvideoBrandingOut",
        "SubscriptionContentDetailsIn": "_youtube_330_SubscriptionContentDetailsIn",
        "SubscriptionContentDetailsOut": "_youtube_331_SubscriptionContentDetailsOut",
        "PlaylistListResponseIn": "_youtube_332_PlaylistListResponseIn",
        "PlaylistListResponseOut": "_youtube_333_PlaylistListResponseOut",
        "VideoProjectDetailsIn": "_youtube_334_VideoProjectDetailsIn",
        "VideoProjectDetailsOut": "_youtube_335_VideoProjectDetailsOut",
        "CuepointIn": "_youtube_336_CuepointIn",
        "CuepointOut": "_youtube_337_CuepointOut",
        "ChannelToStoreLinkDetailsIn": "_youtube_338_ChannelToStoreLinkDetailsIn",
        "ChannelToStoreLinkDetailsOut": "_youtube_339_ChannelToStoreLinkDetailsOut",
        "ThumbnailIn": "_youtube_340_ThumbnailIn",
        "ThumbnailOut": "_youtube_341_ThumbnailOut",
        "TokenPaginationIn": "_youtube_342_TokenPaginationIn",
        "TokenPaginationOut": "_youtube_343_TokenPaginationOut",
        "LiveStreamSnippetIn": "_youtube_344_LiveStreamSnippetIn",
        "LiveStreamSnippetOut": "_youtube_345_LiveStreamSnippetOut",
        "ChannelSettingsIn": "_youtube_346_ChannelSettingsIn",
        "ChannelSettingsOut": "_youtube_347_ChannelSettingsOut",
        "VideoCategorySnippetIn": "_youtube_348_VideoCategorySnippetIn",
        "VideoCategorySnippetOut": "_youtube_349_VideoCategorySnippetOut",
        "VideoStatisticsIn": "_youtube_350_VideoStatisticsIn",
        "VideoStatisticsOut": "_youtube_351_VideoStatisticsOut",
        "LiveChatSuperStickerDetailsIn": "_youtube_352_LiveChatSuperStickerDetailsIn",
        "LiveChatSuperStickerDetailsOut": "_youtube_353_LiveChatSuperStickerDetailsOut",
        "ChannelTopicDetailsIn": "_youtube_354_ChannelTopicDetailsIn",
        "ChannelTopicDetailsOut": "_youtube_355_ChannelTopicDetailsOut",
        "PlaylistItemContentDetailsIn": "_youtube_356_PlaylistItemContentDetailsIn",
        "PlaylistItemContentDetailsOut": "_youtube_357_PlaylistItemContentDetailsOut",
        "MembershipsDurationAtLevelIn": "_youtube_358_MembershipsDurationAtLevelIn",
        "MembershipsDurationAtLevelOut": "_youtube_359_MembershipsDurationAtLevelOut",
        "PlaylistStatusIn": "_youtube_360_PlaylistStatusIn",
        "PlaylistStatusOut": "_youtube_361_PlaylistStatusOut",
        "MembershipsDurationIn": "_youtube_362_MembershipsDurationIn",
        "MembershipsDurationOut": "_youtube_363_MembershipsDurationOut",
        "PlaylistIn": "_youtube_364_PlaylistIn",
        "PlaylistOut": "_youtube_365_PlaylistOut",
        "VideoSnippetIn": "_youtube_366_VideoSnippetIn",
        "VideoSnippetOut": "_youtube_367_VideoSnippetOut",
        "ChannelContentDetailsIn": "_youtube_368_ChannelContentDetailsIn",
        "ChannelContentDetailsOut": "_youtube_369_ChannelContentDetailsOut",
        "PlaylistPlayerIn": "_youtube_370_PlaylistPlayerIn",
        "PlaylistPlayerOut": "_youtube_371_PlaylistPlayerOut",
        "SuperChatEventSnippetIn": "_youtube_372_SuperChatEventSnippetIn",
        "SuperChatEventSnippetOut": "_youtube_373_SuperChatEventSnippetOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ChannelSectionTargetingIn"] = t.struct(
        {
            "countries": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "languages": t.array(t.string()).optional(),
        }
    ).named(renames["ChannelSectionTargetingIn"])
    types["ChannelSectionTargetingOut"] = t.struct(
        {
            "countries": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "languages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionTargetingOut"])
    types["PageInfoIn"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "resultsPerPage": t.integer().optional(),
        }
    ).named(renames["PageInfoIn"])
    types["PageInfoOut"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "resultsPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageInfoOut"])
    types["ActivityContentDetailsSubscriptionIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsSubscriptionIn"])
    types["ActivityContentDetailsSubscriptionOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsSubscriptionOut"])
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
    types["SubscriptionSubscriberSnippetIn"] = t.struct(
        {
            "channelId": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
        }
    ).named(renames["SubscriptionSubscriberSnippetIn"])
    types["SubscriptionSubscriberSnippetOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionSubscriberSnippetOut"])
    types["LiveStreamIn"] = t.struct(
        {
            "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
            "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
            "contentDetails": t.proxy(renames["LiveStreamContentDetailsIn"]).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["LiveStreamIn"])
    types["LiveStreamOut"] = t.struct(
        {
            "status": t.proxy(renames["LiveStreamStatusOut"]).optional(),
            "cdn": t.proxy(renames["CdnSettingsOut"]).optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["LiveStreamSnippetOut"]).optional(),
            "contentDetails": t.proxy(
                renames["LiveStreamContentDetailsOut"]
            ).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamOut"])
    types["ImageSettingsIn"] = t.struct(
        {
            "smallBrandedBannerImageImapScript": t.proxy(
                renames["LocalizedPropertyIn"]
            ).optional(),
            "bannerMobileExtraHdImageUrl": t.string().optional(),
            "backgroundImageUrl": t.proxy(renames["LocalizedPropertyIn"]).optional(),
            "bannerMobileHdImageUrl": t.string().optional(),
            "bannerTabletExtraHdImageUrl": t.string().optional(),
            "largeBrandedBannerImageUrl": t.proxy(
                renames["LocalizedPropertyIn"]
            ).optional(),
            "bannerMobileLowImageUrl": t.string().optional(),
            "bannerImageUrl": t.string().optional(),
            "watchIconImageUrl": t.string(),
            "bannerMobileImageUrl": t.string().optional(),
            "smallBrandedBannerImageUrl": t.proxy(
                renames["LocalizedPropertyIn"]
            ).optional(),
            "bannerTvImageUrl": t.string().optional(),
            "largeBrandedBannerImageImapScript": t.proxy(
                renames["LocalizedPropertyIn"]
            ).optional(),
            "bannerTvLowImageUrl": t.string().optional(),
            "bannerTvHighImageUrl": t.string().optional(),
            "trackingImageUrl": t.string().optional(),
            "bannerTvMediumImageUrl": t.string().optional(),
            "bannerMobileMediumHdImageUrl": t.string().optional(),
            "bannerTabletLowImageUrl": t.string().optional(),
            "bannerExternalUrl": t.string().optional(),
            "bannerTabletImageUrl": t.string().optional(),
            "bannerTabletHdImageUrl": t.string().optional(),
        }
    ).named(renames["ImageSettingsIn"])
    types["ImageSettingsOut"] = t.struct(
        {
            "smallBrandedBannerImageImapScript": t.proxy(
                renames["LocalizedPropertyOut"]
            ).optional(),
            "bannerMobileExtraHdImageUrl": t.string().optional(),
            "backgroundImageUrl": t.proxy(renames["LocalizedPropertyOut"]).optional(),
            "bannerMobileHdImageUrl": t.string().optional(),
            "bannerTabletExtraHdImageUrl": t.string().optional(),
            "largeBrandedBannerImageUrl": t.proxy(
                renames["LocalizedPropertyOut"]
            ).optional(),
            "bannerMobileLowImageUrl": t.string().optional(),
            "bannerImageUrl": t.string().optional(),
            "watchIconImageUrl": t.string(),
            "bannerMobileImageUrl": t.string().optional(),
            "smallBrandedBannerImageUrl": t.proxy(
                renames["LocalizedPropertyOut"]
            ).optional(),
            "bannerTvImageUrl": t.string().optional(),
            "largeBrandedBannerImageImapScript": t.proxy(
                renames["LocalizedPropertyOut"]
            ).optional(),
            "bannerTvLowImageUrl": t.string().optional(),
            "bannerTvHighImageUrl": t.string().optional(),
            "trackingImageUrl": t.string().optional(),
            "bannerTvMediumImageUrl": t.string().optional(),
            "bannerMobileMediumHdImageUrl": t.string().optional(),
            "bannerTabletLowImageUrl": t.string().optional(),
            "bannerExternalUrl": t.string().optional(),
            "bannerTabletImageUrl": t.string().optional(),
            "bannerTabletHdImageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageSettingsOut"])
    types["LiveChatModeratorSnippetIn"] = t.struct(
        {
            "moderatorDetails": t.proxy(renames["ChannelProfileDetailsIn"]).optional(),
            "liveChatId": t.string().optional(),
        }
    ).named(renames["LiveChatModeratorSnippetIn"])
    types["LiveChatModeratorSnippetOut"] = t.struct(
        {
            "moderatorDetails": t.proxy(renames["ChannelProfileDetailsOut"]).optional(),
            "liveChatId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatModeratorSnippetOut"])
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
    types["VideoRatingIn"] = t.struct(
        {"videoId": t.string().optional(), "rating": t.string().optional()}
    ).named(renames["VideoRatingIn"])
    types["VideoRatingOut"] = t.struct(
        {
            "videoId": t.string().optional(),
            "rating": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoRatingOut"])
    types["ActivityContentDetailsPlaylistItemIn"] = t.struct(
        {
            "playlistItemId": t.string().optional(),
            "playlistId": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
        }
    ).named(renames["ActivityContentDetailsPlaylistItemIn"])
    types["ActivityContentDetailsPlaylistItemOut"] = t.struct(
        {
            "playlistItemId": t.string().optional(),
            "playlistId": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsPlaylistItemOut"])
    types["SuperChatEventListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]),
            "items": t.array(t.proxy(renames["SuperChatEventIn"])).optional(),
            "visitorId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "etag": t.string().optional(),
        }
    ).named(renames["SuperChatEventListResponseIn"])
    types["SuperChatEventListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]),
            "items": t.array(t.proxy(renames["SuperChatEventOut"])).optional(),
            "visitorId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperChatEventListResponseOut"])
    types["ChannelSectionIn"] = t.struct(
        {
            "targeting": t.proxy(renames["ChannelSectionTargetingIn"]).optional(),
            "kind": t.string().optional(),
            "contentDetails": t.proxy(
                renames["ChannelSectionContentDetailsIn"]
            ).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["ChannelSectionSnippetIn"]).optional(),
        }
    ).named(renames["ChannelSectionIn"])
    types["ChannelSectionOut"] = t.struct(
        {
            "targeting": t.proxy(renames["ChannelSectionTargetingOut"]).optional(),
            "kind": t.string().optional(),
            "contentDetails": t.proxy(
                renames["ChannelSectionContentDetailsOut"]
            ).optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["ChannelSectionSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionOut"])
    types["I18nLanguageListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["I18nLanguageIn"])).optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "eventId": t.string().optional(),
        }
    ).named(renames["I18nLanguageListResponseIn"])
    types["I18nLanguageListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["I18nLanguageOut"])).optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nLanguageListResponseOut"])
    types["LiveChatMessageSnippetIn"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "newSponsorDetails": t.proxy(
                renames["LiveChatNewSponsorDetailsIn"]
            ).optional(),
            "memberMilestoneChatDetails": t.proxy(
                renames["LiveChatMemberMilestoneChatDetailsIn"]
            ).optional(),
            "fanFundingEventDetails": t.proxy(
                renames["LiveChatFanFundingEventDetailsIn"]
            ).optional(),
            "messageRetractedDetails": t.proxy(
                renames["LiveChatMessageRetractedDetailsIn"]
            ),
            "displayMessage": t.string().optional(),
            "authorChannelId": t.string().optional(),
            "messageDeletedDetails": t.proxy(
                renames["LiveChatMessageDeletedDetailsIn"]
            ),
            "textMessageDetails": t.proxy(
                renames["LiveChatTextMessageDetailsIn"]
            ).optional(),
            "superChatDetails": t.proxy(
                renames["LiveChatSuperChatDetailsIn"]
            ).optional(),
            "giftMembershipReceivedDetails": t.proxy(
                renames["LiveChatGiftMembershipReceivedDetailsIn"]
            ).optional(),
            "liveChatId": t.string(),
            "hasDisplayContent": t.boolean().optional(),
            "type": t.string().optional(),
            "userBannedDetails": t.proxy(renames["LiveChatUserBannedMessageDetailsIn"]),
            "membershipGiftingDetails": t.proxy(
                renames["LiveChatMembershipGiftingDetailsIn"]
            ).optional(),
            "superStickerDetails": t.proxy(
                renames["LiveChatSuperStickerDetailsIn"]
            ).optional(),
        }
    ).named(renames["LiveChatMessageSnippetIn"])
    types["LiveChatMessageSnippetOut"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "newSponsorDetails": t.proxy(
                renames["LiveChatNewSponsorDetailsOut"]
            ).optional(),
            "memberMilestoneChatDetails": t.proxy(
                renames["LiveChatMemberMilestoneChatDetailsOut"]
            ).optional(),
            "fanFundingEventDetails": t.proxy(
                renames["LiveChatFanFundingEventDetailsOut"]
            ).optional(),
            "messageRetractedDetails": t.proxy(
                renames["LiveChatMessageRetractedDetailsOut"]
            ),
            "displayMessage": t.string().optional(),
            "authorChannelId": t.string().optional(),
            "messageDeletedDetails": t.proxy(
                renames["LiveChatMessageDeletedDetailsOut"]
            ),
            "textMessageDetails": t.proxy(
                renames["LiveChatTextMessageDetailsOut"]
            ).optional(),
            "superChatDetails": t.proxy(
                renames["LiveChatSuperChatDetailsOut"]
            ).optional(),
            "giftMembershipReceivedDetails": t.proxy(
                renames["LiveChatGiftMembershipReceivedDetailsOut"]
            ).optional(),
            "liveChatId": t.string(),
            "hasDisplayContent": t.boolean().optional(),
            "type": t.string().optional(),
            "userBannedDetails": t.proxy(
                renames["LiveChatUserBannedMessageDetailsOut"]
            ),
            "membershipGiftingDetails": t.proxy(
                renames["LiveChatMembershipGiftingDetailsOut"]
            ).optional(),
            "superStickerDetails": t.proxy(
                renames["LiveChatSuperStickerDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageSnippetOut"])
    types["VideoFileDetailsVideoStreamIn"] = t.struct(
        {
            "bitrateBps": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "rotation": t.string().optional(),
            "frameRateFps": t.number().optional(),
            "vendor": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "codec": t.string().optional(),
        }
    ).named(renames["VideoFileDetailsVideoStreamIn"])
    types["VideoFileDetailsVideoStreamOut"] = t.struct(
        {
            "bitrateBps": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "rotation": t.string().optional(),
            "frameRateFps": t.number().optional(),
            "vendor": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "codec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFileDetailsVideoStreamOut"])
    types["ChannelBannerResourceIn"] = t.struct(
        {
            "url": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string(),
        }
    ).named(renames["ChannelBannerResourceIn"])
    types["ChannelBannerResourceOut"] = t.struct(
        {
            "url": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelBannerResourceOut"])
    types["ThirdPartyLinkListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["ThirdPartyLinkIn"])),
        }
    ).named(renames["ThirdPartyLinkListResponseIn"])
    types["ThirdPartyLinkListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["ThirdPartyLinkOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyLinkListResponseOut"])
    types["LiveChatNewSponsorDetailsIn"] = t.struct(
        {"isUpgrade": t.boolean().optional(), "memberLevelName": t.string().optional()}
    ).named(renames["LiveChatNewSponsorDetailsIn"])
    types["LiveChatNewSponsorDetailsOut"] = t.struct(
        {
            "isUpgrade": t.boolean().optional(),
            "memberLevelName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatNewSponsorDetailsOut"])
    types["CommentIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["CommentSnippetIn"]).optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["CommentSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["CommentThreadSnippetIn"] = t.struct(
        {
            "totalReplyCount": t.integer().optional(),
            "canReply": t.boolean().optional(),
            "channelId": t.string().optional(),
            "videoId": t.string().optional(),
            "topLevelComment": t.proxy(renames["CommentIn"]).optional(),
            "isPublic": t.boolean().optional(),
        }
    ).named(renames["CommentThreadSnippetIn"])
    types["CommentThreadSnippetOut"] = t.struct(
        {
            "totalReplyCount": t.integer().optional(),
            "canReply": t.boolean().optional(),
            "channelId": t.string().optional(),
            "videoId": t.string().optional(),
            "topLevelComment": t.proxy(renames["CommentOut"]).optional(),
            "isPublic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentThreadSnippetOut"])
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
    types["ChannelSectionListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ChannelSectionIn"])).optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ChannelSectionListResponseIn"])
    types["ChannelSectionListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ChannelSectionOut"])).optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionListResponseOut"])
    types["CommentThreadIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["CommentThreadSnippetIn"]).optional(),
            "replies": t.proxy(renames["CommentThreadRepliesIn"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["CommentThreadIn"])
    types["CommentThreadOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["CommentThreadSnippetOut"]).optional(),
            "replies": t.proxy(renames["CommentThreadRepliesOut"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentThreadOut"])
    types["VideoIn"] = t.struct(
        {
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "liveStreamingDetails": t.proxy(
                renames["VideoLiveStreamingDetailsIn"]
            ).optional(),
            "recordingDetails": t.proxy(renames["VideoRecordingDetailsIn"]).optional(),
            "id": t.string().optional(),
            "status": t.proxy(renames["VideoStatusIn"]).optional(),
            "kind": t.string().optional(),
            "processingDetails": t.proxy(
                renames["VideoProcessingDetailsIn"]
            ).optional(),
            "player": t.proxy(renames["VideoPlayerIn"]).optional(),
            "topicDetails": t.proxy(renames["VideoTopicDetailsIn"]).optional(),
            "snippet": t.proxy(renames["VideoSnippetIn"]).optional(),
            "fileDetails": t.proxy(renames["VideoFileDetailsIn"]).optional(),
            "monetizationDetails": t.proxy(
                renames["VideoMonetizationDetailsIn"]
            ).optional(),
            "suggestions": t.proxy(renames["VideoSuggestionsIn"]).optional(),
            "etag": t.string().optional(),
            "statistics": t.proxy(renames["VideoStatisticsIn"]).optional(),
            "ageGating": t.proxy(renames["VideoAgeGatingIn"]).optional(),
            "projectDetails": t.proxy(renames["VideoProjectDetailsIn"]).optional(),
            "contentDetails": t.proxy(renames["VideoContentDetailsIn"]).optional(),
        }
    ).named(renames["VideoIn"])
    types["VideoOut"] = t.struct(
        {
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "liveStreamingDetails": t.proxy(
                renames["VideoLiveStreamingDetailsOut"]
            ).optional(),
            "recordingDetails": t.proxy(renames["VideoRecordingDetailsOut"]).optional(),
            "id": t.string().optional(),
            "status": t.proxy(renames["VideoStatusOut"]).optional(),
            "kind": t.string().optional(),
            "processingDetails": t.proxy(
                renames["VideoProcessingDetailsOut"]
            ).optional(),
            "player": t.proxy(renames["VideoPlayerOut"]).optional(),
            "topicDetails": t.proxy(renames["VideoTopicDetailsOut"]).optional(),
            "snippet": t.proxy(renames["VideoSnippetOut"]).optional(),
            "fileDetails": t.proxy(renames["VideoFileDetailsOut"]).optional(),
            "monetizationDetails": t.proxy(
                renames["VideoMonetizationDetailsOut"]
            ).optional(),
            "suggestions": t.proxy(renames["VideoSuggestionsOut"]).optional(),
            "etag": t.string().optional(),
            "statistics": t.proxy(renames["VideoStatisticsOut"]).optional(),
            "ageGating": t.proxy(renames["VideoAgeGatingOut"]).optional(),
            "projectDetails": t.proxy(renames["VideoProjectDetailsOut"]).optional(),
            "contentDetails": t.proxy(renames["VideoContentDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOut"])
    types["LiveChatTextMessageDetailsIn"] = t.struct(
        {"messageText": t.string().optional()}
    ).named(renames["LiveChatTextMessageDetailsIn"])
    types["LiveChatTextMessageDetailsOut"] = t.struct(
        {
            "messageText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatTextMessageDetailsOut"])
    types["LiveBroadcastListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "visitorId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "nextPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "items": t.array(t.proxy(renames["LiveBroadcastIn"])).optional(),
        }
    ).named(renames["LiveBroadcastListResponseIn"])
    types["LiveBroadcastListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "visitorId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "items": t.array(t.proxy(renames["LiveBroadcastOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastListResponseOut"])
    types["ChannelSectionLocalizationIn"] = t.struct(
        {"title": t.string().optional()}
    ).named(renames["ChannelSectionLocalizationIn"])
    types["ChannelSectionLocalizationOut"] = t.struct(
        {
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionLocalizationOut"])
    types["ChannelStatisticsIn"] = t.struct(
        {
            "hiddenSubscriberCount": t.boolean().optional(),
            "videoCount": t.string().optional(),
            "commentCount": t.string().optional(),
            "subscriberCount": t.string().optional(),
            "viewCount": t.string().optional(),
        }
    ).named(renames["ChannelStatisticsIn"])
    types["ChannelStatisticsOut"] = t.struct(
        {
            "hiddenSubscriberCount": t.boolean().optional(),
            "videoCount": t.string().optional(),
            "commentCount": t.string().optional(),
            "subscriberCount": t.string().optional(),
            "viewCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelStatisticsOut"])
    types["LiveBroadcastContentDetailsIn"] = t.struct(
        {
            "enableAutoStart": t.boolean().optional(),
            "closedCaptionsType": t.string(),
            "mesh": t.string().optional(),
            "enableContentEncryption": t.boolean().optional(),
            "enableEmbed": t.boolean().optional(),
            "enableAutoStop": t.boolean().optional(),
            "enableLowLatency": t.boolean().optional(),
            "recordFromStart": t.boolean().optional(),
            "enableDvr": t.boolean().optional(),
            "startWithSlate": t.boolean().optional(),
            "monitorStream": t.proxy(renames["MonitorStreamInfoIn"]).optional(),
            "latencyPreference": t.string().optional(),
            "boundStreamLastUpdateTimeMs": t.string().optional(),
            "boundStreamId": t.string().optional(),
            "stereoLayout": t.string().optional(),
            "enableClosedCaptions": t.boolean().optional(),
            "projection": t.string().optional(),
        }
    ).named(renames["LiveBroadcastContentDetailsIn"])
    types["LiveBroadcastContentDetailsOut"] = t.struct(
        {
            "enableAutoStart": t.boolean().optional(),
            "closedCaptionsType": t.string(),
            "mesh": t.string().optional(),
            "enableContentEncryption": t.boolean().optional(),
            "enableEmbed": t.boolean().optional(),
            "enableAutoStop": t.boolean().optional(),
            "enableLowLatency": t.boolean().optional(),
            "recordFromStart": t.boolean().optional(),
            "enableDvr": t.boolean().optional(),
            "startWithSlate": t.boolean().optional(),
            "monitorStream": t.proxy(renames["MonitorStreamInfoOut"]).optional(),
            "latencyPreference": t.string().optional(),
            "boundStreamLastUpdateTimeMs": t.string().optional(),
            "boundStreamId": t.string().optional(),
            "stereoLayout": t.string().optional(),
            "enableClosedCaptions": t.boolean().optional(),
            "projection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastContentDetailsOut"])
    types["MemberListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]),
            "items": t.array(t.proxy(renames["MemberIn"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "visitorId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["MemberListResponseIn"])
    types["MemberListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]),
            "items": t.array(t.proxy(renames["MemberOut"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "visitorId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberListResponseOut"])
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
    types["VideoListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "eventId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "nextPageToken": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoIn"])),
        }
    ).named(renames["VideoListResponseIn"])
    types["VideoListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "eventId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "nextPageToken": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoListResponseOut"])
    types["LiveChatMessageIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatMessageSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "authorDetails": t.proxy(
                renames["LiveChatMessageAuthorDetailsIn"]
            ).optional(),
        }
    ).named(renames["LiveChatMessageIn"])
    types["LiveChatMessageOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatMessageSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "authorDetails": t.proxy(
                renames["LiveChatMessageAuthorDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageOut"])
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
    types["CaptionSnippetIn"] = t.struct(
        {
            "isLarge": t.boolean().optional(),
            "name": t.string().optional(),
            "videoId": t.string().optional(),
            "status": t.string().optional(),
            "failureReason": t.string().optional(),
            "isCC": t.boolean().optional(),
            "lastUpdated": t.string().optional(),
            "language": t.string().optional(),
            "isEasyReader": t.boolean().optional(),
            "trackKind": t.string().optional(),
            "isAutoSynced": t.boolean().optional(),
            "audioTrackType": t.string().optional(),
            "isDraft": t.boolean().optional(),
        }
    ).named(renames["CaptionSnippetIn"])
    types["CaptionSnippetOut"] = t.struct(
        {
            "isLarge": t.boolean().optional(),
            "name": t.string().optional(),
            "videoId": t.string().optional(),
            "status": t.string().optional(),
            "failureReason": t.string().optional(),
            "isCC": t.boolean().optional(),
            "lastUpdated": t.string().optional(),
            "language": t.string().optional(),
            "isEasyReader": t.boolean().optional(),
            "trackKind": t.string().optional(),
            "isAutoSynced": t.boolean().optional(),
            "audioTrackType": t.string().optional(),
            "isDraft": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaptionSnippetOut"])
    types["VideoFileDetailsAudioStreamIn"] = t.struct(
        {
            "bitrateBps": t.string().optional(),
            "codec": t.string().optional(),
            "channelCount": t.integer().optional(),
            "vendor": t.string().optional(),
        }
    ).named(renames["VideoFileDetailsAudioStreamIn"])
    types["VideoFileDetailsAudioStreamOut"] = t.struct(
        {
            "bitrateBps": t.string().optional(),
            "codec": t.string().optional(),
            "channelCount": t.integer().optional(),
            "vendor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFileDetailsAudioStreamOut"])
    types["ChannelIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "contentDetails": t.proxy(renames["ChannelContentDetailsIn"]).optional(),
            "id": t.string().optional(),
            "statistics": t.proxy(renames["ChannelStatisticsIn"]).optional(),
            "conversionPings": t.proxy(renames["ChannelConversionPingsIn"]).optional(),
            "status": t.proxy(renames["ChannelStatusIn"]).optional(),
            "auditDetails": t.proxy(renames["ChannelAuditDetailsIn"]).optional(),
            "brandingSettings": t.proxy(
                renames["ChannelBrandingSettingsIn"]
            ).optional(),
            "contentOwnerDetails": t.proxy(
                renames["ChannelContentOwnerDetailsIn"]
            ).optional(),
            "snippet": t.proxy(renames["ChannelSnippetIn"]).optional(),
            "etag": t.string().optional(),
            "topicDetails": t.proxy(renames["ChannelTopicDetailsIn"]).optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "contentDetails": t.proxy(renames["ChannelContentDetailsOut"]).optional(),
            "id": t.string().optional(),
            "statistics": t.proxy(renames["ChannelStatisticsOut"]).optional(),
            "conversionPings": t.proxy(renames["ChannelConversionPingsOut"]).optional(),
            "status": t.proxy(renames["ChannelStatusOut"]).optional(),
            "auditDetails": t.proxy(renames["ChannelAuditDetailsOut"]).optional(),
            "brandingSettings": t.proxy(
                renames["ChannelBrandingSettingsOut"]
            ).optional(),
            "contentOwnerDetails": t.proxy(
                renames["ChannelContentOwnerDetailsOut"]
            ).optional(),
            "snippet": t.proxy(renames["ChannelSnippetOut"]).optional(),
            "etag": t.string().optional(),
            "topicDetails": t.proxy(renames["ChannelTopicDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["ActivityContentDetailsChannelItemIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsChannelItemIn"])
    types["ActivityContentDetailsChannelItemOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsChannelItemOut"])
    types["ChannelProfileDetailsIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "channelId": t.string().optional(),
            "profileImageUrl": t.string().optional(),
            "channelUrl": t.string().optional(),
        }
    ).named(renames["ChannelProfileDetailsIn"])
    types["ChannelProfileDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "channelId": t.string().optional(),
            "profileImageUrl": t.string().optional(),
            "channelUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelProfileDetailsOut"])
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
    types["ThirdPartyLinkIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "status": t.proxy(renames["ThirdPartyLinkStatusIn"]).optional(),
            "etag": t.string().optional(),
            "linkingToken": t.string().optional(),
            "snippet": t.proxy(renames["ThirdPartyLinkSnippetIn"]).optional(),
        }
    ).named(renames["ThirdPartyLinkIn"])
    types["ThirdPartyLinkOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "status": t.proxy(renames["ThirdPartyLinkStatusOut"]).optional(),
            "etag": t.string().optional(),
            "linkingToken": t.string().optional(),
            "snippet": t.proxy(renames["ThirdPartyLinkSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyLinkOut"])
    types["ActivityContentDetailsFavoriteIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsFavoriteIn"])
    types["ActivityContentDetailsFavoriteOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsFavoriteOut"])
    types["CommentListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "visitorId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentIn"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["CommentListResponseIn"])
    types["CommentListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "visitorId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentOut"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentListResponseOut"])
    types["LiveBroadcastIn"] = t.struct(
        {
            "contentDetails": t.proxy(
                renames["LiveBroadcastContentDetailsIn"]
            ).optional(),
            "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
            "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiveBroadcastIn"])
    types["LiveBroadcastOut"] = t.struct(
        {
            "contentDetails": t.proxy(
                renames["LiveBroadcastContentDetailsOut"]
            ).optional(),
            "snippet": t.proxy(renames["LiveBroadcastSnippetOut"]).optional(),
            "statistics": t.proxy(renames["LiveBroadcastStatisticsOut"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["LiveBroadcastStatusOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastOut"])
    types["LiveChatSuperChatDetailsIn"] = t.struct(
        {
            "amountDisplayString": t.string().optional(),
            "amountMicros": t.string().optional(),
            "userComment": t.string().optional(),
            "currency": t.string().optional(),
            "tier": t.integer().optional(),
        }
    ).named(renames["LiveChatSuperChatDetailsIn"])
    types["LiveChatSuperChatDetailsOut"] = t.struct(
        {
            "amountDisplayString": t.string().optional(),
            "amountMicros": t.string().optional(),
            "userComment": t.string().optional(),
            "currency": t.string().optional(),
            "tier": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatSuperChatDetailsOut"])
    types["VideoRecordingDetailsIn"] = t.struct(
        {
            "recordingDate": t.string().optional(),
            "locationDescription": t.string().optional(),
            "location": t.proxy(renames["GeoPointIn"]).optional(),
        }
    ).named(renames["VideoRecordingDetailsIn"])
    types["VideoRecordingDetailsOut"] = t.struct(
        {
            "recordingDate": t.string().optional(),
            "locationDescription": t.string().optional(),
            "location": t.proxy(renames["GeoPointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoRecordingDetailsOut"])
    types["VideoStatusIn"] = t.struct(
        {
            "embeddable": t.boolean().optional(),
            "uploadStatus": t.string().optional(),
            "license": t.string().optional(),
            "publicStatsViewable": t.boolean().optional(),
            "madeForKids": t.boolean(),
            "rejectionReason": t.string().optional(),
            "selfDeclaredMadeForKids": t.boolean(),
            "publishAt": t.string().optional(),
            "privacyStatus": t.string().optional(),
            "failureReason": t.string().optional(),
        }
    ).named(renames["VideoStatusIn"])
    types["VideoStatusOut"] = t.struct(
        {
            "embeddable": t.boolean().optional(),
            "uploadStatus": t.string().optional(),
            "license": t.string().optional(),
            "publicStatsViewable": t.boolean().optional(),
            "madeForKids": t.boolean(),
            "rejectionReason": t.string().optional(),
            "selfDeclaredMadeForKids": t.boolean(),
            "publishAt": t.string().optional(),
            "privacyStatus": t.string().optional(),
            "failureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoStatusOut"])
    types["SuperChatEventIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["SuperChatEventSnippetIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["SuperChatEventIn"])
    types["SuperChatEventOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["SuperChatEventSnippetOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperChatEventOut"])
    types["LiveStreamListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "items": t.array(t.proxy(renames["LiveStreamIn"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
        }
    ).named(renames["LiveStreamListResponseIn"])
    types["LiveStreamListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "items": t.array(t.proxy(renames["LiveStreamOut"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamListResponseOut"])
    types["VideoProcessingDetailsIn"] = t.struct(
        {
            "editorSuggestionsAvailability": t.string().optional(),
            "processingFailureReason": t.string().optional(),
            "processingStatus": t.string().optional(),
            "processingProgress": t.proxy(
                renames["VideoProcessingDetailsProcessingProgressIn"]
            ).optional(),
            "tagSuggestionsAvailability": t.string().optional(),
            "thumbnailsAvailability": t.string().optional(),
            "processingIssuesAvailability": t.string().optional(),
            "fileDetailsAvailability": t.string().optional(),
        }
    ).named(renames["VideoProcessingDetailsIn"])
    types["VideoProcessingDetailsOut"] = t.struct(
        {
            "editorSuggestionsAvailability": t.string().optional(),
            "processingFailureReason": t.string().optional(),
            "processingStatus": t.string().optional(),
            "processingProgress": t.proxy(
                renames["VideoProcessingDetailsProcessingProgressOut"]
            ).optional(),
            "tagSuggestionsAvailability": t.string().optional(),
            "thumbnailsAvailability": t.string().optional(),
            "processingIssuesAvailability": t.string().optional(),
            "fileDetailsAvailability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoProcessingDetailsOut"])
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
    types["SearchResultIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.proxy(renames["ResourceIdIn"]).optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["SearchResultSnippetIn"]).optional(),
        }
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.proxy(renames["ResourceIdOut"]).optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["SearchResultSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["AbuseReportIn"] = t.struct(
        {
            "description": t.string(),
            "abuseTypes": t.array(t.proxy(renames["AbuseTypeIn"])),
            "subject": t.proxy(renames["EntityIn"]),
            "relatedEntities": t.array(t.proxy(renames["RelatedEntityIn"])),
        }
    ).named(renames["AbuseReportIn"])
    types["AbuseReportOut"] = t.struct(
        {
            "description": t.string(),
            "abuseTypes": t.array(t.proxy(renames["AbuseTypeOut"])),
            "subject": t.proxy(renames["EntityOut"]),
            "relatedEntities": t.array(t.proxy(renames["RelatedEntityOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbuseReportOut"])
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
    types["ThirdPartyLinkStatusIn"] = t.struct({"linkStatus": t.string()}).named(
        renames["ThirdPartyLinkStatusIn"]
    )
    types["ThirdPartyLinkStatusOut"] = t.struct(
        {
            "linkStatus": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyLinkStatusOut"])
    types["ContentRatingIn"] = t.struct(
        {
            "egfilmRating": t.string().optional(),
            "fpbRating": t.string().optional(),
            "mocRating": t.string().optional(),
            "nfvcbRating": t.string().optional(),
            "fskRating": t.string().optional(),
            "czfilmRating": t.string().optional(),
            "rcnofRating": t.string().optional(),
            "acbRating": t.string().optional(),
            "russiaRating": t.string().optional(),
            "eefilmRating": t.string().optional(),
            "cicfRating": t.string().optional(),
            "cscfRating": t.string().optional(),
            "anatelRating": t.string().optional(),
            "pefilmRating": t.string().optional(),
            "moctwRating": t.string().optional(),
            "eirinRating": t.string().optional(),
            "bfvcRating": t.string().optional(),
            "catvfrRating": t.string().optional(),
            "cnaRating": t.string().optional(),
            "smaisRating": t.string().optional(),
            "mtrcbRating": t.string().optional(),
            "icaaRating": t.string().optional(),
            "mdaRating": t.string().optional(),
            "mpaatRating": t.string().optional(),
            "incaaRating": t.string().optional(),
            "fmocRating": t.string().optional(),
            "tvpgRating": t.string().optional(),
            "bbfcRating": t.string().optional(),
            "medietilsynetRating": t.string().optional(),
            "nmcRating": t.string().optional(),
            "ecbmctRating": t.string().optional(),
            "lsfRating": t.string().optional(),
            "chvrsRating": t.string().optional(),
            "mccaaRating": t.string().optional(),
            "ilfilmRating": t.string().optional(),
            "grfilmRating": t.string().optional(),
            "smsaRating": t.string().optional(),
            "ifcoRating": t.string().optional(),
            "catvRating": t.string().optional(),
            "fcoRating": t.string().optional(),
            "menaMpaaRating": t.string().optional(),
            "ytRating": t.string().optional(),
            "cbfcRating": t.string().optional(),
            "oflcRating": t.string().optional(),
            "mccypRating": t.string().optional(),
            "mekuRating": t.string().optional(),
            "mpaaRating": t.string().optional(),
            "mcstRating": t.string().optional(),
            "mibacRating": t.string().optional(),
            "cncRating": t.string().optional(),
            "cceRating": t.string().optional(),
            "nkclvRating": t.string().optional(),
            "rtcRating": t.string().optional(),
            "kijkwijzerRating": t.string().optional(),
            "chfilmRating": t.string().optional(),
            "nfrcRating": t.string().optional(),
            "rteRating": t.string().optional(),
            "nbcRating": t.string().optional(),
            "bmukkRating": t.string().optional(),
            "djctqRatingReasons": t.array(t.string()).optional(),
            "cccRating": t.string().optional(),
            "fpbRatingReasons": t.array(t.string()).optional(),
            "kmrbRating": t.string().optional(),
            "csaRating": t.string().optional(),
            "agcomRating": t.string().optional(),
            "nbcplRating": t.string().optional(),
            "kfcbRating": t.string().optional(),
            "fcbmRating": t.string().optional(),
            "djctqRating": t.string().optional(),
            "resorteviolenciaRating": t.string().optional(),
            "skfilmRating": t.string().optional(),
        }
    ).named(renames["ContentRatingIn"])
    types["ContentRatingOut"] = t.struct(
        {
            "egfilmRating": t.string().optional(),
            "fpbRating": t.string().optional(),
            "mocRating": t.string().optional(),
            "nfvcbRating": t.string().optional(),
            "fskRating": t.string().optional(),
            "czfilmRating": t.string().optional(),
            "rcnofRating": t.string().optional(),
            "acbRating": t.string().optional(),
            "russiaRating": t.string().optional(),
            "eefilmRating": t.string().optional(),
            "cicfRating": t.string().optional(),
            "cscfRating": t.string().optional(),
            "anatelRating": t.string().optional(),
            "pefilmRating": t.string().optional(),
            "moctwRating": t.string().optional(),
            "eirinRating": t.string().optional(),
            "bfvcRating": t.string().optional(),
            "catvfrRating": t.string().optional(),
            "cnaRating": t.string().optional(),
            "smaisRating": t.string().optional(),
            "mtrcbRating": t.string().optional(),
            "icaaRating": t.string().optional(),
            "mdaRating": t.string().optional(),
            "mpaatRating": t.string().optional(),
            "incaaRating": t.string().optional(),
            "fmocRating": t.string().optional(),
            "tvpgRating": t.string().optional(),
            "bbfcRating": t.string().optional(),
            "medietilsynetRating": t.string().optional(),
            "nmcRating": t.string().optional(),
            "ecbmctRating": t.string().optional(),
            "lsfRating": t.string().optional(),
            "chvrsRating": t.string().optional(),
            "mccaaRating": t.string().optional(),
            "ilfilmRating": t.string().optional(),
            "grfilmRating": t.string().optional(),
            "smsaRating": t.string().optional(),
            "ifcoRating": t.string().optional(),
            "catvRating": t.string().optional(),
            "fcoRating": t.string().optional(),
            "menaMpaaRating": t.string().optional(),
            "ytRating": t.string().optional(),
            "cbfcRating": t.string().optional(),
            "oflcRating": t.string().optional(),
            "mccypRating": t.string().optional(),
            "mekuRating": t.string().optional(),
            "mpaaRating": t.string().optional(),
            "mcstRating": t.string().optional(),
            "mibacRating": t.string().optional(),
            "cncRating": t.string().optional(),
            "cceRating": t.string().optional(),
            "nkclvRating": t.string().optional(),
            "rtcRating": t.string().optional(),
            "kijkwijzerRating": t.string().optional(),
            "chfilmRating": t.string().optional(),
            "nfrcRating": t.string().optional(),
            "rteRating": t.string().optional(),
            "nbcRating": t.string().optional(),
            "bmukkRating": t.string().optional(),
            "djctqRatingReasons": t.array(t.string()).optional(),
            "cccRating": t.string().optional(),
            "fpbRatingReasons": t.array(t.string()).optional(),
            "kmrbRating": t.string().optional(),
            "csaRating": t.string().optional(),
            "agcomRating": t.string().optional(),
            "nbcplRating": t.string().optional(),
            "kfcbRating": t.string().optional(),
            "fcbmRating": t.string().optional(),
            "djctqRating": t.string().optional(),
            "resorteviolenciaRating": t.string().optional(),
            "skfilmRating": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentRatingOut"])
    types["VideoCategoryListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "visitorId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "eventId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoCategoryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["VideoCategoryListResponseIn"])
    types["VideoCategoryListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "visitorId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "eventId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoCategoryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCategoryListResponseOut"])
    types["ChannelBrandingSettingsIn"] = t.struct(
        {
            "watch": t.proxy(renames["WatchSettingsIn"]).optional(),
            "hints": t.array(t.proxy(renames["PropertyValueIn"])).optional(),
            "image": t.proxy(renames["ImageSettingsIn"]).optional(),
            "channel": t.proxy(renames["ChannelSettingsIn"]).optional(),
        }
    ).named(renames["ChannelBrandingSettingsIn"])
    types["ChannelBrandingSettingsOut"] = t.struct(
        {
            "watch": t.proxy(renames["WatchSettingsOut"]).optional(),
            "hints": t.array(t.proxy(renames["PropertyValueOut"])).optional(),
            "image": t.proxy(renames["ImageSettingsOut"]).optional(),
            "channel": t.proxy(renames["ChannelSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelBrandingSettingsOut"])
    types["LiveStreamContentDetailsIn"] = t.struct(
        {
            "closedCaptionsIngestionUrl": t.string().optional(),
            "isReusable": t.boolean().optional(),
        }
    ).named(renames["LiveStreamContentDetailsIn"])
    types["LiveStreamContentDetailsOut"] = t.struct(
        {
            "closedCaptionsIngestionUrl": t.string().optional(),
            "isReusable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamContentDetailsOut"])
    types["LiveBroadcastSnippetIn"] = t.struct(
        {
            "liveChatId": t.string().optional(),
            "title": t.string().optional(),
            "scheduledEndTime": t.string().optional(),
            "isDefaultBroadcast": t.boolean().optional(),
            "publishedAt": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "scheduledStartTime": t.string().optional(),
            "actualEndTime": t.string().optional(),
            "actualStartTime": t.string().optional(),
            "description": t.string().optional(),
            "channelId": t.string().optional(),
        }
    ).named(renames["LiveBroadcastSnippetIn"])
    types["LiveBroadcastSnippetOut"] = t.struct(
        {
            "liveChatId": t.string().optional(),
            "title": t.string().optional(),
            "scheduledEndTime": t.string().optional(),
            "isDefaultBroadcast": t.boolean().optional(),
            "publishedAt": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "scheduledStartTime": t.string().optional(),
            "actualEndTime": t.string().optional(),
            "actualStartTime": t.string().optional(),
            "description": t.string().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastSnippetOut"])
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
    types["TestItemIn"] = t.struct(
        {
            "id": t.string(),
            "featuredPart": t.boolean(),
            "snippet": t.proxy(renames["TestItemTestItemSnippetIn"]),
            "gaia": t.string(),
        }
    ).named(renames["TestItemIn"])
    types["TestItemOut"] = t.struct(
        {
            "id": t.string(),
            "featuredPart": t.boolean(),
            "snippet": t.proxy(renames["TestItemTestItemSnippetOut"]),
            "gaia": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestItemOut"])
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
    types["VideoLiveStreamingDetailsIn"] = t.struct(
        {
            "actualEndTime": t.string().optional(),
            "actualStartTime": t.string().optional(),
            "scheduledEndTime": t.string().optional(),
            "concurrentViewers": t.string().optional(),
            "activeLiveChatId": t.string().optional(),
            "scheduledStartTime": t.string().optional(),
        }
    ).named(renames["VideoLiveStreamingDetailsIn"])
    types["VideoLiveStreamingDetailsOut"] = t.struct(
        {
            "actualEndTime": t.string().optional(),
            "actualStartTime": t.string().optional(),
            "scheduledEndTime": t.string().optional(),
            "concurrentViewers": t.string().optional(),
            "activeLiveChatId": t.string().optional(),
            "scheduledStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoLiveStreamingDetailsOut"])
    types["IngestionInfoIn"] = t.struct(
        {
            "backupIngestionAddress": t.string().optional(),
            "rtmpsIngestionAddress": t.string().optional(),
            "ingestionAddress": t.string().optional(),
            "streamName": t.string().optional(),
            "rtmpsBackupIngestionAddress": t.string().optional(),
        }
    ).named(renames["IngestionInfoIn"])
    types["IngestionInfoOut"] = t.struct(
        {
            "backupIngestionAddress": t.string().optional(),
            "rtmpsIngestionAddress": t.string().optional(),
            "ingestionAddress": t.string().optional(),
            "streamName": t.string().optional(),
            "rtmpsBackupIngestionAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngestionInfoOut"])
    types["VideoSuggestionsTagSuggestionIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "categoryRestricts": t.array(t.string()).optional(),
        }
    ).named(renames["VideoSuggestionsTagSuggestionIn"])
    types["VideoSuggestionsTagSuggestionOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "categoryRestricts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoSuggestionsTagSuggestionOut"])
    types["ThirdPartyLinkSnippetIn"] = t.struct(
        {
            "channelToStoreLink": t.proxy(
                renames["ChannelToStoreLinkDetailsIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ThirdPartyLinkSnippetIn"])
    types["ThirdPartyLinkSnippetOut"] = t.struct(
        {
            "channelToStoreLink": t.proxy(
                renames["ChannelToStoreLinkDetailsOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyLinkSnippetOut"])
    types["ActivityContentDetailsBulletinIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsBulletinIn"])
    types["ActivityContentDetailsBulletinOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsBulletinOut"])
    types["PlaylistSnippetIn"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "channelTitle": t.string().optional(),
            "localized": t.proxy(renames["PlaylistLocalizationIn"]).optional(),
            "description": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "tags": t.array(t.string()).optional(),
            "defaultLanguage": t.string().optional(),
            "channelId": t.string().optional(),
            "title": t.string().optional(),
            "thumbnailVideoId": t.string().optional(),
        }
    ).named(renames["PlaylistSnippetIn"])
    types["PlaylistSnippetOut"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "channelTitle": t.string().optional(),
            "localized": t.proxy(renames["PlaylistLocalizationOut"]).optional(),
            "description": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "tags": t.array(t.string()).optional(),
            "defaultLanguage": t.string().optional(),
            "channelId": t.string().optional(),
            "title": t.string().optional(),
            "thumbnailVideoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistSnippetOut"])
    types["ActivityContentDetailsCommentIn"] = t.struct(
        {"resourceId": t.proxy(renames["ResourceIdIn"]).optional()}
    ).named(renames["ActivityContentDetailsCommentIn"])
    types["ActivityContentDetailsCommentOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsCommentOut"])
    types["CommentThreadRepliesIn"] = t.struct(
        {"comments": t.array(t.proxy(renames["CommentIn"])).optional()}
    ).named(renames["CommentThreadRepliesIn"])
    types["CommentThreadRepliesOut"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentThreadRepliesOut"])
    types["LanguageTagIn"] = t.struct({"value": t.string()}).named(
        renames["LanguageTagIn"]
    )
    types["LanguageTagOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LanguageTagOut"])
    types["ChannelConversionPingsIn"] = t.struct(
        {"pings": t.array(t.proxy(renames["ChannelConversionPingIn"])).optional()}
    ).named(renames["ChannelConversionPingsIn"])
    types["ChannelConversionPingsOut"] = t.struct(
        {
            "pings": t.array(t.proxy(renames["ChannelConversionPingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelConversionPingsOut"])
    types["VideoAbuseReportReasonListResponseIn"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoAbuseReportReasonIn"])).optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["VideoAbuseReportReasonListResponseIn"])
    types["VideoAbuseReportReasonListResponseOut"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoAbuseReportReasonOut"])).optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportReasonListResponseOut"])
    types["LiveStreamConfigurationIssueIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["LiveStreamConfigurationIssueIn"])
    types["LiveStreamConfigurationIssueOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamConfigurationIssueOut"])
    types["ActivityContentDetailsPromotedItemIn"] = t.struct(
        {
            "adTag": t.string().optional(),
            "videoId": t.string().optional(),
            "creativeViewUrl": t.string().optional(),
            "forecastingUrl": t.array(t.string()).optional(),
            "clickTrackingUrl": t.string().optional(),
            "impressionUrl": t.array(t.string()).optional(),
            "customCtaButtonText": t.string().optional(),
            "descriptionText": t.string().optional(),
            "destinationUrl": t.string().optional(),
            "ctaType": t.string().optional(),
        }
    ).named(renames["ActivityContentDetailsPromotedItemIn"])
    types["ActivityContentDetailsPromotedItemOut"] = t.struct(
        {
            "adTag": t.string().optional(),
            "videoId": t.string().optional(),
            "creativeViewUrl": t.string().optional(),
            "forecastingUrl": t.array(t.string()).optional(),
            "clickTrackingUrl": t.string().optional(),
            "impressionUrl": t.array(t.string()).optional(),
            "customCtaButtonText": t.string().optional(),
            "descriptionText": t.string().optional(),
            "destinationUrl": t.string().optional(),
            "ctaType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsPromotedItemOut"])
    types["I18nRegionIn"] = t.struct(
        {
            "snippet": t.proxy(renames["I18nRegionSnippetIn"]).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["I18nRegionIn"])
    types["I18nRegionOut"] = t.struct(
        {
            "snippet": t.proxy(renames["I18nRegionSnippetOut"]).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nRegionOut"])
    types["EntityIn"] = t.struct(
        {"url": t.string(), "id": t.string(), "typeId": t.string()}
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "url": t.string(),
            "id": t.string(),
            "typeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["VideoCategoryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["VideoCategorySnippetIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["VideoCategoryIn"])
    types["VideoCategoryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["VideoCategorySnippetOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCategoryOut"])
    types["SubscriptionSnippetIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "channelTitle": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "publishedAt": t.string().optional(),
            "channelId": t.string().optional(),
        }
    ).named(renames["SubscriptionSnippetIn"])
    types["SubscriptionSnippetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "channelTitle": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "publishedAt": t.string().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionSnippetOut"])
    types["CommentThreadListResponseIn"] = t.struct(
        {
            "eventId": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentThreadIn"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "nextPageToken": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["CommentThreadListResponseIn"])
    types["CommentThreadListResponseOut"] = t.struct(
        {
            "eventId": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentThreadOut"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentThreadListResponseOut"])
    types["I18nRegionListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["I18nRegionIn"])).optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["I18nRegionListResponseIn"])
    types["I18nRegionListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["I18nRegionOut"])).optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nRegionListResponseOut"])
    types["LiveChatUserBannedMessageDetailsIn"] = t.struct(
        {
            "bannedUserDetails": t.proxy(renames["ChannelProfileDetailsIn"]).optional(),
            "banDurationSeconds": t.string().optional(),
            "banType": t.string().optional(),
        }
    ).named(renames["LiveChatUserBannedMessageDetailsIn"])
    types["LiveChatUserBannedMessageDetailsOut"] = t.struct(
        {
            "bannedUserDetails": t.proxy(
                renames["ChannelProfileDetailsOut"]
            ).optional(),
            "banDurationSeconds": t.string().optional(),
            "banType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatUserBannedMessageDetailsOut"])
    types["VideoTopicDetailsIn"] = t.struct(
        {
            "topicIds": t.array(t.string()).optional(),
            "topicCategories": t.array(t.string()).optional(),
            "relevantTopicIds": t.array(t.string()).optional(),
        }
    ).named(renames["VideoTopicDetailsIn"])
    types["VideoTopicDetailsOut"] = t.struct(
        {
            "topicIds": t.array(t.string()).optional(),
            "topicCategories": t.array(t.string()).optional(),
            "relevantTopicIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoTopicDetailsOut"])
    types["VideoContentDetailsRegionRestrictionIn"] = t.struct(
        {
            "allowed": t.array(t.string()).optional(),
            "blocked": t.array(t.string()).optional(),
        }
    ).named(renames["VideoContentDetailsRegionRestrictionIn"])
    types["VideoContentDetailsRegionRestrictionOut"] = t.struct(
        {
            "allowed": t.array(t.string()).optional(),
            "blocked": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoContentDetailsRegionRestrictionOut"])
    types["GeoPointIn"] = t.struct(
        {
            "latitude": t.number().optional(),
            "altitude": t.number().optional(),
            "longitude": t.number().optional(),
        }
    ).named(renames["GeoPointIn"])
    types["GeoPointOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "altitude": t.number().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoPointOut"])
    types["LiveChatModeratorIn"] = t.struct(
        {
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatModeratorSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["LiveChatModeratorIn"])
    types["LiveChatModeratorOut"] = t.struct(
        {
            "id": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatModeratorSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatModeratorOut"])
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
    types["CaptionListResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["CaptionIn"])).optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
        }
    ).named(renames["CaptionListResponseIn"])
    types["CaptionListResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["CaptionOut"])).optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaptionListResponseOut"])
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
    types["LiveChatMessageListResponseIn"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "offlineAt": t.string().optional(),
            "etag": t.string().optional(),
            "pollingIntervalMillis": t.integer().optional(),
            "nextPageToken": t.string(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["LiveChatMessageIn"])),
        }
    ).named(renames["LiveChatMessageListResponseIn"])
    types["LiveChatMessageListResponseOut"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "offlineAt": t.string().optional(),
            "etag": t.string().optional(),
            "pollingIntervalMillis": t.integer().optional(),
            "nextPageToken": t.string(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["LiveChatMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageListResponseOut"])
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
    types["PlaylistItemListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "eventId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string(),
            "items": t.array(t.proxy(renames["PlaylistItemIn"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "visitorId": t.string().optional(),
        }
    ).named(renames["PlaylistItemListResponseIn"])
    types["PlaylistItemListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "eventId": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string(),
            "items": t.array(t.proxy(renames["PlaylistItemOut"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemListResponseOut"])
    types["VideoPlayerIn"] = t.struct(
        {
            "embedWidth": t.string().optional(),
            "embedHeight": t.string(),
            "embedHtml": t.string().optional(),
        }
    ).named(renames["VideoPlayerIn"])
    types["VideoPlayerOut"] = t.struct(
        {
            "embedWidth": t.string().optional(),
            "embedHeight": t.string(),
            "embedHtml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoPlayerOut"])
    types["TestItemTestItemSnippetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TestItemTestItemSnippetIn"]
    )
    types["TestItemTestItemSnippetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TestItemTestItemSnippetOut"])
    types["LiveChatBanSnippetIn"] = t.struct(
        {
            "banDurationSeconds": t.string().optional(),
            "bannedUserDetails": t.proxy(renames["ChannelProfileDetailsIn"]),
            "liveChatId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["LiveChatBanSnippetIn"])
    types["LiveChatBanSnippetOut"] = t.struct(
        {
            "banDurationSeconds": t.string().optional(),
            "bannedUserDetails": t.proxy(renames["ChannelProfileDetailsOut"]),
            "liveChatId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatBanSnippetOut"])
    types["VideoContentDetailsIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "projection": t.string().optional(),
            "caption": t.string().optional(),
            "contentRating": t.proxy(renames["ContentRatingIn"]).optional(),
            "hasCustomThumbnail": t.boolean().optional(),
            "definition": t.string().optional(),
            "licensedContent": t.boolean().optional(),
            "dimension": t.string().optional(),
            "regionRestriction": t.proxy(
                renames["VideoContentDetailsRegionRestrictionIn"]
            ).optional(),
            "countryRestriction": t.proxy(renames["AccessPolicyIn"]).optional(),
        }
    ).named(renames["VideoContentDetailsIn"])
    types["VideoContentDetailsOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "projection": t.string().optional(),
            "caption": t.string().optional(),
            "contentRating": t.proxy(renames["ContentRatingOut"]).optional(),
            "hasCustomThumbnail": t.boolean().optional(),
            "definition": t.string().optional(),
            "licensedContent": t.boolean().optional(),
            "dimension": t.string().optional(),
            "regionRestriction": t.proxy(
                renames["VideoContentDetailsRegionRestrictionOut"]
            ).optional(),
            "countryRestriction": t.proxy(renames["AccessPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoContentDetailsOut"])
    types["LiveChatModeratorListResponseIn"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "etag": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "items": t.array(t.proxy(renames["LiveChatModeratorIn"])).optional(),
        }
    ).named(renames["LiveChatModeratorListResponseIn"])
    types["LiveChatModeratorListResponseOut"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "etag": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "items": t.array(t.proxy(renames["LiveChatModeratorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatModeratorListResponseOut"])
    types["MembershipsDetailsIn"] = t.struct(
        {
            "membershipsDuration": t.proxy(renames["MembershipsDurationIn"]).optional(),
            "highestAccessibleLevel": t.string().optional(),
            "highestAccessibleLevelDisplayName": t.string().optional(),
            "accessibleLevels": t.array(t.string()).optional(),
            "membershipsDurationAtLevels": t.array(
                t.proxy(renames["MembershipsDurationAtLevelIn"])
            ).optional(),
        }
    ).named(renames["MembershipsDetailsIn"])
    types["MembershipsDetailsOut"] = t.struct(
        {
            "membershipsDuration": t.proxy(
                renames["MembershipsDurationOut"]
            ).optional(),
            "highestAccessibleLevel": t.string().optional(),
            "highestAccessibleLevelDisplayName": t.string().optional(),
            "accessibleLevels": t.array(t.string()).optional(),
            "membershipsDurationAtLevels": t.array(
                t.proxy(renames["MembershipsDurationAtLevelOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsDetailsOut"])
    types["LiveChatBanIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatBanSnippetIn"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["LiveChatBanIn"])
    types["LiveChatBanOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["LiveChatBanSnippetOut"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatBanOut"])
    types["VideoAbuseReportIn"] = t.struct(
        {
            "videoId": t.string().optional(),
            "reasonId": t.string().optional(),
            "secondaryReasonId": t.string().optional(),
            "language": t.string().optional(),
            "comments": t.string().optional(),
        }
    ).named(renames["VideoAbuseReportIn"])
    types["VideoAbuseReportOut"] = t.struct(
        {
            "videoId": t.string().optional(),
            "reasonId": t.string().optional(),
            "secondaryReasonId": t.string().optional(),
            "language": t.string().optional(),
            "comments": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportOut"])
    types["ResourceIdIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "channelId": t.string().optional(),
            "playlistId": t.string().optional(),
            "videoId": t.string().optional(),
        }
    ).named(renames["ResourceIdIn"])
    types["ResourceIdOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "channelId": t.string().optional(),
            "playlistId": t.string().optional(),
            "videoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceIdOut"])
    types["CaptionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CaptionIn"])
    types["CaptionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["CaptionSnippetOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaptionOut"])
    types["VideoAbuseReportReasonIn"] = t.struct(
        {
            "snippet": t.proxy(renames["VideoAbuseReportReasonSnippetIn"]).optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["VideoAbuseReportReasonIn"])
    types["VideoAbuseReportReasonOut"] = t.struct(
        {
            "snippet": t.proxy(renames["VideoAbuseReportReasonSnippetOut"]).optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportReasonOut"])
    types["MembershipsLevelIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["MembershipsLevelSnippetIn"]).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["MembershipsLevelIn"])
    types["MembershipsLevelOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["MembershipsLevelSnippetOut"]).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsLevelOut"])
    types["SearchResultSnippetIn"] = t.struct(
        {
            "title": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "channelTitle": t.string().optional(),
            "publishedAt": t.string().optional(),
            "liveBroadcastContent": t.string().optional(),
            "channelId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SearchResultSnippetIn"])
    types["SearchResultSnippetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "channelTitle": t.string().optional(),
            "publishedAt": t.string().optional(),
            "liveBroadcastContent": t.string().optional(),
            "channelId": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultSnippetOut"])
    types["ThumbnailDetailsIn"] = t.struct(
        {
            "medium": t.proxy(renames["ThumbnailIn"]).optional(),
            "standard": t.proxy(renames["ThumbnailIn"]).optional(),
            "maxres": t.proxy(renames["ThumbnailIn"]).optional(),
            "default": t.proxy(renames["ThumbnailIn"]).optional(),
            "high": t.proxy(renames["ThumbnailIn"]).optional(),
        }
    ).named(renames["ThumbnailDetailsIn"])
    types["ThumbnailDetailsOut"] = t.struct(
        {
            "medium": t.proxy(renames["ThumbnailOut"]).optional(),
            "standard": t.proxy(renames["ThumbnailOut"]).optional(),
            "maxres": t.proxy(renames["ThumbnailOut"]).optional(),
            "default": t.proxy(renames["ThumbnailOut"]).optional(),
            "high": t.proxy(renames["ThumbnailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailDetailsOut"])
    types["ChannelSnippetIn"] = t.struct(
        {
            "description": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "customUrl": t.string().optional(),
            "publishedAt": t.string().optional(),
            "title": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "country": t.string().optional(),
            "localized": t.proxy(renames["ChannelLocalizationIn"]).optional(),
        }
    ).named(renames["ChannelSnippetIn"])
    types["ChannelSnippetOut"] = t.struct(
        {
            "description": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "customUrl": t.string().optional(),
            "publishedAt": t.string().optional(),
            "title": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "country": t.string().optional(),
            "localized": t.proxy(renames["ChannelLocalizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSnippetOut"])
    types["CommentSnippetIn"] = t.struct(
        {
            "textOriginal": t.string().optional(),
            "parentId": t.string().optional(),
            "channelId": t.string().optional(),
            "updatedAt": t.string().optional(),
            "viewerRating": t.string().optional(),
            "textDisplay": t.string().optional(),
            "videoId": t.string().optional(),
            "authorProfileImageUrl": t.string().optional(),
            "authorChannelUrl": t.string().optional(),
            "publishedAt": t.string().optional(),
            "canRate": t.boolean().optional(),
            "moderationStatus": t.string().optional(),
            "likeCount": t.integer().optional(),
            "authorDisplayName": t.string().optional(),
            "authorChannelId": t.proxy(renames["CommentSnippetAuthorChannelIdIn"]),
        }
    ).named(renames["CommentSnippetIn"])
    types["CommentSnippetOut"] = t.struct(
        {
            "textOriginal": t.string().optional(),
            "parentId": t.string().optional(),
            "channelId": t.string().optional(),
            "updatedAt": t.string().optional(),
            "viewerRating": t.string().optional(),
            "textDisplay": t.string().optional(),
            "videoId": t.string().optional(),
            "authorProfileImageUrl": t.string().optional(),
            "authorChannelUrl": t.string().optional(),
            "publishedAt": t.string().optional(),
            "canRate": t.boolean().optional(),
            "moderationStatus": t.string().optional(),
            "likeCount": t.integer().optional(),
            "authorDisplayName": t.string().optional(),
            "authorChannelId": t.proxy(renames["CommentSnippetAuthorChannelIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentSnippetOut"])
    types["ActivityContentDetailsIn"] = t.struct(
        {
            "like": t.proxy(renames["ActivityContentDetailsLikeIn"]).optional(),
            "recommendation": t.proxy(
                renames["ActivityContentDetailsRecommendationIn"]
            ).optional(),
            "upload": t.proxy(renames["ActivityContentDetailsUploadIn"]).optional(),
            "playlistItem": t.proxy(
                renames["ActivityContentDetailsPlaylistItemIn"]
            ).optional(),
            "promotedItem": t.proxy(
                renames["ActivityContentDetailsPromotedItemIn"]
            ).optional(),
            "favorite": t.proxy(renames["ActivityContentDetailsFavoriteIn"]).optional(),
            "bulletin": t.proxy(renames["ActivityContentDetailsBulletinIn"]).optional(),
            "social": t.proxy(renames["ActivityContentDetailsSocialIn"]).optional(),
            "subscription": t.proxy(
                renames["ActivityContentDetailsSubscriptionIn"]
            ).optional(),
            "comment": t.proxy(renames["ActivityContentDetailsCommentIn"]).optional(),
            "channelItem": t.proxy(
                renames["ActivityContentDetailsChannelItemIn"]
            ).optional(),
        }
    ).named(renames["ActivityContentDetailsIn"])
    types["ActivityContentDetailsOut"] = t.struct(
        {
            "like": t.proxy(renames["ActivityContentDetailsLikeOut"]).optional(),
            "recommendation": t.proxy(
                renames["ActivityContentDetailsRecommendationOut"]
            ).optional(),
            "upload": t.proxy(renames["ActivityContentDetailsUploadOut"]).optional(),
            "playlistItem": t.proxy(
                renames["ActivityContentDetailsPlaylistItemOut"]
            ).optional(),
            "promotedItem": t.proxy(
                renames["ActivityContentDetailsPromotedItemOut"]
            ).optional(),
            "favorite": t.proxy(
                renames["ActivityContentDetailsFavoriteOut"]
            ).optional(),
            "bulletin": t.proxy(
                renames["ActivityContentDetailsBulletinOut"]
            ).optional(),
            "social": t.proxy(renames["ActivityContentDetailsSocialOut"]).optional(),
            "subscription": t.proxy(
                renames["ActivityContentDetailsSubscriptionOut"]
            ).optional(),
            "comment": t.proxy(renames["ActivityContentDetailsCommentOut"]).optional(),
            "channelItem": t.proxy(
                renames["ActivityContentDetailsChannelItemOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsOut"])
    types["LiveChatMessageDeletedDetailsIn"] = t.struct(
        {"deletedMessageId": t.string()}
    ).named(renames["LiveChatMessageDeletedDetailsIn"])
    types["LiveChatMessageDeletedDetailsOut"] = t.struct(
        {
            "deletedMessageId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageDeletedDetailsOut"])
    types["WatchSettingsIn"] = t.struct(
        {
            "backgroundColor": t.string().optional(),
            "textColor": t.string().optional(),
            "featuredPlaylistId": t.string().optional(),
        }
    ).named(renames["WatchSettingsIn"])
    types["WatchSettingsOut"] = t.struct(
        {
            "backgroundColor": t.string().optional(),
            "textColor": t.string().optional(),
            "featuredPlaylistId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchSettingsOut"])
    types["ChannelStatusIn"] = t.struct(
        {
            "isLinked": t.boolean().optional(),
            "privacyStatus": t.string().optional(),
            "madeForKids": t.boolean(),
            "longUploadsStatus": t.string().optional(),
            "selfDeclaredMadeForKids": t.boolean(),
        }
    ).named(renames["ChannelStatusIn"])
    types["ChannelStatusOut"] = t.struct(
        {
            "isLinked": t.boolean().optional(),
            "privacyStatus": t.string().optional(),
            "madeForKids": t.boolean(),
            "longUploadsStatus": t.string().optional(),
            "selfDeclaredMadeForKids": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelStatusOut"])
    types["LiveChatMessageAuthorDetailsIn"] = t.struct(
        {
            "isChatSponsor": t.boolean().optional(),
            "isVerified": t.boolean().optional(),
            "isChatModerator": t.boolean().optional(),
            "isChatOwner": t.boolean().optional(),
            "channelId": t.string().optional(),
            "channelUrl": t.string().optional(),
            "profileImageUrl": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LiveChatMessageAuthorDetailsIn"])
    types["LiveChatMessageAuthorDetailsOut"] = t.struct(
        {
            "isChatSponsor": t.boolean().optional(),
            "isVerified": t.boolean().optional(),
            "isChatModerator": t.boolean().optional(),
            "isChatOwner": t.boolean().optional(),
            "channelId": t.string().optional(),
            "channelUrl": t.string().optional(),
            "profileImageUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageAuthorDetailsOut"])
    types["ThumbnailSetResponseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["ThumbnailDetailsIn"])).optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ThumbnailSetResponseIn"])
    types["ThumbnailSetResponseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["ThumbnailDetailsOut"])).optional(),
            "visitorId": t.string().optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailSetResponseOut"])
    types["ChannelSectionSnippetIn"] = t.struct(
        {
            "title": t.string().optional(),
            "localized": t.proxy(renames["ChannelSectionLocalizationIn"]).optional(),
            "style": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "channelId": t.string().optional(),
            "position": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ChannelSectionSnippetIn"])
    types["ChannelSectionSnippetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "localized": t.proxy(renames["ChannelSectionLocalizationOut"]).optional(),
            "style": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "channelId": t.string().optional(),
            "position": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionSnippetOut"])
    types["SearchListResponseIn"] = t.struct(
        {
            "prevPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "regionCode": t.string(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["SearchResultIn"])).optional(),
        }
    ).named(renames["SearchListResponseIn"])
    types["SearchListResponseOut"] = t.struct(
        {
            "prevPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "visitorId": t.string().optional(),
            "etag": t.string().optional(),
            "regionCode": t.string(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchListResponseOut"])
    types["VideoSuggestionsIn"] = t.struct(
        {
            "tagSuggestions": t.array(
                t.proxy(renames["VideoSuggestionsTagSuggestionIn"])
            ).optional(),
            "processingWarnings": t.array(t.string()).optional(),
            "processingErrors": t.array(t.string()).optional(),
            "processingHints": t.array(t.string()).optional(),
            "editorSuggestions": t.array(t.string()).optional(),
        }
    ).named(renames["VideoSuggestionsIn"])
    types["VideoSuggestionsOut"] = t.struct(
        {
            "tagSuggestions": t.array(
                t.proxy(renames["VideoSuggestionsTagSuggestionOut"])
            ).optional(),
            "processingWarnings": t.array(t.string()).optional(),
            "processingErrors": t.array(t.string()).optional(),
            "processingHints": t.array(t.string()).optional(),
            "editorSuggestions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoSuggestionsOut"])
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
    types["ActivityContentDetailsUploadIn"] = t.struct(
        {"videoId": t.string().optional()}
    ).named(renames["ActivityContentDetailsUploadIn"])
    types["ActivityContentDetailsUploadOut"] = t.struct(
        {
            "videoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsUploadOut"])
    types["AbuseTypeIn"] = t.struct({"id": t.string()}).named(renames["AbuseTypeIn"])
    types["AbuseTypeOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbuseTypeOut"])
    types["ActivityContentDetailsRecommendationIn"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
            "reason": t.string().optional(),
            "seedResourceId": t.proxy(renames["ResourceIdIn"]).optional(),
        }
    ).named(renames["ActivityContentDetailsRecommendationIn"])
    types["ActivityContentDetailsRecommendationOut"] = t.struct(
        {
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "reason": t.string().optional(),
            "seedResourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityContentDetailsRecommendationOut"])
    types["VideoAgeGatingIn"] = t.struct(
        {
            "alcoholContent": t.boolean().optional(),
            "videoGameRating": t.string().optional(),
            "restricted": t.boolean().optional(),
        }
    ).named(renames["VideoAgeGatingIn"])
    types["VideoAgeGatingOut"] = t.struct(
        {
            "alcoholContent": t.boolean().optional(),
            "videoGameRating": t.string().optional(),
            "restricted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAgeGatingOut"])
    types["SubscriptionListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["SubscriptionIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "prevPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
        }
    ).named(renames["SubscriptionListResponseIn"])
    types["SubscriptionListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["SubscriptionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "prevPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionListResponseOut"])
    types["PlaylistItemSnippetIn"] = t.struct(
        {
            "channelId": t.string().optional(),
            "videoOwnerChannelId": t.string().optional(),
            "publishedAt": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdIn"]).optional(),
            "playlistId": t.string().optional(),
            "position": t.integer().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "channelTitle": t.string().optional(),
            "videoOwnerChannelTitle": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
        }
    ).named(renames["PlaylistItemSnippetIn"])
    types["PlaylistItemSnippetOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "videoOwnerChannelId": t.string().optional(),
            "publishedAt": t.string().optional(),
            "resourceId": t.proxy(renames["ResourceIdOut"]).optional(),
            "playlistId": t.string().optional(),
            "position": t.integer().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "channelTitle": t.string().optional(),
            "videoOwnerChannelTitle": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemSnippetOut"])
    types["MembershipsLevelListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["MembershipsLevelIn"])).optional(),
            "visitorId": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["MembershipsLevelListResponseIn"])
    types["MembershipsLevelListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["MembershipsLevelOut"])).optional(),
            "visitorId": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsLevelListResponseOut"])
    types["ActivitySnippetIn"] = t.struct(
        {
            "description": t.string().optional(),
            "channelTitle": t.string().optional(),
            "channelId": t.string().optional(),
            "publishedAt": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
            "groupId": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
        }
    ).named(renames["ActivitySnippetIn"])
    types["ActivitySnippetOut"] = t.struct(
        {
            "description": t.string().optional(),
            "channelTitle": t.string().optional(),
            "channelId": t.string().optional(),
            "publishedAt": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
            "groupId": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitySnippetOut"])
    types["LiveChatMessageRetractedDetailsIn"] = t.struct(
        {"retractedMessageId": t.string()}
    ).named(renames["LiveChatMessageRetractedDetailsIn"])
    types["LiveChatMessageRetractedDetailsOut"] = t.struct(
        {
            "retractedMessageId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMessageRetractedDetailsOut"])
    types["LiveBroadcastStatisticsIn"] = t.struct(
        {"concurrentViewers": t.string().optional()}
    ).named(renames["LiveBroadcastStatisticsIn"])
    types["LiveBroadcastStatisticsOut"] = t.struct(
        {
            "concurrentViewers": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastStatisticsOut"])
    types["VideoGetRatingResponseIn"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoRatingIn"])).optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["VideoGetRatingResponseIn"])
    types["VideoGetRatingResponseOut"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["VideoRatingOut"])).optional(),
            "eventId": t.string().optional(),
            "etag": t.string().optional(),
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
    types["LiveBroadcastStatusIn"] = t.struct(
        {
            "privacyStatus": t.string().optional(),
            "liveBroadcastPriority": t.string().optional(),
            "lifeCycleStatus": t.string().optional(),
            "selfDeclaredMadeForKids": t.boolean().optional(),
            "recordingStatus": t.string().optional(),
            "madeForKids": t.boolean().optional(),
        }
    ).named(renames["LiveBroadcastStatusIn"])
    types["LiveBroadcastStatusOut"] = t.struct(
        {
            "privacyStatus": t.string().optional(),
            "liveBroadcastPriority": t.string().optional(),
            "lifeCycleStatus": t.string().optional(),
            "selfDeclaredMadeForKids": t.boolean().optional(),
            "recordingStatus": t.string().optional(),
            "madeForKids": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveBroadcastStatusOut"])
    types["VideoLocalizationIn"] = t.struct(
        {"description": t.string().optional(), "title": t.string().optional()}
    ).named(renames["VideoLocalizationIn"])
    types["VideoLocalizationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoLocalizationOut"])
    types["VideoAbuseReportSecondaryReasonIn"] = t.struct(
        {"id": t.string().optional(), "label": t.string().optional()}
    ).named(renames["VideoAbuseReportSecondaryReasonIn"])
    types["VideoAbuseReportSecondaryReasonOut"] = t.struct(
        {
            "id": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoAbuseReportSecondaryReasonOut"])
    types["VideoProcessingDetailsProcessingProgressIn"] = t.struct(
        {
            "timeLeftMs": t.string().optional(),
            "partsTotal": t.string().optional(),
            "partsProcessed": t.string().optional(),
        }
    ).named(renames["VideoProcessingDetailsProcessingProgressIn"])
    types["VideoProcessingDetailsProcessingProgressOut"] = t.struct(
        {
            "timeLeftMs": t.string().optional(),
            "partsTotal": t.string().optional(),
            "partsProcessed": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoProcessingDetailsProcessingProgressOut"])
    types["RelatedEntityIn"] = t.struct({"entity": t.proxy(renames["EntityIn"])}).named(
        renames["RelatedEntityIn"]
    )
    types["RelatedEntityOut"] = t.struct(
        {
            "entity": t.proxy(renames["EntityOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedEntityOut"])
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
    types["SuperStickerMetadataIn"] = t.struct(
        {
            "altTextLanguage": t.string().optional(),
            "altText": t.string().optional(),
            "stickerId": t.string().optional(),
        }
    ).named(renames["SuperStickerMetadataIn"])
    types["SuperStickerMetadataOut"] = t.struct(
        {
            "altTextLanguage": t.string().optional(),
            "altText": t.string().optional(),
            "stickerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperStickerMetadataOut"])
    types["ActivityIn"] = t.struct(
        {
            "snippet": t.proxy(renames["ActivitySnippetIn"]).optional(),
            "etag": t.string().optional(),
            "contentDetails": t.proxy(renames["ActivityContentDetailsIn"]).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ActivityIn"])
    types["ActivityOut"] = t.struct(
        {
            "snippet": t.proxy(renames["ActivitySnippetOut"]).optional(),
            "etag": t.string().optional(),
            "contentDetails": t.proxy(renames["ActivityContentDetailsOut"]).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityOut"])
    types["PlaylistLocalizationIn"] = t.struct(
        {"description": t.string().optional(), "title": t.string().optional()}
    ).named(renames["PlaylistLocalizationIn"])
    types["PlaylistLocalizationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistLocalizationOut"])
    types["VideoFileDetailsIn"] = t.struct(
        {
            "videoStreams": t.array(
                t.proxy(renames["VideoFileDetailsVideoStreamIn"])
            ).optional(),
            "durationMs": t.string().optional(),
            "fileSize": t.string().optional(),
            "audioStreams": t.array(
                t.proxy(renames["VideoFileDetailsAudioStreamIn"])
            ).optional(),
            "bitrateBps": t.string().optional(),
            "fileType": t.string().optional(),
            "fileName": t.string().optional(),
            "creationTime": t.string().optional(),
            "container": t.string().optional(),
        }
    ).named(renames["VideoFileDetailsIn"])
    types["VideoFileDetailsOut"] = t.struct(
        {
            "videoStreams": t.array(
                t.proxy(renames["VideoFileDetailsVideoStreamOut"])
            ).optional(),
            "durationMs": t.string().optional(),
            "fileSize": t.string().optional(),
            "audioStreams": t.array(
                t.proxy(renames["VideoFileDetailsAudioStreamOut"])
            ).optional(),
            "bitrateBps": t.string().optional(),
            "fileType": t.string().optional(),
            "fileName": t.string().optional(),
            "creationTime": t.string().optional(),
            "container": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoFileDetailsOut"])
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
    types["CommentSnippetAuthorChannelIdIn"] = t.struct({"value": t.string()}).named(
        renames["CommentSnippetAuthorChannelIdIn"]
    )
    types["CommentSnippetAuthorChannelIdOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommentSnippetAuthorChannelIdOut"])
    types["LiveStreamHealthStatusIn"] = t.struct(
        {
            "lastUpdateTimeSeconds": t.string().optional(),
            "status": t.string().optional(),
            "configurationIssues": t.array(
                t.proxy(renames["LiveStreamConfigurationIssueIn"])
            ).optional(),
        }
    ).named(renames["LiveStreamHealthStatusIn"])
    types["LiveStreamHealthStatusOut"] = t.struct(
        {
            "lastUpdateTimeSeconds": t.string().optional(),
            "status": t.string().optional(),
            "configurationIssues": t.array(
                t.proxy(renames["LiveStreamConfigurationIssueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamHealthStatusOut"])
    types["VideoMonetizationDetailsIn"] = t.struct(
        {"access": t.proxy(renames["AccessPolicyIn"]).optional()}
    ).named(renames["VideoMonetizationDetailsIn"])
    types["VideoMonetizationDetailsOut"] = t.struct(
        {
            "access": t.proxy(renames["AccessPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoMonetizationDetailsOut"])
    types["PlaylistItemIn"] = t.struct(
        {
            "contentDetails": t.proxy(
                renames["PlaylistItemContentDetailsIn"]
            ).optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["PlaylistItemSnippetIn"]).optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["PlaylistItemStatusIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlaylistItemIn"])
    types["PlaylistItemOut"] = t.struct(
        {
            "contentDetails": t.proxy(
                renames["PlaylistItemContentDetailsOut"]
            ).optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["PlaylistItemSnippetOut"]).optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["PlaylistItemStatusOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemOut"])
    types["ActivityListResponseIn"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["ActivityIn"])),
            "prevPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "etag": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
        }
    ).named(renames["ActivityListResponseIn"])
    types["ActivityListResponseOut"] = t.struct(
        {
            "visitorId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["ActivityOut"])),
            "prevPageToken": t.string().optional(),
            "eventId": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "etag": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityListResponseOut"])
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
    types["PlaylistItemStatusIn"] = t.struct(
        {"privacyStatus": t.string().optional()}
    ).named(renames["PlaylistItemStatusIn"])
    types["PlaylistItemStatusOut"] = t.struct(
        {
            "privacyStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemStatusOut"])
    types["ChannelSectionContentDetailsIn"] = t.struct(
        {
            "channels": t.array(t.string()).optional(),
            "playlists": t.array(t.string()).optional(),
        }
    ).named(renames["ChannelSectionContentDetailsIn"])
    types["ChannelSectionContentDetailsOut"] = t.struct(
        {
            "channels": t.array(t.string()).optional(),
            "playlists": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSectionContentDetailsOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "contentDetails": t.proxy(
                renames["SubscriptionContentDetailsIn"]
            ).optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["SubscriptionSnippetIn"]).optional(),
            "subscriberSnippet": t.proxy(
                renames["SubscriptionSubscriberSnippetIn"]
            ).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "contentDetails": t.proxy(
                renames["SubscriptionContentDetailsOut"]
            ).optional(),
            "id": t.string().optional(),
            "snippet": t.proxy(renames["SubscriptionSnippetOut"]).optional(),
            "subscriberSnippet": t.proxy(
                renames["SubscriptionSubscriberSnippetOut"]
            ).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["MemberIn"] = t.struct(
        {
            "snippet": t.proxy(renames["MemberSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["MemberIn"])
    types["MemberOut"] = t.struct(
        {
            "snippet": t.proxy(renames["MemberSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberOut"])
    types["CdnSettingsIn"] = t.struct(
        {
            "ingestionInfo": t.proxy(renames["IngestionInfoIn"]).optional(),
            "frameRate": t.string().optional(),
            "format": t.string().optional(),
            "ingestionType": t.string().optional(),
            "resolution": t.string().optional(),
        }
    ).named(renames["CdnSettingsIn"])
    types["CdnSettingsOut"] = t.struct(
        {
            "ingestionInfo": t.proxy(renames["IngestionInfoOut"]).optional(),
            "frameRate": t.string().optional(),
            "format": t.string().optional(),
            "ingestionType": t.string().optional(),
            "resolution": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CdnSettingsOut"])
    types["I18nLanguageIn"] = t.struct(
        {
            "snippet": t.proxy(renames["I18nLanguageSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["I18nLanguageIn"])
    types["I18nLanguageOut"] = t.struct(
        {
            "snippet": t.proxy(renames["I18nLanguageSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nLanguageOut"])
    types["ChannelListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ChannelIn"])),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "prevPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "eventId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
        }
    ).named(renames["ChannelListResponseIn"])
    types["ChannelListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ChannelOut"])),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "prevPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "eventId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "visitorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelListResponseOut"])
    types["PlaylistContentDetailsIn"] = t.struct(
        {"itemCount": t.integer().optional()}
    ).named(renames["PlaylistContentDetailsIn"])
    types["PlaylistContentDetailsOut"] = t.struct(
        {
            "itemCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistContentDetailsOut"])
    types["LiveChatFanFundingEventDetailsIn"] = t.struct(
        {
            "userComment": t.string().optional(),
            "currency": t.string().optional(),
            "amountMicros": t.string().optional(),
            "amountDisplayString": t.string().optional(),
        }
    ).named(renames["LiveChatFanFundingEventDetailsIn"])
    types["LiveChatFanFundingEventDetailsOut"] = t.struct(
        {
            "userComment": t.string().optional(),
            "currency": t.string().optional(),
            "amountMicros": t.string().optional(),
            "amountDisplayString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatFanFundingEventDetailsOut"])
    types["MonitorStreamInfoIn"] = t.struct(
        {
            "enableMonitorStream": t.boolean().optional(),
            "embedHtml": t.string().optional(),
            "broadcastStreamDelayMs": t.integer().optional(),
        }
    ).named(renames["MonitorStreamInfoIn"])
    types["MonitorStreamInfoOut"] = t.struct(
        {
            "enableMonitorStream": t.boolean().optional(),
            "embedHtml": t.string().optional(),
            "broadcastStreamDelayMs": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitorStreamInfoOut"])
    types["LiveChatMemberMilestoneChatDetailsIn"] = t.struct(
        {
            "userComment": t.string().optional(),
            "memberLevelName": t.string().optional(),
            "memberMonth": t.integer().optional(),
        }
    ).named(renames["LiveChatMemberMilestoneChatDetailsIn"])
    types["LiveChatMemberMilestoneChatDetailsOut"] = t.struct(
        {
            "userComment": t.string().optional(),
            "memberLevelName": t.string().optional(),
            "memberMonth": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatMemberMilestoneChatDetailsOut"])
    types["LevelDetailsIn"] = t.struct({"displayName": t.string().optional()}).named(
        renames["LevelDetailsIn"]
    )
    types["LevelDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LevelDetailsOut"])
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
    types["InvideoBrandingIn"] = t.struct(
        {
            "timing": t.proxy(renames["InvideoTimingIn"]).optional(),
            "targetChannelId": t.string().optional(),
            "position": t.proxy(renames["InvideoPositionIn"]).optional(),
            "imageBytes": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["InvideoBrandingIn"])
    types["InvideoBrandingOut"] = t.struct(
        {
            "timing": t.proxy(renames["InvideoTimingOut"]).optional(),
            "targetChannelId": t.string().optional(),
            "position": t.proxy(renames["InvideoPositionOut"]).optional(),
            "imageBytes": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvideoBrandingOut"])
    types["SubscriptionContentDetailsIn"] = t.struct(
        {
            "newItemCount": t.integer().optional(),
            "totalItemCount": t.integer().optional(),
            "activityType": t.string().optional(),
        }
    ).named(renames["SubscriptionContentDetailsIn"])
    types["SubscriptionContentDetailsOut"] = t.struct(
        {
            "newItemCount": t.integer().optional(),
            "totalItemCount": t.integer().optional(),
            "activityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionContentDetailsOut"])
    types["PlaylistListResponseIn"] = t.struct(
        {
            "eventId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]),
            "nextPageToken": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["PlaylistIn"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
        }
    ).named(renames["PlaylistListResponseIn"])
    types["PlaylistListResponseOut"] = t.struct(
        {
            "eventId": t.string().optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]),
            "nextPageToken": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "visitorId": t.string().optional(),
            "items": t.array(t.proxy(renames["PlaylistOut"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistListResponseOut"])
    types["VideoProjectDetailsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VideoProjectDetailsIn"]
    )
    types["VideoProjectDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VideoProjectDetailsOut"])
    types["CuepointIn"] = t.struct(
        {
            "id": t.string().optional(),
            "insertionOffsetTimeMs": t.string().optional(),
            "cueType": t.string(),
            "etag": t.string(),
            "walltimeMs": t.string().optional(),
            "durationSecs": t.integer().optional(),
        }
    ).named(renames["CuepointIn"])
    types["CuepointOut"] = t.struct(
        {
            "id": t.string().optional(),
            "insertionOffsetTimeMs": t.string().optional(),
            "cueType": t.string(),
            "etag": t.string(),
            "walltimeMs": t.string().optional(),
            "durationSecs": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CuepointOut"])
    types["ChannelToStoreLinkDetailsIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "storeName": t.string().optional(),
            "storeUrl": t.string().optional(),
        }
    ).named(renames["ChannelToStoreLinkDetailsIn"])
    types["ChannelToStoreLinkDetailsOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "storeName": t.string().optional(),
            "storeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelToStoreLinkDetailsOut"])
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
    types["TokenPaginationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TokenPaginationIn"]
    )
    types["TokenPaginationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TokenPaginationOut"])
    types["LiveStreamSnippetIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "isDefaultStream": t.boolean(),
            "publishedAt": t.string().optional(),
            "channelId": t.string().optional(),
        }
    ).named(renames["LiveStreamSnippetIn"])
    types["LiveStreamSnippetOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "isDefaultStream": t.boolean(),
            "publishedAt": t.string().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveStreamSnippetOut"])
    types["ChannelSettingsIn"] = t.struct(
        {
            "trackingAnalyticsAccountId": t.string().optional(),
            "moderateComments": t.boolean().optional(),
            "country": t.string().optional(),
            "unsubscribedTrailer": t.string().optional(),
            "featuredChannelsTitle": t.string().optional(),
            "defaultTab": t.string().optional(),
            "profileColor": t.string().optional(),
            "title": t.string().optional(),
            "featuredChannelsUrls": t.array(t.string()).optional(),
            "defaultLanguage": t.string(),
            "showRelatedChannels": t.boolean().optional(),
            "keywords": t.string().optional(),
            "showBrowseView": t.boolean().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ChannelSettingsIn"])
    types["ChannelSettingsOut"] = t.struct(
        {
            "trackingAnalyticsAccountId": t.string().optional(),
            "moderateComments": t.boolean().optional(),
            "country": t.string().optional(),
            "unsubscribedTrailer": t.string().optional(),
            "featuredChannelsTitle": t.string().optional(),
            "defaultTab": t.string().optional(),
            "profileColor": t.string().optional(),
            "title": t.string().optional(),
            "featuredChannelsUrls": t.array(t.string()).optional(),
            "defaultLanguage": t.string(),
            "showRelatedChannels": t.boolean().optional(),
            "keywords": t.string().optional(),
            "showBrowseView": t.boolean().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelSettingsOut"])
    types["VideoCategorySnippetIn"] = t.struct(
        {
            "assignable": t.boolean(),
            "channelId": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["VideoCategorySnippetIn"])
    types["VideoCategorySnippetOut"] = t.struct(
        {
            "assignable": t.boolean(),
            "channelId": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCategorySnippetOut"])
    types["VideoStatisticsIn"] = t.struct(
        {
            "likeCount": t.string().optional(),
            "favoriteCount": t.string().optional(),
            "commentCount": t.string().optional(),
            "viewCount": t.string().optional(),
            "dislikeCount": t.string().optional(),
        }
    ).named(renames["VideoStatisticsIn"])
    types["VideoStatisticsOut"] = t.struct(
        {
            "likeCount": t.string().optional(),
            "favoriteCount": t.string().optional(),
            "commentCount": t.string().optional(),
            "viewCount": t.string().optional(),
            "dislikeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoStatisticsOut"])
    types["LiveChatSuperStickerDetailsIn"] = t.struct(
        {
            "superStickerMetadata": t.proxy(
                renames["SuperStickerMetadataIn"]
            ).optional(),
            "tier": t.integer().optional(),
            "amountDisplayString": t.string().optional(),
            "currency": t.string().optional(),
            "amountMicros": t.string().optional(),
        }
    ).named(renames["LiveChatSuperStickerDetailsIn"])
    types["LiveChatSuperStickerDetailsOut"] = t.struct(
        {
            "superStickerMetadata": t.proxy(
                renames["SuperStickerMetadataOut"]
            ).optional(),
            "tier": t.integer().optional(),
            "amountDisplayString": t.string().optional(),
            "currency": t.string().optional(),
            "amountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiveChatSuperStickerDetailsOut"])
    types["ChannelTopicDetailsIn"] = t.struct(
        {
            "topicCategories": t.array(t.string()).optional(),
            "topicIds": t.array(t.string()).optional(),
        }
    ).named(renames["ChannelTopicDetailsIn"])
    types["ChannelTopicDetailsOut"] = t.struct(
        {
            "topicCategories": t.array(t.string()).optional(),
            "topicIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelTopicDetailsOut"])
    types["PlaylistItemContentDetailsIn"] = t.struct(
        {
            "startAt": t.string().optional(),
            "videoId": t.string().optional(),
            "endAt": t.string().optional(),
            "note": t.string().optional(),
            "videoPublishedAt": t.string().optional(),
        }
    ).named(renames["PlaylistItemContentDetailsIn"])
    types["PlaylistItemContentDetailsOut"] = t.struct(
        {
            "startAt": t.string().optional(),
            "videoId": t.string().optional(),
            "endAt": t.string().optional(),
            "note": t.string().optional(),
            "videoPublishedAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistItemContentDetailsOut"])
    types["MembershipsDurationAtLevelIn"] = t.struct(
        {
            "memberSince": t.string().optional(),
            "level": t.string().optional(),
            "memberTotalDurationMonths": t.integer().optional(),
        }
    ).named(renames["MembershipsDurationAtLevelIn"])
    types["MembershipsDurationAtLevelOut"] = t.struct(
        {
            "memberSince": t.string().optional(),
            "level": t.string().optional(),
            "memberTotalDurationMonths": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsDurationAtLevelOut"])
    types["PlaylistStatusIn"] = t.struct(
        {"privacyStatus": t.string().optional()}
    ).named(renames["PlaylistStatusIn"])
    types["PlaylistStatusOut"] = t.struct(
        {
            "privacyStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistStatusOut"])
    types["MembershipsDurationIn"] = t.struct(
        {
            "memberSince": t.string().optional(),
            "memberTotalDurationMonths": t.integer().optional(),
        }
    ).named(renames["MembershipsDurationIn"])
    types["MembershipsDurationOut"] = t.struct(
        {
            "memberSince": t.string().optional(),
            "memberTotalDurationMonths": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipsDurationOut"])
    types["PlaylistIn"] = t.struct(
        {
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "player": t.proxy(renames["PlaylistPlayerIn"]).optional(),
            "snippet": t.proxy(renames["PlaylistSnippetIn"]).optional(),
            "contentDetails": t.proxy(renames["PlaylistContentDetailsIn"]).optional(),
            "status": t.proxy(renames["PlaylistStatusIn"]).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlaylistIn"])
    types["PlaylistOut"] = t.struct(
        {
            "localizations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "player": t.proxy(renames["PlaylistPlayerOut"]).optional(),
            "snippet": t.proxy(renames["PlaylistSnippetOut"]).optional(),
            "contentDetails": t.proxy(renames["PlaylistContentDetailsOut"]).optional(),
            "status": t.proxy(renames["PlaylistStatusOut"]).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistOut"])
    types["VideoSnippetIn"] = t.struct(
        {
            "title": t.string().optional(),
            "liveBroadcastContent": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsIn"]).optional(),
            "description": t.string().optional(),
            "publishedAt": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "defaultLanguage": t.string().optional(),
            "defaultAudioLanguage": t.string().optional(),
            "localized": t.proxy(renames["VideoLocalizationIn"]).optional(),
            "channelTitle": t.string().optional(),
            "channelId": t.string().optional(),
            "categoryId": t.string().optional(),
        }
    ).named(renames["VideoSnippetIn"])
    types["VideoSnippetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "liveBroadcastContent": t.string().optional(),
            "thumbnails": t.proxy(renames["ThumbnailDetailsOut"]).optional(),
            "description": t.string().optional(),
            "publishedAt": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "defaultLanguage": t.string().optional(),
            "defaultAudioLanguage": t.string().optional(),
            "localized": t.proxy(renames["VideoLocalizationOut"]).optional(),
            "channelTitle": t.string().optional(),
            "channelId": t.string().optional(),
            "categoryId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoSnippetOut"])
    types["ChannelContentDetailsIn"] = t.struct(
        {
            "relatedPlaylists": t.struct(
                {
                    "uploads": t.string().optional(),
                    "watchLater": t.string().optional(),
                    "watchHistory": t.string().optional(),
                    "favorites": t.string().optional(),
                    "likes": t.string().optional(),
                }
            )
        }
    ).named(renames["ChannelContentDetailsIn"])
    types["ChannelContentDetailsOut"] = t.struct(
        {
            "relatedPlaylists": t.struct(
                {
                    "uploads": t.string().optional(),
                    "watchLater": t.string().optional(),
                    "watchHistory": t.string().optional(),
                    "favorites": t.string().optional(),
                    "likes": t.string().optional(),
                }
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelContentDetailsOut"])
    types["PlaylistPlayerIn"] = t.struct({"embedHtml": t.string().optional()}).named(
        renames["PlaylistPlayerIn"]
    )
    types["PlaylistPlayerOut"] = t.struct(
        {
            "embedHtml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaylistPlayerOut"])
    types["SuperChatEventSnippetIn"] = t.struct(
        {
            "currency": t.string().optional(),
            "messageType": t.integer().optional(),
            "channelId": t.string().optional(),
            "createdAt": t.string().optional(),
            "supporterDetails": t.proxy(renames["ChannelProfileDetailsIn"]).optional(),
            "superStickerMetadata": t.proxy(
                renames["SuperStickerMetadataIn"]
            ).optional(),
            "amountMicros": t.string().optional(),
            "displayString": t.string().optional(),
            "commentText": t.string().optional(),
            "isSuperStickerEvent": t.boolean().optional(),
        }
    ).named(renames["SuperChatEventSnippetIn"])
    types["SuperChatEventSnippetOut"] = t.struct(
        {
            "currency": t.string().optional(),
            "messageType": t.integer().optional(),
            "channelId": t.string().optional(),
            "createdAt": t.string().optional(),
            "supporterDetails": t.proxy(renames["ChannelProfileDetailsOut"]).optional(),
            "superStickerMetadata": t.proxy(
                renames["SuperStickerMetadataOut"]
            ).optional(),
            "amountMicros": t.string().optional(),
            "displayString": t.string().optional(),
            "commentText": t.string().optional(),
            "isSuperStickerEvent": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperChatEventSnippetOut"])

    functions = {}
    functions["channelsList"] = youtube.put(
        "youtube/v3/channels",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "kind": t.string().optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "contentDetails": t.proxy(
                    renames["ChannelContentDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["ChannelStatisticsIn"]).optional(),
                "conversionPings": t.proxy(
                    renames["ChannelConversionPingsIn"]
                ).optional(),
                "status": t.proxy(renames["ChannelStatusIn"]).optional(),
                "auditDetails": t.proxy(renames["ChannelAuditDetailsIn"]).optional(),
                "brandingSettings": t.proxy(
                    renames["ChannelBrandingSettingsIn"]
                ).optional(),
                "contentOwnerDetails": t.proxy(
                    renames["ChannelContentOwnerDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["ChannelSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "topicDetails": t.proxy(renames["ChannelTopicDetailsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelsUpdate"] = youtube.put(
        "youtube/v3/channels",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "kind": t.string().optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "contentDetails": t.proxy(
                    renames["ChannelContentDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["ChannelStatisticsIn"]).optional(),
                "conversionPings": t.proxy(
                    renames["ChannelConversionPingsIn"]
                ).optional(),
                "status": t.proxy(renames["ChannelStatusIn"]).optional(),
                "auditDetails": t.proxy(renames["ChannelAuditDetailsIn"]).optional(),
                "brandingSettings": t.proxy(
                    renames["ChannelBrandingSettingsIn"]
                ).optional(),
                "contentOwnerDetails": t.proxy(
                    renames["ChannelContentOwnerDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["ChannelSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "topicDetails": t.proxy(renames["ChannelTopicDetailsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thirdPartyLinksUpdate"] = youtube.delete(
        "youtube/v3/thirdPartyLinks",
        t.struct(
            {
                "externalChannelId": t.string().optional(),
                "part": t.string().optional(),
                "linkingToken": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thirdPartyLinksInsert"] = youtube.delete(
        "youtube/v3/thirdPartyLinks",
        t.struct(
            {
                "externalChannelId": t.string().optional(),
                "part": t.string().optional(),
                "linkingToken": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thirdPartyLinksList"] = youtube.delete(
        "youtube/v3/thirdPartyLinks",
        t.struct(
            {
                "externalChannelId": t.string().optional(),
                "part": t.string().optional(),
                "linkingToken": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["thirdPartyLinksDelete"] = youtube.delete(
        "youtube/v3/thirdPartyLinks",
        t.struct(
            {
                "externalChannelId": t.string().optional(),
                "part": t.string().optional(),
                "linkingToken": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["searchList"] = youtube.get(
        "youtube/v3/search",
        t.struct(
            {
                "forMine": t.boolean().optional(),
                "channelId": t.string().optional(),
                "safeSearch": t.string().optional(),
                "relatedToVideoId": t.string().optional(),
                "videoCaption": t.string().optional(),
                "videoDefinition": t.string().optional(),
                "publishedAfter": t.string().optional(),
                "regionCode": t.string().optional(),
                "channelType": t.string().optional(),
                "videoSyndicated": t.string().optional(),
                "order": t.string().optional(),
                "videoDimension": t.string().optional(),
                "q": t.string().optional(),
                "videoCategoryId": t.string().optional(),
                "pageToken": t.string().optional(),
                "type": t.string().optional(),
                "videoType": t.string().optional(),
                "publishedBefore": t.string().optional(),
                "videoLicense": t.string().optional(),
                "location": t.string().optional(),
                "topicId": t.string().optional(),
                "videoDuration": t.string().optional(),
                "eventType": t.string().optional(),
                "videoEmbeddable": t.string().optional(),
                "relevanceLanguage": t.string().optional(),
                "forDeveloper": t.boolean().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "forContentOwner": t.boolean().optional(),
                "locationRadius": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsDelete"] = youtube.post(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["LiveBroadcastContentDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
                "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsUpdate"] = youtube.post(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["LiveBroadcastContentDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
                "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsBind"] = youtube.post(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["LiveBroadcastContentDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
                "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsList"] = youtube.post(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["LiveBroadcastContentDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
                "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsInsertCuepoint"] = youtube.post(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["LiveBroadcastContentDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
                "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsTransition"] = youtube.post(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["LiveBroadcastContentDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
                "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveBroadcastsInsert"] = youtube.post(
        "youtube/v3/liveBroadcasts",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["LiveBroadcastContentDetailsIn"]
                ).optional(),
                "snippet": t.proxy(renames["LiveBroadcastSnippetIn"]).optional(),
                "statistics": t.proxy(renames["LiveBroadcastStatisticsIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["LiveBroadcastStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveBroadcastOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistItemsInsert"] = youtube.put(
        "youtube/v3/playlistItems",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["PlaylistItemContentDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["PlaylistItemSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["PlaylistItemStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistItemsDelete"] = youtube.put(
        "youtube/v3/playlistItems",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["PlaylistItemContentDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["PlaylistItemSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["PlaylistItemStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistItemsList"] = youtube.put(
        "youtube/v3/playlistItems",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["PlaylistItemContentDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["PlaylistItemSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["PlaylistItemStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistItemsUpdate"] = youtube.put(
        "youtube/v3/playlistItems",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "contentDetails": t.proxy(
                    renames["PlaylistItemContentDetailsIn"]
                ).optional(),
                "id": t.string().optional(),
                "snippet": t.proxy(renames["PlaylistItemSnippetIn"]).optional(),
                "etag": t.string().optional(),
                "status": t.proxy(renames["PlaylistItemStatusIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["youtubeV3UpdateCommentThreads"] = youtube.put(
        "youtube/v3/commentThreads",
        t.struct(
            {
                "part": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["CommentThreadSnippetIn"]).optional(),
                "replies": t.proxy(renames["CommentThreadRepliesIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["i18nLanguagesList"] = youtube.get(
        "youtube/v3/i18nLanguages",
        t.struct(
            {
                "part": t.string().optional(),
                "hl": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["I18nLanguageListResponseOut"]),
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
    functions["testsInsert"] = youtube.post(
        "youtube/v3/tests",
        t.struct(
            {
                "externalChannelId": t.string(),
                "part": t.string(),
                "id": t.string(),
                "featuredPart": t.boolean(),
                "snippet": t.proxy(renames["TestItemTestItemSnippetIn"]),
                "gaia": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatModeratorsInsert"] = youtube.get(
        "youtube/v3/liveChat/moderators",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "liveChatId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "part": t.string().optional(),
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
                "liveChatId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "part": t.string().optional(),
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
                "liveChatId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "part": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatModeratorListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["membersList"] = youtube.get(
        "youtube/v3/members",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "part": t.string().optional(),
                "mode": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filterByMemberChannelId": t.string().optional(),
                "hasAccessToLevel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MemberListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsList"] = youtube.post(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsUpdate"] = youtube.post(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsDelete"] = youtube.post(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsDownload"] = youtube.post(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["captionsInsert"] = youtube.post(
        "youtube/v3/captions",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "part": t.string().optional(),
                "onBehalfOf": t.string().optional(),
                "sync": t.boolean().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["CaptionSnippetIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CaptionOut"]),
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
    functions["subscriptionsInsert"] = youtube.get(
        "youtube/v3/subscriptions",
        t.struct(
            {
                "id": t.string().optional(),
                "order": t.string().optional(),
                "mine": t.boolean().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "mySubscribers": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "myRecentSubscribers": t.boolean(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "forChannelId": t.string().optional(),
                "channelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsDelete"] = youtube.get(
        "youtube/v3/subscriptions",
        t.struct(
            {
                "id": t.string().optional(),
                "order": t.string().optional(),
                "mine": t.boolean().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "mySubscribers": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "myRecentSubscribers": t.boolean(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "forChannelId": t.string().optional(),
                "channelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsList"] = youtube.get(
        "youtube/v3/subscriptions",
        t.struct(
            {
                "id": t.string().optional(),
                "order": t.string().optional(),
                "mine": t.boolean().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "mySubscribers": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "myRecentSubscribers": t.boolean(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "forChannelId": t.string().optional(),
                "channelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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
    functions["activitiesList"] = youtube.get(
        "youtube/v3/activities",
        t.struct(
            {
                "channelId": t.string(),
                "part": t.string().optional(),
                "home": t.boolean(),
                "mine": t.boolean(),
                "publishedBefore": t.string(),
                "publishedAfter": t.string(),
                "maxResults": t.integer().optional(),
                "regionCode": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ActivityListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelSectionsInsert"] = youtube.delete(
        "youtube/v3/channelSections",
        t.struct(
            {
                "id": t.string(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelSectionsList"] = youtube.delete(
        "youtube/v3/channelSections",
        t.struct(
            {
                "id": t.string(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelSectionsUpdate"] = youtube.delete(
        "youtube/v3/channelSections",
        t.struct(
            {
                "id": t.string(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelSectionsDelete"] = youtube.delete(
        "youtube/v3/channelSections",
        t.struct(
            {
                "id": t.string(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistsList"] = youtube.post(
        "youtube/v3/playlists",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "part": t.string().optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "player": t.proxy(renames["PlaylistPlayerIn"]).optional(),
                "snippet": t.proxy(renames["PlaylistSnippetIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["PlaylistContentDetailsIn"]
                ).optional(),
                "status": t.proxy(renames["PlaylistStatusIn"]).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistsUpdate"] = youtube.post(
        "youtube/v3/playlists",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "part": t.string().optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "player": t.proxy(renames["PlaylistPlayerIn"]).optional(),
                "snippet": t.proxy(renames["PlaylistSnippetIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["PlaylistContentDetailsIn"]
                ).optional(),
                "status": t.proxy(renames["PlaylistStatusIn"]).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistsDelete"] = youtube.post(
        "youtube/v3/playlists",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "part": t.string().optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "player": t.proxy(renames["PlaylistPlayerIn"]).optional(),
                "snippet": t.proxy(renames["PlaylistSnippetIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["PlaylistContentDetailsIn"]
                ).optional(),
                "status": t.proxy(renames["PlaylistStatusIn"]).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playlistsInsert"] = youtube.post(
        "youtube/v3/playlists",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "part": t.string().optional(),
                "localizations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "player": t.proxy(renames["PlaylistPlayerIn"]).optional(),
                "snippet": t.proxy(renames["PlaylistSnippetIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["PlaylistContentDetailsIn"]
                ).optional(),
                "status": t.proxy(renames["PlaylistStatusIn"]).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlaylistOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["watermarksUnset"] = youtube.post(
        "youtube/v3/watermarks/set",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "channelId": t.string(),
                "timing": t.proxy(renames["InvideoTimingIn"]).optional(),
                "targetChannelId": t.string().optional(),
                "position": t.proxy(renames["InvideoPositionIn"]).optional(),
                "imageBytes": t.string().optional(),
                "imageUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["watermarksSet"] = youtube.post(
        "youtube/v3/watermarks/set",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "channelId": t.string(),
                "timing": t.proxy(renames["InvideoTimingIn"]).optional(),
                "targetChannelId": t.string().optional(),
                "position": t.proxy(renames["InvideoPositionIn"]).optional(),
                "imageBytes": t.string().optional(),
                "imageUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsList"] = youtube.delete(
        "youtube/v3/comments",
        t.struct({"id": t.string(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsMarkAsSpam"] = youtube.delete(
        "youtube/v3/comments",
        t.struct({"id": t.string(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsInsert"] = youtube.delete(
        "youtube/v3/comments",
        t.struct({"id": t.string(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsSetModerationStatus"] = youtube.delete(
        "youtube/v3/comments",
        t.struct({"id": t.string(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsUpdate"] = youtube.delete(
        "youtube/v3/comments",
        t.struct({"id": t.string(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsDelete"] = youtube.delete(
        "youtube/v3/comments",
        t.struct({"id": t.string(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatMessagesDelete"] = youtube.get(
        "youtube/v3/liveChat/messages",
        t.struct(
            {
                "hl": t.string().optional(),
                "profileImageSize": t.integer().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "liveChatId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatMessageListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatMessagesInsert"] = youtube.get(
        "youtube/v3/liveChat/messages",
        t.struct(
            {
                "hl": t.string().optional(),
                "profileImageSize": t.integer().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "liveChatId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatMessageListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatMessagesList"] = youtube.get(
        "youtube/v3/liveChat/messages",
        t.struct(
            {
                "hl": t.string().optional(),
                "profileImageSize": t.integer().optional(),
                "part": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "liveChatId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatMessageListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveStreamsList"] = youtube.post(
        "youtube/v3/liveStreams",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
                "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["LiveStreamContentDetailsIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
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
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
                "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["LiveStreamContentDetailsIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveStreamsUpdate"] = youtube.post(
        "youtube/v3/liveStreams",
        t.struct(
            {
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
                "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["LiveStreamContentDetailsIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
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
                "part": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "status": t.proxy(renames["LiveStreamStatusIn"]).optional(),
                "cdn": t.proxy(renames["CdnSettingsIn"]).optional(),
                "etag": t.string().optional(),
                "snippet": t.proxy(renames["LiveStreamSnippetIn"]).optional(),
                "contentDetails": t.proxy(
                    renames["LiveStreamContentDetailsIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["abuseReportsInsert"] = youtube.post(
        "youtube/v3/abuseReports",
        t.struct(
            {
                "part": t.string().optional(),
                "description": t.string(),
                "abuseTypes": t.array(t.proxy(renames["AbuseTypeIn"])),
                "subject": t.proxy(renames["EntityIn"]),
                "relatedEntities": t.array(t.proxy(renames["RelatedEntityIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AbuseReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelBannersInsert"] = youtube.post(
        "youtube/v3/channelBanners/insert",
        t.struct(
            {
                "channelId": t.string().optional(),
                "onBehalfOfContentOwnerChannel": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "url": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelBannerResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["superChatEventsList"] = youtube.get(
        "youtube/v3/superChatEvents",
        t.struct(
            {
                "part": t.string().optional(),
                "pageToken": t.string().optional(),
                "hl": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SuperChatEventListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentThreadsInsert"] = youtube.get(
        "youtube/v3/commentThreads",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "moderationStatus": t.string().optional(),
                "pageToken": t.string().optional(),
                "textFormat": t.string().optional(),
                "videoId": t.string().optional(),
                "id": t.string().optional(),
                "searchTerms": t.string().optional(),
                "channelId": t.string().optional(),
                "allThreadsRelatedToChannelId": t.string().optional(),
                "part": t.string().optional(),
                "order": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentThreadListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentThreadsList"] = youtube.get(
        "youtube/v3/commentThreads",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "moderationStatus": t.string().optional(),
                "pageToken": t.string().optional(),
                "textFormat": t.string().optional(),
                "videoId": t.string().optional(),
                "id": t.string().optional(),
                "searchTerms": t.string().optional(),
                "channelId": t.string().optional(),
                "allThreadsRelatedToChannelId": t.string().optional(),
                "part": t.string().optional(),
                "order": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentThreadListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videoCategoriesList"] = youtube.get(
        "youtube/v3/videoCategories",
        t.struct(
            {
                "id": t.string().optional(),
                "hl": t.string(),
                "part": t.string().optional(),
                "regionCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VideoCategoryListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatBansDelete"] = youtube.post(
        "youtube/v3/liveChat/bans",
        t.struct(
            {
                "part": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["LiveChatBanSnippetIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatBanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liveChatBansInsert"] = youtube.post(
        "youtube/v3/liveChat/bans",
        t.struct(
            {
                "part": t.string().optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["LiveChatBanSnippetIn"]).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiveChatBanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosList"] = youtube.delete(
        "youtube/v3/videos",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosGetRating"] = youtube.delete(
        "youtube/v3/videos",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosRate"] = youtube.delete(
        "youtube/v3/videos",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosUpdate"] = youtube.delete(
        "youtube/v3/videos",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosInsert"] = youtube.delete(
        "youtube/v3/videos",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosReportAbuse"] = youtube.delete(
        "youtube/v3/videos",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosDelete"] = youtube.delete(
        "youtube/v3/videos",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="youtube", renames=renames, types=Box(types), functions=Box(functions)
    )
