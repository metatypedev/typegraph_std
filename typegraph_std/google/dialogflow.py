from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_dialogflow() -> Import:
    dialogflow = HTTPRuntime("https://dialogflow.googleapis.com/")

    renames = {
        "ErrorResponse": "_dialogflow_1_ErrorResponse",
        "GoogleCloudDialogflowCxV3ListPagesResponseIn": "_dialogflow_2_GoogleCloudDialogflowCxV3ListPagesResponseIn",
        "GoogleCloudDialogflowCxV3ListPagesResponseOut": "_dialogflow_3_GoogleCloudDialogflowCxV3ListPagesResponseOut",
        "GoogleCloudDialogflowCxV3VoiceSelectionParamsIn": "_dialogflow_4_GoogleCloudDialogflowCxV3VoiceSelectionParamsIn",
        "GoogleCloudDialogflowCxV3VoiceSelectionParamsOut": "_dialogflow_5_GoogleCloudDialogflowCxV3VoiceSelectionParamsOut",
        "GoogleCloudDialogflowCxV3TransitionRouteIn": "_dialogflow_6_GoogleCloudDialogflowCxV3TransitionRouteIn",
        "GoogleCloudDialogflowCxV3TransitionRouteOut": "_dialogflow_7_GoogleCloudDialogflowCxV3TransitionRouteOut",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseIn": "_dialogflow_8_GoogleCloudDialogflowCxV3beta1WebhookResponseIn",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseOut": "_dialogflow_9_GoogleCloudDialogflowCxV3beta1WebhookResponseOut",
        "GoogleCloudDialogflowCxV3AgentValidationResultIn": "_dialogflow_10_GoogleCloudDialogflowCxV3AgentValidationResultIn",
        "GoogleCloudDialogflowCxV3AgentValidationResultOut": "_dialogflow_11_GoogleCloudDialogflowCxV3AgentValidationResultOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseResultIn": "_dialogflow_12_GoogleCloudDialogflowCxV3beta1TestCaseResultIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseResultOut": "_dialogflow_13_GoogleCloudDialogflowCxV3beta1TestCaseResultOut",
        "GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataIn": "_dialogflow_14_GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataOut": "_dialogflow_15_GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataOut",
        "GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataIn": "_dialogflow_16_GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataOut": "_dialogflow_17_GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn": "_dialogflow_18_GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn",
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut": "_dialogflow_19_GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestMetadataIn": "_dialogflow_20_GoogleCloudDialogflowCxV3RunContinuousTestMetadataIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestMetadataOut": "_dialogflow_21_GoogleCloudDialogflowCxV3RunContinuousTestMetadataOut",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataIn": "_dialogflow_22_GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataOut": "_dialogflow_23_GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn": "_dialogflow_24_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut": "_dialogflow_25_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn": "_dialogflow_26_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut": "_dialogflow_27_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut",
        "GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn": "_dialogflow_28_GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn",
        "GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut": "_dialogflow_29_GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut",
        "GoogleCloudDialogflowV2BatchUpdateIntentsResponseIn": "_dialogflow_30_GoogleCloudDialogflowV2BatchUpdateIntentsResponseIn",
        "GoogleCloudDialogflowV2BatchUpdateIntentsResponseOut": "_dialogflow_31_GoogleCloudDialogflowV2BatchUpdateIntentsResponseOut",
        "GoogleCloudDialogflowCxV3IntentTrainingPhraseIn": "_dialogflow_32_GoogleCloudDialogflowCxV3IntentTrainingPhraseIn",
        "GoogleCloudDialogflowCxV3IntentTrainingPhraseOut": "_dialogflow_33_GoogleCloudDialogflowCxV3IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3CalculateCoverageResponseIn": "_dialogflow_34_GoogleCloudDialogflowCxV3CalculateCoverageResponseIn",
        "GoogleCloudDialogflowCxV3CalculateCoverageResponseOut": "_dialogflow_35_GoogleCloudDialogflowCxV3CalculateCoverageResponseOut",
        "GoogleCloudDialogflowCxV3beta1TextInputIn": "_dialogflow_36_GoogleCloudDialogflowCxV3beta1TextInputIn",
        "GoogleCloudDialogflowCxV3beta1TextInputOut": "_dialogflow_37_GoogleCloudDialogflowCxV3beta1TextInputOut",
        "GoogleCloudDialogflowCxV3WebhookIn": "_dialogflow_38_GoogleCloudDialogflowCxV3WebhookIn",
        "GoogleCloudDialogflowCxV3WebhookOut": "_dialogflow_39_GoogleCloudDialogflowCxV3WebhookOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCardIn": "_dialogflow_40_GoogleCloudDialogflowV2beta1IntentMessageCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCardOut": "_dialogflow_41_GoogleCloudDialogflowV2beta1IntentMessageCardOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn": "_dialogflow_42_GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut": "_dialogflow_43_GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn": "_dialogflow_44_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut": "_dialogflow_45_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut",
        "GoogleCloudDialogflowCxV3ConversationTurnIn": "_dialogflow_46_GoogleCloudDialogflowCxV3ConversationTurnIn",
        "GoogleCloudDialogflowCxV3ConversationTurnOut": "_dialogflow_47_GoogleCloudDialogflowCxV3ConversationTurnOut",
        "GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataIn": "_dialogflow_48_GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataOut": "_dialogflow_49_GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesRequestIn": "_dialogflow_50_GoogleCloudDialogflowCxV3ImportTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesRequestOut": "_dialogflow_51_GoogleCloudDialogflowCxV3ImportTestCasesRequestOut",
        "GoogleCloudDialogflowCxV3beta1QueryInputIn": "_dialogflow_52_GoogleCloudDialogflowCxV3beta1QueryInputIn",
        "GoogleCloudDialogflowCxV3beta1QueryInputOut": "_dialogflow_53_GoogleCloudDialogflowCxV3beta1QueryInputOut",
        "GoogleCloudDialogflowV2IntentFollowupIntentInfoIn": "_dialogflow_54_GoogleCloudDialogflowV2IntentFollowupIntentInfoIn",
        "GoogleCloudDialogflowV2IntentFollowupIntentInfoOut": "_dialogflow_55_GoogleCloudDialogflowV2IntentFollowupIntentInfoOut",
        "GoogleCloudDialogflowV2IntentMessageIn": "_dialogflow_56_GoogleCloudDialogflowV2IntentMessageIn",
        "GoogleCloudDialogflowV2IntentMessageOut": "_dialogflow_57_GoogleCloudDialogflowV2IntentMessageOut",
        "GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn": "_dialogflow_58_GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut": "_dialogflow_59_GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut",
        "GoogleCloudDialogflowCxV3ExperimentDefinitionIn": "_dialogflow_60_GoogleCloudDialogflowCxV3ExperimentDefinitionIn",
        "GoogleCloudDialogflowCxV3ExperimentDefinitionOut": "_dialogflow_61_GoogleCloudDialogflowCxV3ExperimentDefinitionOut",
        "GoogleCloudDialogflowV2IntentTrainingPhraseIn": "_dialogflow_62_GoogleCloudDialogflowV2IntentTrainingPhraseIn",
        "GoogleCloudDialogflowV2IntentTrainingPhraseOut": "_dialogflow_63_GoogleCloudDialogflowV2IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataIn": "_dialogflow_64_GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataOut": "_dialogflow_65_GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn": "_dialogflow_66_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut": "_dialogflow_67_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut",
        "GoogleCloudDialogflowV2EventInputIn": "_dialogflow_68_GoogleCloudDialogflowV2EventInputIn",
        "GoogleCloudDialogflowV2EventInputOut": "_dialogflow_69_GoogleCloudDialogflowV2EventInputOut",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersIn": "_dialogflow_70_GoogleCloudDialogflowV2beta1KnowledgeAnswersIn",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersOut": "_dialogflow_71_GoogleCloudDialogflowV2beta1KnowledgeAnswersOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIn": "_dialogflow_72_GoogleCloudDialogflowCxV3beta1WebhookRequestIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestOut": "_dialogflow_73_GoogleCloudDialogflowCxV3beta1WebhookRequestOut",
        "GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn": "_dialogflow_74_GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn",
        "GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut": "_dialogflow_75_GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn": "_dialogflow_76_GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut": "_dialogflow_77_GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut",
        "GoogleCloudDialogflowCxV3StopExperimentRequestIn": "_dialogflow_78_GoogleCloudDialogflowCxV3StopExperimentRequestIn",
        "GoogleCloudDialogflowCxV3StopExperimentRequestOut": "_dialogflow_79_GoogleCloudDialogflowCxV3StopExperimentRequestOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn": "_dialogflow_80_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut": "_dialogflow_81_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut",
        "GoogleCloudDialogflowCxV3CompareVersionsResponseIn": "_dialogflow_82_GoogleCloudDialogflowCxV3CompareVersionsResponseIn",
        "GoogleCloudDialogflowCxV3CompareVersionsResponseOut": "_dialogflow_83_GoogleCloudDialogflowCxV3CompareVersionsResponseOut",
        "GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn": "_dialogflow_84_GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut": "_dialogflow_85_GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn": "_dialogflow_86_GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn",
        "GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut": "_dialogflow_87_GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn": "_dialogflow_88_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut": "_dialogflow_89_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIn": "_dialogflow_90_GoogleCloudDialogflowCxV3WebhookRequestIn",
        "GoogleCloudDialogflowCxV3WebhookRequestOut": "_dialogflow_91_GoogleCloudDialogflowCxV3WebhookRequestOut",
        "GoogleCloudDialogflowV2ArticleAnswerIn": "_dialogflow_92_GoogleCloudDialogflowV2ArticleAnswerIn",
        "GoogleCloudDialogflowV2ArticleAnswerOut": "_dialogflow_93_GoogleCloudDialogflowV2ArticleAnswerOut",
        "GoogleCloudDialogflowV2IntentParameterIn": "_dialogflow_94_GoogleCloudDialogflowV2IntentParameterIn",
        "GoogleCloudDialogflowV2IntentParameterOut": "_dialogflow_95_GoogleCloudDialogflowV2IntentParameterOut",
        "GoogleCloudDialogflowV2beta1IntentMessageImageIn": "_dialogflow_96_GoogleCloudDialogflowV2beta1IntentMessageImageIn",
        "GoogleCloudDialogflowV2beta1IntentMessageImageOut": "_dialogflow_97_GoogleCloudDialogflowV2beta1IntentMessageImageOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn": "_dialogflow_98_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut": "_dialogflow_99_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut",
        "GoogleCloudDialogflowCxV3VariantsHistoryIn": "_dialogflow_100_GoogleCloudDialogflowCxV3VariantsHistoryIn",
        "GoogleCloudDialogflowCxV3VariantsHistoryOut": "_dialogflow_101_GoogleCloudDialogflowCxV3VariantsHistoryOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueIn": "_dialogflow_102_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueOut": "_dialogflow_103_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueOut",
        "GoogleCloudDialogflowCxV3ListChangelogsResponseIn": "_dialogflow_104_GoogleCloudDialogflowCxV3ListChangelogsResponseIn",
        "GoogleCloudDialogflowCxV3ListChangelogsResponseOut": "_dialogflow_105_GoogleCloudDialogflowCxV3ListChangelogsResponseOut",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseIn": "_dialogflow_106_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseOut": "_dialogflow_107_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3FulfillIntentRequestIn": "_dialogflow_108_GoogleCloudDialogflowCxV3FulfillIntentRequestIn",
        "GoogleCloudDialogflowCxV3FulfillIntentRequestOut": "_dialogflow_109_GoogleCloudDialogflowCxV3FulfillIntentRequestOut",
        "GoogleCloudDialogflowCxV3FulfillIntentResponseIn": "_dialogflow_110_GoogleCloudDialogflowCxV3FulfillIntentResponseIn",
        "GoogleCloudDialogflowCxV3FulfillIntentResponseOut": "_dialogflow_111_GoogleCloudDialogflowCxV3FulfillIntentResponseOut",
        "GoogleCloudDialogflowCxV3DeployFlowRequestIn": "_dialogflow_112_GoogleCloudDialogflowCxV3DeployFlowRequestIn",
        "GoogleCloudDialogflowCxV3DeployFlowRequestOut": "_dialogflow_113_GoogleCloudDialogflowCxV3DeployFlowRequestOut",
        "GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn": "_dialogflow_114_GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut": "_dialogflow_115_GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageIn": "_dialogflow_116_GoogleCloudDialogflowCxV3beta1ResponseMessageIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOut": "_dialogflow_117_GoogleCloudDialogflowCxV3beta1ResponseMessageOut",
        "GoogleCloudDialogflowCxV3ImportFlowRequestIn": "_dialogflow_118_GoogleCloudDialogflowCxV3ImportFlowRequestIn",
        "GoogleCloudDialogflowCxV3ImportFlowRequestOut": "_dialogflow_119_GoogleCloudDialogflowCxV3ImportFlowRequestOut",
        "GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataIn": "_dialogflow_120_GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataOut": "_dialogflow_121_GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn": "_dialogflow_122_GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut": "_dialogflow_123_GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut",
        "GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn": "_dialogflow_124_GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn",
        "GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut": "_dialogflow_125_GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut",
        "GoogleCloudDialogflowCxV3MatchIn": "_dialogflow_126_GoogleCloudDialogflowCxV3MatchIn",
        "GoogleCloudDialogflowCxV3MatchOut": "_dialogflow_127_GoogleCloudDialogflowCxV3MatchOut",
        "GoogleCloudDialogflowCxV3ExportAgentRequestIn": "_dialogflow_128_GoogleCloudDialogflowCxV3ExportAgentRequestIn",
        "GoogleCloudDialogflowCxV3ExportAgentRequestOut": "_dialogflow_129_GoogleCloudDialogflowCxV3ExportAgentRequestOut",
        "GoogleCloudDialogflowCxV3beta1EventHandlerIn": "_dialogflow_130_GoogleCloudDialogflowCxV3beta1EventHandlerIn",
        "GoogleCloudDialogflowCxV3beta1EventHandlerOut": "_dialogflow_131_GoogleCloudDialogflowCxV3beta1EventHandlerOut",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn": "_dialogflow_132_GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut": "_dialogflow_133_GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn": "_dialogflow_134_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut": "_dialogflow_135_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut",
        "GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseIn": "_dialogflow_136_GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseIn",
        "GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut": "_dialogflow_137_GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn": "_dialogflow_138_GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut": "_dialogflow_139_GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut",
        "GoogleCloudDialogflowCxV3TextToSpeechSettingsIn": "_dialogflow_140_GoogleCloudDialogflowCxV3TextToSpeechSettingsIn",
        "GoogleCloudDialogflowCxV3TextToSpeechSettingsOut": "_dialogflow_141_GoogleCloudDialogflowCxV3TextToSpeechSettingsOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn": "_dialogflow_142_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut": "_dialogflow_143_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTextIn": "_dialogflow_144_GoogleCloudDialogflowV2beta1IntentMessageTextIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTextOut": "_dialogflow_145_GoogleCloudDialogflowV2beta1IntentMessageTextOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn": "_dialogflow_146_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut": "_dialogflow_147_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn": "_dialogflow_148_GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut": "_dialogflow_149_GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut",
        "GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn": "_dialogflow_150_GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn",
        "GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut": "_dialogflow_151_GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn": "_dialogflow_152_GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut": "_dialogflow_153_GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut",
        "GoogleCloudDialogflowCxV3DetectIntentResponseIn": "_dialogflow_154_GoogleCloudDialogflowCxV3DetectIntentResponseIn",
        "GoogleCloudDialogflowCxV3DetectIntentResponseOut": "_dialogflow_155_GoogleCloudDialogflowCxV3DetectIntentResponseOut",
        "GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn": "_dialogflow_156_GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn",
        "GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut": "_dialogflow_157_GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn": "_dialogflow_158_GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut": "_dialogflow_159_GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut",
        "GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn": "_dialogflow_160_GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn",
        "GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut": "_dialogflow_161_GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut",
        "GoogleCloudDialogflowCxV3VersionIn": "_dialogflow_162_GoogleCloudDialogflowCxV3VersionIn",
        "GoogleCloudDialogflowCxV3VersionOut": "_dialogflow_163_GoogleCloudDialogflowCxV3VersionOut",
        "GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseIn": "_dialogflow_164_GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseIn",
        "GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseOut": "_dialogflow_165_GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn": "_dialogflow_166_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut": "_dialogflow_167_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardIn": "_dialogflow_168_GoogleCloudDialogflowV2IntentMessageBasicCardIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardOut": "_dialogflow_169_GoogleCloudDialogflowV2IntentMessageBasicCardOut",
        "GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataIn": "_dialogflow_170_GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataOut": "_dialogflow_171_GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataOut",
        "GoogleCloudDialogflowV2SuggestArticlesResponseIn": "_dialogflow_172_GoogleCloudDialogflowV2SuggestArticlesResponseIn",
        "GoogleCloudDialogflowV2SuggestArticlesResponseOut": "_dialogflow_173_GoogleCloudDialogflowV2SuggestArticlesResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn": "_dialogflow_174_GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut": "_dialogflow_175_GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut",
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn": "_dialogflow_176_GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut": "_dialogflow_177_GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowV2HumanAgentAssistantEventIn": "_dialogflow_178_GoogleCloudDialogflowV2HumanAgentAssistantEventIn",
        "GoogleCloudDialogflowV2HumanAgentAssistantEventOut": "_dialogflow_179_GoogleCloudDialogflowV2HumanAgentAssistantEventOut",
        "GoogleCloudDialogflowV2ConversationEventIn": "_dialogflow_180_GoogleCloudDialogflowV2ConversationEventIn",
        "GoogleCloudDialogflowV2ConversationEventOut": "_dialogflow_181_GoogleCloudDialogflowV2ConversationEventOut",
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_182_GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_183_GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowCxV3TextInputIn": "_dialogflow_184_GoogleCloudDialogflowCxV3TextInputIn",
        "GoogleCloudDialogflowCxV3TextInputOut": "_dialogflow_185_GoogleCloudDialogflowCxV3TextInputOut",
        "GoogleCloudDialogflowCxV3ListDeploymentsResponseIn": "_dialogflow_186_GoogleCloudDialogflowCxV3ListDeploymentsResponseIn",
        "GoogleCloudDialogflowCxV3ListDeploymentsResponseOut": "_dialogflow_187_GoogleCloudDialogflowCxV3ListDeploymentsResponseOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn": "_dialogflow_188_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut": "_dialogflow_189_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataIn": "_dialogflow_190_GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataIn",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataOut": "_dialogflow_191_GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardIn": "_dialogflow_192_GoogleCloudDialogflowV2beta1IntentMessageTableCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardOut": "_dialogflow_193_GoogleCloudDialogflowV2beta1IntentMessageTableCardOut",
        "GoogleCloudDialogflowV2GcsDestinationIn": "_dialogflow_194_GoogleCloudDialogflowV2GcsDestinationIn",
        "GoogleCloudDialogflowV2GcsDestinationOut": "_dialogflow_195_GoogleCloudDialogflowV2GcsDestinationOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn": "_dialogflow_196_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut": "_dialogflow_197_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn": "_dialogflow_198_GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut": "_dialogflow_199_GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn": "_dialogflow_200_GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut": "_dialogflow_201_GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn": "_dialogflow_202_GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn",
        "GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut": "_dialogflow_203_GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseErrorIn": "_dialogflow_204_GoogleCloudDialogflowCxV3beta1TestCaseErrorIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseErrorOut": "_dialogflow_205_GoogleCloudDialogflowCxV3beta1TestCaseErrorOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupIn": "_dialogflow_206_GoogleCloudDialogflowCxV3TransitionRouteGroupIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupOut": "_dialogflow_207_GoogleCloudDialogflowCxV3TransitionRouteGroupOut",
        "GoogleCloudDialogflowCxV3IntentCoverageIntentIn": "_dialogflow_208_GoogleCloudDialogflowCxV3IntentCoverageIntentIn",
        "GoogleCloudDialogflowCxV3IntentCoverageIntentOut": "_dialogflow_209_GoogleCloudDialogflowCxV3IntentCoverageIntentOut",
        "GoogleCloudDialogflowCxV3beta1IntentInputIn": "_dialogflow_210_GoogleCloudDialogflowCxV3beta1IntentInputIn",
        "GoogleCloudDialogflowCxV3beta1IntentInputOut": "_dialogflow_211_GoogleCloudDialogflowCxV3beta1IntentInputOut",
        "GoogleCloudDialogflowCxV3ValidateAgentRequestIn": "_dialogflow_212_GoogleCloudDialogflowCxV3ValidateAgentRequestIn",
        "GoogleCloudDialogflowCxV3ValidateAgentRequestOut": "_dialogflow_213_GoogleCloudDialogflowCxV3ValidateAgentRequestOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn": "_dialogflow_214_GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut": "_dialogflow_215_GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut",
        "GoogleCloudDialogflowCxV3TestCaseErrorIn": "_dialogflow_216_GoogleCloudDialogflowCxV3TestCaseErrorIn",
        "GoogleCloudDialogflowCxV3TestCaseErrorOut": "_dialogflow_217_GoogleCloudDialogflowCxV3TestCaseErrorOut",
        "GoogleCloudDialogflowCxV3AudioInputIn": "_dialogflow_218_GoogleCloudDialogflowCxV3AudioInputIn",
        "GoogleCloudDialogflowCxV3AudioInputOut": "_dialogflow_219_GoogleCloudDialogflowCxV3AudioInputOut",
        "GoogleCloudDialogflowCxV3VersionVariantsIn": "_dialogflow_220_GoogleCloudDialogflowCxV3VersionVariantsIn",
        "GoogleCloudDialogflowCxV3VersionVariantsOut": "_dialogflow_221_GoogleCloudDialogflowCxV3VersionVariantsOut",
        "GoogleCloudDialogflowCxV3IntentInputIn": "_dialogflow_222_GoogleCloudDialogflowCxV3IntentInputIn",
        "GoogleCloudDialogflowCxV3IntentInputOut": "_dialogflow_223_GoogleCloudDialogflowCxV3IntentInputOut",
        "GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataIn": "_dialogflow_224_GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataOut": "_dialogflow_225_GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn": "_dialogflow_226_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut": "_dialogflow_227_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnIn": "_dialogflow_228_GoogleCloudDialogflowCxV3beta1ConversationTurnIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnOut": "_dialogflow_229_GoogleCloudDialogflowCxV3beta1ConversationTurnOut",
        "GoogleCloudDialogflowCxV3ListFlowsResponseIn": "_dialogflow_230_GoogleCloudDialogflowCxV3ListFlowsResponseIn",
        "GoogleCloudDialogflowCxV3ListFlowsResponseOut": "_dialogflow_231_GoogleCloudDialogflowCxV3ListFlowsResponseOut",
        "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn": "_dialogflow_232_GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn",
        "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut": "_dialogflow_233_GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut",
        "GoogleCloudDialogflowCxV3TestCaseResultIn": "_dialogflow_234_GoogleCloudDialogflowCxV3TestCaseResultIn",
        "GoogleCloudDialogflowCxV3TestCaseResultOut": "_dialogflow_235_GoogleCloudDialogflowCxV3TestCaseResultOut",
        "GoogleCloudDialogflowCxV3SessionEntityTypeIn": "_dialogflow_236_GoogleCloudDialogflowCxV3SessionEntityTypeIn",
        "GoogleCloudDialogflowCxV3SessionEntityTypeOut": "_dialogflow_237_GoogleCloudDialogflowCxV3SessionEntityTypeOut",
        "GoogleCloudDialogflowCxV3TestErrorIn": "_dialogflow_238_GoogleCloudDialogflowCxV3TestErrorIn",
        "GoogleCloudDialogflowCxV3TestErrorOut": "_dialogflow_239_GoogleCloudDialogflowCxV3TestErrorOut",
        "GoogleCloudDialogflowV2ConversationModelIn": "_dialogflow_240_GoogleCloudDialogflowV2ConversationModelIn",
        "GoogleCloudDialogflowV2ConversationModelOut": "_dialogflow_241_GoogleCloudDialogflowV2ConversationModelOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesResponseIn": "_dialogflow_242_GoogleCloudDialogflowCxV3BatchRunTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesResponseOut": "_dialogflow_243_GoogleCloudDialogflowCxV3BatchRunTestCasesResponseOut",
        "GoogleCloudDialogflowV2beta1WebhookRequestIn": "_dialogflow_244_GoogleCloudDialogflowV2beta1WebhookRequestIn",
        "GoogleCloudDialogflowV2beta1WebhookRequestOut": "_dialogflow_245_GoogleCloudDialogflowV2beta1WebhookRequestOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn": "_dialogflow_246_GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut": "_dialogflow_247_GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataIn": "_dialogflow_248_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataOut": "_dialogflow_249_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3MatchIntentResponseIn": "_dialogflow_250_GoogleCloudDialogflowCxV3MatchIntentResponseIn",
        "GoogleCloudDialogflowCxV3MatchIntentResponseOut": "_dialogflow_251_GoogleCloudDialogflowCxV3MatchIntentResponseOut",
        "GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn": "_dialogflow_252_GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn",
        "GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut": "_dialogflow_253_GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut",
        "GoogleCloudDialogflowV2beta1ConversationEventIn": "_dialogflow_254_GoogleCloudDialogflowV2beta1ConversationEventIn",
        "GoogleCloudDialogflowV2beta1ConversationEventOut": "_dialogflow_255_GoogleCloudDialogflowV2beta1ConversationEventOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn": "_dialogflow_256_GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut": "_dialogflow_257_GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut",
        "GoogleCloudDialogflowCxV3OutputAudioConfigIn": "_dialogflow_258_GoogleCloudDialogflowCxV3OutputAudioConfigIn",
        "GoogleCloudDialogflowCxV3OutputAudioConfigOut": "_dialogflow_259_GoogleCloudDialogflowCxV3OutputAudioConfigOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn": "_dialogflow_260_GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut": "_dialogflow_261_GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut",
        "GoogleCloudDialogflowV3alpha1TurnSignalsIn": "_dialogflow_262_GoogleCloudDialogflowV3alpha1TurnSignalsIn",
        "GoogleCloudDialogflowV3alpha1TurnSignalsOut": "_dialogflow_263_GoogleCloudDialogflowV3alpha1TurnSignalsOut",
        "GoogleCloudDialogflowCxV3ResponseMessageTextIn": "_dialogflow_264_GoogleCloudDialogflowCxV3ResponseMessageTextIn",
        "GoogleCloudDialogflowCxV3ResponseMessageTextOut": "_dialogflow_265_GoogleCloudDialogflowCxV3ResponseMessageTextOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn": "_dialogflow_266_GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut": "_dialogflow_267_GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn": "_dialogflow_268_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut": "_dialogflow_269_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut",
        "GoogleCloudDialogflowV2beta1ExportOperationMetadataIn": "_dialogflow_270_GoogleCloudDialogflowV2beta1ExportOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1ExportOperationMetadataOut": "_dialogflow_271_GoogleCloudDialogflowV2beta1ExportOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn": "_dialogflow_272_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut": "_dialogflow_273_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut",
        "GoogleCloudDialogflowV2beta1IntentMessageIn": "_dialogflow_274_GoogleCloudDialogflowV2beta1IntentMessageIn",
        "GoogleCloudDialogflowV2beta1IntentMessageOut": "_dialogflow_275_GoogleCloudDialogflowV2beta1IntentMessageOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn": "_dialogflow_276_GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut": "_dialogflow_277_GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut",
        "GoogleProtobufEmptyIn": "_dialogflow_278_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_dialogflow_279_GoogleProtobufEmptyOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn": "_dialogflow_280_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut": "_dialogflow_281_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut",
        "GoogleCloudDialogflowV2SmartReplyAnswerIn": "_dialogflow_282_GoogleCloudDialogflowV2SmartReplyAnswerIn",
        "GoogleCloudDialogflowV2SmartReplyAnswerOut": "_dialogflow_283_GoogleCloudDialogflowV2SmartReplyAnswerOut",
        "GoogleCloudDialogflowCxV3ExportFlowRequestIn": "_dialogflow_284_GoogleCloudDialogflowCxV3ExportFlowRequestIn",
        "GoogleCloudDialogflowCxV3ExportFlowRequestOut": "_dialogflow_285_GoogleCloudDialogflowCxV3ExportFlowRequestOut",
        "GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn": "_dialogflow_286_GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn",
        "GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut": "_dialogflow_287_GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut",
        "GoogleCloudDialogflowCxV3ImportFlowResponseIn": "_dialogflow_288_GoogleCloudDialogflowCxV3ImportFlowResponseIn",
        "GoogleCloudDialogflowCxV3ImportFlowResponseOut": "_dialogflow_289_GoogleCloudDialogflowCxV3ImportFlowResponseOut",
        "GoogleCloudDialogflowCxV3beta1AudioInputIn": "_dialogflow_290_GoogleCloudDialogflowCxV3beta1AudioInputIn",
        "GoogleCloudDialogflowCxV3beta1AudioInputOut": "_dialogflow_291_GoogleCloudDialogflowCxV3beta1AudioInputOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn": "_dialogflow_292_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut": "_dialogflow_293_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut",
        "GoogleCloudDialogflowCxV3QueryInputIn": "_dialogflow_294_GoogleCloudDialogflowCxV3QueryInputIn",
        "GoogleCloudDialogflowCxV3QueryInputOut": "_dialogflow_295_GoogleCloudDialogflowCxV3QueryInputOut",
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn": "_dialogflow_296_GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn",
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut": "_dialogflow_297_GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut",
        "GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataIn": "_dialogflow_298_GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataOut": "_dialogflow_299_GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3RunTestCaseResponseIn": "_dialogflow_300_GoogleCloudDialogflowCxV3RunTestCaseResponseIn",
        "GoogleCloudDialogflowCxV3RunTestCaseResponseOut": "_dialogflow_301_GoogleCloudDialogflowCxV3RunTestCaseResponseOut",
        "GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn": "_dialogflow_302_GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn",
        "GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut": "_dialogflow_303_GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut",
        "GoogleCloudDialogflowV2WebhookRequestIn": "_dialogflow_304_GoogleCloudDialogflowV2WebhookRequestIn",
        "GoogleCloudDialogflowV2WebhookRequestOut": "_dialogflow_305_GoogleCloudDialogflowV2WebhookRequestOut",
        "GoogleCloudDialogflowV2IntentMessageTextIn": "_dialogflow_306_GoogleCloudDialogflowV2IntentMessageTextIn",
        "GoogleCloudDialogflowV2IntentMessageTextOut": "_dialogflow_307_GoogleCloudDialogflowV2IntentMessageTextOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn": "_dialogflow_308_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut": "_dialogflow_309_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut",
        "GoogleCloudDialogflowCxV3AgentIn": "_dialogflow_310_GoogleCloudDialogflowCxV3AgentIn",
        "GoogleCloudDialogflowCxV3AgentOut": "_dialogflow_311_GoogleCloudDialogflowCxV3AgentOut",
        "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn": "_dialogflow_312_GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn",
        "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut": "_dialogflow_313_GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn": "_dialogflow_314_GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut": "_dialogflow_315_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut",
        "GoogleCloudDialogflowCxV3TestConfigIn": "_dialogflow_316_GoogleCloudDialogflowCxV3TestConfigIn",
        "GoogleCloudDialogflowCxV3TestConfigOut": "_dialogflow_317_GoogleCloudDialogflowCxV3TestConfigOut",
        "GoogleCloudDialogflowV2IntentMessageMediaContentIn": "_dialogflow_318_GoogleCloudDialogflowV2IntentMessageMediaContentIn",
        "GoogleCloudDialogflowV2IntentMessageMediaContentOut": "_dialogflow_319_GoogleCloudDialogflowV2IntentMessageMediaContentOut",
        "GoogleCloudDialogflowV2beta1EventInputIn": "_dialogflow_320_GoogleCloudDialogflowV2beta1EventInputIn",
        "GoogleCloudDialogflowV2beta1EventInputOut": "_dialogflow_321_GoogleCloudDialogflowV2beta1EventInputOut",
        "GoogleCloudDialogflowCxV3beta1IntentIn": "_dialogflow_322_GoogleCloudDialogflowCxV3beta1IntentIn",
        "GoogleCloudDialogflowCxV3beta1IntentOut": "_dialogflow_323_GoogleCloudDialogflowCxV3beta1IntentOut",
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn": "_dialogflow_324_GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut": "_dialogflow_325_GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn": "_dialogflow_326_GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut": "_dialogflow_327_GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut",
        "GoogleCloudDialogflowCxV3RunTestCaseRequestIn": "_dialogflow_328_GoogleCloudDialogflowCxV3RunTestCaseRequestIn",
        "GoogleCloudDialogflowCxV3RunTestCaseRequestOut": "_dialogflow_329_GoogleCloudDialogflowCxV3RunTestCaseRequestOut",
        "GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn": "_dialogflow_330_GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn",
        "GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut": "_dialogflow_331_GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut",
        "GoogleCloudDialogflowCxV3SessionInfoIn": "_dialogflow_332_GoogleCloudDialogflowCxV3SessionInfoIn",
        "GoogleCloudDialogflowCxV3SessionInfoOut": "_dialogflow_333_GoogleCloudDialogflowCxV3SessionInfoOut",
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn": "_dialogflow_334_GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut": "_dialogflow_335_GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3PageIn": "_dialogflow_336_GoogleCloudDialogflowCxV3PageIn",
        "GoogleCloudDialogflowCxV3PageOut": "_dialogflow_337_GoogleCloudDialogflowCxV3PageOut",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn": "_dialogflow_338_GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut": "_dialogflow_339_GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn": "_dialogflow_340_GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut": "_dialogflow_341_GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut",
        "GoogleCloudDialogflowCxV3ListVersionsResponseIn": "_dialogflow_342_GoogleCloudDialogflowCxV3ListVersionsResponseIn",
        "GoogleCloudDialogflowCxV3ListVersionsResponseOut": "_dialogflow_343_GoogleCloudDialogflowCxV3ListVersionsResponseOut",
        "GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn": "_dialogflow_344_GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn",
        "GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut": "_dialogflow_345_GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut",
        "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn": "_dialogflow_346_GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut": "_dialogflow_347_GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowV2SuggestionResultIn": "_dialogflow_348_GoogleCloudDialogflowV2SuggestionResultIn",
        "GoogleCloudDialogflowV2SuggestionResultOut": "_dialogflow_349_GoogleCloudDialogflowV2SuggestionResultOut",
        "GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn": "_dialogflow_350_GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut": "_dialogflow_351_GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut",
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn": "_dialogflow_352_GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut": "_dialogflow_353_GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn": "_dialogflow_354_GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut": "_dialogflow_355_GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut",
        "GoogleCloudDialogflowCxV3ImportDocumentsResponseIn": "_dialogflow_356_GoogleCloudDialogflowCxV3ImportDocumentsResponseIn",
        "GoogleCloudDialogflowCxV3ImportDocumentsResponseOut": "_dialogflow_357_GoogleCloudDialogflowCxV3ImportDocumentsResponseOut",
        "GoogleCloudDialogflowCxV3ConversationTurnUserInputIn": "_dialogflow_358_GoogleCloudDialogflowCxV3ConversationTurnUserInputIn",
        "GoogleCloudDialogflowCxV3ConversationTurnUserInputOut": "_dialogflow_359_GoogleCloudDialogflowCxV3ConversationTurnUserInputOut",
        "GoogleCloudDialogflowCxV3beta1WebhookIn": "_dialogflow_360_GoogleCloudDialogflowCxV3beta1WebhookIn",
        "GoogleCloudDialogflowCxV3beta1WebhookOut": "_dialogflow_361_GoogleCloudDialogflowCxV3beta1WebhookOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn": "_dialogflow_362_GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut": "_dialogflow_363_GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut",
        "GoogleCloudDialogflowCxV3StartExperimentRequestIn": "_dialogflow_364_GoogleCloudDialogflowCxV3StartExperimentRequestIn",
        "GoogleCloudDialogflowCxV3StartExperimentRequestOut": "_dialogflow_365_GoogleCloudDialogflowCxV3StartExperimentRequestOut",
        "GoogleCloudDialogflowV2ExportOperationMetadataIn": "_dialogflow_366_GoogleCloudDialogflowV2ExportOperationMetadataIn",
        "GoogleCloudDialogflowV2ExportOperationMetadataOut": "_dialogflow_367_GoogleCloudDialogflowV2ExportOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn": "_dialogflow_368_GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut": "_dialogflow_369_GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn": "_dialogflow_370_GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut": "_dialogflow_371_GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut",
        "GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataIn": "_dialogflow_372_GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataOut": "_dialogflow_373_GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesResponseIn": "_dialogflow_374_GoogleCloudDialogflowCxV3ImportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesResponseOut": "_dialogflow_375_GoogleCloudDialogflowCxV3ImportTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseResponseIn": "_dialogflow_376_GoogleCloudDialogflowCxV3beta1RunTestCaseResponseIn",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseResponseOut": "_dialogflow_377_GoogleCloudDialogflowCxV3beta1RunTestCaseResponseOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageIn": "_dialogflow_378_GoogleCloudDialogflowCxV3TransitionCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageOut": "_dialogflow_379_GoogleCloudDialogflowCxV3TransitionCoverageOut",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn": "_dialogflow_380_GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut": "_dialogflow_381_GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn": "_dialogflow_382_GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut": "_dialogflow_383_GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn": "_dialogflow_384_GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn",
        "GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut": "_dialogflow_385_GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut",
        "GoogleCloudDialogflowV2ContextIn": "_dialogflow_386_GoogleCloudDialogflowV2ContextIn",
        "GoogleCloudDialogflowV2ContextOut": "_dialogflow_387_GoogleCloudDialogflowV2ContextOut",
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn": "_dialogflow_388_GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn",
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut": "_dialogflow_389_GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn": "_dialogflow_390_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut": "_dialogflow_391_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn": "_dialogflow_392_GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut": "_dialogflow_393_GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut",
        "GoogleCloudDialogflowCxV3WebhookResponseIn": "_dialogflow_394_GoogleCloudDialogflowCxV3WebhookResponseIn",
        "GoogleCloudDialogflowCxV3WebhookResponseOut": "_dialogflow_395_GoogleCloudDialogflowCxV3WebhookResponseOut",
        "GoogleCloudDialogflowCxV3beta1DtmfInputIn": "_dialogflow_396_GoogleCloudDialogflowCxV3beta1DtmfInputIn",
        "GoogleCloudDialogflowCxV3beta1DtmfInputOut": "_dialogflow_397_GoogleCloudDialogflowCxV3beta1DtmfInputOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn": "_dialogflow_398_GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut": "_dialogflow_399_GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut",
        "GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataIn": "_dialogflow_400_GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut": "_dialogflow_401_GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowV2IntentMessageImageIn": "_dialogflow_402_GoogleCloudDialogflowV2IntentMessageImageIn",
        "GoogleCloudDialogflowV2IntentMessageImageOut": "_dialogflow_403_GoogleCloudDialogflowV2IntentMessageImageOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn": "_dialogflow_404_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut": "_dialogflow_405_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut",
        "GoogleCloudDialogflowCxV3beta1FormParameterIn": "_dialogflow_406_GoogleCloudDialogflowCxV3beta1FormParameterIn",
        "GoogleCloudDialogflowCxV3beta1FormParameterOut": "_dialogflow_407_GoogleCloudDialogflowCxV3beta1FormParameterOut",
        "GoogleCloudDialogflowCxV3DeploymentIn": "_dialogflow_408_GoogleCloudDialogflowCxV3DeploymentIn",
        "GoogleCloudDialogflowCxV3DeploymentOut": "_dialogflow_409_GoogleCloudDialogflowCxV3DeploymentOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn": "_dialogflow_410_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut": "_dialogflow_411_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardRowIn": "_dialogflow_412_GoogleCloudDialogflowV2IntentMessageTableCardRowIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardRowOut": "_dialogflow_413_GoogleCloudDialogflowV2IntentMessageTableCardRowOut",
        "GoogleCloudDialogflowCxV3QueryParametersIn": "_dialogflow_414_GoogleCloudDialogflowCxV3QueryParametersIn",
        "GoogleCloudDialogflowCxV3QueryParametersOut": "_dialogflow_415_GoogleCloudDialogflowCxV3QueryParametersOut",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioIn": "_dialogflow_416_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioIn",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut": "_dialogflow_417_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut",
        "GoogleCloudDialogflowV2beta1MessageIn": "_dialogflow_418_GoogleCloudDialogflowV2beta1MessageIn",
        "GoogleCloudDialogflowV2beta1MessageOut": "_dialogflow_419_GoogleCloudDialogflowV2beta1MessageOut",
        "GoogleCloudDialogflowV2ImportDocumentsResponseIn": "_dialogflow_420_GoogleCloudDialogflowV2ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV2ImportDocumentsResponseOut": "_dialogflow_421_GoogleCloudDialogflowV2ImportDocumentsResponseOut",
        "GoogleCloudDialogflowCxV3TestCaseIn": "_dialogflow_422_GoogleCloudDialogflowCxV3TestCaseIn",
        "GoogleCloudDialogflowCxV3TestCaseOut": "_dialogflow_423_GoogleCloudDialogflowCxV3TestCaseOut",
        "GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn": "_dialogflow_424_GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn",
        "GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut": "_dialogflow_425_GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut",
        "GoogleCloudDialogflowV2ExportAgentResponseIn": "_dialogflow_426_GoogleCloudDialogflowV2ExportAgentResponseIn",
        "GoogleCloudDialogflowV2ExportAgentResponseOut": "_dialogflow_427_GoogleCloudDialogflowV2ExportAgentResponseOut",
        "GoogleCloudDialogflowCxV3ListEntityTypesResponseIn": "_dialogflow_428_GoogleCloudDialogflowCxV3ListEntityTypesResponseIn",
        "GoogleCloudDialogflowCxV3ListEntityTypesResponseOut": "_dialogflow_429_GoogleCloudDialogflowCxV3ListEntityTypesResponseOut",
        "GoogleCloudDialogflowV2beta1IntentParameterIn": "_dialogflow_430_GoogleCloudDialogflowV2beta1IntentParameterIn",
        "GoogleCloudDialogflowV2beta1IntentParameterOut": "_dialogflow_431_GoogleCloudDialogflowV2beta1IntentParameterOut",
        "GoogleCloudDialogflowV2QueryResultIn": "_dialogflow_432_GoogleCloudDialogflowV2QueryResultIn",
        "GoogleCloudDialogflowV2QueryResultOut": "_dialogflow_433_GoogleCloudDialogflowV2QueryResultOut",
        "GoogleCloudDialogflowV2beta1SuggestionResultIn": "_dialogflow_434_GoogleCloudDialogflowV2beta1SuggestionResultIn",
        "GoogleCloudDialogflowV2beta1SuggestionResultOut": "_dialogflow_435_GoogleCloudDialogflowV2beta1SuggestionResultOut",
        "GoogleCloudDialogflowCxV3beta1TurnSignalsIn": "_dialogflow_436_GoogleCloudDialogflowCxV3beta1TurnSignalsIn",
        "GoogleCloudDialogflowCxV3beta1TurnSignalsOut": "_dialogflow_437_GoogleCloudDialogflowCxV3beta1TurnSignalsOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn": "_dialogflow_438_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut": "_dialogflow_439_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn": "_dialogflow_440_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut": "_dialogflow_441_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut",
        "GoogleCloudDialogflowCxV3ListIntentsResponseIn": "_dialogflow_442_GoogleCloudDialogflowCxV3ListIntentsResponseIn",
        "GoogleCloudDialogflowCxV3ListIntentsResponseOut": "_dialogflow_443_GoogleCloudDialogflowCxV3ListIntentsResponseOut",
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn": "_dialogflow_444_GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut": "_dialogflow_445_GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1EntityTypeIn": "_dialogflow_446_GoogleCloudDialogflowV2beta1EntityTypeIn",
        "GoogleCloudDialogflowV2beta1EntityTypeOut": "_dialogflow_447_GoogleCloudDialogflowV2beta1EntityTypeOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn": "_dialogflow_448_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut": "_dialogflow_449_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn": "_dialogflow_450_GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut": "_dialogflow_451_GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut",
        "GoogleCloudDialogflowCxV3DeployFlowMetadataIn": "_dialogflow_452_GoogleCloudDialogflowCxV3DeployFlowMetadataIn",
        "GoogleCloudDialogflowCxV3DeployFlowMetadataOut": "_dialogflow_453_GoogleCloudDialogflowCxV3DeployFlowMetadataOut",
        "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn": "_dialogflow_454_GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut": "_dialogflow_455_GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn": "_dialogflow_456_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut": "_dialogflow_457_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut",
        "GoogleCloudDialogflowV2beta1ExportAgentResponseIn": "_dialogflow_458_GoogleCloudDialogflowV2beta1ExportAgentResponseIn",
        "GoogleCloudDialogflowV2beta1ExportAgentResponseOut": "_dialogflow_459_GoogleCloudDialogflowV2beta1ExportAgentResponseOut",
        "GoogleCloudDialogflowV2FaqAnswerIn": "_dialogflow_460_GoogleCloudDialogflowV2FaqAnswerIn",
        "GoogleCloudDialogflowV2FaqAnswerOut": "_dialogflow_461_GoogleCloudDialogflowV2FaqAnswerOut",
        "GoogleCloudDialogflowCxV3MatchIntentRequestIn": "_dialogflow_462_GoogleCloudDialogflowCxV3MatchIntentRequestIn",
        "GoogleCloudDialogflowCxV3MatchIntentRequestOut": "_dialogflow_463_GoogleCloudDialogflowCxV3MatchIntentRequestOut",
        "GoogleCloudDialogflowV2beta1FaqAnswerIn": "_dialogflow_464_GoogleCloudDialogflowV2beta1FaqAnswerIn",
        "GoogleCloudDialogflowV2beta1FaqAnswerOut": "_dialogflow_465_GoogleCloudDialogflowV2beta1FaqAnswerOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn": "_dialogflow_466_GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut": "_dialogflow_467_GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut",
        "GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn": "_dialogflow_468_GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn",
        "GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut": "_dialogflow_469_GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut",
        "GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn": "_dialogflow_470_GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn",
        "GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut": "_dialogflow_471_GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut",
        "GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn": "_dialogflow_472_GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn",
        "GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut": "_dialogflow_473_GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn": "_dialogflow_474_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut": "_dialogflow_475_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut",
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn": "_dialogflow_476_GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut": "_dialogflow_477_GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowCxV3NluSettingsIn": "_dialogflow_478_GoogleCloudDialogflowCxV3NluSettingsIn",
        "GoogleCloudDialogflowCxV3NluSettingsOut": "_dialogflow_479_GoogleCloudDialogflowCxV3NluSettingsOut",
        "GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn": "_dialogflow_480_GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut": "_dialogflow_481_GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut",
        "GoogleCloudDialogflowCxV3beta1InputAudioConfigIn": "_dialogflow_482_GoogleCloudDialogflowCxV3beta1InputAudioConfigIn",
        "GoogleCloudDialogflowCxV3beta1InputAudioConfigOut": "_dialogflow_483_GoogleCloudDialogflowCxV3beta1InputAudioConfigOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataIn": "_dialogflow_484_GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataOut": "_dialogflow_485_GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn": "_dialogflow_486_GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut": "_dialogflow_487_GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut",
        "GoogleCloudDialogflowCxV3ConversationSignalsIn": "_dialogflow_488_GoogleCloudDialogflowCxV3ConversationSignalsIn",
        "GoogleCloudDialogflowCxV3ConversationSignalsOut": "_dialogflow_489_GoogleCloudDialogflowCxV3ConversationSignalsOut",
        "GoogleCloudDialogflowCxV3EntityTypeIn": "_dialogflow_490_GoogleCloudDialogflowCxV3EntityTypeIn",
        "GoogleCloudDialogflowCxV3EntityTypeOut": "_dialogflow_491_GoogleCloudDialogflowCxV3EntityTypeOut",
        "GoogleCloudDialogflowV2OriginalDetectIntentRequestIn": "_dialogflow_492_GoogleCloudDialogflowV2OriginalDetectIntentRequestIn",
        "GoogleCloudDialogflowV2OriginalDetectIntentRequestOut": "_dialogflow_493_GoogleCloudDialogflowV2OriginalDetectIntentRequestOut",
        "GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn": "_dialogflow_494_GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn",
        "GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut": "_dialogflow_495_GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut",
        "GoogleCloudDialogflowCxV3beta1SessionInfoIn": "_dialogflow_496_GoogleCloudDialogflowCxV3beta1SessionInfoIn",
        "GoogleCloudDialogflowCxV3beta1SessionInfoOut": "_dialogflow_497_GoogleCloudDialogflowCxV3beta1SessionInfoOut",
        "GoogleCloudDialogflowCxV3DetectIntentRequestIn": "_dialogflow_498_GoogleCloudDialogflowCxV3DetectIntentRequestIn",
        "GoogleCloudDialogflowCxV3DetectIntentRequestOut": "_dialogflow_499_GoogleCloudDialogflowCxV3DetectIntentRequestOut",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoIn": "_dialogflow_500_GoogleCloudDialogflowCxV3PageInfoFormInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoOut": "_dialogflow_501_GoogleCloudDialogflowCxV3PageInfoFormInfoOut",
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_502_GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_503_GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowCxV3IntentCoverageIn": "_dialogflow_504_GoogleCloudDialogflowCxV3IntentCoverageIn",
        "GoogleCloudDialogflowCxV3IntentCoverageOut": "_dialogflow_505_GoogleCloudDialogflowCxV3IntentCoverageOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioIn": "_dialogflow_506_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut": "_dialogflow_507_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut",
        "GoogleCloudDialogflowV2MessageAnnotationIn": "_dialogflow_508_GoogleCloudDialogflowV2MessageAnnotationIn",
        "GoogleCloudDialogflowV2MessageAnnotationOut": "_dialogflow_509_GoogleCloudDialogflowV2MessageAnnotationOut",
        "GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn": "_dialogflow_510_GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn",
        "GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut": "_dialogflow_511_GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut",
        "GoogleCloudDialogflowCxV3ListWebhooksResponseIn": "_dialogflow_512_GoogleCloudDialogflowCxV3ListWebhooksResponseIn",
        "GoogleCloudDialogflowCxV3ListWebhooksResponseOut": "_dialogflow_513_GoogleCloudDialogflowCxV3ListWebhooksResponseOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn": "_dialogflow_514_GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut": "_dialogflow_515_GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn": "_dialogflow_516_GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut": "_dialogflow_517_GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesMetadataIn": "_dialogflow_518_GoogleCloudDialogflowCxV3ImportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesMetadataOut": "_dialogflow_519_GoogleCloudDialogflowCxV3ImportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataIn": "_dialogflow_520_GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataOut": "_dialogflow_521_GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn": "_dialogflow_522_GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut": "_dialogflow_523_GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesRequestIn": "_dialogflow_524_GoogleCloudDialogflowCxV3ExportTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesRequestOut": "_dialogflow_525_GoogleCloudDialogflowCxV3ExportTestCasesRequestOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn": "_dialogflow_526_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut": "_dialogflow_527_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut",
        "GoogleCloudDialogflowCxV3VersionVariantsVariantIn": "_dialogflow_528_GoogleCloudDialogflowCxV3VersionVariantsVariantIn",
        "GoogleCloudDialogflowCxV3VersionVariantsVariantOut": "_dialogflow_529_GoogleCloudDialogflowCxV3VersionVariantsVariantOut",
        "GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn": "_dialogflow_530_GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut": "_dialogflow_531_GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut",
        "GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataIn": "_dialogflow_532_GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataOut": "_dialogflow_533_GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn": "_dialogflow_534_GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut": "_dialogflow_535_GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut",
        "GoogleCloudDialogflowCxV3beta1PageIn": "_dialogflow_536_GoogleCloudDialogflowCxV3beta1PageIn",
        "GoogleCloudDialogflowCxV3beta1PageOut": "_dialogflow_537_GoogleCloudDialogflowCxV3beta1PageOut",
        "GoogleCloudDialogflowV3alpha1ConversationSignalsIn": "_dialogflow_538_GoogleCloudDialogflowV3alpha1ConversationSignalsIn",
        "GoogleCloudDialogflowV3alpha1ConversationSignalsOut": "_dialogflow_539_GoogleCloudDialogflowV3alpha1ConversationSignalsOut",
        "GoogleCloudDialogflowV2SentimentAnalysisResultIn": "_dialogflow_540_GoogleCloudDialogflowV2SentimentAnalysisResultIn",
        "GoogleCloudDialogflowV2SentimentAnalysisResultOut": "_dialogflow_541_GoogleCloudDialogflowV2SentimentAnalysisResultOut",
        "GoogleLongrunningOperationIn": "_dialogflow_542_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_dialogflow_543_GoogleLongrunningOperationOut",
        "GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn": "_dialogflow_544_GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn",
        "GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut": "_dialogflow_545_GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsIn": "_dialogflow_546_GoogleCloudDialogflowCxV3SecuritySettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsOut": "_dialogflow_547_GoogleCloudDialogflowCxV3SecuritySettingsOut",
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_548_GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_549_GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowCxV3FlowIn": "_dialogflow_550_GoogleCloudDialogflowCxV3FlowIn",
        "GoogleCloudDialogflowCxV3FlowOut": "_dialogflow_551_GoogleCloudDialogflowCxV3FlowOut",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataIn": "_dialogflow_552_GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataOut": "_dialogflow_553_GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataOut",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectIn": "_dialogflow_554_GoogleCloudDialogflowV2IntentMessageCarouselSelectIn",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectOut": "_dialogflow_555_GoogleCloudDialogflowV2IntentMessageCarouselSelectOut",
        "GoogleCloudDialogflowCxV3ContinuousTestResultIn": "_dialogflow_556_GoogleCloudDialogflowCxV3ContinuousTestResultIn",
        "GoogleCloudDialogflowCxV3ContinuousTestResultOut": "_dialogflow_557_GoogleCloudDialogflowCxV3ContinuousTestResultOut",
        "GoogleCloudDialogflowCxV3RestoreAgentRequestIn": "_dialogflow_558_GoogleCloudDialogflowCxV3RestoreAgentRequestIn",
        "GoogleCloudDialogflowCxV3RestoreAgentRequestOut": "_dialogflow_559_GoogleCloudDialogflowCxV3RestoreAgentRequestOut",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn": "_dialogflow_560_GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut": "_dialogflow_561_GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn": "_dialogflow_562_GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut": "_dialogflow_563_GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut",
        "GoogleCloudDialogflowV2SmartReplyModelMetadataIn": "_dialogflow_564_GoogleCloudDialogflowV2SmartReplyModelMetadataIn",
        "GoogleCloudDialogflowV2SmartReplyModelMetadataOut": "_dialogflow_565_GoogleCloudDialogflowV2SmartReplyModelMetadataOut",
        "GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataIn": "_dialogflow_566_GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataOut": "_dialogflow_567_GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ExportAgentResponseIn": "_dialogflow_568_GoogleCloudDialogflowCxV3ExportAgentResponseIn",
        "GoogleCloudDialogflowCxV3ExportAgentResponseOut": "_dialogflow_569_GoogleCloudDialogflowCxV3ExportAgentResponseOut",
        "GoogleCloudDialogflowCxV3beta1ConversationSignalsIn": "_dialogflow_570_GoogleCloudDialogflowCxV3beta1ConversationSignalsIn",
        "GoogleCloudDialogflowCxV3beta1ConversationSignalsOut": "_dialogflow_571_GoogleCloudDialogflowCxV3beta1ConversationSignalsOut",
        "GoogleCloudDialogflowV2IntentIn": "_dialogflow_572_GoogleCloudDialogflowV2IntentIn",
        "GoogleCloudDialogflowV2IntentOut": "_dialogflow_573_GoogleCloudDialogflowV2IntentOut",
        "GoogleCloudDialogflowCxV3RolloutConfigIn": "_dialogflow_574_GoogleCloudDialogflowCxV3RolloutConfigIn",
        "GoogleCloudDialogflowCxV3RolloutConfigOut": "_dialogflow_575_GoogleCloudDialogflowCxV3RolloutConfigOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentIn": "_dialogflow_576_GoogleCloudDialogflowCxV3beta1FulfillmentIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentOut": "_dialogflow_577_GoogleCloudDialogflowCxV3beta1FulfillmentOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn": "_dialogflow_578_GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut": "_dialogflow_579_GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut",
        "GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn": "_dialogflow_580_GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn",
        "GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut": "_dialogflow_581_GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut",
        "GoogleCloudDialogflowCxV3ExperimentResultMetricIn": "_dialogflow_582_GoogleCloudDialogflowCxV3ExperimentResultMetricIn",
        "GoogleCloudDialogflowCxV3ExperimentResultMetricOut": "_dialogflow_583_GoogleCloudDialogflowCxV3ExperimentResultMetricOut",
        "GoogleCloudDialogflowCxV3ExperimentResultIn": "_dialogflow_584_GoogleCloudDialogflowCxV3ExperimentResultIn",
        "GoogleCloudDialogflowCxV3ExperimentResultOut": "_dialogflow_585_GoogleCloudDialogflowCxV3ExperimentResultOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoIn": "_dialogflow_586_GoogleCloudDialogflowCxV3beta1PageInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoOut": "_dialogflow_587_GoogleCloudDialogflowCxV3beta1PageInfoOut",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponseIn": "_dialogflow_588_GoogleCloudDialogflowV2IntentMessageSimpleResponseIn",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponseOut": "_dialogflow_589_GoogleCloudDialogflowV2IntentMessageSimpleResponseOut",
        "GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn": "_dialogflow_590_GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut": "_dialogflow_591_GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowCxV3ListAgentsResponseIn": "_dialogflow_592_GoogleCloudDialogflowCxV3ListAgentsResponseIn",
        "GoogleCloudDialogflowCxV3ListAgentsResponseOut": "_dialogflow_593_GoogleCloudDialogflowCxV3ListAgentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseIn": "_dialogflow_594_GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseIn",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseOut": "_dialogflow_595_GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseOut",
        "GoogleCloudDialogflowCxV3beta1DeployFlowMetadataIn": "_dialogflow_596_GoogleCloudDialogflowCxV3beta1DeployFlowMetadataIn",
        "GoogleCloudDialogflowCxV3beta1DeployFlowMetadataOut": "_dialogflow_597_GoogleCloudDialogflowCxV3beta1DeployFlowMetadataOut",
        "GoogleCloudDialogflowCxV3GcsDestinationIn": "_dialogflow_598_GoogleCloudDialogflowCxV3GcsDestinationIn",
        "GoogleCloudDialogflowCxV3GcsDestinationOut": "_dialogflow_599_GoogleCloudDialogflowCxV3GcsDestinationOut",
        "GoogleCloudDialogflowCxV3ResponseMessageIn": "_dialogflow_600_GoogleCloudDialogflowCxV3ResponseMessageIn",
        "GoogleCloudDialogflowCxV3ResponseMessageOut": "_dialogflow_601_GoogleCloudDialogflowCxV3ResponseMessageOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn": "_dialogflow_602_GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut": "_dialogflow_603_GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut",
        "GoogleCloudDialogflowV2IntentMessageCardIn": "_dialogflow_604_GoogleCloudDialogflowV2IntentMessageCardIn",
        "GoogleCloudDialogflowV2IntentMessageCardOut": "_dialogflow_605_GoogleCloudDialogflowV2IntentMessageCardOut",
        "GoogleCloudDialogflowV2beta1SessionEntityTypeIn": "_dialogflow_606_GoogleCloudDialogflowV2beta1SessionEntityTypeIn",
        "GoogleCloudDialogflowV2beta1SessionEntityTypeOut": "_dialogflow_607_GoogleCloudDialogflowV2beta1SessionEntityTypeOut",
        "GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseIn": "_dialogflow_608_GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseIn",
        "GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseOut": "_dialogflow_609_GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn": "_dialogflow_610_GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut": "_dialogflow_611_GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn": "_dialogflow_612_GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut": "_dialogflow_613_GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut",
        "GoogleRpcStatusIn": "_dialogflow_614_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_dialogflow_615_GoogleRpcStatusOut",
        "GoogleCloudDialogflowV2beta1WebhookResponseIn": "_dialogflow_616_GoogleCloudDialogflowV2beta1WebhookResponseIn",
        "GoogleCloudDialogflowV2beta1WebhookResponseOut": "_dialogflow_617_GoogleCloudDialogflowV2beta1WebhookResponseOut",
        "GoogleCloudDialogflowV2EntityTypeEntityIn": "_dialogflow_618_GoogleCloudDialogflowV2EntityTypeEntityIn",
        "GoogleCloudDialogflowV2EntityTypeEntityOut": "_dialogflow_619_GoogleCloudDialogflowV2EntityTypeEntityOut",
        "GoogleCloudDialogflowCxV3RolloutStateIn": "_dialogflow_620_GoogleCloudDialogflowCxV3RolloutStateIn",
        "GoogleCloudDialogflowCxV3RolloutStateOut": "_dialogflow_621_GoogleCloudDialogflowCxV3RolloutStateOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn": "_dialogflow_622_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut": "_dialogflow_623_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn": "_dialogflow_624_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut": "_dialogflow_625_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut",
        "GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataIn": "_dialogflow_626_GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataOut": "_dialogflow_627_GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn": "_dialogflow_628_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut": "_dialogflow_629_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut",
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn": "_dialogflow_630_GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn",
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut": "_dialogflow_631_GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut",
        "GoogleCloudDialogflowV2SessionEntityTypeIn": "_dialogflow_632_GoogleCloudDialogflowV2SessionEntityTypeIn",
        "GoogleCloudDialogflowV2SessionEntityTypeOut": "_dialogflow_633_GoogleCloudDialogflowV2SessionEntityTypeOut",
        "GoogleCloudDialogflowCxV3PageInfoIn": "_dialogflow_634_GoogleCloudDialogflowCxV3PageInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoOut": "_dialogflow_635_GoogleCloudDialogflowCxV3PageInfoOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn": "_dialogflow_636_GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut": "_dialogflow_637_GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut",
        "GoogleCloudDialogflowV2IntentTrainingPhrasePartIn": "_dialogflow_638_GoogleCloudDialogflowV2IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowV2IntentTrainingPhrasePartOut": "_dialogflow_639_GoogleCloudDialogflowV2IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowV2KnowledgeOperationMetadataIn": "_dialogflow_640_GoogleCloudDialogflowV2KnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV2KnowledgeOperationMetadataOut": "_dialogflow_641_GoogleCloudDialogflowV2KnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn": "_dialogflow_642_GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn",
        "GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut": "_dialogflow_643_GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut",
        "GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn": "_dialogflow_644_GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut": "_dialogflow_645_GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn": "_dialogflow_646_GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut": "_dialogflow_647_GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn": "_dialogflow_648_GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut": "_dialogflow_649_GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut",
        "GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn": "_dialogflow_650_GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn",
        "GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut": "_dialogflow_651_GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn": "_dialogflow_652_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut": "_dialogflow_653_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut",
        "GoogleCloudDialogflowCxV3TestRunDifferenceIn": "_dialogflow_654_GoogleCloudDialogflowCxV3TestRunDifferenceIn",
        "GoogleCloudDialogflowCxV3TestRunDifferenceOut": "_dialogflow_655_GoogleCloudDialogflowCxV3TestRunDifferenceOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn": "_dialogflow_656_GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut": "_dialogflow_657_GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut",
        "GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn": "_dialogflow_658_GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn",
        "GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut": "_dialogflow_659_GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut",
        "GoogleCloudDialogflowCxV3ResourceNameIn": "_dialogflow_660_GoogleCloudDialogflowCxV3ResourceNameIn",
        "GoogleCloudDialogflowCxV3ResourceNameOut": "_dialogflow_661_GoogleCloudDialogflowCxV3ResourceNameOut",
        "GoogleCloudDialogflowCxV3ChangelogIn": "_dialogflow_662_GoogleCloudDialogflowCxV3ChangelogIn",
        "GoogleCloudDialogflowCxV3ChangelogOut": "_dialogflow_663_GoogleCloudDialogflowCxV3ChangelogOut",
        "GoogleCloudDialogflowCxV3DeployFlowResponseIn": "_dialogflow_664_GoogleCloudDialogflowCxV3DeployFlowResponseIn",
        "GoogleCloudDialogflowCxV3DeployFlowResponseOut": "_dialogflow_665_GoogleCloudDialogflowCxV3DeployFlowResponseOut",
        "GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn": "_dialogflow_666_GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn",
        "GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut": "_dialogflow_667_GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut",
        "GoogleCloudDialogflowCxV3beta1IntentParameterIn": "_dialogflow_668_GoogleCloudDialogflowCxV3beta1IntentParameterIn",
        "GoogleCloudDialogflowCxV3beta1IntentParameterOut": "_dialogflow_669_GoogleCloudDialogflowCxV3beta1IntentParameterOut",
        "GoogleCloudDialogflowV2beta1SmartReplyAnswerIn": "_dialogflow_670_GoogleCloudDialogflowV2beta1SmartReplyAnswerIn",
        "GoogleCloudDialogflowV2beta1SmartReplyAnswerOut": "_dialogflow_671_GoogleCloudDialogflowV2beta1SmartReplyAnswerOut",
        "GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn": "_dialogflow_672_GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn",
        "GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut": "_dialogflow_673_GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut",
        "GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn": "_dialogflow_674_GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn",
        "GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut": "_dialogflow_675_GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut",
        "GoogleCloudDialogflowV2WebhookResponseIn": "_dialogflow_676_GoogleCloudDialogflowV2WebhookResponseIn",
        "GoogleCloudDialogflowV2WebhookResponseOut": "_dialogflow_677_GoogleCloudDialogflowV2WebhookResponseOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesResponseIn": "_dialogflow_678_GoogleCloudDialogflowCxV3ExportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesResponseOut": "_dialogflow_679_GoogleCloudDialogflowCxV3ExportTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3TurnSignalsIn": "_dialogflow_680_GoogleCloudDialogflowCxV3TurnSignalsIn",
        "GoogleCloudDialogflowCxV3TurnSignalsOut": "_dialogflow_681_GoogleCloudDialogflowCxV3TurnSignalsOut",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn": "_dialogflow_682_GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut": "_dialogflow_683_GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3FormParameterIn": "_dialogflow_684_GoogleCloudDialogflowCxV3FormParameterIn",
        "GoogleCloudDialogflowCxV3FormParameterOut": "_dialogflow_685_GoogleCloudDialogflowCxV3FormParameterOut",
        "GoogleCloudDialogflowV2beta1IntentIn": "_dialogflow_686_GoogleCloudDialogflowV2beta1IntentIn",
        "GoogleCloudDialogflowV2beta1IntentOut": "_dialogflow_687_GoogleCloudDialogflowV2beta1IntentOut",
        "GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataIn": "_dialogflow_688_GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataOut": "_dialogflow_689_GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn": "_dialogflow_690_GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut": "_dialogflow_691_GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut",
        "GoogleCloudDialogflowV2beta1QueryResultIn": "_dialogflow_692_GoogleCloudDialogflowV2beta1QueryResultIn",
        "GoogleCloudDialogflowV2beta1QueryResultOut": "_dialogflow_693_GoogleCloudDialogflowV2beta1QueryResultOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn": "_dialogflow_694_GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut": "_dialogflow_695_GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut",
        "GoogleCloudDialogflowCxV3FormIn": "_dialogflow_696_GoogleCloudDialogflowCxV3FormIn",
        "GoogleCloudDialogflowCxV3FormOut": "_dialogflow_697_GoogleCloudDialogflowCxV3FormOut",
        "GoogleCloudDialogflowCxV3FlowValidationResultIn": "_dialogflow_698_GoogleCloudDialogflowCxV3FlowValidationResultIn",
        "GoogleCloudDialogflowCxV3FlowValidationResultOut": "_dialogflow_699_GoogleCloudDialogflowCxV3FlowValidationResultOut",
        "GoogleCloudDialogflowCxV3beta1TestConfigIn": "_dialogflow_700_GoogleCloudDialogflowCxV3beta1TestConfigIn",
        "GoogleCloudDialogflowCxV3beta1TestConfigOut": "_dialogflow_701_GoogleCloudDialogflowCxV3beta1TestConfigOut",
        "GoogleCloudLocationListLocationsResponseIn": "_dialogflow_702_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_dialogflow_703_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudDialogflowCxV3beta1TestErrorIn": "_dialogflow_704_GoogleCloudDialogflowCxV3beta1TestErrorIn",
        "GoogleCloudDialogflowCxV3beta1TestErrorOut": "_dialogflow_705_GoogleCloudDialogflowCxV3beta1TestErrorOut",
        "GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn": "_dialogflow_706_GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn",
        "GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut": "_dialogflow_707_GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut",
        "GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn": "_dialogflow_708_GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn",
        "GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut": "_dialogflow_709_GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentIn": "_dialogflow_710_GoogleCloudDialogflowCxV3beta1EnvironmentIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentOut": "_dialogflow_711_GoogleCloudDialogflowCxV3beta1EnvironmentOut",
        "GoogleCloudDialogflowCxV3DeploymentResultIn": "_dialogflow_712_GoogleCloudDialogflowCxV3DeploymentResultIn",
        "GoogleCloudDialogflowCxV3DeploymentResultOut": "_dialogflow_713_GoogleCloudDialogflowCxV3DeploymentResultOut",
        "GoogleTypeLatLngIn": "_dialogflow_714_GoogleTypeLatLngIn",
        "GoogleTypeLatLngOut": "_dialogflow_715_GoogleTypeLatLngOut",
        "GoogleCloudDialogflowCxV3LoadVersionRequestIn": "_dialogflow_716_GoogleCloudDialogflowCxV3LoadVersionRequestIn",
        "GoogleCloudDialogflowCxV3LoadVersionRequestOut": "_dialogflow_717_GoogleCloudDialogflowCxV3LoadVersionRequestOut",
        "GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn": "_dialogflow_718_GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut": "_dialogflow_719_GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn": "_dialogflow_720_GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut": "_dialogflow_721_GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut",
        "GoogleCloudDialogflowV2beta1GcsDestinationIn": "_dialogflow_722_GoogleCloudDialogflowV2beta1GcsDestinationIn",
        "GoogleCloudDialogflowV2beta1GcsDestinationOut": "_dialogflow_723_GoogleCloudDialogflowV2beta1GcsDestinationOut",
        "GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn": "_dialogflow_724_GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut": "_dialogflow_725_GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut",
        "GoogleCloudLocationLocationIn": "_dialogflow_726_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_dialogflow_727_GoogleCloudLocationLocationOut",
        "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn": "_dialogflow_728_GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut": "_dialogflow_729_GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowV2InputDatasetIn": "_dialogflow_730_GoogleCloudDialogflowV2InputDatasetIn",
        "GoogleCloudDialogflowV2InputDatasetOut": "_dialogflow_731_GoogleCloudDialogflowV2InputDatasetOut",
        "GoogleCloudDialogflowCxV3beta1EventInputIn": "_dialogflow_732_GoogleCloudDialogflowCxV3beta1EventInputIn",
        "GoogleCloudDialogflowCxV3beta1EventInputOut": "_dialogflow_733_GoogleCloudDialogflowCxV3beta1EventInputOut",
        "GoogleCloudDialogflowCxV3FulfillmentIn": "_dialogflow_734_GoogleCloudDialogflowCxV3FulfillmentIn",
        "GoogleCloudDialogflowCxV3FulfillmentOut": "_dialogflow_735_GoogleCloudDialogflowCxV3FulfillmentOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseIn": "_dialogflow_736_GoogleCloudDialogflowCxV3beta1TestCaseIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseOut": "_dialogflow_737_GoogleCloudDialogflowCxV3beta1TestCaseOut",
        "GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataIn": "_dialogflow_738_GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataOut": "_dialogflow_739_GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3RunTestCaseMetadataIn": "_dialogflow_740_GoogleCloudDialogflowCxV3RunTestCaseMetadataIn",
        "GoogleCloudDialogflowCxV3RunTestCaseMetadataOut": "_dialogflow_741_GoogleCloudDialogflowCxV3RunTestCaseMetadataOut",
        "GoogleCloudDialogflowCxV3InputAudioConfigIn": "_dialogflow_742_GoogleCloudDialogflowCxV3InputAudioConfigIn",
        "GoogleCloudDialogflowCxV3InputAudioConfigOut": "_dialogflow_743_GoogleCloudDialogflowCxV3InputAudioConfigOut",
        "GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn": "_dialogflow_744_GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut": "_dialogflow_745_GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut",
        "GoogleCloudDialogflowCxV3beta1FormIn": "_dialogflow_746_GoogleCloudDialogflowCxV3beta1FormIn",
        "GoogleCloudDialogflowCxV3beta1FormOut": "_dialogflow_747_GoogleCloudDialogflowCxV3beta1FormOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn": "_dialogflow_748_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut": "_dialogflow_749_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn": "_dialogflow_750_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut": "_dialogflow_751_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut",
        "GoogleCloudDialogflowV2MessageIn": "_dialogflow_752_GoogleCloudDialogflowV2MessageIn",
        "GoogleCloudDialogflowV2MessageOut": "_dialogflow_753_GoogleCloudDialogflowV2MessageOut",
        "GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn": "_dialogflow_754_GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn",
        "GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut": "_dialogflow_755_GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut",
        "GoogleCloudDialogflowCxV3EventInputIn": "_dialogflow_756_GoogleCloudDialogflowCxV3EventInputIn",
        "GoogleCloudDialogflowCxV3EventInputOut": "_dialogflow_757_GoogleCloudDialogflowCxV3EventInputOut",
        "GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn": "_dialogflow_758_GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn",
        "GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut": "_dialogflow_759_GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut",
        "GoogleCloudDialogflowV2IntentMessageListSelectIn": "_dialogflow_760_GoogleCloudDialogflowV2IntentMessageListSelectIn",
        "GoogleCloudDialogflowV2IntentMessageListSelectOut": "_dialogflow_761_GoogleCloudDialogflowV2IntentMessageListSelectOut",
        "GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn": "_dialogflow_762_GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut": "_dialogflow_763_GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut",
        "GoogleCloudDialogflowV2IntentMessageCardButtonIn": "_dialogflow_764_GoogleCloudDialogflowV2IntentMessageCardButtonIn",
        "GoogleCloudDialogflowV2IntentMessageCardButtonOut": "_dialogflow_765_GoogleCloudDialogflowV2IntentMessageCardButtonOut",
        "GoogleCloudDialogflowV2SentimentIn": "_dialogflow_766_GoogleCloudDialogflowV2SentimentIn",
        "GoogleCloudDialogflowV2SentimentOut": "_dialogflow_767_GoogleCloudDialogflowV2SentimentOut",
        "GoogleCloudDialogflowV2EntityTypeIn": "_dialogflow_768_GoogleCloudDialogflowV2EntityTypeIn",
        "GoogleCloudDialogflowV2EntityTypeOut": "_dialogflow_769_GoogleCloudDialogflowV2EntityTypeOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn": "_dialogflow_770_GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut": "_dialogflow_771_GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut",
        "GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn": "_dialogflow_772_GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn",
        "GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut": "_dialogflow_773_GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardIn": "_dialogflow_774_GoogleCloudDialogflowV2IntentMessageTableCardIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardOut": "_dialogflow_775_GoogleCloudDialogflowV2IntentMessageTableCardOut",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn": "_dialogflow_776_GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut": "_dialogflow_777_GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut",
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_778_GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_779_GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowCxV3IntentIn": "_dialogflow_780_GoogleCloudDialogflowCxV3IntentIn",
        "GoogleCloudDialogflowCxV3IntentOut": "_dialogflow_781_GoogleCloudDialogflowCxV3IntentOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn": "_dialogflow_782_GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut": "_dialogflow_783_GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut",
        "GoogleCloudDialogflowCxV3IntentParameterIn": "_dialogflow_784_GoogleCloudDialogflowCxV3IntentParameterIn",
        "GoogleCloudDialogflowCxV3IntentParameterOut": "_dialogflow_785_GoogleCloudDialogflowCxV3IntentParameterOut",
        "GoogleCloudDialogflowCxV3EventHandlerIn": "_dialogflow_786_GoogleCloudDialogflowCxV3EventHandlerIn",
        "GoogleCloudDialogflowCxV3EventHandlerOut": "_dialogflow_787_GoogleCloudDialogflowCxV3EventHandlerOut",
        "GoogleCloudDialogflowCxV3ListExperimentsResponseIn": "_dialogflow_788_GoogleCloudDialogflowCxV3ListExperimentsResponseIn",
        "GoogleCloudDialogflowCxV3ListExperimentsResponseOut": "_dialogflow_789_GoogleCloudDialogflowCxV3ListExperimentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn": "_dialogflow_790_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut": "_dialogflow_791_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestResponseIn": "_dialogflow_792_GoogleCloudDialogflowCxV3RunContinuousTestResponseIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestResponseOut": "_dialogflow_793_GoogleCloudDialogflowCxV3RunContinuousTestResponseOut",
        "GoogleCloudDialogflowCxV3SpeechToTextSettingsIn": "_dialogflow_794_GoogleCloudDialogflowCxV3SpeechToTextSettingsIn",
        "GoogleCloudDialogflowCxV3SpeechToTextSettingsOut": "_dialogflow_795_GoogleCloudDialogflowCxV3SpeechToTextSettingsOut",
        "GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn": "_dialogflow_796_GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut": "_dialogflow_797_GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut",
        "GoogleCloudDialogflowV2beta1ContextIn": "_dialogflow_798_GoogleCloudDialogflowV2beta1ContextIn",
        "GoogleCloudDialogflowV2beta1ContextOut": "_dialogflow_799_GoogleCloudDialogflowV2beta1ContextOut",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectIn": "_dialogflow_800_GoogleCloudDialogflowV2beta1IntentMessageListSelectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectOut": "_dialogflow_801_GoogleCloudDialogflowV2beta1IntentMessageListSelectOut",
        "GoogleCloudDialogflowCxV3AdvancedSettingsIn": "_dialogflow_802_GoogleCloudDialogflowCxV3AdvancedSettingsIn",
        "GoogleCloudDialogflowCxV3AdvancedSettingsOut": "_dialogflow_803_GoogleCloudDialogflowCxV3AdvancedSettingsOut",
        "GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn": "_dialogflow_804_GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn",
        "GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut": "_dialogflow_805_GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut",
        "GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseIn": "_dialogflow_806_GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseIn",
        "GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseOut": "_dialogflow_807_GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseOut",
        "GoogleCloudDialogflowCxV3CompareVersionsRequestIn": "_dialogflow_808_GoogleCloudDialogflowCxV3CompareVersionsRequestIn",
        "GoogleCloudDialogflowCxV3CompareVersionsRequestOut": "_dialogflow_809_GoogleCloudDialogflowCxV3CompareVersionsRequestOut",
        "GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn": "_dialogflow_810_GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn",
        "GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut": "_dialogflow_811_GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardCellIn": "_dialogflow_812_GoogleCloudDialogflowV2IntentMessageTableCardCellIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardCellOut": "_dialogflow_813_GoogleCloudDialogflowV2IntentMessageTableCardCellOut",
        "GoogleCloudDialogflowCxV3ExperimentIn": "_dialogflow_814_GoogleCloudDialogflowCxV3ExperimentIn",
        "GoogleCloudDialogflowCxV3ExperimentOut": "_dialogflow_815_GoogleCloudDialogflowCxV3ExperimentOut",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn": "_dialogflow_816_GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut": "_dialogflow_817_GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowCxV3ListTestCasesResponseIn": "_dialogflow_818_GoogleCloudDialogflowCxV3ListTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ListTestCasesResponseOut": "_dialogflow_819_GoogleCloudDialogflowCxV3ListTestCasesResponseOut",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn": "_dialogflow_820_GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut": "_dialogflow_821_GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut",
        "GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn": "_dialogflow_822_GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn",
        "GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut": "_dialogflow_823_GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut",
        "GoogleCloudDialogflowV2IntentMessageSuggestionIn": "_dialogflow_824_GoogleCloudDialogflowV2IntentMessageSuggestionIn",
        "GoogleCloudDialogflowV2IntentMessageSuggestionOut": "_dialogflow_825_GoogleCloudDialogflowV2IntentMessageSuggestionOut",
        "GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn": "_dialogflow_826_GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn",
        "GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut": "_dialogflow_827_GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut",
        "GoogleCloudDialogflowCxV3ExportFlowResponseIn": "_dialogflow_828_GoogleCloudDialogflowCxV3ExportFlowResponseIn",
        "GoogleCloudDialogflowCxV3ExportFlowResponseOut": "_dialogflow_829_GoogleCloudDialogflowCxV3ExportFlowResponseOut",
        "GoogleCloudDialogflowV2IntentMessageQuickRepliesIn": "_dialogflow_830_GoogleCloudDialogflowV2IntentMessageQuickRepliesIn",
        "GoogleCloudDialogflowV2IntentMessageQuickRepliesOut": "_dialogflow_831_GoogleCloudDialogflowV2IntentMessageQuickRepliesOut",
        "GoogleCloudDialogflowCxV3EnvironmentIn": "_dialogflow_832_GoogleCloudDialogflowCxV3EnvironmentIn",
        "GoogleCloudDialogflowCxV3EnvironmentOut": "_dialogflow_833_GoogleCloudDialogflowCxV3EnvironmentOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn": "_dialogflow_834_GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut": "_dialogflow_835_GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut",
        "GoogleCloudDialogflowCxV3TrainFlowRequestIn": "_dialogflow_836_GoogleCloudDialogflowCxV3TrainFlowRequestIn",
        "GoogleCloudDialogflowCxV3TrainFlowRequestOut": "_dialogflow_837_GoogleCloudDialogflowCxV3TrainFlowRequestOut",
        "GoogleCloudDialogflowV2beta1EntityTypeEntityIn": "_dialogflow_838_GoogleCloudDialogflowV2beta1EntityTypeEntityIn",
        "GoogleCloudDialogflowV2beta1EntityTypeEntityOut": "_dialogflow_839_GoogleCloudDialogflowV2beta1EntityTypeEntityOut",
        "GoogleCloudDialogflowCxV3ListSecuritySettingsResponseIn": "_dialogflow_840_GoogleCloudDialogflowCxV3ListSecuritySettingsResponseIn",
        "GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut": "_dialogflow_841_GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut",
        "GoogleCloudDialogflowV2IntentMessageListSelectItemIn": "_dialogflow_842_GoogleCloudDialogflowV2IntentMessageListSelectItemIn",
        "GoogleCloudDialogflowV2IntentMessageListSelectItemOut": "_dialogflow_843_GoogleCloudDialogflowV2IntentMessageListSelectItemOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn": "_dialogflow_844_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut": "_dialogflow_845_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut",
        "GoogleCloudDialogflowV2beta1MessageAnnotationIn": "_dialogflow_846_GoogleCloudDialogflowV2beta1MessageAnnotationIn",
        "GoogleCloudDialogflowV2beta1MessageAnnotationOut": "_dialogflow_847_GoogleCloudDialogflowV2beta1MessageAnnotationOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestRequestIn": "_dialogflow_848_GoogleCloudDialogflowCxV3RunContinuousTestRequestIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestRequestOut": "_dialogflow_849_GoogleCloudDialogflowCxV3RunContinuousTestRequestOut",
        "GoogleCloudDialogflowCxV3ValidationMessageIn": "_dialogflow_850_GoogleCloudDialogflowCxV3ValidationMessageIn",
        "GoogleCloudDialogflowCxV3ValidationMessageOut": "_dialogflow_851_GoogleCloudDialogflowCxV3ValidationMessageOut",
        "GoogleCloudDialogflowCxV3EntityTypeEntityIn": "_dialogflow_852_GoogleCloudDialogflowCxV3EntityTypeEntityIn",
        "GoogleCloudDialogflowCxV3EntityTypeEntityOut": "_dialogflow_853_GoogleCloudDialogflowCxV3EntityTypeEntityOut",
        "GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn": "_dialogflow_854_GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn",
        "GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut": "_dialogflow_855_GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn": "_dialogflow_856_GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut": "_dialogflow_857_GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut",
        "GoogleCloudDialogflowCxV3ValidateFlowRequestIn": "_dialogflow_858_GoogleCloudDialogflowCxV3ValidateFlowRequestIn",
        "GoogleCloudDialogflowCxV3ValidateFlowRequestOut": "_dialogflow_859_GoogleCloudDialogflowCxV3ValidateFlowRequestOut",
        "GoogleCloudDialogflowV2AnnotatedMessagePartIn": "_dialogflow_860_GoogleCloudDialogflowV2AnnotatedMessagePartIn",
        "GoogleCloudDialogflowV2AnnotatedMessagePartOut": "_dialogflow_861_GoogleCloudDialogflowV2AnnotatedMessagePartOut",
        "GoogleCloudDialogflowCxV3beta1TransitionRouteIn": "_dialogflow_862_GoogleCloudDialogflowCxV3beta1TransitionRouteIn",
        "GoogleCloudDialogflowCxV3beta1TransitionRouteOut": "_dialogflow_863_GoogleCloudDialogflowCxV3beta1TransitionRouteOut",
        "GoogleCloudDialogflowCxV3QueryResultIn": "_dialogflow_864_GoogleCloudDialogflowCxV3QueryResultIn",
        "GoogleCloudDialogflowCxV3QueryResultOut": "_dialogflow_865_GoogleCloudDialogflowCxV3QueryResultOut",
        "GoogleCloudDialogflowV2beta1SentimentIn": "_dialogflow_866_GoogleCloudDialogflowV2beta1SentimentIn",
        "GoogleCloudDialogflowV2beta1SentimentOut": "_dialogflow_867_GoogleCloudDialogflowV2beta1SentimentOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn": "_dialogflow_868_GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut": "_dialogflow_869_GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut",
        "GoogleLongrunningListOperationsResponseIn": "_dialogflow_870_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_dialogflow_871_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn": "_dialogflow_872_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut": "_dialogflow_873_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut",
        "GoogleCloudDialogflowV2IntentMessageSuggestionsIn": "_dialogflow_874_GoogleCloudDialogflowV2IntentMessageSuggestionsIn",
        "GoogleCloudDialogflowV2IntentMessageSuggestionsOut": "_dialogflow_875_GoogleCloudDialogflowV2IntentMessageSuggestionsOut",
        "GoogleCloudDialogflowCxV3DtmfInputIn": "_dialogflow_876_GoogleCloudDialogflowCxV3DtmfInputIn",
        "GoogleCloudDialogflowCxV3DtmfInputOut": "_dialogflow_877_GoogleCloudDialogflowCxV3DtmfInputOut",
        "GoogleCloudDialogflowCxV3SentimentAnalysisResultIn": "_dialogflow_878_GoogleCloudDialogflowCxV3SentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3SentimentAnalysisResultOut": "_dialogflow_879_GoogleCloudDialogflowCxV3SentimentAnalysisResultOut",
        "GoogleCloudDialogflowV2beta1ArticleAnswerIn": "_dialogflow_880_GoogleCloudDialogflowV2beta1ArticleAnswerIn",
        "GoogleCloudDialogflowV2beta1ArticleAnswerOut": "_dialogflow_881_GoogleCloudDialogflowV2beta1ArticleAnswerOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDialogflowCxV3ListPagesResponseIn"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3PageIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListPagesResponseIn"])
    types["GoogleCloudDialogflowCxV3ListPagesResponseOut"] = t.struct(
        {
            "pages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListPagesResponseOut"])
    types["GoogleCloudDialogflowCxV3VoiceSelectionParamsIn"] = t.struct(
        {"ssmlGender": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsIn"])
    types["GoogleCloudDialogflowCxV3VoiceSelectionParamsOut"] = t.struct(
        {
            "ssmlGender": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsOut"])
    types["GoogleCloudDialogflowCxV3TransitionRouteIn"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "condition": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
            "targetPage": t.string().optional(),
            "intent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
    types["GoogleCloudDialogflowCxV3TransitionRouteOut"] = t.struct(
        {
            "name": t.string().optional(),
            "targetFlow": t.string().optional(),
            "condition": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "targetPage": t.string().optional(),
            "intent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookResponseIn"] = t.struct(
        {
            "fulfillmentResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn"
                ]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoIn"]
            ).optional(),
            "targetPage": t.string().optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "targetFlow": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookResponseOut"] = t.struct(
        {
            "fulfillmentResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut"
                ]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoOut"]
            ).optional(),
            "targetPage": t.string().optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "targetFlow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookResponseOut"])
    types["GoogleCloudDialogflowCxV3AgentValidationResultIn"] = t.struct(
        {
            "name": t.string().optional(),
            "flowValidationResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FlowValidationResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentValidationResultIn"])
    types["GoogleCloudDialogflowCxV3AgentValidationResultOut"] = t.struct(
        {
            "name": t.string().optional(),
            "flowValidationResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FlowValidationResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentValidationResultOut"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"] = t.struct(
        {
            "testResult": t.string().optional(),
            "testTime": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnIn"])
            ).optional(),
            "environment": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"] = t.struct(
        {
            "testResult": t.string().optional(),
            "testTime": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnOut"])
            ).optional(),
            "environment": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"])
    types[
        "GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataIn"
    ] = t.struct({"conversationDataset": t.string().optional()}).named(
        renames["GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataOut"
    ] = t.struct(
        {
            "conversationDataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataIn"])
    types["GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataOut"])
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn"
    ] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "conversationDataset": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut"
    ] = t.struct(
        {
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "conversationDataset": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowCxV3RunContinuousTestMetadataIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestErrorIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestMetadataIn"])
    types["GoogleCloudDialogflowCxV3RunContinuousTestMetadataOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestCaseErrorIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestCaseErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataOut"])
    types["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn"] = t.struct(
        {
            "lastMatchedIntent": t.string().optional(),
            "confidence": t.number().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn"])
    types["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut"] = t.struct(
        {
            "lastMatchedIntent": t.string().optional(),
            "confidence": t.number().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn"
    ] = t.struct({"uri": t.string()}).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut"
    ] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn"] = t.struct(
        {
            "name": t.string().optional(),
            "result": t.string().optional(),
            "runTime": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn"])
    types["GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut"] = t.struct(
        {
            "name": t.string().optional(),
            "result": t.string().optional(),
            "runTime": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut"])
    types["GoogleCloudDialogflowV2BatchUpdateIntentsResponseIn"] = t.struct(
        {
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2BatchUpdateIntentsResponseIn"])
    types["GoogleCloudDialogflowV2BatchUpdateIntentsResponseOut"] = t.struct(
        {
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2BatchUpdateIntentsResponseOut"])
    types["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"] = t.struct(
        {
            "id": t.string().optional(),
            "repeatCount": t.integer().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn"])
            ),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowCxV3IntentTrainingPhraseOut"] = t.struct(
        {
            "id": t.string().optional(),
            "repeatCount": t.integer().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseOut"])
    types["GoogleCloudDialogflowCxV3CalculateCoverageResponseIn"] = t.struct(
        {
            "routeGroupCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn"]
            ).optional(),
            "intentCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentCoverageIn"]
            ).optional(),
            "agent": t.string().optional(),
            "transitionCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CalculateCoverageResponseIn"])
    types["GoogleCloudDialogflowCxV3CalculateCoverageResponseOut"] = t.struct(
        {
            "routeGroupCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut"]
            ).optional(),
            "intentCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentCoverageOut"]
            ).optional(),
            "agent": t.string().optional(),
            "transitionCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CalculateCoverageResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1TextInputIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1TextInputIn"])
    types["GoogleCloudDialogflowCxV3beta1TextInputOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1TextInputOut"])
    types["GoogleCloudDialogflowCxV3WebhookIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "name": t.string().optional(),
            "disabled": t.boolean().optional(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
            ).optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
            ).optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookIn"])
    types["GoogleCloudDialogflowCxV3WebhookOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "name": t.string().optional(),
            "disabled": t.boolean().optional(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut"]
            ).optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"]
            ).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardIn"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn"]
                )
            ).optional(),
            "title": t.string().optional(),
            "imageUri": t.string().optional(),
            "subtitle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardOut"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut"]
                )
            ).optional(),
            "title": t.string().optional(),
            "imageUri": t.string().optional(),
            "subtitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn"
    ] = t.struct({"phoneNumber": t.string()}).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn"]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut"
    ] = t.struct(
        {
            "phoneNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut"]
    )
    types["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn"] = t.struct(
        {
            "imageDisplayOptions": t.string().optional(),
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
                    ]
                )
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut"] = t.struct(
        {
            "imageDisplayOptions": t.string().optional(),
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut"])
    types["GoogleCloudDialogflowCxV3ConversationTurnIn"] = t.struct(
        {
            "userInput": t.proxy(
                renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputIn"]
            ).optional(),
            "virtualAgentOutput": t.proxy(
                renames["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
    types["GoogleCloudDialogflowCxV3ConversationTurnOut"] = t.struct(
        {
            "userInput": t.proxy(
                renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputOut"]
            ).optional(),
            "virtualAgentOutput": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnOut"])
    types["GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataIn"])
    types["GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3ImportTestCasesRequestIn"] = t.struct(
        {"gcsUri": t.string().optional(), "content": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3ImportTestCasesRequestOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesRequestOut"])
    types["GoogleCloudDialogflowCxV3beta1QueryInputIn"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EventInputIn"]
            ).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1AudioInputIn"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TextInputIn"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentInputIn"]
            ).optional(),
            "languageCode": t.string(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1DtmfInputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1QueryInputIn"])
    types["GoogleCloudDialogflowCxV3beta1QueryInputOut"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EventInputOut"]
            ).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1AudioInputOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TextInputOut"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentInputOut"]
            ).optional(),
            "languageCode": t.string(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1DtmfInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1QueryInputOut"])
    types["GoogleCloudDialogflowV2IntentFollowupIntentInfoIn"] = t.struct(
        {
            "followupIntentName": t.string().optional(),
            "parentFollowupIntentName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentFollowupIntentInfoIn"])
    types["GoogleCloudDialogflowV2IntentFollowupIntentInfoOut"] = t.struct(
        {
            "followupIntentName": t.string().optional(),
            "parentFollowupIntentName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentFollowupIntentInfoOut"])
    types["GoogleCloudDialogflowV2IntentMessageIn"] = t.struct(
        {
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBasicCardIn"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageMediaContentIn"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSuggestionsIn"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectIn"]
            ).optional(),
            "platform": t.string().optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTextIn"]
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCardIn"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn"]
            ).optional(),
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageListSelectIn"]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTableCardIn"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageQuickRepliesIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageIn"])
    types["GoogleCloudDialogflowV2IntentMessageOut"] = t.struct(
        {
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBasicCardOut"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageMediaContentOut"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSuggestionsOut"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectOut"]
            ).optional(),
            "platform": t.string().optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTextOut"]
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCardOut"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut"]
            ).optional(),
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageListSelectOut"]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTableCardOut"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageQuickRepliesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn"] = t.struct(
        {"title": t.string().optional(), "quickReplies": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut"] = t.struct(
        {
            "title": t.string().optional(),
            "quickReplies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut"])
    types["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"] = t.struct(
        {
            "versionVariants": t.proxy(
                renames["GoogleCloudDialogflowCxV3VersionVariantsIn"]
            ).optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"])
    types["GoogleCloudDialogflowCxV3ExperimentDefinitionOut"] = t.struct(
        {
            "versionVariants": t.proxy(
                renames["GoogleCloudDialogflowCxV3VersionVariantsOut"]
            ).optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentDefinitionOut"])
    types["GoogleCloudDialogflowV2IntentTrainingPhraseIn"] = t.struct(
        {
            "timesAddedCount": t.integer().optional(),
            "type": t.string(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"])
            ),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowV2IntentTrainingPhraseOut"] = t.struct(
        {
            "timesAddedCount": t.integer().optional(),
            "type": t.string(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"])
            ),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhraseOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataIn"
    ] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataOut"
    ] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataOut"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn"
    ] = t.struct(
        {
            "additionalCases": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn"]
            ).optional(),
            "message": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn"
        ]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut"
    ] = t.struct(
        {
            "additionalCases": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut"]
            ).optional(),
            "message": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut"
        ]
    )
    types["GoogleCloudDialogflowV2EventInputIn"] = t.struct(
        {
            "languageCode": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2EventInputIn"])
    types["GoogleCloudDialogflowV2EventInputOut"] = t.struct(
        {
            "languageCode": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EventInputOut"])
    types["GoogleCloudDialogflowV2beta1KnowledgeAnswersIn"] = t.struct(
        {
            "answers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersIn"])
    types["GoogleCloudDialogflowV2beta1KnowledgeAnswersOut"] = t.struct(
        {
            "answers": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIn"] = t.struct(
        {
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoIn"]
            ).optional(),
            "triggerIntent": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "detectIntentResponseId": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
            ).optional(),
            "languageCode": t.string().optional(),
            "transcript": t.string().optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoIn"]
            ).optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"]
            ).optional(),
            "text": t.string().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn"
                ]
            ).optional(),
            "dtmfDigits": t.string().optional(),
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestOut"] = t.struct(
        {
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoOut"]
            ).optional(),
            "triggerIntent": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "detectIntentResponseId": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
            ).optional(),
            "languageCode": t.string().optional(),
            "transcript": t.string().optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoOut"]
            ).optional(),
            "fulfillmentInfo": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"
                ]
            ).optional(),
            "text": t.string().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut"
                ]
            ).optional(),
            "dtmfDigits": t.string().optional(),
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestOut"])
    types["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"] = t.struct(
        {
            "volumeGainDb": t.number().optional(),
            "voice": t.proxy(
                renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsIn"]
            ).optional(),
            "effectsProfileId": t.array(t.string()).optional(),
            "speakingRate": t.number().optional(),
            "pitch": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"])
    types["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"] = t.struct(
        {
            "volumeGainDb": t.number().optional(),
            "voice": t.proxy(
                renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsOut"]
            ).optional(),
            "effectsProfileId": t.array(t.string()).optional(),
            "speakingRate": t.number().optional(),
            "pitch": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn"
    ] = t.struct(
        {
            "mergeBehavior": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut"
    ] = t.struct(
        {
            "mergeBehavior": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut"]
    )
    types["GoogleCloudDialogflowCxV3StopExperimentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StopExperimentRequestIn"])
    types["GoogleCloudDialogflowCxV3StopExperimentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StopExperimentRequestOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn"
    ] = t.struct(
        {
            "thumbnailUri": t.string().optional(),
            "height": t.string(),
            "fileUri": t.string(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn"]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut"
    ] = t.struct(
        {
            "thumbnailUri": t.string().optional(),
            "height": t.string(),
            "fileUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut"]
    )
    types["GoogleCloudDialogflowCxV3CompareVersionsResponseIn"] = t.struct(
        {
            "targetVersionContentJson": t.string().optional(),
            "baseVersionContentJson": t.string().optional(),
            "compareTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseIn"])
    types["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"] = t.struct(
        {
            "targetVersionContentJson": t.string().optional(),
            "baseVersionContentJson": t.string().optional(),
            "compareTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"])
    types["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"] = t.struct(
        {"state": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn"])
    types["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"])
    types[
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
    ] = t.struct(
        {
            "footer": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
                ]
            ),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
    ] = t.struct(
        {
            "footer": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3WebhookRequestIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"]
            ).optional(),
            "transcript": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoIn"]
            ).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn"
                ]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoIn"]
            ).optional(),
            "triggerEvent": t.string().optional(),
            "text": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "dtmfDigits": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn"]
            ).optional(),
            "detectIntentResponseId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestIn"])
    types["GoogleCloudDialogflowCxV3WebhookRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"]
            ).optional(),
            "transcript": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoOut"]
            ).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut"
                ]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoOut"]
            ).optional(),
            "triggerEvent": t.string().optional(),
            "text": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "dtmfDigits": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut"]
            ).optional(),
            "detectIntentResponseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestOut"])
    types["GoogleCloudDialogflowV2ArticleAnswerIn"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "uri": t.string().optional(),
            "snippets": t.array(t.string()).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleAnswerIn"])
    types["GoogleCloudDialogflowV2ArticleAnswerOut"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "uri": t.string().optional(),
            "snippets": t.array(t.string()).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleAnswerOut"])
    types["GoogleCloudDialogflowV2IntentParameterIn"] = t.struct(
        {
            "entityTypeDisplayName": t.string().optional(),
            "mandatory": t.boolean().optional(),
            "value": t.string().optional(),
            "isList": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "prompts": t.array(t.string()).optional(),
            "defaultValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentParameterIn"])
    types["GoogleCloudDialogflowV2IntentParameterOut"] = t.struct(
        {
            "entityTypeDisplayName": t.string().optional(),
            "mandatory": t.boolean().optional(),
            "value": t.string().optional(),
            "isList": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "prompts": t.array(t.string()).optional(),
            "defaultValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentParameterOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageImageIn"] = t.struct(
        {"imageUri": t.string().optional(), "accessibilityText": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageImageOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "accessibilityText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn"] = t.struct(
        {
            "imageDisplayOptions": t.string().optional(),
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
                    ]
                )
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut"] = t.struct(
        {
            "imageDisplayOptions": t.string().optional(),
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut"])
    types["GoogleCloudDialogflowCxV3VariantsHistoryIn"] = t.struct(
        {
            "versionVariants": t.proxy(
                renames["GoogleCloudDialogflowCxV3VersionVariantsIn"]
            ).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
    types["GoogleCloudDialogflowCxV3VariantsHistoryOut"] = t.struct(
        {
            "versionVariants": t.proxy(
                renames["GoogleCloudDialogflowCxV3VersionVariantsOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VariantsHistoryOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueIn"
    ] = t.struct(
        {
            "resolvedValue": t.struct({"_": t.string().optional()}).optional(),
            "originalValue": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueIn"
        ]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueOut"
    ] = t.struct(
        {
            "resolvedValue": t.struct({"_": t.string().optional()}).optional(),
            "originalValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3ListChangelogsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "changelogs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ChangelogIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListChangelogsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListChangelogsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "changelogs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ChangelogOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListChangelogsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseOut"])
    types["GoogleCloudDialogflowCxV3FulfillIntentRequestIn"] = t.struct(
        {
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"]).optional(),
            "matchIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentRequestIn"])
    types["GoogleCloudDialogflowCxV3FulfillIntentRequestOut"] = t.struct(
        {
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"]).optional(),
            "matchIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowCxV3MatchIntentRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentRequestOut"])
    types["GoogleCloudDialogflowCxV3FulfillIntentResponseIn"] = t.struct(
        {
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultIn"]
            ).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
            "outputAudio": t.string().optional(),
            "responseId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseIn"])
    types["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"] = t.struct(
        {
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultOut"]
            ).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "outputAudio": t.string().optional(),
            "responseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"])
    types["GoogleCloudDialogflowCxV3DeployFlowRequestIn"] = t.struct(
        {"flowVersion": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3DeployFlowRequestOut"] = t.struct(
        {
            "flowVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowRequestOut"])
    types["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn"] = t.struct(
        {
            "enablePredeploymentRun": t.boolean().optional(),
            "enableContinuousRun": t.boolean().optional(),
            "testCases": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut"] = t.struct(
        {
            "enablePredeploymentRun": t.boolean().optional(),
            "enableContinuousRun": t.boolean().optional(),
            "testCases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"] = t.struct(
        {
            "liveAgentHandoff": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn"
                ]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "conversationSuccess": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn"
                ]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn"
                ]
            ).optional(),
            "outputAudioText": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn"
                ]
            ).optional(),
            "channel": t.string().optional(),
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"] = t.struct(
        {
            "liveAgentHandoff": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut"
                ]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "endInteraction": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"
                ]
            ).optional(),
            "conversationSuccess": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut"
                ]
            ).optional(),
            "mixedAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut"
                ]
            ).optional(),
            "outputAudioText": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"
                ]
            ).optional(),
            "channel": t.string().optional(),
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
    types["GoogleCloudDialogflowCxV3ImportFlowRequestIn"] = t.struct(
        {
            "flowUri": t.string().optional(),
            "flowContent": t.string().optional(),
            "importOption": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3ImportFlowRequestOut"] = t.struct(
        {
            "flowUri": t.string().optional(),
            "flowContent": t.string().optional(),
            "importOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowRequestOut"])
    types["GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataIn"])
    types["GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn"] = t.struct(
        {"title": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut"])
    types["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"] = t.struct(
        {"value": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"])
    types["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"])
    types["GoogleCloudDialogflowCxV3MatchIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentIn"]).optional(),
            "matchType": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "event": t.string().optional(),
            "resolvedInput": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIn"])
    types["GoogleCloudDialogflowCxV3MatchOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]).optional(),
            "matchType": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "event": t.string().optional(),
            "resolvedInput": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchOut"])
    types["GoogleCloudDialogflowCxV3ExportAgentRequestIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "agentUri": t.string().optional(),
            "dataFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3ExportAgentRequestOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "agentUri": t.string().optional(),
            "dataFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentRequestOut"])
    types["GoogleCloudDialogflowCxV3beta1EventHandlerIn"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
            "targetPage": t.string().optional(),
            "event": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventHandlerIn"])
    types["GoogleCloudDialogflowCxV3beta1EventHandlerOut"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "name": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "targetPage": t.string().optional(),
            "event": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventHandlerOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn"] = t.struct(
        {
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"]
            ),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "title": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut"] = t.struct(
        {
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"]
            ),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "title": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut"])
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn"] = t.struct(
        {
            "routeGroup": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"]
            ).optional(),
            "coverageScore": t.number().optional(),
            "transitions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn"])
    types[
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut"
    ] = t.struct(
        {
            "routeGroup": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"]
            ).optional(),
            "coverageScore": t.number().optional(),
            "transitions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut"]
    )
    types["GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "continuousTestResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ContinuousTestResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "continuousTestResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ContinuousTestResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn"] = t.struct(
        {
            "webhookOverrides": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1WebhookIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut"] = t.struct(
        {
            "webhookOverrides": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1WebhookOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut"])
    types["GoogleCloudDialogflowCxV3TextToSpeechSettingsIn"] = t.struct(
        {"synthesizeSpeechConfigs": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TextToSpeechSettingsIn"])
    types["GoogleCloudDialogflowCxV3TextToSpeechSettingsOut"] = t.struct(
        {
            "synthesizeSpeechConfigs": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TextToSpeechSettingsOut"])
    types[
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
    ] = t.struct({"urlTypeHint": t.string().optional(), "url": t.string()}).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
    ] = t.struct(
        {
            "urlTypeHint": t.string().optional(),
            "url": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1IntentMessageTextIn"] = t.struct(
        {"text": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTextIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTextOut"] = t.struct(
        {
            "text": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTextOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"] = t.struct(
        {
            "suggestions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn"]
                )
            ).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "media": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"] = t.struct(
        {
            "suggestions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut"]
                )
            ).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "media": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn"] = t.struct(
        {"ssml": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut"] = t.struct(
        {
            "ssml": t.string().optional(),
            "text": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"] = t.struct(
        {"version": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"] = t.struct(
        {"version": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"])
    types["GoogleCloudDialogflowCxV3DetectIntentResponseIn"] = t.struct(
        {
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultIn"]
            ).optional(),
            "outputAudio": t.string().optional(),
            "responseId": t.string().optional(),
            "allowCancellation": t.boolean().optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
            "responseType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentResponseIn"])
    types["GoogleCloudDialogflowCxV3DetectIntentResponseOut"] = t.struct(
        {
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultOut"]
            ).optional(),
            "outputAudio": t.string().optional(),
            "responseId": t.string().optional(),
            "allowCancellation": t.boolean().optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "responseType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentResponseOut"])
    types["GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn"] = t.struct(
        {
            "queryTextSentiment": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn"])
    types["GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut"] = t.struct(
        {
            "queryTextSentiment": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"])
    types["GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn"] = t.struct(
        {
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2FaqAnswerIn"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn"])
    types["GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut"] = t.struct(
        {
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2FaqAnswerOut"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut"])
    types["GoogleCloudDialogflowCxV3VersionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionIn"])
    types["GoogleCloudDialogflowCxV3VersionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsOut"]
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionOut"])
    types["GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseIn"] = t.struct(
        {
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseIn"])
    types["GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseOut"] = t.struct(
        {
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseOut"])
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn"] = t.struct(
        {
            "coverages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn"
                    ]
                )
            ).optional(),
            "coverageScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn"])
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut"] = t.struct(
        {
            "coverages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut"
                    ]
                )
            ).optional(),
            "coverageScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardIn"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"]
                )
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "formattedText": t.string(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardOut"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"]
                )
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "formattedText": t.string(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardOut"])
    types["GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataOut"])
    types["GoogleCloudDialogflowV2SuggestArticlesResponseIn"] = t.struct(
        {
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ArticleAnswerIn"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestArticlesResponseIn"])
    types["GoogleCloudDialogflowV2SuggestArticlesResponseOut"] = t.struct(
        {
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ArticleAnswerOut"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestArticlesResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn"] = t.struct(
        {"horizontalAlignment": t.string().optional(), "header": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut"] = t.struct(
        {
            "horizontalAlignment": t.string().optional(),
            "header": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut"])
    types[
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationModel": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2HumanAgentAssistantEventIn"] = t.struct(
        {
            "participant": t.string().optional(),
            "conversation": t.string().optional(),
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SuggestionResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2HumanAgentAssistantEventIn"])
    types["GoogleCloudDialogflowV2HumanAgentAssistantEventOut"] = t.struct(
        {
            "participant": t.string().optional(),
            "conversation": t.string().optional(),
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SuggestionResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2HumanAgentAssistantEventOut"])
    types["GoogleCloudDialogflowV2ConversationEventIn"] = t.struct(
        {
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2MessageIn"]
            ).optional(),
            "type": t.string().optional(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "conversation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationEventIn"])
    types["GoogleCloudDialogflowV2ConversationEventOut"] = t.struct(
        {
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2MessageOut"]
            ).optional(),
            "type": t.string().optional(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "conversation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationEventOut"])
    types[
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "suggestionFeatureType": t.string(),
            "createTime": t.string().optional(),
            "conversationProfile": t.string().optional(),
            "participantRole": t.string(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut"
    ] = t.struct(
        {
            "suggestionFeatureType": t.string(),
            "createTime": t.string().optional(),
            "conversationProfile": t.string().optional(),
            "participantRole": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3TextInputIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3TextInputIn"])
    types["GoogleCloudDialogflowCxV3TextInputOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TextInputOut"])
    types["GoogleCloudDialogflowCxV3ListDeploymentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deployments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3DeploymentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListDeploymentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListDeploymentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deployments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3DeploymentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListDeploymentsResponseOut"])
    types["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn"] = t.struct(
        {
            "caseContent": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn"
                    ]
                )
            ).optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn"])
    types["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut"] = t.struct(
        {
            "caseContent": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut"
                    ]
                )
            ).optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut"])
    types["GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestErrorIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"] = t.struct(
        {
            "columnProperties": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn"
                    ]
                )
            ).optional(),
            "rows": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn"]
                )
            ).optional(),
            "title": t.string(),
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"
                    ]
                )
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"] = t.struct(
        {
            "columnProperties": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut"
                    ]
                )
            ).optional(),
            "rows": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut"]
                )
            ).optional(),
            "title": t.string(),
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"
                    ]
                )
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"])
    types["GoogleCloudDialogflowV2GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2GcsDestinationIn"])
    types["GoogleCloudDialogflowV2GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2GcsDestinationOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn"] = t.struct(
        {"parameterId": t.string().optional(), "text": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut"] = t.struct(
        {
            "parameterId": t.string().optional(),
            "text": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut"])
    types["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn"] = t.struct(
        {
            "initialPromptFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ),
            "repromptEventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn"])
    types["GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut"] = t.struct(
        {
            "initialPromptFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ),
            "repromptEventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseErrorIn"] = t.struct(
        {
            "testCase": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseIn"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseErrorIn"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseErrorOut"] = t.struct(
        {
            "testCase": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseOut"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseErrorOut"])
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"])
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"])
    types["GoogleCloudDialogflowCxV3IntentCoverageIntentIn"] = t.struct(
        {"covered": t.boolean().optional(), "intent": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentCoverageIntentIn"])
    types["GoogleCloudDialogflowCxV3IntentCoverageIntentOut"] = t.struct(
        {
            "covered": t.boolean().optional(),
            "intent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentCoverageIntentOut"])
    types["GoogleCloudDialogflowCxV3beta1IntentInputIn"] = t.struct(
        {"intent": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentInputIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentInputOut"] = t.struct(
        {"intent": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentInputOut"])
    types["GoogleCloudDialogflowCxV3ValidateAgentRequestIn"] = t.struct(
        {"languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ValidateAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3ValidateAgentRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidateAgentRequestOut"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn"] = t.struct(
        {
            "source": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"]
            ).optional(),
            "index": t.integer().optional(),
            "covered": t.boolean().optional(),
            "transitionRoute": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteIn"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"]
            ).optional(),
            "eventHandler": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventHandlerIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut"] = t.struct(
        {
            "source": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"]
            ).optional(),
            "index": t.integer().optional(),
            "covered": t.boolean().optional(),
            "transitionRoute": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteOut"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"]
            ).optional(),
            "eventHandler": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventHandlerOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut"])
    types["GoogleCloudDialogflowCxV3TestCaseErrorIn"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "testCase": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseErrorIn"])
    types["GoogleCloudDialogflowCxV3TestCaseErrorOut"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "testCase": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseErrorOut"])
    types["GoogleCloudDialogflowCxV3AudioInputIn"] = t.struct(
        {
            "config": t.proxy(renames["GoogleCloudDialogflowCxV3InputAudioConfigIn"]),
            "audio": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AudioInputIn"])
    types["GoogleCloudDialogflowCxV3AudioInputOut"] = t.struct(
        {
            "config": t.proxy(renames["GoogleCloudDialogflowCxV3InputAudioConfigOut"]),
            "audio": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AudioInputOut"])
    types["GoogleCloudDialogflowCxV3VersionVariantsIn"] = t.struct(
        {
            "variants": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VersionVariantsVariantIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionVariantsIn"])
    types["GoogleCloudDialogflowCxV3VersionVariantsOut"] = t.struct(
        {
            "variants": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VersionVariantsVariantOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionVariantsOut"])
    types["GoogleCloudDialogflowCxV3IntentInputIn"] = t.struct(
        {"intent": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentInputIn"])
    types["GoogleCloudDialogflowCxV3IntentInputOut"] = t.struct(
        {"intent": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentInputOut"])
    types["GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataIn"])
    types[
        "GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataOut"
    ] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn"] = t.struct(
        {
            "ssml": t.string().optional(),
            "displayText": t.string().optional(),
            "textToSpeech": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut"] = t.struct(
        {
            "ssml": t.string().optional(),
            "displayText": t.string().optional(),
            "textToSpeech": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1ConversationTurnIn"] = t.struct(
        {
            "userInput": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn"]
            ).optional(),
            "virtualAgentOutput": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnIn"])
    types["GoogleCloudDialogflowCxV3beta1ConversationTurnOut"] = t.struct(
        {
            "userInput": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut"]
            ).optional(),
            "virtualAgentOutput": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnOut"])
    types["GoogleCloudDialogflowCxV3ListFlowsResponseIn"] = t.struct(
        {
            "flows": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FlowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListFlowsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListFlowsResponseOut"] = t.struct(
        {
            "flows": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn"] = t.struct(
        {
            "service": t.string(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut"] = t.struct(
        {
            "service": t.string(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut"])
    types["GoogleCloudDialogflowCxV3TestCaseResultIn"] = t.struct(
        {
            "name": t.string().optional(),
            "testResult": t.string().optional(),
            "environment": t.string().optional(),
            "testTime": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseResultIn"])
    types["GoogleCloudDialogflowCxV3TestCaseResultOut"] = t.struct(
        {
            "name": t.string().optional(),
            "testResult": t.string().optional(),
            "environment": t.string().optional(),
            "testTime": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseResultOut"])
    types["GoogleCloudDialogflowCxV3SessionEntityTypeIn"] = t.struct(
        {
            "entityOverrideMode": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
            ),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionEntityTypeIn"])
    types["GoogleCloudDialogflowCxV3SessionEntityTypeOut"] = t.struct(
        {
            "entityOverrideMode": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityOut"])
            ),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"])
    types["GoogleCloudDialogflowCxV3TestErrorIn"] = t.struct(
        {
            "testTime": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "testCase": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestErrorIn"])
    types["GoogleCloudDialogflowCxV3TestErrorOut"] = t.struct(
        {
            "testTime": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "testCase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestErrorOut"])
    types["GoogleCloudDialogflowV2ConversationModelIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "articleSuggestionModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"]
            ).optional(),
            "smartReplyModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"]
            ).optional(),
            "name": t.string().optional(),
            "datasets": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2InputDatasetIn"])
            ),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationModelIn"])
    types["GoogleCloudDialogflowV2ConversationModelOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "articleSuggestionModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"]
            ).optional(),
            "smartReplyModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"]
            ).optional(),
            "name": t.string().optional(),
            "datasets": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2InputDatasetOut"])
            ),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationModelOut"])
    types["GoogleCloudDialogflowCxV3BatchRunTestCasesResponseIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseResultIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchRunTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3BatchRunTestCasesResponseOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchRunTestCasesResponseOut"])
    types["GoogleCloudDialogflowV2beta1WebhookRequestIn"] = t.struct(
        {
            "session": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn"]
            ).optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1QueryResultIn"]
            ).optional(),
            "responseId": t.string().optional(),
            "alternativeQueryResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1QueryResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookRequestIn"])
    types["GoogleCloudDialogflowV2beta1WebhookRequestOut"] = t.struct(
        {
            "session": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut"]
            ).optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1QueryResultOut"]
            ).optional(),
            "responseId": t.string().optional(),
            "alternativeQueryResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1QueryResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookRequestOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn"
    ] = t.struct({"metadata": t.struct({"_": t.string().optional()}).optional()}).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut"
    ] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut"]
    )
    types["GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestErrorIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataOut"])
    types["GoogleCloudDialogflowCxV3MatchIntentResponseIn"] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
            "transcript": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "text": t.string().optional(),
            "matches": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentResponseIn"])
    types["GoogleCloudDialogflowCxV3MatchIntentResponseOut"] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "transcript": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "text": t.string().optional(),
            "matches": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentResponseOut"])
    types["GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn"] = t.struct(
        {"key": t.string(), "synonyms": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn"])
    types["GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut"] = t.struct(
        {
            "key": t.string(),
            "synonyms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut"])
    types["GoogleCloudDialogflowV2beta1ConversationEventIn"] = t.struct(
        {
            "errorStatus": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "conversation": t.string(),
            "type": t.string(),
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ConversationEventIn"])
    types["GoogleCloudDialogflowV2beta1ConversationEventOut"] = t.struct(
        {
            "errorStatus": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "conversation": t.string(),
            "type": t.string(),
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ConversationEventOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn"
    ] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageIn"]
            ).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn"])
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut"
    ] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageOut"]
            ).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut"])
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentOut"]
            ).optional(),
            "differences": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut"]
    )
    types["GoogleCloudDialogflowCxV3OutputAudioConfigIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "audioEncoding": t.string(),
            "synthesizeSpeechConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3OutputAudioConfigOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "audioEncoding": t.string(),
            "synthesizeSpeechConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn"] = t.struct(
        {"ssml": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"] = t.struct(
        {
            "ssml": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"])
    types["GoogleCloudDialogflowV3alpha1TurnSignalsIn"] = t.struct(
        {
            "triggeredAbandonmentEvent": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "dtmfUsed": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "noUserInput": t.boolean().optional(),
            "reachedEndPage": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "agentEscalated": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1TurnSignalsIn"])
    types["GoogleCloudDialogflowV3alpha1TurnSignalsOut"] = t.struct(
        {
            "triggeredAbandonmentEvent": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "dtmfUsed": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "noUserInput": t.boolean().optional(),
            "reachedEndPage": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "agentEscalated": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1TurnSignalsOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageTextIn"] = t.struct(
        {"text": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageTextIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageTextOut"] = t.struct(
        {
            "allowPlaybackInterruption": t.boolean().optional(),
            "text": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageTextOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn"] = t.struct(
        {
            "cells": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn"]
                )
            ).optional(),
            "dividerAfter": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut"] = t.struct(
        {
            "cells": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut"]
                )
            ).optional(),
            "dividerAfter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut"])
    types[
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn"
    ] = t.struct(
        {
            "additionalCases": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn"]
            ).optional(),
            "message": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut"
    ] = t.struct(
        {
            "additionalCases": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut"]
            ).optional(),
            "message": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1ExportOperationMetadataIn"] = t.struct(
        {
            "exportedGcsDestination": t.proxy(
                renames["GoogleCloudDialogflowV2beta1GcsDestinationIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ExportOperationMetadataIn"])
    types["GoogleCloudDialogflowV2beta1ExportOperationMetadataOut"] = t.struct(
        {
            "exportedGcsDestination": t.proxy(
                renames["GoogleCloudDialogflowV2beta1GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ExportOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn"] = t.struct(
        {
            "required": t.boolean().optional(),
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "justCollected": t.boolean().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut"] = t.struct(
        {
            "required": t.boolean().optional(),
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "justCollected": t.boolean().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageIn"] = t.struct(
        {
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTextIn"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn"]
            ).optional(),
            "rbmText": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCardIn"]
            ).optional(),
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectIn"]
            ).optional(),
            "platform": t.string().optional(),
            "rbmCarouselRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn"]
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn"
                ]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn"]
            ).optional(),
            "telephonySynthesizeSpeech": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn"
                ]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"]
            ).optional(),
            "rbmStandaloneRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn"]
            ).optional(),
            "telephonyPlayAudio": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageOut"] = t.struct(
        {
            "browseCarouselCard": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut"
                ]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTextOut"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut"]
            ).optional(),
            "rbmText": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCardOut"]
            ).optional(),
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectOut"]
            ).optional(),
            "platform": t.string().optional(),
            "rbmCarouselRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut"]
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut"
                ]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut"]
            ).optional(),
            "telephonySynthesizeSpeech": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut"
                ]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"]
            ).optional(),
            "rbmStandaloneRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut"]
            ).optional(),
            "telephonyPlayAudio": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"
                ]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"] = t.struct(
        {"key": t.string(), "synonyms": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"] = t.struct(
        {
            "key": t.string(),
            "synonyms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn"] = t.struct(
        {
            "cases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn"])
    types["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut"] = t.struct(
        {
            "cases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut"])
    types["GoogleCloudDialogflowV2SmartReplyAnswerIn"] = t.struct(
        {
            "reply": t.string().optional(),
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SmartReplyAnswerIn"])
    types["GoogleCloudDialogflowV2SmartReplyAnswerOut"] = t.struct(
        {
            "reply": t.string().optional(),
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SmartReplyAnswerOut"])
    types["GoogleCloudDialogflowCxV3ExportFlowRequestIn"] = t.struct(
        {
            "includeReferencedFlows": t.boolean().optional(),
            "flowUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3ExportFlowRequestOut"] = t.struct(
        {
            "includeReferencedFlows": t.boolean().optional(),
            "flowUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportFlowRequestOut"])
    types["GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn"] = t.struct(
        {"header": t.string(), "horizontalAlignment": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn"])
    types["GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut"] = t.struct(
        {
            "header": t.string(),
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut"])
    types["GoogleCloudDialogflowCxV3ImportFlowResponseIn"] = t.struct(
        {"flow": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportFlowResponseOut"] = t.struct(
        {
            "flow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1AudioInputIn"] = t.struct(
        {
            "audio": t.string().optional(),
            "config": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigIn"]
            ),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1AudioInputIn"])
    types["GoogleCloudDialogflowCxV3beta1AudioInputOut"] = t.struct(
        {
            "audio": t.string().optional(),
            "config": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1AudioInputOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn"
                    ]
                )
            )
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut"])
    types["GoogleCloudDialogflowCxV3QueryInputIn"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventInputIn"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentInputIn"]
            ).optional(),
            "dtmf": t.proxy(renames["GoogleCloudDialogflowCxV3DtmfInputIn"]).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3AudioInputIn"]
            ).optional(),
            "languageCode": t.string(),
            "text": t.proxy(renames["GoogleCloudDialogflowCxV3TextInputIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryInputIn"])
    types["GoogleCloudDialogflowCxV3QueryInputOut"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventInputOut"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentInputOut"]
            ).optional(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3DtmfInputOut"]
            ).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3AudioInputOut"]
            ).optional(),
            "languageCode": t.string(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryInputOut"])
    types[
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn"
    ] = t.struct(
        {
            "contentUrl": t.string(),
            "description": t.string().optional(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "name": t.string(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn"]
    )
    types[
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut"
    ] = t.struct(
        {
            "contentUrl": t.string(),
            "description": t.string().optional(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut"
        ]
    )
    types["GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataIn"])
    types["GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3RunTestCaseResponseIn"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseResponseIn"])
    types["GoogleCloudDialogflowCxV3RunTestCaseResponseOut"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseResponseOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"] = t.struct(
        {"metadata": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"])
    types["GoogleCloudDialogflowV2WebhookRequestIn"] = t.struct(
        {
            "session": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"]
            ).optional(),
            "responseId": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2QueryResultIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookRequestIn"])
    types["GoogleCloudDialogflowV2WebhookRequestOut"] = t.struct(
        {
            "session": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"]
            ).optional(),
            "responseId": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2QueryResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookRequestOut"])
    types["GoogleCloudDialogflowV2IntentMessageTextIn"] = t.struct(
        {"text": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTextIn"])
    types["GoogleCloudDialogflowV2IntentMessageTextOut"] = t.struct(
        {
            "text": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTextOut"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn"] = t.struct(
        {
            "cases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut"] = t.struct(
        {
            "cases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut"])
    types["GoogleCloudDialogflowCxV3AgentIn"] = t.struct(
        {
            "supportedLanguageCodes": t.array(t.string()).optional(),
            "speechToTextSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"]
            ).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "securitySettings": t.string().optional(),
            "textToSpeechSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextToSpeechSettingsIn"]
            ).optional(),
            "enableSpellCorrection": t.boolean().optional(),
            "avatarUri": t.string().optional(),
            "advancedSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsIn"]
            ).optional(),
            "description": t.string().optional(),
            "timeZone": t.string(),
            "name": t.string().optional(),
            "defaultLanguageCode": t.string(),
            "startFlow": t.string().optional(),
            "locked": t.boolean().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentIn"])
    types["GoogleCloudDialogflowCxV3AgentOut"] = t.struct(
        {
            "supportedLanguageCodes": t.array(t.string()).optional(),
            "speechToTextSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"]
            ).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "securitySettings": t.string().optional(),
            "textToSpeechSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextToSpeechSettingsOut"]
            ).optional(),
            "enableSpellCorrection": t.boolean().optional(),
            "avatarUri": t.string().optional(),
            "advancedSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsOut"]
            ).optional(),
            "description": t.string().optional(),
            "timeZone": t.string(),
            "name": t.string().optional(),
            "defaultLanguageCode": t.string(),
            "startFlow": t.string().optional(),
            "locked": t.boolean().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"] = t.struct(
        {"metadata": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"] = t.struct(
        {
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn"
                ]
            ),
            "title": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"] = t.struct(
        {
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut"
                ]
            ),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"])
    types["GoogleCloudDialogflowCxV3TestConfigIn"] = t.struct(
        {
            "page": t.string().optional(),
            "flow": t.string().optional(),
            "trackingParameters": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestConfigIn"])
    types["GoogleCloudDialogflowCxV3TestConfigOut"] = t.struct(
        {
            "page": t.string().optional(),
            "flow": t.string().optional(),
            "trackingParameters": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestConfigOut"])
    types["GoogleCloudDialogflowV2IntentMessageMediaContentIn"] = t.struct(
        {
            "mediaObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn"
                    ]
                )
            ),
            "mediaType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageMediaContentIn"])
    types["GoogleCloudDialogflowV2IntentMessageMediaContentOut"] = t.struct(
        {
            "mediaObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut"
                    ]
                )
            ),
            "mediaType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageMediaContentOut"])
    types["GoogleCloudDialogflowV2beta1EventInputIn"] = t.struct(
        {
            "name": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "languageCode": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EventInputIn"])
    types["GoogleCloudDialogflowV2beta1EventInputOut"] = t.struct(
        {
            "name": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EventInputOut"])
    types["GoogleCloudDialogflowCxV3beta1IntentIn"] = t.struct(
        {
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn"])
            ).optional(),
            "name": t.string().optional(),
            "isFallback": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentParameterIn"])
            ).optional(),
            "priority": t.integer().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentOut"] = t.struct(
        {
            "trainingPhrases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut"]
                )
            ).optional(),
            "name": t.string().optional(),
            "isFallback": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentParameterOut"])
            ).optional(),
            "priority": t.integer().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentOut"])
    types[
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn"] = t.struct(
        {"agentUri": t.string().optional(), "agentContent": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "agentContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut"])
    types["GoogleCloudDialogflowCxV3RunTestCaseRequestIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseRequestIn"])
    types["GoogleCloudDialogflowCxV3RunTestCaseRequestOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseRequestOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn"] = t.struct(
        {"audioUri": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut"] = t.struct(
        {
            "allowPlaybackInterruption": t.boolean().optional(),
            "audioUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut"])
    types["GoogleCloudDialogflowCxV3SessionInfoIn"] = t.struct(
        {
            "session": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionInfoIn"])
    types["GoogleCloudDialogflowCxV3SessionInfoOut"] = t.struct(
        {
            "session": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionInfoOut"])
    types[
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn"
    ] = t.struct(
        {"score": t.number().optional(), "magnitude": t.number().optional()}
    ).named(
        renames["GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut"
    ] = t.struct(
        {
            "score": t.number().optional(),
            "magnitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut"]
    )
    types["GoogleCloudDialogflowCxV3PageIn"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
            ).optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
            "name": t.string().optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
            ).optional(),
            "displayName": t.string(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageIn"])
    types["GoogleCloudDialogflowCxV3PageOut"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
            ).optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormOut"]).optional(),
            "name": t.string().optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
            ).optional(),
            "displayName": t.string(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageOut"])
    types["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn"] = t.struct(
        {
            "faqQuestion": t.string().optional(),
            "source": t.string().optional(),
            "matchConfidenceLevel": t.string().optional(),
            "matchConfidence": t.number().optional(),
            "answer": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn"])
    types["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut"] = t.struct(
        {
            "faqQuestion": t.string().optional(),
            "source": t.string().optional(),
            "matchConfidenceLevel": t.string().optional(),
            "matchConfidence": t.number().optional(),
            "answer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn"] = t.struct(
        {
            "mediaObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn"
                    ]
                )
            ),
            "mediaType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut"] = t.struct(
        {
            "mediaObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut"
                    ]
                )
            ),
            "mediaType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut"])
    types["GoogleCloudDialogflowCxV3ListVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VersionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListVersionsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"])
    types["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn"] = t.struct(
        {
            "conversation": t.string().optional(),
            "participant": t.string().optional(),
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SuggestionResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn"])
    types["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut"] = t.struct(
        {
            "conversation": t.string().optional(),
            "participant": t.string().optional(),
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SuggestionResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut"])
    types[
        "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut"
    ] = t.struct(
        {"state": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(
        renames["GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2SuggestionResultIn"] = t.struct(
        {
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn"]
            ).optional(),
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestArticlesResponseIn"]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn"]
            ).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestionResultIn"])
    types["GoogleCloudDialogflowV2SuggestionResultOut"] = t.struct(
        {
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut"]
            ).optional(),
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestArticlesResponseOut"]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestionResultOut"])
    types["GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentIn"]
            ).optional(),
            "deployment": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentOut"]
            ).optional(),
            "deployment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut"])
    types[
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationModel": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn"] = t.struct(
        {
            "latestMessage": t.string().optional(),
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1FaqAnswerIn"])
            ).optional(),
            "contextSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut"] = t.struct(
        {
            "latestMessage": t.string().optional(),
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1FaqAnswerOut"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut"])
    types["GoogleCloudDialogflowCxV3ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowCxV3ConversationTurnUserInputIn"] = t.struct(
        {
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryInputIn"]
            ).optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputIn"])
    types["GoogleCloudDialogflowCxV3ConversationTurnUserInputOut"] = t.struct(
        {
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryInputOut"]
            ).optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookIn"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"]
            ).optional(),
            "timeout": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "serviceDirectory": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut"
                ]
            ).optional(),
            "displayName": t.string(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"]
            ).optional(),
            "timeout": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn"] = t.struct(
        {"postback": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut"] = t.struct(
        {
            "postback": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut"])
    types["GoogleCloudDialogflowCxV3StartExperimentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StartExperimentRequestIn"])
    types["GoogleCloudDialogflowCxV3StartExperimentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StartExperimentRequestOut"])
    types["GoogleCloudDialogflowV2ExportOperationMetadataIn"] = t.struct(
        {
            "exportedGcsDestination": t.proxy(
                renames["GoogleCloudDialogflowV2GcsDestinationIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2ExportOperationMetadataIn"])
    types["GoogleCloudDialogflowV2ExportOperationMetadataOut"] = t.struct(
        {
            "exportedGcsDestination": t.proxy(
                renames["GoogleCloudDialogflowV2GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ExportOperationMetadataOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn"
    ] = t.struct(
        {
            "contentUrl": t.string(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut"
    ] = t.struct(
        {
            "contentUrl": t.string(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn"] = t.struct(
        {
            "suggestions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn"]
                )
            )
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut"] = t.struct(
        {
            "suggestions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut"])
    types["GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataIn"])
    types[
        "GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataOut"
    ] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowCxV3ImportTestCasesResponseIn"] = t.struct(
        {"names": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportTestCasesResponseOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1RunTestCaseResponseIn"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunTestCaseResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1RunTestCaseResponseOut"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunTestCaseResponseOut"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageIn"] = t.struct(
        {
            "coverageScore": t.number().optional(),
            "transitions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageIn"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageOut"] = t.struct(
        {
            "coverageScore": t.number().optional(),
            "transitions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageOut"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"] = t.struct(
        {
            "alias": t.string().optional(),
            "userDefined": t.boolean().optional(),
            "entityType": t.string().optional(),
            "text": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"] = t.struct(
        {
            "alias": t.string().optional(),
            "userDefined": t.boolean().optional(),
            "entityType": t.string().optional(),
            "text": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"] = t.struct(
        {
            "timesAddedCount": t.integer().optional(),
            "name": t.string().optional(),
            "type": t.string(),
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"]
                )
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"] = t.struct(
        {
            "timesAddedCount": t.integer().optional(),
            "name": t.string().optional(),
            "type": t.string(),
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"])
    types["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn"] = t.struct(
        {
            "enableInteractionLogging": t.boolean().optional(),
            "enableStackdriverLogging": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn"])
    types["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut"] = t.struct(
        {
            "enableInteractionLogging": t.boolean().optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut"])
    types["GoogleCloudDialogflowV2ContextIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "lifespanCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ContextIn"])
    types["GoogleCloudDialogflowV2ContextOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "lifespanCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ContextOut"])
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn"
    ] = t.struct(
        {
            "conversationDataset": t.string().optional(),
            "importCount": t.integer().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn"]
    )
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut"
    ] = t.struct(
        {
            "conversationDataset": t.string().optional(),
            "importCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut"]
    )
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn"] = t.struct(
        {"postbackData": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut"] = t.struct(
        {
            "postbackData": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut"])
    types["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn"] = t.struct(
        {
            "description": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn"]
            ),
            "title": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn"])
    types["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut"] = t.struct(
        {
            "description": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut"]
            ),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut"])
    types["GoogleCloudDialogflowCxV3WebhookResponseIn"] = t.struct(
        {
            "fulfillmentResponse": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn"]
            ).optional(),
            "targetPage": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoIn"]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoIn"]
            ).optional(),
            "targetFlow": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseIn"])
    types["GoogleCloudDialogflowCxV3WebhookResponseOut"] = t.struct(
        {
            "fulfillmentResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut"
                ]
            ).optional(),
            "targetPage": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoOut"]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoOut"]
            ).optional(),
            "targetFlow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1DtmfInputIn"] = t.struct(
        {"digits": t.string().optional(), "finishDigit": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1DtmfInputIn"])
    types["GoogleCloudDialogflowCxV3beta1DtmfInputOut"] = t.struct(
        {
            "digits": t.string().optional(),
            "finishDigit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DtmfInputOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn"
    ] = t.struct(
        {"magnitude": t.number().optional(), "score": t.number().optional()}
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut"
    ] = t.struct(
        {
            "magnitude": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataIn"] = t.struct(
        {
            "knowledgeBase": t.string().optional(),
            "exportOperationMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2beta1ExportOperationMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataIn"])
    types["GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut"] = t.struct(
        {
            "state": t.string(),
            "knowledgeBase": t.string().optional(),
            "exportOperationMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2beta1ExportOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut"])
    types["GoogleCloudDialogflowV2IntentMessageImageIn"] = t.struct(
        {"accessibilityText": t.string().optional(), "imageUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageImageIn"])
    types["GoogleCloudDialogflowV2IntentMessageImageOut"] = t.struct(
        {
            "accessibilityText": t.string().optional(),
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageImageOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn"] = t.struct(
        {
            "simpleResponses": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn"]
                )
            )
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut"] = t.struct(
        {
            "simpleResponses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut"])
    types["GoogleCloudDialogflowCxV3beta1FormParameterIn"] = t.struct(
        {
            "required": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string(),
            "isList": t.boolean().optional(),
            "entityType": t.string(),
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn"]
            ),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterIn"])
    types["GoogleCloudDialogflowCxV3beta1FormParameterOut"] = t.struct(
        {
            "required": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string(),
            "isList": t.boolean().optional(),
            "entityType": t.string(),
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterOut"])
    types["GoogleCloudDialogflowCxV3DeploymentIn"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "flowVersion": t.string().optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3DeploymentResultIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentIn"])
    types["GoogleCloudDialogflowCxV3DeploymentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "flowVersion": t.string().optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3DeploymentResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn"
    ] = t.struct({"uri": t.string()}).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut"
    ] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut"
        ]
    )
    types["GoogleCloudDialogflowV2IntentMessageTableCardRowIn"] = t.struct(
        {
            "cells": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellIn"])
            ).optional(),
            "dividerAfter": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowIn"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardRowOut"] = t.struct(
        {
            "cells": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellOut"])
            ).optional(),
            "dividerAfter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowOut"])
    types["GoogleCloudDialogflowCxV3QueryParametersIn"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeIn"])
            ).optional(),
            "analyzeQueryTextSentiment": t.boolean().optional(),
            "disableWebhook": t.boolean().optional(),
            "webhookHeaders": t.struct({"_": t.string().optional()}).optional(),
            "channel": t.string().optional(),
            "currentPage": t.string().optional(),
            "geoLocation": t.proxy(renames["GoogleTypeLatLngIn"]).optional(),
            "flowVersions": t.array(t.string()).optional(),
            "timeZone": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryParametersIn"])
    types["GoogleCloudDialogflowCxV3QueryParametersOut"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"])
            ).optional(),
            "analyzeQueryTextSentiment": t.boolean().optional(),
            "disableWebhook": t.boolean().optional(),
            "webhookHeaders": t.struct({"_": t.string().optional()}).optional(),
            "channel": t.string().optional(),
            "currentPage": t.string().optional(),
            "geoLocation": t.proxy(renames["GoogleTypeLatLngOut"]).optional(),
            "flowVersions": t.array(t.string()).optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryParametersOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut"])
    types["GoogleCloudDialogflowV2beta1MessageIn"] = t.struct(
        {
            "content": t.string(),
            "sendTime": t.string().optional(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1MessageIn"])
    types["GoogleCloudDialogflowV2beta1MessageOut"] = t.struct(
        {
            "content": t.string(),
            "participant": t.string().optional(),
            "sendTime": t.string().optional(),
            "participantRole": t.string().optional(),
            "name": t.string().optional(),
            "sentimentAnalysis": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "createTime": t.string().optional(),
            "messageAnnotation": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1MessageOut"])
    types["GoogleCloudDialogflowV2ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV2ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV2ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowCxV3TestCaseIn"] = t.struct(
        {
            "name": t.string().optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestConfigIn"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "displayName": t.string(),
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
            ).optional(),
            "notes": t.string().optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseIn"])
    types["GoogleCloudDialogflowCxV3TestCaseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestConfigOut"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "creationTime": t.string().optional(),
            "displayName": t.string(),
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnOut"])
            ).optional(),
            "notes": t.string().optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseOut"])
    types["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn"] = t.struct(
        {
            "mergeBehavior": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn"])
    types["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut"] = t.struct(
        {
            "mergeBehavior": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut"])
    types["GoogleCloudDialogflowV2ExportAgentResponseIn"] = t.struct(
        {"agentContent": t.string().optional(), "agentUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2ExportAgentResponseIn"])
    types["GoogleCloudDialogflowV2ExportAgentResponseOut"] = t.struct(
        {
            "agentContent": t.string().optional(),
            "agentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ExportAgentResponseOut"])
    types["GoogleCloudDialogflowCxV3ListEntityTypesResponseIn"] = t.struct(
        {
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListEntityTypesResponseIn"])
    types["GoogleCloudDialogflowCxV3ListEntityTypesResponseOut"] = t.struct(
        {
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListEntityTypesResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentParameterIn"] = t.struct(
        {
            "prompts": t.array(t.string()).optional(),
            "isList": t.boolean().optional(),
            "mandatory": t.boolean().optional(),
            "displayName": t.string(),
            "entityTypeDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "defaultValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentParameterIn"])
    types["GoogleCloudDialogflowV2beta1IntentParameterOut"] = t.struct(
        {
            "prompts": t.array(t.string()).optional(),
            "isList": t.boolean().optional(),
            "mandatory": t.boolean().optional(),
            "displayName": t.string(),
            "entityTypeDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "defaultValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentParameterOut"])
    types["GoogleCloudDialogflowV2QueryResultIn"] = t.struct(
        {
            "speechRecognitionConfidence": t.number().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowV2IntentIn"]).optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "fulfillmentText": t.string().optional(),
            "queryText": t.string().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "action": t.string().optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultIn"]
            ).optional(),
            "webhookSource": t.string().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2QueryResultIn"])
    types["GoogleCloudDialogflowV2QueryResultOut"] = t.struct(
        {
            "speechRecognitionConfidence": t.number().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowV2IntentOut"]).optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "fulfillmentText": t.string().optional(),
            "queryText": t.string().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "action": t.string().optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultOut"]
            ).optional(),
            "webhookSource": t.string().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2QueryResultOut"])
    types["GoogleCloudDialogflowV2beta1SuggestionResultIn"] = t.struct(
        {
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn"]
            ).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestionResultIn"])
    types["GoogleCloudDialogflowV2beta1SuggestionResultOut"] = t.struct(
        {
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestionResultOut"])
    types["GoogleCloudDialogflowCxV3beta1TurnSignalsIn"] = t.struct(
        {
            "agentEscalated": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "sentimentScore": t.number().optional(),
            "userEscalated": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "reachedEndPage": t.boolean().optional(),
            "noUserInput": t.boolean().optional(),
            "dtmfUsed": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TurnSignalsIn"])
    types["GoogleCloudDialogflowCxV3beta1TurnSignalsOut"] = t.struct(
        {
            "agentEscalated": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "sentimentScore": t.number().optional(),
            "userEscalated": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "reachedEndPage": t.boolean().optional(),
            "noUserInput": t.boolean().optional(),
            "dtmfUsed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TurnSignalsOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
    ] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
                ]
            ),
            "footer": t.string().optional(),
            "title": t.string(),
            "description": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
    ] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
                ]
            ),
            "footer": t.string().optional(),
            "title": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "lastMatchedIntent": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "lastMatchedIntent": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut"])
    types["GoogleCloudDialogflowCxV3ListIntentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListIntentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListIntentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListIntentsResponseOut"])
    types[
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn"
    ] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "conversationModelEvaluation": t.string().optional(),
            "conversationModel": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut"
    ] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "conversationModelEvaluation": t.string().optional(),
            "conversationModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1EntityTypeIn"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"])
            ).optional(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "kind": t.string(),
            "autoExpansionMode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeIn"])
    types["GoogleCloudDialogflowV2beta1EntityTypeOut"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"])
            ).optional(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "kind": t.string(),
            "autoExpansionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeOut"])
    types[
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn"
    ] = t.struct(
        {
            "covered": t.boolean().optional(),
            "transitionRoute": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteIn"]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn"
        ]
    )
    types[
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut"
    ] = t.struct(
        {
            "covered": t.boolean().optional(),
            "transitionRoute": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn"] = t.struct(
        {
            "cardContents": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"]
                )
            ),
            "cardWidth": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut"] = t.struct(
        {
            "cardContents": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"
                    ]
                )
            ),
            "cardWidth": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut"])
    types["GoogleCloudDialogflowCxV3DeployFlowMetadataIn"] = t.struct(
        {
            "testErrors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestErrorIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowMetadataIn"])
    types["GoogleCloudDialogflowCxV3DeployFlowMetadataOut"] = t.struct(
        {
            "testErrors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowMetadataOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn"] = t.struct(
        {"phoneNumber": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn"])
    types[
        "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut"
    ] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut"]
    )
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn"] = t.struct(
        {
            "action": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn"]
            ).optional(),
            "reply": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut"] = t.struct(
        {
            "action": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut"
                ]
            ).optional(),
            "reply": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut"])
    types["GoogleCloudDialogflowV2beta1ExportAgentResponseIn"] = t.struct(
        {"agentContent": t.string().optional(), "agentUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1ExportAgentResponseIn"])
    types["GoogleCloudDialogflowV2beta1ExportAgentResponseOut"] = t.struct(
        {
            "agentContent": t.string().optional(),
            "agentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ExportAgentResponseOut"])
    types["GoogleCloudDialogflowV2FaqAnswerIn"] = t.struct(
        {
            "answer": t.string().optional(),
            "source": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "question": t.string().optional(),
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2FaqAnswerIn"])
    types["GoogleCloudDialogflowV2FaqAnswerOut"] = t.struct(
        {
            "answer": t.string().optional(),
            "source": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "question": t.string().optional(),
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2FaqAnswerOut"])
    types["GoogleCloudDialogflowCxV3MatchIntentRequestIn"] = t.struct(
        {
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
            ).optional(),
            "persistParameterChanges": t.boolean().optional(),
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"])
    types["GoogleCloudDialogflowCxV3MatchIntentRequestOut"] = t.struct(
        {
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersOut"]
            ).optional(),
            "persistParameterChanges": t.boolean().optional(),
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentRequestOut"])
    types["GoogleCloudDialogflowV2beta1FaqAnswerIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "source": t.string().optional(),
            "answer": t.string().optional(),
            "question": t.string().optional(),
            "answerRecord": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1FaqAnswerIn"])
    types["GoogleCloudDialogflowV2beta1FaqAnswerOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "source": t.string().optional(),
            "answer": t.string().optional(),
            "question": t.string().optional(),
            "answerRecord": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1FaqAnswerOut"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn"] = t.struct(
        {"text": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut"] = t.struct(
        {
            "text": t.array(t.string()),
            "allowPlaybackInterruption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut"])
    types["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn"] = t.struct(
        {"uri": t.string(), "destinationName": t.string()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn"])
    types["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut"] = t.struct(
        {
            "uri": t.string(),
            "destinationName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut"])
    types["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn"] = t.struct(
        {
            "transitionRouteGroups": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"] = t.struct(
        {
            "transitionRouteGroups": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"])
    types["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"] = t.struct(
        {"tag": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"])
    types["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"]
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut"])
    types[
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationModel": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationModel": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowCxV3NluSettingsIn"] = t.struct(
        {
            "modelTrainingMode": t.string().optional(),
            "classificationThreshold": t.number().optional(),
            "modelType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3NluSettingsIn"])
    types["GoogleCloudDialogflowCxV3NluSettingsOut"] = t.struct(
        {
            "modelTrainingMode": t.string().optional(),
            "classificationThreshold": t.number().optional(),
            "modelType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3NluSettingsOut"])
    types["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"] = t.struct(
        {
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ArticleAnswerIn"])
            ).optional(),
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"] = t.struct(
        {
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ArticleAnswerOut"])
            ).optional(),
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1InputAudioConfigIn"] = t.struct(
        {
            "phraseHints": t.array(t.string()).optional(),
            "enableWordInfo": t.boolean().optional(),
            "singleUtterance": t.boolean().optional(),
            "modelVariant": t.string().optional(),
            "sampleRateHertz": t.integer().optional(),
            "audioEncoding": t.string(),
            "model": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1InputAudioConfigOut"] = t.struct(
        {
            "phraseHints": t.array(t.string()).optional(),
            "enableWordInfo": t.boolean().optional(),
            "singleUtterance": t.boolean().optional(),
            "modelVariant": t.string().optional(),
            "sampleRateHertz": t.integer().optional(),
            "audioEncoding": t.string(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigOut"])
    types["GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestErrorIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"] = t.struct(
        {"tag": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"])
    types["GoogleCloudDialogflowCxV3ConversationSignalsIn"] = t.struct(
        {"turnSignals": t.proxy(renames["GoogleCloudDialogflowCxV3TurnSignalsIn"])}
    ).named(renames["GoogleCloudDialogflowCxV3ConversationSignalsIn"])
    types["GoogleCloudDialogflowCxV3ConversationSignalsOut"] = t.struct(
        {
            "turnSignals": t.proxy(renames["GoogleCloudDialogflowCxV3TurnSignalsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationSignalsOut"])
    types["GoogleCloudDialogflowCxV3EntityTypeIn"] = t.struct(
        {
            "enableFuzzyExtraction": t.boolean().optional(),
            "name": t.string().optional(),
            "redact": t.boolean().optional(),
            "excludedPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"])
            ).optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
            ).optional(),
            "autoExpansionMode": t.string().optional(),
            "kind": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeIn"])
    types["GoogleCloudDialogflowCxV3EntityTypeOut"] = t.struct(
        {
            "enableFuzzyExtraction": t.boolean().optional(),
            "name": t.string().optional(),
            "redact": t.boolean().optional(),
            "excludedPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"])
            ).optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityOut"])
            ).optional(),
            "autoExpansionMode": t.string().optional(),
            "kind": t.string(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeOut"])
    types["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"] = t.struct(
        {
            "source": t.string().optional(),
            "version": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"])
    types["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"] = t.struct(
        {
            "source": t.string().optional(),
            "version": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"])
    types["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"] = t.struct(
        {
            "service": t.string(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"])
    types["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut"] = t.struct(
        {
            "service": t.string(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut"])
    types["GoogleCloudDialogflowCxV3beta1SessionInfoIn"] = t.struct(
        {
            "session": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1SessionInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1SessionInfoOut"] = t.struct(
        {
            "session": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1SessionInfoOut"])
    types["GoogleCloudDialogflowCxV3DetectIntentRequestIn"] = t.struct(
        {
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
            ).optional(),
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentRequestIn"])
    types["GoogleCloudDialogflowCxV3DetectIntentRequestOut"] = t.struct(
        {
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersOut"]
            ).optional(),
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentRequestOut"])
    types["GoogleCloudDialogflowCxV3PageInfoFormInfoIn"] = t.struct(
        {
            "parameterInfo": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoFormInfoIn"])
    types["GoogleCloudDialogflowCxV3PageInfoFormInfoOut"] = t.struct(
        {
            "parameterInfo": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoFormInfoOut"])
    types[
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "conversationProfile": t.string().optional(),
            "participantRole": t.string(),
            "suggestionFeatureType": t.string(),
            "createTime": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut"
    ] = t.struct(
        {
            "conversationProfile": t.string().optional(),
            "participantRole": t.string(),
            "suggestionFeatureType": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3IntentCoverageIn"] = t.struct(
        {
            "coverageScore": t.number().optional(),
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentCoverageIntentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentCoverageIn"])
    types["GoogleCloudDialogflowCxV3IntentCoverageOut"] = t.struct(
        {
            "coverageScore": t.number().optional(),
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentCoverageIntentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentCoverageOut"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut"])
    types["GoogleCloudDialogflowV2MessageAnnotationIn"] = t.struct(
        {
            "containEntities": t.boolean().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2AnnotatedMessagePartIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageAnnotationIn"])
    types["GoogleCloudDialogflowV2MessageAnnotationOut"] = t.struct(
        {
            "containEntities": t.boolean().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2AnnotatedMessagePartOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageAnnotationOut"])
    types["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn"] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageTextIn"])
            ).optional(),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentIn"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn"])
    types["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut"] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "differences": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestRunDifferenceOut"])
            ).optional(),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageTextOut"])
            ).optional(),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentOut"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut"])
    types["GoogleCloudDialogflowCxV3ListWebhooksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "webhooks": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3WebhookIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseIn"])
    types["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "webhooks": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn"] = t.struct(
        {
            "enableSentimentAnalysis": t.boolean().optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1QueryInputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn"])
    types["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut"] = t.struct(
        {
            "enableSentimentAnalysis": t.boolean().optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1QueryInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn"
    ] = t.struct({"ssml": t.string().optional(), "text": t.string().optional()}).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn"]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut"
    ] = t.struct(
        {
            "ssml": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut"]
    )
    types["GoogleCloudDialogflowCxV3ImportTestCasesMetadataIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseErrorIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3ImportTestCasesMetadataOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataIn"])
    types[
        "GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataOut"
    ] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"] = t.struct(
        {
            "enableContinuousRun": t.boolean().optional(),
            "enablePredeploymentRun": t.boolean().optional(),
            "testCases": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"] = t.struct(
        {
            "enableContinuousRun": t.boolean().optional(),
            "enablePredeploymentRun": t.boolean().optional(),
            "testCases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesRequestIn"] = t.struct(
        {
            "dataFormat": t.string().optional(),
            "gcsUri": t.string().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesRequestOut"] = t.struct(
        {
            "dataFormat": t.string().optional(),
            "gcsUri": t.string().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesRequestOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"] = t.struct(
        {
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn"
                ]
            ),
            "title": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"] = t.struct(
        {
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut"
                ]
            ),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"])
    types["GoogleCloudDialogflowCxV3VersionVariantsVariantIn"] = t.struct(
        {
            "version": t.string().optional(),
            "trafficAllocation": t.number().optional(),
            "isControlGroup": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionVariantsVariantIn"])
    types["GoogleCloudDialogflowCxV3VersionVariantsVariantOut"] = t.struct(
        {
            "version": t.string().optional(),
            "trafficAllocation": t.number().optional(),
            "isControlGroup": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionVariantsVariantOut"])
    types["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn"] = t.struct(
        {"flow": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut"] = t.struct(
        {
            "flow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1PageIn"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerIn"])
            ).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"])
            ).optional(),
            "name": t.string().optional(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3beta1FormIn"]).optional(),
            "displayName": t.string(),
            "transitionRouteGroups": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageIn"])
    types["GoogleCloudDialogflowCxV3beta1PageOut"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerOut"])
            ).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteOut"])
            ).optional(),
            "name": t.string().optional(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "form": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FormOut"]
            ).optional(),
            "displayName": t.string(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageOut"])
    types["GoogleCloudDialogflowV3alpha1ConversationSignalsIn"] = t.struct(
        {"turnSignals": t.proxy(renames["GoogleCloudDialogflowV3alpha1TurnSignalsIn"])}
    ).named(renames["GoogleCloudDialogflowV3alpha1ConversationSignalsIn"])
    types["GoogleCloudDialogflowV3alpha1ConversationSignalsOut"] = t.struct(
        {
            "turnSignals": t.proxy(
                renames["GoogleCloudDialogflowV3alpha1TurnSignalsOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1ConversationSignalsOut"])
    types["GoogleCloudDialogflowV2SentimentAnalysisResultIn"] = t.struct(
        {
            "queryTextSentiment": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2SentimentAnalysisResultIn"])
    types["GoogleCloudDialogflowV2SentimentAnalysisResultOut"] = t.struct(
        {
            "queryTextSentiment": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SentimentAnalysisResultOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn"])
    types["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsIn"] = t.struct(
        {
            "insightsExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn"
                ]
            ).optional(),
            "redactionScope": t.string().optional(),
            "purgeDataTypes": t.array(t.string()).optional(),
            "deidentifyTemplate": t.string().optional(),
            "retentionWindowDays": t.integer().optional(),
            "displayName": t.string(),
            "audioExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"
                ]
            ).optional(),
            "redactionStrategy": t.string().optional(),
            "name": t.string().optional(),
            "inspectTemplate": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsIn"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsOut"] = t.struct(
        {
            "insightsExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut"
                ]
            ).optional(),
            "redactionScope": t.string().optional(),
            "purgeDataTypes": t.array(t.string()).optional(),
            "deidentifyTemplate": t.string().optional(),
            "retentionWindowDays": t.integer().optional(),
            "displayName": t.string(),
            "audioExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"
                ]
            ).optional(),
            "redactionStrategy": t.string().optional(),
            "name": t.string().optional(),
            "inspectTemplate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"])
    types[
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "conversationProfile": t.string().optional(),
            "participantRole": t.string(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "conversationProfile": t.string().optional(),
            "participantRole": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowCxV3FlowIn"] = t.struct(
        {
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
            ).optional(),
            "displayName": t.string(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsIn"]
            ).optional(),
            "description": t.string().optional(),
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowIn"])
    types["GoogleCloudDialogflowCxV3FlowOut"] = t.struct(
        {
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
            ).optional(),
            "displayName": t.string(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsOut"]
            ).optional(),
            "description": t.string().optional(),
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowOut"])
    types["GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataIn"])
    types[
        "GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataOut"
    ] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2IntentMessageCarouselSelectIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn"]
                )
            )
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectIn"])
    types["GoogleCloudDialogflowV2IntentMessageCarouselSelectOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectOut"])
    types["GoogleCloudDialogflowCxV3ContinuousTestResultIn"] = t.struct(
        {
            "name": t.string().optional(),
            "result": t.string().optional(),
            "runTime": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ContinuousTestResultIn"])
    types["GoogleCloudDialogflowCxV3ContinuousTestResultOut"] = t.struct(
        {
            "name": t.string().optional(),
            "result": t.string().optional(),
            "runTime": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ContinuousTestResultOut"])
    types["GoogleCloudDialogflowCxV3RestoreAgentRequestIn"] = t.struct(
        {
            "agentContent": t.string().optional(),
            "restoreOption": t.string().optional(),
            "agentUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RestoreAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3RestoreAgentRequestOut"] = t.struct(
        {
            "agentContent": t.string().optional(),
            "restoreOption": t.string().optional(),
            "agentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RestoreAgentRequestOut"])
    types["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn"] = t.struct(
        {"names": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"] = t.struct(
        {
            "page": t.proxy(renames["GoogleCloudDialogflowCxV3PageIn"]).optional(),
            "flow": t.proxy(renames["GoogleCloudDialogflowCxV3FlowIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"] = t.struct(
        {
            "page": t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]).optional(),
            "flow": t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"])
    types["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"] = t.struct(
        {"trainingModelType": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"])
    types["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"] = t.struct(
        {
            "trainingModelType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataIn"])
    types[
        "GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataOut"
    ] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowCxV3ExportAgentResponseIn"] = t.struct(
        {"agentUri": t.string().optional(), "agentContent": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentResponseIn"])
    types["GoogleCloudDialogflowCxV3ExportAgentResponseOut"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "agentContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1ConversationSignalsIn"] = t.struct(
        {"turnSignals": t.proxy(renames["GoogleCloudDialogflowCxV3beta1TurnSignalsIn"])}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationSignalsIn"])
    types["GoogleCloudDialogflowCxV3beta1ConversationSignalsOut"] = t.struct(
        {
            "turnSignals": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TurnSignalsOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationSignalsOut"])
    types["GoogleCloudDialogflowV2IntentIn"] = t.struct(
        {
            "parentFollowupIntentName": t.string().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "events": t.array(t.string()).optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhraseIn"])
            ).optional(),
            "displayName": t.string(),
            "resetContexts": t.boolean().optional(),
            "endInteraction": t.boolean().optional(),
            "isFallback": t.boolean().optional(),
            "webhookState": t.string().optional(),
            "name": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "action": t.string().optional(),
            "mlDisabled": t.boolean().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentParameterIn"])
            ).optional(),
            "priority": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentIn"])
    types["GoogleCloudDialogflowV2IntentOut"] = t.struct(
        {
            "parentFollowupIntentName": t.string().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "rootFollowupIntentName": t.string().optional(),
            "events": t.array(t.string()).optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhraseOut"])
            ).optional(),
            "displayName": t.string(),
            "resetContexts": t.boolean().optional(),
            "endInteraction": t.boolean().optional(),
            "isFallback": t.boolean().optional(),
            "webhookState": t.string().optional(),
            "name": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "followupIntentInfo": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentFollowupIntentInfoOut"])
            ).optional(),
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "action": t.string().optional(),
            "mlDisabled": t.boolean().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentParameterOut"])
            ).optional(),
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentOut"])
    types["GoogleCloudDialogflowCxV3RolloutConfigIn"] = t.struct(
        {
            "rolloutCondition": t.string().optional(),
            "rolloutSteps": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn"])
            ).optional(),
            "failureCondition": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigIn"])
    types["GoogleCloudDialogflowCxV3RolloutConfigOut"] = t.struct(
        {
            "rolloutCondition": t.string().optional(),
            "rolloutSteps": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut"])
            ).optional(),
            "failureCondition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigOut"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentIn"] = t.struct(
        {
            "returnPartialResponses": t.boolean().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
            ).optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn"
                    ]
                )
            ).optional(),
            "tag": t.string().optional(),
            "webhook": t.string().optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentOut"] = t.struct(
        {
            "returnPartialResponses": t.boolean().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
            ).optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut"
                    ]
                )
            ).optional(),
            "tag": t.string().optional(),
            "webhook": t.string().optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"
                    ]
                )
            ).optional(),
            "title": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "formattedText": t.string(),
            "subtitle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"
                    ]
                )
            ).optional(),
            "title": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "formattedText": t.string(),
            "subtitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"])
    types["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "trafficPercent": t.integer().optional(),
            "minDuration": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn"])
    types["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "trafficPercent": t.integer().optional(),
            "minDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut"])
    types["GoogleCloudDialogflowCxV3ExperimentResultMetricIn"] = t.struct(
        {
            "type": t.string().optional(),
            "ratio": t.number().optional(),
            "count": t.number().optional(),
            "confidenceInterval": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"]
            ).optional(),
            "countType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultMetricOut"] = t.struct(
        {
            "type": t.string().optional(),
            "ratio": t.number().optional(),
            "count": t.number().optional(),
            "confidenceInterval": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut"
                ]
            ).optional(),
            "countType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricOut"])
    types["GoogleCloudDialogflowCxV3ExperimentResultIn"] = t.struct(
        {
            "versionMetrics": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn"]
                )
            ).optional(),
            "lastUpdateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultOut"] = t.struct(
        {
            "versionMetrics": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut"
                    ]
                )
            ).optional(),
            "lastUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultOut"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "currentPage": t.string().optional(),
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "currentPage": t.string().optional(),
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoOut"])
    types["GoogleCloudDialogflowV2IntentMessageSimpleResponseIn"] = t.struct(
        {
            "ssml": t.string().optional(),
            "textToSpeech": t.string().optional(),
            "displayText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponseIn"])
    types["GoogleCloudDialogflowV2IntentMessageSimpleResponseOut"] = t.struct(
        {
            "ssml": t.string().optional(),
            "textToSpeech": t.string().optional(),
            "displayText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponseOut"])
    types["GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowCxV3ListAgentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "agents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3AgentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListAgentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListAgentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "agents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseIn"] = t.struct(
        {
            "continuousTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseOut"] = t.struct(
        {
            "continuousTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1DeployFlowMetadataIn"] = t.struct(
        {
            "testErrors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestErrorIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DeployFlowMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1DeployFlowMetadataOut"] = t.struct(
        {
            "testErrors": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DeployFlowMetadataOut"])
    types["GoogleCloudDialogflowCxV3GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3GcsDestinationIn"])
    types["GoogleCloudDialogflowCxV3GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GcsDestinationOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageIn"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "channel": t.string().optional(),
            "liveAgentHandoff": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"]
            ).optional(),
            "conversationSuccess": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn"
                ]
            ).optional(),
            "outputAudioText": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageTextIn"]
            ).optional(),
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageOut"] = t.struct(
        {
            "endInteraction": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "channel": t.string().optional(),
            "liveAgentHandoff": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"]
            ).optional(),
            "conversationSuccess": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"
                ]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut"
                ]
            ).optional(),
            "mixedAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut"]
            ).optional(),
            "outputAudioText": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageTextOut"]
            ).optional(),
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut"])
    types["GoogleCloudDialogflowV2IntentMessageCardIn"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageCardButtonIn"])
            ).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageCardOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageCardButtonOut"])
            ).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardOut"])
    types["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"])
            ),
            "name": t.string(),
            "entityOverrideMode": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"])
    types["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"])
            ),
            "name": t.string(),
            "entityOverrideMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"])
    types["GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseIn"] = t.struct(
        {
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseIn"])
    types["GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseOut"] = t.struct(
        {
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn"
    ] = t.struct({"phoneNumber": t.string().optional()}).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut"
    ] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut"]
    )
    types["GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn"] = t.struct(
        {"flowContent": t.string().optional(), "flowUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut"] = t.struct(
        {
            "flowContent": t.string().optional(),
            "flowUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudDialogflowV2beta1WebhookResponseIn"] = t.struct(
        {
            "liveAgentHandoff": t.boolean().optional(),
            "source": t.string().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2beta1EventInputIn"]
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "endInteraction": t.boolean().optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookResponseIn"])
    types["GoogleCloudDialogflowV2beta1WebhookResponseOut"] = t.struct(
        {
            "liveAgentHandoff": t.boolean().optional(),
            "source": t.string().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2beta1EventInputOut"]
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "endInteraction": t.boolean().optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookResponseOut"])
    types["GoogleCloudDialogflowV2EntityTypeEntityIn"] = t.struct(
        {"synonyms": t.array(t.string()), "value": t.string()}
    ).named(renames["GoogleCloudDialogflowV2EntityTypeEntityIn"])
    types["GoogleCloudDialogflowV2EntityTypeEntityOut"] = t.struct(
        {
            "synonyms": t.array(t.string()),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EntityTypeEntityOut"])
    types["GoogleCloudDialogflowCxV3RolloutStateIn"] = t.struct(
        {
            "step": t.string().optional(),
            "stepIndex": t.integer().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutStateIn"])
    types["GoogleCloudDialogflowCxV3RolloutStateOut"] = t.struct(
        {
            "step": t.string().optional(),
            "stepIndex": t.integer().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutStateOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn"] = t.struct(
        {
            "dial": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn"
                ]
            ).optional(),
            "shareLocation": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn"
                ]
            ).optional(),
            "postbackData": t.string().optional(),
            "text": t.string().optional(),
            "openUrl": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut"] = t.struct(
        {
            "dial": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut"
                ]
            ).optional(),
            "shareLocation": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut"
                ]
            ).optional(),
            "postbackData": t.string().optional(),
            "text": t.string().optional(),
            "openUrl": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
    ] = t.struct({"urlTypeHint": t.string().optional(), "url": t.string()}).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
    ] = t.struct(
        {
            "urlTypeHint": t.string().optional(),
            "url": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn"] = t.struct(
        {"uri": t.string().optional(), "audio": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "audio": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut"])
    types[
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2SessionEntityTypeIn"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityIn"])
            ),
            "name": t.string(),
            "entityOverrideMode": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2SessionEntityTypeIn"])
    types["GoogleCloudDialogflowV2SessionEntityTypeOut"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityOut"])
            ),
            "name": t.string(),
            "entityOverrideMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SessionEntityTypeOut"])
    types["GoogleCloudDialogflowCxV3PageInfoIn"] = t.struct(
        {
            "currentPage": t.string().optional(),
            "displayName": t.string().optional(),
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoFormInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoIn"])
    types["GoogleCloudDialogflowCxV3PageInfoOut"] = t.struct(
        {
            "currentPage": t.string().optional(),
            "displayName": t.string().optional(),
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoFormInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoOut"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "parameter": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "parameter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut"])
    types["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"] = t.struct(
        {
            "userDefined": t.boolean().optional(),
            "text": t.string(),
            "entityType": t.string().optional(),
            "alias": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"] = t.struct(
        {
            "userDefined": t.boolean().optional(),
            "text": t.string(),
            "entityType": t.string().optional(),
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"])
    types["GoogleCloudDialogflowV2KnowledgeOperationMetadataIn"] = t.struct(
        {
            "knowledgeBase": t.string().optional(),
            "exportOperationMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ExportOperationMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2KnowledgeOperationMetadataIn"])
    types["GoogleCloudDialogflowV2KnowledgeOperationMetadataOut"] = t.struct(
        {
            "knowledgeBase": t.string().optional(),
            "exportOperationMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ExportOperationMetadataOut"]
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2KnowledgeOperationMetadataOut"])
    types["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn"] = t.struct(
        {
            "parentFollowupIntentName": t.string().optional(),
            "followupIntentName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn"])
    types["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut"] = t.struct(
        {
            "parentFollowupIntentName": t.string().optional(),
            "followupIntentName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut"])
    types["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut"])
    types["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "required": t.boolean().optional(),
            "justCollected": t.boolean().optional(),
            "state": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn"])
    types["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "required": t.boolean().optional(),
            "justCollected": t.boolean().optional(),
            "state": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"] = t.struct(
        {
            "audioExportPattern": t.string().optional(),
            "enableAudioRedaction": t.boolean().optional(),
            "audioFormat": t.string().optional(),
            "gcsBucket": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"] = t.struct(
        {
            "audioExportPattern": t.string().optional(),
            "enableAudioRedaction": t.boolean().optional(),
            "audioFormat": t.string().optional(),
            "gcsBucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"])
    types["GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn"] = t.struct(
        {
            "entityType": t.string().optional(),
            "text": t.string(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn"])
    types["GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut"] = t.struct(
        {
            "entityType": t.string().optional(),
            "text": t.string(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn"
    ] = t.struct({"phoneNumber": t.string()}).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut"
    ] = t.struct(
        {
            "phoneNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3TestRunDifferenceIn"] = t.struct(
        {"description": t.string().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TestRunDifferenceIn"])
    types["GoogleCloudDialogflowCxV3TestRunDifferenceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestRunDifferenceOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn"] = t.struct(
        {
            "rbmSuggestion": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn"]
                )
            ).optional(),
            "text": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut"] = t.struct(
        {
            "rbmSuggestion": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut"]
                )
            ).optional(),
            "text": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut"])
    types["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "parameter": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn"])
    types["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "parameter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut"])
    types["GoogleCloudDialogflowCxV3ResourceNameIn"] = t.struct(
        {"name": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResourceNameIn"])
    types["GoogleCloudDialogflowCxV3ResourceNameOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResourceNameOut"])
    types["GoogleCloudDialogflowCxV3ChangelogIn"] = t.struct(
        {
            "name": t.string().optional(),
            "action": t.string().optional(),
            "createTime": t.string().optional(),
            "userEmail": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "resource": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ChangelogIn"])
    types["GoogleCloudDialogflowCxV3ChangelogOut"] = t.struct(
        {
            "name": t.string().optional(),
            "action": t.string().optional(),
            "createTime": t.string().optional(),
            "userEmail": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ChangelogOut"])
    types["GoogleCloudDialogflowCxV3DeployFlowResponseIn"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentIn"]
            ).optional(),
            "deployment": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3DeployFlowResponseOut"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentOut"]
            ).optional(),
            "deployment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"] = t.struct(
        {
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "webhookType": t.string().optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "uri": t.string(),
            "password": t.string().optional(),
            "requestBody": t.string().optional(),
            "httpMethod": t.string().optional(),
            "username": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"] = t.struct(
        {
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "webhookType": t.string().optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "uri": t.string(),
            "password": t.string().optional(),
            "requestBody": t.string().optional(),
            "httpMethod": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"])
    types["GoogleCloudDialogflowCxV3beta1IntentParameterIn"] = t.struct(
        {
            "entityType": t.string(),
            "redact": t.boolean().optional(),
            "isList": t.boolean().optional(),
            "id": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentParameterIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentParameterOut"] = t.struct(
        {
            "entityType": t.string(),
            "redact": t.boolean().optional(),
            "isList": t.boolean().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentParameterOut"])
    types["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"] = t.struct(
        {
            "reply": t.string().optional(),
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"])
    types["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"] = t.struct(
        {
            "reply": t.string().optional(),
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"])
    types["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"] = t.struct(
        {
            "upperBound": t.number().optional(),
            "lowerBound": t.number().optional(),
            "ratio": t.number().optional(),
            "confidenceLevel": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut"] = t.struct(
        {
            "upperBound": t.number().optional(),
            "lowerBound": t.number().optional(),
            "ratio": t.number().optional(),
            "confidenceLevel": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut"])
    types["GoogleCloudDialogflowV2WebhookResponseIn"] = t.struct(
        {
            "source": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SessionEntityTypeIn"])
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2EventInputIn"]
            ).optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookResponseIn"])
    types["GoogleCloudDialogflowV2WebhookResponseOut"] = t.struct(
        {
            "source": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SessionEntityTypeOut"])
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2EventInputOut"]
            ).optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookResponseOut"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesResponseIn"] = t.struct(
        {"content": t.string().optional(), "gcsUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesResponseOut"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesResponseOut"])
    types["GoogleCloudDialogflowCxV3TurnSignalsIn"] = t.struct(
        {
            "webhookStatuses": t.array(t.string()).optional(),
            "noMatch": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "noUserInput": t.boolean().optional(),
            "dtmfUsed": t.boolean().optional(),
            "reachedEndPage": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "agentEscalated": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TurnSignalsIn"])
    types["GoogleCloudDialogflowCxV3TurnSignalsOut"] = t.struct(
        {
            "webhookStatuses": t.array(t.string()).optional(),
            "noMatch": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "noUserInput": t.boolean().optional(),
            "dtmfUsed": t.boolean().optional(),
            "reachedEndPage": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "agentEscalated": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TurnSignalsOut"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut"])
    types["GoogleCloudDialogflowCxV3FormParameterIn"] = t.struct(
        {
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn"]
            ),
            "displayName": t.string(),
            "redact": t.boolean().optional(),
            "entityType": t.string(),
            "required": t.boolean().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "isList": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterIn"])
    types["GoogleCloudDialogflowCxV3FormParameterOut"] = t.struct(
        {
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut"]
            ),
            "displayName": t.string(),
            "redact": t.boolean().optional(),
            "entityType": t.string(),
            "required": t.boolean().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "isList": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterOut"])
    types["GoogleCloudDialogflowV2beta1IntentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "endInteraction": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "mlDisabled": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentParameterIn"])
            ).optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"])
            ).optional(),
            "webhookState": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "isFallback": t.boolean().optional(),
            "mlEnabled": t.boolean().optional(),
            "priority": t.integer().optional(),
            "parentFollowupIntentName": t.string().optional(),
            "displayName": t.string(),
            "action": t.string().optional(),
            "resetContexts": t.boolean().optional(),
            "inputContextNames": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentIn"])
    types["GoogleCloudDialogflowV2beta1IntentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "endInteraction": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "mlDisabled": t.boolean().optional(),
            "followupIntentInfo": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut"]
                )
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentParameterOut"])
            ).optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"])
            ).optional(),
            "rootFollowupIntentName": t.string().optional(),
            "webhookState": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "isFallback": t.boolean().optional(),
            "mlEnabled": t.boolean().optional(),
            "priority": t.integer().optional(),
            "parentFollowupIntentName": t.string().optional(),
            "displayName": t.string(),
            "action": t.string().optional(),
            "resetContexts": t.boolean().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentOut"])
    types["GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut"])
    types["GoogleCloudDialogflowV2beta1QueryResultIn"] = t.struct(
        {
            "cancelsSlotFilling": t.boolean().optional(),
            "action": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "queryText": t.string().optional(),
            "intentDetectionConfidence": t.number().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "knowledgeAnswers": t.proxy(
                renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersIn"]
            ).optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn"]
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentIn"]
            ).optional(),
            "languageCode": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "webhookSource": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1QueryResultIn"])
    types["GoogleCloudDialogflowV2beta1QueryResultOut"] = t.struct(
        {
            "cancelsSlotFilling": t.boolean().optional(),
            "action": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "queryText": t.string().optional(),
            "intentDetectionConfidence": t.number().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "knowledgeAnswers": t.proxy(
                renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersOut"]
            ).optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut"]
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "webhookSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1QueryResultOut"])
    types[
        "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn"
    ] = t.struct({"enableInsightsExport": t.boolean().optional()}).named(
        renames["GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut"
    ] = t.struct(
        {
            "enableInsightsExport": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut"]
    )
    types["GoogleCloudDialogflowCxV3FormIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FormParameterIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormIn"])
    types["GoogleCloudDialogflowCxV3FormOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FormParameterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormOut"])
    types["GoogleCloudDialogflowCxV3FlowValidationResultIn"] = t.struct(
        {
            "name": t.string().optional(),
            "validationMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ValidationMessageIn"])
            ).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowValidationResultIn"])
    types["GoogleCloudDialogflowCxV3FlowValidationResultOut"] = t.struct(
        {
            "name": t.string().optional(),
            "validationMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ValidationMessageOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowValidationResultOut"])
    types["GoogleCloudDialogflowCxV3beta1TestConfigIn"] = t.struct(
        {
            "flow": t.string().optional(),
            "trackingParameters": t.array(t.string()).optional(),
            "page": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1TestConfigOut"] = t.struct(
        {
            "flow": t.string().optional(),
            "trackingParameters": t.array(t.string()).optional(),
            "page": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestConfigOut"])
    types["GoogleCloudLocationListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseIn"])
    types["GoogleCloudLocationListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1TestErrorIn"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "testTime": t.string().optional(),
            "testCase": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestErrorIn"])
    types["GoogleCloudDialogflowCxV3beta1TestErrorOut"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "testTime": t.string().optional(),
            "testCase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestErrorOut"])
    types["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"] = t.struct(
        {
            "password": t.string().optional(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "username": t.string().optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "httpMethod": t.string().optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "webhookType": t.string().optional(),
            "requestBody": t.string().optional(),
            "uri": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"])
    types["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"] = t.struct(
        {
            "password": t.string().optional(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "username": t.string().optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "httpMethod": t.string().optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "webhookType": t.string().optional(),
            "requestBody": t.string().optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"])
    types["GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn"] = t.struct(
        {"type": t.string().optional(), "description": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn"])
    types["GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentIn"] = t.struct(
        {
            "displayName": t.string(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"]
            ).optional(),
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn"]
            ).optional(),
            "versionConfigs": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentOut"] = t.struct(
        {
            "displayName": t.string(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"]
            ).optional(),
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut"]
            ).optional(),
            "versionConfigs": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentOut"])
    types["GoogleCloudDialogflowCxV3DeploymentResultIn"] = t.struct(
        {
            "experiment": t.string().optional(),
            "deploymentTestResults": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentResultIn"])
    types["GoogleCloudDialogflowCxV3DeploymentResultOut"] = t.struct(
        {
            "experiment": t.string().optional(),
            "deploymentTestResults": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentResultOut"])
    types["GoogleTypeLatLngIn"] = t.struct(
        {"longitude": t.number().optional(), "latitude": t.number().optional()}
    ).named(renames["GoogleTypeLatLngIn"])
    types["GoogleTypeLatLngOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeLatLngOut"])
    types["GoogleCloudDialogflowCxV3LoadVersionRequestIn"] = t.struct(
        {"allowOverrideAgentResources": t.boolean().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3LoadVersionRequestIn"])
    types["GoogleCloudDialogflowCxV3LoadVersionRequestOut"] = t.struct(
        {
            "allowOverrideAgentResources": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3LoadVersionRequestOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn"] = t.struct(
        {"uri": t.string(), "destinationName": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut"] = t.struct(
        {
            "uri": t.string(),
            "destinationName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn"] = t.struct(
        {"content": t.string().optional(), "gcsUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut"])
    types["GoogleCloudDialogflowV2beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1GcsDestinationIn"])
    types["GoogleCloudDialogflowV2beta1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1GcsDestinationOut"])
    types["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn"] = t.struct(
        {"parameterId": t.string().optional(), "text": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut"] = t.struct(
        {
            "parameterId": t.string().optional(),
            "text": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut"])
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut"
    ] = t.struct(
        {"state": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2InputDatasetIn"] = t.struct(
        {"dataset": t.string()}
    ).named(renames["GoogleCloudDialogflowV2InputDatasetIn"])
    types["GoogleCloudDialogflowV2InputDatasetOut"] = t.struct(
        {"dataset": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2InputDatasetOut"])
    types["GoogleCloudDialogflowCxV3beta1EventInputIn"] = t.struct(
        {"event": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventInputIn"])
    types["GoogleCloudDialogflowCxV3beta1EventInputOut"] = t.struct(
        {
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventInputOut"])
    types["GoogleCloudDialogflowCxV3FulfillmentIn"] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn"]
                )
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn"]
                )
            ).optional(),
            "tag": t.string().optional(),
            "webhook": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentIn"])
    types["GoogleCloudDialogflowCxV3FulfillmentOut"] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut"]
                )
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut"]
                )
            ).optional(),
            "tag": t.string().optional(),
            "webhook": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentOut"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseIn"] = t.struct(
        {
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestConfigIn"]
            ).optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"]
            ).optional(),
            "notes": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnIn"])
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseIn"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseOut"] = t.struct(
        {
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestConfigOut"]
            ).optional(),
            "creationTime": t.string().optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"]
            ).optional(),
            "notes": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnOut"])
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseOut"])
    types["GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataIn"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataOut"] = t.struct(
        {
            "genericMetadata": t.proxy(
                renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3RunTestCaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseMetadataIn"])
    types["GoogleCloudDialogflowCxV3RunTestCaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseMetadataOut"])
    types["GoogleCloudDialogflowCxV3InputAudioConfigIn"] = t.struct(
        {
            "phraseHints": t.array(t.string()).optional(),
            "audioEncoding": t.string(),
            "modelVariant": t.string().optional(),
            "enableWordInfo": t.boolean().optional(),
            "sampleRateHertz": t.integer().optional(),
            "model": t.string().optional(),
            "singleUtterance": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3InputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3InputAudioConfigOut"] = t.struct(
        {
            "phraseHints": t.array(t.string()).optional(),
            "audioEncoding": t.string(),
            "modelVariant": t.string().optional(),
            "enableWordInfo": t.boolean().optional(),
            "sampleRateHertz": t.integer().optional(),
            "model": t.string().optional(),
            "singleUtterance": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3InputAudioConfigOut"])
    types["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"] = t.struct(
        {
            "latestMessage": t.string().optional(),
            "smartReplyAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"])
            ).optional(),
            "contextSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"] = t.struct(
        {
            "latestMessage": t.string().optional(),
            "smartReplyAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1FormIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1FormParameterIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormIn"])
    types["GoogleCloudDialogflowCxV3beta1FormOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1FormParameterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormOut"])
    types[
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn"
    ] = t.struct({"uri": t.string()}).named(
        renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn"]
    )
    types[
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut"
    ] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(
        renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut"]
    )
    types[
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn"
    ] = t.struct(
        {
            "originalValue": t.string().optional(),
            "resolvedValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn"
        ]
    )
    types[
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut"
    ] = t.struct(
        {
            "originalValue": t.string().optional(),
            "resolvedValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut"
        ]
    )
    types["GoogleCloudDialogflowV2MessageIn"] = t.struct(
        {
            "content": t.string(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "sendTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageIn"])
    types["GoogleCloudDialogflowV2MessageOut"] = t.struct(
        {
            "participantRole": t.string().optional(),
            "sentimentAnalysis": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultOut"]
            ).optional(),
            "content": t.string(),
            "participant": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "messageAnnotation": t.proxy(
                renames["GoogleCloudDialogflowV2MessageAnnotationOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "sendTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageOut"])
    types["GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut"])
    types["GoogleCloudDialogflowCxV3EventInputIn"] = t.struct(
        {"event": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EventInputIn"])
    types["GoogleCloudDialogflowCxV3EventInputOut"] = t.struct(
        {
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventInputOut"])
    types["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectIn"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"])
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectIn"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectOut"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectOut"])
    types["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"] = t.struct(
        {"version": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"] = t.struct(
        {"version": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"])
    types["GoogleCloudDialogflowV2IntentMessageCardButtonIn"] = t.struct(
        {"text": t.string().optional(), "postback": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardButtonIn"])
    types["GoogleCloudDialogflowV2IntentMessageCardButtonOut"] = t.struct(
        {
            "text": t.string().optional(),
            "postback": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardButtonOut"])
    types["GoogleCloudDialogflowV2SentimentIn"] = t.struct(
        {"magnitude": t.number().optional(), "score": t.number().optional()}
    ).named(renames["GoogleCloudDialogflowV2SentimentIn"])
    types["GoogleCloudDialogflowV2SentimentOut"] = t.struct(
        {
            "magnitude": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SentimentOut"])
    types["GoogleCloudDialogflowV2EntityTypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "autoExpansionMode": t.string().optional(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "kind": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EntityTypeIn"])
    types["GoogleCloudDialogflowV2EntityTypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "autoExpansionMode": t.string().optional(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "kind": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EntityTypeOut"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn"] = t.struct(
        {"audioUri": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut"] = t.struct(
        {
            "allowPlaybackInterruption": t.boolean().optional(),
            "audioUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut"])
    types["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn"] = t.struct(
        {
            "repromptEventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerIn"])
            ).optional(),
            "initialPromptFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn"])
    types["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut"] = t.struct(
        {
            "repromptEventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerOut"])
            ).optional(),
            "initialPromptFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardIn"] = t.struct(
        {
            "rows": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowIn"])
            ).optional(),
            "title": t.string(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"]
                )
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "columnProperties": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn"]
                )
            ).optional(),
            "subtitle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardOut"] = t.struct(
        {
            "rows": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowOut"])
            ).optional(),
            "title": t.string(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"]
                )
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "columnProperties": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut"]
                )
            ).optional(),
            "subtitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardOut"])
    types["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn"] = t.struct(
        {
            "repeatCount": t.integer().optional(),
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn"]
                )
            ),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut"] = t.struct(
        {
            "repeatCount": t.integer().optional(),
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut"]
                )
            ),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut"])
    types[
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "participantRole": t.string(),
            "createTime": t.string().optional(),
            "conversationProfile": t.string().optional(),
            "suggestionFeatureType": t.string(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut"
    ] = t.struct(
        {
            "participantRole": t.string(),
            "createTime": t.string().optional(),
            "conversationProfile": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3IntentIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string(),
            "isFallback": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
            ).optional(),
            "priority": t.integer().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentIn"])
    types["GoogleCloudDialogflowCxV3IntentOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string(),
            "isFallback": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterOut"])
            ).optional(),
            "priority": t.integer().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseOut"])
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"] = t.struct(
        {"audioUri": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"] = t.struct(
        {"audioUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"])
    types["GoogleCloudDialogflowCxV3IntentParameterIn"] = t.struct(
        {
            "isList": t.boolean().optional(),
            "entityType": t.string(),
            "id": t.string(),
            "redact": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
    types["GoogleCloudDialogflowCxV3IntentParameterOut"] = t.struct(
        {
            "isList": t.boolean().optional(),
            "entityType": t.string(),
            "id": t.string(),
            "redact": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentParameterOut"])
    types["GoogleCloudDialogflowCxV3EventHandlerIn"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "event": t.string(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
            "targetPage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
    types["GoogleCloudDialogflowCxV3EventHandlerOut"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "event": t.string(),
            "name": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "targetPage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
    types["GoogleCloudDialogflowCxV3ListExperimentsResponseIn"] = t.struct(
        {
            "experiments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListExperimentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListExperimentsResponseOut"] = t.struct(
        {
            "experiments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListExperimentsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn"] = t.struct(
        {
            "caseContent": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn"
                    ]
                )
            ).optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn"])
    types[
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut"
    ] = t.struct(
        {
            "caseContent": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut"
                    ]
                )
            ).optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut"]
    )
    types["GoogleCloudDialogflowCxV3RunContinuousTestResponseIn"] = t.struct(
        {
            "continuousTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3ContinuousTestResultIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestResponseIn"])
    types["GoogleCloudDialogflowCxV3RunContinuousTestResponseOut"] = t.struct(
        {
            "continuousTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3ContinuousTestResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestResponseOut"])
    types["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"] = t.struct(
        {"enableSpeechAdaptation": t.boolean().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"])
    types["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"] = t.struct(
        {
            "enableSpeechAdaptation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"])
    types["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn"] = t.struct(
        {
            "webhookOverrides": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3WebhookIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut"] = t.struct(
        {
            "webhookOverrides": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut"])
    types["GoogleCloudDialogflowV2beta1ContextIn"] = t.struct(
        {
            "lifespanCount": t.integer().optional(),
            "name": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ContextIn"])
    types["GoogleCloudDialogflowV2beta1ContextOut"] = t.struct(
        {
            "lifespanCount": t.integer().optional(),
            "name": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ContextOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn"]
                )
            ),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut"
                    ]
                )
            ),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectOut"])
    types["GoogleCloudDialogflowCxV3AdvancedSettingsIn"] = t.struct(
        {
            "loggingSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn"]
            ).optional(),
            "audioExportGcsDestination": t.proxy(
                renames["GoogleCloudDialogflowCxV3GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AdvancedSettingsIn"])
    types["GoogleCloudDialogflowCxV3AdvancedSettingsOut"] = t.struct(
        {
            "loggingSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut"]
            ).optional(),
            "audioExportGcsDestination": t.proxy(
                renames["GoogleCloudDialogflowCxV3GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AdvancedSettingsOut"])
    types["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"] = t.struct(
        {"trainingModelType": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"])
    types["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"] = t.struct(
        {
            "trainingModelType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"])
    types["GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseIn"] = t.struct(
        {
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseIn"])
    types["GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseOut"] = t.struct(
        {
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseOut"])
    types["GoogleCloudDialogflowCxV3CompareVersionsRequestIn"] = t.struct(
        {"targetVersion": t.string(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsRequestIn"])
    types["GoogleCloudDialogflowCxV3CompareVersionsRequestOut"] = t.struct(
        {
            "targetVersion": t.string(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsRequestOut"])
    types["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn"] = t.struct(
        {
            "source": t.string().optional(),
            "version": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn"])
    types["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut"] = t.struct(
        {
            "source": t.string().optional(),
            "version": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardCellIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellIn"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardCellOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellOut"])
    types["GoogleCloudDialogflowCxV3ExperimentIn"] = t.struct(
        {
            "rolloutFailureReason": t.string().optional(),
            "rolloutState": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
            ).optional(),
            "variantsHistory": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
            ).optional(),
            "lastUpdateTime": t.string().optional(),
            "startTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "definition": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
            ).optional(),
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "displayName": t.string(),
            "experimentLength": t.string().optional(),
            "rolloutConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
            ).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentIn"])
    types["GoogleCloudDialogflowCxV3ExperimentOut"] = t.struct(
        {
            "rolloutFailureReason": t.string().optional(),
            "rolloutState": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutStateOut"]
            ).optional(),
            "variantsHistory": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryOut"])
            ).optional(),
            "lastUpdateTime": t.string().optional(),
            "startTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "definition": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentDefinitionOut"]
            ).optional(),
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "displayName": t.string(),
            "experimentLength": t.string().optional(),
            "rolloutConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutConfigOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentOut"])
    types["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowCxV3ListTestCasesResponseIn"] = t.struct(
        {
            "testCases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3ListTestCasesResponseOut"] = t.struct(
        {
            "testCases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTestCasesResponseOut"])
    types["GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn"] = t.struct(
        {
            "simpleResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponseIn"])
            )
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn"])
    types["GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut"] = t.struct(
        {
            "simpleResponses": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageSimpleResponseOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut"])
    types["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn"] = t.struct(
        {
            "sessionCount": t.integer().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut"] = t.struct(
        {
            "sessionCount": t.integer().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut"])
    types["GoogleCloudDialogflowV2IntentMessageSuggestionIn"] = t.struct(
        {"title": t.string()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSuggestionIn"])
    types["GoogleCloudDialogflowV2IntentMessageSuggestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSuggestionOut"])
    types["GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn"] = t.struct(
        {"latestMessage": t.string().optional(), "contextSize": t.integer().optional()}
    ).named(renames["GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn"])
    types["GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut"] = t.struct(
        {
            "smartReplyAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SmartReplyAnswerOut"])
            ).optional(),
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut"])
    types["GoogleCloudDialogflowCxV3ExportFlowResponseIn"] = t.struct(
        {"flowUri": t.string().optional(), "flowContent": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3ExportFlowResponseOut"] = t.struct(
        {
            "flowUri": t.string().optional(),
            "flowContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportFlowResponseOut"])
    types["GoogleCloudDialogflowV2IntentMessageQuickRepliesIn"] = t.struct(
        {"quickReplies": t.array(t.string()).optional(), "title": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageQuickRepliesIn"])
    types["GoogleCloudDialogflowV2IntentMessageQuickRepliesOut"] = t.struct(
        {
            "quickReplies": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageQuickRepliesOut"])
    types["GoogleCloudDialogflowCxV3EnvironmentIn"] = t.struct(
        {
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn"]
            ).optional(),
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn"]
            ).optional(),
            "versionConfigs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"])
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentOut"] = t.struct(
        {
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut"]
            ).optional(),
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut"]
            ).optional(),
            "versionConfigs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"])
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentOut"])
    types["GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn"] = t.struct(
        {"environment": t.string().optional(), "testCases": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "testCases": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut"])
    types["GoogleCloudDialogflowCxV3TrainFlowRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TrainFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3TrainFlowRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TrainFlowRequestOut"])
    types["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"] = t.struct(
        {"synonyms": t.array(t.string()), "value": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"])
    types["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"] = t.struct(
        {
            "synonyms": t.array(t.string()),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"])
    types["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseIn"] = t.struct(
        {
            "securitySettings": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SecuritySettingsIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut"] = t.struct(
        {
            "securitySettings": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "title": t.string(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn"]
            ),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "title": t.string(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut"]
            ),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn"] = t.struct(
        {
            "parameterInfo": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut"] = t.struct(
        {
            "parameterInfo": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut"])
    types["GoogleCloudDialogflowV2beta1MessageAnnotationIn"] = t.struct(
        {
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn"])
            ).optional(),
            "containEntities": t.boolean(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1MessageAnnotationIn"])
    types["GoogleCloudDialogflowV2beta1MessageAnnotationOut"] = t.struct(
        {
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut"])
            ).optional(),
            "containEntities": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1MessageAnnotationOut"])
    types["GoogleCloudDialogflowCxV3RunContinuousTestRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestRequestIn"])
    types["GoogleCloudDialogflowCxV3RunContinuousTestRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestRequestOut"])
    types["GoogleCloudDialogflowCxV3ValidationMessageIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "resourceNames": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResourceNameIn"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "detail": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidationMessageIn"])
    types["GoogleCloudDialogflowCxV3ValidationMessageOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "resourceNames": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResourceNameOut"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "detail": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidationMessageOut"])
    types["GoogleCloudDialogflowCxV3EntityTypeEntityIn"] = t.struct(
        {"value": t.string(), "synonyms": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
    types["GoogleCloudDialogflowCxV3EntityTypeEntityOut"] = t.struct(
        {
            "value": t.string(),
            "synonyms": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeEntityOut"])
    types["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "testCaseResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "testCaseResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn"] = t.struct(
        {
            "cardContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"]
            ),
            "cardOrientation": t.string(),
            "thumbnailImageAlignment": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut"] = t.struct(
        {
            "cardContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"]
            ),
            "cardOrientation": t.string(),
            "thumbnailImageAlignment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut"])
    types["GoogleCloudDialogflowCxV3ValidateFlowRequestIn"] = t.struct(
        {"languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ValidateFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3ValidateFlowRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidateFlowRequestOut"])
    types["GoogleCloudDialogflowV2AnnotatedMessagePartIn"] = t.struct(
        {
            "entityType": t.string().optional(),
            "text": t.string().optional(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2AnnotatedMessagePartIn"])
    types["GoogleCloudDialogflowV2AnnotatedMessagePartOut"] = t.struct(
        {
            "entityType": t.string().optional(),
            "text": t.string().optional(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2AnnotatedMessagePartOut"])
    types["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
            "condition": t.string().optional(),
            "intent": t.string().optional(),
            "targetPage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"])
    types["GoogleCloudDialogflowCxV3beta1TransitionRouteOut"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "name": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "condition": t.string().optional(),
            "intent": t.string().optional(),
            "targetPage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteOut"])
    types["GoogleCloudDialogflowCxV3QueryResultIn"] = t.struct(
        {
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentIn"]).optional(),
            "webhookStatuses": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
            "responseMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "triggerIntent": t.string().optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"]).optional(),
            "languageCode": t.string().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultIn"]
            ).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerEvent": t.string().optional(),
            "webhookPayloads": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "transcript": t.string().optional(),
            "text": t.string().optional(),
            "dtmf": t.proxy(renames["GoogleCloudDialogflowCxV3DtmfInputIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryResultIn"])
    types["GoogleCloudDialogflowCxV3QueryResultOut"] = t.struct(
        {
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]).optional(),
            "webhookStatuses": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "responseMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "triggerIntent": t.string().optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"]).optional(),
            "languageCode": t.string().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultOut"]
            ).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerEvent": t.string().optional(),
            "webhookPayloads": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "transcript": t.string().optional(),
            "text": t.string().optional(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3DtmfInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryResultOut"])
    types["GoogleCloudDialogflowV2beta1SentimentIn"] = t.struct(
        {"magnitude": t.number().optional(), "score": t.number().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1SentimentIn"])
    types["GoogleCloudDialogflowV2beta1SentimentOut"] = t.struct(
        {
            "magnitude": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SentimentOut"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn"] = t.struct(
        {"metadata": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn"])
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut"
    ] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut"]
    )
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn"
    ] = t.struct({"uri": t.string().optional(), "audio": t.string().optional()}).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut"
    ] = t.struct(
        {
            "uri": t.string().optional(),
            "audio": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut"]
    )
    types["GoogleCloudDialogflowV2IntentMessageSuggestionsIn"] = t.struct(
        {
            "suggestions": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageSuggestionIn"])
            )
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSuggestionsIn"])
    types["GoogleCloudDialogflowV2IntentMessageSuggestionsOut"] = t.struct(
        {
            "suggestions": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageSuggestionOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSuggestionsOut"])
    types["GoogleCloudDialogflowCxV3DtmfInputIn"] = t.struct(
        {"digits": t.string().optional(), "finishDigit": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3DtmfInputIn"])
    types["GoogleCloudDialogflowCxV3DtmfInputOut"] = t.struct(
        {
            "digits": t.string().optional(),
            "finishDigit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DtmfInputOut"])
    types["GoogleCloudDialogflowCxV3SentimentAnalysisResultIn"] = t.struct(
        {"score": t.number().optional(), "magnitude": t.number().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultIn"])
    types["GoogleCloudDialogflowCxV3SentimentAnalysisResultOut"] = t.struct(
        {
            "score": t.number().optional(),
            "magnitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultOut"])
    types["GoogleCloudDialogflowV2beta1ArticleAnswerIn"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "uri": t.string().optional(),
            "title": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "snippets": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ArticleAnswerIn"])
    types["GoogleCloudDialogflowV2beta1ArticleAnswerOut"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "uri": t.string().optional(),
            "title": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "snippets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ArticleAnswerOut"])

    functions = {}
    functions["projectsOperationsCancel"] = dialogflow.get(
        "v3/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = dialogflow.get(
        "v3/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = dialogflow.get(
        "v3/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudLocationLocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudLocationLocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = dialogflow.get(
        "v3/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = dialogflow.get(
        "v3/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = dialogflow.get(
        "v3/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsCreate"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsDelete"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsGetValidationResult"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsValidate"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsRestore"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsPatch"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsExport"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsList"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3AgentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPatch"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsTrain"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsImport"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsDelete"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsList"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsValidate"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsExport"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsCreate"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsGetValidationResult"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsTransitionRouteGroupsGet"] = dialogflow.get(
        "v3/{parent}/transitionRouteGroups",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsFlowsTransitionRouteGroupsPatch"
    ] = dialogflow.get(
        "v3/{parent}/transitionRouteGroups",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsFlowsTransitionRouteGroupsDelete"
    ] = dialogflow.get(
        "v3/{parent}/transitionRouteGroups",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsFlowsTransitionRouteGroupsCreate"
    ] = dialogflow.get(
        "v3/{parent}/transitionRouteGroups",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsTransitionRouteGroupsList"] = dialogflow.get(
        "v3/{parent}/transitionRouteGroups",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsCreate"] = dialogflow.get(
        "v3/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsDelete"] = dialogflow.get(
        "v3/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsGet"] = dialogflow.get(
        "v3/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsPatch"] = dialogflow.get(
        "v3/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsCompareVersions"] = dialogflow.get(
        "v3/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsLoad"] = dialogflow.get(
        "v3/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsList"] = dialogflow.get(
        "v3/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesDelete"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesGet"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesList"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesCreate"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesPatch"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksPatch"] = dialogflow.get(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksGet"] = dialogflow.get(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksCreate"] = dialogflow.get(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksDelete"] = dialogflow.get(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksList"] = dialogflow.get(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsMatchIntent"] = dialogflow.post(
        "v3/{session}:detectIntent",
        t.struct(
            {
                "session": t.string(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "queryParams": t.proxy(
                    renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
                ).optional(),
                "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3DetectIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsFulfillIntent"] = dialogflow.post(
        "v3/{session}:detectIntent",
        t.struct(
            {
                "session": t.string(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "queryParams": t.proxy(
                    renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
                ).optional(),
                "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3DetectIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsDetectIntent"] = dialogflow.post(
        "v3/{session}:detectIntent",
        t.struct(
            {
                "session": t.string(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "queryParams": t.proxy(
                    renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
                ).optional(),
                "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3DetectIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesGet"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "entityOverrideMode": t.string(),
                "entities": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesCreate"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "entityOverrideMode": t.string(),
                "entities": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesDelete"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "entityOverrideMode": t.string(),
                "entities": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesList"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "entityOverrideMode": t.string(),
                "entities": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesPatch"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "entityOverrideMode": t.string(),
                "entities": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsChangelogsList"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ChangelogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsChangelogsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ChangelogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsList"] = dialogflow.get(
        "v3/{name}:lookupEnvironmentHistory",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsGet"] = dialogflow.get(
        "v3/{name}:lookupEnvironmentHistory",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsRunContinuousTest"] = dialogflow.get(
        "v3/{name}:lookupEnvironmentHistory",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDelete"] = dialogflow.get(
        "v3/{name}:lookupEnvironmentHistory",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsPatch"] = dialogflow.get(
        "v3/{name}:lookupEnvironmentHistory",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDeployFlow"] = dialogflow.get(
        "v3/{name}:lookupEnvironmentHistory",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsCreate"] = dialogflow.get(
        "v3/{name}:lookupEnvironmentHistory",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsLookupEnvironmentHistory"
    ] = dialogflow.get(
        "v3/{name}:lookupEnvironmentHistory",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsContinuousTestResultsList"
    ] = dialogflow.get(
        "v3/{parent}/continuousTestResults",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsCreate"] = dialogflow.post(
        "v3/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsDelete"] = dialogflow.post(
        "v3/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsPatch"] = dialogflow.post(
        "v3/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsList"] = dialogflow.post(
        "v3/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsGet"] = dialogflow.post(
        "v3/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsStop"] = dialogflow.post(
        "v3/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsStart"] = dialogflow.post(
        "v3/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDeploymentsList"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDeploymentsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsDetectIntent"
    ] = dialogflow.post(
        "v3/{session}:fulfillIntent",
        t.struct(
            {
                "session": t.string(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
                ).optional(),
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsMatchIntent"
    ] = dialogflow.post(
        "v3/{session}:fulfillIntent",
        t.struct(
            {
                "session": t.string(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
                ).optional(),
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsFulfillIntent"
    ] = dialogflow.post(
        "v3/{session}:fulfillIntent",
        t.struct(
            {
                "session": t.string(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
                ).optional(),
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesCreate"
    ] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesPatch"
    ] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesDelete"
    ] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesList"
    ] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesGet"
    ] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesBatchDelete"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesBatchRun"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesGet"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesCalculateCoverage"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesExport"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesList"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesRun"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesCreate"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesImport"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesPatch"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "testConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestConfigIn"]
                ).optional(),
                "tags": t.array(t.string()).optional(),
                "displayName": t.string(),
                "testCaseConversationTurns": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
                ).optional(),
                "notes": t.string().optional(),
                "lastTestResult": t.proxy(
                    renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesResultsList"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseResultOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesResultsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseResultOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEntityTypesPatch"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEntityTypesCreate"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEntityTypesList"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEntityTypesDelete"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEntityTypesGet"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsPatch"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsGet"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsList"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsCreate"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsDelete"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsDelete"] = dialogflow.get(
        "v3/{parent}/securitySettings",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsCreate"] = dialogflow.get(
        "v3/{parent}/securitySettings",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsGet"] = dialogflow.get(
        "v3/{parent}/securitySettings",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsPatch"] = dialogflow.get(
        "v3/{parent}/securitySettings",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsList"] = dialogflow.get(
        "v3/{parent}/securitySettings",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dialogflow",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
