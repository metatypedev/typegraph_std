from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudsearch() -> Import:
    cloudsearch = HTTPRuntime("https://cloudsearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudsearch_1_ErrorResponse",
        "MessageAddedIn": "_cloudsearch_2_MessageAddedIn",
        "MessageAddedOut": "_cloudsearch_3_MessageAddedOut",
        "GsuiteIntegrationMetadataIn": "_cloudsearch_4_GsuiteIntegrationMetadataIn",
        "GsuiteIntegrationMetadataOut": "_cloudsearch_5_GsuiteIntegrationMetadataOut",
        "AppsDynamiteStorageDateTimePickerIn": "_cloudsearch_6_AppsDynamiteStorageDateTimePickerIn",
        "AppsDynamiteStorageDateTimePickerOut": "_cloudsearch_7_AppsDynamiteStorageDateTimePickerOut",
        "CardHeaderIn": "_cloudsearch_8_CardHeaderIn",
        "CardHeaderOut": "_cloudsearch_9_CardHeaderOut",
        "AppsDynamiteV1ApiCompatV1ActionConfirmIn": "_cloudsearch_10_AppsDynamiteV1ApiCompatV1ActionConfirmIn",
        "AppsDynamiteV1ApiCompatV1ActionConfirmOut": "_cloudsearch_11_AppsDynamiteV1ApiCompatV1ActionConfirmOut",
        "CustomerSearchApplicationStatsIn": "_cloudsearch_12_CustomerSearchApplicationStatsIn",
        "CustomerSearchApplicationStatsOut": "_cloudsearch_13_CustomerSearchApplicationStatsOut",
        "JobsettedServerSpecIn": "_cloudsearch_14_JobsettedServerSpecIn",
        "JobsettedServerSpecOut": "_cloudsearch_15_JobsettedServerSpecOut",
        "AppsDynamiteSharedAssistantSuggestionIn": "_cloudsearch_16_AppsDynamiteSharedAssistantSuggestionIn",
        "AppsDynamiteSharedAssistantSuggestionOut": "_cloudsearch_17_AppsDynamiteSharedAssistantSuggestionOut",
        "SearchApplicationUserStatsIn": "_cloudsearch_18_SearchApplicationUserStatsIn",
        "SearchApplicationUserStatsOut": "_cloudsearch_19_SearchApplicationUserStatsOut",
        "DataSourceIndexStatsIn": "_cloudsearch_20_DataSourceIndexStatsIn",
        "DataSourceIndexStatsOut": "_cloudsearch_21_DataSourceIndexStatsOut",
        "WidgetMarkupIn": "_cloudsearch_22_WidgetMarkupIn",
        "WidgetMarkupOut": "_cloudsearch_23_WidgetMarkupOut",
        "AppsDynamiteSharedSpaceInfoIn": "_cloudsearch_24_AppsDynamiteSharedSpaceInfoIn",
        "AppsDynamiteSharedSpaceInfoOut": "_cloudsearch_25_AppsDynamiteSharedSpaceInfoOut",
        "RecipientIn": "_cloudsearch_26_RecipientIn",
        "RecipientOut": "_cloudsearch_27_RecipientOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn": "_cloudsearch_28_AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut": "_cloudsearch_29_AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut",
        "LabelDeletedIn": "_cloudsearch_30_LabelDeletedIn",
        "LabelDeletedOut": "_cloudsearch_31_LabelDeletedOut",
        "GoogleChatV1ContextualAddOnMarkupCardCardActionIn": "_cloudsearch_32_GoogleChatV1ContextualAddOnMarkupCardCardActionIn",
        "GoogleChatV1ContextualAddOnMarkupCardCardActionOut": "_cloudsearch_33_GoogleChatV1ContextualAddOnMarkupCardCardActionOut",
        "RequestOptionsIn": "_cloudsearch_34_RequestOptionsIn",
        "RequestOptionsOut": "_cloudsearch_35_RequestOptionsOut",
        "RosterIn": "_cloudsearch_36_RosterIn",
        "RosterOut": "_cloudsearch_37_RosterOut",
        "UserIdIn": "_cloudsearch_38_UserIdIn",
        "UserIdOut": "_cloudsearch_39_UserIdOut",
        "OtrChatMessageEventIn": "_cloudsearch_40_OtrChatMessageEventIn",
        "OtrChatMessageEventOut": "_cloudsearch_41_OtrChatMessageEventOut",
        "TypeInfoIn": "_cloudsearch_42_TypeInfoIn",
        "TypeInfoOut": "_cloudsearch_43_TypeInfoOut",
        "SimpleSecretLabelProtoIn": "_cloudsearch_44_SimpleSecretLabelProtoIn",
        "SimpleSecretLabelProtoOut": "_cloudsearch_45_SimpleSecretLabelProtoOut",
        "NameIn": "_cloudsearch_46_NameIn",
        "NameOut": "_cloudsearch_47_NameOut",
        "AppsDynamiteStorageBorderStyleIn": "_cloudsearch_48_AppsDynamiteStorageBorderStyleIn",
        "AppsDynamiteStorageBorderStyleOut": "_cloudsearch_49_AppsDynamiteStorageBorderStyleOut",
        "AppsDynamiteStorageCardSectionIn": "_cloudsearch_50_AppsDynamiteStorageCardSectionIn",
        "AppsDynamiteStorageCardSectionOut": "_cloudsearch_51_AppsDynamiteStorageCardSectionOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn": "_cloudsearch_52_AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut": "_cloudsearch_53_AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut",
        "WrappedResourceKeyIn": "_cloudsearch_54_WrappedResourceKeyIn",
        "WrappedResourceKeyOut": "_cloudsearch_55_WrappedResourceKeyOut",
        "ScoringConfigIn": "_cloudsearch_56_ScoringConfigIn",
        "ScoringConfigOut": "_cloudsearch_57_ScoringConfigOut",
        "CustomerIdIn": "_cloudsearch_58_CustomerIdIn",
        "CustomerIdOut": "_cloudsearch_59_CustomerIdOut",
        "GoogleChatV1WidgetMarkupButtonIn": "_cloudsearch_60_GoogleChatV1WidgetMarkupButtonIn",
        "GoogleChatV1WidgetMarkupButtonOut": "_cloudsearch_61_GoogleChatV1WidgetMarkupButtonOut",
        "RoomUpdatedMetadataIn": "_cloudsearch_62_RoomUpdatedMetadataIn",
        "RoomUpdatedMetadataOut": "_cloudsearch_63_RoomUpdatedMetadataOut",
        "CallInfoIn": "_cloudsearch_64_CallInfoIn",
        "CallInfoOut": "_cloudsearch_65_CallInfoOut",
        "AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn": "_cloudsearch_66_AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn",
        "AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut": "_cloudsearch_67_AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn": "_cloudsearch_68_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut": "_cloudsearch_69_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut",
        "MembershipChangedMetadataIn": "_cloudsearch_70_MembershipChangedMetadataIn",
        "MembershipChangedMetadataOut": "_cloudsearch_71_MembershipChangedMetadataOut",
        "PostiniUserProtoIn": "_cloudsearch_72_PostiniUserProtoIn",
        "PostiniUserProtoOut": "_cloudsearch_73_PostiniUserProtoOut",
        "ShareScopeIn": "_cloudsearch_74_ShareScopeIn",
        "ShareScopeOut": "_cloudsearch_75_ShareScopeOut",
        "CustomEmojiMetadataIn": "_cloudsearch_76_CustomEmojiMetadataIn",
        "CustomEmojiMetadataOut": "_cloudsearch_77_CustomEmojiMetadataOut",
        "SpellResultIn": "_cloudsearch_78_SpellResultIn",
        "SpellResultOut": "_cloudsearch_79_SpellResultOut",
        "RequestFileScopeForActiveDocumentIn": "_cloudsearch_80_RequestFileScopeForActiveDocumentIn",
        "RequestFileScopeForActiveDocumentOut": "_cloudsearch_81_RequestFileScopeForActiveDocumentOut",
        "VideoCallMetadataIn": "_cloudsearch_82_VideoCallMetadataIn",
        "VideoCallMetadataOut": "_cloudsearch_83_VideoCallMetadataOut",
        "AppsDynamiteStorageOnClickIn": "_cloudsearch_84_AppsDynamiteStorageOnClickIn",
        "AppsDynamiteStorageOnClickOut": "_cloudsearch_85_AppsDynamiteStorageOnClickOut",
        "UnmappedIdentityIn": "_cloudsearch_86_UnmappedIdentityIn",
        "UnmappedIdentityOut": "_cloudsearch_87_UnmappedIdentityOut",
        "AppsDynamiteStorageMaterialIconIn": "_cloudsearch_88_AppsDynamiteStorageMaterialIconIn",
        "AppsDynamiteStorageMaterialIconOut": "_cloudsearch_89_AppsDynamiteStorageMaterialIconOut",
        "HtmlPropertyOptionsIn": "_cloudsearch_90_HtmlPropertyOptionsIn",
        "HtmlPropertyOptionsOut": "_cloudsearch_91_HtmlPropertyOptionsOut",
        "RankIn": "_cloudsearch_92_RankIn",
        "RankOut": "_cloudsearch_93_RankOut",
        "MessageDeletedIn": "_cloudsearch_94_MessageDeletedIn",
        "MessageDeletedOut": "_cloudsearch_95_MessageDeletedOut",
        "ButtonIn": "_cloudsearch_96_ButtonIn",
        "ButtonOut": "_cloudsearch_97_ButtonOut",
        "AppsDynamiteStorageColumnsIn": "_cloudsearch_98_AppsDynamiteStorageColumnsIn",
        "AppsDynamiteStorageColumnsOut": "_cloudsearch_99_AppsDynamiteStorageColumnsOut",
        "IntegerFacetingOptionsIn": "_cloudsearch_100_IntegerFacetingOptionsIn",
        "IntegerFacetingOptionsOut": "_cloudsearch_101_IntegerFacetingOptionsOut",
        "UserMentionMetadataIn": "_cloudsearch_102_UserMentionMetadataIn",
        "UserMentionMetadataOut": "_cloudsearch_103_UserMentionMetadataOut",
        "ToolbarIn": "_cloudsearch_104_ToolbarIn",
        "ToolbarOut": "_cloudsearch_105_ToolbarOut",
        "RbacSubjectProtoIn": "_cloudsearch_106_RbacSubjectProtoIn",
        "RbacSubjectProtoOut": "_cloudsearch_107_RbacSubjectProtoOut",
        "SlashCommandMetadataIn": "_cloudsearch_108_SlashCommandMetadataIn",
        "SlashCommandMetadataOut": "_cloudsearch_109_SlashCommandMetadataOut",
        "UserDisplayInfoIn": "_cloudsearch_110_UserDisplayInfoIn",
        "UserDisplayInfoOut": "_cloudsearch_111_UserDisplayInfoOut",
        "ItemIn": "_cloudsearch_112_ItemIn",
        "ItemOut": "_cloudsearch_113_ItemOut",
        "ThreadUpdateIn": "_cloudsearch_114_ThreadUpdateIn",
        "ThreadUpdateOut": "_cloudsearch_115_ThreadUpdateOut",
        "StructuredDataObjectIn": "_cloudsearch_116_StructuredDataObjectIn",
        "StructuredDataObjectOut": "_cloudsearch_117_StructuredDataObjectOut",
        "ObjectDefinitionIn": "_cloudsearch_118_ObjectDefinitionIn",
        "ObjectDefinitionOut": "_cloudsearch_119_ObjectDefinitionOut",
        "FacetResultIn": "_cloudsearch_120_FacetResultIn",
        "FacetResultOut": "_cloudsearch_121_FacetResultOut",
        "FormattingIn": "_cloudsearch_122_FormattingIn",
        "FormattingOut": "_cloudsearch_123_FormattingOut",
        "GoogleChatV1WidgetMarkupImageIn": "_cloudsearch_124_GoogleChatV1WidgetMarkupImageIn",
        "GoogleChatV1WidgetMarkupImageOut": "_cloudsearch_125_GoogleChatV1WidgetMarkupImageOut",
        "RestrictItemIn": "_cloudsearch_126_RestrictItemIn",
        "RestrictItemOut": "_cloudsearch_127_RestrictItemOut",
        "FuseboxPrefUpdatePreStateIn": "_cloudsearch_128_FuseboxPrefUpdatePreStateIn",
        "FuseboxPrefUpdatePreStateOut": "_cloudsearch_129_FuseboxPrefUpdatePreStateOut",
        "DriveMimeTypeRestrictIn": "_cloudsearch_130_DriveMimeTypeRestrictIn",
        "DriveMimeTypeRestrictOut": "_cloudsearch_131_DriveMimeTypeRestrictOut",
        "AppsDynamiteSharedOriginAppSuggestionIn": "_cloudsearch_132_AppsDynamiteSharedOriginAppSuggestionIn",
        "AppsDynamiteSharedOriginAppSuggestionOut": "_cloudsearch_133_AppsDynamiteSharedOriginAppSuggestionOut",
        "BorderStyleIn": "_cloudsearch_134_BorderStyleIn",
        "BorderStyleOut": "_cloudsearch_135_BorderStyleOut",
        "AttributesIn": "_cloudsearch_136_AttributesIn",
        "AttributesOut": "_cloudsearch_137_AttributesOut",
        "EnumPropertyOptionsIn": "_cloudsearch_138_EnumPropertyOptionsIn",
        "EnumPropertyOptionsOut": "_cloudsearch_139_EnumPropertyOptionsOut",
        "AppsDynamiteSharedDocumentIn": "_cloudsearch_140_AppsDynamiteSharedDocumentIn",
        "AppsDynamiteSharedDocumentOut": "_cloudsearch_141_AppsDynamiteSharedDocumentOut",
        "SearchItemsByViewUrlResponseIn": "_cloudsearch_142_SearchItemsByViewUrlResponseIn",
        "SearchItemsByViewUrlResponseOut": "_cloudsearch_143_SearchItemsByViewUrlResponseOut",
        "ProvenanceIn": "_cloudsearch_144_ProvenanceIn",
        "ProvenanceOut": "_cloudsearch_145_ProvenanceOut",
        "QueryInterpretationOptionsIn": "_cloudsearch_146_QueryInterpretationOptionsIn",
        "QueryInterpretationOptionsOut": "_cloudsearch_147_QueryInterpretationOptionsOut",
        "YouTubeLiveBroadcastEventIn": "_cloudsearch_148_YouTubeLiveBroadcastEventIn",
        "YouTubeLiveBroadcastEventOut": "_cloudsearch_149_YouTubeLiveBroadcastEventOut",
        "RoomRenameMetadataIn": "_cloudsearch_150_RoomRenameMetadataIn",
        "RoomRenameMetadataOut": "_cloudsearch_151_RoomRenameMetadataOut",
        "AppsDynamiteSharedEmojiIn": "_cloudsearch_152_AppsDynamiteSharedEmojiIn",
        "AppsDynamiteSharedEmojiOut": "_cloudsearch_153_AppsDynamiteSharedEmojiOut",
        "RosterIdIn": "_cloudsearch_154_RosterIdIn",
        "RosterIdOut": "_cloudsearch_155_RosterIdOut",
        "IconImageIn": "_cloudsearch_156_IconImageIn",
        "IconImageOut": "_cloudsearch_157_IconImageOut",
        "AppsDynamiteSharedActivityFeedAnnotationDataIn": "_cloudsearch_158_AppsDynamiteSharedActivityFeedAnnotationDataIn",
        "AppsDynamiteSharedActivityFeedAnnotationDataOut": "_cloudsearch_159_AppsDynamiteSharedActivityFeedAnnotationDataOut",
        "GatewayAccessIn": "_cloudsearch_160_GatewayAccessIn",
        "GatewayAccessOut": "_cloudsearch_161_GatewayAccessOut",
        "ContentReportJustificationIn": "_cloudsearch_162_ContentReportJustificationIn",
        "ContentReportJustificationOut": "_cloudsearch_163_ContentReportJustificationOut",
        "AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn": "_cloudsearch_164_AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn",
        "AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut": "_cloudsearch_165_AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut",
        "IndexItemOptionsIn": "_cloudsearch_166_IndexItemOptionsIn",
        "IndexItemOptionsOut": "_cloudsearch_167_IndexItemOptionsOut",
        "AppsDynamiteSharedDlpMetricsMetadataIn": "_cloudsearch_168_AppsDynamiteSharedDlpMetricsMetadataIn",
        "AppsDynamiteSharedDlpMetricsMetadataOut": "_cloudsearch_169_AppsDynamiteSharedDlpMetricsMetadataOut",
        "ObjectOptionsIn": "_cloudsearch_170_ObjectOptionsIn",
        "ObjectOptionsOut": "_cloudsearch_171_ObjectOptionsOut",
        "PushItemIn": "_cloudsearch_172_PushItemIn",
        "PushItemOut": "_cloudsearch_173_PushItemOut",
        "MdbUserProtoIn": "_cloudsearch_174_MdbUserProtoIn",
        "MdbUserProtoOut": "_cloudsearch_175_MdbUserProtoOut",
        "ActionParameterIn": "_cloudsearch_176_ActionParameterIn",
        "ActionParameterOut": "_cloudsearch_177_ActionParameterOut",
        "ChatProtoIn": "_cloudsearch_178_ChatProtoIn",
        "ChatProtoOut": "_cloudsearch_179_ChatProtoOut",
        "AppsDynamiteSharedMeetMetadataIn": "_cloudsearch_180_AppsDynamiteSharedMeetMetadataIn",
        "AppsDynamiteSharedMeetMetadataOut": "_cloudsearch_181_AppsDynamiteSharedMeetMetadataOut",
        "DateOperatorOptionsIn": "_cloudsearch_182_DateOperatorOptionsIn",
        "DateOperatorOptionsOut": "_cloudsearch_183_DateOperatorOptionsOut",
        "ContextualAddOnMarkupIn": "_cloudsearch_184_ContextualAddOnMarkupIn",
        "ContextualAddOnMarkupOut": "_cloudsearch_185_ContextualAddOnMarkupOut",
        "YoutubeUserProtoIn": "_cloudsearch_186_YoutubeUserProtoIn",
        "YoutubeUserProtoOut": "_cloudsearch_187_YoutubeUserProtoOut",
        "EditorClientActionMarkupIn": "_cloudsearch_188_EditorClientActionMarkupIn",
        "EditorClientActionMarkupOut": "_cloudsearch_189_EditorClientActionMarkupOut",
        "ResultDisplayLineIn": "_cloudsearch_190_ResultDisplayLineIn",
        "ResultDisplayLineOut": "_cloudsearch_191_ResultDisplayLineOut",
        "AuthorizedItemIdIn": "_cloudsearch_192_AuthorizedItemIdIn",
        "AuthorizedItemIdOut": "_cloudsearch_193_AuthorizedItemIdOut",
        "GaiaUserProtoIn": "_cloudsearch_194_GaiaUserProtoIn",
        "GaiaUserProtoOut": "_cloudsearch_195_GaiaUserProtoOut",
        "AutoCompleteIn": "_cloudsearch_196_AutoCompleteIn",
        "AutoCompleteOut": "_cloudsearch_197_AutoCompleteOut",
        "AppsDynamiteSharedChatItemIn": "_cloudsearch_198_AppsDynamiteSharedChatItemIn",
        "AppsDynamiteSharedChatItemOut": "_cloudsearch_199_AppsDynamiteSharedChatItemOut",
        "EmailAddressIn": "_cloudsearch_200_EmailAddressIn",
        "EmailAddressOut": "_cloudsearch_201_EmailAddressOut",
        "CustomFunctionReturnValueMarkupIn": "_cloudsearch_202_CustomFunctionReturnValueMarkupIn",
        "CustomFunctionReturnValueMarkupOut": "_cloudsearch_203_CustomFunctionReturnValueMarkupOut",
        "AppsDynamiteSharedCustomEmojiIn": "_cloudsearch_204_AppsDynamiteSharedCustomEmojiIn",
        "AppsDynamiteSharedCustomEmojiOut": "_cloudsearch_205_AppsDynamiteSharedCustomEmojiOut",
        "ContentReportSummaryIn": "_cloudsearch_206_ContentReportSummaryIn",
        "ContentReportSummaryOut": "_cloudsearch_207_ContentReportSummaryOut",
        "DeleteMetadataIn": "_cloudsearch_208_DeleteMetadataIn",
        "DeleteMetadataOut": "_cloudsearch_209_DeleteMetadataOut",
        "GetCustomerSessionStatsResponseIn": "_cloudsearch_210_GetCustomerSessionStatsResponseIn",
        "GetCustomerSessionStatsResponseOut": "_cloudsearch_211_GetCustomerSessionStatsResponseOut",
        "ChatContentExtensionIn": "_cloudsearch_212_ChatContentExtensionIn",
        "ChatContentExtensionOut": "_cloudsearch_213_ChatContentExtensionOut",
        "RbacRoleProtoIn": "_cloudsearch_214_RbacRoleProtoIn",
        "RbacRoleProtoOut": "_cloudsearch_215_RbacRoleProtoOut",
        "UpdateSchemaRequestIn": "_cloudsearch_216_UpdateSchemaRequestIn",
        "UpdateSchemaRequestOut": "_cloudsearch_217_UpdateSchemaRequestOut",
        "QueryOperatorIn": "_cloudsearch_218_QueryOperatorIn",
        "QueryOperatorOut": "_cloudsearch_219_QueryOperatorOut",
        "GoogleChatV1WidgetMarkupFormActionActionParameterIn": "_cloudsearch_220_GoogleChatV1WidgetMarkupFormActionActionParameterIn",
        "GoogleChatV1WidgetMarkupFormActionActionParameterOut": "_cloudsearch_221_GoogleChatV1WidgetMarkupFormActionActionParameterOut",
        "PollItemsRequestIn": "_cloudsearch_222_PollItemsRequestIn",
        "PollItemsRequestOut": "_cloudsearch_223_PollItemsRequestOut",
        "ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn": "_cloudsearch_224_ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut": "_cloudsearch_225_ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut",
        "AppsDynamiteSharedCallAnnotationDataIn": "_cloudsearch_226_AppsDynamiteSharedCallAnnotationDataIn",
        "AppsDynamiteSharedCallAnnotationDataOut": "_cloudsearch_227_AppsDynamiteSharedCallAnnotationDataOut",
        "AppsDynamiteSharedVideoReferenceIn": "_cloudsearch_228_AppsDynamiteSharedVideoReferenceIn",
        "AppsDynamiteSharedVideoReferenceOut": "_cloudsearch_229_AppsDynamiteSharedVideoReferenceOut",
        "AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn": "_cloudsearch_230_AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn",
        "AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut": "_cloudsearch_231_AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut",
        "LabelRenamedIn": "_cloudsearch_232_LabelRenamedIn",
        "LabelRenamedOut": "_cloudsearch_233_LabelRenamedOut",
        "ErrorInfoIn": "_cloudsearch_234_ErrorInfoIn",
        "ErrorInfoOut": "_cloudsearch_235_ErrorInfoOut",
        "GoogleChatV1ContextualAddOnMarkupCardIn": "_cloudsearch_236_GoogleChatV1ContextualAddOnMarkupCardIn",
        "GoogleChatV1ContextualAddOnMarkupCardOut": "_cloudsearch_237_GoogleChatV1ContextualAddOnMarkupCardOut",
        "ObjectValuesIn": "_cloudsearch_238_ObjectValuesIn",
        "ObjectValuesOut": "_cloudsearch_239_ObjectValuesOut",
        "ContextAttributeIn": "_cloudsearch_240_ContextAttributeIn",
        "ContextAttributeOut": "_cloudsearch_241_ContextAttributeOut",
        "TriggerActionIn": "_cloudsearch_242_TriggerActionIn",
        "TriggerActionOut": "_cloudsearch_243_TriggerActionOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn": "_cloudsearch_244_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut": "_cloudsearch_245_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut",
        "ResetSearchApplicationRequestIn": "_cloudsearch_246_ResetSearchApplicationRequestIn",
        "ResetSearchApplicationRequestOut": "_cloudsearch_247_ResetSearchApplicationRequestOut",
        "PhotoIn": "_cloudsearch_248_PhotoIn",
        "PhotoOut": "_cloudsearch_249_PhotoOut",
        "AppsDynamiteStorageSelectionInputSelectionItemIn": "_cloudsearch_250_AppsDynamiteStorageSelectionInputSelectionItemIn",
        "AppsDynamiteStorageSelectionInputSelectionItemOut": "_cloudsearch_251_AppsDynamiteStorageSelectionInputSelectionItemOut",
        "AttributeRemovedIn": "_cloudsearch_252_AttributeRemovedIn",
        "AttributeRemovedOut": "_cloudsearch_253_AttributeRemovedOut",
        "AppsDynamiteSharedSegmentedMembershipCountIn": "_cloudsearch_254_AppsDynamiteSharedSegmentedMembershipCountIn",
        "AppsDynamiteSharedSegmentedMembershipCountOut": "_cloudsearch_255_AppsDynamiteSharedSegmentedMembershipCountOut",
        "MultiKeyIn": "_cloudsearch_256_MultiKeyIn",
        "MultiKeyOut": "_cloudsearch_257_MultiKeyOut",
        "UpdateSubjectIn": "_cloudsearch_258_UpdateSubjectIn",
        "UpdateSubjectOut": "_cloudsearch_259_UpdateSubjectOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn": "_cloudsearch_260_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut": "_cloudsearch_261_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut",
        "StreamingSessionInfoIn": "_cloudsearch_262_StreamingSessionInfoIn",
        "StreamingSessionInfoOut": "_cloudsearch_263_StreamingSessionInfoOut",
        "RecordingInfoIn": "_cloudsearch_264_RecordingInfoIn",
        "RecordingInfoOut": "_cloudsearch_265_RecordingInfoOut",
        "HtmlValuesIn": "_cloudsearch_266_HtmlValuesIn",
        "HtmlValuesOut": "_cloudsearch_267_HtmlValuesOut",
        "ClusterInfoIn": "_cloudsearch_268_ClusterInfoIn",
        "ClusterInfoOut": "_cloudsearch_269_ClusterInfoOut",
        "SortOptionsIn": "_cloudsearch_270_SortOptionsIn",
        "SortOptionsOut": "_cloudsearch_271_SortOptionsOut",
        "GoogleChatV1ContextualAddOnMarkupCardSectionIn": "_cloudsearch_272_GoogleChatV1ContextualAddOnMarkupCardSectionIn",
        "GoogleChatV1ContextualAddOnMarkupCardSectionOut": "_cloudsearch_273_GoogleChatV1ContextualAddOnMarkupCardSectionOut",
        "ImapSessionContextIn": "_cloudsearch_274_ImapSessionContextIn",
        "ImapSessionContextOut": "_cloudsearch_275_ImapSessionContextOut",
        "IndexItemRequestIn": "_cloudsearch_276_IndexItemRequestIn",
        "IndexItemRequestOut": "_cloudsearch_277_IndexItemRequestOut",
        "LabelUpdatedIn": "_cloudsearch_278_LabelUpdatedIn",
        "LabelUpdatedOut": "_cloudsearch_279_LabelUpdatedOut",
        "AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn": "_cloudsearch_280_AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn",
        "AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut": "_cloudsearch_281_AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut",
        "GroupDetailsUpdatedMetadataIn": "_cloudsearch_282_GroupDetailsUpdatedMetadataIn",
        "GroupDetailsUpdatedMetadataOut": "_cloudsearch_283_GroupDetailsUpdatedMetadataOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn": "_cloudsearch_284_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut": "_cloudsearch_285_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut",
        "FolderAttributeIn": "_cloudsearch_286_FolderAttributeIn",
        "FolderAttributeOut": "_cloudsearch_287_FolderAttributeOut",
        "AffectedMembershipIn": "_cloudsearch_288_AffectedMembershipIn",
        "AffectedMembershipOut": "_cloudsearch_289_AffectedMembershipOut",
        "ChatConserverDynamitePlaceholderMetadataIn": "_cloudsearch_290_ChatConserverDynamitePlaceholderMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataOut": "_cloudsearch_291_ChatConserverDynamitePlaceholderMetadataOut",
        "DividerIn": "_cloudsearch_292_DividerIn",
        "DividerOut": "_cloudsearch_293_DividerOut",
        "ResourceRoleProtoIn": "_cloudsearch_294_ResourceRoleProtoIn",
        "ResourceRoleProtoOut": "_cloudsearch_295_ResourceRoleProtoOut",
        "PhoneAccessIn": "_cloudsearch_296_PhoneAccessIn",
        "PhoneAccessOut": "_cloudsearch_297_PhoneAccessOut",
        "CoActivityIn": "_cloudsearch_298_CoActivityIn",
        "CoActivityOut": "_cloudsearch_299_CoActivityOut",
        "VPCSettingsIn": "_cloudsearch_300_VPCSettingsIn",
        "VPCSettingsOut": "_cloudsearch_301_VPCSettingsOut",
        "ItemAclIn": "_cloudsearch_302_ItemAclIn",
        "ItemAclOut": "_cloudsearch_303_ItemAclOut",
        "SimpleSecretHolderProtoIn": "_cloudsearch_304_SimpleSecretHolderProtoIn",
        "SimpleSecretHolderProtoOut": "_cloudsearch_305_SimpleSecretHolderProtoOut",
        "ListDataSourceResponseIn": "_cloudsearch_306_ListDataSourceResponseIn",
        "ListDataSourceResponseOut": "_cloudsearch_307_ListDataSourceResponseOut",
        "AppsDynamiteSharedAvatarInfoIn": "_cloudsearch_308_AppsDynamiteSharedAvatarInfoIn",
        "AppsDynamiteSharedAvatarInfoOut": "_cloudsearch_309_AppsDynamiteSharedAvatarInfoOut",
        "ListOperationsResponseIn": "_cloudsearch_310_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudsearch_311_ListOperationsResponseOut",
        "PresenterIn": "_cloudsearch_312_PresenterIn",
        "PresenterOut": "_cloudsearch_313_PresenterOut",
        "FreshnessOptionsIn": "_cloudsearch_314_FreshnessOptionsIn",
        "FreshnessOptionsOut": "_cloudsearch_315_FreshnessOptionsOut",
        "CheckAccessResponseIn": "_cloudsearch_316_CheckAccessResponseIn",
        "CheckAccessResponseOut": "_cloudsearch_317_CheckAccessResponseOut",
        "DriveFollowUpRestrictIn": "_cloudsearch_318_DriveFollowUpRestrictIn",
        "DriveFollowUpRestrictOut": "_cloudsearch_319_DriveFollowUpRestrictOut",
        "TopicStateIn": "_cloudsearch_320_TopicStateIn",
        "TopicStateOut": "_cloudsearch_321_TopicStateOut",
        "SourceConfigIn": "_cloudsearch_322_SourceConfigIn",
        "SourceConfigOut": "_cloudsearch_323_SourceConfigOut",
        "QueryInterpretationIn": "_cloudsearch_324_QueryInterpretationIn",
        "QueryInterpretationOut": "_cloudsearch_325_QueryInterpretationOut",
        "FacetBucketIn": "_cloudsearch_326_FacetBucketIn",
        "FacetBucketOut": "_cloudsearch_327_FacetBucketOut",
        "TextValuesIn": "_cloudsearch_328_TextValuesIn",
        "TextValuesOut": "_cloudsearch_329_TextValuesOut",
        "AppsDynamiteStorageImageIn": "_cloudsearch_330_AppsDynamiteStorageImageIn",
        "AppsDynamiteStorageImageOut": "_cloudsearch_331_AppsDynamiteStorageImageOut",
        "TopicIdIn": "_cloudsearch_332_TopicIdIn",
        "TopicIdOut": "_cloudsearch_333_TopicIdOut",
        "MatchRangeIn": "_cloudsearch_334_MatchRangeIn",
        "MatchRangeOut": "_cloudsearch_335_MatchRangeOut",
        "SuggestResponseIn": "_cloudsearch_336_SuggestResponseIn",
        "SuggestResponseOut": "_cloudsearch_337_SuggestResponseOut",
        "MediaIn": "_cloudsearch_338_MediaIn",
        "MediaOut": "_cloudsearch_339_MediaOut",
        "WonderMessageMappingIn": "_cloudsearch_340_WonderMessageMappingIn",
        "WonderMessageMappingOut": "_cloudsearch_341_WonderMessageMappingOut",
        "TrustedResourceUrlProtoIn": "_cloudsearch_342_TrustedResourceUrlProtoIn",
        "TrustedResourceUrlProtoOut": "_cloudsearch_343_TrustedResourceUrlProtoOut",
        "ClientContextIn": "_cloudsearch_344_ClientContextIn",
        "ClientContextOut": "_cloudsearch_345_ClientContextOut",
        "SuggestResultIn": "_cloudsearch_346_SuggestResultIn",
        "SuggestResultOut": "_cloudsearch_347_SuggestResultOut",
        "AclFixStatusIn": "_cloudsearch_348_AclFixStatusIn",
        "AclFixStatusOut": "_cloudsearch_349_AclFixStatusOut",
        "ListItemsResponseIn": "_cloudsearch_350_ListItemsResponseIn",
        "ListItemsResponseOut": "_cloudsearch_351_ListItemsResponseOut",
        "RenameEventIn": "_cloudsearch_352_RenameEventIn",
        "RenameEventOut": "_cloudsearch_353_RenameEventOut",
        "AppsDynamiteStorageIconIn": "_cloudsearch_354_AppsDynamiteStorageIconIn",
        "AppsDynamiteStorageIconOut": "_cloudsearch_355_AppsDynamiteStorageIconOut",
        "DataLossPreventionMetadataIn": "_cloudsearch_356_DataLossPreventionMetadataIn",
        "DataLossPreventionMetadataOut": "_cloudsearch_357_DataLossPreventionMetadataOut",
        "BroadcastStatsIn": "_cloudsearch_358_BroadcastStatsIn",
        "BroadcastStatsOut": "_cloudsearch_359_BroadcastStatsOut",
        "AppsDynamiteSharedChatItemActivityInfoIn": "_cloudsearch_360_AppsDynamiteSharedChatItemActivityInfoIn",
        "AppsDynamiteSharedChatItemActivityInfoOut": "_cloudsearch_361_AppsDynamiteSharedChatItemActivityInfoOut",
        "SchemaIn": "_cloudsearch_362_SchemaIn",
        "SchemaOut": "_cloudsearch_363_SchemaOut",
        "GetCustomerIndexStatsResponseIn": "_cloudsearch_364_GetCustomerIndexStatsResponseIn",
        "GetCustomerIndexStatsResponseOut": "_cloudsearch_365_GetCustomerIndexStatsResponseOut",
        "TextPropertyOptionsIn": "_cloudsearch_366_TextPropertyOptionsIn",
        "TextPropertyOptionsOut": "_cloudsearch_367_TextPropertyOptionsOut",
        "EmbedClientItemIn": "_cloudsearch_368_EmbedClientItemIn",
        "EmbedClientItemOut": "_cloudsearch_369_EmbedClientItemOut",
        "ConsentedAppUnfurlMetadataIn": "_cloudsearch_370_ConsentedAppUnfurlMetadataIn",
        "ConsentedAppUnfurlMetadataOut": "_cloudsearch_371_ConsentedAppUnfurlMetadataOut",
        "AnnotationIn": "_cloudsearch_372_AnnotationIn",
        "AnnotationOut": "_cloudsearch_373_AnnotationOut",
        "SessionContextIn": "_cloudsearch_374_SessionContextIn",
        "SessionContextOut": "_cloudsearch_375_SessionContextOut",
        "ItemContentIn": "_cloudsearch_376_ItemContentIn",
        "ItemContentOut": "_cloudsearch_377_ItemContentOut",
        "CustomerSessionStatsIn": "_cloudsearch_378_CustomerSessionStatsIn",
        "CustomerSessionStatsOut": "_cloudsearch_379_CustomerSessionStatsOut",
        "VoicePhoneNumberI18nDataIn": "_cloudsearch_380_VoicePhoneNumberI18nDataIn",
        "VoicePhoneNumberI18nDataOut": "_cloudsearch_381_VoicePhoneNumberI18nDataOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn": "_cloudsearch_382_AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut": "_cloudsearch_383_AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut",
        "FilterIn": "_cloudsearch_384_FilterIn",
        "FilterOut": "_cloudsearch_385_FilterOut",
        "RecordingSessionInfoIn": "_cloudsearch_386_RecordingSessionInfoIn",
        "RecordingSessionInfoOut": "_cloudsearch_387_RecordingSessionInfoOut",
        "AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn": "_cloudsearch_388_AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn",
        "AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut": "_cloudsearch_389_AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut",
        "ResultDisplayFieldIn": "_cloudsearch_390_ResultDisplayFieldIn",
        "ResultDisplayFieldOut": "_cloudsearch_391_ResultDisplayFieldOut",
        "PreStateIn": "_cloudsearch_392_PreStateIn",
        "PreStateOut": "_cloudsearch_393_PreStateOut",
        "DataSourceRestrictionIn": "_cloudsearch_394_DataSourceRestrictionIn",
        "DataSourceRestrictionOut": "_cloudsearch_395_DataSourceRestrictionOut",
        "AppsDynamiteSharedGroupVisibilityIn": "_cloudsearch_396_AppsDynamiteSharedGroupVisibilityIn",
        "AppsDynamiteSharedGroupVisibilityOut": "_cloudsearch_397_AppsDynamiteSharedGroupVisibilityOut",
        "HostAppActionMarkupIn": "_cloudsearch_398_HostAppActionMarkupIn",
        "HostAppActionMarkupOut": "_cloudsearch_399_HostAppActionMarkupOut",
        "PollItemsResponseIn": "_cloudsearch_400_PollItemsResponseIn",
        "PollItemsResponseOut": "_cloudsearch_401_PollItemsResponseOut",
        "ObjectPropertyOptionsIn": "_cloudsearch_402_ObjectPropertyOptionsIn",
        "ObjectPropertyOptionsOut": "_cloudsearch_403_ObjectPropertyOptionsOut",
        "AppsDynamiteSharedDimensionIn": "_cloudsearch_404_AppsDynamiteSharedDimensionIn",
        "AppsDynamiteSharedDimensionOut": "_cloudsearch_405_AppsDynamiteSharedDimensionOut",
        "AppsDynamiteSharedJustificationIn": "_cloudsearch_406_AppsDynamiteSharedJustificationIn",
        "AppsDynamiteSharedJustificationOut": "_cloudsearch_407_AppsDynamiteSharedJustificationOut",
        "YouTubeBroadcastStatsIn": "_cloudsearch_408_YouTubeBroadcastStatsIn",
        "YouTubeBroadcastStatsOut": "_cloudsearch_409_YouTubeBroadcastStatsOut",
        "AppsDynamiteStorageDividerIn": "_cloudsearch_410_AppsDynamiteStorageDividerIn",
        "AppsDynamiteStorageDividerOut": "_cloudsearch_411_AppsDynamiteStorageDividerOut",
        "HashtagDataIn": "_cloudsearch_412_HashtagDataIn",
        "HashtagDataOut": "_cloudsearch_413_HashtagDataOut",
        "ChatConserverMessageContentIn": "_cloudsearch_414_ChatConserverMessageContentIn",
        "ChatConserverMessageContentOut": "_cloudsearch_415_ChatConserverMessageContentOut",
        "MessageAttributesIn": "_cloudsearch_416_MessageAttributesIn",
        "MessageAttributesOut": "_cloudsearch_417_MessageAttributesOut",
        "PaygateInfoIn": "_cloudsearch_418_PaygateInfoIn",
        "PaygateInfoOut": "_cloudsearch_419_PaygateInfoOut",
        "AppsDynamiteSharedBackendUploadMetadataIn": "_cloudsearch_420_AppsDynamiteSharedBackendUploadMetadataIn",
        "AppsDynamiteSharedBackendUploadMetadataOut": "_cloudsearch_421_AppsDynamiteSharedBackendUploadMetadataOut",
        "SupportUrlsIn": "_cloudsearch_422_SupportUrlsIn",
        "SupportUrlsOut": "_cloudsearch_423_SupportUrlsOut",
        "AppsDynamiteStorageTextInputIn": "_cloudsearch_424_AppsDynamiteStorageTextInputIn",
        "AppsDynamiteStorageTextInputOut": "_cloudsearch_425_AppsDynamiteStorageTextInputOut",
        "TriggerIn": "_cloudsearch_426_TriggerIn",
        "TriggerOut": "_cloudsearch_427_TriggerOut",
        "GoogleDocsMetadataIn": "_cloudsearch_428_GoogleDocsMetadataIn",
        "GoogleDocsMetadataOut": "_cloudsearch_429_GoogleDocsMetadataOut",
        "DoubleOperatorOptionsIn": "_cloudsearch_430_DoubleOperatorOptionsIn",
        "DoubleOperatorOptionsOut": "_cloudsearch_431_DoubleOperatorOptionsOut",
        "GoogleChatV1ContextualAddOnMarkupIn": "_cloudsearch_432_GoogleChatV1ContextualAddOnMarkupIn",
        "GoogleChatV1ContextualAddOnMarkupOut": "_cloudsearch_433_GoogleChatV1ContextualAddOnMarkupOut",
        "TextOperatorOptionsIn": "_cloudsearch_434_TextOperatorOptionsIn",
        "TextOperatorOptionsOut": "_cloudsearch_435_TextOperatorOptionsOut",
        "AppsDynamiteSharedContentReportTypeIn": "_cloudsearch_436_AppsDynamiteSharedContentReportTypeIn",
        "AppsDynamiteSharedContentReportTypeOut": "_cloudsearch_437_AppsDynamiteSharedContentReportTypeOut",
        "SearchQualityMetadataIn": "_cloudsearch_438_SearchQualityMetadataIn",
        "SearchQualityMetadataOut": "_cloudsearch_439_SearchQualityMetadataOut",
        "InteractionIn": "_cloudsearch_440_InteractionIn",
        "InteractionOut": "_cloudsearch_441_InteractionOut",
        "AttributeIn": "_cloudsearch_442_AttributeIn",
        "AttributeOut": "_cloudsearch_443_AttributeOut",
        "QueryItemIn": "_cloudsearch_444_QueryItemIn",
        "QueryItemOut": "_cloudsearch_445_QueryItemOut",
        "AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn": "_cloudsearch_446_AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut": "_cloudsearch_447_AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut",
        "AppsDynamiteSharedAssistantUnfulfillableRequestIn": "_cloudsearch_448_AppsDynamiteSharedAssistantUnfulfillableRequestIn",
        "AppsDynamiteSharedAssistantUnfulfillableRequestOut": "_cloudsearch_449_AppsDynamiteSharedAssistantUnfulfillableRequestOut",
        "AppsDynamiteSharedSegmentedMembershipCountsIn": "_cloudsearch_450_AppsDynamiteSharedSegmentedMembershipCountsIn",
        "AppsDynamiteSharedSegmentedMembershipCountsOut": "_cloudsearch_451_AppsDynamiteSharedSegmentedMembershipCountsOut",
        "TranscriptionSessionInfoIn": "_cloudsearch_452_TranscriptionSessionInfoIn",
        "TranscriptionSessionInfoOut": "_cloudsearch_453_TranscriptionSessionInfoOut",
        "IntegrationConfigUpdatedMetadataIn": "_cloudsearch_454_IntegrationConfigUpdatedMetadataIn",
        "IntegrationConfigUpdatedMetadataOut": "_cloudsearch_455_IntegrationConfigUpdatedMetadataOut",
        "PrincipalProtoIn": "_cloudsearch_456_PrincipalProtoIn",
        "PrincipalProtoOut": "_cloudsearch_457_PrincipalProtoOut",
        "CardActionIn": "_cloudsearch_458_CardActionIn",
        "CardActionOut": "_cloudsearch_459_CardActionOut",
        "ReferenceIn": "_cloudsearch_460_ReferenceIn",
        "ReferenceOut": "_cloudsearch_461_ReferenceOut",
        "DlpScanSummaryIn": "_cloudsearch_462_DlpScanSummaryIn",
        "DlpScanSummaryOut": "_cloudsearch_463_DlpScanSummaryOut",
        "AppsDynamiteSharedOrganizationInfoCustomerInfoIn": "_cloudsearch_464_AppsDynamiteSharedOrganizationInfoCustomerInfoIn",
        "AppsDynamiteSharedOrganizationInfoCustomerInfoOut": "_cloudsearch_465_AppsDynamiteSharedOrganizationInfoCustomerInfoOut",
        "CaribouAttributeValueIn": "_cloudsearch_466_CaribouAttributeValueIn",
        "CaribouAttributeValueOut": "_cloudsearch_467_CaribouAttributeValueOut",
        "AppsDynamiteV1ApiCompatV1FieldIn": "_cloudsearch_468_AppsDynamiteV1ApiCompatV1FieldIn",
        "AppsDynamiteV1ApiCompatV1FieldOut": "_cloudsearch_469_AppsDynamiteV1ApiCompatV1FieldOut",
        "SearchResultIn": "_cloudsearch_470_SearchResultIn",
        "SearchResultOut": "_cloudsearch_471_SearchResultOut",
        "AppsDynamiteSharedMessageInfoIn": "_cloudsearch_472_AppsDynamiteSharedMessageInfoIn",
        "AppsDynamiteSharedMessageInfoOut": "_cloudsearch_473_AppsDynamiteSharedMessageInfoOut",
        "SearchApplicationSessionStatsIn": "_cloudsearch_474_SearchApplicationSessionStatsIn",
        "SearchApplicationSessionStatsOut": "_cloudsearch_475_SearchApplicationSessionStatsOut",
        "AppIdIn": "_cloudsearch_476_AppIdIn",
        "AppIdOut": "_cloudsearch_477_AppIdOut",
        "ImageKeyValueIn": "_cloudsearch_478_ImageKeyValueIn",
        "ImageKeyValueOut": "_cloudsearch_479_ImageKeyValueOut",
        "AppsDynamiteStorageButtonListIn": "_cloudsearch_480_AppsDynamiteStorageButtonListIn",
        "AppsDynamiteStorageButtonListOut": "_cloudsearch_481_AppsDynamiteStorageButtonListOut",
        "SocialGraphNodeProtoIn": "_cloudsearch_482_SocialGraphNodeProtoIn",
        "SocialGraphNodeProtoOut": "_cloudsearch_483_SocialGraphNodeProtoOut",
        "DoublePropertyOptionsIn": "_cloudsearch_484_DoublePropertyOptionsIn",
        "DoublePropertyOptionsOut": "_cloudsearch_485_DoublePropertyOptionsOut",
        "GSuitePrincipalIn": "_cloudsearch_486_GSuitePrincipalIn",
        "GSuitePrincipalOut": "_cloudsearch_487_GSuitePrincipalOut",
        "AppsDynamiteSharedRetentionSettingsIn": "_cloudsearch_488_AppsDynamiteSharedRetentionSettingsIn",
        "AppsDynamiteSharedRetentionSettingsOut": "_cloudsearch_489_AppsDynamiteSharedRetentionSettingsOut",
        "CardIn": "_cloudsearch_490_CardIn",
        "CardOut": "_cloudsearch_491_CardOut",
        "AppsDynamiteStorageOpenLinkAppUriIn": "_cloudsearch_492_AppsDynamiteStorageOpenLinkAppUriIn",
        "AppsDynamiteStorageOpenLinkAppUriOut": "_cloudsearch_493_AppsDynamiteStorageOpenLinkAppUriOut",
        "ResultDisplayMetadataIn": "_cloudsearch_494_ResultDisplayMetadataIn",
        "ResultDisplayMetadataOut": "_cloudsearch_495_ResultDisplayMetadataOut",
        "FormatMetadataIn": "_cloudsearch_496_FormatMetadataIn",
        "FormatMetadataOut": "_cloudsearch_497_FormatMetadataOut",
        "AppsDynamiteSharedJustificationPersonIn": "_cloudsearch_498_AppsDynamiteSharedJustificationPersonIn",
        "AppsDynamiteSharedJustificationPersonOut": "_cloudsearch_499_AppsDynamiteSharedJustificationPersonOut",
        "MessageParentIdIn": "_cloudsearch_500_MessageParentIdIn",
        "MessageParentIdOut": "_cloudsearch_501_MessageParentIdOut",
        "HistoryRecordIn": "_cloudsearch_502_HistoryRecordIn",
        "HistoryRecordOut": "_cloudsearch_503_HistoryRecordOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataIn": "_cloudsearch_504_AppsDynamiteSharedCalendarEventAnnotationDataIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataOut": "_cloudsearch_505_AppsDynamiteSharedCalendarEventAnnotationDataOut",
        "AppsDynamiteV1ApiCompatV1AttachmentIn": "_cloudsearch_506_AppsDynamiteV1ApiCompatV1AttachmentIn",
        "AppsDynamiteV1ApiCompatV1AttachmentOut": "_cloudsearch_507_AppsDynamiteV1ApiCompatV1AttachmentOut",
        "DatePropertyOptionsIn": "_cloudsearch_508_DatePropertyOptionsIn",
        "DatePropertyOptionsOut": "_cloudsearch_509_DatePropertyOptionsOut",
        "AppsDynamiteSharedTasksAnnotationDataCreationIn": "_cloudsearch_510_AppsDynamiteSharedTasksAnnotationDataCreationIn",
        "AppsDynamiteSharedTasksAnnotationDataCreationOut": "_cloudsearch_511_AppsDynamiteSharedTasksAnnotationDataCreationOut",
        "ListItemNamesForUnmappedIdentityResponseIn": "_cloudsearch_512_ListItemNamesForUnmappedIdentityResponseIn",
        "ListItemNamesForUnmappedIdentityResponseOut": "_cloudsearch_513_ListItemNamesForUnmappedIdentityResponseOut",
        "AppsDynamiteStorageActionIn": "_cloudsearch_514_AppsDynamiteStorageActionIn",
        "AppsDynamiteStorageActionOut": "_cloudsearch_515_AppsDynamiteStorageActionOut",
        "ColorIn": "_cloudsearch_516_ColorIn",
        "ColorOut": "_cloudsearch_517_ColorOut",
        "HangoutVideoEventMetadataIn": "_cloudsearch_518_HangoutVideoEventMetadataIn",
        "HangoutVideoEventMetadataOut": "_cloudsearch_519_HangoutVideoEventMetadataOut",
        "ListQuerySourcesResponseIn": "_cloudsearch_520_ListQuerySourcesResponseIn",
        "ListQuerySourcesResponseOut": "_cloudsearch_521_ListQuerySourcesResponseOut",
        "AppsDynamiteSharedAssistantAnnotationDataIn": "_cloudsearch_522_AppsDynamiteSharedAssistantAnnotationDataIn",
        "AppsDynamiteSharedAssistantAnnotationDataOut": "_cloudsearch_523_AppsDynamiteSharedAssistantAnnotationDataOut",
        "UpdateBccRecipientsIn": "_cloudsearch_524_UpdateBccRecipientsIn",
        "UpdateBccRecipientsOut": "_cloudsearch_525_UpdateBccRecipientsOut",
        "ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn": "_cloudsearch_526_ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut": "_cloudsearch_527_ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut",
        "ImapSyncDeleteIn": "_cloudsearch_528_ImapSyncDeleteIn",
        "ImapSyncDeleteOut": "_cloudsearch_529_ImapSyncDeleteOut",
        "ChatConserverDynamitePlaceholderMetadataTasksMetadataIn": "_cloudsearch_530_ChatConserverDynamitePlaceholderMetadataTasksMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataTasksMetadataOut": "_cloudsearch_531_ChatConserverDynamitePlaceholderMetadataTasksMetadataOut",
        "GoogleChatV1WidgetMarkupImageButtonIn": "_cloudsearch_532_GoogleChatV1WidgetMarkupImageButtonIn",
        "GoogleChatV1WidgetMarkupImageButtonOut": "_cloudsearch_533_GoogleChatV1WidgetMarkupImageButtonOut",
        "MessageIdIn": "_cloudsearch_534_MessageIdIn",
        "MessageIdOut": "_cloudsearch_535_MessageIdOut",
        "AppsDynamiteSharedUserBlockRelationshipIn": "_cloudsearch_536_AppsDynamiteSharedUserBlockRelationshipIn",
        "AppsDynamiteSharedUserBlockRelationshipOut": "_cloudsearch_537_AppsDynamiteSharedUserBlockRelationshipOut",
        "MatchInfoIn": "_cloudsearch_538_MatchInfoIn",
        "MatchInfoOut": "_cloudsearch_539_MatchInfoOut",
        "OperationIn": "_cloudsearch_540_OperationIn",
        "OperationOut": "_cloudsearch_541_OperationOut",
        "UpdateDataSourceRequestIn": "_cloudsearch_542_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_cloudsearch_543_UpdateDataSourceRequestOut",
        "ImageComponentIn": "_cloudsearch_544_ImageComponentIn",
        "ImageComponentOut": "_cloudsearch_545_ImageComponentOut",
        "DebugOptionsIn": "_cloudsearch_546_DebugOptionsIn",
        "DebugOptionsOut": "_cloudsearch_547_DebugOptionsOut",
        "AppsDynamiteStorageGridIn": "_cloudsearch_548_AppsDynamiteStorageGridIn",
        "AppsDynamiteStorageGridOut": "_cloudsearch_549_AppsDynamiteStorageGridOut",
        "AppsDynamiteSharedOrganizationInfoConsumerInfoIn": "_cloudsearch_550_AppsDynamiteSharedOrganizationInfoConsumerInfoIn",
        "AppsDynamiteSharedOrganizationInfoConsumerInfoOut": "_cloudsearch_551_AppsDynamiteSharedOrganizationInfoConsumerInfoOut",
        "CalendarClientActionMarkupIn": "_cloudsearch_552_CalendarClientActionMarkupIn",
        "CalendarClientActionMarkupOut": "_cloudsearch_553_CalendarClientActionMarkupOut",
        "SpaceIdIn": "_cloudsearch_554_SpaceIdIn",
        "SpaceIdOut": "_cloudsearch_555_SpaceIdOut",
        "AppsDynamiteStorageDecoratedTextIn": "_cloudsearch_556_AppsDynamiteStorageDecoratedTextIn",
        "AppsDynamiteStorageDecoratedTextOut": "_cloudsearch_557_AppsDynamiteStorageDecoratedTextOut",
        "SearchResponseIn": "_cloudsearch_558_SearchResponseIn",
        "SearchResponseOut": "_cloudsearch_559_SearchResponseOut",
        "InitializeCustomerRequestIn": "_cloudsearch_560_InitializeCustomerRequestIn",
        "InitializeCustomerRequestOut": "_cloudsearch_561_InitializeCustomerRequestOut",
        "FixedFooterIn": "_cloudsearch_562_FixedFooterIn",
        "FixedFooterOut": "_cloudsearch_563_FixedFooterOut",
        "IncomingWebhookChangedMetadataIn": "_cloudsearch_564_IncomingWebhookChangedMetadataIn",
        "IncomingWebhookChangedMetadataOut": "_cloudsearch_565_IncomingWebhookChangedMetadataOut",
        "BroadcastSessionInfoIn": "_cloudsearch_566_BroadcastSessionInfoIn",
        "BroadcastSessionInfoOut": "_cloudsearch_567_BroadcastSessionInfoOut",
        "AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn": "_cloudsearch_568_AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut": "_cloudsearch_569_AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut",
        "SigningKeyPossessorProtoIn": "_cloudsearch_570_SigningKeyPossessorProtoIn",
        "SigningKeyPossessorProtoOut": "_cloudsearch_571_SigningKeyPossessorProtoOut",
        "AppsDynamiteStorageCardCardHeaderIn": "_cloudsearch_572_AppsDynamiteStorageCardCardHeaderIn",
        "AppsDynamiteStorageCardCardHeaderOut": "_cloudsearch_573_AppsDynamiteStorageCardCardHeaderOut",
        "PeopleSuggestionIn": "_cloudsearch_574_PeopleSuggestionIn",
        "PeopleSuggestionOut": "_cloudsearch_575_PeopleSuggestionOut",
        "LinkDataIn": "_cloudsearch_576_LinkDataIn",
        "LinkDataOut": "_cloudsearch_577_LinkDataOut",
        "AppsDynamiteSharedTasksMessageIntegrationPayloadIn": "_cloudsearch_578_AppsDynamiteSharedTasksMessageIntegrationPayloadIn",
        "AppsDynamiteSharedTasksMessageIntegrationPayloadOut": "_cloudsearch_579_AppsDynamiteSharedTasksMessageIntegrationPayloadOut",
        "CollaborationIn": "_cloudsearch_580_CollaborationIn",
        "CollaborationOut": "_cloudsearch_581_CollaborationOut",
        "DoubleValuesIn": "_cloudsearch_582_DoubleValuesIn",
        "DoubleValuesOut": "_cloudsearch_583_DoubleValuesOut",
        "TaskActionMarkupIn": "_cloudsearch_584_TaskActionMarkupIn",
        "TaskActionMarkupOut": "_cloudsearch_585_TaskActionMarkupOut",
        "IntegerOperatorOptionsIn": "_cloudsearch_586_IntegerOperatorOptionsIn",
        "IntegerOperatorOptionsOut": "_cloudsearch_587_IntegerOperatorOptionsOut",
        "StartUploadItemRequestIn": "_cloudsearch_588_StartUploadItemRequestIn",
        "StartUploadItemRequestOut": "_cloudsearch_589_StartUploadItemRequestOut",
        "ReadReceiptsSettingsUpdatedMetadataIn": "_cloudsearch_590_ReadReceiptsSettingsUpdatedMetadataIn",
        "ReadReceiptsSettingsUpdatedMetadataOut": "_cloudsearch_591_ReadReceiptsSettingsUpdatedMetadataOut",
        "BotResponseIn": "_cloudsearch_592_BotResponseIn",
        "BotResponseOut": "_cloudsearch_593_BotResponseOut",
        "ValueFilterIn": "_cloudsearch_594_ValueFilterIn",
        "ValueFilterOut": "_cloudsearch_595_ValueFilterOut",
        "GoogleDocsResultInfoIn": "_cloudsearch_596_GoogleDocsResultInfoIn",
        "GoogleDocsResultInfoOut": "_cloudsearch_597_GoogleDocsResultInfoOut",
        "AppsDynamiteStorageOpenLinkAppUriIntentIn": "_cloudsearch_598_AppsDynamiteStorageOpenLinkAppUriIntentIn",
        "AppsDynamiteStorageOpenLinkAppUriIntentOut": "_cloudsearch_599_AppsDynamiteStorageOpenLinkAppUriIntentOut",
        "StructuredResultIn": "_cloudsearch_600_StructuredResultIn",
        "StructuredResultOut": "_cloudsearch_601_StructuredResultOut",
        "AddonComposeUiActionMarkupIn": "_cloudsearch_602_AddonComposeUiActionMarkupIn",
        "AddonComposeUiActionMarkupOut": "_cloudsearch_603_AddonComposeUiActionMarkupOut",
        "ResultCountsIn": "_cloudsearch_604_ResultCountsIn",
        "ResultCountsOut": "_cloudsearch_605_ResultCountsOut",
        "SelectionItemIn": "_cloudsearch_606_SelectionItemIn",
        "SelectionItemOut": "_cloudsearch_607_SelectionItemOut",
        "DynamiteMessagesScoringInfoIn": "_cloudsearch_608_DynamiteMessagesScoringInfoIn",
        "DynamiteMessagesScoringInfoOut": "_cloudsearch_609_DynamiteMessagesScoringInfoOut",
        "DateIn": "_cloudsearch_610_DateIn",
        "DateOut": "_cloudsearch_611_DateOut",
        "YoutubeMetadataIn": "_cloudsearch_612_YoutubeMetadataIn",
        "YoutubeMetadataOut": "_cloudsearch_613_YoutubeMetadataOut",
        "AppsDynamiteStorageColumnsColumnIn": "_cloudsearch_614_AppsDynamiteStorageColumnsColumnIn",
        "AppsDynamiteStorageColumnsColumnOut": "_cloudsearch_615_AppsDynamiteStorageColumnsColumnOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn": "_cloudsearch_616_AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut": "_cloudsearch_617_AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut",
        "PrefUpdateIn": "_cloudsearch_618_PrefUpdateIn",
        "PrefUpdateOut": "_cloudsearch_619_PrefUpdateOut",
        "LabelUpdateIn": "_cloudsearch_620_LabelUpdateIn",
        "LabelUpdateOut": "_cloudsearch_621_LabelUpdateOut",
        "DriveClientActionMarkupIn": "_cloudsearch_622_DriveClientActionMarkupIn",
        "DriveClientActionMarkupOut": "_cloudsearch_623_DriveClientActionMarkupOut",
        "InviteeInfoIn": "_cloudsearch_624_InviteeInfoIn",
        "InviteeInfoOut": "_cloudsearch_625_InviteeInfoOut",
        "IntegerPropertyOptionsIn": "_cloudsearch_626_IntegerPropertyOptionsIn",
        "IntegerPropertyOptionsOut": "_cloudsearch_627_IntegerPropertyOptionsOut",
        "AppsDynamiteSharedAppProfileIn": "_cloudsearch_628_AppsDynamiteSharedAppProfileIn",
        "AppsDynamiteSharedAppProfileOut": "_cloudsearch_629_AppsDynamiteSharedAppProfileOut",
        "AppsDynamiteSharedFindDocumentSuggestionIn": "_cloudsearch_630_AppsDynamiteSharedFindDocumentSuggestionIn",
        "AppsDynamiteSharedFindDocumentSuggestionOut": "_cloudsearch_631_AppsDynamiteSharedFindDocumentSuggestionOut",
        "AppsDynamiteSharedAssistantSessionContextIn": "_cloudsearch_632_AppsDynamiteSharedAssistantSessionContextIn",
        "AppsDynamiteSharedAssistantSessionContextOut": "_cloudsearch_633_AppsDynamiteSharedAssistantSessionContextOut",
        "AppsDynamiteSharedMessageComponentSearchInfoIn": "_cloudsearch_634_AppsDynamiteSharedMessageComponentSearchInfoIn",
        "AppsDynamiteSharedMessageComponentSearchInfoOut": "_cloudsearch_635_AppsDynamiteSharedMessageComponentSearchInfoOut",
        "DriveTimeSpanRestrictIn": "_cloudsearch_636_DriveTimeSpanRestrictIn",
        "DriveTimeSpanRestrictOut": "_cloudsearch_637_DriveTimeSpanRestrictOut",
        "SocialCommonAttachmentAttachmentIn": "_cloudsearch_638_SocialCommonAttachmentAttachmentIn",
        "SocialCommonAttachmentAttachmentOut": "_cloudsearch_639_SocialCommonAttachmentAttachmentOut",
        "FilterDeletedIn": "_cloudsearch_640_FilterDeletedIn",
        "FilterDeletedOut": "_cloudsearch_641_FilterDeletedOut",
        "SourceIn": "_cloudsearch_642_SourceIn",
        "SourceOut": "_cloudsearch_643_SourceOut",
        "AppsDynamiteStorageImageCropStyleIn": "_cloudsearch_644_AppsDynamiteStorageImageCropStyleIn",
        "AppsDynamiteStorageImageCropStyleOut": "_cloudsearch_645_AppsDynamiteStorageImageCropStyleOut",
        "GetSearchApplicationUserStatsResponseIn": "_cloudsearch_646_GetSearchApplicationUserStatsResponseIn",
        "GetSearchApplicationUserStatsResponseOut": "_cloudsearch_647_GetSearchApplicationUserStatsResponseOut",
        "TombstoneMetadataIn": "_cloudsearch_648_TombstoneMetadataIn",
        "TombstoneMetadataOut": "_cloudsearch_649_TombstoneMetadataOut",
        "SearchApplicationIn": "_cloudsearch_650_SearchApplicationIn",
        "SearchApplicationOut": "_cloudsearch_651_SearchApplicationOut",
        "FilterCreatedIn": "_cloudsearch_652_FilterCreatedIn",
        "FilterCreatedOut": "_cloudsearch_653_FilterCreatedOut",
        "StreamViewerStatsIn": "_cloudsearch_654_StreamViewerStatsIn",
        "StreamViewerStatsOut": "_cloudsearch_655_StreamViewerStatsOut",
        "ErrorMessageIn": "_cloudsearch_656_ErrorMessageIn",
        "ErrorMessageOut": "_cloudsearch_657_ErrorMessageOut",
        "LdapUserProtoIn": "_cloudsearch_658_LdapUserProtoIn",
        "LdapUserProtoOut": "_cloudsearch_659_LdapUserProtoOut",
        "AppsDynamiteSharedTextSegmentIn": "_cloudsearch_660_AppsDynamiteSharedTextSegmentIn",
        "AppsDynamiteSharedTextSegmentOut": "_cloudsearch_661_AppsDynamiteSharedTextSegmentOut",
        "PrincipalIn": "_cloudsearch_662_PrincipalIn",
        "PrincipalOut": "_cloudsearch_663_PrincipalOut",
        "OnClickIn": "_cloudsearch_664_OnClickIn",
        "OnClickOut": "_cloudsearch_665_OnClickOut",
        "IdIn": "_cloudsearch_666_IdIn",
        "IdOut": "_cloudsearch_667_IdOut",
        "UploadMetadataIn": "_cloudsearch_668_UploadMetadataIn",
        "UploadMetadataOut": "_cloudsearch_669_UploadMetadataOut",
        "CommunalLabelTagIn": "_cloudsearch_670_CommunalLabelTagIn",
        "CommunalLabelTagOut": "_cloudsearch_671_CommunalLabelTagOut",
        "AppsDynamiteSharedReactionIn": "_cloudsearch_672_AppsDynamiteSharedReactionIn",
        "AppsDynamiteSharedReactionOut": "_cloudsearch_673_AppsDynamiteSharedReactionOut",
        "ItemMetadataIn": "_cloudsearch_674_ItemMetadataIn",
        "ItemMetadataOut": "_cloudsearch_675_ItemMetadataOut",
        "AppsDynamiteSharedTasksAnnotationDataIn": "_cloudsearch_676_AppsDynamiteSharedTasksAnnotationDataIn",
        "AppsDynamiteSharedTasksAnnotationDataOut": "_cloudsearch_677_AppsDynamiteSharedTasksAnnotationDataOut",
        "FolderIn": "_cloudsearch_678_FolderIn",
        "FolderOut": "_cloudsearch_679_FolderOut",
        "AttachmentIn": "_cloudsearch_680_AttachmentIn",
        "AttachmentOut": "_cloudsearch_681_AttachmentOut",
        "UnreserveItemsRequestIn": "_cloudsearch_682_UnreserveItemsRequestIn",
        "UnreserveItemsRequestOut": "_cloudsearch_683_UnreserveItemsRequestOut",
        "GatewaySipAccessIn": "_cloudsearch_684_GatewaySipAccessIn",
        "GatewaySipAccessOut": "_cloudsearch_685_GatewaySipAccessOut",
        "UpdateDraftActionMarkupIn": "_cloudsearch_686_UpdateDraftActionMarkupIn",
        "UpdateDraftActionMarkupOut": "_cloudsearch_687_UpdateDraftActionMarkupOut",
        "BotInfoIn": "_cloudsearch_688_BotInfoIn",
        "BotInfoOut": "_cloudsearch_689_BotInfoOut",
        "SquareProtoIn": "_cloudsearch_690_SquareProtoIn",
        "SquareProtoOut": "_cloudsearch_691_SquareProtoOut",
        "AppsDynamiteSharedAssistantFeedbackContextIn": "_cloudsearch_692_AppsDynamiteSharedAssistantFeedbackContextIn",
        "AppsDynamiteSharedAssistantFeedbackContextOut": "_cloudsearch_693_AppsDynamiteSharedAssistantFeedbackContextOut",
        "DeleteQueueItemsRequestIn": "_cloudsearch_694_DeleteQueueItemsRequestIn",
        "DeleteQueueItemsRequestOut": "_cloudsearch_695_DeleteQueueItemsRequestOut",
        "DocumentInfoIn": "_cloudsearch_696_DocumentInfoIn",
        "DocumentInfoOut": "_cloudsearch_697_DocumentInfoOut",
        "TransactionContextIn": "_cloudsearch_698_TransactionContextIn",
        "TransactionContextOut": "_cloudsearch_699_TransactionContextOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn": "_cloudsearch_700_AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut": "_cloudsearch_701_AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut",
        "ItemStructuredDataIn": "_cloudsearch_702_ItemStructuredDataIn",
        "ItemStructuredDataOut": "_cloudsearch_703_ItemStructuredDataOut",
        "TimestampOperatorOptionsIn": "_cloudsearch_704_TimestampOperatorOptionsIn",
        "TimestampOperatorOptionsOut": "_cloudsearch_705_TimestampOperatorOptionsOut",
        "ImapsyncFolderAttributeFolderMessageIn": "_cloudsearch_706_ImapsyncFolderAttributeFolderMessageIn",
        "ImapsyncFolderAttributeFolderMessageOut": "_cloudsearch_707_ImapsyncFolderAttributeFolderMessageOut",
        "MessageSetIn": "_cloudsearch_708_MessageSetIn",
        "MessageSetOut": "_cloudsearch_709_MessageSetOut",
        "StatusIn": "_cloudsearch_710_StatusIn",
        "StatusOut": "_cloudsearch_711_StatusOut",
        "BroadcastAccessIn": "_cloudsearch_712_BroadcastAccessIn",
        "BroadcastAccessOut": "_cloudsearch_713_BroadcastAccessOut",
        "SettingsIn": "_cloudsearch_714_SettingsIn",
        "SettingsOut": "_cloudsearch_715_SettingsOut",
        "ItemStatusIn": "_cloudsearch_716_ItemStatusIn",
        "ItemStatusOut": "_cloudsearch_717_ItemStatusOut",
        "RequestFileScopeIn": "_cloudsearch_718_RequestFileScopeIn",
        "RequestFileScopeOut": "_cloudsearch_719_RequestFileScopeOut",
        "WonderCardDeleteIn": "_cloudsearch_720_WonderCardDeleteIn",
        "WonderCardDeleteOut": "_cloudsearch_721_WonderCardDeleteOut",
        "TextKeyValueIn": "_cloudsearch_722_TextKeyValueIn",
        "TextKeyValueOut": "_cloudsearch_723_TextKeyValueOut",
        "EventProtoIn": "_cloudsearch_724_EventProtoIn",
        "EventProtoOut": "_cloudsearch_725_EventProtoOut",
        "AppsDynamiteStorageCardCardActionIn": "_cloudsearch_726_AppsDynamiteStorageCardCardActionIn",
        "AppsDynamiteStorageCardCardActionOut": "_cloudsearch_727_AppsDynamiteStorageCardCardActionOut",
        "AppsDynamiteSharedMessageIntegrationPayloadIn": "_cloudsearch_728_AppsDynamiteSharedMessageIntegrationPayloadIn",
        "AppsDynamiteSharedMessageIntegrationPayloadOut": "_cloudsearch_729_AppsDynamiteSharedMessageIntegrationPayloadOut",
        "CustomerUserStatsIn": "_cloudsearch_730_CustomerUserStatsIn",
        "CustomerUserStatsOut": "_cloudsearch_731_CustomerUserStatsOut",
        "DriveMetadataIn": "_cloudsearch_732_DriveMetadataIn",
        "DriveMetadataOut": "_cloudsearch_733_DriveMetadataOut",
        "OsVersionIn": "_cloudsearch_734_OsVersionIn",
        "OsVersionOut": "_cloudsearch_735_OsVersionOut",
        "ContentReportIn": "_cloudsearch_736_ContentReportIn",
        "ContentReportOut": "_cloudsearch_737_ContentReportOut",
        "GaiaGroupProtoIn": "_cloudsearch_738_GaiaGroupProtoIn",
        "GaiaGroupProtoOut": "_cloudsearch_739_GaiaGroupProtoOut",
        "CapTokenHolderProtoIn": "_cloudsearch_740_CapTokenHolderProtoIn",
        "CapTokenHolderProtoOut": "_cloudsearch_741_CapTokenHolderProtoOut",
        "PrefWrittenIn": "_cloudsearch_742_PrefWrittenIn",
        "PrefWrittenOut": "_cloudsearch_743_PrefWrittenOut",
        "AckInfoIn": "_cloudsearch_744_AckInfoIn",
        "AckInfoOut": "_cloudsearch_745_AckInfoOut",
        "InsertContentIn": "_cloudsearch_746_InsertContentIn",
        "InsertContentOut": "_cloudsearch_747_InsertContentOut",
        "FuseboxItemIn": "_cloudsearch_748_FuseboxItemIn",
        "FuseboxItemOut": "_cloudsearch_749_FuseboxItemOut",
        "CustomerQueryStatsIn": "_cloudsearch_750_CustomerQueryStatsIn",
        "CustomerQueryStatsOut": "_cloudsearch_751_CustomerQueryStatsOut",
        "PrivateMessageInfoIn": "_cloudsearch_752_PrivateMessageInfoIn",
        "PrivateMessageInfoOut": "_cloudsearch_753_PrivateMessageInfoOut",
        "MessageInfoIn": "_cloudsearch_754_MessageInfoIn",
        "MessageInfoOut": "_cloudsearch_755_MessageInfoOut",
        "DateTimePickerIn": "_cloudsearch_756_DateTimePickerIn",
        "DateTimePickerOut": "_cloudsearch_757_DateTimePickerOut",
        "TopicStateUpdateIn": "_cloudsearch_758_TopicStateUpdateIn",
        "TopicStateUpdateOut": "_cloudsearch_759_TopicStateUpdateOut",
        "ProcessingErrorIn": "_cloudsearch_760_ProcessingErrorIn",
        "ProcessingErrorOut": "_cloudsearch_761_ProcessingErrorOut",
        "ThreadKeySetIn": "_cloudsearch_762_ThreadKeySetIn",
        "ThreadKeySetOut": "_cloudsearch_763_ThreadKeySetOut",
        "DriveLocationRestrictIn": "_cloudsearch_764_DriveLocationRestrictIn",
        "DriveLocationRestrictOut": "_cloudsearch_765_DriveLocationRestrictOut",
        "LabelCreatedIn": "_cloudsearch_766_LabelCreatedIn",
        "LabelCreatedOut": "_cloudsearch_767_LabelCreatedOut",
        "AppsDynamiteStorageSuggestionsIn": "_cloudsearch_768_AppsDynamiteStorageSuggestionsIn",
        "AppsDynamiteStorageSuggestionsOut": "_cloudsearch_769_AppsDynamiteStorageSuggestionsOut",
        "GetCustomerQueryStatsResponseIn": "_cloudsearch_770_GetCustomerQueryStatsResponseIn",
        "GetCustomerQueryStatsResponseOut": "_cloudsearch_771_GetCustomerQueryStatsResponseOut",
        "DeliveryMediumIn": "_cloudsearch_772_DeliveryMediumIn",
        "DeliveryMediumOut": "_cloudsearch_773_DeliveryMediumOut",
        "IntegerValuesIn": "_cloudsearch_774_IntegerValuesIn",
        "IntegerValuesOut": "_cloudsearch_775_IntegerValuesOut",
        "AppsDynamiteStorageCardIn": "_cloudsearch_776_AppsDynamiteStorageCardIn",
        "AppsDynamiteStorageCardOut": "_cloudsearch_777_AppsDynamiteStorageCardOut",
        "BooleanPropertyOptionsIn": "_cloudsearch_778_BooleanPropertyOptionsIn",
        "BooleanPropertyOptionsOut": "_cloudsearch_779_BooleanPropertyOptionsOut",
        "GridIn": "_cloudsearch_780_GridIn",
        "GridOut": "_cloudsearch_781_GridOut",
        "UserInfoIn": "_cloudsearch_782_UserInfoIn",
        "UserInfoOut": "_cloudsearch_783_UserInfoOut",
        "PossiblyTrimmedModelIn": "_cloudsearch_784_PossiblyTrimmedModelIn",
        "PossiblyTrimmedModelOut": "_cloudsearch_785_PossiblyTrimmedModelOut",
        "AppsDynamiteStorageSelectionInputIn": "_cloudsearch_786_AppsDynamiteStorageSelectionInputIn",
        "AppsDynamiteStorageSelectionInputOut": "_cloudsearch_787_AppsDynamiteStorageSelectionInputOut",
        "AppsDynamiteStorageActionActionParameterIn": "_cloudsearch_788_AppsDynamiteStorageActionActionParameterIn",
        "AppsDynamiteStorageActionActionParameterOut": "_cloudsearch_789_AppsDynamiteStorageActionActionParameterOut",
        "SourceCrowdingConfigIn": "_cloudsearch_790_SourceCrowdingConfigIn",
        "SourceCrowdingConfigOut": "_cloudsearch_791_SourceCrowdingConfigOut",
        "GetSearchApplicationSessionStatsResponseIn": "_cloudsearch_792_GetSearchApplicationSessionStatsResponseIn",
        "GetSearchApplicationSessionStatsResponseOut": "_cloudsearch_793_GetSearchApplicationSessionStatsResponseOut",
        "GmailClientActionMarkupIn": "_cloudsearch_794_GmailClientActionMarkupIn",
        "GmailClientActionMarkupOut": "_cloudsearch_795_GmailClientActionMarkupOut",
        "AppsDynamiteSharedChatItemGroupInfoIn": "_cloudsearch_796_AppsDynamiteSharedChatItemGroupInfoIn",
        "AppsDynamiteSharedChatItemGroupInfoOut": "_cloudsearch_797_AppsDynamiteSharedChatItemGroupInfoOut",
        "CustomerSettingsIn": "_cloudsearch_798_CustomerSettingsIn",
        "CustomerSettingsOut": "_cloudsearch_799_CustomerSettingsOut",
        "CloudPrincipalProtoIn": "_cloudsearch_800_CloudPrincipalProtoIn",
        "CloudPrincipalProtoOut": "_cloudsearch_801_CloudPrincipalProtoOut",
        "RpcOptionsIn": "_cloudsearch_802_RpcOptionsIn",
        "RpcOptionsOut": "_cloudsearch_803_RpcOptionsOut",
        "PinnedItemIdIn": "_cloudsearch_804_PinnedItemIdIn",
        "PinnedItemIdOut": "_cloudsearch_805_PinnedItemIdOut",
        "IntegrationConfigMutationIn": "_cloudsearch_806_IntegrationConfigMutationIn",
        "IntegrationConfigMutationOut": "_cloudsearch_807_IntegrationConfigMutationOut",
        "SegmentIn": "_cloudsearch_808_SegmentIn",
        "SegmentOut": "_cloudsearch_809_SegmentOut",
        "TriggerKeyIn": "_cloudsearch_810_TriggerKeyIn",
        "TriggerKeyOut": "_cloudsearch_811_TriggerKeyOut",
        "ReactionInfoIn": "_cloudsearch_812_ReactionInfoIn",
        "ReactionInfoOut": "_cloudsearch_813_ReactionInfoOut",
        "SheetsClientActionMarkupIn": "_cloudsearch_814_SheetsClientActionMarkupIn",
        "SheetsClientActionMarkupOut": "_cloudsearch_815_SheetsClientActionMarkupOut",
        "DmIdIn": "_cloudsearch_816_DmIdIn",
        "DmIdOut": "_cloudsearch_817_DmIdOut",
        "AppsDynamiteSharedCallMetadataIn": "_cloudsearch_818_AppsDynamiteSharedCallMetadataIn",
        "AppsDynamiteSharedCallMetadataOut": "_cloudsearch_819_AppsDynamiteSharedCallMetadataOut",
        "AttributeSetIn": "_cloudsearch_820_AttributeSetIn",
        "AttributeSetOut": "_cloudsearch_821_AttributeSetOut",
        "FacetOptionsIn": "_cloudsearch_822_FacetOptionsIn",
        "FacetOptionsOut": "_cloudsearch_823_FacetOptionsOut",
        "RequiredMessageFeaturesMetadataIn": "_cloudsearch_824_RequiredMessageFeaturesMetadataIn",
        "RequiredMessageFeaturesMetadataOut": "_cloudsearch_825_RequiredMessageFeaturesMetadataOut",
        "ImapUidsReassignIn": "_cloudsearch_826_ImapUidsReassignIn",
        "ImapUidsReassignOut": "_cloudsearch_827_ImapUidsReassignOut",
        "TextButtonIn": "_cloudsearch_828_TextButtonIn",
        "TextButtonOut": "_cloudsearch_829_TextButtonOut",
        "MessageIn": "_cloudsearch_830_MessageIn",
        "MessageOut": "_cloudsearch_831_MessageOut",
        "EnumValuesIn": "_cloudsearch_832_EnumValuesIn",
        "EnumValuesOut": "_cloudsearch_833_EnumValuesOut",
        "UserMentionDataIn": "_cloudsearch_834_UserMentionDataIn",
        "UserMentionDataOut": "_cloudsearch_835_UserMentionDataOut",
        "BabelPlaceholderMetadataIn": "_cloudsearch_836_BabelPlaceholderMetadataIn",
        "BabelPlaceholderMetadataOut": "_cloudsearch_837_BabelPlaceholderMetadataOut",
        "InviteAcceptedEventIn": "_cloudsearch_838_InviteAcceptedEventIn",
        "InviteAcceptedEventOut": "_cloudsearch_839_InviteAcceptedEventOut",
        "EventAnnotationIn": "_cloudsearch_840_EventAnnotationIn",
        "EventAnnotationOut": "_cloudsearch_841_EventAnnotationOut",
        "TimestampPropertyOptionsIn": "_cloudsearch_842_TimestampPropertyOptionsIn",
        "TimestampPropertyOptionsOut": "_cloudsearch_843_TimestampPropertyOptionsOut",
        "SourceScoringConfigIn": "_cloudsearch_844_SourceScoringConfigIn",
        "SourceScoringConfigOut": "_cloudsearch_845_SourceScoringConfigOut",
        "DynamiteSpacesScoringInfoIn": "_cloudsearch_846_DynamiteSpacesScoringInfoIn",
        "DynamiteSpacesScoringInfoOut": "_cloudsearch_847_DynamiteSpacesScoringInfoOut",
        "DataSourceIn": "_cloudsearch_848_DataSourceIn",
        "DataSourceOut": "_cloudsearch_849_DataSourceOut",
        "MdbGroupProtoIn": "_cloudsearch_850_MdbGroupProtoIn",
        "MdbGroupProtoOut": "_cloudsearch_851_MdbGroupProtoOut",
        "ChatClientActionMarkupIn": "_cloudsearch_852_ChatClientActionMarkupIn",
        "ChatClientActionMarkupOut": "_cloudsearch_853_ChatClientActionMarkupOut",
        "AppsDynamiteStorageGridGridItemIn": "_cloudsearch_854_AppsDynamiteStorageGridGridItemIn",
        "AppsDynamiteStorageGridGridItemOut": "_cloudsearch_855_AppsDynamiteStorageGridGridItemOut",
        "ReferencesIn": "_cloudsearch_856_ReferencesIn",
        "ReferencesOut": "_cloudsearch_857_ReferencesOut",
        "PropertyDisplayOptionsIn": "_cloudsearch_858_PropertyDisplayOptionsIn",
        "PropertyDisplayOptionsOut": "_cloudsearch_859_PropertyDisplayOptionsOut",
        "SourceResultCountIn": "_cloudsearch_860_SourceResultCountIn",
        "SourceResultCountOut": "_cloudsearch_861_SourceResultCountOut",
        "ItemThreadIn": "_cloudsearch_862_ItemThreadIn",
        "ItemThreadOut": "_cloudsearch_863_ItemThreadOut",
        "ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn": "_cloudsearch_864_ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut": "_cloudsearch_865_ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut",
        "CircleProtoIn": "_cloudsearch_866_CircleProtoIn",
        "CircleProtoOut": "_cloudsearch_867_CircleProtoOut",
        "ImapUpdateIn": "_cloudsearch_868_ImapUpdateIn",
        "ImapUpdateOut": "_cloudsearch_869_ImapUpdateOut",
        "UpdateCcRecipientsIn": "_cloudsearch_870_UpdateCcRecipientsIn",
        "UpdateCcRecipientsOut": "_cloudsearch_871_UpdateCcRecipientsOut",
        "AppsDynamiteStorageImageComponentIn": "_cloudsearch_872_AppsDynamiteStorageImageComponentIn",
        "AppsDynamiteStorageImageComponentOut": "_cloudsearch_873_AppsDynamiteStorageImageComponentOut",
        "AppsDynamiteStorageColumnsColumnWidgetsIn": "_cloudsearch_874_AppsDynamiteStorageColumnsColumnWidgetsIn",
        "AppsDynamiteStorageColumnsColumnWidgetsOut": "_cloudsearch_875_AppsDynamiteStorageColumnsColumnWidgetsOut",
        "BabelMessagePropsIn": "_cloudsearch_876_BabelMessagePropsIn",
        "BabelMessagePropsOut": "_cloudsearch_877_BabelMessagePropsOut",
        "AppsDynamiteSharedTextSegmentsWithDescriptionIn": "_cloudsearch_878_AppsDynamiteSharedTextSegmentsWithDescriptionIn",
        "AppsDynamiteSharedTextSegmentsWithDescriptionOut": "_cloudsearch_879_AppsDynamiteSharedTextSegmentsWithDescriptionOut",
        "AppsDynamiteV1ApiCompatV1ActionIn": "_cloudsearch_880_AppsDynamiteV1ApiCompatV1ActionIn",
        "AppsDynamiteV1ApiCompatV1ActionOut": "_cloudsearch_881_AppsDynamiteV1ApiCompatV1ActionOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn": "_cloudsearch_882_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut": "_cloudsearch_883_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut",
        "ListUnmappedIdentitiesResponseIn": "_cloudsearch_884_ListUnmappedIdentitiesResponseIn",
        "ListUnmappedIdentitiesResponseOut": "_cloudsearch_885_ListUnmappedIdentitiesResponseOut",
        "UniversalPhoneAccessIn": "_cloudsearch_886_UniversalPhoneAccessIn",
        "UniversalPhoneAccessOut": "_cloudsearch_887_UniversalPhoneAccessOut",
        "LanguageConfigIn": "_cloudsearch_888_LanguageConfigIn",
        "LanguageConfigOut": "_cloudsearch_889_LanguageConfigOut",
        "ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn": "_cloudsearch_890_ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut": "_cloudsearch_891_ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut",
        "NamedPropertyIn": "_cloudsearch_892_NamedPropertyIn",
        "NamedPropertyOut": "_cloudsearch_893_NamedPropertyOut",
        "GoogleChatV1WidgetMarkupKeyValueIn": "_cloudsearch_894_GoogleChatV1WidgetMarkupKeyValueIn",
        "GoogleChatV1WidgetMarkupKeyValueOut": "_cloudsearch_895_GoogleChatV1WidgetMarkupKeyValueOut",
        "EditMetadataIn": "_cloudsearch_896_EditMetadataIn",
        "EditMetadataOut": "_cloudsearch_897_EditMetadataOut",
        "UpdateBodyIn": "_cloudsearch_898_UpdateBodyIn",
        "UpdateBodyOut": "_cloudsearch_899_UpdateBodyOut",
        "SessionEventIn": "_cloudsearch_900_SessionEventIn",
        "SessionEventOut": "_cloudsearch_901_SessionEventOut",
        "ValueIn": "_cloudsearch_902_ValueIn",
        "ValueOut": "_cloudsearch_903_ValueOut",
        "StoredParticipantIdIn": "_cloudsearch_904_StoredParticipantIdIn",
        "StoredParticipantIdOut": "_cloudsearch_905_StoredParticipantIdOut",
        "LdapGroupProtoIn": "_cloudsearch_906_LdapGroupProtoIn",
        "LdapGroupProtoOut": "_cloudsearch_907_LdapGroupProtoOut",
        "AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn": "_cloudsearch_908_AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut": "_cloudsearch_909_AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut",
        "ItemCountByStatusIn": "_cloudsearch_910_ItemCountByStatusIn",
        "ItemCountByStatusOut": "_cloudsearch_911_ItemCountByStatusOut",
        "FieldViolationIn": "_cloudsearch_912_FieldViolationIn",
        "FieldViolationOut": "_cloudsearch_913_FieldViolationOut",
        "PrefDeletedIn": "_cloudsearch_914_PrefDeletedIn",
        "PrefDeletedOut": "_cloudsearch_915_PrefDeletedOut",
        "SuggestRequestIn": "_cloudsearch_916_SuggestRequestIn",
        "SuggestRequestOut": "_cloudsearch_917_SuggestRequestOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn": "_cloudsearch_918_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut": "_cloudsearch_919_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut",
        "ImageButtonIn": "_cloudsearch_920_ImageButtonIn",
        "ImageButtonOut": "_cloudsearch_921_ImageButtonOut",
        "WhiteboardInfoIn": "_cloudsearch_922_WhiteboardInfoIn",
        "WhiteboardInfoOut": "_cloudsearch_923_WhiteboardInfoOut",
        "GoogleChatV1WidgetMarkupTextButtonIn": "_cloudsearch_924_GoogleChatV1WidgetMarkupTextButtonIn",
        "GoogleChatV1WidgetMarkupTextButtonOut": "_cloudsearch_925_GoogleChatV1WidgetMarkupTextButtonOut",
        "AutoCompleteItemIn": "_cloudsearch_926_AutoCompleteItemIn",
        "AutoCompleteItemOut": "_cloudsearch_927_AutoCompleteItemOut",
        "AppsDynamiteStorageButtonIn": "_cloudsearch_928_AppsDynamiteStorageButtonIn",
        "AppsDynamiteStorageButtonOut": "_cloudsearch_929_AppsDynamiteStorageButtonOut",
        "QuerySourceIn": "_cloudsearch_930_QuerySourceIn",
        "QuerySourceOut": "_cloudsearch_931_QuerySourceOut",
        "UploadItemRefIn": "_cloudsearch_932_UploadItemRefIn",
        "UploadItemRefOut": "_cloudsearch_933_UploadItemRefOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn": "_cloudsearch_934_AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut": "_cloudsearch_935_AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut",
        "VideoInfoIn": "_cloudsearch_936_VideoInfoIn",
        "VideoInfoOut": "_cloudsearch_937_VideoInfoOut",
        "EnumOperatorOptionsIn": "_cloudsearch_938_EnumOperatorOptionsIn",
        "EnumOperatorOptionsOut": "_cloudsearch_939_EnumOperatorOptionsOut",
        "TriggersIn": "_cloudsearch_940_TriggersIn",
        "TriggersOut": "_cloudsearch_941_TriggersOut",
        "SafeUrlProtoIn": "_cloudsearch_942_SafeUrlProtoIn",
        "SafeUrlProtoOut": "_cloudsearch_943_SafeUrlProtoOut",
        "AppsDynamiteSharedCardClickSuggestionIn": "_cloudsearch_944_AppsDynamiteSharedCardClickSuggestionIn",
        "AppsDynamiteSharedCardClickSuggestionOut": "_cloudsearch_945_AppsDynamiteSharedCardClickSuggestionOut",
        "AuditLoggingSettingsIn": "_cloudsearch_946_AuditLoggingSettingsIn",
        "AuditLoggingSettingsOut": "_cloudsearch_947_AuditLoggingSettingsOut",
        "SwitchWidgetIn": "_cloudsearch_948_SwitchWidgetIn",
        "SwitchWidgetOut": "_cloudsearch_949_SwitchWidgetOut",
        "HostProtoIn": "_cloudsearch_950_HostProtoIn",
        "HostProtoOut": "_cloudsearch_951_HostProtoOut",
        "GoogleChatV1WidgetMarkupOnClickIn": "_cloudsearch_952_GoogleChatV1WidgetMarkupOnClickIn",
        "GoogleChatV1WidgetMarkupOnClickOut": "_cloudsearch_953_GoogleChatV1WidgetMarkupOnClickOut",
        "GetDataSourceIndexStatsResponseIn": "_cloudsearch_954_GetDataSourceIndexStatsResponseIn",
        "GetDataSourceIndexStatsResponseOut": "_cloudsearch_955_GetDataSourceIndexStatsResponseOut",
        "CardCapabilityMetadataIn": "_cloudsearch_956_CardCapabilityMetadataIn",
        "CardCapabilityMetadataOut": "_cloudsearch_957_CardCapabilityMetadataOut",
        "MetalineIn": "_cloudsearch_958_MetalineIn",
        "MetalineOut": "_cloudsearch_959_MetalineOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn": "_cloudsearch_960_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut": "_cloudsearch_961_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut",
        "CompositeFilterIn": "_cloudsearch_962_CompositeFilterIn",
        "CompositeFilterOut": "_cloudsearch_963_CompositeFilterOut",
        "PersonIn": "_cloudsearch_964_PersonIn",
        "PersonOut": "_cloudsearch_965_PersonOut",
        "PackagingServiceClientIn": "_cloudsearch_966_PackagingServiceClientIn",
        "PackagingServiceClientOut": "_cloudsearch_967_PackagingServiceClientOut",
        "PropertyDefinitionIn": "_cloudsearch_968_PropertyDefinitionIn",
        "PropertyDefinitionOut": "_cloudsearch_969_PropertyDefinitionOut",
        "GoogleChatV1WidgetMarkupOpenLinkIn": "_cloudsearch_970_GoogleChatV1WidgetMarkupOpenLinkIn",
        "GoogleChatV1WidgetMarkupOpenLinkOut": "_cloudsearch_971_GoogleChatV1WidgetMarkupOpenLinkOut",
        "PersonalLabelTagIn": "_cloudsearch_972_PersonalLabelTagIn",
        "PersonalLabelTagOut": "_cloudsearch_973_PersonalLabelTagOut",
        "SessionStateInfoIn": "_cloudsearch_974_SessionStateInfoIn",
        "SessionStateInfoOut": "_cloudsearch_975_SessionStateInfoOut",
        "GetCustomerSearchApplicationStatsResponseIn": "_cloudsearch_976_GetCustomerSearchApplicationStatsResponseIn",
        "GetCustomerSearchApplicationStatsResponseOut": "_cloudsearch_977_GetCustomerSearchApplicationStatsResponseOut",
        "AppsDynamiteStorageWidgetIn": "_cloudsearch_978_AppsDynamiteStorageWidgetIn",
        "AppsDynamiteStorageWidgetOut": "_cloudsearch_979_AppsDynamiteStorageWidgetOut",
        "SearchApplicationQueryStatsIn": "_cloudsearch_980_SearchApplicationQueryStatsIn",
        "SearchApplicationQueryStatsOut": "_cloudsearch_981_SearchApplicationQueryStatsOut",
        "MenuItemIn": "_cloudsearch_982_MenuItemIn",
        "MenuItemOut": "_cloudsearch_983_MenuItemOut",
        "SectionIn": "_cloudsearch_984_SectionIn",
        "SectionOut": "_cloudsearch_985_SectionOut",
        "TextFieldIn": "_cloudsearch_986_TextFieldIn",
        "TextFieldOut": "_cloudsearch_987_TextFieldOut",
        "ZwiebackSessionProtoIn": "_cloudsearch_988_ZwiebackSessionProtoIn",
        "ZwiebackSessionProtoOut": "_cloudsearch_989_ZwiebackSessionProtoOut",
        "LabelAddedIn": "_cloudsearch_990_LabelAddedIn",
        "LabelAddedOut": "_cloudsearch_991_LabelAddedOut",
        "SearchRequestIn": "_cloudsearch_992_SearchRequestIn",
        "SearchRequestOut": "_cloudsearch_993_SearchRequestOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn": "_cloudsearch_994_AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut": "_cloudsearch_995_AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut",
        "AppsDynamiteSharedTextWithDescriptionIn": "_cloudsearch_996_AppsDynamiteSharedTextWithDescriptionIn",
        "AppsDynamiteSharedTextWithDescriptionOut": "_cloudsearch_997_AppsDynamiteSharedTextWithDescriptionOut",
        "UserIn": "_cloudsearch_998_UserIn",
        "UserOut": "_cloudsearch_999_UserOut",
        "YouTubeBroadcastSessionInfoIn": "_cloudsearch_1000_YouTubeBroadcastSessionInfoIn",
        "YouTubeBroadcastSessionInfoOut": "_cloudsearch_1001_YouTubeBroadcastSessionInfoOut",
        "MemberIdIn": "_cloudsearch_1002_MemberIdIn",
        "MemberIdOut": "_cloudsearch_1003_MemberIdOut",
        "OpenCreatedDraftActionMarkupIn": "_cloudsearch_1004_OpenCreatedDraftActionMarkupIn",
        "OpenCreatedDraftActionMarkupOut": "_cloudsearch_1005_OpenCreatedDraftActionMarkupOut",
        "ImageIn": "_cloudsearch_1006_ImageIn",
        "ImageOut": "_cloudsearch_1007_ImageOut",
        "SelectionControlIn": "_cloudsearch_1008_SelectionControlIn",
        "SelectionControlOut": "_cloudsearch_1009_SelectionControlOut",
        "TransientDataIn": "_cloudsearch_1010_TransientDataIn",
        "TransientDataOut": "_cloudsearch_1011_TransientDataOut",
        "GetSearchApplicationQueryStatsResponseIn": "_cloudsearch_1012_GetSearchApplicationQueryStatsResponseIn",
        "GetSearchApplicationQueryStatsResponseOut": "_cloudsearch_1013_GetSearchApplicationQueryStatsResponseOut",
        "ImageCropStyleIn": "_cloudsearch_1014_ImageCropStyleIn",
        "ImageCropStyleOut": "_cloudsearch_1015_ImageCropStyleOut",
        "PhoneNumberIn": "_cloudsearch_1016_PhoneNumberIn",
        "PhoneNumberOut": "_cloudsearch_1017_PhoneNumberOut",
        "MetadataIn": "_cloudsearch_1018_MetadataIn",
        "MetadataOut": "_cloudsearch_1019_MetadataOut",
        "MeetingSpaceIn": "_cloudsearch_1020_MeetingSpaceIn",
        "MeetingSpaceOut": "_cloudsearch_1021_MeetingSpaceOut",
        "GetCustomerUserStatsResponseIn": "_cloudsearch_1022_GetCustomerUserStatsResponseIn",
        "GetCustomerUserStatsResponseOut": "_cloudsearch_1023_GetCustomerUserStatsResponseOut",
        "AclInfoIn": "_cloudsearch_1024_AclInfoIn",
        "AclInfoOut": "_cloudsearch_1025_AclInfoOut",
        "EnumValuePairIn": "_cloudsearch_1026_EnumValuePairIn",
        "EnumValuePairOut": "_cloudsearch_1027_EnumValuePairOut",
        "LegacyUploadMetadataIn": "_cloudsearch_1028_LegacyUploadMetadataIn",
        "LegacyUploadMetadataOut": "_cloudsearch_1029_LegacyUploadMetadataOut",
        "MenuIn": "_cloudsearch_1030_MenuIn",
        "MenuOut": "_cloudsearch_1031_MenuOut",
        "AppsDynamiteStorageDecoratedTextSwitchControlIn": "_cloudsearch_1032_AppsDynamiteStorageDecoratedTextSwitchControlIn",
        "AppsDynamiteStorageDecoratedTextSwitchControlOut": "_cloudsearch_1033_AppsDynamiteStorageDecoratedTextSwitchControlOut",
        "OtrModificationEventIn": "_cloudsearch_1034_OtrModificationEventIn",
        "OtrModificationEventOut": "_cloudsearch_1035_OtrModificationEventOut",
        "TimestampValuesIn": "_cloudsearch_1036_TimestampValuesIn",
        "TimestampValuesOut": "_cloudsearch_1037_TimestampValuesOut",
        "AppsDynamiteStorageTextParagraphIn": "_cloudsearch_1038_AppsDynamiteStorageTextParagraphIn",
        "AppsDynamiteStorageTextParagraphOut": "_cloudsearch_1039_AppsDynamiteStorageTextParagraphOut",
        "FilterOptionsIn": "_cloudsearch_1040_FilterOptionsIn",
        "FilterOptionsOut": "_cloudsearch_1041_FilterOptionsOut",
        "AppsDynamiteStorageOpenLinkIn": "_cloudsearch_1042_AppsDynamiteStorageOpenLinkIn",
        "AppsDynamiteStorageOpenLinkOut": "_cloudsearch_1043_AppsDynamiteStorageOpenLinkOut",
        "CustomerIndexStatsIn": "_cloudsearch_1044_CustomerIndexStatsIn",
        "CustomerIndexStatsOut": "_cloudsearch_1045_CustomerIndexStatsOut",
        "QueryInterpretationConfigIn": "_cloudsearch_1046_QueryInterpretationConfigIn",
        "QueryInterpretationConfigOut": "_cloudsearch_1047_QueryInterpretationConfigOut",
        "ChatConserverDynamitePlaceholderMetadataEditMetadataIn": "_cloudsearch_1048_ChatConserverDynamitePlaceholderMetadataEditMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataEditMetadataOut": "_cloudsearch_1049_ChatConserverDynamitePlaceholderMetadataEditMetadataOut",
        "MessagePropsIn": "_cloudsearch_1050_MessagePropsIn",
        "MessagePropsOut": "_cloudsearch_1051_MessagePropsOut",
        "UpdateToRecipientsIn": "_cloudsearch_1052_UpdateToRecipientsIn",
        "UpdateToRecipientsOut": "_cloudsearch_1053_UpdateToRecipientsOut",
        "QuerySuggestionIn": "_cloudsearch_1054_QuerySuggestionIn",
        "QuerySuggestionOut": "_cloudsearch_1055_QuerySuggestionOut",
        "AppsDynamiteStorageSuggestionsSuggestionItemIn": "_cloudsearch_1056_AppsDynamiteStorageSuggestionsSuggestionItemIn",
        "AppsDynamiteStorageSuggestionsSuggestionItemOut": "_cloudsearch_1057_AppsDynamiteStorageSuggestionsSuggestionItemOut",
        "ContactGroupProtoIn": "_cloudsearch_1058_ContactGroupProtoIn",
        "ContactGroupProtoOut": "_cloudsearch_1059_ContactGroupProtoOut",
        "KeyValueIn": "_cloudsearch_1060_KeyValueIn",
        "KeyValueOut": "_cloudsearch_1061_KeyValueOut",
        "PushItemRequestIn": "_cloudsearch_1062_PushItemRequestIn",
        "PushItemRequestOut": "_cloudsearch_1063_PushItemRequestOut",
        "BooleanOperatorOptionsIn": "_cloudsearch_1064_BooleanOperatorOptionsIn",
        "BooleanOperatorOptionsOut": "_cloudsearch_1065_BooleanOperatorOptionsOut",
        "ItemPartsIn": "_cloudsearch_1066_ItemPartsIn",
        "ItemPartsOut": "_cloudsearch_1067_ItemPartsOut",
        "ResponseDebugInfoIn": "_cloudsearch_1068_ResponseDebugInfoIn",
        "ResponseDebugInfoOut": "_cloudsearch_1069_ResponseDebugInfoOut",
        "MembershipChangeEventIn": "_cloudsearch_1070_MembershipChangeEventIn",
        "MembershipChangeEventOut": "_cloudsearch_1071_MembershipChangeEventOut",
        "FilterUpdateIn": "_cloudsearch_1072_FilterUpdateIn",
        "FilterUpdateOut": "_cloudsearch_1073_FilterUpdateOut",
        "GoogleChatV1WidgetMarkupFormActionIn": "_cloudsearch_1074_GoogleChatV1WidgetMarkupFormActionIn",
        "GoogleChatV1WidgetMarkupFormActionOut": "_cloudsearch_1075_GoogleChatV1WidgetMarkupFormActionOut",
        "AppsDynamiteSharedGroupDetailsIn": "_cloudsearch_1076_AppsDynamiteSharedGroupDetailsIn",
        "AppsDynamiteSharedGroupDetailsOut": "_cloudsearch_1077_AppsDynamiteSharedGroupDetailsOut",
        "ImapsyncFolderAttributeFolderMessageFlagsIn": "_cloudsearch_1078_ImapsyncFolderAttributeFolderMessageFlagsIn",
        "ImapsyncFolderAttributeFolderMessageFlagsOut": "_cloudsearch_1079_ImapsyncFolderAttributeFolderMessageFlagsOut",
        "DeepLinkDataIn": "_cloudsearch_1080_DeepLinkDataIn",
        "DeepLinkDataOut": "_cloudsearch_1081_DeepLinkDataOut",
        "InteractionDataIn": "_cloudsearch_1082_InteractionDataIn",
        "InteractionDataOut": "_cloudsearch_1083_InteractionDataOut",
        "EmailOwnerProtoIn": "_cloudsearch_1084_EmailOwnerProtoIn",
        "EmailOwnerProtoOut": "_cloudsearch_1085_EmailOwnerProtoOut",
        "AclFixRequestIn": "_cloudsearch_1086_AclFixRequestIn",
        "AclFixRequestOut": "_cloudsearch_1087_AclFixRequestOut",
        "DisplayedPropertyIn": "_cloudsearch_1088_DisplayedPropertyIn",
        "DisplayedPropertyOut": "_cloudsearch_1089_DisplayedPropertyOut",
        "CseInfoIn": "_cloudsearch_1090_CseInfoIn",
        "CseInfoOut": "_cloudsearch_1091_CseInfoOut",
        "AppsDynamiteSharedOrganizationInfoIn": "_cloudsearch_1092_AppsDynamiteSharedOrganizationInfoIn",
        "AppsDynamiteSharedOrganizationInfoOut": "_cloudsearch_1093_AppsDynamiteSharedOrganizationInfoOut",
        "VoicePhoneNumberIn": "_cloudsearch_1094_VoicePhoneNumberIn",
        "VoicePhoneNumberOut": "_cloudsearch_1095_VoicePhoneNumberOut",
        "SnippetIn": "_cloudsearch_1096_SnippetIn",
        "SnippetOut": "_cloudsearch_1097_SnippetOut",
        "HistoryIn": "_cloudsearch_1098_HistoryIn",
        "HistoryOut": "_cloudsearch_1099_HistoryOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn": "_cloudsearch_1100_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut": "_cloudsearch_1101_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut",
        "GoogleChatV1WidgetMarkupTextParagraphIn": "_cloudsearch_1102_GoogleChatV1WidgetMarkupTextParagraphIn",
        "GoogleChatV1WidgetMarkupTextParagraphOut": "_cloudsearch_1103_GoogleChatV1WidgetMarkupTextParagraphOut",
        "FormActionIn": "_cloudsearch_1104_FormActionIn",
        "FormActionOut": "_cloudsearch_1105_FormActionOut",
        "UrlMetadataIn": "_cloudsearch_1106_UrlMetadataIn",
        "UrlMetadataOut": "_cloudsearch_1107_UrlMetadataOut",
        "HtmlOperatorOptionsIn": "_cloudsearch_1108_HtmlOperatorOptionsIn",
        "HtmlOperatorOptionsOut": "_cloudsearch_1109_HtmlOperatorOptionsOut",
        "HangoutEventIn": "_cloudsearch_1110_HangoutEventIn",
        "HangoutEventOut": "_cloudsearch_1111_HangoutEventOut",
        "SearchItemsByViewUrlRequestIn": "_cloudsearch_1112_SearchItemsByViewUrlRequestIn",
        "SearchItemsByViewUrlRequestOut": "_cloudsearch_1113_SearchItemsByViewUrlRequestOut",
        "GroupIdIn": "_cloudsearch_1114_GroupIdIn",
        "GroupIdOut": "_cloudsearch_1115_GroupIdOut",
        "GoogleChatV1WidgetMarkupIn": "_cloudsearch_1116_GoogleChatV1WidgetMarkupIn",
        "GoogleChatV1WidgetMarkupOut": "_cloudsearch_1117_GoogleChatV1WidgetMarkupOut",
        "AllAuthenticatedUsersProtoIn": "_cloudsearch_1118_AllAuthenticatedUsersProtoIn",
        "AllAuthenticatedUsersProtoOut": "_cloudsearch_1119_AllAuthenticatedUsersProtoOut",
        "RecordingEventIn": "_cloudsearch_1120_RecordingEventIn",
        "RecordingEventOut": "_cloudsearch_1121_RecordingEventOut",
        "DateValuesIn": "_cloudsearch_1122_DateValuesIn",
        "DateValuesOut": "_cloudsearch_1123_DateValuesOut",
        "AppsDynamiteSharedAssistantDebugContextIn": "_cloudsearch_1124_AppsDynamiteSharedAssistantDebugContextIn",
        "AppsDynamiteSharedAssistantDebugContextOut": "_cloudsearch_1125_AppsDynamiteSharedAssistantDebugContextOut",
        "ObjectDisplayOptionsIn": "_cloudsearch_1126_ObjectDisplayOptionsIn",
        "ObjectDisplayOptionsOut": "_cloudsearch_1127_ObjectDisplayOptionsOut",
        "AppsDynamiteSharedPhoneNumberIn": "_cloudsearch_1128_AppsDynamiteSharedPhoneNumberIn",
        "AppsDynamiteSharedPhoneNumberOut": "_cloudsearch_1129_AppsDynamiteSharedPhoneNumberOut",
        "GridItemIn": "_cloudsearch_1130_GridItemIn",
        "GridItemOut": "_cloudsearch_1131_GridItemOut",
        "OpenLinkIn": "_cloudsearch_1132_OpenLinkIn",
        "OpenLinkOut": "_cloudsearch_1133_OpenLinkOut",
        "FuseboxItemThreadMatchInfoIn": "_cloudsearch_1134_FuseboxItemThreadMatchInfoIn",
        "FuseboxItemThreadMatchInfoOut": "_cloudsearch_1135_FuseboxItemThreadMatchInfoOut",
        "GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn": "_cloudsearch_1136_GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn",
        "GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut": "_cloudsearch_1137_GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut",
        "OAuthConsumerProtoIn": "_cloudsearch_1138_OAuthConsumerProtoIn",
        "OAuthConsumerProtoOut": "_cloudsearch_1139_OAuthConsumerProtoOut",
        "ResultDebugInfoIn": "_cloudsearch_1140_ResultDebugInfoIn",
        "ResultDebugInfoOut": "_cloudsearch_1141_ResultDebugInfoOut",
        "TransactionDebugInfoIn": "_cloudsearch_1142_TransactionDebugInfoIn",
        "TransactionDebugInfoOut": "_cloudsearch_1143_TransactionDebugInfoOut",
        "QueryCountByStatusIn": "_cloudsearch_1144_QueryCountByStatusIn",
        "QueryCountByStatusOut": "_cloudsearch_1145_QueryCountByStatusOut",
        "MemberIn": "_cloudsearch_1146_MemberIn",
        "MemberOut": "_cloudsearch_1147_MemberOut",
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn": "_cloudsearch_1148_ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut": "_cloudsearch_1149_ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut",
        "LabelsIn": "_cloudsearch_1150_LabelsIn",
        "LabelsOut": "_cloudsearch_1151_LabelsOut",
        "RepositoryErrorIn": "_cloudsearch_1152_RepositoryErrorIn",
        "RepositoryErrorOut": "_cloudsearch_1153_RepositoryErrorOut",
        "ListSearchApplicationsResponseIn": "_cloudsearch_1154_ListSearchApplicationsResponseIn",
        "ListSearchApplicationsResponseOut": "_cloudsearch_1155_ListSearchApplicationsResponseOut",
        "GroupLinkSharingModificationEventIn": "_cloudsearch_1156_GroupLinkSharingModificationEventIn",
        "GroupLinkSharingModificationEventOut": "_cloudsearch_1157_GroupLinkSharingModificationEventOut",
        "DlpActionIn": "_cloudsearch_1158_DlpActionIn",
        "DlpActionOut": "_cloudsearch_1159_DlpActionOut",
        "GroupRetentionSettingsUpdatedMetaDataIn": "_cloudsearch_1160_GroupRetentionSettingsUpdatedMetaDataIn",
        "GroupRetentionSettingsUpdatedMetaDataOut": "_cloudsearch_1161_GroupRetentionSettingsUpdatedMetaDataOut",
        "RetrievalImportanceIn": "_cloudsearch_1162_RetrievalImportanceIn",
        "RetrievalImportanceOut": "_cloudsearch_1163_RetrievalImportanceOut",
        "QuotedMessageMetadataIn": "_cloudsearch_1164_QuotedMessageMetadataIn",
        "QuotedMessageMetadataOut": "_cloudsearch_1165_QuotedMessageMetadataOut",
        "LabelRemovedIn": "_cloudsearch_1166_LabelRemovedIn",
        "LabelRemovedOut": "_cloudsearch_1167_LabelRemovedOut",
        "TextParagraphIn": "_cloudsearch_1168_TextParagraphIn",
        "TextParagraphOut": "_cloudsearch_1169_TextParagraphOut",
        "AbuseReportingConfigIn": "_cloudsearch_1170_AbuseReportingConfigIn",
        "AbuseReportingConfigOut": "_cloudsearch_1171_AbuseReportingConfigOut",
        "CallSettingsIn": "_cloudsearch_1172_CallSettingsIn",
        "CallSettingsOut": "_cloudsearch_1173_CallSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MessageAddedIn"] = t.struct(
        {
            "attributeIds": t.array(t.string()),
            "syncIds": t.array(t.integer()).optional(),
            "labelIds": t.array(t.string()),
            "messageKey": t.proxy(renames["MultiKeyIn"]),
        }
    ).named(renames["MessageAddedIn"])
    types["MessageAddedOut"] = t.struct(
        {
            "attributeIds": t.array(t.string()),
            "syncIds": t.array(t.integer()).optional(),
            "labelIds": t.array(t.string()),
            "messageKey": t.proxy(renames["MultiKeyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageAddedOut"])
    types["GsuiteIntegrationMetadataIn"] = t.struct(
        {
            "assistantData": t.proxy(
                renames["AppsDynamiteSharedAssistantAnnotationDataIn"]
            ),
            "clientType": t.string(),
            "calendarEventData": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataIn"]
            ),
            "indexableTexts": t.array(t.string()).optional(),
            "tasksData": t.proxy(renames["AppsDynamiteSharedTasksAnnotationDataIn"]),
            "activityFeedData": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataIn"]
            ),
            "callData": t.proxy(
                renames["AppsDynamiteSharedCallAnnotationDataIn"]
            ).optional(),
        }
    ).named(renames["GsuiteIntegrationMetadataIn"])
    types["GsuiteIntegrationMetadataOut"] = t.struct(
        {
            "assistantData": t.proxy(
                renames["AppsDynamiteSharedAssistantAnnotationDataOut"]
            ),
            "clientType": t.string(),
            "calendarEventData": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataOut"]
            ),
            "indexableTexts": t.array(t.string()).optional(),
            "tasksData": t.proxy(renames["AppsDynamiteSharedTasksAnnotationDataOut"]),
            "activityFeedData": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataOut"]
            ),
            "callData": t.proxy(
                renames["AppsDynamiteSharedCallAnnotationDataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GsuiteIntegrationMetadataOut"])
    types["AppsDynamiteStorageDateTimePickerIn"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "label": t.string().optional(),
            "name": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "type": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageDateTimePickerIn"])
    types["AppsDynamiteStorageDateTimePickerOut"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "label": t.string().optional(),
            "name": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "type": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDateTimePickerOut"])
    types["CardHeaderIn"] = t.struct(
        {
            "title": t.string().optional(),
            "imageUrl": t.string(),
            "imageAltText": t.string().optional(),
            "imageStyle": t.string(),
            "subtitle": t.string(),
        }
    ).named(renames["CardHeaderIn"])
    types["CardHeaderOut"] = t.struct(
        {
            "title": t.string().optional(),
            "imageUrl": t.string(),
            "imageAltText": t.string().optional(),
            "imageStyle": t.string(),
            "subtitle": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardHeaderOut"])
    types["AppsDynamiteV1ApiCompatV1ActionConfirmIn"] = t.struct(
        {
            "title": t.string().optional(),
            "dismiss_text": t.string().optional(),
            "ok_text": t.string().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionConfirmIn"])
    types["AppsDynamiteV1ApiCompatV1ActionConfirmOut"] = t.struct(
        {
            "title": t.string().optional(),
            "dismiss_text": t.string().optional(),
            "ok_text": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionConfirmOut"])
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
    types["JobsettedServerSpecIn"] = t.struct(
        {"serverName": t.string().optional(), "portName": t.string().optional()}
    ).named(renames["JobsettedServerSpecIn"])
    types["JobsettedServerSpecOut"] = t.struct(
        {
            "serverName": t.string().optional(),
            "portName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobsettedServerSpecOut"])
    types["AppsDynamiteSharedAssistantSuggestionIn"] = t.struct(
        {
            "sessionContext": t.proxy(
                renames["AppsDynamiteSharedAssistantSessionContextIn"]
            ).optional(),
            "serializedSuggestions": t.string().optional(),
            "feedbackContext": t.proxy(
                renames["AppsDynamiteSharedAssistantFeedbackContextIn"]
            ).optional(),
            "debugContext": t.proxy(
                renames["AppsDynamiteSharedAssistantDebugContextIn"]
            ).optional(),
            "findDocumentSuggestion": t.proxy(
                renames["AppsDynamiteSharedFindDocumentSuggestionIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSuggestionIn"])
    types["AppsDynamiteSharedAssistantSuggestionOut"] = t.struct(
        {
            "sessionContext": t.proxy(
                renames["AppsDynamiteSharedAssistantSessionContextOut"]
            ).optional(),
            "serializedSuggestions": t.string().optional(),
            "feedbackContext": t.proxy(
                renames["AppsDynamiteSharedAssistantFeedbackContextOut"]
            ).optional(),
            "debugContext": t.proxy(
                renames["AppsDynamiteSharedAssistantDebugContextOut"]
            ).optional(),
            "findDocumentSuggestion": t.proxy(
                renames["AppsDynamiteSharedFindDocumentSuggestionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSuggestionOut"])
    types["SearchApplicationUserStatsIn"] = t.struct(
        {
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "oneDayActiveUsersCount": t.string().optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
        }
    ).named(renames["SearchApplicationUserStatsIn"])
    types["SearchApplicationUserStatsOut"] = t.struct(
        {
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "oneDayActiveUsersCount": t.string().optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationUserStatsOut"])
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
    types["WidgetMarkupIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]),
            "dateTimePicker": t.proxy(renames["DateTimePickerIn"]),
            "menu": t.proxy(renames["MenuIn"]).optional(),
            "textKeyValue": t.proxy(renames["TextKeyValueIn"]),
            "textField": t.proxy(renames["TextFieldIn"]),
            "selectionControl": t.proxy(renames["SelectionControlIn"]),
            "grid": t.proxy(renames["GridIn"]),
            "textParagraph": t.proxy(renames["TextParagraphIn"]).optional(),
            "divider": t.proxy(renames["DividerIn"]),
            "keyValue": t.proxy(renames["KeyValueIn"]),
            "imageKeyValue": t.proxy(renames["ImageKeyValueIn"]),
            "horizontalAlignment": t.string().optional(),
            "buttons": t.array(t.proxy(renames["ButtonIn"])).optional(),
        }
    ).named(renames["WidgetMarkupIn"])
    types["WidgetMarkupOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]),
            "dateTimePicker": t.proxy(renames["DateTimePickerOut"]),
            "menu": t.proxy(renames["MenuOut"]).optional(),
            "textKeyValue": t.proxy(renames["TextKeyValueOut"]),
            "textField": t.proxy(renames["TextFieldOut"]),
            "selectionControl": t.proxy(renames["SelectionControlOut"]),
            "grid": t.proxy(renames["GridOut"]),
            "textParagraph": t.proxy(renames["TextParagraphOut"]).optional(),
            "divider": t.proxy(renames["DividerOut"]),
            "keyValue": t.proxy(renames["KeyValueOut"]),
            "imageKeyValue": t.proxy(renames["ImageKeyValueOut"]),
            "horizontalAlignment": t.string().optional(),
            "buttons": t.array(t.proxy(renames["ButtonOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WidgetMarkupOut"])
    types["AppsDynamiteSharedSpaceInfoIn"] = t.struct(
        {
            "groupId": t.proxy(renames["GroupIdIn"]),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsIn"]
            ).optional(),
            "userMembershipState": t.string().optional(),
            "inviterEmail": t.string().optional(),
            "isExternal": t.boolean().optional(),
            "avatarUrl": t.string(),
            "description": t.string(),
            "name": t.string(),
            "avatarInfo": t.proxy(renames["AppsDynamiteSharedAvatarInfoIn"]),
            "numMembers": t.integer().optional(),
        }
    ).named(renames["AppsDynamiteSharedSpaceInfoIn"])
    types["AppsDynamiteSharedSpaceInfoOut"] = t.struct(
        {
            "groupId": t.proxy(renames["GroupIdOut"]),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsOut"]
            ).optional(),
            "userMembershipState": t.string().optional(),
            "inviterEmail": t.string().optional(),
            "isExternal": t.boolean().optional(),
            "avatarUrl": t.string(),
            "description": t.string(),
            "name": t.string(),
            "avatarInfo": t.proxy(renames["AppsDynamiteSharedAvatarInfoOut"]),
            "numMembers": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedSpaceInfoOut"])
    types["RecipientIn"] = t.struct({"email": t.string()}).named(renames["RecipientIn"])
    types["RecipientOut"] = t.struct(
        {"email": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RecipientOut"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut"])
    types["LabelDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelDeletedIn"]
    )
    types["LabelDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelDeletedOut"])
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
    types["RequestOptionsIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "languageCode": t.string().optional(),
            "timeZone": t.string().optional(),
            "searchApplicationId": t.string().optional(),
        }
    ).named(renames["RequestOptionsIn"])
    types["RequestOptionsOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "languageCode": t.string().optional(),
            "timeZone": t.string().optional(),
            "searchApplicationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOptionsOut"])
    types["RosterIn"] = t.struct(
        {
            "name": t.string(),
            "id": t.proxy(renames["RosterIdIn"]),
            "isMembershipVisibleToCaller": t.boolean().optional(),
            "avatarUrl": t.string(),
            "rosterGaiaKey": t.string().optional(),
            "rosterState": t.string().optional(),
            "membershipCount": t.integer(),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsIn"]
            ).optional(),
        }
    ).named(renames["RosterIn"])
    types["RosterOut"] = t.struct(
        {
            "name": t.string(),
            "id": t.proxy(renames["RosterIdOut"]),
            "isMembershipVisibleToCaller": t.boolean().optional(),
            "avatarUrl": t.string(),
            "rosterGaiaKey": t.string().optional(),
            "rosterState": t.string().optional(),
            "membershipCount": t.integer(),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RosterOut"])
    types["UserIdIn"] = t.struct(
        {
            "originAppId": t.proxy(renames["AppIdIn"]).optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "actingUserId": t.string().optional(),
        }
    ).named(renames["UserIdIn"])
    types["UserIdOut"] = t.struct(
        {
            "originAppId": t.proxy(renames["AppIdOut"]).optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "actingUserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserIdOut"])
    types["OtrChatMessageEventIn"] = t.struct(
        {
            "kansasRowId": t.string(),
            "kansasVersionInfo": t.string(),
            "messageOtrStatus": t.string(),
            "expirationTimestampUsec": t.string(),
        }
    ).named(renames["OtrChatMessageEventIn"])
    types["OtrChatMessageEventOut"] = t.struct(
        {
            "kansasRowId": t.string(),
            "kansasVersionInfo": t.string(),
            "messageOtrStatus": t.string(),
            "expirationTimestampUsec": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtrChatMessageEventOut"])
    types["TypeInfoIn"] = t.struct(
        {"videoInfo": t.proxy(renames["VideoInfoIn"]).optional()}
    ).named(renames["TypeInfoIn"])
    types["TypeInfoOut"] = t.struct(
        {
            "videoInfo": t.proxy(renames["VideoInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeInfoOut"])
    types["SimpleSecretLabelProtoIn"] = t.struct(
        {
            "capabilityId": t.integer().optional(),
            "inviteId": t.string().optional(),
            "type": t.string().optional(),
            "genericLabel": t.string().optional(),
        }
    ).named(renames["SimpleSecretLabelProtoIn"])
    types["SimpleSecretLabelProtoOut"] = t.struct(
        {
            "capabilityId": t.integer().optional(),
            "inviteId": t.string().optional(),
            "type": t.string().optional(),
            "genericLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleSecretLabelProtoOut"])
    types["NameIn"] = t.struct({"displayName": t.string().optional()}).named(
        renames["NameIn"]
    )
    types["NameOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
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
    types["AppsDynamiteStorageCardSectionIn"] = t.struct(
        {
            "header": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageWidgetIn"])
            ).optional(),
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "collapsible": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteStorageCardSectionIn"])
    types["AppsDynamiteStorageCardSectionOut"] = t.struct(
        {
            "header": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageWidgetOut"])
            ).optional(),
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "collapsible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardSectionOut"])
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
    types["WrappedResourceKeyIn"] = t.struct(
        {"resourceKey": t.string().optional()}
    ).named(renames["WrappedResourceKeyIn"])
    types["WrappedResourceKeyOut"] = t.struct(
        {
            "resourceKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WrappedResourceKeyOut"])
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
    types["CustomerIdIn"] = t.struct({"customerId": t.string()}).named(
        renames["CustomerIdIn"]
    )
    types["CustomerIdOut"] = t.struct(
        {
            "customerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerIdOut"])
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
    types["RoomUpdatedMetadataIn"] = t.struct(
        {
            "visibility": t.proxy(
                renames["AppsDynamiteSharedGroupVisibilityIn"]
            ).optional(),
            "renameMetadata": t.proxy(renames["RoomRenameMetadataIn"]),
            "groupLinkSharingEnabled": t.boolean(),
            "name": t.string().optional(),
            "initiator": t.proxy(renames["UserIn"]).optional(),
            "groupDetailsMetadata": t.proxy(renames["GroupDetailsUpdatedMetadataIn"]),
            "initiatorType": t.string().optional(),
        }
    ).named(renames["RoomUpdatedMetadataIn"])
    types["RoomUpdatedMetadataOut"] = t.struct(
        {
            "visibility": t.proxy(
                renames["AppsDynamiteSharedGroupVisibilityOut"]
            ).optional(),
            "renameMetadata": t.proxy(renames["RoomRenameMetadataOut"]),
            "groupLinkSharingEnabled": t.boolean(),
            "name": t.string().optional(),
            "initiator": t.proxy(renames["UserOut"]).optional(),
            "groupDetailsMetadata": t.proxy(renames["GroupDetailsUpdatedMetadataOut"]),
            "initiatorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoomUpdatedMetadataOut"])
    types["CallInfoIn"] = t.struct(
        {
            "presenter": t.proxy(renames["PresenterIn"]).optional(),
            "transcriptionSessionInfo": t.proxy(
                renames["TranscriptionSessionInfoIn"]
            ).optional(),
            "coActivity": t.proxy(renames["CoActivityIn"]).optional(),
            "recordingSessionInfo": t.proxy(
                renames["RecordingSessionInfoIn"]
            ).optional(),
            "youTubeBroadcastSessionInfos": t.array(
                t.proxy(renames["YouTubeBroadcastSessionInfoIn"])
            ).optional(),
            "viewerCount": t.integer().optional(),
            "broadcastSessionInfo": t.proxy(
                renames["BroadcastSessionInfoIn"]
            ).optional(),
            "collaboration": t.proxy(renames["CollaborationIn"]).optional(),
            "abuseReportingConfig": t.proxy(
                renames["AbuseReportingConfigIn"]
            ).optional(),
            "settings": t.proxy(renames["CallSettingsIn"]).optional(),
            "paygateInfo": t.proxy(renames["PaygateInfoIn"]).optional(),
            "cseInfo": t.proxy(renames["CseInfoIn"]).optional(),
            "availableAccessTypes": t.array(t.string()).optional(),
            "recordingInfo": t.proxy(renames["RecordingInfoIn"]).optional(),
        }
    ).named(renames["CallInfoIn"])
    types["CallInfoOut"] = t.struct(
        {
            "presenter": t.proxy(renames["PresenterOut"]).optional(),
            "transcriptionSessionInfo": t.proxy(
                renames["TranscriptionSessionInfoOut"]
            ).optional(),
            "coActivity": t.proxy(renames["CoActivityOut"]).optional(),
            "recordingSessionInfo": t.proxy(
                renames["RecordingSessionInfoOut"]
            ).optional(),
            "youTubeBroadcastSessionInfos": t.array(
                t.proxy(renames["YouTubeBroadcastSessionInfoOut"])
            ).optional(),
            "streamingSessions": t.array(
                t.proxy(renames["StreamingSessionInfoOut"])
            ).optional(),
            "viewerCount": t.integer().optional(),
            "broadcastSessionInfo": t.proxy(
                renames["BroadcastSessionInfoOut"]
            ).optional(),
            "collaboration": t.proxy(renames["CollaborationOut"]).optional(),
            "abuseReportingConfig": t.proxy(
                renames["AbuseReportingConfigOut"]
            ).optional(),
            "attachedDocuments": t.array(
                t.proxy(renames["DocumentInfoOut"])
            ).optional(),
            "calendarEventId": t.string().optional(),
            "settings": t.proxy(renames["CallSettingsOut"]).optional(),
            "availableReactions": t.array(
                t.proxy(renames["ReactionInfoOut"])
            ).optional(),
            "organizationName": t.string().optional(),
            "paygateInfo": t.proxy(renames["PaygateInfoOut"]).optional(),
            "cseInfo": t.proxy(renames["CseInfoOut"]).optional(),
            "availableAccessTypes": t.array(t.string()).optional(),
            "artifactOwner": t.proxy(renames["UserDisplayInfoOut"]).optional(),
            "recordingInfo": t.proxy(renames["RecordingInfoOut"]).optional(),
            "maxJoinedDevices": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CallInfoOut"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn"] = t.struct(
        {
            "updaterCountToShow": t.integer().optional(),
            "updaterCountDisplayType": t.string().optional(),
            "updaterToShow": t.proxy(renames["UserIdIn"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut"] = t.struct(
        {
            "updaterCountToShow": t.integer().optional(),
            "updaterCountDisplayType": t.string().optional(),
            "updaterToShow": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn"
    ] = t.struct(
        {
            "pin": t.string().optional(),
            "passcode": t.string().optional(),
            "uri": t.string().optional(),
            "password": t.string().optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "regionCode": t.string().optional(),
            "accessCode": t.string().optional(),
            "meetingCode": t.string().optional(),
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
            "pin": t.string().optional(),
            "passcode": t.string().optional(),
            "uri": t.string().optional(),
            "password": t.string().optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "regionCode": t.string().optional(),
            "accessCode": t.string().optional(),
            "meetingCode": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut"
        ]
    )
    types["MembershipChangedMetadataIn"] = t.struct(
        {
            "affectedMembers": t.array(t.proxy(renames["MemberIdIn"])).optional(),
            "initiatorProfile": t.proxy(renames["UserIn"]).optional(),
            "initiatorType": t.string().optional(),
            "affectedMemberships": t.array(t.proxy(renames["AffectedMembershipIn"])),
            "affectedMemberProfiles": t.array(t.proxy(renames["MemberIn"])),
            "initiator": t.proxy(renames["UserIdIn"]).optional(),
            "type": t.string(),
        }
    ).named(renames["MembershipChangedMetadataIn"])
    types["MembershipChangedMetadataOut"] = t.struct(
        {
            "affectedMembers": t.array(t.proxy(renames["MemberIdOut"])).optional(),
            "initiatorProfile": t.proxy(renames["UserOut"]).optional(),
            "initiatorType": t.string().optional(),
            "affectedMemberships": t.array(t.proxy(renames["AffectedMembershipOut"])),
            "affectedMemberProfiles": t.array(t.proxy(renames["MemberOut"])),
            "initiator": t.proxy(renames["UserIdOut"]).optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipChangedMetadataOut"])
    types["PostiniUserProtoIn"] = t.struct({"postiniUserId": t.string()}).named(
        renames["PostiniUserProtoIn"]
    )
    types["PostiniUserProtoOut"] = t.struct(
        {
            "postiniUserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostiniUserProtoOut"])
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
    types["CustomEmojiMetadataIn"] = t.struct(
        {"customEmoji": t.proxy(renames["AppsDynamiteSharedCustomEmojiIn"])}
    ).named(renames["CustomEmojiMetadataIn"])
    types["CustomEmojiMetadataOut"] = t.struct(
        {
            "customEmoji": t.proxy(renames["AppsDynamiteSharedCustomEmojiOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomEmojiMetadataOut"])
    types["SpellResultIn"] = t.struct({"suggestedQuery": t.string().optional()}).named(
        renames["SpellResultIn"]
    )
    types["SpellResultOut"] = t.struct(
        {
            "suggestedQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpellResultOut"])
    types["RequestFileScopeForActiveDocumentIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestFileScopeForActiveDocumentIn"])
    types["RequestFileScopeForActiveDocumentOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestFileScopeForActiveDocumentOut"])
    types["VideoCallMetadataIn"] = t.struct(
        {
            "meetingSpace": t.proxy(renames["MeetingSpaceIn"]).optional(),
            "shouldNotRender": t.boolean().optional(),
            "wasCreatedInCurrentGroup": t.boolean().optional(),
        }
    ).named(renames["VideoCallMetadataIn"])
    types["VideoCallMetadataOut"] = t.struct(
        {
            "meetingSpace": t.proxy(renames["MeetingSpaceOut"]).optional(),
            "shouldNotRender": t.boolean().optional(),
            "wasCreatedInCurrentGroup": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCallMetadataOut"])
    types["AppsDynamiteStorageOnClickIn"] = t.struct(
        {
            "hostAppAction": t.proxy(renames["HostAppActionMarkupIn"]).optional(),
            "action": t.proxy(renames["AppsDynamiteStorageActionIn"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "openLink": t.proxy(renames["AppsDynamiteStorageOpenLinkIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOnClickIn"])
    types["AppsDynamiteStorageOnClickOut"] = t.struct(
        {
            "hostAppAction": t.proxy(renames["HostAppActionMarkupOut"]).optional(),
            "action": t.proxy(renames["AppsDynamiteStorageActionOut"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "openLink": t.proxy(renames["AppsDynamiteStorageOpenLinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOnClickOut"])
    types["UnmappedIdentityIn"] = t.struct(
        {
            "externalIdentity": t.proxy(renames["PrincipalIn"]).optional(),
            "resolutionStatusCode": t.string().optional(),
        }
    ).named(renames["UnmappedIdentityIn"])
    types["UnmappedIdentityOut"] = t.struct(
        {
            "externalIdentity": t.proxy(renames["PrincipalOut"]).optional(),
            "resolutionStatusCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmappedIdentityOut"])
    types["AppsDynamiteStorageMaterialIconIn"] = t.struct(
        {
            "weight": t.integer().optional(),
            "fill": t.boolean().optional(),
            "grade": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageMaterialIconIn"])
    types["AppsDynamiteStorageMaterialIconOut"] = t.struct(
        {
            "weight": t.integer().optional(),
            "fill": t.boolean().optional(),
            "grade": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageMaterialIconOut"])
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
    types["MessageDeletedIn"] = t.struct(
        {
            "imapSyncMappings": t.array(
                t.proxy(renames["ImapSyncDeleteIn"])
            ).optional(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
            "wonderCardMappings": t.array(
                t.proxy(renames["WonderCardDeleteIn"])
            ).optional(),
        }
    ).named(renames["MessageDeletedIn"])
    types["MessageDeletedOut"] = t.struct(
        {
            "imapSyncMappings": t.array(
                t.proxy(renames["ImapSyncDeleteOut"])
            ).optional(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "wonderCardMappings": t.array(
                t.proxy(renames["WonderCardDeleteOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageDeletedOut"])
    types["ButtonIn"] = t.struct(
        {
            "imageButton": t.proxy(renames["ImageButtonIn"]),
            "textButton": t.proxy(renames["TextButtonIn"]),
        }
    ).named(renames["ButtonIn"])
    types["ButtonOut"] = t.struct(
        {
            "imageButton": t.proxy(renames["ImageButtonOut"]),
            "textButton": t.proxy(renames["TextButtonOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ButtonOut"])
    types["AppsDynamiteStorageColumnsIn"] = t.struct(
        {
            "columnItems": t.array(
                t.proxy(renames["AppsDynamiteStorageColumnsColumnIn"])
            ).optional(),
            "wrapStyle": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsIn"])
    types["AppsDynamiteStorageColumnsOut"] = t.struct(
        {
            "columnItems": t.array(
                t.proxy(renames["AppsDynamiteStorageColumnsColumnOut"])
            ).optional(),
            "wrapStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsOut"])
    types["IntegerFacetingOptionsIn"] = t.struct(
        {"integerBuckets": t.array(t.string()).optional()}
    ).named(renames["IntegerFacetingOptionsIn"])
    types["IntegerFacetingOptionsOut"] = t.struct(
        {
            "integerBuckets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerFacetingOptionsOut"])
    types["UserMentionMetadataIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "inviteeInfo": t.proxy(renames["InviteeInfoIn"]).optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
            "type": t.string(),
            "gender": t.string().optional(),
            "userMentionError": t.string().optional(),
        }
    ).named(renames["UserMentionMetadataIn"])
    types["UserMentionMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "inviteeInfo": t.proxy(renames["InviteeInfoOut"]).optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "type": t.string(),
            "gender": t.string().optional(),
            "userMentionError": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserMentionMetadataOut"])
    types["ToolbarIn"] = t.struct(
        {"name": t.string(), "iconUrl": t.string(), "color": t.string().optional()}
    ).named(renames["ToolbarIn"])
    types["ToolbarOut"] = t.struct(
        {
            "name": t.string(),
            "iconUrl": t.string(),
            "color": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolbarOut"])
    types["RbacSubjectProtoIn"] = t.struct({"username": t.string().optional()}).named(
        renames["RbacSubjectProtoIn"]
    )
    types["RbacSubjectProtoOut"] = t.struct(
        {
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RbacSubjectProtoOut"])
    types["SlashCommandMetadataIn"] = t.struct(
        {
            "type": t.string(),
            "argumentsHint": t.string().optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
            "triggersDialog": t.boolean().optional(),
            "commandName": t.string().optional(),
            "commandId": t.string().optional(),
        }
    ).named(renames["SlashCommandMetadataIn"])
    types["SlashCommandMetadataOut"] = t.struct(
        {
            "type": t.string(),
            "argumentsHint": t.string().optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "triggersDialog": t.boolean().optional(),
            "commandName": t.string().optional(),
            "commandId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandMetadataOut"])
    types["UserDisplayInfoIn"] = t.struct(
        {"displayName": t.string().optional(), "avatarUrl": t.string().optional()}
    ).named(renames["UserDisplayInfoIn"])
    types["UserDisplayInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "avatarUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDisplayInfoOut"])
    types["ItemIn"] = t.struct(
        {
            "version": t.string(),
            "status": t.proxy(renames["ItemStatusIn"]).optional(),
            "acl": t.proxy(renames["ItemAclIn"]).optional(),
            "queue": t.string().optional(),
            "payload": t.string().optional(),
            "itemType": t.string().optional(),
            "content": t.proxy(renames["ItemContentIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.proxy(renames["ItemMetadataIn"]).optional(),
            "structuredData": t.proxy(renames["ItemStructuredDataIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "version": t.string(),
            "status": t.proxy(renames["ItemStatusOut"]).optional(),
            "acl": t.proxy(renames["ItemAclOut"]).optional(),
            "queue": t.string().optional(),
            "payload": t.string().optional(),
            "itemType": t.string().optional(),
            "content": t.proxy(renames["ItemContentOut"]).optional(),
            "name": t.string().optional(),
            "metadata": t.proxy(renames["ItemMetadataOut"]).optional(),
            "structuredData": t.proxy(renames["ItemStructuredDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["ThreadUpdateIn"] = t.struct(
        {
            "threadLocator": t.string().optional(),
            "attributeRemoved": t.proxy(renames["AttributeRemovedIn"]),
            "preState": t.array(t.proxy(renames["PreStateIn"])).optional(),
            "labelAdded": t.proxy(renames["LabelAddedIn"]),
            "originalThreadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "messageDeleted": t.proxy(renames["MessageDeletedIn"]),
            "lastHistoryRecordId": t.string().optional(),
            "threadKeySet": t.proxy(renames["ThreadKeySetIn"]),
            "messageAdded": t.proxy(renames["MessageAddedIn"]),
            "labelRemoved": t.proxy(renames["LabelRemovedIn"]),
            "attributeSet": t.proxy(renames["AttributeSetIn"]),
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "topicStateUpdate": t.proxy(renames["TopicStateUpdateIn"]),
        }
    ).named(renames["ThreadUpdateIn"])
    types["ThreadUpdateOut"] = t.struct(
        {
            "threadLocator": t.string().optional(),
            "attributeRemoved": t.proxy(renames["AttributeRemovedOut"]),
            "preState": t.array(t.proxy(renames["PreStateOut"])).optional(),
            "labelAdded": t.proxy(renames["LabelAddedOut"]),
            "originalThreadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "messageDeleted": t.proxy(renames["MessageDeletedOut"]),
            "lastHistoryRecordId": t.string().optional(),
            "threadKeySet": t.proxy(renames["ThreadKeySetOut"]),
            "messageAdded": t.proxy(renames["MessageAddedOut"]),
            "labelRemoved": t.proxy(renames["LabelRemovedOut"]),
            "attributeSet": t.proxy(renames["AttributeSetOut"]),
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "topicStateUpdate": t.proxy(renames["TopicStateUpdateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThreadUpdateOut"])
    types["StructuredDataObjectIn"] = t.struct(
        {"properties": t.array(t.proxy(renames["NamedPropertyIn"])).optional()}
    ).named(renames["StructuredDataObjectIn"])
    types["StructuredDataObjectOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["NamedPropertyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredDataObjectOut"])
    types["ObjectDefinitionIn"] = t.struct(
        {
            "propertyDefinitions": t.array(
                t.proxy(renames["PropertyDefinitionIn"])
            ).optional(),
            "name": t.string().optional(),
            "options": t.proxy(renames["ObjectOptionsIn"]).optional(),
        }
    ).named(renames["ObjectDefinitionIn"])
    types["ObjectDefinitionOut"] = t.struct(
        {
            "propertyDefinitions": t.array(
                t.proxy(renames["PropertyDefinitionOut"])
            ).optional(),
            "name": t.string().optional(),
            "options": t.proxy(renames["ObjectOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectDefinitionOut"])
    types["FacetResultIn"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["FacetBucketIn"])).optional(),
            "operatorName": t.string().optional(),
            "sourceName": t.string().optional(),
            "objectType": t.string().optional(),
        }
    ).named(renames["FacetResultIn"])
    types["FacetResultOut"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["FacetBucketOut"])).optional(),
            "operatorName": t.string().optional(),
            "sourceName": t.string().optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetResultOut"])
    types["FormattingIn"] = t.struct(
        {
            "underline": t.boolean(),
            "italics": t.boolean(),
            "highlight": t.boolean().optional(),
            "bold": t.boolean(),
            "style": t.string().optional(),
            "strikethrough": t.boolean(),
        }
    ).named(renames["FormattingIn"])
    types["FormattingOut"] = t.struct(
        {
            "underline": t.boolean(),
            "italics": t.boolean(),
            "highlight": t.boolean().optional(),
            "bold": t.boolean(),
            "style": t.string().optional(),
            "strikethrough": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormattingOut"])
    types["GoogleChatV1WidgetMarkupImageIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "aspectRatio": t.number().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageIn"])
    types["GoogleChatV1WidgetMarkupImageOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "aspectRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageOut"])
    types["RestrictItemIn"] = t.struct(
        {
            "driveMimeTypeRestrict": t.proxy(
                renames["DriveMimeTypeRestrictIn"]
            ).optional(),
            "driveFollowUpRestrict": t.proxy(renames["DriveFollowUpRestrictIn"]),
            "driveLocationRestrict": t.proxy(renames["DriveLocationRestrictIn"]),
            "driveTimeSpanRestrict": t.proxy(renames["DriveTimeSpanRestrictIn"]),
            "searchOperator": t.string().optional(),
        }
    ).named(renames["RestrictItemIn"])
    types["RestrictItemOut"] = t.struct(
        {
            "driveMimeTypeRestrict": t.proxy(
                renames["DriveMimeTypeRestrictOut"]
            ).optional(),
            "driveFollowUpRestrict": t.proxy(renames["DriveFollowUpRestrictOut"]),
            "driveLocationRestrict": t.proxy(renames["DriveLocationRestrictOut"]),
            "driveTimeSpanRestrict": t.proxy(renames["DriveTimeSpanRestrictOut"]),
            "searchOperator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictItemOut"])
    types["FuseboxPrefUpdatePreStateIn"] = t.struct({"value": t.string()}).named(
        renames["FuseboxPrefUpdatePreStateIn"]
    )
    types["FuseboxPrefUpdatePreStateOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FuseboxPrefUpdatePreStateOut"])
    types["DriveMimeTypeRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveMimeTypeRestrictIn"]
    )
    types["DriveMimeTypeRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveMimeTypeRestrictOut"])
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
    types["BorderStyleIn"] = t.struct(
        {
            "cornerRadius": t.integer().optional(),
            "type": t.string().optional(),
            "strokeColor": t.string().optional(),
        }
    ).named(renames["BorderStyleIn"])
    types["BorderStyleOut"] = t.struct(
        {
            "cornerRadius": t.integer().optional(),
            "type": t.string().optional(),
            "strokeColor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BorderStyleOut"])
    types["AttributesIn"] = t.struct(
        {"attribute": t.array(t.proxy(renames["AttributeIn"]))}
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "attribute": t.array(t.proxy(renames["AttributeOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])
    types["EnumPropertyOptionsIn"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "possibleValues": t.array(t.proxy(renames["EnumValuePairIn"])).optional(),
            "operatorOptions": t.proxy(renames["EnumOperatorOptionsIn"]).optional(),
        }
    ).named(renames["EnumPropertyOptionsIn"])
    types["EnumPropertyOptionsOut"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "possibleValues": t.array(t.proxy(renames["EnumValuePairOut"])).optional(),
            "operatorOptions": t.proxy(renames["EnumOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumPropertyOptionsOut"])
    types["AppsDynamiteSharedDocumentIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "fileId": t.string().optional(),
            "title": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "url": t.string().optional(),
            "justification": t.proxy(
                renames["AppsDynamiteSharedJustificationIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedDocumentIn"])
    types["AppsDynamiteSharedDocumentOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "fileId": t.string().optional(),
            "title": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "url": t.string().optional(),
            "justification": t.proxy(
                renames["AppsDynamiteSharedJustificationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedDocumentOut"])
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
    types["ProvenanceIn"] = t.struct(
        {
            "canonicalUrl": t.string().optional(),
            "inputUrl": t.string().optional(),
            "itemtype": t.array(t.string()).optional(),
            "retrievedTimestampMsec": t.string().optional(),
            "annotationBlob": t.string().optional(),
            "retrievedUrl": t.string().optional(),
        }
    ).named(renames["ProvenanceIn"])
    types["ProvenanceOut"] = t.struct(
        {
            "canonicalUrl": t.string().optional(),
            "inputUrl": t.string().optional(),
            "itemtype": t.array(t.string()).optional(),
            "retrievedTimestampMsec": t.string().optional(),
            "annotationBlob": t.string().optional(),
            "retrievedUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvenanceOut"])
    types["QueryInterpretationOptionsIn"] = t.struct(
        {
            "disableNlInterpretation": t.boolean().optional(),
            "enableVerbatimMode": t.boolean().optional(),
            "disableSupplementalResults": t.boolean().optional(),
        }
    ).named(renames["QueryInterpretationOptionsIn"])
    types["QueryInterpretationOptionsOut"] = t.struct(
        {
            "disableNlInterpretation": t.boolean().optional(),
            "enableVerbatimMode": t.boolean().optional(),
            "disableSupplementalResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationOptionsOut"])
    types["YouTubeLiveBroadcastEventIn"] = t.struct(
        {
            "brandAccountGaiaId": t.string().optional(),
            "channelId": t.string().optional(),
            "broadcastId": t.string().optional(),
        }
    ).named(renames["YouTubeLiveBroadcastEventIn"])
    types["YouTubeLiveBroadcastEventOut"] = t.struct(
        {
            "viewUrl": t.string().optional(),
            "brandAccountGaiaId": t.string().optional(),
            "channelId": t.string().optional(),
            "broadcastId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeLiveBroadcastEventOut"])
    types["RoomRenameMetadataIn"] = t.struct(
        {"newName": t.string(), "prevName": t.string().optional()}
    ).named(renames["RoomRenameMetadataIn"])
    types["RoomRenameMetadataOut"] = t.struct(
        {
            "newName": t.string(),
            "prevName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoomRenameMetadataOut"])
    types["AppsDynamiteSharedEmojiIn"] = t.struct(
        {
            "unicode": t.string().optional(),
            "customEmoji": t.proxy(
                renames["AppsDynamiteSharedCustomEmojiIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedEmojiIn"])
    types["AppsDynamiteSharedEmojiOut"] = t.struct(
        {
            "unicode": t.string().optional(),
            "customEmoji": t.proxy(
                renames["AppsDynamiteSharedCustomEmojiOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedEmojiOut"])
    types["RosterIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["RosterIdIn"]
    )
    types["RosterIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RosterIdOut"])
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
    types["AppsDynamiteSharedActivityFeedAnnotationDataIn"] = t.struct(
        {
            "chatItem": t.proxy(renames["AppsDynamiteSharedChatItemIn"]),
            "userInfo": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn"]
            ).optional(),
            "activityFeedMessageId": t.proxy(renames["MessageIdIn"]).optional(),
            "sharedUserInfo": t.proxy(renames["UserInfoIn"]).optional(),
            "activityFeedMessageCreateTime": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataIn"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataOut"] = t.struct(
        {
            "chatItem": t.proxy(renames["AppsDynamiteSharedChatItemOut"]),
            "userInfo": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut"]
            ).optional(),
            "activityFeedMessageId": t.proxy(renames["MessageIdOut"]).optional(),
            "sharedUserInfo": t.proxy(renames["UserInfoOut"]).optional(),
            "activityFeedMessageCreateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataOut"])
    types["GatewayAccessIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["GatewayAccessIn"]
    )
    types["GatewayAccessOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayAccessOut"])
    types["ContentReportJustificationIn"] = t.struct(
        {"userJustification": t.string().optional()}
    ).named(renames["ContentReportJustificationIn"])
    types["ContentReportJustificationOut"] = t.struct(
        {
            "userJustification": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentReportJustificationOut"])
    types["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn"] = t.struct(
        {"state": t.string().optional(), "feedbackChipType": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn"])
    types["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut"] = t.struct(
        {
            "state": t.string().optional(),
            "feedbackChipType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut"])
    types["IndexItemOptionsIn"] = t.struct(
        {"allowUnknownGsuitePrincipals": t.boolean().optional()}
    ).named(renames["IndexItemOptionsIn"])
    types["IndexItemOptionsOut"] = t.struct(
        {
            "allowUnknownGsuitePrincipals": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexItemOptionsOut"])
    types["AppsDynamiteSharedDlpMetricsMetadataIn"] = t.struct(
        {"dlpStatus": t.string().optional()}
    ).named(renames["AppsDynamiteSharedDlpMetricsMetadataIn"])
    types["AppsDynamiteSharedDlpMetricsMetadataOut"] = t.struct(
        {
            "dlpStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedDlpMetricsMetadataOut"])
    types["ObjectOptionsIn"] = t.struct(
        {
            "suggestionFilteringOperators": t.array(t.string()).optional(),
            "displayOptions": t.proxy(renames["ObjectDisplayOptionsIn"]).optional(),
            "freshnessOptions": t.proxy(renames["FreshnessOptionsIn"]).optional(),
        }
    ).named(renames["ObjectOptionsIn"])
    types["ObjectOptionsOut"] = t.struct(
        {
            "suggestionFilteringOperators": t.array(t.string()).optional(),
            "displayOptions": t.proxy(renames["ObjectDisplayOptionsOut"]).optional(),
            "freshnessOptions": t.proxy(renames["FreshnessOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectOptionsOut"])
    types["PushItemIn"] = t.struct(
        {
            "queue": t.string().optional(),
            "contentHash": t.string().optional(),
            "type": t.string().optional(),
            "structuredDataHash": t.string().optional(),
            "payload": t.string().optional(),
            "repositoryError": t.proxy(renames["RepositoryErrorIn"]).optional(),
            "metadataHash": t.string().optional(),
        }
    ).named(renames["PushItemIn"])
    types["PushItemOut"] = t.struct(
        {
            "queue": t.string().optional(),
            "contentHash": t.string().optional(),
            "type": t.string().optional(),
            "structuredDataHash": t.string().optional(),
            "payload": t.string().optional(),
            "repositoryError": t.proxy(renames["RepositoryErrorOut"]).optional(),
            "metadataHash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushItemOut"])
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
    types["ChatProtoIn"] = t.struct(
        {"chatId": t.string().optional(), "memberType": t.integer().optional()}
    ).named(renames["ChatProtoIn"])
    types["ChatProtoOut"] = t.struct(
        {
            "chatId": t.string().optional(),
            "memberType": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatProtoOut"])
    types["AppsDynamiteSharedMeetMetadataIn"] = t.struct(
        {"meetingCode": t.string(), "meetingUrl": t.string()}
    ).named(renames["AppsDynamiteSharedMeetMetadataIn"])
    types["AppsDynamiteSharedMeetMetadataOut"] = t.struct(
        {
            "meetingCode": t.string(),
            "meetingUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMeetMetadataOut"])
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
    types["YoutubeUserProtoIn"] = t.struct({"youtubeUserId": t.string()}).named(
        renames["YoutubeUserProtoIn"]
    )
    types["YoutubeUserProtoOut"] = t.struct(
        {
            "youtubeUserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeUserProtoOut"])
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
    types["ResultDisplayLineIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["ResultDisplayFieldIn"]))}
    ).named(renames["ResultDisplayLineIn"])
    types["ResultDisplayLineOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["ResultDisplayFieldOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayLineOut"])
    types["AuthorizedItemIdIn"] = t.struct(
        {"id": t.string().optional(), "resourceKey": t.string().optional()}
    ).named(renames["AuthorizedItemIdIn"])
    types["AuthorizedItemIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "resourceKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedItemIdOut"])
    types["GaiaUserProtoIn"] = t.struct({"userId": t.string()}).named(
        renames["GaiaUserProtoIn"]
    )
    types["GaiaUserProtoOut"] = t.struct(
        {"userId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GaiaUserProtoOut"])
    types["AutoCompleteIn"] = t.struct(
        {"items": t.array(t.proxy(renames["AutoCompleteItemIn"]))}
    ).named(renames["AutoCompleteIn"])
    types["AutoCompleteOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AutoCompleteItemOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoCompleteOut"])
    types["AppsDynamiteSharedChatItemIn"] = t.struct(
        {
            "activityInfo": t.array(
                t.proxy(renames["AppsDynamiteSharedChatItemActivityInfoIn"])
            ).optional(),
            "groupInfo": t.proxy(
                renames["AppsDynamiteSharedChatItemGroupInfoIn"]
            ).optional(),
            "messageInfo": t.proxy(
                renames["AppsDynamiteSharedMessageInfoIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemIn"])
    types["AppsDynamiteSharedChatItemOut"] = t.struct(
        {
            "activityInfo": t.array(
                t.proxy(renames["AppsDynamiteSharedChatItemActivityInfoOut"])
            ).optional(),
            "groupInfo": t.proxy(
                renames["AppsDynamiteSharedChatItemGroupInfoOut"]
            ).optional(),
            "messageInfo": t.proxy(
                renames["AppsDynamiteSharedMessageInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemOut"])
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
    types["CustomFunctionReturnValueMarkupIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CustomFunctionReturnValueMarkupIn"])
    types["CustomFunctionReturnValueMarkupOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomFunctionReturnValueMarkupOut"])
    types["AppsDynamiteSharedCustomEmojiIn"] = t.struct(
        {
            "creatorUserId": t.proxy(renames["UserIdIn"]).optional(),
            "ownerCustomerId": t.proxy(renames["CustomerIdIn"]).optional(),
            "updateTimeMicros": t.string(),
            "blobId": t.string().optional(),
            "createTimeMicros": t.string().optional(),
            "deleteTimeMicros": t.string().optional(),
            "uuid": t.string().optional(),
            "contentType": t.string().optional(),
            "readToken": t.string().optional(),
            "state": t.string().optional(),
            "shortcode": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedCustomEmojiIn"])
    types["AppsDynamiteSharedCustomEmojiOut"] = t.struct(
        {
            "creatorUserId": t.proxy(renames["UserIdOut"]).optional(),
            "ownerCustomerId": t.proxy(renames["CustomerIdOut"]).optional(),
            "ephemeralUrl": t.string().optional(),
            "updateTimeMicros": t.string(),
            "blobId": t.string().optional(),
            "createTimeMicros": t.string().optional(),
            "deleteTimeMicros": t.string().optional(),
            "uuid": t.string().optional(),
            "contentType": t.string().optional(),
            "readToken": t.string().optional(),
            "state": t.string().optional(),
            "shortcode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCustomEmojiOut"])
    types["ContentReportSummaryIn"] = t.struct(
        {
            "numberReportsAllRevisions": t.integer().optional(),
            "numberReports": t.integer().optional(),
        }
    ).named(renames["ContentReportSummaryIn"])
    types["ContentReportSummaryOut"] = t.struct(
        {
            "numberReportsAllRevisions": t.integer().optional(),
            "numberReports": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentReportSummaryOut"])
    types["DeleteMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteMetadataIn"]
    )
    types["DeleteMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteMetadataOut"])
    types["GetCustomerSessionStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["CustomerSessionStatsIn"]))}
    ).named(renames["GetCustomerSessionStatsResponseIn"])
    types["GetCustomerSessionStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerSessionStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerSessionStatsResponseOut"])
    types["ChatContentExtensionIn"] = t.struct(
        {
            "otrModificationEvent": t.proxy(renames["OtrModificationEventIn"]),
            "renameEvent": t.proxy(renames["RenameEventIn"]),
            "annotation": t.array(t.proxy(renames["EventAnnotationIn"])).optional(),
            "eventOtrStatus": t.string().optional(),
            "hangoutEvent": t.proxy(renames["HangoutEventIn"]).optional(),
            "otrChatMessageEvent": t.proxy(renames["OtrChatMessageEventIn"]).optional(),
            "membershipChangeEvent": t.proxy(
                renames["MembershipChangeEventIn"]
            ).optional(),
            "dynamitePlaceholderMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataIn"]
            ).optional(),
            "inviteAcceptedEvent": t.proxy(renames["InviteAcceptedEventIn"]).optional(),
            "groupLinkSharingModificationEvent": t.proxy(
                renames["GroupLinkSharingModificationEventIn"]
            ).optional(),
        }
    ).named(renames["ChatContentExtensionIn"])
    types["ChatContentExtensionOut"] = t.struct(
        {
            "otrModificationEvent": t.proxy(renames["OtrModificationEventOut"]),
            "renameEvent": t.proxy(renames["RenameEventOut"]),
            "annotation": t.array(t.proxy(renames["EventAnnotationOut"])).optional(),
            "eventOtrStatus": t.string().optional(),
            "hangoutEvent": t.proxy(renames["HangoutEventOut"]).optional(),
            "otrChatMessageEvent": t.proxy(
                renames["OtrChatMessageEventOut"]
            ).optional(),
            "membershipChangeEvent": t.proxy(
                renames["MembershipChangeEventOut"]
            ).optional(),
            "dynamitePlaceholderMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataOut"]
            ).optional(),
            "inviteAcceptedEvent": t.proxy(
                renames["InviteAcceptedEventOut"]
            ).optional(),
            "groupLinkSharingModificationEvent": t.proxy(
                renames["GroupLinkSharingModificationEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatContentExtensionOut"])
    types["RbacRoleProtoIn"] = t.struct(
        {
            "rbacRoleName": t.string().optional(),
            "objectId": t.string(),
            "name": t.string(),
            "rbacNamespace": t.string().optional(),
        }
    ).named(renames["RbacRoleProtoIn"])
    types["RbacRoleProtoOut"] = t.struct(
        {
            "rbacRoleName": t.string().optional(),
            "objectId": t.string(),
            "name": t.string(),
            "rbacNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RbacRoleProtoOut"])
    types["UpdateSchemaRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "schema": t.proxy(renames["SchemaIn"]).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["UpdateSchemaRequestIn"])
    types["UpdateSchemaRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "schema": t.proxy(renames["SchemaOut"]).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSchemaRequestOut"])
    types["QueryOperatorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "enumValues": t.array(t.string()).optional(),
            "isFacetable": t.boolean().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "isReturnable": t.boolean().optional(),
            "objectType": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "isSortable": t.boolean().optional(),
            "operatorName": t.string().optional(),
            "isRepeatable": t.boolean().optional(),
            "displayName": t.string().optional(),
            "isSuggestable": t.boolean().optional(),
        }
    ).named(renames["QueryOperatorIn"])
    types["QueryOperatorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "enumValues": t.array(t.string()).optional(),
            "isFacetable": t.boolean().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "isReturnable": t.boolean().optional(),
            "objectType": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "isSortable": t.boolean().optional(),
            "operatorName": t.string().optional(),
            "isRepeatable": t.boolean().optional(),
            "displayName": t.string().optional(),
            "isSuggestable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOperatorOut"])
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
    types["PollItemsRequestIn"] = t.struct(
        {
            "queue": t.string().optional(),
            "limit": t.integer().optional(),
            "statusCodes": t.array(t.string()).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["PollItemsRequestIn"])
    types["PollItemsRequestOut"] = t.struct(
        {
            "queue": t.string().optional(),
            "limit": t.integer().optional(),
            "statusCodes": t.array(t.string()).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollItemsRequestOut"])
    types["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"] = t.struct(
        {"filename": t.string()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"] = t.struct(
        {"filename": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"])
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
    types["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "deleted": t.boolean().optional(),
            "assignee": t.proxy(renames["UserIdIn"]).optional(),
            "completed": t.boolean().optional(),
            "description": t.string().optional(),
            "startTime": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"])
    types["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "deleted": t.boolean().optional(),
            "assignee": t.proxy(renames["UserIdOut"]).optional(),
            "completed": t.boolean().optional(),
            "description": t.string().optional(),
            "startTime": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"])
    types["LabelRenamedIn"] = t.struct({"oldCanonicalName": t.string()}).named(
        renames["LabelRenamedIn"]
    )
    types["LabelRenamedOut"] = t.struct(
        {
            "oldCanonicalName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelRenamedOut"])
    types["ErrorInfoIn"] = t.struct(
        {"errorMessages": t.array(t.proxy(renames["ErrorMessageIn"]))}
    ).named(renames["ErrorInfoIn"])
    types["ErrorInfoOut"] = t.struct(
        {
            "errorMessages": t.array(t.proxy(renames["ErrorMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorInfoOut"])
    types["GoogleChatV1ContextualAddOnMarkupCardIn"] = t.struct(
        {
            "cardActions": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardCardActionIn"])
            ).optional(),
            "name": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardSectionIn"])
            ).optional(),
            "header": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"]
            ).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardOut"] = t.struct(
        {
            "cardActions": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardCardActionOut"])
            ).optional(),
            "name": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardSectionOut"])
            ).optional(),
            "header": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardOut"])
    types["ObjectValuesIn"] = t.struct(
        {"values": t.array(t.proxy(renames["StructuredDataObjectIn"]))}
    ).named(renames["ObjectValuesIn"])
    types["ObjectValuesOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["StructuredDataObjectOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectValuesOut"])
    types["ContextAttributeIn"] = t.struct(
        {"values": t.array(t.string()).optional(), "name": t.string().optional()}
    ).named(renames["ContextAttributeIn"])
    types["ContextAttributeOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextAttributeOut"])
    types["TriggerActionIn"] = t.struct(
        {"dataInt": t.string(), "action": t.string(), "data": t.string().optional()}
    ).named(renames["TriggerActionIn"])
    types["TriggerActionOut"] = t.struct(
        {
            "dataInt": t.string(),
            "action": t.string(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerActionOut"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn"] = t.struct(
        {
            "startTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn"
                ]
            ).optional(),
            "eventId": t.string().optional(),
            "title": t.string().optional(),
            "endTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn"
                ]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut"] = t.struct(
        {
            "startTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut"
                ]
            ).optional(),
            "eventId": t.string().optional(),
            "title": t.string().optional(),
            "endTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut"])
    types["ResetSearchApplicationRequestIn"] = t.struct(
        {"debugOptions": t.proxy(renames["DebugOptionsIn"]).optional()}
    ).named(renames["ResetSearchApplicationRequestIn"])
    types["ResetSearchApplicationRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetSearchApplicationRequestOut"])
    types["PhotoIn"] = t.struct({"url": t.string().optional()}).named(
        renames["PhotoIn"]
    )
    types["PhotoOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["AppsDynamiteStorageSelectionInputSelectionItemIn"] = t.struct(
        {
            "text": t.string().optional(),
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputSelectionItemIn"])
    types["AppsDynamiteStorageSelectionInputSelectionItemOut"] = t.struct(
        {
            "text": t.string().optional(),
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputSelectionItemOut"])
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
    types["AppsDynamiteSharedSegmentedMembershipCountIn"] = t.struct(
        {
            "membershipCount": t.integer().optional(),
            "membershipState": t.string(),
            "memberType": t.string(),
        }
    ).named(renames["AppsDynamiteSharedSegmentedMembershipCountIn"])
    types["AppsDynamiteSharedSegmentedMembershipCountOut"] = t.struct(
        {
            "membershipCount": t.integer().optional(),
            "membershipState": t.string(),
            "memberType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedSegmentedMembershipCountOut"])
    types["MultiKeyIn"] = t.struct(
        {
            "clientAssignedPermId": t.string().optional(),
            "serverId": t.string().optional(),
        }
    ).named(renames["MultiKeyIn"])
    types["MultiKeyOut"] = t.struct(
        {
            "clientAssignedPermId": t.string().optional(),
            "serverId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiKeyOut"])
    types["UpdateSubjectIn"] = t.struct({"subject": t.string()}).named(
        renames["UpdateSubjectIn"]
    )
    types["UpdateSubjectOut"] = t.struct(
        {"subject": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateSubjectOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn"
    ] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "resourceUrl": t.string(),
            "title": t.string().optional(),
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
            "resourceUrl": t.string(),
            "title": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut"
        ]
    )
    types["StreamingSessionInfoIn"] = t.struct(
        {
            "latestSessionEvent": t.proxy(renames["SessionEventIn"]).optional(),
            "applicationType": t.string().optional(),
            "viewerStats": t.proxy(renames["StreamViewerStatsIn"]).optional(),
            "status": t.string().optional(),
            "sessionId": t.string().optional(),
            "viewerAccessPolicy": t.string().optional(),
            "trainingEnabled": t.boolean().optional(),
            "ownerDisplayName": t.string().optional(),
        }
    ).named(renames["StreamingSessionInfoIn"])
    types["StreamingSessionInfoOut"] = t.struct(
        {
            "latestSessionEvent": t.proxy(renames["SessionEventOut"]).optional(),
            "applicationType": t.string().optional(),
            "viewerStats": t.proxy(renames["StreamViewerStatsOut"]).optional(),
            "status": t.string().optional(),
            "sessionId": t.string().optional(),
            "viewerAccessPolicy": t.string().optional(),
            "trainingEnabled": t.boolean().optional(),
            "ownerDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSessionInfoOut"])
    types["RecordingInfoIn"] = t.struct(
        {
            "ownerDisplayName": t.string().optional(),
            "recordingId": t.string().optional(),
            "recordingApplicationType": t.string().optional(),
            "latestRecordingEvent": t.proxy(renames["RecordingEventIn"]).optional(),
            "producerDeviceId": t.string().optional(),
            "recordingStatus": t.string().optional(),
        }
    ).named(renames["RecordingInfoIn"])
    types["RecordingInfoOut"] = t.struct(
        {
            "ownerDisplayName": t.string().optional(),
            "recordingId": t.string().optional(),
            "recordingApplicationType": t.string().optional(),
            "latestRecordingEvent": t.proxy(renames["RecordingEventOut"]).optional(),
            "producerDeviceId": t.string().optional(),
            "recordingStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordingInfoOut"])
    types["HtmlValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["HtmlValuesIn"]
    )
    types["HtmlValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlValuesOut"])
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
    types["GoogleChatV1ContextualAddOnMarkupCardSectionIn"] = t.struct(
        {
            "header": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupIn"])
            ).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardSectionIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardSectionOut"] = t.struct(
        {
            "header": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardSectionOut"])
    types["ImapSessionContextIn"] = t.struct(
        {
            "possiblyTrimmedModel": t.proxy(renames["PossiblyTrimmedModelIn"]),
            "os": t.string(),
            "app": t.string(),
            "guidFingerprint": t.string().optional(),
            "osVersion": t.proxy(renames["OsVersionIn"]),
            "deviceType": t.string().optional(),
        }
    ).named(renames["ImapSessionContextIn"])
    types["ImapSessionContextOut"] = t.struct(
        {
            "possiblyTrimmedModel": t.proxy(renames["PossiblyTrimmedModelOut"]),
            "os": t.string(),
            "app": t.string(),
            "guidFingerprint": t.string().optional(),
            "osVersion": t.proxy(renames["OsVersionOut"]),
            "deviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapSessionContextOut"])
    types["IndexItemRequestIn"] = t.struct(
        {
            "mode": t.string(),
            "indexItemOptions": t.proxy(renames["IndexItemOptionsIn"]),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "connectorName": t.string().optional(),
            "item": t.proxy(renames["ItemIn"]).optional(),
        }
    ).named(renames["IndexItemRequestIn"])
    types["IndexItemRequestOut"] = t.struct(
        {
            "mode": t.string(),
            "indexItemOptions": t.proxy(renames["IndexItemOptionsOut"]),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "connectorName": t.string().optional(),
            "item": t.proxy(renames["ItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexItemRequestOut"])
    types["LabelUpdatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelUpdatedIn"]
    )
    types["LabelUpdatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelUpdatedOut"])
    types["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"])
    types["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"])
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
    types["FolderAttributeIn"] = t.struct(
        {"folder": t.array(t.proxy(renames["FolderIn"])).optional()}
    ).named(renames["FolderAttributeIn"])
    types["FolderAttributeOut"] = t.struct(
        {
            "folder": t.array(t.proxy(renames["FolderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderAttributeOut"])
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
    types["ChatConserverDynamitePlaceholderMetadataIn"] = t.struct(
        {
            "calendarEventMetadata": t.proxy(
                renames[
                    "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"
                ]
            ),
            "editMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"]
            ),
            "botMessageMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"]
            ),
            "attachmentMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"]
            ),
            "videoCallMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"]
            ),
            "spaceUrl": t.string().optional(),
            "deleteMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"]
            ),
            "tasksMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"]
            ),
        }
    ).named(renames["ChatConserverDynamitePlaceholderMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataOut"] = t.struct(
        {
            "calendarEventMetadata": t.proxy(
                renames[
                    "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"
                ]
            ),
            "editMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"]
            ),
            "botMessageMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut"]
            ),
            "attachmentMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"]
            ),
            "videoCallMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut"]
            ),
            "spaceUrl": t.string().optional(),
            "deleteMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"]
            ),
            "tasksMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatConserverDynamitePlaceholderMetadataOut"])
    types["DividerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DividerIn"]
    )
    types["DividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DividerOut"])
    types["ResourceRoleProtoIn"] = t.struct(
        {
            "applicationId": t.string(),
            "roleId": t.integer(),
            "objectId": t.string(),
            "objectPart": t.string(),
        }
    ).named(renames["ResourceRoleProtoIn"])
    types["ResourceRoleProtoOut"] = t.struct(
        {
            "applicationId": t.string(),
            "roleId": t.integer(),
            "objectId": t.string(),
            "objectPart": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRoleProtoOut"])
    types["PhoneAccessIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "formattedPhoneNumber": t.string().optional(),
            "pin": t.string().optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["PhoneAccessIn"])
    types["PhoneAccessOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "formattedPhoneNumber": t.string().optional(),
            "pin": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneAccessOut"])
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
    types["VPCSettingsIn"] = t.struct({"project": t.string().optional()}).named(
        renames["VPCSettingsIn"]
    )
    types["VPCSettingsOut"] = t.struct(
        {
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VPCSettingsOut"])
    types["ItemAclIn"] = t.struct(
        {
            "owners": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "inheritAclFrom": t.string().optional(),
            "readers": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "deniedReaders": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "aclInheritanceType": t.string().optional(),
        }
    ).named(renames["ItemAclIn"])
    types["ItemAclOut"] = t.struct(
        {
            "owners": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "inheritAclFrom": t.string().optional(),
            "readers": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "deniedReaders": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "aclInheritanceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemAclOut"])
    types["SimpleSecretHolderProtoIn"] = t.struct(
        {"label": t.proxy(renames["SimpleSecretLabelProtoIn"]).optional()}
    ).named(renames["SimpleSecretHolderProtoIn"])
    types["SimpleSecretHolderProtoOut"] = t.struct(
        {
            "label": t.proxy(renames["SimpleSecretLabelProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleSecretHolderProtoOut"])
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
    types["AppsDynamiteSharedAvatarInfoIn"] = t.struct(
        {"emoji": t.proxy(renames["AppsDynamiteSharedEmojiIn"])}
    ).named(renames["AppsDynamiteSharedAvatarInfoIn"])
    types["AppsDynamiteSharedAvatarInfoOut"] = t.struct(
        {
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAvatarInfoOut"])
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
    types["PresenterIn"] = t.struct(
        {
            "copresenterDeviceIds": t.array(t.string()).optional(),
            "presenterDeviceId": t.string().optional(),
            "byDeviceId": t.string().optional(),
        }
    ).named(renames["PresenterIn"])
    types["PresenterOut"] = t.struct(
        {
            "copresenterDeviceIds": t.array(t.string()).optional(),
            "presenterDeviceId": t.string().optional(),
            "byDeviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresenterOut"])
    types["FreshnessOptionsIn"] = t.struct(
        {
            "freshnessProperty": t.string().optional(),
            "freshnessDuration": t.string().optional(),
        }
    ).named(renames["FreshnessOptionsIn"])
    types["FreshnessOptionsOut"] = t.struct(
        {
            "freshnessProperty": t.string().optional(),
            "freshnessDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreshnessOptionsOut"])
    types["CheckAccessResponseIn"] = t.struct(
        {"hasAccess": t.boolean().optional()}
    ).named(renames["CheckAccessResponseIn"])
    types["CheckAccessResponseOut"] = t.struct(
        {
            "hasAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckAccessResponseOut"])
    types["DriveFollowUpRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveFollowUpRestrictIn"]
    )
    types["DriveFollowUpRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveFollowUpRestrictOut"])
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
    types["SourceConfigIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "crowdingConfig": t.proxy(renames["SourceCrowdingConfigIn"]).optional(),
            "scoringConfig": t.proxy(renames["SourceScoringConfigIn"]).optional(),
        }
    ).named(renames["SourceConfigIn"])
    types["SourceConfigOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "crowdingConfig": t.proxy(renames["SourceCrowdingConfigOut"]).optional(),
            "scoringConfig": t.proxy(renames["SourceScoringConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceConfigOut"])
    types["QueryInterpretationIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "interpretationType": t.string(),
            "interpretedQuery": t.string().optional(),
        }
    ).named(renames["QueryInterpretationIn"])
    types["QueryInterpretationOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "interpretationType": t.string(),
            "interpretedQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationOut"])
    types["FacetBucketIn"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "value": t.proxy(renames["ValueIn"]),
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "count": t.integer().optional(),
        }
    ).named(renames["FacetBucketIn"])
    types["FacetBucketOut"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "value": t.proxy(renames["ValueOut"]),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "count": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetBucketOut"])
    types["TextValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["TextValuesIn"]
    )
    types["TextValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextValuesOut"])
    types["AppsDynamiteStorageImageIn"] = t.struct(
        {
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]),
            "altText": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageImageIn"])
    types["AppsDynamiteStorageImageOut"] = t.struct(
        {
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]),
            "altText": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageOut"])
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
    types["SuggestResponseIn"] = t.struct(
        {"suggestResults": t.array(t.proxy(renames["SuggestResultIn"])).optional()}
    ).named(renames["SuggestResponseIn"])
    types["SuggestResponseOut"] = t.struct(
        {
            "suggestResults": t.array(t.proxy(renames["SuggestResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestResponseOut"])
    types["MediaIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["MediaIn"]
    )
    types["MediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["WonderMessageMappingIn"] = t.struct(
        {"wonderCardMessageId": t.array(t.string()).optional()}
    ).named(renames["WonderMessageMappingIn"])
    types["WonderMessageMappingOut"] = t.struct(
        {
            "wonderCardMessageId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WonderMessageMappingOut"])
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
    types["ClientContextIn"] = t.struct(
        {
            "sessionContext": t.proxy(renames["SessionContextIn"]).optional(),
            "clientOperationId": t.string().optional(),
            "clientType": t.string().optional(),
            "userIp": t.string().optional(),
        }
    ).named(renames["ClientContextIn"])
    types["ClientContextOut"] = t.struct(
        {
            "sessionContext": t.proxy(renames["SessionContextOut"]).optional(),
            "clientOperationId": t.string().optional(),
            "clientType": t.string().optional(),
            "userIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientContextOut"])
    types["SuggestResultIn"] = t.struct(
        {
            "peopleSuggestion": t.proxy(renames["PeopleSuggestionIn"]).optional(),
            "querySuggestion": t.proxy(renames["QuerySuggestionIn"]).optional(),
            "suggestedQuery": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["SuggestResultIn"])
    types["SuggestResultOut"] = t.struct(
        {
            "peopleSuggestion": t.proxy(renames["PeopleSuggestionOut"]).optional(),
            "querySuggestion": t.proxy(renames["QuerySuggestionOut"]).optional(),
            "suggestedQuery": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestResultOut"])
    types["AclFixStatusIn"] = t.struct(
        {
            "fixability": t.string(),
            "fixableEmailAddress": t.array(t.string()).optional(),
            "outOfDomainWarningEmailAddress": t.array(t.string()).optional(),
        }
    ).named(renames["AclFixStatusIn"])
    types["AclFixStatusOut"] = t.struct(
        {
            "fixability": t.string(),
            "fixableEmailAddress": t.array(t.string()).optional(),
            "outOfDomainWarningEmailAddress": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclFixStatusOut"])
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
    types["RenameEventIn"] = t.struct(
        {"newName": t.string(), "originalName": t.string()}
    ).named(renames["RenameEventIn"])
    types["RenameEventOut"] = t.struct(
        {
            "newName": t.string(),
            "originalName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameEventOut"])
    types["AppsDynamiteStorageIconIn"] = t.struct(
        {
            "materialIcon": t.proxy(
                renames["AppsDynamiteStorageMaterialIconIn"]
            ).optional(),
            "imageType": t.string().optional(),
            "knownIcon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageIconIn"])
    types["AppsDynamiteStorageIconOut"] = t.struct(
        {
            "materialIcon": t.proxy(
                renames["AppsDynamiteStorageMaterialIconOut"]
            ).optional(),
            "imageType": t.string().optional(),
            "knownIcon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageIconOut"])
    types["DataLossPreventionMetadataIn"] = t.struct(
        {
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryIn"]).optional(),
            "warnAcknowledged": t.boolean().optional(),
        }
    ).named(renames["DataLossPreventionMetadataIn"])
    types["DataLossPreventionMetadataOut"] = t.struct(
        {
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryOut"]).optional(),
            "warnAcknowledged": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLossPreventionMetadataOut"])
    types["BroadcastStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["BroadcastStatsIn"])
    types["BroadcastStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BroadcastStatsOut"])
    types["AppsDynamiteSharedChatItemActivityInfoIn"] = t.struct(
        {
            "feedItemReactions": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"]
            ),
            "feedItemNudge": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"]
            ),
            "feedItemThreadReply": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"]
            ),
            "feedItemUserMention": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"]
            ),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoIn"])
    types["AppsDynamiteSharedChatItemActivityInfoOut"] = t.struct(
        {
            "feedItemReactions": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"]
            ),
            "feedItemNudge": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut"]
            ),
            "feedItemThreadReply": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut"]
            ),
            "feedItemUserMention": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoOut"])
    types["SchemaIn"] = t.struct(
        {
            "operationIds": t.array(t.string()).optional(),
            "objectDefinitions": t.array(
                t.proxy(renames["ObjectDefinitionIn"])
            ).optional(),
        }
    ).named(renames["SchemaIn"])
    types["SchemaOut"] = t.struct(
        {
            "operationIds": t.array(t.string()).optional(),
            "objectDefinitions": t.array(
                t.proxy(renames["ObjectDefinitionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaOut"])
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
    types["EmbedClientItemIn"] = t.struct(
        {
            "deepLinkData": t.proxy(renames["DeepLinkDataIn"]).optional(),
            "signature": t.string().optional(),
            "id": t.string().optional(),
            "type": t.array(t.string()).optional(),
            "transientData": t.proxy(renames["TransientDataIn"]).optional(),
            "provenance": t.proxy(renames["ProvenanceIn"]).optional(),
            "renderId": t.string().optional(),
            "canonicalId": t.string().optional(),
        }
    ).named(renames["EmbedClientItemIn"])
    types["EmbedClientItemOut"] = t.struct(
        {
            "deepLinkData": t.proxy(renames["DeepLinkDataOut"]).optional(),
            "signature": t.string().optional(),
            "id": t.string().optional(),
            "type": t.array(t.string()).optional(),
            "transientData": t.proxy(renames["TransientDataOut"]).optional(),
            "provenance": t.proxy(renames["ProvenanceOut"]).optional(),
            "renderId": t.string().optional(),
            "canonicalId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbedClientItemOut"])
    types["ConsentedAppUnfurlMetadataIn"] = t.struct(
        {"clientSpecifiedAppId": t.proxy(renames["UserIdIn"]).optional()}
    ).named(renames["ConsentedAppUnfurlMetadataIn"])
    types["ConsentedAppUnfurlMetadataOut"] = t.struct(
        {
            "clientSpecifiedAppId": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentedAppUnfurlMetadataOut"])
    types["AnnotationIn"] = t.struct(
        {
            "chipRenderType": t.string().optional(),
            "consentedAppUnfurlMetadata": t.proxy(
                renames["ConsentedAppUnfurlMetadataIn"]
            ),
            "membershipChanged": t.proxy(
                renames["MembershipChangedMetadataIn"]
            ).optional(),
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
            "uploadMetadata": t.proxy(renames["UploadMetadataIn"]),
            "requiredMessageFeaturesMetadata": t.proxy(
                renames["RequiredMessageFeaturesMetadataIn"]
            ).optional(),
            "incomingWebhookChangedMetadata": t.proxy(
                renames["IncomingWebhookChangedMetadataIn"]
            ),
            "integrationConfigUpdated": t.proxy(
                renames["IntegrationConfigUpdatedMetadataIn"]
            ).optional(),
            "componentSearchInfo": t.proxy(
                renames["AppsDynamiteSharedMessageComponentSearchInfoIn"]
            ).optional(),
            "roomUpdated": t.proxy(renames["RoomUpdatedMetadataIn"]),
            "length": t.integer().optional(),
            "cardCapabilityMetadata": t.proxy(
                renames["CardCapabilityMetadataIn"]
            ).optional(),
            "urlMetadata": t.proxy(renames["UrlMetadataIn"]),
            "dataLossPreventionMetadata": t.proxy(
                renames["DataLossPreventionMetadataIn"]
            ),
            "slashCommandMetadata": t.proxy(renames["SlashCommandMetadataIn"]),
            "videoCallMetadata": t.proxy(renames["VideoCallMetadataIn"]),
            "formatMetadata": t.proxy(renames["FormatMetadataIn"]),
            "readReceiptsSettingsMetadata": t.proxy(
                renames["ReadReceiptsSettingsUpdatedMetadataIn"]
            ),
            "interactionData": t.proxy(renames["InteractionDataIn"]).optional(),
            "localId": t.string().optional(),
            "uniqueId": t.string().optional(),
            "youtubeMetadata": t.proxy(renames["YoutubeMetadataIn"]),
            "driveMetadata": t.proxy(renames["DriveMetadataIn"]).optional(),
            "groupRetentionSettingsUpdated": t.proxy(
                renames["GroupRetentionSettingsUpdatedMetaDataIn"]
            ),
            "babelPlaceholderMetadata": t.proxy(renames["BabelPlaceholderMetadataIn"]),
            "inlineRenderFormat": t.string().optional(),
            "customEmojiMetadata": t.proxy(renames["CustomEmojiMetadataIn"]),
            "gsuiteIntegrationMetadata": t.proxy(
                renames["GsuiteIntegrationMetadataIn"]
            ).optional(),
            "serverInvalidated": t.boolean().optional(),
            "userMentionMetadata": t.proxy(renames["UserMentionMetadataIn"]).optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "chipRenderType": t.string().optional(),
            "consentedAppUnfurlMetadata": t.proxy(
                renames["ConsentedAppUnfurlMetadataOut"]
            ),
            "membershipChanged": t.proxy(
                renames["MembershipChangedMetadataOut"]
            ).optional(),
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
            "uploadMetadata": t.proxy(renames["UploadMetadataOut"]),
            "requiredMessageFeaturesMetadata": t.proxy(
                renames["RequiredMessageFeaturesMetadataOut"]
            ).optional(),
            "incomingWebhookChangedMetadata": t.proxy(
                renames["IncomingWebhookChangedMetadataOut"]
            ),
            "integrationConfigUpdated": t.proxy(
                renames["IntegrationConfigUpdatedMetadataOut"]
            ).optional(),
            "componentSearchInfo": t.proxy(
                renames["AppsDynamiteSharedMessageComponentSearchInfoOut"]
            ).optional(),
            "roomUpdated": t.proxy(renames["RoomUpdatedMetadataOut"]),
            "length": t.integer().optional(),
            "cardCapabilityMetadata": t.proxy(
                renames["CardCapabilityMetadataOut"]
            ).optional(),
            "urlMetadata": t.proxy(renames["UrlMetadataOut"]),
            "dataLossPreventionMetadata": t.proxy(
                renames["DataLossPreventionMetadataOut"]
            ),
            "slashCommandMetadata": t.proxy(renames["SlashCommandMetadataOut"]),
            "videoCallMetadata": t.proxy(renames["VideoCallMetadataOut"]),
            "formatMetadata": t.proxy(renames["FormatMetadataOut"]),
            "readReceiptsSettingsMetadata": t.proxy(
                renames["ReadReceiptsSettingsUpdatedMetadataOut"]
            ),
            "interactionData": t.proxy(renames["InteractionDataOut"]).optional(),
            "localId": t.string().optional(),
            "uniqueId": t.string().optional(),
            "youtubeMetadata": t.proxy(renames["YoutubeMetadataOut"]),
            "driveMetadata": t.proxy(renames["DriveMetadataOut"]).optional(),
            "groupRetentionSettingsUpdated": t.proxy(
                renames["GroupRetentionSettingsUpdatedMetaDataOut"]
            ),
            "babelPlaceholderMetadata": t.proxy(renames["BabelPlaceholderMetadataOut"]),
            "inlineRenderFormat": t.string().optional(),
            "customEmojiMetadata": t.proxy(renames["CustomEmojiMetadataOut"]),
            "gsuiteIntegrationMetadata": t.proxy(
                renames["GsuiteIntegrationMetadataOut"]
            ).optional(),
            "serverInvalidated": t.boolean().optional(),
            "userMentionMetadata": t.proxy(
                renames["UserMentionMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["SessionContextIn"] = t.struct(
        {
            "delegateUserId": t.string().optional(),
            "imapSessionContext": t.proxy(renames["ImapSessionContextIn"]).optional(),
            "dusi": t.string().optional(),
            "oauthProjectId": t.string().optional(),
            "authTime": t.string().optional(),
            "oauthLoginId": t.integer().optional(),
        }
    ).named(renames["SessionContextIn"])
    types["SessionContextOut"] = t.struct(
        {
            "delegateUserId": t.string().optional(),
            "imapSessionContext": t.proxy(renames["ImapSessionContextOut"]).optional(),
            "dusi": t.string().optional(),
            "oauthProjectId": t.string().optional(),
            "authTime": t.string().optional(),
            "oauthLoginId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionContextOut"])
    types["ItemContentIn"] = t.struct(
        {
            "inlineContent": t.string().optional(),
            "contentDataRef": t.proxy(renames["UploadItemRefIn"]).optional(),
            "contentFormat": t.string(),
            "hash": t.string().optional(),
        }
    ).named(renames["ItemContentIn"])
    types["ItemContentOut"] = t.struct(
        {
            "inlineContent": t.string().optional(),
            "contentDataRef": t.proxy(renames["UploadItemRefOut"]).optional(),
            "contentFormat": t.string(),
            "hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemContentOut"])
    types["CustomerSessionStatsIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "searchSessionsCount": t.string().optional(),
        }
    ).named(renames["CustomerSessionStatsIn"])
    types["CustomerSessionStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "searchSessionsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerSessionStatsOut"])
    types["VoicePhoneNumberI18nDataIn"] = t.struct(
        {
            "isValid": t.boolean().optional(),
            "countryCode": t.integer().optional(),
            "validationResult": t.string().optional(),
            "nationalNumber": t.string().optional(),
            "internationalNumber": t.string().optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["VoicePhoneNumberI18nDataIn"])
    types["VoicePhoneNumberI18nDataOut"] = t.struct(
        {
            "isValid": t.boolean().optional(),
            "countryCode": t.integer().optional(),
            "validationResult": t.string().optional(),
            "nationalNumber": t.string().optional(),
            "internationalNumber": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoicePhoneNumberI18nDataOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"])
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
    types["RecordingSessionInfoIn"] = t.struct(
        {
            "recordingSessionId": t.string().optional(),
            "ownerEmail": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
        }
    ).named(renames["RecordingSessionInfoIn"])
    types["RecordingSessionInfoOut"] = t.struct(
        {
            "recordingSessionId": t.string().optional(),
            "ownerEmail": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordingSessionInfoOut"])
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
    types["ResultDisplayFieldIn"] = t.struct(
        {
            "property": t.proxy(renames["NamedPropertyIn"]).optional(),
            "label": t.string().optional(),
            "operatorName": t.string().optional(),
        }
    ).named(renames["ResultDisplayFieldIn"])
    types["ResultDisplayFieldOut"] = t.struct(
        {
            "property": t.proxy(renames["NamedPropertyOut"]).optional(),
            "label": t.string().optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayFieldOut"])
    types["PreStateIn"] = t.struct(
        {
            "syncIds": t.array(t.integer()).optional(),
            "messageKey": t.proxy(renames["MultiKeyIn"]),
            "threadKey": t.proxy(renames["MultiKeyIn"]),
            "labelIds": t.array(t.string()),
        }
    ).named(renames["PreStateIn"])
    types["PreStateOut"] = t.struct(
        {
            "syncIds": t.array(t.integer()).optional(),
            "messageKey": t.proxy(renames["MultiKeyOut"]),
            "threadKey": t.proxy(renames["MultiKeyOut"]),
            "labelIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreStateOut"])
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
    types["AppsDynamiteSharedGroupVisibilityIn"] = t.struct(
        {"state": t.string()}
    ).named(renames["AppsDynamiteSharedGroupVisibilityIn"])
    types["AppsDynamiteSharedGroupVisibilityOut"] = t.struct(
        {"state": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedGroupVisibilityOut"])
    types["HostAppActionMarkupIn"] = t.struct(
        {
            "driveAction": t.proxy(renames["DriveClientActionMarkupIn"]).optional(),
            "sheetsAction": t.proxy(renames["SheetsClientActionMarkupIn"]).optional(),
            "gmailAction": t.proxy(renames["GmailClientActionMarkupIn"]).optional(),
            "editorAction": t.proxy(renames["EditorClientActionMarkupIn"]).optional(),
            "chatAction": t.proxy(renames["ChatClientActionMarkupIn"]).optional(),
            "calendarAction": t.proxy(
                renames["CalendarClientActionMarkupIn"]
            ).optional(),
        }
    ).named(renames["HostAppActionMarkupIn"])
    types["HostAppActionMarkupOut"] = t.struct(
        {
            "driveAction": t.proxy(renames["DriveClientActionMarkupOut"]).optional(),
            "sheetsAction": t.proxy(renames["SheetsClientActionMarkupOut"]).optional(),
            "gmailAction": t.proxy(renames["GmailClientActionMarkupOut"]).optional(),
            "editorAction": t.proxy(renames["EditorClientActionMarkupOut"]).optional(),
            "chatAction": t.proxy(renames["ChatClientActionMarkupOut"]).optional(),
            "calendarAction": t.proxy(
                renames["CalendarClientActionMarkupOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostAppActionMarkupOut"])
    types["PollItemsResponseIn"] = t.struct(
        {"items": t.array(t.proxy(renames["ItemIn"])).optional()}
    ).named(renames["PollItemsResponseIn"])
    types["PollItemsResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollItemsResponseOut"])
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
        {"height": t.integer(), "width": t.integer()}
    ).named(renames["AppsDynamiteSharedDimensionIn"])
    types["AppsDynamiteSharedDimensionOut"] = t.struct(
        {
            "height": t.integer(),
            "width": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedDimensionOut"])
    types["AppsDynamiteSharedJustificationIn"] = t.struct(
        {
            "topics": t.array(t.string()).optional(),
            "actionType": t.string().optional(),
            "actionTime": t.string().optional(),
            "documentOwner": t.proxy(
                renames["AppsDynamiteSharedJustificationPersonIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedJustificationIn"])
    types["AppsDynamiteSharedJustificationOut"] = t.struct(
        {
            "topics": t.array(t.string()).optional(),
            "actionType": t.string().optional(),
            "actionTime": t.string().optional(),
            "documentOwner": t.proxy(
                renames["AppsDynamiteSharedJustificationPersonOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedJustificationOut"])
    types["YouTubeBroadcastStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["YouTubeBroadcastStatsIn"])
    types["YouTubeBroadcastStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeBroadcastStatsOut"])
    types["AppsDynamiteStorageDividerIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteStorageDividerIn"])
    types["AppsDynamiteStorageDividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteStorageDividerOut"])
    types["HashtagDataIn"] = t.struct({"searchText": t.string()}).named(
        renames["HashtagDataIn"]
    )
    types["HashtagDataOut"] = t.struct(
        {
            "searchText": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashtagDataOut"])
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
    types["MessageAttributesIn"] = t.struct(
        {"isTombstone": t.boolean().optional()}
    ).named(renames["MessageAttributesIn"])
    types["MessageAttributesOut"] = t.struct(
        {
            "isTombstone": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageAttributesOut"])
    types["PaygateInfoIn"] = t.struct(
        {
            "callEndingTime": t.string().optional(),
            "showUpgradePromos": t.boolean().optional(),
            "callEndingSoonWarningTime": t.string().optional(),
        }
    ).named(renames["PaygateInfoIn"])
    types["PaygateInfoOut"] = t.struct(
        {
            "callEndingTime": t.string().optional(),
            "showUpgradePromos": t.boolean().optional(),
            "callEndingSoonWarningTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaygateInfoOut"])
    types["AppsDynamiteSharedBackendUploadMetadataIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryIn"]).optional(),
            "virusScanResult": t.string().optional(),
            "uploadTimestampUsec": t.string().optional(),
            "contentSize": t.string().optional(),
            "dlpScanOutcome": t.string().optional(),
            "quoteReplyMessageId": t.proxy(renames["MessageIdIn"]).optional(),
            "blobPath": t.string().optional(),
            "videoThumbnailBlobId": t.string().optional(),
            "sha256": t.string().optional(),
            "uploadIp": t.string().optional(),
            "isClientSideTranscodedVideo": t.boolean().optional(),
            "groupId": t.proxy(renames["GroupIdIn"]).optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionIn"]
            ).optional(),
            "contentName": t.string().optional(),
            "videoId": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedBackendUploadMetadataIn"])
    types["AppsDynamiteSharedBackendUploadMetadataOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryOut"]).optional(),
            "virusScanResult": t.string().optional(),
            "uploadTimestampUsec": t.string().optional(),
            "contentSize": t.string().optional(),
            "dlpScanOutcome": t.string().optional(),
            "quoteReplyMessageId": t.proxy(renames["MessageIdOut"]).optional(),
            "blobPath": t.string().optional(),
            "videoThumbnailBlobId": t.string().optional(),
            "sha256": t.string().optional(),
            "uploadIp": t.string().optional(),
            "isClientSideTranscodedVideo": t.boolean().optional(),
            "groupId": t.proxy(renames["GroupIdOut"]).optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionOut"]
            ).optional(),
            "contentName": t.string().optional(),
            "videoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedBackendUploadMetadataOut"])
    types["SupportUrlsIn"] = t.struct(
        {
            "tosUrl": t.string().optional(),
            "setupUrl": t.string().optional(),
            "gwmUrl": t.string().optional(),
            "deletionPolicyUrl": t.string().optional(),
            "supportUrl": t.string().optional(),
            "privacyPolicyUrl": t.string().optional(),
            "adminConfigUrl": t.string().optional(),
        }
    ).named(renames["SupportUrlsIn"])
    types["SupportUrlsOut"] = t.struct(
        {
            "tosUrl": t.string().optional(),
            "setupUrl": t.string().optional(),
            "gwmUrl": t.string().optional(),
            "deletionPolicyUrl": t.string().optional(),
            "supportUrl": t.string().optional(),
            "privacyPolicyUrl": t.string().optional(),
            "adminConfigUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportUrlsOut"])
    types["AppsDynamiteStorageTextInputIn"] = t.struct(
        {
            "name": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["AppsDynamiteStorageSuggestionsIn"]
            ).optional(),
            "hintText": t.string().optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "autoCompleteAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "label": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageTextInputIn"])
    types["AppsDynamiteStorageTextInputOut"] = t.struct(
        {
            "name": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["AppsDynamiteStorageSuggestionsOut"]
            ).optional(),
            "hintText": t.string().optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "autoCompleteAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageTextInputOut"])
    types["TriggerIn"] = t.struct(
        {
            "rpcOptions": t.proxy(renames["RpcOptionsIn"]),
            "dispatcher": t.string().optional(),
            "key": t.string().optional(),
            "jobsettedServerSpec": t.proxy(renames["JobsettedServerSpecIn"]).optional(),
            "triggerKey": t.proxy(renames["TriggerKeyIn"]).optional(),
            "fireTimeUs": t.string().optional(),
            "triggerAction": t.proxy(renames["TriggerActionIn"]).optional(),
            "dispatchId": t.integer().optional(),
            "actionType": t.integer().optional(),
            "sliceFireTimeUs": t.string().optional(),
            "batchTimeUs": t.string().optional(),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "rpcOptions": t.proxy(renames["RpcOptionsOut"]),
            "dispatcher": t.string().optional(),
            "key": t.string().optional(),
            "jobsettedServerSpec": t.proxy(
                renames["JobsettedServerSpecOut"]
            ).optional(),
            "triggerKey": t.proxy(renames["TriggerKeyOut"]).optional(),
            "fireTimeUs": t.string().optional(),
            "triggerAction": t.proxy(renames["TriggerActionOut"]).optional(),
            "dispatchId": t.integer().optional(),
            "actionType": t.integer().optional(),
            "sliceFireTimeUs": t.string().optional(),
            "batchTimeUs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["GoogleDocsMetadataIn"] = t.struct(
        {
            "typeInfo": t.proxy(renames["TypeInfoIn"]).optional(),
            "lastContentModifiedTimestamp": t.string().optional(),
            "numSubscribers": t.integer().optional(),
            "numViewers": t.integer().optional(),
            "aclInfo": t.proxy(renames["AclInfoIn"]).optional(),
            "resultInfo": t.proxy(renames["GoogleDocsResultInfoIn"]).optional(),
            "documentType": t.string().optional(),
            "fileExtension": t.string().optional(),
        }
    ).named(renames["GoogleDocsMetadataIn"])
    types["GoogleDocsMetadataOut"] = t.struct(
        {
            "typeInfo": t.proxy(renames["TypeInfoOut"]).optional(),
            "lastContentModifiedTimestamp": t.string().optional(),
            "numSubscribers": t.integer().optional(),
            "numViewers": t.integer().optional(),
            "aclInfo": t.proxy(renames["AclInfoOut"]).optional(),
            "resultInfo": t.proxy(renames["GoogleDocsResultInfoOut"]).optional(),
            "documentType": t.string().optional(),
            "fileExtension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDocsMetadataOut"])
    types["DoubleOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["DoubleOperatorOptionsIn"])
    types["DoubleOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleOperatorOptionsOut"])
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
    types["TextOperatorOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "exactMatchWithOperator": t.boolean().optional(),
        }
    ).named(renames["TextOperatorOptionsIn"])
    types["TextOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "exactMatchWithOperator": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextOperatorOptionsOut"])
    types["AppsDynamiteSharedContentReportTypeIn"] = t.struct(
        {"systemViolation": t.string()}
    ).named(renames["AppsDynamiteSharedContentReportTypeIn"])
    types["AppsDynamiteSharedContentReportTypeOut"] = t.struct(
        {
            "systemViolation": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedContentReportTypeOut"])
    types["SearchQualityMetadataIn"] = t.struct(
        {"quality": t.number().optional()}
    ).named(renames["SearchQualityMetadataIn"])
    types["SearchQualityMetadataOut"] = t.struct(
        {
            "quality": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchQualityMetadataOut"])
    types["InteractionIn"] = t.struct(
        {
            "principal": t.proxy(renames["PrincipalIn"]).optional(),
            "type": t.string(),
            "interactionTime": t.string().optional(),
        }
    ).named(renames["InteractionIn"])
    types["InteractionOut"] = t.struct(
        {
            "principal": t.proxy(renames["PrincipalOut"]).optional(),
            "type": t.string(),
            "interactionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InteractionOut"])
    types["AttributeIn"] = t.struct(
        {
            "value": t.proxy(renames["CaribouAttributeValueIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "value": t.proxy(renames["CaribouAttributeValueOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["QueryItemIn"] = t.struct({"isSynthetic": t.boolean().optional()}).named(
        renames["QueryItemIn"]
    )
    types["QueryItemOut"] = t.struct(
        {
            "isSynthetic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryItemOut"])
    types["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"])
    types["AppsDynamiteSharedAssistantUnfulfillableRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantUnfulfillableRequestIn"])
    types["AppsDynamiteSharedAssistantUnfulfillableRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedAssistantUnfulfillableRequestOut"])
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
    types["TranscriptionSessionInfoIn"] = t.struct(
        {
            "transcriptionSessionId": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
        }
    ).named(renames["TranscriptionSessionInfoIn"])
    types["TranscriptionSessionInfoOut"] = t.struct(
        {
            "transcriptionSessionId": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscriptionSessionInfoOut"])
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
    types["PrincipalProtoIn"] = t.struct(
        {
            "mdbUser": t.proxy(renames["MdbUserProtoIn"]).optional(),
            "gaiaGroup": t.proxy(renames["GaiaGroupProtoIn"]).optional(),
            "oauthConsumer": t.proxy(renames["OAuthConsumerProtoIn"]).optional(),
            "rbacRole": t.proxy(renames["RbacRoleProtoIn"]).optional(),
            "scope": t.string().optional(),
            "rbacSubject": t.proxy(renames["RbacSubjectProtoIn"]).optional(),
            "mdbGroup": t.proxy(renames["MdbGroupProtoIn"]).optional(),
            "postiniUser": t.proxy(renames["PostiniUserProtoIn"]).optional(),
            "circle": t.proxy(renames["CircleProtoIn"]).optional(),
            "zwiebackSession": t.proxy(renames["ZwiebackSessionProtoIn"]).optional(),
            "contactGroup": t.proxy(renames["ContactGroupProtoIn"]).optional(),
            "emailOwner": t.proxy(renames["EmailOwnerProtoIn"]).optional(),
            "allAuthenticatedUsers": t.proxy(
                renames["AllAuthenticatedUsersProtoIn"]
            ).optional(),
            "square": t.proxy(renames["SquareProtoIn"]).optional(),
            "chat": t.proxy(renames["ChatProtoIn"]).optional(),
            "cloudPrincipal": t.proxy(renames["CloudPrincipalProtoIn"]).optional(),
            "ldapUser": t.proxy(renames["LdapUserProtoIn"]).optional(),
            "resourceRole": t.proxy(renames["ResourceRoleProtoIn"]).optional(),
            "simpleSecretHolder": t.proxy(
                renames["SimpleSecretHolderProtoIn"]
            ).optional(),
            "gaiaUser": t.proxy(renames["GaiaUserProtoIn"]).optional(),
            "youtubeUser": t.proxy(renames["YoutubeUserProtoIn"]).optional(),
            "socialGraphNode": t.proxy(renames["SocialGraphNodeProtoIn"]).optional(),
            "event": t.proxy(renames["EventProtoIn"]).optional(),
            "capTokenHolder": t.proxy(renames["CapTokenHolderProtoIn"]).optional(),
            "signingKeyPossessor": t.proxy(
                renames["SigningKeyPossessorProtoIn"]
            ).optional(),
            "host": t.proxy(renames["HostProtoIn"]).optional(),
            "ldapGroup": t.proxy(renames["LdapGroupProtoIn"]).optional(),
        }
    ).named(renames["PrincipalProtoIn"])
    types["PrincipalProtoOut"] = t.struct(
        {
            "mdbUser": t.proxy(renames["MdbUserProtoOut"]).optional(),
            "gaiaGroup": t.proxy(renames["GaiaGroupProtoOut"]).optional(),
            "oauthConsumer": t.proxy(renames["OAuthConsumerProtoOut"]).optional(),
            "rbacRole": t.proxy(renames["RbacRoleProtoOut"]).optional(),
            "scope": t.string().optional(),
            "rbacSubject": t.proxy(renames["RbacSubjectProtoOut"]).optional(),
            "mdbGroup": t.proxy(renames["MdbGroupProtoOut"]).optional(),
            "postiniUser": t.proxy(renames["PostiniUserProtoOut"]).optional(),
            "circle": t.proxy(renames["CircleProtoOut"]).optional(),
            "zwiebackSession": t.proxy(renames["ZwiebackSessionProtoOut"]).optional(),
            "contactGroup": t.proxy(renames["ContactGroupProtoOut"]).optional(),
            "emailOwner": t.proxy(renames["EmailOwnerProtoOut"]).optional(),
            "allAuthenticatedUsers": t.proxy(
                renames["AllAuthenticatedUsersProtoOut"]
            ).optional(),
            "square": t.proxy(renames["SquareProtoOut"]).optional(),
            "chat": t.proxy(renames["ChatProtoOut"]).optional(),
            "cloudPrincipal": t.proxy(renames["CloudPrincipalProtoOut"]).optional(),
            "ldapUser": t.proxy(renames["LdapUserProtoOut"]).optional(),
            "resourceRole": t.proxy(renames["ResourceRoleProtoOut"]).optional(),
            "simpleSecretHolder": t.proxy(
                renames["SimpleSecretHolderProtoOut"]
            ).optional(),
            "gaiaUser": t.proxy(renames["GaiaUserProtoOut"]).optional(),
            "youtubeUser": t.proxy(renames["YoutubeUserProtoOut"]).optional(),
            "socialGraphNode": t.proxy(renames["SocialGraphNodeProtoOut"]).optional(),
            "event": t.proxy(renames["EventProtoOut"]).optional(),
            "capTokenHolder": t.proxy(renames["CapTokenHolderProtoOut"]).optional(),
            "signingKeyPossessor": t.proxy(
                renames["SigningKeyPossessorProtoOut"]
            ).optional(),
            "host": t.proxy(renames["HostProtoOut"]).optional(),
            "ldapGroup": t.proxy(renames["LdapGroupProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrincipalProtoOut"])
    types["CardActionIn"] = t.struct(
        {"onClick": t.proxy(renames["OnClickIn"]), "actionLabel": t.string().optional()}
    ).named(renames["CardActionIn"])
    types["CardActionOut"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickOut"]),
            "actionLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardActionOut"])
    types["ReferenceIn"] = t.struct(
        {
            "hash": t.string(),
            "size": t.string(),
            "name": t.string().optional(),
            "blobId": t.string(),
            "contentType": t.string(),
            "key": t.string().optional(),
        }
    ).named(renames["ReferenceIn"])
    types["ReferenceOut"] = t.struct(
        {
            "hash": t.string(),
            "size": t.string(),
            "name": t.string().optional(),
            "blobId": t.string(),
            "contentType": t.string(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceOut"])
    types["DlpScanSummaryIn"] = t.struct(
        {
            "dlpAction": t.proxy(renames["DlpActionIn"]),
            "scanId": t.string().optional(),
            "scanOutcome": t.string().optional(),
            "scanNotApplicableForContext": t.boolean().optional(),
        }
    ).named(renames["DlpScanSummaryIn"])
    types["DlpScanSummaryOut"] = t.struct(
        {
            "dlpAction": t.proxy(renames["DlpActionOut"]),
            "scanId": t.string().optional(),
            "scanOutcome": t.string().optional(),
            "scanNotApplicableForContext": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpScanSummaryOut"])
    types["AppsDynamiteSharedOrganizationInfoCustomerInfoIn"] = t.struct(
        {"customerId": t.proxy(renames["CustomerIdIn"])}
    ).named(renames["AppsDynamiteSharedOrganizationInfoCustomerInfoIn"])
    types["AppsDynamiteSharedOrganizationInfoCustomerInfoOut"] = t.struct(
        {
            "customerId": t.proxy(renames["CustomerIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedOrganizationInfoCustomerInfoOut"])
    types["CaribouAttributeValueIn"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "longValue": t.string(),
            "rawByteValue": t.string().optional(),
            "intValue": t.integer(),
            "stringValue": t.string(),
        }
    ).named(renames["CaribouAttributeValueIn"])
    types["CaribouAttributeValueOut"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "longValue": t.string(),
            "rawByteValue": t.string().optional(),
            "intValue": t.integer(),
            "stringValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaribouAttributeValueOut"])
    types["AppsDynamiteV1ApiCompatV1FieldIn"] = t.struct(
        {
            "value": t.string().optional(),
            "title": t.string().optional(),
            "short": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1FieldIn"])
    types["AppsDynamiteV1ApiCompatV1FieldOut"] = t.struct(
        {
            "value": t.string().optional(),
            "title": t.string().optional(),
            "short": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1FieldOut"])
    types["SearchResultIn"] = t.struct(
        {
            "url": t.string().optional(),
            "clusteredResults": t.array(t.proxy(renames["SearchResultIn"])).optional(),
            "debugInfo": t.proxy(renames["ResultDebugInfoIn"]).optional(),
            "metadata": t.proxy(renames["MetadataIn"]).optional(),
            "title": t.string().optional(),
            "snippet": t.proxy(renames["SnippetIn"]).optional(),
        }
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "url": t.string().optional(),
            "clusteredResults": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "debugInfo": t.proxy(renames["ResultDebugInfoOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "title": t.string().optional(),
            "snippet": t.proxy(renames["SnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["AppsDynamiteSharedMessageInfoIn"] = t.struct(
        {
            "messageType": t.string().optional(),
            "topicReadTimeUsec": t.string().optional(),
            "messageId": t.proxy(renames["MessageIdIn"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageInfoIn"])
    types["AppsDynamiteSharedMessageInfoOut"] = t.struct(
        {
            "messageType": t.string().optional(),
            "topicReadTimeUsec": t.string().optional(),
            "messageId": t.proxy(renames["MessageIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageInfoOut"])
    types["SearchApplicationSessionStatsIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "searchSessionsCount": t.string().optional(),
        }
    ).named(renames["SearchApplicationSessionStatsIn"])
    types["SearchApplicationSessionStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "searchSessionsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationSessionStatsOut"])
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
    types["ImageKeyValueIn"] = t.struct(
        {
            "text": t.string(),
            "icon": t.string(),
            "onClick": t.proxy(renames["OnClickIn"]),
            "iconUrl": t.string(),
        }
    ).named(renames["ImageKeyValueIn"])
    types["ImageKeyValueOut"] = t.struct(
        {
            "text": t.string(),
            "icon": t.string(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "iconUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageKeyValueOut"])
    types["AppsDynamiteStorageButtonListIn"] = t.struct(
        {"buttons": t.array(t.proxy(renames["AppsDynamiteStorageButtonIn"]))}
    ).named(renames["AppsDynamiteStorageButtonListIn"])
    types["AppsDynamiteStorageButtonListOut"] = t.struct(
        {
            "buttons": t.array(t.proxy(renames["AppsDynamiteStorageButtonOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonListOut"])
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
    types["DoublePropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["DoubleOperatorOptionsIn"]).optional()}
    ).named(renames["DoublePropertyOptionsIn"])
    types["DoublePropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["DoubleOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoublePropertyOptionsOut"])
    types["GSuitePrincipalIn"] = t.struct(
        {
            "gsuiteGroupEmail": t.string().optional(),
            "gsuiteUserEmail": t.string().optional(),
            "gsuiteDomain": t.boolean().optional(),
        }
    ).named(renames["GSuitePrincipalIn"])
    types["GSuitePrincipalOut"] = t.struct(
        {
            "gsuiteGroupEmail": t.string().optional(),
            "gsuiteUserEmail": t.string().optional(),
            "gsuiteDomain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GSuitePrincipalOut"])
    types["AppsDynamiteSharedRetentionSettingsIn"] = t.struct(
        {"state": t.string().optional(), "expiryTimestamp": t.string().optional()}
    ).named(renames["AppsDynamiteSharedRetentionSettingsIn"])
    types["AppsDynamiteSharedRetentionSettingsOut"] = t.struct(
        {
            "state": t.string().optional(),
            "expiryTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedRetentionSettingsOut"])
    types["CardIn"] = t.struct(
        {
            "header": t.proxy(renames["CardHeaderIn"]),
            "peekCardHeader": t.proxy(renames["CardHeaderIn"]).optional(),
            "displayStyle": t.string(),
            "name": t.string().optional(),
            "cardActions": t.array(t.proxy(renames["CardActionIn"])),
            "fixedFooter": t.proxy(renames["FixedFooterIn"]),
            "sections": t.array(t.proxy(renames["SectionIn"])),
        }
    ).named(renames["CardIn"])
    types["CardOut"] = t.struct(
        {
            "header": t.proxy(renames["CardHeaderOut"]),
            "peekCardHeader": t.proxy(renames["CardHeaderOut"]).optional(),
            "displayStyle": t.string(),
            "name": t.string().optional(),
            "cardActions": t.array(t.proxy(renames["CardActionOut"])),
            "fixedFooter": t.proxy(renames["FixedFooterOut"]),
            "sections": t.array(t.proxy(renames["SectionOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardOut"])
    types["AppsDynamiteStorageOpenLinkAppUriIn"] = t.struct(
        {
            "iosUri": t.string().optional(),
            "androidIntent": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIntentIn"]
            ).optional(),
            "companionUri": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIn"])
    types["AppsDynamiteStorageOpenLinkAppUriOut"] = t.struct(
        {
            "iosUri": t.string().optional(),
            "androidIntent": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIntentOut"]
            ).optional(),
            "companionUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriOut"])
    types["ResultDisplayMetadataIn"] = t.struct(
        {
            "objectTypeLabel": t.string().optional(),
            "metalines": t.array(t.proxy(renames["ResultDisplayLineIn"])).optional(),
        }
    ).named(renames["ResultDisplayMetadataIn"])
    types["ResultDisplayMetadataOut"] = t.struct(
        {
            "objectTypeLabel": t.string().optional(),
            "metalines": t.array(t.proxy(renames["ResultDisplayLineOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayMetadataOut"])
    types["FormatMetadataIn"] = t.struct(
        {"formatType": t.string().optional(), "fontColor": t.integer().optional()}
    ).named(renames["FormatMetadataIn"])
    types["FormatMetadataOut"] = t.struct(
        {
            "formatType": t.string().optional(),
            "fontColor": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatMetadataOut"])
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
    types["MessageParentIdIn"] = t.struct(
        {"topicId": t.proxy(renames["TopicIdIn"]).optional()}
    ).named(renames["MessageParentIdIn"])
    types["MessageParentIdOut"] = t.struct(
        {
            "topicId": t.proxy(renames["TopicIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageParentIdOut"])
    types["HistoryRecordIn"] = t.struct(
        {
            "type": t.string(),
            "threadUpdate": t.proxy(renames["ThreadUpdateIn"]),
            "labelUpdate": t.proxy(renames["LabelUpdateIn"]),
            "clientContext": t.proxy(renames["ClientContextIn"]).optional(),
            "recordId": t.string().optional(),
            "txnDebugInfo": t.proxy(renames["TransactionDebugInfoIn"]),
            "filterUpdate": t.proxy(renames["FilterUpdateIn"]),
            "imapUpdate": t.proxy(renames["ImapUpdateIn"]),
            "prefUpdate": t.proxy(renames["PrefUpdateIn"]),
            "transactionContext": t.proxy(renames["TransactionContextIn"]).optional(),
        }
    ).named(renames["HistoryRecordIn"])
    types["HistoryRecordOut"] = t.struct(
        {
            "type": t.string(),
            "threadUpdate": t.proxy(renames["ThreadUpdateOut"]),
            "labelUpdate": t.proxy(renames["LabelUpdateOut"]),
            "clientContext": t.proxy(renames["ClientContextOut"]).optional(),
            "recordId": t.string().optional(),
            "txnDebugInfo": t.proxy(renames["TransactionDebugInfoOut"]),
            "filterUpdate": t.proxy(renames["FilterUpdateOut"]),
            "imapUpdate": t.proxy(renames["ImapUpdateOut"]),
            "prefUpdate": t.proxy(renames["PrefUpdateOut"]),
            "transactionContext": t.proxy(renames["TransactionContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryRecordOut"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataIn"] = t.struct(
        {
            "eventCreation": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn"]
            ).optional(),
            "calendarEvent": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn"]
            ),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataIn"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataOut"] = t.struct(
        {
            "eventCreation": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut"]
            ).optional(),
            "calendarEvent": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataOut"])
    types["AppsDynamiteV1ApiCompatV1AttachmentIn"] = t.struct(
        {
            "thumb_url": t.string().optional(),
            "pretext": t.string().optional(),
            "callback_id": t.string().optional(),
            "color": t.string().optional(),
            "mrkdwn_in": t.array(t.string()).optional(),
            "author_name": t.string().optional(),
            "attachment_type": t.string().optional(),
            "image_url": t.string().optional(),
            "author_link": t.string().optional(),
            "fallback": t.string().optional(),
            "text": t.string().optional(),
            "footer": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1ActionIn"])
            ).optional(),
            "ts": t.integer().optional(),
            "title": t.string().optional(),
            "author_icon": t.string().optional(),
            "title_link": t.string().optional(),
            "footer_icon": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1FieldIn"])
            ).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1AttachmentIn"])
    types["AppsDynamiteV1ApiCompatV1AttachmentOut"] = t.struct(
        {
            "thumb_url": t.string().optional(),
            "pretext": t.string().optional(),
            "callback_id": t.string().optional(),
            "color": t.string().optional(),
            "mrkdwn_in": t.array(t.string()).optional(),
            "author_name": t.string().optional(),
            "attachment_type": t.string().optional(),
            "image_url": t.string().optional(),
            "author_link": t.string().optional(),
            "fallback": t.string().optional(),
            "text": t.string().optional(),
            "footer": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1ActionOut"])
            ).optional(),
            "ts": t.integer().optional(),
            "title": t.string().optional(),
            "author_icon": t.string().optional(),
            "title_link": t.string().optional(),
            "footer_icon": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1FieldOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1AttachmentOut"])
    types["DatePropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["DateOperatorOptionsIn"]).optional()}
    ).named(renames["DatePropertyOptionsIn"])
    types["DatePropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["DateOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatePropertyOptionsOut"])
    types["AppsDynamiteSharedTasksAnnotationDataCreationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCreationIn"])
    types["AppsDynamiteSharedTasksAnnotationDataCreationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCreationOut"])
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
    types["AppsDynamiteStorageActionIn"] = t.struct(
        {
            "interaction": t.string(),
            "loadIndicator": t.string(),
            "parameters": t.array(
                t.proxy(renames["AppsDynamiteStorageActionActionParameterIn"])
            ).optional(),
            "persistValues": t.boolean().optional(),
            "function": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageActionIn"])
    types["AppsDynamiteStorageActionOut"] = t.struct(
        {
            "interaction": t.string(),
            "loadIndicator": t.string(),
            "parameters": t.array(
                t.proxy(renames["AppsDynamiteStorageActionActionParameterOut"])
            ).optional(),
            "persistValues": t.boolean().optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageActionOut"])
    types["ColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "alpha": t.number().optional(),
            "green": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "alpha": t.number().optional(),
            "green": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["HangoutVideoEventMetadataIn"] = t.struct(
        {"hangoutVideoType": t.string()}
    ).named(renames["HangoutVideoEventMetadataIn"])
    types["HangoutVideoEventMetadataOut"] = t.struct(
        {
            "hangoutVideoType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutVideoEventMetadataOut"])
    types["ListQuerySourcesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string(),
            "sources": t.array(t.proxy(renames["QuerySourceIn"])),
        }
    ).named(renames["ListQuerySourcesResponseIn"])
    types["ListQuerySourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string(),
            "sources": t.array(t.proxy(renames["QuerySourceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQuerySourcesResponseOut"])
    types["AppsDynamiteSharedAssistantAnnotationDataIn"] = t.struct(
        {
            "unfulfillable": t.proxy(
                renames["AppsDynamiteSharedAssistantUnfulfillableRequestIn"]
            ).optional(),
            "suggestion": t.proxy(
                renames["AppsDynamiteSharedAssistantSuggestionIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantAnnotationDataIn"])
    types["AppsDynamiteSharedAssistantAnnotationDataOut"] = t.struct(
        {
            "unfulfillable": t.proxy(
                renames["AppsDynamiteSharedAssistantUnfulfillableRequestOut"]
            ).optional(),
            "suggestion": t.proxy(
                renames["AppsDynamiteSharedAssistantSuggestionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantAnnotationDataOut"])
    types["UpdateBccRecipientsIn"] = t.struct(
        {"bccRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateBccRecipientsIn"])
    types["UpdateBccRecipientsOut"] = t.struct(
        {
            "bccRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBccRecipientsOut"])
    types["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut"])
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
    types["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"])
    types["GoogleChatV1WidgetMarkupImageButtonIn"] = t.struct(
        {
            "icon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "name": t.string().optional(),
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageButtonIn"])
    types["GoogleChatV1WidgetMarkupImageButtonOut"] = t.struct(
        {
            "icon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "name": t.string().optional(),
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageButtonOut"])
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
    types["AppsDynamiteSharedUserBlockRelationshipIn"] = t.struct(
        {"hasBlockedRequester": t.boolean(), "isBlockedByRequester": t.boolean()}
    ).named(renames["AppsDynamiteSharedUserBlockRelationshipIn"])
    types["AppsDynamiteSharedUserBlockRelationshipOut"] = t.struct(
        {
            "hasBlockedRequester": t.boolean(),
            "isBlockedByRequester": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedUserBlockRelationshipOut"])
    types["MatchInfoIn"] = t.struct(
        {"matchingImageReferenceKey": t.array(t.string()).optional()}
    ).named(renames["MatchInfoIn"])
    types["MatchInfoOut"] = t.struct(
        {
            "matchingImageReferenceKey": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchInfoOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["UpdateDataSourceRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "source": t.proxy(renames["DataSourceIn"]),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestIn"])
    types["UpdateDataSourceRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "source": t.proxy(renames["DataSourceOut"]),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestOut"])
    types["ImageComponentIn"] = t.struct(
        {
            "cropStyle": t.proxy(renames["ImageCropStyleIn"]),
            "borderStyle": t.proxy(renames["BorderStyleIn"]),
            "altText": t.string(),
            "imageUrl": t.string(),
        }
    ).named(renames["ImageComponentIn"])
    types["ImageComponentOut"] = t.struct(
        {
            "cropStyle": t.proxy(renames["ImageCropStyleOut"]),
            "borderStyle": t.proxy(renames["BorderStyleOut"]),
            "altText": t.string(),
            "imageUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageComponentOut"])
    types["DebugOptionsIn"] = t.struct(
        {"enableDebugging": t.boolean().optional()}
    ).named(renames["DebugOptionsIn"])
    types["DebugOptionsOut"] = t.struct(
        {
            "enableDebugging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugOptionsOut"])
    types["AppsDynamiteStorageGridIn"] = t.struct(
        {
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleIn"]
            ).optional(),
            "columnCount": t.integer().optional(),
            "title": t.string().optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageGridGridItemIn"])
            ).optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageGridIn"])
    types["AppsDynamiteStorageGridOut"] = t.struct(
        {
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleOut"]
            ).optional(),
            "columnCount": t.integer().optional(),
            "title": t.string().optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageGridGridItemOut"])
            ).optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageGridOut"])
    types["AppsDynamiteSharedOrganizationInfoConsumerInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedOrganizationInfoConsumerInfoIn"])
    types["AppsDynamiteSharedOrganizationInfoConsumerInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedOrganizationInfoConsumerInfoOut"])
    types["CalendarClientActionMarkupIn"] = t.struct(
        {
            "addAttachmentsActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn"
                ]
            ).optional(),
            "editAttendeesActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn"
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
            "addAttachmentsActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut"
                ]
            ).optional(),
            "editAttendeesActionMarkup": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut"
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
    types["SpaceIdIn"] = t.struct({"spaceId": t.string().optional()}).named(
        renames["SpaceIdIn"]
    )
    types["SpaceIdOut"] = t.struct(
        {
            "spaceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceIdOut"])
    types["AppsDynamiteStorageDecoratedTextIn"] = t.struct(
        {
            "wrapText": t.boolean().optional(),
            "text": t.string(),
            "bottomLabel": t.string().optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "switchControl": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextSwitchControlIn"]
            ).optional(),
            "button": t.proxy(renames["AppsDynamiteStorageButtonIn"]).optional(),
            "endIcon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "startIcon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
            "topLabel": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextIn"])
    types["AppsDynamiteStorageDecoratedTextOut"] = t.struct(
        {
            "wrapText": t.boolean().optional(),
            "text": t.string(),
            "bottomLabel": t.string().optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "switchControl": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextSwitchControlOut"]
            ).optional(),
            "button": t.proxy(renames["AppsDynamiteStorageButtonOut"]).optional(),
            "endIcon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "startIcon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "topLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextOut"])
    types["SearchResponseIn"] = t.struct(
        {
            "resultCountExact": t.string().optional(),
            "facetResults": t.array(t.proxy(renames["FacetResultIn"])).optional(),
            "results": t.array(t.proxy(renames["SearchResultIn"])).optional(),
            "hasMoreResults": t.boolean().optional(),
            "queryInterpretation": t.proxy(renames["QueryInterpretationIn"]).optional(),
            "spellResults": t.array(t.proxy(renames["SpellResultIn"])).optional(),
            "resultCountEstimate": t.string().optional(),
            "resultCounts": t.proxy(renames["ResultCountsIn"]).optional(),
            "structuredResults": t.array(
                t.proxy(renames["StructuredResultIn"])
            ).optional(),
            "debugInfo": t.proxy(renames["ResponseDebugInfoIn"]).optional(),
            "errorInfo": t.proxy(renames["ErrorInfoIn"]).optional(),
        }
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "resultCountExact": t.string().optional(),
            "facetResults": t.array(t.proxy(renames["FacetResultOut"])).optional(),
            "results": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "hasMoreResults": t.boolean().optional(),
            "queryInterpretation": t.proxy(
                renames["QueryInterpretationOut"]
            ).optional(),
            "spellResults": t.array(t.proxy(renames["SpellResultOut"])).optional(),
            "resultCountEstimate": t.string().optional(),
            "resultCounts": t.proxy(renames["ResultCountsOut"]).optional(),
            "structuredResults": t.array(
                t.proxy(renames["StructuredResultOut"])
            ).optional(),
            "debugInfo": t.proxy(renames["ResponseDebugInfoOut"]).optional(),
            "errorInfo": t.proxy(renames["ErrorInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
    types["InitializeCustomerRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InitializeCustomerRequestIn"]
    )
    types["InitializeCustomerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InitializeCustomerRequestOut"])
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
    types["IncomingWebhookChangedMetadataIn"] = t.struct(
        {
            "obfuscatedIncomingWebhookId": t.string().optional(),
            "oldIncomingWebhookName": t.string().optional(),
            "initiatorId": t.proxy(renames["UserIdIn"]).optional(),
            "incomingWebhookName": t.string().optional(),
            "type": t.string().optional(),
            "initiatorProfile": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["IncomingWebhookChangedMetadataIn"])
    types["IncomingWebhookChangedMetadataOut"] = t.struct(
        {
            "obfuscatedIncomingWebhookId": t.string().optional(),
            "oldIncomingWebhookName": t.string().optional(),
            "initiatorId": t.proxy(renames["UserIdOut"]).optional(),
            "incomingWebhookName": t.string().optional(),
            "type": t.string().optional(),
            "initiatorProfile": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncomingWebhookChangedMetadataOut"])
    types["BroadcastSessionInfoIn"] = t.struct(
        {
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
            "ingestionId": t.string().optional(),
            "broadcastSessionId": t.string().optional(),
        }
    ).named(renames["BroadcastSessionInfoIn"])
    types["BroadcastSessionInfoOut"] = t.struct(
        {
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "broadcastStats": t.proxy(renames["BroadcastStatsOut"]).optional(),
            "ingestionId": t.string().optional(),
            "broadcastSessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BroadcastSessionInfoOut"])
    types["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"] = t.struct(
        {"oldAssignee": t.proxy(renames["UserIdIn"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"] = t.struct(
        {
            "oldAssignee": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"])
    types["SigningKeyPossessorProtoIn"] = t.struct(
        {
            "keymasterKeyType": t.integer().optional(),
            "serializedVerificationKey": t.string().optional(),
            "serializedVerificationKeyset": t.string().optional(),
        }
    ).named(renames["SigningKeyPossessorProtoIn"])
    types["SigningKeyPossessorProtoOut"] = t.struct(
        {
            "keymasterKeyType": t.integer().optional(),
            "serializedVerificationKey": t.string().optional(),
            "serializedVerificationKeyset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SigningKeyPossessorProtoOut"])
    types["AppsDynamiteStorageCardCardHeaderIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "imageUrl": t.string().optional(),
            "imageAltText": t.string().optional(),
            "imageType": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageCardCardHeaderIn"])
    types["AppsDynamiteStorageCardCardHeaderOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "imageUrl": t.string().optional(),
            "imageAltText": t.string().optional(),
            "imageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardCardHeaderOut"])
    types["PeopleSuggestionIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["PeopleSuggestionIn"])
    types["PeopleSuggestionOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeopleSuggestionOut"])
    types["LinkDataIn"] = t.struct(
        {
            "displayUrl": t.string().optional(),
            "linkTarget": t.string().optional(),
            "attachment": t.proxy(
                renames["SocialCommonAttachmentAttachmentIn"]
            ).optional(),
            "title": t.string().optional(),
            "linkType": t.string().optional(),
            "attachmentRenderHint": t.string().optional(),
        }
    ).named(renames["LinkDataIn"])
    types["LinkDataOut"] = t.struct(
        {
            "displayUrl": t.string().optional(),
            "linkTarget": t.string().optional(),
            "attachment": t.proxy(
                renames["SocialCommonAttachmentAttachmentOut"]
            ).optional(),
            "title": t.string().optional(),
            "linkType": t.string().optional(),
            "attachmentRenderHint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkDataOut"])
    types["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"])
    types["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"])
    types["CollaborationIn"] = t.struct(
        {
            "initiator": t.proxy(renames["UserDisplayInfoIn"]).optional(),
            "attachmentId": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["CollaborationIn"])
    types["CollaborationOut"] = t.struct(
        {
            "initiator": t.proxy(renames["UserDisplayInfoOut"]).optional(),
            "attachmentId": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollaborationOut"])
    types["DoubleValuesIn"] = t.struct({"values": t.array(t.number())}).named(
        renames["DoubleValuesIn"]
    )
    types["DoubleValuesOut"] = t.struct(
        {
            "values": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleValuesOut"])
    types["TaskActionMarkupIn"] = t.struct({"reloadTasks": t.boolean()}).named(
        renames["TaskActionMarkupIn"]
    )
    types["TaskActionMarkupOut"] = t.struct(
        {
            "reloadTasks": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskActionMarkupOut"])
    types["IntegerOperatorOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
        }
    ).named(renames["IntegerOperatorOptionsIn"])
    types["IntegerOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerOperatorOptionsOut"])
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
    types["ReadReceiptsSettingsUpdatedMetadataIn"] = t.struct(
        {"readReceiptsEnabled": t.boolean().optional()}
    ).named(renames["ReadReceiptsSettingsUpdatedMetadataIn"])
    types["ReadReceiptsSettingsUpdatedMetadataOut"] = t.struct(
        {
            "readReceiptsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadReceiptsSettingsUpdatedMetadataOut"])
    types["BotResponseIn"] = t.struct(
        {
            "setupUrl": t.string().optional(),
            "botId": t.proxy(renames["UserIdIn"]),
            "requiredAction": t.string(),
            "responseType": t.string(),
        }
    ).named(renames["BotResponseIn"])
    types["BotResponseOut"] = t.struct(
        {
            "setupUrl": t.string().optional(),
            "botId": t.proxy(renames["UserIdOut"]),
            "requiredAction": t.string(),
            "responseType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BotResponseOut"])
    types["ValueFilterIn"] = t.struct(
        {
            "value": t.proxy(renames["ValueIn"]).optional(),
            "operatorName": t.string().optional(),
        }
    ).named(renames["ValueFilterIn"])
    types["ValueFilterOut"] = t.struct(
        {
            "value": t.proxy(renames["ValueOut"]).optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueFilterOut"])
    types["GoogleDocsResultInfoIn"] = t.struct(
        {
            "encryptedId": t.string().optional(),
            "attachmentSha1": t.string().optional(),
            "cosmoId": t.proxy(renames["IdIn"]).optional(),
            "mimeType": t.string().optional(),
            "cosmoNameSpace": t.integer().optional(),
            "shareScope": t.proxy(renames["ShareScopeIn"]).optional(),
        }
    ).named(renames["GoogleDocsResultInfoIn"])
    types["GoogleDocsResultInfoOut"] = t.struct(
        {
            "encryptedId": t.string().optional(),
            "attachmentSha1": t.string().optional(),
            "cosmoId": t.proxy(renames["IdOut"]).optional(),
            "mimeType": t.string().optional(),
            "cosmoNameSpace": t.integer().optional(),
            "shareScope": t.proxy(renames["ShareScopeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDocsResultInfoOut"])
    types["AppsDynamiteStorageOpenLinkAppUriIntentIn"] = t.struct(
        {
            "extraData": t.array(
                t.proxy(renames["AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn"])
            ).optional(),
            "intentAction": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIntentIn"])
    types["AppsDynamiteStorageOpenLinkAppUriIntentOut"] = t.struct(
        {
            "extraData": t.array(
                t.proxy(renames["AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut"])
            ).optional(),
            "intentAction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIntentOut"])
    types["StructuredResultIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["StructuredResultIn"])
    types["StructuredResultOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredResultOut"])
    types["AddonComposeUiActionMarkupIn"] = t.struct({"type": t.string()}).named(
        renames["AddonComposeUiActionMarkupIn"]
    )
    types["AddonComposeUiActionMarkupOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddonComposeUiActionMarkupOut"])
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
    types["SelectionItemIn"] = t.struct(
        {
            "text": t.string().optional(),
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["SelectionItemIn"])
    types["SelectionItemOut"] = t.struct(
        {
            "text": t.string().optional(),
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionItemOut"])
    types["DynamiteMessagesScoringInfoIn"] = t.struct(
        {
            "commonCountToMembershipCountRatio": t.number(),
            "joinedSpaceAffinityScore": t.number(),
            "messageAgeInDays": t.number(),
            "commonCountToContactListCountRatio": t.number(),
            "commonContactCount": t.string(),
            "spaceId": t.string(),
            "messageSenderAffinityScore": t.number(),
            "crowdingMultiplier": t.number(),
            "finalScore": t.number(),
            "unjoinedSpaceAffinityScore": t.number(),
            "lastReadTimestampAgeInDays": t.number(),
            "creatorGaiaId": t.string(),
            "dasContactCount": t.string(),
            "creatorInSearcherContactList": t.boolean(),
            "topicalityScore": t.number(),
            "freshnessScore": t.number(),
            "spaceMembershipCount": t.string(),
        }
    ).named(renames["DynamiteMessagesScoringInfoIn"])
    types["DynamiteMessagesScoringInfoOut"] = t.struct(
        {
            "commonCountToMembershipCountRatio": t.number(),
            "joinedSpaceAffinityScore": t.number(),
            "messageAgeInDays": t.number(),
            "commonCountToContactListCountRatio": t.number(),
            "commonContactCount": t.string(),
            "spaceId": t.string(),
            "messageSenderAffinityScore": t.number(),
            "crowdingMultiplier": t.number(),
            "finalScore": t.number(),
            "unjoinedSpaceAffinityScore": t.number(),
            "lastReadTimestampAgeInDays": t.number(),
            "creatorGaiaId": t.string(),
            "dasContactCount": t.string(),
            "creatorInSearcherContactList": t.boolean(),
            "topicalityScore": t.number(),
            "freshnessScore": t.number(),
            "spaceMembershipCount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamiteMessagesScoringInfoOut"])
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
    types["YoutubeMetadataIn"] = t.struct(
        {
            "shouldNotRender": t.boolean().optional(),
            "startTime": t.integer().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["YoutubeMetadataIn"])
    types["YoutubeMetadataOut"] = t.struct(
        {
            "shouldNotRender": t.boolean().optional(),
            "startTime": t.integer().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeMetadataOut"])
    types["AppsDynamiteStorageColumnsColumnIn"] = t.struct(
        {
            "horizontalSizeStyle": t.string().optional(),
            "verticalAlignment": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageColumnsColumnWidgetsIn"])
            ).optional(),
            "horizontalAlignment": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnIn"])
    types["AppsDynamiteStorageColumnsColumnOut"] = t.struct(
        {
            "horizontalSizeStyle": t.string().optional(),
            "verticalAlignment": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageColumnsColumnWidgetsOut"])
            ).optional(),
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"] = t.struct(
        {"nudgeType": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut"] = t.struct(
        {
            "nudgeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut"])
    types["PrefUpdateIn"] = t.struct(
        {
            "preState": t.proxy(renames["FuseboxPrefUpdatePreStateIn"]),
            "prefDeleted": t.proxy(renames["PrefDeletedIn"]),
            "name": t.string().optional(),
            "prefWritten": t.proxy(renames["PrefWrittenIn"]),
        }
    ).named(renames["PrefUpdateIn"])
    types["PrefUpdateOut"] = t.struct(
        {
            "preState": t.proxy(renames["FuseboxPrefUpdatePreStateOut"]),
            "prefDeleted": t.proxy(renames["PrefDeletedOut"]),
            "name": t.string().optional(),
            "prefWritten": t.proxy(renames["PrefWrittenOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrefUpdateOut"])
    types["LabelUpdateIn"] = t.struct(
        {
            "labelDeleted": t.proxy(renames["LabelDeletedIn"]),
            "labelRenamed": t.proxy(renames["LabelRenamedIn"]),
            "labelCreated": t.proxy(renames["LabelCreatedIn"]),
            "labelId": t.string(),
            "canonicalName": t.string(),
            "labelUpdated": t.proxy(renames["LabelUpdatedIn"]),
            "syncId": t.integer(),
        }
    ).named(renames["LabelUpdateIn"])
    types["LabelUpdateOut"] = t.struct(
        {
            "labelDeleted": t.proxy(renames["LabelDeletedOut"]),
            "labelRenamed": t.proxy(renames["LabelRenamedOut"]),
            "labelCreated": t.proxy(renames["LabelCreatedOut"]),
            "labelId": t.string(),
            "canonicalName": t.string(),
            "labelUpdated": t.proxy(renames["LabelUpdatedOut"]),
            "syncId": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelUpdateOut"])
    types["DriveClientActionMarkupIn"] = t.struct(
        {"requestFileScope": t.proxy(renames["RequestFileScopeIn"])}
    ).named(renames["DriveClientActionMarkupIn"])
    types["DriveClientActionMarkupOut"] = t.struct(
        {
            "requestFileScope": t.proxy(renames["RequestFileScopeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveClientActionMarkupOut"])
    types["InviteeInfoIn"] = t.struct(
        {
            "email": t.string().optional(),
            "userId": t.proxy(renames["UserIdIn"]).optional(),
        }
    ).named(renames["InviteeInfoIn"])
    types["InviteeInfoOut"] = t.struct(
        {
            "email": t.string().optional(),
            "userId": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InviteeInfoOut"])
    types["IntegerPropertyOptionsIn"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["IntegerOperatorOptionsIn"]).optional(),
            "maximumValue": t.string().optional(),
            "minimumValue": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsIn"]
            ).optional(),
            "orderedRanking": t.string().optional(),
        }
    ).named(renames["IntegerPropertyOptionsIn"])
    types["IntegerPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["IntegerOperatorOptionsOut"]).optional(),
            "maximumValue": t.string().optional(),
            "minimumValue": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsOut"]
            ).optional(),
            "orderedRanking": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerPropertyOptionsOut"])
    types["AppsDynamiteSharedAppProfileIn"] = t.struct(
        {
            "name": t.string().optional(),
            "avatarUrl": t.string().optional(),
            "avatarEmoji": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedAppProfileIn"])
    types["AppsDynamiteSharedAppProfileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "avatarUrl": t.string().optional(),
            "avatarEmoji": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAppProfileOut"])
    types["AppsDynamiteSharedFindDocumentSuggestionIn"] = t.struct(
        {
            "showActionButtons": t.boolean().optional(),
            "documentSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedDocumentIn"])
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedFindDocumentSuggestionIn"])
    types["AppsDynamiteSharedFindDocumentSuggestionOut"] = t.struct(
        {
            "showActionButtons": t.boolean().optional(),
            "documentSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedDocumentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedFindDocumentSuggestionOut"])
    types["AppsDynamiteSharedAssistantSessionContextIn"] = t.struct(
        {"contextualSessionId": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantSessionContextIn"])
    types["AppsDynamiteSharedAssistantSessionContextOut"] = t.struct(
        {
            "contextualSessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSessionContextOut"])
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
    types["DriveTimeSpanRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveTimeSpanRestrictIn"]
    )
    types["DriveTimeSpanRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveTimeSpanRestrictOut"])
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
    types["FilterDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilterDeletedIn"]
    )
    types["FilterDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FilterDeletedOut"])
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
    types["GetSearchApplicationUserStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["SearchApplicationUserStatsIn"]))}
    ).named(renames["GetSearchApplicationUserStatsResponseIn"])
    types["GetSearchApplicationUserStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["SearchApplicationUserStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationUserStatsResponseOut"])
    types["TombstoneMetadataIn"] = t.struct(
        {"tombstoneType": t.string().optional()}
    ).named(renames["TombstoneMetadataIn"])
    types["TombstoneMetadataOut"] = t.struct(
        {
            "tombstoneType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TombstoneMetadataOut"])
    types["SearchApplicationIn"] = t.struct(
        {
            "defaultFacetOptions": t.array(
                t.proxy(renames["FacetOptionsIn"])
            ).optional(),
            "returnResultThumbnailUrls": t.boolean().optional(),
            "displayName": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
            "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
            "enableAuditLog": t.boolean().optional(),
            "name": t.string().optional(),
            "queryInterpretationConfig": t.proxy(
                renames["QueryInterpretationConfigIn"]
            ).optional(),
            "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
        }
    ).named(renames["SearchApplicationIn"])
    types["SearchApplicationOut"] = t.struct(
        {
            "defaultFacetOptions": t.array(
                t.proxy(renames["FacetOptionsOut"])
            ).optional(),
            "returnResultThumbnailUrls": t.boolean().optional(),
            "displayName": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "operationIds": t.array(t.string()).optional(),
            "defaultSortOptions": t.proxy(renames["SortOptionsOut"]).optional(),
            "scoringConfig": t.proxy(renames["ScoringConfigOut"]).optional(),
            "enableAuditLog": t.boolean().optional(),
            "name": t.string().optional(),
            "queryInterpretationConfig": t.proxy(
                renames["QueryInterpretationConfigOut"]
            ).optional(),
            "sourceConfig": t.array(t.proxy(renames["SourceConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationOut"])
    types["FilterCreatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilterCreatedIn"]
    )
    types["FilterCreatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FilterCreatedOut"])
    types["StreamViewerStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["StreamViewerStatsIn"])
    types["StreamViewerStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamViewerStatsOut"])
    types["ErrorMessageIn"] = t.struct(
        {"errorMessage": t.string(), "source": t.proxy(renames["SourceIn"])}
    ).named(renames["ErrorMessageIn"])
    types["ErrorMessageOut"] = t.struct(
        {
            "errorMessage": t.string(),
            "source": t.proxy(renames["SourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorMessageOut"])
    types["LdapUserProtoIn"] = t.struct({"userName": t.string()}).named(
        renames["LdapUserProtoIn"]
    )
    types["LdapUserProtoOut"] = t.struct(
        {"userName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LdapUserProtoOut"])
    types["AppsDynamiteSharedTextSegmentIn"] = t.struct(
        {"startIndex": t.integer().optional(), "length": t.integer().optional()}
    ).named(renames["AppsDynamiteSharedTextSegmentIn"])
    types["AppsDynamiteSharedTextSegmentOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "length": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTextSegmentOut"])
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
    types["OnClickIn"] = t.struct(
        {
            "action": t.proxy(renames["FormActionIn"]),
            "link": t.string().optional(),
            "openLink": t.proxy(renames["OpenLinkIn"]),
            "openLinkAction": t.proxy(renames["FormActionIn"]).optional(),
        }
    ).named(renames["OnClickIn"])
    types["OnClickOut"] = t.struct(
        {
            "action": t.proxy(renames["FormActionOut"]),
            "link": t.string().optional(),
            "openLink": t.proxy(renames["OpenLinkOut"]),
            "openLinkAction": t.proxy(renames["FormActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnClickOut"])
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
    types["UploadMetadataIn"] = t.struct(
        {
            "videoReference": t.proxy(
                renames["AppsDynamiteSharedVideoReferenceIn"]
            ).optional(),
            "virusScanResult": t.string().optional(),
            "attachmentToken": t.string().optional(),
            "dlpMetricsMetadata": t.proxy(
                renames["AppsDynamiteSharedDlpMetricsMetadataIn"]
            ).optional(),
            "contentType": t.string().optional(),
            "localId": t.string().optional(),
            "clonedDriveAction": t.string().optional(),
            "contentName": t.string().optional(),
            "latestVirusScanTimestamp": t.string().optional(),
            "backendUploadMetadata": t.proxy(
                renames["AppsDynamiteSharedBackendUploadMetadataIn"]
            ).optional(),
            "clonedDriveId": t.string().optional(),
            "clonedAuthorizedItemId": t.proxy(renames["AuthorizedItemIdIn"]).optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionIn"]
            ).optional(),
        }
    ).named(renames["UploadMetadataIn"])
    types["UploadMetadataOut"] = t.struct(
        {
            "videoReference": t.proxy(
                renames["AppsDynamiteSharedVideoReferenceOut"]
            ).optional(),
            "virusScanResult": t.string().optional(),
            "attachmentToken": t.string().optional(),
            "dlpMetricsMetadata": t.proxy(
                renames["AppsDynamiteSharedDlpMetricsMetadataOut"]
            ).optional(),
            "contentType": t.string().optional(),
            "localId": t.string().optional(),
            "clonedDriveAction": t.string().optional(),
            "contentName": t.string().optional(),
            "latestVirusScanTimestamp": t.string().optional(),
            "backendUploadMetadata": t.proxy(
                renames["AppsDynamiteSharedBackendUploadMetadataOut"]
            ).optional(),
            "clonedDriveId": t.string().optional(),
            "clonedAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdOut"]
            ).optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadMetadataOut"])
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
    types["AppsDynamiteSharedReactionIn"] = t.struct(
        {
            "count": t.integer().optional(),
            "createTimestamp": t.string().optional(),
            "currentUserParticipated": t.boolean().optional(),
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiIn"]),
        }
    ).named(renames["AppsDynamiteSharedReactionIn"])
    types["AppsDynamiteSharedReactionOut"] = t.struct(
        {
            "count": t.integer().optional(),
            "createTimestamp": t.string().optional(),
            "currentUserParticipated": t.boolean().optional(),
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedReactionOut"])
    types["ItemMetadataIn"] = t.struct(
        {
            "objectType": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeIn"])
            ).optional(),
            "mimeType": t.string().optional(),
            "containerName": t.string().optional(),
            "hash": t.string().optional(),
            "sourceRepositoryUrl": t.string().optional(),
            "keywords": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "interactions": t.array(t.proxy(renames["InteractionIn"])).optional(),
            "searchQualityMetadata": t.proxy(
                renames["SearchQualityMetadataIn"]
            ).optional(),
        }
    ).named(renames["ItemMetadataIn"])
    types["ItemMetadataOut"] = t.struct(
        {
            "objectType": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeOut"])
            ).optional(),
            "mimeType": t.string().optional(),
            "containerName": t.string().optional(),
            "hash": t.string().optional(),
            "sourceRepositoryUrl": t.string().optional(),
            "keywords": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "interactions": t.array(t.proxy(renames["InteractionOut"])).optional(),
            "searchQualityMetadata": t.proxy(
                renames["SearchQualityMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemMetadataOut"])
    types["AppsDynamiteSharedTasksAnnotationDataIn"] = t.struct(
        {
            "taskId": t.string().optional(),
            "taskProperties": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"]
            ).optional(),
            "assigneeChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"]
            ),
            "deletionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"]
            ),
            "creation": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCreationIn"]
            ),
            "userDefinedMessage": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"]
            ),
            "completionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"]
            ),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataIn"])
    types["AppsDynamiteSharedTasksAnnotationDataOut"] = t.struct(
        {
            "taskId": t.string().optional(),
            "taskProperties": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"]
            ).optional(),
            "assigneeChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"]
            ),
            "deletionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"]
            ),
            "creation": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCreationOut"]
            ),
            "userDefinedMessage": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"]
            ),
            "completionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataOut"])
    types["FolderIn"] = t.struct(
        {
            "message": t.array(
                t.proxy(renames["ImapsyncFolderAttributeFolderMessageIn"])
            ).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "message": t.array(
                t.proxy(renames["ImapsyncFolderAttributeFolderMessageOut"])
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["AttachmentIn"] = t.struct(
        {
            "deprecatedAddOnData": t.proxy(
                renames["ContextualAddOnMarkupIn"]
            ).optional(),
            "appId": t.proxy(renames["UserIdIn"]).optional(),
            "attachmentId": t.string().optional(),
            "slackDataImageUrlHeight": t.integer().optional(),
            "slackData": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1AttachmentIn"]
            ).optional(),
            "cardAddOnData": t.proxy(renames["AppsDynamiteStorageCardIn"]).optional(),
            "addOnData": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupIn"]
            ).optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "deprecatedAddOnData": t.proxy(
                renames["ContextualAddOnMarkupOut"]
            ).optional(),
            "appId": t.proxy(renames["UserIdOut"]).optional(),
            "attachmentId": t.string().optional(),
            "slackDataImageUrlHeight": t.integer().optional(),
            "slackData": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1AttachmentOut"]
            ).optional(),
            "cardAddOnData": t.proxy(renames["AppsDynamiteStorageCardOut"]).optional(),
            "addOnData": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["UnreserveItemsRequestIn"] = t.struct(
        {
            "connectorName": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "queue": t.string().optional(),
        }
    ).named(renames["UnreserveItemsRequestIn"])
    types["UnreserveItemsRequestOut"] = t.struct(
        {
            "connectorName": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "queue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnreserveItemsRequestOut"])
    types["GatewaySipAccessIn"] = t.struct(
        {"uri": t.string().optional(), "sipAccessCode": t.string().optional()}
    ).named(renames["GatewaySipAccessIn"])
    types["GatewaySipAccessOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "sipAccessCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySipAccessOut"])
    types["UpdateDraftActionMarkupIn"] = t.struct(
        {
            "updateSubject": t.proxy(renames["UpdateSubjectIn"]).optional(),
            "updateCcRecipients": t.proxy(renames["UpdateCcRecipientsIn"]).optional(),
            "updateBccRecipients": t.proxy(renames["UpdateBccRecipientsIn"]).optional(),
            "updateToRecipients": t.proxy(renames["UpdateToRecipientsIn"]).optional(),
            "updateBody": t.proxy(renames["UpdateBodyIn"]).optional(),
        }
    ).named(renames["UpdateDraftActionMarkupIn"])
    types["UpdateDraftActionMarkupOut"] = t.struct(
        {
            "updateSubject": t.proxy(renames["UpdateSubjectOut"]).optional(),
            "updateCcRecipients": t.proxy(renames["UpdateCcRecipientsOut"]).optional(),
            "updateBccRecipients": t.proxy(
                renames["UpdateBccRecipientsOut"]
            ).optional(),
            "updateToRecipients": t.proxy(renames["UpdateToRecipientsOut"]).optional(),
            "updateBody": t.proxy(renames["UpdateBodyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDraftActionMarkupOut"])
    types["BotInfoIn"] = t.struct(
        {
            "supportedUses": t.array(t.string()).optional(),
            "supportHomeScreen": t.boolean().optional(),
            "supportUrls": t.proxy(renames["SupportUrlsIn"]).optional(),
            "marketPlaceBannerUrl": t.string().optional(),
            "status": t.string().optional(),
            "botAvatarUrl": t.string().optional(),
            "appAllowlistStatus": t.string(),
            "appId": t.proxy(renames["AppIdIn"]).optional(),
            "botName": t.string().optional(),
            "description": t.string().optional(),
            "developerName": t.string().optional(),
        }
    ).named(renames["BotInfoIn"])
    types["BotInfoOut"] = t.struct(
        {
            "supportedUses": t.array(t.string()).optional(),
            "supportHomeScreen": t.boolean().optional(),
            "supportUrls": t.proxy(renames["SupportUrlsOut"]).optional(),
            "marketPlaceBannerUrl": t.string().optional(),
            "status": t.string().optional(),
            "botAvatarUrl": t.string().optional(),
            "appAllowlistStatus": t.string(),
            "appId": t.proxy(renames["AppIdOut"]).optional(),
            "botName": t.string().optional(),
            "description": t.string().optional(),
            "developerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BotInfoOut"])
    types["SquareProtoIn"] = t.struct(
        {"memberType": t.integer().optional(), "squareId": t.string().optional()}
    ).named(renames["SquareProtoIn"])
    types["SquareProtoOut"] = t.struct(
        {
            "memberType": t.integer().optional(),
            "squareId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SquareProtoOut"])
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
    types["DeleteQueueItemsRequestIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "queue": t.string().optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["DeleteQueueItemsRequestIn"])
    types["DeleteQueueItemsRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "queue": t.string().optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteQueueItemsRequestOut"])
    types["DocumentInfoIn"] = t.struct(
        {"whiteboardInfo": t.proxy(renames["WhiteboardInfoIn"]).optional()}
    ).named(renames["DocumentInfoIn"])
    types["DocumentInfoOut"] = t.struct(
        {
            "whiteboardInfo": t.proxy(renames["WhiteboardInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentInfoOut"])
    types["TransactionContextIn"] = t.struct(
        {
            "endingRecordId": t.string().optional(),
            "writeTimestampUs": t.string().optional(),
            "startingRecordId": t.string().optional(),
        }
    ).named(renames["TransactionContextIn"])
    types["TransactionContextOut"] = t.struct(
        {
            "endingRecordId": t.string().optional(),
            "writeTimestampUs": t.string().optional(),
            "startingRecordId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionContextOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"])
    types["ItemStructuredDataIn"] = t.struct(
        {
            "object": t.proxy(renames["StructuredDataObjectIn"]).optional(),
            "hash": t.string().optional(),
        }
    ).named(renames["ItemStructuredDataIn"])
    types["ItemStructuredDataOut"] = t.struct(
        {
            "object": t.proxy(renames["StructuredDataObjectOut"]).optional(),
            "hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemStructuredDataOut"])
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
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
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
    types["BroadcastAccessIn"] = t.struct(
        {"viewUrl": t.string().optional(), "accessPolicy": t.string().optional()}
    ).named(renames["BroadcastAccessIn"])
    types["BroadcastAccessOut"] = t.struct(
        {
            "viewUrl": t.string().optional(),
            "accessPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BroadcastAccessOut"])
    types["SettingsIn"] = t.struct(
        {
            "defaultAsViewer": t.boolean().optional(),
            "chatLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "accessType": t.string().optional(),
            "accessLock": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "cohostArtifactSharingEnabled": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "defaultAsViewer": t.boolean().optional(),
            "chatLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "accessType": t.string().optional(),
            "accessLock": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "cohostArtifactSharingEnabled": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
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
    types["RequestFileScopeIn"] = t.struct({"itemId": t.string()}).named(
        renames["RequestFileScopeIn"]
    )
    types["RequestFileScopeOut"] = t.struct(
        {"itemId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestFileScopeOut"])
    types["WonderCardDeleteIn"] = t.struct(
        {
            "messageMappings": t.struct({"_": t.string().optional()}).optional(),
            "msgId": t.string().optional(),
        }
    ).named(renames["WonderCardDeleteIn"])
    types["WonderCardDeleteOut"] = t.struct(
        {
            "messageMappings": t.struct({"_": t.string().optional()}).optional(),
            "msgId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WonderCardDeleteOut"])
    types["TextKeyValueIn"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickIn"]),
            "key": t.string(),
            "text": t.string(),
        }
    ).named(renames["TextKeyValueIn"])
    types["TextKeyValueOut"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickOut"]),
            "key": t.string(),
            "text": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextKeyValueOut"])
    types["EventProtoIn"] = t.struct(
        {"memberType": t.integer().optional(), "eventId": t.string().optional()}
    ).named(renames["EventProtoIn"])
    types["EventProtoOut"] = t.struct(
        {
            "memberType": t.integer().optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventProtoOut"])
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
    types["AppsDynamiteSharedMessageIntegrationPayloadIn"] = t.struct(
        {
            "projectNumber": t.string().optional(),
            "tasksMessageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"]
            ),
            "type": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageIntegrationPayloadIn"])
    types["AppsDynamiteSharedMessageIntegrationPayloadOut"] = t.struct(
        {
            "projectNumber": t.string().optional(),
            "tasksMessageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"]
            ),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageIntegrationPayloadOut"])
    types["CustomerUserStatsIn"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
        }
    ).named(renames["CustomerUserStatsIn"])
    types["CustomerUserStatsOut"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerUserStatsOut"])
    types["DriveMetadataIn"] = t.struct(
        {
            "thumbnailWidth": t.integer().optional(),
            "legacyUploadMetadata": t.proxy(
                renames["LegacyUploadMetadataIn"]
            ).optional(),
            "isOwner": t.boolean().optional(),
            "canEdit": t.boolean().optional(),
            "urlFragment": t.string().optional(),
            "encryptedResourceKey": t.string().optional(),
            "shortcutAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdIn"]
            ).optional(),
            "externalMimetype": t.string().optional(),
            "driveAction": t.string().optional(),
            "encryptedDocId": t.boolean().optional(),
            "aclFixRequest": t.proxy(renames["AclFixRequestIn"]),
            "isDownloadRestricted": t.boolean().optional(),
            "organizationDisplayName": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "wrappedResourceKey": t.proxy(renames["WrappedResourceKeyIn"]).optional(),
            "canView": t.boolean().optional(),
            "id": t.string().optional(),
            "driveState": t.string(),
            "aclFixStatus": t.proxy(renames["AclFixStatusIn"]),
            "canShare": t.boolean().optional(),
            "title": t.string().optional(),
            "mimetype": t.string().optional(),
            "thumbnailHeight": t.integer().optional(),
            "shouldNotRender": t.boolean().optional(),
        }
    ).named(renames["DriveMetadataIn"])
    types["DriveMetadataOut"] = t.struct(
        {
            "thumbnailWidth": t.integer().optional(),
            "legacyUploadMetadata": t.proxy(
                renames["LegacyUploadMetadataOut"]
            ).optional(),
            "isOwner": t.boolean().optional(),
            "canEdit": t.boolean().optional(),
            "urlFragment": t.string().optional(),
            "encryptedResourceKey": t.string().optional(),
            "shortcutAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdOut"]
            ).optional(),
            "externalMimetype": t.string().optional(),
            "driveAction": t.string().optional(),
            "embedUrl": t.proxy(renames["TrustedResourceUrlProtoOut"]).optional(),
            "encryptedDocId": t.boolean().optional(),
            "aclFixRequest": t.proxy(renames["AclFixRequestOut"]),
            "isDownloadRestricted": t.boolean().optional(),
            "organizationDisplayName": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "wrappedResourceKey": t.proxy(renames["WrappedResourceKeyOut"]).optional(),
            "canView": t.boolean().optional(),
            "id": t.string().optional(),
            "driveState": t.string(),
            "aclFixStatus": t.proxy(renames["AclFixStatusOut"]),
            "canShare": t.boolean().optional(),
            "title": t.string().optional(),
            "mimetype": t.string().optional(),
            "thumbnailHeight": t.integer().optional(),
            "shouldNotRender": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveMetadataOut"])
    types["OsVersionIn"] = t.struct(
        {
            "majorVersion": t.integer(),
            "minorVersion": t.integer(),
            "tertiaryVersion": t.integer(),
        }
    ).named(renames["OsVersionIn"])
    types["OsVersionOut"] = t.struct(
        {
            "majorVersion": t.integer(),
            "minorVersion": t.integer(),
            "tertiaryVersion": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsVersionOut"])
    types["ContentReportIn"] = t.struct(
        {
            "reporterUserId": t.proxy(renames["UserIdIn"]).optional(),
            "revisionCreateTimestamp": t.string().optional(),
            "reportJustification": t.proxy(
                renames["ContentReportJustificationIn"]
            ).optional(),
            "reportType": t.proxy(
                renames["AppsDynamiteSharedContentReportTypeIn"]
            ).optional(),
            "reportCreateTimestamp": t.string().optional(),
        }
    ).named(renames["ContentReportIn"])
    types["ContentReportOut"] = t.struct(
        {
            "reporterUserId": t.proxy(renames["UserIdOut"]).optional(),
            "revisionCreateTimestamp": t.string().optional(),
            "reportJustification": t.proxy(
                renames["ContentReportJustificationOut"]
            ).optional(),
            "reportType": t.proxy(
                renames["AppsDynamiteSharedContentReportTypeOut"]
            ).optional(),
            "reportCreateTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentReportOut"])
    types["GaiaGroupProtoIn"] = t.struct({"groupId": t.string()}).named(
        renames["GaiaGroupProtoIn"]
    )
    types["GaiaGroupProtoOut"] = t.struct(
        {"groupId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GaiaGroupProtoOut"])
    types["CapTokenHolderProtoIn"] = t.struct(
        {"tokenHmacSha1Prefix": t.string().optional()}
    ).named(renames["CapTokenHolderProtoIn"])
    types["CapTokenHolderProtoOut"] = t.struct(
        {
            "tokenHmacSha1Prefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapTokenHolderProtoOut"])
    types["PrefWrittenIn"] = t.struct({"value": t.string()}).named(
        renames["PrefWrittenIn"]
    )
    types["PrefWrittenOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PrefWrittenOut"])
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
    types["FuseboxItemIn"] = t.struct(
        {
            "triggers": t.proxy(renames["TriggersIn"]),
            "readTs": t.string().optional(),
            "references": t.proxy(renames["ReferencesIn"]).optional(),
            "history": t.proxy(renames["HistoryIn"]),
            "labels": t.proxy(renames["LabelsIn"]),
            "snippet": t.string().optional(),
            "lastModificationTimeUs": t.string().optional(),
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "attributes": t.proxy(renames["AttributesIn"]),
            "itemKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "parts": t.proxy(renames["ItemPartsIn"]).optional(),
            "creationTimeMicroseconds": t.string().optional(),
            "threadLocator": t.string().optional(),
            "lockerReferences": t.proxy(renames["ReferencesIn"]).optional(),
            "matchInfo": t.proxy(renames["MatchInfoIn"]),
            "version": t.string().optional(),
        }
    ).named(renames["FuseboxItemIn"])
    types["FuseboxItemOut"] = t.struct(
        {
            "triggers": t.proxy(renames["TriggersOut"]),
            "readTs": t.string().optional(),
            "references": t.proxy(renames["ReferencesOut"]).optional(),
            "history": t.proxy(renames["HistoryOut"]),
            "labels": t.proxy(renames["LabelsOut"]),
            "snippet": t.string().optional(),
            "lastModificationTimeUs": t.string().optional(),
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "attributes": t.proxy(renames["AttributesOut"]),
            "itemKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "parts": t.proxy(renames["ItemPartsOut"]).optional(),
            "creationTimeMicroseconds": t.string().optional(),
            "threadLocator": t.string().optional(),
            "lockerReferences": t.proxy(renames["ReferencesOut"]).optional(),
            "matchInfo": t.proxy(renames["MatchInfoOut"]),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FuseboxItemOut"])
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
    types["PrivateMessageInfoIn"] = t.struct(
        {
            "contextualAddOnMarkup": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupIn"])
            ),
            "userId": t.proxy(renames["UserIdIn"]),
            "gsuiteIntegrationMetadata": t.array(
                t.proxy(renames["GsuiteIntegrationMetadataIn"])
            ),
            "annotations": t.array(t.proxy(renames["AnnotationIn"])).optional(),
            "attachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["PrivateMessageInfoIn"])
    types["PrivateMessageInfoOut"] = t.struct(
        {
            "contextualAddOnMarkup": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupOut"])
            ),
            "userId": t.proxy(renames["UserIdOut"]),
            "gsuiteIntegrationMetadata": t.array(
                t.proxy(renames["GsuiteIntegrationMetadataOut"])
            ),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateMessageInfoOut"])
    types["MessageInfoIn"] = t.struct(
        {
            "message": t.proxy(renames["MessageIn"]).optional(),
            "searcherMembershipState": t.string().optional(),
            "authorUserType": t.string().optional(),
        }
    ).named(renames["MessageInfoIn"])
    types["MessageInfoOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "searcherMembershipState": t.string().optional(),
            "authorUserType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageInfoOut"])
    types["DateTimePickerIn"] = t.struct(
        {
            "timezoneOffsetDate": t.integer().optional(),
            "valueMsEpoch": t.string().optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DateTimePickerIn"])
    types["DateTimePickerOut"] = t.struct(
        {
            "timezoneOffsetDate": t.integer().optional(),
            "valueMsEpoch": t.string().optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimePickerOut"])
    types["TopicStateUpdateIn"] = t.struct(
        {"topicState": t.proxy(renames["TopicStateIn"])}
    ).named(renames["TopicStateUpdateIn"])
    types["TopicStateUpdateOut"] = t.struct(
        {
            "topicState": t.proxy(renames["TopicStateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicStateUpdateOut"])
    types["ProcessingErrorIn"] = t.struct(
        {
            "code": t.string().optional(),
            "fieldViolations": t.array(t.proxy(renames["FieldViolationIn"])).optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["ProcessingErrorIn"])
    types["ProcessingErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "fieldViolations": t.array(
                t.proxy(renames["FieldViolationOut"])
            ).optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingErrorOut"])
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
    types["DriveLocationRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveLocationRestrictIn"]
    )
    types["DriveLocationRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveLocationRestrictOut"])
    types["LabelCreatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelCreatedIn"]
    )
    types["LabelCreatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelCreatedOut"])
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
    types["IntegerValuesIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["IntegerValuesIn"]
    )
    types["IntegerValuesOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerValuesOut"])
    types["AppsDynamiteStorageCardIn"] = t.struct(
        {
            "name": t.string().optional(),
            "header": t.proxy(
                renames["AppsDynamiteStorageCardCardHeaderIn"]
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["AppsDynamiteStorageCardCardActionIn"])
            ).optional(),
            "sections": t.array(
                t.proxy(renames["AppsDynamiteStorageCardSectionIn"])
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardIn"])
    types["AppsDynamiteStorageCardOut"] = t.struct(
        {
            "name": t.string().optional(),
            "header": t.proxy(
                renames["AppsDynamiteStorageCardCardHeaderOut"]
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["AppsDynamiteStorageCardCardActionOut"])
            ).optional(),
            "sections": t.array(
                t.proxy(renames["AppsDynamiteStorageCardSectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardOut"])
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
            "items": t.array(t.proxy(renames["GridItemIn"])).optional(),
            "borderStyle": t.proxy(renames["BorderStyleIn"]).optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "numColumns": t.integer().optional(),
        }
    ).named(renames["GridIn"])
    types["GridOut"] = t.struct(
        {
            "title": t.string().optional(),
            "items": t.array(t.proxy(renames["GridItemOut"])).optional(),
            "borderStyle": t.proxy(renames["BorderStyleOut"]).optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "numColumns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridOut"])
    types["UserInfoIn"] = t.struct(
        {
            "updaterToShowGaiaId": t.string().optional(),
            "updaterToShowUserId": t.proxy(renames["UserIdIn"]).optional(),
            "updaterToShowEmail": t.string().optional(),
            "updaterCountDisplayType": t.string().optional(),
            "driveNotificationAvatarUrl": t.string().optional(),
            "updaterCountToShow": t.integer().optional(),
            "updaterToShowName": t.string().optional(),
        }
    ).named(renames["UserInfoIn"])
    types["UserInfoOut"] = t.struct(
        {
            "updaterToShowGaiaId": t.string().optional(),
            "updaterToShowUserId": t.proxy(renames["UserIdOut"]).optional(),
            "updaterToShowEmail": t.string().optional(),
            "updaterCountDisplayType": t.string().optional(),
            "driveNotificationAvatarUrl": t.string().optional(),
            "updaterCountToShow": t.integer().optional(),
            "updaterToShowName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
    types["PossiblyTrimmedModelIn"] = t.struct(
        {"isTrimmed": t.boolean(), "model": t.string()}
    ).named(renames["PossiblyTrimmedModelIn"])
    types["PossiblyTrimmedModelOut"] = t.struct(
        {
            "isTrimmed": t.boolean(),
            "model": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PossiblyTrimmedModelOut"])
    types["AppsDynamiteStorageSelectionInputIn"] = t.struct(
        {
            "name": t.string().optional(),
            "label": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageSelectionInputSelectionItemIn"])
            ),
            "type": t.string(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputIn"])
    types["AppsDynamiteStorageSelectionInputOut"] = t.struct(
        {
            "name": t.string().optional(),
            "label": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageSelectionInputSelectionItemOut"])
            ),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputOut"])
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
    types["GetSearchApplicationSessionStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["SearchApplicationSessionStatsIn"]))}
    ).named(renames["GetSearchApplicationSessionStatsResponseIn"])
    types["GetSearchApplicationSessionStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["SearchApplicationSessionStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationSessionStatsResponseOut"])
    types["GmailClientActionMarkupIn"] = t.struct(
        {
            "updateDraftActionMarkup": t.proxy(renames["UpdateDraftActionMarkupIn"]),
            "taskAction": t.proxy(renames["TaskActionMarkupIn"]),
            "addonComposeUiActionMarkup": t.proxy(
                renames["AddonComposeUiActionMarkupIn"]
            ),
            "openCreatedDraftActionMarkup": t.proxy(
                renames["OpenCreatedDraftActionMarkupIn"]
            ),
        }
    ).named(renames["GmailClientActionMarkupIn"])
    types["GmailClientActionMarkupOut"] = t.struct(
        {
            "updateDraftActionMarkup": t.proxy(renames["UpdateDraftActionMarkupOut"]),
            "taskAction": t.proxy(renames["TaskActionMarkupOut"]),
            "addonComposeUiActionMarkup": t.proxy(
                renames["AddonComposeUiActionMarkupOut"]
            ),
            "openCreatedDraftActionMarkup": t.proxy(
                renames["OpenCreatedDraftActionMarkupOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmailClientActionMarkupOut"])
    types["AppsDynamiteSharedChatItemGroupInfoIn"] = t.struct(
        {
            "groupName": t.string(),
            "attributeCheckerGroupType": t.string().optional(),
            "inlineThreadingEnabled": t.boolean().optional(),
            "groupReadTimeUsec": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemGroupInfoIn"])
    types["AppsDynamiteSharedChatItemGroupInfoOut"] = t.struct(
        {
            "groupName": t.string(),
            "attributeCheckerGroupType": t.string().optional(),
            "inlineThreadingEnabled": t.boolean().optional(),
            "groupReadTimeUsec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemGroupInfoOut"])
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
    types["CloudPrincipalProtoIn"] = t.struct({"id": t.string().optional()}).named(
        renames["CloudPrincipalProtoIn"]
    )
    types["CloudPrincipalProtoOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudPrincipalProtoOut"])
    types["RpcOptionsIn"] = t.struct(
        {"requestExtensions": t.proxy(renames["MessageSetIn"]).optional()}
    ).named(renames["RpcOptionsIn"])
    types["RpcOptionsOut"] = t.struct(
        {
            "requestExtensions": t.proxy(renames["MessageSetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RpcOptionsOut"])
    types["PinnedItemIdIn"] = t.struct({"driveId": t.string().optional()}).named(
        renames["PinnedItemIdIn"]
    )
    types["PinnedItemIdOut"] = t.struct(
        {
            "driveId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PinnedItemIdOut"])
    types["IntegrationConfigMutationIn"] = t.struct(
        {
            "addPinnedItem": t.proxy(renames["PinnedItemIdIn"]).optional(),
            "removePinnedItem": t.proxy(renames["PinnedItemIdIn"]).optional(),
            "addApp": t.proxy(renames["AppIdIn"]).optional(),
            "removeApp": t.proxy(renames["AppIdIn"]).optional(),
        }
    ).named(renames["IntegrationConfigMutationIn"])
    types["IntegrationConfigMutationOut"] = t.struct(
        {
            "addPinnedItem": t.proxy(renames["PinnedItemIdOut"]).optional(),
            "removePinnedItem": t.proxy(renames["PinnedItemIdOut"]).optional(),
            "addApp": t.proxy(renames["AppIdOut"]).optional(),
            "removeApp": t.proxy(renames["AppIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegrationConfigMutationOut"])
    types["SegmentIn"] = t.struct(
        {
            "hashtagData": t.proxy(renames["HashtagDataIn"]).optional(),
            "formatting": t.proxy(renames["FormattingIn"]).optional(),
            "userMentionData": t.proxy(renames["UserMentionDataIn"]).optional(),
            "type": t.string().optional(),
            "text": t.string().optional(),
            "linkData": t.proxy(renames["LinkDataIn"]).optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "hashtagData": t.proxy(renames["HashtagDataOut"]).optional(),
            "formatting": t.proxy(renames["FormattingOut"]).optional(),
            "userMentionData": t.proxy(renames["UserMentionDataOut"]).optional(),
            "type": t.string().optional(),
            "text": t.string().optional(),
            "linkData": t.proxy(renames["LinkDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
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
    types["ReactionInfoIn"] = t.struct({"emoji": t.string().optional()}).named(
        renames["ReactionInfoIn"]
    )
    types["ReactionInfoOut"] = t.struct(
        {
            "emoji": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReactionInfoOut"])
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
    types["DmIdIn"] = t.struct({"dmId": t.string().optional()}).named(renames["DmIdIn"])
    types["DmIdOut"] = t.struct(
        {
            "dmId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DmIdOut"])
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
    types["FacetOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsIn"]
            ).optional(),
            "numFacetBuckets": t.integer().optional(),
            "objectType": t.string().optional(),
            "sourceName": t.string().optional(),
        }
    ).named(renames["FacetOptionsIn"])
    types["FacetOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsOut"]
            ).optional(),
            "numFacetBuckets": t.integer().optional(),
            "objectType": t.string().optional(),
            "sourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetOptionsOut"])
    types["RequiredMessageFeaturesMetadataIn"] = t.struct(
        {"requiredFeatures": t.array(t.string())}
    ).named(renames["RequiredMessageFeaturesMetadataIn"])
    types["RequiredMessageFeaturesMetadataOut"] = t.struct(
        {
            "requiredFeatures": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequiredMessageFeaturesMetadataOut"])
    types["ImapUidsReassignIn"] = t.struct(
        {"messageId": t.array(t.string()).optional(), "labelId": t.string().optional()}
    ).named(renames["ImapUidsReassignIn"])
    types["ImapUidsReassignOut"] = t.struct(
        {
            "messageId": t.array(t.string()).optional(),
            "labelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapUidsReassignOut"])
    types["TextButtonIn"] = t.struct(
        {
            "backgroundColor": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]),
            "altText": t.string().optional(),
            "style": t.string(),
            "text": t.string().optional(),
            "disabled": t.boolean(),
        }
    ).named(renames["TextButtonIn"])
    types["TextButtonOut"] = t.struct(
        {
            "backgroundColor": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "altText": t.string().optional(),
            "style": t.string(),
            "text": t.string().optional(),
            "disabled": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextButtonOut"])
    types["MessageIn"] = t.struct(
        {
            "lastEditTime": t.string().optional(),
            "deletableBy": t.string().optional(),
            "appProfile": t.proxy(renames["AppsDynamiteSharedAppProfileIn"]).optional(),
            "attachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "id": t.proxy(renames["MessageIdIn"]).optional(),
            "privateMessageViewer": t.proxy(renames["UserIdIn"]).optional(),
            "tombstoneMetadata": t.proxy(renames["TombstoneMetadataIn"]).optional(),
            "botResponses": t.array(t.proxy(renames["BotResponseIn"])).optional(),
            "deletedByVault": t.boolean().optional(),
            "communalLabels": t.array(
                t.proxy(renames["CommunalLabelTagIn"])
            ).optional(),
            "attributes": t.proxy(renames["MessageAttributesIn"]).optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryIn"]).optional(),
            "originAppSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedOriginAppSuggestionIn"])
            ).optional(),
            "isContentPurged": t.boolean().optional(),
            "richTextFormattingType": t.string().optional(),
            "deleteTime": t.string().optional(),
            "deleteTimeForRequester": t.string().optional(),
            "reactions": t.array(
                t.proxy(renames["AppsDynamiteSharedReactionIn"])
            ).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationIn"])).optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataIn"])).optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsIn"]
            ).optional(),
            "creatorId": t.proxy(renames["UserIdIn"]).optional(),
            "createTime": t.string().optional(),
            "messageOrigin": t.string().optional(),
            "fallbackText": t.string().optional(),
            "textBody": t.string().optional(),
            "updaterId": t.proxy(renames["UserIdIn"]).optional(),
            "secondaryMessageKey": t.string().optional(),
            "props": t.proxy(renames["MessagePropsIn"]).optional(),
            "editableBy": t.string().optional(),
            "localId": t.string().optional(),
            "personalLabels": t.array(
                t.proxy(renames["PersonalLabelTagIn"])
            ).optional(),
            "lastUpdateTime": t.string().optional(),
            "messageState": t.string().optional(),
            "privateMessageInfos": t.array(
                t.proxy(renames["PrivateMessageInfoIn"])
            ).optional(),
            "messageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedMessageIntegrationPayloadIn"]
            ).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "contentReportSummary": t.proxy(renames["ContentReportSummaryOut"]),
            "lastEditTime": t.string().optional(),
            "deletableBy": t.string().optional(),
            "appProfile": t.proxy(
                renames["AppsDynamiteSharedAppProfileOut"]
            ).optional(),
            "quotedByState": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "id": t.proxy(renames["MessageIdOut"]).optional(),
            "privateMessageViewer": t.proxy(renames["UserIdOut"]).optional(),
            "tombstoneMetadata": t.proxy(renames["TombstoneMetadataOut"]).optional(),
            "botResponses": t.array(t.proxy(renames["BotResponseOut"])).optional(),
            "deletedByVault": t.boolean().optional(),
            "communalLabels": t.array(
                t.proxy(renames["CommunalLabelTagOut"])
            ).optional(),
            "attributes": t.proxy(renames["MessageAttributesOut"]).optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryOut"]).optional(),
            "reports": t.array(t.proxy(renames["ContentReportOut"])).optional(),
            "originAppSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedOriginAppSuggestionOut"])
            ).optional(),
            "isContentPurged": t.boolean().optional(),
            "richTextFormattingType": t.string().optional(),
            "deleteTime": t.string().optional(),
            "deleteTimeForRequester": t.string().optional(),
            "reactions": t.array(
                t.proxy(renames["AppsDynamiteSharedReactionOut"])
            ).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataOut"])).optional(),
            "quotedMessageMetadata": t.proxy(
                renames["QuotedMessageMetadataOut"]
            ).optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsOut"]
            ).optional(),
            "creatorId": t.proxy(renames["UserIdOut"]).optional(),
            "createTime": t.string().optional(),
            "messageOrigin": t.string().optional(),
            "fallbackText": t.string().optional(),
            "textBody": t.string().optional(),
            "updaterId": t.proxy(renames["UserIdOut"]).optional(),
            "secondaryMessageKey": t.string().optional(),
            "props": t.proxy(renames["MessagePropsOut"]).optional(),
            "editableBy": t.string().optional(),
            "localId": t.string().optional(),
            "isInlineReply": t.boolean().optional(),
            "personalLabels": t.array(
                t.proxy(renames["PersonalLabelTagOut"])
            ).optional(),
            "lastUpdateTime": t.string().optional(),
            "messageState": t.string().optional(),
            "privateMessageInfos": t.array(
                t.proxy(renames["PrivateMessageInfoOut"])
            ).optional(),
            "messageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedMessageIntegrationPayloadOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["EnumValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["EnumValuesIn"]
    )
    types["EnumValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValuesOut"])
    types["UserMentionDataIn"] = t.struct(
        {
            "email": t.string(),
            "userGaiaId": t.string().optional(),
            "user": t.proxy(renames["PrincipalProtoIn"]).optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["UserMentionDataIn"])
    types["UserMentionDataOut"] = t.struct(
        {
            "email": t.string(),
            "userGaiaId": t.string().optional(),
            "user": t.proxy(renames["PrincipalProtoOut"]).optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserMentionDataOut"])
    types["BabelPlaceholderMetadataIn"] = t.struct(
        {
            "deleteMetadata": t.proxy(renames["DeleteMetadataIn"]),
            "hangoutVideoMetadata": t.proxy(renames["HangoutVideoEventMetadataIn"]),
            "editMetadata": t.proxy(renames["EditMetadataIn"]),
        }
    ).named(renames["BabelPlaceholderMetadataIn"])
    types["BabelPlaceholderMetadataOut"] = t.struct(
        {
            "deleteMetadata": t.proxy(renames["DeleteMetadataOut"]),
            "hangoutVideoMetadata": t.proxy(renames["HangoutVideoEventMetadataOut"]),
            "editMetadata": t.proxy(renames["EditMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BabelPlaceholderMetadataOut"])
    types["InviteAcceptedEventIn"] = t.struct(
        {"participantId": t.array(t.proxy(renames["StoredParticipantIdIn"]))}
    ).named(renames["InviteAcceptedEventIn"])
    types["InviteAcceptedEventOut"] = t.struct(
        {
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InviteAcceptedEventOut"])
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
    types["SourceScoringConfigIn"] = t.struct(
        {"sourceImportance": t.string().optional()}
    ).named(renames["SourceScoringConfigIn"])
    types["SourceScoringConfigOut"] = t.struct(
        {
            "sourceImportance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceScoringConfigOut"])
    types["DynamiteSpacesScoringInfoIn"] = t.struct(
        {
            "finalScore": t.number(),
            "freshnessScore": t.number(),
            "spaceCreationTimestampSecs": t.string(),
            "smallUnjoinedSpacesAffinityScore": t.number(),
            "topicalityScore": t.number(),
            "contactsIntersectionCount": t.number(),
            "smallContactListAffinityScore": t.number(),
            "memberMetadataCount": t.number(),
            "lastMessagePostedTimestampSecs": t.string(),
            "commonContactCountAffinityScore": t.number(),
            "memberCountScore": t.number(),
            "affinityScore": t.number(),
            "spaceAgeInDays": t.number(),
            "lastReadTimestampSecs": t.string(),
            "messageScore": t.number(),
            "numAucContacts": t.string(),
            "joinedSpacesAffinityScore": t.number(),
        }
    ).named(renames["DynamiteSpacesScoringInfoIn"])
    types["DynamiteSpacesScoringInfoOut"] = t.struct(
        {
            "finalScore": t.number(),
            "freshnessScore": t.number(),
            "spaceCreationTimestampSecs": t.string(),
            "smallUnjoinedSpacesAffinityScore": t.number(),
            "topicalityScore": t.number(),
            "contactsIntersectionCount": t.number(),
            "smallContactListAffinityScore": t.number(),
            "memberMetadataCount": t.number(),
            "lastMessagePostedTimestampSecs": t.string(),
            "commonContactCountAffinityScore": t.number(),
            "memberCountScore": t.number(),
            "affinityScore": t.number(),
            "spaceAgeInDays": t.number(),
            "lastReadTimestampSecs": t.string(),
            "messageScore": t.number(),
            "numAucContacts": t.string(),
            "joinedSpacesAffinityScore": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamiteSpacesScoringInfoOut"])
    types["DataSourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "returnThumbnailUrls": t.boolean().optional(),
            "shortName": t.string().optional(),
            "indexingServiceAccounts": t.array(t.string()).optional(),
            "operationIds": t.array(t.string()).optional(),
            "disableModifications": t.boolean().optional(),
            "displayName": t.string(),
            "disableServing": t.boolean().optional(),
            "itemsVisibility": t.array(
                t.proxy(renames["GSuitePrincipalIn"])
            ).optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "returnThumbnailUrls": t.boolean().optional(),
            "shortName": t.string().optional(),
            "indexingServiceAccounts": t.array(t.string()).optional(),
            "operationIds": t.array(t.string()).optional(),
            "disableModifications": t.boolean().optional(),
            "displayName": t.string(),
            "disableServing": t.boolean().optional(),
            "itemsVisibility": t.array(
                t.proxy(renames["GSuitePrincipalOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["MdbGroupProtoIn"] = t.struct({"groupName": t.string()}).named(
        renames["MdbGroupProtoIn"]
    )
    types["MdbGroupProtoOut"] = t.struct(
        {"groupName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MdbGroupProtoOut"])
    types["ChatClientActionMarkupIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ChatClientActionMarkupIn"]
    )
    types["ChatClientActionMarkupOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatClientActionMarkupOut"])
    types["AppsDynamiteStorageGridGridItemIn"] = t.struct(
        {
            "layout": t.string().optional(),
            "id": t.string().optional(),
            "subtitle": t.string().optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageComponentIn"]).optional(),
            "textAlignment": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageGridGridItemIn"])
    types["AppsDynamiteStorageGridGridItemOut"] = t.struct(
        {
            "layout": t.string().optional(),
            "id": t.string().optional(),
            "subtitle": t.string().optional(),
            "image": t.proxy(
                renames["AppsDynamiteStorageImageComponentOut"]
            ).optional(),
            "textAlignment": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageGridGridItemOut"])
    types["ReferencesIn"] = t.struct(
        {"references": t.array(t.proxy(renames["ReferenceIn"]))}
    ).named(renames["ReferencesIn"])
    types["ReferencesOut"] = t.struct(
        {
            "references": t.array(t.proxy(renames["ReferenceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferencesOut"])
    types["PropertyDisplayOptionsIn"] = t.struct(
        {"displayLabel": t.string().optional()}
    ).named(renames["PropertyDisplayOptionsIn"])
    types["PropertyDisplayOptionsOut"] = t.struct(
        {
            "displayLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyDisplayOptionsOut"])
    types["SourceResultCountIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "hasMoreResults": t.boolean().optional(),
            "resultCountExact": t.string().optional(),
            "resultCountEstimate": t.string().optional(),
        }
    ).named(renames["SourceResultCountIn"])
    types["SourceResultCountOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "hasMoreResults": t.boolean().optional(),
            "resultCountExact": t.string().optional(),
            "resultCountEstimate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceResultCountOut"])
    types["ItemThreadIn"] = t.struct(
        {
            "threadLocator": t.string().optional(),
            "lastItemId": t.string().optional(),
            "item": t.array(t.proxy(renames["FuseboxItemIn"])).optional(),
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "snippet": t.string().optional(),
            "clusterInfo": t.proxy(renames["ClusterInfoIn"]),
            "version": t.string().optional(),
            "matchInfo": t.proxy(renames["FuseboxItemThreadMatchInfoIn"]),
            "topicState": t.proxy(renames["TopicStateIn"]).optional(),
        }
    ).named(renames["ItemThreadIn"])
    types["ItemThreadOut"] = t.struct(
        {
            "threadLocator": t.string().optional(),
            "lastItemId": t.string().optional(),
            "item": t.array(t.proxy(renames["FuseboxItemOut"])).optional(),
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "snippet": t.string().optional(),
            "clusterInfo": t.proxy(renames["ClusterInfoOut"]),
            "version": t.string().optional(),
            "matchInfo": t.proxy(renames["FuseboxItemThreadMatchInfoOut"]),
            "topicState": t.proxy(renames["TopicStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemThreadOut"])
    types["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"] = t.struct(
        {"meetingUrl": t.string()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut"] = t.struct(
        {
            "meetingUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut"])
    types["CircleProtoIn"] = t.struct(
        {
            "ownerGaiaId": t.string().optional(),
            "circleId": t.string().optional(),
            "requiredConsistencyTimestampUsec": t.string().optional(),
        }
    ).named(renames["CircleProtoIn"])
    types["CircleProtoOut"] = t.struct(
        {
            "ownerGaiaId": t.string().optional(),
            "circleId": t.string().optional(),
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CircleProtoOut"])
    types["ImapUpdateIn"] = t.struct(
        {"imapUidsReassign": t.proxy(renames["ImapUidsReassignIn"])}
    ).named(renames["ImapUpdateIn"])
    types["ImapUpdateOut"] = t.struct(
        {
            "imapUidsReassign": t.proxy(renames["ImapUidsReassignOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapUpdateOut"])
    types["UpdateCcRecipientsIn"] = t.struct(
        {"ccRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateCcRecipientsIn"])
    types["UpdateCcRecipientsOut"] = t.struct(
        {
            "ccRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCcRecipientsOut"])
    types["AppsDynamiteStorageImageComponentIn"] = t.struct(
        {
            "cropStyle": t.proxy(
                renames["AppsDynamiteStorageImageCropStyleIn"]
            ).optional(),
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleIn"]
            ).optional(),
            "altText": t.string().optional(),
            "imageUri": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageImageComponentIn"])
    types["AppsDynamiteStorageImageComponentOut"] = t.struct(
        {
            "cropStyle": t.proxy(
                renames["AppsDynamiteStorageImageCropStyleOut"]
            ).optional(),
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleOut"]
            ).optional(),
            "altText": t.string().optional(),
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageComponentOut"])
    types["AppsDynamiteStorageColumnsColumnWidgetsIn"] = t.struct(
        {
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputIn"]
            ).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListIn"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphIn"]
            ).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerIn"]
            ).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextIn"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageIn"]).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnWidgetsIn"])
    types["AppsDynamiteStorageColumnsColumnWidgetsOut"] = t.struct(
        {
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputOut"]
            ).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListOut"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphOut"]
            ).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerOut"]
            ).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextOut"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageOut"]).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnWidgetsOut"])
    types["BabelMessagePropsIn"] = t.struct(
        {
            "eventId": t.string().optional(),
            "wasUpdatedByBackfill": t.boolean().optional(),
            "messageContent": t.proxy(
                renames["ChatConserverMessageContentIn"]
            ).optional(),
            "clientGeneratedId": t.string().optional(),
            "contentExtension": t.proxy(renames["ChatContentExtensionIn"]).optional(),
            "deliveryMedium": t.proxy(renames["DeliveryMediumIn"]).optional(),
        }
    ).named(renames["BabelMessagePropsIn"])
    types["BabelMessagePropsOut"] = t.struct(
        {
            "eventId": t.string().optional(),
            "wasUpdatedByBackfill": t.boolean().optional(),
            "messageContent": t.proxy(
                renames["ChatConserverMessageContentOut"]
            ).optional(),
            "clientGeneratedId": t.string().optional(),
            "contentExtension": t.proxy(renames["ChatContentExtensionOut"]).optional(),
            "deliveryMedium": t.proxy(renames["DeliveryMediumOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BabelMessagePropsOut"])
    types["AppsDynamiteSharedTextSegmentsWithDescriptionIn"] = t.struct(
        {
            "textSegment": t.array(t.proxy(renames["AppsDynamiteSharedTextSegmentIn"])),
            "descriptionType": t.string(),
        }
    ).named(renames["AppsDynamiteSharedTextSegmentsWithDescriptionIn"])
    types["AppsDynamiteSharedTextSegmentsWithDescriptionOut"] = t.struct(
        {
            "textSegment": t.array(
                t.proxy(renames["AppsDynamiteSharedTextSegmentOut"])
            ),
            "descriptionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTextSegmentsWithDescriptionOut"])
    types["AppsDynamiteV1ApiCompatV1ActionIn"] = t.struct(
        {
            "style": t.string().optional(),
            "type": t.string().optional(),
            "text": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confirm": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1ActionConfirmIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionIn"])
    types["AppsDynamiteV1ApiCompatV1ActionOut"] = t.struct(
        {
            "style": t.string().optional(),
            "type": t.string().optional(),
            "text": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confirm": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1ActionConfirmOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn"
    ] = t.struct(
        {"type": t.string().optional(), "authenticationUrl": t.string().optional()}
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn"
        ]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut"
    ] = t.struct(
        {
            "type": t.string().optional(),
            "authenticationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut"
        ]
    )
    types["ListUnmappedIdentitiesResponseIn"] = t.struct(
        {
            "unmappedIdentities": t.array(t.proxy(renames["UnmappedIdentityIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUnmappedIdentitiesResponseIn"])
    types["ListUnmappedIdentitiesResponseOut"] = t.struct(
        {
            "unmappedIdentities": t.array(t.proxy(renames["UnmappedIdentityOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUnmappedIdentitiesResponseOut"])
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
    types["LanguageConfigIn"] = t.struct(
        {"spokenLanguages": t.array(t.string()).optional()}
    ).named(renames["LanguageConfigIn"])
    types["LanguageConfigOut"] = t.struct(
        {
            "spokenLanguages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageConfigOut"])
    types["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"])
    types["NamedPropertyIn"] = t.struct(
        {
            "enumValues": t.proxy(renames["EnumValuesIn"]),
            "textValues": t.proxy(renames["TextValuesIn"]),
            "integerValues": t.proxy(renames["IntegerValuesIn"]),
            "doubleValues": t.proxy(renames["DoubleValuesIn"]),
            "dateValues": t.proxy(renames["DateValuesIn"]),
            "booleanValue": t.boolean(),
            "htmlValues": t.proxy(renames["HtmlValuesIn"]),
            "name": t.string().optional(),
            "objectValues": t.proxy(renames["ObjectValuesIn"]),
            "timestampValues": t.proxy(renames["TimestampValuesIn"]),
        }
    ).named(renames["NamedPropertyIn"])
    types["NamedPropertyOut"] = t.struct(
        {
            "enumValues": t.proxy(renames["EnumValuesOut"]),
            "textValues": t.proxy(renames["TextValuesOut"]),
            "integerValues": t.proxy(renames["IntegerValuesOut"]),
            "doubleValues": t.proxy(renames["DoubleValuesOut"]),
            "dateValues": t.proxy(renames["DateValuesOut"]),
            "booleanValue": t.boolean(),
            "htmlValues": t.proxy(renames["HtmlValuesOut"]),
            "name": t.string().optional(),
            "objectValues": t.proxy(renames["ObjectValuesOut"]),
            "timestampValues": t.proxy(renames["TimestampValuesOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedPropertyOut"])
    types["GoogleChatV1WidgetMarkupKeyValueIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "icon": t.string().optional(),
            "topLabel": t.string().optional(),
            "content": t.string().optional(),
            "iconUrl": t.string().optional(),
            "button": t.proxy(renames["GoogleChatV1WidgetMarkupButtonIn"]).optional(),
            "contentMultiline": t.boolean().optional(),
            "bottomLabel": t.string().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupKeyValueIn"])
    types["GoogleChatV1WidgetMarkupKeyValueOut"] = t.struct(
        {
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "icon": t.string().optional(),
            "topLabel": t.string().optional(),
            "content": t.string().optional(),
            "iconUrl": t.string().optional(),
            "button": t.proxy(renames["GoogleChatV1WidgetMarkupButtonOut"]).optional(),
            "contentMultiline": t.boolean().optional(),
            "bottomLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupKeyValueOut"])
    types["EditMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EditMetadataIn"]
    )
    types["EditMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EditMetadataOut"])
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
    types["ValueIn"] = t.struct(
        {
            "integerValue": t.string(),
            "doubleValue": t.number(),
            "dateValue": t.proxy(renames["DateIn"]),
            "booleanValue": t.boolean(),
            "stringValue": t.string(),
            "timestampValue": t.string(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "integerValue": t.string(),
            "doubleValue": t.number(),
            "dateValue": t.proxy(renames["DateOut"]),
            "booleanValue": t.boolean(),
            "stringValue": t.string(),
            "timestampValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["StoredParticipantIdIn"] = t.struct({"gaiaId": t.string()}).named(
        renames["StoredParticipantIdIn"]
    )
    types["StoredParticipantIdOut"] = t.struct(
        {"gaiaId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StoredParticipantIdOut"])
    types["LdapGroupProtoIn"] = t.struct({"groupName": t.string()}).named(
        renames["LdapGroupProtoIn"]
    )
    types["LdapGroupProtoOut"] = t.struct(
        {"groupName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LdapGroupProtoOut"])
    types["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"])
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
    types["PrefDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PrefDeletedIn"]
    )
    types["PrefDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PrefDeletedOut"])
    types["SuggestRequestIn"] = t.struct(
        {
            "query": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
        }
    ).named(renames["SuggestRequestIn"])
    types["SuggestRequestOut"] = t.struct(
        {
            "query": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestRequestOut"])
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn"
    ] = t.struct(
        {
            "parameters": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn"
                    ]
                )
            ).optional(),
            "note": t.string().optional(),
            "error": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn"
                ]
            ).optional(),
            "entryPoints": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn"
                    ]
                )
            ).optional(),
            "conferenceId": t.string().optional(),
            "conferenceSolutionId": t.string().optional(),
        }
    ).named(
        renames["AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn"]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut"
    ] = t.struct(
        {
            "parameters": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut"
                    ]
                )
            ).optional(),
            "note": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "entryPoints": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut"
                    ]
                )
            ).optional(),
            "conferenceId": t.string().optional(),
            "conferenceSolutionId": t.string().optional(),
        }
    ).named(
        renames["AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut"]
    )
    types["ImageButtonIn"] = t.struct(
        {
            "icon": t.string(),
            "onClick": t.proxy(renames["OnClickIn"]),
            "name": t.string(),
            "iconUrl": t.string(),
        }
    ).named(renames["ImageButtonIn"])
    types["ImageButtonOut"] = t.struct(
        {
            "icon": t.string(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "name": t.string(),
            "iconUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageButtonOut"])
    types["WhiteboardInfoIn"] = t.struct(
        {
            "title": t.string().optional(),
            "id": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["WhiteboardInfoIn"])
    types["WhiteboardInfoOut"] = t.struct(
        {
            "title": t.string().optional(),
            "id": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WhiteboardInfoOut"])
    types["GoogleChatV1WidgetMarkupTextButtonIn"] = t.struct(
        {
            "text": t.string().optional(),
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupTextButtonIn"])
    types["GoogleChatV1WidgetMarkupTextButtonOut"] = t.struct(
        {
            "text": t.string().optional(),
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupTextButtonOut"])
    types["AutoCompleteItemIn"] = t.struct({"text": t.string()}).named(
        renames["AutoCompleteItemIn"]
    )
    types["AutoCompleteItemOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AutoCompleteItemOut"])
    types["AppsDynamiteStorageButtonIn"] = t.struct(
        {
            "icon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "altText": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
            "disabled": t.boolean().optional(),
            "text": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonIn"])
    types["AppsDynamiteStorageButtonOut"] = t.struct(
        {
            "icon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "altText": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "disabled": t.boolean().optional(),
            "text": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonOut"])
    types["QuerySourceIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "displayName": t.string().optional(),
            "operators": t.array(t.proxy(renames["QueryOperatorIn"])).optional(),
            "shortName": t.string().optional(),
        }
    ).named(renames["QuerySourceIn"])
    types["QuerySourceOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "displayName": t.string().optional(),
            "operators": t.array(t.proxy(renames["QueryOperatorOut"])).optional(),
            "shortName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuerySourceOut"])
    types["UploadItemRefIn"] = t.struct({"name": t.string().optional()}).named(
        renames["UploadItemRefIn"]
    )
    types["UploadItemRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadItemRefOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"] = t.struct(
        {"replyType": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut"] = t.struct(
        {
            "replyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut"])
    types["VideoInfoIn"] = t.struct({"duration": t.integer().optional()}).named(
        renames["VideoInfoIn"]
    )
    types["VideoInfoOut"] = t.struct(
        {
            "duration": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoInfoOut"])
    types["EnumOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["EnumOperatorOptionsIn"])
    types["EnumOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOperatorOptionsOut"])
    types["TriggersIn"] = t.struct(
        {"triggers": t.array(t.proxy(renames["TriggerIn"])).optional()}
    ).named(renames["TriggersIn"])
    types["TriggersOut"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggersOut"])
    types["SafeUrlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeUrlWrappedValue": t.string().optional()}
    ).named(renames["SafeUrlProtoIn"])
    types["SafeUrlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeUrlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeUrlProtoOut"])
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
    types["AuditLoggingSettingsIn"] = t.struct(
        {
            "logDataReadActions": t.boolean().optional(),
            "project": t.string().optional(),
            "logAdminReadActions": t.boolean().optional(),
            "logDataWriteActions": t.boolean().optional(),
        }
    ).named(renames["AuditLoggingSettingsIn"])
    types["AuditLoggingSettingsOut"] = t.struct(
        {
            "logDataReadActions": t.boolean().optional(),
            "project": t.string().optional(),
            "logAdminReadActions": t.boolean().optional(),
            "logDataWriteActions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLoggingSettingsOut"])
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
    types["HostProtoIn"] = t.struct(
        {"hostOwner": t.string().optional(), "hostName": t.string().optional()}
    ).named(renames["HostProtoIn"])
    types["HostProtoOut"] = t.struct(
        {
            "hostOwner": t.string().optional(),
            "hostName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostProtoOut"])
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
    types["GetDataSourceIndexStatsResponseIn"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["DataSourceIndexStatsIn"])).optional(),
            "averageIndexedItemCount": t.string().optional(),
        }
    ).named(renames["GetDataSourceIndexStatsResponseIn"])
    types["GetDataSourceIndexStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["DataSourceIndexStatsOut"])).optional(),
            "averageIndexedItemCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDataSourceIndexStatsResponseOut"])
    types["CardCapabilityMetadataIn"] = t.struct(
        {"requiredCapabilities": t.array(t.string()).optional()}
    ).named(renames["CardCapabilityMetadataIn"])
    types["CardCapabilityMetadataOut"] = t.struct(
        {
            "requiredCapabilities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardCapabilityMetadataOut"])
    types["MetalineIn"] = t.struct(
        {"properties": t.array(t.proxy(renames["DisplayedPropertyIn"])).optional()}
    ).named(renames["MetalineIn"])
    types["MetalineOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["DisplayedPropertyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetalineOut"])
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
    types["CompositeFilterIn"] = t.struct(
        {
            "subFilters": t.array(t.proxy(renames["FilterIn"])).optional(),
            "logicOperator": t.string().optional(),
        }
    ).named(renames["CompositeFilterIn"])
    types["CompositeFilterOut"] = t.struct(
        {
            "subFilters": t.array(t.proxy(renames["FilterOut"])).optional(),
            "logicOperator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeFilterOut"])
    types["PersonIn"] = t.struct(
        {
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressIn"])).optional(),
            "name": t.string().optional(),
            "photos": t.array(t.proxy(renames["PhotoIn"])).optional(),
            "obfuscatedId": t.string().optional(),
            "personNames": t.array(t.proxy(renames["NameIn"])).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberOut"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressOut"])).optional(),
            "name": t.string().optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "obfuscatedId": t.string().optional(),
            "personNames": t.array(t.proxy(renames["NameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["PackagingServiceClientIn"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "type": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
        }
    ).named(renames["PackagingServiceClientIn"])
    types["PackagingServiceClientOut"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "type": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackagingServiceClientOut"])
    types["PropertyDefinitionIn"] = t.struct(
        {
            "textPropertyOptions": t.proxy(renames["TextPropertyOptionsIn"]),
            "name": t.string().optional(),
            "displayOptions": t.proxy(renames["PropertyDisplayOptionsIn"]).optional(),
            "objectPropertyOptions": t.proxy(renames["ObjectPropertyOptionsIn"]),
            "booleanPropertyOptions": t.proxy(renames["BooleanPropertyOptionsIn"]),
            "isRepeatable": t.boolean().optional(),
            "integerPropertyOptions": t.proxy(renames["IntegerPropertyOptionsIn"]),
            "datePropertyOptions": t.proxy(renames["DatePropertyOptionsIn"]),
            "htmlPropertyOptions": t.proxy(renames["HtmlPropertyOptionsIn"]),
            "isFacetable": t.boolean().optional(),
            "enumPropertyOptions": t.proxy(renames["EnumPropertyOptionsIn"]),
            "isSuggestable": t.boolean().optional(),
            "isSortable": t.boolean().optional(),
            "isWildcardSearchable": t.boolean().optional(),
            "isReturnable": t.boolean().optional(),
            "doublePropertyOptions": t.proxy(renames["DoublePropertyOptionsIn"]),
            "timestampPropertyOptions": t.proxy(renames["TimestampPropertyOptionsIn"]),
        }
    ).named(renames["PropertyDefinitionIn"])
    types["PropertyDefinitionOut"] = t.struct(
        {
            "textPropertyOptions": t.proxy(renames["TextPropertyOptionsOut"]),
            "name": t.string().optional(),
            "displayOptions": t.proxy(renames["PropertyDisplayOptionsOut"]).optional(),
            "objectPropertyOptions": t.proxy(renames["ObjectPropertyOptionsOut"]),
            "booleanPropertyOptions": t.proxy(renames["BooleanPropertyOptionsOut"]),
            "isRepeatable": t.boolean().optional(),
            "integerPropertyOptions": t.proxy(renames["IntegerPropertyOptionsOut"]),
            "datePropertyOptions": t.proxy(renames["DatePropertyOptionsOut"]),
            "htmlPropertyOptions": t.proxy(renames["HtmlPropertyOptionsOut"]),
            "isFacetable": t.boolean().optional(),
            "enumPropertyOptions": t.proxy(renames["EnumPropertyOptionsOut"]),
            "isSuggestable": t.boolean().optional(),
            "isSortable": t.boolean().optional(),
            "isWildcardSearchable": t.boolean().optional(),
            "isReturnable": t.boolean().optional(),
            "doublePropertyOptions": t.proxy(renames["DoublePropertyOptionsOut"]),
            "timestampPropertyOptions": t.proxy(renames["TimestampPropertyOptionsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyDefinitionOut"])
    types["GoogleChatV1WidgetMarkupOpenLinkIn"] = t.struct(
        {"url": t.string().optional()}
    ).named(renames["GoogleChatV1WidgetMarkupOpenLinkIn"])
    types["GoogleChatV1WidgetMarkupOpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupOpenLinkOut"])
    types["PersonalLabelTagIn"] = t.struct({"labelId": t.string().optional()}).named(
        renames["PersonalLabelTagIn"]
    )
    types["PersonalLabelTagOut"] = t.struct(
        {
            "labelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalLabelTagOut"])
    types["SessionStateInfoIn"] = t.struct(
        {
            "languageConfig": t.proxy(renames["LanguageConfigIn"]).optional(),
            "sessionState": t.string().optional(),
        }
    ).named(renames["SessionStateInfoIn"])
    types["SessionStateInfoOut"] = t.struct(
        {
            "languageConfig": t.proxy(renames["LanguageConfigOut"]).optional(),
            "lastActorDeviceId": t.string().optional(),
            "maxEndTime": t.string().optional(),
            "ackInfo": t.proxy(renames["AckInfoOut"]).optional(),
            "sessionState": t.string().optional(),
            "sessionStopReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionStateInfoOut"])
    types["GetCustomerSearchApplicationStatsResponseIn"] = t.struct(
        {
            "stats": t.array(
                t.proxy(renames["CustomerSearchApplicationStatsIn"])
            ).optional(),
            "averageSearchApplicationCount": t.string().optional(),
        }
    ).named(renames["GetCustomerSearchApplicationStatsResponseIn"])
    types["GetCustomerSearchApplicationStatsResponseOut"] = t.struct(
        {
            "stats": t.array(
                t.proxy(renames["CustomerSearchApplicationStatsOut"])
            ).optional(),
            "averageSearchApplicationCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerSearchApplicationStatsResponseOut"])
    types["AppsDynamiteStorageWidgetIn"] = t.struct(
        {
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphIn"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageIn"]).optional(),
            "columns": t.proxy(renames["AppsDynamiteStorageColumnsIn"]).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextIn"]
            ).optional(),
            "horizontalAlignment": t.string().optional(),
            "grid": t.proxy(renames["AppsDynamiteStorageGridIn"]).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputIn"]).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerIn"]
            ).optional(),
            "divider": t.proxy(renames["AppsDynamiteStorageDividerIn"]).optional(),
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputIn"]
            ).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageWidgetIn"])
    types["AppsDynamiteStorageWidgetOut"] = t.struct(
        {
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphOut"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageOut"]).optional(),
            "columns": t.proxy(renames["AppsDynamiteStorageColumnsOut"]).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextOut"]
            ).optional(),
            "horizontalAlignment": t.string().optional(),
            "grid": t.proxy(renames["AppsDynamiteStorageGridOut"]).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputOut"]).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerOut"]
            ).optional(),
            "divider": t.proxy(renames["AppsDynamiteStorageDividerOut"]).optional(),
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputOut"]
            ).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageWidgetOut"])
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
    types["SectionIn"] = t.struct(
        {
            "collapsable": t.boolean().optional(),
            "numUncollapsableWidgets": t.integer().optional(),
            "description": t.string().optional(),
            "widgets": t.array(t.proxy(renames["WidgetMarkupIn"])).optional(),
        }
    ).named(renames["SectionIn"])
    types["SectionOut"] = t.struct(
        {
            "collapsable": t.boolean().optional(),
            "numUncollapsableWidgets": t.integer().optional(),
            "description": t.string().optional(),
            "widgets": t.array(t.proxy(renames["WidgetMarkupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionOut"])
    types["TextFieldIn"] = t.struct(
        {
            "label": t.string().optional(),
            "autoCompleteCallback": t.proxy(renames["FormActionIn"]).optional(),
            "hintText": t.string(),
            "value": t.string().optional(),
            "onChange": t.proxy(renames["FormActionIn"]),
            "type": t.string(),
            "autoComplete": t.proxy(renames["AutoCompleteIn"]).optional(),
            "maxLines": t.integer(),
            "name": t.string().optional(),
            "autoCompleteMultipleSelections": t.boolean().optional(),
        }
    ).named(renames["TextFieldIn"])
    types["TextFieldOut"] = t.struct(
        {
            "label": t.string().optional(),
            "autoCompleteCallback": t.proxy(renames["FormActionOut"]).optional(),
            "hintText": t.string(),
            "value": t.string().optional(),
            "onChange": t.proxy(renames["FormActionOut"]),
            "type": t.string(),
            "autoComplete": t.proxy(renames["AutoCompleteOut"]).optional(),
            "maxLines": t.integer(),
            "name": t.string().optional(),
            "autoCompleteMultipleSelections": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFieldOut"])
    types["ZwiebackSessionProtoIn"] = t.struct({"zwiebackSessionId": t.string()}).named(
        renames["ZwiebackSessionProtoIn"]
    )
    types["ZwiebackSessionProtoOut"] = t.struct(
        {
            "zwiebackSessionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZwiebackSessionProtoOut"])
    types["LabelAddedIn"] = t.struct(
        {
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
            "labelName": t.string(),
            "syncId": t.integer(),
            "labelId": t.string(),
        }
    ).named(renames["LabelAddedIn"])
    types["LabelAddedOut"] = t.struct(
        {
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "labelName": t.string(),
            "syncId": t.integer(),
            "labelId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelAddedOut"])
    types["SearchRequestIn"] = t.struct(
        {
            "queryInterpretationOptions": t.proxy(
                renames["QueryInterpretationOptionsIn"]
            ).optional(),
            "sortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeIn"])
            ).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "start": t.integer().optional(),
            "facetOptions": t.array(t.proxy(renames["FacetOptionsIn"])),
            "pageSize": t.integer().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["SearchRequestIn"])
    types["SearchRequestOut"] = t.struct(
        {
            "queryInterpretationOptions": t.proxy(
                renames["QueryInterpretationOptionsOut"]
            ).optional(),
            "sortOptions": t.proxy(renames["SortOptionsOut"]).optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeOut"])
            ).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "start": t.integer().optional(),
            "facetOptions": t.array(t.proxy(renames["FacetOptionsOut"])),
            "pageSize": t.integer().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchRequestOut"])
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
    types["UserIn"] = t.struct(
        {
            "avatarUrl": t.string().optional(),
            "name": t.string().optional(),
            "organizationInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoIn"]
            ).optional(),
            "botInfo": t.proxy(renames["BotInfoIn"]).optional(),
            "userAccountState": t.string().optional(),
            "phoneNumber": t.array(
                t.proxy(renames["AppsDynamiteSharedPhoneNumberIn"])
            ).optional(),
            "isAnonymous": t.boolean().optional(),
            "blockRelationship": t.proxy(
                renames["AppsDynamiteSharedUserBlockRelationshipIn"]
            ).optional(),
            "deleted": t.boolean().optional(),
            "email": t.string().optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
            "gender": t.string().optional(),
            "userProfileVisibility": t.string().optional(),
            "lastName": t.string().optional(),
            "firstName": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "avatarUrl": t.string().optional(),
            "name": t.string().optional(),
            "organizationInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoOut"]
            ).optional(),
            "botInfo": t.proxy(renames["BotInfoOut"]).optional(),
            "userAccountState": t.string().optional(),
            "phoneNumber": t.array(
                t.proxy(renames["AppsDynamiteSharedPhoneNumberOut"])
            ).optional(),
            "isAnonymous": t.boolean().optional(),
            "blockRelationship": t.proxy(
                renames["AppsDynamiteSharedUserBlockRelationshipOut"]
            ).optional(),
            "deleted": t.boolean().optional(),
            "email": t.string().optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "gender": t.string().optional(),
            "userProfileVisibility": t.string().optional(),
            "lastName": t.string().optional(),
            "firstName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["YouTubeBroadcastSessionInfoIn"] = t.struct(
        {
            "youTubeLiveBroadcastEvent": t.proxy(
                renames["YouTubeLiveBroadcastEventIn"]
            ).optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
            "broadcastStats": t.proxy(renames["YouTubeBroadcastStatsIn"]).optional(),
            "youTubeBroadcastSessionId": t.string().optional(),
        }
    ).named(renames["YouTubeBroadcastSessionInfoIn"])
    types["YouTubeBroadcastSessionInfoOut"] = t.struct(
        {
            "youTubeLiveBroadcastEvent": t.proxy(
                renames["YouTubeLiveBroadcastEventOut"]
            ).optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "broadcastStats": t.proxy(renames["YouTubeBroadcastStatsOut"]).optional(),
            "youTubeBroadcastSessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeBroadcastSessionInfoOut"])
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
    types["OpenCreatedDraftActionMarkupIn"] = t.struct(
        {
            "draftId": t.string().optional(),
            "draftThreadServerPermId": t.string().optional(),
            "draftThreadId": t.string().optional(),
            "draftStorageId": t.string().optional(),
        }
    ).named(renames["OpenCreatedDraftActionMarkupIn"])
    types["OpenCreatedDraftActionMarkupOut"] = t.struct(
        {
            "draftId": t.string().optional(),
            "draftThreadServerPermId": t.string().optional(),
            "draftThreadId": t.string().optional(),
            "draftStorageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenCreatedDraftActionMarkupOut"])
    types["ImageIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "imageUrl": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "onClick": t.proxy(renames["OnClickIn"]),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "imageUrl": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["SelectionControlIn"] = t.struct(
        {
            "name": t.string().optional(),
            "items": t.array(t.proxy(renames["SelectionItemIn"])).optional(),
            "label": t.string().optional(),
            "type": t.string(),
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
        }
    ).named(renames["SelectionControlIn"])
    types["SelectionControlOut"] = t.struct(
        {
            "name": t.string().optional(),
            "items": t.array(t.proxy(renames["SelectionItemOut"])).optional(),
            "label": t.string().optional(),
            "type": t.string(),
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionControlOut"])
    types["TransientDataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TransientDataIn"]
    )
    types["TransientDataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TransientDataOut"])
    types["GetSearchApplicationQueryStatsResponseIn"] = t.struct(
        {
            "totalQueryCount": t.string().optional(),
            "stats": t.array(
                t.proxy(renames["SearchApplicationQueryStatsIn"])
            ).optional(),
        }
    ).named(renames["GetSearchApplicationQueryStatsResponseIn"])
    types["GetSearchApplicationQueryStatsResponseOut"] = t.struct(
        {
            "totalQueryCount": t.string().optional(),
            "stats": t.array(
                t.proxy(renames["SearchApplicationQueryStatsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationQueryStatsResponseOut"])
    types["ImageCropStyleIn"] = t.struct(
        {"aspectRatio": t.number().optional(), "type": t.string().optional()}
    ).named(renames["ImageCropStyleIn"])
    types["ImageCropStyleOut"] = t.struct(
        {
            "aspectRatio": t.number().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageCropStyleOut"])
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
    types["MetadataIn"] = t.struct(
        {
            "objectType": t.string().optional(),
            "displayOptions": t.proxy(renames["ResultDisplayMetadataIn"]).optional(),
            "mimeType": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "updateTime": t.string().optional(),
            "fields": t.array(t.proxy(renames["NamedPropertyIn"])).optional(),
            "owner": t.proxy(renames["PersonIn"]).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "objectType": t.string().optional(),
            "displayOptions": t.proxy(renames["ResultDisplayMetadataOut"]).optional(),
            "mimeType": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "updateTime": t.string().optional(),
            "fields": t.array(t.proxy(renames["NamedPropertyOut"])).optional(),
            "owner": t.proxy(renames["PersonOut"]).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["MeetingSpaceIn"] = t.struct(
        {
            "phoneAccess": t.array(t.proxy(renames["PhoneAccessIn"])).optional(),
            "meetingCode": t.string().optional(),
            "meetingSpaceId": t.string().optional(),
            "gatewayAccess": t.proxy(renames["GatewayAccessIn"]).optional(),
            "universalPhoneAccess": t.proxy(
                renames["UniversalPhoneAccessIn"]
            ).optional(),
            "acceptedNumberClass": t.array(t.string()).optional(),
            "meetingAlias": t.string().optional(),
            "callInfo": t.proxy(renames["CallInfoIn"]).optional(),
            "broadcastAccess": t.proxy(renames["BroadcastAccessIn"]).optional(),
            "gatewaySipAccess": t.array(
                t.proxy(renames["GatewaySipAccessIn"])
            ).optional(),
            "meetingUrl": t.string().optional(),
            "settings": t.proxy(renames["SettingsIn"]).optional(),
        }
    ).named(renames["MeetingSpaceIn"])
    types["MeetingSpaceOut"] = t.struct(
        {
            "phoneAccess": t.array(t.proxy(renames["PhoneAccessOut"])).optional(),
            "meetingCode": t.string().optional(),
            "meetingSpaceId": t.string().optional(),
            "gatewayAccess": t.proxy(renames["GatewayAccessOut"]).optional(),
            "universalPhoneAccess": t.proxy(
                renames["UniversalPhoneAccessOut"]
            ).optional(),
            "acceptedNumberClass": t.array(t.string()).optional(),
            "meetingAlias": t.string().optional(),
            "callInfo": t.proxy(renames["CallInfoOut"]).optional(),
            "broadcastAccess": t.proxy(renames["BroadcastAccessOut"]).optional(),
            "gatewaySipAccess": t.array(
                t.proxy(renames["GatewaySipAccessOut"])
            ).optional(),
            "moreJoinUrl": t.string().optional(),
            "meetingUrl": t.string().optional(),
            "settings": t.proxy(renames["SettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeetingSpaceOut"])
    types["GetCustomerUserStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["CustomerUserStatsIn"]))}
    ).named(renames["GetCustomerUserStatsResponseIn"])
    types["GetCustomerUserStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerUserStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerUserStatsResponseOut"])
    types["AclInfoIn"] = t.struct(
        {
            "usersCount": t.integer().optional(),
            "scope": t.string().optional(),
            "groupsCount": t.integer().optional(),
        }
    ).named(renames["AclInfoIn"])
    types["AclInfoOut"] = t.struct(
        {
            "usersCount": t.integer().optional(),
            "scope": t.string().optional(),
            "groupsCount": t.integer().optional(),
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
    types["LegacyUploadMetadataIn"] = t.struct(
        {
            "legacyUniqueId": t.string().optional(),
            "uploadMetadata": t.proxy(renames["UploadMetadataIn"]).optional(),
        }
    ).named(renames["LegacyUploadMetadataIn"])
    types["LegacyUploadMetadataOut"] = t.struct(
        {
            "legacyUniqueId": t.string().optional(),
            "uploadMetadata": t.proxy(renames["UploadMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LegacyUploadMetadataOut"])
    types["MenuIn"] = t.struct(
        {
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
            "items": t.array(t.proxy(renames["MenuItemIn"])),
            "name": t.string().optional(),
            "label": t.string().optional(),
        }
    ).named(renames["MenuIn"])
    types["MenuOut"] = t.struct(
        {
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "items": t.array(t.proxy(renames["MenuItemOut"])),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MenuOut"])
    types["AppsDynamiteStorageDecoratedTextSwitchControlIn"] = t.struct(
        {
            "value": t.string().optional(),
            "controlType": t.string().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "selected": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextSwitchControlIn"])
    types["AppsDynamiteStorageDecoratedTextSwitchControlOut"] = t.struct(
        {
            "value": t.string().optional(),
            "controlType": t.string().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "selected": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextSwitchControlOut"])
    types["OtrModificationEventIn"] = t.struct(
        {
            "oldOtrStatus": t.string(),
            "newOtrStatus": t.string(),
            "oldOtrToggle": t.string(),
            "newOtrToggle": t.string(),
        }
    ).named(renames["OtrModificationEventIn"])
    types["OtrModificationEventOut"] = t.struct(
        {
            "oldOtrStatus": t.string(),
            "newOtrStatus": t.string(),
            "oldOtrToggle": t.string(),
            "newOtrToggle": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtrModificationEventOut"])
    types["TimestampValuesIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["TimestampValuesIn"]
    )
    types["TimestampValuesOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampValuesOut"])
    types["AppsDynamiteStorageTextParagraphIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["AppsDynamiteStorageTextParagraphIn"])
    types["AppsDynamiteStorageTextParagraphOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageTextParagraphOut"])
    types["FilterOptionsIn"] = t.struct(
        {
            "objectType": t.string().optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
        }
    ).named(renames["FilterOptionsIn"])
    types["FilterOptionsOut"] = t.struct(
        {
            "objectType": t.string().optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOptionsOut"])
    types["AppsDynamiteStorageOpenLinkIn"] = t.struct(
        {
            "appUri": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIn"]
            ).optional(),
            "onClose": t.string(),
            "openAs": t.string(),
            "url": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkIn"])
    types["AppsDynamiteStorageOpenLinkOut"] = t.struct(
        {
            "appUri": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriOut"]
            ).optional(),
            "onClose": t.string(),
            "openAs": t.string(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkOut"])
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
    types["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"])
    types["MessagePropsIn"] = t.struct(
        {"babelProps": t.proxy(renames["BabelMessagePropsIn"])}
    ).named(renames["MessagePropsIn"])
    types["MessagePropsOut"] = t.struct(
        {
            "babelProps": t.proxy(renames["BabelMessagePropsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessagePropsOut"])
    types["UpdateToRecipientsIn"] = t.struct(
        {"toRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateToRecipientsIn"])
    types["UpdateToRecipientsOut"] = t.struct(
        {
            "toRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateToRecipientsOut"])
    types["QuerySuggestionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["QuerySuggestionIn"]
    )
    types["QuerySuggestionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QuerySuggestionOut"])
    types["AppsDynamiteStorageSuggestionsSuggestionItemIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["AppsDynamiteStorageSuggestionsSuggestionItemIn"])
    types["AppsDynamiteStorageSuggestionsSuggestionItemOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteStorageSuggestionsSuggestionItemOut"])
    types["ContactGroupProtoIn"] = t.struct(
        {
            "groupId": t.string().optional(),
            "ownerGaiaId": t.string(),
            "requiredConsistencyTimestampUsec": t.string().optional(),
        }
    ).named(renames["ContactGroupProtoIn"])
    types["ContactGroupProtoOut"] = t.struct(
        {
            "groupId": t.string().optional(),
            "ownerGaiaId": t.string(),
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupProtoOut"])
    types["KeyValueIn"] = t.struct(
        {
            "button": t.proxy(renames["ButtonIn"]),
            "iconAltText": t.string().optional(),
            "contentMultiline": t.boolean(),
            "content": t.string().optional(),
            "switchWidget": t.proxy(renames["SwitchWidgetIn"]),
            "endIcon": t.proxy(renames["IconImageIn"]),
            "imageStyle": t.string(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "iconUrl": t.string(),
            "startIcon": t.proxy(renames["IconImageIn"]).optional(),
            "topLabel": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "icon": t.string(),
        }
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "button": t.proxy(renames["ButtonOut"]),
            "iconAltText": t.string().optional(),
            "contentMultiline": t.boolean(),
            "content": t.string().optional(),
            "switchWidget": t.proxy(renames["SwitchWidgetOut"]),
            "endIcon": t.proxy(renames["IconImageOut"]),
            "imageStyle": t.string(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "iconUrl": t.string(),
            "startIcon": t.proxy(renames["IconImageOut"]).optional(),
            "topLabel": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "icon": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
    types["PushItemRequestIn"] = t.struct(
        {
            "connectorName": t.string().optional(),
            "item": t.proxy(renames["PushItemIn"]).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["PushItemRequestIn"])
    types["PushItemRequestOut"] = t.struct(
        {
            "connectorName": t.string().optional(),
            "item": t.proxy(renames["PushItemOut"]).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushItemRequestOut"])
    types["BooleanOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["BooleanOperatorOptionsIn"])
    types["BooleanOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanOperatorOptionsOut"])
    types["ItemPartsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ItemPartsIn"]
    )
    types["ItemPartsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ItemPartsOut"])
    types["ResponseDebugInfoIn"] = t.struct(
        {"formattedDebugInfo": t.string().optional()}
    ).named(renames["ResponseDebugInfoIn"])
    types["ResponseDebugInfoOut"] = t.struct(
        {
            "formattedDebugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseDebugInfoOut"])
    types["MembershipChangeEventIn"] = t.struct(
        {
            "participantId": t.array(t.proxy(renames["StoredParticipantIdIn"])),
            "leaveReason": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["MembershipChangeEventIn"])
    types["MembershipChangeEventOut"] = t.struct(
        {
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "leaveReason": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipChangeEventOut"])
    types["FilterUpdateIn"] = t.struct(
        {
            "filterDeleted": t.proxy(renames["FilterDeletedIn"]),
            "filterCreated": t.proxy(renames["FilterCreatedIn"]),
            "filterId": t.string(),
        }
    ).named(renames["FilterUpdateIn"])
    types["FilterUpdateOut"] = t.struct(
        {
            "filterDeleted": t.proxy(renames["FilterDeletedOut"]),
            "filterCreated": t.proxy(renames["FilterCreatedOut"]),
            "filterId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterUpdateOut"])
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
    types["AppsDynamiteSharedGroupDetailsIn"] = t.struct(
        {"guidelines": t.string().optional(), "description": t.string().optional()}
    ).named(renames["AppsDynamiteSharedGroupDetailsIn"])
    types["AppsDynamiteSharedGroupDetailsOut"] = t.struct(
        {
            "guidelines": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedGroupDetailsOut"])
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
    types["InteractionDataIn"] = t.struct(
        {"url": t.proxy(renames["SafeUrlProtoIn"]).optional()}
    ).named(renames["InteractionDataIn"])
    types["InteractionDataOut"] = t.struct(
        {
            "url": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InteractionDataOut"])
    types["EmailOwnerProtoIn"] = t.struct({"email": t.string()}).named(
        renames["EmailOwnerProtoIn"]
    )
    types["EmailOwnerProtoOut"] = t.struct(
        {"email": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmailOwnerProtoOut"])
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
    types["DisplayedPropertyIn"] = t.struct(
        {"propertyName": t.string().optional()}
    ).named(renames["DisplayedPropertyIn"])
    types["DisplayedPropertyOut"] = t.struct(
        {
            "propertyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayedPropertyOut"])
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
    types["AppsDynamiteSharedOrganizationInfoIn"] = t.struct(
        {
            "consumerInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoConsumerInfoIn"]
            ),
            "customerInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoCustomerInfoIn"]
            ),
        }
    ).named(renames["AppsDynamiteSharedOrganizationInfoIn"])
    types["AppsDynamiteSharedOrganizationInfoOut"] = t.struct(
        {
            "consumerInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoConsumerInfoOut"]
            ),
            "customerInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoCustomerInfoOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedOrganizationInfoOut"])
    types["VoicePhoneNumberIn"] = t.struct(
        {
            "i18nData": t.proxy(renames["VoicePhoneNumberI18nDataIn"]).optional(),
            "e164": t.string().optional(),
        }
    ).named(renames["VoicePhoneNumberIn"])
    types["VoicePhoneNumberOut"] = t.struct(
        {
            "i18nData": t.proxy(renames["VoicePhoneNumberI18nDataOut"]).optional(),
            "e164": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoicePhoneNumberOut"])
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
    types["HistoryIn"] = t.struct(
        {"record": t.array(t.proxy(renames["HistoryRecordIn"]))}
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "record": t.array(t.proxy(renames["HistoryRecordOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
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
    types["GoogleChatV1WidgetMarkupTextParagraphIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleChatV1WidgetMarkupTextParagraphIn"])
    types["GoogleChatV1WidgetMarkupTextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChatV1WidgetMarkupTextParagraphOut"])
    types["FormActionIn"] = t.struct(
        {
            "loadIndicator": t.string(),
            "actionMethodName": t.string().optional(),
            "persistValues": t.boolean().optional(),
            "parameters": t.array(t.proxy(renames["ActionParameterIn"])),
        }
    ).named(renames["FormActionIn"])
    types["FormActionOut"] = t.struct(
        {
            "loadIndicator": t.string(),
            "actionMethodName": t.string().optional(),
            "persistValues": t.boolean().optional(),
            "parameters": t.array(t.proxy(renames["ActionParameterOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormActionOut"])
    types["UrlMetadataIn"] = t.struct(
        {
            "url": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "title": t.string().optional(),
            "imageWidth": t.string().optional(),
            "intImageHeight": t.integer().optional(),
            "snippet": t.string().optional(),
            "gwsUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "gwsUrlExpirationTimestamp": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
            "domain": t.string().optional(),
            "imageUrl": t.string().optional(),
            "intImageWidth": t.integer().optional(),
            "urlSource": t.string(),
            "redirectUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "mimeType": t.string().optional(),
            "imageHeight": t.string().optional(),
        }
    ).named(renames["UrlMetadataIn"])
    types["UrlMetadataOut"] = t.struct(
        {
            "url": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "title": t.string().optional(),
            "imageWidth": t.string().optional(),
            "intImageHeight": t.integer().optional(),
            "snippet": t.string().optional(),
            "gwsUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "gwsUrlExpirationTimestamp": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
            "domain": t.string().optional(),
            "imageUrl": t.string().optional(),
            "intImageWidth": t.integer().optional(),
            "urlSource": t.string(),
            "redirectUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "mimeType": t.string().optional(),
            "imageHeight": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlMetadataOut"])
    types["HtmlOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["HtmlOperatorOptionsIn"])
    types["HtmlOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlOperatorOptionsOut"])
    types["HangoutEventIn"] = t.struct(
        {
            "mediaType": t.string(),
            "hangoutDurationSecs": t.string(),
            "participantId": t.array(t.proxy(renames["StoredParticipantIdIn"])),
            "type": t.string(),
        }
    ).named(renames["HangoutEventIn"])
    types["HangoutEventOut"] = t.struct(
        {
            "mediaType": t.string(),
            "hangoutDurationSecs": t.string(),
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutEventOut"])
    types["SearchItemsByViewUrlRequestIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "pageToken": t.string().optional(),
            "viewUrl": t.string().optional(),
        }
    ).named(renames["SearchItemsByViewUrlRequestIn"])
    types["SearchItemsByViewUrlRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "pageToken": t.string().optional(),
            "viewUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchItemsByViewUrlRequestOut"])
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
    types["GoogleChatV1WidgetMarkupIn"] = t.struct(
        {
            "textParagraph": t.proxy(
                renames["GoogleChatV1WidgetMarkupTextParagraphIn"]
            ).optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupButtonIn"])
            ).optional(),
            "keyValue": t.proxy(
                renames["GoogleChatV1WidgetMarkupKeyValueIn"]
            ).optional(),
            "image": t.proxy(renames["GoogleChatV1WidgetMarkupImageIn"]).optional(),
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
            "keyValue": t.proxy(
                renames["GoogleChatV1WidgetMarkupKeyValueOut"]
            ).optional(),
            "image": t.proxy(renames["GoogleChatV1WidgetMarkupImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupOut"])
    types["AllAuthenticatedUsersProtoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AllAuthenticatedUsersProtoIn"])
    types["AllAuthenticatedUsersProtoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AllAuthenticatedUsersProtoOut"])
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
    types["DateValuesIn"] = t.struct(
        {"values": t.array(t.proxy(renames["DateIn"]))}
    ).named(renames["DateValuesIn"])
    types["DateValuesOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["DateOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateValuesOut"])
    types["AppsDynamiteSharedAssistantDebugContextIn"] = t.struct(
        {"query": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantDebugContextIn"])
    types["AppsDynamiteSharedAssistantDebugContextOut"] = t.struct(
        {
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantDebugContextOut"])
    types["ObjectDisplayOptionsIn"] = t.struct(
        {
            "metalines": t.array(t.proxy(renames["MetalineIn"])).optional(),
            "objectDisplayLabel": t.string().optional(),
        }
    ).named(renames["ObjectDisplayOptionsIn"])
    types["ObjectDisplayOptionsOut"] = t.struct(
        {
            "metalines": t.array(t.proxy(renames["MetalineOut"])).optional(),
            "objectDisplayLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectDisplayOptionsOut"])
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
    types["GridItemIn"] = t.struct(
        {
            "subtitle": t.string(),
            "textAlignment": t.string(),
            "title": t.string().optional(),
            "identifier": t.string().optional(),
            "image": t.proxy(renames["ImageComponentIn"]),
            "layout": t.string(),
        }
    ).named(renames["GridItemIn"])
    types["GridItemOut"] = t.struct(
        {
            "subtitle": t.string(),
            "textAlignment": t.string(),
            "title": t.string().optional(),
            "identifier": t.string().optional(),
            "image": t.proxy(renames["ImageComponentOut"]),
            "layout": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridItemOut"])
    types["OpenLinkIn"] = t.struct(
        {
            "openAs": t.string(),
            "loadIndicator": t.string().optional(),
            "url": t.string(),
            "onClose": t.string(),
        }
    ).named(renames["OpenLinkIn"])
    types["OpenLinkOut"] = t.struct(
        {
            "openAs": t.string(),
            "loadIndicator": t.string().optional(),
            "url": t.string(),
            "onClose": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenLinkOut"])
    types["FuseboxItemThreadMatchInfoIn"] = t.struct(
        {
            "matchingItemKey": t.array(t.proxy(renames["MultiKeyIn"])).optional(),
            "lastMatchingItemKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "rank": t.proxy(renames["RankIn"]).optional(),
            "lastMatchingItemId": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["FuseboxItemThreadMatchInfoIn"])
    types["FuseboxItemThreadMatchInfoOut"] = t.struct(
        {
            "matchingItemKey": t.array(t.proxy(renames["MultiKeyOut"])).optional(),
            "lastMatchingItemKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "rank": t.proxy(renames["RankOut"]).optional(),
            "lastMatchingItemId": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FuseboxItemThreadMatchInfoOut"])
    types["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"])
    types["OAuthConsumerProtoIn"] = t.struct({"domain": t.string()}).named(
        renames["OAuthConsumerProtoIn"]
    )
    types["OAuthConsumerProtoOut"] = t.struct(
        {"domain": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OAuthConsumerProtoOut"])
    types["ResultDebugInfoIn"] = t.struct(
        {"formattedDebugInfo": t.string().optional()}
    ).named(renames["ResultDebugInfoIn"])
    types["ResultDebugInfoOut"] = t.struct(
        {
            "formattedDebugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDebugInfoOut"])
    types["TransactionDebugInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TransactionDebugInfoIn"]
    )
    types["TransactionDebugInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TransactionDebugInfoOut"])
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
    types["MemberIn"] = t.struct(
        {"roster": t.proxy(renames["RosterIn"]), "user": t.proxy(renames["UserIn"])}
    ).named(renames["MemberIn"])
    types["MemberOut"] = t.struct(
        {
            "roster": t.proxy(renames["RosterOut"]),
            "user": t.proxy(renames["UserOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberOut"])
    types["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"])
    types[
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"]
    )
    types["LabelsIn"] = t.struct(
        {
            "displayName": t.array(t.string()).optional(),
            "id": t.array(t.string()).optional(),
        }
    ).named(renames["LabelsIn"])
    types["LabelsOut"] = t.struct(
        {
            "displayName": t.array(t.string()).optional(),
            "id": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelsOut"])
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
    types["GroupLinkSharingModificationEventIn"] = t.struct(
        {"newStatus": t.string()}
    ).named(renames["GroupLinkSharingModificationEventIn"])
    types["GroupLinkSharingModificationEventOut"] = t.struct(
        {"newStatus": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GroupLinkSharingModificationEventOut"])
    types["DlpActionIn"] = t.struct(
        {"unsafeHtmlMessageBody": t.string().optional(), "actionType": t.string()}
    ).named(renames["DlpActionIn"])
    types["DlpActionOut"] = t.struct(
        {
            "unsafeHtmlMessageBody": t.string().optional(),
            "actionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpActionOut"])
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
    types["RetrievalImportanceIn"] = t.struct(
        {"importance": t.string().optional()}
    ).named(renames["RetrievalImportanceIn"])
    types["RetrievalImportanceOut"] = t.struct(
        {
            "importance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrievalImportanceOut"])
    types["QuotedMessageMetadataIn"] = t.struct(
        {
            "lastUpdateTimeWhenQuotedMicros": t.string().optional(),
            "messageId": t.proxy(renames["MessageIdIn"]).optional(),
        }
    ).named(renames["QuotedMessageMetadataIn"])
    types["QuotedMessageMetadataOut"] = t.struct(
        {
            "creatorId": t.proxy(renames["UserIdOut"]).optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsOut"]
            ).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "lastUpdateTimeWhenQuotedMicros": t.string().optional(),
            "messageState": t.string().optional(),
            "botAttachmentState": t.string().optional(),
            "messageId": t.proxy(renames["MessageIdOut"]).optional(),
            "lastEditTimeMicros": t.string().optional(),
            "textBody": t.string().optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataOut"])).optional(),
            "updaterId": t.proxy(renames["UserIdOut"]).optional(),
            "createTimeMicros": t.string().optional(),
            "appProfile": t.proxy(
                renames["AppsDynamiteSharedAppProfileOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotedMessageMetadataOut"])
    types["LabelRemovedIn"] = t.struct(
        {
            "labelId": t.string(),
            "labelName": t.string(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
            "syncId": t.integer(),
        }
    ).named(renames["LabelRemovedIn"])
    types["LabelRemovedOut"] = t.struct(
        {
            "labelId": t.string(),
            "labelName": t.string(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "syncId": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelRemovedOut"])
    types["TextParagraphIn"] = t.struct({"text": t.string()}).named(
        renames["TextParagraphIn"]
    )
    types["TextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextParagraphOut"])
    types["AbuseReportingConfigIn"] = t.struct(
        {
            "recordingAllowed": t.boolean().optional(),
            "writtenUgcAllowed": t.boolean().optional(),
        }
    ).named(renames["AbuseReportingConfigIn"])
    types["AbuseReportingConfigOut"] = t.struct(
        {
            "recordingAllowed": t.boolean().optional(),
            "writtenUgcAllowed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbuseReportingConfigOut"])
    types["CallSettingsIn"] = t.struct(
        {
            "allowJoiningBeforeHost": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "audioLock": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "accessLock": t.boolean().optional(),
            "videoLock": t.boolean().optional(),
            "chatLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "accessType": t.string().optional(),
        }
    ).named(renames["CallSettingsIn"])
    types["CallSettingsOut"] = t.struct(
        {
            "allowJoiningBeforeHost": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "audioLock": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "accessLock": t.boolean().optional(),
            "videoLock": t.boolean().optional(),
            "chatLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "accessType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CallSettingsOut"])

    functions = {}
    functions["mediaUpload"] = cloudsearch.post(
        "v1/media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["MediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetIndex"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "toDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetSearchapplication"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "toDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetQuery"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "toDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetUser"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "toDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetSession"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "toDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsQuerySearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/query/{name}",
        t.struct(
            {
                "fromDate.year": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "name": t.string().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationQueryStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsIndexDatasourcesGet"] = cloudsearch.get(
        "v1/stats/index/{name}",
        t.struct(
            {
                "toDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "name": t.string().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDataSourceIndexStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsSessionSearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/session/{name}",
        t.struct(
            {
                "toDate.month": t.integer().optional(),
                "name": t.string().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsUserSearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/user/{name}",
        t.struct(
            {
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "name": t.string().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugIdentitysourcesUnmappedidsList"] = cloudsearch.get(
        "v1/debug/{parent}/unmappedids",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "resolutionStatusCode": t.string().optional(),
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
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "userResourceName": t.string(),
                "groupResourceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListItemNamesForUnmappedIdentityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsCheckAccess"] = cloudsearch.post(
        "v1/debug/{name}/items:searchByViewUrl",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "pageToken": t.string().optional(),
                "viewUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchItemsByViewUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsSearchByViewUrl"] = cloudsearch.post(
        "v1/debug/{name}/items:searchByViewUrl",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "pageToken": t.string().optional(),
                "viewUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchItemsByViewUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsUnmappedidsList"] = cloudsearch.get(
        "v1/debug/{parent}/unmappedids",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUnmappedIdentitiesResponseOut"]),
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
    functions["indexingDatasourcesDeleteSchema"] = cloudsearch.put(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesGetSchema"] = cloudsearch.put(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesUpdateSchema"] = cloudsearch.put(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsGet"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsList"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsDelete"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsIndex"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsUnreserve"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsUpload"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsPush"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsPoll"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsDeleteQueueItems"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "queue": t.string().optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsGetCustomer"] = cloudsearch.patch(
        "v1/settings/customer",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "vpcSettings": t.proxy(renames["VPCSettingsIn"]).optional(),
                "auditLoggingSettings": t.proxy(
                    renames["AuditLoggingSettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsUpdateCustomer"] = cloudsearch.patch(
        "v1/settings/customer",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "vpcSettings": t.proxy(renames["VPCSettingsIn"]).optional(),
                "auditLoggingSettings": t.proxy(
                    renames["AuditLoggingSettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesUpdate"] = cloudsearch.delete(
        "v1/settings/{name}",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesList"] = cloudsearch.delete(
        "v1/settings/{name}",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesCreate"] = cloudsearch.delete(
        "v1/settings/{name}",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesGet"] = cloudsearch.delete(
        "v1/settings/{name}",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesPatch"] = cloudsearch.delete(
        "v1/settings/{name}",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesDelete"] = cloudsearch.delete(
        "v1/settings/{name}",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsUpdate"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsDelete"] = cloudsearch.get(
        "v1/settings/searchapplications",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchApplicationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySuggest"] = cloudsearch.post(
        "v1/query/search",
        t.struct(
            {
                "queryInterpretationOptions": t.proxy(
                    renames["QueryInterpretationOptionsIn"]
                ).optional(),
                "sortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "contextAttributes": t.array(
                    t.proxy(renames["ContextAttributeIn"])
                ).optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "start": t.integer().optional(),
                "facetOptions": t.array(t.proxy(renames["FacetOptionsIn"])),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySearch"] = cloudsearch.post(
        "v1/query/search",
        t.struct(
            {
                "queryInterpretationOptions": t.proxy(
                    renames["QueryInterpretationOptionsIn"]
                ).optional(),
                "sortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "contextAttributes": t.array(
                    t.proxy(renames["ContextAttributeIn"])
                ).optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "start": t.integer().optional(),
                "facetOptions": t.array(t.proxy(renames["FacetOptionsIn"])),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySourcesList"] = cloudsearch.get(
        "v1/query/sources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "requestOptions.searchApplicationId": t.string().optional(),
                "requestOptions.languageCode": t.string().optional(),
                "requestOptions.timeZone": t.string().optional(),
                "requestOptions.debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListQuerySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudsearch", renames=renames, types=types, functions=functions
    )
