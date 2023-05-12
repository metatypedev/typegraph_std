from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_dialogflow() -> Import:
    dialogflow = HTTPRuntime("https://dialogflow.googleapis.com/")

    renames = {
        "ErrorResponse": "_dialogflow_1_ErrorResponse",
        "GoogleCloudDialogflowV2EntityTypeEntityIn": "_dialogflow_2_GoogleCloudDialogflowV2EntityTypeEntityIn",
        "GoogleCloudDialogflowV2EntityTypeEntityOut": "_dialogflow_3_GoogleCloudDialogflowV2EntityTypeEntityOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn": "_dialogflow_4_GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut": "_dialogflow_5_GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut",
        "GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataIn": "_dialogflow_6_GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataOut": "_dialogflow_7_GoogleCloudDialogflowCxV3beta1DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ConversationTurnUserInputIn": "_dialogflow_8_GoogleCloudDialogflowCxV3ConversationTurnUserInputIn",
        "GoogleCloudDialogflowCxV3ConversationTurnUserInputOut": "_dialogflow_9_GoogleCloudDialogflowCxV3ConversationTurnUserInputOut",
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn": "_dialogflow_10_GoogleCloudDialogflowV2ImportConversationDataOperationResponseIn",
        "GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut": "_dialogflow_11_GoogleCloudDialogflowV2ImportConversationDataOperationResponseOut",
        "GoogleCloudDialogflowV2SessionEntityTypeIn": "_dialogflow_12_GoogleCloudDialogflowV2SessionEntityTypeIn",
        "GoogleCloudDialogflowV2SessionEntityTypeOut": "_dialogflow_13_GoogleCloudDialogflowV2SessionEntityTypeOut",
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn": "_dialogflow_14_GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut": "_dialogflow_15_GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn": "_dialogflow_16_GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut": "_dialogflow_17_GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesRequestIn": "_dialogflow_18_GoogleCloudDialogflowCxV3ImportTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesRequestOut": "_dialogflow_19_GoogleCloudDialogflowCxV3ImportTestCasesRequestOut",
        "GoogleCloudDialogflowV2AnnotatedMessagePartIn": "_dialogflow_20_GoogleCloudDialogflowV2AnnotatedMessagePartIn",
        "GoogleCloudDialogflowV2AnnotatedMessagePartOut": "_dialogflow_21_GoogleCloudDialogflowV2AnnotatedMessagePartOut",
        "GoogleCloudDialogflowCxV3beta1SessionInfoIn": "_dialogflow_22_GoogleCloudDialogflowCxV3beta1SessionInfoIn",
        "GoogleCloudDialogflowCxV3beta1SessionInfoOut": "_dialogflow_23_GoogleCloudDialogflowCxV3beta1SessionInfoOut",
        "GoogleCloudDialogflowV2IntentMessageImageIn": "_dialogflow_24_GoogleCloudDialogflowV2IntentMessageImageIn",
        "GoogleCloudDialogflowV2IntentMessageImageOut": "_dialogflow_25_GoogleCloudDialogflowV2IntentMessageImageOut",
        "GoogleCloudDialogflowV2beta1SuggestionResultIn": "_dialogflow_26_GoogleCloudDialogflowV2beta1SuggestionResultIn",
        "GoogleCloudDialogflowV2beta1SuggestionResultOut": "_dialogflow_27_GoogleCloudDialogflowV2beta1SuggestionResultOut",
        "GoogleCloudDialogflowCxV3FlowIn": "_dialogflow_28_GoogleCloudDialogflowCxV3FlowIn",
        "GoogleCloudDialogflowCxV3FlowOut": "_dialogflow_29_GoogleCloudDialogflowCxV3FlowOut",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataIn": "_dialogflow_30_GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataIn",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataOut": "_dialogflow_31_GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadataOut",
        "GoogleCloudDialogflowCxV3CompareVersionsResponseIn": "_dialogflow_32_GoogleCloudDialogflowCxV3CompareVersionsResponseIn",
        "GoogleCloudDialogflowCxV3CompareVersionsResponseOut": "_dialogflow_33_GoogleCloudDialogflowCxV3CompareVersionsResponseOut",
        "GoogleTypeLatLngIn": "_dialogflow_34_GoogleTypeLatLngIn",
        "GoogleTypeLatLngOut": "_dialogflow_35_GoogleTypeLatLngOut",
        "GoogleCloudDialogflowCxV3AdvancedSettingsIn": "_dialogflow_36_GoogleCloudDialogflowCxV3AdvancedSettingsIn",
        "GoogleCloudDialogflowCxV3AdvancedSettingsOut": "_dialogflow_37_GoogleCloudDialogflowCxV3AdvancedSettingsOut",
        "GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn": "_dialogflow_38_GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut": "_dialogflow_39_GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut",
        "GoogleCloudDialogflowV2ExportAgentResponseIn": "_dialogflow_40_GoogleCloudDialogflowV2ExportAgentResponseIn",
        "GoogleCloudDialogflowV2ExportAgentResponseOut": "_dialogflow_41_GoogleCloudDialogflowV2ExportAgentResponseOut",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersIn": "_dialogflow_42_GoogleCloudDialogflowV2beta1KnowledgeAnswersIn",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersOut": "_dialogflow_43_GoogleCloudDialogflowV2beta1KnowledgeAnswersOut",
        "GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn": "_dialogflow_44_GoogleCloudDialogflowCxV3beta1ExportAgentResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut": "_dialogflow_45_GoogleCloudDialogflowCxV3beta1ExportAgentResponseOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageIn": "_dialogflow_46_GoogleCloudDialogflowCxV3beta1ResponseMessageIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOut": "_dialogflow_47_GoogleCloudDialogflowCxV3beta1ResponseMessageOut",
        "GoogleCloudDialogflowCxV3LoadVersionRequestIn": "_dialogflow_48_GoogleCloudDialogflowCxV3LoadVersionRequestIn",
        "GoogleCloudDialogflowCxV3LoadVersionRequestOut": "_dialogflow_49_GoogleCloudDialogflowCxV3LoadVersionRequestOut",
        "GoogleCloudDialogflowV2IntentMessageCardIn": "_dialogflow_50_GoogleCloudDialogflowV2IntentMessageCardIn",
        "GoogleCloudDialogflowV2IntentMessageCardOut": "_dialogflow_51_GoogleCloudDialogflowV2IntentMessageCardOut",
        "GoogleCloudDialogflowCxV3WebhookResponseIn": "_dialogflow_52_GoogleCloudDialogflowCxV3WebhookResponseIn",
        "GoogleCloudDialogflowCxV3WebhookResponseOut": "_dialogflow_53_GoogleCloudDialogflowCxV3WebhookResponseOut",
        "GoogleCloudDialogflowV2beta1IntentParameterIn": "_dialogflow_54_GoogleCloudDialogflowV2beta1IntentParameterIn",
        "GoogleCloudDialogflowV2beta1IntentParameterOut": "_dialogflow_55_GoogleCloudDialogflowV2beta1IntentParameterOut",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn": "_dialogflow_56_GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut": "_dialogflow_57_GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseErrorIn": "_dialogflow_58_GoogleCloudDialogflowCxV3beta1TestCaseErrorIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseErrorOut": "_dialogflow_59_GoogleCloudDialogflowCxV3beta1TestCaseErrorOut",
        "GoogleCloudDialogflowCxV3RunTestCaseMetadataIn": "_dialogflow_60_GoogleCloudDialogflowCxV3RunTestCaseMetadataIn",
        "GoogleCloudDialogflowCxV3RunTestCaseMetadataOut": "_dialogflow_61_GoogleCloudDialogflowCxV3RunTestCaseMetadataOut",
        "GoogleCloudDialogflowCxV3PageIn": "_dialogflow_62_GoogleCloudDialogflowCxV3PageIn",
        "GoogleCloudDialogflowCxV3PageOut": "_dialogflow_63_GoogleCloudDialogflowCxV3PageOut",
        "GoogleCloudDialogflowV2IntentFollowupIntentInfoIn": "_dialogflow_64_GoogleCloudDialogflowV2IntentFollowupIntentInfoIn",
        "GoogleCloudDialogflowV2IntentFollowupIntentInfoOut": "_dialogflow_65_GoogleCloudDialogflowV2IntentFollowupIntentInfoOut",
        "GoogleCloudDialogflowCxV3FormIn": "_dialogflow_66_GoogleCloudDialogflowCxV3FormIn",
        "GoogleCloudDialogflowCxV3FormOut": "_dialogflow_67_GoogleCloudDialogflowCxV3FormOut",
        "GoogleCloudDialogflowCxV3NluSettingsIn": "_dialogflow_68_GoogleCloudDialogflowCxV3NluSettingsIn",
        "GoogleCloudDialogflowCxV3NluSettingsOut": "_dialogflow_69_GoogleCloudDialogflowCxV3NluSettingsOut",
        "GoogleCloudDialogflowCxV3DeployFlowResponseIn": "_dialogflow_70_GoogleCloudDialogflowCxV3DeployFlowResponseIn",
        "GoogleCloudDialogflowCxV3DeployFlowResponseOut": "_dialogflow_71_GoogleCloudDialogflowCxV3DeployFlowResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn": "_dialogflow_72_GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut": "_dialogflow_73_GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut",
        "GoogleCloudDialogflowCxV3EventHandlerIn": "_dialogflow_74_GoogleCloudDialogflowCxV3EventHandlerIn",
        "GoogleCloudDialogflowCxV3EventHandlerOut": "_dialogflow_75_GoogleCloudDialogflowCxV3EventHandlerOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn": "_dialogflow_76_GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut": "_dialogflow_77_GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterActionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn": "_dialogflow_78_GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut": "_dialogflow_79_GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut",
        "GoogleCloudDialogflowCxV3ExportAgentResponseIn": "_dialogflow_80_GoogleCloudDialogflowCxV3ExportAgentResponseIn",
        "GoogleCloudDialogflowCxV3ExportAgentResponseOut": "_dialogflow_81_GoogleCloudDialogflowCxV3ExportAgentResponseOut",
        "GoogleCloudDialogflowCxV3DeployFlowMetadataIn": "_dialogflow_82_GoogleCloudDialogflowCxV3DeployFlowMetadataIn",
        "GoogleCloudDialogflowCxV3DeployFlowMetadataOut": "_dialogflow_83_GoogleCloudDialogflowCxV3DeployFlowMetadataOut",
        "GoogleCloudDialogflowV2ExportOperationMetadataIn": "_dialogflow_84_GoogleCloudDialogflowV2ExportOperationMetadataIn",
        "GoogleCloudDialogflowV2ExportOperationMetadataOut": "_dialogflow_85_GoogleCloudDialogflowV2ExportOperationMetadataOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataIn": "_dialogflow_86_GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataOut": "_dialogflow_87_GoogleCloudDialogflowCxV3BatchRunTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3ExportFlowRequestIn": "_dialogflow_88_GoogleCloudDialogflowCxV3ExportFlowRequestIn",
        "GoogleCloudDialogflowCxV3ExportFlowRequestOut": "_dialogflow_89_GoogleCloudDialogflowCxV3ExportFlowRequestOut",
        "GoogleCloudDialogflowV3alpha1TurnSignalsIn": "_dialogflow_90_GoogleCloudDialogflowV3alpha1TurnSignalsIn",
        "GoogleCloudDialogflowV3alpha1TurnSignalsOut": "_dialogflow_91_GoogleCloudDialogflowV3alpha1TurnSignalsOut",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseIn": "_dialogflow_92_GoogleCloudDialogflowCxV3beta1WebhookResponseIn",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseOut": "_dialogflow_93_GoogleCloudDialogflowCxV3beta1WebhookResponseOut",
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn": "_dialogflow_94_GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut": "_dialogflow_95_GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowV2IntentIn": "_dialogflow_96_GoogleCloudDialogflowV2IntentIn",
        "GoogleCloudDialogflowV2IntentOut": "_dialogflow_97_GoogleCloudDialogflowV2IntentOut",
        "GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn": "_dialogflow_98_GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn",
        "GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut": "_dialogflow_99_GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut",
        "GoogleCloudDialogflowCxV3beta1PageIn": "_dialogflow_100_GoogleCloudDialogflowCxV3beta1PageIn",
        "GoogleCloudDialogflowCxV3beta1PageOut": "_dialogflow_101_GoogleCloudDialogflowCxV3beta1PageOut",
        "GoogleCloudDialogflowV2SentimentIn": "_dialogflow_102_GoogleCloudDialogflowV2SentimentIn",
        "GoogleCloudDialogflowV2SentimentOut": "_dialogflow_103_GoogleCloudDialogflowV2SentimentOut",
        "GoogleCloudDialogflowV2MessageIn": "_dialogflow_104_GoogleCloudDialogflowV2MessageIn",
        "GoogleCloudDialogflowV2MessageOut": "_dialogflow_105_GoogleCloudDialogflowV2MessageOut",
        "GoogleCloudDialogflowV2ConversationModelIn": "_dialogflow_106_GoogleCloudDialogflowV2ConversationModelIn",
        "GoogleCloudDialogflowV2ConversationModelOut": "_dialogflow_107_GoogleCloudDialogflowV2ConversationModelOut",
        "GoogleCloudDialogflowCxV3TestCaseIn": "_dialogflow_108_GoogleCloudDialogflowCxV3TestCaseIn",
        "GoogleCloudDialogflowCxV3TestCaseOut": "_dialogflow_109_GoogleCloudDialogflowCxV3TestCaseOut",
        "GoogleCloudDialogflowCxV3ExportFlowResponseIn": "_dialogflow_110_GoogleCloudDialogflowCxV3ExportFlowResponseIn",
        "GoogleCloudDialogflowCxV3ExportFlowResponseOut": "_dialogflow_111_GoogleCloudDialogflowCxV3ExportFlowResponseOut",
        "GoogleCloudDialogflowCxV3StopExperimentRequestIn": "_dialogflow_112_GoogleCloudDialogflowCxV3StopExperimentRequestIn",
        "GoogleCloudDialogflowCxV3StopExperimentRequestOut": "_dialogflow_113_GoogleCloudDialogflowCxV3StopExperimentRequestOut",
        "GoogleCloudDialogflowCxV3beta1AudioInputIn": "_dialogflow_114_GoogleCloudDialogflowCxV3beta1AudioInputIn",
        "GoogleCloudDialogflowCxV3beta1AudioInputOut": "_dialogflow_115_GoogleCloudDialogflowCxV3beta1AudioInputOut",
        "GoogleCloudDialogflowCxV3PageInfoIn": "_dialogflow_116_GoogleCloudDialogflowCxV3PageInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoOut": "_dialogflow_117_GoogleCloudDialogflowCxV3PageInfoOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentIn": "_dialogflow_118_GoogleCloudDialogflowCxV3beta1FulfillmentIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentOut": "_dialogflow_119_GoogleCloudDialogflowCxV3beta1FulfillmentOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn": "_dialogflow_120_GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut": "_dialogflow_121_GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut",
        "GoogleCloudDialogflowCxV3DetectIntentResponseIn": "_dialogflow_122_GoogleCloudDialogflowCxV3DetectIntentResponseIn",
        "GoogleCloudDialogflowCxV3DetectIntentResponseOut": "_dialogflow_123_GoogleCloudDialogflowCxV3DetectIntentResponseOut",
        "GoogleCloudDialogflowV2BatchUpdateIntentsResponseIn": "_dialogflow_124_GoogleCloudDialogflowV2BatchUpdateIntentsResponseIn",
        "GoogleCloudDialogflowV2BatchUpdateIntentsResponseOut": "_dialogflow_125_GoogleCloudDialogflowV2BatchUpdateIntentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1ConversationSignalsIn": "_dialogflow_126_GoogleCloudDialogflowCxV3beta1ConversationSignalsIn",
        "GoogleCloudDialogflowCxV3beta1ConversationSignalsOut": "_dialogflow_127_GoogleCloudDialogflowCxV3beta1ConversationSignalsOut",
        "GoogleCloudDialogflowCxV3RunTestCaseRequestIn": "_dialogflow_128_GoogleCloudDialogflowCxV3RunTestCaseRequestIn",
        "GoogleCloudDialogflowCxV3RunTestCaseRequestOut": "_dialogflow_129_GoogleCloudDialogflowCxV3RunTestCaseRequestOut",
        "GoogleCloudDialogflowCxV3ResponseMessageIn": "_dialogflow_130_GoogleCloudDialogflowCxV3ResponseMessageIn",
        "GoogleCloudDialogflowCxV3ResponseMessageOut": "_dialogflow_131_GoogleCloudDialogflowCxV3ResponseMessageOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn": "_dialogflow_132_GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut": "_dialogflow_133_GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataIn": "_dialogflow_134_GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataOut": "_dialogflow_135_GoogleCloudDialogflowV3alpha1DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataIn": "_dialogflow_136_GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut": "_dialogflow_137_GoogleCloudDialogflowV2beta1KnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowV2OriginalDetectIntentRequestIn": "_dialogflow_138_GoogleCloudDialogflowV2OriginalDetectIntentRequestIn",
        "GoogleCloudDialogflowV2OriginalDetectIntentRequestOut": "_dialogflow_139_GoogleCloudDialogflowV2OriginalDetectIntentRequestOut",
        "GoogleCloudDialogflowCxV3ExperimentResultMetricIn": "_dialogflow_140_GoogleCloudDialogflowCxV3ExperimentResultMetricIn",
        "GoogleCloudDialogflowCxV3ExperimentResultMetricOut": "_dialogflow_141_GoogleCloudDialogflowCxV3ExperimentResultMetricOut",
        "GoogleCloudDialogflowCxV3ImportDocumentsResponseIn": "_dialogflow_142_GoogleCloudDialogflowCxV3ImportDocumentsResponseIn",
        "GoogleCloudDialogflowCxV3ImportDocumentsResponseOut": "_dialogflow_143_GoogleCloudDialogflowCxV3ImportDocumentsResponseOut",
        "GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataIn": "_dialogflow_144_GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataOut": "_dialogflow_145_GoogleCloudDialogflowCxV3UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn": "_dialogflow_146_GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut": "_dialogflow_147_GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageIn": "_dialogflow_148_GoogleCloudDialogflowV2beta1IntentMessageIn",
        "GoogleCloudDialogflowV2beta1IntentMessageOut": "_dialogflow_149_GoogleCloudDialogflowV2beta1IntentMessageOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn": "_dialogflow_150_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut": "_dialogflow_151_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut",
        "GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn": "_dialogflow_152_GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn",
        "GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut": "_dialogflow_153_GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut",
        "GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn": "_dialogflow_154_GoogleCloudDialogflowCxV3beta1DeployFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut": "_dialogflow_155_GoogleCloudDialogflowCxV3beta1DeployFlowResponseOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIn": "_dialogflow_156_GoogleCloudDialogflowCxV3beta1WebhookRequestIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestOut": "_dialogflow_157_GoogleCloudDialogflowCxV3beta1WebhookRequestOut",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn": "_dialogflow_158_GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut": "_dialogflow_159_GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn": "_dialogflow_160_GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut": "_dialogflow_161_GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut",
        "GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataIn": "_dialogflow_162_GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataOut": "_dialogflow_163_GoogleCloudDialogflowCxV3beta1ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn": "_dialogflow_164_GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn",
        "GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut": "_dialogflow_165_GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseResultIn": "_dialogflow_166_GoogleCloudDialogflowCxV3beta1TestCaseResultIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseResultOut": "_dialogflow_167_GoogleCloudDialogflowCxV3beta1TestCaseResultOut",
        "GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn": "_dialogflow_168_GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsIn",
        "GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut": "_dialogflow_169_GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettingsOut",
        "GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn": "_dialogflow_170_GoogleCloudDialogflowCxV3beta1TestRunDifferenceIn",
        "GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut": "_dialogflow_171_GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataIn": "_dialogflow_172_GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataOut": "_dialogflow_173_GoogleCloudDialogflowCxV3beta1ImportDocumentsOperationMetadataOut",
        "GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn": "_dialogflow_174_GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut": "_dialogflow_175_GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentIn": "_dialogflow_176_GoogleCloudDialogflowCxV3beta1EnvironmentIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentOut": "_dialogflow_177_GoogleCloudDialogflowCxV3beta1EnvironmentOut",
        "GoogleCloudDialogflowCxV3beta1TestConfigIn": "_dialogflow_178_GoogleCloudDialogflowCxV3beta1TestConfigIn",
        "GoogleCloudDialogflowCxV3beta1TestConfigOut": "_dialogflow_179_GoogleCloudDialogflowCxV3beta1TestConfigOut",
        "GoogleCloudDialogflowCxV3EnvironmentIn": "_dialogflow_180_GoogleCloudDialogflowCxV3EnvironmentIn",
        "GoogleCloudDialogflowCxV3EnvironmentOut": "_dialogflow_181_GoogleCloudDialogflowCxV3EnvironmentOut",
        "GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn": "_dialogflow_182_GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut": "_dialogflow_183_GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3QueryParametersIn": "_dialogflow_184_GoogleCloudDialogflowCxV3QueryParametersIn",
        "GoogleCloudDialogflowCxV3QueryParametersOut": "_dialogflow_185_GoogleCloudDialogflowCxV3QueryParametersOut",
        "GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn": "_dialogflow_186_GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseIn",
        "GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut": "_dialogflow_187_GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut",
        "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn": "_dialogflow_188_GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallIn",
        "GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut": "_dialogflow_189_GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCallOut",
        "GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn": "_dialogflow_190_GoogleCloudDialogflowV2beta1AnnotatedMessagePartIn",
        "GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut": "_dialogflow_191_GoogleCloudDialogflowV2beta1AnnotatedMessagePartOut",
        "GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataIn": "_dialogflow_192_GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataOut": "_dialogflow_193_GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadataOut",
        "GoogleCloudDialogflowCxV3TestConfigIn": "_dialogflow_194_GoogleCloudDialogflowCxV3TestConfigIn",
        "GoogleCloudDialogflowCxV3TestConfigOut": "_dialogflow_195_GoogleCloudDialogflowCxV3TestConfigOut",
        "GoogleCloudDialogflowCxV3DeploymentIn": "_dialogflow_196_GoogleCloudDialogflowCxV3DeploymentIn",
        "GoogleCloudDialogflowCxV3DeploymentOut": "_dialogflow_197_GoogleCloudDialogflowCxV3DeploymentOut",
        "GoogleCloudDialogflowCxV3ExperimentIn": "_dialogflow_198_GoogleCloudDialogflowCxV3ExperimentIn",
        "GoogleCloudDialogflowCxV3ExperimentOut": "_dialogflow_199_GoogleCloudDialogflowCxV3ExperimentOut",
        "GoogleCloudDialogflowCxV3ValidationMessageIn": "_dialogflow_200_GoogleCloudDialogflowCxV3ValidationMessageIn",
        "GoogleCloudDialogflowCxV3ValidationMessageOut": "_dialogflow_201_GoogleCloudDialogflowCxV3ValidationMessageOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestMetadataIn": "_dialogflow_202_GoogleCloudDialogflowCxV3RunContinuousTestMetadataIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestMetadataOut": "_dialogflow_203_GoogleCloudDialogflowCxV3RunContinuousTestMetadataOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn": "_dialogflow_204_GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut": "_dialogflow_205_GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut",
        "GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn": "_dialogflow_206_GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn",
        "GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut": "_dialogflow_207_GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut",
        "GoogleCloudDialogflowCxV3ExperimentDefinitionIn": "_dialogflow_208_GoogleCloudDialogflowCxV3ExperimentDefinitionIn",
        "GoogleCloudDialogflowCxV3ExperimentDefinitionOut": "_dialogflow_209_GoogleCloudDialogflowCxV3ExperimentDefinitionOut",
        "GoogleCloudDialogflowCxV3TestCaseResultIn": "_dialogflow_210_GoogleCloudDialogflowCxV3TestCaseResultIn",
        "GoogleCloudDialogflowCxV3TestCaseResultOut": "_dialogflow_211_GoogleCloudDialogflowCxV3TestCaseResultOut",
        "GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn": "_dialogflow_212_GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut": "_dialogflow_213_GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut",
        "GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataIn": "_dialogflow_214_GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataOut": "_dialogflow_215_GoogleCloudDialogflowCxV3beta1UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesResponseIn": "_dialogflow_216_GoogleCloudDialogflowCxV3ImportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesResponseOut": "_dialogflow_217_GoogleCloudDialogflowCxV3ImportTestCasesResponseOut",
        "GoogleCloudDialogflowV2beta1ConversationEventIn": "_dialogflow_218_GoogleCloudDialogflowV2beta1ConversationEventIn",
        "GoogleCloudDialogflowV2beta1ConversationEventOut": "_dialogflow_219_GoogleCloudDialogflowV2beta1ConversationEventOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesResponseIn": "_dialogflow_220_GoogleCloudDialogflowCxV3BatchRunTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesResponseOut": "_dialogflow_221_GoogleCloudDialogflowCxV3BatchRunTestCasesResponseOut",
        "GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn": "_dialogflow_222_GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn",
        "GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut": "_dialogflow_223_GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut",
        "GoogleCloudDialogflowCxV3beta1DeployFlowMetadataIn": "_dialogflow_224_GoogleCloudDialogflowCxV3beta1DeployFlowMetadataIn",
        "GoogleCloudDialogflowCxV3beta1DeployFlowMetadataOut": "_dialogflow_225_GoogleCloudDialogflowCxV3beta1DeployFlowMetadataOut",
        "GoogleCloudDialogflowV2beta1WebhookRequestIn": "_dialogflow_226_GoogleCloudDialogflowV2beta1WebhookRequestIn",
        "GoogleCloudDialogflowV2beta1WebhookRequestOut": "_dialogflow_227_GoogleCloudDialogflowV2beta1WebhookRequestOut",
        "GoogleCloudDialogflowCxV3OutputAudioConfigIn": "_dialogflow_228_GoogleCloudDialogflowCxV3OutputAudioConfigIn",
        "GoogleCloudDialogflowCxV3OutputAudioConfigOut": "_dialogflow_229_GoogleCloudDialogflowCxV3OutputAudioConfigOut",
        "GoogleCloudDialogflowV2InputDatasetIn": "_dialogflow_230_GoogleCloudDialogflowV2InputDatasetIn",
        "GoogleCloudDialogflowV2InputDatasetOut": "_dialogflow_231_GoogleCloudDialogflowV2InputDatasetOut",
        "GoogleCloudDialogflowCxV3ListFlowsResponseIn": "_dialogflow_232_GoogleCloudDialogflowCxV3ListFlowsResponseIn",
        "GoogleCloudDialogflowCxV3ListFlowsResponseOut": "_dialogflow_233_GoogleCloudDialogflowCxV3ListFlowsResponseOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn": "_dialogflow_234_GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut": "_dialogflow_235_GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut",
        "GoogleCloudDialogflowV2SuggestionResultIn": "_dialogflow_236_GoogleCloudDialogflowV2SuggestionResultIn",
        "GoogleCloudDialogflowV2SuggestionResultOut": "_dialogflow_237_GoogleCloudDialogflowV2SuggestionResultOut",
        "GoogleCloudDialogflowCxV3ResourceNameIn": "_dialogflow_238_GoogleCloudDialogflowCxV3ResourceNameIn",
        "GoogleCloudDialogflowCxV3ResourceNameOut": "_dialogflow_239_GoogleCloudDialogflowCxV3ResourceNameOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardCellIn": "_dialogflow_240_GoogleCloudDialogflowV2IntentMessageTableCardCellIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardCellOut": "_dialogflow_241_GoogleCloudDialogflowV2IntentMessageTableCardCellOut",
        "GoogleCloudDialogflowCxV3FulfillmentIn": "_dialogflow_242_GoogleCloudDialogflowCxV3FulfillmentIn",
        "GoogleCloudDialogflowCxV3FulfillmentOut": "_dialogflow_243_GoogleCloudDialogflowCxV3FulfillmentOut",
        "GoogleCloudDialogflowV2EntityTypeIn": "_dialogflow_244_GoogleCloudDialogflowV2EntityTypeIn",
        "GoogleCloudDialogflowV2EntityTypeOut": "_dialogflow_245_GoogleCloudDialogflowV2EntityTypeOut",
        "GoogleCloudDialogflowV2GcsDestinationIn": "_dialogflow_246_GoogleCloudDialogflowV2GcsDestinationIn",
        "GoogleCloudDialogflowV2GcsDestinationOut": "_dialogflow_247_GoogleCloudDialogflowV2GcsDestinationOut",
        "GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn": "_dialogflow_248_GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn",
        "GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut": "_dialogflow_249_GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn": "_dialogflow_250_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut": "_dialogflow_251_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut",
        "GoogleCloudDialogflowCxV3IntentInputIn": "_dialogflow_252_GoogleCloudDialogflowCxV3IntentInputIn",
        "GoogleCloudDialogflowCxV3IntentInputOut": "_dialogflow_253_GoogleCloudDialogflowCxV3IntentInputOut",
        "GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseIn": "_dialogflow_254_GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseIn",
        "GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseOut": "_dialogflow_255_GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1IntentParameterIn": "_dialogflow_256_GoogleCloudDialogflowCxV3beta1IntentParameterIn",
        "GoogleCloudDialogflowCxV3beta1IntentParameterOut": "_dialogflow_257_GoogleCloudDialogflowCxV3beta1IntentParameterOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn": "_dialogflow_258_GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut": "_dialogflow_259_GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut",
        "GoogleCloudDialogflowCxV3QueryInputIn": "_dialogflow_260_GoogleCloudDialogflowCxV3QueryInputIn",
        "GoogleCloudDialogflowCxV3QueryInputOut": "_dialogflow_261_GoogleCloudDialogflowCxV3QueryInputOut",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn": "_dialogflow_262_GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn",
        "GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut": "_dialogflow_263_GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut",
        "GoogleCloudDialogflowCxV3ListTestCasesResponseIn": "_dialogflow_264_GoogleCloudDialogflowCxV3ListTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ListTestCasesResponseOut": "_dialogflow_265_GoogleCloudDialogflowCxV3ListTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataIn": "_dialogflow_266_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataOut": "_dialogflow_267_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadataOut",
        "GoogleCloudDialogflowV2beta1FaqAnswerIn": "_dialogflow_268_GoogleCloudDialogflowV2beta1FaqAnswerIn",
        "GoogleCloudDialogflowV2beta1FaqAnswerOut": "_dialogflow_269_GoogleCloudDialogflowV2beta1FaqAnswerOut",
        "GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn": "_dialogflow_270_GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn",
        "GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut": "_dialogflow_271_GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut",
        "GoogleCloudDialogflowCxV3IntentTrainingPhraseIn": "_dialogflow_272_GoogleCloudDialogflowCxV3IntentTrainingPhraseIn",
        "GoogleCloudDialogflowCxV3IntentTrainingPhraseOut": "_dialogflow_273_GoogleCloudDialogflowCxV3IntentTrainingPhraseOut",
        "GoogleLongrunningListOperationsResponseIn": "_dialogflow_274_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_dialogflow_275_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDialogflowV2beta1IntentIn": "_dialogflow_276_GoogleCloudDialogflowV2beta1IntentIn",
        "GoogleCloudDialogflowV2beta1IntentOut": "_dialogflow_277_GoogleCloudDialogflowV2beta1IntentOut",
        "GoogleCloudDialogflowCxV3ListPagesResponseIn": "_dialogflow_278_GoogleCloudDialogflowCxV3ListPagesResponseIn",
        "GoogleCloudDialogflowCxV3ListPagesResponseOut": "_dialogflow_279_GoogleCloudDialogflowCxV3ListPagesResponseOut",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn": "_dialogflow_280_GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut": "_dialogflow_281_GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn": "_dialogflow_282_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut": "_dialogflow_283_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn": "_dialogflow_284_GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut": "_dialogflow_285_GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn": "_dialogflow_286_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut": "_dialogflow_287_GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionOut",
        "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn": "_dialogflow_288_GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn",
        "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut": "_dialogflow_289_GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut",
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn": "_dialogflow_290_GoogleCloudDialogflowV2DeployConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut": "_dialogflow_291_GoogleCloudDialogflowV2DeployConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowCxV3SessionInfoIn": "_dialogflow_292_GoogleCloudDialogflowCxV3SessionInfoIn",
        "GoogleCloudDialogflowCxV3SessionInfoOut": "_dialogflow_293_GoogleCloudDialogflowCxV3SessionInfoOut",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn": "_dialogflow_294_GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut": "_dialogflow_295_GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut",
        "GoogleCloudDialogflowCxV3RestoreAgentRequestIn": "_dialogflow_296_GoogleCloudDialogflowCxV3RestoreAgentRequestIn",
        "GoogleCloudDialogflowCxV3RestoreAgentRequestOut": "_dialogflow_297_GoogleCloudDialogflowCxV3RestoreAgentRequestOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoIn": "_dialogflow_298_GoogleCloudDialogflowCxV3beta1PageInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoOut": "_dialogflow_299_GoogleCloudDialogflowCxV3beta1PageInfoOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn": "_dialogflow_300_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut": "_dialogflow_301_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn": "_dialogflow_302_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut": "_dialogflow_303_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegmentOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn": "_dialogflow_304_GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut": "_dialogflow_305_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn": "_dialogflow_306_GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut": "_dialogflow_307_GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn": "_dialogflow_308_GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut": "_dialogflow_309_GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut",
        "GoogleCloudDialogflowCxV3TransitionRouteIn": "_dialogflow_310_GoogleCloudDialogflowCxV3TransitionRouteIn",
        "GoogleCloudDialogflowCxV3TransitionRouteOut": "_dialogflow_311_GoogleCloudDialogflowCxV3TransitionRouteOut",
        "GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn": "_dialogflow_312_GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsIn",
        "GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut": "_dialogflow_313_GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsOut",
        "GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn": "_dialogflow_314_GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn",
        "GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut": "_dialogflow_315_GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut",
        "GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn": "_dialogflow_316_GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn",
        "GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut": "_dialogflow_317_GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectIn": "_dialogflow_318_GoogleCloudDialogflowV2IntentMessageCarouselSelectIn",
        "GoogleCloudDialogflowV2IntentMessageCarouselSelectOut": "_dialogflow_319_GoogleCloudDialogflowV2IntentMessageCarouselSelectOut",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoIn": "_dialogflow_320_GoogleCloudDialogflowCxV3PageInfoFormInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoOut": "_dialogflow_321_GoogleCloudDialogflowCxV3PageInfoFormInfoOut",
        "GoogleCloudDialogflowCxV3beta1EventInputIn": "_dialogflow_322_GoogleCloudDialogflowCxV3beta1EventInputIn",
        "GoogleCloudDialogflowCxV3beta1EventInputOut": "_dialogflow_323_GoogleCloudDialogflowCxV3beta1EventInputOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIn": "_dialogflow_324_GoogleCloudDialogflowCxV3WebhookRequestIn",
        "GoogleCloudDialogflowCxV3WebhookRequestOut": "_dialogflow_325_GoogleCloudDialogflowCxV3WebhookRequestOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn": "_dialogflow_326_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut": "_dialogflow_327_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut",
        "GoogleCloudDialogflowCxV3ContinuousTestResultIn": "_dialogflow_328_GoogleCloudDialogflowCxV3ContinuousTestResultIn",
        "GoogleCloudDialogflowCxV3ContinuousTestResultOut": "_dialogflow_329_GoogleCloudDialogflowCxV3ContinuousTestResultOut",
        "GoogleCloudDialogflowCxV3beta1TransitionRouteIn": "_dialogflow_330_GoogleCloudDialogflowCxV3beta1TransitionRouteIn",
        "GoogleCloudDialogflowCxV3beta1TransitionRouteOut": "_dialogflow_331_GoogleCloudDialogflowCxV3beta1TransitionRouteOut",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn": "_dialogflow_332_GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut": "_dialogflow_333_GoogleCloudDialogflowCxV3beta1ExportTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupIn": "_dialogflow_334_GoogleCloudDialogflowCxV3TransitionRouteGroupIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupOut": "_dialogflow_335_GoogleCloudDialogflowCxV3TransitionRouteGroupOut",
        "GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn": "_dialogflow_336_GoogleCloudDialogflowCxV3IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut": "_dialogflow_337_GoogleCloudDialogflowCxV3IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowCxV3IntentCoverageIn": "_dialogflow_338_GoogleCloudDialogflowCxV3IntentCoverageIn",
        "GoogleCloudDialogflowCxV3IntentCoverageOut": "_dialogflow_339_GoogleCloudDialogflowCxV3IntentCoverageOut",
        "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn": "_dialogflow_340_GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn",
        "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut": "_dialogflow_341_GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut",
        "GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn": "_dialogflow_342_GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut": "_dialogflow_343_GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn": "_dialogflow_344_GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut": "_dialogflow_345_GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut",
        "GoogleCloudDialogflowV2IntentMessageListSelectIn": "_dialogflow_346_GoogleCloudDialogflowV2IntentMessageListSelectIn",
        "GoogleCloudDialogflowV2IntentMessageListSelectOut": "_dialogflow_347_GoogleCloudDialogflowV2IntentMessageListSelectOut",
        "GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn": "_dialogflow_348_GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn",
        "GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut": "_dialogflow_349_GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut",
        "GoogleCloudDialogflowCxV3RunTestCaseResponseIn": "_dialogflow_350_GoogleCloudDialogflowCxV3RunTestCaseResponseIn",
        "GoogleCloudDialogflowCxV3RunTestCaseResponseOut": "_dialogflow_351_GoogleCloudDialogflowCxV3RunTestCaseResponseOut",
        "GoogleCloudDialogflowCxV3ImportFlowRequestIn": "_dialogflow_352_GoogleCloudDialogflowCxV3ImportFlowRequestIn",
        "GoogleCloudDialogflowCxV3ImportFlowRequestOut": "_dialogflow_353_GoogleCloudDialogflowCxV3ImportFlowRequestOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestRequestIn": "_dialogflow_354_GoogleCloudDialogflowCxV3RunContinuousTestRequestIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestRequestOut": "_dialogflow_355_GoogleCloudDialogflowCxV3RunContinuousTestRequestOut",
        "GoogleLongrunningOperationIn": "_dialogflow_356_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_dialogflow_357_GoogleLongrunningOperationOut",
        "GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn": "_dialogflow_358_GoogleCloudDialogflowCxV3beta1ExportFlowResponseIn",
        "GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut": "_dialogflow_359_GoogleCloudDialogflowCxV3beta1ExportFlowResponseOut",
        "GoogleCloudDialogflowV2beta1MessageIn": "_dialogflow_360_GoogleCloudDialogflowV2beta1MessageIn",
        "GoogleCloudDialogflowV2beta1MessageOut": "_dialogflow_361_GoogleCloudDialogflowV2beta1MessageOut",
        "GoogleCloudDialogflowCxV3beta1TestErrorIn": "_dialogflow_362_GoogleCloudDialogflowCxV3beta1TestErrorIn",
        "GoogleCloudDialogflowCxV3beta1TestErrorOut": "_dialogflow_363_GoogleCloudDialogflowCxV3beta1TestErrorOut",
        "GoogleCloudDialogflowCxV3ExperimentResultIn": "_dialogflow_364_GoogleCloudDialogflowCxV3ExperimentResultIn",
        "GoogleCloudDialogflowCxV3ExperimentResultOut": "_dialogflow_365_GoogleCloudDialogflowCxV3ExperimentResultOut",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseIn": "_dialogflow_366_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseOut": "_dialogflow_367_GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponseOut",
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_368_GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_369_GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowCxV3RunContinuousTestResponseIn": "_dialogflow_370_GoogleCloudDialogflowCxV3RunContinuousTestResponseIn",
        "GoogleCloudDialogflowCxV3RunContinuousTestResponseOut": "_dialogflow_371_GoogleCloudDialogflowCxV3RunContinuousTestResponseOut",
        "GoogleCloudDialogflowCxV3AgentIn": "_dialogflow_372_GoogleCloudDialogflowCxV3AgentIn",
        "GoogleCloudDialogflowCxV3AgentOut": "_dialogflow_373_GoogleCloudDialogflowCxV3AgentOut",
        "GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn": "_dialogflow_374_GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut": "_dialogflow_375_GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut",
        "GoogleCloudDialogflowCxV3ListChangelogsResponseIn": "_dialogflow_376_GoogleCloudDialogflowCxV3ListChangelogsResponseIn",
        "GoogleCloudDialogflowCxV3ListChangelogsResponseOut": "_dialogflow_377_GoogleCloudDialogflowCxV3ListChangelogsResponseOut",
        "GoogleCloudDialogflowCxV3TextInputIn": "_dialogflow_378_GoogleCloudDialogflowCxV3TextInputIn",
        "GoogleCloudDialogflowCxV3TextInputOut": "_dialogflow_379_GoogleCloudDialogflowCxV3TextInputOut",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn": "_dialogflow_380_GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut": "_dialogflow_381_GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3ValidateAgentRequestIn": "_dialogflow_382_GoogleCloudDialogflowCxV3ValidateAgentRequestIn",
        "GoogleCloudDialogflowCxV3ValidateAgentRequestOut": "_dialogflow_383_GoogleCloudDialogflowCxV3ValidateAgentRequestOut",
        "GoogleCloudDialogflowCxV3beta1FormParameterIn": "_dialogflow_384_GoogleCloudDialogflowCxV3beta1FormParameterIn",
        "GoogleCloudDialogflowCxV3beta1FormParameterOut": "_dialogflow_385_GoogleCloudDialogflowCxV3beta1FormParameterOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn": "_dialogflow_386_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut": "_dialogflow_387_GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriActionOut",
        "GoogleCloudDialogflowCxV3beta1EventHandlerIn": "_dialogflow_388_GoogleCloudDialogflowCxV3beta1EventHandlerIn",
        "GoogleCloudDialogflowCxV3beta1EventHandlerOut": "_dialogflow_389_GoogleCloudDialogflowCxV3beta1EventHandlerOut",
        "GoogleCloudDialogflowV2IntentMessageBasicCardIn": "_dialogflow_390_GoogleCloudDialogflowV2IntentMessageBasicCardIn",
        "GoogleCloudDialogflowV2IntentMessageBasicCardOut": "_dialogflow_391_GoogleCloudDialogflowV2IntentMessageBasicCardOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueIn": "_dialogflow_392_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueOut": "_dialogflow_393_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValueOut",
        "GoogleCloudDialogflowCxV3ImportFlowResponseIn": "_dialogflow_394_GoogleCloudDialogflowCxV3ImportFlowResponseIn",
        "GoogleCloudDialogflowCxV3ImportFlowResponseOut": "_dialogflow_395_GoogleCloudDialogflowCxV3ImportFlowResponseOut",
        "GoogleCloudDialogflowCxV3beta1TurnSignalsIn": "_dialogflow_396_GoogleCloudDialogflowCxV3beta1TurnSignalsIn",
        "GoogleCloudDialogflowCxV3beta1TurnSignalsOut": "_dialogflow_397_GoogleCloudDialogflowCxV3beta1TurnSignalsOut",
        "GoogleCloudDialogflowV2ConversationEventIn": "_dialogflow_398_GoogleCloudDialogflowV2ConversationEventIn",
        "GoogleCloudDialogflowV2ConversationEventOut": "_dialogflow_399_GoogleCloudDialogflowV2ConversationEventOut",
        "GoogleCloudDialogflowV2beta1EntityTypeEntityIn": "_dialogflow_400_GoogleCloudDialogflowV2beta1EntityTypeEntityIn",
        "GoogleCloudDialogflowV2beta1EntityTypeEntityOut": "_dialogflow_401_GoogleCloudDialogflowV2beta1EntityTypeEntityOut",
        "GoogleCloudDialogflowCxV3QueryResultIn": "_dialogflow_402_GoogleCloudDialogflowCxV3QueryResultIn",
        "GoogleCloudDialogflowCxV3QueryResultOut": "_dialogflow_403_GoogleCloudDialogflowCxV3QueryResultOut",
        "GoogleCloudDialogflowCxV3MatchIntentResponseIn": "_dialogflow_404_GoogleCloudDialogflowCxV3MatchIntentResponseIn",
        "GoogleCloudDialogflowCxV3MatchIntentResponseOut": "_dialogflow_405_GoogleCloudDialogflowCxV3MatchIntentResponseOut",
        "GoogleCloudDialogflowV2beta1SessionEntityTypeIn": "_dialogflow_406_GoogleCloudDialogflowV2beta1SessionEntityTypeIn",
        "GoogleCloudDialogflowV2beta1SessionEntityTypeOut": "_dialogflow_407_GoogleCloudDialogflowV2beta1SessionEntityTypeOut",
        "GoogleCloudDialogflowCxV3MatchIntentRequestIn": "_dialogflow_408_GoogleCloudDialogflowCxV3MatchIntentRequestIn",
        "GoogleCloudDialogflowCxV3MatchIntentRequestOut": "_dialogflow_409_GoogleCloudDialogflowCxV3MatchIntentRequestOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageIn": "_dialogflow_410_GoogleCloudDialogflowCxV3TransitionCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageOut": "_dialogflow_411_GoogleCloudDialogflowCxV3TransitionCoverageOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn": "_dialogflow_412_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut": "_dialogflow_413_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut",
        "GoogleCloudDialogflowCxV3ExportAgentRequestIn": "_dialogflow_414_GoogleCloudDialogflowCxV3ExportAgentRequestIn",
        "GoogleCloudDialogflowCxV3ExportAgentRequestOut": "_dialogflow_415_GoogleCloudDialogflowCxV3ExportAgentRequestOut",
        "GoogleCloudDialogflowCxV3FlowValidationResultIn": "_dialogflow_416_GoogleCloudDialogflowCxV3FlowValidationResultIn",
        "GoogleCloudDialogflowCxV3FlowValidationResultOut": "_dialogflow_417_GoogleCloudDialogflowCxV3FlowValidationResultOut",
        "GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataIn": "_dialogflow_418_GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataOut": "_dialogflow_419_GoogleCloudDialogflowV3alpha1CreateDocumentOperationMetadataOut",
        "GoogleProtobufEmptyIn": "_dialogflow_420_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_dialogflow_421_GoogleProtobufEmptyOut",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataIn": "_dialogflow_422_GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataOut": "_dialogflow_423_GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioIn": "_dialogflow_424_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut": "_dialogflow_425_GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut",
        "GoogleCloudDialogflowV2beta1SmartReplyAnswerIn": "_dialogflow_426_GoogleCloudDialogflowV2beta1SmartReplyAnswerIn",
        "GoogleCloudDialogflowV2beta1SmartReplyAnswerOut": "_dialogflow_427_GoogleCloudDialogflowV2beta1SmartReplyAnswerOut",
        "GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseIn": "_dialogflow_428_GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseIn",
        "GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseOut": "_dialogflow_429_GoogleCloudDialogflowV2BatchUpdateEntityTypesResponseOut",
        "GoogleCloudDialogflowV2beta1ArticleAnswerIn": "_dialogflow_430_GoogleCloudDialogflowV2beta1ArticleAnswerIn",
        "GoogleCloudDialogflowV2beta1ArticleAnswerOut": "_dialogflow_431_GoogleCloudDialogflowV2beta1ArticleAnswerOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn": "_dialogflow_432_GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut": "_dialogflow_433_GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn": "_dialogflow_434_GoogleCloudDialogflowCxV3BatchRunTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut": "_dialogflow_435_GoogleCloudDialogflowCxV3BatchRunTestCasesRequestOut",
        "GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn": "_dialogflow_436_GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn",
        "GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut": "_dialogflow_437_GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut",
        "GoogleCloudDialogflowCxV3SpeechToTextSettingsIn": "_dialogflow_438_GoogleCloudDialogflowCxV3SpeechToTextSettingsIn",
        "GoogleCloudDialogflowCxV3SpeechToTextSettingsOut": "_dialogflow_439_GoogleCloudDialogflowCxV3SpeechToTextSettingsOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn": "_dialogflow_440_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut": "_dialogflow_441_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn": "_dialogflow_442_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut": "_dialogflow_443_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn": "_dialogflow_444_GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut": "_dialogflow_445_GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut",
        "GoogleCloudDialogflowCxV3VersionIn": "_dialogflow_446_GoogleCloudDialogflowCxV3VersionIn",
        "GoogleCloudDialogflowCxV3VersionOut": "_dialogflow_447_GoogleCloudDialogflowCxV3VersionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectIn": "_dialogflow_448_GoogleCloudDialogflowV2beta1IntentMessageListSelectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectOut": "_dialogflow_449_GoogleCloudDialogflowV2beta1IntentMessageListSelectOut",
        "GoogleCloudDialogflowCxV3IntentCoverageIntentIn": "_dialogflow_450_GoogleCloudDialogflowCxV3IntentCoverageIntentIn",
        "GoogleCloudDialogflowCxV3IntentCoverageIntentOut": "_dialogflow_451_GoogleCloudDialogflowCxV3IntentCoverageIntentOut",
        "GoogleCloudDialogflowCxV3ConversationTurnIn": "_dialogflow_452_GoogleCloudDialogflowCxV3ConversationTurnIn",
        "GoogleCloudDialogflowCxV3ConversationTurnOut": "_dialogflow_453_GoogleCloudDialogflowCxV3ConversationTurnOut",
        "GoogleCloudDialogflowV2beta1GcsDestinationIn": "_dialogflow_454_GoogleCloudDialogflowV2beta1GcsDestinationIn",
        "GoogleCloudDialogflowV2beta1GcsDestinationOut": "_dialogflow_455_GoogleCloudDialogflowV2beta1GcsDestinationOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardRowIn": "_dialogflow_456_GoogleCloudDialogflowV2IntentMessageTableCardRowIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardRowOut": "_dialogflow_457_GoogleCloudDialogflowV2IntentMessageTableCardRowOut",
        "GoogleCloudLocationLocationIn": "_dialogflow_458_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_dialogflow_459_GoogleCloudLocationLocationOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn": "_dialogflow_460_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut": "_dialogflow_461_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnIn": "_dialogflow_462_GoogleCloudDialogflowCxV3beta1ConversationTurnIn",
        "GoogleCloudDialogflowCxV3beta1ConversationTurnOut": "_dialogflow_463_GoogleCloudDialogflowCxV3beta1ConversationTurnOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn": "_dialogflow_464_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut": "_dialogflow_465_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut",
        "GoogleCloudDialogflowCxV3DeployFlowRequestIn": "_dialogflow_466_GoogleCloudDialogflowCxV3DeployFlowRequestIn",
        "GoogleCloudDialogflowCxV3DeployFlowRequestOut": "_dialogflow_467_GoogleCloudDialogflowCxV3DeployFlowRequestOut",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn": "_dialogflow_468_GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut": "_dialogflow_469_GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn": "_dialogflow_470_GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut": "_dialogflow_471_GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn": "_dialogflow_472_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut": "_dialogflow_473_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut",
        "GoogleCloudDialogflowCxV3beta1TestCaseIn": "_dialogflow_474_GoogleCloudDialogflowCxV3beta1TestCaseIn",
        "GoogleCloudDialogflowCxV3beta1TestCaseOut": "_dialogflow_475_GoogleCloudDialogflowCxV3beta1TestCaseOut",
        "GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn": "_dialogflow_476_GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn",
        "GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut": "_dialogflow_477_GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut",
        "GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataIn": "_dialogflow_478_GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataOut": "_dialogflow_479_GoogleCloudDialogflowCxV3ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn": "_dialogflow_480_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut": "_dialogflow_481_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn": "_dialogflow_482_GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut": "_dialogflow_483_GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut",
        "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn": "_dialogflow_484_GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut": "_dialogflow_485_GoogleCloudDialogflowCxV3beta1GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1DtmfInputIn": "_dialogflow_486_GoogleCloudDialogflowCxV3beta1DtmfInputIn",
        "GoogleCloudDialogflowCxV3beta1DtmfInputOut": "_dialogflow_487_GoogleCloudDialogflowCxV3beta1DtmfInputOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn": "_dialogflow_488_GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut": "_dialogflow_489_GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut",
        "GoogleCloudDialogflowV2HumanAgentAssistantEventIn": "_dialogflow_490_GoogleCloudDialogflowV2HumanAgentAssistantEventIn",
        "GoogleCloudDialogflowV2HumanAgentAssistantEventOut": "_dialogflow_491_GoogleCloudDialogflowV2HumanAgentAssistantEventOut",
        "GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataIn": "_dialogflow_492_GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataOut": "_dialogflow_493_GoogleCloudDialogflowV3alpha1ReloadDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn": "_dialogflow_494_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut": "_dialogflow_495_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReplyOut",
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn": "_dialogflow_496_GoogleCloudDialogflowV2CreateConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut": "_dialogflow_497_GoogleCloudDialogflowV2CreateConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn": "_dialogflow_498_GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn",
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut": "_dialogflow_499_GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut",
        "GoogleCloudDialogflowCxV3ListEntityTypesResponseIn": "_dialogflow_500_GoogleCloudDialogflowCxV3ListEntityTypesResponseIn",
        "GoogleCloudDialogflowCxV3ListEntityTypesResponseOut": "_dialogflow_501_GoogleCloudDialogflowCxV3ListEntityTypesResponseOut",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn": "_dialogflow_502_GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn",
        "GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut": "_dialogflow_503_GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut",
        "GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn": "_dialogflow_504_GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn",
        "GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut": "_dialogflow_505_GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut",
        "GoogleCloudDialogflowV2IntentMessageTextIn": "_dialogflow_506_GoogleCloudDialogflowV2IntentMessageTextIn",
        "GoogleCloudDialogflowV2IntentMessageTextOut": "_dialogflow_507_GoogleCloudDialogflowV2IntentMessageTextOut",
        "GoogleCloudDialogflowCxV3ValidateFlowRequestIn": "_dialogflow_508_GoogleCloudDialogflowCxV3ValidateFlowRequestIn",
        "GoogleCloudDialogflowCxV3ValidateFlowRequestOut": "_dialogflow_509_GoogleCloudDialogflowCxV3ValidateFlowRequestOut",
        "GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataIn": "_dialogflow_510_GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataOut": "_dialogflow_511_GoogleCloudDialogflowCxV3DeleteDocumentOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn": "_dialogflow_512_GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut": "_dialogflow_513_GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn": "_dialogflow_514_GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn",
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut": "_dialogflow_515_GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut",
        "GoogleCloudDialogflowV2QueryResultIn": "_dialogflow_516_GoogleCloudDialogflowV2QueryResultIn",
        "GoogleCloudDialogflowV2QueryResultOut": "_dialogflow_517_GoogleCloudDialogflowV2QueryResultOut",
        "GoogleCloudDialogflowCxV3beta1InputAudioConfigIn": "_dialogflow_518_GoogleCloudDialogflowCxV3beta1InputAudioConfigIn",
        "GoogleCloudDialogflowCxV3beta1InputAudioConfigOut": "_dialogflow_519_GoogleCloudDialogflowCxV3beta1InputAudioConfigOut",
        "GoogleCloudDialogflowV2beta1ExportAgentResponseIn": "_dialogflow_520_GoogleCloudDialogflowV2beta1ExportAgentResponseIn",
        "GoogleCloudDialogflowV2beta1ExportAgentResponseOut": "_dialogflow_521_GoogleCloudDialogflowV2beta1ExportAgentResponseOut",
        "GoogleCloudDialogflowCxV3ListAgentsResponseIn": "_dialogflow_522_GoogleCloudDialogflowCxV3ListAgentsResponseIn",
        "GoogleCloudDialogflowCxV3ListAgentsResponseOut": "_dialogflow_523_GoogleCloudDialogflowCxV3ListAgentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn": "_dialogflow_524_GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut": "_dialogflow_525_GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut",
        "GoogleCloudDialogflowCxV3ListIntentsResponseIn": "_dialogflow_526_GoogleCloudDialogflowCxV3ListIntentsResponseIn",
        "GoogleCloudDialogflowCxV3ListIntentsResponseOut": "_dialogflow_527_GoogleCloudDialogflowCxV3ListIntentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn": "_dialogflow_528_GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut": "_dialogflow_529_GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut",
        "GoogleCloudDialogflowV2IntentMessageQuickRepliesIn": "_dialogflow_530_GoogleCloudDialogflowV2IntentMessageQuickRepliesIn",
        "GoogleCloudDialogflowV2IntentMessageQuickRepliesOut": "_dialogflow_531_GoogleCloudDialogflowV2IntentMessageQuickRepliesOut",
        "GoogleCloudDialogflowV2SmartReplyAnswerIn": "_dialogflow_532_GoogleCloudDialogflowV2SmartReplyAnswerIn",
        "GoogleCloudDialogflowV2SmartReplyAnswerOut": "_dialogflow_533_GoogleCloudDialogflowV2SmartReplyAnswerOut",
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn": "_dialogflow_534_GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn",
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut": "_dialogflow_535_GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut",
        "GoogleCloudDialogflowV2FaqAnswerIn": "_dialogflow_536_GoogleCloudDialogflowV2FaqAnswerIn",
        "GoogleCloudDialogflowV2FaqAnswerOut": "_dialogflow_537_GoogleCloudDialogflowV2FaqAnswerOut",
        "GoogleCloudDialogflowCxV3SessionEntityTypeIn": "_dialogflow_538_GoogleCloudDialogflowCxV3SessionEntityTypeIn",
        "GoogleCloudDialogflowCxV3SessionEntityTypeOut": "_dialogflow_539_GoogleCloudDialogflowCxV3SessionEntityTypeOut",
        "GoogleCloudDialogflowCxV3ListVersionsResponseIn": "_dialogflow_540_GoogleCloudDialogflowCxV3ListVersionsResponseIn",
        "GoogleCloudDialogflowCxV3ListVersionsResponseOut": "_dialogflow_541_GoogleCloudDialogflowCxV3ListVersionsResponseOut",
        "GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn": "_dialogflow_542_GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn",
        "GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut": "_dialogflow_543_GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut",
        "GoogleCloudDialogflowV2beta1IntentMessageImageIn": "_dialogflow_544_GoogleCloudDialogflowV2beta1IntentMessageImageIn",
        "GoogleCloudDialogflowV2beta1IntentMessageImageOut": "_dialogflow_545_GoogleCloudDialogflowV2beta1IntentMessageImageOut",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseResponseIn": "_dialogflow_546_GoogleCloudDialogflowCxV3beta1RunTestCaseResponseIn",
        "GoogleCloudDialogflowCxV3beta1RunTestCaseResponseOut": "_dialogflow_547_GoogleCloudDialogflowCxV3beta1RunTestCaseResponseOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn": "_dialogflow_548_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut": "_dialogflow_549_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentOut",
        "GoogleCloudDialogflowCxV3IntentParameterIn": "_dialogflow_550_GoogleCloudDialogflowCxV3IntentParameterIn",
        "GoogleCloudDialogflowCxV3IntentParameterOut": "_dialogflow_551_GoogleCloudDialogflowCxV3IntentParameterOut",
        "GoogleCloudDialogflowCxV3StartExperimentRequestIn": "_dialogflow_552_GoogleCloudDialogflowCxV3StartExperimentRequestIn",
        "GoogleCloudDialogflowCxV3StartExperimentRequestOut": "_dialogflow_553_GoogleCloudDialogflowCxV3StartExperimentRequestOut",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn": "_dialogflow_554_GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut": "_dialogflow_555_GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3ListExperimentsResponseIn": "_dialogflow_556_GoogleCloudDialogflowCxV3ListExperimentsResponseIn",
        "GoogleCloudDialogflowCxV3ListExperimentsResponseOut": "_dialogflow_557_GoogleCloudDialogflowCxV3ListExperimentsResponseOut",
        "GoogleCloudDialogflowCxV3TrainFlowRequestIn": "_dialogflow_558_GoogleCloudDialogflowCxV3TrainFlowRequestIn",
        "GoogleCloudDialogflowCxV3TrainFlowRequestOut": "_dialogflow_559_GoogleCloudDialogflowCxV3TrainFlowRequestOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn": "_dialogflow_560_GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut": "_dialogflow_561_GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut",
        "GoogleCloudDialogflowCxV3ResponseMessageTextIn": "_dialogflow_562_GoogleCloudDialogflowCxV3ResponseMessageTextIn",
        "GoogleCloudDialogflowCxV3ResponseMessageTextOut": "_dialogflow_563_GoogleCloudDialogflowCxV3ResponseMessageTextOut",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn": "_dialogflow_564_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn",
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut": "_dialogflow_565_GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut",
        "GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn": "_dialogflow_566_GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn",
        "GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut": "_dialogflow_567_GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut",
        "GoogleCloudDialogflowCxV3ListSecuritySettingsResponseIn": "_dialogflow_568_GoogleCloudDialogflowCxV3ListSecuritySettingsResponseIn",
        "GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut": "_dialogflow_569_GoogleCloudDialogflowCxV3ListSecuritySettingsResponseOut",
        "GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn": "_dialogflow_570_GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut": "_dialogflow_571_GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn": "_dialogflow_572_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut": "_dialogflow_573_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut",
        "GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseIn": "_dialogflow_574_GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseIn",
        "GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut": "_dialogflow_575_GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn": "_dialogflow_576_GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut": "_dialogflow_577_GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn": "_dialogflow_578_GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseIn",
        "GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut": "_dialogflow_579_GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut",
        "GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn": "_dialogflow_580_GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut": "_dialogflow_581_GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn": "_dialogflow_582_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut": "_dialogflow_583_GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut",
        "GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn": "_dialogflow_584_GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn",
        "GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut": "_dialogflow_585_GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn": "_dialogflow_586_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn",
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut": "_dialogflow_587_GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut",
        "GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn": "_dialogflow_588_GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn",
        "GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut": "_dialogflow_589_GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut",
        "GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn": "_dialogflow_590_GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn",
        "GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut": "_dialogflow_591_GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut",
        "GoogleCloudDialogflowV2ArticleAnswerIn": "_dialogflow_592_GoogleCloudDialogflowV2ArticleAnswerIn",
        "GoogleCloudDialogflowV2ArticleAnswerOut": "_dialogflow_593_GoogleCloudDialogflowV2ArticleAnswerOut",
        "GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn": "_dialogflow_594_GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn",
        "GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut": "_dialogflow_595_GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTextIn": "_dialogflow_596_GoogleCloudDialogflowV2beta1IntentMessageTextIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTextOut": "_dialogflow_597_GoogleCloudDialogflowV2beta1IntentMessageTextOut",
        "GoogleCloudDialogflowCxV3AudioInputIn": "_dialogflow_598_GoogleCloudDialogflowCxV3AudioInputIn",
        "GoogleCloudDialogflowCxV3AudioInputOut": "_dialogflow_599_GoogleCloudDialogflowCxV3AudioInputOut",
        "GoogleCloudDialogflowV2ContextIn": "_dialogflow_600_GoogleCloudDialogflowV2ContextIn",
        "GoogleCloudDialogflowV2ContextOut": "_dialogflow_601_GoogleCloudDialogflowV2ContextOut",
        "GoogleCloudDialogflowCxV3ListWebhooksResponseIn": "_dialogflow_602_GoogleCloudDialogflowCxV3ListWebhooksResponseIn",
        "GoogleCloudDialogflowCxV3ListWebhooksResponseOut": "_dialogflow_603_GoogleCloudDialogflowCxV3ListWebhooksResponseOut",
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn": "_dialogflow_604_GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn",
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut": "_dialogflow_605_GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut",
        "GoogleCloudDialogflowCxV3CalculateCoverageResponseIn": "_dialogflow_606_GoogleCloudDialogflowCxV3CalculateCoverageResponseIn",
        "GoogleCloudDialogflowCxV3CalculateCoverageResponseOut": "_dialogflow_607_GoogleCloudDialogflowCxV3CalculateCoverageResponseOut",
        "GoogleCloudDialogflowCxV3TurnSignalsIn": "_dialogflow_608_GoogleCloudDialogflowCxV3TurnSignalsIn",
        "GoogleCloudDialogflowCxV3TurnSignalsOut": "_dialogflow_609_GoogleCloudDialogflowCxV3TurnSignalsOut",
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn": "_dialogflow_610_GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut": "_dialogflow_611_GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn": "_dialogflow_612_GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut": "_dialogflow_613_GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn": "_dialogflow_614_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut": "_dialogflow_615_GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut",
        "GoogleCloudDialogflowV2IntentMessageCardButtonIn": "_dialogflow_616_GoogleCloudDialogflowV2IntentMessageCardButtonIn",
        "GoogleCloudDialogflowV2IntentMessageCardButtonOut": "_dialogflow_617_GoogleCloudDialogflowV2IntentMessageCardButtonOut",
        "GoogleCloudDialogflowCxV3GcsDestinationIn": "_dialogflow_618_GoogleCloudDialogflowCxV3GcsDestinationIn",
        "GoogleCloudDialogflowCxV3GcsDestinationOut": "_dialogflow_619_GoogleCloudDialogflowCxV3GcsDestinationOut",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn": "_dialogflow_620_GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffIn",
        "GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut": "_dialogflow_621_GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoffOut",
        "GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn": "_dialogflow_622_GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn",
        "GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut": "_dialogflow_623_GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut",
        "GoogleCloudDialogflowV2IntentParameterIn": "_dialogflow_624_GoogleCloudDialogflowV2IntentParameterIn",
        "GoogleCloudDialogflowV2IntentParameterOut": "_dialogflow_625_GoogleCloudDialogflowV2IntentParameterOut",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn": "_dialogflow_626_GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut": "_dialogflow_627_GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn": "_dialogflow_628_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut": "_dialogflow_629_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut",
        "GoogleCloudDialogflowCxV3beta1QueryInputIn": "_dialogflow_630_GoogleCloudDialogflowCxV3beta1QueryInputIn",
        "GoogleCloudDialogflowCxV3beta1QueryInputOut": "_dialogflow_631_GoogleCloudDialogflowCxV3beta1QueryInputOut",
        "GoogleCloudDialogflowCxV3TestErrorIn": "_dialogflow_632_GoogleCloudDialogflowCxV3TestErrorIn",
        "GoogleCloudDialogflowCxV3TestErrorOut": "_dialogflow_633_GoogleCloudDialogflowCxV3TestErrorOut",
        "GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataIn": "_dialogflow_634_GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataOut": "_dialogflow_635_GoogleCloudDialogflowV3alpha1UpdateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesResponseIn": "_dialogflow_636_GoogleCloudDialogflowCxV3ExportTestCasesResponseIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesResponseOut": "_dialogflow_637_GoogleCloudDialogflowCxV3ExportTestCasesResponseOut",
        "GoogleCloudDialogflowV2SuggestArticlesResponseIn": "_dialogflow_638_GoogleCloudDialogflowV2SuggestArticlesResponseIn",
        "GoogleCloudDialogflowV2SuggestArticlesResponseOut": "_dialogflow_639_GoogleCloudDialogflowV2SuggestArticlesResponseOut",
        "GoogleCloudLocationListLocationsResponseIn": "_dialogflow_640_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_dialogflow_641_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudDialogflowCxV3beta1FormIn": "_dialogflow_642_GoogleCloudDialogflowCxV3beta1FormIn",
        "GoogleCloudDialogflowCxV3beta1FormOut": "_dialogflow_643_GoogleCloudDialogflowCxV3beta1FormOut",
        "GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn": "_dialogflow_644_GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn",
        "GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut": "_dialogflow_645_GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut",
        "GoogleCloudDialogflowCxV3AgentValidationResultIn": "_dialogflow_646_GoogleCloudDialogflowCxV3AgentValidationResultIn",
        "GoogleCloudDialogflowCxV3AgentValidationResultOut": "_dialogflow_647_GoogleCloudDialogflowCxV3AgentValidationResultOut",
        "GoogleCloudDialogflowCxV3WebhookIn": "_dialogflow_648_GoogleCloudDialogflowCxV3WebhookIn",
        "GoogleCloudDialogflowCxV3WebhookOut": "_dialogflow_649_GoogleCloudDialogflowCxV3WebhookOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn": "_dialogflow_650_GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut": "_dialogflow_651_GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut",
        "GoogleCloudDialogflowCxV3beta1IntentIn": "_dialogflow_652_GoogleCloudDialogflowCxV3beta1IntentIn",
        "GoogleCloudDialogflowCxV3beta1IntentOut": "_dialogflow_653_GoogleCloudDialogflowCxV3beta1IntentOut",
        "GoogleCloudDialogflowCxV3beta1TextInputIn": "_dialogflow_654_GoogleCloudDialogflowCxV3beta1TextInputIn",
        "GoogleCloudDialogflowCxV3beta1TextInputOut": "_dialogflow_655_GoogleCloudDialogflowCxV3beta1TextInputOut",
        "GoogleCloudDialogflowCxV3TextToSpeechSettingsIn": "_dialogflow_656_GoogleCloudDialogflowCxV3TextToSpeechSettingsIn",
        "GoogleCloudDialogflowCxV3TextToSpeechSettingsOut": "_dialogflow_657_GoogleCloudDialogflowCxV3TextToSpeechSettingsOut",
        "GoogleCloudDialogflowCxV3SentimentAnalysisResultIn": "_dialogflow_658_GoogleCloudDialogflowCxV3SentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3SentimentAnalysisResultOut": "_dialogflow_659_GoogleCloudDialogflowCxV3SentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3InputAudioConfigIn": "_dialogflow_660_GoogleCloudDialogflowCxV3InputAudioConfigIn",
        "GoogleCloudDialogflowCxV3InputAudioConfigOut": "_dialogflow_661_GoogleCloudDialogflowCxV3InputAudioConfigOut",
        "GoogleCloudDialogflowCxV3DtmfInputIn": "_dialogflow_662_GoogleCloudDialogflowCxV3DtmfInputIn",
        "GoogleCloudDialogflowCxV3DtmfInputOut": "_dialogflow_663_GoogleCloudDialogflowCxV3DtmfInputOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn": "_dialogflow_664_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut": "_dialogflow_665_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut",
        "GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataIn": "_dialogflow_666_GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataOut": "_dialogflow_667_GoogleCloudDialogflowCxV3ImportDocumentsOperationMetadataOut",
        "GoogleCloudDialogflowCxV3FulfillIntentResponseIn": "_dialogflow_668_GoogleCloudDialogflowCxV3FulfillIntentResponseIn",
        "GoogleCloudDialogflowCxV3FulfillIntentResponseOut": "_dialogflow_669_GoogleCloudDialogflowCxV3FulfillIntentResponseOut",
        "GoogleCloudDialogflowV2beta1MessageAnnotationIn": "_dialogflow_670_GoogleCloudDialogflowV2beta1MessageAnnotationIn",
        "GoogleCloudDialogflowV2beta1MessageAnnotationOut": "_dialogflow_671_GoogleCloudDialogflowV2beta1MessageAnnotationOut",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn": "_dialogflow_672_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseIn",
        "GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut": "_dialogflow_673_GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseOut",
        "GoogleCloudDialogflowCxV3RolloutConfigIn": "_dialogflow_674_GoogleCloudDialogflowCxV3RolloutConfigIn",
        "GoogleCloudDialogflowCxV3RolloutConfigOut": "_dialogflow_675_GoogleCloudDialogflowCxV3RolloutConfigOut",
        "GoogleCloudDialogflowV2SentimentAnalysisResultIn": "_dialogflow_676_GoogleCloudDialogflowV2SentimentAnalysisResultIn",
        "GoogleCloudDialogflowV2SentimentAnalysisResultOut": "_dialogflow_677_GoogleCloudDialogflowV2SentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3RolloutStateIn": "_dialogflow_678_GoogleCloudDialogflowCxV3RolloutStateIn",
        "GoogleCloudDialogflowCxV3RolloutStateOut": "_dialogflow_679_GoogleCloudDialogflowCxV3RolloutStateOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn": "_dialogflow_680_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut": "_dialogflow_681_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn": "_dialogflow_682_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut": "_dialogflow_683_GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut",
        "GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn": "_dialogflow_684_GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn",
        "GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut": "_dialogflow_685_GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn": "_dialogflow_686_GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut": "_dialogflow_687_GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn": "_dialogflow_688_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut": "_dialogflow_689_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut",
        "GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn": "_dialogflow_690_GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn",
        "GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut": "_dialogflow_691_GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn": "_dialogflow_692_GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut": "_dialogflow_693_GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut",
        "GoogleCloudDialogflowCxV3SecuritySettingsIn": "_dialogflow_694_GoogleCloudDialogflowCxV3SecuritySettingsIn",
        "GoogleCloudDialogflowCxV3SecuritySettingsOut": "_dialogflow_695_GoogleCloudDialogflowCxV3SecuritySettingsOut",
        "GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn": "_dialogflow_696_GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn",
        "GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut": "_dialogflow_697_GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut",
        "GoogleCloudDialogflowCxV3DetectIntentRequestIn": "_dialogflow_698_GoogleCloudDialogflowCxV3DetectIntentRequestIn",
        "GoogleCloudDialogflowCxV3DetectIntentRequestOut": "_dialogflow_699_GoogleCloudDialogflowCxV3DetectIntentRequestOut",
        "GoogleCloudDialogflowCxV3DeploymentResultIn": "_dialogflow_700_GoogleCloudDialogflowCxV3DeploymentResultIn",
        "GoogleCloudDialogflowCxV3DeploymentResultOut": "_dialogflow_701_GoogleCloudDialogflowCxV3DeploymentResultOut",
        "GoogleCloudDialogflowCxV3VersionVariantsVariantIn": "_dialogflow_702_GoogleCloudDialogflowCxV3VersionVariantsVariantIn",
        "GoogleCloudDialogflowCxV3VersionVariantsVariantOut": "_dialogflow_703_GoogleCloudDialogflowCxV3VersionVariantsVariantOut",
        "GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn": "_dialogflow_704_GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut": "_dialogflow_705_GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut",
        "GoogleCloudDialogflowV2SmartReplyModelMetadataIn": "_dialogflow_706_GoogleCloudDialogflowV2SmartReplyModelMetadataIn",
        "GoogleCloudDialogflowV2SmartReplyModelMetadataOut": "_dialogflow_707_GoogleCloudDialogflowV2SmartReplyModelMetadataOut",
        "GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn": "_dialogflow_708_GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn",
        "GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut": "_dialogflow_709_GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn": "_dialogflow_710_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn",
        "GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut": "_dialogflow_711_GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut",
        "GoogleCloudDialogflowV3alpha1ConversationSignalsIn": "_dialogflow_712_GoogleCloudDialogflowV3alpha1ConversationSignalsIn",
        "GoogleCloudDialogflowV3alpha1ConversationSignalsOut": "_dialogflow_713_GoogleCloudDialogflowV3alpha1ConversationSignalsOut",
        "GoogleCloudDialogflowCxV3beta1WebhookIn": "_dialogflow_714_GoogleCloudDialogflowCxV3beta1WebhookIn",
        "GoogleCloudDialogflowCxV3beta1WebhookOut": "_dialogflow_715_GoogleCloudDialogflowCxV3beta1WebhookOut",
        "GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn": "_dialogflow_716_GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn",
        "GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut": "_dialogflow_717_GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn": "_dialogflow_718_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut": "_dialogflow_719_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut",
        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn": "_dialogflow_720_GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut": "_dialogflow_721_GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut",
        "GoogleCloudDialogflowCxV3beta1IntentInputIn": "_dialogflow_722_GoogleCloudDialogflowCxV3beta1IntentInputIn",
        "GoogleCloudDialogflowCxV3beta1IntentInputOut": "_dialogflow_723_GoogleCloudDialogflowCxV3beta1IntentInputOut",
        "GoogleCloudDialogflowCxV3EntityTypeIn": "_dialogflow_724_GoogleCloudDialogflowCxV3EntityTypeIn",
        "GoogleCloudDialogflowCxV3EntityTypeOut": "_dialogflow_725_GoogleCloudDialogflowCxV3EntityTypeOut",
        "GoogleCloudDialogflowV2IntentMessageTableCardIn": "_dialogflow_726_GoogleCloudDialogflowV2IntentMessageTableCardIn",
        "GoogleCloudDialogflowV2IntentMessageTableCardOut": "_dialogflow_727_GoogleCloudDialogflowV2IntentMessageTableCardOut",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn": "_dialogflow_728_GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn",
        "GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut": "_dialogflow_729_GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn": "_dialogflow_730_GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut": "_dialogflow_731_GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut",
        "GoogleCloudDialogflowV2IntentMessageListSelectItemIn": "_dialogflow_732_GoogleCloudDialogflowV2IntentMessageListSelectItemIn",
        "GoogleCloudDialogflowV2IntentMessageListSelectItemOut": "_dialogflow_733_GoogleCloudDialogflowV2IntentMessageListSelectItemOut",
        "GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn": "_dialogflow_734_GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn",
        "GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut": "_dialogflow_735_GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut",
        "GoogleCloudDialogflowV2beta1QueryResultIn": "_dialogflow_736_GoogleCloudDialogflowV2beta1QueryResultIn",
        "GoogleCloudDialogflowV2beta1QueryResultOut": "_dialogflow_737_GoogleCloudDialogflowV2beta1QueryResultOut",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn": "_dialogflow_738_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn",
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut": "_dialogflow_739_GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut",
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn": "_dialogflow_740_GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataIn",
        "GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut": "_dialogflow_741_GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1ExportOperationMetadataIn": "_dialogflow_742_GoogleCloudDialogflowV2beta1ExportOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1ExportOperationMetadataOut": "_dialogflow_743_GoogleCloudDialogflowV2beta1ExportOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ConversationSignalsIn": "_dialogflow_744_GoogleCloudDialogflowCxV3ConversationSignalsIn",
        "GoogleCloudDialogflowCxV3ConversationSignalsOut": "_dialogflow_745_GoogleCloudDialogflowCxV3ConversationSignalsOut",
        "GoogleCloudDialogflowCxV3MatchIn": "_dialogflow_746_GoogleCloudDialogflowCxV3MatchIn",
        "GoogleCloudDialogflowCxV3MatchOut": "_dialogflow_747_GoogleCloudDialogflowCxV3MatchOut",
        "GoogleCloudDialogflowV2WebhookResponseIn": "_dialogflow_748_GoogleCloudDialogflowV2WebhookResponseIn",
        "GoogleCloudDialogflowV2WebhookResponseOut": "_dialogflow_749_GoogleCloudDialogflowV2WebhookResponseOut",
        "GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn": "_dialogflow_750_GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn",
        "GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut": "_dialogflow_751_GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1EntityTypeIn": "_dialogflow_752_GoogleCloudDialogflowV2beta1EntityTypeIn",
        "GoogleCloudDialogflowV2beta1EntityTypeOut": "_dialogflow_753_GoogleCloudDialogflowV2beta1EntityTypeOut",
        "GoogleCloudDialogflowV2ImportDocumentsResponseIn": "_dialogflow_754_GoogleCloudDialogflowV2ImportDocumentsResponseIn",
        "GoogleCloudDialogflowV2ImportDocumentsResponseOut": "_dialogflow_755_GoogleCloudDialogflowV2ImportDocumentsResponseOut",
        "GoogleCloudDialogflowCxV3ImportTestCasesMetadataIn": "_dialogflow_756_GoogleCloudDialogflowCxV3ImportTestCasesMetadataIn",
        "GoogleCloudDialogflowCxV3ImportTestCasesMetadataOut": "_dialogflow_757_GoogleCloudDialogflowCxV3ImportTestCasesMetadataOut",
        "GoogleCloudDialogflowCxV3VariantsHistoryIn": "_dialogflow_758_GoogleCloudDialogflowCxV3VariantsHistoryIn",
        "GoogleCloudDialogflowCxV3VariantsHistoryOut": "_dialogflow_759_GoogleCloudDialogflowCxV3VariantsHistoryOut",
        "GoogleCloudDialogflowCxV3EventInputIn": "_dialogflow_760_GoogleCloudDialogflowCxV3EventInputIn",
        "GoogleCloudDialogflowCxV3EventInputOut": "_dialogflow_761_GoogleCloudDialogflowCxV3EventInputOut",
        "GoogleCloudDialogflowV2EventInputIn": "_dialogflow_762_GoogleCloudDialogflowV2EventInputIn",
        "GoogleCloudDialogflowV2EventInputOut": "_dialogflow_763_GoogleCloudDialogflowV2EventInputOut",
        "GoogleCloudDialogflowV2KnowledgeOperationMetadataIn": "_dialogflow_764_GoogleCloudDialogflowV2KnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV2KnowledgeOperationMetadataOut": "_dialogflow_765_GoogleCloudDialogflowV2KnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3TestCaseErrorIn": "_dialogflow_766_GoogleCloudDialogflowCxV3TestCaseErrorIn",
        "GoogleCloudDialogflowCxV3TestCaseErrorOut": "_dialogflow_767_GoogleCloudDialogflowCxV3TestCaseErrorOut",
        "GoogleCloudDialogflowV2WebhookRequestIn": "_dialogflow_768_GoogleCloudDialogflowV2WebhookRequestIn",
        "GoogleCloudDialogflowV2WebhookRequestOut": "_dialogflow_769_GoogleCloudDialogflowV2WebhookRequestOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn": "_dialogflow_770_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut": "_dialogflow_771_GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn": "_dialogflow_772_GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut": "_dialogflow_773_GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut",
        "GoogleCloudDialogflowV2beta1WebhookResponseIn": "_dialogflow_774_GoogleCloudDialogflowV2beta1WebhookResponseIn",
        "GoogleCloudDialogflowV2beta1WebhookResponseOut": "_dialogflow_775_GoogleCloudDialogflowV2beta1WebhookResponseOut",
        "GoogleCloudDialogflowCxV3FulfillIntentRequestIn": "_dialogflow_776_GoogleCloudDialogflowCxV3FulfillIntentRequestIn",
        "GoogleCloudDialogflowCxV3FulfillIntentRequestOut": "_dialogflow_777_GoogleCloudDialogflowCxV3FulfillIntentRequestOut",
        "GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn": "_dialogflow_778_GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn",
        "GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut": "_dialogflow_779_GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut",
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_780_GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_781_GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowV2IntentMessageSuggestionsIn": "_dialogflow_782_GoogleCloudDialogflowV2IntentMessageSuggestionsIn",
        "GoogleCloudDialogflowV2IntentMessageSuggestionsOut": "_dialogflow_783_GoogleCloudDialogflowV2IntentMessageSuggestionsOut",
        "GoogleCloudDialogflowCxV3IntentIn": "_dialogflow_784_GoogleCloudDialogflowCxV3IntentIn",
        "GoogleCloudDialogflowCxV3IntentOut": "_dialogflow_785_GoogleCloudDialogflowCxV3IntentOut",
        "GoogleCloudDialogflowCxV3ListDeploymentsResponseIn": "_dialogflow_786_GoogleCloudDialogflowCxV3ListDeploymentsResponseIn",
        "GoogleCloudDialogflowCxV3ListDeploymentsResponseOut": "_dialogflow_787_GoogleCloudDialogflowCxV3ListDeploymentsResponseOut",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioIn": "_dialogflow_788_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioIn",
        "GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut": "_dialogflow_789_GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut",
        "GoogleCloudDialogflowCxV3TestRunDifferenceIn": "_dialogflow_790_GoogleCloudDialogflowCxV3TestRunDifferenceIn",
        "GoogleCloudDialogflowCxV3TestRunDifferenceOut": "_dialogflow_791_GoogleCloudDialogflowCxV3TestRunDifferenceOut",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseIn": "_dialogflow_792_GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseIn",
        "GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseOut": "_dialogflow_793_GoogleCloudDialogflowCxV3beta1RunContinuousTestResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn": "_dialogflow_794_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut": "_dialogflow_795_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn": "_dialogflow_796_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut": "_dialogflow_797_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut",
        "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn": "_dialogflow_798_GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut": "_dialogflow_799_GoogleCloudDialogflowV3alpha1GenericKnowledgeOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn": "_dialogflow_800_GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut": "_dialogflow_801_GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_802_GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_803_GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardIn": "_dialogflow_804_GoogleCloudDialogflowV2beta1IntentMessageTableCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageTableCardOut": "_dialogflow_805_GoogleCloudDialogflowV2beta1IntentMessageTableCardOut",
        "GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn": "_dialogflow_806_GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn",
        "GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut": "_dialogflow_807_GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut",
        "GoogleCloudDialogflowCxV3VoiceSelectionParamsIn": "_dialogflow_808_GoogleCloudDialogflowCxV3VoiceSelectionParamsIn",
        "GoogleCloudDialogflowCxV3VoiceSelectionParamsOut": "_dialogflow_809_GoogleCloudDialogflowCxV3VoiceSelectionParamsOut",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn": "_dialogflow_810_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn",
        "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut": "_dialogflow_811_GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut",
        "GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn": "_dialogflow_812_GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn",
        "GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut": "_dialogflow_813_GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut",
        "GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn": "_dialogflow_814_GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn",
        "GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut": "_dialogflow_815_GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut",
        "GoogleCloudDialogflowCxV3EntityTypeEntityIn": "_dialogflow_816_GoogleCloudDialogflowCxV3EntityTypeEntityIn",
        "GoogleCloudDialogflowCxV3EntityTypeEntityOut": "_dialogflow_817_GoogleCloudDialogflowCxV3EntityTypeEntityOut",
        "GoogleCloudDialogflowV2IntentTrainingPhraseIn": "_dialogflow_818_GoogleCloudDialogflowV2IntentTrainingPhraseIn",
        "GoogleCloudDialogflowV2IntentTrainingPhraseOut": "_dialogflow_819_GoogleCloudDialogflowV2IntentTrainingPhraseOut",
        "GoogleCloudDialogflowCxV3CompareVersionsRequestIn": "_dialogflow_820_GoogleCloudDialogflowCxV3CompareVersionsRequestIn",
        "GoogleCloudDialogflowCxV3CompareVersionsRequestOut": "_dialogflow_821_GoogleCloudDialogflowCxV3CompareVersionsRequestOut",
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn": "_dialogflow_822_GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataIn",
        "GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut": "_dialogflow_823_GoogleCloudDialogflowV2DeleteConversationModelOperationMetadataOut",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn": "_dialogflow_824_GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultIn",
        "GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut": "_dialogflow_825_GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResultOut",
        "GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn": "_dialogflow_826_GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut": "_dialogflow_827_GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut",
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn": "_dialogflow_828_GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn",
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut": "_dialogflow_829_GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut",
        "GoogleCloudDialogflowV2beta1EventInputIn": "_dialogflow_830_GoogleCloudDialogflowV2beta1EventInputIn",
        "GoogleCloudDialogflowV2beta1EventInputOut": "_dialogflow_831_GoogleCloudDialogflowV2beta1EventInputOut",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn": "_dialogflow_832_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn",
        "GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut": "_dialogflow_833_GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut",
        "GoogleCloudDialogflowCxV3ExportTestCasesRequestIn": "_dialogflow_834_GoogleCloudDialogflowCxV3ExportTestCasesRequestIn",
        "GoogleCloudDialogflowCxV3ExportTestCasesRequestOut": "_dialogflow_835_GoogleCloudDialogflowCxV3ExportTestCasesRequestOut",
        "GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataIn": "_dialogflow_836_GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataOut": "_dialogflow_837_GoogleCloudDialogflowCxV3CreateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn": "_dialogflow_838_GoogleCloudDialogflowCxV3ListTestCaseResultsResponseIn",
        "GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut": "_dialogflow_839_GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut",
        "GoogleCloudDialogflowV2beta1ContextIn": "_dialogflow_840_GoogleCloudDialogflowV2beta1ContextIn",
        "GoogleCloudDialogflowV2beta1ContextOut": "_dialogflow_841_GoogleCloudDialogflowV2beta1ContextOut",
        "GoogleCloudDialogflowV2IntentTrainingPhrasePartIn": "_dialogflow_842_GoogleCloudDialogflowV2IntentTrainingPhrasePartIn",
        "GoogleCloudDialogflowV2IntentTrainingPhrasePartOut": "_dialogflow_843_GoogleCloudDialogflowV2IntentTrainingPhrasePartOut",
        "GoogleCloudDialogflowCxV3FormParameterIn": "_dialogflow_844_GoogleCloudDialogflowCxV3FormParameterIn",
        "GoogleCloudDialogflowCxV3FormParameterOut": "_dialogflow_845_GoogleCloudDialogflowCxV3FormParameterOut",
        "GoogleCloudDialogflowV2beta1SentimentIn": "_dialogflow_846_GoogleCloudDialogflowV2beta1SentimentIn",
        "GoogleCloudDialogflowV2beta1SentimentOut": "_dialogflow_847_GoogleCloudDialogflowV2beta1SentimentOut",
        "GoogleCloudDialogflowCxV3VersionVariantsIn": "_dialogflow_848_GoogleCloudDialogflowCxV3VersionVariantsIn",
        "GoogleCloudDialogflowCxV3VersionVariantsOut": "_dialogflow_849_GoogleCloudDialogflowCxV3VersionVariantsOut",
        "GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn": "_dialogflow_850_GoogleCloudDialogflowV2SuggestSmartRepliesResponseIn",
        "GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut": "_dialogflow_851_GoogleCloudDialogflowV2SuggestSmartRepliesResponseOut",
        "GoogleCloudDialogflowV2MessageAnnotationIn": "_dialogflow_852_GoogleCloudDialogflowV2MessageAnnotationIn",
        "GoogleCloudDialogflowV2MessageAnnotationOut": "_dialogflow_853_GoogleCloudDialogflowV2MessageAnnotationOut",
        "GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataIn": "_dialogflow_854_GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataIn",
        "GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataOut": "_dialogflow_855_GoogleCloudDialogflowCxV3beta1CreateDocumentOperationMetadataOut",
        "GoogleCloudDialogflowCxV3ChangelogIn": "_dialogflow_856_GoogleCloudDialogflowCxV3ChangelogIn",
        "GoogleCloudDialogflowCxV3ChangelogOut": "_dialogflow_857_GoogleCloudDialogflowCxV3ChangelogOut",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn": "_dialogflow_858_GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn",
        "GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut": "_dialogflow_859_GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut",
        "GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseIn": "_dialogflow_860_GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseIn",
        "GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseOut": "_dialogflow_861_GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponseOut",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn": "_dialogflow_862_GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn",
        "GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut": "_dialogflow_863_GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponseIn": "_dialogflow_864_GoogleCloudDialogflowV2IntentMessageSimpleResponseIn",
        "GoogleCloudDialogflowV2IntentMessageSimpleResponseOut": "_dialogflow_865_GoogleCloudDialogflowV2IntentMessageSimpleResponseOut",
        "GoogleCloudDialogflowV2beta1IntentMessageCardIn": "_dialogflow_866_GoogleCloudDialogflowV2beta1IntentMessageCardIn",
        "GoogleCloudDialogflowV2beta1IntentMessageCardOut": "_dialogflow_867_GoogleCloudDialogflowV2beta1IntentMessageCardOut",
        "GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn": "_dialogflow_868_GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseIn",
        "GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut": "_dialogflow_869_GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseOut",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn": "_dialogflow_870_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn",
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut": "_dialogflow_871_GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut",
        "GoogleCloudDialogflowV2IntentMessageSuggestionIn": "_dialogflow_872_GoogleCloudDialogflowV2IntentMessageSuggestionIn",
        "GoogleCloudDialogflowV2IntentMessageSuggestionOut": "_dialogflow_873_GoogleCloudDialogflowV2IntentMessageSuggestionOut",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataIn": "_dialogflow_874_GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataIn",
        "GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataOut": "_dialogflow_875_GoogleCloudDialogflowV3alpha1ImportDocumentsOperationMetadataOut",
        "GoogleRpcStatusIn": "_dialogflow_876_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_dialogflow_877_GoogleRpcStatusOut",
        "GoogleCloudDialogflowV2IntentMessageIn": "_dialogflow_878_GoogleCloudDialogflowV2IntentMessageIn",
        "GoogleCloudDialogflowV2IntentMessageOut": "_dialogflow_879_GoogleCloudDialogflowV2IntentMessageOut",
        "GoogleCloudDialogflowV2IntentMessageMediaContentIn": "_dialogflow_880_GoogleCloudDialogflowV2IntentMessageMediaContentIn",
        "GoogleCloudDialogflowV2IntentMessageMediaContentOut": "_dialogflow_881_GoogleCloudDialogflowV2IntentMessageMediaContentOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"] = t.struct(
        {"audioUri": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"] = t.struct(
        {"audioUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"])
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
    types["GoogleCloudDialogflowCxV3ConversationTurnUserInputIn"] = t.struct(
        {
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryInputIn"]
            ).optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputIn"])
    types["GoogleCloudDialogflowCxV3ConversationTurnUserInputOut"] = t.struct(
        {
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryInputOut"]
            ).optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnUserInputOut"])
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
    types["GoogleCloudDialogflowV2SessionEntityTypeIn"] = t.struct(
        {
            "name": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityIn"])
            ),
            "entityOverrideMode": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2SessionEntityTypeIn"])
    types["GoogleCloudDialogflowV2SessionEntityTypeOut"] = t.struct(
        {
            "name": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityOut"])
            ),
            "entityOverrideMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SessionEntityTypeOut"])
    types[
        "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataIn"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "conversationModelEvaluation": t.string().optional(),
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
            "conversationModel": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "conversationModelEvaluation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadataOut"
        ]
    )
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
    types["GoogleCloudDialogflowCxV3ImportTestCasesRequestIn"] = t.struct(
        {"content": t.string().optional(), "gcsUri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3ImportTestCasesRequestOut"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesRequestOut"])
    types["GoogleCloudDialogflowV2AnnotatedMessagePartIn"] = t.struct(
        {
            "text": t.string().optional(),
            "entityType": t.string().optional(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2AnnotatedMessagePartIn"])
    types["GoogleCloudDialogflowV2AnnotatedMessagePartOut"] = t.struct(
        {
            "text": t.string().optional(),
            "entityType": t.string().optional(),
            "formattedValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2AnnotatedMessagePartOut"])
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
    types["GoogleCloudDialogflowV2beta1SuggestionResultIn"] = t.struct(
        {
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"]
            ).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestionResultIn"])
    types["GoogleCloudDialogflowV2beta1SuggestionResultOut"] = t.struct(
        {
            "suggestArticlesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "suggestSmartRepliesResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"]
            ).optional(),
            "suggestFaqAnswersResponse": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestionResultOut"])
    types["GoogleCloudDialogflowCxV3FlowIn"] = t.struct(
        {
            "transitionRouteGroups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
            ).optional(),
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
            ).optional(),
            "displayName": t.string(),
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowIn"])
    types["GoogleCloudDialogflowCxV3FlowOut"] = t.struct(
        {
            "transitionRouteGroups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
            ).optional(),
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
            ).optional(),
            "displayName": t.string(),
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FlowOut"])
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
    types["GoogleCloudDialogflowCxV3CompareVersionsResponseIn"] = t.struct(
        {
            "baseVersionContentJson": t.string().optional(),
            "compareTime": t.string().optional(),
            "targetVersionContentJson": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseIn"])
    types["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"] = t.struct(
        {
            "baseVersionContentJson": t.string().optional(),
            "compareTime": t.string().optional(),
            "targetVersionContentJson": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"])
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
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioIn"]
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
            "conversationSuccess": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessOut"
                ]
            ).optional(),
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudioOut"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCallOut"
                ]
            ).optional(),
            "endInteraction": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"
                ]
            ).optional(),
            "mixedAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioOut"]
            ).optional(),
            "outputAudioText": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"
                ]
            ).optional(),
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
    types["GoogleCloudDialogflowCxV3LoadVersionRequestIn"] = t.struct(
        {"allowOverrideAgentResources": t.boolean().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3LoadVersionRequestIn"])
    types["GoogleCloudDialogflowCxV3LoadVersionRequestOut"] = t.struct(
        {
            "allowOverrideAgentResources": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3LoadVersionRequestOut"])
    types["GoogleCloudDialogflowV2IntentMessageCardIn"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageCardButtonIn"])
            ).optional(),
            "imageUri": t.string().optional(),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageCardOut"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageCardButtonOut"])
            ).optional(),
            "imageUri": t.string().optional(),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardOut"])
    types["GoogleCloudDialogflowCxV3WebhookResponseIn"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoIn"]
            ).optional(),
            "targetFlow": t.string().optional(),
            "fulfillmentResponse": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn"]
            ).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseIn"])
    types["GoogleCloudDialogflowCxV3WebhookResponseOut"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoOut"]
            ).optional(),
            "targetFlow": t.string().optional(),
            "fulfillmentResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut"
                ]
            ).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentParameterIn"] = t.struct(
        {
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "isList": t.boolean().optional(),
            "entityTypeDisplayName": t.string().optional(),
            "value": t.string().optional(),
            "mandatory": t.boolean().optional(),
            "displayName": t.string(),
            "prompts": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentParameterIn"])
    types["GoogleCloudDialogflowV2beta1IntentParameterOut"] = t.struct(
        {
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "isList": t.boolean().optional(),
            "entityTypeDisplayName": t.string().optional(),
            "value": t.string().optional(),
            "mandatory": t.boolean().optional(),
            "displayName": t.string(),
            "prompts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentParameterOut"])
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
    types["GoogleCloudDialogflowCxV3RunTestCaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseMetadataIn"])
    types["GoogleCloudDialogflowCxV3RunTestCaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseMetadataOut"])
    types["GoogleCloudDialogflowCxV3PageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
            ).optional(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
            ).optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageIn"])
    types["GoogleCloudDialogflowCxV3PageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormOut"]).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
            ).optional(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
            ).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageOut"])
    types["GoogleCloudDialogflowV2IntentFollowupIntentInfoIn"] = t.struct(
        {
            "parentFollowupIntentName": t.string().optional(),
            "followupIntentName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentFollowupIntentInfoIn"])
    types["GoogleCloudDialogflowV2IntentFollowupIntentInfoOut"] = t.struct(
        {
            "parentFollowupIntentName": t.string().optional(),
            "followupIntentName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentFollowupIntentInfoOut"])
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
    types["GoogleCloudDialogflowCxV3NluSettingsIn"] = t.struct(
        {
            "classificationThreshold": t.number().optional(),
            "modelType": t.string().optional(),
            "modelTrainingMode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3NluSettingsIn"])
    types["GoogleCloudDialogflowCxV3NluSettingsOut"] = t.struct(
        {
            "classificationThreshold": t.number().optional(),
            "modelType": t.string().optional(),
            "modelTrainingMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3NluSettingsOut"])
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
    types["GoogleCloudDialogflowCxV3EventHandlerIn"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
            "event": t.string(),
            "targetFlow": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
    types["GoogleCloudDialogflowCxV3EventHandlerOut"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "name": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "event": t.string(),
            "targetFlow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
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
    types["GoogleCloudDialogflowV3alpha1TurnSignalsIn"] = t.struct(
        {
            "agentEscalated": t.boolean().optional(),
            "noUserInput": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "dtmfUsed": t.boolean().optional(),
            "triggeredAbandonmentEvent": t.boolean().optional(),
            "reachedEndPage": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "noMatch": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "userEscalated": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1TurnSignalsIn"])
    types["GoogleCloudDialogflowV3alpha1TurnSignalsOut"] = t.struct(
        {
            "agentEscalated": t.boolean().optional(),
            "noUserInput": t.boolean().optional(),
            "sentimentMagnitude": t.number().optional(),
            "dtmfUsed": t.boolean().optional(),
            "triggeredAbandonmentEvent": t.boolean().optional(),
            "reachedEndPage": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "noMatch": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "userEscalated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1TurnSignalsOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookResponseIn"] = t.struct(
        {
            "fulfillmentResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn"
                ]
            ).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoIn"]
            ).optional(),
            "targetPage": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "targetFlow": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookResponseOut"] = t.struct(
        {
            "fulfillmentResponse": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut"
                ]
            ).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoOut"]
            ).optional(),
            "targetPage": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "targetFlow": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookResponseOut"])
    types[
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut"
    ] = t.struct(
        {
            "conversationModel": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2UndeployConversationModelOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowV2IntentIn"] = t.struct(
        {
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "parentFollowupIntentName": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentParameterIn"])
            ).optional(),
            "endInteraction": t.boolean().optional(),
            "action": t.string().optional(),
            "isFallback": t.boolean().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "mlDisabled": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
            "resetContexts": t.boolean().optional(),
            "displayName": t.string(),
            "webhookState": t.string().optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "priority": t.integer().optional(),
            "name": t.string().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhraseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentIn"])
    types["GoogleCloudDialogflowV2IntentOut"] = t.struct(
        {
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "parentFollowupIntentName": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentParameterOut"])
            ).optional(),
            "endInteraction": t.boolean().optional(),
            "action": t.string().optional(),
            "isFallback": t.boolean().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "mlDisabled": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "followupIntentInfo": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentFollowupIntentInfoOut"])
            ).optional(),
            "resetContexts": t.boolean().optional(),
            "displayName": t.string(),
            "webhookState": t.string().optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "priority": t.integer().optional(),
            "name": t.string().optional(),
            "rootFollowupIntentName": t.string().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhraseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentOut"])
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
    types["GoogleCloudDialogflowCxV3beta1PageIn"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerIn"])
            ).optional(),
            "form": t.proxy(renames["GoogleCloudDialogflowCxV3beta1FormIn"]).optional(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
            "name": t.string().optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"])
            ).optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageIn"])
    types["GoogleCloudDialogflowCxV3beta1PageOut"] = t.struct(
        {
            "eventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1EventHandlerOut"])
            ).optional(),
            "form": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FormOut"]
            ).optional(),
            "entryFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "name": t.string().optional(),
            "transitionRouteGroups": t.array(t.string()).optional(),
            "transitionRoutes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteOut"])
            ).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageOut"])
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
    types["GoogleCloudDialogflowV2MessageIn"] = t.struct(
        {
            "content": t.string(),
            "sendTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageIn"])
    types["GoogleCloudDialogflowV2MessageOut"] = t.struct(
        {
            "content": t.string(),
            "createTime": t.string().optional(),
            "participantRole": t.string().optional(),
            "messageAnnotation": t.proxy(
                renames["GoogleCloudDialogflowV2MessageAnnotationOut"]
            ).optional(),
            "sendTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "sentimentAnalysis": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultOut"]
            ).optional(),
            "participant": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2MessageOut"])
    types["GoogleCloudDialogflowV2ConversationModelIn"] = t.struct(
        {
            "displayName": t.string(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "datasets": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2InputDatasetIn"])
            ),
            "articleSuggestionModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"]
            ).optional(),
            "smartReplyModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationModelIn"])
    types["GoogleCloudDialogflowV2ConversationModelOut"] = t.struct(
        {
            "displayName": t.string(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "datasets": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2InputDatasetOut"])
            ),
            "articleSuggestionModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"]
            ).optional(),
            "smartReplyModelMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationModelOut"])
    types["GoogleCloudDialogflowCxV3TestCaseIn"] = t.struct(
        {
            "displayName": t.string(),
            "notes": t.string().optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
            ).optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseResultIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseIn"])
    types["GoogleCloudDialogflowCxV3TestCaseOut"] = t.struct(
        {
            "displayName": t.string(),
            "notes": t.string().optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestConfigOut"]
            ).optional(),
            "creationTime": t.string().optional(),
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnOut"])
            ).optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseOut"])
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
    types["GoogleCloudDialogflowCxV3StopExperimentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StopExperimentRequestIn"])
    types["GoogleCloudDialogflowCxV3StopExperimentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StopExperimentRequestOut"])
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
    types["GoogleCloudDialogflowCxV3PageInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoFormInfoIn"]
            ).optional(),
            "currentPage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoIn"])
    types["GoogleCloudDialogflowCxV3PageInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoFormInfoOut"]
            ).optional(),
            "currentPage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoOut"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentIn"] = t.struct(
        {
            "webhook": t.string().optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn"
                    ]
                )
            ).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
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
            "webhook": t.string().optional(),
            "conditionalCases": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut"
                    ]
                )
            ).optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
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
    types["GoogleCloudDialogflowCxV3DetectIntentResponseIn"] = t.struct(
        {
            "responseId": t.string().optional(),
            "outputAudio": t.string().optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
            "allowCancellation": t.boolean().optional(),
            "responseType": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentResponseIn"])
    types["GoogleCloudDialogflowCxV3DetectIntentResponseOut"] = t.struct(
        {
            "responseId": t.string().optional(),
            "outputAudio": t.string().optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "allowCancellation": t.boolean().optional(),
            "responseType": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DetectIntentResponseOut"])
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
    types["GoogleCloudDialogflowCxV3RunTestCaseRequestIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseRequestIn"])
    types["GoogleCloudDialogflowCxV3RunTestCaseRequestOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RunTestCaseRequestOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageIn"] = t.struct(
        {
            "conversationSuccess": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"]
            ).optional(),
            "liveAgentHandoff": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"]
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
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageOut"] = t.struct(
        {
            "conversationSuccess": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"
                ]
            ).optional(),
            "liveAgentHandoff": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"]
            ).optional(),
            "endInteraction": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"]
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
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "mixedAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioOut"]
            ).optional(),
            "playAudio": t.proxy(
                renames["GoogleCloudDialogflowCxV3ResponseMessagePlayAudioOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
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
    types["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "source": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"])
    types["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "source": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"])
    types["GoogleCloudDialogflowCxV3ExperimentResultMetricIn"] = t.struct(
        {
            "countType": t.string().optional(),
            "count": t.number().optional(),
            "ratio": t.number().optional(),
            "confidenceInterval": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultMetricIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultMetricOut"] = t.struct(
        {
            "countType": t.string().optional(),
            "count": t.number().optional(),
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
    types["GoogleCloudDialogflowCxV3ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportDocumentsResponseOut"])
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
    types["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV3alpha1ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageIn"] = t.struct(
        {
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectIn"]
            ).optional(),
            "rbmText": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmTextIn"]
            ).optional(),
            "platform": t.string().optional(),
            "rbmCarouselRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardIn"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesIn"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectIn"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallIn"
                ]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsIn"]
            ).optional(),
            "rbmStandaloneRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn"]
            ).optional(),
            "telephonyPlayAudio": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioIn"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageMediaContentIn"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCardIn"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesIn"]
            ).optional(),
            "telephonySynthesizeSpeech": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechIn"
                ]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionIn"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageOut"] = t.struct(
        {
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectOut"]
            ).optional(),
            "rbmText": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmTextOut"]
            ).optional(),
            "platform": t.string().optional(),
            "rbmCarouselRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardOut"
                ]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageQuickRepliesOut"]
            ).optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectOut"]
            ).optional(),
            "telephonyTransferCall": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallOut"
                ]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionsOut"]
            ).optional(),
            "rbmStandaloneRichCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut"]
            ).optional(),
            "telephonyPlayAudio": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudioOut"
                ]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageMediaContentOut"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageCardOut"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"]
            ).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSimpleResponsesOut"]
            ).optional(),
            "telephonySynthesizeSpeech": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeechOut"
                ]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestionOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageTextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
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
    types["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"] = t.struct(
        {
            "volumeGainDb": t.number().optional(),
            "speakingRate": t.number().optional(),
            "voice": t.proxy(
                renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsIn"]
            ).optional(),
            "pitch": t.number().optional(),
            "effectsProfileId": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"])
    types["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"] = t.struct(
        {
            "volumeGainDb": t.number().optional(),
            "speakingRate": t.number().optional(),
            "voice": t.proxy(
                renames["GoogleCloudDialogflowCxV3VoiceSelectionParamsOut"]
            ).optional(),
            "pitch": t.number().optional(),
            "effectsProfileId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"])
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
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIn"] = t.struct(
        {
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoIn"]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoIn"]
            ).optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"]
            ).optional(),
            "detectIntentResponseId": t.string().optional(),
            "transcript": t.string().optional(),
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
            "triggerIntent": t.string().optional(),
            "text": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "dtmfDigits": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestOut"] = t.struct(
        {
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoOut"]
            ).optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1SessionInfoOut"]
            ).optional(),
            "fulfillmentInfo": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"
                ]
            ).optional(),
            "detectIntentResponseId": t.string().optional(),
            "transcript": t.string().optional(),
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
            "triggerIntent": t.string().optional(),
            "text": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "dtmfDigits": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestOut"])
    types["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "title": t.string(),
            "description": t.string().optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn"]
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemIn"])
    types["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "title": t.string(),
            "description": t.string().optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectItemOut"])
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
    types["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"] = t.struct(
        {
            "testResult": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnIn"])
            ).optional(),
            "environment": t.string().optional(),
            "name": t.string().optional(),
            "testTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"] = t.struct(
        {
            "testResult": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnOut"])
            ).optional(),
            "environment": t.string().optional(),
            "name": t.string().optional(),
            "testTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"])
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
    types["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn"] = t.struct(
        {
            "enableContinuousRun": t.boolean().optional(),
            "testCases": t.array(t.string()).optional(),
            "enablePredeploymentRun": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut"] = t.struct(
        {
            "enableContinuousRun": t.boolean().optional(),
            "testCases": t.array(t.string()).optional(),
            "enablePredeploymentRun": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentIn"] = t.struct(
        {
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "versionConfigs": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"]
                )
            ).optional(),
            "displayName": t.string(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentOut"] = t.struct(
        {
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "versionConfigs": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"]
                )
            ).optional(),
            "displayName": t.string(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentOut"])
    types["GoogleCloudDialogflowCxV3beta1TestConfigIn"] = t.struct(
        {
            "trackingParameters": t.array(t.string()).optional(),
            "page": t.string().optional(),
            "flow": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1TestConfigOut"] = t.struct(
        {
            "trackingParameters": t.array(t.string()).optional(),
            "page": t.string().optional(),
            "flow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestConfigOut"])
    types["GoogleCloudDialogflowCxV3EnvironmentIn"] = t.struct(
        {
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigIn"]
            ).optional(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "versionConfigs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentOut"] = t.struct(
        {
            "webhookConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentWebhookConfigOut"]
            ).optional(),
            "testCasesConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "versionConfigs": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"])
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentOut"])
    types["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"] = t.struct(
        {"state": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GenericKnowledgeOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3QueryParametersIn"] = t.struct(
        {
            "disableWebhook": t.boolean().optional(),
            "timeZone": t.string().optional(),
            "geoLocation": t.proxy(renames["GoogleTypeLatLngIn"]).optional(),
            "channel": t.string().optional(),
            "analyzeQueryTextSentiment": t.boolean().optional(),
            "webhookHeaders": t.struct({"_": t.string().optional()}).optional(),
            "currentPage": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "flowVersions": t.array(t.string()).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryParametersIn"])
    types["GoogleCloudDialogflowCxV3QueryParametersOut"] = t.struct(
        {
            "disableWebhook": t.boolean().optional(),
            "timeZone": t.string().optional(),
            "geoLocation": t.proxy(renames["GoogleTypeLatLngOut"]).optional(),
            "channel": t.string().optional(),
            "analyzeQueryTextSentiment": t.boolean().optional(),
            "webhookHeaders": t.struct({"_": t.string().optional()}).optional(),
            "currentPage": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "flowVersions": t.array(t.string()).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryParametersOut"])
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
    types["GoogleCloudDialogflowCxV3TestConfigIn"] = t.struct(
        {
            "flow": t.string().optional(),
            "page": t.string().optional(),
            "trackingParameters": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestConfigIn"])
    types["GoogleCloudDialogflowCxV3TestConfigOut"] = t.struct(
        {
            "flow": t.string().optional(),
            "page": t.string().optional(),
            "trackingParameters": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestConfigOut"])
    types["GoogleCloudDialogflowCxV3DeploymentIn"] = t.struct(
        {
            "flowVersion": t.string().optional(),
            "startTime": t.string().optional(),
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3DeploymentResultIn"]
            ).optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentIn"])
    types["GoogleCloudDialogflowCxV3DeploymentOut"] = t.struct(
        {
            "flowVersion": t.string().optional(),
            "startTime": t.string().optional(),
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3DeploymentResultOut"]
            ).optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeploymentOut"])
    types["GoogleCloudDialogflowCxV3ExperimentIn"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
            ).optional(),
            "rolloutConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
            ).optional(),
            "variantsHistory": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
            ).optional(),
            "startTime": t.string().optional(),
            "displayName": t.string(),
            "experimentLength": t.string().optional(),
            "endTime": t.string().optional(),
            "description": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "rolloutFailureReason": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "definition": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "rolloutState": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentIn"])
    types["GoogleCloudDialogflowCxV3ExperimentOut"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentResultOut"]
            ).optional(),
            "rolloutConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutConfigOut"]
            ).optional(),
            "variantsHistory": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "displayName": t.string(),
            "experimentLength": t.string().optional(),
            "endTime": t.string().optional(),
            "description": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "rolloutFailureReason": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "definition": t.proxy(
                renames["GoogleCloudDialogflowCxV3ExperimentDefinitionOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "rolloutState": t.proxy(
                renames["GoogleCloudDialogflowCxV3RolloutStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentOut"])
    types["GoogleCloudDialogflowCxV3ValidationMessageIn"] = t.struct(
        {
            "resourceNames": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResourceNameIn"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "severity": t.string().optional(),
            "detail": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidationMessageIn"])
    types["GoogleCloudDialogflowCxV3ValidationMessageOut"] = t.struct(
        {
            "resourceNames": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResourceNameOut"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "severity": t.string().optional(),
            "detail": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidationMessageOut"])
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
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "transitionRoute": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteIn"]
            ).optional(),
            "source": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeIn"]
            ).optional(),
            "covered": t.boolean().optional(),
            "eventHandler": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventHandlerIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "transitionRoute": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteOut"]
            ).optional(),
            "source": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionNodeOut"]
            ).optional(),
            "covered": t.boolean().optional(),
            "eventHandler": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventHandlerOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut"])
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
    types["GoogleCloudDialogflowCxV3TestCaseResultIn"] = t.struct(
        {
            "testTime": t.string().optional(),
            "testResult": t.string().optional(),
            "name": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnIn"])
            ).optional(),
            "environment": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseResultIn"])
    types["GoogleCloudDialogflowCxV3TestCaseResultOut"] = t.struct(
        {
            "testTime": t.string().optional(),
            "testResult": t.string().optional(),
            "name": t.string().optional(),
            "conversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ConversationTurnOut"])
            ).optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseResultOut"])
    types["GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn"] = t.struct(
        {"flow": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut"] = t.struct(
        {
            "flow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportFlowResponseOut"])
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
    types["GoogleCloudDialogflowCxV3ImportTestCasesResponseIn"] = t.struct(
        {"names": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportTestCasesResponseOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportTestCasesResponseOut"])
    types["GoogleCloudDialogflowV2beta1ConversationEventIn"] = t.struct(
        {
            "conversation": t.string(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageIn"]
            ).optional(),
            "type": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ConversationEventIn"])
    types["GoogleCloudDialogflowV2beta1ConversationEventOut"] = t.struct(
        {
            "conversation": t.string(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageOut"]
            ).optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ConversationEventOut"])
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
    types["GoogleCloudDialogflowV2beta1WebhookRequestIn"] = t.struct(
        {
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1QueryResultIn"]
            ).optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestIn"]
            ).optional(),
            "alternativeQueryResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1QueryResultIn"])
            ).optional(),
            "responseId": t.string().optional(),
            "session": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookRequestIn"])
    types["GoogleCloudDialogflowV2beta1WebhookRequestOut"] = t.struct(
        {
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1QueryResultOut"]
            ).optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2beta1OriginalDetectIntentRequestOut"]
            ).optional(),
            "alternativeQueryResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1QueryResultOut"])
            ).optional(),
            "responseId": t.string().optional(),
            "session": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookRequestOut"])
    types["GoogleCloudDialogflowCxV3OutputAudioConfigIn"] = t.struct(
        {
            "audioEncoding": t.string(),
            "sampleRateHertz": t.integer().optional(),
            "synthesizeSpeechConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3OutputAudioConfigOut"] = t.struct(
        {
            "audioEncoding": t.string(),
            "sampleRateHertz": t.integer().optional(),
            "synthesizeSpeechConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3SynthesizeSpeechConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"])
    types["GoogleCloudDialogflowV2InputDatasetIn"] = t.struct(
        {"dataset": t.string()}
    ).named(renames["GoogleCloudDialogflowV2InputDatasetIn"])
    types["GoogleCloudDialogflowV2InputDatasetOut"] = t.struct(
        {"dataset": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2InputDatasetOut"])
    types["GoogleCloudDialogflowCxV3ListFlowsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "flows": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FlowIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListFlowsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListFlowsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "flows": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3FlowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn"] = t.struct(
        {
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1QueryInputIn"]
            ).optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputIn"])
    types["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut"] = t.struct(
        {
            "input": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1QueryInputOut"]
            ).optional(),
            "injectedParameters": t.struct({"_": t.string().optional()}).optional(),
            "isWebhookEnabled": t.boolean().optional(),
            "enableSentimentAnalysis": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnUserInputOut"])
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
    types["GoogleCloudDialogflowV2IntentMessageTableCardCellIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellIn"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardCellOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardCellOut"])
    types["GoogleCloudDialogflowCxV3FulfillmentIn"] = t.struct(
        {
            "conditionalCases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesIn"]
                )
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionIn"]
                )
            ).optional(),
            "tag": t.string().optional(),
            "webhook": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentIn"])
    types["GoogleCloudDialogflowCxV3FulfillmentOut"] = t.struct(
        {
            "conditionalCases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentConditionalCasesOut"]
                )
            ).optional(),
            "returnPartialResponses": t.boolean().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "setParameterActions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentSetParameterActionOut"]
                )
            ).optional(),
            "tag": t.string().optional(),
            "webhook": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillmentOut"])
    types["GoogleCloudDialogflowV2EntityTypeIn"] = t.struct(
        {
            "kind": t.string(),
            "autoExpansionMode": t.string().optional(),
            "displayName": t.string(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EntityTypeIn"])
    types["GoogleCloudDialogflowV2EntityTypeOut"] = t.struct(
        {
            "kind": t.string(),
            "autoExpansionMode": t.string().optional(),
            "displayName": t.string(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2EntityTypeEntityOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EntityTypeOut"])
    types["GoogleCloudDialogflowV2GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2GcsDestinationIn"])
    types["GoogleCloudDialogflowV2GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2GcsDestinationOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"] = t.struct(
        {
            "allowedCaCerts": t.array(t.string()).optional(),
            "httpMethod": t.string().optional(),
            "password": t.string().optional(),
            "uri": t.string(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "requestBody": t.string().optional(),
            "webhookType": t.string().optional(),
            "username": t.string().optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"] = t.struct(
        {
            "allowedCaCerts": t.array(t.string()).optional(),
            "httpMethod": t.string().optional(),
            "password": t.string().optional(),
            "uri": t.string(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "requestBody": t.string().optional(),
            "webhookType": t.string().optional(),
            "username": t.string().optional(),
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"])
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
    types["GoogleCloudDialogflowCxV3IntentInputIn"] = t.struct(
        {"intent": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentInputIn"])
    types["GoogleCloudDialogflowCxV3IntentInputOut"] = t.struct(
        {"intent": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentInputOut"])
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
    types["GoogleCloudDialogflowCxV3beta1IntentParameterIn"] = t.struct(
        {
            "redact": t.boolean().optional(),
            "entityType": t.string(),
            "isList": t.boolean().optional(),
            "id": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentParameterIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentParameterOut"] = t.struct(
        {
            "redact": t.boolean().optional(),
            "entityType": t.string(),
            "isList": t.boolean().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentParameterOut"])
    types[
        "GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputIn"
    ] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageIn"]
            ).optional(),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextIn"])
            ).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentIn"]
            ).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
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
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageTextOut"])
            ).optional(),
            "differences": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1TestRunDifferenceOut"])
            ).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentOut"]
            ).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutputOut"]
    )
    types["GoogleCloudDialogflowCxV3QueryInputIn"] = t.struct(
        {
            "dtmf": t.proxy(renames["GoogleCloudDialogflowCxV3DtmfInputIn"]).optional(),
            "languageCode": t.string(),
            "text": t.proxy(renames["GoogleCloudDialogflowCxV3TextInputIn"]).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3AudioInputIn"]
            ).optional(),
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventInputIn"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentInputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryInputIn"])
    types["GoogleCloudDialogflowCxV3QueryInputOut"] = t.struct(
        {
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3DtmfInputOut"]
            ).optional(),
            "languageCode": t.string(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextInputOut"]
            ).optional(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3AudioInputOut"]
            ).optional(),
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3EventInputOut"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryInputOut"])
    types["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn"] = t.struct(
        {
            "matchConfidenceLevel": t.string().optional(),
            "source": t.string().optional(),
            "faqQuestion": t.string().optional(),
            "matchConfidence": t.number().optional(),
            "answer": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerIn"])
    types["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut"] = t.struct(
        {
            "matchConfidenceLevel": t.string().optional(),
            "source": t.string().optional(),
            "faqQuestion": t.string().optional(),
            "matchConfidence": t.number().optional(),
            "answer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswerOut"])
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
    types["GoogleCloudDialogflowV2beta1FaqAnswerIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "source": t.string().optional(),
            "question": t.string().optional(),
            "answerRecord": t.string().optional(),
            "answer": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1FaqAnswerIn"])
    types["GoogleCloudDialogflowV2beta1FaqAnswerOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "source": t.string().optional(),
            "question": t.string().optional(),
            "answerRecord": t.string().optional(),
            "answer": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1FaqAnswerOut"])
    types["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"] = t.struct(
        {"tag": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"])
    types["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"])
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
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentIn"] = t.struct(
        {
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"])
            ).optional(),
            "parentFollowupIntentName": t.string().optional(),
            "isFallback": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "action": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "endInteraction": t.boolean().optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentParameterIn"])
            ).optional(),
            "priority": t.integer().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "mlEnabled": t.boolean().optional(),
            "displayName": t.string(),
            "mlDisabled": t.boolean().optional(),
            "webhookState": t.string().optional(),
            "resetContexts": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentIn"])
    types["GoogleCloudDialogflowV2beta1IntentOut"] = t.struct(
        {
            "defaultResponsePlatforms": t.array(t.string()).optional(),
            "rootFollowupIntentName": t.string().optional(),
            "inputContextNames": t.array(t.string()).optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"])
            ).optional(),
            "followupIntentInfo": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut"]
                )
            ).optional(),
            "parentFollowupIntentName": t.string().optional(),
            "isFallback": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "action": t.string().optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "endInteraction": t.boolean().optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentParameterOut"])
            ).optional(),
            "priority": t.integer().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "mlEnabled": t.boolean().optional(),
            "displayName": t.string(),
            "mlDisabled": t.boolean().optional(),
            "webhookState": t.string().optional(),
            "resetContexts": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentOut"])
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
    types["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportDocumentsResponseOut"])
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
    types["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"] = t.struct(
        {"version": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"] = t.struct(
        {"version": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfigOut"])
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
    types["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn"] = t.struct(
        {
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"]
            ).optional(),
            "service": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut"] = t.struct(
        {
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"]
            ).optional(),
            "service": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut"])
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
    types["GoogleCloudDialogflowCxV3RestoreAgentRequestIn"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "agentContent": t.string().optional(),
            "restoreOption": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RestoreAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3RestoreAgentRequestOut"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "agentContent": t.string().optional(),
            "restoreOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RestoreAgentRequestOut"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoIn"] = t.struct(
        {
            "currentPage": t.string().optional(),
            "displayName": t.string().optional(),
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoOut"] = t.struct(
        {
            "currentPage": t.string().optional(),
            "displayName": t.string().optional(),
            "formInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoOut"])
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
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn"] = t.struct(
        {"text": t.string().optional(), "ssml": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"] = t.struct(
        {
            "text": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "ssml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioTextOut"])
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
    types["GoogleCloudDialogflowCxV3TransitionRouteIn"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ).optional(),
            "intent": t.string().optional(),
            "condition": t.string().optional(),
            "targetFlow": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
    types["GoogleCloudDialogflowCxV3TransitionRouteOut"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "name": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ).optional(),
            "intent": t.string().optional(),
            "condition": t.string().optional(),
            "targetFlow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteOut"])
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
    types["GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn"] = t.struct(
        {
            "latestMessage": t.string().optional(),
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2FaqAnswerIn"])
            ).optional(),
            "contextSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseIn"])
    types["GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut"] = t.struct(
        {
            "latestMessage": t.string().optional(),
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2FaqAnswerOut"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestFaqAnswersResponseOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageEndInteractionOut"])
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
    types["GoogleCloudDialogflowCxV3beta1EventInputIn"] = t.struct(
        {"event": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventInputIn"])
    types["GoogleCloudDialogflowCxV3beta1EventInputOut"] = t.struct(
        {
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventInputOut"])
    types["GoogleCloudDialogflowCxV3WebhookRequestIn"] = t.struct(
        {
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIn"]
            ).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultIn"
                ]
            ).optional(),
            "triggerIntent": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoIn"]
            ).optional(),
            "triggerEvent": t.string().optional(),
            "languageCode": t.string().optional(),
            "text": t.string().optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoIn"]
            ).optional(),
            "dtmfDigits": t.string().optional(),
            "transcript": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "detectIntentResponseId": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestIn"])
    types["GoogleCloudDialogflowCxV3WebhookRequestOut"] = t.struct(
        {
            "intentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestIntentInfoOut"]
            ).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResultOut"
                ]
            ).optional(),
            "triggerIntent": t.string().optional(),
            "sessionInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3SessionInfoOut"]
            ).optional(),
            "triggerEvent": t.string().optional(),
            "languageCode": t.string().optional(),
            "text": t.string().optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageInfoOut"]
            ).optional(),
            "dtmfDigits": t.string().optional(),
            "transcript": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "detectIntentResponseId": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "fulfillmentInfo": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookRequestOut"])
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
    types["GoogleCloudDialogflowCxV3ContinuousTestResultIn"] = t.struct(
        {
            "result": t.string().optional(),
            "name": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
            "runTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ContinuousTestResultIn"])
    types["GoogleCloudDialogflowCxV3ContinuousTestResultOut"] = t.struct(
        {
            "result": t.string().optional(),
            "name": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
            "runTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ContinuousTestResultOut"])
    types["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "targetPage": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
            "intent": t.string().optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteIn"])
    types["GoogleCloudDialogflowCxV3beta1TransitionRouteOut"] = t.struct(
        {
            "targetFlow": t.string().optional(),
            "targetPage": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "intent": t.string().optional(),
            "condition": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TransitionRouteOut"])
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
    types["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"] = t.struct(
        {"metadata": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageConversationSuccessOut"])
    types["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"] = t.struct(
        {
            "audioFormat": t.string().optional(),
            "audioExportPattern": t.string().optional(),
            "enableAudioRedaction": t.boolean().optional(),
            "gcsBucket": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"] = t.struct(
        {
            "audioFormat": t.string().optional(),
            "audioExportPattern": t.string().optional(),
            "enableAudioRedaction": t.boolean().optional(),
            "gcsBucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"])
            ),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectIn"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"]
                )
            ),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectOut"])
    types["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn"] = t.struct(
        {
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SuggestionResultIn"])
            ).optional(),
            "conversation": t.string().optional(),
            "participant": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventIn"])
    types["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut"] = t.struct(
        {
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SuggestionResultOut"])
            ).optional(),
            "conversation": t.string().optional(),
            "participant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1HumanAgentAssistantEventOut"])
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
    types["GoogleCloudDialogflowCxV3RunContinuousTestRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestRequestIn"])
    types["GoogleCloudDialogflowCxV3RunContinuousTestRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3RunContinuousTestRequestOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleCloudDialogflowV2beta1MessageIn"] = t.struct(
        {
            "content": t.string(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "sendTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1MessageIn"])
    types["GoogleCloudDialogflowV2beta1MessageOut"] = t.struct(
        {
            "participant": t.string().optional(),
            "content": t.string(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "participantRole": t.string().optional(),
            "sentimentAnalysis": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "messageAnnotation": t.proxy(
                renames["GoogleCloudDialogflowV2beta1MessageAnnotationOut"]
            ).optional(),
            "sendTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1MessageOut"])
    types["GoogleCloudDialogflowCxV3beta1TestErrorIn"] = t.struct(
        {
            "testCase": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "testTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestErrorIn"])
    types["GoogleCloudDialogflowCxV3beta1TestErrorOut"] = t.struct(
        {
            "testCase": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "testTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestErrorOut"])
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
    types[
        "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationProfile": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "participantRole": t.string(),
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
            "conversationProfile": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "participantRole": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadataOut"
        ]
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
    types["GoogleCloudDialogflowCxV3AgentIn"] = t.struct(
        {
            "speechToTextSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"]
            ).optional(),
            "enableSpellCorrection": t.boolean().optional(),
            "supportedLanguageCodes": t.array(t.string()).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "timeZone": t.string(),
            "name": t.string().optional(),
            "securitySettings": t.string().optional(),
            "startFlow": t.string().optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "locked": t.boolean().optional(),
            "textToSpeechSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextToSpeechSettingsIn"]
            ).optional(),
            "advancedSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsIn"]
            ).optional(),
            "avatarUri": t.string().optional(),
            "defaultLanguageCode": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentIn"])
    types["GoogleCloudDialogflowCxV3AgentOut"] = t.struct(
        {
            "speechToTextSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"]
            ).optional(),
            "enableSpellCorrection": t.boolean().optional(),
            "supportedLanguageCodes": t.array(t.string()).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "timeZone": t.string(),
            "name": t.string().optional(),
            "securitySettings": t.string().optional(),
            "startFlow": t.string().optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "locked": t.boolean().optional(),
            "textToSpeechSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3TextToSpeechSettingsOut"]
            ).optional(),
            "advancedSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3AdvancedSettingsOut"]
            ).optional(),
            "avatarUri": t.string().optional(),
            "defaultLanguageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3AgentOut"])
    types["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"] = t.struct(
        {
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ArticleAnswerIn"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"] = t.struct(
        {
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ArticleAnswerOut"])
            ).optional(),
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestArticlesResponseOut"])
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
    types["GoogleCloudDialogflowCxV3TextInputIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3TextInputIn"])
    types["GoogleCloudDialogflowCxV3TextInputOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TextInputOut"])
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
    types["GoogleCloudDialogflowCxV3ValidateAgentRequestIn"] = t.struct(
        {"languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ValidateAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3ValidateAgentRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidateAgentRequestOut"])
    types["GoogleCloudDialogflowCxV3beta1FormParameterIn"] = t.struct(
        {
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorIn"]
            ),
            "displayName": t.string(),
            "isList": t.boolean().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "redact": t.boolean().optional(),
            "required": t.boolean().optional(),
            "entityType": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterIn"])
    types["GoogleCloudDialogflowCxV3beta1FormParameterOut"] = t.struct(
        {
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FormParameterFillBehaviorOut"]
            ),
            "displayName": t.string(),
            "isList": t.boolean().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "redact": t.boolean().optional(),
            "required": t.boolean().optional(),
            "entityType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FormParameterOut"])
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
    types["GoogleCloudDialogflowCxV3beta1EventHandlerIn"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "targetFlow": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentIn"]
            ).optional(),
            "event": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventHandlerIn"])
    types["GoogleCloudDialogflowCxV3beta1EventHandlerOut"] = t.struct(
        {
            "targetPage": t.string().optional(),
            "targetFlow": t.string().optional(),
            "triggerFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentOut"]
            ).optional(),
            "name": t.string().optional(),
            "event": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EventHandlerOut"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardIn"] = t.struct(
        {
            "formattedText": t.string(),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageBasicCardOut"] = t.struct(
        {
            "formattedText": t.string(),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageBasicCardOut"])
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
    types["GoogleCloudDialogflowCxV3ImportFlowResponseIn"] = t.struct(
        {"flow": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowResponseIn"])
    types["GoogleCloudDialogflowCxV3ImportFlowResponseOut"] = t.struct(
        {
            "flow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ImportFlowResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1TurnSignalsIn"] = t.struct(
        {
            "failureReasons": t.array(t.string()).optional(),
            "reachedEndPage": t.boolean().optional(),
            "dtmfUsed": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "noUserInput": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "sentimentMagnitude": t.number().optional(),
            "agentEscalated": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TurnSignalsIn"])
    types["GoogleCloudDialogflowCxV3beta1TurnSignalsOut"] = t.struct(
        {
            "failureReasons": t.array(t.string()).optional(),
            "reachedEndPage": t.boolean().optional(),
            "dtmfUsed": t.boolean().optional(),
            "userEscalated": t.boolean().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "noUserInput": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "sentimentMagnitude": t.number().optional(),
            "agentEscalated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TurnSignalsOut"])
    types["GoogleCloudDialogflowV2ConversationEventIn"] = t.struct(
        {
            "type": t.string().optional(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "conversation": t.string().optional(),
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2MessageIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationEventIn"])
    types["GoogleCloudDialogflowV2ConversationEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "errorStatus": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "conversation": t.string().optional(),
            "newMessagePayload": t.proxy(
                renames["GoogleCloudDialogflowV2MessageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ConversationEventOut"])
    types["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"] = t.struct(
        {"value": t.string(), "synonyms": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"])
    types["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"] = t.struct(
        {
            "value": t.string(),
            "synonyms": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"])
    types["GoogleCloudDialogflowCxV3QueryResultIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "languageCode": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "transcript": t.string().optional(),
            "webhookStatuses": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
            "responseMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentIn"]).optional(),
            "dtmf": t.proxy(renames["GoogleCloudDialogflowCxV3DtmfInputIn"]).optional(),
            "triggerEvent": t.string().optional(),
            "text": t.string().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultIn"]
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
            "triggerIntent": t.string().optional(),
            "webhookPayloads": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryResultIn"])
    types["GoogleCloudDialogflowCxV3QueryResultOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "languageCode": t.string().optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "transcript": t.string().optional(),
            "webhookStatuses": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "responseMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "intentDetectionConfidence": t.number().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]).optional(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3DtmfInputOut"]
            ).optional(),
            "triggerEvent": t.string().optional(),
            "text": t.string().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3SentimentAnalysisResultOut"]
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "triggerIntent": t.string().optional(),
            "webhookPayloads": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3QueryResultOut"])
    types["GoogleCloudDialogflowCxV3MatchIntentResponseIn"] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
            "matches": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"])
            ).optional(),
            "transcript": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "text": t.string().optional(),
            "triggerEvent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentResponseIn"])
    types["GoogleCloudDialogflowCxV3MatchIntentResponseOut"] = t.struct(
        {
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "matches": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"])
            ).optional(),
            "transcript": t.string().optional(),
            "triggerIntent": t.string().optional(),
            "text": t.string().optional(),
            "triggerEvent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentResponseOut"])
    types["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"] = t.struct(
        {
            "name": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"])
            ),
            "entityOverrideMode": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"])
    types["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"] = t.struct(
        {
            "name": t.string(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"])
            ),
            "entityOverrideMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"])
    types["GoogleCloudDialogflowCxV3MatchIntentRequestIn"] = t.struct(
        {
            "persistParameterChanges": t.boolean().optional(),
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputIn"]),
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"])
    types["GoogleCloudDialogflowCxV3MatchIntentRequestOut"] = t.struct(
        {
            "persistParameterChanges": t.boolean().optional(),
            "queryInput": t.proxy(renames["GoogleCloudDialogflowCxV3QueryInputOut"]),
            "queryParams": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIntentRequestOut"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageIn"] = t.struct(
        {
            "transitions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionIn"]
                )
            ).optional(),
            "coverageScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageIn"])
    types["GoogleCloudDialogflowCxV3TransitionCoverageOut"] = t.struct(
        {
            "transitions": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3TransitionCoverageTransitionOut"]
                )
            ).optional(),
            "coverageScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionCoverageOut"])
    types[
        "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueIn"
    ] = t.struct(
        {
            "resolvedValue": t.struct({"_": t.string().optional()}).optional(),
            "originalValue": t.string().optional(),
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
            "resolvedValue": t.struct({"_": t.string().optional()}).optional(),
            "originalValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValueOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3ExportAgentRequestIn"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "environment": t.string().optional(),
            "dataFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentRequestIn"])
    types["GoogleCloudDialogflowCxV3ExportAgentRequestOut"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "environment": t.string().optional(),
            "dataFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportAgentRequestOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "reply": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"])
    types["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "reply": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"])
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
    types["GoogleCloudDialogflowV2beta1ArticleAnswerIn"] = t.struct(
        {
            "snippets": t.array(t.string()).optional(),
            "answerRecord": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ArticleAnswerIn"])
    types["GoogleCloudDialogflowV2beta1ArticleAnswerOut"] = t.struct(
        {
            "snippets": t.array(t.string()).optional(),
            "answerRecord": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ArticleAnswerOut"])
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
    types["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn"] = t.struct(
        {"ssml": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut"] = t.struct(
        {
            "allowPlaybackInterruption": t.boolean().optional(),
            "ssml": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageOutputAudioTextOut"])
    types["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"] = t.struct(
        {"enableSpeechAdaptation": t.boolean().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsIn"])
    types["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"] = t.struct(
        {
            "enableSpeechAdaptation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SpeechToTextSettingsOut"])
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
    types[
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn"
    ] = t.struct(
        {
            "message": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"]
            ).optional(),
            "additionalCases": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesIn"]
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
            "message": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"]
            ).optional(),
            "additionalCases": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionIn"])
    types["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteractionOut"])
    types["GoogleCloudDialogflowCxV3VersionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionIn"])
    types["GoogleCloudDialogflowCxV3VersionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "nluSettings": t.proxy(
                renames["GoogleCloudDialogflowCxV3NluSettingsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "displayName": t.string(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionOut"])
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
    types["GoogleCloudDialogflowCxV3IntentCoverageIntentIn"] = t.struct(
        {"intent": t.string().optional(), "covered": t.boolean().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3IntentCoverageIntentIn"])
    types["GoogleCloudDialogflowCxV3IntentCoverageIntentOut"] = t.struct(
        {
            "intent": t.string().optional(),
            "covered": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentCoverageIntentOut"])
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
    types["GoogleCloudDialogflowV2beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1GcsDestinationIn"])
    types["GoogleCloudDialogflowV2beta1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1GcsDestinationOut"])
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
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
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
    types["GoogleCloudDialogflowCxV3DeployFlowRequestIn"] = t.struct(
        {"flowVersion": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3DeployFlowRequestOut"] = t.struct(
        {
            "flowVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3DeployFlowRequestOut"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"] = t.struct(
        {
            "text": t.string(),
            "userDefined": t.boolean().optional(),
            "entityType": t.string().optional(),
            "alias": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"] = t.struct(
        {
            "text": t.string(),
            "userDefined": t.boolean().optional(),
            "entityType": t.string().optional(),
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"])
    types["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1RunTestCaseMetadataOut"])
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
    types["GoogleCloudDialogflowCxV3beta1TestCaseIn"] = t.struct(
        {
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseResultIn"]
            ).optional(),
            "notes": t.string().optional(),
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnIn"])
            ).optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestConfigIn"]
            ).optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseIn"])
    types["GoogleCloudDialogflowCxV3beta1TestCaseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "lastTestResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestCaseResultOut"]
            ).optional(),
            "notes": t.string().optional(),
            "testCaseConversationTurns": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ConversationTurnOut"])
            ).optional(),
            "testConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TestConfigOut"]
            ).optional(),
            "creationTime": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1TestCaseOut"])
    types["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "minDuration": t.string().optional(),
            "trafficPercent": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn"])
    types["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "minDuration": t.string().optional(),
            "trafficPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn"] = t.struct(
        {"title": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageSuggestionOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn"] = t.struct(
        {
            "cardWidth": t.string(),
            "cardContents": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"]
                )
            ),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut"] = t.struct(
        {
            "cardWidth": t.string(),
            "cardContents": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCardOut"])
    types["GoogleCloudDialogflowV2HumanAgentAssistantEventIn"] = t.struct(
        {
            "participant": t.string().optional(),
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SuggestionResultIn"])
            ).optional(),
            "conversation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2HumanAgentAssistantEventIn"])
    types["GoogleCloudDialogflowV2HumanAgentAssistantEventOut"] = t.struct(
        {
            "participant": t.string().optional(),
            "suggestionResults": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SuggestionResultOut"])
            ).optional(),
            "conversation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2HumanAgentAssistantEventOut"])
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
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn"
    ] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageIn"])
            ).optional(),
            "mergeBehavior": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseIn"]
    )
    types[
        "GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut"
    ] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1ResponseMessageOut"])
            ).optional(),
            "mergeBehavior": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponseOut"]
    )
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
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"] = t.struct(
        {
            "timesAddedCount": t.integer().optional(),
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartIn"]
                )
            ),
            "type": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"] = t.struct(
        {
            "timesAddedCount": t.integer().optional(),
            "parts": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentTrainingPhrasePartOut"]
                )
            ),
            "type": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentTrainingPhraseOut"])
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
    types["GoogleCloudDialogflowV2IntentMessageTextIn"] = t.struct(
        {"text": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTextIn"])
    types["GoogleCloudDialogflowV2IntentMessageTextOut"] = t.struct(
        {
            "text": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTextOut"])
    types["GoogleCloudDialogflowCxV3ValidateFlowRequestIn"] = t.struct(
        {"languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ValidateFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3ValidateFlowRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ValidateFlowRequestOut"])
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
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectIn"
    ] = t.struct(
        {
            "contentUrl": t.string(),
            "name": t.string(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "description": t.string().optional(),
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
            "name": t.string(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObjectOut"
        ]
    )
    types["GoogleCloudDialogflowV2QueryResultIn"] = t.struct(
        {
            "intentDetectionConfidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "action": t.string().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowV2IntentIn"]).optional(),
            "webhookSource": t.string().optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultIn"]
            ).optional(),
            "queryText": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "fulfillmentText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2QueryResultIn"])
    types["GoogleCloudDialogflowV2QueryResultOut"] = t.struct(
        {
            "intentDetectionConfidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "action": t.string().optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowV2IntentOut"]).optional(),
            "webhookSource": t.string().optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2SentimentAnalysisResultOut"]
            ).optional(),
            "queryText": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "fulfillmentText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2QueryResultOut"])
    types["GoogleCloudDialogflowCxV3beta1InputAudioConfigIn"] = t.struct(
        {
            "modelVariant": t.string().optional(),
            "singleUtterance": t.boolean().optional(),
            "model": t.string().optional(),
            "audioEncoding": t.string(),
            "phraseHints": t.array(t.string()).optional(),
            "sampleRateHertz": t.integer().optional(),
            "enableWordInfo": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1InputAudioConfigOut"] = t.struct(
        {
            "modelVariant": t.string().optional(),
            "singleUtterance": t.boolean().optional(),
            "model": t.string().optional(),
            "audioEncoding": t.string(),
            "phraseHints": t.array(t.string()).optional(),
            "sampleRateHertz": t.integer().optional(),
            "enableWordInfo": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1InputAudioConfigOut"])
    types["GoogleCloudDialogflowV2beta1ExportAgentResponseIn"] = t.struct(
        {"agentUri": t.string().optional(), "agentContent": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1ExportAgentResponseIn"])
    types["GoogleCloudDialogflowV2beta1ExportAgentResponseOut"] = t.struct(
        {
            "agentUri": t.string().optional(),
            "agentContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ExportAgentResponseOut"])
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
    types["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn"] = t.struct(
        {"names": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseIn"])
    types["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ImportTestCasesResponseOut"])
    types["GoogleCloudDialogflowCxV3ListIntentsResponseIn"] = t.struct(
        {
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListIntentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListIntentsResponseOut"] = t.struct(
        {
            "intents": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListIntentsResponseOut"])
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
    types[
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn"
    ] = t.struct(
        {
            "name": t.string(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "description": t.string().optional(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "contentUrl": t.string(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectIn"]
    )
    types[
        "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut"
    ] = t.struct(
        {
            "name": t.string(),
            "largeImage": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "description": t.string().optional(),
            "icon": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "contentUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObjectOut"
        ]
    )
    types["GoogleCloudDialogflowV2FaqAnswerIn"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
            "answer": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "question": t.string().optional(),
            "source": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2FaqAnswerIn"])
    types["GoogleCloudDialogflowV2FaqAnswerOut"] = t.struct(
        {
            "answerRecord": t.string().optional(),
            "confidence": t.number().optional(),
            "answer": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "question": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2FaqAnswerOut"])
    types["GoogleCloudDialogflowCxV3SessionEntityTypeIn"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
            ),
            "entityOverrideMode": t.string(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionEntityTypeIn"])
    types["GoogleCloudDialogflowCxV3SessionEntityTypeOut"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityOut"])
            ),
            "entityOverrideMode": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SessionEntityTypeOut"])
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
    types["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn"] = t.struct(
        {
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageTextIn"])
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageIn"]
            ).optional(),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentIn"]
            ).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputIn"])
    types["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut"] = t.struct(
        {
            "diagnosticInfo": t.struct({"_": t.string().optional()}),
            "textResponses": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageTextOut"])
            ).optional(),
            "differences": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3TestRunDifferenceOut"])
            ).optional(),
            "currentPage": t.proxy(
                renames["GoogleCloudDialogflowCxV3PageOut"]
            ).optional(),
            "triggeredIntent": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentOut"]
            ).optional(),
            "sessionParameters": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputOut"])
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
    types["GoogleCloudDialogflowCxV3IntentParameterIn"] = t.struct(
        {
            "isList": t.boolean().optional(),
            "id": t.string(),
            "redact": t.boolean().optional(),
            "entityType": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
    types["GoogleCloudDialogflowCxV3IntentParameterOut"] = t.struct(
        {
            "isList": t.boolean().optional(),
            "id": t.string(),
            "redact": t.boolean().optional(),
            "entityType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentParameterOut"])
    types["GoogleCloudDialogflowCxV3StartExperimentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StartExperimentRequestIn"])
    types["GoogleCloudDialogflowCxV3StartExperimentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3StartExperimentRequestOut"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadataOut"])
    types["GoogleCloudDialogflowCxV3ListExperimentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "experiments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListExperimentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListExperimentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "experiments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListExperimentsResponseOut"])
    types["GoogleCloudDialogflowCxV3TrainFlowRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TrainFlowRequestIn"])
    types["GoogleCloudDialogflowCxV3TrainFlowRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3TrainFlowRequestOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn"] = t.struct(
        {
            "followupIntentName": t.string().optional(),
            "parentFollowupIntentName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoIn"])
    types["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut"] = t.struct(
        {
            "followupIntentName": t.string().optional(),
            "parentFollowupIntentName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentFollowupIntentInfoOut"])
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
    types["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "smartReplyAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "latestMessage": t.string().optional(),
            "smartReplyAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SmartReplyAnswerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseOut"])
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
    types["GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesMetadataIn"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesMetadataOut"])
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
    types["GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ImportDocumentsResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn"] = t.struct(
        {
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"]
            ),
            "description": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "title": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut"] = t.struct(
        {
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"]
            ),
            "description": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItemOut"])
    types["GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListEnvironmentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EnvironmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListEnvironmentsResponseOut"])
    types["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn"] = t.struct(
        {
            "condition": t.string().optional(),
            "caseContent": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseIn"])
    types[
        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut"
    ] = t.struct(
        {
            "condition": t.string().optional(),
            "caseContent": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContentOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseOut"]
    )
    types["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"] = t.struct(
        {"trainingModelType": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataIn"])
    types["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"] = t.struct(
        {
            "trainingModelType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleSuggestionModelMetadataOut"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"] = t.struct(
        {
            "testCases": t.array(t.string()).optional(),
            "enableContinuousRun": t.boolean().optional(),
            "enablePredeploymentRun": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigIn"])
    types["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"] = t.struct(
        {
            "testCases": t.array(t.string()).optional(),
            "enableContinuousRun": t.boolean().optional(),
            "enablePredeploymentRun": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfigOut"])
    types["GoogleCloudDialogflowV2ArticleAnswerIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "snippets": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "answerRecord": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleAnswerIn"])
    types["GoogleCloudDialogflowV2ArticleAnswerOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "snippets": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "answerRecord": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ArticleAnswerOut"])
    types["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn"] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageIn"])
            ).optional(),
            "mergeBehavior": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseIn"])
    types["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut"] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3ResponseMessageOut"])
            ).optional(),
            "mergeBehavior": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTextIn"] = t.struct(
        {"text": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTextIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTextOut"] = t.struct(
        {
            "text": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTextOut"])
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
    types["GoogleCloudDialogflowV2ContextIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "lifespanCount": t.integer().optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2ContextIn"])
    types["GoogleCloudDialogflowV2ContextOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "lifespanCount": t.integer().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ContextOut"])
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
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationDataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "conversationDataset": t.string().optional(),
            "partialFailures": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2ImportConversationDataOperationMetadataOut"]
    )
    types["GoogleCloudDialogflowCxV3CalculateCoverageResponseIn"] = t.struct(
        {
            "routeGroupCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageIn"]
            ).optional(),
            "transitionCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageIn"]
            ).optional(),
            "intentCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentCoverageIn"]
            ).optional(),
            "agent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CalculateCoverageResponseIn"])
    types["GoogleCloudDialogflowCxV3CalculateCoverageResponseOut"] = t.struct(
        {
            "routeGroupCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageOut"]
            ).optional(),
            "transitionCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionCoverageOut"]
            ).optional(),
            "intentCoverage": t.proxy(
                renames["GoogleCloudDialogflowCxV3IntentCoverageOut"]
            ).optional(),
            "agent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CalculateCoverageResponseOut"])
    types["GoogleCloudDialogflowCxV3TurnSignalsIn"] = t.struct(
        {
            "reachedEndPage": t.boolean().optional(),
            "agentEscalated": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "userEscalated": t.boolean().optional(),
            "noUserInput": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "sentimentMagnitude": t.number().optional(),
            "dtmfUsed": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TurnSignalsIn"])
    types["GoogleCloudDialogflowCxV3TurnSignalsOut"] = t.struct(
        {
            "reachedEndPage": t.boolean().optional(),
            "agentEscalated": t.boolean().optional(),
            "sentimentScore": t.number().optional(),
            "userEscalated": t.boolean().optional(),
            "noUserInput": t.boolean().optional(),
            "noMatch": t.boolean().optional(),
            "webhookStatuses": t.array(t.string()).optional(),
            "sentimentMagnitude": t.number().optional(),
            "dtmfUsed": t.boolean().optional(),
            "failureReasons": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TurnSignalsOut"])
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
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"] = t.struct(
        {"tag": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfoOut"])
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
    ] = t.struct(
        {
            "footer": t.string().optional(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
                ]
            ),
            "description": t.string().optional(),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
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
            "footer": t.string().optional(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
                ]
            ),
            "description": t.string().optional(),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
        ]
    )
    types["GoogleCloudDialogflowV2IntentMessageCardButtonIn"] = t.struct(
        {"postback": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardButtonIn"])
    types["GoogleCloudDialogflowV2IntentMessageCardButtonOut"] = t.struct(
        {
            "postback": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageCardButtonOut"])
    types["GoogleCloudDialogflowCxV3GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3GcsDestinationIn"])
    types["GoogleCloudDialogflowCxV3GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3GcsDestinationOut"])
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
            "name": t.string().optional(),
            "runTime": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ContinuousTestResultIn"])
    types["GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut"] = t.struct(
        {
            "result": t.string().optional(),
            "name": t.string().optional(),
            "runTime": t.string().optional(),
            "testCaseResults": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1ContinuousTestResultOut"])
    types["GoogleCloudDialogflowV2IntentParameterIn"] = t.struct(
        {
            "isList": t.boolean().optional(),
            "prompts": t.array(t.string()).optional(),
            "value": t.string().optional(),
            "mandatory": t.boolean().optional(),
            "entityTypeDisplayName": t.string().optional(),
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentParameterIn"])
    types["GoogleCloudDialogflowV2IntentParameterOut"] = t.struct(
        {
            "isList": t.boolean().optional(),
            "prompts": t.array(t.string()).optional(),
            "value": t.string().optional(),
            "mandatory": t.boolean().optional(),
            "entityTypeDisplayName": t.string().optional(),
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentParameterOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "formattedText": t.string(),
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"
                    ]
                )
            ).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "formattedText": t.string(),
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"
                    ]
                )
            ).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageBasicCardOut"])
    types[
        "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemIn"
    ] = t.struct(
        {
            "title": t.string(),
            "footer": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionIn"
                ]
            ),
            "description": t.string().optional(),
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
            "title": t.string(),
            "footer": t.string().optional(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "openUriAction": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlActionOut"
                ]
            ),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOut"
        ]
    )
    types["GoogleCloudDialogflowCxV3beta1QueryInputIn"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EventInputIn"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TextInputIn"]
            ).optional(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1DtmfInputIn"]
            ).optional(),
            "languageCode": t.string(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1AudioInputIn"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentInputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1QueryInputIn"])
    types["GoogleCloudDialogflowCxV3beta1QueryInputOut"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1EventInputOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1TextInputOut"]
            ).optional(),
            "dtmf": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1DtmfInputOut"]
            ).optional(),
            "languageCode": t.string(),
            "audio": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1AudioInputOut"]
            ).optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1IntentInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1QueryInputOut"])
    types["GoogleCloudDialogflowCxV3TestErrorIn"] = t.struct(
        {
            "testCase": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "testTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestErrorIn"])
    types["GoogleCloudDialogflowCxV3TestErrorOut"] = t.struct(
        {
            "testCase": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "testTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestErrorOut"])
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
    types["GoogleCloudDialogflowV2SuggestArticlesResponseIn"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ArticleAnswerIn"])
            ).optional(),
            "latestMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestArticlesResponseIn"])
    types["GoogleCloudDialogflowV2SuggestArticlesResponseOut"] = t.struct(
        {
            "contextSize": t.integer().optional(),
            "articleAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ArticleAnswerOut"])
            ).optional(),
            "latestMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SuggestArticlesResponseOut"])
    types["GoogleCloudLocationListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseIn"])
    types["GoogleCloudLocationListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseOut"])
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
    types["GoogleCloudDialogflowCxV3WebhookIn"] = t.struct(
        {
            "name": t.string().optional(),
            "timeout": t.string().optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
            ).optional(),
            "displayName": t.string(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
            ).optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookIn"])
    types["GoogleCloudDialogflowCxV3WebhookOut"] = t.struct(
        {
            "name": t.string().optional(),
            "timeout": t.string().optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"]
            ).optional(),
            "displayName": t.string(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut"]
            ).optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookOut"])
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
    types["GoogleCloudDialogflowCxV3beta1IntentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "priority": t.integer().optional(),
            "displayName": t.string(),
            "isFallback": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentParameterIn"])
            ).optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseIn"])
            ).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "priority": t.integer().optional(),
            "displayName": t.string(),
            "isFallback": t.boolean().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3beta1IntentParameterOut"])
            ).optional(),
            "trainingPhrases": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowCxV3beta1IntentTrainingPhraseOut"]
                )
            ).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentOut"])
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
    types["GoogleCloudDialogflowCxV3InputAudioConfigIn"] = t.struct(
        {
            "singleUtterance": t.boolean().optional(),
            "enableWordInfo": t.boolean().optional(),
            "audioEncoding": t.string(),
            "phraseHints": t.array(t.string()).optional(),
            "modelVariant": t.string().optional(),
            "model": t.string().optional(),
            "sampleRateHertz": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3InputAudioConfigIn"])
    types["GoogleCloudDialogflowCxV3InputAudioConfigOut"] = t.struct(
        {
            "singleUtterance": t.boolean().optional(),
            "enableWordInfo": t.boolean().optional(),
            "audioEncoding": t.string(),
            "phraseHints": t.array(t.string()).optional(),
            "modelVariant": t.string().optional(),
            "model": t.string().optional(),
            "sampleRateHertz": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3InputAudioConfigOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"] = t.struct(
        {
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
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"] = t.struct(
        {
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
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"])
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
    types["GoogleCloudDialogflowCxV3FulfillIntentResponseIn"] = t.struct(
        {
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
            "responseId": t.string().optional(),
            "outputAudio": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseIn"])
    types["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"] = t.struct(
        {
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "responseId": t.string().optional(),
            "outputAudio": t.string().optional(),
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowCxV3QueryResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentResponseOut"])
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
    types["GoogleCloudDialogflowCxV3RolloutConfigIn"] = t.struct(
        {
            "failureCondition": t.string().optional(),
            "rolloutCondition": t.string().optional(),
            "rolloutSteps": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigIn"])
    types["GoogleCloudDialogflowCxV3RolloutConfigOut"] = t.struct(
        {
            "failureCondition": t.string().optional(),
            "rolloutCondition": t.string().optional(),
            "rolloutSteps": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3RolloutConfigRolloutStepOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutConfigOut"])
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
    types["GoogleCloudDialogflowCxV3RolloutStateIn"] = t.struct(
        {
            "stepIndex": t.integer().optional(),
            "startTime": t.string().optional(),
            "step": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutStateIn"])
    types["GoogleCloudDialogflowCxV3RolloutStateOut"] = t.struct(
        {
            "stepIndex": t.integer().optional(),
            "startTime": t.string().optional(),
            "step": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3RolloutStateOut"])
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
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn"
    ] = t.struct(
        {
            "thumbnailUri": t.string().optional(),
            "fileUri": t.string(),
            "height": t.string(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaIn"]
    )
    types[
        "GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut"
    ] = t.struct(
        {
            "thumbnailUri": t.string().optional(),
            "fileUri": t.string(),
            "height": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaOut"]
    )
    types["GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn"] = t.struct(
        {
            "repromptEventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
            ).optional(),
            "initialPromptFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
            ),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn"])
    types["GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut"] = t.struct(
        {
            "repromptEventHandlers": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerOut"])
            ).optional(),
            "initialPromptFulfillment": t.proxy(
                renames["GoogleCloudDialogflowCxV3FulfillmentOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn"] = t.struct(
        {"text": t.string().optional(), "postback": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut"] = t.struct(
        {
            "text": t.string().optional(),
            "postback": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsIn"] = t.struct(
        {
            "redactionScope": t.string().optional(),
            "purgeDataTypes": t.array(t.string()).optional(),
            "deidentifyTemplate": t.string().optional(),
            "redactionStrategy": t.string().optional(),
            "name": t.string().optional(),
            "insightsExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsIn"
                ]
            ).optional(),
            "inspectTemplate": t.string().optional(),
            "audioExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsIn"
                ]
            ).optional(),
            "retentionWindowDays": t.integer().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsIn"])
    types["GoogleCloudDialogflowCxV3SecuritySettingsOut"] = t.struct(
        {
            "redactionScope": t.string().optional(),
            "purgeDataTypes": t.array(t.string()).optional(),
            "deidentifyTemplate": t.string().optional(),
            "redactionStrategy": t.string().optional(),
            "name": t.string().optional(),
            "insightsExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettingsOut"
                ]
            ).optional(),
            "inspectTemplate": t.string().optional(),
            "audioExportSettings": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettingsOut"
                ]
            ).optional(),
            "retentionWindowDays": t.integer().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"])
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
    types["GoogleCloudDialogflowCxV3VersionVariantsVariantIn"] = t.struct(
        {
            "trafficAllocation": t.number().optional(),
            "isControlGroup": t.boolean().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionVariantsVariantIn"])
    types["GoogleCloudDialogflowCxV3VersionVariantsVariantOut"] = t.struct(
        {
            "trafficAllocation": t.number().optional(),
            "isControlGroup": t.boolean().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3VersionVariantsVariantOut"])
    types["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"] = t.struct(
        {"version": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigIn"])
    types["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"] = t.struct(
        {"version": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EnvironmentVersionConfigOut"])
    types["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"] = t.struct(
        {"trainingModelType": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowV2SmartReplyModelMetadataIn"])
    types["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"] = t.struct(
        {
            "trainingModelType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2SmartReplyModelMetadataOut"])
    types["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"] = t.struct(
        {
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
            ).optional(),
            "service": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"])
    types["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut"] = t.struct(
        {
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"]
            ).optional(),
            "service": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigOut"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn"] = t.struct(
        {
            "state": t.string().optional(),
            "justCollected": t.boolean().optional(),
            "required": t.boolean().optional(),
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut"] = t.struct(
        {
            "state": t.string().optional(),
            "justCollected": t.boolean().optional(),
            "required": t.boolean().optional(),
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfoOut"])
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
    types["GoogleCloudDialogflowCxV3beta1WebhookIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "disabled": t.boolean().optional(),
            "serviceDirectory": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "disabled": t.boolean().optional(),
            "serviceDirectory": t.proxy(
                renames[
                    "GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfigOut"
                ]
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "genericWebService": t.proxy(
                renames["GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookOut"])
    types["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn"] = t.struct(
        {
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1FaqAnswerIn"])
            ).optional(),
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseIn"])
    types["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut"] = t.struct(
        {
            "faqAnswers": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1FaqAnswerOut"])
            ).optional(),
            "latestMessage": t.string().optional(),
            "contextSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn"] = t.struct(
        {"uri": t.string().optional(), "audio": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "audio": t.string().optional(),
            "allowPlaybackInterruption": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegmentOut"])
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
    types["GoogleCloudDialogflowCxV3beta1IntentInputIn"] = t.struct(
        {"intent": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentInputIn"])
    types["GoogleCloudDialogflowCxV3beta1IntentInputOut"] = t.struct(
        {"intent": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3beta1IntentInputOut"])
    types["GoogleCloudDialogflowCxV3EntityTypeIn"] = t.struct(
        {
            "enableFuzzyExtraction": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
            ).optional(),
            "autoExpansionMode": t.string().optional(),
            "excludedPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "kind": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeIn"])
    types["GoogleCloudDialogflowCxV3EntityTypeOut"] = t.struct(
        {
            "enableFuzzyExtraction": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeEntityOut"])
            ).optional(),
            "autoExpansionMode": t.string().optional(),
            "excludedPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"])
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeOut"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowIn"])
            ).optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonIn"]
                )
            ).optional(),
            "columnProperties": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesIn"]
                )
            ).optional(),
            "title": t.string(),
            "subtitle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardIn"])
    types["GoogleCloudDialogflowV2IntentMessageTableCardOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageTableCardRowOut"])
            ).optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageBasicCardButtonOut"]
                )
            ).optional(),
            "columnProperties": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2IntentMessageColumnPropertiesOut"]
                )
            ).optional(),
            "title": t.string(),
            "subtitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageTableCardOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn"] = t.struct(
        {
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoIn"]
            ),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut"] = t.struct(
        {
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfoOut"]
            ),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageListSelectItemOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn"] = t.struct(
        {"text": t.string()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardCellOut"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"] = t.struct(
        {
            "description": t.string().optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoIn"]
            ),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemIn"])
    types["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"] = t.struct(
        {
            "description": t.string().optional(),
            "info": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSelectItemInfoOut"]
            ),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageListSelectItemOut"])
    types["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"] = t.struct(
        {
            "lowerBound": t.number().optional(),
            "ratio": t.number().optional(),
            "confidenceLevel": t.number().optional(),
            "upperBound": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalIn"])
    types["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut"] = t.struct(
        {
            "lowerBound": t.number().optional(),
            "ratio": t.number().optional(),
            "confidenceLevel": t.number().optional(),
            "upperBound": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExperimentResultConfidenceIntervalOut"])
    types["GoogleCloudDialogflowV2beta1QueryResultIn"] = t.struct(
        {
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "webhookSource": t.string().optional(),
            "languageCode": t.string().optional(),
            "action": t.string().optional(),
            "intentDetectionConfidence": t.number().optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "queryText": t.string().optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentIn"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultIn"]
            ).optional(),
            "knowledgeAnswers": t.proxy(
                renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersIn"]
            ).optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "fulfillmentText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1QueryResultIn"])
    types["GoogleCloudDialogflowV2beta1QueryResultOut"] = t.struct(
        {
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "webhookSource": t.string().optional(),
            "languageCode": t.string().optional(),
            "action": t.string().optional(),
            "intentDetectionConfidence": t.number().optional(),
            "allRequiredParamsPresent": t.boolean().optional(),
            "cancelsSlotFilling": t.boolean().optional(),
            "webhookPayload": t.struct({"_": t.string().optional()}).optional(),
            "diagnosticInfo": t.struct({"_": t.string().optional()}).optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "queryText": t.string().optional(),
            "intent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentOut"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "sentimentAnalysisResult": t.proxy(
                renames["GoogleCloudDialogflowV2beta1SentimentAnalysisResultOut"]
            ).optional(),
            "knowledgeAnswers": t.proxy(
                renames["GoogleCloudDialogflowV2beta1KnowledgeAnswersOut"]
            ).optional(),
            "speechRecognitionConfidence": t.number().optional(),
            "fulfillmentText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1QueryResultOut"])
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
    types["GoogleCloudDialogflowCxV3ConversationSignalsIn"] = t.struct(
        {"turnSignals": t.proxy(renames["GoogleCloudDialogflowCxV3TurnSignalsIn"])}
    ).named(renames["GoogleCloudDialogflowCxV3ConversationSignalsIn"])
    types["GoogleCloudDialogflowCxV3ConversationSignalsOut"] = t.struct(
        {
            "turnSignals": t.proxy(renames["GoogleCloudDialogflowCxV3TurnSignalsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ConversationSignalsOut"])
    types["GoogleCloudDialogflowCxV3MatchIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "resolvedInput": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "event": t.string().optional(),
            "matchType": t.string().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchIn"])
    types["GoogleCloudDialogflowCxV3MatchOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "resolvedInput": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "event": t.string().optional(),
            "matchType": t.string().optional(),
            "intent": t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3MatchOut"])
    types["GoogleCloudDialogflowV2WebhookResponseIn"] = t.struct(
        {
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageIn"])
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "source": t.string().optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2EventInputIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SessionEntityTypeIn"])
            ).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookResponseIn"])
    types["GoogleCloudDialogflowV2WebhookResponseOut"] = t.struct(
        {
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentMessageOut"])
            ).optional(),
            "fulfillmentText": t.string().optional(),
            "source": t.string().optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2EventInputOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2SessionEntityTypeOut"])
            ).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2ContextOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookResponseOut"])
    types["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataIn"])
    types["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3CreateVersionOperationMetadataOut"])
    types["GoogleCloudDialogflowV2beta1EntityTypeIn"] = t.struct(
        {
            "displayName": t.string(),
            "kind": t.string(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "name": t.string().optional(),
            "autoExpansionMode": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeIn"])
    types["GoogleCloudDialogflowV2beta1EntityTypeOut"] = t.struct(
        {
            "displayName": t.string(),
            "kind": t.string(),
            "enableFuzzyExtraction": t.boolean().optional(),
            "name": t.string().optional(),
            "autoExpansionMode": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1EntityTypeEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EntityTypeOut"])
    types["GoogleCloudDialogflowV2ImportDocumentsResponseIn"] = t.struct(
        {"warnings": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudDialogflowV2ImportDocumentsResponseIn"])
    types["GoogleCloudDialogflowV2ImportDocumentsResponseOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2ImportDocumentsResponseOut"])
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
    types["GoogleCloudDialogflowCxV3EventInputIn"] = t.struct(
        {"event": t.string().optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EventInputIn"])
    types["GoogleCloudDialogflowCxV3EventInputOut"] = t.struct(
        {
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EventInputOut"])
    types["GoogleCloudDialogflowV2EventInputIn"] = t.struct(
        {
            "languageCode": t.string(),
            "name": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EventInputIn"])
    types["GoogleCloudDialogflowV2EventInputOut"] = t.struct(
        {
            "languageCode": t.string(),
            "name": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2EventInputOut"])
    types["GoogleCloudDialogflowV2KnowledgeOperationMetadataIn"] = t.struct(
        {
            "exportOperationMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ExportOperationMetadataIn"]
            ).optional(),
            "knowledgeBase": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2KnowledgeOperationMetadataIn"])
    types["GoogleCloudDialogflowV2KnowledgeOperationMetadataOut"] = t.struct(
        {
            "exportOperationMetadata": t.proxy(
                renames["GoogleCloudDialogflowV2ExportOperationMetadataOut"]
            ).optional(),
            "knowledgeBase": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2KnowledgeOperationMetadataOut"])
    types["GoogleCloudDialogflowCxV3TestCaseErrorIn"] = t.struct(
        {
            "testCase": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseIn"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseErrorIn"])
    types["GoogleCloudDialogflowCxV3TestCaseErrorOut"] = t.struct(
        {
            "testCase": t.proxy(
                renames["GoogleCloudDialogflowCxV3TestCaseOut"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TestCaseErrorOut"])
    types["GoogleCloudDialogflowV2WebhookRequestIn"] = t.struct(
        {
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2QueryResultIn"]
            ).optional(),
            "session": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestIn"]
            ).optional(),
            "responseId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookRequestIn"])
    types["GoogleCloudDialogflowV2WebhookRequestOut"] = t.struct(
        {
            "queryResult": t.proxy(
                renames["GoogleCloudDialogflowV2QueryResultOut"]
            ).optional(),
            "session": t.string().optional(),
            "originalDetectIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowV2OriginalDetectIntentRequestOut"]
            ).optional(),
            "responseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2WebhookRequestOut"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "confidence": t.number().optional(),
            "lastMatchedIntent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIn"])
    types["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "confidence": t.number().optional(),
            "lastMatchedIntent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn"] = t.struct(
        {
            "thumbnailImageAlignment": t.string(),
            "cardContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentIn"]
            ),
            "cardOrientation": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut"] = t.struct(
        {
            "thumbnailImageAlignment": t.string(),
            "cardContent": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentOut"]
            ),
            "cardOrientation": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCardOut"])
    types["GoogleCloudDialogflowV2beta1WebhookResponseIn"] = t.struct(
        {
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeIn"])
            ).optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageIn"])
            ).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "endInteraction": t.boolean().optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2beta1EventInputIn"]
            ).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextIn"])
            ).optional(),
            "source": t.string().optional(),
            "fulfillmentText": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookResponseIn"])
    types["GoogleCloudDialogflowV2beta1WebhookResponseOut"] = t.struct(
        {
            "sessionEntityTypes": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1SessionEntityTypeOut"])
            ).optional(),
            "fulfillmentMessages": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1IntentMessageOut"])
            ).optional(),
            "liveAgentHandoff": t.boolean().optional(),
            "endInteraction": t.boolean().optional(),
            "followupEventInput": t.proxy(
                renames["GoogleCloudDialogflowV2beta1EventInputOut"]
            ).optional(),
            "outputContexts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2beta1ContextOut"])
            ).optional(),
            "source": t.string().optional(),
            "fulfillmentText": t.string().optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1WebhookResponseOut"])
    types["GoogleCloudDialogflowCxV3FulfillIntentRequestIn"] = t.struct(
        {
            "matchIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
            ).optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchIn"]).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentRequestIn"])
    types["GoogleCloudDialogflowCxV3FulfillIntentRequestOut"] = t.struct(
        {
            "matchIntentRequest": t.proxy(
                renames["GoogleCloudDialogflowCxV3MatchIntentRequestOut"]
            ).optional(),
            "match": t.proxy(renames["GoogleCloudDialogflowCxV3MatchOut"]).optional(),
            "outputAudioConfig": t.proxy(
                renames["GoogleCloudDialogflowCxV3OutputAudioConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FulfillIntentRequestOut"])
    types["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"] = t.struct(
        {"metadata": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffIn"])
    types["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoffOut"])
    types[
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "participantRole": t.string(),
            "createTime": t.string().optional(),
            "conversationProfile": t.string().optional(),
            "suggestionFeatureType": t.string(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataIn"]
    )
    types[
        "GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut"
    ] = t.struct(
        {
            "participantRole": t.string(),
            "createTime": t.string().optional(),
            "conversationProfile": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadataOut"]
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
    types["GoogleCloudDialogflowCxV3IntentIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "priority": t.integer().optional(),
            "isFallback": t.boolean().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentIn"])
    types["GoogleCloudDialogflowCxV3IntentOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "priority": t.integer().optional(),
            "isFallback": t.boolean().optional(),
            "trainingPhrases": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseOut"])
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3IntentOut"])
    types["GoogleCloudDialogflowCxV3ListDeploymentsResponseIn"] = t.struct(
        {
            "deployments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3DeploymentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListDeploymentsResponseIn"])
    types["GoogleCloudDialogflowCxV3ListDeploymentsResponseOut"] = t.struct(
        {
            "deployments": t.array(
                t.proxy(renames["GoogleCloudDialogflowCxV3DeploymentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ListDeploymentsResponseOut"])
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
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn"] = t.struct(
        {
            "openUrl": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriIn"
                ]
            ).optional(),
            "dial": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialIn"
                ]
            ).optional(),
            "postbackData": t.string().optional(),
            "shareLocation": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationIn"
                ]
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut"] = t.struct(
        {
            "openUrl": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUriOut"
                ]
            ).optional(),
            "dial": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDialOut"
                ]
            ).optional(),
            "postbackData": t.string().optional(),
            "shareLocation": t.proxy(
                renames[
                    "GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocationOut"
                ]
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionOut"])
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
    types[
        "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "participantRole": t.string(),
            "suggestionFeatureType": t.string(),
            "conversationProfile": t.string().optional(),
            "createTime": t.string().optional(),
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
            "participantRole": t.string(),
            "suggestionFeatureType": t.string(),
            "conversationProfile": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadataOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "columnProperties": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesIn"
                    ]
                )
            ).optional(),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageIn"]
            ).optional(),
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonIn"
                    ]
                )
            ).optional(),
            "rows": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "columnProperties": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageColumnPropertiesOut"
                    ]
                )
            ).optional(),
            "title": t.string(),
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2beta1IntentMessageImageOut"]
            ).optional(),
            "buttons": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOut"
                    ]
                )
            ).optional(),
            "rows": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardRowOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageTableCardOut"])
    types["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"] = t.struct(
        {
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string(),
            "requestBody": t.string().optional(),
            "username": t.string().optional(),
            "webhookType": t.string().optional(),
            "httpMethod": t.string().optional(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "password": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"])
    types["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"] = t.struct(
        {
            "parameterMapping": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string(),
            "requestBody": t.string().optional(),
            "username": t.string().optional(),
            "webhookType": t.string().optional(),
            "httpMethod": t.string().optional(),
            "requestHeaders": t.struct({"_": t.string().optional()}).optional(),
            "allowedCaCerts": t.array(t.string()).optional(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceOut"])
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
    types["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"] = t.struct(
        {"value": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseIn"])
    types["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeExcludedPhraseOut"])
    types["GoogleCloudDialogflowCxV3EntityTypeEntityIn"] = t.struct(
        {"synonyms": t.array(t.string()), "value": t.string()}
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeEntityIn"])
    types["GoogleCloudDialogflowCxV3EntityTypeEntityOut"] = t.struct(
        {
            "synonyms": t.array(t.string()),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3EntityTypeEntityOut"])
    types["GoogleCloudDialogflowV2IntentTrainingPhraseIn"] = t.struct(
        {
            "type": t.string(),
            "timesAddedCount": t.integer().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"])
            ),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhraseIn"])
    types["GoogleCloudDialogflowV2IntentTrainingPhraseOut"] = t.struct(
        {
            "type": t.string(),
            "timesAddedCount": t.integer().optional(),
            "parts": t.array(
                t.proxy(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"])
            ),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhraseOut"])
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
    types["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequestOut"])
    types[
        "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataIn"
    ] = t.struct(
        {
            "participantRole": t.string(),
            "conversationProfile": t.string().optional(),
            "createTime": t.string().optional(),
            "suggestionFeatureType": t.string(),
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
            "participantRole": t.string(),
            "conversationProfile": t.string().optional(),
            "createTime": t.string().optional(),
            "suggestionFeatureType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadataOut"
        ]
    )
    types["GoogleCloudDialogflowV2beta1EventInputIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "languageCode": t.string(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EventInputIn"])
    types["GoogleCloudDialogflowV2beta1EventInputOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "languageCode": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1EventInputOut"])
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
    types["GoogleCloudDialogflowCxV3ExportTestCasesRequestIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "gcsUri": t.string().optional(),
            "dataFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesRequestIn"])
    types["GoogleCloudDialogflowCxV3ExportTestCasesRequestOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "gcsUri": t.string().optional(),
            "dataFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ExportTestCasesRequestOut"])
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
    types["GoogleCloudDialogflowV2beta1ContextIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "lifespanCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ContextIn"])
    types["GoogleCloudDialogflowV2beta1ContextOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "lifespanCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1ContextOut"])
    types["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"] = t.struct(
        {
            "text": t.string(),
            "entityType": t.string().optional(),
            "userDefined": t.boolean().optional(),
            "alias": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartIn"])
    types["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"] = t.struct(
        {
            "text": t.string(),
            "entityType": t.string().optional(),
            "userDefined": t.boolean().optional(),
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentTrainingPhrasePartOut"])
    types["GoogleCloudDialogflowCxV3FormParameterIn"] = t.struct(
        {
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorIn"]
            ),
            "displayName": t.string(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "entityType": t.string(),
            "isList": t.boolean().optional(),
            "required": t.boolean().optional(),
            "redact": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterIn"])
    types["GoogleCloudDialogflowCxV3FormParameterOut"] = t.struct(
        {
            "fillBehavior": t.proxy(
                renames["GoogleCloudDialogflowCxV3FormParameterFillBehaviorOut"]
            ),
            "displayName": t.string(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "entityType": t.string(),
            "isList": t.boolean().optional(),
            "required": t.boolean().optional(),
            "redact": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3FormParameterOut"])
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
    types["GoogleCloudDialogflowCxV3ChangelogIn"] = t.struct(
        {
            "type": t.string().optional(),
            "action": t.string().optional(),
            "createTime": t.string().optional(),
            "userEmail": t.string().optional(),
            "resource": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ChangelogIn"])
    types["GoogleCloudDialogflowCxV3ChangelogOut"] = t.struct(
        {
            "type": t.string().optional(),
            "action": t.string().optional(),
            "createTime": t.string().optional(),
            "userEmail": t.string().optional(),
            "resource": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3ChangelogOut"])
    types["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn"] = t.struct(
        {
            "justCollected": t.boolean().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "required": t.boolean().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoIn"])
    types["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut"] = t.struct(
        {
            "justCollected": t.boolean().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "required": t.boolean().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfoOut"])
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
    types["GoogleCloudDialogflowV2IntentMessageSimpleResponseIn"] = t.struct(
        {
            "textToSpeech": t.string().optional(),
            "displayText": t.string().optional(),
            "ssml": t.string().optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponseIn"])
    types["GoogleCloudDialogflowV2IntentMessageSimpleResponseOut"] = t.struct(
        {
            "textToSpeech": t.string().optional(),
            "displayText": t.string().optional(),
            "ssml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSimpleResponseOut"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardIn"] = t.struct(
        {
            "title": t.string().optional(),
            "imageUri": t.string().optional(),
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardIn"])
    types["GoogleCloudDialogflowV2beta1IntentMessageCardOut"] = t.struct(
        {
            "title": t.string().optional(),
            "imageUri": t.string().optional(),
            "subtitle": t.string().optional(),
            "buttons": t.array(
                t.proxy(
                    renames["GoogleCloudDialogflowV2beta1IntentMessageCardButtonOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2beta1IntentMessageCardOut"])
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
    types["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn"] = t.struct(
        {
            "transitions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionIn"
                    ]
                )
            ).optional(),
            "routeGroup": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupIn"]
            ).optional(),
            "coverageScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageIn"])
    types[
        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut"
    ] = t.struct(
        {
            "transitions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransitionOut"
                    ]
                )
            ).optional(),
            "routeGroup": t.proxy(
                renames["GoogleCloudDialogflowCxV3TransitionRouteGroupOut"]
            ).optional(),
            "coverageScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageOut"]
    )
    types["GoogleCloudDialogflowV2IntentMessageSuggestionIn"] = t.struct(
        {"title": t.string()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSuggestionIn"])
    types["GoogleCloudDialogflowV2IntentMessageSuggestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDialogflowV2IntentMessageSuggestionOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudDialogflowV2IntentMessageIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageIn"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSimpleResponsesIn"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageQuickRepliesIn"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionIn"]
            ).optional(),
            "platform": t.string().optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectIn"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTextIn"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageMediaContentIn"]
            ).optional(),
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageListSelectIn"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSuggestionsIn"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCardIn"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTableCardIn"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardIn"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBasicCardIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageIn"])
    types["GoogleCloudDialogflowV2IntentMessageOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageImageOut"]
            ).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "simpleResponses": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSimpleResponsesOut"]
            ).optional(),
            "quickReplies": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageQuickRepliesOut"]
            ).optional(),
            "linkOutSuggestion": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageLinkOutSuggestionOut"]
            ).optional(),
            "platform": t.string().optional(),
            "carouselSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCarouselSelectOut"]
            ).optional(),
            "text": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTextOut"]
            ).optional(),
            "mediaContent": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageMediaContentOut"]
            ).optional(),
            "listSelect": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageListSelectOut"]
            ).optional(),
            "suggestions": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageSuggestionsOut"]
            ).optional(),
            "card": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageCardOut"]
            ).optional(),
            "tableCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageTableCardOut"]
            ).optional(),
            "browseCarouselCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardOut"]
            ).optional(),
            "basicCard": t.proxy(
                renames["GoogleCloudDialogflowV2IntentMessageBasicCardOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDialogflowV2IntentMessageOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = dialogflow.get(
        "v3/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsPatch"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsDelete"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsList"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsCreate"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSecuritySettingsGet"] = dialogflow.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDialogflowCxV3SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsPatch"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsValidate"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsGet"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsDelete"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsCreate"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsGetValidationResult"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsExport"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsRestore"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsList"] = dialogflow.get(
        "v3/{parent}/agents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListAgentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsDetectIntent"] = dialogflow.post(
        "v3/{session}:fulfillIntent",
        t.struct(
            {
                "session": t.string(),
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
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
    functions["projectsLocationsAgentsSessionsMatchIntent"] = dialogflow.post(
        "v3/{session}:fulfillIntent",
        t.struct(
            {
                "session": t.string(),
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
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
                "matchIntentRequest": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIntentRequestIn"]
                ).optional(),
                "match": t.proxy(
                    renames["GoogleCloudDialogflowCxV3MatchIn"]
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
    functions["projectsLocationsAgentsSessionsEntityTypesGet"] = dialogflow.get(
        "v3/{parent}/entityTypes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsSessionsEntityTypesDelete"] = dialogflow.get(
        "v3/{parent}/entityTypes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsDelete"] = dialogflow.post(
        "v3/{parent}/intents",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "priority": t.integer().optional(),
                "isFallback": t.boolean().optional(),
                "trainingPhrases": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
                ).optional(),
                "parameters": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsPatch"] = dialogflow.post(
        "v3/{parent}/intents",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "priority": t.integer().optional(),
                "isFallback": t.boolean().optional(),
                "trainingPhrases": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
                ).optional(),
                "parameters": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsGet"] = dialogflow.post(
        "v3/{parent}/intents",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "priority": t.integer().optional(),
                "isFallback": t.boolean().optional(),
                "trainingPhrases": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
                ).optional(),
                "parameters": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsList"] = dialogflow.post(
        "v3/{parent}/intents",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "priority": t.integer().optional(),
                "isFallback": t.boolean().optional(),
                "trainingPhrases": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
                ).optional(),
                "parameters": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsIntentsCreate"] = dialogflow.post(
        "v3/{parent}/intents",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "priority": t.integer().optional(),
                "isFallback": t.boolean().optional(),
                "trainingPhrases": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentTrainingPhraseIn"])
                ).optional(),
                "parameters": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3IntentParameterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3IntentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsValidate"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsGetValidationResult"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsGet"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsExport"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPatch"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsCreate"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsTrain"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsImport"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsDelete"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsList"] = dialogflow.get(
        "v3/{parent}/flows",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListFlowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesList"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsPagesDelete"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "form": t.proxy(renames["GoogleCloudDialogflowCxV3FormIn"]).optional(),
                "transitionRoutes": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3TransitionRouteIn"])
                ).optional(),
                "entryFulfillment": t.proxy(
                    renames["GoogleCloudDialogflowCxV3FulfillmentIn"]
                ).optional(),
                "transitionRouteGroups": t.array(t.string()).optional(),
                "eventHandlers": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3EventHandlerIn"])
                ).optional(),
                "displayName": t.string(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsCreate"] = dialogflow.post(
        "v3/{baseVersion}:compareVersions",
        t.struct(
            {
                "baseVersion": t.string(),
                "languageCode": t.string().optional(),
                "targetVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsList"] = dialogflow.post(
        "v3/{baseVersion}:compareVersions",
        t.struct(
            {
                "baseVersion": t.string(),
                "languageCode": t.string().optional(),
                "targetVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsPatch"] = dialogflow.post(
        "v3/{baseVersion}:compareVersions",
        t.struct(
            {
                "baseVersion": t.string(),
                "languageCode": t.string().optional(),
                "targetVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsLoad"] = dialogflow.post(
        "v3/{baseVersion}:compareVersions",
        t.struct(
            {
                "baseVersion": t.string(),
                "languageCode": t.string().optional(),
                "targetVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsDelete"] = dialogflow.post(
        "v3/{baseVersion}:compareVersions",
        t.struct(
            {
                "baseVersion": t.string(),
                "languageCode": t.string().optional(),
                "targetVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsGet"] = dialogflow.post(
        "v3/{baseVersion}:compareVersions",
        t.struct(
            {
                "baseVersion": t.string(),
                "languageCode": t.string().optional(),
                "targetVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsFlowsVersionsCompareVersions"] = dialogflow.post(
        "v3/{baseVersion}:compareVersions",
        t.struct(
            {
                "baseVersion": t.string(),
                "languageCode": t.string().optional(),
                "targetVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3CompareVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsPatch"] = dialogflow.post(
        "v3/{environment}:runContinuousTest",
        t.struct(
            {
                "environment": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsCreate"] = dialogflow.post(
        "v3/{environment}:runContinuousTest",
        t.struct(
            {
                "environment": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsLookupEnvironmentHistory"
    ] = dialogflow.post(
        "v3/{environment}:runContinuousTest",
        t.struct(
            {
                "environment": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsList"] = dialogflow.post(
        "v3/{environment}:runContinuousTest",
        t.struct(
            {
                "environment": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsGet"] = dialogflow.post(
        "v3/{environment}:runContinuousTest",
        t.struct(
            {
                "environment": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDelete"] = dialogflow.post(
        "v3/{environment}:runContinuousTest",
        t.struct(
            {
                "environment": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDeployFlow"] = dialogflow.post(
        "v3/{environment}:runContinuousTest",
        t.struct(
            {
                "environment": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsRunContinuousTest"] = dialogflow.post(
        "v3/{environment}:runContinuousTest",
        t.struct(
            {
                "environment": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsDeploymentsGet"] = dialogflow.get(
        "v3/{parent}/deployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsMatchIntent"
    ] = dialogflow.post(
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
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsFulfillIntent"
    ] = dialogflow.post(
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
    functions[
        "projectsLocationsAgentsEnvironmentsSessionsDetectIntent"
    ] = dialogflow.post(
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
        "projectsLocationsAgentsEnvironmentsSessionsEntityTypesGet"
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsExperimentsCreate"
    ] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "result": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
                ).optional(),
                "rolloutConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
                ).optional(),
                "variantsHistory": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "displayName": t.string(),
                "experimentLength": t.string().optional(),
                "endTime": t.string().optional(),
                "description": t.string().optional(),
                "lastUpdateTime": t.string().optional(),
                "rolloutFailureReason": t.string().optional(),
                "state": t.string().optional(),
                "definition": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "rolloutState": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsStop"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "result": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
                ).optional(),
                "rolloutConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
                ).optional(),
                "variantsHistory": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "displayName": t.string(),
                "experimentLength": t.string().optional(),
                "endTime": t.string().optional(),
                "description": t.string().optional(),
                "lastUpdateTime": t.string().optional(),
                "rolloutFailureReason": t.string().optional(),
                "state": t.string().optional(),
                "definition": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "rolloutState": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAgentsEnvironmentsExperimentsDelete"
    ] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "result": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
                ).optional(),
                "rolloutConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
                ).optional(),
                "variantsHistory": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "displayName": t.string(),
                "experimentLength": t.string().optional(),
                "endTime": t.string().optional(),
                "description": t.string().optional(),
                "lastUpdateTime": t.string().optional(),
                "rolloutFailureReason": t.string().optional(),
                "state": t.string().optional(),
                "definition": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "rolloutState": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsList"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "result": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
                ).optional(),
                "rolloutConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
                ).optional(),
                "variantsHistory": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "displayName": t.string(),
                "experimentLength": t.string().optional(),
                "endTime": t.string().optional(),
                "description": t.string().optional(),
                "lastUpdateTime": t.string().optional(),
                "rolloutFailureReason": t.string().optional(),
                "state": t.string().optional(),
                "definition": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "rolloutState": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsGet"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "result": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
                ).optional(),
                "rolloutConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
                ).optional(),
                "variantsHistory": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "displayName": t.string(),
                "experimentLength": t.string().optional(),
                "endTime": t.string().optional(),
                "description": t.string().optional(),
                "lastUpdateTime": t.string().optional(),
                "rolloutFailureReason": t.string().optional(),
                "state": t.string().optional(),
                "definition": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "rolloutState": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsStart"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "result": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
                ).optional(),
                "rolloutConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
                ).optional(),
                "variantsHistory": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "displayName": t.string(),
                "experimentLength": t.string().optional(),
                "endTime": t.string().optional(),
                "description": t.string().optional(),
                "lastUpdateTime": t.string().optional(),
                "rolloutFailureReason": t.string().optional(),
                "state": t.string().optional(),
                "definition": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "rolloutState": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsEnvironmentsExperimentsPatch"] = dialogflow.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "result": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentResultIn"]
                ).optional(),
                "rolloutConfig": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutConfigIn"]
                ).optional(),
                "variantsHistory": t.array(
                    t.proxy(renames["GoogleCloudDialogflowCxV3VariantsHistoryIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "displayName": t.string(),
                "experimentLength": t.string().optional(),
                "endTime": t.string().optional(),
                "description": t.string().optional(),
                "lastUpdateTime": t.string().optional(),
                "rolloutFailureReason": t.string().optional(),
                "state": t.string().optional(),
                "definition": t.proxy(
                    renames["GoogleCloudDialogflowCxV3ExperimentDefinitionIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "rolloutState": t.proxy(
                    renames["GoogleCloudDialogflowCxV3RolloutStateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksDelete"] = dialogflow.post(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "displayName": t.string(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "disabled": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksGet"] = dialogflow.post(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "displayName": t.string(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "disabled": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksPatch"] = dialogflow.post(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "displayName": t.string(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "disabled": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksList"] = dialogflow.post(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "displayName": t.string(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "disabled": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsWebhooksCreate"] = dialogflow.post(
        "v3/{parent}/webhooks",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "genericWebService": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookGenericWebServiceIn"]
                ).optional(),
                "displayName": t.string(),
                "serviceDirectory": t.proxy(
                    renames["GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfigIn"]
                ).optional(),
                "disabled": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3WebhookOut"]),
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
    functions["projectsLocationsAgentsTestCasesBatchRun"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesBatchDelete"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesExport"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesCalculateCoverage"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesPatch"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesGet"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesCreate"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesImport"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesList"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesRun"] = dialogflow.post(
        "v3/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsTestCasesResultsGet"] = dialogflow.get(
        "v3/{parent}/results",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListTestCaseResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsChangelogsGet"] = dialogflow.get(
        "v3/{parent}/changelogs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListChangelogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAgentsChangelogsList"] = dialogflow.get(
        "v3/{parent}/changelogs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDialogflowCxV3ListChangelogsResponseOut"]),
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
    functions["projectsLocationsOperationsList"] = dialogflow.post(
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
    functions["projectsOperationsCancel"] = dialogflow.get(
        "v3/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dialogflow",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
