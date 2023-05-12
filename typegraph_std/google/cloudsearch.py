from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudsearch() -> Import:
    cloudsearch = HTTPRuntime("https://cloudsearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudsearch_1_ErrorResponse",
        "FieldViolationIn": "_cloudsearch_2_FieldViolationIn",
        "FieldViolationOut": "_cloudsearch_3_FieldViolationOut",
        "SortOptionsIn": "_cloudsearch_4_SortOptionsIn",
        "SortOptionsOut": "_cloudsearch_5_SortOptionsOut",
        "FacetBucketIn": "_cloudsearch_6_FacetBucketIn",
        "FacetBucketOut": "_cloudsearch_7_FacetBucketOut",
        "ListItemNamesForUnmappedIdentityResponseIn": "_cloudsearch_8_ListItemNamesForUnmappedIdentityResponseIn",
        "ListItemNamesForUnmappedIdentityResponseOut": "_cloudsearch_9_ListItemNamesForUnmappedIdentityResponseOut",
        "AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn": "_cloudsearch_10_AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn",
        "AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut": "_cloudsearch_11_AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut",
        "DateValuesIn": "_cloudsearch_12_DateValuesIn",
        "DateValuesOut": "_cloudsearch_13_DateValuesOut",
        "LabelRenamedIn": "_cloudsearch_14_LabelRenamedIn",
        "LabelRenamedOut": "_cloudsearch_15_LabelRenamedOut",
        "TransientDataIn": "_cloudsearch_16_TransientDataIn",
        "TransientDataOut": "_cloudsearch_17_TransientDataOut",
        "EmailAddressIn": "_cloudsearch_18_EmailAddressIn",
        "EmailAddressOut": "_cloudsearch_19_EmailAddressOut",
        "TriggerActionIn": "_cloudsearch_20_TriggerActionIn",
        "TriggerActionOut": "_cloudsearch_21_TriggerActionOut",
        "ListSearchApplicationsResponseIn": "_cloudsearch_22_ListSearchApplicationsResponseIn",
        "ListSearchApplicationsResponseOut": "_cloudsearch_23_ListSearchApplicationsResponseOut",
        "RequestOptionsIn": "_cloudsearch_24_RequestOptionsIn",
        "RequestOptionsOut": "_cloudsearch_25_RequestOptionsOut",
        "FacetOptionsIn": "_cloudsearch_26_FacetOptionsIn",
        "FacetOptionsOut": "_cloudsearch_27_FacetOptionsOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn": "_cloudsearch_28_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut": "_cloudsearch_29_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut",
        "ThreadUpdateIn": "_cloudsearch_30_ThreadUpdateIn",
        "ThreadUpdateOut": "_cloudsearch_31_ThreadUpdateOut",
        "BroadcastSessionInfoIn": "_cloudsearch_32_BroadcastSessionInfoIn",
        "BroadcastSessionInfoOut": "_cloudsearch_33_BroadcastSessionInfoOut",
        "ImapsyncFolderAttributeFolderMessageIn": "_cloudsearch_34_ImapsyncFolderAttributeFolderMessageIn",
        "ImapsyncFolderAttributeFolderMessageOut": "_cloudsearch_35_ImapsyncFolderAttributeFolderMessageOut",
        "EmailOwnerProtoIn": "_cloudsearch_36_EmailOwnerProtoIn",
        "EmailOwnerProtoOut": "_cloudsearch_37_EmailOwnerProtoOut",
        "ImapSessionContextIn": "_cloudsearch_38_ImapSessionContextIn",
        "ImapSessionContextOut": "_cloudsearch_39_ImapSessionContextOut",
        "CallSettingsIn": "_cloudsearch_40_CallSettingsIn",
        "CallSettingsOut": "_cloudsearch_41_CallSettingsOut",
        "AppsDynamiteStorageDecoratedTextSwitchControlIn": "_cloudsearch_42_AppsDynamiteStorageDecoratedTextSwitchControlIn",
        "AppsDynamiteStorageDecoratedTextSwitchControlOut": "_cloudsearch_43_AppsDynamiteStorageDecoratedTextSwitchControlOut",
        "TaskActionMarkupIn": "_cloudsearch_44_TaskActionMarkupIn",
        "TaskActionMarkupOut": "_cloudsearch_45_TaskActionMarkupOut",
        "ItemIn": "_cloudsearch_46_ItemIn",
        "ItemOut": "_cloudsearch_47_ItemOut",
        "AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn": "_cloudsearch_48_AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn",
        "AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut": "_cloudsearch_49_AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut",
        "IntegrationConfigUpdatedMetadataIn": "_cloudsearch_50_IntegrationConfigUpdatedMetadataIn",
        "IntegrationConfigUpdatedMetadataOut": "_cloudsearch_51_IntegrationConfigUpdatedMetadataOut",
        "AppsDynamiteSharedAppProfileIn": "_cloudsearch_52_AppsDynamiteSharedAppProfileIn",
        "AppsDynamiteSharedAppProfileOut": "_cloudsearch_53_AppsDynamiteSharedAppProfileOut",
        "UpdateBodyIn": "_cloudsearch_54_UpdateBodyIn",
        "UpdateBodyOut": "_cloudsearch_55_UpdateBodyOut",
        "AppsDynamiteSharedActivityFeedAnnotationDataIn": "_cloudsearch_56_AppsDynamiteSharedActivityFeedAnnotationDataIn",
        "AppsDynamiteSharedActivityFeedAnnotationDataOut": "_cloudsearch_57_AppsDynamiteSharedActivityFeedAnnotationDataOut",
        "IndexItemOptionsIn": "_cloudsearch_58_IndexItemOptionsIn",
        "IndexItemOptionsOut": "_cloudsearch_59_IndexItemOptionsOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn": "_cloudsearch_60_AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut": "_cloudsearch_61_AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut",
        "ValueFilterIn": "_cloudsearch_62_ValueFilterIn",
        "ValueFilterOut": "_cloudsearch_63_ValueFilterOut",
        "StatusIn": "_cloudsearch_64_StatusIn",
        "StatusOut": "_cloudsearch_65_StatusOut",
        "OperationIn": "_cloudsearch_66_OperationIn",
        "OperationOut": "_cloudsearch_67_OperationOut",
        "AppsDynamiteStorageSuggestionsIn": "_cloudsearch_68_AppsDynamiteStorageSuggestionsIn",
        "AppsDynamiteStorageSuggestionsOut": "_cloudsearch_69_AppsDynamiteStorageSuggestionsOut",
        "TopicStateIn": "_cloudsearch_70_TopicStateIn",
        "TopicStateOut": "_cloudsearch_71_TopicStateOut",
        "OAuthConsumerProtoIn": "_cloudsearch_72_OAuthConsumerProtoIn",
        "OAuthConsumerProtoOut": "_cloudsearch_73_OAuthConsumerProtoOut",
        "AppsDynamiteSharedCallAnnotationDataIn": "_cloudsearch_74_AppsDynamiteSharedCallAnnotationDataIn",
        "AppsDynamiteSharedCallAnnotationDataOut": "_cloudsearch_75_AppsDynamiteSharedCallAnnotationDataOut",
        "CardCapabilityMetadataIn": "_cloudsearch_76_CardCapabilityMetadataIn",
        "CardCapabilityMetadataOut": "_cloudsearch_77_CardCapabilityMetadataOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn": "_cloudsearch_78_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut": "_cloudsearch_79_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut",
        "AppsDynamiteSharedDlpMetricsMetadataIn": "_cloudsearch_80_AppsDynamiteSharedDlpMetricsMetadataIn",
        "AppsDynamiteSharedDlpMetricsMetadataOut": "_cloudsearch_81_AppsDynamiteSharedDlpMetricsMetadataOut",
        "HtmlOperatorOptionsIn": "_cloudsearch_82_HtmlOperatorOptionsIn",
        "HtmlOperatorOptionsOut": "_cloudsearch_83_HtmlOperatorOptionsOut",
        "AppsDynamiteStorageColumnsIn": "_cloudsearch_84_AppsDynamiteStorageColumnsIn",
        "AppsDynamiteStorageColumnsOut": "_cloudsearch_85_AppsDynamiteStorageColumnsOut",
        "LabelUpdatedIn": "_cloudsearch_86_LabelUpdatedIn",
        "LabelUpdatedOut": "_cloudsearch_87_LabelUpdatedOut",
        "GoogleChatV1WidgetMarkupIn": "_cloudsearch_88_GoogleChatV1WidgetMarkupIn",
        "GoogleChatV1WidgetMarkupOut": "_cloudsearch_89_GoogleChatV1WidgetMarkupOut",
        "QuotedMessageMetadataIn": "_cloudsearch_90_QuotedMessageMetadataIn",
        "QuotedMessageMetadataOut": "_cloudsearch_91_QuotedMessageMetadataOut",
        "SectionIn": "_cloudsearch_92_SectionIn",
        "SectionOut": "_cloudsearch_93_SectionOut",
        "GoogleChatV1ContextualAddOnMarkupIn": "_cloudsearch_94_GoogleChatV1ContextualAddOnMarkupIn",
        "GoogleChatV1ContextualAddOnMarkupOut": "_cloudsearch_95_GoogleChatV1ContextualAddOnMarkupOut",
        "TriggersIn": "_cloudsearch_96_TriggersIn",
        "TriggersOut": "_cloudsearch_97_TriggersOut",
        "ReferencesIn": "_cloudsearch_98_ReferencesIn",
        "ReferencesOut": "_cloudsearch_99_ReferencesOut",
        "AppsDynamiteSharedJustificationIn": "_cloudsearch_100_AppsDynamiteSharedJustificationIn",
        "AppsDynamiteSharedJustificationOut": "_cloudsearch_101_AppsDynamiteSharedJustificationOut",
        "PrefDeletedIn": "_cloudsearch_102_PrefDeletedIn",
        "PrefDeletedOut": "_cloudsearch_103_PrefDeletedOut",
        "ResponseDebugInfoIn": "_cloudsearch_104_ResponseDebugInfoIn",
        "ResponseDebugInfoOut": "_cloudsearch_105_ResponseDebugInfoOut",
        "SocialGraphNodeProtoIn": "_cloudsearch_106_SocialGraphNodeProtoIn",
        "SocialGraphNodeProtoOut": "_cloudsearch_107_SocialGraphNodeProtoOut",
        "TimestampOperatorOptionsIn": "_cloudsearch_108_TimestampOperatorOptionsIn",
        "TimestampOperatorOptionsOut": "_cloudsearch_109_TimestampOperatorOptionsOut",
        "IdIn": "_cloudsearch_110_IdIn",
        "IdOut": "_cloudsearch_111_IdOut",
        "ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn": "_cloudsearch_112_ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut": "_cloudsearch_113_ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut",
        "CardHeaderIn": "_cloudsearch_114_CardHeaderIn",
        "CardHeaderOut": "_cloudsearch_115_CardHeaderOut",
        "RecordingSessionInfoIn": "_cloudsearch_116_RecordingSessionInfoIn",
        "RecordingSessionInfoOut": "_cloudsearch_117_RecordingSessionInfoOut",
        "AppsDynamiteSharedCustomEmojiIn": "_cloudsearch_118_AppsDynamiteSharedCustomEmojiIn",
        "AppsDynamiteSharedCustomEmojiOut": "_cloudsearch_119_AppsDynamiteSharedCustomEmojiOut",
        "DoubleValuesIn": "_cloudsearch_120_DoubleValuesIn",
        "DoubleValuesOut": "_cloudsearch_121_DoubleValuesOut",
        "FilterCreatedIn": "_cloudsearch_122_FilterCreatedIn",
        "FilterCreatedOut": "_cloudsearch_123_FilterCreatedOut",
        "AppsDynamiteV1ApiCompatV1ActionIn": "_cloudsearch_124_AppsDynamiteV1ApiCompatV1ActionIn",
        "AppsDynamiteV1ApiCompatV1ActionOut": "_cloudsearch_125_AppsDynamiteV1ApiCompatV1ActionOut",
        "DeleteQueueItemsRequestIn": "_cloudsearch_126_DeleteQueueItemsRequestIn",
        "DeleteQueueItemsRequestOut": "_cloudsearch_127_DeleteQueueItemsRequestOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataIn": "_cloudsearch_128_AppsDynamiteSharedCalendarEventAnnotationDataIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataOut": "_cloudsearch_129_AppsDynamiteSharedCalendarEventAnnotationDataOut",
        "SearchResponseIn": "_cloudsearch_130_SearchResponseIn",
        "SearchResponseOut": "_cloudsearch_131_SearchResponseOut",
        "GetDataSourceIndexStatsResponseIn": "_cloudsearch_132_GetDataSourceIndexStatsResponseIn",
        "GetDataSourceIndexStatsResponseOut": "_cloudsearch_133_GetDataSourceIndexStatsResponseOut",
        "DynamiteSpacesScoringInfoIn": "_cloudsearch_134_DynamiteSpacesScoringInfoIn",
        "DynamiteSpacesScoringInfoOut": "_cloudsearch_135_DynamiteSpacesScoringInfoOut",
        "GoogleChatV1WidgetMarkupButtonIn": "_cloudsearch_136_GoogleChatV1WidgetMarkupButtonIn",
        "GoogleChatV1WidgetMarkupButtonOut": "_cloudsearch_137_GoogleChatV1WidgetMarkupButtonOut",
        "SelectionItemIn": "_cloudsearch_138_SelectionItemIn",
        "SelectionItemOut": "_cloudsearch_139_SelectionItemOut",
        "SearchRequestIn": "_cloudsearch_140_SearchRequestIn",
        "SearchRequestOut": "_cloudsearch_141_SearchRequestOut",
        "GoogleChatV1WidgetMarkupOpenLinkIn": "_cloudsearch_142_GoogleChatV1WidgetMarkupOpenLinkIn",
        "GoogleChatV1WidgetMarkupOpenLinkOut": "_cloudsearch_143_GoogleChatV1WidgetMarkupOpenLinkOut",
        "RestrictItemIn": "_cloudsearch_144_RestrictItemIn",
        "RestrictItemOut": "_cloudsearch_145_RestrictItemOut",
        "ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn": "_cloudsearch_146_ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut": "_cloudsearch_147_ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut",
        "ClusterInfoIn": "_cloudsearch_148_ClusterInfoIn",
        "ClusterInfoOut": "_cloudsearch_149_ClusterInfoOut",
        "ImapUpdateIn": "_cloudsearch_150_ImapUpdateIn",
        "ImapUpdateOut": "_cloudsearch_151_ImapUpdateOut",
        "LdapUserProtoIn": "_cloudsearch_152_LdapUserProtoIn",
        "LdapUserProtoOut": "_cloudsearch_153_LdapUserProtoOut",
        "CallInfoIn": "_cloudsearch_154_CallInfoIn",
        "CallInfoOut": "_cloudsearch_155_CallInfoOut",
        "RbacRoleProtoIn": "_cloudsearch_156_RbacRoleProtoIn",
        "RbacRoleProtoOut": "_cloudsearch_157_RbacRoleProtoOut",
        "AppsDynamiteSharedTextSegmentsWithDescriptionIn": "_cloudsearch_158_AppsDynamiteSharedTextSegmentsWithDescriptionIn",
        "AppsDynamiteSharedTextSegmentsWithDescriptionOut": "_cloudsearch_159_AppsDynamiteSharedTextSegmentsWithDescriptionOut",
        "RosterIdIn": "_cloudsearch_160_RosterIdIn",
        "RosterIdOut": "_cloudsearch_161_RosterIdOut",
        "GoogleChatV1WidgetMarkupImageIn": "_cloudsearch_162_GoogleChatV1WidgetMarkupImageIn",
        "GoogleChatV1WidgetMarkupImageOut": "_cloudsearch_163_GoogleChatV1WidgetMarkupImageOut",
        "CustomEmojiMetadataIn": "_cloudsearch_164_CustomEmojiMetadataIn",
        "CustomEmojiMetadataOut": "_cloudsearch_165_CustomEmojiMetadataOut",
        "RecordingInfoIn": "_cloudsearch_166_RecordingInfoIn",
        "RecordingInfoOut": "_cloudsearch_167_RecordingInfoOut",
        "AppsDynamiteSharedContentReportTypeIn": "_cloudsearch_168_AppsDynamiteSharedContentReportTypeIn",
        "AppsDynamiteSharedContentReportTypeOut": "_cloudsearch_169_AppsDynamiteSharedContentReportTypeOut",
        "AppsDynamiteSharedChatItemIn": "_cloudsearch_170_AppsDynamiteSharedChatItemIn",
        "AppsDynamiteSharedChatItemOut": "_cloudsearch_171_AppsDynamiteSharedChatItemOut",
        "GaiaGroupProtoIn": "_cloudsearch_172_GaiaGroupProtoIn",
        "GaiaGroupProtoOut": "_cloudsearch_173_GaiaGroupProtoOut",
        "InviteeInfoIn": "_cloudsearch_174_InviteeInfoIn",
        "InviteeInfoOut": "_cloudsearch_175_InviteeInfoOut",
        "GetSearchApplicationSessionStatsResponseIn": "_cloudsearch_176_GetSearchApplicationSessionStatsResponseIn",
        "GetSearchApplicationSessionStatsResponseOut": "_cloudsearch_177_GetSearchApplicationSessionStatsResponseOut",
        "GoogleChatV1ContextualAddOnMarkupCardCardActionIn": "_cloudsearch_178_GoogleChatV1ContextualAddOnMarkupCardCardActionIn",
        "GoogleChatV1ContextualAddOnMarkupCardCardActionOut": "_cloudsearch_179_GoogleChatV1ContextualAddOnMarkupCardCardActionOut",
        "ButtonIn": "_cloudsearch_180_ButtonIn",
        "ButtonOut": "_cloudsearch_181_ButtonOut",
        "AttachmentIn": "_cloudsearch_182_AttachmentIn",
        "AttachmentOut": "_cloudsearch_183_AttachmentOut",
        "MetalineIn": "_cloudsearch_184_MetalineIn",
        "MetalineOut": "_cloudsearch_185_MetalineOut",
        "AppsDynamiteStorageImageIn": "_cloudsearch_186_AppsDynamiteStorageImageIn",
        "AppsDynamiteStorageImageOut": "_cloudsearch_187_AppsDynamiteStorageImageOut",
        "ChatClientActionMarkupIn": "_cloudsearch_188_ChatClientActionMarkupIn",
        "ChatClientActionMarkupOut": "_cloudsearch_189_ChatClientActionMarkupOut",
        "AppsDynamiteSharedAssistantSessionContextIn": "_cloudsearch_190_AppsDynamiteSharedAssistantSessionContextIn",
        "AppsDynamiteSharedAssistantSessionContextOut": "_cloudsearch_191_AppsDynamiteSharedAssistantSessionContextOut",
        "AppsDynamiteStorageImageCropStyleIn": "_cloudsearch_192_AppsDynamiteStorageImageCropStyleIn",
        "AppsDynamiteStorageImageCropStyleOut": "_cloudsearch_193_AppsDynamiteStorageImageCropStyleOut",
        "AnnotationIn": "_cloudsearch_194_AnnotationIn",
        "AnnotationOut": "_cloudsearch_195_AnnotationOut",
        "DynamiteMessagesScoringInfoIn": "_cloudsearch_196_DynamiteMessagesScoringInfoIn",
        "DynamiteMessagesScoringInfoOut": "_cloudsearch_197_DynamiteMessagesScoringInfoOut",
        "WonderCardDeleteIn": "_cloudsearch_198_WonderCardDeleteIn",
        "WonderCardDeleteOut": "_cloudsearch_199_WonderCardDeleteOut",
        "AppsDynamiteStorageActionActionParameterIn": "_cloudsearch_200_AppsDynamiteStorageActionActionParameterIn",
        "AppsDynamiteStorageActionActionParameterOut": "_cloudsearch_201_AppsDynamiteStorageActionActionParameterOut",
        "TextParagraphIn": "_cloudsearch_202_TextParagraphIn",
        "TextParagraphOut": "_cloudsearch_203_TextParagraphOut",
        "ChatConserverDynamitePlaceholderMetadataEditMetadataIn": "_cloudsearch_204_ChatConserverDynamitePlaceholderMetadataEditMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataEditMetadataOut": "_cloudsearch_205_ChatConserverDynamitePlaceholderMetadataEditMetadataOut",
        "SquareProtoIn": "_cloudsearch_206_SquareProtoIn",
        "SquareProtoOut": "_cloudsearch_207_SquareProtoOut",
        "UniversalPhoneAccessIn": "_cloudsearch_208_UniversalPhoneAccessIn",
        "UniversalPhoneAccessOut": "_cloudsearch_209_UniversalPhoneAccessOut",
        "AppsDynamiteStorageCardCardHeaderIn": "_cloudsearch_210_AppsDynamiteStorageCardCardHeaderIn",
        "AppsDynamiteStorageCardCardHeaderOut": "_cloudsearch_211_AppsDynamiteStorageCardCardHeaderOut",
        "RequestFileScopeIn": "_cloudsearch_212_RequestFileScopeIn",
        "RequestFileScopeOut": "_cloudsearch_213_RequestFileScopeOut",
        "AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn": "_cloudsearch_214_AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut": "_cloudsearch_215_AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut",
        "AppIdIn": "_cloudsearch_216_AppIdIn",
        "AppIdOut": "_cloudsearch_217_AppIdOut",
        "DeleteMetadataIn": "_cloudsearch_218_DeleteMetadataIn",
        "DeleteMetadataOut": "_cloudsearch_219_DeleteMetadataOut",
        "AppsDynamiteStorageDateTimePickerIn": "_cloudsearch_220_AppsDynamiteStorageDateTimePickerIn",
        "AppsDynamiteStorageDateTimePickerOut": "_cloudsearch_221_AppsDynamiteStorageDateTimePickerOut",
        "GetCustomerQueryStatsResponseIn": "_cloudsearch_222_GetCustomerQueryStatsResponseIn",
        "GetCustomerQueryStatsResponseOut": "_cloudsearch_223_GetCustomerQueryStatsResponseOut",
        "MessageAddedIn": "_cloudsearch_224_MessageAddedIn",
        "MessageAddedOut": "_cloudsearch_225_MessageAddedOut",
        "MessageAttributesIn": "_cloudsearch_226_MessageAttributesIn",
        "MessageAttributesOut": "_cloudsearch_227_MessageAttributesOut",
        "SchemaIn": "_cloudsearch_228_SchemaIn",
        "SchemaOut": "_cloudsearch_229_SchemaOut",
        "WonderMessageMappingIn": "_cloudsearch_230_WonderMessageMappingIn",
        "WonderMessageMappingOut": "_cloudsearch_231_WonderMessageMappingOut",
        "KeyValueIn": "_cloudsearch_232_KeyValueIn",
        "KeyValueOut": "_cloudsearch_233_KeyValueOut",
        "IncomingWebhookChangedMetadataIn": "_cloudsearch_234_IncomingWebhookChangedMetadataIn",
        "IncomingWebhookChangedMetadataOut": "_cloudsearch_235_IncomingWebhookChangedMetadataOut",
        "ObjectPropertyOptionsIn": "_cloudsearch_236_ObjectPropertyOptionsIn",
        "ObjectPropertyOptionsOut": "_cloudsearch_237_ObjectPropertyOptionsOut",
        "ObjectValuesIn": "_cloudsearch_238_ObjectValuesIn",
        "ObjectValuesOut": "_cloudsearch_239_ObjectValuesOut",
        "DriveTimeSpanRestrictIn": "_cloudsearch_240_DriveTimeSpanRestrictIn",
        "DriveTimeSpanRestrictOut": "_cloudsearch_241_DriveTimeSpanRestrictOut",
        "GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn": "_cloudsearch_242_GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn",
        "GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut": "_cloudsearch_243_GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut",
        "MessageInfoIn": "_cloudsearch_244_MessageInfoIn",
        "MessageInfoOut": "_cloudsearch_245_MessageInfoOut",
        "TextKeyValueIn": "_cloudsearch_246_TextKeyValueIn",
        "TextKeyValueOut": "_cloudsearch_247_TextKeyValueOut",
        "ChatContentExtensionIn": "_cloudsearch_248_ChatContentExtensionIn",
        "ChatContentExtensionOut": "_cloudsearch_249_ChatContentExtensionOut",
        "ProcessingErrorIn": "_cloudsearch_250_ProcessingErrorIn",
        "ProcessingErrorOut": "_cloudsearch_251_ProcessingErrorOut",
        "CustomerIndexStatsIn": "_cloudsearch_252_CustomerIndexStatsIn",
        "CustomerIndexStatsOut": "_cloudsearch_253_CustomerIndexStatsOut",
        "ObjectDefinitionIn": "_cloudsearch_254_ObjectDefinitionIn",
        "ObjectDefinitionOut": "_cloudsearch_255_ObjectDefinitionOut",
        "ShareScopeIn": "_cloudsearch_256_ShareScopeIn",
        "ShareScopeOut": "_cloudsearch_257_ShareScopeOut",
        "AppsDynamiteSharedCallMetadataIn": "_cloudsearch_258_AppsDynamiteSharedCallMetadataIn",
        "AppsDynamiteSharedCallMetadataOut": "_cloudsearch_259_AppsDynamiteSharedCallMetadataOut",
        "TranscriptionSessionInfoIn": "_cloudsearch_260_TranscriptionSessionInfoIn",
        "TranscriptionSessionInfoOut": "_cloudsearch_261_TranscriptionSessionInfoOut",
        "AppsDynamiteStorageSelectionInputIn": "_cloudsearch_262_AppsDynamiteStorageSelectionInputIn",
        "AppsDynamiteStorageSelectionInputOut": "_cloudsearch_263_AppsDynamiteStorageSelectionInputOut",
        "SocialCommonAttachmentAttachmentIn": "_cloudsearch_264_SocialCommonAttachmentAttachmentIn",
        "SocialCommonAttachmentAttachmentOut": "_cloudsearch_265_SocialCommonAttachmentAttachmentOut",
        "AclFixStatusIn": "_cloudsearch_266_AclFixStatusIn",
        "AclFixStatusOut": "_cloudsearch_267_AclFixStatusOut",
        "TrustedResourceUrlProtoIn": "_cloudsearch_268_TrustedResourceUrlProtoIn",
        "TrustedResourceUrlProtoOut": "_cloudsearch_269_TrustedResourceUrlProtoOut",
        "GoogleChatV1ContextualAddOnMarkupCardIn": "_cloudsearch_270_GoogleChatV1ContextualAddOnMarkupCardIn",
        "GoogleChatV1ContextualAddOnMarkupCardOut": "_cloudsearch_271_GoogleChatV1ContextualAddOnMarkupCardOut",
        "QuerySourceIn": "_cloudsearch_272_QuerySourceIn",
        "QuerySourceOut": "_cloudsearch_273_QuerySourceOut",
        "DebugOptionsIn": "_cloudsearch_274_DebugOptionsIn",
        "DebugOptionsOut": "_cloudsearch_275_DebugOptionsOut",
        "AppsDynamiteStorageOpenLinkAppUriIntentIn": "_cloudsearch_276_AppsDynamiteStorageOpenLinkAppUriIntentIn",
        "AppsDynamiteStorageOpenLinkAppUriIntentOut": "_cloudsearch_277_AppsDynamiteStorageOpenLinkAppUriIntentOut",
        "PrincipalProtoIn": "_cloudsearch_278_PrincipalProtoIn",
        "PrincipalProtoOut": "_cloudsearch_279_PrincipalProtoOut",
        "AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn": "_cloudsearch_280_AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn",
        "AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut": "_cloudsearch_281_AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut",
        "MenuItemIn": "_cloudsearch_282_MenuItemIn",
        "MenuItemOut": "_cloudsearch_283_MenuItemOut",
        "UpdateBccRecipientsIn": "_cloudsearch_284_UpdateBccRecipientsIn",
        "UpdateBccRecipientsOut": "_cloudsearch_285_UpdateBccRecipientsOut",
        "CardActionIn": "_cloudsearch_286_CardActionIn",
        "CardActionOut": "_cloudsearch_287_CardActionOut",
        "AppsDynamiteSharedMessageInfoIn": "_cloudsearch_288_AppsDynamiteSharedMessageInfoIn",
        "AppsDynamiteSharedMessageInfoOut": "_cloudsearch_289_AppsDynamiteSharedMessageInfoOut",
        "TimestampValuesIn": "_cloudsearch_290_TimestampValuesIn",
        "TimestampValuesOut": "_cloudsearch_291_TimestampValuesOut",
        "StreamingSessionInfoIn": "_cloudsearch_292_StreamingSessionInfoIn",
        "StreamingSessionInfoOut": "_cloudsearch_293_StreamingSessionInfoOut",
        "GoogleDocsResultInfoIn": "_cloudsearch_294_GoogleDocsResultInfoIn",
        "GoogleDocsResultInfoOut": "_cloudsearch_295_GoogleDocsResultInfoOut",
        "RbacSubjectProtoIn": "_cloudsearch_296_RbacSubjectProtoIn",
        "RbacSubjectProtoOut": "_cloudsearch_297_RbacSubjectProtoOut",
        "VoicePhoneNumberI18nDataIn": "_cloudsearch_298_VoicePhoneNumberI18nDataIn",
        "VoicePhoneNumberI18nDataOut": "_cloudsearch_299_VoicePhoneNumberI18nDataOut",
        "CustomFunctionReturnValueMarkupIn": "_cloudsearch_300_CustomFunctionReturnValueMarkupIn",
        "CustomFunctionReturnValueMarkupOut": "_cloudsearch_301_CustomFunctionReturnValueMarkupOut",
        "UpdateSchemaRequestIn": "_cloudsearch_302_UpdateSchemaRequestIn",
        "UpdateSchemaRequestOut": "_cloudsearch_303_UpdateSchemaRequestOut",
        "FormatMetadataIn": "_cloudsearch_304_FormatMetadataIn",
        "FormatMetadataOut": "_cloudsearch_305_FormatMetadataOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn": "_cloudsearch_306_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut": "_cloudsearch_307_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn": "_cloudsearch_308_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut": "_cloudsearch_309_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut",
        "CardIn": "_cloudsearch_310_CardIn",
        "CardOut": "_cloudsearch_311_CardOut",
        "GroupDetailsUpdatedMetadataIn": "_cloudsearch_312_GroupDetailsUpdatedMetadataIn",
        "GroupDetailsUpdatedMetadataOut": "_cloudsearch_313_GroupDetailsUpdatedMetadataOut",
        "VPCSettingsIn": "_cloudsearch_314_VPCSettingsIn",
        "VPCSettingsOut": "_cloudsearch_315_VPCSettingsOut",
        "AppsDynamiteSharedGroupVisibilityIn": "_cloudsearch_316_AppsDynamiteSharedGroupVisibilityIn",
        "AppsDynamiteSharedGroupVisibilityOut": "_cloudsearch_317_AppsDynamiteSharedGroupVisibilityOut",
        "AppsDynamiteStorageOpenLinkAppUriIn": "_cloudsearch_318_AppsDynamiteStorageOpenLinkAppUriIn",
        "AppsDynamiteStorageOpenLinkAppUriOut": "_cloudsearch_319_AppsDynamiteStorageOpenLinkAppUriOut",
        "AppsDynamiteSharedJustificationPersonIn": "_cloudsearch_320_AppsDynamiteSharedJustificationPersonIn",
        "AppsDynamiteSharedJustificationPersonOut": "_cloudsearch_321_AppsDynamiteSharedJustificationPersonOut",
        "CaribouAttributeValueIn": "_cloudsearch_322_CaribouAttributeValueIn",
        "CaribouAttributeValueOut": "_cloudsearch_323_CaribouAttributeValueOut",
        "YoutubeMetadataIn": "_cloudsearch_324_YoutubeMetadataIn",
        "YoutubeMetadataOut": "_cloudsearch_325_YoutubeMetadataOut",
        "IconImageIn": "_cloudsearch_326_IconImageIn",
        "IconImageOut": "_cloudsearch_327_IconImageOut",
        "PostiniUserProtoIn": "_cloudsearch_328_PostiniUserProtoIn",
        "PostiniUserProtoOut": "_cloudsearch_329_PostiniUserProtoOut",
        "ItemContentIn": "_cloudsearch_330_ItemContentIn",
        "ItemContentOut": "_cloudsearch_331_ItemContentOut",
        "OsVersionIn": "_cloudsearch_332_OsVersionIn",
        "OsVersionOut": "_cloudsearch_333_OsVersionOut",
        "GridItemIn": "_cloudsearch_334_GridItemIn",
        "GridItemOut": "_cloudsearch_335_GridItemOut",
        "SegmentIn": "_cloudsearch_336_SegmentIn",
        "SegmentOut": "_cloudsearch_337_SegmentOut",
        "SheetsClientActionMarkupIn": "_cloudsearch_338_SheetsClientActionMarkupIn",
        "SheetsClientActionMarkupOut": "_cloudsearch_339_SheetsClientActionMarkupOut",
        "LabelDeletedIn": "_cloudsearch_340_LabelDeletedIn",
        "LabelDeletedOut": "_cloudsearch_341_LabelDeletedOut",
        "GoogleChatV1WidgetMarkupFormActionIn": "_cloudsearch_342_GoogleChatV1WidgetMarkupFormActionIn",
        "GoogleChatV1WidgetMarkupFormActionOut": "_cloudsearch_343_GoogleChatV1WidgetMarkupFormActionOut",
        "TopicStateUpdateIn": "_cloudsearch_344_TopicStateUpdateIn",
        "TopicStateUpdateOut": "_cloudsearch_345_TopicStateUpdateOut",
        "UploadMetadataIn": "_cloudsearch_346_UploadMetadataIn",
        "UploadMetadataOut": "_cloudsearch_347_UploadMetadataOut",
        "WidgetMarkupIn": "_cloudsearch_348_WidgetMarkupIn",
        "WidgetMarkupOut": "_cloudsearch_349_WidgetMarkupOut",
        "GetSearchApplicationQueryStatsResponseIn": "_cloudsearch_350_GetSearchApplicationQueryStatsResponseIn",
        "GetSearchApplicationQueryStatsResponseOut": "_cloudsearch_351_GetSearchApplicationQueryStatsResponseOut",
        "RequestFileScopeForActiveDocumentIn": "_cloudsearch_352_RequestFileScopeForActiveDocumentIn",
        "RequestFileScopeForActiveDocumentOut": "_cloudsearch_353_RequestFileScopeForActiveDocumentOut",
        "DriveMimeTypeRestrictIn": "_cloudsearch_354_DriveMimeTypeRestrictIn",
        "DriveMimeTypeRestrictOut": "_cloudsearch_355_DriveMimeTypeRestrictOut",
        "ImageComponentIn": "_cloudsearch_356_ImageComponentIn",
        "ImageComponentOut": "_cloudsearch_357_ImageComponentOut",
        "AppsDynamiteStorageGridIn": "_cloudsearch_358_AppsDynamiteStorageGridIn",
        "AppsDynamiteStorageGridOut": "_cloudsearch_359_AppsDynamiteStorageGridOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn": "_cloudsearch_360_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut": "_cloudsearch_361_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn": "_cloudsearch_362_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut": "_cloudsearch_363_AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut",
        "NamedPropertyIn": "_cloudsearch_364_NamedPropertyIn",
        "NamedPropertyOut": "_cloudsearch_365_NamedPropertyOut",
        "AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn": "_cloudsearch_366_AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut": "_cloudsearch_367_AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut",
        "SessionContextIn": "_cloudsearch_368_SessionContextIn",
        "SessionContextOut": "_cloudsearch_369_SessionContextOut",
        "AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn": "_cloudsearch_370_AppsDynamiteStorageOpenLinkAppUriIntentExtraDataIn",
        "AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut": "_cloudsearch_371_AppsDynamiteStorageOpenLinkAppUriIntentExtraDataOut",
        "RepositoryErrorIn": "_cloudsearch_372_RepositoryErrorIn",
        "RepositoryErrorOut": "_cloudsearch_373_RepositoryErrorOut",
        "SearchApplicationUserStatsIn": "_cloudsearch_374_SearchApplicationUserStatsIn",
        "SearchApplicationUserStatsOut": "_cloudsearch_375_SearchApplicationUserStatsOut",
        "AppsDynamiteSharedOrganizationInfoIn": "_cloudsearch_376_AppsDynamiteSharedOrganizationInfoIn",
        "AppsDynamiteSharedOrganizationInfoOut": "_cloudsearch_377_AppsDynamiteSharedOrganizationInfoOut",
        "DriveClientActionMarkupIn": "_cloudsearch_378_DriveClientActionMarkupIn",
        "DriveClientActionMarkupOut": "_cloudsearch_379_DriveClientActionMarkupOut",
        "AppsDynamiteSharedGroupDetailsIn": "_cloudsearch_380_AppsDynamiteSharedGroupDetailsIn",
        "AppsDynamiteSharedGroupDetailsOut": "_cloudsearch_381_AppsDynamiteSharedGroupDetailsOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn": "_cloudsearch_382_AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut": "_cloudsearch_383_AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut",
        "FormattingIn": "_cloudsearch_384_FormattingIn",
        "FormattingOut": "_cloudsearch_385_FormattingOut",
        "MenuIn": "_cloudsearch_386_MenuIn",
        "MenuOut": "_cloudsearch_387_MenuOut",
        "AppsDynamiteSharedSegmentedMembershipCountsIn": "_cloudsearch_388_AppsDynamiteSharedSegmentedMembershipCountsIn",
        "AppsDynamiteSharedSegmentedMembershipCountsOut": "_cloudsearch_389_AppsDynamiteSharedSegmentedMembershipCountsOut",
        "SuggestResultIn": "_cloudsearch_390_SuggestResultIn",
        "SuggestResultOut": "_cloudsearch_391_SuggestResultOut",
        "ObjectOptionsIn": "_cloudsearch_392_ObjectOptionsIn",
        "ObjectOptionsOut": "_cloudsearch_393_ObjectOptionsOut",
        "AppsDynamiteStorageColumnsColumnIn": "_cloudsearch_394_AppsDynamiteStorageColumnsColumnIn",
        "AppsDynamiteStorageColumnsColumnOut": "_cloudsearch_395_AppsDynamiteStorageColumnsColumnOut",
        "FolderIn": "_cloudsearch_396_FolderIn",
        "FolderOut": "_cloudsearch_397_FolderOut",
        "ThreadKeySetIn": "_cloudsearch_398_ThreadKeySetIn",
        "ThreadKeySetOut": "_cloudsearch_399_ThreadKeySetOut",
        "AppsDynamiteSharedSpaceInfoIn": "_cloudsearch_400_AppsDynamiteSharedSpaceInfoIn",
        "AppsDynamiteSharedSpaceInfoOut": "_cloudsearch_401_AppsDynamiteSharedSpaceInfoOut",
        "AppsDynamiteStorageMaterialIconIn": "_cloudsearch_402_AppsDynamiteStorageMaterialIconIn",
        "AppsDynamiteStorageMaterialIconOut": "_cloudsearch_403_AppsDynamiteStorageMaterialIconOut",
        "AppsDynamiteStorageImageComponentIn": "_cloudsearch_404_AppsDynamiteStorageImageComponentIn",
        "AppsDynamiteStorageImageComponentOut": "_cloudsearch_405_AppsDynamiteStorageImageComponentOut",
        "BotResponseIn": "_cloudsearch_406_BotResponseIn",
        "BotResponseOut": "_cloudsearch_407_BotResponseOut",
        "GatewayAccessIn": "_cloudsearch_408_GatewayAccessIn",
        "GatewayAccessOut": "_cloudsearch_409_GatewayAccessOut",
        "AppsDynamiteSharedReactionIn": "_cloudsearch_410_AppsDynamiteSharedReactionIn",
        "AppsDynamiteSharedReactionOut": "_cloudsearch_411_AppsDynamiteSharedReactionOut",
        "ImapSyncDeleteIn": "_cloudsearch_412_ImapSyncDeleteIn",
        "ImapSyncDeleteOut": "_cloudsearch_413_ImapSyncDeleteOut",
        "DlpScanSummaryIn": "_cloudsearch_414_DlpScanSummaryIn",
        "DlpScanSummaryOut": "_cloudsearch_415_DlpScanSummaryOut",
        "ItemStatusIn": "_cloudsearch_416_ItemStatusIn",
        "ItemStatusOut": "_cloudsearch_417_ItemStatusOut",
        "AppsDynamiteSharedDocumentIn": "_cloudsearch_418_AppsDynamiteSharedDocumentIn",
        "AppsDynamiteSharedDocumentOut": "_cloudsearch_419_AppsDynamiteSharedDocumentOut",
        "ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn": "_cloudsearch_420_ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut": "_cloudsearch_421_ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut",
        "SafeUrlProtoIn": "_cloudsearch_422_SafeUrlProtoIn",
        "SafeUrlProtoOut": "_cloudsearch_423_SafeUrlProtoOut",
        "MessageDeletedIn": "_cloudsearch_424_MessageDeletedIn",
        "MessageDeletedOut": "_cloudsearch_425_MessageDeletedOut",
        "TombstoneMetadataIn": "_cloudsearch_426_TombstoneMetadataIn",
        "TombstoneMetadataOut": "_cloudsearch_427_TombstoneMetadataOut",
        "DmIdIn": "_cloudsearch_428_DmIdIn",
        "DmIdOut": "_cloudsearch_429_DmIdOut",
        "ReferenceIn": "_cloudsearch_430_ReferenceIn",
        "ReferenceOut": "_cloudsearch_431_ReferenceOut",
        "CollaborationIn": "_cloudsearch_432_CollaborationIn",
        "CollaborationOut": "_cloudsearch_433_CollaborationOut",
        "DriveMetadataIn": "_cloudsearch_434_DriveMetadataIn",
        "DriveMetadataOut": "_cloudsearch_435_DriveMetadataOut",
        "DeepLinkDataIn": "_cloudsearch_436_DeepLinkDataIn",
        "DeepLinkDataOut": "_cloudsearch_437_DeepLinkDataOut",
        "StructuredDataObjectIn": "_cloudsearch_438_StructuredDataObjectIn",
        "StructuredDataObjectOut": "_cloudsearch_439_StructuredDataObjectOut",
        "AffectedMembershipIn": "_cloudsearch_440_AffectedMembershipIn",
        "AffectedMembershipOut": "_cloudsearch_441_AffectedMembershipOut",
        "ZwiebackSessionProtoIn": "_cloudsearch_442_ZwiebackSessionProtoIn",
        "ZwiebackSessionProtoOut": "_cloudsearch_443_ZwiebackSessionProtoOut",
        "AppsDynamiteStorageOpenLinkIn": "_cloudsearch_444_AppsDynamiteStorageOpenLinkIn",
        "AppsDynamiteStorageOpenLinkOut": "_cloudsearch_445_AppsDynamiteStorageOpenLinkOut",
        "GetSearchApplicationUserStatsResponseIn": "_cloudsearch_446_GetSearchApplicationUserStatsResponseIn",
        "GetSearchApplicationUserStatsResponseOut": "_cloudsearch_447_GetSearchApplicationUserStatsResponseOut",
        "ErrorMessageIn": "_cloudsearch_448_ErrorMessageIn",
        "ErrorMessageOut": "_cloudsearch_449_ErrorMessageOut",
        "ProvenanceIn": "_cloudsearch_450_ProvenanceIn",
        "ProvenanceOut": "_cloudsearch_451_ProvenanceOut",
        "EditorClientActionMarkupIn": "_cloudsearch_452_EditorClientActionMarkupIn",
        "EditorClientActionMarkupOut": "_cloudsearch_453_EditorClientActionMarkupOut",
        "UnreserveItemsRequestIn": "_cloudsearch_454_UnreserveItemsRequestIn",
        "UnreserveItemsRequestOut": "_cloudsearch_455_UnreserveItemsRequestOut",
        "TransactionDebugInfoIn": "_cloudsearch_456_TransactionDebugInfoIn",
        "TransactionDebugInfoOut": "_cloudsearch_457_TransactionDebugInfoOut",
        "HostAppActionMarkupIn": "_cloudsearch_458_HostAppActionMarkupIn",
        "HostAppActionMarkupOut": "_cloudsearch_459_HostAppActionMarkupOut",
        "HistoryIn": "_cloudsearch_460_HistoryIn",
        "HistoryOut": "_cloudsearch_461_HistoryOut",
        "MessageParentIdIn": "_cloudsearch_462_MessageParentIdIn",
        "MessageParentIdOut": "_cloudsearch_463_MessageParentIdOut",
        "MemberIn": "_cloudsearch_464_MemberIn",
        "MemberOut": "_cloudsearch_465_MemberOut",
        "AppsDynamiteStorageBorderStyleIn": "_cloudsearch_466_AppsDynamiteStorageBorderStyleIn",
        "AppsDynamiteStorageBorderStyleOut": "_cloudsearch_467_AppsDynamiteStorageBorderStyleOut",
        "AclFixRequestIn": "_cloudsearch_468_AclFixRequestIn",
        "AclFixRequestOut": "_cloudsearch_469_AclFixRequestOut",
        "InviteAcceptedEventIn": "_cloudsearch_470_InviteAcceptedEventIn",
        "InviteAcceptedEventOut": "_cloudsearch_471_InviteAcceptedEventOut",
        "FormActionIn": "_cloudsearch_472_FormActionIn",
        "FormActionOut": "_cloudsearch_473_FormActionOut",
        "AutoCompleteIn": "_cloudsearch_474_AutoCompleteIn",
        "AutoCompleteOut": "_cloudsearch_475_AutoCompleteOut",
        "GoogleChatV1ContextualAddOnMarkupCardSectionIn": "_cloudsearch_476_GoogleChatV1ContextualAddOnMarkupCardSectionIn",
        "GoogleChatV1ContextualAddOnMarkupCardSectionOut": "_cloudsearch_477_GoogleChatV1ContextualAddOnMarkupCardSectionOut",
        "MessageSetIn": "_cloudsearch_478_MessageSetIn",
        "MessageSetOut": "_cloudsearch_479_MessageSetOut",
        "AppsDynamiteSharedFindDocumentSuggestionIn": "_cloudsearch_480_AppsDynamiteSharedFindDocumentSuggestionIn",
        "AppsDynamiteSharedFindDocumentSuggestionOut": "_cloudsearch_481_AppsDynamiteSharedFindDocumentSuggestionOut",
        "EmbedClientItemIn": "_cloudsearch_482_EmbedClientItemIn",
        "EmbedClientItemOut": "_cloudsearch_483_EmbedClientItemOut",
        "SuggestRequestIn": "_cloudsearch_484_SuggestRequestIn",
        "SuggestRequestOut": "_cloudsearch_485_SuggestRequestOut",
        "FuseboxItemIn": "_cloudsearch_486_FuseboxItemIn",
        "FuseboxItemOut": "_cloudsearch_487_FuseboxItemOut",
        "MembershipChangedMetadataIn": "_cloudsearch_488_MembershipChangedMetadataIn",
        "MembershipChangedMetadataOut": "_cloudsearch_489_MembershipChangedMetadataOut",
        "RoomUpdatedMetadataIn": "_cloudsearch_490_RoomUpdatedMetadataIn",
        "RoomUpdatedMetadataOut": "_cloudsearch_491_RoomUpdatedMetadataOut",
        "LabelAddedIn": "_cloudsearch_492_LabelAddedIn",
        "LabelAddedOut": "_cloudsearch_493_LabelAddedOut",
        "InteractionIn": "_cloudsearch_494_InteractionIn",
        "InteractionOut": "_cloudsearch_495_InteractionOut",
        "WrappedResourceKeyIn": "_cloudsearch_496_WrappedResourceKeyIn",
        "WrappedResourceKeyOut": "_cloudsearch_497_WrappedResourceKeyOut",
        "BabelPlaceholderMetadataIn": "_cloudsearch_498_BabelPlaceholderMetadataIn",
        "BabelPlaceholderMetadataOut": "_cloudsearch_499_BabelPlaceholderMetadataOut",
        "MembershipChangeEventIn": "_cloudsearch_500_MembershipChangeEventIn",
        "MembershipChangeEventOut": "_cloudsearch_501_MembershipChangeEventOut",
        "RpcOptionsIn": "_cloudsearch_502_RpcOptionsIn",
        "RpcOptionsOut": "_cloudsearch_503_RpcOptionsOut",
        "ListUnmappedIdentitiesResponseIn": "_cloudsearch_504_ListUnmappedIdentitiesResponseIn",
        "ListUnmappedIdentitiesResponseOut": "_cloudsearch_505_ListUnmappedIdentitiesResponseOut",
        "AuthorizedItemIdIn": "_cloudsearch_506_AuthorizedItemIdIn",
        "AuthorizedItemIdOut": "_cloudsearch_507_AuthorizedItemIdOut",
        "TimestampPropertyOptionsIn": "_cloudsearch_508_TimestampPropertyOptionsIn",
        "TimestampPropertyOptionsOut": "_cloudsearch_509_TimestampPropertyOptionsOut",
        "AllAuthenticatedUsersProtoIn": "_cloudsearch_510_AllAuthenticatedUsersProtoIn",
        "AllAuthenticatedUsersProtoOut": "_cloudsearch_511_AllAuthenticatedUsersProtoOut",
        "DisplayedPropertyIn": "_cloudsearch_512_DisplayedPropertyIn",
        "DisplayedPropertyOut": "_cloudsearch_513_DisplayedPropertyOut",
        "ConsentedAppUnfurlMetadataIn": "_cloudsearch_514_ConsentedAppUnfurlMetadataIn",
        "ConsentedAppUnfurlMetadataOut": "_cloudsearch_515_ConsentedAppUnfurlMetadataOut",
        "PreStateIn": "_cloudsearch_516_PreStateIn",
        "PreStateOut": "_cloudsearch_517_PreStateOut",
        "PersonalLabelTagIn": "_cloudsearch_518_PersonalLabelTagIn",
        "PersonalLabelTagOut": "_cloudsearch_519_PersonalLabelTagOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn": "_cloudsearch_520_AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut": "_cloudsearch_521_AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut",
        "AppsDynamiteSharedTasksMessageIntegrationPayloadIn": "_cloudsearch_522_AppsDynamiteSharedTasksMessageIntegrationPayloadIn",
        "AppsDynamiteSharedTasksMessageIntegrationPayloadOut": "_cloudsearch_523_AppsDynamiteSharedTasksMessageIntegrationPayloadOut",
        "RetrievalImportanceIn": "_cloudsearch_524_RetrievalImportanceIn",
        "RetrievalImportanceOut": "_cloudsearch_525_RetrievalImportanceOut",
        "AppsDynamiteStorageTextParagraphIn": "_cloudsearch_526_AppsDynamiteStorageTextParagraphIn",
        "AppsDynamiteStorageTextParagraphOut": "_cloudsearch_527_AppsDynamiteStorageTextParagraphOut",
        "AppsDynamiteSharedAssistantAnnotationDataIn": "_cloudsearch_528_AppsDynamiteSharedAssistantAnnotationDataIn",
        "AppsDynamiteSharedAssistantAnnotationDataOut": "_cloudsearch_529_AppsDynamiteSharedAssistantAnnotationDataOut",
        "TransactionContextIn": "_cloudsearch_530_TransactionContextIn",
        "TransactionContextOut": "_cloudsearch_531_TransactionContextOut",
        "DoubleOperatorOptionsIn": "_cloudsearch_532_DoubleOperatorOptionsIn",
        "DoubleOperatorOptionsOut": "_cloudsearch_533_DoubleOperatorOptionsOut",
        "QueryInterpretationIn": "_cloudsearch_534_QueryInterpretationIn",
        "QueryInterpretationOut": "_cloudsearch_535_QueryInterpretationOut",
        "AppsDynamiteV1ApiCompatV1AttachmentIn": "_cloudsearch_536_AppsDynamiteV1ApiCompatV1AttachmentIn",
        "AppsDynamiteV1ApiCompatV1AttachmentOut": "_cloudsearch_537_AppsDynamiteV1ApiCompatV1AttachmentOut",
        "MultiKeyIn": "_cloudsearch_538_MultiKeyIn",
        "MultiKeyOut": "_cloudsearch_539_MultiKeyOut",
        "SourceConfigIn": "_cloudsearch_540_SourceConfigIn",
        "SourceConfigOut": "_cloudsearch_541_SourceConfigOut",
        "UpdateCcRecipientsIn": "_cloudsearch_542_UpdateCcRecipientsIn",
        "UpdateCcRecipientsOut": "_cloudsearch_543_UpdateCcRecipientsOut",
        "AppsDynamiteSharedTasksAnnotationDataCreationIn": "_cloudsearch_544_AppsDynamiteSharedTasksAnnotationDataCreationIn",
        "AppsDynamiteSharedTasksAnnotationDataCreationOut": "_cloudsearch_545_AppsDynamiteSharedTasksAnnotationDataCreationOut",
        "ColorIn": "_cloudsearch_546_ColorIn",
        "ColorOut": "_cloudsearch_547_ColorOut",
        "TriggerKeyIn": "_cloudsearch_548_TriggerKeyIn",
        "TriggerKeyOut": "_cloudsearch_549_TriggerKeyOut",
        "CircleProtoIn": "_cloudsearch_550_CircleProtoIn",
        "CircleProtoOut": "_cloudsearch_551_CircleProtoOut",
        "CapTokenHolderProtoIn": "_cloudsearch_552_CapTokenHolderProtoIn",
        "CapTokenHolderProtoOut": "_cloudsearch_553_CapTokenHolderProtoOut",
        "PhotoIn": "_cloudsearch_554_PhotoIn",
        "PhotoOut": "_cloudsearch_555_PhotoOut",
        "SpaceIdIn": "_cloudsearch_556_SpaceIdIn",
        "SpaceIdOut": "_cloudsearch_557_SpaceIdOut",
        "ImageKeyValueIn": "_cloudsearch_558_ImageKeyValueIn",
        "ImageKeyValueOut": "_cloudsearch_559_ImageKeyValueOut",
        "NameIn": "_cloudsearch_560_NameIn",
        "NameOut": "_cloudsearch_561_NameOut",
        "DriveFollowUpRestrictIn": "_cloudsearch_562_DriveFollowUpRestrictIn",
        "DriveFollowUpRestrictOut": "_cloudsearch_563_DriveFollowUpRestrictOut",
        "ChatConserverMessageContentIn": "_cloudsearch_564_ChatConserverMessageContentIn",
        "ChatConserverMessageContentOut": "_cloudsearch_565_ChatConserverMessageContentOut",
        "AppsDynamiteStorageDecoratedTextIn": "_cloudsearch_566_AppsDynamiteStorageDecoratedTextIn",
        "AppsDynamiteStorageDecoratedTextOut": "_cloudsearch_567_AppsDynamiteStorageDecoratedTextOut",
        "EditMetadataIn": "_cloudsearch_568_EditMetadataIn",
        "EditMetadataOut": "_cloudsearch_569_EditMetadataOut",
        "DateIn": "_cloudsearch_570_DateIn",
        "DateOut": "_cloudsearch_571_DateOut",
        "ValueIn": "_cloudsearch_572_ValueIn",
        "ValueOut": "_cloudsearch_573_ValueOut",
        "SourceScoringConfigIn": "_cloudsearch_574_SourceScoringConfigIn",
        "SourceScoringConfigOut": "_cloudsearch_575_SourceScoringConfigOut",
        "VideoInfoIn": "_cloudsearch_576_VideoInfoIn",
        "VideoInfoOut": "_cloudsearch_577_VideoInfoOut",
        "GetCustomerIndexStatsResponseIn": "_cloudsearch_578_GetCustomerIndexStatsResponseIn",
        "GetCustomerIndexStatsResponseOut": "_cloudsearch_579_GetCustomerIndexStatsResponseOut",
        "MessageIdIn": "_cloudsearch_580_MessageIdIn",
        "MessageIdOut": "_cloudsearch_581_MessageIdOut",
        "AppsDynamiteSharedAssistantUnfulfillableRequestIn": "_cloudsearch_582_AppsDynamiteSharedAssistantUnfulfillableRequestIn",
        "AppsDynamiteSharedAssistantUnfulfillableRequestOut": "_cloudsearch_583_AppsDynamiteSharedAssistantUnfulfillableRequestOut",
        "GetCustomerUserStatsResponseIn": "_cloudsearch_584_GetCustomerUserStatsResponseIn",
        "GetCustomerUserStatsResponseOut": "_cloudsearch_585_GetCustomerUserStatsResponseOut",
        "AppsDynamiteSharedOrganizationInfoCustomerInfoIn": "_cloudsearch_586_AppsDynamiteSharedOrganizationInfoCustomerInfoIn",
        "AppsDynamiteSharedOrganizationInfoCustomerInfoOut": "_cloudsearch_587_AppsDynamiteSharedOrganizationInfoCustomerInfoOut",
        "BroadcastStatsIn": "_cloudsearch_588_BroadcastStatsIn",
        "BroadcastStatsOut": "_cloudsearch_589_BroadcastStatsOut",
        "FixedFooterIn": "_cloudsearch_590_FixedFooterIn",
        "FixedFooterOut": "_cloudsearch_591_FixedFooterOut",
        "SimpleSecretLabelProtoIn": "_cloudsearch_592_SimpleSecretLabelProtoIn",
        "SimpleSecretLabelProtoOut": "_cloudsearch_593_SimpleSecretLabelProtoOut",
        "VoicePhoneNumberIn": "_cloudsearch_594_VoicePhoneNumberIn",
        "VoicePhoneNumberOut": "_cloudsearch_595_VoicePhoneNumberOut",
        "ListQuerySourcesResponseIn": "_cloudsearch_596_ListQuerySourcesResponseIn",
        "ListQuerySourcesResponseOut": "_cloudsearch_597_ListQuerySourcesResponseOut",
        "LinkDataIn": "_cloudsearch_598_LinkDataIn",
        "LinkDataOut": "_cloudsearch_599_LinkDataOut",
        "BorderStyleIn": "_cloudsearch_600_BorderStyleIn",
        "BorderStyleOut": "_cloudsearch_601_BorderStyleOut",
        "YoutubeUserProtoIn": "_cloudsearch_602_YoutubeUserProtoIn",
        "YoutubeUserProtoOut": "_cloudsearch_603_YoutubeUserProtoOut",
        "CustomerIdIn": "_cloudsearch_604_CustomerIdIn",
        "CustomerIdOut": "_cloudsearch_605_CustomerIdOut",
        "MessageIn": "_cloudsearch_606_MessageIn",
        "MessageOut": "_cloudsearch_607_MessageOut",
        "GetCustomerSearchApplicationStatsResponseIn": "_cloudsearch_608_GetCustomerSearchApplicationStatsResponseIn",
        "GetCustomerSearchApplicationStatsResponseOut": "_cloudsearch_609_GetCustomerSearchApplicationStatsResponseOut",
        "TextPropertyOptionsIn": "_cloudsearch_610_TextPropertyOptionsIn",
        "TextPropertyOptionsOut": "_cloudsearch_611_TextPropertyOptionsOut",
        "AclInfoIn": "_cloudsearch_612_AclInfoIn",
        "AclInfoOut": "_cloudsearch_613_AclInfoOut",
        "ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn": "_cloudsearch_614_ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut": "_cloudsearch_615_ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut",
        "JobsettedServerSpecIn": "_cloudsearch_616_JobsettedServerSpecIn",
        "JobsettedServerSpecOut": "_cloudsearch_617_JobsettedServerSpecOut",
        "PropertyDefinitionIn": "_cloudsearch_618_PropertyDefinitionIn",
        "PropertyDefinitionOut": "_cloudsearch_619_PropertyDefinitionOut",
        "AppsDynamiteSharedVideoReferenceIn": "_cloudsearch_620_AppsDynamiteSharedVideoReferenceIn",
        "AppsDynamiteSharedVideoReferenceOut": "_cloudsearch_621_AppsDynamiteSharedVideoReferenceOut",
        "GmailClientActionMarkupIn": "_cloudsearch_622_GmailClientActionMarkupIn",
        "GmailClientActionMarkupOut": "_cloudsearch_623_GmailClientActionMarkupOut",
        "AppsDynamiteStorageDividerIn": "_cloudsearch_624_AppsDynamiteStorageDividerIn",
        "AppsDynamiteStorageDividerOut": "_cloudsearch_625_AppsDynamiteStorageDividerOut",
        "SigningKeyPossessorProtoIn": "_cloudsearch_626_SigningKeyPossessorProtoIn",
        "SigningKeyPossessorProtoOut": "_cloudsearch_627_SigningKeyPossessorProtoOut",
        "HostProtoIn": "_cloudsearch_628_HostProtoIn",
        "HostProtoOut": "_cloudsearch_629_HostProtoOut",
        "AppsDynamiteStorageButtonIn": "_cloudsearch_630_AppsDynamiteStorageButtonIn",
        "AppsDynamiteStorageButtonOut": "_cloudsearch_631_AppsDynamiteStorageButtonOut",
        "FilterUpdateIn": "_cloudsearch_632_FilterUpdateIn",
        "FilterUpdateOut": "_cloudsearch_633_FilterUpdateOut",
        "UploadItemRefIn": "_cloudsearch_634_UploadItemRefIn",
        "UploadItemRefOut": "_cloudsearch_635_UploadItemRefOut",
        "ResultDisplayLineIn": "_cloudsearch_636_ResultDisplayLineIn",
        "ResultDisplayLineOut": "_cloudsearch_637_ResultDisplayLineOut",
        "DataSourceIndexStatsIn": "_cloudsearch_638_DataSourceIndexStatsIn",
        "DataSourceIndexStatsOut": "_cloudsearch_639_DataSourceIndexStatsOut",
        "SwitchWidgetIn": "_cloudsearch_640_SwitchWidgetIn",
        "SwitchWidgetOut": "_cloudsearch_641_SwitchWidgetOut",
        "ContentReportIn": "_cloudsearch_642_ContentReportIn",
        "ContentReportOut": "_cloudsearch_643_ContentReportOut",
        "QueryInterpretationConfigIn": "_cloudsearch_644_QueryInterpretationConfigIn",
        "QueryInterpretationConfigOut": "_cloudsearch_645_QueryInterpretationConfigOut",
        "FilterOptionsIn": "_cloudsearch_646_FilterOptionsIn",
        "FilterOptionsOut": "_cloudsearch_647_FilterOptionsOut",
        "ResultDebugInfoIn": "_cloudsearch_648_ResultDebugInfoIn",
        "ResultDebugInfoOut": "_cloudsearch_649_ResultDebugInfoOut",
        "DeliveryMediumIn": "_cloudsearch_650_DeliveryMediumIn",
        "DeliveryMediumOut": "_cloudsearch_651_DeliveryMediumOut",
        "ResultDisplayFieldIn": "_cloudsearch_652_ResultDisplayFieldIn",
        "ResultDisplayFieldOut": "_cloudsearch_653_ResultDisplayFieldOut",
        "LabelRemovedIn": "_cloudsearch_654_LabelRemovedIn",
        "LabelRemovedOut": "_cloudsearch_655_LabelRemovedOut",
        "GatewaySipAccessIn": "_cloudsearch_656_GatewaySipAccessIn",
        "GatewaySipAccessOut": "_cloudsearch_657_GatewaySipAccessOut",
        "ErrorInfoIn": "_cloudsearch_658_ErrorInfoIn",
        "ErrorInfoOut": "_cloudsearch_659_ErrorInfoOut",
        "SessionEventIn": "_cloudsearch_660_SessionEventIn",
        "SessionEventOut": "_cloudsearch_661_SessionEventOut",
        "IntegerPropertyOptionsIn": "_cloudsearch_662_IntegerPropertyOptionsIn",
        "IntegerPropertyOptionsOut": "_cloudsearch_663_IntegerPropertyOptionsOut",
        "AppsDynamiteSharedChatItemActivityInfoIn": "_cloudsearch_664_AppsDynamiteSharedChatItemActivityInfoIn",
        "AppsDynamiteSharedChatItemActivityInfoOut": "_cloudsearch_665_AppsDynamiteSharedChatItemActivityInfoOut",
        "PollItemsResponseIn": "_cloudsearch_666_PollItemsResponseIn",
        "PollItemsResponseOut": "_cloudsearch_667_PollItemsResponseOut",
        "CoActivityIn": "_cloudsearch_668_CoActivityIn",
        "CoActivityOut": "_cloudsearch_669_CoActivityOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn": "_cloudsearch_670_AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut": "_cloudsearch_671_AppsExtensionsMarkupCalendarClientActionMarkupEditConferenceDataActionMarkupOut",
        "SourceIn": "_cloudsearch_672_SourceIn",
        "SourceOut": "_cloudsearch_673_SourceOut",
        "AppsDynamiteSharedMessageComponentSearchInfoIn": "_cloudsearch_674_AppsDynamiteSharedMessageComponentSearchInfoIn",
        "AppsDynamiteSharedMessageComponentSearchInfoOut": "_cloudsearch_675_AppsDynamiteSharedMessageComponentSearchInfoOut",
        "PinnedItemIdIn": "_cloudsearch_676_PinnedItemIdIn",
        "PinnedItemIdOut": "_cloudsearch_677_PinnedItemIdOut",
        "UserMentionDataIn": "_cloudsearch_678_UserMentionDataIn",
        "UserMentionDataOut": "_cloudsearch_679_UserMentionDataOut",
        "AppsDynamiteSharedOrganizationInfoConsumerInfoIn": "_cloudsearch_680_AppsDynamiteSharedOrganizationInfoConsumerInfoIn",
        "AppsDynamiteSharedOrganizationInfoConsumerInfoOut": "_cloudsearch_681_AppsDynamiteSharedOrganizationInfoConsumerInfoOut",
        "GroupIdIn": "_cloudsearch_682_GroupIdIn",
        "GroupIdOut": "_cloudsearch_683_GroupIdOut",
        "AppsDynamiteSharedUserBlockRelationshipIn": "_cloudsearch_684_AppsDynamiteSharedUserBlockRelationshipIn",
        "AppsDynamiteSharedUserBlockRelationshipOut": "_cloudsearch_685_AppsDynamiteSharedUserBlockRelationshipOut",
        "AppsDynamiteStorageActionIn": "_cloudsearch_686_AppsDynamiteStorageActionIn",
        "AppsDynamiteStorageActionOut": "_cloudsearch_687_AppsDynamiteStorageActionOut",
        "GoogleChatV1WidgetMarkupTextButtonIn": "_cloudsearch_688_GoogleChatV1WidgetMarkupTextButtonIn",
        "GoogleChatV1WidgetMarkupTextButtonOut": "_cloudsearch_689_GoogleChatV1WidgetMarkupTextButtonOut",
        "ItemMetadataIn": "_cloudsearch_690_ItemMetadataIn",
        "ItemMetadataOut": "_cloudsearch_691_ItemMetadataOut",
        "TopicIdIn": "_cloudsearch_692_TopicIdIn",
        "TopicIdOut": "_cloudsearch_693_TopicIdOut",
        "ImageButtonIn": "_cloudsearch_694_ImageButtonIn",
        "ImageButtonOut": "_cloudsearch_695_ImageButtonOut",
        "SimpleSecretHolderProtoIn": "_cloudsearch_696_SimpleSecretHolderProtoIn",
        "SimpleSecretHolderProtoOut": "_cloudsearch_697_SimpleSecretHolderProtoOut",
        "AppsDynamiteSharedAssistantFeedbackContextIn": "_cloudsearch_698_AppsDynamiteSharedAssistantFeedbackContextIn",
        "AppsDynamiteSharedAssistantFeedbackContextOut": "_cloudsearch_699_AppsDynamiteSharedAssistantFeedbackContextOut",
        "DataSourceIn": "_cloudsearch_700_DataSourceIn",
        "DataSourceOut": "_cloudsearch_701_DataSourceOut",
        "GridIn": "_cloudsearch_702_GridIn",
        "GridOut": "_cloudsearch_703_GridOut",
        "MdbGroupProtoIn": "_cloudsearch_704_MdbGroupProtoIn",
        "MdbGroupProtoOut": "_cloudsearch_705_MdbGroupProtoOut",
        "YouTubeBroadcastSessionInfoIn": "_cloudsearch_706_YouTubeBroadcastSessionInfoIn",
        "YouTubeBroadcastSessionInfoOut": "_cloudsearch_707_YouTubeBroadcastSessionInfoOut",
        "GoogleChatV1WidgetMarkupOnClickIn": "_cloudsearch_708_GoogleChatV1WidgetMarkupOnClickIn",
        "GoogleChatV1WidgetMarkupOnClickOut": "_cloudsearch_709_GoogleChatV1WidgetMarkupOnClickOut",
        "EnumValuesIn": "_cloudsearch_710_EnumValuesIn",
        "EnumValuesOut": "_cloudsearch_711_EnumValuesOut",
        "ResetSearchApplicationRequestIn": "_cloudsearch_712_ResetSearchApplicationRequestIn",
        "ResetSearchApplicationRequestOut": "_cloudsearch_713_ResetSearchApplicationRequestOut",
        "MessagePropsIn": "_cloudsearch_714_MessagePropsIn",
        "MessagePropsOut": "_cloudsearch_715_MessagePropsOut",
        "LabelUpdateIn": "_cloudsearch_716_LabelUpdateIn",
        "LabelUpdateOut": "_cloudsearch_717_LabelUpdateOut",
        "DoublePropertyOptionsIn": "_cloudsearch_718_DoublePropertyOptionsIn",
        "DoublePropertyOptionsOut": "_cloudsearch_719_DoublePropertyOptionsOut",
        "MatchRangeIn": "_cloudsearch_720_MatchRangeIn",
        "MatchRangeOut": "_cloudsearch_721_MatchRangeOut",
        "QueryCountByStatusIn": "_cloudsearch_722_QueryCountByStatusIn",
        "QueryCountByStatusOut": "_cloudsearch_723_QueryCountByStatusOut",
        "PropertyDisplayOptionsIn": "_cloudsearch_724_PropertyDisplayOptionsIn",
        "PropertyDisplayOptionsOut": "_cloudsearch_725_PropertyDisplayOptionsOut",
        "PollItemsRequestIn": "_cloudsearch_726_PollItemsRequestIn",
        "PollItemsRequestOut": "_cloudsearch_727_PollItemsRequestOut",
        "EventProtoIn": "_cloudsearch_728_EventProtoIn",
        "EventProtoOut": "_cloudsearch_729_EventProtoOut",
        "BroadcastAccessIn": "_cloudsearch_730_BroadcastAccessIn",
        "BroadcastAccessOut": "_cloudsearch_731_BroadcastAccessOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn": "_cloudsearch_732_AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut": "_cloudsearch_733_AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut",
        "PaygateInfoIn": "_cloudsearch_734_PaygateInfoIn",
        "PaygateInfoOut": "_cloudsearch_735_PaygateInfoOut",
        "MetadataIn": "_cloudsearch_736_MetadataIn",
        "MetadataOut": "_cloudsearch_737_MetadataOut",
        "RenameEventIn": "_cloudsearch_738_RenameEventIn",
        "RenameEventOut": "_cloudsearch_739_RenameEventOut",
        "AbuseReportingConfigIn": "_cloudsearch_740_AbuseReportingConfigIn",
        "AbuseReportingConfigOut": "_cloudsearch_741_AbuseReportingConfigOut",
        "ContextualAddOnMarkupIn": "_cloudsearch_742_ContextualAddOnMarkupIn",
        "ContextualAddOnMarkupOut": "_cloudsearch_743_ContextualAddOnMarkupOut",
        "HashtagDataIn": "_cloudsearch_744_HashtagDataIn",
        "HashtagDataOut": "_cloudsearch_745_HashtagDataOut",
        "AppsDynamiteStorageSelectionInputSelectionItemIn": "_cloudsearch_746_AppsDynamiteStorageSelectionInputSelectionItemIn",
        "AppsDynamiteStorageSelectionInputSelectionItemOut": "_cloudsearch_747_AppsDynamiteStorageSelectionInputSelectionItemOut",
        "SearchResultIn": "_cloudsearch_748_SearchResultIn",
        "SearchResultOut": "_cloudsearch_749_SearchResultOut",
        "IntegerFacetingOptionsIn": "_cloudsearch_750_IntegerFacetingOptionsIn",
        "IntegerFacetingOptionsOut": "_cloudsearch_751_IntegerFacetingOptionsOut",
        "AppsDynamiteSharedChatItemGroupInfoIn": "_cloudsearch_752_AppsDynamiteSharedChatItemGroupInfoIn",
        "AppsDynamiteSharedChatItemGroupInfoOut": "_cloudsearch_753_AppsDynamiteSharedChatItemGroupInfoOut",
        "AppsDynamiteSharedAvatarInfoIn": "_cloudsearch_754_AppsDynamiteSharedAvatarInfoIn",
        "AppsDynamiteSharedAvatarInfoOut": "_cloudsearch_755_AppsDynamiteSharedAvatarInfoOut",
        "AppsDynamiteSharedEmojiIn": "_cloudsearch_756_AppsDynamiteSharedEmojiIn",
        "AppsDynamiteSharedEmojiOut": "_cloudsearch_757_AppsDynamiteSharedEmojiOut",
        "PersonIn": "_cloudsearch_758_PersonIn",
        "PersonOut": "_cloudsearch_759_PersonOut",
        "TextOperatorOptionsIn": "_cloudsearch_760_TextOperatorOptionsIn",
        "TextOperatorOptionsOut": "_cloudsearch_761_TextOperatorOptionsOut",
        "RoomRenameMetadataIn": "_cloudsearch_762_RoomRenameMetadataIn",
        "RoomRenameMetadataOut": "_cloudsearch_763_RoomRenameMetadataOut",
        "GroupLinkSharingModificationEventIn": "_cloudsearch_764_GroupLinkSharingModificationEventIn",
        "GroupLinkSharingModificationEventOut": "_cloudsearch_765_GroupLinkSharingModificationEventOut",
        "ResultDisplayMetadataIn": "_cloudsearch_766_ResultDisplayMetadataIn",
        "ResultDisplayMetadataOut": "_cloudsearch_767_ResultDisplayMetadataOut",
        "AppsDynamiteSharedTasksAnnotationDataIn": "_cloudsearch_768_AppsDynamiteSharedTasksAnnotationDataIn",
        "AppsDynamiteSharedTasksAnnotationDataOut": "_cloudsearch_769_AppsDynamiteSharedTasksAnnotationDataOut",
        "SuggestResponseIn": "_cloudsearch_770_SuggestResponseIn",
        "SuggestResponseOut": "_cloudsearch_771_SuggestResponseOut",
        "AddonComposeUiActionMarkupIn": "_cloudsearch_772_AddonComposeUiActionMarkupIn",
        "AddonComposeUiActionMarkupOut": "_cloudsearch_773_AddonComposeUiActionMarkupOut",
        "ResultCountsIn": "_cloudsearch_774_ResultCountsIn",
        "ResultCountsOut": "_cloudsearch_775_ResultCountsOut",
        "EventAnnotationIn": "_cloudsearch_776_EventAnnotationIn",
        "EventAnnotationOut": "_cloudsearch_777_EventAnnotationOut",
        "AppsDynamiteSharedAssistantSuggestionIn": "_cloudsearch_778_AppsDynamiteSharedAssistantSuggestionIn",
        "AppsDynamiteSharedAssistantSuggestionOut": "_cloudsearch_779_AppsDynamiteSharedAssistantSuggestionOut",
        "AppsDynamiteSharedMeetMetadataIn": "_cloudsearch_780_AppsDynamiteSharedMeetMetadataIn",
        "AppsDynamiteSharedMeetMetadataOut": "_cloudsearch_781_AppsDynamiteSharedMeetMetadataOut",
        "BotInfoIn": "_cloudsearch_782_BotInfoIn",
        "BotInfoOut": "_cloudsearch_783_BotInfoOut",
        "OnClickIn": "_cloudsearch_784_OnClickIn",
        "OnClickOut": "_cloudsearch_785_OnClickOut",
        "SpellResultIn": "_cloudsearch_786_SpellResultIn",
        "SpellResultOut": "_cloudsearch_787_SpellResultOut",
        "AppsDynamiteStorageCardCardActionIn": "_cloudsearch_788_AppsDynamiteStorageCardCardActionIn",
        "AppsDynamiteStorageCardCardActionOut": "_cloudsearch_789_AppsDynamiteStorageCardCardActionOut",
        "AppsDynamiteSharedRetentionSettingsIn": "_cloudsearch_790_AppsDynamiteSharedRetentionSettingsIn",
        "AppsDynamiteSharedRetentionSettingsOut": "_cloudsearch_791_AppsDynamiteSharedRetentionSettingsOut",
        "SearchApplicationSessionStatsIn": "_cloudsearch_792_SearchApplicationSessionStatsIn",
        "SearchApplicationSessionStatsOut": "_cloudsearch_793_SearchApplicationSessionStatsOut",
        "GroupRetentionSettingsUpdatedMetaDataIn": "_cloudsearch_794_GroupRetentionSettingsUpdatedMetaDataIn",
        "GroupRetentionSettingsUpdatedMetaDataOut": "_cloudsearch_795_GroupRetentionSettingsUpdatedMetaDataOut",
        "LdapGroupProtoIn": "_cloudsearch_796_LdapGroupProtoIn",
        "LdapGroupProtoOut": "_cloudsearch_797_LdapGroupProtoOut",
        "AppsDynamiteSharedPhoneNumberIn": "_cloudsearch_798_AppsDynamiteSharedPhoneNumberIn",
        "AppsDynamiteSharedPhoneNumberOut": "_cloudsearch_799_AppsDynamiteSharedPhoneNumberOut",
        "ResourceRoleProtoIn": "_cloudsearch_800_ResourceRoleProtoIn",
        "ResourceRoleProtoOut": "_cloudsearch_801_ResourceRoleProtoOut",
        "HistoryRecordIn": "_cloudsearch_802_HistoryRecordIn",
        "HistoryRecordOut": "_cloudsearch_803_HistoryRecordOut",
        "DlpActionIn": "_cloudsearch_804_DlpActionIn",
        "DlpActionOut": "_cloudsearch_805_DlpActionOut",
        "TextButtonIn": "_cloudsearch_806_TextButtonIn",
        "TextButtonOut": "_cloudsearch_807_TextButtonOut",
        "CheckAccessResponseIn": "_cloudsearch_808_CheckAccessResponseIn",
        "CheckAccessResponseOut": "_cloudsearch_809_CheckAccessResponseOut",
        "FuseboxItemThreadMatchInfoIn": "_cloudsearch_810_FuseboxItemThreadMatchInfoIn",
        "FuseboxItemThreadMatchInfoOut": "_cloudsearch_811_FuseboxItemThreadMatchInfoOut",
        "BabelMessagePropsIn": "_cloudsearch_812_BabelMessagePropsIn",
        "BabelMessagePropsOut": "_cloudsearch_813_BabelMessagePropsOut",
        "OpenLinkIn": "_cloudsearch_814_OpenLinkIn",
        "OpenLinkOut": "_cloudsearch_815_OpenLinkOut",
        "InteractionDataIn": "_cloudsearch_816_InteractionDataIn",
        "InteractionDataOut": "_cloudsearch_817_InteractionDataOut",
        "GSuitePrincipalIn": "_cloudsearch_818_GSuitePrincipalIn",
        "GSuitePrincipalOut": "_cloudsearch_819_GSuitePrincipalOut",
        "LegacyUploadMetadataIn": "_cloudsearch_820_LegacyUploadMetadataIn",
        "LegacyUploadMetadataOut": "_cloudsearch_821_LegacyUploadMetadataOut",
        "AppsDynamiteStorageCardIn": "_cloudsearch_822_AppsDynamiteStorageCardIn",
        "AppsDynamiteStorageCardOut": "_cloudsearch_823_AppsDynamiteStorageCardOut",
        "PrefWrittenIn": "_cloudsearch_824_PrefWrittenIn",
        "PrefWrittenOut": "_cloudsearch_825_PrefWrittenOut",
        "AppsDynamiteSharedBackendUploadMetadataIn": "_cloudsearch_826_AppsDynamiteSharedBackendUploadMetadataIn",
        "AppsDynamiteSharedBackendUploadMetadataOut": "_cloudsearch_827_AppsDynamiteSharedBackendUploadMetadataOut",
        "PrincipalIn": "_cloudsearch_828_PrincipalIn",
        "PrincipalOut": "_cloudsearch_829_PrincipalOut",
        "HangoutEventIn": "_cloudsearch_830_HangoutEventIn",
        "HangoutEventOut": "_cloudsearch_831_HangoutEventOut",
        "GsuiteIntegrationMetadataIn": "_cloudsearch_832_GsuiteIntegrationMetadataIn",
        "GsuiteIntegrationMetadataOut": "_cloudsearch_833_GsuiteIntegrationMetadataOut",
        "DriveLocationRestrictIn": "_cloudsearch_834_DriveLocationRestrictIn",
        "DriveLocationRestrictOut": "_cloudsearch_835_DriveLocationRestrictOut",
        "InsertContentIn": "_cloudsearch_836_InsertContentIn",
        "InsertContentOut": "_cloudsearch_837_InsertContentOut",
        "AuditLoggingSettingsIn": "_cloudsearch_838_AuditLoggingSettingsIn",
        "AuditLoggingSettingsOut": "_cloudsearch_839_AuditLoggingSettingsOut",
        "UpdateDraftActionMarkupIn": "_cloudsearch_840_UpdateDraftActionMarkupIn",
        "UpdateDraftActionMarkupOut": "_cloudsearch_841_UpdateDraftActionMarkupOut",
        "ListItemsResponseIn": "_cloudsearch_842_ListItemsResponseIn",
        "ListItemsResponseOut": "_cloudsearch_843_ListItemsResponseOut",
        "StoredParticipantIdIn": "_cloudsearch_844_StoredParticipantIdIn",
        "StoredParticipantIdOut": "_cloudsearch_845_StoredParticipantIdOut",
        "EnumPropertyOptionsIn": "_cloudsearch_846_EnumPropertyOptionsIn",
        "EnumPropertyOptionsOut": "_cloudsearch_847_EnumPropertyOptionsOut",
        "AppsDynamiteStorageCardSectionIn": "_cloudsearch_848_AppsDynamiteStorageCardSectionIn",
        "AppsDynamiteStorageCardSectionOut": "_cloudsearch_849_AppsDynamiteStorageCardSectionOut",
        "RecordingEventIn": "_cloudsearch_850_RecordingEventIn",
        "RecordingEventOut": "_cloudsearch_851_RecordingEventOut",
        "AttributeSetIn": "_cloudsearch_852_AttributeSetIn",
        "AttributeSetOut": "_cloudsearch_853_AttributeSetOut",
        "PresenterIn": "_cloudsearch_854_PresenterIn",
        "PresenterOut": "_cloudsearch_855_PresenterOut",
        "SearchItemsByViewUrlResponseIn": "_cloudsearch_856_SearchItemsByViewUrlResponseIn",
        "SearchItemsByViewUrlResponseOut": "_cloudsearch_857_SearchItemsByViewUrlResponseOut",
        "TypeInfoIn": "_cloudsearch_858_TypeInfoIn",
        "TypeInfoOut": "_cloudsearch_859_TypeInfoOut",
        "SlashCommandMetadataIn": "_cloudsearch_860_SlashCommandMetadataIn",
        "SlashCommandMetadataOut": "_cloudsearch_861_SlashCommandMetadataOut",
        "TextFieldIn": "_cloudsearch_862_TextFieldIn",
        "TextFieldOut": "_cloudsearch_863_TextFieldOut",
        "QuerySuggestionIn": "_cloudsearch_864_QuerySuggestionIn",
        "QuerySuggestionOut": "_cloudsearch_865_QuerySuggestionOut",
        "EnumOperatorOptionsIn": "_cloudsearch_866_EnumOperatorOptionsIn",
        "EnumOperatorOptionsOut": "_cloudsearch_867_EnumOperatorOptionsOut",
        "UserInfoIn": "_cloudsearch_868_UserInfoIn",
        "UserInfoOut": "_cloudsearch_869_UserInfoOut",
        "UnmappedIdentityIn": "_cloudsearch_870_UnmappedIdentityIn",
        "UnmappedIdentityOut": "_cloudsearch_871_UnmappedIdentityOut",
        "SelectionControlIn": "_cloudsearch_872_SelectionControlIn",
        "SelectionControlOut": "_cloudsearch_873_SelectionControlOut",
        "CustomerQueryStatsIn": "_cloudsearch_874_CustomerQueryStatsIn",
        "CustomerQueryStatsOut": "_cloudsearch_875_CustomerQueryStatsOut",
        "AppsDynamiteStorageColumnsColumnWidgetsIn": "_cloudsearch_876_AppsDynamiteStorageColumnsColumnWidgetsIn",
        "AppsDynamiteStorageColumnsColumnWidgetsOut": "_cloudsearch_877_AppsDynamiteStorageColumnsColumnWidgetsOut",
        "ItemThreadIn": "_cloudsearch_878_ItemThreadIn",
        "ItemThreadOut": "_cloudsearch_879_ItemThreadOut",
        "AppsDynamiteStorageTextInputIn": "_cloudsearch_880_AppsDynamiteStorageTextInputIn",
        "AppsDynamiteStorageTextInputOut": "_cloudsearch_881_AppsDynamiteStorageTextInputOut",
        "ImapsyncFolderAttributeFolderMessageFlagsIn": "_cloudsearch_882_ImapsyncFolderAttributeFolderMessageFlagsIn",
        "ImapsyncFolderAttributeFolderMessageFlagsOut": "_cloudsearch_883_ImapsyncFolderAttributeFolderMessageFlagsOut",
        "SearchQualityMetadataIn": "_cloudsearch_884_SearchQualityMetadataIn",
        "SearchQualityMetadataOut": "_cloudsearch_885_SearchQualityMetadataOut",
        "AckInfoIn": "_cloudsearch_886_AckInfoIn",
        "AckInfoOut": "_cloudsearch_887_AckInfoOut",
        "LabelCreatedIn": "_cloudsearch_888_LabelCreatedIn",
        "LabelCreatedOut": "_cloudsearch_889_LabelCreatedOut",
        "GaiaUserProtoIn": "_cloudsearch_890_GaiaUserProtoIn",
        "GaiaUserProtoOut": "_cloudsearch_891_GaiaUserProtoOut",
        "BooleanOperatorOptionsIn": "_cloudsearch_892_BooleanOperatorOptionsIn",
        "BooleanOperatorOptionsOut": "_cloudsearch_893_BooleanOperatorOptionsOut",
        "ContextAttributeIn": "_cloudsearch_894_ContextAttributeIn",
        "ContextAttributeOut": "_cloudsearch_895_ContextAttributeOut",
        "AppsDynamiteStorageGridGridItemIn": "_cloudsearch_896_AppsDynamiteStorageGridGridItemIn",
        "AppsDynamiteStorageGridGridItemOut": "_cloudsearch_897_AppsDynamiteStorageGridGridItemOut",
        "ListDataSourceResponseIn": "_cloudsearch_898_ListDataSourceResponseIn",
        "ListDataSourceResponseOut": "_cloudsearch_899_ListDataSourceResponseOut",
        "CustomerSessionStatsIn": "_cloudsearch_900_CustomerSessionStatsIn",
        "CustomerSessionStatsOut": "_cloudsearch_901_CustomerSessionStatsOut",
        "IntegerOperatorOptionsIn": "_cloudsearch_902_IntegerOperatorOptionsIn",
        "IntegerOperatorOptionsOut": "_cloudsearch_903_IntegerOperatorOptionsOut",
        "FreshnessOptionsIn": "_cloudsearch_904_FreshnessOptionsIn",
        "FreshnessOptionsOut": "_cloudsearch_905_FreshnessOptionsOut",
        "StartUploadItemRequestIn": "_cloudsearch_906_StartUploadItemRequestIn",
        "StartUploadItemRequestOut": "_cloudsearch_907_StartUploadItemRequestOut",
        "UpdateToRecipientsIn": "_cloudsearch_908_UpdateToRecipientsIn",
        "UpdateToRecipientsOut": "_cloudsearch_909_UpdateToRecipientsOut",
        "AppsDynamiteStorageSuggestionsSuggestionItemIn": "_cloudsearch_910_AppsDynamiteStorageSuggestionsSuggestionItemIn",
        "AppsDynamiteStorageSuggestionsSuggestionItemOut": "_cloudsearch_911_AppsDynamiteStorageSuggestionsSuggestionItemOut",
        "SourceCrowdingConfigIn": "_cloudsearch_912_SourceCrowdingConfigIn",
        "SourceCrowdingConfigOut": "_cloudsearch_913_SourceCrowdingConfigOut",
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn": "_cloudsearch_914_ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut": "_cloudsearch_915_ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut",
        "PhoneAccessIn": "_cloudsearch_916_PhoneAccessIn",
        "PhoneAccessOut": "_cloudsearch_917_PhoneAccessOut",
        "AppsDynamiteSharedTextWithDescriptionIn": "_cloudsearch_918_AppsDynamiteSharedTextWithDescriptionIn",
        "AppsDynamiteSharedTextWithDescriptionOut": "_cloudsearch_919_AppsDynamiteSharedTextWithDescriptionOut",
        "GoogleDocsMetadataIn": "_cloudsearch_920_GoogleDocsMetadataIn",
        "GoogleDocsMetadataOut": "_cloudsearch_921_GoogleDocsMetadataOut",
        "DateTimePickerIn": "_cloudsearch_922_DateTimePickerIn",
        "DateTimePickerOut": "_cloudsearch_923_DateTimePickerOut",
        "CustomerSettingsIn": "_cloudsearch_924_CustomerSettingsIn",
        "CustomerSettingsOut": "_cloudsearch_925_CustomerSettingsOut",
        "DividerIn": "_cloudsearch_926_DividerIn",
        "DividerOut": "_cloudsearch_927_DividerOut",
        "LabelsIn": "_cloudsearch_928_LabelsIn",
        "LabelsOut": "_cloudsearch_929_LabelsOut",
        "MdbUserProtoIn": "_cloudsearch_930_MdbUserProtoIn",
        "MdbUserProtoOut": "_cloudsearch_931_MdbUserProtoOut",
        "AppsDynamiteV1ApiCompatV1FieldIn": "_cloudsearch_932_AppsDynamiteV1ApiCompatV1FieldIn",
        "AppsDynamiteV1ApiCompatV1FieldOut": "_cloudsearch_933_AppsDynamiteV1ApiCompatV1FieldOut",
        "YouTubeBroadcastStatsIn": "_cloudsearch_934_YouTubeBroadcastStatsIn",
        "YouTubeBroadcastStatsOut": "_cloudsearch_935_YouTubeBroadcastStatsOut",
        "ClientContextIn": "_cloudsearch_936_ClientContextIn",
        "ClientContextOut": "_cloudsearch_937_ClientContextOut",
        "CustomerUserStatsIn": "_cloudsearch_938_CustomerUserStatsIn",
        "CustomerUserStatsOut": "_cloudsearch_939_CustomerUserStatsOut",
        "SettingsIn": "_cloudsearch_940_SettingsIn",
        "SettingsOut": "_cloudsearch_941_SettingsOut",
        "CompositeFilterIn": "_cloudsearch_942_CompositeFilterIn",
        "CompositeFilterOut": "_cloudsearch_943_CompositeFilterOut",
        "SearchApplicationIn": "_cloudsearch_944_SearchApplicationIn",
        "SearchApplicationOut": "_cloudsearch_945_SearchApplicationOut",
        "GetCustomerSessionStatsResponseIn": "_cloudsearch_946_GetCustomerSessionStatsResponseIn",
        "GetCustomerSessionStatsResponseOut": "_cloudsearch_947_GetCustomerSessionStatsResponseOut",
        "HangoutVideoEventMetadataIn": "_cloudsearch_948_HangoutVideoEventMetadataIn",
        "HangoutVideoEventMetadataOut": "_cloudsearch_949_HangoutVideoEventMetadataOut",
        "FuseboxPrefUpdatePreStateIn": "_cloudsearch_950_FuseboxPrefUpdatePreStateIn",
        "FuseboxPrefUpdatePreStateOut": "_cloudsearch_951_FuseboxPrefUpdatePreStateOut",
        "CalendarClientActionMarkupIn": "_cloudsearch_952_CalendarClientActionMarkupIn",
        "CalendarClientActionMarkupOut": "_cloudsearch_953_CalendarClientActionMarkupOut",
        "HtmlValuesIn": "_cloudsearch_954_HtmlValuesIn",
        "HtmlValuesOut": "_cloudsearch_955_HtmlValuesOut",
        "AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn": "_cloudsearch_956_AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn",
        "AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut": "_cloudsearch_957_AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut",
        "OtrChatMessageEventIn": "_cloudsearch_958_OtrChatMessageEventIn",
        "OtrChatMessageEventOut": "_cloudsearch_959_OtrChatMessageEventOut",
        "ItemStructuredDataIn": "_cloudsearch_960_ItemStructuredDataIn",
        "ItemStructuredDataOut": "_cloudsearch_961_ItemStructuredDataOut",
        "AppsDynamiteStorageButtonListIn": "_cloudsearch_962_AppsDynamiteStorageButtonListIn",
        "AppsDynamiteStorageButtonListOut": "_cloudsearch_963_AppsDynamiteStorageButtonListOut",
        "PackagingServiceClientIn": "_cloudsearch_964_PackagingServiceClientIn",
        "PackagingServiceClientOut": "_cloudsearch_965_PackagingServiceClientOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn": "_cloudsearch_966_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut": "_cloudsearch_967_AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut",
        "AppsDynamiteStorageOnClickIn": "_cloudsearch_968_AppsDynamiteStorageOnClickIn",
        "AppsDynamiteStorageOnClickOut": "_cloudsearch_969_AppsDynamiteStorageOnClickOut",
        "RecipientIn": "_cloudsearch_970_RecipientIn",
        "RecipientOut": "_cloudsearch_971_RecipientOut",
        "ItemCountByStatusIn": "_cloudsearch_972_ItemCountByStatusIn",
        "ItemCountByStatusOut": "_cloudsearch_973_ItemCountByStatusOut",
        "DatePropertyOptionsIn": "_cloudsearch_974_DatePropertyOptionsIn",
        "DatePropertyOptionsOut": "_cloudsearch_975_DatePropertyOptionsOut",
        "AppsDynamiteSharedMessageIntegrationPayloadIn": "_cloudsearch_976_AppsDynamiteSharedMessageIntegrationPayloadIn",
        "AppsDynamiteSharedMessageIntegrationPayloadOut": "_cloudsearch_977_AppsDynamiteSharedMessageIntegrationPayloadOut",
        "RankIn": "_cloudsearch_978_RankIn",
        "RankOut": "_cloudsearch_979_RankOut",
        "PhoneNumberIn": "_cloudsearch_980_PhoneNumberIn",
        "PhoneNumberOut": "_cloudsearch_981_PhoneNumberOut",
        "PushItemRequestIn": "_cloudsearch_982_PushItemRequestIn",
        "PushItemRequestOut": "_cloudsearch_983_PushItemRequestOut",
        "ItemAclIn": "_cloudsearch_984_ItemAclIn",
        "ItemAclOut": "_cloudsearch_985_ItemAclOut",
        "AppsDynamiteStorageIconIn": "_cloudsearch_986_AppsDynamiteStorageIconIn",
        "AppsDynamiteStorageIconOut": "_cloudsearch_987_AppsDynamiteStorageIconOut",
        "MemberIdIn": "_cloudsearch_988_MemberIdIn",
        "MemberIdOut": "_cloudsearch_989_MemberIdOut",
        "SearchItemsByViewUrlRequestIn": "_cloudsearch_990_SearchItemsByViewUrlRequestIn",
        "SearchItemsByViewUrlRequestOut": "_cloudsearch_991_SearchItemsByViewUrlRequestOut",
        "ContentReportSummaryIn": "_cloudsearch_992_ContentReportSummaryIn",
        "ContentReportSummaryOut": "_cloudsearch_993_ContentReportSummaryOut",
        "ImapUidsReassignIn": "_cloudsearch_994_ImapUidsReassignIn",
        "ImapUidsReassignOut": "_cloudsearch_995_ImapUidsReassignOut",
        "ChatConserverDynamitePlaceholderMetadataIn": "_cloudsearch_996_ChatConserverDynamitePlaceholderMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataOut": "_cloudsearch_997_ChatConserverDynamitePlaceholderMetadataOut",
        "IntegerValuesIn": "_cloudsearch_998_IntegerValuesIn",
        "IntegerValuesOut": "_cloudsearch_999_IntegerValuesOut",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn": "_cloudsearch_1000_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn",
        "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut": "_cloudsearch_1001_AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut",
        "AppsDynamiteSharedOriginAppSuggestionIn": "_cloudsearch_1002_AppsDynamiteSharedOriginAppSuggestionIn",
        "AppsDynamiteSharedOriginAppSuggestionOut": "_cloudsearch_1003_AppsDynamiteSharedOriginAppSuggestionOut",
        "AppsDynamiteV1ApiCompatV1ActionConfirmIn": "_cloudsearch_1004_AppsDynamiteV1ApiCompatV1ActionConfirmIn",
        "AppsDynamiteV1ApiCompatV1ActionConfirmOut": "_cloudsearch_1005_AppsDynamiteV1ApiCompatV1ActionConfirmOut",
        "ObjectDisplayOptionsIn": "_cloudsearch_1006_ObjectDisplayOptionsIn",
        "ObjectDisplayOptionsOut": "_cloudsearch_1007_ObjectDisplayOptionsOut",
        "ItemPartsIn": "_cloudsearch_1008_ItemPartsIn",
        "ItemPartsOut": "_cloudsearch_1009_ItemPartsOut",
        "HtmlPropertyOptionsIn": "_cloudsearch_1010_HtmlPropertyOptionsIn",
        "HtmlPropertyOptionsOut": "_cloudsearch_1011_HtmlPropertyOptionsOut",
        "AppsDynamiteSharedDimensionIn": "_cloudsearch_1012_AppsDynamiteSharedDimensionIn",
        "AppsDynamiteSharedDimensionOut": "_cloudsearch_1013_AppsDynamiteSharedDimensionOut",
        "PeopleSuggestionIn": "_cloudsearch_1014_PeopleSuggestionIn",
        "PeopleSuggestionOut": "_cloudsearch_1015_PeopleSuggestionOut",
        "QueryOperatorIn": "_cloudsearch_1016_QueryOperatorIn",
        "QueryOperatorOut": "_cloudsearch_1017_QueryOperatorOut",
        "PushItemIn": "_cloudsearch_1018_PushItemIn",
        "PushItemOut": "_cloudsearch_1019_PushItemOut",
        "MediaIn": "_cloudsearch_1020_MediaIn",
        "MediaOut": "_cloudsearch_1021_MediaOut",
        "ListOperationsResponseIn": "_cloudsearch_1022_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudsearch_1023_ListOperationsResponseOut",
        "AttributesIn": "_cloudsearch_1024_AttributesIn",
        "AttributesOut": "_cloudsearch_1025_AttributesOut",
        "DataSourceRestrictionIn": "_cloudsearch_1026_DataSourceRestrictionIn",
        "DataSourceRestrictionOut": "_cloudsearch_1027_DataSourceRestrictionOut",
        "RosterIn": "_cloudsearch_1028_RosterIn",
        "RosterOut": "_cloudsearch_1029_RosterOut",
        "CommunalLabelTagIn": "_cloudsearch_1030_CommunalLabelTagIn",
        "CommunalLabelTagOut": "_cloudsearch_1031_CommunalLabelTagOut",
        "AppsDynamiteSharedCardClickSuggestionIn": "_cloudsearch_1032_AppsDynamiteSharedCardClickSuggestionIn",
        "AppsDynamiteSharedCardClickSuggestionOut": "_cloudsearch_1033_AppsDynamiteSharedCardClickSuggestionOut",
        "AppsDynamiteSharedSegmentedMembershipCountIn": "_cloudsearch_1034_AppsDynamiteSharedSegmentedMembershipCountIn",
        "AppsDynamiteSharedSegmentedMembershipCountOut": "_cloudsearch_1035_AppsDynamiteSharedSegmentedMembershipCountOut",
        "UrlMetadataIn": "_cloudsearch_1036_UrlMetadataIn",
        "UrlMetadataOut": "_cloudsearch_1037_UrlMetadataOut",
        "CustomerSearchApplicationStatsIn": "_cloudsearch_1038_CustomerSearchApplicationStatsIn",
        "CustomerSearchApplicationStatsOut": "_cloudsearch_1039_CustomerSearchApplicationStatsOut",
        "FacetResultIn": "_cloudsearch_1040_FacetResultIn",
        "FacetResultOut": "_cloudsearch_1041_FacetResultOut",
        "SessionStateInfoIn": "_cloudsearch_1042_SessionStateInfoIn",
        "SessionStateInfoOut": "_cloudsearch_1043_SessionStateInfoOut",
        "FilterDeletedIn": "_cloudsearch_1044_FilterDeletedIn",
        "FilterDeletedOut": "_cloudsearch_1045_FilterDeletedOut",
        "InitializeCustomerRequestIn": "_cloudsearch_1046_InitializeCustomerRequestIn",
        "InitializeCustomerRequestOut": "_cloudsearch_1047_InitializeCustomerRequestOut",
        "ContentReportJustificationIn": "_cloudsearch_1048_ContentReportJustificationIn",
        "ContentReportJustificationOut": "_cloudsearch_1049_ContentReportJustificationOut",
        "CloudPrincipalProtoIn": "_cloudsearch_1050_CloudPrincipalProtoIn",
        "CloudPrincipalProtoOut": "_cloudsearch_1051_CloudPrincipalProtoOut",
        "DataLossPreventionMetadataIn": "_cloudsearch_1052_DataLossPreventionMetadataIn",
        "DataLossPreventionMetadataOut": "_cloudsearch_1053_DataLossPreventionMetadataOut",
        "VideoCallMetadataIn": "_cloudsearch_1054_VideoCallMetadataIn",
        "VideoCallMetadataOut": "_cloudsearch_1055_VideoCallMetadataOut",
        "UserIdIn": "_cloudsearch_1056_UserIdIn",
        "UserIdOut": "_cloudsearch_1057_UserIdOut",
        "UserMentionMetadataIn": "_cloudsearch_1058_UserMentionMetadataIn",
        "UserMentionMetadataOut": "_cloudsearch_1059_UserMentionMetadataOut",
        "WhiteboardInfoIn": "_cloudsearch_1060_WhiteboardInfoIn",
        "WhiteboardInfoOut": "_cloudsearch_1061_WhiteboardInfoOut",
        "UpdateDataSourceRequestIn": "_cloudsearch_1062_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_cloudsearch_1063_UpdateDataSourceRequestOut",
        "CseInfoIn": "_cloudsearch_1064_CseInfoIn",
        "CseInfoOut": "_cloudsearch_1065_CseInfoOut",
        "IndexItemRequestIn": "_cloudsearch_1066_IndexItemRequestIn",
        "IndexItemRequestOut": "_cloudsearch_1067_IndexItemRequestOut",
        "PrefUpdateIn": "_cloudsearch_1068_PrefUpdateIn",
        "PrefUpdateOut": "_cloudsearch_1069_PrefUpdateOut",
        "IntegrationConfigMutationIn": "_cloudsearch_1070_IntegrationConfigMutationIn",
        "IntegrationConfigMutationOut": "_cloudsearch_1071_IntegrationConfigMutationOut",
        "GoogleChatV1WidgetMarkupFormActionActionParameterIn": "_cloudsearch_1072_GoogleChatV1WidgetMarkupFormActionActionParameterIn",
        "GoogleChatV1WidgetMarkupFormActionActionParameterOut": "_cloudsearch_1073_GoogleChatV1WidgetMarkupFormActionActionParameterOut",
        "FilterIn": "_cloudsearch_1074_FilterIn",
        "FilterOut": "_cloudsearch_1075_FilterOut",
        "ImageIn": "_cloudsearch_1076_ImageIn",
        "ImageOut": "_cloudsearch_1077_ImageOut",
        "QueryItemIn": "_cloudsearch_1078_QueryItemIn",
        "QueryItemOut": "_cloudsearch_1079_QueryItemOut",
        "OpenCreatedDraftActionMarkupIn": "_cloudsearch_1080_OpenCreatedDraftActionMarkupIn",
        "OpenCreatedDraftActionMarkupOut": "_cloudsearch_1081_OpenCreatedDraftActionMarkupOut",
        "QueryInterpretationOptionsIn": "_cloudsearch_1082_QueryInterpretationOptionsIn",
        "QueryInterpretationOptionsOut": "_cloudsearch_1083_QueryInterpretationOptionsOut",
        "UserIn": "_cloudsearch_1084_UserIn",
        "UserOut": "_cloudsearch_1085_UserOut",
        "LanguageConfigIn": "_cloudsearch_1086_LanguageConfigIn",
        "LanguageConfigOut": "_cloudsearch_1087_LanguageConfigOut",
        "DocumentInfoIn": "_cloudsearch_1088_DocumentInfoIn",
        "DocumentInfoOut": "_cloudsearch_1089_DocumentInfoOut",
        "BooleanPropertyOptionsIn": "_cloudsearch_1090_BooleanPropertyOptionsIn",
        "BooleanPropertyOptionsOut": "_cloudsearch_1091_BooleanPropertyOptionsOut",
        "UserDisplayInfoIn": "_cloudsearch_1092_UserDisplayInfoIn",
        "UserDisplayInfoOut": "_cloudsearch_1093_UserDisplayInfoOut",
        "EnumValuePairIn": "_cloudsearch_1094_EnumValuePairIn",
        "EnumValuePairOut": "_cloudsearch_1095_EnumValuePairOut",
        "TriggerIn": "_cloudsearch_1096_TriggerIn",
        "TriggerOut": "_cloudsearch_1097_TriggerOut",
        "PossiblyTrimmedModelIn": "_cloudsearch_1098_PossiblyTrimmedModelIn",
        "PossiblyTrimmedModelOut": "_cloudsearch_1099_PossiblyTrimmedModelOut",
        "UpdateSubjectIn": "_cloudsearch_1100_UpdateSubjectIn",
        "UpdateSubjectOut": "_cloudsearch_1101_UpdateSubjectOut",
        "AppsDynamiteSharedAssistantDebugContextIn": "_cloudsearch_1102_AppsDynamiteSharedAssistantDebugContextIn",
        "AppsDynamiteSharedAssistantDebugContextOut": "_cloudsearch_1103_AppsDynamiteSharedAssistantDebugContextOut",
        "DateOperatorOptionsIn": "_cloudsearch_1104_DateOperatorOptionsIn",
        "DateOperatorOptionsOut": "_cloudsearch_1105_DateOperatorOptionsOut",
        "OtrModificationEventIn": "_cloudsearch_1106_OtrModificationEventIn",
        "OtrModificationEventOut": "_cloudsearch_1107_OtrModificationEventOut",
        "RequiredMessageFeaturesMetadataIn": "_cloudsearch_1108_RequiredMessageFeaturesMetadataIn",
        "RequiredMessageFeaturesMetadataOut": "_cloudsearch_1109_RequiredMessageFeaturesMetadataOut",
        "YouTubeLiveBroadcastEventIn": "_cloudsearch_1110_YouTubeLiveBroadcastEventIn",
        "YouTubeLiveBroadcastEventOut": "_cloudsearch_1111_YouTubeLiveBroadcastEventOut",
        "ImageCropStyleIn": "_cloudsearch_1112_ImageCropStyleIn",
        "ImageCropStyleOut": "_cloudsearch_1113_ImageCropStyleOut",
        "AppsDynamiteSharedTextSegmentIn": "_cloudsearch_1114_AppsDynamiteSharedTextSegmentIn",
        "AppsDynamiteSharedTextSegmentOut": "_cloudsearch_1115_AppsDynamiteSharedTextSegmentOut",
        "GoogleChatV1WidgetMarkupKeyValueIn": "_cloudsearch_1116_GoogleChatV1WidgetMarkupKeyValueIn",
        "GoogleChatV1WidgetMarkupKeyValueOut": "_cloudsearch_1117_GoogleChatV1WidgetMarkupKeyValueOut",
        "SearchApplicationQueryStatsIn": "_cloudsearch_1118_SearchApplicationQueryStatsIn",
        "SearchApplicationQueryStatsOut": "_cloudsearch_1119_SearchApplicationQueryStatsOut",
        "PrivateMessageInfoIn": "_cloudsearch_1120_PrivateMessageInfoIn",
        "PrivateMessageInfoOut": "_cloudsearch_1121_PrivateMessageInfoOut",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn": "_cloudsearch_1122_AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn",
        "AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut": "_cloudsearch_1123_AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut",
        "SourceResultCountIn": "_cloudsearch_1124_SourceResultCountIn",
        "SourceResultCountOut": "_cloudsearch_1125_SourceResultCountOut",
        "SnippetIn": "_cloudsearch_1126_SnippetIn",
        "SnippetOut": "_cloudsearch_1127_SnippetOut",
        "AppsDynamiteStorageWidgetIn": "_cloudsearch_1128_AppsDynamiteStorageWidgetIn",
        "AppsDynamiteStorageWidgetOut": "_cloudsearch_1129_AppsDynamiteStorageWidgetOut",
        "ReadReceiptsSettingsUpdatedMetadataIn": "_cloudsearch_1130_ReadReceiptsSettingsUpdatedMetadataIn",
        "ReadReceiptsSettingsUpdatedMetadataOut": "_cloudsearch_1131_ReadReceiptsSettingsUpdatedMetadataOut",
        "AttributeIn": "_cloudsearch_1132_AttributeIn",
        "AttributeOut": "_cloudsearch_1133_AttributeOut",
        "GoogleChatV1WidgetMarkupTextParagraphIn": "_cloudsearch_1134_GoogleChatV1WidgetMarkupTextParagraphIn",
        "GoogleChatV1WidgetMarkupTextParagraphOut": "_cloudsearch_1135_GoogleChatV1WidgetMarkupTextParagraphOut",
        "AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn": "_cloudsearch_1136_AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn",
        "AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut": "_cloudsearch_1137_AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut",
        "AutoCompleteItemIn": "_cloudsearch_1138_AutoCompleteItemIn",
        "AutoCompleteItemOut": "_cloudsearch_1139_AutoCompleteItemOut",
        "FolderAttributeIn": "_cloudsearch_1140_FolderAttributeIn",
        "FolderAttributeOut": "_cloudsearch_1141_FolderAttributeOut",
        "MatchInfoIn": "_cloudsearch_1142_MatchInfoIn",
        "MatchInfoOut": "_cloudsearch_1143_MatchInfoOut",
        "ChatProtoIn": "_cloudsearch_1144_ChatProtoIn",
        "ChatProtoOut": "_cloudsearch_1145_ChatProtoOut",
        "StructuredResultIn": "_cloudsearch_1146_StructuredResultIn",
        "StructuredResultOut": "_cloudsearch_1147_StructuredResultOut",
        "ActionParameterIn": "_cloudsearch_1148_ActionParameterIn",
        "ActionParameterOut": "_cloudsearch_1149_ActionParameterOut",
        "ReactionInfoIn": "_cloudsearch_1150_ReactionInfoIn",
        "ReactionInfoOut": "_cloudsearch_1151_ReactionInfoOut",
        "ToolbarIn": "_cloudsearch_1152_ToolbarIn",
        "ToolbarOut": "_cloudsearch_1153_ToolbarOut",
        "GoogleChatV1WidgetMarkupImageButtonIn": "_cloudsearch_1154_GoogleChatV1WidgetMarkupImageButtonIn",
        "GoogleChatV1WidgetMarkupImageButtonOut": "_cloudsearch_1155_GoogleChatV1WidgetMarkupImageButtonOut",
        "ContactGroupProtoIn": "_cloudsearch_1156_ContactGroupProtoIn",
        "ContactGroupProtoOut": "_cloudsearch_1157_ContactGroupProtoOut",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn": "_cloudsearch_1158_AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupIn",
        "AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut": "_cloudsearch_1159_AppsExtensionsMarkupCalendarClientActionMarkupEditAttendeesActionMarkupOut",
        "ChatConserverDynamitePlaceholderMetadataTasksMetadataIn": "_cloudsearch_1160_ChatConserverDynamitePlaceholderMetadataTasksMetadataIn",
        "ChatConserverDynamitePlaceholderMetadataTasksMetadataOut": "_cloudsearch_1161_ChatConserverDynamitePlaceholderMetadataTasksMetadataOut",
        "ScoringConfigIn": "_cloudsearch_1162_ScoringConfigIn",
        "ScoringConfigOut": "_cloudsearch_1163_ScoringConfigOut",
        "SupportUrlsIn": "_cloudsearch_1164_SupportUrlsIn",
        "SupportUrlsOut": "_cloudsearch_1165_SupportUrlsOut",
        "AttributeRemovedIn": "_cloudsearch_1166_AttributeRemovedIn",
        "AttributeRemovedOut": "_cloudsearch_1167_AttributeRemovedOut",
        "MeetingSpaceIn": "_cloudsearch_1168_MeetingSpaceIn",
        "MeetingSpaceOut": "_cloudsearch_1169_MeetingSpaceOut",
        "StreamViewerStatsIn": "_cloudsearch_1170_StreamViewerStatsIn",
        "StreamViewerStatsOut": "_cloudsearch_1171_StreamViewerStatsOut",
        "TextValuesIn": "_cloudsearch_1172_TextValuesIn",
        "TextValuesOut": "_cloudsearch_1173_TextValuesOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SortOptionsIn"] = t.struct(
        {"operatorName": t.string().optional(), "sortOrder": t.string().optional()}
    ).named(renames["SortOptionsIn"])
    types["SortOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "sortOrder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortOptionsOut"])
    types["FacetBucketIn"] = t.struct(
        {
            "count": t.integer().optional(),
            "percentage": t.integer().optional(),
            "value": t.proxy(renames["ValueIn"]),
            "filter": t.proxy(renames["FilterIn"]).optional(),
        }
    ).named(renames["FacetBucketIn"])
    types["FacetBucketOut"] = t.struct(
        {
            "count": t.integer().optional(),
            "percentage": t.integer().optional(),
            "value": t.proxy(renames["ValueOut"]),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetBucketOut"])
    types["ListItemNamesForUnmappedIdentityResponseIn"] = t.struct(
        {"nextPageToken": t.string().optional(), "itemNames": t.array(t.string())}
    ).named(renames["ListItemNamesForUnmappedIdentityResponseIn"])
    types["ListItemNamesForUnmappedIdentityResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "itemNames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemNamesForUnmappedIdentityResponseOut"])
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
    types["DateValuesIn"] = t.struct(
        {"values": t.array(t.proxy(renames["DateIn"]))}
    ).named(renames["DateValuesIn"])
    types["DateValuesOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["DateOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateValuesOut"])
    types["LabelRenamedIn"] = t.struct({"oldCanonicalName": t.string()}).named(
        renames["LabelRenamedIn"]
    )
    types["LabelRenamedOut"] = t.struct(
        {
            "oldCanonicalName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelRenamedOut"])
    types["TransientDataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TransientDataIn"]
    )
    types["TransientDataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TransientDataOut"])
    types["EmailAddressIn"] = t.struct(
        {
            "type": t.string().optional(),
            "emailUrl": t.string().optional(),
            "emailAddress": t.string().optional(),
            "primary": t.boolean().optional(),
            "customType": t.string().optional(),
        }
    ).named(renames["EmailAddressIn"])
    types["EmailAddressOut"] = t.struct(
        {
            "type": t.string().optional(),
            "emailUrl": t.string().optional(),
            "emailAddress": t.string().optional(),
            "primary": t.boolean().optional(),
            "customType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailAddressOut"])
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
    types["RequestOptionsIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "languageCode": t.string().optional(),
            "searchApplicationId": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["RequestOptionsIn"])
    types["RequestOptionsOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "languageCode": t.string().optional(),
            "searchApplicationId": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOptionsOut"])
    types["FacetOptionsIn"] = t.struct(
        {
            "sourceName": t.string().optional(),
            "numFacetBuckets": t.integer().optional(),
            "objectType": t.string().optional(),
            "operatorName": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsIn"]
            ).optional(),
        }
    ).named(renames["FacetOptionsIn"])
    types["FacetOptionsOut"] = t.struct(
        {
            "sourceName": t.string().optional(),
            "numFacetBuckets": t.integer().optional(),
            "objectType": t.string().optional(),
            "operatorName": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetOptionsOut"])
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
    types["ThreadUpdateIn"] = t.struct(
        {
            "threadLocator": t.string().optional(),
            "labelRemoved": t.proxy(renames["LabelRemovedIn"]),
            "messageAdded": t.proxy(renames["MessageAddedIn"]),
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "originalThreadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "lastHistoryRecordId": t.string().optional(),
            "preState": t.array(t.proxy(renames["PreStateIn"])).optional(),
            "topicStateUpdate": t.proxy(renames["TopicStateUpdateIn"]),
            "attributeRemoved": t.proxy(renames["AttributeRemovedIn"]),
            "attributeSet": t.proxy(renames["AttributeSetIn"]),
            "threadKeySet": t.proxy(renames["ThreadKeySetIn"]),
            "labelAdded": t.proxy(renames["LabelAddedIn"]),
            "messageDeleted": t.proxy(renames["MessageDeletedIn"]),
        }
    ).named(renames["ThreadUpdateIn"])
    types["ThreadUpdateOut"] = t.struct(
        {
            "threadLocator": t.string().optional(),
            "labelRemoved": t.proxy(renames["LabelRemovedOut"]),
            "messageAdded": t.proxy(renames["MessageAddedOut"]),
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "originalThreadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "lastHistoryRecordId": t.string().optional(),
            "preState": t.array(t.proxy(renames["PreStateOut"])).optional(),
            "topicStateUpdate": t.proxy(renames["TopicStateUpdateOut"]),
            "attributeRemoved": t.proxy(renames["AttributeRemovedOut"]),
            "attributeSet": t.proxy(renames["AttributeSetOut"]),
            "threadKeySet": t.proxy(renames["ThreadKeySetOut"]),
            "labelAdded": t.proxy(renames["LabelAddedOut"]),
            "messageDeleted": t.proxy(renames["MessageDeletedOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThreadUpdateOut"])
    types["BroadcastSessionInfoIn"] = t.struct(
        {
            "broadcastSessionId": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
            "ingestionId": t.string().optional(),
        }
    ).named(renames["BroadcastSessionInfoIn"])
    types["BroadcastSessionInfoOut"] = t.struct(
        {
            "broadcastSessionId": t.string().optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "ingestionId": t.string().optional(),
            "broadcastStats": t.proxy(renames["BroadcastStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BroadcastSessionInfoOut"])
    types["ImapsyncFolderAttributeFolderMessageIn"] = t.struct(
        {
            "uid": t.string().optional(),
            "flags": t.proxy(
                renames["ImapsyncFolderAttributeFolderMessageFlagsIn"]
            ).optional(),
        }
    ).named(renames["ImapsyncFolderAttributeFolderMessageIn"])
    types["ImapsyncFolderAttributeFolderMessageOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "flags": t.proxy(
                renames["ImapsyncFolderAttributeFolderMessageFlagsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapsyncFolderAttributeFolderMessageOut"])
    types["EmailOwnerProtoIn"] = t.struct({"email": t.string()}).named(
        renames["EmailOwnerProtoIn"]
    )
    types["EmailOwnerProtoOut"] = t.struct(
        {"email": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmailOwnerProtoOut"])
    types["ImapSessionContextIn"] = t.struct(
        {
            "app": t.string(),
            "deviceType": t.string().optional(),
            "guidFingerprint": t.string().optional(),
            "possiblyTrimmedModel": t.proxy(renames["PossiblyTrimmedModelIn"]),
            "os": t.string(),
            "osVersion": t.proxy(renames["OsVersionIn"]),
        }
    ).named(renames["ImapSessionContextIn"])
    types["ImapSessionContextOut"] = t.struct(
        {
            "app": t.string(),
            "deviceType": t.string().optional(),
            "guidFingerprint": t.string().optional(),
            "possiblyTrimmedModel": t.proxy(renames["PossiblyTrimmedModelOut"]),
            "os": t.string(),
            "osVersion": t.proxy(renames["OsVersionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapSessionContextOut"])
    types["CallSettingsIn"] = t.struct(
        {
            "chatLock": t.boolean().optional(),
            "videoLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "accessType": t.string().optional(),
            "accessLock": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "audioLock": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
        }
    ).named(renames["CallSettingsIn"])
    types["CallSettingsOut"] = t.struct(
        {
            "chatLock": t.boolean().optional(),
            "videoLock": t.boolean().optional(),
            "cseEnabled": t.boolean().optional(),
            "accessType": t.string().optional(),
            "accessLock": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "audioLock": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CallSettingsOut"])
    types["AppsDynamiteStorageDecoratedTextSwitchControlIn"] = t.struct(
        {
            "controlType": t.string().optional(),
            "selected": t.boolean().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextSwitchControlIn"])
    types["AppsDynamiteStorageDecoratedTextSwitchControlOut"] = t.struct(
        {
            "controlType": t.string().optional(),
            "selected": t.boolean().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextSwitchControlOut"])
    types["TaskActionMarkupIn"] = t.struct({"reloadTasks": t.boolean()}).named(
        renames["TaskActionMarkupIn"]
    )
    types["TaskActionMarkupOut"] = t.struct(
        {
            "reloadTasks": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskActionMarkupOut"])
    types["ItemIn"] = t.struct(
        {
            "acl": t.proxy(renames["ItemAclIn"]).optional(),
            "metadata": t.proxy(renames["ItemMetadataIn"]).optional(),
            "status": t.proxy(renames["ItemStatusIn"]).optional(),
            "version": t.string(),
            "payload": t.string().optional(),
            "queue": t.string().optional(),
            "structuredData": t.proxy(renames["ItemStructuredDataIn"]).optional(),
            "name": t.string().optional(),
            "itemType": t.string().optional(),
            "content": t.proxy(renames["ItemContentIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "acl": t.proxy(renames["ItemAclOut"]).optional(),
            "metadata": t.proxy(renames["ItemMetadataOut"]).optional(),
            "status": t.proxy(renames["ItemStatusOut"]).optional(),
            "version": t.string(),
            "payload": t.string().optional(),
            "queue": t.string().optional(),
            "structuredData": t.proxy(renames["ItemStructuredDataOut"]).optional(),
            "name": t.string().optional(),
            "itemType": t.string().optional(),
            "content": t.proxy(renames["ItemContentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"])
    types["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"])
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
    types["UpdateBodyIn"] = t.struct(
        {
            "type": t.string(),
            "insertContents": t.array(t.proxy(renames["InsertContentIn"])).optional(),
        }
    ).named(renames["UpdateBodyIn"])
    types["UpdateBodyOut"] = t.struct(
        {
            "type": t.string(),
            "insertContents": t.array(t.proxy(renames["InsertContentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBodyOut"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataIn"] = t.struct(
        {
            "activityFeedMessageId": t.proxy(renames["MessageIdIn"]).optional(),
            "sharedUserInfo": t.proxy(renames["UserInfoIn"]).optional(),
            "chatItem": t.proxy(renames["AppsDynamiteSharedChatItemIn"]),
            "userInfo": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoIn"]
            ).optional(),
            "activityFeedMessageCreateTime": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataIn"])
    types["AppsDynamiteSharedActivityFeedAnnotationDataOut"] = t.struct(
        {
            "activityFeedMessageId": t.proxy(renames["MessageIdOut"]).optional(),
            "sharedUserInfo": t.proxy(renames["UserInfoOut"]).optional(),
            "chatItem": t.proxy(renames["AppsDynamiteSharedChatItemOut"]),
            "userInfo": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataUserInfoOut"]
            ).optional(),
            "activityFeedMessageCreateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedActivityFeedAnnotationDataOut"])
    types["IndexItemOptionsIn"] = t.struct(
        {"allowUnknownGsuitePrincipals": t.boolean().optional()}
    ).named(renames["IndexItemOptionsIn"])
    types["IndexItemOptionsOut"] = t.struct(
        {
            "allowUnknownGsuitePrincipals": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexItemOptionsOut"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationIn"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataEventCreationOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["TopicStateIn"] = t.struct(
        {
            "labelIdMessageCount": t.struct({"_": t.string().optional()}).optional(),
            "numConstituents": t.integer().optional(),
        }
    ).named(renames["TopicStateIn"])
    types["TopicStateOut"] = t.struct(
        {
            "labelIdMessageCount": t.struct({"_": t.string().optional()}).optional(),
            "numConstituents": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicStateOut"])
    types["OAuthConsumerProtoIn"] = t.struct({"domain": t.string()}).named(
        renames["OAuthConsumerProtoIn"]
    )
    types["OAuthConsumerProtoOut"] = t.struct(
        {"domain": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OAuthConsumerProtoOut"])
    types["AppsDynamiteSharedCallAnnotationDataIn"] = t.struct(
        {
            "callMetadata": t.proxy(renames["AppsDynamiteSharedCallMetadataIn"]),
            "callEndedTimestamp": t.string().optional(),
            "callStatus": t.string(),
        }
    ).named(renames["AppsDynamiteSharedCallAnnotationDataIn"])
    types["AppsDynamiteSharedCallAnnotationDataOut"] = t.struct(
        {
            "callMetadata": t.proxy(renames["AppsDynamiteSharedCallMetadataOut"]),
            "callEndedTimestamp": t.string().optional(),
            "callStatus": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCallAnnotationDataOut"])
    types["CardCapabilityMetadataIn"] = t.struct(
        {"requiredCapabilities": t.array(t.string()).optional()}
    ).named(renames["CardCapabilityMetadataIn"])
    types["CardCapabilityMetadataOut"] = t.struct(
        {
            "requiredCapabilities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardCapabilityMetadataOut"])
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
    types["AppsDynamiteSharedDlpMetricsMetadataIn"] = t.struct(
        {"dlpStatus": t.string().optional()}
    ).named(renames["AppsDynamiteSharedDlpMetricsMetadataIn"])
    types["AppsDynamiteSharedDlpMetricsMetadataOut"] = t.struct(
        {
            "dlpStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedDlpMetricsMetadataOut"])
    types["HtmlOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["HtmlOperatorOptionsIn"])
    types["HtmlOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlOperatorOptionsOut"])
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
    types["LabelUpdatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelUpdatedIn"]
    )
    types["LabelUpdatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelUpdatedOut"])
    types["GoogleChatV1WidgetMarkupIn"] = t.struct(
        {
            "image": t.proxy(renames["GoogleChatV1WidgetMarkupImageIn"]).optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupButtonIn"])
            ).optional(),
            "keyValue": t.proxy(
                renames["GoogleChatV1WidgetMarkupKeyValueIn"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["GoogleChatV1WidgetMarkupTextParagraphIn"]
            ).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupIn"])
    types["GoogleChatV1WidgetMarkupOut"] = t.struct(
        {
            "image": t.proxy(renames["GoogleChatV1WidgetMarkupImageOut"]).optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleChatV1WidgetMarkupButtonOut"])
            ).optional(),
            "keyValue": t.proxy(
                renames["GoogleChatV1WidgetMarkupKeyValueOut"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["GoogleChatV1WidgetMarkupTextParagraphOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupOut"])
    types["QuotedMessageMetadataIn"] = t.struct(
        {
            "messageId": t.proxy(renames["MessageIdIn"]).optional(),
            "lastUpdateTimeWhenQuotedMicros": t.string().optional(),
        }
    ).named(renames["QuotedMessageMetadataIn"])
    types["QuotedMessageMetadataOut"] = t.struct(
        {
            "messageState": t.string().optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsOut"]
            ).optional(),
            "createTimeMicros": t.string().optional(),
            "updaterId": t.proxy(renames["UserIdOut"]).optional(),
            "textBody": t.string().optional(),
            "appProfile": t.proxy(
                renames["AppsDynamiteSharedAppProfileOut"]
            ).optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataOut"])).optional(),
            "botAttachmentState": t.string().optional(),
            "messageId": t.proxy(renames["MessageIdOut"]).optional(),
            "lastUpdateTimeWhenQuotedMicros": t.string().optional(),
            "lastEditTimeMicros": t.string().optional(),
            "creatorId": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotedMessageMetadataOut"])
    types["SectionIn"] = t.struct(
        {
            "numUncollapsableWidgets": t.integer().optional(),
            "collapsable": t.boolean().optional(),
            "widgets": t.array(t.proxy(renames["WidgetMarkupIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SectionIn"])
    types["SectionOut"] = t.struct(
        {
            "numUncollapsableWidgets": t.integer().optional(),
            "collapsable": t.boolean().optional(),
            "widgets": t.array(t.proxy(renames["WidgetMarkupOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionOut"])
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
    types["TriggersIn"] = t.struct(
        {"triggers": t.array(t.proxy(renames["TriggerIn"])).optional()}
    ).named(renames["TriggersIn"])
    types["TriggersOut"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggersOut"])
    types["ReferencesIn"] = t.struct(
        {"references": t.array(t.proxy(renames["ReferenceIn"]))}
    ).named(renames["ReferencesIn"])
    types["ReferencesOut"] = t.struct(
        {
            "references": t.array(t.proxy(renames["ReferenceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferencesOut"])
    types["AppsDynamiteSharedJustificationIn"] = t.struct(
        {
            "documentOwner": t.proxy(
                renames["AppsDynamiteSharedJustificationPersonIn"]
            ).optional(),
            "topics": t.array(t.string()).optional(),
            "actionTime": t.string().optional(),
            "actionType": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedJustificationIn"])
    types["AppsDynamiteSharedJustificationOut"] = t.struct(
        {
            "documentOwner": t.proxy(
                renames["AppsDynamiteSharedJustificationPersonOut"]
            ).optional(),
            "topics": t.array(t.string()).optional(),
            "actionTime": t.string().optional(),
            "actionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedJustificationOut"])
    types["PrefDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PrefDeletedIn"]
    )
    types["PrefDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PrefDeletedOut"])
    types["ResponseDebugInfoIn"] = t.struct(
        {"formattedDebugInfo": t.string().optional()}
    ).named(renames["ResponseDebugInfoIn"])
    types["ResponseDebugInfoOut"] = t.struct(
        {
            "formattedDebugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseDebugInfoOut"])
    types["SocialGraphNodeProtoIn"] = t.struct(
        {"sgnDomain": t.string().optional(), "sgnPk": t.string()}
    ).named(renames["SocialGraphNodeProtoIn"])
    types["SocialGraphNodeProtoOut"] = t.struct(
        {
            "sgnDomain": t.string().optional(),
            "sgnPk": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocialGraphNodeProtoOut"])
    types["TimestampOperatorOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
        }
    ).named(renames["TimestampOperatorOptionsIn"])
    types["TimestampOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampOperatorOptionsOut"])
    types["IdIn"] = t.struct(
        {
            "localId": t.string().optional(),
            "creatorUserId": t.string().optional(),
            "nameSpace": t.integer().optional(),
        }
    ).named(renames["IdIn"])
    types["IdOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "creatorUserId": t.string().optional(),
            "nameSpace": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdOut"])
    types["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"])
    types["CardHeaderIn"] = t.struct(
        {
            "subtitle": t.string(),
            "title": t.string().optional(),
            "imageStyle": t.string(),
            "imageAltText": t.string().optional(),
            "imageUrl": t.string(),
        }
    ).named(renames["CardHeaderIn"])
    types["CardHeaderOut"] = t.struct(
        {
            "subtitle": t.string(),
            "title": t.string().optional(),
            "imageStyle": t.string(),
            "imageAltText": t.string().optional(),
            "imageUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardHeaderOut"])
    types["RecordingSessionInfoIn"] = t.struct(
        {
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
            "recordingSessionId": t.string().optional(),
            "ownerEmail": t.string().optional(),
        }
    ).named(renames["RecordingSessionInfoIn"])
    types["RecordingSessionInfoOut"] = t.struct(
        {
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "recordingSessionId": t.string().optional(),
            "ownerEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordingSessionInfoOut"])
    types["AppsDynamiteSharedCustomEmojiIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "readToken": t.string().optional(),
            "ownerCustomerId": t.proxy(renames["CustomerIdIn"]).optional(),
            "shortcode": t.string().optional(),
            "creatorUserId": t.proxy(renames["UserIdIn"]).optional(),
            "createTimeMicros": t.string().optional(),
            "blobId": t.string().optional(),
            "uuid": t.string().optional(),
            "updateTimeMicros": t.string(),
            "deleteTimeMicros": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedCustomEmojiIn"])
    types["AppsDynamiteSharedCustomEmojiOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "readToken": t.string().optional(),
            "ownerCustomerId": t.proxy(renames["CustomerIdOut"]).optional(),
            "shortcode": t.string().optional(),
            "creatorUserId": t.proxy(renames["UserIdOut"]).optional(),
            "ephemeralUrl": t.string().optional(),
            "createTimeMicros": t.string().optional(),
            "blobId": t.string().optional(),
            "uuid": t.string().optional(),
            "updateTimeMicros": t.string(),
            "deleteTimeMicros": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCustomEmojiOut"])
    types["DoubleValuesIn"] = t.struct({"values": t.array(t.number())}).named(
        renames["DoubleValuesIn"]
    )
    types["DoubleValuesOut"] = t.struct(
        {
            "values": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleValuesOut"])
    types["FilterCreatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilterCreatedIn"]
    )
    types["FilterCreatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FilterCreatedOut"])
    types["AppsDynamiteV1ApiCompatV1ActionIn"] = t.struct(
        {
            "text": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "confirm": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1ActionConfirmIn"]
            ).optional(),
            "style": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionIn"])
    types["AppsDynamiteV1ApiCompatV1ActionOut"] = t.struct(
        {
            "text": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "confirm": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1ActionConfirmOut"]
            ).optional(),
            "style": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionOut"])
    types["DeleteQueueItemsRequestIn"] = t.struct(
        {
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["DeleteQueueItemsRequestIn"])
    types["DeleteQueueItemsRequestOut"] = t.struct(
        {
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteQueueItemsRequestOut"])
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
    types["SearchResponseIn"] = t.struct(
        {
            "errorInfo": t.proxy(renames["ErrorInfoIn"]).optional(),
            "resultCounts": t.proxy(renames["ResultCountsIn"]).optional(),
            "resultCountEstimate": t.string().optional(),
            "debugInfo": t.proxy(renames["ResponseDebugInfoIn"]).optional(),
            "queryInterpretation": t.proxy(renames["QueryInterpretationIn"]).optional(),
            "results": t.array(t.proxy(renames["SearchResultIn"])).optional(),
            "resultCountExact": t.string().optional(),
            "hasMoreResults": t.boolean().optional(),
            "facetResults": t.array(t.proxy(renames["FacetResultIn"])).optional(),
            "structuredResults": t.array(
                t.proxy(renames["StructuredResultIn"])
            ).optional(),
            "spellResults": t.array(t.proxy(renames["SpellResultIn"])).optional(),
        }
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "errorInfo": t.proxy(renames["ErrorInfoOut"]).optional(),
            "resultCounts": t.proxy(renames["ResultCountsOut"]).optional(),
            "resultCountEstimate": t.string().optional(),
            "debugInfo": t.proxy(renames["ResponseDebugInfoOut"]).optional(),
            "queryInterpretation": t.proxy(
                renames["QueryInterpretationOut"]
            ).optional(),
            "results": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "resultCountExact": t.string().optional(),
            "hasMoreResults": t.boolean().optional(),
            "facetResults": t.array(t.proxy(renames["FacetResultOut"])).optional(),
            "structuredResults": t.array(
                t.proxy(renames["StructuredResultOut"])
            ).optional(),
            "spellResults": t.array(t.proxy(renames["SpellResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
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
    types["DynamiteSpacesScoringInfoIn"] = t.struct(
        {
            "memberCountScore": t.number(),
            "contactsIntersectionCount": t.number(),
            "lastMessagePostedTimestampSecs": t.string(),
            "smallUnjoinedSpacesAffinityScore": t.number(),
            "freshnessScore": t.number(),
            "lastReadTimestampSecs": t.string(),
            "memberMetadataCount": t.number(),
            "commonContactCountAffinityScore": t.number(),
            "joinedSpacesAffinityScore": t.number(),
            "spaceCreationTimestampSecs": t.string(),
            "spaceAgeInDays": t.number(),
            "topicalityScore": t.number(),
            "smallContactListAffinityScore": t.number(),
            "messageScore": t.number(),
            "finalScore": t.number(),
            "affinityScore": t.number(),
            "numAucContacts": t.string(),
        }
    ).named(renames["DynamiteSpacesScoringInfoIn"])
    types["DynamiteSpacesScoringInfoOut"] = t.struct(
        {
            "memberCountScore": t.number(),
            "contactsIntersectionCount": t.number(),
            "lastMessagePostedTimestampSecs": t.string(),
            "smallUnjoinedSpacesAffinityScore": t.number(),
            "freshnessScore": t.number(),
            "lastReadTimestampSecs": t.string(),
            "memberMetadataCount": t.number(),
            "commonContactCountAffinityScore": t.number(),
            "joinedSpacesAffinityScore": t.number(),
            "spaceCreationTimestampSecs": t.string(),
            "spaceAgeInDays": t.number(),
            "topicalityScore": t.number(),
            "smallContactListAffinityScore": t.number(),
            "messageScore": t.number(),
            "finalScore": t.number(),
            "affinityScore": t.number(),
            "numAucContacts": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamiteSpacesScoringInfoOut"])
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
    types["SelectionItemIn"] = t.struct(
        {
            "value": t.string().optional(),
            "selected": t.boolean().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["SelectionItemIn"])
    types["SelectionItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "selected": t.boolean().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionItemOut"])
    types["SearchRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "pageSize": t.integer().optional(),
            "start": t.integer().optional(),
            "facetOptions": t.array(t.proxy(renames["FacetOptionsIn"])),
            "queryInterpretationOptions": t.proxy(
                renames["QueryInterpretationOptionsIn"]
            ).optional(),
            "query": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeIn"])
            ).optional(),
            "sortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
        }
    ).named(renames["SearchRequestIn"])
    types["SearchRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "pageSize": t.integer().optional(),
            "start": t.integer().optional(),
            "facetOptions": t.array(t.proxy(renames["FacetOptionsOut"])),
            "queryInterpretationOptions": t.proxy(
                renames["QueryInterpretationOptionsOut"]
            ).optional(),
            "query": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeOut"])
            ).optional(),
            "sortOptions": t.proxy(renames["SortOptionsOut"]).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchRequestOut"])
    types["GoogleChatV1WidgetMarkupOpenLinkIn"] = t.struct(
        {"url": t.string().optional()}
    ).named(renames["GoogleChatV1WidgetMarkupOpenLinkIn"])
    types["GoogleChatV1WidgetMarkupOpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupOpenLinkOut"])
    types["RestrictItemIn"] = t.struct(
        {
            "driveFollowUpRestrict": t.proxy(renames["DriveFollowUpRestrictIn"]),
            "driveTimeSpanRestrict": t.proxy(renames["DriveTimeSpanRestrictIn"]),
            "searchOperator": t.string().optional(),
            "driveLocationRestrict": t.proxy(renames["DriveLocationRestrictIn"]),
            "driveMimeTypeRestrict": t.proxy(
                renames["DriveMimeTypeRestrictIn"]
            ).optional(),
        }
    ).named(renames["RestrictItemIn"])
    types["RestrictItemOut"] = t.struct(
        {
            "driveFollowUpRestrict": t.proxy(renames["DriveFollowUpRestrictOut"]),
            "driveTimeSpanRestrict": t.proxy(renames["DriveTimeSpanRestrictOut"]),
            "searchOperator": t.string().optional(),
            "driveLocationRestrict": t.proxy(renames["DriveLocationRestrictOut"]),
            "driveMimeTypeRestrict": t.proxy(
                renames["DriveMimeTypeRestrictOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictItemOut"])
    types["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"] = t.struct(
        {"filename": t.string()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"] = t.struct(
        {"filename": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"])
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
    types["ImapUpdateIn"] = t.struct(
        {"imapUidsReassign": t.proxy(renames["ImapUidsReassignIn"])}
    ).named(renames["ImapUpdateIn"])
    types["ImapUpdateOut"] = t.struct(
        {
            "imapUidsReassign": t.proxy(renames["ImapUidsReassignOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapUpdateOut"])
    types["LdapUserProtoIn"] = t.struct({"userName": t.string()}).named(
        renames["LdapUserProtoIn"]
    )
    types["LdapUserProtoOut"] = t.struct(
        {"userName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LdapUserProtoOut"])
    types["CallInfoIn"] = t.struct(
        {
            "abuseReportingConfig": t.proxy(
                renames["AbuseReportingConfigIn"]
            ).optional(),
            "collaboration": t.proxy(renames["CollaborationIn"]).optional(),
            "youTubeBroadcastSessionInfos": t.array(
                t.proxy(renames["YouTubeBroadcastSessionInfoIn"])
            ).optional(),
            "paygateInfo": t.proxy(renames["PaygateInfoIn"]).optional(),
            "availableAccessTypes": t.array(t.string()).optional(),
            "viewerCount": t.integer().optional(),
            "broadcastSessionInfo": t.proxy(
                renames["BroadcastSessionInfoIn"]
            ).optional(),
            "presenter": t.proxy(renames["PresenterIn"]).optional(),
            "settings": t.proxy(renames["CallSettingsIn"]).optional(),
            "transcriptionSessionInfo": t.proxy(
                renames["TranscriptionSessionInfoIn"]
            ).optional(),
            "recordingSessionInfo": t.proxy(
                renames["RecordingSessionInfoIn"]
            ).optional(),
            "cseInfo": t.proxy(renames["CseInfoIn"]).optional(),
            "recordingInfo": t.proxy(renames["RecordingInfoIn"]).optional(),
            "coActivity": t.proxy(renames["CoActivityIn"]).optional(),
        }
    ).named(renames["CallInfoIn"])
    types["CallInfoOut"] = t.struct(
        {
            "abuseReportingConfig": t.proxy(
                renames["AbuseReportingConfigOut"]
            ).optional(),
            "availableReactions": t.array(
                t.proxy(renames["ReactionInfoOut"])
            ).optional(),
            "collaboration": t.proxy(renames["CollaborationOut"]).optional(),
            "artifactOwner": t.proxy(renames["UserDisplayInfoOut"]).optional(),
            "youTubeBroadcastSessionInfos": t.array(
                t.proxy(renames["YouTubeBroadcastSessionInfoOut"])
            ).optional(),
            "streamingSessions": t.array(
                t.proxy(renames["StreamingSessionInfoOut"])
            ).optional(),
            "paygateInfo": t.proxy(renames["PaygateInfoOut"]).optional(),
            "availableAccessTypes": t.array(t.string()).optional(),
            "viewerCount": t.integer().optional(),
            "attachedDocuments": t.array(
                t.proxy(renames["DocumentInfoOut"])
            ).optional(),
            "broadcastSessionInfo": t.proxy(
                renames["BroadcastSessionInfoOut"]
            ).optional(),
            "presenter": t.proxy(renames["PresenterOut"]).optional(),
            "settings": t.proxy(renames["CallSettingsOut"]).optional(),
            "transcriptionSessionInfo": t.proxy(
                renames["TranscriptionSessionInfoOut"]
            ).optional(),
            "recordingSessionInfo": t.proxy(
                renames["RecordingSessionInfoOut"]
            ).optional(),
            "cseInfo": t.proxy(renames["CseInfoOut"]).optional(),
            "recordingInfo": t.proxy(renames["RecordingInfoOut"]).optional(),
            "organizationName": t.string().optional(),
            "coActivity": t.proxy(renames["CoActivityOut"]).optional(),
            "calendarEventId": t.string().optional(),
            "maxJoinedDevices": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CallInfoOut"])
    types["RbacRoleProtoIn"] = t.struct(
        {
            "objectId": t.string(),
            "rbacRoleName": t.string().optional(),
            "rbacNamespace": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["RbacRoleProtoIn"])
    types["RbacRoleProtoOut"] = t.struct(
        {
            "objectId": t.string(),
            "rbacRoleName": t.string().optional(),
            "rbacNamespace": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RbacRoleProtoOut"])
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
    types["RosterIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["RosterIdIn"]
    )
    types["RosterIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RosterIdOut"])
    types["GoogleChatV1WidgetMarkupImageIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "aspectRatio": t.number().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageIn"])
    types["GoogleChatV1WidgetMarkupImageOut"] = t.struct(
        {
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "aspectRatio": t.number().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageOut"])
    types["CustomEmojiMetadataIn"] = t.struct(
        {"customEmoji": t.proxy(renames["AppsDynamiteSharedCustomEmojiIn"])}
    ).named(renames["CustomEmojiMetadataIn"])
    types["CustomEmojiMetadataOut"] = t.struct(
        {
            "customEmoji": t.proxy(renames["AppsDynamiteSharedCustomEmojiOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomEmojiMetadataOut"])
    types["RecordingInfoIn"] = t.struct(
        {
            "recordingStatus": t.string().optional(),
            "latestRecordingEvent": t.proxy(renames["RecordingEventIn"]).optional(),
            "recordingApplicationType": t.string().optional(),
            "recordingId": t.string().optional(),
            "ownerDisplayName": t.string().optional(),
            "producerDeviceId": t.string().optional(),
        }
    ).named(renames["RecordingInfoIn"])
    types["RecordingInfoOut"] = t.struct(
        {
            "recordingStatus": t.string().optional(),
            "latestRecordingEvent": t.proxy(renames["RecordingEventOut"]).optional(),
            "recordingApplicationType": t.string().optional(),
            "recordingId": t.string().optional(),
            "ownerDisplayName": t.string().optional(),
            "producerDeviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordingInfoOut"])
    types["AppsDynamiteSharedContentReportTypeIn"] = t.struct(
        {"systemViolation": t.string()}
    ).named(renames["AppsDynamiteSharedContentReportTypeIn"])
    types["AppsDynamiteSharedContentReportTypeOut"] = t.struct(
        {
            "systemViolation": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedContentReportTypeOut"])
    types["AppsDynamiteSharedChatItemIn"] = t.struct(
        {
            "messageInfo": t.proxy(
                renames["AppsDynamiteSharedMessageInfoIn"]
            ).optional(),
            "groupInfo": t.proxy(
                renames["AppsDynamiteSharedChatItemGroupInfoIn"]
            ).optional(),
            "activityInfo": t.array(
                t.proxy(renames["AppsDynamiteSharedChatItemActivityInfoIn"])
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemIn"])
    types["AppsDynamiteSharedChatItemOut"] = t.struct(
        {
            "messageInfo": t.proxy(
                renames["AppsDynamiteSharedMessageInfoOut"]
            ).optional(),
            "groupInfo": t.proxy(
                renames["AppsDynamiteSharedChatItemGroupInfoOut"]
            ).optional(),
            "activityInfo": t.array(
                t.proxy(renames["AppsDynamiteSharedChatItemActivityInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemOut"])
    types["GaiaGroupProtoIn"] = t.struct({"groupId": t.string()}).named(
        renames["GaiaGroupProtoIn"]
    )
    types["GaiaGroupProtoOut"] = t.struct(
        {"groupId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GaiaGroupProtoOut"])
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
    types["GetSearchApplicationSessionStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["SearchApplicationSessionStatsIn"]))}
    ).named(renames["GetSearchApplicationSessionStatsResponseIn"])
    types["GetSearchApplicationSessionStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["SearchApplicationSessionStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationSessionStatsResponseOut"])
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
    types["AttachmentIn"] = t.struct(
        {
            "slackDataImageUrlHeight": t.integer().optional(),
            "attachmentId": t.string().optional(),
            "appId": t.proxy(renames["UserIdIn"]).optional(),
            "slackData": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1AttachmentIn"]
            ).optional(),
            "deprecatedAddOnData": t.proxy(
                renames["ContextualAddOnMarkupIn"]
            ).optional(),
            "cardAddOnData": t.proxy(renames["AppsDynamiteStorageCardIn"]).optional(),
            "addOnData": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupIn"]
            ).optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "slackDataImageUrlHeight": t.integer().optional(),
            "attachmentId": t.string().optional(),
            "appId": t.proxy(renames["UserIdOut"]).optional(),
            "slackData": t.proxy(
                renames["AppsDynamiteV1ApiCompatV1AttachmentOut"]
            ).optional(),
            "deprecatedAddOnData": t.proxy(
                renames["ContextualAddOnMarkupOut"]
            ).optional(),
            "cardAddOnData": t.proxy(renames["AppsDynamiteStorageCardOut"]).optional(),
            "addOnData": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["MetalineIn"] = t.struct(
        {"properties": t.array(t.proxy(renames["DisplayedPropertyIn"])).optional()}
    ).named(renames["MetalineIn"])
    types["MetalineOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["DisplayedPropertyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetalineOut"])
    types["AppsDynamiteStorageImageIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageImageIn"])
    types["AppsDynamiteStorageImageOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageOut"])
    types["ChatClientActionMarkupIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ChatClientActionMarkupIn"]
    )
    types["ChatClientActionMarkupOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatClientActionMarkupOut"])
    types["AppsDynamiteSharedAssistantSessionContextIn"] = t.struct(
        {"contextualSessionId": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantSessionContextIn"])
    types["AppsDynamiteSharedAssistantSessionContextOut"] = t.struct(
        {
            "contextualSessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSessionContextOut"])
    types["AppsDynamiteStorageImageCropStyleIn"] = t.struct(
        {"aspectRatio": t.number().optional(), "type": t.string().optional()}
    ).named(renames["AppsDynamiteStorageImageCropStyleIn"])
    types["AppsDynamiteStorageImageCropStyleOut"] = t.struct(
        {
            "aspectRatio": t.number().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageCropStyleOut"])
    types["AnnotationIn"] = t.struct(
        {
            "componentSearchInfo": t.proxy(
                renames["AppsDynamiteSharedMessageComponentSearchInfoIn"]
            ).optional(),
            "customEmojiMetadata": t.proxy(renames["CustomEmojiMetadataIn"]),
            "cardCapabilityMetadata": t.proxy(
                renames["CardCapabilityMetadataIn"]
            ).optional(),
            "localId": t.string().optional(),
            "babelPlaceholderMetadata": t.proxy(renames["BabelPlaceholderMetadataIn"]),
            "userMentionMetadata": t.proxy(renames["UserMentionMetadataIn"]).optional(),
            "startIndex": t.integer().optional(),
            "consentedAppUnfurlMetadata": t.proxy(
                renames["ConsentedAppUnfurlMetadataIn"]
            ),
            "roomUpdated": t.proxy(renames["RoomUpdatedMetadataIn"]),
            "gsuiteIntegrationMetadata": t.proxy(
                renames["GsuiteIntegrationMetadataIn"]
            ).optional(),
            "youtubeMetadata": t.proxy(renames["YoutubeMetadataIn"]),
            "driveMetadata": t.proxy(renames["DriveMetadataIn"]).optional(),
            "length": t.integer().optional(),
            "serverInvalidated": t.boolean().optional(),
            "incomingWebhookChangedMetadata": t.proxy(
                renames["IncomingWebhookChangedMetadataIn"]
            ),
            "integrationConfigUpdated": t.proxy(
                renames["IntegrationConfigUpdatedMetadataIn"]
            ).optional(),
            "uploadMetadata": t.proxy(renames["UploadMetadataIn"]),
            "formatMetadata": t.proxy(renames["FormatMetadataIn"]),
            "chipRenderType": t.string().optional(),
            "interactionData": t.proxy(renames["InteractionDataIn"]).optional(),
            "videoCallMetadata": t.proxy(renames["VideoCallMetadataIn"]),
            "urlMetadata": t.proxy(renames["UrlMetadataIn"]),
            "readReceiptsSettingsMetadata": t.proxy(
                renames["ReadReceiptsSettingsUpdatedMetadataIn"]
            ),
            "uniqueId": t.string().optional(),
            "membershipChanged": t.proxy(
                renames["MembershipChangedMetadataIn"]
            ).optional(),
            "type": t.string().optional(),
            "inlineRenderFormat": t.string().optional(),
            "requiredMessageFeaturesMetadata": t.proxy(
                renames["RequiredMessageFeaturesMetadataIn"]
            ).optional(),
            "slashCommandMetadata": t.proxy(renames["SlashCommandMetadataIn"]),
            "dataLossPreventionMetadata": t.proxy(
                renames["DataLossPreventionMetadataIn"]
            ),
            "groupRetentionSettingsUpdated": t.proxy(
                renames["GroupRetentionSettingsUpdatedMetaDataIn"]
            ),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "componentSearchInfo": t.proxy(
                renames["AppsDynamiteSharedMessageComponentSearchInfoOut"]
            ).optional(),
            "customEmojiMetadata": t.proxy(renames["CustomEmojiMetadataOut"]),
            "cardCapabilityMetadata": t.proxy(
                renames["CardCapabilityMetadataOut"]
            ).optional(),
            "localId": t.string().optional(),
            "babelPlaceholderMetadata": t.proxy(renames["BabelPlaceholderMetadataOut"]),
            "userMentionMetadata": t.proxy(
                renames["UserMentionMetadataOut"]
            ).optional(),
            "startIndex": t.integer().optional(),
            "consentedAppUnfurlMetadata": t.proxy(
                renames["ConsentedAppUnfurlMetadataOut"]
            ),
            "roomUpdated": t.proxy(renames["RoomUpdatedMetadataOut"]),
            "gsuiteIntegrationMetadata": t.proxy(
                renames["GsuiteIntegrationMetadataOut"]
            ).optional(),
            "youtubeMetadata": t.proxy(renames["YoutubeMetadataOut"]),
            "driveMetadata": t.proxy(renames["DriveMetadataOut"]).optional(),
            "length": t.integer().optional(),
            "serverInvalidated": t.boolean().optional(),
            "incomingWebhookChangedMetadata": t.proxy(
                renames["IncomingWebhookChangedMetadataOut"]
            ),
            "integrationConfigUpdated": t.proxy(
                renames["IntegrationConfigUpdatedMetadataOut"]
            ).optional(),
            "uploadMetadata": t.proxy(renames["UploadMetadataOut"]),
            "formatMetadata": t.proxy(renames["FormatMetadataOut"]),
            "chipRenderType": t.string().optional(),
            "interactionData": t.proxy(renames["InteractionDataOut"]).optional(),
            "videoCallMetadata": t.proxy(renames["VideoCallMetadataOut"]),
            "urlMetadata": t.proxy(renames["UrlMetadataOut"]),
            "readReceiptsSettingsMetadata": t.proxy(
                renames["ReadReceiptsSettingsUpdatedMetadataOut"]
            ),
            "uniqueId": t.string().optional(),
            "membershipChanged": t.proxy(
                renames["MembershipChangedMetadataOut"]
            ).optional(),
            "type": t.string().optional(),
            "inlineRenderFormat": t.string().optional(),
            "requiredMessageFeaturesMetadata": t.proxy(
                renames["RequiredMessageFeaturesMetadataOut"]
            ).optional(),
            "slashCommandMetadata": t.proxy(renames["SlashCommandMetadataOut"]),
            "dataLossPreventionMetadata": t.proxy(
                renames["DataLossPreventionMetadataOut"]
            ),
            "groupRetentionSettingsUpdated": t.proxy(
                renames["GroupRetentionSettingsUpdatedMetaDataOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["DynamiteMessagesScoringInfoIn"] = t.struct(
        {
            "creatorInSearcherContactList": t.boolean(),
            "lastReadTimestampAgeInDays": t.number(),
            "dasContactCount": t.string(),
            "creatorGaiaId": t.string(),
            "topicalityScore": t.number(),
            "freshnessScore": t.number(),
            "crowdingMultiplier": t.number(),
            "commonContactCount": t.string(),
            "commonCountToContactListCountRatio": t.number(),
            "messageAgeInDays": t.number(),
            "messageSenderAffinityScore": t.number(),
            "unjoinedSpaceAffinityScore": t.number(),
            "commonCountToMembershipCountRatio": t.number(),
            "spaceMembershipCount": t.string(),
            "spaceId": t.string(),
            "joinedSpaceAffinityScore": t.number(),
            "finalScore": t.number(),
        }
    ).named(renames["DynamiteMessagesScoringInfoIn"])
    types["DynamiteMessagesScoringInfoOut"] = t.struct(
        {
            "creatorInSearcherContactList": t.boolean(),
            "lastReadTimestampAgeInDays": t.number(),
            "dasContactCount": t.string(),
            "creatorGaiaId": t.string(),
            "topicalityScore": t.number(),
            "freshnessScore": t.number(),
            "crowdingMultiplier": t.number(),
            "commonContactCount": t.string(),
            "commonCountToContactListCountRatio": t.number(),
            "messageAgeInDays": t.number(),
            "messageSenderAffinityScore": t.number(),
            "unjoinedSpaceAffinityScore": t.number(),
            "commonCountToMembershipCountRatio": t.number(),
            "spaceMembershipCount": t.string(),
            "spaceId": t.string(),
            "joinedSpaceAffinityScore": t.number(),
            "finalScore": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamiteMessagesScoringInfoOut"])
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
    types["TextParagraphIn"] = t.struct({"text": t.string()}).named(
        renames["TextParagraphIn"]
    )
    types["TextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextParagraphOut"])
    types["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"])
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
    types["AppsDynamiteStorageCardCardHeaderIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "imageAltText": t.string().optional(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "imageType": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageCardCardHeaderIn"])
    types["AppsDynamiteStorageCardCardHeaderOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "imageAltText": t.string().optional(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "imageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardCardHeaderOut"])
    types["RequestFileScopeIn"] = t.struct({"itemId": t.string()}).named(
        renames["RequestFileScopeIn"]
    )
    types["RequestFileScopeOut"] = t.struct(
        {"itemId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestFileScopeOut"])
    types["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"])
    types["AppIdIn"] = t.struct(
        {
            "appType": t.string().optional(),
            "id": t.string().optional(),
            "gsuiteAppType": t.string().optional(),
        }
    ).named(renames["AppIdIn"])
    types["AppIdOut"] = t.struct(
        {
            "appType": t.string().optional(),
            "id": t.string().optional(),
            "gsuiteAppType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppIdOut"])
    types["DeleteMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteMetadataIn"]
    )
    types["DeleteMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteMetadataOut"])
    types["AppsDynamiteStorageDateTimePickerIn"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageDateTimePickerIn"])
    types["AppsDynamiteStorageDateTimePickerOut"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDateTimePickerOut"])
    types["GetCustomerQueryStatsResponseIn"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerQueryStatsIn"])),
            "totalQueryCount": t.string().optional(),
        }
    ).named(renames["GetCustomerQueryStatsResponseIn"])
    types["GetCustomerQueryStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerQueryStatsOut"])),
            "totalQueryCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerQueryStatsResponseOut"])
    types["MessageAddedIn"] = t.struct(
        {
            "messageKey": t.proxy(renames["MultiKeyIn"]),
            "attributeIds": t.array(t.string()),
            "labelIds": t.array(t.string()),
            "syncIds": t.array(t.integer()).optional(),
        }
    ).named(renames["MessageAddedIn"])
    types["MessageAddedOut"] = t.struct(
        {
            "messageKey": t.proxy(renames["MultiKeyOut"]),
            "attributeIds": t.array(t.string()),
            "labelIds": t.array(t.string()),
            "syncIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageAddedOut"])
    types["MessageAttributesIn"] = t.struct(
        {"isTombstone": t.boolean().optional()}
    ).named(renames["MessageAttributesIn"])
    types["MessageAttributesOut"] = t.struct(
        {
            "isTombstone": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageAttributesOut"])
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
    types["WonderMessageMappingIn"] = t.struct(
        {"wonderCardMessageId": t.array(t.string()).optional()}
    ).named(renames["WonderMessageMappingIn"])
    types["WonderMessageMappingOut"] = t.struct(
        {
            "wonderCardMessageId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WonderMessageMappingOut"])
    types["KeyValueIn"] = t.struct(
        {
            "startIcon": t.proxy(renames["IconImageIn"]).optional(),
            "iconUrl": t.string(),
            "icon": t.string(),
            "switchWidget": t.proxy(renames["SwitchWidgetIn"]),
            "contentMultiline": t.boolean(),
            "button": t.proxy(renames["ButtonIn"]),
            "imageStyle": t.string(),
            "iconAltText": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "endIcon": t.proxy(renames["IconImageIn"]),
            "topLabel": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "startIcon": t.proxy(renames["IconImageOut"]).optional(),
            "iconUrl": t.string(),
            "icon": t.string(),
            "switchWidget": t.proxy(renames["SwitchWidgetOut"]),
            "contentMultiline": t.boolean(),
            "button": t.proxy(renames["ButtonOut"]),
            "imageStyle": t.string(),
            "iconAltText": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "endIcon": t.proxy(renames["IconImageOut"]),
            "topLabel": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
    types["IncomingWebhookChangedMetadataIn"] = t.struct(
        {
            "incomingWebhookName": t.string().optional(),
            "initiatorId": t.proxy(renames["UserIdIn"]).optional(),
            "oldIncomingWebhookName": t.string().optional(),
            "initiatorProfile": t.proxy(renames["UserIn"]).optional(),
            "obfuscatedIncomingWebhookId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["IncomingWebhookChangedMetadataIn"])
    types["IncomingWebhookChangedMetadataOut"] = t.struct(
        {
            "incomingWebhookName": t.string().optional(),
            "initiatorId": t.proxy(renames["UserIdOut"]).optional(),
            "oldIncomingWebhookName": t.string().optional(),
            "initiatorProfile": t.proxy(renames["UserOut"]).optional(),
            "obfuscatedIncomingWebhookId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncomingWebhookChangedMetadataOut"])
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
    types["ObjectValuesIn"] = t.struct(
        {"values": t.array(t.proxy(renames["StructuredDataObjectIn"]))}
    ).named(renames["ObjectValuesIn"])
    types["ObjectValuesOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["StructuredDataObjectOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectValuesOut"])
    types["DriveTimeSpanRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveTimeSpanRestrictIn"]
    )
    types["DriveTimeSpanRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveTimeSpanRestrictOut"])
    types["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"])
    types["MessageInfoIn"] = t.struct(
        {
            "authorUserType": t.string().optional(),
            "searcherMembershipState": t.string().optional(),
            "message": t.proxy(renames["MessageIn"]).optional(),
        }
    ).named(renames["MessageInfoIn"])
    types["MessageInfoOut"] = t.struct(
        {
            "authorUserType": t.string().optional(),
            "searcherMembershipState": t.string().optional(),
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageInfoOut"])
    types["TextKeyValueIn"] = t.struct(
        {
            "text": t.string(),
            "key": t.string(),
            "onClick": t.proxy(renames["OnClickIn"]),
        }
    ).named(renames["TextKeyValueIn"])
    types["TextKeyValueOut"] = t.struct(
        {
            "text": t.string(),
            "key": t.string(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextKeyValueOut"])
    types["ChatContentExtensionIn"] = t.struct(
        {
            "membershipChangeEvent": t.proxy(
                renames["MembershipChangeEventIn"]
            ).optional(),
            "eventOtrStatus": t.string().optional(),
            "hangoutEvent": t.proxy(renames["HangoutEventIn"]).optional(),
            "otrModificationEvent": t.proxy(renames["OtrModificationEventIn"]),
            "inviteAcceptedEvent": t.proxy(renames["InviteAcceptedEventIn"]).optional(),
            "annotation": t.array(t.proxy(renames["EventAnnotationIn"])).optional(),
            "otrChatMessageEvent": t.proxy(renames["OtrChatMessageEventIn"]).optional(),
            "renameEvent": t.proxy(renames["RenameEventIn"]),
            "dynamitePlaceholderMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataIn"]
            ).optional(),
            "groupLinkSharingModificationEvent": t.proxy(
                renames["GroupLinkSharingModificationEventIn"]
            ).optional(),
        }
    ).named(renames["ChatContentExtensionIn"])
    types["ChatContentExtensionOut"] = t.struct(
        {
            "membershipChangeEvent": t.proxy(
                renames["MembershipChangeEventOut"]
            ).optional(),
            "eventOtrStatus": t.string().optional(),
            "hangoutEvent": t.proxy(renames["HangoutEventOut"]).optional(),
            "otrModificationEvent": t.proxy(renames["OtrModificationEventOut"]),
            "inviteAcceptedEvent": t.proxy(
                renames["InviteAcceptedEventOut"]
            ).optional(),
            "annotation": t.array(t.proxy(renames["EventAnnotationOut"])).optional(),
            "otrChatMessageEvent": t.proxy(
                renames["OtrChatMessageEventOut"]
            ).optional(),
            "renameEvent": t.proxy(renames["RenameEventOut"]),
            "dynamitePlaceholderMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataOut"]
            ).optional(),
            "groupLinkSharingModificationEvent": t.proxy(
                renames["GroupLinkSharingModificationEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatContentExtensionOut"])
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
    types["CustomerIndexStatsIn"] = t.struct(
        {
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusIn"])
            ).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["CustomerIndexStatsIn"])
    types["CustomerIndexStatsOut"] = t.struct(
        {
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusOut"])
            ).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerIndexStatsOut"])
    types["ObjectDefinitionIn"] = t.struct(
        {
            "options": t.proxy(renames["ObjectOptionsIn"]).optional(),
            "propertyDefinitions": t.array(
                t.proxy(renames["PropertyDefinitionIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ObjectDefinitionIn"])
    types["ObjectDefinitionOut"] = t.struct(
        {
            "options": t.proxy(renames["ObjectOptionsOut"]).optional(),
            "propertyDefinitions": t.array(
                t.proxy(renames["PropertyDefinitionOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectDefinitionOut"])
    types["ShareScopeIn"] = t.struct(
        {"scope": t.string().optional(), "domain": t.string().optional()}
    ).named(renames["ShareScopeIn"])
    types["ShareScopeOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShareScopeOut"])
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
    types["AppsDynamiteStorageSelectionInputIn"] = t.struct(
        {
            "label": t.string().optional(),
            "type": t.string(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageSelectionInputSelectionItemIn"])
            ),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputIn"])
    types["AppsDynamiteStorageSelectionInputOut"] = t.struct(
        {
            "label": t.string().optional(),
            "type": t.string(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageSelectionInputSelectionItemOut"])
            ),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputOut"])
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
    types["AclFixStatusIn"] = t.struct(
        {
            "outOfDomainWarningEmailAddress": t.array(t.string()).optional(),
            "fixableEmailAddress": t.array(t.string()).optional(),
            "fixability": t.string(),
        }
    ).named(renames["AclFixStatusIn"])
    types["AclFixStatusOut"] = t.struct(
        {
            "outOfDomainWarningEmailAddress": t.array(t.string()).optional(),
            "fixableEmailAddress": t.array(t.string()).optional(),
            "fixability": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclFixStatusOut"])
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
    types["GoogleChatV1ContextualAddOnMarkupCardIn"] = t.struct(
        {
            "sections": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardSectionIn"])
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardCardActionIn"])
            ).optional(),
            "name": t.string().optional(),
            "header": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderIn"]
            ).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardIn"])
    types["GoogleChatV1ContextualAddOnMarkupCardOut"] = t.struct(
        {
            "sections": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardSectionOut"])
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupCardCardActionOut"])
            ).optional(),
            "name": t.string().optional(),
            "header": t.proxy(
                renames["GoogleChatV1ContextualAddOnMarkupCardCardHeaderOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1ContextualAddOnMarkupCardOut"])
    types["QuerySourceIn"] = t.struct(
        {
            "shortName": t.string().optional(),
            "operators": t.array(t.proxy(renames["QueryOperatorIn"])).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["QuerySourceIn"])
    types["QuerySourceOut"] = t.struct(
        {
            "shortName": t.string().optional(),
            "operators": t.array(t.proxy(renames["QueryOperatorOut"])).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuerySourceOut"])
    types["DebugOptionsIn"] = t.struct(
        {"enableDebugging": t.boolean().optional()}
    ).named(renames["DebugOptionsIn"])
    types["DebugOptionsOut"] = t.struct(
        {
            "enableDebugging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugOptionsOut"])
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
    types["PrincipalProtoIn"] = t.struct(
        {
            "emailOwner": t.proxy(renames["EmailOwnerProtoIn"]).optional(),
            "contactGroup": t.proxy(renames["ContactGroupProtoIn"]).optional(),
            "circle": t.proxy(renames["CircleProtoIn"]).optional(),
            "simpleSecretHolder": t.proxy(
                renames["SimpleSecretHolderProtoIn"]
            ).optional(),
            "capTokenHolder": t.proxy(renames["CapTokenHolderProtoIn"]).optional(),
            "rbacRole": t.proxy(renames["RbacRoleProtoIn"]).optional(),
            "signingKeyPossessor": t.proxy(
                renames["SigningKeyPossessorProtoIn"]
            ).optional(),
            "allAuthenticatedUsers": t.proxy(
                renames["AllAuthenticatedUsersProtoIn"]
            ).optional(),
            "resourceRole": t.proxy(renames["ResourceRoleProtoIn"]).optional(),
            "gaiaGroup": t.proxy(renames["GaiaGroupProtoIn"]).optional(),
            "cloudPrincipal": t.proxy(renames["CloudPrincipalProtoIn"]).optional(),
            "mdbGroup": t.proxy(renames["MdbGroupProtoIn"]).optional(),
            "postiniUser": t.proxy(renames["PostiniUserProtoIn"]).optional(),
            "mdbUser": t.proxy(renames["MdbUserProtoIn"]).optional(),
            "scope": t.string().optional(),
            "host": t.proxy(renames["HostProtoIn"]).optional(),
            "socialGraphNode": t.proxy(renames["SocialGraphNodeProtoIn"]).optional(),
            "rbacSubject": t.proxy(renames["RbacSubjectProtoIn"]).optional(),
            "youtubeUser": t.proxy(renames["YoutubeUserProtoIn"]).optional(),
            "chat": t.proxy(renames["ChatProtoIn"]).optional(),
            "ldapGroup": t.proxy(renames["LdapGroupProtoIn"]).optional(),
            "gaiaUser": t.proxy(renames["GaiaUserProtoIn"]).optional(),
            "event": t.proxy(renames["EventProtoIn"]).optional(),
            "oauthConsumer": t.proxy(renames["OAuthConsumerProtoIn"]).optional(),
            "zwiebackSession": t.proxy(renames["ZwiebackSessionProtoIn"]).optional(),
            "ldapUser": t.proxy(renames["LdapUserProtoIn"]).optional(),
            "square": t.proxy(renames["SquareProtoIn"]).optional(),
        }
    ).named(renames["PrincipalProtoIn"])
    types["PrincipalProtoOut"] = t.struct(
        {
            "emailOwner": t.proxy(renames["EmailOwnerProtoOut"]).optional(),
            "contactGroup": t.proxy(renames["ContactGroupProtoOut"]).optional(),
            "circle": t.proxy(renames["CircleProtoOut"]).optional(),
            "simpleSecretHolder": t.proxy(
                renames["SimpleSecretHolderProtoOut"]
            ).optional(),
            "capTokenHolder": t.proxy(renames["CapTokenHolderProtoOut"]).optional(),
            "rbacRole": t.proxy(renames["RbacRoleProtoOut"]).optional(),
            "signingKeyPossessor": t.proxy(
                renames["SigningKeyPossessorProtoOut"]
            ).optional(),
            "allAuthenticatedUsers": t.proxy(
                renames["AllAuthenticatedUsersProtoOut"]
            ).optional(),
            "resourceRole": t.proxy(renames["ResourceRoleProtoOut"]).optional(),
            "gaiaGroup": t.proxy(renames["GaiaGroupProtoOut"]).optional(),
            "cloudPrincipal": t.proxy(renames["CloudPrincipalProtoOut"]).optional(),
            "mdbGroup": t.proxy(renames["MdbGroupProtoOut"]).optional(),
            "postiniUser": t.proxy(renames["PostiniUserProtoOut"]).optional(),
            "mdbUser": t.proxy(renames["MdbUserProtoOut"]).optional(),
            "scope": t.string().optional(),
            "host": t.proxy(renames["HostProtoOut"]).optional(),
            "socialGraphNode": t.proxy(renames["SocialGraphNodeProtoOut"]).optional(),
            "rbacSubject": t.proxy(renames["RbacSubjectProtoOut"]).optional(),
            "youtubeUser": t.proxy(renames["YoutubeUserProtoOut"]).optional(),
            "chat": t.proxy(renames["ChatProtoOut"]).optional(),
            "ldapGroup": t.proxy(renames["LdapGroupProtoOut"]).optional(),
            "gaiaUser": t.proxy(renames["GaiaUserProtoOut"]).optional(),
            "event": t.proxy(renames["EventProtoOut"]).optional(),
            "oauthConsumer": t.proxy(renames["OAuthConsumerProtoOut"]).optional(),
            "zwiebackSession": t.proxy(renames["ZwiebackSessionProtoOut"]).optional(),
            "ldapUser": t.proxy(renames["LdapUserProtoOut"]).optional(),
            "square": t.proxy(renames["SquareProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrincipalProtoOut"])
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
    types["MenuItemIn"] = t.struct(
        {
            "value": t.string().optional(),
            "text": t.string().optional(),
            "selected": t.boolean(),
        }
    ).named(renames["MenuItemIn"])
    types["MenuItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "text": t.string().optional(),
            "selected": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MenuItemOut"])
    types["UpdateBccRecipientsIn"] = t.struct(
        {"bccRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateBccRecipientsIn"])
    types["UpdateBccRecipientsOut"] = t.struct(
        {
            "bccRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBccRecipientsOut"])
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
    types["AppsDynamiteSharedMessageInfoIn"] = t.struct(
        {
            "messageId": t.proxy(renames["MessageIdIn"]).optional(),
            "topicReadTimeUsec": t.string().optional(),
            "messageType": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageInfoIn"])
    types["AppsDynamiteSharedMessageInfoOut"] = t.struct(
        {
            "messageId": t.proxy(renames["MessageIdOut"]).optional(),
            "topicReadTimeUsec": t.string().optional(),
            "messageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageInfoOut"])
    types["TimestampValuesIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["TimestampValuesIn"]
    )
    types["TimestampValuesOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampValuesOut"])
    types["StreamingSessionInfoIn"] = t.struct(
        {
            "status": t.string().optional(),
            "sessionId": t.string().optional(),
            "latestSessionEvent": t.proxy(renames["SessionEventIn"]).optional(),
            "viewerStats": t.proxy(renames["StreamViewerStatsIn"]).optional(),
            "viewerAccessPolicy": t.string().optional(),
            "applicationType": t.string().optional(),
            "trainingEnabled": t.boolean().optional(),
            "ownerDisplayName": t.string().optional(),
        }
    ).named(renames["StreamingSessionInfoIn"])
    types["StreamingSessionInfoOut"] = t.struct(
        {
            "status": t.string().optional(),
            "sessionId": t.string().optional(),
            "latestSessionEvent": t.proxy(renames["SessionEventOut"]).optional(),
            "viewerStats": t.proxy(renames["StreamViewerStatsOut"]).optional(),
            "viewerAccessPolicy": t.string().optional(),
            "applicationType": t.string().optional(),
            "trainingEnabled": t.boolean().optional(),
            "ownerDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSessionInfoOut"])
    types["GoogleDocsResultInfoIn"] = t.struct(
        {
            "attachmentSha1": t.string().optional(),
            "cosmoNameSpace": t.integer().optional(),
            "mimeType": t.string().optional(),
            "cosmoId": t.proxy(renames["IdIn"]).optional(),
            "shareScope": t.proxy(renames["ShareScopeIn"]).optional(),
            "encryptedId": t.string().optional(),
        }
    ).named(renames["GoogleDocsResultInfoIn"])
    types["GoogleDocsResultInfoOut"] = t.struct(
        {
            "attachmentSha1": t.string().optional(),
            "cosmoNameSpace": t.integer().optional(),
            "mimeType": t.string().optional(),
            "cosmoId": t.proxy(renames["IdOut"]).optional(),
            "shareScope": t.proxy(renames["ShareScopeOut"]).optional(),
            "encryptedId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDocsResultInfoOut"])
    types["RbacSubjectProtoIn"] = t.struct({"username": t.string().optional()}).named(
        renames["RbacSubjectProtoIn"]
    )
    types["RbacSubjectProtoOut"] = t.struct(
        {
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RbacSubjectProtoOut"])
    types["VoicePhoneNumberI18nDataIn"] = t.struct(
        {
            "isValid": t.boolean().optional(),
            "regionCode": t.string().optional(),
            "nationalNumber": t.string().optional(),
            "validationResult": t.string().optional(),
            "countryCode": t.integer().optional(),
            "internationalNumber": t.string().optional(),
        }
    ).named(renames["VoicePhoneNumberI18nDataIn"])
    types["VoicePhoneNumberI18nDataOut"] = t.struct(
        {
            "isValid": t.boolean().optional(),
            "regionCode": t.string().optional(),
            "nationalNumber": t.string().optional(),
            "validationResult": t.string().optional(),
            "countryCode": t.integer().optional(),
            "internationalNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoicePhoneNumberI18nDataOut"])
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
    types["UpdateSchemaRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "schema": t.proxy(renames["SchemaIn"]).optional(),
        }
    ).named(renames["UpdateSchemaRequestIn"])
    types["UpdateSchemaRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "schema": t.proxy(renames["SchemaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSchemaRequestOut"])
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
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn"
    ] = t.struct(
        {
            "conferenceSolutionId": t.string().optional(),
            "error": t.proxy(
                renames[
                    "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupErrorIn"
                ]
            ).optional(),
            "parameters": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterIn"
                    ]
                )
            ).optional(),
            "note": t.string().optional(),
            "entryPoints": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn"
                    ]
                )
            ).optional(),
            "conferenceId": t.string().optional(),
        }
    ).named(
        renames["AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupIn"]
    )
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut"
    ] = t.struct(
        {
            "conferenceSolutionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "parameters": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupParameterOut"
                    ]
                )
            ).optional(),
            "note": t.string().optional(),
            "entryPoints": t.array(
                t.proxy(
                    renames[
                        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut"
                    ]
                )
            ).optional(),
            "conferenceId": t.string().optional(),
        }
    ).named(
        renames["AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupOut"]
    )
    types["CardIn"] = t.struct(
        {
            "header": t.proxy(renames["CardHeaderIn"]),
            "name": t.string().optional(),
            "cardActions": t.array(t.proxy(renames["CardActionIn"])),
            "peekCardHeader": t.proxy(renames["CardHeaderIn"]).optional(),
            "sections": t.array(t.proxy(renames["SectionIn"])),
            "displayStyle": t.string(),
            "fixedFooter": t.proxy(renames["FixedFooterIn"]),
        }
    ).named(renames["CardIn"])
    types["CardOut"] = t.struct(
        {
            "header": t.proxy(renames["CardHeaderOut"]),
            "name": t.string().optional(),
            "cardActions": t.array(t.proxy(renames["CardActionOut"])),
            "peekCardHeader": t.proxy(renames["CardHeaderOut"]).optional(),
            "sections": t.array(t.proxy(renames["SectionOut"])),
            "displayStyle": t.string(),
            "fixedFooter": t.proxy(renames["FixedFooterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardOut"])
    types["GroupDetailsUpdatedMetadataIn"] = t.struct(
        {
            "prevGroupDetails": t.proxy(renames["AppsDynamiteSharedGroupDetailsIn"]),
            "newGroupDetails": t.proxy(renames["AppsDynamiteSharedGroupDetailsIn"]),
        }
    ).named(renames["GroupDetailsUpdatedMetadataIn"])
    types["GroupDetailsUpdatedMetadataOut"] = t.struct(
        {
            "prevGroupDetails": t.proxy(renames["AppsDynamiteSharedGroupDetailsOut"]),
            "newGroupDetails": t.proxy(renames["AppsDynamiteSharedGroupDetailsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupDetailsUpdatedMetadataOut"])
    types["VPCSettingsIn"] = t.struct({"project": t.string().optional()}).named(
        renames["VPCSettingsIn"]
    )
    types["VPCSettingsOut"] = t.struct(
        {
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VPCSettingsOut"])
    types["AppsDynamiteSharedGroupVisibilityIn"] = t.struct(
        {"state": t.string()}
    ).named(renames["AppsDynamiteSharedGroupVisibilityIn"])
    types["AppsDynamiteSharedGroupVisibilityOut"] = t.struct(
        {"state": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedGroupVisibilityOut"])
    types["AppsDynamiteStorageOpenLinkAppUriIn"] = t.struct(
        {
            "androidIntent": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIntentIn"]
            ).optional(),
            "companionUri": t.string().optional(),
            "iosUri": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriIn"])
    types["AppsDynamiteStorageOpenLinkAppUriOut"] = t.struct(
        {
            "androidIntent": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIntentOut"]
            ).optional(),
            "companionUri": t.string().optional(),
            "iosUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkAppUriOut"])
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
    types["CaribouAttributeValueIn"] = t.struct(
        {
            "rawByteValue": t.string().optional(),
            "intValue": t.integer(),
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string(),
            "longValue": t.string(),
        }
    ).named(renames["CaribouAttributeValueIn"])
    types["CaribouAttributeValueOut"] = t.struct(
        {
            "rawByteValue": t.string().optional(),
            "intValue": t.integer(),
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string(),
            "longValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaribouAttributeValueOut"])
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
    types["IconImageIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "iconUrl": t.string(),
            "icon": t.string(),
            "imageStyle": t.string().optional(),
        }
    ).named(renames["IconImageIn"])
    types["IconImageOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "iconUrl": t.string(),
            "icon": t.string(),
            "imageStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IconImageOut"])
    types["PostiniUserProtoIn"] = t.struct({"postiniUserId": t.string()}).named(
        renames["PostiniUserProtoIn"]
    )
    types["PostiniUserProtoOut"] = t.struct(
        {
            "postiniUserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostiniUserProtoOut"])
    types["ItemContentIn"] = t.struct(
        {
            "hash": t.string().optional(),
            "inlineContent": t.string().optional(),
            "contentDataRef": t.proxy(renames["UploadItemRefIn"]).optional(),
            "contentFormat": t.string(),
        }
    ).named(renames["ItemContentIn"])
    types["ItemContentOut"] = t.struct(
        {
            "hash": t.string().optional(),
            "inlineContent": t.string().optional(),
            "contentDataRef": t.proxy(renames["UploadItemRefOut"]).optional(),
            "contentFormat": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemContentOut"])
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
    types["GridItemIn"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string(),
            "layout": t.string(),
            "identifier": t.string().optional(),
            "image": t.proxy(renames["ImageComponentIn"]),
            "textAlignment": t.string(),
        }
    ).named(renames["GridItemIn"])
    types["GridItemOut"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string(),
            "layout": t.string(),
            "identifier": t.string().optional(),
            "image": t.proxy(renames["ImageComponentOut"]),
            "textAlignment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridItemOut"])
    types["SegmentIn"] = t.struct(
        {
            "text": t.string().optional(),
            "formatting": t.proxy(renames["FormattingIn"]).optional(),
            "hashtagData": t.proxy(renames["HashtagDataIn"]).optional(),
            "type": t.string().optional(),
            "userMentionData": t.proxy(renames["UserMentionDataIn"]).optional(),
            "linkData": t.proxy(renames["LinkDataIn"]).optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "text": t.string().optional(),
            "formatting": t.proxy(renames["FormattingOut"]).optional(),
            "hashtagData": t.proxy(renames["HashtagDataOut"]).optional(),
            "type": t.string().optional(),
            "userMentionData": t.proxy(renames["UserMentionDataOut"]).optional(),
            "linkData": t.proxy(renames["LinkDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
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
    types["LabelDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelDeletedIn"]
    )
    types["LabelDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelDeletedOut"])
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
    types["TopicStateUpdateIn"] = t.struct(
        {"topicState": t.proxy(renames["TopicStateIn"])}
    ).named(renames["TopicStateUpdateIn"])
    types["TopicStateUpdateOut"] = t.struct(
        {
            "topicState": t.proxy(renames["TopicStateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicStateUpdateOut"])
    types["UploadMetadataIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "attachmentToken": t.string().optional(),
            "localId": t.string().optional(),
            "latestVirusScanTimestamp": t.string().optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionIn"]
            ).optional(),
            "clonedDriveAction": t.string().optional(),
            "clonedDriveId": t.string().optional(),
            "virusScanResult": t.string().optional(),
            "clonedAuthorizedItemId": t.proxy(renames["AuthorizedItemIdIn"]).optional(),
            "backendUploadMetadata": t.proxy(
                renames["AppsDynamiteSharedBackendUploadMetadataIn"]
            ).optional(),
            "videoReference": t.proxy(
                renames["AppsDynamiteSharedVideoReferenceIn"]
            ).optional(),
            "contentName": t.string().optional(),
            "dlpMetricsMetadata": t.proxy(
                renames["AppsDynamiteSharedDlpMetricsMetadataIn"]
            ).optional(),
        }
    ).named(renames["UploadMetadataIn"])
    types["UploadMetadataOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "attachmentToken": t.string().optional(),
            "localId": t.string().optional(),
            "latestVirusScanTimestamp": t.string().optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionOut"]
            ).optional(),
            "clonedDriveAction": t.string().optional(),
            "clonedDriveId": t.string().optional(),
            "virusScanResult": t.string().optional(),
            "clonedAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdOut"]
            ).optional(),
            "backendUploadMetadata": t.proxy(
                renames["AppsDynamiteSharedBackendUploadMetadataOut"]
            ).optional(),
            "videoReference": t.proxy(
                renames["AppsDynamiteSharedVideoReferenceOut"]
            ).optional(),
            "contentName": t.string().optional(),
            "dlpMetricsMetadata": t.proxy(
                renames["AppsDynamiteSharedDlpMetricsMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadMetadataOut"])
    types["WidgetMarkupIn"] = t.struct(
        {
            "dateTimePicker": t.proxy(renames["DateTimePickerIn"]),
            "image": t.proxy(renames["ImageIn"]),
            "divider": t.proxy(renames["DividerIn"]),
            "textKeyValue": t.proxy(renames["TextKeyValueIn"]),
            "textParagraph": t.proxy(renames["TextParagraphIn"]).optional(),
            "selectionControl": t.proxy(renames["SelectionControlIn"]),
            "imageKeyValue": t.proxy(renames["ImageKeyValueIn"]),
            "buttons": t.array(t.proxy(renames["ButtonIn"])).optional(),
            "grid": t.proxy(renames["GridIn"]),
            "textField": t.proxy(renames["TextFieldIn"]),
            "horizontalAlignment": t.string().optional(),
            "keyValue": t.proxy(renames["KeyValueIn"]),
            "menu": t.proxy(renames["MenuIn"]).optional(),
        }
    ).named(renames["WidgetMarkupIn"])
    types["WidgetMarkupOut"] = t.struct(
        {
            "dateTimePicker": t.proxy(renames["DateTimePickerOut"]),
            "image": t.proxy(renames["ImageOut"]),
            "divider": t.proxy(renames["DividerOut"]),
            "textKeyValue": t.proxy(renames["TextKeyValueOut"]),
            "textParagraph": t.proxy(renames["TextParagraphOut"]).optional(),
            "selectionControl": t.proxy(renames["SelectionControlOut"]),
            "imageKeyValue": t.proxy(renames["ImageKeyValueOut"]),
            "buttons": t.array(t.proxy(renames["ButtonOut"])).optional(),
            "grid": t.proxy(renames["GridOut"]),
            "textField": t.proxy(renames["TextFieldOut"]),
            "horizontalAlignment": t.string().optional(),
            "keyValue": t.proxy(renames["KeyValueOut"]),
            "menu": t.proxy(renames["MenuOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WidgetMarkupOut"])
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
    types["RequestFileScopeForActiveDocumentIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestFileScopeForActiveDocumentIn"])
    types["RequestFileScopeForActiveDocumentOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestFileScopeForActiveDocumentOut"])
    types["DriveMimeTypeRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveMimeTypeRestrictIn"]
    )
    types["DriveMimeTypeRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveMimeTypeRestrictOut"])
    types["ImageComponentIn"] = t.struct(
        {
            "imageUrl": t.string(),
            "cropStyle": t.proxy(renames["ImageCropStyleIn"]),
            "altText": t.string(),
            "borderStyle": t.proxy(renames["BorderStyleIn"]),
        }
    ).named(renames["ImageComponentIn"])
    types["ImageComponentOut"] = t.struct(
        {
            "imageUrl": t.string(),
            "cropStyle": t.proxy(renames["ImageCropStyleOut"]),
            "altText": t.string(),
            "borderStyle": t.proxy(renames["BorderStyleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageComponentOut"])
    types["AppsDynamiteStorageGridIn"] = t.struct(
        {
            "columnCount": t.integer().optional(),
            "title": t.string().optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageGridGridItemIn"])
            ).optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageGridIn"])
    types["AppsDynamiteStorageGridOut"] = t.struct(
        {
            "columnCount": t.integer().optional(),
            "title": t.string().optional(),
            "items": t.array(
                t.proxy(renames["AppsDynamiteStorageGridGridItemOut"])
            ).optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageGridOut"])
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
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupIn"
    ] = t.struct(
        {
            "regionCode": t.string().optional(),
            "accessCode": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "label": t.string().optional(),
            "meetingCode": t.string().optional(),
            "password": t.string().optional(),
            "pin": t.string().optional(),
            "uri": t.string().optional(),
            "passcode": t.string().optional(),
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
            "accessCode": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "label": t.string().optional(),
            "meetingCode": t.string().optional(),
            "password": t.string().optional(),
            "pin": t.string().optional(),
            "uri": t.string().optional(),
            "passcode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupConferenceDataMarkupEntryPointMarkupOut"
        ]
    )
    types["NamedPropertyIn"] = t.struct(
        {
            "booleanValue": t.boolean(),
            "dateValues": t.proxy(renames["DateValuesIn"]),
            "htmlValues": t.proxy(renames["HtmlValuesIn"]),
            "objectValues": t.proxy(renames["ObjectValuesIn"]),
            "timestampValues": t.proxy(renames["TimestampValuesIn"]),
            "doubleValues": t.proxy(renames["DoubleValuesIn"]),
            "name": t.string().optional(),
            "enumValues": t.proxy(renames["EnumValuesIn"]),
            "integerValues": t.proxy(renames["IntegerValuesIn"]),
            "textValues": t.proxy(renames["TextValuesIn"]),
        }
    ).named(renames["NamedPropertyIn"])
    types["NamedPropertyOut"] = t.struct(
        {
            "booleanValue": t.boolean(),
            "dateValues": t.proxy(renames["DateValuesOut"]),
            "htmlValues": t.proxy(renames["HtmlValuesOut"]),
            "objectValues": t.proxy(renames["ObjectValuesOut"]),
            "timestampValues": t.proxy(renames["TimestampValuesOut"]),
            "doubleValues": t.proxy(renames["DoubleValuesOut"]),
            "name": t.string().optional(),
            "enumValues": t.proxy(renames["EnumValuesOut"]),
            "integerValues": t.proxy(renames["IntegerValuesOut"]),
            "textValues": t.proxy(renames["TextValuesOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedPropertyOut"])
    types["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"] = t.struct(
        {"oldAssignee": t.proxy(renames["UserIdIn"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"] = t.struct(
        {
            "oldAssignee": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"])
    types["SessionContextIn"] = t.struct(
        {
            "oauthLoginId": t.integer().optional(),
            "authTime": t.string().optional(),
            "imapSessionContext": t.proxy(renames["ImapSessionContextIn"]).optional(),
            "delegateUserId": t.string().optional(),
            "dusi": t.string().optional(),
            "oauthProjectId": t.string().optional(),
        }
    ).named(renames["SessionContextIn"])
    types["SessionContextOut"] = t.struct(
        {
            "oauthLoginId": t.integer().optional(),
            "authTime": t.string().optional(),
            "imapSessionContext": t.proxy(renames["ImapSessionContextOut"]).optional(),
            "delegateUserId": t.string().optional(),
            "dusi": t.string().optional(),
            "oauthProjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionContextOut"])
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
    types["RepositoryErrorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "errorMessage": t.string().optional(),
            "httpStatusCode": t.integer().optional(),
        }
    ).named(renames["RepositoryErrorIn"])
    types["RepositoryErrorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "errorMessage": t.string().optional(),
            "httpStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryErrorOut"])
    types["SearchApplicationUserStatsIn"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["SearchApplicationUserStatsIn"])
    types["SearchApplicationUserStatsOut"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationUserStatsOut"])
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
    types["DriveClientActionMarkupIn"] = t.struct(
        {"requestFileScope": t.proxy(renames["RequestFileScopeIn"])}
    ).named(renames["DriveClientActionMarkupIn"])
    types["DriveClientActionMarkupOut"] = t.struct(
        {
            "requestFileScope": t.proxy(renames["RequestFileScopeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveClientActionMarkupOut"])
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
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"] = t.struct(
        {"replyType": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut"] = t.struct(
        {
            "replyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyOut"])
    types["FormattingIn"] = t.struct(
        {
            "bold": t.boolean(),
            "highlight": t.boolean().optional(),
            "italics": t.boolean(),
            "style": t.string().optional(),
            "underline": t.boolean(),
            "strikethrough": t.boolean(),
        }
    ).named(renames["FormattingIn"])
    types["FormattingOut"] = t.struct(
        {
            "bold": t.boolean(),
            "highlight": t.boolean().optional(),
            "italics": t.boolean(),
            "style": t.string().optional(),
            "underline": t.boolean(),
            "strikethrough": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormattingOut"])
    types["MenuIn"] = t.struct(
        {
            "label": t.string().optional(),
            "name": t.string().optional(),
            "items": t.array(t.proxy(renames["MenuItemIn"])),
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
        }
    ).named(renames["MenuIn"])
    types["MenuOut"] = t.struct(
        {
            "label": t.string().optional(),
            "name": t.string().optional(),
            "items": t.array(t.proxy(renames["MenuItemOut"])),
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MenuOut"])
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
    types["AppsDynamiteSharedSpaceInfoIn"] = t.struct(
        {
            "avatarUrl": t.string(),
            "description": t.string(),
            "groupId": t.proxy(renames["GroupIdIn"]),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsIn"]
            ).optional(),
            "inviterEmail": t.string().optional(),
            "userMembershipState": t.string().optional(),
            "avatarInfo": t.proxy(renames["AppsDynamiteSharedAvatarInfoIn"]),
            "name": t.string(),
            "isExternal": t.boolean().optional(),
            "numMembers": t.integer().optional(),
        }
    ).named(renames["AppsDynamiteSharedSpaceInfoIn"])
    types["AppsDynamiteSharedSpaceInfoOut"] = t.struct(
        {
            "avatarUrl": t.string(),
            "description": t.string(),
            "groupId": t.proxy(renames["GroupIdOut"]),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsOut"]
            ).optional(),
            "inviterEmail": t.string().optional(),
            "userMembershipState": t.string().optional(),
            "avatarInfo": t.proxy(renames["AppsDynamiteSharedAvatarInfoOut"]),
            "name": t.string(),
            "isExternal": t.boolean().optional(),
            "numMembers": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedSpaceInfoOut"])
    types["AppsDynamiteStorageMaterialIconIn"] = t.struct(
        {
            "name": t.string().optional(),
            "fill": t.boolean().optional(),
            "grade": t.integer().optional(),
            "weight": t.integer().optional(),
        }
    ).named(renames["AppsDynamiteStorageMaterialIconIn"])
    types["AppsDynamiteStorageMaterialIconOut"] = t.struct(
        {
            "name": t.string().optional(),
            "fill": t.boolean().optional(),
            "grade": t.integer().optional(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageMaterialIconOut"])
    types["AppsDynamiteStorageImageComponentIn"] = t.struct(
        {
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleIn"]
            ).optional(),
            "altText": t.string().optional(),
            "imageUri": t.string().optional(),
            "cropStyle": t.proxy(
                renames["AppsDynamiteStorageImageCropStyleIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageComponentIn"])
    types["AppsDynamiteStorageImageComponentOut"] = t.struct(
        {
            "borderStyle": t.proxy(
                renames["AppsDynamiteStorageBorderStyleOut"]
            ).optional(),
            "altText": t.string().optional(),
            "imageUri": t.string().optional(),
            "cropStyle": t.proxy(
                renames["AppsDynamiteStorageImageCropStyleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageImageComponentOut"])
    types["BotResponseIn"] = t.struct(
        {
            "requiredAction": t.string(),
            "setupUrl": t.string().optional(),
            "responseType": t.string(),
            "botId": t.proxy(renames["UserIdIn"]),
        }
    ).named(renames["BotResponseIn"])
    types["BotResponseOut"] = t.struct(
        {
            "requiredAction": t.string(),
            "setupUrl": t.string().optional(),
            "responseType": t.string(),
            "botId": t.proxy(renames["UserIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BotResponseOut"])
    types["GatewayAccessIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["GatewayAccessIn"]
    )
    types["GatewayAccessOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayAccessOut"])
    types["AppsDynamiteSharedReactionIn"] = t.struct(
        {
            "createTimestamp": t.string().optional(),
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiIn"]),
            "count": t.integer().optional(),
            "currentUserParticipated": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteSharedReactionIn"])
    types["AppsDynamiteSharedReactionOut"] = t.struct(
        {
            "createTimestamp": t.string().optional(),
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiOut"]),
            "count": t.integer().optional(),
            "currentUserParticipated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedReactionOut"])
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
    types["DlpScanSummaryIn"] = t.struct(
        {
            "scanNotApplicableForContext": t.boolean().optional(),
            "dlpAction": t.proxy(renames["DlpActionIn"]),
            "scanId": t.string().optional(),
            "scanOutcome": t.string().optional(),
        }
    ).named(renames["DlpScanSummaryIn"])
    types["DlpScanSummaryOut"] = t.struct(
        {
            "scanNotApplicableForContext": t.boolean().optional(),
            "dlpAction": t.proxy(renames["DlpActionOut"]),
            "scanId": t.string().optional(),
            "scanOutcome": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpScanSummaryOut"])
    types["ItemStatusIn"] = t.struct(
        {
            "processingErrors": t.array(
                t.proxy(renames["ProcessingErrorIn"])
            ).optional(),
            "repositoryErrors": t.array(
                t.proxy(renames["RepositoryErrorIn"])
            ).optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ItemStatusIn"])
    types["ItemStatusOut"] = t.struct(
        {
            "processingErrors": t.array(
                t.proxy(renames["ProcessingErrorOut"])
            ).optional(),
            "repositoryErrors": t.array(
                t.proxy(renames["RepositoryErrorOut"])
            ).optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemStatusOut"])
    types["AppsDynamiteSharedDocumentIn"] = t.struct(
        {
            "title": t.string().optional(),
            "url": t.string().optional(),
            "fileId": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "justification": t.proxy(
                renames["AppsDynamiteSharedJustificationIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedDocumentIn"])
    types["AppsDynamiteSharedDocumentOut"] = t.struct(
        {
            "title": t.string().optional(),
            "url": t.string().optional(),
            "fileId": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "justification": t.proxy(
                renames["AppsDynamiteSharedJustificationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedDocumentOut"])
    types["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"] = t.struct(
        {"meetingUrl": t.string()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut"] = t.struct(
        {
            "meetingUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataOut"])
    types["SafeUrlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeUrlWrappedValue": t.string().optional()}
    ).named(renames["SafeUrlProtoIn"])
    types["SafeUrlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeUrlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeUrlProtoOut"])
    types["MessageDeletedIn"] = t.struct(
        {
            "imapSyncMappings": t.array(
                t.proxy(renames["ImapSyncDeleteIn"])
            ).optional(),
            "wonderCardMappings": t.array(
                t.proxy(renames["WonderCardDeleteIn"])
            ).optional(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
        }
    ).named(renames["MessageDeletedIn"])
    types["MessageDeletedOut"] = t.struct(
        {
            "imapSyncMappings": t.array(
                t.proxy(renames["ImapSyncDeleteOut"])
            ).optional(),
            "wonderCardMappings": t.array(
                t.proxy(renames["WonderCardDeleteOut"])
            ).optional(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageDeletedOut"])
    types["TombstoneMetadataIn"] = t.struct(
        {"tombstoneType": t.string().optional()}
    ).named(renames["TombstoneMetadataIn"])
    types["TombstoneMetadataOut"] = t.struct(
        {
            "tombstoneType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TombstoneMetadataOut"])
    types["DmIdIn"] = t.struct({"dmId": t.string().optional()}).named(renames["DmIdIn"])
    types["DmIdOut"] = t.struct(
        {
            "dmId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DmIdOut"])
    types["ReferenceIn"] = t.struct(
        {
            "blobId": t.string(),
            "hash": t.string(),
            "size": t.string(),
            "contentType": t.string(),
            "name": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ReferenceIn"])
    types["ReferenceOut"] = t.struct(
        {
            "blobId": t.string(),
            "hash": t.string(),
            "size": t.string(),
            "contentType": t.string(),
            "name": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceOut"])
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
    types["DriveMetadataIn"] = t.struct(
        {
            "id": t.string().optional(),
            "canShare": t.boolean().optional(),
            "legacyUploadMetadata": t.proxy(
                renames["LegacyUploadMetadataIn"]
            ).optional(),
            "urlFragment": t.string().optional(),
            "thumbnailHeight": t.integer().optional(),
            "isDownloadRestricted": t.boolean().optional(),
            "aclFixStatus": t.proxy(renames["AclFixStatusIn"]),
            "encryptedDocId": t.boolean().optional(),
            "driveState": t.string(),
            "encryptedResourceKey": t.string().optional(),
            "title": t.string().optional(),
            "organizationDisplayName": t.string().optional(),
            "mimetype": t.string().optional(),
            "shortcutAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdIn"]
            ).optional(),
            "canEdit": t.boolean().optional(),
            "shouldNotRender": t.boolean().optional(),
            "aclFixRequest": t.proxy(renames["AclFixRequestIn"]),
            "wrappedResourceKey": t.proxy(renames["WrappedResourceKeyIn"]).optional(),
            "thumbnailWidth": t.integer().optional(),
            "canView": t.boolean().optional(),
            "isOwner": t.boolean().optional(),
            "thumbnailUrl": t.string().optional(),
            "externalMimetype": t.string().optional(),
            "driveAction": t.string().optional(),
        }
    ).named(renames["DriveMetadataIn"])
    types["DriveMetadataOut"] = t.struct(
        {
            "id": t.string().optional(),
            "canShare": t.boolean().optional(),
            "legacyUploadMetadata": t.proxy(
                renames["LegacyUploadMetadataOut"]
            ).optional(),
            "urlFragment": t.string().optional(),
            "thumbnailHeight": t.integer().optional(),
            "isDownloadRestricted": t.boolean().optional(),
            "aclFixStatus": t.proxy(renames["AclFixStatusOut"]),
            "encryptedDocId": t.boolean().optional(),
            "driveState": t.string(),
            "encryptedResourceKey": t.string().optional(),
            "title": t.string().optional(),
            "organizationDisplayName": t.string().optional(),
            "mimetype": t.string().optional(),
            "embedUrl": t.proxy(renames["TrustedResourceUrlProtoOut"]).optional(),
            "shortcutAuthorizedItemId": t.proxy(
                renames["AuthorizedItemIdOut"]
            ).optional(),
            "canEdit": t.boolean().optional(),
            "shouldNotRender": t.boolean().optional(),
            "aclFixRequest": t.proxy(renames["AclFixRequestOut"]),
            "wrappedResourceKey": t.proxy(renames["WrappedResourceKeyOut"]).optional(),
            "thumbnailWidth": t.integer().optional(),
            "canView": t.boolean().optional(),
            "isOwner": t.boolean().optional(),
            "thumbnailUrl": t.string().optional(),
            "externalMimetype": t.string().optional(),
            "driveAction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveMetadataOut"])
    types["DeepLinkDataIn"] = t.struct(
        {
            "appId": t.string().optional(),
            "deepLinkId": t.string().optional(),
            "url": t.string().optional(),
            "client": t.array(t.proxy(renames["PackagingServiceClientIn"])).optional(),
        }
    ).named(renames["DeepLinkDataIn"])
    types["DeepLinkDataOut"] = t.struct(
        {
            "appId": t.string().optional(),
            "deepLinkId": t.string().optional(),
            "url": t.string().optional(),
            "client": t.array(t.proxy(renames["PackagingServiceClientOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeepLinkDataOut"])
    types["StructuredDataObjectIn"] = t.struct(
        {"properties": t.array(t.proxy(renames["NamedPropertyIn"])).optional()}
    ).named(renames["StructuredDataObjectIn"])
    types["StructuredDataObjectOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["NamedPropertyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredDataObjectOut"])
    types["AffectedMembershipIn"] = t.struct(
        {
            "targetMembershipRole": t.string(),
            "affectedMember": t.proxy(renames["MemberIdIn"]),
            "priorMembershipRole": t.string(),
            "priorMembershipState": t.string(),
        }
    ).named(renames["AffectedMembershipIn"])
    types["AffectedMembershipOut"] = t.struct(
        {
            "targetMembershipRole": t.string(),
            "affectedMember": t.proxy(renames["MemberIdOut"]),
            "priorMembershipRole": t.string(),
            "priorMembershipState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AffectedMembershipOut"])
    types["ZwiebackSessionProtoIn"] = t.struct({"zwiebackSessionId": t.string()}).named(
        renames["ZwiebackSessionProtoIn"]
    )
    types["ZwiebackSessionProtoOut"] = t.struct(
        {
            "zwiebackSessionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZwiebackSessionProtoOut"])
    types["AppsDynamiteStorageOpenLinkIn"] = t.struct(
        {
            "url": t.string().optional(),
            "onClose": t.string(),
            "openAs": t.string(),
            "appUri": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkIn"])
    types["AppsDynamiteStorageOpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "onClose": t.string(),
            "openAs": t.string(),
            "appUri": t.proxy(
                renames["AppsDynamiteStorageOpenLinkAppUriOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOpenLinkOut"])
    types["GetSearchApplicationUserStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["SearchApplicationUserStatsIn"]))}
    ).named(renames["GetSearchApplicationUserStatsResponseIn"])
    types["GetSearchApplicationUserStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["SearchApplicationUserStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationUserStatsResponseOut"])
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
    types["ProvenanceIn"] = t.struct(
        {
            "retrievedTimestampMsec": t.string().optional(),
            "inputUrl": t.string().optional(),
            "retrievedUrl": t.string().optional(),
            "itemtype": t.array(t.string()).optional(),
            "annotationBlob": t.string().optional(),
            "canonicalUrl": t.string().optional(),
        }
    ).named(renames["ProvenanceIn"])
    types["ProvenanceOut"] = t.struct(
        {
            "retrievedTimestampMsec": t.string().optional(),
            "inputUrl": t.string().optional(),
            "retrievedUrl": t.string().optional(),
            "itemtype": t.array(t.string()).optional(),
            "annotationBlob": t.string().optional(),
            "canonicalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvenanceOut"])
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
    types["UnreserveItemsRequestIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "connectorName": t.string().optional(),
            "queue": t.string().optional(),
        }
    ).named(renames["UnreserveItemsRequestIn"])
    types["UnreserveItemsRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "connectorName": t.string().optional(),
            "queue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnreserveItemsRequestOut"])
    types["TransactionDebugInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TransactionDebugInfoIn"]
    )
    types["TransactionDebugInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TransactionDebugInfoOut"])
    types["HostAppActionMarkupIn"] = t.struct(
        {
            "calendarAction": t.proxy(
                renames["CalendarClientActionMarkupIn"]
            ).optional(),
            "gmailAction": t.proxy(renames["GmailClientActionMarkupIn"]).optional(),
            "driveAction": t.proxy(renames["DriveClientActionMarkupIn"]).optional(),
            "editorAction": t.proxy(renames["EditorClientActionMarkupIn"]).optional(),
            "sheetsAction": t.proxy(renames["SheetsClientActionMarkupIn"]).optional(),
            "chatAction": t.proxy(renames["ChatClientActionMarkupIn"]).optional(),
        }
    ).named(renames["HostAppActionMarkupIn"])
    types["HostAppActionMarkupOut"] = t.struct(
        {
            "calendarAction": t.proxy(
                renames["CalendarClientActionMarkupOut"]
            ).optional(),
            "gmailAction": t.proxy(renames["GmailClientActionMarkupOut"]).optional(),
            "driveAction": t.proxy(renames["DriveClientActionMarkupOut"]).optional(),
            "editorAction": t.proxy(renames["EditorClientActionMarkupOut"]).optional(),
            "sheetsAction": t.proxy(renames["SheetsClientActionMarkupOut"]).optional(),
            "chatAction": t.proxy(renames["ChatClientActionMarkupOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostAppActionMarkupOut"])
    types["HistoryIn"] = t.struct(
        {"record": t.array(t.proxy(renames["HistoryRecordIn"]))}
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "record": t.array(t.proxy(renames["HistoryRecordOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
    types["MessageParentIdIn"] = t.struct(
        {"topicId": t.proxy(renames["TopicIdIn"]).optional()}
    ).named(renames["MessageParentIdIn"])
    types["MessageParentIdOut"] = t.struct(
        {
            "topicId": t.proxy(renames["TopicIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageParentIdOut"])
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
    types["AppsDynamiteStorageBorderStyleIn"] = t.struct(
        {
            "strokeColor": t.proxy(renames["ColorIn"]).optional(),
            "cornerRadius": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageBorderStyleIn"])
    types["AppsDynamiteStorageBorderStyleOut"] = t.struct(
        {
            "strokeColor": t.proxy(renames["ColorOut"]).optional(),
            "cornerRadius": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageBorderStyleOut"])
    types["AclFixRequestIn"] = t.struct(
        {
            "shouldFix": t.boolean().optional(),
            "recipientEmails": t.array(t.string()).optional(),
            "role": t.string(),
        }
    ).named(renames["AclFixRequestIn"])
    types["AclFixRequestOut"] = t.struct(
        {
            "shouldFix": t.boolean().optional(),
            "recipientEmails": t.array(t.string()).optional(),
            "role": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclFixRequestOut"])
    types["InviteAcceptedEventIn"] = t.struct(
        {"participantId": t.array(t.proxy(renames["StoredParticipantIdIn"]))}
    ).named(renames["InviteAcceptedEventIn"])
    types["InviteAcceptedEventOut"] = t.struct(
        {
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InviteAcceptedEventOut"])
    types["FormActionIn"] = t.struct(
        {
            "loadIndicator": t.string(),
            "persistValues": t.boolean().optional(),
            "parameters": t.array(t.proxy(renames["ActionParameterIn"])),
            "actionMethodName": t.string().optional(),
        }
    ).named(renames["FormActionIn"])
    types["FormActionOut"] = t.struct(
        {
            "loadIndicator": t.string(),
            "persistValues": t.boolean().optional(),
            "parameters": t.array(t.proxy(renames["ActionParameterOut"])),
            "actionMethodName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormActionOut"])
    types["AutoCompleteIn"] = t.struct(
        {"items": t.array(t.proxy(renames["AutoCompleteItemIn"]))}
    ).named(renames["AutoCompleteIn"])
    types["AutoCompleteOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AutoCompleteItemOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoCompleteOut"])
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
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
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
    types["EmbedClientItemIn"] = t.struct(
        {
            "id": t.string().optional(),
            "canonicalId": t.string().optional(),
            "signature": t.string().optional(),
            "type": t.array(t.string()).optional(),
            "provenance": t.proxy(renames["ProvenanceIn"]).optional(),
            "deepLinkData": t.proxy(renames["DeepLinkDataIn"]).optional(),
            "renderId": t.string().optional(),
            "transientData": t.proxy(renames["TransientDataIn"]).optional(),
        }
    ).named(renames["EmbedClientItemIn"])
    types["EmbedClientItemOut"] = t.struct(
        {
            "id": t.string().optional(),
            "canonicalId": t.string().optional(),
            "signature": t.string().optional(),
            "type": t.array(t.string()).optional(),
            "provenance": t.proxy(renames["ProvenanceOut"]).optional(),
            "deepLinkData": t.proxy(renames["DeepLinkDataOut"]).optional(),
            "renderId": t.string().optional(),
            "transientData": t.proxy(renames["TransientDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmbedClientItemOut"])
    types["SuggestRequestIn"] = t.struct(
        {
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "query": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
        }
    ).named(renames["SuggestRequestIn"])
    types["SuggestRequestOut"] = t.struct(
        {
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "query": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestRequestOut"])
    types["FuseboxItemIn"] = t.struct(
        {
            "creationTimeMicroseconds": t.string().optional(),
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "history": t.proxy(renames["HistoryIn"]),
            "parts": t.proxy(renames["ItemPartsIn"]).optional(),
            "labels": t.proxy(renames["LabelsIn"]),
            "references": t.proxy(renames["ReferencesIn"]).optional(),
            "matchInfo": t.proxy(renames["MatchInfoIn"]),
            "lastModificationTimeUs": t.string().optional(),
            "readTs": t.string().optional(),
            "version": t.string().optional(),
            "threadLocator": t.string().optional(),
            "triggers": t.proxy(renames["TriggersIn"]),
            "snippet": t.string().optional(),
            "attributes": t.proxy(renames["AttributesIn"]),
            "lockerReferences": t.proxy(renames["ReferencesIn"]).optional(),
            "itemKey": t.proxy(renames["MultiKeyIn"]).optional(),
        }
    ).named(renames["FuseboxItemIn"])
    types["FuseboxItemOut"] = t.struct(
        {
            "creationTimeMicroseconds": t.string().optional(),
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "history": t.proxy(renames["HistoryOut"]),
            "parts": t.proxy(renames["ItemPartsOut"]).optional(),
            "labels": t.proxy(renames["LabelsOut"]),
            "references": t.proxy(renames["ReferencesOut"]).optional(),
            "matchInfo": t.proxy(renames["MatchInfoOut"]),
            "lastModificationTimeUs": t.string().optional(),
            "readTs": t.string().optional(),
            "version": t.string().optional(),
            "threadLocator": t.string().optional(),
            "triggers": t.proxy(renames["TriggersOut"]),
            "snippet": t.string().optional(),
            "attributes": t.proxy(renames["AttributesOut"]),
            "lockerReferences": t.proxy(renames["ReferencesOut"]).optional(),
            "itemKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FuseboxItemOut"])
    types["MembershipChangedMetadataIn"] = t.struct(
        {
            "initiatorType": t.string().optional(),
            "type": t.string(),
            "initiatorProfile": t.proxy(renames["UserIn"]).optional(),
            "affectedMembers": t.array(t.proxy(renames["MemberIdIn"])).optional(),
            "affectedMemberships": t.array(t.proxy(renames["AffectedMembershipIn"])),
            "affectedMemberProfiles": t.array(t.proxy(renames["MemberIn"])),
            "initiator": t.proxy(renames["UserIdIn"]).optional(),
        }
    ).named(renames["MembershipChangedMetadataIn"])
    types["MembershipChangedMetadataOut"] = t.struct(
        {
            "initiatorType": t.string().optional(),
            "type": t.string(),
            "initiatorProfile": t.proxy(renames["UserOut"]).optional(),
            "affectedMembers": t.array(t.proxy(renames["MemberIdOut"])).optional(),
            "affectedMemberships": t.array(t.proxy(renames["AffectedMembershipOut"])),
            "affectedMemberProfiles": t.array(t.proxy(renames["MemberOut"])),
            "initiator": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipChangedMetadataOut"])
    types["RoomUpdatedMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "visibility": t.proxy(
                renames["AppsDynamiteSharedGroupVisibilityIn"]
            ).optional(),
            "groupLinkSharingEnabled": t.boolean(),
            "renameMetadata": t.proxy(renames["RoomRenameMetadataIn"]),
            "initiatorType": t.string().optional(),
            "groupDetailsMetadata": t.proxy(renames["GroupDetailsUpdatedMetadataIn"]),
            "initiator": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["RoomUpdatedMetadataIn"])
    types["RoomUpdatedMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "visibility": t.proxy(
                renames["AppsDynamiteSharedGroupVisibilityOut"]
            ).optional(),
            "groupLinkSharingEnabled": t.boolean(),
            "renameMetadata": t.proxy(renames["RoomRenameMetadataOut"]),
            "initiatorType": t.string().optional(),
            "groupDetailsMetadata": t.proxy(renames["GroupDetailsUpdatedMetadataOut"]),
            "initiator": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoomUpdatedMetadataOut"])
    types["LabelAddedIn"] = t.struct(
        {
            "labelId": t.string(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
            "syncId": t.integer(),
            "labelName": t.string(),
        }
    ).named(renames["LabelAddedIn"])
    types["LabelAddedOut"] = t.struct(
        {
            "labelId": t.string(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "syncId": t.integer(),
            "labelName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelAddedOut"])
    types["InteractionIn"] = t.struct(
        {
            "type": t.string(),
            "principal": t.proxy(renames["PrincipalIn"]).optional(),
            "interactionTime": t.string().optional(),
        }
    ).named(renames["InteractionIn"])
    types["InteractionOut"] = t.struct(
        {
            "type": t.string(),
            "principal": t.proxy(renames["PrincipalOut"]).optional(),
            "interactionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InteractionOut"])
    types["WrappedResourceKeyIn"] = t.struct(
        {"resourceKey": t.string().optional()}
    ).named(renames["WrappedResourceKeyIn"])
    types["WrappedResourceKeyOut"] = t.struct(
        {
            "resourceKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WrappedResourceKeyOut"])
    types["BabelPlaceholderMetadataIn"] = t.struct(
        {
            "hangoutVideoMetadata": t.proxy(renames["HangoutVideoEventMetadataIn"]),
            "deleteMetadata": t.proxy(renames["DeleteMetadataIn"]),
            "editMetadata": t.proxy(renames["EditMetadataIn"]),
        }
    ).named(renames["BabelPlaceholderMetadataIn"])
    types["BabelPlaceholderMetadataOut"] = t.struct(
        {
            "hangoutVideoMetadata": t.proxy(renames["HangoutVideoEventMetadataOut"]),
            "deleteMetadata": t.proxy(renames["DeleteMetadataOut"]),
            "editMetadata": t.proxy(renames["EditMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BabelPlaceholderMetadataOut"])
    types["MembershipChangeEventIn"] = t.struct(
        {
            "type": t.string(),
            "leaveReason": t.string().optional(),
            "participantId": t.array(t.proxy(renames["StoredParticipantIdIn"])),
        }
    ).named(renames["MembershipChangeEventIn"])
    types["MembershipChangeEventOut"] = t.struct(
        {
            "type": t.string(),
            "leaveReason": t.string().optional(),
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipChangeEventOut"])
    types["RpcOptionsIn"] = t.struct(
        {"requestExtensions": t.proxy(renames["MessageSetIn"]).optional()}
    ).named(renames["RpcOptionsIn"])
    types["RpcOptionsOut"] = t.struct(
        {
            "requestExtensions": t.proxy(renames["MessageSetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RpcOptionsOut"])
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
    types["AllAuthenticatedUsersProtoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AllAuthenticatedUsersProtoIn"])
    types["AllAuthenticatedUsersProtoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AllAuthenticatedUsersProtoOut"])
    types["DisplayedPropertyIn"] = t.struct(
        {"propertyName": t.string().optional()}
    ).named(renames["DisplayedPropertyIn"])
    types["DisplayedPropertyOut"] = t.struct(
        {
            "propertyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayedPropertyOut"])
    types["ConsentedAppUnfurlMetadataIn"] = t.struct(
        {"clientSpecifiedAppId": t.proxy(renames["UserIdIn"]).optional()}
    ).named(renames["ConsentedAppUnfurlMetadataIn"])
    types["ConsentedAppUnfurlMetadataOut"] = t.struct(
        {
            "clientSpecifiedAppId": t.proxy(renames["UserIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentedAppUnfurlMetadataOut"])
    types["PreStateIn"] = t.struct(
        {
            "labelIds": t.array(t.string()),
            "syncIds": t.array(t.integer()).optional(),
            "messageKey": t.proxy(renames["MultiKeyIn"]),
            "threadKey": t.proxy(renames["MultiKeyIn"]),
        }
    ).named(renames["PreStateIn"])
    types["PreStateOut"] = t.struct(
        {
            "labelIds": t.array(t.string()),
            "syncIds": t.array(t.integer()).optional(),
            "messageKey": t.proxy(renames["MultiKeyOut"]),
            "threadKey": t.proxy(renames["MultiKeyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreStateOut"])
    types["PersonalLabelTagIn"] = t.struct({"labelId": t.string().optional()}).named(
        renames["PersonalLabelTagIn"]
    )
    types["PersonalLabelTagOut"] = t.struct(
        {
            "labelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalLabelTagOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"])
    types["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"])
    types["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"])
    types["RetrievalImportanceIn"] = t.struct(
        {"importance": t.string().optional()}
    ).named(renames["RetrievalImportanceIn"])
    types["RetrievalImportanceOut"] = t.struct(
        {
            "importance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrievalImportanceOut"])
    types["AppsDynamiteStorageTextParagraphIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["AppsDynamiteStorageTextParagraphIn"])
    types["AppsDynamiteStorageTextParagraphOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageTextParagraphOut"])
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
    types["TransactionContextIn"] = t.struct(
        {
            "endingRecordId": t.string().optional(),
            "startingRecordId": t.string().optional(),
            "writeTimestampUs": t.string().optional(),
        }
    ).named(renames["TransactionContextIn"])
    types["TransactionContextOut"] = t.struct(
        {
            "endingRecordId": t.string().optional(),
            "startingRecordId": t.string().optional(),
            "writeTimestampUs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionContextOut"])
    types["DoubleOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["DoubleOperatorOptionsIn"])
    types["DoubleOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleOperatorOptionsOut"])
    types["QueryInterpretationIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "interpretedQuery": t.string().optional(),
            "interpretationType": t.string(),
        }
    ).named(renames["QueryInterpretationIn"])
    types["QueryInterpretationOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "interpretedQuery": t.string().optional(),
            "interpretationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationOut"])
    types["AppsDynamiteV1ApiCompatV1AttachmentIn"] = t.struct(
        {
            "title": t.string().optional(),
            "callback_id": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1ActionIn"])
            ).optional(),
            "pretext": t.string().optional(),
            "author_link": t.string().optional(),
            "mrkdwn_in": t.array(t.string()).optional(),
            "author_name": t.string().optional(),
            "color": t.string().optional(),
            "footer_icon": t.string().optional(),
            "text": t.string().optional(),
            "fallback": t.string().optional(),
            "author_icon": t.string().optional(),
            "thumb_url": t.string().optional(),
            "attachment_type": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1FieldIn"])
            ).optional(),
            "ts": t.integer().optional(),
            "image_url": t.string().optional(),
            "footer": t.string().optional(),
            "title_link": t.string().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1AttachmentIn"])
    types["AppsDynamiteV1ApiCompatV1AttachmentOut"] = t.struct(
        {
            "title": t.string().optional(),
            "callback_id": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1ActionOut"])
            ).optional(),
            "pretext": t.string().optional(),
            "author_link": t.string().optional(),
            "mrkdwn_in": t.array(t.string()).optional(),
            "author_name": t.string().optional(),
            "color": t.string().optional(),
            "footer_icon": t.string().optional(),
            "text": t.string().optional(),
            "fallback": t.string().optional(),
            "author_icon": t.string().optional(),
            "thumb_url": t.string().optional(),
            "attachment_type": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["AppsDynamiteV1ApiCompatV1FieldOut"])
            ).optional(),
            "ts": t.integer().optional(),
            "image_url": t.string().optional(),
            "footer": t.string().optional(),
            "title_link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1AttachmentOut"])
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
    types["UpdateCcRecipientsIn"] = t.struct(
        {"ccRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateCcRecipientsIn"])
    types["UpdateCcRecipientsOut"] = t.struct(
        {
            "ccRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCcRecipientsOut"])
    types["AppsDynamiteSharedTasksAnnotationDataCreationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCreationIn"])
    types["AppsDynamiteSharedTasksAnnotationDataCreationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCreationOut"])
    types["ColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
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
    types["CircleProtoIn"] = t.struct(
        {
            "circleId": t.string().optional(),
            "ownerGaiaId": t.string().optional(),
            "requiredConsistencyTimestampUsec": t.string().optional(),
        }
    ).named(renames["CircleProtoIn"])
    types["CircleProtoOut"] = t.struct(
        {
            "circleId": t.string().optional(),
            "ownerGaiaId": t.string().optional(),
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CircleProtoOut"])
    types["CapTokenHolderProtoIn"] = t.struct(
        {"tokenHmacSha1Prefix": t.string().optional()}
    ).named(renames["CapTokenHolderProtoIn"])
    types["CapTokenHolderProtoOut"] = t.struct(
        {
            "tokenHmacSha1Prefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapTokenHolderProtoOut"])
    types["PhotoIn"] = t.struct({"url": t.string().optional()}).named(
        renames["PhotoIn"]
    )
    types["PhotoOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["SpaceIdIn"] = t.struct({"spaceId": t.string().optional()}).named(
        renames["SpaceIdIn"]
    )
    types["SpaceIdOut"] = t.struct(
        {
            "spaceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceIdOut"])
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
    types["NameIn"] = t.struct({"displayName": t.string().optional()}).named(
        renames["NameIn"]
    )
    types["NameOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
    types["DriveFollowUpRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveFollowUpRestrictIn"]
    )
    types["DriveFollowUpRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveFollowUpRestrictOut"])
    types["ChatConserverMessageContentIn"] = t.struct(
        {
            "segment": t.array(t.proxy(renames["SegmentIn"])).optional(),
            "attachment": t.array(
                t.proxy(renames["SocialCommonAttachmentAttachmentIn"])
            ).optional(),
        }
    ).named(renames["ChatConserverMessageContentIn"])
    types["ChatConserverMessageContentOut"] = t.struct(
        {
            "segment": t.array(t.proxy(renames["SegmentOut"])).optional(),
            "attachment": t.array(
                t.proxy(renames["SocialCommonAttachmentAttachmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatConserverMessageContentOut"])
    types["AppsDynamiteStorageDecoratedTextIn"] = t.struct(
        {
            "switchControl": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextSwitchControlIn"]
            ).optional(),
            "button": t.proxy(renames["AppsDynamiteStorageButtonIn"]).optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "wrapText": t.boolean().optional(),
            "endIcon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "bottomLabel": t.string().optional(),
            "text": t.string(),
            "topLabel": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
            "startIcon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextIn"])
    types["AppsDynamiteStorageDecoratedTextOut"] = t.struct(
        {
            "switchControl": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextSwitchControlOut"]
            ).optional(),
            "button": t.proxy(renames["AppsDynamiteStorageButtonOut"]).optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "wrapText": t.boolean().optional(),
            "endIcon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "bottomLabel": t.string().optional(),
            "text": t.string(),
            "topLabel": t.string().optional(),
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "startIcon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageDecoratedTextOut"])
    types["EditMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EditMetadataIn"]
    )
    types["EditMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EditMetadataOut"])
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
    types["ValueIn"] = t.struct(
        {
            "stringValue": t.string(),
            "integerValue": t.string(),
            "doubleValue": t.number(),
            "booleanValue": t.boolean(),
            "timestampValue": t.string(),
            "dateValue": t.proxy(renames["DateIn"]),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "stringValue": t.string(),
            "integerValue": t.string(),
            "doubleValue": t.number(),
            "booleanValue": t.boolean(),
            "timestampValue": t.string(),
            "dateValue": t.proxy(renames["DateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["SourceScoringConfigIn"] = t.struct(
        {"sourceImportance": t.string().optional()}
    ).named(renames["SourceScoringConfigIn"])
    types["SourceScoringConfigOut"] = t.struct(
        {
            "sourceImportance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceScoringConfigOut"])
    types["VideoInfoIn"] = t.struct({"duration": t.integer().optional()}).named(
        renames["VideoInfoIn"]
    )
    types["VideoInfoOut"] = t.struct(
        {
            "duration": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoInfoOut"])
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
    types["MessageIdIn"] = t.struct(
        {
            "messageId": t.string().optional(),
            "parentId": t.proxy(renames["MessageParentIdIn"]).optional(),
        }
    ).named(renames["MessageIdIn"])
    types["MessageIdOut"] = t.struct(
        {
            "messageId": t.string().optional(),
            "parentId": t.proxy(renames["MessageParentIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageIdOut"])
    types["AppsDynamiteSharedAssistantUnfulfillableRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantUnfulfillableRequestIn"])
    types["AppsDynamiteSharedAssistantUnfulfillableRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedAssistantUnfulfillableRequestOut"])
    types["GetCustomerUserStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["CustomerUserStatsIn"]))}
    ).named(renames["GetCustomerUserStatsResponseIn"])
    types["GetCustomerUserStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerUserStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerUserStatsResponseOut"])
    types["AppsDynamiteSharedOrganizationInfoCustomerInfoIn"] = t.struct(
        {"customerId": t.proxy(renames["CustomerIdIn"])}
    ).named(renames["AppsDynamiteSharedOrganizationInfoCustomerInfoIn"])
    types["AppsDynamiteSharedOrganizationInfoCustomerInfoOut"] = t.struct(
        {
            "customerId": t.proxy(renames["CustomerIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedOrganizationInfoCustomerInfoOut"])
    types["BroadcastStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["BroadcastStatsIn"])
    types["BroadcastStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BroadcastStatsOut"])
    types["FixedFooterIn"] = t.struct(
        {
            "secondaryButton": t.proxy(renames["TextButtonIn"]),
            "primaryButton": t.proxy(renames["TextButtonIn"]),
            "buttons": t.array(t.proxy(renames["ButtonIn"])),
        }
    ).named(renames["FixedFooterIn"])
    types["FixedFooterOut"] = t.struct(
        {
            "secondaryButton": t.proxy(renames["TextButtonOut"]),
            "primaryButton": t.proxy(renames["TextButtonOut"]),
            "buttons": t.array(t.proxy(renames["ButtonOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixedFooterOut"])
    types["SimpleSecretLabelProtoIn"] = t.struct(
        {
            "inviteId": t.string().optional(),
            "genericLabel": t.string().optional(),
            "capabilityId": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SimpleSecretLabelProtoIn"])
    types["SimpleSecretLabelProtoOut"] = t.struct(
        {
            "inviteId": t.string().optional(),
            "genericLabel": t.string().optional(),
            "capabilityId": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleSecretLabelProtoOut"])
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
    types["LinkDataIn"] = t.struct(
        {
            "attachment": t.proxy(
                renames["SocialCommonAttachmentAttachmentIn"]
            ).optional(),
            "title": t.string().optional(),
            "linkType": t.string().optional(),
            "displayUrl": t.string().optional(),
            "linkTarget": t.string().optional(),
            "attachmentRenderHint": t.string().optional(),
        }
    ).named(renames["LinkDataIn"])
    types["LinkDataOut"] = t.struct(
        {
            "attachment": t.proxy(
                renames["SocialCommonAttachmentAttachmentOut"]
            ).optional(),
            "title": t.string().optional(),
            "linkType": t.string().optional(),
            "displayUrl": t.string().optional(),
            "linkTarget": t.string().optional(),
            "attachmentRenderHint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkDataOut"])
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
    types["YoutubeUserProtoIn"] = t.struct({"youtubeUserId": t.string()}).named(
        renames["YoutubeUserProtoIn"]
    )
    types["YoutubeUserProtoOut"] = t.struct(
        {
            "youtubeUserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YoutubeUserProtoOut"])
    types["CustomerIdIn"] = t.struct({"customerId": t.string()}).named(
        renames["CustomerIdIn"]
    )
    types["CustomerIdOut"] = t.struct(
        {
            "customerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerIdOut"])
    types["MessageIn"] = t.struct(
        {
            "lastEditTime": t.string().optional(),
            "communalLabels": t.array(
                t.proxy(renames["CommunalLabelTagIn"])
            ).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationIn"])).optional(),
            "props": t.proxy(renames["MessagePropsIn"]).optional(),
            "textBody": t.string().optional(),
            "editableBy": t.string().optional(),
            "originAppSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedOriginAppSuggestionIn"])
            ).optional(),
            "messageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedMessageIntegrationPayloadIn"]
            ).optional(),
            "personalLabels": t.array(
                t.proxy(renames["PersonalLabelTagIn"])
            ).optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryIn"]).optional(),
            "secondaryMessageKey": t.string().optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsIn"]
            ).optional(),
            "attributes": t.proxy(renames["MessageAttributesIn"]).optional(),
            "fallbackText": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "reactions": t.array(
                t.proxy(renames["AppsDynamiteSharedReactionIn"])
            ).optional(),
            "deleteTimeForRequester": t.string().optional(),
            "createTime": t.string().optional(),
            "appProfile": t.proxy(renames["AppsDynamiteSharedAppProfileIn"]).optional(),
            "deleteTime": t.string().optional(),
            "deletableBy": t.string().optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataIn"])).optional(),
            "messageOrigin": t.string().optional(),
            "isContentPurged": t.boolean().optional(),
            "id": t.proxy(renames["MessageIdIn"]).optional(),
            "attachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "updaterId": t.proxy(renames["UserIdIn"]).optional(),
            "privateMessageViewer": t.proxy(renames["UserIdIn"]).optional(),
            "creatorId": t.proxy(renames["UserIdIn"]).optional(),
            "messageState": t.string().optional(),
            "botResponses": t.array(t.proxy(renames["BotResponseIn"])).optional(),
            "privateMessageInfos": t.array(
                t.proxy(renames["PrivateMessageInfoIn"])
            ).optional(),
            "richTextFormattingType": t.string().optional(),
            "tombstoneMetadata": t.proxy(renames["TombstoneMetadataIn"]).optional(),
            "deletedByVault": t.boolean().optional(),
            "localId": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "lastEditTime": t.string().optional(),
            "communalLabels": t.array(
                t.proxy(renames["CommunalLabelTagOut"])
            ).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "props": t.proxy(renames["MessagePropsOut"]).optional(),
            "textBody": t.string().optional(),
            "editableBy": t.string().optional(),
            "originAppSuggestions": t.array(
                t.proxy(renames["AppsDynamiteSharedOriginAppSuggestionOut"])
            ).optional(),
            "quotedMessageMetadata": t.proxy(
                renames["QuotedMessageMetadataOut"]
            ).optional(),
            "messageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedMessageIntegrationPayloadOut"]
            ).optional(),
            "personalLabels": t.array(
                t.proxy(renames["PersonalLabelTagOut"])
            ).optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryOut"]).optional(),
            "secondaryMessageKey": t.string().optional(),
            "retentionSettings": t.proxy(
                renames["AppsDynamiteSharedRetentionSettingsOut"]
            ).optional(),
            "attributes": t.proxy(renames["MessageAttributesOut"]).optional(),
            "fallbackText": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "reactions": t.array(
                t.proxy(renames["AppsDynamiteSharedReactionOut"])
            ).optional(),
            "deleteTimeForRequester": t.string().optional(),
            "contentReportSummary": t.proxy(renames["ContentReportSummaryOut"]),
            "createTime": t.string().optional(),
            "appProfile": t.proxy(
                renames["AppsDynamiteSharedAppProfileOut"]
            ).optional(),
            "quotedByState": t.string().optional(),
            "deleteTime": t.string().optional(),
            "isInlineReply": t.boolean().optional(),
            "deletableBy": t.string().optional(),
            "uploadMetadata": t.array(t.proxy(renames["UploadMetadataOut"])).optional(),
            "messageOrigin": t.string().optional(),
            "isContentPurged": t.boolean().optional(),
            "id": t.proxy(renames["MessageIdOut"]).optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "reports": t.array(t.proxy(renames["ContentReportOut"])).optional(),
            "updaterId": t.proxy(renames["UserIdOut"]).optional(),
            "privateMessageViewer": t.proxy(renames["UserIdOut"]).optional(),
            "creatorId": t.proxy(renames["UserIdOut"]).optional(),
            "messageState": t.string().optional(),
            "botResponses": t.array(t.proxy(renames["BotResponseOut"])).optional(),
            "privateMessageInfos": t.array(
                t.proxy(renames["PrivateMessageInfoOut"])
            ).optional(),
            "richTextFormattingType": t.string().optional(),
            "tombstoneMetadata": t.proxy(renames["TombstoneMetadataOut"]).optional(),
            "deletedByVault": t.boolean().optional(),
            "localId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
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
    types["AclInfoIn"] = t.struct(
        {
            "groupsCount": t.integer().optional(),
            "usersCount": t.integer().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["AclInfoIn"])
    types["AclInfoOut"] = t.struct(
        {
            "groupsCount": t.integer().optional(),
            "usersCount": t.integer().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclInfoOut"])
    types["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataOut"])
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
    types["PropertyDefinitionIn"] = t.struct(
        {
            "booleanPropertyOptions": t.proxy(renames["BooleanPropertyOptionsIn"]),
            "displayOptions": t.proxy(renames["PropertyDisplayOptionsIn"]).optional(),
            "doublePropertyOptions": t.proxy(renames["DoublePropertyOptionsIn"]),
            "isReturnable": t.boolean().optional(),
            "isWildcardSearchable": t.boolean().optional(),
            "textPropertyOptions": t.proxy(renames["TextPropertyOptionsIn"]),
            "htmlPropertyOptions": t.proxy(renames["HtmlPropertyOptionsIn"]),
            "isSortable": t.boolean().optional(),
            "isSuggestable": t.boolean().optional(),
            "name": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "datePropertyOptions": t.proxy(renames["DatePropertyOptionsIn"]),
            "isRepeatable": t.boolean().optional(),
            "timestampPropertyOptions": t.proxy(renames["TimestampPropertyOptionsIn"]),
            "enumPropertyOptions": t.proxy(renames["EnumPropertyOptionsIn"]),
            "integerPropertyOptions": t.proxy(renames["IntegerPropertyOptionsIn"]),
            "objectPropertyOptions": t.proxy(renames["ObjectPropertyOptionsIn"]),
        }
    ).named(renames["PropertyDefinitionIn"])
    types["PropertyDefinitionOut"] = t.struct(
        {
            "booleanPropertyOptions": t.proxy(renames["BooleanPropertyOptionsOut"]),
            "displayOptions": t.proxy(renames["PropertyDisplayOptionsOut"]).optional(),
            "doublePropertyOptions": t.proxy(renames["DoublePropertyOptionsOut"]),
            "isReturnable": t.boolean().optional(),
            "isWildcardSearchable": t.boolean().optional(),
            "textPropertyOptions": t.proxy(renames["TextPropertyOptionsOut"]),
            "htmlPropertyOptions": t.proxy(renames["HtmlPropertyOptionsOut"]),
            "isSortable": t.boolean().optional(),
            "isSuggestable": t.boolean().optional(),
            "name": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "datePropertyOptions": t.proxy(renames["DatePropertyOptionsOut"]),
            "isRepeatable": t.boolean().optional(),
            "timestampPropertyOptions": t.proxy(renames["TimestampPropertyOptionsOut"]),
            "enumPropertyOptions": t.proxy(renames["EnumPropertyOptionsOut"]),
            "integerPropertyOptions": t.proxy(renames["IntegerPropertyOptionsOut"]),
            "objectPropertyOptions": t.proxy(renames["ObjectPropertyOptionsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyDefinitionOut"])
    types["AppsDynamiteSharedVideoReferenceIn"] = t.struct(
        {"format": t.array(t.integer()).optional(), "status": t.string().optional()}
    ).named(renames["AppsDynamiteSharedVideoReferenceIn"])
    types["AppsDynamiteSharedVideoReferenceOut"] = t.struct(
        {
            "format": t.array(t.integer()).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedVideoReferenceOut"])
    types["GmailClientActionMarkupIn"] = t.struct(
        {
            "openCreatedDraftActionMarkup": t.proxy(
                renames["OpenCreatedDraftActionMarkupIn"]
            ),
            "updateDraftActionMarkup": t.proxy(renames["UpdateDraftActionMarkupIn"]),
            "taskAction": t.proxy(renames["TaskActionMarkupIn"]),
            "addonComposeUiActionMarkup": t.proxy(
                renames["AddonComposeUiActionMarkupIn"]
            ),
        }
    ).named(renames["GmailClientActionMarkupIn"])
    types["GmailClientActionMarkupOut"] = t.struct(
        {
            "openCreatedDraftActionMarkup": t.proxy(
                renames["OpenCreatedDraftActionMarkupOut"]
            ),
            "updateDraftActionMarkup": t.proxy(renames["UpdateDraftActionMarkupOut"]),
            "taskAction": t.proxy(renames["TaskActionMarkupOut"]),
            "addonComposeUiActionMarkup": t.proxy(
                renames["AddonComposeUiActionMarkupOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmailClientActionMarkupOut"])
    types["AppsDynamiteStorageDividerIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteStorageDividerIn"])
    types["AppsDynamiteStorageDividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteStorageDividerOut"])
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
    types["AppsDynamiteStorageButtonIn"] = t.struct(
        {
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconIn"]).optional(),
            "text": t.string().optional(),
            "altText": t.string().optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonIn"])
    types["AppsDynamiteStorageButtonOut"] = t.struct(
        {
            "onClick": t.proxy(renames["AppsDynamiteStorageOnClickOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "icon": t.proxy(renames["AppsDynamiteStorageIconOut"]).optional(),
            "text": t.string().optional(),
            "altText": t.string().optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonOut"])
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
    types["UploadItemRefIn"] = t.struct({"name": t.string().optional()}).named(
        renames["UploadItemRefIn"]
    )
    types["UploadItemRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadItemRefOut"])
    types["ResultDisplayLineIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["ResultDisplayFieldIn"]))}
    ).named(renames["ResultDisplayLineIn"])
    types["ResultDisplayLineOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["ResultDisplayFieldOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayLineOut"])
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
    types["SwitchWidgetIn"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "controlType": t.string(),
            "selected": t.boolean(),
            "onChange": t.proxy(renames["FormActionIn"]),
        }
    ).named(renames["SwitchWidgetIn"])
    types["SwitchWidgetOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "controlType": t.string(),
            "selected": t.boolean(),
            "onChange": t.proxy(renames["FormActionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SwitchWidgetOut"])
    types["ContentReportIn"] = t.struct(
        {
            "reportType": t.proxy(
                renames["AppsDynamiteSharedContentReportTypeIn"]
            ).optional(),
            "reportCreateTimestamp": t.string().optional(),
            "revisionCreateTimestamp": t.string().optional(),
            "reporterUserId": t.proxy(renames["UserIdIn"]).optional(),
            "reportJustification": t.proxy(
                renames["ContentReportJustificationIn"]
            ).optional(),
        }
    ).named(renames["ContentReportIn"])
    types["ContentReportOut"] = t.struct(
        {
            "reportType": t.proxy(
                renames["AppsDynamiteSharedContentReportTypeOut"]
            ).optional(),
            "reportCreateTimestamp": t.string().optional(),
            "revisionCreateTimestamp": t.string().optional(),
            "reporterUserId": t.proxy(renames["UserIdOut"]).optional(),
            "reportJustification": t.proxy(
                renames["ContentReportJustificationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentReportOut"])
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
    types["ResultDebugInfoIn"] = t.struct(
        {"formattedDebugInfo": t.string().optional()}
    ).named(renames["ResultDebugInfoIn"])
    types["ResultDebugInfoOut"] = t.struct(
        {
            "formattedDebugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDebugInfoOut"])
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
    types["ResultDisplayFieldIn"] = t.struct(
        {
            "property": t.proxy(renames["NamedPropertyIn"]).optional(),
            "operatorName": t.string().optional(),
            "label": t.string().optional(),
        }
    ).named(renames["ResultDisplayFieldIn"])
    types["ResultDisplayFieldOut"] = t.struct(
        {
            "property": t.proxy(renames["NamedPropertyOut"]).optional(),
            "operatorName": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayFieldOut"])
    types["LabelRemovedIn"] = t.struct(
        {
            "labelId": t.string(),
            "labelName": t.string(),
            "syncId": t.integer(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
        }
    ).named(renames["LabelRemovedIn"])
    types["LabelRemovedOut"] = t.struct(
        {
            "labelId": t.string(),
            "labelName": t.string(),
            "syncId": t.integer(),
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelRemovedOut"])
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
    types["ErrorInfoIn"] = t.struct(
        {"errorMessages": t.array(t.proxy(renames["ErrorMessageIn"]))}
    ).named(renames["ErrorInfoIn"])
    types["ErrorInfoOut"] = t.struct(
        {
            "errorMessages": t.array(t.proxy(renames["ErrorMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorInfoOut"])
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
    types["IntegerPropertyOptionsIn"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsIn"]
            ).optional(),
            "operatorOptions": t.proxy(renames["IntegerOperatorOptionsIn"]).optional(),
            "maximumValue": t.string().optional(),
            "minimumValue": t.string().optional(),
        }
    ).named(renames["IntegerPropertyOptionsIn"])
    types["IntegerPropertyOptionsOut"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsOut"]
            ).optional(),
            "operatorOptions": t.proxy(renames["IntegerOperatorOptionsOut"]).optional(),
            "maximumValue": t.string().optional(),
            "minimumValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerPropertyOptionsOut"])
    types["AppsDynamiteSharedChatItemActivityInfoIn"] = t.struct(
        {
            "feedItemNudge": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"]
            ),
            "feedItemThreadReply": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReplyIn"]
            ),
            "feedItemUserMention": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionIn"]
            ),
            "feedItemReactions": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"]
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
            "feedItemUserMention": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemUserMentionOut"]
            ),
            "feedItemReactions": t.proxy(
                renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoOut"])
    types["PollItemsResponseIn"] = t.struct(
        {"items": t.array(t.proxy(renames["ItemIn"])).optional()}
    ).named(renames["PollItemsResponseIn"])
    types["PollItemsResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollItemsResponseOut"])
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
    types["SourceIn"] = t.struct(
        {"predefinedSource": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "predefinedSource": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["AppsDynamiteSharedMessageComponentSearchInfoIn"] = t.struct(
        {
            "titleTextWithDescription": t.proxy(
                renames["AppsDynamiteSharedTextWithDescriptionIn"]
            ).optional(),
            "matchedSearch": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageComponentSearchInfoIn"])
    types["AppsDynamiteSharedMessageComponentSearchInfoOut"] = t.struct(
        {
            "titleTextWithDescription": t.proxy(
                renames["AppsDynamiteSharedTextWithDescriptionOut"]
            ).optional(),
            "matchedSearch": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageComponentSearchInfoOut"])
    types["PinnedItemIdIn"] = t.struct({"driveId": t.string().optional()}).named(
        renames["PinnedItemIdIn"]
    )
    types["PinnedItemIdOut"] = t.struct(
        {
            "driveId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PinnedItemIdOut"])
    types["UserMentionDataIn"] = t.struct(
        {
            "user": t.proxy(renames["PrincipalProtoIn"]).optional(),
            "email": t.string(),
            "userGaiaId": t.string().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["UserMentionDataIn"])
    types["UserMentionDataOut"] = t.struct(
        {
            "user": t.proxy(renames["PrincipalProtoOut"]).optional(),
            "email": t.string(),
            "userGaiaId": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserMentionDataOut"])
    types["AppsDynamiteSharedOrganizationInfoConsumerInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedOrganizationInfoConsumerInfoIn"])
    types["AppsDynamiteSharedOrganizationInfoConsumerInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedOrganizationInfoConsumerInfoOut"])
    types["GroupIdIn"] = t.struct(
        {
            "dmId": t.proxy(renames["DmIdIn"]).optional(),
            "spaceId": t.proxy(renames["SpaceIdIn"]).optional(),
        }
    ).named(renames["GroupIdIn"])
    types["GroupIdOut"] = t.struct(
        {
            "dmId": t.proxy(renames["DmIdOut"]).optional(),
            "spaceId": t.proxy(renames["SpaceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupIdOut"])
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
    types["AppsDynamiteStorageActionIn"] = t.struct(
        {
            "persistValues": t.boolean().optional(),
            "loadIndicator": t.string(),
            "interaction": t.string(),
            "function": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["AppsDynamiteStorageActionActionParameterIn"])
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageActionIn"])
    types["AppsDynamiteStorageActionOut"] = t.struct(
        {
            "persistValues": t.boolean().optional(),
            "loadIndicator": t.string(),
            "interaction": t.string(),
            "function": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["AppsDynamiteStorageActionActionParameterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageActionOut"])
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
    types["ItemMetadataIn"] = t.struct(
        {
            "objectType": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeIn"])
            ).optional(),
            "createTime": t.string().optional(),
            "searchQualityMetadata": t.proxy(
                renames["SearchQualityMetadataIn"]
            ).optional(),
            "keywords": t.array(t.string()).optional(),
            "sourceRepositoryUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "title": t.string().optional(),
            "containerName": t.string().optional(),
            "hash": t.string().optional(),
            "interactions": t.array(t.proxy(renames["InteractionIn"])).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["ItemMetadataIn"])
    types["ItemMetadataOut"] = t.struct(
        {
            "objectType": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "searchQualityMetadata": t.proxy(
                renames["SearchQualityMetadataOut"]
            ).optional(),
            "keywords": t.array(t.string()).optional(),
            "sourceRepositoryUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "title": t.string().optional(),
            "containerName": t.string().optional(),
            "hash": t.string().optional(),
            "interactions": t.array(t.proxy(renames["InteractionOut"])).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemMetadataOut"])
    types["TopicIdIn"] = t.struct(
        {
            "topicId": t.string().optional(),
            "groupId": t.proxy(renames["GroupIdIn"]).optional(),
        }
    ).named(renames["TopicIdIn"])
    types["TopicIdOut"] = t.struct(
        {
            "topicId": t.string().optional(),
            "groupId": t.proxy(renames["GroupIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicIdOut"])
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
    types["SimpleSecretHolderProtoIn"] = t.struct(
        {"label": t.proxy(renames["SimpleSecretLabelProtoIn"]).optional()}
    ).named(renames["SimpleSecretHolderProtoIn"])
    types["SimpleSecretHolderProtoOut"] = t.struct(
        {
            "label": t.proxy(renames["SimpleSecretLabelProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleSecretHolderProtoOut"])
    types["AppsDynamiteSharedAssistantFeedbackContextIn"] = t.struct(
        {
            "thumbsFeedback": t.string().optional(),
            "feedbackChips": t.array(
                t.proxy(
                    renames["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipIn"]
                )
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantFeedbackContextIn"])
    types["AppsDynamiteSharedAssistantFeedbackContextOut"] = t.struct(
        {
            "thumbsFeedback": t.string().optional(),
            "feedbackChips": t.array(
                t.proxy(
                    renames["AppsDynamiteSharedAssistantFeedbackContextFeedbackChipOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantFeedbackContextOut"])
    types["DataSourceIn"] = t.struct(
        {
            "disableModifications": t.boolean().optional(),
            "itemsVisibility": t.array(
                t.proxy(renames["GSuitePrincipalIn"])
            ).optional(),
            "name": t.string().optional(),
            "disableServing": t.boolean().optional(),
            "indexingServiceAccounts": t.array(t.string()).optional(),
            "operationIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "returnThumbnailUrls": t.boolean().optional(),
            "shortName": t.string().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "disableModifications": t.boolean().optional(),
            "itemsVisibility": t.array(
                t.proxy(renames["GSuitePrincipalOut"])
            ).optional(),
            "name": t.string().optional(),
            "disableServing": t.boolean().optional(),
            "indexingServiceAccounts": t.array(t.string()).optional(),
            "operationIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "returnThumbnailUrls": t.boolean().optional(),
            "shortName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["GridIn"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "borderStyle": t.proxy(renames["BorderStyleIn"]).optional(),
            "title": t.string().optional(),
            "items": t.array(t.proxy(renames["GridItemIn"])).optional(),
            "numColumns": t.integer().optional(),
        }
    ).named(renames["GridIn"])
    types["GridOut"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "borderStyle": t.proxy(renames["BorderStyleOut"]).optional(),
            "title": t.string().optional(),
            "items": t.array(t.proxy(renames["GridItemOut"])).optional(),
            "numColumns": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridOut"])
    types["MdbGroupProtoIn"] = t.struct({"groupName": t.string()}).named(
        renames["MdbGroupProtoIn"]
    )
    types["MdbGroupProtoOut"] = t.struct(
        {"groupName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MdbGroupProtoOut"])
    types["YouTubeBroadcastSessionInfoIn"] = t.struct(
        {
            "broadcastStats": t.proxy(renames["YouTubeBroadcastStatsIn"]).optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoIn"]).optional(),
            "youTubeLiveBroadcastEvent": t.proxy(
                renames["YouTubeLiveBroadcastEventIn"]
            ).optional(),
            "youTubeBroadcastSessionId": t.string().optional(),
        }
    ).named(renames["YouTubeBroadcastSessionInfoIn"])
    types["YouTubeBroadcastSessionInfoOut"] = t.struct(
        {
            "broadcastStats": t.proxy(renames["YouTubeBroadcastStatsOut"]).optional(),
            "sessionStateInfo": t.proxy(renames["SessionStateInfoOut"]).optional(),
            "youTubeLiveBroadcastEvent": t.proxy(
                renames["YouTubeLiveBroadcastEventOut"]
            ).optional(),
            "youTubeBroadcastSessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeBroadcastSessionInfoOut"])
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
    types["EnumValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["EnumValuesIn"]
    )
    types["EnumValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValuesOut"])
    types["ResetSearchApplicationRequestIn"] = t.struct(
        {"debugOptions": t.proxy(renames["DebugOptionsIn"]).optional()}
    ).named(renames["ResetSearchApplicationRequestIn"])
    types["ResetSearchApplicationRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetSearchApplicationRequestOut"])
    types["MessagePropsIn"] = t.struct(
        {"babelProps": t.proxy(renames["BabelMessagePropsIn"])}
    ).named(renames["MessagePropsIn"])
    types["MessagePropsOut"] = t.struct(
        {
            "babelProps": t.proxy(renames["BabelMessagePropsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessagePropsOut"])
    types["LabelUpdateIn"] = t.struct(
        {
            "canonicalName": t.string(),
            "labelCreated": t.proxy(renames["LabelCreatedIn"]),
            "syncId": t.integer(),
            "labelRenamed": t.proxy(renames["LabelRenamedIn"]),
            "labelDeleted": t.proxy(renames["LabelDeletedIn"]),
            "labelUpdated": t.proxy(renames["LabelUpdatedIn"]),
            "labelId": t.string(),
        }
    ).named(renames["LabelUpdateIn"])
    types["LabelUpdateOut"] = t.struct(
        {
            "canonicalName": t.string(),
            "labelCreated": t.proxy(renames["LabelCreatedOut"]),
            "syncId": t.integer(),
            "labelRenamed": t.proxy(renames["LabelRenamedOut"]),
            "labelDeleted": t.proxy(renames["LabelDeletedOut"]),
            "labelUpdated": t.proxy(renames["LabelUpdatedOut"]),
            "labelId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelUpdateOut"])
    types["DoublePropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["DoubleOperatorOptionsIn"]).optional()}
    ).named(renames["DoublePropertyOptionsIn"])
    types["DoublePropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["DoubleOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoublePropertyOptionsOut"])
    types["MatchRangeIn"] = t.struct(
        {"start": t.integer().optional(), "end": t.integer().optional()}
    ).named(renames["MatchRangeIn"])
    types["MatchRangeOut"] = t.struct(
        {
            "start": t.integer().optional(),
            "end": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchRangeOut"])
    types["QueryCountByStatusIn"] = t.struct(
        {"count": t.string(), "statusCode": t.integer().optional()}
    ).named(renames["QueryCountByStatusIn"])
    types["QueryCountByStatusOut"] = t.struct(
        {
            "count": t.string(),
            "statusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryCountByStatusOut"])
    types["PropertyDisplayOptionsIn"] = t.struct(
        {"displayLabel": t.string().optional()}
    ).named(renames["PropertyDisplayOptionsIn"])
    types["PropertyDisplayOptionsOut"] = t.struct(
        {
            "displayLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyDisplayOptionsOut"])
    types["PollItemsRequestIn"] = t.struct(
        {
            "queue": t.string().optional(),
            "statusCodes": t.array(t.string()).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "limit": t.integer().optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["PollItemsRequestIn"])
    types["PollItemsRequestOut"] = t.struct(
        {
            "queue": t.string().optional(),
            "statusCodes": t.array(t.string()).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "limit": t.integer().optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollItemsRequestOut"])
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
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"] = t.struct(
        {"nudgeType": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut"] = t.struct(
        {
            "nudgeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemNudgeOut"])
    types["PaygateInfoIn"] = t.struct(
        {
            "showUpgradePromos": t.boolean().optional(),
            "callEndingSoonWarningTime": t.string().optional(),
            "callEndingTime": t.string().optional(),
        }
    ).named(renames["PaygateInfoIn"])
    types["PaygateInfoOut"] = t.struct(
        {
            "showUpgradePromos": t.boolean().optional(),
            "callEndingSoonWarningTime": t.string().optional(),
            "callEndingTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaygateInfoOut"])
    types["MetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "fields": t.array(t.proxy(renames["NamedPropertyIn"])).optional(),
            "displayOptions": t.proxy(renames["ResultDisplayMetadataIn"]).optional(),
            "createTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "objectType": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "owner": t.proxy(renames["PersonIn"]).optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "fields": t.array(t.proxy(renames["NamedPropertyOut"])).optional(),
            "displayOptions": t.proxy(renames["ResultDisplayMetadataOut"]).optional(),
            "createTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "objectType": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "owner": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["HashtagDataIn"] = t.struct({"searchText": t.string()}).named(
        renames["HashtagDataIn"]
    )
    types["HashtagDataOut"] = t.struct(
        {
            "searchText": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashtagDataOut"])
    types["AppsDynamiteStorageSelectionInputSelectionItemIn"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "text": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputSelectionItemIn"])
    types["AppsDynamiteStorageSelectionInputSelectionItemOut"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "text": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageSelectionInputSelectionItemOut"])
    types["SearchResultIn"] = t.struct(
        {
            "debugInfo": t.proxy(renames["ResultDebugInfoIn"]).optional(),
            "url": t.string().optional(),
            "snippet": t.proxy(renames["SnippetIn"]).optional(),
            "metadata": t.proxy(renames["MetadataIn"]).optional(),
            "title": t.string().optional(),
            "clusteredResults": t.array(t.proxy(renames["SearchResultIn"])).optional(),
        }
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "debugInfo": t.proxy(renames["ResultDebugInfoOut"]).optional(),
            "url": t.string().optional(),
            "snippet": t.proxy(renames["SnippetOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "title": t.string().optional(),
            "clusteredResults": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["IntegerFacetingOptionsIn"] = t.struct(
        {"integerBuckets": t.array(t.string()).optional()}
    ).named(renames["IntegerFacetingOptionsIn"])
    types["IntegerFacetingOptionsOut"] = t.struct(
        {
            "integerBuckets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerFacetingOptionsOut"])
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
    types["AppsDynamiteSharedAvatarInfoIn"] = t.struct(
        {"emoji": t.proxy(renames["AppsDynamiteSharedEmojiIn"])}
    ).named(renames["AppsDynamiteSharedAvatarInfoIn"])
    types["AppsDynamiteSharedAvatarInfoOut"] = t.struct(
        {
            "emoji": t.proxy(renames["AppsDynamiteSharedEmojiOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAvatarInfoOut"])
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
    types["PersonIn"] = t.struct(
        {
            "emailAddresses": t.array(t.proxy(renames["EmailAddressIn"])).optional(),
            "name": t.string().optional(),
            "photos": t.array(t.proxy(renames["PhotoIn"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
            "personNames": t.array(t.proxy(renames["NameIn"])).optional(),
            "obfuscatedId": t.string().optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "emailAddresses": t.array(t.proxy(renames["EmailAddressOut"])).optional(),
            "name": t.string().optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberOut"])).optional(),
            "personNames": t.array(t.proxy(renames["NameOut"])).optional(),
            "obfuscatedId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
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
    types["GroupLinkSharingModificationEventIn"] = t.struct(
        {"newStatus": t.string()}
    ).named(renames["GroupLinkSharingModificationEventIn"])
    types["GroupLinkSharingModificationEventOut"] = t.struct(
        {"newStatus": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GroupLinkSharingModificationEventOut"])
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
    types["AppsDynamiteSharedTasksAnnotationDataIn"] = t.struct(
        {
            "assigneeChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeIn"]
            ),
            "taskId": t.string().optional(),
            "completionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"]
            ),
            "creation": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCreationIn"]
            ),
            "taskProperties": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"]
            ).optional(),
            "deletionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeIn"]
            ),
            "userDefinedMessage": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageIn"]
            ),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataIn"])
    types["AppsDynamiteSharedTasksAnnotationDataOut"] = t.struct(
        {
            "assigneeChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataAssigneeChangeOut"]
            ),
            "taskId": t.string().optional(),
            "completionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"]
            ),
            "creation": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataCreationOut"]
            ),
            "taskProperties": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"]
            ).optional(),
            "deletionChange": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataDeletionChangeOut"]
            ),
            "userDefinedMessage": t.proxy(
                renames["AppsDynamiteSharedTasksAnnotationDataUserDefinedMessageOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataOut"])
    types["SuggestResponseIn"] = t.struct(
        {"suggestResults": t.array(t.proxy(renames["SuggestResultIn"])).optional()}
    ).named(renames["SuggestResponseIn"])
    types["SuggestResponseOut"] = t.struct(
        {
            "suggestResults": t.array(t.proxy(renames["SuggestResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestResponseOut"])
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
    types["AppsDynamiteSharedAssistantSuggestionIn"] = t.struct(
        {
            "debugContext": t.proxy(
                renames["AppsDynamiteSharedAssistantDebugContextIn"]
            ).optional(),
            "feedbackContext": t.proxy(
                renames["AppsDynamiteSharedAssistantFeedbackContextIn"]
            ).optional(),
            "serializedSuggestions": t.string().optional(),
            "findDocumentSuggestion": t.proxy(
                renames["AppsDynamiteSharedFindDocumentSuggestionIn"]
            ).optional(),
            "sessionContext": t.proxy(
                renames["AppsDynamiteSharedAssistantSessionContextIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSuggestionIn"])
    types["AppsDynamiteSharedAssistantSuggestionOut"] = t.struct(
        {
            "debugContext": t.proxy(
                renames["AppsDynamiteSharedAssistantDebugContextOut"]
            ).optional(),
            "feedbackContext": t.proxy(
                renames["AppsDynamiteSharedAssistantFeedbackContextOut"]
            ).optional(),
            "serializedSuggestions": t.string().optional(),
            "findDocumentSuggestion": t.proxy(
                renames["AppsDynamiteSharedFindDocumentSuggestionOut"]
            ).optional(),
            "sessionContext": t.proxy(
                renames["AppsDynamiteSharedAssistantSessionContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantSuggestionOut"])
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
    types["BotInfoIn"] = t.struct(
        {
            "supportUrls": t.proxy(renames["SupportUrlsIn"]).optional(),
            "supportHomeScreen": t.boolean().optional(),
            "developerName": t.string().optional(),
            "appAllowlistStatus": t.string(),
            "status": t.string().optional(),
            "botName": t.string().optional(),
            "marketPlaceBannerUrl": t.string().optional(),
            "botAvatarUrl": t.string().optional(),
            "description": t.string().optional(),
            "appId": t.proxy(renames["AppIdIn"]).optional(),
            "supportedUses": t.array(t.string()).optional(),
        }
    ).named(renames["BotInfoIn"])
    types["BotInfoOut"] = t.struct(
        {
            "supportUrls": t.proxy(renames["SupportUrlsOut"]).optional(),
            "supportHomeScreen": t.boolean().optional(),
            "developerName": t.string().optional(),
            "appAllowlistStatus": t.string(),
            "status": t.string().optional(),
            "botName": t.string().optional(),
            "marketPlaceBannerUrl": t.string().optional(),
            "botAvatarUrl": t.string().optional(),
            "description": t.string().optional(),
            "appId": t.proxy(renames["AppIdOut"]).optional(),
            "supportedUses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BotInfoOut"])
    types["OnClickIn"] = t.struct(
        {
            "action": t.proxy(renames["FormActionIn"]),
            "openLinkAction": t.proxy(renames["FormActionIn"]).optional(),
            "openLink": t.proxy(renames["OpenLinkIn"]),
            "link": t.string().optional(),
        }
    ).named(renames["OnClickIn"])
    types["OnClickOut"] = t.struct(
        {
            "action": t.proxy(renames["FormActionOut"]),
            "openLinkAction": t.proxy(renames["FormActionOut"]).optional(),
            "openLink": t.proxy(renames["OpenLinkOut"]),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnClickOut"])
    types["SpellResultIn"] = t.struct({"suggestedQuery": t.string().optional()}).named(
        renames["SpellResultIn"]
    )
    types["SpellResultOut"] = t.struct(
        {
            "suggestedQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpellResultOut"])
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
    types["LdapGroupProtoIn"] = t.struct({"groupName": t.string()}).named(
        renames["LdapGroupProtoIn"]
    )
    types["LdapGroupProtoOut"] = t.struct(
        {"groupName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LdapGroupProtoOut"])
    types["AppsDynamiteSharedPhoneNumberIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string().optional()}
    ).named(renames["AppsDynamiteSharedPhoneNumberIn"])
    types["AppsDynamiteSharedPhoneNumberOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedPhoneNumberOut"])
    types["ResourceRoleProtoIn"] = t.struct(
        {
            "roleId": t.integer(),
            "objectId": t.string(),
            "objectPart": t.string(),
            "applicationId": t.string(),
        }
    ).named(renames["ResourceRoleProtoIn"])
    types["ResourceRoleProtoOut"] = t.struct(
        {
            "roleId": t.integer(),
            "objectId": t.string(),
            "objectPart": t.string(),
            "applicationId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRoleProtoOut"])
    types["HistoryRecordIn"] = t.struct(
        {
            "type": t.string(),
            "threadUpdate": t.proxy(renames["ThreadUpdateIn"]),
            "transactionContext": t.proxy(renames["TransactionContextIn"]).optional(),
            "labelUpdate": t.proxy(renames["LabelUpdateIn"]),
            "txnDebugInfo": t.proxy(renames["TransactionDebugInfoIn"]),
            "prefUpdate": t.proxy(renames["PrefUpdateIn"]),
            "clientContext": t.proxy(renames["ClientContextIn"]).optional(),
            "recordId": t.string().optional(),
            "imapUpdate": t.proxy(renames["ImapUpdateIn"]),
            "filterUpdate": t.proxy(renames["FilterUpdateIn"]),
        }
    ).named(renames["HistoryRecordIn"])
    types["HistoryRecordOut"] = t.struct(
        {
            "type": t.string(),
            "threadUpdate": t.proxy(renames["ThreadUpdateOut"]),
            "transactionContext": t.proxy(renames["TransactionContextOut"]).optional(),
            "labelUpdate": t.proxy(renames["LabelUpdateOut"]),
            "txnDebugInfo": t.proxy(renames["TransactionDebugInfoOut"]),
            "prefUpdate": t.proxy(renames["PrefUpdateOut"]),
            "clientContext": t.proxy(renames["ClientContextOut"]).optional(),
            "recordId": t.string().optional(),
            "imapUpdate": t.proxy(renames["ImapUpdateOut"]),
            "filterUpdate": t.proxy(renames["FilterUpdateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryRecordOut"])
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
    types["TextButtonIn"] = t.struct(
        {
            "style": t.string(),
            "disabled": t.boolean(),
            "text": t.string().optional(),
            "altText": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]),
        }
    ).named(renames["TextButtonIn"])
    types["TextButtonOut"] = t.struct(
        {
            "style": t.string(),
            "disabled": t.boolean(),
            "text": t.string().optional(),
            "altText": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextButtonOut"])
    types["CheckAccessResponseIn"] = t.struct(
        {"hasAccess": t.boolean().optional()}
    ).named(renames["CheckAccessResponseIn"])
    types["CheckAccessResponseOut"] = t.struct(
        {
            "hasAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckAccessResponseOut"])
    types["FuseboxItemThreadMatchInfoIn"] = t.struct(
        {
            "rank": t.proxy(renames["RankIn"]).optional(),
            "lastMatchingItemKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "lastMatchingItemId": t.string().optional(),
            "matchingItemKey": t.array(t.proxy(renames["MultiKeyIn"])).optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["FuseboxItemThreadMatchInfoIn"])
    types["FuseboxItemThreadMatchInfoOut"] = t.struct(
        {
            "rank": t.proxy(renames["RankOut"]).optional(),
            "lastMatchingItemKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "lastMatchingItemId": t.string().optional(),
            "matchingItemKey": t.array(t.proxy(renames["MultiKeyOut"])).optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FuseboxItemThreadMatchInfoOut"])
    types["BabelMessagePropsIn"] = t.struct(
        {
            "wasUpdatedByBackfill": t.boolean().optional(),
            "messageContent": t.proxy(
                renames["ChatConserverMessageContentIn"]
            ).optional(),
            "contentExtension": t.proxy(renames["ChatContentExtensionIn"]).optional(),
            "deliveryMedium": t.proxy(renames["DeliveryMediumIn"]).optional(),
            "eventId": t.string().optional(),
            "clientGeneratedId": t.string().optional(),
        }
    ).named(renames["BabelMessagePropsIn"])
    types["BabelMessagePropsOut"] = t.struct(
        {
            "wasUpdatedByBackfill": t.boolean().optional(),
            "messageContent": t.proxy(
                renames["ChatConserverMessageContentOut"]
            ).optional(),
            "contentExtension": t.proxy(renames["ChatContentExtensionOut"]).optional(),
            "deliveryMedium": t.proxy(renames["DeliveryMediumOut"]).optional(),
            "eventId": t.string().optional(),
            "clientGeneratedId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BabelMessagePropsOut"])
    types["OpenLinkIn"] = t.struct(
        {
            "url": t.string(),
            "openAs": t.string(),
            "onClose": t.string(),
            "loadIndicator": t.string().optional(),
        }
    ).named(renames["OpenLinkIn"])
    types["OpenLinkOut"] = t.struct(
        {
            "url": t.string(),
            "openAs": t.string(),
            "onClose": t.string(),
            "loadIndicator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenLinkOut"])
    types["InteractionDataIn"] = t.struct(
        {"url": t.proxy(renames["SafeUrlProtoIn"]).optional()}
    ).named(renames["InteractionDataIn"])
    types["InteractionDataOut"] = t.struct(
        {
            "url": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InteractionDataOut"])
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
    types["AppsDynamiteStorageCardIn"] = t.struct(
        {
            "name": t.string().optional(),
            "cardActions": t.array(
                t.proxy(renames["AppsDynamiteStorageCardCardActionIn"])
            ).optional(),
            "sections": t.array(
                t.proxy(renames["AppsDynamiteStorageCardSectionIn"])
            ).optional(),
            "header": t.proxy(
                renames["AppsDynamiteStorageCardCardHeaderIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardIn"])
    types["AppsDynamiteStorageCardOut"] = t.struct(
        {
            "name": t.string().optional(),
            "cardActions": t.array(
                t.proxy(renames["AppsDynamiteStorageCardCardActionOut"])
            ).optional(),
            "sections": t.array(
                t.proxy(renames["AppsDynamiteStorageCardSectionOut"])
            ).optional(),
            "header": t.proxy(
                renames["AppsDynamiteStorageCardCardHeaderOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardOut"])
    types["PrefWrittenIn"] = t.struct({"value": t.string()}).named(
        renames["PrefWrittenIn"]
    )
    types["PrefWrittenOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PrefWrittenOut"])
    types["AppsDynamiteSharedBackendUploadMetadataIn"] = t.struct(
        {
            "isClientSideTranscodedVideo": t.boolean().optional(),
            "contentSize": t.string().optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryIn"]).optional(),
            "uploadTimestampUsec": t.string().optional(),
            "sha256": t.string().optional(),
            "videoThumbnailBlobId": t.string().optional(),
            "groupId": t.proxy(renames["GroupIdIn"]).optional(),
            "videoId": t.string().optional(),
            "quoteReplyMessageId": t.proxy(renames["MessageIdIn"]).optional(),
            "contentType": t.string().optional(),
            "dlpScanOutcome": t.string().optional(),
            "contentName": t.string().optional(),
            "uploadIp": t.string().optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionIn"]
            ).optional(),
            "virusScanResult": t.string().optional(),
            "blobPath": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedBackendUploadMetadataIn"])
    types["AppsDynamiteSharedBackendUploadMetadataOut"] = t.struct(
        {
            "isClientSideTranscodedVideo": t.boolean().optional(),
            "contentSize": t.string().optional(),
            "dlpScanSummary": t.proxy(renames["DlpScanSummaryOut"]).optional(),
            "uploadTimestampUsec": t.string().optional(),
            "sha256": t.string().optional(),
            "videoThumbnailBlobId": t.string().optional(),
            "groupId": t.proxy(renames["GroupIdOut"]).optional(),
            "videoId": t.string().optional(),
            "quoteReplyMessageId": t.proxy(renames["MessageIdOut"]).optional(),
            "contentType": t.string().optional(),
            "dlpScanOutcome": t.string().optional(),
            "contentName": t.string().optional(),
            "uploadIp": t.string().optional(),
            "originalDimension": t.proxy(
                renames["AppsDynamiteSharedDimensionOut"]
            ).optional(),
            "virusScanResult": t.string().optional(),
            "blobPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedBackendUploadMetadataOut"])
    types["PrincipalIn"] = t.struct(
        {
            "userResourceName": t.string().optional(),
            "gsuitePrincipal": t.proxy(renames["GSuitePrincipalIn"]).optional(),
            "groupResourceName": t.string().optional(),
        }
    ).named(renames["PrincipalIn"])
    types["PrincipalOut"] = t.struct(
        {
            "userResourceName": t.string().optional(),
            "gsuitePrincipal": t.proxy(renames["GSuitePrincipalOut"]).optional(),
            "groupResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrincipalOut"])
    types["HangoutEventIn"] = t.struct(
        {
            "mediaType": t.string(),
            "type": t.string(),
            "hangoutDurationSecs": t.string(),
            "participantId": t.array(t.proxy(renames["StoredParticipantIdIn"])),
        }
    ).named(renames["HangoutEventIn"])
    types["HangoutEventOut"] = t.struct(
        {
            "mediaType": t.string(),
            "type": t.string(),
            "hangoutDurationSecs": t.string(),
            "participantId": t.array(t.proxy(renames["StoredParticipantIdOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutEventOut"])
    types["GsuiteIntegrationMetadataIn"] = t.struct(
        {
            "clientType": t.string(),
            "callData": t.proxy(
                renames["AppsDynamiteSharedCallAnnotationDataIn"]
            ).optional(),
            "tasksData": t.proxy(renames["AppsDynamiteSharedTasksAnnotationDataIn"]),
            "indexableTexts": t.array(t.string()).optional(),
            "assistantData": t.proxy(
                renames["AppsDynamiteSharedAssistantAnnotationDataIn"]
            ),
            "calendarEventData": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataIn"]
            ),
            "activityFeedData": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataIn"]
            ),
        }
    ).named(renames["GsuiteIntegrationMetadataIn"])
    types["GsuiteIntegrationMetadataOut"] = t.struct(
        {
            "clientType": t.string(),
            "callData": t.proxy(
                renames["AppsDynamiteSharedCallAnnotationDataOut"]
            ).optional(),
            "tasksData": t.proxy(renames["AppsDynamiteSharedTasksAnnotationDataOut"]),
            "indexableTexts": t.array(t.string()).optional(),
            "assistantData": t.proxy(
                renames["AppsDynamiteSharedAssistantAnnotationDataOut"]
            ),
            "calendarEventData": t.proxy(
                renames["AppsDynamiteSharedCalendarEventAnnotationDataOut"]
            ),
            "activityFeedData": t.proxy(
                renames["AppsDynamiteSharedActivityFeedAnnotationDataOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GsuiteIntegrationMetadataOut"])
    types["DriveLocationRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveLocationRestrictIn"]
    )
    types["DriveLocationRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveLocationRestrictOut"])
    types["InsertContentIn"] = t.struct(
        {
            "mimeType": t.string(),
            "contentType": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["InsertContentIn"])
    types["InsertContentOut"] = t.struct(
        {
            "mimeType": t.string(),
            "contentType": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsertContentOut"])
    types["AuditLoggingSettingsIn"] = t.struct(
        {
            "logAdminReadActions": t.boolean().optional(),
            "project": t.string().optional(),
            "logDataReadActions": t.boolean().optional(),
            "logDataWriteActions": t.boolean().optional(),
        }
    ).named(renames["AuditLoggingSettingsIn"])
    types["AuditLoggingSettingsOut"] = t.struct(
        {
            "logAdminReadActions": t.boolean().optional(),
            "project": t.string().optional(),
            "logDataReadActions": t.boolean().optional(),
            "logDataWriteActions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLoggingSettingsOut"])
    types["UpdateDraftActionMarkupIn"] = t.struct(
        {
            "updateBody": t.proxy(renames["UpdateBodyIn"]).optional(),
            "updateSubject": t.proxy(renames["UpdateSubjectIn"]).optional(),
            "updateBccRecipients": t.proxy(renames["UpdateBccRecipientsIn"]).optional(),
            "updateCcRecipients": t.proxy(renames["UpdateCcRecipientsIn"]).optional(),
            "updateToRecipients": t.proxy(renames["UpdateToRecipientsIn"]).optional(),
        }
    ).named(renames["UpdateDraftActionMarkupIn"])
    types["UpdateDraftActionMarkupOut"] = t.struct(
        {
            "updateBody": t.proxy(renames["UpdateBodyOut"]).optional(),
            "updateSubject": t.proxy(renames["UpdateSubjectOut"]).optional(),
            "updateBccRecipients": t.proxy(
                renames["UpdateBccRecipientsOut"]
            ).optional(),
            "updateCcRecipients": t.proxy(renames["UpdateCcRecipientsOut"]).optional(),
            "updateToRecipients": t.proxy(renames["UpdateToRecipientsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDraftActionMarkupOut"])
    types["ListItemsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemIn"])),
        }
    ).named(renames["ListItemsResponseIn"])
    types["ListItemsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemsResponseOut"])
    types["StoredParticipantIdIn"] = t.struct({"gaiaId": t.string()}).named(
        renames["StoredParticipantIdIn"]
    )
    types["StoredParticipantIdOut"] = t.struct(
        {"gaiaId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StoredParticipantIdOut"])
    types["EnumPropertyOptionsIn"] = t.struct(
        {
            "possibleValues": t.array(t.proxy(renames["EnumValuePairIn"])).optional(),
            "orderedRanking": t.string().optional(),
            "operatorOptions": t.proxy(renames["EnumOperatorOptionsIn"]).optional(),
        }
    ).named(renames["EnumPropertyOptionsIn"])
    types["EnumPropertyOptionsOut"] = t.struct(
        {
            "possibleValues": t.array(t.proxy(renames["EnumValuePairOut"])).optional(),
            "orderedRanking": t.string().optional(),
            "operatorOptions": t.proxy(renames["EnumOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumPropertyOptionsOut"])
    types["AppsDynamiteStorageCardSectionIn"] = t.struct(
        {
            "header": t.string().optional(),
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageWidgetIn"])
            ).optional(),
            "collapsible": t.boolean().optional(),
        }
    ).named(renames["AppsDynamiteStorageCardSectionIn"])
    types["AppsDynamiteStorageCardSectionOut"] = t.struct(
        {
            "header": t.string().optional(),
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "widgets": t.array(
                t.proxy(renames["AppsDynamiteStorageWidgetOut"])
            ).optional(),
            "collapsible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageCardSectionOut"])
    types["RecordingEventIn"] = t.struct(
        {"type": t.string().optional(), "deviceId": t.string().optional()}
    ).named(renames["RecordingEventIn"])
    types["RecordingEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordingEventOut"])
    types["AttributeSetIn"] = t.struct(
        {
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
            "attributeValue": t.string().optional(),
            "attributeId": t.string(),
        }
    ).named(renames["AttributeSetIn"])
    types["AttributeSetOut"] = t.struct(
        {
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "attributeValue": t.string().optional(),
            "attributeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeSetOut"])
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
    types["TypeInfoIn"] = t.struct(
        {"videoInfo": t.proxy(renames["VideoInfoIn"]).optional()}
    ).named(renames["TypeInfoIn"])
    types["TypeInfoOut"] = t.struct(
        {
            "videoInfo": t.proxy(renames["VideoInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeInfoOut"])
    types["SlashCommandMetadataIn"] = t.struct(
        {
            "argumentsHint": t.string().optional(),
            "commandName": t.string().optional(),
            "commandId": t.string().optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
            "triggersDialog": t.boolean().optional(),
            "type": t.string(),
        }
    ).named(renames["SlashCommandMetadataIn"])
    types["SlashCommandMetadataOut"] = t.struct(
        {
            "argumentsHint": t.string().optional(),
            "commandName": t.string().optional(),
            "commandId": t.string().optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "triggersDialog": t.boolean().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandMetadataOut"])
    types["TextFieldIn"] = t.struct(
        {
            "autoCompleteMultipleSelections": t.boolean().optional(),
            "onChange": t.proxy(renames["FormActionIn"]),
            "autoComplete": t.proxy(renames["AutoCompleteIn"]).optional(),
            "hintText": t.string(),
            "value": t.string().optional(),
            "label": t.string().optional(),
            "type": t.string(),
            "maxLines": t.integer(),
            "name": t.string().optional(),
            "autoCompleteCallback": t.proxy(renames["FormActionIn"]).optional(),
        }
    ).named(renames["TextFieldIn"])
    types["TextFieldOut"] = t.struct(
        {
            "autoCompleteMultipleSelections": t.boolean().optional(),
            "onChange": t.proxy(renames["FormActionOut"]),
            "autoComplete": t.proxy(renames["AutoCompleteOut"]).optional(),
            "hintText": t.string(),
            "value": t.string().optional(),
            "label": t.string().optional(),
            "type": t.string(),
            "maxLines": t.integer(),
            "name": t.string().optional(),
            "autoCompleteCallback": t.proxy(renames["FormActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextFieldOut"])
    types["QuerySuggestionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["QuerySuggestionIn"]
    )
    types["QuerySuggestionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QuerySuggestionOut"])
    types["EnumOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["EnumOperatorOptionsIn"])
    types["EnumOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOperatorOptionsOut"])
    types["UserInfoIn"] = t.struct(
        {
            "updaterCountDisplayType": t.string().optional(),
            "updaterToShowEmail": t.string().optional(),
            "updaterToShowGaiaId": t.string().optional(),
            "updaterToShowUserId": t.proxy(renames["UserIdIn"]).optional(),
            "driveNotificationAvatarUrl": t.string().optional(),
            "updaterCountToShow": t.integer().optional(),
            "updaterToShowName": t.string().optional(),
        }
    ).named(renames["UserInfoIn"])
    types["UserInfoOut"] = t.struct(
        {
            "updaterCountDisplayType": t.string().optional(),
            "updaterToShowEmail": t.string().optional(),
            "updaterToShowGaiaId": t.string().optional(),
            "updaterToShowUserId": t.proxy(renames["UserIdOut"]).optional(),
            "driveNotificationAvatarUrl": t.string().optional(),
            "updaterCountToShow": t.integer().optional(),
            "updaterToShowName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
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
    types["SelectionControlIn"] = t.struct(
        {
            "type": t.string(),
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "items": t.array(t.proxy(renames["SelectionItemIn"])).optional(),
        }
    ).named(renames["SelectionControlIn"])
    types["SelectionControlOut"] = t.struct(
        {
            "type": t.string(),
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "items": t.array(t.proxy(renames["SelectionItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionControlOut"])
    types["CustomerQueryStatsIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusIn"])),
        }
    ).named(renames["CustomerQueryStatsIn"])
    types["CustomerQueryStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerQueryStatsOut"])
    types["AppsDynamiteStorageColumnsColumnWidgetsIn"] = t.struct(
        {
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerIn"]
            ).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListIn"]
            ).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputIn"]).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextIn"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageIn"]).optional(),
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputIn"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnWidgetsIn"])
    types["AppsDynamiteStorageColumnsColumnWidgetsOut"] = t.struct(
        {
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerOut"]
            ).optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListOut"]
            ).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputOut"]).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextOut"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageOut"]).optional(),
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputOut"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageColumnsColumnWidgetsOut"])
    types["ItemThreadIn"] = t.struct(
        {
            "topicState": t.proxy(renames["TopicStateIn"]).optional(),
            "snippet": t.string().optional(),
            "lastItemId": t.string().optional(),
            "threadLocator": t.string().optional(),
            "clusterInfo": t.proxy(renames["ClusterInfoIn"]),
            "item": t.array(t.proxy(renames["FuseboxItemIn"])).optional(),
            "threadKey": t.proxy(renames["MultiKeyIn"]).optional(),
            "matchInfo": t.proxy(renames["FuseboxItemThreadMatchInfoIn"]),
            "version": t.string().optional(),
        }
    ).named(renames["ItemThreadIn"])
    types["ItemThreadOut"] = t.struct(
        {
            "topicState": t.proxy(renames["TopicStateOut"]).optional(),
            "snippet": t.string().optional(),
            "lastItemId": t.string().optional(),
            "threadLocator": t.string().optional(),
            "clusterInfo": t.proxy(renames["ClusterInfoOut"]),
            "item": t.array(t.proxy(renames["FuseboxItemOut"])).optional(),
            "threadKey": t.proxy(renames["MultiKeyOut"]).optional(),
            "matchInfo": t.proxy(renames["FuseboxItemThreadMatchInfoOut"]),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemThreadOut"])
    types["AppsDynamiteStorageTextInputIn"] = t.struct(
        {
            "type": t.string().optional(),
            "autoCompleteAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
            "initialSuggestions": t.proxy(
                renames["AppsDynamiteStorageSuggestionsIn"]
            ).optional(),
            "value": t.string().optional(),
            "label": t.string().optional(),
            "name": t.string().optional(),
            "hintText": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageTextInputIn"])
    types["AppsDynamiteStorageTextInputOut"] = t.struct(
        {
            "type": t.string().optional(),
            "autoCompleteAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "onChangeAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "initialSuggestions": t.proxy(
                renames["AppsDynamiteStorageSuggestionsOut"]
            ).optional(),
            "value": t.string().optional(),
            "label": t.string().optional(),
            "name": t.string().optional(),
            "hintText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageTextInputOut"])
    types["ImapsyncFolderAttributeFolderMessageFlagsIn"] = t.struct(
        {"seen": t.boolean().optional(), "flagged": t.boolean().optional()}
    ).named(renames["ImapsyncFolderAttributeFolderMessageFlagsIn"])
    types["ImapsyncFolderAttributeFolderMessageFlagsOut"] = t.struct(
        {
            "seen": t.boolean().optional(),
            "flagged": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapsyncFolderAttributeFolderMessageFlagsOut"])
    types["SearchQualityMetadataIn"] = t.struct(
        {"quality": t.number().optional()}
    ).named(renames["SearchQualityMetadataIn"])
    types["SearchQualityMetadataOut"] = t.struct(
        {
            "quality": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchQualityMetadataOut"])
    types["AckInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AckInfoIn"]
    )
    types["AckInfoOut"] = t.struct(
        {
            "unackedDeviceIds": t.array(t.string()).optional(),
            "unackedDeviceCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AckInfoOut"])
    types["LabelCreatedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LabelCreatedIn"]
    )
    types["LabelCreatedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LabelCreatedOut"])
    types["GaiaUserProtoIn"] = t.struct({"userId": t.string()}).named(
        renames["GaiaUserProtoIn"]
    )
    types["GaiaUserProtoOut"] = t.struct(
        {"userId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GaiaUserProtoOut"])
    types["BooleanOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["BooleanOperatorOptionsIn"])
    types["BooleanOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanOperatorOptionsOut"])
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
    types["AppsDynamiteStorageGridGridItemIn"] = t.struct(
        {
            "layout": t.string().optional(),
            "subtitle": t.string().optional(),
            "textAlignment": t.string().optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageComponentIn"]).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageGridGridItemIn"])
    types["AppsDynamiteStorageGridGridItemOut"] = t.struct(
        {
            "layout": t.string().optional(),
            "subtitle": t.string().optional(),
            "textAlignment": t.string().optional(),
            "image": t.proxy(
                renames["AppsDynamiteStorageImageComponentOut"]
            ).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageGridGridItemOut"])
    types["ListDataSourceResponseIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["DataSourceIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDataSourceResponseIn"])
    types["ListDataSourceResponseOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["DataSourceOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataSourceResponseOut"])
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
    types["IntegerOperatorOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
        }
    ).named(renames["IntegerOperatorOptionsIn"])
    types["IntegerOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerOperatorOptionsOut"])
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
    types["UpdateToRecipientsIn"] = t.struct(
        {"toRecipients": t.array(t.proxy(renames["RecipientIn"]))}
    ).named(renames["UpdateToRecipientsIn"])
    types["UpdateToRecipientsOut"] = t.struct(
        {
            "toRecipients": t.array(t.proxy(renames["RecipientOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateToRecipientsOut"])
    types["AppsDynamiteStorageSuggestionsSuggestionItemIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["AppsDynamiteStorageSuggestionsSuggestionItemIn"])
    types["AppsDynamiteStorageSuggestionsSuggestionItemOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteStorageSuggestionsSuggestionItemOut"])
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
    types["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"])
    types[
        "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"]
    )
    types["PhoneAccessIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "formattedPhoneNumber": t.string().optional(),
            "pin": t.string().optional(),
        }
    ).named(renames["PhoneAccessIn"])
    types["PhoneAccessOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "formattedPhoneNumber": t.string().optional(),
            "pin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneAccessOut"])
    types["AppsDynamiteSharedTextWithDescriptionIn"] = t.struct(
        {
            "textBody": t.string(),
            "textSegmentsWithDescription": t.array(
                t.proxy(renames["AppsDynamiteSharedTextSegmentsWithDescriptionIn"])
            ),
        }
    ).named(renames["AppsDynamiteSharedTextWithDescriptionIn"])
    types["AppsDynamiteSharedTextWithDescriptionOut"] = t.struct(
        {
            "textBody": t.string(),
            "textSegmentsWithDescription": t.array(
                t.proxy(renames["AppsDynamiteSharedTextSegmentsWithDescriptionOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTextWithDescriptionOut"])
    types["GoogleDocsMetadataIn"] = t.struct(
        {
            "typeInfo": t.proxy(renames["TypeInfoIn"]).optional(),
            "documentType": t.string().optional(),
            "aclInfo": t.proxy(renames["AclInfoIn"]).optional(),
            "lastContentModifiedTimestamp": t.string().optional(),
            "resultInfo": t.proxy(renames["GoogleDocsResultInfoIn"]).optional(),
            "numSubscribers": t.integer().optional(),
            "fileExtension": t.string().optional(),
            "numViewers": t.integer().optional(),
        }
    ).named(renames["GoogleDocsMetadataIn"])
    types["GoogleDocsMetadataOut"] = t.struct(
        {
            "typeInfo": t.proxy(renames["TypeInfoOut"]).optional(),
            "documentType": t.string().optional(),
            "aclInfo": t.proxy(renames["AclInfoOut"]).optional(),
            "lastContentModifiedTimestamp": t.string().optional(),
            "resultInfo": t.proxy(renames["GoogleDocsResultInfoOut"]).optional(),
            "numSubscribers": t.integer().optional(),
            "fileExtension": t.string().optional(),
            "numViewers": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDocsMetadataOut"])
    types["DateTimePickerIn"] = t.struct(
        {
            "onChange": t.proxy(renames["FormActionIn"]).optional(),
            "valueMsEpoch": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "label": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
        }
    ).named(renames["DateTimePickerIn"])
    types["DateTimePickerOut"] = t.struct(
        {
            "onChange": t.proxy(renames["FormActionOut"]).optional(),
            "valueMsEpoch": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "label": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimePickerOut"])
    types["CustomerSettingsIn"] = t.struct(
        {
            "auditLoggingSettings": t.proxy(
                renames["AuditLoggingSettingsIn"]
            ).optional(),
            "vpcSettings": t.proxy(renames["VPCSettingsIn"]).optional(),
        }
    ).named(renames["CustomerSettingsIn"])
    types["CustomerSettingsOut"] = t.struct(
        {
            "auditLoggingSettings": t.proxy(
                renames["AuditLoggingSettingsOut"]
            ).optional(),
            "vpcSettings": t.proxy(renames["VPCSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerSettingsOut"])
    types["DividerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DividerIn"]
    )
    types["DividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DividerOut"])
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
    types["YouTubeBroadcastStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["YouTubeBroadcastStatsIn"])
    types["YouTubeBroadcastStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeBroadcastStatsOut"])
    types["ClientContextIn"] = t.struct(
        {
            "clientOperationId": t.string().optional(),
            "clientType": t.string().optional(),
            "sessionContext": t.proxy(renames["SessionContextIn"]).optional(),
            "userIp": t.string().optional(),
        }
    ).named(renames["ClientContextIn"])
    types["ClientContextOut"] = t.struct(
        {
            "clientOperationId": t.string().optional(),
            "clientType": t.string().optional(),
            "sessionContext": t.proxy(renames["SessionContextOut"]).optional(),
            "userIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientContextOut"])
    types["CustomerUserStatsIn"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
        }
    ).named(renames["CustomerUserStatsIn"])
    types["CustomerUserStatsOut"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerUserStatsOut"])
    types["SettingsIn"] = t.struct(
        {
            "chatLock": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "accessType": t.string().optional(),
            "cseEnabled": t.boolean().optional(),
            "accessLock": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "defaultAsViewer": t.boolean().optional(),
            "cohostArtifactSharingEnabled": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "chatLock": t.boolean().optional(),
            "presentLock": t.boolean().optional(),
            "moderationEnabled": t.boolean().optional(),
            "accessType": t.string().optional(),
            "cseEnabled": t.boolean().optional(),
            "accessLock": t.boolean().optional(),
            "reactionsLock": t.boolean().optional(),
            "defaultAsViewer": t.boolean().optional(),
            "cohostArtifactSharingEnabled": t.boolean().optional(),
            "attendanceReportEnabled": t.boolean().optional(),
            "allowJoiningBeforeHost": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
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
    types["SearchApplicationIn"] = t.struct(
        {
            "enableAuditLog": t.boolean().optional(),
            "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
            "displayName": t.string().optional(),
            "defaultFacetOptions": t.array(
                t.proxy(renames["FacetOptionsIn"])
            ).optional(),
            "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
            "queryInterpretationConfig": t.proxy(
                renames["QueryInterpretationConfigIn"]
            ).optional(),
            "returnResultThumbnailUrls": t.boolean().optional(),
            "name": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
        }
    ).named(renames["SearchApplicationIn"])
    types["SearchApplicationOut"] = t.struct(
        {
            "enableAuditLog": t.boolean().optional(),
            "operationIds": t.array(t.string()).optional(),
            "defaultSortOptions": t.proxy(renames["SortOptionsOut"]).optional(),
            "displayName": t.string().optional(),
            "defaultFacetOptions": t.array(
                t.proxy(renames["FacetOptionsOut"])
            ).optional(),
            "scoringConfig": t.proxy(renames["ScoringConfigOut"]).optional(),
            "queryInterpretationConfig": t.proxy(
                renames["QueryInterpretationConfigOut"]
            ).optional(),
            "returnResultThumbnailUrls": t.boolean().optional(),
            "name": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "sourceConfig": t.array(t.proxy(renames["SourceConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationOut"])
    types["GetCustomerSessionStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["CustomerSessionStatsIn"]))}
    ).named(renames["GetCustomerSessionStatsResponseIn"])
    types["GetCustomerSessionStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerSessionStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerSessionStatsResponseOut"])
    types["HangoutVideoEventMetadataIn"] = t.struct(
        {"hangoutVideoType": t.string()}
    ).named(renames["HangoutVideoEventMetadataIn"])
    types["HangoutVideoEventMetadataOut"] = t.struct(
        {
            "hangoutVideoType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutVideoEventMetadataOut"])
    types["FuseboxPrefUpdatePreStateIn"] = t.struct({"value": t.string()}).named(
        renames["FuseboxPrefUpdatePreStateIn"]
    )
    types["FuseboxPrefUpdatePreStateOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FuseboxPrefUpdatePreStateOut"])
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
    types["HtmlValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["HtmlValuesIn"]
    )
    types["HtmlValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlValuesOut"])
    types["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeIn"])
    types["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataCompletionChangeOut"])
    types["OtrChatMessageEventIn"] = t.struct(
        {
            "kansasVersionInfo": t.string(),
            "kansasRowId": t.string(),
            "expirationTimestampUsec": t.string(),
            "messageOtrStatus": t.string(),
        }
    ).named(renames["OtrChatMessageEventIn"])
    types["OtrChatMessageEventOut"] = t.struct(
        {
            "kansasVersionInfo": t.string(),
            "kansasRowId": t.string(),
            "expirationTimestampUsec": t.string(),
            "messageOtrStatus": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtrChatMessageEventOut"])
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
    types["AppsDynamiteStorageButtonListIn"] = t.struct(
        {"buttons": t.array(t.proxy(renames["AppsDynamiteStorageButtonIn"]))}
    ).named(renames["AppsDynamiteStorageButtonListIn"])
    types["AppsDynamiteStorageButtonListOut"] = t.struct(
        {
            "buttons": t.array(t.proxy(renames["AppsDynamiteStorageButtonOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageButtonListOut"])
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
    types[
        "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentIn"
    ] = t.struct(
        {
            "resourceUrl": t.string(),
            "iconUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "title": t.string().optional(),
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
            "resourceUrl": t.string(),
            "iconUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "AppsExtensionsMarkupCalendarClientActionMarkupAddAttachmentsActionMarkupAddonAttachmentOut"
        ]
    )
    types["AppsDynamiteStorageOnClickIn"] = t.struct(
        {
            "hostAppAction": t.proxy(renames["HostAppActionMarkupIn"]).optional(),
            "action": t.proxy(renames["AppsDynamiteStorageActionIn"]).optional(),
            "openLink": t.proxy(renames["AppsDynamiteStorageOpenLinkIn"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["AppsDynamiteStorageActionIn"]
            ).optional(),
        }
    ).named(renames["AppsDynamiteStorageOnClickIn"])
    types["AppsDynamiteStorageOnClickOut"] = t.struct(
        {
            "hostAppAction": t.proxy(renames["HostAppActionMarkupOut"]).optional(),
            "action": t.proxy(renames["AppsDynamiteStorageActionOut"]).optional(),
            "openLink": t.proxy(renames["AppsDynamiteStorageOpenLinkOut"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["AppsDynamiteStorageActionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageOnClickOut"])
    types["RecipientIn"] = t.struct({"email": t.string()}).named(renames["RecipientIn"])
    types["RecipientOut"] = t.struct(
        {"email": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RecipientOut"])
    types["ItemCountByStatusIn"] = t.struct(
        {
            "indexedItemsCount": t.string().optional(),
            "statusCode": t.string().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["ItemCountByStatusIn"])
    types["ItemCountByStatusOut"] = t.struct(
        {
            "indexedItemsCount": t.string().optional(),
            "statusCode": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemCountByStatusOut"])
    types["DatePropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["DateOperatorOptionsIn"]).optional()}
    ).named(renames["DatePropertyOptionsIn"])
    types["DatePropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["DateOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatePropertyOptionsOut"])
    types["AppsDynamiteSharedMessageIntegrationPayloadIn"] = t.struct(
        {
            "type": t.string().optional(),
            "tasksMessageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedTasksMessageIntegrationPayloadIn"]
            ),
            "projectNumber": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageIntegrationPayloadIn"])
    types["AppsDynamiteSharedMessageIntegrationPayloadOut"] = t.struct(
        {
            "type": t.string().optional(),
            "tasksMessageIntegrationPayload": t.proxy(
                renames["AppsDynamiteSharedTasksMessageIntegrationPayloadOut"]
            ),
            "projectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedMessageIntegrationPayloadOut"])
    types["RankIn"] = t.struct(
        {"primary": t.string().optional(), "secondary": t.string().optional()}
    ).named(renames["RankIn"])
    types["RankOut"] = t.struct(
        {
            "primary": t.string().optional(),
            "secondary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RankOut"])
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
    types["PushItemRequestIn"] = t.struct(
        {
            "item": t.proxy(renames["PushItemIn"]).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["PushItemRequestIn"])
    types["PushItemRequestOut"] = t.struct(
        {
            "item": t.proxy(renames["PushItemOut"]).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushItemRequestOut"])
    types["ItemAclIn"] = t.struct(
        {
            "owners": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "deniedReaders": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "aclInheritanceType": t.string().optional(),
            "readers": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "inheritAclFrom": t.string().optional(),
        }
    ).named(renames["ItemAclIn"])
    types["ItemAclOut"] = t.struct(
        {
            "owners": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "deniedReaders": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "aclInheritanceType": t.string().optional(),
            "readers": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "inheritAclFrom": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemAclOut"])
    types["AppsDynamiteStorageIconIn"] = t.struct(
        {
            "imageType": t.string().optional(),
            "iconUrl": t.string().optional(),
            "knownIcon": t.string().optional(),
            "materialIcon": t.proxy(
                renames["AppsDynamiteStorageMaterialIconIn"]
            ).optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["AppsDynamiteStorageIconIn"])
    types["AppsDynamiteStorageIconOut"] = t.struct(
        {
            "imageType": t.string().optional(),
            "iconUrl": t.string().optional(),
            "knownIcon": t.string().optional(),
            "materialIcon": t.proxy(
                renames["AppsDynamiteStorageMaterialIconOut"]
            ).optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageIconOut"])
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
    types["ChatConserverDynamitePlaceholderMetadataIn"] = t.struct(
        {
            "botMessageMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataBotMessageMetadataIn"]
            ),
            "videoCallMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataVideoCallMetadataIn"]
            ),
            "spaceUrl": t.string().optional(),
            "editMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataEditMetadataIn"]
            ),
            "deleteMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataIn"]
            ),
            "attachmentMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataIn"]
            ),
            "calendarEventMetadata": t.proxy(
                renames[
                    "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataIn"
                ]
            ),
            "tasksMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"]
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
            "spaceUrl": t.string().optional(),
            "editMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataEditMetadataOut"]
            ),
            "deleteMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataDeleteMetadataOut"]
            ),
            "attachmentMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataAttachmentMetadataOut"]
            ),
            "calendarEventMetadata": t.proxy(
                renames[
                    "ChatConserverDynamitePlaceholderMetadataCalendarEventMetadataOut"
                ]
            ),
            "tasksMetadata": t.proxy(
                renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatConserverDynamitePlaceholderMetadataOut"])
    types["IntegerValuesIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["IntegerValuesIn"]
    )
    types["IntegerValuesOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerValuesOut"])
    types["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventIn"] = t.struct(
        {
            "endTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn"
                ]
            ).optional(),
            "eventId": t.string().optional(),
            "startTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeIn"
                ]
            ).optional(),
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
            "eventId": t.string().optional(),
            "startTime": t.proxy(
                renames[
                    "AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTimeOut"
                ]
            ).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventOut"])
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
    types["AppsDynamiteV1ApiCompatV1ActionConfirmIn"] = t.struct(
        {
            "text": t.string().optional(),
            "dismiss_text": t.string().optional(),
            "ok_text": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionConfirmIn"])
    types["AppsDynamiteV1ApiCompatV1ActionConfirmOut"] = t.struct(
        {
            "text": t.string().optional(),
            "dismiss_text": t.string().optional(),
            "ok_text": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteV1ApiCompatV1ActionConfirmOut"])
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
    types["ItemPartsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ItemPartsIn"]
    )
    types["ItemPartsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ItemPartsOut"])
    types["HtmlPropertyOptionsIn"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["HtmlOperatorOptionsIn"]).optional(),
            "retrievalImportance": t.proxy(renames["RetrievalImportanceIn"]).optional(),
        }
    ).named(renames["HtmlPropertyOptionsIn"])
    types["HtmlPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["HtmlOperatorOptionsOut"]).optional(),
            "retrievalImportance": t.proxy(
                renames["RetrievalImportanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlPropertyOptionsOut"])
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
    types["PeopleSuggestionIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["PeopleSuggestionIn"])
    types["PeopleSuggestionOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeopleSuggestionOut"])
    types["QueryOperatorIn"] = t.struct(
        {
            "greaterThanOperatorName": t.string().optional(),
            "isRepeatable": t.boolean().optional(),
            "enumValues": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "operatorName": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "isReturnable": t.boolean().optional(),
            "lessThanOperatorName": t.string().optional(),
            "isSortable": t.boolean().optional(),
            "isSuggestable": t.boolean().optional(),
            "objectType": t.string().optional(),
        }
    ).named(renames["QueryOperatorIn"])
    types["QueryOperatorOut"] = t.struct(
        {
            "greaterThanOperatorName": t.string().optional(),
            "isRepeatable": t.boolean().optional(),
            "enumValues": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "operatorName": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "isReturnable": t.boolean().optional(),
            "lessThanOperatorName": t.string().optional(),
            "isSortable": t.boolean().optional(),
            "isSuggestable": t.boolean().optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOperatorOut"])
    types["PushItemIn"] = t.struct(
        {
            "structuredDataHash": t.string().optional(),
            "type": t.string().optional(),
            "queue": t.string().optional(),
            "payload": t.string().optional(),
            "repositoryError": t.proxy(renames["RepositoryErrorIn"]).optional(),
            "metadataHash": t.string().optional(),
            "contentHash": t.string().optional(),
        }
    ).named(renames["PushItemIn"])
    types["PushItemOut"] = t.struct(
        {
            "structuredDataHash": t.string().optional(),
            "type": t.string().optional(),
            "queue": t.string().optional(),
            "payload": t.string().optional(),
            "repositoryError": t.proxy(renames["RepositoryErrorOut"]).optional(),
            "metadataHash": t.string().optional(),
            "contentHash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushItemOut"])
    types["MediaIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["MediaIn"]
    )
    types["MediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["AttributesIn"] = t.struct(
        {"attribute": t.array(t.proxy(renames["AttributeIn"]))}
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "attribute": t.array(t.proxy(renames["AttributeOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])
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
    types["RosterIn"] = t.struct(
        {
            "rosterGaiaKey": t.string().optional(),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsIn"]
            ).optional(),
            "avatarUrl": t.string(),
            "rosterState": t.string().optional(),
            "name": t.string(),
            "membershipCount": t.integer(),
            "id": t.proxy(renames["RosterIdIn"]),
            "isMembershipVisibleToCaller": t.boolean().optional(),
        }
    ).named(renames["RosterIn"])
    types["RosterOut"] = t.struct(
        {
            "rosterGaiaKey": t.string().optional(),
            "segmentedMembershipCounts": t.proxy(
                renames["AppsDynamiteSharedSegmentedMembershipCountsOut"]
            ).optional(),
            "avatarUrl": t.string(),
            "rosterState": t.string().optional(),
            "name": t.string(),
            "membershipCount": t.integer(),
            "id": t.proxy(renames["RosterIdOut"]),
            "isMembershipVisibleToCaller": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RosterOut"])
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
    types["AppsDynamiteSharedCardClickSuggestionIn"] = t.struct(
        {
            "suggestionMessageId": t.proxy(renames["MessageIdIn"]).optional(),
            "actionId": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedCardClickSuggestionIn"])
    types["AppsDynamiteSharedCardClickSuggestionOut"] = t.struct(
        {
            "suggestionMessageId": t.proxy(renames["MessageIdOut"]).optional(),
            "actionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedCardClickSuggestionOut"])
    types["AppsDynamiteSharedSegmentedMembershipCountIn"] = t.struct(
        {
            "memberType": t.string(),
            "membershipCount": t.integer().optional(),
            "membershipState": t.string(),
        }
    ).named(renames["AppsDynamiteSharedSegmentedMembershipCountIn"])
    types["AppsDynamiteSharedSegmentedMembershipCountOut"] = t.struct(
        {
            "memberType": t.string(),
            "membershipCount": t.integer().optional(),
            "membershipState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedSegmentedMembershipCountOut"])
    types["UrlMetadataIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "urlSource": t.string(),
            "redirectUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "gwsUrlExpirationTimestamp": t.string().optional(),
            "snippet": t.string().optional(),
            "domain": t.string().optional(),
            "mimeType": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
            "intImageHeight": t.integer().optional(),
            "intImageWidth": t.integer().optional(),
            "gwsUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "imageWidth": t.string().optional(),
            "title": t.string().optional(),
            "url": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "imageHeight": t.string().optional(),
        }
    ).named(renames["UrlMetadataIn"])
    types["UrlMetadataOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "urlSource": t.string(),
            "redirectUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "gwsUrlExpirationTimestamp": t.string().optional(),
            "snippet": t.string().optional(),
            "domain": t.string().optional(),
            "mimeType": t.string().optional(),
            "shouldNotRender": t.boolean().optional(),
            "intImageHeight": t.integer().optional(),
            "intImageWidth": t.integer().optional(),
            "gwsUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "imageWidth": t.string().optional(),
            "title": t.string().optional(),
            "url": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "imageHeight": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlMetadataOut"])
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
    types["FacetResultIn"] = t.struct(
        {
            "sourceName": t.string().optional(),
            "operatorName": t.string().optional(),
            "objectType": t.string().optional(),
            "buckets": t.array(t.proxy(renames["FacetBucketIn"])).optional(),
        }
    ).named(renames["FacetResultIn"])
    types["FacetResultOut"] = t.struct(
        {
            "sourceName": t.string().optional(),
            "operatorName": t.string().optional(),
            "objectType": t.string().optional(),
            "buckets": t.array(t.proxy(renames["FacetBucketOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetResultOut"])
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
    types["FilterDeletedIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilterDeletedIn"]
    )
    types["FilterDeletedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FilterDeletedOut"])
    types["InitializeCustomerRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InitializeCustomerRequestIn"]
    )
    types["InitializeCustomerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InitializeCustomerRequestOut"])
    types["ContentReportJustificationIn"] = t.struct(
        {"userJustification": t.string().optional()}
    ).named(renames["ContentReportJustificationIn"])
    types["ContentReportJustificationOut"] = t.struct(
        {
            "userJustification": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentReportJustificationOut"])
    types["CloudPrincipalProtoIn"] = t.struct({"id": t.string().optional()}).named(
        renames["CloudPrincipalProtoIn"]
    )
    types["CloudPrincipalProtoOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudPrincipalProtoOut"])
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
    types["VideoCallMetadataIn"] = t.struct(
        {
            "shouldNotRender": t.boolean().optional(),
            "wasCreatedInCurrentGroup": t.boolean().optional(),
            "meetingSpace": t.proxy(renames["MeetingSpaceIn"]).optional(),
        }
    ).named(renames["VideoCallMetadataIn"])
    types["VideoCallMetadataOut"] = t.struct(
        {
            "shouldNotRender": t.boolean().optional(),
            "wasCreatedInCurrentGroup": t.boolean().optional(),
            "meetingSpace": t.proxy(renames["MeetingSpaceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoCallMetadataOut"])
    types["UserIdIn"] = t.struct(
        {
            "type": t.string().optional(),
            "actingUserId": t.string().optional(),
            "id": t.string().optional(),
            "originAppId": t.proxy(renames["AppIdIn"]).optional(),
        }
    ).named(renames["UserIdIn"])
    types["UserIdOut"] = t.struct(
        {
            "type": t.string().optional(),
            "actingUserId": t.string().optional(),
            "id": t.string().optional(),
            "originAppId": t.proxy(renames["AppIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserIdOut"])
    types["UserMentionMetadataIn"] = t.struct(
        {
            "userMentionError": t.string().optional(),
            "inviteeInfo": t.proxy(renames["InviteeInfoIn"]).optional(),
            "displayName": t.string().optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
            "type": t.string(),
            "gender": t.string().optional(),
        }
    ).named(renames["UserMentionMetadataIn"])
    types["UserMentionMetadataOut"] = t.struct(
        {
            "userMentionError": t.string().optional(),
            "inviteeInfo": t.proxy(renames["InviteeInfoOut"]).optional(),
            "displayName": t.string().optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "type": t.string(),
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserMentionMetadataOut"])
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
    types["UpdateDataSourceRequestIn"] = t.struct(
        {
            "source": t.proxy(renames["DataSourceIn"]),
            "updateMask": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestIn"])
    types["UpdateDataSourceRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["DataSourceOut"]),
            "updateMask": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestOut"])
    types["CseInfoIn"] = t.struct(
        {"cseDomain": t.string().optional(), "wrappedKey": t.string().optional()}
    ).named(renames["CseInfoIn"])
    types["CseInfoOut"] = t.struct(
        {
            "cseDomain": t.string().optional(),
            "wrappedKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CseInfoOut"])
    types["IndexItemRequestIn"] = t.struct(
        {
            "mode": t.string(),
            "indexItemOptions": t.proxy(renames["IndexItemOptionsIn"]),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "item": t.proxy(renames["ItemIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["IndexItemRequestIn"])
    types["IndexItemRequestOut"] = t.struct(
        {
            "mode": t.string(),
            "indexItemOptions": t.proxy(renames["IndexItemOptionsOut"]),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "item": t.proxy(renames["ItemOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexItemRequestOut"])
    types["PrefUpdateIn"] = t.struct(
        {
            "prefDeleted": t.proxy(renames["PrefDeletedIn"]),
            "name": t.string().optional(),
            "preState": t.proxy(renames["FuseboxPrefUpdatePreStateIn"]),
            "prefWritten": t.proxy(renames["PrefWrittenIn"]),
        }
    ).named(renames["PrefUpdateIn"])
    types["PrefUpdateOut"] = t.struct(
        {
            "prefDeleted": t.proxy(renames["PrefDeletedOut"]),
            "name": t.string().optional(),
            "preState": t.proxy(renames["FuseboxPrefUpdatePreStateOut"]),
            "prefWritten": t.proxy(renames["PrefWrittenOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrefUpdateOut"])
    types["IntegrationConfigMutationIn"] = t.struct(
        {
            "addPinnedItem": t.proxy(renames["PinnedItemIdIn"]).optional(),
            "removeApp": t.proxy(renames["AppIdIn"]).optional(),
            "removePinnedItem": t.proxy(renames["PinnedItemIdIn"]).optional(),
            "addApp": t.proxy(renames["AppIdIn"]).optional(),
        }
    ).named(renames["IntegrationConfigMutationIn"])
    types["IntegrationConfigMutationOut"] = t.struct(
        {
            "addPinnedItem": t.proxy(renames["PinnedItemIdOut"]).optional(),
            "removeApp": t.proxy(renames["AppIdOut"]).optional(),
            "removePinnedItem": t.proxy(renames["PinnedItemIdOut"]).optional(),
            "addApp": t.proxy(renames["AppIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegrationConfigMutationOut"])
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
    types["FilterIn"] = t.struct(
        {
            "compositeFilter": t.proxy(renames["CompositeFilterIn"]),
            "valueFilter": t.proxy(renames["ValueFilterIn"]),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "compositeFilter": t.proxy(renames["CompositeFilterOut"]),
            "valueFilter": t.proxy(renames["ValueFilterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["ImageIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]),
            "imageUrl": t.string().optional(),
            "aspectRatio": t.number().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]),
            "imageUrl": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["QueryItemIn"] = t.struct({"isSynthetic": t.boolean().optional()}).named(
        renames["QueryItemIn"]
    )
    types["QueryItemOut"] = t.struct(
        {
            "isSynthetic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryItemOut"])
    types["OpenCreatedDraftActionMarkupIn"] = t.struct(
        {
            "draftStorageId": t.string().optional(),
            "draftThreadId": t.string().optional(),
            "draftThreadServerPermId": t.string().optional(),
            "draftId": t.string().optional(),
        }
    ).named(renames["OpenCreatedDraftActionMarkupIn"])
    types["OpenCreatedDraftActionMarkupOut"] = t.struct(
        {
            "draftStorageId": t.string().optional(),
            "draftThreadId": t.string().optional(),
            "draftThreadServerPermId": t.string().optional(),
            "draftId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenCreatedDraftActionMarkupOut"])
    types["QueryInterpretationOptionsIn"] = t.struct(
        {
            "disableSupplementalResults": t.boolean().optional(),
            "enableVerbatimMode": t.boolean().optional(),
            "disableNlInterpretation": t.boolean().optional(),
        }
    ).named(renames["QueryInterpretationOptionsIn"])
    types["QueryInterpretationOptionsOut"] = t.struct(
        {
            "disableSupplementalResults": t.boolean().optional(),
            "enableVerbatimMode": t.boolean().optional(),
            "disableNlInterpretation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationOptionsOut"])
    types["UserIn"] = t.struct(
        {
            "avatarUrl": t.string().optional(),
            "userAccountState": t.string().optional(),
            "id": t.proxy(renames["UserIdIn"]).optional(),
            "botInfo": t.proxy(renames["BotInfoIn"]).optional(),
            "organizationInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoIn"]
            ).optional(),
            "gender": t.string().optional(),
            "email": t.string().optional(),
            "blockRelationship": t.proxy(
                renames["AppsDynamiteSharedUserBlockRelationshipIn"]
            ).optional(),
            "phoneNumber": t.array(
                t.proxy(renames["AppsDynamiteSharedPhoneNumberIn"])
            ).optional(),
            "name": t.string().optional(),
            "lastName": t.string().optional(),
            "isAnonymous": t.boolean().optional(),
            "userProfileVisibility": t.string().optional(),
            "firstName": t.string().optional(),
            "deleted": t.boolean().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "avatarUrl": t.string().optional(),
            "userAccountState": t.string().optional(),
            "id": t.proxy(renames["UserIdOut"]).optional(),
            "botInfo": t.proxy(renames["BotInfoOut"]).optional(),
            "organizationInfo": t.proxy(
                renames["AppsDynamiteSharedOrganizationInfoOut"]
            ).optional(),
            "gender": t.string().optional(),
            "email": t.string().optional(),
            "blockRelationship": t.proxy(
                renames["AppsDynamiteSharedUserBlockRelationshipOut"]
            ).optional(),
            "phoneNumber": t.array(
                t.proxy(renames["AppsDynamiteSharedPhoneNumberOut"])
            ).optional(),
            "name": t.string().optional(),
            "lastName": t.string().optional(),
            "isAnonymous": t.boolean().optional(),
            "userProfileVisibility": t.string().optional(),
            "firstName": t.string().optional(),
            "deleted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["LanguageConfigIn"] = t.struct(
        {"spokenLanguages": t.array(t.string()).optional()}
    ).named(renames["LanguageConfigIn"])
    types["LanguageConfigOut"] = t.struct(
        {
            "spokenLanguages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageConfigOut"])
    types["DocumentInfoIn"] = t.struct(
        {"whiteboardInfo": t.proxy(renames["WhiteboardInfoIn"]).optional()}
    ).named(renames["DocumentInfoIn"])
    types["DocumentInfoOut"] = t.struct(
        {
            "whiteboardInfo": t.proxy(renames["WhiteboardInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentInfoOut"])
    types["BooleanPropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["BooleanOperatorOptionsIn"]).optional()}
    ).named(renames["BooleanPropertyOptionsIn"])
    types["BooleanPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["BooleanOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanPropertyOptionsOut"])
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
    types["EnumValuePairIn"] = t.struct(
        {"integerValue": t.integer().optional(), "stringValue": t.string().optional()}
    ).named(renames["EnumValuePairIn"])
    types["EnumValuePairOut"] = t.struct(
        {
            "integerValue": t.integer().optional(),
            "stringValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValuePairOut"])
    types["TriggerIn"] = t.struct(
        {
            "batchTimeUs": t.string().optional(),
            "jobsettedServerSpec": t.proxy(renames["JobsettedServerSpecIn"]).optional(),
            "key": t.string().optional(),
            "triggerKey": t.proxy(renames["TriggerKeyIn"]).optional(),
            "fireTimeUs": t.string().optional(),
            "dispatcher": t.string().optional(),
            "rpcOptions": t.proxy(renames["RpcOptionsIn"]),
            "dispatchId": t.integer().optional(),
            "sliceFireTimeUs": t.string().optional(),
            "actionType": t.integer().optional(),
            "triggerAction": t.proxy(renames["TriggerActionIn"]).optional(),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "batchTimeUs": t.string().optional(),
            "jobsettedServerSpec": t.proxy(
                renames["JobsettedServerSpecOut"]
            ).optional(),
            "key": t.string().optional(),
            "triggerKey": t.proxy(renames["TriggerKeyOut"]).optional(),
            "fireTimeUs": t.string().optional(),
            "dispatcher": t.string().optional(),
            "rpcOptions": t.proxy(renames["RpcOptionsOut"]),
            "dispatchId": t.integer().optional(),
            "sliceFireTimeUs": t.string().optional(),
            "actionType": t.integer().optional(),
            "triggerAction": t.proxy(renames["TriggerActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
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
    types["UpdateSubjectIn"] = t.struct({"subject": t.string()}).named(
        renames["UpdateSubjectIn"]
    )
    types["UpdateSubjectOut"] = t.struct(
        {"subject": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateSubjectOut"])
    types["AppsDynamiteSharedAssistantDebugContextIn"] = t.struct(
        {"query": t.string().optional()}
    ).named(renames["AppsDynamiteSharedAssistantDebugContextIn"])
    types["AppsDynamiteSharedAssistantDebugContextOut"] = t.struct(
        {
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedAssistantDebugContextOut"])
    types["DateOperatorOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
        }
    ).named(renames["DateOperatorOptionsIn"])
    types["DateOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOperatorOptionsOut"])
    types["OtrModificationEventIn"] = t.struct(
        {
            "oldOtrStatus": t.string(),
            "oldOtrToggle": t.string(),
            "newOtrStatus": t.string(),
            "newOtrToggle": t.string(),
        }
    ).named(renames["OtrModificationEventIn"])
    types["OtrModificationEventOut"] = t.struct(
        {
            "oldOtrStatus": t.string(),
            "oldOtrToggle": t.string(),
            "newOtrStatus": t.string(),
            "newOtrToggle": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtrModificationEventOut"])
    types["RequiredMessageFeaturesMetadataIn"] = t.struct(
        {"requiredFeatures": t.array(t.string())}
    ).named(renames["RequiredMessageFeaturesMetadataIn"])
    types["RequiredMessageFeaturesMetadataOut"] = t.struct(
        {
            "requiredFeatures": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequiredMessageFeaturesMetadataOut"])
    types["YouTubeLiveBroadcastEventIn"] = t.struct(
        {
            "broadcastId": t.string().optional(),
            "channelId": t.string().optional(),
            "brandAccountGaiaId": t.string().optional(),
        }
    ).named(renames["YouTubeLiveBroadcastEventIn"])
    types["YouTubeLiveBroadcastEventOut"] = t.struct(
        {
            "broadcastId": t.string().optional(),
            "viewUrl": t.string().optional(),
            "channelId": t.string().optional(),
            "brandAccountGaiaId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeLiveBroadcastEventOut"])
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
    types["GoogleChatV1WidgetMarkupKeyValueIn"] = t.struct(
        {
            "button": t.proxy(renames["GoogleChatV1WidgetMarkupButtonIn"]).optional(),
            "iconUrl": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "icon": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "content": t.string().optional(),
            "topLabel": t.string().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupKeyValueIn"])
    types["GoogleChatV1WidgetMarkupKeyValueOut"] = t.struct(
        {
            "button": t.proxy(renames["GoogleChatV1WidgetMarkupButtonOut"]).optional(),
            "iconUrl": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "icon": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "content": t.string().optional(),
            "topLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupKeyValueOut"])
    types["SearchApplicationQueryStatsIn"] = t.struct(
        {
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusIn"])),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["SearchApplicationQueryStatsIn"])
    types["SearchApplicationQueryStatsOut"] = t.struct(
        {
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusOut"])),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationQueryStatsOut"])
    types["PrivateMessageInfoIn"] = t.struct(
        {
            "contextualAddOnMarkup": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupIn"])
            ),
            "attachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "text": t.string().optional(),
            "gsuiteIntegrationMetadata": t.array(
                t.proxy(renames["GsuiteIntegrationMetadataIn"])
            ),
            "annotations": t.array(t.proxy(renames["AnnotationIn"])).optional(),
            "userId": t.proxy(renames["UserIdIn"]),
        }
    ).named(renames["PrivateMessageInfoIn"])
    types["PrivateMessageInfoOut"] = t.struct(
        {
            "contextualAddOnMarkup": t.array(
                t.proxy(renames["GoogleChatV1ContextualAddOnMarkupOut"])
            ),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "text": t.string().optional(),
            "gsuiteIntegrationMetadata": t.array(
                t.proxy(renames["GsuiteIntegrationMetadataOut"])
            ),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "userId": t.proxy(renames["UserIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateMessageInfoOut"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsIn"])
    types["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppsDynamiteSharedChatItemActivityInfoFeedItemReactionsOut"])
    types["SourceResultCountIn"] = t.struct(
        {
            "hasMoreResults": t.boolean().optional(),
            "resultCountExact": t.string().optional(),
            "resultCountEstimate": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["SourceResultCountIn"])
    types["SourceResultCountOut"] = t.struct(
        {
            "hasMoreResults": t.boolean().optional(),
            "resultCountExact": t.string().optional(),
            "resultCountEstimate": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceResultCountOut"])
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
    types["AppsDynamiteStorageWidgetIn"] = t.struct(
        {
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputIn"]
            ).optional(),
            "columns": t.proxy(renames["AppsDynamiteStorageColumnsIn"]).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputIn"]).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextIn"]
            ).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerIn"]
            ).optional(),
            "grid": t.proxy(renames["AppsDynamiteStorageGridIn"]).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphIn"]
            ).optional(),
            "divider": t.proxy(renames["AppsDynamiteStorageDividerIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListIn"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageIn"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageWidgetIn"])
    types["AppsDynamiteStorageWidgetOut"] = t.struct(
        {
            "selectionInput": t.proxy(
                renames["AppsDynamiteStorageSelectionInputOut"]
            ).optional(),
            "columns": t.proxy(renames["AppsDynamiteStorageColumnsOut"]).optional(),
            "textInput": t.proxy(renames["AppsDynamiteStorageTextInputOut"]).optional(),
            "decoratedText": t.proxy(
                renames["AppsDynamiteStorageDecoratedTextOut"]
            ).optional(),
            "dateTimePicker": t.proxy(
                renames["AppsDynamiteStorageDateTimePickerOut"]
            ).optional(),
            "grid": t.proxy(renames["AppsDynamiteStorageGridOut"]).optional(),
            "textParagraph": t.proxy(
                renames["AppsDynamiteStorageTextParagraphOut"]
            ).optional(),
            "divider": t.proxy(renames["AppsDynamiteStorageDividerOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "buttonList": t.proxy(
                renames["AppsDynamiteStorageButtonListOut"]
            ).optional(),
            "image": t.proxy(renames["AppsDynamiteStorageImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteStorageWidgetOut"])
    types["ReadReceiptsSettingsUpdatedMetadataIn"] = t.struct(
        {"readReceiptsEnabled": t.boolean().optional()}
    ).named(renames["ReadReceiptsSettingsUpdatedMetadataIn"])
    types["ReadReceiptsSettingsUpdatedMetadataOut"] = t.struct(
        {
            "readReceiptsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadReceiptsSettingsUpdatedMetadataOut"])
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
    types["GoogleChatV1WidgetMarkupTextParagraphIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleChatV1WidgetMarkupTextParagraphIn"])
    types["GoogleChatV1WidgetMarkupTextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChatV1WidgetMarkupTextParagraphOut"])
    types["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "assignee": t.proxy(renames["UserIdIn"]).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "completed": t.boolean().optional(),
            "deleted": t.boolean().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesIn"])
    types["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "assignee": t.proxy(renames["UserIdOut"]).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "completed": t.boolean().optional(),
            "deleted": t.boolean().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsDynamiteSharedTasksAnnotationDataTaskPropertiesOut"])
    types["AutoCompleteItemIn"] = t.struct({"text": t.string()}).named(
        renames["AutoCompleteItemIn"]
    )
    types["AutoCompleteItemOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AutoCompleteItemOut"])
    types["FolderAttributeIn"] = t.struct(
        {"folder": t.array(t.proxy(renames["FolderIn"])).optional()}
    ).named(renames["FolderAttributeIn"])
    types["FolderAttributeOut"] = t.struct(
        {
            "folder": t.array(t.proxy(renames["FolderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderAttributeOut"])
    types["MatchInfoIn"] = t.struct(
        {"matchingImageReferenceKey": t.array(t.string()).optional()}
    ).named(renames["MatchInfoIn"])
    types["MatchInfoOut"] = t.struct(
        {
            "matchingImageReferenceKey": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchInfoOut"])
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
    types["StructuredResultIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["StructuredResultIn"])
    types["StructuredResultOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredResultOut"])
    types["ActionParameterIn"] = t.struct(
        {"key": t.string(), "value": t.string()}
    ).named(renames["ActionParameterIn"])
    types["ActionParameterOut"] = t.struct(
        {
            "key": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionParameterOut"])
    types["ReactionInfoIn"] = t.struct({"emoji": t.string().optional()}).named(
        renames["ReactionInfoIn"]
    )
    types["ReactionInfoOut"] = t.struct(
        {
            "emoji": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReactionInfoOut"])
    types["ToolbarIn"] = t.struct(
        {"color": t.string().optional(), "iconUrl": t.string(), "name": t.string()}
    ).named(renames["ToolbarIn"])
    types["ToolbarOut"] = t.struct(
        {
            "color": t.string().optional(),
            "iconUrl": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolbarOut"])
    types["GoogleChatV1WidgetMarkupImageButtonIn"] = t.struct(
        {
            "name": t.string().optional(),
            "iconUrl": t.string().optional(),
            "onClick": t.proxy(renames["GoogleChatV1WidgetMarkupOnClickIn"]).optional(),
            "icon": t.string().optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageButtonIn"])
    types["GoogleChatV1WidgetMarkupImageButtonOut"] = t.struct(
        {
            "name": t.string().optional(),
            "iconUrl": t.string().optional(),
            "onClick": t.proxy(
                renames["GoogleChatV1WidgetMarkupOnClickOut"]
            ).optional(),
            "icon": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChatV1WidgetMarkupImageButtonOut"])
    types["ContactGroupProtoIn"] = t.struct(
        {
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "ownerGaiaId": t.string(),
            "groupId": t.string().optional(),
        }
    ).named(renames["ContactGroupProtoIn"])
    types["ContactGroupProtoOut"] = t.struct(
        {
            "requiredConsistencyTimestampUsec": t.string().optional(),
            "ownerGaiaId": t.string(),
            "groupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupProtoOut"])
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
    types["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataIn"])
    types["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ChatConserverDynamitePlaceholderMetadataTasksMetadataOut"])
    types["ScoringConfigIn"] = t.struct(
        {
            "disableFreshness": t.boolean().optional(),
            "disablePersonalization": t.boolean().optional(),
        }
    ).named(renames["ScoringConfigIn"])
    types["ScoringConfigOut"] = t.struct(
        {
            "disableFreshness": t.boolean().optional(),
            "disablePersonalization": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScoringConfigOut"])
    types["SupportUrlsIn"] = t.struct(
        {
            "tosUrl": t.string().optional(),
            "deletionPolicyUrl": t.string().optional(),
            "supportUrl": t.string().optional(),
            "privacyPolicyUrl": t.string().optional(),
            "adminConfigUrl": t.string().optional(),
            "setupUrl": t.string().optional(),
            "gwmUrl": t.string().optional(),
        }
    ).named(renames["SupportUrlsIn"])
    types["SupportUrlsOut"] = t.struct(
        {
            "tosUrl": t.string().optional(),
            "deletionPolicyUrl": t.string().optional(),
            "supportUrl": t.string().optional(),
            "privacyPolicyUrl": t.string().optional(),
            "adminConfigUrl": t.string().optional(),
            "setupUrl": t.string().optional(),
            "gwmUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportUrlsOut"])
    types["AttributeRemovedIn"] = t.struct(
        {
            "messageKeys": t.array(t.proxy(renames["MultiKeyIn"])),
            "attributeId": t.string(),
        }
    ).named(renames["AttributeRemovedIn"])
    types["AttributeRemovedOut"] = t.struct(
        {
            "messageKeys": t.array(t.proxy(renames["MultiKeyOut"])),
            "attributeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeRemovedOut"])
    types["MeetingSpaceIn"] = t.struct(
        {
            "phoneAccess": t.array(t.proxy(renames["PhoneAccessIn"])).optional(),
            "broadcastAccess": t.proxy(renames["BroadcastAccessIn"]).optional(),
            "meetingSpaceId": t.string().optional(),
            "universalPhoneAccess": t.proxy(
                renames["UniversalPhoneAccessIn"]
            ).optional(),
            "meetingUrl": t.string().optional(),
            "callInfo": t.proxy(renames["CallInfoIn"]).optional(),
            "meetingAlias": t.string().optional(),
            "settings": t.proxy(renames["SettingsIn"]).optional(),
            "meetingCode": t.string().optional(),
            "acceptedNumberClass": t.array(t.string()).optional(),
            "gatewayAccess": t.proxy(renames["GatewayAccessIn"]).optional(),
            "gatewaySipAccess": t.array(
                t.proxy(renames["GatewaySipAccessIn"])
            ).optional(),
        }
    ).named(renames["MeetingSpaceIn"])
    types["MeetingSpaceOut"] = t.struct(
        {
            "phoneAccess": t.array(t.proxy(renames["PhoneAccessOut"])).optional(),
            "broadcastAccess": t.proxy(renames["BroadcastAccessOut"]).optional(),
            "meetingSpaceId": t.string().optional(),
            "universalPhoneAccess": t.proxy(
                renames["UniversalPhoneAccessOut"]
            ).optional(),
            "meetingUrl": t.string().optional(),
            "callInfo": t.proxy(renames["CallInfoOut"]).optional(),
            "moreJoinUrl": t.string().optional(),
            "meetingAlias": t.string().optional(),
            "settings": t.proxy(renames["SettingsOut"]).optional(),
            "meetingCode": t.string().optional(),
            "acceptedNumberClass": t.array(t.string()).optional(),
            "gatewayAccess": t.proxy(renames["GatewayAccessOut"]).optional(),
            "gatewaySipAccess": t.array(
                t.proxy(renames["GatewaySipAccessOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeetingSpaceOut"])
    types["StreamViewerStatsIn"] = t.struct(
        {"estimatedViewerCount": t.string().optional()}
    ).named(renames["StreamViewerStatsIn"])
    types["StreamViewerStatsOut"] = t.struct(
        {
            "estimatedViewerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamViewerStatsOut"])
    types["TextValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["TextValuesIn"]
    )
    types["TextValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextValuesOut"])

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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
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
    functions["indexingDatasourcesItemsUnreserve"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsGet"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsList"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsDeleteQueueItems"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsIndex"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsPoll"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsDelete"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsPush"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsUpload"] = cloudsearch.post(
        "v1/indexing/{name}:upload",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "connectorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadItemRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugIdentitysourcesUnmappedidsList"] = cloudsearch.get(
        "v1/debug/{parent}/unmappedids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "resolutionStatusCode": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
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
                "groupResourceName": t.string(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListItemNamesForUnmappedIdentityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsSearchByViewUrl"] = cloudsearch.post(
        "v1/debug/{name}:checkAccess",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "name": t.string().optional(),
                "userResourceName": t.string().optional(),
                "gsuitePrincipal": t.proxy(renames["GSuitePrincipalIn"]).optional(),
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
                "userResourceName": t.string().optional(),
                "gsuitePrincipal": t.proxy(renames["GSuitePrincipalIn"]).optional(),
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
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUnmappedIdentitiesResponseOut"]),
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
    functions["settingsSearchapplicationsGet"] = cloudsearch.put(
        "v1/settings/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enableAuditLog": t.boolean().optional(),
                "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "defaultFacetOptions": t.array(
                    t.proxy(renames["FacetOptionsIn"])
                ).optional(),
                "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
                "queryInterpretationConfig": t.proxy(
                    renames["QueryInterpretationConfigIn"]
                ).optional(),
                "returnResultThumbnailUrls": t.boolean().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsDelete"] = cloudsearch.put(
        "v1/settings/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enableAuditLog": t.boolean().optional(),
                "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "defaultFacetOptions": t.array(
                    t.proxy(renames["FacetOptionsIn"])
                ).optional(),
                "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
                "queryInterpretationConfig": t.proxy(
                    renames["QueryInterpretationConfigIn"]
                ).optional(),
                "returnResultThumbnailUrls": t.boolean().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsReset"] = cloudsearch.put(
        "v1/settings/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enableAuditLog": t.boolean().optional(),
                "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "defaultFacetOptions": t.array(
                    t.proxy(renames["FacetOptionsIn"])
                ).optional(),
                "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
                "queryInterpretationConfig": t.proxy(
                    renames["QueryInterpretationConfigIn"]
                ).optional(),
                "returnResultThumbnailUrls": t.boolean().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsList"] = cloudsearch.put(
        "v1/settings/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enableAuditLog": t.boolean().optional(),
                "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "defaultFacetOptions": t.array(
                    t.proxy(renames["FacetOptionsIn"])
                ).optional(),
                "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
                "queryInterpretationConfig": t.proxy(
                    renames["QueryInterpretationConfigIn"]
                ).optional(),
                "returnResultThumbnailUrls": t.boolean().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsCreate"] = cloudsearch.put(
        "v1/settings/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enableAuditLog": t.boolean().optional(),
                "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "defaultFacetOptions": t.array(
                    t.proxy(renames["FacetOptionsIn"])
                ).optional(),
                "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
                "queryInterpretationConfig": t.proxy(
                    renames["QueryInterpretationConfigIn"]
                ).optional(),
                "returnResultThumbnailUrls": t.boolean().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsPatch"] = cloudsearch.put(
        "v1/settings/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enableAuditLog": t.boolean().optional(),
                "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "defaultFacetOptions": t.array(
                    t.proxy(renames["FacetOptionsIn"])
                ).optional(),
                "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
                "queryInterpretationConfig": t.proxy(
                    renames["QueryInterpretationConfigIn"]
                ).optional(),
                "returnResultThumbnailUrls": t.boolean().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsUpdate"] = cloudsearch.put(
        "v1/settings/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enableAuditLog": t.boolean().optional(),
                "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "defaultFacetOptions": t.array(
                    t.proxy(renames["FacetOptionsIn"])
                ).optional(),
                "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
                "queryInterpretationConfig": t.proxy(
                    renames["QueryInterpretationConfigIn"]
                ).optional(),
                "returnResultThumbnailUrls": t.boolean().optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesDelete"] = cloudsearch.get(
        "v1/settings/datasources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesCreate"] = cloudsearch.get(
        "v1/settings/datasources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesUpdate"] = cloudsearch.get(
        "v1/settings/datasources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesPatch"] = cloudsearch.get(
        "v1/settings/datasources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesGet"] = cloudsearch.get(
        "v1/settings/datasources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesList"] = cloudsearch.get(
        "v1/settings/datasources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySearch"] = cloudsearch.post(
        "v1/query/suggest",
        t.struct(
            {
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "query": t.string().optional(),
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
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "query": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "requestOptions.timeZone": t.string().optional(),
                "requestOptions.languageCode": t.string().optional(),
                "requestOptions.searchApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListQuerySourcesResponseOut"]),
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
    functions["statsGetIndex"] = cloudsearch.get(
        "v1/stats/user",
        t.struct(
            {
                "toDate.month": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetQuery"] = cloudsearch.get(
        "v1/stats/user",
        t.struct(
            {
                "toDate.month": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetSession"] = cloudsearch.get(
        "v1/stats/user",
        t.struct(
            {
                "toDate.month": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetSearchapplication"] = cloudsearch.get(
        "v1/stats/user",
        t.struct(
            {
                "toDate.month": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetUser"] = cloudsearch.get(
        "v1/stats/user",
        t.struct(
            {
                "toDate.month": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsSessionSearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/session/{name}",
        t.struct(
            {
                "toDate.year": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "name": t.string().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsQuerySearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/query/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "toDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
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
                "fromDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "name": t.string().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
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
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "name": t.string().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudsearch",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
