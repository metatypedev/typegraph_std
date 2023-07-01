from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_dialogflow():
    dialogflow = HTTPRuntime("https://dialogflow.googleapis.com/")

    renames = {
        "ErrorResponse": "_dialogflow_1_ErrorResponse",
        "GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn": "_dialogflow_2_GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn",
        "GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut": "_dialogflow_3_GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn": "_dialogflow_4_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut": "_dialogflow_5_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut",
        "GoogleCloudDialogflowCxV3DeployFlowRequestIn": "_dialogflow_6_GoogleCloudDialogflowCxV3DeployFlowRequestIn",
        "GoogleCloudDialogflowCxV3DeployFlowRequestOut": "_dialogflow_7_GoogleCloudDialogflowCxV3DeployFlowRequestOut",
        "GoogleCloudDialogflowCxV3TestCaseErrorIn": "_dialogflow_8_GoogleCloudDialogflowCxV3TestCaseErrorIn",
        "GoogleCloudDialogflowCxV3TestCaseErrorOut": "_dialogflow_9_GoogleCloudDialogflowCxV3TestCaseErrorOut",
        "GoogleCloudDialogflowCxV3DeploymentIn": "_dialogflow_10_GoogleCloudDialogflowCxV3DeploymentIn",
        "GoogleCloudDialogflowCxV3DeploymentOut": "_dialogflow_11_GoogleCloudDialogflowCxV3DeploymentOut",
        "GoogleCloudDialogflowV2GcsDestinationIn": "_dialogflow_12_GoogleCloudDialogflowV2GcsDestinationIn",
        "GoogleCloudDialogflowV2GcsDestinationOut": "_dialogflow_13_GoogleCloudDialogflowV2GcsDestinationOut",
        "GoogleCloudDialogflowCxV3IntentTrainingPhraseIn": "_dialogflow_14_GoogleCloudDialogflowCxV3IntentTrainingPhraseIn",
        "GoogleCloudDialogflowCxV3IntentTrainingPhraseOut": "_dialogflow_15_GoogleCloudDialogflowCxV3IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3CompareVersionsResponseIn": "_dialogflow_16_GoogleCloudDialogflowCxV3CompareVersionsResponseIn",
        "GoogleCloudDialogflowCxV3CompareVersionsResponseOut": "_dialogflow_17_GoogleCloudDialogflowCxV3CompareVersionsResponseOut",
        "GoogleCloudDialogflowCxV3beta1FormParameterIn": "_dialogflow_18_GoogleCloudDialogflowCxV3beta1FormParameterIn",
        "GoogleCloudDialogflowCxV3beta1FormParameterOut": "_dialogflow_19_GoogleCloudDialogflowCxV3beta1FormParameterOut",
        "GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn": "_dialogflow_20_GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn",
        "GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut": "_dialogflow_21_GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn": "_dialogflow_22_GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut": "_dialogflow_23_GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut",
        "GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn": "_dialogflow_24_GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut": "_dialogflow_25_GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut",
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn": "_dialogflow_26_GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut": "_dialogflow_27_GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageIn": "_dialogflow_28_GoogleCloudDialogflowCxV3beta1ResponseMessageIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOut": "_dialogflow_29_GoogleCloudDialogflowCxV3beta1ResponseMessageOut",
        "GoogleCloudDialogflowV2beta1IntentMessageImageIn": "_dialogflow_30_GoogleCloudDialogflowV2beta1IntentMessageImageIn",
        "GoogleCloudDialogflowV2beta1IntentMessageImageOut": "_dialogflow_31_GoogleCloudDialogflowV2beta1IntentMessageImageOut",
        "GoogleCloudDialogflowV2WebhookResponseIn": "_dialogflow_32_GoogleCloudDialogflowV2WebhookResponseIn",
        "GoogleCloudDialogflowV2WebhookResponseOut": "_dialogflow_33_GoogleCloudDialogflowV2WebhookResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn": "_dialogflow_34_GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut": "_dialogflow_35_GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn": "_dialogflow_36_GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut": "_dialogflow_37_GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn": "_dialogflow_38_GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut": "_dialogflow_39_GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueIn": "_dialogflow_40_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueOut": "_dialogflow_41_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueOut",
        "GoogleCloudDialogflowCxV3VersionVariantsVariantIn": "_dialogflow_42_GoogleCloudDialogflowCxV3VersionVariantsVariantIn",
        "GoogleCloudDialogflowCxV3VersionVariantsVariantOut": "_dialogflow_43_GoogleCloudDialogflowCxV3VersionVariantsVariantOut",
        "GoogleCloudDialogflowCxV3ResourceNameIn": "_dialogflow_44_GoogleCloudDialogflowCxV3ResourceNameIn",
        "GoogleCloudDialogflowCxV3ResourceNameOut": "_dialogflow_45_GoogleCloudDialogflowCxV3ResourceNameOut",
        "GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataIn": "_dialogflow_46_GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataOut": "_dialogflow_47_GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3WebhookResponseIn": "_dialogflow_48_GoogleCloudDialogflowCxV3WebhookResponseIn",
        "GoogleCloudDialogflowCxV3WebhookResponseOut": "_dialogflow_49_GoogleCloudDialogflowCxV3WebhookResponseOut",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataIn": "_dialogflow_50_GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataOut": "_dialogflow_51_GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ListTestCasesResponseIn": "_dialogflow_52_GoogleCloudDialogflowCxV3ListTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ListTestCasesResponseOut": "_dialogflow_53_GoogleCloudDialogflowCxV3ListTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIn": "_dialogflow_54_GoogleCloudDialogflowCxV3beta1WebhookRequestIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestOut": "_dialogflow_55_GoogleCloudDialogflowCxV3beta1WebhookRequestOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn": "_dialogflow_56_GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut": "_dialogflow_57_GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut",
        "GoogleCloudDialogflowCxV3beta1IntentInputIn": "_dialogflow_58_GoogleCloudDialogflowCxV3beta1IntentInputIn",
        "GoogleCloudDialogflowCxV3beta1IntentInputOut": "_dialogflow_59_GoogleCloudDialogflowCxV3beta1IntentInputOut",
        "GoogleCloudDialogflowCxV3SessionEntityTypeIn": "_dialogflow_60_GoogleCloudDialogflowCxV3SessionEntityTypeIn",
        "GoogleCloudDialogflowCxV3SessionEntityTypeOut": "_dialogflow_61_GoogleCloudDialogflowCxV3SessionEntityTypeOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn": "_dialogflow_62_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut": "_dialogflow_63_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut",
        "GoogleCloudDialogflowCxV3EventInputIn": "_dialogflow_64_GoogleCloudDialogflowCxV3EventInputIn",
        "GoogleCloudDialogflowCxV3EventInputOut": "_dialogflow_65_GoogleCloudDialogflowCxV3EventInputOut",
        "GoogleCloudDialogflowCxV3TestErrorIn": "_dialogflow_66_GoogleCloudDialogflowCxV3TestErrorIn",
        "GoogleCloudDialogflowCxV3TestErrorOut": "_dialogflow_67_GoogleCloudDialogflowCxV3TestErrorOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn": "_dialogflow_68_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut": "_dialogflow_69_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut",
        "GoogleCloudDialogflowCxV3DeployFlowMetadataIn": "_dialogflow_70_GoogleCloudDialogflowCxV3DeployFlowMetadataIn",
        "GoogleCloudDialogflowCxV3DeployFlowMetadataOut": "_dialogflow_71_GoogleCloudDialogflowCxV3DeployFlowMetadataOut",
        "GoogleCloudDialogflowCxV3FulfillIntentResponseIn": "_dialogflow_72_GoogleCloudDialogflowCxV3FulfillIntentResponseIn",
        "GoogleCloudDialogflowCxV3FulfillIntentResponseOut": "_dialogflow_73_GoogleCloudDialogflowCxV3FulfillIntentResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn": "_dialogflow_74_GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut": "_dialogflow_75_GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut",
        "GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn": "_dialogflow_76_GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn",
        "GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut": "_dialogflow_77_GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut",
        "GoogleCloudDialogflowCxV3TurnSignalsIn": "_dialogflow_78_GoogleCloudDialogflowCxV3TurnSignalsIn",
        "GoogleCloudDialogflowCxV3TurnSignalsOut": "_dialogflow_79_GoogleCloudDialogflowCxV3TurnSignalsOut",
        "GoogleCloudDialogflowCxV3beta1AudioInputIn": "_dialogflow_80_GoogleCloudDialogflowCxV3beta1AudioInputIn",
        "GoogleCloudDialogflowCxV3beta1AudioInputOut": "_dialogflow_81_GoogleCloudDialogflowCxV3beta1AudioInputOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesResponseIn": "_dialogflow_82_GoogleCloudDialogflowCxV3ExportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesResponseOut": "_dialogflow_83_GoogleCloudDialogflowCxV3ExportTestCasesResponseOut",
        "GoogleCloudDialogflowV2beta1ExportAgentResponseIn": "_dialogflow_84_GoogleCloudDialogflowV2beta1ExportAgentResponseIn",
        "GoogleCloudDialogflowV2beta1ExportAgentResponseOut": "_dialogflow_85_GoogleCloudDialogflowV2beta1ExportAgentResponseOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageIn": "_dialogflow_86_GoogleCloudDialogflowCxV3TransitionCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageOut": "_dialogflow_87_GoogleCloudDialogflowCxV3TransitionCoverageOut",
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn": "_dialogflow_88_GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut": "_dialogflow_89_GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataIn": "_dialogflow_90_GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataOut": "_dialogflow_91_GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3PageInfoIn": "_dialogflow_92_GoogleCloudDialogflowCxV3PageInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoOut": "_dialogflow_93_GoogleCloudDialogflowCxV3PageInfoOut",
        "GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn": "_dialogflow_94_GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn",
        "GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut": "_dialogflow_95_GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut",
        "GoogleCloudDialogflowCxV3QueryParametersIn": "_dialogflow_96_GoogleCloudDialogflowCxV3QueryParametersIn",
        "GoogleCloudDialogflowCxV3QueryParametersOut": "_dialogflow_97_GoogleCloudDialogflowCxV3QueryParametersOut",
        "GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn": "_dialogflow_98_GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn",
        "GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut": "_dialogflow_99_GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut",
        "GoogleCloudDialogflowV2beta1EntityTypeIn": "_dialogflow_100_GoogleCloudDialogflowV2beta1EntityTypeIn",
        "GoogleCloudDialogflowV2beta1EntityTypeOut": "_dialogflow_101_GoogleCloudDialogflowV2beta1EntityTypeOut",
        "GoogleCloudDialogflowCxV3FormParameterIn": "_dialogflow_102_GoogleCloudDialogflowCxV3FormParameterIn",
        "GoogleCloudDialogflowCxV3FormParameterOut": "_dialogflow_103_GoogleCloudDialogflowCxV3FormParameterOut",
        "GoogleCloudDialogflowV2InputDatasetIn": "_dialogflow_104_GoogleCloudDialogflowV2InputDatasetIn",
        "GoogleCloudDialogflowV2InputDatasetOut": "_dialogflow_105_GoogleCloudDialogflowV2InputDatasetOut",
        "GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn": "_dialogflow_106_GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn",
        "GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut": "_dialogflow_107_GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn": "_dialogflow_108_GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut": "_dialogflow_109_GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn": "_dialogflow_110_GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut": "_dialogflow_111_GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardIn": "_dialogflow_112_GoogleCloudDialogflowV2IntentMessageBasicCardIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardOut": "_dialogflow_113_GoogleCloudDialogflowV2IntentMessageBasicCardOut",
        "GoogleCloudDialogflowCxV3TestConfigIn": "_dialogflow_114_GoogleCloudDialogflowCxV3TestConfigIn",
        "GoogleCloudDialogflowCxV3TestConfigOut": "_dialogflow_115_GoogleCloudDialogflowCxV3TestConfigOut",
        "GoogleCloudDialogflowCxV3beta1TestErrorIn": "_dialogflow_116_GoogleCloudDialogflowCxV3beta1TestErrorIn",
        "GoogleCloudDialogflowCxV3beta1TestErrorOut": "_dialogflow_117_GoogleCloudDialogflowCxV3beta1TestErrorOut",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn": "_dialogflow_118_GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut": "_dialogflow_119_GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn": "_dialogflow_120_GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn",
        "GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut": "_dialogflow_121_GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut",
        "GoogleCloudDialogflowCxV3FulfillIntentRequestIn": "_dialogflow_122_GoogleCloudDialogflowCxV3FulfillIntentRequestIn",
        "GoogleCloudDialogflowCxV3FulfillIntentRequestOut": "_dialogflow_123_GoogleCloudDialogflowCxV3FulfillIntentRequestOut",
        "GoogleCloudDialogflowCxV3QueryResultIn": "_dialogflow_124_GoogleCloudDialogflowCxV3QueryResultIn",
        "GoogleCloudDialogflowCxV3QueryResultOut": "_dialogflow_125_GoogleCloudDialogflowCxV3QueryResultOut",
        "GoogleCloudDialogflowV2FaqAnswerIn": "_dialogflow_126_GoogleCloudDialogflowV2FaqAnswerIn",
        "GoogleCloudDialogflowV2FaqAnswerOut": "_dialogflow_127_GoogleCloudDialogflowV2FaqAnswerOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestResponseIn": "_dialogflow_128_GoogleCloudDialogflowCxV3RunContinuousTestResponseIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestResponseOut": "_dialogflow_129_GoogleCloudDialogflowCxV3RunContinuousTestResponseOut",
        "GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn": "_dialogflow_130_GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn",
        "GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut": "_dialogflow_131_GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn": "_dialogflow_132_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut": "_dialogflow_133_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn": "_dialogflow_134_GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut": "_dialogflow_135_GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn": "_dialogflow_136_GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut": "_dialogflow_137_GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut",
        "GoogleCloudDialogflowCxV3NluSettingsIn": "_dialogflow_138_GoogleCloudDialogflowCxV3NluSettingsIn",
        "GoogleCloudDialogflowCxV3NluSettingsOut": "_dialogflow_139_GoogleCloudDialogflowCxV3NluSettingsOut",
        "GoogleCloudDialogflowV2EntityTypeEntityIn": "_dialogflow_140_GoogleCloudDialogflowV2EntityTypeEntityIn",
        "GoogleCloudDialogflowV2EntityTypeEntityOut": "_dialogflow_141_GoogleCloudDialogflowV2EntityTypeEntityOut",
        "GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn": "_dialogflow_142_GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut": "_dialogflow_143_GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut",
        "GoogleCloudDialogflowCxV3ExportFlowResponseIn": "_dialogflow_144_GoogleCloudDialogflowCxV3ExportFlowResponseIn",
        "GoogleCloudDialogflowCxV3ExportFlowResponseOut": "_dialogflow_145_GoogleCloudDialogflowCxV3ExportFlowResponseOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn": "_dialogflow_146_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut": "_dialogflow_147_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut",
        "GoogleCloudDialogflowCxV3ValidateAgentRequestIn": "_dialogflow_148_GoogleCloudDialogflowCxV3ValidateAgentRequestIn",
        "GoogleCloudDialogflowCxV3ValidateAgentRequestOut": "_dialogflow_149_GoogleCloudDialogflowCxV3ValidateAgentRequestOut",
        "GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseIn": "_dialogflow_150_GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseIn",
        "GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut": "_dialogflow_151_GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn": "_dialogflow_152_GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut": "_dialogflow_153_GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut",
        "GoogleCloudDialogflowV2beta1MessageAnnotationIn": "_dialogflow_154_GoogleCloudDialogflowV2beta1MessageAnnotationIn",
        "GoogleCloudDialogflowV2beta1MessageAnnotationOut": "_dialogflow_155_GoogleCloudDialogflowV2beta1MessageAnnotationOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn": "_dialogflow_156_GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut": "_dialogflow_157_GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut",
        "GoogleTypeLatLngIn": "_dialogflow_158_GoogleTypeLatLngIn",
        "GoogleTypeLatLngOut": "_dialogflow_159_GoogleTypeLatLngOut",
        "GoogleCloudDialogflowCxV3TransitionRouteIn": "_dialogflow_160_GoogleCloudDialogflowCxV3TransitionRouteIn",
        "GoogleCloudDialogflowCxV3TransitionRouteOut": "_dialogflow_161_GoogleCloudDialogflowCxV3TransitionRouteOut",
        "GoogleCloudDialogflowCxV3IntentIn": "_dialogflow_162_GoogleCloudDialogflowCxV3IntentIn",
        "GoogleCloudDialogflowCxV3IntentOut": "_dialogflow_163_GoogleCloudDialogflowCxV3IntentOut",
        "GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn": "_dialogflow_164_GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut": "_dialogflow_165_GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut",
        "GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn": "_dialogflow_166_GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut": "_dialogflow_167_GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageIn": "_dialogflow_168_GoogleCloudDialogflowV2beta1IntentMessageIn",
        "GoogleCloudDialogflowV2beta1IntentMessageOut": "_dialogflow_169_GoogleCloudDialogflowV2beta1IntentMessageOut",
        "GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn": "_dialogflow_170_GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn",
        "GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut": "_dialogflow_171_GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1TextInputIn": "_dialogflow_172_GoogleCloudDialogflowCxV3beta1TextInputIn",
        "GoogleCloudDialogflowCxV3beta1TextInputOut": "_dialogflow_173_GoogleCloudDialogflowCxV3beta1TextInputOut",
        "GoogleCloudDialogflowCxV3TextToSpeechSettingsIn": "_dialogflow_174_GoogleCloudDialogflowCxV3TextToSpeechSettingsIn",
        "GoogleCloudDialogflowCxV3TextToSpeechSettingsOut": "_dialogflow_175_GoogleCloudDialogflowCxV3TextToSpeechSettingsOut",
        "GoogleCloudDialogflowCxV3DeployFlowResponseIn": "_dialogflow_176_GoogleCloudDialogflowCxV3DeployFlowResponseIn",
        "GoogleCloudDialogflowCxV3DeployFlowResponseOut": "_dialogflow_177_GoogleCloudDialogflowCxV3DeployFlowResponseOut",
        "GoogleCloudDialogflowCxV3AdvancedSettingsIn": "_dialogflow_178_GoogleCloudDialogflowCxV3AdvancedSettingsIn",
        "GoogleCloudDialogflowCxV3AdvancedSettingsOut": "_dialogflow_179_GoogleCloudDialogflowCxV3AdvancedSettingsOut",
        "GoogleCloudDialogflowCxV3ExportFlowRequestIn": "_dialogflow_180_GoogleCloudDialogflowCxV3ExportFlowRequestIn",
        "GoogleCloudDialogflowCxV3ExportFlowRequestOut": "_dialogflow_181_GoogleCloudDialogflowCxV3ExportFlowRequestOut",
        "GoogleCloudDialogflowCxV3FormIn": "_dialogflow_182_GoogleCloudDialogflowCxV3FormIn",
        "GoogleCloudDialogflowCxV3FormOut": "_dialogflow_183_GoogleCloudDialogflowCxV3FormOut",
        "GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn": "_dialogflow_184_GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut": "_dialogflow_185_GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesMetadataIn": "_dialogflow_186_GoogleCloudDialogflowCxV3ImportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesMetadataOut": "_dialogflow_187_GoogleCloudDialogflowCxV3ImportTestCasesMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn": "_dialogflow_188_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut": "_dialogflow_189_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut",
        "GoogleCloudDialogflowV2beta1SuggestionResultIn": "_dialogflow_190_GoogleCloudDialogflowV2beta1SuggestionResultIn",
        "GoogleCloudDialogflowV2beta1SuggestionResultOut": "_dialogflow_191_GoogleCloudDialogflowV2beta1SuggestionResultOut",
        "GoogleCloudDialogflowCxV3RunTestCaseRequestIn": "_dialogflow_192_GoogleCloudDialogflowCxV3RunTestCaseRequestIn",
        "GoogleCloudDialogflowCxV3RunTestCaseRequestOut": "_dialogflow_193_GoogleCloudDialogflowCxV3RunTestCaseRequestOut",
        "GoogleCloudDialogflowV2IntentMessageCardIn": "_dialogflow_194_GoogleCloudDialogflowV2IntentMessageCardIn",
        "GoogleCloudDialogflowV2IntentMessageCardOut": "_dialogflow_195_GoogleCloudDialogflowV2IntentMessageCardOut",
        "GoogleCloudDialogflowCxV3SessionInfoIn": "_dialogflow_196_GoogleCloudDialogflowCxV3SessionInfoIn",
        "GoogleCloudDialogflowCxV3SessionInfoOut": "_dialogflow_197_GoogleCloudDialogflowCxV3SessionInfoOut",
        "GoogleCloudDialogflowCxV3ListDeploymentsResponseIn": "_dialogflow_198_GoogleCloudDialogflowCxV3ListDeploymentsResponseIn",
        "GoogleCloudDialogflowCxV3ListDeploymentsResponseOut": "_dialogflow_199_GoogleCloudDialogflowCxV3ListDeploymentsResponseOut",
        "GoogleCloudDialogflowCxV3SentimentAnalysisResultIn": "_dialogflow_200_GoogleCloudDialogflowCxV3SentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3SentimentAnalysisResultOut": "_dialogflow_201_GoogleCloudDialogflowCxV3SentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3beta1InputAudioConfigIn": "_dialogflow_202_GoogleCloudDialogflowCxV3beta1InputAudioConfigIn",
        "GoogleCloudDialogflowCxV3beta1InputAudioConfigOut": "_dialogflow_203_GoogleCloudDialogflowCxV3beta1InputAudioConfigOut",
        "GoogleCloudLocationListLocationsResponseIn": "_dialogflow_204_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_dialogflow_205_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudDialogflowV2IntentIn": "_dialogflow_206_GoogleCloudDialogflowV2IntentIn",
        "GoogleCloudDialogflowV2IntentOut": "_dialogflow_207_GoogleCloudDialogflowV2IntentOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn": "_dialogflow_208_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut": "_dialogflow_209_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn": "_dialogflow_210_GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut": "_dialogflow_211_GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectIn": "_dialogflow_212_GoogleCloudDialogflowV2IntentMessageCarouselSelectIn",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectOut": "_dialogflow_213_GoogleCloudDialogflowV2IntentMessageCarouselSelectOut",
        "GoogleCloudDialogflowCxV3ListVersionsResponseIn": "_dialogflow_214_GoogleCloudDialogflowCxV3ListVersionsResponseIn",
        "GoogleCloudDialogflowCxV3ListVersionsResponseOut": "_dialogflow_215_GoogleCloudDialogflowCxV3ListVersionsResponseOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn": "_dialogflow_216_GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut": "_dialogflow_217_GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowV2beta1FaqAnswerIn": "_dialogflow_218_GoogleCloudDialogflowV2beta1FaqAnswerIn",
        "GoogleCloudDialogflowV2beta1FaqAnswerOut": "_dialogflow_219_GoogleCloudDialogflowV2beta1FaqAnswerOut",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn": "_dialogflow_220_GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut": "_dialogflow_221_GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn": "_dialogflow_222_GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut": "_dialogflow_223_GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3DeploymentResultIn": "_dialogflow_224_GoogleCloudDialogflowCxV3DeploymentResultIn",
        "GoogleCloudDialogflowCxV3DeploymentResultOut": "_dialogflow_225_GoogleCloudDialogflowCxV3DeploymentResultOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardIn": "_dialogflow_226_GoogleCloudDialogflowV2beta1IntentMessageTableCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardOut": "_dialogflow_227_GoogleCloudDialogflowV2beta1IntentMessageTableCardOut",
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn": "_dialogflow_228_GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn",
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut": "_dialogflow_229_GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn": "_dialogflow_230_GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut": "_dialogflow_231_GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut",
        "GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn": "_dialogflow_232_GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn",
        "GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut": "_dialogflow_233_GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3ExperimentDefinitionIn": "_dialogflow_234_GoogleCloudDialogflowCxV3ExperimentDefinitionIn",
        "GoogleCloudDialogflowCxV3ExperimentDefinitionOut": "_dialogflow_235_GoogleCloudDialogflowCxV3ExperimentDefinitionOut",
        "GoogleCloudDialogflowCxV3VariantsHistoryIn": "_dialogflow_236_GoogleCloudDialogflowCxV3VariantsHistoryIn",
        "GoogleCloudDialogflowCxV3VariantsHistoryOut": "_dialogflow_237_GoogleCloudDialogflowCxV3VariantsHistoryOut",
        "GoogleCloudDialogflowV2EventInputIn": "_dialogflow_238_GoogleCloudDialogflowV2EventInputIn",
        "GoogleCloudDialogflowV2EventInputOut": "_dialogflow_239_GoogleCloudDialogflowV2EventInputOut",
        "GoogleCloudDialogflowCxV3ImportFlowRequestIn": "_dialogflow_240_GoogleCloudDialogflowCxV3ImportFlowRequestIn",
        "GoogleCloudDialogflowCxV3ImportFlowRequestOut": "_dialogflow_241_GoogleCloudDialogflowCxV3ImportFlowRequestOut",
        "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn": "_dialogflow_242_GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut": "_dialogflow_243_GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn": "_dialogflow_244_GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut": "_dialogflow_245_GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut",
        "GoogleCloudDialogflowV2SuggestArticlesResponseIn": "_dialogflow_246_GoogleCloudDialogflowV2SuggestArticlesResponseIn",
        "GoogleCloudDialogflowV2SuggestArticlesResponseOut": "_dialogflow_247_GoogleCloudDialogflowV2SuggestArticlesResponseOut",
        "GoogleCloudDialogflowCxV3TestCaseIn": "_dialogflow_248_GoogleCloudDialogflowCxV3TestCaseIn",
        "GoogleCloudDialogflowCxV3TestCaseOut": "_dialogflow_249_GoogleCloudDialogflowCxV3TestCaseOut",
        "GoogleCloudDialogflowCxV3PageIn": "_dialogflow_250_GoogleCloudDialogflowCxV3PageIn",
        "GoogleCloudDialogflowCxV3PageOut": "_dialogflow_251_GoogleCloudDialogflowCxV3PageOut",
        "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn": "_dialogflow_252_GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn",
        "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut": "_dialogflow_253_GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut",
        "GoogleCloudDialogflowCxV3FlowIn": "_dialogflow_254_GoogleCloudDialogflowCxV3FlowIn",
        "GoogleCloudDialogflowCxV3FlowOut": "_dialogflow_255_GoogleCloudDialogflowCxV3FlowOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupIn": "_dialogflow_256_GoogleCloudDialogflowCxV3TransitionRouteGroupIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupOut": "_dialogflow_257_GoogleCloudDialogflowCxV3TransitionRouteGroupOut",
        "GoogleCloudDialogflowCxV3IntentParameterIn": "_dialogflow_258_GoogleCloudDialogflowCxV3IntentParameterIn",
        "GoogleCloudDialogflowCxV3IntentParameterOut": "_dialogflow_259_GoogleCloudDialogflowCxV3IntentParameterOut",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn": "_dialogflow_260_GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut": "_dialogflow_261_GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn": "_dialogflow_262_GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn",
        "GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut": "_dialogflow_263_GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut",
        "GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn": "_dialogflow_264_GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn",
        "GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut": "_dialogflow_265_GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut",
        "GoogleCloudDialogflowCxV3MatchIntentResponseIn": "_dialogflow_266_GoogleCloudDialogflowCxV3MatchIntentResponseIn",
        "GoogleCloudDialogflowCxV3MatchIntentResponseOut": "_dialogflow_267_GoogleCloudDialogflowCxV3MatchIntentResponseOut",
        "GoogleCloudDialogflowCxV3RestoreAgentRequestIn": "_dialogflow_268_GoogleCloudDialogflowCxV3RestoreAgentRequestIn",
        "GoogleCloudDialogflowCxV3RestoreAgentRequestOut": "_dialogflow_269_GoogleCloudDialogflowCxV3RestoreAgentRequestOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataIn": "_dialogflow_270_GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataOut": "_dialogflow_271_GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn": "_dialogflow_272_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut": "_dialogflow_273_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn": "_dialogflow_274_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut": "_dialogflow_275_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut",
        "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn": "_dialogflow_276_GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut": "_dialogflow_277_GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseIn": "_dialogflow_278_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseOut": "_dialogflow_279_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3MatchIntentRequestIn": "_dialogflow_280_GoogleCloudDialogflowCxV3MatchIntentRequestIn",
        "GoogleCloudDialogflowCxV3MatchIntentRequestOut": "_dialogflow_281_GoogleCloudDialogflowCxV3MatchIntentRequestOut",
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn": "_dialogflow_282_GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut": "_dialogflow_283_GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_284_GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_285_GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn": "_dialogflow_286_GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut": "_dialogflow_287_GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3beta1IntentIn": "_dialogflow_288_GoogleCloudDialogflowCxV3beta1IntentIn",
        "GoogleCloudDialogflowCxV3beta1IntentOut": "_dialogflow_289_GoogleCloudDialogflowCxV3beta1IntentOut",
        "GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataIn": "_dialogflow_290_GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataOut": "_dialogflow_291_GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataIn": "_dialogflow_292_GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataOut": "_dialogflow_293_GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3FlowValidationResultIn": "_dialogflow_294_GoogleCloudDialogflowCxV3FlowValidationResultIn",
        "GoogleCloudDialogflowCxV3FlowValidationResultOut": "_dialogflow_295_GoogleCloudDialogflowCxV3FlowValidationResultOut",
        "GoogleCloudDialogflowV2SuggestionResultIn": "_dialogflow_296_GoogleCloudDialogflowV2SuggestionResultIn",
        "GoogleCloudDialogflowV2SuggestionResultOut": "_dialogflow_297_GoogleCloudDialogflowV2SuggestionResultOut",
        "GoogleCloudDialogflowV3alpha1ConversationSignalsIn": "_dialogflow_298_GoogleCloudDialogflowV3alpha1ConversationSignalsIn",
        "GoogleCloudDialogflowV3alpha1ConversationSignalsOut": "_dialogflow_299_GoogleCloudDialogflowV3alpha1ConversationSignalsOut",
        "GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn": "_dialogflow_300_GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn",
        "GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut": "_dialogflow_301_GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectIn": "_dialogflow_302_GoogleCloudDialogflowV2beta1IntentMessageListSelectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectOut": "_dialogflow_303_GoogleCloudDialogflowV2beta1IntentMessageListSelectOut",
        "GoogleCloudDialogflowCxV3RunTestCaseResponseIn": "_dialogflow_304_GoogleCloudDialogflowCxV3RunTestCaseResponseIn",
        "GoogleCloudDialogflowCxV3RunTestCaseResponseOut": "_dialogflow_305_GoogleCloudDialogflowCxV3RunTestCaseResponseOut",
        "GoogleCloudDialogflowCxV3ExperimentResultIn": "_dialogflow_306_GoogleCloudDialogflowCxV3ExperimentResultIn",
        "GoogleCloudDialogflowCxV3ExperimentResultOut": "_dialogflow_307_GoogleCloudDialogflowCxV3ExperimentResultOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesRequestIn": "_dialogflow_308_GoogleCloudDialogflowCxV3ImportTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesRequestOut": "_dialogflow_309_GoogleCloudDialogflowCxV3ImportTestCasesRequestOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn": "_dialogflow_310_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut": "_dialogflow_311_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut",
        "GoogleCloudDialogflowCxV3ListExperimentsResponseIn": "_dialogflow_312_GoogleCloudDialogflowCxV3ListExperimentsResponseIn",
        "GoogleCloudDialogflowCxV3ListExperimentsResponseOut": "_dialogflow_313_GoogleCloudDialogflowCxV3ListExperimentsResponseOut",
        "GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataIn": "_dialogflow_314_GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataOut": "_dialogflow_315_GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3IntentCoverageIn": "_dialogflow_316_GoogleCloudDialogflowCxV3IntentCoverageIn",
        "GoogleCloudDialogflowCxV3IntentCoverageOut": "_dialogflow_317_GoogleCloudDialogflowCxV3IntentCoverageOut",
        "GoogleCloudDialogflowCxV3ValidateFlowRequestIn": "_dialogflow_318_GoogleCloudDialogflowCxV3ValidateFlowRequestIn",
        "GoogleCloudDialogflowCxV3ValidateFlowRequestOut": "_dialogflow_319_GoogleCloudDialogflowCxV3ValidateFlowRequestOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn": "_dialogflow_320_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut": "_dialogflow_321_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardRowIn": "_dialogflow_322_GoogleCloudDialogflowV2IntentMessageTableCardRowIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardRowOut": "_dialogflow_323_GoogleCloudDialogflowV2IntentMessageTableCardRowOut",
        "GoogleCloudDialogflowCxV3beta1DtmfInputIn": "_dialogflow_324_GoogleCloudDialogflowCxV3beta1DtmfInputIn",
        "GoogleCloudDialogflowCxV3beta1DtmfInputOut": "_dialogflow_325_GoogleCloudDialogflowCxV3beta1DtmfInputOut",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoIn": "_dialogflow_326_GoogleCloudDialogflowCxV3PageInfoFormInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoOut": "_dialogflow_327_GoogleCloudDialogflowCxV3PageInfoFormInfoOut",
        "GoogleCloudDialogflowCxV3StopExperimentRequestIn": "_dialogflow_328_GoogleCloudDialogflowCxV3StopExperimentRequestIn",
        "GoogleCloudDialogflowCxV3StopExperimentRequestOut": "_dialogflow_329_GoogleCloudDialogflowCxV3StopExperimentRequestOut",
        "GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataIn": "_dialogflow_330_GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataOut": "_dialogflow_331_GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataOut",
        "GoogleCloudDialogflowV2IntentTrainingPhrasePartIn": "_dialogflow_332_GoogleCloudDialogflowV2IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowV2IntentTrainingPhrasePartOut": "_dialogflow_333_GoogleCloudDialogflowV2IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowCxV3StartExperimentRequestIn": "_dialogflow_334_GoogleCloudDialogflowCxV3StartExperimentRequestIn",
        "GoogleCloudDialogflowCxV3StartExperimentRequestOut": "_dialogflow_335_GoogleCloudDialogflowCxV3StartExperimentRequestOut",
        "GoogleCloudDialogflowCxV3ContinuousTestResultIn": "_dialogflow_336_GoogleCloudDialogflowCxV3ContinuousTestResultIn",
        "GoogleCloudDialogflowCxV3ContinuousTestResultOut": "_dialogflow_337_GoogleCloudDialogflowCxV3ContinuousTestResultOut",
        "GoogleCloudDialogflowV2IntentMessageQuickRepliesIn": "_dialogflow_338_GoogleCloudDialogflowV2IntentMessageQuickRepliesIn",
        "GoogleCloudDialogflowV2IntentMessageQuickRepliesOut": "_dialogflow_339_GoogleCloudDialogflowV2IntentMessageQuickRepliesOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn": "_dialogflow_340_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut": "_dialogflow_341_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut",
        "GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn": "_dialogflow_342_GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut": "_dialogflow_343_GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut",
        "GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn": "_dialogflow_344_GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut": "_dialogflow_345_GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowV2MessageAnnotationIn": "_dialogflow_346_GoogleCloudDialogflowV2MessageAnnotationIn",
        "GoogleCloudDialogflowV2MessageAnnotationOut": "_dialogflow_347_GoogleCloudDialogflowV2MessageAnnotationOut",
        "GoogleCloudDialogflowV2SentimentIn": "_dialogflow_348_GoogleCloudDialogflowV2SentimentIn",
        "GoogleCloudDialogflowV2SentimentOut": "_dialogflow_349_GoogleCloudDialogflowV2SentimentOut",
        "GoogleCloudDialogflowV2IntentMessageTextIn": "_dialogflow_350_GoogleCloudDialogflowV2IntentMessageTextIn",
        "GoogleCloudDialogflowV2IntentMessageTextOut": "_dialogflow_351_GoogleCloudDialogflowV2IntentMessageTextOut",
        "GoogleCloudDialogflowCxV3DetectIntentResponseIn": "_dialogflow_352_GoogleCloudDialogflowCxV3DetectIntentResponseIn",
        "GoogleCloudDialogflowCxV3DetectIntentResponseOut": "_dialogflow_353_GoogleCloudDialogflowCxV3DetectIntentResponseOut",
        "GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseIn": "_dialogflow_354_GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseOut": "_dialogflow_355_GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseOut",
        "GoogleCloudDialogflowV2ExportOperationMetadataIn": "_dialogflow_356_GoogleCloudDialogflowV2ExportOperationMetadataIn",
        "GoogleCloudDialogflowV2ExportOperationMetadataOut": "_dialogflow_357_GoogleCloudDialogflowV2ExportOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ConversationSignalsIn": "_dialogflow_358_GoogleCloudDialogflowCxV3ConversationSignalsIn",
        "GoogleCloudDialogflowCxV3ConversationSignalsOut": "_dialogflow_359_GoogleCloudDialogflowCxV3ConversationSignalsOut",
        "GoogleCloudDialogflowV2IntentParameterIn": "_dialogflow_360_GoogleCloudDialogflowV2IntentParameterIn",
        "GoogleCloudDialogflowV2IntentParameterOut": "_dialogflow_361_GoogleCloudDialogflowV2IntentParameterOut",
        "GoogleCloudDialogflowV2KnowledgeOperationMetadataIn": "_dialogflow_362_GoogleCloudDialogflowV2KnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV2KnowledgeOperationMetadataOut": "_dialogflow_363_GoogleCloudDialogflowV2KnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ResponseMessageTextIn": "_dialogflow_364_GoogleCloudDialogflowCxV3ResponseMessageTextIn",
        "GoogleCloudDialogflowCxV3ResponseMessageTextOut": "_dialogflow_365_GoogleCloudDialogflowCxV3ResponseMessageTextOut",
        "GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn": "_dialogflow_366_GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn",
        "GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut": "_dialogflow_367_GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn": "_dialogflow_368_GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut": "_dialogflow_369_GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut",
        "GoogleCloudDialogflowCxV3RunTestCaseMetadataIn": "_dialogflow_370_GoogleCloudDialogflowCxV3RunTestCaseMetadataIn",
        "GoogleCloudDialogflowCxV3RunTestCaseMetadataOut": "_dialogflow_371_GoogleCloudDialogflowCxV3RunTestCaseMetadataOut",
        "GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn": "_dialogflow_372_GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut": "_dialogflow_373_GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn": "_dialogflow_374_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut": "_dialogflow_375_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn": "_dialogflow_376_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut": "_dialogflow_377_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut",
        "GoogleCloudDialogflowV2SentimentAnalysisResultIn": "_dialogflow_378_GoogleCloudDialogflowV2SentimentAnalysisResultIn",
        "GoogleCloudDialogflowV2SentimentAnalysisResultOut": "_dialogflow_379_GoogleCloudDialogflowV2SentimentAnalysisResultOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn": "_dialogflow_380_GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut": "_dialogflow_381_GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowCxV3beta1EventInputIn": "_dialogflow_382_GoogleCloudDialogflowCxV3beta1EventInputIn",
        "GoogleCloudDialogflowCxV3beta1EventInputOut": "_dialogflow_383_GoogleCloudDialogflowCxV3beta1EventInputOut",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseIn": "_dialogflow_384_GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseIn",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseOut": "_dialogflow_385_GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseOut",
        "GoogleCloudDialogflowV2BatchUpdateIntentsResponseIn": "_dialogflow_386_GoogleCloudDialogflowV2BatchUpdateIntentsResponseIn",
        "GoogleCloudDialogflowV2BatchUpdateIntentsResponseOut": "_dialogflow_387_GoogleCloudDialogflowV2BatchUpdateIntentsResponseOut",
        "GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn": "_dialogflow_388_GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut": "_dialogflow_389_GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseIn": "_dialogflow_390_GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseIn",
        "GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseOut": "_dialogflow_391_GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseOut",
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn": "_dialogflow_392_GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn",
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut": "_dialogflow_393_GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentSuggestionIn": "_dialogflow_394_GoogleCloudDialogflowV2beta1IntentSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentSuggestionOut": "_dialogflow_395_GoogleCloudDialogflowV2beta1IntentSuggestionOut",
        "GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataIn": "_dialogflow_396_GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataOut": "_dialogflow_397_GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ConversationTurnIn": "_dialogflow_398_GoogleCloudDialogflowCxV3ConversationTurnIn",
        "GoogleCloudDialogflowCxV3ConversationTurnOut": "_dialogflow_399_GoogleCloudDialogflowCxV3ConversationTurnOut",
        "GoogleCloudDialogflowV2IntentMessageListSelectIn": "_dialogflow_400_GoogleCloudDialogflowV2IntentMessageListSelectIn",
        "GoogleCloudDialogflowV2IntentMessageListSelectOut": "_dialogflow_401_GoogleCloudDialogflowV2IntentMessageListSelectOut",
        "GoogleCloudDialogflowCxV3beta1IntentParameterIn": "_dialogflow_402_GoogleCloudDialogflowCxV3beta1IntentParameterIn",
        "GoogleCloudDialogflowCxV3beta1IntentParameterOut": "_dialogflow_403_GoogleCloudDialogflowCxV3beta1IntentParameterOut",
        "GoogleCloudDialogflowCxV3ListWebhooksResponseIn": "_dialogflow_404_GoogleCloudDialogflowCxV3ListWebhooksResponseIn",
        "GoogleCloudDialogflowCxV3ListWebhooksResponseOut": "_dialogflow_405_GoogleCloudDialogflowCxV3ListWebhooksResponseOut",
        "GoogleCloudDialogflowV2beta1QueryResultIn": "_dialogflow_406_GoogleCloudDialogflowV2beta1QueryResultIn",
        "GoogleCloudDialogflowV2beta1QueryResultOut": "_dialogflow_407_GoogleCloudDialogflowV2beta1QueryResultOut",
        "GoogleCloudDialogflowCxV3TrainFlowRequestIn": "_dialogflow_408_GoogleCloudDialogflowCxV3TrainFlowRequestIn",
        "GoogleCloudDialogflowCxV3TrainFlowRequestOut": "_dialogflow_409_GoogleCloudDialogflowCxV3TrainFlowRequestOut",
        "GoogleRpcStatusIn": "_dialogflow_410_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_dialogflow_411_GoogleRpcStatusOut",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataIn": "_dialogflow_412_GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataOut": "_dialogflow_413_GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn": "_dialogflow_414_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut": "_dialogflow_415_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn": "_dialogflow_416_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut": "_dialogflow_417_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn": "_dialogflow_418_GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut": "_dialogflow_419_GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCardIn": "_dialogflow_420_GoogleCloudDialogflowV2beta1IntentMessageCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCardOut": "_dialogflow_421_GoogleCloudDialogflowV2beta1IntentMessageCardOut",
        "GoogleCloudDialogflowCxV3ListIntentsResponseIn": "_dialogflow_422_GoogleCloudDialogflowCxV3ListIntentsResponseIn",
        "GoogleCloudDialogflowCxV3ListIntentsResponseOut": "_dialogflow_423_GoogleCloudDialogflowCxV3ListIntentsResponseOut",
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn": "_dialogflow_424_GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut": "_dialogflow_425_GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn": "_dialogflow_426_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut": "_dialogflow_427_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut",
        "GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn": "_dialogflow_428_GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn",
        "GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut": "_dialogflow_429_GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn": "_dialogflow_430_GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut": "_dialogflow_431_GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut",
        "GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataIn": "_dialogflow_432_GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataOut": "_dialogflow_433_GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesResponseIn": "_dialogflow_434_GoogleCloudDialogflowCxV3BatchRunTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesResponseOut": "_dialogflow_435_GoogleCloudDialogflowCxV3BatchRunTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseIn": "_dialogflow_436_GoogleCloudDialogflowCxV3beta1WebhookResponseIn",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseOut": "_dialogflow_437_GoogleCloudDialogflowCxV3beta1WebhookResponseOut",
        "GoogleCloudDialogflowV2WebhookRequestIn": "_dialogflow_438_GoogleCloudDialogflowV2WebhookRequestIn",
        "GoogleCloudDialogflowV2WebhookRequestOut": "_dialogflow_439_GoogleCloudDialogflowV2WebhookRequestOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn": "_dialogflow_440_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut": "_dialogflow_441_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut",
        "GoogleCloudDialogflowV2beta1SentimentIn": "_dialogflow_442_GoogleCloudDialogflowV2beta1SentimentIn",
        "GoogleCloudDialogflowV2beta1SentimentOut": "_dialogflow_443_GoogleCloudDialogflowV2beta1SentimentOut",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn": "_dialogflow_444_GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut": "_dialogflow_445_GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut",
        "GoogleCloudDialogflowCxV3beta1SessionInfoIn": "_dialogflow_446_GoogleCloudDialogflowCxV3beta1SessionInfoIn",
        "GoogleCloudDialogflowCxV3beta1SessionInfoOut": "_dialogflow_447_GoogleCloudDialogflowCxV3beta1SessionInfoOut",
        "GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseIn": "_dialogflow_448_GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseIn",
        "GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseOut": "_dialogflow_449_GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseOut",
        "GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataIn": "_dialogflow_450_GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataOut": "_dialogflow_451_GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_452_GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_453_GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1ConversationEventIn": "_dialogflow_454_GoogleCloudDialogflowV2beta1ConversationEventIn",
        "GoogleCloudDialogflowV2beta1ConversationEventOut": "_dialogflow_455_GoogleCloudDialogflowV2beta1ConversationEventOut",
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn": "_dialogflow_456_GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut": "_dialogflow_457_GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut",
        "GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseIn": "_dialogflow_458_GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseIn",
        "GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseOut": "_dialogflow_459_GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseOut",
        "GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn": "_dialogflow_460_GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut": "_dialogflow_461_GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesResponseIn": "_dialogflow_462_GoogleCloudDialogflowCxV3ImportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesResponseOut": "_dialogflow_463_GoogleCloudDialogflowCxV3ImportTestCasesResponseOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardIn": "_dialogflow_464_GoogleCloudDialogflowV2IntentMessageTableCardIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardOut": "_dialogflow_465_GoogleCloudDialogflowV2IntentMessageTableCardOut",
        "GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn": "_dialogflow_466_GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut": "_dialogflow_467_GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut",
        "GoogleCloudDialogflowCxV3InputAudioConfigIn": "_dialogflow_468_GoogleCloudDialogflowCxV3InputAudioConfigIn",
        "GoogleCloudDialogflowCxV3InputAudioConfigOut": "_dialogflow_469_GoogleCloudDialogflowCxV3InputAudioConfigOut",
        "GoogleCloudDialogflowCxV3CompareVersionsRequestIn": "_dialogflow_470_GoogleCloudDialogflowCxV3CompareVersionsRequestIn",
        "GoogleCloudDialogflowCxV3CompareVersionsRequestOut": "_dialogflow_471_GoogleCloudDialogflowCxV3CompareVersionsRequestOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn": "_dialogflow_472_GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut": "_dialogflow_473_GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn": "_dialogflow_474_GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn",
        "GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut": "_dialogflow_475_GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut",
        "GoogleCloudDialogflowCxV3QueryInputIn": "_dialogflow_476_GoogleCloudDialogflowCxV3QueryInputIn",
        "GoogleCloudDialogflowCxV3QueryInputOut": "_dialogflow_477_GoogleCloudDialogflowCxV3QueryInputOut",
        "GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataIn": "_dialogflow_478_GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataOut": "_dialogflow_479_GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1DeployFlowMetadataIn": "_dialogflow_480_GoogleCloudDialogflowCxV3beta1DeployFlowMetadataIn",
        "GoogleCloudDialogflowCxV3beta1DeployFlowMetadataOut": "_dialogflow_481_GoogleCloudDialogflowCxV3beta1DeployFlowMetadataOut",
        "GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn": "_dialogflow_482_GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn",
        "GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut": "_dialogflow_483_GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut",
        "GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn": "_dialogflow_484_GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn",
        "GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut": "_dialogflow_485_GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut",
        "GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn": "_dialogflow_486_GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn",
        "GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut": "_dialogflow_487_GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut",
        "GoogleCloudDialogflowCxV3IntentCoverageIntentIn": "_dialogflow_488_GoogleCloudDialogflowCxV3IntentCoverageIntentIn",
        "GoogleCloudDialogflowCxV3IntentCoverageIntentOut": "_dialogflow_489_GoogleCloudDialogflowCxV3IntentCoverageIntentOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIn": "_dialogflow_490_GoogleCloudDialogflowCxV3WebhookRequestIn",
        "GoogleCloudDialogflowCxV3WebhookRequestOut": "_dialogflow_491_GoogleCloudDialogflowCxV3WebhookRequestOut",
        "GoogleCloudDialogflowCxV3EntityTypeEntityIn": "_dialogflow_492_GoogleCloudDialogflowCxV3EntityTypeEntityIn",
        "GoogleCloudDialogflowCxV3EntityTypeEntityOut": "_dialogflow_493_GoogleCloudDialogflowCxV3EntityTypeEntityOut",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn": "_dialogflow_494_GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut": "_dialogflow_495_GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn": "_dialogflow_496_GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut": "_dialogflow_497_GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowV2beta1SessionEntityTypeIn": "_dialogflow_498_GoogleCloudDialogflowV2beta1SessionEntityTypeIn",
        "GoogleCloudDialogflowV2beta1SessionEntityTypeOut": "_dialogflow_499_GoogleCloudDialogflowV2beta1SessionEntityTypeOut",
        "GoogleCloudDialogflowV2AnnotatedMessagePartIn": "_dialogflow_500_GoogleCloudDialogflowV2AnnotatedMessagePartIn",
        "GoogleCloudDialogflowV2AnnotatedMessagePartOut": "_dialogflow_501_GoogleCloudDialogflowV2AnnotatedMessagePartOut",
        "GoogleCloudDialogflowCxV3ListChangelogsResponseIn": "_dialogflow_502_GoogleCloudDialogflowCxV3ListChangelogsResponseIn",
        "GoogleCloudDialogflowCxV3ListChangelogsResponseOut": "_dialogflow_503_GoogleCloudDialogflowCxV3ListChangelogsResponseOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn": "_dialogflow_504_GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut": "_dialogflow_505_GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn": "_dialogflow_506_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut": "_dialogflow_507_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestMetadataIn": "_dialogflow_508_GoogleCloudDialogflowCxV3RunContinuousTestMetadataIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestMetadataOut": "_dialogflow_509_GoogleCloudDialogflowCxV3RunContinuousTestMetadataOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn": "_dialogflow_510_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut": "_dialogflow_511_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut",
        "GoogleCloudDialogflowV2IntentTrainingPhraseIn": "_dialogflow_512_GoogleCloudDialogflowV2IntentTrainingPhraseIn",
        "GoogleCloudDialogflowV2IntentTrainingPhraseOut": "_dialogflow_513_GoogleCloudDialogflowV2IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn": "_dialogflow_514_GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut": "_dialogflow_515_GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut",
        "GoogleCloudDialogflowCxV3TestRunDifferenceIn": "_dialogflow_516_GoogleCloudDialogflowCxV3TestRunDifferenceIn",
        "GoogleCloudDialogflowCxV3TestRunDifferenceOut": "_dialogflow_517_GoogleCloudDialogflowCxV3TestRunDifferenceOut",
        "GoogleCloudDialogflowV2EntityTypeIn": "_dialogflow_518_GoogleCloudDialogflowV2EntityTypeIn",
        "GoogleCloudDialogflowV2EntityTypeOut": "_dialogflow_519_GoogleCloudDialogflowV2EntityTypeOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn": "_dialogflow_520_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut": "_dialogflow_521_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut",
        "GoogleCloudDialogflowV2beta1WebhookRequestIn": "_dialogflow_522_GoogleCloudDialogflowV2beta1WebhookRequestIn",
        "GoogleCloudDialogflowV2beta1WebhookRequestOut": "_dialogflow_523_GoogleCloudDialogflowV2beta1WebhookRequestOut",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioIn": "_dialogflow_524_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioIn",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut": "_dialogflow_525_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseResultIn": "_dialogflow_526_GoogleCloudDialogflowCxV3beta1TestCaseResultIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseResultOut": "_dialogflow_527_GoogleCloudDialogflowCxV3beta1TestCaseResultOut",
        "GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataIn": "_dialogflow_528_GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut": "_dialogflow_529_GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn": "_dialogflow_530_GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut": "_dialogflow_531_GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ListPagesResponseIn": "_dialogflow_532_GoogleCloudDialogflowCxV3ListPagesResponseIn",
        "GoogleCloudDialogflowCxV3ListPagesResponseOut": "_dialogflow_533_GoogleCloudDialogflowCxV3ListPagesResponseOut",
        "GoogleCloudDialogflowV2ImportDocumentsResponseIn": "_dialogflow_534_GoogleCloudDialogflowV2ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV2ImportDocumentsResponseOut": "_dialogflow_535_GoogleCloudDialogflowV2ImportDocumentsResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn": "_dialogflow_536_GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut": "_dialogflow_537_GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut",
        "GoogleCloudDialogflowCxV3IntentInputIn": "_dialogflow_538_GoogleCloudDialogflowCxV3IntentInputIn",
        "GoogleCloudDialogflowCxV3IntentInputOut": "_dialogflow_539_GoogleCloudDialogflowCxV3IntentInputOut",
        "GoogleCloudDialogflowCxV3VersionVariantsIn": "_dialogflow_540_GoogleCloudDialogflowCxV3VersionVariantsIn",
        "GoogleCloudDialogflowCxV3VersionVariantsOut": "_dialogflow_541_GoogleCloudDialogflowCxV3VersionVariantsOut",
        "GoogleCloudDialogflowCxV3EventHandlerIn": "_dialogflow_542_GoogleCloudDialogflowCxV3EventHandlerIn",
        "GoogleCloudDialogflowCxV3EventHandlerOut": "_dialogflow_543_GoogleCloudDialogflowCxV3EventHandlerOut",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn": "_dialogflow_544_GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut": "_dialogflow_545_GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataIn": "_dialogflow_546_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataOut": "_dialogflow_547_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn": "_dialogflow_548_GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut": "_dialogflow_549_GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut",
        "GoogleCloudDialogflowV2SessionEntityTypeIn": "_dialogflow_550_GoogleCloudDialogflowV2SessionEntityTypeIn",
        "GoogleCloudDialogflowV2SessionEntityTypeOut": "_dialogflow_551_GoogleCloudDialogflowV2SessionEntityTypeOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentIn": "_dialogflow_552_GoogleCloudDialogflowCxV3beta1FulfillmentIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentOut": "_dialogflow_553_GoogleCloudDialogflowCxV3beta1FulfillmentOut",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn": "_dialogflow_554_GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut": "_dialogflow_555_GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut",
        "GoogleCloudDialogflowV2beta1WebhookResponseIn": "_dialogflow_556_GoogleCloudDialogflowV2beta1WebhookResponseIn",
        "GoogleCloudDialogflowV2beta1WebhookResponseOut": "_dialogflow_557_GoogleCloudDialogflowV2beta1WebhookResponseOut",
        "GoogleCloudDialogflowV2beta1ContextIn": "_dialogflow_558_GoogleCloudDialogflowV2beta1ContextIn",
        "GoogleCloudDialogflowV2beta1ContextOut": "_dialogflow_559_GoogleCloudDialogflowV2beta1ContextOut",
        "GoogleProtobufEmptyIn": "_dialogflow_560_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_dialogflow_561_GoogleProtobufEmptyOut",
        "GoogleCloudDialogflowCxV3beta1TransitionRouteIn": "_dialogflow_562_GoogleCloudDialogflowCxV3beta1TransitionRouteIn",
        "GoogleCloudDialogflowCxV3beta1TransitionRouteOut": "_dialogflow_563_GoogleCloudDialogflowCxV3beta1TransitionRouteOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn": "_dialogflow_564_GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut": "_dialogflow_565_GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut",
        "GoogleCloudDialogflowCxV3ExperimentResultMetricIn": "_dialogflow_566_GoogleCloudDialogflowCxV3ExperimentResultMetricIn",
        "GoogleCloudDialogflowCxV3ExperimentResultMetricOut": "_dialogflow_567_GoogleCloudDialogflowCxV3ExperimentResultMetricOut",
        "GoogleCloudDialogflowV2ExportAgentResponseIn": "_dialogflow_568_GoogleCloudDialogflowV2ExportAgentResponseIn",
        "GoogleCloudDialogflowV2ExportAgentResponseOut": "_dialogflow_569_GoogleCloudDialogflowV2ExportAgentResponseOut",
        "GoogleCloudDialogflowV2IntentMessageIn": "_dialogflow_570_GoogleCloudDialogflowV2IntentMessageIn",
        "GoogleCloudDialogflowV2IntentMessageOut": "_dialogflow_571_GoogleCloudDialogflowV2IntentMessageOut",
        "GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn": "_dialogflow_572_GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut": "_dialogflow_573_GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn": "_dialogflow_574_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut": "_dialogflow_575_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut",
        "GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn": "_dialogflow_576_GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn",
        "GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut": "_dialogflow_577_GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTextIn": "_dialogflow_578_GoogleCloudDialogflowV2beta1IntentMessageTextIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTextOut": "_dialogflow_579_GoogleCloudDialogflowV2beta1IntentMessageTextOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn": "_dialogflow_580_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut": "_dialogflow_581_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsIn": "_dialogflow_582_GoogleCloudDialogflowCxV3SecuritySettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsOut": "_dialogflow_583_GoogleCloudDialogflowCxV3SecuritySettingsOut",
        "GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn": "_dialogflow_584_GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn",
        "GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut": "_dialogflow_585_GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut",
        "GoogleCloudDialogflowCxV3ListEntityTypesResponseIn": "_dialogflow_586_GoogleCloudDialogflowCxV3ListEntityTypesResponseIn",
        "GoogleCloudDialogflowCxV3ListEntityTypesResponseOut": "_dialogflow_587_GoogleCloudDialogflowCxV3ListEntityTypesResponseOut",
        "GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataIn": "_dialogflow_588_GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataOut": "_dialogflow_589_GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2ConversationModelIn": "_dialogflow_590_GoogleCloudDialogflowV2ConversationModelIn",
        "GoogleCloudDialogflowV2ConversationModelOut": "_dialogflow_591_GoogleCloudDialogflowV2ConversationModelOut",
        "GoogleCloudDialogflowCxV3DetectIntentRequestIn": "_dialogflow_592_GoogleCloudDialogflowCxV3DetectIntentRequestIn",
        "GoogleCloudDialogflowCxV3DetectIntentRequestOut": "_dialogflow_593_GoogleCloudDialogflowCxV3DetectIntentRequestOut",
        "GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn": "_dialogflow_594_GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn",
        "GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut": "_dialogflow_595_GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut",
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_596_GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_597_GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn": "_dialogflow_598_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut": "_dialogflow_599_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut",
        "GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn": "_dialogflow_600_GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn",
        "GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut": "_dialogflow_601_GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut",
        "GoogleCloudDialogflowCxV3EnvironmentIn": "_dialogflow_602_GoogleCloudDialogflowCxV3EnvironmentIn",
        "GoogleCloudDialogflowCxV3EnvironmentOut": "_dialogflow_603_GoogleCloudDialogflowCxV3EnvironmentOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoIn": "_dialogflow_604_GoogleCloudDialogflowCxV3beta1PageInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoOut": "_dialogflow_605_GoogleCloudDialogflowCxV3beta1PageInfoOut",
        "GoogleCloudDialogflowCxV3beta1TurnSignalsIn": "_dialogflow_606_GoogleCloudDialogflowCxV3beta1TurnSignalsIn",
        "GoogleCloudDialogflowCxV3beta1TurnSignalsOut": "_dialogflow_607_GoogleCloudDialogflowCxV3beta1TurnSignalsOut",
        "GoogleCloudDialogflowV2OriginalDetectIntentRequestIn": "_dialogflow_608_GoogleCloudDialogflowV2OriginalDetectIntentRequestIn",
        "GoogleCloudDialogflowV2OriginalDetectIntentRequestOut": "_dialogflow_609_GoogleCloudDialogflowV2OriginalDetectIntentRequestOut",
        "GoogleCloudDialogflowV2ArticleAnswerIn": "_dialogflow_610_GoogleCloudDialogflowV2ArticleAnswerIn",
        "GoogleCloudDialogflowV2ArticleAnswerOut": "_dialogflow_611_GoogleCloudDialogflowV2ArticleAnswerOut",
        "GoogleCloudDialogflowV2beta1DialogflowAssistAnswerIn": "_dialogflow_612_GoogleCloudDialogflowV2beta1DialogflowAssistAnswerIn",
        "GoogleCloudDialogflowV2beta1DialogflowAssistAnswerOut": "_dialogflow_613_GoogleCloudDialogflowV2beta1DialogflowAssistAnswerOut",
        "GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn": "_dialogflow_614_GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn",
        "GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut": "_dialogflow_615_GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut",
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn": "_dialogflow_616_GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut": "_dialogflow_617_GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn": "_dialogflow_618_GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut": "_dialogflow_619_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn": "_dialogflow_620_GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut": "_dialogflow_621_GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowCxV3beta1FormIn": "_dialogflow_622_GoogleCloudDialogflowCxV3beta1FormIn",
        "GoogleCloudDialogflowCxV3beta1FormOut": "_dialogflow_623_GoogleCloudDialogflowCxV3beta1FormOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn": "_dialogflow_624_GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut": "_dialogflow_625_GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn": "_dialogflow_626_GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut": "_dialogflow_627_GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut",
        "GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn": "_dialogflow_628_GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn",
        "GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut": "_dialogflow_629_GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut",
        "GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn": "_dialogflow_630_GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn",
        "GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut": "_dialogflow_631_GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardCellIn": "_dialogflow_632_GoogleCloudDialogflowV2IntentMessageTableCardCellIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardCellOut": "_dialogflow_633_GoogleCloudDialogflowV2IntentMessageTableCardCellOut",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersIn": "_dialogflow_634_GoogleCloudDialogflowV2beta1KnowledgeAnswersIn",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersOut": "_dialogflow_635_GoogleCloudDialogflowV2beta1KnowledgeAnswersOut",
        "GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn": "_dialogflow_636_GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn",
        "GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut": "_dialogflow_637_GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut",
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn": "_dialogflow_638_GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn",
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut": "_dialogflow_639_GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut",
        "GoogleCloudDialogflowV2MessageIn": "_dialogflow_640_GoogleCloudDialogflowV2MessageIn",
        "GoogleCloudDialogflowV2MessageOut": "_dialogflow_641_GoogleCloudDialogflowV2MessageOut",
        "GoogleCloudDialogflowCxV3CalculateCoverageResponseIn": "_dialogflow_642_GoogleCloudDialogflowCxV3CalculateCoverageResponseIn",
        "GoogleCloudDialogflowCxV3CalculateCoverageResponseOut": "_dialogflow_643_GoogleCloudDialogflowCxV3CalculateCoverageResponseOut",
        "GoogleCloudDialogflowCxV3VersionIn": "_dialogflow_644_GoogleCloudDialogflowCxV3VersionIn",
        "GoogleCloudDialogflowCxV3VersionOut": "_dialogflow_645_GoogleCloudDialogflowCxV3VersionOut",
        "GoogleCloudDialogflowCxV3GcsDestinationIn": "_dialogflow_646_GoogleCloudDialogflowCxV3GcsDestinationIn",
        "GoogleCloudDialogflowCxV3GcsDestinationOut": "_dialogflow_647_GoogleCloudDialogflowCxV3GcsDestinationOut",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponseIn": "_dialogflow_648_GoogleCloudDialogflowV2IntentMessageSimpleResponseIn",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponseOut": "_dialogflow_649_GoogleCloudDialogflowV2IntentMessageSimpleResponseOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn": "_dialogflow_650_GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut": "_dialogflow_651_GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn": "_dialogflow_652_GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut": "_dialogflow_653_GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn": "_dialogflow_654_GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut": "_dialogflow_655_GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn": "_dialogflow_656_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut": "_dialogflow_657_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseResponseIn": "_dialogflow_658_GoogleCloudDialogflowCxV3beta1RunTestCaseResponseIn",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseResponseOut": "_dialogflow_659_GoogleCloudDialogflowCxV3beta1RunTestCaseResponseOut",
        "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn": "_dialogflow_660_GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn",
        "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut": "_dialogflow_661_GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut",
        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn": "_dialogflow_662_GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut": "_dialogflow_663_GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut",
        "GoogleCloudDialogflowV2beta1EntityTypeEntityIn": "_dialogflow_664_GoogleCloudDialogflowV2beta1EntityTypeEntityIn",
        "GoogleCloudDialogflowV2beta1EntityTypeEntityOut": "_dialogflow_665_GoogleCloudDialogflowV2beta1EntityTypeEntityOut",
        "GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn": "_dialogflow_666_GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut": "_dialogflow_667_GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut",
        "GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataIn": "_dialogflow_668_GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataOut": "_dialogflow_669_GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1WebhookIn": "_dialogflow_670_GoogleCloudDialogflowCxV3beta1WebhookIn",
        "GoogleCloudDialogflowCxV3beta1WebhookOut": "_dialogflow_671_GoogleCloudDialogflowCxV3beta1WebhookOut",
        "GoogleCloudDialogflowCxV3ChangelogIn": "_dialogflow_672_GoogleCloudDialogflowCxV3ChangelogIn",
        "GoogleCloudDialogflowCxV3ChangelogOut": "_dialogflow_673_GoogleCloudDialogflowCxV3ChangelogOut",
        "GoogleCloudDialogflowV2ConversationEventIn": "_dialogflow_674_GoogleCloudDialogflowV2ConversationEventIn",
        "GoogleCloudDialogflowV2ConversationEventOut": "_dialogflow_675_GoogleCloudDialogflowV2ConversationEventOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn": "_dialogflow_676_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut": "_dialogflow_677_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut",
        "GoogleCloudDialogflowCxV3OutputAudioConfigIn": "_dialogflow_678_GoogleCloudDialogflowCxV3OutputAudioConfigIn",
        "GoogleCloudDialogflowCxV3OutputAudioConfigOut": "_dialogflow_679_GoogleCloudDialogflowCxV3OutputAudioConfigOut",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn": "_dialogflow_680_GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut": "_dialogflow_681_GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut",
        "GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn": "_dialogflow_682_GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn",
        "GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut": "_dialogflow_683_GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut",
        "GoogleCloudDialogflowV2IntentMessageSuggestionsIn": "_dialogflow_684_GoogleCloudDialogflowV2IntentMessageSuggestionsIn",
        "GoogleCloudDialogflowV2IntentMessageSuggestionsOut": "_dialogflow_685_GoogleCloudDialogflowV2IntentMessageSuggestionsOut",
        "GoogleCloudDialogflowCxV3ValidationMessageIn": "_dialogflow_686_GoogleCloudDialogflowCxV3ValidationMessageIn",
        "GoogleCloudDialogflowCxV3ValidationMessageOut": "_dialogflow_687_GoogleCloudDialogflowCxV3ValidationMessageOut",
        "GoogleCloudDialogflowCxV3MatchIn": "_dialogflow_688_GoogleCloudDialogflowCxV3MatchIn",
        "GoogleCloudDialogflowCxV3MatchOut": "_dialogflow_689_GoogleCloudDialogflowCxV3MatchOut",
        "GoogleCloudDialogflowCxV3LoadVersionRequestIn": "_dialogflow_690_GoogleCloudDialogflowCxV3LoadVersionRequestIn",
        "GoogleCloudDialogflowCxV3LoadVersionRequestOut": "_dialogflow_691_GoogleCloudDialogflowCxV3LoadVersionRequestOut",
        "GoogleCloudDialogflowCxV3RolloutConfigIn": "_dialogflow_692_GoogleCloudDialogflowCxV3RolloutConfigIn",
        "GoogleCloudDialogflowCxV3RolloutConfigOut": "_dialogflow_693_GoogleCloudDialogflowCxV3RolloutConfigOut",
        "GoogleCloudDialogflowCxV3ListFlowsResponseIn": "_dialogflow_694_GoogleCloudDialogflowCxV3ListFlowsResponseIn",
        "GoogleCloudDialogflowCxV3ListFlowsResponseOut": "_dialogflow_695_GoogleCloudDialogflowCxV3ListFlowsResponseOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestRequestIn": "_dialogflow_696_GoogleCloudDialogflowCxV3RunContinuousTestRequestIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestRequestOut": "_dialogflow_697_GoogleCloudDialogflowCxV3RunContinuousTestRequestOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn": "_dialogflow_698_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut": "_dialogflow_699_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut",
        "GoogleCloudDialogflowV2ContextIn": "_dialogflow_700_GoogleCloudDialogflowV2ContextIn",
        "GoogleCloudDialogflowV2ContextOut": "_dialogflow_701_GoogleCloudDialogflowV2ContextOut",
        "GoogleCloudDialogflowCxV3TextInputIn": "_dialogflow_702_GoogleCloudDialogflowCxV3TextInputIn",
        "GoogleCloudDialogflowCxV3TextInputOut": "_dialogflow_703_GoogleCloudDialogflowCxV3TextInputOut",
        "GoogleCloudDialogflowCxV3ImportFlowResponseIn": "_dialogflow_704_GoogleCloudDialogflowCxV3ImportFlowResponseIn",
        "GoogleCloudDialogflowCxV3ImportFlowResponseOut": "_dialogflow_705_GoogleCloudDialogflowCxV3ImportFlowResponseOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentIn": "_dialogflow_706_GoogleCloudDialogflowCxV3beta1EnvironmentIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentOut": "_dialogflow_707_GoogleCloudDialogflowCxV3beta1EnvironmentOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn": "_dialogflow_708_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut": "_dialogflow_709_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn": "_dialogflow_710_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut": "_dialogflow_711_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataIn": "_dialogflow_712_GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataOut": "_dialogflow_713_GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ListAgentsResponseIn": "_dialogflow_714_GoogleCloudDialogflowCxV3ListAgentsResponseIn",
        "GoogleCloudDialogflowCxV3ListAgentsResponseOut": "_dialogflow_715_GoogleCloudDialogflowCxV3ListAgentsResponseOut",
        "GoogleCloudDialogflowV2IntentMessageImageIn": "_dialogflow_716_GoogleCloudDialogflowV2IntentMessageImageIn",
        "GoogleCloudDialogflowV2IntentMessageImageOut": "_dialogflow_717_GoogleCloudDialogflowV2IntentMessageImageOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn": "_dialogflow_718_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut": "_dialogflow_719_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut",
        "GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn": "_dialogflow_720_GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn",
        "GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut": "_dialogflow_721_GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut",
        "GoogleCloudDialogflowCxV3SpeechToTextSettingsIn": "_dialogflow_722_GoogleCloudDialogflowCxV3SpeechToTextSettingsIn",
        "GoogleCloudDialogflowCxV3SpeechToTextSettingsOut": "_dialogflow_723_GoogleCloudDialogflowCxV3SpeechToTextSettingsOut",
        "GoogleCloudDialogflowCxV3beta1TestConfigIn": "_dialogflow_724_GoogleCloudDialogflowCxV3beta1TestConfigIn",
        "GoogleCloudDialogflowCxV3beta1TestConfigOut": "_dialogflow_725_GoogleCloudDialogflowCxV3beta1TestConfigOut",
        "GoogleCloudDialogflowCxV3AudioInputIn": "_dialogflow_726_GoogleCloudDialogflowCxV3AudioInputIn",
        "GoogleCloudDialogflowCxV3AudioInputOut": "_dialogflow_727_GoogleCloudDialogflowCxV3AudioInputOut",
        "GoogleCloudDialogflowV2IntentMessageListSelectItemIn": "_dialogflow_728_GoogleCloudDialogflowV2IntentMessageListSelectItemIn",
        "GoogleCloudDialogflowV2IntentMessageListSelectItemOut": "_dialogflow_729_GoogleCloudDialogflowV2IntentMessageListSelectItemOut",
        "GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn": "_dialogflow_730_GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn",
        "GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut": "_dialogflow_731_GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut",
        "GoogleCloudDialogflowCxV3WebhookIn": "_dialogflow_732_GoogleCloudDialogflowCxV3WebhookIn",
        "GoogleCloudDialogflowCxV3WebhookOut": "_dialogflow_733_GoogleCloudDialogflowCxV3WebhookOut",
        "GoogleLongrunningListOperationsResponseIn": "_dialogflow_734_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_dialogflow_735_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn": "_dialogflow_736_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut": "_dialogflow_737_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn": "_dialogflow_738_GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut": "_dialogflow_739_GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnIn": "_dialogflow_740_GoogleCloudDialogflowCxV3beta1ConversationTurnIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnOut": "_dialogflow_741_GoogleCloudDialogflowCxV3beta1ConversationTurnOut",
        "GoogleCloudDialogflowCxV3ResponseMessageIn": "_dialogflow_742_GoogleCloudDialogflowCxV3ResponseMessageIn",
        "GoogleCloudDialogflowCxV3ResponseMessageOut": "_dialogflow_743_GoogleCloudDialogflowCxV3ResponseMessageOut",
        "GoogleCloudDialogflowV3alpha1TurnSignalsIn": "_dialogflow_744_GoogleCloudDialogflowV3alpha1TurnSignalsIn",
        "GoogleCloudDialogflowV3alpha1TurnSignalsOut": "_dialogflow_745_GoogleCloudDialogflowV3alpha1TurnSignalsOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn": "_dialogflow_746_GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut": "_dialogflow_747_GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut",
        "GoogleCloudDialogflowV2IntentMessageCardButtonIn": "_dialogflow_748_GoogleCloudDialogflowV2IntentMessageCardButtonIn",
        "GoogleCloudDialogflowV2IntentMessageCardButtonOut": "_dialogflow_749_GoogleCloudDialogflowV2IntentMessageCardButtonOut",
        "GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn": "_dialogflow_750_GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn",
        "GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut": "_dialogflow_751_GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut",
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_752_GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_753_GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn": "_dialogflow_754_GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn",
        "GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut": "_dialogflow_755_GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioIn": "_dialogflow_756_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut": "_dialogflow_757_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut",
        "GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn": "_dialogflow_758_GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut": "_dialogflow_759_GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut",
        "GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn": "_dialogflow_760_GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn",
        "GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut": "_dialogflow_761_GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn": "_dialogflow_762_GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut": "_dialogflow_763_GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut",
        "GoogleCloudDialogflowCxV3ExportAgentResponseIn": "_dialogflow_764_GoogleCloudDialogflowCxV3ExportAgentResponseIn",
        "GoogleCloudDialogflowCxV3ExportAgentResponseOut": "_dialogflow_765_GoogleCloudDialogflowCxV3ExportAgentResponseOut",
        "GoogleCloudDialogflowV2beta1IntentIn": "_dialogflow_766_GoogleCloudDialogflowV2beta1IntentIn",
        "GoogleCloudDialogflowV2beta1IntentOut": "_dialogflow_767_GoogleCloudDialogflowV2beta1IntentOut",
        "GoogleCloudDialogflowCxV3ExportAgentRequestIn": "_dialogflow_768_GoogleCloudDialogflowCxV3ExportAgentRequestIn",
        "GoogleCloudDialogflowCxV3ExportAgentRequestOut": "_dialogflow_769_GoogleCloudDialogflowCxV3ExportAgentRequestOut",
        "GoogleCloudDialogflowV2SmartReplyAnswerIn": "_dialogflow_770_GoogleCloudDialogflowV2SmartReplyAnswerIn",
        "GoogleCloudDialogflowV2SmartReplyAnswerOut": "_dialogflow_771_GoogleCloudDialogflowV2SmartReplyAnswerOut",
        "GoogleCloudDialogflowCxV3ImportDocumentsResponseIn": "_dialogflow_772_GoogleCloudDialogflowCxV3ImportDocumentsResponseIn",
        "GoogleCloudDialogflowCxV3ImportDocumentsResponseOut": "_dialogflow_773_GoogleCloudDialogflowCxV3ImportDocumentsResponseOut",
        "GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataIn": "_dialogflow_774_GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataOut": "_dialogflow_775_GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ListSecuritySettingsResponseIn": "_dialogflow_776_GoogleCloudDialogflowCxV3ListSecuritySettingsResponseIn",
        "GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut": "_dialogflow_777_GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesRequestIn": "_dialogflow_778_GoogleCloudDialogflowCxV3ExportTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesRequestOut": "_dialogflow_779_GoogleCloudDialogflowCxV3ExportTestCasesRequestOut",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn": "_dialogflow_780_GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut": "_dialogflow_781_GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn": "_dialogflow_782_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut": "_dialogflow_783_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut",
        "GoogleCloudDialogflowV2SmartReplyModelMetadataIn": "_dialogflow_784_GoogleCloudDialogflowV2SmartReplyModelMetadataIn",
        "GoogleCloudDialogflowV2SmartReplyModelMetadataOut": "_dialogflow_785_GoogleCloudDialogflowV2SmartReplyModelMetadataOut",
        "GoogleCloudDialogflowCxV3ExperimentIn": "_dialogflow_786_GoogleCloudDialogflowCxV3ExperimentIn",
        "GoogleCloudDialogflowCxV3ExperimentOut": "_dialogflow_787_GoogleCloudDialogflowCxV3ExperimentOut",
        "GoogleCloudDialogflowCxV3EntityTypeIn": "_dialogflow_788_GoogleCloudDialogflowCxV3EntityTypeIn",
        "GoogleCloudDialogflowCxV3EntityTypeOut": "_dialogflow_789_GoogleCloudDialogflowCxV3EntityTypeOut",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataIn": "_dialogflow_790_GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataIn",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataOut": "_dialogflow_791_GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseErrorIn": "_dialogflow_792_GoogleCloudDialogflowCxV3beta1TestCaseErrorIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseErrorOut": "_dialogflow_793_GoogleCloudDialogflowCxV3beta1TestCaseErrorOut",
        "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn": "_dialogflow_794_GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut": "_dialogflow_795_GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3DtmfInputIn": "_dialogflow_796_GoogleCloudDialogflowCxV3DtmfInputIn",
        "GoogleCloudDialogflowCxV3DtmfInputOut": "_dialogflow_797_GoogleCloudDialogflowCxV3DtmfInputOut",
        "GoogleCloudDialogflowCxV3VoiceSelectionParamsIn": "_dialogflow_798_GoogleCloudDialogflowCxV3VoiceSelectionParamsIn",
        "GoogleCloudDialogflowCxV3VoiceSelectionParamsOut": "_dialogflow_799_GoogleCloudDialogflowCxV3VoiceSelectionParamsOut",
        "GoogleCloudDialogflowV2beta1ExportOperationMetadataIn": "_dialogflow_800_GoogleCloudDialogflowV2beta1ExportOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1ExportOperationMetadataOut": "_dialogflow_801_GoogleCloudDialogflowV2beta1ExportOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentParameterIn": "_dialogflow_802_GoogleCloudDialogflowV2beta1IntentParameterIn",
        "GoogleCloudDialogflowV2beta1IntentParameterOut": "_dialogflow_803_GoogleCloudDialogflowV2beta1IntentParameterOut",
        "GoogleCloudDialogflowV2beta1SmartReplyAnswerIn": "_dialogflow_804_GoogleCloudDialogflowV2beta1SmartReplyAnswerIn",
        "GoogleCloudDialogflowV2beta1SmartReplyAnswerOut": "_dialogflow_805_GoogleCloudDialogflowV2beta1SmartReplyAnswerOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseIn": "_dialogflow_806_GoogleCloudDialogflowCxV3beta1TestCaseIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseOut": "_dialogflow_807_GoogleCloudDialogflowCxV3beta1TestCaseOut",
        "GoogleCloudDialogflowV2beta1ArticleAnswerIn": "_dialogflow_808_GoogleCloudDialogflowV2beta1ArticleAnswerIn",
        "GoogleCloudDialogflowV2beta1ArticleAnswerOut": "_dialogflow_809_GoogleCloudDialogflowV2beta1ArticleAnswerOut",
        "GoogleCloudDialogflowV2beta1GcsDestinationIn": "_dialogflow_810_GoogleCloudDialogflowV2beta1GcsDestinationIn",
        "GoogleCloudDialogflowV2beta1GcsDestinationOut": "_dialogflow_811_GoogleCloudDialogflowV2beta1GcsDestinationOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn": "_dialogflow_812_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut": "_dialogflow_813_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut",
        "GoogleCloudDialogflowV2HumanAgentAssistantEventIn": "_dialogflow_814_GoogleCloudDialogflowV2HumanAgentAssistantEventIn",
        "GoogleCloudDialogflowV2HumanAgentAssistantEventOut": "_dialogflow_815_GoogleCloudDialogflowV2HumanAgentAssistantEventOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn": "_dialogflow_816_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut": "_dialogflow_817_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut",
        "GoogleCloudDialogflowCxV3FulfillmentIn": "_dialogflow_818_GoogleCloudDialogflowCxV3FulfillmentIn",
        "GoogleCloudDialogflowCxV3FulfillmentOut": "_dialogflow_819_GoogleCloudDialogflowCxV3FulfillmentOut",
        "GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn": "_dialogflow_820_GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn",
        "GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut": "_dialogflow_821_GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut",
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn": "_dialogflow_822_GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn",
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut": "_dialogflow_823_GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn": "_dialogflow_824_GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut": "_dialogflow_825_GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut",
        "GoogleCloudDialogflowCxV3RolloutStateIn": "_dialogflow_826_GoogleCloudDialogflowCxV3RolloutStateIn",
        "GoogleCloudDialogflowCxV3RolloutStateOut": "_dialogflow_827_GoogleCloudDialogflowCxV3RolloutStateOut",
        "GoogleCloudDialogflowCxV3beta1ConversationSignalsIn": "_dialogflow_828_GoogleCloudDialogflowCxV3beta1ConversationSignalsIn",
        "GoogleCloudDialogflowCxV3beta1ConversationSignalsOut": "_dialogflow_829_GoogleCloudDialogflowCxV3beta1ConversationSignalsOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn": "_dialogflow_830_GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut": "_dialogflow_831_GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn": "_dialogflow_832_GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn",
        "GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut": "_dialogflow_833_GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut",
        "GoogleCloudDialogflowV2IntentMessageSuggestionIn": "_dialogflow_834_GoogleCloudDialogflowV2IntentMessageSuggestionIn",
        "GoogleCloudDialogflowV2IntentMessageSuggestionOut": "_dialogflow_835_GoogleCloudDialogflowV2IntentMessageSuggestionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn": "_dialogflow_836_GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut": "_dialogflow_837_GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut",
        "GoogleCloudDialogflowV2beta1MessageIn": "_dialogflow_838_GoogleCloudDialogflowV2beta1MessageIn",
        "GoogleCloudDialogflowV2beta1MessageOut": "_dialogflow_839_GoogleCloudDialogflowV2beta1MessageOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn": "_dialogflow_840_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut": "_dialogflow_841_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn": "_dialogflow_842_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut": "_dialogflow_843_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut",
        "GoogleLongrunningOperationIn": "_dialogflow_844_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_dialogflow_845_GoogleLongrunningOperationOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn": "_dialogflow_846_GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut": "_dialogflow_847_GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut",
        "GoogleCloudDialogflowV2QueryResultIn": "_dialogflow_848_GoogleCloudDialogflowV2QueryResultIn",
        "GoogleCloudDialogflowV2QueryResultOut": "_dialogflow_849_GoogleCloudDialogflowV2QueryResultOut",
        "GoogleCloudDialogflowV2IntentFollowupIntentInfoIn": "_dialogflow_850_GoogleCloudDialogflowV2IntentFollowupIntentInfoIn",
        "GoogleCloudDialogflowV2IntentFollowupIntentInfoOut": "_dialogflow_851_GoogleCloudDialogflowV2IntentFollowupIntentInfoOut",
        "GoogleCloudLocationLocationIn": "_dialogflow_852_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_dialogflow_853_GoogleCloudLocationLocationOut",
        "GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn": "_dialogflow_854_GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn",
        "GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut": "_dialogflow_855_GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut",
        "GoogleCloudDialogflowCxV3beta1PageIn": "_dialogflow_856_GoogleCloudDialogflowCxV3beta1PageIn",
        "GoogleCloudDialogflowCxV3beta1PageOut": "_dialogflow_857_GoogleCloudDialogflowCxV3beta1PageOut",
        "GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn": "_dialogflow_858_GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn",
        "GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut": "_dialogflow_859_GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut",
        "GoogleCloudDialogflowCxV3beta1EventHandlerIn": "_dialogflow_860_GoogleCloudDialogflowCxV3beta1EventHandlerIn",
        "GoogleCloudDialogflowCxV3beta1EventHandlerOut": "_dialogflow_861_GoogleCloudDialogflowCxV3beta1EventHandlerOut",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn": "_dialogflow_862_GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut": "_dialogflow_863_GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn": "_dialogflow_864_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut": "_dialogflow_865_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut",
        "GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn": "_dialogflow_866_GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut": "_dialogflow_867_GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut",
        "GoogleCloudDialogflowCxV3ConversationTurnUserInputIn": "_dialogflow_868_GoogleCloudDialogflowCxV3ConversationTurnUserInputIn",
        "GoogleCloudDialogflowCxV3ConversationTurnUserInputOut": "_dialogflow_869_GoogleCloudDialogflowCxV3ConversationTurnUserInputOut",
        "GoogleCloudDialogflowV2beta1EventInputIn": "_dialogflow_870_GoogleCloudDialogflowV2beta1EventInputIn",
        "GoogleCloudDialogflowV2beta1EventInputOut": "_dialogflow_871_GoogleCloudDialogflowV2beta1EventInputOut",
        "GoogleCloudDialogflowCxV3beta1QueryInputIn": "_dialogflow_872_GoogleCloudDialogflowCxV3beta1QueryInputIn",
        "GoogleCloudDialogflowCxV3beta1QueryInputOut": "_dialogflow_873_GoogleCloudDialogflowCxV3beta1QueryInputOut",
        "GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataIn": "_dialogflow_874_GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataOut": "_dialogflow_875_GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3AgentIn": "_dialogflow_876_GoogleCloudDialogflowCxV3AgentIn",
        "GoogleCloudDialogflowCxV3AgentOut": "_dialogflow_877_GoogleCloudDialogflowCxV3AgentOut",
        "GoogleCloudDialogflowCxV3AgentValidationResultIn": "_dialogflow_878_GoogleCloudDialogflowCxV3AgentValidationResultIn",
        "GoogleCloudDialogflowCxV3AgentValidationResultOut": "_dialogflow_879_GoogleCloudDialogflowCxV3AgentValidationResultOut",
        "GoogleCloudDialogflowCxV3TestCaseResultIn": "_dialogflow_880_GoogleCloudDialogflowCxV3TestCaseResultIn",
        "GoogleCloudDialogflowCxV3TestCaseResultOut": "_dialogflow_881_GoogleCloudDialogflowCxV3TestCaseResultOut",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn": "_dialogflow_882_GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut": "_dialogflow_883_GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowV2IntentMessageMediaContentIn": "_dialogflow_884_GoogleCloudDialogflowV2IntentMessageMediaContentIn",
        "GoogleCloudDialogflowV2IntentMessageMediaContentOut": "_dialogflow_885_GoogleCloudDialogflowV2IntentMessageMediaContentOut",
        "GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn": "_dialogflow_886_GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn",
        "GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut": "_dialogflow_887_GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn"] = t.struct(
        {
            "enableStackdriverLogging": t.boolean().optional(),
            "enableInteractionLogging": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn"])
    types["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut"] = t.struct(
        {
            "enableStackdriverLogging": t.boolean().optional(),
            "enableInteractionLogging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut"])
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn"] = t.struct(
        {
            "coverageScore": t.number().optional(),
            "routeGroup": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"]
            ).optional(),
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
            "coverageScore": t.number().optional(),
            "routeGroup": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"]
            ).optional(),
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
    types["GoogleCloudDialogflowCxV3DeployFlowRequestIn"] = t.struct(
        {"flowVersion": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3DeployFlowRequestOut"] = t.struct(
        {
            "flowVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowRequestOut"])
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
    types["GoogleCloudDialogflowCxV3DeploymentIn"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3DeploymentResultIn"]
            ).optional(),
            "flowVersion": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentIn"])
    types["GoogleCloudDialogflowCxV3DeploymentOut"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3DeploymentResultOut"]
            ).optional(),
            "flowVersion": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentOut"])
    types["GoogleCloudDialogflowV2GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2GcsDestinationIn"])
    types["GoogleCloudDialogflowV2GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2GcsDestinationOut"])
    types["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"] = t.struct(
        {
            "id": t.string().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn"])
            ),
            "repeatCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowCxV3IntentTrainingPhraseOut"] = t.struct(
        {
            "id": t.string().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut"])
            ),
            "repeatCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseOut"])
    types["GoogleCloudDialogflowCxV3CompareVersionsResponseIn"] = t.struct(
        {
            "compareTime": t.string().optional(),
            "baseVersionContentJson": t.string().optional(),
            "targetVersionContentJson": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseIn"])
    types["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"] = t.struct(
        {
            "compareTime": t.string().optional(),
            "baseVersionContentJson": t.string().optional(),
            "targetVersionContentJson": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1FormParameterIn"] = t.struct(
        {
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "redact": t.boolean().optional(),
            "required": t.boolean().optional(),
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
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "redact": t.boolean().optional(),
            "required": t.boolean().optional(),
            "displayName": t.string(),
            "isList": t.boolean().optional(),
            "entityType": t.string(),
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterOut"])
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
    types["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"] = t.struct(
        {"version": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"] = t.struct(
        {"version": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn"] = t.struct(
        {"quickReplies": t.array(t.string()).optional(), "title": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut"] = t.struct(
        {
            "quickReplies": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut"])
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
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"] = t.struct(
        {
            "conversationSuccess": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn"
                ]
            ).optional(),
            "channel": t.string().optional(),
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn"]
            ).optional(),
            "liveAgentHandoff": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn"
                ]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "outputAudioText": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn"
                ]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"] = t.struct(
        {
            "conversationSuccess": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut"
                ]
            ).optional(),
            "endInteraction": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"
                ]
            ).optional(),
            "channel": t.string().optional(),
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut"]
            ).optional(),
            "liveAgentHandoff": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut"
                ]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "mixedAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut"]
            ).optional(),
            "outputAudioText": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"
                ]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageImageIn"] = t.struct(
        {"accessibilityText": t.string().optional(), "imageUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageImageOut"] = t.struct(
        {
            "accessibilityText": t.string().optional(),
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"])
    types["GoogleCloudDialogflowV2WebhookResponseIn"] = t.struct(
        {
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2EventInputIn"]
            ).optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SessionEntityTypeIn"])
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
            "source": t.string().optional(),
            "fulfillmentText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookResponseIn"])
    types["GoogleCloudDialogflowV2WebhookResponseOut"] = t.struct(
        {
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2EventInputOut"]
            ).optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SessionEntityTypeOut"])
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "source": t.string().optional(),
            "fulfillmentText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookResponseOut"])
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
    types["GoogleCloudDialogflowCxV3VersionVariantsVariantIn"] = t.struct(
        {
            "version": t.string().optional(),
            "isControlGroup": t.boolean().optional(),
            "trafficAllocation": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionVariantsVariantIn"])
    types["GoogleCloudDialogflowCxV3VersionVariantsVariantOut"] = t.struct(
        {
            "version": t.string().optional(),
            "isControlGroup": t.boolean().optional(),
            "trafficAllocation": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionVariantsVariantOut"])
    types["GoogleCloudDialogflowCxV3ResourceNameIn"] = t.struct(
        {"displayName": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResourceNameIn"])
    types["GoogleCloudDialogflowCxV3ResourceNameOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResourceNameOut"])
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
    types["GoogleCloudDialogflowCxV3WebhookResponseIn"] = t.struct(
        {
            "fulfillmentResponse": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoIn"]
            ).optional(),
            "targetPage": t.string().optional(),
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
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoOut"]
            ).optional(),
            "targetPage": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoOut"]
            ).optional(),
            "targetFlow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseOut"])
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
    types["GoogleCloudDialogflowCxV3ListTestCasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "testCases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3ListTestCasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "testCases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTestCasesResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIn"] = t.struct(
        {
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn"]
            ).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
            ).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn"
                ]
            ).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoIn"]
            ).optional(),
            "triggerIntent": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoIn"]
            ).optional(),
            "detectIntentResponseId": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "text": t.string().optional(),
            "transcript": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "dtmfDigits": t.string().optional(),
            "languageCode": t.string().optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestOut"] = t.struct(
        {
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut"]
            ).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
            ).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut"
                ]
            ).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoOut"]
            ).optional(),
            "triggerIntent": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoOut"]
            ).optional(),
            "detectIntentResponseId": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "text": t.string().optional(),
            "transcript": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "dtmfDigits": t.string().optional(),
            "languageCode": t.string().optional(),
            "fulfillmentInfo": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn"
    ] = t.struct(
        {
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageIn"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn"])
            ).optional(),
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
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageOut"]
            ).optional(),
            "differences": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut"])
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut"])
            ).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut"]
    )
    types["GoogleCloudDialogflowCxV3beta1IntentInputIn"] = t.struct(
        {"intent": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentInputIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentInputOut"] = t.struct(
        {"intent": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentInputOut"])
    types["GoogleCloudDialogflowCxV3SessionEntityTypeIn"] = t.struct(
        {
            "name": t.string(),
            "entityOverrideMode": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
            ),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionEntityTypeIn"])
    types["GoogleCloudDialogflowCxV3SessionEntityTypeOut"] = t.struct(
        {
            "name": t.string(),
            "entityOverrideMode": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"])
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
    types["GoogleCloudDialogflowCxV3EventInputIn"] = t.struct(
        {"event": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EventInputIn"])
    types["GoogleCloudDialogflowCxV3EventInputOut"] = t.struct(
        {
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventInputOut"])
    types["GoogleCloudDialogflowCxV3TestErrorIn"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "testCase": t.string().optional(),
            "testTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestErrorIn"])
    types["GoogleCloudDialogflowCxV3TestErrorOut"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "testCase": t.string().optional(),
            "testTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestErrorOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
    ] = t.struct({"url": t.string(), "urlTypeHint": t.string().optional()}).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
    ] = t.struct(
        {
            "url": t.string(),
            "urlTypeHint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
        ]
    )
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
    types["GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn"] = t.struct(
        {"horizontalAlignment": t.string().optional(), "header": t.string()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn"])
    types["GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut"] = t.struct(
        {
            "horizontalAlignment": t.string().optional(),
            "header": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut"])
    types["GoogleCloudDialogflowCxV3TurnSignalsIn"] = t.struct(
        {
            "noUserInput": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "reachedEndPage": t.boolean().optional(),
            "agentEscalated": t.boolean().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "failureReasons": t.array(t.string()).optional(),
            "dtmfUsed": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TurnSignalsIn"])
    types["GoogleCloudDialogflowCxV3TurnSignalsOut"] = t.struct(
        {
            "noUserInput": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "reachedEndPage": t.boolean().optional(),
            "agentEscalated": t.boolean().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "failureReasons": t.array(t.string()).optional(),
            "dtmfUsed": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TurnSignalsOut"])
    types["GoogleCloudDialogflowCxV3beta1AudioInputIn"] = t.struct(
        {
            "config": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigIn"]
            ),
            "audio": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1AudioInputIn"])
    types["GoogleCloudDialogflowCxV3beta1AudioInputOut"] = t.struct(
        {
            "config": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigOut"]
            ),
            "audio": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1AudioInputOut"])
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
    types[
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut"]
    )
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
    types["GoogleCloudDialogflowCxV3PageInfoIn"] = t.struct(
        {
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoFormInfoIn"]
            ).optional(),
            "currentPage": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoIn"])
    types["GoogleCloudDialogflowCxV3PageInfoOut"] = t.struct(
        {
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoFormInfoOut"]
            ).optional(),
            "currentPage": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoOut"])
    types["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "source": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn"])
    types["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut"])
    types["GoogleCloudDialogflowCxV3QueryParametersIn"] = t.struct(
        {
            "geoLocation": t.proxy(renames["GoogleTypeLatLngIn"]).optional(),
            "webhookHeaders": t.struct({"_": t.string().optional()}).optional(),
            "timeZone": t.string().optional(),
            "analyzeQueryTextSentiment": t.boolean().optional(),
            "channel": t.string().optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeIn"])
            ).optional(),
            "disableWebhook": t.boolean().optional(),
            "sessionTtl": t.string().optional(),
            "currentPage": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "flowVersions": t.array(t.string()).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryParametersIn"])
    types["GoogleCloudDialogflowCxV3QueryParametersOut"] = t.struct(
        {
            "geoLocation": t.proxy(renames["GoogleTypeLatLngOut"]).optional(),
            "webhookHeaders": t.struct({"_": t.string().optional()}).optional(),
            "timeZone": t.string().optional(),
            "analyzeQueryTextSentiment": t.boolean().optional(),
            "channel": t.string().optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"])
            ).optional(),
            "disableWebhook": t.boolean().optional(),
            "sessionTtl": t.string().optional(),
            "currentPage": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "flowVersions": t.array(t.string()).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryParametersOut"])
    types["GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn"] = t.struct(
        {
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2FaqAnswerIn"])
            ).optional(),
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn"])
    types["GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut"] = t.struct(
        {
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2FaqAnswerOut"])
            ).optional(),
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut"])
    types["GoogleCloudDialogflowV2beta1EntityTypeIn"] = t.struct(
        {
            "enableFuzzyExtraction": t.boolean().optional(),
            "autoExpansionMode": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string(),
            "displayName": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeIn"])
    types["GoogleCloudDialogflowV2beta1EntityTypeOut"] = t.struct(
        {
            "enableFuzzyExtraction": t.boolean().optional(),
            "autoExpansionMode": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string(),
            "displayName": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeOut"])
    types["GoogleCloudDialogflowCxV3FormParameterIn"] = t.struct(
        {
            "displayName": t.string(),
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn"]
            ),
            "isList": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "required": t.boolean().optional(),
            "entityType": t.string(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterIn"])
    types["GoogleCloudDialogflowCxV3FormParameterOut"] = t.struct(
        {
            "displayName": t.string(),
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut"]
            ),
            "isList": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "required": t.boolean().optional(),
            "entityType": t.string(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterOut"])
    types["GoogleCloudDialogflowV2InputDatasetIn"] = t.struct(
        {"dataset": t.string()}
    ).named(renames["GoogleCloudDialogflowV2InputDatasetIn"])
    types["GoogleCloudDialogflowV2InputDatasetOut"] = t.struct(
        {"dataset": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2InputDatasetOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn"] = t.struct(
        {"text": t.string().optional(), "ssml": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut"] = t.struct(
        {
            "text": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "ssml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "formattedText": t.string(),
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
            "title": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "formattedText": t.string(),
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
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardIn"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"]
                )
            ).optional(),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "formattedText": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardOut"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"]
                )
            ).optional(),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "formattedText": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardOut"])
    types["GoogleCloudDialogflowCxV3TestConfigIn"] = t.struct(
        {
            "trackingParameters": t.array(t.string()).optional(),
            "flow": t.string().optional(),
            "page": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestConfigIn"])
    types["GoogleCloudDialogflowCxV3TestConfigOut"] = t.struct(
        {
            "trackingParameters": t.array(t.string()).optional(),
            "flow": t.string().optional(),
            "page": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestConfigOut"])
    types["GoogleCloudDialogflowCxV3beta1TestErrorIn"] = t.struct(
        {
            "testCase": t.string().optional(),
            "testTime": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestErrorIn"])
    types["GoogleCloudDialogflowCxV3beta1TestErrorOut"] = t.struct(
        {
            "testCase": t.string().optional(),
            "testTime": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestErrorOut"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut"])
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
    types["GoogleCloudDialogflowCxV3FulfillIntentRequestIn"] = t.struct(
        {
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"]).optional(),
            "matchIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
            ).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentRequestIn"])
    types["GoogleCloudDialogflowCxV3FulfillIntentRequestOut"] = t.struct(
        {
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"]).optional(),
            "matchIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowCxV3MatchIntentRequestOut"]
            ).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentRequestOut"])
    types["GoogleCloudDialogflowCxV3QueryResultIn"] = t.struct(
        {
            "webhookPayloads": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "triggerIntent": t.string().optional(),
            "text": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultIn"]
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentIn"]).optional(),
            "languageCode": t.string().optional(),
            "transcript": t.string().optional(),
            "webhookStatuses": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "triggerEvent": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"]).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "dtmf": t.proxy(renames["GoogleCloudDialogflowCxV3DtmfInputIn"]).optional(),
            "responseMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryResultIn"])
    types["GoogleCloudDialogflowCxV3QueryResultOut"] = t.struct(
        {
            "webhookPayloads": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "triggerIntent": t.string().optional(),
            "text": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultOut"]
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]).optional(),
            "languageCode": t.string().optional(),
            "transcript": t.string().optional(),
            "webhookStatuses": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "triggerEvent": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"]).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3DtmfInputOut"]
            ).optional(),
            "responseMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryResultOut"])
    types["GoogleCloudDialogflowV2FaqAnswerIn"] = t.struct(
        {
            "question": t.string().optional(),
            "answer": t.string().optional(),
            "confidence": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "answerRecord": t.string().optional(),
            "source": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2FaqAnswerIn"])
    types["GoogleCloudDialogflowV2FaqAnswerOut"] = t.struct(
        {
            "question": t.string().optional(),
            "answer": t.string().optional(),
            "confidence": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "answerRecord": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2FaqAnswerOut"])
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
    types["GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn"] = t.struct(
        {"description": t.string().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn"])
    types["GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut"])
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
            "description": t.string().optional(),
            "title": t.string(),
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
            "description": t.string().optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn"] = t.struct(
        {"audioUri": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut"] = t.struct(
        {
            "audioUri": t.string(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"] = t.struct(
        {"audioUri": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"] = t.struct(
        {"audioUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"])
    types["GoogleCloudDialogflowCxV3NluSettingsIn"] = t.struct(
        {
            "modelType": t.string().optional(),
            "classificationThreshold": t.number().optional(),
            "modelTrainingMode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3NluSettingsIn"])
    types["GoogleCloudDialogflowCxV3NluSettingsOut"] = t.struct(
        {
            "modelType": t.string().optional(),
            "classificationThreshold": t.number().optional(),
            "modelTrainingMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3NluSettingsOut"])
    types["GoogleCloudDialogflowV2EntityTypeEntityIn"] = t.struct(
        {"value": t.string(), "synonyms": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowV2EntityTypeEntityIn"])
    types["GoogleCloudDialogflowV2EntityTypeEntityOut"] = t.struct(
        {
            "value": t.string(),
            "synonyms": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EntityTypeEntityOut"])
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
    types["GoogleCloudDialogflowCxV3ExportFlowResponseIn"] = t.struct(
        {"flowContent": t.string().optional(), "flowUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3ExportFlowResponseOut"] = t.struct(
        {
            "flowContent": t.string().optional(),
            "flowUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportFlowResponseOut"])
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
    types["GoogleCloudDialogflowCxV3ValidateAgentRequestIn"] = t.struct(
        {"languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ValidateAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3ValidateAgentRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidateAgentRequestOut"])
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
    types["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn"] = t.struct(
        {
            "matchConfidence": t.number().optional(),
            "answer": t.string().optional(),
            "faqQuestion": t.string().optional(),
            "matchConfidenceLevel": t.string().optional(),
            "source": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn"])
    types["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut"] = t.struct(
        {
            "matchConfidence": t.number().optional(),
            "answer": t.string().optional(),
            "faqQuestion": t.string().optional(),
            "matchConfidenceLevel": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut"])
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
    types["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"] = t.struct(
        {
            "enableContinuousRun": t.boolean().optional(),
            "testCases": t.array(t.string()).optional(),
            "enablePredeploymentRun": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"] = t.struct(
        {
            "enableContinuousRun": t.boolean().optional(),
            "testCases": t.array(t.string()).optional(),
            "enablePredeploymentRun": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"])
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
    types["GoogleCloudDialogflowCxV3TransitionRouteIn"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "targetFlow": t.string().optional(),
            "intent": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
    types["GoogleCloudDialogflowCxV3TransitionRouteOut"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "targetFlow": t.string().optional(),
            "intent": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "name": t.string().optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
    types["GoogleCloudDialogflowCxV3IntentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
            ).optional(),
            "displayName": t.string(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "isFallback": t.boolean().optional(),
            "description": t.string().optional(),
            "priority": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentIn"])
    types["GoogleCloudDialogflowCxV3IntentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterOut"])
            ).optional(),
            "displayName": t.string(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "isFallback": t.boolean().optional(),
            "description": t.string().optional(),
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentOut"])
    types["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"] = t.struct(
        {
            "smartReplyAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"] = t.struct(
        {
            "smartReplyAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn"] = t.struct(
        {
            "deployment": t.string().optional(),
            "environment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut"] = t.struct(
        {
            "deployment": t.string().optional(),
            "environment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn"
                ]
            ).optional(),
            "platform": t.string().optional(),
            "rbmStandaloneRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCardIn"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTextIn"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"]
            ).optional(),
            "telephonyPlayAudio": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn"]
            ).optional(),
            "rbmCarouselRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn"]
            ).optional(),
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectIn"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn"]
            ).optional(),
            "telephonySynthesizeSpeech": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn"
                ]
            ).optional(),
            "rbmText": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut"
                ]
            ).optional(),
            "platform": t.string().optional(),
            "rbmStandaloneRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCardOut"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTextOut"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"]
            ).optional(),
            "telephonyPlayAudio": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"
                ]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut"]
            ).optional(),
            "rbmCarouselRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut"]
            ).optional(),
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectOut"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut"
                ]
            ).optional(),
            "telephonySynthesizeSpeech": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut"
                ]
            ).optional(),
            "rbmText": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
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
    types["GoogleCloudDialogflowCxV3beta1TextInputIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1TextInputIn"])
    types["GoogleCloudDialogflowCxV3beta1TextInputOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1TextInputOut"])
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
    types["GoogleCloudDialogflowCxV3AdvancedSettingsIn"] = t.struct(
        {
            "audioExportGcsDestination": t.proxy(
                renames["GoogleCloudDialogflowCxV3GcsDestinationIn"]
            ).optional(),
            "loggingSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AdvancedSettingsIn"])
    types["GoogleCloudDialogflowCxV3AdvancedSettingsOut"] = t.struct(
        {
            "audioExportGcsDestination": t.proxy(
                renames["GoogleCloudDialogflowCxV3GcsDestinationOut"]
            ).optional(),
            "loggingSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AdvancedSettingsOut"])
    types["GoogleCloudDialogflowCxV3ExportFlowRequestIn"] = t.struct(
        {
            "flowUri": t.string().optional(),
            "includeReferencedFlows": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3ExportFlowRequestOut"] = t.struct(
        {
            "flowUri": t.string().optional(),
            "includeReferencedFlows": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportFlowRequestOut"])
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
    types["GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn"] = t.struct(
        {"flow": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut"] = t.struct(
        {
            "flow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut"])
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
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn"
    ] = t.struct(
        {
            "height": t.string(),
            "fileUri": t.string(),
            "thumbnailUri": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn"]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut"
    ] = t.struct(
        {
            "height": t.string(),
            "fileUri": t.string(),
            "thumbnailUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut"]
    )
    types["GoogleCloudDialogflowV2beta1SuggestionResultIn"] = t.struct(
        {
            "suggestDialogflowAssistsResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseIn"
                ]
            ).optional(),
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"]
            ).optional(),
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"]
            ).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "suggestEntityExtractionResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseIn"
                ]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestionResultIn"])
    types["GoogleCloudDialogflowV2beta1SuggestionResultOut"] = t.struct(
        {
            "suggestDialogflowAssistsResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseOut"
                ]
            ).optional(),
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"]
            ).optional(),
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "suggestEntityExtractionResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseOut"
                ]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestionResultOut"])
    types["GoogleCloudDialogflowCxV3RunTestCaseRequestIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseRequestIn"])
    types["GoogleCloudDialogflowCxV3RunTestCaseRequestOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseRequestOut"])
    types["GoogleCloudDialogflowV2IntentMessageCardIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "imageUri": t.string().optional(),
            "title": t.string().optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageCardButtonIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageCardOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "imageUri": t.string().optional(),
            "title": t.string().optional(),
            "buttons": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageCardButtonOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardOut"])
    types["GoogleCloudDialogflowCxV3SessionInfoIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "session": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionInfoIn"])
    types["GoogleCloudDialogflowCxV3SessionInfoOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "session": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionInfoOut"])
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
    types["GoogleCloudDialogflowCxV3SentimentAnalysisResultIn"] = t.struct(
        {"magnitude": t.number().optional(), "score": t.number().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultIn"])
    types["GoogleCloudDialogflowCxV3SentimentAnalysisResultOut"] = t.struct(
        {
            "magnitude": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultOut"])
    types["GoogleCloudDialogflowCxV3beta1InputAudioConfigIn"] = t.struct(
        {
            "phraseHints": t.array(t.string()).optional(),
            "model": t.string().optional(),
            "modelVariant": t.string().optional(),
            "enableWordInfo": t.boolean().optional(),
            "audioEncoding": t.string(),
            "sampleRateHertz": t.integer().optional(),
            "singleUtterance": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1InputAudioConfigOut"] = t.struct(
        {
            "phraseHints": t.array(t.string()).optional(),
            "model": t.string().optional(),
            "modelVariant": t.string().optional(),
            "enableWordInfo": t.boolean().optional(),
            "audioEncoding": t.string(),
            "sampleRateHertz": t.integer().optional(),
            "singleUtterance": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigOut"])
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
    types["GoogleCloudDialogflowV2IntentIn"] = t.struct(
        {
            "resetContexts": t.boolean().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
            "events": t.array(t.string()).optional(),
            "priority": t.integer().optional(),
            "parentFollowupIntentName": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
            "isFallback": t.boolean().optional(),
            "webhookState": t.string().optional(),
            "endInteraction": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentParameterIn"])
            ).optional(),
            "action": t.string().optional(),
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "mlDisabled": t.boolean().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhraseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentIn"])
    types["GoogleCloudDialogflowV2IntentOut"] = t.struct(
        {
            "resetContexts": t.boolean().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "events": t.array(t.string()).optional(),
            "priority": t.integer().optional(),
            "rootFollowupIntentName": t.string().optional(),
            "parentFollowupIntentName": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "isFallback": t.boolean().optional(),
            "webhookState": t.string().optional(),
            "endInteraction": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentParameterOut"])
            ).optional(),
            "action": t.string().optional(),
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "mlDisabled": t.boolean().optional(),
            "followupIntentInfo": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentFollowupIntentInfoOut"])
            ).optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhraseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn"] = t.struct(
        {
            "openUrl": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn"
                ]
            ).optional(),
            "text": t.string().optional(),
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
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut"] = t.struct(
        {
            "openUrl": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut"
                ]
            ).optional(),
            "text": t.string().optional(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut"])
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
    types["GoogleCloudDialogflowCxV3ListVersionsResponseIn"] = t.struct(
        {
            "versions": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VersionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListVersionsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListVersionsResponseOut"] = t.struct(
        {
            "versions": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListVersionsResponseOut"])
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
    types["GoogleCloudDialogflowV2beta1FaqAnswerIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "answer": t.string().optional(),
            "question": t.string().optional(),
            "source": t.string().optional(),
            "answerRecord": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1FaqAnswerIn"])
    types["GoogleCloudDialogflowV2beta1FaqAnswerOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "answer": t.string().optional(),
            "question": t.string().optional(),
            "source": t.string().optional(),
            "answerRecord": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1FaqAnswerOut"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"] = t.struct(
        {
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"]
                )
            ),
            "name": t.string().optional(),
            "type": t.string(),
            "timesAddedCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"] = t.struct(
        {
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"]
                )
            ),
            "name": t.string().optional(),
            "type": t.string(),
            "timesAddedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"])
    types["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn"] = t.struct(
        {"names": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut"])
    types["GoogleCloudDialogflowCxV3DeploymentResultIn"] = t.struct(
        {
            "deploymentTestResults": t.array(t.string()).optional(),
            "experiment": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentResultIn"])
    types["GoogleCloudDialogflowCxV3DeploymentResultOut"] = t.struct(
        {
            "deploymentTestResults": t.array(t.string()).optional(),
            "experiment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentResultOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "title": t.string(),
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
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "title": t.string(),
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
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"])
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "conversationDataset": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "conversationDataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ArticleAnswerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ArticleAnswerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"])
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
    types["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"] = t.struct(
        {
            "condition": t.string().optional(),
            "versionVariants": t.proxy(
                renames["GoogleCloudDialogflowCxV3VersionVariantsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"])
    types["GoogleCloudDialogflowCxV3ExperimentDefinitionOut"] = t.struct(
        {
            "condition": t.string().optional(),
            "versionVariants": t.proxy(
                renames["GoogleCloudDialogflowCxV3VersionVariantsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentDefinitionOut"])
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
    types["GoogleCloudDialogflowV2EventInputIn"] = t.struct(
        {
            "name": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "languageCode": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2EventInputIn"])
    types["GoogleCloudDialogflowV2EventInputOut"] = t.struct(
        {
            "name": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EventInputOut"])
    types["GoogleCloudDialogflowCxV3ImportFlowRequestIn"] = t.struct(
        {
            "importOption": t.string().optional(),
            "flowUri": t.string().optional(),
            "flowContent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3ImportFlowRequestOut"] = t.struct(
        {
            "importOption": t.string().optional(),
            "flowUri": t.string().optional(),
            "flowContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowRequestOut"])
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
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn"] = t.struct(
        {"text": t.string().optional(), "ssml": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"] = t.struct(
        {
            "allowPlaybackInterruption": t.boolean().optional(),
            "text": t.string().optional(),
            "ssml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"])
    types["GoogleCloudDialogflowV2SuggestArticlesResponseIn"] = t.struct(
        {
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ArticleAnswerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestArticlesResponseIn"])
    types["GoogleCloudDialogflowV2SuggestArticlesResponseOut"] = t.struct(
        {
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ArticleAnswerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestArticlesResponseOut"])
    types["GoogleCloudDialogflowCxV3TestCaseIn"] = t.struct(
        {
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
            ).optional(),
            "name": t.string().optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
            ).optional(),
            "displayName": t.string(),
            "notes": t.string().optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestConfigIn"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseIn"])
    types["GoogleCloudDialogflowCxV3TestCaseOut"] = t.struct(
        {
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnOut"])
            ).optional(),
            "name": t.string().optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseResultOut"]
            ).optional(),
            "displayName": t.string(),
            "creationTime": t.string().optional(),
            "notes": t.string().optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestConfigOut"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseOut"])
    types["GoogleCloudDialogflowCxV3PageIn"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
            ).optional(),
            "displayName": t.string(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
            ).optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageIn"])
    types["GoogleCloudDialogflowCxV3PageOut"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
            ).optional(),
            "displayName": t.string(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
            ).optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"] = t.struct(
        {"metadata": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"])
    types["GoogleCloudDialogflowCxV3FlowIn"] = t.struct(
        {
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsIn"]
            ).optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowIn"])
    types["GoogleCloudDialogflowCxV3FlowOut"] = t.struct(
        {
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsOut"]
            ).optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowOut"])
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"] = t.struct(
        {
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"])
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"] = t.struct(
        {
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"])
    types["GoogleCloudDialogflowCxV3IntentParameterIn"] = t.struct(
        {
            "redact": t.boolean().optional(),
            "entityType": t.string(),
            "isList": t.boolean().optional(),
            "id": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
    types["GoogleCloudDialogflowCxV3IntentParameterOut"] = t.struct(
        {
            "redact": t.boolean().optional(),
            "entityType": t.string(),
            "isList": t.boolean().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentParameterOut"])
    types["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn"] = t.struct(
        {"text": t.string(), "parameterId": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut"] = t.struct(
        {
            "text": t.string(),
            "parameterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"])
    types["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"] = t.struct(
        {"trainingModelType": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"])
    types["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"] = t.struct(
        {
            "trainingModelType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"])
    types["GoogleCloudDialogflowCxV3MatchIntentResponseIn"] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
            "text": t.string().optional(),
            "matches": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"])
            ).optional(),
            "transcript": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "triggerIntent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentResponseIn"])
    types["GoogleCloudDialogflowCxV3MatchIntentResponseOut"] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "text": t.string().optional(),
            "matches": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"])
            ).optional(),
            "transcript": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentResponseOut"])
    types["GoogleCloudDialogflowCxV3RestoreAgentRequestIn"] = t.struct(
        {
            "agentContent": t.string().optional(),
            "agentUri": t.string().optional(),
            "restoreOption": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RestoreAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3RestoreAgentRequestOut"] = t.struct(
        {
            "agentContent": t.string().optional(),
            "agentUri": t.string().optional(),
            "restoreOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RestoreAgentRequestOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "suggestions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn"]
                )
            ).optional(),
            "media": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "suggestions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut"]
                )
            ).optional(),
            "media": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn"] = t.struct(
        {
            "textToSpeech": t.string().optional(),
            "displayText": t.string().optional(),
            "ssml": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut"] = t.struct(
        {
            "textToSpeech": t.string().optional(),
            "displayText": t.string().optional(),
            "ssml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut"])
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
    types["GoogleCloudDialogflowCxV3MatchIntentRequestIn"] = t.struct(
        {
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
            ).optional(),
            "persistParameterChanges": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"])
    types["GoogleCloudDialogflowCxV3MatchIntentRequestOut"] = t.struct(
        {
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputOut"]),
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersOut"]
            ).optional(),
            "persistParameterChanges": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentRequestOut"])
    types[
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut"]
    )
    types[
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "conversationProfile": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "createTime": t.string().optional(),
            "participantRole": t.string(),
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
            "suggestionFeatureType": t.string(),
            "createTime": t.string().optional(),
            "participantRole": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn"] = t.struct(
        {
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn"]
                )
            ),
            "repeatCount": t.integer().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut"] = t.struct(
        {
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut"]
                )
            ),
            "repeatCount": t.integer().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut"])
    types["GoogleCloudDialogflowCxV3beta1IntentIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentParameterIn"])
            ).optional(),
            "isFallback": t.boolean().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn"])
            ).optional(),
            "priority": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentParameterOut"])
            ).optional(),
            "isFallback": t.boolean().optional(),
            "trainingPhrases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut"]
                )
            ).optional(),
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentOut"])
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
    types["GoogleCloudDialogflowCxV3FlowValidationResultIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "validationMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ValidationMessageIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowValidationResultIn"])
    types["GoogleCloudDialogflowCxV3FlowValidationResultOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "validationMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ValidationMessageOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowValidationResultOut"])
    types["GoogleCloudDialogflowV2SuggestionResultIn"] = t.struct(
        {
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestArticlesResponseIn"]
            ).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn"]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestionResultIn"])
    types["GoogleCloudDialogflowV2SuggestionResultOut"] = t.struct(
        {
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestArticlesResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut"]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestionResultOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectIn"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn"]
                )
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectOut"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectOut"])
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
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "confidence": t.number().optional(),
            "lastMatchedIntent": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "confidence": t.number().optional(),
            "lastMatchedIntent": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut"])
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
    types["GoogleCloudDialogflowCxV3IntentCoverageIn"] = t.struct(
        {
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentCoverageIntentIn"])
            ).optional(),
            "coverageScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentCoverageIn"])
    types["GoogleCloudDialogflowCxV3IntentCoverageOut"] = t.struct(
        {
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentCoverageIntentOut"])
            ).optional(),
            "coverageScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentCoverageOut"])
    types["GoogleCloudDialogflowCxV3ValidateFlowRequestIn"] = t.struct(
        {"languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ValidateFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3ValidateFlowRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidateFlowRequestOut"])
    types[
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn"
    ] = t.struct(
        {
            "message": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageIn"]
            ).optional(),
            "additionalCases": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut"
    ] = t.struct(
        {
            "message": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageOut"]
            ).optional(),
            "additionalCases": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut"
        ]
    )
    types["GoogleCloudDialogflowV2IntentMessageTableCardRowIn"] = t.struct(
        {
            "dividerAfter": t.boolean().optional(),
            "cells": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowIn"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardRowOut"] = t.struct(
        {
            "dividerAfter": t.boolean().optional(),
            "cells": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowOut"])
    types["GoogleCloudDialogflowCxV3beta1DtmfInputIn"] = t.struct(
        {"finishDigit": t.string().optional(), "digits": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1DtmfInputIn"])
    types["GoogleCloudDialogflowCxV3beta1DtmfInputOut"] = t.struct(
        {
            "finishDigit": t.string().optional(),
            "digits": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1DtmfInputOut"])
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
    types["GoogleCloudDialogflowCxV3StopExperimentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StopExperimentRequestIn"])
    types["GoogleCloudDialogflowCxV3StopExperimentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StopExperimentRequestOut"])
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
    types["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"] = t.struct(
        {
            "entityType": t.string().optional(),
            "alias": t.string().optional(),
            "userDefined": t.boolean().optional(),
            "text": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"] = t.struct(
        {
            "entityType": t.string().optional(),
            "alias": t.string().optional(),
            "userDefined": t.boolean().optional(),
            "text": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"])
    types["GoogleCloudDialogflowCxV3StartExperimentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StartExperimentRequestIn"])
    types["GoogleCloudDialogflowCxV3StartExperimentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StartExperimentRequestOut"])
    types["GoogleCloudDialogflowCxV3ContinuousTestResultIn"] = t.struct(
        {
            "testCaseResults": t.array(t.string()).optional(),
            "runTime": t.string().optional(),
            "name": t.string().optional(),
            "result": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ContinuousTestResultIn"])
    types["GoogleCloudDialogflowCxV3ContinuousTestResultOut"] = t.struct(
        {
            "testCaseResults": t.array(t.string()).optional(),
            "runTime": t.string().optional(),
            "name": t.string().optional(),
            "result": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ContinuousTestResultOut"])
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
    types["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut"])
    types["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn"] = t.struct(
        {"text": t.string(), "parameterId": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut"] = t.struct(
        {
            "text": t.string(),
            "parameterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut"])
    types["GoogleCloudDialogflowV2MessageAnnotationIn"] = t.struct(
        {
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2AnnotatedMessagePartIn"])
            ).optional(),
            "containEntities": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageAnnotationIn"])
    types["GoogleCloudDialogflowV2MessageAnnotationOut"] = t.struct(
        {
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2AnnotatedMessagePartOut"])
            ).optional(),
            "containEntities": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageAnnotationOut"])
    types["GoogleCloudDialogflowV2SentimentIn"] = t.struct(
        {"score": t.number().optional(), "magnitude": t.number().optional()}
    ).named(renames["GoogleCloudDialogflowV2SentimentIn"])
    types["GoogleCloudDialogflowV2SentimentOut"] = t.struct(
        {
            "score": t.number().optional(),
            "magnitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SentimentOut"])
    types["GoogleCloudDialogflowV2IntentMessageTextIn"] = t.struct(
        {"text": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTextIn"])
    types["GoogleCloudDialogflowV2IntentMessageTextOut"] = t.struct(
        {
            "text": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTextOut"])
    types["GoogleCloudDialogflowCxV3DetectIntentResponseIn"] = t.struct(
        {
            "outputAudio": t.string().optional(),
            "responseId": t.string().optional(),
            "responseType": t.string().optional(),
            "allowCancellation": t.boolean().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultIn"]
            ).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentResponseIn"])
    types["GoogleCloudDialogflowCxV3DetectIntentResponseOut"] = t.struct(
        {
            "outputAudio": t.string().optional(),
            "responseId": t.string().optional(),
            "responseType": t.string().optional(),
            "allowCancellation": t.boolean().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultOut"]
            ).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentResponseOut"])
    types["GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseIn"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "dialogflowAssistAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1DialogflowAssistAnswerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseOut"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "dialogflowAssistAnswers": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1DialogflowAssistAnswerOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponseOut"])
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
    types["GoogleCloudDialogflowCxV3ConversationSignalsIn"] = t.struct(
        {"turnSignals": t.proxy(renames["GoogleCloudDialogflowCxV3TurnSignalsIn"])}
    ).named(renames["GoogleCloudDialogflowCxV3ConversationSignalsIn"])
    types["GoogleCloudDialogflowCxV3ConversationSignalsOut"] = t.struct(
        {
            "turnSignals": t.proxy(renames["GoogleCloudDialogflowCxV3TurnSignalsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationSignalsOut"])
    types["GoogleCloudDialogflowV2IntentParameterIn"] = t.struct(
        {
            "displayName": t.string(),
            "prompts": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "isList": t.boolean().optional(),
            "value": t.string().optional(),
            "entityTypeDisplayName": t.string().optional(),
            "mandatory": t.boolean().optional(),
            "defaultValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentParameterIn"])
    types["GoogleCloudDialogflowV2IntentParameterOut"] = t.struct(
        {
            "displayName": t.string(),
            "prompts": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "isList": t.boolean().optional(),
            "value": t.string().optional(),
            "entityTypeDisplayName": t.string().optional(),
            "mandatory": t.boolean().optional(),
            "defaultValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentParameterOut"])
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
            "state": t.string().optional(),
            "exportOperationMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ExportOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2KnowledgeOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageTextIn"] = t.struct(
        {"text": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageTextIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageTextOut"] = t.struct(
        {
            "text": t.array(t.string()),
            "allowPlaybackInterruption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageTextOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn"] = t.struct(
        {"audioUri": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut"] = t.struct(
        {
            "audioUri": t.string(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "title": t.string(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"]
            ),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "title": t.string(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"]
            ),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut"])
    types["GoogleCloudDialogflowCxV3RunTestCaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseMetadataIn"])
    types["GoogleCloudDialogflowCxV3RunTestCaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseMetadataOut"])
    types["GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn"] = t.struct(
        {"audio": t.string().optional(), "uri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut"] = t.struct(
        {
            "audio": t.string().optional(),
            "uri": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut"])
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
    types["GoogleCloudDialogflowCxV3beta1EventInputIn"] = t.struct(
        {"event": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventInputIn"])
    types["GoogleCloudDialogflowCxV3beta1EventInputOut"] = t.struct(
        {
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventInputOut"])
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
    types["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"] = t.struct(
        {"state": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"])
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
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2beta1IntentSuggestionIn"] = t.struct(
        {
            "intentV2": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentSuggestionIn"])
    types["GoogleCloudDialogflowV2beta1IntentSuggestionOut"] = t.struct(
        {
            "intentV2": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentSuggestionOut"])
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
    types["GoogleCloudDialogflowCxV3ConversationTurnIn"] = t.struct(
        {
            "virtualAgentOutput": t.proxy(
                renames["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn"]
            ).optional(),
            "userInput": t.proxy(
                renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
    types["GoogleCloudDialogflowCxV3ConversationTurnOut"] = t.struct(
        {
            "virtualAgentOutput": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut"
                ]
            ).optional(),
            "userInput": t.proxy(
                renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnOut"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"])
            ),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectIn"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"]
                )
            ),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectOut"])
    types["GoogleCloudDialogflowCxV3beta1IntentParameterIn"] = t.struct(
        {
            "entityType": t.string(),
            "isList": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "id": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentParameterIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentParameterOut"] = t.struct(
        {
            "entityType": t.string(),
            "isList": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentParameterOut"])
    types["GoogleCloudDialogflowCxV3ListWebhooksResponseIn"] = t.struct(
        {
            "webhooks": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3WebhookIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseIn"])
    types["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"] = t.struct(
        {
            "webhooks": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListWebhooksResponseOut"])
    types["GoogleCloudDialogflowV2beta1QueryResultIn"] = t.struct(
        {
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn"]
            ).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentIn"]
            ).optional(),
            "languageCode": t.string().optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "action": t.string().optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "knowledgeAnswers": t.proxy(
                renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersIn"]
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "queryText": t.string().optional(),
            "webhookSource": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1QueryResultIn"])
    types["GoogleCloudDialogflowV2beta1QueryResultOut"] = t.struct(
        {
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut"]
            ).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "action": t.string().optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "knowledgeAnswers": t.proxy(
                renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersOut"]
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "queryText": t.string().optional(),
            "webhookSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1QueryResultOut"])
    types["GoogleCloudDialogflowCxV3TrainFlowRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TrainFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3TrainFlowRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TrainFlowRequestOut"])
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
    types["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn"] = t.struct(
        {
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "justCollected": t.boolean().optional(),
            "required": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut"] = t.struct(
        {
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "justCollected": t.boolean().optional(),
            "required": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut"])
    types[
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
    ] = t.struct(
        {
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
                ]
            ),
            "title": t.string(),
            "footer": t.string().optional(),
            "description": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
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
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
                ]
            ),
            "title": t.string(),
            "footer": t.string().optional(),
            "description": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardIn"] = t.struct(
        {
            "title": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn"]
                )
            ).optional(),
            "subtitle": t.string().optional(),
            "imageUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardOut"] = t.struct(
        {
            "title": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut"]
                )
            ).optional(),
            "subtitle": t.string().optional(),
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardOut"])
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
            "conversationModelEvaluation": t.string().optional(),
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
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
            "conversationModelEvaluation": t.string().optional(),
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut"
        ]
    )
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
    types["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"] = t.struct(
        {
            "lowerBound": t.number().optional(),
            "upperBound": t.number().optional(),
            "confidenceLevel": t.number().optional(),
            "ratio": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut"] = t.struct(
        {
            "lowerBound": t.number().optional(),
            "upperBound": t.number().optional(),
            "confidenceLevel": t.number().optional(),
            "ratio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut"])
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
    types["GoogleCloudDialogflowCxV3beta1WebhookResponseIn"] = t.struct(
        {
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoIn"]
            ).optional(),
            "targetPage": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "fulfillmentResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn"
                ]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoIn"]
            ).optional(),
            "targetFlow": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookResponseOut"] = t.struct(
        {
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoOut"]
            ).optional(),
            "targetPage": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "fulfillmentResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut"
                ]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoOut"]
            ).optional(),
            "targetFlow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookResponseOut"])
    types["GoogleCloudDialogflowV2WebhookRequestIn"] = t.struct(
        {
            "session": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2QueryResultIn"]
            ).optional(),
            "responseId": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookRequestIn"])
    types["GoogleCloudDialogflowV2WebhookRequestOut"] = t.struct(
        {
            "session": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2QueryResultOut"]
            ).optional(),
            "responseId": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookRequestOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
                    ]
                )
            ),
            "imageDisplayOptions": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
                    ]
                )
            ),
            "imageDisplayOptions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut"])
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
    types["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut"])
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
    types[
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "participantRole": t.string(),
            "suggestionFeatureType": t.string(),
            "conversationProfile": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "participantRole": t.string(),
            "suggestionFeatureType": t.string(),
            "conversationProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2beta1ConversationEventIn"] = t.struct(
        {
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageIn"]
            ).optional(),
            "conversation": t.string(),
            "type": t.string(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ConversationEventIn"])
    types["GoogleCloudDialogflowV2beta1ConversationEventOut"] = t.struct(
        {
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageOut"]
            ).optional(),
            "conversation": t.string(),
            "type": t.string(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ConversationEventOut"])
    types[
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn"
    ] = t.struct(
        {"magnitude": t.number().optional(), "score": t.number().optional()}
    ).named(
        renames["GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut"
    ] = t.struct(
        {
            "magnitude": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut"]
    )
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
    types["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"] = t.struct(
        {"version": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"] = t.struct(
        {"version": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"])
    types["GoogleCloudDialogflowCxV3ImportTestCasesResponseIn"] = t.struct(
        {"names": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportTestCasesResponseOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesResponseOut"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"]
                )
            ).optional(),
            "title": t.string(),
            "columnProperties": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn"]
                )
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowIn"])
            ).optional(),
            "subtitle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"]
                )
            ).optional(),
            "title": t.string(),
            "columnProperties": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut"]
                )
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowOut"])
            ).optional(),
            "subtitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn"] = t.struct(
        {"destinationName": t.string(), "uri": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut"] = t.struct(
        {
            "destinationName": t.string(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut"])
    types["GoogleCloudDialogflowCxV3InputAudioConfigIn"] = t.struct(
        {
            "audioEncoding": t.string(),
            "enableWordInfo": t.boolean().optional(),
            "model": t.string().optional(),
            "modelVariant": t.string().optional(),
            "singleUtterance": t.boolean().optional(),
            "sampleRateHertz": t.integer().optional(),
            "phraseHints": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3InputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3InputAudioConfigOut"] = t.struct(
        {
            "audioEncoding": t.string(),
            "enableWordInfo": t.boolean().optional(),
            "model": t.string().optional(),
            "modelVariant": t.string().optional(),
            "singleUtterance": t.boolean().optional(),
            "sampleRateHertz": t.integer().optional(),
            "phraseHints": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3InputAudioConfigOut"])
    types["GoogleCloudDialogflowCxV3CompareVersionsRequestIn"] = t.struct(
        {"languageCode": t.string().optional(), "targetVersion": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsRequestIn"])
    types["GoogleCloudDialogflowCxV3CompareVersionsRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "targetVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsRequestOut"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"] = t.struct(
        {"metadata": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"])
    types["GoogleCloudDialogflowCxV3QueryInputIn"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventInputIn"]
            ).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3AudioInputIn"]
            ).optional(),
            "text": t.proxy(renames["GoogleCloudDialogflowCxV3TextInputIn"]).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentInputIn"]
            ).optional(),
            "languageCode": t.string(),
            "dtmf": t.proxy(renames["GoogleCloudDialogflowCxV3DtmfInputIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryInputIn"])
    types["GoogleCloudDialogflowCxV3QueryInputOut"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventInputOut"]
            ).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3AudioInputOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextInputOut"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentInputOut"]
            ).optional(),
            "languageCode": t.string(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3DtmfInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryInputOut"])
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
    types["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn"] = t.struct(
        {
            "parameter": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn"])
    types["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut"] = t.struct(
        {
            "parameter": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut"])
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
    types["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn"] = t.struct(
        {
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn"])
    types["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"] = t.struct(
        {
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"])
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
    types["GoogleCloudDialogflowCxV3WebhookRequestIn"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoIn"]
            ).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn"
                ]
            ).optional(),
            "dtmfDigits": t.string().optional(),
            "detectIntentResponseId": t.string().optional(),
            "transcript": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"]
            ).optional(),
            "languageCode": t.string().optional(),
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn"]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoIn"]
            ).optional(),
            "triggerEvent": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestIn"])
    types["GoogleCloudDialogflowCxV3WebhookRequestOut"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoOut"]
            ).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut"
                ]
            ).optional(),
            "dtmfDigits": t.string().optional(),
            "detectIntentResponseId": t.string().optional(),
            "transcript": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut"]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoOut"]
            ).optional(),
            "triggerEvent": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestOut"])
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
    types["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn"]
            ),
            "description": t.string().optional(),
            "title": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn"])
    types["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut"]
            ),
            "description": t.string().optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut"])
    types["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"] = t.struct(
        {
            "entityOverrideMode": t.string(),
            "name": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"])
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"])
    types["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"] = t.struct(
        {
            "entityOverrideMode": t.string(),
            "name": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"])
    types["GoogleCloudDialogflowV2AnnotatedMessagePartIn"] = t.struct(
        {
            "text": t.string().optional(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
            "entityType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2AnnotatedMessagePartIn"])
    types["GoogleCloudDialogflowV2AnnotatedMessagePartOut"] = t.struct(
        {
            "text": t.string().optional(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
            "entityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2AnnotatedMessagePartOut"])
    types["GoogleCloudDialogflowCxV3ListChangelogsResponseIn"] = t.struct(
        {
            "changelogs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ChangelogIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListChangelogsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListChangelogsResponseOut"] = t.struct(
        {
            "changelogs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ChangelogOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListChangelogsResponseOut"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "covered": t.boolean().optional(),
            "transitionRoute": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteIn"]
            ).optional(),
            "source": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"]
            ).optional(),
            "eventHandler": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventHandlerIn"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "covered": t.boolean().optional(),
            "transitionRoute": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteOut"]
            ).optional(),
            "source": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"]
            ).optional(),
            "eventHandler": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventHandlerOut"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut"])
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
    types["GoogleCloudDialogflowV2IntentTrainingPhraseIn"] = t.struct(
        {
            "type": t.string(),
            "timesAddedCount": t.integer().optional(),
            "name": t.string().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"])
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowV2IntentTrainingPhraseOut"] = t.struct(
        {
            "type": t.string(),
            "timesAddedCount": t.integer().optional(),
            "name": t.string().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhraseOut"])
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
    types["GoogleCloudDialogflowV2EntityTypeIn"] = t.struct(
        {
            "enableFuzzyExtraction": t.boolean().optional(),
            "kind": t.string(),
            "autoExpansionMode": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityIn"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EntityTypeIn"])
    types["GoogleCloudDialogflowV2EntityTypeOut"] = t.struct(
        {
            "enableFuzzyExtraction": t.boolean().optional(),
            "kind": t.string(),
            "autoExpansionMode": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityOut"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EntityTypeOut"])
    types[
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
    ] = t.struct({"url": t.string(), "urlTypeHint": t.string().optional()}).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
        ]
    )
    types[
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
    ] = t.struct(
        {
            "url": t.string(),
            "urlTypeHint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1WebhookRequestIn"] = t.struct(
        {
            "alternativeQueryResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1QueryResultIn"])
            ).optional(),
            "responseId": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn"]
            ).optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1QueryResultIn"]
            ).optional(),
            "session": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookRequestIn"])
    types["GoogleCloudDialogflowV2beta1WebhookRequestOut"] = t.struct(
        {
            "alternativeQueryResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1QueryResultOut"])
            ).optional(),
            "responseId": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut"]
            ).optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1QueryResultOut"]
            ).optional(),
            "session": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookRequestOut"])
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
    types["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"] = t.struct(
        {
            "testResult": t.string().optional(),
            "testTime": t.string().optional(),
            "name": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnIn"])
            ).optional(),
            "environment": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"] = t.struct(
        {
            "testResult": t.string().optional(),
            "testTime": t.string().optional(),
            "name": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnOut"])
            ).optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"])
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
            "knowledgeBase": t.string().optional(),
            "exportOperationMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2beta1ExportOperationMetadataOut"]
            ).optional(),
            "state": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3ListPagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3PageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListPagesResponseIn"])
    types["GoogleCloudDialogflowCxV3ListPagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListPagesResponseOut"])
    types["GoogleCloudDialogflowV2ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV2ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV2ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ImportDocumentsResponseOut"])
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
    types["GoogleCloudDialogflowCxV3IntentInputIn"] = t.struct(
        {"intent": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentInputIn"])
    types["GoogleCloudDialogflowCxV3IntentInputOut"] = t.struct(
        {"intent": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentInputOut"])
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
    types["GoogleCloudDialogflowCxV3EventHandlerIn"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
            "targetFlow": t.string().optional(),
            "event": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
    types["GoogleCloudDialogflowCxV3EventHandlerOut"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "name": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "targetFlow": t.string().optional(),
            "event": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn"] = t.struct(
        {"gcsUri": t.string().optional(), "content": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut"])
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
    types["GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn"] = t.struct(
        {"testCases": t.array(t.string()), "environment": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut"] = t.struct(
        {
            "testCases": t.array(t.string()),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut"])
    types["GoogleCloudDialogflowV2SessionEntityTypeIn"] = t.struct(
        {
            "name": t.string(),
            "entityOverrideMode": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityIn"])
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2SessionEntityTypeIn"])
    types["GoogleCloudDialogflowV2SessionEntityTypeOut"] = t.struct(
        {
            "name": t.string(),
            "entityOverrideMode": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SessionEntityTypeOut"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentIn"] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
            "webhook": t.string().optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn"
                    ]
                )
            ).optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn"
                    ]
                )
            ).optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentOut"] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
            "webhook": t.string().optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut"
                    ]
                )
            ).optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut"
                    ]
                )
            ).optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"])
    types["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn"] = t.struct(
        {
            "state": t.string().optional(),
            "justCollected": t.boolean().optional(),
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "required": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn"])
    types["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut"] = t.struct(
        {
            "state": t.string().optional(),
            "justCollected": t.boolean().optional(),
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "required": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut"])
    types["GoogleCloudDialogflowV2beta1WebhookResponseIn"] = t.struct(
        {
            "source": t.string().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "endInteraction": t.boolean().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "fulfillmentText": t.string().optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"])
            ).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2beta1EventInputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookResponseIn"])
    types["GoogleCloudDialogflowV2beta1WebhookResponseOut"] = t.struct(
        {
            "source": t.string().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "endInteraction": t.boolean().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "fulfillmentText": t.string().optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"])
            ).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2beta1EventInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookResponseOut"])
    types["GoogleCloudDialogflowV2beta1ContextIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "lifespanCount": t.integer().optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ContextIn"])
    types["GoogleCloudDialogflowV2beta1ContextOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "lifespanCount": t.integer().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ContextOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"] = t.struct(
        {
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
            "targetPage": t.string().optional(),
            "intent": t.string().optional(),
            "targetFlow": t.string().optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"])
    types["GoogleCloudDialogflowCxV3beta1TransitionRouteOut"] = t.struct(
        {
            "name": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "targetPage": t.string().optional(),
            "intent": t.string().optional(),
            "targetFlow": t.string().optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn"] = t.struct(
        {
            "dividerAfter": t.boolean().optional(),
            "cells": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut"] = t.struct(
        {
            "dividerAfter": t.boolean().optional(),
            "cells": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut"])
    types["GoogleCloudDialogflowCxV3ExperimentResultMetricIn"] = t.struct(
        {
            "count": t.number().optional(),
            "countType": t.string().optional(),
            "ratio": t.number().optional(),
            "confidenceInterval": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultMetricOut"] = t.struct(
        {
            "count": t.number().optional(),
            "countType": t.string().optional(),
            "ratio": t.number().optional(),
            "confidenceInterval": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut"
                ]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricOut"])
    types["GoogleCloudDialogflowV2ExportAgentResponseIn"] = t.struct(
        {"agentUri": t.string().optional(), "agentContent": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2ExportAgentResponseIn"])
    types["GoogleCloudDialogflowV2ExportAgentResponseOut"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "agentContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ExportAgentResponseOut"])
    types["GoogleCloudDialogflowV2IntentMessageIn"] = t.struct(
        {
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageListSelectIn"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageQuickRepliesIn"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBasicCardIn"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCardIn"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTableCardIn"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSuggestionsIn"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTextIn"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageMediaContentIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectIn"]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn"]
            ).optional(),
            "platform": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageIn"])
    types["GoogleCloudDialogflowV2IntentMessageOut"] = t.struct(
        {
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageListSelectOut"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageQuickRepliesOut"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBasicCardOut"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCardOut"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTableCardOut"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSuggestionsOut"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTextOut"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageMediaContentOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectOut"]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut"]
            ).optional(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageOut"])
    types["GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn"] = t.struct(
        {"agentContent": t.string().optional(), "agentUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut"] = t.struct(
        {
            "agentContent": t.string().optional(),
            "agentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn"] = t.struct(
        {
            "reply": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn"]
            ).optional(),
            "action": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut"] = t.struct(
        {
            "reply": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut"]
            ).optional(),
            "action": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut"])
    types["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transitionRouteGroups": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transitionRouteGroups": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTextIn"] = t.struct(
        {"text": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTextIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTextOut"] = t.struct(
        {
            "text": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTextOut"])
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
    types["GoogleCloudDialogflowCxV3SecuritySettingsIn"] = t.struct(
        {
            "redactionScope": t.string().optional(),
            "deidentifyTemplate": t.string().optional(),
            "insightsExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn"
                ]
            ).optional(),
            "inspectTemplate": t.string().optional(),
            "purgeDataTypes": t.array(t.string()).optional(),
            "audioExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"
                ]
            ).optional(),
            "redactionStrategy": t.string().optional(),
            "retentionWindowDays": t.integer().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsIn"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsOut"] = t.struct(
        {
            "redactionScope": t.string().optional(),
            "deidentifyTemplate": t.string().optional(),
            "insightsExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut"
                ]
            ).optional(),
            "inspectTemplate": t.string().optional(),
            "purgeDataTypes": t.array(t.string()).optional(),
            "audioExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"
                ]
            ).optional(),
            "redactionStrategy": t.string().optional(),
            "retentionWindowDays": t.integer().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"])
    types["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "requestBody": t.string().optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string(),
            "webhookType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"])
    types["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "requestBody": t.string().optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string(),
            "webhookType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"])
    types["GoogleCloudDialogflowCxV3ListEntityTypesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListEntityTypesResponseIn"])
    types["GoogleCloudDialogflowCxV3ListEntityTypesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListEntityTypesResponseOut"])
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
    types["GoogleCloudDialogflowV2ConversationModelIn"] = t.struct(
        {
            "smartReplyModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"]
            ).optional(),
            "displayName": t.string(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "articleSuggestionModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"]
            ).optional(),
            "datasets": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2InputDatasetIn"])
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationModelIn"])
    types["GoogleCloudDialogflowV2ConversationModelOut"] = t.struct(
        {
            "smartReplyModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"]
            ).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "articleSuggestionModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"]
            ).optional(),
            "datasets": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2InputDatasetOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationModelOut"])
    types["GoogleCloudDialogflowCxV3DetectIntentRequestIn"] = t.struct(
        {
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
            ).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentRequestIn"])
    types["GoogleCloudDialogflowCxV3DetectIntentRequestOut"] = t.struct(
        {
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersOut"]
            ).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentRequestOut"])
    types["GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn"] = t.struct(
        {"contextSize": t.integer().optional(), "latestMessage": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn"])
    types["GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "smartReplyAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SmartReplyAnswerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut"])
    types[
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "participantRole": t.string(),
            "conversationProfile": t.string().optional(),
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
            "createTime": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "participantRole": t.string(),
            "conversationProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut"
        ]
    )
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
    types["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3EnvironmentIn"] = t.struct(
        {
            "description": t.string().optional(),
            "versionConfigs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"])
            ).optional(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn"]
            ).optional(),
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentOut"] = t.struct(
        {
            "description": t.string().optional(),
            "versionConfigs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"])
            ).optional(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut"]
            ).optional(),
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentOut"])
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
    types["GoogleCloudDialogflowCxV3beta1TurnSignalsIn"] = t.struct(
        {
            "dtmfUsed": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "agentEscalated": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "sentimentScore": t.number().optional(),
            "reachedEndPage": t.boolean().optional(),
            "noUserInput": t.boolean().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "userEscalated": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TurnSignalsIn"])
    types["GoogleCloudDialogflowCxV3beta1TurnSignalsOut"] = t.struct(
        {
            "dtmfUsed": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "agentEscalated": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "sentimentScore": t.number().optional(),
            "reachedEndPage": t.boolean().optional(),
            "noUserInput": t.boolean().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "userEscalated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TurnSignalsOut"])
    types["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"] = t.struct(
        {
            "version": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "source": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"])
    types["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"] = t.struct(
        {
            "version": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"])
    types["GoogleCloudDialogflowV2ArticleAnswerIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "uri": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "snippets": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "answerRecord": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleAnswerIn"])
    types["GoogleCloudDialogflowV2ArticleAnswerOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "uri": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "snippets": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "answerRecord": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleAnswerOut"])
    types["GoogleCloudDialogflowV2beta1DialogflowAssistAnswerIn"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1QueryResultIn"]
            ).optional(),
            "intentSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentSuggestionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1DialogflowAssistAnswerIn"])
    types["GoogleCloudDialogflowV2beta1DialogflowAssistAnswerOut"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1QueryResultOut"]
            ).optional(),
            "intentSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentSuggestionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1DialogflowAssistAnswerOut"])
    types["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn"] = t.struct(
        {
            "conversation": t.string().optional(),
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SuggestionResultIn"])
            ).optional(),
            "participant": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn"])
    types["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut"] = t.struct(
        {
            "conversation": t.string().optional(),
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SuggestionResultOut"])
            ).optional(),
            "participant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut"])
    types[
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationModel": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"] = t.struct(
        {
            "title": t.string(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn"
                ]
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"] = t.struct(
        {
            "title": t.string(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"] = t.struct(
        {
            "text": t.string(),
            "alias": t.string().optional(),
            "userDefined": t.boolean().optional(),
            "entityType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"] = t.struct(
        {
            "text": t.string(),
            "alias": t.string().optional(),
            "userDefined": t.boolean().optional(),
            "entityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"] = t.struct(
        {"synonyms": t.array(t.string()).optional(), "key": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"] = t.struct(
        {
            "synonyms": t.array(t.string()).optional(),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"])
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
    types["GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn"] = t.struct(
        {
            "result": t.string().optional(),
            "runTime": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn"])
    types["GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut"] = t.struct(
        {
            "result": t.string().optional(),
            "runTime": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut"])
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
    types["GoogleCloudDialogflowV2IntentMessageTableCardCellIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellIn"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardCellOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellOut"])
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
    types["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn"] = t.struct(
        {
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageTextIn"])
            ).optional(),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentIn"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn"])
    types["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut"] = t.struct(
        {
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageTextOut"])
            ).optional(),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentOut"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "differences": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestRunDifferenceOut"])
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut"])
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn"
    ] = t.struct(
        {
            "importCount": t.integer().optional(),
            "conversationDataset": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn"]
    )
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut"
    ] = t.struct(
        {
            "importCount": t.integer().optional(),
            "conversationDataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut"]
    )
    types["GoogleCloudDialogflowV2MessageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sendTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "content": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageIn"])
    types["GoogleCloudDialogflowV2MessageOut"] = t.struct(
        {
            "participant": t.string().optional(),
            "participantRole": t.string().optional(),
            "sentimentAnalysis": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultOut"]
            ).optional(),
            "name": t.string().optional(),
            "messageAnnotation": t.proxy(
                renames["GoogleCloudDialogflowV2MessageAnnotationOut"]
            ).optional(),
            "sendTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "content": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageOut"])
    types["GoogleCloudDialogflowCxV3CalculateCoverageResponseIn"] = t.struct(
        {
            "agent": t.string().optional(),
            "routeGroupCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn"]
            ).optional(),
            "intentCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentCoverageIn"]
            ).optional(),
            "transitionCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CalculateCoverageResponseIn"])
    types["GoogleCloudDialogflowCxV3CalculateCoverageResponseOut"] = t.struct(
        {
            "agent": t.string().optional(),
            "routeGroupCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut"]
            ).optional(),
            "intentCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentCoverageOut"]
            ).optional(),
            "transitionCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CalculateCoverageResponseOut"])
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
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsOut"]
            ).optional(),
            "description": t.string().optional(),
            "displayName": t.string(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionOut"])
    types["GoogleCloudDialogflowCxV3GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3GcsDestinationIn"])
    types["GoogleCloudDialogflowCxV3GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GcsDestinationOut"])
    types["GoogleCloudDialogflowV2IntentMessageSimpleResponseIn"] = t.struct(
        {
            "textToSpeech": t.string().optional(),
            "ssml": t.string().optional(),
            "displayText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponseIn"])
    types["GoogleCloudDialogflowV2IntentMessageSimpleResponseOut"] = t.struct(
        {
            "textToSpeech": t.string().optional(),
            "ssml": t.string().optional(),
            "displayText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn"
    ] = t.struct({"text": t.string().optional(), "ssml": t.string().optional()}).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn"]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut"
    ] = t.struct(
        {
            "text": t.string().optional(),
            "ssml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut"]
    )
    types["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"] = t.struct(
        {
            "audioExportPattern": t.string().optional(),
            "enableAudioRedaction": t.boolean().optional(),
            "gcsBucket": t.string().optional(),
            "audioFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"] = t.struct(
        {
            "audioExportPattern": t.string().optional(),
            "enableAudioRedaction": t.boolean().optional(),
            "gcsBucket": t.string().optional(),
            "audioFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn"] = t.struct(
        {"header": t.string(), "horizontalAlignment": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut"] = t.struct(
        {
            "header": t.string(),
            "horizontalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut"])
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
    types["GoogleCloudDialogflowCxV3beta1WebhookIn"] = t.struct(
        {
            "displayName": t.string(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn"]
            ).optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"]
            ).optional(),
            "timeout": t.string().optional(),
            "disabled": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookOut"] = t.struct(
        {
            "displayName": t.string(),
            "serviceDirectory": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut"
                ]
            ).optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"]
            ).optional(),
            "timeout": t.string().optional(),
            "disabled": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookOut"])
    types["GoogleCloudDialogflowCxV3ChangelogIn"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "resource": t.string().optional(),
            "action": t.string().optional(),
            "type": t.string().optional(),
            "userEmail": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ChangelogIn"])
    types["GoogleCloudDialogflowCxV3ChangelogOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "resource": t.string().optional(),
            "action": t.string().optional(),
            "type": t.string().optional(),
            "userEmail": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ChangelogOut"])
    types["GoogleCloudDialogflowV2ConversationEventIn"] = t.struct(
        {
            "conversation": t.string().optional(),
            "type": t.string().optional(),
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2MessageIn"]
            ).optional(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationEventIn"])
    types["GoogleCloudDialogflowV2ConversationEventOut"] = t.struct(
        {
            "conversation": t.string().optional(),
            "type": t.string().optional(),
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2MessageOut"]
            ).optional(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationEventOut"])
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
    types["GoogleCloudDialogflowCxV3OutputAudioConfigIn"] = t.struct(
        {
            "audioEncoding": t.string(),
            "synthesizeSpeechConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"]
            ).optional(),
            "sampleRateHertz": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3OutputAudioConfigOut"] = t.struct(
        {
            "audioEncoding": t.string(),
            "synthesizeSpeechConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"]
            ).optional(),
            "sampleRateHertz": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"])
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
    types["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn"])
    types["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut"])
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
    types["GoogleCloudDialogflowCxV3ValidationMessageIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "detail": t.string().optional(),
            "resources": t.array(t.string()).optional(),
            "resourceNames": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResourceNameIn"])
            ).optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidationMessageIn"])
    types["GoogleCloudDialogflowCxV3ValidationMessageOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "detail": t.string().optional(),
            "resources": t.array(t.string()).optional(),
            "resourceNames": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResourceNameOut"])
            ).optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidationMessageOut"])
    types["GoogleCloudDialogflowCxV3MatchIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "event": t.string().optional(),
            "resolvedInput": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentIn"]).optional(),
            "matchType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIn"])
    types["GoogleCloudDialogflowCxV3MatchOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "event": t.string().optional(),
            "resolvedInput": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]).optional(),
            "matchType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchOut"])
    types["GoogleCloudDialogflowCxV3LoadVersionRequestIn"] = t.struct(
        {"allowOverrideAgentResources": t.boolean().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3LoadVersionRequestIn"])
    types["GoogleCloudDialogflowCxV3LoadVersionRequestOut"] = t.struct(
        {
            "allowOverrideAgentResources": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3LoadVersionRequestOut"])
    types["GoogleCloudDialogflowCxV3RolloutConfigIn"] = t.struct(
        {
            "rolloutSteps": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn"])
            ).optional(),
            "failureCondition": t.string().optional(),
            "rolloutCondition": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigIn"])
    types["GoogleCloudDialogflowCxV3RolloutConfigOut"] = t.struct(
        {
            "rolloutSteps": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut"])
            ).optional(),
            "failureCondition": t.string().optional(),
            "rolloutCondition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigOut"])
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
    types["GoogleCloudDialogflowCxV3RunContinuousTestRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestRequestIn"])
    types["GoogleCloudDialogflowCxV3RunContinuousTestRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestRequestOut"])
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
    types["GoogleCloudDialogflowCxV3TextInputIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3TextInputIn"])
    types["GoogleCloudDialogflowCxV3TextInputOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TextInputOut"])
    types["GoogleCloudDialogflowCxV3ImportFlowResponseIn"] = t.struct(
        {"flow": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportFlowResponseOut"] = t.struct(
        {
            "flow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentIn"] = t.struct(
        {
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "versionConfigs": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"]
                )
            ).optional(),
            "displayName": t.string(),
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "versionConfigs": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"]
                )
            ).optional(),
            "displayName": t.string(),
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentOut"])
    types["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "lastMatchedIntent": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn"])
    types["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "lastMatchedIntent": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut"])
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
    types["GoogleCloudDialogflowV2IntentMessageImageIn"] = t.struct(
        {"imageUri": t.string().optional(), "accessibilityText": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageImageIn"])
    types["GoogleCloudDialogflowV2IntentMessageImageOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "accessibilityText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageImageOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn"
    ] = t.struct({"audio": t.string().optional(), "uri": t.string().optional()}).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut"
    ] = t.struct(
        {
            "audio": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut"]
    )
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
    types["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"] = t.struct(
        {"enableSpeechAdaptation": t.boolean().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"])
    types["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"] = t.struct(
        {
            "enableSpeechAdaptation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"])
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
    types["GoogleCloudDialogflowCxV3AudioInputIn"] = t.struct(
        {
            "audio": t.string().optional(),
            "config": t.proxy(renames["GoogleCloudDialogflowCxV3InputAudioConfigIn"]),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AudioInputIn"])
    types["GoogleCloudDialogflowCxV3AudioInputOut"] = t.struct(
        {
            "audio": t.string().optional(),
            "config": t.proxy(renames["GoogleCloudDialogflowCxV3InputAudioConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AudioInputOut"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"] = t.struct(
        {
            "title": t.string(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn"]
            ),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"] = t.struct(
        {
            "title": t.string(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut"]
            ),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"])
    types["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"] = t.struct(
        {"value": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"])
    types["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"])
    types["GoogleCloudDialogflowCxV3WebhookIn"] = t.struct(
        {
            "name": t.string().optional(),
            "disabled": t.boolean().optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
            ).optional(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "timeout": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookIn"])
    types["GoogleCloudDialogflowCxV3WebhookOut"] = t.struct(
        {
            "name": t.string().optional(),
            "disabled": t.boolean().optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"]
            ).optional(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut"]
            ).optional(),
            "displayName": t.string(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookOut"])
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
    types["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn"] = t.struct(
        {
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1QueryInputIn"]
            ).optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn"])
    types["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut"] = t.struct(
        {
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1QueryInputOut"]
            ).optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut"])
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
    types["GoogleCloudDialogflowCxV3ResponseMessageIn"] = t.struct(
        {
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn"]
            ).optional(),
            "conversationSuccess": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"]
            ).optional(),
            "channel": t.string().optional(),
            "outputAudioText": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn"
                ]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageTextIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "liveAgentHandoff": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageOut"] = t.struct(
        {
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut"]
            ).optional(),
            "conversationSuccess": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"
                ]
            ).optional(),
            "channel": t.string().optional(),
            "outputAudioText": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut"
                ]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageTextOut"]
            ).optional(),
            "mixedAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "liveAgentHandoff": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"]
            ).optional(),
            "endInteraction": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
    types["GoogleCloudDialogflowV3alpha1TurnSignalsIn"] = t.struct(
        {
            "reachedEndPage": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "agentEscalated": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "noUserInput": t.boolean().optional(),
            "dtmfUsed": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "triggeredAbandonmentEvent": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1TurnSignalsIn"])
    types["GoogleCloudDialogflowV3alpha1TurnSignalsOut"] = t.struct(
        {
            "reachedEndPage": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "agentEscalated": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "noUserInput": t.boolean().optional(),
            "dtmfUsed": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "triggeredAbandonmentEvent": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1TurnSignalsOut"])
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
    types["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn"] = t.struct(
        {
            "initialPromptFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ),
            "repromptEventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn"])
    types["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut"] = t.struct(
        {
            "initialPromptFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ),
            "repromptEventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut"])
    types[
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "participantRole": t.string(),
            "suggestionFeatureType": t.string(),
            "conversationProfile": t.string().optional(),
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
            "createTime": t.string().optional(),
            "participantRole": t.string(),
            "suggestionFeatureType": t.string(),
            "conversationProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"] = t.struct(
        {
            "username": t.string().optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "uri": t.string(),
            "password": t.string().optional(),
            "webhookType": t.string().optional(),
            "httpMethod": t.string().optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "requestBody": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"] = t.struct(
        {
            "username": t.string().optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "uri": t.string(),
            "password": t.string().optional(),
            "webhookType": t.string().optional(),
            "httpMethod": t.string().optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "requestBody": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"])
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
    types["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"] = t.struct(
        {
            "effectsProfileId": t.array(t.string()).optional(),
            "pitch": t.number().optional(),
            "voice": t.proxy(
                renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsIn"]
            ).optional(),
            "speakingRate": t.number().optional(),
            "volumeGainDb": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"])
    types["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"] = t.struct(
        {
            "effectsProfileId": t.array(t.string()).optional(),
            "pitch": t.number().optional(),
            "voice": t.proxy(
                renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsOut"]
            ).optional(),
            "speakingRate": t.number().optional(),
            "volumeGainDb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"] = t.struct(
        {"tag": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"])
    types["GoogleCloudDialogflowCxV3ExportAgentResponseIn"] = t.struct(
        {"agentContent": t.string().optional(), "agentUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentResponseIn"])
    types["GoogleCloudDialogflowCxV3ExportAgentResponseOut"] = t.struct(
        {
            "agentContent": t.string().optional(),
            "agentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentParameterIn"])
            ).optional(),
            "mlDisabled": t.boolean().optional(),
            "displayName": t.string(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "action": t.string().optional(),
            "webhookState": t.string().optional(),
            "isFallback": t.boolean().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "priority": t.integer().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "parentFollowupIntentName": t.string().optional(),
            "name": t.string().optional(),
            "resetContexts": t.boolean().optional(),
            "endInteraction": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "mlEnabled": t.boolean().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentIn"])
    types["GoogleCloudDialogflowV2beta1IntentOut"] = t.struct(
        {
            "followupIntentInfo": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut"]
                )
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentParameterOut"])
            ).optional(),
            "mlDisabled": t.boolean().optional(),
            "displayName": t.string(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "action": t.string().optional(),
            "webhookState": t.string().optional(),
            "isFallback": t.boolean().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "priority": t.integer().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "parentFollowupIntentName": t.string().optional(),
            "name": t.string().optional(),
            "rootFollowupIntentName": t.string().optional(),
            "resetContexts": t.boolean().optional(),
            "endInteraction": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "mlEnabled": t.boolean().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentOut"])
    types["GoogleCloudDialogflowCxV3ExportAgentRequestIn"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "environment": t.string().optional(),
            "includeBigqueryExportSettings": t.boolean().optional(),
            "dataFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3ExportAgentRequestOut"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "environment": t.string().optional(),
            "includeBigqueryExportSettings": t.boolean().optional(),
            "dataFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentRequestOut"])
    types["GoogleCloudDialogflowV2SmartReplyAnswerIn"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
            "reply": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SmartReplyAnswerIn"])
    types["GoogleCloudDialogflowV2SmartReplyAnswerOut"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
            "reply": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SmartReplyAnswerOut"])
    types["GoogleCloudDialogflowCxV3ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportDocumentsResponseOut"])
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
    types["GoogleCloudDialogflowCxV3ExportTestCasesRequestIn"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "filter": t.string().optional(),
            "dataFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesRequestOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "filter": t.string().optional(),
            "dataFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesRequestOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn"
    ] = t.struct(
        {
            "name": t.string(),
            "contentUrl": t.string(),
            "description": t.string().optional(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
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
            "name": t.string(),
            "contentUrl": t.string(),
            "description": t.string().optional(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
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
    types["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"] = t.struct(
        {"trainingModelType": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"])
    types["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"] = t.struct(
        {
            "trainingModelType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"])
    types["GoogleCloudDialogflowCxV3ExperimentIn"] = t.struct(
        {
            "definition": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "rolloutState": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
            ).optional(),
            "state": t.string().optional(),
            "rolloutFailureReason": t.string().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "experimentLength": t.string().optional(),
            "rolloutConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
            ).optional(),
            "description": t.string().optional(),
            "variantsHistory": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
            ).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentIn"])
    types["GoogleCloudDialogflowCxV3ExperimentOut"] = t.struct(
        {
            "definition": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentDefinitionOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "rolloutState": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutStateOut"]
            ).optional(),
            "state": t.string().optional(),
            "rolloutFailureReason": t.string().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "experimentLength": t.string().optional(),
            "rolloutConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultOut"]
            ).optional(),
            "description": t.string().optional(),
            "variantsHistory": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentOut"])
    types["GoogleCloudDialogflowCxV3EntityTypeIn"] = t.struct(
        {
            "autoExpansionMode": t.string().optional(),
            "excludedPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"])
            ).optional(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "kind": t.string(),
            "redact": t.boolean().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeIn"])
    types["GoogleCloudDialogflowCxV3EntityTypeOut"] = t.struct(
        {
            "autoExpansionMode": t.string().optional(),
            "excludedPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"])
            ).optional(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "kind": t.string(),
            "redact": t.boolean().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityOut"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeOut"])
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
    types["GoogleCloudDialogflowCxV3VoiceSelectionParamsIn"] = t.struct(
        {"name": t.string().optional(), "ssmlGender": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsIn"])
    types["GoogleCloudDialogflowCxV3VoiceSelectionParamsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "ssmlGender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentParameterIn"] = t.struct(
        {
            "mandatory": t.boolean().optional(),
            "isList": t.boolean().optional(),
            "name": t.string().optional(),
            "entityTypeDisplayName": t.string().optional(),
            "defaultValue": t.string().optional(),
            "prompts": t.array(t.string()).optional(),
            "value": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentParameterIn"])
    types["GoogleCloudDialogflowV2beta1IntentParameterOut"] = t.struct(
        {
            "mandatory": t.boolean().optional(),
            "isList": t.boolean().optional(),
            "name": t.string().optional(),
            "entityTypeDisplayName": t.string().optional(),
            "defaultValue": t.string().optional(),
            "prompts": t.array(t.string()).optional(),
            "value": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentParameterOut"])
    types["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "answerRecord": t.string().optional(),
            "reply": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"])
    types["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "answerRecord": t.string().optional(),
            "reply": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseIn"] = t.struct(
        {
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnIn"])
            ).optional(),
            "notes": t.string().optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestConfigIn"]
            ).optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseIn"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseOut"] = t.struct(
        {
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnOut"])
            ).optional(),
            "notes": t.string().optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestConfigOut"]
            ).optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "creationTime": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseOut"])
    types["GoogleCloudDialogflowV2beta1ArticleAnswerIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string().optional(),
            "snippets": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "answerRecord": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ArticleAnswerIn"])
    types["GoogleCloudDialogflowV2beta1ArticleAnswerOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string().optional(),
            "snippets": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "answerRecord": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ArticleAnswerOut"])
    types["GoogleCloudDialogflowV2beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1GcsDestinationIn"])
    types["GoogleCloudDialogflowV2beta1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1GcsDestinationOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn"] = t.struct(
        {"text": t.string().optional(), "postbackData": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut"] = t.struct(
        {
            "text": t.string().optional(),
            "postbackData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut"])
    types["GoogleCloudDialogflowV2HumanAgentAssistantEventIn"] = t.struct(
        {
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SuggestionResultIn"])
            ).optional(),
            "participant": t.string().optional(),
            "conversation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2HumanAgentAssistantEventIn"])
    types["GoogleCloudDialogflowV2HumanAgentAssistantEventOut"] = t.struct(
        {
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SuggestionResultOut"])
            ).optional(),
            "participant": t.string().optional(),
            "conversation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2HumanAgentAssistantEventOut"])
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
    types["GoogleCloudDialogflowCxV3FulfillmentIn"] = t.struct(
        {
            "webhook": t.string().optional(),
            "tag": t.string().optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn"]
                )
            ).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn"]
                )
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentIn"])
    types["GoogleCloudDialogflowCxV3FulfillmentOut"] = t.struct(
        {
            "webhook": t.string().optional(),
            "tag": t.string().optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut"]
                )
            ).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut"]
                )
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentOut"])
    types["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn"] = t.struct(
        {
            "testCaseResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseResultIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut"] = t.struct(
        {
            "testCaseResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestCaseResultOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut"])
    types[
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn"
    ] = t.struct(
        {
            "description": t.string().optional(),
            "contentUrl": t.string(),
            "name": t.string(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn"]
    )
    types[
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut"
    ] = t.struct(
        {
            "description": t.string().optional(),
            "contentUrl": t.string(),
            "name": t.string(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"] = t.struct(
        {
            "flow": t.proxy(renames["GoogleCloudDialogflowCxV3FlowIn"]).optional(),
            "page": t.proxy(renames["GoogleCloudDialogflowCxV3PageIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"] = t.struct(
        {
            "flow": t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"]).optional(),
            "page": t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"])
    types["GoogleCloudDialogflowCxV3RolloutStateIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "stepIndex": t.integer().optional(),
            "step": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutStateIn"])
    types["GoogleCloudDialogflowCxV3RolloutStateOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "stepIndex": t.integer().optional(),
            "step": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutStateOut"])
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
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn"
    ] = t.struct(
        {"score": t.number().optional(), "magnitude": t.number().optional()}
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut"
    ] = t.struct(
        {
            "score": t.number().optional(),
            "magnitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn"] = t.struct(
        {
            "sessionCount": t.integer().optional(),
            "version": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut"] = t.struct(
        {
            "sessionCount": t.integer().optional(),
            "version": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut"])
    types["GoogleCloudDialogflowV2IntentMessageSuggestionIn"] = t.struct(
        {"title": t.string()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSuggestionIn"])
    types["GoogleCloudDialogflowV2IntentMessageSuggestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSuggestionOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn"] = t.struct(
        {"title": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut"])
    types["GoogleCloudDialogflowV2beta1MessageIn"] = t.struct(
        {
            "sendTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "content": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1MessageIn"])
    types["GoogleCloudDialogflowV2beta1MessageOut"] = t.struct(
        {
            "sendTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "createTime": t.string().optional(),
            "participantRole": t.string().optional(),
            "participant": t.string().optional(),
            "name": t.string().optional(),
            "content": t.string(),
            "sentimentAnalysis": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut"]
            ).optional(),
            "messageAnnotation": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageAnnotationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1MessageOut"])
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
    types["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
                    ]
                )
            ),
            "imageDisplayOptions": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
                    ]
                )
            ),
            "imageDisplayOptions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleCloudDialogflowV2QueryResultIn"] = t.struct(
        {
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
            "languageCode": t.string().optional(),
            "webhookSource": t.string().optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowV2IntentIn"]).optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "action": t.string().optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "fulfillmentText": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultIn"]
            ).optional(),
            "queryText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2QueryResultIn"])
    types["GoogleCloudDialogflowV2QueryResultOut"] = t.struct(
        {
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "languageCode": t.string().optional(),
            "webhookSource": t.string().optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowV2IntentOut"]).optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "action": t.string().optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "fulfillmentText": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultOut"]
            ).optional(),
            "queryText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2QueryResultOut"])
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
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
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
    types["GoogleCloudDialogflowCxV3beta1PageIn"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerIn"])
            ).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"])
            ).optional(),
            "displayName": t.string(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3beta1FormIn"]).optional(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
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
            "displayName": t.string(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "form": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FormOut"]
            ).optional(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageOut"])
    types["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"] = t.struct(
        {"tag": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"])
    types["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"])
    types["GoogleCloudDialogflowCxV3beta1EventHandlerIn"] = t.struct(
        {
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
            "event": t.string(),
            "targetPage": t.string().optional(),
            "targetFlow": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventHandlerIn"])
    types["GoogleCloudDialogflowCxV3beta1EventHandlerOut"] = t.struct(
        {
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "event": t.string(),
            "targetPage": t.string().optional(),
            "name": t.string().optional(),
            "targetFlow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventHandlerOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"] = t.struct(
        {
            "title": t.string(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn"
                ]
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"] = t.struct(
        {
            "title": t.string(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"])
    types["GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn"] = t.struct(
        {"flowUri": t.string().optional(), "flowContent": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut"] = t.struct(
        {
            "flowUri": t.string().optional(),
            "flowContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut"])
    types["GoogleCloudDialogflowCxV3ConversationTurnUserInputIn"] = t.struct(
        {
            "isWebhookEnabled": t.boolean().optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryInputIn"]
            ).optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputIn"])
    types["GoogleCloudDialogflowCxV3ConversationTurnUserInputOut"] = t.struct(
        {
            "isWebhookEnabled": t.boolean().optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryInputOut"]
            ).optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputOut"])
    types["GoogleCloudDialogflowV2beta1EventInputIn"] = t.struct(
        {
            "languageCode": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EventInputIn"])
    types["GoogleCloudDialogflowV2beta1EventInputOut"] = t.struct(
        {
            "languageCode": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EventInputOut"])
    types["GoogleCloudDialogflowCxV3beta1QueryInputIn"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EventInputIn"]
            ).optional(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1DtmfInputIn"]
            ).optional(),
            "languageCode": t.string(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TextInputIn"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentInputIn"]
            ).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1AudioInputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1QueryInputIn"])
    types["GoogleCloudDialogflowCxV3beta1QueryInputOut"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EventInputOut"]
            ).optional(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1DtmfInputOut"]
            ).optional(),
            "languageCode": t.string(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TextInputOut"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentInputOut"]
            ).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1AudioInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1QueryInputOut"])
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
    types["GoogleCloudDialogflowCxV3AgentIn"] = t.struct(
        {
            "enableSpellCorrection": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "locked": t.boolean().optional(),
            "securitySettings": t.string().optional(),
            "advancedSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsIn"]
            ).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "startFlow": t.string().optional(),
            "speechToTextSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"]
            ).optional(),
            "textToSpeechSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextToSpeechSettingsIn"]
            ).optional(),
            "supportedLanguageCodes": t.array(t.string()).optional(),
            "avatarUri": t.string().optional(),
            "defaultLanguageCode": t.string(),
            "timeZone": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentIn"])
    types["GoogleCloudDialogflowCxV3AgentOut"] = t.struct(
        {
            "enableSpellCorrection": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "locked": t.boolean().optional(),
            "securitySettings": t.string().optional(),
            "advancedSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsOut"]
            ).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "startFlow": t.string().optional(),
            "speechToTextSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"]
            ).optional(),
            "textToSpeechSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextToSpeechSettingsOut"]
            ).optional(),
            "supportedLanguageCodes": t.array(t.string()).optional(),
            "avatarUri": t.string().optional(),
            "defaultLanguageCode": t.string(),
            "timeZone": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentOut"])
    types["GoogleCloudDialogflowCxV3AgentValidationResultIn"] = t.struct(
        {
            "flowValidationResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FlowValidationResultIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentValidationResultIn"])
    types["GoogleCloudDialogflowCxV3AgentValidationResultOut"] = t.struct(
        {
            "flowValidationResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FlowValidationResultOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentValidationResultOut"])
    types["GoogleCloudDialogflowCxV3TestCaseResultIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "testResult": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
            ).optional(),
            "testTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseResultIn"])
    types["GoogleCloudDialogflowCxV3TestCaseResultOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "testResult": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnOut"])
            ).optional(),
            "testTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseResultOut"])
    types["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowV2IntentMessageMediaContentIn"] = t.struct(
        {
            "mediaType": t.string().optional(),
            "mediaObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn"
                    ]
                )
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageMediaContentIn"])
    types["GoogleCloudDialogflowV2IntentMessageMediaContentOut"] = t.struct(
        {
            "mediaType": t.string().optional(),
            "mediaObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageMediaContentOut"])
    types["GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn"] = t.struct(
        {
            "text": t.string(),
            "entityType": t.string().optional(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn"])
    types["GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut"] = t.struct(
        {
            "text": t.string(),
            "entityType": t.string().optional(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut"])

    functions = {}
    functions["projectsLocationsGet"] = dialogflow.get(
        "v3/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = dialogflow.get(
        "v3/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsDelete"] = dialogflow.get(
        "v3/{parent}/securitySettings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = dialogflow.post(
        "v3/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = dialogflow.post(
        "v3/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = dialogflow.post(
        "v3/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
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
    functions["projectsLocationsAgentsCreate"] = dialogflow.get(
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
    functions["projectsLocationsAgentsValidate"] = dialogflow.get(
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
    functions["projectsLocationsAgentsPatch"] = dialogflow.get(
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
    functions["projectsLocationsAgentsGetValidationResult"] = dialogflow.get(
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
    functions["projectsLocationsAgentsEntityTypesPatch"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
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
                "languageCode": t.string().optional(),
                "name": t.string(),
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
                "languageCode": t.string().optional(),
                "name": t.string(),
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
                "languageCode": t.string().optional(),
                "name": t.string(),
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
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsList"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsGetValidationResult"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsValidate"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPatch"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsDelete"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsGet"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsExport"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsCreate"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsTrain"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsImport"] = dialogflow.post(
        "v3/{parent}/flows:import",
        t.struct(
            {
                "parent": t.string(),
                "importOption": t.string().optional(),
                "flowUri": t.string().optional(),
                "flowContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsLoad"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsDelete"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsGet"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsList"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsCreate"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsCompareVersions"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsPatch"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesDelete"] = dialogflow.post(
        "v3/{parent}/pages",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesGet"] = dialogflow.post(
        "v3/{parent}/pages",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesList"] = dialogflow.post(
        "v3/{parent}/pages",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesPatch"] = dialogflow.post(
        "v3/{parent}/pages",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesCreate"] = dialogflow.post(
        "v3/{parent}/pages",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsFlowsTransitionRouteGroupsCreate"
    ] = dialogflow.get(
        "v3/{parent}/transitionRouteGroups",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsTransitionRouteGroupsGet"] = dialogflow.get(
        "v3/{parent}/transitionRouteGroups",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksCreate"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "disabled": t.boolean().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "displayName": t.string(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksDelete"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "disabled": t.boolean().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "displayName": t.string(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksList"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "disabled": t.boolean().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "displayName": t.string(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksGet"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "disabled": t.boolean().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "displayName": t.string(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksPatch"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "disabled": t.boolean().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "displayName": t.string(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsMatchIntent"] = dialogflow.post(
        "v3/{session}:fulfillIntent",
        t.struct(
            {
                "session": t.string(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
                ).optional(),
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsDetectIntent"] = dialogflow.post(
        "v3/{session}:fulfillIntent",
        t.struct(
            {
                "session": t.string(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
                ).optional(),
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsFulfillIntent"] = dialogflow.post(
        "v3/{session}:fulfillIntent",
        t.struct(
            {
                "session": t.string(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
                ).optional(),
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "outputAudioConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesDelete"] = dialogflow.get(
        "v3/{parent}/entityTypes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesPatch"] = dialogflow.get(
        "v3/{parent}/entityTypes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesGet"] = dialogflow.get(
        "v3/{parent}/entityTypes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesCreate"] = dialogflow.get(
        "v3/{parent}/entityTypes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesList"] = dialogflow.get(
        "v3/{parent}/entityTypes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"]),
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
    functions["projectsLocationsAgentsIntentsDelete"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsPatch"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsCreate"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsList"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsCreate"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsLookupEnvironmentHistory"
    ] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsPatch"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsGet"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsList"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDeployFlow"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsRunContinuousTest"
    ] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDelete"] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsFulfillIntent"
    ] = dialogflow.post(
        "v3/{session}:matchIntent",
        t.struct(
            {
                "session": t.string(),
                "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
                "queryParams": t.proxy(
                    renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
                ).optional(),
                "persistParameterChanges": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3MatchIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsDetectIntent"
    ] = dialogflow.post(
        "v3/{session}:matchIntent",
        t.struct(
            {
                "session": t.string(),
                "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
                "queryParams": t.proxy(
                    renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
                ).optional(),
                "persistParameterChanges": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3MatchIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsMatchIntent"
    ] = dialogflow.post(
        "v3/{session}:matchIntent",
        t.struct(
            {
                "session": t.string(),
                "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
                "queryParams": t.proxy(
                    renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
                ).optional(),
                "persistParameterChanges": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3MatchIntentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesList"
    ] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesGet"
    ] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesCreate"
    ] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesPatch"
    ] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesDelete"
    ] = dialogflow.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
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
    functions["projectsLocationsAgentsEnvironmentsExperimentsDelete"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsList"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsStart"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsPatch"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsCreate"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsStop"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDeploymentsGet"] = dialogflow.get(
        "v3/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDeploymentsList"] = dialogflow.get(
        "v3/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesList"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesRun"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesImport"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesBatchRun"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesCreate"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesGet"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesCalculateCoverage"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesPatch"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesExport"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesBatchDelete"] = dialogflow.post(
        "v3/{parent}/testCases:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesResultsGet"] = dialogflow.get(
        "v3/{parent}/results",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesResultsList"] = dialogflow.get(
        "v3/{parent}/results",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsCancel"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dialogflow",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
