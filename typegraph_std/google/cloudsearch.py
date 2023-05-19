from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudsearch() -> Import:
    cloudsearch = HTTPRuntime("https://cloudsearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudsearch_1_ErrorResponse",
        "HistoryIn": "_cloudsearch_2_HistoryIn",
        "HistoryOut": "_cloudsearch_3_HistoryOut",
        "AclFixStatusIn": "_cloudsearch_4_AclFixStatusIn",
        "AclFixStatusOut": "_cloudsearch_5_AclFixStatusOut",
        "GetSearchApplicationSessionStatsResponseIn": "_cloudsearch_6_GetSearchApplicationSessionStatsResponseIn",
        "GetSearchApplicationSessionStatsResponseOut": "_cloudsearch_7_GetSearchApplicationSessionStatsResponseOut",
        "FuseboxItemThreadMatchInfoIn": "_cloudsearch_8_FuseboxItemThreadMatchInfoIn",
        "FuseboxItemThreadMatchInfoOut": "_cloudsearch_9_FuseboxItemThreadMatchInfoOut",
        "MdbGroupProtoIn": "_cloudsearch_10_MdbGroupProtoIn",
        "MdbGroupProtoOut": "_cloudsearch_11_MdbGroupProtoOut",
        "AuthorizedItemIdIn": "_cloudsearch_12_AuthorizedItemIdIn",
        "AuthorizedItemIdOut": "_cloudsearch_13_AuthorizedItemIdOut",
        "SourceConfigIn": "_cloudsearch_14_SourceConfigIn",
        "SourceConfigOut": "_cloudsearch_15_SourceConfigOut",
        "QueryInterpretationConfigIn": "_cloudsearch_16_QueryInterpretationConfigIn",
        "QueryInterpretationConfigOut": "_cloudsearch_17_QueryInterpretationConfigOut",
        "PhoneNumberIn": "_cloudsearch_18_PhoneNumberIn",
        "PhoneNumberOut": "_cloudsearch_19_PhoneNumberOut",
        "GetSearchApplicationUserStatsResponseIn": "_cloudsearch_20_GetSearchApplicationUserStatsResponseIn",
        "GetSearchApplicationUserStatsResponseOut": "_cloudsearch_21_GetSearchApplicationUserStatsResponseOut",
        "BabelPlaceholderMetadataIn": "_cloudsearch_22_BabelPlaceholderMetadataIn",
        "BabelPlaceholderMetadataOut": "_cloudsearch_23_BabelPlaceholderMetadataOut",
        "LanguageConfigIn": "_cloudsearch_24_LanguageConfigIn",
        "LanguageConfigOut": "_cloudsearch_25_LanguageConfigOut",
        "MenuItemIn": "_cloudsearch_26_MenuItemIn",
        "MenuItemOut": "_cloudsearch_27_MenuItemOut",
        "CallInfoIn": "_cloudsearch_28_CallInfoIn",
        "CallInfoOut": "_cloudsearch_29_CallInfoOut",
        "AppsDynamiteSharedEmojiIn": "_cloudsearch_30_AppsDynamiteSharedEmojiIn",
        "AppsDynamiteSharedEmojiOut": "_cloudsearch_31_AppsDynamiteSharedEmojiOut",
        "MessagePropsIn": "_cloudsearch_32_MessagePropsIn",
        "MessagePropsOut": "_cloudsearch_33_MessagePropsOut",
        "SearchQualityMetadataIn": "_cloudsearch_34_SearchQualityMetadataIn",
        "SearchQualityMetadataOut": "_cloudsearch_35_SearchQualityMetadataOut",
        "AclInfoIn": "_cloudsearch_36_AclInfoIn",
        "AclInfoOut": "_cloudsearch_37_AclInfoOut",
        "EnumValuePairIn": "_cloudsearch_38_EnumValuePairIn",
        "EnumValuePairOut": "_cloudsearch_39_EnumValuePairOut",
        "GoogleChatV1WidgetMarkupImageButtonIn": "_cloudsearch_40_GoogleChatV1WidgetMarkupImageButtonIn",
        "GoogleChatV1WidgetMarkupImageButtonOut": "_cloudsearch_41_GoogleChatV1WidgetMarkupImageButtonOut",
        "VPCSettingsIn": "_cloudsearch_42_VPCSettingsIn",
        "VPCSettingsOut": "_cloudsearch_43_VPCSettingsOut",
        "PossiblyTrimmedModelIn": "_cloudsearch_44_PossiblyTrimmedModelIn",
        "PossiblyTrimmedModelOut": "_cloudsearch_45_PossiblyTrimmedModelOut",
        "PeopleSuggestionIn": "_cloudsearch_46_PeopleSuggestionIn",
        "PeopleSuggestionOut": "_cloudsearch_47_PeopleSuggestionOut",
        "AppsDynamiteSharedOriginAppSuggestionIn": "_cloudsearch_48_AppsDynamiteSharedOriginAppSuggestionIn",
        "AppsDynamiteSharedOriginAppSuggestionOut": "_cloudsearch_49_AppsDynamiteSharedOriginAppSuggestionOut",
        "HtmlOperatorOptionsIn": "_cloudsearch_50_HtmlOperatorOptionsIn",
        "HtmlOperatorOptionsOut": "_cloudsearch_51_HtmlOperatorOptionsOut",
        "GetCustomerSessionStatsResponseIn": "_cloudsearch_52_GetCustomerSessionStatsResponseIn",
        "GetCustomerSessionStatsResponseOut": "_cloudsearch_53_GetCustomerSessionStatsResponseOut",
        "DateValuesIn": "_cloudsearch_54_DateValuesIn",
        "DateValuesOut": "_cloudsearch_55_DateValuesOut",
        "ListSearchApplicationsResponseIn": "_cloudsearch_56_ListSearchApplicationsResponseIn",
        "ListSearchApplicationsResponseOut": "_cloudsearch_57_ListSearchApplicationsResponseOut",
        "PollItemsResponseIn": "_cloudsearch_58_PollItemsResponseIn",
        "PollItemsResponseOut": "_cloudsearch_59_PollItemsResponseOut",
        "TombstoneMetadataIn": "_cloudsearch_60_TombstoneMetadataIn",
        "TombstoneMetadataOut": "_cloudsearch_61_TombstoneMetadataOut",
        "GetCustomerIndexStatsResponseIn": "_cloudsearch_62_GetCustomerIndexStatsResponseIn",
        "GetCustomerIndexStatsResponseOut": "_cloudsearch_63_GetCustomerIndexStatsResponseOut",
        "OnClickIn": "_cloudsearch_64_OnClickIn",
        "OnClickOut": "_cloudsearch_65_OnClickOut",
        "TextPropertyOptionsIn": "_cloudsearch_66_TextPropertyOptionsIn",
        "TextPropertyOptionsOut": "_cloudsearch_67_TextPropertyOptionsOut",
        "KeyValueIn": "_cloudsearch_68_KeyValueIn",
        "KeyValueOut": "_cloudsearch_69_KeyValueOut",
        "AppsDynamiteStorageOpenLinkAppUriIn": "_cloudsearch_70_AppsDynamiteStorageOpenLinkAppUriIn",
        "AppsDynamiteStorageOpenLinkAppUriOut": "_cloudsearch_71_AppsDynamiteStorageOpenLinkAppUriOut",
        "CustomEmojiMetadataIn": "_cloudsearch_72_CustomEmojiMetadataIn",
        "CustomEmojiMetadataOut": "_cloudsearch_73_CustomEmojiMetadataOut",
        "DriveTimeSpanRestrictIn": "_cloudsearch_74_DriveTimeSpanRestrictIn",
        "DriveTimeSpanRestrictOut": "_cloudsearch_75_DriveTimeSpanRestrictOut",
        "VideoCallMetadataIn": "_cloudsearch_76_VideoCallMetadataIn",
        "VideoCallMetadataOut": "_cloudsearch_77_VideoCallMetadataOut",
        "AttributeRemovedIn": "_cloudsearch_78_AttributeRemovedIn",
        "AttributeRemovedOut": "_cloudsearch_79_AttributeRemovedOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn": "_cloudsearch_80_AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut": "_cloudsearch_81_AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut",
        "TaskActionMarkupIn": "_cloudsearch_82_TaskActionMarkupIn",
        "TaskActionMarkupOut": "_cloudsearch_83_TaskActionMarkupOut",
        "CompositeFilterIn": "_cloudsearch_84_CompositeFilterIn",
        "CompositeFilterOut": "_cloudsearch_85_CompositeFilterOut",
        "AuditLoggingSettingsIn": "_cloudsearch_86_AuditLoggingSettingsIn",
        "AuditLoggingSettingsOut": "_cloudsearch_87_AuditLoggingSettingsOut",
        "LabelsIn": "_cloudsearch_88_LabelsIn",
        "LabelsOut": "_cloudsearch_89_LabelsOut",
        "SigningKeyPossessorProtoIn": "_cloudsearch_90_SigningKeyPossessorProtoIn",
        "SigningKeyPossessorProtoOut": "_cloudsearch_91_SigningKeyPossessorProtoOut",
        "LabelRenamedIn": "_cloudsearch_92_LabelRenamedIn",
        "LabelRenamedOut": "_cloudsearch_93_LabelRenamedOut",
        "GetDataSourceIndexStatsResponseIn": "_cloudsearch_94_GetDataSourceIndexStatsResponseIn",
        "GetDataSourceIndexStatsResponseOut": "_cloudsearch_95_GetDataSourceIndexStatsResponseOut",
        "IntegerFacetingOptionsIn": "_cloudsearch_96_IntegerFacetingOptionsIn",
        "IntegerFacetingOptionsOut": "_cloudsearch_97_IntegerFacetingOptionsOut",
        "GroupIdIn": "_cloudsearch_98_GroupIdIn",
        "GroupIdOut": "_cloudsearch_99_GroupIdOut",
        "AppsDynamiteStorageColumnsColumnWidgetsIn": "_cloudsearch_100_AppsDynamiteStorageColumnsColumnWidgetsIn",
        "AppsDynamiteStorageColumnsColumnWidgetsOut": "_cloudsearch_101_AppsDynamiteStorageColumnsColumnWidgetsOut",
        "IdIn": "_cloudsearch_102_IdIn",
        "IdOut": "_cloudsearch_103_IdOut",
        "CardHeaderIn": "_cloudsearch_104_CardHeaderIn",
        "CardHeaderOut": "_cloudsearch_105_CardHeaderOut",
        "MdbUserProtoIn": "_cloudsearch_106_MdbUserProtoIn",
        "MdbUserProtoOut": "_cloudsearch_107_MdbUserProtoOut",
        "ColorIn": "_cloudsearch_108_ColorIn",
        "ColorOut": "_cloudsearch_109_ColorOut",
        "GetSearchApplicationQueryStatsResponseIn": "_cloudsearch_110_GetSearchApplicationQueryStatsResponseIn",
        "GetSearchApplicationQueryStatsResponseOut": "_cloudsearch_111_GetSearchApplicationQueryStatsResponseOut",
        "AppsDynamiteStorageButtonIn": "_cloudsearch_112_AppsDynamiteStorageButtonIn",
        "AppsDynamiteStorageButtonOut": "_cloudsearch_113_AppsDynamiteStorageButtonOut",
        "AppsDynamiteStorageSuggestionsIn": "_cloudsearch_114_AppsDynamiteStorageSuggestionsIn",
        "AppsDynamiteStorageSuggestionsOut": "_cloudsearch_115_AppsDynamiteStorageSuggestionsOut",
        "AppsDynamiteStorageButtonListIn": "_cloudsearch_116_AppsDynamiteStorageButtonListIn",
        "AppsDynamiteStorageButtonListOut": "_cloudsearch_117_AppsDynamiteStorageButtonListOut",
        "GoogleChatV1WidgetMarkupButtonIn": "_cloudsearch_118_GoogleChatV1WidgetMarkupButtonIn",
        "GoogleChatV1WidgetMarkupButtonOut": "_cloudsearch_119_GoogleChatV1WidgetMarkupButtonOut",
        "MessageAddedIn": "_cloudsearch_120_MessageAddedIn",
        "MessageAddedOut": "_cloudsearch_121_MessageAddedOut",
        "CloudPrincipalProtoIn": "_cloudsearch_122_CloudPrincipalProtoIn",
        "CloudPrincipalProtoOut": "_cloudsearch_123_CloudPrincipalProtoOut",
        "PostiniUserProtoIn": "_cloudsearch_124_PostiniUserProtoIn",
        "PostiniUserProtoOut": "_cloudsearch_125_PostiniUserProtoOut",
        "TextParagraphIn": "_cloudsearch_126_TextParagraphIn",
        "TextParagraphOut": "_cloudsearch_127_TextParagraphOut",
        "AppsDynamiteSharedFindDocumentSuggestionIn": "_cloudsearch_128_AppsDynamiteSharedFindDocumentSuggestionIn",
        "AppsDynamiteSharedFindDocumentSuggestionOut": "_cloudsearch_129_AppsDynamiteSharedFindDocumentSuggestionOut",
        "SortOptionsIn": "_cloudsearch_130_SortOptionsIn",
        "SortOptionsOut": "_cloudsearch_131_SortOptionsOut",
        "DriveLocationRestrictIn": "_cloudsearch_132_DriveLocationRestrictIn",
        "DriveLocationRestrictOut": "_cloudsearch_133_DriveLocationRestrictOut",
        "PrefWrittenIn": "_cloudsearch_134_PrefWrittenIn",
        "PrefWrittenOut": "_cloudsearch_135_PrefWrittenOut",
        "TimestampPropertyOptionsIn": "_cloudsearch_136_TimestampPropertyOptionsIn",
        "TimestampPropertyOptionsOut": "_cloudsearch_137_TimestampPropertyOptionsOut",
        "TransientDataIn": "_cloudsearch_138_TransientDataIn",
        "TransientDataOut": "_cloudsearch_139_TransientDataOut",
        "BooleanPropertyOptionsIn": "_cloudsearch_140_BooleanPropertyOptionsIn",
        "BooleanPropertyOptionsOut": "_cloudsearch_141_BooleanPropertyOptionsOut",
        "GridIn": "_cloudsearch_142_GridIn",
        "GridOut": "_cloudsearch_143_GridOut",
        "AbuseReportingConfigIn": "_cloudsearch_144_AbuseReportingConfigIn",
        "AbuseReportingConfigOut": "_cloudsearch_145_AbuseReportingConfigOut",
        "ValueIn": "_cloudsearch_146_ValueIn",
        "ValueOut": "_cloudsearch_147_ValueOut",
        "GoogleChatV1WidgetMarkupFormActionIn": "_cloudsearch_148_GoogleChatV1WidgetMarkupFormActionIn",
        "GoogleChatV1WidgetMarkupFormActionOut": "_cloudsearch_149_GoogleChatV1WidgetMarkupFormActionOut",
        "ImageComponentIn": "_cloudsearch_150_ImageComponentIn",
        "ImageComponentOut": "_cloudsearch_151_ImageComponentOut",
        "FormActionIn": "_cloudsearch_152_FormActionIn",
        "FormActionOut": "_cloudsearch_153_FormActionOut",
        "AppsDynamiteSharedChatItemIn": "_cloudsearch_154_AppsDynamiteSharedChatItemIn",
        "AppsDynamiteSharedChatItemOut": "_cloudsearch_155_AppsDynamiteSharedChatItemOut",
        "InitializeCustomerRequestIn": "_cloudsearch_156_InitializeCustomerRequestIn",
        "InitializeCustomerRequestOut": "_cloudsearch_157_InitializeCustomerRequestOut",
        "IconImageIn": "_cloudsearch_158_IconImageIn",
        "IconImageOut": "_cloudsearch_159_IconImageOut",
        "ResourceRoleProtoIn": "_cloudsearch_160_ResourceRoleProtoIn",
        "ResourceRoleProtoOut": "_cloudsearch_161_ResourceRoleProtoOut",
        "DriveClientActionMarkupIn": "_cloudsearch_162_DriveClientActionMarkupIn",
        "DriveClientActionMarkupOut": "_cloudsearch_163_DriveClientActionMarkupOut",
        "QueryInterpretationOptionsIn": "_cloudsearch_164_QueryInterpretationOptionsIn",
        "QueryInterpretationOptionsOut": "_cloudsearch_165_QueryInterpretationOptionsOut",
        "FilterCreatedIn": "_cloudsearch_166_FilterCreatedIn",
        "FilterCreatedOut": "_cloudsearch_167_FilterCreatedOut",
        "MemberIdIn": "_cloudsearch_168_MemberIdIn",
        "MemberIdOut": "_cloudsearch_169_MemberIdOut",
        "MessageInfoIn": "_cloudsearch_170_MessageInfoIn",
        "MessageInfoOut": "_cloudsearch_171_MessageInfoOut",
        "QueryItemIn": "_cloudsearch_172_QueryItemIn",
        "QueryItemOut": "_cloudsearch_173_QueryItemOut",
        "AppsDynamiteSharedMeetMetadataIn": "_cloudsearch_174_AppsDynamiteSharedMeetMetadataIn",
        "AppsDynamiteSharedMeetMetadataOut": "_cloudsearch_175_AppsDynamiteSharedMeetMetadataOut",
        "CapTokenHolderProtoIn": "_cloudsearch_176_CapTokenHolderProtoIn",
        "CapTokenHolderProtoOut": "_cloudsearch_177_CapTokenHolderProtoOut",
        "AppsDynamiteSharedTasksAnnotationDataCreationIn": "_cloudsearch_178_AppsDynamiteSharedTasksAnnotationDataCreationIn",
        "AppsDynamiteSharedTasksAnnotationDataCreationOut": "_cloudsearch_179_AppsDynamiteSharedTasksAnnotationDataCreationOut",
        "AppsDynamiteStorageTextParagraphIn": "_cloudsearch_180_AppsDynamiteStorageTextParagraphIn",
        "AppsDynamiteStorageTextParagraphOut": "_cloudsearch_181_AppsDynamiteStorageTextParagraphOut",
        "GoogleChatV1WidgetMarkupTextButtonIn": "_cloudsearch_182_GoogleChatV1WidgetMarkupTextButtonIn",
        "GoogleChatV1WidgetMarkupTextButtonOut": "_cloudsearch_183_GoogleChatV1WidgetMarkupTextButtonOut",
        "HostProtoIn": "_cloudsearch_184_HostProtoIn",
        "HostProtoOut": "_cloudsearch_185_HostProtoOut",
        "FilterDeletedIn": "_cloudsearch_186_FilterDeletedIn",
        "FilterDeletedOut": "_cloudsearch_187_FilterDeletedOut",
        "DynamiteMessagesScoringInfoIn": "_cloudsearch_188_DynamiteMessagesScoringInfoIn",
        "DynamiteMessagesScoringInfoOut": "_cloudsearch_189_DynamiteMessagesScoringInfoOut",
        "AppsDynamiteStorageBorderStyleIn": "_cloudsearch_190_AppsDynamiteStorageBorderStyleIn",
        "AppsDynamiteStorageBorderStyleOut": "_cloudsearch_191_AppsDynamiteStorageBorderStyleOut",
        "AppsDynamiteSharedDocumentIn": "_cloudsearch_192_AppsDynamiteSharedDocumentIn",
        "AppsDynamiteSharedDocumentOut": "_cloudsearch_193_AppsDynamiteSharedDocumentOut",
        "RenameEventIn": "_cloudsearch_194_RenameEventIn",
        "RenameEventOut": "_cloudsearch_195_RenameEventOut",
        "ContentReportJustificationIn": "_cloudsearch_196_ContentReportJustificationIn",
        "ContentReportJustificationOut": "_cloudsearch_197_ContentReportJustificationOut",
        "MatchRangeIn": "_cloudsearch_198_MatchRangeIn",
        "MatchRangeOut": "_cloudsearch_199_MatchRangeOut",
        "ChatProtoIn": "_cloudsearch_200_ChatProtoIn",
        "ChatProtoOut": "_cloudsearch_201_ChatProtoOut",
        "GsuiteIntegrationMetadataIn": "_cloudsearch_202_GsuiteIntegrationMetadataIn",
        "GsuiteIntegrationMetadataOut": "_cloudsearch_203_GsuiteIntegrationMetadataOut",
        "SearchItemsByViewUrlResponseIn": "_cloudsearch_204_SearchItemsByViewUrlResponseIn",
        "SearchItemsByViewUrlResponseOut": "_cloudsearch_205_SearchItemsByViewUrlResponseOut",
        "ButtonIn": "_cloudsearch_206_ButtonIn",
        "ButtonOut": "_cloudsearch_207_ButtonOut",
        "AppsDynamiteSharedCallMetadataIn": "_cloudsearch_208_AppsDynamiteSharedCallMetadataIn",
        "AppsDynamiteSharedCallMetadataOut": "_cloudsearch_209_AppsDynamiteSharedCallMetadataOut",
        "AppsDynamiteSharedAssistantDebugContextIn": "_cloudsearch_210_AppsDynamiteSharedAssistantDebugContextIn",
        "AppsDynamiteSharedAssistantDebugContextOut": "_cloudsearch_211_AppsDynamiteSharedAssistantDebugContextOut",
        "AppsDynamiteSharedAssistantSessionContextIn": "_cloudsearch_212_AppsDynamiteSharedAssistantSessionContextIn",
        "AppsDynamiteSharedAssistantSessionContextOut": "_cloudsearch_213_AppsDynamiteSharedAssistantSessionContextOut",
        "AppsDynamiteV1ApiCompatV1AttachmentIn": "_cloudsearch_214_AppsDynamiteV1ApiCompatV1AttachmentIn",
        "AppsDynamiteV1ApiCompatV1AttachmentOut": "_cloudsearch_215_AppsDynamiteV1ApiCompatV1AttachmentOut",
        "ReactionInfoIn": "_cloudsearch_216_ReactionInfoIn",
        "ReactionInfoOut": "_cloudsearch_217_ReactionInfoOut",
        "EditorClientActionMarkupIn": "_cloudsearch_218_EditorClientActionMarkupIn",
        "EditorClientActionMarkupOut": "_cloudsearch_219_EditorClientActionMarkupOut",
        "HangoutEventIn": "_cloudsearch_220_HangoutEventIn",
        "HangoutEventOut": "_cloudsearch_221_HangoutEventOut",
        "SearchApplicationIn": "_cloudsearch_222_SearchApplicationIn",
        "SearchApplicationOut": "_cloudsearch_223_SearchApplicationOut",
        "GoogleChatV1WidgetMarkupFormActionActionParameterIn": "_cloudsearch_224_GoogleChatV1WidgetMarkupFormActionActionParameterIn",
        "GoogleChatV1WidgetMarkupFormActionActionParameterOut": "_cloudsearch_225_GoogleChatV1WidgetMarkupFormActionActionParameterOut",
        "FacetResultIn": "_cloudsearch_226_FacetResultIn",
        "FacetResultOut": "_cloudsearch_227_FacetResultOut",
        "GmailClientActionMarkupIn": "_cloudsearch_228_GmailClientActionMarkupIn",
        "GmailClientActionMarkupOut": "_cloudsearch_229_GmailClientActionMarkupOut",
        "MediaIn": "_cloudsearch_230_MediaIn",
        "MediaOut": "_cloudsearch_231_MediaOut",
        "AppsDynamiteSharedSegmentedMembershipCountIn": "_cloudsearch_232_AppsDynamiteSharedSegmentedMembershipCountIn",
        "AppsDynamiteSharedSegmentedMembershipCountOut": "_cloudsearch_233_AppsDynamiteSharedSegmentedMembershipCountOut",
        "StreamViewerStatsIn": "_cloudsearch_234_StreamViewerStatsIn",
        "StreamViewerStatsOut": "_cloudsearch_235_StreamViewerStatsOut",
        "VideoInfoIn": "_cloudsearch_236_VideoInfoIn",
        "VideoInfoOut": "_cloudsearch_237_VideoInfoOut",
        "ClusterInfoIn": "_cloudsearch_238_ClusterInfoIn",
        "ClusterInfoOut": "_cloudsearch_239_ClusterInfoOut",
        "ListItemNamesForUnmappedIdentityResponseIn": "_cloudsearch_240_ListItemNamesForUnmappedIdentityResponseIn",
        "ListItemNamesForUnmappedIdentityResponseOut": "_cloudsearch_241_ListItemNamesForUnmappedIdentityResponseOut",
        "ResultDisplayFieldIn": "_cloudsearch_242_ResultDisplayFieldIn",
        "ResultDisplayFieldOut": "_cloudsearch_243_ResultDisplayFieldOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn": "_cloudsearch_244_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut": "_cloudsearch_245_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut",
        "SchemaIn": "_cloudsearch_246_SchemaIn",
        "SchemaOut": "_cloudsearch_247_SchemaOut",
        "JobsettedServerSpecIn": "_cloudsearch_248_JobsettedServerSpecIn",
        "JobsettedServerSpecOut": "_cloudsearch_249_JobsettedServerSpecOut",
        "ItemContentIn": "_cloudsearch_250_ItemContentIn",
        "ItemContentOut": "_cloudsearch_251_ItemContentOut",
        "MembershipChangedMetadataIn": "_cloudsearch_252_MembershipChangedMetadataIn",
        "MembershipChangedMetadataOut": "_cloudsearch_253_MembershipChangedMetadataOut",
        "QueryCountByStatusIn": "_cloudsearch_254_QueryCountByStatusIn",
        "QueryCountByStatusOut": "_cloudsearch_255_QueryCountByStatusOut",
        "VoicePhoneNumberI18nDataIn": "_cloudsearch_256_VoicePhoneNumberI18nDataIn",
        "VoicePhoneNumberI18nDataOut": "_cloudsearch_257_VoicePhoneNumberI18nDataOut",
        "TriggerActionIn": "_cloudsearch_258_TriggerActionIn",
        "TriggerActionOut": "_cloudsearch_259_TriggerActionOut",
        "GridItemIn": "_cloudsearch_260_GridItemIn",
        "GridItemOut": "_cloudsearch_261_GridItemOut",
        "GSuitePrincipalIn": "_cloudsearch_262_GSuitePrincipalIn",
        "GSuitePrincipalOut": "_cloudsearch_263_GSuitePrincipalOut",
        "SlashCommandMetadataIn": "_cloudsearch_264_SlashCommandMetadataIn",
        "SlashCommandMetadataOut": "_cloudsearch_265_SlashCommandMetadataOut",
        "IndexItemOptionsIn": "_cloudsearch_266_IndexItemOptionsIn",
        "IndexItemOptionsOut": "_cloudsearch_267_IndexItemOptionsOut",
        "CseInfoIn": "_cloudsearch_268_CseInfoIn",
        "CseInfoOut": "_cloudsearch_269_CseInfoOut",
        "CustomFunctionReturnValueMarkupIn": "_cloudsearch_270_CustomFunctionReturnValueMarkupIn",
        "CustomFunctionReturnValueMarkupOut": "_cloudsearch_271_CustomFunctionReturnValueMarkupOut",
        "GoogleChatV1ContextualAddOnMarkupIn": "_cloudsearch_272_GoogleChatV1ContextualAddOnMarkupIn",
        "GoogleChatV1ContextualAddOnMarkupOut": "_cloudsearch_273_GoogleChatV1ContextualAddOnMarkupOut",
        "PreStateIn": "_cloudsearch_274_PreStateIn",
        "PreStateOut": "_cloudsearch_275_PreStateOut",
        "PinnedItemIdIn": "_cloudsearch_276_PinnedItemIdIn",
        "PinnedItemIdOut": "_cloudsearch_277_PinnedItemIdOut",
        "YouTubeBroadcastSessionInfoIn": "_cloudsearch_278_YouTubeBroadcastSessionInfoIn",
        "YouTubeBroadcastSessionInfoOut": "_cloudsearch_279_YouTubeBroadcastSessionInfoOut",
        "QueryOperatorIn": "_cloudsearch_280_QueryOperatorIn",
        "QueryOperatorOut": "_cloudsearch_281_QueryOperatorOut",
        "CustomerUserStatsIn": "_cloudsearch_282_CustomerUserStatsIn",
        "CustomerUserStatsOut": "_cloudsearch_283_CustomerUserStatsOut",
        "IntegerOperatorOptionsIn": "_cloudsearch_284_IntegerOperatorOptionsIn",
        "IntegerOperatorOptionsOut": "_cloudsearch_285_IntegerOperatorOptionsOut",
        "EditMetadataIn": "_cloudsearch_286_EditMetadataIn",
        "EditMetadataOut": "_cloudsearch_287_EditMetadataOut",
        "FolderAttributeIn": "_cloudsearch_288_FolderAttributeIn",
        "FolderAttributeOut": "_cloudsearch_289_FolderAttributeOut",
        "RecordingInfoIn": "_cloudsearch_290_RecordingInfoIn",
        "RecordingInfoOut": "_cloudsearch_291_RecordingInfoOut",
        "TriggerKeyIn": "_cloudsearch_292_TriggerKeyIn",
        "TriggerKeyOut": "_cloudsearch_293_TriggerKeyOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn": "_cloudsearch_294_AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut": "_cloudsearch_295_AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut",
        "CustomerIndexStatsIn": "_cloudsearch_296_CustomerIndexStatsIn",
        "CustomerIndexStatsOut": "_cloudsearch_297_CustomerIndexStatsOut",
        "InteractionIn": "_cloudsearch_298_InteractionIn",
        "InteractionOut": "_cloudsearch_299_InteractionOut",
        "MemberIn": "_cloudsearch_300_MemberIn",
        "MemberOut": "_cloudsearch_301_MemberOut",
        "OtrModificationEventIn": "_cloudsearch_302_OtrModificationEventIn",
        "OtrModificationEventOut": "_cloudsearch_303_OtrModificationEventOut",
        "DisplayedPropertyIn": "_cloudsearch_304_DisplayedPropertyIn",
        "DisplayedPropertyOut": "_cloudsearch_305_DisplayedPropertyOut",
        "SelectionControlIn": "_cloudsearch_306_SelectionControlIn",
        "SelectionControlOut": "_cloudsearch_307_SelectionControlOut",
        "IntegerValuesIn": "_cloudsearch_308_IntegerValuesIn",
        "IntegerValuesOut": "_cloudsearch_309_IntegerValuesOut",
        "DriveFollowUpRestrictIn": "_cloudsearch_310_DriveFollowUpRestrictIn",
        "DriveFollowUpRestrictOut": "_cloudsearch_311_DriveFollowUpRestrictOut",
        "GaiaGroupProtoIn": "_cloudsearch_312_GaiaGroupProtoIn",
        "GaiaGroupProtoOut": "_cloudsearch_313_GaiaGroupProtoOut",
        "LdapGroupProtoIn": "_cloudsearch_314_LdapGroupProtoIn",
        "LdapGroupProtoOut": "_cloudsearch_315_LdapGroupProtoOut",
        "YouTubeBroadcastStatsIn": "_cloudsearch_316_YouTubeBroadcastStatsIn",
        "YouTubeBroadcastStatsOut": "_cloudsearch_317_YouTubeBroadcastStatsOut",
        "TopicStateIn": "_cloudsearch_318_TopicStateIn",
        "TopicStateOut": "_cloudsearch_319_TopicStateOut",
        "UpdateDraftActionMarkupIn": "_cloudsearch_320_UpdateDraftActionMarkupIn",
        "UpdateDraftActionMarkupOut": "_cloudsearch_321_UpdateDraftActionMarkupOut",
        "MessageAttributesIn": "_cloudsearch_322_MessageAttributesIn",
        "MessageAttributesOut": "_cloudsearch_323_MessageAttributesOut",
        "AppsDynamiteStorageOnClickIn": "_cloudsearch_324_AppsDynamiteStorageOnClickIn",
        "AppsDynamiteStorageOnClickOut": "_cloudsearch_325_AppsDynamiteStorageOnClickOut",
        "CardCapabilityMetadataIn": "_cloudsearch_326_CardCapabilityMetadataIn",
        "CardCapabilityMetadataOut": "_cloudsearch_327_CardCapabilityMetadataOut",
        "AppsDynamiteSharedTasksAnnotationDataIn": "_cloudsearch_328_AppsDynamiteSharedTasksAnnotationDataIn",
        "AppsDynamiteSharedTasksAnnotationDataOut": "_cloudsearch_329_AppsDynamiteSharedTasksAnnotationDataOut",
        "UserMentionMetadataIn": "_cloudsearch_330_UserMentionMetadataIn",
        "UserMentionMetadataOut": "_cloudsearch_331_UserMentionMetadataOut",
        "GoogleChatV1ContextualAddOnMarkupCardCardActionIn": "_cloudsearch_332_GoogleChatV1ContextualAddOnMarkupCardCardActionIn",
        "GoogleChatV1ContextualAddOnMarkupCardCardActionOut": "_cloudsearch_333_GoogleChatV1ContextualAddOnMarkupCardCardActionOut",
        "AppsDynamiteSharedOrganizationInfoIn": "_cloudsearch_334_AppsDynamiteSharedOrganizationInfoIn",
        "AppsDynamiteSharedOrganizationInfoOut": "_cloudsearch_335_AppsDynamiteSharedOrganizationInfoOut",
        "AppsDynamiteStorageDividerIn": "_cloudsearch_336_AppsDynamiteStorageDividerIn",
        "AppsDynamiteStorageDividerOut": "_cloudsearch_337_AppsDynamiteStorageDividerOut",
        "SearchResponseIn": "_cloudsearch_338_SearchResponseIn",
        "SearchResponseOut": "_cloudsearch_339_SearchResponseOut",
        "TextKeyValueIn": "_cloudsearch_340_TextKeyValueIn",
        "TextKeyValueOut": "_cloudsearch_341_TextKeyValueOut",
        "EnumOperatorOptionsIn": "_cloudsearch_342_EnumOperatorOptionsIn",
        "EnumOperatorOptionsOut": "_cloudsearch_343_EnumOperatorOptionsOut",
        "SocialGraphNodeProtoIn": "_cloudsearch_344_SocialGraphNodeProtoIn",
        "SocialGraphNodeProtoOut": "_cloudsearch_345_SocialGraphNodeProtoOut",
        "AppsDynamiteSharedContentReportTypeIn": "_cloudsearch_346_AppsDynamiteSharedContentReportTypeIn",
        "AppsDynamiteSharedContentReportTypeOut": "_cloudsearch_347_AppsDynamiteSharedContentReportTypeOut",
        "MultiKeyIn": "_cloudsearch_348_MultiKeyIn",
        "MultiKeyOut": "_cloudsearch_349_MultiKeyOut",
        "ContextualAddOnMarkupIn": "_cloudsearch_350_ContextualAddOnMarkupIn",
        "ContextualAddOnMarkupOut": "_cloudsearch_351_ContextualAddOnMarkupOut",
        "RetrievalImportanceIn": "_cloudsearch_352_RetrievalImportanceIn",
        "RetrievalImportanceOut": "_cloudsearch_353_RetrievalImportanceOut",
        "RequestFileScopeForActiveDocumentIn": "_cloudsearch_354_RequestFileScopeForActiveDocumentIn",
        "RequestFileScopeForActiveDocumentOut": "_cloudsearch_355_RequestFileScopeForActiveDocumentOut",
        "AnnotationIn": "_cloudsearch_356_AnnotationIn",
        "AnnotationOut": "_cloudsearch_357_AnnotationOut",
        "BabelMessagePropsIn": "_cloudsearch_358_BabelMessagePropsIn",
        "BabelMessagePropsOut": "_cloudsearch_359_BabelMessagePropsOut",
        "YoutubeMetadataIn": "_cloudsearch_360_YoutubeMetadataIn",
        "YoutubeMetadataOut": "_cloudsearch_361_YoutubeMetadataOut",
        "AppsDynamiteSharedJustificationPersonIn": "_cloudsearch_362_AppsDynamiteSharedJustificationPersonIn",
        "AppsDynamiteSharedJustificationPersonOut": "_cloudsearch_363_AppsDynamiteSharedJustificationPersonOut",
        "RequestOptionsIn": "_cloudsearch_364_RequestOptionsIn",
        "RequestOptionsOut": "_cloudsearch_365_RequestOptionsOut",
        "FixedFooterIn": "_cloudsearch_366_FixedFooterIn",
        "FixedFooterOut": "_cloudsearch_367_FixedFooterOut",
        "AppsDynamiteSharedAssistantUnfulfillableRequestIn": "_cloudsearch_368_AppsDynamiteSharedAssistantUnfulfillableRequestIn",
        "AppsDynamiteSharedAssistantUnfulfillableRequestOut": "_cloudsearch_369_AppsDynamiteSharedAssistantUnfulfillableRequestOut",
        "AppsDynamiteSharedTextSegmentIn": "_cloudsearch_370_AppsDynamiteSharedTextSegmentIn",
        "AppsDynamiteSharedTextSegmentOut": "_cloudsearch_371_AppsDynamiteSharedTextSegmentOut",
        "AppsDynamiteSharedGroupDetailsIn": "_cloudsearch_372_AppsDynamiteSharedGroupDetailsIn",
        "AppsDynamiteSharedGroupDetailsOut": "_cloudsearch_373_AppsDynamiteSharedGroupDetailsOut",
        "AppsDynamiteV1ApiCompatV1ActionConfirmIn": "_cloudsearch_374_AppsDynamiteV1ApiCompatV1ActionConfirmIn",
        "AppsDynamiteV1ApiCompatV1ActionConfirmOut": "_cloudsearch_375_AppsDynamiteV1ApiCompatV1ActionConfirmOut",
        "SnippetIn": "_cloudsearch_376_SnippetIn",
        "SnippetOut": "_cloudsearch_377_SnippetOut",
        "AppsDynamiteStorageGridGridItemIn": "_cloudsearch_378_AppsDynamiteStorageGridGridItemIn",
        "AppsDynamiteStorageGridGridItemOut": "_cloudsearch_379_AppsDynamiteStorageGridGridItemOut",
        "GoogleChatV1WidgetMarkupOpenLinkIn": "_cloudsearch_380_GoogleChatV1WidgetMarkupOpenLinkIn",
        "GoogleChatV1WidgetMarkupOpenLinkOut": "_cloudsearch_381_GoogleChatV1WidgetMarkupOpenLinkOut",
        "IntegerPropertyOptionsIn": "_cloudsearch_382_IntegerPropertyOptionsIn",
        "IntegerPropertyOptionsOut": "_cloudsearch_383_IntegerPropertyOptionsOut",
        "MetadataIn": "_cloudsearch_384_MetadataIn",
        "MetadataOut": "_cloudsearch_385_MetadataOut",
        "FormattingIn": "_cloudsearch_386_FormattingIn",
        "FormattingOut": "_cloudsearch_387_FormattingOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn": "_cloudsearch_388_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut": "_cloudsearch_389_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut",
        "SearchApplicationQueryStatsIn": "_cloudsearch_390_SearchApplicationQueryStatsIn",
        "SearchApplicationQueryStatsOut": "_cloudsearch_391_SearchApplicationQueryStatsOut",
        "StreamingSessionInfoIn": "_cloudsearch_392_StreamingSessionInfoIn",
        "StreamingSessionInfoOut": "_cloudsearch_393_StreamingSessionInfoOut",
        "AppsDynamiteSharedTextWithDescriptionIn": "_cloudsearch_394_AppsDynamiteSharedTextWithDescriptionIn",
        "AppsDynamiteSharedTextWithDescriptionOut": "_cloudsearch_395_AppsDynamiteSharedTextWithDescriptionOut",
        "ImapSessionContextIn": "_cloudsearch_396_ImapSessionContextIn",
        "ImapSessionContextOut": "_cloudsearch_397_ImapSessionContextOut",
        "MeetingSpaceIn": "_cloudsearch_398_MeetingSpaceIn",
        "MeetingSpaceOut": "_cloudsearch_399_MeetingSpaceOut",
        "AppsDynamiteStorageCardIn": "_cloudsearch_400_AppsDynamiteStorageCardIn",
        "AppsDynamiteStorageCardOut": "_cloudsearch_401_AppsDynamiteStorageCardOut",
        "PushItemRequestIn": "_cloudsearch_402_PushItemRequestIn",
        "PushItemRequestOut": "_cloudsearch_403_PushItemRequestOut",
        "ScoringConfigIn": "_cloudsearch_404_ScoringConfigIn",
        "ScoringConfigOut": "_cloudsearch_405_ScoringConfigOut",
        "SheetsClientActionMarkupIn": "_cloudsearch_406_SheetsClientActionMarkupIn",
        "SheetsClientActionMarkupOut": "_cloudsearch_407_SheetsClientActionMarkupOut",
        "ResultCountsIn": "_cloudsearch_408_ResultCountsIn",
        "ResultCountsOut": "_cloudsearch_409_ResultCountsOut",
        "DriveMetadataIn": "_cloudsearch_410_DriveMetadataIn",
        "DriveMetadataOut": "_cloudsearch_411_DriveMetadataOut",
        "IndexItemRequestIn": "_cloudsearch_412_IndexItemRequestIn",
        "IndexItemRequestOut": "_cloudsearch_413_IndexItemRequestOut",
        "GatewayAccessIn": "_cloudsearch_414_GatewayAccessIn",
        "GatewayAccessOut": "_cloudsearch_415_GatewayAccessOut",
        "ConsentedAppUnfurlMetadataIn": "_cloudsearch_416_ConsentedAppUnfurlMetadataIn",
        "ConsentedAppUnfurlMetadataOut": "_cloudsearch_417_ConsentedAppUnfurlMetadataOut",
        "AttachmentIn": "_cloudsearch_418_AttachmentIn",
        "AttachmentOut": "_cloudsearch_419_AttachmentOut",
        "UserInfoIn": "_cloudsearch_420_UserInfoIn",
        "UserInfoOut": "_cloudsearch_421_UserInfoOut",
        "AppsDynamiteStorageImageCropStyleIn": "_cloudsearch_422_AppsDynamiteStorageImageCropStyleIn",
        "AppsDynamiteStorageImageCropStyleOut": "_cloudsearch_423_AppsDynamiteStorageImageCropStyleOut",
        "SourceResultCountIn": "_cloudsearch_424_SourceResultCountIn",
        "SourceResultCountOut": "_cloudsearch_425_SourceResultCountOut",
        "BroadcastStatsIn": "_cloudsearch_426_BroadcastStatsIn",
        "BroadcastStatsOut": "_cloudsearch_427_BroadcastStatsOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataIn": "_cloudsearch_428_AppsDynamiteSharedCalendarEventAnnotationDataIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataOut": "_cloudsearch_429_AppsDynamiteSharedCalendarEventAnnotationDataOut",
        "AppsDynamiteStorageDecoratedTextSwitchControlIn": "_cloudsearch_430_AppsDynamiteStorageDecoratedTextSwitchControlIn",
        "AppsDynamiteStorageDecoratedTextSwitchControlOut": "_cloudsearch_431_AppsDynamiteStorageDecoratedTextSwitchControlOut",
        "TypeInfoIn": "_cloudsearch_432_TypeInfoIn",
        "TypeInfoOut": "_cloudsearch_433_TypeInfoOut",
        "ReferencesIn": "_cloudsearch_434_ReferencesIn",
        "ReferencesOut": "_cloudsearch_435_ReferencesOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn": "_cloudsearch_436_AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut": "_cloudsearch_437_AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut",
        "HtmlValuesIn": "_cloudsearch_438_HtmlValuesIn",
        "HtmlValuesOut": "_cloudsearch_439_HtmlValuesOut",
        "ThreadKeySetIn": "_cloudsearch_440_ThreadKeySetIn",
        "ThreadKeySetOut": "_cloudsearch_441_ThreadKeySetOut",
        "WidgetMarkupIn": "_cloudsearch_442_WidgetMarkupIn",
        "WidgetMarkupOut": "_cloudsearch_443_WidgetMarkupOut",
        "ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn": "_cloudsearch_444_ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut": "_cloudsearch_445_ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut",
        "DateIn": "_cloudsearch_446_DateIn",
        "DateOut": "_cloudsearch_447_DateOut",
        "OtrChatMessageEventIn": "_cloudsearch_448_OtrChatMessageEventIn",
        "OtrChatMessageEventOut": "_cloudsearch_449_OtrChatMessageEventOut",
        "EnumValuesIn": "_cloudsearch_450_EnumValuesIn",
        "EnumValuesOut": "_cloudsearch_451_EnumValuesOut",
        "SessionStateInfoIn": "_cloudsearch_452_SessionStateInfoIn",
        "SessionStateInfoOut": "_cloudsearch_453_SessionStateInfoOut",
        "AppsDynamiteStorageColumnsIn": "_cloudsearch_454_AppsDynamiteStorageColumnsIn",
        "AppsDynamiteStorageColumnsOut": "_cloudsearch_455_AppsDynamiteStorageColumnsOut",
        "UserIdIn": "_cloudsearch_456_UserIdIn",
        "UserIdOut": "_cloudsearch_457_UserIdOut",
        "AppsDynamiteSharedGroupVisibilityIn": "_cloudsearch_458_AppsDynamiteSharedGroupVisibilityIn",
        "AppsDynamiteSharedGroupVisibilityOut": "_cloudsearch_459_AppsDynamiteSharedGroupVisibilityOut",
        "AppsDynamiteSharedUserBlockRelationshipIn": "_cloudsearch_460_AppsDynamiteSharedUserBlockRelationshipIn",
        "AppsDynamiteSharedUserBlockRelationshipOut": "_cloudsearch_461_AppsDynamiteSharedUserBlockRelationshipOut",
        "UnmappedIdentityIn": "_cloudsearch_462_UnmappedIdentityIn",
        "UnmappedIdentityOut": "_cloudsearch_463_UnmappedIdentityOut",
        "GroupRetentionSettingsUpdatedMetaDataIn": "_cloudsearch_464_GroupRetentionSettingsUpdatedMetaDataIn",
        "GroupRetentionSettingsUpdatedMetaDataOut": "_cloudsearch_465_GroupRetentionSettingsUpdatedMetaDataOut",
        "SafeUrlProtoIn": "_cloudsearch_466_SafeUrlProtoIn",
        "SafeUrlProtoOut": "_cloudsearch_467_SafeUrlProtoOut",
        "MessageParentIdIn": "_cloudsearch_468_MessageParentIdIn",
        "MessageParentIdOut": "_cloudsearch_469_MessageParentIdOut",
        "ImapUpdateIn": "_cloudsearch_470_ImapUpdateIn",
        "ImapUpdateOut": "_cloudsearch_471_ImapUpdateOut",
        "PropertyDisplayOptionsIn": "_cloudsearch_472_PropertyDisplayOptionsIn",
        "PropertyDisplayOptionsOut": "_cloudsearch_473_PropertyDisplayOptionsOut",
        "SearchItemsByViewUrlRequestIn": "_cloudsearch_474_SearchItemsByViewUrlRequestIn",
        "SearchItemsByViewUrlRequestOut": "_cloudsearch_475_SearchItemsByViewUrlRequestOut",
        "AppsDynamiteSharedSpaceInfoIn": "_cloudsearch_476_AppsDynamiteSharedSpaceInfoIn",
        "AppsDynamiteSharedSpaceInfoOut": "_cloudsearch_477_AppsDynamiteSharedSpaceInfoOut",
        "GoogleDocsResultInfoIn": "_cloudsearch_478_GoogleDocsResultInfoIn",
        "GoogleDocsResultInfoOut": "_cloudsearch_479_GoogleDocsResultInfoOut",
        "ContactGroupProtoIn": "_cloudsearch_480_ContactGroupProtoIn",
        "ContactGroupProtoOut": "_cloudsearch_481_ContactGroupProtoOut",
        "UserDisplayInfoIn": "_cloudsearch_482_UserDisplayInfoIn",
        "UserDisplayInfoOut": "_cloudsearch_483_UserDisplayInfoOut",
        "CollaborationIn": "_cloudsearch_484_CollaborationIn",
        "CollaborationOut": "_cloudsearch_485_CollaborationOut",
        "ListOperationsResponseIn": "_cloudsearch_486_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudsearch_487_ListOperationsResponseOut",
        "TopicIdIn": "_cloudsearch_488_TopicIdIn",
        "TopicIdOut": "_cloudsearch_489_TopicIdOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn": "_cloudsearch_490_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut": "_cloudsearch_491_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn": "_cloudsearch_492_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut": "_cloudsearch_493_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut",
        "OpenLinkIn": "_cloudsearch_494_OpenLinkIn",
        "OpenLinkOut": "_cloudsearch_495_OpenLinkOut",
        "AppsDynamiteSharedAssistantSuggestionIn": "_cloudsearch_496_AppsDynamiteSharedAssistantSuggestionIn",
        "AppsDynamiteSharedAssistantSuggestionOut": "_cloudsearch_497_AppsDynamiteSharedAssistantSuggestionOut",
        "AppsDynamiteStorageDateTimePickerIn": "_cloudsearch_498_AppsDynamiteStorageDateTimePickerIn",
        "AppsDynamiteStorageDateTimePickerOut": "_cloudsearch_499_AppsDynamiteStorageDateTimePickerOut",
        "UpdateBodyIn": "_cloudsearch_500_UpdateBodyIn",
        "UpdateBodyOut": "_cloudsearch_501_UpdateBodyOut",
        "ObjectPropertyOptionsIn": "_cloudsearch_502_ObjectPropertyOptionsIn",
        "ObjectPropertyOptionsOut": "_cloudsearch_503_ObjectPropertyOptionsOut",
        "AppsDynamiteSharedDimensionIn": "_cloudsearch_504_AppsDynamiteSharedDimensionIn",
        "AppsDynamiteSharedDimensionOut": "_cloudsearch_505_AppsDynamiteSharedDimensionOut",
        "RankIn": "_cloudsearch_506_RankIn",
        "RankOut": "_cloudsearch_507_RankOut",
        "PrefUpdateIn": "_cloudsearch_508_PrefUpdateIn",
        "PrefUpdateOut": "_cloudsearch_509_PrefUpdateOut",
        "QuotedMessageMetadataIn": "_cloudsearch_510_QuotedMessageMetadataIn",
        "QuotedMessageMetadataOut": "_cloudsearch_511_QuotedMessageMetadataOut",
        "UpdateSchemaRequestIn": "_cloudsearch_512_UpdateSchemaRequestIn",
        "UpdateSchemaRequestOut": "_cloudsearch_513_UpdateSchemaRequestOut",
        "BorderStyleIn": "_cloudsearch_514_BorderStyleIn",
        "BorderStyleOut": "_cloudsearch_515_BorderStyleOut",
        "StartUploadItemRequestIn": "_cloudsearch_516_StartUploadItemRequestIn",
        "StartUploadItemRequestOut": "_cloudsearch_517_StartUploadItemRequestOut",
        "ItemCountByStatusIn": "_cloudsearch_518_ItemCountByStatusIn",
        "ItemCountByStatusOut": "_cloudsearch_519_ItemCountByStatusOut",
        "InteractionDataIn": "_cloudsearch_520_InteractionDataIn",
        "InteractionDataOut": "_cloudsearch_521_InteractionDataOut",
        "ImageButtonIn": "_cloudsearch_522_ImageButtonIn",
        "ImageButtonOut": "_cloudsearch_523_ImageButtonOut",
        "ContextAttributeIn": "_cloudsearch_524_ContextAttributeIn",
        "ContextAttributeOut": "_cloudsearch_525_ContextAttributeOut",
        "BooleanOperatorOptionsIn": "_cloudsearch_526_BooleanOperatorOptionsIn",
        "BooleanOperatorOptionsOut": "_cloudsearch_527_BooleanOperatorOptionsOut",
        "OsVersionIn": "_cloudsearch_528_OsVersionIn",
        "OsVersionOut": "_cloudsearch_529_OsVersionOut",
        "ItemStructuredDataIn": "_cloudsearch_530_ItemStructuredDataIn",
        "ItemStructuredDataOut": "_cloudsearch_531_ItemStructuredDataOut",
        "DividerIn": "_cloudsearch_532_DividerIn",
        "DividerOut": "_cloudsearch_533_DividerOut",
        "PushItemIn": "_cloudsearch_534_PushItemIn",
        "PushItemOut": "_cloudsearch_535_PushItemOut",
        "AppsDynamiteSharedCardClickSuggestionIn": "_cloudsearch_536_AppsDynamiteSharedCardClickSuggestionIn",
        "AppsDynamiteSharedCardClickSuggestionOut": "_cloudsearch_537_AppsDynamiteSharedCardClickSuggestionOut",
        "StoredParticipantIdIn": "_cloudsearch_538_StoredParticipantIdIn",
        "StoredParticipantIdOut": "_cloudsearch_539_StoredParticipantIdOut",
        "AppsDynamiteSharedCallAnnotationDataIn": "_cloudsearch_540_AppsDynamiteSharedCallAnnotationDataIn",
        "AppsDynamiteSharedCallAnnotationDataOut": "_cloudsearch_541_AppsDynamiteSharedCallAnnotationDataOut",
        "TriggerIn": "_cloudsearch_542_TriggerIn",
        "TriggerOut": "_cloudsearch_543_TriggerOut",
        "UnreserveItemsRequestIn": "_cloudsearch_544_UnreserveItemsRequestIn",
        "UnreserveItemsRequestOut": "_cloudsearch_545_UnreserveItemsRequestOut",
        "DynamiteSpacesScoringInfoIn": "_cloudsearch_546_DynamiteSpacesScoringInfoIn",
        "DynamiteSpacesScoringInfoOut": "_cloudsearch_547_DynamiteSpacesScoringInfoOut",
        "MenuIn": "_cloudsearch_548_MenuIn",
        "MenuOut": "_cloudsearch_549_MenuOut",
        "ListItemsResponseIn": "_cloudsearch_550_ListItemsResponseIn",
        "ListItemsResponseOut": "_cloudsearch_551_ListItemsResponseOut",
        "RecipientIn": "_cloudsearch_552_RecipientIn",
        "RecipientOut": "_cloudsearch_553_RecipientOut",
        "ItemIn": "_cloudsearch_554_ItemIn",
        "ItemOut": "_cloudsearch_555_ItemOut",
        "FolderIn": "_cloudsearch_556_FolderIn",
        "FolderOut": "_cloudsearch_557_FolderOut",
        "SegmentIn": "_cloudsearch_558_SegmentIn",
        "SegmentOut": "_cloudsearch_559_SegmentOut",
        "SourceIn": "_cloudsearch_560_SourceIn",
        "SourceOut": "_cloudsearch_561_SourceOut",
        "ItemPartsIn": "_cloudsearch_562_ItemPartsIn",
        "ItemPartsOut": "_cloudsearch_563_ItemPartsOut",
        "ReferenceIn": "_cloudsearch_564_ReferenceIn",
        "ReferenceOut": "_cloudsearch_565_ReferenceOut",
        "TextValuesIn": "_cloudsearch_566_TextValuesIn",
        "TextValuesOut": "_cloudsearch_567_TextValuesOut",
        "LinkDataIn": "_cloudsearch_568_LinkDataIn",
        "LinkDataOut": "_cloudsearch_569_LinkDataOut",
        "TransactionDebugInfoIn": "_cloudsearch_570_TransactionDebugInfoIn",
        "TransactionDebugInfoOut": "_cloudsearch_571_TransactionDebugInfoOut",
        "RbacSubjectProtoIn": "_cloudsearch_572_RbacSubjectProtoIn",
        "RbacSubjectProtoOut": "_cloudsearch_573_RbacSubjectProtoOut",
        "DeleteMetadataIn": "_cloudsearch_574_DeleteMetadataIn",
        "DeleteMetadataOut": "_cloudsearch_575_DeleteMetadataOut",
        "GoogleChatV1WidgetMarkupKeyValueIn": "_cloudsearch_576_GoogleChatV1WidgetMarkupKeyValueIn",
        "GoogleChatV1WidgetMarkupKeyValueOut": "_cloudsearch_577_GoogleChatV1WidgetMarkupKeyValueOut",
        "QueryInterpretationIn": "_cloudsearch_578_QueryInterpretationIn",
        "QueryInterpretationOut": "_cloudsearch_579_QueryInterpretationOut",
        "DeepLinkDataIn": "_cloudsearch_580_DeepLinkDataIn",
        "DeepLinkDataOut": "_cloudsearch_581_DeepLinkDataOut",
        "SearchApplicationSessionStatsIn": "_cloudsearch_582_SearchApplicationSessionStatsIn",
        "SearchApplicationSessionStatsOut": "_cloudsearch_583_SearchApplicationSessionStatsOut",
        "TransactionContextIn": "_cloudsearch_584_TransactionContextIn",
        "TransactionContextOut": "_cloudsearch_585_TransactionContextOut",
        "AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn": "_cloudsearch_586_AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn",
        "AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut": "_cloudsearch_587_AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut",
        "UpdateCcRecipientsIn": "_cloudsearch_588_UpdateCcRecipientsIn",
        "UpdateCcRecipientsOut": "_cloudsearch_589_UpdateCcRecipientsOut",
        "FilterIn": "_cloudsearch_590_FilterIn",
        "FilterOut": "_cloudsearch_591_FilterOut",
        "AppsDynamiteSharedTextSegmentsWithDescriptionIn": "_cloudsearch_592_AppsDynamiteSharedTextSegmentsWithDescriptionIn",
        "AppsDynamiteSharedTextSegmentsWithDescriptionOut": "_cloudsearch_593_AppsDynamiteSharedTextSegmentsWithDescriptionOut",
        "StatusIn": "_cloudsearch_594_StatusIn",
        "StatusOut": "_cloudsearch_595_StatusOut",
        "ObjectValuesIn": "_cloudsearch_596_ObjectValuesIn",
        "ObjectValuesOut": "_cloudsearch_597_ObjectValuesOut",
        "SuggestResultIn": "_cloudsearch_598_SuggestResultIn",
        "SuggestResultOut": "_cloudsearch_599_SuggestResultOut",
        "AttributeSetIn": "_cloudsearch_600_AttributeSetIn",
        "AttributeSetOut": "_cloudsearch_601_AttributeSetOut",
        "ImapsyncFolderAttributeFolderMessageIn": "_cloudsearch_602_ImapsyncFolderAttributeFolderMessageIn",
        "ImapsyncFolderAttributeFolderMessageOut": "_cloudsearch_603_ImapsyncFolderAttributeFolderMessageOut",
        "OpenCreatedDraftActionMarkupIn": "_cloudsearch_604_OpenCreatedDraftActionMarkupIn",
        "OpenCreatedDraftActionMarkupOut": "_cloudsearch_605_OpenCreatedDraftActionMarkupOut",
        "ItemAclIn": "_cloudsearch_606_ItemAclIn",
        "ItemAclOut": "_cloudsearch_607_ItemAclOut",
        "AppsDynamiteSharedReactionIn": "_cloudsearch_608_AppsDynamiteSharedReactionIn",
        "AppsDynamiteSharedReactionOut": "_cloudsearch_609_AppsDynamiteSharedReactionOut",
        "BotInfoIn": "_cloudsearch_610_BotInfoIn",
        "BotInfoOut": "_cloudsearch_611_BotInfoOut",
        "TranscriptionSessionInfoIn": "_cloudsearch_612_TranscriptionSessionInfoIn",
        "TranscriptionSessionInfoOut": "_cloudsearch_613_TranscriptionSessionInfoOut",
        "GetCustomerQueryStatsResponseIn": "_cloudsearch_614_GetCustomerQueryStatsResponseIn",
        "GetCustomerQueryStatsResponseOut": "_cloudsearch_615_GetCustomerQueryStatsResponseOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn": "_cloudsearch_616_AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut": "_cloudsearch_617_AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut",
        "ImageIn": "_cloudsearch_618_ImageIn",
        "ImageOut": "_cloudsearch_619_ImageOut",
        "SessionEventIn": "_cloudsearch_620_SessionEventIn",
        "SessionEventOut": "_cloudsearch_621_SessionEventOut",
        "LabelUpdatedIn": "_cloudsearch_622_LabelUpdatedIn",
        "LabelUpdatedOut": "_cloudsearch_623_LabelUpdatedOut",
        "AppsDynamiteStorageIconIn": "_cloudsearch_624_AppsDynamiteStorageIconIn",
        "AppsDynamiteStorageIconOut": "_cloudsearch_625_AppsDynamiteStorageIconOut",
        "ItemStatusIn": "_cloudsearch_626_ItemStatusIn",
        "ItemStatusOut": "_cloudsearch_627_ItemStatusOut",
        "GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn": "_cloudsearch_628_GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn",
        "GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut": "_cloudsearch_629_GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut",
        "CustomerIdIn": "_cloudsearch_630_CustomerIdIn",
        "CustomerIdOut": "_cloudsearch_631_CustomerIdOut",
        "AttributesIn": "_cloudsearch_632_AttributesIn",
        "AttributesOut": "_cloudsearch_633_AttributesOut",
        "PrefDeletedIn": "_cloudsearch_634_PrefDeletedIn",
        "PrefDeletedOut": "_cloudsearch_635_PrefDeletedOut",
        "PrivateMessageInfoIn": "_cloudsearch_636_PrivateMessageInfoIn",
        "PrivateMessageInfoOut": "_cloudsearch_637_PrivateMessageInfoOut",
        "ValueFilterIn": "_cloudsearch_638_ValueFilterIn",
        "ValueFilterOut": "_cloudsearch_639_ValueFilterOut",
        "LabelUpdateIn": "_cloudsearch_640_LabelUpdateIn",
        "LabelUpdateOut": "_cloudsearch_641_LabelUpdateOut",
        "AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn": "_cloudsearch_642_AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn",
        "AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut": "_cloudsearch_643_AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut",
        "VoicePhoneNumberIn": "_cloudsearch_644_VoicePhoneNumberIn",
        "VoicePhoneNumberOut": "_cloudsearch_645_VoicePhoneNumberOut",
        "AppsDynamiteSharedMessageIntegrationPayloadIn": "_cloudsearch_646_AppsDynamiteSharedMessageIntegrationPayloadIn",
        "AppsDynamiteSharedMessageIntegrationPayloadOut": "_cloudsearch_647_AppsDynamiteSharedMessageIntegrationPayloadOut",
        "AppsDynamiteStorageGridIn": "_cloudsearch_648_AppsDynamiteStorageGridIn",
        "AppsDynamiteStorageGridOut": "_cloudsearch_649_AppsDynamiteStorageGridOut",
        "AppsDynamiteSharedMessageComponentSearchInfoIn": "_cloudsearch_650_AppsDynamiteSharedMessageComponentSearchInfoIn",
        "AppsDynamiteSharedMessageComponentSearchInfoOut": "_cloudsearch_651_AppsDynamiteSharedMessageComponentSearchInfoOut",
        "GoogleChatV1ContextualAddOnMarkupCardIn": "_cloudsearch_652_GoogleChatV1ContextualAddOnMarkupCardIn",
        "GoogleChatV1ContextualAddOnMarkupCardOut": "_cloudsearch_653_GoogleChatV1ContextualAddOnMarkupCardOut",
        "DocumentInfoIn": "_cloudsearch_654_DocumentInfoIn",
        "DocumentInfoOut": "_cloudsearch_655_DocumentInfoOut",
        "DateTimePickerIn": "_cloudsearch_656_DateTimePickerIn",
        "DateTimePickerOut": "_cloudsearch_657_DateTimePickerOut",
        "DmIdIn": "_cloudsearch_658_DmIdIn",
        "DmIdOut": "_cloudsearch_659_DmIdOut",
        "UrlMetadataIn": "_cloudsearch_660_UrlMetadataIn",
        "UrlMetadataOut": "_cloudsearch_661_UrlMetadataOut",
        "CardActionIn": "_cloudsearch_662_CardActionIn",
        "CardActionOut": "_cloudsearch_663_CardActionOut",
        "HistoryRecordIn": "_cloudsearch_664_HistoryRecordIn",
        "HistoryRecordOut": "_cloudsearch_665_HistoryRecordOut",
        "CustomerSearchApplicationStatsIn": "_cloudsearch_666_CustomerSearchApplicationStatsIn",
        "CustomerSearchApplicationStatsOut": "_cloudsearch_667_CustomerSearchApplicationStatsOut",
        "ShareScopeIn": "_cloudsearch_668_ShareScopeIn",
        "ShareScopeOut": "_cloudsearch_669_ShareScopeOut",
        "StructuredResultIn": "_cloudsearch_670_StructuredResultIn",
        "StructuredResultOut": "_cloudsearch_671_StructuredResultOut",
        "YoutubeUserProtoIn": "_cloudsearch_672_YoutubeUserProtoIn",
        "YoutubeUserProtoOut": "_cloudsearch_673_YoutubeUserProtoOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn": "_cloudsearch_674_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut": "_cloudsearch_675_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut",
        "CallSettingsIn": "_cloudsearch_676_CallSettingsIn",
        "CallSettingsOut": "_cloudsearch_677_CallSettingsOut",
        "AppsDynamiteStorageCardSectionIn": "_cloudsearch_678_AppsDynamiteStorageCardSectionIn",
        "AppsDynamiteStorageCardSectionOut": "_cloudsearch_679_AppsDynamiteStorageCardSectionOut",
        "ItemThreadIn": "_cloudsearch_680_ItemThreadIn",
        "ItemThreadOut": "_cloudsearch_681_ItemThreadOut",
        "HostAppActionMarkupIn": "_cloudsearch_682_HostAppActionMarkupIn",
        "HostAppActionMarkupOut": "_cloudsearch_683_HostAppActionMarkupOut",
        "EventAnnotationIn": "_cloudsearch_684_EventAnnotationIn",
        "EventAnnotationOut": "_cloudsearch_685_EventAnnotationOut",
        "SocialCommonAttachmentAttachmentIn": "_cloudsearch_686_SocialCommonAttachmentAttachmentIn",
        "SocialCommonAttachmentAttachmentOut": "_cloudsearch_687_SocialCommonAttachmentAttachmentOut",
        "AppsDynamiteStorageImageComponentIn": "_cloudsearch_688_AppsDynamiteStorageImageComponentIn",
        "AppsDynamiteStorageImageComponentOut": "_cloudsearch_689_AppsDynamiteStorageImageComponentOut",
        "DoubleValuesIn": "_cloudsearch_690_DoubleValuesIn",
        "DoubleValuesOut": "_cloudsearch_691_DoubleValuesOut",
        "ContentReportSummaryIn": "_cloudsearch_692_ContentReportSummaryIn",
        "ContentReportSummaryOut": "_cloudsearch_693_ContentReportSummaryOut",
        "GoogleChatV1WidgetMarkupImageIn": "_cloudsearch_694_GoogleChatV1WidgetMarkupImageIn",
        "GoogleChatV1WidgetMarkupImageOut": "_cloudsearch_695_GoogleChatV1WidgetMarkupImageOut",
        "SuggestResponseIn": "_cloudsearch_696_SuggestResponseIn",
        "SuggestResponseOut": "_cloudsearch_697_SuggestResponseOut",
        "ResponseDebugInfoIn": "_cloudsearch_698_ResponseDebugInfoIn",
        "ResponseDebugInfoOut": "_cloudsearch_699_ResponseDebugInfoOut",
        "CustomerQueryStatsIn": "_cloudsearch_700_CustomerQueryStatsIn",
        "CustomerQueryStatsOut": "_cloudsearch_701_CustomerQueryStatsOut",
        "AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn": "_cloudsearch_702_AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut": "_cloudsearch_703_AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut",
        "AppsDynamiteStorageActionIn": "_cloudsearch_704_AppsDynamiteStorageActionIn",
        "AppsDynamiteStorageActionOut": "_cloudsearch_705_AppsDynamiteStorageActionOut",
        "UpdateToRecipientsIn": "_cloudsearch_706_UpdateToRecipientsIn",
        "UpdateToRecipientsOut": "_cloudsearch_707_UpdateToRecipientsOut",
        "TextFieldIn": "_cloudsearch_708_TextFieldIn",
        "TextFieldOut": "_cloudsearch_709_TextFieldOut",
        "CircleProtoIn": "_cloudsearch_710_CircleProtoIn",
        "CircleProtoOut": "_cloudsearch_711_CircleProtoOut",
        "DateOperatorOptionsIn": "_cloudsearch_712_DateOperatorOptionsIn",
        "DateOperatorOptionsOut": "_cloudsearch_713_DateOperatorOptionsOut",
        "AppsDynamiteStorageDecoratedTextIn": "_cloudsearch_714_AppsDynamiteStorageDecoratedTextIn",
        "AppsDynamiteStorageDecoratedTextOut": "_cloudsearch_715_AppsDynamiteStorageDecoratedTextOut",
        "EmailOwnerProtoIn": "_cloudsearch_716_EmailOwnerProtoIn",
        "EmailOwnerProtoOut": "_cloudsearch_717_EmailOwnerProtoOut",
        "AppsDynamiteSharedTasksMessageIntegrationPayloadIn": "_cloudsearch_718_AppsDynamiteSharedTasksMessageIntegrationPayloadIn",
        "AppsDynamiteSharedTasksMessageIntegrationPayloadOut": "_cloudsearch_719_AppsDynamiteSharedTasksMessageIntegrationPayloadOut",
        "RestrictItemIn": "_cloudsearch_720_RestrictItemIn",
        "RestrictItemOut": "_cloudsearch_721_RestrictItemOut",
        "ImapUidsReassignIn": "_cloudsearch_722_ImapUidsReassignIn",
        "ImapUidsReassignOut": "_cloudsearch_723_ImapUidsReassignOut",
        "DlpActionIn": "_cloudsearch_724_DlpActionIn",
        "DlpActionOut": "_cloudsearch_725_DlpActionOut",
        "TextOperatorOptionsIn": "_cloudsearch_726_TextOperatorOptionsIn",
        "TextOperatorOptionsOut": "_cloudsearch_727_TextOperatorOptionsOut",
        "ObjectOptionsIn": "_cloudsearch_728_ObjectOptionsIn",
        "ObjectOptionsOut": "_cloudsearch_729_ObjectOptionsOut",
        "AppsDynamiteStorageCardCardHeaderIn": "_cloudsearch_730_AppsDynamiteStorageCardCardHeaderIn",
        "AppsDynamiteStorageCardCardHeaderOut": "_cloudsearch_731_AppsDynamiteStorageCardCardHeaderOut",
        "RepositoryErrorIn": "_cloudsearch_732_RepositoryErrorIn",
        "RepositoryErrorOut": "_cloudsearch_733_RepositoryErrorOut",
        "DataLossPreventionMetadataIn": "_cloudsearch_734_DataLossPreventionMetadataIn",
        "DataLossPreventionMetadataOut": "_cloudsearch_735_DataLossPreventionMetadataOut",
        "ResultDisplayLineIn": "_cloudsearch_736_ResultDisplayLineIn",
        "ResultDisplayLineOut": "_cloudsearch_737_ResultDisplayLineOut",
        "CaribouAttributeValueIn": "_cloudsearch_738_CaribouAttributeValueIn",
        "CaribouAttributeValueOut": "_cloudsearch_739_CaribouAttributeValueOut",
        "WonderMessageMappingIn": "_cloudsearch_740_WonderMessageMappingIn",
        "WonderMessageMappingOut": "_cloudsearch_741_WonderMessageMappingOut",
        "SwitchWidgetIn": "_cloudsearch_742_SwitchWidgetIn",
        "SwitchWidgetOut": "_cloudsearch_743_SwitchWidgetOut",
        "EmailAddressIn": "_cloudsearch_744_EmailAddressIn",
        "EmailAddressOut": "_cloudsearch_745_EmailAddressOut",
        "TopicStateUpdateIn": "_cloudsearch_746_TopicStateUpdateIn",
        "TopicStateUpdateOut": "_cloudsearch_747_TopicStateUpdateOut",
        "ChatConserverDynamitePlaceholderMetadataEditMetadataIn": "_cloudsearch_748_ChatConserverDynamitePlaceholderMetadataEditMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataEditMetadataOut": "_cloudsearch_749_ChatConserverDynamitePlaceholderMetadataEditMetadataOut",
        "DriveMimeTypeRestrictIn": "_cloudsearch_750_DriveMimeTypeRestrictIn",
        "DriveMimeTypeRestrictOut": "_cloudsearch_751_DriveMimeTypeRestrictOut",
        "FacetBucketIn": "_cloudsearch_752_FacetBucketIn",
        "FacetBucketOut": "_cloudsearch_753_FacetBucketOut",
        "GroupDetailsUpdatedMetadataIn": "_cloudsearch_754_GroupDetailsUpdatedMetadataIn",
        "GroupDetailsUpdatedMetadataOut": "_cloudsearch_755_GroupDetailsUpdatedMetadataOut",
        "AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn": "_cloudsearch_756_AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn",
        "AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut": "_cloudsearch_757_AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut",
        "ResultDisplayMetadataIn": "_cloudsearch_758_ResultDisplayMetadataIn",
        "ResultDisplayMetadataOut": "_cloudsearch_759_ResultDisplayMetadataOut",
        "AppsDynamiteStorageMaterialIconIn": "_cloudsearch_760_AppsDynamiteStorageMaterialIconIn",
        "AppsDynamiteStorageMaterialIconOut": "_cloudsearch_761_AppsDynamiteStorageMaterialIconOut",
        "AutoCompleteIn": "_cloudsearch_762_AutoCompleteIn",
        "AutoCompleteOut": "_cloudsearch_763_AutoCompleteOut",
        "PresenterIn": "_cloudsearch_764_PresenterIn",
        "PresenterOut": "_cloudsearch_765_PresenterOut",
        "RbacRoleProtoIn": "_cloudsearch_766_RbacRoleProtoIn",
        "RbacRoleProtoOut": "_cloudsearch_767_RbacRoleProtoOut",
        "ZwiebackSessionProtoIn": "_cloudsearch_768_ZwiebackSessionProtoIn",
        "ZwiebackSessionProtoOut": "_cloudsearch_769_ZwiebackSessionProtoOut",
        "MembershipChangeEventIn": "_cloudsearch_770_MembershipChangeEventIn",
        "MembershipChangeEventOut": "_cloudsearch_771_MembershipChangeEventOut",
        "GetCustomerUserStatsResponseIn": "_cloudsearch_772_GetCustomerUserStatsResponseIn",
        "GetCustomerUserStatsResponseOut": "_cloudsearch_773_GetCustomerUserStatsResponseOut",
        "BotResponseIn": "_cloudsearch_774_BotResponseIn",
        "BotResponseOut": "_cloudsearch_775_BotResponseOut",
        "PrincipalProtoIn": "_cloudsearch_776_PrincipalProtoIn",
        "PrincipalProtoOut": "_cloudsearch_777_PrincipalProtoOut",
        "TrustedResourceUrlProtoIn": "_cloudsearch_778_TrustedResourceUrlProtoIn",
        "TrustedResourceUrlProtoOut": "_cloudsearch_779_TrustedResourceUrlProtoOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn": "_cloudsearch_780_AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut": "_cloudsearch_781_AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut",
        "CalendarClientActionMarkupIn": "_cloudsearch_782_CalendarClientActionMarkupIn",
        "CalendarClientActionMarkupOut": "_cloudsearch_783_CalendarClientActionMarkupOut",
        "PackagingServiceClientIn": "_cloudsearch_784_PackagingServiceClientIn",
        "PackagingServiceClientOut": "_cloudsearch_785_PackagingServiceClientOut",
        "TimestampOperatorOptionsIn": "_cloudsearch_786_TimestampOperatorOptionsIn",
        "TimestampOperatorOptionsOut": "_cloudsearch_787_TimestampOperatorOptionsOut",
        "GoogleChatV1WidgetMarkupTextParagraphIn": "_cloudsearch_788_GoogleChatV1WidgetMarkupTextParagraphIn",
        "GoogleChatV1WidgetMarkupTextParagraphOut": "_cloudsearch_789_GoogleChatV1WidgetMarkupTextParagraphOut",
        "RosterIdIn": "_cloudsearch_790_RosterIdIn",
        "RosterIdOut": "_cloudsearch_791_RosterIdOut",
        "AppsDynamiteSharedMessageInfoIn": "_cloudsearch_792_AppsDynamiteSharedMessageInfoIn",
        "AppsDynamiteSharedMessageInfoOut": "_cloudsearch_793_AppsDynamiteSharedMessageInfoOut",
        "ProvenanceIn": "_cloudsearch_794_ProvenanceIn",
        "ProvenanceOut": "_cloudsearch_795_ProvenanceOut",
        "GaiaUserProtoIn": "_cloudsearch_796_GaiaUserProtoIn",
        "GaiaUserProtoOut": "_cloudsearch_797_GaiaUserProtoOut",
        "OAuthConsumerProtoIn": "_cloudsearch_798_OAuthConsumerProtoIn",
        "OAuthConsumerProtoOut": "_cloudsearch_799_OAuthConsumerProtoOut",
        "MessageSetIn": "_cloudsearch_800_MessageSetIn",
        "MessageSetOut": "_cloudsearch_801_MessageSetOut",
        "AppsDynamiteSharedJustificationIn": "_cloudsearch_802_AppsDynamiteSharedJustificationIn",
        "AppsDynamiteSharedJustificationOut": "_cloudsearch_803_AppsDynamiteSharedJustificationOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn": "_cloudsearch_804_AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut": "_cloudsearch_805_AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut",
        "AppIdIn": "_cloudsearch_806_AppIdIn",
        "AppIdOut": "_cloudsearch_807_AppIdOut",
        "ResultDebugInfoIn": "_cloudsearch_808_ResultDebugInfoIn",
        "ResultDebugInfoOut": "_cloudsearch_809_ResultDebugInfoOut",
        "FormatMetadataIn": "_cloudsearch_810_FormatMetadataIn",
        "FormatMetadataOut": "_cloudsearch_811_FormatMetadataOut",
        "LabelRemovedIn": "_cloudsearch_812_LabelRemovedIn",
        "LabelRemovedOut": "_cloudsearch_813_LabelRemovedOut",
        "WhiteboardInfoIn": "_cloudsearch_814_WhiteboardInfoIn",
        "WhiteboardInfoOut": "_cloudsearch_815_WhiteboardInfoOut",
        "WrappedResourceKeyIn": "_cloudsearch_816_WrappedResourceKeyIn",
        "WrappedResourceKeyOut": "_cloudsearch_817_WrappedResourceKeyOut",
        "StructuredDataObjectIn": "_cloudsearch_818_StructuredDataObjectIn",
        "StructuredDataObjectOut": "_cloudsearch_819_StructuredDataObjectOut",
        "UpdateDataSourceRequestIn": "_cloudsearch_820_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_cloudsearch_821_UpdateDataSourceRequestOut",
        "SupportUrlsIn": "_cloudsearch_822_SupportUrlsIn",
        "SupportUrlsOut": "_cloudsearch_823_SupportUrlsOut",
        "AppsDynamiteSharedVideoReferenceIn": "_cloudsearch_824_AppsDynamiteSharedVideoReferenceIn",
        "AppsDynamiteSharedVideoReferenceOut": "_cloudsearch_825_AppsDynamiteSharedVideoReferenceOut",
        "UploadMetadataIn": "_cloudsearch_826_UploadMetadataIn",
        "UploadMetadataOut": "_cloudsearch_827_UploadMetadataOut",
        "TriggersIn": "_cloudsearch_828_TriggersIn",
        "TriggersOut": "_cloudsearch_829_TriggersOut",
        "GroupLinkSharingModificationEventIn": "_cloudsearch_830_GroupLinkSharingModificationEventIn",
        "GroupLinkSharingModificationEventOut": "_cloudsearch_831_GroupLinkSharingModificationEventOut",
        "SearchApplicationUserStatsIn": "_cloudsearch_832_SearchApplicationUserStatsIn",
        "SearchApplicationUserStatsOut": "_cloudsearch_833_SearchApplicationUserStatsOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn": "_cloudsearch_834_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut": "_cloudsearch_835_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut",
        "ImapsyncFolderAttributeFolderMessageFlagsIn": "_cloudsearch_836_ImapsyncFolderAttributeFolderMessageFlagsIn",
        "ImapsyncFolderAttributeFolderMessageFlagsOut": "_cloudsearch_837_ImapsyncFolderAttributeFolderMessageFlagsOut",
        "LdapUserProtoIn": "_cloudsearch_838_LdapUserProtoIn",
        "LdapUserProtoOut": "_cloudsearch_839_LdapUserProtoOut",
        "PersonalLabelTagIn": "_cloudsearch_840_PersonalLabelTagIn",
        "PersonalLabelTagOut": "_cloudsearch_841_PersonalLabelTagOut",
        "RpcOptionsIn": "_cloudsearch_842_RpcOptionsIn",
        "RpcOptionsOut": "_cloudsearch_843_RpcOptionsOut",
        "ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn": "_cloudsearch_844_ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut": "_cloudsearch_845_ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut",
        "RecordingEventIn": "_cloudsearch_846_RecordingEventIn",
        "RecordingEventOut": "_cloudsearch_847_RecordingEventOut",
        "PhoneAccessIn": "_cloudsearch_848_PhoneAccessIn",
        "PhoneAccessOut": "_cloudsearch_849_PhoneAccessOut",
        "ChatConserverDynamitePlaceholderMetadataTasksMetadataIn": "_cloudsearch_850_ChatConserverDynamitePlaceholderMetadataTasksMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataTasksMetadataOut": "_cloudsearch_851_ChatConserverDynamitePlaceholderMetadataTasksMetadataOut",
        "LabelCreatedIn": "_cloudsearch_852_LabelCreatedIn",
        "LabelCreatedOut": "_cloudsearch_853_LabelCreatedOut",
        "AppsDynamiteSharedChatItemGroupInfoIn": "_cloudsearch_854_AppsDynamiteSharedChatItemGroupInfoIn",
        "AppsDynamiteSharedChatItemGroupInfoOut": "_cloudsearch_855_AppsDynamiteSharedChatItemGroupInfoOut",
        "AppsDynamiteStorageSuggestionsSuggestionItemIn": "_cloudsearch_856_AppsDynamiteStorageSuggestionsSuggestionItemIn",
        "AppsDynamiteStorageSuggestionsSuggestionItemOut": "_cloudsearch_857_AppsDynamiteStorageSuggestionsSuggestionItemOut",
        "FieldViolationIn": "_cloudsearch_858_FieldViolationIn",
        "FieldViolationOut": "_cloudsearch_859_FieldViolationOut",
        "NameIn": "_cloudsearch_860_NameIn",
        "NameOut": "_cloudsearch_861_NameOut",
        "UserMentionDataIn": "_cloudsearch_862_UserMentionDataIn",
        "UserMentionDataOut": "_cloudsearch_863_UserMentionDataOut",
        "ItemMetadataIn": "_cloudsearch_864_ItemMetadataIn",
        "ItemMetadataOut": "_cloudsearch_865_ItemMetadataOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn": "_cloudsearch_866_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut": "_cloudsearch_867_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut",
        "DebugOptionsIn": "_cloudsearch_868_DebugOptionsIn",
        "DebugOptionsOut": "_cloudsearch_869_DebugOptionsOut",
        "AppsDynamiteV1ApiCompatV1ActionIn": "_cloudsearch_870_AppsDynamiteV1ApiCompatV1ActionIn",
        "AppsDynamiteV1ApiCompatV1ActionOut": "_cloudsearch_871_AppsDynamiteV1ApiCompatV1ActionOut",
        "QuerySourceIn": "_cloudsearch_872_QuerySourceIn",
        "QuerySourceOut": "_cloudsearch_873_QuerySourceOut",
        "FuseboxPrefUpdatePreStateIn": "_cloudsearch_874_FuseboxPrefUpdatePreStateIn",
        "FuseboxPrefUpdatePreStateOut": "_cloudsearch_875_FuseboxPrefUpdatePreStateOut",
        "AppsDynamiteSharedChatItemActivityInfoIn": "_cloudsearch_876_AppsDynamiteSharedChatItemActivityInfoIn",
        "AppsDynamiteSharedChatItemActivityInfoOut": "_cloudsearch_877_AppsDynamiteSharedChatItemActivityInfoOut",
        "AppsDynamiteSharedOrganizationInfoConsumerInfoIn": "_cloudsearch_878_AppsDynamiteSharedOrganizationInfoConsumerInfoIn",
        "AppsDynamiteSharedOrganizationInfoConsumerInfoOut": "_cloudsearch_879_AppsDynamiteSharedOrganizationInfoConsumerInfoOut",
        "FacetOptionsIn": "_cloudsearch_880_FacetOptionsIn",
        "FacetOptionsOut": "_cloudsearch_881_FacetOptionsOut",
        "GoogleDocsMetadataIn": "_cloudsearch_882_GoogleDocsMetadataIn",
        "GoogleDocsMetadataOut": "_cloudsearch_883_GoogleDocsMetadataOut",
        "HashtagDataIn": "_cloudsearch_884_HashtagDataIn",
        "HashtagDataOut": "_cloudsearch_885_HashtagDataOut",
        "AutoCompleteItemIn": "_cloudsearch_886_AutoCompleteItemIn",
        "AutoCompleteItemOut": "_cloudsearch_887_AutoCompleteItemOut",
        "SearchResultIn": "_cloudsearch_888_SearchResultIn",
        "SearchResultOut": "_cloudsearch_889_SearchResultOut",
        "ObjectDefinitionIn": "_cloudsearch_890_ObjectDefinitionIn",
        "ObjectDefinitionOut": "_cloudsearch_891_ObjectDefinitionOut",
        "LabelDeletedIn": "_cloudsearch_892_LabelDeletedIn",
        "LabelDeletedOut": "_cloudsearch_893_LabelDeletedOut",
        "GoogleChatV1ContextualAddOnMarkupCardSectionIn": "_cloudsearch_894_GoogleChatV1ContextualAddOnMarkupCardSectionIn",
        "GoogleChatV1ContextualAddOnMarkupCardSectionOut": "_cloudsearch_895_GoogleChatV1ContextualAddOnMarkupCardSectionOut",
        "ToolbarIn": "_cloudsearch_896_ToolbarIn",
        "ToolbarOut": "_cloudsearch_897_ToolbarOut",
        "DlpScanSummaryIn": "_cloudsearch_898_DlpScanSummaryIn",
        "DlpScanSummaryOut": "_cloudsearch_899_DlpScanSummaryOut",
        "MessageIn": "_cloudsearch_900_MessageIn",
        "MessageOut": "_cloudsearch_901_MessageOut",
        "AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn": "_cloudsearch_902_AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut": "_cloudsearch_903_AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut",
        "AppsDynamiteSharedSegmentedMembershipCountsIn": "_cloudsearch_904_AppsDynamiteSharedSegmentedMembershipCountsIn",
        "AppsDynamiteSharedSegmentedMembershipCountsOut": "_cloudsearch_905_AppsDynamiteSharedSegmentedMembershipCountsOut",
        "DeliveryMediumIn": "_cloudsearch_906_DeliveryMediumIn",
        "DeliveryMediumOut": "_cloudsearch_907_DeliveryMediumOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn": "_cloudsearch_908_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut": "_cloudsearch_909_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut",
        "AckInfoIn": "_cloudsearch_910_AckInfoIn",
        "AckInfoOut": "_cloudsearch_911_AckInfoOut",
        "SimpleSecretLabelProtoIn": "_cloudsearch_912_SimpleSecretLabelProtoIn",
        "SimpleSecretLabelProtoOut": "_cloudsearch_913_SimpleSecretLabelProtoOut",
        "PropertyDefinitionIn": "_cloudsearch_914_PropertyDefinitionIn",
        "PropertyDefinitionOut": "_cloudsearch_915_PropertyDefinitionOut",
        "CustomerSettingsIn": "_cloudsearch_916_CustomerSettingsIn",
        "CustomerSettingsOut": "_cloudsearch_917_CustomerSettingsOut",
        "EmbedClientItemIn": "_cloudsearch_918_EmbedClientItemIn",
        "EmbedClientItemOut": "_cloudsearch_919_EmbedClientItemOut",
        "CheckAccessResponseIn": "_cloudsearch_920_CheckAccessResponseIn",
        "CheckAccessResponseOut": "_cloudsearch_921_CheckAccessResponseOut",
        "BroadcastAccessIn": "_cloudsearch_922_BroadcastAccessIn",
        "BroadcastAccessOut": "_cloudsearch_923_BroadcastAccessOut",
        "ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn": "_cloudsearch_924_ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut": "_cloudsearch_925_ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut",
        "AppsDynamiteStorageOpenLinkIn": "_cloudsearch_926_AppsDynamiteStorageOpenLinkIn",
        "AppsDynamiteStorageOpenLinkOut": "_cloudsearch_927_AppsDynamiteStorageOpenLinkOut",
        "ListUnmappedIdentitiesResponseIn": "_cloudsearch_928_ListUnmappedIdentitiesResponseIn",
        "ListUnmappedIdentitiesResponseOut": "_cloudsearch_929_ListUnmappedIdentitiesResponseOut",
        "OperationIn": "_cloudsearch_930_OperationIn",
        "OperationOut": "_cloudsearch_931_OperationOut",
        "MessageDeletedIn": "_cloudsearch_932_MessageDeletedIn",
        "MessageDeletedOut": "_cloudsearch_933_MessageDeletedOut",
        "PollItemsRequestIn": "_cloudsearch_934_PollItemsRequestIn",
        "PollItemsRequestOut": "_cloudsearch_935_PollItemsRequestOut",
        "ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn": "_cloudsearch_936_ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut": "_cloudsearch_937_ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut",
        "AttributeIn": "_cloudsearch_938_AttributeIn",
        "AttributeOut": "_cloudsearch_939_AttributeOut",
        "ListQuerySourcesResponseIn": "_cloudsearch_940_ListQuerySourcesResponseIn",
        "ListQuerySourcesResponseOut": "_cloudsearch_941_ListQuerySourcesResponseOut",
        "DoublePropertyOptionsIn": "_cloudsearch_942_DoublePropertyOptionsIn",
        "DoublePropertyOptionsOut": "_cloudsearch_943_DoublePropertyOptionsOut",
        "DeleteQueueItemsRequestIn": "_cloudsearch_944_DeleteQueueItemsRequestIn",
        "DeleteQueueItemsRequestOut": "_cloudsearch_945_DeleteQueueItemsRequestOut",
        "AddonComposeUiActionMarkupIn": "_cloudsearch_946_AddonComposeUiActionMarkupIn",
        "AddonComposeUiActionMarkupOut": "_cloudsearch_947_AddonComposeUiActionMarkupOut",
        "ErrorMessageIn": "_cloudsearch_948_ErrorMessageIn",
        "ErrorMessageOut": "_cloudsearch_949_ErrorMessageOut",
        "FreshnessOptionsIn": "_cloudsearch_950_FreshnessOptionsIn",
        "FreshnessOptionsOut": "_cloudsearch_951_FreshnessOptionsOut",
        "UserIn": "_cloudsearch_952_UserIn",
        "UserOut": "_cloudsearch_953_UserOut",
        "MatchInfoIn": "_cloudsearch_954_MatchInfoIn",
        "MatchInfoOut": "_cloudsearch_955_MatchInfoOut",
        "ChatContentExtensionIn": "_cloudsearch_956_ChatContentExtensionIn",
        "ChatContentExtensionOut": "_cloudsearch_957_ChatContentExtensionOut",
        "ImapSyncDeleteIn": "_cloudsearch_958_ImapSyncDeleteIn",
        "ImapSyncDeleteOut": "_cloudsearch_959_ImapSyncDeleteOut",
        "PhotoIn": "_cloudsearch_960_PhotoIn",
        "PhotoOut": "_cloudsearch_961_PhotoOut",
        "ClientContextIn": "_cloudsearch_962_ClientContextIn",
        "ClientContextOut": "_cloudsearch_963_ClientContextOut",
        "UploadItemRefIn": "_cloudsearch_964_UploadItemRefIn",
        "UploadItemRefOut": "_cloudsearch_965_UploadItemRefOut",
        "CoActivityIn": "_cloudsearch_966_CoActivityIn",
        "CoActivityOut": "_cloudsearch_967_CoActivityOut",
        "SelectionItemIn": "_cloudsearch_968_SelectionItemIn",
        "SelectionItemOut": "_cloudsearch_969_SelectionItemOut",
        "InviteeInfoIn": "_cloudsearch_970_InviteeInfoIn",
        "InviteeInfoOut": "_cloudsearch_971_InviteeInfoOut",
        "DataSourceIndexStatsIn": "_cloudsearch_972_DataSourceIndexStatsIn",
        "DataSourceIndexStatsOut": "_cloudsearch_973_DataSourceIndexStatsOut",
        "AppsDynamiteStorageCardCardActionIn": "_cloudsearch_974_AppsDynamiteStorageCardCardActionIn",
        "AppsDynamiteStorageCardCardActionOut": "_cloudsearch_975_AppsDynamiteStorageCardCardActionOut",
        "GoogleChatV1WidgetMarkupIn": "_cloudsearch_976_GoogleChatV1WidgetMarkupIn",
        "GoogleChatV1WidgetMarkupOut": "_cloudsearch_977_GoogleChatV1WidgetMarkupOut",
        "MetalineIn": "_cloudsearch_978_MetalineIn",
        "MetalineOut": "_cloudsearch_979_MetalineOut",
        "SpellResultIn": "_cloudsearch_980_SpellResultIn",
        "SpellResultOut": "_cloudsearch_981_SpellResultOut",
        "DoubleOperatorOptionsIn": "_cloudsearch_982_DoubleOperatorOptionsIn",
        "DoubleOperatorOptionsOut": "_cloudsearch_983_DoubleOperatorOptionsOut",
        "GetCustomerSearchApplicationStatsResponseIn": "_cloudsearch_984_GetCustomerSearchApplicationStatsResponseIn",
        "GetCustomerSearchApplicationStatsResponseOut": "_cloudsearch_985_GetCustomerSearchApplicationStatsResponseOut",
        "AppsDynamiteSharedAssistantFeedbackContextIn": "_cloudsearch_986_AppsDynamiteSharedAssistantFeedbackContextIn",
        "AppsDynamiteSharedAssistantFeedbackContextOut": "_cloudsearch_987_AppsDynamiteSharedAssistantFeedbackContextOut",
        "IncomingWebhookChangedMetadataIn": "_cloudsearch_988_IncomingWebhookChangedMetadataIn",
        "IncomingWebhookChangedMetadataOut": "_cloudsearch_989_IncomingWebhookChangedMetadataOut",
        "FilterOptionsIn": "_cloudsearch_990_FilterOptionsIn",
        "FilterOptionsOut": "_cloudsearch_991_FilterOptionsOut",
        "ChatConserverDynamitePlaceholderMetadataIn": "_cloudsearch_992_ChatConserverDynamitePlaceholderMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataOut": "_cloudsearch_993_ChatConserverDynamitePlaceholderMetadataOut",
        "AppsDynamiteStorageSelectionInputIn": "_cloudsearch_994_AppsDynamiteStorageSelectionInputIn",
        "AppsDynamiteStorageSelectionInputOut": "_cloudsearch_995_AppsDynamiteStorageSelectionInputOut",
        "ResetSearchApplicationRequestIn": "_cloudsearch_996_ResetSearchApplicationRequestIn",
        "ResetSearchApplicationRequestOut": "_cloudsearch_997_ResetSearchApplicationRequestOut",
        "DatePropertyOptionsIn": "_cloudsearch_998_DatePropertyOptionsIn",
        "DatePropertyOptionsOut": "_cloudsearch_999_DatePropertyOptionsOut",
        "YouTubeLiveBroadcastEventIn": "_cloudsearch_1000_YouTubeLiveBroadcastEventIn",
        "YouTubeLiveBroadcastEventOut": "_cloudsearch_1001_YouTubeLiveBroadcastEventOut",
        "AppsDynamiteSharedAssistantAnnotationDataIn": "_cloudsearch_1002_AppsDynamiteSharedAssistantAnnotationDataIn",
        "AppsDynamiteSharedAssistantAnnotationDataOut": "_cloudsearch_1003_AppsDynamiteSharedAssistantAnnotationDataOut",
        "ContentReportIn": "_cloudsearch_1004_ContentReportIn",
        "ContentReportOut": "_cloudsearch_1005_ContentReportOut",
        "SimpleSecretHolderProtoIn": "_cloudsearch_1006_SimpleSecretHolderProtoIn",
        "SimpleSecretHolderProtoOut": "_cloudsearch_1007_SimpleSecretHolderProtoOut",
        "AllAuthenticatedUsersProtoIn": "_cloudsearch_1008_AllAuthenticatedUsersProtoIn",
        "AllAuthenticatedUsersProtoOut": "_cloudsearch_1009_AllAuthenticatedUsersProtoOut",
        "UpdateBccRecipientsIn": "_cloudsearch_1010_UpdateBccRecipientsIn",
        "UpdateBccRecipientsOut": "_cloudsearch_1011_UpdateBccRecipientsOut",
        "AppsDynamiteSharedOrganizationInfoCustomerInfoIn": "_cloudsearch_1012_AppsDynamiteSharedOrganizationInfoCustomerInfoIn",
        "AppsDynamiteSharedOrganizationInfoCustomerInfoOut": "_cloudsearch_1013_AppsDynamiteSharedOrganizationInfoCustomerInfoOut",
        "CardIn": "_cloudsearch_1014_CardIn",
        "CardOut": "_cloudsearch_1015_CardOut",
        "HangoutVideoEventMetadataIn": "_cloudsearch_1016_HangoutVideoEventMetadataIn",
        "HangoutVideoEventMetadataOut": "_cloudsearch_1017_HangoutVideoEventMetadataOut",
        "LabelAddedIn": "_cloudsearch_1018_LabelAddedIn",
        "LabelAddedOut": "_cloudsearch_1019_LabelAddedOut",
        "AppsDynamiteSharedActivityFeedAnnotationDataIn": "_cloudsearch_1020_AppsDynamiteSharedActivityFeedAnnotationDataIn",
        "AppsDynamiteSharedActivityFeedAnnotationDataOut": "_cloudsearch_1021_AppsDynamiteSharedActivityFeedAnnotationDataOut",
        "FuseboxItemIn": "_cloudsearch_1022_FuseboxItemIn",
        "FuseboxItemOut": "_cloudsearch_1023_FuseboxItemOut",
        "CommunalLabelTagIn": "_cloudsearch_1024_CommunalLabelTagIn",
        "CommunalLabelTagOut": "_cloudsearch_1025_CommunalLabelTagOut",
        "AppsDynamiteStorageColumnsColumnIn": "_cloudsearch_1026_AppsDynamiteStorageColumnsColumnIn",
        "AppsDynamiteStorageColumnsColumnOut": "_cloudsearch_1027_AppsDynamiteStorageColumnsColumnOut",
        "ChatClientActionMarkupIn": "_cloudsearch_1028_ChatClientActionMarkupIn",
        "ChatClientActionMarkupOut": "_cloudsearch_1029_ChatClientActionMarkupOut",
        "EnumPropertyOptionsIn": "_cloudsearch_1030_EnumPropertyOptionsIn",
        "EnumPropertyOptionsOut": "_cloudsearch_1031_EnumPropertyOptionsOut",
        "ErrorInfoIn": "_cloudsearch_1032_ErrorInfoIn",
        "ErrorInfoOut": "_cloudsearch_1033_ErrorInfoOut",
        "RecordingSessionInfoIn": "_cloudsearch_1034_RecordingSessionInfoIn",
        "RecordingSessionInfoOut": "_cloudsearch_1035_RecordingSessionInfoOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn": "_cloudsearch_1036_AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut": "_cloudsearch_1037_AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut",
        "RosterIn": "_cloudsearch_1038_RosterIn",
        "RosterOut": "_cloudsearch_1039_RosterOut",
        "SpaceIdIn": "_cloudsearch_1040_SpaceIdIn",
        "SpaceIdOut": "_cloudsearch_1041_SpaceIdOut",
        "AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn": "_cloudsearch_1042_AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn",
        "AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut": "_cloudsearch_1043_AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut",
        "AppsDynamiteStorageSelectionInputSelectionItemIn": "_cloudsearch_1044_AppsDynamiteStorageSelectionInputSelectionItemIn",
        "AppsDynamiteStorageSelectionInputSelectionItemOut": "_cloudsearch_1045_AppsDynamiteStorageSelectionInputSelectionItemOut",
        "SourceScoringConfigIn": "_cloudsearch_1046_SourceScoringConfigIn",
        "SourceScoringConfigOut": "_cloudsearch_1047_SourceScoringConfigOut",
        "DataSourceIn": "_cloudsearch_1048_DataSourceIn",
        "DataSourceOut": "_cloudsearch_1049_DataSourceOut",
        "TextButtonIn": "_cloudsearch_1050_TextButtonIn",
        "TextButtonOut": "_cloudsearch_1051_TextButtonOut",
        "ListDataSourceResponseIn": "_cloudsearch_1052_ListDataSourceResponseIn",
        "ListDataSourceResponseOut": "_cloudsearch_1053_ListDataSourceResponseOut",
        "QuerySuggestionIn": "_cloudsearch_1054_QuerySuggestionIn",
        "QuerySuggestionOut": "_cloudsearch_1055_QuerySuggestionOut",
        "ChatConserverMessageContentIn": "_cloudsearch_1056_ChatConserverMessageContentIn",
        "ChatConserverMessageContentOut": "_cloudsearch_1057_ChatConserverMessageContentOut",
        "AppsDynamiteSharedAppProfileIn": "_cloudsearch_1058_AppsDynamiteSharedAppProfileIn",
        "AppsDynamiteSharedAppProfileOut": "_cloudsearch_1059_AppsDynamiteSharedAppProfileOut",
        "AppsDynamiteSharedAvatarInfoIn": "_cloudsearch_1060_AppsDynamiteSharedAvatarInfoIn",
        "AppsDynamiteSharedAvatarInfoOut": "_cloudsearch_1061_AppsDynamiteSharedAvatarInfoOut",
        "AppsDynamiteSharedCustomEmojiIn": "_cloudsearch_1062_AppsDynamiteSharedCustomEmojiIn",
        "AppsDynamiteSharedCustomEmojiOut": "_cloudsearch_1063_AppsDynamiteSharedCustomEmojiOut",
        "AppsDynamiteStorageTextInputIn": "_cloudsearch_1064_AppsDynamiteStorageTextInputIn",
        "AppsDynamiteStorageTextInputOut": "_cloudsearch_1065_AppsDynamiteStorageTextInputOut",
        "MessageIdIn": "_cloudsearch_1066_MessageIdIn",
        "MessageIdOut": "_cloudsearch_1067_MessageIdOut",
        "AppsDynamiteStorageOpenLinkAppUriIntentIn": "_cloudsearch_1068_AppsDynamiteStorageOpenLinkAppUriIntentIn",
        "AppsDynamiteStorageOpenLinkAppUriIntentOut": "_cloudsearch_1069_AppsDynamiteStorageOpenLinkAppUriIntentOut",
        "AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn": "_cloudsearch_1070_AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut": "_cloudsearch_1071_AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut",
        "EventProtoIn": "_cloudsearch_1072_EventProtoIn",
        "EventProtoOut": "_cloudsearch_1073_EventProtoOut",
        "AffectedMembershipIn": "_cloudsearch_1074_AffectedMembershipIn",
        "AffectedMembershipOut": "_cloudsearch_1075_AffectedMembershipOut",
        "HtmlPropertyOptionsIn": "_cloudsearch_1076_HtmlPropertyOptionsIn",
        "HtmlPropertyOptionsOut": "_cloudsearch_1077_HtmlPropertyOptionsOut",
        "ObjectDisplayOptionsIn": "_cloudsearch_1078_ObjectDisplayOptionsIn",
        "ObjectDisplayOptionsOut": "_cloudsearch_1079_ObjectDisplayOptionsOut",
        "ImageCropStyleIn": "_cloudsearch_1080_ImageCropStyleIn",
        "ImageCropStyleOut": "_cloudsearch_1081_ImageCropStyleOut",
        "SectionIn": "_cloudsearch_1082_SectionIn",
        "SectionOut": "_cloudsearch_1083_SectionOut",
        "PrincipalIn": "_cloudsearch_1084_PrincipalIn",
        "PrincipalOut": "_cloudsearch_1085_PrincipalOut",
        "ReadReceiptsSettingsUpdatedMetadataIn": "_cloudsearch_1086_ReadReceiptsSettingsUpdatedMetadataIn",
        "ReadReceiptsSettingsUpdatedMetadataOut": "_cloudsearch_1087_ReadReceiptsSettingsUpdatedMetadataOut",
        "SessionContextIn": "_cloudsearch_1088_SessionContextIn",
        "SessionContextOut": "_cloudsearch_1089_SessionContextOut",
        "AclFixRequestIn": "_cloudsearch_1090_AclFixRequestIn",
        "AclFixRequestOut": "_cloudsearch_1091_AclFixRequestOut",
        "AppsDynamiteStorageActionActionParameterIn": "_cloudsearch_1092_AppsDynamiteStorageActionActionParameterIn",
        "AppsDynamiteStorageActionActionParameterOut": "_cloudsearch_1093_AppsDynamiteStorageActionActionParameterOut",
        "NamedPropertyIn": "_cloudsearch_1094_NamedPropertyIn",
        "NamedPropertyOut": "_cloudsearch_1095_NamedPropertyOut",
        "UniversalPhoneAccessIn": "_cloudsearch_1096_UniversalPhoneAccessIn",
        "UniversalPhoneAccessOut": "_cloudsearch_1097_UniversalPhoneAccessOut",
        "AppsDynamiteStorageImageIn": "_cloudsearch_1098_AppsDynamiteStorageImageIn",
        "AppsDynamiteStorageImageOut": "_cloudsearch_1099_AppsDynamiteStorageImageOut",
        "RequestFileScopeIn": "_cloudsearch_1100_RequestFileScopeIn",
        "RequestFileScopeOut": "_cloudsearch_1101_RequestFileScopeOut",
        "ThreadUpdateIn": "_cloudsearch_1102_ThreadUpdateIn",
        "ThreadUpdateOut": "_cloudsearch_1103_ThreadUpdateOut",
        "SourceCrowdingConfigIn": "_cloudsearch_1104_SourceCrowdingConfigIn",
        "SourceCrowdingConfigOut": "_cloudsearch_1105_SourceCrowdingConfigOut",
        "SettingsIn": "_cloudsearch_1106_SettingsIn",
        "SettingsOut": "_cloudsearch_1107_SettingsOut",
        "ImageKeyValueIn": "_cloudsearch_1108_ImageKeyValueIn",
        "ImageKeyValueOut": "_cloudsearch_1109_ImageKeyValueOut",
        "RoomUpdatedMetadataIn": "_cloudsearch_1110_RoomUpdatedMetadataIn",
        "RoomUpdatedMetadataOut": "_cloudsearch_1111_RoomUpdatedMetadataOut",
        "UpdateSubjectIn": "_cloudsearch_1112_UpdateSubjectIn",
        "UpdateSubjectOut": "_cloudsearch_1113_UpdateSubjectOut",
        "TimestampValuesIn": "_cloudsearch_1114_TimestampValuesIn",
        "TimestampValuesOut": "_cloudsearch_1115_TimestampValuesOut",
        "InviteAcceptedEventIn": "_cloudsearch_1116_InviteAcceptedEventIn",
        "InviteAcceptedEventOut": "_cloudsearch_1117_InviteAcceptedEventOut",
        "AppsDynamiteSharedPhoneNumberIn": "_cloudsearch_1118_AppsDynamiteSharedPhoneNumberIn",
        "AppsDynamiteSharedPhoneNumberOut": "_cloudsearch_1119_AppsDynamiteSharedPhoneNumberOut",
        "IntegrationConfigUpdatedMetadataIn": "_cloudsearch_1120_IntegrationConfigUpdatedMetadataIn",
        "IntegrationConfigUpdatedMetadataOut": "_cloudsearch_1121_IntegrationConfigUpdatedMetadataOut",
        "SquareProtoIn": "_cloudsearch_1122_SquareProtoIn",
        "SquareProtoOut": "_cloudsearch_1123_SquareProtoOut",
        "BroadcastSessionInfoIn": "_cloudsearch_1124_BroadcastSessionInfoIn",
        "BroadcastSessionInfoOut": "_cloudsearch_1125_BroadcastSessionInfoOut",
        "SuggestRequestIn": "_cloudsearch_1126_SuggestRequestIn",
        "SuggestRequestOut": "_cloudsearch_1127_SuggestRequestOut",
        "RoomRenameMetadataIn": "_cloudsearch_1128_RoomRenameMetadataIn",
        "RoomRenameMetadataOut": "_cloudsearch_1129_RoomRenameMetadataOut",
        "ActionParameterIn": "_cloudsearch_1130_ActionParameterIn",
        "ActionParameterOut": "_cloudsearch_1131_ActionParameterOut",
        "GoogleChatV1WidgetMarkupOnClickIn": "_cloudsearch_1132_GoogleChatV1WidgetMarkupOnClickIn",
        "GoogleChatV1WidgetMarkupOnClickOut": "_cloudsearch_1133_GoogleChatV1WidgetMarkupOnClickOut",
        "RequiredMessageFeaturesMetadataIn": "_cloudsearch_1134_RequiredMessageFeaturesMetadataIn",
        "RequiredMessageFeaturesMetadataOut": "_cloudsearch_1135_RequiredMessageFeaturesMetadataOut",
        "DataSourceRestrictionIn": "_cloudsearch_1136_DataSourceRestrictionIn",
        "DataSourceRestrictionOut": "_cloudsearch_1137_DataSourceRestrictionOut",
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn": "_cloudsearch_1138_ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut": "_cloudsearch_1139_ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut",
        "LegacyUploadMetadataIn": "_cloudsearch_1140_LegacyUploadMetadataIn",
        "LegacyUploadMetadataOut": "_cloudsearch_1141_LegacyUploadMetadataOut",
        "AppsDynamiteStorageWidgetIn": "_cloudsearch_1142_AppsDynamiteStorageWidgetIn",
        "AppsDynamiteStorageWidgetOut": "_cloudsearch_1143_AppsDynamiteStorageWidgetOut",
        "PersonIn": "_cloudsearch_1144_PersonIn",
        "PersonOut": "_cloudsearch_1145_PersonOut",
        "AppsDynamiteSharedBackendUploadMetadataIn": "_cloudsearch_1146_AppsDynamiteSharedBackendUploadMetadataIn",
        "AppsDynamiteSharedBackendUploadMetadataOut": "_cloudsearch_1147_AppsDynamiteSharedBackendUploadMetadataOut",
        "AppsDynamiteSharedRetentionSettingsIn": "_cloudsearch_1148_AppsDynamiteSharedRetentionSettingsIn",
        "AppsDynamiteSharedRetentionSettingsOut": "_cloudsearch_1149_AppsDynamiteSharedRetentionSettingsOut",
        "CustomerSessionStatsIn": "_cloudsearch_1150_CustomerSessionStatsIn",
        "CustomerSessionStatsOut": "_cloudsearch_1151_CustomerSessionStatsOut",
        "WonderCardDeleteIn": "_cloudsearch_1152_WonderCardDeleteIn",
        "WonderCardDeleteOut": "_cloudsearch_1153_WonderCardDeleteOut",
        "SearchRequestIn": "_cloudsearch_1154_SearchRequestIn",
        "SearchRequestOut": "_cloudsearch_1155_SearchRequestOut",
        "InsertContentIn": "_cloudsearch_1156_InsertContentIn",
        "InsertContentOut": "_cloudsearch_1157_InsertContentOut",
        "AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn": "_cloudsearch_1158_AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn",
        "AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut": "_cloudsearch_1159_AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut",
        "GatewaySipAccessIn": "_cloudsearch_1160_GatewaySipAccessIn",
        "GatewaySipAccessOut": "_cloudsearch_1161_GatewaySipAccessOut",
        "PaygateInfoIn": "_cloudsearch_1162_PaygateInfoIn",
        "PaygateInfoOut": "_cloudsearch_1163_PaygateInfoOut",
        "AppsDynamiteV1ApiCompatV1FieldIn": "_cloudsearch_1164_AppsDynamiteV1ApiCompatV1FieldIn",
        "AppsDynamiteV1ApiCompatV1FieldOut": "_cloudsearch_1165_AppsDynamiteV1ApiCompatV1FieldOut",
        "AppsDynamiteSharedDlpMetricsMetadataIn": "_cloudsearch_1166_AppsDynamiteSharedDlpMetricsMetadataIn",
        "AppsDynamiteSharedDlpMetricsMetadataOut": "_cloudsearch_1167_AppsDynamiteSharedDlpMetricsMetadataOut",
        "FilterUpdateIn": "_cloudsearch_1168_FilterUpdateIn",
        "FilterUpdateOut": "_cloudsearch_1169_FilterUpdateOut",
        "IntegrationConfigMutationIn": "_cloudsearch_1170_IntegrationConfigMutationIn",
        "IntegrationConfigMutationOut": "_cloudsearch_1171_IntegrationConfigMutationOut",
        "ProcessingErrorIn": "_cloudsearch_1172_ProcessingErrorIn",
        "ProcessingErrorOut": "_cloudsearch_1173_ProcessingErrorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["HistoryIn"] = t.struct(
        {"record": t.array(t.proxy(renames["HistoryRecordIn"]))}
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "record": t.array(t.proxy(renames["HistoryRecordOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
    types["AclFixStatusIn"] = t.struct(
        {
            "fixableEmailAddress": t.array(t.string()).optional(),
            "fixability": t.string(),
            "outOfDomainWarningEmailAddress": t.array(t.string()).optional(),
        }
    ).named(renames["AclFixStatusIn"])
    types["AclFixStatusOut"] = t.struct(
        {
            "fixableEmailAddress": t.array(t.string()).optional(),
            "fixability": t.string(),
            "outOfDomainWarningEmailAddress": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclFixStatusOut"])
    types["GetSearchApplicationSessionStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["SearchApplicationSessionStatsIn"]))}
    ).named(renames["GetSearchApplicationSessionStatsResponseIn"])
    types["GetSearchApplicationSessionStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["SearchApplicationSessionStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationSessionStatsResponseOut"])
    types["FuseboxItemThreadMatchInfoIn"] = t.struct(
        {
            "lastMatchingItemId": t.string().optional(),
            "clusterId": t.string().optional(),
            "lastMatchingItemKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "rank": t.proxy(renames["RankIn"]).optional(),
            "matchingItemKey": t.array(t.proxy(renames["MultiKeyIn"])).optional(),
        }
    ).named(renames["FuseboxItemThreadMatchInfoIn"])
    types["FuseboxItemThreadMatchInfoOut"] = t.struct(
        {
            "lastMatchingItemId": t.string().optional(),
            "clusterId": t.string().optional(),
            "lastMatchingItemKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "rank": t.proxy(renames["RankOut"]).optional(),
            "matchingItemKey": t.array(t.proxy(renames["MultiKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FuseboxItemThreadMatchInfoOut"])
    types["MdbGroupProtoIn"] = t.struct({"groupName": t.string()}).named(
        renames["MdbGroupProtoIn"]
    )
    types["MdbGroupProtoOut"] = t.struct(
        {"groupName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MdbGroupProtoOut"])
    types["AuthorizedItemIdIn"] = t.struct(
        {"resourceKey": t.string().optional(), "id": t.string().optional()}
    ).named(renames["AuthorizedItemIdIn"])
    types["AuthorizedItemIdOut"] = t.struct(
        {
            "resourceKey": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedItemIdOut"])
    types["SourceConfigIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "scoringConfig": t.proxy(renames["SourceScoringConfigIn"]).optional(),
            "crowdingConfig": t.proxy(renames["SourceCrowdingConfigIn"]).optional(),
        }
    ).named(renames["SourceConfigIn"])
    types["SourceConfigOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "scoringConfig": t.proxy(renames["SourceScoringConfigOut"]).optional(),
            "crowdingConfig": t.proxy(renames["SourceCrowdingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceConfigOut"])
    types["QueryInterpretationConfigIn"] = t.struct(
        {
            "forceVerbatimMode": t.boolean().optional(),
            "forceDisableSupplementalResults": t.boolean().optional(),
        }
    ).named(renames["QueryInterpretationConfigIn"])
    types["QueryInterpretationConfigOut"] = t.struct(
        {
            "forceVerbatimMode": t.boolean().optional(),
            "forceDisableSupplementalResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationConfigOut"])
    types["PhoneNumberIn"] = t.struct(
        {"type": t.string(), "phoneNumber": t.string().optional()}
    ).named(renames["PhoneNumberIn"])
    types["PhoneNumberOut"] = t.struct(
        {
            "type": t.string(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneNumberOut"])
    types["GetSearchApplicationUserStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["SearchApplicationUserStatsIn"]))}
    ).named(renames["GetSearchApplicationUserStatsResponseIn"])
    types["GetSearchApplicationUserStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["SearchApplicationUserStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationUserStatsResponseOut"])
    types["BabelPlaceholderMetadataIn"] = t.struct(
        {
            "hangoutVideoMetadata": t.proxy(renames["HangoutVideoEventMetadataIn"]),
            "editMetadata": t.proxy(renames["EditMetadataIn"]),
            "deleteMetadata": t.proxy(renames["DeleteMetadataIn"]),
        }
    ).named(renames["BabelPlaceholderMetadataIn"])
    types["BabelPlaceholderMetadataOut"] = t.struct(
        {
            "hangoutVideoMetadata": t.proxy(renames["HangoutVideoEventMetadataOut"]),
            "editMetadata": t.proxy(renames["EditMetadataOut"]),
            "deleteMetadata": t.proxy(renames["DeleteMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BabelPlaceholderMetadataOut"])
    types["LanguageConfigIn"] = t.struct(
        {"spokenLanguages": t.array(t.string()).optional()}
    ).named(renames["LanguageConfigIn"])
    types["LanguageConfigOut"] = t.struct(
        {
            "spokenLanguages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageConfigOut"])
    types["MenuItemIn"] = t.struct(
        {
            "selected": t.boolean(),
            "text": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["MenuItemIn"])
    types["MenuItemOut"] = t.struct(
        {
            "selected": t.boolean(),
            "text": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MenuItemOut"])
    types["CallInfoIn"] = t.struct(
        {
            "paygateInfo": t.proxy(renames["PaygateInfoIn"]).optional(),
            "availableAccessTypes": t.array(t.string()).optional(),
            "broadcastSessionInfo": t.proxy(
                renames["BroadcastSessionInfoIn"]
            ).optional(),
            "cseInfo": t.proxy(renames["CseInfoIn"]).optional(),
            "settings": t.proxy(renames["CallSettingsIn"]).optional(),
            "abuseReportingConfig": t.proxy(
                renames["AbuseReportingConfigIn"]
            ).optional(),
            "youTubeBroadcastSessionInfos": t.array(
                t.proxy(renames["YouTubeBroadcastSessionInfoIn"])
            ).optional(),
            "coActivity": t.proxy(renames["CoActivityIn"]).optional(),
            "presenter": t.proxy(renames["PresenterIn"]).optional(),
            "collaboration": t.proxy(renames["CollaborationIn"]).optional(),
            "recordingSessionInfo": t.proxy(
                renames["RecordingSessionInfoIn"]
            ).optional(),
            "viewerCount": t.integer().optional(),
            "recordingInfo": t.proxy(renames["RecordingInfoIn"]).optional(),
            "transcriptionSessionInfo": t.proxy(
                renames["TranscriptionSessionInfoIn"]
            ).optional(),
        }
    ).named(renames["CallInfoIn"])
    types["CallInfoOut"] = t.struct(
        {
            "paygateInfo": t.proxy(renames["PaygateInfoOut"]).optional(),
            "availableAccessTypes": t.array(t.string()).optional(),
            "broadcastSessionInfo": t.proxy(
                renames["BroadcastSessionInfoOut"]
            ).optional(),
            "cseInfo": t.proxy(renames["CseInfoOut"]).optional(),
            "availableReactions": t.array(
                t.proxy(renames["ReactionInfoOut"])
            ).optional(),
            "settings": t.proxy(renames["CallSettingsOut"]).optional(),
            "maxJoinedDevices": t.integer().optional(),
            "attachedDocuments": t.array(
                t.proxy(renames["DocumentInfoOut"])
            ).optional(),
            "abuseReportingConfig": t.proxy(
                renames["AbuseReportingConfigOut"]
            ).optional(),
            "youTubeBroadcastSessionInfos": t.array(
                t.proxy(renames["YouTubeBroadcastSessionInfoOut"])
            ).optional(),
            "coActivity": t.proxy(renames["CoActivityOut"]).optional(),
            "presenter": t.proxy(renames["PresenterOut"]).optional(),
            "artifactOwner": t.proxy(renames["UserDisplayInfoOut"]).optional(),
            "calendarEventId": t.string().optional(),
            "collaboration": t.proxy(renames["CollaborationOut"]).optional(),
            "recordingSessionInfo": t.proxy(
                renames["RecordingSessionInfoOut"]
            ).optional(),
            "streamingSessions": t.array(
                t.proxy(renames["StreamingSessionInfoOut"])
            ).optional(),
            "viewerCount": t.integer().optional(),
            "recordingInfo": t.proxy(renames["RecordingInfoOut"]).optional(),
            "organizationName": t.string().optional(),
            "transcriptionSessionInfo": t.proxy(
                renames["TranscriptionSessionInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CallInfoOut"])
    types["AppsDynamiteSharedEmojiIn"] = t.struct(
        {
            "customEmoji": t.proxy(
                renames["AppsDynamiteSharedCustomEmojiIn"]
            ).optional(),
            "unicode": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedEmojiIn"])
    types["AppsDynamiteSharedEmojiOut"] = t.struct(
        {
            "customEmoji": t.proxy(
                renames["AppsDynamiteSharedCustomEmojiOut"]
            ).optional(),
            "unicode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedEmojiOut"])
    types["MessagePropsIn"] = t.struct(
        {"babelProps": t.proxy(renames["BabelMessagePropsIn"])}
    ).named(renames["MessagePropsIn"])
    types["MessagePropsOut"] = t.struct(
        {
            "babelProps": t.proxy(renames["BabelMessagePropsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessagePropsOut"])
    types["SearchQualityMetadataIn"] = t.struct(
        {"quality": t.number().optional()}
    ).named(renames["SearchQualityMetadataIn"])
    types["SearchQualityMetadataOut"] = t.struct(
        {
            "quality": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchQualityMetadataOut"])
    types["AclInfoIn"] = t.struct(
        {
            "usersCount": t.integer().optional(),
            "groupsCount": t.integer().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["AclInfoIn"])
    types["AclInfoOut"] = t.struct(
        {
            "usersCount": t.integer().optional(),
            "groupsCount": t.integer().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclInfoOut"])
    types["EnumValuePairIn"] = t.struct(
        {"stringValue": t.string().optional(), "integerValue": t.integer().optional()}
    ).named(renames["EnumValuePairIn"])
    types["EnumValuePairOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "integerValue": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValuePairOut"])
    types["GoogleChatV1WidgetMarkupImageButtonIn"] = t.struct(
        {
            "icon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageButtonIn"])
    types["GoogleChatV1WidgetMarkupImageButtonOut"] = t.struct(
        {
            "icon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageButtonOut"])
    types["VPCSettingsIn"] = t.struct({"project": t.string().optional()}).named(
        renames["VPCSettingsIn"]
    )
    types["VPCSettingsOut"] = t.struct(
        {
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VPCSettingsOut"])
    types["PossiblyTrimmedModelIn"] = t.struct(
        {"model": t.string(), "isTrimmed": t.boolean()}
    ).named(renames["PossiblyTrimmedModelIn"])
    types["PossiblyTrimmedModelOut"] = t.struct(
        {
            "model": t.string(),
            "isTrimmed": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PossiblyTrimmedModelOut"])
    types["PeopleSuggestionIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["PeopleSuggestionIn"])
    types["PeopleSuggestionOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeopleSuggestionOut"])
    types["AppsDynamiteSharedOriginAppSuggestionIn"] = t.struct(
        {
            "cardClickSuggestion": t.proxy(
                renames["AppsDynamiteSharedCardClickSuggestionIn"]
            ),
            "appId": t.proxy(renames["AppIdIn"]),
        }
    ).named(renames["AppsDynamiteSharedOriginAppSuggestionIn"])
    types["AppsDynamiteSharedOriginAppSuggestionOut"] = t.struct(
        {
            "cardClickSuggestion": t.proxy(
                renames["AppsDynamiteSharedCardClickSuggestionOut"]
            ),
            "appId": t.proxy(renames["AppIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedOriginAppSuggestionOut"])
    types["HtmlOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["HtmlOperatorOptionsIn"])
    types["HtmlOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlOperatorOptionsOut"])
    types["GetCustomerSessionStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["CustomerSessionStatsIn"]))}
    ).named(renames["GetCustomerSessionStatsResponseIn"])
    types["GetCustomerSessionStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerSessionStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerSessionStatsResponseOut"])
    types["DateValuesIn"] = t.struct(
        {"values": t.array(t.proxy(renames["DateIn"]))}
    ).named(renames["DateValuesIn"])
    types["DateValuesOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["DateOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateValuesOut"])
    types["ListSearchApplicationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "searchApplications": t.array(t.proxy(renames["SearchApplicationIn"])),
        }
    ).named(renames["ListSearchApplicationsResponseIn"])
    types["ListSearchApplicationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "searchApplications": t.array(t.proxy(renames["SearchApplicationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSearchApplicationsResponseOut"])
    types["PollItemsResponseIn"] = t.struct(
        {"items": t.array(t.proxy(renames["ItemIn"])).optional()}
    ).named(renames["PollItemsResponseIn"])
    types["PollItemsResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollItemsResponseOut"])
    types["TombstoneMetadataIn"] = t.struct(
        {"tombstoneType": t.string().optional()}
    ).named(renames["TombstoneMetadataIn"])
    types["TombstoneMetadataOut"] = t.struct(
        {
            "tombstoneType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TombstoneMetadataOut"])
    types["GetCustomerIndexStatsResponseIn"] = t.struct(
        {
            "averageIndexedItemCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["CustomerIndexStatsIn"])).optional(),
        }
    ).named(renames["GetCustomerIndexStatsResponseIn"])
    types["GetCustomerIndexStatsResponseOut"] = t.struct(
        {
            "averageIndexedItemCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["CustomerIndexStatsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerIndexStatsResponseOut"])
    types["OnClickIn"] = t.struct(
        {
            "openLink": t.proxy(renames["OpenLinkIn"]),
            "link": t.string().optional(),
            "openLinkAction": t.proxy(renames["FormActionIn"]).optional(),
            "action": t.proxy(renames["FormActionIn"]),
        }
    ).named(renames["OnClickIn"])
    types["OnClickOut"] = t.struct(
        {
            "openLink": t.proxy(renames["OpenLinkOut"]),
            "link": t.string().optional(),
            "openLinkAction": t.proxy(renames["FormActionOut"]).optional(),
            "action": t.proxy(renames["FormActionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnClickOut"])
    types["TextPropertyOptionsIn"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["TextOperatorOptionsIn"]).optional(),
            "retrievalImportance": t.proxy(renames["RetrievalImportanceIn"]).optional(),
        }
    ).named(renames["TextPropertyOptionsIn"])
    types["TextPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["TextOperatorOptionsOut"]).optional(),
            "retrievalImportance": t.proxy(
                renames["RetrievalImportanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPropertyOptionsOut"])
    types["KeyValueIn"] = t.struct(
        {
            "imageStyle": t.string(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "topLabel": t.string().optional(),
            "iconUrl": t.string(),
            "contentMultiline": t.boolean(),
            "endIcon": t.proxy(renames["IconImageIn"]),
            "startIcon": t.proxy(renames["IconImageIn"]).optional(),
            "bottomLabel": t.string().optional(),
            "content": t.string().optional(),
            "icon": t.string(),
            "button": t.proxy(renames["ButtonIn"]),
            "iconAltText": t.string().optional(),
            "switchWidget": t.proxy(renames["SwitchWidgetIn"]),
        }
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "imageStyle": t.string(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "topLabel": t.string().optional(),
            "iconUrl": t.string(),
            "contentMultiline": t.boolean(),
            "endIcon": t.proxy(renames["IconImageOut"]),
            "startIcon": t.proxy(renames["IconImageOut"]).optional(),
            "bottomLabel": t.string().optional(),
            "content": t.string().optional(),
            "icon": t.string(),
            "button": t.proxy(renames["ButtonOut"]),
            "iconAltText": t.string().optional(),
            "switchWidget": t.proxy(renames["SwitchWidgetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
    types["AppsDynamiteStorageOpenLinkAppUriIn"] = t.struct(
        {
            "companionUri": t.string().optional(),
            "androidIntent": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIntentIn"]
            ).optional(),
            "iosUri": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIn"])
    types["AppsDynamiteStorageOpenLinkAppUriOut"] = t.struct(
        {
            "companionUri": t.string().optional(),
            "androidIntent": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIntentOut"]
            ).optional(),
            "iosUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriOut"])
    types["CustomEmojiMetadataIn"] = t.struct(
        {"customEmoji": t.proxy(renames["AppsDynamiteSharedCustomEmojiIn"])}
    ).named(renames["CustomEmojiMetadataIn"])
    types["CustomEmojiMetadataOut"] = t.struct(
        {
            "customEmoji": t.proxy(renames["AppsDynamiteSharedCustomEmojiOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomEmojiMetadataOut"])
    types["DriveTimeSpanRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveTimeSpanRestrictIn"]
    )
    types["DriveTimeSpanRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveTimeSpanRestrictOut"])
    types["VideoCallMetadataIn"] = t.struct(
        {
            "wasCreatedInCurrentGroup": t.boolean().optional(),
            "meetingSpace": t.proxy(renames["MeetingSpaceIn"]).optional(),
            "shouldNotRender": t.boolean().optional(),
        }
    ).named(renames["VideoCallMetadataIn"])
    types["VideoCallMetadataOut"] = t.struct(
        {
            "wasCreatedInCurrentGroup": t.boolean().optional(),
            "meetingSpace": t.proxy(renames["MeetingSpaceOut"]).optional(),
            "shouldNotRender": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCallMetadataOut"])
    types["AttributeRemovedIn"] = t.struct(
        {
            "attributeId": t.string(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
        }
    ).named(renames["AttributeRemovedIn"])
    types["AttributeRemovedOut"] = t.struct(
        {
            "attributeId": t.string(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeRemovedOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"])
    types["TaskActionMarkupIn"] = t.struct({"reloadTasks": t.boolean()}).named(
        renames["TaskActionMarkupIn"]
    )
    types["TaskActionMarkupOut"] = t.struct(
        {
            "reloadTasks": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskActionMarkupOut"])
    types["CompositeFilterIn"] = t.struct(
        {
            "logicOperator": t.string().optional(),
            "subFilters": t.array(t.proxy(renames["FilterIn"])).optional(),
        }
    ).named(renames["CompositeFilterIn"])
    types["CompositeFilterOut"] = t.struct(
        {
            "logicOperator": t.string().optional(),
            "subFilters": t.array(t.proxy(renames["FilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeFilterOut"])
    types["AuditLoggingSettingsIn"] = t.struct(
        {
            "logDataWriteActions": t.boolean().optional(),
            "logAdminReadActions": t.boolean().optional(),
            "project": t.string().optional(),
            "logDataReadActions": t.boolean().optional(),
        }
    ).named(renames["AuditLoggingSettingsIn"])
    types["AuditLoggingSettingsOut"] = t.struct(
        {
            "logDataWriteActions": t.boolean().optional(),
            "logAdminReadActions": t.boolean().optional(),
            "project": t.string().optional(),
            "logDataReadActions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLoggingSettingsOut"])
    types["LabelsIn"] = t.struct(
        {
            "id": t.array(t.string()).optional(),
            "displayName": t.array(t.string()).optional(),
        }
    ).named(renames["LabelsIn"])
    types["LabelsOut"] = t.struct(
        {
            "id": t.array(t.string()).optional(),
            "displayName": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelsOut"])
    types["SigningKeyPossessorProtoIn"] = t.struct(
        {
            "serializedVerificationKey": t.string().optional(),
            "keymasterKeyType": t.integer().optional(),
            "serializedVerificationKeyset": t.string().optional(),
        }
    ).named(renames["SigningKeyPossessorProtoIn"])
    types["SigningKeyPossessorProtoOut"] = t.struct(
        {
            "serializedVerificationKey": t.string().optional(),
            "keymasterKeyType": t.integer().optional(),
            "serializedVerificationKeyset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SigningKeyPossessorProtoOut"])
    types["LabelRenamedIn"] = t.struct({"oldCanonicalName": t.string()}).named(
        renames["LabelRenamedIn"]
    )
    types["LabelRenamedOut"] = t.struct(
        {
            "oldCanonicalName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelRenamedOut"])
    types["GetDataSourceIndexStatsResponseIn"] = t.struct(
        {
            "averageIndexedItemCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["DataSourceIndexStatsIn"])).optional(),
        }
    ).named(renames["GetDataSourceIndexStatsResponseIn"])
    types["GetDataSourceIndexStatsResponseOut"] = t.struct(
        {
            "averageIndexedItemCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["DataSourceIndexStatsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDataSourceIndexStatsResponseOut"])
    types["IntegerFacetingOptionsIn"] = t.struct(
        {"integerBuckets": t.array(t.string()).optional()}
    ).named(renames["IntegerFacetingOptionsIn"])
    types["IntegerFacetingOptionsOut"] = t.struct(
        {
            "integerBuckets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerFacetingOptionsOut"])
    types["GroupIdIn"] = t.struct(
        {
            "spaceId": t.proxy(renames["SpaceIdIn"]).optional(),
            "dmId": t.proxy(renames["DmIdIn"]).optional(),
        }
    ).named(renames["GroupIdIn"])
    types["GroupIdOut"] = t.struct(
        {
            "spaceId": t.proxy(renames["SpaceIdOut"]).optional(),
            "dmId": t.proxy(renames["DmIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupIdOut"])
    types["AppsDynamiteStorageColumnsColumnWidgetsIn"] = t.struct(
        {
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputIn"]).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerIn"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageIn"]).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListIn"]
            ).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextIn"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphIn"]
            ).optional(),
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnWidgetsIn"])
    types["AppsDynamiteStorageColumnsColumnWidgetsOut"] = t.struct(
        {
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputOut"]).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerOut"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageOut"]).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListOut"]
            ).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextOut"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphOut"]
            ).optional(),
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnWidgetsOut"])
    types["IdIn"] = t.struct(
        {
            "localId": t.string().optional(),
            "nameSpace": t.integer().optional(),
            "creatorUserId": t.string().optional(),
        }
    ).named(renames["IdIn"])
    types["IdOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "nameSpace": t.integer().optional(),
            "creatorUserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdOut"])
    types["CardHeaderIn"] = t.struct(
        {
            "imageAltText": t.string().optional(),
            "subtitle": t.string(),
            "imageStyle": t.string(),
            "imageUrl": t.string(),
            "title": t.string().optional(),
        }
    ).named(renames["CardHeaderIn"])
    types["CardHeaderOut"] = t.struct(
        {
            "imageAltText": t.string().optional(),
            "subtitle": t.string(),
            "imageStyle": t.string(),
            "imageUrl": t.string(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardHeaderOut"])
    types["MdbUserProtoIn"] = t.struct(
        {"gaiaId": t.string().optional(), "userName": t.string()}
    ).named(renames["MdbUserProtoIn"])
    types["MdbUserProtoOut"] = t.struct(
        {
            "gaiaId": t.string().optional(),
            "userName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MdbUserProtoOut"])
    types["ColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["GetSearchApplicationQueryStatsResponseIn"] = t.struct(
        {
            "stats": t.array(
                t.proxy(renames["SearchApplicationQueryStatsIn"])
            ).optional(),
            "totalQueryCount": t.string().optional(),
        }
    ).named(renames["GetSearchApplicationQueryStatsResponseIn"])
    types["GetSearchApplicationQueryStatsResponseOut"] = t.struct(
        {
            "stats": t.array(
                t.proxy(renames["SearchApplicationQueryStatsOut"])
            ).optional(),
            "totalQueryCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationQueryStatsResponseOut"])
    types["AppsDynamiteStorageButtonIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "disabled": t.boolean().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonIn"])
    types["AppsDynamiteStorageButtonOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "disabled": t.boolean().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonOut"])
    types["AppsDynamiteStorageSuggestionsIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageSuggestionsSuggestionItemIn"])
            ).optional()
        }
    ).named(renames["AppsDynamiteStorageSuggestionsIn"])
    types["AppsDynamiteStorageSuggestionsOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageSuggestionsSuggestionItemOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageSuggestionsOut"])
    types["AppsDynamiteStorageButtonListIn"] = t.struct(
        {"buttons": t.array(t.proxy(renames["AppsDynamiteStorageButtonIn"]))}
    ).named(renames["AppsDynamiteStorageButtonListIn"])
    types["AppsDynamiteStorageButtonListOut"] = t.struct(
        {
            "buttons": t.array(t.proxy(renames["AppsDynamiteStorageButtonOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonListOut"])
    types["GoogleChatV1WidgetMarkupButtonIn"] = t.struct(
        {
            "textButton": t.proxy(
                renames["GoogleChatV1WidgetMarkupTextButtonIn"]
            ).optional(),
            "imageButton": t.proxy(
                renames["GoogleChatV1WidgetMarkupImageButtonIn"]
            ).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupButtonIn"])
    types["GoogleChatV1WidgetMarkupButtonOut"] = t.struct(
        {
            "textButton": t.proxy(
                renames["GoogleChatV1WidgetMarkupTextButtonOut"]
            ).optional(),
            "imageButton": t.proxy(
                renames["GoogleChatV1WidgetMarkupImageButtonOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupButtonOut"])
    types["MessageAddedIn"] = t.struct(
        {
            "attributeIds": t.array(t.string()),
            "labelIds": t.array(t.string()),
            "messageKey": t.proxy(renames["MultiKeyIn"]),
            "syncIds": t.array(t.integer()).optional(),
        }
    ).named(renames["MessageAddedIn"])
    types["MessageAddedOut"] = t.struct(
        {
            "attributeIds": t.array(t.string()),
            "labelIds": t.array(t.string()),
            "messageKey": t.proxy(renames["MultiKeyOut"]),
            "syncIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageAddedOut"])
    types["CloudPrincipalProtoIn"] = t.struct({"id": t.string().optional()}).named(
        renames["CloudPrincipalProtoIn"]
    )
    types["CloudPrincipalProtoOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudPrincipalProtoOut"])
    types["PostiniUserProtoIn"] = t.struct({"postiniUserId": t.string()}).named(
        renames["PostiniUserProtoIn"]
    )
    types["PostiniUserProtoOut"] = t.struct(
        {
            "postiniUserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostiniUserProtoOut"])
    types["TextParagraphIn"] = t.struct({"text": t.string()}).named(
        renames["TextParagraphIn"]
    )
    types["TextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextParagraphOut"])
    types["AppsDynamiteSharedFindDocumentSuggestionIn"] = t.struct(
        {
            "documentSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedDocumentIn"])
            ).optional(),
            "showActionButtons": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteSharedFindDocumentSuggestionIn"])
    types["AppsDynamiteSharedFindDocumentSuggestionOut"] = t.struct(
        {
            "documentSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedDocumentOut"])
            ).optional(),
            "showActionButtons": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedFindDocumentSuggestionOut"])
    types["SortOptionsIn"] = t.struct(
        {"sortOrder": t.string().optional(), "operatorName": t.string().optional()}
    ).named(renames["SortOptionsIn"])
    types["SortOptionsOut"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortOptionsOut"])
    types["DriveLocationRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveLocationRestrictIn"]
    )
    types["DriveLocationRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveLocationRestrictOut"])
    types["PrefWrittenIn"] = t.struct({"value": t.string()}).named(
        renames["PrefWrittenIn"]
    )
    types["PrefWrittenOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PrefWrittenOut"])
    types["TimestampPropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["TimestampOperatorOptionsIn"]).optional()}
    ).named(renames["TimestampPropertyOptionsIn"])
    types["TimestampPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(
                renames["TimestampOperatorOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampPropertyOptionsOut"])
    types["TransientDataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TransientDataIn"]
    )
    types["TransientDataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TransientDataOut"])
    types["BooleanPropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["BooleanOperatorOptionsIn"]).optional()}
    ).named(renames["BooleanPropertyOptionsIn"])
    types["BooleanPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["BooleanOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanPropertyOptionsOut"])
    types["GridIn"] = t.struct(
        {
            "title": t.string().optional(),
            "numColumns": t.integer().optional(),
            "borderStyle": t.proxy(renames["BorderStyleIn"]).optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "items": t.array(t.proxy(renames["GridItemIn"])).optional(),
        }
    ).named(renames["GridIn"])
    types["GridOut"] = t.struct(
        {
            "title": t.string().optional(),
            "numColumns": t.integer().optional(),
            "borderStyle": t.proxy(renames["BorderStyleOut"]).optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "items": t.array(t.proxy(renames["GridItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridOut"])
    types["AbuseReportingConfigIn"] = t.struct(
        {
            "writtenUgcAllowed": t.boolean().optional(),
            "recordingAllowed": t.boolean().optional(),
        }
    ).named(renames["AbuseReportingConfigIn"])
    types["AbuseReportingConfigOut"] = t.struct(
        {
            "writtenUgcAllowed": t.boolean().optional(),
            "recordingAllowed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbuseReportingConfigOut"])
    types["ValueIn"] = t.struct(
        {
            "dateValue": t.proxy(renames["DateIn"]),
            "doubleValue": t.number(),
            "booleanValue": t.boolean(),
            "timestampValue": t.string(),
            "stringValue": t.string(),
            "integerValue": t.string(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "dateValue": t.proxy(renames["DateOut"]),
            "doubleValue": t.number(),
            "booleanValue": t.boolean(),
            "timestampValue": t.string(),
            "stringValue": t.string(),
            "integerValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["GoogleChatV1WidgetMarkupFormActionIn"] = t.struct(
        {
            "actionMethodName": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupFormActionActionParameterIn"])
            ).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupFormActionIn"])
    types["GoogleChatV1WidgetMarkupFormActionOut"] = t.struct(
        {
            "actionMethodName": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupFormActionActionParameterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupFormActionOut"])
    types["ImageComponentIn"] = t.struct(
        {
            "imageUrl": t.string(),
            "borderStyle": t.proxy(renames["BorderStyleIn"]),
            "cropStyle": t.proxy(renames["ImageCropStyleIn"]),
            "altText": t.string(),
        }
    ).named(renames["ImageComponentIn"])
    types["ImageComponentOut"] = t.struct(
        {
            "imageUrl": t.string(),
            "borderStyle": t.proxy(renames["BorderStyleOut"]),
            "cropStyle": t.proxy(renames["ImageCropStyleOut"]),
            "altText": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageComponentOut"])
    types["FormActionIn"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ActionParameterIn"])),
            "persistValues": t.boolean().optional(),
            "actionMethodName": t.string().optional(),
            "loadIndicator": t.string(),
        }
    ).named(renames["FormActionIn"])
    types["FormActionOut"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ActionParameterOut"])),
            "persistValues": t.boolean().optional(),
            "actionMethodName": t.string().optional(),
            "loadIndicator": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormActionOut"])
    types["AppsDynamiteSharedChatItemIn"] = t.struct(
        {
            "messageInfo": t.proxy(
                renames["AppsDynamiteSharedMessageInfoIn"]
            ).optional(),
            "activityInfo": t.array(
                t.proxy(renames["AppsDynamiteSharedChatItemActivityInfoIn"])
            ).optional(),
            "groupInfo": t.proxy(
                renames["AppsDynamiteSharedChatItemGroupInfoIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemIn"])
    types["AppsDynamiteSharedChatItemOut"] = t.struct(
        {
            "messageInfo": t.proxy(
                renames["AppsDynamiteSharedMessageInfoOut"]
            ).optional(),
            "activityInfo": t.array(
                t.proxy(renames["AppsDynamiteSharedChatItemActivityInfoOut"])
            ).optional(),
            "groupInfo": t.proxy(
                renames["AppsDynamiteSharedChatItemGroupInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemOut"])
    types["InitializeCustomerRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InitializeCustomerRequestIn"]
    )
    types["InitializeCustomerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InitializeCustomerRequestOut"])
    types["IconImageIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "icon": t.string(),
            "iconUrl": t.string(),
            "imageStyle": t.string().optional(),
        }
    ).named(renames["IconImageIn"])
    types["IconImageOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "icon": t.string(),
            "iconUrl": t.string(),
            "imageStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IconImageOut"])
    types["ResourceRoleProtoIn"] = t.struct(
        {
            "objectPart": t.string(),
            "roleId": t.integer(),
            "objectId": t.string(),
            "applicationId": t.string(),
        }
    ).named(renames["ResourceRoleProtoIn"])
    types["ResourceRoleProtoOut"] = t.struct(
        {
            "objectPart": t.string(),
            "roleId": t.integer(),
            "objectId": t.string(),
            "applicationId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRoleProtoOut"])
    types["DriveClientActionMarkupIn"] = t.struct(
        {"requestFileScope": t.proxy(renames["RequestFileScopeIn"])}
    ).named(renames["DriveClientActionMarkupIn"])
    types["DriveClientActionMarkupOut"] = t.struct(
        {
            "requestFileScope": t.proxy(renames["RequestFileScopeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveClientActionMarkupOut"])
    types["QueryInterpretationOptionsIn"] = t.struct(
        {
            "disableSupplementalResults": t.boolean().optional(),
            "disableNlInterpretation": t.boolean().optional(),
            "enableVerbatimMode": t.boolean().optional(),
        }
    ).named(renames["QueryInterpretationOptionsIn"])
    types["QueryInterpretationOptionsOut"] = t.struct(
        {
            "disableSupplementalResults": t.boolean().optional(),
            "disableNlInterpretation": t.boolean().optional(),
            "enableVerbatimMode": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationOptionsOut"])
    types["FilterCreatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilterCreatedIn"]
    )
    types["FilterCreatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FilterCreatedOut"])
    types["MemberIdIn"] = t.struct(
        {
            "rosterId": t.proxy(renames["RosterIdIn"]).optional(),
            "userId": t.proxy(renames["UserIdIn"]).optional(),
        }
    ).named(renames["MemberIdIn"])
    types["MemberIdOut"] = t.struct(
        {
            "rosterId": t.proxy(renames["RosterIdOut"]).optional(),
            "userId": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberIdOut"])
    types["MessageInfoIn"] = t.struct(
        {
            "message": t.proxy(renames["MessageIn"]).optional(),
            "authorUserType": t.string().optional(),
            "searcherMembershipState": t.string().optional(),
        }
    ).named(renames["MessageInfoIn"])
    types["MessageInfoOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "authorUserType": t.string().optional(),
            "searcherMembershipState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageInfoOut"])
    types["QueryItemIn"] = t.struct({"isSynthetic": t.boolean().optional()}).named(
        renames["QueryItemIn"]
    )
    types["QueryItemOut"] = t.struct(
        {
            "isSynthetic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryItemOut"])
    types["AppsDynamiteSharedMeetMetadataIn"] = t.struct(
        {"meetingUrl": t.string(), "meetingCode": t.string()}
    ).named(renames["AppsDynamiteSharedMeetMetadataIn"])
    types["AppsDynamiteSharedMeetMetadataOut"] = t.struct(
        {
            "meetingUrl": t.string(),
            "meetingCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMeetMetadataOut"])
    types["CapTokenHolderProtoIn"] = t.struct(
        {"tokenHmacSha1Prefix": t.string().optional()}
    ).named(renames["CapTokenHolderProtoIn"])
    types["CapTokenHolderProtoOut"] = t.struct(
        {
            "tokenHmacSha1Prefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapTokenHolderProtoOut"])
    types["AppsDynamiteSharedTasksAnnotationDataCreationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCreationIn"])
    types["AppsDynamiteSharedTasksAnnotationDataCreationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCreationOut"])
    types["AppsDynamiteStorageTextParagraphIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["AppsDynamiteStorageTextParagraphIn"])
    types["AppsDynamiteStorageTextParagraphOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageTextParagraphOut"])
    types["GoogleChatV1WidgetMarkupTextButtonIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupTextButtonIn"])
    types["GoogleChatV1WidgetMarkupTextButtonOut"] = t.struct(
        {
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupTextButtonOut"])
    types["HostProtoIn"] = t.struct(
        {"hostName": t.string().optional(), "hostOwner": t.string().optional()}
    ).named(renames["HostProtoIn"])
    types["HostProtoOut"] = t.struct(
        {
            "hostName": t.string().optional(),
            "hostOwner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostProtoOut"])
    types["FilterDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilterDeletedIn"]
    )
    types["FilterDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FilterDeletedOut"])
    types["DynamiteMessagesScoringInfoIn"] = t.struct(
        {
            "messageSenderAffinityScore": t.number(),
            "finalScore": t.number(),
            "spaceId": t.string(),
            "creatorGaiaId": t.string(),
            "dasContactCount": t.string(),
            "unjoinedSpaceAffinityScore": t.number(),
            "topicalityScore": t.number(),
            "freshnessScore": t.number(),
            "crowdingMultiplier": t.number(),
            "spaceMembershipCount": t.string(),
            "commonContactCount": t.string(),
            "joinedSpaceAffinityScore": t.number(),
            "commonCountToContactListCountRatio": t.number(),
            "creatorInSearcherContactList": t.boolean(),
            "lastReadTimestampAgeInDays": t.number(),
            "commonCountToMembershipCountRatio": t.number(),
            "messageAgeInDays": t.number(),
        }
    ).named(renames["DynamiteMessagesScoringInfoIn"])
    types["DynamiteMessagesScoringInfoOut"] = t.struct(
        {
            "messageSenderAffinityScore": t.number(),
            "finalScore": t.number(),
            "spaceId": t.string(),
            "creatorGaiaId": t.string(),
            "dasContactCount": t.string(),
            "unjoinedSpaceAffinityScore": t.number(),
            "topicalityScore": t.number(),
            "freshnessScore": t.number(),
            "crowdingMultiplier": t.number(),
            "spaceMembershipCount": t.string(),
            "commonContactCount": t.string(),
            "joinedSpaceAffinityScore": t.number(),
            "commonCountToContactListCountRatio": t.number(),
            "creatorInSearcherContactList": t.boolean(),
            "lastReadTimestampAgeInDays": t.number(),
            "commonCountToMembershipCountRatio": t.number(),
            "messageAgeInDays": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamiteMessagesScoringInfoOut"])
    types["AppsDynamiteStorageBorderStyleIn"] = t.struct(
        {
            "cornerRadius": t.integer().optional(),
            "strokeColor": t.proxy(renames["ColorIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageBorderStyleIn"])
    types["AppsDynamiteStorageBorderStyleOut"] = t.struct(
        {
            "cornerRadius": t.integer().optional(),
            "strokeColor": t.proxy(renames["ColorOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageBorderStyleOut"])
    types["AppsDynamiteSharedDocumentIn"] = t.struct(
        {
            "lastModifiedTime": t.string().optional(),
            "title": t.string().optional(),
            "url": t.string().optional(),
            "justification": t.proxy(
                renames["AppsDynamiteSharedJustificationIn"]
            ).optional(),
            "mimeType": t.string().optional(),
            "fileId": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedDocumentIn"])
    types["AppsDynamiteSharedDocumentOut"] = t.struct(
        {
            "lastModifiedTime": t.string().optional(),
            "title": t.string().optional(),
            "url": t.string().optional(),
            "justification": t.proxy(
                renames["AppsDynamiteSharedJustificationOut"]
            ).optional(),
            "mimeType": t.string().optional(),
            "fileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedDocumentOut"])
    types["RenameEventIn"] = t.struct(
        {"originalName": t.string(), "newName": t.string()}
    ).named(renames["RenameEventIn"])
    types["RenameEventOut"] = t.struct(
        {
            "originalName": t.string(),
            "newName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameEventOut"])
    types["ContentReportJustificationIn"] = t.struct(
        {"userJustification": t.string().optional()}
    ).named(renames["ContentReportJustificationIn"])
    types["ContentReportJustificationOut"] = t.struct(
        {
            "userJustification": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentReportJustificationOut"])
    types["MatchRangeIn"] = t.struct(
        {"end": t.integer().optional(), "start": t.integer().optional()}
    ).named(renames["MatchRangeIn"])
    types["MatchRangeOut"] = t.struct(
        {
            "end": t.integer().optional(),
            "start": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchRangeOut"])
    types["ChatProtoIn"] = t.struct(
        {"memberType": t.integer().optional(), "chatId": t.string().optional()}
    ).named(renames["ChatProtoIn"])
    types["ChatProtoOut"] = t.struct(
        {
            "memberType": t.integer().optional(),
            "chatId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatProtoOut"])
    types["GsuiteIntegrationMetadataIn"] = t.struct(
        {
            "callData": t.proxy(
                renames["AppsDynamiteSharedCallAnnotationDataIn"]
            ).optional(),
            "assistantData": t.proxy(
                renames["AppsDynamiteSharedAssistantAnnotationDataIn"]
            ),
            "calendarEventData": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataIn"]
            ),
            "tasksData": t.proxy(renames["AppsDynamiteSharedTasksAnnotationDataIn"]),
            "indexableTexts": t.array(t.string()).optional(),
            "clientType": t.string(),
            "activityFeedData": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataIn"]
            ),
        }
    ).named(renames["GsuiteIntegrationMetadataIn"])
    types["GsuiteIntegrationMetadataOut"] = t.struct(
        {
            "callData": t.proxy(
                renames["AppsDynamiteSharedCallAnnotationDataOut"]
            ).optional(),
            "assistantData": t.proxy(
                renames["AppsDynamiteSharedAssistantAnnotationDataOut"]
            ),
            "calendarEventData": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataOut"]
            ),
            "tasksData": t.proxy(renames["AppsDynamiteSharedTasksAnnotationDataOut"]),
            "indexableTexts": t.array(t.string()).optional(),
            "clientType": t.string(),
            "activityFeedData": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GsuiteIntegrationMetadataOut"])
    types["SearchItemsByViewUrlResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemIn"])),
        }
    ).named(renames["SearchItemsByViewUrlResponseIn"])
    types["SearchItemsByViewUrlResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchItemsByViewUrlResponseOut"])
    types["ButtonIn"] = t.struct(
        {
            "textButton": t.proxy(renames["TextButtonIn"]),
            "imageButton": t.proxy(renames["ImageButtonIn"]),
        }
    ).named(renames["ButtonIn"])
    types["ButtonOut"] = t.struct(
        {
            "textButton": t.proxy(renames["TextButtonOut"]),
            "imageButton": t.proxy(renames["ImageButtonOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ButtonOut"])
    types["AppsDynamiteSharedCallMetadataIn"] = t.struct(
        {
            "meetMetadata": t.proxy(
                renames["AppsDynamiteSharedMeetMetadataIn"]
            ).optional()
        }
    ).named(renames["AppsDynamiteSharedCallMetadataIn"])
    types["AppsDynamiteSharedCallMetadataOut"] = t.struct(
        {
            "meetMetadata": t.proxy(
                renames["AppsDynamiteSharedMeetMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCallMetadataOut"])
    types["AppsDynamiteSharedAssistantDebugContextIn"] = t.struct(
        {"query": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantDebugContextIn"])
    types["AppsDynamiteSharedAssistantDebugContextOut"] = t.struct(
        {
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantDebugContextOut"])
    types["AppsDynamiteSharedAssistantSessionContextIn"] = t.struct(
        {"contextualSessionId": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantSessionContextIn"])
    types["AppsDynamiteSharedAssistantSessionContextOut"] = t.struct(
        {
            "contextualSessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSessionContextOut"])
    types["AppsDynamiteV1ApiCompatV1AttachmentIn"] = t.struct(
        {
            "actions": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1ActionIn"])
            ).optional(),
            "attachment_type": t.string().optional(),
            "author_name": t.string().optional(),
            "image_url": t.string().optional(),
            "color": t.string().optional(),
            "author_icon": t.string().optional(),
            "thumb_url": t.string().optional(),
            "footer": t.string().optional(),
            "pretext": t.string().optional(),
            "fallback": t.string().optional(),
            "title": t.string().optional(),
            "text": t.string().optional(),
            "author_link": t.string().optional(),
            "title_link": t.string().optional(),
            "callback_id": t.string().optional(),
            "ts": t.integer().optional(),
            "fields": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1FieldIn"])
            ).optional(),
            "mrkdwn_in": t.array(t.string()).optional(),
            "footer_icon": t.string().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1AttachmentIn"])
    types["AppsDynamiteV1ApiCompatV1AttachmentOut"] = t.struct(
        {
            "actions": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1ActionOut"])
            ).optional(),
            "attachment_type": t.string().optional(),
            "author_name": t.string().optional(),
            "image_url": t.string().optional(),
            "color": t.string().optional(),
            "author_icon": t.string().optional(),
            "thumb_url": t.string().optional(),
            "footer": t.string().optional(),
            "pretext": t.string().optional(),
            "fallback": t.string().optional(),
            "title": t.string().optional(),
            "text": t.string().optional(),
            "author_link": t.string().optional(),
            "title_link": t.string().optional(),
            "callback_id": t.string().optional(),
            "ts": t.integer().optional(),
            "fields": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1FieldOut"])
            ).optional(),
            "mrkdwn_in": t.array(t.string()).optional(),
            "footer_icon": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1AttachmentOut"])
    types["ReactionInfoIn"] = t.struct({"emoji": t.string().optional()}).named(
        renames["ReactionInfoIn"]
    )
    types["ReactionInfoOut"] = t.struct(
        {
            "emoji": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReactionInfoOut"])
    types["EditorClientActionMarkupIn"] = t.struct(
        {
            "requestFileScopeForActiveDocument": t.proxy(
                renames["RequestFileScopeForActiveDocumentIn"]
            )
        }
    ).named(renames["EditorClientActionMarkupIn"])
    types["EditorClientActionMarkupOut"] = t.struct(
        {
            "requestFileScopeForActiveDocument": t.proxy(
                renames["RequestFileScopeForActiveDocumentOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditorClientActionMarkupOut"])
    types["HangoutEventIn"] = t.struct(
        {
            "participantId": t.array(t.proxy(renames["StoredParticipantIdIn"])),
            "mediaType": t.string(),
            "hangoutDurationSecs": t.string(),
            "type": t.string(),
        }
    ).named(renames["HangoutEventIn"])
    types["HangoutEventOut"] = t.struct(
        {
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "mediaType": t.string(),
            "hangoutDurationSecs": t.string(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutEventOut"])
    types["SearchApplicationIn"] = t.struct(
        {
            "defaultFacetOptions": t.array(
                t.proxy(renames["FacetOptionsIn"])
            ).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "returnResultThumbnailUrls": t.boolean().optional(),
            "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
            "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
            "queryInterpretationConfig": t.proxy(
                renames["QueryInterpretationConfigIn"]
            ).optional(),
            "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
            "enableAuditLog": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["SearchApplicationIn"])
    types["SearchApplicationOut"] = t.struct(
        {
            "defaultFacetOptions": t.array(
                t.proxy(renames["FacetOptionsOut"])
            ).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "returnResultThumbnailUrls": t.boolean().optional(),
            "defaultSortOptions": t.proxy(renames["SortOptionsOut"]).optional(),
            "scoringConfig": t.proxy(renames["ScoringConfigOut"]).optional(),
            "queryInterpretationConfig": t.proxy(
                renames["QueryInterpretationConfigOut"]
            ).optional(),
            "operationIds": t.array(t.string()).optional(),
            "sourceConfig": t.array(t.proxy(renames["SourceConfigOut"])).optional(),
            "enableAuditLog": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationOut"])
    types["GoogleChatV1WidgetMarkupFormActionActionParameterIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleChatV1WidgetMarkupFormActionActionParameterIn"])
    types["GoogleChatV1WidgetMarkupFormActionActionParameterOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupFormActionActionParameterOut"])
    types["FacetResultIn"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["FacetBucketIn"])).optional(),
            "objectType": t.string().optional(),
            "sourceName": t.string().optional(),
            "operatorName": t.string().optional(),
        }
    ).named(renames["FacetResultIn"])
    types["FacetResultOut"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["FacetBucketOut"])).optional(),
            "objectType": t.string().optional(),
            "sourceName": t.string().optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetResultOut"])
    types["GmailClientActionMarkupIn"] = t.struct(
        {
            "updateDraftActionMarkup": t.proxy(renames["UpdateDraftActionMarkupIn"]),
            "openCreatedDraftActionMarkup": t.proxy(
                renames["OpenCreatedDraftActionMarkupIn"]
            ),
            "taskAction": t.proxy(renames["TaskActionMarkupIn"]),
            "addonComposeUiActionMarkup": t.proxy(
                renames["AddonComposeUiActionMarkupIn"]
            ),
        }
    ).named(renames["GmailClientActionMarkupIn"])
    types["GmailClientActionMarkupOut"] = t.struct(
        {
            "updateDraftActionMarkup": t.proxy(renames["UpdateDraftActionMarkupOut"]),
            "openCreatedDraftActionMarkup": t.proxy(
                renames["OpenCreatedDraftActionMarkupOut"]
            ),
            "taskAction": t.proxy(renames["TaskActionMarkupOut"]),
            "addonComposeUiActionMarkup": t.proxy(
                renames["AddonComposeUiActionMarkupOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmailClientActionMarkupOut"])
    types["MediaIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["MediaIn"]
    )
    types["MediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["AppsDynamiteSharedSegmentedMembershipCountIn"] = t.struct(
        {
            "membershipCount": t.integer().optional(),
            "memberType": t.string(),
            "membershipState": t.string(),
        }
    ).named(renames["AppsDynamiteSharedSegmentedMembershipCountIn"])
    types["AppsDynamiteSharedSegmentedMembershipCountOut"] = t.struct(
        {
            "membershipCount": t.integer().optional(),
            "memberType": t.string(),
            "membershipState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedSegmentedMembershipCountOut"])
    types["StreamViewerStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["StreamViewerStatsIn"])
    types["StreamViewerStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamViewerStatsOut"])
    types["VideoInfoIn"] = t.struct({"duration": t.integer().optional()}).named(
        renames["VideoInfoIn"]
    )
    types["VideoInfoOut"] = t.struct(
        {
            "duration": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoInfoOut"])
    types["ClusterInfoIn"] = t.struct(
        {
            "throttled": t.boolean().optional(),
            "clusterId": t.array(t.string()).optional(),
        }
    ).named(renames["ClusterInfoIn"])
    types["ClusterInfoOut"] = t.struct(
        {
            "throttled": t.boolean().optional(),
            "clusterId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterInfoOut"])
    types["ListItemNamesForUnmappedIdentityResponseIn"] = t.struct(
        {"itemNames": t.array(t.string()), "nextPageToken": t.string().optional()}
    ).named(renames["ListItemNamesForUnmappedIdentityResponseIn"])
    types["ListItemNamesForUnmappedIdentityResponseOut"] = t.struct(
        {
            "itemNames": t.array(t.string()),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemNamesForUnmappedIdentityResponseOut"])
    types["ResultDisplayFieldIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "property": t.proxy(renames["NamedPropertyIn"]).optional(),
            "label": t.string().optional(),
        }
    ).named(renames["ResultDisplayFieldIn"])
    types["ResultDisplayFieldOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "property": t.proxy(renames["NamedPropertyOut"]).optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayFieldOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn"
    ] = t.struct({"value": t.string().optional(), "key": t.string().optional()}).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn"
        ]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut"
    ] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut"
        ]
    )
    types["SchemaIn"] = t.struct(
        {
            "objectDefinitions": t.array(
                t.proxy(renames["ObjectDefinitionIn"])
            ).optional(),
            "operationIds": t.array(t.string()).optional(),
        }
    ).named(renames["SchemaIn"])
    types["SchemaOut"] = t.struct(
        {
            "objectDefinitions": t.array(
                t.proxy(renames["ObjectDefinitionOut"])
            ).optional(),
            "operationIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaOut"])
    types["JobsettedServerSpecIn"] = t.struct(
        {"portName": t.string().optional(), "serverName": t.string().optional()}
    ).named(renames["JobsettedServerSpecIn"])
    types["JobsettedServerSpecOut"] = t.struct(
        {
            "portName": t.string().optional(),
            "serverName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobsettedServerSpecOut"])
    types["ItemContentIn"] = t.struct(
        {
            "contentDataRef": t.proxy(renames["UploadItemRefIn"]).optional(),
            "inlineContent": t.string().optional(),
            "contentFormat": t.string(),
            "hash": t.string().optional(),
        }
    ).named(renames["ItemContentIn"])
    types["ItemContentOut"] = t.struct(
        {
            "contentDataRef": t.proxy(renames["UploadItemRefOut"]).optional(),
            "inlineContent": t.string().optional(),
            "contentFormat": t.string(),
            "hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemContentOut"])
    types["MembershipChangedMetadataIn"] = t.struct(
        {
            "initiatorType": t.string().optional(),
            "affectedMemberProfiles": t.array(t.proxy(renames["MemberIn"])),
            "initiator": t.proxy(renames["UserIdIn"]).optional(),
            "type": t.string(),
            "initiatorProfile": t.proxy(renames["UserIn"]).optional(),
            "affectedMembers": t.array(t.proxy(renames["MemberIdIn"])).optional(),
            "affectedMemberships": t.array(t.proxy(renames["AffectedMembershipIn"])),
        }
    ).named(renames["MembershipChangedMetadataIn"])
    types["MembershipChangedMetadataOut"] = t.struct(
        {
            "initiatorType": t.string().optional(),
            "affectedMemberProfiles": t.array(t.proxy(renames["MemberOut"])),
            "initiator": t.proxy(renames["UserIdOut"]).optional(),
            "type": t.string(),
            "initiatorProfile": t.proxy(renames["UserOut"]).optional(),
            "affectedMembers": t.array(t.proxy(renames["MemberIdOut"])).optional(),
            "affectedMemberships": t.array(t.proxy(renames["AffectedMembershipOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipChangedMetadataOut"])
    types["QueryCountByStatusIn"] = t.struct(
        {"statusCode": t.integer().optional(), "count": t.string()}
    ).named(renames["QueryCountByStatusIn"])
    types["QueryCountByStatusOut"] = t.struct(
        {
            "statusCode": t.integer().optional(),
            "count": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryCountByStatusOut"])
    types["VoicePhoneNumberI18nDataIn"] = t.struct(
        {
            "countryCode": t.integer().optional(),
            "internationalNumber": t.string().optional(),
            "isValid": t.boolean().optional(),
            "regionCode": t.string().optional(),
            "validationResult": t.string().optional(),
            "nationalNumber": t.string().optional(),
        }
    ).named(renames["VoicePhoneNumberI18nDataIn"])
    types["VoicePhoneNumberI18nDataOut"] = t.struct(
        {
            "countryCode": t.integer().optional(),
            "internationalNumber": t.string().optional(),
            "isValid": t.boolean().optional(),
            "regionCode": t.string().optional(),
            "validationResult": t.string().optional(),
            "nationalNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoicePhoneNumberI18nDataOut"])
    types["TriggerActionIn"] = t.struct(
        {"data": t.string().optional(), "action": t.string(), "dataInt": t.string()}
    ).named(renames["TriggerActionIn"])
    types["TriggerActionOut"] = t.struct(
        {
            "data": t.string().optional(),
            "action": t.string(),
            "dataInt": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerActionOut"])
    types["GridItemIn"] = t.struct(
        {
            "textAlignment": t.string(),
            "image": t.proxy(renames["ImageComponentIn"]),
            "layout": t.string(),
            "identifier": t.string().optional(),
            "title": t.string().optional(),
            "subtitle": t.string(),
        }
    ).named(renames["GridItemIn"])
    types["GridItemOut"] = t.struct(
        {
            "textAlignment": t.string(),
            "image": t.proxy(renames["ImageComponentOut"]),
            "layout": t.string(),
            "identifier": t.string().optional(),
            "title": t.string().optional(),
            "subtitle": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridItemOut"])
    types["GSuitePrincipalIn"] = t.struct(
        {
            "gsuiteUserEmail": t.string().optional(),
            "gsuiteDomain": t.boolean().optional(),
            "gsuiteGroupEmail": t.string().optional(),
        }
    ).named(renames["GSuitePrincipalIn"])
    types["GSuitePrincipalOut"] = t.struct(
        {
            "gsuiteUserEmail": t.string().optional(),
            "gsuiteDomain": t.boolean().optional(),
            "gsuiteGroupEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GSuitePrincipalOut"])
    types["SlashCommandMetadataIn"] = t.struct(
        {
            "argumentsHint": t.string().optional(),
            "triggersDialog": t.boolean().optional(),
            "type": t.string(),
            "commandId": t.string().optional(),
            "commandName": t.string().optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
        }
    ).named(renames["SlashCommandMetadataIn"])
    types["SlashCommandMetadataOut"] = t.struct(
        {
            "argumentsHint": t.string().optional(),
            "triggersDialog": t.boolean().optional(),
            "type": t.string(),
            "commandId": t.string().optional(),
            "commandName": t.string().optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandMetadataOut"])
    types["IndexItemOptionsIn"] = t.struct(
        {"allowUnknownGsuitePrincipals": t.boolean().optional()}
    ).named(renames["IndexItemOptionsIn"])
    types["IndexItemOptionsOut"] = t.struct(
        {
            "allowUnknownGsuitePrincipals": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexItemOptionsOut"])
    types["CseInfoIn"] = t.struct(
        {"wrappedKey": t.string().optional(), "cseDomain": t.string().optional()}
    ).named(renames["CseInfoIn"])
    types["CseInfoOut"] = t.struct(
        {
            "wrappedKey": t.string().optional(),
            "cseDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CseInfoOut"])
    types["CustomFunctionReturnValueMarkupIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["CustomFunctionReturnValueMarkupIn"])
    types["CustomFunctionReturnValueMarkupOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomFunctionReturnValueMarkupOut"])
    types["GoogleChatV1ContextualAddOnMarkupIn"] = t.struct(
        {
            "cards": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardIn"])
            ).optional()
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupIn"])
    types["GoogleChatV1ContextualAddOnMarkupOut"] = t.struct(
        {
            "cards": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupOut"])
    types["PreStateIn"] = t.struct(
        {
            "syncIds": t.array(t.integer()).optional(),
            "messageKey": t.proxy(renames["MultiKeyIn"]),
            "labelIds": t.array(t.string()),
            "threadKey": t.proxy(renames["MultiKeyIn"]),
        }
    ).named(renames["PreStateIn"])
    types["PreStateOut"] = t.struct(
        {
            "syncIds": t.array(t.integer()).optional(),
            "messageKey": t.proxy(renames["MultiKeyOut"]),
            "labelIds": t.array(t.string()),
            "threadKey": t.proxy(renames["MultiKeyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreStateOut"])
    types["PinnedItemIdIn"] = t.struct({"driveId": t.string().optional()}).named(
        renames["PinnedItemIdIn"]
    )
    types["PinnedItemIdOut"] = t.struct(
        {
            "driveId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PinnedItemIdOut"])
    types["YouTubeBroadcastSessionInfoIn"] = t.struct(
        {
            "broadcastStats": t.proxy(renames["YouTubeBroadcastStatsIn"]).optional(),
            "youTubeLiveBroadcastEvent": t.proxy(
                renames["YouTubeLiveBroadcastEventIn"]
            ).optional(),
            "youTubeBroadcastSessionId": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
        }
    ).named(renames["YouTubeBroadcastSessionInfoIn"])
    types["YouTubeBroadcastSessionInfoOut"] = t.struct(
        {
            "broadcastStats": t.proxy(renames["YouTubeBroadcastStatsOut"]).optional(),
            "youTubeLiveBroadcastEvent": t.proxy(
                renames["YouTubeLiveBroadcastEventOut"]
            ).optional(),
            "youTubeBroadcastSessionId": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeBroadcastSessionInfoOut"])
    types["QueryOperatorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "isReturnable": t.boolean().optional(),
            "isSortable": t.boolean().optional(),
            "objectType": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "isSuggestable": t.boolean().optional(),
            "operatorName": t.string().optional(),
            "enumValues": t.array(t.string()).optional(),
            "isRepeatable": t.boolean().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["QueryOperatorIn"])
    types["QueryOperatorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "isReturnable": t.boolean().optional(),
            "isSortable": t.boolean().optional(),
            "objectType": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "isSuggestable": t.boolean().optional(),
            "operatorName": t.string().optional(),
            "enumValues": t.array(t.string()).optional(),
            "isRepeatable": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOperatorOut"])
    types["CustomerUserStatsIn"] = t.struct(
        {
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "oneDayActiveUsersCount": t.string().optional(),
        }
    ).named(renames["CustomerUserStatsIn"])
    types["CustomerUserStatsOut"] = t.struct(
        {
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "oneDayActiveUsersCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerUserStatsOut"])
    types["IntegerOperatorOptionsIn"] = t.struct(
        {
            "lessThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
        }
    ).named(renames["IntegerOperatorOptionsIn"])
    types["IntegerOperatorOptionsOut"] = t.struct(
        {
            "lessThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerOperatorOptionsOut"])
    types["EditMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EditMetadataIn"]
    )
    types["EditMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EditMetadataOut"])
    types["FolderAttributeIn"] = t.struct(
        {"folder": t.array(t.proxy(renames["FolderIn"])).optional()}
    ).named(renames["FolderAttributeIn"])
    types["FolderAttributeOut"] = t.struct(
        {
            "folder": t.array(t.proxy(renames["FolderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderAttributeOut"])
    types["RecordingInfoIn"] = t.struct(
        {
            "latestRecordingEvent": t.proxy(renames["RecordingEventIn"]).optional(),
            "recordingApplicationType": t.string().optional(),
            "recordingStatus": t.string().optional(),
            "recordingId": t.string().optional(),
            "ownerDisplayName": t.string().optional(),
            "producerDeviceId": t.string().optional(),
        }
    ).named(renames["RecordingInfoIn"])
    types["RecordingInfoOut"] = t.struct(
        {
            "latestRecordingEvent": t.proxy(renames["RecordingEventOut"]).optional(),
            "recordingApplicationType": t.string().optional(),
            "recordingStatus": t.string().optional(),
            "recordingId": t.string().optional(),
            "ownerDisplayName": t.string().optional(),
            "producerDeviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordingInfoOut"])
    types["TriggerKeyIn"] = t.struct(
        {"type": t.string().optional(), "instanceId": t.string().optional()}
    ).named(renames["TriggerKeyIn"])
    types["TriggerKeyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "instanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerKeyOut"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut"])
    types["CustomerIndexStatsIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusIn"])
            ).optional(),
        }
    ).named(renames["CustomerIndexStatsIn"])
    types["CustomerIndexStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerIndexStatsOut"])
    types["InteractionIn"] = t.struct(
        {
            "interactionTime": t.string().optional(),
            "principal": t.proxy(renames["PrincipalIn"]).optional(),
            "type": t.string(),
        }
    ).named(renames["InteractionIn"])
    types["InteractionOut"] = t.struct(
        {
            "interactionTime": t.string().optional(),
            "principal": t.proxy(renames["PrincipalOut"]).optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InteractionOut"])
    types["MemberIn"] = t.struct(
        {"user": t.proxy(renames["UserIn"]), "roster": t.proxy(renames["RosterIn"])}
    ).named(renames["MemberIn"])
    types["MemberOut"] = t.struct(
        {
            "user": t.proxy(renames["UserOut"]),
            "roster": t.proxy(renames["RosterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberOut"])
    types["OtrModificationEventIn"] = t.struct(
        {
            "newOtrToggle": t.string(),
            "oldOtrToggle": t.string(),
            "newOtrStatus": t.string(),
            "oldOtrStatus": t.string(),
        }
    ).named(renames["OtrModificationEventIn"])
    types["OtrModificationEventOut"] = t.struct(
        {
            "newOtrToggle": t.string(),
            "oldOtrToggle": t.string(),
            "newOtrStatus": t.string(),
            "oldOtrStatus": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtrModificationEventOut"])
    types["DisplayedPropertyIn"] = t.struct(
        {"propertyName": t.string().optional()}
    ).named(renames["DisplayedPropertyIn"])
    types["DisplayedPropertyOut"] = t.struct(
        {
            "propertyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayedPropertyOut"])
    types["SelectionControlIn"] = t.struct(
        {
            "name": t.string().optional(),
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
            "type": t.string(),
            "label": t.string().optional(),
            "items": t.array(t.proxy(renames["SelectionItemIn"])).optional(),
        }
    ).named(renames["SelectionControlIn"])
    types["SelectionControlOut"] = t.struct(
        {
            "name": t.string().optional(),
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "type": t.string(),
            "label": t.string().optional(),
            "items": t.array(t.proxy(renames["SelectionItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionControlOut"])
    types["IntegerValuesIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["IntegerValuesIn"]
    )
    types["IntegerValuesOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerValuesOut"])
    types["DriveFollowUpRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveFollowUpRestrictIn"]
    )
    types["DriveFollowUpRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveFollowUpRestrictOut"])
    types["GaiaGroupProtoIn"] = t.struct({"groupId": t.string()}).named(
        renames["GaiaGroupProtoIn"]
    )
    types["GaiaGroupProtoOut"] = t.struct(
        {"groupId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GaiaGroupProtoOut"])
    types["LdapGroupProtoIn"] = t.struct({"groupName": t.string()}).named(
        renames["LdapGroupProtoIn"]
    )
    types["LdapGroupProtoOut"] = t.struct(
        {"groupName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LdapGroupProtoOut"])
    types["YouTubeBroadcastStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["YouTubeBroadcastStatsIn"])
    types["YouTubeBroadcastStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeBroadcastStatsOut"])
    types["TopicStateIn"] = t.struct(
        {
            "numConstituents": t.integer().optional(),
            "labelIdMessageCount": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TopicStateIn"])
    types["TopicStateOut"] = t.struct(
        {
            "numConstituents": t.integer().optional(),
            "labelIdMessageCount": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicStateOut"])
    types["UpdateDraftActionMarkupIn"] = t.struct(
        {
            "updateBody": t.proxy(renames["UpdateBodyIn"]).optional(),
            "updateSubject": t.proxy(renames["UpdateSubjectIn"]).optional(),
            "updateToRecipients": t.proxy(renames["UpdateToRecipientsIn"]).optional(),
            "updateBccRecipients": t.proxy(renames["UpdateBccRecipientsIn"]).optional(),
            "updateCcRecipients": t.proxy(renames["UpdateCcRecipientsIn"]).optional(),
        }
    ).named(renames["UpdateDraftActionMarkupIn"])
    types["UpdateDraftActionMarkupOut"] = t.struct(
        {
            "updateBody": t.proxy(renames["UpdateBodyOut"]).optional(),
            "updateSubject": t.proxy(renames["UpdateSubjectOut"]).optional(),
            "updateToRecipients": t.proxy(renames["UpdateToRecipientsOut"]).optional(),
            "updateBccRecipients": t.proxy(
                renames["UpdateBccRecipientsOut"]
            ).optional(),
            "updateCcRecipients": t.proxy(renames["UpdateCcRecipientsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDraftActionMarkupOut"])
    types["MessageAttributesIn"] = t.struct(
        {"isTombstone": t.boolean().optional()}
    ).named(renames["MessageAttributesIn"])
    types["MessageAttributesOut"] = t.struct(
        {
            "isTombstone": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageAttributesOut"])
    types["AppsDynamiteStorageOnClickIn"] = t.struct(
        {
            "openDynamicLinkAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "hostAppAction": t.proxy(renames["HostAppActionMarkupIn"]).optional(),
            "action": t.proxy(renames["AppsDynamiteStorageActionIn"]).optional(),
            "openLink": t.proxy(renames["AppsDynamiteStorageOpenLinkIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOnClickIn"])
    types["AppsDynamiteStorageOnClickOut"] = t.struct(
        {
            "openDynamicLinkAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "hostAppAction": t.proxy(renames["HostAppActionMarkupOut"]).optional(),
            "action": t.proxy(renames["AppsDynamiteStorageActionOut"]).optional(),
            "openLink": t.proxy(renames["AppsDynamiteStorageOpenLinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOnClickOut"])
    types["CardCapabilityMetadataIn"] = t.struct(
        {"requiredCapabilities": t.array(t.string()).optional()}
    ).named(renames["CardCapabilityMetadataIn"])
    types["CardCapabilityMetadataOut"] = t.struct(
        {
            "requiredCapabilities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardCapabilityMetadataOut"])
    types["AppsDynamiteSharedTasksAnnotationDataIn"] = t.struct(
        {
            "taskProperties": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"]
            ).optional(),
            "creation": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCreationIn"]
            ),
            "completionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"]
            ),
            "userDefinedMessage": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"]
            ),
            "deletionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"]
            ),
            "assigneeChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"]
            ),
            "taskId": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataIn"])
    types["AppsDynamiteSharedTasksAnnotationDataOut"] = t.struct(
        {
            "taskProperties": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"]
            ).optional(),
            "creation": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCreationOut"]
            ),
            "completionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"]
            ),
            "userDefinedMessage": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"]
            ),
            "deletionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"]
            ),
            "assigneeChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"]
            ),
            "taskId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataOut"])
    types["UserMentionMetadataIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "type": t.string(),
            "userMentionError": t.string().optional(),
            "gender": t.string().optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
            "inviteeInfo": t.proxy(renames["InviteeInfoIn"]).optional(),
        }
    ).named(renames["UserMentionMetadataIn"])
    types["UserMentionMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "type": t.string(),
            "userMentionError": t.string().optional(),
            "gender": t.string().optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "inviteeInfo": t.proxy(renames["InviteeInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserMentionMetadataOut"])
    types["GoogleChatV1ContextualAddOnMarkupCardCardActionIn"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardCardActionIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardCardActionOut"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardCardActionOut"])
    types["AppsDynamiteSharedOrganizationInfoIn"] = t.struct(
        {
            "customerInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoCustomerInfoIn"]
            ),
            "consumerInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoConsumerInfoIn"]
            ),
        }
    ).named(renames["AppsDynamiteSharedOrganizationInfoIn"])
    types["AppsDynamiteSharedOrganizationInfoOut"] = t.struct(
        {
            "customerInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoCustomerInfoOut"]
            ),
            "consumerInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoConsumerInfoOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedOrganizationInfoOut"])
    types["AppsDynamiteStorageDividerIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteStorageDividerIn"])
    types["AppsDynamiteStorageDividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteStorageDividerOut"])
    types["SearchResponseIn"] = t.struct(
        {
            "hasMoreResults": t.boolean().optional(),
            "errorInfo": t.proxy(renames["ErrorInfoIn"]).optional(),
            "debugInfo": t.proxy(renames["ResponseDebugInfoIn"]).optional(),
            "facetResults": t.array(t.proxy(renames["FacetResultIn"])).optional(),
            "results": t.array(t.proxy(renames["SearchResultIn"])).optional(),
            "structuredResults": t.array(
                t.proxy(renames["StructuredResultIn"])
            ).optional(),
            "resultCountEstimate": t.string().optional(),
            "queryInterpretation": t.proxy(renames["QueryInterpretationIn"]).optional(),
            "resultCounts": t.proxy(renames["ResultCountsIn"]).optional(),
            "spellResults": t.array(t.proxy(renames["SpellResultIn"])).optional(),
            "resultCountExact": t.string().optional(),
        }
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "hasMoreResults": t.boolean().optional(),
            "errorInfo": t.proxy(renames["ErrorInfoOut"]).optional(),
            "debugInfo": t.proxy(renames["ResponseDebugInfoOut"]).optional(),
            "facetResults": t.array(t.proxy(renames["FacetResultOut"])).optional(),
            "results": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "structuredResults": t.array(
                t.proxy(renames["StructuredResultOut"])
            ).optional(),
            "resultCountEstimate": t.string().optional(),
            "queryInterpretation": t.proxy(
                renames["QueryInterpretationOut"]
            ).optional(),
            "resultCounts": t.proxy(renames["ResultCountsOut"]).optional(),
            "spellResults": t.array(t.proxy(renames["SpellResultOut"])).optional(),
            "resultCountExact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
    types["TextKeyValueIn"] = t.struct(
        {
            "key": t.string(),
            "onClick": t.proxy(renames["OnClickIn"]),
            "text": t.string(),
        }
    ).named(renames["TextKeyValueIn"])
    types["TextKeyValueOut"] = t.struct(
        {
            "key": t.string(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "text": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextKeyValueOut"])
    types["EnumOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["EnumOperatorOptionsIn"])
    types["EnumOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOperatorOptionsOut"])
    types["SocialGraphNodeProtoIn"] = t.struct(
        {"sgnPk": t.string(), "sgnDomain": t.string().optional()}
    ).named(renames["SocialGraphNodeProtoIn"])
    types["SocialGraphNodeProtoOut"] = t.struct(
        {
            "sgnPk": t.string(),
            "sgnDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocialGraphNodeProtoOut"])
    types["AppsDynamiteSharedContentReportTypeIn"] = t.struct(
        {"systemViolation": t.string()}
    ).named(renames["AppsDynamiteSharedContentReportTypeIn"])
    types["AppsDynamiteSharedContentReportTypeOut"] = t.struct(
        {
            "systemViolation": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedContentReportTypeOut"])
    types["MultiKeyIn"] = t.struct(
        {
            "serverId": t.string().optional(),
            "clientAssignedPermId": t.string().optional(),
        }
    ).named(renames["MultiKeyIn"])
    types["MultiKeyOut"] = t.struct(
        {
            "serverId": t.string().optional(),
            "clientAssignedPermId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiKeyOut"])
    types["ContextualAddOnMarkupIn"] = t.struct(
        {
            "cards": t.array(t.proxy(renames["CardIn"])).optional(),
            "toolbar": t.proxy(renames["ToolbarIn"]).optional(),
        }
    ).named(renames["ContextualAddOnMarkupIn"])
    types["ContextualAddOnMarkupOut"] = t.struct(
        {
            "cards": t.array(t.proxy(renames["CardOut"])).optional(),
            "toolbar": t.proxy(renames["ToolbarOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextualAddOnMarkupOut"])
    types["RetrievalImportanceIn"] = t.struct(
        {"importance": t.string().optional()}
    ).named(renames["RetrievalImportanceIn"])
    types["RetrievalImportanceOut"] = t.struct(
        {
            "importance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrievalImportanceOut"])
    types["RequestFileScopeForActiveDocumentIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestFileScopeForActiveDocumentIn"])
    types["RequestFileScopeForActiveDocumentOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestFileScopeForActiveDocumentOut"])
    types["AnnotationIn"] = t.struct(
        {
            "requiredMessageFeaturesMetadata": t.proxy(
                renames["RequiredMessageFeaturesMetadataIn"]
            ).optional(),
            "incomingWebhookChangedMetadata": t.proxy(
                renames["IncomingWebhookChangedMetadataIn"]
            ),
            "componentSearchInfo": t.proxy(
                renames["AppsDynamiteSharedMessageComponentSearchInfoIn"]
            ).optional(),
            "roomUpdated": t.proxy(renames["RoomUpdatedMetadataIn"]),
            "slashCommandMetadata": t.proxy(renames["SlashCommandMetadataIn"]),
            "babelPlaceholderMetadata": t.proxy(renames["BabelPlaceholderMetadataIn"]),
            "type": t.string().optional(),
            "urlMetadata": t.proxy(renames["UrlMetadataIn"]),
            "uploadMetadata": t.proxy(renames["UploadMetadataIn"]),
            "customEmojiMetadata": t.proxy(renames["CustomEmojiMetadataIn"]),
            "integrationConfigUpdated": t.proxy(
                renames["IntegrationConfigUpdatedMetadataIn"]
            ).optional(),
            "formatMetadata": t.proxy(renames["FormatMetadataIn"]),
            "chipRenderType": t.string().optional(),
            "dataLossPreventionMetadata": t.proxy(
                renames["DataLossPreventionMetadataIn"]
            ),
            "consentedAppUnfurlMetadata": t.proxy(
                renames["ConsentedAppUnfurlMetadataIn"]
            ),
            "driveMetadata": t.proxy(renames["DriveMetadataIn"]).optional(),
            "interactionData": t.proxy(renames["InteractionDataIn"]).optional(),
            "length": t.integer().optional(),
            "groupRetentionSettingsUpdated": t.proxy(
                renames["GroupRetentionSettingsUpdatedMetaDataIn"]
            ),
            "videoCallMetadata": t.proxy(renames["VideoCallMetadataIn"]),
            "gsuiteIntegrationMetadata": t.proxy(
                renames["GsuiteIntegrationMetadataIn"]
            ).optional(),
            "startIndex": t.integer().optional(),
            "inlineRenderFormat": t.string().optional(),
            "localId": t.string().optional(),
            "youtubeMetadata": t.proxy(renames["YoutubeMetadataIn"]),
            "uniqueId": t.string().optional(),
            "membershipChanged": t.proxy(
                renames["MembershipChangedMetadataIn"]
            ).optional(),
            "cardCapabilityMetadata": t.proxy(
                renames["CardCapabilityMetadataIn"]
            ).optional(),
            "readReceiptsSettingsMetadata": t.proxy(
                renames["ReadReceiptsSettingsUpdatedMetadataIn"]
            ),
            "serverInvalidated": t.boolean().optional(),
            "userMentionMetadata": t.proxy(renames["UserMentionMetadataIn"]).optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "requiredMessageFeaturesMetadata": t.proxy(
                renames["RequiredMessageFeaturesMetadataOut"]
            ).optional(),
            "incomingWebhookChangedMetadata": t.proxy(
                renames["IncomingWebhookChangedMetadataOut"]
            ),
            "componentSearchInfo": t.proxy(
                renames["AppsDynamiteSharedMessageComponentSearchInfoOut"]
            ).optional(),
            "roomUpdated": t.proxy(renames["RoomUpdatedMetadataOut"]),
            "slashCommandMetadata": t.proxy(renames["SlashCommandMetadataOut"]),
            "babelPlaceholderMetadata": t.proxy(renames["BabelPlaceholderMetadataOut"]),
            "type": t.string().optional(),
            "urlMetadata": t.proxy(renames["UrlMetadataOut"]),
            "uploadMetadata": t.proxy(renames["UploadMetadataOut"]),
            "customEmojiMetadata": t.proxy(renames["CustomEmojiMetadataOut"]),
            "integrationConfigUpdated": t.proxy(
                renames["IntegrationConfigUpdatedMetadataOut"]
            ).optional(),
            "formatMetadata": t.proxy(renames["FormatMetadataOut"]),
            "chipRenderType": t.string().optional(),
            "dataLossPreventionMetadata": t.proxy(
                renames["DataLossPreventionMetadataOut"]
            ),
            "consentedAppUnfurlMetadata": t.proxy(
                renames["ConsentedAppUnfurlMetadataOut"]
            ),
            "driveMetadata": t.proxy(renames["DriveMetadataOut"]).optional(),
            "interactionData": t.proxy(renames["InteractionDataOut"]).optional(),
            "length": t.integer().optional(),
            "groupRetentionSettingsUpdated": t.proxy(
                renames["GroupRetentionSettingsUpdatedMetaDataOut"]
            ),
            "videoCallMetadata": t.proxy(renames["VideoCallMetadataOut"]),
            "gsuiteIntegrationMetadata": t.proxy(
                renames["GsuiteIntegrationMetadataOut"]
            ).optional(),
            "startIndex": t.integer().optional(),
            "inlineRenderFormat": t.string().optional(),
            "localId": t.string().optional(),
            "youtubeMetadata": t.proxy(renames["YoutubeMetadataOut"]),
            "uniqueId": t.string().optional(),
            "membershipChanged": t.proxy(
                renames["MembershipChangedMetadataOut"]
            ).optional(),
            "cardCapabilityMetadata": t.proxy(
                renames["CardCapabilityMetadataOut"]
            ).optional(),
            "readReceiptsSettingsMetadata": t.proxy(
                renames["ReadReceiptsSettingsUpdatedMetadataOut"]
            ),
            "serverInvalidated": t.boolean().optional(),
            "userMentionMetadata": t.proxy(
                renames["UserMentionMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["BabelMessagePropsIn"] = t.struct(
        {
            "contentExtension": t.proxy(renames["ChatContentExtensionIn"]).optional(),
            "wasUpdatedByBackfill": t.boolean().optional(),
            "deliveryMedium": t.proxy(renames["DeliveryMediumIn"]).optional(),
            "clientGeneratedId": t.string().optional(),
            "messageContent": t.proxy(
                renames["ChatConserverMessageContentIn"]
            ).optional(),
            "eventId": t.string().optional(),
        }
    ).named(renames["BabelMessagePropsIn"])
    types["BabelMessagePropsOut"] = t.struct(
        {
            "contentExtension": t.proxy(renames["ChatContentExtensionOut"]).optional(),
            "wasUpdatedByBackfill": t.boolean().optional(),
            "deliveryMedium": t.proxy(renames["DeliveryMediumOut"]).optional(),
            "clientGeneratedId": t.string().optional(),
            "messageContent": t.proxy(
                renames["ChatConserverMessageContentOut"]
            ).optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BabelMessagePropsOut"])
    types["YoutubeMetadataIn"] = t.struct(
        {
            "startTime": t.integer().optional(),
            "id": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
        }
    ).named(renames["YoutubeMetadataIn"])
    types["YoutubeMetadataOut"] = t.struct(
        {
            "startTime": t.integer().optional(),
            "id": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeMetadataOut"])
    types["AppsDynamiteSharedJustificationPersonIn"] = t.struct(
        {
            "user": t.proxy(renames["UserIdIn"]).optional(),
            "isRecipient": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteSharedJustificationPersonIn"])
    types["AppsDynamiteSharedJustificationPersonOut"] = t.struct(
        {
            "user": t.proxy(renames["UserIdOut"]).optional(),
            "isRecipient": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedJustificationPersonOut"])
    types["RequestOptionsIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "searchApplicationId": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["RequestOptionsIn"])
    types["RequestOptionsOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "searchApplicationId": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOptionsOut"])
    types["FixedFooterIn"] = t.struct(
        {
            "primaryButton": t.proxy(renames["TextButtonIn"]),
            "buttons": t.array(t.proxy(renames["ButtonIn"])),
            "secondaryButton": t.proxy(renames["TextButtonIn"]),
        }
    ).named(renames["FixedFooterIn"])
    types["FixedFooterOut"] = t.struct(
        {
            "primaryButton": t.proxy(renames["TextButtonOut"]),
            "buttons": t.array(t.proxy(renames["ButtonOut"])),
            "secondaryButton": t.proxy(renames["TextButtonOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixedFooterOut"])
    types["AppsDynamiteSharedAssistantUnfulfillableRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantUnfulfillableRequestIn"])
    types["AppsDynamiteSharedAssistantUnfulfillableRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedAssistantUnfulfillableRequestOut"])
    types["AppsDynamiteSharedTextSegmentIn"] = t.struct(
        {"length": t.integer().optional(), "startIndex": t.integer().optional()}
    ).named(renames["AppsDynamiteSharedTextSegmentIn"])
    types["AppsDynamiteSharedTextSegmentOut"] = t.struct(
        {
            "length": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTextSegmentOut"])
    types["AppsDynamiteSharedGroupDetailsIn"] = t.struct(
        {"description": t.string().optional(), "guidelines": t.string().optional()}
    ).named(renames["AppsDynamiteSharedGroupDetailsIn"])
    types["AppsDynamiteSharedGroupDetailsOut"] = t.struct(
        {
            "description": t.string().optional(),
            "guidelines": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedGroupDetailsOut"])
    types["AppsDynamiteV1ApiCompatV1ActionConfirmIn"] = t.struct(
        {
            "dismiss_text": t.string().optional(),
            "text": t.string().optional(),
            "ok_text": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionConfirmIn"])
    types["AppsDynamiteV1ApiCompatV1ActionConfirmOut"] = t.struct(
        {
            "dismiss_text": t.string().optional(),
            "text": t.string().optional(),
            "ok_text": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionConfirmOut"])
    types["SnippetIn"] = t.struct(
        {
            "matchRanges": t.array(t.proxy(renames["MatchRangeIn"])).optional(),
            "snippet": t.string().optional(),
        }
    ).named(renames["SnippetIn"])
    types["SnippetOut"] = t.struct(
        {
            "matchRanges": t.array(t.proxy(renames["MatchRangeOut"])).optional(),
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnippetOut"])
    types["AppsDynamiteStorageGridGridItemIn"] = t.struct(
        {
            "title": t.string().optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageComponentIn"]).optional(),
            "id": t.string().optional(),
            "subtitle": t.string().optional(),
            "layout": t.string().optional(),
            "textAlignment": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageGridGridItemIn"])
    types["AppsDynamiteStorageGridGridItemOut"] = t.struct(
        {
            "title": t.string().optional(),
            "image": t.proxy(
                renames["AppsDynamiteStorageImageComponentOut"]
            ).optional(),
            "id": t.string().optional(),
            "subtitle": t.string().optional(),
            "layout": t.string().optional(),
            "textAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageGridGridItemOut"])
    types["GoogleChatV1WidgetMarkupOpenLinkIn"] = t.struct(
        {"url": t.string().optional()}
    ).named(renames["GoogleChatV1WidgetMarkupOpenLinkIn"])
    types["GoogleChatV1WidgetMarkupOpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupOpenLinkOut"])
    types["IntegerPropertyOptionsIn"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsIn"]
            ).optional(),
            "minimumValue": t.string().optional(),
            "maximumValue": t.string().optional(),
            "operatorOptions": t.proxy(renames["IntegerOperatorOptionsIn"]).optional(),
        }
    ).named(renames["IntegerPropertyOptionsIn"])
    types["IntegerPropertyOptionsOut"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsOut"]
            ).optional(),
            "minimumValue": t.string().optional(),
            "maximumValue": t.string().optional(),
            "operatorOptions": t.proxy(renames["IntegerOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerPropertyOptionsOut"])
    types["MetadataIn"] = t.struct(
        {
            "owner": t.proxy(renames["PersonIn"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "displayOptions": t.proxy(renames["ResultDisplayMetadataIn"]).optional(),
            "objectType": t.string().optional(),
            "fields": t.array(t.proxy(renames["NamedPropertyIn"])).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "owner": t.proxy(renames["PersonOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "displayOptions": t.proxy(renames["ResultDisplayMetadataOut"]).optional(),
            "objectType": t.string().optional(),
            "fields": t.array(t.proxy(renames["NamedPropertyOut"])).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["FormattingIn"] = t.struct(
        {
            "underline": t.boolean(),
            "highlight": t.boolean().optional(),
            "italics": t.boolean(),
            "style": t.string().optional(),
            "bold": t.boolean(),
            "strikethrough": t.boolean(),
        }
    ).named(renames["FormattingIn"])
    types["FormattingOut"] = t.struct(
        {
            "underline": t.boolean(),
            "highlight": t.boolean().optional(),
            "italics": t.boolean(),
            "style": t.string().optional(),
            "bold": t.boolean(),
            "strikethrough": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormattingOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn"
    ] = t.struct(
        {
            "addonAttachments": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn"
                    ]
                )
            )
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn"
        ]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut"
    ] = t.struct(
        {
            "addonAttachments": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut"
        ]
    )
    types["SearchApplicationQueryStatsIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusIn"])),
        }
    ).named(renames["SearchApplicationQueryStatsIn"])
    types["SearchApplicationQueryStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationQueryStatsOut"])
    types["StreamingSessionInfoIn"] = t.struct(
        {
            "sessionId": t.string().optional(),
            "status": t.string().optional(),
            "viewerStats": t.proxy(renames["StreamViewerStatsIn"]).optional(),
            "viewerAccessPolicy": t.string().optional(),
            "trainingEnabled": t.boolean().optional(),
            "latestSessionEvent": t.proxy(renames["SessionEventIn"]).optional(),
            "ownerDisplayName": t.string().optional(),
            "applicationType": t.string().optional(),
        }
    ).named(renames["StreamingSessionInfoIn"])
    types["StreamingSessionInfoOut"] = t.struct(
        {
            "sessionId": t.string().optional(),
            "status": t.string().optional(),
            "viewerStats": t.proxy(renames["StreamViewerStatsOut"]).optional(),
            "viewerAccessPolicy": t.string().optional(),
            "trainingEnabled": t.boolean().optional(),
            "latestSessionEvent": t.proxy(renames["SessionEventOut"]).optional(),
            "ownerDisplayName": t.string().optional(),
            "applicationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSessionInfoOut"])
    types["AppsDynamiteSharedTextWithDescriptionIn"] = t.struct(
        {
            "textSegmentsWithDescription": t.array(
                t.proxy(renames["AppsDynamiteSharedTextSegmentsWithDescriptionIn"])
            ),
            "textBody": t.string(),
        }
    ).named(renames["AppsDynamiteSharedTextWithDescriptionIn"])
    types["AppsDynamiteSharedTextWithDescriptionOut"] = t.struct(
        {
            "textSegmentsWithDescription": t.array(
                t.proxy(renames["AppsDynamiteSharedTextSegmentsWithDescriptionOut"])
            ),
            "textBody": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTextWithDescriptionOut"])
    types["ImapSessionContextIn"] = t.struct(
        {
            "guidFingerprint": t.string().optional(),
            "os": t.string(),
            "osVersion": t.proxy(renames["OsVersionIn"]),
            "possiblyTrimmedModel": t.proxy(renames["PossiblyTrimmedModelIn"]),
            "deviceType": t.string().optional(),
            "app": t.string(),
        }
    ).named(renames["ImapSessionContextIn"])
    types["ImapSessionContextOut"] = t.struct(
        {
            "guidFingerprint": t.string().optional(),
            "os": t.string(),
            "osVersion": t.proxy(renames["OsVersionOut"]),
            "possiblyTrimmedModel": t.proxy(renames["PossiblyTrimmedModelOut"]),
            "deviceType": t.string().optional(),
            "app": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapSessionContextOut"])
    types["MeetingSpaceIn"] = t.struct(
        {
            "settings": t.proxy(renames["SettingsIn"]).optional(),
            "meetingSpaceId": t.string().optional(),
            "acceptedNumberClass": t.array(t.string()).optional(),
            "gatewaySipAccess": t.array(
                t.proxy(renames["GatewaySipAccessIn"])
            ).optional(),
            "universalPhoneAccess": t.proxy(
                renames["UniversalPhoneAccessIn"]
            ).optional(),
            "meetingCode": t.string().optional(),
            "broadcastAccess": t.proxy(renames["BroadcastAccessIn"]).optional(),
            "meetingAlias": t.string().optional(),
            "meetingUrl": t.string().optional(),
            "gatewayAccess": t.proxy(renames["GatewayAccessIn"]).optional(),
            "callInfo": t.proxy(renames["CallInfoIn"]).optional(),
            "phoneAccess": t.array(t.proxy(renames["PhoneAccessIn"])).optional(),
        }
    ).named(renames["MeetingSpaceIn"])
    types["MeetingSpaceOut"] = t.struct(
        {
            "settings": t.proxy(renames["SettingsOut"]).optional(),
            "meetingSpaceId": t.string().optional(),
            "acceptedNumberClass": t.array(t.string()).optional(),
            "gatewaySipAccess": t.array(
                t.proxy(renames["GatewaySipAccessOut"])
            ).optional(),
            "universalPhoneAccess": t.proxy(
                renames["UniversalPhoneAccessOut"]
            ).optional(),
            "meetingCode": t.string().optional(),
            "broadcastAccess": t.proxy(renames["BroadcastAccessOut"]).optional(),
            "meetingAlias": t.string().optional(),
            "meetingUrl": t.string().optional(),
            "moreJoinUrl": t.string().optional(),
            "gatewayAccess": t.proxy(renames["GatewayAccessOut"]).optional(),
            "callInfo": t.proxy(renames["CallInfoOut"]).optional(),
            "phoneAccess": t.array(t.proxy(renames["PhoneAccessOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeetingSpaceOut"])
    types["AppsDynamiteStorageCardIn"] = t.struct(
        {
            "sections": t.array(
                t.proxy(renames["AppsDynamiteStorageCardSectionIn"])
            ).optional(),
            "header": t.proxy(
                renames["AppsDynamiteStorageCardCardHeaderIn"]
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["AppsDynamiteStorageCardCardActionIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageCardIn"])
    types["AppsDynamiteStorageCardOut"] = t.struct(
        {
            "sections": t.array(
                t.proxy(renames["AppsDynamiteStorageCardSectionOut"])
            ).optional(),
            "header": t.proxy(
                renames["AppsDynamiteStorageCardCardHeaderOut"]
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["AppsDynamiteStorageCardCardActionOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardOut"])
    types["PushItemRequestIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "item": t.proxy(renames["PushItemIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["PushItemRequestIn"])
    types["PushItemRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "item": t.proxy(renames["PushItemOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushItemRequestOut"])
    types["ScoringConfigIn"] = t.struct(
        {
            "disablePersonalization": t.boolean().optional(),
            "disableFreshness": t.boolean().optional(),
        }
    ).named(renames["ScoringConfigIn"])
    types["ScoringConfigOut"] = t.struct(
        {
            "disablePersonalization": t.boolean().optional(),
            "disableFreshness": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScoringConfigOut"])
    types["SheetsClientActionMarkupIn"] = t.struct(
        {
            "customFunctionReturnValueMarkup": t.proxy(
                renames["CustomFunctionReturnValueMarkupIn"]
            )
        }
    ).named(renames["SheetsClientActionMarkupIn"])
    types["SheetsClientActionMarkupOut"] = t.struct(
        {
            "customFunctionReturnValueMarkup": t.proxy(
                renames["CustomFunctionReturnValueMarkupOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SheetsClientActionMarkupOut"])
    types["ResultCountsIn"] = t.struct(
        {
            "sourceResultCounts": t.array(
                t.proxy(renames["SourceResultCountIn"])
            ).optional()
        }
    ).named(renames["ResultCountsIn"])
    types["ResultCountsOut"] = t.struct(
        {
            "sourceResultCounts": t.array(
                t.proxy(renames["SourceResultCountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultCountsOut"])
    types["DriveMetadataIn"] = t.struct(
        {
            "id": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
            "externalMimetype": t.string().optional(),
            "canView": t.boolean().optional(),
            "canEdit": t.boolean().optional(),
            "aclFixRequest": t.proxy(renames["AclFixRequestIn"]),
            "thumbnailHeight": t.integer().optional(),
            "isOwner": t.boolean().optional(),
            "title": t.string().optional(),
            "mimetype": t.string().optional(),
            "wrappedResourceKey": t.proxy(renames["WrappedResourceKeyIn"]).optional(),
            "driveAction": t.string().optional(),
            "encryptedResourceKey": t.string().optional(),
            "driveState": t.string(),
            "aclFixStatus": t.proxy(renames["AclFixStatusIn"]),
            "legacyUploadMetadata": t.proxy(
                renames["LegacyUploadMetadataIn"]
            ).optional(),
            "isDownloadRestricted": t.boolean().optional(),
            "encryptedDocId": t.boolean().optional(),
            "urlFragment": t.string().optional(),
            "thumbnailWidth": t.integer().optional(),
            "shortcutAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdIn"]
            ).optional(),
            "canShare": t.boolean().optional(),
            "organizationDisplayName": t.string().optional(),
        }
    ).named(renames["DriveMetadataIn"])
    types["DriveMetadataOut"] = t.struct(
        {
            "id": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
            "externalMimetype": t.string().optional(),
            "canView": t.boolean().optional(),
            "canEdit": t.boolean().optional(),
            "aclFixRequest": t.proxy(renames["AclFixRequestOut"]),
            "thumbnailHeight": t.integer().optional(),
            "isOwner": t.boolean().optional(),
            "title": t.string().optional(),
            "mimetype": t.string().optional(),
            "wrappedResourceKey": t.proxy(renames["WrappedResourceKeyOut"]).optional(),
            "driveAction": t.string().optional(),
            "encryptedResourceKey": t.string().optional(),
            "driveState": t.string(),
            "aclFixStatus": t.proxy(renames["AclFixStatusOut"]),
            "legacyUploadMetadata": t.proxy(
                renames["LegacyUploadMetadataOut"]
            ).optional(),
            "isDownloadRestricted": t.boolean().optional(),
            "encryptedDocId": t.boolean().optional(),
            "embedUrl": t.proxy(renames["TrustedResourceUrlProtoOut"]).optional(),
            "urlFragment": t.string().optional(),
            "thumbnailWidth": t.integer().optional(),
            "shortcutAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdOut"]
            ).optional(),
            "canShare": t.boolean().optional(),
            "organizationDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveMetadataOut"])
    types["IndexItemRequestIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "item": t.proxy(renames["ItemIn"]).optional(),
            "connectorName": t.string().optional(),
            "mode": t.string(),
            "indexItemOptions": t.proxy(renames["IndexItemOptionsIn"]),
        }
    ).named(renames["IndexItemRequestIn"])
    types["IndexItemRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "item": t.proxy(renames["ItemOut"]).optional(),
            "connectorName": t.string().optional(),
            "mode": t.string(),
            "indexItemOptions": t.proxy(renames["IndexItemOptionsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexItemRequestOut"])
    types["GatewayAccessIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["GatewayAccessIn"]
    )
    types["GatewayAccessOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayAccessOut"])
    types["ConsentedAppUnfurlMetadataIn"] = t.struct(
        {"clientSpecifiedAppId": t.proxy(renames["UserIdIn"]).optional()}
    ).named(renames["ConsentedAppUnfurlMetadataIn"])
    types["ConsentedAppUnfurlMetadataOut"] = t.struct(
        {
            "clientSpecifiedAppId": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentedAppUnfurlMetadataOut"])
    types["AttachmentIn"] = t.struct(
        {
            "cardAddOnData": t.proxy(renames["AppsDynamiteStorageCardIn"]).optional(),
            "attachmentId": t.string().optional(),
            "deprecatedAddOnData": t.proxy(
                renames["ContextualAddOnMarkupIn"]
            ).optional(),
            "appId": t.proxy(renames["UserIdIn"]).optional(),
            "slackData": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1AttachmentIn"]
            ).optional(),
            "slackDataImageUrlHeight": t.integer().optional(),
            "addOnData": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupIn"]
            ).optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "cardAddOnData": t.proxy(renames["AppsDynamiteStorageCardOut"]).optional(),
            "attachmentId": t.string().optional(),
            "deprecatedAddOnData": t.proxy(
                renames["ContextualAddOnMarkupOut"]
            ).optional(),
            "appId": t.proxy(renames["UserIdOut"]).optional(),
            "slackData": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1AttachmentOut"]
            ).optional(),
            "slackDataImageUrlHeight": t.integer().optional(),
            "addOnData": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["UserInfoIn"] = t.struct(
        {
            "updaterToShowGaiaId": t.string().optional(),
            "updaterToShowUserId": t.proxy(renames["UserIdIn"]).optional(),
            "updaterToShowEmail": t.string().optional(),
            "driveNotificationAvatarUrl": t.string().optional(),
            "updaterCountDisplayType": t.string().optional(),
            "updaterCountToShow": t.integer().optional(),
            "updaterToShowName": t.string().optional(),
        }
    ).named(renames["UserInfoIn"])
    types["UserInfoOut"] = t.struct(
        {
            "updaterToShowGaiaId": t.string().optional(),
            "updaterToShowUserId": t.proxy(renames["UserIdOut"]).optional(),
            "updaterToShowEmail": t.string().optional(),
            "driveNotificationAvatarUrl": t.string().optional(),
            "updaterCountDisplayType": t.string().optional(),
            "updaterCountToShow": t.integer().optional(),
            "updaterToShowName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
    types["AppsDynamiteStorageImageCropStyleIn"] = t.struct(
        {"type": t.string().optional(), "aspectRatio": t.number().optional()}
    ).named(renames["AppsDynamiteStorageImageCropStyleIn"])
    types["AppsDynamiteStorageImageCropStyleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageCropStyleOut"])
    types["SourceResultCountIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "resultCountEstimate": t.string().optional(),
            "resultCountExact": t.string().optional(),
            "hasMoreResults": t.boolean().optional(),
        }
    ).named(renames["SourceResultCountIn"])
    types["SourceResultCountOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "resultCountEstimate": t.string().optional(),
            "resultCountExact": t.string().optional(),
            "hasMoreResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceResultCountOut"])
    types["BroadcastStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["BroadcastStatsIn"])
    types["BroadcastStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BroadcastStatsOut"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataIn"] = t.struct(
        {
            "calendarEvent": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn"]
            ),
            "eventCreation": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataIn"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataOut"] = t.struct(
        {
            "calendarEvent": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut"]
            ),
            "eventCreation": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataOut"])
    types["AppsDynamiteStorageDecoratedTextSwitchControlIn"] = t.struct(
        {
            "controlType": t.string().optional(),
            "value": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "selected": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextSwitchControlIn"])
    types["AppsDynamiteStorageDecoratedTextSwitchControlOut"] = t.struct(
        {
            "controlType": t.string().optional(),
            "value": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "selected": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextSwitchControlOut"])
    types["TypeInfoIn"] = t.struct(
        {"videoInfo": t.proxy(renames["VideoInfoIn"]).optional()}
    ).named(renames["TypeInfoIn"])
    types["TypeInfoOut"] = t.struct(
        {
            "videoInfo": t.proxy(renames["VideoInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeInfoOut"])
    types["ReferencesIn"] = t.struct(
        {"references": t.array(t.proxy(renames["ReferenceIn"]))}
    ).named(renames["ReferencesIn"])
    types["ReferencesOut"] = t.struct(
        {
            "references": t.array(t.proxy(renames["ReferenceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferencesOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"] = t.struct(
        {"replyType": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut"] = t.struct(
        {
            "replyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut"])
    types["HtmlValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["HtmlValuesIn"]
    )
    types["HtmlValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlValuesOut"])
    types["ThreadKeySetIn"] = t.struct(
        {
            "newThreadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])).optional(),
        }
    ).named(renames["ThreadKeySetIn"])
    types["ThreadKeySetOut"] = t.struct(
        {
            "newThreadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThreadKeySetOut"])
    types["WidgetMarkupIn"] = t.struct(
        {
            "keyValue": t.proxy(renames["KeyValueIn"]),
            "selectionControl": t.proxy(renames["SelectionControlIn"]),
            "image": t.proxy(renames["ImageIn"]),
            "horizontalAlignment": t.string().optional(),
            "divider": t.proxy(renames["DividerIn"]),
            "textField": t.proxy(renames["TextFieldIn"]),
            "imageKeyValue": t.proxy(renames["ImageKeyValueIn"]),
            "textKeyValue": t.proxy(renames["TextKeyValueIn"]),
            "textParagraph": t.proxy(renames["TextParagraphIn"]).optional(),
            "menu": t.proxy(renames["MenuIn"]).optional(),
            "dateTimePicker": t.proxy(renames["DateTimePickerIn"]),
            "buttons": t.array(t.proxy(renames["ButtonIn"])).optional(),
            "grid": t.proxy(renames["GridIn"]),
        }
    ).named(renames["WidgetMarkupIn"])
    types["WidgetMarkupOut"] = t.struct(
        {
            "keyValue": t.proxy(renames["KeyValueOut"]),
            "selectionControl": t.proxy(renames["SelectionControlOut"]),
            "image": t.proxy(renames["ImageOut"]),
            "horizontalAlignment": t.string().optional(),
            "divider": t.proxy(renames["DividerOut"]),
            "textField": t.proxy(renames["TextFieldOut"]),
            "imageKeyValue": t.proxy(renames["ImageKeyValueOut"]),
            "textKeyValue": t.proxy(renames["TextKeyValueOut"]),
            "textParagraph": t.proxy(renames["TextParagraphOut"]).optional(),
            "menu": t.proxy(renames["MenuOut"]).optional(),
            "dateTimePicker": t.proxy(renames["DateTimePickerOut"]),
            "buttons": t.array(t.proxy(renames["ButtonOut"])).optional(),
            "grid": t.proxy(renames["GridOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WidgetMarkupOut"])
    types["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"] = t.struct(
        {"meetingUrl": t.string()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut"] = t.struct(
        {
            "meetingUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["OtrChatMessageEventIn"] = t.struct(
        {
            "messageOtrStatus": t.string(),
            "expirationTimestampUsec": t.string(),
            "kansasVersionInfo": t.string(),
            "kansasRowId": t.string(),
        }
    ).named(renames["OtrChatMessageEventIn"])
    types["OtrChatMessageEventOut"] = t.struct(
        {
            "messageOtrStatus": t.string(),
            "expirationTimestampUsec": t.string(),
            "kansasVersionInfo": t.string(),
            "kansasRowId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtrChatMessageEventOut"])
    types["EnumValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["EnumValuesIn"]
    )
    types["EnumValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValuesOut"])
    types["SessionStateInfoIn"] = t.struct(
        {
            "sessionState": t.string().optional(),
            "languageConfig": t.proxy(renames["LanguageConfigIn"]).optional(),
        }
    ).named(renames["SessionStateInfoIn"])
    types["SessionStateInfoOut"] = t.struct(
        {
            "lastActorDeviceId": t.string().optional(),
            "sessionState": t.string().optional(),
            "maxEndTime": t.string().optional(),
            "ackInfo": t.proxy(renames["AckInfoOut"]).optional(),
            "sessionStopReason": t.string().optional(),
            "languageConfig": t.proxy(renames["LanguageConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionStateInfoOut"])
    types["AppsDynamiteStorageColumnsIn"] = t.struct(
        {
            "wrapStyle": t.string().optional(),
            "columnItems": t.array(
                t.proxy(renames["AppsDynamiteStorageColumnsColumnIn"])
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsIn"])
    types["AppsDynamiteStorageColumnsOut"] = t.struct(
        {
            "wrapStyle": t.string().optional(),
            "columnItems": t.array(
                t.proxy(renames["AppsDynamiteStorageColumnsColumnOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsOut"])
    types["UserIdIn"] = t.struct(
        {
            "actingUserId": t.string().optional(),
            "originAppId": t.proxy(renames["AppIdIn"]).optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["UserIdIn"])
    types["UserIdOut"] = t.struct(
        {
            "actingUserId": t.string().optional(),
            "originAppId": t.proxy(renames["AppIdOut"]).optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserIdOut"])
    types["AppsDynamiteSharedGroupVisibilityIn"] = t.struct(
        {"state": t.string()}
    ).named(renames["AppsDynamiteSharedGroupVisibilityIn"])
    types["AppsDynamiteSharedGroupVisibilityOut"] = t.struct(
        {"state": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedGroupVisibilityOut"])
    types["AppsDynamiteSharedUserBlockRelationshipIn"] = t.struct(
        {"isBlockedByRequester": t.boolean(), "hasBlockedRequester": t.boolean()}
    ).named(renames["AppsDynamiteSharedUserBlockRelationshipIn"])
    types["AppsDynamiteSharedUserBlockRelationshipOut"] = t.struct(
        {
            "isBlockedByRequester": t.boolean(),
            "hasBlockedRequester": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedUserBlockRelationshipOut"])
    types["UnmappedIdentityIn"] = t.struct(
        {
            "resolutionStatusCode": t.string().optional(),
            "externalIdentity": t.proxy(renames["PrincipalIn"]).optional(),
        }
    ).named(renames["UnmappedIdentityIn"])
    types["UnmappedIdentityOut"] = t.struct(
        {
            "resolutionStatusCode": t.string().optional(),
            "externalIdentity": t.proxy(renames["PrincipalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmappedIdentityOut"])
    types["GroupRetentionSettingsUpdatedMetaDataIn"] = t.struct(
        {
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsIn"]
            ).optional(),
            "initiator": t.proxy(renames["UserIdIn"]).optional(),
        }
    ).named(renames["GroupRetentionSettingsUpdatedMetaDataIn"])
    types["GroupRetentionSettingsUpdatedMetaDataOut"] = t.struct(
        {
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsOut"]
            ).optional(),
            "initiator": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupRetentionSettingsUpdatedMetaDataOut"])
    types["SafeUrlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeUrlWrappedValue": t.string().optional()}
    ).named(renames["SafeUrlProtoIn"])
    types["SafeUrlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeUrlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeUrlProtoOut"])
    types["MessageParentIdIn"] = t.struct(
        {"topicId": t.proxy(renames["TopicIdIn"]).optional()}
    ).named(renames["MessageParentIdIn"])
    types["MessageParentIdOut"] = t.struct(
        {
            "topicId": t.proxy(renames["TopicIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageParentIdOut"])
    types["ImapUpdateIn"] = t.struct(
        {"imapUidsReassign": t.proxy(renames["ImapUidsReassignIn"])}
    ).named(renames["ImapUpdateIn"])
    types["ImapUpdateOut"] = t.struct(
        {
            "imapUidsReassign": t.proxy(renames["ImapUidsReassignOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapUpdateOut"])
    types["PropertyDisplayOptionsIn"] = t.struct(
        {"displayLabel": t.string().optional()}
    ).named(renames["PropertyDisplayOptionsIn"])
    types["PropertyDisplayOptionsOut"] = t.struct(
        {
            "displayLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyDisplayOptionsOut"])
    types["SearchItemsByViewUrlRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "viewUrl": t.string().optional(),
        }
    ).named(renames["SearchItemsByViewUrlRequestIn"])
    types["SearchItemsByViewUrlRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "viewUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchItemsByViewUrlRequestOut"])
    types["AppsDynamiteSharedSpaceInfoIn"] = t.struct(
        {
            "isExternal": t.boolean().optional(),
            "userMembershipState": t.string().optional(),
            "groupId": t.proxy(renames["GroupIdIn"]),
            "avatarInfo": t.proxy(renames["AppsDynamiteSharedAvatarInfoIn"]),
            "avatarUrl": t.string(),
            "description": t.string(),
            "numMembers": t.integer().optional(),
            "inviterEmail": t.string().optional(),
            "name": t.string(),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedSpaceInfoIn"])
    types["AppsDynamiteSharedSpaceInfoOut"] = t.struct(
        {
            "isExternal": t.boolean().optional(),
            "userMembershipState": t.string().optional(),
            "groupId": t.proxy(renames["GroupIdOut"]),
            "avatarInfo": t.proxy(renames["AppsDynamiteSharedAvatarInfoOut"]),
            "avatarUrl": t.string(),
            "description": t.string(),
            "numMembers": t.integer().optional(),
            "inviterEmail": t.string().optional(),
            "name": t.string(),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedSpaceInfoOut"])
    types["GoogleDocsResultInfoIn"] = t.struct(
        {
            "encryptedId": t.string().optional(),
            "mimeType": t.string().optional(),
            "cosmoNameSpace": t.integer().optional(),
            "shareScope": t.proxy(renames["ShareScopeIn"]).optional(),
            "cosmoId": t.proxy(renames["IdIn"]).optional(),
            "attachmentSha1": t.string().optional(),
        }
    ).named(renames["GoogleDocsResultInfoIn"])
    types["GoogleDocsResultInfoOut"] = t.struct(
        {
            "encryptedId": t.string().optional(),
            "mimeType": t.string().optional(),
            "cosmoNameSpace": t.integer().optional(),
            "shareScope": t.proxy(renames["ShareScopeOut"]).optional(),
            "cosmoId": t.proxy(renames["IdOut"]).optional(),
            "attachmentSha1": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDocsResultInfoOut"])
    types["ContactGroupProtoIn"] = t.struct(
        {
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "groupId": t.string().optional(),
            "ownerGaiaId": t.string(),
        }
    ).named(renames["ContactGroupProtoIn"])
    types["ContactGroupProtoOut"] = t.struct(
        {
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "groupId": t.string().optional(),
            "ownerGaiaId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupProtoOut"])
    types["UserDisplayInfoIn"] = t.struct(
        {"avatarUrl": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["UserDisplayInfoIn"])
    types["UserDisplayInfoOut"] = t.struct(
        {
            "avatarUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDisplayInfoOut"])
    types["CollaborationIn"] = t.struct(
        {
            "attachmentId": t.string().optional(),
            "initiator": t.proxy(renames["UserDisplayInfoIn"]).optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["CollaborationIn"])
    types["CollaborationOut"] = t.struct(
        {
            "attachmentId": t.string().optional(),
            "initiator": t.proxy(renames["UserDisplayInfoOut"]).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollaborationOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["TopicIdIn"] = t.struct(
        {
            "groupId": t.proxy(renames["GroupIdIn"]).optional(),
            "topicId": t.string().optional(),
        }
    ).named(renames["TopicIdIn"])
    types["TopicIdOut"] = t.struct(
        {
            "groupId": t.proxy(renames["GroupIdOut"]).optional(),
            "topicId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicIdOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn"
    ] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "title": t.string().optional(),
            "resourceUrl": t.string(),
            "mimeType": t.string().optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn"
        ]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut"
    ] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "title": t.string().optional(),
            "resourceUrl": t.string(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut"
        ]
    )
    types["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn"] = t.struct(
        {
            "endTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn"
                ]
            ).optional(),
            "startTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn"
                ]
            ).optional(),
            "eventId": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut"] = t.struct(
        {
            "endTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut"
                ]
            ).optional(),
            "startTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut"
                ]
            ).optional(),
            "eventId": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut"])
    types["OpenLinkIn"] = t.struct(
        {
            "openAs": t.string(),
            "onClose": t.string(),
            "loadIndicator": t.string().optional(),
            "url": t.string(),
        }
    ).named(renames["OpenLinkIn"])
    types["OpenLinkOut"] = t.struct(
        {
            "openAs": t.string(),
            "onClose": t.string(),
            "loadIndicator": t.string().optional(),
            "url": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenLinkOut"])
    types["AppsDynamiteSharedAssistantSuggestionIn"] = t.struct(
        {
            "debugContext": t.proxy(
                renames["AppsDynamiteSharedAssistantDebugContextIn"]
            ).optional(),
            "serializedSuggestions": t.string().optional(),
            "findDocumentSuggestion": t.proxy(
                renames["AppsDynamiteSharedFindDocumentSuggestionIn"]
            ).optional(),
            "sessionContext": t.proxy(
                renames["AppsDynamiteSharedAssistantSessionContextIn"]
            ).optional(),
            "feedbackContext": t.proxy(
                renames["AppsDynamiteSharedAssistantFeedbackContextIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSuggestionIn"])
    types["AppsDynamiteSharedAssistantSuggestionOut"] = t.struct(
        {
            "debugContext": t.proxy(
                renames["AppsDynamiteSharedAssistantDebugContextOut"]
            ).optional(),
            "serializedSuggestions": t.string().optional(),
            "findDocumentSuggestion": t.proxy(
                renames["AppsDynamiteSharedFindDocumentSuggestionOut"]
            ).optional(),
            "sessionContext": t.proxy(
                renames["AppsDynamiteSharedAssistantSessionContextOut"]
            ).optional(),
            "feedbackContext": t.proxy(
                renames["AppsDynamiteSharedAssistantFeedbackContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSuggestionOut"])
    types["AppsDynamiteStorageDateTimePickerIn"] = t.struct(
        {
            "label": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "valueMsEpoch": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageDateTimePickerIn"])
    types["AppsDynamiteStorageDateTimePickerOut"] = t.struct(
        {
            "label": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "valueMsEpoch": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDateTimePickerOut"])
    types["UpdateBodyIn"] = t.struct(
        {
            "insertContents": t.array(t.proxy(renames["InsertContentIn"])).optional(),
            "type": t.string(),
        }
    ).named(renames["UpdateBodyIn"])
    types["UpdateBodyOut"] = t.struct(
        {
            "insertContents": t.array(t.proxy(renames["InsertContentOut"])).optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBodyOut"])
    types["ObjectPropertyOptionsIn"] = t.struct(
        {
            "subobjectProperties": t.array(
                t.proxy(renames["PropertyDefinitionIn"])
            ).optional()
        }
    ).named(renames["ObjectPropertyOptionsIn"])
    types["ObjectPropertyOptionsOut"] = t.struct(
        {
            "subobjectProperties": t.array(
                t.proxy(renames["PropertyDefinitionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectPropertyOptionsOut"])
    types["AppsDynamiteSharedDimensionIn"] = t.struct(
        {"width": t.integer(), "height": t.integer()}
    ).named(renames["AppsDynamiteSharedDimensionIn"])
    types["AppsDynamiteSharedDimensionOut"] = t.struct(
        {
            "width": t.integer(),
            "height": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedDimensionOut"])
    types["RankIn"] = t.struct(
        {"secondary": t.string().optional(), "primary": t.string().optional()}
    ).named(renames["RankIn"])
    types["RankOut"] = t.struct(
        {
            "secondary": t.string().optional(),
            "primary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RankOut"])
    types["PrefUpdateIn"] = t.struct(
        {
            "preState": t.proxy(renames["FuseboxPrefUpdatePreStateIn"]),
            "prefDeleted": t.proxy(renames["PrefDeletedIn"]),
            "prefWritten": t.proxy(renames["PrefWrittenIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["PrefUpdateIn"])
    types["PrefUpdateOut"] = t.struct(
        {
            "preState": t.proxy(renames["FuseboxPrefUpdatePreStateOut"]),
            "prefDeleted": t.proxy(renames["PrefDeletedOut"]),
            "prefWritten": t.proxy(renames["PrefWrittenOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrefUpdateOut"])
    types["QuotedMessageMetadataIn"] = t.struct(
        {
            "messageId": t.proxy(renames["MessageIdIn"]).optional(),
            "lastUpdateTimeWhenQuotedMicros": t.string().optional(),
        }
    ).named(renames["QuotedMessageMetadataIn"])
    types["QuotedMessageMetadataOut"] = t.struct(
        {
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "textBody": t.string().optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataOut"])).optional(),
            "updaterId": t.proxy(renames["UserIdOut"]).optional(),
            "messageId": t.proxy(renames["MessageIdOut"]).optional(),
            "lastEditTimeMicros": t.string().optional(),
            "lastUpdateTimeWhenQuotedMicros": t.string().optional(),
            "botAttachmentState": t.string().optional(),
            "messageState": t.string().optional(),
            "creatorId": t.proxy(renames["UserIdOut"]).optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsOut"]
            ).optional(),
            "createTimeMicros": t.string().optional(),
            "appProfile": t.proxy(
                renames["AppsDynamiteSharedAppProfileOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotedMessageMetadataOut"])
    types["UpdateSchemaRequestIn"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaIn"]).optional(),
            "validateOnly": t.boolean().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["UpdateSchemaRequestIn"])
    types["UpdateSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]).optional(),
            "validateOnly": t.boolean().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSchemaRequestOut"])
    types["BorderStyleIn"] = t.struct(
        {
            "strokeColor": t.string().optional(),
            "cornerRadius": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["BorderStyleIn"])
    types["BorderStyleOut"] = t.struct(
        {
            "strokeColor": t.string().optional(),
            "cornerRadius": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BorderStyleOut"])
    types["StartUploadItemRequestIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["StartUploadItemRequestIn"])
    types["StartUploadItemRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartUploadItemRequestOut"])
    types["ItemCountByStatusIn"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "count": t.string().optional(),
            "indexedItemsCount": t.string().optional(),
        }
    ).named(renames["ItemCountByStatusIn"])
    types["ItemCountByStatusOut"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "count": t.string().optional(),
            "indexedItemsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemCountByStatusOut"])
    types["InteractionDataIn"] = t.struct(
        {"url": t.proxy(renames["SafeUrlProtoIn"]).optional()}
    ).named(renames["InteractionDataIn"])
    types["InteractionDataOut"] = t.struct(
        {
            "url": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InteractionDataOut"])
    types["ImageButtonIn"] = t.struct(
        {
            "name": t.string(),
            "icon": t.string(),
            "onClick": t.proxy(renames["OnClickIn"]),
            "iconUrl": t.string(),
        }
    ).named(renames["ImageButtonIn"])
    types["ImageButtonOut"] = t.struct(
        {
            "name": t.string(),
            "icon": t.string(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "iconUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageButtonOut"])
    types["ContextAttributeIn"] = t.struct(
        {"name": t.string().optional(), "values": t.array(t.string()).optional()}
    ).named(renames["ContextAttributeIn"])
    types["ContextAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextAttributeOut"])
    types["BooleanOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["BooleanOperatorOptionsIn"])
    types["BooleanOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanOperatorOptionsOut"])
    types["OsVersionIn"] = t.struct(
        {
            "tertiaryVersion": t.integer(),
            "majorVersion": t.integer(),
            "minorVersion": t.integer(),
        }
    ).named(renames["OsVersionIn"])
    types["OsVersionOut"] = t.struct(
        {
            "tertiaryVersion": t.integer(),
            "majorVersion": t.integer(),
            "minorVersion": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsVersionOut"])
    types["ItemStructuredDataIn"] = t.struct(
        {
            "hash": t.string().optional(),
            "object": t.proxy(renames["StructuredDataObjectIn"]).optional(),
        }
    ).named(renames["ItemStructuredDataIn"])
    types["ItemStructuredDataOut"] = t.struct(
        {
            "hash": t.string().optional(),
            "object": t.proxy(renames["StructuredDataObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemStructuredDataOut"])
    types["DividerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DividerIn"]
    )
    types["DividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DividerOut"])
    types["PushItemIn"] = t.struct(
        {
            "repositoryError": t.proxy(renames["RepositoryErrorIn"]).optional(),
            "queue": t.string().optional(),
            "type": t.string().optional(),
            "metadataHash": t.string().optional(),
            "payload": t.string().optional(),
            "structuredDataHash": t.string().optional(),
            "contentHash": t.string().optional(),
        }
    ).named(renames["PushItemIn"])
    types["PushItemOut"] = t.struct(
        {
            "repositoryError": t.proxy(renames["RepositoryErrorOut"]).optional(),
            "queue": t.string().optional(),
            "type": t.string().optional(),
            "metadataHash": t.string().optional(),
            "payload": t.string().optional(),
            "structuredDataHash": t.string().optional(),
            "contentHash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushItemOut"])
    types["AppsDynamiteSharedCardClickSuggestionIn"] = t.struct(
        {
            "actionId": t.string().optional(),
            "suggestionMessageId": t.proxy(renames["MessageIdIn"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCardClickSuggestionIn"])
    types["AppsDynamiteSharedCardClickSuggestionOut"] = t.struct(
        {
            "actionId": t.string().optional(),
            "suggestionMessageId": t.proxy(renames["MessageIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCardClickSuggestionOut"])
    types["StoredParticipantIdIn"] = t.struct({"gaiaId": t.string()}).named(
        renames["StoredParticipantIdIn"]
    )
    types["StoredParticipantIdOut"] = t.struct(
        {"gaiaId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StoredParticipantIdOut"])
    types["AppsDynamiteSharedCallAnnotationDataIn"] = t.struct(
        {
            "callMetadata": t.proxy(renames["AppsDynamiteSharedCallMetadataIn"]),
            "callStatus": t.string(),
            "callEndedTimestamp": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedCallAnnotationDataIn"])
    types["AppsDynamiteSharedCallAnnotationDataOut"] = t.struct(
        {
            "callMetadata": t.proxy(renames["AppsDynamiteSharedCallMetadataOut"]),
            "callStatus": t.string(),
            "callEndedTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCallAnnotationDataOut"])
    types["TriggerIn"] = t.struct(
        {
            "rpcOptions": t.proxy(renames["RpcOptionsIn"]),
            "dispatcher": t.string().optional(),
            "triggerAction": t.proxy(renames["TriggerActionIn"]).optional(),
            "fireTimeUs": t.string().optional(),
            "actionType": t.integer().optional(),
            "triggerKey": t.proxy(renames["TriggerKeyIn"]).optional(),
            "dispatchId": t.integer().optional(),
            "batchTimeUs": t.string().optional(),
            "sliceFireTimeUs": t.string().optional(),
            "jobsettedServerSpec": t.proxy(renames["JobsettedServerSpecIn"]).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "rpcOptions": t.proxy(renames["RpcOptionsOut"]),
            "dispatcher": t.string().optional(),
            "triggerAction": t.proxy(renames["TriggerActionOut"]).optional(),
            "fireTimeUs": t.string().optional(),
            "actionType": t.integer().optional(),
            "triggerKey": t.proxy(renames["TriggerKeyOut"]).optional(),
            "dispatchId": t.integer().optional(),
            "batchTimeUs": t.string().optional(),
            "sliceFireTimeUs": t.string().optional(),
            "jobsettedServerSpec": t.proxy(
                renames["JobsettedServerSpecOut"]
            ).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["UnreserveItemsRequestIn"] = t.struct(
        {
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["UnreserveItemsRequestIn"])
    types["UnreserveItemsRequestOut"] = t.struct(
        {
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnreserveItemsRequestOut"])
    types["DynamiteSpacesScoringInfoIn"] = t.struct(
        {
            "lastReadTimestampSecs": t.string(),
            "spaceAgeInDays": t.number(),
            "topicalityScore": t.number(),
            "freshnessScore": t.number(),
            "numAucContacts": t.string(),
            "contactsIntersectionCount": t.number(),
            "smallUnjoinedSpacesAffinityScore": t.number(),
            "lastMessagePostedTimestampSecs": t.string(),
            "spaceCreationTimestampSecs": t.string(),
            "messageScore": t.number(),
            "commonContactCountAffinityScore": t.number(),
            "smallContactListAffinityScore": t.number(),
            "affinityScore": t.number(),
            "memberMetadataCount": t.number(),
            "finalScore": t.number(),
            "memberCountScore": t.number(),
            "joinedSpacesAffinityScore": t.number(),
        }
    ).named(renames["DynamiteSpacesScoringInfoIn"])
    types["DynamiteSpacesScoringInfoOut"] = t.struct(
        {
            "lastReadTimestampSecs": t.string(),
            "spaceAgeInDays": t.number(),
            "topicalityScore": t.number(),
            "freshnessScore": t.number(),
            "numAucContacts": t.string(),
            "contactsIntersectionCount": t.number(),
            "smallUnjoinedSpacesAffinityScore": t.number(),
            "lastMessagePostedTimestampSecs": t.string(),
            "spaceCreationTimestampSecs": t.string(),
            "messageScore": t.number(),
            "commonContactCountAffinityScore": t.number(),
            "smallContactListAffinityScore": t.number(),
            "affinityScore": t.number(),
            "memberMetadataCount": t.number(),
            "finalScore": t.number(),
            "memberCountScore": t.number(),
            "joinedSpacesAffinityScore": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamiteSpacesScoringInfoOut"])
    types["MenuIn"] = t.struct(
        {
            "label": t.string().optional(),
            "name": t.string().optional(),
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
            "items": t.array(t.proxy(renames["MenuItemIn"])),
        }
    ).named(renames["MenuIn"])
    types["MenuOut"] = t.struct(
        {
            "label": t.string().optional(),
            "name": t.string().optional(),
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "items": t.array(t.proxy(renames["MenuItemOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MenuOut"])
    types["ListItemsResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListItemsResponseIn"])
    types["ListItemsResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemsResponseOut"])
    types["RecipientIn"] = t.struct({"email": t.string()}).named(renames["RecipientIn"])
    types["RecipientOut"] = t.struct(
        {"email": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RecipientOut"])
    types["ItemIn"] = t.struct(
        {
            "payload": t.string().optional(),
            "acl": t.proxy(renames["ItemAclIn"]).optional(),
            "metadata": t.proxy(renames["ItemMetadataIn"]).optional(),
            "name": t.string().optional(),
            "structuredData": t.proxy(renames["ItemStructuredDataIn"]).optional(),
            "queue": t.string().optional(),
            "version": t.string(),
            "itemType": t.string().optional(),
            "status": t.proxy(renames["ItemStatusIn"]).optional(),
            "content": t.proxy(renames["ItemContentIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "payload": t.string().optional(),
            "acl": t.proxy(renames["ItemAclOut"]).optional(),
            "metadata": t.proxy(renames["ItemMetadataOut"]).optional(),
            "name": t.string().optional(),
            "structuredData": t.proxy(renames["ItemStructuredDataOut"]).optional(),
            "queue": t.string().optional(),
            "version": t.string(),
            "itemType": t.string().optional(),
            "status": t.proxy(renames["ItemStatusOut"]).optional(),
            "content": t.proxy(renames["ItemContentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["FolderIn"] = t.struct(
        {
            "id": t.string().optional(),
            "message": t.array(
                t.proxy(renames["ImapsyncFolderAttributeFolderMessageIn"])
            ).optional(),
        }
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "id": t.string().optional(),
            "message": t.array(
                t.proxy(renames["ImapsyncFolderAttributeFolderMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["SegmentIn"] = t.struct(
        {
            "text": t.string().optional(),
            "userMentionData": t.proxy(renames["UserMentionDataIn"]).optional(),
            "formatting": t.proxy(renames["FormattingIn"]).optional(),
            "type": t.string().optional(),
            "hashtagData": t.proxy(renames["HashtagDataIn"]).optional(),
            "linkData": t.proxy(renames["LinkDataIn"]).optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "text": t.string().optional(),
            "userMentionData": t.proxy(renames["UserMentionDataOut"]).optional(),
            "formatting": t.proxy(renames["FormattingOut"]).optional(),
            "type": t.string().optional(),
            "hashtagData": t.proxy(renames["HashtagDataOut"]).optional(),
            "linkData": t.proxy(renames["LinkDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
    types["SourceIn"] = t.struct(
        {"name": t.string().optional(), "predefinedSource": t.string().optional()}
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "predefinedSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["ItemPartsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ItemPartsIn"]
    )
    types["ItemPartsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ItemPartsOut"])
    types["ReferenceIn"] = t.struct(
        {
            "key": t.string().optional(),
            "blobId": t.string(),
            "contentType": t.string(),
            "size": t.string(),
            "hash": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["ReferenceIn"])
    types["ReferenceOut"] = t.struct(
        {
            "key": t.string().optional(),
            "blobId": t.string(),
            "contentType": t.string(),
            "size": t.string(),
            "hash": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceOut"])
    types["TextValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["TextValuesIn"]
    )
    types["TextValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextValuesOut"])
    types["LinkDataIn"] = t.struct(
        {
            "linkTarget": t.string().optional(),
            "linkType": t.string().optional(),
            "attachment": t.proxy(
                renames["SocialCommonAttachmentAttachmentIn"]
            ).optional(),
            "attachmentRenderHint": t.string().optional(),
            "title": t.string().optional(),
            "displayUrl": t.string().optional(),
        }
    ).named(renames["LinkDataIn"])
    types["LinkDataOut"] = t.struct(
        {
            "linkTarget": t.string().optional(),
            "linkType": t.string().optional(),
            "attachment": t.proxy(
                renames["SocialCommonAttachmentAttachmentOut"]
            ).optional(),
            "attachmentRenderHint": t.string().optional(),
            "title": t.string().optional(),
            "displayUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkDataOut"])
    types["TransactionDebugInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TransactionDebugInfoIn"]
    )
    types["TransactionDebugInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TransactionDebugInfoOut"])
    types["RbacSubjectProtoIn"] = t.struct({"username": t.string().optional()}).named(
        renames["RbacSubjectProtoIn"]
    )
    types["RbacSubjectProtoOut"] = t.struct(
        {
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RbacSubjectProtoOut"])
    types["DeleteMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteMetadataIn"]
    )
    types["DeleteMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteMetadataOut"])
    types["GoogleChatV1WidgetMarkupKeyValueIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "button": t.proxy(renames["GoogleChatV1WidgetMarkupButtonIn"]).optional(),
            "iconUrl": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "content": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "icon": t.string().optional(),
            "topLabel": t.string().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupKeyValueIn"])
    types["GoogleChatV1WidgetMarkupKeyValueOut"] = t.struct(
        {
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "button": t.proxy(renames["GoogleChatV1WidgetMarkupButtonOut"]).optional(),
            "iconUrl": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "content": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "icon": t.string().optional(),
            "topLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupKeyValueOut"])
    types["QueryInterpretationIn"] = t.struct(
        {
            "interpretationType": t.string(),
            "interpretedQuery": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["QueryInterpretationIn"])
    types["QueryInterpretationOut"] = t.struct(
        {
            "interpretationType": t.string(),
            "interpretedQuery": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationOut"])
    types["DeepLinkDataIn"] = t.struct(
        {
            "deepLinkId": t.string().optional(),
            "url": t.string().optional(),
            "client": t.array(t.proxy(renames["PackagingServiceClientIn"])).optional(),
            "appId": t.string().optional(),
        }
    ).named(renames["DeepLinkDataIn"])
    types["DeepLinkDataOut"] = t.struct(
        {
            "deepLinkId": t.string().optional(),
            "url": t.string().optional(),
            "client": t.array(t.proxy(renames["PackagingServiceClientOut"])).optional(),
            "appId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeepLinkDataOut"])
    types["SearchApplicationSessionStatsIn"] = t.struct(
        {
            "searchSessionsCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["SearchApplicationSessionStatsIn"])
    types["SearchApplicationSessionStatsOut"] = t.struct(
        {
            "searchSessionsCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationSessionStatsOut"])
    types["TransactionContextIn"] = t.struct(
        {
            "startingRecordId": t.string().optional(),
            "writeTimestampUs": t.string().optional(),
            "endingRecordId": t.string().optional(),
        }
    ).named(renames["TransactionContextIn"])
    types["TransactionContextOut"] = t.struct(
        {
            "startingRecordId": t.string().optional(),
            "writeTimestampUs": t.string().optional(),
            "endingRecordId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionContextOut"])
    types["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"] = t.struct(
        {
            "title": t.string().optional(),
            "startTime": t.string().optional(),
            "completed": t.boolean().optional(),
            "assignee": t.proxy(renames["UserIdIn"]).optional(),
            "deleted": t.boolean().optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"])
    types["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"] = t.struct(
        {
            "title": t.string().optional(),
            "startTime": t.string().optional(),
            "completed": t.boolean().optional(),
            "assignee": t.proxy(renames["UserIdOut"]).optional(),
            "deleted": t.boolean().optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"])
    types["UpdateCcRecipientsIn"] = t.struct(
        {"ccRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateCcRecipientsIn"])
    types["UpdateCcRecipientsOut"] = t.struct(
        {
            "ccRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCcRecipientsOut"])
    types["FilterIn"] = t.struct(
        {
            "valueFilter": t.proxy(renames["ValueFilterIn"]),
            "compositeFilter": t.proxy(renames["CompositeFilterIn"]),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "valueFilter": t.proxy(renames["ValueFilterOut"]),
            "compositeFilter": t.proxy(renames["CompositeFilterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["AppsDynamiteSharedTextSegmentsWithDescriptionIn"] = t.struct(
        {
            "descriptionType": t.string(),
            "textSegment": t.array(t.proxy(renames["AppsDynamiteSharedTextSegmentIn"])),
        }
    ).named(renames["AppsDynamiteSharedTextSegmentsWithDescriptionIn"])
    types["AppsDynamiteSharedTextSegmentsWithDescriptionOut"] = t.struct(
        {
            "descriptionType": t.string(),
            "textSegment": t.array(
                t.proxy(renames["AppsDynamiteSharedTextSegmentOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTextSegmentsWithDescriptionOut"])
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
    types["ObjectValuesIn"] = t.struct(
        {"values": t.array(t.proxy(renames["StructuredDataObjectIn"]))}
    ).named(renames["ObjectValuesIn"])
    types["ObjectValuesOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["StructuredDataObjectOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectValuesOut"])
    types["SuggestResultIn"] = t.struct(
        {
            "querySuggestion": t.proxy(renames["QuerySuggestionIn"]).optional(),
            "peopleSuggestion": t.proxy(renames["PeopleSuggestionIn"]).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "suggestedQuery": t.string().optional(),
        }
    ).named(renames["SuggestResultIn"])
    types["SuggestResultOut"] = t.struct(
        {
            "querySuggestion": t.proxy(renames["QuerySuggestionOut"]).optional(),
            "peopleSuggestion": t.proxy(renames["PeopleSuggestionOut"]).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "suggestedQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestResultOut"])
    types["AttributeSetIn"] = t.struct(
        {
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
            "attributeId": t.string(),
            "attributeValue": t.string().optional(),
        }
    ).named(renames["AttributeSetIn"])
    types["AttributeSetOut"] = t.struct(
        {
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "attributeId": t.string(),
            "attributeValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeSetOut"])
    types["ImapsyncFolderAttributeFolderMessageIn"] = t.struct(
        {
            "flags": t.proxy(
                renames["ImapsyncFolderAttributeFolderMessageFlagsIn"]
            ).optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["ImapsyncFolderAttributeFolderMessageIn"])
    types["ImapsyncFolderAttributeFolderMessageOut"] = t.struct(
        {
            "flags": t.proxy(
                renames["ImapsyncFolderAttributeFolderMessageFlagsOut"]
            ).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapsyncFolderAttributeFolderMessageOut"])
    types["OpenCreatedDraftActionMarkupIn"] = t.struct(
        {
            "draftThreadServerPermId": t.string().optional(),
            "draftStorageId": t.string().optional(),
            "draftId": t.string().optional(),
            "draftThreadId": t.string().optional(),
        }
    ).named(renames["OpenCreatedDraftActionMarkupIn"])
    types["OpenCreatedDraftActionMarkupOut"] = t.struct(
        {
            "draftThreadServerPermId": t.string().optional(),
            "draftStorageId": t.string().optional(),
            "draftId": t.string().optional(),
            "draftThreadId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenCreatedDraftActionMarkupOut"])
    types["ItemAclIn"] = t.struct(
        {
            "readers": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "owners": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "aclInheritanceType": t.string().optional(),
            "inheritAclFrom": t.string().optional(),
            "deniedReaders": t.array(t.proxy(renames["PrincipalIn"])).optional(),
        }
    ).named(renames["ItemAclIn"])
    types["ItemAclOut"] = t.struct(
        {
            "readers": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "owners": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "aclInheritanceType": t.string().optional(),
            "inheritAclFrom": t.string().optional(),
            "deniedReaders": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemAclOut"])
    types["AppsDynamiteSharedReactionIn"] = t.struct(
        {
            "createTimestamp": t.string().optional(),
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiIn"]),
            "currentUserParticipated": t.boolean().optional(),
            "count": t.integer().optional(),
        }
    ).named(renames["AppsDynamiteSharedReactionIn"])
    types["AppsDynamiteSharedReactionOut"] = t.struct(
        {
            "createTimestamp": t.string().optional(),
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiOut"]),
            "currentUserParticipated": t.boolean().optional(),
            "count": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedReactionOut"])
    types["BotInfoIn"] = t.struct(
        {
            "marketPlaceBannerUrl": t.string().optional(),
            "botName": t.string().optional(),
            "developerName": t.string().optional(),
            "supportHomeScreen": t.boolean().optional(),
            "supportUrls": t.proxy(renames["SupportUrlsIn"]).optional(),
            "appId": t.proxy(renames["AppIdIn"]).optional(),
            "supportedUses": t.array(t.string()).optional(),
            "appAllowlistStatus": t.string(),
            "status": t.string().optional(),
            "botAvatarUrl": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["BotInfoIn"])
    types["BotInfoOut"] = t.struct(
        {
            "marketPlaceBannerUrl": t.string().optional(),
            "botName": t.string().optional(),
            "developerName": t.string().optional(),
            "supportHomeScreen": t.boolean().optional(),
            "supportUrls": t.proxy(renames["SupportUrlsOut"]).optional(),
            "appId": t.proxy(renames["AppIdOut"]).optional(),
            "supportedUses": t.array(t.string()).optional(),
            "appAllowlistStatus": t.string(),
            "status": t.string().optional(),
            "botAvatarUrl": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BotInfoOut"])
    types["TranscriptionSessionInfoIn"] = t.struct(
        {
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
            "transcriptionSessionId": t.string().optional(),
        }
    ).named(renames["TranscriptionSessionInfoIn"])
    types["TranscriptionSessionInfoOut"] = t.struct(
        {
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "transcriptionSessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscriptionSessionInfoOut"])
    types["GetCustomerQueryStatsResponseIn"] = t.struct(
        {
            "totalQueryCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["CustomerQueryStatsIn"])),
        }
    ).named(renames["GetCustomerQueryStatsResponseIn"])
    types["GetCustomerQueryStatsResponseOut"] = t.struct(
        {
            "totalQueryCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["CustomerQueryStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerQueryStatsResponseOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn"
    ] = t.struct({"addAttendeeEmails": t.array(t.string()).optional()}).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn"
        ]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut"
    ] = t.struct(
        {
            "addAttendeeEmails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut"
        ]
    )
    types["ImageIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]),
            "altText": t.string().optional(),
            "aspectRatio": t.number().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "altText": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["SessionEventIn"] = t.struct(
        {"type": t.string().optional(), "deviceId": t.string().optional()}
    ).named(renames["SessionEventIn"])
    types["SessionEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionEventOut"])
    types["LabelUpdatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelUpdatedIn"]
    )
    types["LabelUpdatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelUpdatedOut"])
    types["AppsDynamiteStorageIconIn"] = t.struct(
        {
            "imageType": t.string().optional(),
            "materialIcon": t.proxy(
                renames["AppsDynamiteStorageMaterialIconIn"]
            ).optional(),
            "altText": t.string().optional(),
            "knownIcon": t.string().optional(),
            "iconUrl": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageIconIn"])
    types["AppsDynamiteStorageIconOut"] = t.struct(
        {
            "imageType": t.string().optional(),
            "materialIcon": t.proxy(
                renames["AppsDynamiteStorageMaterialIconOut"]
            ).optional(),
            "altText": t.string().optional(),
            "knownIcon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageIconOut"])
    types["ItemStatusIn"] = t.struct(
        {
            "code": t.string().optional(),
            "processingErrors": t.array(
                t.proxy(renames["ProcessingErrorIn"])
            ).optional(),
            "repositoryErrors": t.array(
                t.proxy(renames["RepositoryErrorIn"])
            ).optional(),
        }
    ).named(renames["ItemStatusIn"])
    types["ItemStatusOut"] = t.struct(
        {
            "code": t.string().optional(),
            "processingErrors": t.array(
                t.proxy(renames["ProcessingErrorOut"])
            ).optional(),
            "repositoryErrors": t.array(
                t.proxy(renames["RepositoryErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemStatusOut"])
    types["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "imageStyle": t.string().optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "imageStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"])
    types["CustomerIdIn"] = t.struct({"customerId": t.string()}).named(
        renames["CustomerIdIn"]
    )
    types["CustomerIdOut"] = t.struct(
        {
            "customerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerIdOut"])
    types["AttributesIn"] = t.struct(
        {"attribute": t.array(t.proxy(renames["AttributeIn"]))}
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "attribute": t.array(t.proxy(renames["AttributeOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])
    types["PrefDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PrefDeletedIn"]
    )
    types["PrefDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PrefDeletedOut"])
    types["PrivateMessageInfoIn"] = t.struct(
        {
            "gsuiteIntegrationMetadata": t.array(
                t.proxy(renames["GsuiteIntegrationMetadataIn"])
            ),
            "attachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "contextualAddOnMarkup": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupIn"])
            ),
            "text": t.string().optional(),
            "annotations": t.array(t.proxy(renames["AnnotationIn"])).optional(),
            "userId": t.proxy(renames["UserIdIn"]),
        }
    ).named(renames["PrivateMessageInfoIn"])
    types["PrivateMessageInfoOut"] = t.struct(
        {
            "gsuiteIntegrationMetadata": t.array(
                t.proxy(renames["GsuiteIntegrationMetadataOut"])
            ),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "contextualAddOnMarkup": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupOut"])
            ),
            "text": t.string().optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "userId": t.proxy(renames["UserIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateMessageInfoOut"])
    types["ValueFilterIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "value": t.proxy(renames["ValueIn"]).optional(),
        }
    ).named(renames["ValueFilterIn"])
    types["ValueFilterOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "value": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueFilterOut"])
    types["LabelUpdateIn"] = t.struct(
        {
            "syncId": t.integer(),
            "canonicalName": t.string(),
            "labelId": t.string(),
            "labelUpdated": t.proxy(renames["LabelUpdatedIn"]),
            "labelRenamed": t.proxy(renames["LabelRenamedIn"]),
            "labelDeleted": t.proxy(renames["LabelDeletedIn"]),
            "labelCreated": t.proxy(renames["LabelCreatedIn"]),
        }
    ).named(renames["LabelUpdateIn"])
    types["LabelUpdateOut"] = t.struct(
        {
            "syncId": t.integer(),
            "canonicalName": t.string(),
            "labelId": t.string(),
            "labelUpdated": t.proxy(renames["LabelUpdatedOut"]),
            "labelRenamed": t.proxy(renames["LabelRenamedOut"]),
            "labelDeleted": t.proxy(renames["LabelDeletedOut"]),
            "labelCreated": t.proxy(renames["LabelCreatedOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelUpdateOut"])
    types["AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn"])
    types["AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut"])
    types["VoicePhoneNumberIn"] = t.struct(
        {
            "e164": t.string().optional(),
            "i18nData": t.proxy(renames["VoicePhoneNumberI18nDataIn"]).optional(),
        }
    ).named(renames["VoicePhoneNumberIn"])
    types["VoicePhoneNumberOut"] = t.struct(
        {
            "e164": t.string().optional(),
            "i18nData": t.proxy(renames["VoicePhoneNumberI18nDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoicePhoneNumberOut"])
    types["AppsDynamiteSharedMessageIntegrationPayloadIn"] = t.struct(
        {
            "tasksMessageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"]
            ),
            "type": t.string().optional(),
            "projectNumber": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageIntegrationPayloadIn"])
    types["AppsDynamiteSharedMessageIntegrationPayloadOut"] = t.struct(
        {
            "tasksMessageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"]
            ),
            "type": t.string().optional(),
            "projectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageIntegrationPayloadOut"])
    types["AppsDynamiteStorageGridIn"] = t.struct(
        {
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleIn"]
            ).optional(),
            "columnCount": t.integer().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageGridGridItemIn"])
            ).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageGridIn"])
    types["AppsDynamiteStorageGridOut"] = t.struct(
        {
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleOut"]
            ).optional(),
            "columnCount": t.integer().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageGridGridItemOut"])
            ).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageGridOut"])
    types["AppsDynamiteSharedMessageComponentSearchInfoIn"] = t.struct(
        {
            "matchedSearch": t.boolean().optional(),
            "titleTextWithDescription": t.proxy(
                renames["AppsDynamiteSharedTextWithDescriptionIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageComponentSearchInfoIn"])
    types["AppsDynamiteSharedMessageComponentSearchInfoOut"] = t.struct(
        {
            "matchedSearch": t.boolean().optional(),
            "titleTextWithDescription": t.proxy(
                renames["AppsDynamiteSharedTextWithDescriptionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageComponentSearchInfoOut"])
    types["GoogleChatV1ContextualAddOnMarkupCardIn"] = t.struct(
        {
            "header": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"]
            ).optional(),
            "name": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardSectionIn"])
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardCardActionIn"])
            ).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardOut"] = t.struct(
        {
            "header": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"]
            ).optional(),
            "name": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardSectionOut"])
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardCardActionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardOut"])
    types["DocumentInfoIn"] = t.struct(
        {"whiteboardInfo": t.proxy(renames["WhiteboardInfoIn"]).optional()}
    ).named(renames["DocumentInfoIn"])
    types["DocumentInfoOut"] = t.struct(
        {
            "whiteboardInfo": t.proxy(renames["WhiteboardInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentInfoOut"])
    types["DateTimePickerIn"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "label": t.string().optional(),
        }
    ).named(renames["DateTimePickerIn"])
    types["DateTimePickerOut"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimePickerOut"])
    types["DmIdIn"] = t.struct({"dmId": t.string().optional()}).named(renames["DmIdIn"])
    types["DmIdOut"] = t.struct(
        {
            "dmId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DmIdOut"])
    types["UrlMetadataIn"] = t.struct(
        {
            "intImageWidth": t.integer().optional(),
            "title": t.string().optional(),
            "redirectUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "imageUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "url": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "snippet": t.string().optional(),
            "gwsUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "imageWidth": t.string().optional(),
            "intImageHeight": t.integer().optional(),
            "domain": t.string().optional(),
            "gwsUrlExpirationTimestamp": t.string().optional(),
            "urlSource": t.string(),
            "imageHeight": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
        }
    ).named(renames["UrlMetadataIn"])
    types["UrlMetadataOut"] = t.struct(
        {
            "intImageWidth": t.integer().optional(),
            "title": t.string().optional(),
            "redirectUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "imageUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "url": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "snippet": t.string().optional(),
            "gwsUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "imageWidth": t.string().optional(),
            "intImageHeight": t.integer().optional(),
            "domain": t.string().optional(),
            "gwsUrlExpirationTimestamp": t.string().optional(),
            "urlSource": t.string(),
            "imageHeight": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlMetadataOut"])
    types["CardActionIn"] = t.struct(
        {"actionLabel": t.string().optional(), "onClick": t.proxy(renames["OnClickIn"])}
    ).named(renames["CardActionIn"])
    types["CardActionOut"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardActionOut"])
    types["HistoryRecordIn"] = t.struct(
        {
            "transactionContext": t.proxy(renames["TransactionContextIn"]).optional(),
            "type": t.string(),
            "prefUpdate": t.proxy(renames["PrefUpdateIn"]),
            "txnDebugInfo": t.proxy(renames["TransactionDebugInfoIn"]),
            "clientContext": t.proxy(renames["ClientContextIn"]).optional(),
            "threadUpdate": t.proxy(renames["ThreadUpdateIn"]),
            "recordId": t.string().optional(),
            "imapUpdate": t.proxy(renames["ImapUpdateIn"]),
            "filterUpdate": t.proxy(renames["FilterUpdateIn"]),
            "labelUpdate": t.proxy(renames["LabelUpdateIn"]),
        }
    ).named(renames["HistoryRecordIn"])
    types["HistoryRecordOut"] = t.struct(
        {
            "transactionContext": t.proxy(renames["TransactionContextOut"]).optional(),
            "type": t.string(),
            "prefUpdate": t.proxy(renames["PrefUpdateOut"]),
            "txnDebugInfo": t.proxy(renames["TransactionDebugInfoOut"]),
            "clientContext": t.proxy(renames["ClientContextOut"]).optional(),
            "threadUpdate": t.proxy(renames["ThreadUpdateOut"]),
            "recordId": t.string().optional(),
            "imapUpdate": t.proxy(renames["ImapUpdateOut"]),
            "filterUpdate": t.proxy(renames["FilterUpdateOut"]),
            "labelUpdate": t.proxy(renames["LabelUpdateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryRecordOut"])
    types["CustomerSearchApplicationStatsIn"] = t.struct(
        {"date": t.proxy(renames["DateIn"]).optional(), "count": t.string().optional()}
    ).named(renames["CustomerSearchApplicationStatsIn"])
    types["CustomerSearchApplicationStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerSearchApplicationStatsOut"])
    types["ShareScopeIn"] = t.struct(
        {"domain": t.string().optional(), "scope": t.string().optional()}
    ).named(renames["ShareScopeIn"])
    types["ShareScopeOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShareScopeOut"])
    types["StructuredResultIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["StructuredResultIn"])
    types["StructuredResultOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredResultOut"])
    types["YoutubeUserProtoIn"] = t.struct({"youtubeUserId": t.string()}).named(
        renames["YoutubeUserProtoIn"]
    )
    types["YoutubeUserProtoOut"] = t.struct(
        {
            "youtubeUserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeUserProtoOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn"
    ] = t.struct(
        {
            "regionCode": t.string().optional(),
            "type": t.string().optional(),
            "uri": t.string().optional(),
            "meetingCode": t.string().optional(),
            "accessCode": t.string().optional(),
            "passcode": t.string().optional(),
            "label": t.string().optional(),
            "pin": t.string().optional(),
            "password": t.string().optional(),
            "features": t.array(t.string()).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn"
        ]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut"
    ] = t.struct(
        {
            "regionCode": t.string().optional(),
            "type": t.string().optional(),
            "uri": t.string().optional(),
            "meetingCode": t.string().optional(),
            "accessCode": t.string().optional(),
            "passcode": t.string().optional(),
            "label": t.string().optional(),
            "pin": t.string().optional(),
            "password": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut"
        ]
    )
    types["CallSettingsIn"] = t.struct(
        {
            "chatLock": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "accessLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "videoLock": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "accessType": t.string().optional(),
            "reactionsLock": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "audioLock": t.boolean().optional(),
        }
    ).named(renames["CallSettingsIn"])
    types["CallSettingsOut"] = t.struct(
        {
            "chatLock": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "accessLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "videoLock": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "accessType": t.string().optional(),
            "reactionsLock": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "audioLock": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CallSettingsOut"])
    types["AppsDynamiteStorageCardSectionIn"] = t.struct(
        {
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "collapsible": t.boolean().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageWidgetIn"])
            ).optional(),
            "header": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageCardSectionIn"])
    types["AppsDynamiteStorageCardSectionOut"] = t.struct(
        {
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "collapsible": t.boolean().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageWidgetOut"])
            ).optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardSectionOut"])
    types["ItemThreadIn"] = t.struct(
        {
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "version": t.string().optional(),
            "snippet": t.string().optional(),
            "item": t.array(t.proxy(renames["FuseboxItemIn"])).optional(),
            "clusterInfo": t.proxy(renames["ClusterInfoIn"]),
            "matchInfo": t.proxy(renames["FuseboxItemThreadMatchInfoIn"]),
            "lastItemId": t.string().optional(),
            "topicState": t.proxy(renames["TopicStateIn"]).optional(),
            "threadLocator": t.string().optional(),
        }
    ).named(renames["ItemThreadIn"])
    types["ItemThreadOut"] = t.struct(
        {
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "version": t.string().optional(),
            "snippet": t.string().optional(),
            "item": t.array(t.proxy(renames["FuseboxItemOut"])).optional(),
            "clusterInfo": t.proxy(renames["ClusterInfoOut"]),
            "matchInfo": t.proxy(renames["FuseboxItemThreadMatchInfoOut"]),
            "lastItemId": t.string().optional(),
            "topicState": t.proxy(renames["TopicStateOut"]).optional(),
            "threadLocator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemThreadOut"])
    types["HostAppActionMarkupIn"] = t.struct(
        {
            "editorAction": t.proxy(renames["EditorClientActionMarkupIn"]).optional(),
            "sheetsAction": t.proxy(renames["SheetsClientActionMarkupIn"]).optional(),
            "chatAction": t.proxy(renames["ChatClientActionMarkupIn"]).optional(),
            "calendarAction": t.proxy(
                renames["CalendarClientActionMarkupIn"]
            ).optional(),
            "gmailAction": t.proxy(renames["GmailClientActionMarkupIn"]).optional(),
            "driveAction": t.proxy(renames["DriveClientActionMarkupIn"]).optional(),
        }
    ).named(renames["HostAppActionMarkupIn"])
    types["HostAppActionMarkupOut"] = t.struct(
        {
            "editorAction": t.proxy(renames["EditorClientActionMarkupOut"]).optional(),
            "sheetsAction": t.proxy(renames["SheetsClientActionMarkupOut"]).optional(),
            "chatAction": t.proxy(renames["ChatClientActionMarkupOut"]).optional(),
            "calendarAction": t.proxy(
                renames["CalendarClientActionMarkupOut"]
            ).optional(),
            "gmailAction": t.proxy(renames["GmailClientActionMarkupOut"]).optional(),
            "driveAction": t.proxy(renames["DriveClientActionMarkupOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostAppActionMarkupOut"])
    types["EventAnnotationIn"] = t.struct(
        {"type": t.integer(), "value": t.string()}
    ).named(renames["EventAnnotationIn"])
    types["EventAnnotationOut"] = t.struct(
        {
            "type": t.integer(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventAnnotationOut"])
    types["SocialCommonAttachmentAttachmentIn"] = t.struct(
        {
            "id": t.string().optional(),
            "embedItem": t.proxy(renames["EmbedClientItemIn"]).optional(),
        }
    ).named(renames["SocialCommonAttachmentAttachmentIn"])
    types["SocialCommonAttachmentAttachmentOut"] = t.struct(
        {
            "id": t.string().optional(),
            "embedItem": t.proxy(renames["EmbedClientItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocialCommonAttachmentAttachmentOut"])
    types["AppsDynamiteStorageImageComponentIn"] = t.struct(
        {
            "cropStyle": t.proxy(
                renames["AppsDynamiteStorageImageCropStyleIn"]
            ).optional(),
            "altText": t.string().optional(),
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleIn"]
            ).optional(),
            "imageUri": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageImageComponentIn"])
    types["AppsDynamiteStorageImageComponentOut"] = t.struct(
        {
            "cropStyle": t.proxy(
                renames["AppsDynamiteStorageImageCropStyleOut"]
            ).optional(),
            "altText": t.string().optional(),
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleOut"]
            ).optional(),
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageComponentOut"])
    types["DoubleValuesIn"] = t.struct({"values": t.array(t.number())}).named(
        renames["DoubleValuesIn"]
    )
    types["DoubleValuesOut"] = t.struct(
        {
            "values": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleValuesOut"])
    types["ContentReportSummaryIn"] = t.struct(
        {
            "numberReports": t.integer().optional(),
            "numberReportsAllRevisions": t.integer().optional(),
        }
    ).named(renames["ContentReportSummaryIn"])
    types["ContentReportSummaryOut"] = t.struct(
        {
            "numberReports": t.integer().optional(),
            "numberReportsAllRevisions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentReportSummaryOut"])
    types["GoogleChatV1WidgetMarkupImageIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "imageUrl": t.string().optional(),
            "aspectRatio": t.number().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageIn"])
    types["GoogleChatV1WidgetMarkupImageOut"] = t.struct(
        {
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "imageUrl": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageOut"])
    types["SuggestResponseIn"] = t.struct(
        {"suggestResults": t.array(t.proxy(renames["SuggestResultIn"])).optional()}
    ).named(renames["SuggestResponseIn"])
    types["SuggestResponseOut"] = t.struct(
        {
            "suggestResults": t.array(t.proxy(renames["SuggestResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestResponseOut"])
    types["ResponseDebugInfoIn"] = t.struct(
        {"formattedDebugInfo": t.string().optional()}
    ).named(renames["ResponseDebugInfoIn"])
    types["ResponseDebugInfoOut"] = t.struct(
        {
            "formattedDebugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseDebugInfoOut"])
    types["CustomerQueryStatsIn"] = t.struct(
        {
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusIn"])),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["CustomerQueryStatsIn"])
    types["CustomerQueryStatsOut"] = t.struct(
        {
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusOut"])),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerQueryStatsOut"])
    types["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"])
    types["AppsDynamiteStorageActionIn"] = t.struct(
        {
            "interaction": t.string(),
            "parameters": t.array(
                t.proxy(renames["AppsDynamiteStorageActionActionParameterIn"])
            ).optional(),
            "loadIndicator": t.string(),
            "persistValues": t.boolean().optional(),
            "function": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageActionIn"])
    types["AppsDynamiteStorageActionOut"] = t.struct(
        {
            "interaction": t.string(),
            "parameters": t.array(
                t.proxy(renames["AppsDynamiteStorageActionActionParameterOut"])
            ).optional(),
            "loadIndicator": t.string(),
            "persistValues": t.boolean().optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageActionOut"])
    types["UpdateToRecipientsIn"] = t.struct(
        {"toRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateToRecipientsIn"])
    types["UpdateToRecipientsOut"] = t.struct(
        {
            "toRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateToRecipientsOut"])
    types["TextFieldIn"] = t.struct(
        {
            "autoComplete": t.proxy(renames["AutoCompleteIn"]).optional(),
            "type": t.string(),
            "onChange": t.proxy(renames["FormActionIn"]),
            "value": t.string().optional(),
            "hintText": t.string(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "autoCompleteCallback": t.proxy(renames["FormActionIn"]).optional(),
            "maxLines": t.integer(),
            "autoCompleteMultipleSelections": t.boolean().optional(),
        }
    ).named(renames["TextFieldIn"])
    types["TextFieldOut"] = t.struct(
        {
            "autoComplete": t.proxy(renames["AutoCompleteOut"]).optional(),
            "type": t.string(),
            "onChange": t.proxy(renames["FormActionOut"]),
            "value": t.string().optional(),
            "hintText": t.string(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "autoCompleteCallback": t.proxy(renames["FormActionOut"]).optional(),
            "maxLines": t.integer(),
            "autoCompleteMultipleSelections": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFieldOut"])
    types["CircleProtoIn"] = t.struct(
        {
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "ownerGaiaId": t.string().optional(),
            "circleId": t.string().optional(),
        }
    ).named(renames["CircleProtoIn"])
    types["CircleProtoOut"] = t.struct(
        {
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "ownerGaiaId": t.string().optional(),
            "circleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CircleProtoOut"])
    types["DateOperatorOptionsIn"] = t.struct(
        {
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
        }
    ).named(renames["DateOperatorOptionsIn"])
    types["DateOperatorOptionsOut"] = t.struct(
        {
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOperatorOptionsOut"])
    types["AppsDynamiteStorageDecoratedTextIn"] = t.struct(
        {
            "endIcon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "text": t.string(),
            "switchControl": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextSwitchControlIn"]
            ).optional(),
            "button": t.proxy(renames["AppsDynamiteStorageButtonIn"]).optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
            "bottomLabel": t.string().optional(),
            "wrapText": t.boolean().optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "topLabel": t.string().optional(),
            "startIcon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextIn"])
    types["AppsDynamiteStorageDecoratedTextOut"] = t.struct(
        {
            "endIcon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "text": t.string(),
            "switchControl": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextSwitchControlOut"]
            ).optional(),
            "button": t.proxy(renames["AppsDynamiteStorageButtonOut"]).optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "bottomLabel": t.string().optional(),
            "wrapText": t.boolean().optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "topLabel": t.string().optional(),
            "startIcon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextOut"])
    types["EmailOwnerProtoIn"] = t.struct({"email": t.string()}).named(
        renames["EmailOwnerProtoIn"]
    )
    types["EmailOwnerProtoOut"] = t.struct(
        {"email": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmailOwnerProtoOut"])
    types["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"])
    types["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"])
    types["RestrictItemIn"] = t.struct(
        {
            "driveLocationRestrict": t.proxy(renames["DriveLocationRestrictIn"]),
            "driveTimeSpanRestrict": t.proxy(renames["DriveTimeSpanRestrictIn"]),
            "searchOperator": t.string().optional(),
            "driveMimeTypeRestrict": t.proxy(
                renames["DriveMimeTypeRestrictIn"]
            ).optional(),
            "driveFollowUpRestrict": t.proxy(renames["DriveFollowUpRestrictIn"]),
        }
    ).named(renames["RestrictItemIn"])
    types["RestrictItemOut"] = t.struct(
        {
            "driveLocationRestrict": t.proxy(renames["DriveLocationRestrictOut"]),
            "driveTimeSpanRestrict": t.proxy(renames["DriveTimeSpanRestrictOut"]),
            "searchOperator": t.string().optional(),
            "driveMimeTypeRestrict": t.proxy(
                renames["DriveMimeTypeRestrictOut"]
            ).optional(),
            "driveFollowUpRestrict": t.proxy(renames["DriveFollowUpRestrictOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictItemOut"])
    types["ImapUidsReassignIn"] = t.struct(
        {"labelId": t.string().optional(), "messageId": t.array(t.string()).optional()}
    ).named(renames["ImapUidsReassignIn"])
    types["ImapUidsReassignOut"] = t.struct(
        {
            "labelId": t.string().optional(),
            "messageId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapUidsReassignOut"])
    types["DlpActionIn"] = t.struct(
        {"actionType": t.string(), "unsafeHtmlMessageBody": t.string().optional()}
    ).named(renames["DlpActionIn"])
    types["DlpActionOut"] = t.struct(
        {
            "actionType": t.string(),
            "unsafeHtmlMessageBody": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpActionOut"])
    types["TextOperatorOptionsIn"] = t.struct(
        {
            "exactMatchWithOperator": t.boolean().optional(),
            "operatorName": t.string().optional(),
        }
    ).named(renames["TextOperatorOptionsIn"])
    types["TextOperatorOptionsOut"] = t.struct(
        {
            "exactMatchWithOperator": t.boolean().optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextOperatorOptionsOut"])
    types["ObjectOptionsIn"] = t.struct(
        {
            "freshnessOptions": t.proxy(renames["FreshnessOptionsIn"]).optional(),
            "suggestionFilteringOperators": t.array(t.string()).optional(),
            "displayOptions": t.proxy(renames["ObjectDisplayOptionsIn"]).optional(),
        }
    ).named(renames["ObjectOptionsIn"])
    types["ObjectOptionsOut"] = t.struct(
        {
            "freshnessOptions": t.proxy(renames["FreshnessOptionsOut"]).optional(),
            "suggestionFilteringOperators": t.array(t.string()).optional(),
            "displayOptions": t.proxy(renames["ObjectDisplayOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectOptionsOut"])
    types["AppsDynamiteStorageCardCardHeaderIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "imageAltText": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageType": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageCardCardHeaderIn"])
    types["AppsDynamiteStorageCardCardHeaderOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "imageAltText": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageType": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardCardHeaderOut"])
    types["RepositoryErrorIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "httpStatusCode": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RepositoryErrorIn"])
    types["RepositoryErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "httpStatusCode": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryErrorOut"])
    types["DataLossPreventionMetadataIn"] = t.struct(
        {
            "warnAcknowledged": t.boolean().optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryIn"]).optional(),
        }
    ).named(renames["DataLossPreventionMetadataIn"])
    types["DataLossPreventionMetadataOut"] = t.struct(
        {
            "warnAcknowledged": t.boolean().optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLossPreventionMetadataOut"])
    types["ResultDisplayLineIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["ResultDisplayFieldIn"]))}
    ).named(renames["ResultDisplayLineIn"])
    types["ResultDisplayLineOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["ResultDisplayFieldOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayLineOut"])
    types["CaribouAttributeValueIn"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string(),
            "rawByteValue": t.string().optional(),
            "intValue": t.integer(),
            "longValue": t.string(),
        }
    ).named(renames["CaribouAttributeValueIn"])
    types["CaribouAttributeValueOut"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string(),
            "rawByteValue": t.string().optional(),
            "intValue": t.integer(),
            "longValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaribouAttributeValueOut"])
    types["WonderMessageMappingIn"] = t.struct(
        {"wonderCardMessageId": t.array(t.string()).optional()}
    ).named(renames["WonderMessageMappingIn"])
    types["WonderMessageMappingOut"] = t.struct(
        {
            "wonderCardMessageId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WonderMessageMappingOut"])
    types["SwitchWidgetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "selected": t.boolean(),
            "value": t.string().optional(),
            "onChange": t.proxy(renames["FormActionIn"]),
            "controlType": t.string(),
        }
    ).named(renames["SwitchWidgetIn"])
    types["SwitchWidgetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "selected": t.boolean(),
            "value": t.string().optional(),
            "onChange": t.proxy(renames["FormActionOut"]),
            "controlType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SwitchWidgetOut"])
    types["EmailAddressIn"] = t.struct(
        {
            "primary": t.boolean().optional(),
            "customType": t.string().optional(),
            "emailAddress": t.string().optional(),
            "emailUrl": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["EmailAddressIn"])
    types["EmailAddressOut"] = t.struct(
        {
            "primary": t.boolean().optional(),
            "customType": t.string().optional(),
            "emailAddress": t.string().optional(),
            "emailUrl": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailAddressOut"])
    types["TopicStateUpdateIn"] = t.struct(
        {"topicState": t.proxy(renames["TopicStateIn"])}
    ).named(renames["TopicStateUpdateIn"])
    types["TopicStateUpdateOut"] = t.struct(
        {
            "topicState": t.proxy(renames["TopicStateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicStateUpdateOut"])
    types["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"])
    types["DriveMimeTypeRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveMimeTypeRestrictIn"]
    )
    types["DriveMimeTypeRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveMimeTypeRestrictOut"])
    types["FacetBucketIn"] = t.struct(
        {
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "count": t.integer().optional(),
            "value": t.proxy(renames["ValueIn"]),
            "percentage": t.integer().optional(),
        }
    ).named(renames["FacetBucketIn"])
    types["FacetBucketOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "count": t.integer().optional(),
            "value": t.proxy(renames["ValueOut"]),
            "percentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetBucketOut"])
    types["GroupDetailsUpdatedMetadataIn"] = t.struct(
        {
            "newGroupDetails": t.proxy(renames["AppsDynamiteSharedGroupDetailsIn"]),
            "prevGroupDetails": t.proxy(renames["AppsDynamiteSharedGroupDetailsIn"]),
        }
    ).named(renames["GroupDetailsUpdatedMetadataIn"])
    types["GroupDetailsUpdatedMetadataOut"] = t.struct(
        {
            "newGroupDetails": t.proxy(renames["AppsDynamiteSharedGroupDetailsOut"]),
            "prevGroupDetails": t.proxy(renames["AppsDynamiteSharedGroupDetailsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupDetailsUpdatedMetadataOut"])
    types["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"])
    types["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"])
    types["ResultDisplayMetadataIn"] = t.struct(
        {
            "metalines": t.array(t.proxy(renames["ResultDisplayLineIn"])).optional(),
            "objectTypeLabel": t.string().optional(),
        }
    ).named(renames["ResultDisplayMetadataIn"])
    types["ResultDisplayMetadataOut"] = t.struct(
        {
            "metalines": t.array(t.proxy(renames["ResultDisplayLineOut"])).optional(),
            "objectTypeLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayMetadataOut"])
    types["AppsDynamiteStorageMaterialIconIn"] = t.struct(
        {
            "fill": t.boolean().optional(),
            "grade": t.integer().optional(),
            "name": t.string().optional(),
            "weight": t.integer().optional(),
        }
    ).named(renames["AppsDynamiteStorageMaterialIconIn"])
    types["AppsDynamiteStorageMaterialIconOut"] = t.struct(
        {
            "fill": t.boolean().optional(),
            "grade": t.integer().optional(),
            "name": t.string().optional(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageMaterialIconOut"])
    types["AutoCompleteIn"] = t.struct(
        {"items": t.array(t.proxy(renames["AutoCompleteItemIn"]))}
    ).named(renames["AutoCompleteIn"])
    types["AutoCompleteOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AutoCompleteItemOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoCompleteOut"])
    types["PresenterIn"] = t.struct(
        {
            "presenterDeviceId": t.string().optional(),
            "byDeviceId": t.string().optional(),
            "copresenterDeviceIds": t.array(t.string()).optional(),
        }
    ).named(renames["PresenterIn"])
    types["PresenterOut"] = t.struct(
        {
            "presenterDeviceId": t.string().optional(),
            "byDeviceId": t.string().optional(),
            "copresenterDeviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresenterOut"])
    types["RbacRoleProtoIn"] = t.struct(
        {
            "objectId": t.string(),
            "name": t.string(),
            "rbacNamespace": t.string().optional(),
            "rbacRoleName": t.string().optional(),
        }
    ).named(renames["RbacRoleProtoIn"])
    types["RbacRoleProtoOut"] = t.struct(
        {
            "objectId": t.string(),
            "name": t.string(),
            "rbacNamespace": t.string().optional(),
            "rbacRoleName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RbacRoleProtoOut"])
    types["ZwiebackSessionProtoIn"] = t.struct({"zwiebackSessionId": t.string()}).named(
        renames["ZwiebackSessionProtoIn"]
    )
    types["ZwiebackSessionProtoOut"] = t.struct(
        {
            "zwiebackSessionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZwiebackSessionProtoOut"])
    types["MembershipChangeEventIn"] = t.struct(
        {
            "type": t.string(),
            "participantId": t.array(t.proxy(renames["StoredParticipantIdIn"])),
            "leaveReason": t.string().optional(),
        }
    ).named(renames["MembershipChangeEventIn"])
    types["MembershipChangeEventOut"] = t.struct(
        {
            "type": t.string(),
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "leaveReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipChangeEventOut"])
    types["GetCustomerUserStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["CustomerUserStatsIn"]))}
    ).named(renames["GetCustomerUserStatsResponseIn"])
    types["GetCustomerUserStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerUserStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerUserStatsResponseOut"])
    types["BotResponseIn"] = t.struct(
        {
            "setupUrl": t.string().optional(),
            "botId": t.proxy(renames["UserIdIn"]),
            "responseType": t.string(),
            "requiredAction": t.string(),
        }
    ).named(renames["BotResponseIn"])
    types["BotResponseOut"] = t.struct(
        {
            "setupUrl": t.string().optional(),
            "botId": t.proxy(renames["UserIdOut"]),
            "responseType": t.string(),
            "requiredAction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BotResponseOut"])
    types["PrincipalProtoIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "allAuthenticatedUsers": t.proxy(
                renames["AllAuthenticatedUsersProtoIn"]
            ).optional(),
            "youtubeUser": t.proxy(renames["YoutubeUserProtoIn"]).optional(),
            "square": t.proxy(renames["SquareProtoIn"]).optional(),
            "rbacSubject": t.proxy(renames["RbacSubjectProtoIn"]).optional(),
            "cloudPrincipal": t.proxy(renames["CloudPrincipalProtoIn"]).optional(),
            "rbacRole": t.proxy(renames["RbacRoleProtoIn"]).optional(),
            "postiniUser": t.proxy(renames["PostiniUserProtoIn"]).optional(),
            "mdbUser": t.proxy(renames["MdbUserProtoIn"]).optional(),
            "ldapGroup": t.proxy(renames["LdapGroupProtoIn"]).optional(),
            "signingKeyPossessor": t.proxy(
                renames["SigningKeyPossessorProtoIn"]
            ).optional(),
            "host": t.proxy(renames["HostProtoIn"]).optional(),
            "resourceRole": t.proxy(renames["ResourceRoleProtoIn"]).optional(),
            "mdbGroup": t.proxy(renames["MdbGroupProtoIn"]).optional(),
            "chat": t.proxy(renames["ChatProtoIn"]).optional(),
            "zwiebackSession": t.proxy(renames["ZwiebackSessionProtoIn"]).optional(),
            "gaiaUser": t.proxy(renames["GaiaUserProtoIn"]).optional(),
            "socialGraphNode": t.proxy(renames["SocialGraphNodeProtoIn"]).optional(),
            "circle": t.proxy(renames["CircleProtoIn"]).optional(),
            "ldapUser": t.proxy(renames["LdapUserProtoIn"]).optional(),
            "emailOwner": t.proxy(renames["EmailOwnerProtoIn"]).optional(),
            "contactGroup": t.proxy(renames["ContactGroupProtoIn"]).optional(),
            "capTokenHolder": t.proxy(renames["CapTokenHolderProtoIn"]).optional(),
            "gaiaGroup": t.proxy(renames["GaiaGroupProtoIn"]).optional(),
            "simpleSecretHolder": t.proxy(
                renames["SimpleSecretHolderProtoIn"]
            ).optional(),
            "oauthConsumer": t.proxy(renames["OAuthConsumerProtoIn"]).optional(),
            "event": t.proxy(renames["EventProtoIn"]).optional(),
        }
    ).named(renames["PrincipalProtoIn"])
    types["PrincipalProtoOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "allAuthenticatedUsers": t.proxy(
                renames["AllAuthenticatedUsersProtoOut"]
            ).optional(),
            "youtubeUser": t.proxy(renames["YoutubeUserProtoOut"]).optional(),
            "square": t.proxy(renames["SquareProtoOut"]).optional(),
            "rbacSubject": t.proxy(renames["RbacSubjectProtoOut"]).optional(),
            "cloudPrincipal": t.proxy(renames["CloudPrincipalProtoOut"]).optional(),
            "rbacRole": t.proxy(renames["RbacRoleProtoOut"]).optional(),
            "postiniUser": t.proxy(renames["PostiniUserProtoOut"]).optional(),
            "mdbUser": t.proxy(renames["MdbUserProtoOut"]).optional(),
            "ldapGroup": t.proxy(renames["LdapGroupProtoOut"]).optional(),
            "signingKeyPossessor": t.proxy(
                renames["SigningKeyPossessorProtoOut"]
            ).optional(),
            "host": t.proxy(renames["HostProtoOut"]).optional(),
            "resourceRole": t.proxy(renames["ResourceRoleProtoOut"]).optional(),
            "mdbGroup": t.proxy(renames["MdbGroupProtoOut"]).optional(),
            "chat": t.proxy(renames["ChatProtoOut"]).optional(),
            "zwiebackSession": t.proxy(renames["ZwiebackSessionProtoOut"]).optional(),
            "gaiaUser": t.proxy(renames["GaiaUserProtoOut"]).optional(),
            "socialGraphNode": t.proxy(renames["SocialGraphNodeProtoOut"]).optional(),
            "circle": t.proxy(renames["CircleProtoOut"]).optional(),
            "ldapUser": t.proxy(renames["LdapUserProtoOut"]).optional(),
            "emailOwner": t.proxy(renames["EmailOwnerProtoOut"]).optional(),
            "contactGroup": t.proxy(renames["ContactGroupProtoOut"]).optional(),
            "capTokenHolder": t.proxy(renames["CapTokenHolderProtoOut"]).optional(),
            "gaiaGroup": t.proxy(renames["GaiaGroupProtoOut"]).optional(),
            "simpleSecretHolder": t.proxy(
                renames["SimpleSecretHolderProtoOut"]
            ).optional(),
            "oauthConsumer": t.proxy(renames["OAuthConsumerProtoOut"]).optional(),
            "event": t.proxy(renames["EventProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrincipalProtoOut"])
    types["TrustedResourceUrlProtoIn"] = t.struct(
        {
            "privateDoNotAccessOrElseTrustedResourceUrlWrappedValue": t.string().optional()
        }
    ).named(renames["TrustedResourceUrlProtoIn"])
    types["TrustedResourceUrlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseTrustedResourceUrlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustedResourceUrlProtoOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"] = t.struct(
        {"nudgeType": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut"] = t.struct(
        {
            "nudgeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut"])
    types["CalendarClientActionMarkupIn"] = t.struct(
        {
            "editAttendeesActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn"
                ]
            ).optional(),
            "addAttachmentsActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn"
                ]
            ).optional(),
            "editConferenceDataActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn"
                ]
            ).optional(),
        }
    ).named(renames["CalendarClientActionMarkupIn"])
    types["CalendarClientActionMarkupOut"] = t.struct(
        {
            "editAttendeesActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut"
                ]
            ).optional(),
            "addAttachmentsActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut"
                ]
            ).optional(),
            "editConferenceDataActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarClientActionMarkupOut"])
    types["PackagingServiceClientIn"] = t.struct(
        {
            "type": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "androidPackageName": t.string().optional(),
        }
    ).named(renames["PackagingServiceClientIn"])
    types["PackagingServiceClientOut"] = t.struct(
        {
            "type": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackagingServiceClientOut"])
    types["TimestampOperatorOptionsIn"] = t.struct(
        {
            "lessThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
        }
    ).named(renames["TimestampOperatorOptionsIn"])
    types["TimestampOperatorOptionsOut"] = t.struct(
        {
            "lessThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampOperatorOptionsOut"])
    types["GoogleChatV1WidgetMarkupTextParagraphIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleChatV1WidgetMarkupTextParagraphIn"])
    types["GoogleChatV1WidgetMarkupTextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChatV1WidgetMarkupTextParagraphOut"])
    types["RosterIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["RosterIdIn"]
    )
    types["RosterIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RosterIdOut"])
    types["AppsDynamiteSharedMessageInfoIn"] = t.struct(
        {
            "messageId": t.proxy(renames["MessageIdIn"]).optional(),
            "messageType": t.string().optional(),
            "topicReadTimeUsec": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageInfoIn"])
    types["AppsDynamiteSharedMessageInfoOut"] = t.struct(
        {
            "messageId": t.proxy(renames["MessageIdOut"]).optional(),
            "messageType": t.string().optional(),
            "topicReadTimeUsec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageInfoOut"])
    types["ProvenanceIn"] = t.struct(
        {
            "annotationBlob": t.string().optional(),
            "retrievedTimestampMsec": t.string().optional(),
            "itemtype": t.array(t.string()).optional(),
            "retrievedUrl": t.string().optional(),
            "inputUrl": t.string().optional(),
            "canonicalUrl": t.string().optional(),
        }
    ).named(renames["ProvenanceIn"])
    types["ProvenanceOut"] = t.struct(
        {
            "annotationBlob": t.string().optional(),
            "retrievedTimestampMsec": t.string().optional(),
            "itemtype": t.array(t.string()).optional(),
            "retrievedUrl": t.string().optional(),
            "inputUrl": t.string().optional(),
            "canonicalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvenanceOut"])
    types["GaiaUserProtoIn"] = t.struct({"userId": t.string()}).named(
        renames["GaiaUserProtoIn"]
    )
    types["GaiaUserProtoOut"] = t.struct(
        {"userId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GaiaUserProtoOut"])
    types["OAuthConsumerProtoIn"] = t.struct({"domain": t.string()}).named(
        renames["OAuthConsumerProtoIn"]
    )
    types["OAuthConsumerProtoOut"] = t.struct(
        {"domain": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OAuthConsumerProtoOut"])
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
    types["AppsDynamiteSharedJustificationIn"] = t.struct(
        {
            "actionTime": t.string().optional(),
            "documentOwner": t.proxy(
                renames["AppsDynamiteSharedJustificationPersonIn"]
            ).optional(),
            "actionType": t.string().optional(),
            "topics": t.array(t.string()).optional(),
        }
    ).named(renames["AppsDynamiteSharedJustificationIn"])
    types["AppsDynamiteSharedJustificationOut"] = t.struct(
        {
            "actionTime": t.string().optional(),
            "documentOwner": t.proxy(
                renames["AppsDynamiteSharedJustificationPersonOut"]
            ).optional(),
            "actionType": t.string().optional(),
            "topics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedJustificationOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn"
    ] = t.struct(
        {
            "conferenceData": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn"
                ]
            ).optional()
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn"
        ]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut"
    ] = t.struct(
        {
            "conferenceData": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut"
        ]
    )
    types["AppIdIn"] = t.struct(
        {
            "id": t.string().optional(),
            "gsuiteAppType": t.string().optional(),
            "appType": t.string().optional(),
        }
    ).named(renames["AppIdIn"])
    types["AppIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "gsuiteAppType": t.string().optional(),
            "appType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppIdOut"])
    types["ResultDebugInfoIn"] = t.struct(
        {"formattedDebugInfo": t.string().optional()}
    ).named(renames["ResultDebugInfoIn"])
    types["ResultDebugInfoOut"] = t.struct(
        {
            "formattedDebugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDebugInfoOut"])
    types["FormatMetadataIn"] = t.struct(
        {"fontColor": t.integer().optional(), "formatType": t.string().optional()}
    ).named(renames["FormatMetadataIn"])
    types["FormatMetadataOut"] = t.struct(
        {
            "fontColor": t.integer().optional(),
            "formatType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatMetadataOut"])
    types["LabelRemovedIn"] = t.struct(
        {
            "labelName": t.string(),
            "labelId": t.string(),
            "syncId": t.integer(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
        }
    ).named(renames["LabelRemovedIn"])
    types["LabelRemovedOut"] = t.struct(
        {
            "labelName": t.string(),
            "labelId": t.string(),
            "syncId": t.integer(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelRemovedOut"])
    types["WhiteboardInfoIn"] = t.struct(
        {
            "id": t.string().optional(),
            "title": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["WhiteboardInfoIn"])
    types["WhiteboardInfoOut"] = t.struct(
        {
            "id": t.string().optional(),
            "title": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WhiteboardInfoOut"])
    types["WrappedResourceKeyIn"] = t.struct(
        {"resourceKey": t.string().optional()}
    ).named(renames["WrappedResourceKeyIn"])
    types["WrappedResourceKeyOut"] = t.struct(
        {
            "resourceKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WrappedResourceKeyOut"])
    types["StructuredDataObjectIn"] = t.struct(
        {"properties": t.array(t.proxy(renames["NamedPropertyIn"])).optional()}
    ).named(renames["StructuredDataObjectIn"])
    types["StructuredDataObjectOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["NamedPropertyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredDataObjectOut"])
    types["UpdateDataSourceRequestIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "updateMask": t.string().optional(),
            "source": t.proxy(renames["DataSourceIn"]),
        }
    ).named(renames["UpdateDataSourceRequestIn"])
    types["UpdateDataSourceRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "updateMask": t.string().optional(),
            "source": t.proxy(renames["DataSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestOut"])
    types["SupportUrlsIn"] = t.struct(
        {
            "supportUrl": t.string().optional(),
            "privacyPolicyUrl": t.string().optional(),
            "gwmUrl": t.string().optional(),
            "deletionPolicyUrl": t.string().optional(),
            "setupUrl": t.string().optional(),
            "adminConfigUrl": t.string().optional(),
            "tosUrl": t.string().optional(),
        }
    ).named(renames["SupportUrlsIn"])
    types["SupportUrlsOut"] = t.struct(
        {
            "supportUrl": t.string().optional(),
            "privacyPolicyUrl": t.string().optional(),
            "gwmUrl": t.string().optional(),
            "deletionPolicyUrl": t.string().optional(),
            "setupUrl": t.string().optional(),
            "adminConfigUrl": t.string().optional(),
            "tosUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportUrlsOut"])
    types["AppsDynamiteSharedVideoReferenceIn"] = t.struct(
        {"status": t.string().optional(), "format": t.array(t.integer()).optional()}
    ).named(renames["AppsDynamiteSharedVideoReferenceIn"])
    types["AppsDynamiteSharedVideoReferenceOut"] = t.struct(
        {
            "status": t.string().optional(),
            "format": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedVideoReferenceOut"])
    types["UploadMetadataIn"] = t.struct(
        {
            "localId": t.string().optional(),
            "dlpMetricsMetadata": t.proxy(
                renames["AppsDynamiteSharedDlpMetricsMetadataIn"]
            ).optional(),
            "contentName": t.string().optional(),
            "clonedAuthorizedItemId": t.proxy(renames["AuthorizedItemIdIn"]).optional(),
            "latestVirusScanTimestamp": t.string().optional(),
            "attachmentToken": t.string().optional(),
            "clonedDriveId": t.string().optional(),
            "clonedDriveAction": t.string().optional(),
            "videoReference": t.proxy(
                renames["AppsDynamiteSharedVideoReferenceIn"]
            ).optional(),
            "virusScanResult": t.string().optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionIn"]
            ).optional(),
            "contentType": t.string().optional(),
            "backendUploadMetadata": t.proxy(
                renames["AppsDynamiteSharedBackendUploadMetadataIn"]
            ).optional(),
        }
    ).named(renames["UploadMetadataIn"])
    types["UploadMetadataOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "dlpMetricsMetadata": t.proxy(
                renames["AppsDynamiteSharedDlpMetricsMetadataOut"]
            ).optional(),
            "contentName": t.string().optional(),
            "clonedAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdOut"]
            ).optional(),
            "latestVirusScanTimestamp": t.string().optional(),
            "attachmentToken": t.string().optional(),
            "clonedDriveId": t.string().optional(),
            "clonedDriveAction": t.string().optional(),
            "videoReference": t.proxy(
                renames["AppsDynamiteSharedVideoReferenceOut"]
            ).optional(),
            "virusScanResult": t.string().optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionOut"]
            ).optional(),
            "contentType": t.string().optional(),
            "backendUploadMetadata": t.proxy(
                renames["AppsDynamiteSharedBackendUploadMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadMetadataOut"])
    types["TriggersIn"] = t.struct(
        {"triggers": t.array(t.proxy(renames["TriggerIn"])).optional()}
    ).named(renames["TriggersIn"])
    types["TriggersOut"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggersOut"])
    types["GroupLinkSharingModificationEventIn"] = t.struct(
        {"newStatus": t.string()}
    ).named(renames["GroupLinkSharingModificationEventIn"])
    types["GroupLinkSharingModificationEventOut"] = t.struct(
        {"newStatus": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GroupLinkSharingModificationEventOut"])
    types["SearchApplicationUserStatsIn"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
        }
    ).named(renames["SearchApplicationUserStatsIn"])
    types["SearchApplicationUserStatsOut"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationUserStatsOut"])
    types[
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn"
    ] = t.struct(
        {
            "timed": t.string().optional(),
            "allDay": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(
        renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn"]
    )
    types[
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut"
    ] = t.struct(
        {
            "timed": t.string().optional(),
            "allDay": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut"]
    )
    types["ImapsyncFolderAttributeFolderMessageFlagsIn"] = t.struct(
        {"flagged": t.boolean().optional(), "seen": t.boolean().optional()}
    ).named(renames["ImapsyncFolderAttributeFolderMessageFlagsIn"])
    types["ImapsyncFolderAttributeFolderMessageFlagsOut"] = t.struct(
        {
            "flagged": t.boolean().optional(),
            "seen": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapsyncFolderAttributeFolderMessageFlagsOut"])
    types["LdapUserProtoIn"] = t.struct({"userName": t.string()}).named(
        renames["LdapUserProtoIn"]
    )
    types["LdapUserProtoOut"] = t.struct(
        {"userName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LdapUserProtoOut"])
    types["PersonalLabelTagIn"] = t.struct({"labelId": t.string().optional()}).named(
        renames["PersonalLabelTagIn"]
    )
    types["PersonalLabelTagOut"] = t.struct(
        {
            "labelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalLabelTagOut"])
    types["RpcOptionsIn"] = t.struct(
        {"requestExtensions": t.proxy(renames["MessageSetIn"]).optional()}
    ).named(renames["RpcOptionsIn"])
    types["RpcOptionsOut"] = t.struct(
        {
            "requestExtensions": t.proxy(renames["MessageSetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RpcOptionsOut"])
    types["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"] = t.struct(
        {"filename": t.string()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"] = t.struct(
        {"filename": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"])
    types["RecordingEventIn"] = t.struct(
        {"deviceId": t.string().optional(), "type": t.string().optional()}
    ).named(renames["RecordingEventIn"])
    types["RecordingEventOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordingEventOut"])
    types["PhoneAccessIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "regionCode": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "pin": t.string().optional(),
            "formattedPhoneNumber": t.string().optional(),
        }
    ).named(renames["PhoneAccessIn"])
    types["PhoneAccessOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "regionCode": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "pin": t.string().optional(),
            "formattedPhoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneAccessOut"])
    types["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"])
    types["LabelCreatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelCreatedIn"]
    )
    types["LabelCreatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelCreatedOut"])
    types["AppsDynamiteSharedChatItemGroupInfoIn"] = t.struct(
        {
            "groupName": t.string(),
            "groupReadTimeUsec": t.string().optional(),
            "inlineThreadingEnabled": t.boolean().optional(),
            "attributeCheckerGroupType": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemGroupInfoIn"])
    types["AppsDynamiteSharedChatItemGroupInfoOut"] = t.struct(
        {
            "groupName": t.string(),
            "groupReadTimeUsec": t.string().optional(),
            "inlineThreadingEnabled": t.boolean().optional(),
            "attributeCheckerGroupType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemGroupInfoOut"])
    types["AppsDynamiteStorageSuggestionsSuggestionItemIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["AppsDynamiteStorageSuggestionsSuggestionItemIn"])
    types["AppsDynamiteStorageSuggestionsSuggestionItemOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteStorageSuggestionsSuggestionItemOut"])
    types["FieldViolationIn"] = t.struct(
        {"field": t.string().optional(), "description": t.string().optional()}
    ).named(renames["FieldViolationIn"])
    types["FieldViolationOut"] = t.struct(
        {
            "field": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldViolationOut"])
    types["NameIn"] = t.struct({"displayName": t.string().optional()}).named(
        renames["NameIn"]
    )
    types["NameOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
    types["UserMentionDataIn"] = t.struct(
        {
            "userId": t.string().optional(),
            "userGaiaId": t.string().optional(),
            "email": t.string(),
            "user": t.proxy(renames["PrincipalProtoIn"]).optional(),
        }
    ).named(renames["UserMentionDataIn"])
    types["UserMentionDataOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "userGaiaId": t.string().optional(),
            "email": t.string(),
            "user": t.proxy(renames["PrincipalProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserMentionDataOut"])
    types["ItemMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "title": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeIn"])
            ).optional(),
            "sourceRepositoryUrl": t.string().optional(),
            "objectType": t.string().optional(),
            "interactions": t.array(t.proxy(renames["InteractionIn"])).optional(),
            "keywords": t.array(t.string()).optional(),
            "searchQualityMetadata": t.proxy(
                renames["SearchQualityMetadataIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "containerName": t.string().optional(),
            "mimeType": t.string().optional(),
            "hash": t.string().optional(),
        }
    ).named(renames["ItemMetadataIn"])
    types["ItemMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "title": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeOut"])
            ).optional(),
            "sourceRepositoryUrl": t.string().optional(),
            "objectType": t.string().optional(),
            "interactions": t.array(t.proxy(renames["InteractionOut"])).optional(),
            "keywords": t.array(t.string()).optional(),
            "searchQualityMetadata": t.proxy(
                renames["SearchQualityMetadataOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "containerName": t.string().optional(),
            "mimeType": t.string().optional(),
            "hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemMetadataOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn"
    ] = t.struct(
        {
            "note": t.string().optional(),
            "conferenceId": t.string().optional(),
            "conferenceSolutionId": t.string().optional(),
            "entryPoints": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn"
                    ]
                )
            ).optional(),
            "parameters": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn"
                    ]
                )
            ).optional(),
            "error": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn"
                ]
            ).optional(),
        }
    ).named(
        renames["AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn"]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut"
    ] = t.struct(
        {
            "note": t.string().optional(),
            "conferenceId": t.string().optional(),
            "conferenceSolutionId": t.string().optional(),
            "entryPoints": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut"
                    ]
                )
            ).optional(),
            "parameters": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut"]
    )
    types["DebugOptionsIn"] = t.struct(
        {"enableDebugging": t.boolean().optional()}
    ).named(renames["DebugOptionsIn"])
    types["DebugOptionsOut"] = t.struct(
        {
            "enableDebugging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugOptionsOut"])
    types["AppsDynamiteV1ApiCompatV1ActionIn"] = t.struct(
        {
            "style": t.string().optional(),
            "text": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "confirm": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1ActionConfirmIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionIn"])
    types["AppsDynamiteV1ApiCompatV1ActionOut"] = t.struct(
        {
            "style": t.string().optional(),
            "text": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "confirm": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1ActionConfirmOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionOut"])
    types["QuerySourceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "operators": t.array(t.proxy(renames["QueryOperatorIn"])).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "shortName": t.string().optional(),
        }
    ).named(renames["QuerySourceIn"])
    types["QuerySourceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "operators": t.array(t.proxy(renames["QueryOperatorOut"])).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "shortName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuerySourceOut"])
    types["FuseboxPrefUpdatePreStateIn"] = t.struct({"value": t.string()}).named(
        renames["FuseboxPrefUpdatePreStateIn"]
    )
    types["FuseboxPrefUpdatePreStateOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FuseboxPrefUpdatePreStateOut"])
    types["AppsDynamiteSharedChatItemActivityInfoIn"] = t.struct(
        {
            "feedItemNudge": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"]
            ),
            "feedItemThreadReply": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"]
            ),
            "feedItemReactions": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"]
            ),
            "feedItemUserMention": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"]
            ),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoIn"])
    types["AppsDynamiteSharedChatItemActivityInfoOut"] = t.struct(
        {
            "feedItemNudge": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut"]
            ),
            "feedItemThreadReply": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut"]
            ),
            "feedItemReactions": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"]
            ),
            "feedItemUserMention": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoOut"])
    types["AppsDynamiteSharedOrganizationInfoConsumerInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedOrganizationInfoConsumerInfoIn"])
    types["AppsDynamiteSharedOrganizationInfoConsumerInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedOrganizationInfoConsumerInfoOut"])
    types["FacetOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "sourceName": t.string().optional(),
            "objectType": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsIn"]
            ).optional(),
            "numFacetBuckets": t.integer().optional(),
        }
    ).named(renames["FacetOptionsIn"])
    types["FacetOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "sourceName": t.string().optional(),
            "objectType": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsOut"]
            ).optional(),
            "numFacetBuckets": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetOptionsOut"])
    types["GoogleDocsMetadataIn"] = t.struct(
        {
            "numSubscribers": t.integer().optional(),
            "lastContentModifiedTimestamp": t.string().optional(),
            "fileExtension": t.string().optional(),
            "documentType": t.string().optional(),
            "resultInfo": t.proxy(renames["GoogleDocsResultInfoIn"]).optional(),
            "numViewers": t.integer().optional(),
            "aclInfo": t.proxy(renames["AclInfoIn"]).optional(),
            "typeInfo": t.proxy(renames["TypeInfoIn"]).optional(),
        }
    ).named(renames["GoogleDocsMetadataIn"])
    types["GoogleDocsMetadataOut"] = t.struct(
        {
            "numSubscribers": t.integer().optional(),
            "lastContentModifiedTimestamp": t.string().optional(),
            "fileExtension": t.string().optional(),
            "documentType": t.string().optional(),
            "resultInfo": t.proxy(renames["GoogleDocsResultInfoOut"]).optional(),
            "numViewers": t.integer().optional(),
            "aclInfo": t.proxy(renames["AclInfoOut"]).optional(),
            "typeInfo": t.proxy(renames["TypeInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDocsMetadataOut"])
    types["HashtagDataIn"] = t.struct({"searchText": t.string()}).named(
        renames["HashtagDataIn"]
    )
    types["HashtagDataOut"] = t.struct(
        {
            "searchText": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashtagDataOut"])
    types["AutoCompleteItemIn"] = t.struct({"text": t.string()}).named(
        renames["AutoCompleteItemIn"]
    )
    types["AutoCompleteItemOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AutoCompleteItemOut"])
    types["SearchResultIn"] = t.struct(
        {
            "url": t.string().optional(),
            "debugInfo": t.proxy(renames["ResultDebugInfoIn"]).optional(),
            "title": t.string().optional(),
            "snippet": t.proxy(renames["SnippetIn"]).optional(),
            "clusteredResults": t.array(t.proxy(renames["SearchResultIn"])).optional(),
            "metadata": t.proxy(renames["MetadataIn"]).optional(),
        }
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "url": t.string().optional(),
            "debugInfo": t.proxy(renames["ResultDebugInfoOut"]).optional(),
            "title": t.string().optional(),
            "snippet": t.proxy(renames["SnippetOut"]).optional(),
            "clusteredResults": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["ObjectDefinitionIn"] = t.struct(
        {
            "options": t.proxy(renames["ObjectOptionsIn"]).optional(),
            "name": t.string().optional(),
            "propertyDefinitions": t.array(
                t.proxy(renames["PropertyDefinitionIn"])
            ).optional(),
        }
    ).named(renames["ObjectDefinitionIn"])
    types["ObjectDefinitionOut"] = t.struct(
        {
            "options": t.proxy(renames["ObjectOptionsOut"]).optional(),
            "name": t.string().optional(),
            "propertyDefinitions": t.array(
                t.proxy(renames["PropertyDefinitionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectDefinitionOut"])
    types["LabelDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelDeletedIn"]
    )
    types["LabelDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelDeletedOut"])
    types["GoogleChatV1ContextualAddOnMarkupCardSectionIn"] = t.struct(
        {
            "widgets": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupIn"])
            ).optional(),
            "header": t.string().optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardSectionIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardSectionOut"] = t.struct(
        {
            "widgets": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupOut"])
            ).optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardSectionOut"])
    types["ToolbarIn"] = t.struct(
        {"name": t.string(), "color": t.string().optional(), "iconUrl": t.string()}
    ).named(renames["ToolbarIn"])
    types["ToolbarOut"] = t.struct(
        {
            "name": t.string(),
            "color": t.string().optional(),
            "iconUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolbarOut"])
    types["DlpScanSummaryIn"] = t.struct(
        {
            "scanNotApplicableForContext": t.boolean().optional(),
            "scanOutcome": t.string().optional(),
            "dlpAction": t.proxy(renames["DlpActionIn"]),
            "scanId": t.string().optional(),
        }
    ).named(renames["DlpScanSummaryIn"])
    types["DlpScanSummaryOut"] = t.struct(
        {
            "scanNotApplicableForContext": t.boolean().optional(),
            "scanOutcome": t.string().optional(),
            "dlpAction": t.proxy(renames["DlpActionOut"]),
            "scanId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpScanSummaryOut"])
    types["MessageIn"] = t.struct(
        {
            "personalLabels": t.array(
                t.proxy(renames["PersonalLabelTagIn"])
            ).optional(),
            "originAppSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedOriginAppSuggestionIn"])
            ).optional(),
            "privateMessageViewer": t.proxy(renames["UserIdIn"]).optional(),
            "communalLabels": t.array(
                t.proxy(renames["CommunalLabelTagIn"])
            ).optional(),
            "attributes": t.proxy(renames["MessageAttributesIn"]).optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataIn"])).optional(),
            "props": t.proxy(renames["MessagePropsIn"]).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationIn"])).optional(),
            "appProfile": t.proxy(renames["AppsDynamiteSharedAppProfileIn"]).optional(),
            "deletedByVault": t.boolean().optional(),
            "createTime": t.string().optional(),
            "creatorId": t.proxy(renames["UserIdIn"]).optional(),
            "reactions": t.array(
                t.proxy(renames["AppsDynamiteSharedReactionIn"])
            ).optional(),
            "secondaryMessageKey": t.string().optional(),
            "isContentPurged": t.boolean().optional(),
            "editableBy": t.string().optional(),
            "privateMessageInfos": t.array(
                t.proxy(renames["PrivateMessageInfoIn"])
            ).optional(),
            "lastEditTime": t.string().optional(),
            "deleteTimeForRequester": t.string().optional(),
            "id": t.proxy(renames["MessageIdIn"]).optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryIn"]).optional(),
            "fallbackText": t.string().optional(),
            "richTextFormattingType": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "messageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedMessageIntegrationPayloadIn"]
            ).optional(),
            "botResponses": t.array(t.proxy(renames["BotResponseIn"])).optional(),
            "localId": t.string().optional(),
            "textBody": t.string().optional(),
            "deleteTime": t.string().optional(),
            "messageState": t.string().optional(),
            "messageOrigin": t.string().optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsIn"]
            ).optional(),
            "tombstoneMetadata": t.proxy(renames["TombstoneMetadataIn"]).optional(),
            "updaterId": t.proxy(renames["UserIdIn"]).optional(),
            "deletableBy": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "quotedByState": t.string().optional(),
            "personalLabels": t.array(
                t.proxy(renames["PersonalLabelTagOut"])
            ).optional(),
            "quotedMessageMetadata": t.proxy(
                renames["QuotedMessageMetadataOut"]
            ).optional(),
            "originAppSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedOriginAppSuggestionOut"])
            ).optional(),
            "privateMessageViewer": t.proxy(renames["UserIdOut"]).optional(),
            "communalLabels": t.array(
                t.proxy(renames["CommunalLabelTagOut"])
            ).optional(),
            "attributes": t.proxy(renames["MessageAttributesOut"]).optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataOut"])).optional(),
            "props": t.proxy(renames["MessagePropsOut"]).optional(),
            "reports": t.array(t.proxy(renames["ContentReportOut"])).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "appProfile": t.proxy(
                renames["AppsDynamiteSharedAppProfileOut"]
            ).optional(),
            "isInlineReply": t.boolean().optional(),
            "deletedByVault": t.boolean().optional(),
            "createTime": t.string().optional(),
            "creatorId": t.proxy(renames["UserIdOut"]).optional(),
            "reactions": t.array(
                t.proxy(renames["AppsDynamiteSharedReactionOut"])
            ).optional(),
            "secondaryMessageKey": t.string().optional(),
            "isContentPurged": t.boolean().optional(),
            "editableBy": t.string().optional(),
            "privateMessageInfos": t.array(
                t.proxy(renames["PrivateMessageInfoOut"])
            ).optional(),
            "lastEditTime": t.string().optional(),
            "deleteTimeForRequester": t.string().optional(),
            "id": t.proxy(renames["MessageIdOut"]).optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryOut"]).optional(),
            "fallbackText": t.string().optional(),
            "richTextFormattingType": t.string().optional(),
            "contentReportSummary": t.proxy(renames["ContentReportSummaryOut"]),
            "lastUpdateTime": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "messageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedMessageIntegrationPayloadOut"]
            ).optional(),
            "botResponses": t.array(t.proxy(renames["BotResponseOut"])).optional(),
            "localId": t.string().optional(),
            "textBody": t.string().optional(),
            "deleteTime": t.string().optional(),
            "messageState": t.string().optional(),
            "messageOrigin": t.string().optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsOut"]
            ).optional(),
            "tombstoneMetadata": t.proxy(renames["TombstoneMetadataOut"]).optional(),
            "updaterId": t.proxy(renames["UserIdOut"]).optional(),
            "deletableBy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"])
    types["AppsDynamiteSharedSegmentedMembershipCountsIn"] = t.struct(
        {
            "value": t.array(
                t.proxy(renames["AppsDynamiteSharedSegmentedMembershipCountIn"])
            )
        }
    ).named(renames["AppsDynamiteSharedSegmentedMembershipCountsIn"])
    types["AppsDynamiteSharedSegmentedMembershipCountsOut"] = t.struct(
        {
            "value": t.array(
                t.proxy(renames["AppsDynamiteSharedSegmentedMembershipCountOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedSegmentedMembershipCountsOut"])
    types["DeliveryMediumIn"] = t.struct(
        {
            "selfPhone": t.proxy(renames["VoicePhoneNumberIn"]).optional(),
            "mediumType": t.string().optional(),
        }
    ).named(renames["DeliveryMediumIn"])
    types["DeliveryMediumOut"] = t.struct(
        {
            "selfPhone": t.proxy(renames["VoicePhoneNumberOut"]).optional(),
            "mediumType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryMediumOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn"
    ] = t.struct(
        {"authenticationUrl": t.string().optional(), "type": t.string().optional()}
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn"
        ]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut"
    ] = t.struct(
        {
            "authenticationUrl": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut"
        ]
    )
    types["AckInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AckInfoIn"]
    )
    types["AckInfoOut"] = t.struct(
        {
            "unackedDeviceCount": t.integer().optional(),
            "unackedDeviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AckInfoOut"])
    types["SimpleSecretLabelProtoIn"] = t.struct(
        {
            "capabilityId": t.integer().optional(),
            "type": t.string().optional(),
            "genericLabel": t.string().optional(),
            "inviteId": t.string().optional(),
        }
    ).named(renames["SimpleSecretLabelProtoIn"])
    types["SimpleSecretLabelProtoOut"] = t.struct(
        {
            "capabilityId": t.integer().optional(),
            "type": t.string().optional(),
            "genericLabel": t.string().optional(),
            "inviteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleSecretLabelProtoOut"])
    types["PropertyDefinitionIn"] = t.struct(
        {
            "displayOptions": t.proxy(renames["PropertyDisplayOptionsIn"]).optional(),
            "datePropertyOptions": t.proxy(renames["DatePropertyOptionsIn"]),
            "isSortable": t.boolean().optional(),
            "integerPropertyOptions": t.proxy(renames["IntegerPropertyOptionsIn"]),
            "enumPropertyOptions": t.proxy(renames["EnumPropertyOptionsIn"]),
            "isSuggestable": t.boolean().optional(),
            "isReturnable": t.boolean().optional(),
            "isRepeatable": t.boolean().optional(),
            "htmlPropertyOptions": t.proxy(renames["HtmlPropertyOptionsIn"]),
            "booleanPropertyOptions": t.proxy(renames["BooleanPropertyOptionsIn"]),
            "textPropertyOptions": t.proxy(renames["TextPropertyOptionsIn"]),
            "name": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "timestampPropertyOptions": t.proxy(renames["TimestampPropertyOptionsIn"]),
            "isWildcardSearchable": t.boolean().optional(),
            "doublePropertyOptions": t.proxy(renames["DoublePropertyOptionsIn"]),
            "objectPropertyOptions": t.proxy(renames["ObjectPropertyOptionsIn"]),
        }
    ).named(renames["PropertyDefinitionIn"])
    types["PropertyDefinitionOut"] = t.struct(
        {
            "displayOptions": t.proxy(renames["PropertyDisplayOptionsOut"]).optional(),
            "datePropertyOptions": t.proxy(renames["DatePropertyOptionsOut"]),
            "isSortable": t.boolean().optional(),
            "integerPropertyOptions": t.proxy(renames["IntegerPropertyOptionsOut"]),
            "enumPropertyOptions": t.proxy(renames["EnumPropertyOptionsOut"]),
            "isSuggestable": t.boolean().optional(),
            "isReturnable": t.boolean().optional(),
            "isRepeatable": t.boolean().optional(),
            "htmlPropertyOptions": t.proxy(renames["HtmlPropertyOptionsOut"]),
            "booleanPropertyOptions": t.proxy(renames["BooleanPropertyOptionsOut"]),
            "textPropertyOptions": t.proxy(renames["TextPropertyOptionsOut"]),
            "name": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "timestampPropertyOptions": t.proxy(renames["TimestampPropertyOptionsOut"]),
            "isWildcardSearchable": t.boolean().optional(),
            "doublePropertyOptions": t.proxy(renames["DoublePropertyOptionsOut"]),
            "objectPropertyOptions": t.proxy(renames["ObjectPropertyOptionsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyDefinitionOut"])
    types["CustomerSettingsIn"] = t.struct(
        {
            "vpcSettings": t.proxy(renames["VPCSettingsIn"]).optional(),
            "auditLoggingSettings": t.proxy(
                renames["AuditLoggingSettingsIn"]
            ).optional(),
        }
    ).named(renames["CustomerSettingsIn"])
    types["CustomerSettingsOut"] = t.struct(
        {
            "vpcSettings": t.proxy(renames["VPCSettingsOut"]).optional(),
            "auditLoggingSettings": t.proxy(
                renames["AuditLoggingSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerSettingsOut"])
    types["EmbedClientItemIn"] = t.struct(
        {
            "transientData": t.proxy(renames["TransientDataIn"]).optional(),
            "canonicalId": t.string().optional(),
            "type": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "deepLinkData": t.proxy(renames["DeepLinkDataIn"]).optional(),
            "provenance": t.proxy(renames["ProvenanceIn"]).optional(),
            "signature": t.string().optional(),
            "renderId": t.string().optional(),
        }
    ).named(renames["EmbedClientItemIn"])
    types["EmbedClientItemOut"] = t.struct(
        {
            "transientData": t.proxy(renames["TransientDataOut"]).optional(),
            "canonicalId": t.string().optional(),
            "type": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "deepLinkData": t.proxy(renames["DeepLinkDataOut"]).optional(),
            "provenance": t.proxy(renames["ProvenanceOut"]).optional(),
            "signature": t.string().optional(),
            "renderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbedClientItemOut"])
    types["CheckAccessResponseIn"] = t.struct(
        {"hasAccess": t.boolean().optional()}
    ).named(renames["CheckAccessResponseIn"])
    types["CheckAccessResponseOut"] = t.struct(
        {
            "hasAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckAccessResponseOut"])
    types["BroadcastAccessIn"] = t.struct(
        {"accessPolicy": t.string().optional(), "viewUrl": t.string().optional()}
    ).named(renames["BroadcastAccessIn"])
    types["BroadcastAccessOut"] = t.struct(
        {
            "accessPolicy": t.string().optional(),
            "viewUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BroadcastAccessOut"])
    types["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"])
    types["AppsDynamiteStorageOpenLinkIn"] = t.struct(
        {
            "appUri": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIn"]
            ).optional(),
            "openAs": t.string(),
            "url": t.string().optional(),
            "onClose": t.string(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkIn"])
    types["AppsDynamiteStorageOpenLinkOut"] = t.struct(
        {
            "appUri": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriOut"]
            ).optional(),
            "openAs": t.string(),
            "url": t.string().optional(),
            "onClose": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkOut"])
    types["ListUnmappedIdentitiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unmappedIdentities": t.array(t.proxy(renames["UnmappedIdentityIn"])),
        }
    ).named(renames["ListUnmappedIdentitiesResponseIn"])
    types["ListUnmappedIdentitiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unmappedIdentities": t.array(t.proxy(renames["UnmappedIdentityOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUnmappedIdentitiesResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["MessageDeletedIn"] = t.struct(
        {
            "wonderCardMappings": t.array(
                t.proxy(renames["WonderCardDeleteIn"])
            ).optional(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
            "imapSyncMappings": t.array(
                t.proxy(renames["ImapSyncDeleteIn"])
            ).optional(),
        }
    ).named(renames["MessageDeletedIn"])
    types["MessageDeletedOut"] = t.struct(
        {
            "wonderCardMappings": t.array(
                t.proxy(renames["WonderCardDeleteOut"])
            ).optional(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "imapSyncMappings": t.array(
                t.proxy(renames["ImapSyncDeleteOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageDeletedOut"])
    types["PollItemsRequestIn"] = t.struct(
        {
            "limit": t.integer().optional(),
            "statusCodes": t.array(t.string()).optional(),
            "connectorName": t.string().optional(),
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["PollItemsRequestIn"])
    types["PollItemsRequestOut"] = t.struct(
        {
            "limit": t.integer().optional(),
            "statusCodes": t.array(t.string()).optional(),
            "connectorName": t.string().optional(),
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollItemsRequestOut"])
    types["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut"])
    types["AttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.proxy(renames["CaribouAttributeValueIn"]),
        }
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.proxy(renames["CaribouAttributeValueOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["ListQuerySourcesResponseIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["QuerySourceIn"])),
            "nextPageToken": t.string(),
        }
    ).named(renames["ListQuerySourcesResponseIn"])
    types["ListQuerySourcesResponseOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["QuerySourceOut"])),
            "nextPageToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQuerySourcesResponseOut"])
    types["DoublePropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["DoubleOperatorOptionsIn"]).optional()}
    ).named(renames["DoublePropertyOptionsIn"])
    types["DoublePropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["DoubleOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoublePropertyOptionsOut"])
    types["DeleteQueueItemsRequestIn"] = t.struct(
        {
            "queue": t.string().optional(),
            "connectorName": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["DeleteQueueItemsRequestIn"])
    types["DeleteQueueItemsRequestOut"] = t.struct(
        {
            "queue": t.string().optional(),
            "connectorName": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteQueueItemsRequestOut"])
    types["AddonComposeUiActionMarkupIn"] = t.struct({"type": t.string()}).named(
        renames["AddonComposeUiActionMarkupIn"]
    )
    types["AddonComposeUiActionMarkupOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddonComposeUiActionMarkupOut"])
    types["ErrorMessageIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]), "errorMessage": t.string()}
    ).named(renames["ErrorMessageIn"])
    types["ErrorMessageOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]),
            "errorMessage": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorMessageOut"])
    types["FreshnessOptionsIn"] = t.struct(
        {
            "freshnessDuration": t.string().optional(),
            "freshnessProperty": t.string().optional(),
        }
    ).named(renames["FreshnessOptionsIn"])
    types["FreshnessOptionsOut"] = t.struct(
        {
            "freshnessDuration": t.string().optional(),
            "freshnessProperty": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreshnessOptionsOut"])
    types["UserIn"] = t.struct(
        {
            "organizationInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoIn"]
            ).optional(),
            "userAccountState": t.string().optional(),
            "firstName": t.string().optional(),
            "deleted": t.boolean().optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "blockRelationship": t.proxy(
                renames["AppsDynamiteSharedUserBlockRelationshipIn"]
            ).optional(),
            "lastName": t.string().optional(),
            "phoneNumber": t.array(
                t.proxy(renames["AppsDynamiteSharedPhoneNumberIn"])
            ).optional(),
            "botInfo": t.proxy(renames["BotInfoIn"]).optional(),
            "isAnonymous": t.boolean().optional(),
            "userProfileVisibility": t.string().optional(),
            "avatarUrl": t.string().optional(),
            "gender": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "organizationInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoOut"]
            ).optional(),
            "userAccountState": t.string().optional(),
            "firstName": t.string().optional(),
            "deleted": t.boolean().optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "blockRelationship": t.proxy(
                renames["AppsDynamiteSharedUserBlockRelationshipOut"]
            ).optional(),
            "lastName": t.string().optional(),
            "phoneNumber": t.array(
                t.proxy(renames["AppsDynamiteSharedPhoneNumberOut"])
            ).optional(),
            "botInfo": t.proxy(renames["BotInfoOut"]).optional(),
            "isAnonymous": t.boolean().optional(),
            "userProfileVisibility": t.string().optional(),
            "avatarUrl": t.string().optional(),
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["MatchInfoIn"] = t.struct(
        {"matchingImageReferenceKey": t.array(t.string()).optional()}
    ).named(renames["MatchInfoIn"])
    types["MatchInfoOut"] = t.struct(
        {
            "matchingImageReferenceKey": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchInfoOut"])
    types["ChatContentExtensionIn"] = t.struct(
        {
            "dynamitePlaceholderMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataIn"]
            ).optional(),
            "otrModificationEvent": t.proxy(renames["OtrModificationEventIn"]),
            "membershipChangeEvent": t.proxy(
                renames["MembershipChangeEventIn"]
            ).optional(),
            "inviteAcceptedEvent": t.proxy(renames["InviteAcceptedEventIn"]).optional(),
            "otrChatMessageEvent": t.proxy(renames["OtrChatMessageEventIn"]).optional(),
            "renameEvent": t.proxy(renames["RenameEventIn"]),
            "annotation": t.array(t.proxy(renames["EventAnnotationIn"])).optional(),
            "groupLinkSharingModificationEvent": t.proxy(
                renames["GroupLinkSharingModificationEventIn"]
            ).optional(),
            "eventOtrStatus": t.string().optional(),
            "hangoutEvent": t.proxy(renames["HangoutEventIn"]).optional(),
        }
    ).named(renames["ChatContentExtensionIn"])
    types["ChatContentExtensionOut"] = t.struct(
        {
            "dynamitePlaceholderMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataOut"]
            ).optional(),
            "otrModificationEvent": t.proxy(renames["OtrModificationEventOut"]),
            "membershipChangeEvent": t.proxy(
                renames["MembershipChangeEventOut"]
            ).optional(),
            "inviteAcceptedEvent": t.proxy(
                renames["InviteAcceptedEventOut"]
            ).optional(),
            "otrChatMessageEvent": t.proxy(
                renames["OtrChatMessageEventOut"]
            ).optional(),
            "renameEvent": t.proxy(renames["RenameEventOut"]),
            "annotation": t.array(t.proxy(renames["EventAnnotationOut"])).optional(),
            "groupLinkSharingModificationEvent": t.proxy(
                renames["GroupLinkSharingModificationEventOut"]
            ).optional(),
            "eventOtrStatus": t.string().optional(),
            "hangoutEvent": t.proxy(renames["HangoutEventOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatContentExtensionOut"])
    types["ImapSyncDeleteIn"] = t.struct(
        {
            "mappings": t.proxy(renames["FolderAttributeIn"]).optional(),
            "msgId": t.string(),
        }
    ).named(renames["ImapSyncDeleteIn"])
    types["ImapSyncDeleteOut"] = t.struct(
        {
            "mappings": t.proxy(renames["FolderAttributeOut"]).optional(),
            "msgId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapSyncDeleteOut"])
    types["PhotoIn"] = t.struct({"url": t.string().optional()}).named(
        renames["PhotoIn"]
    )
    types["PhotoOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["ClientContextIn"] = t.struct(
        {
            "clientOperationId": t.string().optional(),
            "userIp": t.string().optional(),
            "sessionContext": t.proxy(renames["SessionContextIn"]).optional(),
            "clientType": t.string().optional(),
        }
    ).named(renames["ClientContextIn"])
    types["ClientContextOut"] = t.struct(
        {
            "clientOperationId": t.string().optional(),
            "userIp": t.string().optional(),
            "sessionContext": t.proxy(renames["SessionContextOut"]).optional(),
            "clientType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientContextOut"])
    types["UploadItemRefIn"] = t.struct({"name": t.string().optional()}).named(
        renames["UploadItemRefIn"]
    )
    types["UploadItemRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadItemRefOut"])
    types["CoActivityIn"] = t.struct(
        {"coActivityApp": t.string().optional(), "activityTitle": t.string().optional()}
    ).named(renames["CoActivityIn"])
    types["CoActivityOut"] = t.struct(
        {
            "coActivityApp": t.string().optional(),
            "activityTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CoActivityOut"])
    types["SelectionItemIn"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["SelectionItemIn"])
    types["SelectionItemOut"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionItemOut"])
    types["InviteeInfoIn"] = t.struct(
        {
            "userId": t.proxy(renames["UserIdIn"]).optional(),
            "email": t.string().optional(),
        }
    ).named(renames["InviteeInfoIn"])
    types["InviteeInfoOut"] = t.struct(
        {
            "userId": t.proxy(renames["UserIdOut"]).optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InviteeInfoOut"])
    types["DataSourceIndexStatsIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusIn"])
            ).optional(),
        }
    ).named(renames["DataSourceIndexStatsIn"])
    types["DataSourceIndexStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceIndexStatsOut"])
    types["AppsDynamiteStorageCardCardActionIn"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardCardActionIn"])
    types["AppsDynamiteStorageCardCardActionOut"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardCardActionOut"])
    types["GoogleChatV1WidgetMarkupIn"] = t.struct(
        {
            "textParagraph": t.proxy(
                renames["GoogleChatV1WidgetMarkupTextParagraphIn"]
            ).optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupButtonIn"])
            ).optional(),
            "image": t.proxy(renames["GoogleChatV1WidgetMarkupImageIn"]).optional(),
            "keyValue": t.proxy(
                renames["GoogleChatV1WidgetMarkupKeyValueIn"]
            ).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupIn"])
    types["GoogleChatV1WidgetMarkupOut"] = t.struct(
        {
            "textParagraph": t.proxy(
                renames["GoogleChatV1WidgetMarkupTextParagraphOut"]
            ).optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupButtonOut"])
            ).optional(),
            "image": t.proxy(renames["GoogleChatV1WidgetMarkupImageOut"]).optional(),
            "keyValue": t.proxy(
                renames["GoogleChatV1WidgetMarkupKeyValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupOut"])
    types["MetalineIn"] = t.struct(
        {"properties": t.array(t.proxy(renames["DisplayedPropertyIn"])).optional()}
    ).named(renames["MetalineIn"])
    types["MetalineOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["DisplayedPropertyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetalineOut"])
    types["SpellResultIn"] = t.struct({"suggestedQuery": t.string().optional()}).named(
        renames["SpellResultIn"]
    )
    types["SpellResultOut"] = t.struct(
        {
            "suggestedQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpellResultOut"])
    types["DoubleOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["DoubleOperatorOptionsIn"])
    types["DoubleOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleOperatorOptionsOut"])
    types["GetCustomerSearchApplicationStatsResponseIn"] = t.struct(
        {
            "averageSearchApplicationCount": t.string().optional(),
            "stats": t.array(
                t.proxy(renames["CustomerSearchApplicationStatsIn"])
            ).optional(),
        }
    ).named(renames["GetCustomerSearchApplicationStatsResponseIn"])
    types["GetCustomerSearchApplicationStatsResponseOut"] = t.struct(
        {
            "averageSearchApplicationCount": t.string().optional(),
            "stats": t.array(
                t.proxy(renames["CustomerSearchApplicationStatsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerSearchApplicationStatsResponseOut"])
    types["AppsDynamiteSharedAssistantFeedbackContextIn"] = t.struct(
        {
            "feedbackChips": t.array(
                t.proxy(
                    renames["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn"]
                )
            ).optional(),
            "thumbsFeedback": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantFeedbackContextIn"])
    types["AppsDynamiteSharedAssistantFeedbackContextOut"] = t.struct(
        {
            "feedbackChips": t.array(
                t.proxy(
                    renames["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut"]
                )
            ).optional(),
            "thumbsFeedback": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantFeedbackContextOut"])
    types["IncomingWebhookChangedMetadataIn"] = t.struct(
        {
            "oldIncomingWebhookName": t.string().optional(),
            "type": t.string().optional(),
            "obfuscatedIncomingWebhookId": t.string().optional(),
            "incomingWebhookName": t.string().optional(),
            "initiatorId": t.proxy(renames["UserIdIn"]).optional(),
            "initiatorProfile": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["IncomingWebhookChangedMetadataIn"])
    types["IncomingWebhookChangedMetadataOut"] = t.struct(
        {
            "oldIncomingWebhookName": t.string().optional(),
            "type": t.string().optional(),
            "obfuscatedIncomingWebhookId": t.string().optional(),
            "incomingWebhookName": t.string().optional(),
            "initiatorId": t.proxy(renames["UserIdOut"]).optional(),
            "initiatorProfile": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncomingWebhookChangedMetadataOut"])
    types["FilterOptionsIn"] = t.struct(
        {
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "objectType": t.string().optional(),
        }
    ).named(renames["FilterOptionsIn"])
    types["FilterOptionsOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOptionsOut"])
    types["ChatConserverDynamitePlaceholderMetadataIn"] = t.struct(
        {
            "botMessageMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"]
            ),
            "videoCallMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"]
            ),
            "deleteMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"]
            ),
            "editMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"]
            ),
            "attachmentMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"]
            ),
            "tasksMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"]
            ),
            "spaceUrl": t.string().optional(),
            "calendarEventMetadata": t.proxy(
                renames[
                    "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"
                ]
            ),
        }
    ).named(renames["ChatConserverDynamitePlaceholderMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataOut"] = t.struct(
        {
            "botMessageMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut"]
            ),
            "videoCallMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut"]
            ),
            "deleteMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"]
            ),
            "editMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"]
            ),
            "attachmentMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"]
            ),
            "tasksMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"]
            ),
            "spaceUrl": t.string().optional(),
            "calendarEventMetadata": t.proxy(
                renames[
                    "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatConserverDynamitePlaceholderMetadataOut"])
    types["AppsDynamiteStorageSelectionInputIn"] = t.struct(
        {
            "type": t.string(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "label": t.string().optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageSelectionInputSelectionItemIn"])
            ),
            "name": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputIn"])
    types["AppsDynamiteStorageSelectionInputOut"] = t.struct(
        {
            "type": t.string(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "label": t.string().optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageSelectionInputSelectionItemOut"])
            ),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputOut"])
    types["ResetSearchApplicationRequestIn"] = t.struct(
        {"debugOptions": t.proxy(renames["DebugOptionsIn"]).optional()}
    ).named(renames["ResetSearchApplicationRequestIn"])
    types["ResetSearchApplicationRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetSearchApplicationRequestOut"])
    types["DatePropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["DateOperatorOptionsIn"]).optional()}
    ).named(renames["DatePropertyOptionsIn"])
    types["DatePropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["DateOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatePropertyOptionsOut"])
    types["YouTubeLiveBroadcastEventIn"] = t.struct(
        {
            "brandAccountGaiaId": t.string().optional(),
            "channelId": t.string().optional(),
            "broadcastId": t.string().optional(),
        }
    ).named(renames["YouTubeLiveBroadcastEventIn"])
    types["YouTubeLiveBroadcastEventOut"] = t.struct(
        {
            "brandAccountGaiaId": t.string().optional(),
            "viewUrl": t.string().optional(),
            "channelId": t.string().optional(),
            "broadcastId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeLiveBroadcastEventOut"])
    types["AppsDynamiteSharedAssistantAnnotationDataIn"] = t.struct(
        {
            "suggestion": t.proxy(
                renames["AppsDynamiteSharedAssistantSuggestionIn"]
            ).optional(),
            "unfulfillable": t.proxy(
                renames["AppsDynamiteSharedAssistantUnfulfillableRequestIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantAnnotationDataIn"])
    types["AppsDynamiteSharedAssistantAnnotationDataOut"] = t.struct(
        {
            "suggestion": t.proxy(
                renames["AppsDynamiteSharedAssistantSuggestionOut"]
            ).optional(),
            "unfulfillable": t.proxy(
                renames["AppsDynamiteSharedAssistantUnfulfillableRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantAnnotationDataOut"])
    types["ContentReportIn"] = t.struct(
        {
            "revisionCreateTimestamp": t.string().optional(),
            "reportJustification": t.proxy(
                renames["ContentReportJustificationIn"]
            ).optional(),
            "reporterUserId": t.proxy(renames["UserIdIn"]).optional(),
            "reportType": t.proxy(
                renames["AppsDynamiteSharedContentReportTypeIn"]
            ).optional(),
            "reportCreateTimestamp": t.string().optional(),
        }
    ).named(renames["ContentReportIn"])
    types["ContentReportOut"] = t.struct(
        {
            "revisionCreateTimestamp": t.string().optional(),
            "reportJustification": t.proxy(
                renames["ContentReportJustificationOut"]
            ).optional(),
            "reporterUserId": t.proxy(renames["UserIdOut"]).optional(),
            "reportType": t.proxy(
                renames["AppsDynamiteSharedContentReportTypeOut"]
            ).optional(),
            "reportCreateTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentReportOut"])
    types["SimpleSecretHolderProtoIn"] = t.struct(
        {"label": t.proxy(renames["SimpleSecretLabelProtoIn"]).optional()}
    ).named(renames["SimpleSecretHolderProtoIn"])
    types["SimpleSecretHolderProtoOut"] = t.struct(
        {
            "label": t.proxy(renames["SimpleSecretLabelProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleSecretHolderProtoOut"])
    types["AllAuthenticatedUsersProtoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AllAuthenticatedUsersProtoIn"])
    types["AllAuthenticatedUsersProtoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AllAuthenticatedUsersProtoOut"])
    types["UpdateBccRecipientsIn"] = t.struct(
        {"bccRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateBccRecipientsIn"])
    types["UpdateBccRecipientsOut"] = t.struct(
        {
            "bccRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBccRecipientsOut"])
    types["AppsDynamiteSharedOrganizationInfoCustomerInfoIn"] = t.struct(
        {"customerId": t.proxy(renames["CustomerIdIn"])}
    ).named(renames["AppsDynamiteSharedOrganizationInfoCustomerInfoIn"])
    types["AppsDynamiteSharedOrganizationInfoCustomerInfoOut"] = t.struct(
        {
            "customerId": t.proxy(renames["CustomerIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedOrganizationInfoCustomerInfoOut"])
    types["CardIn"] = t.struct(
        {
            "cardActions": t.array(t.proxy(renames["CardActionIn"])),
            "header": t.proxy(renames["CardHeaderIn"]),
            "sections": t.array(t.proxy(renames["SectionIn"])),
            "displayStyle": t.string(),
            "name": t.string().optional(),
            "fixedFooter": t.proxy(renames["FixedFooterIn"]),
            "peekCardHeader": t.proxy(renames["CardHeaderIn"]).optional(),
        }
    ).named(renames["CardIn"])
    types["CardOut"] = t.struct(
        {
            "cardActions": t.array(t.proxy(renames["CardActionOut"])),
            "header": t.proxy(renames["CardHeaderOut"]),
            "sections": t.array(t.proxy(renames["SectionOut"])),
            "displayStyle": t.string(),
            "name": t.string().optional(),
            "fixedFooter": t.proxy(renames["FixedFooterOut"]),
            "peekCardHeader": t.proxy(renames["CardHeaderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardOut"])
    types["HangoutVideoEventMetadataIn"] = t.struct(
        {"hangoutVideoType": t.string()}
    ).named(renames["HangoutVideoEventMetadataIn"])
    types["HangoutVideoEventMetadataOut"] = t.struct(
        {
            "hangoutVideoType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutVideoEventMetadataOut"])
    types["LabelAddedIn"] = t.struct(
        {
            "labelName": t.string(),
            "labelId": t.string(),
            "syncId": t.integer(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
        }
    ).named(renames["LabelAddedIn"])
    types["LabelAddedOut"] = t.struct(
        {
            "labelName": t.string(),
            "labelId": t.string(),
            "syncId": t.integer(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelAddedOut"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataIn"] = t.struct(
        {
            "activityFeedMessageCreateTime": t.string().optional(),
            "sharedUserInfo": t.proxy(renames["UserInfoIn"]).optional(),
            "chatItem": t.proxy(renames["AppsDynamiteSharedChatItemIn"]),
            "activityFeedMessageId": t.proxy(renames["MessageIdIn"]).optional(),
            "userInfo": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataIn"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataOut"] = t.struct(
        {
            "activityFeedMessageCreateTime": t.string().optional(),
            "sharedUserInfo": t.proxy(renames["UserInfoOut"]).optional(),
            "chatItem": t.proxy(renames["AppsDynamiteSharedChatItemOut"]),
            "activityFeedMessageId": t.proxy(renames["MessageIdOut"]).optional(),
            "userInfo": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataOut"])
    types["FuseboxItemIn"] = t.struct(
        {
            "references": t.proxy(renames["ReferencesIn"]).optional(),
            "matchInfo": t.proxy(renames["MatchInfoIn"]),
            "snippet": t.string().optional(),
            "labels": t.proxy(renames["LabelsIn"]),
            "version": t.string().optional(),
            "creationTimeMicroseconds": t.string().optional(),
            "parts": t.proxy(renames["ItemPartsIn"]).optional(),
            "lastModificationTimeUs": t.string().optional(),
            "history": t.proxy(renames["HistoryIn"]),
            "readTs": t.string().optional(),
            "itemKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "lockerReferences": t.proxy(renames["ReferencesIn"]).optional(),
            "threadLocator": t.string().optional(),
            "triggers": t.proxy(renames["TriggersIn"]),
            "attributes": t.proxy(renames["AttributesIn"]),
        }
    ).named(renames["FuseboxItemIn"])
    types["FuseboxItemOut"] = t.struct(
        {
            "references": t.proxy(renames["ReferencesOut"]).optional(),
            "matchInfo": t.proxy(renames["MatchInfoOut"]),
            "snippet": t.string().optional(),
            "labels": t.proxy(renames["LabelsOut"]),
            "version": t.string().optional(),
            "creationTimeMicroseconds": t.string().optional(),
            "parts": t.proxy(renames["ItemPartsOut"]).optional(),
            "lastModificationTimeUs": t.string().optional(),
            "history": t.proxy(renames["HistoryOut"]),
            "readTs": t.string().optional(),
            "itemKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "lockerReferences": t.proxy(renames["ReferencesOut"]).optional(),
            "threadLocator": t.string().optional(),
            "triggers": t.proxy(renames["TriggersOut"]),
            "attributes": t.proxy(renames["AttributesOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FuseboxItemOut"])
    types["CommunalLabelTagIn"] = t.struct(
        {"creatorUserId": t.string().optional(), "labelId": t.string().optional()}
    ).named(renames["CommunalLabelTagIn"])
    types["CommunalLabelTagOut"] = t.struct(
        {
            "creatorUserId": t.string().optional(),
            "labelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommunalLabelTagOut"])
    types["AppsDynamiteStorageColumnsColumnIn"] = t.struct(
        {
            "verticalAlignment": t.string().optional(),
            "horizontalSizeStyle": t.string().optional(),
            "horizontalAlignment": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageColumnsColumnWidgetsIn"])
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnIn"])
    types["AppsDynamiteStorageColumnsColumnOut"] = t.struct(
        {
            "verticalAlignment": t.string().optional(),
            "horizontalSizeStyle": t.string().optional(),
            "horizontalAlignment": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageColumnsColumnWidgetsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnOut"])
    types["ChatClientActionMarkupIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ChatClientActionMarkupIn"]
    )
    types["ChatClientActionMarkupOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatClientActionMarkupOut"])
    types["EnumPropertyOptionsIn"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "operatorOptions": t.proxy(renames["EnumOperatorOptionsIn"]).optional(),
            "possibleValues": t.array(t.proxy(renames["EnumValuePairIn"])).optional(),
        }
    ).named(renames["EnumPropertyOptionsIn"])
    types["EnumPropertyOptionsOut"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "operatorOptions": t.proxy(renames["EnumOperatorOptionsOut"]).optional(),
            "possibleValues": t.array(t.proxy(renames["EnumValuePairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumPropertyOptionsOut"])
    types["ErrorInfoIn"] = t.struct(
        {"errorMessages": t.array(t.proxy(renames["ErrorMessageIn"]))}
    ).named(renames["ErrorInfoIn"])
    types["ErrorInfoOut"] = t.struct(
        {
            "errorMessages": t.array(t.proxy(renames["ErrorMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorInfoOut"])
    types["RecordingSessionInfoIn"] = t.struct(
        {
            "ownerEmail": t.string().optional(),
            "recordingSessionId": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
        }
    ).named(renames["RecordingSessionInfoIn"])
    types["RecordingSessionInfoOut"] = t.struct(
        {
            "ownerEmail": t.string().optional(),
            "recordingSessionId": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordingSessionInfoOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"])
    types["RosterIn"] = t.struct(
        {
            "name": t.string(),
            "avatarUrl": t.string(),
            "id": t.proxy(renames["RosterIdIn"]),
            "rosterGaiaKey": t.string().optional(),
            "rosterState": t.string().optional(),
            "isMembershipVisibleToCaller": t.boolean().optional(),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsIn"]
            ).optional(),
            "membershipCount": t.integer(),
        }
    ).named(renames["RosterIn"])
    types["RosterOut"] = t.struct(
        {
            "name": t.string(),
            "avatarUrl": t.string(),
            "id": t.proxy(renames["RosterIdOut"]),
            "rosterGaiaKey": t.string().optional(),
            "rosterState": t.string().optional(),
            "isMembershipVisibleToCaller": t.boolean().optional(),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsOut"]
            ).optional(),
            "membershipCount": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RosterOut"])
    types["SpaceIdIn"] = t.struct({"spaceId": t.string().optional()}).named(
        renames["SpaceIdIn"]
    )
    types["SpaceIdOut"] = t.struct(
        {
            "spaceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceIdOut"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn"] = t.struct(
        {
            "updaterToShow": t.proxy(renames["UserIdIn"]).optional(),
            "updaterCountDisplayType": t.string().optional(),
            "updaterCountToShow": t.integer().optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut"] = t.struct(
        {
            "updaterToShow": t.proxy(renames["UserIdOut"]).optional(),
            "updaterCountDisplayType": t.string().optional(),
            "updaterCountToShow": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut"])
    types["AppsDynamiteStorageSelectionInputSelectionItemIn"] = t.struct(
        {
            "text": t.string().optional(),
            "value": t.string().optional(),
            "selected": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputSelectionItemIn"])
    types["AppsDynamiteStorageSelectionInputSelectionItemOut"] = t.struct(
        {
            "text": t.string().optional(),
            "value": t.string().optional(),
            "selected": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputSelectionItemOut"])
    types["SourceScoringConfigIn"] = t.struct(
        {"sourceImportance": t.string().optional()}
    ).named(renames["SourceScoringConfigIn"])
    types["SourceScoringConfigOut"] = t.struct(
        {
            "sourceImportance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceScoringConfigOut"])
    types["DataSourceIn"] = t.struct(
        {
            "disableModifications": t.boolean().optional(),
            "name": t.string().optional(),
            "shortName": t.string().optional(),
            "displayName": t.string(),
            "operationIds": t.array(t.string()).optional(),
            "disableServing": t.boolean().optional(),
            "indexingServiceAccounts": t.array(t.string()).optional(),
            "returnThumbnailUrls": t.boolean().optional(),
            "itemsVisibility": t.array(
                t.proxy(renames["GSuitePrincipalIn"])
            ).optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "disableModifications": t.boolean().optional(),
            "name": t.string().optional(),
            "shortName": t.string().optional(),
            "displayName": t.string(),
            "operationIds": t.array(t.string()).optional(),
            "disableServing": t.boolean().optional(),
            "indexingServiceAccounts": t.array(t.string()).optional(),
            "returnThumbnailUrls": t.boolean().optional(),
            "itemsVisibility": t.array(
                t.proxy(renames["GSuitePrincipalOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["TextButtonIn"] = t.struct(
        {
            "disabled": t.boolean(),
            "altText": t.string().optional(),
            "text": t.string().optional(),
            "style": t.string(),
            "onClick": t.proxy(renames["OnClickIn"]),
            "backgroundColor": t.string().optional(),
        }
    ).named(renames["TextButtonIn"])
    types["TextButtonOut"] = t.struct(
        {
            "disabled": t.boolean(),
            "altText": t.string().optional(),
            "text": t.string().optional(),
            "style": t.string(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "backgroundColor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextButtonOut"])
    types["ListDataSourceResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sources": t.array(t.proxy(renames["DataSourceIn"])),
        }
    ).named(renames["ListDataSourceResponseIn"])
    types["ListDataSourceResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sources": t.array(t.proxy(renames["DataSourceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataSourceResponseOut"])
    types["QuerySuggestionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["QuerySuggestionIn"]
    )
    types["QuerySuggestionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QuerySuggestionOut"])
    types["ChatConserverMessageContentIn"] = t.struct(
        {
            "attachment": t.array(
                t.proxy(renames["SocialCommonAttachmentAttachmentIn"])
            ).optional(),
            "segment": t.array(t.proxy(renames["SegmentIn"])).optional(),
        }
    ).named(renames["ChatConserverMessageContentIn"])
    types["ChatConserverMessageContentOut"] = t.struct(
        {
            "attachment": t.array(
                t.proxy(renames["SocialCommonAttachmentAttachmentOut"])
            ).optional(),
            "segment": t.array(t.proxy(renames["SegmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatConserverMessageContentOut"])
    types["AppsDynamiteSharedAppProfileIn"] = t.struct(
        {
            "name": t.string().optional(),
            "avatarEmoji": t.string().optional(),
            "avatarUrl": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedAppProfileIn"])
    types["AppsDynamiteSharedAppProfileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "avatarEmoji": t.string().optional(),
            "avatarUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAppProfileOut"])
    types["AppsDynamiteSharedAvatarInfoIn"] = t.struct(
        {"emoji": t.proxy(renames["AppsDynamiteSharedEmojiIn"])}
    ).named(renames["AppsDynamiteSharedAvatarInfoIn"])
    types["AppsDynamiteSharedAvatarInfoOut"] = t.struct(
        {
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAvatarInfoOut"])
    types["AppsDynamiteSharedCustomEmojiIn"] = t.struct(
        {
            "shortcode": t.string().optional(),
            "uuid": t.string().optional(),
            "contentType": t.string().optional(),
            "state": t.string().optional(),
            "blobId": t.string().optional(),
            "deleteTimeMicros": t.string().optional(),
            "updateTimeMicros": t.string(),
            "ownerCustomerId": t.proxy(renames["CustomerIdIn"]).optional(),
            "readToken": t.string().optional(),
            "creatorUserId": t.proxy(renames["UserIdIn"]).optional(),
            "createTimeMicros": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedCustomEmojiIn"])
    types["AppsDynamiteSharedCustomEmojiOut"] = t.struct(
        {
            "shortcode": t.string().optional(),
            "uuid": t.string().optional(),
            "contentType": t.string().optional(),
            "state": t.string().optional(),
            "blobId": t.string().optional(),
            "deleteTimeMicros": t.string().optional(),
            "updateTimeMicros": t.string(),
            "ownerCustomerId": t.proxy(renames["CustomerIdOut"]).optional(),
            "readToken": t.string().optional(),
            "creatorUserId": t.proxy(renames["UserIdOut"]).optional(),
            "createTimeMicros": t.string().optional(),
            "ephemeralUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCustomEmojiOut"])
    types["AppsDynamiteStorageTextInputIn"] = t.struct(
        {
            "label": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["AppsDynamiteStorageSuggestionsIn"]
            ).optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "hintText": t.string().optional(),
            "autoCompleteAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageTextInputIn"])
    types["AppsDynamiteStorageTextInputOut"] = t.struct(
        {
            "label": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["AppsDynamiteStorageSuggestionsOut"]
            ).optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "hintText": t.string().optional(),
            "autoCompleteAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageTextInputOut"])
    types["MessageIdIn"] = t.struct(
        {
            "parentId": t.proxy(renames["MessageParentIdIn"]).optional(),
            "messageId": t.string().optional(),
        }
    ).named(renames["MessageIdIn"])
    types["MessageIdOut"] = t.struct(
        {
            "parentId": t.proxy(renames["MessageParentIdOut"]).optional(),
            "messageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageIdOut"])
    types["AppsDynamiteStorageOpenLinkAppUriIntentIn"] = t.struct(
        {
            "intentAction": t.string().optional(),
            "extraData": t.array(
                t.proxy(renames["AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn"])
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIntentIn"])
    types["AppsDynamiteStorageOpenLinkAppUriIntentOut"] = t.struct(
        {
            "intentAction": t.string().optional(),
            "extraData": t.array(
                t.proxy(renames["AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIntentOut"])
    types["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"] = t.struct(
        {"oldAssignee": t.proxy(renames["UserIdIn"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"] = t.struct(
        {
            "oldAssignee": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"])
    types["EventProtoIn"] = t.struct(
        {"eventId": t.string().optional(), "memberType": t.integer().optional()}
    ).named(renames["EventProtoIn"])
    types["EventProtoOut"] = t.struct(
        {
            "eventId": t.string().optional(),
            "memberType": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventProtoOut"])
    types["AffectedMembershipIn"] = t.struct(
        {
            "priorMembershipRole": t.string(),
            "targetMembershipRole": t.string(),
            "affectedMember": t.proxy(renames["MemberIdIn"]),
            "priorMembershipState": t.string(),
        }
    ).named(renames["AffectedMembershipIn"])
    types["AffectedMembershipOut"] = t.struct(
        {
            "priorMembershipRole": t.string(),
            "targetMembershipRole": t.string(),
            "affectedMember": t.proxy(renames["MemberIdOut"]),
            "priorMembershipState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AffectedMembershipOut"])
    types["HtmlPropertyOptionsIn"] = t.struct(
        {
            "retrievalImportance": t.proxy(renames["RetrievalImportanceIn"]).optional(),
            "operatorOptions": t.proxy(renames["HtmlOperatorOptionsIn"]).optional(),
        }
    ).named(renames["HtmlPropertyOptionsIn"])
    types["HtmlPropertyOptionsOut"] = t.struct(
        {
            "retrievalImportance": t.proxy(
                renames["RetrievalImportanceOut"]
            ).optional(),
            "operatorOptions": t.proxy(renames["HtmlOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlPropertyOptionsOut"])
    types["ObjectDisplayOptionsIn"] = t.struct(
        {
            "objectDisplayLabel": t.string().optional(),
            "metalines": t.array(t.proxy(renames["MetalineIn"])).optional(),
        }
    ).named(renames["ObjectDisplayOptionsIn"])
    types["ObjectDisplayOptionsOut"] = t.struct(
        {
            "objectDisplayLabel": t.string().optional(),
            "metalines": t.array(t.proxy(renames["MetalineOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectDisplayOptionsOut"])
    types["ImageCropStyleIn"] = t.struct(
        {"type": t.string().optional(), "aspectRatio": t.number().optional()}
    ).named(renames["ImageCropStyleIn"])
    types["ImageCropStyleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageCropStyleOut"])
    types["SectionIn"] = t.struct(
        {
            "numUncollapsableWidgets": t.integer().optional(),
            "description": t.string().optional(),
            "widgets": t.array(t.proxy(renames["WidgetMarkupIn"])).optional(),
            "collapsable": t.boolean().optional(),
        }
    ).named(renames["SectionIn"])
    types["SectionOut"] = t.struct(
        {
            "numUncollapsableWidgets": t.integer().optional(),
            "description": t.string().optional(),
            "widgets": t.array(t.proxy(renames["WidgetMarkupOut"])).optional(),
            "collapsable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionOut"])
    types["PrincipalIn"] = t.struct(
        {
            "gsuitePrincipal": t.proxy(renames["GSuitePrincipalIn"]).optional(),
            "userResourceName": t.string().optional(),
            "groupResourceName": t.string().optional(),
        }
    ).named(renames["PrincipalIn"])
    types["PrincipalOut"] = t.struct(
        {
            "gsuitePrincipal": t.proxy(renames["GSuitePrincipalOut"]).optional(),
            "userResourceName": t.string().optional(),
            "groupResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrincipalOut"])
    types["ReadReceiptsSettingsUpdatedMetadataIn"] = t.struct(
        {"readReceiptsEnabled": t.boolean().optional()}
    ).named(renames["ReadReceiptsSettingsUpdatedMetadataIn"])
    types["ReadReceiptsSettingsUpdatedMetadataOut"] = t.struct(
        {
            "readReceiptsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadReceiptsSettingsUpdatedMetadataOut"])
    types["SessionContextIn"] = t.struct(
        {
            "delegateUserId": t.string().optional(),
            "oauthProjectId": t.string().optional(),
            "dusi": t.string().optional(),
            "oauthLoginId": t.integer().optional(),
            "authTime": t.string().optional(),
            "imapSessionContext": t.proxy(renames["ImapSessionContextIn"]).optional(),
        }
    ).named(renames["SessionContextIn"])
    types["SessionContextOut"] = t.struct(
        {
            "delegateUserId": t.string().optional(),
            "oauthProjectId": t.string().optional(),
            "dusi": t.string().optional(),
            "oauthLoginId": t.integer().optional(),
            "authTime": t.string().optional(),
            "imapSessionContext": t.proxy(renames["ImapSessionContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionContextOut"])
    types["AclFixRequestIn"] = t.struct(
        {
            "recipientEmails": t.array(t.string()).optional(),
            "shouldFix": t.boolean().optional(),
            "role": t.string(),
        }
    ).named(renames["AclFixRequestIn"])
    types["AclFixRequestOut"] = t.struct(
        {
            "recipientEmails": t.array(t.string()).optional(),
            "shouldFix": t.boolean().optional(),
            "role": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclFixRequestOut"])
    types["AppsDynamiteStorageActionActionParameterIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["AppsDynamiteStorageActionActionParameterIn"])
    types["AppsDynamiteStorageActionActionParameterOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageActionActionParameterOut"])
    types["NamedPropertyIn"] = t.struct(
        {
            "doubleValues": t.proxy(renames["DoubleValuesIn"]),
            "name": t.string().optional(),
            "integerValues": t.proxy(renames["IntegerValuesIn"]),
            "htmlValues": t.proxy(renames["HtmlValuesIn"]),
            "dateValues": t.proxy(renames["DateValuesIn"]),
            "textValues": t.proxy(renames["TextValuesIn"]),
            "objectValues": t.proxy(renames["ObjectValuesIn"]),
            "enumValues": t.proxy(renames["EnumValuesIn"]),
            "booleanValue": t.boolean(),
            "timestampValues": t.proxy(renames["TimestampValuesIn"]),
        }
    ).named(renames["NamedPropertyIn"])
    types["NamedPropertyOut"] = t.struct(
        {
            "doubleValues": t.proxy(renames["DoubleValuesOut"]),
            "name": t.string().optional(),
            "integerValues": t.proxy(renames["IntegerValuesOut"]),
            "htmlValues": t.proxy(renames["HtmlValuesOut"]),
            "dateValues": t.proxy(renames["DateValuesOut"]),
            "textValues": t.proxy(renames["TextValuesOut"]),
            "objectValues": t.proxy(renames["ObjectValuesOut"]),
            "enumValues": t.proxy(renames["EnumValuesOut"]),
            "booleanValue": t.boolean(),
            "timestampValues": t.proxy(renames["TimestampValuesOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedPropertyOut"])
    types["UniversalPhoneAccessIn"] = t.struct(
        {"pin": t.string().optional(), "pstnInfoUrl": t.string().optional()}
    ).named(renames["UniversalPhoneAccessIn"])
    types["UniversalPhoneAccessOut"] = t.struct(
        {
            "pin": t.string().optional(),
            "pstnInfoUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UniversalPhoneAccessOut"])
    types["AppsDynamiteStorageImageIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]),
            "altText": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageImageIn"])
    types["AppsDynamiteStorageImageOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageOut"])
    types["RequestFileScopeIn"] = t.struct({"itemId": t.string()}).named(
        renames["RequestFileScopeIn"]
    )
    types["RequestFileScopeOut"] = t.struct(
        {"itemId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestFileScopeOut"])
    types["ThreadUpdateIn"] = t.struct(
        {
            "labelAdded": t.proxy(renames["LabelAddedIn"]),
            "originalThreadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "messageDeleted": t.proxy(renames["MessageDeletedIn"]),
            "threadKeySet": t.proxy(renames["ThreadKeySetIn"]),
            "labelRemoved": t.proxy(renames["LabelRemovedIn"]),
            "preState": t.array(t.proxy(renames["PreStateIn"])).optional(),
            "lastHistoryRecordId": t.string().optional(),
            "attributeRemoved": t.proxy(renames["AttributeRemovedIn"]),
            "topicStateUpdate": t.proxy(renames["TopicStateUpdateIn"]),
            "threadLocator": t.string().optional(),
            "messageAdded": t.proxy(renames["MessageAddedIn"]),
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "attributeSet": t.proxy(renames["AttributeSetIn"]),
        }
    ).named(renames["ThreadUpdateIn"])
    types["ThreadUpdateOut"] = t.struct(
        {
            "labelAdded": t.proxy(renames["LabelAddedOut"]),
            "originalThreadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "messageDeleted": t.proxy(renames["MessageDeletedOut"]),
            "threadKeySet": t.proxy(renames["ThreadKeySetOut"]),
            "labelRemoved": t.proxy(renames["LabelRemovedOut"]),
            "preState": t.array(t.proxy(renames["PreStateOut"])).optional(),
            "lastHistoryRecordId": t.string().optional(),
            "attributeRemoved": t.proxy(renames["AttributeRemovedOut"]),
            "topicStateUpdate": t.proxy(renames["TopicStateUpdateOut"]),
            "threadLocator": t.string().optional(),
            "messageAdded": t.proxy(renames["MessageAddedOut"]),
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "attributeSet": t.proxy(renames["AttributeSetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThreadUpdateOut"])
    types["SourceCrowdingConfigIn"] = t.struct(
        {"numResults": t.integer().optional(), "numSuggestions": t.integer().optional()}
    ).named(renames["SourceCrowdingConfigIn"])
    types["SourceCrowdingConfigOut"] = t.struct(
        {
            "numResults": t.integer().optional(),
            "numSuggestions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceCrowdingConfigOut"])
    types["SettingsIn"] = t.struct(
        {
            "chatLock": t.boolean().optional(),
            "cohostArtifactSharingEnabled": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "accessType": t.string().optional(),
            "accessLock": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "defaultAsViewer": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "chatLock": t.boolean().optional(),
            "cohostArtifactSharingEnabled": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "accessType": t.string().optional(),
            "accessLock": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "defaultAsViewer": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["ImageKeyValueIn"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickIn"]),
            "icon": t.string(),
            "text": t.string(),
            "iconUrl": t.string(),
        }
    ).named(renames["ImageKeyValueIn"])
    types["ImageKeyValueOut"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickOut"]),
            "icon": t.string(),
            "text": t.string(),
            "iconUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageKeyValueOut"])
    types["RoomUpdatedMetadataIn"] = t.struct(
        {
            "initiatorType": t.string().optional(),
            "renameMetadata": t.proxy(renames["RoomRenameMetadataIn"]),
            "initiator": t.proxy(renames["UserIn"]).optional(),
            "groupDetailsMetadata": t.proxy(renames["GroupDetailsUpdatedMetadataIn"]),
            "groupLinkSharingEnabled": t.boolean(),
            "name": t.string().optional(),
            "visibility": t.proxy(
                renames["AppsDynamiteSharedGroupVisibilityIn"]
            ).optional(),
        }
    ).named(renames["RoomUpdatedMetadataIn"])
    types["RoomUpdatedMetadataOut"] = t.struct(
        {
            "initiatorType": t.string().optional(),
            "renameMetadata": t.proxy(renames["RoomRenameMetadataOut"]),
            "initiator": t.proxy(renames["UserOut"]).optional(),
            "groupDetailsMetadata": t.proxy(renames["GroupDetailsUpdatedMetadataOut"]),
            "groupLinkSharingEnabled": t.boolean(),
            "name": t.string().optional(),
            "visibility": t.proxy(
                renames["AppsDynamiteSharedGroupVisibilityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoomUpdatedMetadataOut"])
    types["UpdateSubjectIn"] = t.struct({"subject": t.string()}).named(
        renames["UpdateSubjectIn"]
    )
    types["UpdateSubjectOut"] = t.struct(
        {"subject": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateSubjectOut"])
    types["TimestampValuesIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["TimestampValuesIn"]
    )
    types["TimestampValuesOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampValuesOut"])
    types["InviteAcceptedEventIn"] = t.struct(
        {"participantId": t.array(t.proxy(renames["StoredParticipantIdIn"]))}
    ).named(renames["InviteAcceptedEventIn"])
    types["InviteAcceptedEventOut"] = t.struct(
        {
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InviteAcceptedEventOut"])
    types["AppsDynamiteSharedPhoneNumberIn"] = t.struct(
        {"value": t.string().optional(), "type": t.string().optional()}
    ).named(renames["AppsDynamiteSharedPhoneNumberIn"])
    types["AppsDynamiteSharedPhoneNumberOut"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedPhoneNumberOut"])
    types["IntegrationConfigUpdatedMetadataIn"] = t.struct(
        {
            "mutations": t.array(
                t.proxy(renames["IntegrationConfigMutationIn"])
            ).optional(),
            "initiatorId": t.proxy(renames["UserIdIn"]).optional(),
        }
    ).named(renames["IntegrationConfigUpdatedMetadataIn"])
    types["IntegrationConfigUpdatedMetadataOut"] = t.struct(
        {
            "mutations": t.array(
                t.proxy(renames["IntegrationConfigMutationOut"])
            ).optional(),
            "initiatorId": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegrationConfigUpdatedMetadataOut"])
    types["SquareProtoIn"] = t.struct(
        {"squareId": t.string().optional(), "memberType": t.integer().optional()}
    ).named(renames["SquareProtoIn"])
    types["SquareProtoOut"] = t.struct(
        {
            "squareId": t.string().optional(),
            "memberType": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SquareProtoOut"])
    types["BroadcastSessionInfoIn"] = t.struct(
        {
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
            "broadcastSessionId": t.string().optional(),
            "ingestionId": t.string().optional(),
        }
    ).named(renames["BroadcastSessionInfoIn"])
    types["BroadcastSessionInfoOut"] = t.struct(
        {
            "broadcastStats": t.proxy(renames["BroadcastStatsOut"]).optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "broadcastSessionId": t.string().optional(),
            "ingestionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BroadcastSessionInfoOut"])
    types["SuggestRequestIn"] = t.struct(
        {
            "query": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
        }
    ).named(renames["SuggestRequestIn"])
    types["SuggestRequestOut"] = t.struct(
        {
            "query": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestRequestOut"])
    types["RoomRenameMetadataIn"] = t.struct(
        {"prevName": t.string().optional(), "newName": t.string()}
    ).named(renames["RoomRenameMetadataIn"])
    types["RoomRenameMetadataOut"] = t.struct(
        {
            "prevName": t.string().optional(),
            "newName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoomRenameMetadataOut"])
    types["ActionParameterIn"] = t.struct(
        {"value": t.string(), "key": t.string()}
    ).named(renames["ActionParameterIn"])
    types["ActionParameterOut"] = t.struct(
        {
            "value": t.string(),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionParameterOut"])
    types["GoogleChatV1WidgetMarkupOnClickIn"] = t.struct(
        {
            "action": t.proxy(
                renames["GoogleChatV1WidgetMarkupFormActionIn"]
            ).optional(),
            "openLink": t.proxy(
                renames["GoogleChatV1WidgetMarkupOpenLinkIn"]
            ).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupOnClickIn"])
    types["GoogleChatV1WidgetMarkupOnClickOut"] = t.struct(
        {
            "action": t.proxy(
                renames["GoogleChatV1WidgetMarkupFormActionOut"]
            ).optional(),
            "openLink": t.proxy(
                renames["GoogleChatV1WidgetMarkupOpenLinkOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupOnClickOut"])
    types["RequiredMessageFeaturesMetadataIn"] = t.struct(
        {"requiredFeatures": t.array(t.string())}
    ).named(renames["RequiredMessageFeaturesMetadataIn"])
    types["RequiredMessageFeaturesMetadataOut"] = t.struct(
        {
            "requiredFeatures": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequiredMessageFeaturesMetadataOut"])
    types["DataSourceRestrictionIn"] = t.struct(
        {
            "filterOptions": t.array(t.proxy(renames["FilterOptionsIn"])).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["DataSourceRestrictionIn"])
    types["DataSourceRestrictionOut"] = t.struct(
        {
            "filterOptions": t.array(t.proxy(renames["FilterOptionsOut"])).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRestrictionOut"])
    types["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"])
    types[
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"]
    )
    types["LegacyUploadMetadataIn"] = t.struct(
        {
            "uploadMetadata": t.proxy(renames["UploadMetadataIn"]).optional(),
            "legacyUniqueId": t.string().optional(),
        }
    ).named(renames["LegacyUploadMetadataIn"])
    types["LegacyUploadMetadataOut"] = t.struct(
        {
            "uploadMetadata": t.proxy(renames["UploadMetadataOut"]).optional(),
            "legacyUniqueId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LegacyUploadMetadataOut"])
    types["AppsDynamiteStorageWidgetIn"] = t.struct(
        {
            "image": t.proxy(renames["AppsDynamiteStorageImageIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "grid": t.proxy(renames["AppsDynamiteStorageGridIn"]).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputIn"]).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextIn"]
            ).optional(),
            "divider": t.proxy(renames["AppsDynamiteStorageDividerIn"]).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerIn"]
            ).optional(),
            "columns": t.proxy(renames["AppsDynamiteStorageColumnsIn"]).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListIn"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphIn"]
            ).optional(),
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageWidgetIn"])
    types["AppsDynamiteStorageWidgetOut"] = t.struct(
        {
            "image": t.proxy(renames["AppsDynamiteStorageImageOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "grid": t.proxy(renames["AppsDynamiteStorageGridOut"]).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputOut"]).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextOut"]
            ).optional(),
            "divider": t.proxy(renames["AppsDynamiteStorageDividerOut"]).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerOut"]
            ).optional(),
            "columns": t.proxy(renames["AppsDynamiteStorageColumnsOut"]).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListOut"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphOut"]
            ).optional(),
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageWidgetOut"])
    types["PersonIn"] = t.struct(
        {
            "name": t.string().optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressIn"])).optional(),
            "photos": t.array(t.proxy(renames["PhotoIn"])).optional(),
            "personNames": t.array(t.proxy(renames["NameIn"])).optional(),
            "obfuscatedId": t.string().optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "name": t.string().optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressOut"])).optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "personNames": t.array(t.proxy(renames["NameOut"])).optional(),
            "obfuscatedId": t.string().optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["AppsDynamiteSharedBackendUploadMetadataIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "isClientSideTranscodedVideo": t.boolean().optional(),
            "uploadTimestampUsec": t.string().optional(),
            "videoThumbnailBlobId": t.string().optional(),
            "groupId": t.proxy(renames["GroupIdIn"]).optional(),
            "contentSize": t.string().optional(),
            "quoteReplyMessageId": t.proxy(renames["MessageIdIn"]).optional(),
            "dlpScanOutcome": t.string().optional(),
            "uploadIp": t.string().optional(),
            "contentName": t.string().optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryIn"]).optional(),
            "videoId": t.string().optional(),
            "virusScanResult": t.string().optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionIn"]
            ).optional(),
            "sha256": t.string().optional(),
            "blobPath": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedBackendUploadMetadataIn"])
    types["AppsDynamiteSharedBackendUploadMetadataOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "isClientSideTranscodedVideo": t.boolean().optional(),
            "uploadTimestampUsec": t.string().optional(),
            "videoThumbnailBlobId": t.string().optional(),
            "groupId": t.proxy(renames["GroupIdOut"]).optional(),
            "contentSize": t.string().optional(),
            "quoteReplyMessageId": t.proxy(renames["MessageIdOut"]).optional(),
            "dlpScanOutcome": t.string().optional(),
            "uploadIp": t.string().optional(),
            "contentName": t.string().optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryOut"]).optional(),
            "videoId": t.string().optional(),
            "virusScanResult": t.string().optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionOut"]
            ).optional(),
            "sha256": t.string().optional(),
            "blobPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedBackendUploadMetadataOut"])
    types["AppsDynamiteSharedRetentionSettingsIn"] = t.struct(
        {"expiryTimestamp": t.string().optional(), "state": t.string().optional()}
    ).named(renames["AppsDynamiteSharedRetentionSettingsIn"])
    types["AppsDynamiteSharedRetentionSettingsOut"] = t.struct(
        {
            "expiryTimestamp": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedRetentionSettingsOut"])
    types["CustomerSessionStatsIn"] = t.struct(
        {
            "searchSessionsCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["CustomerSessionStatsIn"])
    types["CustomerSessionStatsOut"] = t.struct(
        {
            "searchSessionsCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerSessionStatsOut"])
    types["WonderCardDeleteIn"] = t.struct(
        {
            "msgId": t.string().optional(),
            "messageMappings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WonderCardDeleteIn"])
    types["WonderCardDeleteOut"] = t.struct(
        {
            "msgId": t.string().optional(),
            "messageMappings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WonderCardDeleteOut"])
    types["SearchRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "queryInterpretationOptions": t.proxy(
                renames["QueryInterpretationOptionsIn"]
            ).optional(),
            "pageSize": t.integer().optional(),
            "query": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "facetOptions": t.array(t.proxy(renames["FacetOptionsIn"])),
            "sortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeIn"])
            ).optional(),
            "start": t.integer().optional(),
        }
    ).named(renames["SearchRequestIn"])
    types["SearchRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "queryInterpretationOptions": t.proxy(
                renames["QueryInterpretationOptionsOut"]
            ).optional(),
            "pageSize": t.integer().optional(),
            "query": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "facetOptions": t.array(t.proxy(renames["FacetOptionsOut"])),
            "sortOptions": t.proxy(renames["SortOptionsOut"]).optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeOut"])
            ).optional(),
            "start": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchRequestOut"])
    types["InsertContentIn"] = t.struct(
        {
            "content": t.string().optional(),
            "mimeType": t.string(),
            "contentType": t.string().optional(),
        }
    ).named(renames["InsertContentIn"])
    types["InsertContentOut"] = t.struct(
        {
            "content": t.string().optional(),
            "mimeType": t.string(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertContentOut"])
    types["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn"] = t.struct(
        {"feedbackChipType": t.string().optional(), "state": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn"])
    types["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut"] = t.struct(
        {
            "feedbackChipType": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut"])
    types["GatewaySipAccessIn"] = t.struct(
        {"sipAccessCode": t.string().optional(), "uri": t.string().optional()}
    ).named(renames["GatewaySipAccessIn"])
    types["GatewaySipAccessOut"] = t.struct(
        {
            "sipAccessCode": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySipAccessOut"])
    types["PaygateInfoIn"] = t.struct(
        {
            "callEndingTime": t.string().optional(),
            "callEndingSoonWarningTime": t.string().optional(),
            "showUpgradePromos": t.boolean().optional(),
        }
    ).named(renames["PaygateInfoIn"])
    types["PaygateInfoOut"] = t.struct(
        {
            "callEndingTime": t.string().optional(),
            "callEndingSoonWarningTime": t.string().optional(),
            "showUpgradePromos": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaygateInfoOut"])
    types["AppsDynamiteV1ApiCompatV1FieldIn"] = t.struct(
        {
            "title": t.string().optional(),
            "value": t.string().optional(),
            "short": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1FieldIn"])
    types["AppsDynamiteV1ApiCompatV1FieldOut"] = t.struct(
        {
            "title": t.string().optional(),
            "value": t.string().optional(),
            "short": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1FieldOut"])
    types["AppsDynamiteSharedDlpMetricsMetadataIn"] = t.struct(
        {"dlpStatus": t.string().optional()}
    ).named(renames["AppsDynamiteSharedDlpMetricsMetadataIn"])
    types["AppsDynamiteSharedDlpMetricsMetadataOut"] = t.struct(
        {
            "dlpStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedDlpMetricsMetadataOut"])
    types["FilterUpdateIn"] = t.struct(
        {
            "filterCreated": t.proxy(renames["FilterCreatedIn"]),
            "filterId": t.string(),
            "filterDeleted": t.proxy(renames["FilterDeletedIn"]),
        }
    ).named(renames["FilterUpdateIn"])
    types["FilterUpdateOut"] = t.struct(
        {
            "filterCreated": t.proxy(renames["FilterCreatedOut"]),
            "filterId": t.string(),
            "filterDeleted": t.proxy(renames["FilterDeletedOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterUpdateOut"])
    types["IntegrationConfigMutationIn"] = t.struct(
        {
            "removePinnedItem": t.proxy(renames["PinnedItemIdIn"]).optional(),
            "addApp": t.proxy(renames["AppIdIn"]).optional(),
            "addPinnedItem": t.proxy(renames["PinnedItemIdIn"]).optional(),
            "removeApp": t.proxy(renames["AppIdIn"]).optional(),
        }
    ).named(renames["IntegrationConfigMutationIn"])
    types["IntegrationConfigMutationOut"] = t.struct(
        {
            "removePinnedItem": t.proxy(renames["PinnedItemIdOut"]).optional(),
            "addApp": t.proxy(renames["AppIdOut"]).optional(),
            "addPinnedItem": t.proxy(renames["PinnedItemIdOut"]).optional(),
            "removeApp": t.proxy(renames["AppIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegrationConfigMutationOut"])
    types["ProcessingErrorIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "fieldViolations": t.array(t.proxy(renames["FieldViolationIn"])).optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ProcessingErrorIn"])
    types["ProcessingErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "fieldViolations": t.array(
                t.proxy(renames["FieldViolationOut"])
            ).optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingErrorOut"])

    functions = {}
    functions["statsGetQuery"] = cloudsearch.get(
        "v1/stats/index",
        t.struct(
            {
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerIndexStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetSearchapplication"] = cloudsearch.get(
        "v1/stats/index",
        t.struct(
            {
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerIndexStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetUser"] = cloudsearch.get(
        "v1/stats/index",
        t.struct(
            {
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerIndexStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetSession"] = cloudsearch.get(
        "v1/stats/index",
        t.struct(
            {
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerIndexStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetIndex"] = cloudsearch.get(
        "v1/stats/index",
        t.struct(
            {
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerIndexStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsIndexDatasourcesGet"] = cloudsearch.get(
        "v1/stats/index/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "toDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDataSourceIndexStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsUserSearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/user/{name}",
        t.struct(
            {
                "fromDate.day": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "name": t.string().optional(),
                "toDate.year": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsQuerySearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/query/{name}",
        t.struct(
            {
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationQueryStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsSessionSearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/session/{name}",
        t.struct(
            {
                "toDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "name": t.string().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsSearchByViewUrl"] = cloudsearch.post(
        "v1/debug/{name}:checkAccess",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "gsuitePrincipal": t.proxy(renames["GSuitePrincipalIn"]).optional(),
                "userResourceName": t.string().optional(),
                "groupResourceName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckAccessResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsCheckAccess"] = cloudsearch.post(
        "v1/debug/{name}:checkAccess",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "gsuitePrincipal": t.proxy(renames["GSuitePrincipalIn"]).optional(),
                "userResourceName": t.string().optional(),
                "groupResourceName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckAccessResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsUnmappedidsList"] = cloudsearch.get(
        "v1/debug/{parent}/unmappedids",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUnmappedIdentitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugIdentitysourcesItemsListForunmappedidentity"] = cloudsearch.get(
        "v1/debug/{parent}/items:forunmappedidentity",
        t.struct(
            {
                "userResourceName": t.string(),
                "pageSize": t.integer().optional(),
                "groupResourceName": t.string(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListItemNamesForUnmappedIdentityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugIdentitysourcesUnmappedidsList"] = cloudsearch.get(
        "v1/debug/{parent}/unmappedids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "parent": t.string().optional(),
                "resolutionStatusCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUnmappedIdentitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesGetSchema"] = cloudsearch.delete(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesUpdateSchema"] = cloudsearch.delete(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesDeleteSchema"] = cloudsearch.delete(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsUpload"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsPush"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsDeleteQueueItems"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsIndex"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsList"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsDelete"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsUnreserve"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsPoll"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsGet"] = cloudsearch.get(
        "v1/indexing/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaUpload"] = cloudsearch.post(
        "v1/media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["MediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsUpdateCustomer"] = cloudsearch.get(
        "v1/settings/customer",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["CustomerSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsGetCustomer"] = cloudsearch.get(
        "v1/settings/customer",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["CustomerSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesPatch"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "disableModifications": t.boolean().optional(),
                "name": t.string().optional(),
                "shortName": t.string().optional(),
                "displayName": t.string(),
                "operationIds": t.array(t.string()).optional(),
                "disableServing": t.boolean().optional(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesGet"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "disableModifications": t.boolean().optional(),
                "name": t.string().optional(),
                "shortName": t.string().optional(),
                "displayName": t.string(),
                "operationIds": t.array(t.string()).optional(),
                "disableServing": t.boolean().optional(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesUpdate"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "disableModifications": t.boolean().optional(),
                "name": t.string().optional(),
                "shortName": t.string().optional(),
                "displayName": t.string(),
                "operationIds": t.array(t.string()).optional(),
                "disableServing": t.boolean().optional(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesDelete"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "disableModifications": t.boolean().optional(),
                "name": t.string().optional(),
                "shortName": t.string().optional(),
                "displayName": t.string(),
                "operationIds": t.array(t.string()).optional(),
                "disableServing": t.boolean().optional(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesList"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "disableModifications": t.boolean().optional(),
                "name": t.string().optional(),
                "shortName": t.string().optional(),
                "displayName": t.string(),
                "operationIds": t.array(t.string()).optional(),
                "disableServing": t.boolean().optional(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesCreate"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "disableModifications": t.boolean().optional(),
                "name": t.string().optional(),
                "shortName": t.string().optional(),
                "displayName": t.string(),
                "operationIds": t.array(t.string()).optional(),
                "disableServing": t.boolean().optional(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsDelete"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsUpdate"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsCreate"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsReset"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsPatch"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsGet"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsList"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1InitializeCustomer"] = cloudsearch.post(
        "v1:initializeCustomer",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySearch"] = cloudsearch.post(
        "v1/query/suggest",
        t.struct(
            {
                "query": t.string().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SuggestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySuggest"] = cloudsearch.post(
        "v1/query/suggest",
        t.struct(
            {
                "query": t.string().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SuggestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySourcesList"] = cloudsearch.get(
        "v1/query/sources",
        t.struct(
            {
                "requestOptions.debugOptions.enableDebugging": t.boolean().optional(),
                "requestOptions.languageCode": t.string().optional(),
                "requestOptions.timeZone": t.string().optional(),
                "requestOptions.searchApplicationId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListQuerySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudsearch.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsLroList"] = cloudsearch.get(
        "v1/{name}/lro",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudsearch",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
